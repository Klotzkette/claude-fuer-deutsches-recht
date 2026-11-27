#!/usr/bin/env python3
"""Prüft den amtlichen Beleg in den tatsächlich ausgelieferten Paketvarianten."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile

from activate_quality_release import BUILDER, QUELLEN_TAG, ROOT, metadata_changes
from package_edition import EDITION


class Quellenpakete(unittest.TestCase):
    def test_downloads_und_portable_aktivierung(self):
        scope = json.loads((ROOT / f"scripts/data/{QUELLEN_TAG}-scope.json").read_bytes())
        judge = "richter-verwaltungsgericht"
        office = "ki-native-kanzlei"
        prompt = judge + "-werkstatt.md"
        official = b"https://www.bverwg.de/141026B7VR4.26.0"
        files = {
            judge + ".zip": ("", (
                "skills/juristischer-argumentationskern/SKILL.md",
                "skills/prozessuale-kniffe-und-rechtsprechungsanker/SKILL.md",
                "references/hauptworkflow-fachpruefung.md",
            )),
            office + ".zip": ("", ("references/repository/references/leitentscheidungen-anker.md",)),
            office + "-portable.zip": (office + "/", ("references/repository/references/leitentscheidungen-anker.md",)),
        }
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "ausgabe"
            report = BUILDER.build(output, scope, ROOT)
            self.assertEqual(report, BUILDER.validate_assets(output, scope, ROOT))
            self.assertEqual({p.name for p in output.iterdir()}, set(files) | {prompt, BUILDER.CHECKSUMS, BUILDER.REPORT})
            self.assertIn(official, (output / prompt).read_bytes())
            for name, (prefix, members) in files.items():
                with ZipFile(output / name) as package:
                    manifest = json.loads(package.read(prefix + ".claude-plugin/plugin.json"))
                    self.assertEqual(manifest["version"], scope["version"])
                    for member in members:
                        text = package.read(prefix + member)
                        self.assertIn(official, text)
                        self.assertNotIn(b"WBRE202600612.zip", text)

            updates = metadata_changes(ROOT, scope, report)
            edition = json.loads(updates[ROOT / f"scripts/data/{EDITION}.json"])
            for asset in files:
                self.assertEqual(edition["nachfolger"][asset]["tag"], QUELLEN_TAG)
            self.assertNotIn(ROOT / "gerichtsplugins/.claude-plugin/marketplace.json", updates)
            entries = json.loads(updates[ROOT / ".claude-plugin/marketplace.json"])["plugins"]
            self.assertEqual({e["name"] for e in entries if e["version"] == scope["version"]}, {judge, office})

            invalid = deepcopy(report)
            portable = invalid["plugins"][office]["archives"][office + "-portable.zip"]
            portable[office + "/.codex-plugin/plugin.json"] = "0" * 64
            with self.assertRaisesRegex(ValueError, "Manifest"):
                metadata_changes(ROOT, scope, invalid)


if __name__ == "__main__":
    unittest.main()
