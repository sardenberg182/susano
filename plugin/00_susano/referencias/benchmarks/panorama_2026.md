---
id: ref-benchmarks-panorama-2026
tipo: referencia
origem: susano_benchmark_panorama_2026.md
atualizado: 2026-10-31
---

# SUSANO | BASE DE BENCHMARK E INSIGHTS: PANORAMA DE CONVERSAO 2026

<metadados>
- Arquivo: susano_benchmark_panorama_2026.md
- Tipo: contexto dinamico compartilhado (cross-client), atualizacao anual
- Fonte: Panorama PRO de Geracao de Leads 2026 (Leadster, com Reportei, Ramper e Staage)
- Base do estudo: 2.425 sites brasileiros, 173,6 milhoes de acessos, 3,4 milhoes de leads. Dados coletados ao longo de 2025 via chatbot de marketing conversacional da Leadster e publicados na edicao 2026.
- Vigencia: usar como referencia de mercado ate a publicacao do Panorama 2027
- Protocolo de troca anual: quando a edicao 2027 for processada, este arquivo e removido do Project e substituido por susano_benchmark_panorama_2027.md com a mesma estrutura de blocos. Nenhum outro arquivo depende deste por referencia cruzada.
</metadados>

<instrucoes_de_uso>
Como o Susano deve usar esta base ao analisar performance de clientes:

1. SEMPRE comparar em tres niveis, nesta ordem:
   a) Metrica do cliente vs mediana do canal (referencia de mercado)
   b) Metrica do cliente vs faixa do canal (baixa / media / alta performance)
   c) Metrica do cliente vs mediana do segmento do cliente naquele canal (quando o segmento existir na base)

2. Enquadramento por faixa (regua oficial do estudo):
   - Acima da faixa de alta performance: usar como confirmacao de forca; investigar escalabilidade
   - Entre media e alta: acima do mercado; otimizar incrementalmente
   - Entre baixa e media: abaixo do mercado; sinal de ajuste em criativo, oferta ou pagina
   - Abaixo da faixa de baixa performance: alerta estrutural; revisar estrategia do canal antes de otimizar taticamente

3. Ao citar benchmark em analise ou relatorio, SEMPRE nomear a fonte como "Panorama de Geracao de Leads 2026 (Leadster)" e indicar que a mediana e de mercado brasileiro, nao meta contratual.

4. NUNCA transformar mediana de mercado em meta de cliente sem ajuste de contexto (ticket, ciclo de venda, maturidade de midia, segmento). A mediana e ponto de comparacao, nao objetivo.

5. Se a metrica do cliente nao tiver benchmark correspondente nesta base (ex.: CPL, CAC, ROAS), declarar [DADO AUSENTE NA BASE DE BENCHMARK] e nao inferir valor. Este estudo cobre: taxa de conversao de visitante em lead, participacao de trafego, participacao de leads, qualificacao por leadscore, dispositivo e horario.

6. Conversao neste estudo = lead gerado / acesso ao site (mediana). Nao confundir com conversao de campanha em plataforma (que usa denominadores diferentes). Ao comparar com dados de Meta Ads ou Google Ads extraidos via MCP ou API, alinhar o denominador antes de comparar.

7. Dados do canal IA: tratar como direcionais. O proprio estudo marca amostras minimas (n=5 na matriz conversao x qualidade). Usar para narrativa de tendencia, nunca para meta ou projecao de cliente.
</instrucoes_de_uso>

<limitacoes_metodologicas>
[LIMITACAO METODOLOGICA] Medicao via chatbot Leadster instalado nos sites: a taxa de conversao reflete conversao assistida por marketing conversacional, tendendo a ser maior que a de sites que convertem so por formulario.
[LIMITACAO METODOLOGICA] Atribuicao last-click por canal de origem do acesso. Canais de topo de funil (LinkedIn, social organico) ficam subatribuidos. O proprio estudo discute isso no capitulo de LinkedIn.
[LIMITACAO METODOLOGICA] Leadscore (0 a 5) definido por cada empresa. "Qualificado" (faixa 4-5) nao e regua uniforme entre empresas nem entre segmentos.
[LIMITACAO METODOLOGICA] A fatia "outros" concentra 23,39% do trafego e 33,91% dos leads de 2026 sem abertura por canal. Percentuais por canal sao sobre o total incluindo essa fatia.
[LIMITACAO METODOLOGICA] Meta Ads contabiliza apenas trafego pago. Alcance organico de Instagram e Facebook nao entra na conta.
[LIMITACAO METODOLOGICA] Amostra 100% Brasil e enviesada para empresas que usam chatbot de conversao. Nao aplicar a operacoes internacionais sem ressalva.
[DADO AUSENTE] O estudo nao publica CPC, CPL, CAC ou valores de investimento em reais nesta edicao extraida. Nao usar esta base para benchmark de custo.
</limitacoes_metodologicas>

