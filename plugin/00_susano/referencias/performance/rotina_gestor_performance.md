---
id: ref-perf-rotina-gestor
tipo: referencia
autor: Sarden
origem: Notion do Sarden: 'Guia Operacional Performace' (playbook, 28/03/2026)
atualizado: 2026-11-01
revisao_pendente: Sarden (edição v0.3.0: nota de defaults, papéis genéricos, CRM genérico com anexo HubSpot, dicionário citado, nomenclatura de produto marcada)
---

# Rotina do gestor de performance: diário, semanal, periódico e gatilhos

> Uso: O método operacional do Sarden para gestão de mídia paga: o funil completo por canal (impressão até Won) como ferramenta de decisão, o pipeline (CRM) como fonte da verdade, e quatro blocos de rotina. Usar para montar a rotina de um gestor, auditar uma operação ou diagnosticar queda. O bloco diário em formato de checklist está em `00_susano/referencias/performance/checklist_diario_gestor.md`.

> Todos os thresholds deste arquivo (frequência, discrepância pixel × CRM, LTV:CAC, passo de escala, view rate, taxas por etapa) são **defaults operacionais do método**, a calibrar por frente e registrar em `20_<frente>/<slug>/decisoes.md`; nenhum é benchmark de mercado. Definições de lead, MQL, SQL, CAC e CPL: `00_susano/dna/metodo/dicionario.md`. Papéis: "gestor da frente" e "liderança de growth" são os papéis de escalonamento do método; cada organização mapeia para os seus em `10_<org>/time/`. CRM: o método vale para qualquer CRM; o específico de CRM fica no anexo do fim.

> **🚨 O funil completo por canal : [Impressão até Won] essa é ferramenta de decisão. Tudo começa ali, da contexto e conclusão.**
>
> → O gestor que não sabe responder "onde está a maior queda no funil de cada canal essa semana?" Não está operando.
>
> → A fonte de verdade não é a plataforma, É O PIPELINE no CRM.

## 1. POR QUE ESSA ROTINA EXISTE

O gestor de performance é um alocador de capital. O dinheiro investido em mídia compra dados e inteligência sobre quem converte e quem não converte.

A rotina existe para três coisas:

- [ ] Nada está quebrado (dinheiro não está sendo queimado por erro técnico)
- [ ] O funil inteiro está visível, da impressão até o deal Won,  por canal
- [ ] Cada semana produz decisões ancoradas em dado, não em feeling

**→ OBS: O eixo central de tudo é o funil completo, por canal:**

> **Impressão → Clique → Visita LP → Lead → MQL → SQL → Opp → Won**

Cada transição tem uma taxa de conversão. O trabalho do gestor é saber onde cada canal está quebrando e agir na quebra certa.

## 2. BLOCO 1: ABERTURA DO DIA (30-40 min)

> 🚨 **Regra Absoluta:** não tomar decisão de pausar, escalar ou trocar criativo com base em um dia de dado. O algoritmo precisa de tempo.

Pergunta-guia: **"alguma coisa quebrou ou saiu do padrão?"**

---

### 2.1 Checar se as campanhas estão rodando

> 💡 **Por que:** campanhas pausam silenciosamente. Cada hora parada é dinheiro que não compra dados e aprendizado interrompido.

**Meta Ads Manager**

- [ ] Campanhas ativas com status "Ativa" e entregando
- [ ] Notificações: reprovação de anúncio, restrição de conta, limite de pagamento
- [ ] Gasto diário no pace esperado (se budget é R$ 100 e às 14h gastou R$ 20, algo restringe entrega)

**Google Ads**

- [ ] Status das campanhas: "Ativa", "Limitada por orçamento", "Limitada por lance"
- [ ] Notificações: reprovações, alertas de política
- [ ] Search: Impression Share: se caiu drasticamente, perdeu leilão ou budget acabou cedo

**TikTok Ads Manager**

- [ ] Status das campanhas: TikTok reprova criativos com mais frequência que Meta, checar todo dia
- [ ] Spending on pace: se muito abaixo do budget, pode ser público restrito ou bid baixo
- [ ] Events Manager (Assets → Events): Pixel e/ou Events API reportando eventos? Se parou, campanhas otimizam no vazio

