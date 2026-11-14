#!/usr/bin/env python3
"""Prüft Quellenidentität, Promptgrenzen und den veröffentlichten Aktenumfang."""
import argparse, hashlib, importlib.util, json, re, subprocess, sys, tempfile, unittest, zipfile
from pathlib import Path
from pypdf import PdfReader
from release_routing import scoped_asset_url, validate_plugin_version
ROOT=Path(__file__).resolve().parents[1]
def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def check_component_version(entry, market_version, *, root=ROOT, expected_version=None):
    """Aktuelle Quellenroute prüfen; historische Releaseversion nur im Dist-Lauf pinnen."""
    name, version = entry['name'], entry['version']
    validate_plugin_version(entry, market_version, root=root)
    route = scoped_asset_url(f'{name}.zip', root=root)
    assert route and route.endswith(f'-v{version}/{name}.zip'), f'{name}: Paketroute'
    directory = (root / entry['source']).resolve()
    assert directory.is_relative_to(root.resolve()), f'{name}: Pluginquelle'
    assert (directory / '.claude-plugin/plugin.json').is_file(), f'{name}: Manifest fehlt'
    for relative in ('plugin.json', '.claude-plugin/plugin.json', '.codex-plugin/plugin.json'):
        path = directory / relative
        if path.is_file():
            manifest = json.loads(path.read_text())
            assert (manifest['name'], manifest['version']) == (name, version), str(path)
    if expected_version is not None:
        assert version == expected_version, f'{name}: historische Releaseversion'


class ComponentVersionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.entry = {'name': 'example', 'version': '1.1.0', 'source': './example'}
        self.manifest = self.root / 'example/.claude-plugin/plugin.json'
        self.manifest.parent.mkdir(parents=True)
        self.manifest.write_text(json.dumps({'name': 'example', 'version': '1.1.0'}))
        self.routes = self.root / 'scripts/scoped-release-assets.json'
        self.routes.parent.mkdir()
        self.route('qualitaetsrunde-v1.1.0')

    def route(self, tag):
        self.routes.write_text(json.dumps({'schema_version': 1, 'assets': {'example.zip': tag}}))

    def test_current_source_accepts_matching_new_component(self):
        check_component_version(self.entry, '1.0.0', root=self.root)

    def test_stale_route_rejected_even_at_catalog_version(self):
        self.route('qualitaetsrunde-v1.0.0')
        with self.assertRaises(AssertionError):
            check_component_version(self.entry, '1.1.0', root=self.root)

    def test_stale_manifest_is_rejected(self):
        self.manifest.write_text(json.dumps({'name': 'example', 'version': '1.0.0'}))
        with self.assertRaises(AssertionError):
            check_component_version(self.entry, '1.1.0', root=self.root)

    def test_historical_dist_requires_its_exact_version(self):
        with self.assertRaises(AssertionError):
            check_component_version(self.entry, '1.0.0', root=self.root, expected_version='1.0.0')
        check_component_version(self.entry, '1.0.0', root=self.root, expected_version='1.1.0')


def check(dist=None):
    build=module('build-phishing-release');market=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text());entries={e['name']:e for e in market['plugins']}
    for name in build.PLUGINS:
        check_component_version(entries[name], market['version'],
                                expected_version=build.VERSION if dist else None)
        profile=json.loads((ROOT/'quality/evals'/f'{name}.json').read_text())
        for kind,key in (('schnellstart','mini_review'),('werkstatt','workshop_review')):
            path=ROOT/name/f'{name}-{kind}.md'
            if path.exists():assert profile[key]['sha256']==hashlib.sha256(path.read_bytes()).hexdigest(),str(path)
    for path in build.prompts():
        if path.name.endswith(('-schnellstart.md','-hauptproblem.md')):
            data=path.read_bytes();assert len(data.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n'))<=7500,path.name
    p=ROOT/'betreuungsrecht/betreuungsrecht-unterlagen-werkstatt.md';assert p.read_bytes()==p.with_suffix('.txt').read_bytes()
    subprocess.run([sys.executable,str(ROOT/'scripts/test-phishing-tukowiecka.py')],check=True)
    if dist:
        assert {p.name for p in dist.iterdir()}==build.asset_names(),'Assetliste'
        report=json.loads((dist/'quellenabgleich.json').read_text())
        assert report['tag']==build.TAG,'Historischer Releasetag'
        assert set(report['plugins'])==set(build.PLUGINS),'Komponentenbestand'
        assert all(item['version']==build.VERSION for item in report['plugins'].values()),'Komponentenversionen'
        expected={}
        for line in (dist/'checksums-sha256.txt').read_text().splitlines():
            digest,name=line.split('  ',1);assert name not in expected;expected[name]=digest
            assert hashlib.sha256((dist/name).read_bytes()).hexdigest()==digest,name
        assert set(expected)==build.asset_names()-{'checksums-sha256.txt'}
        for name in build.PLUGINS:
            files=build.sources(name)
            for portable in (False,True):
                prefix=f'{name}/' if portable else ''
                with zipfile.ZipFile(dist/f'{name}{"-portable" if portable else ""}.zip') as archive:
                    assert len(archive.namelist())==len(files)
                    assert set(archive.namelist())=={prefix+n for n in files}
                    for n,p in files.items():assert archive.read(prefix+n)==p.read_bytes(),f'{name}/{n}'
        for p in build.prompts():assert (dist/p.name).read_bytes()==p.read_bytes(),p.name
        case=ROOT/'testakten'/build.CASE
        from testakte_einzelpdf_common import document_arcname_pairs
        from testakte_disclaimer import NOTICE_BYTES
        pairs=document_arcname_pairs(case);assert len(pairs)==28
        with zipfile.ZipFile(dist/build.CASE_ASSETS[0]) as original,zipfile.ZipFile(dist/build.CASE_ASSETS[1]) as individual:
            assert original.read('README.txt').startswith(NOTICE_BYTES)
            assert individual.read('README.txt').startswith(NOTICE_BYTES)
            assert len([n for n in individual.namelist() if n.endswith('.pdf')])==28
            total=0
            import io
            aggregate=PdfReader(dist/build.CASE_ASSETS[2])
            for source,pdfname in pairs:
                assert original.read(source.name)==source.read_bytes()
                for page in PdfReader(io.BytesIO(individual.read(pdfname))).pages:
                    assert page.extract_text()==aggregate.pages[total].extract_text();total+=1
            record=json.loads((ROOT/'quality/phishing-vorfall-pruefer/testakte-pruefung.json').read_text())
            assert total==len(aggregate.pages)==record['packages']['aggregate_pages']
            assert original.read(build.CASE_ASSETS[2])==(dist/build.CASE_ASSETS[2]).read_bytes()
        for name in ('phishing-vorfall-pruefer-werkstatt.pdf','phishing-vorfall-pruefer-schnellstart.pdf'):
            text='\n'.join(p.extract_text() or '' for p in PdfReader(dist/name).pages)
            assert 'C-70/25' in text and 'Tukowiecka' in text and '675u' in text,name
    print('Phishing: Quellen, sieben Komponenten, Promptgrenzen und '+('Releasepakete' if dist else 'Regressionen')+' geprüft.')
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--dist',type=Path);a=p.parse_args()
    result=unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(ComponentVersionTests))
    if not result.wasSuccessful():sys.exit(1)
    check(a.dist.resolve() if a.dist else None)