<benchmark_geral_canais>
## Regua oficial por canal (mediana de conversao, faixas de performance, 2026)

| Canal | Baixa perf. | Mediana (media perf.) | Alta perf. |
|---|---|---|---|
| IA | 5,54% | 7,80% | 13,52% |
| Meta Ads | 0,94% | 3,91% | 13,70% |
| Google Ads | 1,27% | 3,41% | 8,02% |
| Geral (todos os canais) | 1,02% | 3,07% | 7,90% |
| LinkedIn Ads | 0,15% | 2,97% | 18,30% |
| Busca organica | 0,81% | 2,39% | 6,03% |
| Acesso direto | 0,57% | 1,74% | 5,64% |

[DADO] Interpretacao central do estudo: a IA estreia como o canal de maior conversao (7,80%), o dobro da media geral. Entre canais consolidados, Meta Ads lidera (3,91%), seguido de Google Ads (3,41%).

## Serie historica de conversao (mediana, 2024 / 2025 / 2026)

| Canal | 2024 | 2025 | 2026 | Variacao 25-26 |
|---|---|---|---|---|
| IA | sem dado | sem dado | 7,80% | estreia |
| Meta Ads | 3,69% | 3,40% | 3,91% | +15,00% |
| Google Ads | 3,22% | 3,28% | 3,41% | +3,96% |
| Geral | 3,15% | 2,98% | 3,07% | +3,02% |
| LinkedIn Ads | 2,32% | 1,88% | 2,97% | +57,98% |
| Busca organica | 2,37% | 2,32% | 2,39% | +3,02% |
| Acesso direto | 2,39% | 2,08% | 1,74% | -16,35% |

[DADO] Serie longa da mediana geral desde 2022: 3,56% / 3,19% / 3,15% / 2,98% / 3,07%. Quatro anos de queda e reacao em 2026.
[INFERENCIA - apontada pelo proprio estudo] Parte da alta de 2026 e efeito de composicao: o trafego organico de baixa intencao (cauda longa absorvida pela IA) saiu do denominador. Nao significa necessariamente que cada empresa converte melhor. Ao analisar cliente, nao usar "o mercado subiu" como explicacao unica.

## Qualidade dos leads por canal (leadscore, distribuicao 0-1 / 2-3 / 4-5)

| Canal | Desqualificado (0-1) | Mediano (2-3) | Qualificado (4-5) |
|---|---|---|---|
| Busca organica | 28,8% | 26,7% | 44,5% |
| Geral | 27,7% | 29,4% | 42,9% |
| IA | 24,4% | 35,4% | 40,2% |
| Google Ads | 33,1% | 26,8% | 40,1% |
| Meta Ads | 27,0% | 33,3% | 39,7% |
| Acesso direto | 28,3% | 34,0% | 37,7% |
| LinkedIn Ads | 40,2% | 24,7% | 35,1% |

[DADO] O canal que mais converte (IA, Meta) nao e o que mais qualifica (organica). A IA tem a menor taxa de desqualificados do estudo (24,4%).
[ANOMALIA - apontada pelo estudo] Acesso direto com qualidade baixa contraria a expectativa (deveria ser trafego de marca). Explicacao dos especialistas: canal dificil de rastrear (links de WhatsApp, bio, login de plataforma contaminam a categoria).

## Distribuicao de trafego por canal (fatia dos acessos totais)

| Canal | 2024 | 2025 | 2026 | Volume 2026 |
|---|---|---|---|---|
| Busca organica | 42,70% | 33,86% | 27,91% | 48,5 mi |
| Google Ads | 25,20% | 27,48% | 23,40% | 40,6 mi |
| Acesso direto | 12,09% | 13,90% | 15,72% | sem abertura |
| Meta Ads | 5,11% | 6,50% | 9,48% | 16,5 mi |
| Outros | 14,82% | 18,24% | 23,39% | sem abertura |
| IA | sem dado | sem dado | 0,10% | 170,5 mil |
| LinkedIn Ads | 0,07% | 0,09% | 0,10% | 181,9 mil |

