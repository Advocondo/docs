# Completude do backlog

A situação de cada uma das 40 histórias em 26/10/2026, nas duas frentes. Cada história tem uma issue no repositório do back e outra no do front; o número do PR leva ao código que a entregou.

**Como ler as colunas**

- **Back:** *Entregue* quando a issue foi fechada pelo merge do PR na `main`, com a data do fechamento. *Em revisão* quando há um PR aberto. *Pendente* quando ainda não há código.
- **Responsável (back):** quem está atribuído à issue do back.
- **Critérios com teste:** quantos critérios de aceitação da história têm teste automatizado que os cita pelo identificador (ex.: `US13-CA01`). O :warning: marca história entregue com critério sem essa marcação; ver [Pendências e riscos](pendencias.md#riscos).

Para a ligação de cada critério ao código e aos testes, veja [Requisito → código → teste](../rastreabilidade/implementacao.md).

## Resumo

| Frente | Entregues | Em revisão | Pendentes | Sem issue |
| --- | :---: | :---: | :---: | :---: |
| Back-end | 38 | 0 | 1 ([US40](../historias/ep06-painel-cliente.md#us40)) | 1 ([US01](../historias/ep01-portal-autenticacao.md#us01), só front) |
| Front-end | 0 | 1 ([US12](../historias/ep03-cadastro-acordos.md#us12)) | 37 | 2 ([US27](../historias/ep04-parcelas.md#us27) e [US40](../historias/ep06-painel-cliente.md#us40)) |

A [US27](../historias/ep04-parcelas.md#us27) é do perfil Sistema, e a situação "Atrasado" calculada pelo back aparece nas telas das outras histórias. Já a [US40](../historias/ep06-painel-cliente.md#us40) não tem issue no front porque o disparo é automático, mas o registro das datas de envio (US40-CA03) precisará de lugar na interface se o escritório quiser consultá-lo.

## Por épico

### EP01 · Portal & Autenticação { #ep01 }

Back: **5 de 5** histórias entregues.

| História | MVP | Back | Responsável (back) | Front | Critérios com teste |
| --- | :---: | --- | --- | --- | :---: |
| [US01](../historias/ep01-portal-autenticacao.md#us01) Landing page institucional | Sim | Não se aplica (só front) | — | Pendente · [issue #1](https://github.com/Advocondo/front/issues/1) | — |
| [US02](../historias/ep01-portal-autenticacao.md#us02) Login no sistema | Sim | **Entregue** em 17/10 · [#53](https://github.com/Advocondo/back/pull/53) | Gabriela Tiago de Araújo | Pendente · [issue #2](https://github.com/Advocondo/front/issues/2) | 3/3 |
| [US03](../historias/ep01-portal-autenticacao.md#us03) Recuperação de senha |  | **Entregue** em 17/10 · [#57](https://github.com/Advocondo/back/pull/57) | Gabriela Tiago de Araújo | Pendente · [issue #3](https://github.com/Advocondo/front/issues/3) | 3/3 |
| [US04](../historias/ep01-portal-autenticacao.md#us04) Página institucional editável |  | **Entregue** em 25/10 · [#95](https://github.com/Advocondo/back/pull/95) | Gabriela Tiago de Araújo | Pendente · [issue #4](https://github.com/Advocondo/front/issues/4) | 2/2 |
| [US05](../historias/ep01-portal-autenticacao.md#us05) Editar dados do próprio perfil |  | **Entregue** em 17/10 · [#59](https://github.com/Advocondo/back/pull/59) | Gabriela Tiago de Araújo | Pendente · [issue #5](https://github.com/Advocondo/front/issues/5) | 2/2 |
| [US06](../historias/ep01-portal-autenticacao.md#us06) Encerrar sessões em outros dispositivos |  | **Entregue** em 17/10 · [#58](https://github.com/Advocondo/back/pull/58) | Gabriela Tiago de Araújo | Pendente · [issue #6](https://github.com/Advocondo/front/issues/6) | 1/1 |

### EP02 · Gestão de Usuários { #ep02 }

Back: **5 de 5** histórias entregues.

| História | MVP | Back | Responsável (back) | Front | Critérios com teste |
| --- | :---: | --- | --- | --- | :---: |
| [US07](../historias/ep02-usuarios-perfis.md#us07) Convidar novo membro | Sim | **Entregue** em 18/10 · [#60](https://github.com/Advocondo/back/pull/60) | Bruno Oliveira | Pendente · [issue #7](https://github.com/Advocondo/front/issues/7) | 4/4 |
| [US08](../historias/ep02-usuarios-perfis.md#us08) Inativar acesso de usuário | Sim | **Entregue** em 18/10 · [#62](https://github.com/Advocondo/back/pull/62) | Bruno Oliveira | Pendente · [issue #8](https://github.com/Advocondo/front/issues/8) | 3/3 |
| [US09](../historias/ep02-usuarios-perfis.md#us09) Definir nível de acesso | Sim | **Entregue** em 20/10 · [#70](https://github.com/Advocondo/back/pull/70) | Bruno Oliveira | Pendente · [issue #9](https://github.com/Advocondo/front/issues/9) | 2/2 |
| [US10](../historias/ep02-usuarios-perfis.md#us10) Vincular Cliente aos condomínios corretos |  | **Entregue** em 21/10 · [#79](https://github.com/Advocondo/back/pull/79) | Pedro Henrique Braga | Pendente · [issue #10](https://github.com/Advocondo/front/issues/10) | 2/2 |
| [US11](../historias/ep02-usuarios-perfis.md#us11) Histórico de ações da Gestão de Usuários |  | **Entregue** em 20/10 · [#71](https://github.com/Advocondo/back/pull/71) | Bruno Oliveira | Pendente · [issue #11](https://github.com/Advocondo/front/issues/11) | 2/2 |

### EP03 · Cadastro de Acordos { #ep03 }

Back: **13 de 13** histórias entregues.

| História | MVP | Back | Responsável (back) | Front | Critérios com teste |
| --- | :---: | --- | --- | --- | :---: |
| [US12](../historias/ep03-cadastro-acordos.md#us12) Cadastrar condomínio |  | **Entregue** em 20/10 · [#50](https://github.com/Advocondo/back/pull/50) | Mateus Vieira | Em revisão · [#46](https://github.com/Advocondo/front/pull/46) | 2/2 |
| [US13](../historias/ep03-cadastro-acordos.md#us13) Cadastrar devedor | Sim | **Entregue** em 20/10 · [#50](https://github.com/Advocondo/back/pull/50) | Mateus Vieira | Pendente · [issue #13](https://github.com/Advocondo/front/issues/13) | 1/1 |
| [US14](../historias/ep03-cadastro-acordos.md#us14) Importar lista de inadimplentes em lote |  | **Entregue** em 22/10 · [#83](https://github.com/Advocondo/back/pull/83) | Mateus Vieira | Pendente · [issue #14](https://github.com/Advocondo/front/issues/14) | 2/2 |
| [US15](../historias/ep03-cadastro-acordos.md#us15) Cadastrar novo acordo | Sim | **Entregue** em 21/10 · [#76](https://github.com/Advocondo/back/pull/76) | Mateus Vieira | Pendente · [issue #15](https://github.com/Advocondo/front/issues/15) | 3/3 |
| [US16](../historias/ep03-cadastro-acordos.md#us16) Definir honorários do acordo | Sim | **Entregue** em 21/10 · [#76](https://github.com/Advocondo/back/pull/76) | Mateus Vieira | Pendente · [issue #16](https://github.com/Advocondo/front/issues/16) | 2/2 |
| [US17](../historias/ep03-cadastro-acordos.md#us17) Fracionar dívida em parcelas | Sim | **Entregue** em 21/10 · [#76](https://github.com/Advocondo/back/pull/76) | Mateus Vieira | Pendente · [issue #17](https://github.com/Advocondo/front/issues/17) | 3/3 |
| [US18](../historias/ep03-cadastro-acordos.md#us18) Atribuir acordo a um advogado responsável |  | **Entregue** em 21/10 · [#69](https://github.com/Advocondo/back/pull/69) | Pedro Henrique | Pendente · [issue #18](https://github.com/Advocondo/front/issues/18) | 3/3 |
| [US19](../historias/ep03-cadastro-acordos.md#us19) Editar acordo já cadastrado |  | **Entregue** em 25/10 · [#97](https://github.com/Advocondo/back/pull/97) | Pedro Henrique | Pendente · [issue #19](https://github.com/Advocondo/front/issues/19) | 2/2 |
| [US20](../historias/ep03-cadastro-acordos.md#us20) Cancelar/encerrar acordo |  | **Entregue** em 25/10 · [#90](https://github.com/Advocondo/back/pull/90) | Pedro Henrique Braga | Pendente · [issue #20](https://github.com/Advocondo/front/issues/20) | 2/2 |
| [US21](../historias/ep03-cadastro-acordos.md#us21) Anexar documentos ao acordo |  | **Entregue** em 26/10 · [#98](https://github.com/Advocondo/back/pull/98) | Pedro Henrique | Pendente · [issue #21](https://github.com/Advocondo/front/issues/21) | 1/2 :warning: |
| [US22](../historias/ep03-cadastro-acordos.md#us22) Buscar/filtrar acordos | Sim | **Entregue** em 25/10 · [#99](https://github.com/Advocondo/back/pull/99) | Gabriela Tiago de Araújo | Pendente · [issue #22](https://github.com/Advocondo/front/issues/22) | 2/2 |
| [US23](../historias/ep03-cadastro-acordos.md#us23) Acompanhar renovação de contrato |  | **Entregue** em 22/10 · [#63](https://github.com/Advocondo/back/pull/63), [#77](https://github.com/Advocondo/back/pull/77) | Pedro Henrique | Pendente · [issue #23](https://github.com/Advocondo/front/issues/23) | 2/2 |
| [US24](../historias/ep03-cadastro-acordos.md#us24) Gerar e salvar PDF do acordo |  | **Entregue** em 25/10 · [#94](https://github.com/Advocondo/back/pull/94) | Ciro Costa | Pendente · [issue #24](https://github.com/Advocondo/front/issues/24) | 3/3 |

### EP04 · Acompanhamento de Parcelas { #ep04 }

Back: **7 de 7** histórias entregues.

| História | MVP | Back | Responsável (back) | Front | Critérios com teste |
| --- | :---: | --- | --- | --- | :---: |
| [US25](../historias/ep04-parcelas.md#us25) Listar faturas do mês | Sim | **Entregue** em 21/10 · [#80](https://github.com/Advocondo/back/pull/80) | Hauedy | Pendente · [issue #25](https://github.com/Advocondo/front/issues/25) | 2/2 |
| [US26](../historias/ep04-parcelas.md#us26) Dar baixa em parcela paga | Sim | **Entregue** em 22/10 · [#84](https://github.com/Advocondo/back/pull/84) | Hauedy | Pendente · [issue #26](https://github.com/Advocondo/front/issues/26) | 2/2 |
| [US27](../historias/ep04-parcelas.md#us27) Sinalizar parcela em atraso | Sim | **Entregue** em 21/10 · [#64](https://github.com/Advocondo/back/pull/64), [#76](https://github.com/Advocondo/back/pull/76) | Pedro Henrique | Sem issue no front | 1/1 |
| [US28](../historias/ep04-parcelas.md#us28) Registrar pagamento parcial | Sim | **Entregue** em 23/10 · [#85](https://github.com/Advocondo/back/pull/85) | Hauedy | Pendente · [issue #27](https://github.com/Advocondo/front/issues/27) | 2/2 |
| [US29](../historias/ep04-parcelas.md#us29) Registrar emissão de nota fiscal |  | **Entregue** em 25/10 · [#96](https://github.com/Advocondo/back/pull/96) | Hauedy | Pendente · [issue #28](https://github.com/Advocondo/front/issues/28) | 2/2 |
| [US30](../historias/ep04-parcelas.md#us30) Notificação interna de parcela em atraso |  | **Entregue** em 25/10 · [#100](https://github.com/Advocondo/back/pull/100) | Hauedy | Pendente · [issue #29](https://github.com/Advocondo/front/issues/29) | 2/2 |
| [US31](../historias/ep04-parcelas.md#us31) Log de alterações financeiras sensíveis |  | **Entregue** em 25/10 · [#101](https://github.com/Advocondo/back/pull/101) | Hauedy | Pendente · [issue #30](https://github.com/Advocondo/front/issues/30) | 2/2 |

### EP05 · Comissões e Metas { #ep05 }

Back: **5 de 5** histórias entregues.

| História | MVP | Back | Responsável (back) | Front | Critérios com teste |
| --- | :---: | --- | --- | --- | :---: |
| [US32](../historias/ep05-comissoes-metas.md#us32) Visualizar minhas metas e comissões | Sim | **Entregue** em 25/10 · [#86](https://github.com/Advocondo/back/pull/86) | Daniel Nunes Duarte | Pendente · [issue #31](https://github.com/Advocondo/front/issues/31) | 2/2 |
| [US33](../historias/ep05-comissoes-metas.md#us33) Visão global de faturamento e comissões |  | **Entregue** em 25/10 · [#86](https://github.com/Advocondo/back/pull/86) | Daniel Nunes Duarte | Pendente · [issue #32](https://github.com/Advocondo/front/issues/32) | 2/2 |
| [US34](../historias/ep05-comissoes-metas.md#us34) Dashboard de indicadores |  | **Entregue** em 25/10 · [#86](https://github.com/Advocondo/back/pull/86) | Daniel Nunes Duarte | Pendente · [issue #33](https://github.com/Advocondo/front/issues/33) | 2/2 |
| [US35](../historias/ep05-comissoes-metas.md#us35) Exportar relatório de acompanhamento |  | **Entregue** em 25/10 · [#86](https://github.com/Advocondo/back/pull/86) | Daniel Nunes Duarte | Pendente · [issue #34](https://github.com/Advocondo/front/issues/34) | 2/2 |
| [US36](../historias/ep05-comissoes-metas.md#us36) Definir metas por colaborador | Sim | **Entregue** em 22/10 · [#73](https://github.com/Advocondo/back/pull/73) | Pedro Henrique | Pendente · [issue #35](https://github.com/Advocondo/front/issues/35) | 2/2 |

### EP06 · Painel do Cliente { #ep06 }

Back: **3 de 4** histórias entregues.

| História | MVP | Back | Responsável (back) | Front | Critérios com teste |
| --- | :---: | --- | --- | --- | :---: |
| [US37](../historias/ep06-painel-cliente.md#us37) Consultar status dos acordos do condomínio |  | **Entregue** em 22/10 · [#81](https://github.com/Advocondo/back/pull/81) | Pedro Henrique Braga | Pendente · [issue #36](https://github.com/Advocondo/front/issues/36) | 2/2 |
| [US38](../historias/ep06-painel-cliente.md#us38) Histórico de pagamentos de um morador |  | **Entregue** em 25/10 · [#105](https://github.com/Advocondo/back/pull/105) | Ciro Costa | Pendente · [issue #37](https://github.com/Advocondo/front/issues/37) | 1/1 |
| [US39](../historias/ep06-painel-cliente.md#us39) Baixar relatório simplificado |  | **Entregue** em 26/10 · [#104](https://github.com/Advocondo/back/pull/104) | Daniel Nunes Duarte | Pendente · [issue #38](https://github.com/Advocondo/front/issues/38) | 0/2 :warning: |
| [US40](../historias/ep06-painel-cliente.md#us40) Notificação automática por e-mail ao Cliente |  | Pendente · [issue #39](https://github.com/Advocondo/back/issues/39) | Daniel Nunes Duarte | Sem issue no front | — |

## Itens fora das histórias

Trabalho necessário que não corresponde a uma história de usuário.

### Infraestrutura

| Item | Repo | Situação |
| --- | --- | --- |
| Pipeline de CI: lint, tipos, testes e build | back e front | **Entregue** em 30/09 · back [#49](https://github.com/Advocondo/back/pull/49) · front [#45](https://github.com/Advocondo/front/pull/45) |
| Deploy automatizado (Coolify), banco, segredos, observabilidade, HTTPS e CORS | back | **Entregue** em 30/09 · [#49](https://github.com/Advocondo/back/pull/49) |
| Migrations com Alembic | back | **Entregue** em 14/10 · [#52](https://github.com/Advocondo/back/pull/52) |
| Teste que impede duas *heads* do Alembic | back | **Entregue** em 22/10 · [#75](https://github.com/Advocondo/back/pull/75), [#91](https://github.com/Advocondo/back/pull/91) |
| Limpeza diária de sessões e links de redefinição expirados | back | **Entregue** em 25/10 · [#92](https://github.com/Advocondo/back/pull/92) |
| Backup e estratégia de recuperação do banco | back | Issue [#44](https://github.com/Advocondo/back/issues/44) fechada em 25/10 sem PR: o comentário dela diz que o Coolify faz backup automático a cada 30 dias. Falta a restauração documentada (ver [Pendências e riscos](pendencias.md#riscos)) |
| Deploy contínuo do front na Vercel | front | Pendente · [issue #40](https://github.com/Advocondo/front/issues/40) |
| Variáveis de ambiente do front na Vercel | front | Pendente · [issue #41](https://github.com/Advocondo/front/issues/41) |
| Testes E2E (Playwright/Selenium) | front | Pendente · [issue #42](https://github.com/Advocondo/front/issues/42) |
| Monitoramento de erros do front em produção | front | Pendente · [issue #43](https://github.com/Advocondo/front/issues/43) |

### Complementos das histórias

Issues abertas durante o desenvolvimento para cobrir lacunas das histórias originais.

| Item | Origem | Situação |
| --- | --- | --- |
| Destino dos envios do formulário de contato da landing | [US01](../historias/ep01-portal-autenticacao.md#us01) / [US04](../historias/ep01-portal-autenticacao.md#us04) | **Entregue** em 25/10 · [#95](https://github.com/Advocondo/back/pull/95) |
| Histórico das mudanças de vínculo Cliente–condomínio | [US10](../historias/ep02-usuarios-perfis.md#us10) / [US11](../historias/ep02-usuarios-perfis.md#us11) | **Entregue** em 25/10 · [#93](https://github.com/Advocondo/back/pull/93) |
| Reativar acordo cancelado | [US20](../historias/ep03-cadastro-acordos.md#us20) | **Entregue** em 25/10 · [#102](https://github.com/Advocondo/back/pull/102) |
| Fatura individual e faturas do acordo para o Cliente | [US25](../historias/ep04-parcelas.md#us25) / [US37](../historias/ep06-painel-cliente.md#us37) | Back **entregue** em 25/10 · [#103](https://github.com/Advocondo/back/pull/103) · front pendente · [issue #47](https://github.com/Advocondo/front/issues/47) |
| Arquivos anexados no bucket, como os PDFs | [US21](../historias/ep03-cadastro-acordos.md#us21) / [US24](../historias/ep03-cadastro-acordos.md#us24) | **Entregue** em 26/10 · [#98](https://github.com/Advocondo/back/pull/98) |

### Qualidade

Correções dos riscos encontrados na conferência de 25/10 ([Pendências e riscos](pendencias.md#riscos)).

| Item | Risco | Situação |
| --- | --- | --- |
| Testes da [US08](../historias/ep02-usuarios-perfis.md#us08) pela rota | R4 | **Entregue** em 26/10 · [#107](https://github.com/Advocondo/back/pull/107) |
| Testes e documentação dos painéis financeiros ([US32](../historias/ep05-comissoes-metas.md#us32)–[US35](../historias/ep05-comissoes-metas.md#us35)) | R3 | **Entregue** em 26/10 · [#109](https://github.com/Advocondo/back/pull/109) |
| Checagens mortas no router de condomínios e documentação de usuários | R5, R7 | **Entregue** em 26/10 · [#111](https://github.com/Advocondo/back/pull/111) |

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 25/10/2026 | Criação da página com a situação das 40 histórias e dos itens de infraestrutura em 25/10/2026. | Mateus Vieira |
| 1.1 | 26/10/2026 | Atualização para 26/10: US21, US22, US30, US31, US38 e US39 entregues no back, critérios com teste recontados, complementos [back#88](https://github.com/Advocondo/back/issues/88) e [back#89](https://github.com/Advocondo/back/issues/89) entregues, seção de qualidade e situação do backup. | Ciro Costa |
