# Rotina: estado quente semanal (tarefa agendada na nuvem)

Configuração para criar em claude.ai/code/routines (ou `/schedule` no Claude Code), na conta de quem é curador do repositório. A tarefa pertence a essa conta: roda com o GitHub e o uso dela, e os commits saem no nome dela.

| Campo | Valor |
|---|---|
| Nome | `susano-estado-quente-semanal` |
| Gatilho | Schedule, cron `CRON_TZ=America/Sao_Paulo 37 7 * * 1` (segunda, 07:37) |
| Repositório | o repositório do projeto (o app do Claude no GitHub precisa estar instalado nele) |
| Ambiente | Default (rede Trusted); nenhuma variável, nenhum segredo |
| Conectores | Nenhum: remova todos que vierem marcados |
| Modelo | Sonnet (o subagente curador usa Opus por conta própria) |

## Prompt (colar como está)

```text
You are running the weekly hot-state refresh of this repository as an unattended scheduled task. Work at the repository root.

1. Run the /estado-quente skill exactly as written in .claude/skills/estado-quente/SKILL.md, for all active clients.
2. Push to a claude/ branch and open a pull request to main with gh pr create when it is available; otherwise leave the branch pushed and finish by printing its name.
3. Never edit 40_playbooks/, .claude/, .github/ or scripts/. Never call external systems, never send messages, never merge.
4. If nothing changed, do not open a pull request; finish with one line: estado quente sem mudanças.

Write every file and message in Brazilian Portuguese (PT-BR) and never use the em dash character.
```

## Antes de ligar

1. Rodar uma vez com **Run now** e ler a sessão gerada: a doc avisa que o status "Succeeded" diz como a sessão terminou, não se o trabalho foi feito.
2. Conferir no PR que só arquivos `estado.md` mudaram e que cada linha termina com a referência da fonte.
3. Só então deixar o agendamento ligado.
