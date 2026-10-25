# Requisito → código → teste

Esta matriz liga cada critério de aceitação ao módulo do back-end que o implementa, às rotas da API e aos testes automatizados que o verificam. Ela completa a [matriz de rastreabilidade](matriz.md), que trata das dependências entre histórias.

!!! info "Origem dos dados (25/10/2026)"
    - **Módulo e rotas:** esquema OpenAPI da API na `main` do [back-end](https://github.com/Advocondo/back) e páginas de referência em `docs/` desse repositório.
    - **Testes:** busca, em todos os arquivos `test_*.py`, pelo identificador do critério (`US13-CA01`) na docstring, no corpo ou no id de parametrização de cada teste. É a convenção do time para marcar o critério verificado.
    - Os caminhos dos testes são relativos a `src/advocondo/`. Na `main`, os 814 testes passam, com 95% de cobertura.

**Resumo:** dos 87 critérios, 70 pertencem a histórias já entregues no back, e **59** deles têm ao menos um teste que os cita. Os 11 restantes são das histórias [US08](../historias/ep02-usuarios-perfis.md#us08) e [US32](../historias/ep05-comissoes-metas.md#us32)–[US35](../historias/ep05-comissoes-metas.md#us35), descritas em [Pendências e riscos](../acompanhamento/pendencias.md#riscos).

| Situação do critério | Quantidade |
| --- | :---: |
| História entregue e critério citado por teste | 59 |
| História entregue, mas nenhum teste cita o critério | 11 |
| História pendente ou em revisão no back | 14 |
| História só de front ([US01](../historias/ep01-portal-autenticacao.md#us01)) | 3 |
| **Total** | **87** |

## EP01 · Portal & Autenticação { #ep01 }

| História | Módulo | Rotas | Critério | Testes que o citam |
| --- | --- | --- | --- | --- |
| [US01](../historias/ep01-portal-autenticacao.md#us01) | front | — | [US01-CA01](../historias/ep01-portal-autenticacao.md#us01) | só front |
|  |  |  | [US01-CA02](../historias/ep01-portal-autenticacao.md#us01) | só front |
|  |  |  | [US01-CA03](../historias/ep01-portal-autenticacao.md#us01) | só front |
| [US02](../historias/ep01-portal-autenticacao.md#us02) | `auth` | `POST /auth/login` · `GET /auth/me` · `POST /auth/logout` | [US02-CA01](../historias/ep01-portal-autenticacao.md#us02) | **3** · `auth/test_auth_integration.py` ×3 |
|  |  |  | [US02-CA02](../historias/ep01-portal-autenticacao.md#us02) | **1** · `auth/test_auth_integration.py` |
|  |  |  | [US02-CA03](../historias/ep01-portal-autenticacao.md#us02) | **3** · `auth/test_auth_integration.py` ×2, `users/test_users_unit.py` |
| [US03](../historias/ep01-portal-autenticacao.md#us03) | `auth` | `POST /auth/password-reset` · `POST /auth/password-reset/confirm` | [US03-CA01](../historias/ep01-portal-autenticacao.md#us03) | **3** · `auth/test_auth_integration.py` ×3 |
|  |  |  | [US03-CA02](../historias/ep01-portal-autenticacao.md#us03) | **4** · `auth/test_auth_integration.py` ×4 |
|  |  |  | [US03-CA03](../historias/ep01-portal-autenticacao.md#us03) | **2** · `auth/test_auth_integration.py` ×2 |
| [US04](../historias/ep01-portal-autenticacao.md#us04) | `landing` | `GET`/`PATCH /landing` · `POST /landing/images` · `GET`/`DELETE /landing/images/{id}` | [US04-CA01](../historias/ep01-portal-autenticacao.md#us04) | **2** · `landing/test_landing_integration.py` ×2 |
|  |  |  | [US04-CA02](../historias/ep01-portal-autenticacao.md#us04) | **5** · `landing/test_landing_integration.py` ×5 |
| [US05](../historias/ep01-portal-autenticacao.md#us05) | `users` | `PATCH /users/me` | [US05-CA01](../historias/ep01-portal-autenticacao.md#us05) | **3** · `users/test_users_integration.py` ×3 |
|  |  |  | [US05-CA02](../historias/ep01-portal-autenticacao.md#us05) | **2** · `users/test_users_integration.py` ×2 |
| [US06](../historias/ep01-portal-autenticacao.md#us06) | `auth` | `DELETE /auth/sessions` | [US06-CA01](../historias/ep01-portal-autenticacao.md#us06) | **1** · `auth/test_auth_integration.py` |

## EP02 · Gestão de Usuários { #ep02 }

| História | Módulo | Rotas | Critério | Testes que o citam |
| --- | --- | --- | --- | --- |
| [US07](../historias/ep02-usuarios-perfis.md#us07) | `users` | `POST /users/invites` · `POST /users/invites/accept` · `GET /users/lawyers` | [US07-CA01](../historias/ep02-usuarios-perfis.md#us07) | **4** · `users/test_users_integration.py` ×4 |
|  |  |  | [US07-CA02](../historias/ep02-usuarios-perfis.md#us07) | **2** · `users/test_users_integration.py` ×2 |
|  |  |  | [US07-CA03](../historias/ep02-usuarios-perfis.md#us07) | **3** · `users/test_users_integration.py` ×3 |
|  |  |  | [US07-CA04](../historias/ep02-usuarios-perfis.md#us07) | **6** · `users/test_users_integration.py` ×6 |
| [US08](../historias/ep02-usuarios-perfis.md#us08) | `users, auth` | `PATCH /users/{id}/status` | [US08-CA01](../historias/ep02-usuarios-perfis.md#us08) | :warning: nenhum teste cita o critério |
|  |  |  | [US08-CA02](../historias/ep02-usuarios-perfis.md#us08) | :warning: nenhum teste cita o critério |
|  |  |  | [US08-CA03](../historias/ep02-usuarios-perfis.md#us08) | :warning: nenhum teste cita o critério |
| [US09](../historias/ep02-usuarios-perfis.md#us09) | `users` | `PATCH /users/{id}/role` | [US09-CA01](../historias/ep02-usuarios-perfis.md#us09) | **3** · `users/test_users_integration.py` ×3 |
|  |  |  | [US09-CA02](../historias/ep02-usuarios-perfis.md#us09) | **2** · `users/test_users_integration.py` ×2 |
| [US10](../historias/ep02-usuarios-perfis.md#us10) | `users` | `GET`/`PUT /users/{id}/condominiums` | [US10-CA01](../historias/ep02-usuarios-perfis.md#us10) | **3** · `users/test_users_integration.py` ×3 |
|  |  |  | [US10-CA02](../historias/ep02-usuarios-perfis.md#us10) | **5** · `documentos/test_documentos_integration.py`, `painel_cliente/test_painel_cliente_integration.py`, `users/test_users_integration.py` ×3 |
| [US11](../historias/ep02-usuarios-perfis.md#us11) | `users` | `GET /users/{id}/history` | [US11-CA01](../historias/ep02-usuarios-perfis.md#us11) | **8** · `users/test_users_integration.py` ×8 |
|  |  |  | [US11-CA02](../historias/ep02-usuarios-perfis.md#us11) | **2** · `users/test_users_integration.py` ×2 |

## EP03 · Cadastro de Acordos { #ep03 }

| História | Módulo | Rotas | Critério | Testes que o citam |
| --- | --- | --- | --- | --- |
| [US12](../historias/ep03-cadastro-acordos.md#us12) | `condominios` | `POST`/`GET /condominiums` · `GET`/`PATCH /condominiums/{id}` | [US12-CA01](../historias/ep03-cadastro-acordos.md#us12) | **1** · `acordos/test_acordos_integration.py` |
|  |  |  | [US12-CA02](../historias/ep03-cadastro-acordos.md#us12) | **1** · `condominios/test_condominios_integration.py` |
| [US13](../historias/ep03-cadastro-acordos.md#us13) | `devedores` | `POST`/`GET /debtors` · `GET`/`PATCH /debtors/{id}` | [US13-CA01](../historias/ep03-cadastro-acordos.md#us13) | **3** · `devedores/test_devedores_integration.py` ×2, `devedores/test_devedores_unit.py` |
| [US14](../historias/ep03-cadastro-acordos.md#us14) | `devedores` | `POST /debtors/import` · `GET /debtors/import/template` | [US14-CA01](../historias/ep03-cadastro-acordos.md#us14) | **1** · `devedores/test_devedores_integration.py` |
|  |  |  | [US14-CA02](../historias/ep03-cadastro-acordos.md#us14) | **2** · `devedores/test_devedores_integration.py` ×2 |
| [US15](../historias/ep03-cadastro-acordos.md#us15) | `acordos` | `POST`/`GET /agreements` · `GET /agreements/{id}` | [US15-CA01](../historias/ep03-cadastro-acordos.md#us15) | **2** · `acordos/test_acordos_integration.py` ×2 |
|  |  |  | [US15-CA02](../historias/ep03-cadastro-acordos.md#us15) | **3** · `acordos/test_acordos_integration.py`, `acordos/test_acordos_unit.py` ×2 |
|  |  |  | [US15-CA03](../historias/ep03-cadastro-acordos.md#us15) | **2** · `acordos/test_acordos_integration.py` ×2 |
| [US16](../historias/ep03-cadastro-acordos.md#us16) | `acordos, parcelas` | `POST /agreements` (`fee_percentage`) · divisão por parcela em `parcelas/plan.py` | [US16-CA01](../historias/ep03-cadastro-acordos.md#us16) | **4** · `acordos/test_acordos_integration.py`, `acordos/test_acordos_unit.py`, `parcelas/test_parcelas_integration.py`, `parcelas/test_parcelas_unit.py` |
|  |  |  | [US16-CA02](../historias/ep03-cadastro-acordos.md#us16) | **2** · `parcelas/test_parcelas_integration.py`, `parcelas/test_parcelas_unit.py` |
| [US17](../historias/ep03-cadastro-acordos.md#us17) | `parcelas` | `GET /agreements/{id}/installments` · `PATCH /installments/{id}` | [US17-CA01](../historias/ep03-cadastro-acordos.md#us17) | **3** · `acordos/test_acordos_integration.py`, `parcelas/test_parcelas_integration.py`, `parcelas/test_parcelas_unit.py` |
|  |  |  | [US17-CA02](../historias/ep03-cadastro-acordos.md#us17) | **4** · `parcelas/test_parcelas_integration.py` ×2, `parcelas/test_parcelas_unit.py` ×2 |
|  |  |  | [US17-CA03](../historias/ep03-cadastro-acordos.md#us17) | **6** · `parcelas/test_parcelas_integration.py` ×5, `parcelas/test_parcelas_unit.py` |
| [US18](../historias/ep03-cadastro-acordos.md#us18) | `acordos` | `PUT /agreements/{id}/responsible-lawyer` · `GET /agreements/{id}/lawyer-history` | [US18-CA01](../historias/ep03-cadastro-acordos.md#us18) | **12** · `acordos/test_acordos_integration.py` ×5, `acordos/test_acordos_unit.py` ×3, `users/test_users_integration.py` ×3, `users/test_users_unit.py` |
|  |  |  | [US18-CA02](../historias/ep03-cadastro-acordos.md#us18) | **5** · `acordos/test_acordos_integration.py` ×3, `acordos/test_acordos_unit.py` ×2 |
|  |  |  | [US18-CA03](../historias/ep03-cadastro-acordos.md#us18) | **1** · `acordos/test_acordos_integration.py` |
| [US19](../historias/ep03-cadastro-acordos.md#us19) | `acordos` | `PATCH /agreements/{id}` | [US19-CA01](../historias/ep03-cadastro-acordos.md#us19) | **6** · `acordos/test_acordos_integration.py` ×4, `acordos/test_acordos_unit.py` ×2 |
|  |  |  | [US19-CA02](../historias/ep03-cadastro-acordos.md#us19) | **2** · `acordos/test_acordos_integration.py` ×2 |
| [US20](../historias/ep03-cadastro-acordos.md#us20) | `acordos` | `POST /agreements/{id}/cancel` | [US20-CA01](../historias/ep03-cadastro-acordos.md#us20) | **1** · `parcelas/test_parcelas_integration.py` |
|  |  |  | [US20-CA02](../historias/ep03-cadastro-acordos.md#us20) | **1** · `parcelas/test_parcelas_integration.py` |
| [US21](../historias/ep03-cadastro-acordos.md#us21) | `documentos` | PR [#98](https://github.com/Advocondo/back/pull/98) em revisão | [US21-CA01](../historias/ep03-cadastro-acordos.md#us21) | história pendente |
|  |  |  | [US21-CA02](../historias/ep03-cadastro-acordos.md#us21) | história pendente |
| [US22](../historias/ep03-cadastro-acordos.md#us22) | `acordos` | `GET /agreements` já filtra por status, condomínio, devedor e advogado; falta a busca por texto | [US22-CA01](../historias/ep03-cadastro-acordos.md#us22) | história pendente |
|  |  |  | [US22-CA02](../historias/ep03-cadastro-acordos.md#us22) | história pendente |
| [US23](../historias/ep03-cadastro-acordos.md#us23) | `condominios` | campos de contrato e renovação em `/condominiums` | [US23-CA01](../historias/ep03-cadastro-acordos.md#us23) | **8** · `condominios/test_condominios_integration.py` ×4, `condominios/test_condominios_unit.py` ×4 |
|  |  |  | [US23-CA02](../historias/ep03-cadastro-acordos.md#us23) | **1** · `condominios/test_condominios_integration.py` |
| [US24](../historias/ep03-cadastro-acordos.md#us24) | `documentos` | `POST`/`GET /agreements/{id}/pdfs` · `GET /agreements/{id}/pdfs/{pdf_id}` | [US24-CA01](../historias/ep03-cadastro-acordos.md#us24) | **3** · `documentos/test_documentos_integration.py` ×2, `documentos/test_documentos_unit.py` |
|  |  |  | [US24-CA02](../historias/ep03-cadastro-acordos.md#us24) | **1** · `documentos/test_documentos_integration.py` |
|  |  |  | [US24-CA03](../historias/ep03-cadastro-acordos.md#us24) | **6** · `documentos/test_documentos_integration.py` ×5, `documentos/test_documentos_unit.py` |

## EP04 · Acompanhamento de Parcelas { #ep04 }

| História | Módulo | Rotas | Critério | Testes que o citam |
| --- | --- | --- | --- | --- |
| [US25](../historias/ep04-parcelas.md#us25) | `parcelas` | `GET /installments` | [US25-CA01](../historias/ep04-parcelas.md#us25) | **2** · `parcelas/test_parcelas_integration.py`, `parcelas/test_parcelas_unit.py` |
|  |  |  | [US25-CA02](../historias/ep04-parcelas.md#us25) | **3** · `parcelas/test_parcelas_integration.py` ×3 |
| [US26](../historias/ep04-parcelas.md#us26) | `parcelas` | `POST`/`PUT`/`DELETE /installments/{id}/payment` | [US26-CA01](../historias/ep04-parcelas.md#us26) | **3** · `parcelas/test_parcelas_integration.py` ×2, `parcelas/test_parcelas_unit.py` |
|  |  |  | [US26-CA02](../historias/ep04-parcelas.md#us26) | **7** · `parcelas/test_parcelas_integration.py` ×5, `parcelas/test_parcelas_unit.py` ×2 |
| [US27](../historias/ep04-parcelas.md#us27) | `parcelas` | situação calculada em `parcelas/status.py`, exposta nas listagens | [US27-CA01](../historias/ep04-parcelas.md#us27) | **5** · `common/test_common_unit.py`, `parcelas/test_parcelas_integration.py` ×2, `parcelas/test_parcelas_unit.py` ×2 |
| [US28](../historias/ep04-parcelas.md#us28) | `parcelas` | `POST /installments/{id}/payment` (com `amount`) · `GET /installments/{id}/payments` | [US28-CA01](../historias/ep04-parcelas.md#us28) | **3** · `parcelas/test_parcelas_integration.py` ×2, `parcelas/test_parcelas_unit.py` |
|  |  |  | [US28-CA02](../historias/ep04-parcelas.md#us28) | **1** · `parcelas/test_parcelas_integration.py` |
| [US29](../historias/ep04-parcelas.md#us29) | `parcelas` | `PUT /installments/{id}/invoice` · `GET /installments/paid-without-invoice` | [US29-CA01](../historias/ep04-parcelas.md#us29) | **3** · `parcelas/test_parcelas_integration.py` ×2, `parcelas/test_parcelas_unit.py` |
|  |  |  | [US29-CA02](../historias/ep04-parcelas.md#us29) | **1** · `parcelas/test_parcelas_integration.py` |
| [US30](../historias/ep04-parcelas.md#us30) | — | — | [US30-CA01](../historias/ep04-parcelas.md#us30) | história pendente |
|  |  |  | [US30-CA02](../historias/ep04-parcelas.md#us30) | história pendente |
| [US31](../historias/ep04-parcelas.md#us31) | — | — | [US31-CA01](../historias/ep04-parcelas.md#us31) | história pendente |
|  |  |  | [US31-CA02](../historias/ep04-parcelas.md#us31) | história pendente |

## EP05 · Comissões e Metas { #ep05 }

| História | Módulo | Rotas | Critério | Testes que o citam |
| --- | --- | --- | --- | --- |
| [US32](../historias/ep05-comissoes-metas.md#us32) | `painel_operacional` | `GET /operator-panel/financial` | [US32-CA01](../historias/ep05-comissoes-metas.md#us32) | :warning: nenhum teste cita o critério |
|  |  |  | [US32-CA02](../historias/ep05-comissoes-metas.md#us32) | :warning: nenhum teste cita o critério |
| [US33](../historias/ep05-comissoes-metas.md#us33) | `painel_admin` | `GET /admin-panel/financial` | [US33-CA01](../historias/ep05-comissoes-metas.md#us33) | :warning: nenhum teste cita o critério |
|  |  |  | [US33-CA02](../historias/ep05-comissoes-metas.md#us33) | :warning: nenhum teste cita o critério |
| [US34](../historias/ep05-comissoes-metas.md#us34) | `painel_admin` | `GET /admin-panel/dashboard` | [US34-CA01](../historias/ep05-comissoes-metas.md#us34) | :warning: nenhum teste cita o critério |
|  |  |  | [US34-CA02](../historias/ep05-comissoes-metas.md#us34) | :warning: nenhum teste cita o critério |
| [US35](../historias/ep05-comissoes-metas.md#us35) | `painel_admin` | `GET /admin-panel/reports/export` | [US35-CA01](../historias/ep05-comissoes-metas.md#us35) | :warning: nenhum teste cita o critério |
|  |  |  | [US35-CA02](../historias/ep05-comissoes-metas.md#us35) | :warning: nenhum teste cita o critério |
| [US36](../historias/ep05-comissoes-metas.md#us36) | `metas` | `PUT /users/{id}/goals/{year}/{month}` · `GET /goals/me` | [US36-CA01](../historias/ep05-comissoes-metas.md#us36) | **16** · `metas/test_metas_integration.py` ×10, `metas/test_metas_unit.py` ×6 |
|  |  |  | [US36-CA02](../historias/ep05-comissoes-metas.md#us36) | **4** · `metas/test_metas_integration.py` ×4 |

## EP06 · Painel do Cliente { #ep06 }

| História | Módulo | Rotas | Critério | Testes que o citam |
| --- | --- | --- | --- | --- |
| [US37](../historias/ep06-painel-cliente.md#us37) | `painel_cliente` | `GET /client-panel/agreements` | [US37-CA01](../historias/ep06-painel-cliente.md#us37) | **1** · `painel_cliente/test_painel_cliente_integration.py` |
|  |  |  | [US37-CA02](../historias/ep06-painel-cliente.md#us37) | **2** · `painel_cliente/test_painel_cliente_integration.py` ×2 |
| [US38](../historias/ep06-painel-cliente.md#us38) | — | — | [US38-CA01](../historias/ep06-painel-cliente.md#us38) | história pendente |
| [US39](../historias/ep06-painel-cliente.md#us39) | — | — | [US39-CA01](../historias/ep06-painel-cliente.md#us39) | história pendente |
|  |  |  | [US39-CA02](../historias/ep06-painel-cliente.md#us39) | história pendente |
| [US40](../historias/ep06-painel-cliente.md#us40) | — | — | [US40-CA01](../historias/ep06-painel-cliente.md#us40) | história pendente |
|  |  |  | [US40-CA02](../historias/ep06-painel-cliente.md#us40) | história pendente |
|  |  |  | [US40-CA03](../historias/ep06-painel-cliente.md#us40) | história pendente |

## Rotas de suporte

Rotas que não pertencem a uma história, mas sustentam a operação:

| Rota | Para que serve |
| --- | --- |
| `GET /health` · `GET /health/ready` | Health checks do container e do monitoramento externo |
| `POST /setup` | Criação do primeiro Administrador depois do primeiro deploy (ver [Deploy](../infraestrutura/deploy.md)) |
| `PATCH /users/{id}/monthly-goal` | Meta mensal gravada no usuário, usada pelo painel da US32. Duplica a meta da US36; ver [Pendências e riscos](../acompanhamento/pendencias.md#riscos). |

## Manutenção desta página

Ao entregar uma história, marque cada critério nos testes, com a docstring `"""USxx-CAyy"""` ou no id do `pytest.param`, e acrescente aqui o módulo e as rotas da história. Um critério sem teste que o cite fica marcado com :warning:.

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 25/10/2026 | Criação da matriz requisito → código → teste a partir da `main` do back-end em 25/10/2026. | Mateus Vieira |
