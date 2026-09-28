#!/usr/bin/env python3
"""Lesefassung mit Register; Klageerwiderung bleibt als eigener Abschnitt erkennbar."""

from __future__ import annotations

import importlib.util
import io
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from xml.sax.saxutils import escape

from akten_build_runtime import serif_font_path
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_office_pdf import OFFICE_EXTS, render_office_batch

SCRIPTS = Path(__file__).resolve().parent
SLUG = 'fintech-darlehen-vertragsuebernahme-bremen'
GROUPS = {'01_eingang':'Eingang: Gericht, Klage und Anlagen K1 bis K12',
          '02_klageerwiderung':'Gesonderte Klageerwiderung und Anlagen B1 bis B6',
          '03_korrespondenz':'Korrespondenz und Buchungsunterlagen'}


def sources(case):
    paths = [path for path, _ in document_arcname_pairs(case)]
    def order(path):
        relative = path.relative_to(case)
        name = path.name
        rank = 0 if name.startswith('00_Gerichtliche') else 1 if name.startswith('01_Klage') else 2
        return (relative.parts[0], rank, name.casefold())
    return sorted(paths, key=order)


def converter():
    spec = importlib.util.spec_from_file_location('fintech_individual', SCRIPTS/'build-testakten-einzelpdf-zips.py')
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def build_release_pdf(case):
    docs = sources(case)
    office = [p for p in docs if p.suffix.lstrip('.') in OFFICE_EXTS]
    cache = render_office_batch(office)
    if set(cache) != set(office):
        raise RuntimeError('Native Office-Konvertierung fehlt für die bearbeitbaren Schriftsatzunterlagen')
    renderer = converter()
    rendered = [(path, renderer.render_document_pdf(path, case, cache)) for path in docs]
    if any(not data for _, data in rendered):
        raise RuntimeError('Unvollständige Einzelkonvertierung')
    readers = [(path, PdfReader(io.BytesIO(data))) for path, data in rendered]
    rows_per_page = 22
    register_pages = (len(readers)+rows_per_page-1)//rows_per_page
    start_page = register_pages+1
    positions = []
    for path, reader in readers:
        positions.append((path, start_page, len(reader.pages)))
        start_page += len(reader.pages)
    pdfmetrics.registerFont(TTFont('FintechRegister', str(serif_font_path())))
    pdfmetrics.registerFont(TTFont('FintechRegisterBold', str(serif_font_path(True))))
    output = io.BytesIO()
    canvas = Canvas(output, pagesize=A4, invariant=1)
    style = ParagraphStyle('Register', fontName='FintechRegister', fontSize=9, leading=11)
    for offset in range(0, len(positions), rows_per_page):
        canvas.setFont('FintechRegisterBold', 16)
        canvas.drawString(48, 795, 'Weserfunken Darlehensverfahren Bremen')
        canvas.setFont('FintechRegister', 10)
        canvas.drawString(48, 774, 'Landgericht Bremen | 4 O 1186/26 | Aktenstand 28.09.2026')
        canvas.drawString(48, 750, 'Dokumentenregister; Seitenzahlen beziehen sich auf diese Lesefassung.')
        y = 720
        for path, start, count in positions[offset:offset+rows_per_page]:
            para = Paragraph(escape(path.relative_to(case).as_posix()), style)
            _, height = para.wrap(427, 28)
            if height > 28:
                raise ValueError('Registereintrag zu lang: '+path.name)
            para.drawOn(canvas, 48, y-height)
            canvas.setFont('FintechRegister', 9)
            canvas.drawRightString(548, y-10, f'{start}–{start+count-1}')
            y -= 28
        canvas.setFont('FintechRegister', 8)
        canvas.drawString(48, 39, f'Register {offset//rows_per_page+1} / {register_pages}')
        canvas.showPage()
    canvas.save()
    writer = PdfWriter()
    writer.append(PdfReader(io.BytesIO(output.getvalue())))
    groups = {}
    for (path, reader), (_, start, _) in zip(readers, positions):
        folder = path.relative_to(case).parts[0]
        writer.append(reader, import_outline=False)
        if folder not in groups:
            groups[folder] = writer.add_outline_item(GROUPS[folder], start-1)
        writer.add_outline_item(path.stem, start-1, parent=groups[folder])
    writer.add_metadata({'/Title':'Weserfunken Darlehensverfahren Bremen', '/Author':'Klotzkette'})
    target = case/'gesamt-pdf'/(case.name+'_gesamt.pdf')
    target.parent.mkdir(exist_ok=True)
    temporary = target.with_suffix('.tmp')
    try:
        writer.write(temporary)
        assert len(PdfReader(temporary).pages) == start_page-1
        temporary.replace(target)
    finally:
        temporary.unlink(missing_ok=True)
    return target


if __name__ == '__main__':
    print(build_release_pdf(SCRIPTS.parent/'testakten'/SLUG))
