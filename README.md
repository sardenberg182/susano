# susano: a sombra do Sarden

Repositório do Susano, a sombra do Sarden: o método, o DNA, a biblioteca, as referências e o motor com que Matheus Sardenberg (Sarden) cria os seus projetos. Uma fonte só (`modelo/00_susano/`), três jeitos de usar:

| Você quer | Use | Como |
|---|---|---|
| a sombra no projeto que você já tem (qualquer repositório, terminal, desktop ou IDE) | o **plugin** do Claude Code | `/plugin marketplace add sardenberg182/susano` e `/plugin install susano@susano` |
| o segundo cérebro completo: estrutura de pastas, `brain.py`, guardas, CI, mapa e estado quente (funciona também na nuvem do claude.ai/code) | o **template** Copier | `copier copy --vcs-ref v0.4.0 gh:sardenberg182/susano meu-projeto` |
| a sombra numa conversa, sem repositório (Project do claude.ai) | o **pacote de chat** | `python3 ferramentas/gerar_pacote_chat.py` e siga o `LEIA-ME.md` gerado |

O método é do Sarden; o contexto, os dados e as decisões de cada projeto ficam no próprio projeto. Nos três caminhos a abertura da sessão carrega só o núcleo (`00_susano/nucleo.md`, cerca de 2 mil tokens); o resto do método chega por skills (ou pelo índice, no chat), quando a tarefa pede.

O que carrega quando:

