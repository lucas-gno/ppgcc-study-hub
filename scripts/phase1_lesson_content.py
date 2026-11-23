# -*- coding: utf-8 -*-
"""
Phase 1 Lesson Content & Active Retrieval Data Dictionary.
Contains the comprehensive pedagogical text and interactive retention questions
for Topics 01 through 08.
"""

TOPIC_1_DATA = {
    "title": "Teoria dos Conjuntos — A Base Ontológica da Computação",
    "subtitle": "Como organizar dados no vácuo: pertinência, inclusão, partes e a quebra da simetria no produto cartesiano.",
    "philosophy_title": "Da Filosofia à Lógica das Sacolas: O Pensamento Extensional",
    "philosophy_text": """
No cotidiano da computação, manipulamos objetos, variáveis e estruturas de rede. Mas onde essas coisas vivem matematicamente?
No século XIX, matemáticos como Georg Cantor e Gottlob Frege perceberam algo fascinante: <strong>podemos definir qualquer entidade matemática apenas agrupando elementos dentro de uma coleção</strong>.
Na visão extensional da lógica, um conjunto não tem sentimentos nem segredos psicológicos: ele é única e exclusivamente definido pelos elementos que residem dentro dele.
Se dois conjuntos possuem exatamente os mesmos elementos, eles são o mesmo conjunto — não importa a ordem nem se você repetiu o mesmo elemento mil vezes.
""",
    "word_breakdowns": [
        {
            "term": "Extensionalidade",
            "pronunciation": "ex-ten-si-o-na-li-da-de",
            "etymology": "Do latim 'extensio' (aquilo que se estende, lista explícita dos componentes).",
            "plain_meaning": "Dois conjuntos são idênticos se têm os mesmos elementos. Exemplo: {1, 2} é rigorosamente idêntico a {2, 1, 1, 1}.",
        },
        {
            "term": "Cardinalidade",
            "pronunciation": "car-di-na-li-da-de",
            "etymology": "Do latim 'cardo' (ponto de apoio, medida fundamental de contagem).",
            "plain_meaning": "O número total de elementos únicos dentro de um conjunto. Denota-se por |A| ou #(A).",
        },
        {
            "term": "Conjunto das Partes",
            "pronunciation": "con-jun-to das par-tes",
            "etymology": "Em inglês 'Power Set' (Conjunto Potência). Denotado por P(A) ou 2^A.",
            "plain_meaning": "A coleção de todas as combinações de subgrupos possíveis que você pode formar com os elementos de A.",
        },
    ],
    "formulas": [
        {
            "latex": "x \\in A \\quad \\text{vs} \\quad S \\subseteq A",
            "spoken": "x pertence ao conjunto A; S está contido no conjunto A",
            "meaning": "Pertinência (\\in) conecta um ÚNICO elemento ao conjunto. Inclusão (\\subseteq) conecta uma SACOLA inteira a outra sacola maior.",
        },
        {
            "latex": "\\forall A, \\quad \\emptyset \\subseteq A",
            "spoken": "Para todo conjunto A, o conjunto vazio está contido em A",
            "meaning": "O conjunto vazio não possui elementos. Para violar a inclusão, teria que existir alguém no vazio fora de A; como o vazio não tem ninguém, a condição é satisfeita por vacuidade (truth by vacuity).",
        },
        {
            "latex": "|\\mathcal{P}(A)| = 2^{|A|}",
            "spoken": "A cardinalidade do conjunto das partes de A é dois elevado ao número de elementos de A",
            "meaning": "Cada elemento tem duas escolhas binárias independentes: entrar no subconjunto (bit 1) ou ficar de fora (bit 0). Para n elementos, temos 2 x 2 x ... x 2 = 2^n combinações.",
        },
        {
            "latex": "(A \\cup B)^c = A^c \\cap B^c \\quad \\text{e} \\quad (A \\cap B)^c = A^c \\cup B^c",
            "spoken": "O complementar da união de A com B é a interseção do complementar de A com o complementar de B",
            "meaning": "Leis de De Morgan: dizer 'não é verdade que gosto de café OU chá' equivale exatamente a dizer 'NÃO gosto de café E NÃO gosto de chá'.",
        },
        {
            "latex": "A \\times B = \\{ (a, b) \\mid a \\in A \\land b \\in B \\}",
            "spoken": "O produto cartesiano de A por B é o conjunto dos pares ordenados (a, b) onde a pertence a A e b pertence a B",
            "meaning": "O espaço de todas as combinações concebíveis entre dois mundos. Em SQL, é o CROSS JOIN puro de duas tabelas. Cardinalidade total: |A x B| = |A| . |B|.",
        },
    ],
    "computation_title": "Como a Computação Usa Conjuntos: Bancos Relacionais e Tipos",
    "computation_text": """
Toda a teoria de Bancos de Dados Relacionais (inventada por Edgar Codd na IBM em 1970) é uma aplicação direta da Teoria dos Conjuntos:
- Uma tabela SQL é um conjunto (ou multiconjunto) de tuplas;
- Um <code>CROSS JOIN</code> é exatamente o <strong>Produto Cartesiano</strong> $A \\times B$;
- A cláusula <code>WHERE</code> funciona como o operador de compreensão formal $\\{ x \\in U \\mid P(x) \\}$;
- Uma tabela de junção N:N em banco de dados nada mais é do que um <strong>subconjunto</strong> do produto cartesiano: $R \\subseteq A \\times B$.
""",
    "traps": [
        {
            "title": "Confundir Elemento com Subconjunto",
            "text": "Se $A = \\{1, 2\\}$, então $1 \\in A$ é VERDADEIRO, mas $\\{1\\} \\in A$ é FALSO! O subconjunto $\\{1\\}$ está CONTIDO em $A$ ($\\{1\\} \\subseteq A$), mas não é um elemento solto dentro dele.",
        },
        {
            "title": "O Vazio como Subconjunto vs como Elemento",
            "text": "Para qualquer conjunto $A$, $\\emptyset \\subseteq A$ é sempre verdadeiro. Mas $\\emptyset \\in A$ só é verdadeiro se alguém tiver explicitamente colocado o símbolo $\\emptyset$ dentro das chaves de $A$, como em $A = \\{\\emptyset, 1\\}$.",
        },
    ],
    "questions": [
        {
            "question": "Seja o conjunto A = {a, b, c}. Quantos subconjuntos distintos possui o conjunto das partes P(A)?",
            "options": {
                "A": "3 subconjuntos.",
                "B": "6 subconjuntos.",
                "C": "8 subconjuntos.",
                "D": "9 subconjuntos.",
            },
            "correct": "C",
            "correct_fb": "Exato! Como o conjunto possui 3 elementos (|A| = 3), o número total de subconjuntos possíveis no conjunto das partes é dado pela fórmula das escolhas binárias: 2^|A| = 2^3 = 8 subconjuntos.",
            "incorrect_fb": "Cuidado! Não multiplique 3 por 2 nem eleve 3 ao quadrado. O número de subconjuntos de um conjunto com n elementos é 2^n. Para 3 elementos: 2^3 = 8 subconjuntos.",
        },
        {
            "question": "Considere o conjunto S = {1, {2}}. Qual das seguintes afirmações é estritamente verdadeira?",
            "options": {
                "A": "{2} é subconjunto de S ({2} ⊆ S).",
                "B": "{2} é elemento de S ({2} ∈ S).",
                "C": "2 é elemento de S (2 ∈ S).",
                "D": "O conjunto vazio não é subconjunto de S (∅ ⊄ S).",
            },
            "correct": "B",
            "correct_fb": "Perfeito! O objeto {2} está literalmente listado dentro das chaves de S, logo ele atua como um ELEMENTO ({2} ∈ S). Para que 2 pertencesse a S, o número 2 teria que estar desempacotado.",
            "incorrect_fb": "Pegadinha clássica de banca! Repare que {2} está dentro de S como um bloco empacotado. Portanto, {2} é um elemento de S ({2} ∈ S). O número 2 puro não pertence a S, e o conjunto vazio é subconjunto de todo conjunto.",
        },
        {
            "question": "Sejam os conjuntos A = {1, 2} e B = {3, 4, 5}. Qual é o número de pares ordenados do produto cartesiano A x B e qual o valor da afirmação A x B = B x A?",
            "options": {
                "A": "6 pares, e A x B é idêntico a B x A pela propriedade comutativa.",
                "B": "5 pares, e a comutatividade falha pois pares têm direcionalidade.",
                "C": "6 pares, e A x B é diferente de B x A pois a ordem das coordenadas importa.",
                "D": "8 pares, e os produtos são idênticos apenas se A e B forem disjuntos.",
            },
            "correct": "C",
            "correct_fb": "Excelente! O produto cartesiano possui |A| . |B| = 2 . 3 = 6 pares. Além disso, (1, 3) ∈ A x B, mas (1, 3) ∉ B x A (o par em B x A seria (3, 1)). Como pares têm ordem, a comutatividade falha!",
            "incorrect_fb": "Atenção: |A x B| = 2 . 3 = 6 pares. E no par ordenado, a ordem importa: (1, 3) ≠ (3, 1). Logo, A x B ≠ B x A a menos que A = B ou um deles seja vazio.",
        },
        {
            "question": "Pela Primeira Lei de De Morgan para conjuntos, a expressão (A ∪ B)^c equivale exatamente a:",
            "options": {
                "A": "A^c ∪ B^c",
                "B": "A^c ∩ B^c",
                "C": "(A ∩ B)^c",
                "D": "A^c \\ B^c",
            },
            "correct": "B",
            "correct_fb": "Correto! O complementar da união vira a interseção dos complementares: (A ∪ B)^c = A^c ∩ B^c. O 'OU' se transforma em 'E' ao ser negado.",
            "incorrect_fb": "Incorreto. Lembre-se da regra de ouro de De Morgan: ao distribuir o complementar, a união (∪) inverte e se transforma em interseção (∩): (A ∪ B)^c = A^c ∩ B^c.",
        },
    ],
    "next_step": "Dominada a fundação das sacolas de dados e do produto cartesiano, agora daremos o passo definitivo: filtrar esse espaço de possibilidades para criar vínculos entre entidades — as Relações Binárias!",
}

