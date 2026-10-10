---
icon: lucide/git-branch
---

# Matriz de rastreabilidade

Esta página consolida os relacionamentos declarados em cada história e mostra o caminho inverso — quem depende de quem. Ela é a ferramenta para responder a duas perguntas: **em que ordem implementar** e **o que quebra se esta história mudar**.

!!! note "Como ler"
    **Depende de** — histórias que precisam existir antes desta funcionar.  
    **Requisito para** — histórias que deixam de funcionar se esta não existir (inverso da coluna anterior).  
    **Impacto de mudança** — histórias que citam esta por compartilharem regra de negócio; mudou aqui, revise lá.

---

## Matriz principal { #matriz }

| ID | História | Épico | Depende de | Requisito para | Impacto de mudança |
| --- | --- | --- | --- | --- | --- |
| [US01](../historias/ep01-portal-autenticacao.md#us01) | Landing page institucional | EP01 | — | [US04](../historias/ep01-portal-autenticacao.md#us04) | [US02](../historias/ep01-portal-autenticacao.md#us02) · [US04](../historias/ep01-portal-autenticacao.md#us04) |
| [US02](../historias/ep01-portal-autenticacao.md#us02) | Login no sistema | EP01 | — | [US03](../historias/ep01-portal-autenticacao.md#us03) · [US04](../historias/ep01-portal-autenticacao.md#us04) · [US05](../historias/ep01-portal-autenticacao.md#us05) · [US06](../historias/ep01-portal-autenticacao.md#us06) · [US07](../historias/ep02-usuarios-perfis.md#us07) | [US01](../historias/ep01-portal-autenticacao.md#us01) · [US03](../historias/ep01-portal-autenticacao.md#us03) · [US06](../historias/ep01-portal-autenticacao.md#us06) · [US07](../historias/ep02-usuarios-perfis.md#us07) · [US08](../historias/ep02-usuarios-perfis.md#us08) · [US09](../historias/ep02-usuarios-perfis.md#us09) |
| [US03](../historias/ep01-portal-autenticacao.md#us03) | Recuperação de senha | EP01 | [US02](../historias/ep01-portal-autenticacao.md#us02) | — | [US02](../historias/ep01-portal-autenticacao.md#us02) · [US05](../historias/ep01-portal-autenticacao.md#us05) · [US06](../historias/ep01-portal-autenticacao.md#us06) |
| [US04](../historias/ep01-portal-autenticacao.md#us04) | Página institucional editável | EP01 | [US01](../historias/ep01-portal-autenticacao.md#us01) · [US02](../historias/ep01-portal-autenticacao.md#us02) | — | [US01](../historias/ep01-portal-autenticacao.md#us01) · [US09](../historias/ep02-usuarios-perfis.md#us09) |
| [US05](../historias/ep01-portal-autenticacao.md#us05) | Editar dados do próprio perfil | EP01 | [US02](../historias/ep01-portal-autenticacao.md#us02) | — | [US03](../historias/ep01-portal-autenticacao.md#us03) · [US06](../historias/ep01-portal-autenticacao.md#us06) · [US07](../historias/ep02-usuarios-perfis.md#us07) |
| [US06](../historias/ep01-portal-autenticacao.md#us06) | Encerrar sessões em outros dispositivos | EP01 | [US02](../historias/ep01-portal-autenticacao.md#us02) | — | [US02](../historias/ep01-portal-autenticacao.md#us02) · [US03](../historias/ep01-portal-autenticacao.md#us03) · [US05](../historias/ep01-portal-autenticacao.md#us05) |
| [US07](../historias/ep02-usuarios-perfis.md#us07) | Convidar novo membro | EP02 | [US02](../historias/ep01-portal-autenticacao.md#us02) | [US08](../historias/ep02-usuarios-perfis.md#us08) · [US09](../historias/ep02-usuarios-perfis.md#us09) · [US10](../historias/ep02-usuarios-perfis.md#us10) · [US11](../historias/ep02-usuarios-perfis.md#us11) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US36](../historias/ep05-comissoes-metas.md#us36) | [US02](../historias/ep01-portal-autenticacao.md#us02) · [US05](../historias/ep01-portal-autenticacao.md#us05) · [US09](../historias/ep02-usuarios-perfis.md#us09) · [US10](../historias/ep02-usuarios-perfis.md#us10) · [US11](../historias/ep02-usuarios-perfis.md#us11) · [US18](../historias/ep03-cadastro-acordos.md#us18) |
| [US08](../historias/ep02-usuarios-perfis.md#us08) | Inativar acesso de usuário | EP02 | [US07](../historias/ep02-usuarios-perfis.md#us07) | [US11](../historias/ep02-usuarios-perfis.md#us11) | [US02](../historias/ep01-portal-autenticacao.md#us02) · [US11](../historias/ep02-usuarios-perfis.md#us11) |
| [US09](../historias/ep02-usuarios-perfis.md#us09) | Definir nível de acesso | EP02 | [US07](../historias/ep02-usuarios-perfis.md#us07) | [US11](../historias/ep02-usuarios-perfis.md#us11) | [US02](../historias/ep01-portal-autenticacao.md#us02) · [US04](../historias/ep01-portal-autenticacao.md#us04) · [US07](../historias/ep02-usuarios-perfis.md#us07) · [US10](../historias/ep02-usuarios-perfis.md#us10) · [US11](../historias/ep02-usuarios-perfis.md#us11) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US32](../historias/ep05-comissoes-metas.md#us32) · [US33](../historias/ep05-comissoes-metas.md#us33) · [US37](../historias/ep06-painel-cliente.md#us37) |
| [US10](../historias/ep02-usuarios-perfis.md#us10) | Vincular Cliente aos condomínios corretos | EP02 | [US07](../historias/ep02-usuarios-perfis.md#us07) · [US12](../historias/ep03-cadastro-acordos.md#us12) | [US37](../historias/ep06-painel-cliente.md#us37) · [US40](../historias/ep06-painel-cliente.md#us40) | [US07](../historias/ep02-usuarios-perfis.md#us07) · [US09](../historias/ep02-usuarios-perfis.md#us09) · [US12](../historias/ep03-cadastro-acordos.md#us12) · [US15](../historias/ep03-cadastro-acordos.md#us15) · [US24](../historias/ep03-cadastro-acordos.md#us24) · [US37](../historias/ep06-painel-cliente.md#us37) · [US38](../historias/ep06-painel-cliente.md#us38) · [US39](../historias/ep06-painel-cliente.md#us39) · [US40](../historias/ep06-painel-cliente.md#us40) |
| [US11](../historias/ep02-usuarios-perfis.md#us11) | Histórico de ações da Gestão de Usuários | EP02 | [US07](../historias/ep02-usuarios-perfis.md#us07) · [US08](../historias/ep02-usuarios-perfis.md#us08) · [US09](../historias/ep02-usuarios-perfis.md#us09) | — | [US07](../historias/ep02-usuarios-perfis.md#us07) · [US08](../historias/ep02-usuarios-perfis.md#us08) · [US09](../historias/ep02-usuarios-perfis.md#us09) · [US31](../historias/ep04-parcelas.md#us31) |
| [US12](../historias/ep03-cadastro-acordos.md#us12) | Cadastrar condomínio | EP03 | — | [US10](../historias/ep02-usuarios-perfis.md#us10) · [US13](../historias/ep03-cadastro-acordos.md#us13) · [US14](../historias/ep03-cadastro-acordos.md#us14) · [US15](../historias/ep03-cadastro-acordos.md#us15) · [US23](../historias/ep03-cadastro-acordos.md#us23) | [US10](../historias/ep02-usuarios-perfis.md#us10) · [US15](../historias/ep03-cadastro-acordos.md#us15) · [US22](../historias/ep03-cadastro-acordos.md#us22) · [US23](../historias/ep03-cadastro-acordos.md#us23) |
| [US13](../historias/ep03-cadastro-acordos.md#us13) | Cadastrar devedor | EP03 | [US12](../historias/ep03-cadastro-acordos.md#us12) | [US14](../historias/ep03-cadastro-acordos.md#us14) · [US15](../historias/ep03-cadastro-acordos.md#us15) | [US14](../historias/ep03-cadastro-acordos.md#us14) · [US15](../historias/ep03-cadastro-acordos.md#us15) · [US22](../historias/ep03-cadastro-acordos.md#us22) · [US38](../historias/ep06-painel-cliente.md#us38) |
| [US14](../historias/ep03-cadastro-acordos.md#us14) | Importar lista de inadimplentes em lote | EP03 | [US12](../historias/ep03-cadastro-acordos.md#us12) · [US13](../historias/ep03-cadastro-acordos.md#us13) | — | [US13](../historias/ep03-cadastro-acordos.md#us13) · [US15](../historias/ep03-cadastro-acordos.md#us15) |
| [US15](../historias/ep03-cadastro-acordos.md#us15) | Cadastrar novo acordo | EP03 | [US12](../historias/ep03-cadastro-acordos.md#us12) · [US13](../historias/ep03-cadastro-acordos.md#us13) | [US16](../historias/ep03-cadastro-acordos.md#us16) · [US17](../historias/ep03-cadastro-acordos.md#us17) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US19](../historias/ep03-cadastro-acordos.md#us19) · [US20](../historias/ep03-cadastro-acordos.md#us20) · [US21](../historias/ep03-cadastro-acordos.md#us21) · [US22](../historias/ep03-cadastro-acordos.md#us22) · [US24](../historias/ep03-cadastro-acordos.md#us24) · [US34](../historias/ep05-comissoes-metas.md#us34) · [US37](../historias/ep06-painel-cliente.md#us37) | [US10](../historias/ep02-usuarios-perfis.md#us10) · [US12](../historias/ep03-cadastro-acordos.md#us12) · [US13](../historias/ep03-cadastro-acordos.md#us13) · [US14](../historias/ep03-cadastro-acordos.md#us14) · [US16](../historias/ep03-cadastro-acordos.md#us16) · [US17](../historias/ep03-cadastro-acordos.md#us17) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US19](../historias/ep03-cadastro-acordos.md#us19) · [US20](../historias/ep03-cadastro-acordos.md#us20) · [US21](../historias/ep03-cadastro-acordos.md#us21) · [US22](../historias/ep03-cadastro-acordos.md#us22) · [US24](../historias/ep03-cadastro-acordos.md#us24) · [US37](../historias/ep06-painel-cliente.md#us37) |
| [US16](../historias/ep03-cadastro-acordos.md#us16) | Definir honorários do acordo | EP03 | [US15](../historias/ep03-cadastro-acordos.md#us15) | [US33](../historias/ep05-comissoes-metas.md#us33) | [US15](../historias/ep03-cadastro-acordos.md#us15) · [US17](../historias/ep03-cadastro-acordos.md#us17) · [US26](../historias/ep04-parcelas.md#us26) · [US33](../historias/ep05-comissoes-metas.md#us33) · [US37](../historias/ep06-painel-cliente.md#us37) · [US38](../historias/ep06-painel-cliente.md#us38) · [US39](../historias/ep06-painel-cliente.md#us39) |
| [US17](../historias/ep03-cadastro-acordos.md#us17) | Fracionar dívida em parcelas | EP03 | [US15](../historias/ep03-cadastro-acordos.md#us15) | [US20](../historias/ep03-cadastro-acordos.md#us20) · [US24](../historias/ep03-cadastro-acordos.md#us24) · [US25](../historias/ep04-parcelas.md#us25) · [US26](../historias/ep04-parcelas.md#us26) · [US27](../historias/ep04-parcelas.md#us27) | [US15](../historias/ep03-cadastro-acordos.md#us15) · [US16](../historias/ep03-cadastro-acordos.md#us16) · [US19](../historias/ep03-cadastro-acordos.md#us19) · [US20](../historias/ep03-cadastro-acordos.md#us20) · [US25](../historias/ep04-parcelas.md#us25) · [US26](../historias/ep04-parcelas.md#us26) · [US27](../historias/ep04-parcelas.md#us27) |
| [US18](../historias/ep03-cadastro-acordos.md#us18) | Atribuir acordo a um advogado responsável | EP03 | [US07](../historias/ep02-usuarios-perfis.md#us07) · [US15](../historias/ep03-cadastro-acordos.md#us15) | [US30](../historias/ep04-parcelas.md#us30) | [US07](../historias/ep02-usuarios-perfis.md#us07) · [US09](../historias/ep02-usuarios-perfis.md#us09) · [US15](../historias/ep03-cadastro-acordos.md#us15) · [US22](../historias/ep03-cadastro-acordos.md#us22) · [US25](../historias/ep04-parcelas.md#us25) · [US26](../historias/ep04-parcelas.md#us26) · [US30](../historias/ep04-parcelas.md#us30) |
| [US19](../historias/ep03-cadastro-acordos.md#us19) | Editar acordo já cadastrado | EP03 | [US15](../historias/ep03-cadastro-acordos.md#us15) | — | [US15](../historias/ep03-cadastro-acordos.md#us15) · [US17](../historias/ep03-cadastro-acordos.md#us17) · [US26](../historias/ep04-parcelas.md#us26) · [US31](../historias/ep04-parcelas.md#us31) |
| [US20](../historias/ep03-cadastro-acordos.md#us20) | Cancelar/encerrar acordo | EP03 | [US15](../historias/ep03-cadastro-acordos.md#us15) · [US17](../historias/ep03-cadastro-acordos.md#us17) | — | [US15](../historias/ep03-cadastro-acordos.md#us15) · [US17](../historias/ep03-cadastro-acordos.md#us17) · [US21](../historias/ep03-cadastro-acordos.md#us21) · [US22](../historias/ep03-cadastro-acordos.md#us22) · [US25](../historias/ep04-parcelas.md#us25) |
| [US21](../historias/ep03-cadastro-acordos.md#us21) | Anexar documentos ao acordo | EP03 | [US15](../historias/ep03-cadastro-acordos.md#us15) | — | [US15](../historias/ep03-cadastro-acordos.md#us15) · [US20](../historias/ep03-cadastro-acordos.md#us20) · [US24](../historias/ep03-cadastro-acordos.md#us24) |
| [US22](../historias/ep03-cadastro-acordos.md#us22) | Buscar/filtrar acordos | EP03 | [US15](../historias/ep03-cadastro-acordos.md#us15) | — | [US12](../historias/ep03-cadastro-acordos.md#us12) · [US13](../historias/ep03-cadastro-acordos.md#us13) · [US15](../historias/ep03-cadastro-acordos.md#us15) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US20](../historias/ep03-cadastro-acordos.md#us20) · [US25](../historias/ep04-parcelas.md#us25) |
| [US23](../historias/ep03-cadastro-acordos.md#us23) | Acompanhar renovação de contrato | EP03 | [US12](../historias/ep03-cadastro-acordos.md#us12) | — | [US12](../historias/ep03-cadastro-acordos.md#us12) · [US34](../historias/ep05-comissoes-metas.md#us34) |
| [US24](../historias/ep03-cadastro-acordos.md#us24) | Gerar e salvar PDF do acordo | EP03 | [US15](../historias/ep03-cadastro-acordos.md#us15) · [US17](../historias/ep03-cadastro-acordos.md#us17) | [US39](../historias/ep06-painel-cliente.md#us39) | [US10](../historias/ep02-usuarios-perfis.md#us10) · [US15](../historias/ep03-cadastro-acordos.md#us15) · [US21](../historias/ep03-cadastro-acordos.md#us21) · [US39](../historias/ep06-painel-cliente.md#us39) · [US40](../historias/ep06-painel-cliente.md#us40) |
| [US25](../historias/ep04-parcelas.md#us25) | Listar faturas do mês | EP04 | [US17](../historias/ep03-cadastro-acordos.md#us17) | [US26](../historias/ep04-parcelas.md#us26) · [US35](../historias/ep05-comissoes-metas.md#us35) | [US17](../historias/ep03-cadastro-acordos.md#us17) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US20](../historias/ep03-cadastro-acordos.md#us20) · [US22](../historias/ep03-cadastro-acordos.md#us22) · [US26](../historias/ep04-parcelas.md#us26) · [US27](../historias/ep04-parcelas.md#us27) · [US28](../historias/ep04-parcelas.md#us28) · [US30](../historias/ep04-parcelas.md#us30) · [US35](../historias/ep05-comissoes-metas.md#us35) |
| [US26](../historias/ep04-parcelas.md#us26) | Dar baixa em parcela paga | EP04 | [US17](../historias/ep03-cadastro-acordos.md#us17) · [US25](../historias/ep04-parcelas.md#us25) | [US28](../historias/ep04-parcelas.md#us28) · [US29](../historias/ep04-parcelas.md#us29) · [US31](../historias/ep04-parcelas.md#us31) · [US32](../historias/ep05-comissoes-metas.md#us32) · [US33](../historias/ep05-comissoes-metas.md#us33) · [US36](../historias/ep05-comissoes-metas.md#us36) · [US38](../historias/ep06-painel-cliente.md#us38) | [US16](../historias/ep03-cadastro-acordos.md#us16) · [US17](../historias/ep03-cadastro-acordos.md#us17) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US19](../historias/ep03-cadastro-acordos.md#us19) · [US25](../historias/ep04-parcelas.md#us25) · [US28](../historias/ep04-parcelas.md#us28) · [US29](../historias/ep04-parcelas.md#us29) · [US31](../historias/ep04-parcelas.md#us31) · [US32](../historias/ep05-comissoes-metas.md#us32) · [US36](../historias/ep05-comissoes-metas.md#us36) · [US38](../historias/ep06-painel-cliente.md#us38) |
| [US27](../historias/ep04-parcelas.md#us27) | Sinalizar parcela em atraso | EP04 | [US17](../historias/ep03-cadastro-acordos.md#us17) | [US30](../historias/ep04-parcelas.md#us30) · [US34](../historias/ep05-comissoes-metas.md#us34) | [US17](../historias/ep03-cadastro-acordos.md#us17) · [US25](../historias/ep04-parcelas.md#us25) · [US30](../historias/ep04-parcelas.md#us30) · [US34](../historias/ep05-comissoes-metas.md#us34) · [US37](../historias/ep06-painel-cliente.md#us37) |
| [US28](../historias/ep04-parcelas.md#us28) | Registrar pagamento parcial | EP04 | [US26](../historias/ep04-parcelas.md#us26) | — | [US25](../historias/ep04-parcelas.md#us25) · [US26](../historias/ep04-parcelas.md#us26) · [US31](../historias/ep04-parcelas.md#us31) · [US38](../historias/ep06-painel-cliente.md#us38) |
| [US29](../historias/ep04-parcelas.md#us29) | Registrar emissão de nota fiscal | EP04 | [US26](../historias/ep04-parcelas.md#us26) | — | [US26](../historias/ep04-parcelas.md#us26) · [US35](../historias/ep05-comissoes-metas.md#us35) |
| [US30](../historias/ep04-parcelas.md#us30) | Notificação interna de parcela em atraso | EP04 | [US18](../historias/ep03-cadastro-acordos.md#us18) · [US27](../historias/ep04-parcelas.md#us27) | — | [US18](../historias/ep03-cadastro-acordos.md#us18) · [US25](../historias/ep04-parcelas.md#us25) · [US27](../historias/ep04-parcelas.md#us27) · [US40](../historias/ep06-painel-cliente.md#us40) |
| [US31](../historias/ep04-parcelas.md#us31) | Log de alterações financeiras sensíveis | EP04 | [US26](../historias/ep04-parcelas.md#us26) | — | [US11](../historias/ep02-usuarios-perfis.md#us11) · [US19](../historias/ep03-cadastro-acordos.md#us19) · [US26](../historias/ep04-parcelas.md#us26) · [US28](../historias/ep04-parcelas.md#us28) |
| [US32](../historias/ep05-comissoes-metas.md#us32) | Visualizar minhas metas e comissões | EP05 | [US26](../historias/ep04-parcelas.md#us26) · [US36](../historias/ep05-comissoes-metas.md#us36) | — | [US09](../historias/ep02-usuarios-perfis.md#us09) · [US26](../historias/ep04-parcelas.md#us26) · [US33](../historias/ep05-comissoes-metas.md#us33) · [US36](../historias/ep05-comissoes-metas.md#us36) |
| [US33](../historias/ep05-comissoes-metas.md#us33) | Visão global de faturamento e comissões | EP05 | [US16](../historias/ep03-cadastro-acordos.md#us16) · [US26](../historias/ep04-parcelas.md#us26) | [US34](../historias/ep05-comissoes-metas.md#us34) | [US09](../historias/ep02-usuarios-perfis.md#us09) · [US16](../historias/ep03-cadastro-acordos.md#us16) · [US32](../historias/ep05-comissoes-metas.md#us32) · [US34](../historias/ep05-comissoes-metas.md#us34) · [US35](../historias/ep05-comissoes-metas.md#us35) · [US36](../historias/ep05-comissoes-metas.md#us36) |
| [US34](../historias/ep05-comissoes-metas.md#us34) | Dashboard de indicadores | EP05 | [US15](../historias/ep03-cadastro-acordos.md#us15) · [US27](../historias/ep04-parcelas.md#us27) · [US33](../historias/ep05-comissoes-metas.md#us33) | — | [US23](../historias/ep03-cadastro-acordos.md#us23) · [US27](../historias/ep04-parcelas.md#us27) · [US33](../historias/ep05-comissoes-metas.md#us33) · [US35](../historias/ep05-comissoes-metas.md#us35) |
| [US35](../historias/ep05-comissoes-metas.md#us35) | Exportar relatório de acompanhamento | EP05 | [US25](../historias/ep04-parcelas.md#us25) | — | [US25](../historias/ep04-parcelas.md#us25) · [US29](../historias/ep04-parcelas.md#us29) · [US33](../historias/ep05-comissoes-metas.md#us33) · [US34](../historias/ep05-comissoes-metas.md#us34) · [US39](../historias/ep06-painel-cliente.md#us39) |
| [US36](../historias/ep05-comissoes-metas.md#us36) | Definir metas por colaborador | EP05 | [US07](../historias/ep02-usuarios-perfis.md#us07) · [US26](../historias/ep04-parcelas.md#us26) | [US32](../historias/ep05-comissoes-metas.md#us32) | [US26](../historias/ep04-parcelas.md#us26) · [US32](../historias/ep05-comissoes-metas.md#us32) · [US33](../historias/ep05-comissoes-metas.md#us33) |
| [US37](../historias/ep06-painel-cliente.md#us37) | Consultar status dos acordos do condomínio | EP06 | [US10](../historias/ep02-usuarios-perfis.md#us10) · [US15](../historias/ep03-cadastro-acordos.md#us15) | [US38](../historias/ep06-painel-cliente.md#us38) · [US39](../historias/ep06-painel-cliente.md#us39) · [US40](../historias/ep06-painel-cliente.md#us40) | [US09](../historias/ep02-usuarios-perfis.md#us09) · [US10](../historias/ep02-usuarios-perfis.md#us10) · [US15](../historias/ep03-cadastro-acordos.md#us15) · [US16](../historias/ep03-cadastro-acordos.md#us16) · [US27](../historias/ep04-parcelas.md#us27) · [US38](../historias/ep06-painel-cliente.md#us38) |
| [US38](../historias/ep06-painel-cliente.md#us38) | Histórico de pagamentos de um morador | EP06 | [US26](../historias/ep04-parcelas.md#us26) · [US37](../historias/ep06-painel-cliente.md#us37) | — | [US10](../historias/ep02-usuarios-perfis.md#us10) · [US13](../historias/ep03-cadastro-acordos.md#us13) · [US16](../historias/ep03-cadastro-acordos.md#us16) · [US26](../historias/ep04-parcelas.md#us26) · [US28](../historias/ep04-parcelas.md#us28) · [US37](../historias/ep06-painel-cliente.md#us37) · [US39](../historias/ep06-painel-cliente.md#us39) |
| [US39](../historias/ep06-painel-cliente.md#us39) | Baixar relatório simplificado | EP06 | [US24](../historias/ep03-cadastro-acordos.md#us24) · [US37](../historias/ep06-painel-cliente.md#us37) | — | [US10](../historias/ep02-usuarios-perfis.md#us10) · [US16](../historias/ep03-cadastro-acordos.md#us16) · [US24](../historias/ep03-cadastro-acordos.md#us24) · [US35](../historias/ep05-comissoes-metas.md#us35) · [US38](../historias/ep06-painel-cliente.md#us38) · [US40](../historias/ep06-painel-cliente.md#us40) |
| [US40](../historias/ep06-painel-cliente.md#us40) | Notificação automática por e-mail ao Cliente | EP06 | [US10](../historias/ep02-usuarios-perfis.md#us10) · [US37](../historias/ep06-painel-cliente.md#us37) | — | [US10](../historias/ep02-usuarios-perfis.md#us10) · [US24](../historias/ep03-cadastro-acordos.md#us24) · [US30](../historias/ep04-parcelas.md#us30) · [US39](../historias/ep06-painel-cliente.md#us39) |

---

## Cobertura por perfil { #perfis }

Toda história pertence a pelo menos um perfil de acesso. Histórias exercidas por mais de um perfil aparecem em ambas as linhas.

| Perfil | Histórias | Total |
| --- | --- | --- |
| **Visitante** | [US01](../historias/ep01-portal-autenticacao.md#us01) | 1 |
| **Usuário autenticado (qualquer perfil)** | [US02](../historias/ep01-portal-autenticacao.md#us02) · [US03](../historias/ep01-portal-autenticacao.md#us03) · [US05](../historias/ep01-portal-autenticacao.md#us05) · [US06](../historias/ep01-portal-autenticacao.md#us06) | 4 |
| **Administrador** | [US04](../historias/ep01-portal-autenticacao.md#us04) · [US07](../historias/ep02-usuarios-perfis.md#us07) · [US08](../historias/ep02-usuarios-perfis.md#us08) · [US09](../historias/ep02-usuarios-perfis.md#us09) · [US10](../historias/ep02-usuarios-perfis.md#us10) · [US11](../historias/ep02-usuarios-perfis.md#us11) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US23](../historias/ep03-cadastro-acordos.md#us23) · [US30](../historias/ep04-parcelas.md#us30) · [US31](../historias/ep04-parcelas.md#us31) · [US33](../historias/ep05-comissoes-metas.md#us33) · [US34](../historias/ep05-comissoes-metas.md#us34) · [US35](../historias/ep05-comissoes-metas.md#us35) · [US36](../historias/ep05-comissoes-metas.md#us36) | 14 |
| **Equipe Operacional** | [US12](../historias/ep03-cadastro-acordos.md#us12) · [US13](../historias/ep03-cadastro-acordos.md#us13) · [US14](../historias/ep03-cadastro-acordos.md#us14) · [US15](../historias/ep03-cadastro-acordos.md#us15) · [US16](../historias/ep03-cadastro-acordos.md#us16) · [US17](../historias/ep03-cadastro-acordos.md#us17) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US19](../historias/ep03-cadastro-acordos.md#us19) · [US20](../historias/ep03-cadastro-acordos.md#us20) · [US21](../historias/ep03-cadastro-acordos.md#us21) · [US22](../historias/ep03-cadastro-acordos.md#us22) · [US24](../historias/ep03-cadastro-acordos.md#us24) · [US25](../historias/ep04-parcelas.md#us25) · [US26](../historias/ep04-parcelas.md#us26) · [US28](../historias/ep04-parcelas.md#us28) · [US29](../historias/ep04-parcelas.md#us29) · [US30](../historias/ep04-parcelas.md#us30) · [US32](../historias/ep05-comissoes-metas.md#us32) | 18 |
| **Cliente (síndico/administradora)** | [US37](../historias/ep06-painel-cliente.md#us37) · [US38](../historias/ep06-painel-cliente.md#us38) · [US39](../historias/ep06-painel-cliente.md#us39) · [US40](../historias/ep06-painel-cliente.md#us40) | 4 |
| **Sistema (comportamento automático)** | [US27](../historias/ep04-parcelas.md#us27) | 1 |

---

## Pontos de partida { #raizes }

Histórias sem pré-requisitos — podem ser implementadas primeiro, em paralelo:

[US01](../historias/ep01-portal-autenticacao.md#us01) · [US02](../historias/ep01-portal-autenticacao.md#us02) · [US12](../historias/ep03-cadastro-acordos.md#us12)

## Histórias mais críticas { #criticas }

Histórias com maior número de dependentes diretos. Atraso ou mudança nelas se propaga por toda a cadeia:

| História | Dependentes diretos |
| --- | --- |
| [US15](../historias/ep03-cadastro-acordos.md#us15) — Cadastrar novo acordo | 10 ([US16](../historias/ep03-cadastro-acordos.md#us16) · [US17](../historias/ep03-cadastro-acordos.md#us17) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US19](../historias/ep03-cadastro-acordos.md#us19) · [US20](../historias/ep03-cadastro-acordos.md#us20) · [US21](../historias/ep03-cadastro-acordos.md#us21) · [US22](../historias/ep03-cadastro-acordos.md#us22) · [US24](../historias/ep03-cadastro-acordos.md#us24) · [US34](../historias/ep05-comissoes-metas.md#us34) · [US37](../historias/ep06-painel-cliente.md#us37)) |
| [US26](../historias/ep04-parcelas.md#us26) — Dar baixa em parcela paga | 7 ([US28](../historias/ep04-parcelas.md#us28) · [US29](../historias/ep04-parcelas.md#us29) · [US31](../historias/ep04-parcelas.md#us31) · [US32](../historias/ep05-comissoes-metas.md#us32) · [US33](../historias/ep05-comissoes-metas.md#us33) · [US36](../historias/ep05-comissoes-metas.md#us36) · [US38](../historias/ep06-painel-cliente.md#us38)) |
| [US07](../historias/ep02-usuarios-perfis.md#us07) — Convidar novo membro | 6 ([US08](../historias/ep02-usuarios-perfis.md#us08) · [US09](../historias/ep02-usuarios-perfis.md#us09) · [US10](../historias/ep02-usuarios-perfis.md#us10) · [US11](../historias/ep02-usuarios-perfis.md#us11) · [US18](../historias/ep03-cadastro-acordos.md#us18) · [US36](../historias/ep05-comissoes-metas.md#us36)) |
| [US12](../historias/ep03-cadastro-acordos.md#us12) — Cadastrar condomínio | 5 ([US10](../historias/ep02-usuarios-perfis.md#us10) · [US13](../historias/ep03-cadastro-acordos.md#us13) · [US14](../historias/ep03-cadastro-acordos.md#us14) · [US15](../historias/ep03-cadastro-acordos.md#us15) · [US23](../historias/ep03-cadastro-acordos.md#us23)) |
| [US17](../historias/ep03-cadastro-acordos.md#us17) — Fracionar dívida em parcelas | 5 ([US20](../historias/ep03-cadastro-acordos.md#us20) · [US24](../historias/ep03-cadastro-acordos.md#us24) · [US25](../historias/ep04-parcelas.md#us25) · [US26](../historias/ep04-parcelas.md#us26) · [US27](../historias/ep04-parcelas.md#us27)) |
| [US02](../historias/ep01-portal-autenticacao.md#us02) — Login no sistema | 5 ([US03](../historias/ep01-portal-autenticacao.md#us03) · [US04](../historias/ep01-portal-autenticacao.md#us04) · [US05](../historias/ep01-portal-autenticacao.md#us05) · [US06](../historias/ep01-portal-autenticacao.md#us06) · [US07](../historias/ep02-usuarios-perfis.md#us07)) |

---

## Mapa de dependências { #mapa }

Grafo completo de pré-requisitos, agrupado por épico. Cada seta lê-se como **"é pré-requisito de"**.

``` mermaid
graph TD
  subgraph EP01["EP01 · Portal Institucional & Autenticação"]
    direction TB
    US01
    US02
    US03
    US04
    US05
    US06
  end
  subgraph EP02["EP02 · Gestão de Usuários e Perfis"]
    direction TB
    US07
    US08
    US09
    US10
    US11
  end
  subgraph EP03["EP03 · Cadastro de Acordos"]
    direction TB
    US12
    US13
    US14
    US15
    US16
    US17
    US18
    US19
    US20
    US21
    US22
    US23
    US24
  end
  subgraph EP04["EP04 · Acompanhamento de Parcelas"]
    direction TB
    US25
    US26
    US27
    US28
    US29
    US30
    US31
  end
  subgraph EP05["EP05 · Comissões e Metas"]
    direction TB
    US32
    US33
    US34
    US35
    US36
  end
  subgraph EP06["EP06 · Painel do Cliente"]
    direction TB
    US37
    US38
    US39
    US40
  end
  US02 --> US03
  US02 --> US07
  US01 --> US04
  US02 --> US04
  US02 --> US05
  US02 --> US06
  US07 --> US08
  US07 --> US09
  US07 --> US10
  US12 --> US10
  US07 --> US11
  US08 --> US11
  US09 --> US11
  US12 --> US13
  US12 --> US14
  US13 --> US14
  US12 --> US15
  US13 --> US15
  US15 --> US16
  US15 --> US17
  US07 --> US18
  US15 --> US18
  US15 --> US19
  US15 --> US20
  US17 --> US20
  US15 --> US21
  US15 --> US22
  US12 --> US23
  US15 --> US24
  US17 --> US24
  US17 --> US25
  US17 --> US26
  US25 --> US26
  US17 --> US27
  US26 --> US28
  US26 --> US29
  US27 --> US30
  US18 --> US30
  US26 --> US31
  US26 --> US32
  US36 --> US32
  US16 --> US33
  US26 --> US33
  US15 --> US34
  US27 --> US34
  US33 --> US34
  US25 --> US35
  US07 --> US36
  US26 --> US36
  US10 --> US37
  US15 --> US37
  US37 --> US38
  US26 --> US38
  US24 --> US39
  US37 --> US39
  US10 --> US40
  US37 --> US40
```

A leitura de cima para baixo dá uma ordem de implementação possível: as histórias de [pontos de partida](#raizes) primeiro, e cada história depois de todas as que apontam para ela.

Cada nó é uma história; cada seta lê-se como "é pré-requisito de". O grafo é gerado a partir da coluna **Depende de** da matriz acima.

---

## Manutenção desta página { #manutencao }

Ao criar, remover ou repriorizar uma história:

1. Atualize os campos **Depende de** e **Relaciona-se com** na página do épico.
2. Acrescente o link recíproco nas histórias citadas.
3. Reflita a mudança nesta matriz e no [índice completo](../historias/index.md#indice).

As convenções de identificação estão em [Histórias de usuário → convenções](../historias/index.md#convencoes).
