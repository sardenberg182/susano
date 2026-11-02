---
id: ref-perf-licoes-de-conta
tipo: referencia
autor: Sarden
origem: lições de estrutura de conta da operação do Sarden (Meta, Google e transversais, mar a out/2026), só a regra; sem conta, campanha, cliente ou número de cliente
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Lições de conta: Meta, Google e o que vale para os dois

> Uso: regras que já custaram dinheiro em conta real, destiladas em "reconhece-se por" e "o que fazer". Abrir quando a auditoria de uma conta ou a leitura semanal do funil por canal encontrar um dos sinais abaixo. Complementa `rotina_gestor_performance.md` (a rotina) e `00_susano/dna/metodo/integridade_do_dado.md` (o sinal antes da leitura).

## META

- **Advantage+ amplo otimiza para o evento mais fácil, não para o mais qualificado.** Reconhece-se por: campanha de maior verba com a pior taxa de qualificação (lead → MQL de um dígito) e CPL "ótimo". O que fazer: segmentar por ICP e trocar o evento de otimização pelo mais próximo do dinheiro que o volume permitir.
- **Formulário nativo qualifica mais que LP com pixel em lead gen B2B.** Reconhece-se por: lead → MQL muito maior no instant form do que nas campanhas de LP, com a LP registrando bounce rápido como lead. A fricção do formulário dentro do Meta filtra curiosos. Antes de cortar a LP: validar a atribuição das campanhas de LP no CRM; zero absoluto costuma ser bug de tracking, não zero de verdade.
- **Conversa iniciada não é lead.** Campanha de WhatsApp com objetivo de conversa infla "resultado" e esconde o CPL efetivo (conversas ÷ leads que o CRM reconhece). Medir por lead no CRM, nunca por conversa.
- **Frequência acima de 3,0 em público aberto com objetivo de conversão sinaliza saturação.** Retarget com frequência acima de 5 em audiência pequena (abaixo de dez mil pessoas) está esgotado. O que fazer: renovar público antes de criativo.
- **CPL caindo com CAC subindo é compra de lead ruim.** Reconhece-se por: lead → MQL despencando no mesmo período em que o CPL melhora; canais ou fontes baratas respondendo pela maior parte dos leads com MQL residual. Volume sem valor destrói o CAC. O que fazer: custo por MQL e por SQL como métrica do canal; cortar a fonte, não o criativo.
- **Criativo com meses de uso e engajamento bem abaixo da média da conta é fadiga provável.** Default do método: cinco meses no ar e engajamento 35% abaixo da média pedem troca; calibrar por frente.
- **Duas BMs operando a mesma marca sem visibilidade cruzada canibalizam.** Sobreposição de audiência e leilão contra si mesmo. O que fazer: uma BM, ou exclusões cruzadas documentadas.
- **Page view como conversão primária treina o leilão para a métrica errada.** O algoritmo otimiza para o evento que você manda. Conversão primária é o evento mais próximo de receita que tiver volume estatístico.

## GOOGLE

- **Auditar a conta antes de desenhar.** Três erros que explicam "Google não funciona" sem o Google ter sido testado: campanha de Search gastando metade da verba em Display (rede de Display ligada por padrão); AI Max ou correspondência ampla em tudo; conversão primária em page view. Primeiro corrigir, depois concluir.
- **"Tiro de sniper" em fundo de funil.** Só Search, só intenção de compra, sem meta de volumetria: a campanha precisa de conversão, não de impressões. Gasto abaixo do teto é informação (a demanda é essa), não problema.
- **Negativação é diária, não semanal.** Em categoria com homônimo (uma sigla que também é órgão, profissão ou produto de outro setor), a lista de negativas é a primeira entrega e cresce todo dia.
- **Termos de pesquisa semanais promovidos a exata.** Exata em todo termo com evidência; frase só como pega-tudo de cauda; nunca ampla, AI Max ou inserção dinâmica (coloca marca de concorrente no anúncio).
- **Campanhas por tier de intenção, com verba isolada.** Decisão ou troca, comparativo e implementação: o tier de maior intenção nunca disputa verba com o resto; só nele se persegue topo absoluto (parcela de impressões acima de 60%); nos outros, o lance compra o clique pelo que vale.
- **O anúncio filtra antes do clique.** Qualificador de porte ou maturidade no título derruba CTR e sobe conversão. Marca de incumbente ou de concorrente entra como palavra-chave, nunca no texto.
- **Negativas além do homônimo:** informacional (o que é, tutorial, template, planilha), carreira (curso, vaga, salário), fora do ICP (grátis, autônomo, "pequenas empresas"), navegacional (login, app), direção contrária ("alternativa a", "cancelar"), integração (api, sincronizar), outro idioma.
- **Auction Insights por grupo desde a semana 1.** E o Planejador de palavras-chave alimentado com as URLs dos concorrentes devolve as palavras que o Google associa a cada página.
- **Validar RSA por script antes de subir** (títulos até 30 caracteres, descrições até 90).

