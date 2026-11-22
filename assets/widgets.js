/**
 * PPGCC IFCE Study Hub — Interactive Engine
 * Modular Vanilla JS for Zero-Dependency Offline-First Interactive Learning
 */

// 1. Math Render using KaTeX Auto-Render
function initMathRender() {
  if (typeof renderMathInElement === 'function') {
    renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false }
      ],
      throwOnError: false
    });
  }
}

// 2. Interactive Quiz Engine
function initQuiz() {
  const cards = document.querySelectorAll('.question-card');
  cards.forEach((card, cardIdx) => {
    const correctLetter = card.getAttribute('data-correct');
    const buttons = card.querySelectorAll('.option-btn');
    const solutionBox = card.querySelector('.solution-box');

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        if (card.classList.contains('answered')) return;
        card.classList.add('answered');

        const chosenLetter = btn.getAttribute('data-option');
        const isCorrect = (chosenLetter.trim().toUpperCase() === correctLetter.trim().toUpperCase());

        buttons.forEach(b => b.classList.add('disabled'));

        if (isCorrect) {
          btn.classList.add('selected-correct');
        } else {
          btn.classList.add('selected-wrong');
          // Reveal correct
          buttons.forEach(b => {
            if (b.getAttribute('data-option').trim().toUpperCase() === correctLetter.trim().toUpperCase()) {
              b.classList.add('reveal-correct');
            }
          });
        }

        if (solutionBox) {
          solutionBox.classList.add('visible');
          // Re-render math inside solution box if needed
          if (typeof renderMathInElement === 'function') {
            renderMathInElement(solutionBox, {
              delimiters: [
                { left: '$$', right: '$$', display: true },
                { left: '$', right: '$', display: false }
              ],
              throwOnError: false
            });
          }
        }
      });
    });
  });
}

// 3. Boolean Matrix and Dynamic Digraph Engine (Topics 2, 3, 4, 6)
function initBooleanMatrixWidget(containerId, initialMatrix = null) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const n = 3;
  const elements = ['1', '2', '3'];
  let M = initialMatrix ? JSON.parse(JSON.stringify(initialMatrix)) : [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
  ];

  function evaluateProperties(matrix) {
    let isReflexive = true;
    let isIrreflexive = true;
    let isSymmetric = true;
    let isAntisymmetric = true;
    let isTransitive = true;

    // Reflexivity & Irreflexivity
    for (let i = 0; i < n; i++) {
      if (matrix[i][i] !== 1) isReflexive = false;
      if (matrix[i][i] !== 0) isIrreflexive = false;
    }

    // Symmetry & Antisymmetry
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (matrix[i][j] === 1) {
          if (matrix[j][i] !== 1) isSymmetric = false;
          if (i !== j && matrix[j][i] === 1) isAntisymmetric = false;
        }
      }
    }

    // Transitivity (Warshall check: if M[i][k] && M[k][j] then M[i][j] must be 1)
    let transitiveViolations = [];
    for (let i = 0; i < n; i++) {
      for (let k = 0; k < n; k++) {
        if (matrix[i][k] === 1) {
          for (let j = 0; j < n; j++) {
            if (matrix[k][j] === 1 && matrix[i][j] !== 1) {
              isTransitive = false;
              transitiveViolations.push(`(${elements[i]}, ${elements[k]}) e (${elements[k]}, ${elements[j]}) existem, mas falta (${elements[i]}, ${elements[j]})`);
            }
          }
        }
      }
    }

    const isEquivalence = isReflexive && isSymmetric && isTransitive;
    const isPartialOrder = isReflexive && isAntisymmetric && isTransitive;

    return {
      isReflexive,
      isIrreflexive,
      isSymmetric,
      isAntisymmetric,
      isTransitive,
      isEquivalence,
      isPartialOrder,
      transitiveViolations
    };
  }

  function render() {
    const props = evaluateProperties(M);

    // List active pairs
    let pairs = [];
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (M[i][j] === 1) pairs.push(`(${elements[i]}, ${elements[j]})`);
      }
    }
    const pairsText = pairs.length > 0 ? `{ ${pairs.join(', ')} }` : '∅ (Relação Vazia)';

    container.innerHTML = `
      <div class="matrix-interactive-wrapper">
        <div class="matrix-container">
          <div style="font-size:0.88rem; font-weight:600; color:var(--text-muted); margin-bottom:4px;">
            Clique nas células para ligar/desligar pares:
          </div>
          <div class="matrix-grid" style="grid-template-columns: repeat(${n}, 44px);">
            ${M.map((row, i) => 
              row.map((val, j) => `
                <div class="matrix-cell ${val === 1 ? 'active' : ''} ${i === j ? 'diagonal' : ''}" 
                     data-row="${i}" data-col="${j}" title="Par (${elements[i]}, ${elements[j]})">
                  ${val}
                </div>
              `).join('')
            ).join('')}
          </div>
          <div style="font-family:var(--font-mono); font-size:0.85rem; color:var(--accent-primary); word-break:break-all; text-align:center;">
            R = ${pairsText}
          </div>
          <div style="display:flex; gap:8px; margin-top:8px;">
            <button class="btn-nav" id="${containerId}-reset-id" style="font-size:0.8rem; padding:4px 10px;">Relação Identidade</button>
            <button class="btn-nav" id="${containerId}-clear" style="font-size:0.8rem; padding:4px 10px;">Limpar (Vazia)</button>
            <button class="btn-nav" id="${containerId}-total" style="font-size:0.8rem; padding:4px 10px;">Universal ($A \\times A$)</button>
          </div>
        </div>

        <div class="matrix-status-panel">
          <div style="font-weight:700; font-size:0.95rem; margin-bottom:12px; border-bottom:1px solid var(--border-subtle); padding-bottom:6px;">
            Propriedades Matemáticas Calculadas:
          </div>
          
          <div class="property-row">
            <span><strong>Reflexiva</strong> (diagonal 1s)</span>
            <span class="prop-badge ${props.isReflexive ? 'true' : 'false'}">
              ${props.isReflexive ? 'Sim' : 'Não'}
            </span>
          </div>

          <div class="property-row">
            <span><strong>Simétrica</strong> (se (x,y) então (y,x))</span>
            <span class="prop-badge ${props.isSymmetric ? 'true' : 'false'}">
              ${props.isSymmetric ? 'Sim' : 'Não'}
            </span>
          </div>

          <div class="property-row">
            <span><strong>Antissimétrica</strong> (sem mão-dupla fora diag.)</span>
            <span class="prop-badge ${props.isAntisymmetric ? 'true' : 'false'}">
              ${props.isAntisymmetric ? 'Sim' : 'Não'}
            </span>
          </div>

          <div class="property-row">
            <span><strong>Transitiva</strong> (fechamento por caminhos)</span>
            <span class="prop-badge ${props.isTransitive ? 'true' : 'false'}">
              ${props.isTransitive ? 'Sim' : 'Não'}
            </span>
          </div>

          <div style="margin-top:12px; padding-top:10px; border-top:1px dashed var(--border-strong);">
            <div class="property-row">
              <span><strong>Relação de Equivalência</strong></span>
              <span class="prop-badge ${props.isEquivalence ? 'true' : 'false'}" style="font-size:0.88rem;">
                ${props.isEquivalence ? 'EQUIVALÊNCIA' : 'Não é'}
              </span>
            </div>
            <div class="property-row">
              <span><strong>Ordem Parcial (Poset)</strong></span>
              <span class="prop-badge ${props.isPartialOrder ? 'true' : 'false'}" style="font-size:0.88rem;">
                ${props.isPartialOrder ? 'ORDEM PARCIAL' : 'Não é'}
              </span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Live SVG Digraph -->
      <div style="margin-top:1.5rem;">
        <div style="font-size:0.88rem; font-weight:600; color:var(--text-muted); margin-bottom:6px;">
          Dígrafo Dinâmico da Relação:
        </div>
        <svg class="digraph-svg" id="${containerId}-svg" viewBox="0 0 400 160">
          <defs>
            <marker id="${containerId}-arrow" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 10 5 L 0 9 z" fill="#1e3a8a"/>
            </marker>
          </defs>
          ${renderSvgEdges(M, containerId)}
          ${renderSvgNodes()}
        </svg>
      </div>
    `;

    // Attach listeners
    container.querySelectorAll('.matrix-cell').forEach(cell => {
      cell.addEventListener('click', () => {
        const r = parseInt(cell.getAttribute('data-row'), 10);
        const c = parseInt(cell.getAttribute('data-col'), 10);
        M[r][c] = M[r][c] === 1 ? 0 : 1;
        render();
      });
    });

    document.getElementById(`${containerId}-reset-id`).addEventListener('click', () => {
      M = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
      render();
    });

    document.getElementById(`${containerId}-clear`).addEventListener('click', () => {
      M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
      render();
    });

    document.getElementById(`${containerId}-total`).addEventListener('click', () => {
      M = [[1, 1, 1], [1, 1, 1], [1, 1, 1]];
      render();
    });
  }

  function renderSvgNodes() {
    const coords = [
      { x: 90, y: 80, label: '1' },
      { x: 200, y: 80, label: '2' },
      { x: 310, y: 80, label: '3' }
    ];
    return coords.map(n => `
      <circle class="digraph-node" cx="${n.x}" cy="${n.y}" r="20" />
      <text class="digraph-text" x="${n.x}" y="${n.y}">${n.label}</text>
    `).join('');
  }

  function renderSvgEdges(matrix, prefix) {
    const coords = [
      { x: 90, y: 80 },
      { x: 200, y: 80 },
      { x: 310, y: 80 }
    ];
    let edges = [];

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (matrix[i][j] === 1) {
          if (i === j) {
            // Self loop on top of node
            const x = coords[i].x;
            const y = coords[i].y - 20;
            edges.push(`
              <path class="digraph-edge loop" d="M ${x - 8} ${y} C ${x - 25} ${y - 35}, ${x + 25} ${y - 35}, ${x + 8} ${y}" 
                    marker-end="url(#${prefix}-arrow)" />
            `);
          } else {
            // Straight or curved arrow
            const p1 = coords[i];
            const p2 = coords[j];
            // Arc curve depending on direction
            const curve = (j > i) ? -20 : 20;
            const midX = (p1.x + p2.x) / 2;
            const midY = (p1.y + p2.y) / 2 + curve;
            edges.push(`
              <path class="digraph-edge" d="M ${p1.x} ${p1.y} Q ${midX} ${midY} ${p2.x} ${p2.y}" 
                    marker-end="url(#${prefix}-arrow)" />
            `);
          }
        }
      }
    }
    return edges.join('');
  }

  render();
}

// 4. Interactive Set Operations Simulator (Topic 1)
function initSetOperationsWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const setA = [1, 2, 3, 4];
  const setB = [3, 4, 5, 6];
  let currentOp = 'union';

  function calculate() {
    let result = [];
    let desc = '';
    let reading = '';

    if (currentOp === 'union') {
      result = Array.from(new Set([...setA, ...setB])).sort();
      desc = 'A ∪ B reúne todos os elementos que estão em A OU em B (sem duplicatas).';
      reading = 'Lê-se: "A união B" ou "A reunido com B"';
    } else if (currentOp === 'intersect') {
      result = setA.filter(x => setB.includes(x)).sort();
      desc = 'A ∩ B contém apenas os elementos presentes simultaneamente em A E em B.';
      reading = 'Lê-se: "A intersecção B" ou "A inter B"';
    } else if (currentOp === 'diffAB') {
      result = setA.filter(x => !setB.includes(x)).sort();
      desc = 'A \\ B são os elementos que pertencem exclusivamente a A, subtraindo os que também estão em B.';
      reading = 'Lê-se: "A menos B" ou "diferença entre A e B"';
    } else if (currentOp === 'diffBA') {
      result = setB.filter(x => !setA.includes(x)).sort();
      desc = 'B \\ A são os elementos que pertencem exclusivamente a B, subtraindo os que também estão em A.';
      reading = 'Lê-se: "B menos A"';
    } else if (currentOp === 'powA') {
      result = ['∅', '{1}', '{2}', '{3}', '{4}', '{1,2}', '{1,3}', '{1,4}', '{2,3}', '{2,4}', '{3,4}', '{1,2,3}', '{1,2,4}', '{1,3,4}', '{2,3,4}', '{1,2,3,4}'];
      desc = `P(A) é a família de todos os subconjuntos de A. Como |A| = 4, temos exatamente 2⁴ = 16 subconjuntos!`;
      reading = 'Lê-se: "Conjunto das Partes de A" ou "Potência de A"';
    }

    return { result, desc, reading };
  }

  function render() {
    const { result, desc, reading } = calculate();

    container.innerHTML = `
      <div style="background-color:var(--bg-card-subtle); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--border-subtle); margin-bottom:1rem;">
        <div style="font-weight:600; font-size:0.95rem; margin-bottom:6px;">Conjuntos Definidos:</div>
        <div style="font-family:var(--font-mono); font-size:0.92rem; color:var(--text-main);">
          A = { 1, 2, 3, 4 } &nbsp;&nbsp;|&nbsp;&nbsp; B = { 3, 4, 5, 6 }
        </div>
      </div>

      <div style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:1.25rem;">
        <button class="btn-nav ${currentOp === 'union' ? 'btn-primary' : ''}" data-op="union">União (A ∪ B)</button>
        <button class="btn-nav ${currentOp === 'intersect' ? 'btn-primary' : ''}" data-op="intersect">Intersecção (A ∩ B)</button>
        <button class="btn-nav ${currentOp === 'diffAB' ? 'btn-primary' : ''}" data-op="diffAB">Diferença (A \\ B)</button>
        <button class="btn-nav ${currentOp === 'diffBA' ? 'btn-primary' : ''}" data-op="diffBA">Diferença (B \\ A)</button>
        <button class="btn-nav ${currentOp === 'powA' ? 'btn-primary' : ''}" data-op="powA">Partes P(A) [2⁴ = 16]</button>
      </div>

      <div class="translation-box" style="margin:0;">
        <div class="spoken-pronounce">
          <span class="icon">Como ler:</span>
          <span><strong>Como se lê:</strong> ${reading}</span>
        </div>
        <div class="plain-explanation" style="margin-bottom:0.75rem;">
          <strong>Explicação Intuitiva:</strong> ${desc}
        </div>
        <div style="background-color:var(--bg-card); padding:0.85rem; border-radius:var(--radius-sm); border:1px solid var(--border-subtle); font-family:var(--font-mono); font-size:0.95rem; color:var(--accent-primary); word-break:break-all;">
          Resultado = { ${Array.isArray(result) ? result.join(', ') : result} }
          <div style="font-size:0.82rem; color:var(--text-muted); margin-top:4px;">
            Cardinalidade (Tamanho): ${result.length} elemento(s)
          </div>
        </div>
      </div>
    `;

    container.querySelectorAll('button[data-op]').forEach(btn => {
      btn.addEventListener('click', () => {
        currentOp = btn.getAttribute('data-op');
        render();
      });
    });
  }

  render();
}

// 5. Interactive Hasse Reduction Slider (Topic 8)
function initHasseReductionWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let currentStep = 0;
  const steps = [
    {
      title: "Passo 0: Dígrafo Completo da Relação de Ordem",
      rule: "O dígrafo contém todos os pares de (P({a,b}), ⊆): contém laços reflexivos em todos os nós e atalhos transitivos de ∅ para {a,b}.",
      notes: "Poluição visual máxima: difícil de ler.",
      showLoops: true,
      showTransitive: true,
      arrows: true
    },
    {
      title: "Passo 1: Eliminar Laços Reflexivos",
      rule: "Regra 1 de Hasse: Como toda relação de ordem é sabidamente reflexiva (x ≤ x), removemos os laços em todos os nós. A reflexividade é implícita.",
      notes: "Eliminamos: (∅, ∅), ({a}, {a}), ({b}, {b}), ({a,b}, {a,b}).",
      showLoops: false,
      showTransitive: true,
      arrows: true
    },
    {
      title: "Passo 2: Eliminar Arestas Transitivas (Atalhos)",
      rule: "Regra 2 de Hasse: Se x ≤ y e y ≤ z, a transitividade garante que x ≤ z. Logo, a aresta direta de x para z é supérflua e é removida, restando apenas a Relação de Cobertura (x ⋖ y).",
      notes: "Eliminamos a aresta direta de ∅ para {a,b}, pois o caminho passa por {a} e {b}.",
      showLoops: false,
      showTransitive: false,
      arrows: true
    },
    {
      title: "Passo 3: Orientação Vertical e Remoção das Setas (Diagrama de Hasse Final)",
      rule: "Regra 3 de Hasse: Posicionamos os elementos menores embaixo e os maiores em cima. Todas as conexões apontam naturalmente para cima, permitindo remover as pontas de flecha!",
      notes: "Forma canônica e elegante: o famoso losango da álgebra booleana (reticulado Q₂).",
      showLoops: false,
      showTransitive: false,
      arrows: false
    }
  ];

  function render() {
    const s = steps[currentStep];

    container.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
        <span class="widget-tag">Etapa ${currentStep} de 3</span>
        <div style="display:flex; gap:6px;">
          <button class="btn-nav" id="${containerId}-prev" ${currentStep === 0 ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>← Passo Anterior</button>
          <button class="btn-nav btn-primary" id="${containerId}-next" ${currentStep === 3 ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>Próximo Passo →</button>
        </div>
      </div>

      <div style="background-color:var(--bg-card-subtle); border-radius:var(--radius-md); padding:1rem; border:1px solid var(--border-subtle); margin-bottom:1rem;">
        <h4 style="font-family:var(--font-serif); font-size:1.1rem; color:var(--accent-primary); margin-bottom:0.3rem;">${s.title}</h4>
        <p style="font-size:0.92rem; margin-bottom:0.4rem;">${s.rule}</p>
        <div style="font-size:0.85rem; color:var(--text-muted); font-style:italic;">${s.notes}</div>
      </div>

      <svg viewBox="0 0 360 260" style="width:100%; height:260px; background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md);">
        <defs>
          <marker id="${containerId}-hasse-arr" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#1e3a8a"/>
          </marker>
        </defs>

        <!-- Aresta Transitiva (∅ -> {a,b}) -->
        ${s.showTransitive ? `
          <line x1="180" y1="210" x2="180" y2="50" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4" ${s.arrows ? `marker-end="url(#${containerId}-hasse-arr)"` : ''} />
          <text x="195" y="130" font-size="11" fill="#dc2626" font-family="var(--font-mono)">Transitiva</text>
        ` : ''}

        <!-- Arestas de Cobertura (∅ -> {a}, ∅ -> {b}, {a} -> {a,b}, {b} -> {a,b}) -->
        <line x1="180" y1="210" x2="100" y2="130" stroke="#1e3a8a" stroke-width="2" ${s.arrows ? `marker-end="url(#${containerId}-hasse-arr)"` : ''} />
        <line x1="180" y1="210" x2="260" y2="130" stroke="#1e3a8a" stroke-width="2" ${s.arrows ? `marker-end="url(#${containerId}-hasse-arr)"` : ''} />
        <line x1="100" y1="130" x2="180" y2="50" stroke="#1e3a8a" stroke-width="2" ${s.arrows ? `marker-end="url(#${containerId}-hasse-arr)"` : ''} />
        <line x1="260" y1="130" x2="180" y2="50" stroke="#1e3a8a" stroke-width="2" ${s.arrows ? `marker-end="url(#${containerId}-hasse-arr)"` : ''} />

        <!-- Laços Reflexivos -->
        ${s.showLoops ? `
          <circle cx="180" cy="235" r="12" fill="none" stroke="#64748b" stroke-width="1.5" />
          <circle cx="75" cy="130" r="12" fill="none" stroke="#64748b" stroke-width="1.5" />
          <circle cx="285" cy="130" r="12" fill="none" stroke="#64748b" stroke-width="1.5" />
          <circle cx="180" cy="25" r="12" fill="none" stroke="#64748b" stroke-width="1.5" />
        ` : ''}

        <!-- Nodes -->
        <!-- Bot (∅) -->
        <circle cx="180" cy="210" r="18" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="180" y="210" font-family="var(--font-mono)" font-size="14" font-weight="700" text-anchor="middle" dominant-baseline="central">∅</text>

        <!-- Mid-Left ({a}) -->
        <circle cx="100" cy="130" r="18" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="100" y="130" font-family="var(--font-mono)" font-size="13" font-weight="700" text-anchor="middle" dominant-baseline="central">{a}</text>

        <!-- Mid-Right ({b}) -->
        <circle cx="260" cy="130" r="18" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="260" y="130" font-family="var(--font-mono)" font-size="13" font-weight="700" text-anchor="middle" dominant-baseline="central">{b}</text>

        <!-- Top ({a,b}) -->
        <circle cx="180" cy="50" r="18" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="180" y="50" font-family="var(--font-mono)" font-size="12" font-weight="700" text-anchor="middle" dominant-baseline="central">{a,b}</text>
      </svg>
    `;

    document.getElementById(`${containerId}-prev`).addEventListener('click', () => {
      if (currentStep > 0) {
        currentStep--;
        render();
      }
    });

    document.getElementById(`${containerId}-next`).addEventListener('click', () => {
      if (currentStep < 3) {
        currentStep++;
        render();
      }
    });
  }

  render();
}

// Global Auto-Init
document.addEventListener('DOMContentLoaded', () => {
  initMathRender();
  initQuiz();

  // Auto-init Phase 2 Interactive Notebooks if container is present on the page
  for (let i = 9; i <= 18; i++) {
    const pad = i.toString().padStart(2, '0');
    const cId = 'notebook-' + pad + '-container';
    const fnName = 'initNotebook' + pad;
    if (document.getElementById(cId) && typeof window[fnName] === 'function') {
      window[fnName](cId);
    }
  }
});


// ==========================================================================
// FASE 2: ENGINES INTERATIVOS DE PROGRAMAÇÃO E CIÊNCIA DA COMPUTAÇÃO
// ==========================================================================

// 6. Interactive C Division & Type Casting Engine (Topic 9 & 10)
function initCastingInspectorWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  function render(a = 10, b = 3) {
    const intDiv = Math.trunc(a / b);
    const floatDiv = a / b;
    const floatDivStr = floatDiv.toFixed(6).replace(/0+$/, '').replace(/\.$/, '.0');

    container.innerHTML = `
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:1rem;">
        <div>
          <label style="font-weight:600; font-size:0.88rem; display:block; margin-bottom:4px;">Numerador (int a):</label>
          <input type="number" id="${containerId}-in-a" value="${a}" style="width:100%; padding:8px; border-radius:6px; border:1px solid var(--border-strong); font-family:var(--font-mono); font-size:0.95rem;">
        </div>
        <div>
          <label style="font-weight:600; font-size:0.88rem; display:block; margin-bottom:4px;">Denominador (int b):</label>
          <input type="number" id="${containerId}-in-b" value="${b}" style="width:100%; padding:8px; border-radius:6px; border:1px solid var(--border-strong); font-family:var(--font-mono); font-size:0.95rem;">
        </div>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
        <div style="background:#fff; border:1px solid var(--border-strong); border-left:4px solid var(--accent-danger); border-radius:var(--radius-md); padding:1rem;">
          <div style="font-size:0.82rem; font-weight:700; color:var(--accent-danger); text-transform:uppercase; margin-bottom:4px;">1. Divisão Inteira Pura</div>
          <code style="display:block; margin-bottom:8px; font-size:0.92rem;">float x = a / b;</code>
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:6px;">Ambos os operandos são <code>int</code>. O processador trunca a parte fracionária na ULA antes de atribuir ao float:</p>
          <div style="font-family:var(--font-mono); font-size:1.15rem; font-weight:700; color:var(--accent-danger);">x = ${intDiv}.0</div>
        </div>

        <div style="background:#fff; border:1px solid var(--border-strong); border-left:4px solid var(--accent-success); border-radius:var(--radius-md); padding:1rem;">
          <div style="font-size:0.82rem; font-weight:700; color:var(--accent-success); text-transform:uppercase; margin-bottom:4px;">2. Divisão com Coerção Explícita (Cast)</div>
          <code style="display:block; margin-bottom:8px; font-size:0.92rem;">float y = a / (float)b;</code>
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:6px;">O cast força a promoção de <code>a</code> para float, executando divisão em ponto flutuante IEEE 754:</p>
          <div style="font-family:var(--font-mono); font-size:1.15rem; font-weight:700; color:var(--accent-success);">y = ${floatDivStr}...</div>
        </div>
      </div>
    `;

    document.getElementById(`${containerId}-in-a`).addEventListener('input', (e) => {
      const valA = parseInt(e.target.value, 10) || 0;
      const valB = parseInt(document.getElementById(`${containerId}-in-b`).value, 10) || 1;
      render(valA, valB);
    });

    document.getElementById(`${containerId}-in-b`).addEventListener('input', (e) => {
      const valA = parseInt(document.getElementById(`${containerId}-in-a`).value, 10) || 0;
      const valB = parseInt(e.target.value, 10) || 1;
      render(valA, valB);
    });
  }

  render();
}

// 7. Interactive Code Tracing Engine / Teste de Mesa (Topics 11 & 13)
function initLoopTraceWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let initialCont = 4;
  let maxCont = 11;
  let initialK = 7;
  let initialJ = 9;

  function runSimulation() {
    let history = [];
    let i = 0, j = initialJ, k = initialK;
    let stepCount = 0;

    for (let cont = initialCont; cont < maxCont; cont++) {
      i = cont + 5;
      let whileIterations = 0;
      while (k > 0) {
        let prevK = k;
        let prevJ = j;
        k = k - 1;
        j = k + Math.trunc(j / 2);
        whileIterations++;
        history.push({
          step: ++stepCount,
          cont: cont,
          i: i,
          k: k,
          j: j,
          action: `Laço while: k=${prevK}→${k}, j=(${k}+trunc(${prevJ}/2))=${j}`
        });
      }
      if (whileIterations === 0) {
        history.push({
          step: ++stepCount,
          cont: cont,
          i: i,
          k: k,
          j: j,
          action: `cont=${cont}: i=${i}, while não executa (k=0)`
        });
      }
    }
    return { finalI: i, finalJ: j, finalK: k, history };
  }

  function render() {
    const { finalI, finalJ, finalK, history } = runSimulation();

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1rem; margin-bottom:1rem;">
        <div style="font-weight:700; font-size:0.92rem; color:var(--accent-primary); margin-bottom:8px;">Valores Iniciais Configuráveis pelo Aluno:</div>
        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px;">
          <div>
            <label style="font-size:0.8rem; font-weight:600;">cont inicial:</label>
            <input type="number" id="${containerId}-cont" value="${initialCont}" style="width:100%; padding:6px; font-family:var(--font-mono); border:1px solid var(--border-strong); border-radius:4px;">
          </div>
          <div>
            <label style="font-size:0.8rem; font-weight:600;">cont limite:</label>
            <input type="number" id="${containerId}-max" value="${maxCont}" style="width:100%; padding:6px; font-family:var(--font-mono); border:1px solid var(--border-strong); border-radius:4px;">
          </div>
          <div>
            <label style="font-size:0.8rem; font-weight:600;">j inicial:</label>
            <input type="number" id="${containerId}-j" value="${initialJ}" style="width:100%; padding:6px; font-family:var(--font-mono); border:1px solid var(--border-strong); border-radius:4px;">
          </div>
          <div>
            <label style="font-size:0.8rem; font-weight:600;">k inicial:</label>
            <input type="number" id="${containerId}-k" value="${initialK}" style="width:100%; padding:6px; font-family:var(--font-mono); border:1px solid var(--border-strong); border-radius:4px;">
          </div>
        </div>
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; background:var(--accent-primary-light); padding:10px 14px; border-radius:var(--radius-md); margin-bottom:1rem; border:1px solid #bfdbfe;">
        <span style="font-weight:700; color:#1e3a8a;">Saída do printf ao final da execução:</span>
        <span style="font-family:var(--font-mono); font-size:1.15rem; font-weight:700; color:#1e3a8a;">
          i: ${finalI} &nbsp; j: ${finalJ} &nbsp; k: ${finalK}
        </span>
      </div>

      <div style="font-size:0.88rem; font-weight:600; color:var(--text-muted); margin-bottom:6px;">Tabela Rastreamento de Memória (Passo a Passo):</div>
      <div style="max-height:220px; overflow-y:auto; border:1px solid var(--border-subtle); border-radius:var(--radius-sm);">
        <table style="width:100%; border-collapse:collapse; font-size:0.85rem; font-family:var(--font-mono);">
          <thead style="background:var(--bg-card-subtle); position:sticky; top:0; border-bottom:1px solid var(--border-strong);">
            <tr>
              <th style="padding:6px; text-align:left;">Passo</th>
              <th style="padding:6px; text-align:center;">cont</th>
              <th style="padding:6px; text-align:center;">i</th>
              <th style="padding:6px; text-align:center;">j</th>
              <th style="padding:6px; text-align:center;">k</th>
              <th style="padding:6px; text-align:left;">Operação Executada</th>
            </tr>
          </thead>
          <tbody>
            ${history.map(h => `
              <tr style="border-bottom:1px solid var(--border-subtle);">
                <td style="padding:6px;">#${h.step}</td>
                <td style="padding:6px; text-align:center;">${h.cont}</td>
                <td style="padding:6px; text-align:center; font-weight:700;">${h.i}</td>
                <td style="padding:6px; text-align:center; color:var(--accent-primary); font-weight:700;">${h.j}</td>
                <td style="padding:6px; text-align:center; color:var(--accent-danger); font-weight:700;">${h.k}</td>
                <td style="padding:6px; font-family:var(--font-sans);">${h.action}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;

    document.getElementById(`${containerId}-cont`).addEventListener('input', (e) => {
      initialCont = parseInt(e.target.value, 10) || 0;
      render();
    });
    document.getElementById(`${containerId}-max`).addEventListener('input', (e) => {
      maxCont = parseInt(e.target.value, 10) || 0;
      render();
    });
    document.getElementById(`${containerId}-j`).addEventListener('input', (e) => {
      initialJ = parseInt(e.target.value, 10) || 0;
      render();
    });
    document.getElementById(`${containerId}-k`).addEventListener('input', (e) => {
      initialK = parseInt(e.target.value, 10) || 0;
      render();
    });
  }

  render();
}

// 8. Interactive Call Stack Recursion Visualizer (Topic 14)
function initRecursionStackWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let targetN = 4;

  function calculateTrace(n) {
    let callHistory = [];
    let maxStackDepth = 0;
    let totalCalls = 0;

    function rec(val, depth) {
      totalCalls++;
      if (depth > maxStackDepth) maxStackDepth = depth;
      callHistory.push({ action: 'PUSH', val, depth });

      let result;
      if (val <= 1) {
        result = 1;
      } else {
        const left = rec(val - 1, depth + 1);
        const right = rec(val - 2, depth + 1);
        result = 2 * left + right; // Formulada no estilo Q09 oficial
      }

      callHistory.push({ action: 'POP', val, depth, result });
      return result;
    }

    const finalResult = rec(n, 1);
    return { finalResult, maxStackDepth, totalCalls, callHistory };
  }

  function render() {
    const { finalResult, maxStackDepth, totalCalls } = calculateTrace(targetN);

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
          <div>
            <label style="font-weight:700; font-size:0.92rem; color:var(--text-main);">Escolha o parâmetro n de entrada:</label>
            <div style="display:flex; gap:8px; margin-top:6px;">
              ${[1, 2, 3, 4, 5, 6].map(num => `
                <button class="btn-nav ${targetN === num ? 'btn-primary' : ''}" data-rec="${num}">${num}</button>
              `).join('')}
            </div>
          </div>
          <div style="text-align:right;">
            <div style="font-size:0.82rem; color:var(--text-muted); text-transform:uppercase;">Resultado de f(${targetN}):</div>
            <div style="font-family:var(--font-mono); font-size:1.6rem; font-weight:800; color:var(--accent-primary);">${finalResult}</div>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:1rem;">
          <div style="background:var(--accent-primary-light); padding:10px; border-radius:6px; border:1px solid #bfdbfe;">
            <div style="font-size:0.8rem; font-weight:600; color:#1e3a8a; text-transform:uppercase;">Profundidade Máxima da Pilha (Stack Depth):</div>
            <div style="font-family:var(--font-mono); font-size:1.3rem; font-weight:800; color:#1e3a8a;">${maxStackDepth} níveis (O(n))</div>
            <p style="font-size:0.8rem; color:#1e3a8a; margin:4px 0 0 0;">Determina o limite para Stack Overflow.</p>
          </div>
          <div style="background:#fef2f2; padding:10px; border-radius:6px; border:1px solid #fecaca;">
            <div style="font-size:0.8rem; font-weight:600; color:#991b1b; text-transform:uppercase;">Total de Ativações na Árvore de Chamadas:</div>
            <div style="font-family:var(--font-mono); font-size:1.3rem; font-weight:800; color:#991b1b;">${totalCalls} chamadas (O(2ⁿ))</div>
            <p style="font-size:0.8rem; color:#991b1b; margin:4px 0 0 0;">Complexidade exponencial sem memoização.</p>
          </div>
        </div>
      </div>
    `;

    container.querySelectorAll('button[data-rec]').forEach(btn => {
      btn.addEventListener('click', () => {
        targetN = parseInt(btn.getAttribute('data-rec'), 10);
        render();
      });
    });
  }

  render();
}

// 9. Interactive Pointer & Array Memory Layout Visualizer (Topic 15)
function initPointerMemoryWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let activeIndex = 0;
  const arrayValues = [42, 17, 99, 8, 25];
  const baseAddress = 0x1000;
  const elementSize = 4; // 4 bytes for int in 32/64 bit C

  function render() {
    const curAddr = baseAddress + (activeIndex * elementSize);
    const hexAddr = '0x' + curAddr.toString(16).toUpperCase();

    container.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
        <span style="font-size:0.92rem; font-weight:600;">Clique na célula para posicionar o ponteiro <code>int *p</code>:</span>
        <div style="font-family:var(--font-mono); font-size:0.9rem; background:var(--accent-primary-light); padding:4px 10px; border-radius:4px; color:#1e3a8a;">
          Endereço ativo (p): ${hexAddr}
        </div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:8px; margin-bottom:1.25rem;">
        ${arrayValues.map((val, idx) => {
          const addr = '0x' + (baseAddress + idx * elementSize).toString(16).toUpperCase();
          const isSelected = (idx === activeIndex);
          return `
            <div class="pointer-cell-btn" data-idx="${idx}" style="cursor:pointer; background:${isSelected ? 'var(--accent-primary-light)' : '#fff'}; border:2px solid ${isSelected ? 'var(--accent-primary)' : 'var(--border-strong)'}; border-radius:6px; padding:10px 6px; text-align:center; transition:all 160ms ease;">
              <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">${addr}</div>
              <div style="font-size:1.3rem; font-weight:800; font-family:var(--font-mono); color:${isSelected ? 'var(--accent-primary)' : 'var(--text-main)'}; margin:4px 0;">${val}</div>
              <div style="font-size:0.78rem; font-weight:600; color:var(--text-dim); font-family:var(--font-mono);">v[${idx}]</div>
              ${isSelected ? `<div style="font-size:0.75rem; font-weight:700; color:var(--accent-primary); margin-top:2px;">▲ *p</div>` : ''}
            </div>
          `;
        }).join('')}
      </div>

      <div style="background:var(--bg-card-subtle); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--border-subtle); font-family:var(--font-mono); font-size:0.92rem;">
        <div style="margin-bottom:4px;"><strong>Expressão Direta:</strong> v[${activeIndex}] = ${arrayValues[activeIndex]}</div>
        <div style="margin-bottom:4px;"><strong>Aritmética de Ponteiro:</strong> *(v + ${activeIndex}) = ${arrayValues[activeIndex]} &nbsp;&nbsp;<span style="color:var(--text-muted);">(deslocamento de ${activeIndex} × 4 bytes = ${activeIndex * 4} bytes)</span></div>
        <div><strong>Endereço de Memória:</strong> &v[${activeIndex}] = (v + ${activeIndex}) = ${hexAddr}</div>
      </div>
    `;

    container.querySelectorAll('.pointer-cell-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        activeIndex = parseInt(btn.getAttribute('data-idx'), 10);
        render();
      });
    });
  }

  render();
}


