---
id: ref-gtm-modelos-estatisticos-sizing-segmentacao
tipo: referencia
origem: GTM_EST.md (KB_GTM_StatModels_Sizing_Segmentation)
atualizado: 2026-10-31
---

# KB_GTM_StatModels_Sizing_Segmentation

## Scope
Base de conhecimento operacional sobre sizing, segmentação estatística, propensity scoring, lookalikes e pricing analytics para GTM B2B e B2C. Fontes: Seer Interactive, guias de mercado, material de RFM, pricing e GTM de 2024–2025.

## TAM SAM SOM

- TAM: mercado total se houver 100% de penetração.
- SAM: parte do TAM servível por geo, produto, canal e preço.
- SOM: fatia realmente capturável no horizonte de 1–3 anos.

### Métodos
- Top‑down: aplica filtros a partir de mercado total.
- Bottom‑up: parte de contas, usuários, seats, tickets, consumo.
- Value theory: estima valor econômico e converte em willing‑to‑pay.

### Fórmulas
- \(TAM = \sum N_i \times ARPU_i\)
- \(SAM = TAM \times \text{fração servível}\)
- \(SOM = SAM \times \text{share capturável}\)
- SOM bottom‑up: SOM ≈ contas alvo × taxa de conversão × ACV
- IC para proporção: \(p \pm 1{,}96 \cdot \sqrt{p(1-p)/n}\)

### Exemplo
ICP com 10.000 contas, conversão de 3% e ACV de R$ 120.000 → SOM ≈ R$ 36 milhões.

## Segmentação estatística

### Clustering (ICP)
- K‑means: bom para segmentos relativamente esféricos.
- Hierarchical: descobre hierarquia de segmentos.
- DBSCAN: bom para clusters irregulares e outliers.

### RFM
- Recency: tempo desde última interação/compra.
- Frequency: quantidade de eventos.
- Monetary: valor gerado.

Scoring típico: 5 = top quintil, 1 = muito baixo.

## Propensity scoring

Modelo base: \(P(\text{conversão}) = 1 / (1+e^{-(\beta_0+\beta X)})\).

Aplicações:
- Ranking de leads.
- Priorização SDR/AE.
- Triggers de automação e Next‑best‑action.

## Lookalike modeling

- Classifica ICP como “positivo” e prospectos como negativos/sem rótulo.
- Ranqueia por probabilidade de similaridade com o ICP.
- Útil em advertsing e expansão orgânica.

## Pricing analytics

- Van Westendorp: faixa de preço aceitável (barato demais, barato, caro, caro demais).
- Conjoint: estima utilidade por atributo e preço.
- Elasticidade: \(E_p = \%\Delta Q / \%\Delta P\); se < −1, demanda elástica.
- A/B de preço: trate como teste de receita, não apenas de CTR; precisa de amostra grande.

## NOTAS DA MIGRAÇÃO (2026-10-31)

- [VERIFICAR] O original citava fontes como [web:NN] sem a lista de referências; as marcas foram removidas e os números pedem conferência.
