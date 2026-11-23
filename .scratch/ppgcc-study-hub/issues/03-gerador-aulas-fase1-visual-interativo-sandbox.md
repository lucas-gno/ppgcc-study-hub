# 03: Gerador de Aulas Estáticas (Fase 1: Visual SVG + Interativo + Deep-Link de Questões + Molde Sandbox)

**What to build:** O aluno abre qualquer uma das 8 aulas da Fase 1 em HTML estático autocontido, estuda o conteúdo no padrão Zero Base com Tradução Tríplice (Fórmula Simbólica, Caixa Como se Lê fonética e Analogia Prática de TI) e matemática KaTeX local, explora diagramas vetoriais SVG nativos (Pilar Visual) e manipula controles interativos em tempo real (Pilar Interativo) sem nenhuma questão de múltipla escolha poluindo o corpo da aula. Ao terminar a leitura, marca a aula como concluída no rodapé e clica em "Praticar questões desta aula" para abrir o Banco de Questões já filtrado para aquele tópico. O gerador também disponibiliza o molde estrutural validado de Sandboxes Jupyter no Navegador (`.notebook-cell`) sem emojis para as Fases 2, 3 e 4.

**Blocked by:** 02: Edital Verticalizado com Progresso Persistente e Bibliografia Oficial

**Status:** done

- [x] Gera todas as 8 aulas da Fase 1 (tópicos 1 a 8) em HTML offline com KaTeX local e blocos de Tradução Tríplice preservando fórmulas intactas.
- [x] Cada aula embute ao menos um diagrama vetorial `<svg>` nativo e instancia um manipulador interativo em tempo real conectado aos motores de widgets.
- [x] Nenhuma aula contém questões inline; o rodapé traz botão de conclusão sincronizado com o `Store` e link filtrado para praticar as questões daquele tópico no Banco de Questões.
- [x] O componente de Sandbox Jupyter no Navegador e os widgets compartilhados estão livres de emojis e prontos para uso nas Fases 2, 3 e 4.
- [x] Todos os diagramas Mermaid quebrados e diagramas ASCII das aulas 1 a 8 foram substituídos por 16 componentes vetoriais nativos em `<svg>` dentro de `.visual-diagram-card` com zero emojis.
