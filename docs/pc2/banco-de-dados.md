# Banco de dados

| | |
| --- | --- |
| SGBD | **PostgreSQL 18**: o mesmo no desenvolvimento (docker-compose), no CI e em produção (Coolify) |
| Acesso | **SQLAlchemy 2** (ORM tipado, `Mapped[...]`), com o driver `psycopg` 3 |
| Evolução do schema | **Alembic**: 23 migrations versionadas no repositório |
| Tabelas | 17. Ver o [modelo físico](modelo-fisico.md) |

## Como a aplicação usa o banco

- **Uma sessão por requisição.** A dependência `get_session` de [`db.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/db.py) abre a sessão, o FastAPI a injeta no service pelo `dependencies.py` do módulo, e ela é fechada no fim da requisição.
- **Só o service faz `commit`.** O repository consulta e faz `flush`, e o service decide quando a operação inteira termina. Uma operação com várias gravações, como cadastrar um acordo e gerar as parcelas, entra inteira ou não entra.
- **Engine criada sob demanda,** com `pool_pre_ping`. Importar a aplicação não exige banco, e `GET /health/ready` verifica a conexão.
- **Regras também no banco.** O que não pode ser violado está declarado como restrição, além da validação da API: `CHECK`, `UNIQUE` e chaves estrangeiras. Por exemplo, o devedor precisa de telefone ou e-mail, os honorários não passam do total do acordo e o condomínio mais os honorários de cada parcela somam o valor dela.
- **Nomes previsíveis de restrições.** Uma convenção em `db.py` gera `pk_<tabela>`, `uq_<tabela>_<coluna>`, `fk_<tabela>_<coluna>_<tabela_ref>` e `ck_<tabela>_<nome>`, então as migrations podem alterar uma restrição pelo nome em qualquer ambiente.
- **Corrida tratada pelo banco.** Por exemplo, dois cadastros simultâneos com o mesmo CNPJ: a restrição `UNIQUE` barra o segundo, e o repository converte o erro em conflito (409).
- **Enums como texto + `CHECK`** (`common/models.py`, `string_enum`): um valor novo não precisa de `ALTER TYPE`.
- **Valores em dinheiro** como `NUMERIC(12, 2)`, nunca `float`. As divisões são feitas em centavos inteiros (`parcelas/plan.py`).

## Migrations { #migrations }

O schema nunca é criado com `create_all` fora dos testes: toda mudança é uma migration revisada e versionada junto com o código.

```bash
uv run alembic revision --autogenerate -m "create debtors table"   # gera a partir dos models
uv run alembic upgrade head                                         # aplica
uv run alembic downgrade -1                                         # desfaz a última
```

- **No deploy,** o Coolify roda `alembic upgrade head` como *pre-deployment command*, antes de a nova versão da API subir (ver [Deploy](../infraestrutura/deploy.md)).
- **Testadas no CI:** um teste aplica todas as migrations num banco separado e compara o resultado com os models. Se alguém mudar um model e esquecer a migration, o CI falha. O mesmo teste confere que o `downgrade` remove tudo (ver [Testes](testes.md#teste-de-integracao)).
- **Uma head só:** um teste falha se duas branches criarem migrations a partir da mesma base. Isso já quebrou a `main` uma vez ([back#74](https://github.com/Advocondo/back/issues/74)) e motivou o teste.
- O guia completo está em [`docs/migracoes.md`](https://github.com/Advocondo/back/blob/d8fba98/docs/migracoes.md), no back.

### Linha do tempo

| Data | Revisão | Mudança |
| --- | --- | --- |
| 10/10 | `0f214271f4c1` | Tabela `users` |
| 10/10 | `2320693c0417` | Tabela `user_sessions` |
| 11/10 | `0557c13f7116` | Tabela `password_reset_links` |
| 16/10 | `1ffb2dbe4380` | Marcação de advogado e tabela `user_invites` |
| 17/10 | `4ff598a0040e` | Tabela `condominiums` |
| 17/10 | `7328a7cea479` | Tabela `debtors` |
| 17/10 | `b43c7c5ba95d` | Tabela `agreements` |
| 17/10 | `4a5a3c0040a0` | Tabela `installments` |
| 17/10 | `39cb57f92c5e` | Honorários no acordo |
| 17/10 | `9aa921c54a85` | Divisão de cada parcela entre condomínio e honorários |
| 18/10 | `a3c5e8d19b72` | Tabela `user_condominiums` (Cliente ↔ condomínio) |
| 19/10 | `de7be5d29c0e` | Tabela `user_audit_logs` |
| 19/10 | `a49e0752dcdc` | Tabela `goals` |
| 21/10 | `3c0def97fc59` | Advogado responsável e tabela `lawyer_assignments` |
| 21/10 | `71c5d24e8f31` | Meta mensal no usuário (ver o risco [R1](../acompanhamento/pendencias.md#riscos)) |
| 21/10 | `33fed27dfa21` | Tabela `installment_payments` (pagamento parcial) |
| 22/10 | `bb373c1b6d78` | Nota fiscal da parcela |
| 22/10 | `03141b30ed61` | Quem fechou o acordo |
| 22/10 | `183ab32038c5` | Tabelas `landing_blocks` e `landing_images` |
| 22/10 | `79f61dbc2fd4` | Mudanças de vínculo no histórico de usuários |
| 22/10 | `0dc95a13e280` | Tabela `agreement_pdfs` |
| 22/10 | `c8e41f5a7d03` | Cancelamento do acordo |
| 23/10 | `363f6ddd39a5` | Tabela `agreement_edit_logs` |

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 25/10/2026 | Criação da página com o uso do PostgreSQL, do SQLAlchemy e das migrations Alembic. | Mateus Vieira |
