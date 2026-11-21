#!/usr/bin/env python3
"""Sichert die durchgehende, verzweigte Arbeitszeugnisprüfung."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest
from skill_limits import MAX_ACTIVE_SKILLS_PER_PLUGIN
from skill_sources import fachinhalt_path, original_skill_sources, active_owner, registry


ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "arbeitszeugnispruefer"
SPEC = next(p for p in registry() if p["name"] == PLUGIN.name)
ACTIVE_SKILLS = set(SPEC["keep"] + [r["slug"] for r in SPEC["routes"]])

# Die ursprünglichen 31 Texte behalten ihre strengen inhaltlichen Regressionen.
# Die Analyse-Bibliothek wird zusätzlich und mit eigenen Kollisionsprüfungen geprüft.
LEGACY_MODULE_SLUGS = (
    'aeussere-form-und-briefkopf',
    'ampel-einschaetzung-pro-satz',
    'aufforderungsschreiben-berichtigung',
    'auslassungen-erkennen',
    'beendigungsgrund-pruefen',
    'beweislast-bag-9-azr-584-13',
    'doppelboeden-und-verneinungen',
    'einfuehrung-pruefauftrag',
    'frequenzadverbien-pruefen',
    'fuehrungskraft-verhalten-pruefen',
    'geheimcodes-katalog',
    'intake-und-stammdaten-pruefen',
    'juristischer-argumentationskern',
    'klagestrategie-und-vollstreckung',
    'mandantenbericht-erstellen',
    'note-1-formeln-erkennen',
    'note-2-formeln-erkennen',
    'note-3-formeln-erkennen',
    'note-4-formeln-erkennen',
    'note-5-formeln-erkennen',
    'notenstufen-bag-9-azr-386-10',
    'personenreihenfolge-pruefen',
    'rollen-und-modus-wahl',
    'schaufenster-und-drift-erkennen',
    'schlussformel-notenwirkung-bewerten',
    'schlussformel-pruefen',
    'steigerungsadverbien-pruefen',
    'taetigkeitsabschnitt-wertigkeit-pruefen',
    'verhaltensabschnitt-pruefen',
    'zeugnisklarheit-objektiver-empfaengerhorizont',
    'zusammenfassungsformel-erkennen',
)
ANALYSE_MODULE_SLUGS = (
    'ampelsystem-tabellenausgabe',
    'arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste',
    'arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk',
    'arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen',
    'arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine',
    'arbeitszeugnis-gruen-behoerden-gerichts-registerweg',
    'arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung',
    'arbeitszeugnis-orange-risikoampel-gegenargumente',
    'arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation',
    'arbeitszeugnis-zeugnisanalyse-wortlaut-codes',
    'aufforderungsschreiben-arbeitgeber',
    'azubi-zeugnis-analyse',
    'bereichs-drift-detektor',
    'branchen-spezifische-formulierungen',
    'chronologie-und-belegmatrix',
    'dokumente-intake',
    'drift-quellenkarte',
    'erstgespraech-und-mandatsannahme',
    'erstpruefung-rollenklaerung-mandatsziel',
    'fristen-und-risikoampel',
    'geheimcode-katalog',
    'gesamtnoten-aggregation',
    'gruen-flaggen-katalog',
    'klage-strategie-zeugnisberichtigung',
    'leistungsbeurteilung-analyse',
    'leitende-positionen-zeugnisse',
    'mandantenbericht-zeugnisanalyse',
    'muster-arbeitszeugnis-gemischte-noten',
    'muster-arbeitszeugnis-mit-roten-flaggen',
    'muster-arbeitszeugnis-note-1',
    'negationen-und-auslassungen-erkennen',
    'negative-codeworte-katalog',
    'notenrelevante-saetze-identifizieren',
    'orange-flaggen-katalog',
    'output-waehlen',
    'rechtliche-bewertung-bag-rechtsprechung',
    'rote-flaggen-katalog',
    'satzweise-notenmatrix',
    'schlussformel-bewertung',
    'steigerungsadverbien-katalog',
    'unterlagen-luecken',
    'verbesserungsvorschlaege-formulieren',
    'verhaltensbeurteilung-analyse',
    'widerspruechliche-bewertungen',
    'zeugnis-problem-sortieren',
    'zeugnis-ueberblick-extraktion',
    'zeugnisart-erkennung',
    'zufriedenheitsformel-decodierung',
)

def legacy_skill_sources():
    return [source(slug) for slug in LEGACY_MODULE_SLUGS]

def source(slug):
    return fachinhalt_path(PLUGIN / "skills" / slug / "SKILL.md")


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
    return (NO_STATUS_HEADER in text or
            "Keine Status-, Datei-, Rollen- oder Metadatenblöcke voranstellen." in text)


class ArbeitszeugnisprueferTests(unittest.TestCase):
    def test_prompts_use_dialogue_and_finish_the_employee_bundle(self):
        for kind in ("werkstatt", "schnellstart"):
            path = PLUGIN / f"arbeitszeugnispruefer-{kind}.md"
            text = path.read_text(encoding="utf-8")
            with self.subTest(prompt=kind):
                for anchor in (
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
                self.assertRegex(text, r"Lies (?:zuerst|Zeugnis, Tätigkeitsnachweise, Vorfassungen, Beurteilungen, Zusagen, Korrespondenz und Titel zuerst)")
                self.assertRegex(text, r"nichtinteraktive[r]? Bearbeitung")
                self.assertRegex(text, r"(?i)mangelfrei")
                self.assertIn("Verhandlungswunsch", text)
                self.assertRegex(text, r"(?i)(?:Arbeitgeber- oder Personalabteilung|Isolierte Fragen und Arbeitgeberaufträge gesondert bearbeiten)")
                if "Arbeitgeberaufträge" in text:
                    self.assertIn("Für HR Korrekturvermerk und Zeugnisfassung", text)
                self.assertNotIn("skills/", text)
                self.assertNotIn("noch keinen Prüfbericht", text)
                self.assertNotIn("zwei oder drei passende Wege", text)
                self.assertNotIn("Ohne Eingabe biete", text)
                for term in FORBIDDEN_PROMPT_TERMS:
                    self.assertNotIn(term, text)
                self.assertTrue(excludes_status_preamble(text))
                self.assertNotRegex(text, r"(?i)höchstens (?:zwei|drei) (?:punkte|fragen)")
                self.assertTrue(all(re.match(r"##+ \d+(?:\.\d+)*\.? ", line) for line in text.splitlines() if line.startswith("##")))
                if kind == "schnellstart":
                    self.assertLessEqual(len(text.encode("utf-8")), 7500)
                    self.assertLessEqual(len(text), 7500)

    def test_status_preamble_guard_rejects_partial_or_reversed_bans(self):
        # Auch die knappe Fassung verbietet sämtliche vorgeschalteten Statusblöcke.
        self.assertTrue(excludes_status_preamble("Keine Status-, Datei-, Rollen- oder Metadatenblöcke voranstellen."))
        for weakened in (
            "Keine Datei- oder Metadatenblöcke voranstellen.",
            "Status-, Datei-, Rollen- oder Metadatenblöcke voranstellen.",
            "Keine Statusblöcke im Mandantenschreiben; zuerst den Rollenblock ausgeben.",
        ):
            self.assertFalse(excludes_status_preamble(weakened))

    def test_portable_prompts_cover_answer_states_and_followup(self):
        # This is an editorial regression guard, not a model-performance test.
        for kind in ("werkstatt", "schnellstart"):
            text = (PLUGIN / f"arbeitszeugnispruefer-{kind}.md").read_text(encoding="utf-8")
            with self.subTest(prompt=kind):
                self.assertRegex(text, r"(?:Promptdatei|Einfügen oder Hochladen dieser Datei|Ohne Startformel beginnen; ausdrückliche Promptbesprechung bleibt eine solche)")
                for anchor in ("Startformel", "Prüfziel", "Teilantwort", "Suchschleife", "Arbeitgeberantwort", "Vorfassung", "Folgeschreiben"):
                    self.assertIn(anchor, text)
                self.assertRegex(text, r"(?i)(?:unlesbar|OCR)")
                self.assertRegex(text, r"(?i)widerspr[üu]")
                self.assertRegex(text, r"(?i)(?:nicht live geprüft|keine.*live verifizierten)")
                self.assertNotIn("höchstens eine Rückfrage", text)
                self.assertNotIn("nur einmal gebündelt", text)

    def test_gateway_and_recipient_skills_define_the_same_completion(self):
        entry = source("einfuehrung-pruefauftrag").read_text(encoding="utf-8")
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

        roles = source("rollen-und-modus-wahl").read_text(encoding="utf-8")
        self.assertIn("Die Rollenwahl ist nie das Endergebnis", roles)
        self.assertIn("weder als Statuskopf noch als Rollen- oder Metadatenblock", roles)
        self.assertIn("interaktiver Standard", roles)
        self.assertRegex(roles, r"(?:ohne|keinen) weiteren Entwurfsauftrag")
        self.assertIn("kein künstliches Forderungsschreiben", roles)
        self.assertNotIn("roten oder orangefarbenen Befund", roles)

        report = source("mandantenbericht-erstellen").read_text(encoding="utf-8")
        self.assertIn("120 bis 180 Wörter", report)
        self.assertIn("ohne Fülltext", report)
        self.assertIn("einfache, direkte Sie-Sprache", report)
        self.assertIn("Keine Urteilsparade", report)
        self.assertIn("ohne erneuten Entwurfsauftrag", report)

        opposing = source("aufforderungsschreiben-berichtigung").read_text(encoding="utf-8")
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

        intake = source("intake-und-stammdaten-pruefen").read_text(encoding="utf-8")
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
            "8 AZB 25/25",
        ):
            self.assertIn(citation, workshop)
        self.assertIn("Altvolltext ist im heutigen BAG-Onlinearchiv", workshop)
        self.assertIn("kein allgemeines Tabellen- oder Listenverbot", workshop)
        self.assertIn("die bloße zeitliche Abfolge genügt nicht", workshop)
        self.assertIn("Verwechsle die materielle Zeugnisbewertung nicht", workshop)
        self.assertIn("Wahrheit und Klarheit bleiben Grenzen", workshop)
        self.assertIn("Eine angekündigte Korrektur ist noch keine", source("einfuehrung-pruefauftrag").read_text(encoding="utf-8"))

    def test_grade_correction_does_not_reverse_burden_of_proof(self):
        # Guard the note-4/5-to-3 branch independently of above-average targets.
        paths = [PLUGIN / f"arbeitszeugnispruefer-{kind}.md" for kind in ("werkstatt", "schnellstart")]
        paths += [source(slug) for slug in (
            "einfuehrung-pruefauftrag", "beweislast-bag-9-azr-584-13",
            "aufforderungsschreiben-berichtigung", "mandantenbericht-erstellen",
            "klagestrategie-und-vollstreckung",
        )]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertRegex(text, r"(?i)(?:ausgangs- und zielnote|ausgangsnote 4 oder 5 und zielnote 3)")
                self.assertIn("Arbeitgeber", text)
                self.assertIn("Beweislast", text)
                self.assertRegex(text, r"(?i)fehlende.*(?:Mehrleistungsbelege|Belege für Mehrleistung).*nicht.*(?:bloße[nr]? Bitte)")
                self.assertNotIn("Ein Streit über eine bessere Gesamtbewertung verlangt", text)

    def test_every_original_module_has_specific_routing_and_a_continuation_rule(self):
        paths = legacy_skill_sources()
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

    def test_active_routes_cover_every_preserved_specialist(self):
        active = {p.parent.name for p in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(active, ACTIVE_SKILLS)
        self.assertLessEqual(len(active), MAX_ACTIVE_SKILLS_PER_PLUGIN)
        originals = original_skill_sources(PLUGIN)
        self.assertEqual(len(originals), 81)
        for path in originals:
            with self.subTest(module=path.parent.name):
                owner = active_owner(PLUGIN, path.parent.name)
                self.assertIn(owner, active)
                if path.name == "FACHINHALT.md":
                    route = PLUGIN / "skills" / owner / "SKILL.md"
                    self.assertIn(f"../{path.parent.name}/FACHINHALT.md", route.read_text())
                    self.assertFalse(path.with_name("SKILL.md").exists())

    def test_merged_library_preserves_both_specialist_collections(self):
        self.assertEqual(31, len(LEGACY_MODULE_SLUGS))
        self.assertEqual(48, len(ANALYSE_MODULE_SLUGS))
        self.assertFalse(set(LEGACY_MODULE_SLUGS) & set(ANALYSE_MODULE_SLUGS))
        actual = {p.parent.name for p in (PLUGIN / "skills").glob("*/FACHINHALT.md")}
        self.assertEqual((set(LEGACY_MODULE_SLUGS) - {"juristischer-argumentationskern"}) | set(ANALYSE_MODULE_SLUGS), actual)
        self.assertEqual(78, len(actual))
        for slug in ANALYSE_MODULE_SLUGS:
            with self.subTest(module=slug):
                original = ROOT / "arbeitszeugnis-analyse" / "skills" / slug / "FACHINHALT.md"
                self.assertTrue(original.is_file(), "The original source must remain available")
                text = source(slug).read_text(encoding="utf-8")
                self.assertIn("arbeitszeugnis-auslegung-und-arbeitsmodi.md", text)
                owner = active_owner(PLUGIN, slug)
                route = PLUGIN / "skills" / owner / "SKILL.md"
                self.assertIn(f"../{slug}/FACHINHALT.md", route.read_text())

    def test_merged_entry_points_finish_the_correct_assignment(self):
        for slug in ("einstieg-routing", "kaltstart-triage"):
            text = (PLUGIN / "skills" / slug / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill=slug):
                self.assertIn("Analyse", text)
                self.assertIn("Arbeitgeberschreiben", text)
                self.assertIn("Arbeitsbuch", text)
                self.assertRegex(text, r"(?i)(?:keine starre Höchstzahl|Anzahl der Fragerunden folgt dem Fall)")
                self.assertNotRegex(text, r"(?i)(?:höchstens|hoechstens) (?:eine|zwei) (?:Rückfrage|Rueckfrage|Fragen)")
                self.assertIn("ohne", text)
                self.assertRegex(text, r"(?:Status-, Datei-, Rollen-|Status-, Datei-, Rollen- oder Metadaten)")
                self.assertIn("Times New Roman 11", text)
        workshop = (PLUGIN / "arbeitszeugnispruefer-werkstatt.md").read_text(encoding="utf-8")
        self.assertIn("Begrenzte Analyse und Vergleich zweier Fassungen", workshop)
        self.assertIn("nicht ungefragt angehängt", workshop)

    def test_unsafe_note_arithmetic_regression_rejects_legacy_examples(self):
        unsafe = re.compile(r"Gewichteter Wert|Gewichtete Gesamtnote|minus (?:eine )?halbe Stufe|Codewort, unabhaengig vom restlichen Satz|Codewort für Trinkproblem")
        for slug in ("gesamtnoten-aggregation", "satzweise-notenmatrix", "ampelsystem-tabellenausgabe", "negative-codeworte-katalog", "muster-arbeitszeugnis-gemischte-noten"):
            original = (ROOT / "arbeitszeugnis-analyse" / "skills" / slug / "FACHINHALT.md").read_text(encoding="utf-8")
            corrected = source(slug).read_text(encoding="utf-8")
            with self.subTest(module=slug):
                self.assertRegex(original, unsafe, "The regression must actually detect the previous erroneous rule")
                self.assertNotRegex(corrected, unsafe)

    def test_specialists_do_not_turn_style_conventions_into_certain_claims(self):
        all_skills = "\n".join(path.read_text(encoding="utf-8") for path in legacy_skill_sources())
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

        conclusion = source("schlussformel-pruefen").read_text(encoding="utf-8")
        self.assertIn("Zeugnisnote", conclusion)
        self.assertRegex(conclusion, r"(?i)(kein|nicht).*Anspruch")
        order = source("personenreihenfolge-pruefen").read_text(encoding="utf-8")
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

    def test_2026_enforcement_distinguishes_title_from_material_dispute(self):
        for path in (
            source("klagestrategie-und-vollstreckung"),
            PLUGIN / "arbeitszeugnispruefer-werkstatt.md",
            PLUGIN / "arbeitszeugnispruefer-schnellstart.md",
        ):
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertIn("8 AZB 25/25", text)
                self.assertIn("Entwurfsrecht", text)
                self.assertIn("wichtigem Grund", text)
                self.assertRegex(text, r"Erkenntnis(?:verfahren|prozess)")
                self.assertIn("https://www.bundesarbeitsgericht.de/entscheidung/8-azb-25-25/", text)
        procedure = source("klagestrategie-und-vollstreckung").read_text(encoding="utf-8")
        self.assertIn("teilweise", procedure)
        self.assertIn("offen", procedure)
        self.assertIn("724 und 750 ZPO", procedure)

    def test_recent_decisions_reach_independent_prompts_and_specialists(self):
        book = (PLUGIN / "references/arbeitszeugnis-handbuch.md").read_text()
        workshop = (PLUGIN / "arbeitszeugnispruefer-werkstatt.md").read_text()
        quickstart = (PLUGIN / "arbeitszeugnispruefer-schnellstart.md").read_text()
        # Die Werkstatt ist eine eigenständige Datei. Prüfe die vollständigen neuen
        # Dossiers einschließlich Reichweitengrenzen, nicht bloß ein Aktenzeichen.
        cases = (
            ("22.2.11", "3 Ca 7407/25", "schlussformel-pruefen", "NJRE001639396"),
            ("23.8.7", "10 Ta 207/26", "klagestrategie-und-vollstreckung", "LARE260001319"),
        )
        for section, citation, specialist, document_id in cases:
            with self.subTest(case=citation):
                start = book.index(f"#### {section}.")
                stop = book.index("\n### ", start)
                dossier = book[start:stop]
                self.assertIn(citation, dossier)
                self.assertIn(document_id, dossier)
                self.assertIn(dossier, workshop)
                self.assertIn(citation, quickstart)
                self.assertIn(document_id, source(specialist).read_text())

    def test_apprenticeship_sources_agree_on_entitlement(self):
        for slug in ("zeugnisart-erkennung", "azubi-zeugnis-analyse"):
            text = source(slug).read_text()
            with self.subTest(module=slug):
                self.assertIn("Fertigkeiten, Kenntnisse und Fähigkeiten", text)
                self.assertIn("Leistung und Verhalten", text)
                self.assertRegex(text, r"auf Verlangen|verlangt")
                self.assertIn("https://www.gesetze-im-internet.de/bbig_2005/__16.html", text)
                self.assertNotIn("Mögliche Schulprobleme", text)
                self.assertNotIn("fehlendes Verhalten = Rot", text)

    def test_2025_waiver_is_time_limited_and_not_universal_choice_of_law(self):
        for path in (
            source("intake-und-stammdaten-pruefen"),
            PLUGIN / "arbeitszeugnispruefer-werkstatt.md",
        ):
            text = path.read_text(encoding="utf-8")
            self.assertIn("2 AZR 96/24 (B)", text)
            self.assertIn("vor Beendigung", text)
            self.assertIn("EGBGB", text)
            self.assertRegex(text, r"(?i)(?:spätere|zeitlich unbegrenzten)")

    def test_specialists_start_from_their_actual_legal_question(self):
        expectations = {
            "auslassungen-erkennen": ("Branchenübung", "9 AZR 262/20", "Außendienstteams"),
            "frequenzadverbien-pruefen": ("Fehlerfreiheit", "9 AZR 584/13", "Gesamtleistung"),
            "fuehrungskraft-verhalten-pruefen": ("Paragraf 630 BGB", "Projektkoordination", "9 AZR 262/20"),
            "notenstufen-bag-9-azr-386-10": ("historischen Skillnamen", "9 AZR 584/13", "Klarheitsanker"),
            "personenreihenfolge-pruefen": ("kein Spezialurteil", "9 AZR 386/10", "Paragraf 109"),
            "schlussformel-pruefen": ("wesentliches Motiv", "9 AZR 272/22", "nicht abschließend"),
        }
        for slug, anchors in expectations.items():
            text = source(slug).read_text(encoding="utf-8")
            with self.subTest(skill=slug):
                for anchor in anchors:
                    self.assertIn(anchor, text)
        gateway = source("einfuehrung-pruefauftrag").read_text(encoding="utf-8")
        self.assertIn("Keine fünf parallelen Notenprüfungen", gateway)
        for path in legacy_skill_sources():
            self.assertNotIn("§", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