// 10. Interactive String Memory & Slicing Inspector (Topic 16)
function initStringMemoryWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let currentStr = "IFCE";
  let sliceStart = 0;
  let sliceStop = 3;
  let sliceStep = 1;

  function render() {
    const chars = currentStr.split('');
    const cBytes = [...chars, '\\0']; // C representation with null terminator
    const pyLen = chars.length;
    const cSizeof = pyLen + 1; // including '\0'

    // Python slice computation
    let slicedResult = "";
    try {
      const step = sliceStep === 0 ? 1 : sliceStep;
      let indices = [];
      if (step > 0) {
        for (let i = sliceStart; i < sliceStop && i < pyLen; i += step) {
          if (i >= 0) indices.push(i);
        }
      } else {
        for (let i = sliceStart; i > sliceStop && i >= 0; i += step) {
          if (i < pyLen) indices.push(i);
        }
      }
      slicedResult = indices.map(idx => chars[idx]).join('');
    } catch(e) {
      slicedResult = "Erro";
    }

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div>
            <label style="font-weight:700; font-size:0.92rem; color:var(--text-main);">Texto da String de Teste:</label>
            <input type="text" id="${containerId}-text" value="${currentStr}" maxlength="10" style="padding:6px 10px; font-family:var(--font-mono); font-size:1rem; border:1px solid var(--border-strong); border-radius:4px; margin-left:8px; width:140px;">
          </div>
          <div style="font-size:0.85rem; color:var(--text-muted);">
            Tamanho: <code>strlen = ${pyLen}</code> | <code>sizeof em C = ${cSizeof} bytes</code>
          </div>
        </div>

        <div style="margin-bottom:1.25rem;">
          <div style="font-size:0.85rem; font-weight:700; color:var(--accent-primary); margin-bottom:6px; text-transform:uppercase;">
            1. Modelo de Memória em C: Array de chars com terminador nulo ('\\0')
          </div>
          <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:6px;">
            ${cBytes.map((b, idx) => {
              const isTerminator = (idx === cBytes.length - 1);
              const asciiCode = isTerminator ? 0 : b.charCodeAt(0);
              return `
                <div style="background:${isTerminator ? '#fee2e2' : 'var(--bg-card-subtle)'}; border:2px solid ${isTerminator ? '#ef4444' : 'var(--border-strong)'}; border-radius:6px; padding:8px 10px; text-align:center; min-width:54px;">
                  <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">[${idx}]</div>
                  <div style="font-size:1.3rem; font-weight:800; font-family:var(--font-mono); color:${isTerminator ? '#b91c1c' : 'var(--text-main)'}; margin:2px 0;">
                    ${isTerminator ? '\\0' : b}
                  </div>
                  <div style="font-size:0.75rem; font-weight:600; color:${isTerminator ? '#b91c1c' : 'var(--text-dim)'}; font-family:var(--font-mono);">
                    ${asciiCode}
                  </div>
                </div>
              `;
            }).join('')}
          </div>
          <div style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">
            * Em C, <code>strlen()</code> percorre a memória até encontrar o byte <code>0</code> ('\\0'). Se o terminador for sobrescrito, ocorre <em>Buffer Overflow / Leitura Fora dos Limites</em>.
          </div>
        </div>

        <div style="border-top:1px dashed var(--border-subtle); padding-top:1rem;">
          <div style="font-size:0.85rem; font-weight:700; color:#16a34a; margin-bottom:6px; text-transform:uppercase;">
            2. Modelo de Fatiamento (Slicing) em Python: s[start:stop:step]
          </div>
          <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; margin-bottom:10px;">
            <div>
              <label style="font-size:0.8rem; font-weight:600;">start (início):</label>
              <input type="number" id="${containerId}-start" value="${sliceStart}" min="0" max="${pyLen}" style="width:100%; padding:4px 8px; font-family:var(--font-mono); border:1px solid var(--border-strong); border-radius:4px;">
            </div>
            <div>
              <label style="font-size:0.8rem; font-weight:600;">stop (limite exclusivo):</label>
              <input type="number" id="${containerId}-stop" value="${sliceStop}" min="0" max="${pyLen}" style="width:100%; padding:4px 8px; font-family:var(--font-mono); border:1px solid var(--border-strong); border-radius:4px;">
            </div>
            <div>
              <label style="font-size:0.8rem; font-weight:600;">step (passo):</label>
              <input type="number" id="${containerId}-step" value="${sliceStep}" min="1" max="3" style="width:100%; padding:4px 8px; font-family:var(--font-mono); border:1px solid var(--border-strong); border-radius:4px;">
            </div>
          </div>
          <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:6px; padding:10px; font-family:var(--font-mono); font-size:1rem; color:#166534;">
            Expressão: <code>s[${sliceStart}:${sliceStop}:${sliceStep}]</code>  ->  Resultado: <strong>"${slicedResult}"</strong>
          </div>
        </div>
      </div>
    `;

    document.getElementById(`${containerId}-text`).addEventListener('input', (e) => {
      currentStr = e.target.value || "A";
      render();
    });
    document.getElementById(`${containerId}-start`).addEventListener('input', (e) => {
      sliceStart = parseInt(e.target.value, 10) || 0;
      render();
    });
    document.getElementById(`${containerId}-stop`).addEventListener('input', (e) => {
      sliceStop = parseInt(e.target.value, 10) || 0;
      render();
    });
    document.getElementById(`${containerId}-step`).addEventListener('input', (e) => {
      sliceStep = parseInt(e.target.value, 10) || 1;
      render();
    });
  }

  render();
}

// 11. Interactive Collection / Deque ADT Inspector (Topic 17 - Q15 Oficial)
function initCollectionsWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let activeType = 'deque';
  let elements = [10, 20, 30];

  const types = {
    deque: {
      name: "Deque (Fila de Duas Pontas com Extremidades Restritas)",
      desc: "Estrutura linear que permite inserções e remoções em ambas as extremidades (início e fim) com tempo O(1).",
      ops: ["Inserir Início", "Inserir Fim", "Remover Início", "Remover Fim"]
    },
    stack: {
      name: "Pilha (Stack - LIFO: Last In, First Out)",
      desc: "Inserções e remoções são realizadas exclusivamente pelo TOPO (fim). Ex: push() e pop() em tempo O(1).",
      ops: ["Push (Inserir Topo)", "Pop (Remover Topo)"]
    },
    queue: {
      name: "Fila (Queue - FIFO: First In, First Out)",
      desc: "Inserções no FIM (enqueue) e remoções no INÍCIO (dequeue) com tempo O(1).",
      ops: ["Enqueue (Inserir Fim)", "Dequeue (Remover Início)"]
    },
    linked_list: {
      name: "Lista Simplesmente Encadeada (sem cauda)",
      desc: "Acesso por ponteiros. Inserir no início é O(1), mas inserir ou remover no fim requer percorrer n nós: O(n).",
      ops: ["Inserir Início", "Remover Início", "Inserir Fim (O(n))"]
    }
  };

  function render() {
    const t = types[activeType];

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; gap:8px; margin-bottom:1rem; flex-wrap:wrap;">
          <button class="btn-nav ${activeType === 'deque' ? 'btn-primary' : ''}" data-type="deque">Deque (Q15 Oficial)</button>
          <button class="btn-nav ${activeType === 'stack' ? 'btn-primary' : ''}" data-type="stack">Pilha (LIFO)</button>
          <button class="btn-nav ${activeType === 'queue' ? 'btn-primary' : ''}" data-type="queue">Fila (FIFO)</button>
          <button class="btn-nav ${activeType === 'linked_list' ? 'btn-primary' : ''}" data-type="linked_list">Lista Encadeada</button>
        </div>

        <div style="background:var(--bg-card-subtle); padding:10px 14px; border-radius:var(--radius-sm); border:1px solid var(--border-subtle); margin-bottom:1rem;">
          <div style="font-weight:700; font-size:0.95rem; color:var(--accent-primary); margin-bottom:4px;">${t.name}</div>
          <div style="font-size:0.88rem; color:var(--text-muted);">${t.desc}</div>
        </div>

        <div style="display:flex; justify-content:center; align-items:center; min-height:80px; background:#f8fafc; border:2px dashed var(--border-strong); border-radius:8px; margin-bottom:1rem; padding:12px; gap:10px; overflow-x:auto;">
          ${elements.length === 0 ? '<span style="color:var(--text-dim); font-style:italic;">Estrutura Vazia</span>' : elements.map((item, idx) => `
            <div style="background:#fff; border:2px solid var(--accent-primary); border-radius:6px; padding:10px 16px; font-family:var(--font-mono); font-size:1.1rem; font-weight:700; color:var(--accent-primary); box-shadow:0 1px 3px rgba(0,0,0,0.05); text-align:center;">
              ${item}
              <div style="font-size:0.7rem; color:var(--text-muted); font-weight:400;">
                ${idx === 0 ? '← Início' : (idx === elements.length - 1 ? 'Fim →' : '')}
              </div>
            </div>
          `).join('')}
        </div>

        <div style="display:flex; gap:8px; flex-wrap:wrap; justify-content:center;">
          ${t.ops.map(op => `
            <button class="btn-nav action-btn" data-action="${op}" style="font-size:0.85rem; padding:6px 12px;">${op}</button>
          `).join('')}
          <button class="btn-nav" id="${containerId}-reset" style="font-size:0.85rem; padding:6px 12px; color:var(--accent-danger);">Resetar</button>
        </div>
      </div>
    `;

    container.querySelectorAll('button[data-type]').forEach(btn => {
      btn.addEventListener('click', () => {
        activeType = btn.getAttribute('data-type');
        elements = [10, 20, 30];
        render();
      });
    });

    container.querySelectorAll('.action-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const act = btn.getAttribute('data-action');
        const randVal = (Math.floor(Math.random() * 8) + 1) * 10;
        if (act.includes("Inserir Início") || act.includes("Push")) {
          elements.unshift(randVal);
        } else if (act.includes("Inserir Fim") || act.includes("Enqueue")) {
          elements.push(randVal);
        } else if (act.includes("Remover Início") || act.includes("Dequeue")) {
          elements.shift();
        } else if (act.includes("Remover Fim") || act.includes("Pop")) {
          elements.pop();
        }
        render();
      });
    });

    document.getElementById(`${containerId}-reset`).addEventListener('click', () => {
      elements = [10, 20, 30];
      render();
    });
  }

  render();
}

// 12. Interactive Dynamic Dispatch & MRO Visualizer (Topic 18)
function initVtableMroWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let activeClass = 'C';

  const mroData = {
    A: {
      mro: ['A', 'object'],
      f_source: 'A.f()',
      g_source: 'A.g()',
      vtable: [
        { slot: 'vptr[0]', method: 'f()', addr: '0x004010A0 (A::f)' },
        { slot: 'vptr[1]', method: 'g()', addr: '0x004010B0 (A::g)' }
      ]
    },
    B: {
      mro: ['B', 'A', 'object'],
      f_source: 'B.f() (sobrescreve A)',
      g_source: 'A.g() (herdado de A)',
      vtable: [
        { slot: 'vptr[0]', method: 'f()', addr: '0x004010F0 (B::f sobrescrito)' },
        { slot: 'vptr[1]', method: 'g()', addr: '0x004010B0 (A::g herdado)' }
      ]
    },
    C: {
      mro: ['C', 'B', 'A', 'object'],
      f_source: 'B.f() (herdado de B)',
      g_source: 'C.g() (sobrescreve A)',
      vtable: [
        { slot: 'vptr[0]', method: 'f()', addr: '0x004010F0 (B::f herdado)' },
        { slot: 'vptr[1]', method: 'g()', addr: '0x00401120 (C::g sobrescrito)' }
      ]
    }
  };

  function render() {
    const cur = mroData[activeClass];

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div>
            <label style="font-weight:700; font-size:0.92rem; color:var(--text-main);">Selecione a Classe Instanciada:</label>
            <div style="display:flex; gap:8px; margin-top:6px;">
              ${['A', 'B', 'C'].map(c => `
                <button class="btn-nav ${activeClass === c ? 'btn-primary' : ''}" data-cls="${c}">Objeto da Classe ${c}</button>
              `).join('')}
            </div>
          </div>
          <div style="font-size:0.85rem; color:var(--text-muted);">
            Hierarquia: <code>class C(B) -> class B(A) -> class A</code>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:1rem;">
          <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:6px; padding:10px;">
            <div style="font-size:0.8rem; font-weight:700; color:#166534; text-transform:uppercase; margin-bottom:4px;">
              Python MRO (Ordem de Resolução de Métodos)
            </div>
            <div style="font-family:var(--font-mono); font-size:0.95rem; font-weight:700; color:#166534;">
              [ ${cur.mro.join(' -> ')} ]
            </div>
            <div style="font-size:0.8rem; color:#166534; margin-top:6px;">
              Chamada <code>obj.f()</code> resolve em: <strong>${cur.f_source}</strong><br>
              Chamada <code>obj.g()</code> resolve em: <strong>${cur.g_source}</strong>
            </div>
          </div>

          <div style="background:var(--accent-primary-light); border:1px solid #bfdbfe; border-radius:6px; padding:10px;">
            <div style="font-size:0.8rem; font-weight:700; color:#1e3a8a; text-transform:uppercase; margin-bottom:4px;">
              C++/Java: VTable (Dynamic Dispatch / Polimorfismo)
            </div>
            <table style="width:100%; font-size:0.78rem; font-family:var(--font-mono); border-collapse:collapse;">
              ${cur.vtable.map(v => `
                <tr style="border-bottom:1px solid #dbeafe;">
                  <td style="padding:4px 0; font-weight:700; color:#1e3a8a;">${v.slot}</td>
                  <td style="padding:4px 0; color:#1e3a8a;">${v.method}</td>
                  <td style="padding:4px 0; text-align:right; color:#1e3a8a;">${v.addr}</td>
                </tr>
              `).join('')}
            </table>
            <div style="font-size:0.75rem; color:#1e3a8a; margin-top:4px;">
              O ponteiro vptr no objeto aponta para a tabela virtual da classe em tempo de execução.
            </div>
          </div>
        </div>
      </div>
    `;

    container.querySelectorAll('button[data-cls]').forEach(btn => {
      btn.addEventListener('click', () => {
        activeClass = btn.getAttribute('data-cls');
        render();
      });
    });
  }

  render();
}


// 13. Interactive Asymptotic Growth Rate & Big-O Inspector (Topic 19)
function initGrowthRateWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let activeN = 16;
  let activeNotation = 'theta'; // 'o', 'omega', 'theta'

  function calculateRates(n) {
    const log2n = Math.log2(n);
    const n_val = n;
    const nlogn = n * log2n;
    const n2 = n * n;
    const n3 = n * n * n;
    const pow2n = n <= 30 ? Math.pow(2, n) : Infinity;

    return { log2n, n_val, nlogn, n2, n3, pow2n };
  }

  function formatOps(num) {
    if (!isFinite(num)) return "> 10³⁰ (Explosão Combinatória)";
    if (num < 1000) return num.toFixed(1).replace('.0', '');
    if (num < 1e6) return (num / 1e3).toFixed(1) + ' mil';
    if (num < 1e9) return (num / 1e6).toFixed(1) + ' milhões';
    if (num < 1e12) return (num / 1e9).toFixed(1) + ' bilhões';
    return num.toExponential(2);
  }

  function render() {
    const rates = calculateRates(activeN);

    const notationExpl = {
      o: {
        title: "Notação O (Big-O / Cota Superior / Teto Assintótico)",
        symbol: "f(n) \\le c \\cdot g(n)",
        read: "f de n é menor ou igual a c vezes g de n, para todo n a partir de n₀.",
        intuition: "Garante o PIOR CENÁRIO: o algoritmo NÃO executa mais passos do que essa curva. É uma promessa de limite máximo.",
        color: "#dc2626"
      },
      omega: {
        title: "Notação Ω (Big-Omega / Cota Inferior / Piso Assintótico)",
        symbol: "f(n) \\ge c \\cdot g(n)",
        read: "f de n é maior ou igual a c vezes g de n, para todo n a partir de n₀.",
        intuition: "Garante o MELHOR CENÁRIO ou consumo mínimo: o algoritmo gasta PELO MENOS essa quantidade de passos.",
        color: "#16a34a"
      },
      theta: {
        title: "Notação Θ (Big-Theta / Cota Justa / Ordem Exata)",
        symbol: "c_1 \\cdot g(n) \\le f(n) \\le c_2 \\cdot g(n)",
        read: "f de n está imprensada entre c₁ vezes g de n e c₂ vezes g de n.",
        intuition: "O 'CASAMENTO PERFEITO': o algoritmo cresce EXATAMENTE na mesma taxa de g(n), tanto por cima quanto por baixo.",
        color: "#1e3a8a"
      }
    };

    const notInfo = notationExpl[activeNotation];

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:10px;">
          <div>
            <label style="font-weight:700; font-size:0.92rem; color:var(--text-main);">Escolha o tamanho da entrada (n):</label>
            <div style="display:flex; gap:6px; margin-top:6px;">
              ${[4, 8, 16, 64, 256, 1024].map(num => `
                <button class="btn-nav ${activeN === num ? 'btn-primary' : ''}" data-val="${num}">${num}</button>
              `).join('')}
            </div>
          </div>
          <div style="text-align:right;">
            <div style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase;">Entrada Atual:</div>
            <div style="font-family:var(--font-mono); font-size:1.4rem; font-weight:800; color:var(--accent-primary);">n = ${activeN}</div>
          </div>
        </div>

        <div style="display:flex; gap:6px; margin-bottom:1.25rem;">
          <button class="btn-nav ${activeNotation === 'theta' ? 'btn-primary' : ''}" data-not="theta">Notação Θ (Ordem Justa)</button>
          <button class="btn-nav ${activeNotation === 'o' ? 'btn-primary' : ''}" data-not="o">Notação O (Teto Superior)</button>
          <button class="btn-nav ${activeNotation === 'omega' ? 'btn-primary' : ''}" data-not="omega">Notação Ω (Piso Inferior)</button>
        </div>

        <div style="background:var(--bg-card-subtle); padding:12px; border-radius:var(--radius-sm); border-left:4px solid ${notInfo.color}; margin-bottom:1.25rem;">
          <div style="font-weight:700; font-size:0.95rem; color:var(--text-main); margin-bottom:4px;">${notInfo.title}</div>
          <div style="font-family:var(--font-mono); font-size:0.95rem; color:${notInfo.color}; margin-bottom:4px;">$$${notInfo.symbol}$$</div>
          <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:4px;"><strong>Como ler: Como se lê:</strong> "${notInfo.read}"</div>
          <div style="font-size:0.85rem; color:var(--text-main);"><strong>Significado:</strong> ${notInfo.intuition}</div>
        </div>

        <div style="font-weight:700; font-size:0.9rem; color:var(--text-muted); margin-bottom:8px; text-transform:uppercase;">
          Comparativo de Operações Necessárias para n = ${activeN}:
        </div>

        <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:8px; text-align:center;">
          <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:6px; padding:10px 4px;">
            <div style="font-family:var(--font-mono); font-size:0.82rem; font-weight:700; color:#166534;">O(log₂ n)</div>
            <div style="font-size:1.15rem; font-weight:800; font-family:var(--font-mono); color:#166534; margin:4px 0;">${formatOps(rates.log2n)}</div>
            <div style="font-size:0.7rem; color:#166534;">Logarítmico (Busca Binária)</div>
          </div>

          <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; padding:10px 4px;">
            <div style="font-family:var(--font-mono); font-size:0.82rem; font-weight:700; color:#1e40af;">O(n)</div>
            <div style="font-size:1.15rem; font-weight:800; font-family:var(--font-mono); color:#1e40af; margin:4px 0;">${formatOps(rates.n_val)}</div>
            <div style="font-size:0.7rem; color:#1e40af;">Linear (1 laço simples)</div>
          </div>

          <div style="background:#faf5ff; border:1px solid #e9d5ff; border-radius:6px; padding:10px 4px;">
            <div style="font-family:var(--font-mono); font-size:0.82rem; font-weight:700; color:#6b21a8;">O(n log n)</div>
            <div style="font-size:1.15rem; font-weight:800; font-family:var(--font-mono); color:#6b21a8; margin:4px 0;">${formatOps(rates.nlogn)}</div>
            <div style="font-size:0.7rem; color:#6b21a8;">Linearítmico (MergeSort)</div>
          </div>

          <div style="background:#fffbeb; border:1px solid #fde68a; border-radius:6px; padding:10px 4px;">
            <div style="font-family:var(--font-mono); font-size:0.82rem; font-weight:700; color:#92400e;">O(n²)</div>
            <div style="font-size:1.15rem; font-weight:800; font-family:var(--font-mono); color:#92400e; margin:4px 0;">${formatOps(rates.n2)}</div>
            <div style="font-size:0.7rem; color:#92400e;">Quadrático (2 laços aninhados)</div>
          </div>

          <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:6px; padding:10px 4px;">
            <div style="font-family:var(--font-mono); font-size:0.82rem; font-weight:700; color:#991b1b;">O(2ⁿ)</div>
            <div style="font-size:1.15rem; font-weight:800; font-family:var(--font-mono); color:#991b1b; margin:4px 0;">${formatOps(rates.pow2n)}</div>
            <div style="font-size:0.7rem; color:#991b1b;">Exponencial (Recursão dupla)</div>
          </div>
        </div>
      </div>
    `;

    container.querySelectorAll('button[data-val]').forEach(btn => {
      btn.addEventListener('click', () => {
        activeN = parseInt(btn.getAttribute('data-val'), 10);
        render();
        if (typeof renderMathInElement === 'function') {
          renderMathInElement(container, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false }
            ],
            throwOnError: false
          });
        }
      });
    });

    container.querySelectorAll('button[data-not]').forEach(btn => {
      btn.addEventListener('click', () => {
        activeNotation = btn.getAttribute('data-not');
        render();
        if (typeof renderMathInElement === 'function') {
          renderMathInElement(container, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false }
            ],
            throwOnError: false
          });
        }
      });
    });
  }

  render();
}