## TRANSVERSAL

- **Google e Meta nunca se consolidam.** Intenção declarada contra interrupção; o funil por canal é a única leitura. Média dos dois esconde o canal que sangra. A eficiência costuma vir de pausar o que não funciona, não de escala.
- **Ativação faz parte do funil.** Em produto que exige ativação (conta, maquininha, app), venda sem ativação não é LTV; o CAC sustentável se calcula sobre o LTV ajustado pela taxa de ativação. A maioria das análises ignora isso.
- **CPM alto não é CPL alto.** Mercado com CPM três vezes maior pode ter CPL mediano igual, por conversão pós-clique maior e menos tráfego inválido. Benchmark de CPL agregado esconde a diferença entre instant form e LP; dataset internacional sobrerrepresenta e-commerce e anunciante global: referência, nunca meta.
- **Medir custo por MQL e por SQL, não CPL bruto.** Princípio da casa. CPL é diagnóstico; a decisão é no custo da etapa que vende.
- **Pixel acima do CRM é algoritmo otimizando no evento errado.** Duas a três vezes o CRM significa CPL reportado pela metade do real e escala sobre ruído. Correção: evento de lead só na submissão real, conciliação pixel × CRM antes de aumentar verba. Detalhe em `00_susano/dna/metodo/integridade_do_dado.md`.
- **Residual "orgânico" ou "not set" grande não é orgânico, é tracking quebrado.** Sem last click confiável, meta por canal é chute. Ritual mensal de reclassificação do residual com uma fonte só.
- **Monitoramento de conta é processo, não susto.** Conta restrita por método de pagamento com um único administrador de cobrança para a frente por dias: cada hora parada é dado que não se compra. Três camadas: detecção (status de conta via API ou queda súbita de gasto), notificação (responsável certo, automática), resolução (humana). Começar por uma plataforma. Problema de pagamento de cliente escala na hora para o dono da frente; quem lidera olha gerenciador e receita da própria frente ao menos uma ou duas vezes por semana, com os próprios olhos.
- **Dados para análise profunda de Meta Ads, em ordem de impacto:** quebra temporal por dia ou semana (a lacuna mais comum), métricas de eficiência (CTR, CPC, CPM, ROAS, valor), breakdowns de entrega (idade e gênero, plataforma, posicionamento, dispositivo, região), métricas de criativo e vídeo, configuração de público, eventos de funil. Um export lifetime sem granularidade temporal cobre menos de um quinto do que a análise pede: pedir todas as colunas, o maior período, os três níveis (campanha, conjunto, anúncio).

## REFERÊNCIA RÁPIDA

**Melhor para**: auditoria de conta antes de desenhar ou escalar; leitura semanal do funil por canal quando um sinal destes aparece; decisão de pausar, cortar fonte ou trocar criativo.
**Ativar quando**: CPL melhora e MQL piora; frequência sobe; pixel e CRM divergem; Search gasta em Display; "Google não funciona" sem auditoria; pedido de consolidar canais.
**Não usar para**: benchmark de custo (fica em `00_susano/referencias/benchmarks/panorama_2026.md`, com fonte) ou meta da frente (só do registro da frente).
