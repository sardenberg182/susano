---
id: ref-analytics-google-tag-manager
tipo: referencia
origem: KB_GTM_MasterReference.md
atualizado: 2026-10-31
---

# Knowledge Base: Google Tag Manager (GTM) - Master Reference

> Fontes: Analytics Mania (analyticsmania.com) + Métricas Boss (metricasboss.com.br)
> Compilado: Abril 2026 | 47 artigos AM + 17 artigos MB analisados

---

## 1. Setup e Configuração Inicial

### Instalação do GTM

O código do GTM deve ser inserido em duas partes:
- **Script principal** no `<head>` (obrigatório)
- **noscript fallback** logo após abertura do `<body>`

```html
<!-- Google Tag Manager (no <head>) -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXX');</script>

<!-- Google Tag Manager (noscript) logo após <body> -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

**Fonte:** Analytics Mania - GTM Tutorial for Beginners

### Estrutura de Contas e Containers

- Uma conta pode ter múltiplos containers
- Cada container possui ID único (GTM-XXXXX)
- Tipos de container: Web, AMP, iOS, Android, Server
- Ambientes (Environments): Live, Latest, Dev/staging personalizado
- Versionamento automático a cada publicação

### Convenção de Nomenclatura

**NUNCA usar emojis** em nomes de tags/triggers/variáveis. Emojis causam problemas de encoding UTF-16, falhas em JSON serialization e quebra de operações de string em JavaScript.

```javascript
// Problema demonstrado:
const emoji = '🚀';
console.log(emoji.length); // Retorna 2, não 1!

const emojiComplexa = '👨‍👩‍👧‍👦';
console.log(emojiComplexa.length); // Retorna 11!
```

**Esquema recomendado:** `[Plataforma]_[Tipo]_[Função]`

Exemplos:
- `GA4_EV_Compra_Concluida`
- `FB_CONV_Lead`
- `GADS_REM_Carrinho_Aberto`
- `GA4_CFG_Config_Principal`

**Fonte:** Métricas Boss - Por que não devemos usar emojis no GTM

---

## 2. Tags

### Tags de Pageview e Eventos GA4

A tag GA4 Configuration (tipo Google Tag) é obrigatória e deve disparar em All Pages. Event tags referenciam a configuração e enviam eventos específicos.

```
Tag Type: Google Analytics: GA4 Event
Configuration Tag: {{GA4 Config}}
Event Name: purchase (ou evento customizado)
Event Parameters:
  transaction_id: {{DL - transaction_id}}
  value: {{DL - value}}
  currency: {{DL - currency}}
