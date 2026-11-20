#!/usr/bin/env python3
"""Nachweis: Aktenverlust, Verfälschung und kaputte Zusammenführung fallen auf."""
import copy
import json
from pathlib import Path
import runpy
import subprocess
import tempfile
import unittest

V = runpy.run_path(str(Path(__file__).with_name("validate-plugin-consolidation.py")))


class PreservationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write(".claude-plugin/marketplace.json", json.dumps({"plugins": [{"name": "ziel", "source": "./ziel"}]}))
        self.write("ziel/.claude-plugin/plugin.json", '{"name":"ziel","version":"1.0.0"}')
        self.write("ziel/skills/auftrag/SKILL.md", "# Auftrag\n")
        self.write("ziel/README.md", "[Akte](../testakten/fall/beleg.pdf)\n")
        self.write("alt/README.md", "[Gemeinsames Plugin](../ziel/README.md)\n")
        self.write("alt/README-bestand.md", "Ursprünglicher Einstieg\n")
        self.write("testakten/fall/beleg.pdf", b"%PDF-1.7\nOriginalbeleg\n%%EOF")
        self.registry = {"schema_version": 1, "version": "1.0.0", "consolidations": [{"legacy": "alt", "canonical": "ziel", "active_skills": 1, "case_entries": ["testakten/fall"]}]}
        self.inventory = {"schema_version": 1, "protected_files": [{"path": "testakten/fall/beleg.pdf", "git_blob": V["git_blob"](self.root / "testakten/fall/beleg.pdf")}], "plugin_source_files": [{"path": "alt/README.md", "git_blob": V["git_blob"](self.root / "alt/README-bestand.md")}]}

    def write(self, name, data):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data.encode() if isinstance(data, str) else data)
        return p

    def check(self):
        return V["check"](self.root, self.registry, self.inventory)

    def commit_baseline(self):
        def git(*args):
            return subprocess.check_output(["git", "-C", str(self.root), *args], stderr=subprocess.DEVNULL)
        git("init", "-q")
        git("add", ".")
        git("-c", "user.name=Preservation Test", "-c", "user.email=test@example.invalid",
            "-c", "commit.gpgsign=false", "commit", "-qm", "Baseline")
        self.inventory["baseline_commit"] = git("rev-parse", "HEAD").decode().strip()

    def protect(self, name):
        self.inventory["protected_files"].append({"path": name, "git_blob": V["git_blob"](self.root / name)})

    def test_intact_sources_and_archived_entry_pass(self):
        self.assertEqual(self.check(), [])

    def test_missing_or_altered_case_fails(self):
        p = self.root / "testakten/fall/beleg.pdf"
        p.unlink()
        self.assertTrue(any("fehlt" in e for e in self.check()))
        self.write("testakten/fall/beleg.pdf", b"%PDF-1.7\nAusgetauschter Inhalt\n%%EOF")
        self.assertTrue(any("verändert" in e for e in self.check()))

    def test_legacy_and_canonical_cannot_both_remain_active(self):
        self.write(".claude-plugin/marketplace.json", json.dumps({"plugins": [{"name": "ziel", "source": "./ziel"}, {"name": "alt", "source": "./alt"}]}))
        self.assertTrue(any("Marketplace" in e for e in self.check()))

    def test_missing_case_navigation_or_source_archive_fails(self):
        self.write("ziel/README.md", "# Kein Akteneinstieg\n")
        self.write("alt/README-bestand.md", "Gekürzte Ersatzfassung\n")
        errors = self.check()
        self.assertTrue(any("Akteneinstieg fehlt" in e for e in errors))
        self.assertTrue(any("Quellbestand" in e for e in errors))

    def test_extra_active_skill_is_rejected(self):
        self.write("ziel/skills/unerwartet/SKILL.md", "# Zweiter Skill\n")
        self.assertTrue(any("Skill-Auswahl" in e for e in self.check()))

    def test_declared_twenty_one_skills_pass_but_twenty_two_fail(self):
        for number in range(20):
            self.write(f"ziel/skills/fachfrage-{number}/SKILL.md", "# Fachfrage\n")
        self.registry["consolidations"][0]["active_skills"] = 21
        self.assertEqual(self.check(), [])
        self.write("ziel/skills/zusaetzliche-frage/SKILL.md", "# Zusätzliche Frage\n")
        self.registry["consolidations"][0]["active_skills"] = 22
        self.assertTrue(any("überschreitet 21" in e for e in self.check()))

    def test_path_escape_is_rejected(self):
        self.inventory["protected_files"][0]["path"] = "../ausserhalb.pdf"
        with self.assertRaises(ValueError):
            self.check()

    def test_declared_crlf_checkout_passes_but_content_tampering_fails(self):
        self.write("testakten/.gitattributes", "*.eml text eol=crlf\n*.pdf binary\n")
        name = "testakten/fall/nachricht.eml"
        self.write(name, b"Subject: Urspruengliche Nachricht\n\nInhalt\n")
        self.protect(name)
        self.commit_baseline()
        self.write(name, b"Subject: Urspruengliche Nachricht\r\n\r\nInhalt\r\n")
        self.assertEqual(self.check(), [])
        self.write(name, b"Subject: Urspruengliche Nachricht\r\n\r\nManipulierter Inhalt\r\n")
        self.assertTrue(any(name in e and "verändert" in e for e in self.check()))

    def test_only_catalog_row_for_this_case_at_its_table_position_is_allowed(self):
        slug = "akha-wuerzburg-kitaplatz"
        name = f"testakten/{slug}/README.md"
        divider = "| --- | --- | --- |\n"
        original = (
            "# Originalstand\n\n<!-- BEGIN gesamt-pdf-section (autogen) -->\n"
            "| Was | Format | Quelle |\n" + divider + "| Ursprungsakte | PDF | Beleg |\n"
            "<!-- END gesamt-pdf-section (autogen) -->\n\nHistorische Angabe\n"
        )
        row = V["central_row"](slug) + "\n"
        self.write(name, original)
        self.protect(name)
        enhanced = original.replace(divider, divider + row)
        self.write(name, enhanced)
        self.assertEqual(self.check(), [])
        for altered in (
            enhanced.replace("Historische Angabe", "Geänderter Sachverhalt"),
            enhanced.replace(row, row * 2),
            enhanced.replace(row, V["central_row"]("akha-wuerzburg-glatteis") + "\n"),
            enhanced.replace(row, row[:row.rindex("/")+1] + "Falsches-Druckpaket.zip) |\n"),
            original + row,
        ):
            with self.subTest(text=altered):
                self.write(name, altered)
                self.assertTrue(any(name in e and "verändert" in e for e in self.check()))

    def test_binary_and_undeclared_text_remain_byte_exact(self):
        self.write(".gitattributes", "*.pdf binary\n")
        self.write("testakten/fall/notiz.txt", b"Original\n")
        self.protect("testakten/fall/notiz.txt")
        self.commit_baseline()
        # Nachträglich geänderte Attribute dürfen die Ausgangssicherung nicht lockern.
        self.write(".gitattributes", "*.pdf text eol=crlf\n*.txt text eol=crlf\n")
        self.write("testakten/fall/notiz.txt", b"Original\r\n")
        pdf = self.root / "testakten/fall/beleg.pdf"
        pdf.write_bytes(pdf.read_bytes().replace(b"\n", b"\r\n"))
        errors = self.check()
        self.assertTrue(any("notiz.txt" in e and "verändert" in e for e in errors))
        self.assertTrue(any("beleg.pdf" in e and "verändert" in e for e in errors))

    def test_nul_binary_is_not_normalized_even_with_text_attribute(self):
        self.write(".gitattributes", "*.eml text eol=crlf\n")
        name = "testakten/fall/binaer.eml"
        self.write(name, b"binary\0data\n")
        self.protect(name)
        self.commit_baseline()
        self.write(name, b"binary\0data\r\n")
        self.assertTrue(any(name in e and "verändert" in e for e in self.check()))


if __name__ == "__main__":
    unittest.main()
