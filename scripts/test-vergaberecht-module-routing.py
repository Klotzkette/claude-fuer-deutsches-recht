#!/usr/bin/env python3
"""Fachthemen bleiben erhalten; ausführbare Vergabewege müssen tatsächlich existieren."""
from contextlib import redirect_stdout
import copy
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import runpy
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
NESTED = ROOT / 'vergaberecht-werkstatt'
PREVIOUS_AUDIT = 'quality/skill-consolidation/2026-11-14/vergaberecht-role-routing-followup.json'
PROMPT_REVISION = 'quality/hauptskills-2026-11-18/vergabeprompt-fortschreibung.json'
CI_FOLLOWUP = 'quality/hauptskills-2026-11-18/vergabefortfuehrung-ci.json'
sys.path.insert(0, str(NESTED / 'scripts'))
import skill_routing_priorities as R


def load(name):
    spec = importlib.util.spec_from_file_location('routing_' + name.replace('-', '_'), NESTED / 'scripts' / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


V = load('validate-prompt-routing-autarky')
M = load('generate-megaprompt')
U = load('generate-unified-mini-prompts')


def prompt_before_ci_followup(path, expected_sha256, followup=None):
    """Neue Generierung separat binden; den alten Promptnachweis nicht umschreiben."""
    if followup is None:
        followup = json.loads((ROOT / CI_FOLLOWUP).read_text())
    sha = lambda data: hashlib.sha256(data).hexdigest()
    if (followup.get('schema_version') != 1 or followup.get('method') != 'procurement_entrypoint_ci_followup'
            or followup.get('previous_prompt_revision') != PROMPT_REVISION
            or followup.get('previous_prompt_revision_sha256') != sha((ROOT / PROMPT_REVISION).read_bytes())):
        raise ValueError('Unbelegte Vergabeprompt-Folgestufe')
    registry = 'quality/hauptskills-2026-11-18/revisionen.json'
    registry_snapshot = 'quality/hauptskills-2026-11-18/vergabefortfuehrung-ci-vorfassungen/revisionen.json.gz'
    if followup.get('previous_main_registry') != registry or followup.get('previous_main_registry_snapshot') != registry_snapshot:
        raise ValueError('Historische Hauptskill-Registry nicht eindeutig archiviert')
    registry_archive = (ROOT / registry_snapshot).read_bytes()
    if (sha(registry_archive) != followup.get('previous_main_registry_snapshot_sha256')
            or sha(gzip.decompress(registry_archive)) != followup.get('previous_main_registry_sha256')):
        raise ValueError('Historische Hauptskill-Registry verändert')
    expected = {f'vergaberecht-werkstatt/testakten/megaprompts/{role}.md' for role in V.ROLE_FILES}
    records = [row for row in followup.get('files', []) if row.get('kind') == 'generated_megaprompt']
    if len(records) != len(expected) or {row.get('path') for row in records} != expected:
        raise ValueError('Folgestufe benötigt genau die drei erzeugten Vergabeprompts')
    if path not in expected:
        raise ValueError('Kein zulässiger Vergabeprompt')
    row = next(row for row in records if row['path'] == path)
    snapshot = 'quality/hauptskills-2026-11-18/vergabefortfuehrung-ci-vorfassungen/' + path + '.gz'
    generator = 'vergaberecht-werkstatt/scripts/generate-megaprompt.py'
    if (row.get('before_snapshot') != snapshot or row.get('before_sha256') != expected_sha256
            or row.get('generator') != generator or row.get('generator_sha256') != sha((ROOT / generator).read_bytes())):
        raise ValueError('Folgestufe passt nicht zu Vorfassung und Generator')
    archive = (ROOT / snapshot).read_bytes()
    if sha(archive) != row.get('before_snapshot_sha256'):
        raise ValueError('Zwischenarchiv verändert')
    before = gzip.decompress(archive)
    current = (ROOT / path).read_bytes()
    if sha(before) != expected_sha256 or sha(current) != row.get('after_sha256') or before == current:
        raise ValueError('Vergabeprompt-Folgestufe nicht bytegenau gebunden')
    return before


def verified_previous_prompt_bytes(revision=None):
    """Nur drei exakt nachgewiesene Fortschreibungen auf ihren Vorstand zurückführen."""
    if revision is None:
        revision = json.loads((ROOT / PROMPT_REVISION).read_text())
    if revision.get('schema_version') != 1 or revision.get('previous_audit') != PREVIOUS_AUDIT:
        raise ValueError('Unbekannte Vergabeprompt-Fortschreibung')
    sha = lambda data: hashlib.sha256(data).hexdigest()
    if sha((ROOT / PREVIOUS_AUDIT).read_bytes()) != revision.get('previous_audit_sha256'):
        raise ValueError('Historischer Nachweis wurde verändert')
    expected = {f'vergaberecht-werkstatt/testakten/megaprompts/{role}.md' for role in V.ROLE_FILES}
    records = revision.get('files', [])
    if len(records) != len(expected) or {record.get('path') for record in records} != expected:
        raise ValueError('Fortschreibung muss genau die drei Vergaberollen enthalten')
    previous = {}
    for record in records:
        path = record['path']
        snapshot = f"quality/hauptskills-2026-11-18/vergabeprompt-vorfassungen/{Path(path).name}.gz"
        if record.get('before_snapshot') != snapshot:
            raise ValueError(f'{path}: falsche Vorfassung')
        if record.get('generator') != 'vergaberecht-werkstatt/scripts/generate-megaprompt.py':
            raise ValueError(f'{path}: falscher Generator')
        archived = (ROOT / snapshot).read_bytes()
        if sha(archived) != record.get('before_snapshot_sha256'):
            raise ValueError(f'{path}: Archivhash stimmt nicht')
        before = gzip.decompress(archived)
        if sha(before) != record.get('before_sha256'):
            raise ValueError(f'{path}: Vorherhash stimmt nicht')
        current = prompt_before_ci_followup(path, record.get('after_sha256'))
        if sha(current) != record.get('after_sha256'):
            raise ValueError(f'{path}: Nachherhash stimmt nicht')
        if before == current:
            raise ValueError(f'{path}: keine Fortschreibung')
        previous[path] = before
    return previous


class ModuleRoutingTests(unittest.TestCase):
    def test_full_module_inventory_is_separate_from_small_active_menu(self):
        for role, modules, priorities in [('vergabestelle-behoerden', 122, 51), ('bieter-unternehmen', 113, 49), ('konkurrenten-rechtsschutz', 20, 20)]:
            with self.subTest(role=role):
                self.assertEqual(len(M.collect_skills(NESTED / role)), modules)
                self.assertEqual(len(U.collect_skills(NESTED / role)), modules)
                self.assertEqual(len(R.PLUGIN_PRIORITY_MODULES[role]), priorities)
                self.assertLessEqual(len(R.PLUGIN_PRIORITY_SKILLS[role]), 20)
                for topic in R.PLUGIN_PRIORITY_MODULES[role]:
                    route = R.module_route(role, topic)
                    self.assertTrue((NESTED / role / route['source']).is_file())
                    self.assertTrue((NESTED / role / 'skills' / route['skill'] / 'SKILL.md').is_file())

    def test_twelve_role_prompts_and_all_original_trigger_assignments(self):
        self.assertEqual(sum(map(len, V.ROLE_FILES.values())), 12)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(V.main(), 0)

    def test_old_nonactive_slug_wrong_role_wrong_topic_and_missing_topic_rejected(self):
        role, topic = 'bieter-unternehmen', '21-ruegeschreiben-erstellen'
        route = R.module_route(role, topic)
        self.assertNotEqual(route['skill'], topic)
        skills = V.skill_names(role)
        good = R.skill_call(role, topic)
        self.assertEqual(V.validate_module_calls(good, role, skills), [])
        for bad in (good.replace('bieter-unternehmen:', 'vergabestelle-behoerden:'),
                    good.replace(route['skill'], 'vergabe-os-master-orchestrator'),
                    good.replace('21-ruegeschreiben-erstellen', 'nicht-vorhanden'),
                    f"`/{role}:{route['skill']}`"):
            with self.subTest(bad=bad):
                self.assertTrue(V.validate_module_calls(bad, role, skills))
        original = V.ROLE_FILES[role][0]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'prompt.md'
            path.write_text(original.read_text().replace(good, f'`{topic}`'))
            self.assertTrue(any('unbekannte Skill-Slugs' in issue for issue in V.validate_prompt(path, role, skills)))

    def test_mini_cannot_drop_or_misroute_the_preserved_topic(self):
        role = 'bieter-unternehmen'
        path = NESTED / 'unified-mini-prompts' / (role + '.md')
        text = path.read_text()
        trigger, owner, topic = R.PLUGIN_TRIGGER_ROUTES[role][1]
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'unified-mini-prompts' / path.name
            target.parent.mkdir()
            target.write_text(text.replace(trigger, 'anderer Auftrag'))
            self.assertTrue(any('Fachthema/Owner' in error for error in V.validate_prompt(target, role, V.skill_names(role))))
            target.write_text(text.replace(f'|{trigger}|`{owner}`|', f'|{trigger}|`vergabe-os-master-orchestrator`|'))
            self.assertTrue(any('Fachthema/Owner' in error for error in V.validate_prompt(target, role, V.skill_names(role))))

    def test_original_prompt_bytes_remain_recoverable_from_exact_deltas(self):
        engine = runpy.run_path(str(ROOT / 'scripts/consolidate-skill-cap.py'))
        audit = json.loads((ROOT / PREVIOUS_AUDIT).read_text())
        previous = verified_previous_prompt_bytes()
        for record in audit['files']:
            audited = previous[record['path']] if record['path'] in previous else (ROOT / record['path']).read_bytes()
            self.assertEqual(engine['sha'](audited), record['sha256'])
            self.assertEqual(engine['sha'](engine['restore_original'](audited, record['edits'])), record['original_sha256'])

    def test_prompt_revision_rejects_missing_records_and_broken_hash_bindings(self):
        valid = json.loads((ROOT / PROMPT_REVISION).read_text())
        self.assertEqual(len(verified_previous_prompt_bytes(valid)), 3)
        for change in ('missing-role', 'duplicate-role', 'previous_audit_sha256',
                       'before_sha256', 'after_sha256', 'before_snapshot_sha256',
                       'before_snapshot', 'generator'):
            revision = copy.deepcopy(valid)
            if change == 'missing-role':
                revision['files'].pop()
            elif change == 'duplicate-role':
                revision['files'][1] = copy.deepcopy(revision['files'][0])
            elif change == 'previous_audit_sha256':
                revision[change] = '0' * 64
            else:
                revision['files'][0][change] = '0' * 64
            with self.subTest(change=change), self.assertRaises(ValueError):
                verified_previous_prompt_bytes(revision)

    def test_future_generators_keep_valid_calls_and_match_reviewed_full_outputs(self):
        for role in V.ROLE_FILES:
            with self.subTest(role=role):
                mega = M.build_megaprompt(NESTED / role)
                mini = U.fit_prompt({'name': role}, NESTED / role)
                self.assertEqual(mega, (NESTED / 'testakten/megaprompts' / f'{role}.md').read_text())
                self.assertEqual(mini, (NESTED / 'unified-mini-prompts' / f'{role}.md').read_text())
                self.assertEqual(V.validate_module_calls(mega, role, V.skill_names(role)), [])
                self.assertFalse(set(V.extract_skill_slugs(mega, V.skill_names(role))) - V.skill_names(role))
                self.assertLessEqual(len(mini.encode('utf-8')), 7500)
                for trigger, module in R.PLUGIN_TRIGGER_MODULES[role]:
                    self.assertIn(trigger, mini)
                    self.assertIn(R.skill_call(role, module), mega)
                # A bare old Fachmodul in a retained body must also route correctly,
                # rather than only fixing the newly generated menu.
                for module in R.PLUGIN_PRIORITY_MODULES[role]:
                    self.assertEqual(R.rewrite_module_calls(role, f'`{module}`'), R.skill_call(role, module))

    def test_ci_followup_rejects_broken_chain_or_wrong_generator(self):
        valid = json.loads((ROOT / CI_FOLLOWUP).read_text())
        record = next(row for row in valid['files'] if row['kind'] == 'generated_megaprompt')
        self.assertEqual(hashlib.sha256(prompt_before_ci_followup(record['path'], record['before_sha256'])).hexdigest(),
                         record['before_sha256'])
        for field in ('previous_prompt_revision_sha256', 'previous_main_registry_sha256',
                      'previous_main_registry_snapshot', 'previous_main_registry_snapshot_sha256', 'before_sha256', 'after_sha256',
                      'before_snapshot_sha256', 'before_snapshot', 'generator', 'generator_sha256', 'missing-role'):
            changed = copy.deepcopy(valid)
            target = next(row for row in changed['files'] if row['kind'] == 'generated_megaprompt')
            if field.startswith('previous_'):
                changed[field] = '0' * 64
            elif field == 'missing-role':
                changed['files'].remove(target)
            else:
                target[field] = '0' * 64
            with self.subTest(field=field), self.assertRaises(ValueError):
                prompt_before_ci_followup(record['path'], record['before_sha256'], changed)


if __name__ == '__main__':
    unittest.main()
