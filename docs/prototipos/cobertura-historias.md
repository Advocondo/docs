---
icon: lucide/list-checks
title: Cobertura das histórias
---

# Cobertura das histórias de usuário

Verificação das telas do Figma contra as 40 [histórias de usuário](../historias/index.md) desta documentação, organizadas em seis épicos. A análise usa o conteúdo de cada frame no arquivo do Figma em 14/09/2026.

| Situação | Significado |
| --- | --- |
| **Atende** | A tela demonstra o comportamento principal da história. Regras de sistema (validações, cálculos automáticos) ficam fora da verificação. |
| **Parcial** | A tela cobre parte da história, mas falta algo que os critérios de aceitação pedem. |
| **Não demonstrada** | Nenhuma tela do Figma cobre a história. |

!!! note "Sobre o recorte de MVP"

    O recorte de MVP vem do índice dos protótipos de requisito, montado sobre uma versão anterior das histórias, com 37 itens. Os números foram convertidos para a sequência atual. [US18](../historias/ep03-cadastro-acordos.md#us18), [US24](../historias/ep03-cadastro-acordos.md#us24) e [US40](../historias/ep06-painel-cliente.md#us40) entraram depois e ainda não foram classificadas.

## Resumo

| Recorte | Histórias | Atende | Parcial | Não demonstrada |
| --- | --- | --- | --- | --- |
| MVP | 16 | 4 | 9 | 3 |
| Fora do MVP | 21 | 5 | 9 | 7 |
| Ainda não classificadas | 3 | 0 | 0 | 3 |
| **Total** | **40** | **9** | **18** | **13** |

As três histórias do MVP sem tela são [US08](../historias/ep02-usuarios-perfis.md#us08) (inativar usuário), [US13](../historias/ep03-cadastro-acordos.md#us13) (cadastrar devedor) e [US36](../historias/ep05-comissoes-metas.md#us36) (definir metas por colaborador). A lacuna que mais pesa é a US13: o devedor não existe em nenhuma tela, e quatro outras histórias dependem dele.

## EP01 · Portal institucional e autenticação

| História | Tela no Figma | Situação | O que falta |
| --- | --- | --- | --- |
| [US01](../historias/ep01-portal-autenticacao.md#us01) Landing page institucional (MVP) | [Site institucional](site-institucional.md) | Parcial | US01-CA03 pede um ponto de entrada para o Login; a navegação do site tem só Atuação, Assessoria, Por que nós? e Contato. |
| [US02](../historias/ep01-portal-autenticacao.md#us02) Login (MVP) | [Login](login.md) | Atende | O estado de erro genérico de US02-CA02 não é demonstrado. |
| [US03](../historias/ep01-portal-autenticacao.md#us03) Recuperação de senha | [Redefinir Senha](redefinir-senha.md) | Parcial | Só o passo final. Faltam a solicitação por e-mail, o link expirado e a confirmação de sucesso. |
| [US04](../historias/ep01-portal-autenticacao.md#us04) Página institucional editável | nenhuma | Não demonstrada | Exigiria uma área de edição de blocos para o Administrador. |
| [US05](../historias/ep01-portal-autenticacao.md#us05) Editar dados do próprio perfil | [Perfil](perfil.md) | Atende | Pede a senha atual, como a história exige. Separar a troca de senha dos dados cadastrais. |
| [US06](../historias/ep01-portal-autenticacao.md#us06) Encerrar sessões em outros dispositivos | nenhuma | Não demonstrada | Caberia como bloco na tela de Perfil. |

## EP02 · Gestão de usuários e perfis

| História | Tela no Figma | Situação | O que falta |
| --- | --- | --- | --- |
| [US07](../historias/ep02-usuarios-perfis.md#us07) Convidar novo membro (MVP) | [Gestão de Usuários](gestao-de-usuarios.md#dialogo-convidar-membro) | Parcial | E-mail e perfil presentes. Falta a marcação de advogado com número da OAB (US07-CA04), que alimenta a US18. |
| [US08](../historias/ep02-usuarios-perfis.md#us08) Inativar acesso (MVP) | [Gestão de Usuários](gestao-de-usuarios.md) | Não demonstrada | A coluna Ações existe, mas não há ação de inativar, nenhum usuário com status Inativo e nenhuma reativação. |
| [US09](../historias/ep02-usuarios-perfis.md#us09) Definir nível de acesso (MVP) | [Gestão de Usuários](gestao-de-usuarios.md#dialogo-de-edicao) | Atende | O diálogo de edição tem "Selecione o Perfil"; o botão ainda diz "Salvar prazo". |
| [US10](../historias/ep02-usuarios-perfis.md#us10) Vincular Cliente a condomínios | nenhuma | Não demonstrada | O perfil Cliente não existe nas telas; os perfis são Administrador e Equipe Operacional. |
| [US11](../historias/ep02-usuarios-perfis.md#us11) Histórico da gestão de usuários | [Trilha de auditoria](trilha-de-auditoria.md) | Atende | A linha "Inativação de Usuário" traz autor, data e hora. |

## EP03 · Cadastro de acordos

| História | Tela no Figma | Situação | O que falta |
| --- | --- | --- | --- |
| [US12](../historias/ep03-cadastro-acordos.md#us12) Cadastrar condomínio | [Condomínios](condominios.md#dialogo-novo-condominio) | Atende | Nome, endereço e síndico. A edição posterior não tem ação na listagem. |
| [US13](../historias/ep03-cadastro-acordos.md#us13) Cadastrar devedor (MVP) | nenhuma | Não demonstrada | O devedor não aparece em nenhuma tela. Acordos e Acompanhamento identificam a dívida só por condomínio e unidade; não há nome, contato nem alerta de duplicidade. |
| [US14](../historias/ep03-cadastro-acordos.md#us14) Importar inadimplentes em lote | [Acordos](acordos.md#dialogo-importar-inadimplentes) | Parcial | Upload e modelo de planilha presentes. Falta a validação que aponta linhas com erro antes de confirmar. |
| [US15](../historias/ep03-cadastro-acordos.md#us15) Cadastrar novo acordo (MVP) | [Acordos](acordos.md#dialogo-novo-acordo) | Parcial | Tem condomínio, unidade e valor total. Faltam devedor e responsável, ambos pedidos na história. |
| [US16](../historias/ep03-cadastro-acordos.md#us16) Definir honorários (MVP) | [Acordos](acordos.md#dialogo-novo-acordo), [Detalhes do Acordo](detalhes-do-acordo.md) | Parcial | Honorários informados no cadastro e separados do repasse no detalhe. A separação por parcela não aparece. |
| [US17](../historias/ep03-cadastro-acordos.md#us17) Fracionar em parcelas (MVP) | [Acordos](acordos.md#dialogo-novo-acordo) | Parcial | Quantidade e primeiro vencimento no cadastro. As parcelas geradas não aparecem no detalhe, e não há edição de uma parcela específica. |
| [US18](../historias/ep03-cadastro-acordos.md#us18) Atribuir advogado responsável | nenhuma | Não demonstrada | Nenhum cadastro tem campo de responsável. A coluna Responsável do Acompanhamento Mensal mostra um nome, mas não há seleção restrita a advogados nem histórico de reatribuição. |
| [US19](../historias/ep03-cadastro-acordos.md#us19) Editar acordo | [Detalhes do Acordo](detalhes-do-acordo.md) | Parcial | Só o botão Editar. Sem formulário e sem a confirmação extra para acordos com parcelas pagas. |
| [US20](../historias/ep03-cadastro-acordos.md#us20) Cancelar/encerrar acordo | [Detalhes do Acordo](detalhes-do-acordo.md) | Parcial | Só o botão Cancelar, sem confirmação. A listagem conhece apenas Ativo e Concluído; falta o status cancelado. |
| [US21](../historias/ep03-cadastro-acordos.md#us21) Anexar documentos | [Detalhes do Acordo](detalhes-do-acordo.md) | Parcial | Lista de anexos com um arquivo; sem ação de upload visível. |
| [US22](../historias/ep03-cadastro-acordos.md#us22) Buscar/filtrar acordos (MVP) | [Acordos](acordos.md#listagem) | Parcial | A busca fala em "número CNJ, cliente ou unidade" e os filtros são herança de Processos. A história pede devedor, condomínio e responsável, combináveis com status. |
| [US23](../historias/ep03-cadastro-acordos.md#us23) Renovação de contrato | [Condomínios](condominios.md#dialogo-novo-condominio) | Parcial | Datas de início e de renovação no cadastro. Sem sinalização de "próximo da renovação" na listagem nem registro da renovação feita. |
| [US24](../historias/ep03-cadastro-acordos.md#us24) Gerar e salvar PDF do acordo | nenhuma | Não demonstrada | O Detalhes do Acordo não tem ação de gerar PDF nem link de acesso ao arquivo. |

## EP04 · Acompanhamento mensal de parcelas

| História | Tela no Figma | Situação | O que falta |
| --- | --- | --- | --- |
| [US25](../historias/ep04-parcelas.md#us25) Listar faturas do mês (MVP) | [Acompanhamento Mensal](acompanhamento-mensal.md#tela) | Parcial | Lista com condomínio, unidade, valor e situação. Sem devedor e sem filtros por condomínio, responsável ou status. |
| [US26](../historias/ep04-parcelas.md#us26) Dar baixa em parcela paga (MVP) | [Acompanhamento Mensal](acompanhamento-mensal.md#dialogo-registrar-baixa) | Atende | Data do pagamento e confirmação. O cálculo automático da comissão é regra de sistema. |
| [US27](../historias/ep04-parcelas.md#us27) Sinalizar parcela em atraso (MVP) | [Acompanhamento Mensal](acompanhamento-mensal.md#tela) | Atende | Status "Atrasado" na tabela e indicador "Inadimplência do mês". |
| [US28](../historias/ep04-parcelas.md#us28) Registrar pagamento parcial (MVP) | [Acompanhamento Mensal](acompanhamento-mensal.md#dialogo-registrar-baixa) | Parcial | O campo Valor permite informar um valor menor, mas nada mostra o saldo restante nem o histórico de pagamentos parciais. |
| [US29](../historias/ep04-parcelas.md#us29) Registrar emissão de nota fiscal | [Acompanhamento Mensal](acompanhamento-mensal.md#dialogo-registrar-baixa) | Atende | "Nota Fiscal Emitida?" e "Número da NF" no diálogo de baixa. Falta a consulta de parcelas pagas sem nota. |
| [US30](../historias/ep04-parcelas.md#us30) Notificação interna de atraso | barra superior de todas as telas | Parcial | O ícone de sino vem do `TopBar` herdado. Nenhum estado de notificação nem o destino ao clicar foi desenhado. |
| [US31](../historias/ep04-parcelas.md#us31) Log de alterações financeiras | [Trilha de auditoria](trilha-de-auditoria.md) | Atende | "Baixa de Parcela" e "Alteração de Acordo" com autor, data e hora. O valor alterado não tem coluna própria. |

## EP05 · Comissões e metas

| História | Tela no Figma | Situação | O que falta |
| --- | --- | --- | --- |
| [US32](../historias/ep05-comissoes-metas.md#us32) Minhas metas e comissões (MVP) | [Metas e Comissões](metas-e-comissoes.md) | Parcial | Comissões por parcela paga. Não há a meta do próprio colaborador nem o percentual de atingimento, e a tela não distingue o que o operador vê do que o administrador vê. |
| [US33](../historias/ep05-comissoes-metas.md#us33) Visão global de faturamento | [Metas e Comissões](metas-e-comissoes.md) | Parcial | Não há faturamento consolidado nem coluna de colaborador na tabela. |
| [US34](../historias/ep05-comissoes-metas.md#us34) Dashboard de indicadores | [Painel](painel.md) | Parcial | Indicadores presentes (total recuperado, faturas em atraso, acordos ativos, honorários). Sem filtro por período; os blocos de prazos e movimentações são herança da EA Processos. |
| [US35](../historias/ep05-comissoes-metas.md#us35) Exportar relatório de acompanhamento | nenhuma | Não demonstrada | O único "Exportar planilha" está na Trilha de auditoria, não no Acompanhamento Mensal. |
| [US36](../historias/ep05-comissoes-metas.md#us36) Definir metas por colaborador (MVP) | nenhuma | Não demonstrada | Metas e Comissões mostra resultados, não a definição da meta por pessoa. |

## EP06 · Painel do Cliente

| História | Tela no Figma | Situação | O que falta |
| --- | --- | --- | --- |
| [US37](../historias/ep06-painel-cliente.md#us37) Consultar status dos acordos do condomínio | nenhuma | Não demonstrada | O painel do Cliente não existe no Figma. |
| [US38](../historias/ep06-painel-cliente.md#us38) Histórico de pagamentos de um morador | nenhuma | Não demonstrada | Depende da US37 e do devedor da US13. |
| [US39](../historias/ep06-painel-cliente.md#us39) Baixar relatório simplificado | nenhuma | Não demonstrada | Depende da US37. O relatório agora é um PDF (US39-CA01), gerado como na US24. |
| [US40](../historias/ep06-painel-cliente.md#us40) Notificação automática por e-mail ao Cliente | nenhuma | Não demonstrada | O disparo é automático e não precisa de tela própria, mas o registro das datas de envio não aparece em lugar nenhum. |

## Lacunas transversais

1. **Devedor.** A entidade central da recuperação de crédito não aparece em nenhuma tela. Afeta US13, US15, US22, US25 e US38. Sem ela, o acordo é identificado por condomínio e unidade, o que não permite buscar pelo nome nem evitar cadastros duplicados.
2. **Advogado responsável.** A US18 formaliza a atribuição, restrita a usuários marcados como advogado na US07. Nenhuma das duas pontas está desenhada: o convite não tem a marcação de OAB e o cadastro de acordo não tem o campo de responsável. O responsável também é filtro em US22 e US25 e base das comissões em US26 e US32.
3. **Plano de parcelas.** Nenhuma tela mostra as parcelas geradas de um acordo (US17), e o detalhe não separa valor do condomínio e honorários por parcela (US16). O Detalhes do Acordo é o lugar natural para essa tabela.
4. **PDF.** US24 e US39 pedem geração de PDF, com download e link de acesso. Nenhuma tela tem essa ação.
5. **Perfil Cliente.** Não existe nas telas, embora o Login mencione "síndicos autorizados". Afeta US10 e todo o EP06 (US37 a US40).
6. **Herança da EA Processos.** Filtros de Processos na listagem de Acordos, calendário com "Prazo fatal" no Acompanhamento e em Metas, blocos de prazos e movimentações no Painel: nada disso vem das histórias.
7. **Terminologia.** As histórias usam "fatura" (US25) e "parcela" (US26 a US29); o Figma usa só "parcela"; o protótipo de requisito chama a tela de "Faturas do mês". Escolha um termo e mantenha em todas as frentes.

## Ordem sugerida para fechar o MVP

1. Trazer o devedor para o diálogo Novo Acordo, a listagem de Acordos e o Acompanhamento Mensal (US13, US15, US22, US25).
2. Acrescentar a marcação de advogado com OAB ao convite e o campo de responsável, restrito a advogados, ao Novo Acordo e aos filtros (US07, US15, US18, US22, US25).
3. Demonstrar a inativação e a reativação de usuário em Gestão de Usuários (US08).
4. Desenhar a definição de metas por colaborador e separar a visão do operador da visão do administrador em Metas e Comissões (US32, US36).
5. Mostrar o plano de parcelas no Detalhes do Acordo, com a divisão entre condomínio e honorários por parcela (US16, US17).
