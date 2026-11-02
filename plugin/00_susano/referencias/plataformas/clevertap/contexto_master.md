---
id: ref-plataformas-clevertap-contexto-master
tipo: referencia
origem: base de conhecimento de CleverTap consolidada pelo Sarden a partir de três análises e da documentação oficial (coleta de 13/06/2026)
atualizado: 2026-11-01
revisao_pendente: Sarden (edição v0.3.0: ponteiros para arquivos locais do autor removidos; nota de migração sem setor)
---

# CLEVERTAP: BASE DE CONHECIMENTO MESTRA (SUSANO)

> **Tipo:** Base de conhecimento consolidada para instâncias Susano (Claude Projects)
> **Tema:** CleverTap (plataforma de Customer Engagement & Retention)
> **Gerado em:** 2026-06-13
> **Idioma:** PT-BR
> **Fontes consolidadas:** 5 documentos (3 relatórios analíticos independentes + 2 dumps brutos de documentação)
> **Convenção de marcadores anti-alucinação:** `[DADO AUSENTE]` `[INFERÊNCIA]` `[CONTRADIÇÃO]` `[VERIFICAR]` `[LACUNA]`
> **Convenção de tipo de evidência:** `[VENDOR]` (fonte CleverTap/parceiro) · `[INDEPENDENT]` (review/comparativo/fórum/mídia) · `[MISTO]`

---

## COMO USAR ESTE ARQUIVO

Este documento é a fonte única consolidada sobre a CleverTap para uso em Susanos. Ele triangula três pesquisas profundas independentes (cada uma com viés metodológico distinto) e extrai a referência técnica canônica de dois dumps de documentação oficial.

**Aviso de escopo importante (ler antes de carregar):**
- As duas bases brutas de origem (documentação oficial em inglês, 876 páginas, e site oficial em PT-BR, 307 páginas, coletados em 13/06/2026) somam volume inviável para um único arquivo e ficam fora deste repositório. Eles **não cabem** e **não devem** ser colados integralmente em um Claude Project.
- Este arquivo captura a estrutura canônica, os fatos verificáveis e toda a inteligência estratégica dos três relatórios. Para detalhe literal, a fonte é a documentação oficial ao vivo (ver Anexo B).
- Onde os relatórios divergem, a divergência está marcada com `[CONTRADIÇÃO]` em vez de escolher um lado. Isso é proposital: o Susano deve apresentar a tensão, não mascará-la.

**Regra de leitura das notas de usabilidade:** as notas de 1 a 5 em cada dimensão são `[INFERÊNCIA]` analítica dos autores das pesquisas, não métricas oficiais. Use-as como sinal direcional, não como dado duro.

---

## INVENTÁRIO DE FONTES (5 documentos de origem)

| # | Fonte de origem (fora deste repositório) | Natureza | Viés metodológico | Casos-âncora |
|---|---|---|---|---|
| 1 | F1: relatório de usabilidade (sumário executivo) | Relatório de usabilidade (estilo Perplexity, citações inline) | Equilibrado, foco em review platforms globais | TMOV, baz/Banco Azteca, Paysend, MOVii, PayU, Brevistay |
| 2 | F2: relatório analítico profundo | Relatório analítico profundo (estilo Gemini, notas de rodapé) | Crítico, foco Brasil/LatAm e fricções técnicas | RecargaPay, Food To Save, SAF Botafogo, Beep Saúde, Cartão de Todos, Guru, Rei do Pitaco |
| 3 | F3: relatório de pesquisa com citações verificadas | Relatório de pesquisa (estilo Claude, citações verificadas) | Equilibrado, foco em triangulação e governança | TMOV, Banco Promerica, APLAZO, Albo, Circles.Life, HUFT, Eatigo, Rummy Passion, VieON |
| 4 | Documentação oficial (docs e developer) | Dump de documentação técnica (docs.clevertap.com + developer.clevertap.com) | Verbatim oficial, 876 páginas, EN | Referência de produto/SDK/API |
| 5 | Site oficial em PT-BR | Dump do site institucional/produto PT-BR (clevertap.com/pt) | Verbatim oficial, 307 páginas, PT-BR | Posicionamento, planos, CleverAI, verticais |

Todas as fontes foram coletadas em 13/06/2026. O inventário completo de URLs por tipo `[VENDOR]`/`[INDEPENDENT]` está no Anexo A.

---
---

# PARTE I: IDENTIDADE E POSICIONAMENTO

## 1. O que é a CleverTap

**Veredito em uma linha:** plataforma "all-in-one, AI-first" de engajamento e retenção de clientes, mobile-first, que unifica num único produto a coleta de eventos comportamentais, analytics em tempo real, segmentação avançada e orquestração omnichannel de campanhas. `[VENDOR][INDEPENDENT]`

A CleverTap se define como plataforma de Customer Engagement and Retention projetada primariamente para marcas B2C com forte tração em apps e canais móveis. A fundação técnica unifica três camadas: uma Customer Data Platform (CDP), uma engine de analytics em tempo real e um motor de orquestração multicanal, tudo apoiado pelo banco de dados proprietário TesseractDB. `[VENDOR]`

Diferença central de posicionamento frente a ferramentas tradicionais de automação de marketing: o foco está na ativação instantânea e na captura de micro-momentos (ações ocorridas há segundos cruzadas com histórico estendido), não em sincronizações em lote (batch) e queries demoradas. `[VENDOR]`

Leitura analítica mais útil dos relatórios independentes: a CleverTap é menos "ferramenta genérica de campanhas" e mais "plataforma de retention operations para times de negócio que trabalham em cima de behavioral data". `[INFERÊNCIA][INDEPENDENT]`

## 2. História, fundação e estrutura societária

| Marco | Data | Detalhe |
|---|---|---|
| Fundação | Maio 2013 | Empresa criada (origem indiana, sede atual San Francisco / Mumbai) `[VENDOR]` |
| Primeiro cliente | Outubro 2013 | `[VENDOR]` |
| Investimento Seed | Julho 2014 | Accel `[VENDOR]` |
| Série A | Agosto 2015 | Sequoia e Accel `[VENDOR]` |
| Lançamento TechCrunch Disrupt | Setembro 2015 | `[VENDOR]` |
| Primeiro cliente Fortune 500 | Agosto 2016 | `[VENDOR]` |
| Série B | Abril 2019 | Sequoia, Accel e Tiger Global `[VENDOR]` |
| Série C | Outubro 2019 | Sequoia Índia e Tiger Global `[VENDOR]` |
| 10.000 apps no portfólio | Abril 2021 | `[VENDOR]` |
| Aquisição da Patch | Outubro 2021 | Funcionalidades de comunicação in-app incorporadas `[VENDOR]` |
| Aquisição da Leanplum | Maio 2022 | Martech construída para games, assinaturas e apps on-demand (grafada "Leanplun" no site PT, provável erro de digitação) `[VENDOR][VERIFICAR]` |
| Série D | Agosto 2022 | US$ 105 milhões, liderada pela CDPQ, com IIFL AMC Tech Fund, Tiger Global e Sequoia Índia `[VENDOR]` |

