---
name: nova-frente
description: Create the folder of a new frente with scripts/brain.py, run a short intake to fill the context, regenerate the map and open the pull request.
disable-model-invocation: true
argument-hint: "<slug> [Nome do Cliente]"
allowed-tools:
  - Read
  - Edit
  - Write
  - Bash(python3 scripts/brain.py *)
---

Always answer in PT-BR.

1. Confirm the slug (kebab-case), the client's display name and the owner: the Growth Leader responsible and their GitHub handle. One question with defaults if anything is missing.
2. Run `python3 scripts/brain.py --help` and the help of its "novo" command to get the exact syntax, then create the client with it, passing the owner's GitHub handle when the command accepts it (that is what feeds CODEOWNERS). Never create the folder by hand.
3. Intake, asked in one message, partial answers accepted: o que o cliente vende; modelo (B2B ou B2C, high-touch ou low-touch); ICP; canais ativos; stack (CRM, mídia, automação, analytics) com IDs de conta sem credencial; metas do período com número, data e fonte; stakeholders por papel (entram em `10_<org>/pessoas/` só com o OK do dono, com papel e relação, nunca contato); escopo da organização (sem valores financeiros); onde está o material bruto.
4. Fill the files the command created, following `CONVENCOES.md`. Unknown fields stay as [LACUNA] with the question that would fill them.
5. `python3 scripts/brain.py mapa`, `python3 scripts/brain.py validate`, then `/salve` to open the PR. The owner reviews it.