TOPIC_2_DATA = {
    "title": "Relações Binárias — Da Filosofia à Computação",
    "subtitle": "A transição ontológica: como o pensamento lógico se converte em arestas de dígrafos e matrizes booleanas.",
    "philosophy_title": "Da Filosofia para a Lógica Extensional: O Predicado Diádico",
    "philosophy_text": """
Na lógica tradicional de Aristóteles, o foco era quase exclusivo em propriedades individuais: <em>'Sócrates é mortal'</em> ($M(s)$).
Mas quando queremos modelar sistemas de computação, quase nunca lidamos com objetos isolados.
Lidamos com conexões: <em>'O pacote A foi enviado para o nó B'</em>, <em>'O processo 1042 é pai do processo 1088'</em>, ou <em>'O usuário u tem permissão no arquivo f'</em>.
Esses vínculos são chamados de <strong>predicados diádicos</strong> (ou relações binárias).
Para Gottlob Frege e Bertrand Russell, uma relação binária não é um mistério psicológico:
ela é simplesmente o <strong>conjunto de todos os pares ordenados</strong> de entidades para as quais o vínculo de fato existe.
""",
    "word_breakdowns": [
        {
            "term": "Par Ordenado",
            "pronunciation": "par or-de-na-do",
            "etymology": "Do latim 'ordo' (fileira com direção e posição definida).",
            "plain_meaning": "Uma tupla de dois itens onde a ordem importa: (a, b) significa que a é a origem e b é o destino. (a, b) só é igual a (b, a) se a = b.",
        },
        {
            "term": "Relação Binária",
            "pronunciation": "re-la-ção bi-ná-ri-a",
            "etymology": "Do latim 'relatio' (levar de volta, vincular) e 'bis' (dois a dois).",
            "plain_meaning": "Qualquer subconjunto do produto cartesiano: R ⊆ A x B. Se o par (x, y) está em R, eles estão conectados; se não está, não há vínculo.",
        },
        {
            "term": "Matriz Booleana de Adjacência",
            "pronunciation": "ma-triz bo-o-le-a-na de ad-ja-cên-ci-a",
            "etymology": "Em homenagem a George Boole (0 e 1) e adjacência (estar ao lado, conectado).",
            "plain_meaning": "Uma tabela quadrada onde linhas são as origens, colunas são os destinos. Célula = 1 se há aresta; 0 se não há.",
        },
    ],
    "formulas": [
        {
            "latex": "(a, b) = (c, d) \\iff a = c \\land b = d",
            "spoken": "O par ordenado (a, b) é igual ao par (c, d) se, e somente se, a for igual a c e b for igual a d",
            "meaning": "Axioma Fundamental do Par Ordenado: para que dois pares sejam idênticos, as primeiras coordenadas devem ser iguais e as segundas coordenadas também.",
        },
        {
            "latex": "R \\subseteq A \\times B",
            "spoken": "R está contido em A vezes B (R é uma relação binária de A em B)",
            "meaning": "Definição canônica: qualquer subconjunto do produto cartesiano é uma relação válida. Pode ser vazia, total ou intermediária.",
        },
        {
            "latex": "\\text{Total de Relações Possíveis} = 2^{|A \\times B|} = 2^{|A| \\cdot |B|}",
            "spoken": "Total de relações é dois elevado ao número de elementos de A vezes o número de elementos de B",
            "meaning": "Fórmula de contagem oficial da banca (Questão 17 do Edital 53/2025): como há |A| . |B| pares e cada par pode estar presente (1) ou ausente (0), há 2^(|A|.|B|) relações possíveis.",
        },
    ],
    "computation_title": "Dígrafos e Matrizes: Como o Computador Enxerga Vínculos",
    "computation_text": """
Quando uma relação vincula elementos de um conjunto com ele mesmo ($R \\subseteq A \\times A$), ela é chamada de <strong>relação homogênea</strong>.
O computador armazena e processa relações homogêneas por duas representações idênticas:
1. <strong>Grafo Direcionado (Dígrafo):</strong> Os elementos de $A$ são os nós (vértices). Se $(x, y) \\in R$, desenha-se uma flecha saindo de $x$ e apontando para $y$. Se $(x, x) \\in R$, a flecha sai de $x$ e volta para $x$ (um <em>laço</em>).
2. <strong>Matriz Booleana ($M_R$):</strong> Grade $n \\times n$. A diagonal principal $M[i, i]$ indica a presença de laços.
""",
    "traps": [
        {
            "title": "Confundir Número de Pares com Número de Relações",
            "text": "Se $|A| = 3$, o produto cartesiano $A \\times A$ possui $3 \\times 3 = 9$ pares ordenados. Mas o número de RELAÇÕES distintas possíveis NÃO É 9: é $2^9 = 512$ relações! Uma relação é QUALQUER subconjunto dos pares.",
        },
    ],
    "questions": [
        {
            "question": "Sejam A = {1, 2} e B = {x, y}. Qual dos seguintes conjuntos NÃO representa uma relação binária válida de A em B?",
            "options": {
                "A": "R = ∅",
                "B": "R = {(1, x), (2, y)}",
                "C": "R = {(1, x), (x, 1)}",
                "D": "R = {(1, x), (1, y), (2, x), (2, y)}",
            },
            "correct": "C",
            "correct_fb": "Exato! Em uma relação de A em B, o primeiro elemento do par DEVE pertencer a A ({1, 2}) e o segundo DEVE pertencer a B ({x, y}). O par (x, 1) tem x na primeira posição, violando a definição de A x B!",
            "incorrect_fb": "Atenção: uma relação de A em B só pode conter pares onde a primeira coordenada vem de A e a segunda vem de B. O par (x, 1) inverteu a ordem, pertencendo a B x A, não a A x B.",
        },
        {
            "question": "Seja o conjunto S = {1, 2, 3}. Quantas relações binárias homogêneas distintas podem ser definidas sobre S?",
            "options": {
                "A": "9 relações.",
                "B": "27 relações.",
                "C": "512 relações.",
                "D": "1024 relações.",
            },
            "correct": "C",
            "correct_fb": "Perfeito! O produto cartesiano S x S possui 3 x 3 = 9 pares ordenados. Como qualquer subconjunto desse espaço é uma relação, o total de relações é a cardinalidade das partes: 2^9 = 512 relações distintas.",
            "incorrect_fb": "Cuidado com o cálculo: 9 é apenas a quantidade de pares ordenados. O número de relações possíveis é 2 elevado ao total de pares: 2^(3 x 3) = 2^9 = 512.",
        },
        {
            "question": "Seja a relação R = {(1, 4), (2, 3), (3, 2), (4, 1)} sobre o conjunto A = {1, 2, 3, 4}. Qual é o Domínio dom(R) e a Imagem img(R)?",
            "options": {
                "A": "dom(R) = {1, 2} e img(R) = {3, 4}",
                "B": "dom(R) = {1, 2, 3, 4} e img(R) = {1, 2, 3, 4}",
                "C": "dom(R) = {4, 3, 2, 1} e img(R) = {5}",
                "D": "dom(R) = ∅ e img(R) = A x A",
            },
            "correct": "B",
            "correct_fb": "Excelente! O Domínio é o conjunto das primeiras coordenadas: {1, 2, 3, 4}. A Imagem é o conjunto das segundas coordenadas: {4, 3, 2, 1} = {1, 2, 3, 4}. Ambos coincidem com o conjunto A inteiro!",
            "incorrect_fb": "Incorreto. O Domínio reúne todos os elementos que aparecem como primeiro item do par (1, 2, 3, 4) e a Imagem reúne os que aparecem como segundo item (4, 3, 2, 1). Ambos são iguais a {1, 2, 3, 4}.",
        },
        {
            "question": "Em uma matriz booleana de adjacência M_R de dimensão n x n, o que indica quando TODOS os elementos da diagonal principal são iguais a 1 (M[i, i] = 1 para todo i)?",
            "options": {
                "A": "Que a relação é simétrica.",
                "B": "Que todo vértice do dígrafo possui um laço apontando para si mesmo (relação reflexiva).",
                "C": "Que o grafo não possui ciclos.",
                "D": "Que a relação é vazia.",
            },
            "correct": "B",
            "correct_fb": "Brilhante! O elemento M[i, i] representa o par (i, i). Se todos são 1, significa que todo elemento possui um laço apontando para si mesmo no dígrafo. Essa é a definição exata de Reflexividade!",
            "incorrect_fb": "Incorreto. A diagonal principal M[i, i] conecta o vértice i a ele próprio: (i, i). Ter 1 em toda a diagonal significa que todo nó tem um laço, o que caracteriza a Reflexividade.",
        },
    ],
    "next_step": "Agora que sabemos que relações são dígrafos e matrizes, analisaremos os padrões que governam esses vínculos: reflexividade, simetria, antissimetria e transitividade nas Propriedades das Relações!",
}

