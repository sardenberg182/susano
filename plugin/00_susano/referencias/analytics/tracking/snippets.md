---
id: ref-analytics-tracking-snippets
tipo: referencia
origem: KB_Tracking_Snippets_Library.md
atualizado: 2026-10-31
---

# Knowledge Base: Tracking Snippets Library

> Fontes: Analytics Mania + Métricas Boss | Compilado: Abril 2026
> Todos os snippets prontos para uso em GTM Custom HTML tags ou Custom JS Variables

---

## 1. DataLayer Pushes

### 1.1 Inicialização Segura do DataLayer

```javascript
// SEMPRE antes do snippet GTM
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  'visitorType': 'member',
  'pageType': 'article',
  'articleCategory': 'tutorials',
  'articleTitle': document.title,
  'articleAuthor': 'Author Name'
});
```
**Uso:** Inserir no `<head>` antes do GTM para dados disponíveis no primeiro page view.
**Fonte:** Analytics Mania - Data Layer in GTM

### 1.2 Page View com Dados de Página

```javascript
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  'event': 'page_view',
  'page': {
    'title': document.title,
    'url': window.location.href,
    'path': window.location.pathname,
    'referrer': document.referrer
  }
});
```
**Fonte:** Analytics Mania - Data Layer in GTM

### 1.3 E-commerce: View Item

```javascript
dataLayer.push({
  event: "view_item",
  ecommerce: {
    currency: "BRL",
    value: 99.99,
    items: [{
      item_id: "SKU_12345",
      item_name: "Camiseta Exemplo",
      item_category: "Vestuário",
      item_brand: "Marca X",
      price: 99.99,
      quantity: 1
    }]
  }
});
```
**Fonte:** Analytics Mania - Custom Dimensions in GA4

### 1.4 E-commerce: Add to Cart

```javascript
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
```

### 1.5 E-commerce: Purchase

```javascript
dataLayer.push({
  event: "purchase",
  ecommerce: {
    transaction_id: "T_12345",
    value: 99.99,
    tax: 10.00,
    shipping: 5.00,
    currency: "BRL",
    coupon: "DESCONTO10",
    items: [{
      item_id: "SKU_12345",
      item_name: "Camiseta Exemplo",
      item_category: "Vestuário",
      item_brand: "Marca X",
      quantity: 1,
      price: 99.99
    }]
  }
});
```
**Fonte:** Analytics Mania - Benefits of GA4

### 1.6 Custom Event Genérico

```javascript
dataLayer.push({
  'event': 'engagement',
  'engagement_type': 'cta_click',
  'element_class': 'hero-cta',
  'element_text': 'Comece agora'
});
```
**Fonte:** Analytics Mania - Custom Event Trigger

### 1.7 Video Event

```javascript
dataLayer.push({
  'event': 'video_start',
  'video_title': 'Product Demo',
  'video_duration': 120,
  'video_provider': 'youtube'
});
```
**Fonte:** Analytics Mania - Custom Event Trigger

---

## 2. Custom HTML Tags (GTM)

### 2.1 TypeForm Tracking

```html
<script>
window.addEventListener("message", function(event){
  if (event.origin === "https://form.typeform.com" &&
      (event.data.type === "form-started" ||
       event.data.type === "form-submit")) {
    window.dataLayer.push({
      'event': event.data.type.replace("-", "_"),
      'form_id': event.data.formId,
      'form_response_id': event.data.formResponseId || ''
    });
  }
});
</script>
```
**Trigger:** All Pages (ou páginas com TypeForm)
**Fonte:** Analytics Mania - Track Typeform with GTM

### 2.2 Calendly Tracking (com deduplicação)

```html
<script>
var lastCalendlyEvent = null;
window.addEventListener('message', function(e) {
  if (e.data.event && e.data.event.indexOf('calendly') === 0) {
    var eventName = e.data.event.split('.')[1];
    var allowed = ['event_type_viewed', 'profile_page_viewed',
                   'date_and_time_selected', 'event_scheduled'];
    if (allowed.includes(eventName) && eventName !== lastCalendlyEvent) {
      lastCalendlyEvent = eventName;
      window.dataLayer.push({
        'event': 'calendly_' + eventName,
        'calendly_event_type': eventName
      });
    }
  }
});
</script>
```
**Trigger:** All Pages (ou páginas com Calendly)
**Fonte:** Analytics Mania - Track Calendly with GTM