**Números agregados de empresa:** fundada em 2013; mais de 600 colaboradores; total de funding em torno de US$ 356 milhões; valuation de cerca de US$ 1,7 bilhão em 2022; atende 2.000+ marcas em mais de 100 países; presença física em cidades como São Paulo, Bogotá, Nova York, Londres, Dubai, Mumbai e Singapura. `[VENDOR]`

## 3. Posicionamento de mercado e reconhecimentos

- **Gartner Magic Quadrant for Personalization Engines 2026:** reconhecida como **Leader**. `[VENDOR]`
- **G2:** forte visibilidade, com dezenas de badges (Leader, Best Support, Best Results, Best ROI, Easiest Setup nos relatórios Winter/Spring/Summer 2025). Atenção: esses selos são compilados e divulgados pelo próprio vendor. `[VENDOR]`
- **Gartner Peer Insights / Multichannel Marketing Hubs / Mobile Marketing Platforms:** presença com avaliações verificadas (ver notas agregadas no item 18). `[INDEPENDENT]`

**Notas agregadas de review (triangulação das 3 pesquisas):**
- G2: 4,6/5 com cerca de 651 a 660 reviews. `[INDEPENDENT]`
- Gartner Peer Insights: 4,4/5 com cerca de 262 ratings. `[INDEPENDENT]`
- Capterra: 4,4/5 com cerca de 57 a 59 reviews verificados. `[INDEPENDENT]`
- GetApp: 4,4/5. `[INDEPENDENT]`
- Likelihood-to-recommend (TrustRadius e similares): em torno de 7,7 a 8,2/10. `[INDEPENDENT]`
- Perfil predominante dos reviewers: mid-market; no recorte G2 há cerca de 54 reviews classificados como Latin America. `[INDEPENDENT]`

## 4. Modelo de negócio e a métrica MAU

O modelo comercial é baseado em **Monthly Active Users (MAU)** e no volume de processamento de dados subjacente. A edição base "Essentials" começa em **US$ 75/mês** para até **5.000 usuários**, orientada a startups. `[VENDOR]`

Na prática, a complexidade funcional, os add-ons estruturais (ex.: exportação de dados) e a arquitetura de eventos posicionam o produto real quase exclusivamente no quadrante mid-market a enterprise. `[INFERÊNCIA][INDEPENDENT]`

**Fricção comercial documentada sobre MAU:** parte dos reviews critica o cálculo de MAU como inflado (ex.: contabilizar usuário que apenas abriu um email), elevando o custo efetivo. Um review chega a chamar o método de "morally wrong". `[INDEPENDENT]`

## 5. Presença em Brasil e LatAm

- Escritório físico em São Paulo e em Bogotá. `[VENDOR]`
- Parceria com o **Latam Fintech Hub** para impulsionar engajamento e retenção no ecossistema fintech de México, Brasil, Chile, Colômbia e Argentina. `[VENDOR][INDEPENDENT]`
- Participação em eventos regionais (ex.: gamescom Latam). `[VENDOR]`
- WhatsApp como canal de primeira classe, adaptado à realidade transacional brasileira (ver Parte II, item 9). `[VENDOR]`
- **Ressalva de evidência:** a maioria das provas de usabilidade ainda vem de mercados globais; reviews independentes locais em português são escassos. Tratar presença regional como sinal positivo, não como prova de excelência local em suporte/implantação. `[LACUNA][INDEPENDENT]`

---
---

# PARTE II: ARQUITETURA E PRODUTO (referência técnica canônica)

> Extraída da documentação e do site oficiais (coleta de 13/06/2026) e validada contra os três relatórios. Esta é a referência de "o que a plataforma é e faz".

## 6. TesseractDB (núcleo de dados)

TesseractDB é o banco de dados proprietário da CleverTap, descrito como "o primeiro banco de dados do mundo criado especificamente para engajamento e retenção". `[VENDOR]`

Características canônicas:
- Armazena **até 10.000 pontos de dados por usuário**. `[VENDOR]`
- Guarda **todo o histórico do usuário**, com janela de lookback estendida de **até uma década (10 anos)**. `[VENDOR]`
- Processa dados **em tempo real**: acesso instantâneo a bilhões de pontos de dados, zero latência, sem atrasos de lote, sem dependência de ferramentas de terceiros para agir sobre o dado. `[VENDOR]`
- Viabiliza cruzar ações ao vivo (Live Events) com comportamento passado (Past Behaviors) sem latência perceptível, para toda a base, sem amostragem. `[VENDOR][INDEPENDENT]`

**Nota de retenção por plano (do quadro de preços PT):** Essentials e Advanced retêm dados por 3 anos; Cutting Edge retém por 10 anos. O lookback completo de uma década, portanto, é recurso de plano superior. `[VENDOR][VERIFICAR]`

**Trade-off estrutural (insight crítico recorrente):** a mesma fundação que dá o maior ponto forte (analytics sem latência sobre histórico infinito) exige compromisso arquitetônico rígido. Qualquer descuido no planejamento de eventos/identidades torna a ferramenta intransigente depois. Ver fricções A2 e A5. `[INDEPENDENT]`

## 7. Modelo de dados

**Eventos.** Rastreiam ações dos usuários no app ou site (ex.: abrir app, ver produto, ouvir música, comprar, favoritar). Duas categorias: `[VENDOR]`
- **System events (eventos de sistema):** registrados automaticamente após integrar o SDK. Exemplos: App Installed (primeira abertura), App Launched (toda abertura, inclusive retorno ao foreground após 20 min de inatividade), App Uninstalled (rastreado via silent push enviado à base a cada 24h), Web Session Started, entre outros.
- **Custom events (eventos customizados):** definidos e rastreados pela marca via SDK ou API.

**Event properties (propriedades de evento).** Detalhes que descrevem a ação (ex.: no evento "Product viewed", propriedades como product name, category, price). Habilitam insights e segmentação por categoria/faixa de preço. `[VENDOR]`

**Distinção crítica para o operador.** Para extrair valor, é preciso dominar a diferença entre eventos de sistema, propriedades de evento e propriedades de perfil de usuário. Essa taxonomia é a principal barreira de entrada (ver A1). `[INDEPENDENT]`

**User profiles (perfis de usuário).** Perfil unificado por usuário, combinando atributos, histórico de eventos e dados de múltiplas fontes (web, CRM, app). A unificação de identidades (Identity Management) é etapa crítica e frágil: se mal arquitetada no momento zero, gera duplicidade entre usuários anônimos e logados. `[VENDOR][INDEPENDENT]`

## 8. CleverAI: Universo de Agentes Inteligentes

A camada de IA da CleverTap é organizada em torno do **CleverAI Decision Engine (Motor de Decisão CleverAI)**, descrito como o "cérebro" da operação, construído sobre fundação modular e integrável ao ecossistema de IA existente do cliente, apoiado pelo TesseractDB e pelo "Universo de dados" CleverAI. `[VENDOR]`

Quatro famílias de agentes autônomos que operam dentro das diretrizes e metas da marca: `[VENDOR]`

