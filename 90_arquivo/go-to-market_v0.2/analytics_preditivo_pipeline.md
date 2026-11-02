---
id: ref-gtm-analytics-preditivo-pipeline
tipo: referencia
origem: GTM_EST.md (KB_GTM_PredictiveAnalytics_Pipeline)
atualizado: 2026-10-31
---

# KB_GTM_PredictiveAnalytics_Pipeline

## Scope
Base para forecasting de receita, pipeline, lead scoring, churn e win/loss. Fontes: KeyBanc/Sapphire 2024, Bridge Group 2024, materiais de GTM e churn.

## Forecasting de receita

### Weighted pipeline
\[
\text{Forecast} = \sum (\text{Deal Value}_i \times P_i)
\]

### Modelos alternativos
- ARIMA, ETS, Prophet para séries temporais.
- Regressão multivariada quando há drivers explícitos (spend, pipeline, team size).
- Bayesiano para contexto com poucos dados ou atualização contínua.

## Lead scoring

- Logistic regression, Random Forest, Gradient Boosting.
- Métricas úteis: AUC‑ROC, precision@k, recall@k, lift por decil.
- Lead‑to‑customer médio em SaaS situa‑se em torno de 1–5% (benchmarks 2024–2026).

## Churn prediction

- Kaplan‑Meier: curva de sobrevivência.
- Cox PH: hazard ratio por covariáveis.
- Health score: peso de uso, suporte, valor percebido e expansão.
- NRR acima de 100% indica expansão líquida; ~101% reportado em SaaS privado em 2024.

## Win/loss

- Teste de proporções para win rate por segmento.
- Estratificar por deal size, canal, gestão e pessoa.
- Benchmarks 2024: quota attainment na faixa de ~75% em SaaS privado.

## NOTAS DA MIGRAÇÃO (2026-10-31)

- [VERIFICAR] O original citava fontes como [web:NN] sem a lista de referências; as marcas foram removidas e os números pedem conferência.
