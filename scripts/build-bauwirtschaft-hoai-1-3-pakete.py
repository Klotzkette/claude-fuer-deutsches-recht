#!/usr/bin/env python3
"""Native Neuberechnung und geprüfte Exporte nur für HOAI 1 bis 3. Autor: Klotzkette."""
from __future__ import annotations

import argparse
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

from openpyxl import load_workbook
from pypdf import PdfReader, PdfWriter
from PIL import Image, ImageDraw
from akten_build_runtime import screen_font
from office_process import run_office
from testakte_office_pdf import office_binary, render_office_batch
from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME

HERE=Path(__file__).resolve().parent
def module(name, filename):
    spec=importlib.util.spec_from_file_location(name,HERE/filename)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result

B=module("hoai_1_3_originale","build-bauwirtschaft-hoai-1-3-akten.py")
N="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
DC="{http://purl.org/dc/elements/1.1/}"
CP="{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}"
WORKBOOKS={
    (1,12):dict(sheet="Budget",area="A1:G25",input="B9",output="E17",baseline=8068.2,changed=7,expected=8240.75),
    (2,10):dict(sheet="Kosten",area="A1:G30",input="F9",output="G19",baseline=3133231,changed=48000,expected=3190351),
    (3,11):dict(sheet="Berechnung",area="A1:G34",input="D13",output="E19",baseline=2806800,changed=710000,expected=2826800),
    (3,14):dict(sheet="Termine",area="A1:G22",input="C6",output="D17",baseline=6,changed=14,expected=13),
}


def original(phase,number):
    return B.ROOT/"testakten"/B.CASES[phase]["slug"]/B.CASES[phase]["files"][number-1]


def patch_xlsx(path, spec, mutation=None, clear=False):
    """Nur Metadaten, Druckeinstellungen und temporäre Testmutation; keine Tabellenautorenschaft."""
    output=io.BytesIO()
    with zipfile.ZipFile(path) as src,zipfile.ZipFile(output,"w",zipfile.ZIP_DEFLATED) as dst:
        for info in src.infolist():
            data=src.read(info)
            if info.filename=="docProps/core.xml":
                root=ET.fromstring(data)
                for tag in (DC+"creator",CP+"lastModifiedBy"):
                    el=root.find(tag)
                    if el is None:el=ET.SubElement(root,tag)
                    el.text=B.AUTHOR
                data=ET.tostring(root,encoding="utf-8",xml_declaration=True)
            elif info.filename=="xl/workbook.xml":
                root=ET.fromstring(data);names=root.find(N+"definedNames")
                if names is None:names=ET.SubElement(root,N+"definedNames")
                for item in list(names):
                    if item.get("name") in ("_xlnm.Print_Area","_xlnm.Print_Titles"):names.remove(item)
                area=ET.SubElement(names,N+"definedName",name="_xlnm.Print_Area",localSheetId="0")
                area.text=f"'{spec['sheet']}'!{spec['area']}"
                title=ET.SubElement(names,N+"definedName",name="_xlnm.Print_Titles",localSheetId="0");title.text=f"'{spec['sheet']}'!$1:$5"
                calc=root.find(N+"calcPr")
                if calc is None:calc=ET.SubElement(root,N+"calcPr")
                calc.attrib.update(calcMode="auto",fullCalcOnLoad="1",forceFullCalc="1")
                data=ET.tostring(root,encoding="utf-8",xml_declaration=True)
            elif info.filename=="xl/worksheets/sheet1.xml":
                root=ET.fromstring(data)
                setup=root.find(N+"pageSetup")
                if setup is None:setup=ET.SubElement(root,N+"pageSetup")
                setup.attrib.update(paperSize="9",orientation="landscape",fitToWidth="1",fitToHeight="1")
                margins=root.find(N+"pageMargins")
                if margins is None:margins=ET.SubElement(root,N+"pageMargins")
                margins.attrib.update(left="0.5",right="0.5",top="0.45",bottom="0.45",header="0.2",footer="0.2")
                prop=root.find(N+"sheetPr")
                if prop is None:prop=ET.Element(N+"sheetPr");root.insert(0,prop)
                ps=prop.find(N+"pageSetUpPr")
                if ps is None:ps=ET.SubElement(prop,N+"pageSetUpPr")
                ps.set("fitToPage","1")
                if mutation is not None:
                    cell=root.find(f".//{N}c[@r='{spec['input']}']")
                    if cell is None:raise ValueError(spec["input"])
                    for child in list(cell):cell.remove(child)
                    cell.attrib.pop("t",None)
                    if mutation!="blank":ET.SubElement(cell,N+"v").text=str(mutation)
                if clear or mutation is not None:
                    for cell in root.findall(f".//{N}c"):
                        if cell.find(N+"f") is not None:
                            for cache in cell.findall(N+"v"):cell.remove(cache)
                data=ET.tostring(root,encoding="utf-8",xml_declaration=True)
            dst.writestr(info,data)
    path.write_bytes(output.getvalue())


