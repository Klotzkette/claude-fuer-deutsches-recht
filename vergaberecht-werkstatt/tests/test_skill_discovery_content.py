"""Sichtbare Normzitate bleiben streng, technische Fachpfade bleiben stabil."""
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("skill_discovery_content", ROOT / "scripts/validate-skill-discovery.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class BodyNormTests(unittest.TestCase):
    def test_correct_label_with_historical_filename_is_allowed(self):
        body = "[Rüge nach § 160 GWB](../ruege-paragraf-160/FACHINHALT.md)"
        self.assertIsNone(module.BODY_SPELLED_PARAGRAPH_RE.search(module.visible_body_norm_text(body)))

    def test_spelled_out_norm_in_label_or_prose_remains_rejected(self):
        for body in ("[Paragraf 160 GWB](../pruefung/FACHINHALT.md)", "Nach Paragraf 160 GWB prüfen."):
            self.assertIsNotNone(module.BODY_SPELLED_PARAGRAPH_RE.search(module.visible_body_norm_text(body)))

    def test_inline_literal_remains_excluded_but_neighboring_prose_does_not(self):
        body = "`ruege-paragraf-160` und Paragraf 160 GWB"
        actual = module.visible_body_norm_text(body)
        self.assertNotIn("ruege-paragraf-160", actual)
        self.assertIsNotNone(module.BODY_SPELLED_PARAGRAPH_RE.search(actual))


if __name__ == "__main__":
    unittest.main()
