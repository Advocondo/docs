# Lint e análise estática

Lint, formatação, checagem de tipos e busca de segredos rodam automaticamente **a cada push e a cada PR**, nos dois repositórios. Também dá para rodar tudo antes do commit, com os mesmos comandos.

## Back-end

| Ferramenta | O que verifica | Comando |
| --- | --- | --- |
| **ruff** (lint) | Conjunto padrão do ruff 0.16, com 415 regras ativas: erros e nomes indefinidos (pyflakes), sintaxe moderna (pyupgrade), armadilhas comuns (bugbear), simplificações (simplify), regras do pylint, datas sem fuso (`DTZ`), uso de `pytest`, ordem de imports e outras | `uv run ruff check .` |
| **ruff** (formatação) | Formatação única do código, sem discussão de estilo em revisão | `uv run ruff format --check .` |
| **mypy** `--strict` | Tipos em todas as funções e testes, sem `Any` implícito nem chamada sem tipo | `uv run mypy` |
| **gitleaks** | Senhas, tokens e chaves commitados por engano, em todo o histórico do repositório | CI |
| **pytest-cov** | Cobertura dos testes, com o resumo no job e o `coverage.xml` como artefato | `uv run pytest` |

No código inteiro há só 6 supressões, todas restritas a uma regra específica: um `# noqa: F401` para um import que registra os models, um `# type: ignore[call-arg]` porque o `Settings()` lê os campos do ambiente, e quatro `# type: ignore[arg-type]` num teste unitário que usa repositórios falsos.

## Front-end

| Ferramenta | O que verifica | Comando |
| --- | --- | --- |
| **ESLint** | Regras do Next.js (`core-web-vitals`) e do TypeScript | `npm run lint` |
| **TypeScript** (`tsc --noEmit`) | Tipos de todo o projeto, com os tipos das rotas gerados pelo Next | `npx next typegen && npx tsc --noEmit` |
| **gitleaks** | Segredos commitados | CI |
| **Vitest** | Testes unitários | `npm run test` |

As regras de camadas da [arquitetura do front](../arquitetura/index.md#front-end) entram no ESLint com `no-restricted-imports` (um componente não importa services; `fetch` só nos services) quando a estrutura `modules/` chegar à `main`.

## CI { #ci }

| Repositório | Workflow | Etapas |
| --- | --- | --- |
| back | [`.github/workflows/ci.yml`](https://github.com/Advocondo/back/blob/d8fba98/.github/workflows/ci.yml) | gitleaks → `uv sync --locked` → ruff check → ruff format --check → mypy → pytest com cobertura (Postgres 18 próprio do job) → build da imagem de produção (`Dockerfile.prod`) |
| front | [`.github/workflows/ci.yml`](https://github.com/Advocondo/front/blob/main/.github/workflows/ci.yml) | gitleaks → `npm ci` → ESLint → typegen + `tsc` → testes → `next build` |

**A `main` do back é protegida:** um PR só pode entrar se os jobs *Lint e testes* e *Build da imagem de produção* passarem. Código fora do padrão não chega à `main`. Na `main` de 25/10/2026, todos os checks estão verdes.

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 25/10/2026 | Criação da página com as ferramentas de lint, formatação, tipos e segredos e o CI dos dois repositórios. | Mateus Vieira |
