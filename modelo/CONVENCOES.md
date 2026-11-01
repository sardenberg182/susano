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

Arquivos gerenciados (sobrescritos por `copier update`, conferidos pelo `susano-check`): `00_susano/`, `.claude/` (menos `settings.local.json`), `scripts/`, `.github/workflows/`, `CLAUDE.md`, `SUSANO.md`, `CONVENCOES.md`, `CONTRIBUTING.md`. Arquivos do projeto (criados uma vez, o update não toca): `AGENTS.md`, `README.md`, `.github/CODEOWNERS`, pastas `10_` a `90_` e `_templates/`. Gerados pelo projeto (`brain.py`, regenerados no `/salve`): `MAPA.md`, `10_<org>/hot.md`.

## Pasta de uma frente

```
20_<frente>/<slug>/
  README.md      ficha: dono, status, mapa
  contexto.md    quem é (modelo: _templates/contexto_projeto.md)
  estado.md      o que está quente (00_susano/metodo/estado-quente.md)
  decisoes.md    decisões com data e dono; substituídas marcadas, nunca apagadas
  ledger/        AAAA-MM-DD.md, uma linha por fato: ts | fonte | quem | quem_tipo | trecho | ref
  analises/      AAAA-MM-DD_<tema>.md
  reunioes/      AAAA-MM-DD_<tema>.md
```

Crie com `python3 scripts/brain.py novo <slug> --dono <usuário>`.

## Frontmatter

`estado.md`, `contexto.md` e `decisoes.md` de cada frente começam com:

```
---
id: <tipo>-<slug>
tipo: estado | contexto | decisoes
dono: <usuário do GitHub>
atualizado: AAAA-MM-DD
---
```

Arquivos de `10_`, `30_`, `40_` e `50_` levam `id`, `tipo`, `atualizado` e, quando expiram, `revisar_ate: AAAA-MM-DD`. Arquivos do método (`00_susano/`) levam `id` e `tipo` (`identidade`, `metodo`, `pensador`, `instrucao`, `procedimento`, `referencia`).

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

Gate: a pessoa entra só com OK explícito do dono, registrado em `aprovado_por`; sem o campo, `validate` barra. Só papel e relação: telefone ou e-mail nesta pasta é erro de validação, não pergunta. O que ficou combinado com a pessoa fica em `decisoes.md` e `ledger/` da frente; `python3 scripts/brain.py fonte "<nome>"` devolve arquivo e linha.

## Nomes, datas e números

- Slugs em minúsculas, sem acento, com hífen. Datas em ISO (AAAA-MM-DD), fuso America/Sao_Paulo.
- Número sempre com unidade, período, fonte e data. Meta sem registro é [LACUNA].
- Marcadores literais: [DADO], [INFERÊNCIA], [VERIFICAR], [LACUNA], [DADO PENDENTE], [CONTRADIÇÃO], [SENSÍVEL]. [PÚBLICO] marca contato (e-mail, telefone) que o dono decidiu publicar: as guardas não perguntam; nunca libera segredo, cartão ou CPF.
- O caractere travessão é proibido em todo arquivo `.md`: use vírgula, dois-pontos ou "→".

## Validação

- `python3 scripts/brain.py validate`: arquivos obrigatórios, travessão, segredos e dados pessoais (via `.claude/hooks/guardas.py`), frontmatter das frentes, frontmatter e esqueleto do método, links e caminhos citados, frontmatter de `pessoas/`, orçamento de tokens (`nucleo.md` até 2 mil, abertura até 5 mil, estimados).
- `python3 scripts/brain.py mapa`, `hot`, `fonte "<termo>"`, `tokens`: mapa do repositório, estado quente agregado, arquivo e linha de um termo, carga de abertura.
- `python3 scripts/brain.py susano-check`: arquivos gerenciados iguais ao `00_susano/MANIFEST.sha256` da versão instalada.
- `python3 scripts/brain.py audit`: achados mecânicos do brain audit.
- O CI roda `validate` e `susano-check` em todo PR.
