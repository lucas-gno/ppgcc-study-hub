# PPGCC IFCE Study Hub (Turma 2027.1 — Tema CA05)

Plataforma pessoal, 100% estática, offline-first e sem dependências de servidor para preparação ao processo seletivo do **Mestrado Acadêmico em Ciência da Computação (PPGCC — IFCE Campus Fortaleza)**, Edital nº 43/2026 (Retificações nº 01 e nº 02).

- **Linha de Pesquisa:** Computação Aplicada (CA)
- **Tema:** CA05 — *Otimização de recursos computacionais em infraestruturas institucionais baseadas em contêineres*
- **Orientador Alvo:** Prof. Dr. Carlos Maurício Jaborandy de Mattos Dourado Júnior
- **Datas Oficiais:** Prova Escrita em **04/12/2026** (120 min, 20 questões) | Arguição Oral entre **14/12/2026 e 18/12/2026** (máx. 20 min)

---

## 1. Arquitetura e Uso (GitHub Pages & `file:///`)

A plataforma adota arquitetura **Multi-Page Application (MPA)** em HTML5, CSS e Vanilla JS, sem build steps, sem bundlers, sem backend e sem CDNs externas (KaTeX servido localmente em `assets/katex/`):

- **`index.html`** — Visão do Dia (contagem regressiva real, foco do Sprint, fila FSRS, KPIs e projeção $NF$)
- **`edital.html`** — Edital Verticalizado (37 tópicos em 5 fases, pesos reais da banca e bibliografia oficial)
- **`cronograma.html`** — Cronograma de dois Sprints calibrado para 04/12 e 14/12
- **`questoes.html`** — Banco de Questões (60+ questões incluindo Prova Oficial 53/2025), filtros via query string (`?topico=`) e Modo Treino FSRS v5
- **`simulados.html`** — Simulado Oficial cronometrado de 120 minutos e baterias por área
- **`arguicao.html`** — Simulador de Arguição Oral (20 min, rubrica oficial 5+5)
- **`curriculo.html`** — Auditoria Curricular (Anexo VI, cálculo de $DA$ pelo IRA, $NC$ e $NF$)
- **`lessons/*.html`** — Aulas teóricas estáticas geradas com didática Zero Base, diagramas `<svg>`, widgets interativos, sandboxes `.notebook-cell` e link direto para o Banco de Questões

Para usar localmente, basta abrir `index.html` diretamente no navegador (protocolo `file:///`) ou servir a raiz via GitHub Pages (branch `main`, pasta `/`).

---

## 2. Comandos de Construção de Dados e Testes

Pré-requisitos: **Python 3.12+** e **Node.js 20+** (testado em Node v24), sem necessidade de `pip install` ou `npm install`.

```powershell
# 1. Ingerir as 20 questões oficiais do Edital 53/2025 no SQLite (idempotente)
python scripts/import_official_2025.py

# 2. Exportar banco e metadados oficiais para assets/data.js
python scripts/export_db.py

# 3. Gerar/atualizar páginas estáticas de aulas em lessons/*.html
python scripts/generate_lessons.py

# 4. Executar todos os testes automatizados (TDD)
python -m unittest discover -s tests -v
node --test tests/*.test.mjs
```

---

## 3. Mapa de Documentação e Continuidade

Para qualquer novo agente ou sessão em outro computador, consulte na ordem abaixo:

1. [`docs/HANDOFF.md`](docs/HANDOFF.md) — Estado vivo do projeto, tickets concluídos e próximo ticket da fronteira
2. [`AGENTS.md`](AGENTS.md) — Regras operacionais, pedagógicas e de design
3. [`GLOSSARY.md`](GLOSSARY.md) — Vocabulário canônico do domínio
4. [`docs/BANCA_E_EDITAL_2027.md`](docs/BANCA_E_EDITAL_2027.md) — Dossiê da banca examinadora e raio-x das provas anteriores
5. [`docs/adr/`](docs/adr/) — Registros de Decisões Arquiteturais (ADRs 0001 a 0007)
6. [`.scratch/ppgcc-study-hub/issues/`](.scratch/ppgcc-study-hub/issues/) — Backlog completo em fatias verticais (`/to-tickets`)