## Distribuicao de leads por canal (fatia dos leads totais)

| Canal | 2024 | 2025 | 2026 | Volume 2026 |
|---|---|---|---|---|
| Google Ads | 25,40% | 28,15% | 26,85% | 911,4 mil |
| Busca organica | 24,20% | 19,40% | 16,11% | 547,0 mil |
| Meta Ads | 10,50% | 13,75% | 15,83% | 537,5 mil |
| Acesso direto | 9,87% (aprox.) | 9% (aprox.) | 7,02% | sem abertura |
| Outros | 29,85% | 29,66% | 33,91% | sem abertura |
| IA | sem dado | 1,40% (aprox.) | 0,25% | 8.352 |
| LinkedIn Ads | 0,18% | 0,05% | 0,03% | 1.183 |

[VERIFICAR] Os valores de acesso direto e IA em 2024/2025 sairam com sobreposicao na extracao do grafico; os de 2026 e os volumes absolutos sao confiaveis.
[DADO] Leitura de eficiencia (leads acima do peso de trafego em 2026): Google 23,40% do trafego e 26,85% dos leads; Meta 9,48% e 15,83%; IA 0,10% e 0,25% (2,5x o proprio peso). Organica faz o inverso: 27,91% do trafego e 16,11% dos leads (assinatura de topo de funil).

## Dispositivo (2026)

| Canal | Acessos mobile | Leads mobile | Conversao desktop | Conversao mobile |
|---|---|---|---|---|
| Meta Ads | 91,84% | 98,42% | 4,07% | 4,07% |
| LinkedIn Ads | 89,59% | 64,58% | sem dado | sem dado |
| Google Ads | 83,18% | 72,32% | 4,30% | 3,17% |
| Busca organica | 66,15% | 50,12% | 2,42% | 2,51% |
| IA | 16,34% | 38,01% | 8,73% | sem dado |
| Geral | ~74% | sem dado | 3,50% | 3,37% |

[DADO] Tres viradas relevantes de 2026: (1) conversao mobile e desktop do Meta se igualaram em 4,07%; (2) organica converteu mais no mobile que no desktop pela primeira vez; (3) IA e o unico canal desktop-first (83,66% dos acessos no desktop, quase tudo ChatGPT no computador), mas o mobile da IA converte acima do proprio peso.

## Horario (leads fora do expediente: 18h-8h e fins de semana)

| Canal | Fora do horario comercial |
|---|---|
| IA | 47,98% |
| Busca organica | 47,76% |
| Acesso direto | 47,54% |
| Geral | 43,8% |
| Trafego pago (Meta + Google + LinkedIn + outros) | 42,69% |

[DADO] Quase metade do pipeline chega fora do expediente, liderado pelos canais de pesquisa ativa. Implicacao operacional padrao para diagnostico Susano: cliente sem atendimento ou automacao fora do horario esta perdendo a fatia de maior intencao.
[DADO - claim promocional Leadster, usar com ressalva] Responder em ate 5 minutos converte 10x mais que responder em 1 hora; responder em 1 hora da 7x mais chance de qualificar. Numeros citados no material sem fonte metodologica aberta.
</benchmark_geral_canais>

<benchmark_por_segmento>
## Tabela mestra: lider por segmento (volume de leads x conversao x qualidade)

Fonte primaria para "qual canal ganha no segmento X". Percentual de volume = fatia dos leads do segmento vinda do canal lider; conversao e qualidade = valor do canal lider.

