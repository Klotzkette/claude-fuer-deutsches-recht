#!/usr/bin/env python3
"""Regressionen für Verzeichnisse, Downloadwege und Aktenhinweise."""

from __future__ import annotations

import importlib.util
import io
import json
import re
import tempfile
import unittest
from pathlib import Path
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

from testakte_disclaimer import NOTICE_DE, NOTICE_EN, NOTICE_MARKDOWN
from testakte_download_notices import (
    download_group_starts,
    download_readmes,
    ensure_download_notices,
    missing_notice_positions,
)

ROOT = Path(__file__).resolve().parent.parent


def load_script(filename: str):
    spec = importlib.util.spec_from_file_location(filename, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


NAV = load_script("validate-readme-navigation.py")
CASES = load_script("inject-gesamt-pdf-section.py")
PLUGINS = load_script("inject-direkt-loslegen-section.py")
ASSETS = load_script("generate-asset-index.py")
DOWNLOADS = load_script("validate-testakten-readme-downloads.py")


class DownloadNoticeTests(unittest.TestCase):
    table = (
        "| Format | Download |\n| --- | --- |\n"
        "| Gesamt-PDF | [PDF](gesamt-pdf/akte_gesamt.pdf) |\n"
        "| ZIP | [Originaldateien](testakte-akte.zip) |\n"
        "| ZIP | [Einzel-PDFs](testakte-akte-einzelpdfs.zip) |\n"
    )

    def errors(self, text):
        errors = []
        DOWNLOADS.validate_download_notices("README.md", text, errors)
        return errors

    def test_notice_has_unchanged_wording_in_two_blockquote_paragraphs(self):
        self.assertEqual(
            NOTICE_DE,
            "Diese Testakte wurde mit KI generiert und ist ein Experiment. "
            "Benutzung auf eigene Verantwortung und eigene Gefahr.",
        )
        self.assertEqual(
            NOTICE_EN,
            "This test case file was generated with AI and is an experiment. "
            "Use at your own responsibility and risk.",
        )
        self.assertEqual(NOTICE_MARKDOWN, f"> {NOTICE_DE}\n>\n> {NOTICE_EN}")

    def test_notice_must_immediately_precede_first_download_table(self):
        self.assertEqual(self.errors(NOTICE_MARKDOWN + "\n\n" + self.table), [])
        for text in (
            self.table,
            self.table + "\n" + NOTICE_MARKDOWN,
            NOTICE_MARKDOWN + "\n\nAllgemeine Erläuterung.\n\n" + self.table,
            NOTICE_MARKDOWN + "\n\n## Downloads\n\n" + self.table,
            self.table + "\n" + NOTICE_MARKDOWN + "\n\n" + self.table,
            f"> {NOTICE_DE}\n\n" + self.table,
            NOTICE_MARKDOWN.replace("eigene Gefahr", "Gefahr") + "\n\n" + self.table,
            self.table.replace("| Gesamt-PDF", "| " + NOTICE_MARKDOWN.replace("\n", " ")),
        ):
            with self.subTest(text=text):
                self.assertTrue(self.errors(text))

    def test_each_separate_download_group_needs_a_notice(self):
        text = NOTICE_MARKDOWN + "\n\n" + self.table + "\n## Weitere Akte\n\n" + self.table
        self.assertEqual(len(self.errors(text)), 1)
        updated = ensure_download_notices(text)
        self.assertEqual(updated.count(NOTICE_MARKDOWN), 2)
        self.assertEqual(self.errors(updated), [])
        self.assertEqual(ensure_download_notices(updated), updated)

    def test_html_and_markdown_download_groups(self):
        groups = (
            self.table,
            "[PDF](gesamt-pdf/akte_gesamt.pdf) · [ZIP](testakte-akte.zip)\n",
            '- [PDF](gesamt-pdf/akte_gesamt.pdf)\n- [ZIP](testakte-akte.zip)\n',
            '<p>\n<a href="alle-testakten.zip">Originalformate</a>\n<br>\n'
            '<a href="alle-testakten-einzelpdfs.zip">Einzel-PDFs</a>\n</p>\n',
            '> [Sammelpaket](alles-komplettpaket.zip)\n',
            '[PDF](<testakte/gesamt-pdf/testakte_gesamt.pdf> "Lesefassung")\n',
        )
        for group in groups:
            with self.subTest(group=group):
                text = "# Downloads\n\n" + group
                self.assertEqual(len(download_group_starts(text)), 1)
                updated = ensure_download_notices(text)
                self.assertIn(NOTICE_MARKDOWN + "\n\n" + group, updated)
                self.assertEqual(ensure_download_notices(updated), updated)
                self.assertEqual(self.errors(updated), [])

    def test_plugin_zips_navigation_and_code_are_not_case_downloads(self):
        text = (
            "[Plugin](mietrecht.zip) · [Übersicht](testakten/README.md)\n\n"
            "```md\n[Beispiel](testakte-akte.zip)\n```\n\n"
            "~~~html\n<a href='alle-testakten.zip'>Beispiel</a>\n~~~\n"
        )
        self.assertEqual(download_group_starts(text), [])
        self.assertEqual(ensure_download_notices(text), text)

    def test_local_case_pdf_gets_notice_but_external_source_pdf_does_not(self):
        text = "[Brief](01_brief.pdf)\n\n[Quelle](https://example.org/entscheidung.pdf)\n"
        self.assertEqual(len(missing_notice_positions(text, case_readme=True)), 1)
        self.assertEqual(missing_notice_positions(text), [])

    def test_heading_without_blank_line_does_not_swallow_warning(self):
        text = "## Downloads\n" + self.table
        updated = ensure_download_notices(text)
        self.assertTrue(updated.startswith("## Downloads\n\n" + NOTICE_MARKDOWN))
        self.assertEqual(self.errors(updated), [])
        self.assertEqual(ensure_download_notices(updated), updated)

    def test_case_generator_preserves_notice_position_for_all_formats(self):
        for pdf in (None, "gesamt-pdf/akte_gesamt.pdf"):
            for individual in (False, True):
                with self.subTest(pdf=pdf, individual=individual):
                    text = CASES.section_block("akte", pdf, individual)
                    self.assertEqual(text.count(NOTICE_MARKDOWN), 1)
                    self.assertIn(NOTICE_MARKDOWN + "\n\n| Was |", text)
                    self.assertEqual(self.errors(text), [])

    def test_case_injection_is_idempotent_and_covers_older_links(self):
        with tempfile.TemporaryDirectory() as directory:
            readme = Path(directory) / "README.md"
            original = "## Bisheriger Download\n\n[ZIP](testakte-akte.zip)\n"
            readme.write_text("# Akte\n\n" + original, encoding="utf-8")
            with patch.object(CASES, "expected_arcnames", return_value=["brief.pdf"]):
                self.assertEqual(CASES.inject(readme, "akte"), "inserted")
                first = readme.read_text(encoding="utf-8")
                self.assertEqual(CASES.inject(readme, "akte"), "unchanged")
            self.assertEqual(readme.read_text(encoding="utf-8"), first)
            self.assertEqual(first.count(NOTICE_MARKDOWN), 2)
            self.assertEqual(self.errors(first), [])
            self.assertIn("[ZIP](testakte-akte.zip)", first)

    def test_plugin_generator_covers_assigned_local_and_collection_downloads(self):
        directory = ROOT / "mietrecht"
        plugin = {"name": "mietrecht", "description": "Mietrecht"}
        for local, slugs in ((False, []), (False, ["akte"]), (True, [])):
            with self.subTest(local=local, slugs=slugs), patch.object(
                PLUGINS, "has_plugin_local_testakte", return_value=local
            ):
                text = PLUGINS.block(plugin, directory, slugs, 1)
                self.assertIn(NOTICE_MARKDOWN, text)
                self.assertEqual(self.errors(text), [])

    def test_asset_index_generator_is_idempotent_and_warns_before_collection_table(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".claude-plugin").mkdir()
            (root / ".claude-plugin/marketplace.json").write_text(
                json.dumps({"version": "1.0.0", "plugins": []}), encoding="utf-8"
            )
            with patch.object(ASSETS, "REPO", root):
                ASSETS.main()
                first = (root / "ASSET_INDEX.md").read_text(encoding="utf-8")
                ASSETS.main()
            self.assertEqual((root / "ASSET_INDEX.md").read_text(encoding="utf-8"), first)
            self.assertIn(NOTICE_MARKDOWN + "\n\n| Asset |", first)
            self.assertEqual(self.errors(first), [])

    def test_readme_inventory_includes_all_required_download_surfaces(self):
        paths = set(download_readmes(ROOT))
        for relative in (
            "README.md", "ASSET_INDEX.md", "testakten/README.md", "mietrecht/README.md",
            "gerichtsplugins/richter-landgericht-strafkammer/README.md",
            "arbeitszeugnispruefer/testakte/arbeitszeugnis-analyse-bluehendes-leben/README.md",
        ):
            self.assertIn(ROOT / relative, paths)

    def test_validator_main_rejects_missing_notices_on_every_surface(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            case = root / "testakten/akte"
            case.mkdir(parents=True)
            (root / "plugin").mkdir()
            (root / ".claude-plugin").mkdir()
            (root / ".claude-plugin/marketplace.json").write_text(
                json.dumps({"plugins": [{"source": "./plugin"}]}), encoding="utf-8"
            )
            overview = ensure_download_notices(
                "| Akte | Download |\n| --- | --- |\n"
                "| Akte | [PDF](./akte/gesamt-pdf/akte_gesamt.pdf) "
                f"· [ZIP]({DOWNLOADS.release_url('akte')}) "
                f"· [Einzel-PDFs]({DOWNLOADS.release_url('akte', '-einzelpdfs')}) |\n"
            )
            files = {
                "README.md": ensure_download_notices(self.table),
                "ASSET_INDEX.md": ensure_download_notices(self.table),
                "plugin/README.md": ensure_download_notices(self.table),
                "testakten/README.md": overview,
                "testakten/akte/README.md": CASES.section_block("akte", "gesamt-pdf/akte_gesamt.pdf", True),
            }
            for relative, text in files.items():
                (root / relative).write_text(text, encoding="utf-8")
            with patch.object(DOWNLOADS, "ROOT", root), patch.object(
                DOWNLOADS, "TESTAKTEN", root / "testakten"
            ), patch.object(DOWNLOADS, "OVERVIEW", root / "testakten/README.md"):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(DOWNLOADS.main(), 0)
                for relative, text in files.items():
                    with self.subTest(readme=relative):
                        (root / relative).write_text(text.replace(NOTICE_MARKDOWN, ""), encoding="utf-8")
                        messages = io.StringIO()
                        with redirect_stderr(messages):
                            self.assertEqual(DOWNLOADS.main(), 1)
                        self.assertIn("unmittelbar vor Downloadgruppe", messages.getvalue())
                        (root / relative).write_text(text, encoding="utf-8")

    def test_new_case_readme_is_discovered_without_a_hardcoded_list(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = root / "testakten/steuerrecht-bwa-vergleich-nuernberg/README.md"
            readme.parent.mkdir(parents=True)
            readme.write_text("# BWA-Vergleich\n", encoding="utf-8")
            self.assertIn(readme, download_readmes(root))


class NavigationTests(unittest.TestCase):
    def test_curated_and_start_guides_use_checked_downloads(self):
        checked = set(NAV.user_facing_download_docs())
        for filename in ("PROMPTLISTE.md", "QUICKSTART.md", "INSTALLATION_EINFACH.md"):
            self.assertIn(ROOT / filename, checked)

    def test_shared_anchor_target_is_read_once(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "README.md").write_text(
                "# Start\n\n[A](guide.md#überblick) · [B](guide.md#überblick-1)\n",
                encoding="utf-8",
            )
            (root / "guide.md").write_text(
                "# Überblick\n\n## Überblick\n", encoding="utf-8"
            )
            with patch.object(NAV, "REPO", root), patch.object(
                NAV, "heading_anchors", wraps=NAV.heading_anchors
            ) as read_anchors:
                errors = []
                self.assertEqual(NAV.validate_markdown_links(errors), (2, 2))
                self.assertEqual(errors, [])
                self.assertEqual(read_anchors.call_count, 1)

    def test_case_format_count_matches_available_downloads(self):
        two = CASES.section_block("akte", "gesamt.pdf", False)
        three = CASES.section_block("akte", "gesamt.pdf", True)
        self.assertIn("zwei Formaten", two)
        self.assertNotIn("Einzel-PDF-ZIP", two)
        self.assertIn("drei Formaten", three)
        self.assertIn("Einzel-PDF-ZIP", three)
        self.assertIn("English:", three)
        self.assertIn("zuletzt veröffentlichten Release", three)

    def test_curated_inventory_and_category_counts(self):
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        plugins = {entry["name"]: entry["source"].removeprefix("./") for entry in market["plugins"]}
        text = (ROOT / "PROMPTLISTE.md").read_text(encoding="utf-8")
        sections = re.split(r"^## (.+)$", text, flags=re.MULTILINE)
        categories = {}
        listed = []
        for heading, body in zip(sections[1::2], sections[2::2]):
            entries = re.findall(r"^- \[([a-z0-9-]+)\]\((https://[^)]+/tree/main/[^)]+)\):", body, re.MULTILINE)
            if not entries:
                continue
            names = [name for name, _ in entries]
            self.assertEqual(names, sorted(names), heading)
            categories[heading] = len(names)
            for name, url in entries:
                self.assertIn(name, plugins)
                self.assertTrue(url.endswith("/tree/main/" + plugins[name]), name)
            listed.extend(names)
        self.assertEqual(list(categories), sorted(categories, key=str.casefold))
        self.assertEqual(len(listed), len(set(listed)))
        counts = re.findall(r"^\| \[([^]]+)\]\(#[^)]+\) \| (\d+) \|$", text, re.MULTILINE)
        self.assertEqual({title: int(count) for title, count in counts}, categories)
        self.assertIn(f"{len(listed)} kuratierte Plugins in {len(categories)} Kategorien", text)
        self.assertIn(f"insgesamt {len(plugins)} Marketplace-Plugins", text)

    def test_no_obsolete_quickstart_skill_in_plugin_readmes(self):
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        for plugin in market["plugins"]:
            text = (ROOT / plugin["source"] / "README.md").read_text(encoding="utf-8")
            self.assertNotIn("inklusive Schnellstart-Skill", text, plugin["name"])


if __name__ == "__main__":
    unittest.main()
