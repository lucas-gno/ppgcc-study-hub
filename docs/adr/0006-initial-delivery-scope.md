# ADR 0006: Escopo da Primeira Entrega — Fundação Completa e Fase 1 Integral

- **Status:** Aprovado
- **Data:** 2026-11-22
- **Decisor:** Lucas Galdino (Usuário) & Antigravity (Agente)

---

## Contexto e Problema
Precisávamos definir o escopo de implementação inicial: se faríamos uma entrega fatiada (apenas navegação básica e uma ou duas páginas) ou a fundação integral da plataforma com todas as ferramentas de estudo e o primeiro bloco de conteúdo pronto para uso real.

## Decisão
Implementaremos a **Fundação Completa do Hub** contendo:
1. Todas as 7 páginas mestras estruturadas (`index.html`, `edital.html`, `cronograma.html`, `questoes.html`, `simulados.html`, `arguicao.html`, `curriculo.html`).
2. Script de exportação `scripts/export_db.py` gerando `assets/data.js` a partir do `data/mestrado.db`.
3. Módulo de persistência `assets/store.js` com motor FSRS v5 e backup JSON.
4. Script gerador de aulas `scripts/generate_lessons.py` compilando as 8 aulas da Fase 1 para `lessons/0001-*.html` a `lessons/0008-*.html`.
5. Inicialização do repositório Git local e instruções/scripts para vinculação ao repositório remoto privado no GitHub e ativação do GitHub Pages.

## Consequências
### Positivas
- Entrega uma ferramenta de estudo viva e 100% funcional desde o primeiro dia.
- O aluno já pode utilizar imediatamente a rotina diária, responder questões de Lógica com repetição espaçada, testar simulados e revisar a Fase 1.
- Estabelece os alicerces definitivos para a expansão rápida das Fases 2, 3, 4 e 5.
