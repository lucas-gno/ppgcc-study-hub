import test from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const StoreApi = require('../assets/store.js');

const {
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
} = StoreApi;

function makeMemoryStorage(initial = {}) {
  const map = new Map(Object.entries(initial));
  return {
    getItem(k) {
      return map.has(k) ? map.get(k) : null;
    },
    setItem(k, v) {
      map.set(k, String(v));
    },
    removeItem(k) {
      map.delete(k);
    },
  };
}

test('Official Edital 43/2026 + Retificacao 02 score formulas', () => {
  assert.equal(calculateNPE(17), 8.5);
  assert.equal(calculateNPE(6), 3.0);
  assert.equal(calculateNPE(5), 2.5);

  assert.equal(calculateDA(6.5), 0);
  assert.equal(calculateDA(7.0), 0);
  assert.equal(calculateDA(8.5), 5.01);
  assert.equal(calculateDA(10.0), 10);

  // Caps: Qualis <= 30, Sem Qualis <= 30, Pesquisa <= 30, DA <= 10
  const ncResult = calculateNC({
    qualisCount: 5,       // 5*15=75 -> capped at 30
    semQualisCount: 1,    // 1*10=10
    pesquisaAnos: 3,      // 3*10=30
    ira: 8.5,             // DA = 5.01
  });
  assert.equal(ncResult.da, 5.01);
  assert.equal(ncResult.totalAnexoVI, 75.01);
  assert.equal(ncResult.nc, 7.501);

  assert.equal(calculateNF(8.5, 9.2, 7.5), 8.4);

  const cutNpe = evaluateCutoff({ npe: 2.5, na: 8.5 });
  assert.equal(cutNpe.eliminated, true);
  assert.equal(cutNpe.reason, 'NPE');

  const cutNa = evaluateCutoff({ npe: 8.0, na: 6.5 });
  assert.equal(cutNa.eliminated, true);
  assert.equal(cutNa.reason, 'NA');

  const pass = evaluateCutoff({ npe: 8.5, na: 9.2 });
  assert.equal(pass.eliminated, false);
});

test('Deterministic FSRS v5 scheduling respects ratings 1..4', () => {
  const now = '2026-11-22T12:00:00.000Z';
  const fresh = null;

  const again = scheduleCard(fresh, 1, now);
  const hard = scheduleCard(fresh, 2, now);
  const good = scheduleCard(fresh, 3, now);
  const easy = scheduleCard(fresh, 4, now);

  assert.equal(again.intervalDays, 1);
  assert.equal(hard.intervalDays, 2);
  assert.equal(good.intervalDays, 3);
  assert.equal(easy.intervalDays, 8);
  assert.equal(good.dueDate, '2026-11-25');
  assert.equal(easy.dueDate, '2026-11-30');

  // Repeating Good increases interval further
  const secondGood = scheduleCard(good, 3, '2026-11-25T12:00:00.000Z');
  assert.ok(secondGood.intervalDays > good.intervalDays);
});

test('normalizeOptions returns 4 options when alt_e is empty and 5 when populated', () => {
  const q4 = { alt_a: 'A1', alt_b: 'B1', alt_c: 'C1', alt_d: 'D1', alt_e: '' };
  const q5 = { alt_a: 'A2', alt_b: 'B2', alt_c: 'C2', alt_d: 'D2', alt_e: 'E2' };

  assert.deepEqual(
    normalizeOptions(q4).map((o) => o.letter),
    ['A', 'B', 'C', 'D'],
  );
  assert.deepEqual(
    normalizeOptions(q5).map((o) => o.letter),
    ['A', 'B', 'C', 'D', 'E'],
  );
});

test('Real countdown and two-sprint schedule match Retificacao 01 dates', () => {
  const cd = getCountdown('2026-11-22');
  assert.equal(cd.daysToProvaEscrita, 12);
  assert.equal(cd.daysToArguicaoOral, 22);

  const schedule = buildSprintSchedule('2026-11-22');
  assert.equal(schedule.sprint1.length, 11); // 2026-11-23 .. 2026-12-03
  assert.equal(schedule.sprint1[0].date, '2026-11-23');
  assert.equal(schedule.sprint1[schedule.sprint1.length - 1].date, '2026-12-03');

  assert.equal(schedule.sprint2.length, 9); // 2026-12-05 .. 2026-12-13
  assert.equal(schedule.sprint2[0].date, '2026-12-05');
  assert.equal(schedule.sprint2[schedule.sprint2.length - 1].date, '2026-12-13');
});

