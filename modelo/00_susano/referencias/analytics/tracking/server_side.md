---
id: ref-analytics-tracking-server-side
tipo: referencia
origem: KB_ServerSide_Tracking.md
atualizado: 2026-10-31
---

# Knowledge Base: Server-Side Tracking

> Fontes: Analytics Mania + Métricas Boss | Compilado: Abril 2026

---

## 1. GTM Server-Side - Conceitos

### Arquitetura

O GTM Server-Side (sGTM) processa tags em um servidor próprio em vez do browser do usuário.

**Fluxo:**
```
Browser → GTM Client-Side → sGTM Server → Endpoints (GA4, Meta, Google Ads, etc.)
```

**Componentes:**
- **Client (Receptor):** recebe requests do browser
- **Tags Server-Side:** processam e reenviam dados para endpoints
- **Container Server:** hospedado em Google Cloud, Stape.io, Addingwell, etc.

### Benefícios

1. **First-party data collection:** cookies do próprio domínio, não de terceiros
2. **Resistência a ad blockers:** requests vão para seu domínio, não para google-analytics.com
3. **Melhor performance do site:** menos JavaScript no browser
4. **Controle total sobre dados:** enriquecer, anonimizar, filtrar antes de enviar a terceiros
5. **SHA-256 hashing server-side:** processamento criptográfico seguro (não expõe lógica no frontend)
6. **Melhor match rate:** para Enhanced Conversions e Meta CAPI
7. **Compliance facilitado:** um ponto central para aplicar regras de privacidade

**Fonte:** Analytics Mania - Benefits of Server-Side Tagging | Métricas Boss - Server-Side Tracking Guia Completo

---

## 2. Setup e Infraestrutura

### Google Cloud Run (Recomendado)

**Vantagens sobre App Engine:**
- **Scale-to-zero:** custo $0 sem tráfego (vs ~$120/mês fixo do App Engine)
- Arquitetura separada: Produção e Preview isolados
- Rollback de um clique via revisões
- Melhor performance em picos de tráfego
- Infraestrutura multi-regional simplificada

**Setup via Cloud Shell:**
```bash
# 1. Acessar Cloud Shell
https://ssh.cloud.google.com/cloudshell

# 2. Configurar projeto
gcloud config set project SEU_PROJECT_ID

# 3. Executar script de setup
bash -c "$(curl -fsSL https://googletagmanager.com/static/serverjs/setup.sh)"

# 4. Seguir instruções, aceitar padrões (Enter) e confirmar com 'y'
```

**Fonte:** Métricas Boss - GTM Server-Side: App Engine para Cloud Run

### Migração App Engine → Cloud Run

**Procedimento em 4 fases:**

1. **Provisionamento Paralelo:** Provisionar novos serviços no Cloud Run usando a mesma Container Config string
2. **Teste:** Mapear subdomínio temporário (ex: `teste-sgtm.seudominio.com`) ao Cloud Run; validar coleta
3. **Cutover:** Atualizar DNS do subdomínio principal para Cloud Run
4. **Desativação:** Após monitorar estabilidade, desativar App Engine

**Fonte:** Métricas Boss - Migração App Engine para Cloud Run

### Stape.io (Hosting Gerenciado)

Stape.io oferece hosting gerenciado para sGTM, eliminando necessidade de gerenciar infraestrutura GCP diretamente.

**Vantagens:**
- Setup simplificado (sem conhecimento de GCP necessário)
- Dashboard de monitoramento
- Suporte técnico incluído
- A partir de ~$20/mês

**Fonte:** Métricas Boss - Como configurar o Server-Side do GTM usando o Stape

### Comparativo de Custos

| Plataforma | Custo Mensal | Escalabilidade | Complexidade |
|-----------|-------------|----------------|--------------|
| App Engine (legado) | ~$120/mês fixo | Moderada | Média |
| Cloud Run | Pay-per-use ($0 mín.) | Excelente | Média-Alta |
| Stape.io | A partir de ~$20/mês | Boa | Baixa |
| Addingwell | Variável | Boa | Baixa |

---

## 3. SHA-256 Hashing

