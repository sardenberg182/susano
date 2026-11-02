---
paths:
  - "20_*/**"
---

# Frente folders (20_<frente>)

- Structure and frontmatter are canonical in `CONVENCOES.md`. Read its frente section before creating or changing a file here; do not invent fields or file names.
- Each frente folder is self-contained: `README.md` (ficha and map), `contexto.md`, `estado.md`, `decisoes.md`, and on demand `ledger/`, `reunioes/`, `analises/`.
- Isolation: facts from one frente never appear in another frente's files or analysis. A cross-frente comparison happens only on explicit request, in a file outside the frente folders, with every number labeled by frente.
- `estado.md` is the hot state (open now, closed in the last 14 days); follow `00_susano/metodo/estado-quente.md` and bump `atualizado` whenever you touch it.
- `experimentos.md` holds the frente's experiments (`E-NN | data | hipótese | alavanca | corte | status | resultado | decisão e ref`); a hypothesis without a cut (number and deadline) does not enter; "sistematizou" points to the playbook or process it became.
- Decisions are never deleted: a replaced decision is marked as superseded and points to the new one.
- Contract values and fees of the client never enter the frente folder; record where they live (system and ID). Pricing mechanics of the method, without client numbers, may be cited.
- Ledger entries follow `00_susano/metodo/salve.md`: short facts with date, source and reference to the evidence, without interpretation.
- Targets come only from what the frente registers. A metric without a registered target is [LACUNA]; never borrow another frente's target or an unsourced benchmark.
- No contract values or fees. Contacts appear by name and role only, never with personal phone or personal e-mail.
