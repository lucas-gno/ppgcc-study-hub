# 08: Auditoria Curricular Anexo VI, Projeção NF e Publicação GitHub Pages

**What to build:** O aluno audita sua pontuação curricular oficial na página de Currículo usando o slider interativo de IRA (que aplica `DA = min(10, max(0, IRA - 7) * 3.34)`) e os campos dos demais critérios do Anexo VI respeitando tetos individuais e janela 2023-2026, obtém `NC = Total / 10` conforme a Retificação nº 02, simula cenários de Nota Final `NF = (NPE + NA + NC) / 3` comparados às notas reais do Edital 53/2025 e conclui a configuração Git (branch `main`, `.gitignore` e script de deploy) pronta para o repositório privado no GitHub Pages.

**Blocked by:** 01: Fundação de Dados Oficiais, Motor Store e Visão do Dia, 05: Simulados Cronometrados (Oficial 120 min e Por Área), 07: Simulador de Arguição Oral (CA05 — Ficha 5+5 e Cronômetro 20 min)

**Status:** cancelled-by-user (descartado pelo usuario: curriculo fica a cargo da banca)

- [ ] Calcula e persiste `DA`, pontuação limitada do Anexo VI, `NC` e projeção de `NF` exatamente conforme fórmulas oficiais e Retificação nº 02.
- [ ] Compara a projeção de `NF` com os patamares reais do resultado final do Edital 53/2025 e envia `NC`/`NF` para a Visão do Dia.
- [ ] Repositório Git local configurado na branch `main` com `.gitignore` adequado e script de publicação validado para GitHub Pages na raiz.
- [ ] Zero emojis, ícones SVG minimalistas e zero CDNs externas.
