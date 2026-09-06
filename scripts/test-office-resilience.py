#!/usr/bin/env python3
"""Prüft Prozessabbruch, isolierte Konvertierung und begrenzte Paketverarbeitung."""

from __future__ import annotations

import importlib.util
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
import zipfile

from pypdf import PdfWriter
from office_process import pdf_markers, run_office
import testakte_office_pdf as office


ROOT = Path(__file__).resolve().parent.parent
TOOL_DIRS = [
    ROOT / "schriftsatz-versandwerkstatt/skills/versandmappe-endfertigen/werkzeuge",
    ROOT / "anlagen-zu-schriftsaetzen/skills/anlagen-zu-schriftsaetzen/werkzeuge",
]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


TOOLS = [load(folder / filename, f"resilience_{index}") for index, (folder, filename) in enumerate(zip(
    TOOL_DIRS, ("build_versandmappe.py", "build_anlagenkonvolut.py"),
))]
E = load(ROOT / "scripts/build-testakten-einzelpdf-zips.py", "resilience_single")
W = load(ROOT / "scripts/build-testakten-release-zips.py", "resilience_working")


def pdf_bytes():
    writer = PdfWriter()
    writer.add_blank_page(595, 842)
    output = io.BytesIO()
    writer.write(output)
    return output.getvalue()


