"""
PPGCC IFCE Study Hub — Native SVG Diagrams for Discrete Mathematics & Order Theory
Design standard: Apple HIG + Emil Kowalski clean aesthetic
Rules:
- Zero emojis
- 100% vector SVG with viewBox for full responsiveness
- Palette aligned with assets/style.css:
  - Background card: #ffffff with #f8fafc subtle canvas
  - Node fill: #ffffff / #f1f5f9
  - Node border: #0071e3 (primary blue) / #475569 (slate) / #8b5cf6 (purple) / #10b981 (green)
  - Text: #0f172a (high contrast slate)
  - Edges: #64748b (slate 500) with 1.5px / 2px stroke
  - Typography: -apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, sans-serif
"""

def wrap_diagram(title: str, tag: str, svg_content: str, caption: str = "") -> str:
    caption_html = f'<p class="diagram-caption">{caption}</p>' if caption else ""
    return f"""<div class="visual-diagram-card">
  <div class="diagram-header">
    <span class="diagram-tag">{tag}</span>
    <h4 class="diagram-title">{title}</h4>
  </div>
  <div class="diagram-body">
    {svg_content.strip()}
  </div>
  {caption_html}
</div>"""

# ==============================================================================
# TOPICO 1: Produto Cartesiano e Junção Relacional
# ==============================================================================
def get_diagram_topico_1_cartesian_product() -> str:
    svg = """<svg viewBox="0 0 760 380" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0071e3"/>
    </marker>
    <marker id="arrow-slate" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#94a3b8"/>
    </marker>
    <filter id="card-shadow" x="-4%" y="-4%" width="108%" height="108%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.04"/>
    </filter>
  </defs>

  <!-- Container Box 1: Domínio A -->
  <g transform="translate(20, 30)">
    <rect width="150" height="320" rx="12" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.5"/>
    <text x="75" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">Domínio A (Usuários)</text>
    <rect x="20" y="65" width="110" height="44" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#card-shadow)"/>
    <text x="75" y="92" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="600" fill="#0f172a">u1 (Alice)</text>
    <rect x="20" y="145" width="110" height="44" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#card-shadow)"/>
    <text x="75" y="172" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="600" fill="#0f172a">u2 (Bob)</text>
  </g>

  <!-- Container Box 2: Domínio B -->
  <g transform="translate(195, 30)">
    <rect width="150" height="320" rx="12" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.5"/>
    <text x="75" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">Domínio B (Cargos)</text>
    <rect x="20" y="65" width="110" height="44" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#card-shadow)"/>
    <text x="75" y="92" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="600" fill="#0f172a">r1 (Admin)</text>
    <rect x="20" y="145" width="110" height="44" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#card-shadow)"/>
    <text x="75" y="172" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="600" fill="#0f172a">r2 (Dev)</text>
  </g>

  <!-- Edges from A, B to Product -->
  <path d="M 150 117 C 270 117, 280 97, 390 97" fill="none" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow-slate)"/>
  <path d="M 150 117 C 270 117, 280 162, 390 162" fill="none" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow-slate)"/>
  <path d="M 150 197 C 270 197, 280 227, 390 227" fill="none" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow-slate)"/>
  <path d="M 150 197 C 270 197, 280 292, 390 292" fill="none" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow-slate)"/>

  <!-- Container Box 3: Produto Cartesiano A x B -->
  <g transform="translate(395, 30)">
    <rect width="165" height="320" rx="12" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
    <text x="82" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#1e40af">A x B (CROSS JOIN)</text>
    
    <!-- Pair 1 -->
    <rect x="15" y="55" width="135" height="38" rx="8" fill="#ffffff" stroke="#93c5fd" stroke-width="1.5"/>
    <text x="82" y="79" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#1e3a8a">(u1, r1)</text>
    
    <!-- Pair 2 -->
    <rect x="15" y="120" width="135" height="38" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="82" y="144" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#64748b">(u1, r2)</text>
    
    <!-- Pair 3 -->
    <rect x="15" y="185" width="135" height="38" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="82" y="209" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#64748b">(u2, r1)</text>

    <!-- Pair 4 -->
    <rect x="15" y="250" width="135" height="38" rx="8" fill="#ffffff" stroke="#93c5fd" stroke-width="1.5"/>
    <text x="82" y="274" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#1e3a8a">(u2, r2)</text>
  </g>

  <!-- Filter Arrows to Relation R -->
  <path d="M 560 104 L 605 104" fill="none" stroke="#0071e3" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arrow-blue)"/>
  <text x="582" y="94" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="10" font-weight="700" fill="#0071e3">σ</text>

  <path d="M 560 299 L 605 234" fill="none" stroke="#0071e3" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arrow-blue)"/>
  <text x="582" y="258" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="10" font-weight="700" fill="#0071e3">σ</text>

  <!-- Container Box 4: Relação R (Subconjunto Selecionado) -->
  <g transform="translate(610, 30)">
    <rect width="130" height="320" rx="12" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
    <text x="65" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#166534">Relação R ⊆ A x B</text>
    
    <rect x="12" y="85" width="106" height="38" rx="8" fill="#ffffff" stroke="#86efac" stroke-width="1.5"/>
    <text x="65" y="109" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#15803d">(u1, r1)</text>

    <rect x="12" y="215" width="106" height="38" rx="8" fill="#ffffff" stroke="#86efac" stroke-width="1.5"/>
    <text x="65" y="239" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#15803d">(u2, r2)</text>

    <text x="65" y="295" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-style="italic" fill="#15803d">|R| = 2 pares</text>
  </g>
</svg>"""
    return wrap_diagram(
        "Mapeamento de Produto Cartesiano e Junção Relacional",
        "FIGURA 1.1 — ÁLGEBRA RELACIONAL",
        svg,
        "O produto cartesiano A × B gera todas as 4 combinações possíveis (CROSS JOIN). A relação binária de permissões R seleciona apenas o subconjunto onde o usuário possui papel ativo."
    )

