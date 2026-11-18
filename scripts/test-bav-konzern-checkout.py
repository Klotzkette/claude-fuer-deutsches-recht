#!/usr/bin/env python3
"""Aktuellen PR-Paketpfad vom historischen bAV-Release abgrenzen."""
import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from zipfile import ZipFile

import yaml

spec = importlib.util.spec_from_file_location("bav_checkout", Path(__file__).with_name("check-bav-konzern-checkout.py"))
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)
DIST = None


class CheckoutBoundaryTests(unittest.TestCase):
    def fixture(self, root, *, source=None, duplicate=False):
        (root / C.H.PLUGIN).mkdir()
        path = root / ".claude-plugin/marketplace.json"
        path.parent.mkdir()
        entry = {"name": C.H.PLUGIN, "version": "445.36.8", "source": source or f"./{C.H.PLUGIN}"}
        path.write_text(json.dumps({"version": "445.36.8", "plugins": [entry] * (2 if duplicate else 1)}))

    def test_current_version_does_not_relabel_historical_release(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            self.fixture(root)
            self.assertEqual(C.current_version(root), "445.36.8")
            self.assertEqual(C.H.VERSION, "445.36.4")
            self.assertEqual(C.H.TAG, "bav-strategie-konzern-v445.36.4")
            with self.assertRaisesRegex(ValueError, "Version passt nicht"):
                C.H.validate_scope(C.H.SCOPE, root)

    def test_wrong_source_and_duplicate_plugin_are_rejected(self):
        for kwargs in ({"source": "./fremdes-plugin"}, {"duplicate": True}):
            with self.subTest(kwargs=kwargs), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp).resolve()
                self.fixture(root, **kwargs)
                with self.assertRaises(ValueError):
                    C.current_version(root)

    def test_current_check_keeps_complete_payload_without_release_identity(self):
        self.assertEqual(C.expected_names() - {C.REPORT}, C.H.expected_names() - {C.H.REPORT, C.H.CHECKSUMS})
        self.assertEqual(len(C.expected_names()), 17)
        self.assertNotIn(C.H.REPORT, C.expected_names())
        self.assertNotIn(C.H.CHECKSUMS, C.expected_names())

    def test_workflow_separates_pull_request_and_historical_publication(self):
        workflow = yaml.safe_load((C.ROOT / ".github/workflows/bav-konzern-release.yml").read_text())
        steps = workflow["jobs"]["verify"]["steps"]
        for command, event in (("scripts/build-bav-konzern-release.py", "workflow_dispatch"),
                               ("scripts/publish-bav-konzern-release.py", "workflow_dispatch"),
                               ("scripts/check-bav-konzern-checkout.py", "pull_request"),
                               ("scripts/test-bav-konzern-release.py --dist", "workflow_dispatch"),
                               ("scripts/test-bav-konzern-checkout.py", "pull_request")):
            matching = [step for step in steps if command in step.get("run", "")]
            self.assertTrue(matching, command)
            for step in matching:
                self.assertEqual(step.get("if"), f"github.event_name == '{event}'", command)
        unconditional = "\n".join(step.get("run", "") for step in steps if "if" not in step)
        self.assertIn("python3 scripts/test-bav-konzern-akten.py\n", unconditional)
        self.assertIn("python3 scripts/test-bav-konzern-release.py\n", unconditional)

    def test_invalid_expected_commit_fails_before_packaging(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "checkout"
            with self.assertRaisesRegex(ValueError, "exakten sauberen Checkout"):
                C.build(target, expected_commit="not-a-commit")
            self.assertFalse(target.exists())

    def package_copy(self, tmp):
        if DIST is None:
            self.skipTest("Vollständiger aktueller Pakettest mit --dist")
        target = Path(tmp) / "checkout"
        shutil.copytree(DIST, target)
        return target

    def refresh_artifact_hash(self, target, filename):
        report = json.loads((target / C.REPORT).read_text())
        report["artifacts"][filename] = C.sha256_file(target / filename)
        (target / C.REPORT).write_text(json.dumps(report))

    def test_complete_current_package_and_all_four_cases(self):
        if DIST is None:
            self.skipTest("Vollständiger aktueller Pakettest mit --dist")
        report = C.validate(DIST)
        self.assertEqual(report["version"], C.current_version(C.ROOT))
        self.assertEqual(report["purpose"], C.PURPOSE)
        self.assertNotIn("tag", report)
        self.assertEqual(set(report["cases"]), set(C.H.CASES))
        self.assertEqual(len(report["plugin"]["skills"]), 10)
        self.assertEqual(len(report["plugin"]["chapters"]), 8)
        self.assertTrue(all(case["intake"] and case["pdfs"] and case["pages"] for case in report["cases"].values()))
        with self.assertRaisesRegex(ValueError, "exakt 18"):
            C.H.validate_assets(DIST)

    def test_modified_skill_rejected_with_refreshed_artifact_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = self.package_copy(tmp)
            filename = f"{C.H.PLUGIN}.zip"
            with ZipFile(target / filename) as archive:
                contents = {name: archive.read(name) for name in archive.namelist()}
            skill = next(name for name in contents if name.endswith("/SKILL.md"))
            contents[skill] += b"\nUngepruefte Ersatzanweisung\n"
            with ZipFile(target / filename, "w") as archive:
                for name, data in contents.items():
                    archive.writestr(name, data)
            self.refresh_artifact_hash(target, filename)
            with self.assertRaisesRegex(ValueError, "Inhalt weicht vom Quellstand"):
                C.validate(target)

    def test_modified_prompt_rejected_with_refreshed_artifact_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = self.package_copy(tmp)
            filename = C.H.PROMPTS[0]
            (target / filename).write_text("Ungeprüfte Ersatzfassung")
            self.refresh_artifact_hash(target, filename)
            with self.assertRaisesRegex(ValueError, "Abweichender Prompt"):
                C.validate(target)

    def test_modified_native_case_rejected_with_refreshed_artifact_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = self.package_copy(tmp)
            filename = C.H.names(C.H.CASES[0])[0]
            with ZipFile(target / filename) as archive:
                contents = {name: archive.read(name) for name in archive.namelist()}
            member = next(name for name in contents if name.startswith("Grundakte/"))
            contents[member] += b"\nUngepruefte Ersatzdaten\n"
            with ZipFile(target / filename, "w") as archive:
                for name, data in contents.items():
                    archive.writestr(name, data)
            self.refresh_artifact_hash(target, filename)
            with self.assertRaisesRegex(ValueError, "Originalbytes"):
                C.validate(target)

    def test_modified_pdf_export_rejected_with_refreshed_artifact_hash(self):
        for filename in C.H.names(C.H.CASES[0])[1:]:
            with self.subTest(filename=filename), tempfile.TemporaryDirectory() as tmp:
                target = self.package_copy(tmp)
                with (target / filename).open("ab") as export:
                    export.write(b"\n% changed export bytes\n")
                self.refresh_artifact_hash(target, filename)
                with self.assertRaisesRegex(ValueError, "Einzel-PDF-Fassung|Gesamt-PDF weicht"):
                    C.validate(target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=Path)
    args, rest = parser.parse_known_args()
    DIST = args.dist
    unittest.main(argv=[__file__, *rest])
