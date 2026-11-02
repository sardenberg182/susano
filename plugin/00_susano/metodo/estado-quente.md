---
id: metodo-estado-quente
tipo: procedimento
atualizado: 2026-10-31
fonte: modelo de segundo cérebro adaptado pelo Sarden
---

# Estado quente: a foto de 14 dias de cada frente

`estado.md` é o que alguém lê para entrar numa frente em dois minutos.

## Formato

```
---
id: estado-<slug>
tipo: estado
dono: <usuário do GitHub>
atualizado: AAAA-MM-DD
---
# Estado: <slug>
## Aberto agora
## Fechado nos últimos 14 dias
## Próximos prazos
## Riscos e alertas
```

Cada linha leva data e referência (ledger, decisão ou análise). Sem interpretação nova: o estado resume o que já está registrado.

## Refresh semanal (`/estado-quente` ou rotina)

1. Frentes ativas: as que tiveram ledger, decisão ou análise nos últimos 14 dias.
2. Para cada uma, reconstruir o estado a partir do ledger recente, de `decisoes.md` e das análises: o que abriu, o que fechou, o que vence.
3. Item fechado há mais de 14 dias sai do estado (continua no ledger).
4. Atualizar `atualizado`, rodar `brain.py validate` e abrir um PR único com todas as frentes.
5. Na rotina sem supervisão: nunca editar arquivos gerenciados, nunca chamar sistema externo, nunca fazer merge. Frente com dado faltando é reportada como falha, nunca como "sem novidade".
