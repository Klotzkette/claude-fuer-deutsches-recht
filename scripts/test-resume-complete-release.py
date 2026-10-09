#!/usr/bin/env python3
"""Offline-Prüfungen der Herkunft und bytegleichen Release-Wiederaufnahme."""

from copy import deepcopy
from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "resume_complete_release", Path(__file__).with_name("resume-complete-release.py"))
RESUME = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RESUME)
SHA = "a" * 40
OTHER_SHA = "b" * 40
TAG = "v777.2.3"
PUBLISH_STEP = "Beide Releases hochladen, verifizieren und geordnet veröffentlichen"
ARTIFACT_STEP = "Artefakte hochladen (immer)"


class OfflineTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="resume-complete-release-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        # Kein versehentlich echter GitHub-, Git- oder Warteaufruf im Test.
        for target, name in ((RESUME.subprocess, "run"), (RESUME.subprocess, "check_output"),
                             (RESUME.PUBLISH.time, "sleep")):
            guard = patch.object(target, name, side_effect=AssertionError(f"Unerwarteter Aufruf: {name}"))
            guard.start()
            self.addCleanup(guard.stop)


class ProvenanceTests(OfflineTest):
    def setUp(self):
        super().setUp()
        self.config = {
            "repo": "owner/repo", "run_id": 123, "source_commit": SHA, "tag": TAG,
            "required_steps": ["Quellen prüfen", "Pakete prüfen"],
            "artifact_id": 456, "artifact_digest": "sha256:" + "c" * 64,
            "artifact_bytes": 1000,
        }
        self.run = {
            "id": 123, "head_sha": SHA, "repository": {"full_name": "owner/repo"},
            "head_repository": {"full_name": "owner/repo"},
            "path": ".github/workflows/release-plugin-zips.yml",
            "event": "workflow_dispatch", "head_branch": "main",
            "status": "completed", "conclusion": "failure",
        }
        self.jobs = {"total_count": 1, "jobs": [{
            "name": "build-and-release", "conclusion": "failure", "steps": [
                {"name": name, "conclusion": "success"} for name in self.config["required_steps"]
            ] + [{"name": PUBLISH_STEP, "conclusion": "failure"},
                 {"name": ARTIFACT_STEP, "conclusion": "success"}],
        }]}
        self.artifact = {
            "id": 456, "name": "plugin-zips", "expired": False,
            "digest": self.config["artifact_digest"], "size_in_bytes": 1000,
            "workflow_run": {"id": 123, "head_sha": SHA},
        }

    def verify(self, *, run=None, jobs=None, artifact=None, tag_sha=SHA):
        RESUME.verify_run(self.config, self.run if run is None else run,
                          self.jobs if jobs is None else jobs,
                          self.artifact if artifact is None else artifact, tag_sha)

    def test_only_publication_failure_after_successful_build_is_accepted(self):
        self.verify()

    def test_wrong_source_workflow_repository_or_tag_commit_is_rejected(self):
        changes = {
            "id": 124, "head_sha": OTHER_SHA, "repository": {"full_name": "foreign/repo"},
            "head_repository": {"full_name": "fork/repo"}, "path": ".github/workflows/other.yml",
            "event": "push", "head_branch": "feature", "status": "in_progress",
            "conclusion": "success",
        }
        for field, value in changes.items():
            run = deepcopy(self.run)
            run[field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "Quelllauf"):
                self.verify(run=run)
        for tag_sha in (None, OTHER_SHA):
            with self.subTest(tag_sha=tag_sha), self.assertRaisesRegex(ValueError, "Release-Tag"):
                self.verify(tag_sha=tag_sha)

    def test_failed_skipped_missing_or_reordered_build_checks_are_rejected(self):
        for state in ("failure", "skipped", "cancelled", None):
            jobs = deepcopy(self.jobs)
            jobs["jobs"][0]["steps"][0]["conclusion"] = state
            with self.subTest(state=state), self.assertRaisesRegex(ValueError, "Paketprüfungen"):
                self.verify(jobs=jobs)
        for mutation in ("missing", "reordered", "additional_failure", "artifact_failed", "publication_skipped"):
            jobs = deepcopy(self.jobs)
            steps = jobs["jobs"][0]["steps"]
            if mutation == "missing":
                del steps[0]
            elif mutation == "reordered":
                steps[0], steps[1] = steps[1], steps[0]
            elif mutation == "additional_failure":
                steps.append({"name": "Andere Prüfung", "conclusion": "failure"})
            elif mutation == "artifact_failed":
                steps[-1]["conclusion"] = "failure"
            else:
                steps[-2]["conclusion"] = "skipped"
            with self.subTest(mutation=mutation), self.assertRaisesRegex(ValueError, "Paketprüfungen"):
                self.verify(jobs=jobs)

    def test_wrong_job_inventory_is_rejected(self):
        for jobs in ({"total_count": 2, "jobs": self.jobs["jobs"]},
                     {"total_count": 1, "jobs": []},
                     {"total_count": 1, "jobs": self.jobs["jobs"] * 2}):
            with self.subTest(jobs=jobs), self.assertRaisesRegex(ValueError, "Jobbestand"):
                self.verify(jobs=jobs)
        jobs = deepcopy(self.jobs)
        jobs["jobs"][0]["name"] = "other-job"
        with self.assertRaisesRegex(ValueError, "Paketprüfungen"):
            self.verify(jobs=jobs)

    def test_expired_changed_or_foreign_artifact_is_rejected(self):
        changes = {
            "id": 457, "name": "unrelated", "expired": True,
            "digest": "sha256:" + "d" * 64, "size_in_bytes": 1001,
            "workflow_run": {"id": 124, "head_sha": SHA},
        }
        for field, value in changes.items():
            artifact = deepcopy(self.artifact)
            artifact[field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "Artefakt"):
                self.verify(artifact=artifact)
        for run in ({"id": 123, "head_sha": OTHER_SHA}, {}):
            artifact = {**self.artifact, "workflow_run": run}
            with self.subTest(run=run), self.assertRaisesRegex(ValueError, "Artefakt"):
                self.verify(artifact=artifact)
        artifact = {**self.artifact, "expired": "false"}
        with self.assertRaises(ValueError):
            self.verify(artifact=artifact)

    def test_inspect_uses_exact_read_only_endpoints_and_verified_outputs(self):
        responses = {
            "actions/runs/123": self.run,
            "actions/runs/123/jobs?per_page=100": self.jobs,
            "actions/artifacts/456": self.artifact,
        }
        output = self.root / "github-output"
        output.write_text("previous=value\n")
        printed = io.StringIO()
        with patch.object(RESUME, "api", side_effect=lambda repo, resource: responses[resource]) as api, \
                patch.object(RESUME.PUBLISH, "tag_commit", return_value=SHA) as tag, \
                patch.dict(os.environ, {"GITHUB_OUTPUT": str(output)}), redirect_stdout(printed):
            RESUME.inspect(self.config)
        self.assertEqual([call.args for call in api.call_args_list],
                         [("owner/repo", resource) for resource in responses])
        tag.assert_called_once_with("owner/repo", TAG)
        self.assertEqual(json.loads(printed.getvalue()), {"sha": SHA, "artifact_id": 456, "run_id": 123})
        self.assertEqual(output.read_text(), f"previous=value\nsha={SHA}\nartifact_id=456\nrun_id=123\n")

        with patch.object(RESUME, "api", side_effect=lambda repo, resource: responses[resource]), \
                patch.object(RESUME.PUBLISH, "tag_commit", return_value=OTHER_SHA), \
                patch.dict(os.environ, {"GITHUB_OUTPUT": str(output)}), self.assertRaises(ValueError):
            RESUME.inspect(self.config)
        self.assertEqual(output.read_text(), f"previous=value\nsha={SHA}\nartifact_id=456\nrun_id=123\n")


