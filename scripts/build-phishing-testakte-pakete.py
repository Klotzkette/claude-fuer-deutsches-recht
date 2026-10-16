#!/usr/bin/env python3
"""Drei Auslieferungsfassungen der Akte Rabenstein aus denselben Quellen bauen.

Verwendet die zentralen Konverter und Archivregeln. DOCX/PDF werden nativ
übernommen, Excel erhält ausschließlich in der temporären Druckkopie Querformat.
Das Gesamt-PDF besteht in derselben Reihenfolge aus den 28 Einzel-PDFs.
"""
from pathlib import Path
import argparse, hashlib, importlib.util, io, json, shutil, tempfile, zipfile
import xml.etree.ElementTree as ET
from email.parser import BytesParser
from email.policy import default

from pypdf import PdfReader, PdfWriter
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_office_pdf import render_office_batch, normalize_pdf, SHEET_NS

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'phishing-kleinanzeigen-rabenstein-halle'
CASE = ROOT / 'testakten' / SLUG

def module(filename):
    spec=importlib.util.spec_from_file_location(filename.replace('-','_'),ROOT/'scripts'/filename)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result

def sha(data):return hashlib.sha256(data).hexdigest()

def landscape_copy(source,target):
    ns='{'+SHEET_NS+'}'
    with zipfile.ZipFile(source) as original,zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as result:
        for info in original.infolist():
            data=original.read(info)
            if info.filename.startswith('xl/worksheets/') and info.filename.endswith('.xml'):
                sheet=ET.fromstring(data);setup=sheet.find(ns+'pageSetup')
                if setup is None:
                    setup=ET.Element(ns+'pageSetup');sheet.append(setup)
                setup.set('orientation','landscape');setup.set('paperSize','9');setup.set('fitToWidth','1');setup.set('fitToHeight','0')
                # Printed rows need less vertical whitespace than the editing view.
                # Values, formulas, dates and font styles remain untouched.
                for row in sheet.findall(ns+'sheetData/'+ns+'row'):
                    if int(row.get('r','0'))>=6:
                        row.set('ht','36');row.set('customHeight','1')
                data=ET.tostring(sheet,encoding='utf-8',xml_declaration=True)
            result.writestr(info,data)