| Segmento | Mais volume de leads | Maior conversao | Mais qualidade |
|---|---|---|---|
| Agencias | Google (27,4%) | Meta (6,7%) | Google (40,1%) |
| Consultorias | Meta (56,4%) | Google (2,7%) | Google (75,1%) |
| Educacional | Organico (45,5%) | Google (2,7%) | Google (75,5%) |
| Energia | Google (43,8%) | Google (6,6%) | Google (67,6%) |
| Financeiro | Google (24,5%) | Meta (6,4%) | Organico (68,0%) |
| Imoveis | Google (25,0%) | Direto (2,2%) | Meta (73,8%) |
| Industria e Fabricacao | Google (34,3%) | Meta (5,0%) | Direto (44,7%) |
| Juridico | Google (39,1%) | Meta (10,1%) | Meta (41,8%) |
| Logistica e Transporte | Google (40,3%) | Google (4,3%) | Google (23,9%) |
| Marketing e Publicidade | Google (48,2%) | Organico (3,3%) | Google (54,5%) |
| Seguros | Google (28,6%) | Direto (7,8%) | Meta (55,2%) |
| Servicos Medicos e Saude | Google (34,1%) | Google (4,8%) | Meta (57,4%) |
| Software | Google (34,5%) | Meta (4,3%) | Organico (38,0%) |
| Tecnologia e TI | Google (32,1%) | Meta (5,7%) | Organico (48,8%) |
| Telefonia e Internet | Google (30,9%) | Google (2,8%) | Google (67,4%) |
| Venda de Produtos | Google (29,7%) | Google (2,4%) | Meta (45,4%) |
| Venda de Servicos | Google (26,6%) | Meta (4,5%) | Meta (51,4%) |

[DADO] Sintese: Google lidera volume em 15 de 17 segmentos (excecoes: Educacional para organico, Consultorias para Meta). Onde o Meta supera o Google em conversao, quase sempre e segmento B2B.
[CONTRADICAO] Os cards-resumo de cada canal citam contagens ligeiramente diferentes desta tabela (ex.: card do Meta diz lider de conversao em 9/17 segmentos; a tabela mestra soma 7; card do Google diz qualidade em 6/17; a tabela soma 7). Em analise, usar a tabela mestra como fonte primaria e ignorar as contagens dos cards.

## Google Ads por segmento

Conversao (mediana). Faixa do canal: 1,49% a 6,63%; mediana 3,41%.

| Segmento | Conversao | Segmento | Conversao |
|---|---|---|---|
| Imoveis | 1,49% | Agencia | 3,54% |
| Marketing | 2,19% | Industria | 3,61% |
| Software | 2,31% | Venda de Servicos | 4,05% |
| Venda de Produtos | 2,40% | Logistica | 4,30% |
| Tecnologia | 2,52% | Saude | 4,84% |
| Financeiro | 2,69% | Juridico | 5,32% |
| Consultoria | 2,72% | Seguros | 5,93% |
| Educacional | 2,72% | Energia | 6,63% |
| Telefonia | 2,75% | GERAL | 3,41% |

[DADO] Padrao apontado pelo estudo: ticket alto e jornada tecnica (Energia, Seguros, Juridico) convertem acima da media no Google; jornada longa e comparativa (Imoveis, Software) ficam abaixo.

Qualificacao (% de leads 4-5). Faixa: 19,53% a 75,55%; mediana 40,08%.

| Segmento | Qualif. | Segmento | Qualif. |
|---|---|---|---|
| Seguros | 19,53% | Financeiro | 40,85% |
| Logistica | 23,89% | Venda de Servicos | 40,89% |
| Tecnologia | 30,92% | Imoveis | 41,60% |
| Venda de Produtos | 35,13% | Marketing | 54,51% |
| Industria | 36,40% | Saude | 56,75% |
| Juridico | 37,10% | Telefonia | 67,40% |
| Software | 37,91% | Energia | 67,55% |
| GERAL | 40,08% | Consultoria | 75,10% |
| Agencia | 40,09% | Educacional | 75,55% |

[DADO] Contraste-chave para diagnostico: Seguros esta entre os que mais convertem no Google (5,93%) e e o que menos qualifica (19,53%). Converter bem nao e trazer o lead certo.

Participacao no trafego do segmento (Google Ads): Marketing 47,76% | Financeiro 43,97% | Logistica 43,79% | Industria 41,42% | Agencia 41,01% | Juridico 40,30% | Telefonia 36,84% | Venda de Servicos 34,92% | Venda de Produtos 34,09% | Saude 31,64% | Tecnologia 31,33% | Energia 31,03% | Software 27,84% | Imoveis 27,22% | GERAL 23,40% | Seguros 17,07% | Consultoria 11,15% | Educacional 10,10%.

Participacao nos leads do segmento (Google Ads): ancoras confirmadas: Marketing 48,18% | Energia 43,85% | GERAL 26,85% | Consultoria 12,36% | Educacional 8,83%. Demais segmentos entre 24,46% e 40,32%. [VERIFICAR] Pareamento fino dos intermediarios nao validado na extracao; usar as ancoras e a tabela mestra para afirmacoes por segmento.

