---
icon: lucide/user
title: Perfil
---

# Perfil

Tela do próprio usuário para atualizar nome, e-mail e senha.

| | |
| --- | --- |
| Origem | **Criado no Figma** |
| Nó no Figma | [51:2](https://www.figma.com/design/jEwHxavSrPVQrm3hGSLGtC/edson-alexandre-advogados_design-system?node-id=51-2) |
| Fonte no repositório | não existe |
| Componentes | `SidebarNav`, `TopBar`, `Card`, `FieldLabel`, `Input`, `Input type="password"`, `Button` |
| Histórias de usuário | [US05](../historias/ep01-portal-autenticacao.md#us05) (editar o próprio perfil, com senha atual). [US06](../historias/ep01-portal-autenticacao.md#us06) (encerrar sessões em outros dispositivos) não aparece. Ver a [cobertura das histórias](cobertura-historias.md). |

## O que a tela mostra

- Título "Perfil".
- Campos: Nome (obrigatório, exemplo "Fulano de Tal"), E-mail (email@example.com), Senha e Senha Atual.
- Ações: Cancelar e Salvar.

!!! info "Captura pendente"

    Este frame foi criado no Figma e ainda não tem captura exportada. Abra o [nó 51:2](https://www.figma.com/design/jEwHxavSrPVQrm3hGSLGtC/edson-alexandre-advogados_design-system?node-id=51-2) ou exporte o frame em PNG a 1x como `assets/prototipos/perfil.png`.

## Pontos de atenção

- A ordem dos campos de senha está invertida: peça primeiro "Senha atual", depois "Nova senha" e "Confirmar nova senha". Separe a troca de senha dos dados cadastrais, com o próprio botão, para que salvar o nome não exija a senha.
- Não há caminho visível para esta tela na barra lateral. O rodapé do `SidebarNav` mostra o usuário; confirme que o clique ali leva ao Perfil.
- O perfil de acesso (Administrador ou Equipe Operacional) é definido em [Gestão de Usuários](gestao-de-usuarios.md) e pode aparecer aqui só como leitura.
