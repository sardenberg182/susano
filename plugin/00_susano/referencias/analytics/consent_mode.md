---
id: ref-analytics-consent-mode
tipo: referencia
origem: base de conhecimento de consent mode e privacidade compilada pelo Sarden (Analytics Mania e Métricas Boss, abril de 2026)
atualizado: 2026-11-01
revisao_pendente: Sarden (edição v0.3.0: stub do gtag, trigger de Consent Initialization, chaves de dataLayer corrigidas, UET só ad_storage, Chrome mantém cookies de terceiros, perdas sem fonte viraram [LACUNA])
---

# Knowledge Base: Consent Mode e Privacidade

> Fontes: Analytics Mania + Métricas Boss | Compilado: Abril 2026 | Fatos conferidos na documentação oficial em 01/11/2026 onde indicado

> Convenção deste arquivo desde a v0.3.0: `atualizado` no frontmatter é a data da última edição, não de verificação. Fato de produto vale pela data de verificação escrita ao lado dele ("verificado em DD/MM/AAAA"); sem essa data, é [VERIFICAR] antes de usar.

---

## 1. Google Consent Mode v2

### Contexto

Obrigatório para anúncios no EEA (European Economic Area) desde março 2024. Permite que tags do Google ajustem comportamento baseado no consentimento do usuário.

### 4 Sinais de Consentimento

| Sinal | Controla | Impacto |
|-------|----------|---------|
| `ad_storage` | Cookies de publicidade | Remarketing, conversões Google Ads |
| `analytics_storage` | Cookies de analytics | GA4 data collection |
| `ad_user_data` | Dados do usuário para ads | Enhanced Conversions, Customer Match |
| `ad_personalization` | Personalização de anúncios | Remarketing audiences |

### Implementação via GTM

**Passo 1: Default State (ANTES de qualquer tag)**

O comando `gtag('consent', ...)` precisa do stub do gtag antes de qualquer tag; sem ele, `gtag` não existe e o default nunca é registrado. No GTM, esse bloco vai numa tag Custom HTML (ou no template da CMP) disparada pelo trigger **Consent Initialization - All Pages**, o único que roda antes de todas as outras tags (fonte: Google Tag Manager Help, "Consent configuration", e Google tag developer docs, "Manage consent settings", verificado em 01/11/2026).

```javascript
window.dataLayer = window.dataLayer || [];
function gtag(){ dataLayer.push(arguments); }

gtag('consent', 'default', {
  'ad_storage': 'denied',
  'analytics_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'wait_for_update': 500  // ms para aguardar CMP
});
```

**Passo 2: Update após consentimento do usuário**

```javascript
// Quando o usuário aceita cookies:
gtag('consent', 'update', {
  'ad_storage': 'granted',
  'analytics_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted'
});
```

**Passo 3: Configuração no GTM**

No GTM, configurar Built-in Consent em cada tag:
- GA4 Config Tag: requer `analytics_storage`
- Google Ads Conversion: requer `ad_storage` + `ad_user_data`
- Google Ads Remarketing: requer `ad_storage` + `ad_personalization`

**Fonte:** Analytics Mania - Consent Mode + Benefits of GA4 | Métricas Boss - Consent Mode v2

### Implementação via dataLayer

Não existe chave própria de consentimento no dataLayer: as tags do Google leem o estado de consentimento só pelos comandos `gtag('consent', 'default' | 'update', {...})`, que empurram um objeto `arguments` no dataLayer. Chaves inventadas (`consent_analytics`, `consent_ads`) não são lidas por nenhuma tag. O que vale como alternativa ao gtag direto é o template de CMP da galeria do GTM (Cookiebot, Usercentrics, OneTrust, Didomi etc.), que chama a API de consentimento do GTM por baixo; ou, num template custom, a API `setDefaultConsentState` e `updateConsentState` dos templates (fonte: Google Tag Manager developer docs, "Consent APIs", verificado em 01/11/2026).

```javascript
// Alternativa correta sem CMP: o mesmo comando, chamado quando o usuário decide
window.dataLayer = window.dataLayer || [];
function gtag(){ dataLayer.push(arguments); }
gtag('consent', 'update', {
  'ad_storage': 'granted',
  'analytics_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted'
});
// Opcional: um evento para disparar tags que esperam o consentimento
window.dataLayer.push({ 'event': 'consent_updated' });
```

---

## 2. Erro Comum: "Tag Read Consent State Before Default"

### Problema

Erro `A tag read consent state before a default was set` aparece quando uma tag tenta ler o estado de consentimento antes do `gtag('consent', 'default', ...)` ser executado.

### Causa

Ordem de disparo incorreta: tag GA4/Ads dispara ANTES do consent default ser configurado.

### Solução

1. Garantir que o consent default dispare com **prioridade máxima** (tag priority ou trigger sequencing)
2. Usar `wait_for_update: 500` para dar tempo ao CMP
3. No GTM: criar tag de Consent Initialization que dispara antes de todas as outras

**Fonte:** Analytics Mania - A Tag Read Consent State Before Default

---

## 3. Microsoft Consent Mode

### Conceito

Similar ao Google Consent Mode, mas para Microsoft Advertising (Bing Ads). Requer implementação separada no GTM.

