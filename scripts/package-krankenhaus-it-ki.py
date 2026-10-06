"""Reproduzierbarer Komponentenbuild ohne Änderung alter Sammelarchive."""
from pathlib import Path
import importlib.util,json,os,zipfile,hashlib,shutil
from pypdf import PdfReader
from prompt_profiles import PROMPT_SUFFIXES
ROOT=Path(__file__).resolve().parents[1]
SLUG='krankenhaus-it-ki-auenhoehe-thueringen';PLUGIN='krankenhaus-it-ki'
CASE=ROOT/'testakten'/SLUG;QA=Path(os.environ.get('KLINIK_QA_ROOT','/tmp/krankenhaus-it-ki-20261006'))
DIST=QA/'dist'
def module(name):
    sp=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def main():
    assert 'codex-primary-runtime/dependencies/bin/override/soffice' in os.environ['SOFFICE']
    DIST.mkdir(parents=True,exist_ok=True)
    g=module('build-testakte-gesamt-pdf');e=module('build-testakten-einzelpdf-zips');z=module('build-testakten-release-zips')
    status,info=g.build_gesamt_pdf(CASE);assert status=='ok',info;print(info,flush=True)
    out,n=e.build_single(CASE,DIST);assert n==40,n
    native,total=z.build_single(CASE,DIST);assert total==42,total
    # Validate the two individual archives with the central validators. This
    # component build intentionally does not create or claim to check all-case ZIPs.
    nv=module('validate-testakten-release-zips');pv=module('validate-testakten-einzelpdf-zips')
    nv.assert_same(native.name,nv.expected_entries(CASE),nv.zip_entries(native,require_notice=True))
    pv.assert_same(out.name,[pv.NOTICE_FILENAME,*pv.expected_arcnames(CASE)],pv.zip_entries(out,expected_suffix='.pdf'))
    original_paths=[p for p in CASE.iterdir() if p.is_file() and p.suffix in ('.docx','.eml','.pdf','.xlsx')]
    assert len(original_paths)==40
    with zipfile.ZipFile(native) as archive:
        for source in original_paths:
            assert archive.read(source.name)==source.read_bytes(),source.name
    pdf=CASE/'gesamt-pdf'/f'{SLUG}_gesamt.pdf';shutil.copyfile(pdf,DIST/pdf.name)
    plugin=ROOT/PLUGIN;zip_path=DIST/f'{PLUGIN}.zip'
    with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as archive:
        for source in sorted(plugin.rglob('*')):
            if not source.is_file() or source.name.endswith(PROMPT_SUFFIXES) or source.name in ('CLAUDE.md','.DS_Store') or '__pycache__' in source.parts:continue
            z.write_file(archive,source,source.relative_to(plugin).as_posix())
    module('validate-release-zips').validate_plugin_zip(DIST,PLUGIN,'445.33.1')
    module('validate-release-zips').validate_focus_skill(zip_path,plugin,ROOT/'quality/evals'/f'{PLUGIN}.json')
    singles=QA/'einzel-pdf';singles.mkdir(exist_ok=True)
    rows=[]
    with zipfile.ZipFile(out) as archive:
        for name in archive.namelist():
            if name.endswith('.pdf'):
                target=singles/name;target.write_bytes(archive.read(name));rows.append({'file':name,'pages':len(PdfReader(target).pages),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
    checksums={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(DIST.iterdir()) if p.suffix in ('.zip','.pdf')}
    (DIST/'checksums-sha256.txt').write_text(''.join(f'{value}  {name}\n' for name,value in checksums.items()))
    report={'originals':40,'individual_pdfs':rows,'gesamt_pages':len(PdfReader(pdf).pages),'release_assets':checksums,'archive_validation':'Zentrale Einzelarchiv-Validatoren bestanden; alle 40 Originale bytegleich. Keine Sammelarchive geprüft.','note':'Technische Paketprüfung; Sichtprüfung separat dokumentiert.'}
    (ROOT/'quality/krankenhaus-it-ki/pakete.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'originals':40,'individuals':len(rows),'gesamt_pages':report['gesamt_pages'],'dist':str(DIST)}))
if __name__=='__main__':main()
