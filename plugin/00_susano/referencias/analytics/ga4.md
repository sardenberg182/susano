---
id: ref-analytics-ga4
tipo: referencia
origem: KB_GA4_MasterReference.md
atualizado: 2026-10-31
---

# Knowledge Base: Google Analytics 4 (GA4) - Master Reference

> Fontes: Analytics Mania (analyticsmania.com) + Métricas Boss (metricasboss.com.br)
> Compilado: Abril 2026 | Baseado em ~64 artigos analisados

---

## 1. Configuração

### Setup Inicial da Propriedade

GA4 usa modelo de dados baseado em eventos (vs pageview-based do Universal Analytics). Cada interação é um evento com parâmetros.

**Componentes principais:**
- Propriedade GA4 (uma por projeto/negócio)
- Data Streams: Web, iOS, Android (pode ter múltiplos)
- Measurement ID: G-XXXXXXXXXX (para web)
- Data retention: 2 meses (padrão) ou 14 meses (configurável)

### Enhanced Measurement (Automático)

Eventos automaticamente coletados quando Enhanced Measurement está ativo:
- `page_view` - visualização de página
- `scroll` - rolagem até 90% da página
- `click` (outbound) - cliques para outros domínios
- `site_search` - buscas no site (detecta parâmetro `q`, `s`, `search`, etc.)
- `video_engagement` - play, progress, complete de YouTube embeds
- `file_download` - downloads de arquivos (pdf, xlsx, docx, etc.)

### Eventos Recomendados (GA4)

Para e-commerce: `view_item_list`, `select_item`, `view_item`, `add_to_cart`, `view_cart`, `begin_checkout`, `add_shipping_info`, `add_payment_info`, `purchase`, `refund`

Para geração de leads: `sign_up`, `login`, `generate_lead`

Para conteúdo: `share`, `search`, `select_content`

**Fonte:** Analytics Mania - GA4 Tutorial for Beginners + Benefits of GA4

### Custom Dimensions (3 Escopos)

**Event-Scoped:** Anexadas a eventos individuais, variam por ocorrência.
```javascript
dataLayer.push({
  event: "purchase",
  customer_type: "enterprise"  // Event-scoped custom dimension
});
```

**User-Scoped:** Persistentes na sessão/lifetime do usuário.
```javascript
dataLayer.push({
  event: "page_view",
  user_account_status: "premium"  // User-scoped
});
```

**Item-Scoped:** Anexadas a itens em transações e-commerce.
```javascript
dataLayer.push({
  event: "view_item",
  ecommerce: {
    items: [{
      item_id: "SKU_12345",
      item_name: "Camiseta",
      custom_product_line: "limited_edition"  // Item-scoped
    }]
  }
});
```

**Configuração no GA4:**
1. Admin → Custom Definitions → Custom Dimensions
2. Definir scope (Event, User, Item)
3. Parameter name = exatamente como está no dataLayer
4. Aguardar 24h para propagação

**Limites:** 25 event-scoped, 25 user-scoped, 25 item-scoped (varia por plano)

**Fonte:** Analytics Mania - Custom Dimensions in GA4

### User Properties

```javascript
gtag('set', 'user_properties', {
  favorite_category: 'electronics',
  membership_level: 'gold'
});
```

---

## 2. Mensuração

### Cross-Domain Tracking

**Configuração:** Admin → Data Streams → Configure Tag Settings → Configure Your Domains

**Problemas comuns e soluções:**

| Problema | Solução |
|----------|---------|
| Domínio não na lista | Adicionar TODOS os domínios na configuração |
| Parâmetro `_gl` não propaga | Verificar links entre domínios, testar com Preview Mode |
| Self-referrals aparecendo | Configurar referral exclusion list |
| Subdomains | NÃO necessitam cross-domain (mesmo cookie domain) |
| Login redirect quebrando sessão | Adicionar domínio do IdP à lista |

**Fonte:** Analytics Mania - GA4 Cross-Domain Tracking Not Working | Métricas Boss - Cross-Domain Tracking no GA4

### Campaign Tracking (UTM)

**Parâmetros UTM:**
- `utm_source` - Origem (facebook, google, newsletter)
- `utm_medium` - Tipo (cpc, email, organic, social)
- `utm_campaign` - Nome da campanha (spring_sale)
- `utm_term` - Keyword (para paid search)
- `utm_content` - Variação (para A/B testing)

⚠️ **UTMs são case-sensitive no GA4.** `Facebook` ≠ `facebook` ≠ `FACEBOOK`

**Hierarquia de atribuição:**
1. Gclid (auto-tag do Google Ads) - prioridade máxima
2. UTM Parameters - manual
3. Referral headers - automático
4. Direct - sem dados de origem

**Fonte:** Analytics Mania - Track Campaigns in GA4 | Métricas Boss - Guia Completo de Parâmetros UTM

### E-commerce Tracking

**Funnel completo de eventos (ordem recomendada):**
1. `view_item_list` - listagem de produtos
2. `select_item` - clique em produto
3. `view_item` - página de produto
4. `add_to_cart` - adicionar ao carrinho
5. `view_cart` - ver carrinho
6. `begin_checkout` - iniciar checkout
7. `add_shipping_info` - informações de envio
8. `add_payment_info` - informações de pagamento
9. `purchase` - compra finalizada
10. `refund` - estorno (quando aplicável)

**Plataformas GA4-friendly (Métricas Boss):**
- Shopify: tracking nativo integrado
- WooCommerce: via plugin (ex: MonsterInsights)
- VTEX: implementação customizada necessária
- Magento: via extensão

**Fonte:** Analytics Mania - Benefits of GA4 | Métricas Boss - E-commerce GA4

