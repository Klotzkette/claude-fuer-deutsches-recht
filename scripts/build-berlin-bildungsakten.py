#!/usr/bin/env python3
"""Baut ausschließlich die sechs nativen Berliner Bildungsakten.

Aufruf mit gebündeltem Python: --qa-dir /tmp/berlin-bildungsakten-qa.
AKTEN_NODE und AKTEN_NODE_MODULES wählen die gebündelte Tabellenlaufzeit.
--render-docx benötigt den Dokument-Skill-Renderer und prüft alle Word-Seiten.
Gesamt-PDFs und Archive entstehen danach mit den zentralen Repo-Buildern.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import format_datetime
import importlib.util
import json
import mimetypes
import os
from pathlib import Path
import re
import subprocess
import sys

from docx import Document
from docx.oxml.ns import qn

from berlin_bildungsakten_daten import CASES
from akten_build_runtime import node_binary
from testakte_disclaimer import NOTICE_MARKDOWN

ROOT = Path(__file__).resolve().parents[1]


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


native = module('berlin_native', 'build-registerwerkstaetten-akten.py')
render_helpers = module('berlin_render_helpers', 'render-startup-gruender-werkstatt.py')


def word(item, target):
    native.word(item, target)
    doc = Document(target)
    # Die mitgelieferte Word-Standardvorlage kann Theme-Schriften und eine
    # Titellinie mitbringen. Der Repo-Standard ist durchgehend Times 11.
    for root in (doc.styles.element, doc.element):
        for border in list(root.iter(qn('w:pBdr'))):
            border.getparent().remove(border)
        for fonts in root.iter(qn('w:rFonts')):
            for key in list(fonts.attrib):
                if 'theme' in key.lower():
                    del fonts.attrib[key]
            fonts.set(qn('w:ascii'), 'Times New Roman')
            fonts.set(qn('w:hAnsi'), 'Times New Roman')
    native.stable_docx(doc, target)

# Tatsächlich mitversandte Belege; keine nur behaupteten MIME-Anlagen.
ATTACHMENTS = {
    'berlin-kita-sonnenkringel': {
        '10_Rueckmeldung_Platzangebot.eml': ['05_Arbeitgeber_Mara.docx', '06_Wochenplan_September.xlsx'],
    },
    'berlin-schulplatz-siebte-klasse': {
        '06_Nachreichung_am_14_Maerz.eml': ['05_Meldebescheinigung_Haushalt.docx'],
        '15_Eltern_Nachricht_weitergeleitet.eml': ['05_Meldebescheinigung_Haushalt.docx'],
    },
    'berlin-schule-klassenchat': {
        '07_Eltern_bitten_Terminwechsel.eml': ['02_Klassenchat_Export.txt', '10_Emils_Erklaerung.docx'],
        '18_Eltern_Nachtrag.eml': ['17_Lehrerin_Kontext.eml'],
    },
    'berlin-professur-forschungslabor': {
        '05_Uebersendung_Raumbedarf.eml': ['04_Projektbeschreibung_Raum.docx'],
    },
}


def mail(item, target, attachments):
    msg = EmailMessage(policy=SMTP)
    msg['From'], msg['To'], msg['Subject'] = item['from'], item['to'], item['title']
    msg['Date'] = format_datetime(datetime.fromisoformat(item['date']))
    msg['Message-ID'] = '<' + target.stem + '.' + target.parent.name + '@akten.example>'
    msg.set_content(item['body'], charset='utf-8')
    for name in attachments:
        source = target.parent / name
        mime = mimetypes.guess_type(name)[0] or 'application/octet-stream'
        major, minor = mime.split('/', 1)
        if major == 'message':
            # Unveränderte Originalnachricht als allgemein lesbare Datei.
            major, minor = 'application', 'octet-stream'
        msg.add_attachment(source.read_bytes(), maintype=major, subtype=minor, filename=name)
    if msg.is_multipart():
        msg.set_boundary('berlin-' + target.parent.name + '-' + target.stem)
    target.write_bytes(msg.as_bytes())


def readme(case, directory):
    native.readme(case, directory)
    target = directory / 'README.md'
    text = target.read_text()
    text = text.replace('Alle Personen und Unternehmen in dieser Akte sind fiktiv.',
                        'Alle Personen, Unternehmen, Schulen und die Universität an der Spree Berlin in dieser Akte sind fiktiv. Reale Berliner Behördennamen dienen nur der Orts- und Verfahrenseinordnung; die Schreiben, Aktenzeichen und Kontakte sind erfunden. Die Universität ist als staatliche Berliner Universität angelegt.')
    text += '\n## 1.4. Downloads\n\n' + NOTICE_MARKDOWN + '\n\n'
    slug = case['slug']
    text += '| Gesamt-PDF | Akten-ZIP | Einzel-PDF-ZIP |\n| --- | --- | --- |\n'
    text += f'| [{case["title"]}](gesamt-pdf/{slug}_gesamt.pdf) | [Originaldateien](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/{slug}.zip) | [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/{slug}-einzelpdf.zip) |\n'
    target.write_text(text, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--qa-dir', type=Path, required=True)
    parser.add_argument('--render-docx', type=Path)
    parser.add_argument('--only', nargs='*')
    args = parser.parse_args()
    args.qa_dir.mkdir(parents=True, exist_ok=True)
    cases = [c for c in CASES if not args.only or c['slug'] in args.only]
    if args.only and set(args.only) - {c['slug'] for c in cases}:
        raise ValueError('Unbekannte Akte')
    spreadsheets = []
    docxs = []
    for case in cases:
        directory = ROOT / 'testakten' / case['slug']
        directory.mkdir(parents=True, exist_ok=True)
        names = [d['file'] for d in case['documents']]
        if len(names) != len(set(names)) or any(Path(n).name != n for n in names):
            raise ValueError('Ungültige Dateinamen')
        for item in case['documents']:
            target = directory / item['file']
            if target.suffix == '.docx':
                word(item, target)
                docxs.append(target)
            elif target.suffix == '.xlsx':
                spreadsheets.append({**item, 'case': case['slug'], 'output': str(target)})
            elif target.suffix == '.txt':
                target.write_text(item['title'] + '\n' + item['date'] + '\n\n' + item['body'] + '\n', encoding='utf-8')
            elif target.suffix != '.eml':
                raise ValueError('Unbekanntes Format: ' + target.suffix)
        readme(case, directory)
    spec_path = args.qa_dir / 'tabellen-spezifikation.json'
    spec_path.write_text(json.dumps(spreadsheets, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    subprocess.run([node_binary(), str(ROOT / 'scripts/build-berlin-bildungsakten-tabellen.mjs'), str(spec_path), str(args.qa_dir / 'tabellen')], check=True)
    for case in cases:
        directory = ROOT / 'testakten' / case['slug']
        for item in case['documents']:
            if item['file'].endswith('.eml'):
                mail(item, directory / item['file'], ATTACHMENTS.get(case['slug'], {}).get(item['file'], []))
        print(case['slug'], len(case['documents']), flush=True)
    if args.render_docx:
        runtime = Path(sys.executable).resolve().parents[3]
        env = render_helpers.renderer_environment(args.qa_dir, runtime)
        def render(path):
            target = args.qa_dir / 'word' / path.parent.name / path.stem
            target.mkdir(parents=True, exist_ok=True)
            result = subprocess.run([sys.executable, str(args.render_docx), str(path), '--output_dir', str(target), '--emit_pdf', '--dpi', '100'], env=env, capture_output=True, text=True, timeout=300)
            (target / 'render.log').write_text(result.stdout + result.stderr)
            if result.returncode:
                raise RuntimeError(path.name + ': ' + result.stderr[-1500:])
            pages = sorted(target.glob('page-*.png'))
            if not pages:
                raise RuntimeError('Keine gerenderte Seite: ' + str(path))
            return dict(file=str(path), pages=len(pages), images=[str(p) for p in pages])
        with ThreadPoolExecutor(max_workers=3) as executor:
            rendered = list(executor.map(render, docxs))
        (args.qa_dir / 'word-render.json').write_text(json.dumps(rendered, ensure_ascii=False, indent=2) + '\n')
        print('Word-Seiten gerendert:', sum(x['pages'] for x in rendered), flush=True)


if __name__ == '__main__':
    main()