| Família | Papel |
|---|---|
| **Agentes de Estratégia** | Definem o plano de ação para metas de LTV; acionam e gerenciam outros agentes; sugerem caminhos mais inteligentes; aprendem e otimizam; mantêm contexto e ações em memória |
| **Agentes de Decisão** | Identificam produto, oferta e fluxo ideais por cliente; predizem intenção e prescrevem a melhor ação; analisam opções e sugerem inferências |
| **Agentes Criativos** | Geram cópia, criativos e templates personalizados; compreendem emoções, preferências e interesses; otimizam unindo criatividade e resultado |
| **Agentes de Ação** | Constroem e orquestram interações 1:1; colaboram mantendo controle dentro das diretrizes da marca; aprendem para sugerir a próxima melhor ação; recalibram com base nas metas |

Recursos e agentes nomeados associados (citados em docs/site): **IntelliNODE** (nó inteligente em Journeys), **Agente de Previsões / CleverAI Predictions** (segmentação preditiva), **Scribe** (integração de dados sem fricção), **CleverAI** (assistente conversacional / Ask AI no dashboard). `[VENDOR]`

## 9. Canais (omnichannel)

A plataforma documenta 13+ messaging channels. Lista canônica de canais e superfícies: `[VENDOR]`

- **Notificações Push (mobile)**
- **Mensagens In-App**
- **App Inbox (caixa de entrada do app)**
- **Web Push**
- **Web Pop-up**
- **Web Inbox (caixa de entrada da web)**
- **Web Native Display (display nativo da web)**
- **App Native Display (display nativo do app)**
- **Email**
- **SMS**
- **WhatsApp** (sempre como add-on/complemento em todos os planos)
- **RCS**
- **Webhooks**
- **Google Ads** (audiências)
- **Públicos do Facebook**

**WhatsApp em detalhe (crítico para Brasil/LatAm).** A CleverTap opera como **WhatsApp BSP** (Business Solution Provider) e também aceita providers externos via **Generic WhatsApp**. Suporta templates, botões iterativos e fluxos condicionais. É tratado como "first-class citizen" para o mercado transacional brasileiro. `[VENDOR]`

**RenderMax (entrega de push em Android).** Recurso que, segundo o vendor, eleva a render rate de push em dispositivos Android de baixo custo para até cerca de 90%, mantendo consumo de bateria abaixo de 0,1% com oito notificações diárias. Números baseados em comunicação do vendor (2022). `[VENDOR][VERIFICAR]`

**Limitação periférica de entregabilidade (independente).** Em dispositivos Android de fabricantes asiáticas com políticas agressivas de otimização de bateria, taxas de entrega de push caem, forçando rotas de fallback onerosas (SMS, WhatsApp) que pressionam margem. `[INDEPENDENT]`

## 10. Analytics e segmentação

Recursos canônicos de análise (das docs e do quadro de planos): `[VENDOR]`
- **Boards / Custom Dashboards** e dashboards pré-configurados: Today View, Mobile App View, Uninstalls View, Revenue View, NPS Board, Snapshot.
- **Cohorts** (incluindo Cohorts 2.0; modos avançados como Bracketed Cohorts, Cohorts não consolidadas, Curva de Usuário Avançada nos planos superiores).
- **Funnels** (Funnels 2.0).
- **Flows** (Flows 2.0): rastreamento de caminhos de usuário.
- **Pivots** (Pivots 2.0).
- **Trends** (Trends 2.0).
- **RFM (Recência, Frequência, Valor Monetário):** segmentação RFM nativa.
- **Segmentação:** psicográfica, comportamental, usuário ativo, baseada em intenção, lista personalizada, grupos de assinatura de email.
- **Recursos de análise:** eventos compostos, propriedades de eventos agregados, comparação de segmentos, comparação de eventos, funções e fórmulas, análise de sessão, rastreamento de desinstalação, perfil de usuário unificado.

**Diferencial competitivo central (consenso das 3 pesquisas):** segmentação em tempo real + analytics comportamental profundo é o ápice da plataforma. Marketers montam coortes ultra-granulares em segundos, cruzando gatilhos recentes com histórico vitalício, **sem depender de queries SQL** nem da equipe de dados. Comparativos independentes colocam a CleverTap à frente de Braze, MoEngage e Firebase em profundidade analítica nativa. `[INDEPENDENT]`

**Limitação citada:** manipulação granular de geolocalização ao vivo de alta variância (localizar usuários por mudanças instantâneas de zona/CEP) é fraca, enfraquecendo campanhas hiperlocais de última milha. `[INDEPENDENT]`

## 11. Orquestração: Journeys

**Journeys** é o builder visual de campanhas multi-etapa (lifecycle), com nós de condição, delays, A/B testing, channel routing e nós inteligentes (IntelliNODE, CleverAI Predictions). Permite jornadas complexas dentro de um canvas. `[VENDOR]`

**Fricção mais severa e recorrente da plataforma: lock-in pós-publicação.** Uma vez que a jornada entra em status "Running"/"Published", funções estruturais ficam travadas: não dá para alterar/adicionar nós no caminho, mudar entry triggers, nem alterar blocos centrais de segmentação. Apenas ajustes estéticos de texto e configurações periféricas são permitidos. Para corrigir lógica, a equipe é forçada a clonar a jornada, pausar a anterior e iniciar nova, o que quebra a continuidade analítica e gera entidades "fantasma" no painel. Confirmado de forma independente por dois dos três relatórios e pela própria documentação de Journey Operations. `[INDEPENDENT][VENDOR]`

**Latência em In-App.** Campanhas In-App podem demorar períodos aleatórios para renderizar ou para cessar após interrupção manual no painel. `[INDEPENDENT]`

## 12. Otimização de campanha

Recursos canônicos (docs e quadro de planos): `[VENDOR]`
- **A/B & Multivariate Testing** (testes A/B de mensagens).
- **Best Time Campaign / Melhor Hora para Envio.**
- **Send to All Devices (enviar para todos os dispositivos).**
- **Editor de Email** e templates básicos (apenas email no plano base).
- **Entrega Push Aprimorada (RenderMax).**
- **Messaging Frequency Caps (limites de frequência globais)** que blindam o usuário de spam multicanal.
- **Control Groups, Campaign Approval Workflow, Campaign Reports, Notification Delivery Options.**
- **Best Time / Geofencing / Regex / Constant Event Property campaigns.**
- **Lifecycle Optimizer (Otimizador do ciclo de vida):** apenas no plano Cutting Edge.

## 13. Personalização / Individualização

Recursos canônicos: recomendações de produto, boletins (newsletters), conteúdo vinculado (linked content), tags líquidas (Liquid tags), geofencing, personalização no horário de envio do catálogo (catalog send-time), campanha de propriedade constante. Hiperpersonalização é tema central do marketing CleverAI (ver item 8). `[VENDOR]`

## 14. Gestão de dados, importação e exportação

