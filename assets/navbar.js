/**
 * PPGCC IFCE Study Hub — Unified Minimalist Top Navbar & Portable Backup Modal
 * Renders clean Apple HIG / Emil Kowalski navigation across all MPA pages.
 */
(function (root) {
  'use strict';

  function detectPrefix() {
    const p = (root.location && root.location.pathname) || '';
    if (p.includes('/lessons/') || p.includes('/reference/')) return '../';
    return './';
  }

  function currentPageKey() {
    const p = ((root.location && root.location.pathname) || '').toLowerCase();
    if (p.endsWith('edital.html')) return 'edital';
    if (p.endsWith('cronograma.html')) return 'cronograma';
    if (p.endsWith('questoes.html')) return 'questoes';
    if (p.endsWith('simulados.html')) return 'simulados';
    if (p.endsWith('arguicao.html')) return 'arguicao';
    if (p.endsWith('curriculo.html')) return 'curriculo';
    if (p.includes('/lessons/')) return 'edital';
    return 'hoje';
  }

  function initNavbar(options) {
    const opts = options || {};
    const prefix = opts.prefix || detectPrefix();
    const active = opts.active || currentPageKey();
    const I = root.PPGCCIcons || {};
    const icon = (name, sz) => (I[name] ? I[name](sz || 16) : '');

    const store = root.PPGCCStore
      ? (root.__ppgccStoreInstance || (root.__ppgccStoreInstance = root.PPGCCStore.createStore()))
      : null;

    const countdown = root.PPGCCStore ? root.PPGCCStore.getCountdown() : { daysToProvaEscrita: 12 };
    const daysText =
      countdown.daysToProvaEscrita > 0
        ? `04/12 · ${countdown.daysToProvaEscrita}d`
        : countdown.daysToProvaEscrita === 0
        ? 'Prova Hoje'
        : 'Pós-Escrita';

    const navItems = [
      { key: 'hoje', label: 'Hoje', href: `${prefix}index.html`, icon: 'home' },
      { key: 'edital', label: 'Edital', href: `${prefix}edital.html`, icon: 'book' },
      { key: 'cronograma', label: 'Cronograma', href: `${prefix}cronograma.html`, icon: 'calendar' },
      { key: 'questoes', label: 'Questões', href: `${prefix}questoes.html`, icon: 'checkSquare' },
      { key: 'simulados', label: 'Simulados', href: `${prefix}simulados.html`, icon: 'clock' },
    ];

    const header = document.createElement('header');
    header.className = 'hub-navbar';
    header.innerHTML = `
      <div class="hub-navbar-inner">
        <a class="hub-brand" href="${prefix}index.html">
          <span class="hub-brand-mark">${icon('layers', 17)}</span>
          <span class="hub-brand-text">PPGCC IFCE</span>
          <span class="hub-countdown-pill">${daysText}</span>
        </a>
        <nav class="hub-nav-links" aria-label="Navegação principal">
          ${navItems
            .map(
              (item) => `
            <a href="${item.href}" class="hub-nav-link ${item.key === active ? 'is-active' : ''}">
              ${icon(item.icon, 15)}
              <span>${item.label}</span>
            </a>`
            )
            .join('')}
        </nav>
        <div class="hub-nav-actions">
          <button type="button" class="hub-btn-ghost" id="hub-open-backup-btn">
            ${icon('database', 15)}
            <span>Backup</span>
          </button>
          <button type="button" class="hub-btn-ghost hub-mobile-menu-btn" id="hub-mobile-menu-btn" aria-label="Abrir menu">
            ${icon('menu', 18)}
          </button>
        </div>
      </div>
      <div class="hub-mobile-drawer" id="hub-mobile-drawer" hidden>
        ${navItems
          .map(
            (item) => `
          <a href="${item.href}" class="hub-mobile-link ${item.key === active ? 'is-active' : ''}">
            ${icon(item.icon, 16)}
            <span>${item.label}</span>
          </a>`
          )
          .join('')}
      </div>
    `;

    // Insert at top of body
    document.body.insertBefore(header, document.body.firstChild);

    // Mobile drawer toggle
    const mobileBtn = header.querySelector('#hub-mobile-menu-btn');
    const mobileDrawer = header.querySelector('#hub-mobile-drawer');
    if (mobileBtn && mobileDrawer) {
      mobileBtn.addEventListener('click', () => {
        const isHidden = mobileDrawer.hasAttribute('hidden');
        if (isHidden) mobileDrawer.removeAttribute('hidden');
        else mobileDrawer.setAttribute('hidden', '');
      });
    }

    // Backup Modal
    const modal = document.createElement('div');
    modal.className = 'hub-modal-backdrop';
    modal.id = 'hub-backup-modal';
    modal.setAttribute('hidden', '');
    modal.innerHTML = `
      <div class="hub-modal" role="dialog" aria-modal="true" aria-labelledby="hub-backup-title">
        <div class="hub-modal-header">
          <div>
            <h3 id="hub-backup-title">Backup e Sincronização Portável</h3>
            <p class="hub-muted">Exporte seu progresso em JSON para continuar em outro dispositivo sem servidor.</p>
          </div>
          <button type="button" class="hub-icon-close" id="hub-close-backup-btn" aria-label="Fechar">${icon('x', 18)}</button>
        </div>
        <div class="hub-modal-body">
          <div class="hub-backup-stats" id="hub-backup-stats"></div>
          <div class="hub-backup-actions">
            <button type="button" class="hub-btn-primary" id="hub-export-json-btn">
              ${icon('download', 16)}
              <span>Exportar Backup JSON</span>
            </button>
            <label class="hub-btn-secondary hub-file-label">
              ${icon('upload', 16)}
              <span>Importar Backup JSON</span>
              <input type="file" id="hub-import-json-input" accept="application/json,.json" hidden>
            </label>
          </div>
          <div id="hub-backup-feedback" class="hub-feedback-msg" hidden></div>
          <div class="hub-danger-zone">
            <button type="button" class="hub-btn-danger-ghost" id="hub-reset-progress-btn">
              ${icon('rotateCcw', 15)}
              <span>Limpar todo o progresso local</span>
            </button>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    function refreshBackupStats() {
      const box = modal.querySelector('#hub-backup-stats');
      if (!box || !store) return;
      const st = store.getStats();
      box.innerHTML = `
        <div class="hub-mini-stat"><span>Tópicos lidos</span><strong>${st.topicsCompleted} / 37</strong></div>
        <div class="hub-mini-stat"><span>Questões respondidas</span><strong>${st.totalAnswered}</strong></div>
        <div class="hub-mini-stat"><span>Cards FSRS</span><strong>${Object.keys(store.getState().fsrsCards).length}</strong></div>
      `;
    }

    function openModal() {
      refreshBackupStats();
      const fb = modal.querySelector('#hub-backup-feedback');
      if (fb) fb.setAttribute('hidden', '');
      modal.removeAttribute('hidden');
    }
    function closeModal() {
      modal.setAttribute('hidden', '');
    }

    header.querySelector('#hub-open-backup-btn').addEventListener('click', openModal);
    modal.querySelector('#hub-close-backup-btn').addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !modal.hasAttribute('hidden')) closeModal();
    });

    modal.querySelector('#hub-export-json-btn').addEventListener('click', () => {
      if (!store) return;
      const json = store.exportBackup();
      const blob = new Blob([json], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      const stamp = new Date().toISOString().slice(0, 10);
      a.href = url;
      a.download = `ppgcc-study-hub-backup-${stamp}.json`;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
      const fb = modal.querySelector('#hub-backup-feedback');
      fb.textContent = 'Backup exportado com sucesso.';
      fb.className = 'hub-feedback-msg is-ok';
      fb.removeAttribute('hidden');
    });

    modal.querySelector('#hub-import-json-input').addEventListener('change', (e) => {
      const file = e.target.files && e.target.files[0];
      if (!file || !store) return;
      const reader = new FileReader();
      reader.onload = () => {
        const res = store.importBackup(String(reader.result || ''));
        const fb = modal.querySelector('#hub-backup-feedback');
        if (res.ok) {
          fb.textContent = 'Backup restaurado. Recarregando visualização...';
          fb.className = 'hub-feedback-msg is-ok';
          fb.removeAttribute('hidden');
          setTimeout(() => root.location.reload(), 400);
        } else {
          fb.textContent = res.error || 'Falha ao importar backup.';
          fb.className = 'hub-feedback-msg is-err';
          fb.removeAttribute('hidden');
        }
      };
      reader.readAsText(file);
    });

    let resetArmed = false;
    const resetBtn = modal.querySelector('#hub-reset-progress-btn');
    resetBtn.addEventListener('click', () => {
      if (!store) return;
      if (!resetArmed) {
        resetArmed = true;
        resetBtn.querySelector('span').textContent = 'Clique novamente para confirmar limpeza';
        setTimeout(() => {
          resetArmed = false;
          const sp = resetBtn.querySelector('span');
          if (sp) sp.textContent = 'Limpar todo o progresso local';
        }, 3500);
        return;
      }
      store.resetAll();
      root.location.reload();
    });

    return { store };
  }

  root.PPGCCNavbar = { init: initNavbar };
})(typeof window !== 'undefined' ? window : globalThis);
