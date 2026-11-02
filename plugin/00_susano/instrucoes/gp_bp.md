---
id: instr-gp-bp
tipo: instrucao
autor: Sarden
carrega_em: sob demanda (skill susano-rituais)
origem: guia de GP/BP da operação do Sarden (2025 a 2026)
atualizado: 2026-11-01
revisao_pendente: Sarden (edição v0.3.0: carga sob demanda, vocabulário de frente, marcadores canônicos, contexto nos arquivos da frente)
---

# GP/BP: Como o Susano Trabalha com Planejamento de Growth

> Frente: cliente, conta ou produto; o que você chamaria de projeto. Quem pede: quem está na sessão (o dono deste repositório ou o líder da frente).

---

## PROPÓSITO

Este documento instrui o Susano sobre como agir sempre que alguém pedir qualquer trabalho relacionado a GP (Growth Plan) ou BP (Business Plan).

O Susano opera em **4 modos** dependendo do que for pedido. O modo é detectado automaticamente pelo pedido, quem pede não precisa especificar qual é.

---

## DETECÇÃO DE MODO

| Se quem pede disser... | Modo ativado |
|---------------------|--------------|
| "Analisa o meu GP", "O que está errado aqui?", "Revisão do plano" | **MODO 1, ANÁLISE** |
| "Cria um GP", "Monta o plano", "Preciso de um GP do zero" | **MODO 2, CRIAÇÃO** |
| "Atualiza o GP", "Ajusta o plano", "Revisa com os dados novos" | **MODO 3, REVISÃO** |
| "Transforma em apresentação", "Quero levar para os sócios", "Preciso de um doc para investidor" | **MODO 4, APRESENTAÇÃO** |

Se o pedido for ambíguo, o Susano pergunta uma coisa: "Você quer que eu analise o que existe ou crie um novo?"

---

## REGRAS UNIVERSAIS (valem em todos os modos)

**Dados:**
- Nunca invente projeção, taxa, número ou métrica sem base fornecida por quem pede ou registrada no repositório
- Se um dado está ausente e é crítico, declara `[DADO PENDENTE]` e diz o que falta para continuar
- Se está inferindo a partir de padrões ou benchmarks, marca: `[INFERÊNCIA]` com fonte e data, e pede validação
- Dados de execução (CAC real, conversão real, receita realizada) têm precedência absoluta sobre projeções do plano
- Meta e target só do registro da frente (`contexto.md`, `decisoes.md`); referência de mercado entra como [INFERÊNCIA], nunca como meta

**Tom e formato:**
- Direto. Sem suavizar problemas, se o plano tem um furo, nomeia o furo
- Português sempre
- Output completo: nunca truncado, nunca com "[preencha aqui]"

**Quando a planilha estiver presente:**
- Lê todas as abas antes de escrever qualquer coisa
- Registra o que está vazio, com erro ou inconsistente
- Nunca interpola valores ausentes: declara `[LACUNA]`

---

## MODO 1: ANÁLISE

**Ativado quando:** quem pede quer entender o que está certo, errado ou em risco no GP/BP atual.

**O que o Susano faz:**

```
FASE 1, LEITURA
Lê o GP/BP completo (planilha, doc ou dados colados).
Mapeia: estrutura, período, métricas-chave, canais, orçamento, time, KPIs.

FASE 2, DIAGNÓSTICO
Avalia 5 dimensões:
1. COERÊNCIA INTERNA: os números fecham entre si? Há inconsistências matemáticas?
2. ADERÊNCIA À REALIDADE: as projeções são defensáveis dado o histórico disponível?
3. FUNIL: onde está o gargalo? A taxa de conversão mais fraca do funil?
4. ORÇAMENTO: a alocação reflete as apostas certas? CAC está viável?
5. TIME: o time projetado suporta a execução? Há gaps?

FASE 3, SÍNTESE
Identifica:
- O que está sólido (não precisa mudar)
- O que está frágil (precisa atenção antes de escalar)
- O que está errado (precisa corrigir antes de executar)
- O risco principal (o que pode matar o plano se não for endereçado)
```

**Output do Modo 1:**

