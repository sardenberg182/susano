# Como contribuir (gerenciado pelo modelo Susano)

## Fluxo de todo trabalho

1. Branch a partir da `main` atualizada, com a convenção única do método: `salve/AAAA-MM-DD-<tema>` para trabalho de sessão, `estado-quente/AAAA-MM-DD` para o refresh semanal, `susano-vX.Y.Z` para versão do modelo (`/salve` já faz isso; sessão na nuvem que nasceu numa branch `claude/...` mantém a dela).
2. Mudanças com `brain.py validate` e `brain.py susano-check` sem erro.
3. PR com resumo por frente; o dono no `.github/CODEOWNERS` aprova. Ninguém faz merge do próprio PR.

## Configuração do repositório no GitHub (uma vez, pelo dono)

As regras "nunca commit na `main`" e "o dono aprova" só viram trava real com a proteção da branch no GitHub; sem ela, são instrução para pessoas e agentes, não bloqueio. Ao criar o repositório:

1. Proteger a `main`: exigir pull request, exigir revisão do CODEOWNERS, bloquear force push e exclusão da branch, incluir administradores.
2. Exigir o check `validar` (job do workflow `brain`, em `.github/workflows/brain.yml`) antes do merge: sem isso, o CI informa mas não barra.
3. Em repositório público, deixar a execução de workflows de PR de fork exigindo aprovação (padrão do GitHub para colaboradores novos).

## Versão nova do modelo

1. `copier check-update` mostra se há versão nova do `susano`. Leia o `CHANGELOG.md` dela antes.
2. Numa branch `susano-vX.Y.Z` a partir da `main` limpa: `copier update --vcs-ref vX.Y.Z`. O Copier troca os gerenciados e não toca nos arquivos do projeto (`AGENTS.md`, frentes, `10_` a `90_`, `_templates/`).
3. `python3 scripts/brain.py migrar`: aplica o contrato da versão ao que é do projeto (bloco gerenciado do `AGENTS.md`, arquivos obrigatórios de cada frente). Idempotente; nunca sobrescreve arquivo preenchido. AGENTS.md anterior ao bloco vai para `90_arquivo/` e a saída diz o que conferir.
4. `validate` e `susano-check` sem erro; `git diff main` para ler o que mudou (gerenciados, AGENTS.md, arquivos criados). Conflito do Copier (`.rej` ou marcadores no arquivo) se resolve antes do PR, nunca apagando conteúdo do projeto.
5. PR "susano vX.Y.Z"; o dono do projeto aprova. Desfazer: feche o PR e apague a branch; depois do merge, `git revert` do merge volta a versão anterior.
6. Nunca editar `.copier-answers.yml` à mão.

## Arquivos gerenciados

`00_susano/`, `.claude/`, `scripts/`, `.github/workflows/`, `CLAUDE.md`, `SUSANO.md`, `CONVENCOES.md` e `CONTRIBUTING.md` só mudam por versão do modelo. PR que altera um deles fora de uma versão falha no `susano-check`. Melhoria que vale para todos os projetos vira proposta ao Sarden, dono do modelo; o que é só deste projeto vai para `40_playbooks/`.

## Propriedade

O método, a estrutura e o motor deste repositório pertencem ao Sarden e seguem a licença em `00_susano/LICENCA.md`. Contribuição de terceiro ao modelo só entra com cessão por escrito.
