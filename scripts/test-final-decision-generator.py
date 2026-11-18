#!/usr/bin/env python3
"""Entscheidungsgenerator nur an isolierten Testdateien ausführen.

Prüft Dateierhalt, aktive Auswahlgrenze und schreibfreie Fehlerbehandlung;
keine juristische Neubewertung der historischen Entscheidungsvorlage.
"""

from __future__ import annotations

from contextlib import redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("final_decision_generator", SCRIPTS / "add-finale-entscheidung-skill.py")
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)
CONFIG = next(iter(G.PLUGINS.values()))


def snapshot(root: Path) -> dict[str, tuple[str, bytes | str | None]]:
    result = {}
    for path in root.rglob("*"):
        key = path.relative_to(root).as_posix()
        if path.is_symlink():
            result[key] = ("link", os.readlink(path))
        elif path.is_dir():
            result[key] = ("directory", None)
        else:
            result[key] = ("file", path.read_bytes())
    return result


class FinalDecisionGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="final-decision-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()

    def write(self, relative: str, content: str = "Originaltext\n") -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def plugin(self, name: str, count: int) -> None:
        self.write(f"{name}/README.md", "Unveränderte Beschreibung\n")
        for index in range(count):
            slug = "auftrag-bearbeiten" if index == 0 else f"fachfrage-{index}-pruefen"
            self.write(f"{name}/skills/{slug}/SKILL.md", f"# {slug}\n\nGeprüfter Fachtext {index}.\n")

    def profiles(self, names: list[str], entries: list[str] | None = None) -> None:
        self.write("scripts/data/werkstatt-visualisierung-profile.json", json.dumps({
            "schema_version": 1,
            "plugins": {name: {"entry_skills": entries or ["auftrag-bearbeiten"], "mode": "prompt"} for name in names},
        }))

    def run_generator(self, names: list[str]) -> tuple[int, str]:
        output = io.StringIO()
        with patch.object(G, "ROOT", self.root), \
                patch.object(G, "PLUGINS", {name: CONFIG for name in names}), redirect_stdout(output):
            result = G.main()
        return result, output.getvalue()

    def test_existing_and_consolidated_old_or_new_skill_remain_byte_identical(self):
        names = []
        for index, (slug, filename) in enumerate((
            (G.LEGACY_SKILL_NAME, "SKILL.md"),
            (G.LEGACY_SKILL_NAME, "FACHINHALT.md"),
            (G.SKILL_NAME, "SKILL.md"),
            (G.SKILL_NAME, "FACHINHALT.md"),
        )):
            name = f"gericht-{index}"
            names.append(name)
            self.plugin(name, 1)
            self.write(f"{name}/skills/{slug}/{filename}", "Individuell geprüfte Fassung; nicht ersetzen.\n")
        self.profiles(names)
        before = snapshot(self.root)
        code, output = self.run_generator(names)
        self.assertEqual(code, 0, output)
        self.assertEqual(snapshot(self.root), before)
        self.assertEqual(output.count("PRESERVED"), 4)
        self.assertIn("created=0 skipped=4", output)

    def test_twenty_active_skills_including_entry_allow_one_new_skill_and_rerun_is_read_only(self):
        self.plugin("gericht", 20)
        self.profiles(["gericht"])
        before = snapshot(self.root)
        code, output = self.run_generator(["gericht"])
        self.assertEqual(code, 0, output)
        target = self.root / "gericht/skills" / G.SKILL_NAME / "SKILL.md"
        self.assertEqual(G.SKILL_NAME, "entscheidung-volltext-erstellen")
        expected = G.SKILL_TEMPLATE.format(skill_name=G.SKILL_NAME,
            description=G.make_description(CONFIG["title"]), **CONFIG)
        self.assertEqual(target.read_text(encoding="utf-8"), expected)
        self.assertEqual(len(list((self.root / "gericht/skills").glob("*/SKILL.md"))), 21)
        self.assertFalse((self.root / "gericht/skills" / G.LEGACY_SKILL_NAME).exists())
        after = snapshot(self.root)
        self.assertTrue(all(after[key] == value for key, value in before.items()))
        code, output = self.run_generator(["gericht"])
        self.assertEqual(code, 0, output)
        self.assertEqual(snapshot(self.root), after)

    def test_later_twenty_second_skill_fails_before_any_target_is_written(self):
        self.plugin("erstes-gericht", 1)
        self.plugin("volles-gericht", 21)
        self.profiles(["erstes-gericht", "volles-gericht"])
        before = snapshot(self.root)
        code, output = self.run_generator(["erstes-gericht", "volles-gericht"])
        self.assertEqual(code, 1)
        self.assertIn("22 aktive Skills einschließlich Einstiegsskills überschreiten 21", output)
        self.assertEqual(snapshot(self.root), before)

    def test_missing_declared_entry_aborts_before_any_output(self):
        self.plugin("gericht", 1)
        self.profiles(["gericht"], ["auftrag-bearbeiten", "fehlender-einstieg"])
        before = snapshot(self.root)
        code, output = self.run_generator(["gericht"])
        self.assertEqual(code, 1)
        self.assertIn("Deklarierte Einstiegsskills fehlen", output)
        self.assertEqual(snapshot(self.root), before)

    def test_invalid_profile_is_rejected_without_partial_generation(self):
        self.plugin("gericht", 1)
        self.write("scripts/data/werkstatt-visualisierung-profile.json", "[]")
        before = snapshot(self.root)
        code, output = self.run_generator(["gericht"])
        self.assertEqual(code, 1)
        self.assertIn("Ungültige bestehende Einstiegsprofile", output)
        self.assertEqual(snapshot(self.root), before)

    def test_missing_plugin_is_not_created(self):
        before = snapshot(self.root)
        code, output = self.run_generator(["fehlendes-gericht"])
        self.assertEqual(code, 0, output)
        self.assertIn("MISSING fehlendes-gericht", output)
        self.assertEqual(snapshot(self.root), before)

    def test_linked_or_escaping_target_cannot_write_outside_repository(self):
        outside = self.root.parent / "outside"
        outside.mkdir()
        self.plugin("erstes-gericht", 1)
        linked = self.root / "verlinktes-gericht"
        try:
            linked.symlink_to(outside, target_is_directory=True)
        except OSError as exc:
            self.skipTest(f"Symlinks nicht verfügbar: {exc}")
        for name in ("verlinktes-gericht", "../outside"):
            with self.subTest(target=name):
                before = snapshot(self.root)
                code, output = self.run_generator(["erstes-gericht", name])
                self.assertEqual(code, 1, output)
                self.assertEqual(snapshot(self.root), before)
                self.assertEqual(list(outside.iterdir()), [])

    def test_help_and_bad_arguments_are_read_only_before_optional_imports(self):
        scripts = self.root / "scripts"
        scripts.mkdir()
        for name in ("add-finale-entscheidung-skill.py", "generator_cli.py"):
            shutil.copyfile(SCRIPTS / name, scripts / name)
        # skill_limits und Plugin-Dateien fehlen bewusst: CLI muss früher enden.
        before = snapshot(self.root)
        for args, expected in ((["--help"], 0), (["-h"], 0), (["--check"], 2),
                               (["--mistyped"], 2), (["--he"], 2), (["argument"], 2)):
            with self.subTest(arguments=args):
                result = subprocess.run([sys.executable, "-B", str(scripts / "add-finale-entscheidung-skill.py"), *args],
                    cwd=self.root, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                    text=True, capture_output=True, timeout=10, check=False)
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                self.assertEqual(snapshot(self.root), before)


if __name__ == "__main__":
    unittest.main()
