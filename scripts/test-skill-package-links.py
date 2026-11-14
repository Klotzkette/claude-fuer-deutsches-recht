#!/usr/bin/env python3
"""Portabilitätskorrekturen benötigen vorhandene Ziele und inverse Inhaltsbelege."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("package_links", Path(__file__).with_name("repair-skill-package-links.py"))
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)


class PackageLinkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.path = "fachgebiet/skills/alter-inhalt/FACHINHALT.md"
        self.original = b"# Unveraenderter Fachtext\n\n[Fall](../../../testakten/fall/README.md)\n"
        self.write(self.path, self.original)
        self.write("testakten/fall/README.md", b"# Vorhandene Testakte\n")
        active = self.write("fachgebiet/skills/arbeitsweg/SKILL.md", b"# Arbeitsweg\n\n[Vertiefung](../alter-inhalt/FACHINHALT.md)\n")
        digest = R.E["sha"](self.original)
        self.source_map = {"schema_version": 1, "files": [{"original_path": self.path.replace("FACHINHALT", "SKILL"), "path": self.path,
                          "original_sha256": digest, "sha256": digest, "edits": []}], "integration_inventory": [], "migrations": [],
                          "plugins": [{"name": "fachgebiet", "source": "fachgebiet", "active_skills": ["arbeitsweg"],
                                       "routes": [{"slug": "arbeitsweg", "sha256": R.E["file_sha"](active)}]}]}
        profile = {"plugin": "fachgebiet", "reference_reviews": [{"skill_path": self.path, "sha256": digest, "needs_review": True, "verdict": "needs_review", "reviewed_on": "2026-09-01"}]}
        self.write("quality/evals/fachgebiet.json", R.E["json_bytes"](profile))

    def write(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def test_plan_is_read_only_then_composes_lossless_source_proof(self):
        plan = R.prepare(self.root, self.source_map)
        self.assertEqual((self.root / self.path).read_bytes(), self.original)
        self.assertEqual(len(plan["files"]), 1)
        updated, audit = R.apply(self.root, self.source_map, plan, "quality/audit.json")
        self.assertEqual(audit["isolated_package_link_errors"], 0)
        record = updated["files"][0]
        current = (self.root / self.path).read_bytes()
        self.assertIn(b"https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/fall/README.md", current)
        self.assertEqual(R.E["restore_original"](current, record["edits"]), self.original)
        self.assertEqual(record["original_sha256"], R.E["sha"](self.original))
        profile = json.loads((self.root / "quality/evals/fachgebiet.json").read_text())
        review = profile["reference_reviews"][0]
        self.assertEqual(review["sha256"], record["sha256"])
        self.assertTrue(review["needs_review"])
        self.assertEqual(review["reviewed_on"], "2026-09-01")

    def test_missing_target_is_not_invented(self):
        (self.root / "testakten/fall/README.md").unlink()
        with self.assertRaisesRegex(ValueError, "Kein belegtes Repository-Ziel"):
            R.prepare(self.root, self.source_map)
        self.assertEqual((self.root / self.path).read_bytes(), self.original)

    def test_parallel_source_change_prevents_any_followup_mutation(self):
        plan = R.prepare(self.root, self.source_map)
        changed = self.original + b"\nNeue fachliche Aussage\n"
        (self.root / self.path).write_bytes(changed)
        with self.assertRaisesRegex(ValueError, "Quelle seit Plan geändert"):
            R.apply(self.root, self.source_map, plan, "quality/audit.json")
        self.assertEqual((self.root / self.path).read_bytes(), changed)

    def test_explicit_extra_plugin_keeps_its_own_inverse_source_proof(self):
        self.write(".claude-plugin/marketplace.json", json.dumps({"plugins": [
            {"name": "fachgebiet", "source": "./fachgebiet"},
            {"name": "zusatz", "source": "./verschachtelt/zusatz"},
        ]}).encode())
        extra_path = "verschachtelt/zusatz/skills/arbeiten/SKILL.md"
        original = b"# Bestehender Skill\n\n[Fall](../../../../testakten/fall/README.md)\n"
        self.write(extra_path, original)
        plan = R.prepare(self.root, self.source_map, {"plugins": [{"name": "zusatz"}]})
        updated, audit = R.apply(self.root, self.source_map, plan, "quality/audit.json")
        record = next(r for r in updated["files"] if r["path"] == extra_path)
        self.assertEqual(record["preservation_phase"], "additional_unchanged_plugin_package_link")
        self.assertEqual(R.E["restore_original"]((self.root / extra_path).read_bytes(), record["edits"]), original)
        self.assertEqual(audit["isolated_package_link_errors"], 0)
        self.assertEqual([p["name"] for p in updated["plugins"]], ["fachgebiet"])


if __name__ == "__main__":
    unittest.main()
