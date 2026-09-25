#!/usr/bin/env python3
"""Regression für die Verwechslung der Fanpage- und Schrems-Entscheidungen."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / 'datenschutzrecht'
SKILLS = (
    'avv-rolemix-getrennt-vs-gemeinsam',
    'avv-rolemix-getrennt-vs-gemeinsam-verantwortlich',
    'avv-art-26-joint-controllership-deutsch',
    'avv-konzern-und-multi-party-konstellation',
    'dpa-en-controller-tmpl',
    'dpa-en-controller-controller-tmpl',
    'joint-controllership-en-template',
)


class FanpageQuellenTests(unittest.TestCase):
    def test_all_affected_skills_identify_the_correct_judgment(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                text = (PLUGIN / 'skills' / name / 'SKILL.md').read_text()
                self.assertNotIn('C-498/16', text)
                self.assertIn('C-210/16', text)
                self.assertIn('05.06.2018', text)
                self.assertIn('ECLI:EU:C:2018:388', text)
                self.assertIn('../../references/fanpage-entscheidung-quellenpruefung.md', text)

    def test_no_blanket_verification_claim_survives_in_affected_skills(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                text = (PLUGIN / 'skills' / name / 'SKILL.md').read_text()
                self.assertNotRegex(text, r'– (?:verifiziert|verified case numbers|verified[.])')
                self.assertIn('95/46', text)

    def test_legitimate_schrems_identity_is_preserved_and_distinguished(self):
        text = (PLUGIN / 'references' / 'fanpage-entscheidung-quellenpruefung.md').read_text()
        self.assertIn('25.01.2018 - Az. C-498/16, ECLI:EU:C:2018:37', text)
        self.assertIn('05.06.2018 - Az. C-210/16, ECLI:EU:C:2018:388', text)
        self.assertIn('25.09.2026', text)
        self.assertIn('cp180081de.pdf', text)
        self.assertIn('cp180007de.pdf', text)
        self.assertIn('keine Randnummer', text)


if __name__ == '__main__':
    unittest.main()
