#!/usr/bin/env python3
"""Prüft das Quellenprüfer-Plugin; mit --dist zusätzlich die dreizehn Releaseassets."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote
import zipfile

import pdfplumber
from pypdf import PdfReader
import yaml

ROOT = Path(__file__).resolve().parents[1]
NAME = "ki-halluzinationsreduzierer"
PLUGIN = ROOT / NAME
VERSION = "1.0.0"
KINDS = ("werkstatt", "schnellstart", "hauptproblem")
DIST = None
SKILLS = {
    "fundstellen-inventarisieren", "amtliche-quellen-erschliessen",
    "entscheidungsidentitaet-abgleichen", "zitate-und-randnummern-pruefen",
    "aussagen-am-volltext-pruefen", "uebertragbarkeit-und-gegenargumente-pruefen",
    "normfassungen-und-zeitbezug-pruefen", "literatur-materialien-und-standards-pruefen",
    "pruefbericht-und-korrekturfassung-erstellen", "nachpruefung-und-qualitaetskontrolle",
    "halluzinationspruefung-steuern",
}


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), ROOT / "scripts" / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_assets():
    names = {f"{NAME}.zip", f"{NAME}-portable.zip", "quellenabgleich.json", "checksums-sha256.txt"}
    names.update(f"{NAME}-{kind}.{suffix}" for kind in KINDS for suffix in ("md", "txt", "pdf"))
    return names


def expected_sources():
    excluded_prompts = {f"{NAME}-{kind}.{suffix}" for kind in KINDS
                        for suffix in ("md", "txt", "pdf", "docx")}
    sources = {}
    for path in PLUGIN.rglob("*"):
        relative = path.relative_to(PLUGIN)
        if any(part in {".git", ".venv", "node_modules", "__pycache__", "testakte", "testakten"}
               for part in relative.parts):
            continue
        if path.is_file() and path.name not in excluded_prompts | {".DS_Store", "CLAUDE.md"} and path.suffix != ".pyc":
            sources[relative.as_posix()] = path
    for name in ("LICENSE", "LICENSE-APACHE", "LICENSE-MIT", "NOTICE"):
        if name not in sources and (ROOT / name).is_file():
            sources[name] = ROOT / name
    return sources


class HallucinationReducerTests(unittest.TestCase):
    def require_dist(self):
        if DIST is None:
            self.skipTest("Releaseartefakte werden nach dem Build mit --dist geprüft.")
        self.assertTrue(DIST.is_dir(), str(DIST))

    def test_manifests_and_marketplace_version(self):
        for relative in ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
            with self.subTest(manifest=relative):
                data = json.loads((PLUGIN / relative).read_text(encoding="utf-8"))
                self.assertEqual((data["name"], data["version"]), (NAME, VERSION))
        portable = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(portable["$schema"], "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json")
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        found = [entry for entry in marketplace["plugins"] if entry["name"] == NAME]
        self.assertEqual(len(found), 1)
        self.assertEqual((found[0]["source"], found[0]["version"]), ("./" + NAME, VERSION))

    def test_eleven_skills_frontmatter_sections_and_formats(self):
        paths = list((PLUGIN / "skills").glob("*/SKILL.md"))
        self.assertEqual({path.parent.name for path in paths}, SKILLS)
        self.assertEqual(len(paths), 11)
        for path in paths:
            with self.subTest(skill=path.parent.name):
                content = path.read_text(encoding="utf-8")
                parts = content.split("---", 2)
                self.assertEqual(parts[0], "")
                metadata = yaml.safe_load(parts[1])
                self.assertEqual(set(metadata), {"name", "description"})
                self.assertEqual(metadata["name"], path.parent.name)
                self.assertRegex(metadata["name"], r"^[a-z0-9-]{1,64}$")
                self.assertIsInstance(metadata["description"], str)
                self.assertGreater(len(metadata["description"]), 0)
                self.assertLessEqual(len(metadata["description"]), 360)
                self.assertNotIn("§", metadata["description"])
                self.assertNotRegex(metadata["description"], r"\d,\d")
                self.assertNotIn("im Plugin", metadata["description"])
                self.assertEqual(re.findall(r"(?m)^#{1,3} ([1-6])\. ", parts[2]), list("123456"))
                for required in ("Times New Roman", "11 pt", "ausformuliert"):
                    self.assertIn(required, parts[2])
                self.assertNotRegex(parts[2], r"(?m)^#{1,6} .+\n[^\n]")

    def test_local_links_survive_plugin_packaging(self):
        for path in PLUGIN.rglob("*.md"):
            for target in re.findall(r"\]\(([^ )]+)\)", path.read_text(encoding="utf-8")):
                if target.startswith(("https:", "http:", "#", "mailto:")):
                    continue
                relative = unquote(target.split("#")[0]).strip("<>")
                if not relative:
                    continue
                destination = (path.parent / relative).resolve()
                # Die Benutzerübersicht darf in die Repository-Navigation verweisen.
                boundary = ROOT if path == PLUGIN / "README.md" else PLUGIN
                with self.subTest(file=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue(destination.is_relative_to(boundary.resolve()))
                    self.assertTrue(destination.exists(), str(destination))

    def test_prompt_pairs_limits_and_review_hashes(self):
        profile = json.loads((ROOT / "quality/evals" / f"{NAME}.json").read_text(encoding="utf-8"))
        for kind, key in zip(KINDS, ("workshop_review", "mini_review", "focus_review")):
            path = PLUGIN / f"{NAME}-{kind}.md"
            data = path.read_bytes()
            with self.subTest(prompt=kind):
                self.assertEqual(data, path.with_suffix(".txt").read_bytes())
                self.assertFalse(data.startswith(b"---\n"))
                if kind != "werkstatt":
                    self.assertLessEqual(len(data), 7500)
                    self.assertLessEqual(len(data.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")), 7500)
                self.assertEqual(profile[key]["prompt_sha256" if kind == "hauptproblem" else "sha256"], sha(path))
        self.assertEqual(profile["focus_review"]["skill_sha256"],
                         sha(PLUGIN / "skills/halluzinationspruefung-steuern/SKILL.md"))

    def test_renderer_comparison_detects_omissions_and_changed_identifiers(self):
        builder = module("build-ki-halluzinationsreduzierer-release.py")
        self.assertEqual(builder.words("Q- 001 F-002"), builder.words("Q-001 F-002"))
        self.assertNotEqual(builder.words("Q-001 F-002"), builder.words("Q-001 F-003"))
        self.assertNotEqual(builder.words("trägt nicht"), builder.words("trägt"))
        source = "Original https://amtlich.example.invalid/text_42 bleibt nicht ungeprüft."
        rendered = "Original https://amtlich.exam\nple.invalid/text_\n42 bleibt nicht ungeprüft."
        left, right = builder.prose_without_urls(source, rendered)
        self.assertEqual(builder.words(left), builder.words(right))
        with self.assertRaises(ValueError):
            builder.prose_without_urls(source, rendered.replace("42", "43"))
        left, right = builder.prose_without_urls(source, rendered.replace("nicht", ""))
        self.assertTrue(builder.words(left) - builder.words(right))

    def test_release_inventory_checksums_and_source_report(self):
        self.require_dist()
        names = expected_assets()
        self.assertEqual(len(names), 13)
        self.assertEqual({path.name for path in DIST.iterdir()}, names)
        checksums = {}
        for line in (DIST / "checksums-sha256.txt").read_text(encoding="utf-8").splitlines():
            digest, filename = line.split("  ", 1)
            self.assertRegex(digest, r"^[0-9a-f]{64}$")
            self.assertNotIn(filename, checksums)
            checksums[filename] = digest
        self.assertEqual(set(checksums), names - {"checksums-sha256.txt"})
        for filename, digest in checksums.items():
            self.assertEqual(sha(DIST / filename), digest, filename)
        report = json.loads((DIST / "quellenabgleich.json").read_text(encoding="utf-8"))
        self.assertEqual((report["schema_version"], report["plugin"], report["version"], report["tag"]),
                         (1, NAME, VERSION, f"{NAME}-v{VERSION}"))
        self.assertEqual(report["files"], {relative: sha(path) for relative, path in expected_sources().items()})
        expected_prompts = {f"{NAME}-{kind}.{extension}": sha(PLUGIN / f"{NAME}-{kind}.{extension}")
                            for kind in KINDS for extension in ("md", "txt")}
        self.assertEqual(report["prompts"], expected_prompts)
        for filename in expected_prompts:
            self.assertEqual((DIST / filename).read_bytes(), (PLUGIN / filename).read_bytes())

    def test_release_archives_are_exact_and_exclude_standalone_prompts(self):
        self.require_dist()
        sources = expected_sources()
        for suffix, prefix in (("", ""), ("-portable", NAME + "/")):
            with zipfile.ZipFile(DIST / f"{NAME}{suffix}.zip") as archive:
                self.assertIsNone(archive.testzip())
                self.assertEqual(len(archive.namelist()), len(sources))
                self.assertEqual(set(archive.namelist()), {prefix + relative for relative in sources})
                for relative, path in sources.items():
                    self.assertFalse(path.is_symlink())
                    self.assertEqual(archive.read(prefix + relative), path.read_bytes(), relative)
                for name in archive.namelist():
                    parts = Path(name).parts
                    self.assertNotIn("..", parts)
                    self.assertFalse(name.startswith("/"))
                    self.assertFalse(set(parts) & {"testakten", "testakte", "__pycache__", ".git"})
                    self.assertNotIn(Path(name).suffix.lower(), {".pdf", ".docx", ".xlsx", ".eml", ".pyc"})
                    self.assertFalse(any(Path(name).name.startswith(f"{NAME}-{kind}.") for kind in KINDS))
        validator = module("validate-release-zips.py")
        validator.validate_plugin_zip(DIST, NAME, VERSION)
        validator.validate_skill_sources(DIST / f"{NAME}.zip", PLUGIN)
        validator.validate_focus_skill(DIST / f"{NAME}.zip", PLUGIN,
                                       ROOT / "quality/evals" / f"{NAME}.json")

    def test_release_pdfs_text_glyphs_layout_fonts_and_source_coverage(self):
        self.require_dist()
        builder = module("build-ki-halluzinationsreduzierer-release.py")
        report = json.loads((DIST / "quellenabgleich.json").read_text(encoding="utf-8"))
        self.assertEqual(set(report["pdfs"]), {f"{NAME}-{kind}.pdf" for kind in KINDS})
        for kind in KINDS:
            source = PLUGIN / f"{NAME}-{kind}.md"
            target = DIST / f"{NAME}-{kind}.pdf"
            with self.subTest(pdf=target.name):
                metrics = builder.inspect_pdf(source, target)
                record = report["pdfs"][target.name]
                for key, value in metrics.items():
                    self.assertEqual(record[key], value)
                self.assertEqual(record["source_sha256"], sha(source))
                self.assertEqual(record["sha256"], sha(target))
                self.assertEqual(record["font_size"], 11)
                self.assertIn(record["font"], ("Times New Roman", "Liberation Serif (Ersatz für Times New Roman)"))
                self.assertEqual(len(PdfReader(target).pages), record["pages"])
                with pdfplumber.open(target) as document:
                    for page in document.pages:
                        for character in page.chars:
                            if character.get("text", "").strip():
                                self.assertTrue(any(part in character["fontname"] for part in
                                                    ("TimesNewRoman", "LiberationSerif")), character["fontname"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path)
    arguments, remaining = parser.parse_known_args()
    DIST = arguments.dist.resolve() if arguments.dist else None
    unittest.main(argv=[__file__, *remaining])
