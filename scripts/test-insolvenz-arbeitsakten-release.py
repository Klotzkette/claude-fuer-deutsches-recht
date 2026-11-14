#!/usr/bin/env python3
"""Prüft reale Releasepakete und gezielt verfälschte Lesefassungen."""
import argparse
import importlib.util
import io
import os
from pathlib import Path
import shutil
import tempfile
import unittest
from zipfile import ZipFile, ZIP_DEFLATED

from pypdf import PdfReader, PdfWriter

spec = importlib.util.spec_from_file_location('arbeitsakten_release', Path(__file__).with_name('build-insolvenz-arbeitsakten-release.py'))
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)
DIST = None


class ReleaseTests(unittest.TestCase):
    def test_actual_assets_and_sources(self):
        report = release.verify(DIST)
        self.assertEqual(len(release.asset_names()), 32)
        self.assertEqual(sum(x['originals'] for x in report['cases'].values()), 532)
        self.assertEqual(sum(x['intake_originals'] for x in report['cases'].values()), 440)
        self.assertEqual(sum(x['total_pages'] for x in report['cases'].values()), 1317)

    def test_rejects_wrong_combined_pages_with_unchanged_page_count(self):
        with tempfile.TemporaryDirectory(prefix='arbeitsakten-stale-') as temporary:
            target = Path(temporary) / 'assets'
            shutil.copytree(DIST, target, copy_function=os.link)
            path = target / (release.CASES[0] + '_gesamt.pdf')
            reader = PdfReader(path)
            writer = PdfWriter()
            for index, page in enumerate(reader.pages):
                writer.add_page(reader.pages[0] if index == 1 else page)
            stream = io.BytesIO()
            writer.write(stream)
            path.unlink()  # Never modify the source through the temporary hard link.
            path.write_bytes(stream.getvalue())
            self.assertEqual(len(PdfReader(path).pages), len(reader.pages))
            with self.assertRaisesRegex(ValueError, 'andere oder falsch geordnete Dokumentseiten'):
                release.inspect(target, compare_sources=False)

    def test_rejects_changed_original_pdf_under_intake_prefix(self):
        with tempfile.TemporaryDirectory(prefix='arbeitsakten-bytes-') as temporary:
            target = Path(temporary) / 'assets'
            shutil.copytree(DIST, target, copy_function=os.link)
            slug = release.CASES[0]
            with ZipFile(target / f'testakte-{slug}.zip') as native:
                name = next(n for n in native.namelist() if n.startswith('Grundakte/') and n.endswith('.pdf'))
            path = target / f'testakte-{slug}-einzelpdfs.zip'
            with ZipFile(path) as archive:
                contents = {n: archive.read(n) for n in archive.namelist()}
            individual_name = name.removeprefix('Grundakte/')
            self.assertIn(individual_name, contents)
            original = contents[individual_name]
            contents[individual_name] += b'\n% changed after conversion\n'
            self.assertEqual(release.page_text(PdfReader(io.BytesIO(original)).pages[0]),
                             release.page_text(PdfReader(io.BytesIO(contents[individual_name])).pages[0]))
            path.unlink()
            with ZipFile(path, 'w', compression=ZIP_DEFLATED) as archive:
                for n, data in contents.items():
                    archive.writestr(n, data)
            with self.assertRaisesRegex(ValueError, 'Original-PDF fehlt oder ist nicht bytegleich'):
                release.inspect(target, compare_sources=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', required=True, type=Path)
    args, remaining = parser.parse_known_args()
    DIST = args.dist.resolve()
    unittest.main(argv=[__file__, *remaining])
