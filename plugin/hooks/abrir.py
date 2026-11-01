#!/usr/bin/env python3
"""SessionStart do plugin susano: imprime o núcleo da sombra. Texto puro vira contexto da sessão (hooks do Claude Code).

Nunca bloqueia: falha vira uma linha de aviso. Única carga sempre ligada do plugin (cerca de 2 mil tokens).
"""
import os
import sys
from pathlib import Path


def main() -> int:
    raiz = Path(os.environ.get("CLAUDE_PLUGIN_ROOT") or Path(__file__).resolve().parent.parent).resolve()
    nucleo = raiz / "00_susano" / "nucleo.md"
    texto = nucleo.read_text(encoding="utf-8").replace("${CLAUDE_PLUGIN_ROOT}/", str(raiz) + "/")
    print("[SUSANO] Núcleo do método Sarden, instalado pelo plugin susano a pedido do usuário. Fonte: " + str(nucleo))
    print(texto)
    print("[SUSANO] Estilo de saída opcional: /output-style Susano. O método completo mora em " + str(raiz / "00_susano") + ".")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # nunca derrubar a abertura da sessão
        print("[SUSANO] hook de abertura falhou: " + str(exc))
        sys.exit(0)
