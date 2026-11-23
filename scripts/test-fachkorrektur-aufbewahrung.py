#!/usr/bin/env python3
"""Prüft die typischen Fristverwechslungen in den veröffentlichten Fachtexten."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def fachtext(plugin, skill):
    return (ROOT / plugin / 'skills' / skill / 'FACHINHALT.md').read_text(encoding='utf-8')


class Aufbewahrungsfristen(unittest.TestCase):
    def test_buchungsbelege_in_der_creator_buchhaltung(self):
        for skill in ('buchhaltung-datev-creator-kontenplan', 'steuerpruefung-creator-buchhaltung-datev'):
            with self.subTest(skill=skill):
                text = fachtext('influencer-recht', skill).lower()
                for document, years in (
                    ('buchungsbelege', r'(?:acht|8)'),
                    ('jahresabschlüsse', r'(?:zehn|10)'),
                    ('geschäftsbriefe', r'(?:sechs|6)'),
                ):
                    self.assertRegex(text, rf'{document}[^.\n]{{0,110}}\b{years}\b')
                self.assertNotRegex(text, r'belege vernichtet vor ablauf (?:10|zehn) jahre')

    def test_gwg_aufbewahrung_statt_zustaendigkeit(self):
        cases = [('nda-abgleich', 'nda-rueckgabe-vernichtung'),
                 ('nda-abgleich', 'rueckgabe-vernichtung-nda-typen'),
                 ('datenschutzrecht', 'datenschutz-loeschpflicht-art-17-aufbewahrung')]
        for plugin, skill in cases:
            with self.subTest(skill=skill):
                text = fachtext(plugin, skill)
                self.assertIn('gwg_2017/__8.html', text)
                self.assertNotRegex(text, re.compile(r'(?:§\s*(?:17|50)\s+GwG|GwG\s+§\s*(?:17|50))\b', re.I))

    def test_rechnungen_und_stundenzettel(self):
        rechnung = fachtext('mittelstand-corporate-ma', 'mittelstand-ma-erechnung-gobd')
        self.assertIn('ustg_1980/__14b.html', rechnung)
        self.assertNotRegex(rechnung.lower(), r'(?:archivierung (?:10|zehn) jahre|(?:10|zehn) jahre für rechnungen)')
        zeiten = fachtext('kanzlei-allgemein', 'timesheet-aktenzeitung-umgang-ki')
        self.assertIn('Handakte', zeiten)
        self.assertIn('Buchungsbeleg', zeiten)
        self.assertNotRegex(zeiten, r'(?i)(?:10|zehn) Jahre für Buchungsbelege')


if __name__ == '__main__':
    unittest.main()
