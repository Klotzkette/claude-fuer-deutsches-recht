"""Regressionen für Akten in Einzelordnern, mehreren Abruffassungen und Registern."""

import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile

from aktenarbeit_einstiege import mit_verweisen, ohne_verweise
from aktenbestand import fallquellen, pruefe_fundstellen, zaehlung


class InventurTests(unittest.TestCase):
    def test_fachseiten_im_einzelpaket_und_zentrale_fallseiten(self):
        original = "# Fallakte\n\nÖffnen Sie die Eingangsunterlagen.\n\n## Auftrag\n"
        anker = "faelle-g-k.md#fall-interstate-01-alleinstellung"
        for seite, ziel in (
            ("vergaberecht-werkstatt/vergabestelle-behoerden/Interstate AG/01-alleinstellung/README.md",
             "https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/docs/downloads/aktenarbeit/"),
            ("testakten/fall/README.md", "../../docs/downloads/aktenarbeit/"),
        ):
            with self.subTest(seite=seite):
                text = mit_verweisen(original, seite, ["interstate-01-alleinstellung"])
                self.assertIn("](" + ziel + anker + ")", text)
                self.assertEqual(mit_verweisen(text, seite, ["interstate-01-alleinstellung"]), text)
                self.assertEqual(ohne_verweise(text), original)

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
