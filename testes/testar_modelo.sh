#!/usr/bin/env bash
# Aceite de versão: gera um projeto temporário a partir do modelo e roda validate, susano-check e testar_camada.
# Uso: bash testes/testar_modelo.sh [vcs-ref]   (padrão: HEAD)
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
REF="${1:-HEAD}"
TMP="$(mktemp -d)"
copier copy --defaults --quiet --vcs-ref "$REF" \
  --data org=teste --data org_nome=Teste --data frentes=clientes --data dono=dono-teste \
  "$RAIZ" "$TMP/projeto"
cd "$TMP/projeto"
git init -q -b main
git add -A
git -c user.name=teste -c user.email=teste@example.com commit -q -m "projeto gerado"
python3 scripts/brain.py validate
python3 scripts/brain.py susano-check
python3 .claude/testes/testar_camada.py .
echo "testar_modelo: OK ($TMP/projeto)"
