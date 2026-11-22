"""Belege der Neuralis-Gestaltungsakte bis einschließlich 19. März 2026.

Die zwei Vertragsoriginale und ihre gedruckten Fassungen liegen im Repository.
Für den Neusatz der weiteren Belege verwendet NEURALIS_FONT_DIR die lokal
lizenzierten TTF-Dateien von Times New Roman in Normal- und Fettschrift.
"""
import csv
import hashlib
import io
import json
import os
import re
from datetime import datetime
from email import policy
from email.message import EmailMessage
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from docx import Document
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OLD = ROOT / "testakten/statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen"
CASE = ROOT / "testakten/neuralis-medtech-erlangen-gestaltungsakte"
BASE = "Grundakte"
FIRST = "01_Bescheid_und_erste_Aenderung"
MANIFEST = []
BRANDS = {
    "company": ("Neuralis MedTech", "GESCHÄFTSLEITUNG  /  ERLANGEN", "#145C5D"),
    "mail": ("Nachrichtenarchiv", "KORRESPONDENZ  /  EINZELNACHRICHT", "#344B64"),
    "notar": ("Dr. Alfons Reinboth", "NOTAR IN ERLANGEN", "#554055"),
    "register": ("Amtsgericht Fürth", "HANDELSREGISTER  /  ABTEILUNG B", "#303C50"),
    "drv": ("Deutsche Rentenversicherung Bund", "CLEARINGSTELLE  /  ERWERBSSTATUS", "#233D57"),
    "bank": ("Firmenkunden Erlangen", "KREDITADMINISTRATION  /  JAHRESBESTÄTIGUNG", "#5B343C"),
}
INK = "#20262C"


def font_setup():
    explicit = os.environ.get("NEURALIS_FONT_DIR")
    directories = [Path(explicit)] if explicit else [
        Path("/System/Library/Fonts/Supplemental"),
        Path("/usr/share/fonts/truetype/msttcorefonts"),
        Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts",
    ]
    for directory in directories:
        for regular, bold in [
            ("Times New Roman.ttf", "Times New Roman Bold.ttf"),
            ("times.ttf", "timesbd.ttf"),
            ("Times_New_Roman.ttf", "Times_New_Roman_Bold.ttf"),
        ]:
            if (directory / regular).is_file() and (directory / bold).is_file():
                pdfmetrics.registerFont(TTFont("NeuralisSerif", directory / regular))
                pdfmetrics.registerFont(TTFont("NeuralisBold", directory / bold))
                return
    raise FileNotFoundError("Times New Roman, normal und fett, wird für den Neusatz gebraucht. "
                            "NEURALIS_FONT_DIR auf das Verzeichnis der lizenzierten TTF-Dateien setzen.")


def record(phase, stem, source, reading):
    MANIFEST.append({"source": source.relative_to(ROOT).as_posix(), "archive": f"{phase}/{stem}{source.suffix}",
                     "pdf": reading.relative_to(ROOT).as_posix()})


def stable_office(path, *, moment=datetime(2026, 3, 19), replacements=None):
    """ZIP-Zeitstempel und die automatischen Office-Bearbeitungsdaten stabil halten."""
    fixed = io.BytesIO()
    with ZipFile(path) as old, ZipFile(fixed, "w", compression=ZIP_DEFLATED) as new:
        for name in old.namelist():
            data = replacements[name] if replacements and name in replacements else old.read(name)
            if name == "docProps/core.xml":
                data = re.sub(rb"(<dcterms:(?:created|modified)\b[^>]*>)[^<]+", lambda match: match[1] + moment.strftime("%Y-%m-%dT%H:%M:%SZ").encode(), data)
            info = ZipInfo(name, moment.timetuple()[:6])
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            new.writestr(info, data)
    path.write_bytes(fixed.getvalue())


def render(path, *, brand, heading, date, reference, blocks):
    logo, service, color = BRANDS[brand]
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=59, leftMargin=59,
                            topMargin=106, bottomMargin=59, title=heading, author=logo)
    def page(c, d):
        width, height = A4
        c.setFillColor(colors.HexColor(color))
        c.rect(0, height - 12, width, 12, fill=1, stroke=0)
        c.setFont("NeuralisBold", 21)
        c.drawString(59, height - 54, logo)
        c.setFont("Helvetica", 8)
        c.drawString(60, height - 70, service)
        c.setStrokeColor(colors.HexColor("#AEB7B9"))
        c.line(59, height-82, width-59, height-82)
        c.line(59, 43, width-59, 43)
        c.setFillColor(colors.HexColor("#535F65"))
        c.setFont("Helvetica", 8)
        c.drawString(59, 29, reference)
        c.drawRightString(width-59, 29, f"{date}    /    {d.page}")
    def paragraph(value, family="NeuralisSerif", size=11, leading=14.3, space=6, shade=INK, keep=False):
        return Paragraph(escape(str(value)).replace("\n", "<br/>"), ParagraphStyle(
            "body", fontName=family, fontSize=size, leading=leading, spaceAfter=space,
            keepWithNext=keep, textColor=colors.HexColor(shade), allowWidows=0, allowOrphans=0))
    story = [paragraph(reference + "   ·   " + date, "Helvetica", 8.5, 11, 9, color),
             paragraph(heading, "NeuralisBold", 17, 20.2, 14, INK, True)]
    for block in blocks:
        if block == "---":
            story.append(PageBreak())
        elif isinstance(block, list):
            cells = [[paragraph(v, "NeuralisBold" if i==0 else "NeuralisSerif", 9.4, 11.7, 0,
                                "#FFFFFF" if i==0 else INK) for v in row] for i,row in enumerate(block)]
            table = Table(cells, colWidths=[doc.width / len(block[0])]*len(block[0]), repeatRows=1)
            table.setStyle(TableStyle([
                ("BACKGROUND",(0,0),(-1,0),colors.HexColor(color)),
                ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.HexColor("#F0F3F2"),colors.white]),
                ("VALIGN",(0,0),(-1,-1),"TOP"),("TOPPADDING",(0,0),(-1,-1),5),
                ("BOTTOMPADDING",(0,0),(-1,-1),5)]))
            story.extend([table, Spacer(1,8)])
        elif block.startswith("#"):
            story.append(paragraph(block[1:], "NeuralisBold", 11.8, 14.7, 5, color, True))
        else:
            story.append(paragraph(block))
    doc.build(story, onFirstPage=page, onLaterPages=page,
              canvasmaker=lambda *a, **kw: Canvas(*a, **{**kw, "invariant": 1}))