# ==============================================================================
# TOPICO 2: Dígrafo de Relação Binária
# ==============================================================================
def get_diagram_topico_2_digraph() -> str:
    svg = """<svg viewBox="0 0 540 240" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-t2" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0071e3"/>
    </marker>
  </defs>

  <!-- Edges -->
  <!-- 1 -> 2 -->
  <line x1="80" y1="120" x2="200" y2="120" stroke="#0071e3" stroke-width="2" marker-end="url(#arrow-t2)"/>
  <!-- 2 -> 3 -->
  <path d="M 200 120 C 260 50, 340 50, 400 120" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arrow-t2)"/>
  <!-- 3 -> 4 -->
  <path d="M 400 120 C 400 180, 360 200, 300 200" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arrow-t2)"/>
  <!-- 4 -> 2 -->
  <path d="M 300 200 C 240 200, 200 180, 200 120" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arrow-t2)"/>

  <!-- Nodes -->
  <!-- Node 1 -->
  <circle cx="80" cy="120" r="22" fill="#ffffff" stroke="#0071e3" stroke-width="2.5"/>
  <text x="80" y="126" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" fill="#0f172a">1</text>

  <!-- Node 2 -->
  <circle cx="200" cy="120" r="22" fill="#ffffff" stroke="#0071e3" stroke-width="2.5"/>
  <text x="200" y="126" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" fill="#0f172a">2</text>

  <!-- Node 3 -->
  <circle cx="400" cy="120" r="22" fill="#ffffff" stroke="#0071e3" stroke-width="2.5"/>
  <text x="400" y="126" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" fill="#0f172a">3</text>

  <!-- Node 4 -->
  <circle cx="300" cy="200" r="22" fill="#ffffff" stroke="#0071e3" stroke-width="2.5"/>
  <text x="300" y="206" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" fill="#0f172a">4</text>

  <!-- Edge Labels -->
  <text x="140" y="112" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#64748b">(1, 2)</text>
  <text x="300" y="66" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#64748b">(2, 3)</text>
  <text x="375" y="185" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#64748b">(3, 4)</text>
  <text x="225" y="185" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#64748b">(4, 2)</text>
</svg>"""
    return wrap_diagram(
        "Dígrafo da Relação Binária R = {(1,2), (2,3), (3,4), (4,2)}",
        "FIGURA 2.1 — TOPOLOGIA DIRECIONADA",
        svg,
        "Vértice 1 possui apenas grau de saída (fonte). O ciclo direcionado 2 → 3 → 4 → 2 evidencia caminhos múltiplos e não-antissimetria."
    )

# ==============================================================================
# TOPICO 3: Fecho Transitivo de Warshall
# ==============================================================================
def get_diagram_topico_3_transitive_closure() -> str:
    svg = """<svg viewBox="0 0 620 280" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-solid" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0071e3"/>
    </marker>
    <marker id="arr-dash" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#8b5cf6"/>
    </marker>
  </defs>

  <!-- Solid Original Edges R -->
  <line x1="120" y1="140" x2="260" y2="80" stroke="#0071e3" stroke-width="2" marker-end="url(#arr-solid)"/>
  <line x1="260" y1="80" x2="400" y2="140" stroke="#0071e3" stroke-width="2" marker-end="url(#arr-solid)"/>
  <line x1="400" y1="140" x2="260" y2="200" stroke="#0071e3" stroke-width="2" marker-end="url(#arr-solid)"/>
  <line x1="260" y1="200" x2="120" y2="140" stroke="#0071e3" stroke-width="2" marker-end="url(#arr-solid)"/>
  <line x1="400" y1="140" x2="520" y2="140" stroke="#0071e3" stroke-width="2" marker-end="url(#arr-solid)"/>

  <!-- Dashed Transitive Inferred Edges t(R) -->
  <line x1="120" y1="140" x2="400" y2="140" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arr-dash)"/>
  <line x1="120" y1="140" x2="520" y2="140" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arr-dash)"/>
  <line x1="260" y1="80" x2="520" y2="140" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arr-dash)"/>

  <!-- Self-Loops (Ciclos) -->
  <path d="M 110 120 C 70 80, 70 200, 110 160" fill="none" stroke="#8b5cf6" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arr-dash)"/>
  <path d="M 270 60 C 310 20, 210 20, 250 60" fill="none" stroke="#8b5cf6" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arr-dash)"/>

  <!-- Nodes -->
  <g>
    <circle cx="120" cy="140" r="20" fill="#ffffff" stroke="#0071e3" stroke-width="2.5"/>
    <text x="120" y="146" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" fill="#0f172a">1</text>
  </g>
  <g>
    <circle cx="260" cy="80" r="20" fill="#ffffff" stroke="#0071e3" stroke-width="2.5"/>
    <text x="260" y="86" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" fill="#0f172a">2</text>
  </g>
  <g>
    <circle cx="400" cy="140" r="20" fill="#ffffff" stroke="#0071e3" stroke-width="2.5"/>
    <text x="400" y="146" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" fill="#0f172a">3</text>
  </g>
  <g>
    <circle cx="260" cy="200" r="20" fill="#ffffff" stroke="#0071e3" stroke-width="2.5"/>
    <text x="260" y="206" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" fill="#0f172a">4</text>
  </g>
  <g>
    <circle cx="520" cy="140" r="20" fill="#ffffff" stroke="#0071e3" stroke-width="2.5"/>
    <text x="520" y="146" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" fill="#0f172a">5</text>
  </g>

  <!-- Legend -->
  <g transform="translate(180, 245)">
    <line x1="0" y1="10" x2="30" y2="10" stroke="#0071e3" stroke-width="2"/>
    <text x="40" y="14" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#334155">Aresta Original R</text>

    <line x1="170" y1="10" x2="200" y2="10" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="210" y="14" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#8b5cf6">Aresta Transitiva t(R)</text>
  </g>
</svg>"""
    return wrap_diagram(
        "Fecho Transitivo t(R) via Algoritmo de Warshall",
        "FIGURA 3.1 — FECHOS RELACIONAIS",
        svg,
        "As arestas azuis contínuas representam a relação original R. As arestas roxas pontilhadas são adicionadas pelo algoritmo de Warshall por transitividade (caminhos de comprimento ≥ 2)."
    )

