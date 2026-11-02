---
id: ref-analytics-tracking-pixels
tipo: referencia
origem: KB_Pixels_TrackingSetup.md
atualizado: 2026-11-01
revisao_pendente: Sarden (edição v0.3.0: Typeform aponta para o snippet único, YouTube com enablejsapi e nomes do Enhanced Measurement)
---

# Knowledge Base: Pixels e Tracking de Plataformas de Ads

> Convenção deste arquivo desde a v0.3.0: `atualizado` no frontmatter é a data da última edição, não de verificação. Fato de produto vale pela data de verificação escrita ao lado dele ("verificado em DD/MM/AAAA"); sem essa data, é [VERIFICAR] antes de usar.

> Fontes: Analytics Mania + Métricas Boss | Compilado: Abril 2026

---

## 1. Meta Pixel (Facebook/Instagram)

### Instalação via GTM (Custom HTML)

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

### Eventos Padrão Meta

```javascript
// Lead
fbq('track', 'Lead', { content_name: 'Formulário Contato' });

// Purchase
fbq('track', 'Purchase', {
  value: 99.99,
  currency: 'BRL',
  content_ids: ['SKU_12345'],
  content_type: 'product'
});

// AddToCart
fbq('track', 'AddToCart', {
  value: 99.99,
  currency: 'BRL',
  content_ids: ['SKU_12345']
});

// CompleteRegistration
fbq('track', 'CompleteRegistration', { content_name: 'Signup' });

// ViewContent
fbq('track', 'ViewContent', {
  content_ids: ['SKU_12345'],
  content_type: 'product',
  value: 99.99,
  currency: 'BRL'
});

// InitiateCheckout
fbq('track', 'InitiateCheckout', { value: 199.99, currency: 'BRL' });
```

### Conversions API (CAPI)

A CAPI envia eventos server-to-server, independente de cookies ou ad blockers.

**Case Study - Malásia Bottoms Lab (Métricas Boss):**
- Teste A/B: CAPI com parâmetros vs CAPI sem parâmetros
- Resultado: **+24% em vendas** com parâmetros completos
- **-20%** no custo por compra
- Período: 16-30 outubro 2021

**Case Study - Ray-Ban (Métricas Boss):**
- Teste A/B: Pixel sozinho vs Pixel + CAPI
- Resultados com Pixel + CAPI:
  - **+36%** em alcance
  - **-19%** no CPM
  - **+10%** em vendas online
  - **-7%** no custo por conversão
- Período: 11-25 julho 2022

### Deduplicação de Eventos (Pixel + CAPI)

Quando usa Pixel e CAPI simultaneamente, eventos duplicados são enviados. Meta descarta duplicatas automaticamente usando `event_id`.

**Implementação:** Gerar um `event_id` único no frontend, enviar tanto via Pixel quanto via CAPI com o mesmo ID.

```javascript
// No frontend (Pixel):
var eventId = 'evt_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
fbq('track', 'Purchase', { value: 99.99, currency: 'BRL' }, { eventID: eventId });

// No backend (CAPI): enviar mesmo eventId no campo event_id
```

**Fonte:** Analytics Mania + Métricas Boss

### Fontes de Tráfego Facebook no GA4

| Domínio | Descrição |
|---------|-----------|
| `l.facebook.com` | Link Shim (redirecionamento de segurança) - desktop |
| `lm.facebook.com` | Link Shim - mobile |
| `m.facebook.com` | Site mobile do Facebook |
| `facebook.com` | Site desktop |

Todos devem ser agrupados como **Social / facebook** nos Channel Groups.

**Fonte:** Métricas Boss

### Mudança de Label: "Sponsored" → "Ad"

A Meta substituiu o label "Sponsored" por "Ad" em anúncios. Impacto na identificação visual de conteúdo pago pelos usuários.

**Fonte:** Métricas Boss

---

## 2. Google Ads Conversion Tracking

### Setup via GTM

**Tag 1: Conversion Linker (obrigatória)**
- Tipo: Conversion Linker
- Trigger: All Pages
- Função: captura gclid e armazena em first-party cookie

**Tag 2: Google Ads Conversion Tracking**
- Tipo: Google Ads Conversion Tracking
- Trigger: evento de conversão (ex: purchase)

```
Conversion ID: AW-XXXXXXXXX
Conversion Label: XXXXXXXXXXXXXXXXXXX
Conversion Value: {{DL - value}}
Currency Code: {{DL - currency}}
Transaction ID: {{DL - transaction_id}}
```

**Fonte:** Analytics Mania - Google Ads Conversion Tracking with GTM

### Enhanced Conversions

Envia dados hasheados (email, telefone, endereço) para melhorar match rate de conversões.

**Configuração:**
1. Ativar Enhanced Conversions na conta Google Ads
2. No GTM: adicionar campos de Enhanced Conversion na tag
3. Dados são hasheados automaticamente antes do envio

**Campos suportados:**
- Email (hashed SHA-256)
- Phone number
- First name + Last name
- Street address + City + Region + Postal code + Country

**Fonte:** Analytics Mania + Métricas Boss - Enhanced Conversions do Google Ads

