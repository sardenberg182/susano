---
id: dna-integridade-do-dado
tipo: metodo
autor: Sarden
nivel: ATIVO
origem: lições de tracking, atribuição e contagem da operação do Sarden (mar a out/2026), destiladas em regra; exemplos fictícios
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Integridade do dado: sinal contaminado invalida qualquer taxa

## TESE EM UMA LINHA

Antes de ler ROAS, CPL, taxa de conversão ou CAC, conferir se o sinal é íntegro: pixel acima do CRM, "direto" alto demais, negócio duplicado ou critério que mudou no meio da série derrubam a conclusão inteira, por mais bonito que o número pareça.

## MODELOS ATIVOS

- **Checklist de sinal contaminado**: nove sintomas que obrigam a parar antes de ler (seção abaixo). Um só basta.
- **Parar, conciliar, registrar, ler**: a ordem quando o sinal falha. Conciliar fonte com fonte, registrar [CONTRADIÇÃO] com os dois números e as duas fontes, só então ler o que sobrou.
- **Regra dos 60 dias**: quando o histórico não é confiável, os primeiros 60 dias são fundação (tracking, definições, contagem); qualquer KPI prometido antes disso é especulação.
- **Conversão é envio confirmado, nunca clique**: evento de lead no pixel e no CAPI com deduplicação; o lead cai no CRM com origem, campanha e etapa.

## CHECKLIST DE SINAL CONTAMINADO

Qualquer item abaixo invalida a leitura até ser conciliado:

1. **Pixel acima do CRM.** Plataforma reporta o dobro de leads do que o CRM recebeu: o algoritmo está otimizando no evento errado e o CPL reportado é a metade do real. Exemplo fictício: 130 leads no pixel, 62 no CRM; o CPL "de R$ 20" é R$ 42.
2. **"Not Set", "direto" ou "orgânico" alto demais para ser orgânico.** Um terço da receita sem origem não é orgânico, é tracking quebrado. Sem last click confiável, meta por canal é chute e variável por canal não é mensurável.
3. **Negócio duplicado inflando taxa.** Bug de duplicação dobra o denominador de uma etapa e produz conversão de 60% ou mais onde o real é a metade.
4. **UTM quebrada ou ausente.** Tráfego direto absorve conversão quando a UTM falha; a campanha "não converte" porque a conversão foi contada em outro lugar.
5. **Dado de outra frente colado no documento.** Tabela de previsão idêntica em dois projetos é dado colado, não coincidência. Ler sempre com ceticismo de origem.
6. **First click e last click tratados como comparáveis.** O first click do CRM e o last click das plataformas contam histórias diferentes; nunca consolidar como se fossem a mesma métrica.
7. **Dois jeitos de contar cliente.** Filtrar por "negócio ganho" e contar entradas na etapa de ganho dão números diferentes; a diferença muda um case. Cruzar sempre com a lógica do relatório que a frente já usa.
8. **Critério de MQL que mudou no meio da série.** Taxa comparada a um plano feito no critério antigo é incomparável; a série recomeça na data da mudança.
9. **Campo novo no formulário derrubando a conversão da página.** Antes de tratar como bug ou como "LP ruim", isolar o atrito do campo; se for o campo, o que decide é o custo por proposta, não o CPL.

## O QUE FAZER

1. **Parar.** Nenhuma conclusão sai enquanto um item da lista estiver aberto.
2. **Conciliar fonte com fonte.** Pixel contra CRM, plataforma contra pipeline, relatório contra contagem direta; período, fuso e denominador iguais.
3. **Registrar [CONTRADIÇÃO]** com os dois números e as duas fontes, na frente (ledger ou análise). Nada se resolve em silêncio.
4. **Corrigir o sinal**: evento de lead igual a submissão real; Pixel e CAPI com deduplicação; Enhanced Conversions; UTM no destino; lead no CRM com origem, campanha e etapa.
5. **Só então ler**, e dizer no output o que foi conciliado e o que ficou fora.

## REGRA DOS 60 DIAS

Quando o histórico não é confiável, os primeiros 60 dias de uma operação são de fundação: tracking ponta a ponta, dicionário de funil, contagem única, atribuição com herança no CRM. Qualquer KPI prometido antes disso é especulação, e a proposta deve prometer instrumentação e método, não resultado. A "fotografia inicial" do funil na semana zero é o pré-requisito de qualquer variável atribuível.

## RITUAL DE LIMPEZA DO RESIDUAL

Em e-commerce e em qualquer operação com receita sem origem: ritual mensal de reclassificação do residual, nota a nota (UTM e cupom), com uma fonte só de receita definida no cabeçalho e os canais mapeados. O percentual de "sem origem" é um indicador da frente, com meta de queda.

## ALERTAS OPERACIONAIS

- Nunca aprovar verba, escala ou troca de criativo sobre sinal não conciliado.
- Nunca chamar de orgânico o que é "sem origem".
- Nunca consolidar pixel e CRM, nem first click e last click, numa única linha de resultado.
- Nunca prometer KPI antes da fundação quando o histórico é sujo.
- Nunca reler uma série inteira depois de mudança de critério como se fosse uma só.

## REFERÊNCIA RÁPIDA

**Melhor para**: abertura de qualquer análise de mídia, funil ou receita; auditoria de conta; primeira semana de uma frente nova; proposta para cliente com histórico duvidoso.
**Ativar quando**: um número parece bom demais; pixel e CRM divergem; "direto" ou "not set" aparecem com peso relevante; a conversão de uma etapa muda de patamar sem mudança operacional; alguém pede escala ou corte de canal.
