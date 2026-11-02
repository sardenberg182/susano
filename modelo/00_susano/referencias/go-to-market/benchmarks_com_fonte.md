---
id: ref-gtm-benchmarks-com-fonte
tipo: referencia
autor: Sarden (curadoria)
origem: consolidação das tabelas de benchmark de GTM do método; só entram linhas com publisher, ano e link; as linhas sem fonte identificável da versão anterior saíram (ficam em `90_arquivo/` do repositório do modelo)
atualizado: 2026-11-01
revisar_ate: 2027-06-30
revisao_pendente: Sarden (arquivo novo da v0.3.0; registrar aprovado após leitura)
---

# Benchmarks com fonte

> Uso: referência de mercado para contextualizar um número da frente, sempre como [INFERÊNCIA] com publisher, ano e link. Nunca como meta: a meta é só a registrada em `20_<frente>/<slug>/decisoes.md`. Preferir mediana e quartil quando a fonte dá; segmentar por vertical, estágio, região e modelo antes de comparar. Benchmarks de canal pago (CPL, CPC, CPM, conversão de LP) ficam em `00_susano/referencias/benchmarks/panorama_2026.md` e em `00_susano/referencias/landing_pages/playbook_construtor_html.md` (Anexo E).

## SAAS E VENDAS B2B

| Publisher | Ano | Achado (como a fonte reporta) | Link | Verificado em |
|---|---|---|---|---|
| KeyBanc Capital Markets e Sapphire Ventures, Private SaaS Company Survey (15ª edição) | 2024 | NRR mediano de SaaS privado em torno de 101%; GRR em torno de 86% a 90%; foco em eficiência operacional. ARR growth e quota attainment da edição: [VERIFICAR] no relatório completo | https://info.sapphireventures.com/2024-keybanc-capital-markets-and-sapphire-ventures-saas-survey | 01/11/2026 (busca; números confirmados por cobertura secundária, relatório não reaberto) |
| The Bridge Group, SaaS AE Metrics & Compensation Report | 2024 | 172 empresas B2B SaaS; quota anual mediana US$ 800 mil; OTE mediano US$ 190 mil, mix 53:47 base e variável; win rate mediano 19% (23% em 2022); 51% dos AEs batem a meta (66% em 2022) | https://blog.bridgegroupinc.com/2024-ae-metrics-compensation-benchmark | 01/11/2026 (busca; página e números confirmados) |
| Bessemer Venture Partners, State of the Cloud | 2024 | IA como eixo do relatório ("AI Cloud" substituindo o cloud legado); leitura qualitativa, sem benchmark numérico aqui | https://www.wisdomtree.com/us/insights/blog/bvp-just-released-state-of-the-cloud-2024-here-are-some-highlights (resumo); relatório em bvp.com/atlas [VERIFICAR o endereço exato] | 01/11/2026 (busca) |

## BRASIL: E-COMMERCE E SOFTWARE

| Publisher | Ano | Achado (como a fonte reporta) | Link | Verificado em |
|---|---|---|---|---|
| ABComm, balanço do e-commerce brasileiro | 2024 (publicado jan/2025) | faturamento R$ 204,3 bilhões (+10,5%); 414,9 milhões de pedidos; ticket médio R$ 492,40; 91,3 milhões de compradores; projeção 2025 de R$ 234,9 bilhões e ticket R$ 539,28 | https://mercadoeconsumo.com.br/14/01/2025/ecommerce/e-commerce-brasileiro-cresce-105-e-fatura-r-2043-bilhoes-em-2024 | 01/11/2026 (busca; números confirmados em duas coberturas) |
| ABES e IDC, Mercado Brasileiro de Software: Panorama e Tendências | 2024 e 2025 | Brasil de volta ao top 10 mundial de investimento em TI em 2023 e mantido em 10º em 2024 (US$ 58,6 bilhões); crescimento do setor acima da média global | https://www.abes.org.br/dados-do-setor/ | 01/11/2026 (busca; página e posição confirmadas) |

## LANDING PAGES E FORMULÁRIOS (fontes do playbook de LP, Anexo E.3)

| Publisher | Ano | Achado (como a fonte reporta) | Link | Verificado em |
|---|---|---|---|---|
| Unbounce, Conversion Benchmark Report | 2024 | mediana geral 6,6%; SaaS 3,8%; financeiro 8,3%; top 25% a partir de 11,4%; copy em nível de leitura simples converte 11,1% contra 5,3% em nível profissional | https://unbounce.com/landing-pages/whats-a-good-conversion-rate/ | 16/10/2026 (playbook v3.0) [VERIFICAR o link atual] |
| Google e Deloitte, Milliseconds Make Millions | 2020 | 0,1 s de velocidade = +8,4% de conversão no varejo e +21,6% de progressão para envio de formulário em lead gen | https://web.dev/case-studies/milliseconds-make-millions | 16/10/2026 (playbook v3.0) |
| Think with Google, mobile page speed | s.d. [VERIFICAR ano] | de 1 s para 10 s de carregamento, a probabilidade de bounce no mobile sobe 123% | https://thinkwithgoogle.com/marketing-strategies/app-and-mobile/mobile-page-speed-new-industry-benchmarks/ | 16/10/2026 (playbook v3.0) |
| HubSpot (Dan Zarrella), 40 mil landing pages | s.d. [VERIFICAR ano] | o tipo do campo pesa mais que a quantidade de campos na conversão | https://blog.hubspot.com/blog/tabid/6307/bid/6746/which-types-of-form-fields-lower-landing-page-conversions.aspx | 16/10/2026 (playbook v3.0) |
| Neil Patel, 404 e 833 landing pages | s.d. | 1 campo 18,2%; 2 campos 13,0%; 3 campos 11,5%; equilíbrio entre 4 e 6 | https://neilpatel.com/marketing-stats/conversion-rate-by-form-fields/ | 16/10/2026 (playbook v3.0) [VENDOR] |
| LanderLab, landing page best practices | 2026 | barra fixa mobile +14%; CTA em primeira pessoa +14%; hierarquia de 8 estágios | https://landerlab.io/blog/landing-page-best-practices | 16/10/2026 (playbook v3.0) [VENDOR] |

## REGRAS DE USO

- Toda linha entra na resposta como `[INFERÊNCIA] referência de mercado: <achado> (<publisher>, <ano>)`, nunca como fato da frente.
- Dataset internacional sobrerrepresenta e-commerce e anunciante global; dataset de vendor ([VENDOR]) tem viés de produto. Dizer o viés junto com o número.
- Linha nova só com publisher, ano e link que resolve; linha com link quebrado na revisão (`revisar_ate`) sai ou ganha fonte nova.
- Número da frente contra benchmark é contexto; a decisão continua sendo pelo target da frente e pela régua do WBR.
