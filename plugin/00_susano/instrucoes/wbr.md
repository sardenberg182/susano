---
id: instr-wbr
tipo: instrucao
autor: Sarden
carrega_em: sob demanda (skill susano-rituais)
origem: playbook de WBR e template de squad da operação do Sarden (mar/2026), mais as leituras de WBR consolidadas (mar a out/2026); exemplo fictício
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# WBR: Weekly Business Review

## O QUE É

A reunião semanal em que cada líder de frente apresenta e defende os resultados das frentes sob sua responsabilidade para a liderança. Não é reunião de status: é análise crítica, decisão e alinhamento. Quem apresenta chega com número atualizado, desvio analisado e próximos passos com ganho esperado e KPI associado a cada ação. A planilha de dados é obrigatória e atualizada antes da reunião; a preparação é na véspera.

## RÉGUA DE STATUS PELO KPI PRINCIPAL

O status é definido pelo KPI principal em relação à meta, nunca pela percepção de quem apresenta. Default do método, a calibrar por organização e registrar em `10_<org>/`:

| Status | Critério | O que fazer |
|---|---|---|
| No Ritmo | KPI principal em 90% ou mais da meta (pro-rata) | Manter cadência; destacar o que funciona |
| Sinal de Alerta | 70% a 89% | Plano corretivo com ganho esperado claro |
| Fora de Rota | abaixo de 70% | Decisão imediata: replan formal ou escalada |

"80 e poucos por cento" é Sinal de Alerta, não Fora de Rota; 4 de 7 (57%) é Fora de Rota. O status falado precisa sustentar o número.

Variante por projeção final (agenda de trabalho): No Ritmo quando "em linha" é maior ou igual à meta; Sinal de Alerta quando "em linha" está abaixo da meta mas a projeção final (em linha mais o ganho da agenda) alcança a meta, ou seja, a meta depende de a agenda executar; Fora de Rota quando a projeção final fica abaixo da meta, o que exige replan formal com novo número documentado, não ajuste de projeção. Em frente com farol simples: verde 100%, amarelo 80%, vermelho abaixo de 80%, sem tolerância a justificativa de sazonalidade.

## ESTRUTURA

### Nível 1: overview (5 a 8 minutos)

**Bloco A, cabeçalho**: líder da frente; data; semana de referência; frentes ativas; link da planilha de dados; link do CRM ou BI.

**Bloco B, overview**: B1, resumo executivo em 3 a 5 frases para quem já leu o documento (resultado geral contra meta, principal highlight, principal risco, movimento prioritário da próxima semana); B2, painel consolidado com todas as frentes: status, KPI principal, meta da semana, realizado, comentário de uma linha.

### Nível 2: por frente (5 a 8 minutos cada)

- **C1, identificação**: frente, prazo do contrato, status pelo KPI principal.
- **C2, indicadores**: tabela Indicador | Plan semana | Real semana | Plan mês | Real mês, com KPI principal e até dois secundários.
- **C3, análise**: contexto em 2 a 3 frases; análise do gap com o tipo de desvio e o impacto no KPI; highlights; pontos de atenção; replan, se houver, com racional e novo número acordado.
- **C4, execução**: tabela Tarefa | Responsável | Ganho esperado (KPI) | Status | Prazo | Replan. Ganho esperado em um de quatro formatos: resultado direto no KPI principal ("2 SQLs"); melhoria em KPI secundário ("+15% de taxa de resposta"); habilitador ("viabiliza o KPI X"); suporte operacional (com justificativa curta).
- **C5, aprendizados, riscos e pedido de apoio**: o que mudou o jeito de executar nesta semana; o risco que compromete o KPI; o que precisa da liderança (decisão, verba, contato, recurso), com dono e data.
- **C6, próximos passos**: tabela Ação | Responsável | Ganho esperado (KPI) | Prazo. Toda ação com ganho e KPI, sem exceção.

## GLOSSÁRIO

- **WoW** e **MoM**: variação percentual semana contra semana, mês contra mês.
- **Replan**: replanejamento formal de meta com justificativa documentada e novo número acordado.
- **KPI de input**: mede ação controlada pelo time (campanhas ativas, leads, reuniões). **KPI de output**: mede resultado final (receita, contratos, CAC).
- **Status de tarefa**: DONE (entregue e validada; confirmar se o KPI reagiu), IN PROGRESS (no prazo; monitorar atraso), TO DO (sem responsável e prazo é inválida), BLOCKED (dependência externa; escalar e documentar impacto), CAIU (cancelada; documentar motivo e avaliar replan).

