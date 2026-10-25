---
icon: lucide/trending-up
---

# Épico 5 — Comissões e Metas da Equipe

**Objetivo do épico:** dar visão financeira segmentada por perfil — cada colaborador vê o próprio desempenho; o Administrador vê a operação inteira, com indicadores e exportação.

**Perfis envolvidos:** Equipe Operacional (visão individual) · Administrador (visão global)

| ID | História | Perfil |
| --- | --- | --- |
| [US32](#us32) | Visualizar minhas metas e comissões | Equipe Operacional |
| [US33](#us33) | Visão global de faturamento e comissões | Administrador |
| [US34](#us34) | Dashboard de indicadores | Administrador |
| [US35](#us35) | Exportar relatório de acompanhamento | Administrador |
| [US36](#us36) | Definir metas por colaborador | Administrador |

!!! warning "Regra de visibilidade do épico"
    A segregação de dados financeiros entre perfis é transversal a todo o épico: [US32](#us32) e [US33](#us33) são as duas faces da mesma regra, aplicada a partir do nível de acesso definido em [US09](ep02-usuarios-perfis.md#us09).

---

## US32 — Visualizar minhas metas e comissões { #us32 }

> **Como** membro da Equipe Operacional, **eu quero** visualizar minhas próprias metas e o total de comissões acumuladas, **para que** eu acompanhe meu desempenho sem ter acesso aos ganhos dos colegas ou ao faturamento total do escritório.

- **Perfil:** Equipe Operacional
- **Depende de:** [US26](ep04-parcelas.md#us26) · [US36](#us36)
- **Relaciona-se com:** [US09](ep02-usuarios-perfis.md#us09) · [US33](#us33)

**Critérios de aceitação**

- **US32-CA01** — Dado que sou membro da Equipe Operacional, quando acesso o painel financeiro, então vejo apenas minhas próprias comissões e metas.
- **US32-CA02** — O sistema não exibe, para esse perfil, faturamento total do escritório nem comissões de outros colaboradores.

---

## US33 — Visão global de faturamento e comissões { #us33 }

> **Como** Administrador, **eu quero** visualizar o faturamento total do escritório e as comissões de toda a equipe, **para que** eu tenha controle financeiro completo da operação de recuperação de crédito.

- **Perfil:** Administrador
- **Depende de:** [US16](ep03-cadastro-acordos.md#us16) · [US26](ep04-parcelas.md#us26)
- **Relaciona-se com:** [US32](#us32) · [US34](#us34) · [US35](#us35)

**Critérios de aceitação**

- **US33-CA01** — Dado que sou Administrador, quando acesso o painel financeiro, então vejo o faturamento consolidado de todos os acordos e as comissões individuais de cada membro da equipe.
- **US33-CA02** — Esses dados não ficam visíveis para os perfis Equipe Operacional ou Cliente (ver [US32](#us32) e [US37](ep06-painel-cliente.md#us37)).

---

## US34 — Dashboard de indicadores { #us34 }

> **Como** Administrador, **eu quero** ver um painel com indicadores gerais (total de acordos ativos, inadimplência do mês, comissões pagas no período), **para que** eu tenha uma visão rápida da saúde da operação sem abrir relatório por relatório.

- **Perfil:** Administrador
- **Depende de:** [US15](ep03-cadastro-acordos.md#us15) · [US27](ep04-parcelas.md#us27) · [US33](#us33)
- **Relaciona-se com:** [US23](ep03-cadastro-acordos.md#us23) · [US35](#us35)

**Critérios de aceitação**

- **US34-CA01** — O dashboard atualiza os indicadores com base nos dados mais recentes de acordos e parcelas.
- **US34-CA02** — Indicadores são filtráveis por período (ex.: mês/ano).

---

## US35 — Exportar relatório de acompanhamento { #us35 }

> **Como** Administrador, **eu quero** exportar os dados de acompanhamento mensal (ex.: Excel/CSV), **para que** eu possa usar essas informações em reuniões ou repassar à contabilidade.

- **Perfil:** Administrador
- **Depende de:** [US25](ep04-parcelas.md#us25)
- **Relaciona-se com:** [US29](ep04-parcelas.md#us29) · [US34](#us34) · [US39](ep06-painel-cliente.md#us39) (equivalente simplificado para o Cliente)

**Critérios de aceitação**

- **US35-CA01** — A exportação reflete os mesmos filtros aplicados na tela (condomínio, período, status).
- **US35-CA02** — O arquivo exportado abre corretamente em Excel, sem perda de formatação de valores.

---

## US36 — Definir metas por colaborador { #us36 }

> **Como** Administrador, **eu quero** definir metas mensais/individuais para cada membro da Equipe Operacional, **para que** o sistema calcule automaticamente o percentual de atingimento de cada um.

- **Perfil:** Administrador
- **Depende de:** [US07](ep02-usuarios-perfis.md#us07) · [US26](ep04-parcelas.md#us26)
- **Relaciona-se com:** [US32](#us32) · [US33](#us33)

**Critérios de aceitação**

- **US36-CA01** — Dado uma meta definida para um colaborador, quando ele fecha acordos/recebe comissões no período, então o sistema calcula automaticamente o percentual de atingimento da meta.
- **US36-CA02** — Cada colaborador só vê a própria meta e o próprio percentual de atingimento (ver [US32](#us32)).

---

**Navegação:** [← Épico 4 — Acompanhamento de Parcelas](ep04-parcelas.md) · [Índice das histórias](index.md) · [Épico 6 — Painel do Cliente →](ep06-painel-cliente.md) · [Matriz de rastreabilidade](../rastreabilidade/matriz.md)

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 13/09/2026 | Histórias do EP04, do EP05 e do EP06 (US25–US40). | Gabriela Tiago de Araújo |
| 1.1 | 25/10/2026 | Inclusão do histórico de versão. | Mateus Vieira |
