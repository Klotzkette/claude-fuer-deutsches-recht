"""Fortlaufender Kanzleisatz für die Weserfunken-Schriftsätze.

Die Gliederung stammt aus der Dokumentquelle. Kein Versandweg wird aus der
Empfängerrolle abgeleitet. Verträge und historische Anlagen verwenden weiterhin
ihren vorhandenen, gesonderten Satz.
"""
from __future__ import annotations
import os
import re
import json
import zipfile
import io
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from pypdf import PdfReader
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, NextPageTemplate, Paragraph, Spacer, KeepTogether, PageBreak

FONT='WeserKanzleiTimes'
MARGIN=56.7
WIDTH=A4[0]-2*MARGIN


def fonts():
    roots=([Path(os.environ['AKTEN_FONT_DIR'])] if os.environ.get('AKTEN_FONT_DIR') else [])+[
        Path('/System/Library/Fonts/Supplemental'),Path('/usr/share/fonts/truetype/msttcorefonts')]
    variants={'':('Times New Roman.ttf','times.ttf'),'Bold':('Times New Roman Bold.ttf','timesbd.ttf'),
              'Italic':('Times New Roman Italic.ttf','timesi.ttf'),'BoldItalic':('Times New Roman Bold Italic.ttf','timesbi.ttf')}
    for suffix,names in variants.items():
        path=next((r/n for r in roots for n in names if (r/n).is_file()),None)
        if path is None:raise RuntimeError('Lizenzierte Times-New-Roman-TTFs für den Schriftsatzsatz fehlen; AKTEN_FONT_DIR setzen')
        pdfmetrics.registerFont(TTFont(FONT+suffix,str(path)))
    pdfmetrics.registerFontFamily(FONT,normal=FONT,bold=FONT+'Bold',italic=FONT+'Italic',boldItalic=FONT+'BoldItalic')


def sender(document,case):
    s=case[document.get('sender','defence_firm')]
    if document.get('sender')=='administrator':
        return {'brand':'TETTENBORN','sub':'RECHTSANWÄLTIN · INSOLVENZVERWALTUNG','person':'Kunigunde von Tettenborn',
                'firm':s['firm'],'address':s['address'],'email':s['email'],'ref':s['reference'],'color':'#29483D'}
    return {'brand':'RADEMACHER WESTHOFF','sub':'RECHTSANWÄLTE PartG mbB','person':s['lawyer'],
            'firm':s['name'],'address':s['address'],'email':s['email'],'ref':s['reference'],'color':'#29445A'}


def sections(document):
    for item in document['pages']:
        head=item['heading']
        if not re.match(r'^\d+(?:\.\d+)* [^\n]+$',head):raise ValueError('Dezimale Schriftsatzüberschrift erforderlich: '+head)
        yield head, item.get('paragraphs',[])


def date_text(document):return datetime.fromisoformat(document['date']).strftime('%d.%m.%Y')


class PaginationCanvas(Canvas):
    def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs);self.saved=[]
    def showPage(self):self.saved.append(dict(self.__dict__));self._startPage()
    def save(self):
        total=len(self.saved)
        for state in self.saved:
            self.__dict__.update(state)
            self.setFont(FONT,8.5);self.setFillColor(HexColor('#444444'))
            self.drawRightString(A4[0]-MARGIN,31,f'Seite {self._pageNumber} von {total}')
            Canvas.showPage(self)
        Canvas.save(self)


