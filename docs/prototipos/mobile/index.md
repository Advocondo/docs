---
icon: lucide/smartphone
title: Mobile
---

# Protótipos mobile

Catorze telas do sistema de **Gestão de Acordos Extrajudiciais** em 390px de largura, uma por arquivo HTML, compostas com os componentes do design system e ligadas às [histórias de usuário](../../historias/index.md). Elas partem das [telas do Figma](../index.md) e da [cobertura das histórias](../cobertura-historias.md): onde o desktop deixava lacuna (devedor, responsável, plano de parcelas, inativação, metas, sessões), o mobile já traz a solução.

## Onde estão e como abrir

Os arquivos ficam em `prototipos/mobile/` no repositório [`Advocondo/ui-kit`](https://github.com/Advocondo/ui-kit), com um `index.html` que lista todas as telas e estados. Cada arquivo é autocontido: carrega `styles.css` e o bundle do design system, os dados fictícios em `window.EA_MOBILE` e um kit de layout mobile inline. Como o kit usa Babel no navegador, abra por http:

```bash
python3 -m http.server 8000
```

Depois acesse `http://localhost:8000/prototipos/mobile/index.html`. Os estados de cada tela são parâmetros de URL (`?estado=`), e `?perfil=admin` mostra a visão do administrador onde ela existe. A navegação inferior liga as telas entre si.

## Modelo de navegação

| Elemento | Como funciona | Componente |
| --- | --- | --- |
| Barra superior | Navy, 56px, com voltar à esquerda, título e subtítulo, ações à direita (sino, exportar, editar). | layout inline sobre tokens; `IconButton variant="inverse"` |
| Navegação inferior | Cinco itens: Painel, Acordos, Mês, Condomínios, Mais. O item ativo leva marcador navy de 2px no topo. | layout inline sobre tokens; `Icon` |
| Menu "Mais" | Metas e comissões, Trilha, Gestão de usuários, Perfil e Sair. Itens restritos só para o administrador. | `Card`, `Badge` |
| Formulários | Tela cheia, com rodapé fixo (ação primária em largura total e Cancelar abaixo). | `FieldLabel`, `Input`, `Select`, `Radio`, `Switch`, `Checkbox`, `Textarea`, `Button` |
| Confirmações | Diálogo centralizado de 342px, Cancelar à esquerda e ação primária à direita. | `Dialog` |
| Feedback | Toast acima da navegação inferior; alertas no fluxo; estado vazio em card. | `Toast`, `Alert`, `EmptyState` |
| Indicadores | Dois por linha, valor em Playfair no tamanho de título. | `MetricCard` |

Barra superior e navegação inferior não existem como componentes do design system; são propostas para uma futura versão mobile, junto de um `Sheet` (folha inferior) no lugar do `Dialog` centralizado.

## Dados de demonstração

Um único conjunto de dados alimenta todas as telas: 5 condomínios, 11 devedores, 11 acordos, 9 faturas de setembro de 2026, 8 usuários, 10 registros de auditoria e 3 sessões. Os totais batem entre Painel, Faturas do mês, Metas e Trilha (previsto R$ 10.104,26, recebido R$ 2.820,00, atrasado R$ 2.290,00). A pessoa logada é a Dra. Sarah Holanda (Equipe Operacional, advogada) ou, com `?perfil=admin`, a Dra. Amanda Pessoa. Condomínios, devedores, valores, OAB e e-mails são inventados; os nomes da equipe são os publicados pelo escritório.

## Catálogo

| Tela | Histórias | Estados | Arquivo |
| --- | --- | --- | --- |
| [Site institucional](site-institucional.md) | [US01](../../historias/ep01-portal-autenticacao.md#us01) | 2 | `site-institucional.html` |
| [Login](login.md) | [US02](../../historias/ep01-portal-autenticacao.md#us02) | 1 | `login.html` |
| [Redefinir senha](redefinir-senha.md) | [US03](../../historias/ep01-portal-autenticacao.md#us03) | 4 | `redefinir-senha.html` |
| [Painel](painel.md) | [US30](../../historias/ep04-parcelas.md#us30), [US32](../../historias/ep05-comissoes-metas.md#us32), [US34](../../historias/ep05-comissoes-metas.md#us34) | 2 | `painel.html` |
| [Mais](mais.md) | [US07](../../historias/ep02-usuarios-perfis.md#us07), [US11](../../historias/ep02-usuarios-perfis.md#us11), [US32](../../historias/ep05-comissoes-metas.md#us32) | 1 | `mais.html` |
| [Acordos](acordos.md) | [US13](../../historias/ep03-cadastro-acordos.md#us13), [US14](../../historias/ep03-cadastro-acordos.md#us14), [US15](../../historias/ep03-cadastro-acordos.md#us15), [US16](../../historias/ep03-cadastro-acordos.md#us16), [US17](../../historias/ep03-cadastro-acordos.md#us17), [US18](../../historias/ep03-cadastro-acordos.md#us18), [US22](../../historias/ep03-cadastro-acordos.md#us22) | 5 | `acordos.html` |
| [Detalhes do acordo](detalhes-do-acordo.md) | [US16](../../historias/ep03-cadastro-acordos.md#us16), [US17](../../historias/ep03-cadastro-acordos.md#us17), [US19](../../historias/ep03-cadastro-acordos.md#us19), [US20](../../historias/ep03-cadastro-acordos.md#us20), [US21](../../historias/ep03-cadastro-acordos.md#us21), [US24](../../historias/ep03-cadastro-acordos.md#us24), [US31](../../historias/ep04-parcelas.md#us31) | 7 | `detalhes-do-acordo.html` |
| [Faturas do mês](acompanhamento-mensal.md) | [US25](../../historias/ep04-parcelas.md#us25), [US26](../../historias/ep04-parcelas.md#us26), [US27](../../historias/ep04-parcelas.md#us27), [US28](../../historias/ep04-parcelas.md#us28), [US29](../../historias/ep04-parcelas.md#us29), [US35](../../historias/ep05-comissoes-metas.md#us35) | 6 | `acompanhamento-mensal.html` |
| [Condomínios](condominios.md) | [US12](../../historias/ep03-cadastro-acordos.md#us12), [US23](../../historias/ep03-cadastro-acordos.md#us23) | 4 | `condominios.html` |
| [Metas e comissões](metas-e-comissoes.md) | [US32](../../historias/ep05-comissoes-metas.md#us32), [US33](../../historias/ep05-comissoes-metas.md#us33), [US36](../../historias/ep05-comissoes-metas.md#us36) | 2 | `metas-e-comissoes.html` |
| [Trilha de auditoria](trilha-de-auditoria.md) | [US11](../../historias/ep02-usuarios-perfis.md#us11), [US19](../../historias/ep03-cadastro-acordos.md#us19), [US31](../../historias/ep04-parcelas.md#us31) | 3 | `trilha-de-auditoria.html` |
| [Gestão de usuários](gestao-de-usuarios.md) | [US07](../../historias/ep02-usuarios-perfis.md#us07), [US08](../../historias/ep02-usuarios-perfis.md#us08), [US09](../../historias/ep02-usuarios-perfis.md#us09), [US10](../../historias/ep02-usuarios-perfis.md#us10), [US11](../../historias/ep02-usuarios-perfis.md#us11) | 5 | `gestao-de-usuarios.html` |
| [Meu perfil](perfil.md) | [US05](../../historias/ep01-portal-autenticacao.md#us05), [US06](../../historias/ep01-portal-autenticacao.md#us06) | 2 | `perfil.html` |
| [Sobreposições](sobreposicoes.md) | — | 2 | `sobreposicoes.html` |

## Cobertura das histórias no mobile

Situação de cada história nas telas mobile, com o mesmo critério da [cobertura do Figma](../cobertura-historias.md). Resultado: 33 histórias atendidas, 2 parciais e 5 não demonstradas (a edição da landing e o painel do Cliente, ambos fora do MVP).

### EP01 · Portal e autenticação

| História | Tela mobile | Situação | Observação |
| --- | --- | --- | --- |
| [US01](../../historias/ep01-portal-autenticacao.md#us01) | Site institucional | Atende | entrada para o Login no cabeçalho e no hero |
| [US02](../../historias/ep01-portal-autenticacao.md#us02) | Login | Atende | erro genérico demonstrado |
| [US03](../../historias/ep01-portal-autenticacao.md#us03) | Redefinir senha | Atende | fluxo completo em cinco telas |
| [US04](../../historias/ep01-portal-autenticacao.md#us04) | — | Não demonstrada | edição da landing pelo administrador |
| [US05](../../historias/ep01-portal-autenticacao.md#us05) | Perfil | Atende | senha atual exigida |
| [US06](../../historias/ep01-portal-autenticacao.md#us06) | Perfil | Atende | sessões encerradas uma a uma ou todas |

### EP02 · Usuários e perfis

| História | Tela mobile | Situação | Observação |
| --- | --- | --- | --- |
| [US07](../../historias/ep02-usuarios-perfis.md#us07) | Gestão de usuários | Atende | convite com nível de acesso e OAB |
| [US08](../../historias/ep02-usuarios-perfis.md#us08) | Gestão de usuários | Atende | inativar e reativar |
| [US09](../../historias/ep02-usuarios-perfis.md#us09) | Gestão de usuários | Atende | nível de acesso na edição |
| [US10](../../historias/ep02-usuarios-perfis.md#us10) | Gestão de usuários | Atende | Cliente vinculado a condomínios |
| [US11](../../historias/ep02-usuarios-perfis.md#us11) | Gestão de usuários, Trilha | Atende | histórico por usuário e na trilha |

### EP03 · Cadastro de acordos

| História | Tela mobile | Situação | Observação |
| --- | --- | --- | --- |
| [US12](../../historias/ep03-cadastro-acordos.md#us12) | Condomínios | Atende | cadastro e edição |
| [US13](../../historias/ep03-cadastro-acordos.md#us13) | Acordos | Atende | novo devedor com alerta de duplicidade |
| [US14](../../historias/ep03-cadastro-acordos.md#us14) | Acordos | Atende | validação linha a linha |
| [US15](../../historias/ep03-cadastro-acordos.md#us15) | Acordos | Atende | devedor, condomínio, valor e responsável |
| [US16](../../historias/ep03-cadastro-acordos.md#us16) | Acordos, Detalhes | Atende | divisão por parcela na prévia e no plano |
| [US17](../../historias/ep03-cadastro-acordos.md#us17) | Acordos, Detalhes | Parcial | parcelas geradas; edição de uma parcela só como botão |
| [US18](../../historias/ep03-cadastro-acordos.md#us18) | Acordos | Atende | seleção restrita a advogados; reatribuição no histórico |
| [US19](../../historias/ep03-cadastro-acordos.md#us19) | Detalhes | Atende | aviso de parcelas pagas e motivo |
| [US20](../../historias/ep03-cadastro-acordos.md#us20) | Detalhes | Atende | cancelamento com motivo; status na lista |
| [US21](../../historias/ep03-cadastro-acordos.md#us21) | Detalhes | Parcial | lista e download; upload só como botão |
| [US22](../../historias/ep03-cadastro-acordos.md#us22) | Acordos | Atende | busca e filtros combináveis |
| [US23](../../historias/ep03-cadastro-acordos.md#us23) | Condomínios | Atende | etiqueta a 45 dias e registro da renovação |
| [US24](../../historias/ep03-cadastro-acordos.md#us24) | Detalhes | Atende | PDF com download e link |

### EP04 · Parcelas

| História | Tela mobile | Situação | Observação |
| --- | --- | --- | --- |
| [US25](../../historias/ep04-parcelas.md#us25) | Faturas do mês | Atende | devedor, condomínio, valor, status e filtros |
| [US26](../../historias/ep04-parcelas.md#us26) | Faturas do mês | Atende | baixa com data e meio |
| [US27](../../historias/ep04-parcelas.md#us27) | Faturas do mês | Atende | status calculado; notificação |
| [US28](../../historias/ep04-parcelas.md#us28) | Faturas do mês | Atende | parcial com saldo |
| [US29](../../historias/ep04-parcelas.md#us29) | Faturas do mês | Atende | nota fiscal na baixa; recorte sem nota |
| [US30](../../historias/ep04-parcelas.md#us30) | Painel | Atende | sino com contador e central |
| [US31](../../historias/ep04-parcelas.md#us31) | Trilha de auditoria | Atende | autor, data e hora, valor |

### EP05 · Comissões e metas

| História | Tela mobile | Situação | Observação |
| --- | --- | --- | --- |
| [US32](../../historias/ep05-comissoes-metas.md#us32) | Metas e comissões | Atende | só o próprio |
| [US33](../../historias/ep05-comissoes-metas.md#us33) | Metas e comissões | Atende | visão do escritório |
| [US34](../../historias/ep05-comissoes-metas.md#us34) | Painel | Atende | indicadores com filtro de período |
| [US35](../../historias/ep05-comissoes-metas.md#us35) | Faturas do mês | Atende | exportação com os filtros da tela |
| [US36](../../historias/ep05-comissoes-metas.md#us36) | Metas e comissões | Atende | definição de meta por colaborador |

### EP06 · Painel do Cliente

| História | Tela mobile | Situação | Observação |
| --- | --- | --- | --- |
| [US37](../../historias/ep06-painel-cliente.md#us37) | — | Não demonstrada | painel do Cliente não desenhado |
| [US38](../../historias/ep06-painel-cliente.md#us38) | — | Não demonstrada |  |
| [US39](../../historias/ep06-painel-cliente.md#us39) | — | Não demonstrada |  |
| [US40](../../historias/ep06-painel-cliente.md#us40) | — | Não demonstrada |  |

