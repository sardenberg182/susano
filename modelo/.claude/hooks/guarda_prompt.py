#!/usr/bin/env python3
"""UserPromptSubmit do Susano: barra mensagem com segredo, cartao ou CPF (saida 2).

O travessao numa mensagem nao bloqueia: a regra de zero travessao vale para o que se grava.
Falha interna (entrada invalida, import ausente) tambem barra com saida 2, sem repetir o conteudo da mensagem.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import guardas  # dentro do main: import quebrado tambem barra (saida 2)

    entrada = json.load(sys.stdin)
    if not isinstance(entrada, dict):
        raise ValueError("entrada do hook nao e um objeto JSON")
    prompt = entrada.get("prompt") or entrada.get("user_prompt") or ""
    if not isinstance(prompt, str) or not prompt.strip():
        return 0
    achados = [a for a in guardas.bloqueios(guardas.analisar(prompt)) if not a.tipo.startswith("travessao")]
    if achados:
        tipos = ", ".join(sorted({a.tipo for a in achados}))
        print(
            f"Susano barrou a mensagem: ela contem {tipos}. Tire o dado sensivel, aponte onde ele vive "
            "(sistema e ID) e envie de novo.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(
            f"Susano: a guarda de mensagem falhou ({type(exc).__name__}) e barrou a mensagem por seguranca. "
            "Confira o Python 3.9+ e o arquivo .claude/hooks/guardas.py.",
            file=sys.stderr,
        )
        sys.exit(2)
