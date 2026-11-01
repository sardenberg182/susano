---
id: metodo-migrar-frente
tipo: procedimento
atualizado: 2026-10-31
fonte: raio_doc14 e raio_doc16 (migração do Susano antigo)
---

# Migrar uma frente: do contexto antigo para a pasta da frente

Para trazer o contexto de uma frente que vivia fora do repositório (por exemplo, arquivos de um Project do claude.ai).

1. Criar a pasta com `python3 scripts/brain.py novo <slug> --dono <usuário>` se ela não existir.
2. Mapear o material antigo para as seções do `contexto.md` (modelo em `_templates/contexto_projeto.md`): identificação, produto, ICP, funil e métricas, canais, time, GP atual, histórico, contexto da organização.
3. O que está aberto vai para `estado.md`; decisões com data vão para `decisoes.md`; fatos datados viram linhas de ledger com a referência ao arquivo antigo.
4. Fato antigo sem confirmação recente leva [VERIFICAR] com a data da fonte. Métrica sem fonte vira [DADO PENDENTE]; nunca copiar número sem origem.
5. Nenhum dado pessoal bruto, valor de contrato ou fee. Contato do cliente aparece só com nome e papel.
6. Um PR por frente, para o dono revisar só a sua.
