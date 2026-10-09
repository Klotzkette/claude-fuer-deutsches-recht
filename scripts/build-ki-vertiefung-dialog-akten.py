#!/usr/bin/env python3
"""Zwei native Dialog- und Redaktionsakten, ohne Lösung im Nutzercorpus.

Die XLSX-Dateien erzeugt der gleichnamige MJS-Builder. Dieser Builder verwendet
vorhandene DOCX-, MIME- und Renderhilfen unverändert. Office läuft sequenziell.
"""
from pathlib import Path
import argparse, importlib.util, json, hashlib, os
from email import policy
from email.parser import BytesParser

ROOT=Path(__file__).resolve().parents[1]
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--qa-dir',type=Path,default=Path('/tmp/ki-dialog-akten-qa'))
    ap.add_argument('--skip-render',action='store_true')
    args=ap.parse_args();args.qa_dir.mkdir(parents=True,exist_ok=True)
    h=load('dialog_native_helpers',ROOT/'scripts/build-ki-verordnung-artikel5-testakten.py')
    ren=load('dialog_renderer_helpers',ROOT/'scripts/render-startup-gruender-werkstatt.py')
    env=ren.renderer_environment(args.qa_dir,h.RUNTIME);env['PYTHONPATH']=os.environ.get('PYTHONPATH','')
    cases=json.loads((ROOT/'scripts/data/ki-vertiefung-dialog-akten.json').read_text())
    report=[];attachments=[];manifest=[]
    for c in cases:
        d=ROOT/'testakten'/c['slug'];d.mkdir(parents=True,exist_ok=True)
        for item in c['docs']:
            p=d/item['file'];h.word(item,p)
            if not args.skip_render:
                # Alte Vorschauseiten dürfen einen kürzeren Neusatz nicht überleben.
                preview=args.qa_dir/'word'/d.name/p.stem
                if preview.is_dir():
                    for old_image in preview.glob('page-*.png'):old_image.unlink()
                report.append(h.render((item,p),args.qa_dir,env))
        (d/'14_Projektchat.txt').write_text(c['chat'])
        for message in c['emails']:h.eml(message,d)
        for p in sorted(d.glob('*.eml')):
            message=BytesParser(policy=policy.default).parsebytes(p.read_bytes())
            for a in message.iter_attachments():
                target=d/a.get_filename();raw=a.get_payload(decode=True)
                assert target.is_file() and raw==target.read_bytes(),(p,target)
                attachments.append({'eml':str(p.relative_to(ROOT)),'file':target.name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'byte_identical':True})
        files=sorted(p for p in d.iterdir() if p.is_file() and p.suffix.lower() in ['.docx','.pdf','.eml','.xlsx','.txt'] and p.name!='README.txt')
        assert len(files)==20,(c['slug'],len(files))
        base='https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2'
        warning=h.WARNING
        readme=f"# Testakte {c['title']}\n\n## 1. Auftrag\n\n{c['brief']}\n\nAlle Personen, Organisationen, Anschriften und Vorgänge sind fiktiv. Aktenstand ist der 9. Oktober 2026. E-Mail-Adressen verwenden reservierte .example-Domains.\n\n<!-- reserved-example-contacts -->\n\n## 2. Unterlagen und Bearbeitung\n\nDie Akte enthält sechs Word-Dokumente und deren inhaltsgleiche PDF-Lesefassungen, sechs E-Mails mit echten Anhängen, eine mehrblättrige Arbeitsmappe und einen Chatverlauf. Identische Fassungen und eingebettete Anhänge sind keine unabhängigen Mehrfachbeweise. Die Arbeitsmappe berechnet nachvollziehbare Größen und hält fehlende Daten von Nullwerten getrennt. Sie trifft keine rechtliche Entscheidung.\n\nLesen Sie zuerst den Auftrag. Verarbeiten Sie danach die widersprüchlichen Belege und führen Sie den ausformulierten Arbeitsentwurf zum bestellten Produkt fort. Noch fehlende Tatsachen gezielt benennen; vorhandene Angaben nicht erneut vollständig erheben. Die Akte enthält keine rechtliche Musterlösung.\n\n## 3. Downloads\n\n{warning}\n\n| Fassung | Download |\n|---|---|\n| Originalformate | [Akten-ZIP]({base}/testakte-{c['slug']}.zip) |\n| Einzelne Lesefassungen | [Einzel-PDF-ZIP]({base}/testakte-{c['slug']}-einzelpdfs.zip) |\n| Gesamte Akte | [Gesamt-PDF]({base}/{c['slug']}_gesamt.pdf) |\n\n## 4. Einzeldateien\n\n{warning}\n\n| Datei | Format |\n|---|---|\n"+'\n'.join(f'| [{p.name}]({p.name}) | {p.suffix[1:].upper()} |' for p in files)+'\n'
        (d/'README.md').write_text(readme)
        manifest.append({'slug':c['slug'],'title':c['title'],'file_count':len(files),'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]})
    q=ROOT/'quality/ki-verordnung-2026-10-09-vertiefung';q.mkdir(parents=True,exist_ok=True)
    if not args.skip_render:
        (args.qa_dir/'word-render.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    (q/'dialog-akten-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    (q/'dialog-akten-anhaenge.json').write_text(json.dumps(attachments,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(cases)} Akten, {sum(x["file_count"] for x in manifest)} Dateien, {len(attachments)} bytegleiche Anhänge')

if __name__=='__main__':main()
