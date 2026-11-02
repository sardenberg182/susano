---
name: estado-quente
description: Weekly refresh of estado.md for active frentes from recent ledger, decisions and analyses (open now, closed in 14 days), then one pull request. Run weekly or from a scheduled task.
disable-model-invocation: true
argument-hint: "[slug opcional para um cliente só]"
---

Always answer in PT-BR. Never edit `40_playbooks/`, `.claude/`, `.github/` or `scripts/` here.

1. `git pull --ff-only` when the tree is clean.
2. Read the estado section of `CONVENCOES.md` and, if it exists, the weekly ritual in `10_<org>/` (rituais). They define the format; this skill only runs it.
3. Select clients: the slug given, or every client with a ledger file, decision or analysis dated in the last 7 days, plus clients whose `estado.md` is older than 14 days but have an owner.
4. For each selected client, delegate the rewrite of `estado.md` to the `curador` subagent with: the client folder path, the window (today minus 14 days), and the rule that every line ends with a reference to its source file. The curator returns the new content and the list of contradictions found.
5. Write each `estado.md`, bump `atualizado`, keep closed items only within the 14-day window (older ones live in ledger and decisions).
6. `python3 scripts/brain.py validate`; fix errors.
7. Branch `estado-quente/AAAA-MM-DD` (or the session's `claude/` branch), commit only these files, push, open a PR listing per client: open items count, closed items count, contradictions, missing owner.
8. If nothing changed, do not open a PR: finish with one line, `estado quente sem mudanças`.
