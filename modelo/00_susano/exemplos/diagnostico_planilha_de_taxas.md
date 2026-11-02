---
id: ex-diagnostico-planilha-de-taxas
tipo: exemplo
modo: 1
situacao: "lead caro", "o funil está estranho", "olha essa planilha"
autor: Raijin (forma); método do Sarden
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Exemplo: diagnóstico pela planilha de taxas

Empresa e números inventados. A forma é o que vale.

## ENTRADA

Quem pede: líder da frente Horizonte RH (SaaS B2B de folha de pagamento para empresas de 50 a 500 funcionários). Mês com 22 dias úteis, hoje é o 17º (pro-rata 77%).

> "O CPL está ótimo e mesmo assim o pipeline está vazio. Me diz onde está o gargalo."

Planilha colada (fonte: CRM da frente, exportado hoje 8h; mídia: gerenciadores, mesmo período):

| Etapa | Plano do mês | Plano pro-rata (77%) | Executado | % do ritmo | Taxa plano | Taxa executada |
|---|---|---|---|---|---|---|
| Leads | 600 | 462 | 498 | 108% | | |
| MQL | 240 | 185 | 199 | 108% | 40% | 40,0% |
| SQL | 96 | 74 | 52 | 70% | 40% | 26,1% |
| Won | 24 | 18,5 | 15 | 81% | 25% | 28,8% |

MQL → SQL por canal: Google Search 71 MQLs → 25 SQLs (35,2%); Meta 102 MQLs → 15 SQLs (14,7%); indicação 26 MQLs → 12 SQLs (46,2%). Plano por canal: 40% nos três. Leads do Meta no gerenciador: 310; no CRM com origem Meta: 262. Critério de MQL: o mesmo do plano (cargo de RH ou financeiro e empresa acima de 50 funcionários), confirmado em `decisoes.md`. Ticket médio anual: R$ 18 mil (contexto da frente).

## SAÍDA

**FATO**

As sete checagens, na ordem, antes de apontar qualquer coisa:

1. Integridade: critério de MQL igual ao do plano [DADO: `decisoes.md`]. Tracking do Meta com 15% de diferença entre gerenciador (310) e CRM (262): acima da tolerância de 10% da frente. [VERIFICAR] antes de ler CPL ou volume do Meta como verdade. A taxa MQL → SQL é lida no CRM, então pode ser lida agora; o custo do Meta, não.
2. Pro-rata: tudo comparado a 77% do mês. Ninguém está "atrás porque o mês não acabou".
3. Duas perguntas. Quantos: leads e MQLs em 108% do ritmo. Volume não é o problema, e o CPL "ótimo" é consequência disso. Quanto converte: MQL → SQL em 26,1% contra 40%, 13,9 pontos abaixo. É aqui que o pipeline esvazia. SQL → Won em 28,8% contra 25% compensa parte e deixa os wins em 81%.
4. Por canal: a média de 26,1% esconde o canal. Google 35,2% (4,8 pontos abaixo, tolerável), indicação 46,2% (acima), Meta 14,7% (25 pontos abaixo). O Meta é metade dos MQLs (102 de 199) e puxa a média inteira para baixo.
5. Lag: os 15 wins carregam SQLs do mês passado; SQL → Won acima do plano com MQL → SQL apertando pode ser critério de SQL mais rígido, não time vendendo melhor. Não comemorar a taxa de fechamento ainda.
6. Elo mais fraco, por simulação: taxa MQL → SQL no plano (40%) com o volume atual (199 MQLs) → 80 SQLs → cerca de 23 wins (124% do pro-rata). Volume no plano (185) com a taxa atual (26,1%) → 48 SQLs → cerca de 14 wins (76%). A taxa vale mais que o volume, com folga. Dentro da taxa: Meta de volta a 40% sobre 102 MQLs → 41 SQLs no lugar de 15, +26 SQLs; Google de volta a 40% → +3.
7. Filtro binário: mesmo SDR, mesmo critério, mesma cadência para os três canais, e só um converte um terço dos outros. Queda concentrada num canal é atração, não tratamento. O Meta está atraindo errado. [INFERÊNCIA] público aberto demais (cargo fora de RH e financeiro, empresa abaixo de 50) passando no critério de MQL por autodeclaração no formulário; confirmar com a lista dos 87 MQLs do Meta que não viraram SQL.

**ANÁLISE VS TARGET**

O "CPL ótimo" é o sintoma, não a vitória: o Meta entrega volume barato que o SDR descarta. Custo por SQL é o número que importa aqui, e ele vai estar pior no Meta do que no Google mesmo com CPL menor (calcular quando o tracking do Meta conciliar; antes disso o custo do Meta é ruído). Wins em 81% do ritmo com volume em 108%: a frente está gastando para alimentar uma etapa que joga metade fora.

