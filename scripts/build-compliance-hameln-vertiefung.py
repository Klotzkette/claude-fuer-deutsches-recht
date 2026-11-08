#!/usr/bin/env python3
"""Erzeugt fallbezogene Compliance-Fortsetzungen und bearbeitbare Wordvorlagen.

Bestehende Aktenstücke werden nicht verändert. Die kuratierten Inhalte liegen
in data/compliance-hameln-vertiefung.json; der Builder benötigt keine privaten
Ausgangsdateien. Datumsangaben bleiben an die jeweilige Fallchronologie gebunden.
"""
from __future__ import annotations
import argparse
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.utils import format_datetime
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
from zoneinfo import ZoneInfo
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).with_name('data') / 'compliance-hameln-vertiefung.json'
PLUGIN = 'compliance-abteilung-grosskonzern'
MAIL = '12_Ergaenzende_Stellungnahme.eml'
PROTOCOL = '13_Belegabgleich_und_Sicherungsstand.docx'


def field(paragraph, instruction):
    run = paragraph.add_run()
    begin = OxmlElement('w:fldChar'); begin.set(qn('w:fldCharType'), 'begin')
    text = OxmlElement('w:instrText'); text.set(qn('xml:space'), 'preserve'); text.text = ' '+instruction+' '
    end = OxmlElement('w:fldChar'); end.set(qn('w:fldCharType'), 'end')
    for element in (begin,text,end): run._r.append(element)


def setup(c, template=False):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(1.8)
    sec.left_margin, sec.right_margin = Cm(2.1), Cm(2.1)
    sec.header_distance, sec.footer_distance = Cm(0.8), Cm(0.8)
    for name in ('Normal','Title','Subtitle','Heading 1','Heading 2'):
        style=doc.styles[name]; style.font.name='Times New Roman'; style.font.color.rgb=RGBColor(0,0,0)
        fonts=style.element.get_or_add_rPr().get_or_add_rFonts()
        for attr in ('asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme','csTheme'):
            if qn('w:'+attr) in fonts.attrib: del fonts.attrib[qn('w:'+attr)]
        for attr in ('ascii','hAnsi','eastAsia','cs'): fonts.set(qn('w:'+attr),'Times New Roman')
        for border in style.element.xpath('.//w:pBdr'): border.getparent().remove(border)
        style.font.size=Pt(11)
    normal=doc.styles['Normal']; normal.paragraph_format.space_after=Pt(6)
    normal.paragraph_format.line_spacing=1.08
    doc.styles['Title'].font.size=Pt(18); doc.styles['Title'].font.bold=True
    doc.styles['Title'].paragraph_format.space_after=Pt(10)
    doc.styles['Subtitle'].font.size=Pt(10)
    for name in ('Heading 1','Heading 2'):
        s=doc.styles[name];s.font.bold=True;s.paragraph_format.space_before=Pt(11);s.paragraph_format.space_after=Pt(5)
        s.paragraph_format.keep_with_next=True
    head=sec.header.paragraphs[0]
    head.add_run('MERRENSTEG ELEKTROSYSTEME SE').bold=True
    head.add_run('  |  Recht und Compliance  |  Hameln')
    for run in head.runs:run.font.size=Pt(8.5)
    footer=sec.footer.paragraphs[0]
    footer.add_run(c['nr']+'  ·  '+('Entscheidungsvorlage' if template else 'Belegabgleich')+'  |  Seite ')
    field(footer,'PAGE');footer.add_run(' von ');field(footer,'NUMPAGES')
    for run in footer.runs:run.font.size=Pt(8.5)
    # Remove inherited title decorations from the stock OOXML template.
    for style in doc.styles:
        for border in style.element.xpath('.//w:pBdr'): border.getparent().remove(border)
    cp=doc.core_properties;cp.author='Merrensteg Elektrosysteme SE';cp.last_modified_by='Recht und Compliance'
    cp.created=cp.modified=datetime(2026,11,8,9,0,0)
    return doc


def save(doc,path):
    path.parent.mkdir(parents=True,exist_ok=True)
    stream=BytesIO();doc.save(stream)
    with ZipFile(stream) as source,ZipFile(path,'w') as archive:
        for name in source.namelist():
            info=ZipInfo(name,date_time=(2026,11,8,9,0,0));info.compress_type=ZIP_DEFLATED
            archive.writestr(info,source.read(name))


def addpara(doc,text,style=None):
    p=doc.add_paragraph(text,style=style)
    p.paragraph_format.widow_control=True
    return p


def heading(doc,number,text):
    return doc.add_heading(f'{number} {text}',level=1)


