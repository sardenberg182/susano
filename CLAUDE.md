@AGENTS.md

# Claude Code neste repositório

Você está no repositório do modelo Susano, não num projeto gerado por ele. Mantenha o modelo; não aplique o Susano aqui.

- Leia `modelo/00_susano/nucleo.md` antes de mexer em identidade, tom ou skills: ele é o que todo projeto e todo plugin carregam na abertura (teto de 2 mil tokens, `brain.py validate` barra acima disso).
- Mudança no método é mudança em `modelo/00_susano/`; depois regenere (`indice`, `skills`, `manifesto`, `construir_plugin.py`) e rode os dois testes. Nunca edite os gerados.
- `modelo/CLAUDE.md` é o CLAUDE.md dos projetos gerados: ao trabalhar dentro de `modelo/`, ele também carrega; as instruções dele valem para o projeto, não para este repositório.
- Push, tag e criação de repositório no GitHub só com o OK explícito do Sarden na mesma conversa.