def pdf(phase, stem, brand, heading, date, ref, blocks):
    path = CASE / phase / (stem + ".pdf")
    render(path, brand=brand, heading=heading, date=date, reference=ref, blocks=blocks)
    record(phase, stem, path, path)


def mail(phase, stem, date, sender, recipient, subject, body, attachment=None):
    target = CASE / phase / (stem + ".eml")
    m = EmailMessage(policy=policy.SMTP)
    m["From"], m["To"], m["Subject"] = sender, recipient, subject
    m["Date"] = datetime.fromisoformat(date)
    m["Message-ID"] = f"<{stem.lower()}@neuralis.example>"
    m.set_content(body)
    blocks = [f"Von: {sender}\nAn: {recipient}\nGesendet: {m['Date']}"]
    if attachment:
        m.add_attachment(attachment.read_bytes(), maintype="text", subtype="csv", filename=attachment.name)
        m.set_boundary("Neuralis-" + hashlib.sha256(attachment.read_bytes()).hexdigest()[:20])
        blocks.append("Anlage: " + attachment.name)
    target.write_bytes(m.as_bytes())
    reading = HERE / "lesefassungen" / phase / (stem + ".pdf")
    render(reading, brand="mail", heading=subject, date=date[:10], reference=stem.split("_")[0] + "  /  E-Mail",
           blocks=blocks+body.split("\n\n"))
    record(phase, stem, target, reading)


def spreadsheet(phase, stem, caption, date, fields, rows, formats):
    target = CASE / phase / (stem + ".xlsx")
    book = Workbook()
    sheet = book.active
    sheet.title = "Journal"
    sheet.append([caption])
    sheet.append([date])
    sheet.append(fields)
    for row in rows:
        sheet.append(row)
    for c in sheet[3]:
        c.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="155C5D")
    sheet["A1"].font=Font(name="Arial",bold=True,size=14,color="155C5D")
    for idx, width in enumerate([22,24,20,24,52],1):
        sheet.column_dimensions[get_column_letter(idx)].width=width
    for idx in range(4, sheet.max_row+1):
        for col, fmt in formats.items():
            sheet.cell(idx,col).number_format=fmt
        for c in sheet[idx]:
            c.alignment=Alignment(vertical="center", wrap_text=True)
    sheet.freeze_panes="A4"
    sheet.auto_filter.ref=f"A3:{get_column_letter(len(fields))}{sheet.max_row}"
    sheet.sheet_properties.pageSetUpPr.fitToPage=True
    sheet.page_setup.orientation="landscape"
    sheet.page_setup.fitToWidth=1
    sheet.page_setup.fitToHeight=0
    book.save(target)
    stable_office(target)
    reading = HERE / "lesefassungen" / phase / (stem+".pdf")
    render(reading,brand="company",heading=caption,date=date,reference="GF-BÜRO  /  Auszug aus dem Lohnjournal",
           blocks=[ [fields]+[list(map(str,r)) for r in rows], "Abrechnungswerte in EUR. Das Feld SV-Abzug erfasst ausschließlich den in der Abrechnung einbehaltenen Arbeitnehmeranteil. Eine Gesamt-Nettolohnberechnung ist in diesem Auszug nicht enthalten."])
    record(phase, stem, target, reading)

