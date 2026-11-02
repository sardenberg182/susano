---
id: ref-lp-playbook-construtor-html
tipo: referencia
autor: Sarden
origem: playbook operacional do agente construtor de landing page em HTML, v3.0 (16/10/2026), da operação do Sarden; camada de craft Impeccable 4.6 (pbakaus/impeccable, Apache-2.0); casos internos anonimizados para o modelo
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo no modelo na v0.3.0; registrar aprovado após leitura)
---

# PLAYBOOK OPERACIONAL | AGENTE CONSTRUTOR DE LANDING PAGE EM HTML
> Uso: agentes de execução (Claude Code, Cursor, Codex ou o Susano no claude.ai) que constroem a página (HTML, CSS e JS) com racional de performance, conversão, copy e estrutura, e com craft visual no modelo Impeccable
> Versão: 3.0 | Data: 16/10/2026 | Owner: Sarden | Substitui a 2.0 (construtor de HTML sem camada de craft) e a 1.0 (pacote em Markdown)
> Documento-mãe: `00_susano/instrucoes/landing_pages.md` (a lente, a ficha dos 17 campos e o QA de sete blocos). A lente explica o porquê; este arquivo diz o que fazer, na ordem, até a página existir.
> Camada de craft: Impeccable 4.6 (pbakaus/impeccable, Apache-2.0), skill de design para agentes de código. Comandos, regras e detector descritos no Anexo G.
> Idioma de trabalho e de entrega: português (pt-BR)

---

## 0. COMO USAR ESTE PLAYBOOK

Este documento é um passo a passo. Ele segue a ordem em que uma landing page acontece: entender → definir a conversão → decidir o mundo visual → decidir estrutura e primeira dobra → escrever → construir o HTML com compromisso total → formulário → medir → thank-you → QA com detector e revisão de acabamento → entregar com DESIGN.md → analisar. Cada fase tem entradas, ações, saída obrigatória e um gate. O gate é a condição para avançar. Agente não pula gate.

### 0.1 O que o agente entrega

O produto do agente é a **página pronta em HTML**: `index.html`, `obrigado.html` e a pasta `assets/`, publicáveis em qualquer destino (arquivo estático, HubSpot, WordPress, Webflow, Netlify, Cloudflare Pages). Os documentos de trabalho (`docs/`) registram decisões, contrato de direção, copy, tracking, QA, perguntas respondidas e o DESIGN.md do cliente; eles acompanham a página, não a substituem.

### 0.2 Duas camadas, uma hierarquia

| Camada | O que governa | Fonte |
|---|---|---|
| **Conversão** (governa) | objetivo único, três leitores, CTA sempre à mostra, dispositivo pelo canal, formulário mínimo, tracking antes de tráfego | racional do Sarden e knowledge do Susano |
| **Craft visual** (serve a conversão) | mundo visual próprio, composição da primeira dobra, tipografia, cor em escala de página, movimento autoral, piso de qualidade, detector | Impeccable (modo Persuade) |

Conflito entre as camadas se resolve a favor da conversão: uma composição ousada que esconde o CTA ou atrasa a leitura da oferta em 3 segundos não está pronta, ela ainda não terminou de traduzir o mundo para a página. O próprio Impeccable diz isso no modo Persuade: a conversão vive dentro do vocabulário da forma escolhida (gancho em uma linha, ação primária visível, ordem de leitura legível). `[IMP]` mode-persuade.

### 0.3 Divisão de responsabilidades

| O quê | De quem | Regra |
|---|---|---|
| Racional de performance, conversão, copy e estrutura | Do agente, sempre | Não é opcional e não depende do cliente. |
| Craft visual: mundo, composição, tipografia, cor, movimento, acabamento | Do agente, sempre | Página "quadrada" (template da categoria com a cor do cliente) reprova no QA. |
| Design system existente (cores, tipografia, logo, componentes, restrições) | Insumo pedido ao cliente na fase 0 | Mundo estabelecido se herda; o agente não "moderniza" marca de cliente. |
| Decisões de mundo visual quando não existe design system | Do Sarden, em rodada de decisão com opções preparadas pelo agente | O agente prepara as direções; o Sarden trava uma. |
| Dados da página (provas, números, prazos, preços, SLA, nomes) | Do projeto, confirmados por quem responde | Sem confirmação, o bloco não é escrito. |
| Insumos técnicos (domínio, destino, GTM, formulário, CRM, WhatsApp, política) | Do projeto, levantados na fase 0 | Sem eles a página não publica nem mede. |

Quando o design system contraria um racional de conversão (cor de botão sem contraste, fonte de título ilegível em 360 px, exigência de menu completo), o racional vence. O agente aplica a regra, registra a exceção em `01_ficha.md` e avisa o Sarden na mensagem de entrega.

### 0.4 Regras invioláveis

1. **Toda landing page existe para converter.** Informar é meio. Se a conversão não está escrita em uma linha, a página não existe ainda.
2. **Sem inferência e sem pendência.** O que o agente não sabe com dado do projeto, do knowledge ou de fonte citada vira pergunta ao Sarden ou ao cliente antes de escrever. Nunca preencher com suposição. Nunca entregar um bloco com marcador de pendência: pendência no documento gera dúvida em quem lê.
3. **Nunca inventar.** Número, depoimento, nome de cliente, logo, prêmio, nota de avaliação, resultado de case, prazo de entrega, preço, SLA. Se não existe confirmado, o agente pergunta, associa a fonte e verifica; só então escreve o bloco. Material de demonstração (uma tela ilustrativa, um exemplo de relatório) pode ser autorado em fidelidade total, rotulado "exemplo ilustrativo" e listado para substituição; afirmação comercial, nunca. `[IMP]` skill-truth-binds-claims.
4. **Escassez e urgência só quando reais.** Vaga limitada tem número. Prazo tem data. Bônus que some, some. Contador regressivo falso não existe nesta página.
5. **Uma página, uma conversão, um CTA.** Mesmo texto de CTA do topo ao rodapé. Sem navegação, sem links de saída.
6. **CTA sempre à mostra** em qualquer ponto da rolagem, mobile e desktop: no hero pelo botão, no meio pela barra fixa (mobile) ou pelo header (desktop), no fim pelo formulário.
7. **Mobile fácil de clicar e fácil de preencher**, independentemente da direção de dispositivo da página.
8. **Dispositivo vem do canal, do histórico e do benchmark, nessa ordem.** B2B ou B2C não decide nada.
9. **Tracking antes de tráfego.** Página sem evento de conversão testado não é entregue como pronta.
10. **Formato de texto:** sem travessão (usar vírgula, dois-pontos ou →), números em pt-BR (1.250 e 12,5%), frases de até 20 palavras, nível de leitura simples, zero jargão desnecessário.
11. **Perguntar, associar, verificar.** Toda dúvida vira pergunta objetiva, enviada em lote no momento do gate, com a decisão que ela desbloqueia. A resposta é registrada com fonte e data no log de perguntas e respostas. Nenhum marcador de pendência, verificação ou inferência existe nos entregáveis.
12. **Fonte sempre.** Benchmark ou prática de mercado entra com fonte e ano. Princípio entra com o livro, arquivo do knowledge ou regra do Impeccable. Dado do projeto entra com quem confirmou e quando.
13. **HTML próprio, leve e em um arquivo.** Sem framework de CSS ou JS. O único script de terceiro na página é o Google Tag Manager; pixels e conversões vivem dentro do container.
14. **Estratégia não viaja no HTML.** O racional de cada seção (leitor, objetivo, como empurra para o CTA) e o contrato de direção vivem em `docs/01_ficha.md`. O HTML entregue carrega só o código da seção (`data-secao`). Comentário com estratégia de persuasão no código-fonte é dado que o concorrente lê. `[IMP]` new-work, seção 5.
15. **Compromisso total com a direção escolhida.** O build nasce na direção travada, não em uma versão mais segura dela. Botão, campo, link e lista são reconstruídos no vocabulário do mundo; componente de estoque dentro de uma forma comprometida é lapso. `[IMP]` skill-commit-every-atom.
16. **O detector roda antes da entrega e termina sem achado.** `npx impeccable detect index.html obrigado.html`, exit 0. Achado aceito só com exceção aprovada pelo Sarden e registrada no arquivo (`impeccable-disable` com motivo). Sem shell, o checklist manual da fase 9.1 substitui e a entrega diz que o detector não rodou.
17. **Placeholders dos templates deste playbook (`{{...}}`) nunca chegam à entrega.** O QA (fase 9) procura e barra.

### 0.5 Origem das regras (legenda)

`[K]` knowledge do Susano (livro ou método) · `[P]` dado primário de mercado ou padrão técnico público · `[V]` dado de vendor, direcional · `[I]` caso interno da operação do Sarden (cliente e número ficam fora deste repositório) · `[IMP]` regra do Impeccable, com o id da regra quando ele existe no kit · sem marca = regra operacional deste playbook, definida pelo método

### 0.6 Fluxo em uma linha

Fase 0 Entender → Fase 1 Ficha → Fase 2 Mundo visual e contrato de direção → Fase 3 Tipo, estrutura e primeira dobra → Fase 4 Copy → Fase 5 HTML → Fase 6 Formulário → Fase 7 Tracking → Fase 8 Thank-you → Fase 9 QA, detector e revisão de acabamento → Fase 10 Entrega e DESIGN.md → Fase 11 Realidade

### 0.7 Rodadas de decisão (as únicas três)

| Rodada | Fase | O que o Sarden ou o cliente decide | Quando existe |
|---|---|---|---|
| 1. Insumos | 0 | respostas ao lote de perguntas (ICP, canal, provas, design system, insumos técnicos) | sempre |
| 2. Direção visual | 2 | qual mundo visual, entre 3 direções preparadas + a saída padrão (o convencional da categoria, bem feito) | só quando não há design system estabelecido; com design system, pula |
| 3. Primeira dobra | 3 | qual composição da primeira dobra, entre 3 esboços | sempre |

Cada rodada é enviada como um conjunto de opções com a decisão que desbloqueia. Com a ferramenta de pergunta estruturada disponível, as opções vão por ela; sem ela, em uma mensagem, e o agente espera. Se o Sarden delega a escolha em palavras, o agente escolhe pela ficha, declara a evidência no log de perguntas e segue. `[IMP]` visualize, "One approval point".

---

## FASE 0 | ENTENDER (antes de qualquer linha de código)

**Entradas:** brief do Sarden ou do cliente; contexto do projeto (knowledge, CRM, site atual); histórico de tráfego (GA4 fonte/mídia × dispositivo, relatório de cliques por dispositivo da ferramenta de e-mail, campanhas anteriores); benchmark do segmento; design system ou materiais de marca; insumos técnicos.

**Ações:**
1. Ler o ICP do projeto. Escrever em uma linha quem é o leitor e onde ele está quando clica.
2. Identificar o canal de entrada e a jornada: de onde vem o clique e em que tela abre.
3. Levantar o histórico de dispositivo por canal. Registrar os números com data e fonte. Se não existe, registrar "sem histórico" e buscar o benchmark do segmento com fonte e ano.
4. Levantar a temperatura do tráfego: quente (já conhece), morna (conhece quem indicou), fria (não conhece). `[K]` DotCom Secrets.
5. Levantar as provas reais disponíveis: cases com número, depoimentos com nome e cargo, logos autorizados, notas de avaliação, certificações, anos de mercado. Só entra o que o projeto confirma.
6. Identificar a objeção principal (a razão número um pela qual o leitor frio não converte) e as secundárias. `[K]` top 10 objeções, Fórmula de Lançamento.
7. Identificar o Big Domino: a crença que, instalada, torna as outras objeções irrelevantes. `[K]` Expert Secrets.
8. Responder, com o cliente, as três perguntas do modo Persuade: quem precisa agir, no que precisa acreditar para agir, e qual prova, conteúdo ou asset real ganha essa crença. Mais duas de fechamento: o que precisa ficar intocado, e o que faria um resultado polido parecer errado para esse cliente. `[IMP]` new-work, seção 2.
9. Descrever a cena de uso em uma frase: quem abre a página, onde, em que luz e em que estado de espírito. Essa frase decide claro ou escuro na fase 2 e a energia da página. `[IMP]` skill-reflex-theme-by-habit.
10. Pedir o design system ou, na falta dele, os materiais de marca (lista na fase 2.1). Pedir também o site atual ou qualquer página do cliente que já exista: o que já é coerente no código do cliente é mundo estabelecido, mesmo sem documento. `[IMP]` new-work, seção 1.
11. Levantar os insumos técnicos da tabela abaixo.
12. Listar tudo que falta como pergunta objetiva, cada uma com a decisão que ela desbloqueia, e enviar em um único lote ao Sarden ou ao cliente (rodada de decisão 1).

**Insumos técnicos (pedir todos no mesmo lote):**

| Insumo | Para que serve | Quem fornece |
|---|---|---|
| Domínio ou URL final da página | canonical, OG, UTMs, QA de tracking | cliente ou Sarden |
| Destino de publicação (arquivo estático, HubSpot, WordPress, Webflow, Netlify, Cloudflare Pages, outro) | decide como o HTML será publicado e se o formulário usa API ou embed | Sarden |
| ID do container GTM (GTM-XXXXXXX) | único script de terceiro da página | Sarden ou time de tracking |
| Mecanismo de envio do formulário (HubSpot Forms API com portalId e formGuid, embed HubSpot, RD Station, webhook, Netlify Forms) e nomes internos dos campos no CRM | o lead precisa cair no CRM com origem | Sarden ou admin do CRM |
| Número do WhatsApp com DDI e DDD, e quem atende (humano ou bot) | link wa.me e evento de conversa iniciada | cliente |
| URL da política de privacidade e texto de consentimento aprovado pelo jurídico do cliente (linha de aviso ou checkbox) | bloco LGPD do formulário | cliente |
| Razão social e dados do rodapé que o cliente exige | rodapé mínimo | cliente |
| Logo em SVG (ou PNG com fundo transparente), paleta, fontes licenciadas (arquivos woff2), fotos reais do time, produto, serviço e clientes | tokens da fase 2 e assets | cliente |
| Indexação da página (sim ou não) | meta robots e canonical | Sarden |
| SLA de resposta ao lead e responsável pelo atendimento | thank-you e microcopy do CTA | cliente |

**Saída obrigatória:** `docs/00_entendimento.md` (template no Anexo D.1) com todas as perguntas respondidas e registradas com fonte e data. Quando o agente roda com o kit Impeccable instalado, as mesmas respostas alimentam o `PRODUCT.md` via `/impeccable init` (mapa de campos no Anexo G.3).

**Gate 0:** ICP, canal, temperatura, objeção principal, as três perguntas do Persuade, a cena de uso, o status do design system e os insumos técnicos registrados com fonte. Todas as perguntas respondidas. Sem resposta, não avança; o agente aguarda, não presume.

---

## FASE 1 | FICHA DE DEFINIÇÃO DA PÁGINA

Preenchida antes de qualquer estrutura. Sem ficha, não há página.

1. **Conversão única:** esta página existe para ___ (uma linha).
2. **Tipo de conversão:** final (lead, agendamento, compra, trial, inscrição) ou de etapa (clique para a próxima página, avanço de step). Se multi-step: lista dos steps e a conversão única de cada um.
3. **Evento medido:** envio confirmado, conversa iniciada no WhatsApp, agendamento, compra. Nunca clique no botão.
4. **Canal e jornada de entrada:** de onde vem o clique e em que tela abre. Canal mobile por natureza (disparo de WhatsApp, SMS, Meta, Stories) fecha a decisão de dispositivo aqui.
5. **Direção de dispositivo da v1:** mobile ou desktop, com a origem da decisão (canal, histórico ou benchmark) e a data da primeira revisão com dado real.
6. **Temperatura:** quente, morna ou fria.
7. **Leitor 1 (hero):** o que ele precisa ver em 3 segundos para clicar.
8. **Leitor 2 (confirmação):** as 2 a 3 perguntas que ele faz antes de clicar.
9. **Leitor 3 (convencimento):** objeção principal e secundárias.
10. **CTA:** texto em primeira pessoa com o deliverable, posições (hero, meio, final), visibilidade (barra fixa no mobile, header no desktop).
11. **Pós-conversão:** o que acontece nos 5 minutos seguintes (thank-you com SLA, próximo degrau).
12. **Tracking:** evento, UTM, pixel e CAPI, campo de origem no CRM.
13. **Destino de publicação e URL final.**
14. **Mecanismo de envio do formulário** (ou caminho WhatsApp) e nomes dos campos no CRM.
15. **Autoridade visual:** design system recebido (fonte, data) / mundo coerente no site atual do cliente (URL) / marca incompleta (o que está confirmado) / sem autoridade visual (rodada de decisão 2 obrigatória).
16. **Indexação:** sim ou não.
17. **Cena de uso** (uma frase) e **claro ou escuro** decidido por ela.

**Protocolo de dispositivo (ordem de peso):**
1. Canal e jornada da campanha. Jornada mobile por natureza = página mobile. Fim da decisão.
2. Modelo de negócio e histórico do projeto. Canal misto (Search, e-mail, orgânico, LinkedIn) = o dispositivo vem do público e do histórico. B2B ou B2C não decide.
3. Benchmark de mercado. Direção de largada quando não há histórico. Projetar a v1 conforme o benchmark é aceitável; usar benchmark como decisão final não é.

A v1 é sempre **meio-termo**: uma página que funciona por completo nos dois dispositivos, com hierarquia visual e formulário otimizados para o lado da decisão. No HTML isso se traduz em: CSS mobile-first em todos os casos; posição do formulário e composição da primeira dobra decididas pela direção (fases 3 e 5.3).

**Saída obrigatória:** `docs/01_ficha.md` (template no Anexo D.2), seções "Ficha" e "Protocolo de dispositivo".

**Gate 1:** os 17 campos preenchidos com dado confirmado. Campo vazio ou em dúvida volta para a fase 0 como pergunta.

---

## FASE 2 | MUNDO VISUAL, CONTRATO DE DIREÇÃO E TOKENS

Aqui a página deixa de ser "o template da categoria com a cor do cliente". O Impeccable chama isso de decidir o mundo visual antes de escrever código; este playbook adapta o fluxo dele ao trabalho de agência: o cliente manda na marca, o Sarden trava a direção, o agente prepara e executa.

### 2.1 Decidir o que já é verdade (autoridade visual)

Ler o design system, o site atual, tokens, componentes e assets do cliente. Classificar em uma das quatro situações. `[IMP]` new-work, seção 1.

| Situação | O que fazer | Rodada 2 |
|---|---|---|
| **Design system existente** (documento, Figma, DESIGN.md, tokens) | herdar por completo; o trabalho é composição e craft dentro do sistema | não existe |
| **Mundo coerente no código do cliente, sem documento** | documentar o que existe (cores, tipos, formas, componentes) e herdar; não inventar substituto | não existe |
| **Marca incompleta** (logo e 1 ou 2 cores confirmadas, resto aberto) | preservar o confirmado e expandir o sistema para esta página com o Sarden | existe, com o confirmado como restrição pinada |
| **Sem autoridade visual** | criar um mundo com o Sarden | existe |

Materiais a pedir (fase 0), em qualquer situação:

| Material | Formato aceito | Usado em |
|---|---|---|
| Logo principal e versão para fundo escuro | SVG (preferido) ou PNG transparente | header, rodapé, OG |
| Paleta: primária, secundária, fundo, superfície, texto, texto suave, borda, erro, sucesso | hexadecimal | tokens |
| Cor do CTA e cor do texto do CTA | hexadecimal, contraste medido | botão, barra fixa |
| Tipografia de título e de texto, pesos disponíveis | arquivos woff2 licenciados; ou "fonte do sistema" quando o design system define isso | tokens, @font-face |
| Estilo de botão (raio, altura, caixa alta ou não) | descrição ou exemplo | tokens |
| Fotos reais (time, produto, serviço, cliente), ícones, mockup do entregável | WebP, AVIF, JPG, SVG | primeira dobra, prova, mecanismo |
| Restrições de marca (o que não pode) | lista | exceções registradas |
| Imagem para compartilhamento (OG) 1200×630 ou autorização para o agente montar com logo e headline | JPG ou PNG | pré-visualização no WhatsApp, LinkedIn e Meta |

