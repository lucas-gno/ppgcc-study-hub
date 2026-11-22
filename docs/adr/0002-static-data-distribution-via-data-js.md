# ADR 0002: Distribuição de Dados Estáticos via Script Universal (assets/data.js)

- **Status:** Aprovado
- **Data:** 2026-11-22
- **Decisor:** Lucas Galdino (Usuário) & Antigravity (Agente)

---

## Contexto e Problema
O PPGCC IFCE Study Hub precisa funcionar tanto publicado no **GitHub Pages** quanto no sistema de arquivos local sem qualquer servidor web ativo (duplo clique no arquivo HTML no Windows/macOS/Linux/Android, sob protocolo `file:///`). Navegadores modernos impõem restrições de CORS estritas a requisições `fetch()` assíncronas em arquivos locais, o que impediria a leitura direta de arquivos `.json`.

## Decisão
Os dados do banco SQLite local (`data/mestrado.db`) contendo tópicos do edital, fases, questões, gabaritos, cronograma e bibliografia serão compilados por um script Python utilitário (`scripts/export_db.py`) em um arquivo JavaScript estático universal:
`assets/data.js`

Este arquivo expõe um objeto global imutável:
`window.PPGCC_DATA = { fases, topicos, questoes, cronograma, obras, perfil_curriculo }`

Todas as páginas HTML da aplicação MPA incluem este script antes de seus respectivos scripts de controle.

## Consequências
### Positivas
- **Compatibilidade Absoluta Offline & `file:///`:** Permite abrir e utilizar a plataforma completa sem depender de servidor HTTP, sem travas de CORS e sem necessidade de conexão com a internet.
- **Carregamento Instantâneo:** Elimina latências de requisições de rede, proporcionando uma experiência de usuário ultra-responsiva alinhada aos princípios de `/emil-design-eng`.
- **Fonte Única da Verdade:** O banco SQLite `data/mestrado.db` permanece como a fonte primária, sendo facilmente exportado a qualquer momento para atualizar a plataforma estática.

### Trade-offs e Mitigações
- Requer a execução de um script simples (`python scripts/export_db.py`) sempre que novos dados estruturados forem adicionados ao SQLite.
- *Mitigação:* O script será automatizado e integrado ao fluxo de atualização de aulas e deploy.
