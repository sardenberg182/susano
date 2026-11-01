# AGENTS: repositório susano (o modelo, não um projeto)

Este repositório é a fonte do Susano: um template Copier (`modelo/`) e um plugin do Claude Code (`plugin/`), gerados da mesma fonte, `modelo/00_susano/`. Quem abre este repositório com um agente está mantendo o modelo, não usando o Susano num projeto: para isso, veja o `README.md`.

- Dono: Matheus Sardenberg (Sarden). O Raijin propõe mudanças; o Sarden aprova. Nenhum merge sem o OK dele.
- Fonte única: conteúdo do método só em `modelo/00_susano/`. `modelo/00_susano/INDICE.md`, `ATIVOS.md`, `MANIFEST.sha256`, `modelo/.claude/skills/susano-*/` e `plugin/` são gerados; nunca edite à mão.
- Regenerar depois de qualquer mudança em `modelo/`: `python3 modelo/scripts/brain.py --raiz modelo indice`, `skills`, `manifesto`; depois `python3 ferramentas/construir_plugin.py`.
- Testar antes de propor: `bash testes/testar_modelo.sh` (gera um projeto temporário e roda validate, susano-check e os 50 casos de `testar_camada.py`) e `bash testes/testar_plugin.sh`.
- Versão: linha nova no topo do `CHANGELOG.md` (a versão do plugin é lida dali), `README.md` com a tag nova, tag `vX.Y.Z` só depois dos testes.
- Convenções do conteúdo: PT-BR com termos técnicos em inglês; corpo de skill, agente e estilo em inglês; nenhum travessão em arquivo nenhum (`grep -rn` do caractere U+2014); marcadores [DADO], [INFERÊNCIA], [VERIFICAR], [LACUNA], [CONTRADIÇÃO], [SENSÍVEL]; todo fato de produto com data.
- Privacidade: nenhum dado de cliente, nome ligado à operação do Sarden, e-mail, telefone, credencial ou ID real entra aqui. O nome civil do Sarden aparece só em copyright, `sobre_o_sarden.md` e autoria do plugin. A Oficina (persona) é outro repositório e nunca entra neste.
- Textos aprovados pelo Sarden (`identidade.md` v0.1.6, `sobre_o_sarden.md`, os 8 DNAs, a licença) só mudam com nova aprovação dele, registrada no frontmatter `aprovado:`.