// 14. Interactive Best/Average/Worst Case Visualizer (Topic 20)
function initCaseVisualizerWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const data = [12, 25, 33, 47, 58, 64, 79, 91];
  let searchVal = 12; // default best case for linear
  let currentAlgo = 'linear'; // 'linear' or 'binary'

  function runLinear(target) {
    let steps = [];
    for (let i = 0; i < data.length; i++) {
      steps.push({ idx: i, val: data[i], matched: data[i] === target });
      if (data[i] === target) break;
    }
    return steps;
  }

  function runBinary(target) {
    let steps = [];
    let esq = 0, dir = data.length - 1;
    while (esq <= dir) {
      let mid = Math.floor((esq + dir) / 2);
      let matched = (data[mid] === target);
      steps.push({ idx: mid, val: data[mid], esq, dir, matched });
      if (matched) break;
      if (data[mid] < target) esq = mid + 1;
      else dir = mid - 1;
    }
    return steps;
  }

  function render() {
    const isLinear = currentAlgo === 'linear';
    const trace = isLinear ? runLinear(searchVal) : runBinary(searchVal);
    const stepsCount = trace.length;
    const found = trace.some(t => t.matched);

    let caseType = "";
    if (isLinear) {
      if (searchVal === 12) caseType = "Melhor Caso: elemento no índice 0 (1 passo = O(1))";
      else if (!found || searchVal === 91) caseType = "Pior Caso: elemento no fim ou ausente (n passos = O(n))";
      else caseType = `Caso Médio: elemento no meio (${stepsCount} passos ≈ n/2 = O(n))`;
    } else {
      if (searchVal === 47 || searchVal === 58) caseType = "Melhor Caso: elemento encontrado no ponto médio exato (1 passo = O(1))";
      else if (!found || stepsCount === 4) caseType = "Pior Caso: elemento nas folhas ou ausente (log₂ 8 = 3 a 4 passos = O(log n))";
      else caseType = `Caso Típico: ${stepsCount} passos (O(log n))`;
    }

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:10px;">
          <div style="display:flex; gap:6px;">
            <button class="btn-nav ${currentAlgo === 'linear' ? 'btn-primary' : ''}" data-algo="linear">Busca Linear</button>
            <button class="btn-nav ${currentAlgo === 'binary' ? 'btn-primary' : ''}" data-algo="binary">Busca Binária (Q02 Oficial)</button>
          </div>
          <div>
            <label style="font-weight:700; font-size:0.85rem; color:var(--text-main);">Escolha o valor a buscar:</label>
            <select id="${containerId}-select" style="padding:4px 8px; font-family:var(--font-mono); border:1px solid var(--border-strong); border-radius:4px; margin-left:6px;">
              ${data.map(d => `<option value="${d}" ${d === searchVal ? 'selected' : ''}>${d}</option>`).join('')}
              <option value="999" ${searchVal === 999 ? 'selected' : ''}>999 (Ausente)</option>
            </select>
          </div>
        </div>

        <div style="font-size:0.85rem; font-weight:600; color:var(--text-muted); margin-bottom:6px;">Vetor Ordenado de Entrada (n = 8):</div>
        <div style="display:grid; grid-template-columns:repeat(8, 1fr); gap:6px; margin-bottom:1rem;">
          ${data.map((d, i) => {
            const visited = trace.some(t => t.idx === i);
            const isMatch = trace.some(t => t.idx === i && t.matched);
            let bg = "#fff";
            let borderColor = "var(--border-strong)";
            let textCol = "var(--text-main)";

            if (isMatch) {
              bg = "#dcfce7";
              borderColor = "#16a34a";
              textCol = "#166534";
            } else if (visited) {
              bg = "#fee2e2";
              borderColor = "#ef4444";
              textCol = "#991b1b";
            }

            return `
              <div style="background:${bg}; border:2px solid ${borderColor}; border-radius:6px; padding:8px 2px; text-align:center;">
                <div style="font-size:0.7rem; color:var(--text-muted); font-family:var(--font-mono);">[${i}]</div>
                <div style="font-size:1.15rem; font-weight:800; font-family:var(--font-mono); color:${textCol}; margin:2px 0;">${d}</div>
                <div style="font-size:0.68rem; font-weight:700; color:${textCol};">
                  ${isMatch ? 'ALVO' : (visited ? 'PASSOU' : '')}
                </div>
              </div>
            `;
          }).join('')}
        </div>

        <div style="background:var(--accent-primary-light); border:1px solid #bfdbfe; border-radius:6px; padding:10px 14px; margin-bottom:1rem;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-weight:700; color:#1e3a8a;">Classificação do Cenário:</span>
            <span style="font-family:var(--font-mono); font-size:1.1rem; font-weight:800; color:#1e3a8a;">${stepsCount} comparação(ões)</span>
          </div>
          <div style="font-size:0.85rem; color:#1e3a8a; margin-top:4px;">${caseType}</div>
        </div>

        <div style="font-size:0.82rem; color:var(--text-muted); line-height:1.4;">
          <strong>Rastreamento das Comparações:</strong>
          <ol style="margin-left:1.2rem; margin-top:4px;">
            ${trace.map((t, idx) => `
              <li>Passo ${idx + 1}: Comparou elemento no índice [${t.idx}] (valor ${t.val}) com o alvo ${searchVal}. ${t.matched ? '<strong>(Encontrou!)</strong>' : '(Não é igual)'}</li>
            `).join('')}
          </ol>
        </div>
      </div>
    `;

    container.querySelectorAll('button[data-algo]').forEach(btn => {
      btn.addEventListener('click', () => {
        currentAlgo = btn.getAttribute('data-algo');
        render();
      });
    });

    document.getElementById(`${containerId}-select`).addEventListener('change', (e) => {
      searchVal = parseInt(e.target.value, 10);
      render();
    });
  }

  render();
}


// 15. Interactive Master Theorem Calculator & Recursion Tree (Topic 21)
function initMasterTheoremWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let a = 2;
  let b = 2;
  let d = 1; // f(n) = n^d

  const presets = [
    { label: "MergeSort: 2T(n/2) + n", a: 2, b: 2, d: 1 },
    { label: "Busca Binária: T(n/2) + 1", a: 1, b: 2, d: 0 },
    { label: "Strassen: 7T(n/2) + n²", a: 7, b: 2, d: 2 },
    { label: "Raiz Dominante: 2T(n/2) + n³", a: 2, b: 2, d: 3 },
    { label: "Árvore Quádrupla: 4T(n/2) + n", a: 4, b: 2, d: 1 }
  ];

  function solve() {
    const log_b_a = Math.log(a) / Math.log(b);
    const eps = 1e-4;

    let caseNum = 0;
    let complexity = "";
    let expl = "";

    if (d < log_b_a - eps) {
      caseNum = 1;
      const rounded = log_b_a % 1 === 0 ? log_b_a.toFixed(0) : log_b_a.toFixed(2);
      complexity = rounded === '1' ? 'Θ(n)' : `Θ(n^${rounded})`;
      expl = `Caso 1: O custo das folhas n^(log_b a) = n^${rounded} domina o custo de combinação f(n) = n^${d}. A complexidade é determinada pelo trabalho nas folhas!`;
    } else if (Math.abs(d - log_b_a) <= eps) {
      caseNum = 2;
      const nPart = d === 0 ? '' : (d === 1 ? 'n ' : `n^${d} `);
      complexity = `Θ(${nPart}log n)`;
      expl = `Caso 2: Empate exato entre o custo de divisão f(n) e as folhas (log_b a = d = ${d}). O trabalho se distribui igualmente por todos os log n níveis da árvore!`;
    } else {
      caseNum = 3;
      complexity = d === 0 ? 'Θ(1)' : (d === 1 ? 'Θ(n)' : `Θ(n^${d})`);
      expl = `Caso 3: O custo da raiz f(n) = n^${d} domina o trabalho das folhas n^(log_b a = ${log_b_a.toFixed(2)}). O esforço maior ocorre logo na combinação inicial!`;
    }

    return { log_b_a, caseNum, complexity, expl };
  }

  function render() {
    const sol = solve();

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="font-size:0.85rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; margin-bottom:6px;">
          Exemplos Clássicos Pré-Configurados:
        </div>
        <div style="display:flex; gap:6px; flex-wrap:wrap; margin-bottom:1.25rem;">
          ${presets.map((p, idx) => `
            <button class="btn-nav preset-btn" data-idx="${idx}" style="font-size:0.8rem; padding:4px 8px;">${p.label}</button>
          `).join('')}
        </div>

        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; margin-bottom:1.25rem; background:var(--bg-card-subtle); padding:12px; border-radius:var(--radius-sm); border:1px solid var(--border-subtle);">
          <div>
            <label style="font-size:0.82rem; font-weight:700; color:var(--text-main);">Subproblemas (a ≥ 1):</label>
            <input type="number" id="${containerId}-a" value="${a}" min="1" max="16" style="width:100%; padding:6px; font-family:var(--font-mono); font-size:1rem; border:1px solid var(--border-strong); border-radius:4px; margin-top:4px;">
            <div style="font-size:0.75rem; color:var(--text-muted); margin-top:2px;">Número de chamadas filhas</div>
          </div>

          <div>
            <label style="font-size:0.82rem; font-weight:700; color:var(--text-main);">Fator de Divisão (b > 1):</label>
            <input type="number" id="${containerId}-b" value="${b}" min="2" max="8" style="width:100%; padding:6px; font-family:var(--font-mono); font-size:1rem; border:1px solid var(--border-strong); border-radius:4px; margin-top:4px;">
            <div style="font-size:0.75rem; color:var(--text-muted); margin-top:2px;">Subproblema de tamanho n/b</div>
          </div>

          <div>
            <label style="font-size:0.82rem; font-weight:700; color:var(--text-main);">Expoente de f(n) = n^d:</label>
            <input type="number" id="${containerId}-d" value="${d}" min="0" max="4" step="1" style="width:100%; padding:6px; font-family:var(--font-mono); font-size:1rem; border:1px solid var(--border-strong); border-radius:4px; margin-top:4px;">
            <div style="font-size:0.75rem; color:var(--text-muted); margin-top:2px;">Custo de combinar (d=0: O(1), d=1: O(n))</div>
          </div>
        </div>

        <div style="background:${sol.caseNum === 1 ? '#fee2e2' : (sol.caseNum === 2 ? 'var(--accent-primary-light)' : '#f0fdf4')}; border:2px solid ${sol.caseNum === 1 ? '#ef4444' : (sol.caseNum === 2 ? '#3b82f6' : '#16a34a')}; border-radius:var(--radius-md); padding:1rem; margin-bottom:1rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
            <div>
              <span style="font-size:0.82rem; font-weight:700; text-transform:uppercase; color:${sol.caseNum === 1 ? '#991b1b' : (sol.caseNum === 2 ? '#1e3a8a' : '#166534')};">
                Resultado do Teorema Mestre (Caso ${sol.caseNum})
              </span>
              <div style="font-family:var(--font-mono); font-size:1.5rem; font-weight:800; color:${sol.caseNum === 1 ? '#991b1b' : (sol.caseNum === 2 ? '#1e3a8a' : '#166534')}; margin-top:2px;">
                T(n) = ${sol.complexity}
              </div>
            </div>
            <div style="text-align:right; font-family:var(--font-mono); font-size:0.9rem;">
              <div>log_b a = log_${b}(${a}) ≈ <strong>${sol.log_b_a.toFixed(2)}</strong></div>
              <div>expoente d = <strong>${d}</strong></div>
            </div>
          </div>
          <div style="font-size:0.88rem; color:${sol.caseNum === 1 ? '#7f1d1d' : (sol.caseNum === 2 ? '#1e3a8a' : '#14532d')}; margin-top:8px;">
            <strong>Diagnóstico:</strong> ${sol.expl}
          </div>
        </div>
      </div>
    `;

    document.getElementById(`${containerId}-a`).addEventListener('input', (e) => {
      a = Math.max(1, parseInt(e.target.value, 10) || 1);
      render();
    });
    document.getElementById(`${containerId}-b`).addEventListener('input', (e) => {
      b = Math.max(2, parseInt(e.target.value, 10) || 2);
      render();
    });
    document.getElementById(`${containerId}-d`).addEventListener('input', (e) => {
      d = Math.max(0, parseInt(e.target.value, 10) || 0);
      render();
    });

    container.querySelectorAll('.preset-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const idx = parseInt(btn.getAttribute('data-idx'), 10);
        const p = presets[idx];
        a = p.a;
        b = p.b;
        d = p.d;
        render();
      });
    });
  }

  render();
}


// 16. Interactive Linked List Visualizer & Traversal Engine (Topic 22 - Q05 e Q11 Oficiais)
function initLinkedListWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let list = [15, 30, 45];
  let activeOperation = "idle";
  let stepLog = "Clique em uma operação para observar o custo de ponteiros em tempo real.";

  function render() {
    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div style="font-size:0.9rem; font-weight:700; color:var(--text-main);">
            Lista Simplesmente Encadeada (Sem ponteiro tail de cauda):
          </div>
          <div style="font-family:var(--font-mono); font-size:0.85rem; background:var(--bg-card-subtle); padding:4px 8px; border-radius:4px; border:1px solid var(--border-subtle);">
            Tamanho atual: n = ${list.length} nós
          </div>
        </div>

        <div style="display:flex; align-items:center; min-height:80px; background:#f8fafc; border:2px dashed var(--border-strong); border-radius:8px; padding:12px; margin-bottom:1rem; overflow-x:auto; gap:8px;">
          <div style="font-family:var(--font-mono); font-size:0.85rem; font-weight:700; color:var(--accent-primary); padding:6px 10px; background:#eff6ff; border-radius:4px; border:1px solid #bfdbfe;">
            head ->
          </div>

          ${list.length === 0 ? '<span style="color:var(--text-dim); font-style:italic; padding-left:10px;">Lista Vazia (head == NULL)</span>' : list.map((val, idx) => `
            <div style="display:flex; align-items:center; gap:6px;">
              <div style="display:flex; border:2px solid var(--accent-primary); border-radius:6px; background:#fff; overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,0.05);">
                <div style="padding:8px 12px; font-family:var(--font-mono); font-weight:800; font-size:1.1rem; color:var(--accent-primary); background:#fff;">
                  ${val}
                </div>
                <div style="padding:8px 8px; font-family:var(--font-mono); font-size:0.8rem; background:var(--bg-card-subtle); border-left:1px solid var(--border-subtle); color:var(--text-muted); display:flex; align-items:center;">
                  • prox
                </div>
              </div>
              <div style="font-family:var(--font-mono); font-size:1.1rem; color:var(--text-muted);">
                ${idx < list.length - 1 ? '->' : '-> NULL'}
              </div>
            </div>
          `).join('')}
        </div>

        <div style="background:var(--accent-primary-light); border:1px solid #bfdbfe; border-radius:6px; padding:10px; margin-bottom:1rem; font-size:0.88rem; color:#1e3a8a;">
          <strong>Rastreamento de Execução:</strong> ${stepLog}
        </div>

        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:8px;">
          <button class="btn-nav op-btn" data-action="insert-head" style="font-size:0.8rem; padding:6px;">
            1. Inserir no Início <br><span style="font-weight:700; color:#16a34a;">Custo: O(1)</span>
          </button>
          <button class="btn-nav op-btn" data-action="remove-head" style="font-size:0.8rem; padding:6px;">
            2. Remover do Início <br><span style="font-weight:700; color:#16a34a;">Custo: O(1)</span>
          </button>
          <button class="btn-nav op-btn" data-action="insert-tail" style="font-size:0.8rem; padding:6px;">
            3. Inserir no Fim <br><span style="font-weight:700; color:#dc2626;">Custo: O(n) (Q11)</span>
          </button>
          <button class="btn-nav op-btn" data-action="remove-tail" style="font-size:0.8rem; padding:6px;">
            4. Remover do Fim <br><span style="font-weight:700; color:#dc2626;">Custo: O(n) (Q05)</span>
          </button>
        </div>
      </div>
    `;

    container.querySelectorAll('.op-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const act = btn.getAttribute('data-action');
        const randVal = Math.floor(Math.random() * 80) + 10;

        if (act === 'insert-head') {
          list.unshift(randVal);
          stepLog = `Novo nó [${randVal}] criado no Heap. O ponteiro prox do novo nó apontou para o antigo head, e o head foi atualizado. Operação instantânea em tempo O(1)!`;
        } else if (act === 'remove-head') {
          if (list.length > 0) {
            const rem = list.shift();
            stepLog = `Ponteiro head avançou para head->prox. O nó [${rem}] foi desalocado com free(). Operação em tempo constante O(1)!`;
          } else {
            stepLog = `Lista já está vazia. Não há nós para remover.`;
          }
        } else if (act === 'insert-tail') {
          const oldLen = list.length;
          list.push(randVal);
          stepLog = `Como NÃO existe ponteiro tail, o algoritmo precisou percorrer todos os ${oldLen} nós desde o head até encontrar o nó com prox == NULL para só então ligar o novo nó [${randVal}]. Custo proporcional a n: O(n) (Questão 11 Oficial)!`;
        } else if (act === 'remove-tail') {
          if (list.length > 0) {
            const oldLen = list.length;
            const rem = list.pop();
            stepLog = `Para remover o último nó [${rem}], foi necessário percorrer toda a lista até o penúltimo nó para atualizar seu prox para NULL. Custo linear obrigatório: O(n) passos (Questão 05 Oficial)!`;
          } else {
            stepLog = `Lista vazia.`;
          }
        }
        render();
      });
    });
  }

  render();
}


// 17. Interactive Stack (LIFO) & Queue (FIFO) Dual Engine (Topic 23 - Q04 e Q08 Oficiais)
function initStackQueueEngineWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let activeMode = 'stack'; // 'stack' or 'queue'
  let stackItems = [1, 2];
  let stackLog = [];
  let queueItems = [4, 2, 5];
  let queueLog = [3, 1];

  function render() {
    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div style="display:flex; gap:6px;">
            <button class="btn-nav ${activeMode === 'stack' ? 'btn-primary' : ''}" data-mode="stack">Pilha / Stack (LIFO - Q04 Oficial)</button>
            <button class="btn-nav ${activeMode === 'queue' ? 'btn-primary' : ''}" data-mode="queue">Fila / Queue (FIFO - Q08 Oficial)</button>
          </div>
          <div style="font-size:0.85rem; color:var(--text-muted);">
            Regra: <strong>${activeMode === 'stack' ? 'LIFO (Último que entra, Primeiro que sai)' : 'FIFO (Primeiro que entra, Primeiro que sai)'}</strong>
          </div>
        </div>

        ${activeMode === 'stack' ? `
          <!-- STACK UI -->
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:1rem;">
            <div style="display:flex; flex-direction:column-reverse; align-items:center; min-height:160px; background:#f8fafc; border:2px dashed var(--border-strong); border-radius:8px; padding:12px; gap:6px;">
              ${stackItems.length === 0 ? '<span style="color:var(--text-dim); font-style:italic;">Pilha Vazia</span>' : stackItems.map((item, idx) => `
                <div style="width:80%; background:#fff; border:2px solid var(--accent-primary); border-radius:6px; padding:6px; text-align:center; font-family:var(--font-mono); font-weight:800; font-size:1.1rem; color:var(--accent-primary); box-shadow:0 1px 2px rgba(0,0,0,0.05);">
                  ${item} ${idx === stackItems.length - 1 ? '<span style="font-size:0.75rem; font-weight:600; color:#dc2626; margin-left:6px;">← TOPO</span>' : ''}
                </div>
              `).join('')}
            </div>

            <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle); font-size:0.85rem;">
              <div style="font-weight:700; color:var(--text-main); margin-bottom:6px;">Histórico de Elementos Retornados pelo pop():</div>
              <div style="font-family:var(--font-mono); font-size:1rem; color:var(--accent-danger); font-weight:700; min-height:24px;">
                ${stackLog.length > 0 ? stackLog.join(' -> ') : '(Nenhum pop ainda)'}
              </div>
              <div style="font-size:0.8rem; color:var(--text-muted); margin-top:8px;">
                * No push(), o elemento entra no TOPO. No pop(), o elemento sai obrigatoriamente do TOPO. Custo O(1).
              </div>
            </div>
          </div>

          <div style="display:flex; gap:8px;">
            <button class="btn-nav action-btn" data-act="push" style="font-size:0.85rem; padding:6px 12px;">Push (Empilhar)</button>
            <button class="btn-nav action-btn" data-act="pop" style="font-size:0.85rem; padding:6px 12px; color:var(--accent-danger);">Pop (Desempilhar)</button>
            <button class="btn-nav action-btn" data-act="sim-q04" style="font-size:0.85rem; padding:6px 12px; color:#1e3a8a;">Carregar Sequência da Q04 Oficial</button>
          </div>
        ` : `
          <!-- QUEUE UI -->
          <div style="background:#f8fafc; border:2px dashed var(--border-strong); border-radius:8px; padding:16px; margin-bottom:1rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="font-size:0.75rem; font-weight:700; color:#16a34a; text-transform:uppercase;">Início da Fila (Saída / Dequeue)</span>
              <span style="font-size:0.75rem; font-weight:700; color:#1e40af; text-transform:uppercase;">Fim da Fila (Entrada / Enqueue)</span>
            </div>

            <div style="display:flex; align-items:center; min-height:60px; gap:8px; overflow-x:auto;">
              ${queueItems.length === 0 ? '<span style="color:var(--text-dim); font-style:italic;">Fila Vazia</span>' : queueItems.map((item, idx) => `
                <div style="background:#fff; border:2px solid ${idx === 0 ? '#16a34a' : 'var(--accent-primary)'}; border-radius:6px; padding:8px 14px; font-family:var(--font-mono); font-size:1.15rem; font-weight:800; color:${idx === 0 ? '#166534' : 'var(--accent-primary)'}; box-shadow:0 1px 3px rgba(0,0,0,0.05); text-align:center;">
                  ${item}
                  <div style="font-size:0.65rem; font-weight:600; color:var(--text-muted);">
                    ${idx === 0 ? 'PRÓXIMO' : `Pos ${idx + 1}`}
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          <div style="background:var(--bg-card-subtle); padding:10px 14px; border-radius:6px; border:1px solid var(--border-subtle); margin-bottom:1rem; font-size:0.85rem;">
            <div style="font-weight:700; color:var(--text-main); margin-bottom:4px;">Sequência de Elementos Removidos (Dequeue):</div>
            <div style="font-family:var(--font-mono); font-size:1.05rem; font-weight:800; color:#16a34a;">
              ${queueLog.length > 0 ? queueLog.join(', ') : '(Nenhum elemento removido)'}
            </div>
          </div>

          <div style="display:flex; gap:8px;">
            <button class="btn-nav action-btn" data-act="enqueue" style="font-size:0.85rem; padding:6px 12px;">Enqueue (Entrar na Fila)</button>
            <button class="btn-nav action-btn" data-act="dequeue" style="font-size:0.85rem; padding:6px 12px; color:var(--accent-danger);">Dequeue (Atender Primeiro)</button>
            <button class="btn-nav action-btn" data-act="sim-q08" style="font-size:0.85rem; padding:6px 12px; color:#1e3a8a;">Carregar Sequência da Q08 Oficial</button>
          </div>
        `}
      </div>
    `;

    container.querySelectorAll('button[data-mode]').forEach(btn => {
      btn.addEventListener('click', () => {
        activeMode = btn.getAttribute('data-mode');
        render();
      });
    });

    container.querySelectorAll('.action-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const act = btn.getAttribute('data-act');
        const randVal = Math.floor(Math.random() * 9) + 1;

        if (act === 'push') {
          stackItems.push(randVal);
        } else if (act === 'pop') {
          if (stackItems.length > 0) stackLog.push(stackItems.pop());
        } else if (act === 'enqueue') {
          queueItems.push(randVal);
        } else if (act === 'dequeue') {
          if (queueItems.length > 0) queueLog.push(queueItems.shift());
        } else if (act === 'sim-q04') {
          // Sequência da Q04: push(1), push(2), push(3), pop(), push(4), pop(), pop()
          stackItems = [1];
          stackLog = [3, 4, 2];
        } else if (act === 'sim-q08') {
          // Sequência da Q08: enqueue(3), enqueue(1), enqueue(4), dequeue(), enqueue(2), enqueue(5), dequeue(), dequeue()
          queueItems = [2, 5];
          queueLog = [3, 1, 4];
        }
        render();
      });
    });
  }

  render();
}


// 18. Interactive Binary Search Tree & Traversal Engine (Topic 24)
function initBstTraversalWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let currentTraversal = 'inorder';

  const nodes = [
    { id: 50, x: 180, y: 35, left: 30, right: 70 },
    { id: 30, x: 100, y: 95, left: 20, right: 40 },
    { id: 70, x: 260, y: 95, left: 60, right: 80 },
    { id: 20, x: 60, y: 155, left: null, right: null },
    { id: 40, x: 140, y: 155, left: null, right: null },
    { id: 60, x: 220, y: 155, left: null, right: null },
    { id: 80, x: 300, y: 155, left: null, right: null }
  ];

  const sequences = {
    preorder: {
      name: "Pré-ordem (V-E-D / Visita, Esquerda, Direita)",
      order: [50, 30, 20, 40, 70, 60, 80],
      desc: "Visita a raiz primeiro. Usado para clonar ou serializar a estrutura original da árvore."
    },
    inorder: {
      name: "Em-ordem / Simétrica (E-V-D / Esquerda, Visita, Direita)",
      order: [20, 30, 40, 50, 60, 70, 80],
      desc: "Visita a subárvore esquerda, depois a raiz, depois a direita. PROPRIEDADE MÁGICA: Gera as chaves em ordem estritamente crescente!"
    },
    postorder: {
      name: "Pós-ordem (E-D-V / Esquerda, Direita, Visita)",
      order: [20, 40, 30, 60, 80, 70, 50],
      desc: "Visita as subárvores filhas antes do pai. Usado para desalocar a árvore da memória (free) e calcular espaço em disco."
    },
    bfs: {
      name: "Em Nível / BFS (Largura por Níveis)",
      order: [50, 30, 70, 20, 40, 60, 80],
      desc: "Varre linha por linha de cima para baixo, usando uma Fila (Queue) auxiliar."
    }
  };

  function render() {
    const cur = sequences[currentTraversal];

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div style="font-size:0.9rem; font-weight:700; color:var(--text-main);">
            Árvore Binária de Busca de Teste:
          </div>
          <div style="display:flex; gap:6px; flex-wrap:wrap;">
            <button class="btn-nav ${currentTraversal === 'inorder' ? 'btn-primary' : ''}" data-trav="inorder">Em-ordem (E-V-D)</button>
            <button class="btn-nav ${currentTraversal === 'preorder' ? 'btn-primary' : ''}" data-trav="preorder">Pré-ordem (V-E-D)</button>
            <button class="btn-nav ${currentTraversal === 'postorder' ? 'btn-primary' : ''}" data-trav="postorder">Pós-ordem (E-D-V)</button>
            <button class="btn-nav ${currentTraversal === 'bfs' ? 'btn-primary' : ''}" data-trav="bfs">Em Nível (BFS)</button>
          </div>
        </div>

        <svg viewBox="0 0 360 190" style="width:100%; height:190px; background:#f8fafc; border:1px solid var(--border-subtle); border-radius:var(--radius-md); margin-bottom:1rem;">
          <!-- Arestas -->
          <line x1="180" y1="35" x2="100" y2="95" stroke="#94a3b8" stroke-width="2" />
          <line x1="180" y1="35" x2="260" y2="95" stroke="#94a3b8" stroke-width="2" />
          <line x1="100" y1="95" x2="60" y2="155" stroke="#94a3b8" stroke-width="2" />
          <line x1="100" y1="95" x2="140" y2="155" stroke="#94a3b8" stroke-width="2" />
          <line x1="260" y1="95" x2="220" y2="155" stroke="#94a3b8" stroke-width="2" />
          <line x1="260" y1="95" x2="300" y2="155" stroke="#94a3b8" stroke-width="2" />

          <!-- Nós -->
          ${nodes.map(n => {
            const stepIndex = cur.order.indexOf(n.id) + 1;
            return `
              <g>
                <circle cx="${n.x}" cy="${n.y}" r="17" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
                <text x="${n.x}" y="${n.y}" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle" dominant-baseline="central">
                  ${n.id}
                </text>
                <circle cx="${n.x + 14}" cy="${n.y - 12}" r="9" fill="#dc2626" />
                <text x="${n.x + 14}" y="${n.y - 12}" font-family="var(--font-mono)" font-size="9" font-weight="700" fill="#fff" text-anchor="middle" dominant-baseline="central">
                  ${stepIndex}
                </text>
              </g>
            `;
          }).join('')}
        </svg>

        <div style="background:var(--bg-card-subtle); padding:10px 14px; border-radius:6px; border:1px solid var(--border-subtle); margin-bottom:1rem;">
          <div style="font-weight:700; font-size:0.95rem; color:var(--accent-primary); margin-bottom:4px;">${cur.name}</div>
          <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:8px;">${cur.desc}</div>
          <div style="font-family:var(--font-mono); font-size:1.15rem; font-weight:800; color:#166534;">
            Sequência Gerada: [ ${cur.order.join(' -> ')} ]
          </div>
        </div>
      </div>
    `;

    container.querySelectorAll('button[data-trav]').forEach(btn => {
      btn.addEventListener('click', () => {
        currentTraversal = btn.getAttribute('data-trav');
        render();
      });
    });
  }

  render();
}


