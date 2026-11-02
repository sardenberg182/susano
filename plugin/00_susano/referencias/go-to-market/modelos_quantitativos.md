---
id: ref-gtm-modelos-quantitativos
tipo: referencia
autor: Sarden (curadoria); fórmulas de domínio público
origem: consolidação dos nove arquivos de GTM analytics do método (sizing, segmentação, propensity, forecasting, churn, growth curves, atribuição e MMM, experimentação, SQL e ferramentas), reescritos com as fórmulas e um SQL testado; versão anterior em `90_arquivo/` do repositório do modelo
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Modelos quantitativos de GTM: sizing, scoring, forecasting, atribuição, experimentação e SQL

> Uso: a caixa de ferramentas quantitativa do método, uma seção por pergunta. Abrir só a seção que a pergunta pede. Toda fórmula aqui é de domínio público e vale como mecânica; nenhum número de mercado entra como meta (benchmarks com fonte ficam em `benchmarks_com_fonte.md`; fórmulas de unit economics e auditoria de planilha em `auditoria_bp.md`).

## 1. SIZING: TAM, SAM, SOM

- **TAM**: receita se houvesse 100% de penetração: `Σ (contas do segmento i × ARPU do segmento i)`.
- **SAM**: a parte do TAM que o produto, o canal, a geografia e o preço alcançam: `TAM × fração servível`.
- **SOM**: a fatia capturável no horizonte de 1 a 3 anos: `SAM × share capturável`, ou bottom-up: `contas-alvo × taxa de conversão × ACV`.
- Três métodos, usar dois e comparar: top-down (filtros sobre o mercado total), bottom-up (contas, seats, tickets, consumo) e value theory (valor econômico gerado convertido em disposição a pagar).
- Intervalo de confiança para uma proporção (taxa de conversão, share): `p ± 1,96 × √(p(1 − p) ÷ n)`.
- Exemplo inventado: ICP com 10 mil contas, conversão de 3%, ACV de R$ 120 mil → SOM ≈ R$ 36 milhões. O número só vale com a fonte das 10 mil contas e do 3% registradas.

## 2. SEGMENTAÇÃO

- **Clustering para ICP**: k-means (segmentos compactos, precisa escolher k), hierárquico (revela a árvore de segmentos), DBSCAN (clusters irregulares e outliers). Padronizar variáveis antes; validar o cluster contra receita e churn reais, não contra "fazer sentido".
- **RFM**: recência (tempo desde a última compra), frequência (eventos no período), valor monetário. Quintis de 1 a 5 em cada eixo; a combinação (555, 511, 155) vira segmento acionável. Serve para base ativa; não substitui ICP para aquisição.

## 3. PROPENSITY, LOOKALIKE E LEAD SCORING

- **Regressão logística** como modelo base: `P(conversão) = 1 ÷ (1 + e^−(β0 + β·X))`. Exemplo: β0 + β·X = −0,5 → P ≈ 0,38.
- **Alternativas**: random forest e gradient boosting quando há volume e interação entre variáveis; a logística continua sendo o modelo que o time entende.
- **Como avaliar um scoring**: AUC-ROC (separação geral), precision@k e recall@k (os k leads que o SDR vai de fato ligar), lift por decil (quanto o top 10% converte acima da média). Um scoring que não muda a fila do SDR não vale a manutenção.
- **Lookalike**: ICP e clientes como classe positiva, prospectos como não rotulados; ranquear por probabilidade de pertencer à classe positiva. Vale para mídia (audiências) e para priorização outbound.
- Regra do método: o scoring prioriza, não qualifica. MQL continua sendo critério de ICP no formulário (`00_susano/dna/metodo/dicionario.md`).

## 4. PRICING ANALYTICS

- **Van Westendorp**: quatro perguntas (barato demais, barato, caro, caro demais) → faixa de preço aceitável e ponto de indiferença.
- **Gabor-Granger**: disposição a comprar em preços sucessivos → curva de demanda e receita por preço.
- **Conjoint**: utilidade por atributo e por nível de preço; serve para empacotar, não só para precificar.
- **Elasticidade**: `E = %ΔQ ÷ %ΔP`; abaixo de −1, demanda elástica (preço derruba volume mais que proporcionalmente).
- A/B de preço é teste de receita (e de churn), não de CTR; pede amostra grande e janela longa. Mecânica de proposta e três opções em `00_susano/instrucoes/brief_e_proposta.md`.

## 5. FORECASTING

