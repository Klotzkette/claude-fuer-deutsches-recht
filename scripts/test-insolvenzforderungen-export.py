#!/usr/bin/env python3
"""Prüft Rechengenauigkeit, sichere Übergaben und getrennte Prüfstände."""
from copy import deepcopy
from datetime import date
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "insolvenzforderungen-checker/scripts/forderungsexport.py"
SPEC = importlib.util.spec_from_file_location("forderungsexport", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def sample():
    return {"schema_version": 1,
            "verfahren": {"aktenzeichen": "71 IN 1/26", "schuldner": "Verfahren GmbH", "gericht": "Amtsgericht Köln", "eroeffnung": "2026-07-01", "anmeldefrist": "2026-08-14", "stichtag": "2026-09-10"},
            "forderungen": [{"id": "F-0006", "tabellenblatt": 6, "glaeubiger": "Lieferant GmbH", "eingang": "2026-08-10", "rang_angemeldet": "Paragraf 38 InsO", "hauptforderung": "14280.00", "zinsen": "0.00", "kosten": "0.00", "unerlaubte_handlung": "0.00", "grund": "Warenlieferung, Rechnung 17", "belege": ["Rechnung 17", "Zahlung 3570 EUR", "Gutschrift 1190 EUR"], "tituliert": False, "titel_bei_den_akten": False, "fuer_den_ausfall": False, "sicherheit": "Keine angemeldet.", "pruefung": {"status": "vorschlag", "nicht_bestritten": "9520.00", "bestritten": "4760.00", "begruendung": "Zahlung und Gutschrift sind belegt; Prüfungsvorschlag, keine Feststellung."}}]}


def template():
    # Technische Schema-Fixture, kein versandfähiges Muster und keine amtlichen Stammdaten.
    return '''<nachricht.inso.insolvenztabelle.uebergabe.0300005 xmlns="http://www.xjustiz.de">
<nachrichtenkopf xjustizVersion="3.6.2">
<erstellungszeitpunkt>2026-10-01T12:00:00Z</erstellungszeitpunkt>
<absender><informationen><auswahl_kommunikationspartner><sonstige>Verwaltung</sonstige></auswahl_kommunikationspartner></informationen><eigeneNachrichtenID>00000000-0000-4000-8000-000000000001</eigeneNachrichtenID></absender>
<empfaenger><informationen><auswahl_kommunikationspartner><gericht listVersionID="2026-01-01"><code>G-FIXTURE</code></gericht></auswahl_kommunikationspartner></informationen><auswahl_aktenzeichen><aktenzeichen.freitext>71 IN 1/26</aktenzeichen.freitext></auswahl_aktenzeichen></empfaenger>
<ereignis listVersionID="3.7"><code>044</code></ereignis><herstellerinformation><nameDesProdukts>Fixture</nameDesProdukts><herstellerDesProdukts>Fixture</herstellerDesProdukts><version>1</version></herstellerinformation></nachrichtenkopf>
<grunddaten><verfahrensdaten><beteiligung><rolle><rollennummer>R1</rollennummer></rolle><beteiligter><beteiligtennummer>B1</beteiligtennummer><auswahl_beteiligter><organisation><bezeichnung><bezeichnung.aktuell>Lieferant GmbH</bezeichnung.aktuell></bezeichnung></organisation></auswahl_beteiligter></beteiligter></beteiligung></verfahrensdaten></grunddaten>
<fachdaten><beteiligte.inso><beteiligter><ref.beteiligtennummer>B1</ref.beteiligtennummer></beteiligter><identifier>G-0001</identifier><zustellungsart><code>001</code></zustellungsart><uebertragungsweg><code>001</code></uebertragungsweg><postempfaenger>true</postempfaenger></beteiligte.inso></fachdaten>
</nachricht.inso.insolvenztabelle.uebergabe.0300005>'''.replace('<code>', '<code xmlns="">')


class ExportTests(unittest.TestCase):
    def test_decimal_and_partial_dispute(self):
        data = MODULE.validate(sample())
        self.assertIn(b"14280,00;vorschlag;9520,00;4760,00", MODULE.neutral_exports(data)["Prueftabelle.csv"])
        for value in (14280, 14280.00, "14.280,00", "NaN", "-1.00", "1.001", "1e2"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                MODULE.amount(value)

    def test_invalid_totals_and_judicial_status_rejected(self):
        data = sample()
        data["forderungen"][0]["pruefung"]["bestritten"] = "4759.99"
        with self.assertRaisesRegex(ValueError, "gesamte Anmeldung"):
            MODULE.validate(data)
        data = sample()
        data["forderungen"][0]["pruefung"]["status"] = "festgestellt"
        with self.assertRaisesRegex(ValueError, "gerichtliche Feststellung"):
            MODULE.validate(data)

    def test_late_claim_is_kept_and_security_is_not_deducted(self):
        data = sample()
        c = data["forderungen"][0]
        c.update(eingang="2026-09-01", sicherheit="Abtretung; erwarteter Erlös 12000 EUR", hauptforderung="48000.00", fuer_den_ausfall=True)
        c["pruefung"] = {"status": "offen", "begruendung": "Verwertung noch nicht abgeschlossen."}
        csv = MODULE.neutral_exports(MODULE.validate(data))["Prueftabelle.csv"].decode("utf-8-sig")
        self.assertIn("2026-09-01;ja;", csv)
        self.assertIn("48000,00", csv)
        self.assertNotIn("36000,00", csv)

    def test_duplicate_and_unknown_keys_dates_and_booleans(self):
        data = sample()
        data["forderungen"].append(deepcopy(data["forderungen"][0]))
        with self.assertRaises(ValueError):
            MODULE.validate(data)
        for key, value in (("tituliert", "false"), ("eingang", "20260710"), ("titel_bei_den_akten", True), ("tabellenblatt", True), ("unerlaubte_handlung", "99999.00"), ("falsch", "nicht verlieren")):
            data = sample()
            data["forderungen"][0][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                MODULE.validate(data)
        with self.assertRaises(ValueError):
            MODULE.unique_object([("id", 1), ("id", 2)])

    def test_xml_escaping_formula_safety_and_no_overwrite(self):
        data = sample()
        data["forderungen"][0]["glaeubiger"] = '=HYPERLINK("x"); Müller & Söhne'
        outputs = MODULE.neutral_exports(data)
        self.assertIn(b"'=HYPERLINK", outputs["Prueftabelle.csv"])
        root = ET.fromstring(outputs["Pruefdaten_INTERN.xml"])
        self.assertEqual(root.findtext("forderungen/eintrag/glaeubiger"), data["forderungen"][0]["glaeubiger"])
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory) / "export"
            MODULE.export(data, dest)
            before = {p.name: p.read_bytes() for p in dest.iterdir()}
            with self.assertRaises(ValueError):
                MODULE.export(data, dest)
            self.assertEqual(before, {p.name: p.read_bytes() for p in dest.iterdir()})
            report = json.loads((dest / "Pruefprotokoll.json").read_text())
            self.assertFalse(report["versandfreigabe"])

    def test_interest_and_cost_grounds_cannot_disappear(self):
        data = sample()
        c = data["forderungen"][0]
        c["zinsen"] = "1.01"
        c["pruefung"] = {"status": "offen", "begruendung": "Zinszeitraum noch zu prüfen."}
        with self.assertRaisesRegex(ValueError, "Begründung"):
            MODULE.validate(data)
        c["zinsgrund"] = "Zeitraum 1. bis 3. Mai; Berechnung Blatt 4"
        MODULE.validate(data)

    @unittest.skipUnless(os.getenv("XJUSTIZ_XSD"), "Amtliches XSD-Paket für gesonderte Integrationsprüfung erforderlich.")
    def test_real_xjustiz_xsd_and_guardrails(self):
        data = sample()
        data["xjustiz"] = {"empfaenger_code": "G-FIXTURE", "waehrungsliste_version": "2024-01-01"}
        data["forderungen"][0]["xjustiz"] = {"rollennummer": "R1", "beteiligtennummer": "B1", "beteiligtenkennung": "G-0001", "rang_code": "001"}
        schema = Path(os.environ["XJUSTIZ_XSD"])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stammdaten.xml"
            path.write_text(template())
            output = MODULE.xjustiz_export(data, path, schema, date(2026, 10, 1))
            root = ET.fromstring(output)
            ns = {"x": MODULE.NS}
            self.assertEqual(root.findtext("x:fachdaten/x:forderung/x:hauptforderung/x:betrag/x:zahl", namespaces=ns), "14280.00")
            self.assertEqual(root.findall(".//x:erklaerung", ns), [])
            self.assertNotIn(b"9520", output)
            self.assertNotIn(b"4760", output)
            for old, new in (('>044</code>', '>043</code>'), ("71 IN 1/26", "71 IN 2/26"), ("<identifier>G-0001", "<identifier>G-0002"), ("3.6.2", "3.5.1")):
                path.write_text(template().replace(old, new))
                with self.subTest(old=old), self.assertRaises(ValueError):
                    MODULE.xjustiz_export(data, path, schema, date(2026, 10, 1))
            path.write_text(template())
            data["forderungen"][0]["xjustiz"]["rang_code"] = "999"
            with self.assertRaisesRegex(ValueError, "XSD"):
                MODULE.xjustiz_export(data, path, schema, date(2026, 10, 1))
            path.write_text('<!DOCTYPE x [<!ENTITY ext SYSTEM "file:///etc/passwd">]>' + template())
            with self.assertRaisesRegex(ValueError, "DTD"):
                MODULE.xjustiz_export(data, path, schema, date(2026, 10, 1))
            with self.assertRaisesRegex(ValueError, "Gültigkeitszeitraum"):
                MODULE.xjustiz_export(data, path, schema, date(2027, 4, 30))


if __name__ == "__main__":
    unittest.main()
