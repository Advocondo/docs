---
icon: lucide/server
title: Deploy
---

# Deploy

O Advocondo é publicado em dois ambientes separados: o front-end roda na **Vercel**, e o back-end e o banco de dados rodam em uma máquina na **Oracle Cloud**, gerenciada pelo **Coolify**.

```mermaid
flowchart LR
  U[Usuário] --> F["Front-end<br/>Next.js · Vercel"]
  F -->|HTTP| B["Back-end<br/>FastAPI · Coolify"]
  B --> D[(PostgreSQL<br/>Coolify)]
  subgraph OCI [Oracle Cloud]
    B
    D
  end
```

| Parte | Repositório | Hospedagem | Como é publicado |
| --- | --- | --- | --- |
| Front-end | [`Advocondo/front`](https://github.com/Advocondo/front) | Vercel | Build automático a cada push na branch `main` |
| Back-end | [`Advocondo/back`](https://github.com/Advocondo/back) | Oracle Cloud + Coolify | Coolify faz o build da imagem Docker de produção (`Dockerfile.prod`) |
| Banco de dados | — | Oracle Cloud + Coolify | PostgreSQL gerenciado pelo mesmo Coolify do back-end |

## Front-end na Vercel

A Vercel detecta o Next.js e roda `npm run build`. Não é preciso nenhum `vercel.json`.

O `next.config.ts` usa `output: "standalone"` apenas fora da Vercel, porque essa opção é necessária para a imagem Docker (`Dockerfile`), mas quebra o build da Vercel com o erro `ENOENT: ... .next/next-server.js.nft.json`:

```ts
output: process.env.VERCEL ? undefined : "standalone",
```

A Vercel define `VERCEL=1` durante o build, então a mesma configuração serve para os dois casos.

## Back-end na Oracle Cloud com Coolify

O [Coolify](https://coolify.io) roda em uma instância da Oracle Cloud e faz o build e a execução do back-end a partir do repositório `Advocondo/back`.

- **Imagem:** `Dockerfile.prod`, um build multi-stage com `uv`. A imagem final roda como usuário não-root e sobe a API com `python -m advocondo` na porta `8000`.
- **Banco de dados:** o PostgreSQL também é um recurso do mesmo Coolify, na mesma instância. O back-end se conecta a ele pela `DATABASE_URL`.
- **Variáveis de ambiente:** são configuradas no painel do Coolify, e não no repositório. O `.env.example` lista as variáveis esperadas.
- **Migrations:** o schema do banco é atualizado pelo Alembic. Configure no Coolify o *Pre-deployment command* do back-end como `alembic upgrade head`, para que as migrations rodem antes de cada nova versão da API subir. Elas não rodam sozinhas.
- **Verificação:** a rota `GET /health` confirma se a API está no ar, e `GET /health/ready` também verifica o banco.

### Primeiro deploy: criar o Administrador

Os usuários entram no sistema por convite ([US07](../historias/ep02-usuarios-perfis.md#us07)), e só um Administrador logado pode convidar. Por isso, depois do primeiro deploy, o primeiro usuário é criado por um comando, uma única vez. Ele já nasce como Administrador ativo e pode fazer login ([US02](../historias/ep01-portal-autenticacao.md#us02)).

1. Confirme que o deploy terminou e que as migrations rodaram (`GET /health/ready` responde `200`).
2. No Coolify, abra o recurso do back-end e vá em **Terminal**.
3. Rode, com o e-mail e o nome de quem vai administrar o sistema:

    ```bash
    python -m advocondo.users.create_admin --email admin@escritorio.com.br --name "Nome do Administrador"
    ```

4. Digite a senha duas vezes, com pelo menos 8 caracteres. A senha é lida pelo terminal e não fica no histórico do shell.
5. Faça login no front com esse e-mail e essa senha.

O comando só funciona com o banco vazio. Se já existir algum usuário, ele recusa com a mensagem "O primeiro usuário já foi criado. Os demais entram por convite.", então não serve para criar outros administradores depois. Os detalhes, incluindo como corrigir um e-mail digitado errado, estão em `docs/auth.md` no repositório do back-end.

!!! note "O `docker-compose.yml` é só para desenvolvimento"
    O `docker-compose.yml` do back-end usa o `Dockerfile.dev`, com hot reload e o código montado como volume. Ele não é usado em produção.
