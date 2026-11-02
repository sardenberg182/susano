#!/usr/bin/env bash
# Aceite de atualização: um projeto gerado numa versão suportada (padrão v0.3.0), com conteúdo próprio fictício e uma
# frente anterior ao contrato das quatro, é atualizado para a candidata (padrão HEAD) por copier update + brain.py migrar.
# Confere: conteúdo do projeto preservado, contrato novo aplicado, validate e susano-check limpos, migrar idempotente.
# Uso: bash testes/testar_atualizacao.sh [de] [para]   (padrão: v0.3.0 HEAD)
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
DE="${1:-v0.3.0}"
PARA="${2:-HEAD}"
TMP="$(mktemp -d)"
P="$TMP/projeto"
falha() { echo "testar_atualizacao: $*" >&2; exit 1; }
g() { git -c user.name=teste -c user.email=teste@example.com "$@"; }

copier copy --defaults --quiet --vcs-ref "$DE" --data org=norte --data org_nome=Norte --data frentes=clientes \
  --data dono=dono-teste "$RAIZ" "$P"
cd "$P"
g init -q -b main && g add -A && g commit -q -m "projeto em $DE"
python3 scripts/brain.py novo acme --dono dono-teste > /dev/null
printf -- '- 2026-10-28: decisão fictícia: meta de 40 SQLs/mês a partir de novembro (fonte: kickoff).\n' >> 20_clientes/acme/decisoes.md
# frente anterior ao contrato das quatro (sem experimentos.md), como as criadas antes da v0.3.0
mkdir -p 20_clientes/beta
for n in contexto estado decisoes; do
  printf -- '---\nid: %s-beta\ntipo: %s\ndono: dono-teste\natualizado: 2026-09-01\n---\n# %s: beta\n' "$n" "$n" "$n" > "20_clientes/beta/$n.md"
done
python3 - <<'PY'
from pathlib import Path
p = Path("AGENTS.md")
t = p.read_text(encoding="utf-8")
marca = "## Regras próprias de Norte"
assert marca in t, "AGENTS.md da versão de origem sem a seção Regras próprias"
p.write_text(t.split(marca)[0] + marca + "\n\n- WBR toda segunda às 9h com o dono da frente (regra local fictícia).\n", encoding="utf-8")
PY
printf '\n<!-- personalização local do template -->\n' >> _templates/estado.md
g add -A && g commit -q -m "conteúdo próprio fictício"

g switch -q -c susano-candidata
copier update --defaults --quiet --vcs-ref "$PARA" --conflict inline
python3 scripts/brain.py migrar
python3 scripts/brain.py validate > "$TMP/validate.txt" || { cat "$TMP/validate.txt"; falha "validate falhou depois do migrar"; }
python3 scripts/brain.py susano-check > "$TMP/check.txt" || { cat "$TMP/check.txt"; falha "susano-check falhou depois do migrar"; }

grep -q "decisão fictícia: meta de 40 SQLs" 20_clientes/acme/decisoes.md || falha "decisão da frente perdida"
grep -q "WBR toda segunda às 9h" AGENTS.md || falha "regra própria do AGENTS.md perdida"
grep -q "<!-- susano:inicio" AGENTS.md || falha "AGENTS.md sem o bloco gerenciado"
grep -q "personalização local do template" _templates/estado.md || falha "template personalizado sobrescrito"
test -f 20_clientes/beta/experimentos.md || falha "frente antiga sem experimentos.md"
ls 90_arquivo/AGENTS_antes_do_bloco_gerenciado_*.md > /dev/null 2>&1 || falha "AGENTS.md anterior não foi guardado em 90_arquivo/"

g add -A && g commit -q -m "susano: atualização e migrar"
antes="$(git rev-parse HEAD^{tree})"
python3 scripts/brain.py migrar | grep -q "nada a migrar" || falha "segunda execução do migrar mudou algo"
g add -A
depois="$(git write-tree)"
[ "$antes" = "$depois" ] || falha "segunda execução do migrar alterou a árvore"
echo "testar_atualizacao: OK ($DE → $PARA, $P)"
