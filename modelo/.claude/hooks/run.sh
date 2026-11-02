#!/usr/bin/env bash
# Escolhe um Python 3.9+ disponivel e executa o script do hook, preservando o codigo de saida.
# Uso: bash run.sh [--bloqueante] <script.py> [argumentos]
# Sem Python: sai 1 (erro nao bloqueante: abertura de sessao, informativa) ou, com --bloqueante, sai 2
# (trava de privacidade: o Claude Code barra a escrita ou a mensagem em vez de liberar sem checar).
bloqueante=0
if [ "${1:-}" = "--bloqueante" ]; then
  bloqueante=1
  shift
fi
for candidato in python3 python py; do
  if command -v "$candidato" >/dev/null 2>&1; then
    if "$candidato" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' >/dev/null 2>&1; then
      exec "$candidato" "$@"
    fi
  fi
done
if [ "$bloqueante" = 1 ]; then
  echo "Susano: Python 3.9+ nao encontrado; a trava de privacidade nao pode rodar, entao a acao foi barrada. Instale o Python 3.9+ e tente de novo." >&2
  exit 2
fi
echo "Susano: Python 3.9+ nao encontrado; abertura sem o contexto do repositorio (as travas de escrita barram ate o Python voltar)." >&2
exit 1
