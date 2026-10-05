#!/usr/bin/env python3
"""Erzeugt ausschließlich die Originale und Metadaten der Verletzungsrisiko-Akte."""
import argparse
import csv
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

import yaml
from pypdf import PdfReader

from verletzungsrisiko_akte_daten import SLUG, TITLE, DOCUMENTS, TEXTS, CSV_NAME, CSV_HEADERS, CSV_ROWS, ATTACHMENTS, CORE
from testakte_disclaimer import NOTICE_MARKDOWN

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('verletzungsrisiko_native', ROOT/'scripts/build-kommunale-haftpflicht-akten.py')
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)


def metadata(directory):
    names = sorted([d['file'] for d in DOCUMENTS] + list(TEXTS) + [CSV_NAME])
    titles = {d['file']: d['title'] for d in DOCUMENTS}
    titles.update({'13_Chat_Insassen.txt': 'Zeitnaher Nachrichtenverlauf zwischen den Insassen', '16_Zahlung_Fahrzeug.txt': 'Getrennte Sachschadenzahlung', CSV_NAME: 'Gebuchte Leistungen der Krankenkasse je Person'})
    version = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())['version']
    pdf = directory/'gesamt-pdf'/f'{SLUG}_gesamt.pdf'
    extent = f'Das Gesamt-PDF enthält {len(PdfReader(pdf).pages)} Seiten. ' if pdf.exists() else ''
    rows = '\n'.join(f'| [{n}]({n}) | {titles[n]} |' for n in names)
    core = '\n'.join(f'- [{n}]({n})' for n in CORE)
    (directory/'README.md').write_text(f'''<!-- decimal-headings -->

# 1. {TITLE}

## 1.1. Vorgang und Einstieg

Ein kommunaler Transporter stößt beim Rangieren am Bürgerhaus gegen einen besetzten Pkw. Ottokar Wolkenbein und Thusnelda Pimpinella lassen sich in derselben Ambulanz untersuchen; später gehen unterschiedliche Forderungen und Unterlagen bei der Frankenbogen Kommunalversicherung ein.

Stand: 05.10.2026. Beginnen Sie mit der Auftragsmail. Auftraggeber ist ausschließlich der Versicherer. Gefordert sind ein interner Vermerk und getrennte Antwortentwürfe, keine Auszahlung und kein automatischer Versand. Die Akte ist beim Plugin [Kommunale Haftpflicht](../../kommunale-haftpflicht/README.md) eingeordnet. Der Titel bezeichnet die erfundene Fallanlage; er ist keine Feststellung, dass die vorgetragenen Beschwerden nur eingebildet seien.

Für einen kurzen Einstieg reichen zunächst diese sechs Unterlagen:

{core}

Die weiteren Belege dienen der anschließenden Bearbeitung und gezielten Rückfrage. Die Arbeitsdateien enthalten keine Musterlösung, keine Bewertungsmatrix und keine abgeschriebene Seminarfolie.

## 1.2. Downloads

<!-- BEGIN gesamt-pdf-section (autogen) -->

{NOTICE_MARKDOWN}

| Format | Download |
| --- | --- |
| Gesamt-PDF | [Vollständige Lesefassung](gesamt-pdf/{SLUG}_gesamt.pdf) |
| Gemischte Originaldateien und Gesamt-PDF | [Akten-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v{version}/testakte-{SLUG}.zip) |
| Jede Unterlage als eigenes PDF | [Einzel-PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v{version}/testakte-{SLUG}-einzelpdfs.zip) |

<!-- END gesamt-pdf-section (autogen) -->

{extent}18 Originale: zehn Word-Dokumente, fünf E-Mails, zwei Textdateien und eine CSV-Datei. Beide ZIPs sind flach, ohne Unterordner. Das Originalpaket enthält kein Markdown. Die drei Quittungen sind getrennte Dokumente, ebenso die Behandlungsberichte der beiden Insassen. E-Mail-Anlagen sind tatsächlich beigefügt und bytegleich mit den einzeln abgelegten Dateien; sie sind keine zusätzlichen Belege oder Schäden. Die ZIPs enthalten den zweisprachigen Hinweis in README.txt; die PDFs selbst enthalten keine Warnseite.

English: One incident, two occupants, separate medical records and claims. Start with the instruction email. Choose the combined reading PDF, the flat archive of native files, or one PDF per source document. No answer key is included. Each archive contains a bilingual notice in README.txt.

## 1.3. Unterlagen

| Datei | Inhalt |
| --- | --- |
{rows}

## 1.4. Herkunft und Einordnung

<!-- reserved-example-contacts -->

Personen, Stadt Lindenquell, Klinik, Krankenkasse, Versicherer, Anschriften und Vorgangsdaten sind erfunden. Würzburg ist allein der geografische Rahmen. `.example`-Adressen sind nicht zustellbar. Es handelt sich nicht um echte Behandlungsunterlagen oder Zahlungsbelege. AKHA bezeichnet hier nur das fachliche Bearbeitungsumfeld; eine wirkliche Mitgliedschaft oder bestimmte Ausgleichsbedingungen werden nicht behauptet. Das bereitgestellte Seminarfoto mit erkennbaren Personen wird nicht veröffentlicht.

[Alle Testakten](../README.md) · [Plugin](../../kommunale-haftpflicht/README.md) · [Repository](../../README.md)
''', encoding='utf-8')
    checks = [dict(id='bestand', check_type='working_file_count', description='18 getrennte Originalunterlagen vorhanden.', min=18)]
    for extension, count in [('docx', 10), ('eml', 5), ('txt', 2), ('csv', 1)]:
        checks.append(dict(id='format-'+extension, check_type='file_count', description=f'{count} Originale im Format {extension.upper()}.', glob='*.'+extension, min=count))
    for i, name in enumerate(CORE):
        checks.append(dict(id=f'kern-{i+1}', check_type='file_exists', description='Kernunterlage vorhanden.', path=name))
    for i, question in enumerate([
        'Werden die beiden Personen, klinische Befunde, bloßer Verdacht und tatsächliche Beschwerden getrennt gewürdigt, ohne aus einem unauffälligen Röntgenbild allein auf fehlende Verletzung zu schließen?',
        'Werden Primärverletzung, Unfallursächlichkeit, einzelne Folgekosten und die jeweils zutreffenden Beweisanforderungen unterschieden?',
        'Bleiben Kassenregress und Eigenforderungen getrennt, ohne gleiche MIME-Anlagen doppelt zu zählen oder die Sachschadenzahlung als umfassendes Anerkenntnis zu verwenden?',
        'Wird bei ambulanten Leistungen Paragraf 116 Absatz 8 SGB X mitgeprüft, ohne die Pauschale als Ersatz für den Haftungsgrund oder als vereinbarte Pauschalierung zu behandeln?',
        'Wird die Kfz-Rechtsprechung zum Werkstattrisiko nicht ungeprüft als medizinische Haftungsregel übertragen?',
        'Werden offene Kostenpositionen konkret nachgefragt und getrennte, vollständig ausformulierte Antwortentwürfe ohne unbeauftragten Versand geliefert?',
    ]):
        checks.append(dict(id=f'fach-{i+1}', check_type='human_review', description=question, note='Offenes Kriterium für eine spätere Anwendungsprüfung, kein automatisch bestandener juristischer Test.'))
    (directory/'rubric.yaml').write_text(yaml.safe_dump(dict(name=TITLE, plugin='kommunale-haftpflicht', stand='2026-10-05', checks=checks), allow_unicode=True, sort_keys=False), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--metadata-only', action='store_true')
    parser.add_argument('--render-docx', type=Path)
    parser.add_argument('--qa-dir', type=Path)
    args = parser.parse_args()
    directory = ROOT/'testakten'/SLUG
    directory.mkdir(parents=True, exist_ok=True)
    if not args.metadata_only:
        for item in DOCUMENTS:
            if item['file'].endswith('.docx'):
                native.word(item, directory/item['file'])
        for name, text in TEXTS.items():
            (directory/name).write_text(text, encoding='utf-8')
        with (directory/CSV_NAME).open('w', encoding='utf-8', newline='') as stream:
            writer = csv.writer(stream, delimiter=';')
            writer.writerow(CSV_HEADERS)
            writer.writerows(CSV_ROWS)
        for item in DOCUMENTS:
            if item['file'].endswith('.eml'):
                native.builder.mail(item, directory/item['file'], ATTACHMENTS.get(item['file'], []))
    metadata(directory)
    if args.render_docx:
        if not args.qa_dir:
            parser.error('--render-docx benötigt --qa-dir')
        args.qa_dir.mkdir(parents=True, exist_ok=True)
        env = native.builder.render_helpers.renderer_environment(args.qa_dir, Path(sys.executable).resolve().parents[3])
        for path in sorted(directory.glob('*.docx')):
            dest = args.qa_dir/'word'/path.stem
            result = subprocess.run([sys.executable, str(args.render_docx), str(path), '--output_dir', str(dest), '--emit_pdf', '--dpi', '110'], env=env, capture_output=True, text=True, timeout=300)
            if result.returncode or not list(dest.glob('page-*.png')):
                raise RuntimeError(path.name+': '+result.stdout+result.stderr)
            print('Gerendert:', path.name, flush=True)
    print(f'{SLUG}: 18 Originale und Metadaten')


if __name__ == '__main__':
    main()
