# API externa

O back-end se integra a três serviços externos pela API de cada um e também expõe a sua própria API REST, consumida pelo front-end.

## Serviços externos consumidos

| Serviço | Para quê | Biblioteca / protocolo | Código |
| --- | --- | --- | --- |
| **Amazon S3** ou compatível (Cloudflare R2, Backblaze B2) | Guardar os PDFs dos acordos ([US24](../historias/ep03-cadastro-acordos.md#us24)) | API S3 via `boto3` (`put_object`, `get_object`) | [`common/storage.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/common/storage.py) |
| **Servidor SMTP** | E-mails de convite ([US07](../historias/ep02-usuarios-perfis.md#us07)) e de redefinição de senha ([US03](../historias/ep01-portal-autenticacao.md#us03)) | SMTP com STARTTLS (`smtplib`) | [`common/email.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/common/email.py) |
| **Sentry** | Rastrear erros e desempenho em produção | SDK `sentry-sdk[fastapi]` | [`sentry.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/sentry.py) |

### Como a integração é isolada

Cada serviço fica atrás de uma interface (`Protocol`), e a regra de negócio só conhece a interface. A implementação concreta é escolhida pela configuração e injetada pelo FastAPI:

```python
class FileStorage(Protocol):
    def save(self, file: StoredFileMixin, key: str, content: bytes, content_type: str) -> None: ...
    def load(self, file: StoredFileMixin) -> bytes: ...
```

| Interface | Implementações | Escolha |
| --- | --- | --- |
| `FileStorage` | `ObjectStorage` (bucket S3, via `boto3`) · `DatabaseStorage` (bytes na própria linha do banco) | Com as variáveis `S3_*` definidas, usa o bucket; vazias, usa o banco. Uma configuração pela metade impede a API de subir. |
| `EmailSender` | `SmtpEmailSender` · `LogEmailSender` (só no ambiente local, escreve no log) | Com `SMTP_HOST`, usa SMTP; sem ele, só funciona com `ENVIRONMENT=local`, para não vazar links de redefinição em log de produção. |

Decisões que vale destacar:

- **Os PDFs não ficam públicos.** A API lê o objeto do bucket e o entrega ela mesma, então quem não pode ver o acordo não baixa o PDF ([US24-CA03](../historias/ep03-cadastro-acordos.md#us24)). Não há URL pública nem pré-assinada.
- **Arquivos antigos continuam acessíveis.** A leitura olha onde cada arquivo foi gravado, e não a configuração atual, então ligar o bucket depois não quebra os PDFs que já estão no banco.
- **Privacidade no Sentry:** `send_default_pii=False`, para não enviar IP, cookies nem cabeçalhos com dados de devedores.
- **Timeout** de 10 segundos no SMTP, para uma falha do servidor de e-mail não travar a requisição.

### Como é testado sem chamar o serviço real

| Serviço | Teste |
| --- | --- |
| S3 | `FakeS3Client` (`tests/support/storage.py`) no lugar do cliente `boto3`: os testes de integração de [`documentos`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/documentos/test_documentos_integration.py) geram o PDF pela API e conferem o objeto gravado no "bucket" e o download. |
| SMTP | `FakeSmtp` no lugar do `smtplib.SMTP`, em [`common/test_common_unit.py`](https://github.com/Advocondo/back/blob/d8fba98/src/advocondo/common/test_common_unit.py), confere STARTTLS, login e mensagem. Nos testes de integração, a fixture `outbox` captura os e-mails enviados pela API. |
| Sentry | Desligado nos testes (sem `SENTRY_DSN`). `test_app_unit.py` confere que ele só liga quando a variável existe. |

A configuração de cada serviço em produção está em [Deploy → variáveis de ambiente](../infraestrutura/deploy.md#variaveis-de-ambiente-do-back-end).

## API própria (REST)

O back-end expõe uma API REST em JSON. O FastAPI gera o esquema **OpenAPI** e a documentação interativa em `/docs` (Swagger UI) e `/redoc`, onde cada rota pode ser chamada pelo navegador. Todas as rotas exigem `Authorization: Bearer <token>`, com a permissão conferida por perfil. As exceções são as públicas: login, redefinição de senha, aceite de convite, leitura da página institucional e das imagens dela, health checks e `POST /setup`, que exige o token de instalação em vez do login.

A tabela abaixo é gerada do esquema OpenAPI pelo script [`scripts/rotas_api.py`](https://github.com/Advocondo/docs/blob/main/scripts/rotas_api.py). A coluna Referência leva à página que descreve campos, regras e erros de cada grupo.

<!-- rotas-api:inicio -->

**60 operações** em 14 grupos.

| Grupo | Operações | Referência |
| --- | --- | --- |
| `health` | `GET /health`<br>`GET /health/ready` | [`docs/observabilidade.md`](https://github.com/Advocondo/back/blob/main/docs/observabilidade.md) |
| `auth` | `POST /auth/login`<br>`GET /auth/me`<br>`POST /auth/logout`<br>`DELETE /auth/sessions`<br>`POST /auth/password-reset`<br>`POST /auth/password-reset/confirm` | [`docs/auth.md`](https://github.com/Advocondo/back/blob/main/docs/auth.md) |
| `setup` | `POST /setup` | [`docs/auth.md`](https://github.com/Advocondo/back/blob/main/docs/auth.md) |
| `users` | `PATCH /users/me`<br>`POST /users/invites`<br>`POST /users/invites/accept`<br>`GET /users/lawyers`<br>`PATCH /users/{user_id}/status`<br>`PATCH /users/{user_id}/monthly-goal`<br>`GET /users/{user_id}/condominiums`<br>`PUT /users/{user_id}/condominiums`<br>`PATCH /users/{user_id}/role`<br>`GET /users/{user_id}/history` | [`docs/users.md`](https://github.com/Advocondo/back/blob/main/docs/users.md) |
| `goals` | `PUT /users/{user_id}/goals/{year}/{month}`<br>`GET /goals/me` | [`docs/metas.md`](https://github.com/Advocondo/back/blob/main/docs/metas.md) |
| `condominiums` | `POST /condominiums`<br>`GET /condominiums`<br>`GET /condominiums/{condominium_id}`<br>`PATCH /condominiums/{condominium_id}` | [`docs/condominios.md`](https://github.com/Advocondo/back/blob/main/docs/condominios.md) |
| `debtors` | `POST /debtors`<br>`GET /debtors`<br>`POST /debtors/import`<br>`GET /debtors/import/template`<br>`GET /debtors/{debtor_id}`<br>`PATCH /debtors/{debtor_id}` | [`docs/devedores.md`](https://github.com/Advocondo/back/blob/main/docs/devedores.md) |
| `agreements` | `POST /agreements`<br>`GET /agreements`<br>`GET /agreements/{agreement_id}`<br>`PATCH /agreements/{agreement_id}`<br>`POST /agreements/{agreement_id}/cancel`<br>`PUT /agreements/{agreement_id}/responsible-lawyer`<br>`GET /agreements/{agreement_id}/lawyer-history` | [`docs/acordos.md`](https://github.com/Advocondo/back/blob/main/docs/acordos.md) |
| `agreement-pdfs` | `POST /agreements/{agreement_id}/pdfs`<br>`GET /agreements/{agreement_id}/pdfs`<br>`GET /agreements/{agreement_id}/pdfs/{pdf_id}` | [`docs/documentos.md`](https://github.com/Advocondo/back/blob/main/docs/documentos.md) |
| `installments` | `GET /agreements/{agreement_id}/installments`<br>`GET /installments`<br>`GET /installments/paid-without-invoice`<br>`PUT /installments/{installment_id}/invoice`<br>`PATCH /installments/{installment_id}`<br>`POST /installments/{installment_id}/payment`<br>`PUT /installments/{installment_id}/payment`<br>`DELETE /installments/{installment_id}/payment`<br>`GET /installments/{installment_id}/payments` | [`docs/parcelas.md`](https://github.com/Advocondo/back/blob/main/docs/parcelas.md) |
| `admin-panel` | `GET /admin-panel/financial`<br>`GET /admin-panel/dashboard`<br>`GET /admin-panel/reports/export` | sem página própria |
| `operator-panel` | `GET /operator-panel/financial` | sem página própria |
| `client-panel` | `GET /client-panel/agreements` | [`docs/painel-cliente.md`](https://github.com/Advocondo/back/blob/main/docs/painel-cliente.md) |
| `landing` | `GET /landing`<br>`PATCH /landing`<br>`POST /landing/images`<br>`GET /landing/images/{image_id}`<br>`DELETE /landing/images/{image_id}` | [`docs/landing.md`](https://github.com/Advocondo/back/blob/main/docs/landing.md) |

<!-- rotas-api:fim -->

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 25/10/2026 | Criação da página com as integrações externas (S3, SMTP e Sentry) e as rotas da API. | Mateus Vieira |
