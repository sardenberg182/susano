---
name: salve
description: Persist what the session produced (ledger, estado, decisões, analyses) per the salve playbook, regenerate MAPA.md and hot.md, validate, then branch and pull request. Run at the end of a session, after a meeting or any decision.
disable-model-invocation: true
allowed-tools:
  - Read
  - Grep
  - Glob
  - Edit
  - Write
  - Bash(git *)
  - Bash(gh auth status)
  - Bash(gh pr create *)
  - Bash(gh pr view *)
  - Bash(python3 scripts/brain.py *)
---

Always answer in PT-BR. Never commit to `main`, never merge, never include secrets or raw personal data.

## 0. Load the rules of the house
Read `00_susano/metodo/salve.md` and the client and ledger sections of `CONVENCOES.md`. They are canonical: if anything below disagrees with them, follow them and flag [CONTRADIÇÃO] in the PR body. If the playbook does not exist, follow this skill and say so in the PR body.

## 1. Harvest
List what this session produced that should outlive it, one item per line: type (decisão, pendência, status, prazo, métrica, pessoa nova, análise, experimento, aprendizado da frente, aprendizado de método), frente slug or `org`, one factual excerpt with no interpretation, source with date (reunião, mensagem, documento, sistema), and the reference to the evidence (file path or link, never the raw content).
Show the list as a numbered table and ask ONE question: `Salvo estes N itens? (s = todos, números para tirar, ou ajuste)`. Default: todos.

## 2. Write
For each confirmed item, write where the playbook says. Defaults when it is silent:
- Client facts: the day's file in `20_<frente>/<slug>/ledger/`, then `estado.md` (open now, closed in 14 days, `atualizado` bumped), and `decisoes.md` for decisions (superseded ones marked, never deleted).
- Experiments: a line `E-NN` in `20_<frente>/<slug>/experimentos.md` (hypothesis with cut, lever, status rodando/matou/sistematizou, result, decision and reference); a hypothesis without a cut does not enter.
- Learnings that hold only for this frente: `contexto.md`, section "Notas do Susano".
- Analyses and deliverables: `20_<frente>/<slug>/analises/` with the date prefix the conventions require.
- Method learnings (how the organization should work): never edit `40_playbooks/` here. Open a GitHub issue "Contexto novo" with the proposal, or include it as a clearly separated proposal in the PR body.
- Company facts: the `10_<org>/` file the README points to.

## 3. Regenerate and validate
Run `python3 scripts/brain.py mapa` and `python3 scripts/brain.py hot` (both files are generated, never edited by hand), then `python3 scripts/brain.py validate` (confirm syntax with `--help` once). Fix every error. Warnings: fix them or explain them in the PR body. Include `MAPA.md` and `10_<org>/hot.md` in the commit when they changed.

## 4. Branch, commit, pull request
1. If on `main`, create the branch `salve/AAAA-MM-DD-<tema>` (the method's single convention, see `CONTRIBUTING.md`); a cloud session that already started on a `claude/` branch keeps it.
2. `git add` only the files you changed. Never `git add -A`.
3. Commit message: `salve(<cliente>): <resumo de 1 linha>`, body listing the items.
4. `git push -u origin HEAD`.
5. If `gh auth status` succeeds, `gh pr create` with base `main`, a title like the commit and a body with: items saved, files changed, sources, open [VERIFICAR] and [LACUNA]. Otherwise tell the person the branch name and that the PR opens with the "Create PR" button (cloud session) or from the link GitHub printed.
6. Report in at most 8 lines: o que foi salvo, arquivos, branch, PR, quem aprova (CODEOWNERS do cliente ou do arquivo).