### Client-Side vs Server-Side

| Aspecto | Client-Side (cGTM) | Server-Side (sGTM) |
|---------|--------------------|--------------------|
| Execução | Browser do usuário | Servidor controlado |
| Segurança | Código exposto, manipulável | Protegido contra inspeção |
| Ad blockers | Suscetível | Resistente |
| Controle de dados | Limitado | Total - permite anonimização |
| Performance | Impacta dispositivo do usuário | Zero impacto no frontend |

### Por que NÃO implementar SHA-256 no Client-Side GTM

1. **Web Crypto API é assíncrona** → incompatível com variáveis JS síncronas do GTM
2. **CryptoJS está descontinuada** → risco de segurança
3. **Código visível no browser** → qualquer um pode inspecionar e modificar
4. **Impacto em Core Web Vitals** → LCP e TBT degradados
5. **Performance variável** em dispositivos mais lentos

**Recomendação:** Sempre delegar SHA-256 para server-side (sGTM ou backend).

**Fonte:** Métricas Boss - Implementar SHA-256 no GTM: Vale a Pena?

---

## 4. Conversions API (Meta CAPI) via Server-Side

### Implementação via sGTM

O sGTM pode enviar eventos diretamente para Meta CAPI, eliminando a necessidade de implementação backend customizada.

**Fluxo:**
```
Browser → GTM Client → sGTM → Meta CAPI endpoint
                             → GA4
                             → Google Ads
```

### Event Match Quality Score

Indica a qualidade dos parâmetros enviados via CAPI. Quanto mais parâmetros de matching (email, phone, IP, user agent, fbclid), maior o score e melhor a atribuição.

**Parâmetros que melhoram o score:**
- Email (hasheado)
- Phone (hasheado)
- First name + Last name (hasheados)
- City + State + Zip + Country
- External ID
- Client IP address
- Client User Agent
- fbclid (Facebook Click ID)
- fbc cookie
- fbp cookie

### Deduplicação

Essencial quando usa Pixel (client-side) + CAPI (server-side) simultaneamente:
- Usar `event_id` único compartilhado entre ambos
- Meta descarta automaticamente o evento duplicado
- Sem deduplicação: conversões contadas 2x

---

## 5. Google Tag Gateway

### Conceito

Roteamento de requests de analytics através do Cloudflare CDN para first-party data collection.

**Arquitetura:**
```
Website → Cloudflare Workers → Google Analytics
```

Substitui requests diretos para domínios do Google, usando domínio próprio.

### Vantagens

- First-party cookie domain
- Resistência a bloqueadores
- Sem necessidade de infraestrutura server-side completa (mais leve que sGTM)

### Limitações

- Requer domínio customizado + Cloudflare
- Manutenção de Workers
- Menos flexível que sGTM completo

### Quando usar

- **Google Tag Gateway:** quando quer first-party tracking com setup mínimo
- **sGTM completo:** quando precisa de controle total sobre dados, CAPI, enrichment, etc.

**Fonte:** Analytics Mania - Google Tag Gateway

---

## 6. Trade-offs e Decisão

### Quando implementar Server-Side

✅ **Implementar quando:**
- Investimento significativo em paid media (Meta, Google Ads, TikTok)
- Necessidade de compliance com LGPD/GDPR
- Ad blockers impactando dados significativamente
- Precisa de Enhanced Conversions ou CAPI
- Multiple platforms tracking (GA4 + Meta + Google Ads + TikTok)

❌ **Pode adiar quando:**
- Budget limitado e baixo investimento em ads
- Site simples com tracking básico
- Equipe sem capacidade técnica para manutenção

### Impacto Real nos Dados

- Melhoria de **10-30%** na captura de conversões (vs client-side only)
- Resistência a **~30%** de ad blockers que bloqueiam tracking client-side
- Cases reais mostram **+10-24% em vendas atribuídas** (Ray-Ban, Malásia Bottoms Lab)
- Melhor Event Match Quality Score no Meta → melhor otimização de campanhas

## NOTAS DA MIGRAÇÃO (2026-10-31)

- [VERIFICAR] Preços de hosting datados.
