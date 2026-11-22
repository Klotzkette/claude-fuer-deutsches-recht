"""Erzeugt die vier Verhandlungsunterlagen vom 13. bis 16. April 2026."""
import argparse
from datetime import datetime
from email import policy
from email.message import EmailMessage
from io import BytesIO
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


CASE = Path(__file__).resolve().parents[3] / 'testakten/neuralis-medtech-erlangen-gestaltungsakte/02_Gestaltungsvorschlaege'
G06 = 'G06_Satzungsfassung_Weisungen_und_Freigaben.docx'
G07 = 'G07_Stimmbindung_Fonds_und_Seidl.docx'
G08 = 'G08_Konditionen_Teilanteil_und_Finanzierung.docx'
G09 = 'G09_Rueckfragen_von_Dr_Seidl.eml'


def new_document(day, author, firm, reference, title, subtitle, color):
    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(2.65), Cm(2.1)
    section.left_margin, section.right_margin = Cm(2.55), Cm(2.4)
    section.header_distance, section.footer_distance = Cm(1.1), Cm(1)
    for style_name, size in [('Normal', 11), ('Title', 21), ('Heading 1', 14), ('Heading 2', 11)]:
        style = doc.styles[style_name]
        style.font.name, style.font.size = 'Times New Roman', Pt(size)
        style.font.color.rgb = RGBColor.from_string('232427' if style_name == 'Normal' else color)
        style.font.bold = style_name != 'Normal'
        fonts = style.element.get_or_add_rPr().rFonts
        for attr in ('asciiTheme', 'hAnsiTheme', 'eastAsiaTheme', 'cstheme'):
            fonts.attrib.pop(qn('w:' + attr), None)
        style.paragraph_format.space_before = Pt(7 if style_name.startswith('Heading') else 0)
        style.paragraph_format.space_after = Pt(6)
    doc.styles['Normal'].paragraph_format.line_spacing = 1.13
    head = section.header.paragraphs[0]
    head.alignment = WD_ALIGN_PARAGRAPH.RIGHT if day == 14 else WD_ALIGN_PARAGRAPH.LEFT
    run = head.add_run(firm)
    run.font.bold, run.font.size, run.font.color.rgb = True, Pt(12), RGBColor.from_string(color)
    border = OxmlElement('w:pBdr')
    rule = OxmlElement('w:bottom')
    for key, value in [('val', 'single'), ('sz', '8'), ('space', '5'), ('color', color)]:
        rule.set(qn('w:' + key), value)
    border.append(rule)
    head._p.get_or_add_pPr().append(border)
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    footer.add_run(f'{reference}   ·   Entwurf vom {day}. April 2026   ·   Seite ').font.size = Pt(9)
    page = OxmlElement('w:fldSimple')
    page.set(qn('w:instr'), 'PAGE')
    footer._p.append(page)
    date = datetime(2026, 4, day, 8)
    props = doc.core_properties
    props.author, props.title, props.subject = author, title, subtitle
    props.created, props.modified, props.last_modified_by = date, date, author
    doc.add_paragraph(f'{reference}   /   {day}. April 2026').runs[0].italic = True
    doc.add_heading(title, level=0)
    paragraph = doc.add_paragraph(subtitle)
    paragraph.runs[0].bold = True
    return doc


def clause(doc, title, *bodies):
    doc.add_heading(title, level=2)
    for body in bodies:
        doc.add_paragraph(body)


def save(doc, dest):
    # Auch die Zeitstempel der ZIP-Einträge stammen aus dem Aktenstück.
    data = BytesIO()
    doc.save(data)
    stamp = doc.core_properties.created.timetuple()[:6]
    with ZipFile(data) as source, ZipFile(dest, 'w') as target:
        for entry in source.infolist():
            content = source.read(entry)
            info = ZipInfo(entry.filename, stamp)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            target.writestr(info, content)


