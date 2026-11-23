# ADR 0009: Padrão Didático de Excelência (Princípio de Einstein), Degraus Cognitivos, Paleta Visual Semântica e Active Retrieval

- **Status:** Aprovado
- **Data:** 2026-11-23
- **Decisor:** Lucas Galdino (Usuário) & Antigravity (Agente)

---

## Contexto e Problema

O aluno (Lucas Galdino, Analista de TI na DGTI/IFCE) vem de formação em Ciências Humanas e atua na prática com infraestrutura de servidores e contêineres há anos. Ao iniciar os estudos teóricos de Lógica Matemática, Relações e Teoria dos Conjuntos, materiais didáticos tradicionais falham por:
1. Apresentar linguagem excessivamente árida, enciclopédica e intimidadora, presumindo familiaridade prévia com símbolos matemáticos;
2. Jogar múltiplos axiomas e fórmulas em blocos de texto contínuos sem pausas ou degraus cognitivos digestíveis;
3. Não pronunciar os símbolos lógicos nem explicar o porquê de cada operador ter sido inventado;
4. Falta de feedback imediato de compreensão após a leitura, gerando falsa ilusão de competência ou insegurança antes do treino pesado de prova.

O princípio orientador central é o enunciado pelo Prof. Albert Einstein:
> *"Se você não consegue explicar algo para uma criança de seis anos, você mesmo não entende."*

## Decisão

Institui-se o **Padrão Didático e Visual de Excelência** como obrigatório para todas as aulas do projeto (presentes e futuras):

### 1. Linguagem, Tom e Conexão com o Aluno
- **Tom Acolhedor e Direto:** Diálogo direto com o aluno (*"Você"*), empático e desarmador.
- **Aterramento Imediato:** Toda abstração matemática deve ser imediatamente traduzida para uma analogia prática e visceral do mundo real ou de TI/infraestrutura (ex: pacotes de rede, nós de cluster, tabelas relacionais, permissões de sistema de arquivos).
- **Zero Pressuposição de Símbolos:** Nenhum símbolo ($\in, \subseteq, \land, \iff, \forall, \exists, \equiv, \lessdot, \mid, \cup, \cap$) pode ser utilizado sem ser formalmente apresentado, pronunciado foneticamente e explicado.

### 2. Estrutura em Degraus Cognitivos (Micro-Blocos)
- **Desmistificação de Termos (`.word-breakdown`):** Blocos com o termo em destaque, etimologia e pronúncia silábica literal (`.pronunciation`, ex: `[pô-sét]`, `[an-ti-si-mé-tri-ca]`, `[há-sse]`).
- **Caixa de Fórmula Limpa (`.formula-box`):**
  - Fórmula KaTeX limpa e destacada no centro do card branco com sombra suave.
  - Barra de leitura e decodificação integrada na base (`.reading-guide`):
    - **Como se fala:** pronúncia fonética exata em voz alta (ex: *"a é congruente a b módulo n"*).
    - **O que significa:** explicação semântica do símbolo e do operador (ex: *"Repare no símbolo com três tracinhos $\equiv$, que indica equivalência modular"*).
- **Dicionário de Pronúncia de Símbolos Lógicos:** Tabela ou card temático ensinando a pronúncia fonética e significado de cada símbolo lógico utilizado na fase.

### 3. Paleta Semântica e Caixas de Destaque
- `.callout.philosophy` (Borda âmbar `#7c2d12`, fundo `#fff7ed`): Transição ontológica, história da lógica e quebra de paradigma conceitual.
- `.callout.computation` (Borda esmeralda `#065f46`, fundo `#f0fdf4`): Definição formal canônica para o concurso e aplicação em sistemas computacionais.
- `.callout.warning` / `.trap-box` (Borda âmbar `#b45309` ou rosa `#e11d48`, fundo `#fffbeb` ou `#fff1f2`): Armadilhas e pegadinhas clássicas da banca examinadora.
- `.callout.warshall` (Borda violeta `#6b21a8`, fundo `#f5f3ff`): Passos matriciais de algoritmos e transformações de estado.
- Tabelas Acadêmicas (`.academic-table` em `.table-wrapper`): Células confortáveis com `white-space: nowrap` estrito em conceitos e fórmulas KaTeX para nunca quebrar palavras curtas ou símbolos ao meio.

### 4. Interatividade Tátil Dinâmica
- Micro-laboratórios táteis específicos para cada degrau cognitivo (`.interactive-card`):
  - Matrizes booleanas clicáveis com cálculo de propriedades em tempo real;
  - Dígrafos vetoriais SVG interativos que reagem à seleção;
  - Simuladores de redução de Hasse que demonstram a eliminação de atalhos e laços passo a passo.

### 5. Active Retrieval no Rodapé vs. Banco de Questões da Banca
- **Active Retrieval (`.quiz-section`):** Mini-quiz de 4 questões conceituais ao final da aula focado exclusivamente na **retenção e compreensão imediata** do que foi lido.
  - Feedback instantâneo colorido: verde (`.feedback-box.correct`) para acerto e vermelho (`.feedback-box.incorrect`) para erro, com justificativa didática detalhada na hora;
  - Banner de pontuação dinâmico (`.score-banner`) calculando a taxa de retenção ao vivo.
- **Card "Próxima Parada" (`.next-step-card`):** Síntese do degrau conquistado e gancho motivador com o próximo tópico da trilha.
- **Botão Primário para o Banco de Questões de Prova:**
  - Botão de destaque **"Praticar questões desta aula na banca"** (`href="../questoes.html?topico=<id>"`).
  - O Banco de Questões (`questoes.html`) concentra a **cobrança real da banca** (questões oficiais do Edital 53/2025 e inéditas calibradas no padrão `/gerador-questoes-cfp`), com temporizador, motor de repetição espaçada FSRS v5 e Caderno de Erros.

---

## Consequências

- **Acolhimento Total e Autoconfiança:** O aluno estuda sem frustração ou sentimento de inadequação formal.
- **Retenção Ativa Pré-Treino:** O aluno consolida a teoria antes de ser exposto às pegadinhas e pressões de tempo do banco de questões.
- **Coerência Sistêmica:** Todas as lições presentes e futuras das Fases 1 a 5 seguirão exatamente a mesma anatomia pedagógica de excelência.
