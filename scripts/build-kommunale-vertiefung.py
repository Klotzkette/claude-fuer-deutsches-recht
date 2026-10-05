#!/usr/bin/env python3
"""Ergänzt kommunale Akten, ohne bisherige native Originale zu überschreiben."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import format_datetime, formataddr, getaddresses
import importlib.util
import hashlib
import json
import mimetypes
from pathlib import Path
import re
import shutil
import subprocess
import sys
import yaml
from pypdf import PdfReader
from kommunale_vertiefung_daten import cases, FOLDER, native_names
from kommunale_schriftverkehr_daten import cases as old_cases
from readme_decimal_headings import normalize_decimal_headings
from testakte_disclaimer import NOTICE_DE, NOTICE_EN
from testakte_einzelpdf_common import document_arcname_pairs

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('schriftverkehr', ROOT/'scripts/build-kommunale-schriftverkehr.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
NOTICE = f'> {NOTICE_DE}\n>\n> {NOTICE_EN}'

def body(case, item):
    return old.claim_body(case, item)

def source(directory, name):
    p = directory/name
    if not p.is_file() or p.is_symlink() or not p.resolve().is_relative_to(directory.resolve()):
        raise ValueError('Fehlender oder unsicherer Beleg: '+str(p))
    return p

def email(case, item, directory):
    msg = EmailMessage(policy=SMTP)
    for header, key in [('From', 'sender'), ('To', 'recipient')]:
        values = getaddresses([item[key]])
        if not values or any('@' not in addr for _, addr in values):
            raise ValueError('Ungültige Mailadresse: '+item['file'])
        msg[header] = ', '.join(formataddr(pair) for pair in values)
    msg['Subject'] = item['title']
    msg['Date'] = format_datetime(datetime.fromisoformat(item['date']))
    msg['Message-ID'] = f"<{case['slug']}.{Path(item['file']).stem}.vertiefung@akten.example>"
    if item.get('reply_to'):
        msg['In-Reply-To'] = item['reply_to']
    msg.set_content(item['body'], charset='utf-8')
    names = set()
    for name in case.get('attachments', {}).get(item['file'], []):
        p = source(directory, name)
        if p.name in names:
            raise ValueError('Doppelter MIME-Dateiname')
        names.add(p.name)
        mime = mimetypes.guess_type(p.name)[0] or 'application/octet-stream'
        major, minor = mime.split('/', 1)
        if major == 'message':
            major, minor = 'application', 'octet-stream'
        msg.add_attachment(p.read_bytes(), maintype=major, subtype=minor, filename=p.name)
    if msg.is_multipart():
        boundary = 'vertiefung-'+case['slug']+'-'+Path(item['file']).stem
        if len(boundary) > 70:
            boundary = 'vertiefung-'+hashlib.sha256(boundary.encode()).hexdigest()[:40]
        msg.set_boundary(boundary)
    (directory/FOLDER/item['file']).write_bytes(msg.as_bytes())

def metadata(case, directory):
    path = directory/'README.md'
    version = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())['version']
    if case['is_new']:
        core = '\n'.join(f'- [{Path(p).name}]({p})' for p in case['core'])
        if any(Path(p).suffix.lower() == '.pdf' for p in case['core']):
            core = NOTICE+'\n\n'+core
        text = f'''<!-- decimal-headings -->

# {case['title']}

## Vorgang und Auftrag

{case['summary']}

Stand: 05.10.2026. Die Auftragsmail bestimmt Mandantin und Bearbeitungsziel. Erarbeiten Sie aus dem Akteneingang einen eigenen Haftungsvermerk, konkrete Rückfragen und das bestellte Schreiben. Der gesondert bereitgestellte Klageentwurf dient der Bearbeitung und Gegenprüfung; er ist kein tatsächlich eingereichter Schriftsatz. Ein Entwurf aus einer anderen Parteiperspektive begründet kein zusätzliches Mandat.

Passendes Plugin: [Kommunale Haftpflicht](../../kommunale-haftpflicht/README.md).

## Kleiner Einstieg

{core}

## Herkunft

<!-- reserved-example-contacts -->

Alle Personen, Körperschaften mit erfundenem Namen, Unternehmen, Anschriften, Vorgänge, Beträge und Vertragsbedingungen dieser Akte sind erfunden. Würzburg und Bayern bilden den geografischen und landesrechtlichen Rahmen. Reale Gerichtsbezeichnungen dienen nur der Einordnung. Es werden keine tatsächlichen Pflichtverletzungen einer wirklichen Verwaltung behauptet. `.example`-Adressen sind nicht zustellbar. Die Dokumente sind keine echten amtlichen oder medizinischen Urkunden.

Versicherungsscheine, Selbstbehalte, Meldegrenzen und Rückversicherungsprioritäten sind ausschließlich Bedingungen des einzelnen fiktiven Vertrags. Sie bilden keine echten AKHA-Bedingungen nach. Anspruch der geschädigten Person, Deckung der haftenden Körperschaft und Rückdeckung des Versicherers bleiben getrennte Rechtsverhältnisse.

## Downloads

{NOTICE}

| Was | Quelle |
| --- | --- |
| Gesamt-PDF | [Gesamte Akte](gesamt-pdf/{case['slug']}_gesamt.pdf) |
| Originalformate | [Akten-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v{version}/testakte-{case['slug']}.zip) |
| Einzel-PDFs | [PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v{version}/testakte-{case['slug']}-einzelpdfs.zip) |
'''
    else:
        text = path.read_text()
    start, end = '<!-- BEGIN kommunale-vertiefung -->', '<!-- END kommunale-vertiefung -->'
    text = re.sub(re.escape(start)+r'.*?'+re.escape(end)+r'\n*', '', text, flags=re.S)
    rows = []
    for item in case['documents']:
        n = item['file']
        link = f'[{n}]({FOLDER}/{n})'
        if item['kind'] == 'letter':
            pdf = str(Path(n).with_suffix('.pdf'))
            link += f' · [PDF]({FOLDER}/{pdf})'
        rows.append(f"| {link} | {item['title']} |")
    templates = sorted((directory/'briefvorlagen').glob('*.docx'))
    for p in templates:
        rows.append(f'| [{p.name}](briefvorlagen/{p.name}) | Bearbeitbare Fassung des bereits vorhandenen Briefs |')
    pdf = directory/'gesamt-pdf'/f"{case['slug']}_gesamt.pdf"
    page_text = f"Das aktualisierte Gesamt-PDF umfasst {len(PdfReader(pdf).pages)} Seiten." if pdf.exists() else ''
    count = len(document_arcname_pairs(directory))
    notes = case.get('notes', '')
    if isinstance(notes, list): notes = '\n\n'.join(notes)
    section = f'''{start}

## Vertiefter Schriftwechsel und bearbeitbare Briefe

{count} Arbeitsdateien einschließlich der gesonderten Fassungen in Word und PDF. {page_text} Ein Brief in zwei Formaten und seine MIME-Anlage sind derselbe Beleg; sie dürfen weder als zusätzlicher Schaden noch als unabhängige Bestätigung gezählt werden. Die Akteneingänge und bisher vorhandenen Klageentwürfe bleiben erhalten. Neu hinzugekommene Unterlagen befinden sich unter `{FOLDER}`. Vorhandene Brief-PDFs erhalten ergänzende Word-Fassungen unter `briefvorlagen`, soweit solche Briefe bereits zur Akte gehörten.

{notes}

{NOTICE}

| Unterlage | Inhalt |
| --- | --- |
{chr(10).join(rows)}

Die Korrespondenz zeigt Anforderung, Antwort, abweichende Standpunkte und den jeweiligen Entscheidungsstand. Eine Reserve ist keine Zahlung; eine Deckungsprüfung ist kein Haftungsanerkenntnis. Eine Rückversichereranfrage setzt einen konkreten Meldeanlass voraus. Bei kleinen Vorgängen bleibt es deshalb bei der Bearbeitung zwischen Versicherungsnehmer und Erstversicherer. Kein Schreiben wurde wirklich versandt und keine Klage eingereicht.

{end}
'''
    match = re.search(r'(?:<!-- decimal-anchor --> <a id="downloads"></a>\n\n)?^## [^\n]*Downloads\s*$', text, re.M)
    text = text[:match.start()]+section+'\n'+text[match.start():] if match else text+'\n'+section
    if not case['is_new']:
        text = re.sub(r'Insgesamt stehen jetzt \*\*(\d+) Originalunterlagen\*\* zur Verfügung\.', r'Nach dieser ersten Ergänzung umfasste der Bestand **\1 Originalunterlagen**. Den aktuellen Umfang nennt der zusätzliche Vertiefungsabschnitt.', text)
        text = text.replace('18 Originale: zehn Word-Dokumente', 'Der unveränderte Grundbestand umfasst 18 Originale: zehn Word-Dokumente')
        text = re.sub(r'(?<=Seiten\. )(\d+ native Originalunterlagen)', r'Grundbestand: \1', text)
        text = text.replace('Achtzehn native Originalunterlagen:', 'Grundbestand: achtzehn native Originalunterlagen:')
        text = text.replace('Die Arbeitsdateien enthalten keine Musterlösung, keine Bewertungsmatrix und keine abgeschriebene Seminarfolie.', 'Der ursprüngliche Akteneingang enthält keine Musterlösung, Bewertungsmatrix oder abgeschriebene Seminarfolie. Der später ergänzte Klageentwurf ist ein ausdrücklich bestelltes Arbeitsstück zur Gegenprüfung.')
        text = text.replace('No answer key is included.', 'The original case intake contains no answer key; a separately requested draft statement of claim is included for review.')
        text = re.sub(r'Das(?: aktualisierte)? Gesamt-PDF (?:umfasst|enthält) \d+ Seiten\.', page_text, text) if page_text else text
        if pdf.exists():
            pairs = document_arcname_pairs(directory)
            individual_pages = len(PdfReader(pdf).pages)-sum(p.suffix in {'.docx','.xlsx','.pdf'} for p,arc in pairs)
            text = re.sub(r'Das Einzel-PDF-ZIP enthält [^.\n]+ Unterlagen mit zusammen [^.\n]+ Seiten\.', f'Das Einzel-PDF-ZIP enthält {count} Unterlagen mit zusammen {individual_pages} Seiten.', text)
    path.write_text(normalize_decimal_headings(text))
    rubric_path = directory/'rubric.yaml'
    rubric = yaml.safe_load(rubric_path.read_text()) if rubric_path.exists() else {'name': case['title'], 'plugin': 'kommunale-haftpflicht', 'stand': '2026-10-05', 'checks': []}
    if case['is_new']:
        rubric['name'] = case['title']
        rubric['stand'] = '2026-10-05'
    rubric['checks'] = [x for x in rubric.get('checks', []) if not x['id'].startswith('vertiefung-')]
    for i, name in enumerate(native_names(case), 1):
        rubric['checks'].append(dict(id=f'vertiefung-datei-{i}', check_type='file_exists', description='Die zusätzliche Korrespondenz ist vorhanden.', path=FOLDER+'/'+name))
    rubric['checks'].append(dict(id='vertiefung-rollen', check_type='human_review', description='Werden Außenhaftung, Zuständigkeitsauskunft, Primärdeckung und Rückdeckung anhand der konkret vorliegenden Unterlagen getrennt?', note='Offene Anwendungsprüfung; kein automatisch festgestelltes Ergebnis.'))
    rubric_path.write_text(yaml.safe_dump(rubric, allow_unicode=True, sort_keys=False))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--qa-dir', type=Path, required=True)
    parser.add_argument('--groups', nargs='*')
    parser.add_argument('--metadata-only', action='store_true')
    parser.add_argument('--render-docx', type=Path)
    args = parser.parse_args()
    selected = cases(args.groups)
    args.qa_dir.mkdir(parents=True, exist_ok=True)
    old_map = {c['slug']: c for c in old_cases()}
    tasks = []
    for case in selected:
        directory = ROOT/'testakten'/case['slug']
        (directory/FOLDER).mkdir(parents=True, exist_ok=True)
        names = native_names(case)
        if len(names) != len(set(names)) or any(Path(n).name != n for n in names):
            raise ValueError('Ungültiger Dokumentbestand')
        if args.metadata_only:
            metadata(case, directory)
            continue
        if not args.render_docx:
            raise ValueError('Kanonischen Word-Renderer angeben')
        for item in case['documents']:
            if item['kind'] == 'email': continue
            path = directory/FOLDER/item['file']
            old.word(case, item, path)
            tasks.append((case, item, path))
        if case['slug'] in old_map:
            for item in old_map[case['slug']]['documents']:
                if item['kind'] != 'letter': continue
                path = directory/'briefvorlagen'/item['file']
                path.parent.mkdir(exist_ok=True)
                old.word(old_map[case['slug']], item, path)
                tasks.append((case, {**item, 'kind': 'template'}, path))
    if tasks:
        env = old.helper.builder.render_helpers.renderer_environment(args.qa_dir, Path(sys.executable).resolve().parents[3])
        def render(task):
            case, item, path = task
            dest = args.qa_dir/'word'/case['slug']/path.parent.name/path.stem
            dest.mkdir(parents=True, exist_ok=True)
            for image in dest.glob('page-*.png'): image.unlink()
            result = subprocess.run([sys.executable, str(args.render_docx), str(path), '--output_dir', str(dest), '--emit_pdf', '--dpi', '100'], env=env, capture_output=True, text=True, timeout=300)
            (dest/'render.log').write_text(result.stdout+result.stderr)
            if result.returncode: raise RuntimeError(str(path)+': '+result.stderr[-1500:])
            pdf = dest/(path.stem+'.pdf')
            images = sorted(dest.glob('page-*.png'))
            if not pdf.exists() or not images or len(images) != len(PdfReader(pdf).pages):
                raise RuntimeError('Renderbestand unvollständig')
            if item['kind'] == 'letter': shutil.copyfile(pdf, path.with_suffix('.pdf'))
            return dict(case=case['slug'], kind=item['kind'], source=str(path), pdf=str(pdf), pages=len(images), images=[str(p) for p in images])
        with ThreadPoolExecutor(max_workers=3) as pool:
            inventory = list(pool.map(render, tasks))
        (args.qa_dir/('word-render-'+('-'.join(args.groups) if args.groups else 'all')+'.json')).write_text(json.dumps(inventory, ensure_ascii=False, indent=2)+'\n')
        for case in selected:
            directory = ROOT/'testakten'/case['slug']
            pending = [d for d in case['documents'] if d['kind'] == 'email']
            while pending:
                unresolved = {FOLDER+'/'+d['file'] for d in pending}
                ready = [d for d in pending if all(n not in unresolved and (directory/n).is_file() for n in case.get('attachments', {}).get(d['file'], []))]
                if not ready: raise ValueError('Fehlende oder zyklische MIME-Anlage: '+case['slug'])
                for item in ready:
                    email(case, item, directory)
                    pending.remove(item)
            for exhibit in case.get('exhibits', []): source(directory, exhibit['source'])
            metadata(case, directory)
    print('Akten:', len(selected), 'Word-Dokumente:', len(tasks), flush=True)

if __name__ == '__main__': main()