### 2.2 Preparar as direções (só nas situações "marca incompleta" e "sem autoridade visual")

O agente prepara, o Sarden trava. Procedimento, adaptado de `[IMP]` new-work, seção 3 ("Create or replace the visual world") e skill-concept-procedure:

1. Escrever em uma frase o mecanismo único do produto ou serviço, a cena real do público, o lugar cultural desse público e o que esta página precisa provar.
2. Nomear o que a categoria sempre entrega (a página óbvia: contabilidade em azul com foto de stock e três cards; SaaS em Inter com gradiente roxo) e o oposto previsível dela. Os dois ficam fora da lista de candidatos: são a rotina. `[IMP]` skill-calibration-saturated-looks.
3. Listar sete sistemas visuais, artefatos, lugares ou rituais que esse público conhece de cor, cada um com uma linha de por que ressoa e carrega o mecanismo, e uma linha de como se parece (fundo e cores principais, vozes tipográficas, a assinatura que o torna reconhecível). Ordenar por ressonância. O mundo do público inclui o que ele lê e usa todo dia (notações, publicações, programas de identidade, gráficos, interfaces), não só objetos físicos. Quando mais de três dos sete vêm da mesma família de material, a derivação parou no artefato mais óbvio: cavar até cobrir três famílias.
4. Transformar os três mais fortes (de famílias diferentes) em direções completas. Cada direção é um cartão com a mesma anatomia: **tese** (a ideia que esta página possui e o arranjo padrão que recusa), **paleta** (estratégia de cor e 3 a 5 cores com papel), **materiais e tipografia** (vozes de título e texto, com a fonte nomeada), **primeira dobra** (o que está onde, em que escala, onde fica a ação primária), **o que faz pela conversão** (como serve o teste dos 3 segundos e a prova), **risco honesto** (o que pode dar errado, inclusive "familiar demais"). `[IMP]` skill-pick-card-one-only, anatomia dos cartões.
5. Acrescentar a **saída padrão**: o convencional da categoria, executado com craft de referência (nomear 2 ou 3 produtos ao lado dos quais a página vai sentar). Ela é a porta do Sarden, nunca a recomendação do agente; quando o Sarden a escolhe, a convenção vira o compromisso e é executada em fidelidade total, sem ironia. `[IMP]` skill-canon-standing-exit.
6. Enviar os quatro cartões como rodada de decisão 2. Pedido de "mais ousado" ou "mais seguro" nessa rodada é pedido de uma nova mão de direções nesse registro, não de ajuste de um cartão. `[IMP]` skill-assigned-plus-reroll.

Teste de calibragem antes de enviar: se alguém adivinharia o visual de cada cartão só pela categoria do cliente, ou pela categoria mais "o que a IA evita", o cartão ainda é a rotina. Os quatro visuais que toda IA entrega quando o brief está livre: creme com serifa de alto contraste e terracota; quase-preto com um neon e bordas brilhantes; hairlines editoriais com serifa itálica e rótulos em mono; tinta chapada saturada com caixas pretas, sombras duras e display condensado. Legítimos quando o brief pede; rotina quando o brief está livre. `[IMP]` skill-calibration-saturated-looks. Assunto "quente", familiar ou institucional não amolece a calibragem: energia não é inimiga de confiança. `[IMP]` skill-constraints-rule-out-devices-not-energy.

### 2.3 Comprometer o mundo (todas as situações)

Com o mundo decidido (herdado ou travado), fixar antes de qualquer token:

- **Estratégia de cor**, antes das cores: Contida (neutros tingidos do mundo + 1 acento), Comprometida (uma cor saturada carrega 30 a 60% da superfície), Paleta completa (3 ou 4 papéis nomeados) ou Encharcada (a superfície é a cor). Página de conversão tem permissão para as mais ousadas; com design system, a estratégia se escolhe dentro dele (normalmente Comprometida: a primária do cliente possui regiões inteiras, hero ou prova ou fechamento). A cor se compromete em escala de página: campos que possuem regiões inteiras, não acentos espalhados sobre fundo neutro. `[IMP]` skill-color-strategy.
- **Claro ou escuro** pela cena de uso da ficha (campo 17), nunca pela categoria. `[IMP]` skill-reflex-theme-by-habit.
- **Tipografia** com ponto de vista, escolhida como objeto do mundo do público. Sem design system, a fonte vem da direção travada e se auto-hospeda em woff2 (nunca a folha de estilo hospedada do Google Fonts: é um terceiro a mais e uma requisição bloqueante). Fontes que significam "parei de procurar" quando o brief está livre: Inter como display, Space Grotesk, Space Mono, IBM Plex, DM Sans, DM Serif, Outfit, Plus Jakarta Sans, Instrument Sans, Fraunces, Playfair Display, Cormorant, Lora, Crimson, Newsreader, Syne. Usar uma delas exige motivo que nenhuma outra fonte satisfaça; associação de assunto não é motivo. Fonte de display do sistema (Arial Black, Impact, a sans da plataforma) como voz da página também não. `[IMP]` skill-typo-reflex-faces, skill-ban-system-display-face.
- **Neutros tingidos**: texto, borda e fundo derivam do matiz do mundo; preto e cinza puros não entram. `[IMP]` README, anti-patterns.
- **Ícones desenhados** (SVG autoral ou biblioteca real, um só peso de traço); nunca glifo Unicode ou emoji no lugar de ícone. `[IMP]` skill-ban-glyph-icons.
- **Imagem real** quando o brief implica: a foto do objeto físico do assunto, não a da categoria; uma foto decisiva vale mais que cinco medianas. Stock em serviço local sinaliza agregador, não prestador. `[V]` `[IMP]` new-work, "Use real, verified imagery".

### 2.4 Contrato de direção (seis blocos, cerca de 150 palavras)

Registrado em `docs/01_ficha.md`, nunca no HTML. Se um bloco lê como clima ("moderno, clean, confiável"), a direção ainda não está decidida. `[IMP]` skill-decide-then-build.

| Bloco | O que escreve |
|---|---|
| **TESE** | a ideia que esta página possui e o arranjo padrão da categoria que ela recusa |
| **MUNDO PRÓPRIO** | paleta e linguagem de componentes, específicas o bastante para serem reconhecidas com todo o conteúdo removido |
| **HISTÓRIA** | o que o visitante entende, no que acredita e o que faz (os três leitores, na ordem) |
| **PRIMEIRA DOBRA** | a composição exata: o que está onde, em que escala, onde fica a ação primária, o que fica visível em 360×640 |
| **FORMA** | a forma escolhida (cartão travado na rodada 2 ou mundo herdado) e a interação-assinatura (um movimento autoral, se houver) |
| **ACABAMENTO** | a condição de saída, literal: "sem revisão de acabamento e sem DESIGN.md a página não está pronta" |

### 2.5 Tokens (bloco `:root` do HTML)

| Token | O que define | Regra |
|---|---|---|
| `--cor-primaria` e `--cor-sobre-primaria` | identidade e o texto que senta sobre ela quando a primária vira campo | texto sobre a primária com contraste mínimo 4,5:1 `[P]` WCAG 2.2 SC 1.4.3 |
| `--cor-cta` e `--cor-cta-texto` | botão de conversão e barra fixa | a cor de maior contraste da paleta aprovada; o CTA é o elemento de maior contraste em qualquer campo da página; texto do botão com 4,5:1 |
| `--cor-fundo` e `--cor-superficie` | fundo da página e fundo de formulário e header | texto sobre fundo com 4,5:1; neutros tingidos do matiz da primária |
| `--cor-texto` e `--cor-texto-suave` | texto corrido e microcopy | texto suave também passa em 4,5:1; sobre campo colorido, o secundário se tinge do próprio matiz, nunca cinza `[IMP]` skill-color-verify-contrast |
| `--cor-borda`, `--cor-erro`, `--cor-sucesso` | campos, mensagens | erro nunca só por cor: texto junto |
| `--fonte-titulo` e `--fonte-texto` | tipografia | no máximo 2 arquivos woff2 no total; `font-display: swap`; fallback `system-ui, sans-serif` |
| `--raio` | raio de botões e campos | do estilo de botão da marca; cartão, quando existir, entre 12 e 16 px; pílula só em controle pequeno `[IMP]` craft-floor |
| `--sombra` | elevação, quando a direção usa sombra | deslocamento e desfoque suave; halo colorido sem deslocamento é decoração; sombra dura (`4px 4px 0`) só em mundo neobrutalista de verdade `[IMP]` skill-color-no-glow-halo, skill-ban-hard-offset-shadow |
| `--largura-max` | largura do conteúdo no desktop | 1120 px (padrão do playbook; a direção pode pedir outro) |
| `--altura-cta` | altura mínima do botão | 56 px no mobile, nunca abaixo de 48 px |
| `--altura-barra` | altura da barra fixa de CTA no mobile | 72 px, incluindo a área segura do iPhone |
| `--icone-check`, `--icone-seta` | ícones em SVG inline (data URI) usados por máscara | um peso de traço para todos |

Sem design system, os neutros se derivam da primária no próprio CSS, por exemplo `--cor-texto: color-mix(in oklab, var(--cor-primaria) 15%, #141414)`; o contraste se mede na página renderizada (o detector mede ao escanear a URL).

### 2.6 Regras de conflito entre marca e conversão

- O CTA usa a cor de maior contraste da paleta aprovada, mesmo que não seja a "cor principal" da marca. Se nenhuma cor da paleta atinge 4,5:1 com texto branco ou preto, o agente pede ao Sarden uma cor de CTA no lote de perguntas; não escolhe sozinho.
- Fonte de título decorativa ou condensada que fique ilegível em 360 px no tamanho de H1 vai só para o logo; o H1 usa a fonte de texto em peso forte. A exceção é registrada na ficha.
- Menu, links sociais, rodapé institucional completo: não entram, mesmo que o site do cliente tenha. Rodapé é logo, razão social, política de privacidade e nada mais.
- Vídeo de fundo, parallax e animação de entrada em toda seção: não entram. Custam LCP e INP e não empurram para o CTA.

**Saída obrigatória:** `docs/01_ficha.md` com autoridade visual, estratégia de cor, claro ou escuro, fontes, contrato de direção (seis blocos) e tabela de tokens com contraste medido; `assets/` com logo, favicon, fontes e imagem OG.

**Gate 2:** contrato de direção com seis blocos sem clima; nenhum token vazio; contraste medido; teste de calibragem respondido por escrito; todos os assets de marca existentes ou com produção acordada (responsável e data).

---

## FASE 3 | TIPO, ESTRUTURA E PRIMEIRA DOBRA

### 3.1 Tipo

Cruzar temperatura × conversão e escolher o tipo. Registrar o porquê em duas linhas.

| Tipo | Quando usar | Temperatura | CTA | KPI |
|---|---|---|---|---|
| Squeeze (opt-in) | Lead magnet, lista própria | Morno ou frio | 1 a 2 campos | Custo por lead |
| Lead gen B2B consultivo | Diagnóstico, demo, implementação | Quente ou morno | Agendar | SQL agendado, show rate |
| Serviço B2C ou local | Contabilidade, clínica, serviço recorrente | Quente ou morno | Form curto ou WhatsApp | Conversa → MQL no CRM |
| Sales page longa ou VSL | Infoproduto, mentoria, ticket médio-alto | Frio ou morno | Comprar | Checkout, compra |
| Bridge, advertorial, quiz | Meta frio, native, influencer | Frio | Click-through ou avanço de step | CTR da bridge → CVR na LP |
| Webinar ou evento | Educar antes de vender | Frio ou morno | Inscrição | Inscrição → show-up |
| Click-through ou trial | SaaS self-serve, e-commerce | Morno ou quente | Começar grátis | Ativação |
| Thank-you | Pós-conversão | Quente | Próximo degrau | Degrau seguinte, SLA |

Regra: temperatura define o tamanho do pedido. Frio pede micro-compromisso; quente aceita pedido direto. `[K]` DotCom Secrets. Searcher (Google) recebe página direta; scroller (Meta, TikTok) recebe bridge ou narrativa. `[K]` Traffic Secrets.

### 3.2 Estrutura (ordem das seções)

- Ordem = blueprint do tipo (Anexo C). O blueprint fixa a lógica de conversão (o que vem antes do quê); ele não fixa composição. Alteração de ordem exige justificativa na ficha.
- CTA em 3 pontos em página longa (hero, após a prova, final); um único acima da dobra em página curta. `[V]` LanderLab.
- Sem menu, sem links sociais, sem rodapé cheio. Só CTA e links legais.
- **Mapa de conexão (obrigatório):** tabela com todas as seções, o leitor que cada uma serve, o objetivo e a resposta à pergunta "esta seção empurra para o CTA?". Seção que não empurra sai da página. O mapa vive em `01_ficha.md` (regra 14).
- **Ritmo da rolagem:** o mapa também marca a densidade de cada seção (densa, média, quieta) e onde ficam o pico (normalmente a prova) e o fechamento real (CTA final com SLA). Uma passagem densa ganha uma quieta; a página termina ancorada em um fechamento, não esvai. `[IMP]` new-work, "Pace the scroll like a studio".

### 3.3 Primeira dobra (rodada de decisão 3)

A primeira dobra é uma tese, não um cabeçalho. Ela demonstra o mecanismo de cara, na escala que ele tem na vida real, em vez de prender o conceito dentro de um hero padrão. `[IMP]` new-work, "The first viewport is a thesis". O conteúdo de conversão dela é fixo (regras do Sarden); a composição é o que se decide aqui.

**Invariantes de conversão (todo esboço cumpre):**
- Headline, prova imediata e CTA visíveis sem rolar em 360×640 e em 1440×900.
- A ação primária é inconfundível e é a ação real da categoria (formulário, agendamento, WhatsApp), não um link decorativo que aponta para ela em outro lugar. `[IMP]` skill-persuade-conversion-in-form.
- Ordem de leitura legível: gancho → sub → prova → ação, em qualquer composição.
- Nada acima do H1 (sem kicker, sem pré-título): o título carrega o próprio peso. `[IMP]` skill-ban-eyebrow-on-every-section.

**Os três esboços variam o que uma imagem resolve:** o que lidera a tela (a oferta, a prova, o mecanismo demonstrado, o entregável real), a topologia (assimétrica, tipográfica, o produto em funcionamento, o objeto do mundo), a escala e o foco. Nenhum dos três pode ser o template: hero dividido com texto à esquerda, imagem à direita e fileira de logos embaixo, ou título centralizado sobre três cards, é o template qualquer que seja o mundo que o pinte. `[IMP]` mode-persuade, "Comps". Cada esboço é entregue como HTML da primeira dobra (o esqueleto do Anexo A com só a S01, renderizado nos dois viewports e capturado), com uma linha dizendo o que lidera e por quê.

**Teste da memória antes de enviar:** se o visitante saísse depois de uma tela, o que descreveria uma hora depois? Se a resposta honesta é um clima, o conceito ainda não se comprometeu; refazer o esboço. `[IMP]` new-work, "memory test".

**Saída obrigatória:** tipo, justificativa, blueprint, mapa de conexão com ritmo, e o esboço de primeira dobra travado registrados em `docs/01_ficha.md`; os três esboços guardados em `docs/esbocos/` com as capturas.

**Gate 3:** tipo coerente com temperatura e com o canal; mapa de conexão sem "não"; primeira dobra travada pelo Sarden (ou delegada por escrito) e cumprindo as invariantes nos dois viewports. Pedido maior que a temperatura (demo para tráfego frio de Meta, por exemplo) é devolvido para a fase 1.

---

## FASE 4 | COPY (os três leitores)

A página é organizada pelo usuário, não pelo produto. Escrever na ordem dos leitores. A copy nasce em `docs/02_copy.md` e entra no HTML sem alteração. Mudança feita no HTML volta para o `02_copy.md` no mesmo commit: um texto, uma fonte.

### 4.1 Hero (leitor 1, o apressado, 0 a 3 segundos)

- **Headline.** Até 8 palavras. Searcher: promessa do anúncio quase literal (message match). Scroller: Big Idea ou premissa, não promessa. Checar os 10 elementos `[K]` DNA Sarden: clareza, relevância, curiosidade, benefício, urgência quando cabe, emoção, originalidade, ação, fator uau, não óbvio. Escrever 5 variantes e escolher 1; guardar as outras para teste.
- **Sub.** Mecanismo em uma frase + para quem + prazo. É onde a especificidade mora. "Para quem" vive aqui, não em um pré-título acima do H1.
- **Prova imediata.** Um número específico (clientes, cidades, anos, nota com quantidade de avaliações) ou logos autorizados. Sem prova real confirmada pelo cliente, o agente pergunta antes de escrever o bloco; nunca prova genérica, nunca bloco com lacuna.
- **CTA.** Primeira pessoa com deliverable: "Quero meu diagnóstico", "Agendar minha análise", "Falar no WhatsApp". Nunca "Enviar", "Saiba mais", "Entre em contato". `[V]` LanderLab: CTA em primeira pessoa, +14% direcional.
- **Microcopy sob o CTA.** Uma linha que reduz o custo do clique: tempo ("leva 1 minuto"), ausência de compromisso, o que acontece depois.
- **Campo.** Um campo ou um botão. O formulário completo fica para o corpo ou para o multi-step.
- A hero nunca explica. Explicação é trabalho do corpo.

### 4.2 Corpo de confirmação (leitor 2)

- **Você está aqui:** 3 a 4 sintomas que o ICP reconhece, no registro da pergunta mental dele ("faz sentido no meu cenário?"), não no estágio do CRM. `[K]` G4.
- **Mecanismo em 3 passos:** o objetivo de cada etapa, não a metodologia inteira. `[K]` LightCopy.
- **Prova:** 1 a 2 casos específicos com nome, cargo, empresa, antes e depois. Prova (caso) é diferente de prova social (volume); usar os dois, separados. `[K]` Érico Rocha via LightCopy.
- **Provar, não afirmar:** mostrar o assunto fazendo o trabalho dele (a tela em funcionamento, o mecanismo dramatizado, o específico que um concorrente não copia). Material de demonstração é autorado em fidelidade total e rotulado "exemplo ilustrativo"; afirmação comercial continua ininventável. `[IMP]` new-work, "Prove, don't claim".
- **CTA repetido** com o mesmo texto.

### 4.3 Corpo de convencimento (leitor 3)

- **Objeções:** atacar a principal antes do CTA final. Mapear com as 3 crenças falsas `[K]` Expert Secrets: veículo ("não funciona no meu setor"), interna ("meu time não executa"), externa ("não tenho tempo ou orçamento agora"). Cada uma com uma prova própria.
- **Para quem é / para quem não é:** qualificação visível repele quem não é ICP.
- **FAQ:** 5 a 8 perguntas reais (prazo, integração, equipe, preço em faixa, fidelidade, documentos).
- **Garantia, planos, stack de oferta** quando o tipo pede (sales page). Stack: cada item com valor, depois tudo empilhado antes do preço. `[K]` Expert Secrets.
- **CTA final** + o que acontece depois do clique (SLA).

### 4.4 Copy de interface (labels, botões, erros, estados)

Adaptado de `[IMP]` clarify:
- Botão nomeia o que vai acontecer, não o gesto: o texto do CTA é a ação com o deliverable; "Enviando..." nomeia a operação real.
- Label persistente acima do campo; placeholder é exemplo, nunca label. Requisito de formato antes do envio (exemplo: "(DD) 9XXXX-XXXX").
- Erro responde três coisas: o que falhou, por quê quando se sabe, como corrigir. Sem culpar o usuário, sem código interno.
- Falha de envio nomeia a alternativa real (WhatsApp, telefone) em vez de "tente novamente mais tarde".
- Sucesso confirma o resultado e o próximo passo (thank-you com SLA). "Em breve" não existe.
- Mesmo substantivo e mesmo verbo para o mesmo conceito em toda a página; sem variação literária em interface.
- Alt de imagem carrega a informação da imagem; decorativa recebe `alt=""`.

