"""Sichert konkrete Korrekturen, ersetzt keine juristische Einzelfallprüfung."""
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


class RechtsstandRegression(unittest.TestCase):
    def test_softwareanker_unterscheidet_ueberlassung_und_herstellung(self):
        text = read("references/leitentscheidungen-anker.md")
        line = next(line for line in text.splitlines() if "XII ZR 120/04" in line)
        self.assertIn("ASP-Vertrag", line)
        self.assertIn("kein Beleg", line)
        self.assertIn("nr=38367", line)

    def test_nachbesserung_verweist_auf_absatz_eins(self):
        for directory in ("eigenantrag-eigenverwaltung-270b-inso", "eigenantrag-gmbh-eigenverwaltung-270a-inso"):
            for name in ("README.md", directory + ".md"):
                with self.subTest(directory=directory, file=name):
                    text = read(f"insolvenzrecht/{directory}/{name}")
                    self.assertNotRegex(text, r"Nachbesserungsfrist[^\n.]{0,40}§ 270b Abs\. 2")
        text = read("insolvenzrecht/eigenantrag-eigenverwaltung-270b-inso/eigenantrag-eigenverwaltung-270b-inso.md")
        self.assertIn("270b Absatz 1 Satz 2", text)
        self.assertIn("270f", text)
        self.assertNotIn("§ 13 Abs. 3 InsO analog", text)
        positions = {int(n) for n in re.findall(r"Position (\d+)", text)}
        registered = {int(n) for n in re.findall(r"^\| (\d+) \|", text, re.M)}
        self.assertTrue(positions <= registered)

    def test_bankverjaehrung_nicht_mehr_als_offen_dargestellt(self):
        for name in ("README.md", "widerspruch-kontoentgelte.md"):
            text = read("bank-und-kapitalmarktrecht/widerspruch-kontoentgelte/" + name)
            self.assertIn("XI ZR 45/24", text)
            self.assertNotIn("Verjährungsbeginn wegen unzumutbarer Klageerhebung umstritten", text)
            self.assertNotIn("§ 675h Abs. 2 Satz 1 BGB", text)

    def test_urlaubsabgeltung_hat_eigenen_verjaehrungsbeginn(self):
        for name in ("README.md", "klage-urlaubsabgeltung.md"):
            text = read("arbeitsrecht/klage-urlaubsabgeltung/" + name)
            self.assertIn("9 AZR 456/20", text)
            self.assertIn("Beendigungsjahr", text)
        text = read("vorlagen-gerichtsleitend/arbeitsgericht/03-vergleichsvorschlag-gueteverfahren.md")
        self.assertNotIn("[unwiderruflich / widerruflich]", text)
        self.assertIn("9 AZR 104/24", text)

    def test_eigenbedarf_nutzt_keinen_untervermietungsanker(self):
        text = read("mietrecht-und-wohnungseigentumsrecht/ordentliche-kuendigung-wohnraum/README.md")
        self.assertIn("VIII ZR 16/26", text)
        self.assertNotIn("VIII ZR 228/23", text)

    def test_onlinewiderruf_ist_vom_kuendigungsbutton_getrennt(self):
        text = read("agb-recht/agb-saas-und-online-dienstleistungen/agb-saas-und-online-dienstleistungen.md")
        for part in ("356a", "312k", "Widerruf bestätigen", "327h", "327r"):
            self.assertIn(part, text)

    def test_raeumung_trennt_vollstreckbarkeit_und_zahlungsantraege(self):
        text = read("mietrecht-und-wohnungseigentumsrecht/raeumungsklage-wohnraum/raeumungsklage-wohnraum.md")
        self.assertIn("Paragraf 708 Nummer 7 ZPO", text)
        self.assertIn("ohne Sicherheitsleistung", text)
        self.assertIn("Paragraf 711 ZPO", text)
        self.assertIn("Alternative zu Nummer 1 bei Eigenbedarf", text)
        self.assertNotIn("ab jeweiliger Fälligkeit", text)
        self.assertNotIn("Anlagen 3, K 4", text)

    def test_vergleich_enthaelt_leistungsklauseln_statt_arbeitsanweisungen(self):
        text = read("vorlagen-gerichtsleitend/arbeitsgericht/03-vergleichsvorschlag-gueteverfahren.md")
        muster = text.split("## Mustertext mit Platzhaltern", 1)[1].split("## Hinweise zur Verwendung", 1)[0]
        self.assertNotIn("Der Vergleichstext benennt", muster)
        self.assertNotIn("Vor Protokollierung werden", muster)
        self.assertIn("Kosten des Rechtsstreits und des Vergleichs", muster)
        self.assertIn("Maßgeblich ist der Eingang bei Gericht", muster)
        self.assertIn("Paragraf 159 SGB III", text)

    def test_korrekturen_stehen_auch_in_odt(self):
        cases = {
            "arbeitsrecht/arbeitsvertrag-unbefristet": "Widerrufliche Freistellung erfüllt keinen Urlaubsanspruch",
            "arbeitsrecht/zielvereinbarung-bonus": "Interne Festlegung",
            "arbeitsrecht/klage-bonuszahlung-zielvereinbarung": "10 AZR 28/25",
            "arbeitsrecht/klage-urlaubsabgeltung": "9 AZR 456/20",
            "bank-und-kapitalmarktrecht/widerspruch-kontoentgelte": "XI ZR 45/24",
            "insolvenzrecht/eigenantrag-eigenverwaltung-270b-inso": "270b Absatz 1 Satz 2",
            "insolvenzrecht/eigenantrag-gmbh-eigenverwaltung-270a-inso": "270f",
            "agb-recht/agb-online-shop-b2c-warenverkauf": "Widerruf bestätigen",
            "agb-recht/agb-saas-und-online-dienstleistungen": "327h",
            "informationstechnologierecht/software-as-a-service-vertrag": "ausdrücklichen Vereinbarung",
            "allgemeines-und-bereichsuebergreifendes/antrag-prozesskostenhilfe": "nicht kumulative",
            "mietrecht-und-wohnungseigentumsrecht/raeumungsklage-wohnraum": "künftige Zahlungsverweigerung",
            "sportrecht/trainervertrag-profisport": "pauschaler Prämienausschluss",
        }
        for relative, expected in cases.items():
            with self.subTest(template=relative):
                directory = ROOT / relative
                with zipfile.ZipFile(directory / (directory.name + ".odt")) as archive:
                    root = ET.fromstring(archive.read("content.xml"))
                plain = " ".join("".join(root.itertext()).split())
                self.assertIn(expected.lower(), plain.lower())


if __name__ == "__main__":
    unittest.main()