Recursos canônicos: `[VENDOR]`
- **Schema Design.**
- **Acesso API (importação e exportação via API), Report APIs, Real-Time Counts.**
- **Downloads e envios de CSV.**
- **Cloud Storage / Profile Exports.**
- **Exportações para AWS S3 (batch), AWS EventBridge, Google Cloud Platform (GCP), SFTP, Mixpanel, mParticle, Amplitude, Data Warehouse, Snowflake.**
- **Instâncias AWS localizadas.**

**Barreira comercial documentada: add-on "Cloud Export".** Para streaming contínuo e seguro de eventos para ambientes corporativos (S3, GCP, Snowflake), a CleverTap exige o aditivo **Cloud Export**, com cobrança de cerca de **10% adicionais sobre o plano base** contratado. Reviews descrevem isso como um "jardim murado" (walled garden) que aliena times de engenharia de dados. Número de 10% reportado por relatório independente; confirmar em contrato. `[INDEPENDENT][VERIFICAR]`

**Fricção de exportação operacional.** Relatórios padrão chegam por email em CSV considerado "messy/sujo", e extrair dados a nível de interação individual da jornada é descrito como árduo e confuso. Ver A7. `[INDEPENDENT]`

## 15. Integrações, SDKs e parceiros

**SDKs oficiais:** Android, iOS, Web, Flutter, React Native, Unity. Integração com **Segment** (Analytics-Kotlin, Analytics-Swift, Native Android/iOS, React-Native, Web). `[VENDOR]`

**Quick start oficial:** promete ver um evento no dashboard em menos de 10 minutos. Verdadeiro para "prova de vida", não para produção robusta. `[VENDOR][INDEPENDENT]`

**Fricções técnicas reais documentadas (issues públicos GitHub / Stack Overflow / fóruns):** `[INDEPENDENT]`
- Web SDK em SSR/Next.js: erro "HTMLElement is not defined", conflitos de CORS na ingestão, "Can't resolve crypto", JSON parse errors.
- Android SDK: ANRs (ActivityLifecycleCallback, in-app messages, IO em disco), NoClassDefFoundError, StrictMode violations, falhas intermitentes na coleta/armazenamento de tokens FCM (afeta entrega de push).
- iOS SDK: crashes ao abrir App Inbox com propriedades de evento complexas.
- Coexistência problemática com analytics paralelos (Google Analytics 360, Firebase nativo, Branch, AWS Pinpoint).
- Armadilhas de configuração: necessidade de setar região no Web SDK; enviar eventos para sair de "Integration pending".

**Parceiros / catálogo de integrações (docs):** Analytics Partners, Attribution Partners, Amazon EventBridge, Data Warehouse, Content Manager, entre outros. `[VENDOR]`

## 16. Planos e preços

Três edições. Estrutura de disponibilidade de recursos (do quadro de preços PT-BR; nomes de edição inferidos como Essentials / Advanced / Cutting Edge a partir de retenção de dados e do ponto de entrada US$ 75): `[VENDOR][INFERÊNCIA]`

| Recurso (amostra relevante) | Essentials | Advanced | Cutting Edge |
|---|:---:|:---:|:---:|
| Preço de entrada | US$ 75/mês (até 5k MAU) | sob consulta | sob consulta |
| Funis, Cohorts, Eventos, Análise de sessão, Perfil unificado | Sim | Sim | Sim |
| Pivots, Flows | Não | Sim | Sim |
| Cohorts avançadas, Eventos compostos, Comparação de segmentos, Funções/Fórmulas | Não | Sim | Sim |
| Push, In-App, App Inbox, Web Push, Web Pop-up, Web Inbox, Email, SMS, Webhooks | Sim | Sim | Sim |
| Web/App Native Display, Google Ads, Públicos do Facebook | Não | Sim | Sim |
| WhatsApp | Add-on | Add-on | Add-on |
| Segmentação RFM, Baseada em Intenção, Lista Personalizada | Parcial (RFM e Lista só Advanced+; Intenção só Cutting Edge) | Sim | Sim |
| Otimizador do ciclo de vida (Lifecycle Optimizer) | Não | Não | Sim |
| Recomendações de produto | Não | Não | Sim |
| Exportação GCP, S3 batch, EventBridge, SFTP, Mixpanel/mParticle/Amplitude, instâncias AWS localizadas | Não | Sim | Sim |
| 2FA, SSO, Acesso baseado em função | Sim | Sim | Sim |
| Acesso avançado por função, Fluxo de aprovação de campanha | Não | Sim | Sim |
| Política de retenção de dados | 3 anos | 3 anos | 10 anos |

**Add-ons relevantes:** WhatsApp, Email Add-on (no Essentials), Cloud Export (~10% do plano, ver item 14). `[VENDOR][VERIFICAR]`

`[LACUNA]` Os multiplicadores de preço por faixa de MAU em níveis milionários (especialmente LatAm) não são públicos. Exigir simulação formal em negociação.

## 17. Segurança e conformidade

**Certificações e conformidade atuais:** GDPR, CCPA, SOC 2 Tipo II, ISO 27001, HIPAA. Avaliadas por auditores independentes de terceiros. `[VENDOR]`

**Infraestrutura e controles:** `[VENDOR]`
- Dados armazenados em instâncias localizadas da AWS; data centers em conformidade; criptografia de dados em repouso e em trânsito.
- Controles de acesso: autenticação em dois fatores (2FA), acesso baseado em função (RBAC), acesso restrito por IP, fluxo de aprovação de campanhas.
- Portal de Confiança público: `trust.clevertap.com` (postura de segurança, relatórios de auditoria, políticas e controles).

**Implicação para LGPD (atenção do operador):** a hospedagem é AWS com instâncias localizadas e criptografia, mas a transferência/streaming de dados via Cloud Export para terceiros (S3, GCP, Snowflake) constitui compartilhamento de dados com terceiros. Em projetos com promessa de "dados não compartilhados", isso precisa de revisão de base legal e microcopy. `[INFERÊNCIA]`

# PARTE III: USABILIDADE (avaliação consolidada)

> Esta parte triangula as três avaliações analíticas (Fonte 1 / Sumário Executivo, Fonte 2 / Análise Profunda, Fonte 3 / Deep Research). Cada relatório pontuou dez dimensões de usabilidade (A1 a A10) em escala de 1 a 5. As notas divergem de forma relevante: a Fonte 2 (análise crítica, foco Brasil) é sistematicamente mais severa; a Fonte 1 é a mais generosa; a Fonte 3 fica no meio. O operador deve tratar a "nota consolidada" como faixa, não como número absoluto. `[MISTO]`

## 18. Síntese das dimensões A1 a A10

