# Learning Record 0002: Conclusão da Fase 2 (Programação Computacional — C e Python)

- **Data:** 20 de Novembro de 2026
- **Status:** Concluído com 100% de Aproveitamento Pedagógico
- **Módulo:** Fase 2 — Programação Computacional (Anexo VII, Item 2)
- **Tópicos:** 9 a 18

## 1. O que foi Aprendido e Consolidado

### 1.1 Sintaxe, Semântica e Coerção de Tipos (Aula 09)
- **Divisão Inteira vs. Ponto Flutuante (Q10 Oficial 2025):** Em C, se ambos os operandos são inteiros (`int a = 10, b = 3`), a expressão `a / b` realiza truncamento estrito em direção a zero (`3`). A atribuição a um `float x` apenas promove o resultado truncado para `3.0`. Para obter precisão decimal, é obrigatório promover ao menos um operando via cast: `a / (float)b` resulta em `3.333333`.
- **Compilação Estática vs Interpretação Dinâmica:** Em C, checagens de tipo ocorrem no compilador; em Python, variáveis são rótulos para objetos alocados no Heap tipados dinamicamente.

### 1.2 Estruturas de Controle e Decisão (Aula 10)
- **O Fenômeno do Fallthrough no `switch-case`:** Em C/C++, esquecer a diretiva `break` faz a execução escorregar em cascata para os blocos inferiores.
- **Dangling Else:** A ambiguidade do `else` suspenso é resolvida pelo compilador ligando o `else` sempre ao `if` mais próximo ainda não fechado.
- **Curto-Circuito Lógico:** Em `A && B` (C) ou `A and B` (Python), se `A` for falso, `B` não é avaliado.

### 1.3 Estruturas de Repetição e Teste de Mesa (Aula 11)
- **Rastreamento Sistemático Multivariável (Q13 Oficial 2025):** Resolução por tabela de rastreamento com quatro variáveis (`cont`, `i`, `j`, `k`). Entendimento de que o laço interno `while(k > 0)` só itera na primeira passagem do `for`, esgotando `k` até 0. Nas iterações subsequentes, o `while` é ignorado, e `i` continua sendo recalculado até o passo final (`cont = 10, i = 15, j = 1, k = 0`).

### 1.4 Escopo e Tempo de Vida (Aula 12)
- **Segmentos da Memória:** Código (`Text`), Dados Inicializados (`Data`), Dados Não-Inicializados (`BSS`), Monte (`Heap`) e Pilha (`Stack`).
- **Modificador `static` Local em C:** Preserva o valor da variável entre invocações sucessivas da função (tempo de vida global, escopo léxico local).
- **Regra LEGB em Python:** Local $\to$ Enclosing $\to$ Global $\to$ Built-in. Uso de `global` e `nonlocal` para reatribuição.

### 1.5 Funções e Passagem de Parâmetros (Aula 13)
- **Semântica de Passagem:** C adota **estritamente passagem por valor**. Para modificar o chamador, emula-se referência passando o endereço hexadecimal (`&x`) para um ponteiro (`int *p`).
- **Pass-by-Object-Reference em Python:** Passa-se o identificador do objeto. Métodos mutadores (ex: `lista.append()`) alteram o objeto no chamador; reatribuição (`lista = [1, 2]`) apenas cria um novo vínculo local.

### 1.6 Recursividade e Call Stack (Aula 14)
- **Rastreamento de Recorrência (Q09 Oficial 2025):** Resolução bottom-up da relação $f(n) = 2f(n-1) + f(n-2)$, obtendo $f(6) = 99$.
- **Profundidade Máxima da Pilha vs Complexidade (Q05 Banco Oficial):** A pilha de execução armazena uma cadeia linear de frames em profundidade ($O(n)$ de memória), enquanto a árvore total de chamadas ramificadas atinge $O(2^n)$ de nós/tempo.
- **Stack Overflow:** Causado por ausência de caso base ou salto de condição (ex: decremento de 2 em 2 para entradas ímpares com base `n == 0`).

### 1.7 Vetores e Ponteiros (Aula 15)
- **Organização Contígua:** Fórmula física $\text{endereço}(v[i]) = \text{base} + i \times \text{sizeof}(T)$.
- **Decaimento e Aritmética:** O identificador $v$ decai para $\&v[0]$. Consequentemente, $v[i] \equiv *(v + i) \equiv i[v]$.
- **Proteção de Acesso à Memória (Q14 Oficial 2025):** Mecanismo de tratamento de exceções (Exception Handling) para interceptar acessos fora de limites ou ponteiros inválidos.

