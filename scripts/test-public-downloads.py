#!/usr/bin/env python3
"""Offline-Regressionen für öffentlich sichtbare Release-Downloads."""

import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

SPEC = importlib.util.spec_from_file_location("public_downloads", Path(__file__).with_name("validate-public-downloads.py"))
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)
PUBLIC = {"id": 123, "draft": False, "published_at": "2026-10-02T12:00:00Z", "tag_name": "akten-v1.0.0"}


class PublicDownloadTests(unittest.TestCase):
    def test_links_include_html_latest_pinned_and_deduplicate(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "README.md"
            base = CHECK.RELEASE_BASE
            path.write_text(
                f'[ZIP]({base}/download/akten-v1.0.0/fall.zip)\n'
                f'<a href="{base}/download/akten-v1.0.0/fall.zip" download>ZIP</a>\n'
                f'[Andere]({base}/latest/download/plan%20neu.xlsx)\n'
                '[Fremd](https://example.org/releases/latest/download/file.zip)\n', encoding="utf-8",
            )
            links = CHECK.release_links([path])
        self.assertEqual(set(links), {("akten-v1.0.0", "fall.zip"), ("latest", "plan neu.xlsx")})
        self.assertEqual(len(links["akten-v1.0.0", "fall.zip"]), 2)

    def test_draft_and_unpublished_release_fail_before_assets(self):
        for release in ({**PUBLIC, "draft": True}, {**PUBLIC, "published_at": None}, {}):
            with self.subTest(release=release), patch.object(CHECK, "public_json", return_value=release) as api:
                with self.assertRaisesRegex(ValueError, "nicht als veröffentlicht"):
                    CHECK.public_assets("akten-v1.0.0")
                self.assertEqual(api.call_count, 1)

    def test_wrong_tag_fails(self):
        with patch.object(CHECK, "public_json", return_value=PUBLIC):
            with self.assertRaisesRegex(ValueError, "Tag stimmt nicht"):
                CHECK.public_assets("akten-v2.0.0")

    def test_all_asset_pages_are_read(self):
        batch = [{"name": f"fall-{i}.zip"} for i in range(100)]
        with patch.object(CHECK, "public_json", side_effect=[PUBLIC, batch, [{"name": "last.zip"}]]) as api:
            self.assertEqual(len(CHECK.public_assets("akten-v1.0.0")), 101)
            self.assertIn("page=2", api.call_args.args[0])

    def test_duplicate_assets_fail(self):
        with patch.object(CHECK, "public_json", side_effect=[PUBLIC, [{"name": "a.zip"}, {"name": "a.zip"}]]):
            with self.assertRaisesRegex(ValueError, "Doppeltes Asset"):
                CHECK.public_assets("akten-v1.0.0")

    def test_latest_uses_public_latest_endpoint(self):
        with patch.object(CHECK, "public_json", side_effect=[PUBLIC, []]) as api:
            self.assertEqual(CHECK.public_assets("latest"), {})
            self.assertEqual(api.call_args_list[0].args[0], "releases/latest")

    def test_each_release_is_loaded_once_and_bad_assets_fail(self):
        links = {("latest", name): ["README.md:1"] for name in ("ok.zip", "missing.zip", "empty.zip", "pending.zip")}
        assets = {"ok.zip": {"size": 100, "state": "uploaded"}, "empty.zip": {"size": 0, "state": "uploaded"}, "pending.zip": {"size": 100, "state": "new"}}
        with patch.object(CHECK, "public_assets", return_value=assets) as api:
            errors = CHECK.validate(links)
            api.assert_called_once_with("latest")
        self.assertEqual(len(errors), 3)
        self.assertFalse(any("ok.zip" in error for error in errors))

    def test_api_failure_is_not_success_or_false_missing_asset(self):
        with patch.object(CHECK, "public_assets", side_effect=ValueError("API-Limit")):
            errors = CHECK.validate({("latest", "a.zip"): ["README.md:1"]})
        self.assertIn("API-Limit", errors[0])
        self.assertNotIn("Datei fehlt", errors[0])

    def test_api_is_anonymous_and_timeout_bounded(self):
        with patch.object(CHECK, "urlopen", return_value=io.BytesIO(b'{"ok": true}')) as opened:
            self.assertEqual(CHECK.public_json("releases/latest"), {"ok": True})
            request = opened.call_args.args[0]
            self.assertFalse(request.has_header("Authorization"))
            self.assertEqual(opened.call_args.kwargs["timeout"], 20)

    def test_404_and_api_limit_have_distinct_errors(self):
        for code, message in ((404, "Entwurf"), (403, "API-Limit"), (429, "API-Limit")):
            with self.subTest(code=code), patch.object(CHECK, "urlopen", side_effect=HTTPError("https://api.github.com", code, "error", {}, None)):
                with self.assertRaisesRegex(ValueError, message):
                    CHECK.public_json("releases/latest")


if __name__ == "__main__":
    unittest.main()