def articles(out):
    doc = new_document(13, 'Dr. Fabian Rehbogen', 'KANZLEI REHBOGEN UND KOLLEGEN', 'Vogt · G 41/26',
                       'Weisungen, Freigaben und persönliche Zustimmung',
                       'Verhandlungsentwurf für Dr. Henrik Vogt · Alternative ohne Anteilsverkauf', '234E60')
    doc.add_paragraph('Herrn Dr. Vogt zur Weitergabe an den Gesellschafterkreis. Die folgenden Änderungen beziehen sich auf den am 26. Februar bescheinigten Satzungswortlaut. Der Vorschlag belässt die Geschäftsanteile bei 51.000, 32.000 und 17.000 Euro. Der Fonds und Frau Dr. Seidl haben dem Wortlaut bisher nicht zugestimmt.')
    doc.add_heading('1  Persönliches Mitgliedschaftsrecht', level=1)
    clause(doc, '1.1  Ziffer 6.5 wird vollständig ersetzt',
           '„6.5.1 Solange Dr. Henrik Vogt Gesellschafter und Geschäftsführer ist, bedarf jeder Gesellschafterbeschluss zusätzlich zu der gesetzlichen oder satzungsmäßigen Mehrheit seiner ausdrücklichen Zustimmung, soweit ihm bei dem Gegenstand ein Stimmrecht zusteht. Das Recht steht ihm persönlich zu. Es erfasst sämtliche Geschäftsbereiche, jede Einzel- und Rahmenweisung, die Einführung, Änderung und Aufhebung von Berichtspflichten, Freigaben und Geschäftsordnungen sowie die Verteilung der Geschäftsführungsaufgaben. Es gilt auch für die ordentliche Abberufung, die Entziehung übertragener Befugnisse und die Änderung oder Aufhebung dieses Rechts selbst.',
           '6.5.2 Seine ausdrücklich abgegebene Ja-Stimme gilt als Zustimmung. Eine gesonderte Zustimmung hat er vor Feststellung des Beschlussergebnisses persönlich oder durch einen für den konkreten Gegenstand in Textform ausdrücklich Bevollmächtigten zu erklären. Die Erklärung wird mit dem Beschluss protokolliert. Schweigen, Abwesenheit und Stimmenthaltung gelten nicht als Zustimmung. Für die erneute Versammlung nach Ziffer 5.3 und den Umlauf nach Ziffer 5.5 gilt dasselbe. Das Einverständnis mit dem Umlaufverfahren enthält noch keine Zustimmung zur Sache.',
           '6.5.3 Zwingende gesetzliche Stimmverbote bleiben unberührt. Bei einem Stimmverbot nach Ziffer 6.3 oder 10.3 ist für diesen Beschluss keine persönliche Zustimmung erforderlich. Ein bloßer Widerspruch gegen eine vorgeschlagene Weisung begründet für sich weder einen wichtigen Grund zur Abberufung noch einen Einziehungsgrund.“')
    doc.add_page_break()
    doc.add_heading('2  Zuständigkeit für die laufende Geschäftsführung', level=1)
    clause(doc, '2.1  Neuer Eingangssatz zu Ziffer 4.5',
           '„Die Geschäftsführung darf die unter Ziffern 4.5.1 bis 4.5.4 und 7.3 genannten Maßnahmen nur mit vorheriger Zustimmung der Gesellschafterversammlung vornehmen. Treffen mehrere Zustimmungstatbestände zusammen, genügt ein Beschluss, der alle betroffenen Maßnahmen bezeichnet und sämtliche jeweiligen Mehrheits- und Zustimmungserfordernisse erfüllt.“')
    clause(doc, '2.2  Neue Fassung der Ziffer 7.3',
           '„Bei Investitionen und Anschaffungen über 50.000 Euro im Einzelfall, bei der Einstellung, Beförderung oder Kündigung von Mitarbeitern ab der Vergütungsgruppe Leitung sowie bei klinischen Studienverträgen mit einem Volumen über 100.000 Euro holt die Geschäftsführung die vorherige Zustimmung der Gesellschafterversammlung ein. Der Beirat kann vor der Beschlussfassung Stellung nehmen. Eine fehlende oder ablehnende Stellungnahme hindert die Beschlussfassung nicht. Weisungen an die Geschäftsführung und verbindliche Freigaben sind der Gesellschafterversammlung vorbehalten. Weder Geschäftsordnung noch Einzelbeschluss können sie auf den Beirat, einen Ausschuss, einzelne Mitglieder oder Dritte übertragen.“')
    clause(doc, '2.3  Ergänzung zu Ziffer 5 für den Fall ausbleibender Zustimmung',
           '„5.6 Kommt wegen fehlender Zustimmung ein Beschluss nicht zustande, übermittelt die Geschäftsführung allen Gesellschaftern binnen zwei Arbeitstagen den Antrag, die ausstehende Entscheidung und die Folgen der Verzögerung. Sie bietet binnen zehn Arbeitstagen eine moderierte Besprechung an. Eine erneute Beschlussfassung richtet sich nach den Ziffern 5 und 6. Der Moderator entscheidet nicht. Bei Gefahr im Verzug wahrt die Geschäftsführung unverzüglich ihre zwingenden gesetzlichen Pflichten und unterrichtet alle Gesellschafter über Anlass, Umfang und Dauer der Maßnahme. Eine bloße Angebotsfrist berechtigt nicht zur Ersetzung der Zustimmung.“')
    doc.add_paragraph('Zur Besprechung mit Frau Dr. Seidl und dem Fonds: Für einen bereits wirksamen Beschluss wie die Einkaufsregel vom 19. März wäre eigens zu entscheiden, ob er aufgehoben oder geändert werden soll. Für die Verweise in Ziffern 1.2 und 5.2 des Anstellungsvertrags bitten wir um einen separaten Vorschlag der Gesellschaft. Zu klären bleibt, wer sie dabei vertritt. Dieses Papier erteilt keinen Vollzugsauftrag.')
    save(doc, out / G06)


