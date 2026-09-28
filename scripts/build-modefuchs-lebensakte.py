#!/usr/bin/env python3
"""Ergänzt den ModeFuchs-Eingang um native Nachrichten und ihre Originalanhänge."""

from email import policy
from email.message import EmailMessage
from pathlib import Path
import json
import mimetypes
import subprocess
import tempfile

from pypdf import PdfReader
from reportlab.pdfgen.canvas import Canvas

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
            subprocess.run(['pdftoppm', '-r', '140', '-png', str(source), str(prefix)],
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
    build_scans()
    records = json.loads(SOURCE.read_text(encoding='utf-8'))
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
        message.set_content(message_body(row, records), charset='utf-8', cte='quoted-printable')
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
