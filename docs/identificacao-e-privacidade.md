# Testar identificação e manter o tracker privado

## Retomada e piloto Dots — 11/10/2026

Instruções atuais: [dot-tracker.md](dot-tracker.md). `--first-missing` agora escolhe
somente vídeos dos últimos sete dias. O catálogo contém os dez resultados iniciais
e quatro novas identificações do piloto (linhas originais 17, 19, 20 e 21).

O primeiro teste real no GitHub falhou na extração do YouTube. Foi habilitado Node
no yt-dlp e instalado seu pacote de componentes JS. Quando a extração continua
bloqueada, a coleta usa a YouTube Data API existente para descrição e comentários;
nesse caso o relatório informa a ausência de falas e frames. O workflow corrigido
passou em https://github.com/losted-secondary/youtube-tracker/actions/runs/38166014283.
As quatro identificações foram feitas pelo agente desta sessão; o dot ainda precisa
ser criado na conta autenticada. Nenhum agendamento do dot foi criado pelo script.

## O que foi preparado

- `investigate.js`: comando Node.js que coleta pistas de UM vídeo para revisão pelo Dots.
- `collect_evidence.py`: consulta descrição, até 120 comentários/respostas, partes vinculadas (até 2), legendas iniciais e frames. Usa yt-dlp; acesso ao YouTube pode falhar e não é garantido.
- `reviewed_identifications.py`: catálogo dos nove resultados anteriores e do novo teste (The Ruler of Darkness), por ID de vídeo e com evidência.
- `apply_reviewed.py`: grava somente os nomes revisados nas células vazias da aba todos, com notas de evidência; preserva títulos e aliases já preenchidos.
- `main.py`: reaplica de forma idempotente esse catálogo em cada sync e continua procurando comentários do dono quando o primeiro não contém título.
- Workflow `investigate-one-video`: teste manual que entrega um artifact com relatório e imagens, sem editar a planilha nem enviar mensagens.
- Workflow `apply-reviewed`: grava os dez resultados usando a conta de serviço já configurada no GitHub. Começa em dry-run por padrão.

Os workflows que escrevem no Sheets compartilham um grupo de concorrência. Isso evita sobreposição entre esses jobs GitHub, mas não bloqueia edições manuais ou scripts externos. O catálogo contém apenas resultados públicos e os dez IDs investigados, nunca credenciais.

## Teste local

Pré-requisitos: Node 22, Python 3.11+ e, para frames completos, ffmpeg no PATH.

```powershell
cd C:\Users\victo\youtube-tracker
python -m pip install -r requirements-investigate.txt
node investigate.js --video https://youtu.be/j_lwugWFCps --out artifacts/primeiro-teste
```

O comando cria `report.md`, `report.json` e imagens em `artifacts/primeiro-teste`. Não precisa de chave de IA nem da conta de serviço para investigar um link público. `--no-frames` faz um teste mais rápido. Frames em 20/40/80s são pontos iniciais; o Dots deve trocar os pontos se houver vinheta ou cena pouco útil.

Para selecionar o primeiro vídeo ainda sem nome diretamente do Sheets:

```powershell
node investigate.js --first-missing --out artifacts/primeiro-sem-nome
```

Esse modo usa `GOOGLE_CREDENTIALS_JSON` em variável de ambiente e precisa das dependências do projeto. No GitHub Actions o secret existente já é fornecido. Não copiar credenciais para arquivos rastreados nem mensagens.

## Testar pelo GitHub, sem instalar nada no PC

1. Abrir Actions > `investigate-one-video` > Run workflow.
2. Informar o link desejado; deixar vazio seleciona o primeiro sem nome no Sheets.
3. Esperar concluir e baixar o artifact `investigation`.
4. Passar o relatório e frames ao Dots. Pedir pesquisa e confirmação com nomes de personagens, sinopse ou mesmo painel em capítulo.

O JS coleta candidatos e evidências; NÃO implementa reconhecimento visual nem busca reversa, NÃO chama o modelo automaticamente e NÃO decide que uma sugestão é confirmada. O Dots faz a investigação sobre o material. Google Lens foi testado separadamente e bloqueou a busca por verificação de tráfego. Não depender dessa etapa como solução autônoma validada.

Teste executado em 11/10/2026: `j_lwugWFCps` não trouxe título explícito nem comentários na coleta. O JS extraiu legendas e três frames. A pesquisa posterior pelas pistas identificou **The Ruler of Darkness**, corroborado pelo mesmo painel no capítulo 1. O resultado foi então incluído no catálogo revisado; não foi uma decisão automática do regex.