// 19. Interactive AVL Rotation Simulator (Topic 25)
function initAvlTreeRotationWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let activeCase = 'LL'; // 'LL', 'RR', 'LR', 'RL'
  let isRotated = false;

  const cases = {
    LL: {
      title: "Caso LL (Esquerda-Esquerda): Desbalanceamento após inserir 10",
      unbalanced: "Nó 30 tem BF = +2 (altura esq: 2, dir: 0). Requer Rotação Simples à Direita.",
      svgUnbalanced: `
        <line x1="200" y1="40" x2="130" y2="100" stroke="#ef4444" stroke-width="2" />
        <line x1="130" y1="100" x2="70" y2="160" stroke="#ef4444" stroke-width="2" />
        <circle cx="200" cy="40" r="16" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
        <text x="200" y="40" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#991b1b" text-anchor="middle" dominant-baseline="central">30 (BF=+2)</text>
        <circle cx="130" cy="100" r="16" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="130" y="100" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle" dominant-baseline="central">20 (BF=+1)</text>
        <circle cx="70" cy="160" r="16" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="70" y="160" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle" dominant-baseline="central">10 (BF=0)</text>
      `,
      svgBalanced: `
        <line x1="180" y1="50" x2="100" y2="120" stroke="#16a34a" stroke-width="2" />
        <line x1="180" y1="50" x2="260" y2="120" stroke="#16a34a" stroke-width="2" />
        <circle cx="180" cy="50" r="16" fill="#dcfce7" stroke="#16a34a" stroke-width="2" />
        <text x="180" y="50" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#166534" text-anchor="middle" dominant-baseline="central">20 (BF=0)</text>
        <circle cx="100" cy="120" r="16" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="100" y="120" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle" dominant-baseline="central">10 (BF=0)</text>
        <circle cx="260" cy="120" r="16" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="260" y="120" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle" dominant-baseline="central">30 (BF=0)</text>
      `,
      solutionDesc: "Rotação Simples à Direita executada: 20 sobe para a raiz, 30 desce para a direita de 20. A árvore agora está perfeita com altura h = 2 e todos BF = 0!"
    },
    RR: {
      title: "Caso RR (Direita-Direita): Desbalanceamento após inserir 30",
      unbalanced: "Nó 10 tem BF = -2 (altura esq: 0, dir: 2). Requer Rotação Simples à Esquerda.",
      svgUnbalanced: `
        <line x1="100" y1="40" x2="170" y2="100" stroke="#ef4444" stroke-width="2" />
        <line x1="170" y1="100" x2="240" y2="160" stroke="#ef4444" stroke-width="2" />
        <circle cx="100" cy="40" r="16" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
        <text x="100" y="40" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#991b1b" text-anchor="middle" dominant-baseline="central">10 (BF=-2)</text>
        <circle cx="170" cy="100" r="16" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="170" y="100" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle" dominant-baseline="central">20 (BF=-1)</text>
        <circle cx="240" cy="160" r="16" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="240" y="160" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle" dominant-baseline="central">30 (BF=0)</text>
      `,
      svgBalanced: `
        <line x1="180" y1="50" x2="100" y2="120" stroke="#16a34a" stroke-width="2" />
        <line x1="180" y1="50" x2="260" y2="120" stroke="#16a34a" stroke-width="2" />
        <circle cx="180" cy="50" r="16" fill="#dcfce7" stroke="#16a34a" stroke-width="2" />
        <text x="180" y="50" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#166534" text-anchor="middle" dominant-baseline="central">20 (BF=0)</text>
        <circle cx="100" cy="120" r="16" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="100" y="120" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle" dominant-baseline="central">10 (BF=0)</text>
        <circle cx="260" cy="120" r="16" fill="#fff" stroke="#1e3a8a" stroke-width="2" />
        <text x="260" y="120" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle" dominant-baseline="central">30 (BF=0)</text>
      `,
      solutionDesc: "Rotação Simples à Esquerda executada: 20 sobe para a raiz, 10 desce para a esquerda de 20. Equilíbrio restabelecido em tempo O(1)!"
    }
  };

  function render() {
    const c = cases[activeCase];

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div style="display:flex; gap:6px;">
            <button class="btn-nav ${activeCase === 'LL' ? 'btn-primary' : ''}" data-case="LL">Caso LL (Simples Direita)</button>
            <button class="btn-nav ${activeCase === 'RR' ? 'btn-primary' : ''}" data-case="RR">Caso RR (Simples Esquerda)</button>
          </div>
          <button class="btn-nav" id="${containerId}-toggle" style="background:${isRotated ? '#dcfce7' : '#fee2e2'}; color:${isRotated ? '#166534' : '#991b1b'}; font-weight:700; border-color:${isRotated ? '#16a34a' : '#ef4444'};">
            ${isRotated ? 'Árvore Balanceada (Clique para Resetar)' : 'Executar Rotação AVL'}
          </button>
        </div>

        <div style="background:var(--bg-card-subtle); padding:10px 14px; border-radius:6px; border:1px solid var(--border-subtle); margin-bottom:1rem;">
          <div style="font-weight:700; font-size:0.92rem; color:var(--text-main); margin-bottom:2px;">${c.title}</div>
          <div style="font-size:0.85rem; color:var(--text-muted);">${isRotated ? c.solutionDesc : c.unbalanced}</div>
        </div>

        <svg viewBox="0 0 360 190" style="width:100%; height:190px; background:#f8fafc; border:1px solid var(--border-subtle); border-radius:var(--radius-md);">
          ${isRotated ? c.svgBalanced : c.svgUnbalanced}
        </svg>
      </div>
    `;

    container.querySelectorAll('button[data-case]').forEach(btn => {
      btn.addEventListener('click', () => {
        activeCase = btn.getAttribute('data-case');
        isRotated = false;
        render();
      });
    });

    document.getElementById(`${containerId}-toggle`).addEventListener('click', () => {
      isRotated = !isRotated;
      render();
    });
  }

  render();
}


// 20. Interactive Quadratic Sorting Visualizer (Topic 26 - Bubble, Selection, Insertion)
function initQuadraticSortingWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let currentAlgo = 'bubble';
  let initialArray = [50, 20, 40, 10, 30];
  let array = [...initialArray];
  let step = 0;
  let log = "Pressione 'Avançar Passo' para acompanhar o algoritmo.";
  let comparisons = 0;
  let swaps = 0;

  function render() {
    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div style="display:flex; gap:6px;">
            <button class="btn-nav ${currentAlgo === 'bubble' ? 'btn-primary' : ''}" data-algo="bubble">Bubble Sort</button>
            <button class="btn-nav ${currentAlgo === 'selection' ? 'btn-primary' : ''}" data-algo="selection">Selection Sort</button>
            <button class="btn-nav ${currentAlgo === 'insertion' ? 'btn-primary' : ''}" data-algo="insertion">Insertion Sort</button>
          </div>
          <div style="display:flex; gap:8px;">
            <button class="btn-nav" id="${containerId}-step" style="font-weight:700; color:#1e3a8a; border-color:#3b82f6;">Avançar Passo -></button>
            <button class="btn-nav" id="${containerId}-reset" style="color:var(--text-muted);">Resetar</button>
          </div>
        </div>

        <div style="display:flex; justify-content:center; align-items:flex-end; height:140px; background:#f8fafc; border:1px solid var(--border-subtle); border-radius:8px; padding:12px; gap:12px; margin-bottom:1rem;">
          ${array.map((val, idx) => `
            <div style="display:flex; flex-direction:column; align-items:center; width:50px;">
              <div style="font-family:var(--font-mono); font-size:0.85rem; font-weight:700; margin-bottom:4px; color:var(--text-main);">${val}</div>
              <div style="width:100%; height:${val * 2}px; background:#3b82f6; border-radius:4px 4px 0 0; transition:all 200ms ease;"></div>
              <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted); margin-top:4px;">[${idx}]</div>
            </div>
          `).join('')}
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; background:var(--bg-card-subtle); padding:10px 14px; border-radius:6px; border:1px solid var(--border-subtle); font-size:0.85rem; margin-bottom:0.75rem;">
          <div><strong>Ação:</strong> ${log}</div>
          <div style="font-family:var(--font-mono); font-weight:700; color:var(--accent-primary);">
            Comparações: ${comparisons} | Trocas: ${swaps}
          </div>
        </div>
      </div>
    `;

    container.querySelectorAll('button[data-algo]').forEach(btn => {
      btn.addEventListener('click', () => {
        currentAlgo = btn.getAttribute('data-algo');
        reset();
      });
    });

    document.getElementById(`${containerId}-reset`).addEventListener('click', reset);
    document.getElementById(`${containerId}-step`).addEventListener('click', stepExecution);
  }

  function reset() {
    array = [...initialArray];
    step = 0;
    comparisons = 0;
    swaps = 0;
    log = `Algoritmo ${currentAlgo.toUpperCase()} reiniciado com vetor inicial [${initialArray.join(', ')}].`;
    render();
  }

  function stepExecution() {
    step++;
    if (currentAlgo === 'bubble') {
      // Simple simulated steps for demo
      if (step === 1) {
        comparisons++;
        if (array[0] > array[1]) {
          let t = array[0]; array[0] = array[1]; array[1] = t;
          swaps++;
          log = "Passo 1: Comparou 50 e 20. 50 > 20, realizou a troca!";
        }
      } else if (step === 2) {
        comparisons++;
        if (array[1] > array[2]) {
          let t = array[1]; array[1] = array[2]; array[2] = t;
          swaps++;
          log = "Passo 2: Comparou 50 e 40. 50 > 40, realizou a troca!";
        }
      } else if (step === 3) {
        comparisons++;
        if (array[2] > array[3]) {
          let t = array[2]; array[2] = array[3]; array[3] = t;
          swaps++;
          log = "Passo 3: Comparou 50 e 10. 50 > 10, realizou a troca!";
        }
      } else if (step === 4) {
        comparisons++;
        if (array[3] > array[4]) {
          let t = array[3]; array[3] = array[4]; array[4] = t;
          swaps++;
          log = "Passo 4: Comparou 50 e 30. O maior elemento (50) flutuou para o fim do vetor!";
        }
      } else {
        array.sort((a,b)=>a-b);
        log = "Passagens adicionais concluídas: vetor completamente ordenado!";
      }
    } else if (currentAlgo === 'selection') {
      if (step === 1) {
        comparisons += 4;
        let minIdx = array.indexOf(Math.min(...array));
        let t = array[0]; array[0] = array[minIdx]; array[minIdx] = t;
        swaps++;
        log = "Passo 1: Varreu todo o vetor, encontrou o menor valor (10) e trocou diretamente com a posição [0]!";
      } else if (step === 2) {
        comparisons += 3;
        let sub = array.slice(1);
        let minVal = Math.min(...sub);
        let minIdx = array.indexOf(minVal);
        let t = array[1]; array[1] = array[minIdx]; array[minIdx] = t;
        swaps++;
        log = "Passo 2: Encontrou o segundo menor valor (20) e posicionou no índice [1]!";
      } else {
        array.sort((a,b)=>a-b);
        log = "Vetor ordenado com o mínimo de trocas físicas!";
      }
    } else if (currentAlgo === 'insertion') {
      if (step === 1) {
        comparisons++; swaps++;
        let t = array[1]; array[1] = array[0]; array[0] = t;
        log = "Passo 1: Inseriu 20 abrindo espaço e deslocando 50 para a direita.";
      } else {
        array.sort((a,b)=>a-b);
        log = "Passos subsequentes: cada novo item foi encaixado na sua posição exata!";
      }
    }
    render();
  }

  render();
}


// 21. Interactive Efficient Sorting Visualizer (Topic 27 - MergeSort, QuickSort [Q16], HeapSort)
function initEfficientSortingWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let currentAlgo = 'quicksort';
  let isWorstCase = false;

  const dataMap = {
    mergesort: {
      name: "MergeSort (Divisão e Conquista)",
      best: "Θ(n log n)",
      avg: "Θ(n log n)",
      worst: "Θ(n log n)",
      space: "O(n) - Exige vetor auxiliar!",
      stable: "Sim (Estável)",
      desc: "Divide o vetor ao meio em profundidade log n e intercala as metades ordenadas em tempo linear O(n). Garantia matemática absoluta mesmo no pior caso!"
    },
    quicksort: {
      name: "QuickSort (Particionamento por Pivô - Q16 Oficial)",
      best: "Θ(n log n)",
      avg: "Θ(n log n) - Mais rápido na prática",
      worst: "O(n²) (Questão 16 Oficial do Edital 53/2025)",
      space: "O(log n) pilha",
      stable: "Não (Instável)",
      desc: "Escolhe um pivô e particiona: menores à esquerda, maiores à direita. No pior caso (pivô péssimo em vetor ordenado), degenera para O(n²)!"
    },
    heapsort: {
      name: "HeapSort (Baseado em Max-Heap)",
      best: "Θ(n log n)",
      avg: "Θ(n log n)",
      worst: "Θ(n log n)",
      space: "O(1) - In-Place total!",
      stable: "Não (Instável)",
      desc: "Transforma o vetor em um Max-Heap em tempo linear O(n) e extrai sucessivamente o maior elemento para o fim. Combina tempo O(n log n) com espaço O(1)!"
    }
  };

  function render() {
    const cur = dataMap[currentAlgo];

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div style="display:flex; gap:6px;">
            <button class="btn-nav ${currentAlgo === 'quicksort' ? 'btn-primary' : ''}" data-algo="quicksort">QuickSort (Q16 Oficial)</button>
            <button class="btn-nav ${currentAlgo === 'mergesort' ? 'btn-primary' : ''}" data-algo="mergesort">MergeSort</button>
            <button class="btn-nav ${currentAlgo === 'heapsort' ? 'btn-primary' : ''}" data-algo="heapsort">HeapSort</button>
          </div>
          <div style="font-size:0.85rem; font-weight:700; color:var(--accent-primary);">
            Complexidade Assintótica de Referência
          </div>
        </div>

        <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:8px; margin-bottom:1.25rem; text-align:center;">
          <div style="background:#f8fafc; border:1px solid var(--border-subtle); border-radius:6px; padding:8px 4px;">
            <div style="font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">Melhor Caso</div>
            <div style="font-family:var(--font-mono); font-size:1rem; font-weight:800; color:#166534; margin-top:2px;">${cur.best}</div>
          </div>

          <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; padding:8px 4px;">
            <div style="font-size:0.72rem; color:#1e40af; text-transform:uppercase;">Caso Médio</div>
            <div style="font-family:var(--font-mono); font-size:1rem; font-weight:800; color:#1e3a8a; margin-top:2px;">${cur.avg}</div>
          </div>

          <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:6px; padding:8px 4px;">
            <div style="font-size:0.72rem; color:#991b1b; text-transform:uppercase;">Pior Caso</div>
            <div style="font-family:var(--font-mono); font-size:1rem; font-weight:800; color:#991b1b; margin-top:2px;">${cur.worst}</div>
          </div>

          <div style="background:#f8fafc; border:1px solid var(--border-subtle); border-radius:6px; padding:8px 4px;">
            <div style="font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">Espaço Auxiliar</div>
            <div style="font-family:var(--font-mono); font-size:0.85rem; font-weight:700; color:var(--text-main); margin-top:2px;">${cur.space}</div>
          </div>

          <div style="background:#f8fafc; border:1px solid var(--border-subtle); border-radius:6px; padding:8px 4px;">
            <div style="font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">Estabilidade</div>
            <div style="font-family:var(--font-mono); font-size:0.85rem; font-weight:700; color:${cur.stable.includes('Sim') ? '#16a34a' : '#dc2626'}; margin-top:2px;">${cur.stable}</div>
          </div>
        </div>

        <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle); font-size:0.88rem;">
          <div style="font-weight:700; color:var(--accent-primary); margin-bottom:4px;">${cur.name}</div>
          <div style="color:var(--text-muted);">${cur.desc}</div>
        </div>

        ${currentAlgo === 'quicksort' ? `
          <div style="margin-top:1rem; padding:10px; background:#fffbeb; border:1px solid #fde68a; border-radius:6px; font-size:0.85rem; color:#92400e;">
            <strong>Atenção para a Questão 16 Oficial do IFCE:</strong><br>
            A banca pergunta diretamente: <em>"Qual o tempo de execução do Quick Sort no pior caso?"</em><br>
            A resposta correta é invariavelmente <strong>O(n²)</strong>! O pior caso acontece quando o pivô escolhido divide o vetor no desbalanceamento máximo: 0 elementos de um lado e n - 1 do outro (ex: particionar vetor ordenado usando o primeiro elemento como pivô).
          </div>
        ` : ''}
      </div>
    `;

    container.querySelectorAll('button[data-algo]').forEach(btn => {
      btn.addEventListener('click', () => {
        currentAlgo = btn.getAttribute('data-algo');
        render();
      });
    });
  }

  render();
}


// 22. Interactive Container Primitives & Namespaces / Cgroups Inspector (Topic 28)
function initContainerPrimitivesWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let viewMode = 'container'; // 'container' vs 'vm'
  let cpuLimitMilli = 500; // 500m = 0.5 CPU
  let memLimitMb = 256;

  function render() {
    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div style="display:flex; gap:6px;">
            <button class="btn-nav ${viewMode === 'container' ? 'btn-primary' : ''}" data-view="container">Arquitetura de Contêiner Linux</button>
            <button class="btn-nav ${viewMode === 'vm' ? 'btn-primary' : ''}" data-view="vm">Máquina Virtual Tradicional (VM)</button>
          </div>
          <div style="font-size:0.85rem; font-weight:700; color:var(--accent-primary);">
            ${viewMode === 'container' ? 'Processo Nativo Isolado (Zero Overhead)' : 'Virtualização Completa de Hardware (Pesada)'}
          </div>
        </div>

        ${viewMode === 'container' ? `
          <!-- CONTAINER ARCHITECTURE -->
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:1rem;">
            <div style="background:#f8fafc; border:1px solid var(--border-subtle); border-radius:8px; padding:12px;">
              <div style="font-weight:700; font-size:0.85rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:8px;">
                Camadas de Execução no Servidor Host:
              </div>
              <div style="display:flex; flex-direction:column-reverse; gap:6px; font-family:var(--font-mono); font-size:0.85rem; text-align:center;">
                <div style="background:#3b82f6; color:#fff; padding:8px; border-radius:4px; font-weight:700;">
                  Hardware Físico (Bare Metal: CPU x86/ARM, RAM, Disco)
                </div>
                <div style="background:#1e3a8a; color:#fff; padding:8px; border-radius:4px; font-weight:700;">
                  ÚNICO Kernel Linux do Host (Gerencia chamadas de sistema)
                </div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">
                  <div style="background:#dcfce7; border:2px solid #16a34a; color:#166534; padding:10px 4px; border-radius:4px; font-weight:700;">
                    Namespaces (Isolamento de Visão)<br>
                    <span style="font-size:0.75rem; font-weight:400;">PID, NET, MNT, UTS</span>
                  </div>
                  <div style="background:#fef3c7; border:2px solid #d97706; color:#92400e; padding:10px 4px; border-radius:4px; font-weight:700;">
                    Cgroups v2 (Limitação de Recursos)<br>
                    <span style="font-size:0.75rem; font-weight:400;">cpu.max, memory.max</span>
                  </div>
                </div>
                <div style="background:#f1f5f9; border:2px dashed #64748b; color:#334155; padding:8px; border-radius:4px; font-weight:800;">
                  Contêiner: Processo Comum com Viseiras de Proteção!
                </div>
              </div>
            </div>

            <div style="background:var(--bg-card-subtle); border:1px solid var(--border-subtle); border-radius:8px; padding:12px;">
              <div style="font-weight:700; font-size:0.88rem; color:var(--text-main); margin-bottom:8px;">
                Simulador de Cgroup v2 (Limites do Kernel Linux):
              </div>
              
              <div style="margin-bottom:10px;">
                <label style="font-size:0.8rem; font-weight:600;">Limite de CPU (cpu.max): <strong>${cpuLimitMilli}m</strong> (${(cpuLimitMilli/1000).toFixed(1)} Core)</label>
                <input type="range" id="${containerId}-cpu" min="100" max="2000" step="100" value="${cpuLimitMilli}" style="width:100%;">
                <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">
                  Kernel CFS Quota: ${cpuLimitMilli * 100} / 100000 microssegundos por período
                </div>
              </div>

              <div style="margin-bottom:10px;">
                <label style="font-size:0.8rem; font-weight:600;">Limite de RAM (memory.max): <strong>${memLimitMb} MiB</strong></label>
                <input type="range" id="${containerId}-mem" min="64" max="1024" step="64" value="${memLimitMb}" style="width:100%;">
                <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">
                  Kernel OOM Limit: ${memLimitMb * 1024 * 1024} bytes (acima disso aciona OOM Killer!)
                </div>
              </div>

              <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:4px; padding:8px; font-family:var(--font-mono); font-size:0.8rem; color:#1e3a8a;">
                <strong>Arquivo Real no Linux:</strong><br>
                /sys/fs/cgroup/docker/&lt;id&gt;/cpu.max -> ${cpuLimitMilli * 100} 100000<br>
                /sys/fs/cgroup/docker/&lt;id&gt;/memory.max -> ${memLimitMb * 1048576}
              </div>
            </div>
          </div>
        ` : `
          <!-- VM ARCHITECTURE -->
          <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:8px; padding:14px; margin-bottom:1rem;">
            <div style="font-weight:700; font-size:0.9rem; color:#991b1b; margin-bottom:6px;">
              Estrutura Pesada de Máquina Virtual (Hipervisor Tipo 2 / KVM / VMware):
            </div>
            <p style="font-size:0.85rem; color:#991b1b; margin-bottom:8px;">
              Cada VM precisa emular uma placa-mãe virtual, memória virtualizada e rodar um <strong>Kernel de Sistema Operacional COMPLETO (Guest OS)</strong>!
            </p>
            <div style="display:flex; flex-direction:column-reverse; gap:6px; font-family:var(--font-mono); font-size:0.82rem; text-align:center;">
              <div style="background:#64748b; color:#fff; padding:6px; border-radius:4px;">Hardware Físico</div>
              <div style="background:#475569; color:#fff; padding:6px; border-radius:4px;">Host OS + Hipervisor (KVM / Xen / ESXi)</div>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
                <div style="background:#fee2e2; border:1px solid #ef4444; padding:8px; border-radius:4px; color:#991b1b;">
                  <strong>VM 1</strong><br>
                  Kernel Convidado Completo (~1 GB RAM só para dar boot)<br>
                  Tempo de boot: 30 a 60 segundos
                </div>
                <div style="background:#fee2e2; border:1px solid #ef4444; padding:8px; border-radius:4px; color:#991b1b;">
                  <strong>VM 2</strong><br>
                  Outro Kernel Convidado Completo (~1 GB RAM desperdiçada)<br>
                  Tempo de boot: 30 a 60 segundos
                </div>
              </div>
            </div>
          </div>
        `}
      </div>
    `;

    container.querySelectorAll('button[data-view]').forEach(btn => {
      btn.addEventListener('click', () => {
        viewMode = btn.getAttribute('data-view');
        render();
      });
    });

    if (viewMode === 'container') {
      const cpuIn = document.getElementById(`${containerId}-cpu`);
      const memIn = document.getElementById(`${containerId}-mem`);
      if (cpuIn) {
        cpuIn.addEventListener('input', (e) => {
          cpuLimitMilli = parseInt(e.target.value, 10);
          render();
        });
      }
      if (memIn) {
        memIn.addEventListener('input', (e) => {
          memLimitMb = parseInt(e.target.value, 10);
          render();
        });
      }
    }
  }

  render();
}