- **Weighted pipeline**: `Σ (valor × probabilidade histórica da etapa)`; probabilidade por etapa calculada da frente (negócios que passaram pela etapa e fecharam ÷ negócios que passaram pela etapa), nunca o default da ferramenta.
- **Séries temporais**: ETS e ARIMA quando a série é longa e estável; Prophet quando há sazonalidade múltipla e feriados; qualquer um deles com backtest (treinar até o mês t, prever t+1, repetir).
- **Regressão multivariada** quando há drivers explícitos (verba, pipeline, headcount de vendas); **bayesiano** quando há pouco dado e a premissa precisa ser atualizada com o que chega.
- Regra do método: a projeção que soma efeitos independentes de três ações está errada; projeção linear em mês com evento promocional também (`00_susano/instrucoes/wbr.md`, agenda de e-commerce).

## 6. CHURN E RETENÇÃO

- **Kaplan-Meier**: curva de sobrevivência por cohort (quantos continuam clientes em cada mês de vida); compara cohorts sem assumir distribuição.
- **Cox (proportional hazards)**: razão de risco por covariável (plano, canal de origem, uso); diz o que acelera o churn.
- **Health score**: peso de uso, suporte, valor percebido e expansão; só vale depois de calibrado contra churn real (o score precisa ter previsto os churns do trimestre passado).
- **Retenção**: por período fixo (cohort), rolling e ponderada por receita; GRR responde "o que ficou", NRR responde "o que cresceu" (fórmulas em `auditoria_bp.md`).

## 7. WIN/LOSS

- Teste de proporções (dois canais, dois segmentos, dois vendedores): diferença de win rate só é achado com amostra suficiente; abaixo disso, é ruído.
- Estratificar por tamanho de negócio, canal de origem, quem conduziu e motivo de perda (vocabulário de motivo em `00_susano/referencias/plataformas/crm/padrao_implementacao.md`).

## 8. CURVAS DE CRESCIMENTO E SIMULAÇÃO

- **Logística (S-curve)**: `y(t) = K ÷ (1 + e^−a(t − t0))`, com K o teto; usar quando a saturação é a pergunta.
- **Bass**: separa adoção por inovação de adoção por imitação; útil em lançamento.
- **Viralidade**: `K = convites por usuário × conversão do convite`; K acima de 1 é crescimento viral, raro e temporário.
- **Monte Carlo**: distribuições para leads, win rate, ACV, churn e verba → distribuição de receita, não um número; cenários base, otimista e pessimista como percentis, não como três planilhas.

## 9. ATRIBUIÇÃO E MMM

- **Markov**: crédito por efeito de remoção de cada canal da jornada; **Shapley**: divisão justa do crédito entre canais. Os dois pedem jornada completa (first click, last click e jornada de fontes no CRM: `padrao_implementacao.md`).
- **MMM** (Robyn, Meridian, PyMC-Marketing): atribuição em escala com dados agregados; só se sustenta com experimentos de incrementalidade (geo-lift, holdout, ghost ads) calibrando o modelo. LightweightMMM foi descontinuado em favor do Meridian (Google) [VERIFICAR a data oficial da descontinuação antes de citar].
- Regra do método: first click do CRM e last click da plataforma contam histórias diferentes; nunca se consolidam. Direto grande é tracking quebrado até prova em contrário.

## 10. EXPERIMENTAÇÃO

- **Frameworks**: A/B de horizonte fixo (simples, governável), sequencial (decide mais cedo, mais complexo), multi-armed bandit (maximiza resultado durante o teste; ruim para aprender), MVT (muitas variações, pede muito tráfego).
- **Amostra por variante** (duas proporções, aproximação): `n ≈ 2 × p̄(1 − p̄) × (z_α/2 + z_β)² ÷ δ²`, com p̄ a média das taxas, δ a diferença mínima detectável em pontos absolutos, z_α/2 = 1,96 (95%) e z_β = 0,84 (80% de poder). Exemplo: de 4% para 5% → p̄ = 4,5%, δ = 0,01 → n ≈ 6.750 por variante. Taxa baixa e diferença pequena pedem amostra que a maioria das frentes não tem no mês: por isso o corte da hipótese é número e prazo (`00_susano/dna/metodo/diagnostico_de_funil.md`).
- **Vieses**: paradoxo de Simpson (a média esconde a inversão por grupo), sobrevivência (só quem ficou), regressão à média (pico que volta sozinho), espiada (olhar o teste todo dia e parar no primeiro "significativo").
- **O que testar em GTM**: preço (Van Westendorp, Gabor-Granger, conjoint), mensagem (proposta de valor, prova), página (headline e primeira dobra antes de cor), e-mail (assunto, horário, CTA). Uma variável por teste.