**LinkedIn Ads**

- [ ] Entrega e pacing de budget
- [ ] Volume de impressões: audiência pequena satura rápido no LinkedIn, se zerou é esgotamento

---

### 2.2 Checar métrica de alerta primária: cada canal tem a sua

> 💡 **Por que:** "olhar CPM e CPC" como regra genérica esconde o que realmente importa. O sinal de problema é diferente em cada plataforma.

**Meta, Métrica primária: CPM**

- [ ] CPM subindo + CTR estável = saturação de público ou competição no leilão
- [ ] CPM subindo + CTR caindo = criativo morrendo
- [ ] Frequência por conjunto: >3 em público frio em 7 dias = saturação de audiência
- [ ] Variação >30% vs. média 7 dias sem causa → registrar no log

**Google Search, Métrica primária: CPC + Impression Share Lost**

- [ ] CPC subindo = concorrente entrando no leilão ou Quality Score caindo
- [ ] Impression Share Lost by Budget = precisa de mais orçamento
- [ ] Impression Share Lost by Rank = Quality Score ou lance insuficiente

> ***→ Gestão diária de palavras-chave (negativar + adicionar):****Search é o canal onde cada clique custa caro e cada termo errado queima budget em tempo real.*

**Negativar:**

- [ ] Olhar relatório de termos de pesquisa das últimas 24h
- [ ] Termos irrelevantes consumindo budget → negativar imediatamente
- [ ] Termos com intenção informacional pura sem chance de conversão → negativar
- [ ] Termos de concorrentes (se não for estratégia deliberada) → negativar
- [ ] Termos fora do ICP (cargo errado, segmento errado, região errada) → negativar

**Adicionar:**

- [ ] Termo novo com conversão ou CTR alto que ainda não é keyword? → Adicionar como keyword dedicada
- [ ] Keyword de broad/phrase capturando variações relevantes? → Adicionar como exact match
- [ ] Termos revelando intenção nova ou ângulo de dor não coberto? → Adicionar + registrar no log
- [ ] Volume de buscas branded subindo? → Sinal positivo de awareness, monitorar

> ⚠️ *Por que diário: cada dia com termo irrelevante é dinheiro queimado. Cada dia sem capturar termo relevante é tráfego qualificado indo para o concorrente.*

**Google Pmax/Display/YouTube**

- [ ] **Display: CPM + posicionamentos**: CPM subindo pode ser posicionamento ruim entrando
- [ ] **YouTube: view rate**: abaixo de 15% em campanha de vídeo (antigo TrueView) = hook morreu nos primeiros 5 s [VERIFICAR nomenclatura e métrica atuais do Google Ads, 01/11/2026]
- [ ] Pmax: verificar se gasto não está concentrando em Search branded canibalizando orgânico

**TikTok, Métrica primária: completion rate**

- [ ] O algoritmo do TikTok entrega mais para criativos com boa retenção: completion rate caindo = CPM vai subir como consequência
- [ ] Olhar CPM sem completion rate é olhar efeito, não causa
- [ ] Frequência: >2.5 em 7 dias = saturação (TikTok satura mais rápido que Meta)

**LinkedIn, Métrica primária: CTR + volume de impressões**

- [ ] CPM no LinkedIn é estruturalmente alto e estável: não é o sinal de alerta
- [ ] CTR caindo = público saturado ou criativo perdeu relevância
- [ ] Volume de impressões caindo = audiência esgotada

---

### 2.3 Checar integridade do rastreio: cada canal quebra diferente

> 🚨 **Por que:** sem rastreio, qualquer decisão é chute. A quebra se manifesta de forma diferente em cada plataforma.

**Meta**

- [ ] Discrepância entre conversões no Ads Manager vs. eventos no Events Manager
- [ ] Se Events Manager mostra menos eventos que Ads Manager reporta → CAPI pode ter caído
- [ ] Event Match Quality < 5 → degradação silenciosa de sinal

**Google**