def first_contact():
    mail(BASE, "A01_Datenraum_Labor", "2023-07-21T10:38:00+02:00",
         "Caroline Benkert <c.benkert@neuralis.example>", "Henrik Vogt <h.vogt@neuralis.example>",
         "Montag kommt der Wirtschaftsprüfer ins Labor",
         """Guten Morgen Henrik,

Frau Mahler möchte am Montag beim Rundgang vom Bedarf bis zur Unterschrift eine unserer Anschaffungen nachvollziehen. Ich habe den Vorgang E-2306-19 und die Unterlagen zur Leitung der Gesellschaft herausgesucht. Bitte bring auch den Ordner mit der ursprünglichen Vertragsfassung mit. Im Laufwerk liegt sie unter „Gründerrunde“, der Dateiname verrät das Datum nicht.

Für das Bankgespräch am Nachmittag würde ich gern wissen, wer während Deiner Abwesenheit die endgültige Fassung des Quartalsberichts freigibt. Miriam kann die Versuchsdaten erläutern. Das Kreditteam hat aber ausdrücklich nach dem Zeichnungsberechtigten gefragt. Ich lasse das Feld bis zu Deiner Rückmeldung offen.

Caroline
Finanzen · Neuralis MedTech GmbH""")

    for short, stem in [("02_gesellschaftsvertrag","A02_Gesellschaftsvertrag_2023"),
                        ("03_geschaeftsfuehrervertrag","A03_Anstellungsvertrag_Vogt")]:
        source = OLD / (short + ".docx")
        materialized = CASE / BASE / (stem + ".docx")
        materialized.write_bytes(source.read_bytes())
        record(BASE, stem, materialized, HERE / "lesefassungen" / BASE / (stem + ".pdf"))

    pdf(BASE, "A04_Anteilsstand_Maerz", "company", "Gesellschafterverzeichnis zum Quartalsbericht",
        "31.03.2023", "Corporate Office  ·  Anlage Q1/23-4", [
        "Neuralis MedTech GmbH, Henkestraße 91, 91054 Erlangen · Amtsgericht Fürth, HRB 18442",
        "Die Buchhaltung führt die drei vollständig eingezahlten Geschäftsanteile in der Anteilskartei seit der Finanzierungsrunde 2021. Das Stammkapital beträgt 100.000 Euro. Je Euro Nennbetrag wird eine Stimme geführt.",
        [["Anteil","Inhaberin / Inhaber","Nennbetrag","Stimmen"],
         ["1","FrankenHealth Ventures GmbH, München","51.000 €","51.000"],
         ["2","Dr. Henrik Vogt, Erlangen","32.000 €","32.000"],
         ["3","Dr. Miriam Seidl, Nürnberg","17.000 €","17.000"]],
        "Grundlage des Abgleichs sind die im Datenraum der Finanzierungsrunde hinterlegte Liste und der Auszug aus dem Beteiligungskonto. Die am 24. Februar 2023 beschlossene Neufassung des Gesellschaftsvertrags änderte weder die Nennbeträge noch die Inhaber. Für die Stimmzählung im Protokoll ist zusätzlich zu prüfen, wer zu dem betreffenden Tagesordnungspunkt tatsächlich abgestimmt hat.",
        "Aufgestellt für das Bankreporting durch Caroline Benkert, Finanzen. Abgelegt am 03.04.2023 unter Gesellschaft / Quartal 1."])

    pdf(BASE, "A05_Beirat_Investitionsfreigabe", "company", "Freigabe für den Ausbau des Prüfraums",
        "23.06.2023", "Niederschrift  ·  BR 03/23  ·  E-2306-19", [
        "Besprechungsraum 2, Erlangen, 08:30 bis 09:05 Uhr. Anwesend waren alle drei Mitglieder des Beirats. Den Vorsitz führte Prof. Dr. Cornelius Baumhauer. Dr. Vogt war zur Vorstellung des technischen Bedarfs eingeladen. Frau Benkert führte das Protokoll.",
        "#1. Bedarf und Alternativangebot",
        "Die Entwicklungsgruppe beabsichtigt, den vorhandenen Messplatz mit einem Klimaschrank und dem zugehörigen Einbau zu erweitern. Vogt legt das Angebot der Altmühl Prüftechnik GmbH über 62.400 Euro netto vor. Eine Leasingvariante ist in der Investitionsliste noch nicht freigegeben. Ohne Umbau kann die Gruppe die Messreihe im gemieteten Labor fortsetzen, müsste jedoch zwei feste Freitage im Juli abgeben.",
        "#2. Beratung und Abstimmung",
        "Vogt bittet um Freigabe am selben Tag. Der Vorsitzende verlangt eine getrennte Ausweisung von Schrank, Einbau und Abnahme. Ein Mitglied hält die bestehenden Stundensätze im Mietlabor für günstiger. Der Beirat stimmt dem Erwerb mit zwei Ja-Stimmen gegen eine Nein-Stimme unter der Bedingung zu, dass die Einkaufssumme insgesamt 62.400 Euro netto nicht überschreitet. Die ausgewiesenen Positionen gehören zu einem Auftrag. Die Aufteilung in zwei Rechnungen erweitert die Freigabe nicht.",
        "#3. Ausführung",
        "Benkert hinterlegt die Freigabe zur Anforderung E-2306-19. Vogt kann die Bestellung nach Eingang der verlangten Aufstellung unterzeichnen. Er hat an der Abstimmung nicht teilgenommen. Die Sitzungsleitung gibt diese Niederschrift am 26. Juni für das Beschlussbuch frei.",
        "Prof. Dr. Cornelius Baumhauer · Vorsitzender des Beirats\nCaroline Benkert · Protokoll"])

    csv_rows=[["Vorgang","Zeitpunkt","Aktion","Betrag netto EUR","Bediener"],
              ["E-2306-19","20.06.2023 15:34","Bedarf angelegt","62400,00","Vogt"],
              ["E-2306-19","21.06.2023 09:10","Freigabe ausstehend","62400,00","Einkauf"],
              ["E-2306-19","26.06.2023 08:43","Beiratsbeschluss hinterlegt","62400,00","Benkert"],
              ["E-2306-19","27.06.2023 10:26","Angebotsanlage ergänzt","62400,00","Einkauf"],
              ["E-2306-19","27.06.2023 11:08","Bestellung ausgelöst","62400,00","Vogt"]]
    buf=io.StringIO(newline="")
    csv.writer(buf,delimiter=";",lineterminator="\r\n").writerows(csv_rows)
    stem="A07_Einkaufsjournal"
    csv_path=CASE/BASE/(stem+".csv")
    csv_path.write_bytes(buf.getvalue().encode("utf-8-sig"))
    reading=HERE/"lesefassungen"/BASE/(stem+".pdf")
    render(reading,brand="company",heading="Ereignisjournal zur Bestellung",date="21.07.2023",reference="Einkauf  /  E-2306-19",
           blocks=[csv_rows,"Die Wertspalte zeigt den Auftragswert zum Ereigniszeitpunkt."])
    record(BASE,stem,csv_path,reading)
    mail(BASE,"A06_Einkauf_Freigabekette","2023-07-21T11:16:00+02:00",
         "Eva Dorn <e.dorn@neuralis.example>","Caroline Benkert <c.benkert@neuralis.example>",
         "E-2306-19 / Wer hat an welcher Stelle freigegeben?",
         """Hallo Caroline,

anbei der Export zu der einen Bestellung. Die erste Zeile ist unsere Bedarfsanmeldung. Henrik hatte das Gerät mit dem Lieferanten ausgesucht, nach dem Eintrag am Mittwoch konnte er die Bestellung aber noch nicht auslösen. Die Freigabe des Beirats und die unterschriebene Bestellung liegen an verschiedenen Stellen im System.

Der Auftrag gehört zusammen, obwohl der Lieferant den Schrank im Juni anliefert und den Einbau erst nach den Betriebsferien abrechnen möchte. Die fünf Zeilen im Journal enthalten dementsprechend fünfmal denselben Auftragswert.

Viele Grüße
Eva Dorn · Einkauf""",csv_path)
    spreadsheet(BASE,"A08_Lohnjournal_Fruehjahr","Lohnjournal Geschäftsleitung · Personalnummer 04","30.06.2023",
                ["Monat","Festbezug EUR","Variable EUR","SV-Abzug EUR","Vermerk"], [
                    ["März 2023",12000,0,0,"Anstellungsvertrag ab 01.03."],
                    ["April 2023",12000,0,0,"Abrechnung im Stammsatz GF-04"],
                    ["Mai 2023",12000,0,0,"Abrechnung im Stammsatz GF-04"],
                    ["Juni 2023",12000,0,0,"Prämienfeld ohne Freigabe"]],
                {2:'#,##0.00',3:'#,##0.00',4:'#,##0.00'})
    pdf(BASE,"A09_Bank_Sicherheitenstand","bank","Bestätigung zum Investitionskredit 771-4402",
        "14.07.2023","Kreditakte 771-4402  ·  Sicherheit 2021-0417",[
        "An Herrn Dr. Henrik Vogt\nSchuhstraße 12\n91052 Erlangen",
        "Sehr geehrter Herr Dr. Vogt,",
        "Sie baten um eine Mitteilung zum Stand Ihrer persönlichen Sicherheit für den Investitionskredit der Neuralis MedTech GmbH. In unserem Sicherheitenbuch führen wir die am 3. Juni 2021 übernommene selbstschuldnerische Bürgschaft bis zu einem Höchstbetrag von 400.000 Euro. Kreditnehmerin ist die Gesellschaft.",
        "Bis einschließlich 30. Juni 2023 hat die Bank keine Zahlung von Ihnen aus der Bürgschaft verlangt. Die laufenden Zins- und Tilgungsleistungen erhielt sie vom Geschäftskonto der Gesellschaft. Eine persönliche Zahlung Ihrerseits ist für diesen Kredit bislang nicht verbucht.",
        "Diese Mitteilung ist für Ihre private Vermögensaufstellung bestimmt. Der Höchstbetrag entspricht weder dem aktuellen offenen Kredit noch einer fälligen Zahlungsforderung gegen Sie. Für eine Ablösung zum Quartalsende erstellen wir auf Wunsch eine gesonderte Abrechnung.",
        "Mit freundlichen Grüßen\nGuido Landmann\nFirmenkunden · Kreditadministration"])

    mail(BASE,"A10_Abwesenheitsvertretung","2023-07-13T17:48:00+02:00",
         "Prof. Dr. Cornelius Baumhauer <c.baumhauer@neuralis.example>","Dr. Henrik Vogt <h.vogt@neuralis.example>",
         "Freitag im Juli / Wer nimmt das Paket für den Prüfstand an?",
         """Lieber Henrik,

der 21. Juli passt für Deinen halben freien Tag. Trag die Abwesenheit bitte nach wie vor bei Nora ein, damit die Telefonliste für den Nachmittag stimmt. Beim Prüflabor genügt mir Miriams Zusage, dass jemand für die Übergabe vor Ort ist. Für die unterschriftsreifen Unterlagen der Bank möchte ich morgens noch ein Zeitfenster mit Dir haben.

Du hattest gefragt, ob die Eintragung als einer Deiner Urlaubstage zählt. Wir haben beim halben Tag eine entsprechende Zeile, die Jahresübersicht kommt erst zum Jahresende. In den Terminkalender gucken alle, in die Urlaubsübersicht nur Personal und Du.

Beste Grüße
Cornelius""")

