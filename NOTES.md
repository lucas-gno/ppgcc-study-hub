# Notas Pedagógicas, Diretrizes de Design e Arquitetura do Hub (PPGCC IFCE)

> **Documento Central de Governança para Agentes e Desenvolvedores.**  
> Este documento baliza todas as decisões pedagógicas, visuais, interativas e técnicas para a preparação ao processo seletivo do PPGCC IFCE (Edital 43/2026 - Turma 2027.1 / Linha CA05). Ele serve de fundação direta para a criação do `AGENTS.md`, permitindo que qualquer agente de IA assuma o projeto do zero sem quebrar suas diretrizes fundamentais.

---

## 1. Perfil do Aluno e Premissa Pedagógica Fundamental

- **Origem Não-Exata:** O aluno **não vem da área de ciências matemáticas nem da ciência da computação pura**, e sim da área de **ciências humanas**.
- **Condição "Enferrujado":** O aluno está retornando aos estudos teóricos após anos de atuação prática e técnica em infraestrutura/redes. Portanto, **toda a base teórica formal precisa ser construída do zero absoluto**.
- **Proibição de Conhecimento Presumido:** 
  - Jamais assuma que o aluno sabe o significado de símbolos matemáticos ou termos formais (ex.: $\lessdot$, $\preceq$, $\subseteq$, $\equiv_n$, $\forall$, $\exists$, somatórios, notação assintótica $\mathcal{O}/\Omega/\Theta$, lógica booleana, ou álgebra relacional).
  - É proibido jogar uma fórmula "crua" na tela sem dissecar cada caractere que a compõe.
- **Obrigatoriedade da Tradução Tríplice em Todo Conceito Formal:**
  1. **Fórmula Simbólica Rigorosa:** A representação matemática oficial exigida pela banca examinadora.
  2. **Caixa "Como se Lê" (Pronúncia Fonética Passo a Passo):** Transcrição fonética literal para leitura em voz alta (ex.: *"lê-se: x precede imediatamente y"* ou *"para todo x pertencente aos Reais tal que..."*).
  3. **Tradução Intuitiva ("Em Bom Português / Analogia Prática"):** Explicação desmistificada usando analogias cotidianas ou da prática de TI institucional (servidores, arquivos, permissões, hierarquia organizacional), deixando evidente o *porquê* daquilo existir.

---

## 2. A Dicotomia Obrigatória: Visual vs. Interativo

> [!IMPORTANT]
> **Visual** e **Interativo** são dois pilares **distintos que se complementam**. Uma aula não pode ser considerada pronta se tiver apenas texto e fórmulas, nem se tiver apenas um gráfico estático ou apenas um quiz de múltipla escolha.

### A. O Pilar Visual (Representação Espacial e Gráfica)
O aluno vindo de humanas compreende e fixa abstrações matemáticas complexas através da **geometrização e espacialidade**.
- **Diagramas Vetoriais em SVG Puro:** Todas as aulas teóricas precisam conter diagramas gráficos integrados ao HTML (não imagens externas).
  - *Exemplos Obrigatórios na Fase 1:*
    - Diagramas de Hasse para divisibilidade ($D_{12}$, $D_{30}$, etc.);
    - Hipercubos de partes de conjuntos ($Q_3$ / $\mathcal{P}(\{a,b,c\})$);
    - Reticulados notáveis de concurso: Diamante ($M_3$) e Pentágono ($N_5$);
    - Dígrafos de relações com laços, arcos dirigidos e matrizes de adjacência.
  - *Exemplos na Fase 2 e 3:*
    - Mapas visuais de memória física (Stack vs. Heap, tabelas de ponteiros com endereços hexadecimais `0x1000`);
    - Árvores binárias de busca (BST) e diagramas de rotação AVL (Zig-Zig, Zig-Zag);
    - Diagramas de nós de cluster Kubernetes / Google Borg (Pods, cgroups, throttled CPU).

### B. O Pilar Interativo (Manipulação Ativa e Mudança de Estado)
O aluno não pode ser mero espectador passivo. Ele aprende modificando o estado do sistema e observando a consequência imediata.
- **Controles Táteis e Manipuladores:**
  - Sliders ou botões de passo-a-passo (ex.: *Redução de Hasse Passo 0 ao 3: Remover Laços $\rightarrow$ Remover Atalhos $\rightarrow$ Alinhar Verticalmente*);
  - Matrizes booleanas clicáveis onde o aluno liga/desliga células e o painel recalcula instantaneamente se a relação se tornou reflexiva, simétrica ou transitiva;
  - Simuladores de escalonamento onde o aluno ajusta CPU/Memória e observa a ocorrência de *Throttling* ou *Out-Of-Memory (OOM)*.

---

## 3. Sandboxes Jupyter no Navegador (Fase 2, Fase 3 e Sistemas)

