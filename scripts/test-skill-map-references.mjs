import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { validateSkillMapReferences, validateFachinhaltReferences } from './skill-map-references.mjs';

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'legal-skill-map-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  const writeSkill = (plugin, slug) => {
    const file = path.join(root, plugin, 'skills', slug, 'SKILL.md');
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, '# Arbeitsauftrag\n');
    return file;
  };
  return { root, writeSkill, router: writeSkill('plugin', 'einstieg') };
}

test('gelöschte oder umbenannte Ziele werden im richtigen Plugin erkannt', t => {
  const { router, writeSkill } = fixture(t);
  const target = writeSkill('plugin', 'aktueller-sachskill');
  const map = '## Fachlandkarte dieses Plugins\n\n- `aktueller-sachskill` — Aufgabe\n';
  assert.deepEqual(validateSkillMapReferences(router, map), []);
  fs.renameSync(path.dirname(target), path.join(path.dirname(path.dirname(target)), 'neuer-name'));
  writeSkill('anderes-plugin', 'aktueller-sachskill');
  assert.equal(validateSkillMapReferences(router, map).length, 1);
  assert.deepEqual(validateSkillMapReferences(router, map.replace('`aktueller-sachskill`', '`neuer-name`')), []);
});

test('Tabellen und relative Markdown-Links prüfen echte SKILL.md-Dateien', t => {
  const { router, writeSkill } = fixture(t);
  const target = writeSkill('plugin', 'vorhanden');
  const text = [
    '## 2. Fachlandkarte',
    '| Skill | Aufgabe |',
    '| --- | --- |',
    '| `vorhanden` | Bearbeiten |',
    '- [Arbeitsgang](../vorhanden/SKILL.md#arbeitsauftrag)',
    '### Vertiefung',
    '- `fehlt` — Fehlendes Ziel',
    '## 3. Andere Hinweise',
    '- `kein-skillverweis` — Kein Fachlandkarteneintrag',
  ].join('\r\n');
  assert.equal(validateSkillMapReferences(router, text).length, 1);
  fs.rmSync(target);
  fs.mkdirSync(target);
  assert.equal(validateSkillMapReferences(router, text).length, 3);
});

test('Beispiele in Codeblöcken werden nicht als echte Navigation geprüft', t => {
  const { router } = fixture(t);
  const text = [
    '```markdown',
    '## Fachlandkarte als Beispiel',
    '- `beispiel` — Nicht installiert',
    '```',
    '## Fachlandkarte dieses Plugins',
    '~~~markdown',
    '- `beispiel` — Nicht installiert',
    '~~~',
    '## Arbeitsweg',
    '- `anderer-text` — Keine Karte',
  ].join('\n');
  assert.deepEqual(validateSkillMapReferences(router, text), []);
});

test('Navigation kann weder Plugin-Grenzen überschreiten noch Pfade als Slugs tarnen', t => {
  const { router, writeSkill } = fixture(t);
  writeSkill('anderes-plugin', 'vorhanden');
  const text = [
    '## Fachlandkarte dieses Plugins',
    '- `../vorhanden` — Ungültiger Slug',
    '- [Fremdes Plugin](../../../anderes-plugin/skills/vorhanden/SKILL.md)',
  ].join('\n');
  assert.equal(validateSkillMapReferences(router, text).length, 2);
});

test('Fachinhalt ist erreichbar, wird aber niemals als aktiver Fachlandkarten-Skill gezählt', t => {
  const { router, writeSkill } = fixture(t);
  const old = writeSkill('plugin', 'alte-vertiefung');
  const reference = path.join(path.dirname(old), 'FACHINHALT.md');
  fs.renameSync(old, reference);
  const link = '- [Fachinhalt](../alte-vertiefung/FACHINHALT.md)\n';
  assert.deepEqual(validateSkillMapReferences(router, '## Fachvertiefungen gezielt laden\n\n' + link), []);
  assert.equal(validateSkillMapReferences(router, '## Fachlandkarte\n\n' + link).length, 1);
  assert.equal(validateSkillMapReferences(router, '## Fachlandkarte\n\n- `alte-vertiefung`\n').length, 1);
  fs.unlinkSync(reference);
  assert.equal(validateFachinhaltReferences(router, link).length, 1);
});

test('Fachinhalte und Fachlandkarten dürfen nicht per Symlink aus dem Paket ausbrechen', t => {
  const { router, writeSkill } = fixture(t);
  const outside = writeSkill('anderes-plugin', 'fremd');
  const local = writeSkill('plugin', 'vertiefung');
  fs.unlinkSync(local);
  fs.symlinkSync(outside, local);
  assert.equal(validateSkillMapReferences(router, '## Fachlandkarte\n\n- `vertiefung`\n').length, 1);
  const reference = path.join(path.dirname(local), 'FACHINHALT.md');
  fs.symlinkSync(outside, reference);
  assert.equal(validateFachinhaltReferences(router, '[Inhalt](../vertiefung/FACHINHALT.md)').length, 1);
});
