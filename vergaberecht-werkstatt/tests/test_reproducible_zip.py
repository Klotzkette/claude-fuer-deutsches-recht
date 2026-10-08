from __future__ import annotations

import hashlib
import os
import stat
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from reproducible_zip import FIXED_ZIP_TIME, archive_tree, write_archive  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ReproducibleZipTests(unittest.TestCase):
    def test_output_is_sorted_and_independent_of_source_mtime(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "source"
            root.mkdir()
            (root / "z.txt").write_text("z", encoding="utf-8")
            (root / "a.txt").write_text("a", encoding="utf-8")
            first = Path(temp) / "first.zip"
            second = Path(temp) / "second.zip"

            archive_tree(first, root)
            os.utime(root / "a.txt", (1_700_000_000, 1_700_000_000))
            os.utime(root / "z.txt", (1_800_000_000, 1_800_000_000))
            archive_tree(second, root)

            self.assertEqual(digest(first), digest(second))
            self.assertEqual(stat.S_IMODE(first.stat().st_mode), 0o644)
            self.assertEqual(stat.S_IMODE(second.stat().st_mode), 0o644)
            with zipfile.ZipFile(first) as archive:
                self.assertEqual(archive.namelist(), ["a.txt", "z.txt"])
                self.assertTrue(all(item.date_time == FIXED_ZIP_TIME for item in archive.infolist()))

    def test_empty_or_duplicate_input_preserves_existing_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "release.zip"
            output.write_bytes(b"bestehendes Archiv")
            source = Path(temp) / "source.txt"
            source.write_text("Inhalt", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "kein ZIP-Eintrag"):
                write_archive(output, [])
            self.assertEqual(output.read_bytes(), b"bestehendes Archiv")

            with self.assertRaisesRegex(ValueError, "doppelter oder kollidierender ZIP-Eintrag"):
                write_archive(output, [(source, "a.txt"), (source, "a.txt")])
            self.assertEqual(output.read_bytes(), b"bestehendes Archiv")

    def test_archive_streams_sources_and_avoids_recompression(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            text_source = root / "source.txt"
            pdf_source = root / "source.pdf"
            text_source.write_text("Text " * 10_000, encoding="utf-8")
            pdf_source.write_bytes(b"%PDF-1.7\n" + b"0" * 50_000)
            output = root / "release.zip"

            with mock.patch.object(Path, "read_bytes", side_effect=AssertionError("read_bytes")):
                write_archive(
                    output,
                    [(text_source, "source.txt"), (pdf_source, "source.pdf")],
                )

            with zipfile.ZipFile(output) as archive:
                self.assertEqual(
                    archive.getinfo("source.txt").compress_type,
                    zipfile.ZIP_DEFLATED,
                )
                self.assertEqual(
                    archive.getinfo("source.pdf").compress_type,
                    zipfile.ZIP_STORED,
                )

    def test_cross_platform_name_collisions_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source.txt"
            source.write_text("Inhalt", encoding="utf-8")
            output = root / "release.zip"

            with self.assertRaisesRegex(ValueError, "kollidierender"):
                write_archive(output, [(source, "A.txt"), (source, "a.txt")])
            with self.assertRaisesRegex(ValueError, "kollidierender"):
                write_archive(output, [(source, "A\u0308.txt"), (source, "Ä.txt")])

    def test_unsafe_archive_names_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.txt"
            source.write_text("Inhalt", encoding="utf-8")
            output = Path(temp) / "release.zip"

            for arcname in ("/root.txt", "C:/root.txt", "../root.txt", "bad\x00name.txt"):
                with self.subTest(arcname=arcname):
                    with self.assertRaisesRegex(ValueError, "unzulaessiger ZIP-Pfad"):
                        write_archive(output, [(source, arcname)])

    def test_output_inside_source_tree_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "source"
            root.mkdir()
            (root / "source.txt").write_text("Inhalt", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "innerhalb des Quellbaums"):
                archive_tree(root / "release.zip", root)

    def test_symlink_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.txt"
            source.write_text("Inhalt", encoding="utf-8")
            link = Path(temp) / "link.txt"
            try:
                link.symlink_to(source)
            except OSError:
                self.skipTest("Symlinks werden in dieser Umgebung nicht unterstützt")

            with self.assertRaisesRegex(ValueError, "Symlink"):
                write_archive(Path(temp) / "release.zip", [(link, "link.txt")])


if __name__ == "__main__":
    unittest.main()
