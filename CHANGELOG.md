# Changelog do modelo Susano

## v0.3.0 (em construção na branch `v0.3`; tag só no fim do PR-6)

Origem: plano de mudança v0.3.0 revisado pelo Raijin e decidido pelo Sarden em 01/11/2026 (22:40): tom do núcleo mantido com calibração; fusão dos arquivos do Notion aprovada; casos de decisão rodados à mão antes da tag.

### PR-1 `v0.3-nucleo` (01/11/2026)

- `nucleo.md` e `identidade.md`: P-05 passa a "o dado aponta o gargalo; o gargalo chama o modelo; modelo nunca entra antes do dado"; P-06 define frente (projeto, cliente, conta ou produto) e manda `/nova-frente` em vez de inventar contexto; "Sempre e nunca" ganha: editar só o pedido e sinalizar toda adição, pensar antes de perguntar (uma pergunta com default ou um lote por dimensão), marcador só em documento interno (entregável de cliente, playbook publicado e slide saem sem marcador), "rodando" só no ar sem dependência aberta, referência de mercado como [INFERÊNCIA] com fonte e data e nunca como target; tom mantido como aprovado, com a calibração a quem está na sessão em dois registros (decisão do Sarden, 22:40). Teto do núcleo passa de 2.000 para 2.200 tokens estimados (2.095 medidos). `revisao_pendente: Sarden` nos dois arquivos até ele ler os acréscimos.
- `experimentos.md` como quarto arquivo canônico da frente (`_templates/experimentos.md`; `brain.py novo` cria; `validate` exige frontmatter e data; `salve`, `frente`, `segundo_cerebro.md` e `CONVENCOES.md` acompanham): hipótese com corte → resultado → decisão; "sistematizou" aponta para o playbook que nasceu.
- Convenção única de branch: `salve/AAAA-MM-DD-<tema>`, `estado-quente/AAAA-MM-DD`, `susano-vX.Y.Z` (salve, estado-quente, rotina, CONTRIBUTING, CONVENCOES).
- `brain.py`: domínio `exemplos` (skill `susano-exemplos`, gerada quando a pasta existir); `indice` ganha a seção "Operação"; `validate` barra tipo `resumo` (é `pensador` ou `referencia`), exige ENTRADA, SAÍDA e POR QUE ASSIM em tipo `exemplo` e trata `experimentos.md` como os outros três; `primeira_frase` não corta em "vs.", "ex.", "p.", "aprox."; `linhas_ativos` ignora sub-bullet; descrição da `susano-ativos` muda para "consult when the diagnosis names the gargalo".
- Skill `analise` (template e plugin): marcador só em documento interno; "Atl4s" sai; notas de plataforma novas (export do Meta Ads Manager em XML Spreadsheet, CSV do Google Ads em utf-16, MCC e `customer_id` da conta folha, `search_term_view`, `conversion_action.primary_for_goal`, histórico de propriedade fora do MCP do HubSpot, BP só pelo `.xlsx`, dashboard em imagem por seção). Skill `frente` lê `experimentos.md` e lista cortes vencendo (a substituição de `$slug` por `$ARGUMENTS` proposta no plano não entra: `arguments:` com `$nome` é campo oficial do Claude Code, conferido na documentação em 01/11/2026). Estilo de saída e `CLAUDE.md`: calibração do tom, dado antes do modelo, os quatro arquivos da frente.
- `AGENTS.md` do projeto: "Modo sem shell" para agente de chat (lê a mesma ordem, não roda `brain.py`, termina com a lista do que deveria ser salvo e onde); regra 5 separa valor de contrato de cliente (fora) de mecânica de pricing do método (pode entrar). Regras `seguranca`, `frentes` e `conhecimento` idem; `conhecimento` deixa de dizer que o `ATIVOS.md` é pré-carregado.
- Os dois arquivos do Stories 10x saem de `biblioteca/ladeira/` para `referencias/social_organico/` como `tipo: referencia` (eram `resumo` sem o esqueleto de pensador); `[DADO AUSENTE]` vira `[LACUNA]`; restos de pandoc (`---`) limpos; o domínio `performance` passa a cobrir social orgânico. Proveniência interna (`raio_docN`) sai do `fonte:` dos procedimentos de `metodo/`.
- `onboarding`: pre-commit vira padrão em sessão local; campo `preferencias` aceita convenções de leitura (voz ditada). Testes: 58 casos (5 novos: `experimentos.md` nasce com frontmatter, sem frontmatter barra, exemplo sem POR QUE ASSIM barra, tipo `resumo` barra, volta a passar).


