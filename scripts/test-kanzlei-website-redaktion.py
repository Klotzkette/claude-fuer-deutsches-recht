#!/usr/bin/env python3
"""Regressionstests der formalen Redaktionsfreigabe und Paketgrenzen."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "kanzlei-website-redaktion"
spec = importlib.util.spec_from_file_location("redaktion", PLUGIN / "scripts/freigabe_pruefen.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
build_spec = importlib.util.spec_from_file_location("website_build", ROOT / "scripts/build-kanzlei-website-release.py")
builder = importlib.util.module_from_spec(build_spec)
build_spec.loader.exec_module(builder)


def complete():
    data = json.loads((PLUGIN / "assets/freigabe-beispiel.json").read_text())
    data["publication"]["base_revision"] = "revision-17"
    digest = module.fassungs_hash(data["publication"], data["transparency"])
    data["checks"] = dict.fromkeys(data["checks"], True)
    data["human_review"] = {"reviewer": "Prüfer", "at": "2026-10-08T12:00:00+02:00", "scope": "Aussagen mit Quellen abgeglichen", "editorial_responsible": "Redaktion", "content_hash": digest}
    data["release"].update(approved=True, by="Verantwortlicher", at="2026-10-08T12:10:00+02:00", content_hash=digest)
    return data


class ApprovalTests(unittest.TestCase):
    def test_example_never_approves_itself(self):
        data = json.loads((PLUGIN / "assets/freigabe-beispiel.json").read_text())
        self.assertFalse(module.pruefen(data)["formal_vollstaendig"])

    def test_complete_review_is_formally_complete(self):
        self.assertTrue(module.pruefen(complete())["formal_vollstaendig"])

    def test_each_publication_change_invalidates_release(self):
        for key, value in (("body", "Anderer Inhalt"), ("target_url", "https://andere.example/beitrag"), ("base_revision", "revision-18"), ("text_disclosure", "Neuer Hinweis"), ("media", [{"file": "foto.jpg", "sha256": "a"*64}])):
            data = complete()
            data["publication"][key] = value
            with self.subTest(key=key):
                self.assertFalse(module.pruefen(data)["formal_vollstaendig"])

    def test_new_release_does_not_revalidate_old_review(self):
        data = complete()
        data["publication"]["body"] = "Neuer Rechtsbeitrag"
        data["release"]["content_hash"] = module.fassungs_hash(data["publication"], data["transparency"])
        self.assertFalse(module.pruefen(data)["formal_vollstaendig"])

    def test_editorial_name_without_review_is_insufficient(self):
        data = complete()
        data["human_review"].pop("scope")
        self.assertFalse(module.pruefen(data)["formal_vollstaendig"])

    def test_unreviewed_requires_disclosure_and_explicit_exception(self):
        data = complete()
        data["human_review"] = {}
        data["publication"]["text_disclosure"] = "Mit künstlicher Intelligenz erstellt; nicht inhaltlich geprüft."
        data["release"]["content_hash"] = module.fassungs_hash(data["publication"], data["transparency"])
        self.assertFalse(module.pruefen(data)["formal_vollstaendig"])
        data["release"]["allow_unreviewed_publication"] = True
        self.assertTrue(module.pruefen(data)["formal_vollstaendig"])

    def test_contact_update_does_not_force_text_label(self):
        data = complete()
        data["transparency"].update(public_interest=False, reason="Nur bestätigte Telefonnummer geändert")
        data["human_review"] = {}
        data["release"]["content_hash"] = module.fassungs_hash(data["publication"], data["transparency"])
        self.assertTrue(module.pruefen(data)["formal_vollstaendig"])

    def test_changed_transparency_invalidates_approval(self):
        data = complete()
        data["transparency"]["public_interest"] = False
        self.assertFalse(module.pruefen(data)["formal_vollstaendig"])

    def test_deepfake_not_exempt_by_text_review(self):
        data = complete()
        data["transparency"]["deepfake"] = True
        digest = module.fassungs_hash(data["publication"], data["transparency"])
        data["human_review"]["content_hash"] = digest
        data["release"]["content_hash"] = digest
        result = module.pruefen(data)
        self.assertFalse(result["formal_vollstaendig"])
        self.assertEqual(result["fehler"], ["Deepfake-Offenlegung fehlt; Textprüfung ersetzt sie nicht"])
        data["publication"]["media_disclosure"] = "Dieses Bild wurde künstlich verändert."
        digest = module.fassungs_hash(data["publication"], data["transparency"])
        data["human_review"]["content_hash"] = digest
        data["release"]["content_hash"] = digest
        self.assertTrue(module.pruefen(data)["formal_vollstaendig"])

    def test_unknown_or_string_flags_do_not_pass(self):
        for section, key in (("transparency", "public_interest"), ("checks", "rights"), ("release", "approved")):
            data = complete()
            data[section][key] = "true"
            with self.subTest(section=section):
                self.assertFalse(module.pruefen(data)["formal_vollstaendig"])

    def test_invalid_shape_does_not_raise(self):
        for value in ([], None, {}, {"publication": []}):
            self.assertFalse(module.pruefen(value)["formal_vollstaendig"])

    def test_credentials_in_target_blocked(self):
        data = complete()
        data["publication"]["target_url"] = "https://user:secret@host.example/post"
        self.assertFalse(module.pruefen(data)["formal_vollstaendig"])

    def test_ten_skills_and_compact_mini(self):
        self.assertEqual(len(list((PLUGIN / "skills").glob("*/SKILL.md"))), 10)
        mini = (PLUGIN / "kanzlei-website-redaktion-schnellstart.md").read_bytes()
        self.assertLessEqual(len(mini), 7500)
        self.assertLessEqual(len(mini.decode()), 7500)

    def test_packages_are_reproducible_and_do_not_install_prompts(self):
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp) / "first", Path(tmp) / "second"
            builder.build(first)
            builder.build(second)
            self.assertEqual(len(list(first.iterdir())), 7)
            for path in first.iterdir():
                self.assertEqual(path.read_bytes(), (second / path.name).read_bytes())
            for path in first.glob("*.zip"):
                with zipfile.ZipFile(path) as archive:
                    names = archive.namelist()
                    self.assertEqual(sum(n.endswith('/SKILL.md') for n in names), 10)
                    self.assertFalse(any('__pycache__' in n or n.endswith(tuple(builder.PROMPTS)) for n in names))
                    prefix = 'kanzlei-website-redaktion/' if 'portable' in path.name else ''
                    self.assertIn(prefix + 'assets/kanzlei-website-start.md', names)
                    self.assertIn(prefix + 'references/recht-und-transparenz.md', names)
                    self.assertIsNone(archive.testzip())
            with self.assertRaises(ValueError):
                builder.build(first)


if __name__ == "__main__":
    unittest.main()