- [ ] Aba de Conversões: "conversão não verificada" ou queda abrupta no volume
- [ ] GA4 Debug View: Google Tag disparando nos eventos corretos?

**TikTok**

- [ ] Events Manager → Diagnostics: match rate caindo = perda de sinal
- [ ] TikTok é mais sensível que Meta porque Events API é menos madura
- [ ] Se não tem Events API e roda volume significativo → priorizar implementação

**LinkedIn**

- [ ] Campaign Manager → Account Assets → Insight Tag: disparando?
- [ ] Se não dispara, conversões offline param de ser reportadas

**CRM (validação cruzada)**

- [ ] Filtrar contacts criados nas últimas 24h por source = paid
- [ ] Volume bate com volume reportado nas plataformas?
- [ ] A quebra pode ser seletiva: UTM de Meta passando mas de TikTok não. Verificar por canal, não no agregado

**GA4**

- [ ] Relatório de aquisição últimas 24h: todas as fontes de tráfego pago aparecendo?
- [ ] Se alguma fonte zerou → não é queda de performance, é quebra de rastreio

---

### 2.4 Checar volume de leads, MQLs, SQLs e clientes no CRM (20 min)

> 💡 **Por que:** o gestor precisa saber se o dinheiro investido ontem está gerando receita e quanto de receito, além do tempo. É para analisar pipeline, é para detectar discrepância.

- [ ] Contacts criados ontem por source = paid, olhar por canal
- [ ] Volume coerente com investimento?
- [ ] Se ciclo curto: olhar deals novos. Se ciclo longo: deals são análise semanal
- [ ] Leads de paid estão sendo trabalhados pelo comercial? Se parados → escalar para o gestor da frente

- [ ] Volume de MQL's

- [ ] Volume de SQL's

- [ ] Volume de Clientes

---

### 2.5 Registrar sinais no log (5 min)

> 💡 **Por que:** na sexta-feira você não vai lembrar o que aconteceu na segunda. O log transforma observações soltas em padrões.

- [ ] Registrar sinais relevantes dos passos anteriores
- [ ] Por canal: não genérico
- [ ] Classificar: **Anomalia** / **Oportunidade** / **Neutro**
- [ ] Se tomou ação, documentar

---

### 2.6 Pipeline de criativos: brief por canal

> 💡 **Por que:** criativo é munição e cada canal exige munição diferente.

#### ✅ Check do pipeline (todo dia)

- [ ] Quantos criativos prontos para subir por plataforma? (mínimo 2 por canal ativo)
- [ ] Quantos em produção? Quantos briefs pendentes?
- [ ] Se pipeline seco em qualquer canal → escalar prioridade

**Briefs, Meta**

- [ ] Testar variações de hook em formatos múltiplos: estático, vídeo, carrossel
- [ ] Estático ainda performa bem em Meta: não ignorar
- [ ] Copy pode ser longa. Vídeo: legendas obrigatórias (maioria assiste no mudo)
- [ ] Brief referencia: qual hook performou? Qual formato teve melhor CTR-para-conversão?

**Briefs, Google Search**

- [ ] "Criativo" = copy de anúncio (headlines + descriptions)
- [ ] RSA: headlines diversificadas para o algoritmo testar combinações
- [ ] Testar mensagens: dor vs. benefício vs. prova social vs. urgência
- [ ] Brief de Search = brief de copywriting

**Briefs, Google Display/YouTube**

- [ ] Display: banners estáticos em múltiplos tamanhos
- [ ] YouTube (campanha de vídeo, antigo TrueView): hook em 5 segundos. Produção mais elaborada que TikTok
- [ ] YouTube Bumper (6s): mensagem única, puro impacto
- [ ] Brief referencia: view rate + completion rate dos vídeos anteriores

**Briefs, TikTok**

- [ ] Formato vertical nativo 9:16: obrigatório
- [ ] Hook nos primeiros 2-3 segundos: brief começa pelo hook
- [ ] Estética UGC / nativa: produção polida performa pior
- [ ] Som ligado como padrão. Duração: 15-30s conversão, 10-15s awareness
- [ ] Não subir criativo de Meta reciclado sem adaptação completa
- [ ] Brief referencia: completion rate anteriores + top ads do Creative Center