## v0.2.1 (2026-11-01)

- Publicação: repositório público `github.com/sardenberg182/susano` criado pelo Sarden (ordem de 01/11/2026, 19:00; só este repositório, nada da Oficina nem do tegrus-brain). README, catálogo e manifesto do plugin com o endereço real; instalação `claude plugin marketplace add sardenberg182/susano` e `copier copy gh:sardenberg182/susano`.
- `.github/CODEOWNERS` com o Sarden. Proteção da `main` (PR obrigatório, sem force push nem exclusão, vale para admins) configurada pela API; o Raijin propõe por PR e o Sarden aprova. O workflow de CI do repositório (`testar_modelo.sh` e `testar_plugin.sh` em todo PR) está pronto, mas entra num PR próprio: o token do gh que publicou não tem o escopo `workflow`, que o GitHub exige para criar arquivos em `.github/workflows/` [VERIFICAR: `gh auth refresh -s workflow` no Mac do Sarden].

## v0.2.0 (2026-11-01)

- Núcleo da sombra: `00_susano/nucleo.md` (cerca de 1,9 mil tokens estimados) extraído da `identidade.md` aprovada; o `CLAUDE.md` do projeto importa o núcleo e o `AGENTS.md`, não mais a identidade inteira nem o `ATIVOS.md`. `brain.py tokens` estima a carga de abertura; `validate` barra núcleo acima de 2 mil tokens e abertura acima de 8 mil (estimativa de 2,7 caracteres por token, base no glossário da Anthropic de 01/11/2026; medir no `/context`).
- Skills por domínio geradas de `00_susano/` por `brain.py skills` (fonte única, idempotente): `susano-ativos` (o antigo `ATIVOS.md` como skill-índice), `susano-metodo`, `susano-biblioteca`, `susano-performance`, `susano-analytics`, `susano-gtm`, `susano-plataformas`, `susano-rituais`. Cada uma lista os arquivos com tese e "para quê"; o Susano abre só o arquivo que a tarefa pede.
- Degrau 1 do segundo cérebro no template: `brain.py mapa` gera `MAPA.md` (frentes, dono, data e situação do estado, organização, projetos, playbooks, referência); `brain.py hot` gera `10_<org>/hot.md` (estado quente agregado, janela de 14 dias, fonte por frente); `10_<org>/pessoas/` para stakeholders com gate do dono: `brain.py pessoa <slug> ... --aprovado-por <dono>` cria o arquivo (recusa sem o dono e recusa contato nos argumentos), `aprovado_por` obrigatório no `validate`, contato na pasta é erro; modelo em `_templates/pessoa.md`, regra em `.claude/rules/pessoas.md`. Em projeto atualizado de versão anterior, o `pessoa` cria a pasta e o README (o `copier update` não leva arquivos novos para as pastas do projeto); `brain.py fonte "<termo>"` devolve arquivo e linha (resposta com fonte). `/salve` regenera mapa e hot; `/cerebro` parte do `hot.md`; `/frente` e `/cerebro` usam `fonte`.
- `AGENTS.md` do projeto ganha a seção "Como usar o Susano (qualquer agente)": a ordem de leitura para Codex, Cursor, Gemini CLI e Copilot, que não têm o mecanismo de skills.
- Plugin do Claude Code gerado da mesma fonte por `ferramentas/construir_plugin.py`: `plugin/` (manifesto, hook de abertura que injeta o núcleo, 9 skills, subagente `pesquisador`, estilo de saída, `00_susano/`) e catálogo `.claude-plugin/marketplace.json` na raiz. Instalação: `/plugin marketplace add <org>/susano` e `/plugin install susano@susano`.
- Descrições de skills e subagentes encurtadas; estilo de saída enxuto (o tom vive no núcleo). Testes: 53 casos em `testar_camada.py` (17 novos: núcleo, tokens, mapa, hot, fonte, pessoas e o comando `pessoa`, skills), `testar_modelo.sh` e `testar_plugin.sh`; aceite de atualização v0.1.12 → v0.2.0 sem `.rej` e com edição local preservada (01/11/2026).

## v0.1.12 (2026-11-01)

