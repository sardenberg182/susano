---
id: ref-crm-padrao-implementacao
tipo: referencia
autor: Sarden
origem: playbook padrão de implementação de CRM da operação do Sarden (pipes, cadência, atribuição com herança, metas e lições de contagem; mar a out/2026), só a regra; sem cliente, sem número de cliente
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Padrão de implementação de CRM: pipes, cadência, atribuição e metas

> Uso: o esperado de qualquer implementação de CRM no método. Vale para qualquer plataforma; o anexo no fim traduz para HubSpot. Cada frente configura o de-para (nomes de etapa, critério de MQL, propriedades) e registra em `20_<frente>/<slug>/contexto.md`; sem o de-para configurado, o funil por canal não nasce confiável e o módulo de metas não deveria ser exibido.

## TESE

O pipe padrão é o esperado; cada frente configura. Duas estruturas (Lead e Negócio), uma cadência de contato com regra de negócio escrita, sete propriedades de atribuição com herança e metas mensais com quebra semanal. Tudo isso é pré-estrutura: vem antes de qualquer análise de taxa, porque é o que torna a taxa comparável.

## PIPE LEAD

Novo Prospect → Tentativa de Contato → Contactado → Pré-Qualificado (SAL) → Reunião Agendada → Qualificado (SQL). Saída lateral: Prospect Perdido, a partir de Tentativa de Contato, Contactado ou Pré-Qualificado.

Em documento, o pipeline vai em formato kanban (colunas), não em fluxograma.

## CADÊNCIA NA TENTATIVA DE CONTATO (regra de negócio)

| Momento | Ação |
|---|---|
| Primeiras 24 h | 2 mensagens de WhatsApp + 2 e-mails |
| Até 48 h | mais 2 toques |
| Sempre | 2 ligações (a regra é buscar o atendimento, não registrar a tentativa) |
| Atendeu | follow-up conduzido pelo SDR |
| Não atendeu | 1 follow-up por semana até a jornada de perdido |
| Jornada de perdido | vários follow-ups por semana, até completar 1 mês |

A cadência é default do método; a frente ajusta volumes e canais, nunca a lógica (velocidade no pico de intenção, depois persistência decrescente, depois recuperação). Mediana de tempo até a primeira ligação é o indicador da cadência; tarefa concluída com atraso é o indicador de disciplina.

## PIPE NEGÓCIO

Novo SQL → Em andamento → Negociação → Contrato enviado → Negócio Ganho. Saída lateral: Negócio Perdido, a partir de Negociação ou Contrato enviado.

## RECUPERAÇÃO DE PERDIDOS

1 e-mail + 1 WhatsApp por mês, durante 3 meses, com motivo de perda registrado na saída. Arroz com feijão, replicável em qualquer frente. Motivo de perda por canal alimenta a mídia: fora do ICP → targeting; não decisor → copy e público; sumiu → intenção; sem verba → targeting; concorrente → oferta, não tráfego.

## ONDE CADA ETAPA SE QUALIFICA

- **MQL** qualifica no formulário, por pré-requisito de ICP (porte, segmento, perfil, faturamento mínimo quando couber), com critério definido pelo modelo de negócio, não pelo marketing isolado. Lido via lifecycle stage ou propriedade equivalente, com de-para por frente.
- **SQL** qualifica no SDR, por momento de compra e intenção ativa; é o MQL aceito por vendas.
- **Não-MQL fica como lead.** É ativo (nutrição, recuperação), não lixo.
- **A régua de MQL anda na direção do ICP conforme o dado chega.** Critério inicial amplo; com o pós-venda devolvendo quem compra e quem não compra, o critério aperta. O efeito esperado é menos lead na mão do vendedor e mais venda, não "mais MQL"; a meta migra de volume de lead para receita gerada, inclusive para o time de mídia (de trás para frente: receita ← vendas ← SQL ← MQL ← lead). MQL sem critério é o oposto: quase todo lead vira MQL e a etapa seguinte engasga. Quando o critério muda, a data da mudança vai para `decisoes.md`: as taxas antes e depois não se comparam.
- Vocabulário completo em `00_susano/dna/metodo/dicionario.md`.

