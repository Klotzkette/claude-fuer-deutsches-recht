#!/usr/bin/env python3
"""Komponentenpakete, Archivtreue und Veröffentlichungsschranken der Qualitätsrunde."""
import copy
from contextlib import redirect_stdout
import io
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from release_asset_common import is_release_asset, read_checksums

spec = importlib.util.spec_from_file_location("quality_release", Path(__file__).with_name("build-skill-quality-release.py"))
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)


class QualityReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.root, self.dist = self.base / "repo", self.base / "dist"
        self.root.mkdir()
        self.name, self.version = "beispiel", "445.36.0"
        self.tag = "qualitaetsrunde-v445.36.0"
        self.source = "themen/beispiel"
        manifest = {"name": self.name, "version": self.version, "description": "Prüft den konkreten Vertragsauftrag."}
        for path in B.MANIFESTS:
            self.write(f"{self.source}/{path}", json.dumps(manifest))
        self.write(".claude-plugin/marketplace.json", json.dumps({"version": self.version, "plugins": [{"name": self.name, "version": self.version, "source": "./" + self.source}]}))
        self.write("scripts/scoped-release-assets.json", json.dumps({"schema_version": 1, "assets": {"beispiel.zip": self.tag, "beispiel-portable.zip": self.tag}}))
        self.write(f"{self.source}/skills/vertrag-pruefen/SKILL.md", "---\nname: vertrag-pruefen\ndescription: Vertrag prüfen\n---\n\n# Vertrag prüfen\n\n[Details](../alter-vertrag/FACHINHALT.md)\n")
        self.write(f"{self.source}/skills/alter-vertrag/FACHINHALT.md", "# Vollständiger alter Fachtext\n\n[Werkzeug](werkzeuge/rechnen.py)\n")
        self.write(f"{self.source}/skills/alter-vertrag/werkzeuge/rechnen.py", "print('Berechnung')\n")
        self.write(f"{self.source}/beispiel-werkstatt.md", "# Eigenständige Werkstatt\n")
        self.write(f"{self.source}/beispiel-werkstatt.txt", "# Eigenständige Werkstatt\n")
        self.write(f"{self.source}/testakte/downloads/testakte-alt.zip", "Bestand bleibt unberührt")
        self.write("LICENSE", "Lizenz\n")
        self.scope = {"schema_version": 1, "version": self.version, "tag": self.tag,
                      "plugins": [{"name": self.name, "variants": ["native", "portable"],
                                   "prompts": ["beispiel-werkstatt.md", "beispiel-werkstatt.txt"]}]}

    def write(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data.encode() if isinstance(data, str) else data)
        return path

    def build(self):
        return B.build(self.dist, self.scope, self.root)

    def test_paketpflege_binds_both_archives_and_retains_separate_prompts(self):
        tag = "paketpflege-20261122-v" + self.version
        plan = {"edition": "paketpflege-20261122", "gruppen": {
            self.version: {"vorgaenger": self.tag, "native": 1, "portable": 1}}, "unveraendert": []}
        self.write("scripts/data/paketpflege-20261122.json", json.dumps(plan))
        base_url = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/"
        self.write(f"{self.source}/assets/vorschau/index.html", f'<a href="{base_url}{self.tag}/beispiel.zip">ZIP</a>')
        self.write(f"{self.source}/werkzeuge/README.md", f"[Archiv]({base_url}{self.tag}/beispiel.zip) [Skill](../skills/vertrag-pruefen/SKILL.md)")
        scope = B.paketpflege_scope(tag, self.root)
        self.assertEqual(scope["plugins"][0]["variants"], ["native", "portable"])
        self.assertEqual(scope["plugins"][0]["prompts"], [])
        self.assertEqual(set(scope["plugins"][0]["preserved_prompts"]), {"beispiel-werkstatt.md", "beispiel-werkstatt.txt"})
        B.build(self.dist, scope, self.root)
        self.assertEqual(set(p.name for p in self.dist.iterdir()), {"beispiel.zip", "beispiel-portable.zip", B.REPORT, B.CHECKSUMS})
        with zipfile.ZipFile(self.dist / "beispiel.zip") as archive:
            for name in ("assets/vorschau/index.html", "werkzeuge/README.md"):
                self.assertIn(f"{base_url}{tag}/beispiel.zip", archive.read(name).decode())
                self.assertIn(f"{base_url}{self.tag}/beispiel.zip", (self.root / self.source / name).read_text())
        scope["plugins"][0]["variants"].remove("portable")
        with self.assertRaisesRegex(ValueError, "Paketnachauflage"):
            B.validate_scope(scope, self.root)
        self.write("scripts/scoped-release-assets.json", json.dumps({"schema_version": 1, "assets": {"beispiel.zip": self.tag}}))
        with self.assertRaisesRegex(ValueError, "Anzahl"):
            B.paketpflege_scope(tag, self.root)

    def test_activation_only_rewrites_published_live_targets(self):
        from package_edition import activate_routes
        from release_routing import RELEASE_BASE
        tag = "paketpflege-20261122-v" + self.version
        routes = {"beispiel.zip": (self.tag, tag)}
        before = f"[Paket]({RELEASE_BASE}/download/{self.tag}/beispiel.zip)"
        current = self.write("README.md", before)
        previous = self.write("docs/releases/fruehere-ausgabe.md", before)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        self.assertEqual(activate_routes(self.root, routes), 2)
        self.assertEqual(activate_routes(self.root, routes), 0)
        self.assertIn(tag, current.read_text())
        self.assertEqual(previous.read_text(), before)

    def test_native_portable_manifests_fachtext_and_tool_are_byte_exact(self):
        report = self.build()
        self.assertEqual(len(list(self.dist.iterdir())), 6)
        self.assertEqual(len(report["plugins"][self.name]["skills"]), 1)
        self.assertEqual(len(report["plugins"][self.name]["manifests"]), 3)
        with zipfile.ZipFile(self.dist / "beispiel.zip") as native, zipfile.ZipFile(self.dist / "beispiel-portable.zip") as portable:
            self.assertEqual(set(portable.namelist()), {"beispiel/" + n for n in native.namelist()})
            self.assertIn("skills/alter-vertrag/FACHINHALT.md", native.namelist())
            self.assertIn("skills/alter-vertrag/werkzeuge/rechnen.py", native.namelist())
            self.assertFalse(any("testakte" in n or n.endswith("-werkstatt.md") for n in native.namelist()))
        self.assertIn("beispiel-werkstatt.txt", read_checksums(self.dist / B.CHECKSUMS))
        self.assertTrue((self.root / self.source / "testakte/downloads/testakte-alt.zip").exists())

    def test_readme_links_in_both_packages_use_checkout_or_shipped_member(self):
        from package_readme import REPOSITORY, add_to_archive
        source = self.write(f"{self.source}/README.md", (
            "[Skill](skills/vertrag-pruefen/SKILL.md) [Dateien](.) [hier](#beginn)\n"
            "[`Katalog`](../../skills-index/Fall%20%C3%84.md?plain=1#rubrik)\n"
            "[Aktenordner](testakte/) [Werkstatt](beispiel-werkstatt.md)\n"
            "[Ziel]: <../../skills-index/Fall Ä.md> 'Quellenblatt'\n"
            "[Website](https://example.org) [Mail](mailto:kanzlei@example.org)\n"
            "Ein Beispiel: `[fiktiv](../../faellt-ins-leere.md)`\n"
            "```md\n[ebenso](../../beispiel.md)\n```\n"
        ))
        original = source.read_bytes()
        self.write("skills-index/Fall Ä.md", "# Rubrik")
        self.write(f"{self.source}/werkzeuge/README.md", "[Katalog](../../../skills-index/Fall%20%C3%84.md) [Skill](../skills/vertrag-pruefen/SKILL.md)")
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                        "commit", "-qm", "Fixture"], cwd=self.root, check=True)
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=self.root, text=True).strip()
        report = B.build(self.dist, self.scope, self.root, expected_commit=commit)
        with zipfile.ZipFile(self.dist / "beispiel.zip") as native, zipfile.ZipFile(self.dist / "beispiel-portable.zip") as portable:
            output = native.read("README.md")
            self.assertEqual(output, portable.read("beispiel/README.md"))
            nested = native.read("werkzeuge/README.md")
            self.assertEqual(nested, portable.read("beispiel/werkzeuge/README.md"))
            self.assertIn(f"{REPOSITORY}/blob/{commit}/skills-index/Fall%20%C3%84.md".encode(), nested)
            self.assertIn(b"../skills/vertrag-pruefen/SKILL.md", nested)
            self.assertEqual(source.read_bytes(), original)
            expected = original.decode().replace("../../skills-index/Fall%20%C3%84.md", f"{REPOSITORY}/blob/{commit}/skills-index/Fall%20%C3%84.md")
            expected = expected.replace("../../skills-index/Fall Ä.md", f"{REPOSITORY}/blob/{commit}/skills-index/Fall%20%C3%84.md")
            expected = expected.replace("(testakte/)", f"({REPOSITORY}/tree/{commit}/{self.source}/testakte)")
            expected = expected.replace("(beispiel-werkstatt.md)", f"({REPOSITORY}/blob/{commit}/{self.source}/beispiel-werkstatt.md)")
            self.assertEqual(output.decode(), expected)
            self.assertEqual(report["source_state"]["commit"], commit)
            # The collection uses the real ZIP member list and adds the root README last.
            global_zip = self.base / "collection.zip"
            with zipfile.ZipFile(global_zip, "w") as collection:
                for item in native.infolist():
                    if item.filename != "README.md":
                        collection.writestr(item, native.read(item))
        add_to_archive(global_zip, self.root, source.parent, commit)
        with zipfile.ZipFile(global_zip) as collection:
            self.assertEqual(collection.read("README.md"), output)
        with self.assertRaisesRegex(ValueError, "bereits"):
            add_to_archive(global_zip, self.root, source.parent, commit)
        # Replacing the rendered README with the historical broken bytes must fail.
        files = B.source_files(self.root, source.parent)
        stale = self.base / "stale.zip"
        B.write_zip(stale, files)
        with self.assertRaisesRegex(ValueError, "README"):
            B.verify_zip(stale, files, readme=output)

    def test_broken_repository_readme_target_fails_build(self):
        self.write(f"{self.source}/README.md", "[Nicht vorhanden](../../fehlende-datei.md)\n")
        with self.assertRaisesRegex(ValueError, "Ziel im Repository fehlt"):
            self.build()

    def test_only_named_prompt_txt_is_release_asset(self):
        for name in ("beispiel-werkstatt.txt", "beispiel-schnellstart.txt", "beispiel-hauptproblem.txt"):
            path = self.write(name, "Prompt")
            self.assertTrue(is_release_asset(path))
        self.assertFalse(is_release_asset(self.write("intern.txt", "Intern")))

    def test_scope_forbids_invented_codex_and_missing_existing_prompt(self):
        scope = copy.deepcopy(self.scope)
        scope["plugins"][0]["variants"].append("codex")
        with self.assertRaises(ValueError):
            B.validate_scope(scope, self.root)
        scope = copy.deepcopy(self.scope)
        scope["plugins"][0]["prompts"].pop()
        with self.assertRaises(ValueError):
            B.validate_scope(scope, self.root)

    def test_explicit_unchanged_prompts_may_keep_existing_publication(self):
        row = self.scope["plugins"][0]
        row["preserved_prompts"] = {name: B.sha256_file(self.root / self.source / name) for name in row["prompts"]}
        row["prompts"] = []
        self.build()
        self.assertEqual({p.name for p in self.dist.iterdir()}, {"beispiel.zip", "beispiel-portable.zip", B.REPORT, B.CHECKSUMS})
        self.write(f"{self.source}/beispiel-werkstatt.md", "Ungepruefte neue Promptfassung")
        with self.assertRaisesRegex(ValueError, "muss neu veröffentlicht werden"):
            B.validate_scope(self.scope, self.root)

    def test_preserved_prompts_cannot_hide_missing_extra_or_duplicate_file(self):
        row = self.scope["plugins"][0]
        row["preserved_prompts"] = {row["prompts"][0]: B.sha256_file(self.root / self.source / row["prompts"][0])}
        with self.assertRaisesRegex(ValueError, "doppelt deklarierter"):
            B.validate_scope(self.scope, self.root)
        row["prompts"] = []
        with self.assertRaisesRegex(ValueError, "nicht vollständig"):
            B.validate_scope(self.scope, self.root)
        row["preserved_prompts"]["fremd.txt"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "nicht vollständig"):
            B.validate_scope(self.scope, self.root)

    def test_extra_assets_cannot_expand_scope_to_arbitrary_documents(self):
        for extras in ([{"name": "interne-testakte.pdf"}], [{"name": "ki-native-kanzlei-skills-handbuch.pdf"}]):
            scope = {**self.scope, "additional_assets": extras}
            with self.assertRaisesRegex(ValueError, "vollständige geprüfte KI-native-Handbuchpaar"):
                B.validate_scope(scope, self.root)
        self.assertTrue(is_release_asset(self.write("ki-native-kanzlei-skills-handbuch.pdf", b"PDF")))
        self.assertFalse(is_release_asset(self.write("interne-testakte.pdf", b"PDF")))

    def test_anfechtung_445_36_2_scope_requires_both_workshop_assets(self):
        # Nur Scope-Fixture: echte PDF-/ZIP-Inhalte prüft der Exportvertrag separat.
        name, version = "insolvenzanfechtung", "445.36.2"
        tag = "qualitaetsrunde-v445.36.2"
        manifest = {"name": name, "version": version, "description": "Technische Scope-Fixture."}
        for relative in B.MANIFESTS:
            self.write(f"{name}/{relative}", json.dumps(manifest))
        self.write(".claude-plugin/marketplace.json", json.dumps({
            "version": self.version,
            "plugins": [{"name": name, "version": version, "source": "./" + name}],
        }))
        self.write("scripts/scoped-release-assets.json", json.dumps({
            "schema_version": 1, "assets": {name + ".zip": tag},
        }))
        scope = {"schema_version": 1, "version": version, "tag": tag,
                 "plugins": [{"name": name, "variants": ["native"], "prompts": []}]}
        self.write(B.ANFECHTUNG_EVIDENCE, "{}\n")
        extras = []
        for asset in sorted(B.ANFECHTUNG_ASSETS):
            source = "docs/werkstattprompts/insolvenzanfechtung/" + asset
            path = self.write(source, b"Scope-Testdaten; kein echter Export.\n")
            extras.append({"name": asset, "source": source,
                           "evidence": B.ANFECHTUNG_EVIDENCE, "sha256": B.sha256_file(path)})
        complete = {**scope, "additional_assets": extras}
        self.assertIn(name, B.validate_scope(complete, self.root))
        for omitted in (None, [], extras[:1], extras[1:]):
            candidate = copy.deepcopy(scope)
            if omitted is not None:
                candidate["additional_assets"] = omitted
            with self.subTest(assets=omitted), self.assertRaisesRegex(
                ValueError, "445.36.2 benötigt das vollständige geprüfte Werkstattpaar"
            ):
                B.validate_scope(candidate, self.root)

    def test_mismatched_manifest_or_route_stops_build(self):
        self.write(f"{self.source}/.codex-plugin/plugin.json", json.dumps({"name": self.name, "version": "1.0.0"}))
        with self.assertRaises(ValueError):
            self.build()
        self.write("scripts/scoped-release-assets.json", json.dumps({"schema_version": 1, "assets": {}}))
        with self.assertRaises(ValueError):
            B.validate_scope(self.scope, self.root)

    def test_required_file_reviews_block_release_until_complete_and_byte_bound(self):
        self.scope["required_file_reviews"] = {self.name: 1}
        profile_path = "quality/evals/beispiel.json"
        relative = f"{self.source}/skills/vertrag-pruefen/SKILL.md"
        old = {"status": "needs_review", "reason": "Geänderte Fassung", "files": [relative]}
        profile = {"plugin": self.name, "file_review_status": old}
        self.write(profile_path, json.dumps(profile))
        with self.assertRaisesRegex(ValueError, "Dateinachprüfungen"):
            B.validate_scope(self.scope, self.root)
        report = self.write("quality/source-audits/report.md", "Vollständige Lektüre und konkrete Prüfung des Vertragswegs.")
        evidence = {"schema_version": 1, "plugin": self.name, "date": "2026-11-14",
                    "method": "full_file_review", "limits": "Dateiprüfung, kein Modelltest.",
                    "previous_status": old,
                    "files": [{"path": relative, "before_sha256": B.sha256_file(self.root / relative),
                               "reviewed_sha256": B.sha256_file(self.root / relative),
                               "full_file_read": True, "result": "retained",
                               "checked_points": ["Vertragsauftrag abgegrenzt", "Vollständiges Endprodukt verlangt"],
                               "finding": "Auftrag und Quellenpflicht konkret erhalten."}],
                    "reports": {report.relative_to(self.root).as_posix(): B.sha256_file(report)}}
        record = self.write("quality/source-audits/completed.json", json.dumps(evidence))
        profile["file_review_status"] = {"status": "reviewed", "reason": "Vollständig nachgeprüft",
                                         "files": [relative], "evidence": {
                                             "path": record.relative_to(self.root).as_posix(), "sha256": B.sha256_file(record)}}
        self.write(profile_path, json.dumps(profile))
        self.assertIn(self.name, B.validate_scope(self.scope, self.root))
        self.scope["required_file_reviews"][self.name] = 2
        with self.assertRaisesRegex(ValueError, "Dateinachprüfungen"):
            B.validate_scope(self.scope, self.root)
        self.scope["required_file_reviews"][self.name] = 1
        report.write_text("Bericht nachträglich verändert")
        with self.assertRaisesRegex(ValueError, "Nachprüfungsbericht"):
            B.validate_scope(self.scope, self.root)

    def test_required_file_review_rejects_matching_profile_and_evidence_for_wrong_plugin(self):
        from quality_lab import pending_file_reviews

        self.scope["required_file_reviews"] = {self.name: 1}
        relative = f"{self.source}/skills/vertrag-pruefen/SKILL.md"
        sha = B.sha256_file(self.root / relative)
        report = self.write("quality/source-audits/report.md", "Technische Fixture, kein wirklicher Dateireview.")
        evidence = {"schema_version": 1, "plugin": "anderes-plugin", "date": "2026-11-14",
                    "method": "full_file_review", "limits": "Nur technische Testdaten, kein Modelltest.",
                    "previous_status": {"status": "needs_review", "reason": "Fassung verändert", "files": [relative]},
                    "files": [{"path": relative, "before_sha256": sha, "reviewed_sha256": sha,
                               "full_file_read": True, "result": "retained",
                               "checked_points": ["Erster Fixture-Prüfpunkt", "Zweiter Fixture-Prüfpunkt"],
                               "finding": "Technisch vollständiger, aber falsch zugeordneter Beleg."}],
                    "reports": {report.relative_to(self.root).as_posix(): B.sha256_file(report)}}
        record = self.write("quality/source-audits/completed.json", json.dumps(evidence))
        profile = {"plugin": "anderes-plugin", "file_review_status": {
            "status": "reviewed", "reason": "Vollständige Fixture", "files": [relative],
            "evidence": {"path": record.relative_to(self.root).as_posix(), "sha256": B.sha256_file(record)}}}
        # Das Paar ist in sich konsistent. Erst der Release-Scope deckt die Verwechslung auf.
        self.assertEqual(pending_file_reviews(profile, self.root), [])
        self.write(f"quality/evals/{self.name}.json", json.dumps(profile))
        with self.assertRaisesRegex(ValueError, "Nachprüfungsprofil gehört nicht zum Plugin"):
            B.validate_scope(self.scope, self.root)

    def test_twenty_one_active_skills_ship_but_twenty_two_cannot(self):
        for i in range(20):
            name = f"fachfrage-{i}-pruefen"
            self.write(f"{self.source}/skills/{name}/SKILL.md",
                       f"---\nname: {name}\ndescription: Fachfrage prüfen\n---\n\n# Fachfrage prüfen\n")
        report = self.build()
        self.assertEqual(len(report["plugins"][self.name]["skills"]), 21)
        for filename in ("beispiel.zip", "beispiel-portable.zip"):
            with zipfile.ZipFile(self.dist / filename) as archive:
                self.assertEqual(sum(name.endswith("/SKILL.md") for name in archive.namelist()), 21)
        self.write(f"{self.source}/skills/zusaetzliche-frage/SKILL.md", "# Zusätzliche Frage\n")
        with self.assertRaisesRegex(ValueError, "1 bis 21 echte SKILL.md-Dateien, gefunden: 22"):
            B.build(self.dist.with_name("too-many"), self.scope, self.root)

    def test_orphaned_fachtext_cannot_ship(self):
        directory = self.root / self.source
        self.write(f"{self.source}/skills/verwaist/FACHINHALT.md", "# Verwaist\n")
        with self.assertRaises(ValueError):
            B.verify_reachability(B.source_files(self.root, directory))

    def test_missing_tool_cannot_ship(self):
        (self.root / self.source / "skills/alter-vertrag/werkzeuge/rechnen.py").unlink()
        with self.assertRaises(ValueError):
            self.build()

    def test_existing_dist_and_mutated_download_are_rejected(self):
        self.build()
        with self.assertRaises(ValueError):
            self.build()
        (self.dist / "beispiel-werkstatt.txt").write_text("Verändert")
        with self.assertRaises(ValueError):
            B.validate_assets(self.dist, self.scope, self.root)

    def test_source_byte_mismatch_is_rejected_even_with_intact_zip_checksums(self):
        self.build()
        self.write(f"{self.source}/skills/alter-vertrag/werkzeuge/rechnen.py", "print('Fremder Stand')\n")
        with self.assertRaises(ValueError):
            B.validate_assets(self.dist, self.scope, self.root)

    def test_clean_immutable_commit_required_for_publish_build(self):
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "Fixture"], cwd=self.root, check=True)
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=self.root, text=True).strip()
        self.assertEqual(B.checkout_state(self.root, commit), {"commit": commit, "clean": True})
        self.write("uncommitted.md", "Nicht im Commit")
        with self.assertRaises(ValueError):
            B.checkout_state(self.root, commit)

    def test_rate_budget_is_required_before_independent_download(self):
        self.build()
        with patch.object(B, "validate_assets", return_value={}), patch.object(
            B, "require_download_budget", side_effect=RuntimeError("Budget erschöpft")
        ) as budget, patch.object(B.subprocess, "run") as download:
            with self.assertRaisesRegex(RuntimeError, "Budget erschöpft"):
                B.verify_download(self.dist, self.scope, self.root, "example/repo", "a" * 40)
        budget.assert_called_once_with(6)
        download.assert_not_called()

    def test_download_uses_fresh_directory_and_matches_every_local_asset(self):
        self.build()
        import shutil
        def downloaded(command, **kwargs):
            target = Path(command[command.index("--dir") + 1])
            self.assertNotEqual(target, self.dist)
            self.assertEqual(list(target.iterdir()), [])
            self.assertEqual(kwargs["timeout"], 1800)
            for path in self.dist.iterdir():
                shutil.copyfile(path, target / path.name)
        with patch.object(B, "validate_assets", return_value={}) as validate, patch.object(
            B, "require_download_budget"
        ), patch.object(B.subprocess, "run", side_effect=downloaded):
            B.verify_download(self.dist, self.scope, self.root, "example/repo", "a" * 40)
        self.assertEqual(validate.call_count, 2)

    def test_workflow_pins_commit_and_verifies_download_before_publication(self):
        path = Path(__file__).resolve().parents[1] / ".github/workflows/skill-quality-release.yml"
        text = path.read_text()
        self.assertIn("expected_commit:", text)
        self.assertIn("github.ref != 'refs/heads/main'", text)
        self.assertIn("--protect-published", text)
        self.assertIn("--expected-commit", text)
        self.assertNotIn("--clobber", text)
        self.assertNotIn("--latest=true", text)
        self.assertLess(text.index("--verify-download"), text.index("--draft=false"))
        self.assertLess(text.index("Vollständige Pakete"), text.index("Geschützte Veröffentlichung"))
        self.assertIn("timeout-minutes: 240", text)


