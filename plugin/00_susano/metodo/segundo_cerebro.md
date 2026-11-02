---
id: metodo-segundo-cerebro
tipo: procedimento
atualizado: 2026-10-31
fonte: modelo de segundo cérebro adaptado pelo Sarden
---

# Segundo cérebro: como este repositório pensa

## Três pilares

- **Contexto** (o quê e por quê): arquivos de organização, frentes, decisões e referências.
- **Skills** (como): procedimentos em `00_susano/metodo/` executados pelas skills de `.claude/skills/`.
- **Rotinas** (quando): tarefas agendadas que rodam os procedimentos sem supervisão (exemplo: estado quente semanal).

## Três camadas

1. **Bruto**: transcrições, exportações, planilhas. Fica no sistema de origem ou em `bruto/`, que o Git ignora.
2. **Ledger**: fatos curtos e datados, sem interpretação, em `20_<frente>/<slug>/ledger/AAAA-MM-DD.md`. Colunas: `ts | fonte | quem | quem_tipo | trecho | ref`.
3. **Curado**: o que se lê para decidir: `contexto.md`, `estado.md`, `decisoes.md`, análises e playbooks.
4. **Experimentos**: hipótese → corte → resultado → decisão, em `experimentos.md` da frente. É o registro que fecha o ciclo de melhoria: o que matou sai da fila, o que sistematizou vira playbook.

Nada sobe do bruto direto para o curado: passa pelo ledger, com referência à evidência.

## Regras

- **Mapa em todo nível.** Cada pasta tem um `README.md` que diz o que mora ali; o repositório tem `MAPA.md` e `10_<org>/hot.md` (gerados); o método tem `INDICE.md` e a skill `susano-ativos`.
- **Estado quente de 14 dias.** `estado.md` mostra o que está aberto agora e o que fechou nos últimos 14 dias. Mais velho que isso vive no ledger e nas decisões.
- **Uma fonte por assunto.** Duas versões do mesmo assunto viram uma; a substituída vai para `90_arquivo/` com ponteiro.
- **Pastas são convenção, não isolamento.** O isolamento entre frentes é regra (`/frente`) mais revisão no PR.
- **Arquivo é verdade, memória é cache.** Antes de citar decisão, meta ou número, reabra a fonte.
- **Nada se apaga.** Decisão substituída é marcada; conteúdo velho vai para `90_arquivo/`.

## Fronteira: onde cada coisa mora

| Se vale para | Vai para |
|---|---|
| Todo projeto que usa o método | o modelo `susano` (proposta ao Sarden, nunca edição local) |
| Este projeto ou esta organização | as pastas `10_` a `50_` deste repositório |
| O Sarden como pessoa (voz, carreira) | a Oficina, que nunca abre |
| Dado sensível (credencial, dado pessoal, valor de contrato) | fora do Git |

Dado de cliente nunca entra no modelo `susano`.

## Escada de procedimento

Executar uma vez na mão → escrever o procedimento → testar num segundo caso real → só então virar rotina. Rotina sem dois casos reais não entra. "Sistematizar" é o nome dessa decisão quando um experimento vira playbook ou processo.

## Ciclo de vida das skills

Skill sem uso há 30 dias entra em standby (o brain audit aponta); há 90 dias vai para o arquivo. Nunca se exclui: o histórico mostra o que já foi tentado.

## Como o modelo evolui

Mudança no método nasce no repositório `susano`: PR → testes (projeto gerado passa `validate`, `testar_camada` e `susano-check`) → merge → tag → CHANGELOG. Cada projeto recebe a versão por `copier update`, num PR que o dono aprova. Melhoria nascida num projeto que vale para todos vira proposta ao Sarden; contribuição de terceiro só entra com cessão por escrito.