**Briefs, LinkedIn**

- [ ] Tom corporativo/profissional: UGC não funciona
- [ ] Single image com copy profissional. Carousel com dados/insights/frameworks
- [ ] Vídeo: talking head de autoridade, curto (30-60s), produção limpa
- [ ] Brief referencia: CTR + demographics report

#### 🔍 Inteligência competitiva (2-3x por semana)

- [ ] Meta Ad Library: concorrentes e Dream 100
- [ ] TikTok Creative Center: Top Ads: padrões de hook por indústria
- [ ] Google Ads Transparency Center: novos anúncios de concorrentes
- [ ] Ads rodando >30 dias = provavelmente convertendo

---

## 3. BLOCO 2: ANÁLISE SEMANAL (3-4h, dia fixo)

> 💡 O diário acumula sinais. A semanal transforma em decisão. **Tudo gira em torno do funil.**

---

### 3.1 Montar o funil completo por canal

> 🔑 **Esse é o exercício central da semana.** Métricas isoladas não contam a história, o funil conta. Quando você vê o funil inteiro de cada canal lado a lado, a resposta para "onde investir mais?" aparece sozinha.

(imagem do Notion não migrada: Captura_de_Tela_2026-03-28_as_11.27.35.png)

#### 📊 Como ler um funil 360

> 🚨 **A maior queda percentual entre etapas = onde está o problema principal.**

| Queda | Possível Significa | Possíveis Ações |
|---|---|---|
| Impressão → Clique baixa | Problema de criativo/hook | Novos criativos, teste de hook |
| Clique → Visita LP baixa | Página lenta, redirect ou clique acidental | Verificar carregamento, mobile |
| Visita → Engajamento baixa | LP não entrega o que o ad prometeu | Alinhar mensagem ad → LP |
| Engajamento → Lead baixa | Oferta fraca, formulário com fricção | Testar oferta, reduzir fricção |
| Lead → MQL baixa | Tráfego de baixa qualidade | Ajustar público, evento de otimização |
| MQL → SQL baixa | Handoff marketing-vendas | Escalar para o gestor da frente |
| SQL → Won baixa | Problema comercial ou de oferta | Escalar para a liderança de growth |

**📊 Benchmarks esperados por canal (referência)**

- ***Google Search****: CTR mais alto (intenção declarada), conversão LP mais alta, MQL rate mais alta. Pipeline mais rápido. CPC mais alto mas funil mais eficiente*
- ***Meta****: CTR médio, conversão LP média-baixa (interrupção), MQL rate depende da qualificação do público. Volume alto, qualidade variável*
- ***TikTok****: CTR pode ser alto (scroll stopping), conversão LP baixa (público frio), MQL rate tende a ser mais baixa. Completion rate importa mais que CTR*
- ***LinkedIn****: CTR mais baixo, conversão LP média-alta (público qualificado), MQL rate alta. Volume baixo, CPL alto, qualidade alta*
- ***Pmax/Display****: CTR baixo, conversão LP baixa, volume alto, qualidade depende de expansão do algoritmo*

> Comparar canal com canal apenas no **CPA Real e pipeline value**, onde todos se igualam.

---

### 3.2 Diagnóstico de queda [Árvore por Canal]

> 🚨 **Quando algo não performa, a sequência de investigação é diferente em cada plataforma.** Aplicar a mesma lógica para todas gera diagnóstico errado.

**Meta**

1. **Criativo (fadiga)** → CTR caiu? Frequência >3? Criativo tem mais de 2-3 semanas?
2. **Público (saturação)** → Reach caiu? Audiência esgotou? Sobreposição entre conjuntos?
3. **LP (desalinhamento)** → Taxa de engajamento da LP caiu? Promessa do ad ≠ conteúdo da LP?
4. **Oferta** → Tudo acima ok mas conversão caiu? Oferta perdeu relevância?

> *Meta é plataforma de interrupção. Criativo é a variável mais volátil [muda e esgota primeiro].*

**Google Search**