### 4.5 Revisão Light Copy (antes de entregar)

Checklist `[K]` LightCopy:
- [ ] Parece conversa, não anúncio?
- [ ] As premissas são incontestáveis, despretensiosas e simples? (P1 + P2 + P3 = conclusão)
- [ ] Indícios de copy fraca removidos: início técnico, início no imperativo, início prometendo, pretensão, venda perceptível nos 3 primeiros segundos
- [ ] Pelo menos um elemento literário (história, super sincero, metáfora, setup + punch)
- [ ] Nível de leitura simples; frases de até 20 palavras; zero jargão desnecessário. `[P]` Unbounce CBR 2024: copy em nível de 5ª a 7ª série converte 11,1% contra 5,3% em nível profissional
- [ ] Sem "custaria" no lugar de "custa"; sem bônus de enchimento; sem escassez falsa
- [ ] Sem travessão em todo o texto

**Saída obrigatória:** `docs/02_copy.md`, bloco a bloco, com rótulo de leitor e de seção (template no Anexo D.3), incluindo `<title>`, meta description, alt das imagens, labels, mensagens de erro e de falha.

**Gate 4:** headline casa com o anúncio ou com a Big Idea; toda prova confirmada pelo cliente com fonte; CTA único em primeira pessoa; copy de interface completa; revisão Light Copy completa.

---

## FASE 5 | CONSTRUÇÃO DO HTML (compromisso total)

O agente parte do esqueleto do Anexo A. O esqueleto fixa a **mecânica de conversão** (seções, CTA, barra fixa, formulário, tracking, performance). O **mundo visual** (fase 2) e a **primeira dobra travada** (fase 3) substituem o layout neutro dele: entregar o hero do esqueleto como está é entregar o template da categoria. Antes de editar qualquer UI, reler o piso de craft (5.12): ele é a lista de verificação do build, não de planejamento. `[IMP]` skill-craft-floor-load.

### 5.1 Arquitetura do arquivo `index.html`

| Bloco | Conteúdo | Regra |
|---|---|---|
| `<head>` | charset, viewport, `<title>`, description, robots, canonical, Open Graph, favicon, preload da imagem LCP, preload das fontes, inicialização do `dataLayer`, snippet do GTM, CSS inline | `dataLayer` inicializado antes do GTM `[K]` KB GTM. CSS inteiro inline: zero arquivo CSS externo. |
| `<header class="topo">` | logo (sem link de saída) e, só no desktop, o CTA | header fixo no desktop; no mobile mostra só o logo |
| `<main>` | seções `S01` a `S08` na ordem do blueprint, cada uma `<section id="sNN" data-secao="SNN">` | nenhuma seção fora do blueprint sem justificativa na ficha; nenhum comentário de estratégia (regra 14) |
| `<div id="cta-fixa">` | barra fixa de CTA para mobile | regras na 5.4 |
| `<footer>` | logo pequeno, razão social, link da política de privacidade | nada mais |
| `<script>` final | captura de UTM, barra fixa, eventos de etapa, validação e envio do formulário | tudo em um bloco, sem biblioteca; menos de 20 KB |

Um arquivo HTML. CSS e JS inline. Imagens, fontes, logo e favicon em `assets/`. Nenhum outro arquivo.

### 5.2 Compromisso com a direção

- Construir a direção travada, não uma leitura mais segura dela. A forma fornece estrutura, ordem de leitura, convenções de componente e movimento; o produto fornece todo fato. `[IMP]` skill-commit-every-atom.
- Cada átomo no vocabulário do mundo: botão, campo, link, lista, separador, foco. Um componente de estoque dentro de uma forma comprometida é lapso. O esqueleto é ponto de partida, não aparência final.
- Quando o mundo nomeia uma técnica (canvas, view transitions, movimento generativo), construir a técnica, não uma imitação estática dela, dentro do orçamento da 5.7. `[IMP]` new-work, "Build the form's web leverage".
- Autorar os assets, nunca substituir por chrome: gradiente, vidro, ícone genérico em azulejo e polígono de `clip-path` onde caberia um asset real são a lacuna vestida de chrome. `[IMP]` skill-author-assets-not-chrome.
- Em trabalho não assistido, a versão segura é o risco conhecido: o agente entrega a comprometida e deixa a crítica para a revisão de acabamento.

### 5.3 Primeira dobra (S01) em HTML

- Único `<h1>` da página. Até 8 palavras. É o candidato a elemento LCP junto com a mídia; os dois precisam estar no HTML inicial, nunca injetados por JS.
- Ordem no DOM, igual nos dois dispositivos: `<h1>` → sub → prova imediata → CTA → microcopy → mídia ou demonstração. No mobile a mídia fica abaixo do CTA; nunca acima. Nada acima do H1.
- Composição = o esboço travado na fase 3. O `.hero__grid` do esqueleto é só o contêiner; a topologia (assimétrica, tipográfica, produto em funcionamento, objeto do mundo) vem do esboço.
- Teste da primeira tela: em 360×640 (Chrome DevTools, sem barra de endereço) e em 1440×900, headline, prova e CTA aparecem sem rolar. Se a mídia empurra o CTA para fora no mobile, a mídia sai do mobile (usar `<picture>` com fonte grande só a partir de 1024 px e versão pequena abaixo do CTA no mobile, como no esqueleto).
- Direção mobile (ficha, campo 5): uma coluna; CTA como botão de largura total que leva ao formulário (`href="#form-lead"`) e foca o primeiro campo; formulário na seção final.
- Direção desktop: a partir de 1024 px, o **formulário entra na primeira dobra** (mover o `<form id="form-lead">` para dentro de `.hero__midia`, mantendo o id); no mobile o mesmo formulário continua abaixo do texto, em uma coluna. Header com CTA fixo.
- Mídia da primeira dobra: foto real do time, do produto ou do entregável, ou a demonstração do mecanismo (a tela real, rotulada "exemplo ilustrativo" se os dados forem de demonstração). Tamanho máximo 150 KB na versão grande e 40 KB na pequena, WebP ou AVIF, com `width` e `height` declarados e `fetchpriority="high"`. Máscara geométrica (círculo, polígono, recorte radial) fingindo contorno de foto não entra; recorte vem da própria imagem (PNG com alfa). `[IMP]` skill-ban-geometric-occlusion-mask.
- Nada de vídeo de fundo, slider ou animação de entrada no hero.

### 5.4 CTA em HTML

- Um texto de CTA para a página inteira, definido em `02_copy.md`. Hero, barra fixa, header, meio e final usam a mesma string.
- Botão de conversão: `<a class="btn btn--cta" href="#form-lead">` quando leva ao formulário; `<button type="submit" class="btn btn--cta">` dentro do formulário; `<a class="btn btn--cta" href="https://wa.me/...">` quando o CTA é WhatsApp (fase 6.6).
- Altura mínima 56 px no mobile e nunca abaixo de 48 px; largura total no mobile; alvo de toque de pelo menos 44×44 px `[P]` Apple HIG e WCAG 2.2 SC 2.5.5; o mínimo legal de 24×24 px `[P]` WCAG 2.2 SC 2.5.8 nunca é a referência desta página.
- Contraste do texto do botão sobre o botão: mínimo 4,5:1 `[P]` WCAG 2.2 SC 1.4.3. Estado de foco visível (`:focus-visible` com contorno de 3 px na cor do mundo). Estado desabilitado só durante o envio, com texto "Enviando...". Hover muda algo (brilho, deslocamento de 1 px, sombra), nunca nada.
- Redesenhar o botão no vocabulário do mundo (forma, tipografia, relevo, movimento de hover), mantendo as medidas acima. Pílula só em controle pequeno. `[IMP]` skill-ban-codex-over-round.
- **Barra fixa no mobile (`#cta-fixa`):** fixa no rodapé do viewport, altura de até 72 px incluindo `env(safe-area-inset-bottom)`, com o mesmo CTA. Aparece quando nenhum botão de CTA da página está na tela e some quando qualquer um deles (hero, meio, formulário) está visível, ou quando o formulário entra na tela (IntersectionObserver), para nunca duplicar o CTA nem cobrir um campo. Resultado: um CTA visível em qualquer ponto da rolagem, nunca dois. `[V]` LanderLab: barra fixa no mobile, +14% direcional. O `body` recebe `padding-bottom` igual à altura da barra para o conteúdo final não ficar escondido.
- **Desktop:** CTA no header fixo quando a página passa de duas rolagens; repetição do CTA depois da prova (S04) e no final (S08). Sem barra fixa.
- Clique no CTA que leva ao formulário dispara `cta_click` (evento de etapa). Nunca é conversão.

### 5.5 Seções de confirmação e convencimento (S02 a S07)

| Seção | Markup | Regras |
|---|---|---|
| S02 Você está aqui | `<h2>` + `<ul class="lista-check">` com 3 a 4 itens, ícone em SVG por máscara | frase na primeira pessoa do leitor; fecha com CTA repetido só em página longa |
| S03 Mecanismo em 3 passos | `<ol class="passos">` com `<h3>` por passo e uma linha de objetivo; o número entra porque a sequência carrega informação | sem metodologia completa; sem mais de 3 passos `[IMP]` skill-ban-numbered-section-markers (exceção justificada) |
| S04 Prova | campo de cor em escala de página (`.campo-cor`), número grande em numerais tabulares, `<blockquote>` e `<figcaption>` (nome, cargo, empresa, foto real); bloco separado de prova social (logos em SVG ou número) | sem cartão, sem borda lateral colorida, sem cartão dentro de cartão `[IMP]` skill-ban-side-stripe-borders, skill-layout-cards-lazy; CTA repetido depois da prova |
| S05 Objeções | 3 blocos `<article>`: objeção em `<h3>` na voz do leitor, resposta, prova própria | veículo, interna, externa `[K]` Expert Secrets |
| S06 Para quem é / não é | duas listas lado a lado no desktop, empilhadas no mobile | repele quem não é ICP sem ironia |
| S07 FAQ | `<details><summary>` nativo, 5 a 8 itens, seta em SVG por máscara | zero JS para abrir; `summary` com altura mínima de 48 px; abertura dispara `faq_open` (etapa, opcional) |
| S08 CTA final + formulário | `<h2>` com o resultado, `<form id="form-lead">`, linha de SLA ("o que acontece depois do clique") | regras do formulário na fase 6; é o fechamento real da página |

Nenhuma fileira de cards iguais (ícone + título + texto) como estrutura de página; nenhum "benefício" em três colunas genéricas; nenhum ícone decorativo sem função; nenhum template de métrica-herói (número grande, rótulo pequeno, estatísticas de apoio) fora da prova real. Cada bloco responde a uma pergunta real do leitor 2 ou 3 levantada na fase 0. `[IMP]` skill-ban-identical-card-grids, skill-ban-hero-metric, skill-reflex-decorative-chrome.

### 5.6 Imagens e mídia

- Formato WebP ou AVIF para fotos; SVG para logos e ícones. JPG só quando o cliente não autoriza conversão.
- Todo `<img>` com `width` e `height` reais (evita CLS), `alt` descritivo (do `02_copy.md`) e `decoding="async"`. Abaixo da dobra: `loading="lazy"`. Primeira dobra: `fetchpriority="high"`, sem lazy.
- Peso: primeira dobra até 150 KB; demais fotos até 120 KB; logos de prova em SVG ou PNG até 15 KB cada; total de imagens no primeiro carregamento até 600 KB.
- Texto nunca dentro de imagem. Mockup do entregável é a exceção, com o mesmo texto em `alt`.
- Ilustração real ou nenhuma: SVG imitando desenho (cenas "sketch", grão com `feTurbulence`) lê como amador; SVG fazendo geometria (formas, diagramas, linhas animadas) é mídia de primeira classe. `[IMP]` skill-ban-codex-sketchy-svg.
- Fundos são superfícies: listras com `repeating-linear-gradient` e grades sobrepostas só quando há um canvas, mapa ou instrumento real por baixo. `[IMP]` skill-ban-codex-stripes, skill-ban-codex-grid-backgrounds.
- Vídeo: só quando o tipo pede (VSL, webinar). Nunca `autoplay` com som; nunca iframe no carregamento inicial. Usar fachada: poster (imagem) com botão, e o iframe entra só no clique. Vídeo vertical quando a direção é mobile.
- Carrossel, slider e galeria: não entram.

### 5.7 Orçamento de performance

| Item | Limite | Por quê |
|---|---|---|
| `index.html` com CSS inline | até 80 KB | uma requisição, LCP rápido |
| JS próprio | até 20 KB | sem biblioteca; só UTM, barra, eventos, formulário, e o movimento autoral quando houver |
| Fontes | até 2 arquivos woff2, até 100 KB no total, `font-display: swap`, preload, auto-hospedadas | fonte bloqueando render derruba LCP |
| Imagens no primeiro carregamento | até 600 KB | regras da 5.6 |
| Scripts de terceiro | só o GTM | pixels e conversões dentro do container |
| Efeitos caros (blur, backdrop-filter, sombra animada, canvas) | limitados a uma região, só durante a animação, `will-change` só no momento | INP e quadros perdidos no mobile `[IMP]` animate |
| LCP | até 2,5 s (meta interna 1,5 s no mobile) | `[P]` Core Web Vitals, web.dev |
| INP | até 200 ms | `[P]` Core Web Vitals, web.dev |
| CLS | até 0,1 | `[P]` Core Web Vitals, web.dev |
| PageSpeed Insights mobile | performance 90 ou mais antes da entrega | `[I]` caso interno: levar a performance mobile de abaixo de 40 para acima de 90 derrubou o custo por formulário |

`[P]` Google/Deloitte, Milliseconds Make Millions (2020): 0,1 s a menos no mobile aumentou 21,6% a progressão para a página de envio de formulário em sites de lead gen.

Medir com PageSpeed Insights (mobile) na URL de staging. Resultado registrado em `docs/04_qa.md` com data.

### 5.8 Acessibilidade mínima (que também é conversão)

- `<html lang="pt-BR">`. Um `<h1>`; `<h2>` por seção; `<h3>` dentro delas; sem pular níveis.
- Todo campo com `<label for>` visível. Erro de campo em texto, ligado ao campo por `aria-describedby`, nunca só por cor.
- Contraste 4,5:1 em texto e 3:1 em componentes de interface `[P]` WCAG 2.2 SC 1.4.3 e 1.4.11.
- Foco visível em links, botões e campos, desenhado na cor do mundo. Ordem de tabulação igual à ordem visual.
- `alt` em toda imagem com conteúdo; `alt=""` em imagem decorativa.
- `prefers-reduced-motion` respeitado com alternativa intencional: menos movimento e mais suave, não um "mata tudo em 0,01 ms" que destrói o feedback útil. `[IMP]` audit, motion sensitivity.
- Fonte base 16 px no mobile e campos com fonte de 16 px ou mais: o Safari do iOS dá zoom automático em campo com fonte menor que 16 px, e o zoom quebra o preenchimento.

### 5.9 `<head>`: meta, SEO mínimo e compartilhamento

- `<title>`: headline + marca, até 60 caracteres. `meta description`: a sub, até 155 caracteres. Os dois vêm do `02_copy.md`.
- `meta robots`: conforme a ficha (campo 16). Página só de campanha costuma ser `noindex, follow`; a decisão é do Sarden, não do agente.
- `<link rel="canonical">` com a URL final sem parâmetros.
- Open Graph completo (`og:title`, `og:description`, `og:image` 1200×630 até 300 KB, `og:url`, `og:type`). É o que o WhatsApp, o LinkedIn e a Meta mostram na pré-visualização do link; em disparo de WhatsApp a pré-visualização é a primeira dobra da campanha.
- Favicon em SVG (fallback PNG 32×32 se o destino exigir).
- Preload da imagem LCP e das fontes; `preconnect` só para domínio de fonte externa, se houver (não deveria haver: fontes auto-hospedadas).

### 5.10 O que não entra na página

Menu de navegação; links para o site, blog ou redes sociais; pop-up de entrada ou de saída; chat widget que cobre o CTA ou a barra fixa; carrossel; vídeo com autoplay; animação de entrada repetida em cada seção; texto em imagem; contador falso; selo sem registro verificável; kicker ou pré-título acima de título; texto em gradiente; vidro e desfoque como decoração; borda lateral colorida acima de 1 px em cartão, item de lista, callout ou alerta; sombra dura deslocada fora de mundo neobrutalista; mono como fantasia de "técnico" (mono é para código, dado e medida); glifo ou emoji no lugar de ícone; "lorem ipsum", "em breve", placeholder de qualquer tipo; campo de formulário sem justificativa de roteamento; link `href="#"` vazio; biblioteca de terceiros além do GTM. `[IMP]` craft-floor, "Refuse".

### 5.11 CSS mobile-first, tipografia e ritmo

- Base escrita para 360 px. Breakpoints: `min-width: 768px` (tablet, botões com largura automática, listas em duas colunas) e `min-width: 1024px` (desktop, primeira dobra em grid, header com CTA, barra fixa oculta).
- Largura máxima do conteúdo: `--largura-max` (1120 px). Gutter lateral de 20 px no mobile.
- Tipografia: 16 px base no mobile, 18 px no desktop; `line-height` 1,5 no texto e 1,1 a 1,2 nos títulos; H1 com `clamp()` entre 1,875 rem e 2,75 rem (display nunca acima de 6 rem); tracking de título entre -0,02 e -0,03 em, nunca abaixo de -0,04 em; `text-wrap: balance` nos títulos; medida de texto corrido entre 65 e 75 caracteres (`max-width: 65ch`). Passos de escala e peso óbvios entre os papéis (título, sub, texto, rótulo). `[IMP]` skill-typo-floor, skill-typo-codex-tracking-repeat.
- Texto claro sobre fundo escuro compensa nos três eixos: um pouco mais de entrelinha, um toque de tracking, um passo de peso quando a fonte pede. `[IMP]` typeset.
- Ritmo: grupos apertados, separações generosas, mais espaço acima de um título do que abaixo. Escala de espaçamento documentada (base 4, passos 8, 12, 16, 24, 32, 48, 64, 96), nunca valores soltos. Variar a densidade entre seções: a prova é o pico, o FAQ é quieto, o fechamento é denso de novo. Uma passagem densa ganha uma quieta. `[IMP]` skill-layout-spacing-rhythm.
- Superfícies do navegador também carregam o design: `::selection`, `caret-color`, `accent-color`, anel de foco, `text-underline-offset`, numerais tabulares nos números de prova, `scrollbar-color`. É o sinal mais barato de que a página foi construída, não montada. `[IMP]` skill-craft-browser-surfaces.
- Sem `position: fixed` além da barra de CTA e do header no desktop. Sem `100vh` na primeira dobra (a barra de endereço do mobile muda a altura e empurra o CTA).

### 5.12 Piso de craft (verificar no render, em lote)

Checar tudo em uma mesma olhada no render, corrigir o que ela mostra e só então olhar de novo; não tirar print a cada ajuste. `[IMP]` craft-floor, "Verify".

- **Contraste:** texto e placeholder 4,5:1 ou mais; texto grande 3:1. Sobre superfície colorida, o texto secundário se tinge do matiz, nunca cinza.
- **Profundidade:** sombra com deslocamento e desfoque suave; halo colorido sem deslocamento é decoração.
- **Espaço:** grupos apertados, separações generosas, mais espaço acima do título do que abaixo. Ler os valores computados.
- **Tipo:** medida 65 a 75ch, display até 6 rem, tracking até -0,04 em, títulos balanceados, passos de escala e peso óbvios. Rodar a copy real em cada breakpoint e corrigir o que transborda.
- **Movimento:** um momento autoral, não efeitos espalhados nem a mesma entrada em toda seção. Saída exponencial (`cubic-bezier(0.16, 1, 0.3, 1)`) partindo de um estado já visível; nunca bounce ou elástico. Blur, backdrop-filter, clip-path, máscara e sombra pertencem à paleta quando ficam suaves. Conteúdo visível por padrão: script que falha não esconde a página.
- **Estados:** hover, foco, desabilitado, carregando, erro, sucesso. Conteúdo real, controles funcionando, composição responsiva, foco por teclado.
- **Superfícies do navegador** tematizadas (5.11).
- **Copy:** a linguagem do produto; controles nomeiam a ação; erros nomeiam o problema e a recuperação.
- **Cobertura:** todo requisito do brief presente e encontrável em segundos.

