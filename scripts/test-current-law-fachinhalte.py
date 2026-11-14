#!/usr/bin/env python3
"""Erhaltene Fachmodule dürfen die bisherigen Rechtsfehler-Sperren nicht umgehen."""
from contextlib import redirect_stdout
import importlib.util
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("fachinhalt_sentinels", Path(__file__).with_name("validate-current-law-sentinels.py"))
S = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = S
spec.loader.exec_module(S)


class FachinhaltSentinelTests(unittest.TestCase):
    def run_source(self, filename, text, folder="beispiel/skills/vertiefung"):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / folder / filename
            path.parent.mkdir(parents=True)
            path.write_text(text, encoding="utf-8")
            output = io.StringIO()
            with patch.object(S, "REPO", root), patch.object(S, "markdown_files", return_value=[path]), redirect_stdout(output):
                status = S.main()
            return status, output.getvalue()

    def test_wrong_topic_is_rejected_before_and_after_demotion(self):
        folder = "fachanwalt-sportrecht/skills/fussballtransfer-vertragsbruch-und-rstp"
        for filename in ("SKILL.md", "FACHINHALT.md"):
            for bad in ("NADA-Code", "BImSchG"):
                with self.subTest(filename=filename, bad=bad):
                    status, output = self.run_source(filename, f"# Transfer\n\nMaßgeblich ist {bad}.\n", folder)
                    self.assertEqual(status, 1)
                    self.assertIn("fachfremde Doping- oder Immissionsnorm im Fußballtransfer", output)
                    self.assertIn(filename, output)

    def test_all_skill_specific_guards_still_apply_to_preserved_fachtext(self):
        cases = (
            ("### Kuratierte Normen-Bibliothek\n", "fachgebietsweiter Normenanhang"),
            ("| Rechtsprechung live prüfen |\n", "Platzhalterzeile"),
            ("nur verwenden, wenn die Fundstelle über ein amtliches oder frei zugängliches Portal gegengeprüft ist", "ungeprüfter Entscheidungsanker"),
            ("WRONG_TOPIC", "interner Auditstatus"),
        )
        for text, finding in cases:
            with self.subTest(finding=finding):
                status, output = self.run_source("FACHINHALT.md", text)
                self.assertEqual(status, 1)
                self.assertIn(finding, output)

    def test_clean_preserved_text_and_other_subject_remain_permitted(self):
        self.assertEqual(self.run_source("FACHINHALT.md", "# Belegter Prüfauftrag\n")[0], 0)
        self.assertEqual(self.run_source("FACHINHALT.md", "# Immissionsschutz\nBImSchG\n")[0], 0)


if __name__ == "__main__":
    unittest.main()