## ATRIBUIÇÃO COM HERANÇA (7 propriedades)

Sete propriedades padronizadas, replicadas com herança Contato > Lead > Negócio, com prefixo da organização (`[ORG]`, a frente define o seu):

| # | Propriedade | Regra |
|---|---|---|
| 1 | [ORG] First Click | chumbado na criação do contato; nunca muda; herdado |
| 2 | [ORG] Campanha Original | campanha do first click |
| 3 | [ORG] Detalhamento da Campanha Original | detalhe ou segmento do first click |
| 4 | [ORG] Last Click | dinâmico: última conversão com intenção de compra |
| 5 | [ORG] Última Campanha | campanha do last click |
| 6 | [ORG] Detalhamento da Última Campanha | detalhe ou segmento do last click |
| 7 | [ORG] Jornada de Fontes | lista acumulativa de todas as fontes |

Leitura: topo de funil (lead, MQL) lê Contato ou Lead; fundo (SQL, Won, valor) lê Negócio. Dupla visão de graça: first click diz qual canal origina, last click diz qual canal converte. First click do CRM e last click das plataformas contam histórias diferentes e nunca se consolidam como se fossem comparáveis. Sem o remap implementado, o funil por canal não nasce confiável: é item da pré-estrutura. Em documento de produto ou proposta, a atribuição entra como anexo técnico, nunca no corpo.

## METAS

Cadastradas pelo dono da frente, mensais com quebra semanal (diarizar quando a frente tem agenda diária). Status pela régua de `00_susano/instrucoes/wbr.md`. Strike 1, 2 e 3: meses consecutivos sem bater a meta; a partir do terceiro, observação formal e possível troca de quem lidera a frente. **Regra de proteção**: frente sem pré-estrutura completa (métricas definidas, de-para configurado, classificação de canais) não exibe módulo de metas; evita analisar número errado com cara de certo.

## LIÇÕES DE CONTAGEM

- **Dois jeitos de contar "cliente" dão dois números.** Filtrar por negócio fechado (propriedade de closed won) e contar negócios que entraram na etapa de ganho dão resultados diferentes. Antes de publicar um número, cruzar com a lógica do relatório salvo que a frente já usa e declarar a definição no topo do dashboard.
- **Convenção de nome de relatório**: prefixo da organização e padrão fixo (`[ORG] Volume - MQL - DoD`). Dezenas de relatórios com um padrão de nome é parte do ativo; a definição de cada métrica fica visível.
- **Propriedades de tempo ficam em milissegundos** em algumas plataformas; converter antes de ler mediana.
- **Histórico de propriedade fora da API em alguns conectores**: mudança em massa (milhares de negócios num dia) se investiga na interface (histórico da propriedade), e o autor da mudança nem sempre é identificável por ID.
- **Bug de duplicação de negócios infla taxa de conversão.** Taxa SQL → Won acima de 60% pede verificação de duplicidade antes de comemoração.
- **Tráfego direto absorve conversão quando a UTM falha.** Direto grande é tracking quebrado até prova em contrário.

## ANEXO HUBSPOT

- Lifecycle stage como estrutura base de MQL e SQL (com de-para por frente), propriedades de qualificação e "Data de MQL" e "Data de SQL" para medir a passagem.
- Workflows de WhatsApp dentro do CRM: mensagem na chegada, cadência de tentativa, follow-ups de 1 h, 2 h e 24 h; lead atendido no pico de intenção.
- Um portal acessível por vez no conector; confirmar se uma empresa existe é buscar a company pelo nome. Detalhes de plataforma em `00_susano/referencias/plataformas/hubspot/dossie_mestre.md`.

## REFERÊNCIA RÁPIDA

**Melhor para**: implementação ou auditoria de CRM; definir pré-estrutura antes de analisar funil; brief de migração (com `00_susano/instrucoes/brief_e_proposta.md`).
**Ativar quando**: funil por canal não bate; MQL "automático"; duas contagens de cliente; pedido de meta sem de-para configurado; discussão de "qual canal converte".
