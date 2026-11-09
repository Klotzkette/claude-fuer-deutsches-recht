#!/usr/bin/env python3
"""Erzeugt native Aktenstücke, Word-Vorlagen und getrennte Nachbesprechungen."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.utils import format_datetime
from html import escape
from io import BytesIO
import json
import mimetypes
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import LongTable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, TableStyle

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'projekteinkauf-baubranche'
PROJECT = 'Bildungscampus Leineaue · Hannover'
COMPANY = 'Limmerbogen Bau GmbH'
TEAL = '#173D42'
MUTED = '#4A6468'
PALE = '#EEF4F3'
FONT_NAMES = ('Times New Roman.ttf', 'Times New Roman Bold.ttf',
              'Times New Roman Italic.ttf', 'Times New Roman Bold Italic.ttf')


def cases():
    result = []
    for group in ('a', 'b', 'c'):
        source = ROOT / 'scripts/data' / f'{PLUGIN}-{group}.json'
        result.extend(json.loads(source.read_text(encoding='utf-8'))['cases'])
    if [case['id'] for case in result] != [f'PE-{n:02}' for n in range(1, 8)]:
        raise ValueError('Die Falldaten müssen PE-01 bis PE-07 genau einmal enthalten.')
    return result


def display_date(value):
    return datetime.fromisoformat(value).strftime('%d.%m.%Y')


def rows(table):
    header = table['headers']
    values = table['rows']
    if not header or any(len(row) != len(header) for row in values):
        raise ValueError(f'Uneinheitliche Tabellenbreite: {header}')
    return [header, *values]


def visible(value):
    if value is None:
        return ''
    return str(value).replace('.', ',') if isinstance(value, float) else str(value)


def sections(record):
    for index, section in enumerate(record['sections'], 1):
        yield index, re.sub(r'^\d+(?:\.\d+)*\s+', '', section['heading']), section


def set_fonts(font_dir):
    paths = [font_dir / name for name in FONT_NAMES]
    if not all(path.is_file() for path in paths):
        raise ValueError('Vier lizenzierte Times-New-Roman-TTFs erforderlich. PROJEKTEINKAUF_FONT_DIR setzen.')
    for name, path in zip(('PESerif', 'PESerifBold', 'PESerifItalic', 'PESerifBoldItalic'), paths):
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily('PESerif', normal='PESerif', bold='PESerifBold',
                                   italic='PESerifItalic', boldItalic='PESerifBoldItalic')
    return paths


def write_pdf(path, record, case):
    body = ParagraphStyle('Body', fontName='PESerif', fontSize=11, leading=14, spaceAfter=8)
    title = ParagraphStyle('Title', parent=body, fontName='PESerifBold', fontSize=20, leading=23, spaceAfter=10)
    meta = ParagraphStyle('Meta', parent=body, textColor=HexColor(MUTED), fontSize=9, leading=12)
    heading = ParagraphStyle('Heading', parent=body, fontName='PESerifBold', spaceBefore=9, spaceAfter=6, keepWithNext=True)
    cell = ParagraphStyle('Cell', parent=body, fontSize=9.5, leading=11.5, spaceAfter=0)
    head = ParagraphStyle('Table head', parent=cell, fontName='PESerifBold', textColor=white)
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=49, rightMargin=49,
                            topMargin=61, bottomMargin=48, title=record['title'], author=record['issuer'], invariant=1)
    flow = [Paragraph(escape(record['title']), title),
            Paragraph(escape(f"{case['id']} · {record['issuer']} · {display_date(record['date'])}"), meta)]
    for index, label, section in sections(record):
        if section.get('page_break_before'):
            flow.append(PageBreak())
        flow.append(Paragraph(escape(f'{index} {label}'), heading))
        for paragraph in section.get('paragraphs', []):
            flow.append(Paragraph(escape(paragraph), body))
        if 'table' in section:
            data = rows(section['table'])
            grid = [[Paragraph(escape(visible(v)), head if n == 0 else cell) for v in row]
                    for n, row in enumerate(data)]
            table = LongTable(grid, colWidths=[doc.width / len(data[0])] * len(data[0]), repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), HexColor(TEAL)),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor(PALE), white]),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
            ]))
            flow.extend((table, Spacer(1, 7)))

    def furniture(canvas, document):
        width, height = A4
        canvas.setFillColor(HexColor(TEAL))
        canvas.rect(0, height - 6, width, 6, stroke=0, fill=1)
        canvas.setFont('PESerifBold', 10)
        canvas.drawString(49, height - 33, record['issuer'])
        canvas.setFont('PESerif', 9)
        canvas.drawRightString(width - 49, height - 33, case.get('project', PROJECT))
        canvas.setStrokeColor(HexColor('#B9C9C8'))
        canvas.line(49, 40, width - 49, 40)
        canvas.drawString(49, 27, case['id'])
        canvas.drawRightString(width - 49, 27, f'Seite {document.page}')

    doc.build(flow, onFirstPage=furniture, onLaterPages=furniture)


def write_docx(path, record, case):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.05)
    sec.top_margin, sec.bottom_margin = Cm(2.35), Cm(1.95)
    for style_name, size in [('Normal', 11), ('Title', 20), ('Subtitle', 10), ('Heading 1', 12)]:
        style = doc.styles[style_name]
        style.font.name = 'Times New Roman'
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0, 0, 0)
        font = style.element.get_or_add_rPr().get_or_add_rFonts()
        for key in list(font.attrib):
            if key.lower().endswith('theme'):
                del font.attrib[key]
        for name in ('ascii', 'hAnsi', 'eastAsia', 'cs'):
            font.set(qn('w:' + name), 'Times New Roman')
        properties = style.element.get_or_add_pPr()
        border = properties.find(qn('w:pBdr'))
        if border is not None:
            properties.remove(border)
    doc.styles['Normal'].paragraph_format.space_after = Pt(7)
    doc.styles['Normal'].paragraph_format.line_spacing = 1.08
    doc.styles['Title'].font.bold = True
    doc.styles['Heading 1'].font.bold = True
    header = sec.header.paragraphs[0]
    header.style = doc.styles['Normal']
    run = header.add_run(record['issuer'] + '   ·   ' + case.get('project', PROJECT))
    run.bold = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor.from_string(TEAL[1:])
    footer = sec.footer.paragraphs[0]
    footer.style = doc.styles['Normal']
    footer.add_run(f"{case['id']}   ·   {display_date(record['date'])}   ·   Seite ").font.size = Pt(9)
    field = OxmlElement('w:fldSimple')
    field.set(qn('w:instr'), 'PAGE')
    footer._p.append(field)
    doc.add_paragraph(record['title'], 'Title')
    doc.add_paragraph(f"{case['id']} · {display_date(record['date'])}", 'Subtitle')
    for index, label, section in sections(record):
        heading = doc.add_heading(f'{index} {label}', 1)
        if section.get('page_break_before'):
            heading.paragraph_format.page_break_before = True
        for paragraph in section.get('paragraphs', []):
            doc.add_paragraph(paragraph)
        if 'table' in section:
            data = rows(section['table'])
            table = doc.add_table(rows=0, cols=len(data[0]))
            table.style = 'Table Grid'
            for n, row in enumerate(data):
                entry = table.add_row()
                props = entry._tr.get_or_add_trPr()
                props.append(OxmlElement('w:cantSplit'))
                if n == 0:
                    props.append(OxmlElement('w:tblHeader'))
                for item, value in zip(entry.cells, row):
                    item.text = visible(value)
                    if n == 0:
                        shading = OxmlElement('w:shd')
                        shading.set(qn('w:fill'), PALE[1:])
                        item._tc.get_or_add_tcPr().append(shading)
                        item.paragraphs[0].runs[0].bold = True
    doc.core_properties.title = record['title']
    doc.core_properties.author = record['issuer']
    doc.core_properties.created = doc.core_properties.modified = datetime(2026, 11, 9)
    buffer = BytesIO()
    doc.save(buffer)
    with ZipFile(buffer) as source, ZipFile(path, 'w') as out:
        for name in source.namelist():
            info = ZipInfo(name, (2026, 11, 9, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            out.writestr(info, source.read(name))


def write_png(path, record, fonts):
    regular, bold = (ImageFont.truetype(str(p), size) for p, size in zip(fonts, (26, 37)))
    small = ImageFont.truetype(str(fonts[0]), 22)
    width, padding = 1350, 62
    canvas = Image.new('RGB', (width, 2000), 'white')
    draw = ImageDraw.Draw(canvas)

    def text_lines(text, font, max_width):
        result = []
        line = ''
        for word in text.split():
            candidate = (line + ' ' + word).lstrip()
            if line and draw.textlength(candidate, font=font) > max_width:
                result.append(line)
                line = word
            else:
                line = candidate
        return [*result, line]

    draw.rectangle((0, 0, width, 100), fill=TEAL)
    draw.text((padding, 29), record['issuer'], font=bold, fill='white')
    y = 130
    for line in text_lines(record['title'], bold, width - 2 * padding):
        draw.text((padding, y), line, font=bold, fill=TEAL)
        y += 46
    draw.text((padding, y), f"Rekonstruierter Systemauszug · {display_date(record['date'])}", font=small, fill=MUTED)
    y += 46
    for paragraph in record.get('paragraphs', []):
        for line in text_lines(paragraph, regular, width - 2 * padding):
            draw.text((padding, y), line, font=regular, fill=TEAL)
            y += 32
        y += 12
    if 'table' in record:
        table = rows(record['table'])
        cell_width = (width - 2 * padding) / len(table[0])
        for n, row in enumerate(table):
            wrapped = [text_lines(visible(value), small, cell_width - 20) for value in row]
            height = 18 + 27 * max(map(len, wrapped))
            draw.rectangle((padding, y, width - padding, y + height),
                           fill=TEAL if n == 0 else (PALE if n % 2 else '#FFFFFF'))
            for i, lines in enumerate(wrapped):
                for k, line in enumerate(lines):
                    draw.text((padding + i * cell_width + 10, y + 8 + k * 27), line,
                              font=small, fill='white' if n == 0 else TEAL)
            y += height
    if y + 40 > canvas.height:
        raise ValueError('Systemauszug überschreitet seine Zeichenfläche: ' + path.name)
    canvas.crop((0, 0, width, y + 40)).save(path)


def message_id(case, filename):
    domain = case.get('message_domain', 'limmerbogen.example')
    return f"<{case['id'].lower()}.{Path(filename).stem.lower()}@{domain}>"


def write_eml(path, record, case, directory, documents):
    msg = EmailMessage(policy=policy.SMTP)
    for key in ('from_email', 'to_email'):
        if not re.fullmatch(r'[\w.+-]+@[\w.-]+\.example', record[key]):
            raise ValueError('Testmail benötigt reservierte Adresse: ' + record[key])
    msg['From'] = f"{record['from_name']} <{record['from_email']}>"
    msg['To'] = record['to_email']
    msg['Subject'] = record['subject']
    msg['Date'] = format_datetime(datetime.fromisoformat(record['date']))
    msg['Message-ID'] = message_id(case, record['filename'])
    if reply := record.get('reply_to'):
        if reply not in documents or Path(reply).suffix != '.eml':
            raise ValueError('Antwort verweist auf unbekannte Nachricht: ' + reply)
        msg['In-Reply-To'] = message_id(case, reply)
    attachments = record.get('attachments', [])
    body = '\n\n'.join(record['paragraphs']) + '\n'
    if attachments:
        body += '\nAnlagen dieser Nachricht\n' + '\n'.join(attachments) + '\n'
    msg.set_content(body, charset='utf-8', cte='quoted-printable')
    for filename in attachments:
        if filename not in documents or Path(filename).suffix == '.eml':
            raise ValueError('Anlage fehlt im Aktenverzeichnis: ' + filename)
        main, subtype = (mimetypes.guess_type(filename)[0] or 'application/octet-stream').split('/', 1)
        msg.add_attachment((directory / filename).read_bytes(), maintype=main, subtype=subtype, filename=filename)
    if attachments:
        msg.set_boundary(f"{case['id']}-{path.stem}-anlagen")
    path.write_bytes(msg.as_bytes())


def price_template(target):
    headers = ['Anbieter', 'LV-Position', 'Vergleichsmenge', 'Einheit', 'EP netto EUR',
               'Status', 'Positionswert netto EUR', 'Beleg und Annahme']
    count = 18
    return {
        'path': str(target), 'caseId': 'PE-01',
        'sheets': [{'name': 'Preisspiegel', 'title': 'Preisspiegel mit Beleg je Position',
                    'note': 'Tragen Sie Menge und Einzelpreis je Vergleichseinheit ein. Der Positionswert erscheint bei Status belegt.',
                    'headers': headers, 'rows': [[None] * len(headers) for _ in range(count)], 'textColumns': ['B'],
                    'formulas': {f'G{n}': f'=IF(AND(F{n}="belegt",H{n}<>"",COUNT(C{n},E{n})=2),ROUND(C{n}*E{n},2),"")'
                                 for n in range(4, count + 4)}}],
    }


def door_price_template(target, case):
    comparison = case['comparison']
    positions, costs, score = [], [], []
    line_formulas, cost_formulas, score_formulas = {}, {}, {}
    for row, offer in enumerate(comparison['offers'], 4):
        label = f"{offer['id']} {offer['name']}"
        first = len(positions) + 4
        for key, quantity in comparison['quantities'].items():
            positions.append([label, key, quantity, 'Stück', None, None, None, None])
        for key in ('Montage und Logistik', 'Übrige Ergänzungen', 'Unbedingter Preisabzug'):
            positions.append([label, key, 1, 'Pauschal', None, None, None, None])
        last = len(positions) + 3
        for n in range(first, last + 1):
            line_formulas[f'G{n}'] = f'=IF(AND(F{n}="belegt",H{n}<>"",COUNT(C{n},E{n})=2),ROUND(C{n}*E{n},2),"")'
        costs.append([label, None, None, None, None, None, None])
        cost_formulas[f'C{row}'] = f'=IF(COUNT(Positionen!G{first}:G{last})=8,SUM(Positionen!G{first}:G{last}),"")'
        cost_formulas[f'E{row}'] = f'=IF(COUNT(C{row}:D{row})=2,SUM(C{row}:D{row}),"")'
        cost_formulas[f'F{row}'] = f'=IF(AND(B{row}="geeignet",ISNUMBER(E{row}),E{row}>0),E{row},"")'
        score.append([label, None, None, None, None, None, None, None])
        score_formulas[f'B{row}'] = f'=IF(ISNUMBER(Kosten!F{row}),Kosten!F{row},"")'
        score_formulas[f'C{row}'] = f'=IF(ISNUMBER(B{row}),ROUND(45*MIN($B$4:$B$7)/B{row},2),"")'
        score_formulas[f'G{row}'] = (
            f'=IF(COUNT(C{row}:F{row})=4,IF(AND(MIN(D{row}:F{row})>=0,MAX(D{row}:F{row})<=5,'
            f'MOD(D{row},1)=0,MOD(E{row},1)=0,MOD(F{row},1)=0),'
            f'ROUND(C{row}+5*D{row}+4*E{row}+2*F{row},2),""),"")'
        )
    return {'path': str(target), 'caseId': case['id'], 'sheets': [
        {'name': 'Positionen', 'title': 'Vergleichspositionen für 500 Innentüren',
         'note': 'Erfassen Sie Netto-Einheitspreise mit Beleg und Status belegt. Bei enthaltenen Zusatzleistungen belegen Sie den Ansatz von null. Ein unbedingter Preisabzug ist negativ.',
         'headers': ['Anbieter', 'Position', 'Menge', 'Einheit', 'EP netto EUR', 'Stand', 'Wert netto EUR', 'Fundstelle'],
         'rows': positions, 'textColumns': ['B'], 'formulas': line_formulas},
        {'name': 'Kosten', 'title': 'Anschaffung und fünf Jahre Wartung',
         'note': 'Erfassen Sie die gleich abgegrenzte Wartung netto. Setzen Sie den Stand geeignet erst nach Prüfung aller Muss-Kriterien. Bedingte Preisvorteile bleiben in der Begründung getrennt.',
         'headers': ['Anbieter', 'Eignung', 'Auftrag netto EUR', 'Wartung 5 J. netto EUR', 'Vergleich netto EUR',
                     'Wertungsbasis netto EUR', 'Wartungsbeleg und offene Punkte'],
         'rows': costs, 'formulas': cost_formulas},
        {'name': 'Nutzwert', 'title': 'Preis Qualität Termin und Service',
         'note': 'Preispunkte folgen aus dem besten geeigneten Vergleichspreis. Geben Sie je 0 bis 5 Punkte nach Beleg ein. Gewichte gemäß Vorabvermerk sind 45, 25, 20 und 10.',
         'headers': ['Anbieter', 'Wertungsbasis EUR', 'Preis bis 45', 'Qualität 0–5', 'Termin 0–5',
                     'Service 0–5', 'Punkte bis 100', 'Begründung und Fundstellen'],
         'rows': score, 'formulas': score_formulas},
    ]}


def build(target, node, node_modules, fonts, previews, selected=None):
    font_paths = set_fonts(fonts)
    workbooks = []
    emails = []
    planned = cases()
    if selected:
        planned = [case for case in planned if case['id'] == selected]
        if not planned:
            raise ValueError('Unbekannte Fall-ID: ' + selected)
    for case in planned:
        if not re.fullmatch(r'projekteinkauf-[a-z0-9-]+', case['slug']):
            raise ValueError('Ungültiger Aktenname: ' + case['slug'])
        directory = target / 'testakten' / case['slug']
        directory.mkdir(parents=True, exist_ok=True)
        documents = {d['filename']: d for d in case['documents']}
        if len(documents) != len(case['documents']):
            raise ValueError('Doppelte Aktenstücknamen: ' + case['id'])
        for stage in case['stages']:
            if missing := set(stage['files']) - set(documents):
                raise ValueError(f"Unbekannte Unterlage in {case['id']}: {missing}")
        for filename, record in documents.items():
            if Path(filename).name != filename or not re.fullmatch(r'\d{2}[a-z]?_[A-Za-z0-9_.-]+', filename):
                raise ValueError('Ungültiger Aktenstückname: ' + filename)
            path = directory / filename
            match path.suffix:
                case '.pdf':
                    write_pdf(path, record, case)
                case '.docx':
                    write_docx(path, record, case)
                case '.png':
                    write_png(path, record, font_paths)
                case '.csv':
                    with path.open('w', newline='', encoding='utf-8') as stream:
                        csv.writer(stream, lineterminator='\n').writerows(rows(record))
                case '.xlsx':
                    for sheet in record['sheets']:
                        rows(sheet)
                    sheets = record['sheets']
                    if case.get('project'):
                        sheets = [{'note': case['project'] + ' · Einkauf', **sheet} for sheet in sheets]
                    workbooks.append({'path': str(path), 'caseId': case['id'], 'sheets': sheets})
                case '.eml':
                    emails.append((path, record, case, directory, documents))
                case _:
                    raise ValueError('Nicht unterstütztes Format: ' + filename)
        templates = target / PLUGIN / 'templates'
        templates.mkdir(parents=True, exist_ok=True)
        as_of = case.get('as_of', '2026-11-09')
        write_docx(templates / f"{case['slug']}.docx",
                   {**case['template'], 'issuer': case.get('company', COMPANY), 'date': as_of}, case)
        if 'comparison' in case:
            workbooks.append(door_price_template(templates / 'Brandschutztueren_Preisspiegel.xlsx', case))
        debrief = target / 'quality' / PLUGIN / 'nachbesprechung'
        debrief.mkdir(parents=True, exist_ok=True)
        write_pdf(debrief / f"{case['id']}_Nachbesprechung.pdf",
                  {**case['debrief'], 'issuer': 'Schulungsleitung · Projekteinkauf', 'date': as_of}, case)
    if not selected or selected == 'PE-01':
        workbooks.append(price_template(target / PLUGIN / 'templates/Preisspiegel.xlsx'))
    with tempfile.TemporaryDirectory(prefix='projekteinkauf-xlsx-') as directory:
        stage = Path(directory)
        (stage / 'node_modules').symlink_to(node_modules, target_is_directory=True)
        builder = stage / 'build.mjs'
        shutil.copyfile(ROOT / 'scripts/build-projekteinkauf-xlsx.mjs', builder)
        specs = stage / 'workbooks.json'
        specs.write_text(json.dumps(workbooks, ensure_ascii=False), encoding='utf-8')
        args = [str(node), str(builder), str(specs)]
        if previews:
            args.append(str(previews))
        subprocess.run(args, check=True)
    for args in emails:
        write_eml(*args)
    print(f'{len(planned)} Akten, {len(workbooks)} Arbeitsmappen, {len(emails)} E-Mails.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-root', type=Path, default=ROOT)
    parser.add_argument('--node', type=Path, required=True)
    parser.add_argument('--node-modules', type=Path, required=True)
    parser.add_argument('--font-dir', type=Path, default=Path(os.environ.get(
        'PROJEKTEINKAUF_FONT_DIR', '/System/Library/Fonts/Supplemental')))
    parser.add_argument('--xlsx-previews', type=Path)
    parser.add_argument('--case', help='Nur die angegebene Fall-ID bauen, zum Beispiel PE-07.')
    args = parser.parse_args()
    build(args.output_root.resolve(), args.node.resolve(), args.node_modules.resolve(),
          args.font_dir.resolve(), args.xlsx_previews.resolve() if args.xlsx_previews else None, args.case)
