---
name: cerebro
description: Briefing for the person in the session: hot states, their frentes, open items and near deadlines. Use at the start of a work session or when asked what is going on.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash(git pull --ff-only)
  - Bash(python3 scripts/brain.py fonte *)
---

Always answer in PT-BR. Read only; this skill changes no file.

1. If the working tree is clean and the branch tracks a remote, run `git pull --ff-only`. If it fails, say so in one line and continue with the local copy.
2. From the session context, take the person's name and client slugs. If missing, list `10_<org>/time/` and ask one question with the best guess as default.
3. If `10_<org>/hot.md` exists and its `atualizado` is within 14 days, start from it (one read instead of one per frente) and open an `estado.md` only when a line needs detail; otherwise, for each of the person's clients, read `20_<frente>/<slug>/estado.md` (and only the "aberto" or open-items part of `decisoes.md` if `estado.md` points there). For the other clients, read only the `estado.md` files whose `atualizado` date is within 14 days.
4. If `10_<org>/` has a company status or rituals file the README points to, read its current section.
5. Answer in at most 25 lines:
   - **Suas contas**: one line per client, phase or status, the most important open item with owner and date, staleness flag when `estado.md` is older than 14 days.
   - **Em movimento na organização**: up to 5 lines from other hot clients.
   - **Prazos em 7 dias** and **bloqueios**, each with its file path.
   - **Sugestão de foco**: one line, marked [INFERÊNCIA].
6. Every line cites the file it came from. A question about what was agreed with someone ("o que ficou combinado com X?") is answered with `python3 scripts/brain.py fonte "X"`: file and line in the answer, [LACUNA] when nothing cites the name. If a file is missing or empty, say [LACUNA] and which command fills it (`/estado-quente`, `/nova-frente`).
