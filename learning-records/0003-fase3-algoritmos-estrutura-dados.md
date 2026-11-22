# Learning Record 0003: Conclusão da Fase 3 (Algoritmos e Estrutura de Dados)

- **Data:** 20 de Novembro de 2026
- **Status:** Concluído com 100% de Aproveitamento Pedagógico
- **Módulo:** Fase 3 — Algoritmos e Estrutura de Dados (Coração do Edital — Anexo VII, Item 2)
- **Tópicos:** 19 a 27

## 1. O que foi Aprendido e Consolidado

### 1.1 Notação Assintótica e Ordens de Grandeza (Aula 19)
- **Medição Teórica (Q12 Oficial 2025):** O tempo de algoritmos não é cronometrado em segundos ou microsegundos (voláteis e dependentes do hardware), mas mensurado formalmente no **número de operações chave** executadas em função do tamanho da entrada $n$.
- **Laços Aninhados e Progressão Aritmética (Q06 Oficial 2025):** A soma $\sum_{i=1}^n (n - i + 1) = \frac{n(n+1)}{2} = \frac{n^2}{2} + \frac{n}{2}$ possui ordem de grandeza assintótica estritamente dominada por **$O(n^2)$**.
- **A Tríade Formal:** Notação $O$ (cota superior / teto: $f(n) \le c \cdot g(n)$), Notação $\Omega$ (cota inferior / piso: $f(n) \ge c \cdot g(n)$) e Notação $\Theta$ (cota justa / sanduíche: $c_1 g(n) \le f(n) \le c_2 g(n)$).
- **Logaritmos na Prática:** $\log_2 n$ representa o número de vezes que $n$ pode ser dividido pela metade até chegar a 1. Para $n = 1.000.000$, $\log_2 n \approx 20$.

### 1.2 Análise de Pior Caso, Médio e Melhor Caso (Aula 20)
- **A Dependência da Entrada:** O "caso" é o arranjo dos dados para um mesmo $n$. O pior caso garante um teto inviolável de desempenho, essencial para clusters de contêineres e sistemas de tempo real.
- **Busca Binária no Pior Caso (Q02 Oficial 2025):** Algoritmo `Bar(A, n, x)` reduz pela metade o espaço de busca a cada iteração do `while`, atingindo **$\Theta(\log n)$** no pior caso.
- **Série Geométrica com Laço Halving (Q01 Oficial 2025):** Algoritmo `Boo(A, n)` executa um laço interno que soma metades decrescentes ($n/2 + n/4 + \dots = n \sum (1/2)^k = n$). Logo, a complexidade de pior caso é linear: **$\Theta(n)$**.

### 1.3 Teorema Mestre e Recorrências (Aula 21)
- **Forma Canônica:** $T(n) = a T(n/b) + f(n)$, onde $a \ge 1$ (subproblemas), $b > 1$ (divisão) e $f(n)$ (combinação).
- **A Batalha dos Custos:**
  - Caso 1: Folhas vencem ($f(n) < n^{\log_b a}$) $\implies T(n) = \Theta(n^{\log_b a})$ (ex: Strassen $\Theta(n^{2{,}81})$).
  - Caso 2: Empate ($f(n) = n^{\log_b a}$) $\implies T(n) = \Theta(n^{\log_b a} \log n)$ (ex: MergeSort $\Theta(n \log n)$).
  - Caso 3: Raiz vence ($f(n) > n^{\log_b a}$) $\implies T(n) = \Theta(f(n))$.
- **Inaplicabilidade do Teorema Mestre:** Recorrências com redução subtrativa (ex: $T(n) = T(n-1) + n$) não dividem por $b$; são resolvidas por expansão telescópica resultando em **$\Theta(n^2)$** (pior caso do QuickSort).

### 1.4 Estruturas Lineares: Listas Encadeadas (Aula 22)
- **Listas Sem Ponteiro de Cauda (Q05 e Q11 Oficiais 2025):**
  - Acesso ao $i$-ésimo: $O(n)$ (exige caminhamento sequencial de ponteiros).
  - Inserção no início: $O(1)$ (basta atualizar `novo->prox = head`).
  - Remoção no início: $O(1)$.
  - Inserção no fim (sem tail): $O(n)$ (a mais custosa da Q11, exige achar o `NULL`).
  - Remoção no fim (sem tail): $O(n)$ (exige encontrar o penúltimo nó para apontá-lo para `NULL` - Q05).
- **Variações:** Lista Duplamente Encadeada (permite remoção de nó conhecido em $O(1)$) e Lista Circular (usada no escalonador Round-Robin de processos do SO).

### 1.5 Pilhas (LIFO) e Filas (FIFO) (Aula 23)
- **Rastreamento de Pilha (Q04 Oficial 2025):** Execução rigorosa dos 7 passos com retorno final da operação 7 sendo exatamente **2**.
- **Rastreamento de Fila (Q08 Oficial 2025):** Ordem exata de remoção por FIFO gerando a sequência **3, 1, 4**.
- **Aritmética Modular de Vetor Circular:** $\text{fim} = (\text{fim} + 1) \pmod N$ para reuso de slots em tempo $O(1)$.

