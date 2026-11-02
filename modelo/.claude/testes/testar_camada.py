#!/usr/bin/env python3
"""Testes do motor Susano sobre uma cópia do projeto gerado pelo modelo.

Uso: python3 .claude/testes/testar_camada.py <raiz-do-projeto>   (na raiz: ".")
Copia o projeto para uma pasta temporária (sem .git), cria frentes e um perfil fictícios
e exercita hooks, settings, brain.py (validate, susano-check, novo, audit) e o pre-commit.
Imprime PASS/FAIL por caso. Os dados de teste são fictícios.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path

ORIGEM = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
resultados = []


def caso(nome: str, ok: bool, detalhe: str = "") -> None:
    resultados.append((nome, ok))
    print(("PASS " if ok else "FAIL ") + nome + (f"  [{detalhe}]" if detalhe and not ok else ""))


def rodar(cmd, cwd, entrada=None, env=None):
    e = dict(os.environ)
    if env:
        e.update(env)
    r = subprocess.run(cmd, cwd=str(cwd), input=entrada, capture_output=True, text=True, env=e, timeout=120)
    return r.returncode, r.stdout, r.stderr


def escrever(p: Path, texto: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texto, encoding="utf-8")


def datar(estado: Path, quando: str) -> None:
    t = estado.read_text(encoding="utf-8")
    estado.write_text(re.sub(r"^atualizado: .*$", f"atualizado: {quando}", t, count=1, flags=re.M), encoding="utf-8")


def cpf_valido_gerado() -> str:
    base = [5, 2, 9, 9, 8, 2, 2, 4, 7]
    for pos in (9, 10):
        soma = sum(base[i] * ((pos + 1) - i) for i in range(pos))
        dig = (soma * 10) % 11
        base.append(0 if dig == 10 else dig)
    d = "".join(map(str, base))
    return f"{d[:3]}.{d[3:6]}.{d[6:9]}-{d[9:]}"


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="susano_teste_"))
    repo = tmp / "projeto"
    shutil.copytree(ORIGEM, repo, ignore=shutil.ignore_patterns(".git", "__pycache__", "settings.local.json"))
    hoje = date.today()
    recente = (hoje - timedelta(days=3)).isoformat()
    antigo = (hoje - timedelta(days=40)).isoformat()
    brain = [sys.executable, "scripts/brain.py"]

    rodar(["git", "init", "-q", "-b", "main"], repo)
    rodar(["git", "config", "user.name", "Pessoa Teste"], repo)
    rodar(["git", "config", "user.email", "pessoa@example.com"], repo)

    # 0. brain.py no projeto recém-gerado
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(brain + ["validate"], repo)
    caso("brain.py validate: projeto gerado passa", code == 0, (out + err)[-300:])
    code, out, err = rodar(brain + ["susano-check"], repo)
    caso("brain.py susano-check: gerenciados iguais ao MANIFEST", code == 0, (out + err)[-300:])

    # frentes e perfil fictícios
    frentes = sorted(p for p in repo.glob("20_*") if p.is_dir())
    time_dir = sorted(p for p in repo.glob("10_*/time") if p.is_dir())
    caso("estrutura: pastas 10_<org>/time e 20_<frente> existem", bool(frentes) and bool(time_dir))
    if not frentes or not time_dir:
        return 1
    pasta_frentes = frentes[0]
    for slug in ("acme", "beta-labs", "gama"):
        code, out, err = rodar(brain + ["novo", slug, "--dono", "pessoa-teste"], repo)
    caso("brain.py novo: cria a frente com contexto, estado, decisoes e experimentos",
         code == 0 and all((pasta_frentes / "gama" / n).is_file() for n in ("contexto.md", "estado.md", "decisoes.md", "experimentos.md")),
         (out + err)[-200:])
    exp = (pasta_frentes / "gama" / "experimentos.md").read_text(encoding="utf-8") if (pasta_frentes / "gama" / "experimentos.md").is_file() else ""
    caso("experimentos.md: nasce com frontmatter (tipo experimentos) e a tabela E-NN", exp.startswith("---\nid: experimentos-gama\ntipo: experimentos") and "| E-NN |" in exp, exp[:120])
    datar(pasta_frentes / "acme" / "estado.md", recente)
    datar(pasta_frentes / "beta-labs" / "estado.md", antigo)
    datar(pasta_frentes / "gama" / "estado.md", recente)
    escrever(time_dir[0] / "pessoa-teste.md",
             "---\nnome: Pessoa Teste\npapel: Growth Leader\ngithub: pessoa-teste\ngit_nome: Pessoa Teste\n"
             "frentes: acme, beta-labs\npreferencias: respostas curtas\natualizado: 2026-10-31\n---\n# Pessoa Teste\n")
    rodar(["git", "add", "-A"], repo)
    rodar(["git", "commit", "-q", "-m", "base"], repo)
    code, out, err = rodar(brain + ["validate"], repo)
    caso("brain.py validate: passa com frentes criadas pelo novo", code == 0, (out + err)[-300:])
    code, out, _ = rodar(brain + ["audit"], repo)
    caso("brain.py audit: aponta o estado frio", code == 0 and "estado frio" in out and "beta-labs" in out)

    # 0b. v0.2.0: núcleo, carga de abertura, mapa, hot, fonte, pessoas, skills por domínio
    org_dir = time_dir[0].parent
    nucleo = repo / "00_susano" / "nucleo.md"
    caso("nucleo.md: existe e cabe em 2 mil tokens estimados (3 caracteres por token)",
         nucleo.is_file() and len(nucleo.read_text(encoding="utf-8")) <= 2000 * 3,
         f"{len(nucleo.read_text(encoding='utf-8')) if nucleo.is_file() else 0} caracteres")
    claude_md = (repo / "CLAUDE.md").read_text(encoding="utf-8")
    caso("CLAUDE.md: importa o núcleo e não o ATIVOS", "@00_susano/nucleo.md" in claude_md and "@00_susano/ATIVOS.md" not in claude_md)
    code, out, err = rodar(brain + ["tokens"], repo)
    m = re.search(r"abertura: (\d+) tokens estimados \(teto (\d+)", out)
    caso("brain.py tokens: carga de abertura estimada dentro do teto (8 mil)",
         code == 0 and m is not None and int(m.group(1)) <= int(m.group(2)) <= 8000, (out + err)[-200:])
    code, out, err = rodar(brain + ["mapa"], repo)
    mapa = (repo / "MAPA.md").read_text(encoding="utf-8") if (repo / "MAPA.md").is_file() else ""
    caso("brain.py mapa: gera MAPA.md com as frentes, dono e situação",
         code == 0 and "| `acme` | @pessoa-teste |" in mapa and "quente" in mapa and "frio (" in mapa, (out + err)[-200:])
    escrever(pasta_frentes / "acme" / "estado.md",
             f"---\nid: estado-acme\ntipo: estado\ndono: pessoa-teste\natualizado: {recente}\n---\n# Estado: acme\n\n"
             "## Aberto agora\n\n- Reestruturar o funil de inbound (ref: ledger/2026-10-28.md)\n\n## Fechado nos últimos 14 dias\n\n"
             "## Próximos prazos\n\n- 2026-11-10: WBR com a diretoria\n\n## Riscos e alertas\n")
    code, out, err = rodar(brain + ["hot"], repo)
    hot = org_dir / "hot.md"
    hot_txt = hot.read_text(encoding="utf-8") if hot.is_file() else ""
    caso("brain.py hot: agrega o estado quente com fonte e lista a frente fria fora da janela",
         code == 0 and "## acme" in hot_txt and "Reestruturar o funil de inbound" in hot_txt and "2026-11-10: WBR" in hot_txt
         and "Fonte: `" in hot_txt and "`beta-labs`" in hot_txt and "## beta-labs" not in hot_txt, (out + err)[-200:])
    escrever(pasta_frentes / "acme" / "decisoes.md",
             f"---\nid: decisoes-acme\ntipo: decisoes\ndono: pessoa-teste\natualizado: {recente}\n---\n# Decisões: acme\n\n"
             "- 2026-10-28: Combinado com Ana Souza (cliente): meta de 40 SQLs/mês a partir de novembro, fonte reunião de kickoff.\n")
    code, out, err = rodar(brain + ["fonte", "Ana Souza"], repo)
    rel_dec = (pasta_frentes / "acme" / "decisoes.md").relative_to(repo).as_posix()
    caso("brain.py fonte: devolve arquivo e linha do combinado (resposta com fonte)",
         code == 0 and f"{rel_dec}:9: - 2026-10-28: Combinado com Ana Souza" in out and "1 ocorrência" in out, (out + err)[-200:])
    code, out, err = rodar(brain + ["fonte", "Pessoa Inexistente"], repo)
    caso("brain.py fonte: termo ausente vira [LACUNA], não invenção", code == 0 and "0 ocorrência" in out and "[LACUNA]" in out)
    pessoas = org_dir / "pessoas"
    escrever(pessoas / "ana-souza.md",
             f"---\nid: pessoa-ana-souza\ntipo: pessoa\npapel: Head de Marketing\nrelacao: frente acme desde 2026-10\nfrentes: acme\n"
             f"contato_em: CRM, registro 884\natualizado: {recente}\n---\n# Ana Souza\n\nDecide orçamento de mídia da acme.\n")
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(brain + ["validate"], repo)
    caso("pessoas: sem aprovado_por o validate barra (gate do dono)", code == 1 and "aprovado_por" in out, (out + err)[-200:])
    escrever(pessoas / "ana-souza.md",
             f"---\nid: pessoa-ana-souza\ntipo: pessoa\npapel: Head de Marketing\nrelacao: frente acme desde 2026-10\nfrentes: acme\n"
             f"contato_em: CRM, registro 884\naprovado_por: pessoa-teste\natualizado: {recente}\n---\n# Ana Souza\n\n"
             "Decide orçamento de mídia da acme. E-mail: ana.souza@cliente-acme.com.br\n")
    code, out, err = rodar(brain + ["validate"], repo)
    caso("pessoas: e-mail em pessoas/ é erro, não pergunta", code == 1 and "pessoas/" in out and "e-mail" in out, (out + err)[-200:])
    escrever(pessoas / "ana-souza.md",
             f"---\nid: pessoa-ana-souza\ntipo: pessoa\npapel: Head de Marketing\nrelacao: frente acme desde 2026-10\nfrentes: acme\n"
             f"contato_em: CRM, registro 884\naprovado_por: pessoa-teste\natualizado: {recente}\n---\n# Ana Souza\n\nDecide orçamento de mídia da acme.\n")
    code, out, err = rodar(brain + ["validate"], repo)
    caso("pessoas: arquivo completo (papel, relação, aprovado_por) passa", code == 0, (out + err)[-300:])
    code, out, err = rodar(brain + ["pessoa", "joao-lima", "--nome", "João Lima", "--papel", "CFO", "--relacao", "frente acme desde 2026-09"], repo)
    caso("brain.py pessoa: sem --aprovado-por recusa (gate)", code == 1 and "gate" in out and not (pessoas / "joao-lima.md").exists(), out[-200:])
    code, out, err = rodar(brain + ["pessoa", "joao-lima", "--nome", "João Lima", "--papel", "CFO", "--relacao", "fala com joao@cliente-acme.com.br",
                                    "--aprovado-por", "@pessoa-teste"], repo)
    caso("brain.py pessoa: contato nos argumentos recusa", code == 1 and "contato" in out and not (pessoas / "joao-lima.md").exists(), out[-200:])
    code, out, err = rodar(brain + ["pessoa", "joao-lima", "--nome", "João Lima", "--papel", "CFO", "--relacao", "frente acme desde 2026-09",
                                    "--frentes", "acme", "--aprovado-por", "@pessoa-teste"], repo)
    texto_p = (pessoas / "joao-lima.md").read_text(encoding="utf-8") if (pessoas / "joao-lima.md").is_file() else ""
    rodar(["git", "add", "-A"], repo)
    code2, out2, err2 = rodar(brain + ["validate"], repo)
    caso("brain.py pessoa: cria o arquivo com aprovado_por e o validate passa",
         code == 0 and "aprovado_por: pessoa-teste" in texto_p and "papel: CFO" in texto_p and code2 == 0, (out + err + out2)[-300:])
    code, out, err = rodar(brain + ["mapa"], repo)
    mapa = (repo / "MAPA.md").read_text(encoding="utf-8")
    caso("brain.py mapa: conta pessoas e aponta o hot.md gerado", code == 0 and "2 stakeholder(s)" in mapa and "hot.md`: estado quente agregado (gerado em" in mapa)
    # v0.3.0: experimentos sem frontmatter barra; tipo exemplo exige as 3 seções; tipo resumo não existe mais
    escrever(pasta_frentes / "gama" / "experimentos.md", "# Experimentos: gama\n\n| E-NN | data |\n|---|---|\n")
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(brain + ["validate"], repo)
    caso("validate: experimentos.md sem frontmatter barra", code == 1 and "experimentos.md: sem frontmatter" in out, (out + err)[-200:])
    escrever(pasta_frentes / "gama" / "experimentos.md",
             f"---\nid: experimentos-gama\ntipo: experimentos\ndono: pessoa-teste\natualizado: {recente}\n---\n# Experimentos: gama\n\n| E-NN | data |\n|---|---|\n")
    escrever(repo / "00_susano" / "exemplos" / "teste_exemplo.md",
             "---\nid: ex-teste\ntipo: exemplo\nmodo: 1\natualizado: 2026-11-01\n---\n# Exemplo de teste\n\n## ENTRADA\n\nx\n\n## SAÍDA\n\ny\n")
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(brain + ["validate"], repo)
    caso("validate: exemplo sem POR QUE ASSIM barra", code == 1 and "POR QUE ASSIM" in out, (out + err)[-200:])
    escrever(repo / "00_susano" / "exemplos" / "teste_exemplo.md",
             "---\nid: ex-teste\ntipo: resumo\natualizado: 2026-11-01\n---\n# Exemplo de teste\n\n## ENTRADA\n\nx\n\n## SAÍDA\n\ny\n\n## POR QUE ASSIM\n\nz\n")
    code, out, err = rodar(brain + ["validate"], repo)
    caso("validate: tipo resumo não existe mais (erro)", code == 1 and "tipo resumo" in out, (out + err)[-200:])
    (repo / "00_susano" / "exemplos" / "teste_exemplo.md").unlink()
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(brain + ["validate"], repo)
    caso("validate: volta a passar sem o exemplo de teste", code == 0, (out + err)[-300:])
    skills_dom = sorted(p.parent.name for p in (repo / ".claude" / "skills").glob("susano-*/SKILL.md"))
    caso("skills por domínio: as 8 existem", skills_dom == ["susano-analytics", "susano-ativos", "susano-biblioteca", "susano-gtm",
                                                          "susano-metodo", "susano-performance", "susano-plataformas", "susano-rituais"], ",".join(skills_dom))
    citados = set()
    for p in (repo / ".claude" / "skills").glob("susano-*/SKILL.md"):
        citados |= set(re.findall(r"`(00_susano/[^`]+\.md)`", p.read_text(encoding="utf-8")))
    caso("skills por domínio: todo caminho citado existe", bool(citados) and all((repo / c).is_file() for c in citados),
         ",".join(sorted(c for c in citados if not (repo / c).is_file()))[:200])
    antes = {p: p.read_text(encoding="utf-8") for p in (repo / ".claude" / "skills").glob("susano-*/SKILL.md")}
    code, out, err = rodar(brain + ["skills"], repo)
    depois = {p: p.read_text(encoding="utf-8") for p in (repo / ".claude" / "skills").glob("susano-*/SKILL.md")}
    caso("brain.py skills: regenerar não muda nada (idempotente, fonte única)", code == 0 and antes == depois, (out + err)[-200:])
    rodar(["git", "add", "-A"], repo)
    rodar(["git", "commit", "-q", "-m", "v0.2.0 fixtures"], repo)

    env = {"CLAUDE_PROJECT_DIR": str(repo)}
    hooks = repo / ".claude" / "hooks"
    run_sh = ["bash", str(hooks / "run.sh")]

    # 1. settings.json
    cfg = json.loads((repo / ".claude" / "settings.json").read_text(encoding="utf-8"))
    eventos = set(cfg.get("hooks", {}))
    caso("settings.json: JSON válido com SessionStart, UserPromptSubmit e PreToolUse",
         eventos == {"SessionStart", "UserPromptSubmit", "PreToolUse"}, ",".join(sorted(eventos)))
    caso("settings.json: nega edição do método (00_susano)", "Edit(/00_susano/**)" in cfg["permissions"]["deny"])

    # 2. abertura de sessão na raiz, com perfil
    code, out, err = rodar(run_sh + [str(hooks / "sessao_inicio.py")], repo, json.dumps({"cwd": str(repo)}), env)
    caso("sessao_inicio: sai 0 na raiz", code == 0, err.strip()[:120])
    caso("sessao_inicio: reconhece a pessoa pelo git_nome", "Pessoa: Pessoa Teste (Growth Leader)" in out, out[:300])
    caso("sessao_inicio: lista frente quente e marca a da pessoa", "acme (seu)" in out and "gama:" in out, out[:400])
    caso("sessao_inicio: aponta frente fria da pessoa", "suas contas com estado frio: beta-labs" in out, out[:400])
    caso("sessao_inicio: avisa que está na main", "Branch: main" in out)
    caso("sessao_inicio: sem alerta de pasta fora da raiz", "ALERTA" not in out)

    # 3. abertura fora da raiz
    sub = pasta_frentes / "beta-labs"
    code, out, _ = rodar(run_sh + [str(hooks / "sessao_inicio.py")], sub, json.dumps({"cwd": str(sub)}), env)
    caso("sessao_inicio: alerta quando a sessão abre numa subpasta", code == 0 and "ALERTA" in out)

    # 4. pessoa sem perfil
    rodar(["git", "config", "user.name", "Pessoa Nova"], repo)
    code, out, _ = rodar(run_sh + [str(hooks / "sessao_inicio.py")], repo, json.dumps({"cwd": str(repo)}), env)
    caso("sessao_inicio: sem perfil sugere /onboarding", "sem perfil" in out and "/onboarding" in out)
    rodar(["git", "config", "user.name", "Pessoa Teste"], repo)

    # 5. guarda de conteúdo
    alvo = str(pasta_frentes / "beta-labs" / "estado.md")
    token = "gh" + "p_" + "A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q7r8"
    cartao = "4111 1111 " + "1111 1111"
    travessao = "a " + chr(0x2014) + " b"

    def guarda(tool, entrada):
        payload = {"tool_name": tool, "tool_input": entrada, "cwd": str(repo)}
        code, out, err = rodar(run_sh + [str(hooks / "guarda_conteudo.py")], repo, json.dumps(payload), env)
        decisao = ""
        if out.strip():
            decisao = json.loads(out)["hookSpecificOutput"]["permissionDecision"]
        return code, decisao, out, err

    for nome, texto in (("token GitHub", f"chave: {token}"), ("cartão", f"cartao {cartao}"),
                        ("CPF", f"cpf do lead {cpf_valido_gerado()}"), ("travessão", travessao)):
        code, decisao, out, _ = guarda("Write", {"file_path": alvo, "content": texto})
        caso(f"guarda_conteudo: bloqueia {nome} (deny)", code == 0 and decisao == "deny", out.strip()[:90])
    telefone = "(27) " + "99999-8888"
    email_pessoal = "fulano" + "@" + "gmail.com"
    code, decisao, _, _ = guarda("Write", {"file_path": alvo, "content": "contato: " + telefone})
    caso("guarda_conteudo: pergunta em telefone (ask)", decisao == "ask")
    code, decisao, _, _ = guarda("Edit", {"file_path": alvo, "old_string": "x", "new_string": email_pessoal})
    caso("guarda_conteudo: Edit com e-mail pergunta (ask)", decisao == "ask")
    code, decisao, _, _ = guarda("Write", {"file_path": alvo, "content": "contato: " + email_pessoal + " [PUBLICO]"})
    caso("guarda_conteudo: e-mail com [PUBLICO] passa (sem decisão)", code == 0 and decisao == "")
    code, decisao, _, _ = guarda("Write", {"file_path": alvo, "content": "chave: " + token + " [PUBLICO]"})
    caso("guarda_conteudo: [PUBLICO] não libera segredo (deny)", code == 0 and decisao == "deny")
    code, decisao, _, _ = guarda("Write", {"file_path": alvo, "content": "CAC de R$ 182,40 em set/2026 [DADO: CRM]"})
    caso("guarda_conteudo: texto limpo passa (sem decisão)", code == 0 and decisao == "")
    code, decisao, _, _ = guarda("Write", {"file_path": "/tmp/fora.md", "content": token})
    caso("guarda_conteudo: arquivo fora do repositório não é com ele", code == 0 and decisao == "")
    code, decisao, _, _ = guarda("NotebookEdit", {"notebook_path": str(repo / "x.ipynb"), "new_source": token})
    caso("guarda_conteudo: NotebookEdit com token bloqueia", decisao == "deny")

    # 6. guarda de mensagem
    def prompt(texto):
        return rodar(run_sh + [str(hooks / "guarda_prompt.py")], repo, json.dumps({"prompt": texto}), env)
    code, _, err = prompt(f"usa esse token {token}")
    caso("guarda_prompt: token barra a mensagem (saída 2)", code == 2 and "barrou" in err)
    code, _, _ = prompt(f"o cpf é {cpf_valido_gerado()}")
    caso("guarda_prompt: CPF barra a mensagem (saída 2)", code == 2)
    code, _, _ = prompt("analisa o funil " + chr(0x2014) + " sem pressa")
    caso("guarda_prompt: travessão na mensagem não barra", code == 0)

    # 7. run.sh sem python
    vazio = tmp / "semPython"
    vazio.mkdir()
    code, _, err = rodar(["/bin/bash", str(hooks / "run.sh"), str(hooks / "guarda_prompt.py")], repo, "{}",
                         {"PATH": str(vazio)})
    caso("run.sh: sem Python sai 1 (não bloqueante) com aviso", code == 1 and "Python" in err)

    # 8. pre-commit com o brain.py real
    code, out, err = rodar(["bash", str(hooks / "instalar_precommit.sh")], repo)
    caso("instalar_precommit: instala", code == 0 and "instalado" in out, err.strip()[:120])
    code, out, _ = rodar(["bash", str(hooks / "instalar_precommit.sh")], repo)
    caso("instalar_precommit: idempotente", code == 0 and "ja instalado" in out)
    nota = pasta_frentes / "gama" / "analises" / f"{hoje.isoformat()}_nota.md"
    escrever(nota, "# Nota\n\nCAC de R$ 182,40 em set/2026 [DADO: CRM]\n")
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(["git", "commit", "-m", "teste pre-commit"], repo)
    caso("pre-commit: roda brain.py validate e deixa passar arquivo limpo", code == 0 and "validate: OK" in (out + err),
         (out + err)[-200:])
    escrever(nota, "# Nota\n\nfunil " + chr(0x2014) + " cheio\n")
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(["git", "commit", "-m", "teste travessao"], repo)
    caso("pre-commit: barra commit com travessão", code != 0 and "travessão" in (out + err), (out + err)[-200:])
    rodar(["git", "checkout", "--", "."], repo)
    rodar(["git", "reset", "-q", "--hard"], repo)

    # 9. arquivo gerenciado alterado fora de versão
    (repo / "00_susano" / "identidade.md").write_text("mexido\n", encoding="utf-8")
    code, out, _ = rodar(brain + ["susano-check"], repo)
    caso("susano-check: falha quando um gerenciado muda fora de versão", code == 1 and "alterado fora de uma versão" in out)

    falhas = [n for n, ok in resultados if not ok]
    print(f"\n{len(resultados) - len(falhas)}/{len(resultados)} casos passaram. Repositório de teste: {repo}")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
