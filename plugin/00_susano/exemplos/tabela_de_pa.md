---
id: ex-tabela-de-pa
tipo: exemplo
modo: 2
situacao: "transforma isso em plano de ação", "monta a tabela de PA"
autor: Raijin (forma); método do Sarden
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Exemplo: tabela de PA a partir de fatos e causas

Empresa e números inventados. A forma é o que vale.

## ENTRADA

Quem pede: líder da frente Serra Ferramentas (distribuidora B2B com e-commerce próprio; ticket médio do pedido R$ 1.900; margem de contribuição 22%; 1.400 pedidos no mês passado).

> "Saí da reunião com estes fatos e causas. Transforma em PA para eu levar na sexta. Já incluí a ideia do Instagram que o cliente adora."

Colado:

1. Fato: conversão do checkout no mobile em 0,9%; no desktop, 1,8%; 64% das sessões são mobile (GA4, últimos 30 dias). Causa levantada: formulário de endereço com 9 campos e sem preenchimento por CEP; erro de validação de CNPJ só aparece depois do envio.
2. Fato: 38% dos pedidos do mês vieram de 12 clientes; ticket médio caiu 11% em 60 dias (CRM e ERP). Causa levantada: os 12 grandes migraram parte das compras para pedido direto com o vendedor, onde ganham desconto de 8% que o site não oferece.
3. Fato: zero e-mails de carrinho abandonado enviados nas últimas 3 semanas (plataforma de e-mail); 2.300 carrinhos abandonados no período (GA4). Causa levantada: automação não foi recriada na troca de ferramenta.
4. Ideia do cliente: postar 3 vezes por semana no Instagram "para aumentar o awareness da marca".

## SAÍDA

Três PAs entram, um fica de fora. Ganho com a conta aberta; onde a base não está na frente, [LACUNA] no lugar de chute.

| Fato | Causa | PA | Dono e prazo | Indicador-chave | Expectativa de ganho |
|---|---|---|---|---|---|
| Checkout mobile converte 0,9% contra 1,8% no desktop, com 64% das sessões no mobile [DADO: GA4, 30 dias] | formulário de endereço com 9 campos, sem CEP automático; validação de CNPJ só no envio [INFERÊNCIA: causa levantada na reunião, confirmar com gravação de sessão] | endereço por CEP (3 campos digitados), validação de CNPJ no campo, barra de progresso; medir por dispositivo | dev do e-commerce, no ar em 10 dias úteis; leitura em 30 dias | taxa de conversão do checkout mobile | de 0,9% para 1,3% sobre os 659 pedidos/mês que o mobile gera hoje (64% das sessões a 0,9%) → +293 pedidos/mês × R$ 1.900 = + R$ 557 mil de receita → + R$ 122 mil de margem/mês. Corte: abaixo de 1,1% em 30 dias, mata |
| 38% dos pedidos em 12 clientes; ticket médio caiu 11% em 60 dias [DADO: CRM e ERP] | os 12 grandes compram parte direto com o vendedor por 8% de desconto que o site não dá [INFERÊNCIA: hipótese comercial, confirmar com 3 dos 12] | política de preço única: desconto por volume no site igual ao do vendedor, com faixa por valor de pedido; vendedor comissionado também no pedido online da carteira | diretor comercial, decisão até sexta; implantação em 15 dias | ticket médio e share dos 12 no site | recuperar metade da queda de ticket: +5,5% × R$ 1.900 × 1.400 pedidos = + R$ 146 mil/mês de receita, margem a confirmar com o custo do desconto [LACUNA: desconto médio praticado hoje pelo vendedor] |
| 2.300 carrinhos abandonados em 3 semanas, zero e-mails enviados [DADO: GA4 e plataforma de e-mail] | automação não recriada na troca de ferramenta | recriar a automação (1 h, 24 h, 72 h) com o carrinho no corpo e cupom só no terceiro envio; evento de envio e de pedido recuperado no GA4 | gestora de CRM, no ar em 5 dias úteis | pedidos recuperados por carrinho abandonado | recuperação de 3% dos 3.000 carrinhos/mês projetados → +90 pedidos × R$ 1.900 = + R$ 171 mil/mês de receita (3% é a taxa que a frente teve antes da troca, [DADO: relatório da ferramenta antiga, 60 dias]) |

**Fica de fora: "Postar 3 vezes por semana no Instagram para aumentar awareness."** Não passa no filtro do ponteiro: não há indicador que ligue post a pedido na janela do plano, nem baseline de tráfego orgânico do Instagram para o site (0,8% das sessões, GA4). Não move CAC, LTV nem payback de forma que dê para medir em 30 dias. Não é plano, é atividade. Se o cliente quer testar, vira hipótese com corte, não PA: "Baseado em [nenhum dado da frente, só preferência], eu espero que 3 posts/semana com link de produto vão gerar X sessões e Y pedidos em 60 dias" → a frente não tem o X nem o Y, então o teste nasce sem corte e não entra no plano desta sexta. Entra no backlog como P4 até ter uma hipótese que se possa matar.

Ordem de prioridade (ICE): 1) carrinho abandonado (impacto alto, confiança alta pela taxa histórica, esforço de 5 dias); 2) checkout mobile (impacto maior, confiança média, esforço de dev); 3) política de preço (impacto alto, confiança média, esforço de decisão comercial e troca de incentivo). Os três cabem no mês; o terceiro depende de decisão do diretor na sexta, então ele é quem segura o risco.

Uma observação fora do pedido, sinalizada: os ganhos não se somam. O checkout mobile e o carrinho abandonado disputam parte dos mesmos pedidos (carrinho abandonado no mobile por causa do formulário). A projeção combinada é menor que + R$ 874 mil; levar os três ganhos separados, não a soma.

## POR QUE ASSIM

- Todo PA nasce de FATO e CAUSAS e carrega indicador, ganho, dono e prazo juntos; ganho sempre em R$ ou no KPI da frente, com a conta aberta (Δ × base): `00_susano/dna/metodo/diagnostico_de_funil.md#PLANO DE AÇÃO` e `00_susano/instrucoes/wbr.md#PA COMPLETO: GANHO, DONO E PRAZO JUNTOS`.
- O filtro do ponteiro (move CAC, LTV ou payback?) é o que tira a ideia do Instagram do plano sem desqualificar o cliente: vira hipótese sem corte, portanto backlog, não PA: `00_susano/dna/metodo/diagnostico_de_funil.md#MODELOS ATIVOS` ("Filtro do ponteiro") e `00_susano/instrucoes/operacao_e_time.md#PRIORIZAÇÃO`.
- Causa levantada em reunião é [INFERÊNCIA] até ser confirmada; a base que falta é [LACUNA], nunca um número de mercado no lugar: `00_susano/nucleo.md#Sempre e nunca`.
- A adição fora do pedido (os ganhos não se somam) é dita como adição, não embutida: `00_susano/nucleo.md#Sempre e nunca` e `00_susano/dna/metodo/diagnostico_de_funil.md#ALERTAS OPERACIONAIS` (nunca somar efeitos como independentes).
- Marcadores aparecem porque a tabela é documento interno da frente; a versão que vai para o cliente na sexta sai sem marcador, com o [LACUNA] do desconto resolvido antes: `00_susano/nucleo.md#Sempre e nunca`.
