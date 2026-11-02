#!/usr/bin/env python3
"""Gera o pacote de chat do Susano (Caminho 3, Project do claude.ai) a partir de modelo/00_susano/.

Uso, na raiz do repositório susano:  python3 ferramentas/gerar_pacote_chat.py [--destino dist/chat]

Destino suportado: Project do claude.ai (instruções do projeto + conhecimento). GPT do ChatGPT e Gem do Gemini podem
receber o mesmo pacote, mas não são testados: ficam fora da lista de destinos suportados.

Saídas (em --destino):
  INSTRUCOES_DO_PROJETO.md  núcleo adaptado ao chat (sem comandos do template) + regras do modo sem shell; vai nas
                            instruções do Project. Enxuto: identidade, situações e o resto do método vão no conhecimento.
  essencial/                operação, núcleo, identidade, DNA, instruções, exemplos e procedimentos (cabe no contexto)
  completo/                 o método inteiro (passa do contexto do Project: depende da busca automática do plano)
                            Nos dois, o nome do arquivo é o caminho achatado (dna/metodo/x.md vira dna__metodo__x.md,
                            porque o Project mostra só o nome) e MAPA_DE_ARQUIVOS.md liga cada nome ao caminho canônico.
  LEIA-ME.md                procedimento, limites com fonte e data, testes de recuperação
  LICENSE, LICENSE-CONTEUDO.md
  MANIFEST.sha256           sha256 de cada arquivo do pacote, com a versão e o commit de origem
  susano_chat_<versão>.zip  tudo acima num arquivo só

Só biblioteca padrão. Conteúdo dos arquivos do método idêntico à fonte (o teste confere byte a byte).
"""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "modelo" / "00_susano"
ESSENCIAL = ("nucleo.md", "identidade.md", "situacoes.md", "calibracao.md", "INDICE.md", "ATIVOS.md", "sobre_o_sarden.md",
             "LICENCA.md", "pendentes.md", "dna/", "instrucoes/", "exemplos/", "metodo/")
INSTRUCOES_MAX = 9000  # caracteres; teto interno, abaixo do que o Project aceita [VERIFICAR limite oficial das instruções]
P06_TEMPLATE = "Saiba qual é antes de executar (`/frente <slug>`); sem pasta, `/nova-frente` ou onboarding, nunca contexto inventado."
P06_CHAT = ("Saiba qual é antes de executar; sem contexto colado ou no conhecimento, nunca invente: ofereça a ficha da frente "
            "(`instrucoes__onboarding_frente.md`) com o lote mínimo de perguntas.")

ONDE_MORA_CHAT = """## Onde o resto mora (Project de chat)

- O método está no conhecimento deste Project. O nome de cada arquivo é o caminho achatado: `dna/metodo/x.md` vira `dna__metodo__x.md`; `MAPA_DE_ARQUIVOS.md` liga cada nome ao caminho canônico. Cite sempre o canônico: `00_susano/dna/metodo/x.md#seção`.
- Depois do núcleo: `situacoes.md` (pedido → modo → o que abrir); agir ou perguntar: `calibracao.md`; antes de produzir, o exemplo do modo (`exemplos__*.md`). Índice: `INDICE.md`; modelos ativos: `ATIVOS.md`.
- Arquivo citado que não está no conhecimento (pacote essencial): diga que não está carregado e peça para subir; nunca reconstrua de memória.

## Modo sem shell (este Project)

- Não há repositório, `brain.py`, skills, `/frente`, `/nova-frente` nem `/salve`. O contexto da frente entra colado na conversa ou como arquivo do Project; sem ele, um lote de perguntas e trabalho com o que vier marcado.
- Não escreve em lugar nenhum e não promete salvar. Toda sessão de trabalho termina com a lista do que salvar e onde: `20_<frente>/<slug>/contexto.md`, `estado.md`, `decisoes.md`, `experimentos.md` e o ledger, para quem tem o repositório fazer o `/salve`.
- Contexto de uma frente nunca entra na análise de outra, nem como exemplo.
"""


