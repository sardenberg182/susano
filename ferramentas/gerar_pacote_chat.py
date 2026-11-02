#!/usr/bin/env python3
"""Gera o pacote de chat do Susano (Caminho 3) a partir de modelo/00_susano/.

Uso, na raiz do repositório susano:  python3 ferramentas/gerar_pacote_chat.py [--destino dist/chat]

Saídas:
  SYSTEM_PROMPT.md           nucleo.md + identidade.md + situacoes.md concatenados, com a nota de modo sem shell no fim
  susano_conhecimento.zip    a pasta 00_susano/ inteira, sem MANIFEST.sha256 (vai em conhecimento do Project, GPT ou Gem)

Só biblioteca padrão. A mesma fonte do template e do plugin; nada é editado à mão aqui.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "modelo" / "00_susano"
ARQUIVOS_PROMPT = ("nucleo.md", "identidade.md", "situacoes.md")

NOTA_SEM_SHELL = """
## Modo sem shell (este Project)

Você está numa conversa, sem repositório e sem terminal. Vale tudo que está acima, com estas traduções:

- O método chega pelos caminhos de `00_susano/INDICE.md`, que está no conhecimento deste Project junto com todos os arquivos de `00_susano/`; não há skills. Abra (leia) só o arquivo que `situacoes.md` aponta e cite `caminho#seção`.
- Não há `brain.py`, `/frente`, `/nova-frente` nem `/salve`: o contexto da frente entra colado na conversa ou como arquivo do Project. Sem contexto, pergunte (um lote) e trabalhe com o que vier marcado; nunca invente.
- Não abra PR nem escreva em repositório. Entregue no chat. Toda sessão de trabalho termina com a lista do que deveria ser salvo e onde: `20_<frente>/<slug>/contexto.md`, `estado.md`, `decisoes.md`, `experimentos.md`, para quem tem o repositório fazer o `/salve`.
- Documento interno leva marcador; entregável de cliente, playbook publicado e slide saem sem marcador, e o que não fechou se pergunta antes.
"""


def versao_do_changelog() -> str:
    m = re.search(r"^## v(\d+\.\d+\.\d+)", (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else "0.0.0"


def sem_frontmatter(texto: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", texto, count=1, flags=re.S).lstrip("\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--destino", default=str(RAIZ / "dist" / "chat"))
    a = ap.parse_args()
    destino = Path(a.destino)
    destino.mkdir(parents=True, exist_ok=True)
    versao = versao_do_changelog()

    partes = [f"<!-- Susano {versao}: system prompt do Caminho 3, gerado por ferramentas/gerar_pacote_chat.py de modelo/00_susano/. Não editar à mão. -->\n"]
    for nome in ARQUIVOS_PROMPT:
        p = FONTE / nome
        if not p.is_file():
            print(f"ERRO: {p.relative_to(RAIZ)} ausente")
            return 1
        partes.append(sem_frontmatter(p.read_text(encoding="utf-8")).rstrip() + "\n")
    partes.append(NOTA_SEM_SHELL.lstrip("\n"))
    prompt = "\n".join(partes)
    if chr(0x2014) in prompt:
        print("ERRO: travessão no system prompt")
        return 1
    (destino / "SYSTEM_PROMPT.md").write_text(prompt, encoding="utf-8")

    zip_path = destino / "susano_conhecimento.zip"
    n = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(FONTE.rglob("*")):
            if p.is_dir() or p.name == "MANIFEST.sha256" or "__pycache__" in p.parts:
                continue
            z.write(p, Path("00_susano") / p.relative_to(FONTE))
            n += 1
    chars = len(prompt)
    print(f"pacote de chat {versao}: {destino.relative_to(RAIZ) if destino.is_relative_to(RAIZ) else destino}/")
    print(f"  SYSTEM_PROMPT.md: {chars} caracteres (cerca de {round(chars / 2.7)} tokens estimados)")
    print(f"  susano_conhecimento.zip: {n} arquivos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
