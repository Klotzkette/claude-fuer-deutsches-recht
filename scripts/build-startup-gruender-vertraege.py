#!/usr/bin/env python3
"""Baut Schnittflug-Vertragsentwürfe und die zugehörigen Auslagenbelege.

Verträge verwenden den gemeinsamen DOCX-Helfer, Belege sind durchsuchbare
A4-PDFs. Es werden keine Steuer- oder Registerkennungen ergänzt. Der separate
Zahlungsvermerk entspricht dem Stand der privaten Gründerablage.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.pdfgen.canvas import Canvas

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'scripts/data/startup-gruender'
CASE = ROOT / 'testakten/startup-gruender-schnittflug-berlin'


def load_helper():
    spec = importlib.util.spec_from_file_location('startup_lebensakte', ROOT / 'scripts/build-startup-gruender-lebensakte.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fonts():
    candidates = [Path('/System/Library/Fonts/Supplemental'), Path('/usr/share/fonts/truetype/msttcorefonts')]
    for base in candidates:
        regular = base / 'Times New Roman.ttf'
        bold = base / 'Times New Roman Bold.ttf'
        if regular.exists() and bold.exists():
            pdfmetrics.registerFont(TTFont('SchnittflugTimes', str(regular)))
            pdfmetrics.registerFont(TTFont('SchnittflugTimesBold', str(bold)))
            return 'SchnittflugTimes', 'SchnittflugTimesBold'
    # CI machines without the Microsoft font use the metrically compatible face.
    for base in [Path('/usr/share/fonts/truetype/liberation2'), Path('/usr/share/fonts/truetype/liberation')]:
        regular = base / 'LiberationSerif-Regular.ttf'
        bold = base / 'LiberationSerif-Bold.ttf'
        if regular.exists() and bold.exists():
            pdfmetrics.registerFont(TTFont('SchnittflugTimes', str(regular)))
            pdfmetrics.registerFont(TTFont('SchnittflugTimesBold', str(bold)))
            return 'SchnittflugTimes', 'SchnittflugTimesBold'
    raise RuntimeError('Times New Roman oder Liberation Serif wird für Beleg-PDFs benötigt.')


def money(cents: int):
    sign = '-' if cents < 0 else ''
    euros, rest = divmod(abs(cents), 100)
    return f'{sign}{euros:,}'.replace(',', '.') + f',{rest:02d} EUR'


def date_de(iso: str):
    year, month, day = iso.split('-')
    return f'{day}.{month}.{year}'


class StableCanvas(Canvas):
    def __init__(self, *args, **kwargs):
        kwargs['invariant'] = 1
        super().__init__(*args, **kwargs)


def receipt(row: dict, folder: Path, regular: str, bold: str):
    assert row['net_cents'] + row['vat_cents'] == row['gross_cents']
    expected_vat = int((Decimal(row['net_cents']) * Decimal(str(row['vat_rate']))).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    assert expected_vat == row['vat_cents']
    base = ParagraphStyle('body', fontName=regular, fontSize=11, leading=15, spaceAfter=8)
    small = ParagraphStyle('small', parent=base, fontSize=9, leading=12, textColor=colors.HexColor('#4f565b'))
    heading = ParagraphStyle('heading', parent=base, fontName=bold, fontSize=17, leading=21, spaceAfter=10)
    label = ParagraphStyle('label', parent=base, fontName=bold, fontSize=11, leading=14)
    right = ParagraphStyle('right', parent=base, alignment=TA_RIGHT)
    content = []
    content.append(Paragraph(escape(row['supplier']), heading))
    content.append(Paragraph(escape(row['supplier_address']), base))
    content.append(Spacer(1, 18*mm))
    content.append(Paragraph('An ' + escape(row['recipient']), base))
    content.append(Spacer(1, 9*mm))
    credit = row['gross_cents'] < 0
    content.append(Paragraph('Rechnungskorrektur' if credit else 'Rechnung', heading))
    content.append(Paragraph('Belegnummer ' + escape(row['document_number']) + ' · Datum ' + date_de(row['date']), base))
    content.append(Spacer(1, 5*mm))
    content.append(Paragraph('Wir schreiben Ihnen den nachstehenden Betrag gut.' if credit else 'Wir berechnen Ihnen die nachstehende Leistung.', base))
    content.append(Paragraph(escape(row['description']), base))
    content.append(Spacer(1, 8*mm))
    sums = [
        [Paragraph('Nettobetrag', base), Paragraph(money(row['net_cents']), right)],
        [Paragraph('Umsatzsteuer 19 Prozent', base), Paragraph(money(row['vat_cents']), right)],
        [Paragraph('Gesamtbetrag der Korrektur' if credit else 'Rechnungsbetrag', label), Paragraph(money(row['gross_cents']), ParagraphStyle('total', parent=right, fontName=bold))],
    ]
    table = Table(sums, colWidths=[108*mm, 53*mm])
    table.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), .6, colors.HexColor('#d9d9d9')),
        ('INNERGRID', (0, 0), (-1, -1), .4, colors.HexColor('#d9d9d9')),
        ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#edf1f3')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 9), ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    content.append(table)
    content.append(Spacer(1, 8*mm))
    if not row['paid_date']:
        content.append(Paragraph(escape(row['payment']) + '.', base))
        content.append(Paragraph('Bitte geben Sie bei Zahlung die Belegnummer an.', base))
    elif credit:
        content.append(Paragraph('Die Rückzahlung erfolgt auf das bei der ursprünglichen Zahlung verwendete Zahlungsmittel.', base))
    else:
        content.append(Paragraph('Vielen Dank für Ihren Auftrag.', base))
    content.append(Spacer(1, 10*mm))
    note = [Paragraph('Zahlungsvermerk der Gründerablage', label),
            Paragraph('Stand 28.09.2026 · Interne Zuordnung ' + escape(row['id']), small),
            Paragraph(escape(row['payment']), base)]
    if row['paid_date']:
        note.append(Paragraph(('Erstattung' if credit else 'Zahlung') + ' vermerkt am ' + date_de(row['paid_date']) + '.', base))
    note_table = Table([[note]], colWidths=[161*mm])
    note_table.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), .6, colors.HexColor('#d9d9d9')),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f7f7f5')),
        ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 9), ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    content.append(KeepTogether(note_table))
    filename = folder / row['filename']
    doc = SimpleDocTemplate(str(filename), pagesize=A4, rightMargin=24*mm, leftMargin=24*mm,
                            topMargin=20*mm, bottomMargin=20*mm, title=row['document_number'],
                            author=row['supplier'], subject='Rechnungskorrektur' if credit else 'Rechnung')
    doc.build(content, canvasmaker=StableCanvas)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=CASE)
    args = parser.parse_args()
    rows = json.loads((DATA_DIR / 'vertraege.json').read_text(encoding='utf-8'))
    finance = json.loads((DATA_DIR / 'finanz.json').read_text(encoding='utf-8'))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    helper = load_helper()
    for row in rows:
        # Layout only: keep final clauses off nearly empty continuation pages.
        row['layout'] = {'vertical_margin_cm': 1.9, 'paragraph_space_after_pt': 4, 'line_spacing': 1.06}
        if row['file'].startswith('31_'):
            row['layout'].update({'paragraph_space_after_pt': 6, 'line_spacing': 1.15})
        break_before = {'33': [4], '34': [5], '36': [4], '37': [3], '38': [3]}
        for section_number in break_before.get(row['file'][:2], []):
            row['sections'][section_number - 1]['page_break_before'] = True
        helper.save_docx(row, args.output_dir)
    regular, bold = fonts()
    for row in finance['receipts']:
        receipt(row, args.output_dir, regular, bold)
    print(json.dumps({'docx': len(rows), 'pdf': len(finance['receipts'])}))


if __name__ == '__main__':
    main()
