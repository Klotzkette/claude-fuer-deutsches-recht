#!/usr/bin/env python3
"""Offline regression tests for builds before immutable complete release tags."""

from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "prepare_complete_release", Path(__file__).with_name("prepare-complete-release.py"),
)
PREPARE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PREPARE)
SHA = "a" * 40
OTHER = "b" * 40
TAG = "v777.2.3"


class PreparationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="prepare-complete-release-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / ".claude-plugin").mkdir()
        (self.root / ".claude-plugin/marketplace.json").write_text(json.dumps({"version": TAG[1:]}))
        self.refs = {}
        self.objects = {}
        self.commands = []
        self.head = SHA
        self.lookup_error = None
        self.created_sha = SHA
        self.creation_error = None
        run = patch.object(PREPARE.PUBLISH, "run", side_effect=self.run_command)
        run.start()
        self.addCleanup(run.stop)

    def run_command(self, command):
        self.commands.append(command)
        def response(value=None, code=0, error=""):
            return subprocess.CompletedProcess(command, code, json.dumps(value) if value else "", error)
        if command[:1] == ["git"]:
            return subprocess.CompletedProcess(command, 0, self.head + "\n", "")
        self.assertEqual(command[:2], ["gh", "api"])
        resource = command[2]
        if "/git/ref/tags/" in resource:
            if self.lookup_error:
                return response(code=1, error=self.lookup_error)
            obj = self.refs.get(resource.split("/git/ref/tags/")[1])
            return response({"object": obj}) if obj else response(code=1, error="gh: Not Found (HTTP 404)")
        if "/git/tags/" in resource:
            return response({"object": self.objects[resource.rsplit("/", 1)[1]]})
        if resource.endswith("/git/refs"):
            self.assertEqual(command[3:5], ["--method", "POST"])
            tag = next(arg.removeprefix("ref=refs/tags/") for arg in command if arg.startswith("ref="))
            self.assertIn(f"sha={SHA}", command)
            if self.created_sha:
                self.refs[tag] = {"type": "commit", "sha": self.created_sha}
            return response(code=1, error=self.creation_error) if self.creation_error else response({"ref": tag})
        self.fail(f"Unexpected command: {command}")

    def ensure(self, **kwargs):
        return PREPARE.ensure_tag("owner/repo", kwargs.get("tag", TAG), kwargs.get("sha", SHA), self.root)

    def assert_read_only(self):
        self.assertFalse(any("POST" in cmd or "DELETE" in cmd or "PATCH" in cmd for cmd in self.commands))

    def test_missing_tag_uses_workflow_commit_without_writes(self):
        self.assertEqual(PREPARE.resolve_commit("owner/repo", TAG, SHA), SHA)
        self.assert_read_only()

    def test_existing_lightweight_or_nested_annotated_tag_wins_over_workflow(self):
        for reference in ({"type": "commit", "sha": OTHER}, {"type": "tag", "sha": "c" * 40}):
            self.refs[TAG] = reference
            self.objects = {"c" * 40: {"type": "tag", "sha": "d" * 40},
                            "d" * 40: {"type": "commit", "sha": OTHER}}
            self.assertEqual(PREPARE.resolve_commit("owner/repo", TAG, SHA), OTHER)
        self.assert_read_only()

    def test_auth_network_and_ambiguous_not_found_fail_without_fallback(self):
        for error in ("HTTP 403", "network failure", "invalid authentication", "release not found", "Not Found"):
            self.lookup_error = error
            with self.subTest(error=error), self.assertRaises(RuntimeError):
                PREPARE.resolve_commit("owner/repo", TAG, SHA)
            with self.assertRaises(RuntimeError):
                self.ensure()
        self.assert_read_only()

    def test_invalid_inputs_stop_before_remote_calls(self):
        for tag in ("akten-v777.2.3", "v777.2", "v777.2.3\n", "refs/tags/v777.2.3"):
            with self.subTest(tag=tag), self.assertRaises(ValueError):
                PREPARE.resolve_commit("owner/repo", tag, SHA)
        for sha in ("main", "a" * 39, SHA + "\n"):
            with self.subTest(sha=sha), self.assertRaises(ValueError):
                PREPARE.resolve_commit("owner/repo", TAG, sha)
        self.assertEqual(self.commands, [])

    def test_create_exact_validated_commit_and_retry_without_any_mutation(self):
        self.assertEqual(self.ensure(), SHA)
        post = next(command for command in self.commands if "POST" in command)
        self.assertIn(f"ref=refs/tags/{TAG}", post)
        self.assertIn(f"sha={SHA}", post)
        self.assertNotIn("--force", sum(self.commands, []))
        self.commands.clear()
        self.assertEqual(self.ensure(), SHA)
        self.assert_read_only()

    def test_existing_other_commit_is_never_moved(self):
        self.refs[TAG] = {"type": "commit", "sha": OTHER}
        with self.assertRaisesRegex(ValueError, "not changed"):
            self.ensure()
        self.assertEqual(self.refs[TAG]["sha"], OTHER)
        self.assert_read_only()

    def test_wrong_checkout_or_marketplace_never_creates_tag(self):
        self.head = OTHER
        with self.assertRaisesRegex(ValueError, "checkout"):
            self.ensure()
        with self.assertRaisesRegex(ValueError, "marketplace"):
            self.ensure(tag="v777.2.4")
        self.assert_read_only()

    def test_lost_creation_response_is_safe_only_at_the_exact_commit(self):
        self.creation_error = "lost response"
        self.assertEqual(self.ensure(), SHA)
        self.refs.clear()
        self.created_sha = OTHER
        with self.assertRaisesRegex(ValueError, "not changed"):
            self.ensure()
        self.assertEqual(self.refs[TAG]["sha"], OTHER)

    def test_failed_creation_never_claims_success(self):
        self.creation_error = "HTTP 403"
        self.created_sha = None
        with self.assertRaisesRegex(RuntimeError, "Could not create"):
            self.ensure()
        self.assertNotIn(TAG, self.refs)

    def test_cli_success_prints_only_sha_and_error_has_no_sha_output(self):
        arguments = ["prepare", "resolve", TAG, "--repo", "owner/repo", "--fallback-sha", SHA]
        with patch.object(sys, "argv", arguments), redirect_stdout(io.StringIO()) as output:
            self.assertEqual(PREPARE.main(), 0)
        self.assertEqual(output.getvalue(), SHA + "\n")
        self.lookup_error = "HTTP 403"
        with patch.object(sys, "argv", arguments), redirect_stdout(io.StringIO()) as output, \
                redirect_stderr(io.StringIO()) as error:
            self.assertEqual(PREPARE.main(), 1)
        self.assertEqual(output.getvalue(), "")
        self.assertIn("HTTP 403", error.getvalue())


if __name__ == "__main__":
    unittest.main()