def table(doc,cols,rows):
    tab=doc.add_table(rows=1,cols=len(cols));tab.alignment=WD_TABLE_ALIGNMENT.CENTER
    tab.autofit=False
    # Record identifier remains compact; descriptive attributes receive more room.
    widths=[2.2]+[(16.8-2.2)/(len(cols)-1)]*(len(cols)-1)
    if len(cols)==3:widths=[2.2,7.3,7.3]
    for i,col in enumerate(cols):tab.rows[0].cells[i].text=str(col)
    for values in rows:
        for cell,value in zip(tab.add_row().cells,values):cell.text=str(value)
    for rownum,row in enumerate(tab.rows):
        for i,cell in enumerate(row.cells):
            cell.width=Cm(widths[i]);cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            props=cell._tc.get_or_add_tcPr()
            margins=OxmlElement('w:tcMar')
            for edge in ('top','left','bottom','right'):
                el=OxmlElement('w:'+edge);el.set(qn('w:w'),'80');el.set(qn('w:type'),'dxa');margins.append(el)
            props.append(margins)
            if rownum==0:
                shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'E8F0F2');props.append(shade)
            for p in cell.paragraphs:
                p.paragraph_format.space_after=Pt(2);p.paragraph_format.space_before=Pt(2);p.paragraph_format.line_spacing=1.0
                for run in p.runs:run.font.size=Pt(10);run.bold=rownum==0
        if rownum==0:
            repeat=OxmlElement('w:tblHeader');row._tr.get_or_add_trPr().append(repeat)
        no_split=OxmlElement('w:cantSplit');row._tr.get_or_add_trPr().append(no_split)
    borders=OxmlElement('w:tblBorders')
    for edge in ('top','left','bottom','right','insideH','insideV'):
        e=OxmlElement('w:'+edge);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'4');e.set(qn('w:color'),'D9D9D9');borders.append(e)
    tab._tbl.tblPr.append(borders)
    doc.add_paragraph()
    return tab


def mail(c,path):
    m=c['mail'];msg=EmailMessage(policy=policy.SMTP)
    msg['From']=f"{m['from_name']} <{m['from_account']}@merrensteg.example>"
    msg['To']='Fallführung Recht und Compliance <fallfuehrung@merrensteg.example>'
    msg['Subject']=c['nr']+' | '+m['subject']
    moment=datetime.fromisoformat(c['date']).replace(hour=10,minute=18,tzinfo=ZoneInfo('Europe/Berlin'))
    msg['Date']=format_datetime(moment)
    msg['Message-ID']=f"<{c['nr'].lower()}.fortsetzung.{c['date']}@merrensteg.example>"
    msg['In-Reply-To']=f"<{c['nr'].lower()}.12@merrensteg.example>" if c['nr']<'ME-29' else f"<{c['nr'].lower()}.2026-10-12@merrensteg.example>"
    # ME-35 occurs in 2027, not the general October 2026 series.
    if c['nr']=='ME-35':msg.replace_header('In-Reply-To','<me-35.2027-12-10@merrensteg.example>')
    body='Guten Tag,\n\n'+'\n\n'.join(m['paragraphs'])+'\n\nMit freundlichen Grüßen\n'+m['from_name']+'\nMerrensteg Elektrosysteme SE · Hameln\n'
    msg.set_content(body,charset='utf-8',cte='quoted-printable');path.write_bytes(msg.as_bytes())


def protocol(c,path):
    p=c['protocol'];doc=setup(c)
    doc.add_paragraph(p['title'],style='Title')
    day=datetime.fromisoformat(c['date']).strftime('%d.%m.%Y')
    doc.add_paragraph(f"{c['nr']} · {c['title']} · {day}",style='Subtitle')
    addpara(doc,p['scope'])
    heading(doc,1,'Abgleich mit dem vorhandenen Datenregister')
    addpara(doc,'Die folgenden Werte sind aus 04a_Rohdaten.csv übernommen. Die XLSX-Fassung 04_Datenregister.xlsx und die Bildschirmdarstellung 05_Registerauszug.png sind daneben erhalten. Die Übernahme bestätigt den Inhalt des Registers; sie ersetzt nicht die dort benannten Primärnachweise.')
    tab=p['table'];addpara(doc,tab['titel']);table(doc,tab['spalten'],tab['zeilen'])
    heading(doc,2,'Stand der ergänzenden Stellungnahme')
    addpara(doc,f"Die E-Mail 12_Ergaenzende_Stellungnahme.eml von {c['mail']['from_name']} enthält zum Vorgang die nachstehenden Ergänzungen. Die Aussagen bleiben der benannten Stelle zugeordnet; eine rechtliche Bewertung oder abschließende Feststellung ist damit nicht verbunden.")
    for i,paragraph in enumerate(c['mail']['paragraphs'],1):
        addpara(doc,f'{i}. Absatz der Stellungnahme: '+paragraph)
    heading(doc,3,'Sicherung und Aussagegrenzen')
    addpara(doc,p['preservation'])
    addpara(doc,'Die Ausgangsunterlagen bleiben in ihrer bisherigen Fassung erhalten. Neue Zuordnungen, Berechnungen oder Redaktionen werden als eigene Arbeitsfassungen mit Datum und verantwortlicher Stelle geführt. Für eine Behauptung, dass ein im Register genannter Primärbeleg bereits vollständig geprüft sei, ist ein gesonderter Prüfvermerk erforderlich.')
    heading(doc,4,'Noch zu entscheidender Prüfauftrag')
    addpara(doc,p['question'])
    addpara(doc,'Die Fallführung soll festhalten, welche dieser Fragen anhand der vorhandenen Dateien beantwortet werden kann und welcher einzelne Nachweis noch angefordert werden muss. Der Adressatenkreis richtet sich nach dem erforderlichen Zugriff auf die konkreten Inhalte; dieses Protokoll erteilt keine externe Versand- oder Einreichungsfreigabe.')
    heading(doc,5,'Herangezogene Dateistände')
    addpara(doc,'Der Abgleich bezieht sich auf folgende in der Akte erhaltene Dateien: '+', '.join(p['source_files'])+'. Die neue Stellungnahme und dieses Protokoll ergänzen diese Dateistände, ohne sie zu ersetzen.')
    doc.core_properties.title=p['title']+' '+c['nr'];save(doc,path)


