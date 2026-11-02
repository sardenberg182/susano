# susano: a sombra do Sarden

Repositório do Susano, a sombra do Sarden: o método, o DNA, a biblioteca, as referências e o motor com que Matheus Sardenberg (Sarden) cria os seus projetos. Uma fonte só (`modelo/00_susano/`), três jeitos de usar:

| Você quer | Use | Como |
|---|---|---|
| a sombra no projeto que você já tem (qualquer repositório, terminal, desktop ou IDE) | o **plugin** do Claude Code | `/plugin marketplace add sardenberg182/susano` e `/plugin install susano@susano` |
| o segundo cérebro completo: estrutura de pastas, `brain.py`, guardas, CI, mapa e estado quente (funciona também na nuvem do claude.ai/code) | o **template** Copier | `copier copy --vcs-ref v0.2.1 gh:sardenberg182/susano meu-projeto` |
| a sombra numa conversa, sem repositório (Project do claude.ai, GPT do ChatGPT, Gem do Gemini) | o **pacote de chat** | `python3 ferramentas/gerar_pacote_chat.py` e cole os dois arquivos gerados |

O método é do Sarden; o contexto, os dados e as decisões de cada projeto ficam no próprio projeto. Nos três caminhos a abertura da sessão carrega só o núcleo (`00_susano/nucleo.md`, cerca de 2 mil tokens); o resto do método chega por skills (ou pelo índice, no chat), quando a tarefa pede.

O que carrega quando:

| Momento | O que entra | De onde |
|---|---|---|
| abertura da sessão | `00_susano/nucleo.md` (identidade, hierarquia, tom, formato) | hook do plugin, `CLAUDE.md` do template, system prompt no chat |
| primeira leitura depois do núcleo | `00_susano/situacoes.md`: o que a pessoa diz → modo → o que abrir | o próprio núcleo manda |
| quando a tarefa pede | o arquivo do método que a situação aponta (DNA, instrução, referência, exemplo do mesmo modo), por skill `susano-*` ou pelo caminho | `00_susano/INDICE.md` |
| dúvida entre agir e perguntar | `00_susano/calibracao.md` | sob demanda |

Mantém o modelo: o Raijin, agente de manutenção da operação do Sarden. O Raijin propõe por PR, o Sarden aprova; nada entra na `main` sem o OK dele.

## Caminho 1: plugin

```
/plugin marketplace add sardenberg182/susano
/plugin install susano@susano
/output-style Susano        (opcional: o tom já vem no núcleo)
```

No terminal, `claude plugin marketplace add sardenberg182/susano` e `claude plugin install susano@susano`. Para testar a partir de um clone: `claude --plugin-dir ./plugin`. O que vem: hook de abertura com o núcleo, 10 skills (`susano-ativos`, `susano-metodo`, `susano-biblioteca`, `susano-performance`, `susano-analytics`, `susano-gtm`, `susano-plataformas`, `susano-rituais`, `susano-exemplos`, `susano-analise`), o subagente `susano:pesquisador` e o estilo de saída. Detalhes em `plugin/README.md`; custo projetado com `claude plugin details susano` (medido em 01/11/2026: cerca de 600 tokens sempre ligados em descrições, mais o núcleo injetado pelo hook).

Sessão na nuvem (claude.ai/code) não carrega plugin instalado na máquina: lá, use o template.

## Caminho 2: template

```
pip install copier
copier copy --vcs-ref v0.2.1 gh:sardenberg182/susano meu-projeto
```

O Copier pergunta: `org` (vira `10_<org>/`), `org_nome`, `frentes` (vira `20_<frentes>/`, padrão `clientes`), `dono` (usuário do GitHub que aprova os PRs) e `idioma`. Depois: `git init`, `python3 scripts/brain.py mapa`, `validate`, `susano-check`, suba para o GitHub e rode `/onboarding` no Claude Code. O `AGENTS.md` gerado explica a ordem de leitura para qualquer outro agente (Codex, Cursor, Gemini CLI, Copilot).

