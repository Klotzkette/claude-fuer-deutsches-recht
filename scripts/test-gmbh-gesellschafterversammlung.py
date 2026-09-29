#!/usr/bin/env python3
"""Verhaltenstests für exakte Stimmenrechnungen und die Datei-Schnittstelle."""
from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / 'gmbh-gesellschafterversammlung/tools/stimmenpruefer.py'
SPEC = importlib.util.spec_from_file_location('gmbh_stimmenpruefer', TOOL)
assert SPEC and SPEC.loader
RECHNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RECHNER)


def eingabe(*, basis='abgegebene-gueltige-stimmen', schwelle='1/2', vergleich='>',
            stimmen=((40, 'ja'), (30, 'nein'), (30, 'enthaltung')), ausschluesse=()):
    return {'basis': basis, 'schwelle': schwelle, 'vergleich': vergleich,
            'gesellschafter': [{'id': f'person-{i}', 'stimmen': gewicht, 'votum': votum}
                               for i, (gewicht, votum) in enumerate(stimmen, 1)],
            'ausschluesse': list(ausschluesse)}


class Stimmenrechnung(unittest.TestCase):
    def variante(self, data):
        return RECHNER.calculate(data)['varianten'][0]

    def test_enthaltung_ist_keine_neinstimme(self):
        result = self.variante(eingabe())
        self.assertEqual(result['stimmen'], {'ja': '40', 'nein': '30', 'enthaltung': '30',
                                            'ungueltig': '0', 'abwesend': '0'})
        self.assertEqual((result['nenner'], result['ja_anteil_exakt']), ('70', '4/7'))
        self.assertIs(result['arithmetische_schwelle_erreicht'], True)

    def test_abweichende_nenner_haben_unterschiedliche_folgen(self):
        # Zehn abwesende Stimmen und fünf ungültige Voten bleiben erkennbar.
        stimmen = ((40, 'ja'), (25, 'nein'), (20, 'enthaltung'),
                   (5, 'ungueltig'), (10, 'abwesend'))
        erwartet = {'abgegebene-gueltige-stimmen': ('65', '8/13', True),
                    'vertretenes-stimmberechtigtes-kapital': ('90', '4/9', False),
                    'stimmberechtigtes-gesamtkapital': ('100', '2/5', False),
                    'gesamtkapital': ('100', '2/5', False)}
        for basis, (nenner, anteil, erreicht) in erwartet.items():
            with self.subTest(basis=basis):
                r = self.variante(eingabe(basis=basis, stimmen=stimmen))
                self.assertEqual((r['nenner'], r['ja_anteil_exakt']), (nenner, anteil))
                self.assertIs(r['arithmetische_schwelle_erreicht'], erreicht)

    def test_genau_dreiviertel_und_stimmengleichheit(self):
        faelle = [('3/4', '>=', ((60, 'ja'), (20, 'nein'), (20, 'enthaltung')), True),
                  ('3/4', '>', ((60, 'ja'), (20, 'nein'), (20, 'enthaltung')), False),
                  ('1/2', '>', ((50, 'ja'), (50, 'nein')), False),
                  ('1/2', '>=', ((50, 'ja'), (50, 'nein')), True),
                  (1, '>=', ((100, 'ja'),), True),
                  (1, '>', ((100, 'ja'),), False)]
        for schwelle, vergleich, stimmen, erwartet in faelle:
            with self.subTest(schwelle=schwelle, vergleich=vergleich, stimmen=stimmen):
                r = self.variante(eingabe(schwelle=schwelle, vergleich=vergleich, stimmen=stimmen))
                self.assertIs(r['arithmetische_schwelle_erreicht'], erwartet)

    def test_bruchteile_ohne_gerundete_prozententscheidung(self):
        unterhalb = self.variante(eingabe(schwelle='3/4', vergleich='>=',
                     stimmen=(('74999999999999999999/100000000000000000000', 'ja'),
                              ('25000000000000000001/100000000000000000000', 'nein'))))
        self.assertIs(unterhalb['arithmetische_schwelle_erreicht'], False)
        dezimal = self.variante(eingabe(schwelle='0.75', vergleich='>=',
                                       stimmen=(('0.3', 'ja'), ('0.1', 'nein'))))
        self.assertEqual((dezimal['nenner'], dezimal['ja_anteil_exakt']), ('2/5', '3/4'))
        self.assertIs(dezimal['arithmetische_schwelle_erreicht'], True)

    def test_zwei_streitvarianten_sind_unabhaengig(self):
        data = eingabe(stimmen=((49, 'ja'), (51, 'nein')))
        data['alternative_ausschluesse'] = ['person-2']
        vorher = copy.deepcopy(data)
        mit, ohne = RECHNER.calculate(data)['varianten']
        self.assertEqual(data, vorher, 'Die Eingabe darf nicht verändert werden.')
        self.assertEqual((mit['nenner'], mit['ja_anteil_exakt']), ('100', '49/100'))
        self.assertIs(mit['arithmetische_schwelle_erreicht'], False)
        self.assertEqual((ohne['nenner'], ohne['ja_anteil_exakt']), ('49', '1'))
        self.assertIs(ohne['arithmetische_schwelle_erreicht'], True)
        self.assertEqual(ohne['stimmen']['nein'], '0')
        self.assertEqual([mit['variante'], ohne['variante']],
                         ['ausschluesse', 'alternative_ausschluesse'])

    def test_ausschluss_senkt_nicht_jeden_kapitalnenner(self):
        for basis, erwartet in [('stimmberechtigtes-gesamtkapital', ('49', '1', True)),
                                 ('vertretenes-stimmberechtigtes-kapital', ('49', '1', True)),
                                 ('gesamtkapital', ('100', '49/100', False))]:
            with self.subTest(basis=basis):
                r = self.variante(eingabe(basis=basis, stimmen=((49, 'ja'), (51, 'nein')),
                                          ausschluesse=['person-2']))
                self.assertEqual((r['nenner'], r['ja_anteil_exakt'],
                                  r['arithmetische_schwelle_erreicht']), erwartet)

    def test_nullbasis_liefert_keine_scheinentscheidung(self):
        faelle = [eingabe(stimmen=((70, 'enthaltung'), (30, 'ungueltig'))),
                  eingabe(basis='vertretenes-stimmberechtigtes-kapital', stimmen=((100, 'abwesend'),)),
                  eingabe(basis='stimmberechtigtes-gesamtkapital', stimmen=((100, 'ja'),),
                          ausschluesse=['person-1'])]
        for data in faelle:
            with self.subTest(data=data):
                r = self.variante(data)
                self.assertEqual(r['nenner'], '0')
                self.assertIsNone(r['ja_anteil_exakt'])
                self.assertIsNone(r['arithmetische_schwelle_erreicht'])
        # Bei festem Gesamtkapital bleibt ein Nenner trotz Ausschluss erhalten.
        r = self.variante(eingabe(basis='gesamtkapital', stimmen=((100, 'ja'),),
                                  ausschluesse=['person-1']))
        self.assertEqual(r['ja_anteil_exakt'], '0')
        self.assertIs(r['arithmetische_schwelle_erreicht'], False)

    def test_gewichtsskalierung_und_reihenfolge_aendern_keine_quote(self):
        for basis in sorted(RECHNER.BASES):
            original = eingabe(basis=basis, stimmen=((23, 'ja'), (17, 'nein'),
                                                     (29, 'enthaltung'), (31, 'abwesend')),
                               ausschluesse=['person-2'])
            skaliert = copy.deepcopy(original)
            for person in skaliert['gesellschafter']:
                person['stimmen'] = str(Fraction(person['stimmen']) * Fraction(7, 13))
            skaliert['gesellschafter'].reverse()
            a, b = self.variante(original), self.variante(skaliert)
            with self.subTest(basis=basis):
                self.assertEqual(a['ja_anteil_exakt'], b['ja_anteil_exakt'])
                self.assertEqual(a['arithmetische_schwelle_erreicht'], b['arithmetische_schwelle_erreicht'])

    def test_unvollstaendige_oder_mehrdeutige_eingaben_werden_abgewiesen(self):
        fehler = [None, [], {}, eingabe(schwelle=0), eingabe(schwelle='100/99'),
                  eingabe(schwelle=True), eingabe(schwelle=0.5), eingabe(schwelle='1/0'),
                  eingabe(schwelle='NaN'), eingabe(basis='anwesende'), eingabe(vergleich='='),
                  eingabe(stimmen=()), eingabe(stimmen=((0, 'ja'),)),
                  eingabe(stimmen=((-1, 'ja'),)), eingabe(stimmen=((True, 'ja'),)),
                  eingabe(stimmen=((0.25, 'ja'),)), eingabe(stimmen=((1, 'vielleicht'),)),
                  eingabe(ausschluesse=['unbekannt']),
                  eingabe(ausschluesse=['person-1', 'person-1'])]
        for feld in ['ausschluesse', 'schwelle', 'vergleich', 'basis', 'gesellschafter']:
            data = eingabe()
            del data[feld]
            fehler.append(data)
        for feld, wert in [('unbekannt', 3), ('ausschluesse', 'person-1'),
                           ('alternative_ausschluesse', ['unbekannt'])]:
            data = eingabe()
            data[feld] = wert
            fehler.append(data)
        for mutation in ['id-leer', 'id-doppelt', 'feld-extra']:
            data = eingabe()
            if mutation == 'id-leer':
                data['gesellschafter'][0]['id'] = '  '
            elif mutation == 'id-doppelt':
                data['gesellschafter'][1]['id'] = 'person-1'
            else:
                data['gesellschafter'][0]['rechtslage'] = 'angenommen'
            fehler.append(data)
        for data in fehler:
            with self.subTest(data=data), self.assertRaises(ValueError):
                RECHNER.calculate(data)


