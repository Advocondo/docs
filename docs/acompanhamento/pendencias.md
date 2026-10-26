# Pendências e riscos

O que falta para fechar o backlog e o que a conferência de 25/10/2026 encontrou no código já entregue, com a situação de cada item em 26/10/2026. A conferência leu os repositórios, rodou a suíte do back e comparou cada critério de aceitação com os testes; os números estão em [Situação da entrega](index.md).

## Histórias pendentes no back-end { #historias-pendentes }

Das 39 histórias com parte no back, **38 estão na `main`**. Falta uma, que não depende de nenhuma história pendente:

| História | MVP | Responsável | Situação | Depende de (entregues) |
| --- | :---: | --- | --- | --- |
| [US40](../historias/ep06-painel-cliente.md#us40) Notificação automática por e-mail ao Cliente | | Daniel Nunes Duarte | Sem PR. Pode reaproveitar o envio de e-mail de `common/email.py` e o relatório em PDF da [US39](../historias/ep06-painel-cliente.md#us39). | US10, US37 |

Desde a conferência de 25/10 entraram na `main` a [US21](../historias/ep03-cadastro-acordos.md#us21) ([#98](https://github.com/Advocondo/back/pull/98)), a [US22](../historias/ep03-cadastro-acordos.md#us22) ([#99](https://github.com/Advocondo/back/pull/99)), a [US30](../historias/ep04-parcelas.md#us30) ([#100](https://github.com/Advocondo/back/pull/100)), a [US31](../historias/ep04-parcelas.md#us31) ([#101](https://github.com/Advocondo/back/pull/101)), a [US38](../historias/ep06-painel-cliente.md#us38) ([#105](https://github.com/Advocondo/back/pull/105)) e a [US39](../historias/ep06-painel-cliente.md#us39) ([#104](https://github.com/Advocondo/back/pull/104)).

## Front-end { #front-end }

O back do MVP está completo, mas **nenhuma tela de história está na `main` do front**. A única em andamento é Condomínios ([US12](../historias/ep03-cadastro-acordos.md#us12), [PR #46](https://github.com/Advocondo/front/pull/46)). Com isso, o sistema ainda não pode ser usado de ponta a ponta pela interface. Hoje a demonstração depende da documentação interativa da API (`/docs`, gerada pelo FastAPI).

Ordem sugerida para as telas, seguindo o MVP e o que o back já entrega:

1. Landing page e login: [US01](../historias/ep01-portal-autenticacao.md#us01) e [US02](../historias/ep01-portal-autenticacao.md#us02).
2. Gestão de usuários: [US07](../historias/ep02-usuarios-perfis.md#us07) a [US09](../historias/ep02-usuarios-perfis.md#us09).
3. Cadastros: Condomínios ([US12](../historias/ep03-cadastro-acordos.md#us12), em revisão), Devedores ([US13](../historias/ep03-cadastro-acordos.md#us13)) e Novo Acordo com honorários e parcelas ([US15](../historias/ep03-cadastro-acordos.md#us15) a [US17](../historias/ep03-cadastro-acordos.md#us17)).
4. Faturas do mês, baixa e pagamento parcial: [US25](../historias/ep04-parcelas.md#us25), [US26](../historias/ep04-parcelas.md#us26) e [US28](../historias/ep04-parcelas.md#us28).
5. Metas e comissões: [US32](../historias/ep05-comissoes-metas.md#us32) e [US36](../historias/ep05-comissoes-metas.md#us36), depois de resolver os riscos R1, R2 e R8 a R10 abaixo.

Também estão abertas as issues de infraestrutura do front: deploy contínuo e variáveis na Vercel ([#40](https://github.com/Advocondo/front/issues/40), [#41](https://github.com/Advocondo/front/issues/41)), testes E2E ([#42](https://github.com/Advocondo/front/issues/42)) e monitoramento de erros ([#43](https://github.com/Advocondo/front/issues/43)).

## Riscos encontrados na conferência { #riscos }

| ID | Risco | Onde | Impacto | Recomendação | Situação em 26/10 |
| --- | --- | --- | --- | --- | --- |
| R1 | **Meta mensal gravada em dois lugares.** A US36 grava a meta na tabela `goals` (`PUT /users/{id}/goals/{year}/{month}`). O [PR #86](https://github.com/Advocondo/back/pull/86) criou outro campo, `users.monthly_goal` (`PATCH /users/{id}/monthly-goal`), e o painel do operador lê só esse campo. | `painel_operacional/service.py`, `users/models.py`, `metas/` | A meta que o Administrador define pela [US36](../historias/ep05-comissoes-metas.md#us36) não aparece no painel da [US32](../historias/ep05-comissoes-metas.md#us32). | O painel deve ler a meta do mês em `goals`, pelo módulo `metas`. Depois, remover `monthly_goal` e a rota com uma migration. | **Resolvido** em 26/10 · [back #113](https://github.com/Advocondo/back/pull/113): o painel lê a meta do mês em `goals`, e `users.monthly_goal` saiu com uma migration que levou as metas gravadas para `goals`. |
| R2 | **A comissão é igual a 100% dos honorários.** O painel soma `fee_amount` das parcelas pagas dos acordos do advogado responsável. A regra de comissão de cada membro ainda não foi definida pelo PO. | `painel_operacional/repository.py`, `painel_admin/repository.py` | Os valores exibidos como "comissão" nas [US32](../historias/ep05-comissoes-metas.md#us32) a [US34](../historias/ep05-comissoes-metas.md#us34) são, na verdade, honorários recebidos. | Decisão do PO sobre a regra (percentual por membro ou por acordo). Até lá, rotular o valor como "honorários recebidos". | **Aberto**, aguardando decisão do PO. |
| R3 | **US32 a US35 entraram sem testes.** Nenhum teste cita os 8 critérios. A cobertura é de 32% a 38% em `painel_admin` e de 53% a 90% em `painel_operacional`, e esses módulos não têm página em `docs/` do back. | `painel_admin/`, `painel_operacional/` | Os critérios de permissão ([US32-CA02](../historias/ep05-comissoes-metas.md#us32), [US33-CA02](../historias/ep05-comissoes-metas.md#us33)) e de filtros da exportação ([US35-CA01](../historias/ep05-comissoes-metas.md#us35)) não são verificados. Os 95% de cobertura total escondem essa lacuna. | Testes de integração por critério, incluindo 403 para a Equipe Operacional nas rotas do Administrador, e as páginas `painel-admin.md` e `painel-operacional.md`. | **Resolvido** em 26/10 · [back #109](https://github.com/Advocondo/back/pull/109): 35 testes que citam os 8 critérios, cobertura de 97% a 100% nos dois módulos e a página `docs/paineis-financeiros.md`. |
| R4 | **US08 sem testes próprios.** Não há teste que cite os critérios da inativação. O bloqueio de login do usuário inativo é testado em `auth`, mas as guardas de `change_status` (usuário inexistente, pendente ou o próprio Administrador) não são exercitadas. | `users/service.py` (`change_status`) | Uma regressão na inativação e na reativação ([US08](../historias/ep02-usuarios-perfis.md#us08)), que é do MVP, passaria pelo CI. | Uma classe `TestChangeUserStatus` em `users/test_users_integration.py`, marcando US08-CA01 a CA03. | **Resolvido** em 26/10 · [back #107](https://github.com/Advocondo/back/pull/107): `TestChangeUserStatus`, com US08-CA01 a CA03 e as guardas. |
| R5 | **Documentação do back incompleta em `users`.** `docs/users.md` só descreve `PATCH /users/me` e os condomínios do Cliente. Faltam convites, status, perfil, histórico, advogados e meta. | `back/docs/users.md` | O front e quem mantém o código precisam ler o código para saber o contrato dessas rotas. | Completar a página no padrão de `docs/devedores.md`. | **Resolvido** em 26/10 · [back #111](https://github.com/Advocondo/back/pull/111). |
| R6 | **Backup do banco não definido.** | [back#44](https://github.com/Advocondo/back/issues/44) | Uma falha no servidor do Coolify perde os dados de produção. | Backup diário do Postgres com retenção e um teste de restauração documentado em [Deploy](../infraestrutura/deploy.md). | **Parcial.** A issue [#44](https://github.com/Advocondo/back/issues/44) foi fechada em 25/10 sem PR. O comentário dela diz que o Coolify faz backup automático a cada 30 dias, e não diário como recomendado. Retenção e teste de restauração seguem sem documentação. |
| R7 | **Duas checagens mortas no router de condomínios.** `GET` e `PATCH /condominiums/{id}` ainda têm `if ... raise HTTPException`, embora o service já lance `CondominiumNotFoundError`. O código nunca roda e fere a regra de que o router não trata regra de negócio. | `condominios/router.py` | Pequeno: só confunde quem toma o módulo de referência como exemplo. | Remover os dois `if`, como apontado no acompanhamento do [PR #77](https://github.com/Advocondo/back/pull/77). | **Resolvido** em 26/10 · [back #111](https://github.com/Advocondo/back/pull/111). |
| R8 | **Atraso do mês atual no dashboard.** O dashboard da [US34](../historias/ep05-comissoes-metas.md#us34) mede o atraso no último dia do mês consultado. No mês atual, uma parcela que ainda não venceu já conta como atrasada. | `painel_admin/service.py` (`get_dashboard`) | No dia 02/03, uma parcela que vence em 10/03 entra em `overdue_installments` e na taxa de inadimplência do mês. | No mês atual, medir o atraso na data de hoje; nos meses fechados, manter o último dia. | **Resolvido** em 26/10 · [back #113](https://github.com/Advocondo/back/pull/113): no mês atual, o atraso é medido na data de hoje. |
| R9 | **Comissão de Administrador responsável não aparece.** `team_commissions` ([US33](../historias/ep05-comissoes-metas.md#us33)) lista só a Equipe Operacional. A comissão de um Administrador que é o advogado responsável entra no faturamento, mas não aparece para ninguém. | `painel_admin/repository.py` (`team_commissions`) | O total de comissões por membro não bate com o faturamento quando há Administrador advogado. | Decisão do PO: Administrador advogado recebe comissão? | **Aberto**, depende de decisão. |
| R10 | **Comissão e meta contam acordos diferentes.** A comissão ([US32](../historias/ep05-comissoes-metas.md#us32), [US33](../historias/ep05-comissoes-metas.md#us33)) conta os acordos em que o membro é o advogado **responsável**; o atingimento da meta ([US36](../historias/ep05-comissoes-metas.md#us36)) conta os acordos que ele **cadastrou**. | `painel_operacional/repository.py`, `painel_admin/repository.py`, `metas/repository.py` | A mesma pessoa pode ver uma comissão e um atingimento de meta que não batem. | Decisão do PO sobre quem recebe o mérito do acordo; depois, uma só regra nos três módulos. | **Aberto**, depende de decisão. |
| R11 | **Critérios entregues sem marcação nos testes.** Os testes da [US39](../historias/ep06-painel-cliente.md#us39) não citam US39-CA01 e CA02, e o [US21-CA02](../historias/ep03-cadastro-acordos.md#us21) é testado (o banco recusa apagar acordo com documentos) sem a marcação. | `painel_cliente/`, `documentos/` | A [rastreabilidade](../rastreabilidade/implementacao.md) mostra esses 3 critérios como sem teste. | Acrescentar o identificador na docstring dos testes que já existem. | **Aberto.** |

## Decisões pendentes { #decisoes }

| Decisão | Com quem | Afeta |
| --- | --- | --- |
| Regra de comissão de cada membro da equipe | PO e escritório | R2, US32–US34 |
| Se o Administrador que é advogado responsável recebe comissão | PO e escritório | R9, US33 |
| Quem recebe o mérito do acordo nas comissões e nas metas: o advogado responsável ou quem cadastrou | PO e escritório | R10, US32, US33, US36 |
| Provedor de e-mail (SMTP) de produção: sem ele, convites e redefinição de senha não funcionam em produção (ver [Deploy](../infraestrutura/deploy.md#variaveis-de-ambiente-do-back-end)) | Time e escritório | US03, US07, US40 |
| Quais eventos disparam o e-mail automático ao Cliente (US40-CA01 cita exemplos, não uma lista) | PO | US40 |

Resolvidas desde 25/10: o responsável pela [US38](../historias/ep06-painel-cliente.md#us38) (Ciro Costa, entregue em [#105](https://github.com/Advocondo/back/pull/105)) e a reativação de acordo cancelado ([back#88](https://github.com/Advocondo/back/issues/88), entregue em [#102](https://github.com/Advocondo/back/pull/102), com Administrador e Equipe Operacional podendo reativar).

## Próximos passos recomendados

1. **Marcar os critérios nos testes (R11).** Os testes já existem; falta o identificador.
2. **Fechar o backup (R6):** avaliar a frequência (hoje a cada 30 dias) e documentar a restauração em [Deploy](../infraestrutura/deploy.md).
3. **Levar ao PO** as decisões de R2, R9 e R10.
4. **Front do MVP:** a ordem da seção [Front-end](#front-end). O back do MVP está completo.
5. **Restante do back:** a [US40](../historias/ep06-painel-cliente.md#us40), depois da decisão sobre os eventos que disparam o e-mail.

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 25/10/2026 | Criação da página com as histórias pendentes, os riscos encontrados na conferência do back-end e as decisões em aberto. | Mateus Vieira |
| 1.1 | 25/10/2026 | Risco R7 (checagens mortas no router de condomínios) e decisão sobre o provedor de e-mail. | Mateus Vieira |
| 1.2 | 26/10/2026 | Situação em 26/10: só a US40 pendente no back, R3 e R4 resolvidos, R5 e R7 resolvidos, R6 parcial (backup a cada 30 dias no Coolify), novos riscos R8 a R11 e decisões atualizadas. | Ciro Costa |
| 1.3 | 26/10/2026 | R1 e R8 resolvidos em [back #113](https://github.com/Advocondo/back/pull/113); próximos passos atualizados. | Ciro Costa |
