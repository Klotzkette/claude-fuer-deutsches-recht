#!/usr/bin/env python3
"""Trennt geprüfte Quellkandidaten von unveränderlichen Release-Nachweisen."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class SourceReleaseCandidates(unittest.TestCase):
    def test_candidate_never_changes_published_proof_or_release_default(self):
        for name in ("insolvenzanfechtung", "insolvenzsachbearbeitung"):
            spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"build-{name}-release.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            original = module.PROOF.read_bytes()
            expected = json.loads(original)
            with tempfile.TemporaryDirectory() as temp:
                proof = Path(temp) / "proof.json"
                proof.write_bytes(original)
                with patch.object(module, "PROOF", proof), self.subTest(builder=name):
                    self.assertEqual(module.published_proof_status(expected), "matching_release")
                    self.assertEqual(module.published_proof_status(expected, True), "matching_release")
                    candidate = copy.deepcopy(expected)
                    asset = next(iter(candidate["assets"]))
                    candidate["assets"][asset] = "0" * 64
                    with self.assertRaises(ValueError):
                        module.published_proof_status(candidate)
                    self.assertEqual(module.published_proof_status(candidate, True), "source_candidate_not_published")
                    for field in ("version", "release", "plugins"):
                        invalid = copy.deepcopy(candidate)
                        invalid[field] = None
                        with self.subTest(field=field), self.assertRaises(ValueError):
                            module.published_proof_status(invalid, True)
                    invalid = copy.deepcopy(candidate)
                    invalid["assets"] = {}
                    with self.assertRaises(ValueError):
                        module.published_proof_status(invalid, True)
                    with self.assertRaises(ValueError):
                        module.build(Path(temp) / "dist", Path(temp), write_proof=True, candidate=True)
                    self.assertEqual(proof.read_bytes(), original)
                    proof.write_text("{", encoding="utf-8")
                    with self.assertRaises(json.JSONDecodeError):
                        module.published_proof_status(candidate, True)

    def test_workflows_only_enable_candidate_mode_for_pull_requests(self):
        for name in ("insolvenzanfechtung", "insolvenzsachbearbeitung"):
            text = (ROOT / ".github/workflows" / f"{name}-release.yml").read_text(encoding="utf-8")
            self.assertIn('if [ "$GITHUB_EVENT_NAME" = pull_request ]; then candidate=(--candidate); fi', text)
            self.assertIn('"${candidate[@]}"', text)
            self.assertNotIn("--write-proof", text)


if __name__ == "__main__":
    unittest.main()