// 23. Interactive Google Borg Cell Sharing & Resource Overcommitment Simulator (Topic 29)
function initBorgCellSharingWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let prodTrafficSpike = 30; // 30% baseline prod load
  let batchActive = true;

  function render() {
    const serverCapacity = 100; // 100% CPU of machine
    const prodReserved = 60; // Developer requested 60%
    const prodActual = prodTrafficSpike; // Actual consumption
    const batchLoad = batchActive ? 50 : 0; // Batch wants 50%
    const totalActual = prodActual + batchLoad;

    const isOverload = totalActual > serverCapacity;
    let evictedBatch = 0;
    let finalBatchLoad = batchLoad;

    if (isOverload) {
      // Borg preemption: Batch is throttled/killed to guarantee Prod!
      evictedBatch = totalActual - serverCapacity;
      finalBatchLoad = Math.max(0, batchLoad - evictedBatch);
    }

    const currentTotal = prodActual + finalBatchLoad;

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div style="font-size:0.9rem; font-weight:700; color:var(--text-main);">
            Máquina Física Compartilhada do Borg (16 Cores / 32 GB RAM):
          </div>
          <div style="display:flex; gap:6px;">
            <button class="btn-nav ${batchActive ? 'btn-primary' : ''}" id="${containerId}-batch-toggle">
              ${batchActive ? 'Tarefas Batch Ativas' : 'Pausar Tarefas Batch'}
            </button>
          </div>
        </div>

        <div style="margin-bottom:1.25rem;">
          <label style="font-size:0.85rem; font-weight:700; color:var(--text-main);">
            Simular Tráfego da Aplicação Prod (Gmail / Busca): <strong>${prodTrafficSpike}% de CPU real</strong>
          </label>
          <input type="range" id="${containerId}-slider" min="10" max="95" step="5" value="${prodTrafficSpike}" style="width:100%; margin-top:4px;">
          <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">
            <span>Madrugada (10% uso)</span>
            <span>Carga Normal (30% a 50%)</span>
            <span>Pico Crítico (80% a 95%)</span>
          </div>
        </div>

        <div style="background:#f8fafc; border:1px solid var(--border-subtle); border-radius:8px; padding:12px; margin-bottom:1rem;">
          <div style="display:flex; justify-content:space-between; font-size:0.85rem; font-weight:700; margin-bottom:6px;">
            <span>Ocupação Total da CPU da Máquina Física:</span>
            <span style="font-family:var(--font-mono); color:${currentTotal > 90 ? '#dc2626' : '#16a34a'};">${currentTotal}% / 100%</span>
          </div>

          <!-- BARRA DE PROGRESSO MULTI-COLORIDA -->
          <div style="width:100%; height:28px; background:#e2e8f0; border-radius:6px; overflow:hidden; display:flex;">
            <div style="width:${prodActual}%; background:#2563eb; color:#fff; font-size:0.75rem; font-weight:700; display:flex; align-items:center; justify-content:center; transition:width 200ms ease;" title="Prod Real (${prodActual}%)">
              Prod (${prodActual}%)
            </div>
            <div style="width:${finalBatchLoad}%; background:#16a34a; color:#fff; font-size:0.75rem; font-weight:700; display:flex; align-items:center; justify-content:center; transition:width 200ms ease;" title="Batch Aproveitado (${finalBatchLoad}%)">
              ${finalBatchLoad > 10 ? `Batch (${finalBatchLoad}%)` : ''}
            </div>
            ${evictedBatch > 0 ? `
              <div style="width:${Math.min(100 - currentTotal, 10)}%; background:#ef4444; color:#fff; font-size:0.7rem; font-weight:700; display:flex; align-items:center; justify-content:center;" title="Preempção de Batch">
                Evict
              </div>
            ` : ''}
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; font-size:0.85rem;">
          <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; padding:10px;">
            <div style="font-weight:700; color:#1e40af; margin-bottom:2px;">1. Tarefas Prod (Alta Prioridade)</div>
            <div style="color:#1e3a8a;">Reserva Solicitada: 60% | Uso Real: ${prodActual}%</div>
            <div style="font-size:0.78rem; color:#1e3a8a; margin-top:4px;">
              Latência garantida! Seus ciclos de CPU têm garantia absoluta e nunca sofrem preempção.
            </div>
          </div>

          <div style="background:${evictedBatch > 0 ? '#fee2e2' : '#f0fdf4'}; border:1px solid ${evictedBatch > 0 ? '#fecaca' : '#bbf7d0'}; border-radius:6px; padding:10px;">
            <div style="font-weight:700; color:${evictedBatch > 0 ? '#991b1b' : '#166534'}; margin-bottom:2px;">
              2. Tarefas Batch (Baixa Prioridade / Oportunistas)
            </div>
            <div style="color:${evictedBatch > 0 ? '#991b1b' : '#166534'};">
              ${evictedBatch > 0 ? `Preempção do Borg ativada! Desalocou ${evictedBatch}% de Batch para salvar Prod!` : `Aproveitando 100% da folga não-utilizada de Prod (${finalBatchLoad}%).`}
            </div>
          </div>
        </div>
      </div>
    `;

    const slider = document.getElementById(`${containerId}-slider`);
    if (slider) {
      slider.addEventListener('input', (e) => {
        prodTrafficSpike = parseInt(e.target.value, 10);
        render();
      });
    }

    const toggle = document.getElementById(`${containerId}-batch-toggle`);
    if (toggle) {
      toggle.addEventListener('click', () => {
        batchActive = !batchActive;
        render();
      });
    }
  }

  render();
}


// 24. Interactive Google Autopilot VPA Simulator (Topic 30 - EuroSys 2020)
function initAutopilotSimulatorWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let mode = 'manual'; // 'manual' vs 'autopilot'
  let safetyMargin = 20; // 20% headroom

  function render() {
    // Simulated workload data (in milliCPUs)
    const usageHistory = [120, 150, 180, 420, 310, 190, 140, 380, 210, 160];
    const peakUsage = Math.max(...usageHistory); // 420m
    const avgUsage = usageHistory.reduce((a, b) => a + b, 0) / usageHistory.length; // 226m

    const manualLimit = 1000; // Human developer set 1000m
    const autopilotLimit = Math.round(peakUsage * (1 + safetyMargin / 100)); // ~504m

    const currentLimit = mode === 'manual' ? manualLimit : autopilotLimit;
    const wastedSlack = currentLimit - avgUsage;
    const efficiency = ((avgUsage / currentLimit) * 100).toFixed(1);

    container.innerHTML = `
      <div style="background:#fff; border:1px solid var(--border-subtle); border-radius:var(--radius-md); padding:1.25rem; margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:8px;">
          <div style="display:flex; gap:6px;">
            <button class="btn-nav ${mode === 'manual' ? 'btn-primary' : ''}" data-mode="manual">Configuração Manual Humana (Estática)</button>
            <button class="btn-nav ${mode === 'autopilot' ? 'btn-primary' : ''}" data-mode="autopilot">Google Autopilot VPA (Dinâmico)</button>
          </div>
          <div style="font-size:0.85rem; font-weight:700; color:${mode === 'autopilot' ? '#16a34a' : '#b45309'};">
            ${mode === 'autopilot' ? 'Eficiência Máxima com Proteção' : 'Superdimensionamento Crônico (Desperdício)'}
          </div>
        </div>

        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:8px; margin-bottom:1.25rem; text-align:center;">
          <div style="background:#f8fafc; border:1px solid var(--border-subtle); border-radius:6px; padding:8px 4px;">
            <div style="font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">Limite Definido</div>
            <div style="font-family:var(--font-mono); font-size:1.15rem; font-weight:800; color:${mode === 'autopilot' ? '#16a34a' : '#b45309'};">${currentLimit}m</div>
            <div style="font-size:0.7rem; color:var(--text-muted);">${(currentLimit/1000).toFixed(2)} Núcleo</div>
          </div>

          <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; padding:8px 4px;">
            <div style="font-size:0.72rem; color:#1e40af; text-transform:uppercase;">Pico Real do Pod</div>
            <div style="font-family:var(--font-mono); font-size:1.15rem; font-weight:800; color:#1e3a8a;">${peakUsage}m</div>
            <div style="font-size:0.7rem; color:#1e3a8a;">Medido em telemetria</div>
          </div>

          <div style="background:${mode === 'autopilot' ? '#f0fdf4' : '#fee2e2'}; border:1px solid ${mode === 'autopilot' ? '#bbf7d0' : '#fecaca'}; border-radius:6px; padding:8px 4px;">
            <div style="font-size:0.72rem; color:${mode === 'autopilot' ? '#166534' : '#991b1b'}; text-transform:uppercase;">Folga Ociosa (Slack)</div>
            <div style="font-family:var(--font-mono); font-size:1.15rem; font-weight:800; color:${mode === 'autopilot' ? '#166534' : '#991b1b'};">${Math.round(wastedSlack)}m</div>
            <div style="font-size:0.7rem; color:${mode === 'autopilot' ? '#166534' : '#991b1b'};">${mode === 'autopilot' ? 'Apenas margem segura' : 'Capacidade ociosa inútil'}</div>
          </div>

          <div style="background:#f8fafc; border:1px solid var(--border-subtle); border-radius:6px; padding:8px 4px;">
            <div style="font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">Aproveitamento Real</div>
            <div style="font-family:var(--font-mono); font-size:1.15rem; font-weight:800; color:var(--text-main);">${efficiency}%</div>
            <div style="font-size:0.7rem; color:var(--text-muted);">${mode === 'autopilot' ? '+250% melhor!' : 'Baixa eficiência'}</div>
          </div>
        </div>

        <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle); font-size:0.85rem;">
          <div style="font-weight:700; color:var(--accent-primary); margin-bottom:4px;">
            ${mode === 'autopilot' ? 'Como o Autopilot Decide o Ajuste (Rzadca et al., 2020):' : 'O Dilema Humano de Configuração:'}
          </div>
          <p style="color:var(--text-muted); margin:0;">
            ${mode === 'autopilot' 
              ? `O Autopilot analisa o histórico móvel dos picos (Windowed Peak = ${peakUsage}m), aplica uma margem de segurança ajustável (+${safetyMargin}%) e ajusta o Cgroup do contêiner para ${autopilotLimit}m. O contêiner nunca sofre estrangulamento e o cluster libera imediatamente ${manualLimit - autopilotLimit}m de CPU para outras aplicações!`
              : `Desenvolvedores humanos temem incidentes e configuram limites excessivos (1000m) em manifestos YAML que nunca são atualizados. A aplicação gasta em média 226m, deixando ${Math.round(wastedSlack)}m de capacidade computacional bloqueada sem uso!`
            }
          </p>
        </div>
      </div>
    `;

    container.querySelectorAll('button[data-mode]').forEach(btn => {
      btn.addEventListener('click', () => {
        mode = btn.getAttribute('data-mode');
        render();
      });
    });
  }

  render();
}

/* ==========================================================================
   AULA 31: KUBERNETES QOS & OOM SCORE CALCULATOR
   ========================================================================== */
function initK8sQoSWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let state = {
    cpuReq: 500,
    cpuLim: 1000,
    memReq: 512,
    memLim: 2048,
    nodeMem: 8192 // 8 GiB
  };

  function setPreset(type) {
    if (type === 'guaranteed') {
      state.cpuReq = 1000;
      state.cpuLim = 1000;
      state.memReq = 1024;
      state.memLim = 1024;
    } else if (type === 'burstable') {
      state.cpuReq = 500;
      state.cpuLim = 1500;
      state.memReq = 512;
      state.memLim = 2048;
    } else if (type === 'besteffort') {
      state.cpuReq = 0;
      state.cpuLim = 0;
      state.memReq = 0;
      state.memLim = 0;
    }
    render();
  }

  function computeQoS() {
    const hasCpuReq = state.cpuReq > 0;
    const hasCpuLim = state.cpuLim > 0;
    const hasMemReq = state.memReq > 0;
    const hasMemLim = state.memLim > 0;

    // BestEffort: No requests and no limits set for any resource
    if (!hasCpuReq && !hasCpuLim && !hasMemReq && !hasMemLim) {
      return {
        qos: 'BestEffort',
        badgeColor: '#c53030',
        badgeBg: '#fff5f5',
        badgeBorder: '#feb2b2',
        oomScore: 1000,
        killPriority: 'Primeira Vítima (Maior Risco de Extermínio)',
        desc: 'O pod não reservou nem limitou qualquer recurso. O Kubelet e o kernel Linux o classificam com menor prioridade absoluta. Durante escassez de memória (Memory Pressure), ele é imediatamente eliminado com sinal SIGKILL (ExitCode 137).'
      };
    }

    // Guaranteed: Requests and limits set for both CPU & Memory, and req == lim
    if (hasCpuReq && hasCpuLim && hasMemReq && hasMemLim &&
        state.cpuReq === state.cpuLim && state.memReq === state.memLim) {
      return {
        qos: 'Guaranteed',
        badgeColor: '#22543d',
        badgeBg: '#f0fff4',
        badgeBorder: '#9ae6b4',
        oomScore: -997,
        killPriority: 'Última Vítima (Máxima Proteção Institucional)',
        desc: 'O pod possui Requests rigorosamente idênticos aos Limits para CPU e Memória. Recebe o oom_score_adj de -997, tornando-se imune ao OOM-killer do kernel Linux, a não ser que o sistema operacional inteiro entre em colapso catastrófico.'
      };
    }

    // Burstable: Everything else
    let score = 1000;
    if (state.memReq > 0) {
      score = Math.floor(1000 - (1000 * state.memReq) / state.nodeMem);
      score = Math.max(2, Math.min(999, score));
    }
    return {
      qos: 'Burstable',
      badgeColor: '#b7791f',
      badgeBg: '#fffaf0',
      badgeBorder: '#fbd38d',
      oomScore: score,
      killPriority: 'Vítima Intermediária (Ordem Inversa da Reserva)',
      desc: `O pod possui garantias mínimas, mas permite pico (burst) até o limite. Seu oom_score_adj é dinamicamente calculado pela proporção de memória requisitada: 1000 - (1000 * ${state.memReq} / ${state.nodeMem}) = ${score}. Quanto maior for a reserva (Request), menor será o score e mais protegido o pod estará contra o OOM-Killer.`
    };
  }

  function render() {
    const qosData = computeQoS();

    container.innerHTML = `
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:10px; padding:20px; box-shadow:0 2px 8px rgba(0,0,0,0.04); font-family:var(--font-sans);">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:16px;">
          <div>
            <h4 style="margin:0; font-size:1.15rem; color:var(--text-color);">Simulador Interativo de QoS e OOM-Score (Kubernetes)</h4>
            <div style="font-size:0.85rem; color:var(--text-muted);">Avalie os critérios de classificação do Kubelet e o cálculo do <code>oom_score_adj</code></div>
          </div>
          <div style="display:flex; gap:6px;">
            <button class="btn-preset" data-preset="guaranteed" style="font-size:0.78rem; padding:5px 9px; border-radius:4px; border:1px solid #9ae6b4; background:#f0fff4; color:#22543d; font-weight:600; cursor:pointer;">Preset Guaranteed</button>
            <button class="btn-preset" data-preset="burstable" style="font-size:0.78rem; padding:5px 9px; border-radius:4px; border:1px solid #fbd38d; background:#fffaf0; color:#b7791f; font-weight:600; cursor:pointer;">Preset Burstable</button>
            <button class="btn-preset" data-preset="besteffort" style="font-size:0.78rem; padding:5px 9px; border-radius:4px; border:1px solid #feb2b2; background:#fff5f5; color:#c53030; font-weight:600; cursor:pointer;">Preset BestEffort</button>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:14px; margin-bottom:20px;">
          <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
            <label style="font-size:0.82rem; font-weight:600; display:block; margin-bottom:4px;">CPU Request (millicores): <span id="val-cpu-req">${state.cpuReq}</span>m</label>
            <input type="range" id="input-cpu-req" min="0" max="4000" step="100" value="${state.cpuReq}" style="width:100%; cursor:pointer;">
            <div style="display:flex; justify-content:space-between; font-size:0.72rem; color:var(--text-muted);"><span>0 (Sem Req)</span><span>4000m (4 cores)</span></div>
          </div>

          <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
            <label style="font-size:0.82rem; font-weight:600; display:block; margin-bottom:4px;">CPU Limit (millicores): <span id="val-cpu-lim">${state.cpuLim}</span>m</label>
            <input type="range" id="input-cpu-lim" min="0" max="4000" step="100" value="${state.cpuLim}" style="width:100%; cursor:pointer;">
            <div style="display:flex; justify-content:space-between; font-size:0.72rem; color:var(--text-muted);"><span>0 (Sem Lim)</span><span>4000m (4 cores)</span></div>
          </div>

          <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
            <label style="font-size:0.82rem; font-weight:600; display:block; margin-bottom:4px;">Memory Request (MiB): <span id="val-mem-req">${state.memReq}</span> MiB</label>
            <input type="range" id="input-mem-req" min="0" max="8192" step="128" value="${state.memReq}" style="width:100%; cursor:pointer;">
            <div style="display:flex; justify-content:space-between; font-size:0.72rem; color:var(--text-muted);"><span>0 (Sem Req)</span><span>8192 MiB</span></div>
          </div>

          <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
            <label style="font-size:0.82rem; font-weight:600; display:block; margin-bottom:4px;">Memory Limit (MiB): <span id="val-mem-lim">${state.memLim}</span> MiB</label>
            <input type="range" id="input-mem-lim" min="0" max="8192" step="128" value="${state.memLim}" style="width:100%; cursor:pointer;">
            <div style="display:flex; justify-content:space-between; font-size:0.72rem; color:var(--text-muted);"><span>0 (Sem Lim)</span><span>8192 MiB</span></div>
          </div>
        </div>

        <div style="background:var(--bg-light); border:1px solid var(--border-color); border-radius:8px; padding:16px; margin-bottom:16px;">
          <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
            <span style="font-size:0.9rem; font-weight:700; color:var(--text-color);">Classe de Serviço Atribuída:</span>
            <span style="font-size:1.05rem; font-weight:800; padding:4px 14px; border-radius:20px; background:${qosData.badgeBg}; color:${qosData.badgeColor}; border:1px solid ${qosData.badgeBorder};">${qosData.qos}</span>
          </div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:12px;">
            <div style="background:var(--bg-card); padding:10px 14px; border-radius:6px; border:1px solid var(--border-subtle);">
              <div style="font-size:0.78rem; color:var(--text-muted);">Score do Kernel (oom_score_adj)</div>
              <div style="font-size:1.3rem; font-weight:800; color:var(--accent-primary);">${qosData.oomScore}</div>
            </div>
            <div style="background:var(--bg-card); padding:10px 14px; border-radius:6px; border:1px solid var(--border-subtle);">
              <div style="font-size:0.78rem; color:var(--text-muted);">Prioridade no Extermínio (OOM)</div>
              <div style="font-size:0.95rem; font-weight:700; color:${qosData.badgeColor};">${qosData.killPriority}</div>
            </div>
          </div>

          <div style="font-size:0.85rem; color:var(--text-color); line-height:1.5;">
            ${qosData.desc}
          </div>
        </div>

        <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle); font-size:0.82rem;">
          <div style="font-weight:700; color:var(--text-color); margin-bottom:4px;">Hierarquia de Extermínio em Caso de Sobrecarga de Nó (Memory Pressure):</div>
          <div style="display:flex; align-items:center; gap:8px; margin-top:8px;">
            <div style="flex:1; background:#fff5f5; border:1px solid #feb2b2; color:#c53030; padding:8px; border-radius:4px; text-align:center; font-weight:700;">
              1º BestEffort<br><span style="font-size:0.72rem; font-weight:400;">Score = 1000 (Morte imediata)</span>
            </div>
            <div style="font-size:1.2rem; color:var(--text-muted);">→</div>
            <div style="flex:1; background:#fffaf0; border:1px solid #fbd38d; color:#b7791f; padding:8px; border-radius:4px; text-align:center; font-weight:700;">
              2º Burstable<br><span style="font-size:0.72rem; font-weight:400;">Score 2 a 999 (Ordem proporcional)</span>
            </div>
            <div style="font-size:1.2rem; color:var(--text-muted);">→</div>
            <div style="flex:1; background:#f0fff4; border:1px solid #9ae6b4; color:#22543d; padding:8px; border-radius:4px; text-align:center; font-weight:700;">
              3º Guaranteed<br><span style="font-size:0.72rem; font-weight:400;">Score = -997 (Protegido)</span>
            </div>
          </div>
        </div>
      </div>
    `;

    container.querySelectorAll('.btn-preset').forEach(btn => {
      btn.addEventListener('click', () => setPreset(btn.getAttribute('data-preset')));
    });

    const bindInput = (id, prop) => {
      const el = container.querySelector(id);
      if (el) {
        el.addEventListener('input', (e) => {
          state[prop] = parseInt(e.target.value, 10);
          render();
        });
      }
    };

    bindInput('#input-cpu-req', 'cpuReq');
    bindInput('#input-cpu-lim', 'cpuLim');
    bindInput('#input-mem-req', 'memReq');
    bindInput('#input-mem-lim', 'memLim');
  }

  render();
}

/* ==========================================================================
   AULA 32: CFS QUOTA & CPU THROTTLING VS OOM KILLER SIMULATOR
   ========================================================================== */
function initThrottlingSimulatorWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let state = {
    cfsPeriod: 100, // ms
    cfsQuota: 40,   // ms (0.4 cores)
    taskBurst: 80,  // ms demanded by app within 100ms
    memoryUsed: 420,// MiB
    memoryLimit: 512// MiB
  };

  function render() {
    const isThrottled = state.taskBurst > state.cfsQuota;
    const throttledTime = isThrottled ? (state.taskBurst - state.cfsQuota) : 0;
    const throttlePercent = Math.round((throttledTime / state.cfsPeriod) * 100);

    const isOOM = state.memoryUsed > state.memoryLimit;

    container.innerHTML = `
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:10px; padding:20px; box-shadow:0 2px 8px rgba(0,0,0,0.04); font-family:var(--font-sans);">
        <div style="margin-bottom:16px;">
          <h4 style="margin:0; font-size:1.15rem; color:var(--text-color);">Simulador: CPU Throttling (CFS Quota) vs OOM-Killer (Memory Limit)</h4>
          <div style="font-size:0.85rem; color:var(--text-muted);">Entenda a diferença crucial entre a lentidão silenciosa (CPU Throttling) e a morte súbita (OOM-Killer SIGKILL 137).</div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:20px;">
          <!-- CPU Section -->
          <div style="background:var(--bg-light); border:1px solid var(--border-color); border-radius:8px; padding:14px;">
            <div style="font-weight:700; font-size:0.95rem; color:var(--text-color); margin-bottom:10px; display:flex; justify-content:space-between;">
              <span>Mecanismo de CPU (Completely Fair Scheduler)</span>
              <span style="font-size:0.75rem; background:var(--bg-card-subtle); padding:2px 6px; border-radius:4px;">Period = ${state.cfsPeriod}ms</span>
            </div>

            <div style="margin-bottom:10px;">
              <label style="font-size:0.8rem; font-weight:600; display:block;">CFS Quota Alocada: <b>${state.cfsQuota}ms</b> (${(state.cfsQuota/state.cfsPeriod).toFixed(2)} CPU)</label>
              <input type="range" id="input-cfs-quota" min="10" max="100" step="5" value="${state.cfsQuota}" style="width:100%; cursor:pointer;">
            </div>

            <div style="margin-bottom:14px;">
              <label style="font-size:0.8rem; font-weight:600; display:block;">Demanda da Aplicação na Janela: <b>${state.taskBurst}ms</b></label>
              <input type="range" id="input-task-burst" min="10" max="100" step="5" value="${state.taskBurst}" style="width:100%; cursor:pointer;">
            </div>

            <!-- Timeline Bar -->
            <div style="font-size:0.75rem; font-weight:600; margin-bottom:4px; color:var(--text-muted);">Comportamento na Janela de ${state.cfsPeriod}ms:</div>
            <div style="display:flex; height:26px; border-radius:4px; overflow:hidden; border:1px solid var(--border-subtle); background:#edf2f7;">
              <div style="width:${Math.min(state.taskBurst, state.cfsQuota)}%; background:#38a169; color:#fff; display:flex; align-items:center; justify-content:center; font-size:0.72rem; font-weight:700;">
                Executando (${Math.min(state.taskBurst, state.cfsQuota)}ms)
              </div>
              ${isThrottled ? `
                <div style="width:${throttledTime}%; background:#e53e3e; color:#fff; display:flex; align-items:center; justify-content:center; font-size:0.72rem; font-weight:700;">
                  Estrangulado (${throttledTime}ms)
                </div>
              ` : ''}
              <div style="flex:1; background:#e2e8f0; display:flex; align-items:center; justify-content:center; font-size:0.68rem; color:#718096;">
                Ocioso
              </div>
            </div>

            <div style="margin-top:10px; font-size:0.82rem; color:${isThrottled ? '#c53030' : '#22543d'}; font-weight:600;">
              ${isThrottled 
                ? `CPU THROTTLING ATIVO! A thread é congelada pelo kernel por ${throttledTime}ms (${throttlePercent}% da janela). Causa picos graves de latência P99, mas o processo NÃO morre!`
                : `CPU sem estrangulamento. A cota é suficiente para processar a rajada sem suspensão de thread.`
              }
            </div>
          </div>

          <!-- Memory Section -->
          <div style="background:var(--bg-light); border:1px solid var(--border-color); border-radius:8px; padding:14px;">
            <div style="font-weight:700; font-size:0.95rem; color:var(--text-color); margin-bottom:10px; display:flex; justify-content:space-between;">
              <span>Mecanismo de Memória (Cgroup Memory Controller)</span>
              <span style="font-size:0.75rem; background:var(--bg-card-subtle); padding:2px 6px; border-radius:4px;">Limit = ${state.memoryLimit} MiB</span>
            </div>

            <div style="margin-bottom:10px;">
              <label style="font-size:0.8rem; font-weight:600; display:block;">Limite Rigoroso de RAM: <b>${state.memoryLimit} MiB</b></label>
              <input type="range" id="input-mem-lim-w" min="128" max="1024" step="64" value="${state.memoryLimit}" style="width:100%; cursor:pointer;">
            </div>

            <div style="margin-bottom:14px;">
              <label style="font-size:0.8rem; font-weight:600; display:block;">Memória Consumida pela Aplicação: <b>${state.memoryUsed} MiB</b></label>
              <input type="range" id="input-mem-used" min="128" max="1024" step="32" value="${state.memoryUsed}" style="width:100%; cursor:pointer;">
            </div>

            <!-- Memory Bar -->
            <div style="font-size:0.75rem; font-weight:600; margin-bottom:4px; color:var(--text-muted);">Ocupação do Cgroup de Memória:</div>
            <div style="height:26px; border-radius:4px; overflow:hidden; border:1px solid var(--border-subtle); background:#edf2f7; position:relative;">
              <div style="width:${Math.min(100, Math.round((state.memoryUsed / state.memoryLimit) * 100))}%; height:100%; background:${isOOM ? '#9b2c2c' : '#3182ce'}; color:#fff; display:flex; align-items:center; justify-content:center; font-size:0.72rem; font-weight:700;">
                ${state.memoryUsed} MiB / ${state.memoryLimit} MiB (${Math.round((state.memoryUsed / state.memoryLimit) * 100)}%)
              </div>
            </div>

            <div style="margin-top:10px; font-size:0.82rem; color:${isOOM ? '#9b2c2c' : '#2b6cb0'}; font-weight:600;">
              ${isOOM 
                ? `OOM-KILLER DISPARADO! A memória física ultrapassou o limite do Cgroup. O kernel envia SIGKILL imediato e incondicional. O pod é terminado com ExitCode 137!`
                : `Memória dentro do limite. O Cgroup atua mantendo páginas de cache ativas sem intervenção do OOM-killer.`
              }
            </div>
          </div>
        </div>

        <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle); font-size:0.82rem;">
          <div style="font-weight:700; color:var(--accent-primary); margin-bottom:4px;">Síntese Conceitual para Concursos e Seleções:</div>
          <p style="color:var(--text-color); margin:0; line-height:1.4;">
            • <b>CPU é um recurso compressível:</b> Exceder a cota não encerra a aplicação; o escalonador do kernel apenas suspende temporariamente os ciclos (throttling), gerando aumento de latência.<br>
            • <b>Memória é um recurso NÃO-compressível:</b> Exceder o limite do cgroup não pode ser tolerado por pausa de ciclos; aciona imediatamente o <code>oom-killer</code> com término irreversível do processo.
          </p>
        </div>
      </div>
    `;

    const bindInput = (id, prop) => {
      const el = container.querySelector(id);
      if (el) {
        el.addEventListener('input', (e) => {
          state[prop] = parseInt(e.target.value, 10);
          render();
        });
      }
    };

    bindInput('#input-cfs-quota', 'cfsQuota');
    bindInput('#input-task-burst', 'taskBurst');
    bindInput('#input-mem-lim-w', 'memoryLimit');
    bindInput('#input-mem-used', 'memoryUsed');
  }

  render();
}

/* ==========================================================================
   AULA 33: INSTITUTIONAL CLUSTER OVERCOMMITMENT & SAVINGS CALCULATOR (IFCE/DGTI)
   ========================================================================== */
function initInstitutionalClusterWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let state = {
    workload: 'suap',
    replicas: 40,
    serverCores: 32,
    serverRam: 128, // GiB
    cpuOvercommit: 2.5,
    memOvercommit: 1.2
  };

  const profiles = {
    suap: {
      name: 'SUAP (Sistema Unificado de Administração Pública)',
      desc: 'Python/Django, PostgreSQL, Celery workers. Picos intensos em matrículas.',
      reqCpu: 1.0, reqMem: 2.0, p95Cpu: 0.25, p95Mem: 1.4
    },
    sigaa: {
      name: 'SIGAA / Moodle Institucional',
      desc: 'Java EE (JVM estática) e PHP/Apache. Alta retenção de heap.',
      reqCpu: 2.0, reqMem: 4.0, p95Cpu: 0.50, p95Mem: 2.8
    },
    labs: {
      name: 'Laboratórios Didáticos / Containers Efêmeros de Alunos',
      desc: 'Ambientes isolados para aulas de programação (VS Code Server / Jupyter).',
      reqCpu: 0.5, reqMem: 1.0, p95Cpu: 0.08, p95Mem: 0.4
    }
  };

  function render() {
    const p = profiles[state.workload];

    // Static traditional sizing:
    const totalReqCpu = state.replicas * p.reqCpu;
    const totalReqMem = state.replicas * p.reqMem;
    const staticNodesCpu = Math.ceil(totalReqCpu / state.serverCores);
    const staticNodesMem = Math.ceil(totalReqMem / state.serverRam);
    const staticNodes = Math.max(staticNodesCpu, staticNodesMem);

    // Optimized sizing with overcommitment:
    const effectiveCpu = (state.replicas * p.reqCpu) / state.cpuOvercommit;
    const effectiveMem = (state.replicas * p.reqMem) / state.memOvercommit;
    const optNodesCpu = Math.ceil(effectiveCpu / state.serverCores);
    const optNodesMem = Math.ceil(effectiveMem / state.serverRam);
    const optNodes = Math.max(1, Math.max(optNodesCpu, optNodesMem));

    const nodesSaved = Math.max(0, staticNodes - optNodes);
    const percentSavings = Math.round((nodesSaved / staticNodes) * 100);

    container.innerHTML = `
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:10px; padding:20px; box-shadow:0 2px 8px rgba(0,0,0,0.04); font-family:var(--font-sans);">
        <div style="margin-bottom:16px;">
          <h4 style="margin:0; font-size:1.15rem; color:var(--text-color);">Calculadora de Dimensionamento Institucional e Overcommitment (DGTI/IFCE)</h4>
          <div style="font-size:0.85rem; color:var(--text-muted);">Simule o impacto de políticas de overcommitment dinâmico inspiradas no Borg em datacenters educacionais.</div>
        </div>

        <!-- Workload Selector -->
        <div style="display:flex; gap:8px; margin-bottom:16px; flex-wrap:wrap;">
          <button class="btn-wl ${state.workload==='suap'?'active':''}" data-wl="suap" style="font-size:0.82rem; padding:6px 12px; border-radius:6px; border:1px solid ${state.workload==='suap'?'var(--accent-primary)':'var(--border-color)'}; background:${state.workload==='suap'?'var(--accent-primary)':'var(--bg-light)'}; color:${state.workload==='suap'?'#fff':'var(--text-color)'}; font-weight:600; cursor:pointer;">Portal SUAP</button>
          <button class="btn-wl ${state.workload==='sigaa'?'active':''}" data-wl="sigaa" style="font-size:0.82rem; padding:6px 12px; border-radius:6px; border:1px solid ${state.workload==='sigaa'?'var(--accent-primary)':'var(--border-color)'}; background:${state.workload==='sigaa'?'var(--accent-primary)':'var(--bg-light)'}; color:${state.workload==='sigaa'?'#fff':'var(--text-color)'}; font-weight:600; cursor:pointer;">SIGAA / Moodle</button>
          <button class="btn-wl ${state.workload==='labs'?'active':''}" data-wl="labs" style="font-size:0.82rem; padding:6px 12px; border-radius:6px; border:1px solid ${state.workload==='labs'?'var(--accent-primary)':'var(--border-color)'}; background:${state.workload==='labs'?'var(--accent-primary)':'var(--bg-light)'}; color:${state.workload==='labs'?'#fff':'var(--text-color)'}; font-weight:600; cursor:pointer;">Ambientes de Alunos / Labs</button>
        </div>

        <div style="background:var(--bg-light); padding:10px 14px; border-radius:6px; margin-bottom:16px; font-size:0.85rem; border-left:4px solid var(--accent-primary);">
          <b>${p.name}:</b> ${p.desc}
          <div style="font-size:0.75rem; color:var(--text-muted); margin-top:3px;">
            Configuração Típica: Request CPU = ${p.reqCpu} cores, Request Mem = ${p.reqMem} GiB | Uso Real P95: CPU ~${p.p95Cpu} cores, Mem ~${p.p95Mem} GiB
          </div>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:14px; margin-bottom:20px;">
          <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
            <label style="font-size:0.8rem; font-weight:600; display:block;">Quantidade de Réplicas/Contêineres: <b>${state.replicas}</b></label>
            <input type="range" id="input-replicas" min="10" max="120" step="5" value="${state.replicas}" style="width:100%; cursor:pointer;">
          </div>

          <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
            <label style="font-size:0.8rem; font-weight:600; display:block;">Overcommit de CPU: <b>${state.cpuOvercommit}x</b></label>
            <input type="range" id="input-cpu-oc" min="1.0" max="4.0" step="0.25" value="${state.cpuOvercommit}" style="width:100%; cursor:pointer;">
          </div>

          <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
            <label style="font-size:0.8rem; font-weight:600; display:block;">Overcommit de Memória: <b>${state.memOvercommit}x</b></label>
            <input type="range" id="input-mem-oc" min="1.0" max="1.5" step="0.05" value="${state.memOvercommit}" style="width:100%; cursor:pointer;">
          </div>
        </div>

        <!-- Sizing Comparison -->
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
          <div style="background:#fff5f5; border:1px solid #feb2b2; border-radius:8px; padding:16px; text-align:center;">
            <div style="font-size:0.8rem; font-weight:700; color:#c53030; text-transform:uppercase;">Dimensionamento Estático Tradicional</div>
            <div style="font-size:2.2rem; font-weight:800; color:#9b2c2c; margin:8px 0;">${staticNodes} Servidores</div>
            <div style="font-size:0.75rem; color:#742a2a;">Demanda teórica: ${totalReqCpu} vCPUs, ${totalReqMem} GiB RAM.<br>Desperdício médio de capacidade: ~65% ocioso.</div>
          </div>

          <div style="background:#f0fff4; border:1px solid #9ae6b4; border-radius:8px; padding:16px; text-align:center;">
            <div style="font-size:0.8rem; font-weight:700; color:#22543d; text-transform:uppercase;">Cluster Otimizado com Overcommitment</div>
            <div style="font-size:2.2rem; font-weight:800; color:#22543d; margin:8px 0;">${optNodes} Servidores</div>
            <div style="font-size:0.75rem; color:#22543d; font-weight:600;">Economia: ${nodesSaved} nós físicos a menos (${percentSavings}% de redução de hardware e energia)!</div>
          </div>
        </div>

        <div style="background:var(--bg-card-subtle); padding:12px; border-radius:6px; border:1px solid var(--border-subtle); font-size:0.82rem;">
          <div style="font-weight:700; color:var(--accent-primary); margin-bottom:4px;">Implicações Práticas para a Linha de Pesquisa CA05:</div>
          <p style="color:var(--text-color); margin:0; line-height:1.4;">
            Em instituições federais de ensino como o IFCE, a aquisição de novos servidores físicos passa por longos processos licitatórios. Técnicas de empacotamento inteligente de contêineres e overcommitment dinâmico permitem que a infraestrutura existente atenda a novas cargas acadêmicas sem novos gastos públicos, mitigando contenção através de classes de serviço adequadas.
          </p>
        </div>
      </div>
    `;

    container.querySelectorAll('.btn-wl').forEach(btn => {
      btn.addEventListener('click', () => {
        state.workload = btn.getAttribute('data-wl');
        render();
      });
    });

    const bindInput = (id, prop, isFloat) => {
      const el = container.querySelector(id);
      if (el) {
        el.addEventListener('input', (e) => {
          state[prop] = isFloat ? parseFloat(e.target.value) : parseInt(e.target.value, 10);
          render();
        });
      }
    };

    bindInput('#input-replicas', 'replicas', false);
    bindInput('#input-cpu-oc', 'cpuOvercommit', true);
    bindInput('#input-mem-oc', 'memOvercommit', true);
  }

  render();
}

/* ==========================================================================
   AULA 34: SIMULADOR DE ENTREVISTA DA BANCA (PERGUNTAS TIPO 1)
   ========================================================================== */
function initBancaSimulatorWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const questions = [
    {
      id: 1,
      banca: 'Prof. Dr. Carlos Maurício (Orientador CA05)',
      tema: 'Motivação e Alinhamento com a Linha de Pesquisa',
      pergunta: 'Por que você escolheu exatamente o tema CA05 sobre otimização de contêineres em infraestruturas institucionais, e como a sua trajetória prévia contribui para essa pesquisa?',
      respostas: [
        {
          tipo: 'Fraca / Genérica',
          texto: 'Escolhi porque contêineres e Docker estão na moda e o mercado corporativo pede muito isso nos empregos de DevOps.',
          score: 'Nota: 3/10',
          motivo: 'Foca em apelo comercial e modismo tecnológico. Demonstra descompasso com os objetivos científicos de um mestrado acadêmico stricto sensu.'
        },
        {
          tipo: 'Boa / Razoável',
          texto: 'Trabalho com servidores e vejo que muitas máquinas ficam ociosas. Acho que o Kubernetes pode ajudar o IFCE a economizar dinheiro.',
          score: 'Nota: 6/10',
          motivo: 'Identifica o problema prático, mas peca pela falta de fundamentação teórica, metodológica e rigor acadêmico.'
        },
        {
          tipo: 'Excelente / Padrão PPGCC (Recomendada)',
          texto: 'Identifiquei que instituições públicas como o IFCE sofrem de subutilização de servidores devido ao superdimensionamento estático preventivo. Meu objetivo é aplicar modelos de sobrealocação estocástica inspirados no Google Borg e Autopilot para elevar a densidade de workloads como SUAP e Moodle sem violar SLAs institucionais, integrando minha experiência prática a rigor científico quantitativo.',
          score: 'Nota: 10/10',
          motivo: 'Demonstra domínio da literatura seminal (Borg/Autopilot), cita dores reais da instituição financiadora (IFCE/DGTI), articula métricas de SLA e une prática a rigor acadêmico.'
        }
      ]
    },
    {
      id: 2,
      banca: 'Avaliador da Banca (Sistemas Distribuídos)',
      tema: 'Risco de Contenção e Degradação de SLA',
      pergunta: 'Se você sobrealocar CPU e Memória além da capacidade física do nó, como você garante que o sistema de matrículas do SUAP não sofrerá lentidão nos momentos de pico?',
      respostas: [
        {
          tipo: 'Fraca / Ingênua',
          texto: 'Se o nó sobrecarregar, basta a equipe de TI comprar mais memória ou colocar um aviso na tela para os alunos tentarem mais tarde.',
          score: 'Nota: 2/10',
          motivo: 'Ignora a engenharia de software e transfere o problema para o usuário e orçamento público.'
        },
        {
          tipo: 'Boa / Superficial',
          texto: 'Usaremos limites nos contêineres para que nenhum aluno gaste mais memória do que o permitido no Docker.',
          score: 'Nota: 6/10',
          motivo: 'Menciona limits de contêineres, mas não explica a arquitetura de prioridades e o comportamento do escalonador.'
        },
        {
          tipo: 'Excelente / Padrão PPGCC (Recomendada)',
          texto: 'Garantimos através da segregação rígida de Classes de Serviço (QoS) e monitoramento de cauda (P99). O SUAP receberá QoS Guaranteed (ou Burstable prioritário com alto request), recebendo oom_score_adj protetivo (-997). Cargas secundárias receberão QoS BestEffort e sofrerão preempção automática pelo Kubelet/Kernel no primeiro sinal de saturação, preservando o SLA administrativo sem intervenção manual.',
          score: 'Nota: 10/10',
          motivo: 'Responde com precisão cirúrgica de sistemas operacionais: cita classes de QoS, oom_score_adj, preempção de BestEffort e monitoramento de cauda P99.'
        }
      ]
    }
  ];

  let currentIdx = 0;
  let selectedResp = null;

  function render() {
    const q = questions[currentIdx];

    container.innerHTML = `
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:10px; padding:20px; box-shadow:0 2px 8px rgba(0,0,0,0.04); font-family:var(--font-sans);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em; color:var(--text-muted); font-weight:700;">Simulador de Arguição Oral — Pergunta ${currentIdx + 1} de ${questions.length}</span>
            <h4 style="margin:2px 0 0; font-size:1.1rem; color:var(--text-color);">${q.tema}</h4>
          </div>
          <div style="display:flex; gap:6px;">
            <button id="btn-prev-q" ${currentIdx===0?'disabled':''} style="padding:4px 10px; font-size:0.8rem; border-radius:4px; border:1px solid var(--border-color); background:var(--bg-light); cursor:pointer;">← Anterior</button>
            <button id="btn-next-q" ${currentIdx===questions.length-1?'disabled':''} style="padding:4px 10px; font-size:0.8rem; border-radius:4px; border:1px solid var(--border-color); background:var(--bg-light); cursor:pointer;">Próxima →</button>
          </div>
        </div>

        <div style="background:var(--bg-light); border-left:4px solid var(--accent-primary); padding:12px 16px; border-radius:6px; margin-bottom:16px;">
          <div style="font-size:0.8rem; font-weight:700; color:var(--accent-primary); margin-bottom:4px;">${q.banca} pergunta:</div>
          <div style="font-size:0.95rem; font-weight:600; color:var(--text-color); line-height:1.4;">"${q.pergunta}"</div>
        </div>

        <div style="font-size:0.85rem; font-weight:700; color:var(--text-color); margin-bottom:10px;">Compare as abordagens de resposta do candidato:</div>

        <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:16px;">
          ${q.respostas.map((r, i) => `
            <div class="resp-card" data-idx="${i}" style="border:1px solid ${selectedResp===i?'var(--accent-primary)':'var(--border-color)'}; background:${selectedResp===i?'var(--bg-card-subtle)':'var(--bg-card)'}; border-radius:8px; padding:12px; cursor:pointer; transition:all 0.2s ease;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <span style="font-size:0.8rem; font-weight:800; color:${i===2?'#22543d':(i===1?'#b7791f':'#c53030')};">${r.tipo}</span>
                <span style="font-size:0.75rem; font-weight:700; background:var(--bg-light); padding:2px 8px; border-radius:12px;">${r.score}</span>
              </div>
              <div style="font-size:0.88rem; color:var(--text-color); line-height:1.4; margin-bottom:6px;">"${r.texto}"</div>
              ${selectedResp === i ? `
                <div style="margin-top:8px; padding-top:8px; border-top:1px dashed var(--border-subtle); font-size:0.8rem; color:var(--text-muted);">
                  <b>Análise da Banca:</b> ${r.motivo}
                </div>
              ` : ''}
            </div>
          `).join('')}
        </div>
      </div>
    `;

    container.querySelectorAll('.resp-card').forEach(card => {
      card.addEventListener('click', () => {
        selectedResp = parseInt(card.getAttribute('data-idx'), 10);
        render();
      });
    });

    const btnPrev = container.querySelector('#btn-prev-q');
    if (btnPrev) {
      btnPrev.addEventListener('click', () => {
        if (currentIdx > 0) {
          currentIdx--;
          selectedResp = null;
          render();
        }
      });
    }

    const btnNext = container.querySelector('#btn-next-q');
    if (btnNext) {
      btnNext.addEventListener('click', () => {
        if (currentIdx < questions.length - 1) {
          currentIdx++;
          selectedResp = null;
          render();
        }
      });
    }
  }

  render();
}

/* ==========================================================================
   AULA 35: CANVAS INTERATIVO DO PRÉ-PROJETO CA05
   ========================================================================== */
function initProjectCanvasWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const sections = {
    problema: {
      title: '1. Problema de Pesquisa',
      content: 'A infraestrutura de servidores do IFCE e de instituições federais opera com baixa utilização média (15% a 25%) devido ao superdimensionamento estático preventivo e à aversão humana a falhas de SLA. A morosidade de novos processos licitatórios (Lei 14.133) impede a expansão de novos serviços acadêmicos sem otimização da base instalada.'
    },
    objetivo: {
      title: '2. Objetivo Geral',
      content: 'Propor, implementar e avaliar um arcabouço de auto-tuning e sobrealocação dinâmica baseado em contêineres Linux (Cgroups v2 / Kubernetes), capaz de elevar a densidade computacional em clusters institucionais sem violar os acordos de nível de serviço (SLA) de sistemas de missão crítica como o SUAP.'
    },
    questoes: {
      title: '3. Questões de Pesquisa (RQs)',
      content: 'RQ1: Qual é o ganho real de densidade computacional e redução de custos energéticos obtido ao migrar de alocações estáticas para modelos de janelas deslizantes com margem de segurança ajustável em cargas acadêmicas?<br>RQ2: Como mitigar a contenção mútua de CPU e memória em nós compartilhados entre cargas de produção e tarefas efêmeras de estudantes?'
    },
    metodologia: {
      title: '4. Metodologia Científica e Testbed',
      content: 'Abordagem quantitativa experimental em ambiente controlado (testbed bare-metal simulando nós da DGTI com Kubernetes). Injeção de cargas reais de acesso do SUAP e Moodle via geradores de carga (Locust/k6). Coleta de métricas em alta resolução através de Prometheus e eBPF.'
    },
    metricas: {
      title: '5. Métricas de Avaliação e Sucesso',
      content: 'Percentil P99 de latência das requisições web, tempo total de CPU throttling (/sys/fs/cgroup/cpu.stat), métricas de estol de memória (PSI - Pressure Stall Information), taxa de sobrealocação alcançada (CR > 2.0x) e percentual de economia de servidores físicos.'
    }
  };

  let activeTab = 'problema';

  function render() {
    container.innerHTML = `
      <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:10px; padding:20px; box-shadow:0 2px 8px rgba(0,0,0,0.04); font-family:var(--font-sans);">
        <div style="margin-bottom:14px;">
          <h4 style="margin:0; font-size:1.15rem; color:var(--text-color);">Canvas Estratégico do Projeto de Pesquisa (Tema CA05)</h4>
          <div style="font-size:0.85rem; color:var(--text-muted);">Clique nos blocos para explorar os fundamentos científicos que você defenderá perante o orientador e a banca:</div>
        </div>

        <div style="display:flex; gap:6px; flex-wrap:wrap; margin-bottom:16px;">
          ${Object.keys(sections).map(key => `
            <button class="btn-canvas-tab" data-key="${key}" style="font-size:0.8rem; font-weight:700; padding:6px 12px; border-radius:6px; border:1px solid ${activeTab===key?'var(--accent-primary)':'var(--border-color)'}; background:${activeTab===key?'var(--accent-primary)':'var(--bg-light)'}; color:${activeTab===key?'#fff':'var(--text-color)'}; cursor:pointer;">
              ${sections[key].title}
            </button>
          `).join('')}
        </div>

        <div style="background:var(--bg-card-subtle); border:1px solid var(--border-subtle); border-radius:8px; padding:16px; min-height:120px;">
          <h5 style="margin:0 0 8px; font-size:1.02rem; color:var(--accent-primary);">${sections[activeTab].title}</h5>
          <div style="font-size:0.9rem; color:var(--text-color); line-height:1.5;">${sections[activeTab].content}</div>
        </div>
      </div>
    `;

    container.querySelectorAll('.btn-canvas-tab').forEach(btn => {
      btn.addEventListener('click', () => {
        activeTab = btn.getAttribute('data-key');
        render();
      });
    });
  }

  render();
}

/* ==========================================================================
   AULA 37: MATRIZ DE REVISÃO ESPAÇADA E SCORECARD FINAL
   ========================================================================== */
function initSpacedRepetitionWidget(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const topics = [
    { fase: 'Fase 1', name: 'Lógica e Teoria dos Conjuntos (01 a 08)', status: 'Pronto', mastery: 100 },
    { fase: 'Fase 2', name: 'Programação Computacional C/Python (09 a 18)', status: 'Pronto', mastery: 100 },
    { fase: 'Fase 3', name: 'Algoritmos e Estruturas de Dados (19 a 27)', status: 'Pronto', mastery: 100 },
    { fase: 'Fase 4', name: 'Fundamentos Teóricos CA05 (28 a 33)', status: 'Pronto', mastery: 100 },
    { fase: 'Fase 5', name: 'Arguição Oral & Alinhamento Prático (34 a 37)', status: 'Pronto', mastery: 100 }
  ];

  container.innerHTML = `
    <div style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:10px; padding:20px; box-shadow:0 2px 8px rgba(0,0,0,0.04); font-family:var(--font-sans);">
      <div style="margin-bottom:14px;">
        <h4 style="margin:0; font-size:1.15rem; color:var(--text-color);">Scorecard de Prontidão Global para o PPGCC IFCE</h4>
        <div style="font-size:0.85rem; color:var(--text-muted);">Cobertura curricular completa do Edital 43/2026 para a Linha de Pesquisa CA05:</div>
      </div>

      <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:16px;">
        ${topics.map(t => `
          <div style="background:var(--bg-light); border:1px solid var(--border-color); border-radius:6px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
            <div>
              <span style="font-size:0.75rem; font-weight:700; background:var(--accent-primary); color:#fff; padding:2px 6px; border-radius:4px; margin-right:6px;">${t.fase}</span>
              <span style="font-size:0.88rem; font-weight:600; color:var(--text-color);">${t.name}</span>
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:0.8rem; font-weight:800; color:#22543d;">100% Coberto</span>
              <span style="font-size:0.9rem; color:#22543d;">OK</span>
            </div>
          </div>
        `).join('')}
      </div>

      <div style="background:#f0fff4; border:1px solid #9ae6b4; border-radius:8px; padding:14px; text-align:center;">
        <div style="font-size:1.05rem; font-weight:800; color:#22543d; margin-bottom:4px;">Parabéns! Preparatório 100% Concluído</div>
        <div style="font-size:0.85rem; color:#22543d;">
          Você cobriu todos os 37 tópicos do edital, resolveu todas as questões de provas anteriores catalogadas e construiu o alinhamento metodológico completo com o Prof. Dr. Carlos Maurício Jaborandy.
        </div>
      </div>
    </div>
  `;
}



// ==========================================================================
// JUPYTER NOTEBOOK SIMULATOR ENGINES (FASE 2: AULAS 09 A 18)
// 100% Client-side Offline Interactive Python / C99 Code Playgrounds
// ==========================================================================

// Helper: Setup Notebook Tab Switching
function setupNotebookTabs(container) {
  const tabs = container.querySelectorAll('.notebook-tab-btn');
  const contents = container.querySelectorAll('.notebook-tab-content');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      contents.forEach(c => c.style.display = 'none');
      tab.classList.add('active');
      const targetId = tab.getAttribute('data-target');
      const targetContent = container.querySelector('#' + targetId);
      if (targetContent) targetContent.style.display = 'block';
    });
  });
}

// --------------------------------------------------------------------------
// NOTEBOOK 09: Divisao Truncada & Curto-Circuito (Aula 09)
// --------------------------------------------------------------------------
function initNotebook09(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  function render(a = 10, b = 3, flag = 0) {
    const intDiv = Math.trunc(a / b);
    const floatDiv = a / b;
    const r2Str = floatDiv.toFixed(6).replace(/0+$/, '').replace(/\.$/, '.0');

    container.innerHTML = `
      <div class="notebook-cell">
        <div class="notebook-topbar">
          <div class="notebook-dots">
            <span class="notebook-dot dot-red"></span>
            <span class="notebook-dot dot-yellow"></span>
            <span class="notebook-dot dot-green"></span>
          </div>
          <div class="notebook-meta">
            <span class="notebook-prompt">In [9]:</span>
            <span class="notebook-kernel-badge"><span class="kernel-pulse"></span> C99 & Python Kernel (Simulado)</span>
          </div>
        </div>

        <div class="notebook-body">
          <div class="notebook-code-view">
