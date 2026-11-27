#!/usr/bin/env python3
"""Gestaltet die 28 ModeFuchs-Belege aus ihren byteversiegelten Quell-PDFs."""

import argparse
import hashlib
import json
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ContentStream, FloatObject
from reportlab.pdfgen.canvas import Canvas

from modefuchs_briefpapier import draw_letterhead

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / 'scripts/fixtures/modefuchs'
ORIGINALE = ROOT / 'testakten/inkasso-zahlungsklage-modefuchs/originale'

# Jeder alte ReportLab-Kopf ist ein abgeschlossener Block oberhalb des Rumpfs.
# Zahl der Originalzeilen und unterer Rand inklusive der alten Trennlinie (pt).
KOPF = {
    'ModeFuchs GmbH': ('modefuchs', 5, 693),
    'InkassoZentrale GmbH': ('inkasso', 5, 693),
    'Kanzlei Brezelmann & Collegen': ('kanzlei', 5, 693),
    'Musterbank Nürnberg': ('bank', 2, 725),
    'E-Mail-Ausdruck': ('mail', 1, 735),
    'Akte ModeFuchs GmbH ./. Gottlieb von Altenhausen': ('register', 2, 718),
}


def remove_letterhead(page, writer, lower_edge, expected_body):
    """Entfernt die gesetzten Kopfobjekte samt Linie auf der ersten Seite."""
    # Die Textoperanden sind Fontcodes, keine Unicode-Zeichenketten. Ihre
    # Originalbytes erhalten insbesondere den Euro sowie die eingebetteten Fonts.
    content = ContentStream(page.get_contents(), writer, forced_encoding='bytes')
    ops = content.operations
    depth = 0
    first = None
    for index, (_, operator) in enumerate(ops):
        if operator == b'q':
            if depth == 0:
                matrix, move = ops[index + 1]
                if move != b'cm':
                    raise ValueError('Unbekannter Koordinatenursprung im Quellkopf')
                if float(matrix[5]) < lower_edge:
                    break
                if first is None:
                    first = index
            depth += 1
        elif operator == b'Q':
            depth -= 1
    else:
        raise ValueError('Beginn des Belegtexts fehlt')
    if first is None:
        raise ValueError('Erwarteter Quellkopf fehlt')

    content.operations = ops[:first] + ops[index:]
    page.replace_contents(content)
    if ''.join(page.extract_text().split()) != ''.join(expected_body.split()):
        raise ValueError('Beim Abtrennen des Briefkopfs wurde der Belegtext verändert')


def document_kind(sender, number):
    if sender in ('mail', 'bank', 'register'):
        return {'mail': 'email', 'bank': 'kontoauszug', 'register': 'register'}[sender]
    if 13 <= number <= 17:
        return 'intern'
    if 21 <= number <= 24:
        return 'prozess'
    return 'brief'


def style_table(page, writer, number):
    """Lesbare Spaltenköpfe, mit unveränderten Schriftcodes und Zellwerten."""
    content = ContentStream(page.get_contents(), writer, forced_encoding='bytes')
    ops = content.operations
    heading = (0.86, 0.91, 0.89) if number == 19 else (0.94, 0.88, 0.82)
    for i, (color, operator) in enumerate(ops):
        if (operator == b'rg' and tuple(color) == (0.176471,) * 3
                and [op for _, op in ops[i + 1:i + 4]] == [b'n', b're', b'f*']):
            ops[i] = ([FloatObject(v) for v in heading], b'rg')
            break
    else:
        raise ValueError(f'Tabellenkopf im Beleg {number} nicht gefunden')

    if number in (1, 4):
        # Freie Fläche der Summenzeile im ursprünglichen Tabellenkoordinatensystem.
        x, width, height = (250, 150, 34) if number == 1 else (265, 160, 22)
        ops[i + 4:i + 4] = [
            ([], b'q'), ([FloatObject(v) for v in (0.98, 0.95, 0.91)], b'rg'),
            ([], b'n'), ([FloatObject(v) for v in (x, 0, width, height)], b're'),
            ([], b'f*'), ([], b'Q'),
        ]
        # In den beiden schmalen Zellen steht nur der Punkt bzw. das Wortende
        # auf der zweiten Zeile. Beide Fragmente passen auf die normale Grundlinie.
        for j, (text, op) in enumerate(ops[:-2]):
            if (op == b'Tj' and text in ([b'Pos'], [b'Gesamtbetra'])
                    and ops[j + 1][1] == b'T*' and ops[j + 2][1] == b'Tj'
                    and ops[j + 2][0] in ([b'.'], [b'g:'])):
                ops[j], ops[j + 1] = ops[j + 1], ops[j]
    content.operations = ops
    page.replace_contents(content)


def render(source, digest):
    reader = PdfReader(source)
    original_lines = reader.pages[0].extract_text().splitlines()
    sender, count, edge = KOPF[original_lines[0]]
    header = tuple(original_lines[:count])
    # Die FAO kennt keinen Fachanwalt für Zivilrecht. Im gestalteten Briefkopf
    # ist Zivilrecht das Tätigkeitsgebiet. Die gehashte Quelle bleibt unverändert.
    if sender == 'kanzlei' and header[1] == 'Rechtsanwälte · Fachanwalt für Zivilrecht':
        header = (header[0], 'Rechtsanwälte · Zivilrecht', *header[2:])
    document_number = int(source.name[:2])
    kind = document_kind(sender, document_number)
    writer = PdfWriter()
    for number, original in enumerate(reader.pages, start=1):
        page = writer.add_page(original)
        if number == 1:
            remove_letterhead(page, writer, edge, '\n'.join(original_lines[count:]))
            if document_number in (1, 4, 19):
                style_table(page, writer, document_number)
        size = float(page.mediabox.width), float(page.mediabox.height)
        overlay = BytesIO()
        canvas = Canvas(overlay, pagesize=size, invariant=1)
        draw_letterhead(canvas, sender=sender, page_number=number, page_count=len(reader.pages),
                        page_size=size, document_kind=kind, header_lines=header if number == 1 else ())
        canvas.showPage()
        canvas.save()
        page.merge_page(PdfReader(overlay).pages[0], over=False)
        page.compress_content_streams()

    writer.add_metadata({'/Title': source.stem, '/SourceFile': source.name, '/SourceSHA256': digest})
    out = BytesIO()
    writer.write(out)
    return out.getvalue()


def build_originals(*, check=False):
    manifest = json.loads((FIXTURE / 'originale-sha256.json').read_text(encoding='utf-8'))
    sources = sorted((FIXTURE / 'quellbelege').glob('*.pdf'))
    if {p.name for p in sources} != set(manifest):
        raise ValueError('Der Bestand an Quellbelegen weicht vom SHA-256-Verzeichnis ab')
    generated = {}
    for path in sources:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != manifest[path.name]:
            raise ValueError(f'Veränderter Quellbeleg: {path.name}')
        generated[ORIGINALE / path.name] = render(path, digest)
    if check:
        changed = [p.name for p, data in generated.items() if not p.is_file() or p.read_bytes() != data]
        if changed:
            raise ValueError('Abweichende Ausgabe: ' + ', '.join(changed))
    else:
        ORIGINALE.mkdir(parents=True, exist_ok=True)
        for destination, data in generated.items():
            destination.write_bytes(data)


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--check', action='store_true', help='Ausgaben byteweise prüfen, ohne zu schreiben')
    build_originals(check=cli.parse_args().check)
