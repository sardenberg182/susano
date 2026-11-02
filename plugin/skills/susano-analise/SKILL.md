---
name: susano-analise
description: Data analysis in the Susano standard (FATO → análise vs target → PA): definitions first, raw rows outside version control, numbers computed in Python, totals reconciled, targets only from the project's own records. Use for any metric, funnel, campaign, CRM or revenue question.
---

Always answer in PT-BR.

1. **Scope**: which frente (client, account or product), period with time zone (project default America/Sao_Paulo), metric definitions, currency, denominator, attribution model. One question with defaults when something blocking is missing.
2. **Source**: a connector or MCP the person has, or an export the person provides. Confirm schema and field availability through metadata before querying. Raw rows go to a local folder outside version control, never to a committed file.
3. **Compute in Python** every number shown. Reconcile your totals with the source's own total; explain any gap and mark disagreement between sources as [CONTRADIÇÃO].
4. **Compare** with the targets this project registers. No target: [LACUNA] plus who defines it. External benchmarks only with source and date; Sarden's references live in the `susano-performance` and `susano-gtm` skills (`${CLAUDE_PLUGIN_ROOT}/00_susano/referencias/`).
5. **Write the output** as FATO (numbers with source and timestamp) → análise vs target → PA (próximas ações with owner and date). Markers ([DADO], [INFERÊNCIA], [VERIFICAR], [LACUNA], [CONTRADIÇÃO]) on every claim in internal documents and drafts; a client deliverable, published playbook or slide carries none: resolve open points by asking before writing. Aggregates only, never user-level rows or personal data.

Platform notes:
- HubSpot MCP SQL has no JOIN, DISTINCT, CASE or HAVING: paginate raw rows by date slices and aggregate in Python.
- Meta Ads MCP truncates long lists: pull again sorted by spend to be sure nothing relevant was cut.
- Google Ads: confirm which server and customer is accessible, and check field metadata before each query. Under an MCC, query with the leaf account's `customer_id`; `search_term_view` requires `advertising_channel_type = 'SEARCH'`; `conversion_action.primary_for_goal` shows what the auction optimizes for.
- Exports: Meta Ads Manager exports XML Spreadsheet (`ss:Index` shifts columns; the first row is the total); Google Ads CSV is `utf-16`, `sep='\t'`, `skiprows=2`, "Resultados" split by semicolon, the "Total:" row identified by its status. Meta Ads Manager in the browser is a virtualized table: export CSV for the full base; ask for the widest base (all columns, longest period, campaign, ad set and ad) and look at the time breakdown first.
- HubSpot MCP does not expose property history. A business plan or financial model is read through the `.xlsx` formulas (openpyxl), never through a Markdown conversion that destroys them. A dashboard delivered as an image: ask for a screenshot per section or the CSV behind it.