```

### Tags de Conversão Google Ads

Requer duas tags trabalhando juntas:
1. **Conversion Linker** → dispara em ALL PAGES (essencial para capturar gclid)
2. **Google Ads Conversion Tracking** → dispara no evento de conversão

```
Tag Type: Google Ads Conversion Tracking
Conversion ID: AW-XXXXXXXXX
Conversion Label: XXXXXXXXXXXXXXXXXXX
Conversion Value: {{DL - value}}
Currency Code: {{DL - currency}}
Transaction ID: {{DL - transaction_id}}
```

**Fonte:** Analytics Mania - Google Ads Conversion Tracking with GTM

### Meta Pixel via GTM (Custom HTML)

```html
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'SEU_PIXEL_ID');
fbq('track', 'PageView');
</script>
```

Eventos padrão Meta: `Lead`, `Purchase`, `AddToCart`, `CompleteRegistration`, `ViewContent`, `InitiateCheckout`, `AddPaymentInfo`, `Search`.

**Fonte:** Analytics Mania - Facebook Pixel with GTM

### Tags Customizadas (Custom HTML)

Para cenários que não têm tag nativa no GTM. Exemplo de push para dataLayer:

```html
<script>
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  'event': 'engagement',
  'engagement_type': 'click',
  'element_class': 'cta-button'
});
</script>
```

**Importante:** Toda Custom HTML tag deve incluir `window.dataLayer = window.dataLayer || [];` como safety check antes de qualquer push.

---

## 3. Triggers (Acionadores)

### Tipos Principais

| Tipo | Quando Dispara | Uso Típico |
|------|---------------|------------|
| Page View | Container Loaded, DOM Ready, Window Loaded | Tags de config, pageview |
| Click - All Elements | Qualquer clique na página | Botões, elementos genéricos |
| Click - Just Links | Clique em `<a>` | Outbound links, downloads |
| Form Submission | Envio de formulário | Lead capture |
| Scroll Depth | % vertical/horizontal | Engajamento com conteúdo |
| Element Visibility | Elemento entra no viewport | Impressões de banners, seções |
| Custom Event | dataLayer.push com 'event' | Qualquer evento customizado |
| History Change | Mudança de URL em SPA | Navegação em single-page apps |
| Timer | Intervalo de tempo | Time on page, engagement |

### Custom Event Trigger

```javascript
// No site (dataLayer push):
dataLayer.push({
  'event': 'video_start',
  'video_title': 'Product Demo',
  'video_duration': 120
});
```

```
// No GTM:
Trigger Type: Custom Event
Event Name: video_start  ← CASE-SENSITIVE!
Fire on: All Custom Events (ou condição específica)
```

⚠️ **O nome do evento é case-sensitive.** `video_start` ≠ `Video_Start` ≠ `VIDEO_START`

**Fonte:** Analytics Mania - Custom Event Trigger

### Trigger Groups

Permitem combinar múltiplos triggers para que uma tag só dispare quando TODOS os triggers do grupo forem ativados na mesma sessão/página.

**Caso de uso:** Tag só dispara quando usuário:
1. Viu o produto (trigger 1)
2. Adicionou ao carrinho (trigger 2)
3. Iniciou checkout (trigger 3)

**Fonte:** Analytics Mania - Trigger Groups in GTM

### Element Visibility Trigger

Configuração:
- **Selection Method:** ID ou CSS Selector
- **Minimum Percent Visible:** ex: 50%
- **Observe DOM Changes:** ativar para SPAs
- **Fire on:** Once per page / Once per element / Every time

**Fonte:** Analytics Mania - Track Element Visibility

### 7 Métodos de Form Tracking

1. **GTM Form Submission Trigger** - para formulários tradicionais
2. **Thank You Page URL** - trigger de Page View com regex `/thank-you|confirmation|success`
3. **AJAX Form Listener** - Custom HTML com interceptação de XMLHttpRequest
4. **Custom Event via dataLayer** - push no callback de sucesso do form
5. **Element Visibility (Thank You)** - quando elemento de sucesso aparece
6. **postMessage Listener** - para iframes (TypeForm, Calendly, etc.)
7. **Mutation Observer** - para mudanças dinâmicas no DOM

**Fonte:** Analytics Mania - Form Tracking 7 Methods

---

## 4. Variáveis

### 7 Custom Variables Essenciais

**1. Page Title (JavaScript Variable):**
```javascript
function() { return document.title; }
```

**2. Downloaded File Name:**
```javascript
function() { return {{Click URL}}.split('/').pop(); }
```

**3. Mobile Detection:**
```javascript
function() {
  return /iPhone|iPad|iPod|Android|webOS|BlackBerry|Windows Phone/i.test(navigator.userAgent);
}
```

**4. Screen Width:**
```javascript
function() { return window.innerWidth; }
```

**5. Lookup Table - Domain Mapping:**
Input: `{{Page Hostname}}` → Output: nome da unidade de negócio

**6. URL Parameter Variable:**
Tipo: URL Variable | Component: Query | Query Key: `utm_source`

**7. Data Layer Variables:**
Acessam propriedades do dataLayer com dot notation: `ecommerce.items[0].price`

**Fonte:** Analytics Mania - 7 Must-Have GTM Custom Variables

### Variáveis Built-in Essenciais

Ativar em Variables > Built-In Variables > Configure:

**Pages:** Page URL, Page Hostname, Page Path, Referrer
**Clicks:** Click Element, Click Classes, Click ID, Click URL, Click Text
**Forms:** Form Element, Form Classes, Form ID, Form URL, Form Text
**History:** History Source, New History Fragment, Old History Fragment
**Utilities:** Container ID, Container Version, Debug Mode, HTML ID

---

## 5. Data Layer

### Estrutura e Boas Práticas

O dataLayer é um array JavaScript que serve como ponte entre o site e o GTM. **DEVE ser inicializado ANTES do snippet do GTM.**

```javascript
// ANTES do GTM:
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  'visitorType': 'member',
  'pageType': 'article',
  'articleCategory': 'tutorials',
  'articleTitle': document.title,
  'articleAuthor': 'Author Name'
});
```

### Push COM evento vs SEM evento

```javascript
// COM evento - aciona triggers de Custom Event:
dataLayer.push({
  'event': 'form_submit',
  'formName': 'Contact Form',
  'formFields': 3
});

