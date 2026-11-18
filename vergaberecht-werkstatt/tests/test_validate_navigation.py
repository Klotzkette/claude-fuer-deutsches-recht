from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
SCRIPT = ROOT / "scripts" / "validate-navigation.py"
SPEC = importlib.util.spec_from_file_location("validate_navigation", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
navigation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(navigation)


class NavigationParserTests(unittest.TestCase):
    def test_only_navigable_markdown_links_are_returned(self) -> None:
        text = """
[Direkt](./01_akte.md "Aktenstück")
[Fragment](02_akte.md#fundstelle)
[Kodiert](<03%5Fakte.md>)
![Bild](04_akte.md)
<!-- [Kommentar](05_akte.md) -->

```markdown
[Codebeispiel](06_akte.md)
```
"""

        self.assertEqual(
            navigation.markdown_link_targets(text),
            {"./01_akte.md", "02_akte.md", "03_akte.md"},
        )

    def test_numbered_case_docs_accepts_more_than_two_digits(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            for name in ("01_start.md", "99_fortsetzung.md", "100_anlage.md", "README.md"):
                (directory / name).touch()

            self.assertEqual(
                [path.name for path in navigation.numbered_case_docs(directory)],
                ["01_start.md", "99_fortsetzung.md", "100_anlage.md"],
            )

    def test_component_assets_keep_source_edition_while_plugins_use_individual_pins(self):
        source = json.loads((ROOT / "source-import.json").read_text())
        self.assertEqual(navigation.RELEASE_TAG, source["release"])
        role = "bieter-unternehmen"
        current = f"https://github.com/{navigation.REPOSITORY}/releases/download/fachrunde-v9.8.7/{role}.zip"
        with patch.object(navigation, "plugin_download", return_value=current) as resolver:
            self.assertEqual(navigation.asset_download(f"{role}.zip"), current)
            resolver.assert_called_once_with(role)
            for asset in ("alle-skills-markdown.zip", "bieter-unternehmen-unified-mini-prompt.md",
                          "testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung.zip"):
                self.assertEqual(navigation.asset_download(asset), f"{navigation.RELEASE_BASE}/{asset}")
            resolver.assert_called_once_with(role)

    def test_source_edition_rejects_foreign_tag_duplicate_cases_or_missing_role(self):
        source = json.loads((ROOT / "source-import.json").read_text())
        for change in ({"release": "beliebiges-release-v9.8.7"},
                       {"cases": [source["cases"][0]] * 2},
                       {"plugins": source["plugins"][:-1]}):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as temp:
                directory = Path(temp)
                (directory / "source-import.json").write_text(json.dumps({**source, **change}))
                with self.assertRaises(ValueError):
                    navigation.component_release(directory)

    def test_code_and_comments_do_not_satisfy_release_download_coverage(self):
        url = navigation.asset_download("alle-skills-markdown.zip")
        text = f"<!-- [Versteckt]({url}) -->\n\n```markdown\n[Beispiel]({url})\n```\n"
        self.assertEqual(navigation.linked_release_assets(text), set())

    def test_wrong_release_tag_is_rejected_even_with_a_correct_link_present(self):
        original = (ROOT / "README.md").read_text()
        expected = navigation.expected_assets(navigation.plugin_names(), navigation.testakten_slugs())
        for asset in ("bieter-unternehmen.zip", "alle-skills-markdown.zip",
                      "testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung.zip"):
            wrong = f"https://github.com/{navigation.REPOSITORY}/releases/download/fremd-v0.0.1/{asset}"
            with self.subTest(asset=asset), tempfile.TemporaryDirectory() as temp:
                directory = Path(temp)
                (directory / "README.md").write_text(original + f"\n[Falsche Fassung]({wrong})\n")
                errors = []
                with patch.object(navigation, "REPO", directory):
                    navigation.validate_root(expected, errors)
                self.assertTrue(any("abweichendes Releaseziel" in error and wrong in error for error in errors), errors)

    def test_central_case_namesake_cannot_replace_nested_component_edition(self):
        asset = "testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung.zip"
        canonical = navigation.asset_download(asset)
        central = f"https://github.com/{navigation.REPOSITORY}/releases/download/grundakten-sammlung-v1.0.0/{asset}"
        text = (ROOT / "README.md").read_text().replace(canonical, central)
        expected = navigation.expected_assets(navigation.plugin_names(), navigation.testakten_slugs())
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            (directory / "README.md").write_text(text)
            errors = []
            with patch.object(navigation, "REPO", directory):
                navigation.validate_root(expected, errors)
            self.assertTrue(any("kanonischer Download fehlt" in error and asset in error for error in errors), errors)
            self.assertTrue(any("abweichendes Releaseziel" in error and central in error for error in errors), errors)

    def test_live_check_keeps_exact_historical_inventory_and_checks_current_plugins(self):
        expected = navigation.expected_assets(navigation.plugin_names(), navigation.testakten_slugs())
        latest_tag = "fachrunde-v9.8.7"
        latest = {f"{role}.zip" for role in navigation.PROMPT_SUFFIXES} | {"anderes-plugin.zip"}

        def download(role):
            return f"https://github.com/{navigation.REPOSITORY}/releases/download/{latest_tag}/{role}.zip"

        def names(tag, errors):
            return set(expected) if tag == navigation.RELEASE_TAG else set(latest)

        with patch.object(navigation, "plugin_download", side_effect=download), \
                patch.object(navigation, "live_asset_names", side_effect=names) as remote:
            errors = []
            navigation.validate_live_assets(expected, errors)
            self.assertEqual(errors, [])
            self.assertEqual({call.args[0] for call in remote.call_args_list}, {navigation.RELEASE_TAG, latest_tag})
            latest.remove("bieter-unternehmen.zip")
            navigation.validate_live_assets(expected, errors)
            self.assertTrue(any("Plugin-Nachfolger" in error and "bieter-unternehmen.zip" in error for error in errors), errors)

        with patch.object(navigation, "live_asset_names", return_value=expected | {"fremde-datei.zip"}):
            errors = []
            navigation.validate_live_assets(expected, errors)
            self.assertTrue(any("unerwartete Datei: fremde-datei.zip" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