def pooling(out):
    doc = new_document(14, 'Dr. Nora Feldt', 'Feldt | Kammerer  ·  Gesellschaftsrecht', 'FHV 18/26',
                       'Vereinbarung über die Vorbereitung gemeinsamer Stimmen',
                       'Gegenentwurf der Fondsseite für FrankenHealth Ventures GmbH, Dr. Miriam Seidl und Dr. Henrik Vogt', '704437')
    doc.add_paragraph('Für die nächste Finanzierung möchte der Fonds seine Beteiligungsquote halten. Zur Beratung mit Frau Dr. Seidl und Herrn Dr. Vogt schlagen wir vor, die folgende Vereinbarung zunächst für einen begrenzten Zeitraum zu erproben. Das Papier ist ununterzeichnet. Jeder Beteiligte entscheidet nach Prüfung, ob er einen Vertrag schließen möchte.')
    clause(doc, '1  Gegenstand und Beteiligte',
           'Die FrankenHealth Ventures GmbH, Dr. Miriam Seidl und Dr. Henrik Vogt stimmen sich vor Entscheidungen der Neuralis MedTech GmbH über externe Beratungsleistungen ab 18.000 Euro netto je Auftrag, monatliche Einkaufsberichte und Änderungen des Ressorts Entwicklung untereinander ab. Der Vertrag bindet die drei Gesellschafter persönlich. Die Gesellschaft und die Mitglieder des Beirats übernehmen dadurch keine Verpflichtungen. Für alle übrigen Beschlussgegenstände übt jeder Gesellschafter seine Stimme frei aus.')
    clause(doc, '2  Eingang einer Vorlage',
           'Wer einen solchen Gegenstand zur Abstimmung stellen will, sendet allen anderen in einer E-Mail den vollständigen Beschlusstext, den Nettobetrag, den Leistungsgegenstand sowie einen etwaigen Ablauf des Angebots. Bei einer wesentlichen Änderung beginnt die Beratungsfrist für die geänderte Fassung erneut. Jede Seite kann einen eigenen Text oder die Ablehnung des Antrags zur gemeinsamen Entscheidung stellen.')
    clause(doc, '3  Einigung und Abstimmung',
           'Nur wenn alle drei Beteiligten derselben Fassung ausdrücklich in Textform zustimmen, ist sie als gemeinsame Abstimmungslinie vereinbart. Die Parteien verpflichten sich, ihre Stimmen in der Versammlung oder im zulässigen Umlauf entsprechend abzugeben, soweit ihnen ein Stimmrecht zusteht. Die Korrespondenz der drei Parteien ersetzt weder die Einberufung noch die Beschlussfassung der Gesellschaft. Eine Vollmacht wird keinem Teilnehmer erteilt.')
    doc.add_page_break()
    clause(doc, '4  Meinungsverschiedenheiten und laufende Fristen',
           'Bis zum Ablauf des fünften Werktags nach Zugang der vollständigen Vorlage beim letzten Beteiligten wirken die Parteien auf eine Vertagung hin. Als Werktage gelten Montag bis Freitag mit Ausnahme gesetzlicher Feiertage in Erlangen. Geht die Nachricht nach 17 Uhr ein, zählt sie für die Frist als am nächsten Werktag zugegangen. Einigkeit können die Parteien bereits vor Fristablauf herstellen.',
           'Ohne vollständige Einigung darf nach Fristablauf jeder Beteiligte über den unveränderten Antrag nach eigenem Ermessen abstimmen. Läuft vorher eine externe Angebotsfrist ab, bitten die Beteiligten die Geschäftsführung unverzüglich darum, eine Verlängerung anzufragen. Eine kürzere interne Beratung setzt das ausdrückliche Einverständnis aller drei voraus. Die Stimmverbote und die Einberufungsfristen der Gesellschaft bleiben zu beachten.')
    clause(doc, '5  Abweichende Stimmabgabe',
           'Weicht ein Beteiligter schuldhaft von der vereinbarten Abstimmungslinie ab, hat er dies den übrigen unverzüglich mitzuteilen und ihnen den nachgewiesenen, hierdurch entstandenen Schaden nach den gesetzlichen Vorschriften zu ersetzen. Für die Stimmzählung und die Behandlung von Beschlussmängeln gelten das Gesetz und der Gesellschaftsvertrag. Dieser Vertrag räumt niemandem eine zusätzliche Stimme oder ein gesellschaftsvertragliches Zustimmungsrecht ein.')
    clause(doc, '6  Beginn und Ende',
           'Die Vereinbarung beginnt erst mit Unterzeichnung durch alle drei Beteiligten und endet mit Ablauf des 31. März 2027. Eine ordentliche Kündigung vor diesem Termin ist ausgeschlossen. Das Recht zur außerordentlichen Kündigung aus wichtigem Grund bleibt bestehen. Eine Kündigung ist gegenüber allen anderen Beteiligten in Textform zu erklären. Mit ihrem Wirksamwerden endet die gemeinsame Bindung für zukünftige Abstimmungen. Ansprüche aus vor diesem Zeitpunkt erfolgten Verstößen bleiben bestehen.')
    doc.add_paragraph('Verhandlungsfrage der Fondsseite: Kann Frau Dr. Seidl die fünftägige Beratungsfrist auch vertreten, wenn ein Übersetzungsbüro den angebotenen Termin für zwei Prüfzentren nur bis zum folgenden Arbeitstag reserviert?')
    save(doc, out / G07)


