---
id: instr-landing-pages
tipo: instrucao
autor: Sarden
carrega_em: sob demanda (skill susano-performance)
origem: lente de landing page do Sarden e playbook do agente construtor de LP em HTML (v3.0, 16/10/2026), mais os erros vistos em projeto (mar a out/2026); sem cliente, sem número de cliente
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Landing pages: a lente, a ficha e o QA antes do tráfego

Esta instrução é a lente: o que uma página precisa ser para o Sarden aprovar e o que o Susano confere antes de qualquer clique pago. O passo a passo de construção (HTML, formulário, tracking, thank-you, detector, revisão de acabamento e pacote de entrega) vive em `00_susano/referencias/landing_pages/playbook_construtor_html.md`; abra só quando a tarefa for construir ou revisar o código.

## A LENTE

1. **Toda página tem um único objetivo de conversão.** Nunca informacional. Se a conversão não cabe em uma linha, a página ainda não existe. Informar é meio.
2. **Três leitores, nesta ordem.** O apressado converte na hero: a página casa com o anúncio, o CTA e um campo único aparecem sem rolar. O que precisa de confirmação lê o corpo e faz 2 a 3 perguntas antes de clicar. O que precisa ser convencido chega com a objeção principal; o corpo serve os leitores 2 e 3 nessa ordem, confirmação antes de convencimento.
3. **O CTA existe para disparar o objetivo e fica sempre à mostra.** Barra fixa no mobile, header ou repetição no desktop. Um CTA, o mesmo texto do topo ao rodapé, em primeira pessoa e com o deliverable ("Quero meu diagnóstico"). Toda seção conecta ao CTA ou sai da página.
4. **Dispositivo e canal são pré-requisito decidido por protocolo**, não por categoria. Peso nesta ordem: jornada da campanha → modelo de negócio e histórico da frente → benchmark. B2B ou B2C não decide nada: há negócio B2B com a maioria do tráfego de LP no celular. Dispositivo se mede por frente, com data e fonte.
5. **LP é a terceira variável do funil, não a primeira.** Estrutura não compensa oferta fraca nem pré-frame desalinhado com a fonte de tráfego. Antes de mexer na página, confirme oferta e anúncio (`00_susano/biblioteca/brunson/dotcom_secrets.md`, pré-frame e temperatura).

## FICHA DE DEFINIÇÃO (17 campos; sem ficha, não há página)

1. Conversão única: esta página existe para ___ (uma linha).
2. Tipo de conversão: final (lead, agendamento, compra, trial, inscrição) ou de etapa (clique para a próxima página, avanço de step). Multi-step: a conversão única de cada step.
3. Evento medido: envio confirmado, conversa iniciada no WhatsApp, agendamento, compra. Nunca clique no botão.
4. Canal e jornada de entrada: de onde vem o clique e em que tela abre. Canal mobile por natureza (WhatsApp, SMS, Meta, Stories) fecha a decisão de dispositivo aqui.
5. Direção de dispositivo da v1: mobile ou desktop, com a origem da decisão (canal, histórico ou benchmark) e a data da primeira revisão com dado real.
6. Temperatura do tráfego: quente, morna ou fria.
7. Leitor 1 (hero): o que ele precisa ver em 3 segundos para clicar.
8. Leitor 2 (confirmação): as 2 a 3 perguntas que ele faz antes de clicar.
9. Leitor 3 (convencimento): objeção principal e secundárias.
10. CTA: texto em primeira pessoa com o deliverable, posições (hero, meio, final), visibilidade (barra fixa no mobile, header no desktop).
11. Pós-conversão: o que acontece nos 5 minutos seguintes (thank-you com SLA, próximo degrau).
12. Tracking: evento, UTM, pixel e CAPI, campo de origem no CRM.
13. Destino de publicação e URL final.
14. Mecanismo de envio do formulário (ou caminho WhatsApp) e nomes dos campos no CRM.
15. Autoridade visual: design system recebido (fonte, data) / mundo coerente no site atual (URL) / marca incompleta (o que está confirmado) / sem autoridade visual (rodada de direção obrigatória).
16. Indexação: sim ou não.
17. Cena de uso (uma frase: quem abre, onde, em que luz, em que estado de espírito) e claro ou escuro decidido por ela.

