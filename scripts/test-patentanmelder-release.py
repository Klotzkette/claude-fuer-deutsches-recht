#!/usr/bin/env python3
"""Prüft den realen Inhalt der installierbaren Patentrechtsausgabe und der beiden Einzelprompts."""
import json
from pathlib import Path
import re
import tempfile
import unittest
from zipfile import ZipFile

from activate_quality_release import BUILDER, ROOT, SOURCES, metadata_changes
from package_edition import EDITION
from release_routing import RELEASE_BASE

TAG = "qualitaetsrunde-v445.36.14"
SOURCE = SOURCES[TAG]
CASES = ("01-moebel-schnappfuss", "02-gewaechshaus-beschattung", "03-fruchtkisten-pruefstand")
PROMPTS = {"patentrecht-schnellstart.md", "patentrecht-werkstatt.md"}


class PatentanmelderReleaseTests(unittest.TestCase):
    def test_ausgabe_und_aktivierung(self):
        scope = json.loads((ROOT / f"scripts/data/{TAG}-scope.json").read_bytes())
        with tempfile.TemporaryDirectory() as temporary:
            dist = Path(temporary) / "ausgabe"
            report = BUILDER.build(dist, scope, ROOT)
            self.assertEqual({file.name for file in dist.iterdir()},
                             PROMPTS | {"patentrecht.zip", BUILDER.CHECKSUMS, BUILDER.REPORT})
            for prompt in PROMPTS:
                self.assertEqual((dist / prompt).read_bytes(), (ROOT / SOURCE / prompt).read_bytes())
            with ZipFile(dist / "patentrecht.zip") as archive:
                names = set(archive.namelist())
                self.assertEqual(10, sum(bool(re.fullmatch(r"skills/[^/]+/SKILL\.md", n)) for n in names))
                self.assertFalse(names & PROMPTS)
                self.assertEqual("445.36.14", json.loads(archive.read(".claude-plugin/plugin.json"))["version"])
                readme = archive.read("README.md").decode()
                for asset in PROMPTS | {"patentrecht.zip"}:
                    self.assertIn(f"{RELEASE_BASE}/download/{TAG}/{asset}", readme)
                self.assertNotIn(f"{EDITION}-v445.36.9/patentrecht.zip", readme)
                suite = archive.read("Patentanmelder/README.md").decode()
                commit = report["source_state"]["commit"]
                self.assertIn(f"/{commit}/docs/downloads/patentanmelder-werkstatt-testakten.zip", suite)
                for slug in CASES:
                    base = Path("Patentanmelder") / slug
                    files = [path for path in (ROOT / SOURCE / base).rglob("*") if path.is_file()]
                    included = {path.relative_to(ROOT / SOURCE).as_posix() for path in files}
                    self.assertEqual({name for name in names if name.startswith(base.as_posix() + "/")}, included)
                    self.assertIn((base / "README.md").as_posix(), included)
                    for stage in ("Grundakte", "Nachreichungen"):
                        self.assertTrue(any(name.startswith((base / stage).as_posix() + "/") for name in included), slug)
                    for asset in (f"downloads/testakte-{slug}.zip", f"downloads/testakte-{slug}-einzelpdfs.zip",
                                  f"gesamt-pdf/testakte-{slug}_gesamt.pdf"):
                        name = (base / asset).as_posix()
                        self.assertEqual(archive.read(name), (ROOT / SOURCE / name).read_bytes())
            updates = metadata_changes(ROOT, scope, report)
            market = json.loads(updates[ROOT / ".claude-plugin/marketplace.json"])
            plugin, = [entry for entry in market["plugins"] if entry["name"] == SOURCE.name]
            self.assertEqual("445.36.14", plugin["version"])
            old_plan = json.loads((ROOT / f"scripts/data/{EDITION}.json").read_bytes())
            old_plan["nachfolger"]["patentrecht.zip"] = {"ausgabeversion": "445.36.9", "tag": TAG}
            self.assertEqual(json.loads(updates[ROOT / f"scripts/data/{EDITION}.json"]), old_plan)


if __name__ == "__main__":
    unittest.main()