def template(c,path):
    d=c['template'];doc=setup(c,True)
    doc.add_paragraph(d['title'],style='Title')
    doc.add_paragraph(c['nr']+' · '+c['title'],style='Subtitle')
    addpara(doc,'Die Vorlage dient der ausformulierten Bearbeitung dieses Vorgangs. Ersetzen Sie die beschrifteten Eingabefelder durch geprüfte Angaben und konkrete Fundstellen. Die Unterlagen werden zuerst ausgewertet; offene entscheidende Tatsachen bleiben sichtbar. Der Empfängertext enthält nur die für die jeweilige Entscheidung erforderlichen Inhalte.')
    fields=d['fields']
    for i,(title,text) in enumerate(fields,1):
        heading(doc,i,title)
        # Earlier short field labels become complete sentences without inventing facts.
        if text.startswith('[') and text.endswith(']'):
            text='Zu diesem Punkt sind '+text+' durch [Datei und genaue Fundstelle] belegt; offen bleibt [konkret fehlender Nachweis].'
        addpara(doc,text)
    start=len(fields)
    heading(doc,start+1,d['specific_heading']);addpara(doc,d['specific_paragraph'])
    heading(doc,start+2,'Belegte Tatsachen und stärkster Einwand')
    addpara(doc,'Die Feststellung [Behauptung] wird durch [Originaldatei mit Seite, Zeile oder Zeitmarke] getragen. Der stärkste Einwand [Gegenbeleg oder alternative Erklärung] führt zu [begründeter begrenzter Aussage oder Prüfauftrag]. Die ergänzende Stellungnahme und der Belegabgleich sind mit ihrem jeweiligen Quellenstatus berücksichtigt.')
    heading(doc,start+3,'Entscheidung und verbleibende Voraussetzung')
    addpara(doc,'Wir schlagen [konkrete Maßnahme] für [Rechtsträger, Funktion und Zeitraum] unter [überprüfbarer Voraussetzung] vor. Gegenüber [Alternative mit konkreter Folge] überwiegt [begründete Erwägung]. Vor [betroffenem Schritt] klärt [zuständige Rolle] die Tatsache [offener Punkt] anhand [Nachweis].')
    heading(doc,start+4,'Umsetzung und Nachprüfung')
    addpara(doc,'[Verantwortliche Rolle] setzt [Schritt] bis [Datum und Uhrzeit] um. [Unabhängige prüfende Rolle] kontrolliert die Wirkung am [Termin] anhand [beobachtbares Kriterium und Beleg]. Bei [Abweichung] gilt [Stopp, Begrenzung oder Eskalation]. [Zuständige Rolle] erteilt die Freigabe zum [Versand, Vollzug oder Betrieb] erst nach [Nachweis].')
    doc.core_properties.title=d['title'];save(doc,path)


def build(output_root:Path,data:Path=DATA):
    content=json.loads(data.read_text());cases=content['cases']
    assert content['schema_version']==1 and len(cases)==35
    for c in cases:
        assert c['slug'].startswith('compliance-hameln-')
        case=output_root/'testakten'/c['slug'];case.mkdir(parents=True,exist_ok=True)
        mail(c,case/MAIL);protocol(c,case/PROTOCOL)
        template(c,output_root/PLUGIN/'templates'/f"{c['slug']}.docx")
    print(f'{len(cases)} Fallfortsetzungen, {len(cases)*2} neue Aktenstücke, {len(cases)} Wordvorlagen erzeugt.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output-root',type=Path,default=ROOT);parser.add_argument('--data',type=Path,default=DATA)
    args=parser.parse_args();build(args.output_root,args.data)
