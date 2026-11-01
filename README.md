# susano: a sombra do Sarden

Repositório do Susano, a sombra do Sarden: o método, o DNA, a biblioteca, as referências e o motor com que Matheus Sardenberg (Sarden) cria os seus projetos. Uma fonte só (`modelo/00_susano/`), dois jeitos de usar:

| Você quer | Use | Como |
|---|---|---|
| a sombra no projeto que você já tem (qualquer repositório, terminal, desktop ou IDE) | o **plugin** do Claude Code | `/plugin marketplace add sardenberg182/susano` e `/plugin install susano@susano` |
| o segundo cérebro completo: estrutura de pastas, `brain.py`, guardas, CI, mapa e estado quente (funciona também na nuvem do claude.ai/code) | o **template** Copier | `copier copy --vcs-ref v0.2.1 gh:sardenberg182/susano meu-projeto` |

O método é do Sarden; o contexto, os dados e as decisões de cada projeto ficam no próprio projeto. Nos dois caminhos a abertura da sessão carrega só o núcleo (`00_susano/nucleo.md`, cerca de 2 mil tokens); o resto do método chega por skills, quando a tarefa pede.

## Caminho 1: plugin

```
/plugin marketplace add sardenberg182/susano
/plugin install susano@susano
/output-style Susano        (opcional: o tom já vem no núcleo)
```

No terminal, `claude plugin marketplace add sardenberg182/susano` e `claude plugin install susano@susano`. Para testar a partir de um clone: `claude --plugin-dir ./plugin`. O que vem: hook de abertura com o núcleo, 9 skills (`susano-ativos`, `susano-metodo`, `susano-biblioteca`, `susano-performance`, `susano-analytics`, `susano-gtm`, `susano-plataformas`, `susano-rituais`, `susano-analise`), o subagente `susano:pesquisador` e o estilo de saída. Detalhes em `plugin/README.md`; custo projetado com `claude plugin details susano` (medido em 01/11/2026: cerca de 600 tokens sempre ligados em descrições, mais o núcleo injetado pelo hook).

Sessão na nuvem (claude.ai/code) não carrega plugin instalado na máquina: lá, use o template.

## Caminho 2: template

```
pip install copier
copier copy --vcs-ref v0.2.1 gh:sardenberg182/susano meu-projeto
```

O Copier pergunta: `org` (vira `10_<org>/`), `org_nome`, `frentes` (vira `20_<frentes>/`, padrão `clientes`), `dono` (usuário do GitHub que aprova os PRs) e `idioma`. Depois: `git init`, `python3 scripts/brain.py mapa`, `validate`, `susano-check`, suba para o GitHub e rode `/onboarding` no Claude Code. O `AGENTS.md` gerado explica a ordem de leitura para qualquer outro agente (Codex, Cursor, Gemini CLI, Copilot).

Atualizar um projeto: na raiz, `copier check-update`; numa branch, `copier update --vcs-ref vX.Y.Z`, `brain.py validate`, `brain.py susano-check` e PR "susano vX.Y.Z" para o dono aprovar.

## Lançar uma versão (quem mantém o modelo)

1. Mudança em `modelo/` num PR. Linha no `CHANGELOG.md` (a versão do plugin vem dela).
2. `python3 modelo/scripts/brain.py --raiz modelo indice`, `skills` e `manifesto`.
3. `python3 ferramentas/construir_plugin.py`: regenera `plugin/` e `.claude-plugin/marketplace.json` e roda `claude plugin validate`.
4. `bash testes/testar_modelo.sh` (gera projeto temporário: validate, susano-check, testar_camada) e `bash testes/testar_plugin.sh`.
5. Merge, tag `vX.Y.Z`. O Raijin propõe, o Sarden aprova.

## Quem é o Sarden

Matheus Sardenberg, Sarden: estrategista de receita e generalista de growth, CRO da Tegrus (boutique brasileira de Growth e RevOps). O Susano é a sombra de mais de 10 mil horas: projeto, análise, modelo de negócio e o dia a dia que faz uma operação de receita rodar. Perfil em `modelo/00_susano/sobre_o_sarden.md`.

## O que mora onde

| Repositório | Conteúdo | Acesso |
|---|---|---|
| `susano` (este) | a sombra: método, DNA, biblioteca, referências, motor e estrutura, como template (`modelo/`) e como plugin (`plugin/`) | público em github.com/sardenberg182/susano desde 01/11/2026: CC BY 4.0 no conteúdo, MIT no código (decisão do Sarden, 01/11/2026) |
| Oficina (template `persona`) | o Sarden como pessoa (identidade, voz de autor), aplicado só na máquina dele: o projeto ignora `00_pessoal/` e `CLAUDE.local.md`, então nada pessoal entra no Git de um projeto | privado |

Licença: `LICENSE` (código, MIT), `LICENSE-CONTEUDO.md` (conteúdo, CC BY 4.0) e `modelo/00_susano/LICENCA.md` (aviso que vai para cada projeto). Autor: Matheus Sardenberg (Sarden).