Com tudo verde, gastar a página no mundo comprometido; na dúvida entre refinado e comprometido, comprometer. `[IMP]` skill-floor-not-ceiling.

**Saída obrigatória:** `index.html` completo, com tokens, copy, assets, scripts e o mundo aplicado em cada átomo, abrindo sem erro de console no Chrome.

**Gate 5:** teste da primeira tela aprovado em 360×640 e 1440×900; CTA visível em qualquer ponto da rolagem nos dois dispositivos; nenhum `{{` no arquivo; nenhum comentário de estratégia no HTML; piso de craft verificado em lote; PageSpeed Insights mobile medido.

---

## FASE 6 | FORMULÁRIO E MECANISMO DE CONVERSÃO (HTML)

**Regra central:** campos = o mínimo para rotear o lead. Qualificação acontece no multi-step, no bot ou na call.

### 6.1 Tabela de decisão por campo (preencher para cada campo proposto)

| Campo | Necessário para rotear? | Necessário para o próximo passo humano? | Impacto esperado | Decisão |
|---|---|---|---|---|
| E-mail | ... | ... | ... | fica / sai / vai para o step 2 |
| Telefone ou WhatsApp | ... | ... | ... | ... |

Referências `[P]`: formulário de 1 campo converte 18,2%, 2 campos 13,0%, 3 campos 11,5%; as maiores perdas vêm depois dos dois primeiros (Neil Patel, 404 LPs). Textareas e dropdowns múltiplos derrubam mais que campos de texto simples (HubSpot, 40 mil LPs). Entre 4 e 6 campos está o equilíbrio; aos 7 a conversão cai para 8,6% (Neil Patel, 833 LPs).

### 6.2 Regras de campos

- Telefone ou WhatsApp obrigatório quando o próximo passo é humano (SDR). Em topo de funil, tire.
- Multi-step quando precisar de 5 ou mais dados: começar pela pergunta de menor compromisso relevante para qualificar, nunca pedir contato no primeiro step, 2 ou 3 campos por step, indicador de progresso em texto, último step como continuação lógica. `[V]` LanderLab.
- Enriquecimento no lugar de campo quando a stack permite (form shortening no HubSpot). `[K]` dossiê HubSpot.
- Captcha visível custa conversão. Usar honeypot (campo invisível que humano não preenche) e, se o destino exigir captcha, a versão invisível.
- Mobile: uma coluna, autofill ativado, teclado certo para cada campo, multi-step no mobile mesmo quando single-step no desktop.

### 6.3 Markup do formulário

| Campo | Atributos obrigatórios | Por quê |
|---|---|---|
| Nome | `type="text" autocomplete="name" required` | autofill do navegador |
| E-mail | `type="email" inputmode="email" autocomplete="email" required` | teclado com @ e validação nativa |
| Telefone ou WhatsApp | `type="tel" inputmode="tel" autocomplete="tel" required` + máscara leve `(DD) 9XXXX-XXXX` | teclado numérico; o CRM recebe só dígitos com DDI |
| Empresa | `type="text" autocomplete="organization"` | autofill |
| Campo de seleção (faixa, porte) | `<select>` com até 6 opções e a primeira instruindo ("Selecione") | dropdown múltiplo derruba conversão |
| Campos ocultos | `utm_source, utm_medium, utm_campaign, utm_content, utm_term, gclid, fbclid, page_url, lp_versao` | origem chega ao CRM |
| Honeypot | `<input name="site_web" tabindex="-1" autocomplete="off">` dentro de `<div class="hp" aria-hidden="true">` | bot preenche, humano não vê; envio com valor é descartado em silêncio |
| LGPD | linha de aviso com link da política, ou checkbox obrigatório, conforme o jurídico do cliente (fase 0) | base legal do cliente, não do agente |
| Botão | `<button type="submit" class="btn btn--cta">` com o texto do CTA | único botão no formulário |

- `name` de cada campo = nome interno da propriedade no CRM (confirmado na fase 0). UTMs chegam em propriedades próprias do CRM; se não existem, o agente pede a criação na fase 0.
- Todo campo com `<label for>` visível acima; placeholder nunca substitui label.
- Validação inline: ao enviar, campos inválidos recebem `aria-invalid="true"`, mensagem em texto logo abaixo e o foco vai para o primeiro erro. Nunca `alert()`.
- Envio: botão desabilitado com "Enviando..." durante a requisição; sucesso → redirecionar para `obrigado.html`; falha → mensagem com o caminho alternativo (link do WhatsApp ou e-mail) e botão reativado.
- Campo, label, erro e botão redesenhados no vocabulário do mundo (fase 5.2); o formulário "de estoque" dentro de uma página comprometida é o lapso mais comum.
- Sem reCAPTCHA v2 (o de clique). Sem campo "como nos conheceu" (a UTM responde).

### 6.4 Mecanismo de envio (escolher um, conforme a ficha, campo 14)

| Destino | Como | Observação |
|---|---|---|
| HubSpot Forms API | `fetch` POST para `https://api.hsforms.com/submissions/v3/integration/submit/{portalId}/{formGuid}` com `fields[{objectTypeId:'0-1', name, value}]` e `context{hutk, pageUri, pageName}` | endpoint aceita requisição do navegador (CORS) `[P]` documentação HubSpot; `hutk` vem do cookie `hubspotutk` e liga o envio à sessão de tracking do HubSpot |
| Embed de formulário HubSpot | `hbspt.forms.create` dentro do `<div>` do formulário | adiciona JS de terceiro; aceito só quando o destino é HubSpot CMS; o push de `generate_lead` entra no callback `onFormSubmitted` |
| RD Station | embed oficial ou API de conversão | mesma regra de callback |
| Webhook (Make, n8n, Zapier, backend do cliente) | `fetch` POST JSON para a URL do webhook | o webhook grava no CRM; o agente confirma na fase 0 que o CRM recebe origem |
| Netlify Forms | `<form data-netlify="true" name="...">` | só quando o destino é Netlify; o lead ainda precisa chegar ao CRM por integração |
| E-mail apenas | não aceito | lead que não cai no CRM não é mensurável |

### 6.5 Multi-step em HTML

- Cada step é um `<fieldset data-step="N">` com `<legend>` visível; só o step atual está visível (`hidden` nos demais).
- Botão "Continuar" valida o step antes de avançar; o último step tem o botão com o texto do CTA.
- Indicador "Passo N de T" em texto, não só barra colorida.
- Evento `form_step` com o número do step em cada avanço (etapa, não conversão).
- Voltar é permitido sem perder dados.

### 6.6 Caminho WhatsApp (quando o CTA é WhatsApp)

- Link no formato oficial `https://wa.me/55DDDNUMERO?text=MENSAGEM` com o número em formato internacional sem símbolos e a mensagem codificada por URL `[P]` WhatsApp, "Como usar o clique para conversar".
- Mensagem pré-preenchida carrega a campanha em linguagem natural ("Olá! Vim pela página {nome} e quero {deliverable}."), para o atendente ou o bot identificarem a origem.
- `target="_blank"` e `rel="noopener"`; clique dispara `whatsapp_click` (etapa). A conversão é `whatsapp_conversation_started`, medida pelo webhook do bot ou pelo CRM, nunca pelo clique. `[I]` caso interno.
- Especificar: (a) mensagem pré-preenchida, (b) perguntas do bot de pré-qualificação, (c) campos que chegam no CRM, (d) SLA de resposta humana. Nunca comparar funil de WhatsApp com funil de formulário como se fossem o mesmo.
- Formulário e WhatsApp na mesma página só com medição separada e decisão registrada na ficha.

**Saída obrigatória:** formulário dentro de `index.html` conforme as regras acima; tabela de decisão por campo e mecanismo de envio registrados em `docs/01_ficha.md`.

**Gate 6:** nenhum campo sem justificativa de roteamento; envio de teste cai no CRM com UTM; erro inline funciona; honeypot não bloqueia humano.

---

## FASE 7 | TRACKING E MEDIÇÃO (no HTML e no GTM)

Tracking vem antes de tráfego. `[K]` KB Tracking Snippets Library, KB GTM MasterReference, KB Pixels, KB ServerSide.

### 7.1 No HTML

- `window.dataLayer = window.dataLayer || [];` e um push com os dados da página (`lp_nome`, `lp_tipo`, `lp_versao`, `lp_direcao`) **antes** do snippet do GTM, no `<head>`. `[K]` KB GTM: push depois do GTM perde dados no page view.
- Snippet do GTM no `<head>` e `<noscript>` logo após `<body>`.
- Nomes de evento em `snake_case`, sempre os mesmos; evento é case-sensitive no GTM. `[K]` KB GTM.
- Captura de UTM, `gclid` e `fbclid` na entrada, guardada em `sessionStorage` e escrita nos campos ocultos antes do envio (script do Anexo A).
- `event_id` único gerado no envio, guardado em `sessionStorage` e usado uma vez na thank-you para o push de `generate_lead`; o GTM usa o mesmo `event_id` no Pixel e na CAPI para deduplicar. `[K]` KB ServerSide.
- Nenhum ID de pixel, de GA4 ou de conversão do Google Ads escrito no HTML: tudo no container.

### 7.2 Especificação de eventos (tabela obrigatória)

| Evento | Gatilho real | Tipo | GA4 / GTM | Meta Pixel + CAPI | Google Ads | Campo no CRM |
|---|---|---|---|---|---|---|
| page_view | carregamento da LP | etapa | tag GA4 All Pages | PageView | n/a | n/a |
| cta_click | clique em qualquer botão de CTA que leva ao formulário | etapa | custom event com `cta_posicao` | n/a | n/a | n/a |
| form_start | primeiro campo focado | etapa | custom event | n/a | n/a | n/a |
| form_step | avanço de step no multi-step | etapa | custom event com `step` | n/a | n/a | n/a |
| whatsapp_click | clique no link wa.me | etapa | custom event | n/a | n/a | n/a |
| generate_lead | envio confirmado, disparado uma vez na thank-you com `event_id` | **conversão** | custom event → GA4 key event | Lead com `event_id` para dedup | conversão principal + Enhanced Conversions | origem, campanha, etapa |
| whatsapp_conversation_started | conversa iniciada (webhook do bot ou CRM) | **conversão** | custom event ou importação | Lead ou Contact | conversão | origem, campanha, etapa |
| schedule | agendamento confirmado | conversão secundária | custom event | Schedule | conversão secundária | etapa |

### 7.3 Regras

- Conversão dispara no envio confirmado (thank-you com `event_id`). Nunca no clique do botão. Acesso direto a `obrigado.html` sem `event_id` não dispara nada. `[I]` pixel 2,1x o CRM quando o evento disparou fora da submissão.
- Pixel e CAPI com deduplicação por `event_id`.
- Conversion Linker e Enhanced Conversions ativos no Google Ads.
- UTMs conforme o catálogo do projeto (`utm_source, utm_medium, utm_campaign, utm_content, utm_term`), em minúsculas, sem variações ("fb", "facebook" e "meta" não podem coexistir). `[K]` Guia de Web Analytics, KB GA4.
- Lead chega no CRM com origem, campanha, etapa e, no caso de WhatsApp, os dados do bot.
- Consent Mode respeitado quando o cliente usa banner de consentimento.

### 7.4 No GTM (lista do que o agente especifica em `docs/03_tracking.md`)

| Item | Tipo | Gatilho |
|---|---|---|
| Google Tag (GA4) | configuração | All Pages |
| GA4 event: cta_click, form_start, form_step, whatsapp_click, generate_lead, schedule | evento GA4 | Custom Event com o mesmo nome |
| Conversion Linker | Google Ads | All Pages |
| Google Ads Conversion (lead) | Google Ads | Custom Event `generate_lead` |
| Meta Pixel base | Custom HTML ou template | All Pages |
| Meta Lead com `event_id` | Custom HTML ou template | Custom Event `generate_lead`, variável DL `event_id` |
| Variáveis Data Layer: `event_id`, `lp_nome`, `lp_versao`, `cta_posicao`, `step` | variável | n/a |

### 7.5 QA de tracking (executar e registrar)

- [ ] UTMs corretos no URL de destino e nos campos ocultos (inspecionar antes de enviar)
- [ ] Tags disparam na LP (GTM Preview)
- [ ] `generate_lead` chega no GA4 (DebugView) só no envio real, uma vez
- [ ] Google Ads registra a conversão de teste
- [ ] Meta Pixel e CAPI registram e deduplicam (Pixel Helper + Events Manager, mesmo `event_id`)
- [ ] Lead de teste cai no CRM com origem e campanha
- [ ] Acesso direto a `obrigado.html` não gera conversão
- [ ] Mobile testado de ponta a ponta
- [ ] Valores de conversão corretos (quando houver)

**Saída obrigatória:** `docs/03_tracking.md` com a tabela de eventos, a lista do GTM, o catálogo de UTMs da página e o resultado do QA de tracking com evidência (print ou log).

**Gate 7:** todos os itens do QA de tracking com evidência. Sem evidência, a página não é entregue como pronta.

---

## FASE 8 | THANK-YOU PAGE (`obrigado.html`)

A thank-you é parte da conversão, não acessório. É onde a conversão é medida e onde o próximo degrau começa. É também o fechamento real da jornada: a página não esvai, ela termina em uma ação.

**Estrutura (esqueleto no Anexo B):**
1. Confirmação específica com SLA ("Recebemos. Um especialista te chama em até X horas").
2. O que acontece agora (timeline, canal, quem fala).
3. Próximo degrau imediato (agendar direto, baixar material, oferta de qualificação de comprador). `[K]` a buyer is a buyer, DotCom Secrets.
4. Contato direto para quem não quer esperar (WhatsApp, telefone).
5. Push de `generate_lead` com o `event_id` guardado no envio, uma vez, antes do GTM.

**Regras de HTML:** mesmos tokens e header (sem CTA); mesmo mundo visual, mesmo vocabulário de componentes; `meta robots` sempre `noindex, nofollow`; sem formulário; link do próximo degrau com `data-evento="next_step_click"`; prazos reais ("em 5 minutos", "em 24 horas úteis"), nunca "em breve".

**Saída obrigatória:** `obrigado.html`.

**Gate 8:** SLA definido com o responsável pelo atendimento; próximo degrau especificado; `generate_lead` dispara uma vez e só com `event_id`.

---

## FASE 9 | QA, DETECTOR E REVISÃO DE ACABAMENTO

Ordem fixa: detector → auditoria técnica → inspeção em lote → revisão de acabamento por agente separado → checklist de conversão. O resultado de cada etapa vai para `docs/04_qa.md` com evidência (print, JSON, link do PageSpeed).

### 9.1 Detector (mecânico, sem LLM)

```bash
npx impeccable detect index.html obrigado.html
npx impeccable detect --json index.html obrigado.html > docs/detector.json
npx impeccable detect https://URL-DE-STAGING/          # depois de publicar em staging: lê DOM renderizado e estilos computados
```

- Exit 0 = limpo; exit 2 = achados; exit 1 = alvo não escaneado. O build só avança com exit 0. `[IMP]` README, CLI.
- Famílias que o detector pega (59 regras): borda lateral colorida, gradiente roxo-azul e texto em gradiente, easing elástico, halo escuro, cinza sobre cor, fonte superusada, cartão dentro de cartão, linha longa demais, padding apertado, alvo de toque pequeno, título pulando nível, contraste baixo, imagem quebrada, entre outras.
- Exceção só com aprovação do Sarden, registrada no próprio arquivo: `<!-- impeccable-disable overused-font: fonte da marca, aprovada por Sarden em AAAA-MM-DD -->`. Nunca exceção silenciosa.
- Resultado limpo é evidência, não prova: o detector não enxerga hierarquia, ritmo nem composição. `[IMP]` README, "A clean detector run is evidence, not proof".

**Sem shell (agente sem terminal):** o checklist manual abaixo substitui o detector e a entrega declara "detector não rodou; checklist manual aplicado":
- [ ] nenhuma borda lateral colorida acima de 1 px em cartão, lista, callout ou alerta
- [ ] nenhum texto em gradiente; nenhum gradiente roxo-azul; nenhum halo colorido sem deslocamento
- [ ] nenhuma easing bounce ou elástica; nenhuma entrada repetida em toda seção
- [ ] nenhum cinza puro sobre superfície colorida; nenhum preto ou cinza puro no texto
- [ ] nenhuma fonte da lista de reflexo (fase 2.3) sem motivo registrado
- [ ] nenhum cartão dentro de cartão; nenhuma fileira de cards iguais como estrutura
- [ ] nenhum kicker acima de título; nenhum glifo ou emoji como ícone
- [ ] contraste 4,5:1 em todo texto, medido em ferramenta (não a olho)
- [ ] alvos de toque 44 px ou mais; títulos sem pular nível; nenhuma linha acima de 75 caracteres
- [ ] nenhuma imagem quebrada; todo `<img>` com `width`, `height` e `alt`

### 9.2 Auditoria técnica (5 dimensões, nota 0 a 4 cada)

Adaptada de `[IMP]` audit. O agente pontua e justifica cada dimensão em `04_qa.md`; nota mínima 3 em cada uma e 16/20 no total para entregar.

| Dimensão | O que checar | Nota 3 significa |
|---|---|---|
| Acessibilidade | contraste, reduced-motion com alternativa, labels e ARIA, foco e ordem de tab, semântica, alt, erros de formulário | WCAG AA quase todo atendido, lacunas menores |
| Performance | animação de propriedade de layout, blur ou sombra sem limite, imagem sem lazy, `will-change` solto, peso dentro do orçamento | otimizado, melhorias menores possíveis |
| Tematização | nenhuma cor fora dos tokens, nenhum valor solto, modo escuro composto (quando existe), tokens com nome de papel | tokens usados, raros valores soltos |
| Responsivo | nenhuma largura fixa, alvos 44 px, sem rolagem horizontal, texto escalável, breakpoints reais | responsivo, ajustes menores |
| Integridade da implementação | achados do detector verificados em contexto; a página seria trocável por uma de outro produto? | problemas isolados, sistema coerente e próprio |

Qualquer achado vira item P0 (bloqueia), P1 (corrigir antes de publicar), P2 (próxima rodada) ou P3 (se sobrar tempo). P0 e P1 abertos impedem a entrega.

### 9.3 Inspeção em lote (o agente construtor olha o render)

Uma rodada de capturas, no máximo duas, com correções em lote entre elas; não um print por ajuste. `[IMP]` new-work, seção 7.
- Capturar `docs/review/desktop.png` (1440 de largura, página inteira), `docs/review/mobile.png` (390 de largura, página inteira), `docs/review/primeira-dobra-360x640.png` e `docs/review/primeira-dobra-1440x900.png`, e `docs/review/obrigado-mobile.png`. Capturar a partir do topo do documento, com movimento de entrada já assentado; abrir cada arquivo e confirmar que mostra o que o nome diz (sem região preta, sem estado meio carregado). Captura inválida custa a rodada inteira. `[IMP]` skill-capture-validity.
- Dirigir cada interação e estado alcançável: barra fixa aparecendo e sumindo, FAQ aberto e fechado, foco por teclado em cada campo, erro de validação, botão em "Enviando...", falha de envio, conteúdo longo (headline de 8 palavras, nome de 40 caracteres), e checar sobreposição e corte em cada um.
- Criticar o render contra o contrato de direção (seis blocos) e as invariantes de conversão: um visitante de primeira vez sabe o que é, por que importa e o que fazer em segundos, no vocabulário da forma?
- Corrigir o material, recapturar, e parar: depois da segunda rodada o polimento do construtor acabou; o que sobrar vai para a revisão de acabamento, onde um contexto novo acha melhor e mais barato. `[IMP]` new-work, "After the second inspection round".

