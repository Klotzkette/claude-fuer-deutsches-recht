#!/usr/bin/env python3
"""Prüft Generator-Hilfe und Argumentfehler in einer isolierten Dateistruktur."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parent
GENERATORS = (
    "generate-asset-index.py",
    "generate-default-rubrics.py",
    "generate-formatvorlagen.py",
    "generate-megaprompt.py",
    "generate-root-plugin-catalog.py",
    "generate-schwerpunkte.py",
    "generate-skills-md.py",
    "generate-skills-overview.py",
    "generate-werkstatt-und-schnellstart-coverage.py",
    "generate-werkstatt-und-schnellstart-prompts.py",
    "inject-ausformulierungspflicht.py",
    "inject-direkt-loslegen-section.py",
    "inject-gerichtsplugins-werkstatt-header.py",
    "inject-megaprompt-section.py",
    "inject-skills-logic-navigation.py",
    "inject-streitstoff-beitrag-gerichtsplugins.py",
    "inject-testakten-section.py",
    "refine-skill-selection-signals.py",
    "refine-speed-and-elegance.py",
)


def snapshot(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in root.rglob("*")
        if path.is_file()
    }


def run_script(root: Path, script: str, arguments: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-B", str(root / "scripts" / script), *arguments],
        cwd=root,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )


class GeneratorCliTests(unittest.TestCase):
    def test_help_and_rejected_arguments_do_not_write(self) -> None:
        with tempfile.TemporaryDirectory(prefix="generator-cli-") as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            for name in (*GENERATORS, "generator_cli.py"):
                shutil.copyfile(SCRIPTS / name, root / "scripts" / name)
            (root / "README.md").write_text("Unveränderte Startseite\n", encoding="utf-8")
            (root / "beispiel-plugin").mkdir()
            (root / "beispiel-plugin" / "README.md").write_text("Unverändertes Plugin\n", encoding="utf-8")
            before = snapshot(root)

            # Nur CLI und Originalskripte sind vorhanden. Die Argumentprüfung
            # muss selbst vor importspezifischen Generator-Abhängigkeiten enden.
            for name in GENERATORS:
                for arguments, expected in (
                    (["--help"], 0),
                    (["-h"], 0),
                    (["--check"], 2),
                    (["--mistyped-flag"], 2),
                    (["--he"], 2),
                    (["unerwartetes-argument"], 2),
                ):
                    with self.subTest(script=name, arguments=arguments):
                        result = run_script(root, name, arguments)
                        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                        self.assertEqual(snapshot(root), before, "CLI-Aufruf hat Dateien verändert")
                        if expected == 0:
                            self.assertIn("--help", result.stdout)
                            self.assertIn("--check", result.stdout)
                            self.assertIn("nicht unterstützt", result.stdout)
                        else:
                            self.assertIn("Nicht unterstützte Argumente", result.stderr)

    def test_argumentless_entry_still_reaches_writer(self) -> None:
        with tempfile.TemporaryDirectory(prefix="generator-cli-entry-") as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            shutil.copyfile(SCRIPTS / "generator_cli.py", root / "scripts" / "generator_cli.py")
            fixture = root / "scripts" / "write-probe.py"
            fixture.write_text(
                "from generator_cli import parse_generator_cli\n"
                "parse_generator_cli('Schreibprobe')\n"
                "from pathlib import Path\n"
                "Path('output.txt').write_text('ausgeführt', encoding='utf-8')\n",
                encoding="utf-8",
            )
            result = run_script(root, fixture.name, [])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((root / "output.txt").read_text(encoding="utf-8"), "ausgeführt")


if __name__ == "__main__":
    unittest.main()