1. **Termos de pesquisa** → Entrando termos irrelevantes consumindo budget?
2. **Quality Score** → Caiu? LP perdeu relevância? CTR esperado caiu?
3. **Leilão** → Impression Share Lost by Rank ou by Budget? Concorrente novo?
4. **LP** → Conversão da LP caiu com mesmo tráfego?

> *Search tem intenção declarada. Se o termo está errado, nada mais importa.*

**Revisão semanal de palavras-chave:**

- [ ] Quantos termos foram negativados no diário essa semana? Se >20% do budget foi lixo → match types amplos demais
- [ ] Categorizar termos negativados: padrão recorrente? → Criar lista de negativas por categoria
- [ ] Keywords adicionadas no diário estão gerando impressões? CTR coerente?
- [ ] Alguma keyword nova puxou termos irrelevantes? → Ajustar match type
- [ ] Gaps de cobertura: termos relevantes sem keyword dedicada?
- [ ] Match types: exact com bom volume merece phrase? Phrase puxando lixo precisa voltar para exact?
- [ ] Concorrentes em termos não cobertos? (Auction Insights + Transparency Center)
- [ ] Quality Score das keywords principais: estável, subindo ou caindo?

**Google Pmax**

1. **Expansão de público** → Algoritmo expandiu para fora do ICP? Verificar Search terms insights
2. **Asset Groups** → Quais assets performam? Algum concentrando spend sem converter?
3. **Canais** → Pmax mistura Search, Display, YouTube, Demand Gen (antigo Discovery) e Gmail [VERIFICAR a lista atual de inventário, 01/11/2026]. Problema pode estar em um canal específico
4. **Branded cannibalization** → Capturando buscas branded que o orgânico já traria?

**TikTok**

1. **Completion rate** → Caiu? Vídeo não prende mais. Hook morreu. Substituir criativo primeiro
2. **Frequência** → >2.5 em 7 dias? Saturação. Ciclo de vida 7-14 dias
3. **Posicionamento** → Pangle puxando qualidade para baixo? Isolar feed only
4. **Público** → Interesse/lookalike esgotou? Testar broad

> *TikTok penaliza criativo fraco mais agressivamente que qualquer outra plataforma.*

**LinkedIn**

1. **Audiência (esgotamento)** → Volume de impressões caiu? Público pequeno saturou?
2. **Formato (saturação)** → Message ads saturaram? Message ads (antigo Sponsored InMail) com abertura caindo? [VERIFICAR nomenclatura atual do LinkedIn, 01/11/2026]
3. **Oferta/mensagem** → Proposta de valor não ressoa com o seniority?
4. **Segmentação** → Cargo/indústria certo mas senioridade errada?

> 🚨 **Regra em qualquer canal:** Evite mudar mais de uma variável ao mesmo tempo.

---

### 3.3 Análise de pipeline no CRM [Continuação do Funil]

> 💡 **Por que:** o funil não termina no lead. O CRM mostra a segunda metade, e é onde o dinheiro aparece (ou não).

**Velocidade do pipeline por canal**

- [ ] Tempo médio em cada stage, por fonte de origem
- [ ] Google Search fecha mais rápido? (esperado a intenção)
- [ ] TikTok fica mais tempo em stages iniciais? (esperado a público frio)
- [ ] Velocidade afeta payback: canal com CPL mais alto mas ciclo mais curto pode ser mais rentável

**Motivos de perda por canal**

- [ ] Deals Lost da semana filtrados por fonte
- [ ] Agrupar: fora do ICP / sem budget / não decisor / concorrente / sumiu
- [ ] Conectar com campanhas de origem:

| Motivo | Sinal | Ação |
| --- | --- | --- |
| Fora do ICP | Targeting errado | Parar ou reconfigurar segmentação |
| Não era decisor | Criativo/canal atraindo pessoa errada | Ajustar copy e público |
| Sumiu/não respondeu | Lead de baixa intenção | Problema de canal ou criativo |
| Sem budget | Público sem poder de compra | Revisar targeting |
| Concorrente | Problema de oferta | Não é problema de tráfego |

**Ticket médio e Pipeline value por canal**

