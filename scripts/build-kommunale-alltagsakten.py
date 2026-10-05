#!/usr/bin/env python3
"""Baut ausschließlich acht zusätzliche kleine kommunale Haftpflichtakten."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import importlib.util
import json
import re
import subprocess
import sys
import yaml
from pypdf import PdfReader
from kommunale_alltagsakten_daten import CASES, REVIEW

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('kommunal_helper', ROOT/'scripts/build-kommunale-haftpflicht-akten.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)

def add_release_bookmarks(writer, testakte_dir):
    case = next(c for c in CASES if c['slug'] == testakte_dir.name)
    compact = lambda s: re.sub(r'\s+', '', s)
    texts = [compact(p.extract_text() or '') for p in writer.pages]
    for name in sorted(d['file'] for d in case['documents']):
        hits = [i for i, text in enumerate(texts) if compact(name) in text]
        if len(hits) != 1:
            raise ValueError(f'Keine eindeutige PDF-Startseite für {name}: {hits}')
        page = hits[0] + (1 if Path(name).suffix == '.docx' else 0)
        if page >= len(writer.pages):
            raise ValueError('Originalseite fehlt: '+name)
        writer.add_outline_item(Path(name).stem, page)

def metadata(case, directory):
    slug = case['slug']
    names = sorted(d['file'] for d in case['documents'])
    titles = {d['file']: d['title'] for d in case['documents']}
    core = '\n'.join(f'- [{n}]({n})' for n in case['core'])
    rows = '\n'.join(f'| [{n}]({n}) | {titles[n]} |' for n in names)
    version = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())['version']
    pdf = directory/'gesamt-pdf'/f'{slug}_gesamt.pdf'
    extent = f'Das Gesamt-PDF umfasst {len(PdfReader(pdf).pages)} Seiten. ' if pdf.is_file() else ''
    (directory/'README.md').write_text(f'''<!-- decimal-headings -->

# 1. {case['title']}

## 1.1. Vorgang und Auftrag

{case['summary']}

Stand: 05.10.2026. Die Auftragsmail benennt die konkrete Mandantin, den Bearbeitungsstand und den gewünschten Empfänger des Antwortentwurfs. Erarbeiten Sie anhand der Originale einen internen Prüfvermerk und den beauftragten, vollständig ausformulierten Antwortentwurf. Offene Angaben sind gezielt nachzufragen. Es besteht kein Auftrag zum Versand, zur Zahlung oder zum Anerkenntnis.

Passendes Plugin: [Kommunale Haftpflicht](../../kommunale-haftpflicht/README.md).

## 1.2. Kleiner Einstieg

Beginnen Sie für eine kurze Vorführung mit diesen Kernunterlagen. Die weiteren Dateien erlauben anschließend einen vollständigen Belegabgleich. Die Akte enthält keine Musterlösung und keinen fertig ausgearbeiteten Vortrag.

{core}

## 1.3. Umfang und Herkunft

{extent}{len(names)} native Originalunterlagen in bearbeitbaren Word-Dateien, echten E-Mail-Dateien und gegebenenfalls einem Text-Export. Genannte E-Mail-Anlagen sind tatsächlich als identische MIME-Dateien beigefügt; die beigefügte und die gesondert gespeicherte Fassung bilden denselben Beleg.

<!-- reserved-example-contacts -->

Alle Ereignisse, Personen, Unternehmen, Straßen, Kontakte und Aktenzeichen sind erfunden. Der Raum Würzburg und Bayern bilden den geografischen und landesrechtlichen Rahmen; die in einzelnen Akten genannte Stadt Lindenquell ist erfunden. Reale kommunale Behördenbezeichnungen dienen ausschließlich der Verfahrenseinordnung; kein tatsächlicher Schadensvorgang oder Pflichtverstoß einer wirklichen Verwaltung wird behauptet. `.example`-Kontaktadressen sind nicht zustellbar. Die Dokumente sind keine echten behördlichen oder medizinischen Urkunden.

AKHA bezeichnet das fachliche Bearbeitungsumfeld. Aus dem Ordnernamen folgen weder eine reale Mitgliedschaft noch Versicherungsdeckung oder Rückdeckung. Echte AKHA-Bedingungen, interne Schwellen und Rückversicherungsverträge werden nicht nachgebildet. Haftung, eigene Ersatzforderungen der Kommune, primäre Deckung und eine mögliche interne Rückdeckung sind nach dem konkreten Auftrag getrennt zu bearbeiten.

## 1.4. Unterlagen

| Datei | Inhalt |
| --- | --- |
{rows}

## 1.5. Downloads

{helper.NOTICE}

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF | PDF | [Gesamte Akte](gesamt-pdf/{slug}_gesamt.pdf) |
| Akten-ZIP | ZIP | [Native Originale und Gesamt-PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v{version}/testakte-{slug}.zip) |
| Einzel-PDF-ZIP | ZIP | [Jedes Aktenstück als PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v{version}/testakte-{slug}-einzelpdfs.zip) |

Die Archive enthalten alle Arbeitsunterlagen unmittelbar auf der ZIP-Wurzelebene. Die zweisprachige README.txt gehört in beide Archive; redaktionelle Bewertungsdateien und Musterlösungen werden nicht exportiert. Die PDFs enthalten keine Hinweisseite.
''', encoding='utf-8')
    checks = [dict(id='arbeitsbestand', check_type='working_file_count', description='Alle nativen Originalunterlagen sind vorhanden.', min=len(names))]
    for ext in ('docx', 'eml', 'txt'):
        count = sum(n.endswith('.'+ext) for n in names)
        if count:
            checks.append(dict(id='format-'+ext, check_type='file_count', description=f'{count} Originale im Format {ext.upper()}.', glob='*.'+ext, min=count))
    for i, name in enumerate(case['core']):
        checks.append(dict(id=f'kernbeleg-{i+1}', check_type='file_exists', description='Kernunterlage vorhanden.', path=name))
    for i, description in enumerate((*REVIEW[slug], 'Konkrete Mandantin und Interessenlage beibehalten; keine unbelegte Deckung oder AKHA-Mitgliedschaft annehmen.', 'Einen adressatengerechten ausformulierten Antwortentwurf erstellen; offene Nachweise konkret benennen und nichts versenden.')):
        checks.append(dict(id=f'fach-{i+1}', check_type='human_review', description=description, note='Offenes Kriterium für eine spätere Anwendungsprüfung; keine automatisch bestandene juristische Bewertung.'))
    (directory/'rubric.yaml').write_text(yaml.safe_dump(dict(name=case['title'], plugin='kommunale-haftpflicht', stand='2026-10-05', checks=checks), allow_unicode=True, sort_keys=False), encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--qa-dir', type=Path, required=True)
    parser.add_argument('--out-root', type=Path, default=ROOT/'testakten')
    parser.add_argument('--only', nargs='*')
    parser.add_argument('--metadata-only', action='store_true')
    parser.add_argument('--render-docx', type=Path)
    args = parser.parse_args()
    cases = [c for c in CASES if not args.only or c['slug'] in args.only]
    if args.only and set(args.only) != {c['slug'] for c in cases}:
        raise ValueError('Unbekannte Aktenauswahl')
    args.qa_dir.mkdir(parents=True, exist_ok=True)
    docxs, inventory = [], []
    for case in cases:
        directory = args.out_root/case['slug']
        directory.mkdir(parents=True, exist_ok=True)
        names = [d['file'] for d in case['documents']]
        if len(names) != len(set(names)) or any(Path(n).name != n for n in names) or case.get('xlsx'):
            raise ValueError('Unerwarteter Quellenbestand: '+case['slug'])
        if not args.metadata_only:
            for item in case['documents']:
                target = directory/item['file']
                if target.suffix == '.docx':
                    helper.word(item, target)
                    docxs.append(target)
                elif target.suffix == '.txt':
                    target.write_text(item['title']+'\n'+item['date']+'\n\n'+item['body']+'\n', encoding='utf-8')
            pending = [d for d in case['documents'] if d['file'].endswith('.eml')]
            completed = {d['file'] for d in case['documents'] if not d['file'].endswith('.eml')}
            # E-Mail-Anlagen können andere E-Mails enthalten. Nach Abhängigkeiten bauen.
            while pending:
                ready = [d for d in pending if all(n in completed and (directory/n).is_file() for n in case['attachments'].get(d['file'], []))]
                if not ready:
                    raise ValueError('Fehlende oder zyklische MIME-Anlagen: '+case['slug'])
                for item in ready:
                    helper.builder.mail(item, directory/item['file'], case['attachments'].get(item['file'], []))
                    pending.remove(item)
                    completed.add(item['file'])
        metadata(case, directory)
        inventory.append(dict(case=case['slug'], files=sorted(names), core=case['core'], attachments=case['attachments']))
        print(case['slug'], len(names), 'Originale', flush=True)
    (args.qa_dir/'akten-inventar.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2)+'\n')
    if args.render_docx and docxs:
        env = helper.builder.render_helpers.renderer_environment(args.qa_dir, Path(sys.executable).resolve().parents[3])
        def render(path):
            dest = args.qa_dir/'word'/path.parent.name/path.stem
            dest.mkdir(parents=True, exist_ok=True)
            run = subprocess.run([sys.executable, str(args.render_docx), str(path), '--output_dir', str(dest), '--emit_pdf', '--dpi', '100'], env=env, capture_output=True, text=True, timeout=300)
            (dest/'render.log').write_text(run.stdout+run.stderr)
            if run.returncode:
                raise RuntimeError(path.name+': '+run.stderr[-1500:])
            images = sorted(dest.glob('page-*.png'))
            if not images:
                raise RuntimeError('Keine gerenderte Seite: '+str(path))
            return dict(file=str(path), pages=len(images), images=[str(p) for p in images])
        with ThreadPoolExecutor(max_workers=3) as pool:
            result = list(pool.map(render, docxs))
        (args.qa_dir/'word-render.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
        print('Word-Seiten:', sum(item['pages'] for item in result), flush=True)

if __name__ == '__main__':
    main()
