// Modelo sem segredos. Configure em Configurações do projeto > Propriedades do script:
// GITHUB_TOKEN, GITHUB_OWNER, GITHUB_REPO e opcionalmente GITHUB_REF (padrão main).
// NÃO substituir o gatilho atual antes de validar diagnosticarTracker().

function trackerConfig_() {
  const props = PropertiesService.getScriptProperties();
  const token = props.getProperty('GITHUB_TOKEN');
  const owner = props.getProperty('GITHUB_OWNER');
  const repo = props.getProperty('GITHUB_REPO');
  if (!token || !owner || !repo) throw new Error('Configure as propriedades GITHUB_TOKEN, GITHUB_OWNER e GITHUB_REPO.');
  return { token, owner, repo, ref: props.getProperty('GITHUB_REF') || 'main' };
}

function chamarTracker() {
  const cfg = trackerConfig_();
  const endpoint = 'https://api.github.com/repos/' + encodeURIComponent(cfg.owner) + '/' +
    encodeURIComponent(cfg.repo) + '/actions/workflows/sync.yml/dispatches';
  const response = UrlFetchApp.fetch(endpoint, {
    method: 'post', contentType: 'application/json',
    headers: { Authorization: 'Bearer ' + cfg.token, Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28' },
    payload: JSON.stringify({ ref: cfg.ref }), muteHttpExceptions: true,
  });
  const code = response.getResponseCode();
  if (code !== 204) {
    // Não imprimir token nem cabeçalhos.
    throw new Error('GitHub dispatch HTTP ' + code + '. 401: token inválido/expirado; ' +
      '404: repo/ref/workflow ou acesso privado; 403: permissão/política; 422: configuração.');
  }
  console.log('Workflow aceito pelo GitHub. Conferir a execução em Actions; aceitação não garante sucesso do job.');
}

function diagnosticarTracker() {
  const cfg = trackerConfig_();
  const endpoint = 'https://api.github.com/repos/' + encodeURIComponent(cfg.owner) + '/' + encodeURIComponent(cfg.repo);
  const response = UrlFetchApp.fetch(endpoint, {
    headers: { Authorization: 'Bearer ' + cfg.token, Accept: 'application/vnd.github+json' },
    muteHttpExceptions: true,
  });
  const code = response.getResponseCode();
  console.log('Leitura autenticada do repositório: HTTP ' + code);
  if (code === 200) {
    const repo = JSON.parse(response.getContentText());
    console.log('Privado: ' + repo.private + '; branch padrão: ' + repo.default_branch);
  } else {
    console.log('Token ou acesso ao repositório precisa ser corrigido.');
  }
}
