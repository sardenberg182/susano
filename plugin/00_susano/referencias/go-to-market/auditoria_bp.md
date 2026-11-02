---
id: ref-gtm-auditoria-bp
tipo: referencia
autor: Sarden
origem: lições de auditoria de business plan e de unit economics da operação do Sarden (2026), só a mecânica; exemplos inventados, sem o número de nenhum BP real
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Auditoria de BP: as fórmulas certas, os erros clássicos e como ler a planilha

> Uso: antes de aceitar qualquer projeção de receita, CAC, churn ou margem de um business plan (o seu ou o de um cliente). Absorve as fórmulas de unit economics do método. Complementa `00_susano/instrucoes/gp_bp.md` (o ritual de GP e BP) e `modelos_quantitativos.md` (forecasting estatístico, scoring, atribuição).

## TESE

BP se audita na camada de fórmula, não na camada de valor: a maioria dos erros graves é estrutural (acumulador errado, célula sem fórmula, calendário desalinhado) e produz números plausíveis com cara de certo. Primeiro a estrutura, depois as premissas, por último o número.

## FÓRMULAS CERTAS

- **New MRR por tier**: `Σ (novos clientes do tier × ticket do tier)`. Ticket médio agregado superestima quando o mix muda ao longo do plano (o erro cresce com o horizonte: no mês 30 pode passar de 40%).
- **Churn por tier**, nunca agregado: cada tier tem sua taxa; a média ponderada muda com o mix. Em base pequena, a unidade mínima de churn é um cliente: 17 clientes a 3,5% dão 0,6 cliente, e um churn real é 5,9%. Arredondar por mês é defensável em pitch; distribuir proporcional ao risco ponderado evita meses sem churn em nenhum tier.
- **CAC**: `(gasto de marketing + gasto de vendas do período) ÷ novos clientes do período`, por canal sempre que o dado permitir; CAC consolidado esconde o canal que sangra.
- **LTV**: `ARPU × margem bruta ÷ churn mensal` (em meses de vida); ajustar pela taxa de ativação quando o produto exige ativação.
- **Payback de CAC**: `CAC ÷ (ARPU × margem bruta)`, em meses. É o número que o caixa sente.
- **LTV:CAC**: razão; default de leitura do método: abaixo de 3 pede atenção, acima de 5 pode ser subinvestimento. Default, não benchmark.
- **GRR e NRR**: `GRR = (receita inicial da cohort − churn − contração) ÷ receita inicial` (teto 100%); `NRR = GRR + expansão`. Preservação e expansão são perguntas diferentes.
- **Rule of 40**: `crescimento % + margem EBITDA % ≥ 40` como régua de equilíbrio entre crescimento e eficiência, para SaaS em escala; não vale para serviço nem para base pequena.
- **Weighted pipeline**: `forecast = Σ (valor do negócio × probabilidade da etapa)`, com probabilidade histórica por etapa da frente, nunca a probabilidade padrão da ferramenta.
- **Impostos**: no lucro presumido, sobre a receita bruta, não sobre o EBITDA; o adicional de IRPJ não pode faltar. Alíquota e regime são da frente (`contexto.md`), com a data.

## ERROS CLÁSSICOS (reconhece-se por)

1. **Acumulador de MRR que soma a base inteira × ticket todo mês**: receita cresce dezenas de vezes mais que a base. Checagem: receita do mês ÷ clientes ativos deve ficar perto do ticket.
2. **Churn declarado numa célula e referenciado por zero fórmulas**: a premissa existe, o modelo não a usa. Checagem: rastrear as dependências da célula.
3. **Conversão compondo mês a mês sem teto**: 2% ao mês vira taxa impossível em 24 meses. Checagem: a taxa do último mês é defensável contra o histórico?
4. **Headcount crescendo sem linha de salário**: custo fixo não acompanha o time. Checagem: custo de pessoal ÷ headcount deve ser estável ou justificado.
5. **Abas duplicando cabeçalho e zerando receita**: cópia de aba com linha de título no lugar de dado.
6. **Calendário desalinhado entre abas**: uma aba meses à frente das outras; soma de meses diferentes como se fossem o mesmo.
7. **Capacidade menor que carga planejada**: time dimensionado atende menos projetos do que o plano vende (checar no mês mais distante, onde o erro aparece).
8. **Produtividade por pessoa crescendo várias vezes sem premissa de automação**: o plano assume ganho que ninguém explicou.
9. **Margem de serviço irreal**: EBITDA de serviço acima de 50% destrói credibilidade na hora; serviço paga gente.
10. **Ticket médio agregado em plano com mix mudando**: erro 1 das fórmulas certas, versão silenciosa.

## COMO AUDITAR

1. **Ler a camada de fórmula** com `openpyxl` (`load_workbook(caminho)` sem `data_only`): a célula traz a fórmula, não o valor em cache. Nunca MarkItDown ou conversor de texto para modelo financeiro: eles extraem só o valor em cache e escondem toda a estrutura.
2. Mapear as abas, o calendário de cada uma e as células de premissa (inputs). Listar as premissas que nenhuma fórmula referencia.
3. Recalcular em Python os totais-chave (receita, clientes ativos, churn, custo de pessoal, EBITDA) a partir das premissas e comparar com os valores em cache; divergência é achado, nunca "arredondamento".
4. Passar os dez erros clássicos como checklist; cada achado com aba, célula e impacto no número final.
5. Entregar em FATO (o que a planilha diz, com célula) → análise vs target (o que a estrutura implica contra a meta ou contra a realidade) → PA (o que corrigir, em ordem de impacto). Dado ausente é [LACUNA]; premissa sem fonte é [VERIFICAR]; nunca interpolar.

## EXEMPLO FICTÍCIO

BP de uma agência inventada, 36 meses, três tiers. O acumulador de receita somava `clientes_acumulados × ticket_médio` em todo mês, e o churn de 4% estava numa célula que nenhuma fórmula lia. Recalculo em Python: receita do mês 36 caía de R$ 9,8 milhões para R$ 1,1 milhão com o acumulador correto e o churn aplicado; a margem EBITDA de 71% virava 23%. Nenhum número de entrada estava errado; a estrutura estava. PA: corrigir o acumulador (receita = Σ tier × ticket do tier, com churn por tier), ligar a premissa de churn, recalcular capacidade do time no mês 36 (o plano vendia 149 projetos para um time que atendia 132).

## REFERÊNCIA RÁPIDA

**Melhor para**: auditar BP ou GP em planilha antes de qualquer análise; conferir unit economics de proposta, pitch ou plano de cliente.
**Ativar quando**: planilha chega como anexo; receita cresce mais rápido que a base; margem de serviço acima de 50%; churn "declarado"; ticket médio único em plano com tiers.
**Nunca**: ler modelo financeiro por conversor de texto; aceitar probabilidade padrão de etapa no forecast; usar benchmark de mercado como target da frente.