### 1.6 Árvores Binárias de Busca (BST) e Percursos (Aula 24)
- **Propriedade BST:** Chaves menores à esquerda, maiores à direita.
- **Os Três Percursos DFS:**
  - Pré-ordem (V-E-D): Raiz primeiro (usado para serialização/cópia).
  - Em-ordem (E-V-D): Raiz no meio $\implies$ **imprime os nós em ordem crescente!**
  - Pós-ordem (E-D-V): Raiz por último (usado para `free` e desalocação de memória).
- **Remoção de Nó com Dois Filhos:** Substituição pelo Sucessor em-ordem (menor da subárvore direita) ou Antecessor em-ordem (maior da subárvore esquerda).
- **Degeneração:** Inserção ordenada de dados transforma a BST em lista linear com pior caso $O(n)$.

### 1.7 Balanceamento de Árvores: AVL e Rubro-Negras (Aula 25)
- **Árvore AVL:** Invariante $|BF| \le 1$, onde $BF = h_{\text{esq}} - h_{\text{dir}}$. Quatro rotações em tempo constante $O(1)$ (Simples à Direita LL, Simples à Esquerda RR, Dupla LR e Dupla RL).
- **Árvore Rubro-Negra (Red-Black Tree):** 5 regras estritas (Raiz preta, folhas NULL pretas, nós vermelhos não podem ser consecutivos, mesma altura preta em todos os caminhos). Altura $h \le 2 \log_2(n+1)$, assegurando $O(\log n)$.
- **Uso no Kernel Linux:** Adotada no Completely Fair Scheduler (CFS) e na STL (`std::map`) devido ao menor número de rotações em operações intensivas de escrita.

### 1.8 Algoritmos de Ordenação I: Quadráticos (Aula 26)
- **Conceitos:** In-Place ($O(1)$ de espaço auxiliar) e Estabilidade (preservação da ordem relativa de chaves iguais).
- **Bubble Sort:** Trocas adjacentes. Melhor caso $\Theta(n)$ com flag de parada, pior caso $\Theta(n^2)$. Estável.
- **Selection Sort:** Menor para a frente. **$\Theta(n^2)$ EM TODOS OS CASOS**, inclusive no melhor caso! Vantagem: faz no máximo $n - 1$ trocas físicas ($O(n)$ escritas). Instável.
- **Insertion Sort:** Analogia com baralho. Melhor caso linear $\Theta(n)$ para dados previamente ordenados. Estável e imbatível para $n < 30$.

### 1.9 Algoritmos de Ordenação II: Eficientes (Aula 27)
- **Cota Inferior $\Omega(n \log n)$:** Demonstrada pelo modelo da árvore de decisão com $n!$ folhas ($\log_2(n!) \approx n \log n$).
- **QuickSort no Pior Caso (Q16 Oficial 2025):** Tempo de execução no pior caso é **$O(n^2)$** devido ao desbalanceamento extremo de partição ($0$ e $n-1$). Mitigado por Pivô Mediana de Três e QuickSort Randomizado. Na média, é o mais rápido da prática.
- **MergeSort:** Divisão e conquista estável em $\Theta(n \log n)$ em todos os casos, mas consome $O(n)$ de memória auxiliar.
- **HeapSort:** Baseado em Max-Heap. Conquista tempo $\Theta(n \log n)$ no pior caso E espaço $O(1)$ in-place simultaneamente.

---

## 2. Inventário de Aulas da Fase 3 (100% Concluídas)
- [0019-notacao-assintotica-ordens-grandeza.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0019-notacao-assintotica-ordens-grandeza.html)
- [0020-analise-pior-medio-melhor-caso.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0020-analise-pior-medio-melhor-caso.html)
- [0021-teorema-mestre-recorrencias.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0021-teorema-mestre-recorrencias.html)
- [0022-estruturas-lineares-listas-encadeadas.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0022-estruturas-lineares-listas-encadeadas.html)
- [0023-pilhas-e-filas-implementacao-aplicacoes.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0023-pilhas-e-filas-implementacao-aplicacoes.html)
- [0024-arvores-binarias-busca-percursos.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0024-arvores-binarias-busca-percursos.html)
- [0025-balanceamento-arvores-avl-rubro-negras.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0025-balanceamento-arvores-avl-rubro-negras.html)
- [0026-algoritmos-ordenacao-quadraticos.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0026-algoritmos-ordenacao-quadraticos.html)
- [0027-algoritmos-ordenacao-eficientes.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0027-algoritmos-ordenacao-eficientes.html)

---

## 3. Próximo Passo
Avançar para a **Fase 4: Fundamentos Teóricos CA05 — Arquitetura de Contêineres, Google Borg, Autopilot e Kubernetes QoS (Tópicos 28 a 33)**:
- Tópicos 28 a 33:
  28. Arquitetura de Sistemas Baseados em Contêineres (Namespaces, Cgroups, Chroot/Pivot Root e Camadas OverlayFS)
  29. O Sistema Google Borg: Arquitetura, Alocação, Isolamento e Resiliência (Artigo Verma et al., EuroSys 2015)
  30. Autopilot: Auto-Tuning e Auto-Scaling Dinâmico de Recursos (Artigo Rzadca et al., EuroSys 2020)
  31. Classes de Serviço e QoS no Kubernetes: Guaranteed, Burstable e BestEffort
  32. Métricas de Desempenho e Alocação: Overcommitment, Throttling de CPU, OOM-Killer e Eviction
  33. Otimização de Recursos em Infraestruturas Institucionais: Casos de Uso e Restrições DGTI/IFCE
