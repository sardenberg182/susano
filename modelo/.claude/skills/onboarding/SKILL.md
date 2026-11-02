---
name: onboarding
description: First-time setup of a team member: checks the environment, creates the work profile so Susano recognizes the person, offers local safeguards and teaches the daily loop.
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Bash(git --version)
  - Bash(git config --get user.name)
  - Bash(git config --get user.email)
  - Bash(python3 --version)
  - Bash(gh auth status)
---

Always answer in PT-BR. Collect work context only, nothing personal.

1. **Environment**: session type (cloud when the variable CLAUDE_CODE_REMOTE is "true"), `git --version`, `git config --get user.name`, Python 3.9 or newer, `gh auth status` (optional). For each missing item give the exact fix in one line. In a local session, also confirm the session started at the repository root.
2. **Ask in one message**: nome, papel na organização, clientes que você toca (slugs de `20_<frente>/`, show the list), usuário do GitHub, preferências de formato (opcional).
3. **Profile**: create `10_<org>/time/<slug-do-nome>.md` from `10_<org>/time/_modelo.md`. The field `git_nome` must equal the output of `git config --get user.name`, or the session hook will not recognize the person. In a cloud session, use the name GitHub shows for the person's commits.
4. **Local session only**: install the pre-commit check (`bash .claude/hooks/instalar_precommit.sh`) as the default, asking only if the person wants to skip it; then offer `CLAUDE.local.md` at the root (Git ignores it) for personal preferences that should not be shared. In the profile, `preferencias` can hold reading conventions such as "decodificação de voz: termo ditado = termo certo" for someone who dictates.
5. **Teach the loop** in 6 short lines: abrir na raiz → `/cerebro` → `/frente <slug>` → trabalhar (`/analise`, `/ingerir`) → `/salve` → PR aprovado pelo dono.
6. If `MAPA.md` is missing, run `python3 scripts/brain.py mapa` and `python3 scripts/brain.py hot` so the repository has its map; then run `/salve` to open the PR with the new profile.