- Aprovações do Sarden registradas no kit (01/11/2026): licença (16:45), `identidade.md` v0.1.6 (16:51), `sobre_o_sarden.md` com o texto dele (16:43) e os 8 DNAs de `dna/metodo/` (16:54, "Revisado pode seguir"). Cada arquivo aprovado leva a linha `aprovado:` no frontmatter; o texto não muda. `pendentes.md` passa a abrir com o que está aprovado e marca [VERIFICAR] nos thresholds da rotina do gestor, que ele ainda não releu.

## v0.1.11 (2026-11-01)

- Licença definida pelo Sarden (01/11/2026, 16:45): CC BY 4.0 no conteúdo e MIT no código. Sai o [VERIFICAR] da `LICENCA.md`; README deixa de dizer "fechado até definir a licença".

## v0.1.10 (2026-11-01)

- `sobre_o_sarden.md` com o texto final do Sarden (01/11/2026, 16:43): abertura em três linhas, método em duas setas, mantra "1% todos os dias"; contato mantido (LinkedIn e X). README acompanha.

## v0.1.9 (2026-11-01)

- `sobre_o_sarden.md` reescrito com o texto do Sarden (01/11/2026, 16:30): sai a trajetória, saem os cases, sai a localização e a menção a advisory; a seção do método passa a contar de onde ele veio (mais de 10 mil horas de trabalho, projetos, análises, modelos de negócio, melhoria contínua) na voz dele. README acompanha.

## v0.1.8 (2026-11-01)

- Contato do autor em `sobre_o_sarden.md`: LinkedIn e X (@mbasardenberg_); Instagram e e-mail saem (decisão do Sarden, 01/11/2026, 12:25). O marcador [PÚBLICO] continua disponível nas guardas.

## v0.1.7 (2026-11-01)

- `sobre_o_sarden.md` ganha Instagram e e-mail profissional, por decisão do Sarden (01/11/2026, 12:17).
- Marcador [PÚBLICO] nas guardas: linha com contato (e-mail, telefone) que o dono decidiu publicar não dispara pergunta; nunca libera segredo, cartão ou CPF. Documentado em `CONVENCOES.md`, com 2 casos novos em `testar_camada.py`.
- Revisão de segurança do motor: `actions/checkout` fixado por SHA (v7.0.1) em vez de tag flutuante e token do workflow só leitura (`permissions: contents: read`); `CONTRIBUTING.md` ganha a configuração de proteção da `main` no GitHub, sem a qual "nunca commit na main" é instrução e não trava.

## v0.1.6 (2026-11-01)

- Nomes ligados à operação do Sarden saem do modelo (ordem do Sarden, 01/11/2026): um case de cooperativa financeira divulgado pelo fornecedor sai das listas da referência de CleverTap; o crédito de autor da biblioteca `rodrigo_miranda/` perde o nome da empresa. O nome civil fica só nas linhas de copyright, por ordem dele.
- `00_susano/sobre_o_sarden.md`: perfil público do autor (cargo, trajetória, cases com material de apoio, formação, origem do método, LinkedIn), só com dado de carreira já público; a identidade aponta para ele e o README resume. [VERIFICAR] texto a fechar pelo Sarden antes da publicação.

## v0.1.5 (2026-11-01)

- Varredura pós-migração do Notion: o link da página filha no sistema operacional de demanda apontava para uma URL interna do Notion; agora aponta para `panorama_2026_guia_estrategico.md`. Nenhum outro rastro (nome de cliente ou empresa, e-mail, telefone, URL interna, ID real, segredo) no modelo.

## v0.1.4 (2026-11-01)

- Tom de resposta do Susano é o tom do Sarden (decisão do Sarden, 01/11/2026): seção "Tom de resposta: o tom do Sarden" na `identidade.md` e no estilo de saída, extraída do jeito como ele fala no trabalho (parceiro de trincheira, ilusão quebrada na abertura, etapas sem pular, ironia contra o conceito e nunca contra a pessoa, técnico em inglês com coloquial). A voz de autor (post, LinkedIn, e-mail, mensagem) segue fora do modelo.
- Base de performance: 5 direcionais do Notion do Sarden em `00_susano/referencias/performance/` (fundamentos de anúncios, rotina do gestor em 4 blocos, checklist diário, sistema operacional de geração de demanda 2026, guia estratégico do Panorama 2026), convertidos com `migrar_notion.py` e notas de migração em cada arquivo. `pendentes.md` fecha a lacuna.
- Licença: copyright em nome de Matheus Sardenberg (Sarden) em todo lugar (decisão do Sarden, 01/11/2026). Default (a), a confirmar antes da publicação: MIT no código (`LICENSE`) e CC BY 4.0 no conteúdo (`LICENSE-CONTEUDO.md`); `00_susano/LICENCA.md` leva o aviso para cada projeto, com [VERIFICAR].
- Contradições e números sem fonte ficam marcados com as duas fontes (decisão do Sarden, 01/11/2026); nada é resolvido no silêncio.

