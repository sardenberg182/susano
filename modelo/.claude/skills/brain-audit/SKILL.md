---
name: brain-audit
description: Monthly health audit of this repository: brain.py audit plus the qualitative pass (contradictions, superseded decisions, duplicates, stale method), safe fixes only, report in a pull request. Run monthly or when the audit issue opens.
disable-model-invocation: true
context: fork
agent: auditor
background: false
---

Audit this repository for this month and answer in PT-BR.

1. Read `00_susano/metodo/brain-audit.md` if it exists; it is canonical. If the monthly audit issue is open (`gh issue list` when `gh` is available), read it and use it as the starting list.
2. Run `python3 scripts/brain.py audit` (confirm the syntax with `--help`) and keep its output as the mechanical baseline: stale states, overdue reviews, missing owners, broken links.
3. Qualitative pass, each finding with path and evidence:
   - decisions marked current that a later decision or ledger entry contradicts;
   - the same fact with different values in two files ([CONTRADIÇÃO]);
   - duplicated or near-duplicated files in `40_playbooks/` and `50_referencia/`;
   - playbooks past their review date that sessions still cite;
   - Susano skills in `.claude/skills/` with no mention in ledgers or PRs in 30 days (standby) or 90 days (propose archiving under `90_arquivo/`, never delete);
   - `CLAUDE.md`, rules or `estado.md` files that grew past what a session should load.
4. Fix only safe items (broken internal links, obvious typos in metadata). Everything else becomes a PA with owner and date.
5. Write the report where the playbook says, or in `10_<org>/` following `CONVENCOES.md`: FATO (counts) → achados concretos com caminho → PA. A report that says everything is fine without counts is a failure.
6. Validate, branch, commit, push and open the PR; link the audit issue when there is one.
