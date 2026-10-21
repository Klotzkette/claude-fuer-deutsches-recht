#!/usr/bin/env python3
"""Prüft Quellenpaket, eigenständige Prompts und bytegenaue Release-Zuordnung."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote
import zipfile
import yaml
from quality_lab import validate_profile

ROOT = Path(__file__).resolve().parents[1]
NAME = 'insolvenzanfechtung'
PARENT = 'fachanwalt-insolvenz-sanierungsrecht'
DIST = None


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('-', '_'), ROOT/'scripts'/filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class AnfechtungTest(unittest.TestCase):
    def test_eleven_skills_are_activatable_and_references_resolve(self):
        skills = sorted((ROOT/NAME/'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skills), 11)
        for path in skills:
            text = path.read_text(encoding='utf-8')
            front = yaml.safe_load(text.split('---', 2)[1])
            self.assertEqual(set(front), {'name', 'description'})
            self.assertEqual(front['name'], path.parent.name)
            self.assertLessEqual(len(front['description']), 360)
            self.assertNotIn('§', front['description'])
            self.assertNotIn('im Plugin', front['description'])
            self.assertEqual(re.findall(r'^## ([1-6])\.', text, re.M), list('123456'))
            for word in ('Times New Roman', '11 pt', 'ausformuliert'):
                self.assertIn(word, text)
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if target.startswith(('https:', 'http:', '#', 'mailto:')):
                    continue
                target = unquote(target.split('#')[0])
                self.assertTrue((path.parent/target).resolve().exists(), f'{path}: {target}')

    def test_prompts_are_separate_complete_and_bounded(self):
        builder = module('build-insolvenzanfechtung-release.py')
        for source in builder.prompt_sources():
            self.assertEqual(source.read_bytes(), source.with_suffix('.txt').read_bytes())
            data = source.read_bytes().replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
            if 'werkstatt' not in source.name:
                self.assertLessEqual(len(data), 7500, source)
            else:
                self.assertGreater(len(source.read_text().split()), 6000)
            self.assertIn('Trägt nicht', source.read_text())
        profile = json.loads((ROOT/'quality/evals'/f'{NAME}.json').read_text())
        validate_profile(profile, NAME, ROOT/NAME)
        self.assertGreaterEqual(len(profile['sources']), 8)
        self.assertEqual(len(profile['cases']), 3)

    def test_manifests_and_marketplace_agree(self):
        market = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())
        for name, version in ((NAME, '1.0.0'), (PARENT, '445.35.4')):
            entries = [p for p in market['plugins'] if p['name'] == name]
            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0]['version'], version)
            for relative in (('plugin.json', '.claude-plugin/plugin.json', '.codex-plugin/plugin.json') if name == NAME else ('.claude-plugin/plugin.json',)):
                manifest = json.loads((ROOT/name/relative).read_text())
                self.assertEqual((manifest['name'], manifest['version']), (name, version))
                self.assertEqual(manifest['description'], entries[0]['description'])

    def test_release_assets_and_packages_are_byte_exact(self):
        if DIST is None:
            self.skipTest('--dist erforderlich')
        builder = module('build-insolvenzanfechtung-release.py')
        self.assertEqual({p.name for p in DIST.iterdir()}, builder.asset_names())
        lines = (DIST/'checksums-sha256.txt').read_text().splitlines()
        self.assertEqual(len(lines), len(builder.asset_names())-1)
        for line in lines:
            digest, name = line.split('  ', 1)
            self.assertEqual(sha(DIST/name), digest)
        for name in (NAME, PARENT):
            expected = builder.plugin_sources(name)
            for suffix, prefix in (('', ''), ('-portable', name+'/')):
                with zipfile.ZipFile(DIST/(name+suffix+'.zip')) as archive:
                    self.assertIsNone(archive.testzip())
                    self.assertEqual(set(archive.namelist()), {prefix+p for p in expected})
                    for relative, path in expected.items():
                        self.assertEqual(archive.read(prefix+relative), path.read_bytes())
                    for path in archive.namelist():
                        self.assertNotIn('..', Path(path).parts)
                        self.assertFalse(set(Path(path).parts) & {'testakte', 'testakten', 'prompts'})
        record = json.loads((DIST/'quellenabgleich.json').read_text())
        for source in builder.prompt_sources():
            asset = builder.prompt_asset(source)
            self.assertEqual((DIST/asset).read_bytes(), source.read_bytes())
            target = DIST/str(Path(asset).with_suffix('.pdf'))
            result = builder.inspect_pdf(source, target)
            for key, value in result.items():
                self.assertEqual(record['pdfs'][target.name][key], value)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path)
    args, remaining = parser.parse_known_args()
    DIST = args.dist.resolve() if args.dist else None
    unittest.main(argv=[__file__, *remaining])