### 9.4 Revisão de acabamento por agente separado

A página não se avalia sozinha. Um agente revisor novo, sem o histórico da conversa do construtor, recebe o pacote e devolve um veredito. `[IMP]` skill-finish-separate-reviewer. Quando a plataforma não tem subagente, o próprio agente sai por completo do contexto de build (nova sessão) e declara a substituição na entrega.

**Pacote enviado ao revisor:** o pedido original e as respostas confirmadas; `01_ficha.md` (contrato de direção, mapa de conexão, invariantes); `02_copy.md`; `index.html` e `obrigado.html`; as capturas da 9.3; `detector.json`; o resultado da auditoria 9.2; o piso de craft (5.12) e a lista do que não entra (5.10); os esboços da fase 3 e o esboço travado.

**O que o revisor devolve (cinco seções, sempre):**
1. **Conversão:** teste dos 3 segundos na primeira dobra (o que é, para quem, o que fazer), CTA inconfundível em todo ponto da rolagem, message match com o anúncio ou a Big Idea, prova e prova social separadas, objeção principal antes do CTA final, formulário mínimo.
2. **Fidelidade ao contrato:** o render cumpre TESE, MUNDO PRÓPRIO, PRIMEIRA DOBRA e FORMA? O build é a direção travada ou uma versão mais segura dela? O teste da memória passa?
3. **Piso de craft:** cada item da 5.12 e da 5.10, com evidência por captura; achados do detector verificados em contexto; falsos positivos nomeados.
4. **Achados por severidade:** P0 a P3, cada um com local, impacto e correção.
5. **Disposição**, uma das quatro: **recapturar** (a evidência falhou, não o build: recapturar o que o revisor nomeia e rodar a revisão inteira de novo), **reconstruir** (a fidelidade falhou por inteiro: rederivar as regiões nomeadas e voltar para revisão completa, nunca para veredito parcial), **corrigir** (aplicar as correções materiais em um lote, reconstruir uma vez, recapturar os mesmos viewports e devolver ao mesmo revisor para um veredito que pontua cada correção como resolvida, parcial ou não resolvida), **entregar** (nada é devido). `[IMP]` skill-verdict-bounds-the-finish.

**Limites:** duas rodadas de correção é o orçamento; quando o segundo veredito ainda lista itens abertos, a tabela vai para o Sarden decidir entre entregar como está e financiar outra rodada. A lista do revisor é a única lista de trabalho; o construtor não reabre a própria caçada a defeitos nem roda um segundo detector. Veredito reportado com a palavra do revisor e no escopo real: "o revisor pontuou as três correções como resolvidas" é sustentável; "não restam problemas" não é. Evidência do Sarden contra um "entregar" (print dele, descompasso nomeado) reabre a revisão com um revisor novo. `[IMP]` skill-user-evidence-reopens-review.

### 9.5 Checklist de conversão (executar e registrar item a item)

**Objetivo e usuário**
- [ ] Conversão única escrita em uma linha e tipo definido (final ou de etapa)
- [ ] Se multi-step: cada step com uma única conversão, testado isoladamente
- [ ] Primeira dobra serve o leitor apressado: casa com o anúncio; headline, prova e CTA visíveis sem rolar em 360×640 e 1440×900
- [ ] Corpo serve os leitores 2 e 3 na ordem: confirmação antes de convencimento
- [ ] Ficha, contrato de direção e mapa de conexão preenchidos e anexados

**CTA**
- [ ] Um CTA, mesmo texto em toda a página, primeira pessoa com deliverable
- [ ] Visível em qualquer ponto de rolagem: barra fixa no mobile aparece e some na hora certa; header ou repetição no desktop
- [ ] Toda seção está no mapa de conexão e empurra para o CTA (mapa sem "não")
- [ ] Nenhum comentário de estratégia no HTML (buscar "leitor", "objetivo", "empurra" nos comentários)

**Dispositivo e layout**
- [ ] Testado em 360×640, 390×844, 768×1024, 1024×768 e 1440×900: sem rolagem horizontal, nada cortado, nada sobreposto
- [ ] Direção de dispositivo da v1 declarada com origem e refletida na posição do formulário
- [ ] V1 meio-termo: funciona por completo nos dois dispositivos
- [ ] Teste do polegar aprovado: abrir no celular, chegar ao CTA e concluir a ação em menos de 60 segundos sem zoom e sem erro de toque
- [ ] Data marcada para a análise de realidade

**Formulário**
- [ ] Teclado correto em cada campo no celular (e-mail, telefone)
- [ ] Autofill do navegador preenche nome, e-mail e telefone
- [ ] Erro inline aparece, com texto, e o foco vai para o primeiro erro
- [ ] Envio de teste chega ao CRM com UTM e origem
- [ ] Falha de envio mostra o caminho alternativo
- [ ] Honeypot invisível e sem efeito sobre humano

**Persuasão**
- [ ] Big Domino identificado; prova e prova social separadas
- [ ] Objeção principal atacada antes do CTA final
- [ ] Revisão Light Copy completa
- [ ] Nenhum número, depoimento, logo ou resultado sem confirmação do projeto; material de demonstração rotulado

**Craft**
- [ ] Teste de calibragem respondido: ninguém adivinharia o visual só pela categoria do cliente
- [ ] Teste da memória passa na primeira dobra
- [ ] Cor comprometida em escala de página (pelo menos um campo que possui uma região inteira), CTA como elemento de maior contraste em qualquer campo
- [ ] Ritmo da rolagem com pico e fechamento; densidade variando entre seções
- [ ] Um movimento autoral no máximo; nenhuma entrada repetida; reduced-motion com alternativa
- [ ] Superfícies do navegador tematizadas (seleção, caret, foco, sublinhado, numerais tabulares)
- [ ] Detector exit 0 (ou checklist manual declarado); auditoria 16/20 ou mais, sem P0 e P1; revisão de acabamento com disposição "entregar"

**Código e performance**
- [ ] HTML válido no validador do W3C, sem erro
- [ ] Zero erro no console do Chrome
- [ ] Nenhum `{{`, "lorem", "TODO", "xxx", "em breve" no HTML (buscar no arquivo)
- [ ] Sem link `href="#"`; todos os links abrem o destino certo; wa.me abre a conversa com a mensagem
- [ ] PageSpeed Insights mobile: performance 90 ou mais; LCP até 2,5 s; CLS até 0,1
- [ ] Pesos dentro do orçamento da 5.7
- [ ] Lighthouse acessibilidade 90 ou mais; contraste medido
- [ ] Pré-visualização do link (OG) testada: imagem, título e descrição corretos ao colar a URL no WhatsApp

**Medição**
- [ ] QA de tracking da fase 7 com evidência
- [ ] Thank-you com SLA, próximo degrau, `noindex` e conversão disparando uma vez

**Texto**
- [ ] Sem travessão
- [ ] Números em pt-BR
- [ ] Ortografia e concordância revisadas
- [ ] `<title>`, description e `alt` iguais ao `02_copy.md`
- [ ] Nenhum marcador de pendência, verificação ou inferência em nenhum arquivo do pacote; todas as perguntas respondidas e registradas no log

**Governança**
- [ ] Variante B (headline alternativa) construída antes de publicar a A
- [ ] Amostra mínima calculada e janela de teste definida
- [ ] Owner, naming e data de revisão registrados

**Saída obrigatória:** `docs/04_qa.md` com detector (JSON e exit), auditoria (tabela 5 × 0 a 4), capturas, veredito do revisor com as cinco seções, e o checklist item a item com evidência.

**Gate 9:** detector exit 0; auditoria sem P0 e P1; revisão de acabamento com disposição "entregar" (ou decisão do Sarden registrada após a segunda rodada); nenhum item do checklist em aberto. Item que depende do cliente volta como pergunta e a entrega espera a resposta.

---

## FASE 10 | ENTREGA (pacote publicável + DESIGN.md)

### 10.1 DESIGN.md do cliente (documentador)

Depois da última correção, o mundo construído é registrado em `docs/DESIGN.md` no formato oficial DESIGN.md (frontmatter YAML com tokens + até oito seções na ordem canônica: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts). Escrito a partir do build, nunca antes dele: um guia escrito antes é defendido contra a realidade em vez de descrevê-la. `[IMP]` skill-design-md-from-the-build, document. Template no Anexo D.8.

- Mundo novo (rodada 2 aconteceu): DESIGN.md completo, com tokens normativos e prosa de aplicação.
- Mundo herdado (design system ou site do cliente): DESIGN.md registra o incumbente como ele é, com as exceções desta página nomeadas; não "corrige" o sistema do cliente sem pedido.
- O DESIGN.md é entregue no pacote e salvo na pasta ou no knowledge do cliente: a próxima página desse cliente nasce como "mundo estabelecido" e pula a rodada 2. Uma página de mundo novo entregue sem DESIGN.md é um trabalho incompleto.

### 10.2 Pacote

O agente entrega uma pasta nomeada `AAAA-MM-DD_projeto_canal_tipo_vN` com esta estrutura:

```
AAAA-MM-DD_projeto_canal_tipo_vN/
├── index.html                      página completa (fases 2 a 7)
├── obrigado.html                   thank-you (fase 8)
├── assets/
│   ├── logo.svg, logo-escuro.svg, favicon.svg, og.jpg
│   ├── img/   (hero-1200.webp, hero-600.webp, fotos de prova, mockup, demonstração)
│   └── fonts/ (até 2 arquivos woff2, auto-hospedados)
└── docs/
    ├── README.md                   como publicar, configurar o GTM e testar depois de publicar
    ├── DESIGN.md                   o mundo visual registrado a partir do build (10.1)
    ├── 00_entendimento.md          fase 0
    ├── 01_ficha.md                 fases 1, 2, 3 e 6 (ficha, autoridade visual, contrato de direção, tokens, tipo, mapa de conexão, primeira dobra, campos)
    ├── 02_copy.md                  fase 4
    ├── 03_tracking.md              fase 7
    ├── 04_qa.md                    fase 9 (detector, auditoria, capturas, veredito, checklist)
    ├── 05_perguntas_respondidas.md log de perguntas feitas ao Sarden ou ao cliente, com resposta, quem respondeu, data e onde entrou
    ├── 06_plano_de_teste.md        variante B pronta, hipótese, métrica, amostra mínima, janela
    ├── detector.json               saída do detector
    ├── esbocos/                    os três esboços de primeira dobra e as capturas (fase 3)
    └── review/                     capturas da inspeção (9.3)
```

**Mensagem de entrega ao Sarden:** seis linhas no máximo: conversão da página, canal e direção de dispositivo, direção visual travada (ou mundo herdado) e exceções de marca aplicadas, o que foi confirmado com o cliente, veredito do revisor no escopo real, o que será testado primeiro e a data da análise de realidade.

**Gate 10:** todos os arquivos presentes; `index.html` e `obrigado.html` sem placeholder e sem comentário de estratégia; DESIGN.md presente; nenhum documento com marcador de pendência; README com os passos de publicação do destino escolhido.

---

## FASE 11 | PÓS-LANÇAMENTO (análise de realidade)

A página nasce como hipótese. A análise confirma ou inverte.

**Leituras obrigatórias:**

| Momento | O que ler | Decisão |
|---|---|---|
| Dia 1 | Tracking disparando? Pixel igual ao CRM? Leads chegando com origem? | Falha de tracking = pausa e corrige antes de qualquer leitura |
| Dia 7 | Sessões, conversões e taxa por dispositivo e por canal; CPL de plataforma contra CPL de CRM; Core Web Vitals de campo no Search Console ou no PageSpeed | Direção de dispositivo confirmada ou invertida; ficha atualizada |
| Dia 14 | Taxa da LP contra benchmark do tipo e contra histórico; qualidade no CRM (lead → MQL → SQL) | Abaixo do benchmark: aplicar a hierarquia de correção abaixo. Lead barato e ruim = problema de oferta ou de canal, não de LP |
| Semanal | Entrada na WBR com status No Ritmo, Sinal de Alerta ou Fora de Rota | Teste em andamento registrado com hipótese e amostra |

**Hierarquia de correção (ordem):** tracking → message match → primeira dobra → corpo → formulário e CTA → mobile e velocidade → thank-you → teste.

**Ordem de teste (impacto dividido por esforço):** headline → tamanho do formulário → copy do CTA → posição da prova → imagem ou demonstração da primeira dobra → tamanho da página. Uma variável por vez. Nunca KPIs de etapas diferentes na mesma análise. Só 1 em 8 testes dá significância; rodar continuamente. `[K]` GTM EST · `[V]` LanderLab.

**Variantes com o kit:** quando o agente roda com o Impeccable instalado e um servidor local, `/impeccable generate 3 variantes "headline do hero"` ou `/impeccable live` produzem variantes de um elemento nomeado para escolha no navegador; a variante escolhida vira a B do plano de teste. Comandos de refino por achado: `typeset` (hierarquia tipográfica), `layout` (ritmo e agrupamento), `colorize` (cor sem papel), `clarify` (copy de interface), `adapt` (dispositivo), `optimize` (performance), `bolder` (seção que lê plana, sem reescrever o resto), `quieter` (seção que grita), `animate` (um momento autoral), `polish` (passada final). Cada um termina em `polish` e no detector. Anexo G.2.

**Versões:** toda alteração no HTML gera `v{N+1}` com changelog no README (o que mudou, por quê, data). `lp_versao` no `dataLayer` e no campo oculto acompanha a versão. Mudança de token ou de componente atualiza o DESIGN.md.

**Saída obrigatória:** `docs/07_analise_de_realidade.md` nos dias 7 e 14, com números, fonte, decisão e ficha atualizada.

---

## ANEXO A | ESQUELETO `index.html` (lead gen com formulário)

O esqueleto fixa a **mecânica de conversão**: ordem de seções, CTA e barra fixa, formulário com validação e envio, captura de origem, eventos, orçamento de performance, superfícies do navegador. Ele **não** é a aparência final: o mundo visual (fase 2) redesenha cada átomo e a primeira dobra travada (fase 3) substitui a composição neutra da S01. Para outros blueprints, manter `<head>`, header, barra fixa, rodapé e scripts; trocar as seções de `<main>` pela ordem do Anexo C. Tudo entre `{{` e `}}` é substituído na fase correspondente; nada disso chega à entrega. O esqueleto passa limpo no detector (`npx impeccable detect`) com tokens de contraste válido; manter assim depois de aplicar o mundo.