| Momento | O que entra | De onde |
|---|---|---|
| abertura da sessão | `00_susano/nucleo.md` (identidade, hierarquia, tom, formato) | hook do plugin, `CLAUDE.md` do template, instruções do Project no chat |
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
pipx install copier        (ou: uv tool install copier)
copier copy --vcs-ref v0.4.0 gh:sardenberg182/susano meu-projeto
```

`pip install copier` direto falha no Python do Homebrew e em outros ambientes gerenciados (PEP 668); `pipx` e `uv tool` instalam o Copier isolado. Requisitos: para gerar e atualizar, Python 3.10 ou mais novo (o Copier 9.19 exige); no projeto, Python 3.9 ou mais novo, git e Claude Code 2.1.295 ou mais novo (abaixo disso, as travas de privacidade podem liberar a escrita quando estouram o tempo).

O Copier pergunta: `org` (vira `10_<org>/`), `org_nome`, `frentes` (vira `20_<frentes>/`, padrão `clientes`), `dono` (usuário do GitHub que aprova os PRs) e `idioma`. Depois: `git init`, `python3 scripts/brain.py mapa`, `validate`, `susano-check`, suba para o GitHub e rode `/onboarding` no Claude Code. O `AGENTS.md` gerado explica a ordem de leitura para qualquer outro agente (Codex, Cursor, Gemini CLI, Copilot).

Atualizar um projeto: na raiz, `copier check-update`; numa branch `susano-vX.Y.Z`, `copier update --vcs-ref vX.Y.Z`, depois `python3 scripts/brain.py migrar` (bloco gerenciado do `AGENTS.md` e arquivos obrigatórios das frentes, sem tocar no que é do projeto), `validate`, `susano-check`, leitura do `git diff main` e PR "susano vX.Y.Z" para o dono aprovar. Detalhe e como desfazer: `CONTRIBUTING.md` do projeto.

## Caminho 3: Project de chat (claude.ai)

Para quem não tem repositório nem terminal. O pacote é gerado da mesma fonte:

```
python3 ferramentas/gerar_pacote_chat.py            # escreve em dist/chat/
```

Saem: `INSTRUCOES_DO_PROJETO.md` (o núcleo adaptado ao chat e as regras do modo sem shell, cerca de 6,5 mil caracteres: vai nas instruções do Project), `essencial/` (operação, identidade, DNA, instruções, exemplos e procedimentos, cerca de 90 mil tokens estimados: cabe no contexto do Project) e `completo/` (o método inteiro, cerca de 430 mil tokens estimados: passa do contexto e depende da busca automática do plano), os dois com o nome do arquivo achatado (`dna/metodo/x.md` vira `dna__metodo__x.md`, porque o Project mostra só o nome) e um `MAPA_DE_ARQUIVOS.md` que liga cada nome ao caminho canônico. Mais `LEIA-ME.md` (procedimento, limites com fonte e data, quatro perguntas de teste de recuperação), licenças, `MANIFEST.sha256` e um ZIP com tudo. Arquivo do método idêntico à fonte, byte a byte (o CI confere).

Destino suportado: Project do claude.ai. GPT do ChatGPT e Gem do Gemini podem receber o mesmo pacote, mas não são testados.

Regras do modo sem shell, que as próprias instruções carregam: o método chega pelo conhecimento do Project (não há skills, `brain.py`, `/frente` nem `/salve`); arquivo que não está carregado é dito como tal, nunca reconstruído de memória; nada é escrito nem prometido salvar; toda sessão de trabalho termina com a lista do que deveria ser salvo e onde (`20_<frente>/<slug>/contexto.md`, `estado.md`, `decisoes.md`, `experimentos.md`), para quem tem o repositório fazer o `/salve`. Contexto da frente entra colado na conversa ou como arquivo do Project; nunca inventado.

## Lançar uma versão (quem mantém o modelo)

1. Mudança em `modelo/` num PR. Linha no `CHANGELOG.md` (a versão do plugin vem dela).
2. `python3 modelo/scripts/brain.py --raiz modelo indice`, `skills` e `manifesto`; `python3 ferramentas/construir_plugin.py` (regenera `plugin/` e `.claude-plugin/marketplace.json` e roda `claude plugin validate`).
3. Aceite mecânico (o mesmo do CI, job `testes`): `python3 modelo/scripts/brain.py --raiz . varrer --perfil publico`, `bash testes/testar_geradores.sh`, `bash testes/testar_modelo.sh`, `bash testes/testar_atualizacao.sh`, `bash testes/testar_plugin.sh` e `bash testes/testar_pacote_chat.sh`. O job `compatibilidade` repete o modelo no Python 3.9 e no macOS.
4. Avaliação com modelo: `testes/casos_decisao.md` rodado com `python3 testes/rodar_casos.py` (um caso por sessão nova, só leitura) nas variantes plugin e template; o chat é teste manual pelo `LEIA-ME.md` do pacote. A concordância vai para a tabela do arquivo e para o `CHANGELOG.md`; parcial ou divergência vira issue ou correção, nunca aprovação.
5. Autorização do Sarden para distribuir registrada no `CHANGELOG.md` da versão (data, hora, canal) antes do merge; merge e tag `vX.Y.Z` com o OK dele. Aprovação editorial de cada texto é outra coisa: frontmatter `aprovado:`.

Versões homologadas na v0.4.0: Python 3.9 a 3.13 nos projetos (3.13 nas ferramentas do repositório), Copier 9.19.1, Claude Code 2.1.316 no CI e mínimo 2.1.295 nas travas, Git 2.43; CI em Ubuntu e macOS.

Proposta de quem usa o modelo: issue "Proposta para o modelo" (template em `.github/ISSUE_TEMPLATE/`), sem dado de cliente; o Raijin revisa, o Sarden aprova.

## Quem é o Sarden

Matheus Sardenberg, Sarden: estrategista de receita e generalista de growth, CRO da Tegrus (boutique brasileira de Growth e RevOps). O Susano é a sombra de mais de 10 mil horas: projeto, análise, modelo de negócio e o dia a dia que faz uma operação de receita rodar. Perfil em `modelo/00_susano/sobre_o_sarden.md`.

## O que mora onde

| Repositório | Conteúdo | Acesso |
|---|---|---|
| `susano` (este) | a sombra: método, DNA, biblioteca, referências, motor e estrutura, como template (`modelo/`) e como plugin (`plugin/`) | público em github.com/sardenberg182/susano desde 01/11/2026: CC BY 4.0 no conteúdo, MIT no código (decisão do Sarden, 01/11/2026) |
| Oficina (template `persona`) | o Sarden como pessoa (identidade, voz de autor), aplicado só na máquina dele: o projeto ignora `00_pessoal/` e `CLAUDE.local.md`, então nada pessoal entra no Git de um projeto | privado |

Licença: `LICENSE` (código, MIT), `LICENSE-CONTEUDO.md` (conteúdo, CC BY 4.0) e `modelo/00_susano/LICENCA.md` (aviso que vai para cada projeto). Autor: Matheus Sardenberg (Sarden).
