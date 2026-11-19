"""Setzt Geschäftspost, Kontoauszüge und Arbeitsmappen der Böblinger Akte."""
from datetime import datetime
from email.message import EmailMessage
from email.policy import SMTP
from io import BytesIO
from pathlib import Path
import sys
from xml.sax.saxutils import escape
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo

import xlsxwriter
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfgen.canvas import Canvas

from falldaten import FIRMA, HAUS

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'scripts'))
from uferwerk_satz import register_fonts

def eur(value):
    return f"{value:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
def sheet(path, title, sections):
    """Jedes Blatt hat eigene Datenbreiten, Drucktitel und berechnete, gecachte Formeln."""
    book=xlsxwriter.Workbook(path)
    book.set_properties({'title':title, 'author':FIRMA,'created':datetime(2026,9,25,10)})
    header=book.add_format({'bold':1,'font_color':'#FFFFFF','bg_color':'#23575A','text_wrap':1,'valign':'vcenter'})
    caption=book.add_format({'bold':1,'font_size':16,'font_color':'#203F49'})
    note=book.add_format({'font_color':'#425560','text_wrap':1,'valign':'vcenter','font_size':10})
    cell=book.add_format({'text_wrap':1,'valign':'vcenter','bottom':1,'bottom_color':'#D9E2E4'})
    money=book.add_format({'num_format':'#,##0.00;[Red](#,##0.00);0.00','font_color':'#235A7B','valign':'vcenter','bottom':1,'bottom_color':'#D9E2E4'})
    calculated=book.add_format({'num_format':'#,##0.00;[Red](#,##0.00);0.00','font_color':'#184F35','bg_color':'#E7F0ED','valign':'vcenter'})
    for label,sub,columns,widths,rows in sections:
        sh=book.add_worksheet(label)
        sh.hide_gridlines(2);sh.freeze_panes(4,1);sh.set_landscape();sh.set_paper(9);sh.fit_to_pages(1,0)
        sh.set_margins(.35,.35,.52,.52);sh.set_header('&LAutohaus Schönbuchring GmbH&RControlling · Böblingen')
        sh.set_footer('&LBelegauszug · Beträge in EUR&RSeite &P / &N');sh.repeat_rows(0,3)
        sh.merge_range(0,0,0,len(columns)-1,title,caption);sh.set_row(0,27)
        sh.merge_range(1,0,1,len(columns)-1,sub,note);sh.set_row(1,36)
        for j,(name,width) in enumerate(zip(columns,widths)):
            sh.set_column(j,j,width);sh.write(3,j,name,header)
        sh.set_row(3,32)
        for i,row in enumerate(rows,4):
            assert len(row)==len(columns)
            sh.set_row(i,24 if label in {"13 Wochen", "Anschluss"} else 33)
            for j,v in enumerate(row):
                if isinstance(v,tuple) and v[0].startswith('='):sh.write_formula(i,j,v[0],calculated,v[1])
                elif isinstance(v,(int,float)):sh.write_number(i,j,v,money)
                else:sh.write(i,j,v,cell)
        sh.print_area(0,0,3+len(rows),len(columns)-1)
    book.close()

def letter(path,issuer,unit,recipient,when,reference,title,paragraphs,rows=None):
    register_fonts()
    palette = '#1B5954' if issuer==FIRMA else ('#334F71' if 'bank' in issuer.lower() else '#754738')
    style=lambda n,size,font='TNR':ParagraphStyle(n,fontName=font,fontSize=size,leading=size*1.35,spaceAfter=6,textColor=colors.HexColor('#203640'))
    body=style('Inhalt',11);meta=style('Meta',9,'Helvetica');head=style('Titel',18,'Helvetica-Bold')
    def par(s,sty=body):return Paragraph(escape(s).replace('\n','<br/>'),sty)
    def decor(c,doc):
        c.saveState();c.setFillColor(colors.HexColor(palette));c.rect(0,786,A4[0],56,fill=1,stroke=0)
        c.setFillColor(colors.white);c.setFont('Helvetica-Bold',15);c.drawString(46,815,issuer)
        c.setFont('Helvetica',9);c.drawString(46,798,unit)
        c.setStrokeColor(colors.HexColor('#C7D7D6'));c.line(46,48,548,48)
        c.setFillColor(colors.HexColor('#425B63'));c.setFont('Helvetica',8)
        c.drawString(46,32,reference);c.drawRightString(548,32,f'{when}    |    {doc.page}');c.restoreState()
    story=[par(recipient,meta),Spacer(1,10),par(when+'   ·   '+reference,meta),par(title,head),Spacer(1,8)]
    story.extend(par(p) for p in paragraphs)
    if rows:
        sty=style('Zeile',9)
        render=[[par(str(v),sty) for v in row] for row in rows]
        widths={2:[.69,.31],3:[.20,.56,.24],4:[.16,.48,.17,.19]}[len(rows[0])]
        tbl=Table(render,colWidths=[502*w for w in widths],repeatRows=1)
        tbl.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#CEDCDE')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F0F4F3')]),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5)]))
        story.append(tbl)
    doc=SimpleDocTemplate(str(path),pagesize=A4,leftMargin=46,rightMargin=46,topMargin=75,bottomMargin=61,title=title,author=issuer)
    doc.build(story,onFirstPage=decor,onLaterPages=decor,canvasmaker=lambda *a,**kw: Canvas(*a,**{**kw,'invariant':1}))

def word(path,issuer,sub,title,ref,sections,signature):
    doc=Document();sec=doc.sections[0];sec.left_margin=Cm(2.4);sec.right_margin=Cm(2.1);sec.top_margin=Cm(2.1)
    norm=doc.styles['Normal'];norm.font.name='Times New Roman';norm.font.size=Pt(11);norm.paragraph_format.space_after=Pt(5)
    hp=sec.header.paragraphs[0];r=hp.add_run(issuer);r.bold=True;r.font.name='Arial';r.font.color.rgb=RGBColor.from_string('205E62')
    hp.add_run('     |     '+sub).font.size=Pt(9)
    sec.footer.paragraphs[0].add_run(ref).font.size=Pt(9)
    doc.add_paragraph(ref);doc.add_paragraph(title,style='Title')
    for heading,para in sections:
        doc.add_paragraph(heading,style='Heading 2');doc.add_paragraph(para)
    doc.add_paragraph(signature)
    doc.core_properties.author=issuer;doc.core_properties.title=title
    doc.core_properties.modified=doc.core_properties.created=datetime(2026,9,25,9)
    buf=BytesIO();doc.save(buf)
    with ZipFile(buf) as src,ZipFile(path,'w',ZIP_DEFLATED) as out:
        for item in src.infolist():
            info=ZipInfo(item.filename,(2026,9,25,9,0,0));out.writestr(info,src.read(item),compress_type=ZIP_DEFLATED)

def mail(path,when,frm,to,subject,text,attachment=None,reply=None):
    msg=EmailMessage(policy=SMTP)
    msg['From']=frm; msg['To']=to; msg['Subject']=subject;msg['Date']=datetime.fromisoformat(when)
    msg['Message-ID']='<'+path.stem.split('_')[0].lower()+'.sr26@schoenbuchring.example>'
    if reply:msg['In-Reply-To']=reply
    msg.set_content(text)
    if attachment:
        msg.add_attachment(attachment.read_bytes(),maintype='text',subtype='csv',filename=attachment.name)
        msg.set_boundary('sr26-geldverkehr-'+path.stem.split('_')[0])
    path.write_bytes(msg.as_bytes())