# ==============================================================================
# TOPICO 4: Componentes Conexas e Partições
# ==============================================================================
def get_diagram_topico_4_components() -> str:
    svg = """<svg viewBox="0 0 640 240" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Component 1: {1, 2, 3} -->
  <g transform="translate(30, 20)">
    <rect width="180" height="190" rx="12" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
    <text x="90" y="28" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#1e40af">Classe [1] = {1, 2, 3}</text>
    
    <line x1="50" y1="70" x2="130" y2="70" stroke="#0071e3" stroke-width="2"/>
    <line x1="130" y1="70" x2="90" y2="150" stroke="#0071e3" stroke-width="2"/>
    <line x1="90" y1="150" x2="50" y2="70" stroke="#0071e3" stroke-width="2"/>

    <circle cx="50" cy="70" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
    <text x="50" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">1</text>
    <circle cx="130" cy="70" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
    <text x="130" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">2</text>
    <circle cx="90" cy="150" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
    <text x="90" y="155" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">3</text>
  </g>

  <!-- Component 2: {4, 5, 6} -->
  <g transform="translate(240, 20)">
    <rect width="180" height="190" rx="12" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
    <text x="90" y="28" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#166534">Classe [4] = {4, 5, 6}</text>
    
    <line x1="50" y1="70" x2="130" y2="70" stroke="#10b981" stroke-width="2"/>
    <line x1="50" y1="70" x2="50" y2="150" stroke="#10b981" stroke-width="2"/>

    <circle cx="50" cy="70" r="16" fill="#ffffff" stroke="#10b981" stroke-width="2"/>
    <text x="50" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">4</text>
    <circle cx="130" cy="70" r="16" fill="#ffffff" stroke="#10b981" stroke-width="2"/>
    <text x="130" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">5</text>
    <circle cx="50" cy="150" r="16" fill="#ffffff" stroke="#10b981" stroke-width="2"/>
    <text x="50" y="155" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">6</text>
  </g>

  <!-- Component 3: {7} -->
  <g transform="translate(450, 20)">
    <rect width="150" height="190" rx="12" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1.5"/>
    <text x="75" y="28" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#6b21a8">Classe [7] = {7}</text>
    
    <circle cx="75" cy="110" r="18" fill="#ffffff" stroke="#8b5cf6" stroke-width="2"/>
    <text x="75" y="115" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">7</text>
    <text x="75" y="155" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-style="italic" fill="#64748b">(Isolado)</text>
  </g>
</svg>"""
    return wrap_diagram(
        "Componentes Conexas como Classes de Equivalência",
        "FIGURA 4.1 — PARTIÇÃO DO GRAFO NÃO-DIRECIONADO",
        svg,
        "Cada componente conexa no grafo não-direcionado corresponde rigorosamente a uma classe de equivalência disjunta da relação R = Conectado."
    )

def get_diagram_topico_4_mod3_partition() -> str:
    svg = """<svg viewBox="0 0 680 200" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Universe Box -->
  <rect x="15" y="15" width="650" height="170" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="35" y="40" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">Universo dos Inteiros ℤ particionado por Congruência Módulo 3</text>

  <!-- Block [0] -->
  <g transform="translate(35, 55)">
    <rect width="190" height="110" rx="10" fill="#ffffff" stroke="#bfdbfe" stroke-width="1.5"/>
    <text x="95" y="28" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#1e40af">Classe [0] (Resto 0)</text>
    <text x="95" y="60" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" fill="#334155">... -6, -3, 0, 3, 6, 9 ...</text>
    <text x="95" y="85" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#64748b">3k, k ∈ ℤ</text>
  </g>

  <!-- Block [1] -->
  <g transform="translate(245, 55)">
    <rect width="190" height="110" rx="10" fill="#ffffff" stroke="#bbf7d0" stroke-width="1.5"/>
    <text x="95" y="28" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#166534">Classe [1] (Resto 1)</text>
    <text x="95" y="60" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" fill="#334155">... -5, -2, 1, 4, 7, 10 ...</text>
    <text x="95" y="85" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#64748b">3k + 1, k ∈ ℤ</text>
  </g>

  <!-- Block [2] -->
  <g transform="translate(455, 55)">
    <rect width="190" height="110" rx="10" fill="#ffffff" stroke="#fed7aa" stroke-width="1.5"/>
    <text x="95" y="28" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#9a3412">Classe [2] (Resto 2)</text>
    <text x="95" y="60" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" fill="#334155">... -4, -1, 2, 5, 8, 11 ...</text>
    <text x="95" y="85" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#64748b">3k + 2, k ∈ ℤ</text>
  </g>
</svg>"""
    return wrap_diagram(
        "Partição de ℤ em Três Classes Disjuntas Módulo 3",
        "FIGURA 4.2 — CONGRUÊNCIA E PARTIÇÃO",
        svg,
        "A união das três classes reconstitui todo o conjunto dos inteiros ℤ, e a interseção de quaisquer duas classes é estritamente vazia."
    )

# ==============================================================================
# TOPICO 5: Projeção Canônica
# ==============================================================================
def get_diagram_topico_5_projection() -> str:
    svg = """<svg viewBox="0 0 680 300" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-proj" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0071e3"/>
    </marker>
  </defs>

  <!-- Left Container: Conjunto Universo A -->
  <rect x="20" y="20" width="340" height="260" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="190" y="45" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">Conjunto Universo A</text>

  <!-- Subclasses in A -->
  <rect x="40" y="65" width="300" height="42" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
  <text x="190" y="90" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#1e40af">Bloco [0]: Múltiplos de n (resto 0)</text>

  <rect x="40" y="117" width="300" height="42" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
  <text x="190" y="142" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#166534">Bloco [1]: Resto 1 ({..., 1, n+1, ...})</text>

  <rect x="40" y="169" width="300" height="42" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1.5"/>
  <text x="190" y="194" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#6b21a8">Bloco [r]: Resto r ({..., r, n+r, ...})</text>

  <rect x="40" y="221" width="300" height="42" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
  <text x="190" y="246" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#9a3412">Bloco [n-1]: Resto n-1</text>

  <!-- Projection Arrows -->
  <path d="M 340 86 L 470 86" fill="none" stroke="#0071e3" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arr-proj)"/>
  <path d="M 340 138 L 470 138" fill="none" stroke="#0071e3" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arr-proj)"/>
  <path d="M 340 190 L 470 190" fill="none" stroke="#0071e3" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arr-proj)"/>
  <path d="M 340 242 L 470 242" fill="none" stroke="#0071e3" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arr-proj)"/>

  <!-- Projection Label -->
  <text x="405" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="700" fill="#0071e3">π</text>

  <!-- Right Container: Conjunto Quociente A/R -->
  <rect x="480" y="20" width="180" height="260" rx="12" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="570" y="45" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">Quociente A/R = ℤ_n</text>

  <!-- Target Elements in Quotient -->
  <circle cx="570" cy="86" r="18" fill="#eff6ff" stroke="#0071e3" stroke-width="2"/>
  <text x="570" y="91" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#1e40af">[0]</text>

  <circle cx="570" cy="138" r="18" fill="#f0fdf4" stroke="#10b981" stroke-width="2"/>
  <text x="570" y="143" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#166534">[1]</text>

  <circle cx="570" cy="190" r="18" fill="#faf5ff" stroke="#8b5cf6" stroke-width="2"/>
  <text x="570" y="195" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#6b21a8">[r]</text>

  <circle cx="570" cy="242" r="18" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
  <text x="570" y="247" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="700" fill="#9a3412">[n-1]</text>
</svg>"""
    return wrap_diagram(
        "Projeção Canônica π: A → A/R sobre o Conjunto Quociente",
        "FIGURA 5.1 — PROJEÇÃO CANÔNICA",
        svg,
        "A função canônica sobrejetora π mapeia cada elemento a ∈ A para a sua respectiva classe de equivalência [a] no conjunto quociente A/R."
    )

