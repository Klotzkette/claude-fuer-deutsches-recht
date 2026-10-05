#!/usr/bin/env python3
"""Baut nur die native Geburtsschadenakte; die vorhandenen drei Akten bleiben unverändert."""
import argparse,importlib.util,json,shutil,subprocess,sys,re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import yaml
from geburtsschaden_akte_daten import SLUG,TITLE,CORE,XLSX,DOCS,ATTACHMENTS
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('kommunal_native_builder',ROOT/'scripts/build-kommunale-haftpflicht-akten.py');helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)

def add_release_bookmarks(writer,testakte_dir):
    compact=lambda s:re.sub(r'\s+','',s)
    texts=[compact(p.extract_text() or '') for p in writer.pages]
    for name in sorted([d['file'] for d in DOCS]+[XLSX]):
        hits=[i for i,t in enumerate(texts) if compact(name) in t]
        if len(hits)!=1:raise ValueError(f'Keine eindeutige PDF-Startseite: {name}: {hits}')
        page=hits[0]+(1 if Path(name).suffix in {'.docx','.xlsx'} else 0)
        writer.add_outline_item(Path(name).stem,page)

def metadata(directory):
    names=sorted([d['file'] for d in DOCS]+[XLSX]); titles={d['file']:d['title'] for d in DOCS};titles[XLSX]='Vergleich, ausgeführte Zahlungen, interne Schichten und Bedarfsansatz'
    rows='\n'.join(f'| [{n}]({n}) | {titles[n]} |' for n in names)
    core='\n'.join(f'- [{n}]({n})' for n in CORE)
    (directory/'README.md').write_text(f'''<!-- decimal-headings -->

# 1. {TITLE}

## 1.1. Vorgang und Auftrag

Nora Winter erlitt bei ihrer Geburt 2016 in einer kommunal getragenen Krankenhaus-GmbH eine schwere Schädigung. Die Haftung ist anerkannt. Die Frankenbogen Kommunalversicherung VVaG hat nach einem Teilvergleich insgesamt 13,20 Mio. EUR an Nora ausgezahlt: Schmerzensgeld, vergangenen und künftigen Mehrbedarf, Wohnanpassung und künftigen Erwerbsschaden. Die vier früheren Vorschüsse von zusammen 1,20 Mio. EUR sind darin enthalten. Eine gesonderte Reserve und interne Ausgleichs- und Rückdeckungsbeträge bilden andere Größen.

Stand: 05.10.2026. Mandantin ist ausschließlich die fiktive Frankenbogen Kommunalversicherung VVaG. Rechtsanwältin Clara Klee soll die Abrechnung und die offenen Nachweise prüfen und einen internen Antwortentwurf erstellen. Die Klinik sowie Nora und ihre Eltern sind keine weiteren Mandanten. Die Familie kommuniziert über ihren Anwalt mit dem Erstversicherer und hat keinen Kontakt zur AKHA oder zur Rückversicherung.

Passendes Plugin: [Kommunale Haftpflicht](../../kommunale-haftpflicht/README.md).

## 1.2. Kleiner Einstieg

Für die optionale Vorführung im allgemeinen Vortrag zur KI-Rechtsanwendung beginnen Sie mit sechs Kernunterlagen. Die übrigen Quellen vertiefen den Belegabgleich; ein fertiger Vortrag oder eine Musterlösung ist nicht Bestandteil der Akte.

{core}

## 1.3. Umfang und Herkunft

Das Gesamt-PDF umfasst 35 Seiten. Das Einzel-PDF-ZIP enthält achtzehn Unterlagen mit zusammen 22 Seiten.

Achtzehn native Originalunterlagen: zwölf bearbeitbare Word-Dokumente, fünf E-Mail-Dateien und eine Excel-Arbeitsmappe mit vier Tabellenblättern und Arbeitsformeln. Bezeichnete E-Mail-Anlagen sind als identische MIME-Dateien eingebettet. Anlage und gesonderte Datei bezeichnen denselben Beleg und dürfen nicht doppelt berücksichtigt werden.

<!-- reserved-example-contacts -->

Alle Personen, Unternehmen, Kliniken, Stiftungen, kommunalen Beteiligungen, Adressen und Vorgänge sind fiktiv. Würzburg bezeichnet den realen Schauplatz; kein tatsächliches Würzburger Krankenhaus oder tatsächlicher kommunaler Träger wird als Verursacher bezeichnet. Die erfundene Stadt Hainbogen hält im Fall 60 Prozent der Klinik Mainblick GmbH, die ebenfalls erfundene Stiftung Morgenlicht 40 Prozent. Kontaktadressen mit `.example` sind nicht zustellbar.

AKHA ist eine reale Bezeichnung. Der Fall behauptet keine reale Mitgliedschaft und keine realen Vertragsbedingungen. Die interne Modellvereinbarung und das Tabellenblatt „Ausgleichsmodell“ verwenden ausdrücklich erfundene Annahmen: Mitgliedsselbstbehalt 1,50 Mio. EUR; Rückversicherungspriorität 10,00 Mio. EUR auf den ursprünglichen Gesamtschaden; darüber ein Limit von weiteren 10,00 Mio. EUR. Es handelt sich weder um veröffentlichte AKHA-Konditionen noch um einen tatsächlichen Vertrag. Die kommunale Beteiligung und eine Einbeziehung in ein konkretes Ausgleichs- oder Rückdeckungsverhältnis sind eigenständig zu prüfen. Die geschilderten Buchungen gelten ausschließlich innerhalb dieser fiktiven Modellakte.

Auch Vergleich, klinische Befunde, Pflegeangebot und Erwerbsannahmen sind erfunden. Die Kapitalbeträge sind verhandelte Beträge und keine medizinisch gesicherte Lebenszeitprognose. Der außergerichtliche Vergleich enthält einen Vorbehalt für unvorhersehbare weitere Schäden. Eine familiengerichtliche Genehmigung wird nicht erfunden.

## 1.4. Unterlagen

| Datei | Inhalt |
| --- | --- |
{rows}

## 1.5. Downloads

{helper.NOTICE}

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF | PDF | [Gesamte Akte](gesamt-pdf/{SLUG}_gesamt.pdf) |
| Akten-ZIP | ZIP | [Native Originale und Gesamt-PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-{SLUG}.zip) |
| Einzel-PDF-ZIP | ZIP | [Jedes Aktenstück als PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.31.1/testakte-{SLUG}-einzelpdfs.zip) |

Die Archive sind flach. Ihre README.txt enthält den Herkunfts- und Risikohinweis; die PDFs enthalten keine Hinweisseite. Die redaktionelle Bewertungsdatei wird nicht als Arbeitsunterlage exportiert.
''',encoding='utf-8')
    checks=[dict(id='arbeitsbestand',check_type='working_file_count',description='Alle achtzehn nativen Originalunterlagen sind vorhanden.',min=18)]
    for ext,count in [('docx',12),('eml',5),('xlsx',1)]:checks.append(dict(id='format-'+ext,check_type='file_count',description=f'{count} native {ext.upper()}-Unterlagen sind vorhanden.',glob='*.'+ext,min=count))
    for i,name in enumerate(CORE):checks.append(dict(id=f'kernbeleg-{i+1}',check_type='file_exists',description='Kernunterlage vorhanden.',path=name))
    for key,desc in [('mandat','Wird allein der Erstversicherer vertreten und der bereits anerkannte Haftungsstand berücksichtigt?'),('zahlung','Werden Vergleich, Vorschüsse, Schlusszahlung und noch nicht gezahlte Reserve ohne Doppelzählung abgeglichen?'),('schichten','Werden erstversicherte Leistung, Mitgliedsselbstbehalt, Bruttoausgleich und Rückdeckung mit ihrem jeweiligen Bezugsbetrag und Zahlungsempfänger getrennt?'),('quellen','Werden Modellparameter als Annahmen erkannt und keine tatsächlichen AKHA-Konditionen oder Mitgliedschaften behauptet?'),('zukunft','Werden Erwerbsprognose, Vorbehalt, Vertretung und Verjährungsregelung anhand der konkreten Unterlagen geprüft?'),('entwurf','Liegt ein adressatengerechter interner Antwortentwurf mit konkretem nächsten Schritt vor?')]:checks.append(dict(id='fach-'+key,check_type='human_review',description=desc,note='Offen: Kriterium für eine spätere juristische Bearbeitung; keine Musterlösung.'))
    (directory/'rubric.yaml').write_text(yaml.safe_dump(dict(name=TITLE,plugin='kommunale-haftpflicht',stand='2026-10-05',checks=checks),allow_unicode=True,sort_keys=False),encoding='utf-8')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--qa-dir',type=Path,required=True);p.add_argument('--xlsx-source',type=Path,required=True);p.add_argument('--out-root',type=Path,default=ROOT/'testakten');p.add_argument('--render-docx',type=Path);args=p.parse_args()
    directory=args.out_root/SLUG;directory.mkdir(parents=True,exist_ok=True);args.qa_dir.mkdir(parents=True,exist_ok=True)
    source=args.xlsx_source/XLSX
    if source.resolve()!=(directory/XLSX).resolve():shutil.copyfile(source,directory/XLSX)
    docs=[]
    for item in DOCS:
        if item['file'].endswith('.docx'):helper.word(item,directory/item['file']);docs.append(directory/item['file'])
    for item in DOCS:
        if item['file'].endswith('.eml'):helper.builder.mail(item,directory/item['file'],ATTACHMENTS.get(item['file'],[]))
    metadata(directory)
    (args.qa_dir/'akten-inventar.json').write_text(json.dumps(dict(case=SLUG,files=sorted([d['file'] for d in DOCS]+[XLSX]),core=CORE,attachments=ATTACHMENTS),ensure_ascii=False,indent=2)+'\n')
    if args.render_docx:
        env=helper.builder.render_helpers.renderer_environment(args.qa_dir,Path(sys.executable).resolve().parents[3])
        def render(path):
            dest=args.qa_dir/'word'/path.stem;dest.mkdir(parents=True,exist_ok=True)
            r=subprocess.run([sys.executable,str(args.render_docx),str(path),'--output_dir',str(dest),'--emit_pdf','--dpi','100'],env=env,capture_output=True,text=True,timeout=300);(dest/'render.log').write_text(r.stdout+r.stderr)
            if r.returncode:raise RuntimeError(path.name+': '+r.stderr[-1500:])
            images=sorted(dest.glob('page-*.png'))
            if not images:raise RuntimeError('Keine gerenderte Seite '+path.name)
            return dict(file=str(path),pages=len(images),images=[str(p) for p in images])
        with ThreadPoolExecutor(max_workers=3) as pool:result=list(pool.map(render,docs))
        (args.qa_dir/'word-render.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print('Word-Seiten',sum(d['pages'] for d in result))
    print(SLUG,'18 Originale')
if __name__=='__main__':main()
