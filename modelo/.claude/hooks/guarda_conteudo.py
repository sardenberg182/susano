#!/usr/bin/env python3
"""PreToolUse (Write|Edit|NotebookEdit) do Susano.

Bloqueia segredo, cartao, CPF e travessao; pergunta antes de gravar telefone ou e-mail.
Age so em arquivos dentro do repositorio. Falha interna = erro nao bloqueante (o CI segue valendo).
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import guardas  # noqa: E402


def decidir(decisao: str, motivo: str) -> int:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": decisao,
                    "permissionDecisionReason": motivo,
                }
            },
            ensure_ascii=False,
        )
    )
    return 0


def main() -> int:
    entrada = json.load(sys.stdin)
    ti = entrada.get("tool_input") or {}
    caminho = ti.get("file_path") or ti.get("notebook_path") or ""
    partes = [ti.get(k) for k in ("content", "new_string", "new_source") if isinstance(ti.get(k), str)]
    for edicao in ti.get("edits") or []:
        if isinstance(edicao, dict) and isinstance(edicao.get("new_string"), str):
            partes.append(edicao["new_string"])
    texto = "\n".join(partes)
    if not texto or not caminho:
        return 0

    base = Path(entrada.get("cwd") or os.getcwd())
    raiz = Path(os.environ.get("CLAUDE_PROJECT_DIR") or base).resolve()
    alvo = Path(caminho)
    if not alvo.is_absolute():
        alvo = base / alvo
    try:
        rel = alvo.resolve().relative_to(raiz).as_posix()
    except ValueError:
        return 0  # fora do repositorio: quem decide sao as regras de permissao

    achados = guardas.analisar(texto, rel)
    bloqueados = guardas.bloqueios(achados)
    if bloqueados:
        lista = "; ".join(a.texto() for a in bloqueados[:6])
        return decidir(
            "deny",
            f"Susano bloqueou a escrita em {rel}: {lista}. Remova o dado e deixe so a referencia de onde ele vive, "
            "sem o valor. Se for ID de conta de anuncio, escreva com o prefixo da plataforma (ex.: act_).",
        )
    perguntas = guardas.avisos(achados)
    if perguntas:
        lista = "; ".join(a.texto() for a in perguntas[:6])
        return decidir(
            "ask",
            f"Possivel dado pessoal em {rel}: {lista}. Confirme que e contato profissional necessario; "
            "dado pessoal fica no sistema de origem.",
        )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"Susano: guarda de conteudo falhou ({exc}); escrita liberada, o CI valida.", file=sys.stderr)
        sys.exit(1)
