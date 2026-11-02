---
id: dna-dicionario
tipo: metodo
autor: Sarden
nivel: ATIVO
origem: definições de funil, RevOps e performance usadas na operação do Sarden (mar a out/2026); exemplos de critério genéricos
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Dicionário do método: sem definição não tem previsão

## TESE EM UMA LINHA

Nivelamento semântico antes de qualquer plano: todos com o mesmo dicionário de Lead, MQL, SQL, ICP e SLA, cada passagem de etapa com um dono e um lugar onde se mede; quando dois arquivos do método divergem numa definição, vale este.

## POR QUE UM DICIONÁRIO

A transição de etapa é onde o sistema quebra: é ali que a oportunidade muda de dono. Sem dicionário, marketing e vendas discutem opinião. Erro recorrente que precisa de correção explícita: inverter MQL e SQL em proposta ou em plano. E o decisor do cliente nem sempre sabe o que é SQL: o vocabulário do funil não é compartilhado com quem decide, então o documento define antes de usar.

## TERMOS

| Termo | Definição | Dono da passagem | Onde mede (genérico, no CRM) |
|---|---|---|---|
| Lead | Contato identificado que demonstrou interesse (formulário, conversa, cadastro). | Marketing | Objeto de lead ou contato; pipeline de inbound |
| MQL | Lead que atingiu o critério mínimo definido pelo modelo de negócio (não pelo marketing isolado). Qualifica no formulário, por pré-requisito de ICP: faturamento mínimo, perfil, porte, segmento. | Marketing, com critério aprovado pelo negócio | Propriedades de qualificação e data de MQL |
| SQL | MQL que atende critérios comerciais e foi aceito por vendas. Qualifica no SDR, por momento de compra e intenção ativa. | Vendas (SDR) | Etapa do pipeline e data de SQL |
| SAL | Pré-qualificado: lead aceito para abordagem antes da conversa de qualificação. | SDR | Etapa "pré-qualificado" do pipe de lead |
| Oportunidade | SQL com negócio aberto em negociação. | Vendas (closer) | Pipe de negócio |
| Won | Negócio ganho: contrato assinado ou pagamento confirmado, conforme a frente definir uma vez. | Vendas | Etapa de ganho; contagem única (ver `integridade_do_dado.md`, item 7) |
| ICP | Público em que faz mais sentido focar para maximizar rentabilidade: quem maximiza LTV, minimiza churn e sustenta pricing. Função de caixa, não persona. | Negócio | Faturamento, volume de compra, motivos de perda |
| SLA | Acordo formal entre áreas com dois lados: marketing entrega MQL no critério; vendas entrega velocidade de contato. | Ambos | Workflows, tarefas, tempo até a primeira ligação |
| CAC | Custo de aquisição de cliente: investimento total do canal ou da operação dividido pelos clientes ganhos no período. | Negócio | Pipeline (fonte da verdade), nunca a plataforma |
| CAC real | CAC ajustado pelo que de fato ativa ou permanece (ativação, retenção inicial). Quando metade dos clientes não ativa, o LTV real é metade do nominal e o CAC sustentável cai junto. | Negócio | CRM mais dado de produto |
| CPA | Custo por ação (evento definido), métrica de plataforma. Diagnóstico, não resultado. | Mídia | Plataforma |
| CPL | Custo por lead. Diagnóstico; o que decide é custo por MQL e por SQL. | Mídia | Plataforma conciliada com CRM |
| LTV | Valor que um cliente gera ao longo da vida, ajustado por ativação e retenção. | Negócio | Receita por cliente e churn |
| Payback | Meses para o LTV acumulado pagar o CAC. | Negócio | Derivado |
| Pro-rata | Meta ou plano proporcional ao calendário decorrido (dias úteis do mês). Toda comparação executado versus plano é pro-rata. | Análise | Planilha de taxas |
| Em linha | Realizado mais a projeção dos dias restantes (média diária dos últimos 14 dias; curva do ano anterior quando há evento no período). | Análise | Agenda de trabalho |
| Projeção final | Em linha mais o ganho esperado da agenda de ações. | Análise | Agenda de trabalho |
| Replan | Novo número documentado quando a projeção final fica abaixo da meta; não é ajuste de projeção, é decisão. | Dono da frente | `decisoes.md` |
| Strike | Mês consecutivo sem bater a meta; a partir do terceiro, observação formal e possível troca de liderança da frente. | Liderança | Metas da frente |

Vocabulário: ecossistema de canal se chama **parceiro**, nunca "associado".

## FUNIL PADRÃO

Impressão → Clique → Visita → Lead → MQL → SQL → Oportunidade → Won.

Cada transição tem uma taxa; o trabalho é saber onde cada canal quebra e agir na quebra certa. Funis diferentes se mapeiam para este padrão por de-para: um e-commerce lê Visita → Carrinho → Pedido como Lead → SQL → Won; um app lê Instalação → Cadastro → Ativação. O de-para fica registrado em `contexto.md` da frente e é obrigatório antes de qualquer meta.

## REGRA DE CONFLITO

Quando dois arquivos do método divergem numa definição (por exemplo, uma referência de performance que chama de "lead" o que aqui é MQL), vale este arquivo, e a divergência é marcada [CONTRADIÇÃO] no arquivo que diverge, com ponteiro para cá. Uma frente pode especializar uma definição (critério de MQL próprio), nunca contradizê-la.

## ALERTAS OPERACIONAIS

- Nunca aprovar meta antes de o dicionário estar aceito por marketing e vendas.
- Nunca aceitar "depende" como critério de passagem de etapa: exigir o corte exato.
- Nunca deixar MQL ser definido pelo marketing isolado; o critério é do modelo de negócio.
- Nunca inverter MQL e SQL em proposta; reler o documento com a tabela ao lado.

## REFERÊNCIA RÁPIDA

**Melhor para**: abertura de frente nova, estruturação de CRM, construção de plano e meta, proposta que menciona funil, treinamento de time.
**Ativar quando**: dois times usam a mesma palavra com significados diferentes; uma taxa parece incomparável com o plano; um documento mistura métricas de plataforma e de pipeline; alguém pergunta "o que conta como MQL aqui?".
