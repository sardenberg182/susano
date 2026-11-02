#!/usr/bin/env bash
# Aceite de versão: gera projetos temporários a partir do modelo e roda validate, susano-check, migrar e testar_camada.
# Dois projetos: o padrão (nomes curtos) e um com os campos de personalização no limite (nomes longos), que precisa
# nascer válido (orçamento de abertura com margem reservada ao projeto).
# Uso: bash testes/testar_modelo.sh [vcs-ref]   (padrão: HEAD)
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
REF="${1:-HEAD}"
TMP="$(mktemp -d)"
echo "ambiente: $(python3 --version 2>&1); $(git --version); $(copier --version 2>&1)"

gerar() {  # gerar <pasta> <org> <org_nome> <frentes> <dono>
  copier copy --defaults --quiet --vcs-ref "$REF" \
    --data "org=$2" --data "org_nome=$3" --data "frentes=$4" --data "dono=$5" "$RAIZ" "$1"
  (cd "$1" && git init -q -b main && git add -A && git -c user.name=teste -c user.email=teste@example.com commit -q -m "projeto gerado")
}

gerar "$TMP/projeto" teste Teste clientes dono-teste
cd "$TMP/projeto"
python3 scripts/brain.py validate
python3 scripts/brain.py susano-check
python3 scripts/brain.py migrar | grep -q "nada a migrar" || { echo "testar_modelo: projeto novo precisou de migrar" >&2; exit 1; }
python3 .claude/testes/testar_camada.py .

gerar "$TMP/longo" organizacao-ficticia-de-crescimento-e-receita-recorrente \
  "Organização Fictícia de Crescimento, Receita Recorrente e Operações Comerciais Integradas" \
  clientes-contas-e-produtos-estrategicos usuario-ficticio-com-nome-bem-comprido
cd "$TMP/longo"
python3 scripts/brain.py validate > "$TMP/longo_validate.txt" || { cat "$TMP/longo_validate.txt"; echo "testar_modelo: projeto com nomes longos nasceu inválido" >&2; exit 1; }
python3 scripts/brain.py susano-check > /dev/null
python3 scripts/brain.py tokens | tail -2
echo "testar_modelo: OK ($TMP/projeto, $TMP/longo)"
