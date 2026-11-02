# Changelog do modelo Susano

## v0.3.0 (fechada em 01/11/2026 na branch `v0.3`; tag depois do merge em `main` e da rodada dos casos de decisão pelo Sarden)

Origem: plano de mudança v0.3.0 revisado pelo Raijin e decidido pelo Sarden em 01/11/2026 (22:40): tom do núcleo mantido com calibração; fusão dos arquivos do Notion aprovada; casos de decisão rodados à mão antes da tag.

### PR-6 `v0.3-limpeza` (01/11/2026)

- Proveniência: `origem:` da biblioteca passa a citar a obra e o autor (resumo do Sarden), sem nome de arquivo interno; `origem:` dos DNAs em áudio e vídeo deixa de apontar para o próprio arquivo; referências de analytics, CleverTap e WhatsApp descrevem a fonte, não o arquivo; "nome antigo" sai de gp_bp, onboarding_frente e Fernando Miranda; o nome da pasta interna de origem sai de `pendentes.md` e de `balfour/04`.
- P2 residual: exemplo de setor em `balfour/05` neutralizado; UTM de exemplo neutra no guia profundo; CleverTap sem ponteiros para arquivos locais do autor (inventário de fontes descritivo, anexos reescritos) e nota de migração sem setor; nomes internos que restavam no CHANGELOG (conector de dados e repositório privado) neutralizados. Varredura de 40 nomes de cliente, pessoa e ferramenta interna em `modelo/`, `plugin/`, `90_arquivo/`, `testes/`, README e CHANGELOG: zero fora de `sobre_o_sarden.md` e das licenças.
- `pendentes.md` reescrito: título sem versão, aprovações datadas, seção "Em revisão" apontando para os `revisao_pendente` por PR, arquivos de origem sem o nome da pasta interna, revisões abertas com os [VERIFICAR] da v0.3.0 e a rodada dos casos de decisão, seção de propostas por issue.
- README aponta para a tag v0.3.0 no `copier copy` e instala o Copier com `pipx` ou `uv tool` (o `pip install` falha em Python gerenciado, PEP 668; achado ao conferir o ambiente do Sarden em 02/11/2026). Regeneração final (índice, skills, manifesto, plugin) e testes. A tag v0.3.0 e o merge de `v0.3` em `main` acontecem só com o OK do Sarden, depois de ele rodar `testes/casos_decisao.md` e registrar a concordância na tabela do arquivo e aqui.

### PR-5 `v0.3-referencias` (01/11/2026)

