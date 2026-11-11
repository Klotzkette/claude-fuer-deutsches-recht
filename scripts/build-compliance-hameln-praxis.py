#!/usr/bin/env python3
"""Erzeugt die Hamelner Praxisakten mit Sachverhalt und drei Arbeitsrunden."""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
from hashlib import sha256
from html import escape
from io import BytesIO
import importlib.util
import json
from pathlib import Path
import re
from zipfile import ZipFile

from pypdf import PdfReader
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME, notice_text_errors
from testakte_einzelpdf_common import document_arcname_pairs

ROOT = Path(__file__).resolve().parents[1]
TAG = 'compliance-hameln-praxis-v1.0.0'
BUNDLE = 'Hameln_Compliance_39_Praxisakten.zip'
ENTRY = '00_Einstieg.pdf'
NEW_CASES = (
    ('ME-37', 'schokolade-charge-k17'),
    ('ME-38', 'geschenk-geschaeftsfuehrung'),
    ('ME-39', 'sicherheitsrelais-hinweis'),
)


def load_script(filename):
    spec = importlib.util.spec_from_file_location(filename, ROOT / 'scripts' / filename)
    script = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script)
    return script


def cases():
    material = ROOT / 'scripts/data/compliance-hameln-vertiefung.json'
    entries = [{key: item[key] for key in ('nr', 'slug', 'title')}
               for item in json.loads(material.read_text(encoding='utf-8'))['cases']]
    for nr, suffix in [('ME-36', 'auskunft-mit-schwaerzungen'),
                       *NEW_CASES]:
        slug = 'compliance-hameln-' + suffix
        title = (ROOT / 'testakten' / slug / 'README.md').read_text(encoding='utf-8').splitlines()[0]
        entries.append(dict(nr=nr, slug=slug, title=title.removeprefix('# ')))
    if len({case['slug'] for case in entries}) != 39:
        raise ValueError('39 unterschiedliche Hamelner Fälle erwartet.')
    return entries


def make_entry(case, destination):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.platypus import Paragraph, SimpleDocTemplate

    class FixedCanvas(Canvas):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **{**kwargs, 'invariant': 1})

    readme = (destination / 'README.md').read_text(encoding='utf-8')
    match = re.search(r'^## 1 Einstieg und Arbeitsauftrag\n(.*?)^<!-- BEGIN gesamt-pdf-section',
                      readme, re.M | re.S)
    if match is None:
        raise ValueError('Einstieg fehlt für ' + case['nr'])
    navy = colors.HexColor('#12263B')
    teal = colors.HexColor('#0B6567')
    grey = colors.HexColor('#384C60')
    normal = ParagraphStyle('Body', fontName='Helvetica', fontSize=11, leading=16,
                            spaceAfter=10, textColor=navy, alignment=TA_LEFT, splitLongWords=True)
    title = ParagraphStyle('Title', parent=normal, fontName='Helvetica-Bold',
                           fontSize=26, leading=30, spaceAfter=14)
    heading = ParagraphStyle('Heading', parent=normal, fontName='Helvetica-Bold',
                             textColor=teal, fontSize=12, leading=17, spaceBefore=5, keepWithNext=True)
    step = ParagraphStyle('Step', parent=normal, leftIndent=19, firstLineIndent=-19, spaceAfter=8)

    def plain(markdown):
        markdown = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', markdown)
        return escape(markdown.replace('**', '').replace('`', ''))

    def frame(canvas, _document):
        width, height = A4
        canvas.setStrokeColor(teal)
        canvas.setLineWidth(1.5)
        canvas.line(48, height - 59, width - 48, height - 59)
        canvas.setFillColor(grey)
        canvas.setFont('Helvetica-Bold', 9)
        canvas.drawString(48, height - 47, 'COMPLIANCE · HAMELN')
        canvas.drawRightString(width - 48, height - 47, case['nr'])
        canvas.setFont('Helvetica', 9)
        canvas.drawString(48, 38, 'Sachverhalt und Arbeitsauftrag')
        canvas.drawRightString(width - 48, 38, str(canvas.getPageNumber()))

    flow = [Paragraph(plain(case['title']), title)]
    for block in re.split(r'\n\s*\n', match.group(1).strip()):
        if block.startswith('### '):
            flow.append(Paragraph(plain(block[4:]), heading))
        elif re.match(r'^[0-9]+\. ', block):
            for line in block.splitlines():
                flow.append(Paragraph(plain(line), step))
        else:
            flow.append(Paragraph(plain(' '.join(block.splitlines())), normal))
    out = destination / ENTRY
    document = SimpleDocTemplate(str(out), pagesize=A4, topMargin=79, bottomMargin=61,
                                 leftMargin=48, rightMargin=48, title=case['title'],
                                 author='Compliance-Werkstatt Hameln')
    document.build(flow, onFirstPage=frame, onLaterPages=frame, canvasmaker=FixedCanvas)
    reader = PdfReader(out)
    if len(reader.pages) not in (1, 2) or any(len(page.extract_text() or '') < 150 for page in reader.pages):
        raise ValueError('Einstieg mit unbrauchbarem Umbruch: ' + case['nr'])


