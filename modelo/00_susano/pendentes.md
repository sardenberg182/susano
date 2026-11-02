---
id: susano-pendentes
tipo: procedimento
atualizado: 2026-11-02
---

# Pendências do modelo

Este arquivo registra o que está aprovado pelo Sarden, o que espera a leitura dele e as propostas abertas. Muda a cada versão; a versão em si está no `CHANGELOG.md` do repositório do modelo.

## Aprovado pelo Sarden

- 01/11/2026, 16:45: licença CC BY 4.0 no conteúdo, MIT no código (`00_susano/LICENCA.md`, `LICENSE`, `LICENSE-CONTEUDO.md`).
- 01/11/2026, 16:51: `00_susano/identidade.md` v0.1.6, lida no chat. Os acréscimos da v0.3.0 estão em `revisao_pendente`.
- 01/11/2026, 16:43: `00_susano/sobre_o_sarden.md`, texto do próprio Sarden.
- 01/11/2026, 16:54: os 8 DNAs originais de `00_susano/dna/metodo/`, lidos no chat ("Revisado pode seguir"); cada um leva a linha `aprovado:` no frontmatter. As seções ALERTAS OPERACIONAIS e os 5 DNAs novos da v0.3.0 estão em `revisao_pendente`.
- 01/11/2026, 22:40: decisões da v0.3.0: tom do núcleo mantido com calibração a quem está na sessão; fusão dos arquivos do Notion (checklist → índice da rotina; Panorama fonte única); casos de decisão rodados à mão antes da tag; as duas fontes anexadas no chat.
- 02/11/2026, 07:30: depois da rodada dos casos de decisão: nada pessoal de ninguém vai para arquivo ("Não pode gravar nada de ninguém nesse projeto, ele é público"); exemplo e case sempre fictícios, em contexto real, nunca com número real ("Sempre exemplos fictícios com contextos reais, nunca números reais"). As regras entram no núcleo, na identidade, no anti-padrão 18, no diagnóstico de funil, no exemplo de proposta e nas referências; o texto novo segue em `revisao_pendente`.

## Em revisão (aguardando a leitura do Sarden)

Todo arquivo novo ou alterado da v0.3.0 leva `revisao_pendente: Sarden` no frontmatter com o que mudou. Depois da leitura, a linha vira `aprovado: Sarden, AAAA-MM-DD`. Lista por PR no `CHANGELOG.md` (seção v0.3.0): núcleo e identidade (PR-1), DNAs (PR-2), instruções e playbook de LP (PR-3), situações, calibração e exemplos (PR-4), referências (PR-5).

## Arquivos de origem

Os 67 arquivos da pasta de origem da migração estão todos no modelo (57 em 31/10/2026, 10 em 01/11/2026). A versão curta do artigo 4 do Balfour, citada em arquivos antigos, nunca existiu: as citações apontam para `00_susano/biblioteca/balfour/04_model_market_fit.md`. Os nove arquivos de GTM analytics da v0.2.1 e o capítulo Brasil do HubSpot foram fundidos na v0.3.0; os originais ficam em `90_arquivo/` do repositório do modelo.

## Base de performance

Fechada na v0.1.4 (01/11/2026) com os 5 direcionais de performance do Notion do Sarden, em `00_susano/referencias/performance/`; na v0.3.0 ganhou `licoes_de_conta.md` e `regua_criativos_leadgen.md`, e o checklist virou índice da rotina.

## Revisões abertas

- [VERIFICAR] Thresholds de `referencias/performance/rotina_gestor_performance.md` (frequência acima de 3, discrepância acima de 15%, LTV:CAC acima de 3:1, escala de 20% a 30%): declarados como defaults do método na v0.3.0; o Sarden ainda não os releu um a um.
- [VERIFICAR] Nomenclatura de produto marcada na v0.3.0: campanhas de vídeo do Google (antigo TrueView), Demand Gen (antigo Discovery), Message ads do LinkedIn (antigo Sponsored InMail), a sigla SPC da rotina; limite de 100 mil conversas por dia no WhatsApp; páginas internas do Panorama por segmento.
- Contradições e números sem fonte ficam marcados nos próprios arquivos, com as duas fontes preservadas: decisão do Sarden (01/11/2026), ter vários exemplos de fontes e direcionais vale mais do que resolver a contradição no silêncio.
- Skill `stories-10x` a partir do manual e da referência de social orgânico (`referencias/social_organico/`).
- `testes/casos_decisao.md` (repositório do modelo): rodar os 26 casos antes da tag v0.3.0 e registrar a concordância na tabela do arquivo e no `CHANGELOG.md`.

## Propostas abertas (issues do repositório `susano`)

Nenhuma. Propostas de quem usa o modelo entram pela issue "Proposta para o modelo" (`.github/ISSUE_TEMPLATE/proposta_para_o_modelo.md`) e ficam listadas aqui por número até virarem PR.
