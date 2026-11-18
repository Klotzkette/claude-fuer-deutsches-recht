#!/usr/bin/env python3
"""Regressionen für aktuelle Prüfpakete ohne historischen Releaseanspruch."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("classic_checkout", Path(__file__).with_name("check-classic-components-checkout.py"))
CHECK = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CHECK)


class CheckoutTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        self.root.mkdir()
        self.dist = Path(self.temp.name) / "output"

    def put(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def fixture(self, component="cisg"):
        names, dataset, count, skills = CHECK.COMPONENTS[component]
        entries = []
        for name in names:
            entries.append({"name": name, "source": "./" + name, "version": "9.8.7"})
            for relative in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
                self.put(f"{name}/{relative}", json.dumps({"name": name, "version": "9.8.7"}))
            self.put(f"{name}/README.md", "Aktuelles Plugin\n")
            for n in range(skills):
                self.put(f"{name}/skills/route-{n}/SKILL.md", f"---\nname: route-{n}\ndescription: Prüfung\n---\n\n# Prüfung\n\nAktueller Text {n}.\n")
            for kind in ("werkstatt", "schnellstart", "hauptproblem"):
                self.put(f"{name}/{name}-{kind}.md", f"Eigenständiger {kind}\n")
        self.put(".claude-plugin/marketplace.json", json.dumps({"version": "9.8.7", "plugins": entries}))
        self.put("LICENSE", "Testlizenz\n")
        cases = []
        for n in range(count):
            slug = f"fall-{n}"
            name = names[n // 2] if component == "sanktionen" else names[0]
            cases.append({"slug": slug, "plugin": name})
            self.put(f"testakten/{slug}/gesamt-pdf/{slug}_gesamt.pdf", f"Unveränderte PDF-Bytes {n}")
            folder = "downloads" if component == "sanktionen" else "testakte/downloads"
            for suffix in ("", "-einzelpdfs"):
                self.put(f"{name}/{folder}/testakte-{slug}{suffix}.zip", f"Unveränderte ZIP-Bytes {n}{suffix}")
        self.put("scripts/data/" + dataset, json.dumps(cases))
        if component == "kuendigungsschutz":
            name = names[0]
            seewerk = [{"slug": f"seewerk-{n}"} for n in range(2)]
            self.put(f"{name}/testakte/pruefung/seewerk-bestand.json", json.dumps(seewerk))
            for case in seewerk:
                slug = case["slug"]
                for filename in (slug + "_gesamt.pdf", *(f"testakte-{slug}{s}.zip" for s in ("", "-einzelpdfs", "-anlagen-k1-k14"))):
                    self.put(f"{name}/testakte/downloads/{filename}", filename)
            for filename in ("mandantengespraech-seewerk.md", "seewerk-quellen-und-grenzen.md"):
                self.put(f"{name}/referentenmaterial/{filename}", filename)
            self.put(f"{name}/testakte/downloads/testakte-arbeitsrecht-muster-uferwerk-berufung-einzelpdfs.zip", "Uferwerk PDF-ZIP")
        return names

    def checksums(self):
        (self.dist / CHECK.CHECKSUMS).write_text("".join(
            f"{CHECK.sha256_file(p)}  {p.name}\n" for p in sorted(self.dist.iterdir()) if p.name != CHECK.CHECKSUMS))

    def test_all_three_inventories_include_every_historical_companion_asset(self):
        for component, count in (("cisg", 27), ("sanktionen", 44), ("kuendigungsschutz", 38)):
            with self.subTest(component=component), tempfile.TemporaryDirectory() as directory:
                self.root = Path(directory) / "source"
                self.root.mkdir()
                self.dist = Path(directory) / "output"
                names = self.fixture(component)
                report = CHECK.build(self.root, component, self.dist)
                self.assertEqual(len(list(self.dist.iterdir())), count)
                self.assertEqual(report["purpose"], "current-checkout-validation-only")
                self.assertNotIn("tag", report)
                self.assertEqual({row["version"] for row in report["plugins"].values()}, {"9.8.7"})
                for name in names:
                    for kind in ("werkstatt", "schnellstart", "hauptproblem"):
                        self.assertIn(f"{name}-{kind}.md", report["copied_assets"])
                self.assertEqual(CHECK.verify(self.root, component, self.dist), report)

    def test_missing_required_source_asset_fails_before_output(self):
        self.fixture()
        (self.root / "testakten/fall-1/gesamt-pdf/fall-1_gesamt.pdf").unlink()
        with self.assertRaisesRegex(ValueError, "Quelldatei fehlt"):
            CHECK.build(self.root, "cisg", self.dist)
        self.assertFalse(self.dist.exists())

    def test_wrong_manifest_version_is_rejected(self):
        names = self.fixture()
        self.put(f"{names[0]}/.codex-plugin/plugin.json", json.dumps({"name": names[0], "version": "1.0.0"}))
        with self.assertRaisesRegex(ValueError, "Version weicht ab"):
            CHECK.build(self.root, "cisg", self.dist)

    def test_zip_skill_tampering_fails_even_with_recomputed_checksums(self):
        names = self.fixture()
        CHECK.build(self.root, "cisg", self.dist)
        target = self.dist / (names[0] + ".zip")
        with zipfile.ZipFile(target) as archive:
            files = {name: archive.read(name) for name in archive.namelist()}
        files["skills/route-0/SKILL.md"] += b"Manipulation"
        with zipfile.ZipFile(target, "w") as archive:
            for name, content in files.items():
                archive.writestr(name, content)
        self.checksums()
        with self.assertRaisesRegex(ValueError, "Inhalt weicht"):
            CHECK.verify(self.root, "cisg", self.dist)

    def test_current_skill_change_invalidates_source_binding(self):
        names = self.fixture()
        CHECK.build(self.root, "cisg", self.dist)
        self.put(f"{names[0]}/skills/route-0/SKILL.md", "Geänderter aktueller Skill")
        with self.assertRaisesRegex(ValueError, "Quellenbindungen"):
            CHECK.verify(self.root, "cisg", self.dist)

    def test_missing_or_extra_output_files_are_rejected(self):
        self.fixture()
        CHECK.build(self.root, "cisg", self.dist)
        extra = self.dist / "unerwartet.txt"
        extra.write_text("zusätzlich")
        with self.assertRaisesRegex(ValueError, "Prüfbestand"):
            CHECK.verify(self.root, "cisg", self.dist)
        extra.unlink()
        (self.dist / "fall-0_gesamt.pdf").unlink()
        with self.assertRaisesRegex(ValueError, "Prüfbestand"):
            CHECK.verify(self.root, "cisg", self.dist)

    def test_checksums_cannot_omit_or_change_an_asset(self):
        self.fixture()
        CHECK.build(self.root, "cisg", self.dist)
        checksums = self.dist / CHECK.CHECKSUMS
        lines = checksums.read_text().splitlines(keepends=True)
        checksums.write_text("".join(lines[1:]))
        with self.assertRaisesRegex(ValueError, "Prüfsummenbestand"):
            CHECK.verify(self.root, "cisg", self.dist)
        checksums.write_text("0" * 64 + lines[0][64:] + "".join(lines[1:]))
        with self.assertRaisesRegex(ValueError, "Prüfsumme stimmt"):
            CHECK.verify(self.root, "cisg", self.dist)

    def test_copied_pdf_bytes_are_checked_independently_of_checksums(self):
        self.fixture()
        CHECK.build(self.root, "cisg", self.dist)
        (self.dist / "fall-0_gesamt.pdf").write_bytes(b"veraendert")
        self.checksums()
        with self.assertRaisesRegex(ValueError, "Begleitasset weicht"):
            CHECK.verify(self.root, "cisg", self.dist)

    def test_source_inventory_and_report_cannot_omit_files(self):
        names = self.fixture()
        CHECK.build(self.root, "cisg", self.dist)
        report_path = self.dist / CHECK.REPORT
        report = json.loads(report_path.read_text())
        del report["plugins"][names[0]]["files"]["README.md"]
        report_path.write_text(json.dumps(report))
        self.checksums()
        with self.assertRaisesRegex(ValueError, "Quellenbindungen"):
            CHECK.verify(self.root, "cisg", self.dist)

    def test_workflows_keep_source_checks_and_separate_historical_dispatch(self):
        for component, workflow, source_test in (
            ("cisg", "cisg", "test-cisg.py"),
            ("sanktionen", "sanktionen", "test-sanktionen.py"),
            ("kuendigungsschutz", "kuendigungsschutzklagewerkstatt", "test-kuendigungsschutzklagewerkstatt.py"),
        ):
            with self.subTest(component=component):
                config = yaml.load((ROOT / f".github/workflows/{workflow}-release.yml").read_text(), Loader=yaml.BaseLoader)
                steps = config["jobs"]["check"]["steps"]
                current = [s for s in steps if "check-classic-components-checkout.py" in s.get("run", "")]
                self.assertEqual(len(current), 1)
                self.assertEqual(current[0]["if"], "github.event_name == 'pull_request'")
                self.assertIn(f"check-classic-components-checkout.py {component}", current[0]["run"])
                self.assertIn("test-classic-components-checkout.py", current[0]["run"])
                historical = [s for s in steps if f"build-{component}-release.py" in s.get("run", "")]
                self.assertEqual(len(historical), 1)
                self.assertEqual(historical[0]["if"], "github.event_name == 'workflow_dispatch'")
                self.assertIn(source_test + " --dist", historical[0]["run"])
                self.assertTrue(any(f"scripts/{source_test}\n" in s.get("run", "") and "if" not in s for s in steps))


if __name__ == "__main__":
    unittest.main()
