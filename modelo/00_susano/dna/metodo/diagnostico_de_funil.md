---
id: dna-diagnostico-de-funil
tipo: metodo
autor: Sarden
nivel: ATIVO
origem: método de diagnóstico e crescimento da operação do Sarden (treinamento de alavancas, planilha de taxas, hipótese e plano de ação, mar a out/2026); exemplo numérico fictício
atualizado: 2026-11-02
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Diagnóstico de funil: da árvore de alavancas ao plano de ação

## TESE EM UMA LINHA

Diagnóstico é uma ordem, não uma opinião: árvore de alavancas, planilha de taxas executado contra planejado pro-rata, sete checagens antes de apontar gargalo, hipótese com corte e plano de ação com ganho, dono e prazo; no fim de cada teste a decisão é matar ou sistematizar.

## MODELOS ATIVOS

- **A ordem do método**: árvore de alavancas do modelo → planilha de taxas por canal (executado × planejado) → hipótese estruturada → PA com ganho esperado → ICE para priorizar → ciclo analisar → ideias → priorizar → testar → decidir. A árvore vem antes do objetivo: o objetivo só se escolhe conhecendo todas as alavancas.
- **As sete checagens**: integridade de definição e tracking; pro-rata do mês; "quantos" separado de "quanto converte"; por canal, nunca média; lag entre etapas; elo mais fraco por simulação; filtro binário atrai errado ou trata mal.
- **Hipótese com corte**: frase base mais os frames (alavanca, gargalo, lado do filtro, evidência, mede por, confiança, esforço, corte, risco colateral, dono). Hipótese sem corte não entra no plano.
- **Filtro do ponteiro**: o PA move CAC, LTV ou payback? Se não, não é plano, é atividade.
- **Matar ou sistematizar**: a decisão ao fim do teste. Sistematizar é virar processo, playbook e cadência; matar é registrar e seguir. Sem o quinto movimento, o teste vira hábito.

## A ORDEM DO MÉTODO

1. **Árvore de alavancas** do modelo de negócio: todas as alavancas que movem receita (volume por etapa, taxa por etapa, ticket, frequência, retenção), antes de escolher objetivo.
2. **Planilha de taxas por canal**, executado × planejado pro-rata: volume e taxa de cada etapa, por canal, comparados ao ritmo esperado do mês, não ao plano cheio.
3. **Hipótese estruturada** (seção abaixo), uma por gargalo, com corte definido antes de rodar.
4. **PA com ganho esperado**, nascido de FATO e CAUSAS, carregando indicador-chave (tabela da seção Plano de ação).
5. **ICE para priorizar** (impacto, confiança, esforço). Depois de priorizada, a hipótese vira tese do período.
6. **Ciclo**: analisar → ideias → priorizar → testar → decidir. A decisão se chama matar ou sistematizar (não "matar, escalar ou iterar").
7. **Biblioteca de testes**: o que já foi tentado vale mais que teoria e evita reciclar ideia morta. Mora em `experimentos.md` da frente.

## AS 7 CHECAGENS ANTES DE APONTAR GARGALO

1. **Integridade antes de leitura.** A definição de MQL e SQL é a mesma do plano? Tracking e atribuição por canal estão confiáveis? Critério que mudou no meio da série torna as taxas incomparáveis com o plano antigo.
2. **Pro-rata do mês.** Comparar com o ritmo esperado até hoje, nunca com o plano cheio.
3. **Separar as duas perguntas.** "Quantos" (volume contra plano) e "quanto converte" (taxa contra plano, em pontos percentuais). Quase sempre a resposta está na segunda.
4. **Média engana: ler por canal.** O total é dominado pelo canal de maior volume; uma média saudável no topo esconde um canal a 50%.
5. **Lag entre etapas.** SQL para Won deste mês carrega SQLs de meses anteriores. Taxa seguinte subindo quando a anterior aperta pode ser critério mais rígido, não melhoria.
6. **Elo mais fraco, um só.** Simular "e se essa taxa voltasse ao plano?" em cada nó e ver qual devolve mais resultado.
7. **Filtro binário.** O gargalo é "atrai errado" (oferta, ICP, canal) ou "trata mal" (processo, SLA, capacidade)? Queda transversal aos canais aponta processo; queda concentrada num canal aponta canal.

## HIPÓTESE

Frase base: *"Baseado em [observação + tipo de evidência], eu espero que [ação] vai endereçar [resultado esperado na métrica da etapa] → [efeito em R$ subindo a árvore até receita, CAC, LTV ou payback]"*.

Frames que fazem a frase virar aposta:

- **Alavanca**: nó da árvore que a hipótese move.
- **Gargalo**: taxa ou volume, executado contra planejado pro-rata, em qual canal ou segmento. Granular, nunca média.
- **Lado do filtro**: atrai errado ou trata mal.
- **Observação e tipo de evidência**: dado próprio da frente, benchmark com fonte, teoria ou opinião; dado de outra frente não entra, nem anonimizado.
- **Mede por**: métrica, fonte, KPI da etapa certa (nunca KPI de etapa misturada).
- **Confiança**: dada pelo tipo de evidência, não por quem deu a ideia.
- **Esforço**: horas do time, dependência do cliente ou de dev, reversível ou não.
- **Corte**: número e prazo (ou amostra mínima) que matam o teste. Definido antes de rodar.
- **Risco colateral**: qual nó pode piorar (mais MQL com MQL para SQL caindo). Hierarquia: quantidade, qualidade, sustentabilidade.
- **Dono**: uma pessoa.

