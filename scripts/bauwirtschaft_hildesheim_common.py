"""Gemeinsame Originalausgabe für das fiktive Hildesheimer Wohnhaus. Autor: Klotzkette."""
from __future__ import annotations
import mimetypes
import os
import re
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape
from zoneinfo import ZoneInfo
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from akten_build_runtime import serif_font_path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'bauwirtschaft-neubau-achtfamilienhaus-hildesheim'
CASE = ROOT/'testakten'/SLUG
ASSETS = Path(os.environ.get('HILDESHEIM_ASSETS', '/tmp/hildesheim/assets'))
REF = 'SW-HI-26-08'
AUTHOR = 'Klotzkette'
ACTORS = {
 'bauherr': ('Steinbogen Wohnen GmbH','Wohnhof Am Steinbogen 18, 31134 Hildesheim','projekt@steinbogen-wohnen.example','Maren Birk, Geschäftsführerin'),
 'architekt': ('Konturfeld Architektur PartG mbB','Planerhof 12, 31134 Hildesheim','projekt@konturfeld.example','Nora Feld, Architektin'),
 'bauamt': ('Stadt Hildesheim, Bauaufsicht','Markt 3, 31134 Hildesheim','bauaufsicht@hildesheim-akte.example','Jana Linde, Sachbearbeitung'),
 'tragwerk': ('Ingenieurbüro Bogenwerk','Tragwerkhof 7, 31135 Hildesheim','statik@bogenwerk.example','Dr. Jens Rabe, Tragwerksplaner'),
 'tga': ('Planwerk Haustechnik GmbH','Technikring 14, 31135 Hildesheim','planung@planwerk-tga.example','Elif Sand, Fachplanerin'),
 'geo': ('Bodenprofil Ingenieure GmbH','Bohrweg 6, 31137 Hildesheim','bericht@bodenprofil.example','Dr. Ute Venn, Geotechnikerin'),
 'vermessung': ('Vermessungsbüro Leinepunkt','Messbogen 22, 31134 Hildesheim','aufmass@leinepunkt.example','Ole Rehm, Vermessungsingenieur'),
 'rohbau': ('Steinwerk Hochbau GmbH','Werkhof 21, 31135 Hildesheim','bauleitung@steinwerk.example','Timo Wendt, Bauleiter'),
 'huelle': ('Dachraum Gebäudehülle GmbH','Dachbogen 11, 31137 Hildesheim','projekt@dachraum.example','Ina Mertens, Projektleitung'),
 'hls': ('Wärmefluss Haustechnik GmbH','Installationshof 16, 31135 Hildesheim','bau@waermefluss.example','Arne Thiel, Bauleitung'),
 'elektro': ('Lichtkreis Elektro GmbH','Schaltring 9, 31135 Hildesheim','projekt@lichtkreis.example','Selin Voß, Elektromeisterin'),
 'ausbau': ('Innenraum Ausbau GmbH','Werkzeile 24, 31137 Hildesheim','leitung@innenraum-ausbau.example','Jan Merz, Bauleiter'),
 'aufzug': ('Hubpunkt Aufzüge GmbH','Technikhof 5, 31135 Hildesheim','montage@hubpunkt.example','Ralf Hanke, Montageleitung'),
 'aussen': ('Grünkante Garten und Tiefbau GmbH','Pflanzhof 32, 31137 Hildesheim','bau@gruenkante.example','Mira Roth, Geschäftsführerin'),
 'bank': ('Leinebogen Projektbank AG','Bankhof 4, 31134 Hildesheim','finanzierung@leinebogen-bank.example','Petra West, Firmenkunden'),
 'notar': ('Notarin Dr. Carla Fink','Urkundenhof 8, 31134 Hildesheim','kanzlei@notarin-fink.example','Dr. Carla Fink, Notarin'),
 'makler': ('Wohnfeld Grundstücke GmbH','Vermittlerhof 15, 31134 Hildesheim','rechnung@wohnfeld.example','Lutz Berger, Geschäftsführung'),
 'steuer': ('Finanzamt Hildesheim','Steuerpostfach 86, 31134 Hildesheim','post@finanzamt-akte.example','Anja Dorn, Veranlagung'),
 'energie': ('Energiepfad Ingenieurbüro','Energieweg 17, 31135 Hildesheim','planung@energiepfad.example','Nils Frank, Energieplanung'),
 'brand': ('Brandschutzbüro Rettungsweg','Sicherheitsbogen 19, 31134 Hildesheim','nachweise@rettungsweg.example','Dr. Lea Stern, Brandschutzplanung'),
 'versicherung': ('Bauwert Versicherung AG','Versicherungsring 6, 30159 Hannover','vertrag@bauwert.example','Miriam Brand, Vertragsservice'),
 'versorger': ('Leineanschluss Netzdienste GmbH','Netzhof 27, 31135 Hildesheim','anschluss@leineanschluss.example','Henning Wulf, Hausanschlüsse'),
 'verwaltung': ('Steinbogen Wohnen GmbH, Mietverwaltung','Wohnhof Am Steinbogen 18, 31134 Hildesheim','miete@steinbogen-wohnen.example','Lea Fricke, Mietverwaltung'),
 'mieter': ('Familie Hartung, Wohnung 05','Wohnhof Am Steinbogen 18, 31134 Hildesheim','hartung@haushalt.example','Sabine Hartung'),
 'anwalt': ('Kanzlei Leinebogen Rechtsanwälte','Rechtshof 9, 31134 Hildesheim','bau@kanzlei-leinebogen.example','Dr. Felix Groth, Rechtsanwalt'),
 'grundbuch': ('Amtsgericht Hildesheim, Grundbuchamt','Gerichtspostfach 12, 31134 Hildesheim','grundbuch@gericht-akte.example','Klara Sommer, Kostenstelle'),
}