Campo vazio ou em dúvida vira pergunta antes de escrever; a ficha não avança com suposição. O dado da frente (prova, número, prazo, preço, SLA, nome) entra com quem confirmou e quando.

## PROTOCOLO DE DISPOSITIVO (ordem de peso)

1. **Canal e jornada da campanha.** Jornada mobile por natureza = página mobile. Fim da decisão.
2. **Modelo de negócio e histórico da frente.** Canal misto (Search, e-mail, orgânico, LinkedIn) = o dispositivo vem do público e do histórico (GA4 fonte/mídia × dispositivo, cliques por dispositivo da ferramenta de e-mail, campanhas anteriores), registrado com data e fonte. B2B ou B2C não decide.
3. **Benchmark de mercado.** Direção de largada quando não há histórico, com fonte e ano. Projetar a v1 pelo benchmark é aceitável; usar benchmark como decisão final não é.

A v1 é sempre meio-termo: funciona por completo nos dois dispositivos, com hierarquia visual e formulário otimizados para o lado da decisão, e com data marcada para a análise de realidade. No código isso vira CSS mobile-first em todos os casos; a direção decide posição do formulário e composição da primeira dobra.

## ERROS QUE JÁ APARECERAM EM PROJETO

- Ler a conversão da LP sem olhar a qualidade no CRM: o mês de menor CPL foi o de pior passagem MQL → SQL. Taxa da página e qualidade do lead se leem juntas, sempre.
- Conversão disparada no clique e não no envio confirmado: o pixel contou mais que o dobro do CRM.
- Campo a mais no formulário sem medir o custo por proposta. Campo é o mínimo para rotear; qualificar é trabalho do multi-step ou do CRM.
- Navegação e links de saída em LP de tráfego pago. A maioria das páginas de mercado ainda carrega menu; [VERIFICAR] fonte e ano antes de citar o número.
- Decidir dispositivo por categoria (B2B = desktop) em vez de canal, histórico e benchmark.
- Testar cor de botão antes de headline e formulário.
- WhatsApp sem bot e sem CRM; thank-you vazia (precisa de SLA, próximo passo e tracking).
- Jargão e nível de leitura profissional; frases acima de 20 palavras. Copy em nível de leitura simples converte mais; a fonte e o ano estão no Anexo E do playbook.

## QA PRÉ-TRÁFEGO (sete blocos; página sem os sete não recebe clique pago)

| Bloco | O que conferir |
|---|---|
| Objetivo e usuário | conversão em uma linha; leitor 1 identificado; página casa com o anúncio e com a temperatura |
| CTA | um texto, primeira pessoa com deliverable; visível em qualquer ponto da rolagem (barra fixa no mobile, header no desktop) |
| Dispositivo | teste do polegar: chegar ao CTA e concluir em menos de 60 s no celular, sem zoom; direção registrada com origem e data de revisão |
| Persuasão | Big Domino identificado; prova e prova social separadas; objeção principal atacada antes do CTA |
| Atrito e velocidade | campos = mínimo para rotear (multi-step se precisar qualificar); sem navegação nem link de saída; LCP abaixo de 2,5 s no mobile e performance mobile acima de 90 no PageSpeed |
| Medição | UTMs no destino e no catálogo; tags testadas em Preview e DebugView; conversão = envio confirmado; Pixel e CAPI deduplicados; lead no CRM com origem |
| Governança | variante B construída antes de publicar a A; amostra mínima e janela de teste definidas; owner, naming e data de revisão registrados |

## REGRAS PARA O AGENTE CONSTRUTOR

