from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from public_release import canonical_prompt, compact_mini, markdown_download, with_working_downloads
from public_release import REPOSITORY
from testakte_notices import MARKDOWN_WARNING, WARNING, README_NOTICE, with_case_warnings

spec = importlib.util.spec_from_file_location("case_zips", ROOT / "scripts/build-testakten-release-zips.py")
case_zips = importlib.util.module_from_spec(spec)
spec.loader.exec_module(case_zips)

spec = importlib.util.spec_from_file_location("public_validation", ROOT / "scripts/validate-public-integration.py")
public_validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(public_validation)


class PublicIntegrationTests(unittest.TestCase):
    def test_declared_shared_case_readme_requires_existing_file(self):
        relative = "testakten/ki-register-havelgrund-sozialamt/README.md"
        target = f"https://github.com/{REPOSITORY}/blob/main/{relative}"
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            self.assertIsNotNone(public_validation.public_target_error(target, parent_root=parent))
            path = parent / relative
            path.parent.mkdir(parents=True)
            path.write_text("# Gemeinsame Testakte\n", encoding="utf-8")
            self.assertIsNone(public_validation.public_target_error(target, parent_root=parent))

    def test_undeclared_cross_component_file_is_rejected_even_if_it_exists(self):
        relative = "testakten/andere-akte/README.md"
        target = f"https://github.com/{REPOSITORY}/blob/main/{relative}"
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            path = parent / relative
            path.parent.mkdir(parents=True)
            path.write_text("# Andere Testakte\n", encoding="utf-8")
            self.assertIsNotNone(public_validation.public_target_error(target, parent_root=parent))

    def test_shared_case_exception_does_not_allow_other_files_or_url_variants(self):
        base = f"https://github.com/{REPOSITORY}/blob/main/"
        allowed = "testakten/ki-register-havelgrund-sozialamt/README.md"
        targets = [
            base + allowed.replace("README.md", "13_Ereignisse.xlsx"),
            base + allowed + "?download=1",
            base.replace("/blob/", "/tree/") + allowed,
            f"https://raw.githubusercontent.com/{REPOSITORY}/main/{allowed}",
        ]
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            path = parent / allowed
            path.parent.mkdir(parents=True)
            path.write_text("# Gemeinsame Testakte\n", encoding="utf-8")
            for target in targets:
                with self.subTest(target=target):
                    self.assertIsNotNone(public_validation.public_target_error(target, parent_root=parent))

    def test_working_downloads_leave_navigation_and_code_unchanged(self):
        destination = "skills/example/SKILL.md"
        link = f"[Skill]({destination})"
        text = f"# Rolle\n\n{link}\n\n[Navigation](../README.md)\n\n```md\n{link}\n```\n"
        document = ROOT / "bieter-unternehmen/README.md"
        result = with_working_downloads(text, document)
        self.assertIn(markdown_download("bieter-unternehmen/" + destination), result)
        self.assertIn("[Navigation](../README.md)", result)
        self.assertIn(f"```md\n{link}\n```", result)

    def test_canonical_headings_keep_subordinate_hierarchy(self):
        text = "# Titel\n\n## Auftrag\n\n### 1. Start\n\n### 1.1 Detail\n\n### 2. Ende\n\n## Kontrolle\n"
        result = canonical_prompt(text)
        self.assertIn("## 1. Auftrag", result)
        self.assertIn("### 1.1. Start", result)
        self.assertIn("#### 1.1.1. Detail", result)
        self.assertIn("### 1.2. Ende", result)
        self.assertIn("## 2. Kontrolle", result)
        self.assertEqual(canonical_prompt(result), result)

    def test_canonical_normalization_keeps_technical_literals(self):
        text = "# Titel\n\n## Phase A: Start\n\n`Claude-Skill/path`\n\n```text\n## Technical heading\n```\n"
        result = canonical_prompt(text)
        self.assertIn("`Claude-Skill/path`", result)
        self.assertIn("## Technical heading", result)
        self.assertIn("## 1. Start", result)

    def test_mini_only_removes_table_padding(self):
        text = "# Titel\n\n" + "| A | B |\n" * 800
        compact = compact_mini(text)
        self.assertLessEqual(len(compact.encode("utf-8")), 7500)
        self.assertEqual(text.replace(" ", ""), compact.replace(" ", ""))
        self.assertEqual(compact_mini(compact), compact)

    def test_mini_enforces_bytes_not_characters(self):
        with self.assertRaises(ValueError):
            compact_mini("\u00e4" * 4000)

    def test_warning_immediately_before_each_download_group(self):
        table = "| Datei | Link |\n|---|---|\n| Akte | [PDF](gesamt-pdf/akte.pdf) |"
        link = "[ZIP](https://example.org/testakte-fall.zip)"
        original = "# Akte\n\n" + table + "\n\n## Weitere Dateien\n\n" + link + "\n"
        result = with_case_warnings(original)
        self.assertIn(MARKDOWN_WARNING + "\n\n" + table, result)
        self.assertIn(MARKDOWN_WARNING + "\n\n" + link, result)
        self.assertEqual(result.count(WARNING.split("\n")[0]), 2)
        self.assertEqual(with_case_warnings(result), result)

    def test_plugin_zip_is_not_a_case_download(self):
        text = "[Plugin](https://example.org/bieter-unternehmen.zip)\n"
        self.assertEqual(with_case_warnings(text), text)

    def test_generated_block_does_not_accumulate_notices(self):
        block = "<!-- BEGIN downloads -->\n[PDF](akte.pdf)\n"
        text = (MARKDOWN_WARNING + "\n\n") * 2 + block
        expected = MARKDOWN_WARNING + "\n\n" + block
        self.assertEqual(with_case_warnings(text), expected)
        self.assertEqual(with_case_warnings(expected), expected)

    def test_working_zip_is_flat_and_excludes_internal_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            case = root / "fall"
            (case / "docx").mkdir(parents=True)
            (case / "docx/01_akte.docx").write_bytes(b"work")
            (case / "docx/02_solution.docx").write_bytes(b"internal")
            (case / "01_fragment.md").write_text("source")
            (case / "rubric.yaml").write_text("internal")
            (case / "gesamt-pdf").mkdir()
            (case / "gesamt-pdf/fall_gesamt.pdf").write_bytes(b"overall")
            path, _ = case_zips.build_single(case, root / "dist")
            first = path.read_bytes()
            case_zips.build_single(case, root / "dist")
            self.assertEqual(path.read_bytes(), first)
            with zipfile.ZipFile(path) as archive:
                self.assertEqual(archive.namelist()[0], "README.txt")
                self.assertEqual(set(archive.namelist()), {"01_akte.docx", "README.txt"})
                self.assertTrue(archive.read("README.txt").decode("utf-8").startswith(README_NOTICE))

    def test_internal_files_alone_do_not_make_a_working_zip(self):
        with tempfile.TemporaryDirectory() as directory:
            case = Path(directory)
            (case / "docx").mkdir()
            (case / "docx/solution.docx").touch()
            with self.assertRaises(RuntimeError):
                case_zips.testakte_members(case)


if __name__ == "__main__":
    unittest.main()