TOPIC_3_DATA = {
    "title": "Propriedades das Relações Binárias — O DNA Estrutural dos Vínculos",
    "subtitle": "Reflexividade, simetria, antissimetria, transitividade, fechos e o algoritmo de Warshall.",
    "philosophy_title": "O DNA Estrutural: Reconhecendo Padrões nas Redes",
    "philosophy_text": """
Quando analisamos uma rede social, um sistema de arquivos ou uma malha de roteadores, não queremos apenas saber quais conexões existem: queremos entender a <strong>natureza</strong> dessas conexões.
- A conexão é mútua ou de mão única?
- Se você pode ir de A para B e de B para C, consegue cortar caminho direto de A para C?
- Todo mundo está conectado a si mesmo?
Na Lógica Matemática e na Ciência da Computação, essas quatro perguntas recebem os nomes de <strong>Reflexividade, Simetria, Antissimetria e Transitividade</strong>.
Elas são o DNA que define se uma relação servirá para agrupar coisas iguais (equivalência) ou para ranquear coisas de cima a baixo (ordem).
""",
    "word_breakdowns": [
        {
            "term": "Reflexividade",
            "pronunciation": "re-fle-xi-vi-da-de",
            "etymology": "Do latim 'reflectere' (dobrar para trás, olhar para o espelho).",
            "plain_meaning": "Todo elemento conecta-se consigo mesmo. No dígrafo, todo nó tem um laço. Na matriz, a diagonal principal é toda 1.",
        },
        {
            "term": "Antissimetria",
            "pronunciation": "an-ti-si-me-tri-a",
            "etymology": "Anti (oposição ao retorno mútuo) + simetria (medida mútua).",
            "plain_meaning": "Se x conecta em y e x ≠ y, é PROIBIDO y conectar de volta em x! É uma rua de mão única estrita entre cidades diferentes.",
        },
        {
            "term": "Transitividade",
            "pronunciation": "tran-si-ti-vi-da-de",
            "etymology": "Do latim 'transire' (passar através, fazer a ponte).",
            "plain_meaning": "Se há caminho de dois passos (x → y → z), obrigatoriamente existe o atalho de um passo só (x → z).",
        },
    ],
    "formulas": [
        {
            "latex": "\\forall x \\in A, \\quad (x, x) \\in R",
            "spoken": "Para todo x pertencente a A, o par (x, x) pertence a R",
            "meaning": "Definição formal de Reflexividade. Exemplo real: a igualdade (=) e a inclusão de conjuntos (A ⊆ A) são sempre reflexivas.",
        },
        {
            "latex": "\\forall x, y \\in A, \\quad (x, y) \\in R \\implies (y, x) \\in R",
            "spoken": "Para todo x e y em A, se (x, y) está em R, então (y, x) também está em R",
            "meaning": "Definição formal de Simetria. Toda rua é de mão dupla. A matriz de adjacência é simétrica em relação à diagonal principal (M = M^T).",
        },
        {
            "latex": "\\forall x, y \\in A, \\quad (x, y) \\in R \\land (y, x) \\in R \\implies x = y",
            "spoken": "Para todo x e y, se (x, y) está em R e (y, x) está em R, então x obrigatoriamente é igual a y",
            "meaning": "Definição formal de Antissimetria. Só é permitida ida e volta se o ponto de partida e chegada forem o mesmo nó (laço próprio). Entre nós distintos, o retorno mútuo é vetado.",
        },
        {
            "latex": "\\forall x, y, z \\in A, \\quad (x, y) \\in R \\land (y, z) \\in R \\implies (x, z) \\in R",
            "spoken": "Para quaisquer x, y e z, se (x, y) está em R e (y, z) está em R, então (x, z) também está em R",
            "meaning": "Definição formal de Transitividade. Se há escala por y, o voo direto x -> z tem que existir na relação.",
        },
        {
            "latex": "W_k[i, j] = W_{k-1}[i, j] \\lor (W_{k-1}[i, k] \\land W_{k-1}[k, j])",
            "spoken": "O fecho transitivo no passo k conecta i a j se já havia conexão anterior ou se existe caminho passando pelo pivô intermediário k",
            "meaning": "A regra mestre do Algoritmo de Warshall: calcula o fecho transitivo em tempo O(n^3) testando sistematicamente cada vértice k como intermediário.",
        },
    ],
    "computation_title": "Fechos de Relações e o Algoritmo de Warshall",
    "computation_text": """
Quando uma relação não possui uma propriedade desejada, podemos 'completá-la' adicionando a quantidade mínima necessária de pares:
- <strong>Fecho Reflexivo ($R \\cup I$):</strong> Adiciona todos os laços faltantes na diagonal principal;
- <strong>Fecho Simétrico ($R \\cup R^{-1}$):</strong> Adiciona a volta para cada ida que existir;
- <strong>Fecho Transitivo ($R^+$):</strong> Adiciona todos os atalhos indiretos de qualquer comprimento.
O <strong>Algoritmo de Warshall</strong> calcula o fecho transitivo operando sobre matrizes booleanas em três laços aninhados (<code>for k, for i, for j</code>), sendo a base dos algoritmos de alcance em grafos (reachability).
""",
    "traps": [
        {
            "title": "Antissimétrica NÃO é o oposto de Simétrica!",
            "text": "Uma relação pode ser SIMÉTRICA E ANTISSIMÉTRICA ao mesmo tempo! Por exemplo: $R = \\{(1,1), (2,2)\\}$ é simétrica (toda ida tem volta) e é antissimétrica (nunca há volta entre nós distintos). Além disso, uma relação pode não ser nenhuma das duas!",
        },
        {
            "title": "Não-Reflexiva vs Irreflexiva",
            "text": "Irreflexiva exige que NENHUM nó tenha laço ($\\\\forall x, (x,x) \\\\notin R$). Se uma relação tem 3 nós e 2 têm laço mas 1 não tem, ela é <em>não-reflexiva</em> (pois falhou para um), mas NÃO é irreflexiva (pois teve laços).",
        },
    ],
    "questions": [
        {
            "question": "Seja o conjunto A = {1, 2, 3} e a relação R = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}. Quais propriedades R satisfaz?",
            "options": {
                "A": "Apenas simétrica e transitiva, mas não reflexiva.",
                "B": "Reflexiva e simétrica, mas não transitiva.",
                "C": "Reflexiva, simétrica e transitiva.",
                "D": "Antissimétrica e irreflexiva.",
            },
            "correct": "C",
            "correct_fb": "Exato! 1. Reflexiva: (1,1), (2,2) e (3,3) estão todos presentes. 2. Simétrica: (1,2) tem o seu inverso (2,1). 3. Transitiva: a composição de (1,2) com (2,1) dá (1,1) e de (2,1) com (1,2) dá (2,2), ambos presentes. Satisfaz as três!",
            "incorrect_fb": "Verifique com calma: todos os nós têm laço ((1,1), (2,2), (3,3)), logo é reflexiva. O único par assimétrico aparente é (1,2), mas (2,1) está lá, logo é simétrica. E as composições estão satisfeitas, sendo transitiva.",
        },
        {
            "question": "A relação clássica de divisibilidade 'x divide y' (x | y) sobre o conjunto dos inteiros positivos Z+ é:",
            "options": {
                "A": "Simétrica, pois se x divide y, então y divide x.",
                "B": "Antissimétrica, pois se x divide y e y divide x entre inteiros positivos, obrigatoriamente x = y.",
                "C": "Irreflexiva, pois nenhum número divide a si mesmo.",
                "D": "Não-transitiva, pois a divisibilidade se perde após dois passos.",
            },
            "correct": "B",
            "correct_fb": "Perfeito! Se x divide y e y divide x em inteiros positivos, a única possibilidade aritmética é x = y (ex: 2 divide 4, mas 4 NÃO divide 2). Isso é a essência pura da Antissimetria!",
            "incorrect_fb": "Atenção: divisibilidade é reflexiva (x divide x) e transitiva (se x divide y e y divide z, x divide z). E se x divide y e y divide x em inteiros positivos, x = y, logo ela é ANTISSIMÉTRICA.",
        },
        {
            "question": "Se o dígrafo de uma relação homogênea sobre 3 nós contém as arestas (1, 2) e (2, 3), qual aresta mínima DEVE ser acrescentada para formar o Fecho Transitivo da relação?",
            "options": {
                "A": "Aresta (3, 1).",
                "B": "Aresta (2, 1).",
                "C": "Aresta (1, 3).",
                "D": "Arestas (1, 1) e (3, 3).",
            },
            "correct": "C",
            "correct_fb": "Excelente! O fecho transitivo exige o atalho direto do início ao fim do caminho de dois passos: de 1 vai para 2, de 2 vai para 3, logo deve existir obrigatoriamente a aresta (1, 3).",
            "incorrect_fb": "Incorreto. Transitividade diz: se (1, 2) e (2, 3) existem, o atalho de 1 direto para 3 deve existir: (1, 3). O par (3, 1) criaria um ciclo, e (2, 1) seria a volta simétrica.",
        },
        {
            "question": "No Algoritmo de Warshall, qual é o papel da variável pivô k na iteração externa?",
            "options": {
                "A": "Serve apenas como contador de laços sem significado geométrico.",
                "B": "Indica que estamos verificando se existe um caminho de i até j usando apenas vértices do subconjunto {1, 2, ..., k} como intermediários.",
                "C": "Calcula a transposta da matriz booleana.",
                "D": "Remove os laços reflexivos da diagonal principal.",
            },
            "correct": "B",
            "correct_fb": "Brilhante! Essa é a essência da Programação Dinâmica de Warshall: na etapa k, W_k[i, j] é 1 se e somente se existe um caminho de i até j cujos nós intermediários pertencem a {1, ..., k}.",
            "incorrect_fb": "Incorreto. O algoritmo de Warshall constrói a conectividade incrementalmente: no passo k, ele permite que o vértice k seja usado como ponte entre qualquer i e j.",
        },
    ],
    "next_step": "Com o domínio de reflexividade, simetria e transitividade, você acabou de desbloquear a ferramenta mais poderosa de agrupamento matemático: as Relações de Equivalência!",
}

