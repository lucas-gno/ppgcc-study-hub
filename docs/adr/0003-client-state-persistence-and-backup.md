# ADR 0003: Persistência de Progresso do Aluno via store.js com Backup JSON Portável

- **Status:** Aprovado
- **Data:** 2026-11-22
- **Decisor:** Lucas Galdino (Usuário) & Antigravity (Agente)

---

## Contexto e Problema
Por se tratar de uma aplicação 100% estática sem backend autenticado ou banco de dados em nuvem, o progresso individual de estudo do aluno (tópicos lidos, histórico de resoluções no banco de questões, cálculo de intervalos FSRS, sessões de simulados e dados curriculares) reside no cliente. É imprescindível garantir que esses dados não sejam perdidos por limpezas de cache acidentais e que o aluno possa alternar entre estudar no computador, no tablet ou no celular.

## Decisão
Criaremos um módulo unificado de persistência:
`assets/store.js`

Este módulo:
1. Centraliza todas as operações de leitura e escrita sob chaves estruturadas no `localStorage` (ex.: `ppgcc_progress_v1`).
2. Implementa o algoritmo **FSRS v5 determinístico** no lado do cliente para calcular e agendar as revisões de questões.
3. Fornece uma interface global de exportação e importação de estado via arquivos compactos `JSON` (`ppgcc-backup-YYYY-MM-DD.json`), acessível através de um modal minimalista no cabeçalho comum das páginas.
4. Inclui validação de integridade do payload de importação para evitar corrupção de estado.

## Consequências
### Positivas
- **Portabilidade Total:** O aluno pode estudar no desktop, exportar o JSON, enviá-lo para o celular ou tablet e continuar instantaneamente de onde parou.
- **Privacidade e Independência:** Nenhum dado pessoal trafega para servidores de terceiros ou nuvens externas.
- **Desacoplamento de UI:** As páginas MPA consom uma API padronizada (`Store.getTopicStatus()`, `Store.saveQuestionAnswer()`, `Store.getFsrsCards()`, etc.) sem se preocupar com detalhes do armazenamento.
