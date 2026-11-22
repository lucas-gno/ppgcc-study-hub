# 04: Banco de Questões, Filtro por Deep-Link e Modo Treino FSRS v5

**What to build:** O aluno abre o Banco de Questões (diretamente ou pelo botão ao final de uma aula), vê a tela de prontidão já filtrada conforme query params (`?topico=`, `?fase=`, `?origem=`, `?modo=`) com banner contextual e link de retorno para a aula de origem, combina filtros de Fase, Tópico, Origem (Banca Oficial 53/2025 vs. Inéditas) e Modo (Todas, Não Resolvidas, Revisões FSRS, Caderno de Erros, Favoritas), entra no Modo Treino, responde questões de 4 ou 5 alternativas usando mouse ou teclado instantâneo sem atrasos de animação (`A`-`E`, `Enter`, `1`-`4` para FSRS), lê a dissecação cirúrgica de cada distrator e tem as revisões futuras agendadas pelo algoritmo FSRS v5.

**Blocked by:** 01: Fundação de Dados Oficiais, Motor Store e Visão do Dia

**Status:** done

- [x] Lê query strings na inicialização e aplica filtros combinados exibindo contagem exata de questões compatíveis na tela de prontidão.
- [x] Renderiza dinamicamente 4 alternativas (`A`-`D`) ou 5 alternativas (`A`-`E`) sem botões vazios, com feedback imediato de acerto/erro e justificativa detalhada dos distratores.
- [x] Atalhos de teclado (`A`-`E`, `Enter`, `1`-`4`) operam sem animações bloqueantes e atualizam o agendamento FSRS, caderno de erros e favoritas no `Store`.
- [x] Zero emojis, zero CDNs externas e resumo de sessão conectado às métricas da Visão do Dia.
