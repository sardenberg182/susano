---
id: ref-perf-checklist-diario
tipo: referencia
autor: Sarden
origem: checklist diário do gestor de performance da operação do Sarden (01/04/2026); desde a v0.3.0 é só o índice cronometrado do Bloco 1 da rotina, sem texto próprio (fusão aprovada pelo Sarden em 01/11/2026)
atualizado: 2026-11-01
revisao_pendente: Sarden (edição v0.3.0: vira índice da rotina; o texto que divergia saiu)
---

# Checklist diário do gestor de performance (índice do Bloco 1 da rotina)

> Uso: runbook de abertura do dia, cerca de 60 minutos por conta. Cada passo aponta para a seção da rotina (`00_susano/referencias/performance/rotina_gestor_performance.md`), que é a fonte única do texto; este arquivo não repete checklist. Regra absoluta do dia: nenhuma decisão de pausar, escalar ou trocar criativo com um dia de dado; o diário é monitoramento, a decisão é semanal e ancorada no funil por canal.

| # | Passo | Tempo | Seção da rotina | Pergunta que fecha o passo |
|---|---|---|---|---|
| 1 | Campanhas rodando? | 5 min | §2.1 Checar se as campanhas estão rodando | alguma conta, campanha ou pagamento parou de entregar? |
| 2 | Métrica de alerta primária por canal | 5 min | §2.2 Checar métrica de alerta primária | algum canal saiu do padrão dos últimos 7 dias (CPM, CPC e parcela de impressões perdida, frequência, view rate)? |
| 3 | Gestão diária de palavras-chave (Search) | 10 min | §2.2, bloco "Gestão diária de palavras-chave" | que termos entram como negativa hoje e que termos viram exata? |
| 4 | Rastreio íntegro? | 5 min | §2.3 Checar integridade do rastreio | pixel, CAPI, tags e UTMs disparando, e a diferença plataforma × CRM dentro da tolerância da frente? |
| 5 | Leads, MQLs, SQLs e clientes no CRM | 20 min | §2.4 Checar volume de leads, MQLs, SQLs e clientes no CRM | o volume de ontem é coerente com o investimento, por canal, e o comercial está trabalhando os leads? |
| 6 | Registrar sinais no log | 5 min | §2.5 Registrar sinais no log | o que saiu do padrão está escrito com data, canal e hipótese, para a análise semanal? |
| 7 | Pipeline de criativos | 10 min | §2.6 Pipeline de criativos: brief por canal | que criativo está em fadiga e que brief precisa sair hoje para não faltar criativo na semana que vem? |

## Regras do índice

- Thresholds e tolerâncias são os da rotina (defaults do método, calibrados por frente em `decisoes.md`); este arquivo não carrega número.
- Se o passo não cabe no tempo, o que excede vira item da análise semanal (Bloco 2), não decisão do dia.
- Alteração do checklist se faz na rotina; este índice só muda quando a numeração ou o tempo das seções muda.

## REFERÊNCIA RÁPIDA

**Melhor para**: abrir o dia numa conta; treinar quem assume uma conta; auditar se a rotina diária está sendo feita.
**Ativar quando**: "o que eu olho hoje?", "montar o runbook diário", "a conta parou"; o detalhe é sempre na seção da rotina.
