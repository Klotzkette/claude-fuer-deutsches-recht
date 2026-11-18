#!/usr/bin/env python3
"""Prüft aktuelle Insolvenzpakete und vollständige Akten ohne Release-Freigabe.

Historische Builder, Versionen und Veröffentlichungsnachweise bleiben strikt.
Nur deren reine Prompt-Renderer werden für den aktuellen Prüfbestand verwendet.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
from zipfile import ZipFile

from pypdf import PdfReader
from release_routing import scoped_asset_url, validate_plugin_version, verified_scoped_package_version
from testakte_disclaimer import NOTICE_BYTES
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_office_pdf import office_binary, valid_office_container
from testakte_zip_common import source_zip_includes_gesamt_pdf, working_dump_archive_pairs

ROOT = Path(__file__).resolve().parents[1]
COMPONENTS = {
    'insolvenzanfechtung': ('insolvenzanfechtung', 'fachanwalt-insolvenz-sanierungsrecht'),
    'insolvenzsachbearbeitung': ('insolvenzsachbearbeitung', 'insolvenzforderungen-checker'),
    'insolvenzverwaltung-berichtsersteller': ('insolvenzverwaltung-berichtsersteller',),
}
REPORT = 'checkout-pruefung.json'
CHECKSUMS = 'checksums-sha256.txt'
PURPOSE = 'current-checkout-validation-only'


def load(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('-', '_'), ROOT/'scripts'/filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


Q = load('build-skill-quality-release.py')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def historical(component, root):
    module = load(f'build-{component}-release.py')
    module.ROOT = root
    return module


def current_entries(component, root):
    market = json.loads((root/'.claude-plugin/marketplace.json').read_text())
    entries = {}
    for name in COMPONENTS[component]:
        matches = [row for row in market['plugins'] if row['name'] == name]
        if len(matches) != 1 or matches[0].get('source') != './'+name:
            raise ValueError(f'{name}: eindeutige aktuelle Pluginquelle fehlt')
        entry = matches[0]
        validate_plugin_version(entry, market['version'], root=root)
        for suffix in ('', '-portable'):
            asset = name+suffix+'.zip'
            route = scoped_asset_url(asset, root=root)
            if route is None:
                raise ValueError(f'{asset}: exakte Komponentenroute fehlt')
            tag = route.rsplit('/', 2)[-2]
            if not (tag.endswith(f"-v{entry['version']}") or
                    verified_scoped_package_version(asset, tag, entry['version'], root=root)):
                raise ValueError(f'{asset}: Komponentenroute passt nicht zur aktuellen Pluginversion')
        entries[name] = entry
    return entries


def prompts(component, h, root):
    if hasattr(h, 'prompt_sources'):
        return [(source, h.prompt_asset(source)) for source in h.prompt_sources()]
    return [(root/component/f'{component}-{kind}.md', f'{component}-{kind}.md') for kind in h.KINDS]


def expected_names(h):
    return (h.asset_names() - {'quellenabgleich.json'}) | {REPORT}


def inspect_plugins(component, dist, root):
    entries = current_entries(component, root)
    evidence = {}
    for name in COMPONENTS[component]:
        entry = entries[name]
        directory = (root/entry['source']).resolve()
        if directory != root/name:
            raise ValueError(f'{name}: falsche lokale Pluginquelle')
        files = Q.source_files(root, directory)
        manifests = Q.check_manifests(files, name, entry['version'])
        for manifest in manifests:
            if json.loads(files[manifest].read_text()).get('description') != entry['description']:
                raise ValueError(f'{name}: Manifestbeschreibung weicht vom Marketplace ab')
        skills = Q.verify_reachability(files)
        packages = {}
        for suffix, prefix in (('', ''), ('-portable', name+'/')):
            packages[name+suffix+'.zip'] = Q.verify_zip(dist/(name+suffix+'.zip'), files, prefix)
        Q.CHECKS.validate_plugin_zip(dist, name, entry['version'])
        Q.CHECKS.validate_skill_sources(dist/f'{name}.zip', directory)
        Q.CHECKS.validate_focus_skill(dist/f'{name}.zip', directory, root/'quality/evals'/f'{name}.json')
        evidence[name] = {'version': entry['version'], 'manifests': manifests, 'skills': skills, 'packages': packages}
    return evidence


def inspect_case(slug, dist, root):
    directory = root/'testakten'/slug
    original_pairs = working_dump_archive_pairs(directory, include_gesamt_pdf=source_zip_includes_gesamt_pdf(directory))
    pdf_pairs = document_arcname_pairs(directory)
    if not original_pairs or not pdf_pairs:
        raise ValueError(f'{slug}: vollständige Arbeitsunterlagen fehlen')
    for source, _ in pdf_pairs:
        if source.suffix.lower() in {'.docx', '.xlsx', '.odt'} and not valid_office_container(source):
            raise ValueError(f'{slug}: ungültiges natives Office-Dokument: {source}')
    with ZipFile(dist/f'testakte-{slug}.zip') as archive:
        names = archive.namelist()
        expected = {'README.txt'} | {name for _, name in original_pairs}
        if len(names) != len(set(names)) or set(names) != expected or archive.testzip() is not None:
            raise ValueError(f'{slug}: Arbeitsdateien-ZIP ist unvollständig oder überzählig')
        if not archive.read('README.txt').startswith(NOTICE_BYTES):
            raise ValueError(f'{slug}: Aktenhinweis fehlt')
        for source, name in original_pairs:
            if archive.read(name) != source.read_bytes():
                raise ValueError(f'{slug}/{name}: ursprüngliche Arbeitsdatei verändert')
    # Eine gültige PDF-Seite allein belegt noch keine richtige Konvertierung.
    # Erneut aus sämtlichen Originalen rendern und jedes Mitglied bytegenau
    # abgleichen; temporäre Renderziele verlassen niemals den Prüfbereich.
    with tempfile.TemporaryDirectory(prefix='insolvenz-render-vergleich-') as temporary:
        expected_zip, _ = load('build-testakten-einzelpdf-zips.py').build_single(directory, Path(temporary))
        with ZipFile(expected_zip) as rebuilt:
            expected_pdfs = {name: rebuilt.read(name) for _, name in pdf_pairs}
    with ZipFile(dist/f'testakte-{slug}-einzelpdfs.zip') as archive:
        names = archive.namelist()
        expected = {'README.txt'} | {name for _, name in pdf_pairs}
        if len(names) != len(set(names)) or set(names) != expected or archive.testzip() is not None:
            raise ValueError(f'{slug}: Einzel-PDF-ZIP ist unvollständig oder überzählig')
        if not archive.read('README.txt').startswith(NOTICE_BYTES):
            raise ValueError(f'{slug}: Einzel-PDF-Hinweis fehlt')
        pdf_hashes = {}
        for source, name in pdf_pairs:
            data = archive.read(name)
            if not PdfReader(io.BytesIO(data)).pages:
                raise ValueError(f'{slug}/{name}: Einzel-PDF leer')
            if data != expected_pdfs[name]:
                raise ValueError(f'{slug}/{name}: Einzel-PDF weicht vom vollständigen Originalrendering ab')
            pdf_hashes[name] = hashlib.sha256(data).hexdigest()
    combined = directory/'gesamt-pdf'/f'{slug}_gesamt.pdf'
    if (dist/combined.name).read_bytes() != combined.read_bytes() or not PdfReader(combined).pages:
        raise ValueError(f'{slug}: Gesamt-PDF weicht von der geprüften Quelle ab')
    return {'sources': {source.relative_to(root).as_posix(): sha(source) for source, _ in original_pairs},
            'single_pdfs': pdf_hashes, 'combined_pdf': sha(combined)}


def inspect(component, dist, root):
    h = historical(component, root)
    expected = expected_names(h)
    if {p.name for p in dist.iterdir()} - {REPORT, CHECKSUMS} != expected - {REPORT, CHECKSUMS}:
        raise ValueError('Checkout-Prüfbestand ist unvollständig oder überzählig')
    if any(not p.is_file() or p.is_symlink() for p in dist.iterdir()):
        raise ValueError('Nur reguläre Prüfdateien zulässig')
    plugins = inspect_plugins(component, dist, root)
    prompt_evidence = {}
    for source, asset in prompts(component, h, root):
        twin = source.with_suffix('.txt')
        if source.read_bytes() != twin.read_bytes():
            raise ValueError(f'{source}: MD/TXT-Fassungen weichen ab')
        compact = source.read_bytes().replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
        if 'werkstatt' not in source.name and len(compact) > 7500:
            raise ValueError(f'{source}: Kompaktprompt überschreitet 7500 Bytes')
        for path in (source, twin):
            name = str(Path(asset).with_suffix(path.suffix))
            if (dist/name).read_bytes() != path.read_bytes():
                raise ValueError(f'{name}: Prompt weicht von der Quelle ab')
        pdf = dist/str(Path(asset).with_suffix('.pdf'))
        if hasattr(h, 'inspect_pdf'):
            details = h.inspect_pdf(source, pdf)
        else:
            h.VERSION = plugins[component]['version']
            with tempfile.TemporaryDirectory(prefix='insolvenz-prompt-vergleich-') as temporary:
                rendered = Path(temporary)/pdf.name
                h.render_prompt(source, rendered)
                if rendered.read_bytes() != pdf.read_bytes():
                    raise ValueError(f'{pdf.name}: Prompt-PDF weicht vom vollständigen Originalrendering ab')
            details = {'pages': len(PdfReader(pdf).pages)}
        if not details.get('pages'):
            raise ValueError(f'{pdf.name}: Prompt-PDF leer')
        prompt_evidence[asset] = {'source_sha256': sha(source), 'pdf_sha256': sha(pdf), 'inspection': details}
    cases = {slug: inspect_case(slug, dist, root) for slug in h.CASES}
    return {'schema_version': 1, 'purpose': PURPOSE, 'component': component,
            'plugins': plugins, 'prompts': prompt_evidence, 'cases': cases,
            'artifacts': {name: sha(dist/name) for name in sorted(expected-{REPORT, CHECKSUMS})},
            'source_state': Q.checkout_state(root)}


def validate(component, dist, root=ROOT):
    root, dist = root.resolve(), dist.resolve()
    if {p.name for p in dist.iterdir()} != expected_names(historical(component, root)):
        raise ValueError('Exakter Checkout-Dateibestand erforderlich')
    report = json.loads((dist/REPORT).read_text())
    if report != inspect(component, dist, root):
        raise ValueError('Checkout-Nachweis stimmt nicht mit den aktuellen Quellen überein')
    expected_checksums = ''.join(f'{sha(p)}  {p.name}\n' for p in sorted(dist.iterdir()) if p.name != CHECKSUMS)
    if (dist/CHECKSUMS).read_text() != expected_checksums:
        raise ValueError('Checkout-Prüfsummen weichen ab')
    return report


def build(component, dist, root=ROOT, case_assets=None):
    root, dist = root.resolve(), dist.resolve()
    if dist.is_relative_to(root):
        raise ValueError('Checkout-Prüfziel muss außerhalb des Quellrepositories liegen')
    entries = current_entries(component, root)
    h = historical(component, root)
    if component == 'insolvenzverwaltung-berichtsersteller' and not office_binary():
        raise RuntimeError('LibreOffice fehlt; vollständiger Office-Export erforderlich')
    dist.mkdir(parents=True, exist_ok=True)
    if any(dist.iterdir()):
        raise ValueError('Checkout-Prüfziel muss leer sein')
    for name in COMPONENTS[component]:
        files = Q.source_files(root, root/name)
        Q.check_manifests(files, name, entries[name]['version'])
        for suffix, prefix in (('', ''), ('-portable', name+'/')):
            Q.write_zip(dist/(name+suffix+'.zip'), files, prefix)
    # Nur das Renderetikett folgt der aktuellen Fassung; historische Buildguards
    # werden nicht aufgerufen oder verändert und kein Release-Nachweis entsteht.
    h.VERSION = entries[component]['version']
    for source, asset in prompts(component, h, root):
        for path in (source, source.with_suffix('.txt')):
            shutil.copyfile(path, dist/str(Path(asset).with_suffix(path.suffix)))
        h.render_prompt(source, dist/str(Path(asset).with_suffix('.pdf')))
    for slug in h.CASES:
        names = (f'testakte-{slug}.zip', f'testakte-{slug}-einzelpdfs.zip', f'{slug}_gesamt.pdf')
        if case_assets is not None:
            for name in names:
                shutil.copyfile(case_assets/name, dist/name)
        else:
            directory = root/'testakten'/slug
            load('build-testakten-release-zips.py').build_single(directory, dist)
            load('build-testakten-einzelpdf-zips.py').build_single(directory, dist)
            shutil.copyfile(directory/'gesamt-pdf'/names[2], dist/names[2])
    report = inspect(component, dist, root)
    (dist/REPORT).write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    (dist/CHECKSUMS).write_text(''.join(f'{sha(p)}  {p.name}\n' for p in sorted(dist.iterdir()) if p.name != CHECKSUMS))
    return validate(component, dist, root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--component', required=True, choices=COMPONENTS)
    parser.add_argument('--dist', required=True, type=Path)
    parser.add_argument('--case-assets', type=Path)
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    result = validate(args.component, args.dist) if args.verify else build(args.component, args.dist, case_assets=args.case_assets)
    print(f"{args.component}: {len(result['plugins'])} aktuelle Plugins, {len(result['prompts'])} Prompts und {len(result['cases'])} vollständige Akten geprüft; keine Release-Freigabe")