### QR Code Tracking

Usar UTMs na URL do QR code para rastrear tráfego offline:
```
https://seusite.com/landing-page?utm_source=qr_code&utm_medium=offline&utm_campaign=flyer_abril
```

**Fonte:** Analytics Mania - Track QR Codes with GA4

---

## 3. Relatórios e Análise

### Custom Channel Groups

**Configuração:** Admin → Custom Definitions → Custom Channel Groups

- Condições baseadas em `utm_source` e `utm_medium`
- Avaliadas sequencialmente (primeira match ganha)
- Suporta regex patterns
- Retroativo desde a data de criação
- Útil para agrupar tráfego de parceiros, affiliates, etc.

**Fonte:** Analytics Mania - Custom Channel Groups in GA4

### Key Event Rate

Duas métricas distintas:
- **Session Key Event Rate:** sessões com key event / total sessões × 100
- **User Key Event Rate:** usuários com key event / total usuários × 100

Disponível em Reports → Engagement e em Explorations.

**Fonte:** Analytics Mania - Key Event Rate in GA4

### Exit Pages

GA4 **não tem relatório nativo** de exit pages (diferente do UA).

**Solução:** Criar exploração Free Form:
- Dimensão: Page Path
- Métrica: Exits (ou criar custom metric)
- Ordenar: Exits descending

**Fonte:** Analytics Mania - Exit Pages in GA4

### Demographics Reports

**Pré-requisito:** Ativar Google Signals em Admin → Data Collection

**Controle de ad personalization via GTM:**
```javascript
// Custom JavaScript variable para desativar personalização:
function() {
  return false;
}
```

Config no GTM: Field Name: `allow_ad_personalization_signals` → valor da variável acima.

**Fonte:** Analytics Mania - Demographics Reports in GA4

### Looker Studio + GA4

Integração direta via conector nativo GA4. Permite dashboards customizados combinando GA4 + Google Ads + Search Console. Refresh automático configurável.

**Fonte:** Analytics Mania - Looker Studio Tutorial | Métricas Boss - Looker Studio com GA4

### BigQuery Export

Export de dados brutos do GA4 para BigQuery. Permite queries SQL em eventos individuais. Habilitação em Admin → BigQuery Links.

**Fonte:** Analytics Mania - Benefits of GA4

### Data-Driven Attribution

Modelo de atribuição padrão do GA4. Usa machine learning para distribuir crédito entre touchpoints. Requer volume mínimo de dados para funcionar.

**Fonte:** Métricas Boss - Data Driven Attribution no GA4

---

## 4. Integrações

### GA4 + Google Ads

- Importação de conversões do GA4 para Google Ads
- Listas de audiência/remarketing
- Gclid auto-tagging para atribuição precisa
- Smart Bidding usando dados do GA4

**Fonte:** Métricas Boss - Google Ads e GA4 Integração

### GA4 + Search Console

Conectar para ver queries de busca orgânica nos relatórios do GA4.

### GA4 + Looker Studio

Conector nativo para dashboards personalizados.

### Measurement Protocol

Envio de eventos offline via API HTTP diretamente para GA4. Útil para conversões offline, CRM events, etc.

---

## 5. Troubleshooting GA4

### "No Data Available"

**Checklist de diagnóstico (em ordem):**
1. ✅ Measurement ID correto? (G-XXXXXXXXXX)
2. ✅ Network tab: requests para `google-analytics.com/g/collect`?
3. ✅ CSP headers bloqueando? Whitelist `google-analytics.com`
4. ✅ DebugView mostra eventos? (real-time vs reports = 24h+ delay)
5. ✅ Container ID matches?
6. ✅ Extensões bloqueando? (testar em incognito)
7. ✅ Data Stream configurado corretamente?

**Fonte:** Analytics Mania - No Data Available in GA4

### session_start Missing

**Causas comuns:**
- Tag GA4 não dispara no primeiro pageview
- Consent mode bloqueando `analytics_storage`
- Filtros de IP excluindo tráfego interno
- Data retention expirada

**Fonte:** Analytics Mania - session_start Missing in GA4

### Duplicate Events

**Causas:**
- Tag disparando múltiplas vezes (trigger sem condição)
- dataLayer push duplicado
- SPA re-rendering causando re-fire
- Enhanced Measurement + tag manual = duplicação

**Soluções:**
- Verificar trigger conditions no Preview Mode
- Adicionar flag de controle JavaScript
- Usar trigger exceptions
- Desativar enhanced measurement se tracking manual

**Fonte:** Analytics Mania - Duplicate Events in GA4

### DebugView Not Working

**Soluções:**
- Garantir `debug_mode: true` no evento (via GTM ou URL parameter `?debug_mode=true`)
- Testar em janela anônima
- Verificar se IP não está filtrado
- Aguardar alguns segundos (não é instantâneo)

**Fonte:** Analytics Mania - DebugView Not Working

### AI Traffic

Tráfego de bots de AI (ChatGPT, Perplexity, Claude, etc.) pode inflacionar métricas. Identificação via user agent strings e criação de segmentos/filtros específicos para isolar esse tráfego.

**Fonte:** Analytics Mania - AI Traffic in GA4

### Fontes de Tráfego Facebook

| Domínio | O que é | Como classificar |
|---------|---------|-----------------|
| `l.facebook.com` | Link Shim desktop | Social / facebook |
| `lm.facebook.com` | Link Shim mobile | Social / facebook |
| `m.facebook.com` | Site mobile | Social / facebook |
| `facebook.com` | Site desktop | Social / facebook |

**Fonte:** Métricas Boss - Fontes de tráfego l.facebook e lm.facebook