# ==============================================================================
# TOPICO 6: Hipercubo Booleano e Divisores D24
# ==============================================================================
def get_diagram_topico_6_hypercube() -> str:
    svg = """<svg viewBox="0 0 620 360" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Level Lines/Guides -->
  <line x1="40" y1="50" x2="580" y2="50" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="40" y1="140" x2="580" y2="140" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="40" y1="230" x2="580" y2="230" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="40" y1="310" x2="580" y2="310" stroke="#f1f5f9" stroke-width="1"/>

  <text x="50" y="55" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Nível 3 (Supremo)</text>
  <text x="50" y="145" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Nível 2 (Pares)</text>
  <text x="50" y="235" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Nível 1 (Unitários)</text>
  <text x="50" y="315" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Nível 0 (Ínfimo)</text>

  <!-- Edges -->
  <!-- Level 0 to 1 -->
  <line x1="310" y1="310" x2="190" y2="230" stroke="#64748b" stroke-width="1.8"/>
  <line x1="310" y1="310" x2="310" y2="230" stroke="#64748b" stroke-width="1.8"/>
  <line x1="310" y1="310" x2="430" y2="230" stroke="#64748b" stroke-width="1.8"/>

  <!-- Level 1 to 2 -->
  <line x1="190" y1="230" x2="190" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="190" y1="230" x2="310" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="310" y1="230" x2="190" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="310" y1="230" x2="430" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="430" y1="230" x2="310" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="430" y1="230" x2="430" y2="140" stroke="#64748b" stroke-width="1.8"/>

  <!-- Level 2 to 3 -->
  <line x1="190" y1="140" x2="310" y2="50" stroke="#64748b" stroke-width="1.8"/>
  <line x1="310" y1="140" x2="310" y2="50" stroke="#64748b" stroke-width="1.8"/>
  <line x1="430" y1="140" x2="310" y2="50" stroke="#64748b" stroke-width="1.8"/>

  <!-- Level 0 Node -->
  <rect x="285" y="294" width="50" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="310" y="315" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">∅</text>

  <!-- Level 1 Nodes -->
  <rect x="165" y="214" width="50" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="190" y="235" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{a}</text>

  <rect x="285" y="214" width="50" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="310" y="235" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{b}</text>

  <rect x="405" y="214" width="50" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="430" y="235" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{c}</text>

  <!-- Level 2 Nodes -->
  <rect x="155" y="124" width="70" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="190" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{a, b}</text>

  <rect x="275" y="124" width="70" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="310" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{a, c}</text>

  <rect x="395" y="124" width="70" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="430" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{b, c}</text>

  <!-- Level 3 Node -->
  <rect x="265" y="34" width="90" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="310" y="55" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{a, b, c}</text>
</svg>"""
    return wrap_diagram(
        "Diagrama de Hasse do Hipercubo Booleano 𝒫({a,b,c})",
        "FIGURA 6.1 — RETICULADO BOOLEANO",
        svg,
        "A ordem parcial por inclusão ⊆ forma um reticulado booleano graduado com 2³ = 8 vértices e 12 arestas de cobertura."
    )

def get_diagram_topico_6_divisors_24() -> str:
    svg = """<svg viewBox="0 0 540 360" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Edges of D24 -->
  <!-- 1 -> 2, 1 -> 3 -->
  <line x1="270" y1="310" x2="200" y2="240" stroke="#64748b" stroke-width="1.8"/>
  <line x1="270" y1="310" x2="340" y2="240" stroke="#64748b" stroke-width="1.8"/>

  <!-- 2 -> 4, 2 -> 6 -->
  <line x1="200" y1="240" x2="160" y2="170" stroke="#64748b" stroke-width="1.8"/>
  <line x1="200" y1="240" x2="270" y2="170" stroke="#64748b" stroke-width="1.8"/>

  <!-- 3 -> 6 -->
  <line x1="340" y1="240" x2="270" y2="170" stroke="#64748b" stroke-width="1.8"/>

  <!-- 4 -> 8, 4 -> 12 -->
  <line x1="160" y1="170" x2="200" y2="100" stroke="#64748b" stroke-width="1.8"/>
  <line x1="160" y1="170" x2="340" y2="100" stroke="#64748b" stroke-width="1.8"/>

  <!-- 6 -> 12 -->
  <line x1="270" y1="170" x2="340" y2="100" stroke="#64748b" stroke-width="1.8"/>

  <!-- 8 -> 24, 12 -> 24 -->
  <line x1="200" y1="100" x2="270" y2="40" stroke="#64748b" stroke-width="1.8"/>
  <line x1="340" y1="100" x2="270" y2="40" stroke="#64748b" stroke-width="1.8"/>

  <!-- Nodes -->
  <!-- 1 -->
  <circle cx="270" cy="310" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="270" y="315" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">1</text>

  <!-- 2, 3 -->
  <circle cx="200" cy="240" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="200" y="245" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">2</text>

  <circle cx="340" cy="240" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="340" y="245" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">3</text>

  <!-- 4, 6 -->
  <circle cx="160" cy="170" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="160" y="175" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">4</text>

  <circle cx="270" cy="170" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="270" y="175" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">6</text>

  <!-- 8, 12 -->
  <circle cx="200" cy="100" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="200" y="105" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">8</text>

  <circle cx="340" cy="100" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="340" y="105" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">12</text>

  <!-- 24 -->
  <circle cx="270" cy="40" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="270" y="45" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">24</text>
</svg>"""
    return wrap_diagram(
        "Reticulado dos Divisores de 24 (D₂₄ sob Divisibilidade)",
        "FIGURA 6.2 — ORDEM PARCIAL DE DIVISIBILIDADE",
        svg,
        "D₂₄ = {1, 2, 3, 4, 6, 8, 12, 24}. O número 1 é o elemento mínimo absoluto (divide todos) e 24 é o elemento máximo absoluto."
    )