- Referências novas, só regra e sem cliente: `referencias/performance/licoes_de_conta.md` (Meta, Google e transversal: cada lição com "reconhece-se por" e "o que fazer"), `referencias/performance/regua_criativos_leadgen.md` (os 5 componentes com régua default do método, hook por porcentagem assistida, nota de calibração), `referencias/plataformas/crm/padrao_implementacao.md` (pipes Lead e Negócio, cadência, recuperação de perdidos, onde cada etapa se qualifica, 7 propriedades de atribuição com herança e prefixo `[ORG]`, metas com regra de proteção, lições de contagem, anexo HubSpot), `referencias/go-to-market/auditoria_bp.md` (fórmulas certas de unit economics e BP, dez erros clássicos, como auditar na camada de fórmula com openpyxl, exemplo fictício).
- Go-to-market: os nove stubs viram `modelos_quantitativos.md` (sizing, segmentação, scoring, pricing, forecasting, churn, win/loss, curvas e simulação, atribuição e MMM, experimentação com fórmula de amostra, duas consultas GA4 para BigQuery validadas em sintaxe com sqlglot e rodadas em DuckDB sobre dados sintéticos, ferramentas) e `benchmarks_com_fonte.md` (só linha com publisher, ano e link; KeyBanc/Sapphire, Bridge Group, Bessemer, ABComm, ABES/IDC conferidos por busca em 01/11/2026; fontes de LP do playbook; as linhas `web:NN` sem fonte saíram). Originais em `90_arquivo/go-to-market_v0.2/`.
- `rotina_gestor_performance.md`: nota de que todo threshold é default do método; papéis genéricos (gestor da frente, liderança de growth; a organização mapeia em `10_<org>/time/`); CRM genérico com anexo HubSpot; dicionário citado; TrueView, Discovery, SPC e InMail marcados [VERIFICAR] com data. `checklist_diario_gestor.md` vira o índice cronometrado do Bloco 1 da rotina (fusão aprovada pelo Sarden).
- Panorama 2026 como fonte única: `benchmarks/panorama_2026.md` reescrito em markdown acentuado, sem tags XML nem protocolo de Project, com número de página por tabela, marcadores canônicos, os scorecards por canal, a tabela cheia de horário, a síntese por objetivo, a tabela de inconsistências e os cortes B2B/B2C e WhatsApp (nenhum número do original perdido: conferência automática). O guia estratégico perde as 14 tabelas e aponta para a seção de P; o sistema operacional de demanda usa os marcadores canônicos (com [VENDOR] no lugar de [CASO DO FORNECEDOR]), declara o capítulo 12 como camada de liderança com referência à rotina do gestor, corrige a FAQ escapada, remove a página interna da tabela de fontes e cita o benchmark por seção.
- Biblioteca: frases quebradas pela remoção do travessão reescritas (Sean Ellis, Elad Gil, Ladeira, Nardon/G4 Kiso), en dash normalizado (Sean Ellis, Hormozi), auto-referências removidas (Balfour 01 e 03), modelos duplicados de Balfour fundidos (roadmap por canal; Danger Zone), CONEXÕES em Rodrigo Miranda, 4 Fits com quatro itens, contradições marcadas com os dois caminhos (Stack 20% vs 40%, cinco vs seis camadas, refund 5% vs 10%) e nota sobre thresholds de M&A; a dupla "CR 5% vs 10%" do plano não foi encontrada como contradição (os dois livros usam 5 a 10% como baseline do Stack). Fernando Miranda ganha tese, frameworks passivos e conexões, em pt-BR.
- HubSpot (PR-5b): capítulo Brasil fundido no `dossie_mestre.md` (§18.3 e §18.6 com rate limits, webhooks e custom code com fonte e data; §23.1 com as cinco contradições tratadas; §24.5 com as 46 referências com URL; §25 com o capítulo e o anexo da taxonomia de 182 capacidades como [INFERÊNCIA]; perfil "serviços financeiros regulados"; coluna Fontes vazia removida; [DADO AUSENTE] vira [LACUNA]). `brasil_2026-05.md` em `90_arquivo/plataformas_hubspot_v0.2/`.
- Analytics (PR-5c), cada correção com fonte oficial e "verificado em 01/11/2026" ou [VERIFICAR]: consent mode com o stub do gtag e o trigger Consent Initialization, chaves inventadas de dataLayer substituídas pelos comandos `gtag('consent')`, UET lê só `ad_storage` (obrigatório no EEA desde 05/05/2025), Chrome mantém cookies de terceiros (22/04/2025), perdas percentuais sem fonte viraram [LACUNA]; GA4 com os limites oficiais de dimensões custom (50/25/10 e 50 métricas; 360: 125/100/25/125) e DebugView sem parâmetro de URL; GTM com Google tag e Measurement ID, triggers Consent Initialization e Initialization, template oficial do Meta, Tag Assistant atual; guia profundo com nomenclatura única, os quatro estados de consentimento, janelas de atribuição por plataforma, cinco fontes erradas removidas (e 52 marcas no texto) e a seção 17.2 fechada; snippets sem `page_view` duplicado, com `ecommerce: null`, YouTube com `enablejsapi=1` e nomes do Enhanced Measurement, Meta Purchase com aspas, `eventID` e checagem de `fbq`, Typeform e Calendly numa versão só; server-side com o Google tag gateway descrito pelo que é (CDN, sem Workers; Cloudflare 08/05/2025), casos de CAPI separados do sGTM e preços com data; WhatsApp com o cronograma reescrito no passado pela documentação da Meta (BSUID em abril, usernames de empresa em 29/06, envio para BSUID em julho de 2026), formato e troca de BSUID, limite de 100 mil [VERIFICAR]. Os sete arquivos ganham a convenção "verificado em", e `atualizado` deixa de valer como verificação.
- Skills: descrições de metodo (DNAs novos), performance (lições de conta, régua), gtm (3 arquivos) e plataformas (padrão de CRM, dossiê com Brasil) atualizadas; carga de abertura do projeto gerado em 7.952 tokens estimados (teto 8.000).

