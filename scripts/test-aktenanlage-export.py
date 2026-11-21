#!/usr/bin/env python3
"""Prüft den tatsächlichen ZIP-Export und die Trennung von Prüfung, Mandat, Amt und Büro."""
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

TOOL = Path(__file__).resolve().parents[1] / "aktenanleger/werkzeuge/akte_anlegen.py"
spec = importlib.util.spec_from_file_location("aktenexport", TOOL)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class Aktenanlage(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.post = self.root / "Eingang"
        self.post.mkdir()
        self.original = b"From: empfang@example.invalid\r\n\r\nAnfrage\r\n"
        (self.post / "Anfrage.eml").write_bytes(self.original)
        self.stamm = self.root / "Stamm.json"
        self.data = json.loads((TOOL.parent / "aktenstamm-muster.json").read_text())

    def run_export(self, rolle, status):
        self.data.update(rolle=rolle, konfliktstatus=status)
        self.stamm.write_text(json.dumps(self.data))
        target = self.root / (rolle + ".zip")
        mod.akte_anlegen(self.stamm, self.post, target)
        return target

    def test_vier_aktenarten_und_originaltreue(self):
        for rolle, folder in mod.ROLLEN.items():
            with self.subTest(rolle=rolle), ZipFile(self.run_export(rolle, "geprueft")) as result:
                self.assertEqual(result.read(folder + "/01_Eingang/Anfrage.eml"), self.original)
                bestand = json.loads(result.read(folder + "/Originalverzeichnis.json"))
                self.assertEqual(bestand, [{"datei":"Anfrage.eml","bytes":len(self.original),"sha256":hashlib.sha256(self.original).hexdigest()}])
                self.assertIn(self.data["offene_punkte"][0], result.read(folder + "/02_Bearbeitung/Offene_Aufgaben.txt").decode())

    def test_offener_konflikt_und_zweite_anlage(self):
        for rolle in ("notar", "anwalt", "buero"):
            for status in ("offen", "hindernis"):
                with self.subTest(rolle=rolle, status=status), self.assertRaises(ValueError):
                    self.run_export(rolle, status)
                self.assertFalse((self.root / (rolle + ".zip")).exists())
        target = self.run_export("klaerung", "offen")
        old = target.read_bytes()
        with self.assertRaises(FileExistsError):
            self.run_export("klaerung", "hindernis")
        self.assertEqual(target.read_bytes(), old)

    def test_externe_datei_bleibt_ausserhalb_der_akte(self):
        (self.post / "Verweis.txt").symlink_to(self.root / "andere-akte.txt")
        with self.assertRaises(ValueError):
            self.run_export("notar", "geprueft")
        self.assertFalse((self.root / "notar.zip").exists())


if __name__ == "__main__":
    unittest.main()
