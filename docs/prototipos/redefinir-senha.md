---
icon: lucide/key-round
title: Redefinir Senha
---

# Redefinir Senha

Tela derivada do [Login](login.md), com a mesma composição em duas metades. O formulário troca e-mail e senha por "Nova Senha" e "Confirmar Senha".

| | |
| --- | --- |
| Origem | **Criado no Figma**, duplicando a tela de Login |
| Nó no Figma | [124:2766](https://www.figma.com/design/jEwHxavSrPVQrm3hGSLGtC/edson-alexandre-advogados_design-system?node-id=124-2766) |
| Fonte no repositório | não existe; a base é `ui_kits/plataforma_processos/Login.jsx` |
| Componentes | `Logo`, `FieldLabel`, `Input type="password"`, `Button` |
| Histórias de usuário | [US03](../historias/ep01-portal-autenticacao.md#us03) (recuperação de senha), só o passo final: faltam a solicitação por e-mail, o link expirado e a confirmação. Ver a [cobertura das histórias](cobertura-historias.md). |

## O que a tela mostra

- Título "Redefinir Senha".
- Campos "Nova Senha" (obrigatório) e "Confirmar Senha".
- O mesmo rodapé de suporte do Login: "Dúvidas de acesso: (61) 3021-8539 · seg a sex, 09h às 17h".

## Captura

!!! info "Captura pendente"

    Este frame foi criado no Figma e ainda não tem captura exportada. Abra o [nó 124:2766](https://www.figma.com/design/jEwHxavSrPVQrm3hGSLGtC/edson-alexandre-advogados_design-system?node-id=124-2766) ou exporte o frame em PNG a 1x como `assets/prototipos/redefinir-senha.png`.

## Pontos de atenção

- Falta o passo anterior do fluxo: a tela que pede o e-mail e envia o link de redefinição. Sem ela, "Esqueci minha senha" no Login não tem destino.
- Defina os critérios de senha (tamanho mínimo, caracteres) e mostre-os como `hint` do `FieldLabel`, além do estado de erro quando as duas senhas não coincidem.
- Preveja o estado de link expirado e a confirmação de sucesso (um `Alert tone="ok"` ou redirecionamento ao Login com `Toast`).