```html
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{HEADLINE}} | {{MARCA}}</title>
<meta name="description" content="{{SUB}}">
<meta name="robots" content="{{ROBOTS}}">
<link rel="canonical" href="{{URL_FINAL}}">
<meta property="og:type" content="website">
<meta property="og:title" content="{{HEADLINE}}">
<meta property="og:description" content="{{SUB}}">
<meta property="og:image" content="{{URL_FINAL_BASE}}/assets/og.jpg">
<meta property="og:url" content="{{URL_FINAL}}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">

<!-- LCP: mídia da primeira dobra por dispositivo. Remover os dois preloads se a S01 não tiver imagem. -->
<link rel="preload" as="image" href="assets/img/hero-1200.webp" media="(min-width: 1024px)" fetchpriority="high">
<link rel="preload" as="image" href="assets/img/hero-600.webp" media="(max-width: 1023px)" fetchpriority="high">
<!-- Fontes auto-hospedadas: no máximo 2 arquivos. Remover preload e @font-face quando o design system define fonte do sistema. -->
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/{{ARQUIVO_FONTE_TITULO}}.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/{{ARQUIVO_FONTE_TEXTO}}.woff2" crossorigin>

<!-- dataLayer ANTES do GTM (fase 7.1) -->
<script>
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    lp_nome: '{{LP_NOME}}',
    lp_tipo: '{{LP_TIPO}}',
    lp_versao: '{{LP_VERSAO}}',
    lp_direcao: '{{DIRECAO_DISPOSITIVO}}'
  });
</script>
<!-- Google Tag Manager: único script de terceiro da página -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','{{GTM_ID}}');</script>
<!-- End Google Tag Manager -->

<style>
/* ===== 1. TOKENS (fase 2.5): valores do design system aprovado ou derivados da direção travada ===== */
:root{
  --cor-primaria:{{COR_PRIMARIA}};
  --cor-sobre-primaria:{{COR_SOBRE_PRIMARIA}};
  --cor-cta:{{COR_CTA}};
  --cor-cta-texto:{{COR_CTA_TEXTO}};
  --cor-fundo:{{COR_FUNDO}};
  --cor-superficie:{{COR_SUPERFICIE}};
  --cor-texto:{{COR_TEXTO}};
  --cor-texto-suave:{{COR_TEXTO_SUAVE}};
  --cor-borda:{{COR_BORDA}};
  --cor-erro:{{COR_ERRO}};
  --cor-sucesso:{{COR_SUCESSO}};
  --fonte-titulo:'{{FONTE_TITULO}}',system-ui,sans-serif;
  --fonte-texto:'{{FONTE_TEXTO}}',system-ui,sans-serif;
  --raio:{{RAIO}};
  --sombra:0 8px 24px -12px color-mix(in oklab, var(--cor-primaria) 45%, transparent);
  --largura-max:1120px;
  --altura-cta:56px;
  --altura-barra:72px;
  --suave:cubic-bezier(.16,1,.3,1);
  --icone-check:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'><path d='M4 12.5l5 5L20 6.5'/></svg>");
  --icone-seta:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'><path d='M6 9l6 6 6-6'/></svg>");
}
/* Sem design system (fase 2.5): neutros tingidos da primária, nunca preto ou cinza puros. Exemplo:
   --cor-texto:color-mix(in oklab, var(--cor-primaria) 15%, #141414);
   --cor-texto-suave:color-mix(in oklab, var(--cor-primaria) 25%, #4a4a4a);
   --cor-borda:color-mix(in oklab, var(--cor-primaria) 12%, #d8d8d8);
   --cor-fundo:color-mix(in oklab, var(--cor-primaria) 4%, #ffffff); */
@font-face{font-family:'{{FONTE_TITULO}}';src:url('assets/fonts/{{ARQUIVO_FONTE_TITULO}}.woff2') format('woff2');font-weight:700;font-style:normal;font-display:swap}
@font-face{font-family:'{{FONTE_TEXTO}}';src:url('assets/fonts/{{ARQUIVO_FONTE_TEXTO}}.woff2') format('woff2');font-weight:400;font-style:normal;font-display:swap}

/* ===== 2. BASE, mobile first (360 px) ===== */
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;caret-color:var(--cor-primaria);accent-color:var(--cor-primaria);scrollbar-color:color-mix(in oklab, var(--cor-primaria) 55%, var(--cor-fundo)) var(--cor-fundo)}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;font-family:var(--fonte-texto);font-size:16px;line-height:1.5;color:var(--cor-texto);background:var(--cor-fundo);padding-bottom:var(--altura-barra)}
::selection{background:var(--cor-primaria);color:var(--cor-sobre-primaria)}
img{max-width:100%;height:auto;display:block}
h1,h2,h3{font-family:var(--fonte-titulo);font-weight:700;line-height:1.15;margin:0;text-wrap:balance;overflow-wrap:anywhere}
h1{font-size:clamp(1.875rem,6vw,2.75rem);letter-spacing:-0.02em;margin-bottom:16px}
h2{font-size:clamp(1.5rem,4.5vw,2.125rem);letter-spacing:-0.015em;margin-bottom:20px}
h3{font-size:1.125rem;margin:24px 0 6px}
p{margin:0 0 1em;max-width:65ch}
a{color:var(--cor-primaria);text-underline-offset:.15em;text-decoration-thickness:.08em}
.num{font-variant-numeric:tabular-nums}
.container{width:100%;max-width:var(--largura-max);margin:0 auto;padding:0 20px}
section{padding:48px 0}
.suave{color:var(--cor-texto-suave)}
.hp{position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden}

/* ===== 3. HEADER: logo e, só no desktop, o CTA ===== */
.topo{position:sticky;top:0;z-index:40;background:var(--cor-superficie);border-bottom:1px solid var(--cor-borda)}
.topo .container{display:flex;align-items:center;justify-content:space-between;height:64px}
.topo img{height:32px;width:auto}
.topo .btn{display:none}

/* ===== 4. BOTÃO DE CTA (fase 5.4): redesenhar no vocabulário do mundo, manter as medidas ===== */
.btn{display:inline-flex;align-items:center;justify-content:center;width:100%;min-height:var(--altura-cta);padding:0 24px;border:0;border-radius:var(--raio);font-family:var(--fonte-titulo);font-weight:700;font-size:1.0625rem;line-height:1.2;text-align:center;text-decoration:none;cursor:pointer;transition:transform .25s var(--suave),filter .25s var(--suave)}
.btn--cta{background:var(--cor-cta);color:var(--cor-cta-texto);box-shadow:var(--sombra)}
.btn--cta:hover{filter:brightness(1.06);transform:translateY(-1px)}
.btn--cta:focus-visible{outline:3px solid var(--cor-primaria);outline-offset:3px}
.btn[disabled]{opacity:.6;cursor:wait;transform:none}

/* ===== 5. BARRA FIXA DE CTA, só mobile e tablet (fase 5.4) ===== */
#cta-fixa{position:fixed;left:0;right:0;bottom:0;z-index:50;padding:8px 16px calc(8px + env(safe-area-inset-bottom));background:var(--cor-superficie);box-shadow:0 -6px 20px -10px color-mix(in oklab, var(--cor-primaria) 40%, transparent);transform:translateY(110%);transition:transform .3s var(--suave)}
#cta-fixa.visivel{transform:translateY(0)}
@media (prefers-reduced-motion:reduce){#cta-fixa,.btn{transition:none}}

/* ===== 6. PRIMEIRA DOBRA (S01): composição vem do esboço travado na fase 3 ===== */
.hero{padding:40px 0 56px}
.hero__sub{font-size:1.125rem;margin-bottom:12px}
.hero__prova{font-weight:600;margin-bottom:24px}
.hero__micro{font-size:.875rem;color:var(--cor-texto-suave);margin:10px 0 0}
.hero__midia{margin-top:32px}
.hero__midia img{border-radius:var(--raio)}

/* ===== 7. SEÇÕES DO CORPO ===== */
.lista-check{list-style:none;padding:0;margin:0 0 24px}
.lista-check li{position:relative;padding-left:34px;margin-bottom:12px}
.lista-check li::before{content:"";position:absolute;left:0;top:2px;width:22px;height:22px;background:var(--cor-primaria);-webkit-mask:var(--icone-check) center/contain no-repeat;mask:var(--icone-check) center/contain no-repeat}
.passos{list-style:none;padding:0;margin:0 0 24px;counter-reset:passo}
.passos li{position:relative;padding-left:52px;margin-bottom:24px}
.passos li h3{margin-top:0}
.passos li::before{counter-increment:passo;content:counter(passo);position:absolute;left:0;top:0;width:36px;height:36px;border-radius:50%;background:var(--cor-primaria);color:var(--cor-sobre-primaria);font-family:var(--fonte-titulo);font-weight:700;line-height:36px;text-align:center;font-variant-numeric:tabular-nums}
.campo-cor{background:var(--cor-primaria);color:var(--cor-sobre-primaria);padding:64px 0}
.campo-cor h2{color:inherit}
.campo-cor .suave{color:color-mix(in oklab, var(--cor-sobre-primaria) 80%, var(--cor-primaria))}
.caso{margin:0 0 40px;padding:0}
.caso__numero{font-family:var(--fonte-titulo);font-size:clamp(2.75rem,10vw,4.5rem);line-height:1;letter-spacing:-0.02em;font-variant-numeric:tabular-nums;margin-bottom:12px}
.caso blockquote{margin:0 0 12px;font-size:1.125rem;max-width:36ch}
.caso figcaption{font-size:.9375rem}
.prova-social{display:flex;flex-wrap:wrap;gap:16px 28px;align-items:center;margin:0 0 32px}
.prova-social img{height:28px;width:auto}
.objecao{margin-bottom:32px}
.objecao h3{margin-top:0}
.quem{display:grid;gap:40px}
.faq{padding-top:32px}
.faq details{border-bottom:1px solid var(--cor-borda)}
.faq summary{display:flex;align-items:center;gap:16px;min-height:48px;padding:12px 0;font-weight:600;cursor:pointer;list-style:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"";flex:none;width:20px;height:20px;margin-left:auto;background:var(--cor-primaria);-webkit-mask:var(--icone-seta) center/contain no-repeat;mask:var(--icone-seta) center/contain no-repeat;transition:transform .3s var(--suave)}
.faq details[open] summary::after{transform:rotate(180deg)}
.faq details p{padding-bottom:16px}
.cta-meio{text-align:center;margin:8px 0 0}

/* ===== 8. FORMULÁRIO (fase 6): redesenhar campo, label e erro no vocabulário do mundo ===== */
.fechamento{padding:64px 0 72px}
.form{background:var(--cor-superficie);border:1px solid var(--cor-borda);border-radius:var(--raio);padding:28px 20px;box-shadow:var(--sombra)}
.campo{margin-bottom:18px}
.campo label{display:block;font-weight:600;margin-bottom:6px}
.campo input,.campo select{width:100%;min-height:48px;padding:12px 14px;font:inherit;font-size:16px;color:var(--cor-texto);background:var(--cor-superficie);border:1px solid var(--cor-borda);border-radius:var(--raio)}
.campo input:focus,.campo select:focus{outline:2px solid var(--cor-primaria);outline-offset:1px;border-color:var(--cor-primaria)}
.campo input[aria-invalid="true"]{border-color:var(--cor-erro)}
.campo .erro{display:block;min-height:1.25em;margin-top:4px;font-size:.875rem;color:var(--cor-erro)}
.form__lgpd{font-size:.8125rem;color:var(--cor-texto-suave);margin:12px 0}
.form__sla{font-size:.9375rem;margin:14px 0 0}
.form__falha{margin:12px 0 0;padding:12px;border:1px solid var(--cor-erro);border-radius:var(--raio);color:var(--cor-erro)}

/* ===== 9. RODAPÉ ===== */
.rodape{padding:28px 0 36px;font-size:.8125rem;color:var(--cor-texto-suave);border-top:1px solid var(--cor-borda)}
.rodape img{height:24px;width:auto;margin-bottom:8px}

/* ===== 10. TABLET ===== */
@media (min-width:768px){
  body{font-size:17px}
  section{padding:64px 0}
  .campo-cor{padding:88px 0}
  .btn{width:auto;min-width:280px}
  .quem{grid-template-columns:1fr 1fr}
  .form{padding:32px}
}

/* ===== 11. DESKTOP ===== */
@media (min-width:1024px){
  body{font-size:18px;padding-bottom:0}
  .topo .btn{display:inline-flex;min-width:0;min-height:44px;padding:0 20px;font-size:1rem;box-shadow:none}
  #cta-fixa{display:none}
  section{padding:80px 0}
  .campo-cor{padding:104px 0}
  .hero{padding:72px 0 88px}
  .hero__grid{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center}
  .hero__midia{margin-top:0}
  .fechamento .container{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:start}
  .form{max-width:560px}
}
</style>
</head>

<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={{GTM_ID}}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<header class="topo">
  <div class="container">
    <img src="assets/logo.svg" width="140" height="32" alt="{{MARCA}}">
    <a class="btn btn--cta" href="#form-lead" data-evento="cta_click" data-posicao="header">{{CTA}}</a>
  </div>
</header>

<main>

<!-- S01 -->
<section id="s01" class="hero" data-secao="S01">
  <div class="container hero__grid">
    <div class="hero__texto">
      <h1>{{HEADLINE}}</h1>
      <p class="hero__sub">{{SUB}}</p>
      <p class="hero__prova num">{{PROVA_IMEDIATA}}</p>
      <a id="cta-hero" class="btn btn--cta" href="#form-lead" data-evento="cta_click" data-posicao="hero">{{CTA}}</a>
      <p class="hero__micro">{{MICROCOPY_CTA}}</p>
    </div>
    <div class="hero__midia">
      <!-- Direção desktop: mover o <form id="form-lead"> da S08 para cá e remover a mídia. -->
      <picture>
        <source media="(min-width: 1024px)" srcset="assets/img/hero-1200.webp">
        <img src="assets/img/hero-600.webp" width="600" height="450" alt="{{ALT_HERO}}" fetchpriority="high" decoding="async">
      </picture>
    </div>
  </div>
</section>

<!-- S02 -->
<section id="s02" data-secao="S02">
  <div class="container">
    <h2>{{S02_TITULO}}</h2>
    <ul class="lista-check">
      <li>{{S02_SINTOMA_1}}</li>
      <li>{{S02_SINTOMA_2}}</li>
      <li>{{S02_SINTOMA_3}}</li>
    </ul>
  </div>
</section>

<!-- S03 -->
<section id="s03" data-secao="S03">
  <div class="container">
    <h2>{{S03_TITULO}}</h2>
    <ol class="passos">
      <li><h3>{{S03_PASSO_1_TITULO}}</h3><p>{{S03_PASSO_1_OBJETIVO}}</p></li>
      <li><h3>{{S03_PASSO_2_TITULO}}</h3><p>{{S03_PASSO_2_OBJETIVO}}</p></li>
      <li><h3>{{S03_PASSO_3_TITULO}}</h3><p>{{S03_PASSO_3_OBJETIVO}}</p></li>
    </ol>
  </div>
</section>

<!-- S04 -->
<section id="s04" class="campo-cor" data-secao="S04">
  <div class="container">
    <h2>{{S04_TITULO}}</h2>
    <figure class="caso">
      <div class="caso__numero">{{S04_CASO_1_NUMERO}}</div>
      <blockquote>{{S04_CASO_1_DEPOIMENTO}}</blockquote>
      <figcaption class="suave">{{S04_CASO_1_NOME}}, {{S04_CASO_1_CARGO}}, {{S04_CASO_1_EMPRESA}}</figcaption>
    </figure>
    <div class="prova-social">
      <img src="assets/img/logo-cliente-1.svg" width="120" height="28" alt="{{S04_LOGO_1_NOME}}" loading="lazy" decoding="async">
      <img src="assets/img/logo-cliente-2.svg" width="120" height="28" alt="{{S04_LOGO_2_NOME}}" loading="lazy" decoding="async">
      <p class="suave num">{{S04_PROVA_SOCIAL_NUMERO}}</p>
    </div>
    <p class="cta-meio"><a class="btn btn--cta" href="#form-lead" data-evento="cta_click" data-posicao="meio">{{CTA}}</a></p>
  </div>
</section>

<!-- S05 -->
<section id="s05" data-secao="S05">
  <div class="container">
    <h2>{{S05_TITULO}}</h2>
    <article class="objecao"><h3>{{S05_OBJECAO_1}}</h3><p>{{S05_RESPOSTA_1}}</p><p class="suave">{{S05_PROVA_1}}</p></article>
    <article class="objecao"><h3>{{S05_OBJECAO_2}}</h3><p>{{S05_RESPOSTA_2}}</p><p class="suave">{{S05_PROVA_2}}</p></article>
    <article class="objecao"><h3>{{S05_OBJECAO_3}}</h3><p>{{S05_RESPOSTA_3}}</p><p class="suave">{{S05_PROVA_3}}</p></article>
  </div>
</section>

<!-- S06 -->
<section id="s06" data-secao="S06">
  <div class="container quem">
    <div><h2>{{S06_TITULO_E}}</h2><ul class="lista-check"><li>{{S06_E_1}}</li><li>{{S06_E_2}}</li><li>{{S06_E_3}}</li></ul></div>
    <div><h2>{{S06_TITULO_NAO_E}}</h2><ul class="lista-check"><li>{{S06_NAO_E_1}}</li><li>{{S06_NAO_E_2}}</li></ul></div>
  </div>
</section>

<!-- S07 -->
<section id="s07" class="faq" data-secao="S07">
  <div class="container">
    <h2>{{S07_TITULO}}</h2>
    <details><summary>{{S07_P1}}</summary><p>{{S07_R1}}</p></details>
    <details><summary>{{S07_P2}}</summary><p>{{S07_R2}}</p></details>
    <details><summary>{{S07_P3}}</summary><p>{{S07_R3}}</p></details>
    <details><summary>{{S07_P4}}</summary><p>{{S07_R4}}</p></details>
    <details><summary>{{S07_P5}}</summary><p>{{S07_R5}}</p></details>
  </div>
</section>

<!-- S08 -->
<section id="s08" class="fechamento" data-secao="S08">
  <div class="container">
    <div>
      <h2>{{S08_TITULO}}</h2>
      <p>{{S08_TEXTO}}</p>
    </div>
    <form id="form-lead" class="form" novalidate autocomplete="on">
      <div class="campo">
        <label for="firstname">{{LABEL_NOME}}</label>
        <input id="firstname" name="firstname" type="text" autocomplete="name" required aria-describedby="firstname-erro">
        <span id="firstname-erro" class="erro" aria-live="polite"></span>
      </div>
      <div class="campo">
        <label for="email">{{LABEL_EMAIL}}</label>
        <input id="email" name="email" type="email" inputmode="email" autocomplete="email" required aria-describedby="email-erro">
        <span id="email-erro" class="erro" aria-live="polite"></span>
      </div>
      <div class="campo">
        <label for="phone">{{LABEL_WHATSAPP}}</label>
        <input id="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="(11) 99999-9999" required aria-describedby="phone-erro">
        <span id="phone-erro" class="erro" aria-live="polite"></span>
      </div>
      <!-- Campos adicionais só com justificativa de roteamento na ficha (fase 6.1). -->

      <!-- Honeypot: humano não vê, bot preenche -->
      <div class="hp" aria-hidden="true"><label>Site<input name="site_web" type="text" tabindex="-1" autocomplete="off"></label></div>

      <!-- Origem: preenchidos pelo script (fase 7.1). Os names são as propriedades do CRM. -->
      <input type="hidden" name="utm_source"><input type="hidden" name="utm_medium"><input type="hidden" name="utm_campaign">
      <input type="hidden" name="utm_content"><input type="hidden" name="utm_term"><input type="hidden" name="gclid"><input type="hidden" name="fbclid">
      <input type="hidden" name="page_url"><input type="hidden" name="lp_versao" value="{{LP_VERSAO}}">

      <p class="form__lgpd">{{TEXTO_LGPD}} <a href="{{URL_POLITICA}}" target="_blank" rel="noopener">Política de privacidade</a>.</p>
      <button type="submit" class="btn btn--cta">{{CTA}}</button>
      <p class="form__sla">{{SLA_DEPOIS_DO_CLIQUE}}</p>
      <div id="form-falha" class="form__falha" hidden>{{MENSAGEM_FALHA}} <a href="{{LINK_ALTERNATIVO}}" target="_blank" rel="noopener">{{TEXTO_LINK_ALTERNATIVO}}</a></div>
    </form>
  </div>
</section>

</main>

<!-- Barra fixa de CTA: mobile e tablet (fase 5.4) -->
<div id="cta-fixa">
  <a class="btn btn--cta" href="#form-lead" data-evento="cta_click" data-posicao="barra">{{CTA}}</a>
</div>

<footer class="rodape">
  <div class="container">
    <img src="assets/logo.svg" width="105" height="24" alt="{{MARCA}}">
    <p>{{RAZAO_SOCIAL}} · <a href="{{URL_POLITICA}}" target="_blank" rel="noopener">Política de privacidade</a></p>
  </div>
</footer>

<script>
(function () {
  'use strict';
  var form = document.getElementById('form-lead');
  var barra = document.getElementById('cta-fixa');
  var ctaHero = document.getElementById('cta-hero');

  function push(obj) { window.dataLayer = window.dataLayer || []; window.dataLayer.push(obj); }

  /* 1. Origem: UTM e click IDs capturados na entrada, guardados na sessão, escritos nos campos ocultos (fase 7.1) */
  var chaves = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid', 'fbclid'];
  var params = new URLSearchParams(window.location.search);
  chaves.forEach(function (k) {
    var v = params.get(k);
    if (v) { try { sessionStorage.setItem('lp_' + k, v.toLowerCase()); } catch (e) {} }
    var salvo = null;
    try { salvo = sessionStorage.getItem('lp_' + k); } catch (e) {}
    var campo = form.querySelector('input[name="' + k + '"]');
    if (campo && salvo) { campo.value = salvo; }
  });
  var campoUrl = form.querySelector('input[name="page_url"]');
  if (campoUrl) { campoUrl.value = window.location.href; }

  /* 2. Barra fixa (fase 5.4): visível só quando nenhum CTA da página está na tela e o formulário não está visível */
  if (barra && ctaHero && 'IntersectionObserver' in window) {
    var ctasVisiveis = new Set(), formVisivel = false;
    var atualiza = function () { barra.classList.toggle('visivel', ctasVisiveis.size === 0 && !formVisivel); };
    var obsCta = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) { if (e.isIntersecting) { ctasVisiveis.add(e.target); } else { ctasVisiveis.delete(e.target); } });
      atualiza();
    }, { threshold: 0 });
    document.querySelectorAll('main .btn--cta').forEach(function (b) { obsCta.observe(b); });
    new IntersectionObserver(function (e) { formVisivel = e[0].isIntersecting; atualiza(); }, { threshold: 0.15 }).observe(form);
  } else if (barra) {
    barra.classList.add('visivel');
  }

  /* 3. Eventos de etapa (nunca conversão) */
  document.querySelectorAll('[data-evento="cta_click"]').forEach(function (el) {
    el.addEventListener('click', function () {
      push({ event: 'cta_click', cta_posicao: el.getAttribute('data-posicao'), cta_texto: el.textContent.trim() });
      var primeiro = form.querySelector('input:not([type="hidden"])');
      if (primeiro) { setTimeout(function () { primeiro.focus({ preventScroll: true }); }, 400); }
    });
  });
  var formIniciado = false;
  form.addEventListener('focusin', function () {
    if (!formIniciado) { formIniciado = true; push({ event: 'form_start', form_id: form.id }); }
  });
  document.querySelectorAll('.faq details').forEach(function (d) {
    d.addEventListener('toggle', function () { if (d.open) { push({ event: 'faq_open', faq_pergunta: d.querySelector('summary').textContent.trim() }); } });
  });

  /* 4. Máscara leve de telefone: só dígitos, formato (DD) 9XXXX-XXXX */
  var tel = form.querySelector('input[type="tel"]');
  if (tel) {
    tel.addEventListener('input', function () {
      var d = tel.value.replace(/\D/g, '').slice(0, 11);
      var f = d;
      if (d.length > 2) { f = '(' + d.slice(0, 2) + ') ' + d.slice(2); }
      if (d.length > 7) { f = '(' + d.slice(0, 2) + ') ' + d.slice(2, 7) + '-' + d.slice(7); }
      tel.value = f;
    });
  }

  /* 5. Validação inline (fase 6.3) */
  function erro(campo, msg) { campo.setAttribute('aria-invalid', 'true'); var el = document.getElementById(campo.id + '-erro'); if (el) { el.textContent = msg; } }
  function limpa(campo) { campo.removeAttribute('aria-invalid'); var el = document.getElementById(campo.id + '-erro'); if (el) { el.textContent = ''; } }
  function valida() {
    var ok = true;
    form.querySelectorAll('[required]').forEach(function (c) {
      limpa(c);
      var v = c.value.trim();
      if (!v) { erro(c, '{{MSG_CAMPO_VAZIO}}'); ok = false; return; }
      if (c.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) { erro(c, '{{MSG_EMAIL_INVALIDO}}'); ok = false; }
      if (c.type === 'tel' && v.replace(/\D/g, '').length < 10) { erro(c, '{{MSG_TELEFONE_INVALIDO}}'); ok = false; }
    });
    return ok;
  }

  /* 6. Envio (fase 6.4): implementar UMA opção dentro de enviar() */
  function enviar(dados) {
    var campos = [];
    dados.forEach(function (v, k) {
      if (k === 'site_web') { return; }
      if (k === 'phone') { v = '+55' + String(v).replace(/\D/g, ''); }
      campos.push({ objectTypeId: '0-1', name: k, value: v });
    });
    var hutk = (document.cookie.match(/(^|;\s*)hubspotutk=([^;]+)/) || [])[2] || '';
    return fetch('https://api.hsforms.com/submissions/v3/integration/submit/{{PORTAL_ID}}/{{FORM_GUID}}', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ fields: campos, context: { hutk: hutk, pageUri: window.location.href, pageName: document.title } })
    }).then(function (r) { if (!r.ok) { throw new Error('HTTP ' + r.status); } return r; });
  }

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var hp = form.querySelector('input[name="site_web"]');
    if (hp && hp.value) { return; }
    if (!valida()) { var inv = form.querySelector('[aria-invalid="true"]'); if (inv) { inv.focus(); } return; }
    var botao = form.querySelector('button[type="submit"]');
    var texto = botao.textContent;
    botao.disabled = true; botao.textContent = '{{TEXTO_ENVIANDO}}';
    var eventId = (window.crypto && crypto.randomUUID) ? crypto.randomUUID() : String(Date.now()) + Math.random().toString(16).slice(2);
    enviar(new FormData(form)).then(function () {
      try { sessionStorage.setItem('lp_event_id', eventId); } catch (e) {}
      window.location.href = 'obrigado.html';
    }).catch(function () {
      botao.disabled = false; botao.textContent = texto;
      document.getElementById('form-falha').hidden = false;
    });
  });
})();
</script>
</body>
</html>
```

