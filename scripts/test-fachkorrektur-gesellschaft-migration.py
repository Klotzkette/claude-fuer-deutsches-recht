#!/usr/bin/env python3
"""Regressionsfälle aus den externen Hinweisen #721 und #722."""
import importlib
import json
import re
import unittest
from pathlib import Path

import main_skill_revisions as revisions


ROOT = Path(__file__).resolve().parents[1]
MIGRATION = "fachanwalt-migrationsrecht"


def fachtext(plugin, skill):
    source = (ROOT / plugin / "skills" / skill / "FACHINHALT.md").read_text(encoding="utf-8")
    return " ".join(source.casefold().replace("paragraf", "§").split())


class Gesellschaftsrecht(unittest.TestCase):
    def test_mischgruendung_und_unternehmergesellschaft(self):
        text = fachtext("gesellschaftsgruender", "gmbh-vorbereitung")
        # Ein Baranteil von 15.000 EUR, ein voll geleisteter Sachanteil von 10.000.
        baranteil, sachanteil = 15000, 10000
        mindestbar = max(baranteil // 4, 12500 - sachanteil)
        beispiel = re.search(r"15\.000.{0,80}10\.000.{0,120}3\.750.{0,160}13\.750", text)
        self.assertIsNotNone(beispiel)
        self.assertEqual(mindestbar, 3750)
        self.assertRegex(text, r"ug.{0,150}(?:voll|gesamte).{0,100}geld.{0,70}sacheinlagen.{0,30}ausgeschlossen")

    def test_einladungsmangel_und_geltendmachung(self):
        text = fachtext("gesellschaftsrecht", "gesellschafterbeschluss")
        self.assertRegex(text, r"121 abs\. 4 satz 2.{0,110}nicht geladen.{0,90}genehmig")
        self.assertRegex(text, r"242 abs\. 2 satz 4")
        self.assertRegex(text, r"gmbh.{0,90}satzung.{0,170}monat")
        self.assertRegex(text, r"ag.{0,65}monat ab beschlussfassung")
        self.assertRegex(text, r"gmbh: drei viertel der abgegebenen stimmen.{0,240}53 abs\. 2")
        self.assertRegex(text, r"ag: neben der stimmenmehrheit.{0,65}vertretenen grundkapitals")
        self.assertRegex(text, r"aktiennennbeträgen, bei stückaktien nach deren zahl.{0,30}134 abs\. 1")
        self.assertRegex(text, r"notarielle beurkundung der satzungsänderung.{0,30}53 abs\. 3 satz 1")

    def test_kapitalerhoehung_gegen_bareinlagen(self):
        text = fachtext("gesellschaftsgruender", "kapitalerhoehung-bezugsrecht")
        self.assertRegex(text, r"je neuem baranteil mindestens ein viertel")
        self.assertRegex(text, r"56a gmbhg.{0,85}7 abs\. 2 satz 1.{0,20}abs\. 3")
        self.assertRegex(text, r"12\.500.{0,100}kapitalerhöhung einer gmbh nicht")

    def test_innenhaftung_verjaehrung_und_uebergang(self):
        text = fachtext("gesellschaftsrecht", "geschaeftsfuehrer-haftung-43-gmbhg")
        self.assertRegex(text, r"schaden[s]? dem grunde nach")
        self.assertRegex(text, r"fünf jahre.{0,75}kenntnis.{0,45}jahresende")
        self.assertRegex(text, r"103m eginso.{0,90}zahlungen vor dem 1\. januar 2021")
        self.assertRegex(text, r"15b.{0,200}(?:gesellschaft|insolvenzverwalter)")


class Migrationsrecht(unittest.TestCase):
    def test_asylantrag_vor_und_ab_umstellung(self):
        for skill in ("mandat-triage-migrationsrecht", "abschiebungsabwehr",
                      "fachanwalt-migrationsrecht-abschiebungsabwehr"):
            with self.subTest(skill=skill):
                text = fachtext(MIGRATION, skill)
                self.assertRegex(text, r"12\. juni 2026.{0,100}zwei wochen")
                self.assertRegex(text, r"eine woche.{0,165}34a abs\. 3 satz 1")
                self.assertRegex(text, r"67 abs\. 7 buchst\. a")
                self.assertRegex(text, r"belehrung.{0,140}drei monaten?")
                self.assertRegex(text, r"87e asylg.{0,45}79 abs\. 3")

    def test_blaue_karte_grundschwelle_und_zustimmung(self):
        for skill in ("aufenthaltstitel-pruefung", "aufenthaltstitel-antrag",
                      "fachanwalt-migrationsrecht-aufenthaltstitel-antrag"):
            with self.subTest(skill=skill):
                text = fachtext(MIGRATION, skill)
                self.assertRegex(text, r"50\s*%.{0,120}2026.{0,14}50\.700")
                self.assertRegex(text, r"45,3\s*%.{0,120}2026.{0,14}45\.934,20")
                self.assertRegex(text, r"(?:zustimmung.{0,160}18g abs\. 1 satz 2|18g abs\. 1 satz 2.{0,160}zustimmung)")
                self.assertRegex(text, r"(?:isco|engpass).{0,160}(?:drei|3) jahre")
                self.assertRegex(text, r"abs\. 2.{0,180}(?:berufserfahrung|berufspraxis)")

    def test_visum_neuantrag_wahrt_klagefrist_nicht(self):
        for skill in ("mandat-triage-migrationsrecht", "remonstration-visum",
                      "visum-national-d", "workflow-botschaft-visumtermin"):
            with self.subTest(skill=skill):
                text = fachtext(MIGRATION, skill)
                self.assertIn("1. juli 2025", text)
                self.assertIn("klagefrist", text)
                self.assertRegex(text, r"(?:neuantrag|neuer visumantrag|erneute antragstellung).{0,100}"
                                       r"(?:nicht|keine)|klagefrist.{0,90}unabhängig vom neuantrag")

    def test_folgeantrag_separates_vorpruefungsverfahren(self):
        for skill in ("asyl-folgeantrag-71", "fachanwalt-migrationsrecht-asyl-folgeantrag-71"):
            with self.subTest(skill=skill):
                text = fachtext(MIGRATION, skill)
                self.assertRegex(text, r"(?:vorprüfung|71 abs\. 1 asylg).{0,90}art\. 55")
                self.assertRegex(text, r"dreimonatige ausschlussfrist.{0,90}nicht vor")

    def test_anspruchseinbuergerung_in_der_orientierung(self):
        orientierungen = ("orientierung-fachanwaltschaft-mandat", "fachanwalt-migrationsrecht-orientierung")
        quellen = [ROOT / MIGRATION / "skills" / name / "FACHINHALT.md" for name in orientierungen]
        quellen.append(ROOT / "testakten" / "megaprompts" / f"{MIGRATION}.md")
        for quelle in quellen:
            with self.subTest(datei=quelle):
                text = quelle.read_text(encoding="utf-8").lower()
                self.assertRegex(text, r"anspruchseinbürgerung nach fünf jahren rechtmäßigen gewöhnlichen aufenthalts")
                self.assertNotRegex(text, r"acht jahre\s*/\s*verkürzbar")

    def test_gerichtskosten_und_gegenstandswert(self):
        text = fachtext(MIGRATION, "erstgespraech-mandatsannahme")
        self.assertIn("keine gerichtskosten", text)
        self.assertRegex(text, r"5\.000 euro.{0,70}77 abs\. 4 satz 1 asylg.{0,15}10\.000 euro")
        self.assertRegex(text, r"vorläufigen rechtsschutz.{0,25}2\.500 euro")
        self.assertRegex(text, r"weiterer person.{0,40}1\.000.{0,25}500 euro")


class HistorischeFassungen(unittest.TestCase):
    def test_mini_und_werkstatt_mit_alter_und_neuer_pruefung(self):
        profile = json.loads((ROOT / "quality/evals/gesellschaftsgruender.json").read_bytes())
        for field, kind in (("mini_review", "schnellstart"), ("workshop_review", "werkstatt")):
            relative = Path(f"gesellschaftsgruender/gesellschaftsgruender-{kind}.md")
            path = ROOT / relative
            previous = profile["review_history"][-1][field]["sha256"]
            self.assertEqual(revisions.digest(revisions.historical_bytes(ROOT, path, previous)), previous)
            self.assertNotEqual(previous, profile[field]["sha256"])
            self.assertEqual(revisions.digest(path.read_bytes()), profile[field]["sha256"])

    def test_veroeffentlichte_vollpruefung_liefert_korrigierten_auszug(self):
        render = importlib.import_module("generate-megaprompt")
        for plugin, skill in (("gesellschaftsgruender", "gruendungsassistent-erstpruefung-und-mandatsziel"),
                              ("fachanwalt-handels-gesellschaftsrecht", "erstgespraech-mandatsannahme"),
                              (MIGRATION, "mandat-triage-migrationsrecht"),
                              (MIGRATION, "orientierung-fachanwaltschaft-mandat"),
                              (MIGRATION, "fachanwalt-migrationsrecht-orientierung"),
                              (MIGRATION, "erstgespraech-mandatsannahme")):
            source = ROOT / plugin / "skills" / skill / "FACHINHALT.md"
            fm, body = render.extract_frontmatter_and_body(source.read_text())
            section = render.render_skill(source, render.get_description(fm), body)
            mega = (ROOT / f"testakten/megaprompts/{plugin}.md").read_text()
            self.assertEqual(mega.count(section), 1, (plugin, skill))

    def test_beide_register_und_jede_vorfassung(self):
        for topic in ("gesellschaft-und-gruendung", "migrationsrecht"):
            rows = revisions.fachkorrektur_register(ROOT, topic, required=True)
            self.assertTrue(rows)
            for name, record in rows.items():
                with self.subTest(datei=name):
                    relative = Path(name)
                    current = (ROOT / relative).read_bytes()
                    old = revisions.fachkorrektur_vorfassung(ROOT, topic, relative, record, current, None)
                    self.assertEqual(revisions.digest(old), record["vorher"])
                    self.assertEqual(revisions.historical_bytes(ROOT, ROOT / relative, record["vorher"]), old)
                    with self.assertRaises(ValueError):
                        revisions.fachkorrektur_vorfassung(ROOT, topic, relative, record, current + b"!", None)
                    with self.assertRaises(ValueError):
                        revisions.fachkorrektur_vorfassung(ROOT, topic, relative, record, old, None)


if __name__ == "__main__":
    unittest.main()
