---
id: instr-brief-e-proposta
tipo: instrucao
autor: Sarden
carrega_em: sob demanda (skill susano-rituais)
origem: lições de leitura de brief, escopo e proposta da operação do Sarden (mar a out/2026), só a mecânica; sem produto, preço ou cliente
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Brief e proposta: ler a demanda antes de responder

## LER A DEMANDA ANTES DE RESPONDER

A expectativa do cliente vem em camadas, e a proposta responde a todas ou nomeia a que não responde:

1. **Explícita**: o que está escrito no brief.
2. **Implícita**: o que o cliente supõe que está incluído sem dizer.
3. **Comercial**: o que ele precisa mostrar para quem assina.
4. **Estratégica**: o problema de negócio por baixo do pedido.

Depois de ler as camadas, cruzar com o anexo (contrato, escopo anterior, RFP) bloco a bloco: o que o anexo pede que o brief não disse, e o contrário.

## MIGRAÇÃO É TRÊS COISAS

"Migrar" pode ser: **1:1** (carga simples de dados), **com remodelagem** (workflows, pipelines, scoring e páginas redesenhados) ou **com herança operacional** (o que precisa continuar funcionando no dia seguinte). Sem saber qual, ninguém dimensiona. Um pedido que parece "migrar da ferramenta A para a B" costuma ser dois projetos colados: substituição de stack mais salto operacional. Separar as camadas (licença, migração de dados, implantação nova, pedidos vagos) antes de escrever uma linha de escopo. Migração de duas origens simultâneas não cabe no mesmo dimensionamento de origem única.

## BUZZWORD NÃO SE PRECIFICA

"Visibilidade em IA", "automação inteligente", "growth" sozinho: nada disso entra no escopo até virar caso de uso com entrada, saída e dono. Decodificar com o cliente antes, nunca estimar em cima da palavra.

## UNIDADE DE ESCOPO CERTA

Escopo se conta na unidade que o trabalho tem: em site, templates e volume de migração, não "páginas"; em CRM, pipelines, objetos e integrações, não "usuários"; em mídia, canais e campanhas por objetivo, não "verba". Trabalho dentro de projeto maior desconta descoberta compartilhada e templates prontos.

## "ISSO NÃO FAZEMOS" SEM ELABORAÇÃO

Quando o pedido é responsabilidade do cliente (o pacote comercial dele: pitch, pricing, contrato, playbook de vendas), a resposta é curta e sem justificativa longa. Aceitar o limite de escopo quando corrigido, sem elaboração.

## ESTRUTURA DA PROPOSTA

- **Problema → processo → prova.** O caos chega antes da ordem: a seção de problema aterrissa antes da de solução. Para decisor, definição vira diagnóstico só depois do caos; antes disso é aula.
- **Três opções, nunca uma.** Uma opção pede "sim ou não"; três forçam a escolha entre elas e o cliente sente que escolheu. A mesma matemática em formatos diferentes (setup separado mais ramp mais variável) muda a percepção sem mudar o valor.
- **Promete processo quando o histórico não é confiável.** Instrumentação, baseline e método antes de operação gerida; a fotografia inicial do funil na semana zero é pré-requisito de qualquer variável atribuível (variável só sobre o que for atribuído depois do kickoff).
- **Duas frentes simultâneas são proporção de tempo, não fases.** Oitenta por cento na conversão do sprint e vinte na estrutura, invertendo depois; dizer assim, não como fase 1 e fase 2.
- **Escopo complementar é exceção e se diz como exceção.** Quando o cliente já tem um fornecedor na área, mapear o ecossistema, o escopo exato do incumbente e as condições inegociáveis para operar em escopo parcial antes da conversa.
- **"Braço de execução" comoditiza.** A solução enfatiza método, SLA, governança e dado de performance, não "mais mãos".
- **Produto ou escopo novo passa por "é complexo, caro e lento?"** antes de virar tese; a versão simples vem antes de qualquer estimativa de horas.

## LINGUAGEM PARA CLIENTE

- "Oportunidade" no lugar de culpa; o desafio que ancora o escopo vira copy voltada ao cliente.
- Nada de linguagem interna: pricing, scoring, piso de negociação, nota de calibração e marcador de incerteza não circulam. Material externo limpo, arquitetura completa fica no interno.
- Sem matriz de risco colorida, sem gates de execução e sem marcador pendente na versão final: o que não fechou se pergunta e se confirma antes de escrever.
- Prazo de entrega sempre que o cliente espera algo; pergunta clarificadora quando falta pré-condição.

## CHECKLIST DE BURACO OPERACIONAL NO ESCOPO

Antes de enviar, procurar o que o documento não diz:

- Teto de volume (campanhas, envios, páginas) está escrito?
- Quem produz conteúdo, criativo e copy está nomeado?
- Pré-requisitos técnicos na conta do cliente (acessos, tracking, integrações) estão listados antes de prometer relatório ou resultado?
- Dependências do cliente têm dono, data e consequência?
- O que está fora do escopo está dito?
- Crédito, verba ou evento sem captura identificável: a recomendação honesta é não gastar, não "aproveitar".
- A unidade de escopo bate com o trabalho real?

## REFERÊNCIA RÁPIDA

**Melhor para**: leitura de brief, RFP ou pedido de proposta; estrutura de proposta para decisor; revisão de escopo antes de enviar; resposta a pedido fora de escopo.
**Ativar quando**: um pedido chega como uma palavra ("migração", "AEO", "growth"); a proposta começa pela solução; há uma só opção; o histórico do cliente não permite prometer resultado; o escopo está contado na unidade errada.
