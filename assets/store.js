/**
 * PPGCC IFCE Study Hub — Client State Store, Official Edital Formulas & FSRS v5 Engine
 * Pure JS compatible with Browser globals (window.Store / window.PPGCCStore) and Node.js tests.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) {
    module.exports = api;
  }
  if (root) {
    root.PPGCCStore = api;
    root.Store = api;
  }
})(typeof globalThis !== 'undefined' ? globalThis : window, function () {
  'use strict';

  const STORAGE_KEY = 'ppgcc_study_hub_v1';
  const SCHEMA_VERSION = 1;
  const PROVA_ESCRITA_DATE = '2026-12-04';
  const ARGUICAO_START_DATE = '2026-12-14';
  const ARGUICAO_END_DATE = '2026-12-18';

  function roundTo(val, decimals) {
    const factor = Math.pow(10, decimals);
    return Math.round((val + Number.EPSILON) * factor) / factor;
  }

  function isoDateToday(override) {
    if (override) return String(override).slice(0, 10);
    const d = new Date();
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${day}`;
  }

  function addDaysUTC(dateStr, days) {
    const [y, m, d] = dateStr.slice(0, 10).split('-').map(Number);
    const dt = new Date(Date.UTC(y, m - 1, d));
    dt.setUTCDate(dt.getUTCDate() + days);
    return dt.toISOString().slice(0, 10);
  }

  function diffDaysUTC(fromDateStr, toDateStr) {
    const [y1, m1, d1] = fromDateStr.slice(0, 10).split('-').map(Number);
    const [y2, m2, d2] = toDateStr.slice(0, 10).split('-').map(Number);
    const t1 = Date.UTC(y1, m1 - 1, d1);
    const t2 = Date.UTC(y2, m2 - 1, d2);
    return Math.round((t2 - t1) / 86400000);
  }

  // ---------------------------------------------------------------------------
  // 1. Official Formulas (Edital 43/2026 + Retificacao 01 & 02)
  // ---------------------------------------------------------------------------
  function calculateNPE(correctCount) {
    const c = Math.max(0, Math.min(20, Number(correctCount) || 0));
    return roundTo(c * 0.5, 2);
  }

  function calculateDA(ira) {
    const raw = Math.min(10, Math.max(0, Number(ira || 0) - 7.0) * 3.34);
    return roundTo(raw, 4);
  }

  function calculateNC(input) {
    const cfg = input || {};
    const qualisPts = Math.min(30, Math.max(0, Number(cfg.qualisCount || 0)) * 15);
    const semQualisPts = Math.min(30, Math.max(0, Number(cfg.semQualisCount || 0)) * 10);
    const pesquisaPts = Math.min(30, Math.max(0, Number(cfg.pesquisaAnos || 0)) * 10);
    const da = calculateDA(cfg.ira);
    const totalAnexoVI = roundTo(qualisPts + semQualisPts + pesquisaPts + da, 4);
    const nc = roundTo(totalAnexoVI / 10, 4);
    return { qualisPts, semQualisPts, pesquisaPts, da, totalAnexoVI, nc };
  }

  function calculateNF(npe, na, nc) {
    const sum = Number(npe || 0) + Number(na || 0) + Number(nc || 0);
    return roundTo(sum / 3, 2);
  }

  function evaluateCutoff(scores) {
    const s = scores || {};
    if (s.npe !== null && s.npe !== undefined && Number(s.npe) < 3.0) {
      return {
        eliminated: true,
        reason: 'NPE',
        message: 'Eliminado na Prova Escrita (NPE < 3,00).',
      };
    }
    if (s.na !== null && s.na !== undefined && Number(s.na) < 7.0) {
      return {
        eliminated: true,
        reason: 'NA',
        message: 'Eliminado na Arguição Oral (NA < 7,00).',
      };
    }
    return {
      eliminated: false,
      reason: null,
      message: 'Apto (acima dos cortes eliminatórios).',
    };
  }

  // ---------------------------------------------------------------------------
  // 2. Deterministic FSRS v5 Engine
  // ---------------------------------------------------------------------------
  function scheduleCard(card, rating, nowIso) {
    const r = Math.max(1, Math.min(4, Number(rating) || 3));
    const baseDate = isoDateToday(nowIso);
    const prev = card || { reps: 0, lapses: 0, intervalDays: 0, stability: 0, difficulty: 5.0 };

    let intervalDays;
    let stability;
    let difficulty;
    let lapses = prev.lapses || 0;
    const reps = (prev.reps || 0) + 1;

    if (!card || prev.reps === 0) {
      const initialIntervals = { 1: 1, 2: 2, 3: 3, 4: 8 };
      const initialDiffs = { 1: 7.5, 2: 6.2, 3: 5.0, 4: 3.5 };
      intervalDays = initialIntervals[r];
      stability = intervalDays;
      difficulty = initialDiffs[r];
      if (r === 1) lapses += 1;
    } else if (r === 1) {
      intervalDays = 1;
      stability = roundTo(Math.max(1, prev.stability * 0.5), 2);
      difficulty = roundTo(Math.min(10, prev.difficulty + 0.8), 2);
      lapses += 1;
    } else if (r === 2) {
      intervalDays = Math.max(2, Math.round(prev.intervalDays * 1.2));
      stability = roundTo(prev.stability * 1.2, 2);
      difficulty = roundTo(Math.min(10, prev.difficulty + 0.3), 2);
    } else if (r === 3) {
      const mult = 1.8 + (10 - prev.difficulty) * 0.08;
      intervalDays = Math.max(prev.intervalDays + 1, Math.round(prev.intervalDays * mult));
      stability = intervalDays;
      difficulty = roundTo(Math.max(1, prev.difficulty - 0.1), 2);
    } else {
      intervalDays = Math.max(prev.intervalDays + 2, Math.round(prev.intervalDays * 2.5));
      stability = intervalDays;
      difficulty = roundTo(Math.max(1, prev.difficulty - 0.4), 2);
    }

    return {
      reps,
      lapses,
      lastRating: r,
      intervalDays,
      stability,
      difficulty,
      lastReview: baseDate,
      dueDate: addDaysUTC(baseDate, intervalDays),
    };
  }

  // ---------------------------------------------------------------------------
  // 3. Question Helpers & Query Filters
  // ---------------------------------------------------------------------------
  function normalizeOptions(q) {
    if (!q) return [];
    const list = [
      { letter: 'A', text: q.alt_a || '' },
      { letter: 'B', text: q.alt_b || '' },
      { letter: 'C', text: q.alt_c || '' },
      { letter: 'D', text: q.alt_d || '' },
    ];
    if (q.alt_e && String(q.alt_e).trim().length > 0) {
      list.push({ letter: 'E', text: q.alt_e });
    }
    return list;
  }

  function parseQueryFilters(searchStr) {
    const raw = String(searchStr || '').replace(/^\?/, '');
    const params = new URLSearchParams(raw);
    const topicoRaw = params.get('topico');
    const faseRaw = params.get('fase');
    const origemRaw = params.get('origem');
    const modoRaw = params.get('modo');

    const topicoNum = topicoRaw ? Number(topicoRaw) : null;
    const faseNum = faseRaw ? Number(faseRaw) : null;

    return {
      topicoId: Number.isFinite(topicoNum) && topicoNum > 0 ? topicoNum : null,
      faseId: Number.isFinite(faseNum) && faseNum > 0 ? faseNum : null,
      origem: origemRaw ? String(origemRaw).trim() : null,
      modo: modoRaw ? String(modoRaw).trim() : null,
    };
  }

  function filterQuestions(questions, state, filters, todayOverride) {
    const list = Array.isArray(questions) ? questions : [];
    const st = state || {};
    const f = filters || {};
    const today = isoDateToday(todayOverride);
    const answers = st.answers || {};
    const errSet = new Set(st.errorNotebook || []);
    const favSet = new Set(st.favorites || []);
    const cards = st.fsrsCards || {};

    return list.filter((q) => {
      if (f.topicoId && Number(q.topico_id) !== Number(f.topicoId)) return false;
      if (f.faseId && Number(q.fase_id) !== Number(f.faseId)) return false;
      if (f.origem && f.origem !== 'TODAS' && q.origem !== f.origem) return false;
      if (f.nivel && f.nivel !== 'TODOS' && q.nivel !== f.nivel) return false;

      if (f.modo === 'erros') return errSet.has(q.id);
      if (f.modo === 'favoritas') return favSet.has(q.id);
      if (f.modo === 'nao_resolvidas') return !answers[q.id];
      if (f.modo === 'fsrs') {
        const card = cards[q.id];
        return Boolean(card && card.dueDate && card.dueDate <= today);
      }
      return true;
    });
  }

  // ---------------------------------------------------------------------------
  // 4. Countdown & Real Two-Sprint Schedule (Edital 43/2026 + Retificacao 01)
  // ---------------------------------------------------------------------------
  function getCountdown(todayOverride) {
    const today = isoDateToday(todayOverride);
    return {
      today,
      provaEscritaDate: PROVA_ESCRITA_DATE,
      arguicaoStartDate: ARGUICAO_START_DATE,
      arguicaoEndDate: ARGUICAO_END_DATE,
      daysToProvaEscrita: diffDaysUTC(today, PROVA_ESCRITA_DATE),
      daysToArguicaoOral: diffDaysUTC(today, ARGUICAO_START_DATE),
    };
  }

  function buildSprintSchedule(todayOverride) {
    // Sprint 1: 2026-11-23 .. 2026-12-03 (11 dias ponderados por peso da banca: 55% AED, 25% Prog, 20% Logica)
    const sprint1Plan = [
      { date: '2026-11-23', faseId: 1, focus: 'Logica Matematica I: Conjuntos, Relacoes e Propriedades (Topicos 1-4)', topicIds: [1, 2, 3, 4], tipo: 'TEORIA_E_QUESTOES', targetQuestions: 20, minutes: 150 },
      { date: '2026-11-24', faseId: 1, focus: 'Logica Matematica II: Equivalencia, Ordens e Diagramas de Hasse (Topicos 5-8)', topicIds: [5, 6, 7, 8], tipo: 'TEORIA_E_QUESTOES', targetQuestions: 20, minutes: 150 },
      { date: '2026-11-25', faseId: 2, focus: 'Programacao C/Python I: Coercao de Tipos, Controle, Lacos e Teste de Mesa (Topicos 9-12)', topicIds: [9, 10, 11, 12], tipo: 'TEORIA_E_QUESTOES', targetQuestions: 15, minutes: 150 },
      { date: '2026-11-26', faseId: 2, focus: 'Programacao C/Python II: Funcoes, Recursividade, Vetores e Strings (Topicos 13-16)', topicIds: [13, 14, 15, 16], tipo: 'TEORIA_E_QUESTOES', targetQuestions: 15, minutes: 150 },
      { date: '2026-11-27', faseId: 2, focus: 'POO + Simulado Diagnostico 120 min (Prova Oficial 53/2025)', topicIds: [17, 18], tipo: 'SIMULADO_120MIN', targetQuestions: 20, minutes: 180 },
      { date: '2026-11-28', faseId: 3, focus: 'AED Nucleo I: Analise Assintotica, Recorrencias e Series (Topico 19)', topicIds: [19], tipo: 'TEORIA_E_QUESTOES', targetQuestions: 15, minutes: 180 },
      { date: '2026-11-29', faseId: 3, focus: 'AED Nucleo II: Listas Encadeadas, Pilhas LIFO e Filas FIFO (Topicos 20-22)', topicIds: [20, 21, 22], tipo: 'TEORIA_E_QUESTOES', targetQuestions: 20, minutes: 180 },
      { date: '2026-11-30', faseId: 3, focus: 'AED Nucleo III: Arvores BST/AVL e Grafos (Topicos 23-24)', topicIds: [23, 24], tipo: 'TEORIA_E_QUESTOES', targetQuestions: 15, minutes: 180 },
      { date: '2026-12-01', faseId: 3, focus: 'AED Nucleo IV: Ordenacao (Quick/Merge/Quadraticos) e Busca (Topicos 25-26)', topicIds: [25, 26], tipo: 'TEORIA_E_QUESTOES', targetQuestions: 15, minutes: 180 },
      { date: '2026-12-02', faseId: 3, focus: 'AED Nucleo V: Grafos BFS/DFS + Revisao FSRS de Erros', topicIds: [27], tipo: 'REVISAO_FSRS', targetQuestions: 25, minutes: 180 },
      { date: '2026-12-03', faseId: 3, focus: 'Simulado Geral Cronometrado (120 min) + Revisao de Formula/C', topicIds: [1, 9, 19, 20, 21], tipo: 'SIMULADO_120MIN', targetQuestions: 20, minutes: 150 },
    ];

    // Sprint 2: 2026-12-05 .. 2026-12-13 (9 dias dedicados a Arguicao Oral 14-18/12)
    const sprint2Plan = [
      { date: '2026-12-05', faseId: 4, focus: 'CA05 Base I: Arquitetura Kubernetes, Namespaces e Cgroups (Topico 28)', topicIds: [28], tipo: 'TEORIA_ARGUICAO', targetQuestions: 0, minutes: 120 },
      { date: '2026-12-06', faseId: 4, focus: 'CA05 Base II: Requests, Limits e Classes de QoS K8s (Topico 29)', topicIds: [29], tipo: 'TEORIA_ARGUICAO', targetQuestions: 0, minutes: 120 },
      { date: '2026-12-07', faseId: 4, focus: 'Leitura Dirigida I: Google Borg EuroSys 2015 (Topico 30)', topicIds: [30], tipo: 'LEITURA_ARTIGO', targetQuestions: 0, minutes: 150 },
      { date: '2026-12-08', faseId: 4, focus: 'Leitura Dirigida II: Google Autopilot EuroSys 2020 (Topico 31)', topicIds: [31], tipo: 'LEITURA_ARTIGO', targetQuestions: 0, minutes: 150 },
      { date: '2026-12-09', faseId: 4, focus: 'Desempenho: CPU Throttling CFS, OOM-Killer e Mitigacao (Topicos 32-33)', topicIds: [32, 33], tipo: 'TEORIA_ARGUICAO', targetQuestions: 0, minutes: 150 },
      { date: '2026-12-10', faseId: 5, focus: 'DGTI/IFCE I: Mapeamento de Servidores e Gargalos SUAP/Moodle (Topicos 34-35)', topicIds: [34, 35], tipo: 'DEFESA_PRATICA', targetQuestions: 0, minutes: 120 },
      { date: '2026-12-11', faseId: 5, focus: 'DGTI/IFCE II: Tese Central e Desenho Experimental (Topicos 36-37)', topicIds: [36, 37], tipo: 'DEFESA_PRATICA', targetQuestions: 0, minutes: 120 },
      { date: '2026-12-12', faseId: 5, focus: 'Simulado Oral Cronometrado #1 (20 min · 6 perguntas Tipo 1 + Tipo 2)', topicIds: [29, 30, 31, 36], tipo: 'SIMULADO_ORAL', targetQuestions: 0, minutes: 120 },
      { date: '2026-12-13', faseId: 5, focus: 'Simulado Oral Final + Conferencia Documental Anexo VI', topicIds: [32, 33, 37], tipo: 'SIMULADO_ORAL', targetQuestions: 0, minutes: 90 },
    ];

    const today = isoDateToday(todayOverride);
    return {
      today,
      sprint1: sprint1Plan,
      sprint2: sprint2Plan,
      allDays: [...sprint1Plan, ...sprint2Plan],
    };
  }

  // ---------------------------------------------------------------------------
  // 5. Persistent Client Store Factory (localStorage + Backup JSON)
  // ---------------------------------------------------------------------------
  function defaultState() {
    return {
      schemaVersion: SCHEMA_VERSION,
      topicsRead: [],
      answers: {},
      errorNotebook: [],
      favorites: [],
      fsrsCards: {},
      simulados: [],
      arguicaoHistory: [],
      sprintDone: [],
      sprintHoursPerDay: 3,
      curriculo: {
        qualisCount: 0,
        semQualisCount: 0,
        pesquisaAnos: 0,
        ira: 8.5,
      },
      updatedAt: new Date().toISOString(),
    };
  }

  function isValidBackupPayload(obj) {
    if (!obj || typeof obj !== 'object') return false;
    if (obj.schemaVersion !== SCHEMA_VERSION) return false;
    if (!Array.isArray(obj.topicsRead)) return false;
    if (!obj.answers || typeof obj.answers !== 'object') return false;
    if (!obj.fsrsCards || typeof obj.fsrsCards !== 'object') return false;
    return true;
  }

  function createStore(storageBackend, options) {
    const storage =
      storageBackend ||
      (typeof window !== 'undefined' && window.localStorage
        ? window.localStorage
        : {
            _mem: {},
            getItem(k) { return Object.prototype.hasOwnProperty.call(this._mem, k) ? this._mem[k] : null; },
            setItem(k, v) { this._mem[k] = String(v); },
            removeItem(k) { delete this._mem[k]; },
          });

    const opts = options || {};
    const listeners = new Set();

    function load() {
      try {
        const raw = storage.getItem(STORAGE_KEY);
        if (!raw) return defaultState();
        const parsed = JSON.parse(raw);
        if (!isValidBackupPayload(parsed)) return defaultState();
        return Object.assign(defaultState(), parsed);
      } catch (_err) {
        return defaultState();
      }
    }

    let state = load();

    function persist() {
      state.updatedAt = new Date().toISOString();
      storage.setItem(STORAGE_KEY, JSON.stringify(state));
      listeners.forEach((fn) => {
        try { fn(state); } catch (_e) { /* ignore subscriber errors */ }
      });
    }

    function getToday() {
      return isoDateToday(opts.today);
    }

    return {
      getState() {
        return state;
      },
      subscribe(fn) {
        listeners.add(fn);
        return () => listeners.delete(fn);
      },
      isTopicRead(topicId) {
        return state.topicsRead.includes(Number(topicId));
      },
      setTopicRead(topicId, read) {
        const id = Number(topicId);
        const exists = state.topicsRead.includes(id);
        if (read && !exists) state.topicsRead.push(id);
        if (!read && exists) state.topicsRead = state.topicsRead.filter((x) => x !== id);
        persist();
        return this.isTopicRead(id);
      },
      toggleTopicRead(topicId) {
        return this.setTopicRead(topicId, !this.isTopicRead(topicId));
      },
      recordAnswer(questionId, chosenOption, isCorrect, nowIso) {
        const qId = Number(questionId);
        const now = nowIso || new Date().toISOString();
        state.answers[qId] = {
          chosen: String(chosenOption || '').toUpperCase(),
          correct: Boolean(isCorrect),
          answeredAt: now,
        };
        if (!isCorrect) {
          if (!state.errorNotebook.includes(qId)) state.errorNotebook.push(qId);
        }
        persist();
        return state.answers[qId];
      },
      rateFsrsCard(questionId, rating, nowIso) {
        const qId = Number(questionId);
        const updated = scheduleCard(state.fsrsCards[qId] || null, rating, nowIso || getToday());
        state.fsrsCards[qId] = updated;
        persist();
        return updated;
      },
      toggleErrorNotebook(questionId) {
        const qId = Number(questionId);
        if (state.errorNotebook.includes(qId)) {
          state.errorNotebook = state.errorNotebook.filter((x) => x !== qId);
        } else {
          state.errorNotebook.push(qId);
        }
        persist();
        return state.errorNotebook.includes(qId);
      },
      toggleFavorite(questionId) {
        const qId = Number(questionId);
        if (state.favorites.includes(qId)) {
          state.favorites = state.favorites.filter((x) => x !== qId);
        } else {
          state.favorites.push(qId);
        }
        persist();
        return state.favorites.includes(qId);
      },
      saveSimulado(session) {
        state.simulados.unshift(Object.assign({ createdAt: new Date().toISOString() }, session));
        persist();
      },
      saveArguicao(session) {
        state.arguicaoHistory.unshift(Object.assign({ createdAt: new Date().toISOString() }, session));
        persist();
      },
      updateCurriculo(cfg) {
        state.curriculo = Object.assign({}, state.curriculo, cfg);
        persist();
        return calculateNC(state.curriculo);
      },
      toggleSprintDay(dateStr) {
        if (state.sprintDone.includes(dateStr)) {
          state.sprintDone = state.sprintDone.filter((d) => d !== dateStr);
        } else {
          state.sprintDone.push(dateStr);
        }
        persist();
        return state.sprintDone.includes(dateStr);
      },
      setSprintHoursPerDay(hours) {
        state.sprintHoursPerDay = Math.max(1, Math.min(12, Number(hours) || 3));
        persist();
      },
      getDueFsrsIds(questions, todayOverride) {
        const today = isoDateToday(todayOverride || opts.today);
        const qSet = questions ? new Set(questions.map((q) => q.id)) : null;
        return Object.entries(state.fsrsCards)
          .filter(([id, card]) => {
            if (qSet && !qSet.has(Number(id))) return false;
            return card && card.dueDate && card.dueDate <= today;
          })
          .map(([id]) => Number(id));
      },
      getTodaySprintBlock(todayOverride) {
        const today = isoDateToday(todayOverride || opts.today);
        const sched = buildSprintSchedule(today);
        const exact = sched.allDays.find((d) => d.date === today);
        if (exact) return exact;
        if (today === PROVA_ESCRITA_DATE) {
          return {
            date: PROVA_ESCRITA_DATE,
            faseId: 3,
            focus: 'DIA DA PROVA ESCRITA PRESENCIAL (20 questoes em 120 min)',
            topicIds: [],
            tipo: 'DIA_PROVA',
            targetQuestions: 20,
            minutes: 120,
          };
        }
        const nextUpcoming = sched.allDays.find((d) => d.date > today && !state.sprintDone.includes(d.date));
        return nextUpcoming || sched.sprint1[0];
      },
      getStats() {
        const answerVals = Object.values(state.answers);
        const totalAnswered = answerVals.length;
        const totalCorrect = answerVals.filter((a) => a.correct).length;
        const accuracyPct = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;

        const latestNPE = state.simulados.length > 0 ? state.simulados[0].npe : calculateNPE(Math.round((accuracyPct / 100) * 20));
        const latestNA = state.arguicaoHistory.length > 0 ? state.arguicaoHistory[0].na : 0;
        const ncObj = calculateNC(state.curriculo);
        const nf = calculateNF(latestNPE, latestNA, ncObj.nc);

        return {
          topicsCompleted: state.topicsRead.length,
          totalAnswered,
          totalCorrect,
          accuracyPct,
          errorCount: state.errorNotebook.length,
          favoriteCount: state.favorites.length,
          dueFsrsCount: this.getDueFsrsIds().length,
          latestNPE,
          latestNA,
          nc: ncObj.nc,
          projectedNF: nf,
        };
      },
      exportBackup() {
        return JSON.stringify(
          Object.assign({}, state, { exportedAt: new Date().toISOString() }),
          null,
          2
        );
      },
      importBackup(jsonText) {
        try {
          const parsed = JSON.parse(jsonText);
          if (!isValidBackupPayload(parsed)) {
            return { ok: false, error: 'Formato ou versao de backup invalida.' };
          }
          state = Object.assign(defaultState(), parsed);
          persist();
          return { ok: true };
        } catch (err) {
          return { ok: false, error: 'JSON malformado: ' + err.message };
        }
      },
      resetAll() {
        state = defaultState();
        persist();
      },
    };
  }

  return {
    STORAGE_KEY,
    SCHEMA_VERSION,
    PROVA_ESCRITA_DATE,
    ARGUICAO_START_DATE,
    ARGUICAO_END_DATE,
    calculateNPE,
    calculateDA,
    calculateNC,
    calculateNF,
    evaluateCutoff,
    scheduleCard,
    normalizeOptions,
    parseQueryFilters,
    filterQuestions,
    getCountdown,
    buildSprintSchedule,
    createStore,
  };
});
