#!/usr/bin/env python3
"""Native Neuberechnung, Lesefassung und flache Archive. Autor: Klotzkette."""
from __future__ import annotations
import argparse
import csv
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile

from openpyxl import load_workbook
from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Spacer

from office_process import run_office
from testakte_office_pdf import office_binary, render_office_batch
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

HERE=Path(__file__).resolve().parent
def module(name,filename):
    spec=importlib.util.spec_from_file_location(name,HERE/filename);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

B=module("einbeck_native","build-bauwirtschaft-einbeck-akte.py")
QA=B.ASSETS/"qa-einbeck"
N="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
CORE="{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}"
DC="{http://purl.org/dc/elements/1.1/}"

def patch_xlsx(path,mutation=None,clear_formula_cache=False):
    """Ergänzt Drucklayout/Metadaten, ohne Formel- oder Wertautorenschaft zu ersetzen."""
    ranges={9:["A1:G29"],19:["A1:G24"],24:["A1:G29"],37:["A1:G34","A1:F28"]}
    n=int(path.name[:2]);out=io.BytesIO()
    with zipfile.ZipFile(path) as src,zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as dst:
        for info in src.infolist():
            data=src.read(info)
            if info.filename=="docProps/core.xml":
                root=ET.fromstring(data)
                for tag in [DC+"creator",CORE+"lastModifiedBy"]:
                    elem=root.find(tag)
                    if elem is None:elem=ET.SubElement(root,tag)
                    elem.text=B.AUTHOR
                data=ET.tostring(root,encoding="utf-8",xml_declaration=True)
            elif info.filename=="xl/workbook.xml":
                root=ET.fromstring(data);names=root.find(N+"definedNames")
                if names is None:names=ET.SubElement(root,N+"definedNames")
                for item in list(names):
                    if item.get("name") in ("_xlnm.Print_Area","_xlnm.Print_Titles"):names.remove(item)
                for index,sheet in enumerate(root.find(N+"sheets")):
                    area=ET.SubElement(names,N+"definedName",name="_xlnm.Print_Area",localSheetId=str(index));area.text=f"'{sheet.get('name')}'!{ranges[n][index]}"
                    titles=ET.SubElement(names,N+"definedName",name="_xlnm.Print_Titles",localSheetId=str(index));titles.text=f"'{sheet.get('name')}'!$1:$5"
                calc=root.find(N+"calcPr")
                if calc is None:calc=ET.SubElement(root,N+"calcPr")
                calc.set("calcMode","auto");calc.set("fullCalcOnLoad","1");calc.set("forceFullCalc","1")
                data=ET.tostring(root,encoding="utf-8",xml_declaration=True)
            elif info.filename.startswith("xl/worksheets/sheet") and info.filename.endswith(".xml"):
                root=ET.fromstring(data)
                setup=root.find(N+"pageSetup")
                if setup is None:setup=ET.SubElement(root,N+"pageSetup")
                setup.attrib.update(paperSize="9",orientation="landscape",fitToWidth="1",fitToHeight="0")
                prop=root.find(N+"sheetPr")
                if prop is None:prop=ET.Element(N+"sheetPr");root.insert(0,prop)
                ps=prop.find(N+"pageSetUpPr")
                if ps is None:ps=ET.SubElement(prop,N+"pageSetUpPr")
                ps.set("fitToPage","1")
                if mutation and info.filename==f"xl/worksheets/sheet{mutation['sheet']}.xml":
                    cell=root.find(f".//{N}c[@r='{mutation['cell']}']")
                    if cell is None:raise ValueError(mutation)
                    for child in list(cell):cell.remove(child)
                    cell.attrib.pop("t",None)
                    if mutation['value'] is not None:ET.SubElement(cell,N+"v").text=str(mutation['value'])
                if mutation or clear_formula_cache:
                    # Nach einer externen Eingabeänderung darf Office keinen alten Cache übernehmen.
                    for cell in root.findall(f".//{N}c"):
                        if cell.find(N+"f") is not None:
                            for cached in cell.findall(N+"v"):cell.remove(cached)
                data=ET.tostring(root,encoding="utf-8",xml_declaration=True)
            dst.writestr(info,data)
    path.write_bytes(out.getvalue())