```markdown
## ANÁLISE DO GP: [nome/período]

### O que está sólido
[lista direta, sem exagero]

### O que está frágil
[lista com explicação do risco de cada item]

### O que está errado
[lista com explicação do problema e impacto]

### Risco principal
[um parágrafo, o que pode matar o plano e por quê]

### Próximo passo recomendado
[uma ação concreta que quem pede deve tomar agora]
```

---

## MODO 2: CRIAÇÃO

**Ativado quando:** quem pede quer um GP/BP novo do zero.

**O que o Susano faz antes de escrever:**

Se quem pede não forneceu os dados abaixo, pergunta de uma vez (não em múltiplas rodadas):

```
Para criar o GP preciso de:
1. Período coberto (ex: jan a dez de 2026, Q2 2026)
2. Objetivo principal: o número que define sucesso (ex: R$X de MRR, X clientes, X de receita)
3. Canais disponíveis e seus orçamentos estimados
4. Ticket médio e modelo de precificação
5. Time atual e capacidade de contratação
6. Baseline: onde estamos hoje (clientes, receita, CAC, conversão)
7. Restrições: o que não pode mudar (budget máximo, número máximo de contratações, etc.)
```

Se quem pede fornecer uma planilha ou dados parciais, extrai o que conseguir e pergunta apenas o que falta.

**Estrutura do GP criado pelo Susano:**

```markdown
# GROWTH PLAN: [Frente] | [Período]
> Criado por: Susano | Data: [data] | Versão: 1.0

## 1. OBJETIVO E MÉTRICA-NORTE
[O número principal. Período. Como será medido.]

## 2. CONTEXTO E BASELINE
[Onde estamos hoje. Dados reais disponíveis.]

## 3. ESTRATÉGIA
[A lógica do plano em 3 a 5 frases. Por que essa abordagem vai funcionar.]

## 4. CANAIS E FUNIL
[Para cada canal:]
- Canal: [nome]
- Meta de leads/mês: [número]
- Taxa de conversão projetada Lead→Cliente: [%]
- Meta de clientes/mês: [número]
- Investimento mensal: [R$]
- CAC projetado: [R$]

## 5. PROJEÇÕES MENSAIS
[Tabela com período, leads, MQLs, SQLs, clientes, receita, investimento, CAC]
[Cada linha identificada como projeção ou como real]

## 6. ORÇAMENTO
[Total por categoria e por mês]
- Mídia paga: R$
- Time: R$
- Software/ferramentas: R$
- Total: R$

## 7. TIME E CAPACIDADE
[Quem está no time. Quando contratar quem. Custo mensal.]

## 8. INICIATIVAS PRIORITÁRIAS
[As 3 a 5 apostas principais do plano. Para cada uma:]
- Nome da iniciativa
- Objetivo e métrica de sucesso
- Responsável
- Prazo
- Orçamento alocado

## 9. PRESSUPOSTOS CRÍTICOS
[O que precisa ser verdade para o plano funcionar.
Se qualquer um desses cair, o plano precisa ser revisado.]

## 10. RISCOS E PLANO B
[Top 3 riscos. Para cada um: probabilidade, impacto, mitigação.]

## 11. MARCOS E REVISÕES
[Quando revisar o plano. Quais métricas disparam revisão imediata.]
```

---

## MODO 3: REVISÃO

**Ativado quando:** quem pede tem um GP existente e quer atualizá-lo com dados novos ou ajustá-lo.

**O que o Susano faz:**

```
FASE 1, COMPARAÇÃO
Lê o GP atual e os dados novos fornecidos por quem pede.
Identifica: o que mudou, o que ficou como planejado, o que ficou abaixo ou acima.

FASE 2, DIAGNÓSTICO DO DESVIO
Para cada desvio relevante:
- Qual é o desvio (planejado vs. realizado)?
- Qual é a causa provável?
- O desvio é pontual (recuperável) ou estrutural (exige replaneamento)?

FASE 3, REPLAN
Atualiza as projeções com base nos dados reais.
Aponta o que precisa mudar no plano (metas, orçamento, canais, time).
```

**Output do Modo 3:**

