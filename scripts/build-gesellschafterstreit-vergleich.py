#!/usr/bin/env python3
"""Erweitert den Berliner Fall um vollständige Klageanlage und Vergleichsunterlagen.

Die bisherigen Belege bleiben bis auf den korrigierten K7-Exporttag erhalten.
DOCX werden mit dem angegebenen Dokumentenrenderer gesetzt; keine System-
LibreOffice-Installation wird als stiller Ersatz gewählt.
"""
from pathlib import Path
import argparse
from concurrent.futures import ThreadPoolExecutor
import importlib.util
import io
import json
import os
import re
import subprocess
import sys

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from vorfuehrakte_gesellschafter_berlin import CASE as CORE
from gesellschafterstreit_vergleich_daten import CASE
from akten_build_runtime import serif_font_path
from testakte_disclaimer import NOTICE_MARKDOWN

ROOT = Path(__file__).resolve().parents[1]
SUBDIR = 'Vergleich_2026-10-09'
CLAIM_PACKET = 'V00_Klage_mit_Anlagen_K1_bis_K9.pdf'
ANNEXES = {
    'K1': '05_Gesellschaftsvertrag_K1.docx',
    'K2': '06a_Gesellschafterliste_K2.docx',
    'K3': '06b_Registerabruf_K3.pdf',
    'K4': '07_Einladung_K4.docx',
    'K5': '08_Niederschrift_K5.docx',
    'K6': '10_Rechnung_SBS_K6.pdf',
    'K7': '11_Nachrichten_K7.txt',
    'K8': '12_Beanstandung_K8.docx',
    'K9': '13_Antwort_Seidel_K9.docx',
}


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('-', '_'), ROOT / 'scripts' / filename)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def claim_packet(directory, rendered_claim):
    from testakte_office_pdf import render_office_batch
    renderer = module('build-testakten-einzelpdf-zips.py')
    sources = [directory / name for name in ANNEXES.values()]
    cache = render_office_batch([p for p in sources if p.suffix == '.docx'])
    result = PdfWriter()
    result.append(PdfReader(rendered_claim), outline_item='Klageschrift vom 22.09.2026')
    pdfmetrics.registerFont(TTFont('AnlagenSerif', str(serif_font_path())))
    for mark, filename in ANNEXES.items():
        path = directory / filename
        data = renderer.render_document_pdf(path, directory, cache)
        if not data:
            raise RuntimeError('Anlage nicht gerendert: ' + filename)
        reader = PdfReader(io.BytesIO(data))
        start = len(result.pages)
        for number, page in enumerate(reader.pages, 1):
            overlay = io.BytesIO()
            width, height = float(page.mediabox.width), float(page.mediabox.height)
            canvas = Canvas(overlay, pagesize=(width, height), invariant=1)
            canvas.setFont('AnlagenSerif', 11)
            canvas.drawString(48, height - 19, f'Anlage {mark} | Seite {number} von {len(reader.pages)}')
            canvas.save()
            page.merge_page(PdfReader(io.BytesIO(overlay.getvalue())).pages[0])
            result.add_page(page)
        result.add_outline_item(f'Anlage {mark} - {filename}', start)
    result.add_metadata({'/Title': 'Klage Seidel gegen Spreebogen Lichtwerk mit Anlagen K1 bis K9',
                         '/CreationDate': 'D:20261009120000Z', '/ModDate': 'D:20261009120000Z'})
    result.write(directory / SUBDIR / CLAIM_PACKET)


