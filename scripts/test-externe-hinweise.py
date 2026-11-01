#!/usr/bin/env python3
"""Konkrete Rückfallbeispiele und zulässige Altjahre der Eigenprüfung."""
import importlib.util
import sys
import unittest
from pathlib import Path

path = Path(__file__).with_name('validate-current-law-sentinels.py')
spec = importlib.util.spec_from_file_location('eigenpruefung_sentinels', path)
law = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = law
spec.loader.exec_module(law)


class RechtsstandRegressionen(unittest.TestCase):
    def test_fehler_und_zulaessige_abgrenzung(self):
        examples = (
            ('Geschenke an Nichtarbeitnehmer',
             'Geschenke an Nichtarbeitnehmer: Freigrenze 35 Euro',
             'Geschenke: Altgrenze bis 2023 35 Euro; ab 2024 50 Euro.'),
            ('nicht vorhandener Absatz',
             'Paragraf 3 Abs. 1 Nr. 16 EStG', 'Paragraf 3 Nummer 16 EStG'),
            ('aktuelle Lizenzschranke',
             'Paragraf 4j EStG: Lizenzschranke prüfen',
             'Paragraf 4j EStG a.F.: Lizenzschranke letztmals VZ 2024.'),
            ('Drei-Jahres-Laufzeit',
             'BZSt-Freistellungsbescheinigung gilt drei Jahre.',
             'Paragraf 50c EStG: Freistellungsbescheinigung höchstens fünf Jahre.'),
            ('DAC8-Gesetzesabkürzung',
             'KryptoStG', 'Kryptowerte-Steuertransparenz-Gesetz (KStTG)'),
            ('Cloud-Wechselrecht',
             'Data Act Art. 17: Wechselrecht',
             'Artikel 17 betrifft behördliche Datenverlangen; Kapitel VI betrifft Cloud-Wechsel.'),
        )
        for label, wrong, correct in examples:
            sentinel = next(item for item in law.SENTINELS if label in item.label)
            with self.subTest(label=label):
                self.assertIsNotNone(sentinel.pattern.search(wrong))
                self.assertIsNone(sentinel.pattern.search(correct))

    def test_andere_freistellungen_bleiben_ausgenommen(self):
        sentinel = next(item for item in law.SENTINELS if 'Drei-Jahres-Laufzeit' in item.label)
        self.assertIsNone(sentinel.pattern.search('Paragraf 48b: BZSt-Freistellungsbescheinigung drei Jahre'))
        self.assertIsNone(sentinel.pattern.search('BZSt-Freistellungsbescheinigung galt früher drei Jahre'))

    def test_muster_und_vorfilter_sind_vollstaendig(self):
        self.assertEqual(len(law.SENTINELS), len(law.SENTINEL_HINTS))


if __name__ == '__main__':
    unittest.main()