| Dimensão | F1 (Sumário) | F2 (Profunda) | F3 (Deep Res.) | Faixa consolidada | Leitura |
|---|:---:|:---:|:---:|:---:|---|
| A1. Facilidade de configuração inicial | 4 | 2 | 3 | 2 a 4 | "Prova de vida" rápida (menos de 10 min), mas configuração robusta de taxonomia de eventos é trabalhosa |
| A2. Curva de aprendizado | 3 | 2 | 3 | 2 a 3 | Suave no básico, íngreme ao explorar segmentação avançada, Flows e analytics compostos |
| A3. Clareza da interface | 3 | 2 | 3 | 2 a 3 | Densa, muitos menus, "polui" sob carga; melhora com familiaridade |
| A4. Criação de campanhas | 4 | 3 | 3 | 3 a 4 | Fluxo de campanha direto; orquestração multicanal é ponto forte |
| A5. Segmentação e targeting | 4 | 2 | 4 | 2 a 4 | Poder real-time sem SQL é elogiado; F2 critica resolução de identidade frágil |
| A6. Capacidades de analytics | 5 | 5 | 4 | 4 a 5 | Consenso de força máxima: Funnels, Cohorts, Flows, Pivots, RFM |
| A7. Relatórios e exportação | 3 | 2 | 2 | 2 a 3 | Consenso de fraqueza: exportação "bagunçada", Cloud Export pago, CSVs ruins |
| A8. Documentação e suporte | 4 | 2 | 3 | 2 a 4 | Docs amplas; F2 relata churn de CS/account manager no enterprise |
| A9. Integrações e SDKs | 4 | 3 | 3 | 3 a 4 | Cobertura ampla de SDKs; bugs reais em casos de borda (NextJS, iOS, Android) |
| A10. Confiabilidade e performance | 4 | (ranqueada) | 3 | 3 a 4 | Divergência forte; ver PARTE V (incidente MEC) |

`[CONTRADIÇÃO]` A nota de confiabilidade (A10) é o ponto de maior divergência entre fontes. A Fonte 3 cita "100% de uptime nos EUA Jan-Mar 2026" e ao mesmo tempo registra incidentes; a Fonte 2 documenta uma queda de 75h na região MEC em março de 2026. Não há benchmark independente unificado. Tratar como faixa e ver PARTE V.

## 19. Detalhe por dimensão (A1 a A10)

**A1. Facilidade de configuração inicial.** Há consenso de que um SDK pode ser instalado e gerar o primeiro evento ("proof of life") em menos de 10 minutos. `[INDEPENDENT]` A divergência está no que vem depois: definir a taxonomia de eventos, propriedades de usuário e estrutura de perfis exige planejamento e conhecimento de produto. A Fonte 2 considera esse esforço subestimado pelo marketing da CleverTap.

**A2. Curva de aprendizado.** Suave para tarefas centrais (push simples, segmento básico, campanha única). Íngreme ao avançar para Flows 2.0, eventos compostos, funções/fórmulas em analytics e resolução de identidade. As três fontes concordam que a plataforma "entrega valor rápido no básico e cobra esforço no avançado".

**A3. Clareza da interface.** Interface densa, com muitos módulos e menus. Sob volume alto de campanhas e dados, relatos de lentidão e poluição visual. Usuários experientes relatam que a navegação melhora muito após semanas de uso. `[MISTO]`

**A4. Criação de campanhas.** Fluxo de criação de campanha avulsa é direto. A orquestração multicanal (Journeys) e os limites de frequência (frequency caps) são citados como diferencial positivo. A fricção aparece na edição pós-publicação de jornadas (ver item 11).

**A5. Segmentação e targeting.** Forte: segmentação comportamental em tempo real sem necessidade de SQL é repetidamente elogiada. A Fonte 2 pondera que a resolução de identidade (unificação de perfis entre dispositivos/canais) pode ser frágil e gerar duplicidade ou fragmentação de perfil. `[MISTO]`

**A6. Capacidades de analytics.** Ponto mais forte do produto, com consenso entre as três fontes. Funnels 2.0, Cohorts 2.0, Flows 2.0, Pivots 2.0, Trends 2.0, RFM e segmentação preditiva/por intenção colocam a plataforma acima de concorrentes em profundidade analítica nativa.

**A7. Relatórios e exportação.** Ponto mais fraco com consenso. Exportação de dados descrita como "bagunçada"; exportações CSV de baixa qualidade; e o Cloud Export (streaming de eventos brutos para data warehouse) é um add-on pago estimado em ~10% do plano base. Operações que dependem criticamente de BI externo sentem essa limitação. `[VERIFICAR]` no percentual exato.

**A8. Documentação e suporte.** Documentação técnica ampla e geralmente boa (`docs.clevertap.com` e `developer.clevertap.com`, 876 páginas). A Fonte 2 registra um problema relevante no enterprise: rotatividade (churn) de Customer Success e account managers, gerando descontinuidade de relacionamento em contas grandes. `[VERIFICAR]`

**A9. Integrações e SDKs.** Cobertura ampla (Android, iOS, Web, Flutter, React Native, Unity, Segment). Há, porém, bugs reais documentados em casos de borda: SSR no NextJS (`HTMLElement is not defined`, CORS, crypto), perda de token FCM e ANRs no Android, crashes do App Inbox no iOS e conflitos de coexistência com Firebase/Branch/AWS Pinpoint. `[INDEPENDENT]`

**A10. Confiabilidade e performance.** Ver PARTE V. Resumo: orquestração e entrega funcionam bem no dia a dia para a maioria, mas há um incidente grave documentado (queda de 75h na região MEC, março de 2026) e divergência entre fontes sobre o quadro geral de uptime. `[CONTRADIÇÃO]`

# PARTE IV: FRICÇÕES E FORÇAS (ranqueadas e trianguladas)

## 20. Principais fricções (em ordem de severidade/frequência)

1. **Curva de aprendizado e complexidade da taxonomia de eventos após o básico.** A fricção número um por frequência. Definir e manter uma estrutura de eventos e propriedades coerente exige disciplina e conhecimento. Citada pelas três fontes. `[MISTO]`

2. **Lock-in de jornada após publicação.** Fricção estrutural mais citada como "dolorosa": uma vez que uma Journey está em execução (Running), não é possível editar nós, gatilhos ou segmentação; é preciso clonar, ajustar e republicar, perdendo o histórico de execução da versão anterior. Confirmada por duas das três fontes e pela documentação. `[INDEPENDENT]`

3. **Relatórios e exportação fracos, com pedágio do Cloud Export.** Exportação "bagunçada", CSVs ruins e dependência de um add-on pago (~10% do plano) para streaming de dados brutos. Impacta operações orientadas a BI/data warehouse. `[VENDOR][VERIFICAR]` no percentual.

4. **Interface densa e lenta sob carga, com lacunas de governança de UX.** Muitos menus, poluição visual sob volume e relatos de lentidão. Inclui lacunas na UX de governança de webhooks e aprovações. `[MISTO]`

5. **Bugs de SDK em casos de borda e entregabilidade de push em Android asiático.** NextJS SSR, iOS App Inbox, Android FCM/ANR e conflitos de coexistência. Em mercados asiáticos com Android fragmentado, a entregabilidade de push exige atenção (mitigada parcialmente pelo RenderMax). `[INDEPENDENT]`

## 21. Principais forças (em ordem de relevância)

1. **Segmentação em tempo real e analytics comportamental sem SQL.** O maior diferencial. Marketing opera segmentação e análise profunda sem depender de engenharia de dados. Consenso entre as três fontes. `[INDEPENDENT]`

