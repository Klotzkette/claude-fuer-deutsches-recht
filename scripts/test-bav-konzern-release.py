#!/usr/bin/env python3
"""Grenzen des bAV-Pakets und Manipulationen auch bei erneuerten Prüfsummen."""
import argparse
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile

from release_asset_common import is_release_asset, write_checksums
from testakte_disclaimer import NOTICE_BYTES

spec = importlib.util.spec_from_file_location("bav_release", Path(__file__).with_name("build-bav-konzern-release.py"))
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)
DIST = None


class ReleaseBoundaryTests(unittest.TestCase):
    def test_explicit_complete_case_scope(self):
        self.assertEqual(len(B.expected_names()), 18)
        scope = copy.deepcopy(B.SCOPE)
        scope["cases"].pop()
        with self.assertRaisesRegex(ValueError, "vollständige"):
            B.validate_scope(scope, B.ROOT)

    def test_only_named_bav_pdfs_are_uploadable(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            for slug in B.CASES:
                path = folder / B.names(slug)[2]
                path.write_bytes(b"pdf")
                self.assertTrue(is_release_asset(path))
            unrelated = folder / "beliebiges-geheimes-dokument.pdf"
            unrelated.write_bytes(b"pdf")
            self.assertFalse(is_release_asset(unrelated))

    def test_native_payload_requires_exact_source_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            original = folder / "daten.csv"
            original.write_text("Person;Rente\n4711;350\n")
            archive = folder / "testakte.zip"
            with ZipFile(archive, "w") as z:
                z.writestr("README.txt", NOTICE_BYTES)
                z.writestr("Grundakte/daten.csv", "Person;Rente\n4711;950\n")
            with self.assertRaisesRegex(ValueError, "Originalbytes"):
                B.verified_archive(archive, [(original, "Grundakte/daten.csv")], notice=True)

    def test_procedural_document_is_rejected_in_intake(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            original = folder / "Klageschrift.txt"
            original.write_text("Bereits ausgearbeitete Klage")
            archive = folder / "testakte.zip"
            with ZipFile(archive, "w") as z:
                z.writestr("README.txt", NOTICE_BYTES)
                z.writestr("Grundakte/Klageschrift.txt", original.read_bytes())
            with self.assertRaisesRegex(ValueError, "Verfahrens"):
                B.verified_archive(archive, [(original, "Grundakte/Klageschrift.txt")], notice=True)

    def test_duplicate_members_cannot_hide_different_content(self):
        import warnings
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            original = folder / "daten.csv"
            original.write_text("x")
            archive = folder / "testakte.zip"
            with warnings.catch_warnings(), ZipFile(archive, "w") as z:
                warnings.simplefilter("ignore", UserWarning)
                z.writestr("Grundakte/daten.csv", "x")
                z.writestr("Grundakte/daten.csv", "y")
            with self.assertRaisesRegex(ValueError, "Archivbestand"):
                B.verified_archive(archive, [(original, "Grundakte/daten.csv")])

    def test_publisher_uses_component_checks_before_network(self):
        publisher = B.load("publish-skill-quality-release.py")
        with patch.object(B, "checkout_state", side_effect=ValueError("dirty checkout")), patch.object(publisher, "execute") as execute:
            with self.assertRaisesRegex(ValueError, "dirty checkout"):
                publisher.publish(Path("unbuilt"), B.SCOPE, "a" * 40, "owner/repo", builder=B)
            execute.assert_not_called()

    def test_packaged_chapters_must_be_reachable_from_a_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry = root / "scripts/data/skill-source-replacements.json"
            registry.parent.mkdir(parents=True)
            chapters = [f"references/konzern/{i}.md" for i in range(8)]
            registry.write_text(json.dumps({"plugins": {B.PLUGIN: {"chapters": chapters}}}))
            files = {}
            for name in ["skills/start/SKILL.md", *chapters]:
                path = root / B.PLUGIN / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# Fachtext\n")
                files[name] = path
            skill = files["skills/start/SKILL.md"]
            skill.write_text("\n".join(f"[Kapitel](../../{c})" for c in chapters[:-1]))
            with self.assertRaisesRegex(ValueError, "nicht erreichbar"):
                B.verify_chapters(files, ["skills/start/SKILL.md"], root)
            skill.write_text(skill.read_text() + f"\n[Letztes Kapitel](../../{chapters[-1]})")
            self.assertEqual(len(B.verify_chapters(files, ["skills/start/SKILL.md"], root)), 8)

    def test_complete_actual_release(self):
        if DIST is None:
            self.skipTest("Vollständiger Pakettest mit --dist")
        result = B.validate_assets(DIST)
        self.assertEqual(set(result["cases"]), set(B.CASES))
        self.assertEqual(len(result["plugin"]["skills"]), 10)

    def test_refreshed_checksums_cannot_hide_modified_prompt(self):
        if DIST is None:
            self.skipTest("Manipulationsnachweis mit --dist")
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "dist"
            shutil.copytree(DIST, target)
            (target / B.PROMPTS[0]).write_text("Ungeprüfte Ersatzfassung")
            write_checksums(target)
            with self.assertRaisesRegex(ValueError, "Abweichender Prompt"):
                B.validate_assets(target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=Path)
    args, rest = parser.parse_known_args()
    DIST = args.dist
    unittest.main(argv=[__file__, *rest])
