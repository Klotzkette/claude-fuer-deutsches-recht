#!/usr/bin/env python3
"""Geordnete Gesamtakte und Projektordner-ZIPs. Autor: Klotzkette."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import zipfile
from xml.sax.saxutils import escape

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from bauwirtschaft_hildesheim_lebensakte_common import ROOT, CASE, SLUG, ASSETS, setup_fonts
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_office_pdf import render_office_batch, OFFICE_EXTS, OFFICE_BATCH_SIZE


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def fingerprint(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sources(case_dir=CASE):
    return [path for path, _ in document_arcname_pairs(case_dir)]


def render(case_dir=CASE, *, manifests=(), cache_dir=None):
    cache_dir = cache_dir or ASSETS/'pakete-qa'
    cache_dir.mkdir(parents=True, exist_ok=True)
    renderer = module('lebensakte_einzelpdf', 'build-testakten-einzelpdf-zips.py')
    prepared = {}
    for manifest in manifests:
        rows = json.loads(Path(manifest).read_text())
        for row in rows:
            if all(key in row for key in ('source', 'sha256', 'pdf')):
                prepared[row['source']] = row
    pipeline = hashlib.sha256(b''.join((ROOT/'scripts'/name).read_bytes() for name in (
        Path(__file__).name, 'build-testakten-einzelpdf-zips.py', 'build-testakte-gesamt-pdf.py',
        'testakte_office_pdf.py', 'testakte_einzelpdf_common.py', 'testakte_file_filter.py'))).hexdigest()
    paths = document_arcname_pairs(case_dir)
    index = []
    for start in range(0, len(paths), OFFICE_BATCH_SIZE):
        group = paths[start:start+OFFICE_BATCH_SIZE]
        states = []
        office_pending = []
        for source, arcname in group:
            relative = source.relative_to(case_dir).as_posix()
            digest = fingerprint(source)
            folder = cache_dir/relative
            folder.mkdir(parents=True, exist_ok=True)
            target = folder/(source.stem+'.pdf')
            marker = folder/'source.json'
            wanted = {'sha256': digest, 'pipeline': pipeline}
            cached = target.exists() and marker.exists() and json.loads(marker.read_text()) == wanted
            supplied = prepared.get(relative)
            if not cached and supplied and supplied['sha256'] == digest and Path(supplied['pdf']).is_file():
                # Genau die bereits visuell geprüfte Office-Lesefassung übernehmen.
                data = renderer.normalize_pdf_to_a4(Path(supplied['pdf']).read_bytes(), relative)
                if not PdfReader(io.BytesIO(data)).pages:
                    raise ValueError('Leere vorbereitete Lesefassung: '+relative)
                target.write_bytes(data)
                marker.write_text(json.dumps(wanted))
                cached = True
            if not cached and source.suffix.lstrip('.') in OFFICE_EXTS:
                office_pending.append(source)
            states.append((source, relative, arcname, digest, target, marker, wanted, cached))
        office = render_office_batch(office_pending)
        if set(office_pending)-set(office):
            raise RuntimeError('Native Office-Konvertierung fehlt: '+', '.join(str(p) for p in set(office_pending)-set(office)))
        for source, relative, arcname, digest, target, marker, wanted, cached in states:
            if not cached:
                data = renderer.render_document_pdf(source, case_dir, office)
                if not data:
                    raise RuntimeError('Keine Lesefassung: '+relative)
                target.write_bytes(data)
                marker.write_text(json.dumps(wanted))
            if fingerprint(source) != digest:
                raise RuntimeError('Original während der Konvertierung geändert: '+relative)
            pages = len(PdfReader(target).pages)
            if not pages:
                raise RuntimeError('Leere Lesefassung: '+relative)
            index.append({'source': relative, 'sha256': digest, 'pdf': str(target), 'arcname': arcname, 'pages': pages})
            print(f'{relative}: {pages} Seiten', flush=True)
    (cache_dir/'index.json').write_text(json.dumps(index, ensure_ascii=False, indent=2)+'\n')
    return index


def aggregate(index, case_dir=CASE, *, cache_dir=None):
    cache_dir = cache_dir or ASSETS/'pakete-qa'
    cache_dir.mkdir(parents=True, exist_ok=True)
    setup_fonts()
    body = ParagraphStyle('Body', fontName='Hildesheim', fontSize=11, leading=14, spaceAfter=9)
    title = ParagraphStyle('Title', parent=body, fontName='HildesheimBold', fontSize=17, leading=21, spaceAfter=14)
    small = ParagraphStyle('Small', parent=body, fontSize=8.5, leading=11, wordWrap='CJK')
    def p(text, style=body):
        return Paragraph(escape(str(text)), style)
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E8EDF0')),
        ('GRID', (0, 0), (-1, -1), .25, colors.HexColor('#D9D9D9')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ])
    register = cache_dir/'register.pdf'
    def invariant(*args, **kwargs):
        kwargs['invariant'] = 1
        return canvas.Canvas(*args, **kwargs)
    def register_footer(canvas, document):
        canvas.saveState()
        canvas.setFont('Hildesheim', 9)
        canvas.drawString(50, 25, 'SW-HI-26-08 · Dokumentenregister')
        canvas.drawRightString(A4[0]-50, 25, f'Seite {document.page}')
        canvas.restoreState()
    register_pages = 0
    # Die Seitenverweise berücksichtigen den eigenen Umfang des Registers.
    # Neu bauen, bis die gedruckten Startseiten dem tatsächlichen PDF entsprechen.
    for attempt in range(6):
        start_page = register_pages+1
        rows = [[p('Projektordner und Originaldatei', small), p('Ab Seite', small), p('Umfang', small)]]
        for row in index:
            rows.append([p(row['source'], small), p(start_page, small), p(row['pages'], small)])
            start_page += row['pages']
        table = Table(rows, colWidths=[397, 48, 50], repeatRows=1)
        table.setStyle(table_style)
        SimpleDocTemplate(str(register), pagesize=A4, leftMargin=50, rightMargin=50, topMargin=48, bottomMargin=45,
                          title='Projektakte Wohnhof Am Steinbogen', author='Klotzkette').build([
            p('Projektakte Wohnhof Am Steinbogen', title),
            p('Achtfamilienhaus in Hildesheim · SW-HI-26-08'),
            p('Projektunterlagen von Erwerb und Planung bis zur Objektbetreuung. Das Hauptprojekt betrifft die Vermietung; '
              'Ordner 13 enthält ausschließlich eine noch nicht beschlossene Verkaufsoption.'),
            p(f'Das Register weist {len(index)} Originaldateien aus. Die Ablage folgt den Projektordnern. '
              '„Ab Seite“ bezeichnet die PDF-Seite dieser Gesamtakte, „Umfang“ die Seitenzahl der einzelnen Lesefassung. '
              'Maßgeblich für den zeitlichen Stand sind die Datierung und gegebenenfalls eine ausdrücklich zugeordnete Berichtigung der jeweiligen Unterlage.'),
            Spacer(1, 7), table,
        ], canvasmaker=invariant, onFirstPage=register_footer, onLaterPages=register_footer)
        actual = len(PdfReader(register).pages)
        if actual == register_pages:
            break
        register_pages = actual
    else:
        raise RuntimeError('Seitenverweise des Dokumentenregisters konvergieren nicht.')
    writer = PdfWriter()
    writer.append(register, outline_item='Dokumentenregister')
    folders = {}
    for row in index:
        start = len(writer.pages)
        writer.append(row['pdf'], import_outline=False)
        parent = None
        parts = Path(row['source']).parts
        for depth in range(1, len(parts)):
            key = '/'.join(parts[:depth])
            if key not in folders:
                folders[key] = writer.add_outline_item(parts[depth-1], start, parent=parent)
            parent = folders[key]
        writer.add_outline_item(row['source'], start, parent=parent)
    writer.add_metadata({'/Author': 'Klotzkette', '/Creator': 'Klotzkette', '/Producer': 'Klotzkette',
                         '/Title': 'Hildesheim Achtfamilienhaus Projektakte mit Bautagebuch'})
    target = case_dir/'gesamt-pdf'/f'{case_dir.name}_gesamt.pdf'
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name('.'+target.name+'.tmp')
    with temporary.open('wb') as stream:
        writer.write(stream)
    temporary.replace(target)
    print(f'Gesamtakte: {len(index)} Originale, {len(writer.pages)} Seiten, {target}', flush=True)
    return target


def build_release_pdf(case_dir=CASE):
    if case_dir.name != SLUG:
        raise ValueError('Falsche Projektakte: '+case_dir.name)
    cache = ASSETS/'release-qa'
    return aggregate(render(case_dir, cache_dir=cache), case_dir, cache_dir=cache)


def package(index, dist, case_dir=CASE):
    dist.mkdir(parents=True, exist_ok=True)
    total = aggregate(index, case_dir)
    builder = module('lebensakte_original_zip', 'build-testakten-release-zips.py')
    original, _ = builder.build_single(case_dir, dist)
    single = dist/f'testakte-{case_dir.name}-einzelpdfs.zip'
    with zipfile.ZipFile(single, 'w', zipfile.ZIP_DEFLATED) as archive:
        builder.write_bytes(archive, NOTICE_BYTES, NOTICE_FILENAME)
        for row in index:
            builder.write_file(archive, Path(row['pdf']), row['arcname'])
    return original, single, total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--qa-manifest', action='append', default=[])
    parser.add_argument('--release-pdf-only', action='store_true')
    parser.add_argument('--package-only', action='store_true')
    parser.add_argument('--dist', type=Path, default=ASSETS/'dist')
    args = parser.parse_args()
    if args.release_pdf_only:
        build_release_pdf()
        return
    if args.package_only:
        index = json.loads((ASSETS/'pakete-qa/index.json').read_text())
        current = {p.relative_to(CASE).as_posix(): fingerprint(p) for p, _ in document_arcname_pairs(CASE)}
        if current != {row['source']: row['sha256'] for row in index}:
            raise RuntimeError('Originale haben sich nach der Konvertierung geändert.')
    else:
        index = render(manifests=args.qa_manifest)
    for path in package(index, args.dist):
        print(path)


if __name__ == '__main__':
    main()
