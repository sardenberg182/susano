---
id: ref-gtm-growth-modeling-atribuicao
tipo: referencia
origem: GTM_EST.md (KB_GTM_GrowthModeling_Attribution)
atualizado: 2026-10-31
---

# KB_GTM_GrowthModeling_Attribution

## Scope
Modelos de crescimento, simulação e media mix / attribution. Fontes: Bessemer State of the Cloud 2024, materiais de MMM e atribuição.

## Growth curves

- S‑curve logística: \(y(t) = K / (1+e^{-a(t-t_0)})\).
- Bass diffusion: separa inovação e imitação.
- Viralidade: K‑factor = invites per user × conversion rate; K > 1 = crescimento viral.

## Simulação

- Monte Carlo: distribuições de leads, win rate, ACV, churn e spend.
- Cenários: base, bull, bear; melhora decisão frente à incerteza.

## Attribution e MMM

- Markov Chain: crédito por transição de canais.
- Shapley Value: divisão justa entre canais.
- MMM (Robyn, LightweightMMM, PyMC‑Marketing): atribuição em escala, com experimentos de incrementality (geo‑lift, holdout, ghost ads).

## NOTAS DA MIGRAÇÃO (2026-10-31)

- [VERIFICAR] O original citava fontes como [web:NN] sem a lista de referências; as marcas foram removidas e os números pedem conferência.
