# ADR 0007: Linguagem Visual Minimalista (Zero Emojis), Calibração de Cronograma Real e Banco Oficial da Banca

- **Status:** Aprovado
- **Data:** 2026-11-22
- **Decisor:** Lucas Galdino (Usuário) & Antigravity (Agente)

---

## Contexto e Problema
1. O uso de emojis na interface viola a estética minimalista de design engineering (Apple HIG + Emil Kowalski) e introduz ruído visual em um ambiente de estudo técnico focado.
2. O banco legado `data/mestrado.db` continha 44 linhas em `cronograma_diario` distribuídas entre `2026-11-02` e `2026-11-27`, o que não corresponde às datas reais retificadas do Edital nº 43/2026.
3. A prova escrita oficial do PPGCC IFCE (Edital nº 53/2025) possui 20 questões objetivas com duração total de 2 horas (120 minutos) e combina questões de 4 alternativas (`a`–`d`) e 5 alternativas (`a`–`e`).

## Decisão
1. **Zero Emojis e Iconografia Minimalista:** É estritamente proibido utilizar emojis em qualquer texto ou componente da interface (navegação, botões, títulos, badges, alertas, estados vazios ou documentos gerados). Todos os ícones serão SVGs vetoriais inline monocromáticos (`viewBox="0 0 24 24"`, `stroke="currentColor"`, `stroke-width="1.5"`), centralizados em `assets/icons.js`, com escala estrita de paddings e espaçamentos (base 4px/8px).
2. **Calendário Oficial Calibrado (Edital 43/2026 + Retificação nº 01 e nº 02):**
   - Data de referência atual: `22/11/2026`.
   - **Etapa 1 — Prova Escrita Presencial:** **`04/12/2026` (sexta-feira)** (alterada de `05/12/2026` pela Retificação nº 01), duração oficial de **120 minutos (2 horas)**, 20 questões objetivas (0,5 pt cada), corte eliminatório $NPE \ge 3{,}00$. Restam **12 dias corridos** (11 dias úteis até `03/12/2026`).
   - **Etapa 2 — Arguição Oral Presencial:** **`14/12/2026` a `18/12/2026`**, duração máxima de **20 minutos**, 6 perguntas (3 Tipo 1 teóricas do tema CA05 + 3 Tipo 2 sobre currículo/experiência), corte eliminatório $NA \ge 7{,}00$ (**9 dias dedicados** de `05/12` a `13/12/2026`).
   - **Etapa 3 — Avaliação Curricular (Anexo VI + Retificação nº 02):** `14/12/2026` a `18/12/2026`, com $DA = \min(10, \max(0, IRA - 7{,}0) \times 3{,}34)$ e $NC = \text{Total Anexo VI} / 10$.
   - O cronograma será estruturado em **Sprint 1 (23/11 a 03/12/2026 — Prova Escrita, ponderado pelo peso real da banca: 55% AED, 25% Programação C/Python, 20% Lógica)** e **Sprint 2 (05/12 a 13/12/2026 — Arguição Oral CA05 e Defesa DGTI)**, permitindo ajuste flexível de ritmo pelo usuário.
3. **Ingestão Integral da Prova 53/2025 e Suporte a 4/5 Alternativas:** As 20 questões oficiais do Edital nº 53/2025 serão incorporadas ao banco com o gabarito oficial (`B B C B B C E A A D / B C C A C B D B B C`) e justificativas fundamentadas nos pareceres oficiais de recursos da comissão examinadora, com suporte dinâmico para itens de 4 e 5 alternativas no Banco de Questões e nos Simulados.

## Consequências
### Positivas
- Interface visualmente serena, precisa e livre de ruído visual.
- Cronograma alinhado com exatidão às datas oficiais retificadas e à urgência real de preparação.
- Simulados fiéis ao tempo oficial de 120 minutos e ao estilo rigoroso da banca do PPGCC IFCE.