### PR-4 `v0.3-exemplos` (01/11/2026)

- `00_susano/situacoes.md`: roteador para qualquer agente, 17 situações (o que a pessoa diz → modo → o que abrir → saída esperada → armadilha) e as regras do roteador; primeira leitura depois do núcleo (`nucleo.md`, `identidade.md`, `CLAUDE.md` e `AGENTS.md` passam a mandar lê-lo). `00_susano/calibracao.md`: P-04 aplicado em doze pedidos típicos (age, uma pergunta com default ou lote), três discordâncias bem ditas (P-03) e o que não se diz (P-02 e P-06).
- `00_susano/exemplos/`: sete pares entrada → saída com empresas e números inventados, um por modo recorrente (leitura de WBR, diagnóstico pela planilha de taxas, tabela de PA, análise de reunião, resumo executivo semanal, mensagem para líderes, estrutura de proposta), cada um com POR QUE ASSIM ligando as escolhas a `caminho#seção`; `README.md` da pasta com a regra de uso (nunca copiar número de exemplo para frente real). A skill `susano-exemplos` passa a ser gerada (9 skills por domínio no template, 10 no plugin). Núcleo em 2.185 tokens estimados (teto 2.200).
- `testes/casos_decisao.md` na raiz do repositório: 26 casos (situação, entrada fictícia, decisão esperada, regra que sustenta, armadilha) e a tabela de registro de execução; é a medida de "executa como o Susano", rodada à mão pelo Sarden antes da tag (decisão de 01/11/2026). `.github/ISSUE_TEMPLATE/proposta_para_o_modelo.md`: campos para proposta de quem usa o modelo, sem dado de cliente.
- Caminho 3 de distribuição: `ferramentas/gerar_pacote_chat.py` gera `dist/chat/SYSTEM_PROMPT.md` (núcleo + identidade + situações + nota de modo sem shell) e `susano_conhecimento.zip` (`00_susano/` sem manifesto) para Project do claude.ai, GPT ou Gem; README ganha o caminho, a tabela "o que carrega quando" e a linha do Raijin (propõe por PR, o Sarden aprova). `.gitignore` para `dist/` e bytecode (um `.pyc` que estava versionado sai).
- `CONVENCOES.md`: tipo `operacao`, teto de tokens atualizado (2.200 e 8 mil), casos de decisão antes de cada versão. Testes: 62 casos no aceite desta PR (5 novos: nove skills, `landing_pages.md` só na performance, Operação no índice, caminhos de `situacoes.md` e `calibracao.md` existem). Todos os arquivos novos e alterados do método levam `revisao_pendente: Sarden`.

### PR-3 `v0.3-instrucoes` (01/11/2026)