TOPIC_4_DATA = {
    "title": "Relações de Equivalência — A Tríade da Agrupabilidade Perfeita",
    "subtitle": "Reflexiva + Simétrica + Transitiva: o critério universal para classificar e agrupar sem ambiguidades.",
    "philosophy_title": "A Busca pela Igualdade Subjetiva: Classificar sem Excluir",
    "philosophy_text": """
No mundo real, duas coisas quase nunca são estritamente idênticas.
Duas pessoas têm CPFs diferentes, dois pacotes IP têm números de sequência diferentes, duas cadeias de caracteres têm endereços de memória diferentes.
No entanto, quando queremos classificar, dizemos: <em>'Para o meu propósito, essas duas coisas são equivalentes'</em>.
Por exemplo: na arquitetura de contêineres, duas instâncias de microsserviço que consomem menos de 200MB de RAM podem pertencer à mesma classe de agendamento de recursos.
A matemática formalizou essa ideia através da <strong>Relação de Equivalência</strong>:
uma relação que se comporta exatamente como a igualdade clássica ($=$), mas relaxada para qualquer critério que respeite a <strong>Tríade Sagrada: Reflexiva + Simétrica + Transitiva</strong>.
""",
    "word_breakdowns": [
        {
            "term": "Equivalência",
            "pronunciation": "e-qui-va-lên-ci-a",
            "etymology": "Do latim 'aequus' (igual) + 'valere' (ter o mesmo valor, mesmo peso).",
            "plain_meaning": "Uma relação que agrupa elementos que compartilham a mesma propriedade fundamental. Denota-se pelo til (~) ou por ≡.",
        },
        {
            "term": "Congruência Modular",
            "pronunciation": "con-gru-ên-ci-a mo-du-lar",
            "etymology": "Do latim 'congruere' (concordar, coincidir no mesmo ponto).",
            "plain_meaning": "Dois números inteiros são congruentes módulo n se deixam rigorosamente o mesmo resto ao serem divididos por n. É a aritmética dos relógios!",
        },
    ],
    "formulas": [
        {
            "latex": "R \\text{ é de Equivalência} \\iff R \\text{ é Reflexiva, Simétrica e Transitiva (RST)}",
            "spoken": "R é uma relação de equivalência se, e somente se, R for reflexiva, simétrica e transitiva",
            "meaning": "Os 3 Pilares Indispensáveis. Se falhar em apenas um deles, a relação perde a capacidade de criar agrupamentos perfeitos.",
        },
        {
            "latex": "a \\equiv b \\pmod{n} \\iff n \\mid (a - b)",
            "spoken": "a é congruente a b módulo n se, e somente se, n divide a diferença a menos b",
            "meaning": "A fórmula do relógio de 12 horas: 21 horas e 9 horas da noite apontam para o mesmo número porque 12 divide (21 - 9 = 12). Deixam o mesmo resto 9 ao dividir por 12.",
        },
        {
            "latex": "|x| = |y| \\implies x \\sim y",
            "spoken": "Se o valor absoluto de x é igual ao valor absoluto de y, então x é equivalente a y",
            "meaning": "A clássica Questão 18 do Concurso IFCE 2025: números como -5 e +5 são equivalentes porque ambos possuem a mesma distância até a origem (módulo 5).",
        },
    ],
    "computation_title": "Aplicações em Computação: Hashing, Compiladores e Redes",
    "computation_text": """
As relações de equivalência são o alicerce de otimizações críticas em infraestrutura e computação:
1. <strong>Tabelas Hash:</strong> A função hash $h(k) = k \\bmod m$ particiona o universo de chaves em classes de equivalência (os <em>buckets</em>);
2. <strong>Compiladores:</strong> Otimização de código identifica 'expressões comuns' e substitui variáveis equivalentes por um único registrador;
3. <strong>Sub-redes IPv4/IPv6:</strong> A máscara de sub-rede (ex: <code>/24</code>) define uma relação de equivalência: dois IPs são equivalentes se pertencem ao mesmo domínio de broadcast.
""",
    "traps": [
        {
            "title": "A Armadilha do Quase-Igual (Tolerância Não é Equivalência!)",
            "text": "Se definirmos a relação 'x e y têm quase a mesma altura' ($|x - y| \\le 2\\text{cm}$), ela é reflexiva e simétrica, mas NÃO É TRANSITIVA! João tem quase a mesma altura de Pedro (2cm), Pedro de Lucas (2cm), mas João e Lucas diferem por 4cm e não são mais parentes. Sem transitividade, NÃO É equivalência!",
        },
    ],
    "questions": [
        {
            "question": "Para que uma relação binária R sobre um conjunto A seja classificada formalmente como Relação de Equivalência, quais propriedades ela DEVE satisfazer obrigatoriamente?",
            "options": {
                "A": "Reflexiva, antissimétrica e transitiva.",
                "B": "Irreflexiva, simétrica e transitiva.",
                "C": "Reflexiva, simétrica e transitiva.",
                "D": "Reflexiva, simétrica e não-transitiva.",
            },
            "correct": "C",
            "correct_fb": "Exato! A Tríade Sagrada da Equivalência é sempre: Reflexiva (olhar no espelho), Simétrica (mão dupla mútua) e Transitiva (atalhos garantidos). A sigla mnemônica é RST!",
            "incorrect_fb": "Cuidado: a tríade é Reflexiva + Simétrica + Transitiva (RST). Se for antissimétrica em vez de simétrica, vira uma relação de ordem (Poset), que estudaremos adiante.",
        },
        {
            "question": "Na aritmética modular Z, por que podemos afirmar com certeza matemática que 25 ≡ 9 (mod 8)?",
            "options": {
                "A": "Porque 25 e 9 são números ímpares maiores que 8.",
                "B": "Porque 8 divide a diferença (25 - 9 = 16) de forma exata.",
                "C": "Porque 25 dividido por 8 dá quociente 3.",
                "D": "Porque 9 é o antecessor direto de 10.",
            },
            "correct": "B",
            "correct_fb": "Perfeito! A definição formal estabelece: a ≡ b (mod n) ⟺ n | (a - b). Como 25 - 9 = 16, e 8 divide 16 perfeitamente (16 / 8 = 2 sem resto), a equivalência é irrefutável!",
            "incorrect_fb": "Incorreto. A definição de congruência modular exige que n divida a diferença entre os dois números: 25 - 9 = 16. Como 16 é múltiplo exato de 8 (8 x 2 = 16), a afirmação é verdadeira.",
        },
        {
            "question": "Considere a questão oficial Q18 do Concurso PPGCC IFCE 2025: a relação R definida nos inteiros Z por (x, y) ∈ R se, e somente se, |x| = |y|. Essa relação é de equivalência?",
            "options": {
                "A": "Não, pois (-3, 3) está na relação mas (3, -3) não está.",
                "B": "Não, pois o número zero não possui simétrico.",
                "C": "Sim, pois a igualdade de valores absolutos é trivialmente reflexiva (|x|=|x|), simétrica (|x|=|y| => |y|=|x|) e transitiva (|x|=|y| e |y|=|z| => |x|=|z|).",
                "D": "Não, pois falha na transitividade quando x e z têm sinais opostos.",
            },
            "correct": "C",
            "correct_fb": "Brilhante! Essa foi a questão exata da banca: a igualdade de qualquer função f(x) = f(y) (neste caso f(x) = |x|) SEMPRE induz uma relação de equivalência perfeita, pois a igualdade no contradomínio é reflexiva, simétrica e transitiva!",
            "incorrect_fb": "Incorreto. Verifique os três testes: 1. |x| = |x| (sempre verdadeiro). 2. Se |x| = |y|, então |y| = |x| (sempre verdadeiro). 3. Se |x|=|y| e |y|=|z|, então |x|=|z| (sempre verdadeiro). Logo, é uma relação de equivalência!",
        },
        {
            "question": "Em termos visuais e topológicos, como se parece o dígrafo de uma relação de equivalência homogênea?",
            "options": {
                "A": "Uma única linha reta que nunca retorna ao ponto de partida.",
                "B": "Um conjunto de componentes desconexas, onde cada componente é um subgrafo completamente conectado com laços em todos os nós e arestas de mão dupla entre todos os seus membros.",
                "C": "Uma árvore binária perfeita com nós folhas sem arestas de saída.",
                "D": "Um dígrafo sem laços e sem ciclos.",
            },
            "correct": "B",
            "correct_fb": "Exato! Cada classe de equivalência forma uma 'ilha' (componente conexa) onde todo mundo se conecta com todo mundo em mão dupla e cada nó possui um laço próprio. As ilhas não conversam entre si!",
            "incorrect_fb": "Incorreto. Devido à reflexividade (todo nó tem laço), simetria (toda aresta tem volta) e transitividade (todos os pares se conectam), cada grupo de elementos equivalentes forma um subgrafo completo isolado das outras classes.",
        },
    ],
    "next_step": "Agora que vimos como a equivalência cria ilhas perfeitas, vamos aprender a etiquetar e separar essas ilhas no Teorema Fundamental das Classes de Equivalência e Partições!",
}

