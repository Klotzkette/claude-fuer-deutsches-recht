#!/usr/bin/env python3
"""Ergänzt den ModeFuchs-Eingang um native Nachrichten und ihre Originalanhänge."""

from email import policy
from email.message import EmailMessage
from html import escape
from io import BytesIO
from pathlib import Path
import json
import mimetypes
import subprocess
import tempfile

from pypdf import PdfReader
from reportlab.pdfgen.canvas import Canvas

from modefuchs_belege import build_originals

from modefuchs_briefpapier import draw_signet

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'testakten/inkasso-zahlungsklage-modefuchs'
SOURCE = ROOT / 'scripts/fixtures/modefuchs/korrespondenz.json'


def message_body(row, records):
    body = row['body']
    if row.get('quote_message'):
        original = next(item for item in records if item['id'] == row['quote_message'])
        body += ('\n-----Ursprüngliche Nachricht-----\n'
                 f"Von: {original['from']}\nAn: {original['to']}\n"
                 f"Datum: {original['date']}\nBetreff: {original['subject']}\n\n"
                 + original['body'])
    return body


def shop_signet_png():
    stream = BytesIO()
    sheet = Canvas(stream, pagesize=(44, 42), invariant=1)
    draw_signet(sheet, sender='modefuchs', x=0, y=0, scale=1)
    sheet.showPage()
    sheet.save()
    return subprocess.run(
        ['pdftocairo', '-singlefile', '-png', '-transp', '-r', '288', '-', '-'],
        input=stream.getvalue(), capture_output=True, check=True, timeout=30,
    ).stdout


def add_shop_mail_html(message, row, body, signet):
    # Der Shopmailer verschickt dieselbe Nachricht als Klartext und als Geschäfts-E-Mail.
    paragraphs = ''.join('<p>' + escape(part).replace('\n', '<br>') + '</p>'
                         for part in body.strip().split('\n\n'))
    mark_id = 'signet.' + row['id'].strip('<>')
    html = f'''<!doctype html>
<html lang="de"><body style="margin:0;padding:24px 12px;color:#352826;background:#f5f1eb">
<div style="max-width:620px;margin:0 auto;padding:24px 28px;background:#fff;font:16px/1.55 Arial,sans-serif">
<div style="padding:8px 0 18px;border-bottom:2px solid #aa6849">
<img src="cid:{mark_id}" width="44" height="42" alt="" style="vertical-align:middle">
<span style="vertical-align:middle;font:30px Georgia,serif">ModeFuchs</span></div>
<h1 style="margin:24px 0 20px;font:25px/1.25 Georgia,serif">{escape(row['subject'])}</h1>
{paragraphs}</div></body></html>'''
    message.add_alternative(html, subtype='html', charset='utf-8', cte='quoted-printable')
    boundary = '=_modefuchs_' + Path(row['file']).stem
    message.set_boundary(boundary + '_alt')
    related = message.get_payload()[-1]
    related.add_related(signet, maintype='image', subtype='png',
                        cid=f'<{mark_id}>', disposition='inline')
    related.set_boundary(boundary + '_bild')


def build_scans():
    originals = {
        'Scan_20250610_113247.pdf': '07_Erste_Mahnung_Post_05-05-2025.pdf',
        'Scan007.pdf': '08_Zweite_Mahnung_Post_22-05-2025.pdf',
        'Dokument1.pdf': '09_Abtretungserklaerung_08-06-2025.pdf',
    }
    for name, original in originals.items():
        source = CASE / 'originale' / original
        with tempfile.TemporaryDirectory(prefix='modefuchs-scan-') as temporary:
            prefix = Path(temporary) / 'blatt'
            subprocess.run(['pdftocairo', '-r', '160', '-png', str(source), str(prefix)],
                           check=True, capture_output=True, timeout=90)
            images = sorted(Path(temporary).glob('blatt-*.png'))
            pages = PdfReader(source).pages
            if len(images) != len(pages):
                raise ValueError(f'Unvollständiger Scan: {original}')
            pdf = Canvas(str(CASE / name), invariant=1)
            pdf.setAuthor('Klotzkette')
            pdf.setTitle(source.stem)
            for image, page in zip(images, pages):
                width, height = float(page.mediabox.width), float(page.mediabox.height)
                pdf.setPageSize((width, height))
                pdf.drawImage(str(image), 0, 0, width=width, height=height)
                pdf.showPage()
            pdf.save()


def build():
    build_originals()
    build_scans()
    records = json.loads(SOURCE.read_text(encoding='utf-8'))
    signet = shop_signet_png()
    for row in records:
        message = EmailMessage(policy=policy.SMTP)
        for header, key in (('From', 'from'), ('To', 'to'), ('Date', 'date'),
                            ('Subject', 'subject'), ('Message-ID', 'id')):
            message[header] = row[key]
        if row.get('cc'):
            message['Cc'] = row['cc']
        if row.get('reply_to'):
            message['In-Reply-To'] = row['reply_to']
            message['References'] = row['reply_to']
        message['X-Mailer'] = row.get('mailer', 'Desktop Mail 7.4')
        body = message_body(row, records)
        message.set_content(body, charset='utf-8', cte='quoted-printable')
        if row.get('mailer') == 'ShopMailer 7.4':
            add_shop_mail_html(message, row, body, signet)
        attachments = row.get('attachments', [])
        attachment_names = row.get('attachment_names', {})
        if attachments:
            message['X-Attachments'] = '; '.join(attachment_names.get(name, Path(name).name) for name in attachments)
        for name in attachments:
            path = CASE / name
            if not path.is_file() or not path.resolve().is_relative_to(CASE.resolve()):
                raise ValueError(f'Anhang fehlt oder liegt außerhalb der Akte: {name}')
            maintype, subtype = (mimetypes.guess_type(path.name)[0] or 'application/octet-stream').split('/', 1)
            message.add_attachment(path.read_bytes(), maintype=maintype, subtype=subtype,
                                   filename=attachment_names.get(name, path.name))
        if attachments:
            message.set_boundary('=_modefuchs_' + Path(row['file']).stem)
        destination = CASE / row['file']
        if destination.parent != CASE or destination.suffix != '.eml':
            raise ValueError(f'Ungültiger Nachrichtenname: {destination}')
        destination.write_bytes(message.as_bytes())
    print(f'{len(records)} Nachrichten mit vollständigen Headern und Originalanhängen geschrieben.')


if __name__ == '__main__':
    build()