### Evolução das Conversões Google Ads

1. Global Site Tag (gtag.js)
2. Conversion Linker + Tag via GTM
3. Enhanced Conversions (dados first-party hasheados)
4. Consent Mode integration
5. Tendência: mais dados first-party, menos dependência de cookies

**Fonte:** Métricas Boss - A Evolução das Conversões do Google Ads

---

## 3. TikTok Pixel

### Instalação via GTM

Usar Custom HTML tag com snippet do TikTok Pixel base code. Configurar eventos padrão como ViewContent, AddToCart, PlaceAnOrder.

⚠️ **ALERTA:** A extensão do TikTok para Chrome pode causar interferência com o GTM Preview Mode e disparo de tags. **Solução:** desativar a extensão durante debug.

**Fonte:** Métricas Boss - Como instalar o TikTok Pixel via GTM + Extensão TikTok causa problemas no GTM

### TikTok Events API

Similar à Meta CAPI - envio server-side de eventos para melhor match rate. Implementável via GTM Server-Side.

---

## 4. LinkedIn Insight Tag

### Instalação via GTM

Custom HTML tag com o snippet do LinkedIn Insight Tag. Permite:
- Tracking de conversões LinkedIn Ads
- Criação de Matched Audiences para remarketing
- Análise de demographics de visitantes

**Fonte:** Métricas Boss - Como instalar e configurar a LinkedIn Tag via GTM

---

## 5. Tracking de Formulários Third-Party

### TypeForm via GTM

Código único em `00_susano/referencias/analytics/tracking/snippets.md` (seção 2.1); este arquivo não repete o listener. Eventos: `form_started`, `form_submit`, com `form_id` e `form_response_id`.

### Calendly via GTM

Código único em `00_susano/referencias/analytics/tracking/snippets.md` (seção 2.2, com deduplicação); este arquivo não repete o listener.

**Eventos Calendly disponíveis:**
- `calendly.event_type_viewed` - viu tipos de evento
- `calendly.profile_page_viewed` - viu perfil
- `calendly.date_and_time_selected` - selecionou data/hora
- `calendly.event_scheduled` - agendou (conversão principal)

**Fonte:** Analytics Mania - Track Calendly with GTM

---

## 6. Video Tracking

### YouTube via GA4 Enhanced Measurement

Ativação automática: Admin → Data Streams → Enhanced Measurement → Video Engagement. Tracka play, progress (10%, 25%, 50%, 75%), complete para YouTube embeds.

### YouTube via IFrame API (Customizado)

O iframe precisa de `enablejsapi=1` na URL do embed; sem isso a API não dispara eventos. Nomes alinhados ao Enhanced Measurement do GA4 (`video_start`, `video_progress`, `video_complete`); com o Enhanced Measurement de vídeo ligado, não usar este script, para não duplicar.

```javascript
var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('youtube-container', {
    videoId: 'VIDEO_ID',
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });
}

function onPlayerStateChange(event) {
  var states = { '0': 'complete', '1': 'start' };  // pause não é evento do Enhanced Measurement
  var state = states[event.data];
  if (state) {
    window.dataLayer.push({
      'event': 'video_' + state,
      'video_provider': 'youtube',
      'video_title': event.target.getVideoData().title,
      'video_duration': event.target.getDuration()
    });
  }
}
```

**Fonte:** Analytics Mania - YouTube Tracking GTM

### HTML5 Video Player

```javascript
var videos = document.getElementsByTagName('video');
var videoProgress = {};
for (var i = 0; i < videos.length; i++) {
  (function(video, id) {
    videoProgress[id] = { 25: false, 50: false, 75: false };
    video.addEventListener('play', function() {
      window.dataLayer.push({
        'event': 'video_play',
        'video_title': this.title || 'Unknown',
        'video_duration': this.duration,
        'video_provider': 'html5'
      });
    });
    video.addEventListener('ended', function() {
      window.dataLayer.push({ 'event': 'video_complete', 'video_provider': 'html5' });
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
```

**Fonte:** Analytics Mania - Track HTML5 Video Player

---

## 7. Outbound Link Tracking

```
GTM Trigger:
  Type: Click - Just Links
  Condition: Click URL does not contain {{Page Hostname}}

GA4 Event Tag:
  Event Name: outbound_link
  Parameters:
    link_url: {{Click URL}}
    link_text: {{Click Text}}
```

**Nota:** GA4 Enhanced Measurement já tracka outbound clicks automaticamente. Usar tracking customizado apenas se precisar de parâmetros adicionais.

**Fonte:** Analytics Mania - Track Outbound Links with GTM

---

## 8. Affiliate Link Tracking

Configurar trigger de clique que detecta URLs contendo padrão de affiliate (ex: `/go/`, `/refer/`, `?ref=`). Enviar como evento GA4 com parâmetros de affiliate ID e destino.

**Fonte:** Analytics Mania - Track Affiliate Links with GTM

## NOTAS DA MIGRAÇÃO (2026-10-31)

- [VERIFICAR] Cases de 2021 e 2022; snippets repetidos com `00_susano/referencias/analytics/tracking/snippets.md` a consolidar.
