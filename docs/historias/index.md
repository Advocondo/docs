---
icon: lucide/list
---

# Histórias de usuário

As histórias abaixo foram levantadas e validadas em reuniões com o cliente e representam o escopo funcional acordado para o sistema. Cada história é uma unidade de valor entregável, com critérios de aceitação próprios, e é referenciada por um identificador estável ao longo de toda a documentação, do backlog e dos testes.

---

## Convenções { #convencoes }

### Identificação

| Elemento | Formato | Exemplo | Regra |
| --- | --- | --- | --- |
| História | `US` + número sequencial | `US15` | Estável: nunca é renumerada, mesmo que a história mude de épico ou seja removida |
| Critério de aceitação | `US` + número + `-CA` + número | `US15-CA03` | Estável dentro da história; novos critérios entram no fim da lista |
| Épico | `EP` + número | `EP03` | Corresponde a um arquivo `.md` desta seção |

Identificadores removidos **não são reaproveitados**. Se `US14` for descartada, o número 14 permanece vago.

### Formato da história

Toda história segue o padrão **Connextra**:

> **Como** *&lt;perfil&gt;*, **eu quero** *&lt;ação&gt;*, **para que** *&lt;benefício&gt;*.

Os critérios de aceitação usam **Dado / Quando / Então** sempre que descrevem um comportamento observável; regras invariantes (restrições, permissões, validações) são escritas em forma afirmativa direta.

### Campos de rastreabilidade

Cada história declara dois campos de relacionamento, com significados diferentes:

- **Depende de** — histórias que precisam estar implementadas para que esta funcione. Define ordem de implementação.
- **Relaciona-se com** — histórias afetadas pela mesma regra de negócio ou que consomem/alimentam esta, sem bloqueá-la. Define impacto de mudança.

Os dois campos são consolidados na [matriz de rastreabilidade](../rastreabilidade/matriz.md), que também mostra o caminho inverso (quem referencia cada história).

### Links diretos

Cada história tem uma âncora própria e estável. Para referenciar uma história de qualquer lugar da documentação:

``` markdown
[US15](ep03-cadastro-acordos.md#us15)
```

Na navegação do site, o link resolve para `.../historias/ep03-cadastro-acordos/#us15`, apontando direto para a história — use esse endereço em issues, pull requests e commits.

### Como adicionar uma nova história

1. Escolha o épico ao qual ela pertence e abra o `.md` correspondente.
2. Use o próximo número livre da sequência global (não o próximo do épico).
3. Copie o bloco de uma história existente como modelo: título com âncora, citação Connextra, os três campos de rastreabilidade e os critérios numerados.
4. Preencha **Depende de** e **Relaciona-se com** e acrescente o link recíproco nas histórias citadas.
5. Inclua a história na tabela de resumo no topo do épico e na [matriz de rastreabilidade](../rastreabilidade/matriz.md).

---

## Épicos

| # | Épico | Histórias | Objetivo |
| --- | --- | --- | --- |
| EP01 | [Portal Institucional & Autenticação](ep01-portal-autenticacao.md) | US01–US06 | Vitrine pública e controle de acesso |
| EP02 | [Gestão de Usuários e Perfis](ep02-usuarios-perfis.md) | US07–US11 | Quem entra no sistema e com quais permissões |
| EP03 | [Cadastro de Acordos](ep03-cadastro-acordos.md) | US12–US24 | Estrutura do acordo: valores, honorários, parcelas, responsável |
| EP04 | [Acompanhamento de Parcelas](ep04-parcelas.md) | US25–US31 | Rotina mensal de baixa, atraso e auditoria |
| EP05 | [Comissões e Metas](ep05-comissoes-metas.md) | US32–US36 | Desempenho da equipe e visão financeira segmentada |
| EP06 | [Painel do Cliente](ep06-painel-cliente.md) | US37–US40 | Autonomia do síndico/administradora |

---

## Índice completo das histórias { #indice }

As 40 histórias em ordem de identificador. A coluna **CA** indica quantos critérios de aceitação a história possui.