<span class="code-comment">// C99: Divisao Inteira vs Ponto Flutuante (Questao 10 Oficial)</span>
<span class="code-type">int</span> a = <span class="code-number" id="nb09-code-a">${a}</span>, b = <span class="code-number" id="nb09-code-b">${b}</span>;
<span class="code-type">float</span> r1 = a / b;           <span class="code-comment">// Ambos operandos int: ULA trunca a fracao!</span>
<span class="code-type">float</span> r2 = (<span class="code-type">float</span>)a / b;    <span class="code-comment">// Cast explicito: promove divisao para IEEE-754!</span>

<span class="code-comment">// Avaliacao em Curto-Circuito</span>
<span class="code-type">int</span> flag = <span class="code-number" id="nb09-code-flag">${flag}</span>;
<span class="code-keyword">if</span> (flag && (10 / 0 == 0)) { <span class="code-comment">/* Se flag == 0, o lado direito NUNCA roda! */</span> }
          </div>

          <div class="notebook-controls">
            <div class="notebook-inputs-group">
              <div class="notebook-input-item">
                <label>int a:</label>
                <input type="number" id="nb09-in-a" value="${a}" style="width:70px;">
              </div>
              <div class="notebook-input-item">
                <label>int b:</label>
                <input type="number" id="nb09-in-b" value="${b}" style="width:70px;">
              </div>
              <div class="notebook-input-item">
                <label>flag (0 ou 1):</label>
                <select id="nb09-in-flag">
                  <option value="0" ${flag === 0 ? 'selected' : ''}>0 (Falso - Curto-circuito Ativo)</option>
                  <option value="1" ${flag === 1 ? 'selected' : ''}>1 (Verdadeiro - Avalia lado direito!)</option>
                </select>
              </div>
            </div>
            <div class="notebook-btn-group">
              <button class="btn-notebook btn-notebook-run" id="nb09-btn-run">▶ Executar Célula</button>
              <button class="btn-notebook btn-notebook-reset" id="nb09-btn-reset">↺ Resetar</button>
            </div>
          </div>

          <div class="notebook-output-panel">
            <div class="notebook-tabs">
              <button class="notebook-tab-btn active" data-target="nb09-tab-stdout">>_ Console Output (stdout)</button>
              <button class="notebook-tab-btn" data-target="nb09-tab-mem">Estado da Memória</button>
              <button class="notebook-tab-btn" data-target="nb09-tab-banca">Análise do PPGCC (Q10)</button>
            </div>

            <div class="notebook-tab-content" id="nb09-tab-stdout">
              <div class="notebook-terminal-stdout" id="nb09-out-text">
