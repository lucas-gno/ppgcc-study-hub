"""Idempotent ingestion of the 20 official questions from Edital 53/2025 into data/mestrado.db."""

from datetime import datetime, timezone
import pathlib
import sqlite3

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "mestrado.db"

OFFICIAL_QUESTIONS_2025 = [
    {
        "numero_prova": 1,
        "topico_id": 19,
        "nivel": "MEDIO",
        "enunciado": (
            "Considere o algoritmo `Boo(A, n)` abaixo, em que `A` é um vetor de inteiros e $n \\ge 1$ é o seu tamanho.\n\n"
            "```text\n"
            "function Boo(A, n)\n"
            "  esq <- 1\n"
            "  dir <- n\n"
            "  total <- 0\n"
            "  while esq <= dir do\n"
            "    mid <- floor((esq + dir) / 2)\n"
            "    for i <- mid to dir do\n"
            "      total <- total + A[i]\n"
            "    end for\n"
            "    dir <- mid - 1\n"
            "  return total\n"
            "```\n\n"
            "No pior caso, o tempo de execução de `Boo(A, n)`, em notação $\\Theta$, é:"
        ),
        "alt_a": "$\\Theta(\\log n)$",
        "alt_b": "$\\Theta(n)$",
        "alt_c": "$\\Theta(n \\log n)$",
        "alt_d": "$\\Theta(n^2)$",
        "alt_e": "",
        "correta": "B",
        "justificativa": (
            "Alternativa correta: **B** ($\\Theta(n)$). A cada iteração do laço `while`, `dir` é reduzido para `mid - 1`, cortando o intervalo pela metade. "
            "O laço `for` interno percorre a metade superior do intervalo vigente: na 1a iteração executa cerca de $n/2$ passos, na 2a cerca de $n/4$, depois $n/8$, etc. "
            "A soma forma uma série geométrica convergente: $\\sum_{k=1}^{\\log n} \\frac{n}{2^k} < n$, resultando em tempo linear $\\Theta(n)$.\n\n"
            "- **A) Incorreta:** $\\Theta(\\log n)$ seria válido apenas se o trabalho por iteração do `while` fosse constante $O(1)$.\n"
            "- **C) Incorreta:** $\\Theta(n \\log n)$ ocorreria se o laço interno percorresse todos os $n$ elementos em cada uma das $\\log n$ iterações.\n"
            "- **D) Incorreta:** $\\Theta(n^2)$ exigiria $O(n)$ iterações externas executando $O(n)$ passos internos."
        ),
    },
    {
        "numero_prova": 2,
        "topico_id": 26,
        "nivel": "FACIL",
        "enunciado": (
            "Considere o algoritmo `Bar(A, n, x)` abaixo, em que `A` é um vetor ordenado de inteiros, $n \\ge 1$ é o seu tamanho e `x` é um inteiro.\n\n"
            "```text\n"
            "function Bar(A, n, x)\n"
            "  esq <- 1\n"
            "  dir <- n\n"
            "  while esq <= dir do\n"
            "    mid <- floor((esq + dir) / 2)\n"
            "    if A[mid] = x then\n"
            "      return mid\n"
            "    else if A[mid] < x then\n"
            "      esq <- mid + 1\n"
            "    else\n"
            "      dir <- mid - 1\n"
            "  return -1\n"
            "```\n\n"
            "No pior caso, o tempo de execução de `Bar(A, n, x)`, em notação $\\Theta$, é:"
        ),
        "alt_a": "$\\Theta(1)$",
        "alt_b": "$\\Theta(\\log n)$",
        "alt_c": "$\\Theta(n)$",
        "alt_d": "$\\Theta(n \\log n)$",
        "alt_e": "",
        "correta": "B",
        "justificativa": (
            "Alternativa correta: **B** ($\\Theta(\\log n)$). `Bar` é a implementação clássica da Busca Binária. "
            "No pior caso (elemento ausente ou encontrado na última subdivisão), o espaço de busca é dividido por 2 a cada iteração com trabalho $O(1)$ por passo, totalizando $\\Theta(\\log_2 n)$.\n\n"
            "- **A) Incorreta:** $\\Theta(1)$ ocorre apenas no melhor caso (`A[mid] == x` na primeira comparação).\n"
            "- **C) Incorreta:** $\\Theta(n)$ corresponde à busca linear.\n"
            "- **D) Incorreta:** $\\Theta(n \\log n)$ é típico de ordenações eficientes, não de busca em vetor já ordenado."
        ),
    },
    {
        "numero_prova": 3,
        "topico_id": 26,
        "nivel": "DIFICIL",
        "enunciado": (
            "Seja o algoritmo `Bus(A, n, x)` abaixo, tal que `A` é um vetor ordenado de inteiros, $n \\ge 1$ é o tamanho de `A` e `x` é um inteiro.\n\n"
            "```text\n"
            "function Bus(A, n, x)\n"
            "  i <- 0\n"
            "  step <- 1\n"
            "  while i < n and A[i] < x do\n"
            "    i <- i + step\n"
            "    step <- step + 1\n"
            "  start <- max(0, i - (step - 1))\n"
            "  end <- min(i, n)\n"
            "  for j <- start to end - 1 do\n"
            "    if A[j] = x then\n"
            "      return j\n"
            "  end for\n"
            "  return None\n"
            "```\n\n"
            "No pior caso, o tempo de execução de `Bus(A, n, x)`, em notação $\\Theta$, é:"
        ),
        "alt_a": "$\\Theta(1)$",
        "alt_b": "$\\Theta(\\log n)$",
        "alt_c": "$\\Theta(\\sqrt{n})$",
        "alt_d": "$\\Theta(n)$",
        "alt_e": "",
        "correta": "C",
        "justificativa": (
            "Alternativa correta: **C** ($\\Theta(\\sqrt{n})$). No laço `while`, os saltos crescem linearmente: $1 + 2 + 3 + \\dots + k = \\frac{k(k+1)}{2}$. "
            "Para alcançar ou ultrapassar $n$, o número de iterações $k$ satisfaz $k^2 \\approx 2n \\implies k = \\Theta(\\sqrt{n})$. "
            "O último salto tem tamanho `step - 1` $= \\Theta(\\sqrt{n})$, logo o laço `for` sequencial final também executa no máximo $\\Theta(\\sqrt{n})$ passos. Total: $\\Theta(\\sqrt{n})$.\n\n"
            "- **A) Incorreta:** A busca depende de $n$ no pior caso.\n"
            "- **B) Incorreta:** Saltos lineares crecendo de 1 em 1 não dobram exponencialmente o alcance como na busca binária.\n"
            "- **D) Incorreta:** Como o passo aumenta a cada salto, o algoritmo não visita todos os $n$ elementos."
        ),
    },
    {
        "numero_prova": 4,
        "topico_id": 21,
        "nivel": "FACIL",
        "enunciado": (
            "Sobre o funcionamento da estrutura de dados pilha, considere uma pilha inicialmente vazia e a seguinte sequência de operações:\n\n"
            "1. `push(1)`\n"
            "2. `push(2)`\n"
            "3. `push(3)`\n"
            "4. `pop()`\n"
            "5. `push(4)`\n"
            "6. `pop()`\n"
            "7. `pop()`\n\n"
            "Qual é o valor retornado pela última operação `pop()`?"
        ),
        "alt_a": "`1`",
        "alt_b": "`2`",
        "alt_c": "`3`",
        "alt_d": "Nenhum valor é retornado, pois a pilha estaria vazia.",
        "alt_e": "",
        "correta": "B",
        "justificativa": (
            "Alternativa correta: **B** (`2`). Em uma pilha LIFO (*Last-In, First-Out*), o rastreamento passo a passo resulta em:\n"
            "- Após passos 1–3: `[1, 2, 3]` (topo = 3)\n"
            "- Passo 4 (`pop()`): remove `3` -> pilha `[1, 2]`\n"
            "- Passo 5 (`push(4)`): insere `4` -> pilha `[1, 2, 4]`\n"
            "- Passo 6 (`pop()`): remove `4` -> pilha `[1, 2]`\n"
            "- Passo 7 (`pop()`): remove e retorna **`2`**.\n\n"
            "- **A) Incorreta:** `1` permanece na base da pilha após o 7o passo.\n"
            "- **C) Incorreta:** `3` foi removido já no passo 4.\n"
            "- **D) Incorreta:** Foram feitos 4 `push` e 3 `pop`, restando 1 elemento."
        ),
    },
    {
        "numero_prova": 5,
        "topico_id": 20,
        "nivel": "MEDIO",
        "enunciado": (
            "Considere uma lista encadeada com $n$ elementos **sem ponteiro para o último elemento**. "
            "Considere as operações a seguir e suas complexidades no pior caso:\n\n"
            "1. Acessar o $i$-ésimo elemento da lista.\n"
            "2. Inserir um novo nó no início da lista.\n"
            "3. Remover o último elemento da lista.\n\n"
            "Quais são, respectivamente, as complexidades de tempo no pior caso dessas três operações?"
        ),
        "alt_a": "$\\Theta(1), \\Theta(1), \\Theta(1)$",
        "alt_b": "$\\Theta(n), \\Theta(1), \\Theta(n)$",
        "alt_c": "$\\Theta(\\log n), \\Theta(1), \\Theta(\\log n)$",
        "alt_d": "$\\Theta(n), \\Theta(n), \\Theta(1)$",
        "alt_e": "$\\Theta(1), \\Theta(1), \\Theta(n)$",
        "correta": "B",
        "justificativa": (
            "Alternativa correta: **B** ($\\Theta(n), \\Theta(1), \\Theta(n)$).\n"
            "1. Listas encadeadas não possuem acesso aleatório por índice; alcançar o $i$-ésimo nó exige percorrer a cadeia a partir de `head` ($\\Theta(n)$).\n"
            "2. Inserir no início requer apenas ajustar `novo->prox = head; head = novo` em tempo constante ($\\Theta(1)$).\n"
            "3. Remover o último elemento sem ponteiro de cauda (e em lista simples) exige caminhar até o penúltimo nó para atualizar seu ponteiro para `NULL` ($\\Theta(n)$).\n\n"
            "- **A, C, D, E) Incorretas:** Subestimam o acesso sequencial ou erram o custo da inserção na cabeça."
        ),
    },
    {
        "numero_prova": 6,
        "topico_id": 19,
        "nivel": "FACIL",
        "enunciado": (
            "Considere um algoritmo que recebe um vetor de tamanho $n$ e executa o seguinte procedimento:\n\n"
            "```text\n"
            "para i de 1 até n:\n"
            "  para j de i até n:\n"
            "    executar operação de tempo constante\n"
            "```\n\n"
            "Qual é a complexidade temporal desse algoritmo?"
        ),
        "alt_a": "$O(n)$",
        "alt_b": "$O(n \\log n)$",
        "alt_c": "$O(n^2)$",
        "alt_d": "$O(n^3)$",
        "alt_e": "$O(\\log n)$",
        "correta": "C",
        "justificativa": (
            "Alternativa correta: **C** ($O(n^2)$). Quando `i = 1`, o laço interno executa $n$ vezes; quando `i = 2`, executa $n-1$ vezes; até `i = n` (1 vez). "
            "O total de execuções é a soma da PA: $\\sum_{i=1}^{n} (n - i + 1) = \\frac{n(n+1)}{2} = \\frac{n^2 + n}{2} \\in O(n^2)$.\n\n"
            "- **A, B, D, E) Incorretas:** Ignoram a soma quadrática dos dois laços dependentes."
        ),
    },
    {
        "numero_prova": 7,
        "topico_id": 3,
        "nivel": "MEDIO",
        "enunciado": (
            "Considere o conjunto $A = \\{1, 2, 3\\}$. Seja $R$ uma relação definida em $A \\times A$ tal que:\n"
            "- $R$ é **reflexiva**;\n"
            "- $R$ **não é simétrica**;\n"
            "- $R$ é **transitiva**.\n\n"
            "Qual das relações abaixo pode ser $R$?"
        ),
        "alt_a": "$R = \\{(1, 1), (2, 2), (3, 3)\\}$",
        "alt_b": "$R = \\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)\\}$",
        "alt_c": "$R = \\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)\\}$",
        "alt_d": "$R = \\{(1, 1), (2, 2), (1, 2), (3, 1)\\}$",
        "alt_e": "$R = \\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)\\}$",
        "correta": "E",
        "justificativa": (
            "Alternativa correta: **E**. Verificando as três propriedades:\n"
            "- Reflexiva: contém $(1,1), (2,2), (3,3)$.\n"
            "- Não simétrica: contém $(1,2)$, mas não $(2,1)$.\n"
            "- Transitiva: de $(1,2)$ e $(2,3)$, inclui o fecho $(1,3)$.\n\n"
            "- **A) Incorreta:** É reflexiva e transitiva, mas também é simétrica (relação identidade).\n"
            "- **B) Incorreta:** Contém $(1,2)$ e $(2,1)$, logo é simétrica.\n"
            "- **C) Incorreta:** Falha na transitividade porque $(1,2), (2,3) \\in R$, mas $(1,3) \\notin R$.\n"
            "- **D) Incorreta:** Falha na reflexividade porque falta $(3,3)$ (e na transitividade, pois falta $(3,2)$)."
        ),
    },
    {
        "numero_prova": 8,
        "topico_id": 22,
        "nivel": "FACIL",
        "enunciado": (
            "Considere a seguinte sequência de operações sobre uma fila inicialmente vazia:\n\n"
            "`enqueue(3), enqueue(1), enqueue(4), dequeue(), enqueue(2), enqueue(5), dequeue(), dequeue()`\n\n"
            "Qual é a sequência de elementos removidos?"
        ),
        "alt_a": "`3, 1, 4`",
        "alt_b": "`3, 1, 2`",
        "alt_c": "`3, 4, 2`",
        "alt_d": "`3, 1, 5`",
        "alt_e": "`3, 4, 5`",
        "correta": "A",
        "justificativa": (
            "Alternativa correta: **A** (`3, 1, 4`). Na política FIFO (*First-In, First-Out*), os elementos saem exatamente na ordem de entrada:\n"
            "- Enfileira `3, 1, 4` -> fila `[3, 1, 4]`\n"
            "- 1o `dequeue()` remove **`3`** -> `[1, 4]`\n"
            "- Enfileira `2, 5` -> fila `[1, 4, 2, 5]`\n"
            "- 2o `dequeue()` remove **`1`** -> `[4, 2, 5]`\n"
            "- 3o `dequeue()` remove **`4`** -> `[2, 5]`.\n\n"
            "- **B, C, D, E) Incorretas:** Violam a ordem estritamente cronológica de saída FIFO."
        ),
    },
    {
        "numero_prova": 9,
        "topico_id": 14,
        "nivel": "FACIL",
        "enunciado": (
            "Considere a função abaixo em Python:\n\n"
            "```python\n"
            "def f(n):\n"
            "    if n <= 1:\n"
            "        return 1\n"
            "    return 2 * f(n - 1) + f(n - 2)\n"
            "```\n\n"
            "Qual é o valor retornado por `f(6)`?"
        ),
        "alt_a": "`99`",
        "alt_b": "`41`",
        "alt_c": "`34`",
        "alt_d": "`21`",
        "alt_e": "`17`",
        "correta": "A",
        "justificativa": (
            "Alternativa correta: **A** (`99`). Calculando de baixo para cima (bottom-up):\n"
            "- $f(0) = 1$\n"
            "- $f(1) = 1$\n"
            "- $f(2) = 2(1) + 1 = 3$\n"
            "- $f(3) = 2(3) + 1 = 7$\n"
            "- $f(4) = 2(7) + 3 = 17$\n"
            "- $f(5) = 2(17) + 7 = 41$\n"
            "- $f(6) = 2(41) + 17 = 82 + 17 =$ **`99`**.\n\n"
            "- **B) Incorreta:** `41` corresponde a $f(5)$.\n"
            "- **C) Incorreta:** `34` resulta de somar termos de Fibonacci ou erro aritmético.\n"
            "- **D) Incorreta:** `21` corresponde a Fibonacci deslocado.\n"
            "- **E) Incorreta:** `17` corresponde a $f(4)$."
        ),
    },
    {
        "numero_prova": 10,
        "topico_id": 9,
        "nivel": "MEDIO",
        "enunciado": (
            "Considere o código C:\n\n"
            "```c\n"
            "int a = 10, b = 3;\n"
            "float x = a / b;\n"
            "float y = a / (float)b;\n"
            "```\n\n"
            "Quais são os valores de `(x, y)`?"
        ),
        "alt_a": "`3` e `3.0`",
        "alt_b": "`3.0` e `3.0`",
        "alt_c": "`3.0` e `3.3`",
        "alt_d": "`3.0` e `3.333...`",
        "alt_e": "`3.3` e `3.3`",
        "correta": "D",
        "justificativa": (
            "Alternativa correta: **D** (`3.0` e `3.333...`). Conforme parecer oficial da banca do PPGCC ao recurso desta questão:\n"
            "- Em `a / b`, ambos os operandos são `int`, portanto C realiza **divisão inteira** com truncamento antes da atribuição, resultando em `3`, convertido ao `float x` como `3.0`.\n"
            "- Em `a / (float)b`, o cast explícito promove `b` para `float`, forçando `a` a ser promovido também; a divisão em ponto flutuante produz o valor não exato `3.333...` (reticências indicam dízima sem arredondamento).\n\n"
            "- **A, B, C, E) Incorretas:** Ignoram o tipo `float` de `x` (`3` vs `3.0`) ou truncam artificialmente a precisão de `y`."
        ),
    },
    {
        "numero_prova": 11,
        "topico_id": 20,
        "nivel": "FACIL",
        "enunciado": (
            "Uma lista simplesmente encadeada possui nós compostos por um valor e um ponteiro para o próximo. "
            "Qual operação é mais custosa (em tempo) nesta estrutura?"
        ),
        "alt_a": "Inserir no início.",
        "alt_b": "Inserir no fim sem ponteiro para o último.",
        "alt_c": "Ler o primeiro elemento.",
        "alt_d": "Verificar se está vazia.",
        "alt_e": "Remover o primeiro elemento.",
        "correta": "B",
        "justificativa": (
            "Alternativa correta: **B**. Inserir no fim sem ponteiro de cauda exige percorrer toda a lista desde `head` até achar o nó cujo campo `prox` é `NULL`, gastando tempo $O(n)$.\n\n"
            "- **A, C, D, E) Incorretas:** Todas operam diretamente sobre o ponteiro `head` em tempo constante $O(1)$."
        ),
    },
    {
        "numero_prova": 12,
        "topico_id": 19,
        "nivel": "FACIL",
        "enunciado": (
            "O fator tempo, relacionado à complexidade, quando usado para determinar a eficiência de algoritmos é medido em:"
        ),
        "alt_a": "Número de Microsegundos.",
        "alt_b": "Número de Rotinas.",
        "alt_c": "Número de Operações Chave.",
        "alt_d": "Tamanho em kB (kilobytes).",
        "alt_e": "Número de Linhas de Código.",
        "correta": "C",
        "justificativa": (
            "Alternativa correta: **C** (Número de Operações Chave). A análise assintótica independe de clock de CPU, compilador ou linguagem; "
            "por isso conta operações fundamentais (comparações, atribuições, acessos) em função da entrada $n$.\n\n"
            "- **A) Incorreta:** Tempo físico em microssegundos varia conforme hardware e sistema operacional.\n"
            "- **B, E) Incorretas:** Quantidade de funções ou linhas não mede custo em função de $n$ (um laço de 2 linhas pode ser $O(n^2)$).\n"
            "- **D) Incorreta:** Kilobytes referem-se a tamanho de código ou memória."
        ),
    },
    {
        "numero_prova": 13,
        "topico_id": 11,
        "nivel": "MEDIO",
        "enunciado": (
            "A saída do trecho de código em C abaixo é:\n\n"
            "```c\n"
            "int i = 0, j = 9, k = 7, cont;\n"
            "for (cont = 4; cont < 11; cont++) {\n"
            "    i = cont + 5;\n"
            "    while (k > 0) {\n"
            "        k = k - 1;\n"
            "        j = k + j / 2;\n"
            "    }\n"
            "}\n"
            "printf(\"i: %d j: %d k: %d\", i, j, k);\n"
            "```"
        ),
        "alt_a": "Erro em tempo de compilação.",
        "alt_b": "`i: 1 j: 4 k: 1`",
        "alt_c": "`i: 15 j: 1 k: 0`",
        "alt_d": "`i: 13 j: 2 k: 3`",
        "alt_e": "Error em tempo de execução.",
        "correta": "C",
        "justificativa": (
            "Alternativa correta: **C** (`i: 15 j: 1 k: 0`). Teste de mesa completo:\n"
            "- Na 1a passagem do `for` (`cont = 4`): `i = 9`. O `while (k > 0)` zera `k` executando 7 vezes:\n"
            "  - `k=6, j=6+9/2=10`\n"
            "  - `k=5, j=5+10/2=10`\n"
            "  - `k=4, j=4+10/2=9`\n"
            "  - `k=3, j=3+9/2=7`\n"
            "  - `k=2, j=2+7/2=5`\n"
            "  - `k=1, j=1+5/2=3`\n"
            "  - `k=0, j=0+3/2=1`\n"
            "- Nas iterações seguintes (`cont = 5..10`), `k` já vale `0` e nunca é reiniciado, logo o `while` não roda mais e `j` fica congelado em `1`.\n"
            "- No último passo válido (`cont = 10`), `i = 10 + 5 = 15`. Saída: `i: 15 j: 1 k: 0`.\n\n"
            "- **A, B, D, E) Incorretas:** O código compila normalmente sem erro de runtime e o último `cont` antes de `cont < 11` é `10`."
        ),
    },
    {
        "numero_prova": 14,
        "topico_id": 15,
        "nivel": "MEDIO",
        "enunciado": (
            "Que recursos as linguagens oferecem para evitar falhas de acesso a um endereço de memória inexistente?"
        ),
        "alt_a": "Tratamento de Exceções.",
        "alt_b": "Ponteiros.",
        "alt_c": "DMA (Acesso Direto à Memória).",
        "alt_d": "SWAP de Memória em Disco.",
        "alt_e": "Verificação em Tempo de Compilação.",
        "correta": "A",
        "justificativa": (
            "Alternativa correta: **A** (Tratamento de Exceções). Questão clássica recorrente do PPGCC IFCE (presente também na edição 20/2024): "
            "linguagens modernas oferecem mecanismos de exceção em tempo de execução (ex.: `NullPointerException`, `IndexOutOfBoundsException`, `IndexError`) para interceptar e tratar acessos inválidos sem corromper o programa.\n\n"
            "- **B) Incorreta:** Ponteiros crus permitem manipulação direta de endereços, frequentemente *causando* falhas se não validados.\n"
            "- **C, D) Incorretas:** DMA e SWAP são mecanismos de hardware/SO, não recursos de controle de fluxo da linguagem.\n"
            "- **E) Incorreta:** Endereços dinâmicos e limites de índices em tempo de execução não podem ser todos provados estaticamente em compilação."
        ),
    },
    {
        "numero_prova": 15,
        "topico_id": 21,
        "nivel": "DIFICIL",
        "enunciado": (
            "Considere as seguintes definições de classes que representam implementações de estruturas de dados disponíveis na biblioteca padrão de uma linguagem de programação:\n\n"
            "1. **Classe A** — os elementos são organizados em uma estrutura linear que permite inserções **exclusivamente nas extremidades** da sequência.\n"
            "2. **Classe B** — os elementos são armazenados em nós interligados, cada um contendo uma referência para o próximo elemento, permitindo percorrer a estrutura apenas em um sentido.\n"
            "3. **Classe C** — o elemento removido é sempre o último elemento que foi inserido, independentemente de sua posição corrente na estrutura.\n"
            "4. **Classe D** — os elementos são processados de acordo com a ordem estritamente cronológica de entrada, removendo-se sempre o primeiro elemento que foi inserido.\n\n"
            "Assinale a alternativa que representa, respectivamente, as estruturas de dados implementadas pelas classes A, B, C e D."
        ),
        "alt_a": "Deque, lista simplesmente encadeada, pilha baseada em vetor dinâmico e fila circular.",
        "alt_b": "Lista duplamente encadeada, lista simplesmente encadeada, deque em modo LIFO e fila encadeada.",
        "alt_c": "Deque de acesso restrito, lista simplesmente encadeada, pilha ligada e fila implementada sobre buffer circular.",
        "alt_d": "Lista de acesso bidirecional, lista simplesmente encadeada, pilha com política LIFO e deque em modo FIFO.",
        "alt_e": "Estrutura de extremidades duplas baseada em buffer, lista linear encadeada simples, pilha com nó sentinela e fila com controle de overflow circular.",
        "correta": "C",
        "justificativa": (
            "Alternativa correta: **C**. No parecer oficial aos recursos da Prova 53/2025, a comissão reforçou o rigor literal:\n"
            "- O item 1 exige inserções *exclusivamente nas extremidades*, correspondendo exatamente a um **deque de acesso restrito** (e não a um deque genérico).\n"
            "- O item 2 descreve a **lista simplesmente encadeada**.\n"
            "- O item 3 descreve a política LIFO da **pilha ligada**.\n"
            "- O item 4 descreve a fila estritamente FIFO (**fila implementada sobre buffer circular**).\n\n"
            "- **A) Incorreta:** A banca indeferiu explicitamente o recurso pró-alternativa A porque 'deque' genérico e 'fila circular' não refletem com exatidão as restrições descritas nos itens 1 e 4.\n"
            "- **B, D, E) Incorretas:** Trocam o tipo da Classe A (lista dupla não restringe inserção às extremidades) ou inserem detalhes incompatíveis."
        ),
    },
    {
        "numero_prova": 16,
        "topico_id": 25,
        "nivel": "FACIL",
        "enunciado": "Qual o tempo de execução do Quick Sort no pior caso?",
        "alt_a": "$O(n)$",
        "alt_b": "$O(n^2)$",
        "alt_c": "$O(n \\lg n)$",
        "alt_d": "$O(\\lg n)$",
        "alt_e": "",
        "correta": "B",
        "justificativa": (
            "Alternativa correta: **B** ($O(n^2)$). No pior caso (por exemplo, vetor já ordenado escolhendo o primeiro ou último elemento como pivô), "
            "a partição gera subproblemas de tamanhos $0$ e $n-1$, levando à recorrência $T(n) = T(n-1) + \\Theta(n) = \\Theta(n^2)$.\n\n"
            "- **A, D) Incorretas:** Ordenação por comparação tem cota inferior $\\Omega(n \\lg n)$.\n"
            "- **C) Incorreta:** $O(n \\lg n)$ é o caso médio / melhor caso do QuickSort."
        ),
    },
    {
        "numero_prova": 17,
        "topico_id": 2,
        "nivel": "FACIL",
        "enunciado": (
            "Seja o conjunto $A = \\{0, 1\\}$. Quantas relações binárias distintas podem ser definidas sobre o conjunto $A$?"
        ),
        "alt_a": "`2`",
        "alt_b": "`4`",
        "alt_c": "`8`",
        "alt_d": "`16`",
        "alt_e": "",
        "correta": "D",
        "justificativa": (
            "Alternativa correta: **D** (`16`). Uma relação binária sobre $A$ é qualquer subconjunto de $A \\times A$. "
            "Como $|A| = 2$, o produto cartesiano possui $|A \\times A| = 2 \\times 2 = 4$ pares ordenados. "
            "Logo, o número de subconjuntos em $\\mathcal{P}(A \\times A)$ é $2^{|A|^2} = 2^4 = 16$.\n\n"
            "- **A) Incorreta:** `2` é $|A|$.\n"
            "- **B) Incorreta:** `4` é o número de pares em $A \\times A$ (ou $2^{|A|}$).\n"
            "- **C) Incorreta:** `8` resulta de erro de potência $2^3$."
        ),
    },
    {
        "numero_prova": 18,
        "topico_id": 4,
        "nivel": "MEDIO",
        "enunciado": (
            "Seja $R$ a relação definida no conjunto dos números reais por: $(x, y) \\in R$ se, e somente se, $|x| = |y|$. "
            "Pode-se concluir que $R$ é uma relação:"
        ),
        "alt_a": "de ordem.",
        "alt_b": "de equivalência.",
        "alt_c": "antissimétrica.",
        "alt_d": "irreflexiva.",
        "alt_e": "",
        "correta": "B",
        "justificativa": (
            "Alternativa correta: **B** (de equivalência). A igualdade de módulos satisfaz a tríade de equivalência:\n"
            "- **Reflexiva:** $|x| = |x|$ para todo $x \\in \\mathbb{R}$.\n"
            "- **Simétrica:** Se $|x| = |y|$, então $|y| = |x|$.\n"
            "- **Transitiva:** Se $|x| = |y|$ e $|y| = |z|$, então $|x| = |z|$.\n\n"
            "- **A, C) Incorretas:** Não é antissimétrica, pois $(2, -2) \\in R$ e $(-2, 2) \\in R$ com $2 \\neq -2$; logo não pode ser ordem.\n"
            "- **D) Incorreta:** É reflexiva, nunca irreflexiva."
        ),
    },
    {
        "numero_prova": 19,
        "topico_id": 1,
        "nivel": "FACIL",
        "enunciado": "Qual das seguintes relações binárias **não** representa uma função?",
        "alt_a": "$R_1 = \\{(3, 6), (4, 15)\\}$",
        "alt_b": "$R_2 = \\{(4, 5), (7, 2), (7, 9)\\}$",
        "alt_c": "$R_3 = \\{(-2, 5), (-1, 5), (0, 5), (1, 5), (2, 5)\\}$",
        "alt_d": "$R_4 = \\{(x, y) \\mid y = 3x^2 + 2\\}$",
        "alt_e": "",
        "correta": "B",
        "justificativa": (
            "Alternativa correta: **B** ($R_2$). Para ser função, cada elemento do domínio deve estar associado a **no máximo um único** valor na imagem (unicidade de saída). "
            "Em $R_2$, a entrada `7` mapeia simultaneamente para `2` e para `9`, violando a definição de função.\n\n"
            "- **A, C, D) Incorretas:** Todos associam cada entrada $x$ a exatamente um $y$ (em $R_3$, várias entradas compartilharem a mesma saída `5` é perfeitamente válido em função constante)."
        ),
    },
    {
        "numero_prova": 20,
        "topico_id": 14,
        "nivel": "MEDIO",
        "enunciado": (
            "Seja o algoritmo `F(A, i, f)` abaixo tal que `A` é um vetor de inteiros e `i, f` são posições de `A` "
            "de forma que $1 \\le i \\le f \\le m$, em que $m$ é o tamanho de `A` (considerando indexação iniciando em `A[1]`).\n\n"
            "```text\n"
            "function F(A, i, f)\n"
            "  if f <= i then\n"
            "    return A[i]\n"
            "  x <- F(A, i, f - 1)\n"
            "  if x >= A[f] then\n"
            "    return x\n"
            "  return A[f]\n"
            "```\n\n"
            "Considerando a entrada `A = [3, -1, 4, 2, 1]`, `i = 1` e `f = 5`, determine o retorno de `F(A, i, f)`:"
        ),
        "alt_a": "`-1`",
        "alt_b": "`3`",
        "alt_c": "`4`",
        "alt_d": "`9`",
        "alt_e": "",
        "correta": "C",
        "justificativa": (
            "Alternativa correta: **C** (`4`). A função `F(A, i, f)` calcula recursivamente o maior elemento no subvetor `A[i..f]`:\n"
            "- `F(A, 1, 1) = A[1] = 3`\n"
            "- `F(A, 1, 2) = max(3, -1) = 3`\n"
            "- `F(A, 1, 3) = max(3, 4) = 4`\n"
            "- `F(A, 1, 4) = max(4, 2) = 4`\n"
            "- `F(A, 1, 5) = max(4, 1) =` **`4`**.\n\n"
            "- **A) Incorreta:** `-1` é o mínimo do vetor.\n"
            "- **B) Incorreta:** `3` é o elemento inicial.\n"
            "- **D) Incorreta:** `9` seria a soma `3 - 1 + 4 + 2 + 1`, não o máximo."
        ),
    },
]


