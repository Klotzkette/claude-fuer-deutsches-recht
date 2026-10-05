#!/usr/bin/env python3
"""Erstellt drei kleine native Akten. PDFs werden mit den zentralen Buildern erzeugt."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import yaml
from docx import Document
from docx.shared import Pt

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('kommunal_native_builder', ROOT / 'scripts/build-berlin-bildungsakten.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
from kommunale_haftpflicht_akten_daten import CASES

NOTICE = '> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.\n>\n> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.'

def add_release_bookmarks(writer, testakte_dir):
    """Ergänzt Navigation im kanonisch gesetzten PDF, ohne Seiten neu zu setzen."""
    case=next(c for c in CASES if c['slug']==testakte_dir.name)
    names=sorted([d['file'] for d in case['documents']]+case['xlsx'])
    compact=lambda s:re.sub(r'\s+','',s)
    texts=[compact(p.extract_text() or '') for p in writer.pages]
    for name in names:
        matches=[i for i,text in enumerate(texts) if compact(name) in text]
        if len(matches)!=1:
            raise ValueError(f'Keine eindeutige PDF-Startseite für {name}: {matches}')
        page=matches[0]
        if Path(name).suffix in {'.docx','.xlsx'}:
            page+=1  # Die kanonische Trennseite steht unmittelbar davor.
        if page>=len(writer.pages):raise ValueError('Fehlende Originalseite: '+name)
        writer.add_outline_item(Path(name).stem,page)

def word(item, target):
    builder.word(item, target)
    doc = Document(target)
    doc.core_properties.author = item.get('sender', 'Aktenverwaltung')
    doc.styles['Heading 1'].paragraph_format.space_before = Pt(10)
    doc.styles['Heading 1'].paragraph_format.space_after = Pt(6)
    doc.styles['Normal'].paragraph_format.space_after = Pt(6)
    builder.native.stable_docx(doc, target)

def metadata(case, directory):
    slug=case['slug']
    originals=sorted([d['file'] for d in case['documents']]+case['xlsx'])
    titles={d['file']:d['title'] for d in case['documents']}
    titles.update({n:'Bearbeitbare Übersicht der angemeldeten Beträge mit Quellen und Berechnungen' for n in case['xlsx']})
    core='\n'.join(f'- [{n}]({n})' for n in case['core'])
    rows='\n'.join(f'| [{n}]({n}) | {titles[n]} |' for n in originals)
    text=f'''# 1. {case['title']}

## 1.1. Vorgang und Auftrag

{case['summary']}

Stand: 05.10.2026. Beginnen Sie mit der Auftragsmail. Mandantin ist im Sturzfall die Stadt Hainbogen, beim Rohrbruch die Kommunalversorgung Mainbogen GmbH und im Fahrzeugfall ausschließlich die fiktive Frankenbogen Kommunalversicherung VVaG. Im Fahrzeugfall ist die Stadtbetriebe Steinbogen GmbH Versicherungsnehmerin, keine zusätzliche Mandantin. Erarbeiten Sie aus den Quellen eine erste Einschätzung, gezielte Rückfragen und den angeforderten Antwortentwurf. Behauptungen der Beteiligten bleiben bis zur Prüfung Behauptungen.

Passendes Plugin: [Kommunale Haftpflicht](../../kommunale-haftpflicht/README.md).

## 1.2. Kleiner Einstieg

Für eine kurze Vorführung von etwa zehn bis fünfzehn Minuten im allgemeinen Vortrag zur KI-Rechtsanwendung können zunächst die folgenden sechs Kernunterlagen verwendet werden. Die übrigen Unterlagen ermöglichen anschließend eine vertiefte Bearbeitung. Dies ist eine optionale Demonstration mit Arbeitsmaterial, kein fertiger Vortrag.

{core}

## 1.3. Umfang und Herkunft

Zwölf native Originalunterlagen. Word-Dokumente bleiben bearbeitbar; E-Mails enthalten die bezeichneten Anlagen tatsächlich als MIME-Dateien. Eine eingebettete Anlage und ihre gleichnamige Originaldatei sind derselbe Beleg und werden nicht doppelt als Schaden oder Beweis gezählt. Tabellen enthalten angemeldete Beträge und Rechenwege; sie ersetzen keine Prüfung des Anspruchs.

Das Gesamt-PDF umfasst 18 Seiten. Das Einzel-PDF-ZIP enthält zwölf Unterlagen mit zusammen zwölf Seiten.

<!-- reserved-example-contacts -->

Alle Personen, Institutionen, Unternehmen, Straßenanschriften und Vorgänge sind fiktiv. Die Ortsangabe Würzburg in den beiden dort angesiedelten Akten bezeichnet allein den realen Schauplatz. Keine tatsächliche Stadtverwaltung, kein realer Versorger und kein echter kommunaler Betrieb wird als Verursacher bezeichnet. Kontaktadressen mit `.example` sind nicht zustellbar. Die Aktenstücke enthalten keine Musterlösung.

Die Bezeichnung AKHA in den zwei Würzburger Akten ordnet die Übung einem Bearbeitungsumfeld zu. Die fiktiven Ablagevermerke sind keine Aussage über eine tatsächliche Mitgliedschaft, Zuständigkeit oder Deckung. Es werden keine echten AKHA-Bedingungen und keine Rückdeckungsverträge nachgebildet. Haftung, Deckung beziehungsweise Schadenausgleich und Rückdeckung sind anhand der jeweils fehlenden Vertragsunterlagen getrennt zu bearbeiten. Die Kostenübersichten verwenden keine erfundenen Deckungsquoten oder Rückdeckungsgrenzen.

## 1.4. Unterlagen

| Datei | Inhalt |
| --- | --- |
{rows}

## 1.5. Downloads

{NOTICE}

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF | PDF | [Gesamte Akte](gesamt-pdf/{slug}_gesamt.pdf) |
| Akten-ZIP | ZIP | [Native Originale und Gesamt-PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.0/testakte-{slug}.zip) |
| Einzel-PDF-ZIP | ZIP | [Jedes Aktenstück als PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.0/testakte-{slug}-einzelpdfs.zip) |

Die Archive enthalten die Arbeitsdateien unmittelbar auf der ZIP-Wurzelebene und einen Nutzungshinweis. README und redaktionelle Bewertungsdatei gehören nicht zum Arbeitsdump. Die Verknüpfungen beziehen sich auf den Akten-Begleitrelease zu Version 445.31.0.
'''
    (directory/'README.md').write_text(text,encoding='utf-8')
    specific={
      'kommunale-haftpflicht-personenschaden':[
        ('kontrollzeit','Werden Chatzeit, Sturzzeit und nachträglich erinnerte Reinigungskontrolle mit ihren unterschiedlichen Beweisgrenzen verwendet?'),
        ('personenschaden','Werden Behandlung, Haushaltsleistungen und jede Zahlungsposition anhand ihres konkreten Belegstands geprüft, ohne bleibende Folgen oder unbelegte Kosten zu unterstellen?')],
      'akha-wuerzburg-rohrbruch':[
        ('leitung','Werden Lage der Außenleitung, Anlageninhaber und Wasserweg quellengetreu zugeordnet und offene Gebäudefragen separat behandelt?'),
        ('gewerbeschaden','Werden bezahlte Rechnung, Angebot, gebrauchte Mühlen, telefonische Neupreise und gemeldeter Umsatz getrennt bewertet und passende Nachweise angefordert?')],
      'akha-wuerzburg-betriebsfahrzeug':[
        ('versicherermandat','Wird ausschließlich die Frankenbogen Kommunalversicherung VVaG vertreten, ohne die Versicherungsnehmerin oder Anspruchsteller als weitere Mandanten zu behandeln?'),
        ('mehrere-ansprueche','Werden Gebäudeschaden, vorläufige Geräteansätze und Nachbarumsatz jeweils mit eigenen Haftungsgrundlagen, Nachweisen und Grenzen bearbeitet?'),
        ('grossschaden','Bleiben angemeldete Summe, Geräte-Schätzspanne, gesetzliche Haftungsgrenzen und vertragliche Deckung sowie Rückdeckung unterscheidbar?')]}
    checks=[dict(id='arbeitsbestand',check_type='working_file_count',description='Alle zwölf nativen Unterlagen sind vorhanden.',min=12)]
    for ext in ['docx','eml','txt','xlsx']:
        count=sum(n.endswith('.'+ext) for n in originals)
        if count:checks.append(dict(id='format-'+ext,check_type='file_count',description=f'{count} Originaldateien im Format {ext.upper()} sind vorhanden.',glob='*.'+ext,min=count))
    for i,name in enumerate(['README.md',f'gesamt-pdf/{slug}_gesamt.pdf']+case['core'],1):
        checks.append(dict(id=f'kernbeleg-{i}',check_type='file_exists',description='Die maßgebliche Unterlage oder Lesefassung ist vorhanden.',path=name))
    for key,question in specific[slug]+[('vertragssatz','Werden fehlende Vertragsunterlagen konkret angefordert, bevor Mitgliedschaft, Deckung, Meldeweg oder Rückdeckung behauptet werden?'),('antwort','Liegt ein adressatengerechter Entwurf ohne vorweggenommenes Anerkenntnis oder unbeauftragten Versand vor?')]:
        checks.append(dict(id='fach-'+key,check_type='human_review',description=question,note='Offen: Kriterium für eine spätere Bearbeitung. Die technische Bestandsprüfung bewertet keine juristische Modellausgabe.'))
    rubric=dict(name=case['title'],plugin='kommunale-haftpflicht',stand='2026-10-05',pruefstatus='Technische Bestandsprüfung und redaktionelle Aktenprüfung; eine Ergebnisbewertung erfolgt gesondert.',bewertungsgrundlage=dict(rohakte=slug,hinweis='Diese Bewertungsdatei gehört nicht zu den Arbeitsunterlagen und wird aus Exporten ausgeschlossen.'),checks=checks)
    (directory/'rubric.yaml').write_text(yaml.safe_dump(rubric,allow_unicode=True,sort_keys=False),encoding='utf-8')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--qa-dir',type=Path,required=True)
    p.add_argument('--out-root',type=Path,default=ROOT/'testakten')
    p.add_argument('--xlsx-source',type=Path,required=True)
    p.add_argument('--render-docx',type=Path)
    p.add_argument('--metadata',action='store_true',help='README und redaktionelle Rubrik mit erzeugen')
    args=p.parse_args(); args.qa_dir.mkdir(parents=True,exist_ok=True)
    docxs=[]; inventory=[]
    for case in CASES:
        directory=args.out_root/case['slug'];directory.mkdir(parents=True,exist_ok=True)
        for item in case['documents']:
            target=directory/item['file']
            if target.suffix=='.docx': word(item,target);docxs.append(target)
            elif target.suffix=='.txt': target.write_text(item['title']+'\n'+item['date']+'\n\n'+item['body']+'\n',encoding='utf-8')
        for name in case['xlsx']:
            source=args.xlsx_source/case['slug']/name
            if not source.is_file():raise FileNotFoundError(source)
            if source.resolve()!=(directory/name).resolve():shutil.copyfile(source,directory/name)
        for item in case['documents']:
            if item['file'].endswith('.eml'):builder.mail(item,directory/item['file'],case['attachments'].get(item['file'],[]))
        if args.metadata:metadata(case,directory)
        inventory.append(dict(case=case['slug'],files=sorted([d['file'] for d in case['documents']]+case['xlsx']),attachments=case['attachments'],core=case['core']))
        print(case['slug'],len(inventory[-1]['files']),flush=True)
    (args.qa_dir/'akten-inventar.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
    if args.render_docx:
        runtime=Path(sys.executable).resolve().parents[3]
        env=builder.render_helpers.renderer_environment(args.qa_dir,runtime)
        def render(path):
            dest=args.qa_dir/'word'/path.parent.name/path.stem;dest.mkdir(parents=True,exist_ok=True)
            r=subprocess.run([sys.executable,str(args.render_docx),str(path),'--output_dir',str(dest),'--emit_pdf','--dpi','100'],env=env,capture_output=True,text=True,timeout=300)
            (dest/'render.log').write_text(r.stdout+r.stderr)
            if r.returncode:raise RuntimeError(path.name+': '+r.stderr[-1500:])
            pages=sorted(dest.glob('page-*.png'))
            if not pages:raise RuntimeError('Keine gerenderte Seite: '+str(path))
            return dict(file=str(path),pages=len(pages),images=[str(p) for p in pages])
        with ThreadPoolExecutor(max_workers=3) as pool:result=list(pool.map(render,docxs))
        (args.qa_dir/'word-render.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print('Word-Seiten:',sum(i['pages'] for i in result),flush=True)

if __name__=='__main__':main()