test('Query filter parser and question filters work for topic/origin/mode', () => {
  const parsed = parseQueryFilters('?topico=8&origem=PROVA_53_2025&modo=erros');
  assert.equal(parsed.topicoId, 8);
  assert.equal(parsed.origem, 'PROVA_53_2025');
  assert.equal(parsed.modo, 'erros');

  const sampleQuestions = [
    { id: 1, topico_id: 8, fase_id: 1, origem: 'INEDITAS' },
    { id: 2, topico_id: 19, fase_id: 3, origem: 'PROVA_53_2025' },
    { id: 3, topico_id: 8, fase_id: 1, origem: 'PROVA_53_2025' },
  ];
  const state = {
    answers: { 1: { correct: false }, 2: { correct: true } },
    errorNotebook: [1],
    favorites: [2],
    fsrsCards: { 3: { dueDate: '2026-11-22' }, 2: { dueDate: '2026-12-01' } },
  };

  assert.deepEqual(
    filterQuestions(sampleQuestions, state, { topicoId: 8 }, '2026-11-22').map((q) => q.id),
    [1, 3],
  );
  assert.deepEqual(
    filterQuestions(sampleQuestions, state, { modo: 'fsrs' }, '2026-11-22').map((q) => q.id),
    [3],
  );
  assert.deepEqual(
    filterQuestions(sampleQuestions, state, { modo: 'erros' }, '2026-11-22').map((q) => q.id),
    [1],
  );
  assert.deepEqual(
    filterQuestions(sampleQuestions, state, { origem: 'PROVA_53_2025' }, '2026-11-22').map((q) => q.id),
    [2, 3],
  );
});

test('Store persists state, toggles topics/favorites, and safely validates Backup JSON round-trip', () => {
  const storage = makeMemoryStorage();
  const store = createStore(storage, { today: '2026-11-22' });

  store.toggleTopicRead(1);
  assert.equal(store.isTopicRead(1), true);

  store.recordAnswer(10, 'B', true);
  store.rateFsrsCard(10, 3, '2026-11-22T10:00:00.000Z');
  assert.equal(store.getStats().totalAnswered, 1);
  assert.equal(store.getStats().totalCorrect, 1);

  const backupJson = store.exportBackup();

  // New storage restored from backup
  const storage2 = makeMemoryStorage();
  const store2 = createStore(storage2, { today: '2026-11-22' });
  assert.equal(store2.isTopicRead(1), false);

  const importOk = store2.importBackup(backupJson);
  assert.equal(importOk.ok, true);
  assert.equal(store2.isTopicRead(1), true);
  assert.equal(store2.getStats().totalCorrect, 1);

  // Reject malformed or wrong schema backup without wiping existing data
  const bad = store2.importBackup('{"invalid": true}');
  assert.equal(bad.ok, false);
  assert.equal(store2.isTopicRead(1), true);
});

test('Combined faseId + nao_resolvidas + favoritas filters and due FSRS updates work cleanly', () => {
  const qs = [
    { id: 101, topico_id: 1, fase_id: 1, origem: 'INEDITAS' },
    { id: 102, topico_id: 2, fase_id: 1, origem: 'PROVA_53_2025' },
    { id: 103, topico_id: 19, fase_id: 3, origem: 'PROVA_53_2025' },
  ];
  const storage = makeMemoryStorage();
  const store = createStore(storage, { today: '2026-11-22' });

  store.recordAnswer(101, 'A', false, '2026-11-22T10:00:00.000Z');
  store.toggleFavorite(102);
  store.rateFsrsCard(102, 1, '2026-11-22T10:00:00.000Z'); // due 2026-11-23
  store.rateFsrsCard(101, 1, '2026-11-20T10:00:00.000Z'); // due 2026-11-21 (due today!)

  const st = store.getState();
  assert.deepEqual(
    filterQuestions(qs, st, { faseId: 1, modo: 'nao_resolvidas' }, '2026-11-22').map((q) => q.id),
    [102],
  );
  assert.deepEqual(
    filterQuestions(qs, st, { modo: 'favoritas' }, '2026-11-22').map((q) => q.id),
    [102],
  );
  assert.deepEqual(store.getDueFsrsIds(qs, '2026-11-22'), [101]);
  assert.deepEqual(store.getDueFsrsIds(qs, '2026-11-23'), [101, 102]);
});