def pdf(document,case,target):
    fonts();s=sender(document,case)
    styles={
        'body':ParagraphStyle('Body',fontName=FONT,fontSize=11,leading=15.5,spaceAfter=9,allowWidows=0,allowOrphans=0),
        'small':ParagraphStyle('Small',fontName=FONT,fontSize=9,leading=12,spaceAfter=5),
        'title':ParagraphStyle('Title',fontName=FONT+'Bold',fontSize=19,leading=23,spaceBefore=15,spaceAfter=17),
        'h1':ParagraphStyle('H1',fontName=FONT+'Bold',fontSize=13,leading=17,spaceBefore=17,spaceAfter=11,keepWithNext=True),
        'h2':ParagraphStyle('H2',fontName=FONT+'Bold',fontSize=11.5,leading=15.5,spaceBefore=12,spaceAfter=10,keepWithNext=True),
        'role':ParagraphStyle('Role',fontName=FONT+'Bold',fontSize=10,leading=13,spaceBefore=7,spaceAfter=5),
    }
    def p(text,key='body'):return Paragraph(escape(text).replace('\n','<br/>'),styles[key])
    def page(canvas,doc):
        canvas.saveState();canvas.setFillColor(HexColor(s['color']))
        if doc.page==1:
            canvas.setFont(FONT+'Bold',22 if document.get('sender')=='administrator' else 18)
            canvas.drawString(MARGIN,790,s['brand'])
            canvas.setFont(FONT,9);canvas.drawString(MARGIN,773,s['sub'])
            canvas.setStrokeColor(HexColor(s['color']));canvas.setLineWidth(1.2);canvas.line(MARGIN,760,A4[0]-MARGIN,760)
            canvas.setFillColor(HexColor('#333333'));canvas.setFont(FONT,9)
            canvas.drawString(MARGIN,743,s['person']+' · '+s['address'])
            canvas.drawString(MARGIN,729,s['email'])
        else:
            canvas.setFont(FONT+'Bold',10);canvas.drawString(MARGIN,800,s['firm'])
            canvas.setFillColor(HexColor('#444444'));canvas.setFont(FONT,9)
            canvas.drawRightString(A4[0]-MARGIN,800,document['reference']+' | '+date_text(document))
        canvas.setFillColor(HexColor('#444444'));canvas.setFont(FONT,8.5)
        canvas.drawString(MARGIN,31,s['ref']+' · '+document['title'])
        canvas.restoreState()
    doc=BaseDocTemplate(str(target),pagesize=A4,leftMargin=MARGIN,rightMargin=MARGIN,
        topMargin=126,bottomMargin=57,title=document['title'],author=s['person'],creator='Klotzkette',invariant=1)
    doc.addPageTemplates([
        PageTemplate(id='First',frames=[Frame(MARGIN,57,WIDTH,650,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page),
        PageTemplate(id='Later',frames=[Frame(MARGIN,57,WIDTH,718,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page)])
    story=[NextPageTemplate('Later'),p(document['recipient']),Spacer(1,9),
           p(f"Bremen, {date_text(document)}\nUnser Zeichen: {s['ref']}\nGerichtliches Aktenzeichen: {document['reference']}",'small'),p(document['title'],'title')]
    if document.get('transmission'):story.insert(1,p(document['transmission'],'small'))
    for party in document.get('rubrum',[]):
        story.append(KeepTogether([p(party['role'],'role'),p('\n'.join(party['lines']))]))
    story.extend(p(x) for x in document.get('intro',[]))
    if document.get('rubrum'):story.append(PageBreak())
    for head,paras in sections(document):
        level=len(head.split(' ',1)[0].split('.'))
        story.append(p(head,'h1' if level==1 else 'h2'))
        story.extend(KeepTogether([p(text)]) if head.startswith('1.') else p(text) for text in paras)
    if document.get('signature'):
        story.append(KeepTogether([Spacer(1,14),p('\n'.join(document['signature']))]))
    doc.build(story,canvasmaker=PaginationCanvas)
    return len(PdfReader(target).pages)


def docx(document,case,target):
    s=sender(document,case);doc=Document();sec=doc.sections[0]
    sec.page_width,sec.page_height=Cm(21),Cm(29.7)
    sec.top_margin,sec.bottom_margin=Cm(2.45),Cm(2.1)
    sec.left_margin=sec.right_margin=Cm(2)
    sec.header_distance=Cm(1);sec.footer_distance=Cm(1.1);sec.different_first_page_header_footer=True
    for st in doc.styles:
        if st.type!=1:continue
        st.font.name='Times New Roman';st.font.size=Pt(11);st.font.color.rgb=RGBColor(0,0,0)
        st.paragraph_format.space_after=Pt(9);st.paragraph_format.line_spacing=1.15
        st.paragraph_format.widow_control=True
        fonts=st.element.get_or_add_rPr().get_or_add_rFonts()
        for key in list(fonts.attrib):
            if key.endswith('Theme'):del fonts.attrib[key]
        for key in ('ascii','hAnsi','eastAsia','cs'):fonts.set(qn('w:'+key),'Times New Roman')
        for el in st.element.xpath('./w:pPr/w:pBdr'):el.getparent().remove(el)
    doc.styles['Title'].font.size=Pt(19);doc.styles['Title'].font.bold=True
    for key,size in [('Heading 1',13),('Heading 2',11.5),('Heading 3',11)]:
        st=doc.styles[key];st.font.size=Pt(size);st.font.bold=True
        st.paragraph_format.space_before=Pt(14 if key=='Heading 1' else 10)
        st.paragraph_format.space_after=Pt(10);st.paragraph_format.keep_with_next=True
    header=sec.header.paragraphs[0];header.text=s['firm']+' | '+document['reference']
    for r in header.runs:r.font.size=Pt(9)
    for footer in [sec.first_page_footer,sec.footer]:
        p=footer.paragraphs[0];p.text=s['ref']+' · '+document['title']+'\tSeite '
        p.paragraph_format.tab_stops.add_tab_stop(Cm(14.5))
        for code in ['PAGE','NUMPAGES']:
            if code=='NUMPAGES':p.add_run(' von ')
            field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),code);p._p.append(field)
        for r in p.runs:r.font.size=Pt(8.5)
    # The first-page letterhead is body content so that it cannot collide with a long address.
    brand=doc.add_paragraph();r=brand.add_run(s['brand']);r.bold=True;r.font.size=Pt(18)
    brand.paragraph_format.space_after=Pt(4)
    sub=doc.add_paragraph(s['sub']);sub.paragraph_format.space_after=Pt(9)
    for r in sub.runs:r.font.size=Pt(9)
    contact=doc.add_paragraph(s['person']+' · '+s['address']+'\n'+s['email'])
    contact.paragraph_format.space_after=Pt(20)
    for r in contact.runs:r.font.size=Pt(9)
    if document.get('transmission'):doc.add_paragraph(document['transmission'])
    doc.add_paragraph(document['recipient'])
    meta=doc.add_paragraph(f"Bremen, {date_text(document)}\nUnser Zeichen: {s['ref']}\nGerichtliches Aktenzeichen: {document['reference']}")
    for r in meta.runs:r.font.size=Pt(9)
    doc.add_paragraph(document['title'],'Title')
    for party in document.get('rubrum',[]):
        p=doc.add_paragraph();p.add_run(party['role']).bold=True;p.paragraph_format.keep_with_next=True
        doc.add_paragraph('\n'.join(party['lines']))
    for x in document.get('intro',[]):doc.add_paragraph(x)
    for head,paras in sections(document):
        level=min(len(head.split(' ',1)[0].split('.')),3)
        heading=doc.add_paragraph(head,f'Heading {level}')
        if document.get('rubrum') and head.startswith('1 '):heading.paragraph_format.page_break_before=True
        for x in paras:
            paragraph=doc.add_paragraph(x)
            if head.startswith('1.'):paragraph.paragraph_format.keep_together=True
    if document.get('signature'):
        # Never leave a signature alone on an otherwise empty last page.
        doc.paragraphs[-1].paragraph_format.keep_with_next=True
        doc.paragraphs[-1].paragraph_format.keep_together=True
        p=doc.add_paragraph('\n'.join(document['signature']));p.paragraph_format.space_before=Pt(14);p.paragraph_format.keep_together=True
    cp=doc.core_properties;cp.author=cp.last_modified_by='Klotzkette';cp.title=document['title'];cp.language='de-DE'
    cp.created=cp.modified=datetime.fromisoformat(document['date'])
    doc.save(target)
    normalize_docx(target, document['date'])
    return target


def normalize_docx(path, date):
    stamp=(*datetime.fromisoformat(date).timetuple()[:3],12,0,0)
    source=path.read_bytes();out=io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(source)) as original, zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as dest:
        for info in original.infolist():
            info.date_time=stamp
            dest.writestr(info,original.read(info.filename))
    path.write_bytes(out.getvalue())


def approved_original_hashes(baseline):
    """Historische SHA-Guards nur um einzeln dokumentierte Satzänderungen ergänzen."""
    expected=json.loads(baseline.read_text())
    migration=json.loads((baseline.parent/'satz-migration-2026-11.json').read_text())
    for name,item in migration['files'].items():
        if name not in expected:continue
        if expected[name]!=item['before_sha256']:
            raise ValueError('Satzmigration passt nicht zum historischen Bestand: '+name)
        expected[name]=item['after_sha256']
    return expected