# ==============================================================================
# TOPICO 7: Poset Sem Topo/Fundo Únicos e Limitantes Superiores
# ==============================================================================
def get_diagram_topico_7_no_bounds() -> str:
    svg = """<svg viewBox="0 0 540 280" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Edges -->
  <line x1="160" y1="210" x2="160" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="160" y1="140" x2="110" y2="70" stroke="#64748b" stroke-width="1.8"/>
  <line x1="160" y1="140" x2="270" y2="70" stroke="#64748b" stroke-width="1.8"/>
  <line x1="160" y1="210" x2="380" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="380" y1="210" x2="380" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="380" y1="140" x2="270" y2="70" stroke="#64748b" stroke-width="1.8"/>
  <line x1="380" y1="140" x2="430" y2="70" stroke="#64748b" stroke-width="1.8"/>

  <!-- Nodes Minimais -->
  <g>
    <circle cx="160" cy="210" r="18" fill="#f0fdf4" stroke="#10b981" stroke-width="2.5"/>
    <text x="160" y="215" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#15803d">2</text>
  </g>
  <g>
    <circle cx="380" cy="210" r="18" fill="#f0fdf4" stroke="#10b981" stroke-width="2.5"/>
    <text x="380" y="215" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#15803d">3</text>
  </g>
  <text x="270" y="255" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#15803d">Minimais = {2, 3} (Não há mínimo único)</text>

  <!-- Nodes Intermediários -->
  <g>
    <circle cx="160" cy="140" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <text x="160" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">4</text>
  </g>
  <g>
    <circle cx="380" cy="140" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <text x="380" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">6</text>
  </g>

  <!-- Nodes Maximais -->
  <g>
    <circle cx="110" cy="70" r="18" fill="#fef2f2" stroke="#ef4444" stroke-width="2.5"/>
    <text x="110" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#b91c1c">8</text>
  </g>
  <g>
    <circle cx="270" cy="70" r="18" fill="#fef2f2" stroke="#ef4444" stroke-width="2.5"/>
    <text x="270" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#b91c1c">12</text>
  </g>
  <g>
    <circle cx="430" cy="70" r="18" fill="#fef2f2" stroke="#ef4444" stroke-width="2.5"/>
    <text x="430" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#b91c1c">18</text>
  </g>
  <text x="270" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#b91c1c">Maximais = {8, 12, 18} (Não há máximo único)</text>
</svg>"""
    return wrap_diagram(
        "Poset sem Elementos Extremais Globais Únicos",
        "FIGURA 7.1 — MAXIMAIS E MINIMAIS MÚLTIPLOS",
        svg,
        "No subconjunto {2, 3, 4, 6, 8, 12, 18} sob divisibilidade, existem múltiplos elementos minimais (verdes) e múltiplos maximais (vermelhos). Não existe nem mínimo ⊥ nem máximo ⊤."
    )

def get_diagram_topico_7_dual_bounds() -> str:
    svg = """<svg viewBox="0 0 540 280" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Edges -->
  <!-- Minimais a, b to Limitantes c, d -->
  <line x1="210" y1="210" x2="210" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="210" y1="210" x2="330" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="330" y1="210" x2="210" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="330" y1="210" x2="330" y2="140" stroke="#64748b" stroke-width="1.8"/>

  <!-- Limitantes c, d to Maximais e, f -->
  <line x1="210" y1="140" x2="210" y2="70" stroke="#64748b" stroke-width="1.8"/>
  <line x1="210" y1="140" x2="330" y2="70" stroke="#64748b" stroke-width="1.8"/>
  <line x1="330" y1="140" x2="210" y2="70" stroke="#64748b" stroke-width="1.8"/>
  <line x1="330" y1="140" x2="330" y2="70" stroke="#64748b" stroke-width="1.8"/>

  <!-- Minimais a, b -->
  <circle cx="210" cy="210" r="18" fill="#f0fdf4" stroke="#10b981" stroke-width="2"/>
  <text x="210" y="215" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#15803d">a</text>

  <circle cx="330" cy="210" r="18" fill="#f0fdf4" stroke="#10b981" stroke-width="2"/>
  <text x="330" y="215" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#15803d">b</text>

  <!-- Limitantes Superiores Comuns c, d -->
  <circle cx="210" cy="140" r="18" fill="#eff6ff" stroke="#0071e3" stroke-width="2"/>
  <text x="210" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#1e40af">c</text>

  <circle cx="330" cy="140" r="18" fill="#eff6ff" stroke="#0071e3" stroke-width="2"/>
  <text x="330" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#1e40af">d</text>

  <!-- Maximais e, f -->
  <circle cx="210" cy="70" r="18" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
  <text x="210" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#b91c1c">e</text>

  <circle cx="330" cy="70" r="18" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
  <text x="330" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#b91c1c">f</text>

  <!-- Annotations -->
  <text x="140" y="145" text-anchor="end" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#0071e3">Limitantes Superiores de {a,b}</text>
  <text x="140" y="215" text-anchor="end" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#15803d">Elementos {a,b}</text>
  <text x="140" y="75" text-anchor="end" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#ef4444">Maximais</text>
</svg>"""
    return wrap_diagram(
        "Poset com Limitantes Superiores Incomparáveis (Falha de Supremo)",
        "FIGURA 7.2 — AUSÊNCIA DE MENOR LIMITANTE SUPERIOR",
        svg,
        "O par {a, b} possui limitantes superiores comuns {c, d}. Como c e d são incomparáveis (c ≰ d e d ≰ c), não existe menor elemento entre eles, demonstrando que sup{a, b} não existe."
    )

# ==============================================================================
# TOPICO 8: Aulas de Diagramas de Hasse (Algoritmo, Extremais, Hipercubo, D12, Cruzamento, N5/M3)
# ==============================================================================
def get_diagram_topico_8_algorithm() -> str:
    svg = """<svg viewBox="0 0 620 400" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-step" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0071e3"/>
    </marker>
  </defs>

  <!-- Step 1: Dígrafo da Ordem -->
  <g transform="translate(130, 20)">
    <rect width="360" height="52" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="180" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">DÍGRAFO DA ORDEM (P, ≤)</text>
  </g>

  <!-- Transition 1 -->
  <line x1="310" y1="72" x2="310" y2="120" stroke="#0071e3" stroke-width="2" marker-end="url(#arr-step)"/>
  <rect x="180" y="85" width="260" height="22" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
  <text x="310" y="100" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#1e40af">Regra 1: Supressão da Reflexividade (Remove Laços)</text>

  <!-- Step 2: Dígrafo Acíclico Estrito -->
  <g transform="translate(130, 125)">
    <rect width="360" height="52" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="180" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">DÍGRAFO ACÍCLICO ESTRITO (P, &lt;)</text>
  </g>

  <!-- Transition 2 -->
  <line x1="310" y1="177" x2="310" y2="225" stroke="#0071e3" stroke-width="2" marker-end="url(#arr-step)"/>
  <rect x="180" y="190" width="260" height="22" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
  <text x="310" y="205" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#1e40af">Regra 2: Redução Transitiva (Remove Atalhos)</text>

  <!-- Step 3: Dígrafo de Cobertura -->
  <g transform="translate(130, 230)">
    <rect width="360" height="52" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="180" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">DÍGRAFO DE COBERTURA (P, ⋖)</text>
  </g>

  <!-- Transition 3 -->
  <line x1="310" y1="282" x2="310" y2="330" stroke="#0071e3" stroke-width="2" marker-end="url(#arr-step)"/>
  <rect x="160" y="295" width="300" height="22" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
  <text x="310" y="310" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#1e40af">Regra 3: Disposição Vertical e Arestas Não-Direcionadas</text>

  <!-- Step 4: Diagrama de Hasse -->
  <g transform="translate(130, 335)">
    <rect width="360" height="52" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="2"/>
    <text x="180" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#15803d">DIAGRAMA DE HASSE FINAL</text>
  </g>
</svg>"""
    return wrap_diagram(
        "O Algoritmo de Simplificação de Hasse em Três Regras Estritas",
        "FIGURA 8.1 — PIPELINE ALGORÍTMICO",
        svg,
        "Redução do dígrafo original da ordem em seu Diagrama de Hasse via eliminação de laços reflexivos, redução transitiva e elevação espacial ascendente."
    )

