#!/usr/bin/env python3
"""Quellenlinks von sichtbaren Gliederungsfehlern unterscheiden."""

import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "prompt_hygiene", Path(__file__).with_name("audit-generated-prompt-hygiene.py")
)
H = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(H)


class SourceLinks(unittest.TestCase):
    def test_focus_prompt_is_included_in_discovery(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / '.claude-plugin').mkdir()
            (root / 'fachgebiet/.claude-plugin').mkdir(parents=True)
            (root / '.claude-plugin/marketplace.json').write_text(json.dumps({'plugins': [{'source': './fachgebiet'}]}))
            (root / 'fachgebiet/.claude-plugin/plugin.json').write_text(json.dumps({'name': 'fachgebiet'}))
            focus = root / 'fachgebiet/fachgebiet-hauptproblem.md'
            focus.write_text('# Schwerpunkt\n', encoding='utf-8')
            with patch.object(H, 'REPO', root):
                self.assertIn(focus, H.prompt_files())

    def test_individually_maintained_prompt_does_not_bypass_hygiene(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'fachgebiet').mkdir()
            prompt = root / 'fachgebiet/fachgebiet-schnellstart.md'
            prompt.write_text('# Fachgebiet\n\nSichtbar (unvollständig.\n', encoding='utf-8')
            with patch.object(H, 'REPO', root), patch.object(H, 'prompt_files', return_value=[prompt]), \
                 patch.object(H, 'protected_slugs', return_value={'fachgebiet'}), redirect_stdout(io.StringIO()):
                self.assertEqual(H.main(), 1)

    def test_parenthetical_link_preserves_outer_parentheses(self):
        self.assertEqual(
            H.visible_prose("Rn. 34 ([amtliche Gründe](https://gericht.example/entscheidung))."),
            "Rn. 34 (amtliche Gründe).",
        )

    def test_url_with_balanced_parentheses_and_title(self):
        self.assertEqual(
            H.visible_prose('[Norm](https://recht.example/gesetz(2025) "Fassung") prüfen.'),
            "Norm prüfen.",
        )

    def test_visible_link_label_remains_subject_to_audit(self):
        self.assertEqual(H.visible_prose("[Geschuetzte Quelle](https://recht.example/)"),
                         "Geschuetzte Quelle")

    def test_bare_source_brackets_remain_balanced(self):
        self.assertEqual(H.visible_prose("Quelle [https://recht.example/norm]."), "Quelle [].")

    def test_autolinks_and_inline_code_do_not_create_false_errors(self):
        self.assertEqual(H.visible_prose("<https://recht.example/> `([` Ende."), "  Ende.")

    def test_broken_markdown_link_is_not_hidden(self):
        prose = H.visible_prose("Quelle [Norm](https://recht.example/norm")
        self.assertNotEqual(prose.count("("), prose.count(")"))

    def test_unbalanced_prose_next_to_valid_link_is_not_hidden(self):
        prose = H.visible_prose("(Vgl. [Norm](https://recht.example/norm).")
        self.assertNotEqual(prose.count("("), prose.count(")"))

    def test_relative_link_is_also_parsed(self):
        self.assertEqual(H.visible_prose("[Normen](../references/normen.md) (ergänzend)."),
                         "Normen (ergänzend).")

    def test_complete_source_requirement_is_not_a_truncated_case_anchor(self):
        text = "Der BVerfG-Anker ersetzt keinen Tatsachenbeleg. Weitere Aussagen benötigen eine überprüfbare Quelle."
        self.assertIsNone(H.TRUNCATED_CASE_END.search(text))
        self.assertIsNotNone(H.TRUNCATED_CASE_END.search("BGH: Nachweis statt einer."))
        self.assertIsNotNone(H.TRUNCATED_CASE_END.search("BVerfG: Ausnahme nicht der."))


if __name__ == "__main__":
    unittest.main()
