---
icon: lucide/lock
---

# Épico 1 — Portal Institucional & Autenticação

**Objetivo do épico:** garantir a porta de entrada do sistema — a vitrine pública do escritório e o controle de acesso de quem já é usuário cadastrado.

**Perfis envolvidos:** Visitante · Usuário autenticado (qualquer perfil) · Administrador

| ID | História | Perfil |
| --- | --- | --- |
| [US01](#us01) | Landing page institucional | Visitante |
| [US02](#us02) | Login no sistema | Usuário cadastrado |
| [US03](#us03) | Recuperação de senha | Usuário cadastrado |
| [US04](#us04) | Página institucional editável | Administrador |
| [US05](#us05) | Editar dados do próprio perfil | Usuário logado |
| [US06](#us06) | Encerrar sessões em outros dispositivos | Usuário logado |

---

## US01 — Landing page institucional { #us01 }

> **Como** visitante do site do escritório, **eu quero** acessar uma landing page institucional, **para que** eu conheça o escritório e seus serviços antes de decidir contratá-lo.

- **Perfil:** Visitante (não autenticado)
- **Depende de:** —
- **Relaciona-se com:** [US02](#us02) · [US04](#us04)

**Critérios de aceitação**

- **US01-CA01** — Dado que acesso a URL do sistema, quando a página carrega, então vejo a landing page com identidade visual do escritório (logo, cores).
- **US01-CA02** — O layout segue a referência já aprovada pelo cliente.
- **US01-CA03** — A página exibe um ponto de entrada (botão/link) para o Login ([US02](#us02)).

---

## US02 — Login no sistema { #us02 }

> **Como** usuário cadastrado, **eu quero** fazer login com e-mail e senha, **para que** eu acesse o painel do meu perfil.

- **Perfil:** Usuário cadastrado (Administrador, Equipe Operacional ou Cliente)
- **Depende de:** — (o primeiro Administrador é criado na implantação do sistema; os demais usuários entram por convite, na [US07](ep02-usuarios-perfis.md#us07))
- **Relaciona-se com:** [US03](#us03) · [US06](#us06) · [US07](ep02-usuarios-perfis.md#us07) · [US08](ep02-usuarios-perfis.md#us08) · [US09](ep02-usuarios-perfis.md#us09)

**Critérios de aceitação**

- **US02-CA01** — Dado e-mail/senha válidos, quando envio o login, então sou redirecionado ao painel correspondente ao meu perfil.
- **US02-CA02** — Dado e-mail/senha inválidos, então recebo uma mensagem de erro genérica (sem indicar qual campo errou).
- **US02-CA03** — Um usuário inativado não consegue autenticar, mesmo com credenciais corretas (ver [US08](ep02-usuarios-perfis.md#us08)).

---

## US03 — Recuperação de senha { #us03 }

> **Como** usuário cadastrado, **eu quero** solicitar a redefinição da minha senha via e-mail, **para que** eu recupere o acesso caso a esqueça.

- **Perfil:** Usuário cadastrado
- **Depende de:** [US02](#us02)
- **Relaciona-se com:** [US05](#us05) · [US06](#us06)

**Critérios de aceitação**

- **US03-CA01** — Dado um e-mail cadastrado, quando solicito redefinição, então recebo um link de redefinição válido por tempo limitado.
- **US03-CA02** — O link expirado não permite mais redefinir a senha.
- **US03-CA03** — Após redefinir, sessões antigas com a senha anterior deixam de funcionar (ver [US06](#us06)).

---

## US04 — Página institucional editável { #us04 }

> **Como** Administrador, **eu quero** editar os textos e imagens da landing page (sobre o escritório, serviços, contato), **para que** eu não dependa de um desenvolvedor para pequenas atualizações institucionais.

- **Perfil:** Administrador
- **Depende de:** [US01](#us01) · [US02](#us02)
- **Relaciona-se com:** [US09](ep02-usuarios-perfis.md#us09)

**Critérios de aceitação**

- **US04-CA01** — Dado que sou Administrador, quando edito um bloco de texto/imagem, então a alteração é refletida publicamente após salvar.
- **US04-CA02** — Apenas o perfil Administrador tem acesso a essa edição.

---

## US05 — Editar dados do próprio perfil { #us05 }

> **Como** usuário logado, **eu quero** editar meus próprios dados (nome, e-mail, senha), **para que** eu mantenha minhas informações de acesso atualizadas.

- **Perfil:** Usuário logado (qualquer perfil)
- **Depende de:** [US02](#us02)
- **Relaciona-se com:** [US03](#us03) · [US07](ep02-usuarios-perfis.md#us07)

**Critérios de aceitação**

- **US05-CA01** — Dado que estou logado, quando altero meu nome/e-mail/senha e confirmo, então os dados são atualizados sem necessidade de intervenção de um Administrador.
- **US05-CA02** — Alteração de e-mail ou senha exige confirmação da senha atual.

---

## US06 — Encerrar sessões em outros dispositivos { #us06 }

> **Como** usuário logado, **eu quero** poder encerrar sessões ativas em outros dispositivos, **para que** eu tenha mais controle sobre a segurança da minha conta.

- **Perfil:** Usuário logado (qualquer perfil)
- **Depende de:** [US02](#us02)
- **Relaciona-se com:** [US03](#us03) · [US05](#us05)

**Critérios de aceitação**

- **US06-CA01** — Dado que tenho sessões ativas em outros dispositivos, quando escolho encerrá-las, então essas sessões são invalidadas imediatamente.

---

**Navegação:** [Índice das histórias](index.md) · [Épico 2 — Gestão de Usuários →](ep02-usuarios-perfis.md) · [Matriz de rastreabilidade](../rastreabilidade/matriz.md)

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 13/09/2026 | Histórias do EP01 e do EP02 (US01–US11). | Gabriela Tiago de Araújo |
| 1.1 | 10/10/2026 | A US07 passa a depender da US02, e não o contrário. | Gabriela Tiago de Araújo |
| 1.2 | 25/10/2026 | Inclusão do histórico de versão. | Mateus Vieira |
