const test = require('node:test');
const assert = require('node:assert/strict');
const { candidates, prepare, markdown } = require('../investigate.js');

test('questions, redirects and SEO are not titles', () => {
  for (const value of ['Manhwa name?', "manhwa name: It's in the comments", 'Name: https://example.com',
    'Title: Manhwa Recap', 'name: please bro?', 'Name: pinned below']) assert.deepEqual(candidates(value), []);
});

test('finds explicit titles in a response and preserves hypotheses as unverified', () => {
  assert.deepEqual(candidates('Name - The Return of the Mythical Archmage'), ['The Return of the Mythical Archmage']);
  const data = { primary: { video_id: 'ycKWC4EEz6c', title: 'Recap', url: 'https://www.youtube.com/watch?v=ycKWC4EEz6c',
    description: '', comments: [] }, related: [{ video_id: '6mJUJjuzGcs', url: 'https://www.youtube.com/watch?v=6mJUJjuzGcs',
    comments: [{ id: 'reply', text: 'the name of the novel he is animating is "Popularity Above All: I Play the Role of a Super Genius"' }] }] };
  const report = prepare(data, new Date('2026-10-11T18:00:00Z'));
  assert.equal(report.candidates[0].title, 'Popularity Above All: I Play the Role of a Super Genius');
  assert.equal(report.candidates[0].status, 'provavel');
  assert.equal(report.status, 'candidatos_para_validar');
  assert.equal(report.writes_performed, false);
  assert.equal(report.next_check_at, '2026-10-11T21:00:00.000Z');
  assert.match(markdown(report), /Nenhuma célula alterada/);
});
