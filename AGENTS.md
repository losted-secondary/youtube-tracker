# Regras para qualquer IA mexendo neste repo

Duas pessoas editam este projeto, cada uma no seu PC. Para não dar conflito no push:

1. **Antes de alterar qualquer arquivo**, rode `git pull --rebase --autostash`.
   Se der conflito, resolva (ou avise o usuário) ANTES de fazer a alteração pedida.
2. **Terminou a alteração**: commit e `git push` na hora. Não deixe mudança parada sem push.
3. Se o push for recusado porque o remoto andou: `git pull --rebase --autostash` e push de novo.