### 2.3 HTML5 Video Tracking (com milestones)

```html
<script>
var videos = document.getElementsByTagName('video');
var videoProgress = {};

for (var i = 0; i < videos.length; i++) {
  (function(video, id) {
    videoProgress[id] = { 25: false, 50: false, 75: false };

    video.addEventListener('play', function() {
      window.dataLayer.push({
        'event': 'video_play',
        'video_title': this.title || this.src.split('/').pop(),
        'video_duration': Math.round(this.duration),
        'video_provider': 'html5'
      });
    });

    video.addEventListener('pause', function() {
      window.dataLayer.push({
        'event': 'video_pause',
        'video_current_time': Math.round(this.currentTime),
        'video_provider': 'html5'
      });
    });

    video.addEventListener('ended', function() {
      window.dataLayer.push({
        'event': 'video_complete',
        'video_provider': 'html5'
      });
    });

    video.addEventListener('timeupdate', function() {
      var pct = (this.currentTime / this.duration) * 100;
      [25, 50, 75].forEach(function(milestone) {
        if (pct >= milestone && !videoProgress[id][milestone]) {
          videoProgress[id][milestone] = true;
          window.dataLayer.push({
            'event': 'video_progress',
            'video_percent': milestone,
            'video_provider': 'html5'
          });
        }
      });
    });
  })(videos[i], 'video_' + i);
}
</script>
```
**Trigger:** DOM Ready (páginas com vídeo)
**Fonte:** Analytics Mania - Track HTML5 Video Player

### 2.4 YouTube IFrame API Tracking

```html
<script>
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

function onYouTubeIframeAPIReady() {
  var iframes = document.querySelectorAll('iframe[src*="youtube.com"]');
  iframes.forEach(function(iframe, i) {
    var player = new YT.Player(iframe, {
      events: {
        'onStateChange': function(event) {
          var states = { 0: 'complete', 1: 'play', 2: 'pause' };
          var state = states[event.data];
          if (state) {
            window.dataLayer.push({
              'event': 'video_' + state,
              'video_provider': 'youtube',
              'video_title': event.target.getVideoData().title,
              'video_duration': Math.round(event.target.getDuration())
            });
          }
        }
      }
    });
  });
}
</script>
```
**Trigger:** Window Loaded
**Fonte:** Analytics Mania - YouTube Tracking GTM

### 2.5 Meta Pixel Base Code

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
**Trigger:** All Pages
**Fonte:** Analytics Mania - Facebook Pixel with GTM

### 2.6 Meta Pixel: Purchase Event

```html
<script>
fbq('track', 'Purchase', {
  value: {{DL - ecommerce.value}},
  currency: {{DL - ecommerce.currency}},
  content_ids: {{DL - ecommerce.item_ids}},
  content_type: 'product',
  num_items: {{DL - ecommerce.items.length}}
});
</script>
```
**Trigger:** Custom Event = purchase

---

## 3. Custom JavaScript Variables (GTM)

### 3.1 Mobile Detection

```javascript
function() {
  return /iPhone|iPad|iPod|Android|webOS|BlackBerry|Windows Phone/i.test(navigator.userAgent);
}
```
**Retorna:** `true` ou `false`
**Fonte:** Analytics Mania - Custom Variables

### 3.2 Downloaded File Name

```javascript
function() {
  var url = {{Click URL}};
  return url ? url.split('/').pop().split('?')[0] : '';
}
```
**Retorna:** nome do arquivo (ex: `relatorio.pdf`)
**Fonte:** Analytics Mania - Custom Variables

### 3.3 Screen Width

```javascript
function() {
  return window.innerWidth;
}
```
**Uso:** Breakpoint tracking, responsive analytics.
**Fonte:** Analytics Mania - Custom Variables

### 3.4 Page Title

```javascript
function() {
  return document.title;
}
```
**Fonte:** Analytics Mania - Custom Variables

### 3.5 Time on Page (em segundos)

```javascript
function() {
  return Math.round((Date.now() - performance.timing.navigationStart) / 1000);
}
```

