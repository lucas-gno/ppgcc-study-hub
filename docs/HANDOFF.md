# HANDOFF.md — Guia Mestre de Continuidade e Transição para Novo Desktop

> **Propósito:** Permitir que o usuário ou qualquer agente de IA clone este repositório em outro computador, sem acesso ao histórico de chat anterior, e retome imediatamente a execução sabendo com precisão o estado do projeto, as decisões travadas, a resolução de defeitos visuais e os passos exatos para a **Fase 2 (Tópicos 9 a 18 — Programação em C e Python)**.

---

## 1. Repositório Remoto e Hospedagem em Produção

- **Repositório Público GitHub:** `https://github.com/lucas-gno/ppgcc-study-hub` (`git@github.com:lucas-gno/ppgcc-study-hub.git`)
- **Branch principal:** `main` (inclui `.nojekyll`, `data/mestrado.db` e scripts de automação).
- **GitHub Pages Ativo:** `https://lucas-gno.github.io/ppgcc-study-hub/` (servido da raiz `/`, HTTPS forçado).
- **Clonagem em novo desktop:**
  ```bash
  git clone git@github.com:lucas-gno/ppgcc-study-hub.git
  cd ppgcc-study-hub
  ```

---

## 2. Resolução Crítica de Defeitos Visuais (Aulas Fase 1)

### Por que os diagramas Mermaid falharam inicialmente?
O projeto adota uma arquitetura **100% estática, offline-first e sem CDNs externas** (ADRs 0001 e 0005). Mermaid.js exige uma biblioteca JavaScript pesada carregada via CDN ou bundler complexo para renderizar `<pre><code>flowchart...</code></pre>`. Sem essa dependência, o navegador renderizava o código-fonte cru do Mermaid na tela como um bloco de texto escuro.

### Por que alguns diagramas vieram em ASCII desformatado?
As primeiras versões dos tópicos 6, 7 e 8 no banco `data/mestrado.db` traziam diagramas concebidos em texto ASCII simples (`/ \ | X \ /`, `[M1]`, etc.) dentro de blocos ` ```text ` ou ` ``` `. Em telas de alta resolução, essa representação textual fica truncada, sem hierarquia espacial e visualmente pobre.

### A Solução Implementada (100% SVG Vetorial Nativo)
1. **Módulo de Diagramas Vetoriais (`scripts/svg_diagrams.py`):** Criamos 16 diagramas vetoriais nativos em `<svg>` puro, com `viewBox` responsivo, tipografia de sistema Apple (-apple-system), paleta de alto contraste (`#0071e3`, `#10b981`, `#ef4444`, `#8b5cf6`, `#64748b`), nós arredondados com drop-shadow sutil e bordas elegantes, exatamente na mesma linguagem visual dos widgets interativos que o usuário aprovou.
2. **Container CSS `.visual-diagram-card` (`assets/style.css` e `assets/tufte-clean.css`):**
   - Header com `.diagram-tag` (badge minimalista) e `.diagram-title`;
   - Corpo `.diagram-body` com fundo sutil, centralizado e scroll horizontal seguro em telas móveis;
   - Rodapé `.diagram-caption` com explicação conceitual rigorosa ancorada na banca.
3. **Parser HTML Bloco em `scripts/generate_lessons.py`:** Atualizamos o parser `markdown_to_html` para reconhecer e preservar blocos HTML completos (`<div class="visual-diagram-card">...</div>`, `<svg>...`) sem encapsulá-los indevidamente em `<p>` e sem escapar tags.
4. **Migração do Banco (`scripts/migrate_phase1_diagrams.py`):** Atualizamos a coluna `aulas.conteudo_markdown` no banco SQLite `data/mestrado.db` e regeneramos todos os arquivos `lessons/0001` a `0008` e o bundle `assets/data.js`.
5. **Garantia por Teste Automatizado (`tests/test_ui_contracts.py`):** O teste verifica automaticamente que nenhuma aula contém blocos `language-mermaid`, fluxogramas de texto ou diagramas ASCII crus, exigindo a presença de `.visual-diagram-card`.

---

## 3. Estado Atual dos Tickets (`.scratch/ppgcc-study-hub/issues/`)

| Ticket | Título | Bloqueadores | Status Atual |
| --- | --- | --- | --- |
| **01** | Fundação de Dados Oficiais, Motor Store e Visão do Dia (`index.html`) | Nenhum | `done` |
| **02** | Edital Verticalizado com Progresso e Bibliografia (`edital.html`) | 01 | `done` |
| **03** | Gerador de Aulas Fase 1 (Visual SVG + Interativo + Link Banco + Molde Sandbox) | 02 | `done` |
| **04** | Banco de Questões, Deep-Link `?topico=` e Modo Treino FSRS (`questoes.html`) | 01 | `done` |
| **05** | Simulados Cronometrados (Oficial 120 min e Por Área) (`simulados.html`) | 01, 04 | `ready-for-agent` |
| **06** | Cronograma Real de Dois Sprints (`cronograma.html`) | 01, 02 | `ready-for-agent` |
| **07** | Simulador de Arguição Oral CA05 (`arguicao.html`) | 01 | `ready-for-agent` |
| **08** | Auditoria Curricular Anexo VI, Projeção NF (`curriculo.html`) e Deploy GitHub Pages | 01, 05, 07 | `blocked` |

