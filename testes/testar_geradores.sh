#!/usr/bin/env bash
# Geradores idempotentes: regenerar índice, ativos, skills, manifesto e plugin a partir da fonte não pode mudar nem criar
# arquivo nenhum (git diff sozinho não vê arquivo novo: a conferência inclui os não rastreados).
# Uso: bash testes/testar_geradores.sh
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
cd "$RAIZ"
if [ -n "$(git status --porcelain --untracked-files=all)" ]; then
  echo "testar_geradores: rode com a árvore limpa (commite ou guarde as mudanças antes)." >&2
  git status --short --untracked-files=all >&2
  exit 1
fi
python3 modelo/scripts/brain.py --raiz modelo indice
python3 modelo/scripts/brain.py --raiz modelo skills
python3 modelo/scripts/brain.py --raiz modelo manifesto
python3 ferramentas/construir_plugin.py --sem-validar
if [ -n "$(git status --porcelain --untracked-files=all)" ]; then
  echo "testar_geradores: a regeneração mudou ou criou arquivos (fonte única quebrada):" >&2
  git status --short --untracked-files=all >&2
  exit 1
fi
echo "testar_geradores: OK (nada mudou nem apareceu)"
