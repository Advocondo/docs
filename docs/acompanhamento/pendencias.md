# Pendências e riscos

O que falta para fechar o backlog e o que a conferência de 25/10/2026 encontrou no código já entregue. A conferência leu os repositórios, rodou a suíte do back e comparou cada critério de aceitação com os testes; os números estão em [Situação da entrega](index.md).

## Histórias pendentes no back-end { #historias-pendentes }

Todas as dependências dessas histórias já estão na `main`, então **nenhuma está bloqueada** por outra história.

| História | MVP | Responsável | Situação | Depende de (entregues) |
| --- | :---: | --- | --- | --- |
| [US22](../historias/ep03-cadastro-acordos.md#us22) Buscar/filtrar acordos | Sim | Gabriela Tiago de Araújo | Sem PR. `GET /agreements` já combina filtros por status, condomínio, devedor e advogado (US22-CA02). Falta a busca por parte do nome do devedor (US22-CA01). | US15 |
| [US21](../historias/ep03-cadastro-acordos.md#us21) Anexar documentos ao acordo | | Pedro Henrique | Em revisão no [PR #98](https://github.com/Advocondo/back/pull/98) | US15 |
| [US30](../historias/ep04-parcelas.md#us30) Notificação interna de parcela em atraso | | Hauedy | Sem PR | US18, US27 |
| [US31](../historias/ep04-parcelas.md#us31) Log de alterações financeiras sensíveis | | Hauedy | Sem PR | US26 |
| [US38](../historias/ep06-painel-cliente.md#us38) Histórico de pagamentos de um morador | | **sem responsável** | Sem PR | US26, US37 |
| [US39](../historias/ep06-painel-cliente.md#us39) Baixar relatório simplificado | | Daniel Nunes Duarte | Sem PR. Pode reaproveitar a geração de PDF da US24 (módulo `documentos`). | US24, US37 |
| [US40](../historias/ep06-painel-cliente.md#us40) Notificação automática por e-mail ao Cliente | | Daniel Nunes Duarte | Sem PR. Pode reaproveitar o envio de e-mail de `common/email.py`. | US10, US37 |

## Front-end { #front-end }

O back do MVP está quase completo, mas **nenhuma tela de história está na `main` do front**. A única em andamento é Condomínios ([US12](../historias/ep03-cadastro-acordos.md#us12), [PR #46](https://github.com/Advocondo/front/pull/46)). Com isso, o sistema ainda não pode ser usado de ponta a ponta pela interface. Hoje a demonstração depende da documentação interativa da API (`/docs`, gerada pelo FastAPI).

Ordem sugerida para as telas, seguindo o MVP e o que o back já entrega:

1. Landing page e login: [US01](../historias/ep01-portal-autenticacao.md#us01) e [US02](../historias/ep01-portal-autenticacao.md#us02).
2. Gestão de usuários: [US07](../historias/ep02-usuarios-perfis.md#us07) a [US09](../historias/ep02-usuarios-perfis.md#us09).
3. Cadastros: Condomínios ([US12](../historias/ep03-cadastro-acordos.md#us12), em revisão), Devedores ([US13](../historias/ep03-cadastro-acordos.md#us13)) e Novo Acordo com honorários e parcelas ([US15](../historias/ep03-cadastro-acordos.md#us15) a [US17](../historias/ep03-cadastro-acordos.md#us17)).
4. Faturas do mês, baixa e pagamento parcial: [US25](../historias/ep04-parcelas.md#us25), [US26](../historias/ep04-parcelas.md#us26) e [US28](../historias/ep04-parcelas.md#us28).
5. Metas e comissões: [US32](../historias/ep05-comissoes-metas.md#us32) e [US36](../historias/ep05-comissoes-metas.md#us36), depois de resolver os riscos R1 e R2 abaixo.

Também estão abertas as issues de infraestrutura do front: deploy contínuo e variáveis na Vercel ([#40](https://github.com/Advocondo/front/issues/40), [#41](https://github.com/Advocondo/front/issues/41)), testes E2E ([#42](https://github.com/Advocondo/front/issues/42)) e monitoramento de erros ([#43](https://github.com/Advocondo/front/issues/43)).

## Riscos encontrados na conferência { #riscos }

| ID | Risco | Onde | Impacto | Recomendação |
| --- | --- | --- | --- | --- |
| R1 | **Meta mensal gravada em dois lugares.** A US36 grava a meta na tabela `goals` (`PUT /users/{id}/goals/{year}/{month}`). O [PR #86](https://github.com/Advocondo/back/pull/86) criou outro campo, `users.monthly_goal` (`PATCH /users/{id}/monthly-goal`), e o painel do operador lê só esse campo. | `painel_operacional/service.py`, `users/models.py`, `metas/` | A meta que o Administrador define pela [US36](../historias/ep05-comissoes-metas.md#us36) não aparece no painel da [US32](../historias/ep05-comissoes-metas.md#us32). | O painel deve ler a meta do mês em `goals`, pelo módulo `metas`. Depois, remover `monthly_goal` e a rota com uma migration. |
| R2 | **A comissão é igual a 100% dos honorários.** O painel soma `fee_amount` das parcelas pagas dos acordos do advogado responsável. A regra de comissão de cada membro ainda não foi definida pelo PO. | `painel_operacional/repository.py`, `painel_admin/repository.py` | Os valores exibidos como "comissão" nas [US32](../historias/ep05-comissoes-metas.md#us32) a [US34](../historias/ep05-comissoes-metas.md#us34) são, na verdade, honorários recebidos. | Decisão do PO sobre a regra (percentual por membro ou por acordo). Até lá, rotular o valor como "honorários recebidos". |
| R3 | **US32 a US35 entraram sem testes.** Nenhum teste cita os 8 critérios. A cobertura é de 32% a 38% em `painel_admin` e de 53% a 90% em `painel_operacional`, e esses módulos não têm página em `docs/` do back. | `painel_admin/`, `painel_operacional/` | Os critérios de permissão ([US32-CA02](../historias/ep05-comissoes-metas.md#us32), [US33-CA02](../historias/ep05-comissoes-metas.md#us33)) e de filtros da exportação ([US35-CA01](../historias/ep05-comissoes-metas.md#us35)) não são verificados. Os 95% de cobertura total escondem essa lacuna. | Testes de integração por critério, incluindo 403 para a Equipe Operacional nas rotas do Administrador, e as páginas `painel-admin.md` e `painel-operacional.md`. |
| R4 | **US08 sem testes próprios.** Não há teste que cite os critérios da inativação. O bloqueio de login do usuário inativo é testado em `auth`, mas as guardas de `change_status` (usuário inexistente, pendente ou o próprio Administrador) não são exercitadas. | `users/service.py` (`change_status`) | Uma regressão na inativação e na reativação ([US08](../historias/ep02-usuarios-perfis.md#us08)), que é do MVP, passaria pelo CI. | Uma classe `TestChangeUserStatus` em `users/test_users_integration.py`, marcando US08-CA01 a CA03. |
| R5 | **Documentação do back incompleta em `users`.** `docs/users.md` só descreve `PATCH /users/me` e os condomínios do Cliente. Faltam convites, status, perfil, histórico, advogados e meta. | `back/docs/users.md` | O front e quem mantém o código precisam ler o código para saber o contrato dessas rotas. | Completar a página no padrão de `docs/devedores.md`. |
| R6 | **Backup do banco não definido.** | [back#44](https://github.com/Advocondo/back/issues/44) | Uma falha no servidor do Coolify perde os dados de produção. | Backup diário do Postgres com retenção e um teste de restauração documentado em [Deploy](../infraestrutura/deploy.md). |
| R7 | **Duas checagens mortas no router de condomínios.** `GET` e `PATCH /condominiums/{id}` ainda têm `if ... raise HTTPException`, embora o service já lance `CondominiumNotFoundError`. O código nunca roda e fere a regra de que o router não trata regra de negócio. | `condominios/router.py` | Pequeno: só confunde quem toma o módulo de referência como exemplo. | Remover os dois `if`, como apontado no acompanhamento do [PR #77](https://github.com/Advocondo/back/pull/77). |

## Decisões pendentes { #decisoes }

| Decisão | Com quem | Afeta |
| --- | --- | --- |
| Regra de comissão de cada membro da equipe | PO e escritório | R2, US32–US34 |
| Provedor de e-mail (SMTP) de produção: sem ele, convites e redefinição de senha não funcionam em produção (ver [Deploy](../infraestrutura/deploy.md#variaveis-de-ambiente-do-back-end)) | Time e escritório | US03, US07, US40 |
| Responsável pela [US38](../historias/ep06-painel-cliente.md#us38) | Time | US38 |
| Escopo da reativação de acordo cancelado ([back#88](https://github.com/Advocondo/back/issues/88)), que não está em nenhuma história | PO | US20 |
| Quais eventos disparam o e-mail automático ao Cliente (US40-CA01 cita exemplos, não uma lista) | PO | US40 |

## Próximos passos recomendados

1. **Corrigir o que já está na `main`:** R1 e R3 (painéis financeiros) e R4 (US08). São correções pequenas, que tornam confiável o que vai ser demonstrado.
2. **Fechar o MVP no back:** US22, com a busca por texto em `GET /agreements`.
3. **Front do MVP:** a ordem da seção [Front-end](#front-end).
4. **Restante do back:** revisar e fazer o merge da US21 (PR #98), e depois US30, US31, US38, US39 e US40.
5. **Infraestrutura:** backup (R6) e deploy do front na Vercel.

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 25/10/2026 | Criação da página com as histórias pendentes, os riscos encontrados na conferência do back-end e as decisões em aberto. | Mateus Vieira |
| 1.1 | 25/10/2026 | Risco R7 (checagens mortas no router de condomínios) e decisão sobre o provedor de e-mail. | Mateus Vieira |