TOPIC_5_DATA = {
    "title": "Classes de Equivalência e Partições — Organizando o Caos em Gavetas Perfeitas",
    "subtitle": "O Teorema Fundamental das Relações de Equivalência: gavetas disjuntas, quociente A/~ e congruência modular.",
    "philosophy_title": "O Armário Perfeito: Gavetas Sem Furos e Sem Sobreposição",
    "philosophy_text": """
Imagine que você tem a tarefa de organizar centenas de arquivos espalhados na área de trabalho de um servidor.
Você cria pastas temáticas. Para que essa organização seja impecável, ela precisa respeitar duas regras de ouro:
1. <strong>Nenhum arquivo pode ficar órfão</strong> (todo arquivo deve estar em alguma pasta);
2. <strong>Nenhum arquivo pode estar em duas pastas ao mesmo tempo</strong> (as pastas não se sobrepõem).
Na matemática, esse armário perfeito chama-se <strong>Partição de um Conjunto</strong>.
E o resultado mais belo da álgebra discreta nos diz:
<strong>Toda relação de equivalência particiona o conjunto em gavetas perfeitas — e cada uma dessas gavetas é chamada de Classe de Equivalência!</strong>
""",
    "word_breakdowns": [
        {
            "term": "Classe de Equivalência",
            "pronunciation": "clas-se de e-qui-va-lên-ci-a",
            "etymology": "Do latim 'classis' (grupo convocado sob a mesma bandeira).",
            "plain_meaning": "O conjunto de todos os elementos que são equivalentes a um representante escolhido 'a'. Denota-se por [a] ou ā.",
        },
        {
            "term": "Conjunto Quociente",
            "pronunciation": "con-jun-to quo-ci-en-te",
            "etymology": "Do latim 'quotiens' (quantas vezes se divide uma totalidade).",
            "plain_meaning": "A coleção de todas as gavetas (classes de equivalência). Denota-se por A/~ ou A/R. É o conjunto cujos elementos são as próprias classes!",
        },
        {
            "term": "Partição",
            "pronunciation": "par-ti-ção",
            "etymology": "Do latim 'partitio' (divisão de uma totalidade em fatias sem perda de massa).",
            "plain_meaning": "Uma família de subconjuntos não vazios que divide o conjunto original sem sobras e sem cruzamentos.",
        },
    ],
    "formulas": [
        {
            "latex": "[a]_R = \\{ x \\in A \\mid (x, a) \\in R \\}",
            "spoken": "A classe de equivalência de a segundo R é o conjunto dos elementos x em A tais que x se relaciona com a",
            "meaning": "Definição formal da gaveta: todos os elementos que compartilham a mesma essência de 'a' entram dentro da mesma chave $[a]$.",
        },
        {
            "latex": "[a] = [b] \\iff a \\sim b \\qquad \\text{caso contrário} \\qquad [a] \\cap [b] = \\emptyset",
            "spoken": "A classe de a é idêntica à classe de b se, e somente se, a for equivalente a b; caso contrário, a interseção entre elas é vazia",
            "meaning": "O Teorema da Disjunção Total: duas classes de equivalência NUNCA se cruzam pela metade! Ou elas são a mesmíssima gaveta, ou são completamente estranhas entre si.",
        },
        {
            "latex": "A / \\sim \\, = \\{ [a] \\mid a \\in A \\}",
            "spoken": "O conjunto quociente de A por til é o conjunto de todas as classes de equivalência de A",
            "meaning": "O novo universo onde cada elemento é uma gaveta inteira. Exemplo: Z / 3Z tem apenas 3 elementos: a classe [0] (múltiplos de 3), [1] (resto 1) e [2] (resto 2).",
        },
    ],
    "computation_title": "O Teorema Fundamental das Relações de Equivalência",
    "computation_text": """
Este teorema é um dos mais cobrados em pós-graduação e concursos:
- <strong>Direção 1:</strong> Dada qualquer relação de equivalência $R$ sobre $A$, as classes de equivalência formam uma partição legítima de $A$;
- <strong>Direção 2:</strong> Dada qualquer partição $\\mathcal{P} = \\{A_1, A_2, \\dots, A_k\\}$ de $A$, existe uma relação de equivalência induzida onde $(x, y) \\in R \\iff x$ e $y$ pertencem ao mesmíssimo bloco $A_i$.
Existe uma bijeção de um-para-um entre o conceito de 'Relação de Equivalência' e o conceito de 'Partição'!
""",
    "traps": [
        {
            "title": "Achar que o Quociente Tem o Mesmo Tamanho do Conjunto Original",
            "text": "Se $A = \\{0, 1, 2, 3, 4, 5\\}$ e a relação for congruência módulo 2 (par ou ímpar), o conjunto $A$ tem 6 números inteiros. Mas o conjunto quociente $A / \\sim$ tem APENAS DOIS ELEMENTOS: a gaveta dos pares $[0] = \\{0, 2, 4\\}$ e a gaveta dos ímpares $[1] = \\{1, 3, 5\\}$.",
        },
    ],
    "questions": [
        {
            "question": "Sejam a e b elementos de um conjunto A sobre o qual está definida uma relação de equivalência ~. Se soubermos que a interseção [a] ∩ [b] NÃO é vazia, o que podemos afirmar com certeza matemática?",
            "options": {
                "A": "Que a e b não são equivalentes.",
                "B": "Que as classes são rigorosamente idênticas: [a] = [b].",
                "C": "Que uma classe é subconjunto próprio da outra.",
                "D": "Que a relação perdeu a transitividade.",
            },
            "correct": "B",
            "correct_fb": "Exato! Esse é o Teorema da Disjunção das Classes: classes de equivalência nunca têm interseção parcial. Se elas compartilham ao menos um único elemento em comum, então elas são a mesmíssima classe: [a] = [b]!",
            "incorrect_fb": "Cuidado: na teoria das relações de equivalência, duas classes ou são completamente disjuntas ([a] ∩ [b] = ∅) ou são idênticas ([a] = [b]). Compartilhar um elemento obriga que sejam a mesma gaveta.",
        },
        {
            "question": "Considere o conjunto dos inteiros Z e a relação de equivalência dada pela congruência módulo 4 (a ≡ b mod 4). Quantas classes de equivalência distintas compõem o conjunto quociente Z / 4Z?",
            "options": {
                "A": "Infinitas classes de equivalência.",
                "B": "Exatamente 2 classes (positivos e negativos).",
                "C": "Exatamente 4 classes: [0], [1], [2] e [3].",
                "D": "16 classes distintas.",
            },
            "correct": "C",
            "correct_fb": "Perfeito! Qualquer número inteiro dividido por 4 deixa resto 0, 1, 2 ou 3. Cada possível resto forma uma gaveta infinita de números. Portanto, o conjunto quociente possui exatamente 4 classes: {[0], [1], [2], [3]}.",
            "incorrect_fb": "Incorreto. Na divisão euclidiana por 4, os únicos restos possíveis são 0, 1, 2 e 3. Cada inteiro cai em exatamente uma dessas 4 gavetas, totalizando 4 classes no conjunto quociente.",
        },
        {
            "question": "Qual das seguintes coleções de subconjuntos representa uma partição válida do conjunto S = {1, 2, 3, 4, 5, 6}?",
            "options": {
                "A": "P = {{1, 2}, {3, 4}, {5}}",
                "B": "P = {{1, 2, 3}, {3, 4, 5}, {6}}",
                "C": "P = {{1, 3, 5}, {2, 4, 6}}",
                "D": "P = {{1, 2, 3, 4, 5, 6}, ∅}",
            },
            "correct": "C",
            "correct_fb": "Excelente! Na opção C, os subconjuntos {1, 3, 5} e {2, 4, 6} são não-vazios, sua interseção é vazia (disjuntos) e sua união recompõe S perfeitamente: {1, 2, 3, 4, 5, 6}. É uma partição impecável!",
            "incorrect_fb": "Verifique os critérios de partição: 1. Nenhum bloco pode ser vazio (D tem ∅). 2. A união deve dar S inteiro (A esqueceu o 6). 3. Os blocos devem ser disjuntos (B repete o 3). A única correta é a C.",
        },
        {
            "question": "Dada uma relação de equivalência em um conjunto finito com n elementos, se a relação for a menor relação de equivalência possível (apenas os laços reflexivos R = {(x, x) | x ∈ A}), quantas classes de equivalência existirão no conjunto quociente?",
            "options": {
                "A": "Apenas 1 classe contendo todo mundo.",
                "B": "Exatamente n classes, onde cada classe é um conjunto unitário {[x] = {x}}.",
                "C": "Zero classes.",
                "D": "n^2 classes.",
            },
            "correct": "B",
            "correct_fb": "Brilhante! Quando cada elemento só é equivalente a si próprio (relação de igualdade estrita x = y), cada elemento mora em sua própria gaveta individual, gerando exatamente n classes unitárias!",
            "incorrect_fb": "Incorreto. Se ninguém se relaciona com ninguém além de si mesmo, não há agrupamentos maiores. Cada elemento fica isolado em sua própria classe unitária {x}, totalizando n classes.",
        },
    ],
    "next_step": "Até aqui, estudamos relações que agrupam elementos em igualdade. Agora faremos o movimento oposto: construir hierarquias de cima a baixo substituindo a simetria pela antissimetria nas Relações de Ordem (Posets)!",
}