def import_official_questions(db_path: pathlib.Path = DB_PATH) -> int:
    conn = sqlite3.connect(db_path)
    try:
        cols = {c[1] for c in conn.execute("PRAGMA table_info(questoes)").fetchall()}
        if "numero_prova" not in cols:
            conn.execute("ALTER TABLE questoes ADD COLUMN numero_prova INTEGER")

        now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        conn.execute("DELETE FROM questoes WHERE origem = 'PROVA_53_2025'")

        for q in OFFICIAL_QUESTIONS_2025:
            conn.execute(
                """
                INSERT INTO questoes (
                    topico_id, tipo, enunciado,
                    alt_a, alt_b, alt_c, alt_d, alt_e,
                    correta, justificativa, nivel, criado_em,
                    origem, caderno_erros, favorita, numero_prova
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    q["topico_id"],
                    "OBJETIVA",
                    q["enunciado"],
                    q["alt_a"],
                    q["alt_b"],
                    q["alt_c"],
                    q["alt_d"],
                    q["alt_e"],
                    q["correta"],
                    q["justificativa"],
                    q["nivel"],
                    now_iso,
                    "PROVA_53_2025",
                    0,
                    0,
                    q["numero_prova"],
                ),
            )
        conn.commit()
        count = conn.execute(
            "SELECT COUNT(*) FROM questoes WHERE origem = 'PROVA_53_2025'"
        ).fetchone()[0]
        return count
    finally:
        conn.close()


if __name__ == "__main__":
    total = import_official_questions()
    print(f"Imported {total} official questions (PROVA_53_2025) into {DB_PATH}")
