# Convenções do repositório (gerenciado pelo modelo Susano)

Este arquivo muda só por versão do modelo. Regras específicas da organização vão em `AGENTS.md`.

## Mapa de pastas

| Pasta | O que mora ali | Quem muda |
|---|---|---|
| `00_susano/` | o método Sarden: identidade, DNA, biblioteca, instruções, procedimentos do segundo cérebro, referências | só versão do modelo |
| `10_<org>/` | a organização: quem é, time (`time/`), stakeholders (`pessoas/`, com gate), decisões da organização (`decisoes.md`), estado quente agregado (`hot.md`, gerado), rituais, auditorias | o projeto |
| `20_<frente>/<slug>/` | cada frente de trabalho (cliente, conta ou produto) | o projeto, com o dono da frente |
| `30_projetos/` | iniciativas com começo e fim | o projeto |
| `40_playbooks/` | processos próprios da organização (não o método) | o projeto, por PR |
| `50_referencia/` | referências usadas só neste projeto | o projeto |
| `90_arquivo/` | o que foi substituído, com ponteiro de onde estava | o projeto |
| `_templates/` | modelos de arquivo para copiar | o projeto |
| `MAPA.md` | mapa do repositório gerado por `brain.py mapa` (frentes, dono, data, organização, projetos, playbooks, referência) | gerado, nunca à mão |

Arquivos gerenciados (sobrescritos por `copier update`, conferidos pelo `susano-check`): `00_susano/`, `.claude/` (menos `settings.local.json`), `scripts/`, `.github/workflows/`, `CLAUDE.md`, `SUSANO.md`, `CONVENCOES.md`, `CONTRIBUTING.md`. Arquivos do projeto (criados uma vez, o update não toca): `AGENTS.md`, `README.md`, `.github/CODEOWNERS`, pastas `10_` a `90_` e `_templates/`. O `AGENTS.md` tem três partes: cabeçalho com os nomes do projeto, o bloco gerenciado entre `<!-- susano:inicio` e `<!-- susano:fim -->` (cópia de `scripts/agents_gerenciado.md`, conferida pelo `susano-check`, reescrita pelo `brain.py migrar`) e as Regras próprias, que são do dono e prevalecem sobre os padrões do bloco, nunca para liberar credencial, CPF, cartão ou contato pessoal. Gerados pelo projeto (`brain.py`, regenerados no `/salve`): `MAPA.md`, `10_<org>/hot.md`. Exceções da inspeção de privacidade, quando houver: `PRIVACIDADE_EXCECOES.md` na raiz (do projeto).

## Pasta de uma frente

```
20_<frente>/<slug>/
  README.md      ficha: dono, status, mapa
  contexto.md    quem é (modelo: _templates/contexto_projeto.md)
  estado.md      o que está quente (00_susano/metodo/estado-quente.md)
  decisoes.md    decisões com data e dono; substituídas marcadas, nunca apagadas
  experimentos.md hipótese com corte → resultado → decisão (modelo: _templates/experimentos.md)
  ledger/        AAAA-MM-DD.md, uma linha por fato: ts | fonte | quem | quem_tipo | trecho | ref
  analises/      AAAA-MM-DD_<tema>.md
  reunioes/      AAAA-MM-DD_<tema>.md
```

Crie com `python3 scripts/brain.py novo <slug> --dono <usuário>`. Os quatro arquivos (`contexto.md`, `estado.md`, `decisoes.md`, `experimentos.md`) são obrigatórios: o `validate` barra a falta e o `brain.py migrar` cria o que falta a partir de `_templates/`, sem tocar no que está preenchido.

## Frontmatter

`estado.md`, `contexto.md`, `decisoes.md` e `experimentos.md` de cada frente começam com:

```
---
id: <tipo>-<slug>
tipo: estado | contexto | decisoes | experimentos
dono: <usuário do GitHub>
atualizado: AAAA-MM-DD
---
```