TOPIC_6_DATA = {
    "title": "Relações de Ordem — Posets e a Construção de Hierarquias",
    "subtitle": "A substituição da simetria pela antissimetria: ordens parciais, elementos incomparáveis e cadeias lineares.",
    "philosophy_title": "Da Igualdade para a Hierarquia: A Quebra da Mão Dupla",
    "philosophy_text": """
Nas relações de equivalência, a regra de ouro era a Simetria: se eu estou conectado a você, você está conectado a mim. Isso criava ilhas de iguais.
Mas na vida real e nos sistemas computacionais, muitas vezes queremos <strong>ranquear, priorizar e ordenar</strong>:
- O processo A deve executar antes do processo B;
- O pacote <code>libssl-dev</code> precisa ser instalado antes do servidor web;
- Na hierarquia de permissões, o <code>root</code> está acima do usuário comum.
Para construir uma hierarquia sem ciclos viciosos, a matemática precisou <strong>expulsar a simetria</strong> e colocar em seu lugar a <strong>Antissimetria</strong>.
Surge assim a estrutura mais fascinante da computação discreta: o <strong>Poset (Partially Ordered Set)</strong>.
""",
    "word_breakdowns": [
        {
            "term": "Poset",
            "pronunciation": "pô-sét",
            "etymology": "Acrônimo em inglês para 'Partially Ordered Set' (Conjunto Parcialmente Ordenado).",
            "plain_meaning": "Um par (S, ≤) onde a relação ≤ é Reflexiva, Antissimétrica e Transitiva (RAT). Permite que alguns elementos fiquem lado a lado sem se comparar.",
        },
        {
            "term": "Incomparabilidade",
            "pronunciation": "in-com-pa-ra-bi-li-da-de",
            "etymology": "In (negação) + comparabilis (aquilo que pode ser medido em uma mesma régua).",
            "plain_meaning": "Dois elementos 'a' e 'b' são incomparáveis (a ∥ b) quando nem a ≤ b e nem b ≤ a. Exemplo: um peixe e um pássaro não são um menor que o outro.",
        },
        {
            "term": "Cadeia (Ordem Linear)",
            "pronunciation": "ca-dei-a",
            "etymology": "Do latim 'catena' (elos sequenciais onde cada um se liga ao próximo).",
            "plain_meaning": "Um subconjunto do poset onde todos os elementos podem ser comparados entre si (sem elementos paralelos). É uma fila indiana perfeita.",
        },
    ],
    "formulas": [
        {
            "latex": "(S, \\le) \\text{ é Poset} \\iff \\le \\text{ é Reflexiva, Antissimétrica e Transitiva (RAT)}",
            "spoken": "O par S com menor ou igual é um poset se, e somente se, a relação for reflexiva, antissimétrica e transitiva",
            "meaning": "A Tríade Sagrada da Ordem. A antissimetria garante que não há voltas mútuas: se x está abaixo de y, y jamais poderá estar abaixo de x.",
        },
        {
            "latex": "a \\parallel b \\iff \\neg(a \\le b) \\land \\neg(b \\le a)",
            "spoken": "a é incomparável a b se, e somente se, não é verdade que a seja menor ou igual a b e não é verdade que b seja menor ou igual a a",
            "meaning": "A essência da ordem PARCIAL: a relação não é obrigada a decidir quem é o chefe entre dois nós concorrentes. Exemplo em partes: {1} e {2} são incomparáveis sob inclusão.",
        },
        {
            "latex": "\\forall x, y \\in S, \\quad (x \\le y) \\lor (y \\le x) \\implies \\text{Ordem Total}",
            "spoken": "Para quaisquer x e y em S, x é menor ou igual a y ou y é menor ou igual a x, implicando que a ordem é total",
            "meaning": "Se a incomparabilidade for extirpada e todo mundo puder ser medido na mesma régua linear, a ordem parcial é promovida a Ordem Total (ou Linear).",
        },
    ],
    "computation_title": "Onde Posets Brilham na Computação: Grafos de Dependência e DAGs",
    "computation_text": """
Todo grafo acíclico direcionado (DAG) transitivamente fechado é um Poset:
1. <strong>Compilação com <code>make</code> / CI/CD:</strong> Se a tarefa B depende de A, e C depende de B, A deve rodar antes de C (transitividade). Mas tarefas D e E que não dependem uma da outra rodam em paralelo (são <em>incomparáveis</em>!);
2. <strong>Controle de Concorrência e Relógios de Lamport:</strong> No processamento distribuído, o 'aconteceu-antes' (<em>happened-before relation</em> $\\to$) é uma ordem parcial estrita;
3. <strong>Sistemas de Tipos:</strong> Na orientação a objetos, a relação 'é subtipo de' ($<:$) forma um poset de herança.
""",
    "traps": [
        {
            "title": "Ordem Parcial NÃO significa 'Incompleta'!",
            "text": "O termo 'parcial' assusta quem está começando. Não significa que falta trabalho ou que a relação está quebrada. Significa apenas que a estrutura tem ramos em árvore ou malha, em vez de ser uma linha reta de fila única.",
        },
    ],
    "questions": [
        {
            "question": "Qual é a tríade exata de propriedades que define matematicamente um Poset (Conjunto Parcialmente Ordenado)?",
            "options": {
                "A": "Reflexiva, Simétrica e Transitiva (RST).",
                "B": "Irreflexiva, Antissimétrica e Transitiva (IAT).",
                "C": "Reflexiva, Antissimétrica e Transitiva (RAT).",
                "D": "Reflexiva, Antissimétrica e Não-Transitiva.",
            },
            "correct": "C",
            "correct_fb": "Exato! Um Poset é definido pela tríade RAT: Reflexiva (todo elemento é menor ou igual a si mesmo), Antissimétrica (não há idas e voltas entre nós distintos) e Transitiva (se a <= b e b <= c, então a <= c).",
            "incorrect_fb": "Atenção à troca de letras: RST define Relação de Equivalência. RAT define Relação de Ordem Parcial (Poset). A diferença crucial é a Antissimetria no lugar da Simetria!",
        },
        {
            "question": "Considere o conjunto S = {1, 2, 3} e o poset do conjunto das partes (P(S), ⊆) ordenado pela inclusão de conjuntos. O que pode ser dito sobre os elementos {1} e {2}?",
            "options": {
                "A": "{1} ⊆ {2}, pois 1 é menor que 2.",
                "B": "{1} e {2} são incomparáveis ({1} ∥ {2}), pois nenhum deles é subconjunto do outro.",
                "C": "O conjunto das partes forma uma ordem total.",
                "D": "{2} ⊆ {1} pela propriedade reflexiva.",
            },
            "correct": "B",
            "correct_fb": "Perfeito! Como {1} não está contido em {2} e {2} não está contido em {1}, eles não possuem conexão de inclusão entre si. Eles são perfeitamente INCOMPARÁVEIS ({1} ∥ {2})!",
            "incorrect_fb": "Cuidado: a ordem aqui não é a numeração dos inteiros, mas a inclusão de conjuntos (⊆). O conjunto {1} tem o número 1, o {2} tem o número 2. Nenhum contém o outro, logo são incomparáveis.",
        },
        {
            "question": "Em um poset (S, ≤), o que caracteriza formalmente um subconjunto C ⊆ S como sendo uma Cadeia (Chain)?",
            "options": {
                "A": "Todos os elementos de C são mutuamente incomparáveis entre si.",
                "B": "C é um subconjunto totalmente ordenado, onde para quaisquer dois elementos x, y em C, ou x ≤ y ou y ≤ x.",
                "C": "C contém obrigatoriamente um ciclo direcionado.",
                "D": "C possui cardinalidade infinita.",
            },
            "correct": "B",
            "correct_fb": "Excelente! Uma cadeia é uma fatia do poset onde todos os elementos se alinham em uma fila única sem bifurcações: quaisquer dois elementos podem ser comparados entre si.",
            "incorrect_fb": "Incorreto. A definição de cadeia é exatamente a linearidade: para quaisquer x e y no subconjunto, um é menor ou igual ao outro. Se todos fossem incomparáveis, teríamos uma ANTICADEIA.",
        },
        {
            "question": "Qual das seguintes relações é um exemplo canônico de Ordem Total sobre os números inteiros?",
            "options": {
                "A": "A relação de divisibilidade 'x divide y' (x | y).",
                "B": "A relação usual 'menor ou igual que' (x ≤ y).",
                "C": "A relação 'x e y têm a mesma paridade'.",
                "D": "O produto cartesiano Z x Z.",
            },
            "correct": "B",
            "correct_fb": "Brilhante! Na relação usual ≤ dos inteiros, dados quaisquer dois números, ou x ≤ y ou y ≤ x (ex: entre 7 e 12, sabemos que 7 ≤ 12). Não existem inteiros incomparáveis sob essa relação, sendo uma Ordem Total!",
            "incorrect_fb": "Incorreto. Na divisibilidade (x | y), o 2 e o 3 são incomparáveis (2 não divide 3 e 3 não divide 2), sendo ordem parcial. A relação usual ≤ compara absolutamente todos os pares, sendo Total.",
        },
    ],
    "next_step": "Com a estrutura hierárquica do Poset em mãos, agora decifraremos as maiores armadilhas de concurso sobre o topo e a base da ordem: Elementos Maximais, Minimais, Supremo, Ínfimo e Reticulados!",
}

