#!/usr/bin/env python3
"""Confere o endereço de autor e de committer dos commits de um intervalo (repositório público: SUS05).

Uso:  python3 ferramentas/conferir_autoria.py [--com-merges] origin/main..HEAD
      --com-merges inclui os commits de merge, que ficam de fora sem a flag

Aceita só endereços que não identificam uma caixa de e-mail pessoal ou corporativa: o noreply da conta do GitHub
(`<id>+<usuario>@users.noreply.github.com`, inclusive bots como `<id>+dependabot[bot]@...`), o do próprio GitHub
(`noreply@github.com`, commits feitos pela web), o do agente (`noreply@anthropic.com`) e os domínios reservados de
exemplo (`example.com`, `example.org`). No PR, os commits de merge ficam de fora; no push da main, o CI usa
`--com-merges`. Merge e rebase feitos pelo GitHub gravam a conta de quem integra, com o e-mail configurado nela naquela
hora; o commit de merge e os commits refeitos pelo rebase só existem na main, por isso a conferência roda no push.
Imprime o endereço recusado só pelo domínio, nunca inteiro.
"""
from __future__ import annotations

import re
import subprocess
import sys

PERMITIDOS = [
    re.compile(r"^[0-9]+\+[A-Za-z0-9-]+(?:\[bot\])?@users\.noreply\.github\.com$"),
    re.compile(r"^[A-Za-z0-9-]+@users\.noreply\.github\.com$"),
    re.compile(r"^noreply@github\.com$"),
    re.compile(r"^noreply@anthropic\.com$"),
    re.compile(r"^[^@\s]+@example\.(?:com|org)$"),
]


def permitido(email: str) -> bool:
    return any(rx.match(email) for rx in PERMITIDOS)


def main() -> int:
    args = sys.argv[1:]
    com_merges = "--com-merges" in args
    args = [a for a in args if a != "--com-merges"]
    if len(args) != 1:
        print(__doc__)
        return 2
    cmd = ["git", "log", "--format=%h%x09%ae%x09%ce", args[0]]
    if not com_merges:
        cmd.insert(2, "--no-merges")
    r = subprocess.run(cmd, capture_output=True, text=True)
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
    print(f"conferir_autoria: {len(linhas)} commit(s) em {args[0]}, {len(recusados)} endereço(s) recusado(s)")
    return 1 if recusados else 0


if __name__ == "__main__":
    sys.exit(main())
