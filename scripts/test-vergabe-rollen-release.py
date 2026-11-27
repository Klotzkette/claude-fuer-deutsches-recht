#!/usr/bin/env python3
"""Prüft die drei Pakete und ihre gemeinsame, wiederholbare Marketplace-Aktivierung."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile

from activate_quality_release import BUILDER, ROOT, SOURCE_GROUPS, VERGABE_TAG, metadata_changes
from package_edition import EDITION


class VergaberollenFreigabe(unittest.TestCase):
    def test_pakete_und_gemeinsame_aktivierung(self):
        scope = json.loads((ROOT / f"scripts/data/{VERGABE_TAG}-scope.json").read_bytes())
        sources = SOURCE_GROUPS[VERGABE_TAG]
        self.assertEqual(len(sources), 3)
        version = scope["version"]
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "ausgabe"
            report = BUILDER.build(output, scope, ROOT)
            self.assertEqual(report, BUILDER.validate_assets(output, scope, ROOT))
            self.assertEqual(len(list(output.iterdir())), 11)
            for source in sources:
                name = source.name
                with ZipFile(output / (name + ".zip")) as archive:
                    self.assertEqual(json.loads(archive.read(".claude-plugin/plugin.json"))["version"], version)
                    self.assertGreater(len(report["plugins"][name]["skills"]), 0)
                for art in ("schnellstart", "werkstatt"):
                    filename = f"{name}-{art}.md"
                    self.assertEqual((output / filename).read_bytes(), (ROOT / source / filename).read_bytes())
            updates = metadata_changes(ROOT, scope, report)
            for manifest in (".claude-plugin/marketplace.json", "vergaberecht-werkstatt/.claude-plugin/marketplace.json"):
                entries = json.loads(updates[ROOT / manifest])["plugins"]
                self.assertEqual({row["name"] for row in entries if row["version"] == version},
                                 {source.name for source in sources})
            edition = json.loads(updates[ROOT / f"scripts/data/{EDITION}.json"])
            for source in sources:
                self.assertEqual(edition["nachfolger"][source.name + ".zip"]["tag"], VERGABE_TAG)
            sandbox = Path(temp) / "aktiviert"
            for path, data in updates.items():
                target = sandbox / path.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            for plugin, source in zip(scope["plugins"], sources, strict=True):
                for filename in plugin["prompts"]:
                    (sandbox / source / filename).write_bytes((ROOT / source / filename).read_bytes())
            second = metadata_changes(sandbox, scope, report)
            self.assertTrue(all(path.read_bytes() == data for path, data in second.items()))
            incomplete = copy.deepcopy(report)
            incomplete["plugins"].pop(sources[-1].name)
            with self.assertRaises(ValueError):
                metadata_changes(sandbox, scope, incomplete)
            # Ein einziger geänderter Prompt verhindert die gesamte Freigabeplanung.
            changed = sandbox / sources[-1] / f"{sources[-1].name}-werkstatt.md"
            changed.write_text("abweichender Text", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "lokaler Prompt"):
                metadata_changes(sandbox, scope, report)


if __name__ == "__main__":
    unittest.main()