def euro(value):
    return f'{value:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.')

def setup_fonts():
    for suffix,bold in [('',False),('Bold',True)]:
        if 'Hildesheim'+suffix not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont('Hildesheim'+suffix,str(serif_font_path(bold))))
    pdfmetrics.registerFontFamily('Hildesheim',normal='Hildesheim',bold='HildesheimBold',italic='Hildesheim',boldItalic='HildesheimBold')

def _body_text(d):
    text=[]
    for item in d['sections']:
        if isinstance(item,str):text.append(item)
        elif item[0]=='h':text.append(item[1])
        elif item[0]=='t':text.extend(' | '.join(map(str,row)) for row in item[1])
    return '\n\n'.join(text)

def written_norms(value):
    """Normzitate nach der Hauskonvention ausschreiben, Kennungen erhalten."""
    if isinstance(value, str):
        value = re.sub(r'§§\s*', 'Paragrafen ', value)
        return re.sub(r'§\s*', 'Paragraf ', value)
    if isinstance(value, dict):
        return {key: written_norms(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return type(value)(written_norms(item) for item in value)
    return value

def pdf(d):
    d=written_norms(d)
    setup_fonts(); sender=ACTORS[d['issuer']]; recipient=ACTORS[d['recipient']]
    body=ParagraphStyle('Body',fontName='Hildesheim',fontSize=11,leading=14.2,spaceAfter=8)
    small=ParagraphStyle('Small',parent=body,fontSize=9,leading=11.5,spaceAfter=4)
    heading=ParagraphStyle('Heading',parent=body,fontName='HildesheimBold',fontSize=12,leading=15,spaceBefore=10,spaceAfter=10,keepWithNext=True)
    title=ParagraphStyle('Title',parent=heading,fontSize=16,leading=19)
    def p(s,style=body):return Paragraph(escape(str(s)).replace('\n','<br/>'),style)
    def frame(c,document):
        c.setFont('HildesheimBold',12);c.drawString(50,804,sender[0])
        c.setFont('Hildesheim',9);c.drawString(50,789,sender[1]);c.drawString(50,776,sender[2])
        c.setFont('Hildesheim',8);c.drawString(50,29,REF+' · '+d['date']);c.drawRightString(545,29,f'Seite {document.page}')
    story=[p(recipient[0]+'\n'+recipient[1],small),p('Hildesheim, '+datetime.fromisoformat(d['date']).strftime('%d.%m.%Y'),small),p(d['title'],title)]
    for item in d['sections']:
        if isinstance(item,str):story.append(p(item))
        elif item[0]=='h':story.append(p(item[1],heading))
        elif item[0]=='page':story.append(PageBreak())
        elif item[0]=='t':
            widths=item[2] if len(item)>2 else [495/len(item[1][0])]*len(item[1][0])
            t=Table([[p(v,small) for v in row] for row in item[1]],colWidths=widths,repeatRows=1,hAlign='LEFT')
            t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8edf0')),('GRID',(0,0),(-1,-1),.3,colors.HexColor('#c5cbd0')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            story.extend([t,Spacer(1,9)])
    story.append(KeepTogether([Spacer(1,8),p(d.get('signer','gez. '+sender[3])),p('Anlagen: '+('; '.join(d.get('attachments',[])) or 'keine'),small)]))
    SimpleDocTemplate(str(CASE/d['filename']),pagesize=A4,leftMargin=50,rightMargin=50,topMargin=96,bottomMargin=48,title=d['title'],author=AUTHOR,creator=AUTHOR).build(story,onFirstPage=frame,onLaterPages=frame)

def docx(d):
    d=written_norms(d)
    doc=Document();s=doc.sections[0];s.page_width=Cm(21);s.page_height=Cm(29.7);s.top_margin=Cm(1.6);s.bottom_margin=Cm(1.6);s.left_margin=Cm(1.8);s.right_margin=Cm(1.8)
    for style in doc.styles:
        if style.type==1:
            style.font.name='Times New Roman';style.font.size=Pt(11);style.font.color.rgb=RGBColor(0,0,0);style.paragraph_format.space_after=Pt(8)
            f=style.element.get_or_add_rPr().get_or_add_rFonts()
            for key in list(f.attrib):
                if key.endswith('Theme'):del f.attrib[key]
            for key in ('ascii','hAnsi','eastAsia','cs'):f.set(qn('w:'+key),'Times New Roman')
            for border in style.element.xpath('./w:pPr/w:pBdr'):border.getparent().remove(border)
    for name,size in [('Title',16),('Heading 1',12)]:
        doc.styles[name].font.size=Pt(size);doc.styles[name].font.bold=True;doc.styles[name].paragraph_format.space_before=Pt(10);doc.styles[name].paragraph_format.space_after=Pt(10)
    cp=doc.core_properties;cp.author=AUTHOR;cp.last_modified_by=AUTHOR;cp.title=d['title'];cp.language='de-DE';cp.created=datetime.fromisoformat(d['date']);cp.modified=cp.created
    sender=ACTORS[d['issuer']];recipient=ACTORS[d['recipient']]
    doc.add_paragraph(sender[0]).runs[0].bold=True;doc.add_paragraph(sender[1]+'\n'+sender[2]);doc.add_paragraph(recipient[0]+'\n'+recipient[1]);doc.add_paragraph('Hildesheim, '+datetime.fromisoformat(d['date']).strftime('%d.%m.%Y')+' · '+REF);doc.add_paragraph(d['title'],'Title')
    for item in d['sections']:
        if isinstance(item,str):doc.add_paragraph(item)
        elif item[0]=='h':doc.add_paragraph(item[1],'Heading 1')
        elif item[0]=='page':doc.add_page_break()
        elif item[0]=='t':
            table=doc.add_table(rows=0,cols=len(item[1][0]));table.style='Table Grid'
            for i,row in enumerate(item[1]):
                r=table.add_row();r._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
                if i==0:r._tr.get_or_add_trPr().append(OxmlElement('w:tblHeader'))
                for cell,value in zip(r.cells,row):
                    cell.text=str(value)
                    for p in cell.paragraphs:
                        for run in p.runs:run.font.size=Pt(10);run.bold=i==0
            doc.add_paragraph()
    doc.add_paragraph(d.get('signer','gez. '+sender[3]));doc.add_paragraph('Anlagen: '+('; '.join(d.get('attachments',[])) or 'keine'))
    foot=s.footer.paragraphs[0];foot.text=REF+' · Seite ';field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');foot._p.append(field)
    doc.save(CASE/d['filename'])

def eml(d):
    d=written_norms(d)
    sender=ACTORS[d['issuer']];recipient=ACTORS[d['recipient']];dt=datetime.fromisoformat(d['date']+'T10:24:00').replace(tzinfo=ZoneInfo('Europe/Berlin'))
    msg=EmailMessage(policy=policy.SMTP);msg['From']=Address(display_name=sender[3],addr_spec=sender[2]);msg['To']=Address(display_name=recipient[3],addr_spec=recipient[2]);msg['Date']=format_datetime(dt);msg['Subject']=REF+' / '+d['title'];msg['Message-ID']=f'<sw-hi-26-08.{d["number"]}.{d["date"]}@{sender[2].split("@")[1]}>';msg['Return-Path']=f'<{sender[2]}>';msg['Received']=f'from mail.{sender[2].split("@")[1]} by archiv.steinbogen-wohnen.example with ESMTP; {format_datetime(dt)}';msg['Content-Language']='de-DE'
    msg.set_content('Sehr geehrte Damen und Herren,\n\n'+_body_text(d)+'\n\nMit freundlichen Grüßen\n'+sender[3]+'\n'+sender[0]+'\n'+sender[1]+'\n'+sender[2]+'\n\nAnlagen: '+('; '.join(d.get('attachments',[])) or 'keine')+'\n',charset='utf-8')
    for name in d.get('attachments',[]):
        p=CASE/name
        if not p.is_file():raise FileNotFoundError(p)
        maintype,subtype=(mimetypes.guess_type(name)[0] or 'application/octet-stream').split('/',1);msg.add_attachment(p.read_bytes(),maintype=maintype,subtype=subtype,filename=name)
    (CASE/d['filename']).write_bytes(msg.as_bytes())

def build_records(records):
    CASE.mkdir(parents=True,exist_ok=True);ASSETS.mkdir(parents=True,exist_ok=True)
    for suffix in ('.pdf','.docx','.eml'):
        for d in records:
            if not d.get('plan') and Path(d['filename']).suffix==suffix:{'.pdf':pdf,'.docx':docx,'.eml':eml}[suffix](d)

record = dict
