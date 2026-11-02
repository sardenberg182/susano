#!/usr/bin/env bash
# Aceite do plugin: reconstrói plugin/ e o catálogo, confere que nada mudou nem apareceu (fonte única), roda o hook de
# abertura em caminhos de instalação diferentes (curto, longo, com espaço, com acento) e confere componentes e manifestos.
# Uso: bash testes/testar_plugin.sh [--org <owner>]
# SUSANO_EXIGIR_CLI=1: sem o claude CLI, o aceite falha (no CI de release, checagem pulada não é aprovação).
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
cd "$RAIZ"
python3 ferramentas/construir_plugin.py "$@"
if [ -n "$(git status --porcelain --untracked-files=all -- plugin .claude-plugin)" ]; then
  echo "testar_plugin: plugin/ ou .claude-plugin/ diferem do commit (arquivo mudado ou novo); reconstrua e commite (fonte única)." >&2
  git status --short --untracked-files=all -- plugin .claude-plugin >&2
  exit 1
fi
if [ "${SUSANO_EXIGIR_CLI:-0}" = 1 ] && ! command -v claude >/dev/null 2>&1; then
  echo "testar_plugin: SUSANO_EXIGIR_CLI=1 e o claude CLI não está instalado: a validação nativa do manifesto não rodou." >&2
  exit 1
fi
python3 - <<'EOF'
import json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, "modelo/scripts")
import brain

PLUGIN = Path("plugin").resolve()
erros = []

# 1. orçamento do núcleo canônico do plugin, medido antes de qualquer caminho local (tokens estimados)
nucleo = (PLUGIN / "00_susano" / "nucleo.md").read_text(encoding="utf-8")
n = brain.estimar_tokens(nucleo)
if n > brain.NUCLEO_TOKENS_MAX:
    erros.append(f"núcleo do plugin com {n} tokens estimados (teto {brain.NUCLEO_TOKENS_MAX})")
if not nucleo.startswith("# Susano: núcleo da sombra"):
    erros.append("núcleo do plugin não começa pelo título (frontmatter sobrando?)")

# 2. hook de abertura em quatro caminhos de instalação: mesmo resultado, sem variável crua, caminhos que existem
tmp = Path(tempfile.mkdtemp(prefix="susano_plugin_"))
raizes = [tmp / "p", tmp / ("instalacao-" + "x" * 80) / "plugin", tmp / "com espaço" / "plugin", tmp / "ação ênfase ç" / "plugin"]
normalizadas = []
for raiz in raizes:
    shutil.copytree(PLUGIN, raiz)
    r = subprocess.run([sys.executable, str(raiz / "hooks" / "abrir.py")], capture_output=True, text=True,
                       env=dict(os.environ, CLAUDE_PLUGIN_ROOT=str(raiz)), timeout=30)
    saida = r.stdout
    if r.returncode != 0:
        erros.append(f"hook saiu {r.returncode} em {raiz}")
    for marca in ("P-01 Nunca alucina", "Tom: o do Sarden", "onboarding_frente.md"):
        if marca not in saida:
            erros.append(f"hook sem '{marca}' em {raiz}")
    if "${CLAUDE_PLUGIN_ROOT}" in saida:
        erros.append(f"variável não substituída na saída do hook em {raiz}")
    for caminho in re.findall(re.escape(str(raiz)) + r"(/[^\s`)]*)", saida):
        alvo = Path(str(raiz) + caminho.rstrip(".,;:"))
        if caminho.strip("/") and not alvo.exists():
            erros.append(f"hook aponta para {alvo}, que não existe")
    normalizadas.append(saida.replace(str(raiz), "<RAIZ>"))
if len(set(normalizadas)) != 1:
    erros.append("saída do hook muda com o caminho de instalação (além do próprio caminho)")
LIMITE = 6500
if len(normalizadas[0]) > LIMITE:
    erros.append(f"saída do hook com {len(normalizadas[0])} caracteres sem o caminho local (teto {LIMITE})")

# 3. componentes: as 10 skills, o subagente, o estilo, licenças, README e o hook
skills = ["ativos", "metodo", "biblioteca", "performance", "analytics", "gtm", "plataformas", "rituais", "exemplos", "analise"]
for s in skills:
    p = PLUGIN / "skills" / f"susano-{s}" / "SKILL.md"
    fm = brain.frontmatter(p.read_text(encoding="utf-8")) if p.is_file() else {}
    if fm.get("name") != f"susano-{s}" or not fm.get("description"):
        erros.append(f"skill susano-{s} ausente ou sem name/description")
existentes = sorted(p.parent.name for p in (PLUGIN / "skills").glob("*/SKILL.md"))
if existentes != sorted(f"susano-{s}" for s in skills):
    erros.append(f"skills do plugin diferem do esperado: {existentes}")
for rel in ("agents/pesquisador.md", "output-styles/susano.md", "hooks/abrir.py", "hooks/hooks.json", "LICENSE",
            "LICENSE-CONTEUDO.md", "README.md", "00_susano/INDICE.md", "00_susano/situacoes.md", "00_susano/instrucoes/onboarding_frente.md"):
    if not (PLUGIN / rel).is_file():
        erros.append(f"plugin sem {rel}")

# 4. manifestos
m = json.loads(Path(".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
p = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
h = json.loads((PLUGIN / "hooks" / "hooks.json").read_text(encoding="utf-8"))
if not (m["name"] == "susano" and m["plugins"][0]["source"] == "./plugin" and m["plugins"][0]["name"] == "susano"):
    erros.append(f"marketplace.json inesperado: {m}")
if not (p["name"] == "susano" and p["version"]):
    erros.append(f"plugin.json inesperado: {p}")
if list(h["hooks"]) != ["SessionStart"]:
    erros.append(f"hooks.json inesperado: {h}")

for e in erros:
    print("ERRO  " + e)
print(f"plugin {p['version']}: núcleo {n} tokens estimados; hook com {len(normalizadas[0])} caracteres sem o caminho, "
      f"igual nos {len(raizes)} caminhos; {len(existentes)} skills")
sys.exit(1 if erros else 0)
EOF
echo "testar_plugin: OK"
