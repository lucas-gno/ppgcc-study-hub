# HANDOFF.md — Guia de Continuidade entre Sessões e Desktops

> **Propósito:** Permitir que o usuário ou qualquer agente de IA abra este repositório em outro desktop, sem acesso ao histórico de chat anterior, e retome imediatamente a execução exatamente do ponto onde paramos.

---

## 1. Resumo Executivo da Arquitetura (Decisões Travadas)

Todas as escolhas arquiteturais foram resolvidas antes do código e formalizadas em `docs/adr/`:
- **ADR 0001:** Frontend **MPA** (páginas HTML independentes na raiz + `lessons/*.html`).
- **ADR 0002:** Distribuição de dados via `assets/data.js` (`window.PPGCC_DATA`), gerado de `data/mestrado.db` por `scripts/export_db.py`. Funciona via `file:///` e GitHub Pages sem CORS.
- **ADR 0003:** Persistência do usuário em `localStorage` (`ppgcc_study_hub_v1`) via `assets/store.js`, com motor FSRS v5 determinístico e Backup JSON portável (Exportar/Importar).
- **ADR 0004:** Aulas geradas por `scripts/generate_lessons.py` com didática Zero Base + Tradução Tríplice, Pilar Visual (`<svg>` nativo), Pilar Interativo (`assets/widgets.js`), Sandboxes Jupyter (`.notebook-cell` nas Fases 2–4) e **zero questões no corpo da aula** — substituídas no rodapé pelo botão `../questoes.html?topico=<id>`.
- **ADR 0005:** Deploy direto no GitHub Pages a partir da raiz `/` da branch `main` (repositório privado).
- **ADR 0006 & 0007:** Zero emojis na UI; ícones SVG minimalistas `1.5px` em `assets/icons.js`; escala rigorosa de paddings 4px/8px; calendário real do Edital 43/2026 (`04/12/2026` Prova Escrita 120 min; `14/12–18/12/2026` Arguição Oral 20 min); suporte a questões de 4 e 5 alternativas; ingestão integral da Prova Edital 53/2025.

---

## 2. Estado Atual dos Tickets (`.scratch/ppgcc-study-hub/issues/`)

| Ticket | Título | Bloqueadores | Status Atual |
| --- | --- | --- | --- |
| **01** | Fundação de Dados Oficiais, Motor Store e Visão do Dia (`index.html`) | Nenhum | `done` |
| **02** | Edital Verticalizado com Progresso e Bibliografia (`edital.html`) | 01 | `done` |
| **03** | Gerador de Aulas Fase 1 (Visual SVG + Interativo + Link Banco + Molde Sandbox) | 02 | `done` |
| **04** | Banco de Questões, Deep-Link `?topico=` e Modo Treino FSRS (`questoes.html`) | 01 | `done` |
| **05** | Simulados Cronometrados (Oficial 120 min e Por Área) (`simulados.html`) | 01, 04 | `ready-for-agent` |
| **06** | Cronograma Real de Dois Sprints (`cronograma.html`) | 01, 02 | `ready-for-agent` |
| **07** | Simulador de Arguição Oral CA05 (`arguicao.html`) | 01 | `ready-for-agent` |
| **08** | Auditoria Curricular Anexo VI, Projeção NF (`curriculo.html`) e Deploy GitHub Pages | 01, 05, 07 | `blocked` |

**Fronteira atual de trabalho:** Tickets **05**, **06** e **07** têm todos os seus bloqueadores concluídos (`ready-for-agent`) e podem ser executados imediatamente.

---

## 3. O que Já Está Funcionando e Verificado

- **Dados (`data/mestrado.db` -> `assets/data.js`):** 5 fases com peso real (55% AED, 25% Prog, 20% Lógica), 37 tópicos, 7 obras bibliográficas, 6 perguntas estratégicas de arguição e 64 questões totais (40 inéditas Fase 1 + 20 oficiais do Edital 53/2025 + 4 complementares).
- **Motor (`assets/store.js`):** Fórmulas oficiais ($NPE$, $DA$, $NC$, $NF$, cortes), FSRS v5 determinístico, Sprints reais (`23/11–03/12` e `05/12–13/12`), filtros combinados e Backup JSON com validação.
- **Páginas prontas na raiz:** `index.html`, `edital.html`, `questoes.html`.
- **Aulas Fase 1 prontas (`lessons/`):** `0001-teoria-dos-conjuntos.html` a `0008-diagramas-de-hasse.html` (SVG nativo + widgets `assets/widgets.js` sem emojis + KaTeX local + rodapé linkado a `../questoes.html?topico=<id>`).
- **Molde Sandbox Jupyter (`.notebook-cell`):** `render_notebook_sandbox_shell` implementado e testado em `scripts/generate_lessons.py` para uso nas próximas fases (2, 3 e 4).

---

## 4. Costuras de Teste (TDD Seams) e Última Verificação

Nenhum pacote externo (`pip` ou `npm`) é necessário:
- **Seam A (Pipeline Python) & Seam C (Contratos HTML/Aulas):**
  ```powershell
  python -m unittest discover -s tests -v
  ```
  *Última execução (2026-11-22): 7/7 testes verdes (`OK`).*
- **Seam B (Domínio JS — Fórmulas, FSRS v5, Filtros, Sprints, Backup):**
  ```powershell
  node --test tests/*.test.mjs
  ```
  *Última execução (2026-11-22): 7/7 testes verdes (`pass 7, fail 0`).*

---

## 5. Prompt de Retomada para Outro Desktop / Novo Agente

Caso continue em outra máquina sem este histórico, cole o texto abaixo no novo chat:

```text
Leia AGENTS.md, GLOSSARY.md, docs/HANDOFF.md, docs/BANCA_E_EDITAL_2027.md e os arquivos em docs/adr/ e .scratch/ppgcc-study-hub/issues/.
Execute as suítes `python -m unittest discover -s tests -v` e `node --test tests/*.test.mjs` para verificar o estado atual.
Os Tickets 01 a 04 (Fundação, Edital, Aulas Fase 1 e Banco de Questões) já estão concluídos. Assuma os próximos tickets na fronteira (05, 06 e 07 em .scratch/ppgcc-study-hub/issues/) respeitando estritamente TDD (Red -> Green), zero emojis, ícones SVG minimalistas (assets/icons.js), Visual + Interativo + .notebook-cell (NOTES.md) e zero questões inline nas aulas.
```

---

## 6. Repositório Remoto e Hospedagem

- **Repositório Público:** `https://github.com/lucas-gno/ppgcc-study-hub` (`git@github.com:lucas-gno/ppgcc-study-hub.git`)
- **Branch principal:** `main` (inclui `.nojekyll`, `data/mestrado.db` e `scripts/deploy.ps1`)
- **Clonagem em outro desktop:**
  ```bash
  git clone git@github.com:lucas-gno/ppgcc-study-hub.git
  ```
- **GitHub Pages Ativo:** `https://lucas-gno.github.io/ppgcc-study-hub/` (branch `main`, pasta `/`, HTTPS forçado).