def archived_individual_pdfs(case, basis, directory, dist, native):
    is_first_series = case['nr'] != 'ME-36'
    previous_dir = basis / ('35' if is_first_series else '36')
    inventory = json.loads((previous_dir / 'release-bestand.json').read_text(encoding='utf-8'))
    previous_tag = 'compliance-abteilung-grosskonzern-v445.35.13' if is_first_series else 'compliance-hameln-auskunft-v1.0.0'
    if inventory['tag'] != previous_tag:
        raise ValueError('Falscher Basisrelease für ' + case['nr'])
    record = next(c for c in inventory['cases'] if c['nr'] == case['nr']) if is_first_series else inventory['case']
    name = record['individual']
    source_zip = previous_dir / name
    pairs = document_arcname_pairs(directory)
    original_hashes = {path.name: sha256(path.read_bytes()).hexdigest()
                       for path, _ in pairs if path.name != ENTRY}
    if original_hashes != record['source_sha256'] or pairs[0][0].name != ENTRY:
        raise ValueError('Basisdokumente verändert: ' + case['nr'])
    with ZipFile(source_zip) as prior, ZipFile(dist / name, 'x') as updated:
        expected = [NOTICE_FILENAME, *(archive_name for path, archive_name in pairs if path.name != ENTRY)]
        if set(prior.namelist()) != set(expected) or notice_text_errors(prior.read(NOTICE_FILENAME)):
            raise ValueError('Unvollständiges PDF-Archiv: ' + case['nr'])
        if not is_first_series and sha256(source_zip.read_bytes()).hexdigest() != inventory['assets'][name]:
            raise ValueError('Basisarchiv für ME-36 weicht ab.')
        native.write_bytes(updated, NOTICE_BYTES, NOTICE_FILENAME)
        for path, archive_name in pairs:
            data = path.read_bytes() if path.name == ENTRY else prior.read(archive_name)
            if (is_first_series and path.name != ENTRY
                    and sha256(data).hexdigest() != inventory['archives'][name][archive_name]['sha256']):
                raise ValueError('Basis-PDF weicht ab: ' + archive_name)
            native.write_bytes(updated, data, archive_name)
    return dist / name


def build_case(task):
    case, destination, basis = task
    dist = Path(destination)
    builder = load_script('build-compliance-hameln-release.py')
    prepared = None
    if int(case['nr'][3:]) <= 36:
        directory = ROOT / 'testakten' / case['slug']
        make_entry(case, directory)
        native = builder.module('build-testakten-release-zips.py')
        prepared = archived_individual_pdfs(case, Path(basis), directory, dist, native)
    result = builder.build_case((case, str(dist), True), individual=prepared)
    if case['nr'] in ('ME-37', 'ME-38', 'ME-39'):
        expected = {'ME-37': 12, 'ME-38': 9, 'ME-39': 9}
        if result['documents'] != expected[case['nr']]:
            raise ValueError('Native Arbeitsunterlagen unvollständig: ' + case['nr'])
    return result


