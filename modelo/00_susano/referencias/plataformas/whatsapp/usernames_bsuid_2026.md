---
id: ref-plataformas-whatsapp-usernames-bsuid-2026
tipo: referencia
origem: documento informativo de provedor de soluções WhatsApp (março de 2026), conferido na documentação da Meta em 01/11/2026
atualizado: 2026-11-01
revisao_pendente: Sarden (edição v0.3.0: cronograma conferido na documentação da Meta, formato e comportamento do BSUID, limites de envio marcados)
---

# WhatsApp Usernames & BSUID: Mudanças Estruturais 2026

**Fonte original**: documento informativo de um provedor de soluções WhatsApp (março de 2026), baseado em documentação oficial da Meta, WABetaInfo, Twilio e Sanuker
**Conferido em 01/11/2026** contra a página "Business-scoped user IDs" da Meta for Developers (developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/) e o changelog da Twilio (18/02/2026): o cronograma abaixo foi reescrito no passado com o que se confirmou.
**Classificação**: Conhecimento de plataforma, aplicável a todos os clientes que operam via WhatsApp Business

---

## 1. Contexto Geral

A Meta está implementando a maior mudança estrutural do WhatsApp desde a criptografia ponta a ponta (2016). Ao longo de 2026, em rollout gradual por região, usuários e empresas passaram a poder se comunicar via nomes de usuário (@username), sem necessidade de compartilhar número de telefone. Os BSUIDs chegaram aos webhooks em abril de 2026; a reserva de username para empresas abriu em 29/06/2026; o envio de mensagem para um BSUID é aceito pela API desde julho de 2026 (fonte: Meta for Developers, "Business-scoped user IDs", verificado em 01/11/2026).

O número de telefone continua existindo como âncora de verificação da conta. O username é uma camada adicional e opcional de identidade.

---

## 2. Usernames: O que são e como funcionam

Username é um identificador único no formato `@nomedeusuario` (mesmo padrão do Instagram/Telegram).

### Funcionalidades habilitadas por username

- Iniciar conversas sem revelar número de telefone
- Fazer e receber chamadas de voz/vídeo usando apenas o username
- Participar de grupos sem expor número pessoal
- Pesquisar empresas na barra de busca pelo @username comercial

### Diferenças por tipo de perfil

| Aspecto | Usuário Pessoal | Empresa (WhatsApp Business) |
|---|---|---|
| Username | Oculta o número pessoal; exibe apenas o @username | Ganha um @username pesquisável; número comercial ainda aparece |
| Número de telefone | Fica invisível para quem não está nos contatos salvos | Continua visível no perfil comercial |
| Descoberta | Pode ser encontrado pela busca via @username | Clientes podem buscar e iniciar conversa pelo @username |
| Privacidade extra | Pode configurar chave de username opcional | API lida com BSUID; não precisa de chave |

### Reserva de Username

- Processo vinculado a contas Meta
- Quem já tem @username no Instagram ou Facebook poderá reivindicá-lo para o WhatsApp
- Reserva e adoção de username comercial abertas em 29/06/2026, pelo Meta Business Suite, WhatsApp Manager, app WhatsApp Business ou Username API (confirmado na documentação da Meta em 01/11/2026)

---

## 3. BSUID (Business-Scoped User ID)

Novo identificador técnico que permite empresas continuarem se comunicando com clientes mesmo quando o número de telefone estiver oculto.

### Características técnicas

- Único por par empresa-usuário (mesmo cliente terá BSUIDs diferentes para empresas diferentes)
- Formato: código de país ISO 3166 alpha-2, ponto e até 128 caracteres alfanuméricos (ex.: `BR.1A2B...`); nos webhooks da Twilio, prefixado com `whatsapp:`
- Entregue via webhooks da API no campo `user_id`, presente em todos os webhooks de mensagem desde o início de abril de 2026
- Muda quando o usuário troca de número: a Meta avisa por mensagem de sistema no webhook de mensagens, com o ID novo e o anterior; o campo de webhook `user_id_update` anunciado em julho de 2026 não existe (correção da Meta em 11/08/2026)
- Sempre presente nos webhooks, mesmo que o usuário não tenha ativado username
- Não visível na interface (identificador de backend; usuário vê apenas o @username)
- Muda se a empresa migrar de WABA/BSP (novos BSUIDs gerados para todos os clientes)

### Lógica de identificação nos webhooks

| Cenário | Campo "to"/"from" | Campo BSUID |
|---|---|---|
| Usuário SEM username | Número de telefone | BSUID (campo extra) |
| Usuário COM username (número oculto) | BSUID | BSUID |
| Cliente já na Contact Book (interação prévia) | Número de telefone | BSUID (campo extra) |

### Contact Book (Agenda de Contatos)

- Lançado no início de abril de 2026 (configuração gerenciável no Business Manager desde março)
- Armazena automaticamente pares número + BSUID de interações anteriores
- Clientes que já conversaram com a empresa antes do rollout terão números preservados nos webhooks

### Período de transição

Após qualquer interação entre empresa e cliente, o WhatsApp continua retornando o número de telefone nos webhooks por 30 dias corridos, mesmo que o usuário tenha ativado o username.

---

## 4. Impactos Operacionais para Empresas

### O que muda