def get_diagram_topico_8_extremals() -> str:
    svg = """<svg viewBox="0 0 520 300" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Edges -->
  <line x1="260" y1="240" x2="190" y2="180" stroke="#64748b" stroke-width="1.8"/>
  <line x1="260" y1="240" x2="330" y2="180" stroke="#64748b" stroke-width="1.8"/>
  <line x1="190" y1="180" x2="190" y2="120" stroke="#64748b" stroke-width="1.8"/>
  <line x1="330" y1="180" x2="330" y2="120" stroke="#64748b" stroke-width="1.8"/>
  <line x1="190" y1="120" x2="150" y2="60" stroke="#64748b" stroke-width="1.8"/>
  <line x1="190" y1="120" x2="330" y2="60" stroke="#64748b" stroke-width="1.8"/>
  <line x1="330" y1="120" x2="330" y2="60" stroke="#64748b" stroke-width="1.8"/>

  <!-- Unique Bottom (⊥) -->
  <circle cx="260" cy="240" r="18" fill="#eff6ff" stroke="#0071e3" stroke-width="2.5"/>
  <text x="260" y="245" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" fill="#0071e3">⊥</text>
  <text x="370" y="245" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#0071e3">Mínimo Global Único (Grau inf = 0)</text>

  <!-- Level 1: a, b -->
  <circle cx="190" cy="180" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="190" y="185" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">a</text>

  <circle cx="330" cy="180" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="330" y="185" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">b</text>

  <!-- Level 2: c, d -->
  <circle cx="190" cy="120" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="190" y="125" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">c</text>

  <circle cx="330" cy="120" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="330" y="125" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">d</text>

  <!-- Maximais: M1, M2 -->
  <circle cx="150" cy="60" r="18" fill="#fef2f2" stroke="#ef4444" stroke-width="2.5"/>
  <text x="150" y="65" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#b91c1c">M₁</text>

  <circle cx="330" cy="60" r="18" fill="#fef2f2" stroke="#ef4444" stroke-width="2.5"/>
  <text x="330" y="65" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#b91c1c">M₂</text>
  <text x="370" y="65" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" fill="#b91c1c">Maximais Múltiplos (Grau sup = 0)</text>
</svg>"""
    return wrap_diagram(
        "Identificação Topológica de Elementos Extremais",
        "FIGURA 8.2 — ASSINATURA TOPOLÓGICA",
        svg,
        "Nós sem arestas superiores são maximais (M₁, M₂). O nó inferior único de onde partem caminhos para todos os vértices é o mínimo absoluto ⊥."
    )

def get_diagram_topico_8_hypercube() -> str:
    # Re-use the clean hypercube SVG
    return wrap_diagram(
        "O Hipercubo Booleano 𝒫({a,b,c}) sob Inclusão",
        "EXEMPLO 1 — RETICULADO BOOLEANO Q₃",
        get_diagram_topico_6_hypercube_raw(),
        "Cada nível k representa subconjuntos de cardinalidade exata k. As arestas representam a relação de cobertura X ⋖ Y ⟺ X ⊂ Y e |Y| = |X| + 1."
    )

def get_diagram_topico_6_hypercube_raw() -> str:
    return """<svg viewBox="0 0 620 360" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Level Lines -->
  <line x1="40" y1="50" x2="580" y2="50" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="40" y1="140" x2="580" y2="140" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="40" y1="230" x2="580" y2="230" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="40" y1="310" x2="580" y2="310" stroke="#f1f5f9" stroke-width="1"/>

  <text x="50" y="55" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Nível 3: {a, b, c} (Top ⊤)</text>
  <text x="50" y="145" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Nível 2: Pares</text>
  <text x="50" y="235" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Nível 1: Unitários</text>
  <text x="50" y="315" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Nível 0: ∅ (Bottom ⊥)</text>

  <!-- Edges -->
  <line x1="310" y1="310" x2="190" y2="230" stroke="#64748b" stroke-width="1.8"/>
  <line x1="310" y1="310" x2="310" y2="230" stroke="#64748b" stroke-width="1.8"/>
  <line x1="310" y1="310" x2="430" y2="230" stroke="#64748b" stroke-width="1.8"/>

  <line x1="190" y1="230" x2="190" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="190" y1="230" x2="310" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="310" y1="230" x2="190" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="310" y1="230" x2="430" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="430" y1="230" x2="310" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="430" y1="230" x2="430" y2="140" stroke="#64748b" stroke-width="1.8"/>

  <line x1="190" y1="140" x2="310" y2="50" stroke="#64748b" stroke-width="1.8"/>
  <line x1="310" y1="140" x2="310" y2="50" stroke="#64748b" stroke-width="1.8"/>
  <line x1="430" y1="140" x2="310" y2="50" stroke="#64748b" stroke-width="1.8"/>

  <!-- Nodes -->
  <rect x="285" y="294" width="50" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="310" y="315" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">∅</text>

  <rect x="165" y="214" width="50" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="190" y="235" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{a}</text>

  <rect x="285" y="214" width="50" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="310" y="235" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{b}</text>

  <rect x="405" y="214" width="50" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="430" y="235" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{c}</text>

  <rect x="155" y="124" width="70" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="190" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{a, b}</text>

  <rect x="275" y="124" width="70" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="310" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{a, c}</text>

  <rect x="395" y="124" width="70" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="430" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{b, c}</text>

  <rect x="265" y="34" width="90" height="32" rx="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="310" y="55" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">{a, b, c}</text>
</svg>"""

