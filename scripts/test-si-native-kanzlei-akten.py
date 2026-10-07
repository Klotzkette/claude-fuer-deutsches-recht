#!/usr/bin/env python3
"""Prüft die 24 kurzen Arbeitsakten ohne Neugenerierung oder Änderung von Dateien."""
from pathlib import Path
from collections import Counter
from email.parser import BytesParser
from email.policy import default
from email.utils import getaddresses, parsedate_to_datetime
from docx import Document
from pypdf import PdfReader
import hashlib, json, re

ROOT=Path(__file__).resolve().parents[1]

def normalized(value):
    return re.sub(r'\s+', '', value)

def main():
    cases=json.loads((ROOT/'scripts/si-native-kanzlei-faelle.json').read_text())
    assert len(cases)==24
    assert len({c['slug'] for c in cases})==24
    assert len({c['fachgebiet'] for c in cases})==24
    manifest=json.loads((ROOT/'quality/si-native-kanzlei/testakten-originale.json').read_text())
    assert len(manifest)==216
    records={(r['case'],r['name']):r for r in manifest}
    ids=set();totals=Counter()
    for c in cases:
        folder=ROOT/'testakten'/c['slug']
        files=[p for p in folder.iterdir() if p.is_file() and p.suffix in ('.eml','.pdf','.docx','.xlsx')]
        assert Counter(p.suffix for p in files)=={'.eml':4,'.pdf':3,'.docx':2,'.xlsx':1},c['slug']
        totals.update(p.suffix for p in files)
        for f in files:
            if f.suffix!='.xlsx':
                assert hashlib.sha256(f.read_bytes()).hexdigest()==records[(c['slug'],f.name)]['sha256'],f
            if f.suffix=='.pdf':
                pdf=PdfReader(f)
                assert len(pdf.pages)==1,f
                box=pdf.pages[0].mediabox
                assert abs(float(box.width)-595.28)<1 and abs(float(box.height)-841.89)<1,f
                text=pdf.pages[0].extract_text()
                assert 'Diese Testakte wurde mit KI generiert' not in text
                assert 'This test case file was generated' not in text
            if f.suffix=='.docx':
                doc=Document(f)
                assert doc.styles['Normal'].font.name=='Times New Roman',f
                assert doc.styles['Normal'].font.size.pt==11,f
                assert doc.core_properties.author=='Klotzkette',f
                if f.name.startswith('09_'):
                    text='\n'.join(p.text for p in doc.paragraphs)
                    assert normalized(c['draft']) in normalized(text),f
                    assert all(blank in text for blank in c['draft_blanks']),f
            if f.suffix=='.eml':
                msg=BytesParser(policy=default).parsebytes(f.read_bytes())
                assert not msg.defects,f
                assert all(msg.get(k) for k in ('From','To','Subject','Date','Message-ID')),f
                assert parsedate_to_datetime(msg['Date']).tzinfo,f
                mid=str(msg['Message-ID']);assert mid not in ids,f;ids.add(mid)
                for key in ('From','To'):
                    addresses=getaddresses([str(msg[key])])
                    assert len(addresses)==1,(f,key,addresses)
                    assert addresses[0][1].rsplit('@',1)[-1].endswith('.example'),(f,key,addresses)
                body=msg.get_body(preferencelist=('plain',))
                assert body is not None and '\ufffd' not in body.get_content(),f
                if f.name.startswith('01_'):assert normalized(c['opening']) in normalized(body.get_content()),f
                if f.name.startswith('03_'):assert normalized(c['response']) in normalized(body.get_content()),f
                if f.name.startswith('04_'):
                    text=body.get_content()
                    assert c['case_id'] in text
                    for row in c['times'][:2]:
                        assert str(row['minutes'])+' Minuten' in text
                        assert row['narrative'] in text
                    assert 'keinen geschätzten Betrag buchen' in text
        assert c['times'][2]['minutes'] is None
        assert c['times'][2]['confirmed'] is False
        assert c['times'][3]['billable'] is False
        assert c['times'][3]['confirmed'] is False
    print(json.dumps({'cases':len(cases),'originals':sum(totals.values()),'formats':dict(totals),'unique_mail_ids':len(ids),'passed':True},ensure_ascii=False))

if __name__=='__main__':
    main()