def formulas(path):
    w=load_workbook(path,data_only=False)
    result={(s.title,c.coordinate):c.value for s in w for row in s for c in row if c.data_type=="f"};w.close();return result


def roundtrip(paths,directory):
    binary=office_binary()
    if not binary:raise RuntimeError("Gebündelte Office-Laufzeit fehlt; SOFFICE setzen.")
    output=directory/"output";output.mkdir(parents=True,exist_ok=True)
    command=[binary,f"-env:UserInstallation={(directory/'profile').resolve().as_uri()}","--headless","--convert-to","xlsx","--outdir",str(output),*[str(p.resolve()) for p in paths]]
    code,logs=run_office(command,env=os.environ.copy(),timeout=180)
    (directory/"office.log").write_text(logs,encoding="utf-8")
    result=[output/p.name for p in paths]
    if code or any(not p.exists() for p in result):raise RuntimeError(logs)
    return result


def native(phases,qa):
    checks=[]
    for (phase,number),spec in WORKBOOKS.items():
        if phase not in phases:continue
        source=original(phase,number);patch_xlsx(source,spec,clear=True);before=formulas(source)
        with tempfile.TemporaryDirectory(prefix=f"native-{phase}-{number}-",dir=qa) as tmp:
            output=roundtrip([source],Path(tmp))[0]
            assert formulas(output)==before,f"Formeln verändert: {source.name}"
            w=load_workbook(output,data_only=True);value=w[spec["sheet"]][spec["output"]].value
            assert isinstance(value,(int,float)) and abs(value-spec["baseline"])<.01,(source.name,value,spec["baseline"])
            assert not [(s.title,c.coordinate,c.value) for s in w for row in s for c in row if c.data_type=="e"]
            w.close();shutil.copyfile(output,source);patch_xlsx(source,spec)
        checks.append(dict(phase=phase,file=source.name,result=value,formulas=len(before),engine="LibreOffice",input_mutation="separater Test --native"))
    (qa/"native-basis.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding="utf-8")
    return checks


def normalize_pdf(data,title):
    r=PdfReader(io.BytesIO(data));w=PdfWriter();w.clone_document_from_reader(r)
    w.add_metadata({"/Author":B.AUTHOR,"/Creator":B.AUTHOR,"/Producer":B.AUTHOR,"/Title":title})
    output=io.BytesIO();w.write(output);return output.getvalue()


def render(phase,qa):
    E=module("hoai_1_3_einzel","build-testakten-einzelpdf-zips.py")
    c=B.CASES[phase];case=B.ROOT/"testakten"/c["slug"]
    pdfdir=qa/f"phase-{phase}"/"einzel-pdf";pdfdir.mkdir(parents=True,exist_ok=True)
    renderer=os.environ.get("DOCX_RENDERER")
    if not renderer:raise RuntimeError("DOCX_RENDERER auf render_docx.py der Dokumentwerkzeuge setzen.")
    office=render_office_batch([case/name for name in c["files"] if name.endswith(".xlsx")])
    index=[]
    for n,name in enumerate(c["files"],1):
        source=case/name
        if source.suffix==".docx":
            target=qa/f"phase-{phase}"/f"docx-{n:02d}"
            process=subprocess.run([os.environ.get("DOCX_PYTHON",sys.executable),renderer,str(source),"--output_dir",str(target),"--emit_pdf","--dpi","100"],capture_output=True,text=True)
            if process.returncode:raise RuntimeError(process.stdout+process.stderr)
            data=(target/(source.stem+".pdf")).read_bytes()
        else:data=E.render_document_pdf(source,case,office)
        if not data:raise RuntimeError(name)
        dest=pdfdir/(source.stem+".pdf");dest.write_bytes(normalize_pdf(data,source.stem))
        pages=len(PdfReader(dest).pages)
        preview=qa/f"phase-{phase}"/f"pdf-{n:02d}";preview.mkdir(parents=True,exist_ok=True)
        for stale in preview.glob("page-*.png"):stale.unlink()
        subprocess.run(["pdftoppm","-png","-r","100",str(dest),str(preview/"page")],check=True,capture_output=True)
        index.append(dict(number=n,file=name,pdf=str(dest),pages=pages))
        print(f"Phase {phase} Dokument {n:02d}: {pages} Seiten",flush=True)
    (qa/f"phase-{phase}"/"index.json").write_text(json.dumps(index,ensure_ascii=False,indent=2),encoding="utf-8")
    return index


def package(phase,index,assets,qa):
    c=B.CASES[phase];case=B.ROOT/"testakten"/c["slug"]
    Z=module("hoai_1_3_zip","build-testakten-release-zips.py")
    E=module("hoai_1_3_einzel_export","build-testakten-einzelpdf-zips.py")
    # Die zentrale Zusammenstellung bleibt unverändert; nur eigene Zielakte aufrufen.
    G=module("hoai_1_3_gesamt","build-testakte-gesamt-pdf.py")
    status,message=G.build_gesamt_pdf(case)
    if status!="ok":raise RuntimeError(message)
    total=case/"gesamt-pdf"/(c["slug"]+"_gesamt.pdf")
    Z.build_single(case,assets)
    E.build_single(case,assets)
    shutil.copyfile(total,assets/total.name)
    preview=qa/f"phase-{phase}"/"gesamt";preview.mkdir(parents=True,exist_ok=True)
    for stale in preview.glob("page-*.png"):stale.unlink()
    subprocess.run(["pdftoppm","-png","-r","85",str(total),str(preview/"page")],check=True,capture_output=True)
    print(f"Phase {phase}: zentraler Gesamt-PDF-Builder und beide ZIPs abgeschlossen.",flush=True)


def contact_sheets(phase,qa):
    files=sorted((qa/f"phase-{phase}").glob("pdf-*/page-*.png"))
    for stale in (qa/f"phase-{phase}").glob("kontakt-*.png"):stale.unlink()
    for start in range(0,len(files),6):
        page=Image.new("RGB",(1500,2180),"white");draw=ImageDraw.Draw(page)
        for i,path in enumerate(files[start:start+6]):
            with Image.open(path) as im:
                im.thumbnail((485,690));x=(i%3)*500;y=(i//3)*1080
                draw.text((x+8,y+8),path.parent.name+" / "+path.stem,font=screen_font(18),fill="black")
                page.paste(im,(x+(500-im.width)//2,y+40))
        page.save(qa/f"phase-{phase}"/f"kontakt-{start//6+1:02d}.png")


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--phase",type=int,choices=[1,2,3],action="append")
    parser.add_argument("--assets",type=Path,default=Path(os.environ.get("HOAI_1_3_ASSETS","/tmp/bauwirtschaft-hoai-1-3-assets")))
    parser.add_argument("--stage",choices=["native","render","package","all"],default="all")
    args=parser.parse_args();phases=args.phase or [1,2,3];assets=args.assets.resolve();qa=assets/"qa-hoai-1-3";qa.mkdir(parents=True,exist_ok=True)
    if args.stage in ("native","all"):native(phases,qa)
    if args.stage=="native":return
    for phase in phases:
        index=render(phase,qa) if args.stage in ("render","all") else json.loads((qa/f"phase-{phase}"/"index.json").read_text())
        if args.stage in ("package","all"):package(phase,index,assets,qa)
        contact_sheets(phase,qa)


if __name__=="__main__":main()