Trajetoria: trafego 25,20% (2024) -> 27,48% (2025) -> 23,40% (2026); leads 25,40% -> 28,15% -> 26,85%. Perde trafego, ganha eficiencia. Conversao desktop caiu de 4,95% para 4,30%; mobile subiu de 3,03% para 3,17% (menor folga da serie).

Card oficial de uso (Google): usar quando precisa de volume previsivel, ha demanda ativa buscando o produto, fundo de funil. Pensar duas vezes: categoria nova sem busca, orcamento curto que exige CPC baixo, objetivo de criar demanda em vez de captura-la.

## Meta Ads por segmento

Conversao (mediana). 15 segmentos com dado; mediana do canal 3,91%.

| Segmento | Conversao | Segmento | Conversao |
|---|---|---|---|
| Consultoria | 1,23% | Venda de Servicos | 4,54% |
| Imoveis | 1,60% | Industria | 4,97% |
| Venda de Produtos | 1,77% | Tecnologia | 5,71% |
| Educacional | 2,21% | Financeiro | 6,39% |
| Marketing | 3,26% | Agencia | 6,65% |
| GERAL | 3,91% | Seguros | 6,84% |
| Saude | 4,25% | Juridico | 10,12% |
| Software | 4,27% | | |

[LACUNA] Energia, Logistica e Telefonia sem dado de conversao Meta nesta edicao.

Qualificacao (% de leads 4-5). Faixa: 10,00% a 87,97%; mediana 39,72%.

| Segmento | Qualif. | Segmento | Qualif. |
|---|---|---|---|
| Marketing | 10,00% | Venda de Servicos | 51,41% |
| Industria | 15,61% | Financeiro | 52,57% |
| Agencia | 22,77% | Seguros | 55,22% |
| Tecnologia | 23,61% | Saude | 57,35% |
| Software | 24,05% | Educacional | 57,54% |
| GERAL | 39,72% | Consultoria | 61,29% |
| Juridico | 41,79% | Imoveis | 73,75% |
| Telefonia | 44,74% | Energia | 87,97% |
| Venda de Produtos | 45,36% | | |

[DADO] Ponto cego do Meta apontado pelo estudo: os segmentos onde ele mais converte (Software, Tecnologia, Agencia, Marketing) estao entre os que menos qualificam no canal.

Participacao no trafego do segmento (Meta Ads): ancoras: Marketing 26,59% | Financeiro 16,87% | Venda de Servicos 12,49% | Venda de Produtos 12,18% | GERAL 9,48% | pisos: Energia 3,49% e Logistica 2,87%. Meta nao lidera trafego em nenhum segmento.

Participacao nos leads do segmento (Meta Ads): ancoras: Consultoria 56,39% (unico segmento onde o Meta e o canal numero 1 em leads) | Venda de Servicos 23,79% | Software 21,78% | Financeiro 19,94% | Tecnologia 18,48% | GERAL 15,83% | pisos: Educacional 1,44% e Energia 2,18%.

Trajetoria: trafego 5,11% (2024) -> 6,50% (2025) -> 9,48% (2026), mais que dobrou; leads 10,50% -> 13,75% -> 15,83%. Alerta 2026: trafego cresceu 52% no ano e leads apenas 5%; a folga leads/trafego caiu de 2x para 1,67x. Meta e canal quase 100% mobile (98,42% dos leads).

[DADO] Motores do amadurecimento do Meta segundo o estudo: APIs de conversao (CAPI, evento server-side devolvendo o dado que o pixel perdeu com iOS e cookies) e IA de campanha (Advantage+ e publicos amplos, segmentacao no algoritmo). Consequencia operacional: a alavanca controlavel do anunciante migrou para o criativo. Enviar evento de lead qualificado (nao lead bruto) de volta para a plataforma redireciona o algoritmo para o ICP.

Card oficial de uso (Meta): usar quando quer alcancar quem ainda nao busca, alimentar topo e meio de funil, e a experiencia mobile esta pronta. Pensar duas vezes: decisor de nicho dificil de segmentar, time sem capacidade de produzir criativo, atendimento restrito ao horario comercial.

## Busca organica por segmento

