# ADR 0001: Adoção de Arquitetura Multi-Page Application (MPA) para o Study Hub

- **Status:** Aprovado
- **Data:** 2026-11-22
- **Decisor:** Lucas Galdino (Usuário) & Antigravity (Agente)

---

## Contexto e Problema
O PPGCC IFCE Study Hub será publicado no **GitHub Pages** para estudo pessoal, individual e multiplataforma (desktop, tablet e mobile). O projeto busca a simplicidade operacional máxima, sem dependência de servidores de aplicação (Node/Python) nem etapas complexas de build. Foi necessário decidir entre uma aplicação de página única (SPA com hash routing) e uma aplicação multipáginas (MPA com arquivos HTML distintos).

## Decisão
Adotamos uma arquitetura **Multi-Page Application (MPA)** composta por arquivos HTML semânticos e independentes na raiz e diretórios específicos:
- `index.html` (Visão do Dia / Dashboard Principal)
- `edital.html` (Edital Verticalizado e Progresso por Fases)
- `cronograma.html` (Calendário e Linha do Tempo de Estudos)
- `questoes.html` (Banco de Questões e Treino FSRS)
- `simulados.html` (Simulador Cronometrado Oficial e por Área)
- `arguicao.html` (Banca de Arguição Oral Simulada)
- `curriculo.html` (Auditor de Títulos, Barema Anexo VI e Projeção de Nota Final)
- `lessons/*.html` (Aulas teóricas completas e autônomas)

## Consequências
### Positivas
- **Independência Total e Modularidade:** Cada página possui seu ciclo de vida limpo e claro, facilitando depuração direta via navegador.
- **URLs Canônicas Naturais:** Cada seção possui seu endereço real (`/edital.html`, `/questoes.html`), funcionando diretamente sem necessidade de tratamento especial de rotas 404 no GitHub Pages.
- **Alinhamento com o Padrão `/teach`:** Permite que as aulas em `lessons/*.html` existam como documentos autocontidos e acessíveis diretamente por links padrão.

### Trade-offs e Mitigações
- A navegação entre seções causa recarregamento completo da página. 
- *Mitigação:* Usar cache agressivo dos assets (`style.css`, `widgets.js`, `katex/`), manter dados estáticos em `assets/data.js` e persistir todo o progresso do usuário de forma reativa no `localStorage` por meio de um módulo unificado `assets/store.js`.