// SEM evento - apenas armazena dados para variáveis:
dataLayer.push({
  'formName': 'Contact Form',
  'formFields': 3
});
```

### E-commerce Data Layer (GA4 Format)

```javascript
// view_item
dataLayer.push({
  event: "view_item",
  ecommerce: {
    currency: "BRL",
    value: 99.99,
    items: [{
      item_id: "SKU_12345",
      item_name: "Camiseta Exemplo",
      item_category: "Vestuário",
      price: 99.99,
      quantity: 1
    }]
  }
});

// add_to_cart
dataLayer.push({
  event: "add_to_cart",
  ecommerce: {
    currency: "BRL",
    value: 99.99,
    items: [{
      item_id: "SKU_12345",
      item_name: "Camiseta Exemplo",
      price: 99.99,
      quantity: 1
    }]
  }
});

// purchase
dataLayer.push({
  event: "purchase",
  ecommerce: {
    transaction_id: "T_12345",
    value: 99.99,
    tax: 10.00,
    shipping: 5.00,
    currency: "BRL",
    items: [{
      item_id: "SKU_12345",
      item_name: "Camiseta Exemplo",
      quantity: 1,
      price: 99.99
    }]
  }
});
```

**Fonte:** Analytics Mania - Data Layer in GTM + Benefits of GA4

### Convenções de Nomenclatura

- Usar camelCase consistentemente
- Evitar caracteres especiais e espaços
- Documentar schema para equipe
- Nomes auto-descritivos

**Fonte:** Analytics Mania - Data Layer in GTM | Métricas Boss - Como usar o Data Layer

---

## 6. Debug e QA

### Preview Mode do GTM

O Preview Mode exibe um painel de debug com:
- **Event Timeline:** eventos na ordem que ocorreram
- **Tags Tab:** quais tags dispararam (e quais não)
- **Variables Tab:** valores resolvidos de cada variável
- **Data Layer Tab:** estado completo do dataLayer naquele momento

### 5 Eventos Padrão na Timeline

1. **Container Loaded** - GTM carregou
2. **DOM Ready** - DOM parseado
3. **Window Loaded** - tudo carregou (imagens, scripts)
4. **Click** - clique detectado
5. **Form Submit** - formulário enviado

### Troubleshooting Matrix

| Problema | Investigar | Solução |
|----------|-----------|---------|
| Tag não dispara | Triggers tab | Verificar condições do trigger |
| Dados errados | Variables tab | Verificar push do dataLayer |
| Variável vazia | Data Layer tab | Garantir push antes do disparo |
| Evento não aparece | Event timeline | Verificar se evento ocorre na página |
| GA4 não recebe | Tag firing status | Verificar Measurement ID |
| Eventos duplicados | Timeline count | Adicionar exceções ao trigger |
| Preview não abre | Extensões do browser | Desativar ad blockers e extensões |

**Fonte:** Analytics Mania - GTM Debug Mode

### Chrome Extensions Recomendadas

- **Tag Assistant Legacy** - visualiza tags disparadas
- **Adswerve dataLayer Inspector** - inspeciona dataLayer em tempo real
- **WASP** (Web Analytics Solution Profiler) - análise completa de tags
- **Omnibug** - monitora requests de analytics
- **GTM/GA Debugger** - debug detalhado

**Fonte:** Analytics Mania - GTM Chrome Extensions

### 21 Erros Comuns de GTM

**Erros Críticos de Data Layer:**
1. dataLayer.push() APÓS script do GTM → dados perdidos no page load
2. Naming inconsistente (camelCase vs snake_case) → matching failures
3. Emojis em nomes → UTF-16 encoding issues

**Erros de Trigger:**
4. Trigger muito amplo → captura eventos não intencionais
5. Missing trigger exceptions → tags disparam onde não deveriam
6. Event name com case errado → trigger não ativa
7. Variáveis no trigger incorretamente scoped

**Erros de Container:**
8. GTM code fora do head tag
9. Sem versionamento/documentação
10. IDs hardcoded em tags
11. Dados sensíveis em tags
12. Publicação sem teste no Preview Mode

**Checklist de Auditoria de Container:**
- [ ] GTM code no head tag
- [ ] dataLayer inicializado antes do GTM
- [ ] Naming conventions consistentes
- [ ] Todos os triggers documentados
- [ ] Sem IDs hardcoded ou dados sensíveis
- [ ] Preview Mode testado antes de publicar
- [ ] Variable data types verificados
- [ ] Trigger conditions validadas

**Fonte:** Analytics Mania - 21 Common GTM Mistakes
