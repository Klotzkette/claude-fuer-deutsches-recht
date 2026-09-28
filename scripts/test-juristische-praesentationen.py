#!/usr/bin/env python3
"""Regressionen für Präsentationsvorlage, Paketprüfung und Plugin-Integration."""

from __future__ import annotations

import importlib.util
import json
import re
import tempfile
import unittest
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch
from xml.etree import ElementTree as ET
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'juristische-praesentationen'
PLUGIN = ROOT / SLUG
DECK = PLUGIN / 'assets/juristische-praesentation-vorlage.pptx'
spec = importlib.util.spec_from_file_location('presentation_check', PLUGIN / 'scripts/pptx_pruefen.py')
CHECK = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CHECK)
NS = {'p': CHECK.P, 'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
MEDIA = {'e6d525f40b6946a13718573e067e8a05a7882e8248e2d8d0346c7d931c4c3be9',
         '488edc74fae51bd9a7f84f7b5da72174d5d8479bc0ca866c25eee704ec29ccb1'}


class PresentationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        with ZipFile(DECK) as z:
            self.parts = {n: z.read(n) for n in z.namelist()}

    def mutated(self, changes):
        target = Path(self.tmp.name) / 'mutation.pptx'
        parts = {**self.parts, **changes}
        with ZipFile(target, 'w', ZIP_DEFLATED) as z:
            for n, b in parts.items():
                if b is not None:
                    z.writestr(n, b)
        return target

    def test_template_integrity_and_design(self):
        report = CHECK.inspect(DECK, template=True)
        self.assertEqual(report['errors'], [])
        self.assertEqual((report['slides'], report['layouts']), (6, 23))
        self.assertEqual(report['animations'], 0)
        self.assertEqual(report['playback_check'], 'nicht durchgeführt')
        root = ET.fromstring(self.parts['ppt/presentation.xml'])
        size = root.find('p:sldSz', NS)
        self.assertEqual((size.get('cx'), size.get('cy')), ('9144000', '5143500'))
        theme = ET.fromstring(self.parts['ppt/theme/theme1.xml'])
        colors = {n.get('val') for n in theme.iter(f"{{{NS['a']}}}srgbClr")}
        self.assertTrue({'19243F', 'F7F7F7', 'EA5474'} <= colors)

    def test_template_contains_only_reviewed_media_and_no_old_payloads(self):
        media = {sha256(b).hexdigest() for n, b in self.parts.items() if n.startswith('ppt/media/')}
        self.assertEqual(media, MEDIA)
        self.assertFalse(any(n.startswith(('ppt/embeddings/', 'ppt/tags/', 'customXml/', 'ppt/comments/', 'docProps/thumbnail')) for n in self.parts))
        for n, data in self.parts.items():
            if n.endswith('.rels'):
                self.assertFalse(any(x.get('TargetMode') == 'External' for x in ET.fromstring(data)))
        for n in ('docProps/core.xml', 'docProps/app.xml'):
            fields = {x.tag.split('}')[-1] for x in ET.fromstring(self.parts[n])}
            self.assertFalse(fields & {'creator', 'lastModifiedBy', 'Company', 'Manager', 'Template', 'Application'})

    def test_broken_relationship_is_rejected(self):
        broken = self.parts['ppt/_rels/presentation.xml.rels'].replace(b'slides/slide1.xml', b'slides/missing.xml')
        report = CHECK.inspect(self.mutated({'ppt/_rels/presentation.xml.rels': broken}))
        self.assertTrue(any('Verknüpfungsziel fehlt' in e for e in report['errors']))

    def test_presentation_root_requires_correct_name_and_namespace(self):
        name = 'ppt/presentation.xml'
        for tag in ('presentation', f'{{{CHECK.P}}}other', '{urn:other}presentation'):
            with self.subTest(tag=tag):
                root = ET.fromstring(self.parts[name])
                root.tag = tag
                report = CHECK.inspect(self.mutated({name: ET.tostring(root)}), template=True)
                self.assertTrue(any('Wurzelelement' in e for e in report['errors']))

    def test_slide_ids_must_be_present_and_nonempty(self):
        name = 'ppt/presentation.xml'
        for value in (None, '', '   '):
            with self.subTest(value=value):
                root = ET.fromstring(self.parts[name])
                first = root.find(f'{{{CHECK.P}}}sldIdLst/{{{CHECK.P}}}sldId')
                if value is None:
                    first.attrib.pop('id')
                else:
                    first.set('id', value)
                report = CHECK.inspect(self.mutated({name: ET.tostring(root)}), template=True)
                self.assertTrue(any('leere oder doppelte IDs' in e for e in report['errors']))
        root = ET.fromstring(self.parts[name])
        root.find(f'{{{CHECK.P}}}sldIdLst').clear()
        self.assertTrue(any('Folienfolge fehlt' in e for e in CHECK.inspect(
            self.mutated({name: ET.tostring(root)}), template=True)['errors']))

    def test_slide_sequence_rejects_external_relationship(self):
        name = 'ppt/_rels/presentation.xml.rels'
        presentation = ET.fromstring(self.parts['ppt/presentation.xml'])
        entry = presentation.find(f'{{{CHECK.P}}}sldIdLst/{{{CHECK.P}}}sldId')
        root = ET.fromstring(self.parts[name])
        relation = next(rel for rel in root if rel.get('Id') == entry.get(f'{{{CHECK.R}}}id'))
        relation.set('TargetMode', 'External')
        relation.set('Target', 'https://example.invalid/slide1.xml')
        report = CHECK.inspect(self.mutated({name: ET.tostring(root)}), template=True)
        self.assertTrue(any('ungültigen Folienverweis' in e for e in report['errors']))

        root = ET.fromstring(self.parts[name])
        ET.SubElement(root, f'{{{CHECK.PACKAGE_R}}}Relationship', {
            'Id': 'externalLink', 'Type': f'{CHECK.R}/hyperlink',
            'TargetMode': 'External', 'Target': 'https://example.invalid/'})
        report = CHECK.inspect(self.mutated({name: ET.tostring(root)}), template=True)
        self.assertEqual(report['errors'], [])
        self.assertTrue(any('Externe Verknüpfung' in w for w in report['warnings']))

    def test_archive_paths_and_budget_are_bounded(self):
        report = CHECK.inspect(self.mutated({'../outside.txt': b'bad'}))
        self.assertIn('Unsicherer Paketpfad.', report['errors'])
        with patch.object(CHECK, 'MAX_BYTES', 10):
            self.assertTrue(CHECK.inspect(DECK)['errors'])

    def test_duplicate_parts_and_invalid_xml_are_rejected(self):
        target = self.mutated({})
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            with ZipFile(target, 'a') as z:
                z.writestr('ppt/presentation.xml', b'<broken>')
        self.assertIn('Doppelte Paketpfade.', CHECK.inspect(target)['errors'])
        self.assertTrue(CHECK.inspect(self.mutated({'ppt/presentation.xml': b'<broken>'}))['errors'])

    def test_hidden_terms_across_text_runs_are_detected(self):
        data = b'<root><t>Private</t><t> Kanzlei</t></root>'
        target = self.mutated({'docProps/custom.xml': data})
        self.assertTrue(CHECK.inspect(target, ('private  kanzlei',))['errors'])

    def test_forbidden_name_split_across_formatted_runs(self):
        data = b'<root>\n <r><t>Priv</t></r>\n <r><t>ate</t></r>\n</root>'
        target = self.mutated({'docProps/custom.xml': data})
        self.assertTrue(any('Suchbegriff' in e for e in CHECK.inspect(target, ('PRIVATE',))['errors']))
        self.assertFalse(CHECK.inspect(target, ('unrelated',), template=True)['errors'])

    def test_dtd_rejected_in_utf8_and_utf16(self):
        payload = '<!DOCTYPE root [<!ENTITY x "expanded">]><root>&x;</root>'
        for encoding in ('utf-8', 'utf-16', 'utf-16-be', 'utf-16-le'):
            with self.subTest(encoding=encoding):
                data = ('<?xml version="1.0" encoding="' + encoding + '"?>' + payload).encode(encoding)
                report = CHECK.inspect(self.mutated({'docProps/custom.xml': data}))
                self.assertTrue(report['errors'])
                self.assertTrue(any('DTD' in e or 'encoding' in e for e in report['errors']))
        safe = '<?xml version="1.0" encoding="UTF-16"?><root>Größe</root>'.encode('utf-16')
        self.assertFalse(CHECK.inspect(self.mutated({'docProps/custom.xml': safe}), template=True)['errors'])

    def test_missing_external_target_and_disguised_internal_url(self):
        name = 'ppt/_rels/presentation.xml.rels'
        for mode, target in (('External', ''), ('Internal', 'https://example.invalid/ppt/slides/slide1.xml'),
                             ('Internal', '//example.invalid/ppt/slides/slide1.xml'),
                             ('Internal', 'slides/%6dissing.xml'), ('wrong', 'slides/slide1.xml')):
            with self.subTest(mode=mode, target=target):
                root = ET.fromstring(self.parts[name])
                root[0].set('TargetMode', mode)
                root[0].set('Target', target)
                self.assertTrue(CHECK.inspect(self.mutated({name: ET.tostring(root)}))['errors'])

    def test_uncompressed_and_xml_budgets(self):
        target = self.mutated({'large.txt': b'x' * (2 * 1024 * 1024)})
        budget = target.stat().st_size + 1024
        with ZipFile(target) as archive:
            self.assertGreater(sum(info.file_size for info in archive.infolist()), budget)
        with patch.object(CHECK, 'MAX_BYTES', budget):
            self.assertTrue(any('Entpackter Inhalt' in e for e in CHECK.inspect(target)['errors']))
        with patch.object(CHECK, 'MAX_PARTS', 1):
            self.assertTrue(CHECK.inspect(DECK)['errors'])
        with patch.object(CHECK, 'MAX_XML_BYTES', 10):
            self.assertTrue(any('XML-Bestandteil' in e for e in CHECK.inspect(DECK)['errors']))

    def test_unsupported_compression_reports_failure(self):
        with patch.object(CHECK.ZipFile, 'open', side_effect=NotImplementedError('compression unavailable')):
            self.assertIn('compression unavailable', CHECK.inspect(DECK)['errors'])

    def test_active_objects_and_missing_animation_targets_are_rejected(self):
        self.assertTrue(CHECK.inspect(self.mutated({'ppt/embeddings/oleObject1.bin': b'old'}))['errors'])
        root = ET.fromstring(self.parts['ppt/slides/slide1.xml'])
        ET.SubElement(root, f'{{{CHECK.P}}}spTgt', {'spid': '999999'})
        target = self.mutated({'ppt/slides/slide1.xml': ET.tostring(root)})
        self.assertTrue(any('Animationsziel fehlt' in e for e in CHECK.inspect(target)['errors']))

    def test_template_mode_does_not_hide_real_errors(self):
        a = CHECK.inspect(DECK)
        b = CHECK.inspect(DECK, template=True)
        self.assertTrue(any('Inhaltsfeld' in w for w in a['warnings']))
        self.assertFalse(any('Inhaltsfeld' in w for w in b['warnings']))
        broken = self.mutated({'ppt/presentation.xml': None})
        self.assertTrue(CHECK.inspect(broken, template=True)['errors'])

    def test_package_checks_leave_input_unchanged(self):
        before = DECK.read_bytes()
        CHECK.inspect(DECK)
        self.assertEqual(DECK.read_bytes(), before)

    def test_twelve_skills_and_separate_prompts(self):
        skills = sorted((PLUGIN / 'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skills), 12)
        self.assertIn('serioes-animieren', {p.parent.name for p in skills})
        self.assertIn('jugendgerecht-umformulieren', {p.parent.name for p in skills})
        mini = PLUGIN / f'{SLUG}-schnellstart.md'
        workshop = PLUGIN / f'{SLUG}-werkstatt.md'
        self.assertLessEqual(len(mini.read_bytes()), 7500)
        self.assertGreater(len(workshop.read_bytes()), 16000)
        self.assertFalse(any(p.parent.name.endswith(('schnellstart', 'werkstatt')) for p in skills))
        for path in skills:
            text = path.read_text(encoding='utf-8')
            self.assertNotIn(chr(167), text)
            for heading in range(1, 7):
                self.assertRegex(text, rf'(?m)^## {heading}\. ')

    def test_local_runtime_links_stay_inside_installed_plugin(self):
        from markdown_it import MarkdownIt
        from urllib.parse import unquote, urlsplit
        for path in [*(PLUGIN / 'skills').glob('*/SKILL.md'), *(PLUGIN / 'references').glob('*.md')]:
            for token in MarkdownIt().parse(path.read_text(encoding='utf-8')):
                for child in token.children or []:
                    if child.type != 'link_open':
                        continue
                    url = urlsplit(child.attrGet('href') or '')
                    if url.scheme or not url.path:
                        continue
                    resolved = (path.parent / unquote(url.path)).resolve()
                    self.assertTrue(resolved.is_relative_to(PLUGIN))
                    self.assertTrue(resolved.is_file(), str(resolved))

    def test_manifest_matches_marketplace(self):
        market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
        entry = next(p for p in market['plugins'] if p['name'] == SLUG)
        manifest = json.loads((PLUGIN / '.claude-plugin/plugin.json').read_text())
        for field in ('name', 'version', 'description', 'author'):
            self.assertEqual(entry[field], manifest[field])
        self.assertEqual(manifest['version'], market['version'])


if __name__ == '__main__':
    unittest.main()
