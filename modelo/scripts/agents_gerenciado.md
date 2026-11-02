<!-- susano:inicio | gerenciado pelo modelo Susano: não edite aqui; `python3 scripts/brain.py migrar` reescreve a cada versão. Regra local vai em "Regras próprias", abaixo. -->
## Regras do Susano (agentes e pessoas)

1. Nunca commit na `main`: branch e PR; ninguém faz merge do próprio PR.
2. `python3 scripts/brain.py validate` antes de cada commit; `susano-check` antes do PR.
3. Uma frente por vez: número, ICP, meta ou decisão de uma frente nunca aparece em outra; comparação só a pedido, rotulada por frente.
4. Marcadores literais ([DADO], [INFERÊNCIA], [VERIFICAR], [LACUNA], [DADO PENDENTE], [CONTRADIÇÃO], [SENSÍVEL]); número com unidade, período, fonte e data; nenhum travessão.
5. Nunca entram credencial, CPF, cartão, telefone ou e-mail pessoal. Contrato, fee e financeiro de cliente ficam fora, salvo se as Regras próprias liberarem (repositório privado, decisão do dono). Stakeholder entra em `10_<org>/pessoas/` só com OK do dono (`brain.py pessoa ... --aprovado-por`): papel e relação, nunca contato.
6. Ação em sistema externo (enviar, publicar, submeter, deletar) só com aprovação explícita da pessoa.
7. Gerenciados (lista em `CONVENCOES.md`) e este bloco só mudam por versão do modelo. As Regras próprias prevalecem sobre os padrões deste bloco quando o dono decide, nunca para liberar credencial, CPF, cartão ou contato pessoal.

## Como usar o Susano

O Claude Code carrega o núcleo pelo `CLAUDE.md` e o método pelas skills. Outro agente lê, nesta ordem:

1. `00_susano/nucleo.md` inteiro: identidade, P-01 a P-06, tom e formato.
2. `00_susano/situacoes.md` (pedido → modo → o que abrir) e `00_susano/calibracao.md` (agir ou perguntar).
3. `MAPA.md` e `10_<org>/hot.md` (gerados por `brain.py mapa` e `hot`).
4. Da frente: `contexto.md`, `estado.md`, `decisoes.md` e `experimentos.md`.
5. O índice do domínio em `.claude/skills/susano-*/SKILL.md`, depois só o arquivo que a tarefa pede; cite `caminho#seção`. Antes de produzir, o exemplo do modo em `00_susano/exemplos/`.
6. Combinado, decidido ou medido: `python3 scripts/brain.py fonte "<termo>" --frente <slug>` (`--todas` só em comparação pedida); sem ocorrência é [LACUNA].
7. Ao encerrar: salve como `00_susano/metodo/salve.md` manda, rode `mapa`, `hot` e `validate`, PR na branch `salve/AAAA-MM-DD-<tema>`.

Sem shell: os mesmos arquivos na mesma ordem; entrega no chat e fecha com a lista do que salvar e onde (arquivo e seção). Nunca inventa o conteúdo de arquivo que não leu.
<!-- susano:fim -->
