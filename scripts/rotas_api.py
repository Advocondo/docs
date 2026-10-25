"""Gera a tabela das rotas da API do back-end, a partir do esquema OpenAPI.

Preenche a página `docs/pc2/api-externa.md` entre os marcadores
`<!-- rotas-api:inicio -->` e `<!-- rotas-api:fim -->`. A aplicação é criada com as
variáveis do `.env.example`, sem conectar ao banco.

Uso, a partir da pasta do back-end:

    set -a && . ./.env.example && set +a
    uv run python ../docs/scripts/rotas_api.py ../docs/docs/pc2/api-externa.md
"""

import sys
from collections import defaultdict
from pathlib import Path

from advocondo.main import create_app

START = "<!-- rotas-api:inicio -->"
END = "<!-- rotas-api:fim -->"
BACK_DOCS = "https://github.com/Advocondo/back/blob/main/docs/"
# Página de referência de cada grupo de rotas (tag do OpenAPI) em docs/ do back.
REFERENCE = {
    "auth": "auth.md",
    "setup": "auth.md",
    "users": "users.md",
    "goals": "metas.md",
    "condominiums": "condominios.md",
    "debtors": "devedores.md",
    "agreements": "acordos.md",
    "agreement-pdfs": "documentos.md",
    "installments": "parcelas.md",
    "client-panel": "painel-cliente.md",
    "landing": "landing.md",
    "health": "observabilidade.md",
}


def generate() -> str:
    schema = create_app().openapi()
    groups: dict[str, list[str]] = defaultdict(list)
    for path, operations in schema["paths"].items():
        for method, operation in operations.items():
            tag = (operation.get("tags") or ["outros"])[0]
            groups[tag].append(f"`{method.upper()} {path}`")
    total = sum(len(routes) for routes in groups.values())
    rows = [
        f"**{total} operações** em {len(groups)} grupos.",
        "",
        "| Grupo | Operações | Referência |",
        "| --- | --- | --- |",
    ]
    for tag, routes in groups.items():
        page = REFERENCE.get(tag)
        link = f"[`docs/{page}`]({BACK_DOCS}{page})" if page else "sem página própria"
        rows.append(f"| `{tag}` | {'<br>'.join(routes)} | {link} |")
    return "\n".join(rows)


def main() -> None:
    page = Path(sys.argv[1])
    text = page.read_text()
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    page.write_text(f"{before}{START}\n\n{generate()}\n\n{END}{after}")


if __name__ == "__main__":
    main()
