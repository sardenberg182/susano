#!/usr/bin/env bash
# Aceite do pacote de chat (Project do claude.ai): gera numa pasta temporária e confere arquivos esperados, integridade do
# ZIP e do MANIFEST, igualdade byte a byte com a fonte, licenças, tamanho das instruções e privacidade (perfil público),
# inclusive um segredo fictício plantado dentro de uma cópia do ZIP. A recuperação no produto é teste manual (LEIA-ME.md).
# Uso: bash testes/testar_pacote_chat.sh
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
cd "$RAIZ"
TMP="$(mktemp -d)"
python3 ferramentas/gerar_pacote_chat.py --destino "$TMP/chat"
python3 - "$TMP/chat" <<'PY'
import hashlib, re, sys, zipfile
from pathlib import Path
destino, fonte, raiz = Path(sys.argv[1]), Path("modelo/00_susano"), Path(".")
erros = []
for nome in ("INSTRUCOES_DO_PROJETO.md", "LEIA-ME.md", "LICENSE", "LICENSE-CONTEUDO.md", "MANIFEST.sha256",
             "essencial/MAPA_DE_ARQUIVOS.md", "completo/MAPA_DE_ARQUIVOS.md"):
    if not (destino / nome).is_file():
        erros.append(f"falta {nome}")
for lic in ("LICENSE", "LICENSE-CONTEUDO.md"):
    if (destino / lic).read_bytes() != (raiz / lic).read_bytes():
        erros.append(f"{lic} diferente da raiz")
texto = (destino / "INSTRUCOES_DO_PROJETO.md").read_text(encoding="utf-8")
if len(texto) > 9000 or chr(0x2014) in texto or "Modo sem shell" not in texto or "P-01 Nunca alucina" not in texto:
    erros.append("instruções fora do contrato (tamanho, travessão, núcleo ou modo sem shell)")
if "`/frente <slug>`" in texto or "scripts/brain.py" in texto:
    erros.append("instruções do chat citam comando do template")
todos = {p.relative_to(fonte).as_posix() for p in fonte.rglob("*") if p.is_file() and p.name != "MANIFEST.sha256" and "__pycache__" not in p.parts}
for pacote in ("essencial", "completo"):
    mapa = dict(re.findall(r"^\| `([^`]+)` \| `00_susano/([^`]+)` \|$", (destino / pacote / "MAPA_DE_ARQUIVOS.md").read_text(encoding="utf-8"), re.M))
    presentes = {p.name for p in (destino / pacote).iterdir() if p.name != "MAPA_DE_ARQUIVOS.md"}
    if presentes != set(mapa):
        erros.append(f"{pacote}: arquivos e mapa não batem ({len(presentes)} contra {len(mapa)})")
    for plano, rel in mapa.items():
        if (destino / pacote / plano).read_bytes() != (fonte / rel).read_bytes():
            erros.append(f"{pacote}/{plano} diferente da fonte {rel}")
    if pacote == "completo" and set(mapa.values()) != todos:
        erros.append("completo/ não tem todo o método")
    if pacote == "essencial" and not {"nucleo.md", "situacoes.md", "calibracao.md", "instrucoes/onboarding_frente.md"} <= set(mapa.values()):
        erros.append("essencial/ sem os arquivos de operação")
linhas = [l for l in (destino / "MANIFEST.sha256").read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]
for l in linhas:
    h, rel = l.split("  ", 1)
    if hashlib.sha256((destino / rel).read_bytes()).hexdigest() != h:
        erros.append(f"MANIFEST não bate em {rel}")
zips = list(destino.glob("susano_chat_*.zip"))
if len(zips) != 1:
    erros.append("ZIP do pacote ausente ou repetido")
else:
    with zipfile.ZipFile(zips[0]) as z:
        if z.testzip() is not None:
            erros.append("ZIP corrompido")
        nomes = set(z.namelist())
        esperados = {p.relative_to(destino).as_posix() for p in destino.rglob("*") if p.is_file() and p != zips[0]}
        if nomes != esperados:
            erros.append(f"ZIP não tem exatamente os arquivos do pacote ({len(nomes)} contra {len(esperados)})")
for e in erros:
    print("ERRO  " + e)
print(f"pacote de chat: {len(linhas)} arquivos no MANIFEST; instruções com {len(texto)} caracteres")
sys.exit(1 if erros else 0)
PY
python3 modelo/scripts/brain.py --raiz . varrer --perfil publico "$TMP/chat"
# negativo: segredo fictício plantado numa cópia do ZIP precisa ser pego antes da publicação
python3 - "$TMP" <<'PY'
import sys, zipfile, shutil
from pathlib import Path
tmp = Path(sys.argv[1])
original = next((tmp / "chat").glob("susano_chat_*.zip"))
(tmp / "plantado").mkdir()
copia = tmp / "plantado" / original.name
shutil.copy2(original, copia)
with zipfile.ZipFile(copia, "a") as z:
    z.writestr("essencial/plantado.md", "chave " + "gh" + "p_" + "Z9y8X7w6V5u4T3s2R1q0P9o8N7m6L5k4J3i2" + "\n")
PY
if python3 modelo/scripts/brain.py --raiz . varrer --perfil publico "$TMP/plantado" > "$TMP/plantado.txt"; then
  cat "$TMP/plantado.txt"; echo "testar_pacote_chat: segredo plantado no ZIP passou pela inspeção" >&2; exit 1
fi
grep -q "plantado.md:1: token GitHub" "$TMP/plantado.txt" || { cat "$TMP/plantado.txt"; echo "testar_pacote_chat: achado sem regra ou local" >&2; exit 1; }
echo "testar_pacote_chat: OK ($TMP/chat)"