- Conversão governa; a camada visual (kit Impeccable, Apache-2.0) existe para a página não sair "quadrada", template da categoria com a cor do cliente. Conflito entre as camadas se resolve a favor da conversão.
- As únicas três rodadas de decisão: insumos (fase 0), direção visual (só sem design system) e primeira dobra. Cada rodada vai em lote, com a decisão que desbloqueia.
- Revisão final por agente separado, que produz o DESIGN.md do cliente. A lista do revisor é a única lista de trabalho: o construtor não reabre a própria caçada a defeitos. Veredito no escopo real ("o revisor pontuou as três correções como resolvidas"), nunca "não restam problemas". Evidência contra um "entregar" reabre a revisão com revisor novo.
- Nenhum comentário de estratégia dentro do HTML entregue: racional de seção e contrato de direção vivem em `docs/`, nunca no código que o concorrente lê.
- Em entregável não entra marcador ([INFERÊNCIA], [LACUNA], [VERIFICAR]): item não resolvido vira pergunta e confirmação antes de escrever. Marcador é ferramenta de documento interno e de rascunho.
- Detector roda antes da entrega e termina sem achado; sem shell, o checklist manual substitui e a entrega diz que o detector não rodou.

## COMO O SUSANO AJUDA

- **Brief de LP novo**: monta a ficha dos 17 campos a partir do que existe na frente (`20_<frente>/<slug>/contexto.md`, histórico de tráfego, provas confirmadas), lista o que falta como um único lote de perguntas e só então passa o brief ao agente construtor ou ao time.
- **Revisão de página existente**: roda os sete blocos do QA e entrega a lista de correções em ordem de impacto (medição e CTA antes de cor e tipografia), cada item com o que muda e por quê.
- **Leitura pós-lançamento**: taxa da página contra benchmark do tipo e contra histórico, lida junto com a qualidade no CRM (lead → MQL → SQL). Taxa alta com qualidade caindo é alerta, não vitória. Hierarquia de correção: oferta e pré-frame → headline e primeira dobra → formulário → velocidade → o resto.
- **Hipótese de teste**: formato do método (`00_susano/dna/metodo/diagnostico_de_funil.md`); variante B antes de publicar a A; registro em `20_<frente>/<slug>/experimentos.md` com corte, número e prazo.

## EXEMPLO FICTÍCIO

Pedido: "Preciso de uma LP para captar diagnóstico gratuito de uma consultoria contábil para clínicas." Frente fictícia: Contábil Norte, B2B, canal de entrada Meta (Stories e feed), tráfego frio, prova confirmada: 140 clínicas atendidas e 2 depoimentos com nome e cargo autorizados.

Ficha (resumo): conversão única = pedir o diagnóstico; evento = envio confirmado do formulário; canal mobile por natureza → direção mobile, revisão com dado real em 30 dias; temperatura fria; leitor 1 vê "Diagnóstico gratuito da sua clínica em 48 h" com a mesma promessa do anúncio; leitor 2 pergunta "quanto custa depois", "quanto tempo leva", "preciso trocar de contador"; leitor 3 traz a objeção "meu contador atual resolve"; CTA "Quero meu diagnóstico" na hero, no meio e no fim, barra fixa no mobile; pós-conversão: thank-you com SLA de 1 dia útil e WhatsApp do atendimento; campos: nome, WhatsApp, número de profissionais (mínimo para rotear); autoridade visual: marca incompleta (logo e duas cores) → rodada de direção.

Saída do Susano: a ficha, o lote de perguntas pendentes (URL final, container GTM, mecanismo de envio, texto de consentimento, SLA confirmado) e, depois das respostas, o brief para o agente construtor. Nada de número inventado: prova que o cliente não confirmou não entra.

## REFERÊNCIA RÁPIDA

**Usar quando**: brief de LP, revisão de página antes de tráfego, leitura de resultado de LP, hipótese de teste de página.
**Não usar quando**: a dúvida é de oferta ou de pré-frame (variáveis 1 e 2 do funil; `dotcom_secrets.md` e `copy_e_headline.md` primeiro) ou de tracking em geral (skill `susano-analytics`).
**Sequência**: lente → ficha → protocolo de dispositivo → construção pelo playbook → QA de sete blocos → análise de realidade com qualidade no CRM.