**Fronteira atual de trabalho:** Tickets **05**, **06** e **07** têm todos os bloqueadores concluídos (`ready-for-agent`).

---

## 4. O que Já Está Funcionando e Verificado

1. **Dados Globais (`data/mestrado.db` -> `assets/data.js`):**
   - 5 Fases do Edital com pesos reais (55% AED, 25% Programação, 20% Lógica e Conjuntos);
   - 37 Tópicos de estudo;
   - 64 Questões totais (20 questões oficiais do Edital 53/2025 com gabarito e resolução passo a passo + 40 questões autorais inéditas com pegadinhas de banca para a Fase 1 + 4 questões complementares);
   - 7 Obras bibliográficas oficiais catalogadas com vínculos diretos aos tópicos;
   - 6 Perguntas de arguição oral modeladas para o Tema CA05 (orientação Prof. Dr. Carlos Maurício).
2. **Motor no Cliente (`assets/store.js`):**
   - Fórmulas oficiais do Edital 43/2026 e Retificação nº 02:
     - $NPE = \text{acertos} \times 0{,}5$ (corte $NPE \ge 3{,}00$);
     - $DA = \min(10, \max(0, IRA - 7{,}0) \times 3{,}34)$ (Anexo VI);
     - $NC = \text{pontos Anexo VI} / 10$;
     - $NF = (NPE + NA + NC) / 3$;
   - Algoritmo determinístico FSRS v5 (ratings 1 a 4 com matriz $S, D, R$);
   - Calendário real de 2 Sprints (Sprint 1: `23/11–03/12/2026` Prova Escrita; Sprint 2: `05/12–13/12/2026` Arguição Oral);
   - Backup JSON completo (Exportar / Importar com validação de integridade).
3. **Páginas Principais Concluídas:**
   - `index.html`: Visão do dia, metas diárias, cards de progresso, atalhos rápidos e modal de backup.
   - `edital.html`: Matriz de tópicos, status de leitura por aula, peso na prova e bibliografia recomendada.
   - `questoes.html`: Banco de questões com filtro por tópicos (`?topico=ID`), alternância 4/5 itens, Modo Treino FSRS, Modo Prova e explicações detalhadas da banca.
4. **Aulas da Fase 1 (`lessons/0001` a `0008`):**
   - 100% livres de emojis;
   - 100% livres de Mermaid ou árvores ASCII desformatadas;
   - Didática Zero Base com Tradução Tríplice (`.como-se-le`);
   - Pilar Visual (diagramas vetoriais `<svg>` nativos) + Pilar Interativo (`assets/widgets.js`);
   - Rodapé com botão de alternância de leitura (`Store.toggleTopicRead`) e botão primário para o Banco de Questões (`../questoes.html?topico=<id>`).

---

## 5. Diretrizes Obrigatórias para a Fase 2 (Tópicos 9 a 18 — Programação C e Python)

Quando o agente no novo desktop iniciar a confecção das aulas da **Fase 2 (Programação)**, ele DEVE seguir estritamente o protocolo abaixo:

### 5.1. Os 10 Tópicos da Fase 2
- **Tópico 09:** Tipos primitivos, operadores, precedência e conversão de tipos (C e Python)
- **Tópico 10:** Estruturas de controle de fluxo e repetição (if, switch, for, while, do-while)
- **Tópico 11:** Funções, escopo de variáveis, passagem por valor e por referência
- **Tópico 12:** Arrays unidimensionais e multidimensionais, strings e buffers em C
- **Tópico 13:** Ponteiros em C: aritmética de ponteiros, ponteiros para ponteiros, ponteiros para funções
- **Tópico 14:** Alocação dinâmica de memória em C: malloc, calloc, realloc, free e vazamento de memória
- **Tópico 15:** Estruturas heterogêneas (struct, union, typedef) e alinhamento de memória/padding
- **Tópico 16:** Manipulação de arquivos em C (fopen, fread, fwrite, fscanf, fprintf, fseek) e Python
- **Tópico 17:** Paradigma procedural vs orientado a objetos em Python (classes, dunder methods, herança)
- **Tópico 18:** Tratamento de exceções, geradores, iteradores e context managers em Python

### 5.2. A Tríade da Aula de Programação
1. **Didática Zero Base com Tradução Tríplice (`.como-se-le`):**
   - Exemplo para ponteiro: `int *ptr = &val;`
   - Formal: Notação C de ponteiro tipado referenciando endereço de memória.
   - Como se lê: *"int asterisco ptr recebe e-comercial val"*.
   - Analogia prática: *"A variável val é uma caixa contendo um valor. &val é o CEP dessa caixa. ptr é um papel onde anotamos o CEP, e *ptr significa ir até o endereço anotado no papel e abrir a caixa"*.
