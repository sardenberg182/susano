#!/usr/bin/env bash
# Aceite do plugin: reconstrói plugin/ e o catálogo, confere o hook de abertura e valida os manifestos.
# Uso: bash testes/testar_plugin.sh [--org <owner>]
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
cd "$RAIZ"
python3 ferramentas/construir_plugin.py "$@"
if ! git diff --quiet -- plugin .claude-plugin 2>/dev/null; then
  echo "testar_plugin: plugin/ ou .claude-plugin/ diferem do que está commitado; reconstrua e commite (fonte única)." >&2
  git status --short -- plugin .claude-plugin >&2
  exit 1
fi
saida="$(CLAUDE_PLUGIN_ROOT="$RAIZ/plugin" python3 plugin/hooks/abrir.py)"
grep -q "P-01 Nunca alucina" <<<"$saida" || { echo "testar_plugin: hook de abertura sem o núcleo" >&2; exit 1; }
grep -q "Tom: o do Sarden" <<<"$saida" || { echo "testar_plugin: hook de abertura sem a seção de tom" >&2; exit 1; }
grep -q '\${CLAUDE_PLUGIN_ROOT}' <<<"$saida" && { echo "testar_plugin: variável não substituída na saída do hook" >&2; exit 1; }
test "$(printf '%s' "$saida" | wc -c)" -le 6500 || { echo "testar_plugin: saída do hook acima de 6500 caracteres" >&2; exit 1; }
for s in ativos metodo biblioteca performance analytics gtm plataformas rituais analise; do
  test -f "plugin/skills/susano-$s/SKILL.md" || { echo "testar_plugin: falta a skill susano-$s" >&2; exit 1; }
done
python3 - <<'EOF'
import json, pathlib
m = json.loads(pathlib.Path(".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
p = json.loads(pathlib.Path("plugin/.claude-plugin/plugin.json").read_text(encoding="utf-8"))
assert m["name"] == "susano" and m["plugins"][0]["source"] == "./plugin" and m["plugins"][0]["name"] == "susano", m
assert p["name"] == "susano" and p["version"], p
h = json.loads(pathlib.Path("plugin/hooks/hooks.json").read_text(encoding="utf-8"))
assert list(h["hooks"]) == ["SessionStart"], h
print("manifestos: OK (plugin %s)" % p["version"])
EOF
echo "testar_plugin: OK"
