# Pessoas (stakeholders)

Um arquivo por stakeholder externo ao time (cliente, parceiro, fornecedor, conselheiro), criado com `python3 scripts/brain.py pessoa <slug> --nome ... --papel ... --relacao ... --aprovado-por <dono>` (modelo em `_templates/pessoa.md`). Serve para o Susano saber quem é quem numa frente e o que ficou combinado com cada um, com fonte.

Regras (a trava está em `scripts/brain.py validate`):

- Entrada só com OK do dono do repositório, registrado no campo `aprovado_por` (usuário do GitHub) e na data. Sem esse campo o `validate` barra.
- Só papel e relação de trabalho: `papel` (cargo ou função), `relacao` (frente ou projeto em que a pessoa atua e desde quando). Nada de telefone, e-mail, endereço, saúde, família ou finanças: contato pessoal fica no sistema de origem (CRM, agenda), e aqui entra só "onde achar" (sistema e ID).
- O que ficou combinado com a pessoa não mora aqui: mora em `decisoes.md` e `ledger/` da frente. `python3 scripts/brain.py fonte "<nome>"` devolve arquivo e linha.