### 1.8 Manipulação de Strings (Aula 16)
- **O Sentinela `\0` em C:** Caractere nulo (ASCII 0) delimitador obrigatório. Diferença crucial: `strlen()` conta caracteres úteis ($O(n)$), `sizeof()` retorna a capacidade total do buffer ($O(1)$).
- **Comparação:** `s1 == s2` compara endereços de memória dos ponteiros. O conteúdo deve ser comparado via `strcmp()`.
- **Strings em Python:** Objetos imutáveis com fatiamento indexado `s[start:stop:step]` e suporte a passos negativos.

### 1.9 Programação Orientada a Objetos (Aula 17)
- **Classes, Objetos e Construtores:** Moldes no código vs instâncias alocadas no Heap. O método `__init__` em Python e construtores de C++/Java sem tipo de retorno.
- **Atributos de Classe vs Instância:** A armadilha de atributos mutáveis compartilhados em Python.
- **Coleções da Biblioteca Padrão (Q15 Oficial 2025):** Identificação e propriedades do **Deque** (fila de duas pontas com inserções e remoções restritas às extremidades em tempo $O(1)$).

### 1.10 POO Avançada: Encapsulamento, Herança e Polimorfismo (Aula 18)
- **Encapsulamento e Name Mangling:** `public`, `protected` e `private` em C++/Java versus convenções e o mangling `_Classe__atributo` em Python.
- **O Parâmetro `self` vs `this`:** Invocação explícita na definição em Python (`Classe.metodo(obj, x)`) vs ponteiro implícito no registrador em C++.
- **Dynamic Dispatch e VTable:** Ponteiro `vptr` em cada instância que referencia a tabela de métodos virtuais para despacho polimórfico $O(1)$.
- **MRO (Method Resolution Order):** Resolução do problema do diamante em Python via algoritmo C3 Linearization.

---

## 2. Inventário de Aulas da Fase 2 (100% Concluídas)
- [0009-sintaxe-semantica-c-python.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0009-sintaxe-semantica-c-python.html)
- [0010-estruturas-de-controle.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0010-estruturas-de-controle.html)
- [0011-estruturas-de-repeticao.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0011-estruturas-de-repeticao.html)
- [0012-escopo-e-tempo-de-vida.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0012-escopo-e-tempo-de-vida.html)
- [0013-funcoes-e-passagem-parametros.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0013-funcoes-e-passagem-parametros.html)
- [0014-recursividade-e-call-stack.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0014-recursividade-e-call-stack.html)
- [0015-manipulacao-de-vetores-e-ponteiros.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0015-manipulacao-de-vetores-e-ponteiros.html)
- [0016-manipulacao-de-strings.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0016-manipulacao-de-strings.html)
- [0017-programacao-orientada-a-objetos.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0017-programacao-orientada-a-objetos.html)
- [0018-poo-avancada-encapsulamento-heranca.html](file:///c:/Users/Lucas-Galdino/PPGCC/lessons/0018-poo-avancada-encapsulamento-heranca.html)

---

## 3. Próximo Passo
Avançar para a **Fase 3: Algoritmos e Estrutura de Dados (Coração do Edital — Tópicos 19 a 27)**:
- Tópicos 19 a 27:
  19. Notação Assintótica ($O$, $\Omega$, $\Theta$) e Ordens de Grandeza
  20. Análise de Complexidade de Pior Caso, Médio e Melhor Caso
  21. Teorema Mestre e Resolução de Recorrências ($T(n) = aT(n/b) + f(n)$)
  22. Estruturas Lineares: Listas Encadeadas (Simples, Dupla, Circular)
  23. Pilhas (LIFO) e Filas (FIFO) — Implementação e Aplicações
  24. Árvores Binárias de Busca (BST) e Percursos (Pré-ordem, Em-ordem, Pós-ordem)
  25. Balanceamento de Árvores (Conceito de Árvores AVL e Rubro-Negras)
  26. Algoritmos de Ordenação I: Quadráticos ($O(n^2)$ — Bubble, Insertion, Selection)
  27. Algoritmos de Ordenação II: Eficientes ($O(n \log n)$ — MergeSort, QuickSort, HeapSort)