```markdown
## REVISÃO DO GP: [nome/período]
> Data da revisão: [data] | Período analisado: [período]

### Desempenho vs. Plano
| Métrica | Planejado | Realizado | Desvio | Tipo |
|---------|-----------|-----------|--------|------|
| [métrica] | [valor] | [valor] | [%] | [Pontual/Estrutural] |

### Causas dos principais desvios
[Para cada desvio relevante, causa e implicação]

### O que muda no plano
[Lista objetiva de ajustes necessários, metas, orçamento, canais, time]

### Projeções atualizadas
[Tabela revisada com os novos números]

### Próximo passo
[Uma ação concreta]
```

---

## MODO 4: APRESENTAÇÃO

**Ativado quando:** quem pede quer transformar o GP/BP em documento estratégico para sócios ou investidores.

**O que o Susano faz:**

Transforma o GP/BP técnico em documento executivo, linguagem de negócio, não de growth hacker. Remove jargão de funil. Mantém os números, mas contextualiza o que significam para quem não vive no dia a dia da operação.

**Estrutura do documento de apresentação:**

```markdown
# [Frente]: Plano de Crescimento [Período]
> Versão executiva | Data: [data]

## RESUMO EXECUTIVO
[3 a 5 frases. O que o negócio faz, onde está hoje, onde quer chegar e como.]

## OPORTUNIDADE
[O tamanho do mercado. Por que agora. Por que essa empresa tem vantagem.]

## ONDE ESTAMOS HOJE
[Números reais. Sem projeção. CAC, receita, clientes, canais.]

## ONDE QUEREMOS CHEGAR
[A meta principal. Período. O que muda quando chegar lá.]

## COMO VAMOS CHEGAR LÁ
[A estratégia em linguagem executiva. Canais, alavancas, sequência.]

## INVESTIMENTO NECESSÁRIO
[Total por período. Retorno esperado. Payback.]

## TIME E EXECUÇÃO
[Quem executa. Quando. Marcos principais.]

## RISCOS CONHECIDOS
[Honesto. 3 riscos reais com mitigação.]

## PRÓXIMOS PASSOS
[O que acontece nos próximos 30/60/90 dias.]
```

---

## COMPORTAMENTO POR TIPO DE INPUT

**Se quem pede colar dados brutos (tabela, números, texto):**
→ Extrai os dados, estrutura internamente, executa o modo correto

**Se quem pede fizer upload de planilha .xlsx:**
→ Lê todas as abas, mapeia a estrutura, identifica a versão ativa do plano, executa o modo correto

**Se quem pede der um briefing verbal ("preciso de um GP para o canal X com budget Y"):**
→ Identifica o que falta, faz as perguntas necessárias de uma vez, executa após receber as respostas

**Se o pedido misturar modos ("analisa e já me dá o plano revisado"):**
→ Executa Modo 1 primeiro, depois Modo 3 com base no diagnóstico, entrega os dois na mesma resposta

---

## CONTEXTO POR FRENTE (aplicar em todos os modos)

Cada frente tem sua pasta em `20_<frente>/<slug>/`. Antes de trabalhar em qualquer GP/BP, o Susano:

1. **Identifica a frente**: "Esse GP é de qual frente?" (`/frente <slug>`)
2. **Consulta o registro**: lê `contexto.md` (quem é, funil, canais, ticket), `estado.md` (o que está quente), `decisoes.md` (metas e decisões vigentes) e `experimentos.md` (o que está em teste)
3. **Aplica os dados da frente**: canais, ticket, funil, ferramentas, métricas, benchmarks

O Susano NUNCA mistura dados de frentes diferentes em um mesmo GP/BP. Cada frente tem seus próprios canais, taxas, ticket, funil e benchmarks.

Se a frente não tem pasta no repositório, o Susano aponta `/nova-frente` (ou o onboarding, em `00_susano/instrucoes/onboarding_frente.md`) e pede os dados mínimos antes de prosseguir:
- Canais ativos e orçamento estimado por canal
- Ticket médio e modelo de precificação
- Funil (estágios e taxas de conversão disponíveis)
- Ferramentas em uso (CRM, mídia, automação)
- Métricas-chave e benchmarks atuais (CAC, CPL, conversão)
