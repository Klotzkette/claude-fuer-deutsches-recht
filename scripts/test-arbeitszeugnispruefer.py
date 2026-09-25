#!/usr/bin/env python3
"""Sichert die durchgehende, verzweigte Arbeitszeugnisprüfung."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "arbeitszeugnispruefer"


def load_script(filename: str):
    spec = importlib.util.spec_from_file_location(filename, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


README_GENERATOR = load_script("inject-direkt-loslegen-section.py")
FORBIDDEN_PROMPT_TERMS = (
    "Aktenkern",
    "Ampel-Bilanz",
    "Fallkarte",
    "Fachvotum",
    "Gate",
    "Lieferstück",
    "Output",
    "Sofortbild",
    "Stop-Kriterien",
    "Werkstattfluss",
)
NO_STATUS_HEADER = (
    "weder einen Statuskopf noch einen Datei-, Metadaten-, Rollen-, Aktenstands- oder "
    "Bearbeitungsblock"
)


def excludes_status_preamble(text):
    """Verlangt das vollständige Verbot des vorgeschalteten Arbeitsstands."""
    return NO_STATUS_HEADER in text


class ArbeitszeugnisprueferTests(unittest.TestCase):
    def test_prompts_use_dialogue_and_finish_the_employee_bundle(self):
        for kind in ("werkstatt", "schnellstart"):
            path = PLUGIN / f"arbeitszeugnispruefer-{kind}.md"
            text = path.read_text(encoding="utf-8")
            with self.subTest(prompt=kind):
                for anchor in (
                    "Lies zuerst",
                    "interaktiv",
                    "warte auf die",
                    "Zahl der Fragerunden",
                    "Platzhalter",
                    "ohne neuen Auftrag",
                    "Mandantenschreiben",
                    "Arbeitgeberschreiben",
                    "120 bis 180 Wörter",
                    "ohne Fülltext",
                ):
                    self.assertIn(anchor, text)
                self.assertRegex(text, r"nichtinteraktive[r]? Bearbeitung")
                self.assertRegex(text, r"(?i)(?:mangelfrei|keine Änderung).*(?:kein|entfällt|ohne).*?(?:Forderungs|Arbeitgeber|extern)")
                self.assertRegex(text, r"(?i)Arbeitgeber- oder Personalabteilung")
                self.assertNotIn("skills/", text)
                self.assertNotIn("noch keinen Prüfbericht", text)
                self.assertNotIn("zwei oder drei passende Wege", text)
                self.assertNotIn("Ohne Eingabe biete", text)
                for term in FORBIDDEN_PROMPT_TERMS:
                    self.assertNotIn(term, text)
                self.assertTrue(excludes_status_preamble(text))
                self.assertNotRegex(text, r"(?i)höchstens (?:zwei|drei) (?:punkte|fragen)")
                self.assertTrue(all(re.match(r"##+ \d+(?:\.\d+)*\. ", line) for line in text.splitlines() if line.startswith("##")))
                if kind == "schnellstart":
                    self.assertLess(len(text.encode("utf-8")), 7500)

    def test_gateway_and_recipient_skills_define_the_same_completion(self):
        entry = (PLUGIN / "skills/einfuehrung-pruefauftrag/SKILL.md").read_text(encoding="utf-8")
        for anchor in (
            "Lies zuerst",
            "arbeitszeugnisgenerator",
            "Eine Rückfrage ist ein Zwischenschritt",
            "Nach der Antwort",
            "interaktive Standard",
            "warte auf die tatsächliche Antwort",
            "ausdrücklich nichtinteraktiver Bearbeitung",
            "120 bis 180 Wörter",
            "Arbeitgeberschreiben",
            "ohne weiteren Auftrag",
            "mangelfrei",
            NO_STATUS_HEADER,
        ):
            self.assertIn(anchor, entry)

        roles = (PLUGIN / "skills/rollen-und-modus-wahl/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Die Rollenwahl ist nie das Endergebnis", roles)
        self.assertIn("weder als Statuskopf noch als Rollen- oder Metadatenblock", roles)
        self.assertIn("interaktiver Standard", roles)
        self.assertRegex(roles, r"(?:ohne|keinen) weiteren Entwurfsauftrag")
        self.assertIn("kein künstliches Forderungsschreiben", roles)
        self.assertNotIn("roten oder orangefarbenen Befund", roles)

        report = (PLUGIN / "skills/mandantenbericht-erstellen/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("120 bis 180 Wörter", report)
        self.assertIn("ohne Fülltext", report)
        self.assertIn("einfache, direkte Sie-Sprache", report)
        self.assertIn("Keine Urteilsparade", report)
        self.assertIn("ohne erneuten Entwurfsauftrag", report)

        opposing = (PLUGIN / "skills/aufforderungsschreiben-berichtigung/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("ohne erneuten Entwurfsauftrag", opposing)
        self.assertIn("kein Arbeitgeberschreiben", opposing)
        self.assertIn("objektiven Fehler", opposing)
        self.assertIn("beweisabhängigen Aufwertung", opposing)
        self.assertIn("Verhandlungsziel", opposing)
        self.assertIn("erfinde keine Nutzerantwort", opposing)

        megaprompt = (ROOT / "testakten/megaprompts/arbeitszeugnispruefer.md").read_text(encoding="utf-8")
        self.assertIn("Skill: `einfuehrung-pruefauftrag`", megaprompt)
        self.assertIn(NO_STATUS_HEADER, megaprompt)
        self.assertLess(
            megaprompt.index("Skill: `einfuehrung-pruefauftrag`"),
            megaprompt.index("Skill: `juristischer-argumentationskern`"),
        )

        readme = (PLUGIN / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("fachbezogenen Erststand mit Ergebnisrichtung", readme)
        self.assertNotIn("Frage nur einmal gebündelt", readme)
        self.assertNotIn("Erfasse zuerst Dateinamen und Metadaten", readme)
        self.assertNotIn("Lies Dateinamen, Metadaten", readme)
        self.assertIn(NO_STATUS_HEADER, readme)
        self.assertIn("Ein in den Chat kopierter Prompt wird interaktiv bearbeitet", readme)
        self.assertIn("Fehlt eine entscheidungserhebliche Tatsache, beginne mit der Rückfrage", readme)
        self.assertIn("warte auf die tatsächliche Antwort", readme)
        self.assertIn("ohne neuen Auftrag", readme)
        self.assertIn("kein künstliches Arbeitgeberschreiben", readme)

        generated_start = README_GENERATOR.quickstart_section("arbeitszeugnispruefer", PLUGIN)
        self.assertIn(NO_STATUS_HEADER, generated_start)
        self.assertIn("kurzem Mandantenschreiben", generated_start)
        self.assertIn("abgestuftem Arbeitgeberschreiben", generated_start)
        self.assertIn("Ein in den Chat kopierter Prompt wird interaktiv bearbeitet", generated_start)
        self.assertIn("Fehlt eine entscheidungserhebliche Tatsache, beginne mit der Rückfrage", generated_start)
        self.assertIn("warte auf die tatsächliche Antwort", generated_start)
        self.assertIn("ausdrücklich nichtinteraktiver Bearbeitung", generated_start)
        self.assertNotIn("Erfasse zuerst Dateinamen und Metadaten", generated_start)
        self.assertNotIn("Lies Dateinamen, Metadaten", generated_start)
        generic_start = README_GENERATOR.quickstart_section("beispiel-plugin", PLUGIN)
        self.assertIn("ohne seine Inhalte ungefragt aufzulisten", generic_start)
        self.assertNotIn("Frage nur einmal gebündelt", generic_start)
        self.assertIn("Verarbeite die Antwort im bestehenden Entwurf", generic_start)

        intake = (PLUGIN / "skills/intake-und-stammdaten-pruefen/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Die Aufnahme bleibt intern", intake)
        self.assertIn(
            "einen Statuskopf oder einen Datei-, Metadaten-, Rollen-, Aktenstands- oder Bearbeitungsblock",
            intake,
        )
        self.assertIn("nicht als eigenes Zwischenprodukt ausgegeben", intake)

    def test_workshop_embeds_case_law_with_limits(self):
        workshop = (PLUGIN / "arbeitszeugnispruefer-werkstatt.md").read_text(encoding="utf-8")
        self.assertIn("Sind alle entscheidenden Angaben vorhanden, schließe den Auftrag unmittelbar ab", workshop)
        self.assertNotIn("Rn. 14, 18 und 28", workshop)
        for citation in (
            "9 AZR 248/07",
            "9 AZR 584/13",
            "9 AZR 386/10",
            "9 AZR 262/20",
            "9 AZR 227/11",
            "9 AZR 146/21",
            "9 AZR 272/22",
            "9 AZB 49/16",
        ):
            self.assertIn(citation, workshop)
        self.assertIn("Altvolltext ist im heutigen BAG-Onlinearchiv", workshop)
        self.assertIn("kein allgemeines Tabellen- oder Listenverbot", workshop)
        self.assertIn("die bloße zeitliche Abfolge genügt nicht", workshop)
        self.assertIn("Verwechsle die materielle Zeugnisbewertung nicht", workshop)

    def test_every_skill_has_specific_routing_and_a_continuation_rule(self):
        paths = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(paths), 31)
        descriptions = []
        for path in paths:
            text = path.read_text(encoding="utf-8")
            match = re.search(r'^description: "([^"]+)"$', text, re.M)
            self.assertIsNotNone(match, path)
            descriptions.append(match.group(1))
            with self.subTest(skill=path.parent.name):
                self.assertNotIn("§", match.group(1))
                self.assertNotIn("Prüfprodukt mit Risiko und nächstem Schritt", text)
                self.assertRegex(text, r"(?i)(nach der antwort|laufenden bearbeitung|größeren auftrag|bestellte[nmrs]? (?:bericht|dokument|entwurf|ergebnis)|vollständige[nmrs]? (?:bericht|dokument|entwurf|ergebnis|fassung))")
        self.assertEqual(len(descriptions), len(set(descriptions)))

    def test_specialists_do_not_turn_style_conventions_into_certain_claims(self):
        all_skills = "\n".join(path.read_text(encoding="utf-8") for path in (PLUGIN / "skills").glob("*/SKILL.md"))
        for assertion in (
            "Eine falsche Reihenfolge ist ein eigener Berichtigungspunkt",
            "Alle fünf Bausteine",
            "vier von fünf Schlussbausteinen",
            "Fehlt der Maximalsteigerer",
            "ist ein roter Auslassungsbefund",
            "Streitwert beträgt in der Regel ein Bruttomonatsgehalt",
            "Aufforderungsschreiben wird nur bei",
        ):
            self.assertNotIn(assertion, all_skills)

        conclusion = (PLUGIN / "skills/schlussformel-pruefen/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Zeugnisnote", conclusion)
        self.assertRegex(conclusion, r"(?i)(kein|nicht).*Anspruch")
        order = (PLUGIN / "skills/personenreihenfolge-pruefen/SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(order, r"(?i)(nicht.*für sich|allein weder)")

    def test_review_hashes_match_both_prompts(self):
        profile = json.loads((ROOT / "quality/evals/arbeitszeugnispruefer.json").read_text(encoding="utf-8"))
        quickstart = (PLUGIN / "arbeitszeugnispruefer-schnellstart.md").read_bytes()
        workshop = (PLUGIN / "arbeitszeugnispruefer-werkstatt.md").read_bytes()
        self.assertEqual(profile["mini_review"]["sha256"], hashlib.sha256(quickstart).hexdigest())
        self.assertEqual(profile["workshop_review"]["sha256"], hashlib.sha256(workshop).hexdigest())
        criteria = "\n".join(
            criterion["text"]
            for case in profile["cases"]
            for criterion in case["criteria"]
        )
        self.assertIn("Keine Ausgabe beginnt mit einem Status-, Rollen-, Datei- oder Metadatenblock", criteria)


if __name__ == "__main__":
    unittest.main()
