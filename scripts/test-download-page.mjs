import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import { runInNewContext } from 'node:vm';

const html = readFileSync(new URL('../uebersicht-fachanwaltschaften/download.html', import.meta.url), 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
const pages = 'https://klotzkette.github.io/claude-fuer-deutsches-recht/';
const repository = 'Klotzkette/claude-fuer-deutsches-recht';

const skill = 'demo/skills/erste pruefung/SKILL.md';
const scenarios = [
  ['Pages liefert den Skill', skill, [200], 'demo--erste pruefung.md'],
  ['Raw liefert Markdown nach Pages-404', skill, [404, 200], 'demo--erste pruefung.md'],
  ['Raw liefert Markdown nach Netzfehler', skill, [0, 200], 'demo--erste pruefung.md'],
  ['Beide Quellen fehlen', skill, [404, 404], null],
  ['Pages liefert einen verschachtelten Zusatzprompt',
    'insolvenzsachbearbeitung/prompts/verbraucherinsolvenz/verbraucherinsolvenz-werkstatt.txt',
    [200], 'verbraucherinsolvenz-werkstatt.txt'],
  ['Ein fehlender TXT-Prompt bleibt ein Downloadfehler',
    'demo/fehlender-schnellstart.txt', [404, 404], null],
  ['Gewöhnliche TXT-Datei führt zur GitHub-Quelle', 'requirements.txt', [], null],
];
for (const kind of ['werkstatt', 'schnellstart', 'hauptproblem']) {
  const name = `demo-${kind}.txt`;
  scenarios.push([`Raw liefert ${kind}-TXT`, `demo/${name}`, [404, 200], name]);
}

for (const [title, path, responses, filename] of scenarios) {
  test(title, async () => {
    const calls = [];
    const download = {
      click() { this.clicked = true; },
      removeAttribute(key) { delete this[key]; },
    };
    const errors = new Set();
    const elements = { download, file: {}, source: {}, status: { classList: errors } };
    const location = new URL('download.html', pages);
    location.searchParams.set('path', path);
    await runInNewContext(script, {
      URL, URLSearchParams, window: { location }, document: { getElementById: id => elements[id] },
      fetch: async url => {
        const code = responses[calls.length];
        calls.push(String(url));
        if (!code) throw new TypeError('Netzfehler');
        return new Response('Beispielinhalt', { status: code });
      },
    });

    const target = path.split('/').map(encodeURIComponent).join('/');
    const urls = [`${pages}downloads/${target}`, `https://raw.githubusercontent.com/${repository}/main/${target}`];
    assert.deepEqual(calls, urls.slice(0, responses.length));
    assert.equal(elements.source.href, `https://github.com/${repository}/blob/main/${target}`);
    if (filename) {
      assert.equal(download.clicked, true);
      assert.equal(download.download, filename);
      assert.equal(await (await fetch(download.href)).text(), 'Beispielinhalt');
      URL.revokeObjectURL(download.href);
    } else {
      assert.ok(errors.has('error'));
      assert.equal(download.clicked, undefined);
      assert.equal(download.href, undefined);
    }
  });
}
