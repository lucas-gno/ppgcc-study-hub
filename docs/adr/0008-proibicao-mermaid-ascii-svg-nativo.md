# ADR 0008: Proibição Estrita de Mermaid e ASCII Art — Padrão Obrigatório de Diagramas Vetoriais em SVG Nativo

- **Status:** Aprovado
- **Data:** 2026-11-22
- **Decisor:** Lucas Galdino (Usuário) & Antigravity (Agente)

---

## 1. Contexto e Problema

Durante a validação visual das primeiras aulas da Fase 1 geradas no repositório, identificamos duas falhas críticas de didática e experiência do usuário:
1. **Blocos de Código Mermaid Quebrados:** Diagramas declarados como ````mermaid flowchart LR ... ```` foram renderizados na tela como blocos escuros de código-fonte cru `<pre><code>...</code></pre>`. Isso ocorreu porque a arquitetura do projeto é **100% estática, offline-first e sem dependências de rede externas** ([ADR 0001](0001-frontend-mpa-architecture.md) e [ADR 0005](0005-github-pages-deployment.md)), não havendo runtime JavaScript do Mermaid instalado.
2. **Diagramas em Texto ASCII Desformatado:** Diversas seções teóricas fundamentais (algoritmo de simplificação de Hasse, elementos extremais, divisores de 24, reticulado $D_{12}$ e hipercubo booleano $Q_3$) foram inicialmente redigidas como arte ASCII monoespaçada (`/ \ | X \ /`, `[M1]`, etc.) dentro de blocos de texto. Em telas de alta resolução, essas representações quebram alinhamentos, não possuem contraste hierárquico e transmitem um aspecto amador e inacabado, em contraste direto com os Laboratórios Interativos (`assets/widgets.js`), que usam vetores SVG elegantes e minimalistas.

---

## 2. Decisão

### 2.1. Proibições Terminantes
1. **É TERMINANTEMENTE PROIBIDO USAR MERMAID:** Nenhum agente deve tentar escrever blocos `mermaid`, `flowchart` ou tentar "resolver" a ausência do Mermaid injetando scripts externos (`<script src="https://cdn...">`), pacotes `npm` ou bundlers pesados. Isso violaria a regra de zero CDNs externas e o funcionamento offline via `file:///`.
2. **É TERMINANTEMENTE PROIBIDO USAR ASCII ART:** Nenhum agente deve desenhar diagramas estruturais com caracteres de texto (`/`, `\`, `|`, `+---`, `X`, etc.) dentro de blocos monoespaçados.

---

### 2.2. Padrão Obrigatório: Componentes Vetoriais SVG Nativos

Todo e qualquer diagrama representativo (fluxogramas, dígrafos, reticulados, topologias de rede, mapas de memória Stack/Heap, diagramas de ponteiros, alinhamento de structs, etc.) deve ser implementado como **vetor `<svg>` nativo puro**, encapsulado no componente padronizado `.visual-diagram-card`.

---

## 3. Passo a Passo Obrigatório (Receita para Fases 2, 3 e 4)

Qualquer agente que for implementar novas aulas (Fase 2: Programação C/Python; Fase 3: Algoritmos e Estruturas de Dados; Fase 4: Sistemas e Contêineres) DEVE seguir rigorosamente estes 5 passos:

### Passo 1: Construir a Função do Diagrama em `scripts/svg_diagrams.py`
Crie uma função geradora do diagrama que utilize o helper `wrap_diagram`:
```python
import scripts.svg_diagrams as sd

def get_diagram_topico_XX_meu_diagrama() -> str:
    svg = """<svg viewBox="0 0 640 260" class="responsive-diagram-svg" xmlns="http://www.w3.org/2000/svg">
  <!-- Definições de marcadores de setas minimalistas -->
  <defs>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0071e3"/>
    </marker>
  </defs>

  <!-- Elementos visuais com tipografia de sistema Apple e paleta de alto contraste -->
  <rect x="20" y="20" width="180" height="80" rx="10" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>
  <text x="110" y="65" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Text', system-ui, sans-serif" font-size="14" font-weight="700" fill="#0f172a">Stack Frame</text>
</svg>"""
    return sd.wrap_diagram(
        title="Título Claro do Diagrama",
        tag="FIGURA X.X — CATEGORIA TEMÁTICA",
        svg_content=svg,
        caption="Legenda analítica rigorosa ancorada na cobrança do edital e da banca."
    )
```

### Passo 2: Utilizar a Estrutura Semântica `.visual-diagram-card`
O helper `wrap_diagram` gera automaticamente a seguinte estrutura HTML validada:
```html
<div class="visual-diagram-card">
  <div class="diagram-header">
    <span class="diagram-tag">FIGURA X.X — IDENTIFICAÇÃO</span>
    <h4 class="diagram-title">Título Conceitual do Diagrama</h4>
  </div>
  <div class="diagram-body">
    <svg viewBox="0 0 W H" class="responsive-diagram-svg">...</svg>
  </div>
  <p class="diagram-caption">Legenda conceitual explicativa.</p>
</div>
```
Esta estrutura já possui suporte visual de alta fidelidade em `assets/style.css` e `assets/tufte-clean.css` (borda suave, elevação Apple, scroll horizontal seguro para smartphones e zero emojis).

### Passo 3: Inserir o Bloco HTML Diretamente no Banco SQLite (`data/mestrado.db`)
Insira o HTML retornado pela função dentro do campo `conteudo_markdown` da tabela `aulas`:
```python
cursor.execute(
    "UPDATE aulas SET conteudo_markdown = ? WHERE topico_id = ?",
    (conteudo_com_svg_html, topico_id)
)
conn.commit()
```

### Passo 4: Regenerar as Aulas Estáticas e o Bundle de Dados
O script `scripts/generate_lessons.py` possui suporte a blocos HTML de primeiro nível (`is_html_block_start` e rastreamento de profundidade de tags), preservando a marcação do diagrama sem quebrá-la em parágrafos `<p>` nem escapar tags:
```bash
python scripts/generate_lessons.py
python scripts/export_db.py
```

### Passo 5: Validar a Ausência de Regressões por Testes Automatizados
A suíte `tests/test_ui_contracts.py` valida automaticamente:
- Ausência de `language-mermaid`;
- Ausência de `flowchart`;
- Ausência de caracteres de árvores ASCII monoespaçadas;
- Presença obrigatória de containers `.visual-diagram-card`.
Execute:
```powershell
python -m unittest discover -s tests -v
node --test tests/*.test.mjs
```

---

## 4. Consequências

### Positivas
- **Aparência Profissional e Polida:** Diagramas SVG nativos escalam com perfeição em telas retina/4K e dispositivos móveis, sem distorção nem desformatação.
- **100% Autocontido e Offline:** Nenhuma requisição a CDNs de terceiros, compatível com abertura direta via `file:///` e com o GitHub Pages.
- **Manutenibilidade:** Diagramas centralizados em `scripts/svg_diagrams.py`, facilitando modificações, testes de acessibilidade e evolução visual.

### Negativas / Custos
- Exige que o agente desenhe coordenadas vetoriais `<svg>` (`<rect>`, `<circle>`, `<line>`, `<path>`, `<text>`) ao invés de escrever declarações textuais sucintas do Mermaid. Este custo é absorvido pela garantia de fidelidade visual absoluta e ausência de falhas em tempo de execução.
