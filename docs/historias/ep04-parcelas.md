---
icon: lucide/calendar
---

# Épico 4 — Acompanhamento Mensal de Parcelas

**Objetivo do épico:** transformar o acordo cadastrado em rotina mensal — conferir o que vence, dar baixa, sinalizar atraso, registrar nota fiscal e manter rastro de toda movimentação financeira.

**Perfis envolvidos:** Equipe Operacional (operação diária) · Administrador (notificação e auditoria)

| ID | História | Perfil |
| --- | --- | --- |
| [US25](#us25) | Listar faturas do mês | Equipe Operacional |
| [US26](#us26) | Dar baixa em parcela paga | Equipe Operacional |
| [US27](#us27) | Sinalizar parcela em atraso | Sistema (automático) |
| [US28](#us28) | Registrar pagamento parcial | Equipe Operacional |
| [US29](#us29) | Registrar emissão de nota fiscal | Equipe Operacional |
| [US30](#us30) | Notificação interna de parcela em atraso | Administrador / responsável |
| [US31](#us31) | Log de alterações financeiras sensíveis | Administrador |

---

## US25 — Listar faturas do mês { #us25 }

> **Como** membro da Equipe Operacional, **eu quero** ver as faturas com vencimento no mês corrente, **para que** eu saiba o que preciso conferir e dar baixa.

- **Perfil:** Equipe Operacional
- **Depende de:** [US17](ep03-cadastro-acordos.md#us17)
- **Relaciona-se com:** [US22](ep03-cadastro-acordos.md#us22) · [US26](#us26) · [US27](#us27) · [US35](ep05-comissoes-metas.md#us35)

**Critérios de aceitação**

- **US25-CA01** — A lista mostra devedor, condomínio, valor e status (ex.: "Em aberto", "Pago", "Atrasado").
- **US25-CA02** — É possível filtrar por condomínio, responsável pelo acordo ou status.

---

## US26 — Dar baixa em parcela paga { #us26 }

> **Como** membro da Equipe Operacional, **eu quero** marcar uma parcela como paga, **para que** o status do acordo se atualize e a comissão do responsável seja calculada automaticamente.

- **Perfil:** Equipe Operacional
- **Depende de:** [US17](ep03-cadastro-acordos.md#us17) · [US25](#us25)
- **Relaciona-se com:** [US16](ep03-cadastro-acordos.md#us16) · [US28](#us28) · [US29](#us29) · [US31](#us31) · [US32](ep05-comissoes-metas.md#us32) · [US36](ep05-comissoes-metas.md#us36) · [US38](ep06-painel-cliente.md#us38)

**Critérios de aceitação**

- **US26-CA01** — Dado uma parcela em aberto, quando marco como "paga" e informo a data de pagamento, então o status muda para "Pago" e a comissão do responsável é atualizada automaticamente (ver [US32](ep05-comissoes-metas.md#us32)).
- **US26-CA02** — Uma parcela já baixada só pode ser corrigida/estornada por quem tem permissão para isso (ver [US09](ep02-usuarios-perfis.md#us09) e [US31](#us31)).

---

## US27 — Sinalizar parcela em atraso { #us27 }

> **Como** membro da Equipe Operacional, **eu quero** que o sistema marque automaticamente parcelas vencidas sem baixa como "Atrasado", **para que** eu identifique rapidamente inadimplências dentro do próprio acordo.

- **Perfil:** Sistema (cálculo automático), consumido por Equipe Operacional, Administrador e Cliente
- **Depende de:** [US17](ep03-cadastro-acordos.md#us17)
- **Relaciona-se com:** [US25](#us25) · [US30](#us30) · [US34](ep05-comissoes-metas.md#us34) · [US37](ep06-painel-cliente.md#us37)

**Critérios de aceitação**

- **US27-CA01** — O status "Atrasado" é calculado automaticamente pelo sistema, sem ação manual, assim que a data de vencimento passa sem baixa.

---

## US28 — Registrar pagamento parcial { #us28 }

> **Como** membro da Equipe Operacional, **eu quero** registrar que uma parcela foi paga parcialmente, **para que** o sistema reflita corretamente valores em aberto.

- **Perfil:** Equipe Operacional
- **Depende de:** [US26](#us26)
- **Relaciona-se com:** [US25](#us25) · [US31](#us31) · [US38](ep06-painel-cliente.md#us38)

**Critérios de aceitação**

- **US28-CA01** — Dado um valor parcial informado, quando registro o pagamento, então o sistema mantém o saldo restante da parcela como "Em aberto" (ou status equivalente), sem marcá-la como totalmente paga.
- **US28-CA02** — O histórico da parcela mostra os valores pagos em cada registro parcial.

---

## US29 — Registrar emissão de nota fiscal { #us29 }

> **Como** membro da Equipe Operacional, **eu quero** registrar a emissão da nota fiscal vinculada a uma parcela paga, **para que** o controle contábil de emissão de notas fique integrado ao sistema.

- **Perfil:** Equipe Operacional
- **Depende de:** [US26](#us26)
- **Relaciona-se com:** [US35](ep05-comissoes-metas.md#us35)

**Critérios de aceitação**

- **US29-CA01** — Dado uma parcela marcada como paga, quando registro os dados da nota fiscal emitida (número, data), então essa informação fica vinculada à parcela.
- **US29-CA02** — É possível consultar quais parcelas pagas ainda não têm nota fiscal registrada.

---

## US30 — Notificação interna de parcela em atraso { #us30 }

> **Como** Administrador, **eu quero** ser notificado internamente (ex.: ícone de sino) quando uma parcela ficar em atraso, **para que** a equipe seja avisada sem depender de e-mail/WhatsApp automático.

- **Perfil:** Administrador e usuário responsável pelo acordo
- **Depende de:** [US27](#us27) · [US18](ep03-cadastro-acordos.md#us18)
- **Relaciona-se com:** [US25](#us25) · [US40](ep06-painel-cliente.md#us40)

**Critérios de aceitação**

- **US30-CA01** — Dado que uma parcela muda para status "Atrasado", quando isso ocorre, então uma notificação aparece no ícone de sino do usuário responsável e do Administrador.
- **US30-CA02** — Ao clicar na notificação, o usuário é levado direto para a parcela/acordo correspondente.

!!! info "Notificação interna × notificação externa"
    Esta história cobre apenas o aviso **dentro do sistema**. O envio automático de e-mail ao Cliente é tratado em [US40](ep06-painel-cliente.md#us40).

---

## US31 — Log de alterações financeiras sensíveis { #us31 }

> **Como** Administrador, **eu quero** visualizar um log de quem deu baixa, editou ou estornou uma parcela, **para que** eu tenha rastreabilidade sobre movimentações financeiras do escritório.

- **Perfil:** Administrador
- **Depende de:** [US26](#us26)
- **Relaciona-se com:** [US19](ep03-cadastro-acordos.md#us19) · [US28](#us28) · [US11](ep02-usuarios-perfis.md#us11) (log equivalente para acessos)

**Critérios de aceitação**

- **US31-CA01** — Cada baixa/edição/estorno registra usuário responsável, data/hora e valor alterado.
- **US31-CA02** — O log é visível apenas para o perfil Administrador.

---

**Navegação:** [← Épico 3 — Cadastro de Acordos](ep03-cadastro-acordos.md) · [Índice das histórias](index.md) · [Épico 5 — Comissões e Metas →](ep05-comissoes-metas.md) · [Matriz de rastreabilidade](../rastreabilidade/matriz.md)

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 13/09/2026 | Histórias do EP04, do EP05 e do EP06 (US25–US40). | Gabriela Tiago de Araújo |
| 1.1 | 25/10/2026 | Inclusão do histórico de versão. | Mateus Vieira |
