from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "build-testakte-gesamt-pdf.py"
sys.path.insert(0, str(SCRIPT.parent))
SPEC = importlib.util.spec_from_file_location("build_testakte_gesamt_pdf", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
renderer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(renderer)


class TestaktePdfRendererTests(unittest.TestCase):
    def test_h3_keeps_immediately_following_content(self) -> None:
        flowables = renderer.md_to_flowables(
            "### Tatbestand\nErste entscheidende Zeile.\nZweite Zeile."
        )
        rendered = " ".join(
            item.getPlainText() for item in flowables if isinstance(item, Paragraph)
        )
        self.assertIn("Tatbestand", rendered)
        self.assertIn("Erste entscheidende Zeile.", rendered)
        self.assertIn("Zweite Zeile.", rendered)

    def test_long_unbroken_sentence_is_hard_split(self) -> None:
        source = "A" * 205
        parts = renderer._split_long_text(source, chunk=80)
        self.assertEqual(source, "".join(parts))
        self.assertTrue(parts)
        self.assertLessEqual(max(map(len, parts)), 80)

    def test_temporary_styles_are_restored_after_failure(self) -> None:
        original = renderer.s_body.fontSize
        with self.assertRaisesRegex(RuntimeError, "stop"):
            with renderer.temporary_style_values(
                {renderer.s_body: {"fontSize": original - 1}}
            ):
                self.assertEqual(renderer.s_body.fontSize, original - 1)
                raise RuntimeError("stop")
        self.assertEqual(renderer.s_body.fontSize, original)


if __name__ == "__main__":
    unittest.main()
