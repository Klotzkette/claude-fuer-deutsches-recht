#!/usr/bin/env python3
"""Regressionen der PR-Prüfung 650–652; ersetzt keine juristische Vollprüfung.

Sichert besonders folgenschwere Verfahrenshinweise mit positiven Ankern und
Gegenbeispielen aus dem früheren Stand. Historische Grenzen und technische
Skill-Slugs bleiben ausdrücklich zulässig.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "mahn": "forderungsmanagement-klagewerkstatt/skills/mahnbescheid-online/SKILL.md",
    "vollstreckung": "urteilsbauer-relationsmacher/skills/vorlaeufige-vollstreckbarkeit/SKILL.md",
    "berufung": "urteilsbauer-relationsmacher/skills/rechtsmittelbelehrung-zivil-relation/SKILL.md",
    "marken": "fachanwalt-strafrecht/skills/strafrecht-spezial-markenrecht-143-markeng/SKILL.md",
    "qualifikation": "fachanwalt-strafrecht/skills/strafrecht-spezial-markenrecht-143a-markeng-bandenmaessig/SKILL.md",
    "erbschein": "docs/experimentell/vorlagensammlung-recht/erbrecht/beschwerde-nachlassgericht-erbschein/beschwerde-nachlassgericht-erbschein.md",
    "medizin": "fachanwalt-medizinrecht/skills/behandlungsvertrag-630a/SKILL.md",
}
# (Kennung, erforderliches Muster). Die Regeln verlangen Informationen, keine
# exakte Formulierung; zusätzliche Beispiele und Visualisierungen bleiben frei.
REQUIRED = {
    "mahn": [
        ("Hessen-Huenfeld", r"Hessen\s*\|\s*AG Hünfeld"),
        ("Bremen-Bremen", r"\| Bremen\s*\|\s*AG Bremen"),
        ("NRW-geteilte-Zustaendigkeit", r"Düsseldorf und Hamm[^\n]*Hagen"),
        ("Antragsteller-ohne-Inland", r"Fehlt dem Antragsteller[^\n]*Wedding"),
    ],
    "vollstreckung": [
        ("Hauptsachegrenze", r"Hauptsacheverurteilung[^\n]*1[.]?250 EUR"),
        ("Kostengrenze", r"Kostenentscheidung[^\n]*1[.]?500 EUR"),
        ("713-keine-Grundlage", r"§ 713 ersetzt weder § 708 noch § 709"),
        ("711-von-Amts-wegen", r"§ 711[^\n]*von Amts wegen"),
        ("Verhandlung-Uebergang", r"mündliche Verhandlung[^\n]*geschlossen"),
        ("Schriftverfahren-Uebergang", r"Einreichungsschluss"),
    ],
    "berufung": [
        ("Uebergangsnorm", r"§ 47 EGZPO"),
        ("Verhandlung-Uebergang", r"geschlossener mündlicher Verhandlung"),
        ("Schriftverfahren-Uebergang", r"Einreichungsschluss"),
        ("Form", r"anwaltliche[nr]? Berufungsschrift"),
        ("Fristbeginn-spaetestens", r"fünf Monaten"),
    ],
    "marken": [
        ("Antragsnorm", r"§ 143 Abs[.] 4"),
        ("Unionsmarken-Verweisung", r"§ 144 Abs[.] 2"),
        ("Privatklagenorm", r"§ 374 Abs[.] 1 Nr[.] 8"),
        ("Vergehen", r"Qualifikation[^\n]*Vergehen"),
    ],
    "qualifikation": [("Vergehen", r"Vergehen"), ("Qualifikationsnorm", r"§ 143 Abs[.] 2")],
    "erbschein": [("FamFG-Uebergang", r"493 Abs[.] 6 FamFG"), ("Aktuelle-Grenze", r"1[.]?000 EUR")],
    "medizin": [("LG-Sonderzustaendigkeit", r"71 Abs[.] 2 Nr[.] 9 GVG"), ("GVG-Uebergang", r"44 EGGVG")],
}
FORBIDDEN = {
    "mahn": [("Hessen-falsches-Gericht", r"Hessen\s*\|\s*AG (?:Frankfurt|Kassel)")],
    "vollstreckung": [("1500-als-Hauptsachegrenze", r"Hauptsacheverurteilung darf deren Gegenstand 1[.]?500 EUR")],
    "berufung": [("Berufung-zu-Protokoll", r"schriftlich oder zu Protokoll der\s+Geschäftsstelle einzulegen"),
                  ("Begruendung-ein-Monat", r"binnen einer weiteren Frist von einem Monat[^.]*zu begründen")],
    "marken": [("144-keine-Antragsnorm", r"(?:Paragraph|§) 144 Abs[.]? 1 MarkenG:\s*Antragsdelikt")],
    "qualifikation": [("Qualifikation-kein-Verbrechen", r"(?:ist|handelt es sich um) ein Verbrechen")],
}


def validate_text(group: str, text: str) -> list[str]:
    errors = [label for label, pattern in REQUIRED[group] if not re.search(pattern, text)]
    errors.extend(label for label, pattern in FORBIDDEN.get(group, []) if re.search(pattern, text))
    return errors


class ReviewedLawCorrections(unittest.TestCase):
    def test_current_working_documents(self):
        for group, relative in FILES.items():
            with self.subTest(file=relative):
                self.assertEqual([], validate_text(group, (ROOT / relative).read_text()))

    def test_old_mahn_assignment_is_rejected(self):
        text = (ROOT / FILES["mahn"]).read_text().replace("| Hessen | AG Hünfeld |", "| Hessen | AG Frankfurt |")
        self.assertIn("Hessen-falsches-Gericht", validate_text("mahn", text))

    def test_cost_limit_cannot_replace_main_claim_limit(self):
        text = (ROOT / FILES["vollstreckung"]).read_text().replace("deren Gegenstand 1.250 EUR", "deren Gegenstand 1.500 EUR")
        self.assertIn("1500-als-Hauptsachegrenze", validate_text("vollstreckung", text))

    def test_decision_date_alone_is_not_enough(self):
        text = (ROOT / FILES["vollstreckung"]).read_text()
        text = "\n".join(line for line in text.splitlines() if "Nach § 47 EGZPO" not in line)
        self.assertIn("Verhandlung-Uebergang", validate_text("vollstreckung", text))

    def test_old_appeal_form_is_rejected(self):
        text = (ROOT / FILES["berufung"]).read_text() + "\nschriftlich oder zu Protokoll der\nGeschäftsstelle einzulegen"
        self.assertIn("Berufung-zu-Protokoll", validate_text("berufung", text))

    def test_old_request_norm_is_rejected(self):
        text = (ROOT / FILES["marken"]).read_text() + "\nParagraph 144 Abs 1 MarkenG: Antragsdelikt."
        self.assertIn("144-keine-Antragsnorm", validate_text("marken", text))

    def test_historical_600_euros_and_technical_slug_are_allowed(self):
        self.assertEqual([], validate_text("vollstreckung", (ROOT / FILES["vollstreckung"]).read_text()))
        self.assertEqual([], validate_text("qualifikation", (ROOT / FILES["qualifikation"]).read_text()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