def financing(out):
    doc = new_document(15, 'Dr. Nora Feldt', 'FrankenHealth Ventures  /  Beteiligungsmanagement', 'FHV · Investitionsausschuss',
                       'Teilverkauf aus Geschäftsanteil Nr. 1',
                       'Konditionen zur Aussprache · Erstellt von Dr. Nora Feldt für die Verkäuferseite', '31574B')
    doc.add_paragraph('Der Ausschuss soll entscheiden können, ob die Verhandlung eines Verkaufs an Herrn Dr. Vogt wirtschaftlich in Betracht kommt. Berechnet ist ein Szenario. Die Bewertung der Studien, die Finanzierungsprüfung des Käufers und die interne Freigabe des Fonds stehen aus. Weder ein verbindliches Angebot noch eine Kreditzusage liegen vor.')
    doc.add_heading('1  Kalkulation für den Gesprächseinstieg', level=1)
    rows = [('Position', 'Rechenannahme'), ('Eigenkapitalwert der Neuralis MedTech GmbH', '2.000.000 €'),
            ('Stück aus Anteil Nr. 1 / 100.000 € Stammkapital', '18.000 € nominal / 18 %'),
            ('Angesetzter Kaufpreis für das Anteilsstück', '360.000 €'),
            ('Private Eigenmittel des Käufers', '120.000 €'),
            ('Vorgesehener privater Bankkredit des Käufers', '240.000 €')]
    table = doc.add_table(rows=0, cols=2)
    table.autofit = False
    table.columns[0].width, table.columns[1].width = Cm(10.6), Cm(5.2)
    for idx, row in enumerate(rows):
        cells = table.add_row().cells
        for col, value in enumerate(row):
            cell = cells[col]
            cell.width = table.columns[col].width
            p = cell.paragraphs[0]
            if col == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            r = p.add_run(value)
            r.bold = idx == 0 or idx == 3
            p.paragraph_format.space_before, p.paragraph_format.space_after = Pt(3), Pt(3)
            shade = OxmlElement('w:shd')
            shade.set(qn('w:fill'), '31574B' if idx == 0 else ('E5EEEA' if idx % 2 else 'F7F9F8'))
            cell._tc.get_or_add_tcPr().append(shade)
            if idx == 0:
                r.font.color.rgb = RGBColor.from_string('FFFFFF')
    clause(doc, '1.1  Empfänger des Kaufpreises',
           'Der gesamte Kaufpreis flösse der Verkäuferin zu. Der Gesellschaft fließt aus diesem Verkauf kein neues Kapital zu. Auf den angenommenen Eigenkapitalwert wird in dieser Rechnung weder ein Minderheitsabschlag noch ein Zuschlag für den Verlust der einfachen Mehrheit des Fonds angewendet. Beide Punkte sind mit dem Ausschuss zu verhandeln.')
    clause(doc, '1.2  Finanzierungsnachweis vor der Beurkundung',
           'Der Käufer soll dem Fonds einen Eigenmittelnachweis über 120.000 Euro und eine verbindliche Finanzierungsbestätigung über weitere 240.000 Euro vorlegen. Ein Zins- oder Tilgungsangebot liegt noch nicht vor. Gebühren und Transaktionskosten wären zusätzlich privat zu decken. Der Investitionskredit 771-4402 der Gesellschaft und Vogts ältere Bürgschaft bleiben gesondert. Für den Erwerb sind weder Sicherheiten noch ein Schuldbeitritt der Neuralis vorgesehen.')
    doc.add_page_break()
    doc.add_heading('2  Vorschlag für die notarielle Kauf- und Abtretungsfassung', level=1)
    doc.add_paragraph('Die folgenden Klauseln beschreiben den Inhalt einer erst auszuhandelnden Urkunde. Die Nummern der neuen Geschäftsanteile wären vor einer Beurkundung anhand der letzten aufgenommenen Liste festzulegen.')
    clause(doc, '2.1  Teilung, Kaufgegenstand und Rechte',
           'Die Parteien sehen die Teilung des Geschäftsanteils Nr. 1 in einen Geschäftsanteil zu 33.000 Euro und einen Geschäftsanteil zu 18.000 Euro vor. Nur der Geschäftsanteil zu 18.000 Euro soll Gegenstand des Verkaufs und der Abtretung sein. Der bisherige Anteil des Käufers zu 32.000 Euro besteht daneben fort. Die Verkäuferin übernimmt die Gewähr, dass der Kaufgegenstand bei Übergang voll eingezahlt und frei von Rechten Dritter ist. Der Käufer erteilt weder der Verkäuferin noch der finanzierenden Bank eine Stimmrechtsvollmacht.')
    clause(doc, '2.2  Fälligkeit und Zahlung',
           'Der Kaufpreis von 360.000 Euro ist zehn Bankarbeitstage nach Zugang einer Fälligkeitsmitteilung des beurkundenden Notars beim Käufer zur Zahlung an die Verkäuferin fällig. Voraussetzung der Mitteilung sind der Nachweis der wirksamen Teilung, die vorherige Zustimmung nach Ziffer 9.1 des Gesellschaftsvertrags und die Klärung etwaiger Vorkaufsrechte. Beruft sich ein Beteiligter auf ein solches Recht, ist die Mitteilung bis zum Nachweis seines Erlöschens oder seiner Nichtausübung zurückzustellen. Der Fonds wünscht vor einer Bindung geklärt zu sehen, ob Ziffer 9.2 den Verkauf an einen bereits beteiligten Gesellschafter erfasst und ob Nebenvereinbarungen bestehen.')
    clause(doc, '2.3  Aufschiebende Bedingung und Gesellschafterliste',
           'Die dingliche Abtretung soll erst mit der vollständigen Gutschrift des Kaufpreises auf dem Konto der Verkäuferin wirksam werden. Die Verkäuferin meldet den Geldeingang dem Notar und dem Käufer unverzüglich in Textform mit einem Bankbeleg. Die Mitteilung dient dem Nachweis. Nach Wirksamwerden reicht der mitwirkende Notar die aktualisierte Liste nach § 40 Abs. 2 GmbHG ein und übersendet der Gesellschaft eine Abschrift. Die Aufnahme in das Handelsregister ist für die Legitimation gegenüber der Gesellschaft nach § 16 GmbHG gesondert festzuhalten.')
    doc.add_paragraph('Zurück an den Ausschuss: Nach dem Erwerb stünden 33.000 Stimmen des Fonds und 17.000 Stimmen von Frau Dr. Seidl neben 50.000 Stimmen von Herrn Dr. Vogt. Der Verkauf allein ändert weder den Maßstab der abgegebenen Stimmen noch das Entsendungsrecht für zwei Beiratsmitglieder. Ob und in welcher Fassung Änderungen des Beirats zugleich Bedingung eines Abschlusses sein sollen, ist vor Freigabe der Verhandlung zu entscheiden.')
    save(doc, out / G08)