def get_diagram_topico_8_divisors_12() -> str:
    svg = """<svg viewBox="0 0 460 300" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Edges -->
  <line x1="230" y1="240" x2="160" y2="170" stroke="#64748b" stroke-width="1.8"/>
  <line x1="230" y1="240" x2="300" y2="170" stroke="#64748b" stroke-width="1.8"/>
  <line x1="160" y1="170" x2="160" y2="100" stroke="#64748b" stroke-width="1.8"/>
  <line x1="160" y1="170" x2="300" y2="100" stroke="#64748b" stroke-width="1.8"/>
  <line x1="300" y1="170" x2="300" y2="100" stroke="#64748b" stroke-width="1.8"/>
  <line x1="160" y1="100" x2="230" y2="40" stroke="#64748b" stroke-width="1.8"/>
  <line x1="300" y1="100" x2="230" y2="40" stroke="#64748b" stroke-width="1.8"/>

  <!-- Nodes -->
  <!-- 1 -->
  <circle cx="230" cy="240" r="18" fill="#eff6ff" stroke="#0071e3" stroke-width="2"/>
  <text x="230" y="245" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#1e40af">1</text>
  <text x="270" y="245" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#64748b">Bottom ⊥</text>

  <!-- 2, 3 -->
  <circle cx="160" cy="170" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="160" y="175" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">2</text>

  <circle cx="300" cy="170" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="300" y="175" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">3</text>

  <!-- 4, 6 -->
  <circle cx="160" cy="100" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="160" y="105" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">4</text>

  <circle cx="300" cy="100" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="300" y="105" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">6</text>

  <!-- 12 -->
  <circle cx="230" cy="40" r="18" fill="#f0fdf4" stroke="#10b981" stroke-width="2"/>
  <text x="230" y="45" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#15803d">12</text>
  <text x="270" y="45" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#15803d">Top ⊤</text>
</svg>"""
    return wrap_diagram(
        "Diagrama de Hasse dos Divisores de 12 (D₁₂ sob Divisibilidade)",
        "EXEMPLO 2 — RETICULADO DISTRIBUTIVO D₁₂",
        svg,
        "D₁₂ = {1, 2, 3, 4, 6, 12}. Como todo par possui supremo (MMC) e ínfimo (MDC) únicos, D₁₂ é um reticulado distributivo completo."
    )

def get_diagram_topico_8_cross_lattice() -> str:
    svg = """<svg viewBox="0 0 460 300" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Cross Edges -->
  <line x1="230" y1="240" x2="160" y2="180" stroke="#64748b" stroke-width="1.8"/>
  <line x1="230" y1="240" x2="300" y2="180" stroke="#64748b" stroke-width="1.8"/>

  <!-- The X Cross -->
  <line x1="160" y1="180" x2="160" y2="110" stroke="#64748b" stroke-width="1.8"/>
  <line x1="160" y1="180" x2="300" y2="110" stroke="#0071e3" stroke-width="2"/>
  <line x1="300" y1="180" x2="160" y2="110" stroke="#0071e3" stroke-width="2"/>
  <line x1="300" y1="180" x2="300" y2="110" stroke="#64748b" stroke-width="1.8"/>

  <line x1="160" y1="110" x2="230" y2="40" stroke="#64748b" stroke-width="1.8"/>
  <line x1="300" y1="110" x2="230" y2="40" stroke="#64748b" stroke-width="1.8"/>

  <!-- Nodes -->
  <!-- Bottom ⊥ -->
  <circle cx="230" cy="240" r="18" fill="#eff6ff" stroke="#0071e3" stroke-width="2"/>
  <text x="230" y="245" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" fill="#0071e3">⊥</text>

  <!-- a, b -->
  <circle cx="160" cy="180" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="160" y="185" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">a</text>

  <circle cx="300" cy="180" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="300" y="185" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">b</text>

  <!-- c, d -->
  <circle cx="160" cy="110" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="160" y="115" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">c</text>

  <circle cx="300" cy="110" r="18" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
  <text x="300" y="115" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">d</text>

  <!-- Top ⊤ -->
  <circle cx="230" cy="40" r="18" fill="#f0fdf4" stroke="#10b981" stroke-width="2"/>
  <text x="230" y="45" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" fill="#15803d">⊤</text>
</svg>"""
    return wrap_diagram(
        "Poset com Cruzamento Central X ({⊥, a, b, c, d, ⊤})",
        "FIGURA 8.3 — TOPOLOGIA DE CRUZAMENTO",
        svg,
        "As conexões cruzadas a ⋖ d e b ⋖ c produzem limitantes superiores comuns c e d para o par {a, b}. Como c e d são incomparáveis, este poset NÃO é um reticulado."
    )

def get_diagram_topico_8_n5_m3() -> str:
    svg = """<svg viewBox="0 0 680 320" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Sublattice N5 (Pentágono) -->
  <g transform="translate(40, 20)">
    <rect width="280" height="280" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="140" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">Reticulado N₅ (Pentágono)</text>
    <text x="140" y="50" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#ef4444">Não-Modular (Teorema de Dedekind)</text>

    <!-- N5 Edges -->
    <line x1="140" y1="240" x2="80" y2="180" stroke="#64748b" stroke-width="2"/>
    <line x1="80" y1="180" x2="80" y2="120" stroke="#64748b" stroke-width="2"/>
    <line x1="80" y1="120" x2="140" y2="70" stroke="#64748b" stroke-width="2"/>
    <line x1="140" y1="240" x2="200" y2="150" stroke="#64748b" stroke-width="2"/>
    <line x1="200" y1="150" x2="140" y2="70" stroke="#64748b" stroke-width="2"/>

    <!-- N5 Nodes -->
    <circle cx="140" cy="240" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
    <text x="140" y="245" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">0</text>

    <circle cx="80" cy="180" r="16" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <text x="80" y="185" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">a</text>

    <circle cx="80" cy="120" r="16" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <text x="80" y="125" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">b</text>

    <circle cx="200" cy="150" r="16" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <text x="200" y="155" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">c</text>

    <circle cx="140" cy="70" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
    <text x="140" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">1</text>
  </g>

  <!-- Sublattice M3 (Diamante) -->
  <g transform="translate(360, 20)">
    <rect width="280" height="280" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="140" y="32" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">Reticulado M₃ (Diamante)</text>
    <text x="140" y="50" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="11" font-weight="600" fill="#b45309">Modular, mas Não-Distributivo</text>

    <!-- M3 Edges -->
    <line x1="140" y1="240" x2="60" y2="150" stroke="#64748b" stroke-width="2"/>
    <line x1="140" y1="240" x2="140" y2="150" stroke="#64748b" stroke-width="2"/>
    <line x1="140" y1="240" x2="220" y2="150" stroke="#64748b" stroke-width="2"/>

    <line x1="60" y1="150" x2="140" y2="70" stroke="#64748b" stroke-width="2"/>
    <line x1="140" y1="150" x2="140" y2="70" stroke="#64748b" stroke-width="2"/>
    <line x1="220" y1="150" x2="140" y2="70" stroke="#64748b" stroke-width="2"/>

    <!-- M3 Nodes -->
    <circle cx="140" cy="240" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
    <text x="140" y="245" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">0</text>

    <circle cx="60" cy="150" r="16" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <text x="60" y="155" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">a</text>

    <circle cx="140" cy="150" r="16" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <text x="140" y="155" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">b</text>

    <circle cx="220" cy="150" r="16" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <text x="220" y="155" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">c</text>

    <circle cx="140" cy="70" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
    <text x="140" y="75" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" fill="#0f172a">1</text>
  </g>
</svg>"""
    return wrap_diagram(
        "Sub-reticulados Proibidos: Teoremas de Dedekind e Birkhoff",
        "FIGURA 8.4 — RETICULADOS PROIBIDOS N₅ E M₃",
        svg,
        "Um reticulado é modular se e somente se não contém N₅ como sub-reticulado. Um reticulado é distributivo se e somente se não contém nem N₅ nem M₃."
    )


