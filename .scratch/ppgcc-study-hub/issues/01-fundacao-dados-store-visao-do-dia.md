# 01: Fundação de Dados Oficiais, Motor Store e Visão do Dia

**What to build:** O aluno abre a Visão do Dia diretamente no navegador (via protocolo local ou GitHub Pages), enxerga a contagem regressiva real para a Prova Escrita (`04/12/2026`, 120 minutos) e para a Arguição Oral (`14/12/2026`), navega por uma barra minimalista sem emojis com ícones SVG padronizados, acompanha o bloco prioritário de estudo do Sprint atual e a fila de revisões FSRS pendentes, além de poder exportar, importar ou restaurar seu progresso em JSON. Por trás, a base estática offline passa a incorporar as 20 questões oficiais da Prova Edital 53/2025 junto aos 37 tópicos e metas oficiais.

**Blocked by:** None (can start immediately)

**Status:** done

- [x] As 20 questões reais do Edital 53/2025 são ingeridas de forma idempotente no banco e exportadas com o gabarito literal oficial e suporte a itens de 4 e 5 alternativas.
- [x] O arquivo estático universal de dados carrega todos os 37 tópicos, 5 fases, 7 obras e 60+ questões sem depender de servidor HTTP ou rede.
- [x] O motor de estado calcula com exatidão determinística as fórmulas oficiais do edital (`NPE`, `DA`, `NC`, `NF`, cortes eliminatórios), agenda cards via FSRS v5, calcula o cronograma de Sprints reais e faz round-trip validado de Backup JSON no `localStorage`.
- [x] A Visão do Dia e a barra de navegação unificada usam exclusivamente ícones SVG minimalistas (zero emojis), respeitam escala de paddings 4px/8px e zero CDNs externas.
