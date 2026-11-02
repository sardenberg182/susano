---
id: ex-leitura-de-wbr
tipo: exemplo
modo: 1
situacao: "prepara o WBR", "analisa o WBR", "qual o status da frente"
autor: Raijin (forma); método do Sarden
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Exemplo: leitura de WBR com duas frentes

Empresas, pessoas e números inventados. A forma é o que vale.

## ENTRADA

Quem pede: líder de duas frentes, na véspera do WBR. Semana 3 de um mês com 21 dias úteis; hoje é o 16º (pro-rata 76%).

> "Lê o meu WBR antes da reunião de amanhã e me diz onde eu vou apanhar."

Painel colado (fonte: planilha de dados da frente, atualizada hoje às 9h):

| Frente | KPI principal | Meta do mês | Meta pro-rata (76%) | Realizado | Status informado |
|---|---|---|---|---|---|
| Clínicas Aurora | agendamentos de avaliação | 320 | 243 | 251 | No Ritmo |
| Logística Pampa | SQLs | 24 | 18 | 9 | Sinal de Alerta ("o mês ainda tem duas semanas") |

Secundários colados:
- Aurora: custo por agendamento R$ 48 (plano R$ 55); comparecimento às avaliações 61% (histórico 70%).
- Pampa: MQLs 67 (plano pro-rata 61); MQL → SQL 13,4% (plano 30%). Por canal: LinkedIn Ads 51 MQLs → 4 SQLs (7,8%); Google Search 16 MQLs → 5 SQLs (31,3%).

Próximos passos no documento:
- Aurora: "Subir a verba do Meta em 20%", ganho esperado "+40 agendamentos", dona: gestora de mídia, prazo sexta.
- Pampa: "Produzir 4 criativos novos para LinkedIn" (sem ganho esperado); "Aumentar a cadência de follow-up" (sem dono, sem prazo).

## SAÍDA

Status pela régua, antes de qualquer leitura (`decisoes.md` da frente: 90% ou mais No Ritmo, 70% a 89% Sinal de Alerta, abaixo de 70% Fora de Rota):

| Frente | Realizado / pro-rata | Status pela régua | Status informado | Bate? |
|---|---|---|---|---|
| Aurora | 251 / 243 = 103% | No Ritmo | No Ritmo | sim |
| Pampa | 9 / 18 = 50% | Fora de Rota | Sinal de Alerta | não |

Pampa vai apanhar no primeiro minuto: 50% não é alerta, é Fora de Rota. "O mês ainda tem duas semanas" não é critério; a régua é pro-rata, e você combinou isso.

**Clínicas Aurora**

- Melhor ponto: volume e custo acima do plano juntos (251 agendamentos a R$ 48, 13% abaixo do custo planejado). Isso é mídia funcionando.
- Ponto de atenção: o furo não é volume, é taxa. Comparecimento caiu de 70% para 61% [DADO: planilha da frente, hoje]. Em agendamentos presentes, 251 × 61% = 153, contra 243 × 70% = 170 que o plano supõe. Você está 10% abaixo do plano na métrica que vira receita, com o KPI principal no verde. Taxa no topo com qualidade caindo é volume sem qualidade.
- O PA não mexe na alavanca que quebrou: "+20% de verba" ataca volume; o problema é comparecimento. Mais agendamento com 61% de presença é mais no-show pago. [INFERÊNCIA] a queda de presença coincide com o volume maior do Meta (público mais frio); conferir presença por canal antes de concluir.
- Hipótese para levar no lugar: "Baseado na queda de comparecimento de 70% para 61% com o volume do Meta subindo (dado próprio da frente), eu espero que confirmação por WhatsApp 24 h antes com reagendamento em um toque vai levar a presença de volta a 68% → +18 avaliações presentes no mês → + R$ (18 × ticket de avaliação convertida, pela taxa de fechamento da frente)". Corte: 2 semanas ou 120 agendamentos; abaixo de 65%, mata e volta para público. Dona: a mesma gestora. Verba do Meta fica onde está até a presença voltar.
- A pergunta na sala: "Quantas dessas 251 pessoas sentaram na cadeira?"

**Logística Pampa**