class RestoreTests(OfflineTest):
    def setUp(self):
        super().setUp()
        self.source, self.artifact, self.staging = (self.root / name for name in ("source", "saved", "staging"))
        (self.source / ".claude-plugin").mkdir(parents=True)
        (self.source / ".claude-plugin/marketplace.json").write_text(json.dumps({"version": TAG[1:]}))
        (self.source / "scripts").mkdir()
        self.slugs = ("alpha-case", "beta-case", "gamma-case")
        (self.source / "scripts/release-routes.json").write_text(json.dumps({
            "schema_version": 1, "companion_case_slugs": self.slugs,
        }))
        limit = patch.object(RESUME.R, "MAX_RELEASE_ASSETS", 5)
        limit.start()
        self.addCleanup(limit.stop)
        self.files = {"plugin.zip": b"installierbares Paket", "notes.md": b"Freigabevermerk\n",
                      "marketplace.json": json.dumps({"version": TAG[1:]}).encode()}
        for slug in self.slugs:
            for suffix in ("", "-einzelpdfs"):
                self.files[f"testakte-{slug}{suffix}.zip"] = f"Paket {slug}{suffix}".encode()
        for name, data in self.files.items():
            path = self.artifact / "dist" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        self.groups = {
            RESUME.R.companion_stage(n): RESUME.R.companion_asset_names(slugs)
            for n, slugs in enumerate(RESUME.R.companion_case_groups(self.slugs), 1)
        }
        self.groups["main"] = set(self.files) - set().union(*self.groups.values())
        self.config = {"source_commit": SHA, "tag": TAG, "checksums": {},
                       "dist_hashed_assets": len(self.files),
                       "group_assets_including_checksums": {group: len(names) + 1 for group, names in self.groups.items()}}
        self.save_manifest("dist/checksums-sha256.txt", self.files)
        for group, names in self.groups.items():
            self.save_manifest(f"release-staging/{group}/checksums-sha256.txt", names)
        self.original_manifests = {name: (self.artifact / name).read_bytes() for name in self.config["checksums"]}

    def save_manifest(self, relative, names):
        path = self.artifact / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("".join(f"{hashlib.sha256(self.files[name]).hexdigest()}  {name}\n" for name in sorted(names)))
        self.record_manifest(relative)

    def record_manifest(self, relative):
        raw = (self.artifact / relative).read_bytes()
        self.config["checksums"][relative] = {"size": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}

    def restore(self, sha=SHA):
        with patch.object(RESUME.subprocess, "check_output", return_value=sha + "\n") as git, redirect_stdout(io.StringIO()):
            RESUME.restore(self.config, self.artifact, self.source, self.staging)
        git.assert_called_once_with(["git", "-C", str(self.source), "rev-parse", "HEAD"], text=True)

    def assert_rejected_before_staging(self, message):
        with self.assertRaisesRegex(ValueError, message):
            self.restore()
        self.assertFalse(self.staging.exists())

    def test_success_preserves_every_package_checksum_and_hardlink(self):
        self.restore()
        self.assertEqual({path.name for path in self.staging.iterdir()}, set(self.groups))
        for relative, original in self.original_manifests.items():
            self.assertEqual((self.artifact / relative).read_bytes(), original)
        for group, names in self.groups.items():
            directory = self.staging / group
            self.assertEqual({path.name for path in directory.iterdir()}, names | {"checksums-sha256.txt"})
            self.assertEqual((directory / "checksums-sha256.txt").read_bytes(),
                             self.original_manifests[f"release-staging/{group}/checksums-sha256.txt"])
            for name in names:
                original, restored = self.artifact / "dist" / name, directory / name
                self.assertEqual(restored.read_bytes(), self.files[name])
                self.assertEqual((restored.stat().st_dev, restored.stat().st_ino),
                                 (original.stat().st_dev, original.stat().st_ino))
            self.assertEqual(set(RESUME.expected_asset_metadata(directory)), names | {"checksums-sha256.txt"})

    def test_wrong_checkout_sha_or_marketplace_version_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Quellcheckout"):
            self.restore(OTHER_SHA)
        self.assertFalse(self.staging.exists())
        (self.source / ".claude-plugin/marketplace.json").write_text('{"version":"1.0.0"}')
        self.assert_rejected_before_staging("Quellcheckout")

    def test_changed_package_bytes_are_rejected_even_with_original_length(self):
        path = self.artifact / "dist/plugin.zip"
        path.write_bytes(b"X" * len(self.files["plugin.zip"]))
        self.assert_rejected_before_staging("Paketbytes verändert")

    def test_changed_saved_checksum_manifest_is_rejected(self):
        path = self.artifact / "release-staging/companion/checksums-sha256.txt"
        path.write_bytes(path.read_bytes().replace(b"a", b"b", 1))
        self.assert_rejected_before_staging("Prüfsummenliste verändert")

    def test_missing_package_is_rejected(self):
        (self.artifact / "dist/testakte-alpha-case.zip").unlink()
        self.assert_rejected_before_staging("fehlende, fremde oder verknüpfte Dateien")

    def test_foreign_extra_file_is_rejected(self):
        (self.artifact / "unrelated.txt").write_text("fremd")
        self.assert_rejected_before_staging("fehlende, fremde oder verknüpfte Dateien")

    def test_symlink_package_is_rejected_even_with_correct_bytes(self):
        path = self.artifact / "dist/plugin.zip"
        outside = self.root / "same-package.zip"
        outside.write_bytes(path.read_bytes())
        path.unlink()
        path.symlink_to(outside)
        self.assert_rejected_before_staging("fehlende, fremde oder verknüpfte Dateien")

    def test_symlink_manifest_or_directory_is_rejected(self):
        path = self.artifact / "dist/checksums-sha256.txt"
        outside = self.root / "same-checksums.txt"
        outside.write_bytes(path.read_bytes())
        path.unlink()
        path.symlink_to(outside)
        self.assert_rejected_before_staging("Prüfsummenliste verändert")
        path.unlink()
        path.write_bytes(outside.read_bytes())
        (self.artifact / "linked-directory").symlink_to(self.source, target_is_directory=True)
        self.assert_rejected_before_staging("fehlende, fremde oder verknüpfte Dateien")

    def test_wrong_dist_inventory_count_is_rejected(self):
        self.config["dist_hashed_assets"] += 1
        self.assert_rejected_before_staging("Unvollständiger Gesamtbestand")

    def test_wrong_group_names_counts_or_asset_assignment_are_rejected(self):
        self.config["group_assets_including_checksums"]["unexpected"] = 1
        self.assert_rejected_before_staging("Releaseaufteilung")
        del self.config["group_assets_including_checksums"]["unexpected"]
        self.config["group_assets_including_checksums"]["main"] += 1
        self.assert_rejected_before_staging("abweichende Gruppe")
        self.config["group_assets_including_checksums"]["main"] -= 1
        main, companion = set(self.groups["main"]), set(self.groups["companion"])
        main.remove("plugin.zip")
        moved = sorted(companion)[0]
        companion.remove(moved)
        main.add(moved)
        companion.add("plugin.zip")
        self.save_manifest("release-staging/main/checksums-sha256.txt", main)
        self.save_manifest("release-staging/companion/checksums-sha256.txt", companion)
        self.assert_rejected_before_staging("abweichende Gruppe")

    def test_group_digest_must_match_original_dist_manifest(self):
        relative = "release-staging/main/checksums-sha256.txt"
        path = self.artifact / relative
        raw = path.read_text()
        path.write_text("0" * 64 + raw[64:])
        self.record_manifest(relative)
        self.assert_rejected_before_staging("abweichende Gruppe")

    def test_existing_staging_is_not_overwritten(self):
        self.staging.mkdir()
        sentinel = self.staging / "keep.txt"
        sentinel.write_text("bestehender Stand")
        with self.assertRaises(FileExistsError):
            self.restore()
        self.assertEqual(sentinel.read_text(), "bestehender Stand")
        self.assertEqual(list(self.staging.iterdir()), [sentinel])


if __name__ == "__main__":
    unittest.main()