AMEND_PATENT = ("6.2.9 Abweichend vom Eingangssatz zu Ziffer 6.2 bedarf die Lizenzierung von Patenten der "
                "Patentfamilie NLM-4 an einen Vertragspartner mit Sitz außerhalb der Europäischen Union einer "
                "Mehrheit von neunzig Prozent der abgegebenen Stimmen.")
AMEND_RESSORT = ("6.5 Solange Dr. Henrik Vogt der Gesellschaft als Geschäftsführer angehört und mindestens "
                 "25 Prozent des Stammkapitals hält, bedarf sowohl die Änderung seines Ressorts Entwicklung, "
                 "regulatorische Zulassung und klinische Kooperationen als auch eine an ihn gerichtete Weisung, "
                 "die eine bereits laufende klinische Studie unmittelbar unterbricht, seiner Zustimmung. "
                 "Für andere Weisungen gelten Ziffern 4.3 und 6.1. Die Zustimmungsvorbehalte des Beirats "
                 "nach Ziffer 7.3 bleiben bestehen.")
REF = "Status  ·  C 25/8146-NM"


def decision_and_amendment():
    pdf(FIRST,"B01_Antrag_Erwerbsstatus","company","Antrag auf Feststellung des Erwerbsstatus",
        "15.12.2025", "Geschäftsleitung  ·  NMT / GF-04",[
        "Deutsche Rentenversicherung Bund\nClearingstelle\n10704 Berlin",
        "Sehr geehrte Damen und Herren,",
        "wir bitten gemeinsam nach § 7a Abs. 1 SGB IV um Entscheidung über die Tätigkeit von Dr. Henrik Vogt als Geschäftsführer der Neuralis MedTech GmbH auf Grundlage des ab 1. März 2023 geltenden Anstellungsvertrags. Die Gesellschaft hat hierfür bislang keine Anmeldung als Beschäftigten abgegeben. Nach unserer Kenntnis ist weder bei einer Einzugsstelle noch bei einem anderen Versicherungsträger ein Verfahren zur Versicherungspflicht dieser Tätigkeit eingeleitet.",
        "Herr Dr. Vogt hält 32.000 Euro am Stammkapital von 100.000 Euro. Das in der Satzung bezeichnete Entwicklungsressort prägt unsere Produkte. Die Geschäftsleitung ist auf seinen persönlichen Kontakt zu den Prüfkliniken angewiesen. Vogt hält sich deshalb für selbständig. Er vertritt die GmbH allein, haftet gegenüber der Hausbank aus einer Bürgschaft und stimmt bei den Gesellschafterversammlungen mit.",
        "Der Fonds hat Ende November nach einer schriftlichen Entscheidung über diese Tätigkeit gefragt. Die beigefügte Satzung gilt im übersandten Wortlaut seit dem 6. März 2023. Es ist danach kein Änderungsbeschluss gefasst worden. Im Bereich großer Investitionen verlangt die Geschäftsleitung eine Freigabe des Beirats. Ein Originalvorgang ist unter E-2306-19 nachvollziehbar.",
        "Anlagen aus dem Gesellschaftsordner: Satzung vom 24.02.2023, Anstellungsvertrag vom 27.02.2023, Anteilsstand und Beiratsprotokoll vom 23.06.2023. Um getrennte Bekanntgabe an den Geschäftsführer und die Gesellschaft wird gebeten.",
        "Dr. Henrik Vogt · für die Gesellschaft als Geschäftsführer\nDr. Henrik Vogt · zugleich im eigenen Namen"])

    pdf(FIRST,"B02_Anhoerung","drv","Anhörung im Anfrageverfahren",
        "16.01.2026",REF,[
        "Neuralis MedTech GmbH\nHenkestraße 91\n91054 Erlangen\nGleichlautendes Schreiben an Herrn Dr. Henrik Vogt",
        "Sehr geehrte Damen und Herren,",
        "nach Auswertung der bisher vorgelegten Unterlagen beabsichtigen wir, die seit dem 1. März 2023 ausgeübte Geschäftsführertätigkeit als Beschäftigung einzuordnen. Wir geben Ihnen Gelegenheit, sich bis zum 30. Januar 2026 zu den für die Entscheidung erheblichen Tatsachen zu äußern.",
        "Bei vollständiger Teilnahme an der Gesellschafterversammlung verfügen die übrigen Gesellschafter über 68.000 von 100.000 Stimmen. Nach Ziffern 4.3 und 6.1 des vorgelegten Gesellschaftsvertrags können sie gemeinsam Weisungen in der gewöhnlichen Geschäftsführung beschließen. Bei einzelnen Geschäften reicht die einfache Mehrheit dagegen nicht aus.",
        "Bitte legen Sie etwaige weitere Bestimmungen vor, nach denen Herr Dr. Vogt auch andere Beschlüsse von seiner persönlichen Zustimmung abhängig machen kann. Teilen Sie uns mit, ob der Gesellschaftsvertrag seit dem 6. März 2023 geändert wurde. Für die Beurteilung sind der Beschluss und der jeweilige Zeitpunkt der Eintragung von Interesse.",
        "Bitte erläutern Sie, wer in dem Vorgang E-2306-19 abgestimmt und wer den Auftrag rechtsverbindlich ausgelöst hat. Für Ihre Stellungnahme können Sie ergänzend auf den tatsächlichen Umgang mit Abwesenheiten und Reisekosten eingehen.",
        "Im Auftrag\nR. Brandel · Clearingstelle"])

    pdf(FIRST,"B03_Aeusserung_der_Beteiligten","company","Stellungnahme zum Schreiben vom 16. Januar",
        "29.01.2026",REF,[
        "Deutsche Rentenversicherung Bund\nClearingstelle\n10704 Berlin",
        "Sehr geehrte Frau Brandel,",
        "Herr Dr. Vogt hat den Klimaschrank ausgewählt und die fachlichen Anforderungen ausgehandelt. Am 23. Juni 2023 hatte er im Beirat keine Stimme. Die Zustimmung kam mit zwei Stimmen gegen eine zustande. Am 27. Juni hat er die Bestellung allein unterzeichnet. Diese Unterschrift und sein Mitspracherecht als Gesellschafter sind zwei verschiedene Vorgänge.",
        "Wir haben die Urkundensammlung der Gesellschaft mit dem Registerordner verglichen. Zwischen der Eintragung vom 6. März 2023 und heute wurde keine Änderung des Gesellschaftsvertrags eingetragen. Ein gesonderter Stimmbindungsvertrag oder eine Vollmacht, mit der Vogt Stimmen des Fonds oder von Miriam Seidl ausüben könnte, ist uns nicht bekannt.",
        "Für Vogts Abwesenheiten orientieren wir uns am Kalender der klinischen Partner. Er verschiebt die eigenen Termine selbst und schuldet keine Zeiterfassung. Der bezahlte Jahresurlaub ist im Vertrag weiterhin vereinbart. Eine Vertretung durch einen von ihm ausgesuchten und bezahlten Dritten ist bislang nicht vorgekommen.",
        "Vogt meint, dass er durch die qualifizierten Beschlussmehrheiten das wichtigste Patent im Unternehmen halten könnte. Ohne sein Fachwissen wäre eine Verlagerung der Entwicklung sehr schwer. Wir bitten, die tatsächlichen Möglichkeiten des Geschäftsführers und sein persönliches Kreditrisiko bei Ihrer Würdigung zu berücksichtigen.",
        "Dr. Henrik Vogt · Geschäftsführer und Beteiligter\nCaroline Benkert · Finanzen, Auskunft zu den Unterlagen"])

    pdf(FIRST,"B04_Bescheid_Erwerbsstatus","drv","Bescheid über den Erwerbsstatus",
        "09.02.2026",REF,[
        "An Herrn Dr. Henrik Vogt\nSchuhstraße 12\n91052 Erlangen\nDie Neuralis MedTech GmbH erhält eine gleichlautende Ausfertigung.",
        "Sehr geehrter Herr Dr. Vogt,",
        "#1. Entscheidung",
        "Wir stellen auf den gemeinsamen Antrag vom 15. Dezember 2025 fest, dass Sie die Tätigkeit als Geschäftsführer für die Neuralis MedTech GmbH auf Grundlage des seit 1. März 2023 bestehenden Anstellungsvertrags seit diesem Tag im Rahmen einer Beschäftigung ausüben.",
        "#2. Tatsächliche Grundlagen",
        "Sie halten 32.000 von 100.000 Stimmen, der Fonds 51.000 und Frau Dr. Seidl 17.000. Jede Stimme folgt dem Nennbetrag des Geschäftsanteils. Sie können die Gesellschaft nach außen allein vertreten. Intern verweist Ziffer 4.3 des am 6. März 2023 eingetragenen Gesellschaftsvertrags auf Weisungen der Gesellschafterversammlung. Für gewöhnliche Weisungen reicht nach Ziffer 6.1 die Mehrheit der abgegebenen Stimmen. Für die in Ziffer 6.2 aufgezählten Geschäfte gilt ein höheres Quorum.",
        "Ihre Stellungnahme vom 29. Januar 2026, die Vertragsunterlagen, der Bestellauszug und der Schriftverkehr über die Abwesenheitsvertretung wurden berücksichtigt. Sie konnten das Prüfgerät auswählen und nach Freigabe die Bestellung unterschreiben. Die Zustimmung des Beirats fiel zuvor ohne Ihre Stimme. Sie beziehen eine feste monatliche Vergütung von 12.000 Euro. Sie haben der Hausbank für den Investitionskredit eine persönliche Bürgschaft gestellt.",
        "---","#3. Würdigung",
        "Nach §§ 7 Abs. 1, 7a Abs. 2 SGB IV würdigen wir die rechtlichen und tatsächlichen Umstände der konkret ausgeübten Geschäftsführertätigkeit. Bei der Leitung einer GmbH ist erheblich, ob ein mitarbeitender Gesellschafter aufgrund seiner gesellschaftsrechtlichen Stellung auch eine ihm unerwünschte Weisung aus der gewöhnlichen Geschäftsführung zuverlässig verhindern kann.",
        "Ihre Beteiligung reicht bei Teilnahme aller drei Gesellschafter aus, einzelne Satzungs- und Strukturentscheidungen zu verhindern. Ihre Mitgesellschafter können Ihnen aber auch bei Ihrer ausdrücklichen Gegenstimme mit 68.000 Stimmen sachliche Vorgaben erteilen. Die Satzung enthält für diese Entscheidungen weder ein persönliches Zustimmungsrecht noch ein umfassendes erhöhtes Mehrheitserfordernis. Eine maßgebliche Einflussmöglichkeit auf einzelne grundsätzliche Geschäfte genügt dafür nicht. Vgl. Bundessozialgericht, Urteil vom 1. Februar 2022, B 12 KR 37/19 R, Rn. 13–17.",
        "Die Außenvertretungsbefugnis erklärt Ihre Unterschrift unter der Bestellung. Fachliche Selbständigkeit bei der Auswahl von Messgeräten und die persönliche Bürgschaft begründen ein erhebliches wirtschaftliches Interesse. Keiner dieser Umstände verschafft Ihnen eine zusätzliche Stimme. Die feste Vergütung, die bezahlte Abwesenheit und der ausschließliche Einsatz für die Gesellschaft fügen sich in die gesellschaftsrechtliche Zuordnung ein.",
        "#4. Gegenstand und Rechtsbehelf",
        "Die Entscheidung betrifft den Erwerbsstatus in der bezeichneten Tätigkeit. Über konkrete Versicherungspflichten einzelner Zweige, Beitragsbeträge und deren Fälligkeit wird mit diesem Bescheid nicht entschieden.",
        "Sie können innerhalb eines Monats nach Bekanntgabe Widerspruch bei der Deutschen Rentenversicherung Bund in Berlin einlegen. Der Widerspruch kann schriftlich, zur Niederschrift, in elektronischer Form nach § 36a Abs. 2 SGB I oder schriftformersetzend nach § 36a Abs. 2a SGB I und § 9a Abs. 5 OZG eingereicht werden. Postanschrift: Deutsche Rentenversicherung Bund, 10704 Berlin.",
        "Im Auftrag\nR. Brandel · Clearingstelle"])

    mail(FIRST,"B05_Post_und_Termin","2026-02-11T15:23:00+01:00",
         "Dr. Henrik Vogt <h.vogt@neuralis.example>","Caroline Benkert <c.benkert@neuralis.example>",
         "Die beiden Briefe aus Berlin",
         """Caroline,

der Zusteller hat mir den Brief für mich persönlich heute um 08:12 Uhr gegen Empfangsbestätigung in die Hand gegeben. Der Brief für die Gesellschaft wurde nach Deinem Eingangsbuch heute um 09:06 Uhr in der Poststelle ebenfalls förmlich zugestellt. Der Umschlag mit dem gelben Vermerk liegt bei meiner Ausfertigung.

Ich bin davon ausgegangen, dass ich mit 32 Prozent und dem Risiko gegenüber der Bank als Gründer auf eigene Rechnung arbeite. Jetzt steht dort „Beschäftigung“. Nächsten Dienstag muss ich den Investoren etwas zum laufenden Betrieb sagen können. Bitte trenne das, was im Brief steht, von einer Zahlung, über deren Höhe bislang kein Schreiben vorliegt.

Miriam würde mit einer schriftlichen Sicherung meines Entwicklungsressorts leben. Torben will weder die kaufmännische Leitung abgeben noch jede Bestellung einstimmig entscheiden. Ich lasse das Notariat wegen eines Termins anrufen. Bitte frag den Rentenberater unabhängig davon nach der laufenden Widerspruchsfrist.

Henrik""")

    pdf(FIRST,"B06_Vertretungsnachweis_Fonds","notar","Registereinsicht zur Vertretung des Fonds",
        "23.02.2026","AG München  ·  HRB 234981  ·  Abdruck für die Notariatsakte",[
        "#1. Firma, Sitz und Vertretung",
        "FrankenHealth Ventures GmbH, München. Geschäftsanschrift im Inland: Isartorplatz 6, 80331 München. Gegenstand ist der Erwerb, das Halten und die Verwaltung von Beteiligungen an Unternehmen des Gesundheitssektors.",
        "Ist ein Geschäftsführer bestellt, vertritt er die Gesellschaft allein. Sind mehrere Geschäftsführer bestellt, wird die Gesellschaft durch zwei Geschäftsführer gemeinschaftlich oder durch einen Geschäftsführer gemeinsam mit einem Prokuristen vertreten. Einzelvertretungsbefugnis kann erteilt werden.",
        "#2. Personenbezogene Eintragung",
        "Geschäftsführer: Torben Aldenhoven, München, einzelvertretungsberechtigt. Das Vorliegen einer Befreiung von § 181 BGB ist für diesen Auszug nicht bescheinigt. Aldenhoven tritt in der Erlanger Urkunde ausschließlich für die Fonds-GmbH auf.",
        "Abrufvermerk der Notariatskanzlei Reinboth: Für die Beurkundung am 24. Februar um 09:00 Uhr elektronisch eingesehen. Die geschäftsführende Gesellschaft und der im Termin erscheinende Vertreter sind identifiziert. Ablage RB 126/26, Registerbeleg 1.",
        "Nina Wüst · Sachbearbeitung Gesellschaftsrecht"])

    pdf(FIRST,"B07_Urkunde_126_2026","notar","Niederschrift einer Gesellschafterversammlung",
        "24.02.2026","UVZ 126/2026  ·  Neuralis MedTech GmbH",[
        "#1. Erschienene und Feststellungen",
        "Verhandelt in Erlangen am 24. Februar 2026. Vor mir, Notar Dr. Alfons Reinboth, erschienen Herr Torben Aldenhoven für die FrankenHealth Ventures GmbH, Herr Dr. Henrik Vogt und Frau Dr. Miriam Seidl, beide im eigenen Namen. Die Erschienenen wiesen sich durch ihre gültigen Personalausweise aus. Der Notar bescheinigt nach Einsicht in das Handelsregister des Amtsgerichts München vom 23. Februar 2026 zu HRB 234981 die Einzelvertretungsberechtigung des Herrn Aldenhoven für die FrankenHealth Ventures GmbH.",
        "Nach der zuletzt in den Registerordner der Neuralis MedTech GmbH aufgenommenen Gesellschafterliste hält die Fonds-GmbH Geschäftsanteil 1 zu 51.000 Euro, Dr. Vogt Geschäftsanteil 2 zu 32.000 Euro und Dr. Seidl Geschäftsanteil 3 zu 17.000 Euro. Das gesamte Stammkapital ist vertreten. Alle Beteiligten erklären sich mit der Versammlung und der sofortigen Beschlussfassung trotz abgekürzter Ladungsfrist einverstanden. Torben Aldenhoven übernimmt den Vorsitz.",
        "#2. Beschlossene Änderungen",
        "Ziffer 6.2 des Gesellschaftsvertrags wird um folgende Ziffer ergänzt:",
        AMEND_PATENT,
        "Nach Ziffer 6.4 wird folgende Ziffer eingefügt:",
        AMEND_RESSORT,
        "---","#3. Abstimmung und Beschlussfeststellung",
        "Über beide Änderungen wird gemeinsam abgestimmt. Die FrankenHealth Ventures GmbH stimmt mit 51.000 Stimmen, Dr. Henrik Vogt mit 32.000 Stimmen und Dr. Miriam Seidl mit 17.000 Stimmen zu. Gegenstimmen und Enthaltungen werden nicht abgegeben. Der Vorsitzende stellt den Beschluss mit 100.000 Ja-Stimmen fest.",
        "Alle übrigen Bestimmungen des Gesellschaftsvertrags vom 24. Februar 2023 gelten unverändert. Eine Änderung des Anstellungsvertrags ist nicht Gegenstand der Abstimmung. Die Geschäftsführung soll den Beschluss zum Register anmelden. Für das Unternehmen bestand keine Verpflichtung, ein bestimmtes sozialversicherungsrechtliches Ergebnis herbeizuführen.",
        "#4. Erläuterung und Vollzug",
        "Der Notar erläuterte, dass die Satzungsänderung erst mit Eintragung in das Handelsregister rechtliche Wirkung erlangt. Die Erschienenen baten um elektronischen Vollzug und um Übersendung der Eintragungsnachricht an die Gesellschaft. Mit der Prüfung eines Rechtsbehelfs gegen den im Februar zugegangenen Bescheid haben sie den Notar nicht beauftragt.",
        "Die Niederschrift wurde den Erschienenen vom Notar vollständig vorgelesen, von ihnen genehmigt und von ihnen sowie dem Notar eigenhändig unterschrieben. Wiedergabe der Namen aus der Urschrift:",
        "Torben Aldenhoven · Dr. Henrik Vogt · Dr. Miriam Seidl\nDr. Alfons Reinboth, Notar",
        "Einfache Abschrift für die Gesellschaft. Verwahrung der Urschrift bei dem beurkundenden Notar."])

    clauses = Document(OLD/"02_gesellschaftsvertrag.docx").paragraphs
    text = [p.text.strip() for p in clauses if re.match(r"^\d+[ .]", p.text.strip())]
    assert all(any(t.startswith(n) for t in text) for n in ["6.2.8 ", "6.4 ", "14.4 "])
    def numbered(t):
        return "#"+t if re.match(r"^\d+ ",t) else t
    contents=[]
    for t in text:
        contents.append(numbered(t))
        if t.startswith("6.2.8 "): contents.append(AMEND_PATENT)
        if t.startswith("6.4 "): contents.append(AMEND_RESSORT)
    contents += ["#Bescheinigung nach § 54 Abs. 1 Satz 2 GmbHG",
                 "Die geänderten Bestimmungen des vorstehenden Gesellschaftsvertrags entsprechen dem Beschluss vom 24. Februar 2026, UVZ 126/2026. Die unveränderten Bestimmungen entsprechen dem zuletzt zum Handelsregister eingereichten vollständigen Wortlaut vom 24. Februar 2023. Dies bescheinige ich in Erlangen am 26. Februar 2026.",
                 "Dr. Alfons Reinboth, Notar"]
    pdf(FIRST,"B08_Satzungswortlaut_mit_Bescheinigung","notar","Vollständiger Wortlaut des Gesellschaftsvertrags",
        "26.02.2026","Neuralis MedTech GmbH  ·  AG Fürth, HRB 18442",contents)

    pdf(FIRST,"B09_Anmeldung_und_Eingang","notar","Handelsregisteranmeldung mit Übermittlungsvermerk",
        "26.02.2026","Vollzug RB 126/26  ·  AG Fürth, HRB 18442",[
        "An das Amtsgericht Fürth – Registergericht",
        "In der Registersache Neuralis MedTech GmbH melde ich als alleinvertretungsberechtigter Geschäftsführer zur Eintragung an, dass durch den Beschluss vom 24. Februar 2026 die Ziffern 6.2 und 6.5 des Gesellschaftsvertrags geändert beziehungsweise ergänzt wurden. Stammkapital, Gesellschafter und Vertretung sind unverändert.",
        "Beigefügt sind die elektronisch beglaubigte Abschrift der Niederschrift UVZ 126/2026 und der vollständige Wortlaut des Gesellschaftsvertrags mit der Bescheinigung des Notars. Um Eintragungsmitteilung an die Notariatskanzlei wird gebeten.",
        "Erlangen, 26. Februar 2026 · Dr. Henrik Vogt",
        "Die vor mir vollzogene Unterschrift des mir aus der Urkunde UVZ 126/2026 bekannten Dr. Henrik Vogt beglaubige ich. Erlangen, 26. Februar 2026. Dr. Alfons Reinboth, Notar. UVZ 132/2026.",
        "#Übermittlungsvermerk der Geschäftsstelle",
        "Am 26.02.2026 um 14:17 Uhr elektronisch an das Registergericht Fürth versandt. Eingangsbestätigung 14:18 Uhr, Vorgang RB-126-2602. Drei Dateien laut Versandliste: Anmeldung UVZ 132/2026, Beschluss UVZ 126/2026, bescheinigter vollständiger Wortlaut. Nina Wüst, Notariatskanzlei Reinboth."])

    pdf(FIRST,"B10_Eintragungsmitteilung","register","Mitteilung über die Eintragung im Handelsregister",
        "09.03.2026","Amtsgericht Fürth  ·  HRB 18442  ·  laufende Nummer 4",[
        "An Notar Dr. Alfons Reinboth, Erlangen\nIhr Vorgang RB 126/26",
        "In der Registersache Neuralis MedTech GmbH mit Sitz in Erlangen und Geschäftsanschrift Henkestraße 91, 91054 Erlangen wurde am 9. März 2026 in Abteilung B die nachstehende Eintragung vorgenommen.",
        [["Spalte","Inhalt der Eintragung"],["6 a)","Die Gesellschafterversammlung vom 24. Februar 2026 hat die Änderung der Ziffer 6 des Gesellschaftsvertrags (Gesellschafterbeschlüsse und Mehrheiten) beschlossen."],["7 a)","09.03.2026"]],
        "Die am 26. Februar 2026 übermittelte Anmeldung wurde für die laufende Nummer 4 erledigt. Die elektronische Dokumentensammlung enthält den Beschluss und den bescheinigten Wortlaut. Gegenstand der Eintragung ist die Änderung des Gesellschaftsvertrags.",
        "Maschinell erstellte Eintragungsmitteilung. Eingang im Vollzugsfach der Notariatskanzlei am 9. März, 13:47 Uhr. Aktenvermerk N. Wüst."])

    pdf(FIRST,"B11_Einkaufsweisung_Abstimmung","company","Beschluss über den Einkauf externer Beratungsleistungen",
        "19.03.2026","Niederschrift  ·  GSV 02/26  ·  Einkauf Klinikkooperationen",[
        "Von 08:00 bis 08:42 Uhr in Erlangen. Der Geschäftsführer hatte die Gesellschafter am 3. März mit Tagesordnung eingeladen. Anwesend waren alle Gesellschafter. Der Vorsitzende stellte das vertretene Kapital mit 100.000 Euro fest.",
        "#1. Antrag und Beratung",
        "Der Fonds beantragt, den Zahlungsabfluss an externe Berater transparenter zu machen. Jede Beauftragung externer Beratungsleistungen ab 18.000 Euro netto je Auftrag soll vor der Bestellung einen Freigabebeschluss der Gesellschafterversammlung erfordern. Die Geschäftsführung soll ab April bis zum dritten Werktag jeden Monats einen Bericht über diese Aufträge mit Betrag, Auftragnehmer und Zahlungsziel vorlegen. Weitergehende Zustimmungsvorbehalte des Beirats bleiben unberührt.",
        "Vogt erklärt, er habe die externe Übersetzung der Vertragsunterlagen für zwei Kliniken für 21.600 Euro ausgehandelt. Die Verzögerung durch den erneuten Umlauf sei schwer zu erklären. Beide Studien liefen unverändert weiter. Der Übersetzungsauftrag und der Monatsbericht änderten aus seiner Sicht nichts am Studienplan, schränkten ihn im Alltag aber erheblich ein.",
        "#2. Abstimmung",
        [["Gesellschafter","Stimmen","Votum"],["FrankenHealth Ventures GmbH","51.000","Ja"],["Dr. Henrik Vogt","32.000","Nein"],["Dr. Miriam Seidl","17.000","Ja"]],
        "Der Vorsitzende stellt 68.000 Ja- und 32.000 Nein-Stimmen fest und verkündet den Antrag als angenommen. Vogt bittet darum, seine Gegenstimme im Beschlussbuch zu vermerken. Der Einkauf hält den Auftrag E-2603-11 bis zur Einzelfreigabe zurück. Die Geschäftsführung soll das Beschlussblatt mit dem Vertragsordner an die Gesellschafter versenden.",
        "Torben Aldenhoven · Vorsitz der Gesellschafterversammlung\nCaroline Benkert · Protokoll"])
    mail(FIRST,"B12_Anforderung_Einzelfreigabe","2026-03-19T15:42:00+01:00",
         "Eva Dorn <e.dorn@neuralis.example>","Dr. Henrik Vogt <h.vogt@neuralis.example>",
         "E-2603-11 wartet im Freigabefach",
         """Hallo Henrik,

ich habe die Bestellung über 21.600 Euro netto nach der heutigen Sitzung wieder auf „wartet auf Beschluss“ gesetzt. Die Übersetzungen sind bestelltauglich, es fehlt nur die Einzelfreigabe aus der Gesellschafterrunde. Die beiden Prüfzentren arbeiten derweil mit den bisherigen Fassungen weiter. Ich habe bei keinem Zentrum eine Unterbrechung veranlasst.

Ich weiß, dass Du das heute Vormittag anders haben wolltest. Dein Häkchen „fachlich geprüft“ bleibt sichtbar. Für den Datensatz habe ich die Vergabedokumente aber noch nicht aus dem Haus geschickt. Caroline bereitet die Umlaufunterlagen vor.

Gruß
Eva""")

