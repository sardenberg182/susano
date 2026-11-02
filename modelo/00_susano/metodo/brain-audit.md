---
id: metodo-brain-audit
tipo: procedimento
atualizado: 2026-10-31
fonte: modelo de segundo cérebro adaptado pelo Sarden
---

# Brain audit: a poda mensal

## 1. Base mecânica

`python3 scripts/brain.py audit`: estados frios (mais de 14 dias), frentes sem dono, projetos parados há mais de 90 dias, revisões vencidas (`revisar_ate`). Somar os avisos de `brain.py validate` (links quebrados, dados que parecem pessoais).

## 2. Passe qualitativo

- Contradições entre arquivos da mesma frente ou entre playbook e prática registrada.
- Decisões substituídas ainda tratadas como atuais.
- Arquivos duplicados ou quase iguais em `40_playbooks/` e `50_referencia/`: fundir numa fonte só.
- Skills sem uso há 30 dias → standby; há 90 dias → arquivo. Nunca excluir.
- Referências com data de produto vencida (preço, limite, cota): marcar [VERIFICAR].
- Propostas para o modelo paradas há mais de 30 dias: lembrar o dono.

## 3. Relatório

`10_<org>/auditorias/AAAA-MM_brain-audit.md`: FATO (contagens) → achados concretos com caminho → PA com dono e prazo. Relatório que diz "está tudo bem" sem contagens não vale.

## 4. Correções

Cada correção vai num PR separado por área, para cada dono revisar só a sua parte.
