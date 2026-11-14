#!/usr/bin/env python3
"""Paketregressionen: reproduzierbarer Build und unabhängiger Quellenabgleich."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

SPEC = importlib.util.spec_from_file_location("release", Path(__file__).with_name("build-insolvenzrecht-release.py"))
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dist = Path(self.temp.name) / "dist"
        with contextlib.redirect_stdout(io.StringIO()):
            release.build(self.dist)

    def refresh_checksums(self):
        (self.dist / release.CHECKSUMS).write_text("".join(
            f"{hashlib.sha256((self.dist / name).read_bytes()).hexdigest()}  {name}\n"
            for name in sorted(release.PAYLOAD)))

    def test_repeat_is_byte_identical_and_refuses_overwrite(self):
        second = Path(self.temp.name) / "second"
        with contextlib.redirect_stdout(io.StringIO()):
            release.build(second)
        for name in release.ASSETS:
            self.assertEqual((self.dist / name).read_bytes(), (second / name).read_bytes(), name)
        with self.assertRaisesRegex(ValueError, "leer"):
            release.build(self.dist)

    def test_rehashed_stale_plugin_is_rejected(self):
        path = self.dist / "insolvenzrecht.zip"
        with zipfile.ZipFile(path) as archive:
            content = {name: archive.read(name) for name in archive.namelist()}
        content["skills/einstieg-routing/SKILL.md"] = b"Veralteter Einstieg ohne Fachmodule.\n"
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
            for name, payload in content.items():
                archive.writestr(name, payload)
        self.refresh_checksums()
        with self.assertRaisesRegex(ValueError, "ZIP-Datei weicht ab"):
            release.verify(self.dist)

    def test_rehashed_wrong_prompt_is_rejected(self):
        (self.dist / release.PROMPTS[0]).write_text("Veralteter Werkstattprompt.\n")
        self.refresh_checksums()
        with self.assertRaisesRegex(ValueError, "Prompt weicht ab"):
            release.verify(self.dist)

    def test_incomplete_or_extra_release_is_rejected(self):
        (self.dist / "unerwartet.txt").write_text("nicht freigegeben")
        with self.assertRaisesRegex(ValueError, "genau sechs"):
            release.verify(self.dist)
        (self.dist / "unerwartet.txt").unlink()
        (self.dist / release.PROMPTS[1]).unlink()
        with self.assertRaisesRegex(ValueError, "genau sechs"):
            release.verify(self.dist)

    def test_stale_import_source_map_blocks_verify_and_build(self):
        with patch.object(release.FACHMODULE, "check_tree", return_value=["veraltet: SOURCE_MAP.json"]):
            with self.assertRaisesRegex(ValueError, "Originalquellen.*|SOURCE_MAP"):
                release.verify(self.dist)
            with self.assertRaisesRegex(ValueError, "Originalquellen.*|SOURCE_MAP"):
                release.build(Path(self.temp.name) / "stale-build")


class ReleaseTagTests(unittest.TestCase):
    def test_tag_must_resolve_to_checked_commit(self):
        tag = "insolvenzrecht-v445.35.4"
        expected = "a" * 40
        remote = json.dumps({"type": "commit", "sha": expected})
        with patch.object(release.subprocess, "check_output", side_effect=[expected + "\n", remote]) as command:
            release.verify_remote_tag(tag)
        self.assertEqual(command.call_args_list[0].args[0], ["git", "rev-parse", "HEAD"])
        self.assertEqual(command.call_args_list[1].args[0],
                         ["gh", "api", f"repos/{release.REPOSITORY}/git/ref/tags/{tag}", "--jq", ".object"])

    def test_foreign_tag_commit_is_rejected(self):
        remote = json.dumps({"type": "commit", "sha": "b" * 40})
        with patch.object(release.subprocess, "check_output", side_effect=["a" * 40, remote]):
            with self.assertRaisesRegex(ValueError, "geprüften Checkout"):
                release.verify_remote_tag("insolvenzrecht-v445.35.4")

    def test_nested_annotated_tag_is_peeled_to_commit(self):
        expected = "a" * 40
        objects = [json.dumps({"type": kind, "sha": sha * 40}) for kind, sha in
                   (("tag", "b"), ("tag", "c"), ("commit", "a"))]
        with patch.object(release.subprocess, "check_output", side_effect=[expected, *objects]) as command:
            release.verify_remote_tag("insolvenzrecht-v445.35.4")
        self.assertEqual(command.call_args_list[-1].args[0][2],
                         f"repos/{release.REPOSITORY}/git/tags/{'c' * 40}")


if __name__ == "__main__":
    unittest.main()
