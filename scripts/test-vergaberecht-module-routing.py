#!/usr/bin/env python3
"""Fachthemen bleiben erhalten; ausführbare Vergabewege müssen tatsächlich existieren."""
from contextlib import redirect_stdout
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
        audit = json.loads((ROOT / 'quality/skill-consolidation/2026-11-14/vergaberecht-role-routing-followup.json').read_text())
        for record in audit['files']:
            current = (ROOT / record['path']).read_bytes()
            self.assertEqual(engine['sha'](current), record['sha256'])
            self.assertEqual(engine['sha'](engine['restore_original'](current, record['edits'])), record['original_sha256'])

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


if __name__ == '__main__':
    unittest.main()
