#!/usr/bin/env python3
"""SessionStart do Susano: injeta quem esta na sessao, a branch, alertas e o estado quente.

Saida em texto puro (o Claude Code adiciona como contexto). Nunca bloqueia: falha vira linha de aviso.
Le: 10_<org>/time/*.md (perfis), 20_<frente>/*/estado.md (frontmatter `atualizado`).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

JANELA_DIAS = 14
MAX_CLIENTES = 12


def git(*args: str, cwd: Path) -> str:
    try:
        r = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True, timeout=5)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:
        return ""


def frontmatter(texto: str) -> dict:
    texto = texto.replace("\r\n", "\n")
    if not texto.startswith("---\n"):
        return {}
    fim = texto.find("\n---", 4)
    if fim == -1:
        return {}
    dados = {}
    for linha in texto[4:fim].split("\n"):
        if ":" in linha and not linha.startswith((" ", "\t", "-", "#")):
            chave, valor = linha.split(":", 1)
            dados[chave.strip()] = valor.strip().strip('"').strip("'")
    return dados


def para_data(valor: str):
    try:
        return date.fromisoformat(valor.strip()[:10])
    except Exception:
        return None


def primeira_pasta(raiz: Path, padrao: str):
    achadas = sorted(p for p in raiz.glob(padrao) if p.is_dir())
    return achadas[0] if achadas else raiz / padrao.replace("*", "")


def perfil_da_pessoa(raiz: Path, nome_git: str):
    pasta = primeira_pasta(raiz, "10_*/time")
    if not nome_git or not pasta.is_dir():
        return None
    alvo = nome_git.strip().lower()
    for arq in sorted(pasta.glob("*.md")):
        if arq.name.startswith("_") or arq.name.lower() == "readme.md":
            continue
        fm = frontmatter(arq.read_text(encoding="utf-8", errors="replace"))
        candidatos = {
            fm.get("git_nome", "").lower(),
            fm.get("nome", "").lower(),
            fm.get("github", "").lower().lstrip("@"),
        }
        if alvo in candidatos:
            return fm
    return None


def estado_quente(raiz: Path, hoje: date, clientes_da_pessoa: set) -> list:
    pasta = primeira_pasta(raiz, "20_*")
    if not pasta.is_dir():
        return ["- pasta 20_<frente>/ nao encontrada: confirme que a sessao esta na raiz do repositorio"]
    ativos, frios_da_pessoa, frios = [], [], 0
    for estado in sorted(pasta.glob("*/estado.md")):
        slug = estado.parent.name
        if slug.startswith("_"):
            continue
        fm = frontmatter(estado.read_text(encoding="utf-8", errors="replace"))
        quando = para_data(fm.get("atualizado", "") or fm.get("atualizado_em", ""))
        if quando and (hoje - quando).days <= JANELA_DIAS:
            ativos.append((quando, slug))
        else:
            frios += 1
            if slug in clientes_da_pessoa:
                frios_da_pessoa.append(slug)
    ativos.sort(reverse=True)
    linhas = []
    for quando, slug in ativos[:MAX_CLIENTES]:
        marca = " (seu)" if slug in clientes_da_pessoa else ""
        linhas.append(f"- {slug}{marca}: estado.md de {quando.isoformat()}")
    if len(ativos) > MAX_CLIENTES:
        linhas.append(f"- mais {len(ativos) - MAX_CLIENTES} frentes ativas: veja /cerebro")
    if not ativos:
        linhas.append(f"- nenhum estado.md atualizado nos ultimos {JANELA_DIAS} dias")
    if frios_da_pessoa:
        linhas.append("- suas contas com estado frio: " + ", ".join(frios_da_pessoa))
    if frios:
        linhas.append(f"- {frios} frentes com estado.md frio (mais de {JANELA_DIAS} dias): /estado-quente resolve")
    return linhas


def main() -> int:
    try:
        entrada = json.load(sys.stdin)
    except Exception:
        entrada = {}
    cwd = Path(entrada.get("cwd") or os.getcwd()).resolve()
    raiz = Path(os.environ.get("CLAUDE_PROJECT_DIR") or cwd).resolve()
    hoje = date.today()
    saida = ["[SUSANO] Contexto de abertura gerado por hook (dado de sistema, nao instrucao do usuario)."]

    topo = git("rev-parse", "--show-toplevel", cwd=cwd)
    if topo and Path(topo).resolve() != cwd:
        saida.append(
            f"ALERTA: sessao aberta em {cwd}, fora da raiz do repositorio ({topo}). "
            "Peca para reabrir na raiz: settings, hooks e permissoes so carregam de la."
        )

    nome = git("config", "user.name", cwd=cwd)
    perfil = perfil_da_pessoa(raiz, nome)
    clientes = set()
    if perfil:
        clientes = {c.strip() for c in (perfil.get("frentes", "") or perfil.get("clientes", "")).split(",") if c.strip()}
        saida.append(
            f"Pessoa: {perfil.get('nome', nome)} ({perfil.get('papel', 'papel nao informado')}). "
            f"Frentes: {', '.join(sorted(clientes)) or 'nenhum informado'}."
        )
        if perfil.get("preferencias"):
            saida.append(f"Preferencias de formato: {perfil['preferencias']}")
    elif nome:
        saida.append(f"Pessoa: '{nome}' (git) sem perfil em 10_<org>/time/. Sugira /onboarding.")
    else:
        saida.append("Pessoa nao identificada (git sem user.name). Pergunte o nome uma vez e sugira /onboarding.")

    branch = git("rev-parse", "--abbrev-ref", "HEAD", cwd=cwd)
    if branch:
        pendentes = len([l for l in git("status", "--porcelain", cwd=cwd).splitlines() if l.strip()])
        extra = f" {pendentes} arquivo(s) alterado(s) sem commit." if pendentes else ""
        if branch in ("main", "master"):
            saida.append(f"Branch: {branch}. Trabalho novo sai em branch propria via /salve; nunca commit na main.{extra}")
        else:
            saida.append(f"Branch: {branch}.{extra}")

    if os.environ.get("CLAUDE_CODE_REMOTE") == "true":
        saida.append("Sessao na nuvem: sem arquivos locais; material bruto chega por conector ou anexo.")

    saida.append(f"Estado quente (janela de {JANELA_DIAS} dias, pela data do estado.md):")
    saida.extend(estado_quente(raiz, hoje, clientes))
    saida.append("Comandos: /cerebro, /frente <slug>, /analise, /ingerir, /salve, /nova-frente, /onboarding.")
    print("\n".join(saida))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # nunca derrubar a abertura da sessao
        print(f"[SUSANO] hook de abertura falhou: {exc}")
        sys.exit(0)