Arquivos de `10_`, `30_`, `40_` e `50_` levam `id`, `tipo`, `atualizado` e, quando expiram, `revisar_ate: AAAA-MM-DD`. Referência volátil (preço, limite, recurso ou benchmark de plataforma) separa a edição da conferência: `atualizado` é a data da última edição, `verificado_em: AAAA-MM-DD` é a data em que a fonte foi conferida, `revisar_ate` é o prazo da próxima conferência e a fonte vai com data no corpo; quem confere é o dono do arquivo. O `brain.py audit` lista referência sem `verificado_em` e revisão vencida. Arquivos do método (`00_susano/`) levam `id` e `tipo` (`identidade`, `operacao` para `situacoes.md` e `calibracao.md`, `metodo`, `pensador`, `instrucao`, `procedimento`, `referencia`, `exemplo`). Um `exemplo` tem as seções ENTRADA, SAÍDA e POR QUE ASSIM. O tipo `resumo` não existe mais: é `pensador` (com o esqueleto) ou `referencia`.

## Esqueleto dos pensadores (`tipo: pensador`)

Obrigatórias: TESE EM UMA LINHA, MODELOS ATIVOS, PRINCÍPIOS OPERACIONAIS, ALERTAS CRÍTICOS, REFERÊNCIA RÁPIDA. Recomendadas: FRAMEWORKS PASSIVOS, CONEXÕES. Modelos ativos: o Susano aplica sempre que o contexto pede (resumidos em `00_susano/ATIVOS.md`). Frameworks passivos: só quando a situação chama.

## Pessoas (`10_<org>/pessoas/`)

Um arquivo por stakeholder externo (cliente, parceiro, fornecedor), criado com `python3 scripts/brain.py pessoa <slug> --nome ... --papel ... --relacao ... --aprovado-por <dono>` (modelo em `_templates/pessoa.md`):

```
---
id: pessoa-<slug-do-nome>
tipo: pessoa
papel: cargo ou função
relacao: frente ou projeto em que atua e desde quando
frentes: slug-1, slug-2
contato_em: sistema e ID onde o contato vive (nunca o contato)
aprovado_por: <usuário do GitHub do dono que autorizou>
atualizado: AAAA-MM-DD
---
```

Gate: a pessoa entra só com OK explícito do dono, registrado em `aprovado_por`; sem o campo, `validate` barra. Só papel e relação: telefone ou e-mail nesta pasta é erro de validação, não pergunta. O que ficou combinado com a pessoa fica em `decisoes.md` e `ledger/` da frente; `python3 scripts/brain.py fonte "<nome>" --frente <slug>` devolve arquivo e linha.

## Nomes, datas e números

- Slugs em minúsculas, sem acento, com hífen. Datas em ISO (AAAA-MM-DD), fuso America/Sao_Paulo.
- Número sempre com unidade, período, fonte e data. Meta sem registro é [LACUNA].
- Marcadores literais: [DADO], [INFERÊNCIA], [VERIFICAR], [LACUNA], [DADO PENDENTE], [CONTRADIÇÃO], [SENSÍVEL], [VENDOR] (caso ou número divulgado pelo fornecedor da plataforma). Marcador é de documento interno e rascunho; entregável de cliente, playbook publicado e slide saem sem marcador. [PÚBLICO] marca contato (e-mail, telefone) que o dono decidiu publicar: as guardas não perguntam; nunca libera segredo, cartão ou CPF.
- O caractere travessão é proibido em todo arquivo `.md`: use vírgula, dois-pontos ou "→".

## Validação

