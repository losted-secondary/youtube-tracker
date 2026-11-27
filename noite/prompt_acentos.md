MODO AUTÔNOMO: não pergunte nada, não use skills. Pasta: C:\Users\victo\Desktop\momo-apps\tracker
NUNCA rode git (nada de add/commit/push). Só edite os dois arquivos abaixo.

Os arquivos artifacts\cacador\notas_agente.json e artifacts\cacador\dossies.json foram gravados com a
codificação errada: as letras acentuadas do português viraram '?' (ex.: "Ap?s", "invenc?vel", "Vingan?a",
"ingl?s", "h?", "?ltimo"). Restaure a acentuação correta de TODOS os textos em português (campos premissa,
porque, risco, youtube, dossie e quaisquer outros), deduzindo pela palavra. NÃO mude o conteúdo, números,
nomes de obras, links nem as chaves. Pontos de interrogação de verdade (fim de pergunta) ficam.
Leia e grave com Python: json.load(open(p, encoding='utf-8')) e
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1).
Trabalhe em blocos e confira no fim que não sobrou '?' no meio de palavra. Responda só "FEITO".