2. **Journeys e orquestração omnichannel com limites de frequência.** Construtor visual de jornadas multicanal com controle de frequência e fadiga, cobrindo 13+ canais a partir de uma única plataforma. `[MISTO]`

3. **Centralização de analytics e engajamento numa só plataforma.** Reduz o número de ferramentas (analytics de produto + CRM de marketing + orquestração) e o custo de integração entre elas. `[INFERÊNCIA]`

4. **Boa usabilidade para as tarefas centrais.** Para o caso de uso mais comum (engajar usuários de app via push/in-app com segmentação comportamental), a curva inicial é suave e o tempo até o primeiro valor é curto. `[MISTO]`

5. **Custo-benefício frente ao Braze.** Posicionada como alternativa mais acessível ao Braze em capacidade analítica nativa comparável ou superior, especialmente para mid-market. `[VENDOR]` no enquadramento de preço; `[INDEPENDENT]` na comparação de analytics.

# PARTE V: CONFIABILIDADE E INCIDENTES

## 22. Quadro de confiabilidade (com contradição entre fontes)

`[CONTRADIÇÃO]` As fontes divergem sobre o quadro de uptime e devem ser lidas em conjunto, não isoladamente:

- **Fonte 2 (Análise Profunda):** documenta uma queda (outage) de aproximadamente 75 horas na região MEC (Middle East / monitoramento via IsDown e StatusGator) em março de 2026, além de instabilidades pontuais relatadas em regiões da Europa entre 2025 e 2026. `[VERIFICAR]`
- **Fonte 3 (Deep Research):** registra o mesmo incidente da região MEC em março de 2026 e uma falha no módulo de atualização de segmentos (segment-refresh), mas também reporta "100% de uptime nos EUA entre janeiro e março de 2026" e status "All Systems Operational" na página oficial. `[VERIFICAR]`
- **Leitura para o operador:** o incidente da região MEC em março de 2026 é o ponto de maior consenso entre as duas fontes que tratam de confiabilidade. O quadro geral de uptime aparenta ser regionalizado (uma região pode cair sem afetar as demais). Não há benchmark de uptime de terceiro independente e unificado. Para projetos com SLA crítico, exigir o status page histórico e cláusula contratual de SLA. `[LACUNA]`

## 23. RenderMax e entregabilidade de push

`[VENDOR][VERIFICAR]` A CleverTap divulga o RenderMax como tecnologia para elevar a taxa de renderização de push em Android para cerca de 90%, com impacto declarado inferior a 0,1% de bateria a cada 8 notificações (números de comunicação do fornecedor, ~2022). Não há verificação independente desses percentuais nas fontes. Em mercados com Android fragmentado (sul/sudeste asiático), a entregabilidade de push é um tema operacional real e o RenderMax é o mitigador oferecido.

## 24. Página de status e monitoramento

Página de status oficial e portal de confiança (`trust.clevertap.com`) existem e devem ser usados como fonte primária de incidentes. Ferramentas de terceiros citadas pelas fontes para histórico de incidentes: IsDown e StatusGator. `[INDEPENDENT]`

# PARTE VI: CASOS DE USO E ESTUDOS DE CASO

## 25. Principais trabalhos a resolver (jobs-to-be-done)

A plataforma é contratada predominantemente para: `[INFERÊNCIA]` consolidada das três fontes
- Aumentar ativação e conversão de novos usuários (onboarding comportamental).
- Aumentar retenção e reduzir churn via jornadas de ciclo de vida.
- Recuperar carrinho abandonado e reativar usuários dormentes.
- Orquestrar comunicação omnichannel (push, in-app, email, WhatsApp, SMS) com controle de frequência.
- Substituir/centralizar um stack fragmentado de analytics de produto + ferramenta de campanha.
- Personalizar conteúdo e ofertas em tempo real com base em comportamento.

## 26. Padrões por vertical

- **Fintech / BFSI:** ativação de cadastro, conversão de KYC/primeiro uso, ofertas de crédito, reengajamento transacional. Casos: RecargaPay, baz/Banco Azteca, Paysend, MOVii, PayU, Banco Promerica, APLAZO, Maya, Albo, M-KOPA, Guru Investimentos.
- **E-commerce / varejo:** carrinho abandonado, recomendação de produto, RFM, campanhas sazonais. Casos: Cartão de Todos, HUFT (Heads Up For Tails), Libas, BloomingWear, AJIO, Tata StarQuik.
- **Gaming / fantasy / real-money gaming:** stickiness diário, retenção D30, torneios, depósitos. Casos: Rei do Pitaco, Rummy Passion, MPL, WinZO, MobilityWare.
- **Mídia / streaming / assinatura:** engajamento de conteúdo, conversão de assinatura, CTR de push. Casos: VieON, SonyLIV, The Hindu, JioSaavn, MX Player.
- **Viagem / hospitalidade:** conversão de reserva, recuperação de busca, fidelidade. Casos: Brevistay, Eatigo, Cleartrip.
- **Food delivery / restaurantes:** ativação, recompra, recuperação. Casos: Food To Save, Faasos, Chakkizza, Shawarmer.
- **Telecom:** reengajamento, recarga, redução de churn. Casos: Circles.Life, Banglalink, Ooredoo.
- **Saúde:** ativação sazonal, NPS, jornadas de cuidado. Caso: Beep Saúde.
- **Esporte / clube (SAF):** monetização de torcida, ecommerce, CRM de fãs. Caso: SAF Botafogo.

## 27. Tabela mestra de estudos de caso (consolidada das três fontes)

> Todos os números de uplift abaixo são divulgados pelo fornecedor ou pelos próprios clientes em materiais da CleverTap, salvo indicação. Tratar como `[VENDOR]` por padrão. Verificar antes de citar a clientes.

