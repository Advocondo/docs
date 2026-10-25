---
icon: lucide/users
---

# Épico 2 — Gestão de Usuários e Perfis de Acesso

**Objetivo do épico:** dar ao Administrador o controle de quem entra no sistema, com quais permissões e sobre quais dados — com rastreabilidade das mudanças de acesso.

**Perfis envolvidos:** Administrador (executa) · Equipe Operacional e Cliente (afetados)

| ID | História | Perfil |
| --- | --- | --- |
| [US07](#us07) | Convidar novo membro | Administrador |
| [US08](#us08) | Inativar acesso de usuário | Administrador |
| [US09](#us09) | Definir nível de acesso | Administrador |
| [US10](#us10) | Vincular Cliente aos condomínios corretos | Administrador |
| [US11](#us11) | Histórico de ações da Gestão de Usuários | Administrador |

---

## US07 — Convidar novo membro { #us07 }

> **Como** Administrador, **eu quero** convidar um novo colaborador informando e-mail e nível de acesso (Equipe Operacional ou Cliente), **para que** ele acesse o sistema com as permissões corretas.

- **Perfil:** Administrador
- **Depende de:** [US02](ep01-portal-autenticacao.md#us02) (o Administrador precisa estar logado)
- **Relaciona-se com:** [US05](ep01-portal-autenticacao.md#us05) · [US09](#us09) · [US10](#us10) · [US11](#us11) · [US18](ep03-cadastro-acordos.md#us18)

**Critérios de aceitação**

- **US07-CA01** — Dado e-mail + perfil selecionado, quando confirmo o convite, então o usuário é criado como pendente/ativo.
- **US07-CA02** — Só o Administrador vê e acessa esse módulo.
- **US07-CA03** — O sistema não permite cadastrar dois usuários com o mesmo e-mail.
- **US07-CA04** — Ao cadastrar um usuário, é possível marcar se ele é advogado, informando o número da OAB; essa marcação é independente do nível de acesso e alimenta a atribuição de responsável em [US18](ep03-cadastro-acordos.md#us18).

---

## US08 — Inativar acesso de usuário { #us08 }

> **Como** Administrador, **eu quero** inativar o acesso de um usuário, **para que** pessoas que saíram do escritório ou da carteira de clientes não acessem mais o sistema.

- **Perfil:** Administrador
- **Depende de:** [US07](#us07)
- **Relaciona-se com:** [US02](ep01-portal-autenticacao.md#us02) · [US11](#us11)

**Critérios de aceitação**

- **US08-CA01** — Dado um usuário ativo, quando o Administrador clica em "inativar", então o status muda para inativo imediatamente.
- **US08-CA02** — Um usuário inativado não consegue mais logar (ver [US02](ep01-portal-autenticacao.md#us02)).
- **US08-CA03** — A ação é reversível (é possível reativar).

---

## US09 — Definir nível de acesso { #us09 }

> **Como** Administrador, **eu quero** definir ou alterar o perfil de um usuário, **para que** cada pessoa tenha permissões compatíveis com sua função.

- **Perfil:** Administrador
- **Depende de:** [US07](#us07)
- **Relaciona-se com:** [US10](#us10) · [US11](#us11) · [US32](ep05-comissoes-metas.md#us32) · [US33](ep05-comissoes-metas.md#us33) · [US37](ep06-painel-cliente.md#us37)

**Critérios de aceitação**

- **US09-CA01** — Dado um usuário cadastrado, quando altero seu perfil, então as permissões de tela e dados dele são atualizadas de acordo com o novo perfil.
- **US09-CA02** — A alteração de perfil é restrita ao Administrador.

---

## US10 — Vincular Cliente aos condomínios corretos { #us10 }

> **Como** Administrador, **eu quero** associar um usuário do perfil Cliente a um ou mais condomínios específicos, **para que** ele só visualize dados dos condomínios pelos quais é responsável.

- **Perfil:** Administrador
- **Depende de:** [US07](#us07) · [US12](ep03-cadastro-acordos.md#us12)
- **Relaciona-se com:** [US15](ep03-cadastro-acordos.md#us15) · [US24](ep03-cadastro-acordos.md#us24) · [US37](ep06-painel-cliente.md#us37) · [US38](ep06-painel-cliente.md#us38) · [US39](ep06-painel-cliente.md#us39) · [US40](ep06-painel-cliente.md#us40)

**Critérios de aceitação**

- **US10-CA01** — Dado um usuário Cliente, quando vinculo condomínio(s) a ele, então ele só vê acordos desses condomínios no painel (ver [US37](ep06-painel-cliente.md#us37)).
- **US10-CA02** — Um Cliente sem nenhum condomínio vinculado não vê nenhum acordo.

---

## US11 — Histórico de ações da Gestão de Usuários { #us11 }

> **Como** Administrador, **eu quero** ver um histórico de quem convidou, inativou ou alterou o perfil de cada usuário, **para que** eu tenha rastreabilidade sobre mudanças de acesso.

- **Perfil:** Administrador
- **Depende de:** [US07](#us07) · [US08](#us08) · [US09](#us09)
- **Relaciona-se com:** [US31](ep04-parcelas.md#us31) (log equivalente para movimentações financeiras)

**Critérios de aceitação**

- **US11-CA01** — Cada alteração de usuário registra data, autor da ação e o que foi alterado.
- **US11-CA02** — O histórico é visível apenas para o perfil Administrador.

---

**Navegação:** [← Épico 1 — Portal & Autenticação](ep01-portal-autenticacao.md) · [Índice das histórias](index.md) · [Épico 3 — Cadastro de Acordos →](ep03-cadastro-acordos.md) · [Matriz de rastreabilidade](../rastreabilidade/matriz.md)

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 13/09/2026 | Histórias do EP01 e do EP02 (US01–US11). | Gabriela Tiago de Araújo |
| 1.1 | 10/10/2026 | A US07 passa a depender da US02, e não o contrário. | Gabriela Tiago de Araújo |
| 1.2 | 25/10/2026 | Inclusão do histórico de versão. | Mateus Vieira |
