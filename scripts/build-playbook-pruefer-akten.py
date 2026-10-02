#!/usr/bin/env python3
"""Baut ausschließlich die zwei Playbookakten mit dem gemeinsamen Office-Builder.

--out-root erlaubt einen reproduzierbaren Vergleich außerhalb des Repositorys.
Gesamt-PDFs und Archive entstehen durch die zentralen Repo-Builder.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import importlib.util
import json
import subprocess
import sys
from docx import Document
from docx.shared import Pt

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('playbook_native_builder', ROOT / 'scripts/build-berlin-bildungsakten.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
from playbook_pruefer_akten_daten import CASES


def word(item, target):
    layout_item = dict(item)
    if item['file'].startswith(('04_', '05_', '06_')):
        # Verträge führen ihre Parteien vollständig in Abschnitt 1 auf.
        # Ein zusätzlicher Briefadressblock würde nur den Text wiederholen.
        layout_item.pop('sender', None)
        layout_item.pop('recipient', None)
    builder.word(layout_item, target)
    doc = Document(target)
    doc.core_properties.author = item.get('sender', 'Aktenverwaltung')
    if item['file'].startswith(('04_', '05_', '06_')):
        doc.styles['Heading 1'].paragraph_format.space_before = Pt(10)
        doc.styles['Heading 1'].paragraph_format.space_after = Pt(6)
        doc.styles['Normal'].paragraph_format.space_after = Pt(6)
    for p in doc.paragraphs:
        if p.text.startswith(('Startposition ', 'Rückfallposition ', 'Nicht akzeptable Position ')):
            p.paragraph_format.keep_with_next = True
            for r in p.runs:
                r.bold = True
        if p.text.startswith(('NDA-', 'ARB-')):
            p.paragraph_format.space_after = Pt(6)
    builder.native.stable_docx(doc, target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--qa-dir', type=Path, required=True)
    parser.add_argument('--out-root', type=Path, default=ROOT / 'testakten')
    parser.add_argument('--render-docx', type=Path)
    parser.add_argument('--only', nargs='*')
    args = parser.parse_args()
    args.qa_dir.mkdir(parents=True, exist_ok=True)
    selected = [c for c in CASES if not args.only or c['slug'] in args.only]
    if args.only and set(args.only) - {c['slug'] for c in selected}:
        raise ValueError('Unbekannte Akte')
    docxs = []
    for case in selected:
        directory = args.out_root / case['slug']
        directory.mkdir(parents=True, exist_ok=True)
        names = [d['file'] for d in case['documents']]
        if len(set(names)) != len(names) or any(Path(n).name != n for n in names):
            raise ValueError('Ungültige Dateinamen')
        for item in case['documents']:
            target = directory / item['file']
            if target.suffix == '.docx':
                word(item, target)
                docxs.append(target)
            elif target.suffix == '.txt':
                target.write_text(item['title'] + '\n' + item['date'] + '\n\n' + item['body'] + '\n', encoding='utf-8')
            elif target.suffix != '.eml':
                raise ValueError('Unbekanntes Format: ' + target.suffix)
        for item in case['documents']:
            if item['file'].endswith('.eml'):
                builder.mail(item, directory / item['file'], case['attachments'].get(item['file'], []))
        print(case['slug'], len(case['documents']), flush=True)
    if args.render_docx:
        runtime = Path(sys.executable).resolve().parents[3]
        env = builder.render_helpers.renderer_environment(args.qa_dir, runtime)
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