**Sinais Microsoft:**
- `ad_storage` é o único sinal que a tag UET lê (granted ou denied); o parâmetro `asc` em cada evento UET mostra o estado enviado. Consentimento obrigatório para tráfego do EEA, Reino Unido e Suíça desde 05/05/2025 (fonte: Microsoft Advertising Help, "UET Consent Mode", via documentação de CMPs; verificado em 01/11/2026).
- `analytics_storage` não é lido pelo UET; é o Microsoft Clarity que usa `ad_Storage` e `analytics_Storage` na sua Consent API v2 [VERIFICAR a grafia e a data de enforcement do Clarity na documentação oficial].

### Implementação

Tag separada no GTM para Microsoft UET tag com consent settings.

**Fonte:** Analytics Mania - Microsoft Consent Mode

---

## 4. Cookies e GTM

### Manipulação de Cookies via GTM

Custom HTML tags podem ler e escrever cookies para persistência de dados entre sessões.

```javascript
// Ler cookie
function getCookie(name) {
  var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? match[2] : null;
}

// Escrever cookie
function setCookie(name, value, days) {
  var expires = "";
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + value + expires + "; path=/; SameSite=Lax";
}
```

### First-Party vs Third-Party Cookies

| Aspecto | First-Party | Third-Party |
|---------|-------------|-------------|
| Domínio | Mesmo do site | Domínio externo |
| Browsers | Aceitos | Bloqueados por padrão em Safari, Firefox e Brave; no Chrome continuam permitidos por padrão (Google manteve os cookies de terceiros e desistiu do prompt em 22/04/2025; bloqueio só no modo anônimo), fonte: Privacy Sandbox blog, "Next steps for Privacy Sandbox and tracking protections in Chrome", 22/04/2025, verificado em 01/11/2026 |
| Server-Side | Fortalece | N/A |
| Duração | Até 400 dias (server-set) | 7 dias (Safari ITP) |
| Uso | Analytics, preferências | Remarketing cross-site |

**Fonte:** Analytics Mania - Cookies with GTM

---

## 5. LGPD (Brasil)

### Impacto no Tracking

A LGPD (Lei Geral de Proteção de Dados) exige:
- **Base legal** para tratamento de dados pessoais (incluindo cookies de analytics)
- **Consentimento explícito** antes de coletar dados
- **Transparência** sobre quais dados são coletados e para quê
- **Direito de acesso e exclusão** de dados pelo titular

### Implementação Prática

1. **Cookie banner** com opção clara de aceitar/recusar
2. **Consent Mode** configurado como `denied` por padrão
3. **Update para `granted`** apenas após consentimento explícito
4. **Documentação** de quais tags/pixels são usados e porquê
5. **Política de privacidade** detalhando ferramentas de tracking

### Impacto na Coleta de Dados

Com consent mode em `denied`:
- GA4 coleta dados anonimizados (sem cookies)
- Google modela conversões usando Behavioral Modeling
- Perda de dados sem consentimento: depende da taxa de aceite do banner e da cobertura da modelagem; [LACUNA] a faixa de 20% a 40% citada nas fontes não tem base publicada; medir na própria frente (sessões com consentimento ÷ sessões totais) antes de citar número
- Server-side tracking ajuda a mitigar parte da perda

**Fonte:** Métricas Boss - LGPD no GA4 + Como a LGPD afeta o rastreamento web

---

## 6. GDPR (Europa)

### Requisitos para Tracking

- Consentimento antes de qualquer cookie de tracking
- Google Consent Mode v2 obrigatório para ads no EEA
- Opção de recusar deve ser tão fácil quanto aceitar
- Retenção de dados limitada e documentada

---

## 7. Impacto na Mensuração

### Behavioral Modeling (Google)

Quando `analytics_storage` está em `denied`, GA4 usa machine learning para modelar:
- Conversões estimadas
- Sessões estimadas
- Dados demográficos inferidos

### Estratégias para Minimizar Perda

1. **Consent Mode v2** - permite modelagem de dados pelo Google
2. **Server-side tracking** - first-party cookies com maior duração
3. **Enhanced Conversions** - dados hasheados para melhor match
4. **Meta CAPI** - tracking server-to-server
5. **Cookie banner UX** - design que maximiza aceite sem ser invasivo

### Métricas de Impacto

| Cenário | Efeito esperado (direção, não número) |
|---------|------------------------|
| Sem consent mode, sem server-side | maior perda: nada é coletado de quem recusa e não há modelagem |
| Com consent mode, sem server-side | pings sem cookie permitem modelagem de conversões e comportamento no GA4 e no Google Ads (modo avançado) |
| Com consent mode + server-side | cookies first-party de maior duração e menos bloqueio; ganho de cobertura dos consentidos, não dos que recusaram |
| Com consent mode + server-side + CAPI | melhor correspondência de eventos no Meta (Event Match Quality) e deduplicação com o pixel |

[LACUNA] As faixas percentuais de perda que circulavam nesta tabela (30% a 50%, 15% a 25%, 5% a 15%, 3% a 10%) não têm fonte publicada; saíram na v0.3.0. O número certo é o da frente: sessões ou conversões com consentimento contra o total, antes e depois de cada camada.