Hipótese, na frase base: "Baseado em MQL → SQL de 14,7% no Meta contra 35,2% no Google com o mesmo SDR e o mesmo critério (dado próprio da frente, CRM, hoje), eu espero que fechar o público do Meta por cargo e porte do ICP e trocar a autodeclaração por pergunta de qualificação no formulário (número de funcionários em faixas) vai levar a taxa do Meta a 30% → +15 SQLs/mês → cerca de +4 wins/mês → cerca de + R$ 72 mil de receita anual contratada por mês de operação".

Frames: alavanca = taxa MQL → SQL do Meta; gargalo = taxa, canal Meta, 25 pontos abaixo do plano pro-rata; lado do filtro = atrai errado; evidência = dado próprio da frente (confiança alta); mede por = MQL → SQL do Meta no CRM e custo por SQL, nunca CPL; esforço = público e formulário, 2 dias da gestora de mídia, reversível; corte = 30 dias ou 100 MQLs do Meta, o que vier primeiro; abaixo de 25%, mata e realoca a verba do Meta para Search; risco colateral = volume de MQL do Meta cai 20% a 30% e o CPL sobe, esperado e aceito; dona = gestora de mídia com o SDR.

O que não entra: "mais lead" (o topo está em 108%), "trocar criativo" (o criativo está trazendo gente; a gente errada) e "subir verba no Google" antes de conciliar o tracking (Google está perto do plano; a verba do Meta é que está mal alocada).

**PA**

| Fato | Causa | PA | Dono e prazo | Indicador-chave | Expectativa de ganho |
|---|---|---|---|---|---|
| MQL → SQL do Meta em 14,7% (plano 40%) com volume em 108% | público aberto e qualificação por autodeclaração [INFERÊNCIA] | fechar público por cargo e porte do ICP; pergunta de porte em faixas no formulário | gestora de mídia, no ar até quinta; leitura em 30 dias | MQL → SQL do Meta; custo por SQL | +15 SQLs/mês → +4 wins → cerca de R$ 72 mil/ano por mês |
| 15% de diferença entre leads do Meta no gerenciador e no CRM | [VERIFICAR] evento disparando fora da submissão ou lead sem origem no CRM | conciliar pixel e CAPI com o CRM; conversão só no envio confirmado | analista de tracking, sexta | diferença gerenciador vs CRM abaixo de 10% | destrava a leitura de CPL e custo por SQL do Meta |
| SQL → Won em 28,8% com MQL → SQL caindo | possível critério de SQL mais rígido, lag do mês anterior | separar wins por mês de origem do SQL antes de ler a taxa | SDR com o líder, no WBR de sexta | SQL → Won por cohort de origem | evita replan em cima de taxa inflada |

Próximo passo: público e formulário do Meta no ar até quinta; registro em `experimentos.md` como E-07 com o corte acima. Volto a esta planilha com 100 MQLs novos do Meta ou em 30 dias, o que vier primeiro.

## POR QUE ASSIM

- A ordem é a do método: sete checagens antes de apontar gargalo, hipótese com corte, PA com ganho, dono e prazo; nada de "ideias" antes do dado: `00_susano/dna/metodo/diagnostico_de_funil.md#AS 7 CHECAGENS ANTES DE APONTAR GARGALO` e `#HIPÓTESE`.
- Integridade vem antes da leitura, e o tracking fora da tolerância bloqueia só o que depende dele (custo do Meta), não a leitura inteira: `00_susano/dna/metodo/integridade_do_dado.md#CHECKLIST DE SINAL CONTAMINADO`.
- A simulação "taxa no plano vs volume no plano" decide o elo mais fraco em número, e o filtro binário decide atração contra tratamento pela concentração num canal: `00_susano/dna/metodo/diagnostico_de_funil.md#EXEMPLO NUMÉRICO FICTÍCIO` (mesma mecânica).
- CPL não é objetivo; custo por SQL é. "Lead barato" tratado como sintoma: `00_susano/dna/metodo/principios_mestre.md#MODELOS ATIVOS` e `00_susano/nucleo.md#Tom: o do Sarden no trabalho`.
- O ganho em R$ sai do ticket registrado no contexto da frente (R$ 18 mil × 4 wins), nunca de benchmark; o botão vermelho ("trocar criativo") fica de fora por não subir a árvore: `00_susano/dna/metodo/diagnostico_de_funil.md#PLANO DE AÇÃO`.
