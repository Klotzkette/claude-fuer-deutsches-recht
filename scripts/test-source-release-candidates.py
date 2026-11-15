#!/usr/bin/env python3
"""Trennt geprüfte Quellkandidaten von unveränderlichen Release-Nachweisen."""

import copy
import importlib.util
import json
import io
import re
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest
import zipfile
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

    def test_anfechtung_workflow_build_and_verify_use_the_fixed_component_scope(self):
        text = (ROOT/'.github/workflows/insolvenzanfechtung-release.yml').read_text(encoding='utf-8')
        commands = re.findall(r'^\s*python3 scripts/build-skill-quality-release\.py[^\n]*', text, re.M)
        self.assertEqual(len(commands), 2)
        for command in commands:
            self.assertIn('--scope scripts/data/insolvenzanfechtung-pruefumfang.json', command)
            self.assertNotIn('skill-quality-release-scope.json', command)
        self.assertNotIn('--verify', commands[0])
        self.assertIn('--verify', commands[1])


class InsolvenzanfechtungCurrentParent(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location("anfechtung_current_parent", ROOT / "scripts/build-insolvenzanfechtung-release.py")
        self.builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.builder)
        self.assertEqual((self.builder.VERSION, self.builder.TAG, self.builder.PARENT_VERSION),
                         ("1.1.0", "insolvenzanfechtung-v1.1.0", "445.35.4"))
        self.original_proof = self.builder.PROOF.read_bytes()
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.proof = self.root / "historical-proof.json"
        self.proof.write_bytes(self.original_proof)
        self.enterContext(patch.object(self.builder, "ROOT", self.root))
        self.enterContext(patch.object(self.builder, "PROOF", self.proof))
        self.market_path = self.root / ".claude-plugin/marketplace.json"
        self.route_path = self.root / "scripts/scoped-release-assets.json"
        self.parent_manifest = self.root / self.builder.PARENT / ".claude-plugin/plugin.json"
        self.market = {"version": "445.35.3", "plugins": [{"name": self.builder.PARENT,
                       "version": "445.36.0", "source": "./" + self.builder.PARENT}]}
        self.route = {"schema_version": 1, "assets": {self.builder.PARENT + ".zip": "qualitaetsrunde-v445.36.0"}}
        self.write_json(self.market_path, self.market)
        self.write_json(self.route_path, self.route)
        self.write_json(self.parent_manifest, {"name": self.builder.PARENT, "version": "445.36.0"})
        for relative in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
            self.write_json(self.root / self.builder.NAME / relative, {"name": self.builder.NAME, "version": "1.1.0"})
        for number in range(11):
            source = self.root / self.builder.NAME / "skills" / f"fachmodul-{number}" / "SKILL.md"
            source.parent.mkdir(parents=True)
            source.write_text("Erhaltener Fachtext", encoding="utf-8")

    @staticmethod
    def write_json(path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def test_candidate_build_uses_current_exact_parent_without_release_tag(self):
        dist = self.root / "candidate"
        with patch.object(self.builder, "CASES", ()), patch.object(self.builder, "prompt_sources", return_value=[]), redirect_stdout(io.StringIO()):
            self.builder.build(dist, self.root, candidate=True)
        record = json.loads((dist / "quellenabgleich.json").read_text())
        self.assertIsNone(record["tag"])
        self.assertEqual(record["build_mode"], "source_candidate_not_published")
        self.assertEqual(record["published_proof_status"], "source_candidate_not_published")
        self.assertEqual(record["historical_release_reference"], "insolvenzanfechtung-v1.1.0")
        self.assertEqual(record["candidate_parent_route"], {"version": "445.36.0", "tag": "qualitaetsrunde-v445.36.0"})
        self.assertEqual(record["plugins"][self.builder.PARENT]["version"], "445.36.0")
        with zipfile.ZipFile(dist / (self.builder.PARENT + ".zip")) as archive:
            self.assertEqual(archive.read(".claude-plugin/plugin.json"), self.parent_manifest.read_bytes())
        self.assertEqual(self.proof.read_bytes(), self.original_proof)
        self.assertEqual(json.loads(self.route_path.read_text()), self.route)

    def test_historical_default_and_proof_writer_reject_new_parent_before_output(self):
        for kwargs in ({}, {"write_proof": True}, {"write_proof": True, "candidate": True}):
            dist = self.root / "historical"
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                self.builder.build(dist, self.root, **kwargs)
            self.assertFalse(dist.exists())
            self.assertEqual(self.proof.read_bytes(), self.original_proof)

    def test_candidate_requires_exact_marketplace_manifest_and_route(self):
        self.assertEqual(self.builder.candidate_parent_identity()["version"], "445.36.0")
        for kind in ("missing-route", "wrong-route-version", "wrong-manifest-version", "duplicate-marketplace", "different-source"):
            market, route = copy.deepcopy(self.market), copy.deepcopy(self.route)
            manifest = {"name": self.builder.PARENT, "version": "445.36.0"}
            if kind == "missing-route":
                route["assets"] = {}
            elif kind == "wrong-route-version":
                route["assets"][self.builder.PARENT + ".zip"] = "qualitaetsrunde-v445.36.1"
            elif kind == "wrong-manifest-version":
                manifest["version"] = "445.36.1"
            elif kind == "duplicate-marketplace":
                market["plugins"].append(copy.deepcopy(market["plugins"][0]))
            else:
                market["plugins"][0]["source"] = "./anderes-plugin"
            self.write_json(self.market_path, market)
            self.write_json(self.route_path, route)
            self.write_json(self.parent_manifest, manifest)
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                self.builder.candidate_parent_identity()
        self.assertEqual(self.proof.read_bytes(), self.original_proof)

    def test_candidate_proof_never_accepts_arbitrary_version(self):
        proof = json.loads(self.original_proof)
        proof["version"] = "445.36.0"
        proof["assets"][self.builder.PARENT + ".zip"] = "0" * 64
        self.assertEqual(self.builder.published_proof_status(proof, True), "source_candidate_not_published")
        with self.assertRaises(ValueError):
            self.builder.published_proof_status(proof)
        proof["version"] = "445.36.1"
        with self.assertRaises(ValueError):
            self.builder.published_proof_status(proof, True)
        self.assertEqual(self.proof.read_bytes(), self.original_proof)


if __name__ == "__main__":
    unittest.main()
