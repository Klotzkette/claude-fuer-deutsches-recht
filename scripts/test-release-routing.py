#!/usr/bin/env python3
"""Offline regressions for routing, staging and two-release publication."""

from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from contextlib import redirect_stdout, redirect_stderr
from functools import partial
from pathlib import Path
from unittest.mock import patch

from release_asset_common import expected_asset_metadata, read_checksums, sha256_file, write_checksums
import release_routing as R
from testakte_download_notices import ensure_download_notices, missing_notice_positions

SCRIPTS = Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


STAGE = load("stage-release-assets")
PUBLISH = load("publish-release-assets")
UPLOAD = load("upload-release-assets")
CASES = load("inject-gesamt-pdf-section")
PLUGINS = load("inject-direkt-loslegen-section")
INDEX = load("generate-asset-index")
CATALOG = load("generate-root-plugin-catalog")
DOWNLOADS = load("validate-testakten-readme-downloads")
SHA = "a" * 40
VERSION = "777.2.3"
TAG = f"akten-v{VERSION}"
FIXTURE_CASES = ("fixture-alpha", "fixture-beta", "fixture-gamma", "fixture-delta")
FIXTURE_ASSET_NAMES = {
    "testakte-fixture-alpha.zip", "testakte-fixture-alpha-einzelpdfs.zip",
    "testakte-fixture-beta.zip", "testakte-fixture-beta-einzelpdfs.zip",
    "testakte-fixture-gamma.zip", "testakte-fixture-gamma-einzelpdfs.zip",
    "testakte-fixture-delta.zip", "testakte-fixture-delta-einzelpdfs.zip",
}


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="release-routing-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / ".claude-plugin").mkdir()
        (self.root / ".claude-plugin/marketplace.json").write_text(
            json.dumps({"version": VERSION, "plugins": []}), encoding="utf-8",
        )
        self.dist = self.root / "dist"
        self.dist.mkdir()
        self.staging = self.root / "staging"
        # Verhaltens- und Grenztests bleiben von produktiven Erweiterungen unabhängig.
        self.config = self.root / "fixture-routes.json"
        self.config.write_text(json.dumps({"schema_version": 1, "companion_case_slugs": FIXTURE_CASES}))
        self.slugs = R.companion_cases(self.config)
        self.names = set(FIXTURE_ASSET_NAMES)
        self.empty_config = self.root / "no-routes.json"
        self.empty_config.write_text(json.dumps({"schema_version": 1, "companion_case_slugs": []}))

    def build(self, ordinary=1):
        for name in self.names:
            with zipfile.ZipFile(self.dist / name, "w") as archive:
                archive.writestr("README.txt", "fixture")
        for name in ("alle-testakten.zip", "alle-testakten-einzelpdfs.zip", "alles-komplettpaket.zip"):
            with zipfile.ZipFile(self.dist / name, "w") as archive:
                for asset in sorted(self.names):
                    if name == "alle-testakten.zip" and asset.endswith("-einzelpdfs.zip"):
                        continue
                    if name == "alle-testakten-einzelpdfs.zip" and not asset.endswith("-einzelpdfs.zip"):
                        continue
                    prefix = "testakten/" if name == "alles-komplettpaket.zip" else ""
                    archive.write(self.dist / asset, prefix + asset)
        for i in range(ordinary):
            (self.dist / f"existing-{i}.zip").write_bytes(b"existing")
        write_checksums(self.dist)