- [ ] Won por plataforma × ticket médio
- [ ] Se TikTok traz ticket 40% menor que LinkedIn, mesmo com CPL mais baixo o ROI pode ser pior
- [ ] Pipeline value = soma dos deals em aberto por fonte
- [ ] Pipeline value / investimento = pipeline ROI
- [ ] Alocar budget com base em receita potencial, não volume de leads

---

### 3.4 Identificar o gargalo principal e decidir

> 🔑 **Quando tudo compete por atenção, o funil diz por onde começar.** A maior queda percentual = onde investir energia primeiro.

- [ ] Olhar o funil completo de cada canal (passo 3.1)
- [ ] Identificar: qual canal tem a maior queda em qual transição?
- [ ] Definir 1 a 3 hipóteses testáveis para a próxima semana
- [ ] Cada hipótese com: variável isolada + critério plataforma + critério CRM + tempo mínimo
- [ ] Decidir para cada campanha: **escalar / manter / pausar**: justificativa em dado
- [ ] Decidir realocação de budget entre canais (CPA Real + pipeline ROI)

**💡 Considerar LP dedicada por canal**

- [ ] Se queda Visita → Engajamento é muito maior em um canal, LP pode estar otimizada para perfil de outro
- [ ] Visitante de Google Search: intenção → LP direta
- [ ] Visitante de Meta/TikTok: sem intenção → LP precisa criar contexto e desejo
- [ ] LP dedicada por canal só vale se o volume justificar

---

### 3.5 Feedback loop: CRM → plataformas

> ⚠️ **Por que:** o algoritmo otimiza para o evento que você manda. Se manda "lead" (formulário), ele aprende a trazer quem preenche formulário [não necessariamente quem compra].

- [ ] Exportar lista de MQLs e SQLs dos últimos 30-60 dias por canal
- [ ] Subir como custom audience:

| Plataforma | Ação |
| --- | --- |
| Meta | Lookalike de MQLs qualificados (não de todos os leads) |
| Google | Customer Match para ajustar bidding |
| TikTok | Lookalike de leads qualificados (se volume > 1.000 contacts) |
| LinkedIn | Matched Audience |

- [ ] Se CPA melhorando mas MQL rate caindo → algoritmo aprendeu a trazer lead fácil, não bom
- [ ] Considerar mudar otimização de "lead" para "MQL" ou enviar conversões offline
- [ ] Passo quinzenal ou mensal dependendo do volume

---

### 3.6 Report semanal

> 💡 **Responde uma pergunta: "o dinheiro investido essa semana está virando pipeline qualificado e receita?"**

#### ✅ Estrutura do report

- [ ] Resumo executivo (3-5 linhas): investimento, leads, MQLs, Won, CPA Real, status vs. meta
- [ ] Funil por canal (tabela do passo 3.1 condensada)
- [ ] Gargalo principal: maior queda, qual canal, o que significa
- [ ] Motivos de perda: top 3 da semana e canal de concentração
- [ ] Testes: resultado plataforma + CRM, próximos testes
- [ ] Realocação de budget: justificativa
- [ ] Pendências: rastreio, criativos, LP, CRM

> 🚨 **Regras:** máximo 1 páginas. Sem métrica de vaidade. Se rastreio está quebrado, isso é o destaque principal.

---

## 4. BLOCO 3: REVISÕES PERIÓDICAS

---

### 4.1 Validação estrutural (quinzenal, 30-45 min)

> 💡 **Por que:** a operação diária e semanal pega problemas de performance. A quinzenal pega problemas de estrutura.

*→ Exemplo: sobreposição de público, retargeting mal montado, budget mal distribuído.*

**Meta**

- [ ] Sobreposição de públicos >30% → consolidar
- [ ] Retargeting: Engaged (5-7d) → Landed (7-14d) → Owned. Buckets montados?
- [ ] Split prospecção/retargeting: 70-80% / 20-30%
- [ ] Advantage+/Broad vs. manual: testado?

**Google**

- [ ] Negativas atualizadas? Match types adequados?
- [ ] Pmax: insights de público: expandiu para fora do ICP?
- [ ] Budget entre Search/Display/YouTube faz sentido?

