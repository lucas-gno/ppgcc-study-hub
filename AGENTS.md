# AGENTS.md — Guia Mestre e Instruções Operacionais para Agentes de IA

> **ATENÇÃO, AGENTE:** Leia este documento antes de executar qualquer alteração no projeto. Se você acabou de assumir este repositório em outro desktop ou em uma nova sessão sem histórico de chat, leia em seguida [`docs/HANDOFF.md`](docs/HANDOFF.md), [`GLOSSARY.md`](GLOSSARY.md), [`docs/BANCA_E_EDITAL_2027.md`](docs/BANCA_E_EDITAL_2027.md) e os registros em [`docs/adr/`](docs/adr/).

---

## 1. Missão e Contexto Real do Concurso

- **Objetivo Central:** Aprovação em 1º lugar no **Processo Seletivo do Mestrado Acadêmico em Ciência da Computação (PPGCC - IFCE Campus Fortaleza)**, Edital nº 43/2026 (Retificações nº 01 e nº 02, Turma 2027.1).
- **Linha de Pesquisa e Tema:** Computação Aplicada (CA) — **Tema CA05:** *"Otimização de recursos computacionais em infraestruturas institucionais baseadas em contêineres"* (1 vaga, orientação do **Prof. Dr. Carlos Maurício Jaborandy de Mattos Dourado Júnior**).
- **Calendário Real Vigente (`22/11/2026`):**
  - **Prova Escrita Presencial ($NPE$):** **`04/12/2026` (sexta-feira)** (alterada de 05/12 pela Retificação nº 01), **20 questões objetivas**, 0,5 pt cada, **120 minutos (2 horas)**, corte $NPE \ge 3{,}00$ (meta $\ge 8{,}50$).
  - **Arguição Oral Presencial ($NA$):** **`14/12/2026` a `18/12/2026`**, máx. **20 minutos**, **6 perguntas** (3 Tipo 1 = 5 pts + 3 Tipo 2 = 5 pts), corte $NA \ge 7{,}00$ (meta $\ge 9{,}20$).
  - **Avaliação Curricular ($NC$ — Retificação nº 02):** $DA = \min(10, \max(0, IRA - 7{,}0) \times 3{,}34)$, $NC = \text{Total Anexo VI} / 10$, $NF = (NPE + NA + NC) / 3$.
- **Peso Real da Banca (Edital 53/2025 + Portaria nº 7234/2026):** 55% Algoritmos e Estruturas de Dados, 25% Programação (C/Python), 20% Lógica Matemática e Conjuntos. Veja detalhes em [`docs/BANCA_E_EDITAL_2027.md`](docs/BANCA_E_EDITAL_2027.md).

---

## 2. Perfil do Aluno e Didática Zero Base

- **Origem Não-Exata ("Enferrujado"):** O aluno (Lucas Galdino, Analista de TI na DGTI/IFCE) vem das Ciências Humanas e atua na prática de infraestrutura há anos. **É terminantemente proibido presumir qualquer conhecimento formal prévio.**
- **Tradução Tríplice Obrigatória em Todo Conceito Formal:**
  1. **Fórmula Simbólica Formal:** Notação rigorosa cobrada pela banca.
  2. **Caixa "Como se Lê" (`.como-se-le`):** Pronúncia fonética literal em voz alta.
  3. **Tradução Intuitiva / Analogia Prática:** Explicação ancorada no cotidiano de TI e infraestrutura.

---

## 3. Padrão de Aula: Visual + Interativo + Sandboxes Jupyter + Separação de Questões

> [!CRITICAL]
> **Visual** e **Interativo** são dois pilares distintos e complementares obrigatórios (`NOTES.md` Seção 2), somados aos **Sandboxes Jupyter no Navegador** (`NOTES.md` Seção 3).

