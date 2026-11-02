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
    escrever(pasta_frentes / "beta-labs" / "decisoes.md",
             f"---\nid: decisoes-beta-labs\ntipo: decisoes\ndono: pessoa-teste\natualizado: {antigo}\n---\n# Decisões: beta-labs\n\n"
             "- 2026-10-20: Combinado com Ana Souza (cliente): meta de 25 SQLs/mês, fonte reunião mensal.\n")
    code, out, err = rodar(brain + ["fonte", "Ana Souza", "--frente", "acme"], repo)
    rel_dec = (pasta_frentes / "acme" / "decisoes.md").relative_to(repo).as_posix()
    caso("brain.py fonte --frente: devolve arquivo e linha do combinado, rotulado pela frente",
         code == 0 and f"[frente:acme] {rel_dec}:9: - 2026-10-28: Combinado com Ana Souza" in out and "1 ocorrência" in out, (out + err)[-200:])
    caso("brain.py fonte --frente: a mesma expressão em outra frente não aparece (isolamento)", "beta-labs" not in out and "25 SQLs" not in out)
    code, out, err = rodar(brain + ["fonte", "Ana Souza", "--todas"], repo)
    caso("brain.py fonte --todas: só a pedido, cada linha com a frente de origem",
         code == 0 and "[frente:acme]" in out and "[frente:beta-labs]" in out and "2 ocorrência" in out and "pedido explícito" in out,
         (out + err)[-300:])
    code, out, err = rodar(brain + ["fonte", "Ana Souza"], repo)
    caso("brain.py fonte sem foco: nenhuma frente entra e a saída aponta --frente",
         code == 0 and "0 ocorrência" in out and "[frente:" not in out and "--frente <slug>" in out, (out + err)[-300:])
    code, out, err = rodar(brain + ["fonte", "Ana Souza", "--frente", "nao-existe"], repo)
    caso("brain.py fonte --frente: slug que não existe é erro", code == 1 and "não existe" in out, (out + err)[-200:])
    code, out, err = rodar(brain + ["fonte", "Pessoa Inexistente", "--frente", "acme"], repo)
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
             "Decide orçamento de mídia da acme. E-mail: ana.souza" + "@" + "cliente-acme.com.br\n")
    code, out, err = rodar(brain + ["validate"], repo)
    caso("pessoas: e-mail em pessoas/ é erro, não pergunta", code == 1 and "pessoas/" in out and "e-mail" in out, (out + err)[-200:])
    escrever(pessoas / "ana-souza.md",
             f"---\nid: pessoa-ana-souza\ntipo: pessoa\npapel: Head de Marketing\nrelacao: frente acme desde 2026-10\nfrentes: acme\n"
             f"contato_em: CRM, registro 884\naprovado_por: pessoa-teste\natualizado: {recente}\n---\n# Ana Souza\n\nDecide orçamento de mídia da acme.\n")
    code, out, err = rodar(brain + ["validate"], repo)
    caso("pessoas: arquivo completo (papel, relação, aprovado_por) passa", code == 0, (out + err)[-300:])
    code, out, err = rodar(brain + ["pessoa", "joao-lima", "--nome", "João Lima", "--papel", "CFO", "--relacao", "frente acme desde 2026-09"], repo)
    caso("brain.py pessoa: sem --aprovado-por recusa (gate)", code == 1 and "gate" in out and not (pessoas / "joao-lima.md").exists(), out[-200:])
    code, out, err = rodar(brain + ["pessoa", "joao-lima", "--nome", "João Lima", "--papel", "CFO", "--relacao", "fala com joao" + "@" + "cliente-acme.com.br",
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
    caso("skills por domínio: as 9 existem (v0.3: exemplos)", skills_dom == ["susano-analytics", "susano-ativos", "susano-biblioteca",
                                                                           "susano-exemplos", "susano-gtm", "susano-metodo", "susano-performance",
                                                                           "susano-plataformas", "susano-rituais"], ",".join(skills_dom))
    perf = (repo / ".claude" / "skills" / "susano-performance" / "SKILL.md").read_text(encoding="utf-8")
    rit = (repo / ".claude" / "skills" / "susano-rituais" / "SKILL.md").read_text(encoding="utf-8")
    caso("skills v0.3: landing_pages.md só na performance (arquivo e exclusão no mapa de domínios)",
         "00_susano/instrucoes/landing_pages.md" in perf and "00_susano/instrucoes/landing_pages.md" not in rit
         and "00_susano/instrucoes/wbr.md" in rit)
    indice = (repo / "00_susano" / "INDICE.md").read_text(encoding="utf-8")
    caso("indice v0.3: Operação lista situacoes.md, calibracao.md e exemplos/README.md",
         all(f"`00_susano/{n}`" in indice for n in ("situacoes.md", "calibracao.md", "exemplos/README.md")))
    for n in ("situacoes.md", "calibracao.md"):
        texto = (repo / "00_susano" / n).read_text(encoding="utf-8")
        caso(f"v0.3: {n} cita só caminhos que existem",
             all((repo / c).is_file() for c in re.findall(r"`(00_susano/[^`#\s]+\.md)`", texto)),
             ",".join(c for c in re.findall(r"`(00_susano/[^`#\s]+\.md)`", texto) if not (repo / c).is_file())[:200])
    citados = set()
    for p in (repo / ".claude" / "skills").glob("susano-*/SKILL.md"):
        citados |= set(re.findall(r"`(00_susano/[^`]+\.md)`", p.read_text(encoding="utf-8")))
    caso("skills por domínio: todo caminho citado existe", bool(citados) and all((repo / c).is_file() for c in citados),
         ",".join(sorted(c for c in citados if not (repo / c).is_file()))[:200])
    antes = {p: p.read_text(encoding="utf-8") for p in (repo / ".claude" / "skills").glob("susano-*/SKILL.md")}
    code, out, err = rodar(brain + ["skills"], repo)
    depois = {p: p.read_text(encoding="utf-8") for p in (repo / ".claude" / "skills").glob("susano-*/SKILL.md")}
    caso("brain.py skills: regenerar não muda nada (idempotente, fonte única)", code == 0 and antes == depois, (out + err)[-200:])

    # 0c. v0.4.0: migrar (bloco gerenciado do AGENTS.md, as quatro da frente), orçamento em duas partes, mapa
    code, out, err = rodar(brain + ["migrar"], repo)
    caso("brain.py migrar: projeto novo já está no contrato (nada a migrar)", code == 0 and "nada a migrar" in out, (out + err)[-200:])
    code, out, err = rodar(brain + ["tokens"], repo)
    m = re.search(r"gerenciado: (\d+) \(teto (\d+)\); projeto: (\d+)", out)
    caso("brain.py tokens: separa pacote gerenciado e parte do projeto, com o gerenciado no teto",
         code == 0 and m is not None and int(m.group(1)) <= int(m.group(2)) and "AGENTS.md (bloco gerenciado)" in out, (out + err)[-300:])
    (pasta_frentes / "gama" / "experimentos.md").unlink()
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(brain + ["validate"], repo)
    caso("validate: frente sem um dos quatro arquivos obrigatórios falha", code == 1 and "falta experimentos.md" in out, (out + err)[-300:])
    decisoes_acme = (pasta_frentes / "acme" / "decisoes.md").read_text(encoding="utf-8")
    code, out, err = rodar(brain + ["migrar"], repo)
    caso("brain.py migrar: cria o arquivo que falta na frente sem tocar no que está preenchido",
         code == 0 and (pasta_frentes / "gama" / "experimentos.md").is_file() and "1 mudança" in out
         and (pasta_frentes / "acme" / "decisoes.md").read_text(encoding="utf-8") == decisoes_acme, (out + err)[-300:])
    agents = repo / "AGENTS.md"
    agents_novo = agents.read_text(encoding="utf-8")
    escrever(agents, "# AGENTS: Teste\n\nRegras antigas.\n\n## Regras\n\n1. Nunca commit na main.\n\n"
                     "## Regras próprias de Teste\n\n- WBR toda segunda às 9h, com o dono da frente.\n")
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(brain + ["susano-check"], repo)
    caso("susano-check: AGENTS.md sem o bloco gerenciado falha e aponta o migrar", code == 1 and "brain.py migrar" in out, (out + err)[-300:])
    code, out, err = rodar(brain + ["migrar"], repo)
    agents_migrado = agents.read_text(encoding="utf-8")
    arquivados = list((repo / "90_arquivo").glob("AGENTS_antes_do_bloco_gerenciado_*.md"))
    caso("brain.py migrar: AGENTS.md antigo ganha o bloco gerenciado, Regras próprias preservadas, anterior no 90_arquivo",
         code == 0 and "<!-- susano:inicio" in agents_migrado and "WBR toda segunda às 9h" in agents_migrado
         and "Regras antigas." not in agents_migrado and len(arquivados) == 1 and "Regras antigas." in arquivados[0].read_text(encoding="utf-8"),
         (out + err)[-300:])
    code, out, err = rodar(brain + ["migrar"], repo)
    caso("brain.py migrar: segunda execução não muda nada (idempotente)", code == 0 and "nada a migrar" in out
         and agents.read_text(encoding="utf-8") == agents_migrado, (out + err)[-200:])
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(brain + ["susano-check"], repo)
    caso("susano-check: passa depois do migrar", code == 0, (out + err)[-300:])
    escrever(agents, agents_migrado.replace("ninguém faz merge do próprio PR", "o dono faz merge quando quiser"))
    code, out, err = rodar(brain + ["susano-check"], repo)
    caso("susano-check: bloco gerenciado editado à mão falha", code == 1 and "bloco gerenciado diferente" in out, (out + err)[-300:])
    escrever(agents, agents_novo)
    for arq in arquivados:
        arq.unlink()
    escrever(repo / "60_aprendizados" / "README.md", "# Aprendizados entre frentes\n\nPadrões que valem para mais de uma frente.\n")
    code, out, err = rodar(brain + ["mapa"], repo)
    mapa = (repo / "MAPA.md").read_text(encoding="utf-8")
    caso("brain.py mapa: lista pasta extra do projeto com a primeira linha do README",
         code == 0 and "`60_aprendizados/`: Aprendizados entre frentes" in mapa, mapa[-300:])
    rodar(["git", "add", "-A"], repo)
    rodar(["git", "commit", "-q", "-m", "v0.2.0 fixtures"], repo)

    claude_novo, claude_velho = tmp / "claude_novo", tmp / "claude_velho"
    escrever(claude_novo, "#!/bin/sh\necho '2.1.316 (Claude Code)'\n")
    escrever(claude_velho, "#!/bin/sh\necho '2.1.100 (Claude Code)'\n")
    claude_novo.chmod(0o755)
    claude_velho.chmod(0o755)
    env = {"CLAUDE_PROJECT_DIR": str(repo), "CLAUDE_CODE_EXECPATH": str(claude_novo)}
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

    code, out, _ = rodar(run_sh + [str(hooks / "sessao_inicio.py")], repo, json.dumps({"cwd": str(repo)}),
                         dict(env, CLAUDE_CODE_EXECPATH=str(claude_velho)))
    caso("sessao_inicio: alerta quando o Claude Code está abaixo do mínimo das travas (2.1.295)",
         code == 0 and "ALERTA: Claude Code 2.1.100 abaixo do minimo 2.1.295" in out, out[:300])

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
    code, decisao, _, _ = guarda("Write", {"file_path": alvo, "content": "remetente: noreply" + "@" + "plataforma-ficticia.com.br"})
    caso("guarda_conteudo: endereço de sistema (noreply) não é contato de pessoa (sem decisão)", code == 0 and decisao == "")
    code, decisao, _, _ = guarda("Write", {"file_path": alvo, "content": "chave: " + token + " [PUBLICO]"})
    caso("guarda_conteudo: [PUBLICO] não libera segredo (deny)", code == 0 and decisao == "deny")
    code, decisao, _, _ = guarda("Write", {"file_path": alvo, "content": "CAC de R$ 182,40 em set/2026 [DADO: CRM]"})
    caso("guarda_conteudo: texto limpo passa (sem decisão)", code == 0 and decisao == "")
    code, decisao, _, _ = guarda("Write", {"file_path": "/tmp/fora.md", "content": token})
    caso("guarda_conteudo: arquivo fora do repositório não é com ele", code == 0 and decisao == "")
    code, decisao, _, _ = guarda("NotebookEdit", {"notebook_path": str(repo / "x.ipynb"), "new_source": token})
    caso("guarda_conteudo: NotebookEdit com token bloqueia", decisao == "deny")
    code, decisao, _, _ = guarda("MultiEdit", {"file_path": alvo, "edits": [{"old_string": "a", "new_string": "ok"},
                                                                            {"old_string": "b", "new_string": token}]})
    caso("guarda_conteudo: MultiEdit com token numa das edições bloqueia", decisao == "deny")
    caso("settings.json: matcher da guarda cobre Write, Edit, MultiEdit e NotebookEdit",
         cfg["hooks"]["PreToolUse"][0]["matcher"] == "Write|Edit|MultiEdit|NotebookEdit")

    # 5b. falha da guarda barra (SUS04): entrada inválida, import quebrado, sem vazar o conteúdo
    code, out, err = rodar(run_sh + [str(hooks / "guarda_conteudo.py")], repo, "isto não é JSON " + token, env)
    caso("guarda_conteudo: JSON inválido barra (saída 2) sem repetir o conteúdo", code == 2 and "falhou" in err and token not in err + out,
         err.strip()[:160])
    code, out, err = rodar(run_sh + [str(hooks / "guarda_prompt.py")], repo, "[1, 2", env)
    caso("guarda_prompt: JSON inválido barra (saída 2)", code == 2 and "falhou" in err, err.strip()[:160])
    quebrado = tmp / "hooks_quebrados"
    shutil.copytree(hooks, quebrado, ignore=shutil.ignore_patterns("__pycache__"))
    (quebrado / "guardas.py").write_text("raise ImportError('biblioteca indisponivel')\n", encoding="utf-8")
    payload = json.dumps({"tool_name": "Write", "tool_input": {"file_path": alvo, "content": "texto limpo"}, "cwd": str(repo)})
    code, out, err = rodar(["bash", str(quebrado / "run.sh"), "--bloqueante", str(quebrado / "guarda_conteudo.py")], repo, payload, env)
    caso("guarda_conteudo: import das guardas quebrado barra a escrita (saída 2)", code == 2 and "ImportError" in err, err.strip()[:160])
    code, out, err = rodar(["bash", str(quebrado / "run.sh"), "--bloqueante", str(quebrado / "guarda_prompt.py")], repo,
                           json.dumps({"prompt": "oi"}), env)
    caso("guarda_prompt: import das guardas quebrado barra a mensagem (saída 2)", code == 2 and "ImportError" in err, err.strip()[:160])
    code, out, err = rodar(run_sh + [str(hooks / "sessao_inicio.py")], repo, "não é JSON", env)
    caso("sessao_inicio: hook informativo, entrada inválida não barra (sai 0)", code == 0 and "[SUSANO]" in out, err.strip()[:160])
    for evento in ("UserPromptSubmit", "PreToolUse"):
        h = cfg["hooks"][evento][0]["hooks"][0]
        caso(f"settings.json: guarda de {evento} bloqueia em falha (onFailure block e run.sh --bloqueante)",
             h.get("onFailure") == "block" and "run.sh\" --bloqueante" in h["command"], json.dumps(h)[:200])
    h = cfg["hooks"]["SessionStart"][0]["hooks"][0]
    caso("settings.json: abertura segue informativa (sem onFailure block, sem --bloqueante)",
         "onFailure" not in h and "--bloqueante" not in h["command"])

    # 6. guarda de mensagem
    def prompt(texto):
        return rodar(run_sh + [str(hooks / "guarda_prompt.py")], repo, json.dumps({"prompt": texto}), env)
    code, _, err = prompt(f"usa esse token {token}")
    caso("guarda_prompt: token barra a mensagem (saída 2)", code == 2 and "barrou" in err)
    code, _, _ = prompt(f"o cpf é {cpf_valido_gerado()}")
    caso("guarda_prompt: CPF barra a mensagem (saída 2)", code == 2)
    code, _, _ = prompt("analisa o funil " + chr(0x2014) + " sem pressa")
    caso("guarda_prompt: travessão na mensagem não barra", code == 0)

    # 7. run.sh sem python: abertura informativa (1), trava bloqueante (2)
    vazio = tmp / "semPython"
    vazio.mkdir()
    code, _, err = rodar(["/bin/bash", str(hooks / "run.sh"), str(hooks / "sessao_inicio.py")], repo, "{}",
                         {"PATH": str(vazio)})
    caso("run.sh: sem Python, a abertura sai 1 (não bloqueante) com aviso", code == 1 and "Python" in err)
    code, _, err = rodar(["/bin/bash", str(hooks / "run.sh"), "--bloqueante", str(hooks / "guarda_prompt.py")], repo, "{}",
                         {"PATH": str(vazio)})
    caso("run.sh --bloqueante: sem Python, a trava sai 2 (barra a ação) com aviso", code == 2 and "barrada" in err, err.strip()[:160])

    # 8. pre-commit: índice do Git (não o disco), hook anterior preservado, reinstalação idempotente
    code, out, err = rodar(["bash", str(hooks / "instalar_precommit.sh")], repo)
    caso("instalar_precommit: instala", code == 0 and "instalado" in out, err.strip()[:120])
    hook_pc = repo / ".git" / "hooks" / "pre-commit"
    antes_pc = hook_pc.read_text(encoding="utf-8") if hook_pc.is_file() else ""
    code, out, _ = rodar(["bash", str(hooks / "instalar_precommit.sh")], repo)
    caso("instalar_precommit: idempotente (reinstalar não muda nem multiplica a cadeia)",
         code == 0 and "ja instalado" in out and hook_pc.read_text(encoding="utf-8") == antes_pc and antes_pc.count("varrer --staged") == 1)
    nota = pasta_frentes / "gama" / "analises" / f"{hoje.isoformat()}_nota.md"
    escrever(nota, "# Nota\n\nCAC de R$ 182,40 em set/2026 [DADO: CRM]\n")
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(["git", "commit", "-m", "teste pre-commit"], repo)
    caso("pre-commit: inspeciona o índice, roda brain.py validate e deixa passar arquivo limpo",
         code == 0 and "validate: OK" in (out + err) and "varrer (perfil projeto, índice" in (out + err), (out + err)[-200:])
    escrever(nota, "# Nota\n\nfunil " + chr(0x2014) + " cheio\n")
    rodar(["git", "add", "-A"], repo)
    code, out, err = rodar(["git", "commit", "-m", "teste travessao"], repo)
    caso("pre-commit: barra commit com travessão", code != 0 and "travessão" in (out + err), (out + err)[-200:])
    rodar(["git", "checkout", "--", "."], repo)
    rodar(["git", "reset", "-q", "--hard"], repo)
    estranho = pasta_frentes / "gama" / "analises" / "relatório de mídia ação.csv"
    escrever(estranho, f"campanha,token\nbusca,{token}\n")
    rodar(["git", "add", "--", str(estranho.relative_to(repo))], repo)
    escrever(estranho, "campanha,cpl\nbusca,12.30\n")  # disco limpo, índice com o token
    code, out, err = rodar(["git", "commit", "-m", "teste indice"], repo)
    caso("pre-commit: token no índice com disco limpo barra o commit (nome com espaço e acento)",
         code != 0 and "token GitHub" in (out + err) and "relatório de mídia ação.csv" in (out + err), (out + err)[-300:])
    rodar(["git", "reset", "-q", "--", str(estranho.relative_to(repo))], repo)  # tira do índice; o disco fica
    code, out, err = rodar(["git", "commit", "-m", "corrige", "--allow-empty"], repo)
    caso("pre-commit: tirar o arquivo do índice permite seguir pelo fluxo normal", code == 0, (out + err)[-300:])
    (estranho).write_text("", encoding="utf-8")
    rodar(["git", "add", "-A"], repo)
    rodar(["git", "commit", "-q", "-m", "csv limpo"], repo)
    # hook anterior: num clone do projeto, um pre-commit que falha já existia antes da instalação
    outro = tmp / "projeto_com_hook"
    rodar(["git", "clone", "-q", str(repo), str(outro)], tmp)
    rodar(["git", "config", "user.name", "Pessoa Teste"], outro)
    rodar(["git", "config", "user.email", "pessoa@example.com"], outro)
    escrever(outro / ".git" / "hooks" / "pre-commit", "#!/usr/bin/env bash\necho 'checagem antiga falhou' >&2\nexit 1\n")
    (outro / ".git" / "hooks" / "pre-commit").chmod(0o755)
    code, out, err = rodar(["bash", str(outro / ".claude" / "hooks" / "instalar_precommit.sh")], outro)
    caso("instalar_precommit: preserva o hook anterior", code == 0 and (outro / ".git" / "hooks" / "pre-commit.antes-susano").is_file(),
         (out + err)[-200:])
    escrever(outro / "40_playbooks" / "teste_hook.md", "# Teste\n\nlimpo\n")
    rodar(["git", "add", "-A"], outro)
    code, out, err = rodar(["git", "commit", "-m", "teste hook anterior"], outro)
    caso("pre-commit: a falha do hook anterior continua barrando o commit", code != 0 and "checagem antiga falhou" in (out + err),
         (out + err)[-200:])
    escrever(outro / ".git" / "hooks" / "pre-commit.antes-susano", "#!/usr/bin/env bash\nexit 0\n")
    code, out, err = rodar(["git", "commit", "-m", "teste hook anterior ok"], outro)
    caso("pre-commit: hook anterior passando, a cadeia do Susano roda depois", code == 0 and "validate: OK" in (out + err),
         (out + err)[-200:])
    code, out, _ = rodar(["bash", str(outro / ".claude" / "hooks" / "instalar_precommit.sh")], outro)
    caso("instalar_precommit: reinstalar com hook anterior não duplica a cadeia", code == 0 and "ja instalado" in out
         and (outro / ".git" / "hooks" / "pre-commit").read_text(encoding="utf-8").count("pre-commit.antes-susano") == 2)

    # 10. inspeção de privacidade em todo formato e pasta (SUS02)
    def fixture(rel_path: str, conteudo, forcar: bool = False):
        p = repo / rel_path
        p.parent.mkdir(parents=True, exist_ok=True)
        (p.write_bytes if isinstance(conteudo, bytes) else lambda c: p.write_text(c, encoding="utf-8"))(conteudo)
        rodar(["git", "add"] + (["-f"] if forcar else []) + ["--", rel_path], repo)
        return p

    def retirar(p: Path):
        rodar(["git", "rm", "-q", "-f", "--cached", "--", p.relative_to(repo).as_posix()], repo)
        p.unlink()

    rel_frente = pasta_frentes.relative_to(repo).as_posix()
    caderno = json.dumps({"cells": [{"cell_type": "code", "source": ["token = '" + token + "'"]}], "nbformat": 4})
    for rel_path, conteudo, forcar in ((f"{rel_frente}/gama/analises/export.csv", f"campanha,chave\nbusca,{token}\n", False),
                                       ("90_arquivo/antigo/nota.md", f"# Antigo\n\nchave {token}\n", False),
                                       (".env", f"API_KEY={token}\n", True),
                                       ("50_referencia/caderno.ipynb", caderno, False),
                                       ("50_referencia/LEIAME", f"chave {token}\n", False)):
        p = fixture(rel_path, conteudo, forcar)
        code, out, err = rodar(brain + ["validate"], repo)
        extra = (rel_path != ".env") or "apesar do .gitignore" in out
        caso(f"validate: token em {rel_path} é erro (todo formato e pasta)", code == 1 and f"{rel_path}:" in out and "token GitHub" in out and extra,
             out[-300:])
        retirar(p)
    import io as _io
    import zipfile as _zipfile
    buf = _io.BytesIO()
    with _zipfile.ZipFile(buf, "w") as z:
        z.writestr("dentro/nota.md", f"chave {token}\n")
    p = fixture("50_referencia/pacote.zip", buf.getvalue())
    code, out, err = rodar(brain + ["validate"], repo)
    caso("validate: ZIP é aberto e o token dentro dele é erro", code == 1 and "pacote.zip!dentro/nota.md:1: token GitHub" in out, out[-300:])
    retirar(p)
    p = fixture("50_referencia/diagrama.png", b"\x89PNG\r\n\x1a\n" + bytes(64))
    code, out, err = rodar(brain + ["validate"], repo)
    caso("validate: binário não inspecionável vira aviso visível no projeto", code == 0 and "sem inspeção de privacidade" in out
         and "diagrama.png" in out, out[-300:])
    code, out, err = rodar(brain + ["varrer", "--perfil", "publico", "50_referencia/diagrama.png"], repo)
    caso("varrer --perfil publico: binário não inspecionável é erro", code == 1 and "não inspecionado" in out, out[-300:])
    retirar(p)
    contato = fixture("50_referencia/contatos.md", "# Fornecedores\n\nSuporte: atendimento" + "@" + "fornecedor-ficticio.com.br\n")
    code, out, err = rodar(brain + ["validate"], repo)
    caso("validate: e-mail fora de pessoas/ é aviso no projeto", code == 0 and "contatos.md:3: e-mail" in out, out[-300:])
    code, out, err = rodar(brain + ["varrer", "--perfil", "publico"], repo)
    caso("varrer --perfil publico: e-mail é erro", code == 1 and "repositório público não leva contato" in out, out[-300:])
    excecoes = repo / "PRIVACIDADE_EXCECOES.md"
    escrever(excecoes, "# Exceções\n\n| regra | caminho | motivo |\n|---|---|---|\n"
                       "| e-mail | 50_referencia/contatos.md | canal público do fornecedor fictício do teste |\n")
    code, out, err = rodar(brain + ["varrer", "--perfil", "publico", "50_referencia/contatos.md"], repo)
    caso("varrer: exceção por regra e arquivo exato, com motivo, libera o contato", code == 0, out[-300:])
    escrever(excecoes, "# Exceções\n\n| regra | caminho | motivo |\n|---|---|---|\n| e-mail | 50_referencia/ | pasta inteira |\n"
                       f"| token GitHub | {rel_frente}/gama/estado.md | fixture |\n| telefone | 50_referencia/contatos.md | |\n")
    code, out, err = rodar(brain + ["varrer", "--perfil", "publico", "50_referencia/contatos.md"], repo)
    caso("varrer: exceção de pasta, de segredo ou sem motivo é recusada",
         code == 1 and "arquivo exato" in out and "não aceita exceção" in out and "sem motivo" in out, out[-400:])
    excecoes.unlink()
    retirar(contato)
    guardas_py = hooks / "guardas.py"
    guardas_py.rename(hooks / "guardas.py.fora")
    code, out, err = rodar(brain + ["validate"], repo)
    guardas_py_fora = hooks / "guardas.py.fora"
    guardas_py_fora.rename(guardas_py)
    caso("validate: sem a biblioteca de guardas falha (nunca sucesso sem inspeção)", code == 1 and "inspeção de privacidade não rodou" in out,
         out[-300:])
    rodar(["git", "add", "-A"], repo)
    rodar(["git", "commit", "-q", "-m", "fixtures de privacidade"], repo)
    code, out, err = rodar(brain + ["validate"], repo)
    caso("validate: volta a passar depois das fixtures de privacidade", code == 0, out[-300:])

    # 9. arquivo gerenciado alterado fora de versão
    (repo / "00_susano" / "identidade.md").write_text("mexido\n", encoding="utf-8")
    code, out, _ = rodar(brain + ["susano-check"], repo)
    caso("susano-check: falha quando um gerenciado muda fora de versão", code == 1 and "alterado fora de uma versão" in out)

    falhas = [n for n, ok in resultados if not ok]
    print(f"\n{len(resultados) - len(falhas)}/{len(resultados)} casos passaram. Repositório de teste: {repo}")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