**TikTok**

- [ ] Interest vs. lookalike vs. broad, qual performa?
- [ ] Lances automáticos vs. manual: automático viável acima de 50 conversões/semana (default do método) [VERIFICAR o que a sigla SPC designava no original e o mínimo atual recomendado pelo Google, 01/11/2026]
- [ ] Pangle ativo e não performa? Excluir
- [ ] Criativos com >14 dias → substituir. TikTok consome criativo mais rápido
- [ ] Brand safety configurado?

**LinkedIn**

- [ ] Público amplo demais ou restrito demais?
- [ ] Formato: qual performa por objetivo?

**Rastreio (validação rápida)**

- [ ] UTMs seguindo padrão? `source` / `medium` / `campaign` / `content`
- [ ] Discrepância leads plataforma vs. CRM por canal: <15% ok, >15% investigar, >30% congelar decisões
- [ ] Eventos de conversão corretos em todas as plataformas?
- [ ] CRM: original source drill-down populando? Workflows de lifecycle stage funcionando?

---

### 4.2 Revisão de CAC Real vs. LTV (mensal, 1h)

> 🚨 **Por que:** CPL é proxy. CPA da plataforma é proxy. CAC Real comparado com LTV é a métrica final que diz se o motor está saudável.

- [ ] CAC Real por canal: investimento / deals Won, por plataforma
- [ ] LTV:CAC: saudável >3:1 para B2B
- [ ] Ranking de canais por CAC Real → guia realocação do próximo mês
- [ ] Tendência 3-6 meses por canal
- [ ] Se CAC subindo: diagnosticar camada: mídia (eficiência), funil (conversão), pipeline (qualificação), mercado (saturação)
- [ ] Pipeline value por canal: quanto está em aberto por fonte
- [ ] Win rate por canal: efetividade real de cada fonte
- [ ] Revisão em conjunto com o gestor da frente e a liderança de growth

---

## 5. BLOCO 4: GATILHOS (ativados por evento)

---

### 5.1 ✅ Antes de ligar qualquer campanha nova

> 🚨 **Por que:** campanha ligada sem rastreio íntegro queima dinheiro sem aprendizado. Campanha sem hipótese é aposta, não teste.

#### Checklist obrigatório

- [ ] LP publicada e testada (carregamento, mobile, formulário)
- [ ] Formulário integrado com CRM, hidden fields de UTM passando
- [ ] UTMs definidos e documentados
- [ ] Tags no GTM configuradas e testadas via Preview Mode
- [ ] Meta Pixel / CAPI / Google Tag / TikTok Pixel / Events API validados
- [ ] Evento de conversão correto selecionado na plataforma
- [ ] Workflow no CRM: lead → lifecycle stage → notificação comercial
- [ ] Hipótese documentada
- [ ] Critério de sucesso duplo: plataforma + CRM
- [ ] Tempo mínimo de aprendizado definido e alinhado
- [ ] Budget diário configurado (não lifetime em teste)

**⚠️ Específico TikTok, antes de ligar primeira campanha**

- [ ] Criativos em formato nativo 9:16, hook em 2-3s, estética UGC, som ligado
- [ ] Não subir criativo de Meta reciclado sem adaptação
- [ ] Começar com posicionamento TikTok feed only para isolar dados
- [ ] Se volume esperado < 50 conversões/semana, otimizar para evento mais acima no funil

---

### 5.2 ✅ Antes de escalar budget

> 🚨 **Por que:** escalar campanha não validada = multiplicar o prejuízo. Escalar rápido demais reseta o aprendizado.

- [ ] Variável vencedora isolada e confirmada
- [ ] CPA estável por 7-14 dias (não pico de 2-3 dias)
- [ ] MQL rate estável ou melhorando no CRM
- [ ] Volume > 50 conversões no período
- [ ] Funil pós-clique aguenta: LP, time comercial, capacidade de atendimento
- [ ] Time comercial tem capacidade para volume maior
- [ ] Rastreio validado
- [ ] Escalar 20-30% por vez, aguardar 3-5 dias, reavaliar

