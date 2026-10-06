#!/usr/bin/env python3
"""Baut zwei verbundene, native Bauvergabeakten; fremde Akten bleiben unberührt."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import csv
from datetime import date, datetime
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import format_datetime, formataddr
import hashlib
import importlib.util
import json
import mimetypes
from pathlib import Path
import shutil
import subprocess
import sys
from pypdf import PdfReader
from bauvergabe_falldaten import CASES, LV, STAGES, PLUGINS, total, money
from bauvergabe_aktentexte import documents, de
from testakte_disclaimer import NOTICE_MARKDOWN

ROOT=Path(__file__).resolve().parents[1]
def module(name,filename):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/filename)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
word_builder=module('bau_native','build-berlin-bildungsakten.py')

def safe(directory,name):
    p=directory/name
    if not p.resolve().is_relative_to(directory.resolve()) or p.is_symlink():
        raise ValueError('Unsicherer Aktenpfad: '+name)
    return p

def mail(c,item,directory):
    message=EmailMessage(policy=SMTP)
    message['From']=item['sender'];message['To']=item['recipient']
    message['Subject']=item['title'];message['Date']=format_datetime(datetime.fromisoformat(item['date']))
    identity=hashlib.sha256((c['slug']+item['file']).encode()).hexdigest()[:32]
    message['Message-ID']=f'<{identity}@bauvergabe.example>'
    message.set_content(item['body'],charset='utf-8')
    for name in item.get('attachments',[]):
        p=safe(directory,name)
        if not p.is_file():raise ValueError('Fehlende echte MIME-Anlage: '+name)
        major,minor=(mimetypes.guess_type(p.name)[0] or 'application/octet-stream').split('/',1)
        message.add_attachment(p.read_bytes(),maintype=major,subtype=minor,filename=p.name)
    if message.is_multipart():message.set_boundary('bau-'+identity)
    safe(directory,item['file']).write_bytes(message.as_bytes())

def csvfile(path,header,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8-sig',newline='') as out:
        writer=csv.writer(out,delimiter=';');writer.writerow(header);writer.writerows(rows)

def metadata(c,directory):
    files=sorted(p for p in directory.rglob('*') if p.is_file() and p.suffix in {'.docx','.eml','.pdf','.xlsx','.csv','.txt'} and 'gesamt-pdf' not in p.parts)
    pdf=directory/'gesamt-pdf'/f"{c['slug']}_gesamt.pdf"
    pages=f'Das Gesamt-PDF umfasst {len(PdfReader(pdf).pages)} Seiten.' if pdf.exists() else ''
    stages=[]
    for (stage,label),plugin in zip(STAGES.items(),PLUGINS):
        stages.append(f'| [{stage}]({stage}/) | {label} | [{plugin}](../../bauvergabe/{plugin}/README.md) |')
    text=f'''<!-- decimal-headings -->

# 1. {c['title']}

## 1.1. Ein Bauvorhaben, fünf Arbeitsstationen

{c['owner']} bereitet {c['lot']} innerhalb eines Vorhabens mit {money(c['project_net'])} EUR geschätztem Gesamtbauwert ohne Umsatzsteuer vor. Die Akte beginnt mit einem noch nicht ausschreibungsreifen Planungsstand. Danach folgen Berichtigung, Angebot, Wertung, Rechtsschutz, Zuschlag, Ausführung und Nachtrag. Derselbe Vertrag und dieselben Beteiligten bleiben durchgehend erhalten. Die Stufen Bieterarbeit und Verfahrensführung überschneiden sich zeitlich; ihre Nummern kennzeichnen die Perspektiven und keine voneinander getrennten Bauprojekte.

| Aktenordner | Arbeitsauftrag | Passendes Plugin |
| --- | --- | --- |
{chr(10).join(stages)}

[Zur gesamten Bauvergabe-Reihe](../../bauvergabe/README.md).

## 1.2. Rollen und zeitlich begrenzter Einstieg

Für die Unterlagenerstellung zunächst nur `01-vergabeunterlagen` verwenden. Für die Vergabestelle kommen `02-vergabeverfahren` und die ihr tatsächlich übermittelten Bieterunterlagen hinzu. Als Bieter ausschließlich den veröffentlichten Leistungsstand, die allgemein bekannt gegebenen Berichtigungen und `03-bieterarbeit` verwenden; vertrauliche Konkurrenzangebote und interne Wertungsunterlagen gehören nicht in diesen Arbeitskontext. Im Rechtsschutz ist Mandantin {c['rival']}; `04-rechtsschutz` bezeichnet den Informationsstand ihrer Kanzlei. Im Nachtragsmanagement ist Mandantin grundsätzlich {c['winner']}; die Auftraggeberantwort bleibt Gegenposition, kein weiteres Mandat.

Ein vollständiger Aktenordner enthält mehr Informationen als eine Partei in jeder einzelnen Phase kennen durfte. Deshalb die späteren Unterlagen nicht schon bei der ersten Übung laden. Im Gesamt-PDF helfen die Dokumentbezeichnungen und Lesezeichen bei der gezielten Auswahl. Die spätere Abhilfe ist keine Musterlösung für eine frühere, noch offene Bewertung. Die Entwürfe und Bearbeitungsvermerke dürfen fachliche Fehler, Beleglücken und streitige Behauptungen enthalten; sie sind zu prüfen und nicht als richtige Lösung zu übernehmen.

## 1.3. Umfang und Grenzen

Die Akte enthält **{len(files)} native Dateien**, darunter bearbeitbare Word-Dokumente, Briefe zusätzlich als PDF, echte E-Mails mit bezeichneten MIME-Anlagen, Rechentabellen und CSV-Listen. {pages} Ein Brief in Word und PDF sowie seine E-Mail-Anlage bleiben ein und derselbe Vorgang. Sie sind keine drei verschiedenen Beweise. Die ZIPs bewahren auf Wunsch der zusammenhängenden Projektstruktur die fünf Stufenordner; beide enthalten zusätzlich die vorgeschriebene `README.txt` an ihrer Wurzel.

Die technische Leistungsbeschreibung bildet einen begrenzten Rohbauausschnitt als Arbeitsakte ab. Sie ist keine geprüfte Ausführungsplanung für ein echtes Gebäude. Fehlende Statik, Ausführungsdetails, Behördenentscheidungen und Portalnachweise werden nicht als vorhanden behauptet. CSV und XLSX sind keine validierten GAEB-Dateien. Die Rechtsschutzakte enthält Kanzleientwürfe und Aktennotizen, keine nachgebildeten gerichtlichen Entscheidungen oder echt wirkenden Zugangssiegel.

## 1.4. Herkunft und Rechtsstand

<!-- reserved-example-contacts -->

Alle Gesellschaften, Personen, Anschriften, Vergabeverfahren, Preise und Geschäftsvorgänge sind fiktiv. Münster und Bielefeld sind reale Schauplätze; die Akte behauptet keine tatsächliche kommunale Beschaffung. Kontakte mit `.example` sind nicht zustellbar. Rechtsstand ist der **06.10.2026**. Die Unterlagen ab dem späteren Oktober 2026 bis zur Ausführung 2027 sind ausdrücklich eine fiktive Fortsetzung auf diesem eingefrorenen Rechtsstand. Vor einer realen Verwendung sind die dann geltenden Normen, Schwellenwerte, Landesregeln und Übergangsvorschriften erneut zu prüfen.

## 1.5. Downloads

{NOTICE_MARKDOWN}

| Format | Download |
| --- | --- |
| Gesamt-PDF | [Gesamte Akte](gesamt-pdf/{c['slug']}_gesamt.pdf) |
| Originaldateien | [Projektakte als ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.32.0/testakte-{c['slug']}.zip) |
| Einzel-PDFs | [Alle Unterlagen als einzelne PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.32.0/testakte-{c['slug']}-einzelpdfs.zip) |
'''
    (directory/'README.md').write_text(text)
    checks=[dict(id=f'original-{i+1}',check_type='file_exists',description='Die benannte Arbeitsunterlage ist vorhanden.',path=p.relative_to(directory).as_posix()) for i,p in enumerate(files)]
    checks.append(dict(id='gesamt-pdf',check_type='file_exists',description='Die durchgehende Lesefassung liegt vor.',path=f"gesamt-pdf/{c['slug']}_gesamt.pdf"))
    # JSON ist eine Teilmenge von YAML und vermeidet eine Schreibabhängigkeit
    # vom bewusst kleinen YAML-Lesemodul des Repositorys.
    (directory/'rubric.yaml').write_text(json.dumps(dict(id=c['slug'],name=c['title'],title=c['title'],plugin=PLUGINS[0],checks=checks),ensure_ascii=False,indent=2)+'\n')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--qa-dir',type=Path,required=True)
    parser.add_argument('--render-docx',type=Path)
    parser.add_argument('--metadata-only',action='store_true')
    args=parser.parse_args();args.qa_dir.mkdir(parents=True,exist_ok=True)
    if args.metadata_only:
        for c in CASES:metadata(c,ROOT/'testakten'/c['slug'])
        return
    if not args.render_docx:raise ValueError('Kanonischer Word-Renderer erforderlich')
    tasks=[]
    for c in CASES:
        directory=ROOT/'testakten'/c['slug'];directory.mkdir(parents=True,exist_ok=True)
        for stage in STAGES:(directory/stage).mkdir(exist_ok=True)
        for item in documents(c):
            target=safe(directory,item['file'])
            if target.suffix=='.docx':
                word_builder.word(item,target);tasks.append((c,item,target))
        csvfile(directory/'01-vergabeunterlagen/07_Mengen_Preisblatt.csv',['OZ','Kurztext','Einheit','Menge','Einheitspreis_netto_EUR'],[[pos,title,unit,q,''] for (pos,title,unit),q in zip(LV,c['quantities'])])
        csvfile(directory/'02-vergabeverfahren/04_Angebotseingang.csv',['Kennung','Unternehmen','Angebot_netto_EUR','Eingang','Fassung','Status'],[
            ['A1',c['winner'],money(total(c)),c['deadline']+' 09:42:18','A2','endgültig abgegeben'],
            ['A2',c['rival'],money(total(c,c['rival_multiplier'])),c['deadline']+' 09:51:04','A1','endgültig abgegeben'],
            ['A3','Hugo Zement & Partner GmbH',money(total(c,c['third_multiplier'])),c['deadline']+' 08:55:31','A1','endgültig abgegeben'],
            ['A1-alt',c['winner'],'',c['deadline']+' 09:21:10','A1','zurückgezogen; kein viertes Angebot']])
        if c['short']=='Klinik':rows=[['N01-1','Beton','m3',220,268],['N01-2','Betonstahl','kg',34000,2.52],['N01-3','Schalung','m2',920,78]]
        else:rows=[['N01-1','Mauerwerk','m2',140,186],['N01-2','Beton','m3',44,257],['N01-3','Betonstahl','kg',8000,2.48]]
        csvfile(directory/'05-nachtragsmanagement/04_Aufmass_N01.csv',['Position','Leistung','Einheit','Zusatzmenge','beanspruchter_Kostensatz_netto_EUR'],rows)
    env=word_builder.render_helpers.renderer_environment(args.qa_dir,Path(sys.executable).resolve().parents[3])
    def render(task):
        c,item,path=task;out=args.qa_dir/'word'/c['slug']/path.parent.name/path.stem;out.mkdir(parents=True,exist_ok=True)
        for image in out.glob('page-*.png'):image.unlink()
        run=subprocess.run([sys.executable,str(args.render_docx),str(path),'--output_dir',str(out),'--emit_pdf','--dpi','100'],env=env,capture_output=True,text=True,timeout=300)
        (out/'render.log').write_text(run.stdout+run.stderr)
        if run.returncode:raise RuntimeError(f'{path}: {run.stderr[-1500:]}')
        pdf=out/(path.stem+'.pdf');pages=sorted(out.glob('page-*.png'))
        if not pdf.exists() or len(pages)!=len(PdfReader(pdf).pages):raise ValueError('Unvollständiges Rendering')
        if item['pdf']:shutil.copyfile(pdf,path.with_suffix('.pdf'))
        return dict(source=path.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),pdf=str(pdf),pages=[str(p) for p in pages])
    with ThreadPoolExecutor(max_workers=2) as pool:rendered=list(pool.map(render,tasks))
    for c in CASES:
        directory=ROOT/'testakten'/c['slug']
        for item in documents(c):
            if item['file'].endswith('.eml'):mail(c,item,directory)
        metadata(c,directory)
    (args.qa_dir/'word-render-manifest.json').write_text(json.dumps(rendered,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(rendered)} Word-Dateien gerendert; Sichtprüfung steht gesondert an.',flush=True)
if __name__=='__main__':main()