## 11. SQL PARA GA4 NO BIGQUERY

Duas consultas sobre a exportação padrão do GA4 (`events_*`, `event_date` como string `AAAAMMDD`, `event_name`, `user_pseudo_id`). Testado em 01/11/2026: sintaxe validada no dialeto BigQuery com sqlglot 30.27 e lógica rodada em DuckDB 2.0 sobre eventos sintéticos (transpilação automática); **não rodado em projeto BigQuery real** [VERIFICAR o custo da varredura por `_TABLE_SUFFIX` na conta antes de agendar].

Cohort por mês do primeiro purchase e recompra nos meses seguintes:

```sql
WITH compras AS (
  SELECT user_pseudo_id,
         DATE_TRUNC(PARSE_DATE('%Y%m%d', event_date), MONTH) AS mes
  FROM `projeto.analytics_000000.events_*`
  WHERE event_name = 'purchase'
    AND _TABLE_SUFFIX BETWEEN '20260101' AND '20261231'
),
primeira AS (
  SELECT user_pseudo_id, MIN(mes) AS cohort FROM compras GROUP BY 1
)
SELECT p.cohort,
       DATE_DIFF(c.mes, p.cohort, MONTH) AS mes_n,
       COUNT(DISTINCT c.user_pseudo_id) AS compradores
FROM compras c
JOIN primeira p USING (user_pseudo_id)
GROUP BY 1, 2
ORDER BY 1, 2;
```

Funil por dia (usuários únicos por etapa e taxa de compra):

```sql
WITH por_usuario AS (
  SELECT PARSE_DATE('%Y%m%d', event_date) AS dia,
         user_pseudo_id,
         LOGICAL_OR(event_name = 'page_view') AS viu,
         LOGICAL_OR(event_name = 'view_item') AS viu_item,
         LOGICAL_OR(event_name = 'add_to_cart') AS carrinho,
         LOGICAL_OR(event_name = 'begin_checkout') AS checkout,
         LOGICAL_OR(event_name = 'purchase') AS comprou
  FROM `projeto.analytics_000000.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20260101' AND '20260131'
  GROUP BY 1, 2
)
SELECT dia,
       COUNTIF(viu) AS usuarios,
       COUNTIF(viu_item) AS viram_item,
       COUNTIF(carrinho) AS carrinho,
       COUNTIF(checkout) AS checkout,
       COUNTIF(comprou) AS compraram,
       SAFE_DIVIDE(COUNTIF(comprou), COUNTIF(viu)) AS taxa_compra
FROM por_usuario
GROUP BY 1
ORDER BY 1;
```

Notas: `user_pseudo_id` conta dispositivos, não pessoas (use `user_id` quando a frente o envia); o funil por dia perde quem começa num dia e compra no outro, por isso serve para monitorar, e a cohort serve para decidir; sempre filtrar `_TABLE_SUFFIX`, senão a consulta varre todo o histórico e o custo escala.

## 12. FERRAMENTAS

- Python: `pandas` (manipulação), `scipy` e `statsmodels` (testes e regressão), `scikit-learn` (scoring e clustering), `prophet` (séries), `lifelines` (sobrevivência), `lifetimes` (CLV probabilístico), `openpyxl` (planilha na camada de fórmula). R: `survival`, `forecast`, `caret`.
- Planilha: calculadora de amostra (fórmula da seção 10), weighted pipeline, Monte Carlo com `RAND()` e intervalo de confiança de proporção; quando passa disso, Python.
- Regra do método: número se calcula em código e se concilia com a fonte; nunca se estima em prosa (`.claude/skills/analise`).

## REFERÊNCIA RÁPIDA

**Melhor para**: dimensionar mercado, priorizar leads, prever receita, medir churn, atribuir canal, desenhar e dimensionar teste, puxar cohort e funil do GA4.
**Ativar quando**: alguém pede "o tamanho do mercado", "um score", "a projeção", "quanto tempo de teste", "qual canal converte" ou uma query de GA4.
**Nunca**: usar número de mercado como meta da frente; aceitar probabilidade de etapa padrão da ferramenta; somar efeitos independentes; rodar teste sem corte.
