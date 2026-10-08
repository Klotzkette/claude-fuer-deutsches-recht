#!/usr/bin/env python3
"""Redaktionelle Regressionen für Kanzleistart und Posteingangszuordnung.

Diese Prüfungen kontrollieren Anweisungsverträge, keine Modellleistung oder
Produktivkonten. Laufzeittests der Hilfsprogramme werden getrennt ausgeführt.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'ki-native-kanzlei'


class StartContracts(unittest.TestCase):
    def read(self, name):
        return (PLUGIN / name).read_text(encoding='utf-8')

    def test_individual_entry_and_routing(self):
        main = self.read('skills/ki-kanzlei-steuern/SKILL.md')
        for skill, command in [
            ('kanzlei-gruenden-einrichten', 'kanzlei-starten'),
            ('posteingang-mandate-zuordnen', 'posteingang'),
        ]:
            self.assertIn(skill, main)
            self.assertIn(skill, self.read(f'commands/{command}.md'))
            text = self.read(f'skills/{skill}/SKILL.md')
            self.assertEqual(re.findall(r'^## ([1-6])\.', text, re.M), list('123456'))
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
                if not target.startswith(('https://', 'http://', '#')):
                    self.assertTrue((PLUGIN / 'skills' / skill / target.split('#')[0]).exists(), target)

    def test_setup_does_not_claim_automatic_readiness(self):
        text = self.read('skills/kanzlei-gruenden-einrichten/SKILL.md')
        for required in ['Paragraf 59f BRAO', 'Paragraf 51 BRAO', 'Arbeitskopie',
                         'keine Änderung in der Kanzleisoftware', 'isolierten Verzeichnis',
                         'niemals den produktiven Bestand', 'keinen Hintergrunddienst',
                         'Zugangsdaten werden nie erfragt']:
            self.assertIn(required, text)
        self.assertIn('noch nicht geprüft', text)

    def test_inbox_scope_and_recovery_remain_explicit(self):
        text = self.read('skills/posteingang-mandate-zuordnen/SKILL.md')
        for required in ['Message-ID', 'Anhänge', 'eEB', 'CC/BCC', 'Timeout']:
            self.assertIn(required, text)
        self.assertRegex(text, r'(?i)(seitenweise|Seitennavigation|Seiten|paginier)')
        self.assertRegex(text, r'(?i)(Überlappung|überlappend)')
        self.assertIn('Bei unklarem Ausgang halte die Wiederholung an', text)

    def test_organisation_preserves_separate_send_approval(self):
        text = self.read('assets/kanzleiorganisation-vorlage.md')
        self.assertNotIn('Die Maschine versendet auf keiner Stufe', text)
        for required in ['beA', 'eEB', 'Freigabe', 'Wiederherstellung', 'führend']:
            self.assertIn(required, text)

    def test_compact_prompts_and_plain_text_match(self):
        for kind in ['werkstatt', 'schnellstart', 'hauptproblem']:
            path = PLUGIN / f'ki-native-kanzlei-{kind}.md'
            self.assertEqual(path.read_bytes(), path.with_suffix('.txt').read_bytes())
            if kind != 'werkstatt':
                self.assertLessEqual(len(path.read_bytes()), 7500)
            for term in ['Kanzlei', 'Probemandat', 'beA']:
                self.assertIn(term, path.read_text())


if __name__ == '__main__':
    unittest.main()
