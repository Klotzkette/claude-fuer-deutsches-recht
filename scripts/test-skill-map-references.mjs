import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { validateSkillMapReferences } from './skill-map-references.mjs';

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
