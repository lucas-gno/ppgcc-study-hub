# Dossiê de Inteligência: Banca PPGCC IFCE e Edital nº 43/2026 (Turma 2027.1)

Este documento consolida todos os fatos verificados nos arquivos oficiais (`data/edital/`, `data/provas_anteriores/`) e no portal oficial do programa (`https://ppgcc.ifce.edu.br/` e `https://portal.ifce.edu.br/`), servindo de base permanente para qualquer agente que trabalhe no **PPGCC IFCE Study Hub**.

---

## 1. Edital nº 43/2026, Retificações e Cronograma Oficial

- **Programa:** Mestrado Acadêmico em Ciência da Computação — IFCE Campus Fortaleza (CAPES, 360h de disciplinas, regime diurno, dedicação mínima 20h/semana).
- **Vagas Totais:** 35 (24 Ampla Concorrência, 7 PPI, 4 PCD).
- **Tema Alvo:** **CA05** — *"Otimização de recursos computacionais em infraestruturas institucionais baseadas em contêineres"* (Linha: Computação Aplicada, **1 vaga**, Proponente: **Prof. Dr. Carlos Maurício Jaborandy de Mattos Dourado Júnior**).
- **Retificação nº 01 (28/10/2026):** Deferida a Impugnação nº 01 (liberdade de crença religiosa, art. 5º, VIII, CF), alterando a realização da Prova Escrita Presencial de `05/12/2026 (sábado)` para **`04/12/2026 (sexta-feira)`**.
- **Retificação nº 02 (29/10/2026):** Define explicitamente $NC = \text{Pontuação Total Anexo VI} / 10$, resultando em nota de `0` a `10`.

### Cronograma Oficial Vigente (a partir de 22/11/2026)

| Etapa / Evento | Data Oficial | Observação Operacional |
| --- | --- | --- |
| Lista preliminar das inscrições | `24/11/2026` | Recurso em `25/11/2026`; resposta em `26/11/2026` |
| Lista final das inscrições e local/horário da prova | `27/11/2026` | Publicação no portal do IFCE |
| **Etapa 1 — Prova Escrita Presencial ($NPE$)** | **`04/12/2026` (sexta)** | **20 questões objetivas**, 0,5 pt cada, **120 min (2 horas)**, corte $NPE \ge 3{,}00$ |
| Resultado preliminar e recursos da Prova Escrita | `09/12` e `10/12/2026` | Recursos das 7h30 às 23h59 para `selecao@ppgcc.ifce.edu.br` |
| Resultado final da Prova Escrita + Calendário Oral | `11/12/2026` | Divulgação da escala individual de arguição |
| **Etapa 2 — Arguição Oral Presencial ($NA$)** | **`14/12` a `18/12/2026`** | **Máximo 20 minutos**, **6 perguntas** (3 Tipo 1 + 3 Tipo 2), corte $NA \ge 7{,}00$ |
| **Etapa 3 — Avaliação Curricular ($NC$)** | **`14/12` a `18/12/2026`** | Análise de Anexo VI e histórico da graduação (itens 2023–2026) |
| Resultados da Arguição Oral | `04/01` a `08/01/2027` | Preliminar `04/01`, recurso `05/01`, final `08/01` |
| Resultados do Currículo e Parcial Geral | `18/01` a `20/01/2027` | Preliminar `18/01`, recurso `19/01`, parcial `20/01` |

### Logística de Prova (referência Comunicado Edital 53/2025)
- Local adotado na edição anterior: Campus Fortaleza do IFCE (Av. Treze de Maio, 2081), **Auditório da Pós-Graduação** (Bloco Didático, 2º andar, sobre o estacionamento coberto).
- Horário padrão: **09h00 às 11h00** (fechamento rigoroso das portas às 09h00; chegada recomendada com 1h de antecedência e documento oficial com foto).

---

## 2. Fórmulas Matemáticas Oficiais

- **Prova Escrita ($NPE$):**
  $$NPE = 0{,}5 \times \text{acertos} \quad (NPE \in [0, 10],\ \text{eliminatório se } NPE < 3{,}00)$$