1. **Pilar Visual (SVG Nativo — Proibido Mermaid e Proibido ASCII Art):** Toda aula contém diagramas vetoriais em `<svg>` puro embutidos diretamente no HTML dentro de containers `.visual-diagram-card` (Diagramas de Hasse $D_{12}$, hipercubo $Q_3$, $M_3/N_5$, dígrafos, Stack/Heap, BST/AVL, topologia Borg/Kubernetes). É **estritamente proibido** usar blocos `mermaid`/`flowchart` ou diagramas desenhados em texto ASCII desformatado.
2. **Pilar Interativo (`assets/widgets.js`):** Toda aula instancia controles táteis que reagem em tempo real (`initSetOperationsWidget`, `initBooleanMatrixWidget`, `initHasseReductionWidget`, etc.).
3. **Sandboxes Jupyter no Navegador (`.notebook-cell`):** Obrigatório em todas as aulas de código, algoritmos e sistemas (Fases 2, 3 e 4), contendo: topbar macOS minimalista, editor sintático dark monospaced, `.notebook-inputs-group`, botões Executar/Passo/Reset, console `stdout` colorido e `.notebook-inspector-panel` de memória/ponteiros.
4. **Separação Estrita Aulas vs. Banco de Questões (ADR 0004):**
   - **Proibido colocar questões de múltipla escolha no corpo das aulas.**
   - Toda prática de questões ocorre exclusivamente em `questoes.html` e `simulados.html`.
   - O rodapé de cada aula traz apenas o botão de marcar como concluída (`Store.toggleTopicRead`) e o botão primário **"Praticar questões desta aula"** (`../questoes.html?topico=<id>`).

---

## 4. Identidade Visual, Zero Emojis e Movimento

- **Zero Emojis (ADR 0007):** É estritamente proibido o uso de emojis em qualquer texto de interface, navegação, botões, badges, títulos, widgets ou documentação operacional.
- **Iconografia SVG Monocromática (`assets/icons.js`):** Somente ícones SVG inline (`1.5px` stroke, `stroke="currentColor"`).
- **Design System & Paddings:** Estética Apple HIG + Emil Kowalski (`assets/style.css`). Escala disciplinada de espaçamentos em múltiplos de `4px`/`8px` (cards com `padding: 24px`, grids com `gap: 20px–24px`, containers com `padding: 28px 24px`). Tipografia 100% grotesca sem serifas.
- **Movimento (`/animate` + `/emil-design-eng`):** Apenas `transform` e `opacity`, `:active scale(0.97)`, nunca `transition: all` ou `scale(0)`. Ações de teclado de alta frequência (`A`–`E`, `1`–`4` no treino de questões) não devem ter animação. Respeitar `@media (hover: hover) and (pointer: fine)` e `@media (prefers-reduced-motion: reduce)`.

---

## 5. Arquitetura Estática, Persistência e GitHub Pages (ADRs 0001–0007)

- **MPA 100% Estática e Offline-First (ADR 0001 & 0005):** Páginas HTML independentes na raiz (`index.html`, `edital.html`, `cronograma.html`, `questoes.html`, `simulados.html`, `arguicao.html`, `curriculo.html`) + `lessons/*.html`, servidas diretamente da raiz `/` da branch `main` no GitHub Pages e compatíveis com abertura local direta via `file:///`. Zero backend, zero autenticação, zero CDNs externas (`assets/katex/` local).
- **Pipeline de Dados (ADR 0002):** `data/mestrado.db` -> `scripts/import_official_2025.py` -> `scripts/export_db.py` -> `assets/data.js` (`window.PPGCC_DATA`) e `scripts/generate_lessons.py` -> `lessons/*.html`.
- **Estado no Cliente (ADR 0003):** `assets/store.js` gerencia persistência em `localStorage` (`ppgcc_study_hub_v1`), algoritmo determinístico FSRS v5, cálculos oficiais ($NPE, NA, DA, NC, NF$), planejador de Sprints reais e Backup JSON portável (Exportar/Importar).

---

## 6. Fluxo de Desenvolvimento, Tickets e TDD

- **Tickets Verticais (`/to-tickets`):** Todos os 8 tickets do projeto residem em `.scratch/ppgcc-study-hub/issues/<NN>-<slug>.md`. Trabalhe sempre na fronteira (tickets com todos os bloqueadores `done`).
- **TDD Estrito (`/tdd`):**
  - Testes Python (Seam A — Pipeline e Seam C — Contratos HTML): `python -m unittest discover -s tests -v`
  - Testes JavaScript (Seam B — `assets/store.js`, FSRS v5, fórmulas e filtros): `node --test tests/*.test.mjs`
  - Ciclo obrigatório **Red -> Green** em cada fatia vertical.
- **Checklist antes de finalizar qualquer ticket:**
  - [ ] Zero emojis em arquivos alterados;
  - [ ] Zero links para CDNs externas;
  - [ ] Suíte Python (`unittest`) e JS (`node --test`) 100% verdes;
  - [ ] Status do ticket atualizado e [`docs/HANDOFF.md`](docs/HANDOFF.md) sincronizado.
