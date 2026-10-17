# Débito técnico — Mateus (`matix0`)

Registro persistente do que ficou pendente nas tarefas feitas por Mateus (com agente de IA). Fica na raiz do repositório `docs` (fora de `docs/`, então **não** vai para o site publicado) para valer entre repositórios e sessões.

## Regras de uso

- **Ao fechar cada US/PR**, o agente revisa este arquivo: adiciona o que ficou pendente, atualiza o status do que mudou e move o resolvido para "Resolvidos".
- Um item = uma pendência acionável, com ID estável (`DT-nnn`, nunca reaproveitado), origem e como resolver.
- **Tipo:** `bloqueio` (impede avançar) · `ação manual` (só o Mateus/time pode fazer) · `dívida` (código/doc a melhorar) · `fora do escopo` (decisão de adiar) · `decisão` (confirmar com PO/time).
- **Status:** `aberto` · `em andamento` · `resolvido`.
- **Branches:** `<nº da US>-<mini-descrição>`, como as do time (ex.: `13-cadastrar-devedor`, `09-docs-condominio`), inclusive as locais. Exceção histórica: o PR back#50 continua na `US-12-cadastrar-condominio`.
- **Commits:** Conventional Commits em inglês (`feat(condominios): ...`).
- **PRs:** corpo só com o link da issue (`Closes #N`); texto extra só se algo não puder ser implementado ou houver um problema a explicar. Merge exige 1 review e CI verde.
- **Idioma:** código em inglês (classes, campos, JSON, tabelas e rotas); domínios (pastas `condominios/`, `devedores/`...) e mensagens ao usuário em português.
- Mudanças deste arquivo vão no PR da US que as originou (ou em um PR próprio quando for só atualização).

## Abertos