Para todas as aulas que envolvem código-fonte (C99, Python), algoritmos, análise de complexidade e estruturas de dados:
- **Obrigatório Integrar o Simulador Jupyter:** O aluno não aprende a programar ou raciocinar sobre ponteiros lendo texto estático.
- **Recursos Obrigatórios do Componente Sandbox (`.notebook-cell`):**
  1. **Topbar macOS Minimalista:** Indicadores visuais clássicos (pontos vermelho, amarelo e verde) e badge de kernel ativo (*Kernel Simulado C99/Python*).
  2. **Código-Fonte Didático:** Apresentado com realce de sintaxe (*Dark Monospaced Theme*).
  3. **Grupo de Entradas Interativas (`.notebook-inputs-group`):** Campos onde o aluno pode alterar variáveis de teste (tamanho do array, valor de entrada, nós a inserir) sem necessidade de reescrever código.
  4. **Controles de Execução:** Botão primário com animação tátil (`▶ Executar Código`), botão de execução passo-a-passo e reset.
  5. **Console `stdout` Integrado:** Terminal de saída em tempo real simulado com código de cores (verde para saída normal, ciano para métricas de tempo, vermelho para erros/traps).
  6. **Inspetor Visual de Memória (`.notebook-inspector-panel`):** Tabela ou mapa interativo mostrando a evolução das variáveis na memória e ponteiros em tempo real.

---

## 4. Identidade Visual e Experiência do Usuário (UI/UX)

Seguindo rigorosamente as diretrizes das skills `/apple-design`, `/emil-design-eng`, `/animate` e `/antigravity-design-expert`:
- **Estética Geral:** Moderno, luminoso, clean e minimalista — eliminando qualquer aparência de "livro acadêmico vintage" (sem fontes serifadas antigas, sem fundos marfim amarelados).
- **Tipografia:** 100% grotesca de sistema (`-apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Inter", system-ui, sans-serif`).
  - *Tracking Óptico:* Títulos com tracking negativo refinado (`-0.028em` em H1 e `-0.02em` em H2) e entrelinha respirada (`1.68` - `1.70`) no corpo.
  - *Zero Serifa:* Proibição total de fontes clássicas acadêmicas (`Charter`, `Georgia`, `Times`).
- **Canvas e Cores:**
  - Canvas claro e luminoso (`#f8fafc`), cartões em branco puro (`#ffffff`) e bordas suaves Slate (`#e2e8f0`).
  - Paleta de acentos Apple: Azul Apple (`#0071e3`), Verde Esmeralda (`#10b981`), Vermelho Apple (`#ef4444`), Âmbar (`#f59e0b`), Violeta (`#8b5cf6`) e Ciano Céu (`#0284c7`).
- **Micro-interações Táteis:**
  - Resposta imediata no clique: `:active { transform: scale(0.985); }`.
  - Hover com leve elevação flutuante: `:hover { transform: translateY(-1px); }`.
  - Curvas de aceleração Apple: `--ease-apple: cubic-bezier(0.16, 1, 0.3, 1)`.
- **Sistema de Questões Interativas (Quiz):**
  - Botões de opção (`.option-btn`) com indicador circular de letra (A–E);
  - Feedback visual imediato ao clique (verde para acerto, vermelho com vibração *shake* para erro);
  - Gabarito e dissecação cirúrgica de distratores revelados com animação de slide-fade (`solutionFadeSlide 240ms`).

---

## 5. Arquitetura Técnica, GitHub Pages e Próximos Passos (`AGENTS.md`)

- **Objetivo Estratégico:** O hub será hospedado publicamente no **GitHub Pages** para que o usuário possa estudar online de qualquer dispositivo (desktop, tablet, celular), inspirado no modelo de sucesso do projeto do próprio usuário: [`https://github.com/lucas-sva/cfp-study-hub`](https://github.com/lucas-sva/cfp-study-hub), porém com uma estrutura mais simples, leve e focada em uso pessoal.
- **Premissas da Arquitetura Estática:**
  - **100% Estático e Offline-First:** Arquivos `.html`, `.css` e `.js` puros (Vanilla).
  - Sem necessidade de bundlers, webpack, vite, frameworks pesados (React/Vue) ou servidores Node/Python em execução.
  - O KaTeX é servido localmente em `assets/katex/` para independência total de rede.
  - Sincronização espelhada garantida entre o repositório local e o Google Drive (`g:\Meu Drive\PPGCC-IFCE\`).
- **Missão do Futuro `AGENTS.md`:**
  - O `AGENTS.md` a ser elaborado servirá como guia mestre de instruções para que qualquer novo agente de IA ou subagente possa:
    1. Auditar se todas as 37 aulas cumprem a regra de ter partes visuais (SVG) e interativas (widgets/sandboxes);
    2. Inserir e instanciar os widgets pendentes (como os diagramas da Aula 8 e similares);
    3. Manter a coerência didática Zero-Base e a identidade visual Apple/Emil Kowalski;
    4. Automatizar a estrutura de publicação contínua no GitHub Pages.