def seidl(out):
    mail = EmailMessage(policy=policy.SMTP)
    mail['From'] = 'Dr. Miriam Seidl <m.seidl@neuralis.example>'
    mail['To'] = 'Dr. Nora Feldt <n.feldt@feldt-kammerer.example>, Dr. Fabian Rehbogen <rehbogen@kanzlei-rehbogen.de>'
    mail['Cc'] = 'Caroline Benkert <c.benkert@neuralis.example>'
    mail['Date'] = 'Thu, 16 Apr 2026 09:12:00 +0200'
    mail['Subject'] = 'Vor dem Gesellschaftergespräch: Wer darf dem Übersetzungsbüro zusagen?'
    mail['Message-ID'] = '<20260416.0912.seidl.neuralis@neuralis.example>'
    mail.set_content("""Sehr geehrte Frau Dr. Feldt, sehr geehrter Herr Dr. Rehbogen,

am 19. März habe ich für den Monatsbericht und die Freigabeschwelle gestimmt. Mir fehlte der Überblick darüber, welche Beträge die einzelnen Prüfzentren bereits gebunden hatten. Ich wollte damit nicht erreichen, dass ausgerechnet die Bestellung der englischen Unterlagen über 21.600 Euro an einem nicht erreichbaren Gesellschafter hängenbleibt.

Bei Ihrem Satzungsentwurf, Herr Dr. Rehbogen, hätte ich gern einen Vorschlag für die Sommerferien: Könnte Henrik mir für eine bestimmte Sitzung und einen genau bezeichneten Übersetzungsauftrag Vollmacht geben, ohne mir damit auch seine Entscheidung über den Monatsbericht zu übertragen? Wer prüft die Vollmacht, bevor der Vorsitzende das Ergebnis feststellt? Ich möchte keinen Eintrag im Protokoll verantworten, der unsere beiden Abstimmungen zusammenzieht.

Beim Vertragsentwurf vom Dienstag ist mir ein anderer Punkt wichtig. Beim Einkauf können wir oft fünf Werktage warten, bei einer Rückfrage des Prüfzentrums am Vormittag gelegentlich nicht einmal bis zum nächsten Tag. Ich kann mir vorstellen, wiederkehrende Kleinaufträge in einem befristeten Rahmen vorab zu behandeln. Dafür brauche ich eine Betragsgrenze je Auftrag und ein Gesamtbudget. Mit wem würde ich so eine Regelung vereinbaren, und welche Freigabe wäre weiterhin innerhalb der Gesellschaft erforderlich?

Den Ansatz von 360.000 Euro für das Stück aus dem Fondsanteil habe ich verstanden. Wenn der Betrag an den Fonds geht, wie finanzieren wir dann den nächsten Studienabschnitt? Ich würde den Vorschlag erst mit unserer Liquiditätsplanung vergleichen, bevor wir über den Verlust der Fondsmehrheit sprechen. Bitte nehmen Sie meine Fragen auf die Gesprächsliste. Ich sage damit keinem der Texte zu.

Freundliche Grüße
Dr. Miriam Seidl
Gesellschafterin · Neuralis MedTech GmbH""")
    (out / G09).write_bytes(mail.as_bytes())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=CASE)
    out = parser.parse_args().output
    out.mkdir(parents=True, exist_ok=True)
    articles(out)
    pooling(out)
    financing(out)
    seidl(out)


if __name__ == '__main__':
    main()