Atualizar um projeto: na raiz, `copier check-update`; numa branch, `copier update --vcs-ref vX.Y.Z`, `brain.py validate`, `brain.py susano-check` e PR "susano vX.Y.Z" para o dono aprovar.

## Caminho 3: Project de chat (claude.ai, ChatGPT, Gemini)

Para quem não tem repositório nem terminal. O pacote é gerado da mesma fonte:

```
python3 ferramentas/gerar_pacote_chat.py            # escreve em dist/chat/
```

Saem dois arquivos: `SYSTEM_PROMPT.md` (o `nucleo.md`, a `identidade.md` e o `situacoes.md` concatenados, com a nota de modo sem shell no fim) e `susano_conhecimento.zip` (a pasta `00_susano/` inteira, sem o `MANIFEST.sha256`). No Project do claude.ai: o `SYSTEM_PROMPT.md` vai em instruções do projeto e o conteúdo do zip vai em conhecimento do projeto; no GPT ou no Gem, o equivalente (instruções e arquivos).

Regras do modo sem shell, que o próprio `SYSTEM_PROMPT.md` carrega: o Susano lê o método pelos caminhos do `INDICE.md` (não há skills), não roda `brain.py`, não abre PR e não escreve em repositório; entrega no chat e termina toda sessão de trabalho com a lista do que deveria ser salvo e onde (`20_<frente>/<slug>/contexto.md`, `estado.md`, `decisoes.md`, `experimentos.md`), para quem tem o repositório fazer o `/salve`. Contexto da frente entra colado na conversa ou como arquivo do Project; nunca inventado.

## Lançar uma versão (quem mantém o modelo)

1. Mudança em `modelo/` num PR. Linha no `CHANGELOG.md` (a versão do plugin vem dela).
2. `python3 modelo/scripts/brain.py --raiz modelo indice`, `skills` e `manifesto`.
3. `python3 ferramentas/construir_plugin.py`: regenera `plugin/` e `.claude-plugin/marketplace.json` e roda `claude plugin validate`.
4. `bash testes/testar_modelo.sh` (gera projeto temporário: validate, susano-check, testar_camada) e `bash testes/testar_plugin.sh`.
5. `testes/casos_decisao.md`: rodar os casos no agente (à mão ou `claude -p`) e registrar a concordância na tabela do arquivo e no `CHANGELOG.md`.
6. Merge, tag `vX.Y.Z`. O Raijin propõe, o Sarden aprova.

Proposta de quem usa o modelo: issue "Proposta para o modelo" (template em `.github/ISSUE_TEMPLATE/`), sem dado de cliente; o Raijin revisa, o Sarden aprova.

## Quem é o Sarden

Matheus Sardenberg, Sarden: estrategista de receita e generalista de growth, CRO da Tegrus (boutique brasileira de Growth e RevOps). O Susano é a sombra de mais de 10 mil horas: projeto, análise, modelo de negócio e o dia a dia que faz uma operação de receita rodar. Perfil em `modelo/00_susano/sobre_o_sarden.md`.

## O que mora onde

| Repositório | Conteúdo | Acesso |
|---|---|---|
| `susano` (este) | a sombra: método, DNA, biblioteca, referências, motor e estrutura, como template (`modelo/`) e como plugin (`plugin/`) | público em github.com/sardenberg182/susano desde 01/11/2026: CC BY 4.0 no conteúdo, MIT no código (decisão do Sarden, 01/11/2026) |
| Oficina (template `persona`) | o Sarden como pessoa (identidade, voz de autor), aplicado só na máquina dele: o projeto ignora `00_pessoal/` e `CLAUDE.local.md`, então nada pessoal entra no Git de um projeto | privado |

Licença: `LICENSE` (código, MIT), `LICENSE-CONTEUDO.md` (conteúdo, CC BY 4.0) e `modelo/00_susano/LICENCA.md` (aviso que vai para cada projeto). Autor: Matheus Sardenberg (Sarden).