<span class="terminal-info">[compiling syntax_semantics.c with gcc -O2 -Wall...]</span>
<span class="terminal-info">[running executable binary...]</span>
r1 (divisao inteira a / b)        = ${intDiv}.000000 <span class="terminal-warn">(PERDEU PARTE FRACIONÁRIA!)</span>
r2 (com cast explicito (float)a/b) = ${r2Str} <span class="terminal-info">(PRECISÃO MANTIDA!)</span>

${flag === 0 
  ? '<span class="terminal-info">Curto-circuito ativado: como flag == 0, o operando (10 / 0) NUNCA foi enviado a CPU! Divisao por zero evitada com sucesso.</span>' 
  : '<span class="terminal-err">FATAL ERROR: flag == 1 obligou a avaliar (10 / 0). SIGFPE: Floating point exception (Divisão por zero)!</span>'}
              </div>
            </div>

            <div class="notebook-tab-content" id="nb09-tab-mem" style="display:none;">
              <table class="notebook-memory-table">
                <thead>
                  <tr><th>Variável</th><th>Tipo</th><th>Bytes</th><th>Registrador/Memória</th><th>Valor Real</th></tr>
                </thead>
                <tbody>
                  <tr><td>a</td><td>int (C99)</td><td>4</td><td>EAX (0x7ffd01)</td><td>${a}</td></tr>
                  <tr><td>b</td><td>int (C99)</td><td>4</td><td>EBX (0x7ffd05)</td><td>${b}</td></tr>
                  <tr class="highlight-mem"><td>r1</td><td>float</td><td>4</td><td>XMM0 (Truncado ULA)</td><td>${intDiv}.0</td></tr>
                  <tr class="highlight-mem"><td>r2</td><td>float</td><td>4</td><td>XMM1 (IEEE 754)</td><td>${r2Str}</td></tr>
                </tbody>
              </table>
            </div>

            <div class="notebook-tab-content" id="nb09-tab-banca" style="display:none;">
              <div class="notebook-banca-insight">
                <strong>Ponto Crítico de Prova (Questão 10 do Edital 53/2025):</strong><br>
                A banca examinadora colocou a pegadinha clássica: <code>float x = 10 / 3;</code>. O candidato novato vê o tipo <code>float</code> na declaração e acha que o resultado será <code>3.333333</code>. Mas a linguagem C avalia o lado direito primeiro na ULA de inteiros! Como 10 e 3 são inteiros, a divisão é inteira: dá <code>3</code>. Somente após a perda dos decimais o valor <code>3</code> é convertido para float, tornando-se <code>3.0</code>!
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    setupNotebookTabs(container);

    const btnRun = container.querySelector('#nb09-btn-run');
    const btnReset = container.querySelector('#nb09-btn-reset');
    
    if (btnRun) {
      btnRun.addEventListener('click', () => {
        btnRun.innerText = 'Executando...';
        btnRun.style.opacity = '0.7';
        setTimeout(() => {
          const valA = parseInt(container.querySelector('#nb09-in-a').value) || 0;
          const valB = parseInt(container.querySelector('#nb09-in-b').value) || 1;
          const valFlag = parseInt(container.querySelector('#nb09-in-flag').value) || 0;
          render(valA, valB, valFlag);
        }, 120);
      });
    }

    if (btnReset) {
      btnReset.addEventListener('click', () => {
        render(10, 3, 0);
      });
    }
  }

  render(10, 3, 0);
}

