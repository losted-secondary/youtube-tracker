const $ = id => document.getElementById(id);
const storageKey = 'momo-title-creator-v1';
let token = '', busy = false, syncing = false, lastResult = null, toastTimer;
const fields = ['story', 'constraints', 'count', 'language'];
function save() { try { localStorage.setItem(storageKey, JSON.stringify(Object.fromEntries(fields.map(k => [k, $(k).value])))); } catch {} }
try { const draft = JSON.parse(localStorage.getItem(storageKey) || '{}'); for (const k of fields) if (typeof draft[k] === 'string') $(k).value = draft[k]; } catch {}
function counter() { $('counter').textContent = `${$('story').value.length.toLocaleString('pt-BR')} / 12.000`; }
fields.forEach(k => $(k).addEventListener('input', () => { save(); counter(); })); counter();
function message(text) { $('toast').textContent = text; $('toast').hidden = false; clearTimeout(toastTimer); toastTimer = setTimeout(() => $('toast').hidden = true, 2500); }
async function copy(text) { try { await navigator.clipboard.writeText(text); message('Copiado!'); } catch { message('Não foi possível copiar. Selecione o texto e use Ctrl+C.'); } }
function el(tag, text, className) { const node = document.createElement(tag); if (text !== undefined) node.textContent = text; if (className) node.className = className; return node; }
function controls() { $('generate').disabled = busy || syncing || !token; $('sync').disabled = busy || syncing || !token; }
async function status() {
  try {
    const response = await fetch('/api/status'); if (!response.ok) throw Error(); const data = await response.json(); token = data.token; syncing = data.syncing;
    $('library-count').textContent = `${data.winners} títulos acima de 200 mil views`;
    const date = data.updated_at ? new Date(data.updated_at).toLocaleString('pt-BR') : 'ainda não atualizada';
    $('library-detail').textContent = `${data.controls} vídeos de comparação. ${data.missing} sem título disponível. ${data.errors} consultas com falha. Atualizada em ${date}.`;
    $('patterns').replaceChildren(...Object.entries(data.patterns).map(([name, count]) => el('span', `${name}: ${count}`)));
    $('sync-state').textContent = data.error || data.message;
    if (!data.configured) { $('error').textContent = 'Chave OpenAI não encontrada. Configure a chave no servidor para gerar.'; $('error').hidden = false; }
    controls(); if (syncing) setTimeout(status, 2000);
  } catch { $('error').textContent = 'Não foi possível conectar ao servidor local. Abra iniciar_titulos.bat e atualize a página.'; $('error').hidden = false; }
}
function render(result) {
  $('cards').replaceChildren(); $('reading').textContent = result.story_reading; $('reading').hidden = false;
  $('cautions').replaceChildren(...result.cautions.map(text => el('li', text))); $('cautions').hidden = !result.cautions.length;
  for (const suggestion of result.suggestions) {
    const card = el('article', undefined, 'title-card'); const top = el('div', undefined, 'card-top');
    const button = el('button', 'Copiar', 'text-button'); button.type = 'button'; button.addEventListener('click', () => copy(suggestion.title));
    top.append(el('span', suggestion.angle), button); card.append(top, el('h3', suggestion.title), el('p', suggestion.why));
    const details = el('details'); details.append(el('summary', `Por trás do título · ${suggestion.references.length} referência(s)`), el('p', `Na sua história: ${suggestion.story_evidence}`));
    for (const ref of suggestion.references) {
      const block = el('div', undefined, 'reference'); const link = el('a', ref.title); link.href = ref.url; link.target = '_blank'; link.rel = 'noopener noreferrer';
      block.append(link, el('small', `${ref.channel} · ${ref.views.toLocaleString('pt-BR')} views na coleta${ref.peer_ratio ? ` · ${Number(ref.peer_ratio).toLocaleString('pt-BR')}× a mediana de vídeos de idade semelhante no canal` : ''}`)); details.append(block);
    }
    card.append(details); $('cards').append(card);
  }
  $('copy-all').hidden = false; $('result-note').hidden = false;
}
$('example').addEventListener('click', () => {
  $('story').value = 'Um jovem curandeiro é expulso de sua equipe por não conseguir lutar. Sozinho, ele descobre que sua magia de cura também consegue restaurar armas antigas. Ele começa a recuperar equipamentos abandonados para sobreviver e decide abrir uma oficina. Seu objetivo é conquistar independência, sem voltar para a equipe que o rejeitou.';
  $('constraints').value = 'Não inventar poderes de combate nem vingança. Não revelar o destino final da oficina.'; save(); counter(); $('story').focus();
});
$('copy-all').addEventListener('click', () => lastResult && copy(lastResult.suggestions.map(s => s.title).join('\n')));
$('sync').addEventListener('click', async () => {
  syncing = true; controls(); $('sync-state').textContent = 'Iniciando atualização…';
  try { const r = await fetch('/api/sync', {method:'POST', headers:{'Content-Type':'application/json','X-Session-Token':token}, body:'{}'}); const d = await r.json(); if (!r.ok) throw Error(d.error); await status(); }
  catch (e) { syncing = false; controls(); $('sync-state').textContent = e.message; }
});
$('form').addEventListener('submit', async event => {
  event.preventDefault(); if (busy || syncing) return; busy = true; controls(); save();
  $('error').hidden = true; $('empty').hidden = true; $('loading').hidden = false; $('cards').hidden = true; $('reading').hidden = true; $('cautions').hidden = true; $('copy-all').hidden = true; $('result-note').hidden = true; document.querySelector('.results').setAttribute('aria-busy','true');
  const start = Date.now(); $('elapsed').textContent = '0 s'; const timer = setInterval(() => $('elapsed').textContent = `${Math.floor((Date.now()-start)/1000)} s`, 1000);
  try {
    const response = await fetch('/api/generate', {method:'POST',headers:{'Content-Type':'application/json','X-Session-Token':token},body:JSON.stringify({story:$('story').value, constraints:$('constraints').value, count:Number($('count').value),language:$('language').value})});
    const result = await response.json(); if (!response.ok) throw Error(result.error || 'Falha ao gerar títulos.'); lastResult = result; render(result);
  } catch (error) { $('error').textContent = error.message || 'Conexão perdida. Tente novamente.'; $('error').hidden = false; if (lastResult) render(lastResult); else $('empty').hidden = false; }
  finally { clearInterval(timer); busy = false; controls(); $('loading').hidden = true; $('cards').hidden = false; document.querySelector('.results').setAttribute('aria-busy','false'); }
});
status();