def versao_do_changelog() -> str:
    m = re.search(r"^## v(\d+\.\d+\.\d+)", (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else "0.0.0"


def commit_de_origem() -> str:
    try:
        r = subprocess.run(["git", "rev-parse", "HEAD"], cwd=RAIZ, capture_output=True, text=True, timeout=10)
        sujo = subprocess.run(["git", "status", "--porcelain", "--", "modelo/00_susano"], cwd=RAIZ, capture_output=True, text=True,
                              timeout=10).stdout.strip()
        return r.stdout.strip() + (" (com mudanças não commitadas em modelo/00_susano)" if sujo else "")
    except (OSError, subprocess.SubprocessError):
        return "?"


def achatar(rel: str) -> str:
    return rel.replace("/", "__")


def instrucoes(versao: str) -> str:
    nucleo = (FONTE / "nucleo.md").read_text(encoding="utf-8")
    nucleo = re.sub(r"\A---\n.*?\n---\n+", "", nucleo, count=1, flags=re.S)
    if P06_TEMPLATE not in nucleo:
        raise SystemExit("gerar_pacote_chat: a frase de P-06 mudou no núcleo; ajuste a adaptação do chat")
    nucleo = nucleo.replace(P06_TEMPLATE, P06_CHAT)
    ini = nucleo.index("## Onde o resto mora")
    texto = (f"<!-- Susano {versao}: instruções do Project de chat, geradas por ferramentas/gerar_pacote_chat.py de "
             "modelo/00_susano/. Não editar à mão. -->\n\n" + nucleo[:ini] + ONDE_MORA_CHAT)
    return texto


def leia_me(versao: str, origem: str, n_ess: int, n_comp: int, chars_ess: int, chars_comp: int) -> str:
    return f"""# Pacote de chat do Susano {versao}

Gerado por `ferramentas/gerar_pacote_chat.py` a partir de `modelo/00_susano/` (commit {origem}). Conteúdo sob CC BY 4.0 e código sob MIT: `LICENSE-CONTEUDO.md` e `LICENSE`. Autor: Matheus Sardenberg (Sarden).

## Destino suportado: Project do claude.ai

1. Crie um Project no claude.ai.
2. Cole `INSTRUCOES_DO_PROJETO.md` inteiro nas instruções do Project.
3. Suba para o conhecimento do Project todos os arquivos de `essencial/` ({n_ess} arquivos, {chars_ess} caracteres, cerca de {round(chars_ess / 2.7)} tokens estimados). Precisa das referências de plataforma, performance e landing page? Use `completo/` ({n_comp} arquivos, cerca de {round(chars_comp / 2.7)} tokens estimados): passa do contexto do Project e depende da busca automática do plano [VERIFICAR no plano de quem usa].
4. Faça os testes de recuperação abaixo numa conversa nova do Project e registre o resultado.

Limites conhecidos [DADO, support.claude.com, artigo "What kinds of documents can I upload to Claude?", consultado em 02/11/2026]: até 30 MB por arquivo no conhecimento do Project; número de arquivos sem limite, desde que o conteúdo total caiba no contexto; só texto é extraído (exceto PDF multimodal). O limite de tamanho das instruções do Project não está publicado na mesma página [VERIFICAR]; o gerador mantém as instruções abaixo de {INSTRUCOES_MAX} caracteres.

GPT do ChatGPT e Gem do Gemini não são destinos testados: o pacote pode funcionar, mas sem garantia de recuperação nem de formato.

## Testes de recuperação (manual, por destino)

| Pergunta numa conversa nova | O Susano precisa | Arquivo |
|---|---|---|
| "Qual é o filtro binário do diagnóstico de funil?" | responder e citar `00_susano/dna/metodo/diagnostico_de_funil.md` | `dna__metodo__diagnostico_de_funil.md` |
| "Me dá a estrutura de uma proposta para o decisor." | seguir problema → processo → prova e citar `00_susano/instrucoes/brief_e_proposta.md` | `instrucoes__brief_e_proposta.md` |
| "Analisa o funil da Cooperativa Sul." (sem contexto colado) | não inventar; oferecer a ficha da frente e o lote mínimo | `instrucoes__onboarding_frente.md` |
| "O que diz o dossiê de HubSpot sobre o Brasil?" (só com `essencial/`) | dizer que o arquivo não está carregado e pedir para subir, sem reconstruir de memória | não está no essencial |

## Integridade

`MANIFEST.sha256` lista o sha256 de cada arquivo do pacote. Os arquivos de `essencial/` e `completo/` são cópias exatas da fonte, só com o nome achatado; `MAPA_DE_ARQUIVOS.md` dá o caminho canônico de cada um.
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--destino", default=str(RAIZ / "dist" / "chat"))
    a = ap.parse_args()
    destino = Path(a.destino)
    if destino.exists():
        shutil.rmtree(destino)
    destino.mkdir(parents=True)
    versao = versao_do_changelog()
    origem = commit_de_origem()

    texto = instrucoes(versao)
    if chr(0x2014) in texto:
        print("ERRO: travessão nas instruções")
        return 1
    if len(texto) > INSTRUCOES_MAX:
        print(f"ERRO: instruções com {len(texto)} caracteres (teto {INSTRUCOES_MAX})")
        return 1
    (destino / "INSTRUCOES_DO_PROJETO.md").write_text(texto, encoding="utf-8")

    fontes = sorted(p for p in FONTE.rglob("*") if p.is_file() and p.name != "MANIFEST.sha256" and "__pycache__" not in p.parts)
    contagem = {}
    for pacote in ("essencial", "completo"):
        pasta = destino / pacote
        pasta.mkdir()
        linhas = [f"# Mapa de arquivos ({pacote}, Susano {versao})", "",
                  "Nome no conhecimento do Project → caminho canônico no método (cite o canônico).", "",
                  "| Arquivo | Caminho canônico |", "|---|---|"]
        n = chars = 0
        for p in fontes:
            rel = p.relative_to(FONTE).as_posix()
            if pacote == "essencial" and not any(rel == e or (e.endswith("/") and rel.startswith(e)) for e in ESSENCIAL):
                continue
            plano = achatar(rel)
            if (pasta / plano).exists():
                print(f"ERRO: nome achatado repetido: {plano}")
                return 1
            shutil.copyfile(p, pasta / plano)
            linhas.append(f"| `{plano}` | `00_susano/{rel}` |")
            n += 1
            chars += len(p.read_text(encoding="utf-8", errors="replace"))
        (pasta / "MAPA_DE_ARQUIVOS.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
        contagem[pacote] = (n, chars)
    (n_ess, chars_ess), (n_comp, chars_comp) = contagem["essencial"], contagem["completo"]
    (destino / "LEIA-ME.md").write_text(leia_me(versao, origem, n_ess, n_comp, chars_ess, chars_comp), encoding="utf-8")
    shutil.copy2(RAIZ / "LICENSE", destino / "LICENSE")
    shutil.copy2(RAIZ / "LICENSE-CONTEUDO.md", destino / "LICENSE-CONTEUDO.md")

    arquivos = sorted(p for p in destino.rglob("*") if p.is_file())
    manifesto = [f"# Susano {versao}, pacote de chat; origem {origem}"]
    manifesto += [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(destino).as_posix()}" for p in arquivos]
    (destino / "MANIFEST.sha256").write_text("\n".join(manifesto) + "\n", encoding="utf-8")
    zip_path = destino / f"susano_chat_{versao}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(x for x in destino.rglob("*") if x.is_file() and x != zip_path):
            z.write(p, p.relative_to(destino).as_posix())
    print(f"pacote de chat {versao}: {destino}")
    print(f"  INSTRUCOES_DO_PROJETO.md: {len(texto)} caracteres (teto {INSTRUCOES_MAX}; cerca de {round(len(texto) / 2.7)} tokens estimados)")
    print(f"  essencial/: {contagem['essencial'][0]} arquivos, cerca de {round(contagem['essencial'][1] / 2.7)} tokens estimados")
    print(f"  completo/: {contagem['completo'][0]} arquivos, cerca de {round(contagem['completo'][1] / 2.7)} tokens estimados")
    print(f"  {zip_path.name}: {len(arquivos)} arquivos + MANIFEST.sha256")
    return 0


if __name__ == "__main__":
    sys.exit(main())