---

## ANEXO B | ESQUELETO `obrigado.html`

```html
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TY_TITULO}} | {{MARCA}}</title>
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">

<!-- Conversão: generate_lead dispara UMA vez, só com event_id vindo do envio real (fase 7.3). Antes do GTM. -->
<script>
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({ lp_nome: '{{LP_NOME}}', lp_versao: '{{LP_VERSAO}}', page_tipo: 'thank_you' });
  (function () {
    var eid = null;
    try { eid = sessionStorage.getItem('lp_event_id'); } catch (e) {}
    if (eid) {
      window.dataLayer.push({ event: 'generate_lead', lp_nome: '{{LP_NOME}}', event_id: eid });
      try { sessionStorage.removeItem('lp_event_id'); } catch (e) {}
    }
  })();
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','{{GTM_ID}}');</script>
<!-- End Google Tag Manager -->

<style>
/* Copiar os blocos 1 (tokens), 2 (base), 3 (header), 4 (botão), 7 (seções do corpo) e 9 (rodapé) do index.html. Sem barra fixa. */
{{CSS_COPIADO_DO_INDEX}}
body{padding-bottom:0}
.ty{padding:48px 0 64px}
.ty h1{margin-bottom:12px}
.ty__sla{font-size:1.125rem;font-weight:600;margin-bottom:32px}
.ty h2{margin-top:8px}
.ty .passos{margin-bottom:40px}
.ty__contato{margin-top:28px}
@media (min-width:1024px){.ty{padding:88px 0 104px}.ty .container{max-width:720px}}
</style>
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={{GTM_ID}}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<header class="topo"><div class="container"><img src="assets/logo.svg" width="140" height="32" alt="{{MARCA}}"></div></header>

<main>
<!-- TY -->
<section class="ty" data-secao="TY">
  <div class="container">
    <h1>{{TY_CONFIRMACAO}}</h1>
    <p class="ty__sla">{{TY_SLA}}</p>

    <h2>{{TY_O_QUE_ACONTECE_AGORA}}</h2>
    <ol class="passos">
      <li><h3>{{TY_PASSO_1_TITULO}}</h3><p>{{TY_PASSO_1_TEXTO}}</p></li>
      <li><h3>{{TY_PASSO_2_TITULO}}</h3><p>{{TY_PASSO_2_TEXTO}}</p></li>
      <li><h3>{{TY_PASSO_3_TITULO}}</h3><p>{{TY_PASSO_3_TEXTO}}</p></li>
    </ol>

    <h2>{{TY_PROXIMO_DEGRAU_TITULO}}</h2>
    <p>{{TY_PROXIMO_DEGRAU_TEXTO}}</p>
    <a class="btn btn--cta" href="{{TY_PROXIMO_DEGRAU_URL}}" data-evento="next_step_click" target="_blank" rel="noopener">{{TY_PROXIMO_DEGRAU_CTA}}</a>

    <p class="ty__contato">{{TY_CONTATO_DIRETO}} <a href="https://wa.me/{{WHATSAPP_NUMERO}}?text={{WHATSAPP_MENSAGEM_CODIFICADA}}" target="_blank" rel="noopener">{{TY_CONTATO_LINK_TEXTO}}</a></p>
  </div>
</section>
</main>

<footer class="rodape"><div class="container"><img src="assets/logo.svg" width="105" height="24" alt="{{MARCA}}"><p>{{RAZAO_SOCIAL}} · <a href="{{URL_POLITICA}}" target="_blank" rel="noopener">Política de privacidade</a></p></div></footer>

<script>
(function () {
  function push(obj) { window.dataLayer = window.dataLayer || []; window.dataLayer.push(obj); }
  document.querySelectorAll('[data-evento="next_step_click"]').forEach(function (el) {
    el.addEventListener('click', function () { push({ event: 'next_step_click', destino: el.getAttribute('href') }); });
  });
})();
</script>
</body>
</html>
```

---

## ANEXO C | BLUEPRINTS POR TIPO (ordem das seções em `<main>`)

O blueprint fixa a lógica de conversão (ordem e função das seções). A composição de cada seção, em especial da primeira dobra, vem das fases 2 e 3. O código da seção (`S01`...) vai no `id` e no `data-secao`; o racional vai no mapa de conexão de `01_ficha.md`.

### C.1 Squeeze page
1. S01 Primeira dobra: headline = promessa do lead magnet (até 8 palavras); sub = para quem + o que resolve + em quanto tempo; o entregável real em cena (mockup verdadeiro, não ícone); formulário de e-mail (+ nome se a nutrição for personalizada) dentro da primeira dobra; CTA em primeira pessoa; micro-prova (número de downloads ou 1 depoimento)
2. S02 O que você recebe: 3 itens do conteúdo (`lista-check`)
3. S03 Quem assina: 2 linhas + resultado, com foto real
4. S08 CTA final com o mesmo formulário (âncora) e rodapé LGPD
Thank-you: entrega do material + oferta de qualificação de comprador imediata.

### C.2 Lead gen B2B consultivo (esqueleto completo do Anexo A)
1. S01 Primeira dobra: headline no KPI do decisor (não a categoria do serviço); sub = mecanismo em uma frase + ICP explícito; prova acima da dobra (logos, número, rating); CTA primário agendar; o mecanismo demonstrado quando a direção pede (a tela real, rotulada se ilustrativa)
2. S02 Você está aqui: 3 a 4 sintomas
3. S03 Mecanismo em 3 passos
4. S04 Prova (pico da rolagem, campo de cor): 1 a 2 cases com número, nome, cargo, antes e depois; prova social separada; CTA repetido
5. S05 Objeções: veículo, interna, externa
6. S06 Para quem é / para quem não é
7. S07 FAQ (quieto): prazo, integração, time, preço em faixa
8. S08 Fechamento: CTA final + o que acontece depois do clique + formulário de 3 a 5 campos (multi-step para qualificar)
Regras: new opportunity, nunca improvement; não ensinar na página; prova específica, nunca "milhares de clientes".

### C.3 Serviço B2C ou local (com WhatsApp)
1. S01 Primeira dobra: headline = problema + resultado + geografia (quando local); sub = prazo, preço de entrada ou "a partir de", diferencial; prova imediata (nota, número de clientes, anos na cidade, foto real do time ou do lugar); CTA = formulário curto ou WhatsApp (nunca os dois sem medir separado)
2. S03 Como funciona em 3 passos
3. S04 Depoimentos com nome, cidade, situação (campo de cor); CTA repetido
4. S05 Planos ou faixas de preço com âncora
5. S07 FAQ (migração, prazo, documentos, fidelidade)
6. S08 Fechamento: CTA final + horário de atendimento + tempo de resposta prometido
Regras: WhatsApp como funil próprio (bot, CRM, evento = conversa iniciada); foto real, nunca stock; barra fixa com o link wa.me.

### C.4 Sales page longa ou VSL
1. S01 Hook: Big Idea como afirmação (VSL com fachada de vídeo, poster + clique)
2. S02 Identificação: "sempre que..." (âncora cotidiana)
3. S03 Virada: a história que instalou a crença (epiphany bridge)
4. S04 Furadeira: o método
5. S05 Quadro: resultado tangível imediato
6. S06 Decorado: o desejo profundo, com detalhe específico
7. S07 Prova (casos) + prova social (volume), separadas
8. S08 Stack: item a item com valor, tudo empilhado antes do preço
9. S09 Preço com ancoragem descendente
10. S10 Garantia
11. S11 Escassez real (número ou data)
12. S12 FAQ das 10 objeções
13. S13 CTA final (checkout); CTA repetido em 3 pontos
Regras: cobrir os 3 compradores (emocional, lógico, FOMO); sem "custaria"; sem bônus de enchimento; escassez só real.

### C.5 Bridge, advertorial e quiz
Advertorial: S01 título editorial → S02 premissa incontestável (P1) → S03 história com o avatar (P2) → S04 o que a maioria faz errado e por quê (P3 → conclusão) → S05 solução como consequência lógica → S06 uma prova → S07 CTA de click-through (link para a LP, sem formulário).
Quiz: S01 pergunta de menor compromisso → S02 4 a 8 perguntas em `<fieldset data-step>` com "Passo N de T" → S03 resultado que entrega valor → S04 só então o contato.
Regras: casar formato com canal (native = advertorial e listicle; Meta = quiz e problema/solução; Search = problema/solução curta); escrever a transição conteúdo → oferta primeiro; sem início técnico, imperativo ou prometendo.

### C.6 Webinar ou evento
1. S01 Primeira dobra: headline = o "one thing" que a pessoa sai sabendo; data, hora, duração, formato; CTA garantir vaga
2. S02 3 "segredos" como curiosidade (o que será quebrado, não o conteúdo)
3. S03 Quem apresenta (2 linhas + resultado, foto real)
4. S06 Para quem é
5. S04 Prova social de edições e inscritos
6. S08 Formulário: nome, e-mail, WhatsApp (lembrete faz parte da conversão)
Thank-you: adicionar à agenda (link .ics ou Google Agenda) + sequência de lembrete. KPI real = show-up.

### C.7 Thank-you page (Anexo B)
1. Confirmação específica com SLA
2. O que acontece agora (timeline, canal, quem)
3. Próximo degrau imediato
4. Contato direto para quem não quer esperar
Conversão dispara aqui, uma vez, com `event_id`.

### C.8 Click-through ou trial
1. S01 Primeira dobra: headline de resultado; sub = a dor que o produto remove; campo único (e-mail) + CTA começar grátis; o produto em funcionamento em cena
2. S02 3 benefícios (`lista-check`)
3. S04 Prova (logos, número de clientes)
4. S08 CTA final (mesmo campo único)
Regras: KPI é ativação, não signup; trial CTA supera demo CTA em self-serve.

---

## ANEXO D | TEMPLATES DE TRABALHO (`docs/`)

### D.1 `00_entendimento.md`

```markdown
# Entendimento | {projeto} | {canal} | {data}

## ICP e leitor
- Quem é:
- Onde está quando clica:
- Fonte:

## Canal e jornada
- Canal de entrada:
- Tela em que abre:
- Mobile por natureza? (sim / não)

## Histórico de dispositivo por canal
| Canal | Sessões mobile % | Conversões mobile % | Taxa mobile | Taxa desktop | Período | Fonte |
|---|---|---|---|---|---|---|

## Benchmark do segmento (só se não houver histórico)
| Métrica | Valor | Fonte | Ano |
|---|---|---|---|

## Temperatura do tráfego
- Quente / morna / fria, e por quê:

## Persuade (três perguntas + duas de fechamento)
- Quem precisa agir:
- No que precisa acreditar para agir:
- Qual prova, conteúdo ou asset real ganha essa crença:
- O que precisa ficar intocado:
- O que faria um resultado polido parecer errado:

## Cena de uso
- Quem abre, onde, em que luz, em que estado de espírito (uma frase):

## Provas reais disponíveis
| Prova | Tipo (caso / social / autoridade / demonstração) | Confirmada por | Status |
|---|---|---|---|

## Objeções
- Principal:
- Secundárias:

## Big Domino
- Se o leitor acreditar que ___, as outras objeções deixam de importar.

## Autoridade visual e materiais de marca
- Situação (design system / mundo no código / marca incompleta / sem autoridade):
| Material | Recebido (sim / não) | Formato | Fonte | Data |
|---|---|---|---|---|

## Insumos técnicos
| Insumo | Valor | Fornecido por | Data |
|---|---|---|---|
| URL final | | | |
| Destino de publicação | | | |
| GTM ID | | | |
| Mecanismo do formulário (portalId, formGuid ou URL do webhook) | | | |
| Nomes dos campos no CRM | | | |
| WhatsApp (número, quem atende) | | | |
| Política de privacidade (URL) e texto de consentimento | | | |
| Razão social para o rodapé | | | |
| Indexação | | | |
| SLA e responsável pelo atendimento | | | |

## Perguntas enviadas e respondidas (nada avança sem resposta)
| Pergunta | Decisão que desbloqueia | Para quem | Resposta | Respondido por | Data |
|---|---|---|---|---|---|
```

### D.2 `01_ficha.md`

```markdown
# Ficha | {projeto} | {canal} | {tipo} | v{N}

## Ficha (fase 1)
1. Conversão única: esta página existe para
2. Tipo de conversão: final / de etapa (steps: )
3. Evento medido:
4. Canal e jornada de entrada:
5. Direção de dispositivo da v1: mobile / desktop. Origem: canal / histórico / benchmark. Revisão com dado real em: {data}
6. Temperatura:
7. Leitor 1 (hero) precisa ver:
8. Leitor 2 (confirmação) pergunta:
9. Leitor 3 (convencimento) objeta:
10. CTA: texto "{...}"; posições: hero, meio, final; visibilidade: barra fixa mobile / header desktop
11. Pós-conversão:
12. Tracking: evento {…}; UTM {…}; pixel + CAPI {…}; campo CRM {…}
13. Destino de publicação e URL final:
14. Mecanismo de envio do formulário e nomes dos campos no CRM:
15. Autoridade visual: design system de {fonte} em {data} / mundo no site {URL} / marca incompleta ({confirmado}) / sem autoridade (rodada 2 em {data})
16. Indexação: sim / não
17. Cena de uso: {uma frase}. Claro / escuro: {decisão}

## Mundo visual (fase 2)
- Estratégia de cor: contida / comprometida / paleta completa / encharcada, e por quê
- Fontes: título {nome, origem, licença}; texto {nome, origem, licença}; motivo da escolha
- Teste de calibragem (resposta por escrito):
- Rodada 2 (se houve): cartões enviados {A, B, C, saída padrão}; travado: {X}; por quem; data

## Contrato de direção (fase 2.4)
- TESE:
- MUNDO PRÓPRIO:
- HISTÓRIA:
- PRIMEIRA DOBRA:
- FORMA:
- ACABAMENTO: sem revisão de acabamento e sem DESIGN.md a página não está pronta

## Tokens (fase 2.5)
| Token | Valor | Contraste medido | Origem |
|---|---|---|---|
| --cor-primaria / --cor-sobre-primaria | | x,x:1 | |
| --cor-cta / --cor-cta-texto | | x,x:1 | |
| --cor-fundo / --cor-texto | | x,x:1 | |
| --cor-texto-suave sobre fundo | | x,x:1 | |
| --fonte-titulo / --fonte-texto | | n/a | |
| Exceções de marca aplicadas (regra 2.6) | | | |

## Tipo e blueprint (fase 3.1)
- Tipo escolhido:
- Justificativa (duas linhas):
- Blueprint base: Anexo C.{n}

## Mapa de conexão e ritmo (fase 3.2)
| Seção | Leitor | Objetivo | Empurra para o CTA? | Como | Densidade (densa / média / quieta) |
|---|---|---|---|---|---|
| S01 | 1 | | sim | CTA primário | densa |
| S02 | 2 | | sim | | |
- Pico da rolagem: S0_ · Fechamento: S08

## Primeira dobra (fase 3.3)
- Esboços enviados: 1) {o que lidera} 2) {o que lidera} 3) {o que lidera}; capturas em docs/esbocos/
- Travado: {n}, por quem, data (ou "delegado por escrito em {data}; escolhido pela evidência {…}")
- Teste da memória (resposta):
- Invariantes conferidas em 360×640 e 1440×900: sim

## Campos do formulário (fase 6)
| Campo | Name no CRM | Necessário para rotear? | Necessário para o próximo passo humano? | Decisão |
|---|---|---|---|---|

## Assets
| Asset | Seção | Peso | Status (existe / será produzido até data acordada) | Responsável |
|---|---|---|---|---|
```

### D.3 `02_copy.md`

```markdown
# Copy | {projeto} | {canal} | v{N}

## Head
- title (até 60 caracteres):
- description (até 155 caracteres):
- alt da mídia da primeira dobra:

## [S01] Primeira dobra (leitor 1)
- Headline (escolhida):
- Variantes guardadas para teste: 1) 2) 3) 4)
- Sub (mecanismo + para quem + prazo):
- Prova imediata:
- CTA (string única da página):
- Microcopy sob o CTA:

## [S02] Você está aqui (leitor 2)
- Título:
- Sintoma 1:
- Sintoma 2:
- Sintoma 3:

## [S03] Mecanismo em 3 passos (leitor 2)
- Título:
- Passo 1 (título + objetivo):
- Passo 2 (título + objetivo):
- Passo 3 (título + objetivo):

## [S04] Prova (leitor 2)
- Título:
- Caso 1: número, depoimento, nome, cargo, empresa, fonte de confirmação
- Prova social: logos autorizados (nomes), número, fonte de confirmação
- Material de demonstração (se houver): o que é, rótulo "exemplo ilustrativo", o que substitui depois

## [S05] Objeções (leitor 3)
- Veículo: objeção → resposta → prova
- Interna: objeção → resposta → prova
- Externa: objeção → resposta → prova

## [S06] Para quem é / para quem não é
- É: 1) 2) 3)
- Não é: 1) 2)

## [S07] FAQ
- P1: / R1:
- P2: / R2:
- P3: / R3:
- P4: / R4:
- P5: / R5:

## [S08] Fechamento
- Título:
- Texto de apoio (uma ou duas linhas):
- Labels dos campos:
- Texto LGPD aprovado:
- O que acontece depois do clique (SLA):
- Mensagem de falha e link alternativo:
- Mensagens de erro (vazio, e-mail, telefone):
- Texto do botão em envio:

## [TY] Thank-you
- Confirmação com SLA:
- O que acontece agora (3 passos):
- Próximo degrau (título, texto, CTA, URL):
- Contato direto:

## Revisão Light Copy e copy de interface
- [ ] itens do checklist 4.5
- [ ] itens da 4.4
```

### D.4 `03_tracking.md`

```markdown
# Tracking | {projeto} | {canal} | v{N}

## Eventos (tabela da fase 7.2 preenchida para esta página)
| Evento | Gatilho real | Tipo | GA4 / GTM | Meta | Google Ads | CRM |
|---|---|---|---|---|---|---|

## GTM (fase 7.4): tags, triggers e variáveis a criar ou conferir
| Item | Tipo | Gatilho | Status |
|---|---|---|---|

## Catálogo de UTMs desta página
| Canal | utm_source | utm_medium | utm_campaign | utm_content | utm_term | URL completa |
|---|---|---|---|---|---|---|

## QA de tracking (fase 7.5)
| Item | Resultado | Evidência (print ou log) | Data |
|---|---|---|---|
```