2. **Pilar Visual em SVG Nativo (NUNCA Mermaid, NUNCA ASCII):**
   - Tópico 12 e 13: Diagrama vetorial de blocos de memória contíguos (Stack vs Heap, endereços `0x1000`, `0x1004`, setas de ponteiro apontando para células).
   - Tópico 14: Diagrama de transição de alocação de memória no Heap (`malloc` -> bloco ocupado -> `free` -> dangling pointer / memory leak).
   - Tópico 15: Diagrama de alinhamento de memória (padding de 4 ou 8 bytes na `struct` em arquiteturas x86_64).
   - Tópico 16: Diagrama do cursor de arquivo (`SEEK_SET`, `SEEK_CUR`, `SEEK_END`).
   - Tópico 17 e 18: Diagrama de pilha de chamadas e fluxo de geradores `yield`.
3. **Sandboxes Jupyter no Navegador (`.notebook-cell` — NOTES.md Seção 3):**
   - Obrigatório em todas as aulas da Fase 2!
   - Usar a função `render_notebook_sandbox_shell` em `scripts/generate_lessons.py`.
   - Cada sandbox deve possuir:
     - Topbar com as 3 bolinhas macOS minimalistas (vermelho, amarelo, verde);
     - Título do notebook e badge do kernel (ex: `Kernel Simulado C99` ou `Python 3.12 Runtime`);
     - Editor dark monospaced com o código simulado;
     - Inputs interativos (`.notebook-inputs-group`);
     - Botões **Executar**, **Passo a Passo** e **Resetar**;
     - Console de saída `stdout` colorido;
     - Painel inspetor de memória/variáveis (`.notebook-inspector-panel`) mostrando o estado da Stack/Heap a cada passo.
   - Os inicializadores devem ser implementados em `assets/widgets.js` (ex: `initNotebook09(containerId)`, `initNotebook13(containerId)`, etc.).
4. **Separação Estrita Aulas vs. Questões (ADR 0004):**
   - Nenhuma questão de múltipla escolha deve ser colocada no corpo da aula.
   - O rodapé da aula traz apenas o botão de marcar conclusão (`Store.toggleTopicRead`) e o botão primário para o Banco de Questões (`../questoes.html?topico=<id>`).

### 5.3. Pipeline de Geração e Publicação
Após popular `conteudo_markdown` dos tópicos 9 a 18 em `data/mestrado.db`:
```bash
# 1. Regenerar páginas HTML das aulas
python scripts/generate_lessons.py

# 2. Re-exportar banco para o cliente
python scripts/export_db.py

# 3. Rodar suíte de testes (TDD)
python -m unittest discover -s tests -v
node --test tests/*.test.mjs

# 4. Commit e deploy no GitHub Pages
git add .
git commit -m "feat: implementa aulas e sandboxes jupyter da fase 2 (topicos 09 a 18)"
git push origin main
```

---

## 6. Comandos de Verificação TDD

Ambas as suítes de teste rodam com zero dependências externas:
```powershell
# Testes Python (Pipeline de dados, contratos HTML, zero emojis, SVG nativo, ausência de Mermaid/ASCII)
python -m unittest discover -s tests -v

# Testes JavaScript (Fórmulas oficiais do edital, FSRS v5, filtros, persistência e backup)
node --test tests/*.test.mjs
```
*Estado em 22/11/2026: 100% dos testes verdes em ambas as plataformas.*

---

## 7. Mensagem Pronta de Prompt para o Novo Agente / Novo Desktop

Copie e cole o bloco abaixo no chat ao abrir o projeto na nova máquina:

```text
Olá, agente. Estou continuando o desenvolvimento do PPGCC IFCE Study Hub neste novo desktop.
O repositório Git local já está sincronizado com https://github.com/lucas-gno/ppgcc-study-hub.
Antes de começar, leia obrigatoriamente:
1. AGENTS.md
2. docs/HANDOFF.md
3. GLOSSARY.md
4. docs/BANCA_E_EDITAL_2027.md
5. Os registros arquiteturais em docs/adr/ (ADRs 0001 a 0007).

Execute as suítes de teste para confirmar o estado do projeto:
python -m unittest discover -s tests -v
node --test tests/*.test.mjs

Lembre-se das regras pétreas:
- Zero emojis em qualquer arquivo (ADR 0007);
- Zero CDNs externas (100% offline-first com KaTeX local);
- Zero blocos Mermaid ou ASCII art — qualquer visual deve ser <svg> vetorial nativo responsivo em .visual-diagram-card;
- Sandboxes Jupyter no navegador (.notebook-cell) obrigatórias em aulas de código;
- Zero questões no corpo das aulas (separação estrita para questoes.html?topico=ID).

Prossiga com os tickets na fronteira em .scratch/ppgcc-study-hub/issues/ ou com a geração das aulas da Fase 2 conforme as instruções da Seção 5 de docs/HANDOFF.md.
```
