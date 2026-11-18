#!/usr/bin/env python3
"""Negative Prüfungen des aktuellen Checkouts und der getrennten Releasepfade."""
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile, ZIP_DEFLATED

from pypdf import PdfWriter
import yaml
from testakte_disclaimer import NOTICE_BYTES

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('insolvenz_checkout', ROOT/'scripts/check-insolvenz-components-checkout.py')
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


class CheckoutTests(unittest.TestCase):
    def test_all_current_plugin_packages_bind_exact_current_bytes(self):
        for component in C.COMPONENTS:
            with self.subTest(component=component), tempfile.TemporaryDirectory() as folder:
                dist = Path(folder)
                for name in C.COMPONENTS[component]:
                    files = C.Q.source_files(ROOT, ROOT/name)
                    for suffix, prefix in (('', ''), ('-portable', name+'/')):
                        C.Q.write_zip(dist/(name+suffix+'.zip'), files, prefix)
                evidence = C.inspect_plugins(component, dist, ROOT)
                self.assertEqual(set(evidence), set(C.COMPONENTS[component]))
                entries = C.current_entries(component, ROOT)
                for name in evidence:
                    self.assertEqual(evidence[name]['version'], entries[name]['version'])

    def test_changed_skill_missing_extra_and_duplicate_zip_member_are_rejected(self):
        component = 'insolvenzverwaltung-berichtsersteller'
        files = C.Q.source_files(ROOT, ROOT/component)
        for change in ('skill', 'manifest-version', 'missing', 'extra', 'duplicate'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as folder:
                dist = Path(folder)
                C.Q.write_zip(dist/(component+'-portable.zip'), files, component+'/')
                target = dist/(component+'.zip')
                data = {name: path.read_bytes() for name, path in files.items()}
                if change == 'skill':
                    key = next(name for name in data if name.endswith('/SKILL.md'))
                    data[key] += b'\nUngepruefte Aenderung\n'
                elif change == 'manifest-version':
                    key = '.claude-plugin/plugin.json'
                    manifest = json.loads(data[key]);manifest['version'] = '1.1.0'
                    data[key] = json.dumps(manifest).encode()
                elif change == 'missing':
                    del data[next(name for name in data if name.endswith('/SKILL.md'))]
                elif change == 'extra':
                    data['ungeprueft.md'] = b'extra'
                with ZipFile(target, 'w', ZIP_DEFLATED) as archive:
                    for name, raw in data.items(): archive.writestr(name, raw)
                    if change == 'duplicate': archive.writestr('README.md', data['README.md'])
                with self.assertRaises(ValueError): C.inspect_plugins(component, dist, ROOT)

    def test_current_marketplace_rejects_wrong_version_and_missing_exact_pin(self):
        component = 'insolvenzverwaltung-berichtsersteller'
        for change in ('version', 'pin'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as folder:
                root = Path(folder);(root/'.claude-plugin').mkdir();(root/'scripts/data').mkdir(parents=True);(root/component).mkdir()
                version = '777.1.0';tag = 'qualitaetsrunde-v'+version
                market = {'version': version, 'plugins': [{'name': component, 'version': version, 'source': './'+component}]}
                pins = {'schema_version': 1, 'assets': {component+suffix+'.zip': tag for suffix in ('', '-portable')}}
                (root/'.claude-plugin/marketplace.json').write_text(json.dumps(market));(root/'scripts/scoped-release-assets.json').write_text(json.dumps(pins))
                self.assertEqual(C.current_entries(component, root)[component]['version'], version)
                if change == 'version':
                    market['plugins'][0]['version'] = '1.1.0';(root/'.claude-plugin/marketplace.json').write_text(json.dumps(market))
                else:
                    del pins['assets'][component+'-portable.zip'];(root/'scripts/scoped-release-assets.json').write_text(json.dumps(pins))
                with self.assertRaises(ValueError):C.current_entries(component, root)

    def test_missing_or_unrelated_release_scope_allows_independently_pinned_versions(self):
        component = 'insolvenzanfechtung'
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);(root/'.claude-plugin').mkdir();(root/'scripts/data').mkdir(parents=True)
            versions=dict(zip(C.COMPONENTS[component],('777.1.0','776.9.9')))
            market={'version':'777.1.0','plugins':[{'name':name,'version':version,'source':'./'+name} for name,version in versions.items()]}
            pins={'schema_version':1,'assets':{name+suffix+'.zip':'qualitaetsrunde-v'+version for name,version in versions.items() for suffix in ('','-portable')}}
            (root/'.claude-plugin/marketplace.json').write_text(json.dumps(market));(root/'scripts/scoped-release-assets.json').write_text(json.dumps(pins))
            for scope in (None, {'version':'999.1.0','plugins':[{'name':'ganz-anderes-plugin'}]}):
                if scope is not None:(root/'scripts/data/skill-quality-release-scope.json').write_text(json.dumps(scope))
                result=C.current_entries(component,root)
                self.assertEqual({name:entry['version'] for name,entry in result.items()},versions)

    def case_fixture(self, root, dist):
        slug = 'probe';directory = root/'testakten'/slug;(directory/'gesamt-pdf').mkdir(parents=True)
        (directory/'unterlage.txt').write_text('Tatsaechlicher Akteninhalt')
        buffer = io.BytesIO();writer = PdfWriter();writer.add_blank_page(width=595, height=842);writer.write(buffer);pdf=buffer.getvalue()
        combined = directory/'gesamt-pdf'/f'{slug}_gesamt.pdf';combined.write_bytes(pdf);(dist/combined.name).write_bytes(pdf)
        originals = C.working_dump_archive_pairs(directory, include_gesamt_pdf=C.source_zip_includes_gesamt_pdf(directory))
        with ZipFile(dist/f'testakte-{slug}.zip', 'w') as archive:
            archive.writestr('README.txt', NOTICE_BYTES)
            for source, name in originals:archive.write(source,name)
        C.load('build-testakten-einzelpdf-zips.py').build_single(directory, dist)
        return slug

    def test_each_case_checks_original_bytes_pdf_completeness_and_combined_pdf(self):
        for change in ('source', 'missing-single', 'blank-single', 'combined'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as folder:
                root=Path(folder);dist=root/'out';dist.mkdir();slug=self.case_fixture(root,dist)
                self.assertTrue(C.inspect_case(slug,dist,root)['sources'])
                if change=='source':(root/'testakten'/slug/'unterlage.txt').write_text('Anderer ungepruefter Stand')
                elif change=='combined':(dist/f'{slug}_gesamt.pdf').write_bytes(b'changed')
                else:
                    with ZipFile(dist/f'testakte-{slug}-einzelpdfs.zip','w') as archive:
                        archive.writestr('README.txt',NOTICE_BYTES)
                        if change=='blank-single':
                            writer=PdfWriter();writer.add_blank_page(width=595,height=842);buffer=io.BytesIO();writer.write(buffer)
                            archive.writestr('unterlage.pdf',buffer.getvalue())
                with self.assertRaises(ValueError):C.inspect_case(slug,dist,root)

    def test_historical_release_and_current_checkout_have_separate_event_guards(self):
        for component in C.COMPONENTS:
            path=ROOT/'.github/workflows'/f'{component}-release.yml';workflow=yaml.safe_load(path.read_text())
            steps=workflow['jobs']['release']['steps'];current=[];historical=[]
            for step in steps:
                command=step.get('run','')
                if 'check-insolvenz-components-checkout.py' in command or 'test-insolvenz-components-checkout.py' in command:
                    current.append(step);self.assertEqual(step.get('if'), "github.event_name == 'pull_request'")
                    self.assertIn('--verify',command)
                if f'build-{component}-release.py' in command:
                    historical.append(step);self.assertEqual(step.get('if'), "github.event_name == 'workflow_dispatch'")
                    self.assertIn(f'test-{component}.py --dist',command)
                if any(name in command for name in ('build-insolvenzanfechtung-akten.py', 'build-fintech-bremen-pakete.py',
                                                     'build-insolvenzsachbearbeitung-betriebsakten.py', 'build-insolvenzsachbearbeitung-verbraucherakte.py')):
                    self.assertEqual(step.get('if'), "github.event_name == 'workflow_dispatch'")
            self.assertEqual(len(current),1);self.assertEqual(len(historical),1)
            self.assertTrue(any(f'test-{component}.py\n' in step.get('run','') and not step.get('if') for step in steps))
            self.assertNotIn('--scope scripts/data/insolvenzanfechtung-pruefumfang.json',path.read_text())
            self.assertNotIn('--case-assets',current[0]['run'])
            if component == 'insolvenzsachbearbeitung':
                self.assertIn('--current-checkout --report "$RUNNER_TEMP/', current[0]['run'])

    def test_current_case_regression_cannot_overwrite_historical_report(self):
        result=subprocess.run([sys.executable,str(ROOT/'scripts/test-insolvenzsachbearbeitung-betriebsakten.py'),
                               '--current-checkout'],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0)
        self.assertIn('Bericht außerhalb des Quellrepositories',result.stderr)


if __name__ == '__main__':unittest.main()