- Melhor ponto: topo cheio. 67 MQLs contra 61 do plano pro-rata (110%). Volume não é o problema, e isso precisa ser dito antes de alguém pedir mais verba.
- Ponto de atenção: MQL → SQL em 13,4% contra 30% do plano, 16,6 pontos abaixo. Por canal, a queda é concentrada: LinkedIn converte 7,8%, Google 31,3% (no plano). Com o mesmo SDR e o mesmo critério de SQL, canal que converte um quarto do outro está atraindo errado, não tratando mal. [INFERÊNCIA] cargo ou porte fora do ICP no público do LinkedIn; confirmar com os 51 MQLs na planilha (cargo e número de funcionários).
- O diagnóstico do documento não bate com o número: "produzir criativos" supõe que o problema é atração de volume; o volume está acima do plano. "Aumentar cadência de follow-up" trataria "trata mal"; o Google com o mesmo follow-up converte no plano. Dois PAs na alavanca errada, e nenhum dos dois completo: criativo sem ganho esperado, follow-up sem dono e sem prazo. PA pela metade não é PA.
- A meta é jogável? Faltam 15 SQLs em 5 dias úteis. Mesmo que a taxa volte a 30% a partir de amanhã sobre os cerca de 21 MQLs restantes no ritmo atual, entram 6 SQLs: fecha em 15 de 24, 63%, Fora de Rota de qualquer jeito. Então o assunto da reunião não é "como salvar o mês"; é replan formal com número novo documentado e a correção estrutural para o mês que vem.
- Estrutura antes de escala: qualificação no formulário do LinkedIn (cargo e porte como campos obrigatórios) e público fechado por cargo do ICP. Quem não passa fica como lead, que é ativo, não lixo. Mede por custo por SQL, não por CPL: o CPL vai subir e é esperado.
- O que levar amanhã: (1) status corrigido para Fora de Rota, dito por você antes que digam por você; (2) replan: meta do mês para 15 SQLs com a justificativa (público fora do ICP no LinkedIn desde a semana 1), e o número do mês seguinte mantido em 24 com a qualificação no ar; (3) um PA só, completo: "Fechar o público do LinkedIn por cargo do ICP e colocar cargo e porte como campos obrigatórios no formulário; ganho esperado: MQL → SQL do LinkedIn de 7,8% para 25% → +6 SQLs/mês; dona: gestora de mídia com o SDR; no ar até quarta; leitura em 30 dias".
- A pergunta na sala: "Se o Google converte 31% com o mesmo SDR, por que o PA é criativo?"

**Resumo executivo para o B1 (3 a 5 frases, para quem já leu):** Semana dividida. Aurora bate volume e custo (103% da meta pro-rata, R$ 48 por agendamento), mas o comparecimento caiu para 61% e a correção vai para presença, não para verba. Pampa está Fora de Rota (50%), com topo acima do plano e MQL → SQL do LinkedIn em 7,8%: problema de público, não de volume; replan para 15 SQLs no mês e qualificação no formulário no ar até quarta. Decisão pedida à liderança: aprovar o replan da Pampa hoje.

## POR QUE ASSIM

- Status pela régua antes da leitura, e a divergência com o status falado dita na primeira linha: `00_susano/instrucoes/wbr.md#RÉGUA DE STATUS PELO KPI PRINCIPAL` e `#REGRAS QUE NUNCA VIOLA` (nunca pelo feeling).
- A leitura segue as sete perguntas na ordem (pacing, volume ou taxa, diagnóstico bate, alavanca certa, quanto e por quê, meta jogável, estrutura antes de escala) e fecha por frente em melhor ponto → ponto de atenção → a pergunta na sala: `00_susano/instrucoes/wbr.md#A LENTE DE LEITURA EM 7 PERGUNTAS`.
- PA só conta com ganho, dono e prazo juntos; os dois PAs da Pampa são devolvidos e um PA completo entra no lugar: `00_susano/instrucoes/wbr.md#PA COMPLETO: GANHO, DONO E PRAZO JUNTOS`; a hipótese da Aurora está na frase base com corte: `00_susano/dna/metodo/diagnostico_de_funil.md#HIPÓTESE`.
- Queda concentrada num canal aponta atração, queda transversal aponta processo (filtro binário): `00_susano/dna/metodo/diagnostico_de_funil.md#AS 7 CHECAGENS ANTES DE APONTAR GARGALO`, checagens 4 e 7.
- Marcadores [DADO] e [INFERÊNCIA] aparecem porque a leitura é documento interno do líder; o B1 que vai para a reunião sai sem marcador: `00_susano/nucleo.md#Sempre e nunca`.