def readme(directory):
    rows = [(CLAIM_PACKET, 'Vollständige ausgefüllte Klage mit den tatsächlichen Anlagen K1 bis K9 und PDF-Lesezeichen')]
    for item in CASE['docs']:
        rows += [(item['file'], item['title']), (str(Path(item['file']).with_suffix('.pdf')), item['title'] + ' als PDF')]
    rows += [(item['file'], item['title']) for item in CASE['emails']]
    lines = ['# 1 Klage und anschließende Vergleichsverhandlung', '',
             '## 1.1 Arbeitsstand und Einstieg', '',
             'Dieser Teil führt den Berliner Fall am 9. Oktober 2026 fort. Die Klage vom 22. September ist vollständig ausgefüllt und enthält eine ausführliche rechtliche Begründung. V00 verbindet sie mit allen neun tatsächlichen Anlagen; die bearbeitbare Klage bleibt im Kernbestand unter 02_Klage_Seidel.docx.', '',
             CASE['entry'], '',
             '## 1.2 Zwei aufeinanderfolgende Aufgaben', '',
             'Erarbeiten Sie zunächst für die Gesellschaft eine Klageerwiderung aus Klage, Anlagen und dem Nachtrag vom 8. Oktober. Vergleichen Sie Parteibehauptungen mit den vollständigen Nachrichten, der Stimmzählung und den nachgereichten Lieferbelegen. Eine fertige Klageerwiderung ist nicht Bestandteil der Arbeitsakte.', '',
             'Bearbeiten Sie anschließend V01 als Entwurf einer Gesellschaftervereinbarung. Die Briefe, E-Mails und Gesprächsnotizen enthalten die inhaltlichen Wünsche zu jeder Klausel, mit noch offenen Alternativen und unterschiedlichen Grenzen der Beteiligten. Erst die Bearbeitung soll daraus eine abgestimmte Fassung, nötige Beschlüsse und die Voraussetzungen einer Prozessbeendigung entwickeln. Es liegt noch kein geschlossener Vergleich vor.', '',
             'Die Vergleichsgespräche ersetzen keine fristwahrende Prozesshandlung. Maßgeblich bleiben die gerichtlichen Unterlagen und der belegte Übermittlungsstand. Das ursprüngliche Mandat gilt der Gesellschaft; persönliche Interessen und Vertretungsbefugnisse der Beteiligten sind gesondert zu behandeln.', '',
             '## 1.3 Dateien', '', NOTICE_MARKDOWN, '', '| Datei | Inhalt |', '| --- | --- |']
    lines += [f'| [{name}]({name}) | {title} |' for name, title in rows]
    lines += ['', 'V00 ist eine Zusammenstellung der bereits einzeln vorhandenen Klage und K-Anlagen, kein zusätzlicher unabhängiger Beleg. DOCX und zugehörige PDF-Lesefassung sowie E-Mail-Anhänge enthalten denselben Text in unterschiedlichen Formaten. Der chronologisch spätere Vergleichsbestand gehört nicht zu den Klageanlagen vom September.', '',
              'Alle Personen, Kontakte und Vorgänge sind erfunden; `.example`-Adressen sind nicht erreichbar. Keine amtlichen Ausfertigungen und keine echten Unterschriften.', '',
              '[Zur Fallübersicht und den Gesamtdownloads](../README.md)', '']
    (directory / SUBDIR / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    parent = directory / 'README.md'
    text = parent.read_text(encoding='utf-8')
    start, end = '<!-- BEGIN gesellschafterstreit-vergleich -->', '<!-- END gesellschafterstreit-vergleich -->'
    section = '\n'.join([start, '## 1.6 Ausführliche Klage und Vergleichsverhandlung vom 9 Oktober 2026', '',
        'Die vollständig ausgefüllte Klage ist ausgebaut. Ein eigenes PDF verbindet sie mit den tatsächlichen Anlagen K1 bis K9. Fünf neue Word-Dokumente mit PDF-Lesefassungen und sechs E-Mails mit echten Anhängen führen vom Streit zur möglichen neuen Gesellschaftervereinbarung: Wünsche der drei Beteiligten, Gegenpositionen, Gesprächsprotokoll und bearbeitbarer Vertragsentwurf.', '',
        f'[Klagepaket, Vergleichskorrespondenz und Vertragsentwurf]({SUBDIR}/README.md)', '',
        'Die Klageerwiderung bleibt die erste KI-Aufgabe; danach kann der Vereinbarungsentwurf anhand des Schriftverkehrs überarbeitet werden. Die Verhandlung ist offen, der Vergleich nicht geschlossen. Die ausführliche Bearbeitung beider Schritte kann über den ursprünglichen 30-Minuten-Einstieg hinausgehen.', '', end])
    if start in text:
        text = re.sub(re.escape(start) + r'.*?' + re.escape(end), lambda _: section, text, flags=re.S)
    else:
        text = text.rstrip() + '\n\n' + section + '\n'
    parent.write_text(text, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--qa-dir', type=Path, required=True)
    parser.add_argument('--renderer', type=Path, required=True)
    args = parser.parse_args()
    args.qa_dir.mkdir(parents=True, exist_ok=True)
    if not args.renderer.is_file():
        raise ValueError('Dokumentenrenderer fehlt')
    directory = ROOT / 'testakten' / CORE['slug']
    target = directory / SUBDIR
    target.mkdir(exist_ok=True)
    native = module('build-gesellschafterstreit-nachtrag.py')
    original = module('build-gesellschafter-vorfuehrakten.py')
    helper = module('render-startup-gruender-werkstatt.py')
    runtime = Path(sys.executable).resolve().parents[3]
    env = helper.renderer_environment(args.qa_dir, runtime)
    os.environ.update(env)
    claim = next(item for item in CORE['documents'] if item['file'] == '02_Klage_Seidel.docx')
    # Vorführbuilder liefert identische Styles; nur das beauftragte Dokument ändern.
    original.builder.word(claim, directory / claim['file'])
    from docx import Document
    from docx.shared import Pt
    word = Document(directory / claim['file'])
    word.styles['Heading 1'].paragraph_format.space_before = Pt(9)
    word.styles['Heading 1'].paragraph_format.space_after = Pt(5)
    original.builder.native.stable_docx(word, directory / claim['file'])
    item = next(item for item in CORE['documents'] if item['file'] == '11_Nachrichten_K7.txt')
    (directory / item['file']).write_text(item['title'] + '\n' + item['date'] + '\n\n' + item['body'] + '\n', encoding='utf-8')
    for item in CASE['docs']:
        native.word(item, target / item['file'])
        doc = Document(target / item['file'])
        for section in doc.sections:
            for paragraph in section.footer.paragraphs:
                for run in paragraph.runs:
                    if run.text == 'Seite ':
                        run.text = ''
        original.builder.native.stable_docx(doc, target / item['file'])
    def render(job):
        item, path = job
        dest = args.qa_dir / 'word' / path.stem
        dest.mkdir(parents=True, exist_ok=True)
        proc = subprocess.run([sys.executable, str(args.renderer), str(path), '--output_dir', str(dest), '--emit_pdf', '--dpi', '120'],
                              env=env, capture_output=True, text=True, timeout=300)
        (dest / 'render.log').write_text(proc.stdout + proc.stderr)
        pdf = dest / (path.stem + '.pdf')
        images = sorted(dest.glob('page-*.png'))
        if proc.returncode or not pdf.is_file() or not images:
            raise RuntimeError(path.name + ': ' + proc.stderr[-1200:])
        if path.parent == target:
            from testakte_office_pdf import normalize_pdf
            path.with_suffix('.pdf').write_bytes(normalize_pdf(pdf.read_bytes(), item['title']))
        return {'file': str(path.relative_to(ROOT)), 'pdf': str(pdf), 'pages': len(images), 'images': [str(p) for p in images]}
    jobs = [(claim, directory / claim['file'])] + [(item, target / item['file']) for item in CASE['docs']]
    with ThreadPoolExecutor(max_workers=2) as pool:
        manifest = list(pool.map(render, jobs))
    for item in CASE['emails']:
        native.message(item, target)
    # Die Mandatsmail enthält die neue Klage tatsächlich als bytegleichen Anhang.
    item = next(item for item in CORE['documents'] if item['file'] == '01_Mandat_Rabenstein.eml')
    original.builder.mail(item, directory / item['file'], CORE['attachments'][item['file']])
    claim_packet(directory, Path(manifest[0]['pdf']))
    readme(directory)
    (args.qa_dir / 'word-render.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'documents': len(jobs), 'word_pages': sum(x['pages'] for x in manifest), 'case': CORE['slug']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