O contraexemplo que fica de propósito: **o botão vermelho**. Passa no formato ("baseado em X, espero que trocar a cor do botão aumente o clique"), reprova nos frames: evidência é teoria (confiança baixa), resultado esperado é clique (não sobe a árvore até R$), não tem corte.

Primeira lente para gerar hipótese em qualquer queda de taxa: onde está o atrito? Reduzir atrito é mais barato que aumentar desejo.

## PLANO DE AÇÃO

- **Ganho esperado sempre em R$ ou no KPI da frente**, nunca na métrica intermediária. Clique não é ganho; SQL é meio; receita é fim.
- **Filtro do ponteiro**: move CAC, LTV ou payback? Se não, não é plano, é atividade.
- **Capacidade**: cabe nas horas do time e no ciclo? Depende do cliente aprovar? Quem segura a dependência é dono do risco.
- **Recurso compartilhado tem custo de oportunidade**: a hora de quem atende vários projetos é igual para todos.
- Todo PA nasce de FATO e CAUSAS e carrega indicador-chave e expectativa de ganho.

| Fato | Causa | PA | Dono e prazo | Indicador-chave | Expectativa de ganho (R$ ou KPI da frente) |
|---|---|---|---|---|---|

Onde não existe baseline, mostra-se só o alvo; placeholder de dado pendente não entra em material de treinamento nem de cliente.

## EXEMPLO NUMÉRICO FICTÍCIO

Frente inventada: TechFlow, SaaS B2B, mês a 77% do calendário (17 de 22 dias úteis). Plano do mês: 440 MQLs, 190 SQLs, 70 wins.

| Etapa | Plano pro-rata (77%) | Executado | Taxa planejada | Taxa executada |
|---|---|---|---|---|
| MQL | 339 | 318 (94% do ritmo) | | |
| MQL → SQL | | | 43% | 27% |
| SQL | 146 | 86 (59% do ritmo) | | |
| SQL → Won | | | 37% | 47% |
| Won | 54 | 40 (74% do ritmo) | | |

Percorrendo as sete checagens:

1. Integridade: critério de MQL igual ao do plano; tracking por canal conciliado com o CRM. Pode ler.
2. Pro-rata: tudo comparado a 77% do mês, não ao plano cheio.
3. Duas perguntas: volume de MQL em 94% do ritmo (não é o problema); taxa MQL → SQL 16 pontos abaixo do plano (é aqui que quebra). SQL → Won acima do plano compensa parte, mas os wins ficam em 74%.
4. Por canal: a queda de MQL → SQL é transversal (pago social menos 11 pontos, busca paga menos 32, orgânico menos 17); só o outbound segura (79%). Busca paga: 41 MQLs, 6 SQLs, zero wins.
5. Lag: os 40 wins carregam SQLs do mês anterior; a taxa SQL → Won acima do plano pode ser critério de SQL mais rígido, não time vendendo melhor.
6. Simulação: taxa MQL → SQL no plano com o volume atual dá 137 SQLs e cerca de 64 wins (92% do plano); volume no plano com a taxa atual dá 118 SQLs e cerca de 55 wins (79%). A taxa vale mais que o volume.
7. Filtro binário: queda transversal sugere tratamento (velocidade de contato, capacidade de SDR, critério de SQL); a busca paga com zero wins sugere atração (termo fora do ICP). Duas hipóteses, evidências diferentes. "Mais lead" e "trocar criativo" não entram.

Hipótese mais forte, inteira nos números: o outbound converte 79% em SQL e entregou metade do volume planejado; recompor a cadência ao plano dá cerca de +19 MQL → +15 SQL → +11 wins, perto de 28% sobre o mês. O ganho em R$ fecha com o ticket médio da frente.

## ALERTAS OPERACIONAIS

- Nunca apontar gargalo sem a checagem 1: taxa sobre dado contaminado é ruído com cara de insight.
- Nunca aceitar PA sem indicador, ganho, dono e prazo juntos; metade do PA não é PA.
- Nunca somar efeitos de três ações como se fossem independentes numa projeção.
- Nunca medir a taxa certa do canal errado: antes de cortar um canal, olhar em que etapa ele falha.
- Nunca deixar um teste sem decisão: matar ou sistematizar, registrado em `experimentos.md`.

## REFERÊNCIA RÁPIDA

**Melhor para**: análise de funil de qualquer frente, preparação e leitura de WBR, priorização de testes, revisão de plano de ação de time ou de agente.
**Ativar quando**: alguém diz "o problema é volume", "precisamos de mais lead", "vamos trocar o criativo" ou "a conversão caiu" sem ter passado pelas sete checagens; quando um PA chega sem ganho, dono e prazo; quando um teste termina sem decisão.