def native_roundtrip(paths,label):
    base=QA/"office"/label;out=base/"output";out.mkdir(parents=True,exist_ok=True)
    binary=office_binary()
    if not binary:raise RuntimeError("Native Office-Laufzeit fehlt; SOFFICE setzen.")
    cmd=[binary,f"-env:UserInstallation={(base/'profile').resolve().as_uri()}","--headless","--convert-to","xlsx","--outdir",str(out),*[str(p) for p in paths]]
    rc,logs=run_office(cmd,env=os.environ.copy(),timeout=180)
    (base/"lauf.log").write_text(logs,encoding="utf-8")
    results=[out/p.name for p in paths]
    if rc or any(not p.is_file() for p in results):raise RuntimeError(f"Office-Neuberechnung fehlgeschlagen: {logs}")
    return results

def formula_map(path):
    w=load_workbook(path,data_only=False);result={(s.title,c.coordinate):c.value for s in w for row in s for c in row if c.data_type=="f"};w.close();return result

def recalculate():
    files=[B.CASE/B.FILES[n] for n in (9,19,24,37)]
    for p in files:patch_xlsx(p,clear_formula_cache=True)
    originals={p.name:formula_map(p) for p in files}
    outputs=native_roundtrip(files,"baseline")
    checks=[]
    expected={9:("Kosten","E16",337240),19:("Termine","C6",36),24:("LV","E19",99785),37:("Rechnung","E24",114153.8)}
    for p in outputs:
        assert formula_map(p)==originals[p.name],f"Formeländerung durch Office: {p.name}"
        wb=load_workbook(p,data_only=True);s,c,v=expected[int(p.name[:2])];assert abs(wb[s][c].value-v)<.001
        for ws in wb:
            for row in ws:
                assert all(c.data_type!="e" for c in row),p.name
        wb.close();shutil.copyfile(p,B.CASE/p.name);patch_xlsx(B.CASE/p.name)
        checks.append(dict(file=p.name,formulas=len(originals[p.name]),result=v))
    (QA/"native-basispruefung.json").write_text(json.dumps(checks,indent=2,ensure_ascii=False))

def normalize(data,title):
    r=PdfReader(io.BytesIO(data));w=PdfWriter()
    for page in r.pages:w.add_page(page)
    w.add_metadata({"/Author":B.AUTHOR,"/Title":title,"/Creator":B.AUTHOR,"/Producer":B.AUTHOR})
    out=io.BytesIO();w.write(out);return out.getvalue()

def diary_pdf(source):
    with source.open(encoding="utf-8-sig",newline="") as f:rows=list(csv.reader(f))
    flow=[B.para("Bautagebuch Bürgerhaus Leinewinkel",B.TITLE),B.para("Hartwig Architektur · Abschlussstand 18.03.2024 · Empfänger: Vorstand · BH-21-04"),
          B.table(rows,[65,85,55,420,117]),Spacer(1,12),B.para("gez. Lena Hartwig · Tageszeichnungen gemäß letzter Spalte. Anlagen: keine.")]
    out=io.BytesIO();SimpleDocTemplate(out,pagesize=landscape(A4),leftMargin=50,rightMargin=50,topMargin=42,bottomMargin=42,author=B.AUTHOR).build(flow);return out.getvalue()

def render_documents():
    E=module("einbeck_einzel","build-testakten-einzelpdf-zips.py")
    B.register_fonts();pdfdir=QA/"einzel-pdf";pdfdir.mkdir(parents=True,exist_ok=True)
    renderer=os.environ.get("DOCX_RENDERER")
    if not renderer:raise RuntimeError("DOCX_RENDERER muss auf render_docx.py der Dokumentwerkzeuge zeigen.")
    office=render_office_batch([B.CASE/B.FILES[n] for n in (9,19,24,37)])
    index=[]
    for n,name in B.FILES.items():
        source=B.CASE/name;ext=source.suffix.lower()
        if ext==".docx":
            dest=QA/f"docx-{n:02d}"
            subprocess.run([sys.executable,renderer,str(source),"--output_dir",str(dest),"--emit_pdf","--dpi","110"],check=True,capture_output=True,text=True)
            data=(dest/(source.stem+".pdf")).read_bytes()
        elif ext==".csv":data=diary_pdf(source)
        else:data=E.render_document_pdf(source,B.CASE,office)
        if not data:raise RuntimeError(f"Kein PDF: {name}")
        pdf=pdfdir/(source.stem+".pdf");pdf.write_bytes(normalize(data,source.stem))
        pages=len(PdfReader(pdf).pages);index.append(dict(number=n,file=name,pdf=str(pdf),pages=pages))
        print(f"{n:02d}: {pages} Seiten",flush=True)
    (QA/"dokumentindex.json").write_text(json.dumps(index,ensure_ascii=False,indent=2));return index

