#!/usr/bin/env python3
"""Confere o endereço de autor e de committer dos commits de um intervalo (repositório público: SUS05).

Uso:  python3 ferramentas/conferir_autoria.py origin/main..HEAD

Aceita só endereços que não identificam uma caixa de e-mail pessoal ou corporativa: o noreply da conta do GitHub
(`<id>+<usuario>@users.noreply.github.com`), o do próprio GitHub (`noreply@github.com`, commits feitos pela web), o do
agente (`noreply@anthropic.com`) e os domínios reservados de exemplo (`example.com`, `example.org`). Merge fica de fora
(o merge de PR feito pelo GitHub usa o endereço configurado na conta do dono: lá, "Keep my email addresses private").
Imprime o endereço recusado só pelo domínio, nunca inteiro.
"""
from __future__ import annotations

import re
import subprocess
import sys

PERMITIDOS = [
    re.compile(r"^[0-9]+\+[A-Za-z0-9-]+@users\.noreply\.github\.com$"),
    re.compile(r"^[A-Za-z0-9-]+@users\.noreply\.github\.com$"),
    re.compile(r"^noreply@github\.com$"),
    re.compile(r"^noreply@anthropic\.com$"),
    re.compile(r"^[^@\s]+@example\.(?:com|org)$"),
]


def permitido(email: str) -> bool:
    return any(rx.match(email) for rx in PERMITIDOS)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    r = subprocess.run(["git", "log", "--no-merges", "--format=%h%x09%ae%x09%ce", sys.argv[1]], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"conferir_autoria: git log falhou ({r.stderr.strip()[:200]})")
        return 2
    recusados = []
    linhas = [l for l in r.stdout.splitlines() if l.strip()]
    for linha in linhas:
        sha, autor, committer = linha.split("\t")
        for papel, email in (("autor", autor), ("committer", committer)):
            if not permitido(email):
                recusados.append(f"{sha}: {papel} com endereço de @{email.rsplit('@', 1)[-1]} (use o noreply da conta)")
    for rec in recusados:
        print("ERRO  " + rec)
    print(f"conferir_autoria: {len(linhas)} commit(s) em {sys.argv[1]}, {len(recusados)} endereço(s) recusado(s)")
    return 1 if recusados else 0


if __name__ == "__main__":
    sys.exit(main())