class DateiSchnittstelle(unittest.TestCase):
    def aufruf(self, raw, *zusatz):
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / 'Eingabe mit Umlauten ä.json'
            file.write_bytes(raw.encode('utf-8') if isinstance(raw, str) else raw)
            return subprocess.run([sys.executable, str(TOOL), str(file), *zusatz],
                                  capture_output=True, text=True, timeout=10)

    def test_cli_gibt_json_und_nur_arithmetischen_befund_aus(self):
        data = eingabe()
        data['gesellschafter'][0]['id'] = 'Kühnle'
        result = self.aufruf(json.dumps(data, ensure_ascii=False))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, '')
        out = json.loads(result.stdout)
        self.assertEqual(out, RECHNER.calculate(data))
        self.assertIn('nicht rechtlich entschieden', out['hinweis'])
        self.assertNotIn('beschluss_wirksam', out)

    def test_cli_verwirft_doppelte_felder_auch_in_unterobjekten(self):
        raw = json.dumps(eingabe())
        for fehler in [raw.replace('"basis":', '"basis": "gesamtkapital", "basis":', 1),
                       raw.replace('"stimmen": 40', '"stimmen": 1, "stimmen": 40', 1)]:
            result = self.aufruf(fehler)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, '')
            self.assertIn('Doppeltes JSON-Feld', result.stderr)

    def test_cli_fehler_liefern_keine_ergebnisdatei_oder_tracebacks(self):
        raw = json.dumps(eingabe())
        faelle = ['{', 'null', '[1, 2]', raw.replace('"stimmen": 40', '"stimmen": NaN', 1),
                  raw.replace('"stimmen": 40', '"stimmen": Infinity', 1),
                  raw.replace('"stimmen": 40', '"stimmen": 40.0', 1),
                  b'\xff', b' ' * 1_000_001]
        for fehler in faelle:
            with self.subTest(art=str(fehler)[:70]):
                result = self.aufruf(fehler)
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, '')
                self.assertIn('Stimmenprüfung:', result.stderr)
                self.assertNotIn('Traceback', result.stderr)

    def test_cli_aufruf_und_dateifehler(self):
        for args in [[], ['nicht-vorhandene-eingabe.json'], ['eine.json', 'zweite.json']]:
            result = subprocess.run([sys.executable, str(TOOL), *args], capture_output=True,
                                    text=True, timeout=10)
            with self.subTest(args=args):
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, '')
                self.assertIn('Stimmenprüfung:', result.stderr)
                self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