### D.5 `05_perguntas_respondidas.md`

```markdown
# Perguntas e respostas | {projeto} | {canal} | v{N}
| Fase | Pergunta | Decisão que desbloqueava | Para quem | Resposta | Respondido por | Data | Onde entrou |
|---|---|---|---|---|---|---|---|
| 0 | ... | ... | Sarden / cliente | ... | ... | ... | 01_ficha.md, campo 5 |
| 2 | Qual direção visual? (cartões A, B, C, saída padrão) | fase 2 inteira | Sarden | ... | ... | ... | 01_ficha.md, contrato |
| 3 | Qual primeira dobra? (esboços 1, 2, 3) | fase 5.3 | Sarden | ... | ... | ... | 01_ficha.md, primeira dobra |
```
Regra: a tabela só registra perguntas respondidas. Pergunta sem resposta trava a fase; não entra em nenhum outro arquivo. Escolha delegada em palavras é registrada como resposta ("delegado; escolhido X pela evidência Y").

### D.6 `06_plano_de_teste.md`

```markdown
# Plano de teste | {projeto} | {canal} | v{N}
- Hipótese: se {mudança}, então {métrica} sobe porque {razão}
- Variável única testada:
- Variante A:
- Variante B (arquivo index-b.html ou bloco alternativo pronto):
- Métrica primária:
- Métrica de guarda (qualidade no CRM):
- Amostra mínima por variante:
- Janela:
- Critério de decisão:
```

### D.7 `README.md` (publicação)

```markdown
# Publicação | {projeto} | {canal} | v{N}

## Arquivos
- index.html, obrigado.html, assets/ (publicar na mesma pasta; caminhos relativos)

## Destino: {destino da ficha, campo 13}
1. Onde subir os arquivos e como (passo a passo do destino escolhido)
2. URL final e canonical conferidos
3. HTTPS ativo; redirecionamento de http e de www conferido

## GTM
- Container: {GTM_ID}
- Itens criados ou conferidos: lista de 03_tracking.md

## Formulário
- Mecanismo: {HubSpot Forms API portalId/formGuid | webhook URL | embed}
- Campos ocultos mapeados nas propriedades do CRM: lista

## Depois de publicar (mesmo dia)
- [ ] Envio de teste real, lead no CRM com UTM
- [ ] generate_lead no GA4 DebugView, uma vez
- [ ] Conversão de teste no Google Ads e no Events Manager (dedup conferida)
- [ ] PageSpeed Insights mobile na URL final
- [ ] `npx impeccable detect https://URL-FINAL/` com exit 0
- [ ] Pré-visualização do link no WhatsApp

## Changelog
| Versão | Data | O que mudou | Por quê |
|---|---|---|---|
```

### D.8 `DESIGN.md` (formato oficial DESIGN.md, escrito a partir do build)

```markdown
---
name: {cliente}
description: {uma linha: o mundo em uma frase}
colors:
  primaria: "{hex}"
  sobre-primaria: "{hex}"
  cta: "{hex}"
  cta-texto: "{hex}"
  fundo: "{hex}"
  superficie: "{hex}"
  texto: "{hex}"
  texto-suave: "{hex}"
  borda: "{hex}"
typography:
  display:
    fontFamily: "{fonte de título}, system-ui, sans-serif"
    fontSize: "clamp(1.875rem, 6vw, 2.75rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  body:
    fontFamily: "{fonte de texto}, system-ui, sans-serif"
    fontSize: "1rem"
    lineHeight: 1.5
rounded:
  md: "{raio}"
spacing:
  xs: "8px"
  sm: "16px"
  md: "24px"
  lg: "48px"
  xl: "96px"
components:
  button-cta:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.cta-texto}"
    rounded: "{rounded.md}"
    padding: "0 24px"
    height: "56px"
---

# Design System: {cliente}

## Overview
{Estrela-guia do mundo em uma metáfora nomeada; 2 ou 3 frases de filosofia; anti-referência confirmada (o que este mundo recusa).}

## Colors
{Papel de cada cor; estratégia (contida / comprometida / paleta completa / encharcada); onde a primária vira campo; regra de texto secundário sobre cor.}

## Typography
{Vozes de título e texto, origem e licença; escala de papéis; medida; tracking; o que não fazer.}

## Layout
{Largura máxima, gutters, breakpoints, escala de espaçamento, ritmo entre seções, posição do formulário por direção de dispositivo.}

## Elevation & Depth
{Sombra do mundo (deslocamento e desfoque) ou ausência dela; o que nunca entra (halo, sombra dura).}

## Shapes
{Raio de botões, campos e blocos; forma dos ícones (SVG, um peso de traço).}

## Components
{Botão de CTA (estados), campo e label, erro, lista-check, passos, prova, FAQ, barra fixa, header, rodapé: como cada um se desenha neste mundo.}

## Do's and Don'ts
{Cinco a oito linhas de cada lado, específicas deste cliente.}
```

### D.9 Cartão de direção (rodada 2) e esboço de primeira dobra (rodada 3)

```markdown
## Cartão {A|B|C|Saída padrão}: {nome do mundo}
- Tese: {a ideia que a página possui e o arranjo padrão que recusa}
- Paleta: {estratégia} · {3 a 5 cores com papel}
- Materiais e tipografia: {título: fonte} · {texto: fonte} · {assinatura reconhecível}
- Primeira dobra: {o que está onde, em que escala, onde fica a ação}
- O que faz pela conversão: {como serve o teste dos 3 segundos e a prova}
- Risco honesto: {inclusive "familiar demais" quando for o caso}
- Kind: assigned / alternate / canon

## Esboço {1|2|3}: {o que lidera}
- Topologia: {assimétrica / tipográfica / produto em funcionamento / objeto do mundo}
- Invariantes em 360×640 e 1440×900: headline, prova e CTA visíveis sem rolar (sim)
- Captura: docs/esbocos/esboco-{n}-mobile.png · docs/esbocos/esboco-{n}-desktop.png
- Teste da memória: {o que o visitante descreveria uma hora depois}
```

---

## ANEXO E | REFERÊNCIAS

### E.1 Arquivos do knowledge do Susano (consultar quando a fase pedir)
- `00_susano/biblioteca/brunson/dotcom_secrets.md`: pré-frame, temperatura, 5 variáveis do funil, a buyer is a buyer, Stack, 7 funis
- `00_susano/biblioteca/brunson/traffic_secrets.md`: Hook Story Offer, Searcher contra Scroller, 3 closes, retargeting em 3 buckets
- `00_susano/biblioteca/brunson/expert_secrets.md`: Big Domino, Epiphany Bridge, 3 crenças falsas, new opportunity, status, Perfect Webinar
- `00_susano/biblioteca/ladeira/lightcopy_gatilhos.md`: premissas, 3 leis, invisibilidade, Prova contra Prova Social, QFD, copy fraca, erros de oferta
- `00_susano/biblioteca/sean_ellis/hacking_growth.md`: desejo menos atrito, 3 funções da LP
- `00_susano/biblioteca/hormozi/100m_leads.md`: lead magnet (3 tipos), engaged lead
- `00_susano/biblioteca/erico_rocha/formula_lancamento.md`: top 10 objeções, escassez real, VSL auto-contido
- `00_susano/biblioteca/g4/traction_growth_vendas.md`: jornada mental do comprador, métodos por consciência
- `00_susano/dna/metodo/copy_e_headline.md`: 9 heads de copy, 10 elementos de headline
- `00_susano/referencias/analytics/tracking/snippets.md`, `00_susano/referencias/analytics/google_tag_manager.md`, `00_susano/referencias/analytics/tracking/pixels.md`, `00_susano/referencias/analytics/tracking/server_side.md`, `00_susano/referencias/analytics/ga4.md`, `00_susano/referencias/analytics/guia_profundo_web_analytics.md`: dataLayer antes do GTM, 7 métodos de form tracking, custom event no callback de sucesso, UTMs case-sensitive, CAPI com event_id, Enhanced Conversions
- `00_susano/referencias/plataformas/hubspot/dossie_mestre.md`: form shortening, propriedades, atribuição
- `00_susano/dna/metodo/diagnostico_de_funil.md` e `00_susano/referencias/performance/fundamentos_anuncios_performance.md`: sequência de diagnóstico
- `00_susano/referencias/go-to-market/experimentacao.md`: power analysis, testes de página

### E.2 Impeccable (camada de craft)
- Repositório: https://github.com/pbakaus/impeccable (Apache-2.0; versão lida: 4.6.0)
- Documentação: https://impeccable.style/docs/ · detector: https://impeccable.style/docs/detector
- Arquivos do kit citados neste playbook (`skill/SKILL.src.md` e `skill/reference/`): `craft-floor.md` (piso de qualidade, recusas), `new-work.md` (autoridade visual, direções, contrato de direção, build com compromisso, inspeção e acabamento), `mode-persuade.md` (regras do modo Persuade), `visualize.md` (três opções, um ponto de aprovação), `shape.md`, `layout.md`, `typeset.md`, `colorize.md`, `animate.md`, `clarify.md`, `polish.md`, `critique.md` (heurísticas de Nielsen 0 a 4), `audit.md` (5 dimensões), `init.md` (PRODUCT.md), `document.md` (DESIGN.md)
- Formato DESIGN.md: https://raw.githubusercontent.com/google-labs-code/design.md/main/docs/spec.md
- Skill de origem: Anthropic frontend-design, https://github.com/anthropics/skills/tree/main/skills/frontend-design

### E.3 Benchmarks e práticas de mercado (fonte e ano)
- Unbounce Conversion Benchmark Report 2024: mediana geral 6,6%; SaaS 3,8%; financeiro 8,3%; top 25% a partir de 11,4%; copy em nível de leitura de 5ª a 7ª série converte 11,1% contra 5,3% em nível profissional. https://unbounce.com/landing-pages/whats-a-good-conversion-rate/
- HubSpot (Dan Zarrella), 40 mil LPs: tipo do campo pesa mais que quantidade. https://blog.hubspot.com/blog/tabid/6307/bid/6746/which-types-of-form-fields-lower-landing-page-conversions.aspx
- Neil Patel, 404 e 833 LPs: 1 campo 18,2%; 2 campos 13,0%; 3 campos 11,5%; equilíbrio entre 4 e 6. https://neilpatel.com/marketing-stats/conversion-rate-by-form-fields/
- Google/Deloitte, Milliseconds Make Millions (2020): 0,1 s = +8,4% varejo, +21,6% progressão para envio de formulário em lead gen. https://web.dev/case-studies/milliseconds-make-millions
- Think with Google: 1 s → 10 s = +123% de bounce no mobile. https://thinkwithgoogle.com/marketing-strategies/app-and-mobile/mobile-page-speed-new-industry-benchmarks/
- LanderLab, guia 2026 (vendor, direcional): hierarquia de 8 estágios, CTA em 3 pontos, barra fixa mobile +14%, CTA em primeira pessoa +14%, multi-step. https://landerlab.io/blog/landing-page-best-practices
- LanderLab, presell pages 2026 (vendor): 5 formatos de bridge. https://landerlab.io/blog/presell-page-examples
- Hormozi, 100M Offers: equação de valor. https://www.supersummary.com/100m-offers/section-3-summary/

### E.4 Padrões técnicos públicos
- Core Web Vitals (LCP até 2,5 s, INP até 200 ms, CLS até 0,1): https://web.dev/articles/vitals
- PageSpeed Insights (medição mobile obrigatória antes da entrega): https://pagespeed.web.dev/
- WCAG 2.2: contraste 4,5:1 (SC 1.4.3), contraste de componentes 3:1 (SC 1.4.11), alvo mínimo 24×24 (SC 2.5.8), alvo 44×44 (SC 2.5.5): https://www.w3.org/TR/WCAG22/
- Apple Human Interface Guidelines, alvo de toque 44×44 pt: https://developer.apple.com/design/human-interface-guidelines/
- Validador de HTML do W3C: https://validator.w3.org/
- Google Tag Manager, instalação do snippet: https://developers.google.com/tag-platform/tag-manager/web
- HubSpot Forms API, envio de formulário (aceita requisição do navegador): https://developers.hubspot.com/docs/api-reference/legacy/marketing/forms/v3-legacy/submit-data-unauthenticated
- WhatsApp, clique para conversar (formato wa.me e mensagem pré-preenchida): https://whatsapp.com/faq/en/general/26000030
- Open Graph (pré-visualização de link): https://ogp.me/

### E.5 Exemplos de página por tipo (estrutura, não layout)
- Squeeze: https://www.rdstation.com/blog/materiais-educativos/ebooks/exemplos-de-landing-pages/
- Lead gen B2B: https://www.rdstation.com/demonstracao/
- Serviço B2C: https://www.contabilizei.com.br/parcerias/shopee
- Sales page: https://www.seedprod.com/best-sales-page-examples/
- Bridge e quiz: https://landerlab.io/blog/presell-page-examples
- Webinar: https://offers.hubspot.com/inbound-neil-patel e https://slack.com/events/achieving-hybrid-work-success-with-team-collaboration
- Trial: https://www.shopify.com/free-trial
- Thank-you: https://www.wordstream.com/blog/ws/2021/11/23/thank-you-page-examples
- Antes e depois com o Impeccable: https://impeccable.style/cases/neo-mirai
- Galerias: https://unbounce.com/?p=147039 · https://systeme.io/learn/landing-page-examples/ · https://swipepages.com/landing-page-inspiration/industry/saas/

---

## ANEXO F | DEFINIÇÃO DE PRONTO

Uma landing page está pronta para receber tráfego quando, e somente quando:
1. A conversão está escrita em uma linha e o evento medido dispara uma vez, no envio real, com `event_id`.
2. Canal, jornada e direção de dispositivo estão declarados com origem e refletidos na posição do formulário.
3. A v1 funciona por completo nos dois dispositivos, passou no teste da primeira tela em 360×640 e 1440×900 e no teste do polegar.
4. O CTA é único, em primeira pessoa, visível em qualquer ponto de rolagem (botão, barra fixa ou header, formulário) e é o elemento de maior contraste em qualquer campo.
5. Toda seção está no mapa de conexão e empurra para o CTA; o HTML não carrega estratégia.
6. O mundo visual é herdado do cliente ou travado pelo Sarden; o contrato de direção tem seis blocos sem clima; a primeira dobra travada passa no teste da memória; o teste de calibragem foi respondido.
7. Os tokens vêm do design system ou da direção; contraste medido; exceções de marca registradas; neutros tingidos; ícones em SVG; fontes auto-hospedadas.
8. Nenhum número, depoimento, logo ou resultado entrou sem confirmação do projeto; material de demonstração rotulado.
9. O HTML é válido, sem erro de console, sem placeholder, sem biblioteca além do GTM, e PageSpeed Insights mobile marca 90 ou mais.
10. O detector terminou com exit 0 (ou o checklist manual foi aplicado e declarado); a auditoria tem 16/20 ou mais sem P0 e P1.
11. A revisão de acabamento por agente separado terminou em "entregar", ou o Sarden decidiu por escrito após a segunda rodada.
12. O QA de tracking tem evidência para todos os itens; o lead de teste está no CRM com origem.
13. A thank-you tem SLA, próximo degrau e `noindex`.
14. O DESIGN.md do cliente foi escrito a partir do build e salvo onde a próxima página o encontra.
15. A variante B existe.
16. A data da análise de realidade está marcada.
17. Nenhum arquivo do pacote carrega marcador de pendência, verificação ou inferência; o log de perguntas mostra todas respondidas.

---

## ANEXO G | IMPECCABLE: INSTALAÇÃO, COMANDOS POR FASE, MODO SEM O KIT

### G.1 Instalação (agente com terminal: Claude Code, Cursor, Codex)

```bash
npx impeccable install            # na raiz do projeto da página; instala a skill, o hook e o detector
npx impeccable update             # atualizar
/impeccable init                  # dentro do agente: escreve PRODUCT.md com as respostas da fase 0
/impeccable hooks on              # hook que roda o detector a cada edição de arquivo de UI
```

O hook roda o detector a cada edição; com ele ativo, o agente age sobre os achados em vez de reauditar cada regra à mão. `[IMP]` craft-floor. Telemetria anônima do kit pode ser desligada com `npx impeccable telemetry off`.

### G.2 Comandos por fase

| Fase deste playbook | Comando do kit | Para quê |
|---|---|---|
| 0 Entender | `/impeccable init` | PRODUCT.md: verdade do produto (usuários, mecanismo, provas, restrições). Nunca visual. |
| 2 Mundo visual | `/impeccable document` (quando o cliente tem site coerente) | registra o mundo incumbente como DESIGN.md antes de construir |
| 2 Mundo visual | `/impeccable shape <página>` | entrevista e brief confirmado; a rodada de direções acontece dentro do fluxo new-work do kit |
| 3 Primeira dobra | `/impeccable generate 3 "primeira dobra"` (com servidor local) | três variantes da S01 para escolha no navegador |
| 5 HTML | `/impeccable typeset`, `layout`, `colorize`, `animate` (escopo: a página) | ajustes de tipo, ritmo, cor e o movimento autoral dentro do mundo |
| 4 e 6 Copy e formulário | `/impeccable clarify <formulário>` | labels, erros, estados |
| 5 HTML | `/impeccable adapt mobile` ou `desktop` | repensar a página para o outro dispositivo sem "escalar pixels" |
| 5 HTML | `/impeccable bolder <seção>` / `quieter <seção>` | uma seção que lê plana ou que grita, sem tocar o resto |
| 9 QA | `npx impeccable detect index.html obrigado.html` | 59 regras determinísticas, exit 0 obrigatório |
| 9 QA | `/impeccable audit` | 5 dimensões, 0 a 4, P0 a P3 |
| 9 QA | `/impeccable critique <página>` | revisão de design com dois subagentes isolados e heurísticas de Nielsen; alimenta a revisão de acabamento |
| 9 QA | `/impeccable polish` | passada final: estados, alinhamento, tokens, limpeza |
| 9 QA | `/impeccable optimize` | performance quando o PageSpeed reprova |
| 10 Entrega | `/impeccable document` | DESIGN.md a partir do build |
| 11 Realidade | `/impeccable live` | iteração visual de elementos no navegador para variantes de teste |

### G.3 Mapa de campos: entendimento e ficha → PRODUCT.md

| Seção do PRODUCT.md | Vem de |
|---|---|
| Platform | `web` |
| Stack | "static HTML/CSS" (este playbook) + destino de publicação (ficha, campo 13) |
| Users | ICP e leitor; cena de uso (00_entendimento) |
| Product Purpose | conversão única (ficha, campo 1) + o que o produto faz |
| Positioning | mecanismo único em uma frase (fase 2.2, item 1) |
| Operating Context | canal e jornada; onde o leitor está quando clica |
| Capabilities and Constraints | insumos técnicos; restrições de marca; o que precisa ficar intocado |
| Brand Commitments | autoridade visual (ficha, campo 15) e materiais de marca confirmados |
| Evidence on Hand | provas reais disponíveis, com status; ausências que não podem ser inventadas |
| Product Principles | 3 a 5 princípios derivados das respostas do Persuade |
| Accessibility & Inclusion | exigência específica do cliente, quando houver |

### G.4 Modo sem o kit (agente sem terminal, como o Susano no claude.ai)

Este playbook carrega inline tudo que o agente precisa aplicar: piso de craft (5.12), recusas (5.10), estratégia de cor e tipografia (2.3), contrato de direção (2.4), rodadas de decisão (0.7), inspeção (9.3) e revisão de acabamento (9.4). O que o kit automatiza e o modo sem kit faz à mão:
- detector → checklist manual da 9.1, declarado na entrega;
- `critique` com dois subagentes → revisão de acabamento por agente separado (9.4), ou nova sessão quando não há subagente;
- `generate`/`live` → os três esboços em HTML da fase 3, capturados e enviados;
- `document` → o template D.8 preenchido a partir do build.

Quando o Sarden ou um dev tem terminal, o detector roda no pacote entregue antes de publicar (README, "Depois de publicar").
