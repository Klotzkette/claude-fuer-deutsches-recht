"""Lesbare VVT-Arbeitsmappenansicht ohne Spalten- oder Textkürzung."""
from pathlib import Path
from html import escape
import io
from openpyxl import load_workbook
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def render(path):
    book = load_workbook(path, data_only=False)
    font_dir = Path('/System/Library/Fonts/Supplemental')
    regular, bold = font_dir/'Times New Roman.ttf', font_dir/'Times New Roman Bold.ttf'
    label = 'Times New Roman'
    if not regular.exists():
        font_dir=Path('/usr/share/fonts/truetype/liberation2')
        regular,bold=font_dir/'LiberationSerif-Regular.ttf',font_dir/'LiberationSerif-Bold.ttf'
        label='Liberation Serif als Ersatz für Times New Roman'
    pdfmetrics.registerFont(TTFont('VVT-Regular',str(regular)))
    pdfmetrics.registerFont(TTFont('VVT-Bold',str(bold)))
    pdfmetrics.registerFontFamily('VVT-Regular',normal='VVT-Regular',bold='VVT-Bold',italic='VVT-Regular',boldItalic='VVT-Bold')
    body=ParagraphStyle('body',fontName='VVT-Regular',fontSize=11,leading=14,spaceAfter=5,splitLongWords=True)
    heading=ParagraphStyle('heading',parent=body,fontName='VVT-Bold',fontSize=13,spaceBefore=12,spaceAfter=6,keepWithNext=True)
    small=ParagraphStyle('small',parent=body,fontSize=9,leading=12)
    story=[Paragraph(escape(Path(path).stem),heading),Paragraph('Lesbare Druckansicht der Arbeitsmappe. Zellkoordinaten ordnen jeden Wert dem bearbeitbaren Original zu; auch ausgeblendete technische Angaben werden vollständig dokumentiert.',body)]
    for index,sheet in enumerate(book,1):
        story.append(Paragraph(f'{index}. {escape(sheet.title)}',heading))
        for row in sheet:
            cells=[cell for cell in row if cell.value is not None]
            if not cells:continue
            for cell in cells:
                value=cell.value.isoformat() if hasattr(cell.value,'isoformat') else str(cell.value)
                story.append(Paragraph(f'<b>{escape(cell.coordinate)}</b>  '+escape(value).replace('\n','<br/>'),body))
            story.append(Spacer(1,4))
    buffer=io.BytesIO()
    def footer(canvas,doc):
        canvas.setFont('VVT-Regular',8)
        canvas.drawString(48,25,label+' 11 pt')
        canvas.drawRightString(A4[0]-48,25,str(doc.page))
    SimpleDocTemplate(buffer,pagesize=A4,leftMargin=48,rightMargin=48,topMargin=42,bottomMargin=44,invariant=1,title=Path(path).stem).build(story,onFirstPage=footer,onLaterPages=footer)
    return buffer.getvalue()