def build(dist,individual_dir,cache):
    dist.mkdir(parents=True,exist_ok=True);individual_dir.mkdir(parents=True,exist_ok=True)
    individual=module('build-testakten-einzelpdf-zips.py');originals=module('build-testakten-release-zips.py')
    pairs=document_arcname_pairs(CASE);assert len(pairs)==28
    record_path=ROOT/'quality/phishing-vorfall-pruefer/testakte-pruefung.json';record=json.loads(record_path.read_text())
    hashes={x['file']:x['sha256'] for x in record['files']}
    office_cache={};pending=[]
    for source,_ in pairs:
        assert sha(source.read_bytes())==hashes[source.name],f'Quelldatei seit Prüfung geändert: {source.name}'
        if source.suffix=='.docx':
            candidate=cache/source.stem/(source.stem+'.pdf') if cache else None
            review=next(x for x in record['layout_review']['documents'] if x['source']==source.name)
            if candidate and candidate.is_file() and sha(candidate.read_bytes())==review['render_sha256']:
                office_cache[source]=normalize_pdf(candidate.read_bytes(),source.name)
            else:pending.append(source)
    if pending:office_cache.update(render_office_batch(pending))
    with tempfile.TemporaryDirectory(prefix='phishing-print-') as temporary:
        stage=Path(temporary);copies={}
        for source,_ in pairs:
            if source.suffix=='.xlsx':
                copy=stage/source.name;landscape_copy(source,copy);copies[copy]=source
        for copy,data in render_office_batch(list(copies)).items():office_cache[copies[copy]]=data
    for source,_ in pairs:
        if source.suffix in {'.docx','.xlsx'} and source not in office_cache:
            raise RuntimeError(f'Native Office-Konvertierung fehlt: {source.name}')
    writer=PdfWriter();items=[];page_start=1
    zip_path=dist/f'testakte-{SLUG}-einzelpdfs.zip'
    with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as archive:
        individual.write_pdf(archive,NOTICE_FILENAME,NOTICE_BYTES)
        for source,name in pairs:
            data=individual.render_document_pdf(source,CASE,office_cache);assert data and data.startswith(b'%PDF-')
            reader=PdfReader(io.BytesIO(data));pages=len(reader.pages)
            text='\n'.join(p.extract_text() or '' for p in reader.pages)
            assert 'Diese Testakte wurde mit KI generiert' not in text
            assert 'This test case file was generated with AI' not in text
            individual.write_pdf(archive,name,data);(individual_dir/name).write_bytes(data)
            writer.append(io.BytesIO(data),outline_item=source.name)
            items.append({'source':source.name,'pdf':name,'source_sha256':sha(source.read_bytes()),'pdf_sha256':sha(data),'pages':pages,'first_page':page_start,'last_page':page_start+pages-1})
            page_start+=pages
    aggregate=CASE/'gesamt-pdf'/f'{SLUG}_gesamt.pdf';aggregate.parent.mkdir(parents=True,exist_ok=True)
    writer.add_metadata({'/Title':'Kunigunde Rabenstein und die nicht erstattete Zahlung','/Author':'Kanzleiakte','/CreationDate':'D:20261016000000Z','/ModDate':'D:20261016000000Z'})
    writer.write(aggregate);target=dist/aggregate.name;shutil.copyfile(aggregate,target)
    original_path,_=originals.build_single(CASE,dist)
    original_validator=module('validate-testakten-release-zips.py')
    pdf_validator=module('validate-testakten-einzelpdf-zips.py')
    original_validator.assert_same(original_path.name,original_validator.expected_entries(CASE),original_validator.zip_entries(original_path,require_notice=True))
    pdf_validator.assert_same(zip_path.name,[NOTICE_FILENAME,*pdf_validator.expected_arcnames(CASE)],pdf_validator.zip_entries(zip_path,expected_suffix='.pdf'))
    with zipfile.ZipFile(zip_path) as archive:
        assert archive.namelist()[0]=='README.txt' and archive.read('README.txt').startswith(NOTICE_BYTES)
        assert len(archive.namelist())==29 and all('/' not in n for n in archive.namelist())
    with zipfile.ZipFile(original_path) as archive:
        assert archive.namelist()[0]=='README.txt' and archive.read('README.txt').startswith(NOTICE_BYTES)
        assert all('/' not in n for n in archive.namelist())
        for source,_ in pairs:assert archive.read(source.name)==source.read_bytes()
        assert archive.read(aggregate.name)==aggregate.read_bytes()
    combined=PdfReader(aggregate);assert len(combined.pages)==sum(x['pages'] for x in items)
    for item in items:
        single=PdfReader(individual_dir/item['pdf'])
        for offset,page in enumerate(single.pages):
            assert page.extract_text()==combined.pages[item['first_page']-1+offset].extract_text()
    for source,_ in pairs:
        if source.suffix=='.eml':
            mail=BytesParser(policy=default).parsebytes(source.read_bytes())
            for part in mail.iter_attachments():assert part.get_payload(decode=True)==(CASE/part.get_filename()).read_bytes()
    artifacts=[original_path,zip_path,target]
    record['packages']={'date':'2026-10-16','original_sources':len(pairs),'individual_pdfs':len(items),'aggregate_pages':len(combined.pages),'page_map':items,'original_bytes_match':True,'individual_and_aggregate_pages_match':True,'email_attachments_match':True,'archive_notices_valid':True,'pdfs_contain_no_warning':True,'central_single_archive_validators_passed':True,'artifacts':[{'file':p.name,'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in artifacts]}
    record_path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'artifacts':[str(p) for p in artifacts],'sources':len(pairs),'pages':len(combined.pages)},ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--dist',type=Path,required=True);p.add_argument('--individual-dir',type=Path,required=True);p.add_argument('--native-cache',type=Path)
    a=p.parse_args();build(a.dist.resolve(),a.individual_dir.resolve(),a.native_cache.resolve() if a.native_cache else None)
