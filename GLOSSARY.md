# GLOSSARY.md — Vocabulário Canônico do PPGCC IFCE Study Hub

Este documento define a terminologia oficial e incontestável utilizada no projeto do **PPGCC IFCE Study Hub**. Todos os documentos, códigos e interfaces devem aderir a estes termos.

---

## 1. Atores e Contexto Institucional

- **Aluno / Candidato:** Lucas Galdino, Analista de Tecnologia da Informação lotado na Diretoria de Gestão da Tecnologia da Informação (DGTI) do Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE). Possui formação de origem em Ciências Humanas e experiência prática consolidada em infraestrutura de TI, demandando nivelamento formal rigoroso ("Zero Base").
- **Banca Examinadora:** Comissão designada para a aplicação da Prova Escrita e realização da Arguição Oral do Edital nº 43/2026 do PPGCC IFCE Campus Fortaleza.
- **PPGCC IFCE:** Programa de Pós-Graduação em Ciência da Computação do IFCE Campus Fortaleza (Mestrado Acadêmico).
- **Linha de Pesquisa Alvo:** Computação Aplicada (CA).
- **Tema CA05:** *"Otimização de recursos computacionais em infraestruturas institucionais baseadas em contêineres"*.
- **Orientador Alvo:** Prof. Dr. Carlos Maurício Jaborandy de Mattos Dourado Junior.

---

## 2. Sistema de Avaliação e Pontuação Oficial

- **$NPE$ (Nota da Prova Escrita):** Pontuação de 0 a 10 obtida na prova objetiva com 20 questões de múltipla escolha (A a E). Possui corte eliminatório estrito: $NPE \ge 3{,}00$. Meta de liderança: $NPE \ge 8{,}50$.
- **$NA$ (Nota da Arguição Oral):** Pontuação de 0 a 10 atribuída pela banca examinadora após defesa oral do pré-projeto, memorial e entrevista técnica. Possui corte eliminatório estrito: $NA \ge 7{,}00$. Meta de liderança: $NA \ge 9{,}20$.
- **$DA$ (Desempenho Acadêmico):** Componente do Anexo VI calculado diretamente a partir do Índice de Rendimento Acadêmico ($IRA$) da graduação, segundo a fórmula oficial da Retificação nº 02:
  $$DA = \min(10, \max(0, IRA - 7{,}0) \times 3{,}34)$$
- **$NC$ (Nota Curricular):** Pontuação final do currículo, obtida pela soma das pontuações dos itens do Anexo VI dividida por 10 (escala de 0 a 10):
  $$NC = \frac{\text{Total Anexo VI}}{10}$$
- **$NF$ (Nota Final):** Média aritmética simples das três notas:
  $$NF = \frac{NPE + NA + NC}{3}$$
  Meta de aprovação em 1º lugar: $NF \ge 8{,}50$.

---

## 3. Pedagogia e Didática de Ensino

- **Zero Base:** Princípio pedagógico inegociável que proíbe assumir qualquer conhecimento prévio ou óbvio por parte do aluno. Todo formalismo, símbolo e algoritmo deve ser fundamentado a partir de intuições concretas e analogias práticas.
- **Tradução Tríplice:** Metodologia de apresentação de conceitos matemáticos e teóricos em três etapas estruturadas:
  1. *Fórmula Simbólica Formal:* Notação exata de concurso e literatura.
  2. *Caixa "Como se Lê":* Pronúncia fonética literal em voz alta da fórmula caractere por caractere.
  3. *Tradução Intuitiva ("Em Bom Português / Analogia Prática"):* Explicação ancorada na rotina de infraestrutura de TI (redes, permissões de arquivos, hierarquia, servidores).
- **Pilar Visual:** Emprego de diagramas vetoriais embutidos em SVG nativo para compreensão de propriedades espaciais, geométricas e estruturais (Diagramas de Hasse, Grafos, Árvores AVL, Topologia Borg/K8s).
- **Pilar Interativo:** Emprego de controles manipuláveis (sliders, matrizes booleanas táteis, seletores de carga) onde a ação do aluno altera o estado em tempo real.
- **Sandbox Jupyter no Navegador:** Componente interativo `.notebook-cell` que simula um terminal/kernel de execução (C99/Python) com inputs paramétricos, console `stdout` colorido e inspetor visual de variáveis e ponteiros de memória.

---

## 4. Arquitetura da Plataforma de Estudos

- **Study Hub:** Aplicação web estática (HTML5, CSS moderno e Vanilla JavaScript), executada 100% offline-first e publicada no GitHub Pages.
- **Visão do Dia ("Hoje"):** Painel central de controle exibindo a tarefa do dia, metas diárias, revisões pendentes no motor FSRS e atalhos rápidos.
- **Edital Verticalizado:** Visualização estruturada dos 37 tópicos divididos nas 5 Fases do edital, com marcação de progresso de estudo e referências bibliográficas.
- **Cronograma:** Visualização temporal e em blocos de planejamento do percurso de estudos até a data da prova.
- **Banco de Questões & Modo Treino:** Ambiente de resolução de questões com filtros por fase/tópico, teclado tátil, gabarito instantâneo e dissecação cirúrgica de distratores.
- **FSRS v5 (Free Spaced Repetition Scheduler):** Algoritmo de repetição espaçada determinística que programa o intervalo ótimo de revisão de cada questão ou tópico conforme as classificações Again, Hard, Good ou Easy.
- **Simulados por Área / Oficial:** Prova cronometrada (20 questões objetivas) com cálculo automático de $NPE$, feedback de corte eliminatório e relatórios por competência.
- **Arguição Oral Simulada:** Roteiro interativo de preparação com as perguntas padrão da banca (Tipo 1: Domínio Técnico do Tema; Tipo 2: Trajetória Profissional e Viabilidade Institucional).
