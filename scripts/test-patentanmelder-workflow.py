#!/usr/bin/env python3
"""Prüft die publizierten Patent-Einstiege und die tatsächlichen Akten je Wissensstand."""
import json
from pathlib import Path
import tempfile
import unittest

import yaml

import main_skill_revisions as revisions
import quality_lab as lab
from skill_source_replacements import reachable_chapters
import werkstatt_visualisierung as visual


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = "patentrecht"
MAIN = "juristischer-argumentationskern"
DATA = ROOT / "scripts/data/patentanmelder"
PROOF = ROOT / revisions.PATENT_PROOF
CASES = ("01-moebel-schnappfuss", "02-gewaechshaus-beschattung", "03-fruchtkisten-pruefstand")


class PatentanmelderWorkflow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = lab.marketplace(ROOT)[PLUGIN]
        cls.profile = lab.load(ROOT / "quality/evals/patentrecht.json")
        cls.history = lab.load(PROOF / "bestand/quality/evals/patentrecht.json.txt")
        source_map = json.loads((ROOT / "quality/skill-consolidation/2026-11-14/source-map.json").read_bytes())
        cls.old_plugin = next(row for row in source_map["plugins"] if row["name"] == PLUGIN)
        cls.active = sorted((cls.directory / "skills").glob("*/SKILL.md"))

    def test_normale_skill_auswahl_und_eigenstaendiger_hauptworkflow(self):
        ids = {path.parent.name for path in self.active}
        self.assertEqual(len(ids), 10)
        self.assertEqual(ids, set(self.old_plugin["active_skills"]))
        readme = (self.directory / "README.md").read_text()
        for skill in self.active:
            with self.subTest(skill=skill.parent.name):
                front = yaml.safe_load(skill.read_text().split("---", 2)[1])
                self.assertEqual(front["name"], skill.parent.name)
                self.assertIn(f"skills/{skill.parent.name}/SKILL.md", readme)
        self.assertEqual(MAIN, visual.load_profiles()[PLUGIN]["entry_skills"][0])
        self.assertEqual(MAIN, self.profile["selection"]["target_skill"])
        main = self.directory / "skills" / MAIN / "SKILL.md"
        body = main.read_text()
        for subject in ("Patentanmelder", "Patentansprüche prüfen", "Patentanmeldung ausarbeiten"):
            self.assertIn(subject, body)
        chapter = self.directory / "references/patentanmelder-anspruchswerkstatt.md"
        self.assertIn(chapter, reachable_chapters([main], self.directory))
        for route in self.old_plugin["routes"]:
            skill = self.directory / "skills" / route["slug"] / "SKILL.md"
            reachable = reachable_chapters([skill], self.directory)
            for member in route["members"]:
                self.assertIn(self.directory / "skills" / member / "FACHINHALT.md", reachable)
        for name in ("patentrecht-werkstatt.md", "patentrecht-schnellstart.md"):
            self.assertIn(name, readme)
            prompt = (self.directory / name).read_text()
            for term in ("Anspruch", "Offenbarung", "Beschreibung", "Zusammenfassung", "Erfinder"):
                self.assertIn(term, prompt)

    def test_fruehere_pruefungen_und_aktuelle_fassungen(self):
        archive = PROOF / "bestand/quality/evals/patentrecht.json.txt"
        self.assertEqual(lab.digest(archive.read_bytes()),
                         "32573cfdc68db0504b9a574cd991301ba6ed3f0863b1d26677e56c611856a56c")
        lab.validate_profile(self.profile, PLUGIN, self.directory, ROOT)
        for review, kind in (("workshop_review", "werkstatt"), ("mini_review", "schnellstart")):
            path = self.directory / f"{PLUGIN}-{kind}.md"
            expected = self.history[review]["sha256"]
            self.assertEqual(lab.digest(revisions.historical_bytes(ROOT, path, expected, plugin=PLUGIN)), expected)
            self.assertEqual(self.profile[review]["method"], "desk_review")
            self.assertNotEqual(self.profile[review]["sha256"], expected)
        for path in self.active:
            relative = path.relative_to(ROOT).as_posix()
            previous = (PROOF / "bestand" / (relative + ".txt")).read_bytes()
            self.assertEqual(revisions.historical_bytes(ROOT, path, lab.digest(previous), plugin=PLUGIN), previous)
            self.assertNotEqual(path.read_bytes(), previous)
        for route in self.old_plugin["routes"]:
            path = self.directory / "skills" / route["slug"] / "SKILL.md"
            self.assertEqual(lab.digest(revisions.historical_bytes(ROOT, path, route["sha256"],
                                                                 plugin=PLUGIN)), route["sha256"])
        records = revisions.patent_register(ROOT)
        self.assertEqual(sum(row.get("aenderung") == "fristenspalte" for row in records.values()), 53)
        for relative, record in records.items():
            if not relative.endswith("/FACHINHALT.md"):
                continue
            path = ROOT / relative
            prior = revisions.before_patentanmelder(ROOT, path, path.read_bytes(), plugin=PLUGIN)
            self.assertEqual(lab.digest(prior), record["vorher"])
            with self.assertRaises(ValueError):
                revisions.before_patentanmelder(ROOT, path, prior, plugin=PLUGIN)
        with self.assertRaises(ValueError):
            revisions.before_patentanmelder(ROOT, self.active[0], self.active[0].read_bytes() + b"!")
        self.assertIn(self.history["cases"][0], self.profile["cases"])

    def test_grundakte_und_fortsetzung_aus_originalen(self):
        indexed = {case["id"]: case for case in self.profile["cases"]}
        modes = ("plugin", "werkstatt", "schnellstart")
        with tempfile.TemporaryDirectory() as temporary:
            for index, slug in enumerate(CASES):
                source = lab.load(DATA / f"{slug}.json")
                folder = self.directory / "Patentanmelder" / slug
                self.assertTrue((folder / "Auswertung/Erwartungshorizont.pdf").is_file())
                self.assertIn(slug, (folder.parent / "README.md").read_text())
                files = [(folder / doc["phase"] / doc["datei"]).relative_to(ROOT).as_posix()
                         for doc in source["dokumente"]]
                for stage, expected in (("grundakte", [p for p in files if "/Grundakte/" in p]),
                                        ("nachreichung", files)):
                    with self.subTest(fall=slug, stand=stage):
                        case = indexed[slug + "-" + stage]
                        self.assertEqual(case["input_files"], expected)
                        self.assertEqual(case["target_skill"], MAIN)
                        self.assertGreaterEqual(len(case["criteria"]), 3)
                        mode = modes[(index + (stage == "nachreichung")) % len(modes)]
                        run = Path(temporary) / case["id"]
                        manifest = lab.prepare(PLUGIN, case["id"], mode, run, root=ROOT)
                        self.assertEqual(manifest["status"], "prepared")
                        self.assertFalse(any((run / "output").iterdir()))
                        self.assertIs(case["decode_mime_mail"], True)
                        docs = lab.read_source_documents(run, manifest, decode_mime_mail=case["decode_mime_mail"])
                        self.assertEqual(set(docs), {Path(p).name for p in expected})
                        for name, text in docs.items():
                            self.assertTrue(text.strip(), name)
                            if name.endswith(".svg"):
                                self.assertIn("Geometrie am Original prüfen", text)
                                self.assertRegex(text, r"(?:Figur|Bezugszeichen)")
                            if name.endswith(".eml"):
                                message = next(doc for doc in source["dokumente"] if doc["datei"] == name)
                                self.assertIn("Subject: " + message["titel"], text)
                                for paragraph in message["text"]:
                                    self.assertIn(paragraph, text)
                                path = run / "input" / name
                                self.assertEqual(lab.read_artifact(path), path.read_bytes().decode("utf-8"))
                        self.assertTrue(all("Auswertung" not in p for p in expected))
                before = indexed[slug + "-grundakte"]
                after = indexed[slug + "-nachreichung"]
                self.assertLessEqual(set(before["deliverables"]), set(after["deliverables"]))
                if slug == "03-fruchtkisten-pruefstand":
                    self.assertEqual(set(after["deliverables"]) - set(before["deliverables"]), {"weitere-anmeldung.md"})
                self.assertNotEqual(before["criteria"], after["criteria"])

    def test_svg_geometrie_ohne_beschriftung_bleibt_sichtpruefung(self):
        drawing = b'<svg xmlns="http://www.w3.org/2000/svg"><path d="M0 0L10 10"/></svg>'
        with self.assertRaisesRegex(lab.LabError, "Sichtprüfung"):
            lab.read_artifact(Path("skizze.svg"), raw=drawing)


if __name__ == "__main__":
    unittest.main()
