---
id: ex-estrutura-de-proposta
tipo: exemplo
modo: 3
situacao: "brief de migração", "proposta para o decisor"
autor: Raijin (forma); método do Sarden
atualizado: 2026-11-02
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Exemplo: estrutura de proposta a partir de um brief de migração de CRM

Empresa, brief e números inventados. A forma é o que vale. Nenhum preço: valor de contrato não entra no método nem no repositório.

## ENTRADA

Quem pede: sócio da organização, com um brief recebido por e-mail.

> "Chegou isso da Forja Industrial. Me dá a estrutura da proposta para eu levar na reunião com o diretor deles na quinta. Sem preço ainda."

Brief colado (cliente: Forja Industrial, fabricante B2B de componentes, 40 vendedores, 2 CRMs em uso):

> "Queremos migrar nosso CRM para uma plataforma única até março. Hoje temos o comercial numa ferramenta e o pós-venda em outra, com planilhas no meio. Precisamos de automação inteligente para os vendedores pararem de perder follow-up, dashboards para a diretoria e visibilidade em IA. Em anexo, o contrato atual com o fornecedor do CRM comercial (vence em fevereiro) e a lista de 23 relatórios que a diretoria usa hoje."

## SAÍDA

**Leitura da demanda em camadas**

1. Explícita: unificar dois CRMs em uma plataforma até março; automação de follow-up; dashboards; "visibilidade em IA".
2. Implícita: os 23 relatórios da diretoria continuam saindo no dia seguinte à migração; os 40 vendedores não param de vender durante a troca; o histórico dos dois sistemas vem junto.
3. Comercial: o diretor precisa mostrar ao conselho que a troca paga o custo do contrato que vence em fevereiro, com data de corte que não o deixe sem CRM.
4. Estratégica: a empresa não enxerga o cliente de ponta a ponta (venda e pós em sistemas separados, planilha no meio); follow-up perdido é sintoma de processo sem dono, não de falta de automação.

Cruzando com o anexo: o contrato vence em fevereiro e o brief pede março. Ou se renova um mês, ou a migração da origem comercial acontece até fevereiro e o pós-venda em março. Isso é decisão do cliente e entra como pergunta na quinta, não como suposição no escopo. A lista de 23 relatórios é a unidade de escopo mais importante do documento: cada um tem fonte de dado e dono, e nenhum pode "cair".

**O que esse pedido é de verdade**

"Migrar" aqui são três coisas coladas: carga de dados de duas origens (não é 1:1: duas origens simultâneas não cabem no dimensionamento de uma); remodelagem (pipelines, automações e scoring não existem hoje, vão nascer na nova ferramenta); e herança operacional (23 relatórios e 40 vendedores funcionando no dia seguinte). "Automação inteligente" e "visibilidade em IA" não entram no escopo até virarem caso de uso com entrada, saída e dono: na quinta, a pergunta é "qual follow-up vocês perdem, em que etapa, e o que deveria acontecer sozinho?".

**Estrutura da proposta (problema → processo → prova)**

1. **O problema, com os números deles**: dois sistemas, planilha no meio, follow-up perdido em qual etapa e quanto isso custa em pipeline parado [a frente precisa desses números do cliente antes da versão final; sem eles, a seção fica como oportunidade descrita, não quantificada].
2. **O processo**: semana zero de instrumentação (fotografia do funil atual nos dois sistemas e nas planilhas) → desenho do modelo único (objetos, pipelines, propriedades, os 23 relatórios mapeados um a um para a fonte nova) → migração em duas ondas (comercial até a data do contrato, pós-venda depois) → automações só do que o desenho pediu → treinamento por papel → operação assistida por 30 dias. Variável, se houver, só sobre o que for atribuído depois do kickoff.
3. **A prova**: método e governança (ritual semanal, dono de cada relatório, critério de pronto por onda), não "mais mãos". Caso de outro cliente não entra, nem anonimizado: a prova usa exemplo fictício em contexto real, nunca número real.

