#!/usr/bin/env python3
"""Baut das synthetische Prüfbeispiel mit Vorschau, Fehlerexport und Kontrollfassung."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'compliance-hameln-auskunft-mit-schwaerzungen'
CASE = ROOT / 'testakten' / SLUG
DEBRIEF = ROOT / 'quality/hameln-compliance/nachbesprechung'
INK = HexColor('#1A2B35')
MUTED = HexColor('#425C6A')
TEAL = HexColor('#147D79')
PANEL = HexColor('#EAF2F4')
RED = HexColor('#9F262C')
RED_PALE = HexColor('#FBE4E4')
WIDTH, HEIGHT = A4
LEFT = 49
BODY = WIDTH - 2 * LEFT

CUSTOMER = 'Mara Lindhorst'
THIRD_NAME = 'Jonas Evers'
THIRD_PHONE = '05151 000 0187'
RECIPIENT = 'Okerquell Prüftechnik GmbH'
NOTE = (
    'Mara Lindhorst meldete am 19.10.2026 einen Aussetzer nach der',
    'Sicherheitsabschaltung. Servicestatus am 20.10.2026 irrtümlich',
    'auf „Kundin nicht erreichbar“ gesetzt.',
)


def text(pdf, x, y, value, size=11, color=INK, bold=False):
    pdf.setFillColor(color)
    pdf.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    pdf.drawString(x, y, value)


def start(path, title, status, subtitle, *, warning=False):
    pdf = Canvas(str(path), pagesize=A4, invariant=1, pageCompression=1)
    pdf.setTitle(title)
    pdf.setAuthor('Merrensteg Elektrosysteme SE')
    pdf.setSubject('ME-36 | Datenschutzservice Hameln')
    pdf.setFillColor(INK)
    pdf.rect(0, HEIGHT - 64, WIDTH, 64, fill=1, stroke=0)
    text(pdf, LEFT, HEIGHT - 36, 'MERRENSTEG  /  ELEKTROSYSTEME', 15, white, True)
    text(pdf, LEFT, HEIGHT - 51, 'DATENSCHUTZ UND SERVICE     ·     HAMELN', 8, white)
    pdf.setFillColor(RED_PALE if warning else PANEL)
    pdf.roundRect(LEFT, 717, BODY, 29, 5, fill=1, stroke=0)
    text(pdf, LEFT + 13, 727, status, 9.5, RED if warning else TEAL, True)
    text(pdf, LEFT, 680, title, 26, INK, True)
    text(pdf, LEFT, 655, subtitle, 10.5, MUTED)
    pdf.setStrokeColor(PANEL)
    pdf.line(LEFT, 55, WIDTH - LEFT, 55)
    text(pdf, LEFT, 37, 'ME-36   /   DSAR-2026-036   /   Arbeitsakte Hameln', 8.5, MUTED)
    text(pdf, WIDTH - LEFT - 33, 37, '01 / 01', 8.5, MUTED)
    return pdf


def label(pdf, number, title, y):
    text(pdf, LEFT, y, number, 10, TEAL, True)
    text(pdf, LEFT + 25, y, title, 13, INK, True)


def lines(pdf, y, values, x=LEFT + 25):
    for value in values:
        text(pdf, x, y, value)
        y -= 17


def marked(pdf, y, value):
    pdf.setFillColor(RED_PALE)
    pdf.roundRect(LEFT + 19, y - 4, BODY - 38, 17, 3, fill=1, stroke=0)
    text(pdf, LEFT + 25, y, value, 11, RED)


def black_bar(pdf, y, width):
    pdf.setFillColor(INK)
    pdf.rect(LEFT + 25, y - 3, width, 13, fill=1, stroke=0)


def crm(pdf, mode):
    label(pdf, '01', 'Auszug aus der Serviceakte SV-41782', 605)
    lines(pdf, 578, (f'Kundin: {CUSTOMER}   ·   K-60418', 'Datensatz: Bearbeitungsnotiz im Service-CRM'))
    for y, value in zip((529, 512, 495), NOTE):
        if mode == 'preview':
            marked(pdf, y, value)
        else:
            text(pdf, LEFT + 25, y, value)
    lines(pdf, 466, ('Servicestatus am 22.10.2026 berichtigt.',))
    label(pdf, '02', 'Mitgeführter Kontakt aus einem anderen Ticket', 413)
    for y, value, width in ((386, THIRD_NAME, 108), (365, THIRD_PHONE, 125)):
        if mode == 'preview':
            marked(pdf, y, value)
        elif mode == 'overlay':
            text(pdf, LEFT + 25, y, value)
            black_bar(pdf, y, width)
        else:
            black_bar(pdf, y, width)
    label(pdf, '03', 'Belegte Datenweitergabe', 301)
    lines(pdf, 273, (f'21.10.2026   ·   {RECIPIENT}', 'Versandt wurde ein Auszug zum Servicevorgang SV-41782.'))
    if mode == 'preview':
        label(pdf, '04', 'Status im Pilot', 210)
        lines(pdf, 184, ('Rot zeigt einen Vorschlag für die interne Sichtung.',
                         'Den Vorschlag, seinen Umfang und mögliche Fehlstellen einzeln prüfen.',
                         'Bildbeilage und weitere Dateiformate in die Prüfung einbeziehen.'))
    elif mode == 'overlay':
        label(pdf, '04', 'Exporteinstellung im Pilot', 210)
        lines(pdf, 184, ('Option „PDF mit visueller Abdeckung“ ausgewählt.',
                         'Zur Abnahme die Datei als eigenständigen Export prüfen.'))
    else:
        label(pdf, '04', 'Hinweis zum Auszug', 210)
        lines(pdf, 184, ('Der Auszug wahrt den Zusammenhang Ihrer Bearbeitungshistorie.',
                         'Angaben aus dem mitgeführten fremden Ticket wurden ausgeblendet.',
                         'Dieser Auszug ist ein Teilstück für die Nachbesprechung.'))
    pdf.save()


def photo_card():
    # The scan deliberately consists of pixels. No OCR layer is added.
    image = Image.new('RGB', (1200, 440), '#e6ecec')
    draw = ImageDraw.Draw(image)
    label_font = ImageFont.load_default(size=25)
    big_font = ImageFont.load_default(size=38)
    draw.rounded_rectangle((34, 29, 1166, 411), radius=16, fill='#f9faf8', outline='#a5b2b3', width=3)
    draw.rounded_rectangle((75, 86, 345, 350), radius=13, fill='#c8dadb')
    draw.ellipse((153, 117, 267, 231), fill='#58858b')
    draw.rounded_rectangle((118, 236, 304, 331), radius=39, fill='#58858b')
    draw.text((392, 88), 'WERKSTATTZUGANG  /  BESUCHERAUSWEIS', font=label_font, fill='#385660')
    draw.text((392, 151), THIRD_NAME, font=big_font, fill='#1a2b35')
    draw.text((392, 225), 'Ausweis WK-12-774  ·  Platz B-14', font=label_font, fill='#1a2b35')
    draw.text((392, 279), 'Sichtprüfung am 21.10.2026', font=label_font, fill='#385660')
    return image


def build():
    CASE.mkdir(parents=True, exist_ok=True)
    DEBRIEF.mkdir(parents=True, exist_ok=True)
    crm(start(CASE / '09_KI_Pruefansicht.pdf', 'Vorschau mit roten Markierungen',
              'INTERN   /   KI-VORSCHLÄGE UNGEPRÜFT', 'Klarblende Pilot 0.8   ·   Auszug aus dem Sichtungslauf vom 10.11.2026',
              warning=True), 'preview')
    crm(start(CASE / '10_Exportkandidat_Sperren.pdf', 'Export zur technischen Abnahme',
              'GESPERRT   /   TRAININGSEXPORT', 'Klarblende Pilot 0.8   ·   Test der Funktion „Visuelle Abdeckung“',
              warning=True), 'overlay')

    pdf = start(CASE / '11_Gescannte_Fremdbeilage.pdf', 'Beilage zum Sammel-Scan',
                'INTERN   /   SCAN OHNE TEXTSCHICHT', 'Anlage aus dem geteilten Servicepostfach, Eingang vom 21.10.2026')
    label(pdf, '01', 'Bildseite aus dem Sammel-Scan', 602)
    pdf.drawImage(ImageReader(photo_card()), LEFT, 390, width=BODY, height=BODY * 440 / 1200)
    label(pdf, '02', 'Ablagehinweis', 332)
    lines(pdf, 305, ('Die Datei hing an einer Sammelmail mit mehreren Vorgängen.',
                     'Über Dateinamen, Nachrichtenkontext und visuellen Inhalt zuordnen.',
                     'Der Stapellauf hat auf dieser Seite keine Treffer protokolliert.'))
    pdf.save()

    crm(start(DEBRIEF / f'{SLUG}-kontrollmuster.pdf', 'Kontrollmuster zur Datenkopie',
              'NACHBESPRECHUNG   /   BEISPIEL EINER TEILANLAGE', 'Technisch neu erzeugter CRM-Auszug nach der Einzelprüfung'), 'clean')
    pdf = start(DEBRIEF / f'{SLUG}-nachbesprechung.pdf', 'Was nach der Prüfung bleibt',
                'MODERATION   /   GETRENNT VON DER TEILNEHMENDENAKTE', 'Entscheidungshinweise für die Vorführung am Vorgang ME-36')
    label(pdf, '01', 'Die rote Markierung zurücknehmen', 604)
    lines(pdf, 577, ('Die CRM-Notiz betrifft die Kundin und dokumentiert eine Korrektur.',
                     'Inhalt, ursprünglichen Status und Berichtigung zusammen ausgeben.',
                     'Interne Herkunft allein rechtfertigt keine Entfernung.'))
    label(pdf, '02', 'Den Beifang im Scan aussortieren', 492)
    lines(pdf, 465, ('Den fremden Kontakt aus dem gemischten Auszug entfernen.',
                     'Die Bildbeilage einem anderen Ticket zuordnen und ausschließen.',
                     'Bei anderen Bildern Gesichter, Schilder, Kennungen und Kontext prüfen.'))
    label(pdf, '03', 'Die technische Sperre begründen', 380)
    lines(pdf, 353, ('Im Kandidaten verdecken Rechtecke den Inhalt nur optisch.',
                     'Suche oder Textextraktion liefert die überdeckten Originalwerte.',
                     'Das Kontrollmuster schreibt die entfernten Daten nicht in die PDF.'))
    label(pdf, '04', 'Auskunft und Freigabe getrennt abschließen', 268)
    lines(pdf, 241, ('Den tatsächlichen Empfänger anhand des Versandnachweises benennen.',
                     'Antwort nach Art. 15 Abs. 1 DSGVO und Datenkopie zusammen prüfen.',
                     'Dateien, Textschicht, Anhänge und Metadaten im Vier-Augen-Prinzip prüfen.',
                     'Das Kontrollmuster zeigt einen Auszug für die Nachbesprechung.'))
    pdf.save()


if __name__ == '__main__':
    build()