- `python3 scripts/brain.py validate`: privacidade de todo arquivo (abaixo), arquivos obrigatórios (inclusive as quatro de cada frente), travessão nos `.md`, frontmatter das frentes, frontmatter e esqueleto do método, links e caminhos citados, frontmatter de `pessoas/`, orçamento de tokens (`nucleo.md` até 2.200; abertura até 8 mil, com o pacote gerenciado até 6.500 e 1.500 reservados ao projeto, estimados; `brain.py tokens` detalha por parte).
- `python3 scripts/brain.py varrer`: só a privacidade. Todo arquivo do repositório, qualquer extensão (CSV, notebook, `.env` adicionado à força, arquivo sem extensão), inclusive `90_arquivo/`; ZIP, `.xlsx` e `.docx` abertos por dentro; o que não dá para ler (imagem, PDF, cifrado) vira aviso visível. Segredo, cartão e CPF são erro; telefone e e-mail fora de `pessoas/` são aviso no projeto. `--staged` lê o índice do Git (o que vai para o commit); `--perfil publico` também barra contato e formato não inspecionado (repositório e pacote públicos). Exceção só de contato ou binário, por arquivo exato e com motivo, em `PRIVACIDADE_EXCECOES.md` (tabela `| regra | caminho | motivo |`); segredo, cartão e CPF nunca têm exceção.
- `python3 scripts/brain.py migrar`: aplica o contrato da versão instalada ao que é do projeto (bloco gerenciado do `AGENTS.md`, arquivos obrigatórios das frentes). Roda depois de todo `copier update`; idempotente.
- `python3 scripts/brain.py mapa`, `hot`, `fonte "<termo>" --frente <slug>`, `tokens`: mapa do repositório, estado quente agregado, arquivo e linha de um termo na frente em foco (`--todas` só em comparação pedida, cada linha com a origem; sem flag, nenhuma frente entra), carga de abertura por parte.
- `python3 scripts/brain.py susano-check`: arquivos gerenciados iguais ao `00_susano/MANIFEST.sha256` da versão instalada e o bloco gerenciado do `AGENTS.md` igual a `scripts/agents_gerenciado.md`.
- `python3 scripts/brain.py audit`: achados mecânicos do brain audit (estado frio, projeto parado, revisão vencida, referência sem `verificado_em`, revisão editorial pendente do método).
- O CI roda `validate` e `susano-check` em todo PR. O pre-commit (`bash .claude/hooks/instalar_precommit.sh`, oferecido no `/onboarding`) inspeciona o índice com `varrer --staged` e roda o `validate` antes de cada commit; hook anterior é preservado e roda antes.
- Branches: `salve/AAAA-MM-DD-<tema>` (trabalho de sessão), `estado-quente/AAAA-MM-DD` (refresh semanal), `susano-vX.Y.Z` (versão do modelo).
- Antes de cada versão do modelo, o mantenedor roda `testes/casos_decisao.md` (repositório `susano`) no agente e registra a concordância; é a medida de "executa como o Susano".

## Proteções: o que barra, onde e quando

| Camada | Barra | Não cobre |
|---|---|---|
| Guardas do Claude Code (`.claude/hooks/`, Claude Code 2.1.295 ou mais novo, Python 3.9 ou mais novo) | escrita por Write, Edit, MultiEdit e NotebookEdit com segredo, cartão, CPF ou travessão (pergunta antes de contato); mensagem com segredo, cartão ou CPF; falha da própria guarda, Python ausente ou tempo estourado também barram | escrita por Bash ou por ferramenta fora do Claude Code; outros agentes (Codex, Cursor, Gemini CLI, Copilot), que não leem estes hooks |
| Pre-commit local | o que vai para o commit (índice do Git), venha de qualquer ferramenta | `git commit --no-verify` e máquina sem o hook instalado |
| CI (`.github/workflows/brain.yml`) | todo PR: `validate` (privacidade de todo arquivo) e `susano-check` | só barra o merge com o check exigido na proteção da `main` (`CONTRIBUTING.md`); nada fora do Git (`bruto/`, conectores) |

A trava que vale para todo mundo é o CI com o check exigido. As guardas e o pre-commit pegam antes, na máquina de quem escreve; nenhuma das três substitui o cuidado de não trazer dado pessoal para o repositório.
