#!/usr/bin/env node
'use strict';

// CLI para o Dots: prepara evidências; não usa API paga nem escreve na planilha.
const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');

function candidates(text) {
  const clean = String(text || '').normalize('NFKC').replace(/\u200b/g, '');
  const result = [];
  for (const line of clean.split(/\r?\n/)) {
    const patterns = [
      /^\s*(?:manhwa|manhua|manga|novel)\s*[:—–-]\s*(.+)$/i,
      /^\s*[^\w]*(?:(?:manhwa|manhua|manga|novel|series)\s+)?(?:name|title)(?:\s+of\s+the\s+series)?\s*[:—–-]\s*(.+)$/i,
      /(?:the\s+)?name\s+of\s+(?:the\s+)?(?:novel|manhwa|manga|series|story)(?:\s+he\s+is\s+animating)?\s+is\s+(.+)$/i,
      /(?:novel|manhwa|manga|series|story)\s+(?:is\s+)?called\s+(.+)$/i,
    ];
    for (const pattern of patterns) {
      const match = line.match(pattern);
      if (!match) continue;
      const name = match[1].trim().replace(/^["“']|["”']$/g, '').trim();
      if (name.length < 3 || name.length > 180 || /^(?:https?:|manhwa recap)/i.test(name) ||
          /in the comments?|pinned|see below|unknown|\?$|^(?:please|pls|bro|what|qual|nome)\b/i.test(name)) continue;
      if (!result.includes(name)) result.push(name);
    }
  }
  return result;
}

function prepare(data, now = new Date()) {
  const suggestions = [];
  for (const video of [data.primary, ...(data.related || [])]) {
    const sources = [{ text: video.description, type: 'description', url: video.url },
      ...(video.comments || []).map(c => ({ text: c.text, type: c.is_owner ? 'owner_comment' : 'viewer_comment',
        url: `${video.url}&lc=${encodeURIComponent(c.id || '')}` }))];
    for (const source of sources) {
      for (const title of candidates(source.text)) {
        suggestions.push({ title, source: source.type, evidence_url: source.url, text: source.text,
          source_video_id: video.video_id, status: 'provavel' });
      }
    }
  }
  return { ...data, collected_at: now.toISOString(), candidates: suggestions,
    status: suggestions.length ? 'candidatos_para_validar' : 'aguardando_pistas',
    next_check_at: new Date(now.getTime() + 3 * 3600 * 1000).toISOString(),
    writes_performed: false };
}

function markdown(report) {
  const p = report.primary;
  const lines = [`# Investigação: ${p.video_id}`, '', p.title, '', p.url, '',
    `Status: ${report.status}. Nenhuma célula alterada.`,
    `Coleta: ${report.collected_at}. Próxima revisão proposta: ${report.next_check_at}.`, '',
    '## Candidatos extraídos por texto — precisam de validação', ''];
  if (!report.candidates.length) lines.push('Nenhum título explícito extraído. Usar frames e falas abaixo.');
  for (const c of report.candidates) lines.push(`- **${c.title}** (${c.source}): ${c.evidence_url}`);
  for (const v of [p, ...(report.related || [])]) {
    lines.push('', `## Vídeo ${v.video_id}`, '', v.url, '', '### Descrição', '', v.description || '(vazia)',
      '', '### Falas dos primeiros três minutos', '', v.transcript || '(não disponíveis)', '',
      `### Comentários relevantes (${v.comments_sampled || 0} comentários/respostas consultados)`, '');
    const relevant = (v.comments || []).filter(c => c.is_owner ||
      /name|title|sauce|source|called|novel|nome|qual|manga|manhwa/i.test(c.text));
    for (const c of relevant) lines.push(`- ${c.text.replace(/\n/g, ' ')} — ${v.url}&lc=${encodeURIComponent(c.id || '')}`);
    if (v.preview) lines.push('', '### Prévia do começo', '', `![Prévia](${v.preview})`);
    for (const f of v.frames || []) lines.push('', `### Frame aos ${f.seconds}s`, '', `![Frame](${f.file})`);
    for (const error of v.errors || []) lines.push('', `Limitação: ${error}`);
  }
  lines.push('', '## Próximos passos para o Dots', '',
    '1. Validar candidatos com personagens e sinopse; comentários não confirmam sozinhos.',
    '2. Se não houver título, ler/observar frames e falas; pesquisar duas pistas específicas.',
    '3. Comparar os painéis com capítulos candidatos. Guardar timestamp, capítulo e link.',
    '4. Busca reversa é opcional: Google Lens pode exigir intervenção e ainda não foi validado neste ambiente.',
    '5. Se for novel ilustrada com IA, priorizar texto e partes anteriores.',
    '6. Não gravar hipótese em obra. Sem confirmação, revisar em +3h, +24h, +72h e +7d; depois pedir revisão manual.',
    '7. Este arquivo sugere o horário; não cria um agendamento. Configurar a rotina no Dots separadamente.', '');
  return lines.join('\n');
}

function main(argv) {
  const opts = { frames: true, related: true };
  for (let i = 0; i < argv.length; i++) {
    const key = argv[i];
    if (['--video', '--out', '--python'].includes(key)) {
      if (!argv[i + 1] || argv[i + 1].startsWith('--')) throw new Error(`Falta valor para ${key}`);
      opts[key.slice(2)] = argv[++i];
    } else if (key === '--first-missing') opts.firstMissing = true;
    else if (key === '--no-frames') opts.frames = false;
    else if (key === '--no-related') opts.related = false;
    else if (key === '--help') {
      console.log('node investigate.js --video ID_OU_LINK [--out artifacts/teste] [--no-frames] [--no-related]\n' +
        'node investigate.js --first-missing (últimos 7 dias; precisa de GOOGLE_CREDENTIALS_JSON)\n' +
        'Dependências: Python, requirements-investigate.txt; ffmpeg opcional para frames. Sem edição do Sheets.');
      return;
    } else throw new Error(`Opção desconhecida: ${key}`);
  }
  if (!!opts.video === !!opts.firstMissing) throw new Error('Escolha --video ou --first-missing.');
  const out = path.resolve(opts.out || path.join(__dirname, 'artifacts', `investigation-${Date.now()}`));
  fs.mkdirSync(out, { recursive: true });
  const args = [path.join(__dirname, 'collect_evidence.py'), '--out', out];
  args.push(...(opts.firstMissing ? ['--first-missing'] : ['--video', opts.video]));
  if (!opts.frames) args.push('--no-frames');
  if (!opts.related) args.push('--no-related');
  const run = spawnSync(opts.python || process.env.PYTHON || 'python', args,
    { encoding: 'utf8', shell: false, timeout: 540000, maxBuffer: 8 * 1024 * 1024 });
  if (run.error) throw new Error(`Não foi possível executar Python: ${run.error.message}`);
  if (run.stderr) process.stderr.write(run.stderr);
  if (run.status !== 0) throw new Error('Coleta incompleta; consulte a mensagem acima.');
  const report = prepare(JSON.parse(run.stdout));
  fs.writeFileSync(path.join(out, 'report.json'), JSON.stringify(report, null, 2));
  fs.writeFileSync(path.join(out, 'report.md'), markdown(report));
  console.log(`Dossiê: ${path.join(out, 'report.md')}\nStatus: ${report.status}\n` +
    `Candidatos: ${report.candidates.map(c => c.title).join(' | ') || 'nenhum título explícito'}\nNenhuma célula alterada.`);
}

module.exports = { candidates, prepare, markdown, main };
if (require.main === module) {
  try { main(process.argv.slice(2)); }
  catch (error) { console.error(error.message); process.exitCode = 1; }
}
