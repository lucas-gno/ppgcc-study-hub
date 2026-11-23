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

## 2. Perfil do Aluno e Didática Zero Base (Princípio de Einstein)

- **Origem Não-Exata ("Enferrujado"):** O aluno (Lucas Galdino, Analista de TI na DGTI/IFCE) vem das Ciências Humanas e atua na prática de infraestrutura há anos. **É terminantemente proibido presumir qualquer conhecimento formal prévio.**
- **Princípio Maior de Einstein & Feynman:** *"Se você não consegue explicar algo para uma criança de seis anos, você mesmo não entende."* A formalidade matemática existe para dar precisão, nunca para intimidar ou parecer erudita.
- **Linguagem, Tom e Conexão com o Aluno:**
  - Linguajar acolhedor, próximo e direto, dialogando sempre com o aluno (*"Você"*).
  - Nunca iniciar com uma enxurrada de axiomas abstratos. Toda abstração matemática deve ser imediatamente aterrada com uma metáfora visceral do mundo real e de sistemas/infraestrutura (ex: pacotes de rede, nós em um cluster, permissões de arquivos, tabelas de banco de dados).
- **Tradução Tríplice e Desmistificação Fonética de Símbolos:**
  - É proibido usar qualquer símbolo matemático ($\in, \subseteq, \land, \iff, \forall, \exists, \equiv, \lessdot, \mid, \cup, \cap$) sem ensiná-lo primeiro.
  - Toda fórmula formal deve ser encapsulada em um container `.formula-box` contendo a fórmula KaTeX centralizada e uma barra de leitura integrada `.reading-guide`:
    - **Como se fala:** pronúncia fonética exata em voz alta (ex: *"a é congruente a b módulo n"*).
    - **O que significa:** explicação intuitiva imediata do operador (ex: *"Repare no símbolo com três tracinhos $\equiv$, que indica equivalência modular"*).
  - Blocos `.word-breakdown` com etimologia e pronúncia fonética silábica (`.pronunciation`, ex: `[pô-sét]`, `[an-ti-si-mé-tri-ca]`, `[há-sse]`).
  - Glossário / Dicionário de Pronúncia de Símbolos Lógicos presente em pontos estratégicos de cada fase.

---

## 3. Padrão de Aula: Visual + Interativo + Degraus Cognitivos + Active Retrieval

> [!CRITICAL]
> Toda aula segue rigorosamente uma estrutura em **degraus cognitivos em micro-blocos**, combinando quatro pilares complementares.

1. **Pilar Visual (SVG Nativo — Proibido Mermaid e Proibido ASCII Art — ADR 0008):** Toda aula contém diagramas vetoriais em `<svg>` puro embutidos diretamente no HTML dentro de containers `.visual-diagram-card` (Diagramas de Hasse $D_{12}$, hipercubo $Q_3$, $M_3/N_5$, dígrafos, Stack/Heap, BST/AVL, topologia Borg/Kubernetes). É **estritamente proibido** usar blocos `mermaid`/`flowchart` ou diagramas desenhados em texto ASCII desformatado. Siga a receita de 5 passos de [`docs/adr/0008-proibicao-mermaid-ascii-svg-nativo.md`](docs/adr/0008-proibicao-mermaid-ascii-svg-nativo.md).
2. **Caixas Semânticas Coloridas e Destaques Visuais:**
   - `.callout.philosophy`: Transição ontológica, filosófica e histórica da lógica (borda âmbar `#7c2d12`, fundo `#fff7ed`).
   - `.callout.computation`: Definição canônica formal e aplicação direta em computação/infraestrutura (borda esmeralda `#065f46`, fundo `#f0fdf4`).
   - `.callout.warning` / `.trap-box`: Alertas de armadilhas clássicas e pegadinhas de banca de concurso (borda âmbar `#b45309` ou rosa `#e11d48`, fundo `#fffbeb` ou `#fff1f2`).
   - `.callout.warshall`: Algoritmos e passos matriciais iterativos (borda roxa `#6b21a8`, fundo `#f5f3ff`).
   - Tabelas anatômicas (`.table-wrapper` com `.academic-table`): Largura total, espaçamento confortável e `white-space: nowrap` rigoroso em colunas de conceitos/fórmulas para nunca quebrar termos curtos ao meio.
3. **Pilar Interativo Tátil e Sandboxes (`assets/widgets.js` e `.notebook-cell`):**
   - Micro-laboratórios táteis específicos por degrau cognitivo (`.interactive-card` com controles interativos, matrizes booleanas táteis, visualizador de dígrafo SVG que reage a cliques, simulador de Hasse que remove atalhos).
   - Sandboxes Jupyter no Navegador (`.notebook-cell`) para aulas de código, algoritmos e sistemas (Fases 2, 3 e 4).
4. **Active Retrieval (Retenção Imediata) vs. Banco de Questões de Prova (ADR 0004 & ADR 0009):**
   - **Active Retrieval no final de cada aula (`.quiz-section`):** Mini-quiz de 4 perguntas conceituais com feedback instantâneo (verde para acerto, vermelho para erro), justificativa didática em tempo real explicando o porquê de cada item, e banner de score dinâmico (`.score-banner`). Focado na retenção e compreensão da aula pelo aluno.
   - **Card "Próxima Parada" (`.next-step-card`):** Síntese acolhedora do degrau conquistado e gancho conectivo com o próximo assunto da trilha.
   - **Botão Primário para o Banco de Questões de Concurso:** O rodapé da aula traz o botão de destaque **"Praticar questões desta aula na banca"** (`../questoes.html?topico=<id>`), direcionando para o banco oficial de 64+ questões calibradas no padrão `/gerador-questoes-cfp` para treino cronometrado, algoritmo FSRS v5 e Caderno de Erros.

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
