---
id: ref-gtm-experimentacao
tipo: referencia
origem: GTM_EST.md (KB_GTM_Experimentation_Testing)
atualizado: 2026-10-31
---

# KB_GTM_Experimentation_Testing

## Scope
A/B, power analysis, MAB, MVT e vieses estatísticos em GTM.

## Frameworks de teste

- A/B fixed‑horizon: simples, governável.
- Sequential testing: decisão mais rápida, mais complexo.
- Multi‑armed bandit: maximiza recompensa durante o teste.
- MVT: combina variações de múltiplos elementos; pede bastante tráfego.

## Power analysis (esboço)

- n cresce quando baseline cai ou MDE diminui.
- Sempre calcular por variante e por segmento chave.

### Vieses comuns
- Simpson’s Paradox: correlação global esconde contradição por grupo.
- Survivorship bias: analisar só clientes que permanecem.
- Regression to the mean: supor que oscilação extrema persiste.

## Tests de GTM

- Pricing: Van Westendorp, Gabor‑Granger, conjoint.
- Messaging: value proposition, prova social, testemunhos.
- Pages: headline, CTA, proof, layout.
- Email: subject line, send time, copy, CTA.

## NOTAS DA MIGRAÇÃO (2026-10-31)

- [VERIFICAR] O original citava fontes como [web:NN] sem a lista de referências; as marcas foram removidas e os números pedem conferência.
