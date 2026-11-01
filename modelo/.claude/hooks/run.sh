#!/usr/bin/env bash
# Escolhe um Python 3.9+ disponivel e executa o script do hook, preservando o codigo de saida.
# Sem Python: sai com 1 (erro nao bloqueante para hooks do Claude Code; o CI continua validando).
for candidato in python3 python py; do
  if command -v "$candidato" >/dev/null 2>&1; then
    if "$candidato" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' >/dev/null 2>&1; then
      exec "$candidato" "$@"
    fi
  fi
done
echo "Susano: Python 3.9+ nao encontrado; checagem local ignorada (o CI do GitHub segue validando)." >&2
exit 1
