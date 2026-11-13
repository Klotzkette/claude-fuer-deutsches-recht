"""Geschäftsunterlagen für die offene Eingangsbearbeitung der Insolvenzreifeakten.

Die Ergänzungen lesen Beträge aus der gemeinsamen Fallquelle. Sie verändern keine
Buchung und enthalten weder Insolvenzstichtag noch juristische Musterlösung.
"""
from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
import hashlib
from email import policy
from email.message import EmailMessage
from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree, indent

from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, SimpleDocTemplate
from reportlab.pdfgen.canvas import Canvas
from xml.sax.saxutils import escape


def money(value):
    n = Decimal(value) / 100
    return f"{n:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + " EUR"


def date_de(value):
    return datetime.fromisoformat(value).strftime("%d.%m.%Y")


BUSINESS = {
    "CB": {"color": "006663", "contact": "Marlene Wendt", "dept": "Finanzen und Werksdisposition",
           "address": "An der Tonmühle 8, 03044 Cottbus", "invoice_ids": ["CB-K02-01", "CB-K12-04", "CB-CAPEX-01", "CB-GAS-01"],
           "customer_ids": ["CB-DEB-01", "CB-DEB-02", "CB-DEB-03"],
           "topics": ["Werkteile aus Oxidkeramik", "Prüflos HM-2620", "Dichtringserie RD-2633"]},
    "BZ": {"color": "304E6C", "contact": "Tillmann Seifert", "dept": "Kaufmännische Leitung und Montage",
           "address": "Am Werkgraben 24, 14167 Berlin", "invoice_ids": ["BZ-K03-01", "BZ-K13-04", "BZ-STA-01", "BZ-CAPEX-01"],
           "customer_ids": ["BZ-DEB-01", "BZ-DEB-02", "BZ-DEB-03"],
           "topics": ["Montagelos Südspange", "Fassade 7, Aufmaß 3", "Brückenmontage Wasserwerk"]},
    "PR": {"color": "4E4268", "contact": "Malin Stange", "dept": "Charterdisposition und Rechnungswesen",
           "address": "Am Flugfeld 22, 17291 Prenzlau", "invoice_ids": ["PR-K03-01", "PR-K11-04", "PR-ROTOR-01", "PR-CAPEX-01"],
           "customer_ids": ["PR-DEB-01", "PR-DEB-02", "PR-DEB-03"],
           "topics": ["Luftbildauftrag Moorflug", "Transferreihe Inselblick", "Chartergutscheine Juni"]},
}


