---
id: ref-gtm-sql-ga4-bigquery
tipo: referencia
origem: GTM_EST.md (KB_extra_ga4_sql)
atualizado: 2026-10-31
---

# SQL para GA4 + BigQuery

## Cohort por mês de cadastro

```sql
SELECT
  DATE_TRUNC(PARSE_DATE("%Y%m%d", event_date), MONTH) AS cohort_month,
  EXTRACT(YEAR FROM PARSE_DATE("%Y%m%d", event_date)) * 100 + EXTRACT(MONTH FROM PARSE_DATE("%Y%m%d", event_date)) AS cohort_yrmo,
  COUNT(DISTINCT user_pseudo_id) AS users
FROM `project.dataset.events_*`
WHERE event_name = "purchase"
GROUP BY 1, 2
ORDER BY 2;
```

## Funil por dia

```sql
WITH funnels AS (
  SELECT
    user_pseudo_id,
    DATE_TRUNC(PARSE_DATE("%Y%m%d", event_date), DAY) AS visit_day,
    LOGICAL_OR(event_name = "page_view") AS has_view,

## NOTAS DA MIGRAÇÃO (2026-10-31)

- [VERIFICAR] O original citava fontes como [web:NN] sem a lista de referências; as marcas foram removidas e os números pedem conferência.
