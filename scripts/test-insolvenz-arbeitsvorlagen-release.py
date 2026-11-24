#!/usr/bin/env python3
"""Regressionen für die unveränderten Altmitglieder und die gebundene Bezugsfassung."""
import importlib
import io
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from akteneingang.quellen import digest
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME


release = importlib.import_module("build-insolvenz-arbeitsvorlagen-release")


def source_zip(entries):
    stream = io.BytesIO()
    with ZipFile(stream, "w", compression=ZIP_DEFLATED) as archive:
        archive.comment = b"Historische Ausgabe"
        for name, data in entries.items():
            archive.writestr(name, data)
    return stream.getvalue()


class Originalausgaben(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / "testakte-beispiel.zip"
        self.entries = {NOTICE_FILENAME: NOTICE_BYTES + b"Bezug der individuellen Ausgabe",
                        "Grundakte/Eingang.eml": b"Eingang", "Notizen.txt": b"Anwalt"}
        self.old = source_zip(self.entries)
        self.forms = {"Arbeitsvorlagen/vertrag.docx": b"Vertrag", "Arbeitsvorlagen/berechnung.xlsx": b"Rechner"}

    def test_anhaengen_erhaelt_header_komprimierte_bytes_und_aktenstuecke(self):
        release.append_forms(self.old, self.path, self.forms)
        result = release.inspect_archive(self.old, self.path, self.forms)
        self.assertEqual(result, {"alte_dateien": 3, "arbeitsvorlagen": {n: digest(b) for n, b in self.forms.items()}})
        other = self.root / "wiederholung.zip"
        release.append_forms(self.old, other, dict(reversed(self.forms.items())))
        self.assertEqual(other.read_bytes(), self.path.read_bytes())

    def test_entferntes_oder_ersetztes_original_und_falsche_vorlage_werden_erkannt(self):
        variants = [{**self.entries, "Notizen.txt": b"geaendert"},
                    {n: b for n, b in self.entries.items() if n != "Notizen.txt"}]
        for bad in variants:
            with self.subTest(entries=bad):
                release.append_forms(source_zip(bad), self.path, self.forms)
                with self.assertRaises(ValueError):
                    release.inspect_archive(self.old, self.path, self.forms)
        changed = {**self.forms, "Arbeitsvorlagen/vertrag.docx": b"ausgefuelltes Beispiel"}
        release.append_forms(self.old, self.path, changed)
        with self.assertRaisesRegex(ValueError, "Arbeitsvorlage"):
            release.inspect_archive(self.old, self.path, self.forms)

    def test_kollisionen_einschliesslich_grossschreibung_werden_vor_dem_anhaengen_erkannt(self):
        for name in ("arbeitsvorlagen/alt.docx", "GRUNDAKTE/EINGANG.EML", "../Notizen.txt"):
            with self.subTest(name=name):
                original = source_zip({**self.entries, name: b"Alt"})
                with self.assertRaisesRegex(ValueError, "Quell-ZIP"):
                    release.append_forms(original, self.path, self.forms)

    def test_offline_quelle_wird_bei_jedem_lesen_geprueft(self):
        edition = release.Edition(self.root, offline=True)
        row = {"tag": "grundakten-sammlung-v1.0.0", "bytes": len(self.old), "sha256": digest(self.old)}
        name = self.path.name
        with self.assertRaisesRegex(ValueError, "fehlt"):
            edition.original(name, row)
        path = self.root / row["tag"] / name
        path.parent.mkdir()
        path.write_bytes(self.old)
        self.assertEqual(edition.original(name, row), self.old)
        path.write_bytes(bytes([self.old[0] ^ 1]) + self.old[1:])
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            edition.original(name, row)

    def test_scope_fuehrt_exakt_zwei_native_archive_aus_drei_veroeffentlichungen_je_akte(self):
        sources, names, additions = release.scope_files(release.ROOT)
        self.assertEqual(len(sources), 50)
        self.assertEqual(len(additions), 25)
        for slug, forms in additions.items():
            self.assertEqual(names["testakte-" + slug + ".zip"], names["lebensakte-" + slug + ".zip"])
            self.assertGreaterEqual(len(forms), 2)
            self.assertTrue(all(n.startswith("Arbeitsvorlagen/") for n in forms))


if __name__ == "__main__":
    unittest.main()
