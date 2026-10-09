#!/usr/bin/env python3
"""Quellenlinks von sichtbaren Gliederungsfehlern unterscheiden."""

import importlib.util
import hashlib
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
    def test_reviewed_source_requirements_are_not_generic_noise(self):
        for relative in (
            'agb-werkstatt/agb-werkstatt-hauptproblem.md',
            'geldwaeschebeauftragter/geldwaeschebeauftragter-werkstatt.md',
            'krankenhaus-it-ki/krankenhaus-it-ki-schnellstart.md',
        ):
            with self.subTest(path=relative), patch.object(H, 'prompt_files', return_value=[H.REPO / relative]), \
                    redirect_stdout(io.StringIO()):
                self.assertEqual(H.main(), 0)

    def test_reviewed_source_context_is_bound_to_exact_paragraph_and_file(self):
        for relative, reviewed in H.REVIEWED_SOURCE_PARAGRAPHS.items():
            text = (H.REPO / relative).read_text(encoding='utf-8')
            paragraphs = H.re.split(r'\n\s*\n', text)
            noisy = [paragraph for paragraph in paragraphs if any(
                marker in H.visible_prose(paragraph) for marker in H.NOISE_BITS)]
            observed = {hashlib.sha256(' '.join(paragraph.split()).encode()).hexdigest() for paragraph in noisy}
            self.assertEqual(set(reviewed), observed, relative)
            self.assertTrue(all(reviewed.values()))
            self.assertEqual(H.source_noise(text, relative), [])
            for paragraph in noisy:
                with self.subTest(path=relative, paragraph=paragraph[:60]):
                    self.assertTrue(H.source_noise(paragraph, 'anderes-plugin/werkstatt.md'))
                    self.assertTrue(H.source_noise(paragraph + ' Statt Primärquellen genügt Modellwissen.', relative))
                    self.assertEqual(H.source_noise(paragraph.replace(' ', '\n'), relative), [])

    def test_generic_source_noise_stays_rejected_in_reviewed_files(self):
        for relative in H.REVIEWED_SOURCE_PARAGRAPHS:
            original = (H.REPO / relative).read_text(encoding='utf-8')
            for marker in H.NOISE_BITS:
                with self.subTest(path=relative, marker=marker):
                    self.assertIn(marker, H.source_noise(original + '\n\n' + marker + '\n', relative))

    def test_reviewed_source_context_does_not_hide_other_hygiene_errors(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            relative = 'fachgebiet/werkstatt.md'
            path = root / relative
            path.parent.mkdir()
            paragraph = 'Fundstellen über amtliche Quellen prüfen (unvollständig.'
            digest = hashlib.sha256(paragraph.encode()).hexdigest()
            path.write_text(paragraph, encoding='utf-8')
            with patch.dict(H.REVIEWED_SOURCE_PARAGRAPHS, {relative: {digest: 'Fixture'}}), \
                    patch.object(H, 'REPO', root), patch.object(H, 'prompt_files', return_value=[path]), \
                    redirect_stdout(io.StringIO()) as output:
                self.assertEqual(H.main(), 1)
            self.assertIn('unausgeglichene Klammer', output.getvalue())
            self.assertNotIn('Quellenrauschen', output.getvalue())

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