class RepositoryRoutingTests(unittest.TestCase):
    def test_expected_twelve_cases_and_twenty_four_zips(self):
        expected = {
            "ki-hochrisiko-bewerbungsauswahl-kassel", "ki-transparenz-kanzlei-kommunikation-mainz",
            "vergesellschaftung-energienetz-hessen", "enteignung-verkehrsflaeche-goettingen",
            "sozialversicherung-ag-organe-hannover",
            "sozialversicherung-gmbh-fuenfzig-prozent-erfurt",
            "sozialversicherung-gmbh-zwanzig-prozent-berlin",
            "sozialversicherung-musikakademie-prenzlauer-berg",
            "sozialversicherung-programmierer-leipzig",
            "sozialversicherung-syndikus-versorgungswerk-hamburg",
            "statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen",
            "gesellschaftsgruender-topf-tacheles-berlin",
        }
        slugs = R.companion_cases()
        self.assertEqual(set(slugs), expected)
        self.assertEqual(len(R.companion_asset_names(slugs)), 24)
        for slug in sorted(expected):
            for suffix in ("", "-einzelpdfs"):
                with self.subTest(slug=slug, suffix=suffix):
                    self.assertEqual(R.case_asset_url(slug, suffix, version=VERSION),
                                     f"{R.RELEASE_BASE}/download/{TAG}/testakte-{slug}{suffix}.zip")


