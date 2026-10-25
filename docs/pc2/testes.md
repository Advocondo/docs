# Testes

O back-end tem **814 testes automatizados, todos passando, com 95% de cobertura**, medidos no commit [`d8fba98`](https://github.com/Advocondo/back/tree/d8fba98) da `main`. Eles rodam no CI a cada push e PR, e o merge na `main` só acontece com a suíte verde (ver [Lint](lint.md#ci)).

| Tipo | Funções de teste | O que usa |
| --- | :---: | --- |
| Unitário (`test_<modulo>_unit.py`) | 175 | Só código Python, sem banco |
| Integração (`test_<modulo>_integration.py`) | 370 | A API real (`TestClient`) e um PostgreSQL real |
| **Execuções** | **814** | 114 funções são parametrizadas e rodam uma vez por caso |

Cada teste cita o critério de aceitação que verifica (`"""US14-CA01"""`). Isso permite ligar cada critério aos testes na página [Requisito → código → teste](../rastreabilidade/implementacao.md).

## Teste parametrizado { #teste-parametrizado }

**114 usos de `@pytest.mark.parametrize`, em 21 arquivos.** Um mesmo teste roda com vários casos, e cada caso tem um nome legível dado por `pytest.param(..., id=...)`. Esse nome aparece no relatório e no comando para rodar um caso só.

Exemplo de [`test_app_unit.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/test_app_unit.py), o exemplo de referência do time: o mesmo teste verifica o *health check* com tudo no ar, com o banco fora e com uma dependência externa fora.

```python
@pytest.mark.parametrize(
    ("checks", "status_code", "expected"),
    [
        pytest.param({"database": _ok}, 200,
                     {"status": "ok", "checks": {"database": "ok"}}, id="tudo-ok"),
        pytest.param({"database": _fail}, 503,
                     {"status": "error", "checks": {"database": "error"}}, id="banco-fora"),
        pytest.param({"database": _ok, "email": _fail}, 503,
                     {"status": "error", "checks": {"database": "ok", "email": "error"}},
                     id="dependencia-externa-fora"),
    ],
)
def test_readiness(self, client, override_checks, checks, status_code, expected) -> None:
    override_checks(checks)

    response = client.get("/health/ready")
    ...
```

Outros usos típicos:

- **Regras puras com muitos casos:** CNPJ válido e inválido (numérico, alfanumérico, dígito errado, todos iguais), em [`condominios/test_condominios_unit.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/condominios/test_condominios_unit.py).
- **Plano de parcelas (US17):** divisão exata ou com centavos na última parcela, um centavo por parcela, e vencimentos em meses de 31 e 30 dias, fevereiro e fevereiro bissexto, em [`parcelas/test_parcelas_unit.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/parcelas/test_parcelas_unit.py).
- **Permissão por perfil, pela API:** a mesma rota chamada por Administrador, Equipe Operacional e Cliente, em [`auth/test_auth_integration.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/auth/test_auth_integration.py) e [`landing/test_landing_integration.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/landing/test_landing_integration.py).
- **Parametrizado e integração juntos:** [`test_app_integration.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/test_app_integration.py).

## Teste de integração { #teste-de-integracao }

**370 funções de teste exercitam a API de ponta a ponta:** requisição HTTP, router, service, repository e um **PostgreSQL 18 real**, sem mocks do banco.

### Banco de teste isolado

- Um banco próprio, `advocondo_test`, criado automaticamente. A suíte se recusa a rodar se o nome não terminar em `_test`, para nunca apagar dados reais.
- O schema é recriado a partir dos models no início da suíte.
- **Cada teste roda dentro de uma transação que sofre rollback no fim.** Os `commit()` do código testado viram *savepoints*, então todo teste começa com o banco vazio, sem depender da ordem. Trecho de [`conftest.py`](https://github.com/Advocondo/back/blob/d8fba98/conftest.py):

```python
@pytest.fixture
def db_session(db_engine: Engine) -> Iterator[Session]:
    """Sessão cujo conteúdo é descartado ao fim de cada teste."""
    with db_engine.connect() as connection:
        transaction = connection.begin()
        session = Session(
            bind=connection,
            join_transaction_mode="create_savepoint",
            expire_on_commit=False,
        )
        try:
            yield session
        finally:
            session.close()
            transaction.rollback()
```

- No CI, o job sobe um Postgres 18 próprio, descartado ao fim.

### Fixtures

| Fixture | O que entrega |
| --- | --- |
| `db_client` | Cliente HTTP da API usando o banco de teste, o relógio congelado e a caixa de saída de e-mails |
| `create_user`, `create_condominium`, `create_debtor`... | Fábricas que gravam entidades válidas direto no banco; os campos informados substituem os padrões |
| `authenticate_as(user)` | Cria uma sessão e devolve o cabeçalho `Authorization` |
| `clock` | Relógio congelado; `clock.advance(...)` avança o tempo (expiração de sessões e links, parcelas em atraso) |
| `outbox` | Captura os e-mails enviados, para conferir destinatário e link sem SMTP |

### Exemplo: importação de devedores (US14-CA01)

De [`devedores/test_devedores_integration.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/devedores/test_devedores_integration.py): envia uma planilha `.xlsx` de verdade para a API e confere o relatório por linha e que **nada foi gravado** no banco.

```python
def test_preview_points_rows_with_errors_and_saves_nothing(
    self, db_client: TestClient, operator_headers: dict[str, str], mirante: Condominium
) -> None:
    """US14-CA01"""
    response = import_spreadsheet(db_client, operator_headers, mirante.id, SPREADSHEET)

    assert response.status_code == 200
    body = response.json()
    assert [(row["number"], row["status"]) for row in body["rows"]] == [
        (2, "valid"), (3, "invalid"), (4, "valid"), (5, "similar"),
    ]
    assert body["rows"][1]["errors"] == ["Informe o telefone ou o e-mail do devedor."]
    assert debtor_names(db_client, operator_headers, mirante) == []
```

### Migrations testadas de ponta a ponta

[`test_app_integration.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/test_app_integration.py) aplica todas as migrations num banco separado e compara o resultado com os models. Se alguém mudar um model e esquecer a migration, o CI falha. O mesmo teste confere que o `downgrade` remove tudo.

```python
def test_upgrade_builds_the_schema_described_by_the_models(self, alembic_config, migrations_engine):
    command.upgrade(alembic_config, "head")
    with migrations_engine.connect() as connection:
        differences = compare_metadata(MigrationContext.configure(connection), Base.metadata)
    assert differences == []
```

## Como rodar

```bash
docker compose up -d db
uv run pytest                      # tudo, com cobertura
uv run pytest -m "not integration" # só os unitários, sem banco
uv run pytest src/advocondo/devedores -k TestImportDebtors
```

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 25/10/2026 | Criação da página com os testes parametrizados e de integração do back-end. | Mateus Vieira |