- **Arguição Oral ($NA$):**
  - 6 perguntas com igual peso divididas conforme ficha oficial revelada no parecer de recurso do Edital 53/2025: **5 pontos para Tipo 1** (fundamentos teóricos/conceituais da linha e tema) + **5 pontos para Tipo 2** (currículo e experiências profissionais/pesquisa).
  - Critérios do subitem 4.4.2: (a) comunicação clara e objetiva, (b) expressão do domínio do conteúdo, (c) relação entre experiência e linha de pesquisa. Eliminatório se $NA < 7{,}00$.
- **Avaliação Curricular ($NC$ — Anexo VI + Retificação nº 02):**
  $$DA = \min\big(10,\ \max(0,\ IRA - 7{,}0) \times 3{,}34\big)$$
  $$\text{Total Anexo VI} = \min(30, 15 \cdot Q_{\text{Qualis A/B}}) + \min(30, 10 \cdot Q_{\text{Sem Qualis}}) + \min(30, 10 \cdot \text{AnosPesq}_{2023\text{–}2026}) + DA$$
  $$NC = \frac{\text{Total Anexo VI}}{10}$$
- **Nota Final ($NF$) e Desempate:**
  $$NF = \frac{NPE + NA + NC}{3}$$
  Ordem de desempate: (1) maior idade em dias, (2) maior $NPE$, (3) maior $NC$.

---

## 3. Perfil Técnico da Comissão Examinadora (Portaria nº 7234/2026 + `ppgcc.ifce.edu.br/quem-e-quem`)

| Docente | Função na Banca | Linha / Áreas Oficiais no PPGCC | Impacto Direto na Prova e Recursos |
| --- | --- | --- | --- |
| **Saulo Anderson Freitas de Oliveira** | Presidente (Vice-Coordenador do PPGCC) | IA — **Linguagens de Programação**, **Computabilidade**, Processamento de Sinais Biológicos | Autoridade por trás de testes de mesa em C, coerção de tipos (`int` vs `float`), recursão e análise assintótica. Assinou todos os indeferimentos de recurso da prova 53/2025 por rigor literal. |
| **Thiago Alves Rocha** | Vice-Presidente | IA — **Representação do Conhecimento**, **Raciocínio Automatizado**, Inteligência Artificial | Eixo de lógica formal, teoria dos conjuntos, relações binárias, propriedades, equivalência e ordens. |
| **Corneli Gomes Furtado Júnior** | Membro | RCSD — Segurança de Redes, Teleinformática, EaD | Visão de sistemas e redes. |
| **Róger Moura Sarmento** | Membro Colaborador | IA — Processamento Digital de Imagens, Aprendizado de Máquina | Apoio na elaboração e aplicação. |
| **Carlos Maurício Jaborandy de Mattos Dourado Júnior** | Orientador Alvo (Tema CA05) | Docente Permanente — **Redes de Computadores**, **Teleinformática**, **Multimídia via Web** | Avaliador principal da Arguição Oral no tema CA05. |

---

## 4. Radiografia das Provas Anteriores (Editais 53/2025, 20/2024 e 43/2023)

### Distribuição Real da Prova Edital nº 53/2025 (20 questões em 120 min = 6 min/questão)
Gabarito Oficial (`02/12/2025`): **`B B C B B C E A A D` | `B C C A C B D B B C`**.

1. **Algoritmos e Estruturas de Dados — 55% (11 questões):**
   - Complexidade assintótica e análise de pseudocódigo: Q1 (`Boo`, laço interno de metades $\Theta(n)$), Q2 (`Bar`, busca binária $\Theta(\log n)$), Q3 (`Bus`, jump search com passo crescente $\Theta(\sqrt{n})$), Q6 (laço triangular $\Theta(n^2)$), Q12 (métrica de eficiência = número de operações chave).
   - Estruturas lineares e TADs: Q4 (pilha `push/pop`), Q5 (lista simplesmente encadeada sem ponteiro de cauda: acesso $O(n)$, inserção início $O(1)$, remoção fim $O(n)$), Q8 (fila `enqueue/dequeue`), Q11 (operação mais custosa em lista simples sem cauda = inserir no fim), Q15 (classificação literal de deque de acesso restrito, lista simples, pilha ligada e fila sobre buffer circular).
   - Ordenação: Q16 (pior caso do QuickSort $O(n^2)$).