**Três opções, a mesma matemática em formatos diferentes**

| Opção | O que inclui | Para quem faz sentido |
|---|---|---|
| A. Migração assistida | carga das duas origens, modelo único, os 23 relatórios, treinamento; automações só as de follow-up já desenhadas | diretoria que quer trocar de sistema com o mínimo de mudança operacional |
| B. Migração com remodelagem | A mais desenho de pipelines, scoring e automações por etapa, operação assistida por 30 dias | quem quer que a troca resolva o follow-up perdido, não só mude a ferramenta |
| C. Migração com operação gerida | B mais 90 dias de operação do CRM pela frente (rotinas, relatórios, higiene de dado) com variável sobre indicador atribuído a partir do kickoff | quem não tem dono interno do CRM e precisa que o sistema funcione sem depender de um vendedor |

A recomendação, dita na reunião e não no papel: B. A pede "sim ou não"; C pressupõe uma estrutura interna que o brief sugere não existir, e vale como degrau seguinte.

**Perguntas para a quinta (um lote, cada uma com a decisão que destrava)**

- Renovar um mês do contrato atual ou migrar o comercial até fevereiro? (define as ondas e a data de corte)
- Quais dos 23 relatórios a diretoria realmente abre por semana? (define o que migra na onda 1 e o que vira relatório novo)
- Qual follow-up é perdido, em que etapa, e quem é o dono hoje? (define as automações da opção B e tira "inteligente" da frase)
- Existe dono interno do CRM depois da migração? (decide entre B e C)
- Quem produz a limpeza do dado das planilhas antes da carga? (dependência do cliente, com dono, data e consequência)

**Buracos operacionais que a versão final precisa fechar**: teto de registros e de automações na licença escolhida; pré-requisitos técnicos (acessos de administrador nos dois sistemas, exportação completa, integrações atuais listadas); o que está fora (site, mídia, conteúdo); dependências do cliente com consequência escrita; a unidade de escopo contada em objetos, pipelines, integrações e relatórios, não em "usuários".

**Para o material do cliente**: "oportunidade" no lugar de culpa pelo follow-up perdido; sem matriz de risco colorida, sem gate, sem marcador pendente; prazo em tudo que ele espera receber. Pricing, piso de negociação e esta leitura em camadas ficam no interno.

## POR QUE ASSIM

- Quatro camadas da demanda antes de qualquer escopo, e o anexo cruzado bloco a bloco com o brief (contrato que vence antes do prazo pedido): `00_susano/instrucoes/brief_e_proposta.md#LER A DEMANDA ANTES DE RESPONDER`.
- "Migrar" decomposto em carga, remodelagem e herança operacional; buzzword ("automação inteligente", "visibilidade em IA") não se precifica até virar caso de uso: `00_susano/instrucoes/brief_e_proposta.md#MIGRAÇÃO É TRÊS COISAS` e `#BUZZWORD NÃO SE PRECIFICA`.
- Problema → processo → prova, três opções e processo prometido onde o histórico não é confiável (semana zero de instrumentação, variável só sobre o atribuído): `00_susano/instrucoes/brief_e_proposta.md#ESTRUTURA DA PROPOSTA`.
- Unidade de escopo certa (objetos, pipelines, integrações, relatórios) e checklist de buraco operacional antes de enviar: `00_susano/instrucoes/brief_e_proposta.md#UNIDADE DE ESCOPO CERTA` e `#CHECKLIST DE BURACO OPERACIONAL NO ESCOPO`.
- Perguntas em um lote, cada uma com a decisão que destrava; linguagem interna e marcador fora do material do cliente: `00_susano/nucleo.md#Sempre e nunca` e `00_susano/instrucoes/brief_e_proposta.md#LINGUAGEM PARA CLIENTE`. Sem preço: valor de contrato não entra no repositório (`CONVENCOES.md`, segurança).