| Cliente | Vertical | País/Região | Resultados divulgados | Fonte | Flag |
|---|---|---|---|---|---|
| TMOV | Mobilidade/Fintech | LatAm | +187% install-to-registration; +55% DAUs; 16% via indicação (refer-a-friend) | F1 + F3 | `[VENDOR]` |
| baz (Banco Azteca) | Fintech/BFSI | México | Engajamento e conversão (métricas em material do fornecedor) | F1 | `[VENDOR][LACUNA]` |
| Paysend | Fintech | Global/LatAm | Reengajamento e ativação (métricas em material do fornecedor) | F1 | `[VENDOR][LACUNA]` |
| MOVii | Fintech | Colômbia | Conversão e reengajamento (métricas em material do fornecedor) | F1 | `[VENDOR][LACUNA]` |
| PayU | Fintech/Pagamentos | Global/LatAm | Conversão de pagamento (métricas em material do fornecedor) | F1 | `[VENDOR][LACUNA]` |
| Brevistay | Viagem/Hospitalidade | Índia | Conversão de reserva (métricas em material do fornecedor) | F1 | `[VENDOR][LACUNA]` |
| RecargaPay | Fintech | Brasil | +50% conversão de registros; +100% em operações | F2 | `[VENDOR]` |
| Food To Save | Food/Antidesperdício | Brasil | -66% no tempo de registro até a compra; +68% de ativação | F2 | `[VENDOR]` |
| SAF Botafogo | Esporte/Clube | Brasil | ROI de 6,83x; 51% da receita de ecommerce via CRM | F2 | `[VENDOR]` |
| Beep Saúde | Saúde | Brasil | NPS 95; aumento de ~150x na base em pico sazonal | F2 | `[VENDOR][VERIFICAR]` |
| Cartão de Todos | E-commerce/Benefícios | Brasil | 20,4% de conversão em carrinho abandonado; +400% operacional; +2M MAU | F2 | `[VENDOR]` |
| Guru Investimentos | Fintech/Investimentos | Brasil | "+111.912% de ativações" (valor implausível, provável erro de base ou recorte) | F2 | `[VERIFICAR]` |
| Rei do Pitaco | Gaming/Fantasy | Brasil | +50% de retenção | F2 | `[VENDOR]` |
| Banco Promerica | Fintech/BFSI | Guatemala | +105% em desembolsos (disbursements) usando deep links | F3 | `[VENDOR]` |
| APLAZO | Fintech/BNPL | México | +60% recuperação de carrinho; -94% de trabalho operacional; +7% compra de pacote | F3 | `[VENDOR]` |
| Circles.Life | Telecom | Singapura/Ásia | 5x volume de campanhas; equipe de 4 para 1; -10% de churn | F3 | `[VENDOR]` |
| HUFT (Heads Up For Tails) | E-commerce/Pet | Índia | 4x receita atribuída a CRM | F3 | `[VENDOR]` |
| Eatigo | Viagem/Reservas/Food | Sudeste Asiático | 2x conversão; +100% em transações brutas | F3 | `[VENDOR]` |
| Rummy Passion | Real-money gaming | Índia | +23% de stickiness; +41% de retenção D30 | F3 | `[VENDOR]` |
| VieON | Mídia/Streaming | Vietnã | +10% engajamento; +12% checkout; 2x CTR de push | F3 | `[VENDOR]` |

`[LACUNA]` Os seguintes nomes aparecem como exemplos por vertical na Fonte 3, sem métricas detalhadas: MPL, WinZO, MobilityWare, SonyLIV, The Hindu, JioSaavn, MX Player, Cleartrip, Faasos, Chakkizza, Shawarmer, Banglalink, Ooredoo, M-KOPA, Maya, Albo, Libas, BloomingWear, AJIO, Tata StarQuik. Úteis como prova social por setor; não citar números.

## 28. Foco Brasil e LatAm (subseção prioritária)

Esta é a subseção mais relevante para operações com clientes no Brasil e na LatAm.

**Números de caso divulgados pela CleverTap.** São referência de fornecedor `[VENDOR]`, não dado independente: validar a metodologia antes de usar qualquer um como benchmark em proposta. `[VERIFICAR]`

**Casos brasileiros com métricas (todos `[VENDOR]`):** RecargaPay, Food To Save, SAF Botafogo, Beep Saúde, Cartão de Todos, Guru Investimentos (com a ressalva do número implausível), Rei do Pitaco.

**Casos LatAm com métricas (todos `[VENDOR]`):** TMOV, Banco Promerica (Guatemala), APLAZO (México), baz/Banco Azteca (México), MOVii (Colômbia).

**Leitura crítica (Fonte 2):** apesar do volume de casos brasileiros, há poucas métricas brasileiras/LatAm recentes e independentes (não divulgadas pelo fornecedor). A prova social regional é forte; a verificação independente é fraca. `[LACUNA]`

# PARTE VII: ANÁLISE COMPETITIVA

## 29. CleverTap frente aos principais concorrentes

> Comparações trianguladas das três fontes. Onde uma fonte não aprofunda, marca-se `[LACUNA]`.

**CleverTap vs Braze.**
- Braze: construtor de jornadas Canvas maduro, forte em iteração e experimentação, e em casos enterprise de larga escala. Percebido como mais caro.
- CleverTap: analytics nativo mais profundo (Funnels, Cohorts, Flows, Pivots, RFM) e custo-benefício melhor para mid-market. O Braze é frequentemente percebido como tendo analytics nativo mais raso, dependente de exportar para BI externo.
- Enquadramento: CleverTap é a alternativa "analytics-first e mais acessível" ao Braze. `[VENDOR]` no preço, `[INDEPENDENT]` na comparação de analytics.

**CleverTap vs MoEngage.**
- O comparável mais próximo no mid-market. Ambos focam engajamento de app, segmentação comportamental e omnichannel.
- Diferença citada: limites de janela de dados no MoEngage (relatos de limitação em ~30 dias em certos recortes/edições) versus a proposta de histórico longo do TesseractDB na CleverTap (até 10 anos no plano superior). `[VERIFICAR]`
- Decisão geralmente cai em preço, suporte regional e profundidade de analytics. `[MISTO]`

**CleverTap vs Insider.**
- Insider: forte em personalização web e ecommerce, com recursos de personalização de site e recomendação. `[LACUNA]` na Fonte 1 para comparação profunda.
- CleverTap: mais forte em app-led e analytics comportamental; Insider mais forte em web/ecommerce de catálogo. Para operações web-first de varejo, Insider tende a competir bem. `[INFERÊNCIA]`

**CleverTap vs OneSignal.**
- OneSignal: mais simples e barato, foco em push/mensageria. Não é uma plataforma de CRM de ciclo de vida completa.
- CleverTap: muito mais profunda em segmentação, analytics e orquestração. Quem só precisa de push básico tende a achar a CleverTap cara e complexa demais. `[MISTO]`

**CleverTap vs Firebase.**
- Firebase: primitivos para desenvolvedores (mensageria FCM, analytics básico), gratuito ou de baixo custo, forte em times de engenharia. Não é um CRM de marketing de ciclo de vida.
- CleverTap: plataforma de engajamento/CRM para times de marketing, com orquestração e analytics de negócio. Firebase compete no "começo barato"; perde quando a operação de marketing amadurece. `[INFERÊNCIA]`

## 30. Resumo competitivo (uma linha cada)

| Concorrente | Quando ele ganha | Quando a CleverTap ganha |
|---|---|---|
| Braze | Enterprise de larga escala, orçamento maior, iteração via Canvas | Mid-market, analytics nativo profundo, melhor custo |
| MoEngage | Preço/suporte regional favoráveis, caso simples | Histórico de dados longo, profundidade analítica |
| Insider | Web-first, ecommerce de catálogo, personalização de site | App-led, analytics comportamental, omnichannel app |
| OneSignal | Só push básico, orçamento mínimo | Ciclo de vida completo, segmentação e analytics |
| Firebase | Time de engenharia, custo zero, primitivos | Operação de marketing madura, CRM de ciclo de vida |

# PARTE VIII: VEREDITO DE ADEQUAÇÃO (fit)

## 31. Melhor adequação (best-fit)