class RoutingTests(Fixture):
    def setUp(self):
        super().setUp()
        # Die Generatoren importieren eigene Aliase; die echten Helfer lesen die Fixture.
        for module, helpers in (
            (CASES, ("case_asset_url", "companion_cases", "rewrite_case_asset_urls")),
            (PLUGINS, ("case_asset_url", "rewrite_case_asset_urls")),
            (INDEX, ("case_asset_url", "companion_cases")),
            (CATALOG, ("rewrite_case_asset_urls",)),
            (DOWNLOADS, ("case_asset_url", "rewrite_case_asset_urls")),
        ):
            for name in helpers:
                routing = patch.object(module, name, partial(getattr(R, name), config=self.config))
                routing.start()
                self.addCleanup(routing.stop)

    def test_four_case_fixture_has_both_zip_variants(self):
        self.assertEqual(self.slugs, FIXTURE_CASES)
        self.assertEqual(R.companion_asset_names(self.slugs), FIXTURE_ASSET_NAMES)
        self.assertFalse(TAG.startswith("v"))

    def test_urls_follow_marketplace_not_a_hardcoded_version(self):
        for slug in self.slugs:
            for suffix in ("", "-einzelpdfs"):
                self.assertEqual(R.case_asset_url(slug, suffix, root=self.root, config=self.config),
                                 f"{R.RELEASE_BASE}/download/{TAG}/testakte-{slug}{suffix}.zip")
        self.assertIn("/latest/download/", R.case_asset_url("old-case", root=self.root, config=self.config))
        self.assertIn("/latest/download/", R.case_asset_url(self.slugs[0], config=self.empty_config))

    def test_placeholders_and_older_pins_rewritten_but_existing_links_unchanged(self):
        for route in ("latest/download", "download/akten-v1.2.3", "download/v1.2.3"):
            source = "\n".join(f"[ZIP]({R.RELEASE_BASE}/{route}/{name})" for name in sorted(self.names))
            unchanged = f"\n[other]({R.RELEASE_BASE}/latest/download/testakte-old-case.zip)"
            expected = "\n".join(f"[ZIP]({R.RELEASE_BASE}/download/{TAG}/{name})" for name in sorted(self.names))
            result = R.rewrite_case_asset_urls(source + unchanged, root=self.root, config=self.config)
            self.assertEqual(result, expected + unchanged)
            self.assertEqual(R.rewrite_case_asset_urls(result, root=self.root, config=self.config), result)
        self.assertEqual(R.rewrite_case_asset_urls(source, config=self.empty_config), source)

    def test_invalid_versions_and_config_fail_closed(self):
        for value in ("v1.2.3", "1.2", "../x", "1.2.3\n", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                R.companion_tag(value)
        for slugs in (["../case"], ["case", "case"], "case"):
            self.empty_config.write_text(json.dumps({"schema_version": 1, "companion_case_slugs": slugs}))
            with self.assertRaises(ValueError):
                R.companion_cases(self.empty_config)

    def test_case_generator_rewrites_entire_readme_and_is_idempotent(self):
        slug = self.slugs[0]
        directory = self.root / "testakten" / slug
        (directory / "gesamt-pdf").mkdir(parents=True)
        (directory / "gesamt-pdf" / f"{slug}_gesamt.pdf").write_bytes(b"fixture")
        readme = directory / "README.md"
        readme.write_text(f"# Case\n\n[Legacy placeholder]({R.RELEASE_BASE}/latest/download/testakte-{slug}.zip)\n")
        with patch.object(CASES, "REPO_ROOT", self.root), patch.object(CASES, "expected_arcnames", return_value=["doc.pdf"]):
            self.assertEqual(CASES.inject(readme, slug), "inserted")
            text = readme.read_text()
            self.assertNotIn("/latest/download/", text)
            self.assertIn(f"/download/{TAG}/", text)
            self.assertNotIn("ZIP links refer to the latest", text)
            self.assertEqual(missing_notice_positions(text, case_readme=True), [])
            self.assertEqual(CASES.inject(readme, slug), "unchanged")

    def test_plugin_case_links_and_asset_index_use_routes(self):
        slug = self.slugs[0]
        with patch.object(PLUGINS, "REPO", self.root), patch.object(PLUGINS, "TESTAKTEN_DIR", self.root / "testakten"), \
                patch.object(PLUGINS, "get_akte_title", return_value="Case"):
            text = PLUGINS.testakten_section("plugin", self.root / "plugin", [slug])
        self.assertEqual(text.count(f"/download/{TAG}/"), 2)
        section = ensure_download_notices("\n".join(INDEX.companion_section(VERSION)))
        self.assertEqual(missing_notice_positions(section), [])
        for name in self.names:
            self.assertIn(f"/download/{TAG}/{name}", section)
        self.assertIn(f"/download/{TAG}/checksums-sha256.txt", section)
        with patch.object(INDEX, "companion_cases", return_value=()):
            self.assertEqual(INDEX.companion_section(VERSION), [])

    def test_root_catalog_regeneration_resolves_placeholders_in_both_catalogues(self):
        placeholder = f"[ZIP]({R.RELEASE_BASE}/latest/download/testakte-{self.slugs[0]}.zip)"
        readme, overview = self.root / "README.md", self.root / "cases.md"
        readme.write_text(placeholder)
        overview.write_text(f"Stand v1.0.0: 1 zentrale Testakten.\n{placeholder}")
        marketplace = self.root / ".claude-plugin/marketplace.json"
        marketplace.write_text(json.dumps({"version": VERSION, "plugins": [{"name": "p", "version": VERSION}]}))
        with patch.multiple(CATALOG, MARKETPLACE=marketplace, README=readme, TESTAKTEN_README=overview), \
                patch.object(CATALOG, "build_directory", return_value=""), patch.object(CATALOG, "build_catalog", return_value=""), \
                patch.object(CATALOG, "replace_directory", side_effect=lambda text, _: text), \
                patch.object(CATALOG, "replace_catalog", side_effect=lambda text, _: text), \
                patch.object(CATALOG, "inventory_counts", return_value={"skills": 0, "central_testakten": 4}), \
                patch.object(CATALOG, "update_summary_counts", side_effect=lambda text, _: text), redirect_stdout(io.StringIO()):
            CATALOG.main()
        for page in (readme, overview):
            self.assertIn(f"/download/{TAG}/", page.read_text())
            self.assertNotIn("latest/download", page.read_text())

    def test_validator_rejects_placeholder_even_beside_correct_link(self):
        with patch.object(DOWNLOADS, "ROOT", self.root):
            correct = DOWNLOADS.release_url(self.slugs[0])
            self.assertIn(f"/download/{TAG}/", correct)
            for wrong in (correct.replace(f"download/{TAG}", "latest/download"), correct.replace(TAG, "akten-v1.0.0")):
                errors = []
                DOWNLOADS.validate_release_routes("README", correct + "\n" + wrong, errors)
                self.assertEqual(len(errors), 1)
                self.assertIn("README:2:", errors[0])


class StagingTests(Fixture):
    def test_1003_assets_split_into_995_and_9_with_complete_aggregates(self):
        self.build(ordinary=991)
        before = {path.name: sha256_file(path) for path in self.dist.iterdir()}
        self.assertEqual(len(before), 1003)
        self.assertEqual(STAGE.stage_assets(self.dist, self.staging, self.slugs), {"main": 995, "companion": 9})
        main, companion = (expected_asset_metadata(self.staging / name) for name in ("main", "companion"))
        self.assertEqual(set(main) & set(companion), {"checksums-sha256.txt"})
        self.assertEqual(set(companion) - {"checksums-sha256.txt"}, self.names)
        self.assertFalse(self.names & read_checksums(self.staging / "main/checksums-sha256.txt").keys())
        self.assertEqual(set(main) | set(companion), set(before))
        self.assertEqual(before, {path.name: sha256_file(path) for path in self.dist.iterdir()})
        for name in ("alle-testakten.zip", "alle-testakten-einzelpdfs.zip", "alles-komplettpaket.zip"):
            with zipfile.ZipFile(self.staging / "main" / name) as archive:
                if name == "alles-komplettpaket.zip":
                    expected = {"testakten/" + asset for asset in self.names}
                else:
                    expected = {asset for asset in self.names if asset.endswith("-einzelpdfs.zip") == (name == "alle-testakten-einzelpdfs.zip")}
                self.assertEqual(expected, set(archive.namelist()))

    def test_incomplete_aggregates_are_rejected_before_partition(self):
        for index, name in enumerate(("alle-testakten.zip", "alle-testakten-einzelpdfs.zip", "alles-komplettpaket.zip")):
            self.build()
            with zipfile.ZipFile(self.dist / name, "w") as archive:
                archive.writestr("README.txt", "incomplete")
            target = self.root / f"incomplete-{index}"
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, "Incomplete aggregate"):
                STAGE.stage_assets(self.dist, target, self.slugs)
            self.assertFalse(target.exists())

    def test_empty_configuration_preserves_all_assets(self):
        self.build()
        original = expected_asset_metadata(self.dist)
        STAGE.stage_assets(self.dist, self.staging, ())
        self.assertEqual(expected_asset_metadata(self.staging / "main"), original)
        self.assertFalse((self.staging / "companion").exists())

    def test_main_limit_includes_checksum_and_fails_before_writing(self):
        self.build(ordinary=996)
        self.assertEqual(STAGE.stage_assets(self.dist, self.staging, self.slugs)["main"], 1000)
        (self.dist / "one-more.zip").write_bytes(b"extra")
        target = self.root / "over-limit"
        with self.assertRaisesRegex(ValueError, "1001 assets"):
            STAGE.stage_assets(self.dist, target, self.slugs)
        self.assertFalse(target.exists())
        with self.assertRaisesRegex(ValueError, "GitHub limit"):
            expected_asset_metadata(self.dist)

    def test_companion_limit_includes_own_checksum(self):
        slugs = tuple(f"case-{i}" for i in range(500))
        for name in R.companion_asset_names(slugs) | {"plugin.zip"}:
            (self.dist / name).write_bytes(b"fixture")
        with self.assertRaisesRegex(ValueError, "1001 assets"):
            STAGE.stage_assets(self.dist, self.staging, slugs)
        self.assertFalse(self.staging.exists())

    def test_missing_pair_and_nested_or_existing_stage_fail_without_deletion(self):
        self.build()
        (self.dist / next(iter(self.names))).unlink()
        with self.assertRaisesRegex(ValueError, "missing"):
            STAGE.stage_assets(self.dist, self.staging, self.slugs)
        self.assertFalse(self.staging.exists())
        for target in (self.dist, self.dist / "staging", self.root):
            with self.assertRaises(ValueError):
                STAGE.stage_assets(self.dist, target, ())
        self.staging.mkdir()
        sentinel = self.staging / "keep.txt"
        sentinel.write_text("keep")
        with self.assertRaises(ValueError):
            STAGE.stage_assets(self.dist, self.staging, ())
        self.assertEqual(sentinel.read_text(), "keep")


