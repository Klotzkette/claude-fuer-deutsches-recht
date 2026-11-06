#!/usr/bin/env python3
"""Prüft den normalen UStVA-Ausgabeaufruf und die Grenzen des XML-Prüfwegs."""

import copy
import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "steuerrecht-anwalt-und-berater/ustva/werkzeuge/ustva_ausgabe.py"
NAMESPACE = "http://finkonsens.de/elster/elsteranmeldung/ustva/v2025"


def reviewed_data():
    definitions = {
        "81": {"label": "Bemessungsgrundlage 19 Prozent", "unit": "EUR", "semantic": "base_19", "allow_negative": True},
        "66": {"label": "Abziehbare Vorsteuer", "unit": "EUR_CENT", "semantic": "input_tax", "allow_negative": True},
        "83": {"label": "Vorauszahlung", "unit": "EUR_CENT", "semantic": "tax_due", "allow_negative": True},
    }
    return {
        "schema_version": 1,
        "year": 2025,
        "period": "Q4",
        "taxpayer": {"name": "Übungsunternehmer", "steuernummer": "072/000/00000"},
        "approval_status": "reviewed",
        "mapping": {"year": 2025, "source": "Amtliches Jahresformular 2025, geprüfte Zuordnung",
                    "reviewed_on": "2026-11-06", "fields": definitions},
        "fields": [{"kennzahl": number, "label": definitions[number]["label"], "unit": definitions[number]["unit"],
                    "amount": value, "source": "Rechnungsmatrix, Einzelbelege 1 bis 3"}
                   for number, value in (("81", "1000"), ("66", "212.34"), ("83", "-22.34"))],
        "arithmetic": [{"id": "zahllast", "result_field": "83", "terms": [
            {"field": "81", "factor": "0.19"}, {"field": "66", "factor": "-1"}], "rounding": "HALF_UP"}],
        "reconciliation": [{"id": "belegabgleich", "actual": "-22.34", "expected": "-22.34", "source": "Unabhängiger Belegabgleich"}],
    }


class UStvaOutputTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)

    def run_helper(self, data, *extra):
        source = self.directory / "input.json"
        source.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        output = self.directory / "ausgabe"
        result = subprocess.run([sys.executable, str(HELPER), str(source), "--out", str(output), *map(str, extra)],
                                text=True, capture_output=True, timeout=20)
        return result, output

    def assert_rejected(self, data, *extra):
        result, output = self.run_helper(data, *extra)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertFalse(output.exists(), result.stderr)
        self.assertFalse(list(self.directory.glob(".ausgabe.*")))

    def test_normal_entry_point_keeps_refund_sign_and_unsubmitted_state(self):
        result, output = self.run_helper(reviewed_data())
        self.assertEqual(result.returncode, 0, result.stderr)
        with (output / "ustva_2025_Q4_erfassung.csv").open(encoding="utf-8-sig") as stream:
            rows = list(csv.DictReader(stream, delimiter=";"))
        self.assertEqual(rows[-1]["Wert"], "-22,34")
        report = json.loads((output / "ustva_2025_Q4_arbeitsstand.json").read_text())
        self.assertFalse(report["transmission"]["performed"])
        self.assertIsNone(report["transmission"]["receipt"])
        self.assertEqual(report["status"], "prepared_not_transmitted")
        original = (output / "ustva_2025_Q4_erfassung.csv").read_bytes()
        result, _ = self.run_helper(reviewed_data())
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((output / "ustva_2025_Q4_erfassung.csv").read_bytes(), original)

    def test_rejects_duplicate_or_unreviewed_field_semantics(self):
        cases = []
        duplicated = reviewed_data()
        duplicated["fields"].append(copy.deepcopy(duplicated["fields"][0]))
        cases.append(duplicated)
        wrong_unit = reviewed_data()
        wrong_unit["fields"][0]["unit"] = "EUR_CENT"
        cases.append(wrong_unit)
        wrong_meaning = reviewed_data()
        wrong_meaning["fields"][0]["label"] = "Umsatzsteuer statt Bemessungsgrundlage"
        cases.append(wrong_meaning)
        unknown = reviewed_data()
        unknown["fields"][0]["kennzahl"] = "999"
        cases.append(unknown)
        for data in cases:
            with self.subTest(data=data["fields"][0]):
                self.assert_rejected(data)

    def test_rejects_money_errors_and_inconsistent_reconciliation(self):
        for value in ("NaN", "1,00", "1000.001", "1e3"):
            with self.subTest(value=value):
                data = reviewed_data()
                data["fields"][0]["amount"] = value
                self.assert_rejected(data)
        data = reviewed_data()
        data["fields"][-1]["amount"] = "22.34"
        self.assert_rejected(data)
        data = reviewed_data()
        data["reconciliation"][0]["expected"] = "-23.34"
        self.assert_rejected(data)

    def xml_files(self):
        # Kleine technische Testschema-Fixture, kein amtliches ELSTER-Jahresschema.
        schema = self.directory / "fixture.xsd"
        schema.write_text(f'''<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="{NAMESPACE}" xmlns:u="{NAMESPACE}" elementFormDefault="qualified">
<xs:element name="Anmeldungssteuern"><xs:complexType><xs:sequence><xs:element name="Steuerfall"><xs:complexType><xs:sequence>
<xs:element name="Steuernummer" type="xs:string"/>
<xs:element name="Jahr" type="xs:string"/><xs:element name="Zeitraum" type="xs:string"/>
<xs:element name="Kz81" type="xs:decimal"/><xs:element name="Kz66" type="xs:decimal"/><xs:element name="Kz83" type="xs:decimal"/>
<xs:element name="Kz88" type="xs:decimal" minOccurs="0"/>
<xs:element name="Erstellungsdatum" type="xs:string" minOccurs="0"/>
</xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute name="version" type="xs:string" use="required"/></xs:complexType></xs:element></xs:schema>''')
        xml = self.directory / "import.xml"
        xml.write_text(f'''<?xml version="1.0" encoding="ISO-8859-15"?><Anmeldungssteuern xmlns="{NAMESPACE}" version="2025"><Steuerfall><Steuernummer>2807200000000</Steuernummer><Jahr>2025</Jahr><Zeitraum>44</Zeitraum><Kz81>1000</Kz81><Kz66>212.34</Kz66><Kz83>-22.34</Kz83></Steuerfall></Anmeldungssteuern>''', encoding="iso-8859-15")
        data = reviewed_data()
        data["taxpayer"]["steuernummer"] = "28/072/00000000"
        data["mapping"]["xml"] = {
            "namespace": NAMESPACE, "version": "2025", "year_path": "./u:Steuerfall/u:Jahr",
            "period_path": "./u:Steuerfall/u:Zeitraum", "period": "Q4", "period_value": "44",
            "fields": {number: f"./u:Steuerfall/u:Kz{number}" for number in ("81", "66", "83")},
            "taxpayer": {"steuernummer": "./u:Steuerfall/u:Steuernummer"}, "metadata": {},
        }
        return data, xml, schema

    def test_xml_requires_both_schema_and_exact_working_values(self):
        data, xml, schema = self.xml_files()
        result, output = self.run_helper(data, "--import-xml", xml, "--xsd", schema)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads((output / "ustva_2025_Q4_xml_pruefung.json").read_text())
        self.assertFalse(report["annual_plausibility_validated"])
        self.assertFalse(report["portal_acceptance_verified"])
        self.assertFalse(report["transmitted"])
        self.assertEqual((output / "ustva_2025_Q4_import.xml").read_bytes(), xml.read_bytes())
        other = self.directory / "other"
        output.rename(other)
        xml.write_text(xml.read_text(encoding="iso-8859-15").replace("<Kz83>-22.34", "<Kz83>99.99"), encoding="iso-8859-15")
        self.assert_rejected(data, "--import-xml", xml, "--xsd", schema)

    def test_xml_blocks_doctype_and_remote_schema_dependencies(self):
        data, xml, schema = self.xml_files()
        xml.write_text(f'''<!DOCTYPE secret [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><Anmeldungssteuern xmlns="{NAMESPACE}" version="2025">&xxe;</Anmeldungssteuern>''')
        self.assert_rejected(data, "--import-xml", xml, "--xsd", schema)
        data, xml, schema = self.xml_files()
        schema.write_text('''<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"><xs:include schemaLocation="https://example.invalid/remote.xsd"/></xs:schema>''')
        self.assert_rejected(data, "--import-xml", xml, "--xsd", schema)

    def test_xml_rejects_wrong_taxpayer_and_extra_schema_valid_tax_fields(self):
        data, xml, schema = self.xml_files()
        original = xml.read_text(encoding="iso-8859-15")
        xml.write_text(original.replace("2807200000000", "2807200000001"), encoding="iso-8859-15")
        self.assert_rejected(data, "--import-xml", xml, "--xsd", schema)
        xml.write_text(original.replace("</Steuerfall>", "<Kz88>99.99</Kz88></Steuerfall>"), encoding="iso-8859-15")
        self.assert_rejected(data, "--import-xml", xml, "--xsd", schema)
        data["mapping"]["xml"]["metadata"] = {"./u:Steuerfall/u:Kz88": "99.99"}
        self.assert_rejected(data, "--import-xml", xml, "--xsd", schema)
        data["mapping"]["xml"]["metadata"] = {}
        xml.write_text(original.replace("</Steuerfall>", "<Erstellungsdatum>20261106</Erstellungsdatum></Steuerfall>"), encoding="iso-8859-15")
        self.assert_rejected(data, "--import-xml", xml, "--xsd", schema)


if __name__ == "__main__":
    unittest.main()
