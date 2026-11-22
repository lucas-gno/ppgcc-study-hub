# ADR 0004: Geração Estática de Aulas Teóricas, Pilar Visual/Interativo, Sandboxes Jupyter e Separação do Banco de Questões

- **Status:** Aprovado (Revisado em 2026-11-22)
- **Data:** 2026-11-22
- **Decisor:** Lucas Galdino (Usuário) & Antigravity (Agente)

---

## Contexto e Problema
As aulas teóricas precisam cumprir rigorosamente os dois pilares estabelecidos no `NOTES.md`:
1. **A Dicotomia Obrigatória: Visual vs. Interativo** (diagramas vetoriais SVG nativos + manipuladores de estado em tempo real conectados a `assets/widgets.js`).
2. **Sandboxes Jupyter no Navegador** (`.notebook-cell` com topbar macOS minimalista, código didático em tema dark monospaced, `.notebook-inputs-group` para variar parâmetros, botões de execução/passo/reset com ícones SVG minimalistas, console `stdout` colorido e `.notebook-inspector-panel` para inspeção de memória e ponteiros) nas aulas de código, algoritmos e sistemas.

Além disso, incluir questões de múltipla escolha dentro do corpo da aula polui a experiência de leitura conceitual e fragmenta o fluxo do motor de repetição espaçada (FSRS v5) e das métricas de progresso.

## Decisão
1. Implementaremos um script utilitário determinístico (`scripts/generate_lessons.py`) que gera arquivos HTML estáticos puros, semânticos e autocontidos em `lessons/XXXX-<slug>.html`.
2. Cada aula embute obrigatoriamente:
   - Didática **Zero Base** com **Tradução Tríplice** (Fórmula Simbólica Formal, Caixa `.como-se-le` fonética, Tradução Intuitiva / Analogia Prática de TI);
   - **Pilar Visual:** Diagramas vetoriais em `<svg>` puro integrados ao HTML;
   - **Pilar Interativo:** Controles manipuláveis instanciados a partir de `assets/widgets.js`;
   - **Sandboxes Jupyter no Navegador (`.notebook-cell`):** Obrigatório em todas as aulas das Fases 2 (Programação C/Python), 3 (Algoritmos e Estruturas de Dados) e 4 (Sistemas/Contêineres).
3. **Separação Estrita de Questões:** Nenhuma questão de múltipla escolha ficará no corpo da aula. Toda a prática objetiva é centralizada exclusivamente em `questoes.html` (Banco de Questões) e `simulados.html` (Simulados).
4. **Integração por Deep-Link:** Ao final de cada aula, uma barra de conclusão minimalista oferece duas ações:
   - Marcar a aula como concluída (sincronizado com `assets/store.js`);
   - Botão primário **"Praticar questões desta aula"** (`href="../questoes.html?topico=<id>"`), que abre o Banco de Questões já pré-filtrado para aquele tópico específico.

## Consequências
### Positivas
- **Leitura Imersiva e Limpa:** A aula concentra-se exclusivamente na construção conceitual (Zero Base + SVG + Widget Interativo + Sandbox), sem distrações de quiz estático.
- **Fonte Única de Prática e FSRS:** Todas as respostas, erros, favoritas e intervalos de repetição espaçada ficam consolidados em um único motor determinístico em `questoes.html`.
- **Velocidade Instantânea:** HTML pré-compilado abre sem latência tanto no GitHub Pages quanto via protocolo local `file:///`.
