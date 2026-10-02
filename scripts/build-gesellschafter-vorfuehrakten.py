#!/usr/bin/env python3
"""Baut ausschließlich die beiden Vorführakten aus individuellen Quellentexten.

Die optionale Paketstufe verwendet die zentralen Konverter, ohne Sammelarchive
aller anderen Akten vorauszusetzen. Vorhandene Akten werden nicht verändert.
"""
from pathlib import Path
import argparse
import csv
import importlib.util
import json
import os
import subprocess
import sys
import zipfile
from concurrent.futures import ThreadPoolExecutor

from docx import Document
from docx.shared import Pt
from vorfuehrakte_gesellschafter_berlin import CASE as BERLIN
from vorfuehrakte_gesellschafter_muenchen import CASE as MUENCHEN

ROOT = Path(__file__).resolve().parents[1]
CASES = [BERLIN, MUENCHEN]


def module(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / file)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


builder = module('vorfuehr_native', 'build-berlin-bildungsakten.py')


def write_readme(case, directory):
    files = [(d['file'], d['title']) for d in case['documents']]
    files += [(case['xlsx'], case['xlsx_title'])]
    lines = [f"# 1. {case['title']}", '', '## 1.1. Vorgang und Auftrag', '',
             case['summary'], '', f"Aktenstand: {case['date']}. Mandant: {case['client']}.", '',
             case['assignment'], '',
             'Passendes Plugin: [`gesellschafterstreit`](../../gesellschafterstreit/README.md).', '',
             '## 1.2. Verwendung im gemeinsamen 60-Minuten-Termin', '',
             'Für diese Akte sind ungefähr 30 Minuten vorgesehen: fünf Minuten für Auftrag und Kernunterlagen, '
             '15 Minuten für Rückfragen und Dokumententwurf, zehn Minuten für Belegabgleich und Besprechung. '
             'Die Zeitaufteilung ist ein Vorschlag, keine Leistungszusage eines Systems. '
             'Der übrige Aktenbestand dient der Vertiefung und der Überprüfung konkreter Behauptungen.', '',
             'Kernunterlagen: ' + ', '.join(f'[{n}]({n})' for n in case['core']) + '.', '',
             'Mit dem Aktenstand arbeiten. Gerichtliche oder vertragliche Fristen sind nicht auf den Tag '
             'einer späteren Schulung verschoben. Keine Unterlage enthält eine Musterlösung oder eine Bewertung der Bearbeitung.', '',
             '<!-- reserved-example-contacts -->', '',
             'Personen, Unternehmen, Geschäftszeichen und Vorgänge sind erfunden. Die Kontaktadressen mit `.example` '
             'sind nicht erreichbar. Gerichts- und Registerunterlagen sind keine amtlichen Ausfertigungen. '
             'Die Akte ist ausschließlich für Schulungen bestimmt.', '',
             '## 1.3. Einzelunterlagen', '', '| Datei | Inhalt |', '| --- | --- |']
    lines += [f'| [{name}]({name}) | {title} |' for name, title in files]
    lines += ['', '## 1.4. Englischer Kurzüberblick', '', case['english'], '',
              'The two cases are separate matters for one sixty-minute session. Each has a limited core reading set '
              'and additional evidence. No model defence or completed shareholders’ agreement is included.', '']
    (directory / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    counts = {}
    for name, _ in files:
        ext = Path(name).suffix[1:]
        counts[ext] = counts.get(ext, 0) + 1
    # Prüfkriterien gehören zur Qualitätssicherung, niemals in Arbeitsarchive.
    rubric = [f"name: {case['title']}", 'plugin: gesellschafterstreit', "stand: '2026-10-02'",
              'pruefstatus: Technischer Bestand und Aktenkonsistenz geprüft; keine Bewertung einer erzeugten Lösung.',
              'checks:', '- id: arbeitsbestand', '  check_type: working_file_count',
              '  description: Alle eigenständigen Quellenunterlagen sind vorhanden.', f'  min: {len(files)}']
    for ext, count in sorted(counts.items()):
        rubric += [f'- id: format-{ext}', '  check_type: file_count', f'  description: Originaldateien im Format {ext.upper()}.',
                   f"  glob: '*.{ext}'", f'  min: {count}']
    rubric += ['- id: gesamt-pdf', '  check_type: file_exists', '  description: Vollständige Lesefassung vorhanden.',
               f"  path: gesamt-pdf/{case['slug']}_gesamt.pdf", '- id: belegtreue', '  check_type: human_review',
               '  description: Werden Behauptungen, Belege und noch offene Tatsachen auseinandergehalten?',
               '  note: Eine spätere Bearbeitung ist gesondert fachlich zu prüfen.']
    (directory / 'rubric.yaml').write_text('\n'.join(rubric) + '\n', encoding='utf-8')


BERLIN.update(xlsx='19_Projektkonto.xlsx', xlsx_title='Projektkonto August, Buchungen und Kontofortschreibung',
              english='Berlin: A stage-lighting company needs a defence against a shareholder’s challenge to his removal as managing director. The records include the claim, court directions, service record, articles, minutes, invoice, delivery record and correspondence.')
MUENCHEN.update(xlsx='18_Beteiligungsrechnung.xlsx', xlsx_title='Rechnung zur vorgeschlagenen Kapitalaufnahme',
                english='Munich: Two founders want to admit a new investor into a small equipment business. Conflicting proposals, existing articles, development records, budget evidence and bank correspondence support the drafting exercise.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--qa-dir', type=Path, required=True)
    parser.add_argument('--out-root', type=Path, default=ROOT / 'testakten')
    parser.add_argument('--render-docx', type=Path)
    parser.add_argument('--packages', type=Path)
    parser.add_argument('--native-only', action='store_true')
    args = parser.parse_args()
    args.qa_dir.mkdir(parents=True, exist_ok=True)
    docxs = []
    for case in CASES:
        directory = args.out_root / case['slug']
        directory.mkdir(parents=True, exist_ok=True)
        names = [d['file'] for d in case['documents']] + [case['xlsx']]
        if len(names) != len(set(names)) or any(Path(n).name != n for n in names):
            raise ValueError('Ungültige Dateinamen')
        for item in case['documents']:
            target = directory / item['file']
            if target.suffix == '.docx':
                builder.word(item, target)
                doc = Document(target)
                doc.styles['Heading 1'].paragraph_format.space_before = Pt(9)
                doc.styles['Heading 1'].paragraph_format.space_after = Pt(5)
                builder.native.stable_docx(doc, target)
                docxs.append(target)
            elif target.suffix == '.pdf':
                builder.native.pdf(item, target)
            elif target.suffix == '.txt':
                target.write_text(item['title'] + '\n' + item['date'] + '\n\n' + item['body'] + '\n', encoding='utf-8')
            elif target.suffix == '.csv':
                with target.open('w', newline='', encoding='utf-8-sig') as stream:
                    writer = csv.writer(stream, delimiter=';')
                    writer.writerow(item['headers'])
                    writer.writerows(item['rows'])
            elif target.suffix != '.eml':
                raise ValueError(target.suffix)
        for item in case['documents']:
            if item['file'].endswith('.eml'):
                builder.mail(item, directory / item['file'], case['attachments'].get(item['file'], []))
        write_readme(case, directory)
        print(case['slug'], len(names), 'Originale', flush=True)
    if args.native_only:
        return
    for case in CASES:
        if not (args.out_root / case['slug'] / case['xlsx']).is_file():
            raise ValueError('Arbeitsmappe zuerst mit build-gesellschafter-vorfuehrtabellen.mjs erstellen.')
    runtime = Path(sys.executable).resolve().parents[3]
    env = builder.render_helpers.renderer_environment(args.qa_dir, runtime)
    os.environ.update(env)
    if args.render_docx:
        def render(path):
            out = args.qa_dir / 'word' / path.parent.name / path.stem
            out.mkdir(parents=True, exist_ok=True)
            result = subprocess.run([sys.executable, str(args.render_docx), str(path), '--output_dir', str(out),
                                     '--emit_pdf', '--dpi', '100'], capture_output=True, text=True, timeout=300, env=env)
            (out / 'render.log').write_text(result.stdout + result.stderr)
            pages = sorted(out.glob('page-*.png'))
            if result.returncode or not pages:
                raise RuntimeError(f'{path.name}: {result.stderr[-1500:]}')
            return dict(file=str(path), pages=len(pages), images=[str(p) for p in pages])
        with ThreadPoolExecutor(max_workers=2) as executor:
            manifest = list(executor.map(render, docxs))
        (args.qa_dir / 'word-render.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
        print('Word-Seiten gerendert:', sum(d['pages'] for d in manifest), flush=True)
    if args.packages:
        gesamt = module('vorfuehr_gesamt', 'build-gesellschafter-vorfuehrpakete.py')
        originals = module('vorfuehr_originals', 'build-testakten-release-zips.py')
        individual = module('vorfuehr_individual', 'build-testakten-einzelpdf-zips.py')
        inject = module('vorfuehr_downloads', 'inject-gesamt-pdf-section.py')
        args.packages.mkdir(parents=True, exist_ok=True)
        for case in CASES:
            directory = args.out_root / case['slug']
            print(gesamt.build_release_pdf(directory), flush=True)
            originals.build_single(directory, args.packages)
            output = args.packages / f"testakte-{case['slug']}-einzelpdfs.zip"
            with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
                count = individual.add_testakte(archive, directory)
            if count != len(case['documents']) + 1:
                raise RuntimeError(f'{case["slug"]}: {count} Einzel-PDFs statt eines je Original')
            inject.inject(directory / 'README.md', case['slug'])
            print(output.name, count, 'Einzel-PDFs', flush=True)


if __name__ == '__main__':
    main()