- Quatro instruções novas em `00_susano/instrucoes/`, destiladas das fontes que o Sarden anexou em 01/11/2026 (aprendizados consolidados da operação, mar a out/2026, e o playbook do agente construtor de LP v3.0) só em regra, sem cliente, nome ou número de cliente: `wbr.md` (o que é, régua de status pelo KPI principal com default 90/70, estrutura em dois níveis, glossário, tipos de desvio, lente de sete perguntas e três filtros, PA completo, diarizar, pré e pós-agenda, agenda de e-commerce, exemplo fictício), `brief_e_proposta.md` (as quatro camadas da demanda, cruzar com o anexo, migração é três coisas, problema → processo → prova), `operacao_e_time.md` (status que se confia, revisão com folga, pendência completa, passagem de bastão), `landing_pages.md` (a lente dos cinco pontos, a ficha dos 17 campos, o protocolo de dispositivo, os erros vistos em projeto, o QA de sete blocos, as regras do agente construtor e como o Susano ajuda).
- `referencias/landing_pages/playbook_construtor_html.md`: o playbook v3.0 inteiro (fases 0 a 11, anexos A a G, esqueletos de `index.html` e `obrigado.html`, blueprints por tipo, templates de `docs/`, definição de pronto, Impeccable 4.6 com crédito Apache-2.0) como `tipo: referencia`, com o corte P2 feito por script local do Raijin (não versionado: ele carrega os próprios termos que remove): cabeçalho sem nome de agência nem link interno, legenda `[I]` anonimizada, caso de cliente sem nome e sem valores, referência a arquivo interno removida, nomes antigos do knowledge remapeados para os caminhos do modelo.
- `metodo/ingerir.md`: seção "Leitura de reunião e transcrição": resumo executivo → insights → action items com dono e prazo → não dito; agenda longa foca tom, decisões-chave e alinhamentos; fatos para o ledger, mudança de estado via `/salve`.
- `gp_bp.md` passa a `carrega_em: sob demanda` (era toda conversa), vocabulário de frente (nota no topo), marcadores canônicos ([DADO PENDENTE] literal, sem sufixo; [LACUNA] no lugar de [DADO AUSENTE]), meta só do registro da frente e o contexto lido dos quatro arquivos de `20_<frente>/<slug>/` (era `contexto_[nome].md`); `onboarding_projeto.md` vira `onboarding_frente.md` (sob demanda; chamado por `/nova-frente`; a pasta nasce por `brain.py novo`; entrega nos quatro arquivos da frente; stakeholders só por `brain.py pessoa` com o OK do dono).
- `brain.py skills`: a lista de domínios aceita arquivo além de pasta e exclusão com prefixo `-`; `susano-performance` passa a cobrir landing pages (lente e playbook) e `susano-rituais` descreve WBR, brief e proposta, operação e time, GP/BP e onboarding. Todos os arquivos novos e alterados levam `revisao_pendente: Sarden`.

### PR-2 `v0.3-dna` (01/11/2026)

- Cinco DNAs novos em `00_susano/dna/metodo/`, destilados dos aprendizados consolidados da operação do Sarden (mar a out/2026) só em regra, com exemplos fictícios e sem nome, número ou cliente real: `principios_mestre.md` (os 12 princípios e a ordem em que entram num diagnóstico), `anti_padroes.md` (20, cada um com como reconhecer, o que fazer e exemplo inventado), `diagnostico_de_funil.md` (ordem do método, as 7 checagens, hipótese com corte e frames, tabela de PA, exemplo numérico fictício percorrido), `integridade_do_dado.md` (checklist de sinal contaminado, parar e conciliar, regra dos 60 dias, ritual do residual), `dicionario.md` (termos com dono da passagem e onde mede, funil padrão e de-para, regra de conflito).
- `ALERTAS OPERACIONAIS` nos cinco DNAs em áudio e vídeo (`acf_lab`, `arquitetura_midia`, `engenharia_crescimento`, `gtm_e_revops`, `ma_e_valuation`): as regras de decisão das antigas seções de voz, sem a voz.
- `copy_e_headline.md` ganha `nivel: ATIVO` e as seções flecha central, primeira frase, estrutura de VSL, proposta e cliente, ética de copy e referência rápida.
- Todos os arquivos novos e alterados levam `revisao_pendente: Sarden`; o `aprovado:` entra depois da leitura dele. `susano-ativos` cresce com os modelos ativos dos DNAs novos (MANIFEST com 121 gerenciados).

### PR-1 `v0.3-nucleo` (01/11/2026)