| Plataforma | Como escalar |
|---|---|
| Meta | Duplicar conjunto vencedor com budget maior |
| TikTok | Aumento gradual no ad group existente, máximo 20% a cada 48h |
| Google Search | Não escala por budget, escala por cobertura de intenção: aumentar budget só em keywords com Impression Share Lost by Budget + expandir profundidade semântica (long tail, sinônimos, variações de estágio) |
| Google Pmax/Display/YouTube | Aumento gradual de 20% por ciclo + alimentar audience signals com listas de MQLs do CRM, monitorar Search terms insights para evitar expansão fora do ICP |

---

### 5.3 ⚠️ Quando campanha começa a cair

> 🚨 **Por que:** campanha em queda gera pânico. Pânico gera a pior decisão: mexer em tudo ao mesmo tempo.

- [ ] Seguir árvore de diagnóstico do canal específico (passo 3.2)
- [ ] Checar CRM: queda só na plataforma ou qualificação também caiu?
- [ ] CPA subiu + qualificação manteve → pode ser refinamento, não piora
- [ ] CPA subiu + qualificação caiu → problema real, intervir
- [ ] **Nunca mudar mais de uma variável ao mesmo tempo**

---

### 5.4 📝 Ao entrar em um novo projeto

> 💡 **Por que:** cada projeto tem histórico, estrutura e contexto próprios. Agir sem auditar é construir em cima de fundação desconhecida.

**Auditoria de plataformas**

- [ ] **Meta**: estrutura, histórico 90d, Pixel, Event Match Quality, audiences
- [ ] **Google**: campanhas, keywords, negativas, Quality Score, conversões
- [ ] **TikTok**: estrutura, histórico, Pixel, Events API, match rate, criativos nativos ou reciclados
- [ ] **LinkedIn**: segmentações, formatos, CPL histórico

**Auditoria CRM**

- [ ] Pipeline configurado? Stages fazem sentido?
- [ ] Lifecycle stages definidos?
- [ ] Atribuição: UTMs, original source funcionando?
- [ ] Dashboard pipeline por canal existe?
- [ ] Histórico de leads/qualificação por fonte 90 dias
- [ ] Win rate por canal
- [ ] Motivos de perda sendo registrados?
- [ ] Integrações íntegras?
- [ ] Workflows ativos e funcionando?

**GA4 + GTM**

- [ ] Eventos, conversões, fontes, funil
- [ ] Tags documentadas ou caixa preta?

#### Pós-auditoria

- [ ] Documentar estado atual por plataforma + CRM
- [ ] Prioridade: **rastreio → atribuição → estrutura → otimização → escala**
- [ ] Expectativa: 2-4 semanas = compra de dados e validação

---

## ANEXO HUBSPOT

Na operação do Sarden o CRM é o HubSpot. O que é específico da plataforma: lifecycle stage como base de MQL e SQL com de-para por frente; propriedades de qualificação, Data de MQL e Data de SQL; as sete propriedades de atribuição com herança (first click, last click, jornada de fontes); relatórios com prefixo da organização; histórico de propriedade só na interface. Padrão completo em `00_susano/referencias/plataformas/crm/padrao_implementacao.md`; a plataforma em `00_susano/referencias/plataformas/hubspot/dossie_mestre.md`.

## NOTAS DA MIGRAÇÃO (2026-11-01)

- A página original trazia um aviso de confidencialidade para o time de uma organização; o aviso saiu porque o conteúdo é método do Sarden (decisão do Sarden, 01/11/2026). Nenhum dado de cliente no texto.
- Papéis de escalonamento escritos de forma genérica (gestor da frente, liderança de growth) desde a v0.3.0; cada organização mapeia para os seus em `10_<org>/time/`.
- A imagem do funil 360 por canal (captura de tela) não foi migrada; a tabela de leitura do funil que a acompanha está íntegra.
- Thresholds (frequência >3, discrepância >15%, LTV:CAC >3:1, escalar 20 a 30% por vez) são regras operacionais do Sarden, não benchmarks de mercado: tratar como default a calibrar por projeto.