def save_receipt():
    pdf(FIRST,"B05a_Eingang_Widerspruch","drv","Eingang Ihrer Widersprüche",
        "20.02.2026",REF,[
        "An die Neuralis MedTech GmbH\nHenkestraße 91\n91054 Erlangen\nAbschrift an Herrn Dr. Henrik Vogt",
        "Sehr geehrte Damen und Herren,",
        "am 18. Februar 2026 sind bei uns zwei von Herrn Dr. Henrik Vogt unterzeichnete Schreiben eingegangen. Eines wurde für die Gesellschaft, das andere in eigener Sache gegen den Bescheid vom 9. Februar 2026 eingereicht. Wir führen beide Widersprüche unter dem bisherigen Aktenzeichen zusammen.",
        "Sie haben eine ergänzende Begründung angekündigt. Bitte reichen Sie die Unterlagen mit unserem Aktenzeichen ein. Wenn Sie eine zwischenzeitliche Änderung des Gesellschaftsvertrags vortragen, geben Sie das Datum der Beschlussfassung und das Datum einer Registereintragung jeweils gesondert an.",
        "Dieses Schreiben bestätigt den Eingang. Eine Entscheidung über die Widersprüche ergeht gesondert.",
        "Im Auftrag\nR. Brandel · Clearingstelle"])


def main():
    font_setup()
    for phase in (BASE,FIRST):
        (CASE/phase).mkdir(parents=True,exist_ok=True)
    first_contact()
    decision_and_amendment()
    save_receipt()
    from praxisbelege_bauen import build as build_praxisbelege
    MANIFEST.extend(build_praxisbelege())
    records=sorted(MANIFEST,key=lambda r:(r["archive"].split("/")[0]!=BASE,r["archive"]))
    for r in records:
        if not (ROOT/r["pdf"]).is_file() or not (ROOT/r["source"]).is_file():
            raise FileNotFoundError(r)
    (HERE/"manifest-grund.json").write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n")
    print(f"{len(records)} Unterlagen mit zugeordneter Lesefassung")


if __name__ == "__main__":
    main()