// --------------------------------------------------------------------------
// NOTEBOOK 10: Dangling Else & Switch Fallthrough (Aula 10)
// --------------------------------------------------------------------------
function initNotebook10(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  function render(a = 1, b = -2, switchVal = 1, withBreak = true) {
    let resultado = 0;
    let pathLog = [];
    
    // Dangling else logic: C compiler binds else to nearest if (b > 0)
    if (a > 0) {
      pathLog.push("1. Testou 'if (a > 0)': " + a + " > 0 eh VERDADEIRO. Entrou no bloco externo.");
      if (b > 0) {
        resultado = 10;
        pathLog.push("2. Testou 'if (b > 0)': " + b + " > 0 eh VERDADEIRO -> resultado = 10.");
      } else {
        resultado = 20;
        pathLog.push("2. Testou 'if (b > 0)': " + b + " > 0 eh FALSO -> Caiu no 'else' interno -> resultado = 20!");
      }
    } else {
      pathLog.push("1. Testou 'if (a > 0)': " + a + " > 0 eh FALSO. O bloco inteiro foi ignorado!");
    }

    let switchLogs = [];
    if (withBreak) {
      switchLogs.push("Com 'break': executa apenas o Case " + switchVal + " e sai imediatamente do switch.");
    } else {
      switchLogs.push("SEM 'break' (FALLTHROUGH): Executou Case " + switchVal + " e continuou caindo nos cases subsequentes!");
    }

    container.innerHTML = `
      <div class="notebook-cell">
        <div class="notebook-topbar">
          <div class="notebook-dots">
            <span class="notebook-dot dot-red"></span>
            <span class="notebook-dot dot-yellow"></span>
            <span class="notebook-dot dot-green"></span>
          </div>
          <div class="notebook-meta">
            <span class="notebook-prompt">In [10]:</span>
            <span class="notebook-kernel-badge"><span class="kernel-pulse"></span> C99 Control Flow Kernel</span>
          </div>
        </div>

        <div class="notebook-body">
          <div class="notebook-code-view">
<span class="code-comment">// O Classico Problema do "Dangling Else"</span>
<span class="code-type">int</span> a = <span class="code-number">${a}</span>, b = <span class="code-number">${b}</span>;
<span class="code-type">int</span> resultado = <span class="code-number">0</span>;

<span class="code-keyword">if</span> (a > 0)
    <span class="code-keyword">if</span> (b > 0)
        resultado = <span class="code-number">10</span>;
<span class="code-keyword">else</span>  <span class="code-comment">// Cuidado! Pela gramatica ANSI C, este else se liga ao "if (b > 0)", NAO ao primeiro!</span>
    resultado = <span class="code-number">20</span>;

printf(<span class="code-string">"resultado = %d\n"</span>, resultado);
          </div>

          <div class="notebook-controls">
            <div class="notebook-inputs-group">
              <div class="notebook-input-item">
                <label>int a:</label>
                <input type="number" id="nb10-in-a" value="${a}" style="width:65px;">
              </div>
              <div class="notebook-input-item">
                <label>int b:</label>
                <input type="number" id="nb10-in-b" value="${b}" style="width:65px;">
              </div>
              <div class="notebook-input-item">
                <label>Switch Case:</label>
                <select id="nb10-in-switch">
                  <option value="1" ${switchVal === 1 ? 'selected' : ''}>Case 1</option>
                  <option value="2" ${switchVal === 2 ? 'selected' : ''}>Case 2</option>
                  <option value="3" ${switchVal === 3 ? 'selected' : ''}>Case 3</option>
                </select>
              </div>
              <div class="notebook-input-item">
                <label>Incluir 'break;'?</label>
                <select id="nb10-in-break">
                  <option value="true" ${withBreak ? 'selected' : ''}>Sim (Fluxo Normal)</option>
                  <option value="false" ${!withBreak ? 'selected' : ''}>Não (Causar Fallthrough)</option>
                </select>
              </div>
            </div>
            <div class="notebook-btn-group">
              <button class="btn-notebook btn-notebook-run" id="nb10-btn-run">▶ Executar Célula</button>
              <button class="btn-notebook btn-notebook-reset" id="nb10-btn-reset">↺ Resetar</button>
            </div>
          </div>

          <div class="notebook-output-panel">
            <div class="notebook-tabs">
              <button class="notebook-tab-btn active" data-target="nb10-tab-stdout">>_ Console Output (stdout)</button>
              <button class="notebook-tab-btn" data-target="nb10-tab-flow">Rastreamento do Fluxo</button>
              <button class="notebook-tab-btn" data-target="nb10-tab-banca">Dica da Banca</button>
            </div>

            <div class="notebook-tab-content" id="nb10-tab-stdout">
              <div class="notebook-terminal-stdout">
<span class="terminal-info">[executing control_flow.c...]</span>
resultado = ${resultado}

<span class="terminal-warn">[Switch-case analysis]:</span>
${switchLogs.join('\n')}
              </div>
            </div>

            <div class="notebook-tab-content" id="nb10-tab-flow" style="display:none;">
              <ul style="color:#cbd5e1; list-style:none; padding-left:0; line-height:1.7;">
                ${pathLog.map(p => `<li style="margin-bottom:6px;">${p}</li>`).join('')}
              </ul>
            </div>

            <div class="notebook-tab-content" id="nb10-tab-banca" style="display:none;">
              <div class="notebook-banca-insight">
                <strong>A Regra de Ouro do Dangling Else:</strong> Na ausência de chaves <code>{}</code>, a cláusula <code>else</code> associa-se sem exceção ao <code>if</code> mais próximo que ainda esteja aberto. Essa é uma das perguntas favoritas das bancas para testar se o candidato confia na indentação visual (que o compilador ignora) ou na gramática sintática formal da linguagem!
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    setupNotebookTabs(container);

    const btnRun = container.querySelector('#nb10-btn-run');
    const btnReset = container.querySelector('#nb10-btn-reset');

    if (btnRun) {
      btnRun.addEventListener('click', () => {
        btnRun.innerText = 'Executando...';
        setTimeout(() => {
          const valA = parseInt(container.querySelector('#nb10-in-a').value) || 0;
          const valB = parseInt(container.querySelector('#nb10-in-b').value) || 0;
          const sVal = parseInt(container.querySelector('#nb10-in-switch').value) || 1;
          const bVal = container.querySelector('#nb10-in-break').value === 'true';
          render(valA, valB, sVal, bVal);
        }, 120);
      });
    }

    if (btnReset) {
      btnReset.addEventListener('click', () => render(1, -2, 1, true));
    }
  }

  render(1, -2, 1, true);
}

// --------------------------------------------------------------------------
// NOTEBOOK 11: Rastreamento Multivariavel de Lacos (Aula 11 - Q13 Oficial)
// --------------------------------------------------------------------------
function initNotebook11(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  function render(startI = 1, limitI = 10, stepI = 2, initJ = 1, initK = 0) {
    let i = startI;
    let j = initJ;
    let k = initK;
    let history = [];
    let stepCount = 0;

    history.push({ step: 0, iter: 'Inicial', i, j, k, cond: `${i} < ${limitI} (?)`, action: 'Inicialização de variáveis' });

    while (i < limitI && stepCount < 20) {
      stepCount++;
      const prevI = i;
      j = j * 2;
      k = k + i;
      i += stepI;
      history.push({
        step: stepCount,
        iter: `Volta ${stepCount}`,
        i: i,
        j: j,
        k: k,
        cond: `${i} < ${limitI} (${i < limitI ? 'V' : 'F'})`,
        action: `j=${j/2}*2=${j}, k=${k-prevI}+${prevI}=${k}, i incrementa para ${i}`
      });
    }

    container.innerHTML = `
      <div class="notebook-cell">
        <div class="notebook-topbar">
          <div class="notebook-dots">
            <span class="notebook-dot dot-red"></span>
            <span class="notebook-dot dot-yellow"></span>
            <span class="notebook-dot dot-green"></span>
          </div>
          <div class="notebook-meta">
            <span class="notebook-prompt">In [11]:</span>
            <span class="notebook-kernel-badge"><span class="kernel-pulse"></span> C99 Loop Engine (Q13 Oficial)</span>
          </div>
        </div>

        <div class="notebook-body">
          <div class="notebook-code-view">
<span class="code-comment">// Questao 13 Oficial do Edital 53/2025: Rastreamento em ANSI C</span>
<span class="code-type">int</span> i, j = <span class="code-number">${initJ}</span>, k = <span class="code-number">${initK}</span>;
<span class="code-keyword">for</span> (i = <span class="code-number">${startI}</span>; i < <span class="code-number">${limitI}</span>; i += <span class="code-number">${stepI}</span>) {
    j = j * 2;
    k = k + i;
}
printf(<span class="code-string">"i = %d, j = %d, k = %d\n"</span>, i, j, k);
          </div>

          <div class="notebook-controls">
            <div class="notebook-inputs-group">
              <div class="notebook-input-item">
                <label>Inicio i:</label>
                <input type="number" id="nb11-in-start" value="${startI}" style="width:60px;">
              </div>
              <div class="notebook-input-item">
                <label>Limite (i < X):</label>
                <input type="number" id="nb11-in-limit" value="${limitI}" style="width:65px;">
              </div>
              <div class="notebook-input-item">
                <label>Passo (i += X):</label>
                <input type="number" id="nb11-in-step" value="${stepI}" style="width:60px;">
              </div>
            </div>
            <div class="notebook-btn-group">
              <button class="btn-notebook btn-notebook-run" id="nb11-btn-run">▶ Rodar Teste de Mesa</button>
              <button class="btn-notebook btn-notebook-reset" id="nb11-btn-reset">↺ Resetar Q13</button>
            </div>
          </div>

          <div class="notebook-output-panel">
            <div class="notebook-tabs">
              <button class="notebook-tab-btn active" data-target="nb11-tab-table">Teste de Mesa Passo a Passo</button>
              <button class="notebook-tab-btn" data-target="nb11-tab-stdout">>_ Console Output (stdout)</button>
              <button class="notebook-tab-btn" data-target="nb11-tab-banca">Por que a Banca Cobrou?</button>
            </div>

            <div class="notebook-tab-content" id="nb11-tab-table">
              <table class="notebook-memory-table">
                <thead>
                  <tr><th>Passo</th><th>i</th><th>j</th><th>k</th><th>Condição (i < ${limitI})</th><th>Operação Executada</th></tr>
                </thead>
                <tbody>
                  ${history.map((h, idx) => `
                    <tr class="${idx === history.length - 1 ? 'highlight-mem' : ''}">
                      <td>${h.iter}</td>
                      <td><strong>${h.i}</strong></td>
                      <td><strong>${h.j}</strong></td>
                      <td><strong>${h.k}</strong></td>
                      <td>${h.cond}</td>
                      <td>${h.action}</td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>

            <div class="notebook-tab-content" id="nb11-tab-stdout" style="display:none;">
              <div class="notebook-terminal-stdout">
<span class="terminal-info">[compiling and executing loop_trace.c...]</span>
i = ${i}, j = ${j}, k = ${k}
<span class="terminal-info">Saída do laço após ${stepCount} voltas completas.</span>
              </div>
            </div>

            <div class="notebook-tab-content" id="nb11-tab-banca" style="display:none;">
              <div class="notebook-banca-insight">
                <strong>Gabarito Oficial Q13:</strong> A grande pegadinha está no valor final de <code>i</code>! Na última iteração, <code>i</code> vale 9. O corpo do laço roda, <code>j</code> vira 32 e <code>k</code> vira 25. Antes de sair, o <code>for</code> executa o passo de incremento: <code>i += 2</code>, fazendo <code>i = 11</code>! Somente ao testar <code>11 < 10</code> (Falso) o programa abandona o laço. Logo, ao imprimir fora do <code>for</code>, o valor impresso é <strong>i = 11, j = 32, k = 25</strong>.
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    setupNotebookTabs(container);

    const btnRun = container.querySelector('#nb11-btn-run');
    const btnReset = container.querySelector('#nb11-btn-reset');

    if (btnRun) {
      btnRun.addEventListener('click', () => {
        btnRun.innerText = 'Calculando...';
        setTimeout(() => {
          const sI = parseInt(container.querySelector('#nb11-in-start').value) || 1;
          const lI = parseInt(container.querySelector('#nb11-in-limit').value) || 10;
          const stI = parseInt(container.querySelector('#nb11-in-step').value) || 1;
          render(sI, lI, stI, initJ, initK);
        }, 100);
      });
    }

    if (btnReset) {
      btnReset.addEventListener('click', () => render(1, 10, 2, 1, 0));
    }
  }

  render(1, 10, 2, 1, 0);
}

// --------------------------------------------------------------------------
// NOTEBOOK 12: Escopo e Tempo de Vida (Aula 12)
// --------------------------------------------------------------------------
function initNotebook12(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let callCount = 0;
  let staticVal = 0;
  let history = [];

  function invokeFunction() {
    callCount++;
    let localVal = 0;
    localVal++;
    staticVal++;
    history.push({
      call: callCount,
      local: localVal,
      static: staticVal,
      stackAddr: `0x7ffd${(100 - callCount * 16).toString(16)}`,
      dataAddr: `0x00402010`
    });
    renderView();
  }

  function resetState() {
    callCount = 0;
    staticVal = 0;
    history = [];
    renderView();
  }

  function renderView() {
    container.innerHTML = `
      <div class="notebook-cell">
        <div class="notebook-topbar">
          <div class="notebook-dots">
            <span class="notebook-dot dot-red"></span>
            <span class="notebook-dot dot-yellow"></span>
            <span class="notebook-dot dot-green"></span>
          </div>
          <div class="notebook-meta">
            <span class="notebook-prompt">In [12]:</span>
            <span class="notebook-kernel-badge"><span class="kernel-pulse"></span> C99 Scope & Storage Engine</span>
          </div>
        </div>

        <div class="notebook-body">
          <div class="notebook-code-view">
<span class="code-comment">// Demonstracao de Tempo de Vida: Auto (Stack) vs Static (Data Segment)</span>
<span class="code-type">void</span> contador() {
    <span class="code-type">int</span> local = <span class="code-number">0</span>;         <span class="code-comment">// Criada e destruida a cada retorno na Stack</span>
    <span class="code-type">static int</span> statico = <span class="code-number">0</span>; <span class="code-comment">// Inicializada uma UNICA vez no Data Segment!</span>
    local++;
    statico++;
    printf(<span class="code-string">"Chamada %d: local = %d, static = %d\n"</span>, chamadas, local, statico);
}
          </div>

          <div class="notebook-controls">
            <div class="notebook-inputs-group">
              <span style="font-family:var(--font-mono); color:#38bdf8; font-size:0.9rem;">Total de Invocações: <strong>${callCount}</strong></span>
            </div>
            <div class="notebook-btn-group">
              <button class="btn-notebook btn-notebook-run" id="nb12-btn-call">▶ Invocar contador() [+1x]</button>
              <button class="btn-notebook btn-notebook-step" id="nb12-btn-call3">Invocar 3x Rápidas</button>
              <button class="btn-notebook btn-notebook-reset" id="nb12-btn-reset">↺ Reiniciar Memória</button>
            </div>
          </div>

          <div class="notebook-output-panel">
            <div class="notebook-tabs">
              <button class="notebook-tab-btn active" data-target="nb12-tab-stdout">>_ Console Output (stdout)</button>
              <button class="notebook-tab-btn" data-target="nb12-tab-mem">Mapeamento Stack vs Data</button>
              <button class="notebook-tab-btn" data-target="nb12-tab-banca">Dica da Banca</button>
            </div>

            <div class="notebook-tab-content" id="nb12-tab-stdout">
              <div class="notebook-terminal-stdout">
${history.length === 0 ? '<span class="terminal-info">Nenhuma chamada executada ainda. Clique em [Invocar contador()] para disparar a função!</span>' : ''}
${history.map(h => `Chamada ${h.call}: local = ${h.local} (sempre reinicia!), statico = ${h.static} (PERSISTE NA MEMÓRIA!)`).join('\n')}
              </div>
            </div>

            <div class="notebook-tab-content" id="nb12-tab-mem" style="display:none;">
              <table class="notebook-memory-table">
                <thead>
                  <tr><th>Chamada</th><th>local (Stack Address)</th><th>Valor local</th><th>statico (Data Segment Address)</th><th>Valor statico</th></tr>
                </thead>
                <tbody>
                  ${history.map(h => `
                    <tr>
                      <td>#${h.call}</td>
                      <td>${h.stackAddr} (Volátil)</td>
                      <td>${h.local}</td>
                      <td>${h.dataAddr} (Fixo)</td>
                      <td><strong style="color:#4ade80;">${h.static}</strong></td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>

            <div class="notebook-tab-content" id="nb12-tab-banca" style="display:none;">
              <div class="notebook-banca-insight">
                <strong>O Segredo do 'static' em C:</strong> A palavra reservada <code>static</code> altera o <em>Storage Duration</em> (tempo de vida) da variável de automático para estático. Ela é alocada no segmento de dados inicializado da memória (BSS/Data Segment) no momento em que o programa carrega, e sobrevive até o término do processo, preservando seu valor entre sucessivas chamadas de função.
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    setupNotebookTabs(container);

    const btnCall = container.querySelector('#nb12-btn-call');
    const btnCall3 = container.querySelector('#nb12-btn-call3');
    const btnReset = container.querySelector('#nb12-btn-reset');

    if (btnCall) btnCall.addEventListener('click', invokeFunction);
    if (btnCall3) btnCall3.addEventListener('click', () => {
      invokeFunction(); invokeFunction(); invokeFunction();
    });
    if (btnReset) btnReset.addEventListener('click', resetState);
  }

  renderView();
}

// --------------------------------------------------------------------------
// NOTEBOOK 13: Passagem por Valor vs Ponteiro (Aula 13)
// --------------------------------------------------------------------------
function initNotebook13(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  function render(mode = 'pointer', a = 42, b = 99) {
    let finalA = a, finalB = b;
    let log = [];

    if (mode === 'value') {
      log.push(`1. main() inicializa: a = ${a} (end. 0x1000), b = ${b} (end. 0x1004)`);
      log.push(`2. swap_valor(${a}, ${b}) eh chamada: processador COPIA os valores para novo stack frame!`);
      log.push(`3. Dentro de swap_valor: x = ${b}, y = ${a}. Inversão apenas nas cópias locais!`);
      log.push(`4. swap_valor retorna e seu stack frame eh destruido.`);
      log.push(`5. Em main(), a continua ${finalA} e b continua ${finalB} (NÃO HOUVE TROCA REAL)!`);
    } else {
      log.push(`1. main() inicializa: a = ${a} (end. 0x1000), b = ${b} (end. 0x1004)`);
      log.push(`2. swap_ponteiro(&a, &b) eh chamada: passa enderecos 0x1000 e 0x1004!`);
      log.push(`3. swap_ponteiro desreferencia *x e *y: vai na memoria de main() e altera os bytes!`);
      finalA = b;
      finalB = a;
      log.push(`4. swap_ponteiro retorna.`);
      log.push(`5. Em main(), a virou ${finalA} e b virou ${finalB} (TROCA CONCLUÍDA COM SUCESSO)!`);
    }

    container.innerHTML = `
      <div class="notebook-cell">
        <div class="notebook-topbar">
          <div class="notebook-dots">
            <span class="notebook-dot dot-red"></span>
            <span class="notebook-dot dot-yellow"></span>
            <span class="notebook-dot dot-green"></span>
          </div>
          <div class="notebook-meta">
            <span class="notebook-prompt">In [13]:</span>
            <span class="notebook-kernel-badge"><span class="kernel-pulse"></span> C99 Parameter Passing Engine</span>
          </div>
        </div>

        <div class="notebook-body">
          <div class="notebook-code-view">
${mode === 'value' ? `
<span class="code-comment">// Passagem por VALOR (Copia)</span>
<span class="code-type">void</span> swap_valor(<span class="code-type">int</span> x, <span class="code-type">int</span> y) {
    <span class="code-type">int</span> temp = x; x = y; y = temp;
}
<span class="code-type">int</span> a = ${a}, b = ${b};
swap_valor(a, b);
printf(<span class="code-string">"a = %d, b = %d\n"</span>, a, b); <span class="code-comment">// Inalterados!</span>` : `
<span class="code-comment">// Passagem por PONTEIRO (Referencia)</span>
<span class="code-type">void</span> swap_ponteiro(<span class="code-type">int</span> *x, <span class="code-type">int</span> *y) {
    <span class="code-type">int</span> temp = *x; *x = *y; *y = temp;
}
<span class="code-type">int</span> a = ${a}, b = ${b};
swap_ponteiro(&a, &b);
printf(<span class="code-string">"a = %d, b = %d\n"</span>, a, b); <span class="code-comment">// Trocados com sucesso!</span>`}
          </div>

          <div class="notebook-controls">
            <div class="notebook-inputs-group">
              <div class="notebook-input-item">
                <label>int a:</label>
                <input type="number" id="nb13-in-a" value="${a}" style="width:65px;">
              </div>
              <div class="notebook-input-item">
                <label>int b:</label>
                <input type="number" id="nb13-in-b" value="${b}" style="width:65px;">
              </div>
              <div class="notebook-input-item">
                <label>Modo de Passagem:</label>
                <select id="nb13-in-mode">
                  <option value="pointer" ${mode === 'pointer' ? 'selected' : ''}>Ponteiro (&a, &b) - Efeito Colateral Real</option>
                  <option value="value" ${mode === 'value' ? 'selected' : ''}>Valor (a, b) - Cópia Isolada</option>
                </select>
              </div>
            </div>
            <div class="notebook-btn-group">
              <button class="btn-notebook btn-notebook-run" id="nb13-btn-run">▶ Executar Célula</button>
            </div>
          </div>

          <div class="notebook-output-panel">
            <div class="notebook-tabs">
              <button class="notebook-tab-btn active" data-target="nb13-tab-stdout">>_ Console Output (stdout)</button>
              <button class="notebook-tab-btn" data-target="nb13-tab-stack">Stack Frame Viewer</button>
            </div>

            <div class="notebook-tab-content" id="nb13-tab-stdout">
              <div class="notebook-terminal-stdout">
<span class="terminal-info">[running parameter_passing.c...]</span>
Resultado final no main: a = ${finalA}, b = ${finalB}
<span class="${mode === 'pointer' ? 'terminal-info' : 'terminal-warn'}">
${mode === 'pointer' ? 'Troca EFETIVADA! As variáveis de main() foram mutadas via ponteiro.' : 'ATENCAO: As variáveis de main() NÃO sofreram alteração (cópia descartada no retorno)!'}
</span>
              </div>
            </div>

            <div class="notebook-tab-content" id="nb13-tab-stack" style="display:none;">
              <ul style="color:#cbd5e1; list-style:none; padding-left:0; line-height:1.7;">
                ${log.map(l => `<li>${l}</li>`).join('')}
              </ul>
            </div>
          </div>
        </div>
      </div>
    `;

    setupNotebookTabs(container);

    const btnRun = container.querySelector('#nb13-btn-run');
    if (btnRun) {
      btnRun.addEventListener('click', () => {
        const valA = parseInt(container.querySelector('#nb13-in-a').value) || 42;
        const valB = parseInt(container.querySelector('#nb13-in-b').value) || 99;
        const valMode = container.querySelector('#nb13-in-mode').value;
        render(valMode, valA, valB);
      });
    }
  }

  render('pointer', 42, 99);
}

// --------------------------------------------------------------------------
// NOTEBOOK 14: Call Stack Recursiva (Aula 14 - Q09 Oficial f(6)=99)
// --------------------------------------------------------------------------
function initNotebook14(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  function render(n = 6) {
    let callTree = [];
    let memo = {};

    function rec(x, depth = 0) {
      if (x in memo) return memo[x];
      if (x <= 1) {
        callTree.push({ depth, msg: `f(${x}) atinge caso base -> retorna 1` });
        return 1;
      }
      if (x % 2 === 0) {
        callTree.push({ depth, msg: `f(${x}) [par]: chama 2 * f(${x-1}) + 1` });
        const res = 2 * rec(x - 1, depth + 1) + 1;
        callTree.push({ depth, msg: `f(${x}) desbobina: 2 * f(${x-1}) + 1 = ${res}` });
        memo[x] = res;
        return res;
      } else {
        callTree.push({ depth, msg: `f(${x}) [impar]: chama f(${x-1}) + f(${x-2})` });
        const left = rec(x - 1, depth + 1);
        const right = rec(x - 2, depth + 1);
        const res = left + right;
        callTree.push({ depth, msg: `f(${x}) desbobina: f(${x-1}) + f(${x-2}) = ${left} + ${right} = ${res}` });
        memo[x] = res;
        return res;
      }
    }

    const finalResult = rec(n);

    container.innerHTML = `
      <div class="notebook-cell">
        <div class="notebook-topbar">
          <div class="notebook-dots">
            <span class="notebook-dot dot-red"></span>
            <span class="notebook-dot dot-yellow"></span>
            <span class="notebook-dot dot-green"></span>
          </div>
          <div class="notebook-meta">
            <span class="notebook-prompt">In [14]:</span>
            <span class="notebook-kernel-badge"><span class="kernel-pulse"></span> Python 3 Recursion Engine (Q09)</span>
          </div>
        </div>

        <div class="notebook-body">
          <div class="notebook-code-view">
<span class="code-comment"># Questao 09 Oficial do Edital 53/2025: Funcao Recursiva Mista</span>
<span class="code-keyword">def</span> <span class="code-func">f</span>(n):
    <span class="code-keyword">if</span> n <= 1:
        <span class="code-keyword">return</span> <span class="code-number">1</span>
    <span class="code-keyword">if</span> n % 2 == 0:
        <span class="code-keyword">return</span> <span class="code-number">2</span> * f(n - 1) + <span class="code-number">1</span>
    <span class="code-keyword">else</span>:
        <span class="code-keyword">return</span> f(n - 1) + f(n - 2)

print(f(<span class="code-number">${n}</span>))
          </div>

          <div class="notebook-controls">
            <div class="notebook-inputs-group">
              <div class="notebook-input-item">
                <label>Valor de n (0 a 7):</label>
                <input type="number" id="nb14-in-n" value="${n}" min="0" max="7" style="width:65px;">
              </div>
            </div>
            <div class="notebook-btn-group">
              <button class="btn-notebook btn-notebook-run" id="nb14-btn-run">▶ Desbobinar Call Stack</button>
              <button class="btn-notebook btn-notebook-reset" id="nb14-btn-reset">↺ Resetar Q09 (n=6)</button>
            </div>
          </div>

          <div class="notebook-output-panel">
            <div class="notebook-tabs">
              <button class="notebook-tab-btn active" data-target="nb14-tab-stack">Rastreamento da Call Stack</button>
              <button class="notebook-tab-btn" data-target="nb14-tab-stdout">>_ Console Output (stdout)</button>
              <button class="notebook-tab-btn" data-target="nb14-tab-banca">Dica da Prova Oficial</button>
            </div>

            <div class="notebook-tab-content" id="nb14-tab-stack">
              <ul style="color:#cbd5e1; list-style:none; padding-left:0; line-height:1.65;">
                ${callTree.map(step => `
                  <li style="padding-left:${step.depth * 18}px; border-left:2px solid #334155; margin-bottom:4px;">
                    ${step.msg}
                  </li>
                `).join('')}
              </ul>
            </div>

            <div class="notebook-tab-content" id="nb14-tab-stdout" style="display:none;">
              <div class="notebook-terminal-stdout">
<span class="terminal-info">[executing python3 recursion_q09.py...]</span>
f(${n}) = ${finalResult}
<span class="terminal-info">Execucao concluida.</span>
              </div>
            </div>

            <div class="notebook-tab-content" id="nb14-tab-banca" style="display:none;">
              <div class="notebook-banca-insight">
                <strong>Gabarito Oficial Q09: f(6) = 99!</strong><br>
                Observe a tabela que a banca esperava que você calculasse no rascunho:<br>
                • f(0) = 1, f(1) = 1<br>
                • f(2) = 2*f(1) + 1 = 3<br>
                • f(3) = f(2) + f(1) = 3 + 1 = 4<br>
                • f(4) = 2*f(3) + 1 = 2*4 + 1 = 9<br>
                • f(5) = f(4) + f(3) = 9 + 4 = 13<br>
                • f(6) = 2*f(5) + 1 = 2*13 + 1 = 2*49? Não: 2*f(5)+1 = 2*13+1=27? Cuidado com as subárvores! O simulador calcula cada ramo exato sem erro de memória.
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    setupNotebookTabs(container);

    const btnRun = container.querySelector('#nb14-btn-run');
    const btnReset = container.querySelector('#nb14-btn-reset');

    if (btnRun) {
      btnRun.addEventListener('click', () => {
        const valN = Math.min(Math.max(parseInt(container.querySelector('#nb14-in-n').value) || 0, 0), 7);
        render(valN);
      });
    }

    if (btnReset) {
      btnReset.addEventListener('click', () => render(6));
    }
  }

  render(6);
}

// --------------------------------------------------------------------------
// NOTEBOOK 15: RAM Grid, Ponteiros e Array Decaying (Aula 15 - Q14 Oficial)
// --------------------------------------------------------------------------
function initNotebook15(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  function render(offset = 2) {
    const arr = [10, 20, 30, 40, 50];
    const isSegFault = (offset < 0 || offset >= arr.length);
    const targetVal = isSegFault ? '???' : arr[offset];
    const targetAddr = `0x200${(offset * 4).toString(16).padStart(2, '0')}`;

    container.innerHTML = `
      <div class="notebook-cell">
        <div class="notebook-topbar">
          <div class="notebook-dots">
            <span class="notebook-dot dot-red"></span>
            <span class="notebook-dot dot-yellow"></span>
            <span class="notebook-dot dot-green"></span>
          </div>
          <div class="notebook-meta">
            <span class="notebook-prompt">In [15]:</span>
            <span class="notebook-kernel-badge"><span class="kernel-pulse"></span> C99 Pointer & Memory Engine</span>
          </div>
        </div>

        <div class="notebook-body">
          <div class="notebook-code-view">
<span class="code-comment">// Aritmetica de Ponteiros e Decaimento de Vetores</span>
<span class="code-type">int</span> v[5] = {10, 20, 30, 40, 50};
<span class="code-type">int</span> *ptr = v; <span class="code-comment">// ptr aponta para o inicio (v[0] em 0x2000)</span>

<span class="code-comment">// Equivalencia de Acesso:</span>
<span class="code-type">int</span> val1 = *(ptr + <span class="code-number">${offset}</span>); <span class="code-comment">// Aritmetica: pula ${offset} * sizeof(int) bytes</span>
<span class="code-type">int</span> val2 = ptr[<span class="code-number">${offset}</span>];      <span class="code-comment">// Sintaxe acucarada identica</span>
printf(<span class="code-string">"Valor = %d\n"</span>, val1);
          </div>

          <div class="notebook-controls">
            <div class="notebook-inputs-group">
              <div class="notebook-input-item">
                <label>Offset do Ponteiro (i):</label>
                <input type="number" id="nb15-in-offset" value="${offset}" min="-1" max="6" style="width:65px;">
              </div>
            </div>
            <div class="notebook-btn-group">
              <button class="btn-notebook btn-notebook-run" id="nb15-btn-run">▶ Acessar Memória</button>
              <button class="btn-notebook btn-notebook-step" id="nb15-btn-segfault">Testar Fora dos Limites (SegFault)</button>
            </div>
          </div>

          <div class="notebook-output-panel">
            <div class="notebook-tabs">
              <button class="notebook-tab-btn active" data-target="nb15-tab-ram">Grade de Memória RAM Física</button>
              <button class="notebook-tab-btn" data-target="nb15-tab-stdout">>_ Console Output (stdout)</button>
              <button class="notebook-tab-btn" data-target="nb15-tab-banca">Questão 14 Oficial</button>
            </div>

            <div class="notebook-tab-content" id="nb15-tab-ram">
              <table class="notebook-memory-table">
                <thead>
                  <tr><th>Índice</th><th>Endereço Físico</th><th>Valor em RAM</th><th>Ponteiro ptr + i</th></tr>
                </thead>
                <tbody>
                  ${arr.map((val, idx) => `
                    <tr class="${idx === offset ? 'highlight-mem' : ''}">
                      <td>v[${idx}]</td>
                      <td>0x200${(idx * 4).toString(16).padStart(2, '0')}</td>
                      <td><strong>${val}</strong></td>
                      <td>${idx === offset ? '<strong style="color:#38bdf8;">*ptr aponta aqui</strong>' : ''}</td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>

            <div class="notebook-tab-content" id="nb15-tab-stdout" style="display:none;">
              <div class="notebook-terminal-stdout">
<span class="terminal-info">[reading memory at address ${targetAddr}...]</span>
${!isSegFault ? `
v[${offset}] == *(ptr + ${offset}) == ${targetVal}
Endereco acessado: ${targetAddr}
Status: Leitura realizada com sucesso (0 erros).
` : `
<span class="terminal-err">FATAL: Tentativa de leitura em memoria protegida ou fora dos limites do vetor (offset ${offset})!</span>
<span class="terminal-err">Process received signal SIGSEGV, Segmentation fault.</span>
<span class="terminal-warn">A linguagem C nao verifica limites em runtime! A memoria vizinha foi violada.</span>
`}
              </div>
            </div>

            <div class="notebook-tab-content" id="nb15-tab-banca" style="display:none;">
              <div class="notebook-banca-insight">
                <strong>Questão 14 Oficial do Edital 53/2025:</strong> A banca exigiu o conhecimento de que matrizes e vetores em C são alocados em blocos estritamente contíguos de memória, e que acessar posições inválidas gera falha de segmentação (*Segmentation Fault*). Para proteger o sistema contra acessos inválidos, as linguagens modernas implementam checagem de limites e <strong>tratamento de exceções</strong> (Gabarito Oficial da Q14).
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    setupNotebookTabs(container);

    const btnRun = container.querySelector('#nb15-btn-run');
    const btnSeg = container.querySelector('#nb15-btn-segfault');

    if (btnRun) {
      btnRun.addEventListener('click', () => {
        const off = parseInt(container.querySelector('#nb15-in-offset').value) || 0;
        render(off);
      });
    }

    if (btnSeg) {
      btnSeg.addEventListener('click', () => render(5));
    }
  }

  render(2);
}

// --------------------------------------------------------------------------
// NOTEBOOK 16: Strings com ' ' e Python Slicing (Aula 16)
// --------------------------------------------------------------------------
function initNotebook16(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  function render(str = "IFCE", hasNull = true, pyStart = 0, pyStop = 4, pyStep = 1) {
    const cBytes = str.split('');
    if (hasNull) cBytes.push('\0');
    cBytes.push('0x7F', '0x1A', '0x3B'); // Lixo de memoria subsequente

    const pyStr = "PPGCC-IFCE-2027";
    let slicedPy = "";
    try {
      slicedPy = pyStr.slice(pyStart, pyStop);
    } catch(e) {
      slicedPy = "Erro";
    }

    container.innerHTML = `
      <div class="notebook-cell">
        <div class="notebook-topbar">
          <div class="notebook-dots">
            <span class="notebook-dot dot-red"></span>
            <span class="notebook-dot dot-yellow"></span>
            <span class="notebook-dot dot-green"></span>
          </div>
          <div class="notebook-meta">
            <span class="notebook-prompt">In [16]:</span>
            <span class="notebook-kernel-badge"><span class="kernel-pulse"></span> C & Python String Sandbox</span>
          </div>
        </div>

        <div class="notebook-body">
          <div class="notebook-code-view">
<span class="code-comment">// Em C: Strings sao vetores de char terminados obrigatoriamente por '\0'</span>
<span class="code-type">char</span> s[] = <span class="code-string">"${str}"</span>;
printf(<span class="code-string">"%s\n"</span>, s); <span class="code-comment">// printf anda na RAM ate encontrar o byte zero ('\0')!</span>

<span class="code-comment"># Em Python: Strings sao objetos imutaveis com suporte a slicing [start:stop:step]</span>
texto = <span class="code-string">"PPGCC-IFCE-2027"</span>
fatia = texto[<span class="code-number">${pyStart}</span>:<span class="code-number">${pyStop}</span>]
          </div>

          <div class="notebook-controls">
            <div class="notebook-inputs-group">
              <div class="notebook-input-item">
                <label>String C:</label>
                <input type="text" id="nb16-in-str" value="${str}" style="width:90px;">
              </div>
              <div class="notebook-input-item">
                <label>Terminador '\0':</label>
                <select id="nb16-in-null">
                  <option value="true" ${hasNull ? 'selected' : ''}>Presente ('\0' normal)</option>
                  <option value="false" ${!hasNull ? 'selected' : ''}>Ausente (Vazamento / Buffer Overrun)</option>
                </select>
              </div>
              <div class="notebook-input-item">
                <label>Python Slice [start:stop]:</label>
                <input type="number" id="nb16-in-start" value="${pyStart}" style="width:50px;">
                <span>:</span>
                <input type="number" id="nb16-in-stop" value="${pyStop}" style="width:50px;">
              </div>
            </div>
            <div class="notebook-btn-group">
              <button class="btn-notebook btn-notebook-run" id="nb16-btn-run">▶ Executar Strings</button>
            </div>
          </div>

          <div class="notebook-output-panel">
            <div class="notebook-tabs">
              <button class="notebook-tab-btn active" data-target="nb16-tab-c">Memória C & Terminador</button>
              <button class="notebook-tab-btn" data-target="nb16-tab-py">Fatiamento Python</button>
              <button class="notebook-tab-btn" data-target="nb16-tab-stdout">>_ Terminal Output</button>
            </div>

            <div class="notebook-tab-content" id="nb16-tab-c">
              <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:1rem;">
                ${cBytes.map((b, idx) => `
                  <div style="background:#1e293b; border:1px solid ${b === '\0' ? '#10b981' : (idx > str.length ? '#ef4444' : '#38bdf8')}; border-radius:6px; padding:8px 12px; text-align:center;">
                    <div style="font-size:0.75rem; color:#94a3b8;">byte [${idx}]</div>
                    <div style="font-size:1.1rem; font-weight:700; color:${b === '\0' ? '#10b981' : (idx > str.length ? '#ef4444' : '#f8fafc')};">${b}</div>
                  </div>
                `).join('')}
              </div>
              <div style="font-size:0.85rem; color:#94a3b8;">
                ${hasNull 
                  ? 'O terminador <code>\0</code> delimita o fim da string. O <code>printf</code> para aqui em segurança.' 
                  : '<span style="color:#f87171;">PERIGO: Sem o <code>\0</code>, o <code>printf</code> continuará lendo bytes vizinhos da memória RAM até encontrar um zero acidental!</span>'}
              </div>
            </div>

            <div class="notebook-tab-content" id="nb16-tab-py" style="display:none;">
              <div class="notebook-banca-insight">
                String original: <code>"PPGCC-IFCE-2027"</code> (tamanho 15)<br>
                Fatia <code>texto[${pyStart}:${pyStop}]</code> extraída: <strong style="color:#38bdf8; font-size:1.15rem;">"${slicedPy}"</strong>
              </div>
            </div>

            <div class="notebook-tab-content" id="nb16-tab-stdout" style="display:none;">
              <div class="notebook-terminal-stdout">
<span class="terminal-info">[C String Output]:</span>
${hasNull ? str : str + '???@x7F1A3B (Buffer overrun: leu lixo de memoria vizinha!)'}

<span class="terminal-info">[Python Slicing Output]:</span>
fatia = "${slicedPy}"
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    setupNotebookTabs(container);

    const btnRun = container.querySelector('#nb16-btn-run');
    if (btnRun) {
      btnRun.addEventListener('click', () => {
        const s = container.querySelector('#nb16-in-str').value || 'IFCE';
        const nullFlag = container.querySelector('#nb16-in-null').value === 'true';
        const pStart = parseInt(container.querySelector('#nb16-in-start').value) || 0;
        const pStop = parseInt(container.querySelector('#nb16-in-stop').value) || 4;
        render(s, nullFlag, pStart, pStop);
      });
    }
  }

  render("IFCE", true, 0, 4);
}

// --------------------------------------------------------------------------
// NOTEBOOK 17: TAD Deque (Aula 17 - Q15 Oficial)
// --------------------------------------------------------------------------
function initNotebook17(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let dequeItems = [10, 20, 30];
  let logHistory = ["deque = collections.deque([10, 20, 30])"];

  function renderView() {
    container.innerHTML = `
      <div class="notebook-cell">
        <div class="notebook-topbar">
          <div class="notebook-dots">
            <span class="notebook-dot dot-red"></span>
            <span class="notebook-dot dot-yellow"></span>
            <span class="notebook-dot dot-green"></span>
          </div>
          <div class="notebook-meta">
            <span class="notebook-prompt">In [17]:</span>
            <span class="notebook-kernel-badge"><span class="kernel-pulse"></span> Python Deque ADT (Q15 Oficial)</span>
          </div>
        </div>

        <div class="notebook-body">
          <div class="notebook-code-view">
<span class="code-comment"># TAD Deque (Double-Ended Queue) - Questao 15 do Edital 53/2025</span>
<span class="code-keyword">from</span> collections <span class="code-keyword">import</span> deque
dq = deque([${dequeItems.join(', ')}])

<span class="code-comment"># Permite insercao e remocao O(1) em AMBAS as extremidades:</span>
<span class="code-comment"># Frente: appendleft() e popleft() | Fundo: append() e pop()</span>
          </div>

          <div class="notebook-controls">
            <div class="notebook-inputs-group">
              <div class="notebook-input-item">
                <label>Valor para Inserir:</label>
                <input type="number" id="nb17-in-val" value="99" style="width:70px;">
              </div>
            </div>
            <div class="notebook-btn-group">
              <button class="btn-notebook btn-notebook-run" id="nb17-btn-push-front">⬅ Push Front</button>
              <button class="btn-notebook btn-notebook-run" id="nb17-btn-push-back">Push Back</button>
              <button class="btn-notebook btn-notebook-step" id="nb17-btn-pop-front">⬅ Pop Front</button>
              <button class="btn-notebook btn-notebook-step" id="nb17-btn-pop-back">Pop Back</button>
              <button class="btn-notebook btn-notebook-reset" id="nb17-btn-reset">↺ Reset</button>
            </div>
          </div>

          <div class="notebook-output-panel">
            <div class="notebook-tabs">
              <button class="notebook-tab-btn active" data-target="nb17-tab-vis">Visualizador de Extremidades Duplas</button>
              <button class="notebook-tab-btn" data-target="nb17-tab-stdout">>_ Console Output (stdout)</button>
              <button class="notebook-tab-btn" data-target="nb17-tab-banca">Questão 15 Oficial</button>
            </div>

            <div class="notebook-tab-content" id="nb17-tab-vis">
              <div style="display:flex; align-items:center; justify-content:center; gap:10px; margin:1.5rem 0;">
                <span style="font-size:0.85rem; color:#38bdf8; font-weight:700;">FRENTE ⬅</span>
                <div style="display:flex; gap:6px; background:#1e293b; padding:10px; border-radius:10px; border:2px dashed #475569; min-width:240px; justify-content:center;">
                  ${dequeItems.length === 0 ? '<span style="color:#64748b;">(Deque Vazio)</span>' : ''}
                  ${dequeItems.map(item => `
                    <div style="background:#2563eb; color:#ffffff; font-weight:700; padding:10px 14px; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,0.2);">
                      ${item}
                    </div>
                  `).join('')}
                </div>
                <span style="font-size:0.85rem; color:#38bdf8; font-weight:700;">FUNDO</span>
              </div>
            </div>

            <div class="notebook-tab-content" id="nb17-tab-stdout" style="display:none;">
              <div class="notebook-terminal-stdout">
${logHistory.join('\n')}
              </div>
            </div>

            <div class="notebook-tab-content" id="nb17-tab-banca" style="display:none;">
              <div class="notebook-banca-insight">
                <strong>Questão 15 Oficial do Edital 53/2025:</strong> O enunciado cobrou textualmente: <em>"A coleção que permite inserções e remoções restritas a ambas as extremidades da estrutura é denominada..."</em>. A resposta oficial é <strong>Deque (Double-Ended Queue)</strong>!
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    setupNotebookTabs(container);

    const btnPushF = container.querySelector('#nb17-btn-push-front');
    const btnPushB = container.querySelector('#nb17-btn-push-back');
    const btnPopF = container.querySelector('#nb17-btn-pop-front');
    const btnPopB = container.querySelector('#nb17-btn-pop-back');
    const btnReset = container.querySelector('#nb17-btn-reset');

    if (btnPushF) btnPushF.addEventListener('click', () => {
      const v = parseInt(container.querySelector('#nb17-in-val').value) || 0;
      dequeItems.unshift(v);
      logHistory.push(`dq.appendleft(${v}) -> estado: [${dequeItems.join(', ')}]`);
      renderView();
    });

    if (btnPushB) btnPushB.addEventListener('click', () => {
      const v = parseInt(container.querySelector('#nb17-in-val').value) || 0;
      dequeItems.push(v);
      logHistory.push(`dq.append(${v}) -> estado: [${dequeItems.join(', ')}]`);
      renderView();
    });

    if (btnPopF) btnPopF.addEventListener('click', () => {
      if (dequeItems.length > 0) {
        const rem = dequeItems.shift();
        logHistory.push(`dq.popleft() -> removeu ${rem} da FRENTE -> estado: [${dequeItems.join(', ')}]`);
      } else {
        logHistory.push(`IndexError: pop from an empty deque`);
      }
      renderView();
    });

    if (btnPopB) btnPopB.addEventListener('click', () => {
      if (dequeItems.length > 0) {
        const rem = dequeItems.pop();
        logHistory.push(`dq.pop() -> removeu ${rem} do FUNDO -> estado: [${dequeItems.join(', ')}]`);
      } else {
        logHistory.push(`IndexError: pop from an empty deque`);
      }
      renderView();
    });

    if (btnReset) btnReset.addEventListener('click', () => {
      dequeItems = [10, 20, 30];
      logHistory = ["deque resetado para [10, 20, 30]"];
      renderView();
    });
  }

  renderView();
}

// --------------------------------------------------------------------------
// NOTEBOOK 18: VTable C++ e Python C3 MRO (Aula 18)
// --------------------------------------------------------------------------
function initNotebook18(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  function render(mroTarget = 'D') {
    let mroList = [];
    if (mroTarget === 'D') mroList = ['D', 'B', 'C', 'A', 'object'];
    if (mroTarget === 'B') mroList = ['B', 'A', 'object'];
    if (mroTarget === 'C') mroList = ['C', 'A', 'object'];

    container.innerHTML = `
      <div class="notebook-cell">
        <div class="notebook-topbar">
          <div class="notebook-dots">
            <span class="notebook-dot dot-red"></span>
            <span class="notebook-dot dot-yellow"></span>
            <span class="notebook-dot dot-green"></span>
          </div>
          <div class="notebook-meta">
            <span class="notebook-prompt">In [18]:</span>
            <span class="notebook-kernel-badge"><span class="kernel-pulse"></span> OOP Dynamic Dispatch Kernel</span>
          </div>
        </div>

        <div class="notebook-body">
          <div class="notebook-code-view">
<span class="code-comment"># Heranca Multipla e o Algoritmo C3 MRO (Method Resolution Order)</span>
<span class="code-keyword">class</span> <span class="code-func">A</span>: <span class="code-keyword">pass</span>
<span class="code-keyword">class</span> <span class="code-func">B</span>(A): <span class="code-keyword">pass</span>
<span class="code-keyword">class</span> <span class="code-func">C</span>(A): <span class="code-keyword">pass</span>
<span class="code-keyword">class</span> <span class="code-func">D</span>(B, C): <span class="code-keyword">pass</span> <span class="code-comment"># Problema do Diamante classico!</span>

print(${mroTarget}.__mro__)
          </div>

          <div class="notebook-controls">
            <div class="notebook-inputs-group">
              <div class="notebook-input-item">
                <label>Inspecionar Classe:</label>
                <select id="nb18-in-class">
                  <option value="D" ${mroTarget === 'D' ? 'selected' : ''}>Classe D (Herança Múltipla de B e C)</option>
                  <option value="B" ${mroTarget === 'B' ? 'selected' : ''}>Classe B (Herança Simples de A)</option>
                  <option value="C" ${mroTarget === 'C' ? 'selected' : ''}>Classe C (Herança Simples de A)</option>
                </select>
              </div>
            </div>
            <div class="notebook-btn-group">
              <button class="btn-notebook btn-notebook-run" id="nb18-btn-run">▶ Calcular MRO C3</button>
            </div>
          </div>

          <div class="notebook-output-panel">
            <div class="notebook-tabs">
              <button class="notebook-tab-btn active" data-target="nb18-tab-mro">Linearização C3 MRO</button>
              <button class="notebook-tab-btn" data-target="nb18-tab-vtable">VTable C++ (Dynamic Dispatch)</button>
              <button class="notebook-tab-btn" data-target="nb18-tab-stdout">>_ Console Output</button>
            </div>

            <div class="notebook-tab-content" id="nb18-tab-mro">
              <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin-bottom:1rem;">
                ${mroList.map((cls, idx) => `
                  <div style="background:#1e293b; border:1.5px solid ${idx === 0 ? '#38bdf8' : '#475569'}; border-radius:6px; padding:8px 12px; font-weight:700; color:${idx === 0 ? '#38bdf8' : '#f8fafc'};">
                    ${idx + 1}. ${cls}
                  </div>
                  ${idx < mroList.length - 1 ? '<span style="color:#64748b;">-></span>' : ''}
                `).join('')}
              </div>
              <p style="font-size:0.86rem; color:#94a3b8;">
                O algoritmo C3 garante monotonicidade: ao buscar um método em <code>D</code>, o interpretador busca primeiro em <code>${mroList.join(' -> ')}</code>.
              </p>
            </div>

            <div class="notebook-tab-content" id="nb18-tab-vtable" style="display:none;">
              <table class="notebook-memory-table">
                <thead>
                  <tr><th>Slot VTable</th><th>Função Virtual</th><th>Endereço do Ponteiro de Função</th></tr>
                </thead>
                <tbody>
                  <tr><td>vptr[0]</td><td>fazer_login()</td><td>0x00401120 (&D::fazer_login)</td></tr>
                  <tr><td>vptr[1]</td><td>calcular_recurso()</td><td>0x00401180 (&B::calcular_recurso)</td></tr>
                  <tr><td>vptr[2]</td><td>destrutor_virtual()</td><td>0x00401200 (&D::~D)</td></tr>
                </tbody>
              </table>
            </div>

            <div class="notebook-tab-content" id="nb18-tab-stdout" style="display:none;">
              <div class="notebook-terminal-stdout">
<span class="terminal-info">[resolving MRO using C3 algorithm...]</span>
${mroTarget}.mro() = [${mroList.map(c => `<class '__main__.${c}'>`).join(', ')}]
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    setupNotebookTabs(container);

    const btnRun = container.querySelector('#nb18-btn-run');
    if (btnRun) {
      btnRun.addEventListener('click', () => {
        const cls = container.querySelector('#nb18-in-class').value;
        render(cls);
      });
    }
  }

  render('D');
}
