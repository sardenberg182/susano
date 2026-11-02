# Exemplos trabalhados do Susano

Sete pares entrada → saída, um por modo de trabalho recorrente, todos com empresa, pessoas e números inventados. Servem para calibrar a forma da resposta (ordem, profundidade, tom, marcadores) antes de produzir no mesmo modo. No Claude Code chegam pela skill `susano-exemplos`; em outro agente, abra o arquivo pelo caminho.

| Arquivo | Modo | Situação (linha de `00_susano/situacoes.md`) |
|---|---|---|
| `leitura_de_wbr.md` | 1 análise | "prepara o WBR", "analisa o WBR" |
| `diagnostico_planilha_de_taxas.md` | 1 análise | "lead caro", "olha essa planilha" |
| `tabela_de_pa.md` | 2 execução | plano de ação a partir de fatos e causas |
| `analise_de_reuniao.md` | 1 análise | "analisa essa transcrição" |
| `resumo_executivo_semanal.md` | 2 execução | B1 do WBR, "escreve o resumo executivo" |
| `mensagem_para_lideres.md` | 2 execução | "manda uma mensagem para o time" |
| `estrutura_de_proposta.md` | 3 estratégia | "brief de migração", "proposta para o decisor" |

## Como usar

1. Identifique o modo e a situação do pedido em `00_susano/situacoes.md`.
2. Abra o exemplo do mesmo modo e leia a seção POR QUE ASSIM: ela liga cada escolha a uma regra do método, com `caminho#seção`.
3. Produza com a mesma ordem e a mesma profundidade, com os dados da frente real. Nunca copie um número, nome ou taxa de exemplo para uma frente real: todo número aqui é inventado para ilustrar a forma.
4. O exemplo não substitui o arquivo da regra: quando a regra importa, cite o arquivo da regra, não o exemplo.

## Formato de cada exemplo

Frontmatter: `id: ex-<slug>`, `tipo: exemplo`, `modo: 1|2|3`, `situacao:`, `atualizado:`. Corpo: ENTRADA (o pedido da pessoa e os dados colados) · SAÍDA (a resposta completa do Susano) · POR QUE ASSIM (3 a 5 linhas ligando a regras do método). `brain.py validate` exige as três seções.

Proposta de exemplo novo: issue "Proposta para o modelo" no repositório `susano`, com entrada e saída fictícias; entra por PR do mantenedor depois da revisão do Sarden.
