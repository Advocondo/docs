"""Gera o modelo físico do banco (diagrama ER e dicionário de dados) em Markdown.

Lê os models do back-end (`Base.metadata`), sem conectar a nenhum banco, e imprime
o conteúdo da página `docs/pc2/modelo-fisico.md` entre os marcadores
`<!-- modelo-fisico:inicio -->` e `<!-- modelo-fisico:fim -->`.

Uso, a partir da pasta do back-end:

    uv run python ../docs/scripts/modelo_fisico.py ../docs/docs/pc2/modelo-fisico.md
"""

import re
import sys
from pathlib import Path

from sqlalchemy import CheckConstraint, Table, UniqueConstraint
from sqlalchemy.dialects import postgresql

import advocondo.models  # noqa: F401  (registra todos os models no metadata)
from advocondo.db import Base

START = "<!-- modelo-fisico:inicio -->"
END = "<!-- modelo-fisico:fim -->"
DIALECT = postgresql.dialect()


def column_type(column) -> str:
    return column.type.compile(dialect=DIALECT)


def default_of(column) -> str:
    if column.server_default is not None:
        return f"`{column.server_default.arg}`"
    if column.default is not None and column.default.is_scalar:
        return f"`{column.default.arg}`"
    return ""


def keys_of(table: Table, column) -> str:
    keys = []
    if column.primary_key:
        keys.append("PK")
    for foreign_key in column.foreign_keys:
        keys.append(f"FK → `{foreign_key.target_fullname}`")
    for constraint in table.constraints:
        if isinstance(constraint, UniqueConstraint) and column.name in constraint.columns:
            together = [c.name for c in constraint.columns]
            keys.append("único" if len(together) == 1 else f"único ({', '.join(together)})")
    if column.unique:
        keys.append("único")
    indexed = column.index or any(
        column.name in index.columns for index in table.indexes
    )
    if indexed:
        keys.append("índice")
    return ", ".join(dict.fromkeys(keys))


TIMESTAMPS = ("created_at", "updated_at")


def ordered_columns(table: Table) -> list:
    """Chave primária primeiro e as colunas de data de registro por último."""
    return sorted(
        table.columns,
        key=lambda c: (not c.primary_key, c.name in TIMESTAMPS),
    )


# Um diagrama por assunto, para caber na tela. Tabelas de outro assunto citadas por
# chave estrangeira aparecem só com o nome.
GROUPS = {
    "Usuários e acesso": [
        "users", "user_sessions", "password_reset_links", "user_invites",
        "user_audit_logs", "user_condominiums", "goals",
    ],
    "Acordos e cobrança": [
        "condominiums", "debtors", "agreements", "installments",
        "installment_payments", "lawyer_assignments", "agreement_edit_logs",
        "agreement_pdfs",
    ],
    "Página institucional": ["landing_blocks", "landing_images"],
}


def er_diagram(tables: list[Table]) -> str:
    """Diagramas mermaid com as chaves de cada tabela e as ligações entre elas."""
    by_name = {table.name: table for table in tables}
    grouped = {name for names in GROUPS.values() for name in names}
    missing = set(by_name) - grouped
    if missing:
        raise SystemExit(f"Tabelas sem assunto em GROUPS: {sorted(missing)}")
    sections = []
    for title, names in GROUPS.items():
        lines = [f"### {title}", "", "```mermaid", "erDiagram"]
        for name in names:
            table = by_name[name]
            for foreign_key in sorted(table.foreign_keys, key=lambda fk: fk.parent.name):
                target = foreign_key.column.table.name
                # FK que aceita nulo: o filho pode existir sem o pai.
                parent_side = "|o" if foreign_key.parent.nullable else "||"
                lines.append(
                    f'  {target} {parent_side}--o{{ {name} : "{foreign_key.parent.name}"'
                )
        for name in names:
            # Só as chaves; o resto das colunas está no dicionário de dados.
            lines.append(f"  {name} {{")
            for column in ordered_columns(by_name[name]):
                if not (column.primary_key or column.foreign_keys):
                    continue
                kind = re.sub(r"[^A-Za-z0-9_]", "_", column_type(column)).strip("_")
                marks = [m for m, on in (("PK", column.primary_key), ("FK", bool(column.foreign_keys))) if on]
                lines.append(f"    {kind} {column.name} {','.join(marks)}")
            lines.append("  }")
        lines.append("```")
        sections.append("\n".join(lines))
    return "\n\n".join(sections)


def data_dictionary(tables: list[Table]) -> str:
    sections = []
    for table in tables:
        rows = [
            f"### `{table.name}`",
            "",
            "| Coluna | Tipo | Nulo | Padrão | Chaves e índices |",
            "| --- | --- | :---: | --- | --- |",
        ]
        for column in ordered_columns(table):
            rows.append(
                f"| `{column.name}` | `{column_type(column)}` "
                f"| {'sim' if column.nullable else 'não'} | {default_of(column)} "
                f"| {keys_of(table, column)} |"
            )
        checks = [
            c for c in table.constraints if isinstance(c, CheckConstraint)
        ]
        if checks:
            rows.append("")
            rows.append("**Regras (`CHECK`):**")
            rows.append("")
            for check in sorted(checks, key=lambda c: str(c.name)):
                sql = check.sqltext.compile(
                    dialect=DIALECT, compile_kwargs={"literal_binds": True}
                )
                rows.append(f"- `{check.name}`: `{sql}`")
        sections.append("\n".join(rows))
    return "\n\n".join(sections)


def generate() -> str:
    tables = sorted(Base.metadata.tables.values(), key=lambda t: t.name)
    constraints = sum(
        len([c for c in t.constraints if not c.__class__.__name__ == "PrimaryKeyConstraint"])
        + len(t.indexes)
        for t in tables
    )
    summary = (
        f"**{len(tables)} tabelas**, {sum(len(t.columns) for t in tables)} colunas "
        f"e {constraints} restrições e índices (chaves estrangeiras, `UNIQUE`, "
        "`CHECK` e índices), sem contar as chaves primárias."
    )
    return "\n\n".join(
        [summary, "## Diagrama entidade-relacionamento", er_diagram(tables),
         "## Dicionário de dados", data_dictionary(tables)]
    )


def main() -> None:
    page = Path(sys.argv[1])
    text = page.read_text()
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    page.write_text(f"{before}{START}\n\n{generate()}\n\n{END}{after}")


if __name__ == "__main__":
    main()
