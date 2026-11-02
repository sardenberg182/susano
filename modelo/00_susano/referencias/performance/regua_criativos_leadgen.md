---
id: ref-perf-regua-criativos-leadgen
tipo: referencia
autor: Sarden
origem: régua de criativos para lead gen da operação do Sarden (2026); default do método, sem exemplo de cliente
atualizado: 2026-11-01
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Régua de criativos em lead gen: ROAS não mede criativo

> Uso: avaliar criativos de conta de geração de leads com um score composto em que MQL e custo por MQL são o primário e o resto sustenta. Todos os números abaixo são **default do método, a calibrar por frente** e registrar em `20_<frente>/<slug>/decisoes.md`; nenhum é benchmark de mercado.

## TESE

Em conta de lead gen o criativo não vende, qualifica. ROAS não mede criativo porque a receita chega semanas depois e carrega o trabalho do SDR; CTR e hook medem atenção, não intenção. O indicador primário de um criativo é o MQL que ele gera e o custo por MQL (CRM, com origem por anúncio); os outros quatro componentes explicam por que o primário está onde está.

## OS 5 COMPONENTES

| # | Componente | Régua default (calibrar por frente) | Papel |
|---|---|---|---|
| 1 | MQLs gerados e custo por MQL | contra a meta da frente (custo por MQL alvo em `decisoes.md`) | Primário: decide manter, escalar ou pausar |
| 2 | Retenção a 25% da duração (sobre plays de 3 s) | 40% a 50% saudável; abaixo de 30%, o miolo está matando o vídeo | Sustentação: o vídeo segura quem clicou em assistir? |
| 3 | Hook (porcentagem assistida no início) | abaixo de 20% fraco · 20% a 25% ok · 30% ou mais forte · 40% ou mais elite | Gancho: os primeiros segundos prendem? |
| 4 | Frequência | teto 3,5 | Fadiga: o público já viu demais? |
| 5 | CTR (link) | 3% verde · 2% amarelo · abaixo, vermelho | Resposta: a promessa gera clique? |

Leitura: componente 1 define o veredito; 2 a 5 dizem onde mexer. Criativo com MQL bom e CTR vermelho é promessa fraca para gente certa: mexer na chamada, não no público. Criativo com CTR verde e MQL ruim é promessa boa para gente errada: mexer no público ou no filtro do formulário, não no vídeo.

## COMO MEDIR HOOK

Hook se mede por porcentagem assistida, não por "play de 3 s sobre impressão" (decisão do método). Em vídeo de 30 a 60 s, "25% da duração" equivale ao hold rate (ThruPlay), daí a faixa de 40% a 50% no componente 2. Para o hook em si, usar a métrica de retenção dos primeiros segundos da plataforma, sobre quem começou a assistir, comparando criativos da mesma frente e do mesmo posicionamento: hook de feed e de Stories não se comparam.

## NOTA DE CALIBRAÇÃO

A régua de CTR em 3% é aspiracional por decisão (padrão de creators), não média de mercado: feed do Meta costuma rodar bem abaixo disso em lead gen B2B. Aplicada sem calibração, a régua condena o portfólio inteiro e o time passa a trocar criativo que estava gerando MQL. Decisão de régua agressiva precisa ser consciente e registrada; o default existe para não começar do zero, não para julgar sem contexto. Mesma regra para o teto de frequência: público pequeno satura antes de 3,5.

## O QUE NÃO ENTRA NO SCORE

- ROAS e receita (lag e trabalho comercial no meio).
- CPL bruto (lead barato com MQL ruim é o pior criativo da conta, não o melhor).
- Engajamento (curtida, comentário, compartilhamento) como proxy de intenção.
- Comparação entre frentes ou entre contas: a régua é por frente, o portfólio é por frente.

## REFERÊNCIA RÁPIDA

**Melhor para**: decidir manter, escalar ou pausar criativo em conta de lead gen; separar problema de promessa, de público e de produção.
**Ativar quando**: alguém avalia criativo por ROAS, CTR ou "engajou bem"; pedido de "trocar criativo" sem olhar MQL por anúncio; portfólio inteiro "reprovado" por uma régua não calibrada.
**Junto com**: `licoes_de_conta.md` (fadiga, frequência, volume sem valor) e `00_susano/dna/metodo/copy_e_headline.md` (o que mexer na promessa).