class FakeGitHub:
    def __init__(self):
        self.refs = {f"v{VERSION}": {"type": "tag", "sha": "b" * 40}}
        self.objects = {"b" * 40: {"type": "tag", "sha": "c" * 40}, "c" * 40: {"type": "commit", "sha": SHA}}
        self.releases = {}
        self.commands = []
        self.head = SHA

    def run(self, command):
        self.commands.append(command)
        def response(value=None, code=0, error=""):
            return subprocess.CompletedProcess(command, code, json.dumps(value) if value is not None else "", error)
        if command[0] == "git":
            return subprocess.CompletedProcess(command, 0, self.head + "\n", "")
        if command[:2] == ["gh", "api"]:
            resource = command[2]
            if "/git/ref/tags/" in resource:
                obj = self.refs.get(resource.split("/git/ref/tags/")[1])
                return response({"object": obj}) if obj else response(code=1, error="gh: Not Found (HTTP 404)")
            if "/git/tags/" in resource:
                return response({"object": self.objects[resource.rsplit("/", 1)[1]]})
            if resource.endswith("/git/refs"):
                tag = next(arg.removeprefix("ref=refs/tags/") for arg in command if arg.startswith("ref="))
                sha = next(arg.removeprefix("sha=") for arg in command if arg.startswith("sha="))
                self.refs[tag] = {"type": "commit", "sha": sha}
                return response({"ref": tag})
        if command[:3] == ["gh", "release", "view"]:
            release = self.releases.get(command[3])
            return response(release) if release else response(code=1, error="release not found")
        if command[:3] == ["gh", "release", "create"]:
            self.releases[command[3]] = {"tagName": command[3], "isDraft": True, "databaseId": 7}
            return response()
        raise AssertionError(f"Unexpected command: {command}")


