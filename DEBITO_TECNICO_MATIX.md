# Débito técnico — Mateus (`matix0`)

Registro persistente do que ficou pendente nas tarefas feitas por Mateus (com agente de IA). Fica na raiz do repositório `docs` (fora de `docs/`, então **não** vai para o site publicado) para valer entre repositórios e sessões.

## Regras de uso

- **Ao fechar cada US/PR**, o agente revisa este arquivo: adiciona o que ficou pendente, atualiza o status do que mudou e move o resolvido para "Resolvidos".
- Um item = uma pendência acionável, com ID estável (`DT-nnn`, nunca reaproveitado), origem e como resolver.
- **Tipo:** `bloqueio` (impede avançar) · `ação manual` (só o Mateus/time pode fazer) · `dívida` (código/doc a melhorar) · `fora do escopo` (decisão de adiar) · `decisão` (confirmar com PO/time).
- **Status:** `aberto` · `em andamento` · `resolvido`.
- **Branches:** sempre `US-XX-nome-da-us` (ex.: `US-12-cadastrar-condominio`), o mesmo nome em back, front e docs.
- Mudanças deste arquivo vão no PR da US que as originou (ou em um PR próprio quando for só atualização).

## Abertos

| ID | Tipo | Origem | Repo | Pendência | Como resolver | Status |
|---|---|---|---|---|---|---|
| DT-003 | ação manual | US12 | front | O front depende do branch `prepare-build-on-install` do ui-kit (PR [ui-kit#1](https://github.com/Advocondo/ui-kit/pull/1)). Sem merge, `npm ci` quebra se o branch for apagado. | Mergear o ui-kit#1 e repontar `edson-alexandre-design-system` para `github:Advocondo/ui-kit#main` (ou uma tag) no `package.json` do front. Nenhum token é necessário. | aberto |
| DT-004 | ação manual | US12 | back | As migrations não rodam sozinhas no deploy. | Coolify → back-end → *Pre-deployment command*: `alembic upgrade head` (ver `docs/migrations.md`). Fazer antes do primeiro deploy com a tabela `condominios`. | aberto |
| DT-005 | fora do escopo | US12 | back/front | A listagem de condomínios não traz unidades, acordos ativos nem inadimplência acumulada (colunas do protótipo). | Acordos ativos e inadimplência: agregar após US15/US17; unidades: definir a origem do dado (campo no cadastro?) e perguntar ao PO. | aberto |
| DT-006 | dívida | US12 | back | US12-CA01 ("acordo exige condomínio") só se cumpre com a FK obrigatória `acordos.condominio_id`. | Garantir na migration e nos testes da US15. | aberto |
| DT-007 | dívida | US12 | back | `require_user` é um no-op: nenhuma rota está realmente protegida. | Implementar em `advocondo/auth.py` quando a US02 (Gabriela) existir; adicionar testes 401/403 e aplicar perfis. | aberto |
| DT-009 | dívida | US12 | back | Cobertura não exercita `schemas.py` linha 24 (valor não-string na máscara) e o ramo `service.py` 34-37 só pelo teste de corrida. | Cobrir com teste unitário se o CI exigir meta de cobertura. | aberto |
| DT-010 | decisão | US13 | front | Não existe tela do devedor no Figma (`153-3312`, `34-7691`, `153-3303` verificados). Adotada a recomendação da doc: `/devedores` no padrão de Condomínios + seleção no Novo Acordo. | Sinalizar no PR da US13 e pedir desenho ao time de design. | aberto |
| DT-011 | fora do escopo | US15 | back | Campo "responsável" do acordo fica de fora (US18/US07 abertas): coluna `responsavel_id` nullable. | Preencher na US18, com restrição a usuários advogados. | aberto |
| DT-012 | decisão | plano | — | Confirmar prazo "dia 20" = 20/10/2026 e se 12/10 (segunda) é feriado/aula. | Mateus confirma. | aberto |
| DT-014 | dívida | US12 | front | `/` redireciona para `/condominios` (a home do Next era boilerplate). | A landing institucional (US01) assume a rota `/` e remove o redirect. | aberto |
| DT-015 | dívida | US12 | front | A barra lateral usa o texto "Advocondo" no lugar do logo: os assets do ui-kit (`assets/`) não foram copiados para `public/`. | Copiar o logo para `public/design-system/assets/` e usar `<Logo base=...>`; confirmar com o design qual lockup usar. | aberto |
| DT-016 | dívida | US12 | front | A listagem pede no máximo 200 condomínios (limite do back) e não tem paginação. | Paginar com `limit/offset` quando houver mais de 200 ou a lista ficar lenta. | aberto |
| DT-017 | ação manual | US12 | front | `NEXT_PUBLIC_API_URL` é embutida no build: sem ela o front aponta para `http://localhost:8000`. | Definir a variável na Vercel (produção e preview) com a URL https do back e conferir `CORS_ALLOW_ORIGINS`/regex de preview no Coolify. | aberto |
| DT-018 | dívida | US12 | front | As mudanças nos `Dockerfile`/`Dockerfile.dev` (git no Alpine, `ARG NEXT_PUBLIC_API_URL`) não foram testadas: sem Docker no ambiente. | Rodar `docker build --build-arg NEXT_PUBLIC_API_URL=... .` e `docker build -f Dockerfile.dev .` uma vez. | aberto |
| DT-019 | dívida | US12 | front | `@types/node` subiu de ^20 para ^22 (exigência do Vitest 5; CI e Docker já usam Node 22). | Nenhuma ação, apenas ciência: confirmar que o CI ficou verde. | aberto |

## Resolvidos

| ID | Resolvido em | Como |
|---|---|---|
| DT-001 | 01/10/2026 | Commits aplicados a partir dos patches e enviados por SSH pela máquina local (branch `US-12-cadastrar-condominio` em back e docs). PRs e atribuição da issue #11 ao `matix0` seguem pendentes. |
| DT-008 | 01/10/2026 | Postgres 18.6 instalado localmente (mesma versão do CI): 78 testes passando, `alembic upgrade head`/`downgrade base` OK. |
| DT-002 | 02/10/2026 | O `ui-kit` é público (sem token). Instalação via git exigiu o script `prepare` (PR [ui-kit#1](https://github.com/Advocondo/ui-kit/pull/1)). |
| DT-013 | 02/10/2026 | Front da US12 tem ação Editar por linha e o botão correto "Salvar condomínio". Falta avisar o design (o Figma ainda diz "Salvar prazo"). |

## Histórico

- 01/10/2026 — Arquivo criado; DT-001 a DT-013 levantados na US12 (back).
- 01/10/2026 — DT-001 e DT-008 resolvidos.
- 02/10/2026 — Front da US12 entregue; DT-002 e DT-013 resolvidos; DT-003 reformulado; DT-014 a DT-019 levantados.