- `nucleo.md` e `identidade.md`: P-05 passa a "o dado aponta o gargalo; o gargalo chama o modelo; modelo nunca entra antes do dado"; P-06 define frente (projeto, cliente, conta ou produto) e manda `/nova-frente` em vez de inventar contexto; "Sempre e nunca" ganha: editar só o pedido e sinalizar toda adição, pensar antes de perguntar (uma pergunta com default ou um lote por dimensão), marcador só em documento interno (entregável de cliente, playbook publicado e slide saem sem marcador), "rodando" só no ar sem dependência aberta, referência de mercado como [INFERÊNCIA] com fonte e data e nunca como target; tom mantido como aprovado, com a calibração a quem está na sessão em dois registros (decisão do Sarden, 22:40). Teto do núcleo passa de 2.000 para 2.200 tokens estimados (2.095 medidos). `revisao_pendente: Sarden` nos dois arquivos até ele ler os acréscimos.
- `experimentos.md` como quarto arquivo canônico da frente (`_templates/experimentos.md`; `brain.py novo` cria; `validate` exige frontmatter e data; `salve`, `frente`, `segundo_cerebro.md` e `CONVENCOES.md` acompanham): hipótese com corte → resultado → decisão; "sistematizou" aponta para o playbook que nasceu.
- Convenção única de branch: `salve/AAAA-MM-DD-<tema>`, `estado-quente/AAAA-MM-DD`, `susano-vX.Y.Z` (salve, estado-quente, rotina, CONTRIBUTING, CONVENCOES).
- `brain.py`: domínio `exemplos` (skill `susano-exemplos`, gerada quando a pasta existir); `indice` ganha a seção "Operação"; `validate` barra tipo `resumo` (é `pensador` ou `referencia`), exige ENTRADA, SAÍDA e POR QUE ASSIM em tipo `exemplo` e trata `experimentos.md` como os outros três; `primeira_frase` não corta em "vs.", "ex.", "p.", "aprox."; `linhas_ativos` ignora sub-bullet; descrição da `susano-ativos` muda para "consult when the diagnosis names the gargalo".
- Skill `analise` (template e plugin): marcador só em documento interno; o nome do conector interno de dados sai (vira "a SQL connector"); notas de plataforma novas (export do Meta Ads Manager em XML Spreadsheet, CSV do Google Ads em utf-16, MCC e `customer_id` da conta folha, `search_term_view`, `conversion_action.primary_for_goal`, histórico de propriedade fora do MCP do HubSpot, BP só pelo `.xlsx`, dashboard em imagem por seção). Skill `frente` lê `experimentos.md` e lista cortes vencendo (a substituição de `$slug` por `$ARGUMENTS` proposta no plano não entra: `arguments:` com `$nome` é campo oficial do Claude Code, conferido na documentação em 01/11/2026). Estilo de saída e `CLAUDE.md`: calibração do tom, dado antes do modelo, os quatro arquivos da frente.
- `AGENTS.md` do projeto: "Modo sem shell" para agente de chat (lê a mesma ordem, não roda `brain.py`, termina com a lista do que deveria ser salvo e onde); regra 5 separa valor de contrato de cliente (fora) de mecânica de pricing do método (pode entrar). Regras `seguranca`, `frentes` e `conhecimento` idem; `conhecimento` deixa de dizer que o `ATIVOS.md` é pré-carregado.
- Os dois arquivos do Stories 10x saem de `biblioteca/ladeira/` para `referencias/social_organico/` como `tipo: referencia` (eram `resumo` sem o esqueleto de pensador); `[DADO AUSENTE]` vira `[LACUNA]`; restos de pandoc (`---`) limpos; o domínio `performance` passa a cobrir social orgânico. Proveniência interna (`raio_docN`) sai do `fonte:` dos procedimentos de `metodo/`.
- `onboarding`: pre-commit vira padrão em sessão local; campo `preferencias` aceita convenções de leitura (voz ditada). Testes: 58 casos (5 novos: `experimentos.md` nasce com frontmatter, sem frontmatter barra, exemplo sem POR QUE ASSIM barra, tipo `resumo` barra, volta a passar).


## v0.2.1 (2026-11-01)

- Publicação: repositório público `github.com/sardenberg182/susano` criado pelo Sarden (ordem de 01/11/2026, 19:00; só este repositório, nada da Oficina nem do segundo cérebro privado da organização). README, catálogo e manifesto do plugin com o endereço real; instalação `claude plugin marketplace add sardenberg182/susano` e `copier copy gh:sardenberg182/susano`.
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
