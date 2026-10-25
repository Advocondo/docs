# Clean Code

As práticas abaixo valem para todo o back-end e são conferidas em revisão de PR e, quando possível, por ferramenta (ver [Lint](lint.md)). Os exemplos vêm do commit [`d8fba98`](https://github.com/Advocondo/back/tree/d8fba98) da `main`.

## Números

Medido com a AST do Python sobre `src/advocondo`, sem os testes:

| Métrica | Valor |
| --- | --- |
| Funções e métodos | 460 |
| Mediana de linhas por função | **6** |
| Funções com até 20 linhas | **93%** |
| Funções com mais de 40 linhas | 6 (listadas em [Onde melhorar](#onde-melhorar)) |
| `# type: ignore` e `# noqa` em todo o código | 6, cada um restrito a uma regra (ver [Lint](lint.md)) |

## 1. Funções pequenas, que fazem uma coisa

O router só traduz HTTP; a regra fica no service. Trecho de [`devedores/router.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/devedores/router.py):

```python
@router.get("/{debtor_id}")
def get_debtor(
    debtor_id: uuid.UUID, debtor_service: DebtorServiceDependency
) -> DebtorResponse:
    return DebtorResponse.model_validate(debtor_service.get(debtor_id))
```

## 2. Regras de negócio puras, isoladas e com nome de domínio

O que pode ser calculado sem banco vira função pura em arquivo próprio, testável sem fixtures. Trecho de [`parcelas/plan.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/parcelas/plan.py):

```python
def split_amount(total: Decimal, installment_count: int) -> list[Decimal]:
    """Equal installments; the cents that do not divide evenly go to the last one,
    so the installments always add up to the total (US17-CA02)."""
    total_cents = to_cents(total)
    base_cents = total_cents // installment_count
    if base_cents == 0:
        raise InstallmentBelowOneCentError()
    amounts = [base_cents] * installment_count
    amounts[-1] += total_cents - base_cents * installment_count
    return [from_cents(cents) for cents in amounts]
```

Outros exemplos: [`devedores/similarity.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/devedores/similarity.py) (quando dois devedores são a mesma pessoa), [`condominios/cnpj.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/condominios/cnpj.py) (dígitos verificadores do CNPJ, inclusive o alfanumérico) e [`parcelas/status.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/parcelas/status.py) (situação da parcela).

## 3. Nomes que dizem a intenção, sem números mágicos

Constantes nomeadas no lugar de números soltos, e o mesmo valor serve ao banco e à validação. Trecho de [`devedores/models.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/devedores/models.py):

```python
MAX_NAME_LENGTH = 200
MAX_UNIT_LENGTH = 50

class Debtor(UuidPrimaryKeyMixin, TimestampsMixin, Base):
    """A resident in default, registered once and reused in every agreement (US13)."""

    __table_args__ = (
        CheckConstraint("phone IS NOT NULL OR email IS NOT NULL", name="has_a_contact"),
    )
```

O código fica em inglês, que é a convenção do time. As mensagens ao usuário ficam em português.

## 4. Erros de domínio em vez de códigos HTTP espalhados

Cada recusa é uma classe com a mensagem ao usuário. Um único handler converte a hierarquia em status HTTP ([`common/errors.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/common/errors.py), [`common/error_handlers.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/common/error_handlers.py)):

```python
class DebtorNotFoundError(NotFoundError):          # → 404
    message = "Devedor não encontrado."

class ContactRequiredError(BusinessRuleError):     # → 422
    message = "Informe o telefone ou o e-mail do devedor."
```

## 5. Dependências explícitas

Nada é buscado em variável global dentro da regra. O service recebe a sessão, os repositories, o relógio, o envio de e-mail e o armazenamento pelo construtor, montados em `dependencies.py`. É isso que permite testar com relógio congelado e e-mail capturado (ver [Testes](testes.md)).

## 6. Tipagem estrita

Todo o código e os testes passam no `mypy --strict`: funções com tipos de entrada e saída, sem `Any` implícito. Os models usam o estilo tipado do SQLAlchemy 2 (`Mapped[str]`).

## 7. Comentários que explicam o porquê

Os comentários explicam a decisão, e não repetem o código. Exemplo de [`common/storage.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/common/storage.py):

```python
# The object is written before the row is committed. If the commit fails,
# an orphan object is left in the bucket, which is harmless.
```

## 8. Estrutura previsível

Todo módulo tem os mesmos arquivos, e os testes ficam ao lado do código, com no máximo dois arquivos por módulo (`_unit` e `_integration`). As convenções estão escritas em `docs/testes.md` e no README do back, e nesta documentação em [Arquitetura](../arquitetura/index.md).

## Onde melhorar

As seis funções com mais de 40 linhas são candidatas a divisão:

| Função | Linhas |
| --- | :---: |
| `acordos/service.py` · `AgreementService.update` | 92 |
| `painel_admin/repository.py` · `list_installments_for_export` | 86 |
| `documentos/agreement_pdf.py` · `build_agreement_document` | 58 |
| `painel_admin/export.py` · `build_installment_workbook` | 52 |
| `parcelas/service.py` · `_change_amount` | 43 |
| `users/service.py` · `invite` | 41 |

Também estão registrados para depois da entrega:
- dividir o módulo `users`, que tem cinco serviços num arquivo;
- juntar o código repetido dos e-mails de convite e de redefinição;
- remover as checagens mortas do router de condomínios ([R7](../acompanhamento/pendencias.md#riscos)).

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 25/10/2026 | Criação da página com as práticas de Clean Code e as métricas do back-end. | Mateus Vieira |
