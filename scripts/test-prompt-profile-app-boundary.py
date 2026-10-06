"""Keine künstlichen Werkstatt-Prompts für ausschließlich ausführbare Apps."""

import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "prompt_route_audit", Path(__file__).with_name("audit-prompt-profile-routing.py")
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class AppBoundary(unittest.TestCase):
    def run_audit(self, directory, kinds=()):
        with patch.object(AUDIT, "marketplace_plugins", return_value=[("reine-app", directory, "Lokale Anwendung")]), \
                patch.object(AUDIT, "standalone_kinds", return_value=kinds), \
                patch.object(AUDIT, "protected_slugs", return_value=set()), \
                patch.object(AUDIT, "source_anchor_problems", return_value=[]), \
                patch.object(AUDIT, "REPO", directory.parent), \
                contextlib.redirect_stdout(io.StringIO()) as stdout:
            return AUDIT.main(), stdout.getvalue()

    def test_app_needs_no_generator_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.run_audit(Path(tmp))[0], 0)

    def test_unexpected_prompt_is_not_silently_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "reine-app-werkstatt.md").write_text("# Unbestellte Werkstatt\n")
            result, report = self.run_audit(directory)
            self.assertNotEqual(result, 0)
            self.assertIn("verwaister Prompt-Dateiname", report)

    def test_prompt_plugin_still_needs_subject_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            result, report = self.run_audit(Path(tmp), ("werkstatt",))
            self.assertNotEqual(result, 0)
            self.assertIn("Plugins ohne Fachprofil", report)


if __name__ == "__main__":
    unittest.main()
