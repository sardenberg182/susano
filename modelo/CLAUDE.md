@00_susano/nucleo.md
@AGENTS.md

# Susano in Claude Code (managed file: changes only through a model version)

The core above is Sarden's method (`00_susano/nucleo.md`; full version in `00_susano/identidade.md`). `AGENTS.md` holds this repository's own rules. This section adds what Claude Code needs.

1. **Repository root only.** Settings, hooks and permissions load from the directory where the session starts; if the opening context warns otherwise, ask the person to reopen at the root.
2. **One frente at a time.** `/frente <slug>` before frente-specific work (P-06).
3. **Method on demand.** Only the core loads at start. The method lives in skills: `susano-ativos` (active models: load before concluding an analysis, diagnosis, strategy or plan), `susano-metodo`, `susano-biblioteca`, `susano-performance`, `susano-analytics`, `susano-gtm`, `susano-plataformas`, `susano-rituais`. Each is an index: open only the file the task needs and cite `caminho#seção`; `00_susano/INDICE.md` maps everything. Brain procedures are canonical in `00_susano/metodo/`; when a skill and the method disagree, the method wins and you flag [CONTRADIÇÃO].
4. **Managed files are read-only here.** `00_susano/`, `.claude/`, `scripts/`, `.github/workflows/`, `CLAUDE.md`, `SUSANO.md`, `CONVENCOES.md`, `CONTRIBUTING.md` change only through a model version (`copier update` PR). A method improvement becomes a proposal to the owner, never a local edit.
5. **Validate, branch, PR.** `python3 scripts/brain.py validate` after every change, `susano-check` before a PR. Never commit to `main`, never merge: `/salve` opens branch and PR; the CODEOWNERS owner approves.
6. **Numbers in Python**, never estimated in prose; raw pulls stay in `bruto/` (ignored).
7. **Privacy.** Hooks block secrets, CPF, cards and the em dash at write time; never work around a hook (for example by writing through Bash). Stakeholders enter `10_<org>/pessoas/` only with the owner's OK, through `python3 scripts/brain.py pessoa <slug> ... --aprovado-por <dono>`, role and relation only.
8. **External actions** (send, publish, submit, delete in CRM, ads, e-mail, WhatsApp) need the person's explicit approval in the same turn.
9. **Generated files.** `MAPA.md` and `10_<org>/hot.md` come from `brain.py mapa` and `brain.py hot`, never by hand. "O que ficou combinado com X?" is answered with file and line: `python3 scripts/brain.py fonte "X"`.

Commands: `/cerebro` (briefing), `/frente <slug>`, `/analise` (FATO → análise vs target → PA), `/ingerir <material>`, `/salve` (persist, regenerate map and hot, validate, PR), `/nova-frente <slug>`, `/onboarding`, `/estado-quente`, `/brain-audit`; `python3 scripts/brain.py mapa | hot | fonte "<termo>" | tokens`. Evidence from the knowledge base: delegate to the `pesquisador` subagent and cite paths.

When compacting, preserve: the active frente, the person's name, and every decision, open item or number produced in this session that was not saved with `/salve` yet.