def invoice(path, case, entry, outgoing=False):
    """Ein Beleg mit identischer Bruttoforderung und identischer OP-Referenz."""
    profile = BUSINESS[case["prefix"]]
    issuer = case["company"] if outgoing else entry["creditor"]
    recipient = entry["debtor"] if outgoing else case["company"]
    reference = entry["id"]
    issue = entry.get("confirmed_on") if outgoing else entry["arose_on"]
    due = entry["available_on"] if outgoing else entry["due_on"]
    gross = entry["amount_cents"]
    net = int((Decimal(gross) / Decimal("1.19")).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    vat = gross - net
    accent = HexColor("#" + profile["color"])
    counterpart_ids = profile["customer_ids"] if outgoing else profile["invoice_ids"]
    address_index = counterpart_ids.index(reference)
    street = ("An der Feldmühle 12", "Gewerbebogen 34", "Zum alten Wasserturm 9", "Am Industriehof 27")[address_index]
    town = {"CB": "03050 Cottbus", "BZ": "13581 Berlin", "PR": "17291 Prenzlau"}[case["prefix"]]
    counterpart_address = street + ", " + town
    identity = int(hashlib.sha256(issuer.encode()).hexdigest()[:8], 16)
    tax_number = f"{(identity % 900) + 100:03d}/{(identity // 10 % 900) + 100:03d}/{(identity // 100 % 90000) + 10000:05d}"
    bank_iban = case["iban"] if outgoing else f"DE00 0000 0000 {identity % 10000000000:010d}"
    prepayment = reference == "PR-DEB-03"
    description = entry["description"]
    if outgoing and case["prefix"] == "PR":
        description += "; fest vereinbarte Inlands-Charterflüge über 50 km"
    paragraph = ParagraphStyle("InvoiceBody", fontName="Helvetica", fontSize=10, leading=14, spaceAfter=10)
    small = ParagraphStyle("InvoiceSmall", parent=paragraph, fontSize=8, leading=11)
    title = ParagraphStyle("InvoiceTitle", parent=paragraph, fontName="Helvetica-Bold", fontSize=23, leading=28, spaceAfter=20)
    p = lambda s, style=paragraph: Paragraph(escape(str(s)), style)
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=48, rightMargin=48, topMargin=115, bottomMargin=72,
                            title=f"Rechnung {reference}", author=issuer)
    flow = [p(recipient), p(counterpart_address if outgoing else case["address"]), Spacer(1, 20),
            p("Anzahlungsrechnung" if prepayment else "Rechnung", title), p(f"Rechnungsnummer {reference}   |   Rechnungsdatum {date_de(issue)}"),
            p(f"Leistung: {description}"),
            p("Berechnet wird die vereinbarte Anzahlung für die konkret gebuchten Inlandsflüge im Juni 2026. Die ausgegebenen Gutscheine gelten ausschließlich für diese Flüge; ein Umtausch in andere Reiseleistungen ist nicht vereinbart. Die Durchführung steht noch aus." if prepayment else
              f"Vielen Dank für Ihren Auftrag. Wir berechnen das bestätigte Liefer- beziehungsweise Leistungslos gemäß der Auftragsabrechnung. Leistungsdatum: {date_de(issue)}."),
            Spacer(1, 12)]
    rows = [[p("Pos.", small), p("Lieferung / Leistung", small), p("Netto EUR", small)],
            ["1", p(description, paragraph), money(net).replace(" EUR", "")],
            ["", "Nettobetrag", money(net).replace(" EUR", "")],
            ["", "Umsatzsteuer 19 %", money(vat).replace(" EUR", "")],
            ["", "Rechnungsbetrag", money(gross).replace(" EUR", "")]]
    table = Table(rows, colWidths=[36, 333, 130], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#E9EEF1")), ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#111111")),
        ("GRID", (0, 0), (-1, -1), .4, HexColor("#D9D9D9")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (2, 1), (2, -1), "RIGHT"), ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTNAME", (1, -1), (-1, -1), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 11), ("BOTTOMPADDING", (0, 0), (-1, -1), 11)]))
    flow.extend([table, Spacer(1, 20), p(f"Zahlbar ohne Abzug bis {date_de(due)} auf unser unten angegebenes Geschäftskonto. "
                f"Bitte geben Sie bei der Überweisung die Referenz {reference} an."),
                p("Bei Rückfragen zu Menge, Leistungsumfang oder Abrechnung wenden Sie sich bitte an unser Rechnungswesen und nennen Sie die Rechnungsnummer. Vielen Dank für die Zusammenarbeit."),
                p(f"{issuer}\nAbrechnung", small)])
    def head(canvas, document):
        canvas.setFillColor(accent)
        canvas.rect(0, A4[1] - 88, A4[0], 88, fill=1, stroke=0)
        canvas.setFillColor(HexColor("#FFFFFF"))
        canvas.setFont("Helvetica-Bold", 16 if len(issuer) < 42 else 12)
        canvas.drawString(48, A4[1] - 43, issuer)
        canvas.setFont("Helvetica", 9)
        canvas.drawString(48, A4[1] - 65, case["address"] if outgoing else counterpart_address)
        canvas.setFillColor(HexColor("#444444"))
        canvas.setFont("Helvetica", 8)
        canvas.drawString(48, 50, f"Steuernummer {tax_number}  ·  {case['bank_name']}")
        canvas.drawString(48, 37, f"IBAN {bank_iban}  ·  Zahlungsreferenz {reference}")
        canvas.drawString(48, 24, f"Geschäftsführung: {case['manager'] if outgoing else ('Nele Korn', 'Arvid Lenz', 'Mira Busse', 'Henning Rade')[address_index]}")
        canvas.drawRightString(A4[0] - 48, 24, f"Seite {document.page}")
    def factory(*args, **kwargs):
        kwargs["invariant"] = 1
        return Canvas(*args, **kwargs)
    doc.build(flow, onFirstPage=head, onLaterPages=head, canvasmaker=factory)


def office_document(path, case, item):
    doc = Document()
    section = doc.sections[0]
    section.top_margin = section.bottom_margin = Cm(2.2)
    section.left_margin = section.right_margin = Cm(2.4)
    for style_name in ("Normal", "Title", "Heading 1", "Heading 2"):
        style = doc.styles[style_name]
        style.font.name = "Times New Roman"
        rfonts = style.element.get_or_add_rPr().get_or_add_rFonts()
        for key in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme", "csTheme"):
            rfonts.attrib.pop(qn("w:" + key), None)
        for key in ("ascii", "hAnsi", "eastAsia", "cs"):
            rfonts.set(qn("w:" + key), "Times New Roman")
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.font.size = Pt(11 if style_name == "Normal" else 20 if style_name == "Title" else 13)
        for border in style.element.xpath(".//w:pBdr"):
            border.getparent().remove(border)
    doc.styles["Normal"].paragraph_format.space_after = Pt(9)
    doc.styles["Normal"].paragraph_format.line_spacing = 1.08
    header = section.header.paragraphs[0]
    header.add_run(item["issuer"]).bold = True
    header.runs[0].font.color.rgb = RGBColor.from_string(BUSINESS[case["prefix"]]["color"])
    doc.add_paragraph(item["subject"], "Title")
    doc.add_paragraph(f"{date_de(item['date'])}  |  {item['id']}")
    doc.add_paragraph(f"An: {item.get('recipient', case['company'])}")
    for paragraph in item["body"]:
        if len(paragraph) < 100 and paragraph[:1].isdigit() and " " in paragraph:
            doc.add_paragraph(paragraph, "Heading 1")
        else:
            doc.add_paragraph(paragraph)
    if item.get("signature"):
        doc.add_paragraph(item["signature"])
    footer = section.footer.paragraphs[0]
    footer.text = item["id"] + "  |  Seite "
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    footer._p.append(field)
    doc.core_properties.author = item["issuer"]
    doc.core_properties.title = item["subject"]
    doc.save(path)


def email_with_attachments(path, case, item, paths):
    mail = EmailMessage(policy=policy.SMTP)
    prefix = case["prefix"].lower()
    mail["From"] = f"{item['issuer']} <{item.get('sender', 'buchhaltung')}@{prefix}-geschaeft.example>"
    mail["To"] = f"{item.get('recipient', 'Aktenübernahme')} <eingang@verwaltung.example>"
    mail["Subject"] = item["subject"]
    mail["Date"] = format_datetime(datetime.fromisoformat(item["date"] + "T" + item.get("time", "10:17:00")).replace(tzinfo=timezone.utc))
    mail["Message-ID"] = f"<{item['id'].lower()}@{prefix}-geschaeft.example>"
    mail.set_content("\n\n".join(item["body"] + [item.get("signature", item["issuer"])]), charset="utf-8")
    for source in paths:
        mime = {".pdf": ("application", "pdf"), ".csv": ("text", "csv"),
                ".docx": ("application", "vnd.openxmlformats-officedocument.wordprocessingml.document")}[source.suffix]
        mail.add_attachment(source.read_bytes(), maintype=mime[0], subtype=mime[1], filename=source.name)
    path.write_bytes(mail.as_bytes())


def supplemental_documents(case):
    """Branchenspezifische Aktenstücke, die Belege ergänzen, keine Prüfung erledigen."""
    p = case["prefix"]
    b = BUSINESS[p]
    out = []
    def add(code, folder, kind, when, issuer, subject, body, signature=None, attachments=None):
        item = {"id": f"{p}-{code}", "folder": folder, "kind": kind, "date": when,
                "issuer": issuer, "subject": subject, "body": body,
                "signature": signature or b["contact"], "recipient": case["company"], "type": "accounting",
                "color": "#" + b["color"], "letterhead_line": {"05_Betrieb": "Betrieb und Projektabwicklung", "06_Finanzierung": "Verträge und Finanzierung", "07_Vermoegen": "Bestand und Bewertung", "08_Uebergabe": "Buchhaltung und Aktenübergabe"}[folder]}
        if attachments:
            item["attachments"] = attachments
        out.append(item)

    if p == "CB":
        add("WERK-01", "05_Betrieb", "docx", "2026-03-11", case["company"], "Schichtgespräch zur Plattform KX und zur Ofenbelegung", [
            "1 Anlass und Beteiligte", "Am 11. März haben Elin von Tannrode, Laborleiter Jan Lorentz und Disponentin Marlene Wendt den Belegungsplan für die drei Brennöfen abgestimmt. Ofen 1 läuft für Pumpengehäuse, Ofen 2 für Dichtringe. Ofen 3 ist nach dem Umbau für die neue Wärmepumpenserie vorgesehen. Die zwölf Prototypen liegen im Labor. Bei ersten Vorversuchen waren Haarrisse an drei Teilen aufgetreten; die vollständige Temperaturwechselprüfung beginnt am nächsten Tag.",
            "2 Vertrieb und Beschaffung", "Der Vertrieb hat für den Folgeabruf der Küstenwärme Systeme AG 110.000 EUR monatlichen Nettoumsatz in der Jahresplanung hinterlegt. Der Einkaufsausschuss des Kunden tagt am 13. März. Eine unterschriebene Bestellung für die Serie liegt heute nicht vor. Der Werkzeugbau hat bestätigt, dass die bereits erworbenen Formen kaum für andere Kunden nutzbar sind.",
            "3 Operative Absprachen", "Die Geschäftsführerin möchte die restlichen Prüfungen bis Freitag abschließen. Jan Lorentz hält einen weiteren Probelauf für erforderlich. Marlene Wendt soll bis zur Kundenentscheidung keine zusätzliche Toncharge für KX abrufen. Bestehende Pumpen- und Dichtungsaufträge werden weiter gefertigt. Die Gasversorgung darf während des Aufheizens nicht unterbrochen werden.",
            "Die Dokumentation hält den Gesprächsstand fest. Eine Kundenbestellung, Kreditzusage oder Änderung von Zahlungsterminen wurde in dem Gespräch nicht erklärt. Die unterschriebenen Abnahmeblätter sind im Laborordner, nicht in dieser Besprechungsdatei abgelegt." ])
        add("LAB-01", "05_Betrieb", "pdf", "2026-03-16", "Spreeglasur Qualitätslabor", "Prüfbericht KX-12 – Temperaturwechselversuch", [
            "Prüfgegenstand sind zwölf keramische Dichtkörper des Prototypenloses KS-2611. Das Labor hat die Körper vom 12. bis zum 16. März in drei Serien mit je vier Körpern geprüft. Die vereinbarten Eckdaten lauten 40 Temperaturwechsel zwischen 20 und 180 Grad Celsius sowie anschließende Dichtigkeitsprüfung unter 8 bar.",
            "Bei den Proben 3, 7 und 11 trat vor dem 40. Wechsel eine sichtbare Randrissbildung auf. Die übrigen Proben bestanden den Drucktest. Zur Ursache kommen die geänderte Bindercharge und die Haltezeit im Brennprogramm in Betracht. Eine abschließende Zuordnung ist ohne Wiederholung nicht möglich.",
            "Die Erstprüfung enthält keinen Nachweis dafür, dass die Serienanforderung für sämtliche Proben erfüllt ist. Der Kunde hat um Übersendung der Einzelmessreihen gebeten. Diese liegen als Geräteausdruck im Labor; der USB-Export war beim heutigen Versand nicht lesbar. Die Lieferung des Prototypen wird hiervon getrennt behandelt.",
            "Versand: 16. März 2026, 08:42 Uhr, an Marta Enke. Im ERP ist weiterhin die Angebotsnummer KX-26 hinterlegt. Das Feld Auftragseingang wurde vom Vertrieb bisher nicht auf eine bestätigte Bestellung geändert." ], "Jan Lorentz, Laborleitung")
        add("GAS-02", "05_Betrieb", "pdf", "2026-05-12", "Lausitz Industriegas GmbH", "Jahresabrechnung und Fortsetzung der Versorgung", [
            "Die am 11. Mai fällige Jahresabrechnung CB-GAS-01 über 122.000 EUR ist auf unserem Vertragskonto offen. Sie umfasst den Verbrauchsausgleich für die Brennöfen und den Leistungsbezug außerhalb des bisherigen Abschlags. Die Rechnung ist Ihrer Buchhaltung am 21. April zugegangen. Eine vereinbarte Stundung ist nicht hinterlegt.",
            "Im Telefonat am 12. Mai baten Sie um Aufteilung in vier Monatsraten. Wir haben zugesagt, den Antrag nach Vorlage einer unterschriebenen Planung zu prüfen. Eine Zustimmung liegt noch nicht vor. Bis zur Entscheidung bleiben Rechnung und Fälligkeit bestehen. Bitte bestätigen Sie, ob die am 8. Mai an die Werkofen Service OHG freigegebene Investitionsrate den beantragten Gaszahlungsplan beeinflusst.",
            "Die aktuelle Versorgung wird bis zur technischen Abstimmung zunächst aufrechterhalten. Daraus folgt keine Änderung des Zahlungsziels. Eine Abschaltung im laufenden Brand wäre nach Ihrer Mitteilung mit erheblichen Schäden verbunden. Unsere technische Disposition stimmt deshalb einen sicheren Termin mit Ihrer Werksleitung ab.",
            "Bitte übermitteln Sie uns bis zum 15. Mai die angeforderten Unterlagen. Unabhängig davon behalten wir uns die Rechte aus dem Liefervertrag vor." ], "Sören Witt, Forderungsmanagement")
        add("FIN-02", "06_Finanzierung", "pdf", "2026-03-03", "Spreebogen Beteiligungsholding GmbH", "Meldung der verfügbaren Zahlungsmittel an die Tochtergesellschaft", [
            "Zum 2. März beträgt das freie Guthaben unserer Holding 62.000 EUR. Die Meldung betrifft ausschließlich das Holdingkonto. Das Konto der Spreeglasur ist darin nicht enthalten. Die Holding hat keine ungenutzte Kreditlinie und keine Liquiditätszusage eines anderen Gesellschafters.",
            "Für März sind Büro- und Beratungsausgaben von zusammen 8.400 EUR vorgesehen. Die Geschäftsführung erwartet Erlöse aus einem möglichen Beteiligungsverkauf, hat dazu aber weder einen unterschriebenen Kaufvertrag noch einen Zahlungstermin. Die Beteiligung ist bislang nur zwei Interessenten vorgestellt worden.",
            "Unsere Erklärung vom 2. März bleibt eine Erklärung zur geschäftlichen Unterstützung. Die vorliegende Meldung ist kein Zahlungsauftrag und keine Bewilligung einer zusätzlichen Einlage. Über eine etwaige Einzahlung entscheidet die Gesellschafterversammlung gesondert. Bis zur heutigen Meldung ist kein entsprechender Beschluss gefasst." ], "Aenne von Tannrode")
        add("DAR-02", "06_Finanzierung", "pdf", "2026-03-13", case["bank_name"], "Salden- und Sicherheitenbestätigung OF-109", [
            "Das Laufzeitdarlehen OF-109 weist einschließlich der für Mai vorgesehenen Tilgungsrate einen Kapitalstand von 1.040.000 EUR aus. Die offene Rate von 58.000 EUR ist Bestandteil dieses Kapitalstands. Ein weiterer Auszahlungsanspruch aus dem Laufzeitdarlehen besteht nicht.",
            "Gesichert ist die Forderung durch die Grundschuld am Betriebsgrundstück und durch Sicherungseigentum an den drei Brennöfen. Die Sicherheitenüberlassung ist keine zusätzliche Darlehensvaluta. Über einen Verkauf der Sicherungsgegenstände und deren Freigabe ist vorab eine gesonderte Vereinbarung zu schließen.",
            "Die Zwischenlinie über 90.000 EUR ist ein eigenständiger Vertrag und endet am 30. April 2026. Eine Verlängerung ist bisher nicht beschlossen. Eine bloße Anfrage oder ein im Firmenkundenportal angezeigter alter Rahmen stellt keine Auszahlungserlaubnis nach Laufzeitende dar.",
            "Diese Bestätigung dient dem Abgleich der Darlehens- und Sicherheitenakten. Sie enthält keine Änderung der bisherigen Raten. Ein späterer Nachtrag zur Mai-Rate ist dem Vertrag gesondert beizufügen." ], "Betina Riedel, Kreditabteilung")
        add("INV-11", "07_Vermoegen", "pdf", "2026-03-12", "Gewerbegrund Lausitz Immobilien GmbH", "Indikative Preiseinschätzung – Brennring 17", [
            "Besichtigt wurden Produktionshalle, Laboranbau und das im Eigentum der Spreeglasur stehende Grundstück am Brennring 17. Das zusätzlich angemietete Außenlager an der Werkbahn ist nicht Bestandteil des Eigentumsgrundstücks und nicht in dieser Einschätzung enthalten.",
            "Aus zwei jüngeren Vergleichsverkäufen ergeben sich Kaufpreisindikationen um 590.000 EUR. Bei einer Einzelverwertung rechnen wir mit 25.000 EUR notwendigen Verkaufs-, Räumungs- und Vermarktungskosten. Daraus ergibt sich eine Erlöserwartung von 565.000 EUR vor Ablösung der Grundschuld. Der Anlagenbuchwert von 405.000 EUR betrifft denselben Vermögensgegenstand.",
            "Die Grundschuld ist kein zusätzlicher Abzug für die Ermittlung des unverschuldeten Immobilienwerts. Welcher Anteil des Erlöses an die Bank zu zahlen wäre, ist anhand der gesicherten Forderung und der Freigabevereinbarung zu klären. Unsere Kostenschätzung enthält keine Ablösung des Darlehens.",
            "Ein Kaufangebot liegt noch nicht vor. Selbst bei sofortigem Vermarktungsbeginn wären Due Diligence, notarielle Beurkundung, Lastenfreistellung und Kaufpreisfälligkeit abzuwarten. Einen Zahlungseingang innerhalb der nächsten drei Wochen können wir nicht zusagen." ], "Nela Rehberg, Gewerbeimmobilien")
        add("INV-12", "07_Vermoegen", "pdf", "2026-03-12", "Ofenmarkt Ost Verwertungs GmbH", "Abholangebot für drei Brennöfen und Nebenaggregate", [
            "Unser Kaufinteresse betrifft die Anlagen O-101, O-102 und O-103 samt Steuerungen und Abgasführung bis zum Hallenanschluss. Wir bieten für die Gesamtheit 318.000 EUR. Die in der Hallenakte benannte Grundsteuerung gehört zu O-103 und wird nicht zusätzlich vergütet.",
            "Für Trennung, Verpackung, Kranstellung und Abtransport sind nach unserer Besichtigung 40.000 EUR anzusetzen. Bei Übernahme dieser Arbeiten durch uns verbleiben 278.000 EUR. Schäden aus einem unsachgemäßen Abkühlen wären gesondert zu bewerten; das Angebot setzt die dokumentierte Temperaturabsenkung voraus.",
            "Die Maschinen sind für spezielle Losgrößen eingerichtet. Die historische Anschaffung und der fortgeführte Buchwert von 704.000 EUR lassen sich auf dem Zweitmarkt nicht erzielen. Ersatzteilspender werden derzeit zu deutlich niedrigeren Preisen angeboten. Das Angebot gilt nur für die im Inventar aufgeführten eigenen Anlagen.",
            "Die bankseitige Freigabe und ein schriftlicher Kaufvertrag fehlen. Wir zahlen nach Demontagekontrolle und Eigentumsfreigabe. Ein kurzfristiger Zufluss vor diesen Schritten ist nicht vereinbart." ], "Malte Gering, Maschinenverwertung")
        add("INV-13", "07_Vermoegen", "docx", "2026-03-13", case["company"], "Inventurblatt – Rohstoffe, Formen und fertige Restlose", [
            "1 Bestandsaufnahme", "Die Lagerzählung wurde am 13. März von Annika Roth und Laborleiter Jan Lorentz vorgenommen. Einbezogen wurden Tonmischungen, Binder, Standarddichtringe und kundenspezifische Restlose. Der Buchbestand beträgt zusammen 178.000 EUR. Fremdformen mit Kundeneigentumsmarkierung stehen in einem gesonderten Regal und sind in diesem Betrag nicht enthalten.",
            "2 Verwertbare Bestände", "Für Standardton und ungeöffnete Bindergebinde liegen Händlerindikationen von 52.000 EUR vor. Die Standarddichtringe können nach Sortierung voraussichtlich 23.000 EUR erlösen. Beide Beträge sind nach den angebotenen Abholkosten angesetzt. Zusammen werden in der Inventurliste 75.000 EUR vermerkt.",
            "3 Gesperrte Restlose", "Die Prototypenteile KX-12 sind wegen der Rissprüfung gesperrt. Kundenindividuelle Formen haben ohne Übernahme der entsprechenden Produktserie keinen nachgewiesenen Zweitmarkt. Für diese Positionen ist in der Händlerabfrage kein Preis genannt. Eine spätere Nacharbeit ist damit nicht ausgeschlossen, aber noch nicht beauftragt.",
            "Die Inventur ist mengenbezogen. Sie bestätigt weder die Bezahlung einzelner Lieferungen noch die Freigabe vorbehaltener Ware. Nach der Zählung eingehende Lieferungen sind mit ihrem eigenen Wareneingangsdatum zu erfassen. Das Papier-Zählblatt liegt bei der Lagerleitung." ])
        add("TON-03", "05_Betrieb", "eml", "2026-06-22", "Spreeglasur Wareneingang", "Toncharge T-629: Rechnung und gesperrte Palette", [
            "Die Rechnung CB-TON-02 über 16.000 EUR ist in der Postmappe. Wir widersprechen der Rechnung derzeit in voller Höhe, weil die gesamte Charge die vereinbarte Korngröße überschreitet. Das Material wurde nur entladen und nicht verarbeitet. Das Wareneingangsblatt ist kein Abnahmevermerk.",
            "Der Lieferant meint am Telefon, die Werte lägen noch innerhalb seiner Allgemeinen Lieferbedingungen. Uns liegt jedoch die auftragsspezifische Körnungsvorgabe vor. Die Geschäftsführerin hat keine Ratenzahlung und kein Anerkenntnis freigegeben. Bitte den Posten im Buchungssystem nicht als bezahlt oder ausgebucht kennzeichnen.",
            "Annika hat die zwei Probenbeutel im Labor hinterlegt. Die Messreihe aus der eigenen Siebung und die vom Lieferanten angekündigte Gegenprobe fehlen noch im digitalen Ordner. Ich kann die Originale morgen aus dem Wareneingang holen." ], "Annika Roth, Wareneingang")
        add("RUECK-02", "07_Vermoegen", "pdf", "2026-03-13", "Lausitz Netze und Anschluss GmbH", "Anschlussstück Werkbahn – Rückbau bei endgültiger Aufgabe", [
            "Nach Ziffer 9 des Anschlussvertrags ist die betriebliche Gasübergabestation einschließlich der nur für Ihr Werk verlegten Leitung nach endgültiger Aufgabe und Rückgabe des Anschlussstücks zu entfernen. Die laufende Produktion löst noch keine Rückbauleistung aus.",
            "Unser Unternehmerangebot vom 10. März beläuft sich einschließlich Freimessen, Tiefbau und Oberflächenwiederherstellung auf 38.000 EUR. Das Angebot erfasst die Arbeiten am Anschlussstück und enthält nicht den Rückbau der Brennöfen. Es ist deshalb nicht in den Demontagekosten des Maschinenhändlers enthalten.",
            "Wir haben mit Ihrem technischen Leiter noch keinen Einstellungstermin vereinbart. Bei Fortführung bleiben die laufenden Anschlussbedingungen bestehen. Eine Vertragsaufhebung oder ein Verzicht auf die Rückbaupflicht ist nicht erklärt." ], "Renate Voigt, Anschlussmanagement")
        add("MIETE-02", "06_Finanzierung", "pdf", "2026-02-27", "Spreeufer Liegenschaften KG", "Vereinbarung über die Beendigung des Außenlagers", [
            "Die Parteien beenden den Mietvertrag über das Außenlager an der Werkbahn 12 zum 30. November 2026. Die Produktionshalle Brennring 17 ist von dieser Vereinbarung nicht betroffen. Die Zahlung der laufenden Monatsmiete bis zum Beendigungsdatum bleibt bestehen.",
            "Zur Abgeltung der restlichen Bindung aus dem Festmietvertrag zahlt Spreeglasur Industriekeramik GmbH eine einmalige Abfindung von 47.000 EUR am 1. Dezember 2026. Die Abfindung ist zusätzlich zur laufenden Miete vereinbart. Sie ist nicht bereits mit den in der laufenden Buchhaltung erfassten Mietzahlungen erfüllt.",
            "Die KG verzichtet mit Zahlung der Abfindung auf weitere Ansprüche aus der Restlaufzeit. Die Gesellschaft räumt das Lager bis zum 30. November besenrein. Über einen früheren Rückgabetermin oder einen Erlass der Abfindung bedarf es einer gesonderten Vereinbarung. Beide Parteien haben die vorliegende Fassung unterschrieben." ], "Karin Feldt und Elin von Tannrode")
    elif p == "BZ":
        add("MONT-01", "05_Betrieb", "docx", "2026-04-14", case["company"], "Montagebesprechung Südspange – Aufmaß und Geldlauf", [
            "1 Beteiligte und Stand", "Juno Bern von Hallern, Werkstattleiter Bernd Kolbe und Tillmann Seifert haben die offenen Baustellen besprochen. Die Geländer des Loses Südspange sind montiert. Am letzten Handlauf fehlt ein Schutzstopfen; die Bauleitung hat dafür keinen Einbehalt aus der Schlussrate verlangt. Die schriftliche Freigabe des Kunden betrifft 37.000 EUR.",
            "2 Offene Abrechnung", "Die Zahlung soll am 23. April auf dem Geschäftskonto eingehen. Die separate Materialvorfinanzierung über 92.000 EUR ist beantragt. Eine Antwort der Geschäftsführung des Baukontors steht noch aus. Die Werkstatt hat den erwarteten Abschlag in ihrer eigenen Wochenliste mit einem Fragezeichen versehen.",
            "3 Stahl und Personal", "Der Stahlhandel hat den Altposten von 128.000 EUR bis zum 20. April verschoben. Tillmann hält einen weiteren Aufschub für verhandelbar; die Geschäftsführerin verlangt dazu eine unterschriebene Bestätigung. Die Lohnliste und die Sozialversicherungsdatei sollen unabhängig vom Kundenlauf fristgerecht vorbereitet werden.",
            "Die freigegebene Schlussrate und der erbetene neue Abschlag stammen aus unterschiedlichen Vorgängen. Montageleitung und Buchhaltung sollen die Auftragsnummern bei jeder Rückfrage mitführen, damit die April-Freigabe nicht versehentlich für den Mai-Abschnitt verwendet wird." ])
        add("STA-02", "06_Finanzierung", "pdf", "2026-04-21", "Südspange Stahlhandel GmbH", "Offene Rechnung S-2268 – kein weiterer Zahlungsaufschub", [
            "Der schriftlich auf den 20. April verlegte Betrag von 128.000 EUR ist auf unserem Konto nicht eingegangen. Sie baten gestern telefonisch um zwei weitere Wochen. Wir haben erklärt, dass wir die Angelegenheit intern vorlegen. Eine Zustimmung zu einer Verlängerung wurde nicht erteilt.",
            "Nach heutiger Entscheidung verlangen wir den vollständigen Ausgleich der Rechnung. Die Ware wurde geliefert und nach Ihrem Wareneingangsprotokoll verarbeitet. Ein Mangel ist uns zu dieser Lieferung nicht angezeigt. Unsere Entscheidung betrifft nur S-2268 und ändert nichts an späteren Einzelbestellungen.",
            "Ihr Hinweis auf eine noch ausstehende Baustellenzahlung ist zur Kenntnis genommen. Bitte teilen Sie bis zum 23. April mit, wann ein konkreter Zahlungseingang gesichert ist. Wir verzichten durch diese Anfrage weder auf die Fälligkeit noch auf die Geltendmachung unserer Forderung." ], "Hanno Burk, Geschäftsführung")
        add("FASS-01", "05_Betrieb", "pdf", "2026-04-16", "Fassadenbau Kreiser GmbH", "Prüfvermerk Aufmaß 3 – Hauptauftrag und Fensterbandnachtrag", [
            "Das Aufmaß 3 für Fassade 7 wurde mit dem örtlichen Bauleiter am 16. April abgeglichen. Aus dem Hauptauftrag werden 24.000 EUR einschließlich Umsatzsteuer freigegeben. Die Zahlungsanweisung ist für den 11. Mai vorgesehen. Der Rücklauf der unterschriebenen Aufmaßseite ist in der kaufmännischen Akte erfasst.",
            "Die zusätzlich mit 74.000 EUR berechneten Fensterbandänderungen sind in diesem Aufmaß nicht enthalten. Der Baustellenleiter hat lediglich bestätigt, dass einzelne Maße vor Ort angepasst wurden. Eine Vollmacht zur Nachtragsbeauftragung über den vorgesehenen Kleinbetragsrahmen hinaus wurde ihm nicht erteilt.",
            "Schlachtensee Stahl & Form beruft sich auf die technische Notwendigkeit der Änderung. Unser Projektleiter hält die Mehrkosten teilweise für bereits vom Pauschalpreis erfasst. Die Originalanfrage und die Kalkulation fehlen noch. Eine Anerkennung der Nachtragsforderung oder ein Zahlungstermin für diese Position ist mit dem Prüfvermerk nicht verbunden." ], "Aylin Krause, Projektabrechnung")
        add("NR-02", "06_Finanzierung", "eml", "2026-04-11", "Waldhafen Vermögensverwaltung GmbH", "Unterzeichnete Rangvereinbarung und falsches Stammdatenfeld", [
            "Die gestern von beiden Geschäftsführungen unterschriebene Vereinbarung BZ-NR-01 ist beigefügt. Sie erfasst die 185.000 EUR einschließlich der bis zur Unterzeichnung aufgelaufenen Zinsen. Weitere Forderungen unserer Gesellschaft gegen Schlachtensee bestehen nach unserem Abstimmungsblatt nicht.",
            "Im alten Nebenbuch steht weiterhin das Zahlungsziel 30. Juni. Das ist das technische Stammdatenfeld aus dem Darlehensvertrag, nicht eine neue Zahlungsaufforderung. Bitte die Vereinbarung dauerhaft zum Darlehenskonto ablegen. Die Forderung soll nicht aus dem Handelsbilanzkonto verschwinden, nur weil ihre Bedienung beschränkt ist.",
            "Der von uns am 9. April versandte Text ohne Unterschriften war ein Entwurf. Maßgeblich ist die beigefügte unterschriebene Fassung. Eine Kündigung oder Aufhebungsvereinbarung haben wir nicht erklärt." ], "Nora Villbrandt", ["03_Korrespondenz/BZ-NR-01.pdf"])
        add("DAR-02", "06_Finanzierung", "pdf", "2026-04-17", case["bank_name"], "Hallendarlehen – Saldo, Kreditlinie und Freigabebedingungen", [
            "Der Kapitalstand des Hallendarlehens beträgt 640.000 EUR. Die Forderung ist durch eine Grundschuld am Werksgrundstück gesichert. Die Forderung ist im Darlehenskonto geführt und nicht nochmals in den offenen Lieferantenposten enthalten. Tilgungen erfolgen nach dem bisherigen Vertragsplan.",
            "Der freie Kontokorrentrahmen von 15.000 EUR kann bis zum Ablauf des 30. April über die eingerichtete Disposition genutzt werden. Nach Ablauf besteht ohne neue Kreditentscheidung kein weiterer Auszahlungsanspruch. Der für Mai eingereichte Verlängerungsantrag ist noch nicht bewilligt.",
            "Für eine Grundstücksveräußerung benötigen wir Kaufvertragsentwurf, Lastenaufstellung und eine Abwicklungsvereinbarung. Die Bank hat bisher keinen Betrag aus einem bloß erwarteten Kaufpreis zur freien Verwendung freigegeben. Eine Grundschuld mindert nicht die bestehende Darlehensforderung; die Erlösverteilung wird bei einer tatsächlichen Veräußerung festgelegt." ], "Meret Claus, Firmenkunden")
        add("INV-11", "07_Vermoegen", "pdf", "2026-04-17", "Tabea Rohde · Immobilienbewertung", "Werksgelände Zehlendorf – erste Marktindikation", [
            "Die Werkhalle wurde am 15. April von innen und außen besichtigt. Der Buchwert von 310.000 EUR betrifft Grundstück und Halle. Zwei Interessenten nannten unverbindliche Kaufpreisgrößen von 920.000 EUR. Für Veräußerung und vorbereitende Räumung werden 25.000 EUR abgezogen. In der Vergleichsliste stehen daher 895.000 EUR.",
            "Die Einschätzung setzt voraus, dass die im Lageplan gezeichnete Zufahrt für Lieferfahrzeuge und Feuerwehr dauerhaft genutzt werden darf. Die Geschäftsführung hat auf einen alten Kaufvertrag verwiesen. Ein vollständiger Grundbuchauszug mit Bewilligungsunterlagen lag bei der Besichtigung nicht vor. Die Annahme ist im Bewertungsblatt ausdrücklich vermerkt.",
            "Die Interessenten haben weder ein bindendes Angebot noch einen Kaufvertrag abgegeben. Kaufpreiszahlung setzt unter anderem Lastenfreistellung und eine gesicherte Zufahrt voraus. Der Betrag ist keine kurzfristig abrufbare Finanzierungsquelle. Die für Maschinen und Vorräte erfragten Händlerpreise sind nicht im Immobilienpreis enthalten." ], "Tabea Rohde")
        add("WEG-01", "07_Vermoegen", "pdf", "2026-05-18", "Hofwinkel Grundstücksverwaltung GmbH", "Nutzung unseres Hofgrundstücks – Einstellung des Schwerlastverkehrs", [
            "Nach Auswertung der Bewilligungsunterlagen und des am 17. Mai beurkundeten Anerkenntnisses umfasst das bestehende Wegerecht lediglich Fußgänger und gewöhnliche Pkw. Eine Benutzung durch Lastzüge, Sattelauflieger oder schwere Einsatzfahrzeuge wird von uns nicht gestattet.",
            "Wir hatten die Belieferung in der Vergangenheit zeitweise geduldet. Aus der Duldung ist keine Erweiterung der eingetragenen Befugnisse vereinbart worden. Die zur Diskussion gestellte zusätzliche Dienstbarkeit wird nicht bestellt. Die Gesprächsvorschläge Ihres Maklers vom 12. Mai sind damit erledigt.",
            "Ab sofort dürfen keine schweren Fahrzeuge über unseren Hof disponiert werden. Bitte informieren Sie Ihre Transporteure. Über die Folgen für Ihre Betriebs- oder Brandschutzorganisation können wir keine Auskunft erteilen. Eine Vereinbarung über Entschädigung oder einen alternativen Zufahrtsstreifen ist nicht geschlossen." ], "Levin Röser, Geschäftsführung")
        add("INV-12", "07_Vermoegen", "pdf", "2026-05-18", "Spreelager Projekt GmbH", "Befristete Kaufpreisindikation für Lagernutzung", [
            "Nach heutiger Besichtigung kommt für uns eine Nachnutzung ohne Schwerlastverkehr in Betracht. Unter den besprochenen Voraussetzungen bieten wir einen Kaufpreis von 570.000 EUR an. Auf Verkäuferseite erwartete Veräußerungs- und Räumungskosten von 25.000 EUR sind in unserer internen Erlösübersicht berücksichtigt; dort verbleiben 545.000 EUR.",
            "Das Angebot steht unter dem Abschluss eines notariellen Vertrags und der Bestätigung, dass die vorgesehene Lagernutzung genehmigungsrechtlich zulässig ist. Es gilt bis zum 1. Juni. Die Maschinen, das Warenlager und alle Verpflichtungen der Verkäuferin werden nicht übernommen.",
            "Der Kaufpreis soll erst nach Eintritt der üblichen notariellen Fälligkeitsvoraussetzungen gezahlt werden. Eine Anzahlung wird nicht angeboten. Die Ablösung Ihrer Grundschuld ist aus dem Kaufpreis abzuwickeln. Wir haben keinen Termin zugesagt, an dem bereits in den kommenden drei Wochen Geld zur Verfügung stünde." ], "Leonie Wendel, Projektentwicklung")
        add("GEW-02", "07_Vermoegen", "docx", "2026-04-16", case["company"], "Baustellenakte – zwei offene Nachbesserungsvorgänge", [
            "1 Treppenanlage Sonnenhof", "Bei der Treppenanlage Sonnenhof ist die Beschichtung im Anschlussbereich abgeplatzt. Der Auftraggeber hat Nacherfüllung verlangt. Das Angebot des Beschichtungsunternehmens umfasst Ausbau, Transport, neue Beschichtung und Wiedermontage mit 41.000 EUR. Der Schaden ist durch die gemeinsame Besichtigung dokumentiert. Eine zusätzliche Geldforderung des Kunden liegt nicht vor.",
            "2 Geländer Uferkontor", "Bei Uferkontor stimmt der Achsabstand mehrerer Geländerfelder nicht mit dem freigegebenen Plan überein. Eine Weiterverwendung ist nach dem Bauleiterprotokoll ausgeschlossen. Die Kalkulation für Ersatzfelder und Montage beträgt 56.000 EUR. Eine Versicherungszusage liegt nicht vor. Die Geschäftsführung hat um eine gesonderte Deckungsprüfung gebeten.",
            "3 Stand der Erfassung", "Die beiden Vorgänge ergeben zusammen 97.000 EUR. Die Kosten sind in der Liste BZ-GEW-01 erfasst. Sie gehören nicht zu der Nachtragsrechnung über 74.000 EUR an Fassadenbau Kreiser und dürfen nicht mit dieser verrechnet werden. Die Lieferantenangebote gelten für genau die beschriebenen Nacharbeiten.",
            "Die Bauleitung hat Fotos, Aufmaße und E-Mail-Verkehr in ihrer Baustellenablage. Die vorliegende Zusammenstellung bestätigt die heute bekannten Arbeiten. Ob der Auftraggeber eine Ausführung durch einen Dritten beauftragt, steht noch nicht fest." ])
        add("INV-13", "07_Vermoegen", "pdf", "2026-04-16", "Havel Maschinenhandel OHG", "Abholpreise für Maschinen, Fahrzeuge und freie Bestände", [
            "Für Schweißroboter, Brennschneider und Montagefahrzeuge aus Ihrer Liste bieten wir insgesamt 165.000 EUR nach Abbau- und Transportkosten. Die Geräte sind vor Übernahme anhand der Seriennummern zu prüfen. Der Buchwert von 255.000 EUR ist für unser Angebot nicht maßgeblich.",
            "Für marktgängige freie Stahlprofile und nicht auf bestimmte Kunden zugeschnittene Treppenteile ergibt die Mengenabfrage 55.000 EUR nach Abholkosten. Kundeneigene Teile und mit Eigentumsvorbehalt gekennzeichnete Lieferungen sind in unserem Kaufinteresse nicht enthalten. Der Warenbuchwert von 125.000 EUR ist davon zu unterscheiden.",
            "Wir übernehmen weder Nachbesserungspflichten noch Aufträge Ihrer Kunden. Die Rechnungen zu den Maschinen und der Nachweis über die Ablösung etwaiger Sicherheiten sind vor Kauf erforderlich. Die Preisabfrage ist noch kein angenommener Kaufvertrag. Eine sofortige Barauszahlung ist nicht vereinbart." ], "Otto Wernitz")
        add("WERK-02", "05_Betrieb", "eml", "2026-05-19", "Schlachtensee Werkstattleitung", "Zufahrt gesperrt – Morgenlieferung und Speditionsabsprache", [
            "Der Nachbar hat seit gestern Poller vor den Hof gesetzt. Der normale Werkstattwagen passt durch die Pkw-Zufahrt. Der bestellte Sattelzug nicht. Wir mussten die morgen geplante Abholung der großen Träger absagen. Der Spediteur bietet uns noch keinen Ersatztermin an.",
            "Die Kollegen können kleinere Teile weiter fertigstellen. Für die großen Baugruppen fehlen vorerst Verladung und Abtransport. Bitte unterscheiden Sie die bereits abgeschlossenen Aufträge von den noch nicht ausgelieferten Teilen. Eine Rechnung für die noch nicht abgenommenen Träger habe ich nicht freigegeben.",
            "Im alten Lageplan ist der Hofweg als Zufahrt eingezeichnet. Ich hatte deshalb bisher angenommen, dass wir ihn dauerhaft benutzen dürfen. Den Text der Dienstbarkeit habe ich erst heute gesehen. Bitte den Plan nicht ohne die heutige Nachricht an Interessenten weiterreichen." ], "Bernd Kolbe")
    else:
        add("FLOT-01", "05_Betrieb", "docx", "2026-04-29", case["company"], "Flottenblatt und Eigentumsunterlagen – sechs Maschinen", [
            "1 Eigene Maschinen", "Die internen Flottennummern U-01 und U-02 stehen im Eigentum der Uckerbogen Rotorcharter GmbH. Beide sind der Bank zur Sicherung des Fluggerätedarlehens übereignet. Die Kauf- und Sicherheitenverträge liegen in der Fluggeräteakte. Der zusammengefasste Buchwert beträgt 755.000 EUR. Die Haltereintragung ersetzt die Prüfung des Eigentums nicht.",
            "2 Leasingmaschinen", "U-03, U-04, U-05 und U-06 gehören der Fluggeräte Pool Ost GmbH. Die Gesellschaft nutzt sie nach vier zusammengefassten Leasingverträgen. Die Maschinen stehen auf dem Hof, sind aber nicht als eigene Vermögenswerte im Anlagenbuch erfasst. Die eigenen Funkgeräte und lose mitgeführten Werkzeuge sind in der separaten Geräteliste geführt.",
            "3 Betrieb und Wartung", "U-02 ist nach der Triebwerksüberholung wieder für die Einsatzplanung vorgesehen. Die technische Dokumentation muss vollständig bleiben. Bei U-05 steht im Juni eine planmäßige Werkstattphase an. Die 140 Stunden des Sommerkontingents wurden bislang auf die gesamte Flotte verteilt.",
            "Das Flottenblatt enthält keine neuen Flugzulassungen oder behördlichen Freigaben. Für jede Maschine ist der jeweils aktuelle technische Status der Betriebsakte zu entnehmen. Die internen Nummern dienen der eindeutigen Zuordnung und sind keine Luftfahrzeugkennzeichen." ])
        add("CHART-01", "05_Betrieb", "pdf", "2026-04-24", "Waldseen Charterreisen GmbH", "Vertragsblatt WC-112 – Sommerkontingent und Rücktritt", [
            "Waldseen bestellt ein Kontingent von 140 Hubschrauberstunden für das Sommerprogramm am Uckerbogen. Der Einsatzzeitraum läuft von Juni bis August 2026. Die genaue Verteilung richtet sich nach dem abgestimmten Flugplan und den zulässigen Betriebsbedingungen. Die elf separat gebuchten Transfers werden über eigene Vorgangsnummern abgerechnet.",
            "Bei vollständiger Absage des zugrunde liegenden Großevents durch dessen Veranstalter kann Waldseen bis einschließlich 4. Mai vom Hauptkontingent zurücktreten. Der Rücktritt ist per E-Mail an die Charterdisposition zu erklären. Für das wirksam abbestellte Kontingent fällt keine Stornopauschale an. Die gesonderten Transfers bleiben bestehen.",
            "Abschläge aus dem Hauptkontingent werden nur bei Fortbestand der Buchung und nach dem abgestimmten Monatsplan gezahlt. Eine bloße Disposition der Flotte begründet keinen davon unabhängigen Vorschussanspruch. Die Vertragsunterlagen sind von beiden Unternehmen freigegeben; Änderungen bedürfen einer bestätigten Nachricht beider Seiten.",
            "Die angehängte Stundenverteilung ist eine Einsatzplanung. Sie ist nicht als separater Auftrag für 140 weitere Stunden zu erfassen. Bitte verknüpfen Sie die Planung im Dispositionsprogramm mit WC-112." ], "Sabrina Pott, Vertragsplanung")
        add("PAT-03", "06_Finanzierung", "pdf", "2026-03-04", "Wolkenhain Beteiligungs KG", "Liquiditätsnachweis zur Ausstattungszusage", [
            "Das freie Bankguthaben der Wolkenhain Beteiligungs KG beträgt am 4. März 610.000 EUR. Laut Bankauskunft besteht kein Pfandrecht an diesem Guthaben. Für die laufenden eigenen Verpflichtungen bis Ende Mai sind in der internen Finanzübersicht 91.000 EUR vorgesehen. Eine weitere gleichzeitig zugesagte Stützung eines anderen Beteiligungsunternehmens besteht nicht.",
            "Die Ausstattungszusage an Uckerbogen ist auf insgesamt 360.000 EUR begrenzt. Der Anspruch setzt die vereinbarte Anforderung mit Zahlungsplan und fälligen betrieblichen Ausgaben voraus. Die Bearbeitung erfolgt über das Anforderungspostfach. Die finanzielle Auskunft ersetzt diese Anforderung nicht.",
            "Die Zusage endet für neu entstehende Lücken mit Ablauf des 3. Mai. Das freie Guthaben der Holding wird nicht auf ein Konto der Tochter umgebucht und ist nicht deren allgemeines Bankguthaben. Bereits rechtzeitig und vertragsgemäß geltend gemachte Ansprüche bleiben nach der Vereinbarung gesondert zu erfüllen." ], "Lou von Kleist")
        add("PAT-04", "06_Finanzierung", "docx", "2026-04-28", case["company"], "Besprechungsstand – gewünschte Verlängerung der Ausstattungszusage", [
            "1 Gespräch", "Skyler von Falkenhag hat Lou von Kleist am 28. April um Verlängerung der Liquiditätsstützung bis Ende August gebeten. Die Holding will die Entscheidung ihres Gesellschafterkreises abwarten. Im Gespräch wurde keine verbindliche Zusage abgegeben. Ein unterzeichneter Nachtrag liegt nicht vor.",
            "2 Von Uckerbogen gewünschte Fassung", "Nach der Vorstellung der Geschäftsführung soll die bisherige Höchstsumme von 360.000 EUR weitergelten und die Frist bis Ende August verlängert werden. Die Zahlungsanforderung soll weiterhin einen taggenauen Bedarf enthalten. Die Holding hat weder diese Frist noch die neue Fortdauer bestätigt.",
            "3 Offene Aufgaben", "Malin Stange soll das Sommerprogramm und die Wartungsplanung beifügen. Das endgültige Ergebnis des Veranstalters steht noch aus. Die Datei darf deshalb noch nicht als Vertragsnachtrag ins Finanzierungsarchiv umbenannt werden. Sie dokumentiert den beantragten Gesprächsstand und enthält keine Unterschriften der Holding." ])
        add("PAT-05", "06_Finanzierung", "pdf", "2026-05-04", "Wolkenhain Beteiligungs KG", "Protokoll des Anforderungspostfachs 4. März bis 3. Mai", [
            "Das Anforderungspostfach wurde am 4. Mai mit der Buchhaltung abgeglichen. Eingegangen sind am 28. April die Bitte um Vertragsverlängerung und am 30. April die Monatsübersicht. Beide Nachrichten verlangten eine Verlängerung für spätere Mittelbedarfe und enthielten keinen Antrag auf Auszahlung für eine bis zum 3. Mai entstandene fällige Lücke.",
            "Aus dem bisherigen Ausstattungsvertrag ist nach unserem Postfach- und Zahlungsabgleich kein rechtzeitig angeforderter und noch offener Ausgleichsbetrag bekannt. Bitte weisen Sie uns unverzüglich auf eine anderswo zugegangene konkrete Zahlungsanforderung hin. Wir haben nur das vertraglich benannte Postfach und die beiden Geschäftsführungsadressen geprüft.",
            "Die heute versandte Ablehnung betrifft die Verlängerung für neue Mittelbedarfe. Sie soll keine bereits wirksam entstandene Forderung beseitigen. Ein Antrag auf Verlängerung wird von uns nicht als automatische Zahlungsermächtigung behandelt." ], "Lea Kranz, Holdingbuchhaltung")
        add("KART-01", "06_Finanzierung", "pdf", "2026-02-03", case["bank_name"], "Nachtrag zum Kartenakzeptanzvertrag – Rückbelastungsreserve", [
            "Die Bank darf bei erhöhtem Rückbelastungsrisiko einen begründeten Teil des Guthabens auf dem laufenden Geschäftskonto als Reserve sperren. Die Gesellschaft erhält hierzu eine Mitteilung mit Betrag und Wirksamkeitszeitpunkt. Das übrige Konto bleibt nutzbar, soweit keine weitere Maßnahme mitgeteilt wird.",
            "Die Reserve bleibt Guthaben der Gesellschaft und ist für tatsächlich entstehende Rückbelastungen verpfändet. Die Bank erwirbt das Guthaben nicht allein durch die Sperre. Eine entstandene Rückbelastung wird gesondert gebucht und erläutert. Ohne eine solche Buchung wird die Reserve nicht mit einer bereits bestehenden Forderung verrechnet.",
            "Die Freigabe richtet sich nach dem Ende des jeweiligen Rückbelastungsrisikos. Ein verbindlicher kurzfristiger Freigabetermin wird nicht zugesagt. Der angezeigte Kontostand kann deshalb höher sein als der Betrag, über den die Gesellschaft verfügen darf. Neue Zahlungseingänge erhöhen grundsätzlich das verfügbare Guthaben, solange keine ergänzende Sperrmitteilung vorliegt." ], "Ilka Radtke, Zahlungsverkehr")
        add("INV-11", "07_Vermoegen", "pdf", "2026-04-30", "Rotorwert Fluggerätehandel GmbH", "Ankaufspreise U-01 und U-02 – technischer Vorbehalt", [
            "Für die beiden eigenen Maschinen U-01 und U-02 werden nach Prüfung der vorgelegten Unterlagen Bruttoverwertungserlöse von zusammen 565.000 EUR erwartet. Für die notwendige Dokumentenprüfung, Positionierungsflüge, Übergabeinspektion und Vermittlung kalkulieren wir 40.000 EUR. Nach diesen Kosten verbleiben 525.000 EUR.",
            "Der Ansatz setzt vollständige Logbücher und die Bestätigung des technischen Zustands voraus. Die erfolgte Triebwerksüberholung U-02 ist berücksichtigt. Ein fehlendes Logbuch oder eine abweichende Restlaufzeit kann den Preis erheblich verändern. Ein sofortiger Notverkauf ist nicht vereinbart.",
            "Die vier Maschinen U-03 bis U-06 stehen nach den vorgelegten Leasingunterlagen im Eigentum der Leasinggeberin und sind nicht Bestandteil unseres Angebots. Eine Halterstellung oder das Abstellen auf Ihrem Gelände ändert den Gegenstand dieser Anfrage nicht.",
            "Der Bank muss eine Sicherheitenfreigabe vorgelegt werden. Kaufpreiszahlung erfolgt erst nach technischer Prüfung, Kaufvertrag und Übergabe. Wir sagen keinen Zahlungseingang in den nächsten drei Wochen zu." ], "Fenja Ahrens, Fluggerätebewertung")
        add("LEASE-03", "06_Finanzierung", "pdf", "2026-04-30", "Fluggeräte Pool Ost GmbH", "Raten im Mai und Rückgabeabrechnung der vier Leasingmaschinen", [
            "Die zusammengefassten Mai-Raten für U-03 bis U-06 betragen nach dem Vertragsnachtrag 48.000 EUR und sind am 26. Mai fällig. Sie betreffen die Nutzung im Mai. Die Forderung bleibt von einer späteren Rückgabe unberührt. Eine Stundung über den 26. Mai ist nicht vereinbart.",
            "Bei sofortiger Rückgabe zum Ende Mai beträgt die Abgeltung der Restlaufzeit ab Juni 220.000 EUR. Dieser Betrag enthält die Mai-Raten nicht. Er ersetzt die weiteren Raten ab Juni bei vertragsgemäßer Rückgabe der vier Maschinen im dokumentierten Zustand. Eine Doppelberechnung derselben Restlaufzeit ist nicht vorgesehen.",
            "Die Maschinen verbleiben in unserem Eigentum. Eigene Ersatzteile oder Geräte der Uckerbogen werden nur übernommen, wenn sie gesondert vereinbart sind. Die Rückgabeabrechnung betrifft nicht das Bankdarlehen für U-01 und U-02. Ein verbindlicher Übernehmer für die laufenden Verträge liegt uns nicht vor." ], "Eike Mahn, Vertragsverwaltung")
        add("VCH-02", "07_Vermoegen", "docx", "2026-04-30", case["company"], "Gutscheinliste – noch nicht durchgeführte Flüge", [
            "1 Bestandsaufnahme", "Die Disposition hat die verkauften und noch nicht eingelösten eigenen Gutscheine mit dem Bestelljournal abgeglichen. Der zurückzuzahlende Betrag bei vollständiger Aufgabe beträgt 68.000 EUR. Bereits durchgeführte Flüge sind aus dieser Liste entfernt. Die Beträge wurden in früheren Monaten vereinnahmt und werden nicht nochmals als neue Eingänge geplant.",
            "2 Zahlungsweg", "Die hier erfassten Gutscheine wurden durch Banküberweisung bezahlt. Sie betreffen nicht die Kartenumsätze, für die eine Rückbelastungsreserve mit der Bank vereinbart wurde. Eine mögliche Erstattung dieser Gutscheine ist deshalb getrennt von einer etwaigen Belastung aus dem Kartenprogramm zu verfolgen.",
            "3 Ausführung und Erstattung", "Bei Fortführung können die Flüge nach Maßgabe der betrieblichen Verfügbarkeit noch erbracht werden. Eine sofortige Auszahlung an alle Kunden ist nicht verlangt. Bei endgültiger Aufgabe muss die Abwicklung mit jedem Vertrag abgeglichen werden. Die Buchhaltung soll den Bestand nicht mit den separat bestellten elf Transfers des Reiseveranstalters vermischen.",
            "Die Liste wurde von Malin Stange und Disponent Oskar Vehren abgestimmt. Anfragen zu Terminwechseln liegen im Kundenpostfach. Die Vereinbarung einer Erstattung und die tatsächliche Überweisung sind jeweils mit eigener Vorgangsnummer zu dokumentieren." ])
        add("HANG-03", "05_Betrieb", "eml", "2026-05-27", "Uckerbogen Technik", "Hallentorantrieb – Zusatzauftrag nicht abgenommen", [
            "Die Vermieterin hat uns den Nachtrag über 47.000 EUR für den Torantrieb geschickt. Die automatisch eingetragene Fälligkeit ist der 4. Juni. Ich habe die Zusatzleistung nicht abgenommen: Das Tor stoppt zweimal pro Öffnung und der vereinbarte Notbetrieb wurde noch nicht vorgeführt.",
            "Die Vermieterin meint, die Zustimmung zum Einbau reiche aus. Unser Auftrag betrifft aber die betriebsfähige Anlage einschließlich Sicherheitsprüfung. Die Unterlagen zum Hauptmietvertrag liegen in der Ablage. Der offene Zusatzposten ist nicht Teil der normalen Hangarmiete über 12.500 EUR.",
            "Bitte keine automatische Zahlungsfreigabe setzen. Wir verlangen zuerst das Prüfprotokoll und die Mangelbeseitigung. Ich kann nicht bestätigen, ob jemand aus der Geschäftsführung später eine andere Vereinbarung getroffen hat. In meinem Postfach liegt dazu nichts." ], "Oskar Vehren, Technik")
        add("NR-02", "06_Finanzierung", "pdf", "2026-04-30", "Wolkenhain Beteiligungs KG", "Abstimmung Gesellschafterdarlehen 155.000 EUR", [
            "Der noch offene Rückzahlungsanspruch aus dem Gesellschafterdarlehen beträgt 155.000 EUR. Das Darlehen ist von der befristeten Ausstattungszusage getrennt. Die Ausstattungszusage enthält weder einen Erlass des Darlehens noch eine Änderung seines Rangs.",
            "Die Rückzahlung ist nach dem Vertragsplan erst nach dem hier betrachteten Sommergeschäft vorgesehen. Eine vorgezogene Fälligstellung wurde nicht ausgesprochen. Ein qualifizierter Rangrücktritt oder eine Durchsetzungssperre ist zwischen den Parteien nicht unterzeichnet.",
            "Bitte führen Sie die Forderung weiterhin im Darlehenskonto. Der am 28. April besprochene Entwurf betraf nur die Verlängerung der Unterstützung und nicht den Darlehensvertrag. Wir haben keine Erklärung abgegeben, dass das Darlehen nur aus freiem Vermögen bedient werden dürfte." ], "Lea Kranz")

    # Gleiche Büroaufgabe, aber mit konkreten fallbezogenen Fundorten und Lücken.
    search_items = {
        "CB": ["Geräteausdruck zur KX-Messreihe", "Original des Außenlager-Mietvertrags", "Kopie der Sicherheitenliste OF-109", "Gegenprobe zur Toncharge T-629"],
        "BZ": ["vollständige Bewilligung des Hofwegerechts", "Originalfreigabe der Fensterbandänderungen", "Anlagen zum Hallendarlehen", "Fotos der beiden Nachbesserungsvorgänge"],
        "PR": ["Logbuchkopien U-01 und U-02", "Eingangsprotokoll des Holdingpostfachs", "Prüfprotokoll des Hallentorantriebs", "vollständige Gutschein-Bestellbelege"],
    }[p]
    add("UEB-01", "08_Uebergabe", "docx", "2026-07-08", case["company"], "Übergebenes Material und noch gesuchte Unterlagen", [
        "1 Ablage und Ansprechpartner", f"{b['contact']} hat die Bank-PDFs, den Export der Buchungen und die Ordner für Rechnungen und Korrespondenz zusammengestellt. Die Daten stammen aus dem laufenden Geschäftskonto. Die lokale Ablage enthält teils einen E-Mail-Anhang und daneben denselben Beleg als einzeln gespeicherte Datei. Gleiche Belegnummer und gleicher Betrag bezeichnen dann dieselbe Forderung.",
        "2 Noch offene Suche", "Gesucht werden " + ", ".join(search_items) + ". Die genannten Unterlagen sind in der Übergabe bisher nicht vollständig enthalten. Die jeweiligen Ansprechpartner sind angefragt. Das Fehlen einer Datei bedeutet nicht, dass ein Vertrag nicht geschlossen wurde; ältere Vorgänge können im Papierarchiv liegen.",
        "3 Buchungsstand", "Der Export enthält Buchungsdatum und Wertstellung. Bei den übergebenen Einträgen stimmen beide Tage überein. Die Sachbearbeitung hat Zahlungserwartungen und tatsächliche Eingänge nicht in einer gemeinsamen Spalte zusammengeführt. Ein im Debitorenstamm eingetragenes Datum ist deshalb anhand der Kundenbestätigung und des Kontos zu prüfen.",
        "4 Rückfragen", "Bitte nennen Sie bei jeder Rückfrage den Beleg und den benötigten Zeitraum. Die Geschäftsführung kann nicht zuverlässig aus der Erinnerung sagen, wann jede Nachricht gelesen wurde. Für den Inhalt der damaligen Planung sind die gespeicherten Dateien und Nachrichten heranzuziehen. Eine rechtliche Bewertung der Zahlungsunterlagen ist mit der Übergabe nicht erstellt." ])
    return out


def build_supplements(case, directory, letter_pdf, csv_file):
    """Gibt sämtliche neuen Einzelquellen für die Grundakten-Auswahl zurück."""
    prefix = case["prefix"]
    profile = BUSINESS[prefix]
    sources = []
    invoice_dir = directory / "04_Originalbelege"
    invoice_dir.mkdir(parents=True, exist_ok=True)
    lookup = {r["id"]: r for r in case["obligations"]}
    deb = {r["id"]: r for r in case["receivables"]}
    for reference in profile["invoice_ids"]:
        path = invoice_dir / f"{reference}_Rechnung.pdf"
        invoice(path, case, lookup[reference])
        sources.append(path)
    for i, reference in enumerate(profile["customer_ids"]):
        entry = deb[reference]
        path = invoice_dir / f"{reference}_Ausgangsrechnung.pdf"
        invoice(path, case, entry, outgoing=True)
        sources.append(path)
        accepted = invoice_dir / f"{reference}_Leistungsfreigabe.pdf"
        item = {"id": reference + "-ABN", "date": entry["confirmed_on"], "type": "accounting",
                "issuer": entry["debtor"], "subject": profile["topics"][i] + " – Freigabe zur Abrechnung",
                "recipient": case["company"], "signature": "Projektabrechnung",
                "body": [f"Wir bestätigen den für die Abrechnung freigegebenen Leistungsumfang des Vorgangs {reference}. "
                         f"Die vereinbarte Teil- beziehungsweise Restzahlung beträgt {money(entry['amount_cents'])}. "
                         f"Die Anweisung ist für den {date_de(entry['available_on'])} vorgesehen. Die Freigabe betrifft ausschließlich den bezeichneten Vorgang.",
                         "Die fachliche Abnahme bzw. die nach dem Vertrag erforderliche Freigabe ist im Projektkonto erfasst. Nicht beauftragte Nachträge, zusätzliche Kontingente und weitere Leistungsabschnitte sind von dieser Bestätigung nicht umfasst. Bitte rechnen Sie sie nicht unter derselben Referenz mit ab.",
                         "Ein Anspruch auf eine zusätzliche Vorauszahlung wird damit nicht zugesagt. Falls Ihre Rechnung einen anderen Betrag enthält, bitten wir vor Anweisung um Abstimmung. Für den Nachweis des tatsächlichen Zahlungseingangs ist der Kontoauszug maßgeblich."]}
        letter_pdf(accepted, case, item)
        sources.append(accepted)
    entries = supplemental_documents(case)
    for item in entries:
        folder = directory / item["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / f"{item['id']}.{item['kind']}"
        if item["kind"] == "docx":
            office_document(target, case, item)
        elif item["kind"] == "eml":
            attachment_paths = [directory / value for value in item.get("attachments", [])]
            email_with_attachments(target, case, item, attachment_paths)
        else:
            letter_pdf(target, case, item)
        sources.append(target)
    # Echte MIME-Belege plus allein öffnungsfähige Einzeldateien für die Demonstration.
    mail_item = {"id": prefix + "-MAIL-RECH", "date": deb[profile["customer_ids"][0]]["confirmed_on"],
                 "issuer": profile["contact"], "subject": "Freigegebene Rechnung und Leistungsblatt zum Projektkonto",
                 "body": ["Anbei die Rechnung und die Kundenfreigabe zum bezeichneten Projektkonto. Bitte beide Dateien gemeinsam zum Vorgang ablegen. Die Freigabe ist bereits im Nebenbuch verknüpft.",
                          "Der dort genannte Zahlungstermin ist ein angekündigter Termin. Bitte den Kontoabgleich erst nach dem tatsächlichen Eingang abschließen. Die Dateikopien in meinem Versandordner begründen keine weiteren Forderungen."],
                 "signature": profile["contact"] + ", " + profile["dept"]}
    mail_path = directory / "08_Uebergabe" / f"{prefix}-MAIL-RECH.eml"
    first = profile["customer_ids"][0]
    email_with_attachments(mail_path, case, mail_item, [invoice_dir / f"{first}_Ausgangsrechnung.pdf", invoice_dir / f"{first}_Leistungsfreigabe.pdf"])
    sources.append(mail_path)
    # Native Rohdaten: Links zum Beleg, kein rechtlicher Ergebnisstatus.
    csv_path = directory / "08_Uebergabe" / f"{prefix}-Belegablage_Export.csv"
    rows = []
    for ref in profile["invoice_ids"]:
        r = lookup[ref]
        rows.append({"Beleg": ref, "Gegenpartei": r["creditor"], "Rechnungsdatum": r["arose_on"],
                     "Rechnungsbetrag_Cent": r["amount_cents"], "Faelligkeit_Stammdaten": r["due_on"],
                     "Zahlungsbuchung": r.get("payment_id") or "", "Datei": f"04_Originalbelege/{ref}_Rechnung.pdf"})
    for ref in profile["customer_ids"]:
        r = deb[ref]
        rows.append({"Beleg": ref, "Gegenpartei": r["debtor"], "Rechnungsdatum": r["confirmed_on"],
                     "Rechnungsbetrag_Cent": r["amount_cents"], "Faelligkeit_Stammdaten": r["available_on"],
                     "Zahlungsbuchung": r.get("payment_id") or "", "Datei": f"04_Originalbelege/{ref}_Ausgangsrechnung.pdf"})
    csv_file(csv_path, tuple(rows[0]), rows)
    sources.append(csv_path)
    # Payroll is a genuine split of the existing aggregate debit, not new expense.
    payroll = next(r for r in case["obligations"] if r["id"] == prefix + "-LOHN-01")
    staff = case["staff"]
    weights = [68 + ((i * 13) % 49) for i in range(staff)]
    amounts = [payroll["amount_cents"] * w // sum(weights) for w in weights]
    for i in range(payroll["amount_cents"] - sum(amounts)):
        amounts[i % staff] += 1
    payroll_rows = [{"Personalnummer": f"{prefix}-{i+1:03d}", "Abrechnungsmonat": "2026-05",
                     "Nettoauszahlung_Cent": amount, "Sammelbuchung": payroll["payment_id"],
                     "Ausfuehrungstag": payroll["paid_on"]} for i, amount in enumerate(amounts)]
    payroll_path = directory / "02_Buchhaltung" / f"06_{prefix}_Lohnzahlstapel_Mai.csv"
    csv_file(payroll_path, tuple(payroll_rows[0]), payroll_rows)
    sources.append(payroll_path)
    payroll_letter = directory / "02_Buchhaltung" / f"07_{prefix}_Lohnlauf_Begleitzettel.pdf"
    letter_pdf(payroll_letter, case, {"id": prefix + "-LOHNLAUF-01", "date": payroll["paid_on"], "type": "accounting",
                "issuer": payroll["creditor"], "subject": "Lohnlauf Mai – Sammelausführung und Einzelpositionen",
                "recipient": case["company"], "signature": "Abrechnungsteam Lohn",
                "body": [f"Die anliegende Datei enthält {staff} Nettoauszahlungen für den Monat Mai. Teilzeit, unterschiedliche Eintrittszeiten und individuelle Abzüge sind bereits in der Lohnabrechnung berücksichtigt. Die Summe der Einzelpositionen beträgt {money(payroll['amount_cents'])}.",
                         f"Der Zahlungsdienst hat die Einzelpositionen unter der Referenz {payroll['payment_id']} ausgeführt. Der Bankauszug der Gesellschaft zeigt nur diese Sammelbelastung. Die CSV-Einzelpositionen sind keine zusätzlichen Ausgaben neben der Sammelbuchung.",
                         "Die Datei enthält ausschließlich den Nettozahlstapel. Arbeitgeber- und Arbeitnehmerbeiträge zur Sozialversicherung werden in gesonderten Beitragsnachweisen geführt. Die Übermittlung eines Beitragsnachweises ist kein Beleg für den tatsächlichen Zahlungseingang bei der Einzugsstelle.",
                         "Die Personalnummern dienen dem Abgleich mit der Lohnbuchhaltung. Die vollständigen personenbezogenen Abrechnungsblätter werden gesondert verwahrt. Für Rückfragen nennen Sie bitte Personalnummer, Monat und Sammelreferenz."]})
    sources.append(payroll_letter)
    transfer = directory / "02_Buchhaltung" / f"08_{prefix}_Zahlungsausgang_ERP.xml"
    root = Element("ZahlungsausgangExport", {"format": "Interner ERP-Export", "version": "1", "unternehmen": case["company"], "erstellt": "2026-07-07"})
    SubElement(root, "Hinweis").text = "Anwendungsinterner Datenexport; keine Bankeinreichungsdatei. Offene Aufträge begründen keine weitere Forderung neben dem genannten Beleg."
    for entry in case["obligations"]:
        if entry["id"] in profile["invoice_ids"] or (entry["id"].startswith(prefix + "-") and "2026-05" in entry["due_on"] and "-K" not in entry["id"]):
            item = SubElement(root, "Vorgang", {"beleg": entry["id"]})
            for tag, value in (("Empfaenger", entry["creditor"]), ("BetragCent", entry["amount_cents"]),
                               ("FaelligkeitLautStamm", entry["due_on"]), ("Ausfuehrung", entry.get("paid_on") or ""),
                               ("Bankreferenz", entry.get("payment_id") or ""),
                               ("Status", "ausgefuehrt" if entry.get("paid_on") else "offen")):
                SubElement(item, tag).text = str(value)
    indent(root, space="  ")
    ElementTree(root).write(transfer, encoding="utf-8", xml_declaration=True)
    sources.append(transfer)
    # Contemporaneous debtor statements deliberately postdate the first tested §17 date.
    difficulty = {
        "CB": ("2026-05-13", "Lausitz Industriegas GmbH", "CB-GAS-01", "122.000 EUR", "05.06.2026", "Die erwartete Serienbestellung ist weggefallen und die Bank hat die Zwischenlinie nicht verlängert. Den ausstehenden Prototypenbetrag können wir derzeit nicht abrufen."),
        "BZ": ("2026-04-22", "Südspange Stahlhandel GmbH", "BZ-STA-01", "128.000 EUR", "15.05.2026", "Die freigegebene Schlussrate reicht für die Rechnung nicht aus. Der zusätzliche Materialabschlag ist abgelehnt. Die Löhne und die laufenden Montagekosten können wir nicht beliebig verschieben."),
        "PR": ("2026-05-19", "Rotorservice Havel GmbH", "PR-ROTOR-01", "116.000 EUR", "12.06.2026", "Der Reiseveranstalter hat das Sommerkontingent abgesagt. Die Unterstützung der Holding ist nicht verlängert worden. Ein Teil des angezeigten Guthabens ist für das Kartenprogramm gesperrt."),
    }[prefix]
    when, creditor, ref, amount, until, reason = difficulty
    notice = {"id": prefix + "-ZAHL-MAIL-01", "date": when, "issuer": case["manager"], "recipient": creditor,
              "subject": "Ihre offene Rechnung " + ref + " – Bitte um Gespräch",
              "body": [f"Ihre Rechnung über {amount} ist uns bekannt. Wir können den Betrag aus den verfügbaren Mitteln weder heute noch bis zum {until} vollständig begleichen. Auch einen verlässlichen Ratenplan können wir für diesen Zeitraum im Moment nicht zusagen. Bitte lassen Sie uns dennoch über die weitere Zusammenarbeit sprechen.",
                       reason,
                       "Wir arbeiten weiter und wollen die Lage ordnen. Bitte verstehen Sie das nicht als verbindliche Ankündigung eines Zahlungstermins. Sobald ein bestimmter Eingang feststeht, melden wir uns. Eine Vereinbarung über einen neuen Zahlungstermin ist bisher nicht geschlossen."], "signature": case["manager"]}
    notice_path = directory / "05_Betrieb" / f"{prefix}-ZAHL-MAIL-01.eml"
    email_with_attachments(notice_path, case, notice, [])
    sources.append(notice_path)
    return sources
