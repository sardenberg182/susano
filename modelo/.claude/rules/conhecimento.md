---
paths:
  - "00_susano/**"
  - "10_*/**"
  - "30_projetos/**"
  - "40_playbooks/**"
  - "50_referencia/**"
  - "90_arquivo/**"
---

# Method, organization and reference files

- `00_susano/` is Sarden's method, managed by the `susano` model: read it, apply it, never edit it here. A method improvement becomes a proposal to the owner in the `/salve` pull request ("Proposta para o modelo").
- Inside `00_susano/`: `ATIVOS.md` (always loaded) lists the active models; `INDICE.md` maps everything else; `biblioteca/` holds thinkers, `dna/` Sarden's own frameworks, `metodo/` the second-brain procedures, `instrucoes/` the operating instructions (GP/BP, project onboarding), `referencias/` platforms and analytics.
- `40_playbooks/` holds this organization's own processes, not the method. Never rewrite a playbook to fit one frente.
- `50_referencia/` holds external knowledge used only here, as a pair: a deep file and a compact file. Read the compact one first.
- Frontmatter, `tipo` values, validity (`revisar_ate`) and naming are canonical in `CONVENCOES.md`. Copy from `_templates/` instead of starting from scratch.
- Every change updates `atualizado`. No silent edits. Nothing is deleted: superseded content moves to `90_arquivo/` with a pointer.
- After any change run `python3 scripts/brain.py validate`.
