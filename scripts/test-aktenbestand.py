"""Regressionen für Akten in Einzelordnern, mehreren Abruffassungen und Registern."""

import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile

from aktenbestand import fallquellen, pruefe_fundstellen, zaehlung


class InventurTests(unittest.TestCase):
    def test_unabhaengig_von_gesamtdruck_und_downloadzahl(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            market = root / ".claude-plugin/marketplace.json"
            market.parent.mkdir()
            market.write_text(json.dumps({"plugins": [{"name": "fach", "source": "./fach"}]}))
            for folder in ("testakten/zentral", "testakten/megaprompts", "fach/testakten/lokal"):
                case = root / folder
                case.mkdir(parents=True)
                (case / "README.md").write_text("# Fall")
            case = root / "fach/testakten/lokal"
            (case / "auftrag.eml").write_bytes(b"Subject: Auftrag")
            expected = {"central_testakten": 1, "weitere_testakten": 1, "testakten": 2}
            self.assertEqual(zaehlung(root), expected)
            (case / "downloads").mkdir()
            for bundle in ("testakte-lokal.zip", "testakte-lokal-einzelpdfs.zip"):
                with ZipFile(case / "downloads" / bundle, "w") as z:
                    z.writestr("auftrag.eml", b"Subject: Auftrag")
            quellen = fallquellen(root)
            self.assertEqual(zaehlung(root), expected)
            q = quellen["fach/testakten/lokal"]
            self.assertTrue(q["archive"][0].endswith("/testakte-lokal.zip"))
            fall = {"fallpfad": "fach/testakten/lokal", "fundstellen": [q["archive"][0] + "!auftrag.eml"]}
            self.assertEqual(pruefe_fundstellen(root, [fall], quellen), 1)
            fall["fallpfad"] = "testakten/zentral"
            with self.assertRaisesRegex(ValueError, "gehört nicht zur Akte"):
                pruefe_fundstellen(root, [fall], quellen)


if __name__ == "__main__":
    unittest.main()
