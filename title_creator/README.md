# Criador de títulos

Execute `iniciar_titulos.bat` na raiz do tracker. A interface abre em http://127.0.0.1:8765. Mantenha a janela do servidor aberta durante o uso. Requer Python 3.10+.

Alternativa no terminal, a partir da raiz:

```powershell
python -m pip install -r title_creator/requirements.txt
python -m title_creator.server --open
```

## Uso

Cole um resumo, selecione o idioma e de 5 a 10 sugestões. Informe fatos importantes e spoilers a evitar. Cada resultado inclui ângulo, justificativa, fatos da história e links de referência. Rascunhos ficam no armazenamento local do navegador; resultados não são gravados pelo servidor.

O modelo é fixado em `gpt-6-astra`, com raciocínio médio, pela Responses API oficial. Não existe troca silenciosa por outro modelo. A API é cobrada na conta da chave, separadamente da assinatura do ChatGPT. O catálogo completo e o resumo são enviados à OpenAI em cada geração; `store=false` desativa o armazenamento da resposta pela API, mas não constitui promessa de retenção zero.

## Chave

O servidor lê `OPENAI_API_KEY` ou, na ausência dela, `rewrite.api_key` no arquivo `../momo-rewrite/config.yaml`, somente quando o provedor é `openai`. Para outro caminho, use `MOMO_REWRITE_CONFIG`. A configuração do momo-rewrite não é alterada. A chave nunca é copiada para este repositório, retornada à interface ou incluída em logs.

## Biblioteca e atualização

`data/library.csv` contém títulos reais públicos e a procedência da coleta. A sincronização lê somente a aba `todos` da planilha configurada em `core.py`; não altera a planilha. A exportação CSV precisa estar acessível para leitura. Se esse acesso mudar, a biblioteca local continua utilizável.

- Deduplica por ID de vídeo e seleciona views **estritamente maiores que 200.000**. Duplicatas conservam a maior contagem observada.
- Views são **acumuladas** no snapshot da planilha. Não representam ganhos mensais, nem views atualizadas pela coleta de títulos.
- Títulos vêm do endpoint público YouTube oEmbed, sem precisar de outra chave. Vídeos indisponíveis são registrados com erro e excluídos da geração. A data da coleta do título é separada da data da coleta das views.
- Uma amostra de até 80 vídeos abaixo ou iguais ao corte é distribuída entre canais e faixas de idade, excluindo vídeos com menos de 7 dias. É uma comparação exploratória, não um experimento causal.
- `peer_ratio` divide views pela mediana de **outros** vídeos do mesmo canal na mesma faixa de idade (0–7, 8–30, 31–90, 91–180, 181–365, 366+ dias), somente com pelo menos 5 pares e mediana positiva. Usa todos os registros válidos da planilha, antes da seleção do catálogo.
- Tags são classificações heurísticas por palavras, não avaliações humanas nem conclusões sobre eficácia. O Astra recebe os títulos completos, revisa as categorias pelo sentido e escolhe referências semanticamente compatíveis. Um título pode ter múltiplas tags.
- O modelo deve variar os ângulos, respeitar fatos/spoilers e citar IDs existentes. O servidor verifica quantidade, títulos únicos com até 100 caracteres e referências pertencentes ao conjunto de vencedores. Fidelidade semântica depende também da revisão humana.
- Um vídeo popular não prova que seu título causou o sucesso. Títulos atuais podem diferir dos usados durante o crescimento. Canal, idade, obra, thumbnail e distribuição continuam sendo fatores de confusão.

O botão **Atualizar biblioteca** atualiza as views da planilha, inclui novos vídeos e tenta novamente títulos ausentes. Títulos já coletados são reutilizados. Para consultar todos os títulos novamente:

```powershell
python -m title_creator.server --sync --refresh-titles
```

A atualização salva o CSV de forma atômica; falhas de leitura não apagam a biblioteca anterior. O servidor aceita uma operação de geração ou atualização por vez. Serve apenas três arquivos estáticos explícitos, usa token de sessão para operações e escuta exclusivamente em loopback. Não foi projetado para publicação na internet.

## Validação editorial

Teste histórias diferentes (regressão, cura, artesanato, vingança, sobrevivência, romance, academia, sistema, política e comédia). Para cada conjunto, verifique: fatos preservados, spoilers respeitados, ângulos distintos, idioma correto, título publicável e referência pertinente. Registre quais opções você escolheria antes de avaliar resultados reais de publicação. Não há pontuação automática de viralização.

Testes automatizados sem chamadas pagas:

```powershell
python -m pytest tests/test_title_creator.py
```
