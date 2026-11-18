#!/usr/bin/env python3
"""Verlustfreiheit, echte Auswahlgrenze und installierbare Fachbibliotheken."""
import copy
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest
import zipfile

import jsonschema


SCRIPT = Path(__file__).with_name("consolidate-skill-cap.py")
M = runpy.run_path(str(SCRIPT))


class SkillCapMigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo, self.target = self.base / "repo", self.base / "output"
        self.repo.mkdir()
        self.plugin = self.repo / "themen/fachgebiet"
        for slug in ("hauptauftrag", "vertrag", "vollmacht"):
            self.write(f"themen/fachgebiet/skills/{slug}/SKILL.md",
                       f'---\nname: {slug}\ndescription: "Konkretes Fachprodukt"\n---\n\n# {slug} prüfen\n\nÄußerung, Recht und Beleg.\n')
        self.write("themen/fachgebiet/skills/vertrag/werkzeuge/rechnen.py", "print('Berechnung')\n")
        self.write("themen/fachgebiet/skills/vertrag/vorlagen/beispiel.xlsx", b"PK\x00\xffOriginal")
        self.write("themen/fachgebiet/skills/vollmacht/references/pruefung.md", "# Vertretung\n\nGesondert prüfen.\n")
        self.write("themen/fachgebiet/.claude-plugin/plugin.json", '{"name":"fachgebiet","version":"1.0.0"}\n')
        self.write(".claude-plugin/marketplace.json", json.dumps({"plugins": [{"name": "fachgebiet", "source": "./themen/fachgebiet"}]}))
        self.route = {"slug": "abschluss-und-vertretung", "title": "Abschluss und Vertretung prüfen",
                      "description": "Prüft Abschluss und Vollmacht; erstellt eine bereinigte Vertragsfassung.",
                      "purpose": "Vertragsabschluss aus den Unterlagen feststellen.",
                      "inputs": ["Entwurf und Korrespondenz"], "steps": ["Fassungen vergleichen.", "Vertretung getrennt prüfen."],
                      "outputs": ["Bereinigte Vertragsfassung"], "examples": ["Vollmacht fehlt zum jüngsten Entwurf."],
                      "members": ["vertrag", "vollmacht"]}
        self.registry = {"schema_version": 1, "plugins": [{"name": "fachgebiet", "source": "./themen/fachgebiet", "keep": ["hauptauftrag"], "routes": [self.route]}]}

    def write(self, relative, data):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data.encode("utf-8") if isinstance(data, str) else data)
        return path

    def migrate(self):
        return M["migrate"](self.repo, self.target, self.registry)

    def test_check_and_default_are_read_only(self):
        registry = self.base / "registry.json"
        registry.write_text(json.dumps(self.registry))
        before = {str(p.relative_to(self.repo)): p.read_bytes() for p in self.repo.rglob("*") if p.is_file()}
        for flags in ([], ["--check"]):
            result = subprocess.run([sys.executable, str(SCRIPT), "--repo", str(self.repo), "--registry", str(registry), *flags], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        after = {str(p.relative_to(self.repo)): p.read_bytes() for p in self.repo.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.assertFalse(self.target.exists())

    def test_complete_partition_and_twenty_one_cap_are_mandatory(self):
        self.assertEqual([], M["validate_registry"](self.repo, self.registry))
        incomplete = copy.deepcopy(self.registry)
        incomplete["plugins"][0]["routes"][0]["members"].remove("vollmacht")
        self.assertTrue(M["validate_registry"](self.repo, incomplete))
        duplicate = copy.deepcopy(self.registry)
        duplicate["plugins"][0]["routes"][0]["members"].append("hauptauftrag")
        self.assertTrue(M["validate_registry"](self.repo, duplicate))
        too_many = copy.deepcopy(self.registry)
        too_many["plugins"][0]["routes"] *= 21
        self.assertTrue(any("überschreiten 21" in e for e in M["validate_registry"](self.repo, too_many)))

    def test_declared_main_workflow_cannot_be_downgraded_even_with_complete_partition(self):
        self.write("scripts/data/werkstatt-visualisierung-profile.json", json.dumps({
            "schema_version": 1, "plugins": {"fachgebiet": {"entry_skills": ["hauptauftrag"]}}}))
        self.assertEqual(M["validate_registry"](self.repo, self.registry), [])
        downgraded = copy.deepcopy(self.registry)
        downgraded["plugins"][0]["keep"] = []
        downgraded["plugins"][0]["routes"][0]["members"].append("hauptauftrag")
        before = {str(p.relative_to(self.repo)): p.read_bytes() for p in self.repo.rglob("*") if p.is_file()}
        errors = M["validate_registry"](self.repo, downgraded)
        self.assertEqual(len(errors), 1)
        self.assertIn("Einstiegsskills müssen in keep bleiben", errors[0])
        with self.assertRaisesRegex(ValueError, "Einstiegsskills müssen in keep bleiben"):
            M["migrate"](self.repo, self.target, downgraded)
        self.assertFalse(self.target.exists())
        after = {str(p.relative_to(self.repo)): p.read_bytes() for p in self.repo.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_declared_main_workflow_must_exist_and_profile_must_be_valid(self):
        path = "scripts/data/werkstatt-visualisierung-profile.json"
        self.write(path, json.dumps({"schema_version": 1, "plugins": {"fachgebiet": {"entry_skills": ["fehlt"]}}}))
        self.assertTrue(any("Einstiegsskills fehlen" in e
                            for e in M["validate_registry"](self.repo, self.registry)))
        for entry in ([], "hauptauftrag", ["hauptauftrag", "hauptauftrag"], [None], ["../ausserhalb"],
                      ["hauptauftrag", "vertrag", "vollmacht", "weitere"]):
            self.write(path, json.dumps({"schema_version": 1, "plugins": {"fachgebiet": {"entry_skills": entry}}}))
            with self.subTest(entry=entry):
                self.assertTrue(any("entry_skills" in e
                                    for e in M["validate_registry"](self.repo, self.registry)))

    def test_entry_profiles_require_supported_schema_and_plugin_mapping(self):
        path = "scripts/data/werkstatt-visualisierung-profile.json"
        for data in ({}, {"plugins": {}}, {"schema_version": 2, "plugins": {}},
                     {"schema_version": True, "plugins": {}}, {"schema_version": "1", "plugins": {}},
                     {"schema_version": 1, "plugins": []}):
            self.write(path, json.dumps(data))
            with self.subTest(data=data):
                self.assertTrue(any("Einstiegsprofile benötigen schema_version 1" in e
                                    for e in M["validate_registry"](self.repo, self.registry)))

    def test_historical_migrated_registry_is_not_reinterpreted_by_current_entry_profile(self):
        self.migrate()
        # Im migrierten Bestand zählen dessen erhaltene Quellen und Zuordnungen.
        path = self.target / "scripts/data/werkstatt-visualisierung-profile.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"plugins": {"fachgebiet": {"entry_skills": ["vertrag"]}}}))
        self.assertEqual(M["validate_registry"](self.target.resolve(), self.registry, migrated=True), [])
        path.write_text("Unlesbares heutiges Profil")
        self.assertEqual(M["validate_registry"](self.target.resolve(), self.registry, migrated=True), [])

    def test_twenty_routes_and_preserved_main_skill_pass_but_extra_route_fails(self):
        boundary = copy.deepcopy(self.registry)
        routes = boundary["plugins"][0]["routes"]
        for number in range(1, 21):
            source = f"quelle-{number}"
            self.write(f"themen/fachgebiet/skills/{source}/SKILL.md", "# Fachquelle\n")
            route = copy.deepcopy(self.route)
            route.update(slug=f"pruefung-{number}", members=[source])
            routes.append(route)
            if number == 19:
                # Ein erhaltener Hauptskill und zwanzig neue Arbeitswege zählen zusammen.
                self.assertEqual(M["validate_registry"](self.repo, boundary), [])
        self.assertTrue(any("22 Auswahlwege überschreiten 21" in e
                            for e in M["validate_registry"](self.repo, boundary)))

    def test_registry_schema_accepts_twenty_one_routes_but_rejects_twenty_two(self):
        schema = json.loads((SCRIPT.parent / "data/skill-cap-registry.schema.json").read_text())
        boundary = copy.deepcopy(self.registry)
        plugin = boundary["plugins"][0]
        plugin["keep"] = []
        plugin["routes"] = [dict(self.route, slug=f"arbeitsweg-{number}", members=[f"quelle-{number}"])
                            for number in range(21)]
        jsonschema.validate(boundary, schema)
        plugin["routes"].append(dict(self.route, slug="zusaetzlicher-arbeitsweg"))
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(boundary, schema)

    def test_procurement_document_style_is_explicit_and_preserves_sources(self):
        sources = {slug: (self.plugin / "skills" / slug / "SKILL.md").read_bytes()
                   for slug in self.route["members"]}
        sources["vertrag"] = sources["vertrag"].replace(b"# vertrag", b"# Paragraf 134 GWB")
        before = copy.deepcopy(sources)
        ordinary = M["render_route"](self.route, sources).decode()
        self.assertNotIn("<!-- BEGIN output-format-block", ordinary)
        self.assertIn("[Paragraf 134 GWB", ordinary)
        procurement = {**self.route, "document_style": "vergaberecht",
                       "description": "Vorabinformation nach Paragraf 134 GWB vorbereiten."}
        result = M["render_route"](procurement, sources).decode()
        self.assertEqual(result.count("<!-- BEGIN output-format-block (autogen) -->"), 1)
        self.assertEqual(result.count("<!-- END output-format-block (autogen) -->"), 1)
        self.assertIn("[§ 134 GWB", result)
        self.assertIn("description: \"Vorabinformation nach Paragraf 134 GWB", result)
        self.assertIn("../../references/OUTPUT-FORMAT.md", result)
        self.assertIn("Bei abweichenden Vorgaben der Stelle", result)
        self.assertEqual(sources, before)
        self.assertIn("../vertrag/FACHINHALT.md", result)
        self.assertIn("../vollmacht/FACHINHALT.md", result)

    def test_unknown_document_style_is_rejected(self):
        invalid = copy.deepcopy(self.registry)
        invalid["plugins"][0]["routes"][0]["document_style"] = "ungeprueft"
        self.assertTrue(any("document_style" in e for e in M["validate_registry"](self.repo, invalid)))
        with self.assertRaisesRegex(ValueError, "document_style"):
            M["render_route"](invalid["plugins"][0]["routes"][0], {})

    def test_named_steps_render_a_concrete_start_without_affecting_default(self):
        sources = {slug: (self.plugin / "skills" / slug / "SKILL.md").read_bytes()
                   for slug in self.route["members"]}
        ordinary = M["render_route"](self.route, sources).decode()
        self.assertIn("### 3.1. Arbeitsschritt\n\nFassungen vergleichen.", ordinary)
        self.assertIn("Bearbeite den konkreten Auftrag", ordinary)
        self.route["step_titles"] = ["Vertragsfassung festlegen", "Vollmacht abgleichen"]
        revised = M["render_route"](self.route, sources).decode()
        self.assertNotIn("Bearbeite den konkreten Auftrag", revised)
        self.assertIn("### 3.1. Vertragsfassung festlegen\n\nFassungen vergleichen.", revised)
        self.assertIn("### 3.3. Fachvertiefungen gezielt laden", revised)
        self.assertEqual([], M["validate_registry"](self.repo, self.registry))
        self.route["step_titles"] = ["Zu kurz"]
        self.assertTrue(any("step_titles" in error for error in M["validate_registry"](self.repo, self.registry)))
        self.route["step_titles"] = ["Gültig", "Keine\nzweite Zeile"]
        self.assertTrue(any("step_titles" in error for error in M["validate_registry"](self.repo, self.registry)))

    def test_revised_route_is_source_bound_and_reversible(self):
        report = self.migrate()
        attest = report["plugins"][0]["routes"][0]
        directory = self.target / "themen/fachgebiet/skills"
        path = directory / self.route["slug"] / "SKILL.md"
        before = path.read_bytes()
        self.route["step_titles"] = ["Vertragsfassung festlegen", "Vollmacht abgleichen"]
        sources = {slug: (directory / slug / "FACHINHALT.md").read_bytes() for slug in self.route["members"]}
        after = M["render_route"](self.route, sources)
        _, edits = M["exact_edits"](before, [(0, len(before), after)])
        attest.update(original_sha256=M["sha"](before), sha256=M["sha"](after), edits=edits)
        path.write_bytes(after)
        reg_path = self.target / "scripts/data/skill-cap-registry.json"
        reg_path.parent.mkdir(parents=True)
        reg_path.write_bytes(M["json_bytes"](self.registry))
        report["registry_sha256"] = M["sha"](reg_path.read_bytes())
        self.assertEqual([], M["verify_source_map"](self.target, report, strict_links=True))

        before_patch = attest["edits"][0]["before"]
        attest["edits"][0]["before"] = before_patch + "Manipulation"
        self.assertTrue(any("nicht bytegleich rekonstruierbar" in error
                            for error in M["verify_source_map"](self.target, report)))
        attest["edits"][0]["before"] = before_patch

        self.route["step_titles"][0] = "Abweichende Überschrift"
        reg_path.write_bytes(M["json_bytes"](self.registry))
        self.assertTrue(any("Registry" in error for error in M["verify_source_map"](self.target, report)))
        report["registry_sha256"] = M["sha"](reg_path.read_bytes())
        self.assertTrue(any("nicht reproduzieren" in error
                            for error in M["verify_source_map"](self.target, report)))

    def test_new_route_cannot_overwrite_old_or_resource_directory(self):
        for slug in ("vertrag", "hauptauftrag"):
            registry = copy.deepcopy(self.registry)
            registry["plugins"][0]["routes"][0]["slug"] = slug
            self.assertTrue(M["validate_registry"](self.repo, registry))
        self.write("themen/fachgebiet/skills/abschluss-und-vertretung/retained.txt", "Bewahren")
        with self.assertRaises(ValueError):
            self.migrate()

    def test_all_original_bytes_tools_and_templates_remain(self):
        report = self.migrate()
        self.assertEqual([], M["verify_source_map"](self.target, report, strict_links=True))
        for item in report["files"]:
            self.assertEqual((self.repo / item["original_path"]).read_bytes(),
                             M["restore_original"]((self.target / item["path"]).read_bytes(), item["edits"]))
        self.assertTrue((self.plugin / "skills/vertrag/SKILL.md").is_file())
        output = self.target / "themen/fachgebiet"
        self.assertFalse((output / "skills/vertrag/SKILL.md").exists())
        self.assertTrue((output / "skills/vertrag/FACHINHALT.md").is_file())
        self.assertEqual(len(list((output / "skills").glob("*/SKILL.md"))), 2)
        self.assertEqual((output / "skills/vertrag/werkzeuge/rechnen.py").read_bytes(), b"print('Berechnung')\n")

    def test_unicode_link_rewrites_restore_exact_original(self):
        path = self.plugin / "skills/vertrag/SKILL.md"
        extra = ("\nÜberprüfung: [Vollmacht](../vollmacht/SKILL.md#vertretung).\n"
                 "Aufruf /fachgebiet:vollmacht. Lokaler Pfad `../vollmacht/SKILL.md`.\n"
                 "[Quellfassung](https://github.com/example/repo/blob/main/themen/fachgebiet/skills/vollmacht/SKILL.md).\n")
        path.write_text(path.read_text() + extra)
        report = self.migrate()
        item = next(i for i in report["files"] if i["original_path"].endswith("vertrag/SKILL.md"))
        result = (self.target / item["path"]).read_bytes()
        self.assertIn(b"../vollmacht/FACHINHALT.md#vertretung", result)
        self.assertIn(b"/fachgebiet:abschluss-und-vertretung", result)
        self.assertIn(b"/fachgebiet:abschluss-und-vertretung Thema: vollmacht", result)
        self.assertEqual(path.read_bytes(), M["restore_original"](result, item["edits"]))
        self.assertEqual(len(item["edits"]), 4)

    def test_active_map_points_to_real_route_content_links_to_reference(self):
        path = self.plugin / "skills/hauptauftrag/SKILL.md"
        path.write_text(path.read_text() + "\n## 1. Fachlandkarte\n\n- `vertrag`: Prüfung\n- [Vollmacht](../vollmacht/SKILL.md)\n\n## 2. Fachvertiefung\n\n[Vollmacht](../vollmacht/SKILL.md)\n")
        report = self.migrate()
        result = (self.target / "themen/fachgebiet/skills/hauptauftrag/SKILL.md").read_text()
        self.assertIn("`abschluss-und-vertretung`", result)
        self.assertIn("`abschluss-und-vertretung` (Fachthema: vertrag)", result)
        self.assertIn("[Vollmacht](../abschluss-und-vertretung/SKILL.md)", result)
        self.assertIn("[Vollmacht](../vollmacht/FACHINHALT.md)", result)
        self.assertEqual([], M["verify_source_map"](self.target, report, strict_links=True))

    def test_stale_bytes_missing_tools_and_reintroduced_skills_are_rejected(self):
        report = self.migrate()
        path = self.target / "themen/fachgebiet/skills/vertrag/FACHINHALT.md"
        original = path.read_bytes()
        path.write_bytes(original + b"\nErfundene Aussage\n")
        self.assertTrue(M["verify_source_map"](self.target, report))
        path.write_bytes(original)
        tool = self.target / "themen/fachgebiet/skills/vertrag/werkzeuge/rechnen.py"
        tool.unlink()
        self.assertTrue(M["verify_source_map"](self.target, report))
        tool.write_bytes(b"print('Berechnung')\n")
        (path.parent / "SKILL.md").write_bytes(original)
        self.assertTrue(M["verify_source_map"](self.target, report))

    def test_incorrect_rewrite_log_cannot_forge_losslessness(self):
        path = self.plugin / "skills/vertrag/SKILL.md"
        path.write_text(path.read_text() + "\n[Vollmacht](../vollmacht/SKILL.md)\n")
        report = self.migrate()
        item = next(i for i in report["files"] if i["edits"])
        item["edits"][0]["before"] = "gefälschter Originaltext"
        self.assertTrue(M["verify_source_map"](self.target, report))

    def test_isolated_zip_has_references_and_helpers_without_repo_neighbors(self):
        report = self.migrate()
        archive = self.base / "plugin.zip"
        with zipfile.ZipFile(archive, "w") as z:
            for p in (self.target / "themen/fachgebiet").rglob("*"):
                if p.is_file():
                    z.write(p, p.relative_to(self.target))
        isolated = self.base / "isolated"
        with zipfile.ZipFile(archive) as z:
            z.extractall(isolated)
        self.assertEqual([], M["verify_source_map"](isolated, report, strict_links=True))
        (isolated / "themen/fachgebiet/skills/vollmacht/FACHINHALT.md").unlink()
        self.assertTrue(M["verify_source_map"](isolated, report))

    def test_missing_and_outside_links_fail(self):
        report = self.migrate()
        route = self.target / "themen/fachgebiet/skills/abschluss-und-vertretung/SKILL.md"
        route.write_text(route.read_text() + "\n[Fehlt](../nicht-da/FACHINHALT.md)\n[Außerhalb](../../../../outside.md)\n")
        errors = M["local_link_errors"](route, self.target / "themen/fachgebiet")
        self.assertEqual(len(errors), 2)
        self.assertTrue(M["verify_source_map"](self.target, report))

    def test_nonempty_destination_and_existing_reference_are_rejected(self):
        self.target.mkdir()
        (self.target / "user.txt").write_text("Nicht löschen")
        with self.assertRaises(ValueError):
            self.migrate()
        self.assertEqual((self.target / "user.txt").read_text(), "Nicht löschen")
        (self.target / "user.txt").unlink()
        self.write("themen/fachgebiet/skills/vertrag/FACHINHALT.md", "Nicht überschreiben")
        with self.assertRaises(ValueError):
            self.migrate()

    def test_shared_reference_and_evidence_are_localized_with_exact_proof(self):
        path = self.plugin / "skills/vertrag/SKILL.md"
        path.write_text(path.read_text() + "\n[Zitierregel](../../../../references/zitierregel.md)\n")
        original = b"# Zitierregel\n\n[Quellennachweis](../quality/source-audits/nachweis.md)\n"
        self.write("references/zitierregel.md", original)
        self.write("quality/source-audits/nachweis.md", b"# Dokumentierter Nachweis\n")
        report = self.migrate()
        self.assertEqual(len(report["shared_dependencies"]), 2)
        self.assertEqual([], M["verify_source_map"](self.target, report, strict_links=True))
        reference = self.target / "themen/fachgebiet/references/repository/references/zitierregel.md"
        self.assertEqual(reference.read_bytes(), original)
        self.assertIn(b"../../references/repository/references/zitierregel.md", (self.target / "themen/fachgebiet/skills/vertrag/FACHINHALT.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
