---
icon: lucide/building
---

# Épico 6 — Painel do Cliente

**Objetivo do épico:** dar ao síndico/administradora autonomia para acompanhar os acordos do seu condomínio — com informação suficiente para prestar contas em assembleia e sem expor dados internos do escritório.

**Perfis envolvidos:** Cliente (síndico/administradora)

| ID | História | Perfil |
| --- | --- | --- |
| [US37](#us37) | Consultar status dos acordos do condomínio | Cliente |
| [US38](#us38) | Histórico de pagamentos de um morador | Cliente |
| [US39](#us39) | Baixar relatório simplificado | Cliente |
| [US40](#us40) | Notificação automática por e-mail ao Cliente | Cliente |

!!! danger "Regra de confidencialidade do épico"
    Nenhuma tela ou arquivo deste épico expõe honorários ([US16](ep03-cadastro-acordos.md#us16)), comissões ([US32](ep05-comissoes-metas.md#us32), [US33](ep05-comissoes-metas.md#us33)) ou dados de condomínios não vinculados ao usuário ([US10](ep02-usuarios-perfis.md#us10)).

---

## US37 — Consultar status dos acordos do condomínio { #us37 }

> **Como** Cliente (síndico/administradora), **eu quero** ver um painel simplificado com o andamento dos acordos do meu condomínio, **para que** eu acompanhe quem está em dia ou atrasado sem pedir informação ao escritório.

- **Perfil:** Cliente
- **Depende de:** [US10](ep02-usuarios-perfis.md#us10) · [US15](ep03-cadastro-acordos.md#us15)
- **Relaciona-se com:** [US27](ep04-parcelas.md#us27) · [US16](ep03-cadastro-acordos.md#us16) · [US38](#us38)

**Critérios de aceitação**

- **US37-CA01** — Vejo apenas acordos vinculados ao meu condomínio (ver [US10](ep02-usuarios-perfis.md#us10)).
- **US37-CA02** — Status simplificado (ex.: "Em dia"/"Atrasado"), sem valores de honorários ou comissões.

---

## US38 — Histórico de pagamentos de um morador { #us38 }

> **Como** Cliente, **eu quero** ver o histórico de parcelas pagas/atrasadas de um morador específico do meu condomínio, **para que** eu tenha mais detalhe do que apenas o status atual, se precisar prestar contas na assembleia.

- **Perfil:** Cliente
- **Depende de:** [US37](#us37) · [US26](ep04-parcelas.md#us26)
- **Relaciona-se com:** [US13](ep03-cadastro-acordos.md#us13) · [US28](ep04-parcelas.md#us28) · [US39](#us39)

**Critérios de aceitação**

- **US38-CA01** — O histórico mostra apenas valor total pago/em aberto por competência, sem detalhar honorários do escritório (ver [US16](ep03-cadastro-acordos.md#us16)).

---

## US39 — Baixar relatório simplificado { #us39 }

> **Como** Cliente, **eu quero** baixar em PDF um relatório simplificado do andamento dos acordos do meu condomínio, **para que** eu possa apresentá-lo em assembleia de condomínio.

- **Perfil:** Cliente
- **Depende de:** [US24](ep03-cadastro-acordos.md#us24) · [US37](#us37)
- **Relaciona-se com:** [US38](#us38) · [US40](#us40) · [US35](ep05-comissoes-metas.md#us35)

**Critérios de aceitação**

- **US39-CA01** — O relatório é gerado como um PDF (ver [US24](ep03-cadastro-acordos.md#us24)), disponível para download direto.
- **US39-CA02** — O relatório não expõe dados sensíveis do escritório (honorários, comissões, dados de outros condomínios).

---

## US40 — Notificação automática por e-mail ao Cliente { #us40 }

> **Como** Cliente (síndico/administradora), **eu quero** receber automaticamente um e-mail do sistema quando houver uma atualização relevante no andamento dos acordos do meu condomínio, **para que** eu seja informado sem precisar entrar no painel o tempo todo.

- **Perfil:** Cliente
- **Depende de:** [US10](ep02-usuarios-perfis.md#us10) · [US37](#us37)
- **Relaciona-se com:** [US24](ep03-cadastro-acordos.md#us24) · [US39](#us39) · [US30](ep04-parcelas.md#us30) (equivalente interno)

**Critérios de aceitação**

- **US40-CA01** — Dado que ocorre um evento relevante (ex.: fechamento do relatório mensal, mudança de status de um acordo), quando isso acontece, então o sistema dispara automaticamente um e-mail para o endereço do Cliente vinculado àquele condomínio, sem exigir ação manual de ninguém do escritório.
- **US40-CA02** — O e-mail tem caráter informativo (aviso/atualização geral), podendo conter um link de acesso ao relatório/PDF gerado (ver [US24](ep03-cadastro-acordos.md#us24)).
- **US40-CA03** — O sistema registra a data de cada envio automático, para referência futura.

---

**Navegação:** [← Épico 5 — Comissões e Metas](ep05-comissoes-metas.md) · [Índice das histórias](index.md) · [Matriz de rastreabilidade](../rastreabilidade/matriz.md)

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 13/09/2026 | Histórias do EP04, do EP05 e do EP06 (US25–US40). | Gabriela Tiago de Araújo |
| 1.1 | 25/10/2026 | Inclusão do histórico de versão. | Mateus Vieira |