TOPIC_7_DATA = {
    "title": "Propriedades de Relações de Ordem — Extremais, Limites e Reticulados",
    "subtitle": "A distinção crucial entre maximal vs máximo, minimal vs mínimo, limitantes, supremo, ínfimo e reticulados.",
    "philosophy_title": "A Geometria dos Picos: Por que o Maior Nem Sempre é o Máximo",
    "philosophy_text": """
Aqui chegamos ao divisor de águas entre o estudante que decora fórmulas e o candidato que gabarita a prova do mestrado.
Na linguagem coloquial, dizemos que o Everest é 'o ponto máximo' da Terra. Mas o que acontece se estivermos em uma cordilheira com várias montanhas e não houver caminhos conectando seus picos?
Em um Poset, <strong>não existe apenas uma única régua</strong>.
- Um elemento é <strong>Maximal</strong> quando <em>ninguém está acima dele</em> na sua trilha local. Podem existir dezenas de picos isolados!
- Já um elemento é <strong>Máximo</strong> quando <em>ele está acima de ABSOLUTAMENTE TODOS os elementos do conjunto</em>.
Se houver dois picos independentes que não se comparam, <strong>O POSET NÃO TEM ELEMENTO MÁXIMO!</strong>
Compreender essa distinção anatômica desvenda todas as pegadinhas da banca examinadora.
""",
    "word_breakdowns": [
        {
            "term": "Maximal vs Máximo",
            "pronunciation": "ma-xi-mal vs má-xi-mo",
            "etymology": "Maximal (local, ninguém o supera) vs Máximo (global, supera todos).",
            "plain_meaning": "Maximal: 'Ninguém manda em mim'. Máximo: 'Eu sou o chefe de todo mundo sem exceção'. Pode haver vários maximais, mas o máximo, se existir, é ÚNICO.",
        },
        {
            "term": "Supremo (Menor Limitante Superior)",
            "pronunciation": "su-pre-mo",
            "etymology": "Do latim 'supremus' (o mais alto limite inferior da cobertura). Denotado por sup(A) ou a ∨ b.",
            "plain_meaning": "O menor teto comum que abriga dois elementos ao mesmo tempo. Em divisibilidade, é o MMC (Mínimo Múltiplo Comum).",
        },
        {
            "term": "Ínfimo (Maior Limitante Inferior)",
            "pronunciation": "ín-fi-mo",
            "etymology": "Do latim 'infimus' (o piso mais elevado de sustentação). Denotado por inf(A) ou a ∧ b.",
            "plain_meaning": "O maior chão comum sobre o qual dois elementos se apoiam. Em divisibilidade, é o MDC (Máximo Divisor Comum).",
        },
        {
            "term": "Reticulado (Lattice)",
            "pronunciation": "re-ti-cu-la-do",
            "etymology": "Do latim 'reticulum' (rede entrelaçada onde todos os fios convergem).",
            "plain_meaning": "Um poset onde TODO par de elementos {a, b} possui obrigatoriamente um Supremo único (a ∨ b) e um Ínfimo único (a ∧ b).",
        },
    ],
    "formulas": [
        {
            "latex": "m \\in S \\text{ é Maximal} \\iff \\neg \\exists x \\in S \\, (m < x)",
            "spoken": "m em S é maximal se, e somente se, não existe nenhum x em S tal que m seja estritamente menor que x",
            "meaning": "Definição formal de Maximal: ninguém está acima dele. Topologicamente, não parte nenhuma aresta para cima dele.",
        },
        {
            "latex": "M \\in S \\text{ é Máximo} \\iff \\forall x \\in S \\, (x \\le M)",
            "spoken": "M em S é elemento máximo se, e somente se, para todo x em S, x for menor ou igual a M",
            "meaning": "Definição formal de Máximo: todo mundo no conjunto aponta para ele ou está abaixo dele. É o topo absoluto.",
        },
        {
            "latex": "\\text{Se existem } m_1, m_2 \\in S \\text{ com } m_1 \\neq m_2 \\text{ maximais} \\implies \\nexists \\text{ Máximo em } S",
            "spoken": "Se existem m1 e m2 distintos maximais, então não existe elemento máximo em S",
            "meaning": "Teorema de Ouro da Banca IFCE: havendo mais de um maximal concorrente, o poset fica órfão de elemento máximo!",
        },
        {
            "latex": "\\forall a, b \\in L, \\quad \\exists ! \\sup(a, b) = a \\lor b \\quad \\land \\quad \\exists ! \\inf(a, b) = a \\land b",
            "spoken": "Para quaisquer a e b em L, existe um único supremo a join b e existe um único ínfimo a meet b",
            "meaning": "Axioma Fundamental do Reticulado: todo par tem que ter um menor teto comum único e um maior piso comum único.",
        },
    ],
    "computation_title": "Reticulados em Segurança da Informação e Tipos (Modelos Bell-LaPadula)",
    "computation_text": """
A teoria de reticulados é a espinha dorsal da Segurança da Informação:
1. <strong>Modelo de Segurança Multinível (Bell-LaPadula):</strong> Classificações como <em>Público < Restrito < Confidencial < Secreto</em> formam um reticulado. O supremo ($\\\\lor$) calcula a classificação de um documento que combina dados de duas fontes;
2. <strong>Inferência de Tipos em Compiladores:</strong> Quando você escreve uma expressão <code>if condition then int else float</code>, o compilador calcula o <strong>menor supertipo comum</strong> (o Supremo / Join) no reticulado de tipos;
3. <strong>Análise de Fluxo Estático de Dados (Dataflow Analysis):</strong> Otimização de código em compiladores usa reticulados para encontrar variáveis constantes e código morto.
""",
    "traps": [
        {
            "title": "A Pegadinha Clássica do Maior Número do Colégio",
            "text": "Considere o conjunto $B = \\{2, 3, 4, 6, 8, 12\\}$ sob a relação 'divide' ($x \\mid y$). Quem é o elemento máximo? A resposta ingênua é '12'. Mas 12 NÃO É MÁXIMO! Por que? Porque 8 não divide 12! O número 8 também é maximal! Como temos 8 e 12 como maximais, o conjunto NÃO TEM ELEMENTO MÁXIMO!",
        },
    ],
    "questions": [
        {
            "question": "Seja o conjunto B = {2, 3, 4, 6, 8, 12} com a ordem parcial da divisibilidade (x | y). Quais são os elementos maximais e qual é o elemento máximo de B?",
            "options": {
                "A": "Maximais: apenas {12}; Elemento máximo: 12.",
                "B": "Maximais: {8, 12}; Elemento máximo: Não existe.",
                "C": "Maximais: {6, 8, 12}; Elemento máximo: 12.",
                "D": "Maximais: {8, 12}; Elemento máximo: 24.",
            },
            "correct": "B",
            "correct_fb": "Exato! Ninguém em B é múltiplo de 8 além dele mesmo, e ninguém em B é múltiplo de 12 além dele mesmo. Logo, 8 e 12 são dois maximais concorrentes! Pelo Teorema de Ouro, havendo mais de um maximal, NÃO EXISTE elemento máximo!",
            "incorrect_fb": "Cuidado com a pegadinha clássica! 12 não é máximo porque 8 não divide 12 (8 <= 12 é falso na relação de divisibilidade). Como 8 e 12 estão no topo sem ninguém acima deles, ambos são maximais e não há máximo.",
        },
        {
            "question": "Qual é a diferença fundamental entre um elemento Minimal e o elemento Mínimo de um poset?",
            "options": {
                "A": "Não há diferença, são sinônimos perfeitos.",
                "B": "Minimal significa que nenhum elemento do poset é estritamente menor que ele; Mínimo significa que ele é menor ou igual a todos os elementos do poset.",
                "C": "Minimal só existe em ordens totais; Mínimo só existe em ordens parciais.",
                "D": "O minimal é sempre único, enquanto podem existir múltiplos mínimos.",
            },
            "correct": "B",
            "correct_fb": "Perfeito! Minimal é uma propriedade de não-superação local (ninguém está abaixo dele). Mínimo é uma propriedade de sustentação global (ele está abaixo de absolutamente todos os nós).",
            "incorrect_fb": "Incorreto. A definição formal: m é minimal se não existe x tal que x < m. M é mínimo se para todo x, M <= x. Pode haver vários minimais, mas se houver mínimo, ele é único.",
        },
        {
            "question": "O que é necessário e suficiente para que um conjunto parcialmente ordenado (L, ≤) seja formalmente classificado como um Reticulado (Lattice)?",
            "options": {
                "A": "Que a ordem seja total e não possua elementos incomparáveis.",
                "B": "Que todo subconjunto de dois elementos {a, b} possua um único Supremo (menor limitante superior) e um único Ínfimo (maior limitante inferior).",
                "C": "Que o conjunto seja infinito e reflexivo.",
                "D": "Que não possua elementos minimais nem maximais.",
            },
            "correct": "B",
            "correct_fb": "Excelente! Essa é a definição canônica de Reticulado: para todo par de nós {a, b}, deve existir um supremo único (a ∨ b) e um ínfimo único (a ∧ b).",
            "incorrect_fb": "Incorreto. A definição de reticulado é algébrica: todo par precisa ter um menor teto comum (supremo) e um maior piso comum (ínfimo) únicos. Não exige que a ordem seja total.",
        },
        {
            "question": "Considere o conjunto das partes P({a, b}) ordenado por inclusão ⊆: {∅, {a}, {b}, {a, b}}. Essa estrutura é um reticulado? Qual é o supremo de {{a}, {b}}?",
            "options": {
                "A": "Não é reticulado; o supremo não existe.",
                "B": "Sim, é um reticulado; o supremo é {a, b} (a união dos conjuntos).",
                "C": "Sim, é um reticulado; o supremo é ∅ (a interseção dos conjuntos).",
                "D": "Não é reticulado pois {a} e {b} são incomparáveis.",
            },
            "correct": "B",
            "correct_fb": "Brilhante! O conjunto das partes sob inclusão é o reticulado booleano por excelência: o supremo de dois conjuntos é a sua União ({a} ∪ {b} = {a, b}) e o ínfimo é a sua Interseção ({a} ∩ {b} = ∅)!",
            "incorrect_fb": "Incorreto. Todo conjunto das partes sob inclusão forma um reticulado booleano perfeito! O menor teto que contém tanto {a} quanto {b} é a união deles: {a, b}.",
        },
    ],
    "next_step": "Agora que você sabe tudo sobre ordens, maximais e reticulados, vamos aprender a arte de desenhar essas estruturas sem nenhuma poluição visual na aula definitiva da Fase 1: Diagramas de Hasse!",
}

