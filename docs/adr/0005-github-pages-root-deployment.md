# ADR 0005: Publicação Direta na Raiz da Branch Main no GitHub Pages

- **Status:** Aprovado
- **Data:** 2026-11-22
- **Decisor:** Lucas Galdino (Usuário) & Antigravity (Agente)

---

## Contexto e Problema
O repositório do projeto será privado na conta GitHub do usuário e hospedará a versão web do Study Hub para acesso pessoal no celular, tablet e desktop. Precisávamos definir o método de entrega no GitHub Pages entre deploy nativo da raiz (`/`), deploy de pasta `/docs` ou pipeline de CI/CD com GitHub Actions.

## Decisão
Configuraremos a publicação direta a partir da raiz da branch `main` (`/`):
- O arquivo principal de entrada será `index.html` na raiz do repositório.
- Todos os caminhos de assets e links relativos usarão `./assets/...` e `./lessons/...` para compatibilidade universal tanto em subcaminhos do GitHub Pages (`https://<user>.github.io/<repo>/`) quanto em domínios personalizados ou execução local.
- Elimina-se qualquer pipeline de GitHub Actions ou build step na nuvem: o repositório é 100% estático e pronto para servir.

## Consequências
### Positivas
- **Simplicidade Máxima:** Sem containers de build no GitHub Actions, sem tempo de espera de compilação na nuvem e sem consumo de minutos de CI.
- **Transparência e Rapidez:** Um `git push` atualiza o site imediatamente no GitHub Pages.
- **Portabilidade:** A mesma estrutura que roda no GitHub Pages funciona offline no computador local via duplo clique.