PUBLISH = B.load_module("publish-skill-quality-release.py")


class PublisherGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.dist = self.root / "dist"
        self.dist.mkdir()
        self.commit = "a" * 40
        self.scope = {"tag": "qualitaetsrunde-v445.36.0", "version": "445.36.0"}
        notes = self.root / "docs/releases/qualitaetsrunde-v445.36.0.md"
        notes.parent.mkdir(parents=True)
        notes.write_text("Konkrete geprüfte Änderungen\n")
        self.events = []
        for obj, name, value in ((PUBLISH.B, "checkout_state", None), (PUBLISH.B, "validate_assets", {})):
            mock = patch.object(obj, name, return_value=value)
            mock.start(); self.addCleanup(mock.stop)
        execute = patch.object(PUBLISH, "execute", side_effect=lambda command, **kw: self.events.append(command))
        execute.start(); self.addCleanup(execute.stop)

    def publish(self):
        # Mock-Veröffentlichungen dürfen keine scheinbar echte Erfolgsmeldung ausgeben.
        with redirect_stdout(io.StringIO()):
            PUBLISH.publish(self.dist, self.scope, self.commit, "example/repo", root=self.root)

    def test_existing_published_release_is_never_mutated(self):
        with patch.object(PUBLISH.P, "tag_commit", return_value=self.commit), patch.object(PUBLISH.P, "companion_release", return_value={"isDraft": False}):
            with self.assertRaisesRegex(ValueError, "Veröffentlichtes Release"):
                self.publish()
        self.assertFalse(any(command[0] == "gh" for command in self.events))

    def test_foreign_tag_is_never_moved(self):
        with patch.object(PUBLISH.P, "tag_commit", return_value="b" * 40), patch.object(PUBLISH.P, "companion_release", return_value=None):
            with self.assertRaisesRegex(ValueError, "anderen Commit"):
                self.publish()
        self.assertFalse(any(command[0] == "gh" for command in self.events))

    def test_download_failure_prevents_publication(self):
        draft = {"isDraft": True, "databaseId": 7, "tagName": self.scope["tag"]}
        with patch.object(PUBLISH.P, "tag_commit", return_value=self.commit), patch.object(PUBLISH.P, "companion_release", return_value=draft), patch.object(PUBLISH.B, "verify_download", side_effect=ValueError("Download abweichend")):
            with self.assertRaisesRegex(ValueError, "Download abweichend"):
                self.publish()
        self.assertTrue(any("--protect-published" in command for command in self.events))
        uploader = next(command for command in self.events if "--protect-published" in command)
        self.assertIn("--paced-github-token", uploader)
        self.assertEqual(uploader[uploader.index("--workers") + 1], "1")
        self.assertFalse(any("--draft=false" in command for command in self.events))

    def test_tag_after_verification_download_before_publish_and_latest_false(self):
        draft = {"isDraft": True, "databaseId": 7, "tagName": self.scope["tag"]}
        with patch.object(PUBLISH.P, "tag_commit", side_effect=[None, self.commit, self.commit, self.commit]), patch.object(PUBLISH.P, "companion_release", side_effect=[None, draft, draft, {**draft, "isDraft": False}]), patch.object(PUBLISH.B, "verify_download", side_effect=lambda *a: self.events.append(["download-verified"])):
            self.publish()
        downloaded = next(i for i, command in enumerate(self.events) if command[0] == "download-verified")
        published = next(i for i, command in enumerate(self.events) if "--draft=false" in command)
        self.assertLess(downloaded, published)
        self.assertIn("--latest=false", self.events[published])
        self.assertFalse(any("--latest=true" in command or "--clobber" in command for command in self.events))


if __name__ == "__main__":
    unittest.main()