A CleverTap tende a ser a escolha certa quando a operação reúne: `[INFERÊNCIA]` consolidada
- Negócio B2C app-led (ou app-first com web complementar), mid-market a enterprise.
- Mercado em Brasil/LatAm, Sudeste Asiático, Oriente Médio ou Índia (onde a CleverTap tem presença e casos).
- Verticais de fintech, ecommerce, food delivery, gaming ou mídia/assinatura.
- Disponibilidade de algum suporte de engenharia para instrumentar SDKs e taxonomia de eventos.
- Desejo de consolidar analytics de produto + CRM de marketing + orquestração numa só plataforma.
- Necessidade de segmentação comportamental em tempo real sem depender de SQL/engenharia de dados para cada análise.

## 32. Pior adequação (worst-fit)

A CleverTap tende a ser a escolha errada quando a operação é: `[INFERÊNCIA]` consolidada
- Web-first pura, sem app, com foco em personalização de site e catálogo (avaliar Insider).
- Sem qualquer suporte de engenharia para instrumentar a plataforma.
- Necessidade apenas de push básico e barato (avaliar OneSignal).
- Criticamente dependente de exportação de dados e BI externo (o pedágio do Cloud Export e a exportação fraca pesam).
- Dependente de uptime de missão crítica com SLA rígido sem cláusula contratual (ver incidente MEC, PARTE V).

## 33. Recomendação por contexto (resumo acionável)

- **Operação de marketing madura, app-led, LatAm, quer analytics + CRM juntos:** forte candidata. Avançar.
- **Mid-market comparando com MoEngage:** decidir por preço, suporte regional e histórico de dados. Pedir POC.
- **Quer só push barato:** provavelmente cara/complexa demais. Avaliar OneSignal.
- **Web/ecommerce de catálogo:** comparar lado a lado com Insider antes de decidir.
- **BI-crítico:** orçar o Cloud Export desde o início e validar a qualidade de exportação numa POC.
- **SLA crítico:** exigir histórico de status page e cláusula de SLA contratual antes de fechar.

# PARTE IX: LACUNAS CONSOLIDADAS

## 34. O que esta base ainda não cobre (e o operador deve buscar)

`[LACUNA]` Lacunas estruturais identificadas no cruzamento das três fontes:
- Poucas métricas brasileiras/LatAm recentes e verificadas de forma independente (a maioria é divulgada pelo fornecedor).
- Ausência de benchmark independente e unificado de entregabilidade de push e de uptime (os números de RenderMax e de uptime são do fornecedor ou regionais).
- Estudos de caso predominantemente conduzidos/divulgados pelo fornecedor; faltam avaliações neutras de terceiros com metodologia transparente.
- Opacidade de preços enterprise: multiplicadores por faixa de MAU em níveis milionários não são públicos, sobretudo para LatAm.
- Ambiguidade de recursos por edição (Essentials/Advanced/Cutting Edge) nas avaliações de usuários: nem sempre fica claro qual recurso pertence a qual plano.
- Metodologia por trás de números de uplift altos (ex.: Guru +111.912%, Beep +150x) não é detalhada e precisa de verificação antes de uso externo.

# ANEXO A: INVENTÁRIO DE FONTES E URLS

## A.1 Natureza das fontes

| Fonte | Tipo | Viés/Natureza | Classificação de evidência |
|---|---|---|---|
| F1: Sumário Executivo | Relatório de usabilidade (estilo Perplexity) | Equilibrado, plataformas globais de review | `[MISTO]` |
| F2: Análise Profunda | Análise crítica (estilo Gemini) | Crítico, foco Brasil/LatAm | `[MISTO]` tende a `[INDEPENDENT]` no tom |
| F3: Deep Research | Relatório triangulado (estilo Claude) | Equilibrado, foco governança/triangulação | `[MISTO]` |
| Master EN (docs) | Documentação oficial verbatim | Fonte primária do fornecedor | `[VENDOR]` factual |
| Master PT (site) | Site institucional verbatim | Marketing do fornecedor | `[VENDOR]` |

## A.2 Domínios e portais citados

- `docs.clevertap.com` e `developer.clevertap.com`: documentação técnica oficial (876 páginas no master EN). `[VENDOR]` factual.
- `clevertap.com/pt`: site institucional e blog em PT-BR (307 páginas no master PT). `[VENDOR]`.
- `trust.clevertap.com`: portal de confiança e segurança. `[VENDOR]` factual.
- Página de status oficial da CleverTap: incidentes e uptime. `[VENDOR]` factual.
- G2, Gartner Peer Insights, Capterra, GetApp, TrustRadius: plataformas de review. `[INDEPENDENT]` (agregado de usuários).
- Gartner Magic Quadrant (Personalization Engines 2026): analista. `[INDEPENDENT]`.
- IsDown, StatusGator: monitoramento de incidentes de terceiros. `[INDEPENDENT]`.

> Observação: as três análises de origem traziam URLs específicas; elas não estão neste repositório. Para auditoria fina de uma afirmação, conferir na documentação oficial da CleverTap ao vivo e registrar a data.

# ANEXO B: SOBRE OS DOIS MASTERS BRUTOS (não embutidos)

## B.1 Por que não estão embutidos

As duas bases brutas de origem são grandes demais para qualquer contexto de agente e não estão no repositório:
- documentação oficial verbatim, 876 páginas, cerca de 328 mil linhas, em inglês;
- site oficial em PT-BR verbatim, 307 páginas, cerca de 61 mil linhas.

Tentar colá-los inteiros estoura o contexto e degrada o desempenho do agente. Esta base mestra já extraiu deles a referência canônica de produto, técnica e de planos (PARTES I, II e o item 16).

## B.2 Como usá-los quando necessário

Consultar a documentação oficial ao vivo como fonte de detalhe ("lookup"). Quando o operador precisar de um detalhe muito específico (ex.: payload exato de um endpoint, comportamento de um SDK, texto literal de uma página de produto), abrir o master correspondente e fazer busca direcionada (grep/Ctrl+F) pelo termo. Não carregar o arquivo inteiro no agente.

## B.3 Avisos sobre o conteúdo bruto

- A coleta em inglês continha, além das docs, blocos de marketing em PT e um blob de JavaScript minificado de widget; ao buscar nomes de planos e preços na documentação, ignorar conteúdo de widget para evitar falsos positivos.
- Ambos são verbatim e datados da coleta (13/06/2026). Funcionalidades e preços mudam; revalidar contra o site/docs ao vivo antes de decisões contratuais.

---

> FIM DA BASE DE CONHECIMENTO MESTRA. Manter os marcadores de anti-alucinação ao derivar respostas desta base. Diante de conflito entre fontes, expor o conflito (não escolher um lado em silêncio). Diante de número de fornecedor, sinalizar `[VENDOR]` ao usuário. Diante de lacuna, dizer `[LACUNA]` em vez de inventar.

---

## NOTAS DA MIGRAÇÃO (2026-11-01)

- v0.1.6: um case divulgado pelo fornecedor saiu das listas de casos por ordem do Sarden (nome ligado à operação dele). As listas seguem como prova social de fornecedor, `[VENDOR]`, sem dado de cliente do Sarden.
