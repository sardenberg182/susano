---
id: instr-onboarding-frente
tipo: instrucao
autor: Sarden
carrega_em: sob demanda (skill susano-rituais; a skill /nova-frente chama esta instrução)
origem: instrução de onboarding de projeto da operação do Sarden (2025 a 2026)
atualizado: 2026-11-01
revisao_pendente: Sarden (edição v0.3.0: renomeado de onboarding_projeto, vocabulário de frente, entrega nos quatro arquivos da frente)
---

# Onboarding de Frente: Como o Susano Cria o Contexto de uma Frente Nova

> Frente: cliente, conta ou produto; o que você chamaria de projeto. Quem pede: quem está na sessão (o dono deste repositório ou o líder da frente).

---

## PROPÓSITO

Quando uma frente nova chega (briefing, planilha, dados colados ou template parcialmente preenchido), o Susano transforma esse material nos arquivos da frente: `contexto.md` completo e estruturado, `estado.md` com o que está quente, `decisoes.md` com o que já foi decidido e `experimentos.md` pronto para o primeiro teste.

O objetivo é: quem pede preenche o mínimo necessário, o Susano faz o trabalho pesado de estruturar, perguntar o que falta e completar.

---

## DETECÇÃO DE ONBOARDING

O Susano detecta que está em modo de onboarding quando:
- quem pede diz "frente nova", "cliente novo", "onboarding", "cria o contexto de X" ou chama `/nova-frente`
- quem pede cola um briefing, planilha ou dados de uma frente que ainda não tem pasta em `20_<frente>/`
- quem pede faz upload de um template de contexto parcialmente preenchido
- não existe `20_<frente>/<slug>/contexto.md` e quem pede começa a falar da frente

Com shell, a pasta nasce por `python3 scripts/brain.py novo <slug> --dono <handle>` (é o que `/nova-frente` faz); nunca criada à mão. Sem shell, o Susano entrega o conteúdo dos quatro arquivos na resposta para quem pede colar (veja "Modo sem shell" em `AGENTS.md`).

---

## WORKFLOW DE ONBOARDING

### FASE 1: EXTRAÇÃO

Lê tudo que quem pede forneceu (briefing, planilha, texto colado, template preenchido).
Extrai e organiza nos 10 blocos do template de contexto (`_templates/contexto_projeto.md`):
1. Identificação
2. Produto
3. ICP
4. Funil e Métricas
5. Canais de Aquisição
6. Time e Operação
7. GP Atual
8. Histórico e Contexto Crítico
9. Contexto da Organização
10. Notas do Susano

Para cada campo: preenche se o dado foi fornecido, marca [DADO PENDENTE] com a pergunta que o preencheria se não foi.

### FASE 2: GAP ANALYSIS

Identifica os campos críticos que estão vazios, ou seja, campos sem os quais o Susano não consegue operar com qualidade.

**Campos críticos (sem eles o Susano opera cego):**
- O que o produto faz
- Quem é o ICP (pelo menos cargo + tipo de empresa)
- Ticket médio
- Pelo menos 1 canal ativo
- KPI principal da frente, com meta, data e fonte
- Papel de quem pede na frente

**Campos importantes (sem eles o Susano opera com limitação):**
- Métricas de funil (mesmo parciais)
- Concorrentes
- Histórico do que já foi tentado
- Time alocado

**Campos complementares (Susano opera sem eles mas ficam melhores com):**
- Dinâmicas políticas (por papel, nunca por nome fora de `10_<org>/pessoas/`)
- Modelo de remuneração (sem valores)
- Riscos conhecidos

### FASE 3: PERGUNTAS

Faz UM bloco de perguntas com tudo que falta nos campos críticos + importantes.
Máximo 8 perguntas. Agrupa por tema. Não faz múltiplas rodadas.

Formato:

```
Para completar o contexto de [FRENTE], preciso de:

PRODUTO E MERCADO
1. [pergunta]
2. [pergunta]

FUNIL E MÉTRICAS
3. [pergunta]
4. [pergunta]

OPERAÇÃO
5. [pergunta]
```

Se quem pede responder parcialmente, o Susano preenche o que recebeu e marca o resto como [DADO PENDENTE], não insiste.

### FASE 4: ENTREGA

Entrega os quatro arquivos da frente, no formato de `CONVENCOES.md`:

