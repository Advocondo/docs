---
icon: lucide/clipboard-check
---

# PC2 · Critérios técnicos

Evidências do segundo ponto de controle. Cada critério vale 2,5 pontos, num total de 20. Cada um aponta para a página que o explica e para o código no GitHub.

!!! info "Versão conferida"
    Os links para o código apontam para o commit [`d8fba98`](https://github.com/Advocondo/back/tree/d8fba98) da `main` do back-end, de 25/10/2026, para não mudarem depois. Nessa versão, a suíte tem **814 testes passando, com 95% de cobertura**, e o CI está verde.

| Critério | Peso | Onde está | Evidência principal |
| --- | :---: | --- | --- |
| Arquitetura | 2,5 | [Arquitetura](../arquitetura/index.md) | MVC + Camadas em 13 módulos por domínio: [`router.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/devedores/router.py) → [`service.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/devedores/service.py) → [`repository.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/devedores/repository.py) → [`models.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/devedores/models.py) |
| Clean Code | 2,5 | [Clean Code](clean-code.md) | Mediana de 6 linhas por função e 93% das funções com até 20 linhas; nomes que dizem a regra; erros de domínio; regras puras isoladas; tipagem estrita |
| Teste parametrizado | 2,5 | [Testes](testes.md#teste-parametrizado) | 114 usos de `@pytest.mark.parametrize` em 21 arquivos, com casos nomeados por `pytest.param(..., id=...)` |
| Teste de integração | 2,5 | [Testes](testes.md#teste-de-integracao) | 370 testes de integração pela API contra um PostgreSQL real, isolados por transação; migrations testadas de ponta a ponta |
| Banco de dados | 2,5 | [Banco de dados](banco-de-dados.md) | PostgreSQL 18, SQLAlchemy 2 e 23 migrations Alembic versionadas, aplicadas no deploy |
| Modelo físico do banco | 2,5 | [Modelo físico](modelo-fisico.md) | Diagrama ER e dicionário de dados das 17 tabelas, gerados dos models, com tipos, chaves, índices e `CHECK` |
| API externa | 2,5 | [API externa](api-externa.md) | Integrações com Amazon S3 (`boto3`), SMTP e Sentry, isoladas atrás de interfaces; a API REST própria tem 60 operações documentadas em OpenAPI |
| Lint (e derivados) | 2,5 | [Lint](lint.md) | ruff (lint e formatação), mypy `--strict` e gitleaks no CI do back; ESLint e `tsc` no CI do front; merge na `main` só com os checks verdes |

Para a situação de cada história e o que ainda falta, veja [Acompanhamento da entrega](../acompanhamento/index.md).

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 25/10/2026 | Criação da página com as evidências dos critérios do PC2. | Mateus Vieira |