def verify(dist):
    files = {path.name for path in dist.iterdir()}
    inventory = json.loads((dist / 'release-bestand.json').read_text(encoding='utf-8'))
    recorded = dict(line.split('  ', 1)[::-1] for line in
                    (dist / 'checksums-sha256.txt').read_text(encoding='utf-8').splitlines())
    if (inventory['tag'] != TAG or len(inventory['cases']) != 39 or len(files) != 120
            or set(recorded) != files - {'checksums-sha256.txt'}
            or inventory['assets'] != {name: digest for name, digest in recorded.items()
                                       if name != 'release-bestand.json'}):
        raise ValueError('Releaseinventar stimmt nicht mit der Dateiliste überein.')
    for name, digest in recorded.items():
        if sha256((dist / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Dateiprüfsumme weicht ab: ' + name)
    with ZipFile(dist / BUNDLE) as bundle:
        check_notice(bundle)
        for case in inventory['cases']:
            original_path = dist / case['original']
            if bundle.read(original_path.name) != original_path.read_bytes():
                raise ValueError('Originalpaket im Sammel-ZIP weicht ab: ' + case['slug'])
            with ZipFile(original_path) as original, ZipFile(dist / case['individual']) as separate:
                check_notice(original)
                check_notice(separate)
                combined_name = case['slug'] + '_gesamt.pdf'
                data = (dist / combined_name).read_bytes()
                if (original.read(combined_name) != data
                        or sha256(data).hexdigest() != case['combined_sha256']):
                    raise ValueError('Lesefassung weicht ab: ' + case['slug'])
                for name, digest in case['source_sha256'].items():
                    if sha256(original.read(name)).hexdigest() != digest:
                        raise ValueError('Originaldokument weicht ab: ' + name)
                combined = PdfReader(BytesIO(data))
                separate_names = separate.namelist()[1:]
                destinations = [combined.get_destination_page_number(entry) for entry in combined.outline]
                page = 0
                expected = []
                for name in separate_names:
                    expected.append(page)
                    page += len(PdfReader(BytesIO(separate.read(name))).pages)
                if (destinations != expected or page != case['pages'] or page != len(combined.pages)
                        or len(separate_names) != case['documents']
                        or {entry.title for entry in combined.outline} != set(case['source_sha256'])):
                    raise ValueError('Dokumentenfolge oder Seitenzahl weicht ab: ' + case['slug'])
                if int(case['nr'][3:]) <= 36 and (combined.outline[0].title != ENTRY
                        or separate.read(ENTRY) != original.read(ENTRY)):
                    raise ValueError('Einstiegsseite fehlt: ' + case['slug'])
    print(f'{len(files)} Dateien und 39 Akten mit Prüfhinweisen, Originalen und Lesefassungen verifiziert.')


def check_notice(archive):
    names = archive.namelist()
    if (names[0] != NOTICE_FILENAME or notice_text_errors(archive.read(NOTICE_FILENAME))
            or len(names) != len(set(names)) or any('/' in name or '\\' in name for name in names)
            or archive.testzip()):
        raise ValueError('Fehlerhafte oder unzulässige ZIP-Struktur: ' + archive.filename)


def build(dist, basis, jobs):
    if (ROOT / 'testakten/compliance-hameln-schokolade-charge-k17/Grundakte').is_dir():
        raise ValueError(f'Für den historischen Workshop-Stand bitte den Tag {TAG} auschecken.')
    if dist.exists() and any(dist.iterdir()):
        raise ValueError('Das Ausgabeziel muss leer sein.')
    dist.mkdir(parents=True, exist_ok=True)
    all_cases = cases()
    with ProcessPoolExecutor(max_workers=jobs) as executor:
        results = list(executor.map(build_case, ((case, dist, basis) for case in all_cases)))
    builder = load_script('build-compliance-hameln-release.py')
    native = builder.module('build-testakten-release-zips.py')
    with ZipFile(dist / BUNDLE, 'x') as archive:
        native.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for case in results:
            path = dist / case['original']
            native.write_file(archive, path, path.name)
            template = ROOT / builder.PLUGIN / 'templates' / (case['slug'] + '.docx')
            if template.is_file():
                native.write_file(archive, template, template.name)
    files = sorted(dist.iterdir())
    assets = {path.name: sha256(path.read_bytes()).hexdigest() for path in files}
    expected_count = 3 * len(all_cases) + 1
    if len(assets) != expected_count:
        raise ValueError(f'{expected_count} Akten- und Sammeldateien erwartet.')
    inventory = dist / 'release-bestand.json'
    inventory.write_text(json.dumps({'tag': TAG, 'cases': results, 'assets': assets}, ensure_ascii=False, indent=2)
                         + '\n', encoding='utf-8')
    assets[inventory.name] = sha256(inventory.read_bytes()).hexdigest()
    (dist / 'checksums-sha256.txt').write_text(
        ''.join(f'{digest}  {name}\n' for name, digest in sorted(assets.items())), encoding='utf-8')
    verify(dist)
    print(f'{TAG}: {len(results)} Akten, {sum(c["documents"] for c in results)} Dokumente, '
          f'{sum(c["pages"] for c in results)} Seiten, {len(assets) + 1} Dateien.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    parser.add_argument('--verify', action='store_true', help='Ein bestehendes Release unabhängig prüfen.')
    parser.add_argument('--basis', type=Path,
                        help='Veröffentlichte Einzel-PDF-ZIPs und Inventare in Unterordnern 35 und 36.')
    parser.add_argument('--jobs', type=int, default=4)
    args = parser.parse_args()
    if args.verify:
        verify(args.dist.resolve())
    elif args.basis:
        build(args.dist.resolve(), args.basis.resolve(), args.jobs)
    else:
        parser.error('--basis wird zum Bauen benötigt.')
