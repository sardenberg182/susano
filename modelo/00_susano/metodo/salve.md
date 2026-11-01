---
id: metodo-salve
tipo: procedimento
atualizado: 2026-10-31
fonte: modelo de segundo cérebro (Okamoto) adaptado pelo Sarden; raio_doc9
---

# Salve: persistir o que a sessão produziu

Roda no fim de toda sessão que produziu algo que deve sobreviver a ela (`/salve`).

## 1. Listar

Uma linha por item: tipo (decisão, pendência, status, prazo, métrica, pessoa nova, análise, aprendizado de método), slug da frente ou `org`, trecho factual sem interpretação, fonte com data (reunião, mensagem, documento, sistema) e referência à evidência (caminho ou link, nunca o conteúdo bruto). Se nada precisa sobreviver, diga isso e pare.

## 2. Gravar no lugar certo

| Item | Destino |
|---|---|
| Fato de uma frente | linha no ledger do dia: `20_<frente>/<slug>/ledger/AAAA-MM-DD.md` (`ts \| fonte \| quem \| quem_tipo \| trecho \| ref`) |
| Algo aberto ou fechado | `estado.md` da frente: "Aberto agora", "Fechado nos últimos 14 dias", "Próximos prazos"; atualizar `atualizado` |
| Decisão | `decisoes.md` da frente: nova decisão no topo com data e dono; a substituída ganha `[SUBSTITUÍDA em AAAA-MM-DD por D-NN]` e nunca é apagada |
| Análise ou entregável | `20_<frente>/<slug>/analises/AAAA-MM-DD_<tema>.md` |
| Fato da organização | o arquivo de `10_<org>/` que o README indicar |
| Aprendizado de método (vale para todo projeto) | nunca editar `00_susano/`: proposta ao dono no corpo do PR, seção "Proposta para o modelo" |

## 3. Validar

`python3 scripts/brain.py validate` e `python3 scripts/brain.py susano-check`. Corrigir todo erro. Aviso: corrigir ou explicar no PR.

## 4. Abrir o PR

Branch `salve/AAAA-MM-DD-<tema>`, commit com mensagem curta em PT-BR, push e `gh pr create` com: o que mudou por frente, decisões novas, pendências e a seção de proposta para o modelo, se houver. Nunca fazer merge: o dono no CODEOWNERS aprova.