Conversao (mediana). Faixa: 0,65% a 3,64%; mediana 2,39%.

| Segmento | Conversao | Segmento | Conversao |
|---|---|---|---|
| Consultoria | 0,65% | Educacional | 2,49% |
| Imoveis | 1,16% | Saude | 2,54% |
| Logistica | 1,50% | Industria | 2,76% |
| Software | 1,50% | Financeiro | 3,16% |
| Telefonia | 1,74% | Venda de Servicos | 3,20% |
| Juridico | 1,87% | Marketing | 3,30% |
| Venda de Produtos | 2,12% | Seguros | 3,34% |
| Tecnologia | 2,37% | Agencia | 3,64% |
| GERAL | 2,39% | | |

[DADO] Marketing e o unico segmento em que a organica lidera a conversao entre todos os canais.
[DADO - vies analitico apontado pelo estudo] Consultoria, software, agencia e educacional produzem muito conteudo e indexam cauda longa; conversao organica baixa nesses segmentos nao significa site pior, significa mix de trafego informacional.

Qualificacao (% de leads 4-5). Faixa: 14,59% a 68,03%; mediana 44,51% (a maior entre todos os canais).

| Segmento | Qualif. | Segmento | Qualif. |
|---|---|---|---|
| Logistica | 14,59% | Geral | 44,51% |
| Marketing | 16,12% | Telefonia | 46,54% |
| Agencia | 18,48% | Tecnologia | 48,80% |
| Imoveis | 29,35% | Saude | 49,18% |
| Juridico | 30,05% | Energia | 59,06% |
| Venda de Produtos | 35,57% | Educacional | 61,63% |
| Software | 37,97% | Consultoria | 64,99% |
| Industria | 40,30% | Financeiro | 68,03% |
| Seguros | 41,29% | | |
| Venda de Servicos | 43,62% | | |

Participacao no trafego do segmento (organica): topo: Educacional 55,70% | Consultoria 49,65% | Saude 37,70% | Juridico 33,47% [VERIFICAR pareamento do 33,47] | GERAL 27,91% | pisos: Financeiro 10,01% | Marketing 8,49% | Seguros 8,15%.

Participacao nos leads do segmento (organica): topo: Educacional 45,46% (o dobro do segundo colocado) | Logistica 24,16% | GERAL 16,11% | pisos: Juridico 8,03% | Seguros 6,95% | Agencia 5,49%.

Trajetoria: trafego 42,70% (2024) -> 33,86% (2025) -> 27,91% (2026), queda de quase 15 pontos e de 62,9 mi para 48,5 mi de acessos; leads cairam bem menos (24,20% -> 16,11%, 842 mil -> 547 mil). Conversao estavel ha tres anos (2,37 / 2,32 / 2,39). Leitura oficial: evaporou a cauda longa informacional que a IA absorveu; o que ficou e trafego de marca e intencao, com o lead mais qualificado do estudo.

Card oficial de uso (organica): usar quando o segmento ainda e dominado por organica (educacao, saude, juridico), ja existe investimento em marca e conteudo, e a empresa aceita abandonar metrica de trafego. Pensar duas vezes: necessidade de volume rapido e previsivel, dependencia de SEO de "como fazer" (absorvido pela IA), categoria nova sem demanda estabelecida.

## LinkedIn Ads por segmento

[DADO] Menor canal pago do estudo: 0,10% do trafego (181,9 mil acessos) e 0,03% dos leads (1.183). Acessos sobem tres anos seguidos (107,7 mil -> 144,5 mil -> 181,9 mil); leads atribuidos caem na mesma janela (6.194 -> 1.717 -> 1.183).
[LIMITACAO METODOLOGICA] Last-click pune o LinkedIn: o estudo argumenta que o canal trabalha antes do clique final. Nao diagnosticar "LinkedIn nao entrega" para cliente B2B usando so esta base.

Qualificacao: mediana 35,13% (ultima entre os canais). Apenas 3 segmentos com dado: Financeiro 65,35% | Venda de Servicos 35,53% | Software 29,38%. [LACUNA] Demais segmentos sem amostra.

Trafego por segmento (ancoras): Logistica 0,52% | Financeiro 0,46% | Marketing 0,40% | Telefonia 0,31% | demais entre 0,01% e 0,24%. Leads por segmento (ancora): Software 0,17%, distante dos demais (0,01% a 0,05%).