## TIPOS DE DESVIO

- **Falha de execução**: tarefa não entregue, cadência baixa, falta de foco. Revisar o plano com próximos passos concretos.
- **Hipótese errada**: canal que não funciona, oferta inadequada, ICP fora de alvo. Replan com nova estratégia documentada.
- **Fator externo**: dependência de cliente, bloqueio técnico, prazo alterado. Documentar, escalar, ajustar cronograma.

## A LENTE DE LEITURA EM 7 PERGUNTAS

O status pelo número é só a entrada. A leitura passa por sete perguntas, nesta ordem:

1. **Tá em linha? Pelo pacing, não pelo mês.** "Era para estarmos em quanto hoje?" é a primeira pergunta. Antes de reagir, conferir se a métrica e o período na tela são os certos.
2. **Onde está o furo, e é volume ou taxa?** Uma etapa quebrada por frente, separando efeito de verba do efeito de conversão. Lead para MQL igual com mais MQL é dinheiro; CPL melhor com conversão pior é volume sem qualidade.
3. **O diagnóstico bate com o número?** Contexto diz "o problema é volume" e o PA não mexe em volume: PA perdido. Otimizar página quando o problema é qualificação: PA perdido.
4. **O PA mexe na alavanca que quebrou?** Qualidade se resolve com qualificação (formulário com mais barreira, público mais fechado), não com criativo novo ou verba. Uma alavanca em foco; o resto é sustentação e está marcado como tal. Quando o PA não para em pé, levar uma hipótese na alavanca certa.
5. **Quanto, por quê e o que deixa de fazer.** Todo PA com indicador, percentual de ganho e tese que se entende sem explicação oral.
6. **A meta é jogável? Primeiro a regra do jogo.** Teto antes do plano (volume máximo de envio, verba, capacidade). Se não fecha: reprojetar, quebrar a meta por peso de canal e realinhar com o cliente na mesma semana. Pedido de verba sempre ancorado em projeção.
7. **Estrutura antes de escala.** MQL se qualifica no formulário, SQL no SDR, não-MQL fica como lead (é ativo); custo por MQL e SQL vale mais que CPL; CRM centralizado.

Três filtros quando o caso pede: **forecast que aguenta perder uma conta** (backlog com várias contas em negociação, não uma salvadora); **canal por evidência** (o que funcionou em frente parecida, não feeling; lista boa vale mais que lista grande; base de cliente nunca se cruza); **compromisso é compromisso** (prazo que muda vira decisão explícita e a atenção vai para o risco de execução).

Saída da leitura por frente: melhor ponto → ponto de atenção → a pergunta na sala.

## PA COMPLETO: GANHO, DONO E PRAZO JUNTOS

Conta como ganho esperado só quando a ação diz qual indicador move e quanto. "Aumentar a receita" e "fechar o gap" não contam; a organização não é dono. Padrão a cobrar: onde tem ganho falta dono e prazo; onde tem dono e prazo falta ganho. Fechar o loop "ganho prometido na semana anterior aconteceu?" é raro e precisa ser cobrado. Tabela de próximos passos copiada da semana anterior é falha de documento. Bloqueio de cliente pede escalada com dono e data no campo de pedido de apoio.

Leituras recorrentes: decompor gap de receita em volume × ticket (PA que só ataca volume deixa metade do gap na mesa); parte do "gargalo no topo" costuma ser medição (leads que não chegam ao CRM); olhar a taxa certa do canal antes de cortar; realocação por custo unitário vira ganho em número; ganho em taxa não basta quando o absoluto cai; "MQL igual a envio de proposta" mede ação comercial, não qualificação; verificar a unidade do contrato antes de dimensionar o gap; projeção que soma efeitos independentes é projeção errada; inbound batido com demanda reciclada não é demanda nova; risco escrito e não tratado é risco aceito; campanha no ar sem meta de CPL ou de lead não é operação.

## DIARIZAR

Contar os dias úteis → diarizar a meta → quebrar por canal → estimar o ganho de cada um → montar a estratégia → acompanhar todo dia e replanejar. Dá trabalho, por isso quase ninguém faz, por isso quem faz sai na frente.

## PRÉ E PÓS-AGENDA (em primeira pessoa)

Modelo em primeira pessoa, que espelha como a pessoa já pensa; modelo que exige tradução mental morre em duas semanas. Tese se escreve em frase conectada: se a frase não fecha, ainda não se sabe o que se pensa.