| Área | Impacto |
|---|---|
| Descoberta e branding | Empresa encontrável pelo @username na busca do WhatsApp (similar ao Instagram) |
| Identificação de clientes novos | Alguns chegarão sem número visível; identificação via BSUID |
| CRM e integrações | Sistemas integrados (CRM, ERP, BI) precisarão reconhecer BSUID como identificador, além do telefone |
| Limites de envio em massa | [VERIFICAR] A fonte original dizia que empresas verificadas teriam acesso direto a 100 mil conversas por dia sem escalonamento por tiers; a documentação de limites de mensagens da Meta ainda descreve a escada por tiers de conversas iniciadas pela empresa em 24 h. Confirmar na página "Messaging limits" antes de planejar campanha |
| Pacing de campanhas | Meta introduzindo envio em lotes com monitoramento de qualidade antes de liberar próximos lotes |

### O que NÃO muda

- Número de telefone continua obrigatório para criar e verificar conta WhatsApp
- Login continua por número + código SMS (NÃO é email/senha)
- Registro WABA continua igual (número de telefone para conta comercial)
- Criptografia ponta a ponta mantida para comunicação via username
- Templates de mensagem (marketing, utilidade, autenticação) sem alteração
- Mensagens de autenticação (OTP/2FA) continuam sendo enviadas exclusivamente para números de telefone
- Username é opcional para o usuário final
- Chatbots e automações continuam funcionando (desde que plataforma esteja adaptada para BSUID)

---

## 5. Cronograma de Rollout

| Período | Marco | Estado em 01/11/2026 |
|---|---|---|
| Nov 2025 a fev 2026 | Anúncio e documentação | Meta comunicou parceiros; Twilio publicou o changelog do BSUID em 18/02/2026; BSUID visível em webhooks de teste a partir de meados de fevereiro (confirmado) |
| Março a início de abril 2026 | BSUID e Contact Book | BSUIDs em todos os webhooks de mensagem (a partir de 31/03/2026, segundo provedores) e Contact Book no ar no início de abril (confirmado na documentação da Meta) |
| 29/06/2026 | Usernames para empresas | reserva e adoção abertas pelo Business Suite, WhatsApp Manager, app ou Username API (confirmado) |
| Julho 2026 | Envio para BSUID | API aceita mensagem endereçada a BSUID e CTA de pedido de número (confirmado; a documentação listava maio antes) |
| Ao longo de 2026 | Rollout para usuários | gradual por região (Estados Unidos no fim de junho, segundo provedores); [VERIFICAR] o estado por país antes de afirmar cobertura global |

Rollout gradual, não instantâneo: não houve "dia D" único. A integração que ainda não lê BSUID está atrasada, não "se preparando".

---

## 6. Implicações Estratégicas

### Para aquisição de clientes

- Username comercial pesquisável cria novo canal de descoberta orgânica dentro do WhatsApp
- Reduz fricção do primeiro contato (não precisa ter número salvo)
- Alinhamento com comportamento já consolidado no Instagram (@username para buscar marcas)

### Para CRM e dados

- Empresas que dependem exclusivamente de número de telefone como chave primária de contato precisam adaptar schema para suportar BSUID
- Migração de WABA/BSP gera novos BSUIDs para toda a base, exigindo re-mapeamento
- Contact Book mitiga risco de perda de histórico para clientes com interações anteriores

### Para privacidade e compliance

- Tendência de desacoplamento entre identidade e número de telefone
- Clientes novos podem interagir com a empresa sem nunca revelar número pessoal
- Impacto potencial em processos que dependem de telefone para validação de identidade (KYC, onboarding) [INFERÊNCIA]

### Para envio em massa e campanhas

- [VERIFICAR] Se a simplificação dos limites diários se confirmar na documentação de messaging limits, a barreira operacional de escalada por tiers cai; até lá, planejar pela escada vigente
- Pacing de campanhas pode afetar timing de campanhas que dependem de entrega simultânea [INFERÊNCIA]

---

## 7. Lacunas e Pontos em Aberto

- [LACUNA] Regras exatas de reserva de username para empresas que NÃO possuem conta Instagram/Facebook vinculada
- [LACUNA] Comportamento do BSUID em cenários de transferência de conversa entre departamentos/WABAs dentro da mesma empresa
- [LACUNA] Impacto nos relatórios de métricas do WhatsApp Business (se dashboards da Meta serão adaptados para exibir dados por BSUID)
- [LACUNA] Detalhes técnicos sobre a "chave de username" que usuários pessoais podem configurar
- [LACUNA] Política de conflito de usernames entre empresas de mesmo nome em diferentes países
- [LACUNA] Como o BSUID interage com a API de mensagens de autenticação (se OTP continua usando telefone mesmo quando único identificador disponível é BSUID)

---

## 8. Fonte e Confiabilidade

Construído a partir de documento informativo de um provedor de soluções WhatsApp (março de 2026) e conferido em 01/11/2026 contra a documentação da Meta for Developers ("Business-scoped user IDs") e o changelog da Twilio. O que está marcado "confirmado" tem essa conferência; o que está [VERIFICAR] não foi confirmado em fonte oficial nesta data. Seções com [INFERÊNCIA] são conclusões lógicas, não declaradas pela fonte.

## NOTAS DA MIGRAÇÃO (2026-10-31)

- Cronograma reescrito na v0.3.0 com o que se confirmou até 01/11/2026; o limite de 100 mil conversas por dia para empresas verificadas continua [VERIFICAR].