def get_diagram_topico_8_poset_g() -> str:
    svg = """<svg viewBox="0 0 540 360" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Arestas de Cobertura -->
  <!-- Level 0 -> Level 1: a->c, b->c, b->d -->
  <line x1="200" y1="300" x2="200" y2="210" stroke="#64748b" stroke-width="2"/>
  <line x1="340" y1="300" x2="200" y2="210" stroke="#64748b" stroke-width="2"/>
  <line x1="340" y1="300" x2="340" y2="210" stroke="#64748b" stroke-width="2"/>

  <!-- Level 1 -> Level 2: c->e, c->f, d->f -->
  <line x1="200" y1="210" x2="200" y2="120" stroke="#64748b" stroke-width="2"/>
  <line x1="200" y1="210" x2="340" y2="120" stroke="#64748b" stroke-width="2"/>
  <line x1="340" y1="210" x2="340" y2="120" stroke="#64748b" stroke-width="2"/>

  <!-- Level 2 -> Level 3: e->g, f->g -->
  <line x1="200" y1="120" x2="270" y2="40" stroke="#64748b" stroke-width="2"/>
  <line x1="340" y1="120" x2="270" y2="40" stroke="#64748b" stroke-width="2"/>

  <!-- Nos Level 0: a, b (Minimais) -->
  <circle cx="200" cy="300" r="18" fill="#ffffff" stroke="#10b981" stroke-width="2.5"/>
  <text x="200" y="305" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">a</text>

  <circle cx="340" cy="300" r="18" fill="#ffffff" stroke="#10b981" stroke-width="2.5"/>
  <text x="340" y="305" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">b</text>

  <!-- Nos Level 1: c, d -->
  <circle cx="200" cy="210" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="200" y="215" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">c</text>

  <circle cx="340" cy="210" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="340" y="215" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">d</text>

  <!-- Nos Level 2: e, f -->
  <circle cx="200" cy="120" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="200" y="125" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">e</text>

  <circle cx="340" cy="120" r="18" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="340" y="125" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">f</text>

  <!-- No Level 3: g (Maximo) -->
  <circle cx="270" cy="40" r="18" fill="#ffffff" stroke="#8b5cf6" stroke-width="2.5"/>
  <text x="270" y="45" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">g</text>
</svg>"""
    return wrap_diagram(
        "Diagrama de Hasse do Poset P = {a, b, c, d, e, f, g}",
        "FIGURA 8.5 — DIAGRAMA DE HASSE DE COBERTURAS",
        svg,
        "Estrutura com elementos minimais {a, b}, intermediários {c, d, e, f} e elemento máximo único g."
    )


def get_diagram_topico_8_d36() -> str:
    svg = """<svg viewBox="0 0 540 380" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Arestas de D36 (Produto C3 x C3) -->
  <!-- Linhas horizontais (fator 2: 1->2->4; 3->6->12; 9->18->36) -->
  <line x1="170" y1="320" x2="270" y2="280" stroke="#64748b" stroke-width="1.8"/>
  <line x1="270" y1="280" x2="370" y2="240" stroke="#64748b" stroke-width="1.8"/>

  <line x1="170" y1="220" x2="270" y2="180" stroke="#64748b" stroke-width="1.8"/>
  <line x1="270" y1="180" x2="370" y2="140" stroke="#64748b" stroke-width="1.8"/>

  <line x1="170" y1="120" x2="270" y2="80" stroke="#64748b" stroke-width="1.8"/>
  <line x1="270" y1="80" x2="370" y2="40" stroke="#64748b" stroke-width="1.8"/>

  <!-- Linhas verticais (fator 3: 1->3->9; 2->6->18; 4->12->36) -->
  <line x1="170" y1="320" x2="170" y2="220" stroke="#64748b" stroke-width="1.8"/>
  <line x1="170" y1="220" x2="170" y2="120" stroke="#64748b" stroke-width="1.8"/>

  <line x1="270" y1="280" x2="270" y2="180" stroke="#64748b" stroke-width="1.8"/>
  <line x1="270" y1="180" x2="270" y2="80" stroke="#64748b" stroke-width="1.8"/>

  <line x1="370" y1="240" x2="370" y2="140" stroke="#64748b" stroke-width="1.8"/>
  <line x1="370" y1="140" x2="370" y2="40" stroke="#64748b" stroke-width="1.8"/>

  <!-- Vértices -->
  <!-- 1, 2, 4 -->
  <circle cx="170" cy="320" r="16" fill="#ffffff" stroke="#10b981" stroke-width="2"/>
  <text x="170" y="325" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#0f172a">1</text>

  <circle cx="270" cy="280" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="270" y="285" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#0f172a">2</text>

  <circle cx="370" cy="240" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="370" y="245" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#0f172a">4</text>

  <!-- 3, 6, 12 -->
  <circle cx="170" cy="220" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="170" y="225" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#0f172a">3</text>

  <circle cx="270" cy="180" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="270" y="185" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#0f172a">6</text>

  <circle cx="370" cy="140" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="370" y="145" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#0f172a">12</text>

  <!-- 9, 18, 36 -->
  <circle cx="170" cy="120" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="170" y="125" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#0f172a">9</text>

  <circle cx="270" cy="80" r="16" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="270" y="85" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#0f172a">18</text>

  <circle cx="370" cy="40" r="16" fill="#ffffff" stroke="#8b5cf6" stroke-width="2"/>
  <text x="370" y="45" text-anchor="middle" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" fill="#0f172a">36</text>
</svg>"""
    return wrap_diagram(
        "Diagrama de Hasse de D₃₆ ≅ C₃ × C₃",
        "FIGURA 8.6 — PRODUTO DE CADEIAS FINITAS",
        svg,
        "Reticulado distributivo isomorfo à grade 3×3 dos expoentes primos de 36 = 2² · 3² (12 arestas de cobertura)."
    )