class OfficeResilience(unittest.TestCase):
    def test_packaged_helpers_match(self):
        canonical = (ROOT / "scripts/office_process.py").read_bytes()
        for folder in TOOL_DIRS:
            self.assertEqual((folder / "office_process.py").read_bytes(), canonical)
            completed = subprocess.run([sys.executable, "-c", "import office_process"], cwd=folder, timeout=10)
            self.assertEqual(completed.returncode, 0)

    def test_logs_are_bounded_and_stdin_closed(self):
        code, details = run_office([
            sys.executable, "-c", "import sys; assert sys.stdin.read() == ''; sys.stdout.write('x'*3000000+'END')",
        ], timeout=10)
        self.assertEqual(code, 0)
        self.assertLessEqual(len(details.encode()), 2048)
        self.assertTrue(details.endswith("END"))

    @unittest.skipUnless(os.name == "posix", "Prozessgruppenprüfung für Linux und macOS")
    def test_timeout_stops_child_process(self):
        with tempfile.TemporaryDirectory() as tmp:
            marker = Path(tmp) / "child-alive"
            ready = Path(tmp) / "child-started"
            child = "import time; from pathlib import Path; Path(" + repr(str(ready)) + ").touch(); time.sleep(3); Path(" + repr(str(marker)) + ").touch(); time.sleep(10)"
            parent = "import subprocess,sys,time; subprocess.Popen([sys.executable,'-c'," + repr(child) + "]); time.sleep(10)"
            start = time.monotonic()
            with self.assertRaises(subprocess.TimeoutExpired):
                run_office([sys.executable, "-c", parent], timeout=2)
            self.assertLess(time.monotonic() - start, 5)
            self.assertTrue(ready.exists(), "Kindprozess muss für die Prüfung tatsächlich gestartet sein")
            time.sleep(1.5)
            self.assertFalse(marker.exists(), "Kindprozess darf nach dem Abbruch nicht weiterarbeiten")

    def test_markers_across_chunk_boundaries(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source.pdf"
            path.write_bytes(b"x" * (1024 * 1024 - 4) + b"/JavaScript" + b"/Launch")
            self.assertEqual(pdf_markers(path, (b"/JavaScript", b"/Launch", b"/JS")), {b"/JavaScript", b"/Launch"})

    def test_isolated_output_and_old_pdf_not_accepted(self):
        for tool in TOOLS:
            with self.subTest(tool=tool.__name__), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                source = root / "Antrag.docx"
                source.write_bytes(b"source")
                target_dir = root / "out"
                target_dir.mkdir()
                target = target_dir / "Antrag.pdf"
                target.write_bytes(b"old result")
                profiles = []

                def fake(command, **kwargs):
                    profiles.append(next(x for x in command if x.startswith("-env:UserInstallation=")))
                    output = Path(command[command.index("--outdir") + 1])
                    self.assertNotEqual(output, target_dir)
                    self.assertTrue(Path(command[-1]).is_absolute())
                    return 0, ""

                with patch.object(tool.shutil, "which", return_value="office"), patch.object(tool, "run_office", side_effect=fake):
                    with self.assertRaisesRegex(RuntimeError, "keine neue PDF"):
                        tool.konvertiere_office(source, target_dir)
                    with self.assertRaises(RuntimeError):
                        tool.konvertiere_office(source, target_dir)
                self.assertNotEqual(profiles[0], profiles[1])
                self.assertEqual(target.read_bytes(), b"old result")
                self.assertEqual(list(target_dir.iterdir()), [target])

    def test_invalid_output_does_not_replace_valid_previous_output(self):
        for tool in TOOLS:
            with self.subTest(tool=tool.__name__), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                source = root / "Brief.docx"
                source.touch()
                target = root / "Brief.pdf"
                target.write_bytes(pdf_bytes())
                before = target.read_bytes()

                def fake(command, **kwargs):
                    (Path(command[command.index("--outdir") + 1]) / target.name).write_bytes(b"broken")
                    return 0, ""

                with patch.object(tool.shutil, "which", return_value="office"), patch.object(tool, "run_office", side_effect=fake):
                    with self.assertRaisesRegex(RuntimeError, "keine nutzbare PDF"):
                        tool.konvertiere_office(source, root)
                self.assertEqual(target.read_bytes(), before)

    def test_success_replaces_output_only_with_new_pdf(self):
        for tool in TOOLS:
            with self.subTest(tool=tool.__name__), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                source = root / "Brief.docx"
                source.touch()
                result = pdf_bytes()

                def fake(command, **kwargs):
                    (Path(command[command.index("--outdir") + 1]) / "Brief.pdf").write_bytes(result)
                    return 0, ""

                with patch.object(tool.shutil, "which", return_value="office"), patch.object(tool, "run_office", side_effect=fake):
                    target = tool.konvertiere_office(source, root)
                self.assertEqual(target.read_bytes(), result)

    def test_failed_attachment_does_not_prevent_remaining_inventory(self):
        for tool in TOOLS:
            with self.subTest(tool=tool.__name__), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                bad = root / "Anlage_K-01_Brief.docx"
                good = root / "Anlage_K-02_Vertrag.pdf"
                bad.touch()
                good.write_bytes(pdf_bytes())
                def convert(path, *args):
                    if path == bad:
                        raise RuntimeError("Office-Konvertierung nach 120 Sekunden abgebrochen")
                    return path
                with patch.object(tool, "als_pdf", side_effect=convert):
                    attachments, findings = tool.lese_anlagen(root, "K", root, True, None)
                self.assertEqual([a.quelle for a in attachments], [good])
                self.assertTrue(any(b.stufe == "STOP" and "120 Sekunden" in b.text for b in findings))

    def test_bounded_office_groups_preserve_all_results(self):
        paths = [Path(f"source-{n}.docx") for n in range(19)]
        groups = []
        def fake(group, binary):
            groups.append(list(group))
            return {p: str(p).encode() for p in group}
        with patch.object(office, "valid_office_container", return_value=True), patch.object(office, "office_binary", return_value="office"), patch.object(office, "_render_office_group", side_effect=fake):
            result = office.render_office_batch(paths)
        self.assertEqual([len(g) for g in groups], [8, 8, 3])
        self.assertEqual(list(result), paths)

    def test_individual_zip_batch_bound_and_atomic_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            case = root / "akte"
            case.mkdir()
            pairs = [(case / f"{n}.docx", f"{n}.pdf") for n in range(19)]
            sizes = []
            def convert(paths):
                sizes.append(len(paths))
                return {p: pdf_bytes() for p in paths}
            def render(path, case, cache):
                return cache[path]
            with patch.object(E, "document_arcname_pairs", return_value=pairs), patch.object(E, "render_office_batch", side_effect=convert), patch.object(E, "render_document_pdf", side_effect=render):
                output, count = E.build_single(case, root)
            self.assertEqual(sizes, [8, 8, 3])
            self.assertEqual(count, 19)
            previous = output.read_bytes()
            with patch.object(E, "add_testakte", side_effect=RuntimeError("abgebrochen")):
                with self.assertRaises(RuntimeError):
                    E.build_single(case, root)
            self.assertEqual(output.read_bytes(), previous)
            self.assertFalse(output.with_name(f".{output.name}.tmp").exists())

    def test_nested_zip_stored_without_recompression(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inner = root / "inner.zip"
            with zipfile.ZipFile(inner, "w") as archive:
                archive.writestr("datei.txt", "Sachverhalt")
            for write in (E.write_archive, lambda z, p: W.write_file(z, p, p.name)):
                buffer = io.BytesIO()
                with zipfile.ZipFile(buffer, "w") as archive:
                    write(archive, inner)
                with zipfile.ZipFile(buffer) as archive:
                    self.assertEqual(archive.getinfo(inner.name).compress_type, zipfile.ZIP_STORED)
                    self.assertEqual(archive.read(inner.name), inner.read_bytes())


if __name__ == "__main__":
    unittest.main()