TOPIC_8_DATA = {
    "title": "Leitura e Interpretação de Diagramas de Hasse — A Geometria Limpa dos Posets",
    "subtitle": "As 3 regras de redução de Helmut Hasse: eliminando laços e atalhos transitivos para expor a cobertura degrau a degrau.",
    "philosophy_title": "A Arte da Limpeza Visual: Por que Menos é Infinitamente Mais",
    "philosophy_text": """
Se você desenhar o dígrafo completo de um Poset com apenas 8 elementos (como o hipercubo de subconjuntos de 3 itens), o resultado é um pesadelo visual:
são dezenas de laços reflexivos em cada nó e dezenas de flechas de atalhos cruzando a tela em todas as direções.
O matemático alemão Helmut Hasse percebeu algo genial em 1932:
<strong>Como todo mundo já sabe que uma ordem é reflexiva e transitiva, desenhar laços e atalhos é pura redundância inútil!</strong>
Ao eliminar tudo o que é óbvio, criamos o <strong>Diagrama de Hasse</strong>:
uma representação minimalista e elegante onde apenas as arestas essenciais (as <em>coberturas</em>) sobrevivem, e a direção do fluxo é lida naturalmente <strong>de baixo para cima</strong> pela gravidade do desenho.
""",
    "word_breakdowns": [
        {
            "term": "Diagrama de Hasse",
            "pronunciation": "di-a-gra-ma de há-sse",
            "etymology": "Em homenagem a Helmut Hasse (1898–1979), algebrista e teorista dos números alemão.",
            "plain_meaning": "O desenho limpo de um poset onde nós inferiores ficam embaixo, nós superiores ficam em cima, e linhas retas unem quem cobre quem.",
        },
        {
            "term": "Relação de Cobertura",
            "pronunciation": "re-la-ção de co-ber-tu-ra",
            "etymology": "Denotada pelo símbolo ⋖ (x ⋖ y significa 'y cobre x').",
            "plain_meaning": "y está imediatamente acima de x sem NENHUM elemento intermediário entre eles. Exemplo: 2 cobre 1 em divisibilidade, mas 4 NÃO cobre 1 porque o 2 está no meio!",
        },
        {
            "term": "Redução Transitiva",
            "pronunciation": "re-du-ção tran-si-ti-va",
            "etymology": "Reduzir o grafo ao menor número de arestas que preserve o mesmo fecho transitivo.",
            "plain_meaning": "Apagar todas as arestas que são atalhos redundantes de caminhos mais longos.",
        },
    ],
    "formulas": [
        {
            "latex": "x \\lessdot y \\iff x < y \\quad \\land \\quad \\neg \\exists z \\in S \\, (x < z < y)",
            "spoken": "y cobre x se, e somente se, x for menor que y e não existir nenhum elemento z tal que x seja menor que z e z seja menor que y",
            "meaning": "Definição axiomática de Cobertura: y é o sucessor direto degrau a degrau de x. No Diagrama de Hasse, desenham-se EXCLUSIVAMENTE as linhas de cobertura!",
        },
        {
            "latex": "\\text{Regras de Hasse: } 1) \\text{ Apagar laços } (x, x) \\quad 2) \\text{ Apagar atalhos } (x, z) \\text{ se } x < y < z \\quad 3) \\text{ Apagar flechas}",
            "spoken": "As três regras de Hasse: apagar laços reflexivos, apagar atalhos transitivos e apagar pontas de flecha",
            "meaning": "O algoritmo visual canônico: a orientação de baixo para cima substitui as setas; a ausência de atalhos expõe a geometria dos reticulados.",
        },
        {
            "latex": "|E_G| = 12 \\text{ arestas estritas} \\quad \\implies \\quad |E_H| = 7 \\text{ coberturas mantidas} \\quad (5 \\text{ atalhos eliminados})",
            "spoken": "No conjunto dos divisores de doze, o dígrafo estrito tem doze arestas, o diagrama de Hasse mantém sete coberturas e elimina cinco atalhos transitivos",
            "meaning": "Cálculo oficial de concurso da banca IFCE: no conjunto D_12 = {1, 2, 3, 4, 6, 12}, 5 arestas transitivas redundantes são eliminadas ((1,4), (1,6), (1,12), (2,12), (3,12)).",
        },
    ],
    "computation_title": "Contraexemplos Canônicos de Reticulados: Pentágono N5 e Diamante M3",
    "computation_text": """
Dois diagramas de Hasse são imortais na Ciência da Computação teórica:
1. <strong>Pentágono $N_5$:</strong> É o menor exemplo de reticulado que <strong>NÃO É MODULAR</strong>. Possui uma cadeia de comprimento 3 de um lado e um nó solitário do outro lado;
2. <strong>Diamante $M_3$:</strong> É modular, mas <strong>NÃO É DISTRIBUTIVO</strong>. Possui 3 nós centrais incomparáveis concorrendo entre a base e o topo.
<strong>Teorema de Birkhoff:</strong> Um reticulado é distributivo se, e somente se, NÃO CONTÉM $N_5$ nem $M_3$ como subreticulados!
""",
    "traps": [
        {
            "title": "Desenhar Flechas ou Laços no Diagrama de Hasse",
            "text": "É terminação errada colocar flechas direcionadas ou laços no Diagrama de Hasse! Por convenção internacional de Helmut Hasse, flechas e laços são terminantemente proibidos: o menor sempre fica abaixo e o maior acima.",
        },
    ],
    "questions": [
        {
            "question": "Quais são as três operações fundamentais executadas pelo algoritmo de Helmut Hasse para transformar o dígrafo de um poset em seu Diagrama de Hasse?",
            "options": {
                "A": "Adicionar fecho transitivo, inverter as arestas e duplicar os laços.",
                "B": "Eliminar todos os laços reflexivos (x, x), eliminar todas as arestas transitivas redundantes (redução transitiva) e remover as pontas de flecha orientando verticalmente de baixo para cima.",
                "C": "Transformar o dígrafo em uma árvore binária completa de busca.",
                "D": "Manter apenas as arestas que formam ciclos direcionados.",
            },
            "correct": "B",
            "correct_fb": "Exato! Helmut Hasse estabeleceu as 3 regras: 1. Arrancar laços reflexivos. 2. Arrancar atalhos transitivos (preservando apenas coberturas diretas). 3. Remover setas, confiando na orientação vertical (menor embaixo, maior em cima).",
            "incorrect_fb": "Incorreto. O Diagrama de Hasse é uma simplificação minimalista: remove laços (sabemos que é reflexivo), remove atalhos transitivos (sabemos que é transitivo) e troca flechas pela orientação de altura.",
        },
        {
            "question": "Considere o conjunto S = {1, 2, 3, 4, 6, 12} ordenado por divisibilidade (x | y). O dígrafo estrito possui 12 arestas. Quantas arestas são mantidas no Diagrama de Hasse e quantas são eliminadas pela redução transitiva?",
            "options": {
                "A": "Mantém 8 e elimina 4.",
                "B": "Mantém 6 e elimina 6.",
                "C": "Mantém exatamente 7 arestas de cobertura e elimina 5 arestas transitivas redundantes.",
                "D": "Mantém 9 e elimina 3.",
            },
            "correct": "C",
            "correct_fb": "Perfeito! As 7 arestas de cobertura mantidas são: (1,2), (1,3), (2,4), (2,6), (3,6), (4,12) e (6,12). As 5 arestas eliminadas são os atalhos: (1,4), (1,6), (1,12), (2,12) e (3,12). Total: 12 - 7 = 5 eliminadas!",
            "incorrect_fb": "Cuidado com o cálculo: desenhe os níveis de divisibilidade. As ligações diretas de cobertura são 7 arestas. Os atalhos que pulam nós intermediários são exatamente 5 arestas, que são eliminadas.",
        },
        {
            "question": "Ao inspecionar visualmente um Diagrama de Hasse, como identificamos com 100% de precisão os elementos MINIMAIS e os elementos MAXIMAIS?",
            "options": {
                "A": "Minimais são os nós com maior número de arestas; Maximais são os nós com menor número de arestas.",
                "B": "Minimais são os vértices que não possuem nenhuma aresta descendo deles (grau inferior nulo); Maximais são os vértices que não possuem nenhuma aresta subindo deles (grau superior nulo).",
                "C": "Minimais ficam sempre no centro do diagrama; Maximais ficam nas bordas laterais.",
                "D": "Minimais e maximais só podem ser identificados por busca em largura no código C.",
            },
            "correct": "B",
            "correct_fb": "Excelente! Na leitura espacial de Hasse: se nenhuma linha desce de um nó, não há ninguém abaixo dele (ele é Minimal!). Se nenhuma linha sobe dele, não há ninguém acima dele (ele é Maximal!).",
            "incorrect_fb": "Incorreto. A assinatura topológica de Hasse é vertical: vértices na base sem arestas para baixo são minimais; vértices no topo sem arestas para cima são maximais.",
        },
        {
            "question": "Qual é a importância histórica e teórica dos diagramas de Hasse do Pentágono N5 e do Diamante M3 na Teoria dos Reticulados?",
            "options": {
                "A": "São exemplos de relações de equivalência perfeitas.",
                "B": "São os contraexemplos fundamentais do Teorema de Birkhoff: N5 prova que um reticulado não é modular, e M3 prova que não é distributivo.",
                "C": "São os únicos reticulados finitos que existem na computação.",
                "D": "Provam que o conjunto das partes não é um poset.",
            },
            "correct": "B",
            "correct_fb": "Brilhante! O Pentágono N5 e o Diamante M3 são os dois contraexemplos mais famosos de toda a álgebra abstrata. Pelo Teorema de Birkhoff, um reticulado é distributivo se, e somente se, não contém N5 nem M3!",
            "incorrect_fb": "Incorreto. N5 e M3 são os contraexemplos anatômicos universais: N5 é o menor reticulado não-modular e M3 é o menor reticulado modular não-distributivo.",
        },
    ],
    "next_step": "PARABÉNS! Você concluiu a Fase 1 (Lógica Matemática, Relações e Conjuntos) com nível de excelência teórica e visual! Agora que seus fundamentos estão inabaláveis, estamos prontos para a Fase 2: Programação em C e Python!",
}

ALL_PHASE1_DATA = {
    1: TOPIC_1_DATA,
    2: TOPIC_2_DATA,
    3: TOPIC_3_DATA,
    4: TOPIC_4_DATA,
    5: TOPIC_5_DATA,
    6: TOPIC_6_DATA,
    7: TOPIC_7_DATA,
    8: TOPIC_8_DATA,
}