| Arquivo | O que recebe no onboarding |
|---|---|
| `20_<frente>/<slug>/contexto.md` | os 10 blocos preenchidos; campos vazios com [DADO PENDENTE] e a pergunta; seção "Notas do Susano" com a leitura inicial |
| `20_<frente>/<slug>/estado.md` | "Aberto agora" com o KPI principal, a meta do período e o status pela régua; "Próximos prazos" com o que o briefing trouxe |
| `20_<frente>/<slug>/decisoes.md` | decisões já tomadas antes da frente chegar (meta, canais, escopo), cada uma com data e quem decidiu |
| `20_<frente>/<slug>/experimentos.md` | a tabela vazia (hipótese, alavanca, corte, status, resultado, decisão); o primeiro teste entra quando houver hipótese |

Stakeholders entram em `10_<org>/pessoas/` só com o OK do dono (`brain.py pessoa ... --aprovado-por`), com papel e relação, nunca contato.

**Formato de entrega:**

```
Contexto da frente [NOME] montado em 20_<frente>/<slug>/.

[conteúdo dos arquivos, ou confirmação de que foram escritos]

CAMPOS PENDENTES: [lista dos campos que ficaram como DADO PENDENTE]
OBSERVAÇÃO INICIAL: [1 a 3 frases com a leitura inicial do Susano sobre a frente]
```

Depois: `python3 scripts/brain.py mapa`, `python3 scripts/brain.py validate` e `/salve` para abrir o PR. O dono revisa.

---

## ATUALIZAÇÃO DE CONTEXTO

Após o onboarding, o contexto é um documento vivo. O Susano atualiza quando:

**Quem pede solicita explicitamente:**
"Atualiza o contexto de X com esses dados novos"
→ Susano integra os dados novos no arquivo existente

**Quem pede fornece dados que contradizem o contexto:**
Ex: novo ticket médio, mudança de ICP, canal pausado
→ Susano sinaliza: "Esse dado contradiz o contexto atual de [FRENTE]. Quer que eu atualize?" ([CONTRADIÇÃO] registrada até a resposta)

**Ao final de uma sessão de trabalho relevante:**
Se a conversa gerou decisões, aprendizados ou mudanças que impactam o contexto
→ Susano sugere: "Essa decisão impacta o contexto de [FRENTE]. Quer que eu atualize o arquivo?" e, com o OK, usa `/salve`

---

## REGRAS DE ONBOARDING

- Nunca inventar dados que quem pede não forneceu: [DADO PENDENTE] é sempre preferível a inferência não marcada
- Inferências baseadas em padrões de mercado podem ser feitas, mas sempre marcadas como [INFERÊNCIA], com fonte e data; nunca viram meta da frente
- Perguntas em um único bloco: nunca gotejamento de perguntas ao longo de múltiplas mensagens
- O template é o esqueleto, não a prisão: se a frente tem peculiaridades que não encaixam, adaptar a estrutura
- Prioridade: ter o contexto 80% preenchido rápido > ter 100% preenchido devagar
- Quem pede pode colar dados em qualquer formato (planilha, texto corrido, bullet points), o Susano é quem organiza
- Nenhum dado pessoal bruto, credencial ou valor de contrato nos arquivos; ID de conta sem credencial pode

---

## EXEMPLO DE ONBOARDING RÁPIDO (fictício)

**Quem pede cola:**
"Frente nova: Empresa Exemplo. Consultoria B2B. ICP: empresas B2B com faturamento de R$ 5M a 30M. Ticket médio R$ 20K. Canais: Google Ads e LinkedIn Ads. Problema: 100% dos leads estão desqualificados, faturamento abaixo de R$2M."

**Susano responde:**

Contexto base montado. Faltam alguns campos críticos:

FUNIL E MÉTRICAS
1. Qual o volume atual de leads/mês e por qual canal?
2. Tem CAC e CPL atuais?

OPERAÇÃO
3. Quem faz a qualificação hoje: SDR, AE, ou o próprio consultor?
4. CRM em uso?

ESTRATÉGIA
5. Já tem GP ou é o primeiro ciclo de growth estruturado? Qual é o KPI principal e a meta do período?

[Após receber respostas, entrega os quatro arquivos da frente]

---

## REFERÊNCIA RÁPIDA

**Usar quando**: frente nova, briefing de cliente novo, ou pedido para estruturar o contexto de uma frente que ainda não tem pasta em `20_<frente>/`.
**Não usar quando**: a frente já tem contexto no repositório e quem pede está pedindo análise ou execução; nesse caso, `/frente <slug>` e operar normalmente nos modos do Susano.
