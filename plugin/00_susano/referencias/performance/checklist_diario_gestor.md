---
id: ref-perf-checklist-diario
tipo: referencia
autor: Sarden
origem: Notion do Sarden: 'Checklist Diário, Gestor de Performance' (playbook, 01/04/2026)
atualizado: 2026-11-01
---

# Checklist diário do gestor de performance

> Uso: Versão executável do bloco diário da rotina (`00_susano/referencias/performance/rotina_gestor_performance.md`): 7 passos, cerca de 60 minutos, por canal. Usar como runbook de abertura do dia ou como base de uma skill ou rotina de agente.

> **🚨***O funil completo por canal (Impressão até Won) é a única ferramenta de decisão. O gestor que não sabe responder "onde está a maior queda no funil de cada canal essa semana?" não está operando. A fonte de verdade não é a plataforma, é o pipeline no HubSpot. Nenhuma decisão de pausar, escalar ou trocar criativo é tomada com base em um dia de dado.*

## 1. CAMPANHAS RODANDO? (5 min)

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

## 2. MÉTRICA DE ALERTA PRIMÁRIA (5 min)

**Meta, Métrica primária: CPM**

- [ ] CPM subindo + CTR estável = saturação de público ou competição no leilão
- [ ] CPM subindo + CTR caindo = criativo morrendo
- [ ] Frequência por conjunto: >3 em público frio em 7 dias = saturação de audiência
- [ ] Variação >30% vs. média 7 dias sem causa → registrar no log

**Google Search, Métrica primária: CPC + Impression Share Lost**

- [ ] CPC subindo = concorrente entrando no leilão ou Quality Score caindo
- [ ] Impression Share Lost by Budget = precisa de mais orçamento
- [ ] Impression Share Lost by Rank = Quality Score ou lance insuficiente

**Google Pmax/Display/YouTube**

- [ ] **Display: CPM + posicionamentos**: CPM subindo pode ser posicionamento ruim entrando
- [ ] **YouTube: view rate**: abaixo de 15% em TrueView = hook morreu nos primeiros 5s
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

## 3. GESTÃO DIÁRIA DE KEYWORDS: GOOGLE SEARCH (10 min)

> 🔑 *Search é o canal onde cada clique custa caro e cada termo errado queima budget em tempo real.*

#### ❌ Negativar

- [ ] Olhar relatório de termos de pesquisa das últimas 24h
- [ ] Termos irrelevantes consumindo budget → negativar imediatamente
- [ ] Termos com intenção informacional pura sem chance de conversão → negativar
- [ ] Termos de concorrentes (se não for estratégia deliberada) → negativar
- [ ] Termos fora do ICP (cargo errado, segmento errado, região errada) → negativar

#### ➕ Adicionar

- [ ] Termo novo com conversão ou CTR alto que ainda não é keyword? → Adicionar como keyword dedicada
- [ ] Keyword de broad/phrase capturando variações relevantes? → Adicionar como exact match
- [ ] Termos revelando intenção nova ou ângulo de dor não coberto? → Adicionar + registrar no log
- [ ] Volume de buscas branded subindo? → Sinal positivo de awareness, monitorar

> ⚠️ *Cada dia com termo irrelevante é dinheiro queimado. Cada dia sem capturar termo relevante é tráfego qualificado indo para o concorrente.*

---

## 4. RASTREIO ÍNTEGRO? (5 min)

> 🚨 *Sem rastreio, qualquer decisão é chute.*

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

**HubSpot (validação cruzada)**

- [ ] Filtrar contacts criados nas últimas 24h por source = paid
- [ ] Volume bate com volume reportado nas plataformas?
- [ ] A quebra pode ser seletiva: UTM de Meta passando mas de TikTok não. Verificar por canal, não no agregado

**GA4**

- [ ] Relatório de aquisição últimas 24h: todas as fontes de tráfego pago aparecendo?
- [ ] Se alguma fonte zerou → não é queda de performance, é quebra de rastreio

---

## 5. LEADS, MQLs, SQLs E CLIENTES NO HUBSPOT (20 min)

- [ ] Contacts criados ontem por source = paid, olhar por canal
- [ ] Volume coerente com investimento?
- [ ] Se ciclo curto: olhar deals novos. Se ciclo longo: deals são análise semanal
- [ ] Leads de paid estão sendo trabalhados pelo comercial? Se parados → escalar para GP
- [ ] Volume de MQL's
- [ ] Volume de SQL's
- [ ] Volume de Clientes

- [ ] Documentar na planilha de acompanhamento

---

## 6. REGISTRAR SINAIS NO LOG (5 min)

- [ ] Registrar sinais relevantes dos passos anteriores
- [ ] Por canal: não genérico
- [ ] Classificar: **Anomalia** / **Oportunidade** / **Neutro**
- [ ] Se tomou ação, documentar

---

## 7. PIPELINE DE CRIATIVOS (10 min)

#### ✅ Check do pipeline

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
- [ ] YouTube TrueView: hook em 5 segundos. Produção mais elaborada que TikTok
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

## NOTAS DA MIGRAÇÃO (2026-11-01)

- Mesmo aviso de confidencialidade removido que na rotina do gestor (decisão do Sarden, 01/11/2026).
- Idêntico ao Bloco 1 da rotina na data da migração; se um dos dois mudar, o outro acompanha na versão seguinte do modelo.