2. **Programação Computacional (C e Python) — 25% (5 questões):**
   - Q9 (recorrência em Python `2*f(n-1) + f(n-2)` $\to$ `99`).
   - Q10 (divisão inteira vs. cast `(float)b` em C $\to$ `3.0` e `3.333...`).
   - Q13 (teste de mesa em C com `for` e `while` aninhados $\to$ `i: 15 j: 1 k: 0`).
   - Q14 (mecanismo contra acesso a endereço de memória inexistente $\to$ Tratamento de Exceções).
   - Q20 (rastreamento recursivo de máximo em vetor indexado em 1).
3. **Lógica Matemática e Teoria dos Conjuntos — 20% (4 questões):**
   - Q7 (relação em $\{1,2,3\}$ reflexiva, não simétrica e transitiva).
   - Q17 (contagem de relações binárias em $A=\{0,1\}$: $2^{|A|^2} = 16$).
   - Q18 ($|x|=|y|$ em $\mathbb{R}$ é relação de equivalência).
   - Q19 (identificar qual relação binária não representa função).

### Padrões Críticos da Banca
- **Alternativas variáveis (4 ou 5 opções):** Na Prova 53/2025, Q1–Q4 e Q16–Q20 possuem 4 alternativas (`a`–`d`); Q5–Q15 possuem 5 alternativas (`a`–`e`).
- **Reincidência direta estilo POSCOMP:** Questões idênticas ou variações diretas se repetem entre edições (Q14 e Q19 de 53/2025 também apareceram no Edital 20/2024; em 20/2024 caíram ainda máximo em vetor ordenado $O(1)$ e definição de matrizes esparsas).
- **Rigor semântico nos pareceres de recurso (`Resp_Recursos_Prova_Edital_53.2025_texto.txt`):**
  - Q10 indeferida: a banca exige leitura exata da especificação da linguagem C (`3.333...` indica natureza não exata em ponto flutuante, sem arredondamento).
  - Q15 indeferida: a banca rejeitou "deque" genérico e "fila circular" por não expressarem as restrições literais dos itens 1 e 4, validando exclusivamente "deque de acesso restrito" e "fila implementada sobre buffer circular".
- **Notas reais do Edital 53/2025:**
  - Prova Escrita na linha CA (`CA01`, 11 presentes): $NPE$ entre `3,0` e `8,5`, mediana `5,5`; maior $NPE$ geral `9,5` (PDI02).
  - Nota Final na linha CA (`CA01`): `4,13` a `6,17`; maior $NF$ geral `8,83` (PDI02).
- **Status de arquivos históricos (2022–2024):** Os links das páginas antigas em `ppgcc.ifce.edu.br/informacoes-academicas/processos-seletivos/processo-seletivo-turma-2025-1`, `2024-1` e `2023-1` apontam para o legado `ifce.edu.br/acesso-rapido/...` (hoje redirecionado para a home do novo portal), e o Wayback Machine salvou apenas páginas HTML `/view` sem os binários PDF de prova (`404`).

---

## 5. Tema CA05 — Projeto e Bibliografia Obrigatória (Anexo I, págs. 8–10)

- **Objeto da Pesquisa:** Desenvolver e avaliar um método de alocação adaptativa de CPU e memória para aplicações institucionais em contêineres sob infraestrutura com capacidade limitada, mitigando superdimensionamento sem violar SLOs/SLAs.
- **Métricas de Comparação Experimental:** Configurações estáticas vs. método proposto vs. estratégia dinâmica de referência quanto a utilização de CPU/memória, tempo de resposta, vazão, violações de requisitos de desempenho e sobrecarga de gerenciamento.
- **Referências Obrigatórias do Edital:**
  1. VERMA, Abhishek et al. *Large-scale cluster management at Google with Borg*. EuroSys '15, ACM, 2015.
  2. RZADCA, Krzysztof et al. *Autopilot: workload autoscaling at Google*. EuroSys '20, ACM, 2020.
  3. KUBERNETES. *Resource Management for Pods and Containers*. Documentação Oficial.