### 3.6 URL Parameter Extractor

```javascript
function() {
  var param = 'utm_campaign'; // alterar conforme necessário
  var url = new URL(window.location.href);
  return url.searchParams.get(param) || '';
}
```

---

## 4. Consent Mode Setup

### 4.1 Default (denied)

```javascript
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'analytics_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'wait_for_update': 500
});
```

### 4.2 Update (granted)

```javascript
gtag('consent', 'update', {
  'ad_storage': 'granted',
  'analytics_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted'
});
```

**Fonte:** Analytics Mania - Consent Mode + Benefits of GA4

---

## 5. Cookie Utilities

### 5.1 Read Cookie

```javascript
function getCookie(name) {
  var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? decodeURIComponent(match[2]) : null;
}
```

### 5.2 Write Cookie

```javascript
function setCookie(name, value, days) {
  var expires = "";
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + encodeURIComponent(value) + expires + "; path=/; SameSite=Lax; Secure";
}
```

### 5.3 Delete Cookie

```javascript
function deleteCookie(name) {
  document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}
```

**Fonte:** Analytics Mania - Cookies with GTM

---

## 6. GTM Server-Side: Cloud Shell Setup

```bash
# Acessar Cloud Shell
# https://ssh.cloud.google.com/cloudshell

# Configurar projeto
gcloud config set project SEU_PROJECT_ID

# Executar script de setup do sGTM
bash -c "$(curl -fsSL https://googletagmanager.com/static/serverjs/setup.sh)"

# Seguir instruções, aceitar padrões (Enter) e confirmar com 'y'
```

**Fonte:** Métricas Boss - GTM Server-Side App Engine para Cloud Run

---

## 7. Checklists de Referência Rápida

### Setup Novo Cliente (18 itens)

- [ ] Criar conta GTM + container web
- [ ] Instalar snippet GTM no `<head>` e `<body>`
- [ ] Criar propriedade GA4 + data stream web
- [ ] Tag GA4 Configuration no GTM (All Pages)
- [ ] Consent Mode v2 (default denied + update on consent)
- [ ] Enhanced Measurement ativado
- [ ] Conversion Linker tag (All Pages)
- [ ] Google Ads Conversion Tracking tag(s)
- [ ] Meta Pixel via Custom HTML + eventos
- [ ] DataLayer para e-commerce (se aplicável)
- [ ] Cross-domain tracking (se múltiplos domínios)
- [ ] Custom dimensions relevantes
- [ ] Key events/conversões definidos no GA4
- [ ] GA4 conectado ao Google Ads + Search Console
- [ ] Dashboard básico no Looker Studio
- [ ] Naming conventions documentadas
- [ ] Testar via Preview Mode + DebugView
- [ ] Publicar container GTM

### Auditoria de Tracking (15 itens)

- [ ] GTM snippet correto no `<head>`?
- [ ] DataLayer inicializado ANTES do GTM?
- [ ] Tags disparando corretamente? (Preview Mode)
- [ ] Eventos chegando no GA4? (DebugView)
- [ ] Conversões no Google Ads?
- [ ] Meta Pixel disparando? (Pixel Helper)
- [ ] Consent Mode funcionando?
- [ ] Cross-domain preservando sessão?
- [ ] E-commerce data completo?
- [ ] Custom dimensions populando?
- [ ] Sem eventos duplicados?
- [ ] UTMs consistentes?
- [ ] Filtros de IP interno ativos?
- [ ] Enhanced Conversions configurado?
- [ ] Server-side operacional? (se aplicável)

### QA Pré-Campanha (10 itens)

- [ ] UTMs corretos no URL de destino?
- [ ] Landing page sem erros de JS?
- [ ] Tags disparam na landing page? (Preview)
- [ ] Conversão dispara no thank-you/purchase?
- [ ] Google Ads registra conversão?
- [ ] Meta Pixel registra evento?
- [ ] Cross-domain funcionando? (se aplicável)
- [ ] Consent Mode respeitado?
- [ ] Mobile tracking funciona?
- [ ] Valores de conversão corretos?

## NOTAS DA MIGRAÇÃO (2026-10-31)

- Biblioteca canônica de snippets: os de pixels e server-side remetem a ela.
