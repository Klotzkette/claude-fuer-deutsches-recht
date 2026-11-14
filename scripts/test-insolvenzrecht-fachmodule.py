#!/usr/bin/env python3
"""Prüft Auswahl, Herkunft, Drift und eigenständige Paketnutzung der Fachmodule."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path, PurePosixPath
import re
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile, ZIP_DEFLATED


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("insolvenz_fachmodule", ROOT / "scripts/build-insolvenzrecht-fachmodule.py")
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)
PLUGIN = ROOT / "insolvenzrecht"
BASE = PLUGIN / "references/fachmodule"
DIST: Path | None = None
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
CODE_PATH = re.compile(r"`((?:\.\.?/|references/|assets/|skills/)[^`\s]+\.(?:md|csv|html|json|py|pdf|docx|xlsx))`")
LINE_PATH = re.compile(r"(?m)^\s*-\s+((?:\.\.?/|references/|assets/|skills/)[^\s]+\.(?:md|csv|html|json|py|pdf|docx|xlsx))\s*$")


def hash_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()


def local_link_errors(plugin: Path) -> list[str]:
    """Auch reine Vorlagenpfade prüfen; Repository-Geschwister existieren hier nicht."""
    plugin = plugin.resolve()
    errors = []
    for source in (plugin / "references/fachmodule").rglob("*.md"):
        text = source.read_text()
        without_links = LINK.sub("", text)
        hrefs = LINK.findall(text) + CODE_PATH.findall(without_links) + LINE_PATH.findall(without_links)
        for href in hrefs:
            url = urlsplit(href)
            if url.scheme or href.startswith("//") or not url.path:
                continue
            target = (source.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(plugin) or not target.exists():
                errors.append(f"{source.relative_to(plugin)}: {href}")
    return errors


def verify_archive(archive: Path) -> None:
    expected = BUILDER.generate()
    with tempfile.TemporaryDirectory(prefix="inso-isoliertes-paket-") as temp:
        destination = Path(temp)
        with ZipFile(archive) as package:
            names = package.namelist()
            if len(names) != len(set(names)):
                raise AssertionError("Doppelte ZIP-Mitglieder")
            for name in names:
                pure = PurePosixPath(name)
                if pure.is_absolute() or ".." in pure.parts:
                    raise AssertionError(f"Unsicherer ZIP-Pfad: {name}")
                if package.getinfo(name).external_attr >> 16 & 0o170000 == 0o120000:
                    raise AssertionError(f"Symlink im Paket: {name}")
            package.extractall(destination)
        plugin = destination if (destination / ".claude-plugin/plugin.json").is_file() else destination / "insolvenzrecht"
        if not (plugin / ".claude-plugin/plugin.json").is_file():
            raise AssertionError("Hauptplugin-Manifest fehlt")
        errors = BUILDER.check_tree(plugin / "references/fachmodule", expected)
        if errors:
            raise AssertionError("Fachmodule im ZIP weichen ab: " + "; ".join(errors[:10]))
        errors = local_link_errors(plugin)
        if errors:
            raise AssertionError("Paket benötigt fehlende oder externe Dateien: " + "; ".join(errors[:10]))
        provenance = json.loads((plugin / "references/fachmodule/SOURCE_MAP.json").read_text())
        if hash_bytes((plugin / provenance["main_route"]).read_bytes()) != provenance["main_route_sha256"]:
            raise AssertionError("Hauptworkflow im Paket stimmt nicht mit der SourceMap überein")
        active = sorted(path.relative_to(plugin / "skills").as_posix() for path in (plugin / "skills").glob("*/SKILL.md"))
        original = sorted(path.relative_to(PLUGIN / "skills").as_posix() for path in (PLUGIN / "skills").glob("*/SKILL.md"))
        if active != original or len(active) != 99:
            raise AssertionError("Die Integration darf keine zusätzlichen auswählbaren Skills erzeugen")
        if list((plugin / "references/fachmodule").rglob("SKILL.md")):
            raise AssertionError("Fachreferenzen wurden als aktive Skills verpackt")


class InsolvenzFachmodule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / BUILDER.REGISTRY).read_text())
        cls.expected = BUILDER.generate()
        cls.source_map = json.loads(cls.expected[Path("SOURCE_MAP.json")])
        cls.by_source = {row["source"]: row for row in cls.source_map["files"]}

    def test_registry_covers_every_source_skill_and_runtime_file(self):
        expected = set(self.registry["shared_references"])
        for spec in self.registry["modules"].values():
            source = Path(spec["source"])
            expected.update(path.as_posix() for path in BUILDER.source_files(ROOT, source))
            self.assertEqual(set(spec["skills"]), {p.parent.name for p in (ROOT / source / "skills").glob("*/SKILL.md")})
        self.assertEqual(expected, set(self.by_source))
        self.assertEqual(self.source_map["source_skills"], 159)
        self.assertEqual(len(list((PLUGIN / "skills").glob("*/SKILL.md"))), 99)
        for row in self.source_map["files"]:
            self.assertEqual(row["source_sha256"], hash_bytes((ROOT / row["source"]).read_bytes()))
            self.assertTrue(row["reason"].strip())
            if "material_target" in row:
                self.assertEqual(row["material_sha256"], hash_bytes((ROOT / row["material_target"]).read_bytes()))
            elif "target_sha256" in row:
                self.assertEqual(row["target_sha256"], hash_bytes((ROOT / row["target"]).read_bytes()))

    def test_one_main_route_and_no_sibling_installation_required(self):
        routed = [row for row in self.by_source.values() if row["mode"] == "main-route"]
        self.assertEqual(len(routed), 17)
        for row in routed:
            self.assertEqual(row["target"], self.registry["main_route"])
            self.assertIn("material_target", row, "Besondere Kontextregeln dürfen nicht entfallen")
            self.assertTrue((ROOT / row["material_target"]).is_file())
        self.assertEqual(local_link_errors(PLUGIN), [])
        self.assertFalse(list(BASE.rglob("SKILL.md")))
        self.assertFalse(list(BASE.rglob("plugin.json")))

    def test_plan_templates_are_separate_and_byte_identical(self):
        templates = [row for row in self.by_source.values() if row["mode"] == "separate-plan-template"]
        self.assertEqual(len(templates), 22)
        for row in templates:
            self.assertEqual((ROOT / row["source"]).read_bytes(), (ROOT / row["canonical_source"]).read_bytes())
            self.assertEqual(row["canonical_sha256"], row["source_sha256"])
            self.assertTrue(row["target"].startswith(BUILDER.GITHUB + self.registry["plan_plugin"] + "/"))
            self.assertNotIn("material_target", row)
        self.assertFalse(any("planwerkstatt" in p.parts for p in self.expected))
        self.assertGreaterEqual(sum(row["mode"] == "asset" for row in self.by_source.values()), 30)

    def test_current_generated_tree_is_exact_and_deterministic(self):
        self.assertEqual(BUILDER.check_tree(BASE, self.expected), [])
        self.assertEqual(self.expected, BUILDER.generate())
        for target, checksum in self.source_map["generated_files"].items():
            self.assertEqual(hash_bytes((PLUGIN / target).read_bytes()), checksum)

    def test_registry_rejects_unassigned_source_skill(self):
        changed = json.loads(json.dumps(self.registry))
        changed["modules"]["berichte"]["skills"].pop("schlussbericht-erstellen")
        original = Path.read_bytes
        def altered(path):
            return BUILDER.json_bytes(changed) if path == ROOT / BUILDER.REGISTRY else original(path)
        with patch.object(Path, "read_bytes", altered):
            with self.assertRaisesRegex(ValueError, "Registry-Lücke"):
                BUILDER.generate()

    def test_regression_detects_changed_source_and_stale_generated_material(self):
        source = ROOT / "insolvenzverwaltung-berichtsersteller/skills/schlussbericht-erstellen/SKILL.md"
        original = Path.read_bytes
        def altered(path):
            data = original(path)
            return data + b"\nKonkrete neue fachliche Quellregel.\n" if path == source else data
        with patch.object(Path, "read_bytes", altered):
            changed = BUILDER.generate()
        errors = BUILDER.check_tree(BASE, changed)
        self.assertTrue(any("schlussbericht-erstellen.md" in error for error in errors), errors)
        self.assertIn("veraltet: SOURCE_MAP.json", errors)

    def test_source_map_binds_the_current_main_workflow(self):
        route = ROOT / self.registry["main_route"]
        self.assertEqual(self.source_map["main_route_sha256"], hash_bytes(route.read_bytes()))
        original = Path.read_bytes
        def altered(path):
            data = original(path)
            return data + b"\nNeue gemeinsame Auftragssteuerung.\n" if path == route else data
        with patch.object(Path, "read_bytes", altered):
            changed = BUILDER.generate()
        self.assertIn("veraltet: SOURCE_MAP.json", BUILDER.check_tree(BASE, changed))

    def test_regression_detects_missing_local_material_and_repository_escape(self):
        with tempfile.TemporaryDirectory(prefix="inso-negativtest-") as temp:
            root = Path(temp)
            file = root / "references/fachmodule/INDEX.md"
            file.parent.mkdir(parents=True)
            file.write_text("[Fehlt](berichte/nicht-vorhanden.md)\n[Geschwister](../../../insolvenzverwaltung/skills/kommandocenter/SKILL.md)\n")
            errors = local_link_errors(root)
            self.assertEqual(len(errors), 2)

    def test_isolated_main_plugin_contains_all_modules_and_templates(self):
        with tempfile.TemporaryDirectory(prefix="inso-pakettest-") as temp:
            archive = Path(temp) / "insolvenzrecht.zip"
            with ZipFile(archive, "w", ZIP_DEFLATED) as package:
                for source in sorted(PLUGIN.rglob("*")):
                    if source.is_file():
                        package.write(source, source.relative_to(PLUGIN).as_posix())
            verify_archive(archive)

    def test_provided_release_archive(self):
        if DIST is None:
            self.skipTest("Kein extern gebautes Release-Verzeichnis angegeben")
        archive = DIST / "insolvenzrecht.zip"
        self.assertTrue(archive.is_file(), archive)
        verify_archive(archive)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path)
    args, extra = parser.parse_known_args()
    DIST = args.dist
    unittest.main(argv=[__file__, *extra])
