---
icon: lucide/users
title: Gestão de Usuários
---

# Gestão de Usuários

Listagem dos membros da equipe com dois diálogos: um de edição e um de convite. Os dois frames repetem a mesma listagem ao fundo e trazem uma camada `Overlay` com o diálogo.

| | |
| --- | --- |
| Origem | **Criado no Figma** |
| Nós no Figma | listagem com diálogo de edição [124:2095](https://www.figma.com/design/jEwHxavSrPVQrm3hGSLGtC/edson-alexandre-advogados_design-system?node-id=124-2095) · listagem com Convidar Membro [124:2537](https://www.figma.com/design/jEwHxavSrPVQrm3hGSLGtC/edson-alexandre-advogados_design-system?node-id=124-2537) |
| Fonte no repositório | não existe; a composição segue `ui_kits/plataforma_processos/Condominios.jsx` |
| Componentes | `SidebarNav`, `TopBar`, `Input icon="search"`, `Button`, `DataTable`, `Badge` (perfil), `StatusPill` (status), `IconButton` (ações), `Dialog`, `FieldLabel`, `Input`, `Select` |
| Histórias de usuário | [US07](../historias/ep02-usuarios-perfis.md#us07) (convidar), sem a marcação de advogado com OAB da US07-CA04, e [US09](../historias/ep02-usuarios-perfis.md#us09) (definir perfil). [US08](../historias/ep02-usuarios-perfis.md#us08) (inativar) não é demonstrada: não há usuário inativo nem ação de inativar. [US10](../historias/ep02-usuarios-perfis.md#us10) (vincular Cliente a condomínios) não existe, e o perfil Cliente não aparece. Ver a [cobertura das histórias](cobertura-historias.md). |

## Listagem

- Busca "Buscar funcionário" e ação "Convidar Membro".
- Colunas: Nome, E-mail, Perfil, Status, Ações.

| Nome | E-mail | Perfil | Status |
| --- | --- | --- | --- |
| Dr. Edson Alexandre | edson@example.com | Administrador | Ativo |
| Dra. Amanda | amanda@example.com | Administrador | Ativo |
| Arthur | arthur@example.com | Equipe Operacional | Ativo |

Os perfis previstos são **Administrador** e **Equipe Operacional**.

## Diálogo de edição

Frame [124:2095](https://www.figma.com/design/jEwHxavSrPVQrm3hGSLGtC/edson-alexandre-advogados_design-system?node-id=124-2095). Campos Nome Completo (obrigatório, exemplo "Lucas Gonçalves Castro"), E-mail e "Selecione o Perfil". Ações: Cancelar e "Salvar prazo".

## Diálogo Convidar Membro

Frame [124:2537](https://www.figma.com/design/jEwHxavSrPVQrm3hGSLGtC/edson-alexandre-advogados_design-system?node-id=124-2537). Mesmos campos do diálogo de edição. Ações: Cancelar e Convidar.

!!! info "Capturas pendentes"

    Os dois frames ainda não têm captura exportada. Exporte-os em PNG a 1x como `assets/prototipos/gestao-de-usuarios.png` e `gestao-de-usuarios-convidar-membro.png`.

## Pontos de atenção

- O diálogo de edição confirma com "Salvar prazo", rótulo herdado do design system. Deve ser "Salvar alterações".
- Os dois diálogos são idênticos nos campos; o que os diferencia é só o botão. Se a edição é do mesmo formulário, um único `Dialog` com título e ação variáveis basta.
- A listagem só mostra usuários ativos. A [Trilha de auditoria](trilha-de-auditoria.md) registra "Inativação de Usuário", então faltam o status Inativo na coluna Status e a ação de inativar (com confirmação) na coluna Ações.
- O texto de contexto do Login menciona "síndicos autorizados", mas não há perfil de síndico aqui. Confirme se o acesso de clientes está no escopo.
- Os e-mails `example.com` são placeholders adequados; mantenha assim até ter dados reais.
- O convite não permite marcar o usuário como advogado nem informar o número da OAB ([US07](../historias/ep02-usuarios-perfis.md#us07)). Essa marcação é independente do perfil e define quem pode ser responsável por um acordo ([US18](../historias/ep03-cadastro-acordos.md#us18)).