## v0.1.3 (2026-11-01)

- Projeto carrega estrutura de conhecimento e contexto, nunca dado específico do Sarden (ordem do Sarden, 01/11/2026): varredura do modelo inteiro (URLs, IDs, e-mails, telefones, nomes de clientes e empresas, valores, anedotas). Saíram os rastros: menção a projeto interno no README, histórico de migração com nomes de arquivos internos (`docs/origem.md`, agora fora deste repositório), nome civil na `LICENCA.md` que vai para todo projeto, destaque de um único caso na referência de CleverTap (fica a regra geral para números divulgados pelo fornecedor), fonte errada no guia de web analytics e nomes internos nas entradas antigas deste CHANGELOG.
- Tom de resposta explícito na identidade e no estilo de saída: é como o Susano fala com quem está na sessão; a voz de autor do Sarden não entra no modelo (decisão D-1, 01/11/2026).
- `.gitignore` do projeto ignora `00_pessoal/` e `.copier-answers.persona.yml`, além do `CLAUDE.local.md`: a persona da Oficina, quando aplicada, fica só na máquina de quem aplicou.
- Fuso dos números: o do projeto, com America/Sao_Paulo como padrão.
- `.gitignore` sai de `_skip_if_exists`: passa a acompanhar o modelo no `copier update` (testado em 01/11/2026: um arquivo em `_skip_if_exists` não recebe a mudança do modelo no update, mesmo sem edição local). Linhas que o projeto acrescentar são preservadas pelo diff do Copier.

## v0.1.2 (2026-11-01)

- O Susano é a sombra do Sarden: `00_susano/identidade.md` reescrita a partir disso (ordem do Sarden, 01/11/2026).
- Nome "Sarden" em todo DNA, sombra e persona.
- O conteúdo é de autoria do Sarden (decisão de 01/11/2026): saem as travas de revisão jurídica da biblioteca e da licença; a licença de abertura fica a definir.

## v0.1.1 (2026-11-01)

- Os 10 arquivos que faltavam da versão 3.8 do Susano: 6 pensadores na biblioteca (DotCom Secrets e Expert Secrets do Brunson, Fórmula de Lançamento, G4 Traction, Bruno Nardon, Hacking Growth) e 4 DNAs (GTM e RevOps, M&A e valuation, post de hackizinhos, crenças de liderança), com as seções de voz na Oficina.
- A versão curta do artigo 4 do Balfour nunca existiu: as citações apontam para `00_susano/biblioteca/balfour/04_model_market_fit.md`.
- `pendentes.md` sem arquivos faltando; `ATIVOS.md`, `INDICE.md` e `MANIFEST.sha256` regenerados.

## v0.1.0 (2026-10-31)

Primeira versão, montada pelo Raijin a partir da camada v0.1 e dos 57 arquivos do Susano 3.x.

- Modelo Copier (`_subdirectory: modelo`): arquivos gerenciados estáticos com MANIFEST; arquivos do projeto criados uma vez (`_skip_if_exists`).
- Método em `00_susano/`: identidade (system prompt v2 generalizado), DNA do Sarden (método; a voz foi para a Oficina), biblioteca de 21 pensadores e resumos (série Balfour consolidada de 9 arquivos recebidos em 6), instruções GP/BP e onboarding, 6 procedimentos de segundo cérebro, 21 referências (HubSpot, CleverTap, WhatsApp, analytics, tracking, go-to-market, benchmarks).
- `ATIVOS.md` (importado no CLAUDE.md) e `INDICE.md` gerados por `brain.py indice`.
- Motor: hooks, regras, skills (`/frente` e `/nova-frente` no lugar de `/cliente` e `/novo-cliente`), subagentes, estilo de saída, rotina semanal.
- `brain.py`: validate, susano-check, audit, novo, indice, manifesto.
- Pendências em `modelo/00_susano/pendentes.md`.
