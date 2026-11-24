#!/usr/bin/env python3
"""Prüft den Übergang von den publizierten Insolvenzaktensätzen zu ihren neuen Originalarchiven."""
import hashlib
import importlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from release_routing import RELEASE_BASE


A = importlib.import_module("activate-insolvenz-arbeitsvorlagen")
SLUG = "starug-schutzschirm-grossbach-druckguss-erfurt"
LIFE = f"lebensakte-{SLUG}.zip"
ORIGINAL = f"testakte-{SLUG}.zip"
OLD = "grundakten-sammlung-v1.0.0"


class Aktivierung(unittest.TestCase):
    def test_nur_die_beiden_vollarchive_und_aktuelle_kataloge(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(["git", "init", "--quiet"], cwd=root, check=True)
            route_file = root / "scripts/scoped-release-assets.json"
            route_file.parent.mkdir()
            pdf = f"testakte-{SLUG}-einzelpdfs.zip"
            route_file.write_text(json.dumps({"schema_version": 1, "assets": {pdf: "akten-v1.0.0", ORIGINAL: OLD}}))
            paths = ("testakten/fall/README.md", "docs/grundakten-lebenswelt/Fachakten.md",
                     "docs/releases/historisch.md", "quality/archiv/README.md")
            text = "\n".join(f"{RELEASE_BASE}/download/{tag}/{asset}" for tag, asset in (
                (A.FACHTAG, LIFE), (OLD, ORIGINAL), ("akten-v1.0.0", pdf), (A.FACHTAG, f"druckakte-{SLUG}.zip")))
            for name in paths:
                file = root / name
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text(text)
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            sources = {LIFE: {"tag": A.FACHTAG}, ORIGINAL: {"tag": OLD}}
            self.assertEqual(A.activate_verified(root, sources), 3)
            self.assertEqual(A.activate_verified(root, sources), 0)
            expected = text.replace(f"/{A.FACHTAG}/{LIFE}", f"/{A.TAG}/{LIFE}").replace(
                f"/{OLD}/{ORIGINAL}", f"/{A.TAG}/{ORIGINAL}")
            for path in paths[:2]:
                self.assertEqual((root / path).read_text(), expected)
            for path in paths[2:]:
                self.assertEqual((root / path).read_text(), text)
            pins = json.loads(route_file.read_bytes())
            self.assertEqual(pins["assets"], {pdf: "akten-v1.0.0", ORIGINAL: A.TAG, LIFE: A.TAG})
            pins["assets"][ORIGINAL] = "andere-ausgabe-v2.0.0"
            route_file.write_text(json.dumps(pins))
            with self.assertRaisesRegex(ValueError, "überschreiben"):
                A.activate_verified(root, sources)

    def test_falscher_commit_und_download_integritaet(self):
        public = importlib.import_module("validate-public-downloads")
        publisher = importlib.import_module("publish-release-assets")
        data = b"synthetischer Testbestand"
        name = "arbeitsakte-fiktiv.zip"
        asset = {"state": "uploaded", "size": len(data), "digest": "sha256:" + hashlib.sha256(data).hexdigest()}
        with tempfile.TemporaryDirectory() as temporary, patch.object(public, "public_assets", return_value={name: asset}), \
                patch.object(publisher, "tag_commit", return_value="a" * 40), \
                patch.object(A, "urlopen", side_effect=lambda *_args, **_kwargs: io.BytesIO(data)) as download:
            out = Path(temporary)
            with self.assertRaisesRegex(ValueError, "Quellcommit"):
                A.public_files(out, {name}, "b" * 40)
            download.assert_not_called()
            A.public_files(out, {name}, "a" * 40)
            self.assertEqual((out / name).read_bytes(), data)
            asset["digest"] = "sha256:" + "0" * 64
            with self.assertRaisesRegex(ValueError, "GitHub-Metadaten"):
                A.public_files(out, {name}, "a" * 40)


if __name__ == "__main__":
    unittest.main()
