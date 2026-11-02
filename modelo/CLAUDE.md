@00_susano/nucleo.md
@AGENTS.md

# Susano in Claude Code (managed: changes only through a model version)

Above: the method's core (`00_susano/nucleo.md`; full identity in `00_susano/identidade.md`) and this repository's rules (`AGENTS.md`). Claude Code specifics:

1. Work from the repository root: settings, hooks and permissions load from there. If the opening context warns otherwise, ask the person to reopen at the root.
2. `/frente <slug>` before frente-specific work (P-06).
3. Method on demand: start from `00_susano/situacoes.md`; the `susano-*` skills are the domain indexes (`susano-ativos` when the gargalo is named, `susano-exemplos` before producing). Second-brain procedures are canonical in `00_susano/metodo/`: when a skill disagrees, the method wins and you flag [CONTRADIÇÃO].
4. Hooks block secrets, CPF, cards and the em dash at write time, and also block when they fail. Never work around a hook (for example by writing through Bash).
5. Numbers in Python, never estimated in prose; raw pulls stay in `bruto/` (ignored). Evidence from the knowledge base: the `pesquisador` subagent, with paths.

Commands: `/cerebro`, `/frente <slug>`, `/analise`, `/ingerir <material>`, `/salve` (persist, regenerate map and hot, validate, PR), `/nova-frente <slug>`, `/onboarding`, `/estado-quente`, `/brain-audit`.

When compacting, preserve: the active frente, the person's name, and every decision, open item or number from this session not yet saved with `/salve`.
