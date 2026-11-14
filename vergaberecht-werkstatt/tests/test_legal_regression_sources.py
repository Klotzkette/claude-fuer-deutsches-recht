"""Erhaltene Fachquellen behalten ihre verpflichtenden Norm-/Quellenanker."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location("legal_regression_sources", ROOT / "scripts/validate-legal-regressions.py")
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)
import skill_sources


class RequiredSourceTests(unittest.TestCase):
    def test_registered_module_still_requires_each_legal_marker(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            old = root / "rolle/skills/fachthema/SKILL.md"
            source = old.with_name("FACHINHALT.md")
            source.parent.mkdir(parents=True)
            markers = ("§ 160 Abs. 3 Satz 1 Nr. 5 GWB", "§ 187 Abs. 2 GWB")
            source.write_text("\n".join(markers), encoding="utf-8")
            with patch.object(validator, "ROOT", root), patch.object(skill_sources, "moved_sources", return_value={old.resolve(): source.resolve()}):
                self.assertEqual(validator.required_source_problems(old, markers, "Pflichtdatei fehlt", "aktueller Normanker fehlt"), [])
                source.write_text(markers[0], encoding="utf-8")
                errors = validator.required_source_problems(old, markers, "Pflichtdatei fehlt", "aktueller Normanker fehlt")
                self.assertEqual(errors, ["rolle/skills/fachthema/FACHINHALT.md: aktueller Normanker fehlt: § 187 Abs. 2 GWB"])
                source.unlink()
                self.assertEqual(validator.required_source_problems(old, markers, "Pflichtdatei fehlt", "aktueller Normanker fehlt"),
                                 ["rolle/skills/fachthema/SKILL.md: Pflichtdatei fehlt"])

    def test_unregistered_replacement_does_not_satisfy_source_requirement(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            old = root / "rolle/skills/fachthema/SKILL.md"
            source = old.with_name("FACHINHALT.md")
            source.parent.mkdir(parents=True)
            source.write_text("Quelle 2026/2027", encoding="utf-8")
            with patch.object(validator, "ROOT", root), patch.object(skill_sources, "moved_sources", return_value={}):
                self.assertEqual(validator.required_source_problems(old, ("Quelle 2026/2027",), "Pflichtdatei für Schwellenwertquellen fehlt", "Schwellenwertquelle 2026/2027 fehlt"),
                                 ["rolle/skills/fachthema/SKILL.md: Pflichtdatei für Schwellenwertquellen fehlt"])


if __name__ == "__main__":
    unittest.main()
