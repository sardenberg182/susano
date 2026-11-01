# Plugin susano (Claude Code)

A sombra do Sarden como plugin do Claude Code: o método, o DNA, a biblioteca e as referências de growth e RevOps de Matheus Sardenberg (Sarden) dentro do projeto que você já tem, sem mudar a estrutura dele. Gerado por `ferramentas/construir_plugin.py` a partir de `modelo/00_susano/`; não editar à mão.

## Instalar

Na sessão do Claude Code:

```
/plugin marketplace add sardenberg182/susano
/plugin install susano@susano
```

No terminal: `claude plugin marketplace add sardenberg182/susano` e `claude plugin install susano@susano`. Para testar a partir de um clone, sem instalar: `claude --plugin-dir ./plugin`.

Depois: `/output-style Susano` ativa o estilo de resposta (opcional; o tom já vem no núcleo).

## O que carrega quando

- Sempre ligado: o núcleo (`00_susano/nucleo.md`, cerca de 2 mil tokens), injetado na abertura da sessão pelo hook `hooks/abrir.py`, mais as descrições das skills e do subagente. `claude plugin details susano` mostra a projeção.
- Sob demanda: as skills `susano-ativos`, `susano-metodo`, `susano-biblioteca`, `susano-performance`, `susano-analytics`, `susano-gtm`, `susano-plataformas`, `susano-rituais` e `susano-analise`. Cada uma é um índice que aponta o arquivo certo em `00_susano/`; o Susano abre só esse arquivo e cita caminho e seção.
- Subagente `susano:pesquisador`: evidência com caminho, sobre o método e sobre os documentos do projeto.

## O que não vem no plugin

A estrutura de segundo cérebro (pastas de organização e frentes, `brain.py`, guardas de escrita, CI, `MAPA.md`, `hot.md`): isso é o template Copier do mesmo repositório (`copier copy gh:sardenberg182/susano <pasta>`). O plugin é a sombra; o template é o cérebro completo.

## Licença e autoria

Conteúdo (método, DNA, biblioteca, referências) sob CC BY 4.0; código sob MIT. Copyright (c) 2026 Matheus Sardenberg (Sarden). Crédito ao usar: "Baseado no Susano, de Matheus Sardenberg (Sarden), CC BY 4.0. Adaptado." Versão 0.2.1.