Instrução inicial para o Dots:

> Neste repositório, execute `node investigate.js --first-missing`. Se não houver credenciais locais, leia o primeiro vídeo sem obra na aba todos pelo Google Drive conectado e passe o link com `--video`. Leia o relatório e as imagens. Pesquise os candidatos e confirme por personagens/enredo ou painel idêntico. Guarde fontes e timestamps. Se não houver confirmação, mantenha pendente e revise em 3h, 24h, 72h e 7 dias. Nunca escreva candidato como título definitivo. Use os recursos incluídos no plano; não contrate API ou serviço. Comece com um único vídeo e me apresente o resultado.

O arquivo registra a próxima tentativa proposta, mas NÃO agenda uma tarefa no Dots. Configurar recorrência na interface do Dots após testar. Para gravar novos resultados, acrescentar ao catálogo revisado ou usar uma conexão Sheets com acesso de Editor. A integração Google desta sessão retornou HTTP 403, acesso de comentarista; a conta de serviço do tracker pode ter autorização de Editor independente.

## Por que público funcionou e privado pode ter falhado

O tracker não usa GitHub Pages nem arquivos públicos como mecanismo de sincronização. É Python no GitHub Actions, acionado por Apps Script a cada 10 minutos, com credenciais Google e YouTube em Secrets. Portanto, a visibilidade pública NÃO é exigência do código.

Não há no repositório o Apps Script real com seu token, nem acesso ao faturamento do dono. A causa histórica ainda não está confirmada. Conferir:

1. **Token do Apps Script**: um token que acessava só repositórios públicos pode falhar no privado. Usar token fine-grained com o proprietário correto, este repositório selecionado e `Actions: Read and write`; atender políticas de aprovação/SSO se aplicáveis. Token classic para repo privado requer escopo `repo`. Não publicar o token.
2. **Quota do Actions**: padrão público é gratuito; privado tem franquia. O plano GitHub Free inclui 2.000 minutos/mês; o Pro do GITHUB inclui 3.000 (independente do ChatGPT Pro). Cada job arredonda para um minuto inteiro. Em 30 dias, um gatilho a cada 10 minutos gera 4.320 jobs, pelo menos 4.320 minutos, mesmo que cada job leve 28 segundos. Estoura ambas as franquias. Sem faturamento permitido, os jobs podem parar.
3. **Permissões/configuração**: Actions habilitado no repo privado, secrets presentes, branch/workflow correto, checkout com `contents: read`. Aceitar um dispatch não garante que o runner tenha iniciado.

Diagnóstico: olhar Apps Script > Execuções para HTTP do dispatch; 401 aponta token inválido, 404 pode ocultar falta de acesso privado, 403 aponta permissão/política. Se o dispatch é aceito mas o job não inicia, verificar Actions e Billing do dono. As execuções recentes consultadas estavam funcionando a cada 10 minutos; isso não identifica a falha anterior.

Alternativas: repo privado com faturamento de Actions aprovado pelo dono; runner próprio; ou reduzir a frequência. Não mudar para 30/60 minutos sem ajustar e validar a lógica de varredura completa em `main.py`, hoje baseada em cair nos primeiros 10 minutos da hora. A configuração de faturamento e visibilidade não foi alterada.

`docs/apps-script-trigger.gs` é um modelo seguro de dispatch e diagnóstico, com token em Script Properties. Para usar: Extensões > Apps Script na planilha, criar arquivo, colar conteúdo e configurar as propriedades. Rodar `diagnosticarTracker` e depois `chamarTracker` uma vez. Não criar um segundo gatilho periódico enquanto o antigo estiver ativo.

Fontes:
- https://docs.github.com/en/billing/concepts/product-billing/github-actions
- https://docs.github.com/en/actions/how-tos/monitor-workflows/view-job-execution-time
- https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event
- https://developers.google.com/youtube/v3/docs/commentThreads

## Custos do piloto

Nenhuma API de IA paga é necessária para os scripts. Pesquisa do Dots usa os limites do plano ChatGPT; GitHub privado tem custos/franquias próprios. O workflow de investigação é manual para não adicionar consumo recorrente até validar o fluxo. WhatsApp e monitoramento de sites ainda não foram configurados nesta etapa.
