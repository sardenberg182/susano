# Susano: o método Sarden no Claude Code

O Susano é o jeito de trabalhar com este repositório pelo Claude Code. O repositório guarda o conhecimento do projeto (organização, frentes, decisões, referências); o Susano é o agente que lê esse conhecimento, trabalha com você e, no fim, salva o que mudou para o próximo que chegar. O método vem do modelo `susano`, do Sarden, e chega aqui como arquivos gerenciados em `00_susano/`.

## O que você precisa

- Assento no Claude com acesso ao Claude Code (2.1.295 ou mais novo: abaixo disso, as travas de privacidade podem liberar a escrita quando estouram o tempo; a abertura avisa).
- Conta no GitHub com acesso a este repositório.
- App desktop do Claude ou o navegador em claude.ai/code.

## Primeiro acesso

**Nuvem (recomendado para quem não programa):** no app do Claude, aba Code, ambiente Cloud, escolha este repositório. Na primeira vez, conecte o GitHub. Digite `/onboarding`.

**Local:** git e Python 3.9 ou mais novo (sem Python, as travas barram a escrita em vez de liberar). Clone o repositório, abra a pasta raiz no app (Code → Local) ou rode `claude` na raiz, aceite o diálogo de confiança da pasta e rode `/onboarding`. Ele oferece instalar a checagem antes de cada commit.

## O dia a dia

1. Abra sempre na raiz do repositório: em subpasta, regras e travas não carregam.
2. `/cerebro` para saber o que está rolando.
3. `/frente <slug>` para focar numa frente: o Susano passa a usar só os dados dela.
4. Trabalhe: análise (`/analise`), material novo (`/ingerir`), planos e entregas.
5. `/salve` no fim: registra o que aconteceu, atualiza o estado, valida e abre o PR.
6. O dono aprova o PR. Até lá, nada entra na `main`.

## Como o Susano carrega o método

Na abertura entra só o núcleo (`00_susano/nucleo.md`, cerca de 2 mil tokens) mais as regras deste repositório: o pacote do modelo cabe em 6.500 tokens estimados e 1.500 ficam reservados ao que o projeto acrescenta. O resto do método chega por skills, quando a tarefa pede: modelos ativos, DNA, biblioteca, performance, analytics, GTM, plataformas, rituais. Cada skill é um índice que aponta o arquivo certo em `00_susano/`; o Susano abre só esse arquivo e cita caminho e seção. `python3 scripts/brain.py tokens` mostra a estimativa da carga de abertura.

## De onde vem o método

`00_susano/` é cópia gerenciada do modelo. Ninguém edita aqui: uma versão nova chega por `copier update`, num PR que o dono do projeto aprova (veja `CONTRIBUTING.md`). Ideia de melhoria do método: anote no PR do `/salve`, seção "Proposta para o modelo".

## Comandos

| Comando | Para quê |
|---|---|
| `/cerebro` | briefing do que está quente |
| `/frente <slug>` | foco numa frente, com isolamento |
| `/analise` | análise de dados: FATO → análise vs target → PA |
| `/ingerir <material>` | material bruto vira conhecimento no lugar certo |
| `/salve` | persiste a sessão, valida e abre o PR |
| `/nova-frente <slug>` | cria a pasta de uma frente |
| `/onboarding` | primeiro acesso |
| `/estado-quente` | refresh semanal dos estados |
| `/brain-audit` | auditoria mensal |
| skills `susano-*` | o método por domínio (ativos, metodo, biblioteca, performance, analytics, gtm, plataformas, rituais): o Susano carrega a que a tarefa pede; você pode pedir pelo nome |
| `python3 scripts/brain.py mapa` | gera `MAPA.md`: frentes, dono, data do estado, organização, projetos |
| `python3 scripts/brain.py hot` | gera `10_<org>/hot.md`: estado quente agregado (14 dias) |
| `python3 scripts/brain.py fonte "<termo>" --frente <slug>` | arquivo e linha de qualquer combinado, decisão ou número da frente em foco (`--todas` só para comparar, com a origem em cada linha) |
| `python3 scripts/brain.py migrar` | depois de um `copier update`: aplica o contrato da versão (bloco gerenciado do `AGENTS.md`, arquivos obrigatórios das frentes) |
| `python3 scripts/brain.py pessoa <slug> ... --aprovado-por <dono>` | registra um stakeholder em `10_<org>/pessoas/` (só com OK do dono) |