| ID | Tipo | Origem | Repo | Pendência | Como resolver | Status |
|---|---|---|---|---|---|---|
| DT-003 | ação manual | US12 | front | O front depende do branch `prepare-build-on-install` do ui-kit (PR [ui-kit#1](https://github.com/Advocondo/ui-kit/pull/1)). Sem merge, `npm ci` quebra se o branch for apagado. | Mergear o ui-kit#1 e repontar `edson-alexandre-design-system` para `github:Advocondo/ui-kit#main` (ou uma tag) no `package.json` do front. Nenhum token é necessário. | aberto |
| DT-004 | ação manual | US12 | back | As migrations não rodam sozinhas no deploy. | Coolify → back-end → *Pre-deployment command*: `alembic upgrade head` (ver `docs/migrations.md`). Fazer antes do primeiro deploy com a tabela `condominios`. | aberto |
| DT-005 | fora do escopo | US12 | back/front | A listagem de condomínios não traz unidades, acordos ativos nem inadimplência acumulada (colunas do protótipo). | Acordos ativos e inadimplência: agregar após US15/US17; unidades: definir a origem do dado (campo no cadastro?) e perguntar ao PO. | aberto |
| DT-010 | decisão | US13 | front | Não existe tela do devedor no Figma (`153-3312`, `34-7691`, `153-3303` verificados). Adotada a recomendação da doc: `/devedores` no padrão de Condomínios + seleção no Novo Acordo. | Sinalizar no PR da US13 e pedir desenho ao time de design. | aberto |
| DT-012 | decisão | plano | — | Confirmar prazo "dia 20" = 20/10/2026 e se 12/10 (segunda) é feriado/aula. | Mateus confirma. | aberto |
| DT-014 | dívida | US12 | front | `/` redireciona para `/condominios` (a home do Next era boilerplate). | A landing institucional (US01) assume a rota `/` e remove o redirect. | aberto |
| DT-015 | dívida | US12 | front | A barra lateral usa o texto "Advocondo" no lugar do logo: os assets do ui-kit (`assets/`) não foram copiados para `public/`. | Copiar o logo para `public/design-system/assets/` e usar `<Logo base=...>`; confirmar com o design qual lockup usar. | aberto |
| DT-016 | dívida | US12 | front | A listagem pede no máximo 200 condomínios (limite do back) e não tem paginação. | Paginar com `limit/offset` quando houver mais de 200 ou a lista ficar lenta. | aberto |
| DT-017 | ação manual | US12 | front | `NEXT_PUBLIC_API_URL` é embutida no build: sem ela o front aponta para `http://localhost:8000`. | Definir a variável na Vercel (produção e preview) com a URL https do back e conferir `CORS_ALLOW_ORIGINS`/regex de preview no Coolify. | aberto |
| DT-018 | dívida | US12 | front | As mudanças nos `Dockerfile`/`Dockerfile.dev` (git no Alpine, `ARG NEXT_PUBLIC_API_URL`) não foram testadas: sem Docker no ambiente. | Rodar `docker build --build-arg NEXT_PUBLIC_API_URL=... .` e `docker build -f Dockerfile.dev .` uma vez. | aberto |
| DT-019 | dívida | US12 | front | `@types/node` subiu de ^20 para ^22 (exigência do Vitest 5; CI e Docker já usam Node 22). | Nenhuma ação, apenas ciência: confirmar que o CI ficou verde. | aberto |
| DT-020 | dívida | US12 | front | A listagem carrega os dados no navegador (`useEffect`), pois ainda não há login. A página já é um Server Component fino, mas a busca inicial não é renderizada no servidor. | Com a US02, avaliar buscar a 1ª página no servidor (fetch com token) e passar à view client como prop. | aberto |
| DT-011 | fora do escopo | US15 | back | O acordo ainda não tem advogado responsável: a US18 depende da marcação de advogado do convite (US07, back#60). Nenhuma coluna foi criada antes da hora. | Na US18: coluna `responsible_id` (FK para `users`), restrita a usuários advogados, com histórico de reatribuição. | aberto |
| DT-021 | dívida | US12–US17 | front | O front (front#46) usa as rotas e campos antigos em português (`/condominios`, `nome`, `sindico_nome`...) e não envia o token de login. O back agora usa `/condominiums`, `/debtors`, `/agreements`, `/installments`, campos em inglês e exige `Authorization`. | Ao retomar o front: atualizar `app/lib/api.ts` e os tipos, enviar o token do login e cobrir devedor, acordo e parcelas. | aberto |
| DT-022 | ação manual | US12–US16 | back | Os PRs são empilhados: back#50 → #65 → #66 → #67 → #68. Cada um tem como base o branch do anterior. | Mergear nessa ordem; depois de cada merge, trocar a base do PR seguinte para `main` (o GitHub faz sozinho se o branch mergeado for apagado). | aberto |
| DT-023 | ação manual | US12, US17 | back | Os PRs do Pedro (back#63 US23, #64 US27) também criam `condominios/__init__.py`, `parcelas/__init__.py` e arquivos `test_*_unit.py`, e mexem no `pyproject.toml`. | Quem mergear depois resolve o conflito (pequeno). Os nomes `contract_renewal_date`, `due_date` e `payment_date` já batem com as funções dele (avisado nos PRs). | aberto |
| DT-024 | dívida | US16 | back | A comissão (US26, US32) ainda não existe. | Calcular sobre `installments.fee_amount` das parcelas pagas; o honorário já está dividido por parcela. | aberto |
| DT-025 | fora do escopo | US17 | back | Mudar o valor da última parcela em aberto é recusado, porque não há parcela seguinte para absorver a diferença; mudar o total é a US19 (editar acordo). | Implementar a US19 recalculando o plano e a divisão de honorários das parcelas em aberto. | aberto |

## Resolvidos

| ID | Resolvido em | Como |
|---|---|---|
| DT-001 | 01/10/2026 | Commits aplicados a partir dos patches e enviados por SSH pela máquina local (branch `US-12-cadastrar-condominio` em back e docs). PRs e atribuição da issue #11 ao `matix0` seguem pendentes. |
| DT-008 | 01/10/2026 | Postgres 18.6 instalado localmente (mesma versão do CI): 78 testes passando, `alembic upgrade head`/`downgrade base` OK. |
| DT-002 | 02/10/2026 | O `ui-kit` é público (sem token). Instalação via git exigiu o script `prepare` (PR [ui-kit#1](https://github.com/Advocondo/ui-kit/pull/1)). |
| DT-013 | 02/10/2026 | Front da US12 tem ação Editar por linha e o botão correto "Salvar condomínio". Falta avisar o design (o Figma ainda diz "Salvar prazo"). |
| Revisão US12 (1) | 02/10/2026 | Back: erros de negócio registrados uma vez por módulo (`advocondo/errors.py` + `register_errors`), sem try/except por endpoint. |
| Revisão US12 (2) | 02/10/2026 | Front: `Field` e `Section` movidos para `app/components/FormField.tsx` para reuso nas próximas telas. |
| Revisão US12 (3) | 02/10/2026 | Front: `page.tsx` virou Server Component fino com `metadata`; interação em `CondominiosView` (client). Resta o DT-020. |
| Revisão US12 (4) | 02/10/2026 | Front: `UFS.ts` renomeado para `ufs.ts`. |
| DT-006 | 17/10/2026 | `agreements.condominium_id` é `NOT NULL` com FK (back#66); acordo sem condomínio cadastrado é recusado com 404. |
| DT-007 | 17/10/2026 | O login da Gabriela entrou no `main`; as rotas internas usam `require_office_staff` (Administrador ou Equipe Operacional), com testes 401/403 (back#50). |
| DT-009 | 17/10/2026 | O código antigo da US12 foi refeito na arquitetura do grupo; cobertura total da suíte em 98%. |

## Histórico

- 01/10/2026 — Arquivo criado; DT-001 a DT-013 levantados na US12 (back).
- 01/10/2026 — DT-001 e DT-008 resolvidos.
- 02/10/2026 — Front da US12 entregue; DT-002 e DT-013 resolvidos; DT-003 reformulado; DT-014 a DT-019 levantados.
- 02/10/2026 — Revisão de arquitetura da US12: 4 correções aplicadas (back e front); DT-020 levantado.
- 17/10/2026 — Back de US12, US13, US15, US17 e US16 refeito/entregue na arquitetura do grupo (back#50, #65, #66, #67, #68); convenções de branch, commit, PR e idioma atualizadas; DT-006, DT-007 e DT-009 resolvidos; DT-021 a DT-025 levantados.