Dispositivo: acesso 89,59% mobile; leads viraram mobile pela primeira vez em 2026 (64,58%).

Card oficial de uso (LinkedIn): usar para B2B de ticket alto e ciclo longo, segmentacao por cargo/empresa/setor, ABM. Pensar duas vezes: ticket baixo (a conta nao fecha), orcamento curto, sucesso medido por volume de leads.

## IA (novo canal) por segmento

[DADO] Estreia no Panorama: 0,10% do trafego (170,5 mil acessos), 0,25% dos leads (8.352), conversao mediana 7,80% (a maior do estudo), 2,5x acima do proprio peso de trafego. 78,36% dos acessos de IA vem do ChatGPT (Perplexity 8,42%, Gemini 5,87%, Copilot 3,77%, demais abaixo de 2%).
[LIMITACAO METODOLOGICA] Volume minimo. A matriz conversao x qualidade do estudo marca n=5 para IA, com rotulo "direcional". Nunca usar valores de IA como meta de cliente.

Qualificacao por segmento (% de leads 4-5; mediana do canal 40,22%): Agencia 15,12% | Imoveis 35,16% | Software 35,22% | Marketing 36,11% | Saude 38,71% | Industria 38,94% | Juridico 39,33% | Venda de Produtos 39,66% | GERAL 40,22% | Tecnologia 45,00% | Financeiro 48,23% | Venda de Servicos 52,46% | Seguros 53,57% | Consultoria 59,21% | Educacional 60,42%.

Trafego de IA por segmento (% dos acessos do segmento): topo: Energia 0,30% | Agencia 0,28% | Software 0,24% | Consultoria 0,24% | Tecnologia 0,22% | media 0,10% | pisos: Telefonia/Seguros/Marketing 0,06% | Financeiro 0,03%.

Leads de IA por segmento (% dos leads do segmento): topo: Energia 0,70% | Consultoria 0,48% | Industria 0,39% | Software e Tecnologia 0,37% | media 0,25% | pisos: Juridico 0,11% | Marketing 0,10% | Financeiro 0,07%.

Dispositivo: unico canal desktop-first (83,66% dos acessos no desktop; ChatGPT no computador), mas mobile entrega 38,01% dos leads com 16,34% dos acessos. Horario: canal mais always-on do estudo (47,98% dos leads fora do expediente).

Card oficial de uso (IA): usar para construir citacao e autoridade, lead de alta intencao que chega decidido, venda tecnica ou consultiva. Pensar duas vezes: necessidade de volume rapido, dependencia de atribuicao limpa, setor com baixa presenca em IA.

## Acesso direto

[DADO] 15,72% do trafego e 7,02% dos leads em 2026. Conversao mediana 1,74%, unico canal em queda (2,39% -> 2,08% -> 1,74%). Qualificados 37,7%.
[ANOMALIA] Qualidade abaixo do esperado para canal de marca; categoria contaminada por links nao rastreados (WhatsApp, bio, login). Ao analisar cliente, tratar acesso direto como proxy imperfeito de marca e checar instrumentacao de UTM antes de concluir.
</benchmark_por_segmento>

<insights_estrategicos_2026>
Sinteses qualitativas do estudo e dos especialistas convidados (Leadster, Ramper, Reportei, Staage), parafraseadas. Usar como camada de narrativa em analises, sempre com atribuicao "segundo o Panorama 2026", nunca como dado do cliente.

1. TESE CENTRAL DO ANO: a hierarquia de canais que valeu por anos comecou a se mover. A IA estreia convertendo o dobro da media, o organico troca volume por qualidade, o Meta amadurece como canal de performance e o Google segue lider de volume mas perde participacao.

2. IA COMO CANAL: a funcao da IA nao e mandar trafego, e responder na conversa; o pouco trafego que ela devolve chega decidido. O canal esta gratuito e aberto hoje, e a expectativa dos especialistas e que vire midia paga e cara quando consolidar. Construir presenca em recomendacao de IA agora (o que o mercado chama de GEO: ser a fonte citada pelo modelo) e aposta de custo baixo com janela de tempo.

3. ORGANICA: a queda de trafego e real (15 pontos em dois anos), mas concentrada em cauda longa informacional que nao convertia. Estrategia de conteudo recomendada: migrar de "como fazer" (absorvido pela IA) para conteudo de dado proprietario e autoridade citavel; a regua de autoridade virou citacao pelos modelos. Marca, presenca do founder e canais relacionais ganham peso.