PRÉ: **Minha tese** (2 a 4 linhas em prosa) → **Insights que eu tirei** (do contexto, das conversas anteriores, dos dados) → **O que eu preciso falar** (checklist, não script) → **O que eu espero que aconteça** (o que sai decidido, quem sai comprometido com o quê; sem este bloco, a reunião vira mensagem).

PÓS: **Fatos importantes** (fato, não interpretação) → **Observações** (leituras, sinais, entrelinhas) → **O que ficou combinado** (quem faz o quê até quando). Separar fato de observação de propósito: misturar os dois é como nasce a narrativa que vira "verdade" três semanas depois. Compromisso não registrado é o buraco que custa caro.

## AGENDA DE E-COMMERCE

Em e-commerce a receita decompõe em três alavancas (sessões × conversão × ticket médio); todo gap e toda ação cabem em uma delas e o documento não precisa de narrativa.

Estrutura: cabeçalho (frente, período, KPI, meta, fonte do realizado, responsável) → tese em três linhas (tese do período; gap explicado em tráfego, conversão ou ticket e em qual canal; aposta da agenda) → resultado em uma linha (Meta | Realizado | Em linha | Ganho da agenda | Projeção final | Status) → alavancas (sessões, conversão, pedidos, ticket) → por canal (paid social, paid search e shopping, orgânico, CRM, direto e marca, marketplaces e afiliados) → agenda (ação, canal, alavanca, conta do ganho, ganho em R$, responsável, prazo, status).

Regras: em linha é realizado mais a média diária dos últimos 14 dias vezes os dias restantes, ajustado pela curva do mesmo período do ano anterior quando há data promocional (nunca projeção linear em mês com evento); realizado por canal vem de uma fonte só, definida no cabeçalho (número de plataforma de mídia é diagnóstico); ganho esperado sempre em R$ com a conta aberta (Δ × base); totais batem entre blocos; só entra número com fonte, o resto fica `{{ }}`.

## COMO O SUSANO AJUDA

- **"Monta o WBR" ou "preenche com estes dados"**: documento completo na estrutura acima; campo sem informação vira [DADO PENDENTE] (documento interno); nenhum KPI numérico sem fonte confirmada.
- **"Analisa o WBR"**: passa as 7 perguntas; confere se o status bate com o número, se toda ação tem ganho, dono e prazo, se a análise do gap nomeia o tipo de desvio.
- **"Escreve o resumo executivo"**: B1 em 3 a 5 frases, para quem já leu.
- **"Prepara o WBR"**: monta a partir dos dados fornecidos, sinaliza o que falta, entrega pronto.

## REGRAS QUE NUNCA VIOLA

- Nunca define status pelo feeling: sempre pelo KPI principal contra a meta.
- Nunca preenche KPI ou resultado sem dado confirmado.
- Nunca entrega ação sem ganho esperado e KPI associado.
- Nunca omite BLOCKED: tarefa travada aparece com o impacto no KPI.
- Nunca redige análise de gap genérica: sempre o tipo de desvio e o impacto específico.
- Nunca mistura dado de uma frente em outra.

## EXEMPLO FICTÍCIO

Duas frentes inventadas, semana 4 de um mês qualquer. Metalúrgica Ômega: 7 SQLs contra meta de 6 (117%), No Ritmo, com um modelo novo de follow-up por setor documentado e replicável. Farmácias Vida+: 1 SQL contra meta de 4 (25%), Fora de Rota, por bloqueio de verba do cliente há duas semanas.

Resumo executivo: "Semana dividida. Ômega entregou acima da meta com o novo follow-up por setor, já documentado. Vida+ está Fora de Rota por bloqueio de verba do cliente há duas semanas. Sem decisão hoje para escalar ao sponsor, o mês fecha em 43% da meta."

Próximo passo correto (Vida+): "Liderança contata o sponsor para liberar a verba, viabiliza 3 SQLs adicionais (KPI principal), prazo sexta-feira, dono: nome do líder da frente."

## REFERÊNCIA RÁPIDA

**Melhor para**: montar, preencher, revisar ou analisar o WBR e a agenda de trabalho semanal de qualquer frente; preparar e fechar reunião com a lente das 7 perguntas.
**Ativar quando**: o pedido envolve WBR, agenda semanal, status de frente, resumo executivo de semana, pré ou pós de reunião de resultado. Outros rituais (GP, BP) têm estrutura própria em `gp_bp.md`.
