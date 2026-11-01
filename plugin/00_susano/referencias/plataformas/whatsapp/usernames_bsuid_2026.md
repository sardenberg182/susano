---
id: ref-plataformas-whatsapp-usernames-bsuid-2026
tipo: referencia
origem: whatsapp_usernames_bsuid_2026.md
atualizado: 2026-10-31
---

# WhatsApp Usernames & BSUID: Mudanças Estruturais 2026

**Fonte**: Documento informativo ChatX/Devsky Tecnologia, Março 2026
**Baseado em**: Documentação oficial Meta, WhatsApp Business API, WABetaInfo, Twilio, Sanuker
**Última atualização**: Março 2026
**Classificação**: Conhecimento de plataforma, aplicável a todos os clientes que operam via WhatsApp Business

---

## 1. Contexto Geral

A Meta está implementando a maior mudança estrutural do WhatsApp desde a criptografia ponta a ponta (2016). A partir de junho de 2026, usuários e empresas poderão se comunicar via nomes de usuário (@username), sem necessidade de compartilhar número de telefone.

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
- Reserva pode iniciar antes do rollout completo, ainda no 1º semestre de 2026

---

## 3. BSUID (Business-Scoped User ID)

Novo identificador técnico que permite empresas continuarem se comunicando com clientes mesmo quando o número de telefone estiver oculto.

### Características técnicas

- Único por par empresa-usuário (mesmo cliente terá BSUIDs diferentes para empresas diferentes)
- Até 128 caracteres alfanuméricos
- Entregue via webhooks da API no campo `user_id`
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

- Lançamento previsto para abril de 2026
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
| Limites de envio em massa | Meta simplificando: empresas verificadas terão acesso direto a 100k mensagens/dia, sem escalonamento gradual por tiers (2K > 10K > 100K) |
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

| Período | Marco | Detalhes |
|---|---|---|
| Nov 2025 | Anúncio oficial | Meta comunica parceiros e publica documentação para desenvolvedores |
| 1º sem. 2026 | Reserva de usernames | Possibilidade de reservar @usernames vinculados a contas Meta (Instagram/Facebook) |
| Abril 2026 | Contact Book | Lançamento da agenda de contatos automática com pares número + BSUID |
| Junho 2026 | Rollout inicial | Usernames em países de teste; deadline para empresas terem APIs adaptadas |
| Agosto 2026 | Rollout global | Expansão para todos os países; usernames disponíveis para todos os usuários |

Rollout é gradual, não instantâneo. Não haverá "dia D" único.

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

- Simplificação dos limites diários (100k direto para verificadas) reduz barreira operacional
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

Este arquivo foi construído a partir de documento informativo da ChatX/Devsky Tecnologia (março 2026), que por sua vez cita documentação oficial da Meta, WhatsApp Business API, WABetaInfo, Twilio e Sanuker.

Nível de confiabilidade: **Alto para o que está documentado**. Cronograma sujeito a alterações pela Meta. Seções marcadas com [INFERÊNCIA] representam conclusões lógicas não confirmadas pela fonte original.

## NOTAS DA MIGRAÇÃO (2026-10-31)

- [VERIFICAR] O cronograma (junho e agosto de 2026) é anterior a esta migração: confirmar o estado atual na documentação oficial da Meta antes de usar.
- [VERIFICAR] Limite de 100 mil mensagens por dia para empresas verificadas.
