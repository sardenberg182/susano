# Exceções da inspeção de privacidade (repositório susano, perfil público)

Lido por `python3 modelo/scripts/brain.py --raiz . varrer --perfil publico` no CI. No perfil público, telefone, e-mail e formato que não dá para inspecionar barram; esta tabela libera só o que é fixture ou exemplo fictício, um arquivo exato por linha, com motivo. Segredo, cartão e CPF nunca têm exceção: o teste monta o valor em tempo de execução. Exceção do próprio método (vale também nos projetos) fica em `EXCECOES_GERENCIADAS`, no `brain.py`.

| regra | caminho | motivo |
|---|---|---|
| telefone | testes/rodar_casos.py | caso C-15: telefone fictício na entrada, para medir se o Susano recusa gravar contato em pessoas/ |