| ID | História | Épico | Perfil | CA |
| --- | --- | --- | --- | --- |
| [US01](ep01-portal-autenticacao.md#us01) | Landing page institucional | [EP01](ep01-portal-autenticacao.md) | Visitante | 3 |
| [US02](ep01-portal-autenticacao.md#us02) | Login no sistema | [EP01](ep01-portal-autenticacao.md) | Usuário cadastrado | 3 |
| [US03](ep01-portal-autenticacao.md#us03) | Recuperação de senha | [EP01](ep01-portal-autenticacao.md) | Usuário cadastrado | 3 |
| [US04](ep01-portal-autenticacao.md#us04) | Página institucional editável | [EP01](ep01-portal-autenticacao.md) | Administrador | 2 |
| [US05](ep01-portal-autenticacao.md#us05) | Editar dados do próprio perfil | [EP01](ep01-portal-autenticacao.md) | Usuário logado | 2 |
| [US06](ep01-portal-autenticacao.md#us06) | Encerrar sessões em outros dispositivos | [EP01](ep01-portal-autenticacao.md) | Usuário logado | 1 |
| [US07](ep02-usuarios-perfis.md#us07) | Convidar novo membro | [EP02](ep02-usuarios-perfis.md) | Administrador | 4 |
| [US08](ep02-usuarios-perfis.md#us08) | Inativar acesso de usuário | [EP02](ep02-usuarios-perfis.md) | Administrador | 3 |
| [US09](ep02-usuarios-perfis.md#us09) | Definir nível de acesso | [EP02](ep02-usuarios-perfis.md) | Administrador | 2 |
| [US10](ep02-usuarios-perfis.md#us10) | Vincular Cliente aos condomínios corretos | [EP02](ep02-usuarios-perfis.md) | Administrador | 2 |
| [US11](ep02-usuarios-perfis.md#us11) | Histórico de ações da Gestão de Usuários | [EP02](ep02-usuarios-perfis.md) | Administrador | 2 |
| [US12](ep03-cadastro-acordos.md#us12) | Cadastrar condomínio | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 2 |
| [US13](ep03-cadastro-acordos.md#us13) | Cadastrar devedor | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 1 |
| [US14](ep03-cadastro-acordos.md#us14) | Importar lista de inadimplentes em lote | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 2 |
| [US15](ep03-cadastro-acordos.md#us15) | Cadastrar novo acordo | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 3 |
| [US16](ep03-cadastro-acordos.md#us16) | Definir honorários do acordo | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 2 |
| [US17](ep03-cadastro-acordos.md#us17) | Fracionar dívida em parcelas | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 3 |
| [US18](ep03-cadastro-acordos.md#us18) | Atribuir acordo a um advogado responsável | [EP03](ep03-cadastro-acordos.md) | Administrador / Equipe Operacional | 3 |
| [US19](ep03-cadastro-acordos.md#us19) | Editar acordo já cadastrado | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 2 |
| [US20](ep03-cadastro-acordos.md#us20) | Cancelar/encerrar acordo | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 2 |
| [US21](ep03-cadastro-acordos.md#us21) | Anexar documentos ao acordo | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 2 |
| [US22](ep03-cadastro-acordos.md#us22) | Buscar/filtrar acordos | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 2 |
| [US23](ep03-cadastro-acordos.md#us23) | Acompanhar renovação de contrato | [EP03](ep03-cadastro-acordos.md) | Administrador | 2 |
| [US24](ep03-cadastro-acordos.md#us24) | Gerar e salvar PDF do acordo | [EP03](ep03-cadastro-acordos.md) | Equipe Operacional | 3 |
| [US25](ep04-parcelas.md#us25) | Listar faturas do mês | [EP04](ep04-parcelas.md) | Equipe Operacional | 2 |
| [US26](ep04-parcelas.md#us26) | Dar baixa em parcela paga | [EP04](ep04-parcelas.md) | Equipe Operacional | 2 |
| [US27](ep04-parcelas.md#us27) | Sinalizar parcela em atraso | [EP04](ep04-parcelas.md) | Sistema | 1 |
| [US28](ep04-parcelas.md#us28) | Registrar pagamento parcial | [EP04](ep04-parcelas.md) | Equipe Operacional | 2 |
| [US29](ep04-parcelas.md#us29) | Registrar emissão de nota fiscal | [EP04](ep04-parcelas.md) | Equipe Operacional | 2 |
| [US30](ep04-parcelas.md#us30) | Notificação interna de parcela em atraso | [EP04](ep04-parcelas.md) | Administrador e usuário responsável pelo acordo | 2 |
| [US31](ep04-parcelas.md#us31) | Log de alterações financeiras sensíveis | [EP04](ep04-parcelas.md) | Administrador | 2 |
| [US32](ep05-comissoes-metas.md#us32) | Visualizar minhas metas e comissões | [EP05](ep05-comissoes-metas.md) | Equipe Operacional | 2 |
| [US33](ep05-comissoes-metas.md#us33) | Visão global de faturamento e comissões | [EP05](ep05-comissoes-metas.md) | Administrador | 2 |
| [US34](ep05-comissoes-metas.md#us34) | Dashboard de indicadores | [EP05](ep05-comissoes-metas.md) | Administrador | 2 |
| [US35](ep05-comissoes-metas.md#us35) | Exportar relatório de acompanhamento | [EP05](ep05-comissoes-metas.md) | Administrador | 2 |
| [US36](ep05-comissoes-metas.md#us36) | Definir metas por colaborador | [EP05](ep05-comissoes-metas.md) | Administrador | 2 |
| [US37](ep06-painel-cliente.md#us37) | Consultar status dos acordos do condomínio | [EP06](ep06-painel-cliente.md) | Cliente | 2 |
| [US38](ep06-painel-cliente.md#us38) | Histórico de pagamentos de um morador | [EP06](ep06-painel-cliente.md) | Cliente | 1 |
| [US39](ep06-painel-cliente.md#us39) | Baixar relatório simplificado | [EP06](ep06-painel-cliente.md) | Cliente | 2 |
| [US40](ep06-painel-cliente.md#us40) | Notificação automática por e-mail ao Cliente | [EP06](ep06-painel-cliente.md) | Cliente | 3 |

Total: **40 histórias** e **87 critérios de aceitação** em 6 épicos.

Para as dependências entre histórias, veja a [matriz de rastreabilidade](../rastreabilidade/matriz.md).

---

## Histórico de versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 13/09/2026 | Criação da seção de histórias e das convenções de identificação. | Gabriela Tiago de Araújo |
| 1.1 | 13/09/2026 | Matriz de rastreabilidade e índice completo das histórias. | Gabriela Tiago de Araújo |
| 1.2 | 25/10/2026 | Inclusão do histórico de versão. | Mateus Vieira |
