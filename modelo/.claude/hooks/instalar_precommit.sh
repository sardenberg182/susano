#!/usr/bin/env bash
# Instala um pre-commit local que inspeciona a versao que vai para o commit (indice do Git, nao o disco) e roda a
# validacao do repositorio. Hook anterior e preservado e continua rodando antes; a falha dele barra o commit.
# Idempotente: reinstalar nao muda nem multiplica a cadeia.
# Uso, na raiz do repositorio: bash .claude/hooks/instalar_precommit.sh
set -euo pipefail

raiz="$(git rev-parse --show-toplevel)"
hook="$(git rev-parse --git-path hooks)/pre-commit"
case "$hook" in /*) ;; *) hook="$raiz/$hook" ;; esac
anterior="$hook.antes-susano"
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
  if [ -e "$anterior" ]; then
    echo "Ja existe $anterior e o pre-commit atual nao e o do Susano: junte os dois a mao (ou use um gerenciador de hooks) para nao perder nenhuma checagem." >&2
    exit 1
  fi
  mv "$hook" "$anterior"
  chmod +x "$anterior"
  echo "pre-commit anterior preservado em $anterior: ele roda antes do Susano e a falha dele barra o commit."
fi
mkdir -p "$(dirname "$hook")"
cat > "$hook" <<'HOOK'
#!/usr/bin/env bash
# susano-precommit
# 1) hook anterior, se havia; 2) privacidade do que vai para o commit (indice); 3) validacao do repositorio.
raiz="$(git rev-parse --show-toplevel)"
anterior="$(git rev-parse --git-path hooks)/pre-commit.antes-susano"
case "$anterior" in /*) ;; *) anterior="$raiz/$anterior" ;; esac
if [ -x "$anterior" ]; then
  "$anterior" "$@" || { echo "pre-commit anterior (pre-commit.antes-susano) falhou: commit barrado." >&2; exit 1; }
fi
bash "$raiz/.claude/hooks/run.sh" --bloqueante "$raiz/scripts/brain.py" varrer --staged || exit 1
exec bash "$raiz/.claude/hooks/run.sh" --bloqueante "$raiz/scripts/brain.py" validate
HOOK
chmod +x "$hook"
echo "pre-commit instalado: inspeciona o indice do Git (brain.py varrer --staged) e roda brain.py validate antes de cada commit."
