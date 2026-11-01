#!/usr/bin/env bash
# Instala um pre-commit local que roda a validacao do repositorio (scripts/brain.py validate). Idempotente.
# Uso, na raiz do repositorio: bash .claude/hooks/instalar_precommit.sh
set -euo pipefail

raiz="$(git rev-parse --show-toplevel)"
hook="$(git rev-parse --git-path hooks)/pre-commit"
case "$hook" in /*) ;; *) hook="$raiz/$hook" ;; esac
marca="# susano-precommit"

if [ ! -f "$raiz/scripts/brain.py" ]; then
  echo "scripts/brain.py nao encontrado: rode na raiz do repositorio." >&2
  exit 1
fi
if [ -f "$hook" ] && grep -q "$marca" "$hook"; then
  echo "pre-commit do Susano ja instalado em $hook"
  exit 0
fi
if [ -f "$hook" ]; then
  cp "$hook" "$hook.antes-susano"
  echo "pre-commit anterior guardado em $hook.antes-susano"
fi
mkdir -p "$(dirname "$hook")"
cat > "$hook" <<'HOOK'
#!/usr/bin/env bash
# susano-precommit
raiz="$(git rev-parse --show-toplevel)"
exec bash "$raiz/.claude/hooks/run.sh" "$raiz/scripts/brain.py" validate
HOOK
chmod +x "$hook"
echo "pre-commit instalado: roda 'scripts/brain.py validate' antes de cada commit."
