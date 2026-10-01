# Débito técnico — Mateus (`matix0`)

Registro persistente do que ficou pendente nas tarefas feitas por Mateus (com agente de IA). Fica na raiz do repositório `docs` (fora de `docs/`, então **não** vai para o site publicado) para valer entre repositórios e sessões.

## Regras de uso

- **Ao fechar cada US/PR**, o agente revisa este arquivo: adiciona o que ficou pendente, atualiza o status do que mudou e move o resolvido para "Resolvidos".
- Um item = uma pendência acionável, com ID estável (`DT-nnn`, nunca reaproveitado), origem e como resolver.
- **Tipo:** `bloqueio` (impede avançar) · `ação manual` (só o Mateus/time pode fazer) · `dívida` (código/doc a melhorar) · `fora do escopo` (decisão de adiar) · `decisão` (confirmar com PO/time).
- **Status:** `aberto` · `em andamento` · `resolvido`.
- Mudanças deste arquivo vão no PR da US que as originou (ou em um PR próprio quando for só atualização).

## Abertos

| ID | Tipo | Origem | Repo | Pendência | Como resolver | Status |
|---|---|---|---|---|---|---|
| DT-001 | bloqueio | US12 | back/front/docs | O Claude GitHub App não tem acesso à org Advocondo: `git push` e edição de issues retornam 403. Branches e commits estão só locais. | Owner da org instala o app em https://github.com/apps/claude/installations/select_target ou Mateus reconecta o GitHub em claude.ai. Depois: push, PRs com `Closes #N`, atribuir issues a `matix0`. | aberto |
| DT-002 | bloqueio | US12 | front | Sem acesso a `Advocondo/ui-kit` (privado): o front da US12 não pode ser implementado com o design system. | Liberar o acesso (mesmo passo do DT-001) ou colar README/componentes; depois seguir `LIBRARY.md`. | aberto |
| DT-003 | ação manual | US12 | front | Token read-only do GitHub nos segredos do GitHub Actions e da Vercel para o `npm ci` instalar o ui-kit (`github:Advocondo/ui-kit`). | Criar o token, configurar `UI_KIT_TOKEN` (nome a definir) no CI e na Vercel; documentar em `docs/segredos` do front. | aberto |
| DT-004 | ação manual | US12 | back | As migrations não rodam sozinhas no deploy. | Coolify → back-end → *Pre-deployment command*: `alembic upgrade head` (ver `docs/migrations.md`). Fazer antes do primeiro deploy com a tabela `condominios`. | aberto |
| DT-005 | fora do escopo | US12 | back/front | A listagem de condomínios não traz unidades, acordos ativos nem inadimplência acumulada (colunas do protótipo). | Acordos ativos e inadimplência: agregar após US15/US17; unidades: definir a origem do dado (campo no cadastro?) e perguntar ao PO. | aberto |
| DT-006 | dívida | US12 | back | US12-CA01 ("acordo exige condomínio") só se cumpre com a FK obrigatória `acordos.condominio_id`. | Garantir na migration e nos testes da US15. | aberto |
| DT-007 | dívida | US12 | back | `require_user` é um no-op: nenhuma rota está realmente protegida. | Implementar em `advocondo/auth.py` quando a US02 (Gabriela) existir; adicionar testes 401/403 e aplicar perfis. | aberto |
| DT-008 | dívida | US12 | back | Testes rodados localmente em Postgres 16; CI usa 18. | Conferir o CI no primeiro PR; se divergir, alinhar. | aberto |
| DT-009 | dívida | US12 | back | Cobertura não exercita `schemas.py` linha 24 (valor não-string na máscara) e o ramo `service.py` 34-37 só pelo teste de corrida. | Cobrir com teste unitário se o CI exigir meta de cobertura. | aberto |
| DT-010 | decisão | US13 | front | Não existe tela do devedor no Figma (`153-3312`, `34-7691`, `153-3303` verificados). Adotada a recomendação da doc: `/devedores` no padrão de Condomínios + seleção no Novo Acordo. | Sinalizar no PR da US13 e pedir desenho ao time de design. | aberto |
| DT-011 | fora do escopo | US15 | back | Campo "responsável" do acordo fica de fora (US18/US07 abertas): coluna `responsavel_id` nullable. | Preencher na US18, com restrição a usuários advogados. | aberto |
| DT-012 | decisão | plano | — | Confirmar prazo "dia 20" = 20/10/2026 e se 12/10 (segunda) é feriado/aula. | Mateus confirma. | aberto |
| DT-013 | dívida | US12 | front | Protótipo não tem ação de editar na listagem de condomínios (US12-CA02 na UI) e o botão do diálogo diz "Salvar prazo". | Implementar edição (diálogo ou página) e rótulo "Salvar condomínio"; avisar o design. | aberto |

## Resolvidos

| ID | Resolvido em | Como |
|---|---|---|
| — | — | — |

## Histórico

- 01/10/2026 — Arquivo criado; DT-001 a DT-013 levantados na US12 (back).
