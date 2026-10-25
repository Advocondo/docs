---
icon: lucide/file-text
---

# Épico 3 — Cadastro de Acordos

**Objetivo do épico:** registrar no sistema toda a estrutura de um acordo extrajudicial — condomínio, devedor, valores, honorários, parcelamento, responsável e documentação — para que ele possa ser acompanhado mês a mês.

**Perfis envolvidos:** Equipe Operacional (executa a maior parte) · Administrador (atribuição e contratos)

| ID | História | Perfil |
| --- | --- | --- |
| [US12](#us12) | Cadastrar condomínio | Equipe Operacional |
| [US13](#us13) | Cadastrar devedor | Equipe Operacional |
| [US14](#us14) | Importar lista de inadimplentes em lote | Equipe Operacional |
| [US15](#us15) | Cadastrar novo acordo | Equipe Operacional |
| [US16](#us16) | Definir honorários do acordo | Equipe Operacional |
| [US17](#us17) | Fracionar dívida em parcelas | Equipe Operacional |
| [US18](#us18) | Atribuir acordo a um advogado responsável | Administrador / Equipe Operacional |
| [US19](#us19) | Editar acordo já cadastrado | Equipe Operacional |
| [US20](#us20) | Cancelar/encerrar acordo | Equipe Operacional |
| [US21](#us21) | Anexar documentos ao acordo | Equipe Operacional |
| [US22](#us22) | Buscar/filtrar acordos | Equipe Operacional |
| [US23](#us23) | Acompanhar renovação de contrato | Administrador |
| [US24](#us24) | Gerar e salvar PDF do acordo | Equipe Operacional |

---

## US12 — Cadastrar condomínio { #us12 }

> **Como** membro da Equipe Operacional, **eu quero** cadastrar um novo condomínio (nome, endereço, síndico/administradora responsável), **para que** ele fique disponível para vincular a novos acordos e usuários Cliente.

- **Perfil:** Equipe Operacional
- **Depende de:** —
- **Relaciona-se com:** [US10](ep02-usuarios-perfis.md#us10) · [US15](#us15) · [US22](#us22) · [US23](#us23)

**Critérios de aceitação**

- **US12-CA01** — Não é possível cadastrar um acordo sem selecionar um condomínio já cadastrado (ver [US15](#us15)).
- **US12-CA02** — Um condomínio pode ser editado depois (ex.: troca de administradora).

---

## US13 — Cadastrar devedor { #us13 }

> **Como** membro da Equipe Operacional, **eu quero** cadastrar os dados do devedor (nome, unidade, contato), **para que** eu não precise redigitar essa informação a cada novo acordo com o mesmo morador.

- **Perfil:** Equipe Operacional
- **Depende de:** [US12](#us12)
- **Relaciona-se com:** [US14](#us14) · [US15](#us15) · [US22](#us22) · [US38](ep06-painel-cliente.md#us38)

**Critérios de aceitação**

- **US13-CA01** — O sistema alerta se já existe devedor com dados similares cadastrado, evitando duplicidade.

---

## US14 — Importar lista de inadimplentes em lote { #us14 }

> **Como** membro da Equipe Operacional, **eu quero** importar uma planilha com a lista de moradores inadimplentes recebida do condomínio, **para que** eu não precise cadastrar um por um manualmente.

- **Perfil:** Equipe Operacional
- **Depende de:** [US12](#us12) · [US13](#us13)
- **Relaciona-se com:** [US15](#us15)

**Critérios de aceitação**

- **US14-CA01** — Dado um arquivo no formato aceito, quando faço o upload, então o sistema valida e aponta linhas com erro antes de confirmar a importação.
- **US14-CA02** — Registros importados com sucesso ficam disponíveis para vincular a novos acordos.

---

## US15 — Cadastrar novo acordo { #us15 }

> **Como** membro da Equipe Operacional, **eu quero** cadastrar um acordo informando devedor, condomínio, valor total da dívida e responsável, **para que** o acordo seja controlado no sistema.

- **Perfil:** Equipe Operacional
- **Depende de:** [US12](#us12) · [US13](#us13)
- **Relaciona-se com:** [US16](#us16) · [US17](#us17) · [US18](#us18) · [US19](#us19) · [US20](#us20) · [US21](#us21) · [US22](#us22) · [US24](#us24) · [US37](ep06-painel-cliente.md#us37)

**Critérios de aceitação**

- **US15-CA01** — Dado os dados obrigatórios preenchidos, quando salvo o cadastro, então o acordo aparece na lista de acordos ativos.
- **US15-CA02** — O sistema não permite salvar sem os campos obrigatórios.
- **US15-CA03** — O acordo fica vinculado ao condomínio, para que o Cliente correspondente consiga visualizá-lo (ver [US10](ep02-usuarios-perfis.md#us10) e [US37](ep06-painel-cliente.md#us37)).

---

## US16 — Definir honorários do acordo { #us16 }

> **Como** membro da Equipe Operacional, **eu quero** definir a fatia de honorários advocatícios do acordo, **para que** o sistema separe automaticamente o valor do condomínio e o valor do escritório em cada parcela.

- **Perfil:** Equipe Operacional
- **Depende de:** [US15](#us15)
- **Relaciona-se com:** [US17](#us17) · [US26](ep04-parcelas.md#us26) · [US33](ep05-comissoes-metas.md#us33) · [US37](ep06-painel-cliente.md#us37) · [US38](ep06-painel-cliente.md#us38) · [US39](ep06-painel-cliente.md#us39)

**Critérios de aceitação**

- **US16-CA01** — Dado um acordo com valor total definido, quando informo o percentual/valor de honorários, então o sistema calcula e exibe separadamente "valor do condomínio" e "valor de honorários" por parcela.
- **US16-CA02** — A soma de (valor do condomínio + honorários) de cada parcela é igual ao valor total daquela parcela.

!!! warning "Restrição de visibilidade"
    Valores de honorários não são exibidos ao perfil Cliente — ver [US37](ep06-painel-cliente.md#us37), [US38](ep06-painel-cliente.md#us38) e [US39](ep06-painel-cliente.md#us39).

---

## US17 — Fracionar dívida em parcelas { #us17 }

> **Como** membro da Equipe Operacional, **eu quero** definir número de parcelas e vencimentos, **para que** o parcelamento negociado com o devedor fique refletido no sistema.

- **Perfil:** Equipe Operacional
- **Depende de:** [US15](#us15)
- **Relaciona-se com:** [US16](#us16) · [US20](#us20) · [US25](ep04-parcelas.md#us25) · [US26](ep04-parcelas.md#us26) · [US27](ep04-parcelas.md#us27)

**Critérios de aceitação**

- **US17-CA01** — Dado um acordo cadastrado, quando informo o número de parcelas, então o sistema gera automaticamente as faturas mensais com valor e vencimento de cada uma.
- **US17-CA02** — A soma das parcelas geradas é igual ao valor total do acordo.
- **US17-CA03** — É possível editar manualmente valor/data de uma parcela específica antes da baixa (ver [US26](ep04-parcelas.md#us26)).

---

## US18 — Atribuir acordo a um advogado responsável { #us18 }

> **Como** Administrador ou membro da Equipe Operacional, **eu quero** atribuir um acordo a um advogado cadastrado no sistema, **para que** fique claro quem responde juridicamente por aquele caso.

- **Perfil:** Administrador · Equipe Operacional
- **Depende de:** [US07](ep02-usuarios-perfis.md#us07) (marcação de advogado/OAB) · [US15](#us15)
- **Relaciona-se com:** [US09](ep02-usuarios-perfis.md#us09) · [US22](#us22) · [US25](ep04-parcelas.md#us25) · [US26](ep04-parcelas.md#us26) · [US30](ep04-parcelas.md#us30)

**Critérios de aceitação**

- **US18-CA01** — Dado um acordo cadastrado, quando escolho um responsável, então a lista de seleção mostra apenas usuários marcados como advogado (com OAB) no cadastro (ver [US07](ep02-usuarios-perfis.md#us07)).
- **US18-CA02** — É possível reatribuir o acordo a outro advogado posteriormente, mantendo o histórico de reatribuições (quem era antes, quem passou a ser, e quando).
- **US18-CA03** — O advogado atribuído consegue visualizar os acordos sob sua responsabilidade, conforme o nível de acesso definido para o seu perfil (ver [US09](ep02-usuarios-perfis.md#us09)).

---

## US19 — Editar acordo já cadastrado { #us19 }

> **Como** membro da Equipe Operacional, **eu quero** editar dados de um acordo (ex.: dados do devedor, valor renegociado), **para que** eu corrija informações incorretas ou reflita uma renegociação.

- **Perfil:** Equipe Operacional
- **Depende de:** [US15](#us15)
- **Relaciona-se com:** [US17](#us17) · [US26](ep04-parcelas.md#us26) · [US31](ep04-parcelas.md#us31)

**Critérios de aceitação**

- **US19-CA01** — Alterações em acordos com parcelas já pagas exigem confirmação extra, para evitar edição acidental de histórico financeiro.
- **US19-CA02** — O sistema mantém registro de quem editou e quando (ver [US31](ep04-parcelas.md#us31)).

---

## US20 — Cancelar/encerrar acordo { #us20 }

> **Como** membro da Equipe Operacional, **eu quero** marcar um acordo como cancelado ou quebrado, **para que** ele saia da lista de acordos ativos sem perder o histórico.

- **Perfil:** Equipe Operacional
- **Depende de:** [US15](#us15) · [US17](#us17)
- **Relaciona-se com:** [US21](#us21) · [US22](#us22) · [US25](ep04-parcelas.md#us25)

**Critérios de aceitação**

- **US20-CA01** — Um acordo cancelado não gera novas parcelas futuras.
- **US20-CA02** — O histórico de parcelas já pagas permanece consultável.

---

## US21 — Anexar documentos ao acordo { #us21 }

> **Como** membro da Equipe Operacional, **eu quero** anexar documentos (ex.: termo de acordo assinado, comprovantes) ao cadastro do acordo, **para que** toda a documentação fique centralizada no sistema.

- **Perfil:** Equipe Operacional
- **Depende de:** [US15](#us15)
- **Relaciona-se com:** [US20](#us20) · [US24](#us24)

**Critérios de aceitação**

- **US21-CA01** — É possível fazer upload e download dos arquivos anexados a um acordo específico.
- **US21-CA02** — Documentos anexados ficam vinculados permanentemente ao acordo, mesmo se ele for cancelado (ver [US20](#us20)).

---

## US22 — Buscar/filtrar acordos { #us22 }

> **Como** membro da Equipe Operacional, **eu quero** buscar acordos por nome do devedor, condomínio ou responsável, **para que** eu encontre rapidamente um acordo específico.

- **Perfil:** Equipe Operacional
- **Depende de:** [US15](#us15)
- **Relaciona-se com:** [US12](#us12) · [US13](#us13) · [US18](#us18) · [US25](ep04-parcelas.md#us25)

**Critérios de aceitação**

- **US22-CA01** — A busca retorna resultados parciais (ex.: parte do nome do devedor).
- **US22-CA02** — Filtros são combináveis (ex.: condomínio + status).

---

## US23 — Acompanhar renovação de contrato { #us23 }

> **Como** Administrador, **eu quero** acompanhar a data de renovação do contrato de prestação de serviço com cada condomínio, **para que** eu não perca o prazo de renegociação/renovação.

- **Perfil:** Administrador
- **Depende de:** [US12](#us12)
- **Relaciona-se com:** [US34](ep05-comissoes-metas.md#us34)

**Critérios de aceitação**

- **US23-CA01** — Dado um condomínio com data de renovação cadastrada, quando o prazo se aproxima, então o sistema sinaliza visualmente esse condomínio como "próximo da renovação".
- **US23-CA02** — É possível registrar quando o contrato foi renovado, atualizando a próxima data de referência.

---

## US24 — Gerar e salvar PDF do acordo { #us24 }

> **Como** membro da Equipe Operacional, **eu quero** gerar um PDF com os dados do acordo (devedor, condomínio, valores, parcelas) e salvá-lo no sistema com um link de acesso, **para que** eu possa compartilhar ou consultar o documento sem recriar a informação manualmente.

- **Perfil:** Equipe Operacional
- **Depende de:** [US15](#us15) · [US17](#us17)
- **Relaciona-se com:** [US10](ep02-usuarios-perfis.md#us10) · [US21](#us21) · [US39](ep06-painel-cliente.md#us39) · [US40](ep06-painel-cliente.md#us40)

**Critérios de aceitação**

- **US24-CA01** — Dado um acordo cadastrado, quando gero o PDF, então o sistema cria o arquivo com os dados principais do acordo formatados.
- **US24-CA02** — O PDF gerado fica disponível tanto para download direto quanto por um link de acesso.
- **US24-CA03** — O link respeita as mesmas permissões de acesso do acordo (ex.: um Cliente só acessa PDFs de acordos do seu próprio condomínio — ver [US10](ep02-usuarios-perfis.md#us10)).

!!! note "Componente reutilizado"
    A geração de PDF desta história é a base do relatório simplificado do Cliente ([US39](ep06-painel-cliente.md#us39)) e do link enviado por e-mail ([US40](ep06-painel-cliente.md#us40)).

---

**Navegação:** [← Épico 2 — Gestão de Usuários](ep02-usuarios-perfis.md) · [Índice das histórias](index.md) · [Épico 4 — Acompanhamento de Parcelas →](ep04-parcelas.md) · [Matriz de rastreabilidade](../rastreabilidade/matriz.md)

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 13/09/2026 | Histórias do EP03 (US12–US24). | Gabriela Tiago de Araújo |
| 1.1 | 25/10/2026 | Inclusão do histórico de versão. | Mateus Vieira |
