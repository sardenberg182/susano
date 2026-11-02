#!/usr/bin/env python3
"""PreToolUse (Write|Edit|MultiEdit|NotebookEdit) do Susano.

Bloqueia segredo, cartao, CPF e travessao; pergunta antes de gravar telefone ou e-mail.
Age so em arquivos dentro do repositorio. Falha interna (entrada invalida, import ausente, erro de leitura)
barra a escrita com saida 2: uma trava de privacidade que nao conseguiu checar nao libera nada.
A mensagem de falha cita so o tipo do erro, nunca o conteudo que seria gravado.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path


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
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import guardas  # dentro do main: import quebrado tambem barra (saida 2)

    entrada = json.load(sys.stdin)
    if not isinstance(entrada, dict):
        raise ValueError("entrada do hook nao e um objeto JSON")
    ti = entrada.get("tool_input") or {}
    if not isinstance(ti, dict):
        raise ValueError("tool_input nao e um objeto")
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
        print(
            f"Susano: a guarda de conteudo falhou ({type(exc).__name__}) e barrou a escrita por seguranca. "
            "Confira o Python 3.9+ e o arquivo .claude/hooks/guardas.py; o CI segue validando.",
            file=sys.stderr,
        )
        sys.exit(2)
