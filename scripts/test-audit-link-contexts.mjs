import test from 'node:test';
import assert from 'node:assert/strict';
import { auditLinkContexts } from './audit-link-contexts.mjs';

const root = '/repo';
const source = '/repo/quality/skill-consolidation/2026-11-14/source-map.json';
const row = { path: 'plugin/skills/alt/FACHINHALT.md', edits: [{ before: '[Alt](../alt/SKILL.md)', after: '[Jetzt](../ziel/FACHINHALT.md)' }] };

test('Aktueller Link wird am Quellpfad geprüft; alter Text bleibt historische Evidenz', () => {
  const raw = JSON.stringify({ schema_version: 1, files: [row] });
  const contexts = auditLinkContexts(source, raw, root);
  assert.deepEqual(contexts[1], { file: '/repo/plugin/skills/alt/FACHINHALT.md', text: '[Jetzt](../ziel/FACHINHALT.md)' });
  assert.ok(!contexts[0].text.includes('[Alt]'));
  assert.ok(JSON.parse(raw).files[0].edits[0].before.includes('SKILL.md'));
});

test('Sonstige JSON-Felder und gewöhnliche JSON-Dateien bleiben geprüft', () => {
  const raw = JSON.stringify({ schema_version: 1, files: [row], note: '[Defekt](fehlt.md)' });
  assert.ok(auditLinkContexts(source, raw, root)[0].text.includes('[Defekt](fehlt.md)'));
  assert.deepEqual(auditLinkContexts('/repo/quality/anderes.json', raw, root), [{ file: '/repo/quality/anderes.json', text: raw }]);
});

test('Mini-Redaktionsnachweis nutzt den protokollierten Promptpfad', () => {
  const file = '/repo/quality/source-audits/2026-11-14/mini-laengenredaktion.json';
  const data = { date: '2026-11-14', method: 'Lektüre', files: [{ path: 'plugin/mini.md', edits: [{ old: '[Alt](alt.md)', new: '[Neu](neu.md)' }] }] };
  assert.deepEqual(auditLinkContexts(file, JSON.stringify(data), root)[1], { file: '/repo/plugin/mini.md', text: '[Neu](neu.md)' });
});

test('Renderer-Code ist Code; erzeugte Links werden am tatsächlichen Skill geprüft', () => {
  const file = '/repo/quality/skill-consolidation/2026-11-14/vergaberecht-followup.json';
  const data = { schema_version: 1, changes: [row], renderer_delta: {
    path: 'scripts/consolidate-skill-cap.py', edits: [{ before: '', after: 'output = "[Format](../../references/OUTPUT-FORMAT.md)"' }],
    note: '[Sonstiger Link](kontrolle.md)' } };
  const contexts = auditLinkContexts(file, JSON.stringify(data), root);
  assert.deepEqual(contexts[1], { file: '/repo/plugin/skills/alt/FACHINHALT.md', text: '[Jetzt](../ziel/FACHINHALT.md)' });
  assert.ok(!contexts[0].text.includes('OUTPUT-FORMAT.md'));
  assert.ok(contexts[0].text.includes('[Sonstiger Link](kontrolle.md)'));
  data.renderer_delta.path = 'beliebige.md';
  assert.throws(() => auditLinkContexts(file, JSON.stringify(data), root));
});

test('Ungültige Form, fehlende Texte und ausbrechende Pfade werden abgelehnt', () => {
  for (const data of [ { schema_version: 2, files: [] }, { schema_version: 1, files: {} },
    ...['../outside.md', '/outside.md'].map(p => ({ schema_version: 1, files: [{ ...row, path: p }] })),
    { schema_version: 1, files: [{ ...row, edits: [{ before: 'alt' }] }] } ]) {
    assert.throws(() => auditLinkContexts(source, JSON.stringify(data), root));
  }
});
