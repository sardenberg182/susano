---
paths:
  - "10_*/pessoas/**"
---

# Stakeholders (10_<org>/pessoas)

- One file per external stakeholder, created with `python3 scripts/brain.py pessoa <slug> --nome ... --papel ... --relacao ... --frentes ... --aprovado-por <dono>` (the command refuses to run without the owner's handle and refuses contact data in the arguments); `_templates/pessoa.md` shows the shape. Frontmatter is mandatory: `id`, `tipo: pessoa`, `papel`, `relacao`, `aprovado_por`, `atualizado` (`brain.py validate` blocks a file without them).
- Gate: a person enters only with the repository owner's explicit OK in this session, recorded in `aprovado_por`. No OK, no file: say so and keep the fact in the frente's ledger with the person's name only.
- Role and working relation only. Never phone, e-mail, address, health, family or finances; `contato_em` records the system and ID where the contact lives, never the value. The content guard asks on any contact pattern; in this folder, `validate` treats it as an error.
- What was agreed with the person lives in the frente's `decisoes.md` and `ledger/`, not here. Answer "o que ficou combinado com X" with `python3 scripts/brain.py fonte "X"` and cite file and line.
