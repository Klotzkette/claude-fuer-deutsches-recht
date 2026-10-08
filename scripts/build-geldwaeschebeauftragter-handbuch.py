#!/usr/bin/env python3
"""Die geprüften Skills und die Werkstatt unverändert in lesbare A4-PDFs setzen.

Python: reportlab, pypdf. Keine künstlichen Seitenumbrüche in den Skilltexten.
"""
import argparse,hashlib,html,json,re,unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,LongTable,TableStyle
from pypdf import PdfReader,PdfWriter
ROOT=Path(__file__).resolve().parents[1]
LINK_BASE='https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/'

def text_tokens(s):
    return Counter(re.findall(r'[\w§]+',unicodedata.normalize('NFKC',s).casefold()))

def inline(s):
    # Render source text; hyperlink target remains clickable without printing a long URL.
    stash=[]
    def link(m):
        label,url=m.groups()
        if not re.match(r'^https?://',url):url=urljoin(LINK_BASE,url)
        stash.append('<a color="#174a60" href="'+html.escape(url,quote=True)+'">'+html.escape(label)+'</a>')
        return f'LINKTOKEN{len(stash)-1}ENDTOKEN'
    s=re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)',link,s)
    s=html.escape(s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
    s=re.sub(r'`([^`]+)`',r'\1',s)
    for i,v in enumerate(stash):s=s.replace(f'LINKTOKEN{i}ENDTOKEN',v)
    return s

FONT_FILES={'times-new-roman':('Times New Roman','Times New Roman.ttf','Times New Roman Bold.ttf','Times New Roman Italic.ttf','Times New Roman Bold Italic.ttf'),
            'liberation-serif':('Liberation Serif (metrisch kompatibel zu Times New Roman)','LiberationSerif-Regular.ttf','LiberationSerif-Bold.ttf','LiberationSerif-Italic.ttf','LiberationSerif-BoldItalic.ttf')}
FONT_LABEL='Times New Roman'

def setup(fontdir,family='times-new-roman'):
    """Registriert die Schriftfamilie unter dem internen Namen TNR; die tatsächlich verwendete Schrift wird im Bericht ausgewiesen."""
    global FONT_LABEL
    label,*files=FONT_FILES[family];FONT_LABEL=label
    for name,file in zip(['TNR','TNR-Bold','TNR-Italic','TNR-BoldItalic'],files):
        pdfmetrics.registerFont(TTFont(name,str(fontdir/file)))
    pdfmetrics.registerFontFamily('TNR',normal='TNR',bold='TNR-Bold',italic='TNR-Italic',boldItalic='TNR-BoldItalic')


def render(source,target):
    global LINK_BASE
    LINK_BASE='https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/'+source.parent.relative_to(ROOT).as_posix()+'/'
    source_text=source.read_text();body=re.sub(r'^---\n.*?\n---\s*','',source_text,flags=re.S)
    lines=body.splitlines();title=next(x.lstrip('# ').strip() for x in lines if x.startswith('# '))
    styles={0:ParagraphStyle('Body',fontName='TNR',fontSize=11,leading=14.3,spaceAfter=6,alignment=TA_LEFT,splitLongWords=True,allowWidows=0,allowOrphans=0)}
    for level,size in [(1,17),(2,13),(3,11.5),(4,11)]:
        styles[level]=ParagraphStyle('H'+str(level),parent=styles[0],fontName='TNR-Bold',fontSize=size,leading=size+3,spaceBefore=9 if level>1 else 0,spaceAfter=7,keepWithNext=True)
    cell=ParagraphStyle('Cell',parent=styles[0],spaceAfter=0,leading=13.5)
    elements=[];expected=[]
    def para(s,level=0):
        p=Paragraph(inline(s),styles.get(level,styles[4]));plain=p.getPlainText()
        missing={c for c in plain if not c.isspace() and ord(c) not in pdfmetrics.getFont('TNR').face.charToGlyph}
        if missing:raise ValueError('Schrift unterstützt Zeichen nicht: '+repr(missing))
        expected.append(plain);return p
    i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('```'):
            i+=1
            while i<len(lines) and not lines[i].strip().startswith('```'):
                if lines[i].strip():elements.append(para(lines[i]))
                i+=1
            i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                l=lines[i].strip();i+=1
                if re.fullmatch(r'[|:\-\s]+',l):continue
                values=[x.strip() for x in l.strip('|').split('|')];ps=[]
                for v in values:
                    p=Paragraph(inline(v),cell);expected.append(p.getPlainText());ps.append(p)
                rows.append(ps)
            n=max(map(len,rows));rows=[r+['']*(n-len(r)) for r in rows]
            widths=[(A4[0]-120)/n]*n
            if n==3 and all(isinstance(r[0],Paragraph) and r[0].getPlainText().isdigit() for r in rows[1:]):widths=[28,(A4[0]-148)/2,(A4[0]-148)/2]
            table=LongTable(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),HexColor('#eaf0f2')),('LINEBELOW',(0,0),(-1,0),.5,HexColor('#80939a')),('LINEBELOW',(0,1),(-1,-1),.25,HexColor('#cad4d8')),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            elements.extend([table,Spacer(1,7)]);continue
        m=re.match(r'^(#{1,6})\s+(.+)',line)
        if m:elements.append(para(m.group(2),min(len(m.group(1)),4)));i+=1;continue
        if re.match(r'^[-*]\s+',line):elements.append(para('• '+line[2:]));i+=1;continue
        if re.match(r'^\d+\.\s+',line):elements.append(para(line));i+=1;continue
        if re.fullmatch(r'[-=_]{3,}',line):i+=1;continue
        chunk=[line.lstrip('> ')];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||```|[-*] |\d+\. )',lines[i].strip()):
            chunk.append(lines[i].strip().lstrip('> '));i+=1
        elements.append(para(' '.join(chunk)))
    slug=source.parent.name
    def page(c,doc):
        c.saveState();c.setFont('TNR',9);c.setFillColor(HexColor('#52616a'))
        c.drawString(60,A4[1]-32,'Geldwäschebeauftragter | '+slug)
        c.drawString(60,30,'Stand: 8. Oktober 2026 | Quellen jeweils am konkreten Fall prüfen')
        c.drawRightString(A4[0]-60,30,str(doc.page));c.restoreState()
    doc=SimpleDocTemplate(str(target),pagesize=A4,leftMargin=60,rightMargin=60,topMargin=53,bottomMargin=52,title=title,author='Klotzkette',subject='Geldwäschebeauftragter – ausführlicher Skill',invariant=1)
    doc.build(elements,onFirstPage=page,onLaterPages=page)
    reader=PdfReader(target)
    body_pages=[]
    for number,page_obj in enumerate(reader.pages,1):
        ls=(page_obj.extract_text() or '').splitlines()
        assert ls[0]=='Geldwäschebeauftragter | '+slug and ls[2]==str(number),(slug,number,'header/footer extraction')
        body_pages.append(' '.join(ls[3:]))
    normalize=lambda x: ''.join(re.findall(r'[\w§]+',unicodedata.normalize('NFKC',x).casefold()))
    extracted=normalize(' '.join(body_pages));cursor=0
    for segment in expected:
        segment=normalize(segment)
        if not segment:continue
        found=extracted.find(segment,cursor)
        if found<0:raise ValueError(f'{slug}: Textabschnitt fehlt oder Reihenfolge abweichend: {segment[:100]}')
        cursor=found+len(segment)
    return {'skill':slug,'title':title,'source':source.relative_to(ROOT).as_posix(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'words':len(re.findall(r'\S+',body)),'utf8_bytes':len(source.read_bytes()),'pages':len(reader.pages),'pdf':target.name,'pdf_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'body_text_coverage':'all rendered source text segments present in source order'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True,type=Path);args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    tnr=Path('/System/Library/Fonts/Supplemental')
    if (tnr/'Times New Roman.ttf').exists(): setup(tnr)
    else: setup(Path('/usr/share/fonts/truetype/liberation2'),'liberation-serif')
    rows=[]
    for source in sorted((ROOT/'geldwaeschebeauftragter/skills').glob('*/SKILL.md')):
        rows.append(render(source,args.out/(source.parent.name+'.pdf')))
    writer=PdfWriter()
    for row in rows:writer.append(args.out/row['pdf'],outline_item=row['title'])
    target=args.out/'geldwaeschebeauftragter-skills-handbuch.pdf';writer.add_metadata({'/Title':'Geldwäschebeauftragter: elf Arbeitsabläufe','/Author':'Klotzkette'});writer.write(target)
    workshop=render(ROOT/'geldwaeschebeauftragter/geldwaeschebeauftragter-werkstatt.md',args.out/'geldwaeschebeauftragter-werkstatt-lesefassung.pdf')
    report={'date':'2026-10-08','font':FONT_LABEL,'skills':rows,'skill_count':len(rows),'handbook_pages':len(PdfReader(target).pages),'workshop':workshop}
    (args.out/'umfang.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'skills':len(rows),'handbook_pages':report['handbook_pages'],'workshop_pages':workshop['pages']},ensure_ascii=False))
if __name__=='__main__':main()
