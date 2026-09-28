#!/usr/bin/env python3
"""Erzeugt ausschließlich die zehn nachgereichten Schnittflug-Finanzbelege."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def eur(cents: int) -> str:
    sign = '-' if cents < 0 else ''
    whole, rest = divmod(abs(cents), 100)
    return f'{sign}{whole:,}'.replace(',', '.') + f',{rest:02d} EUR'


def date(value: str) -> str:
    return '.'.join(reversed(value[:10].split('-')))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--qa-dir', type=Path, default=Path('/tmp/schnittflug-erweiterung/finanz-qa'))
    args = parser.parse_args()
    assert not args.qa_dir.resolve().is_relative_to(ROOT)
    args.qa_dir.mkdir(parents=True, exist_ok=True)
    data = json.loads((ROOT / 'scripts/data/startup-gruender/finanz-ergaenzung.json').read_text())
    facts = json.loads((ROOT / 'scripts/data/startup-gruender/fallstamm.json').read_text())
    dest = ROOT / 'testakten' / facts['case_slug']
    fonts = Path('/System/Library/Fonts/Supplemental')
    for name, file in [('TNR', 'Times New Roman.ttf'), ('TNRBold', 'Times New Roman Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(fonts / file)))
    body = ParagraphStyle('Body', fontName='TNR', fontSize=11, leading=15, spaceAfter=9)
    title = ParagraphStyle('Title', parent=body, fontName='TNRBold', fontSize=16, leading=20, spaceAfter=16)
    heading = ParagraphStyle('Heading', parent=body, fontName='TNRBold', fontSize=12, leading=16, spaceBefore=12, spaceAfter=8)
    small = ParagraphStyle('Small', parent=body, fontSize=9, leading=12, textColor=colors.HexColor('#444444'))
    right = ParagraphStyle('Right', parent=body, alignment=TA_RIGHT)
    manifest = []
    for row in data['documents']:
        output = dest / row['filename']
        story = [Paragraph(escape(row['supplier']), heading), Paragraph(escape(row['address']), small), Spacer(1, 11 * mm)]
        story += [Paragraph(escape(row['recipient']), body), Spacer(1, 8 * mm), Paragraph(escape(row['title']), title)]
        meta = [[Paragraph('Belegnummer', body), Paragraph(escape(row['number']), body)], [Paragraph('Belegdatum', body), Paragraph(date(row['date']), body)]]
        table = Table(meta, colWidths=[42 * mm, 123 * mm]); table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0)])); story.append(table)
        story += [Spacer(1, 4 * mm), Paragraph(escape(row['description']), body)]
        if row['kind'] in ('invoice', 'credit'):
            assert row['net_cents'] + row['vat_cents'] == row['gross_cents']
            amounts = [('Nettobetrag', row['net_cents']), ('Umsatzsteuer 19 %', row['vat_cents']), ('Gutschrift gesamt' if row['kind'] == 'credit' else 'Rechnungsbetrag', row['gross_cents'])]
        else:
            amounts = [('Privat gezahlter Betrag', row['payment_cents'])]
        values = [[Paragraph(label, body), Paragraph(eur(value), right)] for label, value in amounts]
        table = Table(values, colWidths=[112 * mm, 53 * mm]); table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('LINEABOVE',(0,-1),(-1,-1),0.6,colors.HexColor('#737373')),('BACKGROUND',(0,-1),(-1,-1),colors.HexColor('#F0F1F2'))])); story += [Spacer(1, 3 * mm), table, Spacer(1, 6 * mm), Paragraph(escape(row['text']), body)]
        story += [Paragraph('Ablagevermerk Ottilie', heading), Paragraph(escape(row['note']), body), Paragraph(f"Interne Zuordnung: {row['id']}. Bezug: {row['target']}. Nachreichung am 28.09.2026 um 14:20 Uhr.", small)]
        def footer(canvas, document):
            canvas.saveState(); canvas.setFont('TNR', 9); canvas.setFillColor(colors.HexColor('#555555')); canvas.drawString(23 * mm, 17 * mm, f"Kostenablage Schnittflug · {row['id']}"); canvas.drawRightString(187 * mm, 17 * mm, str(document.page)); canvas.restoreState()
        doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=23 * mm, leftMargin=23 * mm, topMargin=18 * mm, bottomMargin=25 * mm, author='Ottilie Kühnle', title=row['title'], subject='Nachgereichte private Kosten- und Zahlungsunterlagen')
        doc.build(story, onFirstPage=footer, onLaterPages=footer)
        reader = PdfReader(output)
        assert len(reader.pages) == 1, (output.name, len(reader.pages))
        text = '\n'.join(p.extract_text() for p in reader.pages)
        assert row['id'] in text and row['target'] in text and row['recipient'] in text
        assert 'Diese Testakte wurde' not in text and 'This test case file' not in text
        (args.qa_dir / f'{output.stem}.txt').write_text(text)
        manifest.append({'file': output.name, 'pages': 1, 'sha256': hashlib.sha256(output.read_bytes()).hexdigest()})
    (args.qa_dir / 'pdf-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(manifest)} neue Einzelbelege erstellt und textlich geprüft.')


if __name__ == '__main__':
    main()
