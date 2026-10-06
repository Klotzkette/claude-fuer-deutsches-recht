#!/usr/bin/env python3
"""Vergleicht ursprüngliche native PDF-Seiten pixelweise mit dem Ausgangsstand."""
from pathlib import Path
import hashlib
import json
import subprocess
import pypdfium2 as pdfium
from pypdf import PdfReader
from PIL import ImageChops

ROOT=Path(__file__).resolve().parents[1]
SLUG='bauwirtschaft-vergabeverfahren-feuerwehrhaus-northeim'
QA=Path('/tmp/bauwirtschaft-vertiefung-20261006/northeim')
path=f'testakten/{SLUG}/gesamt-pdf/{SLUG}_gesamt.pdf'
old=QA/'vorher-gesamt.pdf'
old.write_bytes(subprocess.check_output(['git','show',f'b2f0298220c9f82557206da9e5d3d086217d7467:{path}'],cwd=ROOT))
oldreader=PdfReader(old);texts=[p.extract_text() or ''for p in oldreader.pages]
oldnative=pdfium.PdfDocument(str(old));newnative=pdfium.PdfDocument(str(ROOT/path))
manifest=json.loads((QA/'manifest.json').read_text());results=[]
for item in manifest:
    if int(item['file'][:2])>32:continue
    extension=Path(item['file']).suffix
    start=next((i+1 for i,t in enumerate(texts)if item['file']in t and t.startswith(('EXCEL-TABELLE','WORD-DOKUMENT','PDF-ANHANG'))),None)
    for local in range(item['pages']):
        n=item['start']-1+local;current=newnative[n].render(scale=1.5).to_pil().convert('RGB')
        same=False
        if start is not None:
            previous=oldnative[start+local].render(scale=1.5).to_pil().convert('RGB')
            same=current.size==previous.size and ImageChops.difference(current,previous).getbbox() is None
        if not same:
            folder=QA/'changed-original-pages';folder.mkdir(exist_ok=True)
            current.save(folder/f'{Path(item["file"]).stem}-{local+1}.png')
        results.append({'file':item['file'],'page':local+1,'pixelgleich':same,'native':start is not None})
(QA/'seitenvergleich.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print(json.dumps({'originalseiten':len(results),'pixelgleich':sum(x['pixelgleich']for x in results),'gesondert_sichten':sum(not x['pixelgleich']for x in results)},ensure_ascii=False))