4. META: dois motores explicam a maturidade: CAPI (evento de conversao server-side recuperando sinal perdido por iOS e cookies) e IA de campanha (Advantage+, publicos amplos). A variavel que o anunciante controla de fato virou o criativo. Pratica recomendada: devolver para a plataforma o evento de lead QUALIFICADO, nao de lead bruto, para o algoritmo otimizar contra o ICP.

5. GOOGLE: perde participacao mas segue dominando mais de 50% do trafego de quase qualquer empresa com site (somando pago e organico, lidera trafego em 16 de 17 segmentos). Leitura de demanda importa: segmentos com categoria estabelecida e keyword expressa rendem no Google; demanda nao verbalizada rende no Meta. Alerta de especialista: 3,41% e baixo para canal de intencao; landing page fraca desperdicando trafego bom e hipotese diagnostica frequente.

6. LINKEDIN: paradoxo de atribuicao. Acessos sobem, leads last-click despencam, mas o canal trabalha topo e meio de funil em B2B de ciclo longo (jornadas de ate 24 meses citadas). Empresas que mais investem tendem a ter reguas de qualificacao mais duras, o que rebaixa o leadscore do canal. Diagnostico justo exige visao multi-touch.

7. JORNADA MOBILE E FORA DO EXPEDIENTE: a jornada saiu do horario comercial (43,8% dos leads fora do expediente, com pico citado de 18h-22h em B2B para empresarios) e do desktop (74% dos acessos mobile). Implicacoes de diagnostico: atendimento/qualificacao 24h (SDR de plantao, IA de atendimento) e experiencia mobile do site sao alavancas antes de escalar midia. Nao desligar campanha a noite sem teste: leilao mais barato quando concorrentes desligam.

8. LEADSCORE E ICP: "qualificado" e regua interna de cada empresa. ICP largo infla a taxa de qualificacao sem melhorar qualidade real; regua apertada seca pipeline. Em diagnostico Susano, checar a definicao de leadscore do cliente antes de comparar com as medianas deste arquivo.
</insights_estrategicos_2026>

<protocolo_de_analise_susano>
Ao produzir analise de performance usando esta base, o Susano segue este formato de citacao:

1. Declarar o dado do cliente com fonte e periodo.
2. Declarar o benchmark com fonte fixa: "mediana de mercado (Panorama Leadster 2026)".
3. Classificar na regua de faixas do canal (baixa / media / alta performance).
4. Se houver benchmark do segmento do cliente, refinar a comparacao no nivel segmento x canal.
5. Aplicar os marcadores padrao Susano quando couber: [DADO], [INFERENCIA], [CONTRADICAO], [LACUNA], [ANOMALIA], [VERIFICAR], [DADO AUSENTE], [LIMITACAO METODOLOGICA].
6. Fechar com leitura acionavel: o que o desvio vs benchmark sugere testar primeiro.

Exemplo de frase-padrao:
"[DADO] A conversao de Meta Ads do cliente em junho foi 2,1% (fonte: Meta MCP). Contra a mediana de mercado de 3,91% (Panorama Leadster 2026), o cliente opera entre a faixa de baixa (0,94%) e media performance, no terco inferior do mercado. No segmento Juridico, a referencia sobe para 10,12%, ampliando o gap. [INFERENCIA] O padrao e compativel com criativo ou oferta desalinhados do ICP; prioridade de teste: criativo e evento de qualificacao via CAPI."

Regras rigidas:
- Nao converter benchmark em meta sem contexto do cliente.
- Nao usar dados de IA (canal) para metas ou projecoes.
- Nao usar esta base para benchmark de custo (CPC/CPL/CAC): [DADO AUSENTE].
- Ao detectar que o denominador do cliente difere do estudo (conversao de campanha vs conversao de site), normalizar ou declarar a diferenca.
- Se o segmento do cliente nao mapear em nenhum dos 17 segmentos do estudo, usar apenas a regua geral do canal e declarar [LACUNA] de segmento.
</protocolo_de_analise_susano>

## NOTAS DA MIGRAÇÃO (2026-10-31)

- Troca anual: substituir quando sair a edição seguinte.
- [LACUNA] Sem benchmark de custo de mídia paga (CPC, CPL, CAC): o próprio estudo declara.
