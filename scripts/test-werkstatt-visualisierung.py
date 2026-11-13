#!/usr/bin/env python3
"""Offline-Vertrag für Visualisierungsanweisungen und verlustfreie Einbindung.

Prüft Quellen, Auswahl, Erhaltung und Fähigkeitsgrenzen. Ein erfolgreicher Lauf
behauptet weder Modellbefolgung noch eine gerenderte oder geöffnete Oberfläche.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

import werkstatt_visualisierung as V
from prompt_profiles import standalone_kinds
from themen_profile import PROFILE_BY_KEY


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('sync_visual_workflow', ROOT / 'scripts/sync-werkstatt-visualisierung.py')
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)
MEGA_SPEC = importlib.util.spec_from_file_location('visual_megaprompt', ROOT / 'scripts/generate-megaprompt.py')
MEGA = importlib.util.module_from_spec(MEGA_SPEC)
MEGA_SPEC.loader.exec_module(MEGA)


class VisualisierungTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profiles = V.load_profiles()
        cls.marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())['plugins']
        cls.sources = {item['name']: ROOT / item['source'] for item in cls.marketplace}

    def test_all_marketplace_plugins_have_existing_deliberate_entry_skills(self):
        self.assertEqual(set(self.profiles), set(self.sources))
        for slug, entry in self.profiles.items():
            with self.subTest(plugin=slug):
                chosen = entry['entry_skills']
                self.assertGreaterEqual(len(chosen), 1)
                self.assertLessEqual(len(chosen), 3)
                self.assertEqual(len(chosen), len(set(chosen)))
                self.assertTrue(entry['rationale'].strip())
                for name in chosen:
                    self.assertRegex(name, r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
                    path = self.sources[slug] / 'skills' / name / 'SKILL.md'
                    self.assertTrue(path.is_file(), str(path))
                    self.assertRegex(path.read_text(), r'(?m)^name:\s*[\"\']?' + re.escape(name) + r'[\"\']?\s*$')

    def test_themes_have_exactly_one_existing_visual_family(self):
        for slug, entry in self.profiles.items():
            with self.subTest(plugin=slug):
                self.assertIn(entry['theme'], PROFILE_BY_KEY)
                self.assertIn(V.family(entry['theme']), V.VIEWS)
                self.assertIn(V.family_for(slug, entry['theme']), V.VIEWS)
        for overrides in (V.OVERRIDES, V.FAMILY_OVERRIDES, V.LABEL_OVERRIDES):
            self.assertTrue(set(overrides) <= set(self.sources), 'Keine ungenutzten oder falsch geschriebenen Plugin-Ausnahmen')
        with self.assertRaises(ValueError):
            V.family('nicht-vorhandenes-thema')
        with patch.dict(V.GROUPS, {'zweites-schema': 'insolvenz'}):
            with self.assertRaises(ValueError):
                V.family('insolvenz')

    def test_app_boundary_matches_publication_profiles(self):
        promptless = {slug for slug in self.sources if not standalone_kinds(slug)}
        self.assertEqual(promptless, {'grundstuecksrecherche', 'schriftsatzwerkstatt-bea'})
        self.assertEqual({slug for slug, item in self.profiles.items() if item['mode'] == 'app'}, promptless)
        for slug in promptless:
            original = '# Vorhandene App\n\nDie Anwendung ist der Arbeitsort.\n'
            self.assertEqual(V.block(original, slug), original)
            skill = V.block(original, slug, kind='skill')
            self.assertRegex(skill, r'vorhandene(?:r)? Anwend')
            self.assertIn('nicht durch ein neu erfundenes Applet', skill)
            self.assertEqual(V.remove_block(skill), original)

    def test_idempotence_and_byte_exact_preservation(self):
        for original in (
            '', '# Auftrag', '# Auftrag\n', '# Auftrag\n\n',
            '# Auftrag\r\n\r\n## 1.1. Fachinhalt\r\nÄnderung € 1.234,56\r\n',
            '# Auftrag\n\n## 1. Fachinhalt\n\n```text\nE-Mail / Konto 001\n```\n\n',
        ):
            with self.subTest(original=repr(original)):
                generated = V.block(original, 'bauunternehmer-einkauf')
                self.assertEqual(V.block(generated, 'bauunternehmer-einkauf'), generated)
                self.assertEqual(V.remove_block(generated).encode(), original.encode())
                self.assertEqual(generated.count(V.BEGIN), 1)
                self.assertEqual(generated.count(V.END), 1)

    def test_replacement_does_not_erase_existing_following_text(self):
        source = '# Vertrag\n\nVollständiger unveränderter Klauseltext.\n'
        generated = V.block(source, 'vertragserstellung', kind='skill')
        trailer = '\n## 7. Individuelle Fachergänzung\n\nDie Sonderregel bleibt erhalten.\n'
        combined = generated + trailer
        self.assertEqual(V.remove_block(combined), source + trailer)
        rewritten = V.block(combined, 'vertragserstellung')
        self.assertEqual(V.remove_block(rewritten), source + trailer)
        self.assertNotIn('../../references/', rewritten)
        self.assertEqual(V.block(rewritten, 'vertragserstellung'), rewritten)

    def test_broken_or_reordered_markers_are_rejected(self):
        bad = (
            V.BEGIN, V.END, V.END + '\n' + V.BEGIN,
            V.BEGIN + '\n' + V.BEGIN + '\n' + V.END + '\n' + V.END,
            V.BEGIN + '\n' + V.END + '\n' + V.BEGIN + '\n' + V.END,
        )
        for content in bad:
            with self.subTest(content=content), self.assertRaises(ValueError):
                V.block(content, 'arbeitsrecht')

    def test_heading_follows_existing_decimal_levels(self):
        for original in (
            '# 1. Fall\n\n## 1.1. Zweck\n\n## 1.6. Beispiel\n',
            '# Fall\n\n## 1 Zweck\n\n## 3 Ergebnis\n',
        ):
            generated = V.block(original, 'arbeitsrecht')
            inserted = generated.split(V.BEGIN, 1)[1]
            expected = 2 if '1.6.' in original else 4
            self.assertRegex(inserted, rf'\n## {expected}\. Verständlich')

    def test_standalone_is_complete_and_skill_has_package_local_reference(self):
        text = V.block('# Fachauftrag\n', 'bauunternehmer-einkauf')
        self.assertNotIn('../../references/', text)
        for required in (V.SERVICE, V.RUNTIME, V.QUALITY, V.CONTINUATION):
            self.assertIn(required, text)
        skill = V.block('# Fachauftrag\n', 'bauunternehmer-einkauf', kind='skill')
        self.assertIn('../../references/' + V.REFERENCE, skill)
        self.assertIn('Ohne diese Fähigkeit', skill)

    def test_host_capability_fallback_and_no_unconditional_success_claim(self):
        text = V.block('# Auftrag\n', 'bauunternehmer-einkauf')
        for required in (
            'tatsächlich verfügbaren Werkzeuge',
            'Aus Modellname, Dateiname oder Nutzervermutung keine Fähigkeiten ableiten',
            'sofern die Umgebung das unterstützt',
            'Fehlt die interaktive Oberfläche',
            'Ohne Werkzeuge im Text weiterarbeiten',
            'nicht ausgeführt wurde',
        ):
            self.assertIn(required, text)
        self.assertNotRegex(text, r'(?i)\b(?:ChatGPT|Claude|Cowork|GPT-\d)\b')
        self.assertNotIn('<iframe', text)
        self.assertNotRegex(text, r'(?i)(?:immer|automatisch) (?:öffentlich|veröffentlichen|hochladen)')

    def test_ui_selection_has_explicit_bridge_independent_handoff(self):
        text = V.reference('compliance-abteilung-grosskonzern', self.profiles['compliance-abteilung-grosskonzern'])
        # Eine lokale Auswahl allein ist noch keine Nachricht an das Modell.
        self.assertRegex(text, r'(?i)(?:Rückkanal|Rückmeldung|Bridge|Übertragung an das Modell|Übergabe an den Chat)')
        self.assertRegex(text, r'(?i)(?:Übernahmetext|Übernahme als Text|Auswahl als Text|kopierbare.*Auswahl|lesbare.*Auswahl)')

    def test_visuals_keep_proof_uncertainty_and_output_obligation(self):
        text = V.block('# Auftrag\n', 'zahlungsunfaehigkeits-und-ueberschuldungspruefer')
        for required in (
            'Fehlend ist nicht null', 'Originalbelegen', 'Keine erfundenen Erfolgschancen',
            'automatisch verbindlichen Rechtsentscheidungen', 'vollständigen Sätzen fertigstellen',
            'keine Freigabe für Versand', 'keine auszuführenden Anweisungen',
            'nicht als aktives HTML ausführen', 'per Tastatur', 'ohne Farbe',
        ):
            self.assertIn(required, text)
        self.assertIn('keinen neuen Eintrittstag', text)

    def test_concrete_routes_do_not_reduce_every_case_to_same_dashboard(self):
        pairs = (
            ('zahlungsunfaehigkeits-und-ueberschuldungspruefer', ('Aktiva I/II', 'Passiva I/II', 'Fortbestehensprognose')),
            ('compliance-abteilung-grosskonzern', ('Rezeptur', 'Charge', 'Etikett', 'Grundaktenmodus')),
            ('bauunternehmer-einkauf', ('Bedarfsermittlung', 'LV-Position', 'vier Angebote', 'Nebenpreis')),
            ('steuerrecht-anwalt-und-berater', ('Erklärungsfelder', 'Rechnungsdatum', 'Leistungszeitraum', 'reicht keine Erklärung ein')),
        )
        for slug, markers in pairs:
            with self.subTest(plugin=slug):
                text = V.route_text(slug, self.profiles[slug]['theme'])
                for marker in markers:
                    self.assertIn(marker, text)
        public_procurement = V.route_text('bauvergabe-verfahren', 'vergabe')
        self.assertIn('nicht durch frei verschiebbare Gewichte', public_procurement)
        history = V.route_text('preussisches-allgemeines-landrecht-pralr', 'pralr')
        self.assertIn('historische Übergänge', history)
        self.assertNotIn('Fristenblatt', history)

    def test_every_workshop_and_entry_skill_can_roundtrip_without_writing(self):
        before = {slug: sorted(p.relative_to(path).as_posix() for p in (path / 'skills').glob('*/SKILL.md')) for slug, path in self.sources.items()}
        checked_workshops = 0
        with patch.object(Path, 'write_text', side_effect=AssertionError('Renderer darf keine Datei schreiben')), \
                patch.object(Path, 'write_bytes', side_effect=AssertionError('Renderer darf keine Datei schreiben')):
            for slug, entry in self.profiles.items():
                files = [(self.sources[slug] / 'skills' / name / 'SKILL.md', 'skill') for name in entry['entry_skills']]
                if 'werkstatt' in standalone_kinds(slug):
                    files.append((self.sources[slug] / f'{slug}-werkstatt.md', 'workshop'))
                for path, kind in files:
                    with self.subTest(file=str(path)):
                        original = path.read_text(encoding='utf-8')
                        base = V.remove_block(original)
                        produced = V.block(original, slug, kind=kind)
                        self.assertEqual(V.remove_block(produced).encode(), base.encode())
                        self.assertEqual(V.block(produced, slug, kind=kind), produced)
                        checked_workshops += kind == 'workshop'
        self.assertEqual(checked_workshops, len(self.sources) - 2)
        after = {slug: sorted(p.relative_to(path).as_posix() for p in (path / 'skills').glob('*/SKILL.md')) for slug, path in self.sources.items()}
        self.assertEqual(before, after, 'Keine zusätzlichen Hauptskills oder veränderten Skillzahlen')

    def test_subject_overrides_include_question_and_output(self):
        compliance = V.route_text('compliance-abteilung-grosskonzern', self.profiles['compliance-abteilung-grosskonzern']['theme'])
        self.assertNotIn('Leitfrage für Gesellschaftsrecht', compliance)
        self.assertNotIn('begründete Strukturentscheidung', compliance)
        self.assertRegex(compliance, r'(?i)(?:Untersuchungs|Maßnahmen|Prüfbericht)')
        rental = V.route_text('mietrecht', self.profiles['mietrecht']['theme'])
        self.assertNotIn('Registerart', rental)
        certificate = V.route_text('arbeitszeugnisgenerator', self.profiles['arbeitszeugnisgenerator']['theme'])
        self.assertNotIn('Fristenblatt', certificate)

    def test_unknown_slug_is_not_silently_given_a_generic_legal_route(self):
        original = '# Unbekanntes Arbeitsfeld\n'
        self.assertEqual(V.block(original, 'unbekanntes-arbeitsfeld'), original)


class SynchronisierungTests(unittest.TestCase):
    def fixture(self, root, slug, entry):
        directory = root / slug
        for name in entry['entry_skills']:
            skill = directory / 'skills' / name / 'SKILL.md'
            skill.parent.mkdir(parents=True, exist_ok=True)
            skill.write_text(f'---\nname: {name}\ndescription: Fall bearbeiten.\n---\n\n# 1. Auftrag\n\nUnveränderter Fachtext.\n')
        if entry['mode'] == 'prompt':
            (directory / f'{slug}-werkstatt.md').write_bytes('# Fachauftrag\r\n\r\nOriginal € 1.234,56.\r\n'.encode())
            (directory / f'{slug}-schnellstart.md').write_bytes('# Kurzauftrag\r\n\r\nKurzer unveränderter Fachtext.\r\n'.encode())
        return directory

    def test_plan_preserves_sources_and_app_boundary_without_new_skills(self):
        all_profiles = V.load_profiles()
        names = ('bauunternehmer-einkauf', 'grundstuecksrecherche')
        profiles = {name: all_profiles[name] for name in names}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            manifest = root / '.claude-plugin/marketplace.json'
            manifest.parent.mkdir()
            manifest.write_text(json.dumps({'plugins': [{'name': name, 'source': './' + name} for name in names]}))
            for slug, entry in profiles.items():
                self.fixture(root, slug, entry)
            before = {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            with patch.object(Path, 'write_bytes', side_effect=AssertionError('plan darf nicht schreiben')):
                outputs, report = SYNC.plan(root, profiles)
            after = {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(before, after)
            for path, content in outputs.items():
                if path.name == V.REFERENCE:
                    continue
                self.assertEqual(V.remove_block(content.decode()).encode(), before[path.relative_to(root).as_posix()])
            self.assertEqual(report['method'], 'desk_review')
            self.assertFalse(any(path.name.endswith('-werkstatt.md') for path in outputs if 'grundstuecksrecherche' in path.parts))
            for path, content in outputs.items():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            repeated, _ = SYNC.plan(root, profiles)
            self.assertEqual(outputs, repeated)
            self.assertEqual(
                {p for p in before if p.endswith('/SKILL.md')},
                {p.relative_to(root).as_posix() for p in root.rglob('SKILL.md')},
            )
            broken = {name: profiles[name] for name in names[:1]}
            with self.assertRaisesRegex(ValueError, 'Marketplace nicht exakt'):
                SYNC.plan(root, broken)

    def test_hash_review_does_not_certify_preexisting_changes_or_live_execution(self):
        slug = 'bauunternehmer-einkauf'
        entry = V.load_profiles()[slug]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            directory = self.fixture(root, slug, entry)
            manifest = root / '.claude-plugin/marketplace.json'
            manifest.parent.mkdir()
            manifest.write_text(json.dumps({'plugins': [{'name': slug, 'source': './' + slug}]}))
            workshop = directory / f'{slug}-werkstatt.md'
            skill = directory / 'skills' / entry['entry_skills'][0] / 'SKILL.md'
            relative_skill = skill.relative_to(root).as_posix()
            profile_path = root / 'quality/evals' / f'{slug}.json'
            profile_path.parent.mkdir(parents=True)
            old = {
                'plugin': slug,
                'editorial_status': 'needs_review',
                'workshop_review': {'sha256': hashlib.sha256(workshop.read_bytes()).hexdigest()},
                'artifact_hashes': {relative_skill: '0' * 64},
            }
            profile_path.write_text(json.dumps(old))
            outputs = {p: V.block(p.read_bytes().decode(), slug, kind=kind).encode()
                       for p, kind in ((workshop, 'workshop'), (skill, 'skill'))}
            updates = SYNC.reviewed_profiles(root, outputs)
            updated = json.loads(updates[profile_path])
            self.assertEqual(updated['workshop_review']['sha256'], hashlib.sha256(outputs[workshop]).hexdigest())
            self.assertEqual(updated['artifact_hashes'][relative_skill], '0' * 64)
            self.assertEqual(updated['editorial_status'], 'needs_review')
            self.assertEqual(updated['visual_workflow_review']['method'], 'desk_review')
            self.assertIn(relative_skill, updated['visual_workflow_review']['pending_prior_changes'])
            self.assertIn('kein Live-Modelltest', updated['visual_workflow_review']['limits'])
            self.assertEqual(json.loads(profile_path.read_text()), old, 'Reviewplan schreibt nicht selbst')

    def test_canonical_root_and_output_keys_accept_existing_root_alias(self):
        slug = 'bauunternehmer-einkauf'
        profiles = {slug: V.load_profiles()[slug]}
        with tempfile.TemporaryDirectory() as tmp:
            parent = Path(tmp).resolve()
            root = parent / 'repo'
            root.mkdir()
            alias = parent / 'repo-alias'
            alias.symlink_to(root, target_is_directory=True)
            manifest = root / '.claude-plugin/marketplace.json'
            manifest.parent.mkdir()
            manifest.write_text(json.dumps({'plugins': [{'name': slug, 'source': './' + slug}]}))
            self.fixture(root, slug, profiles[slug])
            direct, report = SYNC.plan(root, profiles)
            aliased, alias_report = SYNC.plan(alias, profiles)
            self.assertEqual(direct, aliased)
            self.assertEqual(report, alias_report)
            sample = next(iter(direct))
            self.assertEqual(SYNC.output_path(root, alias / sample.relative_to(root)), sample)
            self.assertEqual(SYNC.reviewed_profiles(alias, {alias / path.relative_to(root): data for path, data in direct.items()}), {})

    def test_plan_rejects_symlinked_generated_reference_and_traversal_skills(self):
        slug = 'bauunternehmer-einkauf'
        profiles = {slug: V.load_profiles()[slug]}
        with tempfile.TemporaryDirectory() as tmp:
            parent = Path(tmp).resolve()
            root = parent / 'repo'
            root.mkdir()
            manifest = root / '.claude-plugin/marketplace.json'
            manifest.parent.mkdir()
            manifest.write_text(json.dumps({'plugins': [{'name': slug, 'source': './' + slug}]}))
            directory = self.fixture(root, slug, profiles[slug])
            outside = parent / 'outside'
            outside.mkdir()
            ref_dir = directory / 'references'
            ref_dir.symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, 'Ausgabepfad|Ausgabeordner'):
                SYNC.plan(root, profiles)
            self.assertEqual(list(outside.iterdir()), [])
            ref_dir.unlink()
            ref_dir.mkdir()
            target = outside / 'unveraendert.md'
            target.write_bytes(b'Original')
            ref = ref_dir / V.REFERENCE
            ref.symlink_to(target)
            with self.assertRaisesRegex(ValueError, 'Ausgabepfad|Ausgabeordner'):
                SYNC.plan(root, profiles)
            self.assertEqual(target.read_bytes(), b'Original')
            bad = {slug: {**profiles[slug], 'entry_skills': ['../ausbruch']}}
            with self.assertRaisesRegex(ValueError, 'Einstiegsskills'):
                SYNC.plan(root, bad)

    def test_megaprompt_deduplicates_skill_blocks_and_keeps_fachtext(self):
        slug = 'bauunternehmer-einkauf'
        entry = V.load_profiles()[slug]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            directory = self.fixture(root, slug, entry)
            other = directory / 'skills/weitere-pruefung/SKILL.md'
            other.parent.mkdir(parents=True)
            other.write_text('---\nname: weitere-pruefung\ndescription: Zusätzliche Fachprüfung.\n---\n\n# 1. Fachtext\n\nIndividuell belegter Inhalt bleibt erhalten.\n')
            with patch.object(MEGA, 'REPO', root):
                baseline = MEGA.build_megaprompt(directory)
                for path in directory.glob('skills/*/SKILL.md'):
                    path.write_text(V.block(path.read_text(), slug, kind='skill'))
                enriched = MEGA.build_megaprompt(directory)
            self.assertEqual(enriched, baseline)
            self.assertEqual(enriched.count(V.BEGIN), 1)
            self.assertEqual(enriched.count(V.END), 1)
            self.assertIn('Individuell belegter Inhalt bleibt erhalten.', enriched)
            self.assertNotIn('../../references/', enriched)
            self.assertIsNone(MEGA.build_megaprompt(root / 'grundstuecksrecherche'))

    def test_short_prompts_remain_unenriched_and_remove_only_old_marked_block(self):
        slug = 'arbeitsrecht'
        profiles = {slug: V.load_profiles()[slug]}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            manifest = root / '.claude-plugin/marketplace.json'
            manifest.parent.mkdir()
            manifest.write_text(json.dumps({'plugins': [{'name': slug, 'source': './' + slug}]}))
            directory = self.fixture(root, slug, profiles[slug])
            originals = {}
            for kind in ('schnellstart', 'hauptproblem'):
                path = directory / f'{slug}-{kind}.md'
                originals[path] = f'# {kind}\r\n\r\nKurzauftrag mit € und Umlauten.\r\n'.encode()
                path.write_bytes(V.block(originals[path].decode(), slug).encode())
            outputs, _ = SYNC.plan(root, profiles)
            for path, content in originals.items():
                self.assertEqual(outputs[path], content)
                self.assertNotIn(V.BEGIN.encode(), outputs[path])
                path.write_bytes(outputs[path])
            repeated, _ = SYNC.plan(root, profiles)
            for path, content in originals.items():
                self.assertEqual(repeated[path], content)


if __name__ == '__main__':
    unittest.main()