class PublicationTests(Fixture):
    def setUp(self):
        super().setUp()
        self.build()
        STAGE.stage_assets(self.dist, self.staging, self.slugs)
        self.gh = FakeGitHub()
        runner = patch.object(PUBLISH, "run", side_effect=self.gh.run)
        runner.start()
        self.addCleanup(runner.stop)
        executor = patch.object(PUBLISH, "execute")
        self.execute = executor.start()
        self.addCleanup(executor.stop)

    def publish(self, **kwargs):
        PUBLISH.publish(self.staging, f"v{VERSION}", "owner/repo", root=self.root, config=self.config, **kwargs)

    def test_annotated_parent_exact_sha_never_latest_and_publish_order(self):
        self.publish()
        create = next(cmd for cmd in self.gh.commands if cmd[:3] == ["gh", "release", "create"])
        self.assertEqual(create[create.index("--target") + 1], SHA)
        for flag in ("--draft", "--latest=false", "--verify-tag"):
            self.assertIn(flag, create)
        notes = create[create.index("--notes") + 1]
        self.assertIn("vollständig", notes)
        self.assertIn("für", notes)
        post = next(cmd for cmd in self.gh.commands if "POST" in cmd)
        self.assertIn(f"ref=refs/tags/{TAG}", post)
        self.assertIn(f"sha={SHA}", post)
        commands = [call.args[0] for call in self.execute.call_args_list]
        self.assertEqual([Path(cmd[1]).name if cmd[0] == sys.executable else cmd[2] for cmd in commands],
                         ["upload-release-assets.py"] * 2 + ["validate-release-assets.py"] * 2 + ["edit"] * 2)
        self.assertIn("--require-existing", commands[1])
        self.assertEqual(commands[-2][3], TAG)
        self.assertIn("--latest=false", commands[-2])
        self.assertEqual(commands[-1][3], f"v{VERSION}")
        self.assertNotIn("--latest=false", commands[-1])
        self.assertNotIn("--force", sum(self.gh.commands + commands, []))
        self.assertNotIn("DELETE", sum(self.gh.commands + commands, []))

    def test_existing_published_companion_is_reusable_without_recreation(self):
        self.gh.refs[TAG] = {"type": "commit", "sha": SHA}
        self.gh.releases[TAG] = {"tagName": TAG, "isDraft": False, "databaseId": 7}
        self.publish()
        self.assertFalse(any("POST" in cmd or "create" in cmd for cmd in self.gh.commands))

    def test_lost_creation_responses_reuse_exact_ref_and_draft(self):
        def lost_response(command):
            result = self.gh.run(command)
            if "POST" in command or command[:3] == ["gh", "release", "create"]:
                return subprocess.CompletedProcess(command, 1, "", "lost response")
            return result
        with patch.object(PUBLISH, "run", side_effect=lost_response):
            self.publish()
        self.assertEqual(self.execute.call_count, 6)

    def test_ensure_existing_companion_retry_does_not_change_latest(self):
        self.gh.refs[TAG] = {"type": "commit", "sha": SHA}
        for draft in (True, False):
            self.gh.releases[TAG] = {"tagName": TAG, "isDraft": draft, "databaseId": 7}
            self.gh.commands.clear()
            PUBLISH.ensure_companion("owner/repo", TAG, f"v{VERSION}", SHA)
            self.assertTrue(all(
                (cmd[:2] == ["gh", "api"] and len(cmd) == 3) or cmd[:3] == ["gh", "release", "view"]
                for cmd in self.gh.commands
            ))
            self.execute.assert_not_called()

    def test_release_lookup_failure_is_not_permission_to_create(self):
        self.gh.refs[TAG] = {"type": "commit", "sha": SHA}
        for message in ("HTTP 403", "network failure", "invalid authentication"):
            def failed_view(command):
                if command[:3] == ["gh", "release", "view"]:
                    return subprocess.CompletedProcess(command, 1, "", message)
                return self.gh.run(command)
            with patch.object(PUBLISH, "run", side_effect=failed_view), self.assertRaises(RuntimeError):
                self.publish()
        self.assertFalse(any("create" in cmd for cmd in self.gh.commands))
        self.execute.assert_not_called()

    def test_mismatching_companion_is_not_overwritten(self):
        self.gh.refs[TAG] = {"type": "commit", "sha": "d" * 40}
        with self.assertRaisesRegex(ValueError, "not changed"):
            self.publish()
        self.assertFalse(any("POST" in cmd or "create" in cmd for cmd in self.gh.commands))
        self.execute.assert_not_called()

    def test_wrong_checkout_or_primary_version_stops_before_remote_writes(self):
        self.gh.head = "e" * 40
        with self.assertRaisesRegex(ValueError, "checkout"):
            self.publish()
        with self.assertRaisesRegex(ValueError, "marketplace version"):
            PUBLISH.publish(self.staging, "v1.2.3", "owner/repo", root=self.root, config=self.config)
        self.assertFalse(any("POST" in cmd or "create" in cmd for cmd in self.gh.commands))
        self.execute.assert_not_called()

    def test_every_upload_or_verification_failure_blocks_publication(self):
        for failing in range(4):
            self.execute.reset_mock()
            count = 0
            def fail(command):
                nonlocal count
                count += 1
                if count == failing + 1:
                    raise subprocess.CalledProcessError(1, command)
            self.execute.side_effect = fail
            with self.subTest(failing=failing), self.assertRaises(subprocess.CalledProcessError):
                self.publish()
            self.assertFalse(any(call.args[0][:3] == ["gh", "release", "edit"] for call in self.execute.call_args_list))

    def test_failed_companion_publication_keeps_main_unpublished(self):
        def fail(command):
            if command[:4] == ["gh", "release", "edit", TAG]:
                raise subprocess.CalledProcessError(1, command)
        self.execute.side_effect = fail
        with self.assertRaises(subprocess.CalledProcessError):
            self.publish()
        self.assertEqual(self.execute.call_count, 5)
        self.assertFalse(any(call.args[0][:4] == ["gh", "release", "edit", f"v{VERSION}"] for call in self.execute.call_args_list))

    def test_tag_moved_after_verification_blocks_both_publications(self):
        def move(command):
            if "validate-release-assets.py" in command[1] and command[3] == TAG:
                self.gh.refs[TAG] = {"type": "commit", "sha": "e" * 40}
        self.execute.side_effect = move
        with self.assertRaisesRegex(ValueError, "moved"):
            self.publish()
        self.assertEqual(self.execute.call_count, 4)

    def test_auth_failure_is_not_treated_as_missing_tag(self):
        with patch.object(PUBLISH, "run", return_value=subprocess.CompletedProcess([], 1, "", "HTTP 403")):
            with self.assertRaises(RuntimeError):
                PUBLISH.ensure_companion("owner/repo", TAG, f"v{VERSION}", SHA)

    def test_malformed_stages_fail_before_remote_calls(self):
        (self.staging / "companion" / "unexpected.zip").write_bytes(b"wrong")
        write_checksums(self.staging / "companion")
        with self.assertRaisesRegex(ValueError, "configured release routes"):
            self.publish()
        self.assertEqual(self.gh.commands, [])
        self.execute.assert_not_called()

    def test_no_companion_configuration_keeps_old_publisher_sequence(self):
        stage = self.root / "ordinary-staging"
        STAGE.stage_assets(self.dist, stage, ())
        PUBLISH.publish(stage, "v1.2.3", "owner/repo", root=self.root, config=self.empty_config)
        self.assertEqual(self.gh.commands, [])
        commands = [call.args[0] for call in self.execute.call_args_list]
        self.assertEqual(len(commands), 3)
        self.assertNotIn("--protect-published", commands[0])
        self.assertNotIn("--require-existing", commands[0])
        self.assertEqual(commands[-1], ["gh", "release", "edit", "v1.2.3", "--draft=false", "--repo", "owner/repo"])

    def test_uploader_protects_published_assets_and_requires_existing_companion(self):
        argv = ["upload", str(self.staging / "companion"), TAG, "--repo", "owner/repo", "--require-existing", "--protect-published"]
        metadata = expected_asset_metadata(self.staging / "companion")
        remote = {name: {**entry, "state": "uploaded"} for name, entry in metadata.items()}
        with patch.object(sys, "argv", argv), patch.object(UPLOAD, "view_release") as view, \
                patch.object(UPLOAD, "ensure_release") as ensure, patch.object(UPLOAD, "fetch_remote_assets", return_value=remote), \
                patch.object(UPLOAD, "delete_asset") as delete, patch.object(UPLOAD, "upload_one") as upload, \
                redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            view.return_value = {"id": 1, "isDraft": False}
            self.assertEqual(UPLOAD.main(), 0)
            remote[next(iter(self.names))]["size"] += 1
            self.assertEqual(UPLOAD.main(), 1)
            view.return_value = None
            self.assertEqual(UPLOAD.main(), 1)
            ensure.assert_not_called()
            delete.assert_not_called()
            upload.assert_not_called()


class WorkflowTests(unittest.TestCase):
    def test_partition_after_complete_packaging_and_checkout_requested_tag(self):
        text = (SCRIPTS.parent / ".github/workflows/release-plugin-zips.yml").read_text()
        self.assertLess(text.index('test -s dist/alles-komplettpaket.zip'), text.index("scripts/stage-release-assets.py"))
        self.assertLess(text.index("scripts/stage-release-assets.py"), text.index("scripts/publish-release-assets.py"))
        self.assertIn("ref: ${{ github.event.inputs.tag || github.ref }}", text)
        self.assertIn("      - 'v*'", text)
        self.assertNotIn("      - 'akten-", text)
        self.assertLess(text.index("scripts/generate-root-plugin-catalog.py"), text.index("scripts/validate-testakten-readme-downloads.py"))


if __name__ == "__main__":
    unittest.main()
