---
name: frente
description: Focus the session on one frente (client, account or product): loads its ficha, context, hot state, decisions and ledger and enforces isolation. Use whenever the user names a frente, before any frente-specific work.
argument-hint: "<slug-do-cliente>"
arguments: slug
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash(python3 scripts/brain.py fonte *)
---

Always answer in PT-BR. Read only.

Client: $slug

1. Resolve the folder. If `$slug` is empty or `20_<frente>/$slug/` does not exist, list the folders in `20_<frente>/`, match the user's words to a slug and ask one question with the best match as default. Stop until there is a valid folder.
2. Read, in this order: `20_<frente>/$slug/README.md` (ficha: owner, status, map), `contexto.md`, `estado.md`, `decisoes.md` (current decisions; older or superseded ones only on demand), the three most recent files in `ledger/` if the folder exists, and the file list of `analises/`, `reunioes/` and `playbooks/`.
3. Declare focus in one line: `Foco: <nome> (<slug>). Dono: <owner>. Estado de <data do estado.md>.` Flag [VERIFICAR] when `estado.md` is older than 14 days.
4. Isolation for the rest of the session: use only `20_<frente>/$slug/`, `10_<org>/`, `40_playbooks/` and `50_referencia/`. Anything from another client needs an explicit request and a label with that client's name.
5. Targets: use only what this client's files register. A metric without a target is [LACUNA]; never borrow one.
6. "O que ficou combinado com <pessoa>?" and any question about a past decision, target or number: run `python3 scripts/brain.py fonte "<termo>"` and answer with file and line; `10_<org>/pessoas/<slug>.md` gives the person's role and relation (never contact data).
7. Summary in at most 12 lines: momento atual, até 3 prioridades, as 3 pendências mais críticas (dono e prazo), decisões vigentes mais recentes, lacunas de contexto que travam o trabalho (e quem preenche).
