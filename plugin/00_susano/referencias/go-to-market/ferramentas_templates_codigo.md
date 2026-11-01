---
id: ref-gtm-ferramentas-templates-codigo
tipo: referencia
origem: GTM_EST.md (KB_GTM_Tools_Code_Templates)
atualizado: 2026-10-31
---

# KB_GTM_Tools_Code_Templates

## Python / R

- Bibliotecas recomendadas: pandas, scipy, statsmodels, scikit‑learn, prophet, lifetimes, lifelines, R packages survival/forecast/caret.

## SQL padrão

- Cohort analysis.
- Funnel analysis.
- RFM scoring.
- LTV por coorte.
- CAC por canal.

### Exemplo de cohort (SQL)

```sql
SELECT
  DATE_TRUNC(signup_date, MONTH) AS cohort_month,
  COUNT(DISTINCT user_id) AS users
FROM users
GROUP BY 1;
```

### Exemplo de funil

```sql
WITH funnels AS (
  SELECT
    user_id,
    LOGICAL_OR(event = 'view') AS has_view,
    LOGICAL_OR(event = 'purchase') AS has_purchase
  FROM events
  GROUP BY 1
)
SELECT
  COUNT(*) AS visits,
  COUNTIF(has_purchase) AS purchases,
  SAFE_DIVIDE(1.0 * purchases, COUNT(*)) AS cvr
FROM funnels;
```

## Sheets / Excel

- Sample size calculator.
- Weighted pipeline forecast.
- Monte Carlo com RAND().
- IC de proporção.

## NOTAS DA MIGRAÇÃO (2026-10-31)

- [VERIFICAR] O original citava fontes como [web:NN] sem a lista de referências; as marcas foram removidas e os números pedem conferência.