def render_previews(index):
    binary=shutil.which("pdftoppm")
    if not binary:raise RuntimeError("PDF-Vorschauen benötigen pdftoppm aus Poppler im PATH.")
    for d in index:
        dest=QA/f"pdf-{d['number']:02d}";dest.mkdir(parents=True,exist_ok=True)
        for old in dest.glob("seite-*.png"):old.unlink()
        prefix=dest/"poppler"
        subprocess.run([binary,"-png","-r","94",str(d["pdf"]),str(prefix)],check=True,capture_output=True,text=True)
        pages=sorted(dest.glob("poppler-*.png"))
        if len(pages)!=d["pages"]:raise RuntimeError(f"Unvollständige PDF-Vorschau: {d['file']}")
        for page in pages:
            number=int(page.stem.rsplit("-",1)[1]);page.rename(dest/f"seite-{number:02d}.png")

def package(index):
    E=module("einbeck_einzel","build-testakten-einzelpdf-zips.py")
    Z=module("einbeck_zip","build-testakten-release-zips.py")
    cover=QA/"register.pdf"
    rows=[["Nr.","Unterlage","Seiten"]]+[[str(d['number']),Path(d['file']).stem[14:].replace('_',' '),str(d['pages'])] for d in index]
    SimpleDocTemplate(str(cover),pagesize=A4,leftMargin=50,rightMargin=50,topMargin=50,bottomMargin=50,author=B.AUTHOR,title="Bürgerhaus Einbeck Aktenregister").build([
      B.para("Bürgerhaus Leinewinkel in Einbeck",B.TITLE),B.para("Umbau und Nordanbau · Projekt BH-21-04"),
      B.para("Aktenstand 21.09.2026 · 44 Originalunterlagen · Beginn November 2020 · Übergabe April 2024"),
      B.para("1 Dokumentenregister",B.HEAD),B.table(rows,[35,410,50])])
    w=PdfWriter();w.append(cover);cursor=len(PdfReader(cover).pages)
    for d in index:
        d["gesamt_start"]=cursor+1;w.append(d['pdf'],outline_item=f"{d['number']:02d} {Path(d['file']).stem[14:]}");cursor+=d['pages']
    w.add_metadata({"/Author":B.AUTHOR,"/Title":"Bürgerhaus Leinewinkel Einbeck · Gesamtakte","/Creator":B.AUTHOR,"/Producer":B.AUTHOR})
    total=B.ASSETS/(B.SLUG+"_gesamt.pdf")
    with total.open("wb") as f:w.write(f)
    notice=NOTICE_BYTES+b"\n\n"+"Bürgerhaus Leinewinkel in Einbeck. Autor: Klotzkette. 44 Originalunterlagen. Aktenstand 21.09.2026. Alle Personen, Firmen, Grundstücksdaten und Verwaltungsvorgänge dieser Akte sind erfunden; der Ort und die verlinkten amtlichen Quellen sind real. Die Akte enthält keine Musterlösung.\n".encode("utf-8")
    original=B.ASSETS/f"testakte-{B.SLUG}.zip";single=B.ASSETS/f"testakte-{B.SLUG}-einzelpdfs.zip"
    with zipfile.ZipFile(original,"w",zipfile.ZIP_DEFLATED) as z:
        Z.write_bytes(z,notice,NOTICE_FILENAME)
        for name in B.FILES.values():Z.write_file(z,B.CASE/name,name)
    with zipfile.ZipFile(single,"w",zipfile.ZIP_DEFLATED) as z:
        E.write_pdf(z,NOTICE_FILENAME,notice)
        for d in index:E.write_pdf(z,Path(d['pdf']).name,Path(d['pdf']).read_bytes())
    (QA/"dokumentindex.json").write_text(json.dumps(index,ensure_ascii=False,indent=2))
    render_previews(index)
    print(json.dumps(dict(total=str(total),pages=cursor,originals=str(original),individual=str(single)),ensure_ascii=False))

def main():
    p=argparse.ArgumentParser();p.add_argument("--stage",choices=["recalculate","render","package","all"],default="all");args=p.parse_args();QA.mkdir(parents=True,exist_ok=True)
    if args.stage in ("recalculate","all"):recalculate()
    if args.stage=="recalculate":return
    if args.stage in ("render","all"):
        B.define_documents()
        for n,d in B.DATA.items():
            if B.FILES[n].endswith(".eml"):B.eml(d)
        index=render_documents()
    else:index=json.loads((QA/"dokumentindex.json").read_text())
    if args.stage!="render":package(index)

if __name__=="__main__":main()
