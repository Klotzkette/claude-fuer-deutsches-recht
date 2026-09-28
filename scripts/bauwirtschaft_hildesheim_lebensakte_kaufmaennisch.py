#!/usr/bin/env python3
"""Belegzugänge, Projektorganisation und kaufmännische Wordvorlagen. Autor: Klotzkette."""
from __future__ import annotations

from datetime import datetime
from email import policy
from email.headerregistry import Address
from email.message import EmailMessage
from email.utils import format_datetime
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import re
import subprocess
import sys
from zoneinfo import ZoneInfo

from bauwirtschaft_hildesheim_lebensakte_common import (
    ROOT, CASE, QUALITY, ACTORS, REF, euro, new_document, save_docx, normalize_docx,
)


def invoice_mails():
    data = json.loads((ROOT/'quality/hildesheim-achtfamilienhaus/finanzdaten.json').read_text())
    entries = {x['source']: CASE/x['target'] for x in json.loads((QUALITY/'basisdateien.json').read_text())}
    outputs = []
    for invoice in data['invoices']:
        xml_name = Path(invoice['filename']).stem + '_XRechnung.xml'
        if xml_name not in entries:
            continue
        sender = ACTORS[invoice['issuer']]
        recipient = ACTORS['buchhaltung']
        correction = invoice['gross'] < 0
        label = 'Rechnungskorrektur' if correction else 'Rechnung'
        amount_label = 'Erstattungsbetrag' if correction else 'mit diesem Beleg angeforderte Zahlbetrag'
        date = datetime.fromisoformat(invoice['date']+'T14:18:00').replace(tzinfo=ZoneInfo('Europe/Berlin'))
        message = EmailMessage(policy=policy.SMTP)
        message['From'] = Address(display_name=sender[3], addr_spec=sender[2])
        message['To'] = Address(display_name=recipient[3], addr_spec=recipient[2])
        message['Date'] = format_datetime(date)
        message['Subject'] = f'{REF} / {label} {invoice["id"]} / {invoice["label"]}'
        message['Message-ID'] = f'<sw-hi-belegzugang-{invoice["id"].lower()}@{sender[2].split("@")[1]}>'
        message['Return-Path'] = '<'+sender[2]+'>'
        message['Received'] = f'from mail.{sender[2].split("@")[1]} by eingang.steinbogen-wohnen.example with ESMTP; {format_datetime(date)}'
        message['Content-Language'] = 'de-DE'
        body = [
            'Sehr geehrte Frau Wagner,',
            f'für das Bauvorhaben Wohnhof Am Steinbogen übersenden wir Ihnen unsere {label} {invoice["id"]} vom {date:%d.%m.%Y}. Gegenstand ist {invoice["label"]}. Der abgerechnete Leistungszeitraum lautet {invoice["period"]}.',
            f'Der {amount_label} beträgt {euro(abs(invoice["gross"]))} EUR. Bitte führen Sie unsere Belegnummer im Verwendungszweck an, damit Ihre Zahlung beziehungsweise die Erstattung der richtigen Forderung zugeordnet werden kann.',
        ]
        if invoice.get('prior'):
            body.append('Die in der Schlussrechnung abgesetzten früheren Abschlagsrechnungen sind '+', '.join(invoice['prior'])+'. Die kumulierte Leistung und die bereits abgerechneten Abschläge sind getrennt ausgewiesen. Maßgeblich für diese Zahlungsanforderung ist der verbleibende Zahlbetrag.')
        if correction:
            body.append('Die Korrektur bezieht sich auf die vereinbarte Behandlung des Bodenbelags in Wohnung 07. Sie ersetzt keine andere Schlussrechnungsposition. Die ursprüngliche Schlussrechnung und die gesonderte Vereinbarung bleiben Bestandteil unserer Abrechnung.')
        body.extend([
            'Die strukturierte XML-Datei und die beigefügte PDF-Lesefassung stellen denselben Abrechnungsbeleg dar. Bitte erfassen Sie die Forderung nur einmal. Bei Abweichungen zwischen Ihrer Bestellung und unserer Abrechnung nennen Sie uns bitte die betroffene Position und den zugehörigen Vertrags- oder Nachtragsstand.',
            'Rückfragen zur Zuordnung beantworten wir über diese Projektadresse. Eine Änderung der Bankverbindung wird nicht mit dieser Nachricht erklärt.',
            'Mit freundlichen Grüßen\n'+sender[3]+'\n'+sender[0]+'\n'+sender[1]+'\n'+sender[2],
        ])
        message.set_content('\n\n'.join(body)+'\n', charset='utf-8')
        hashes = {}
        for name in (invoice['filename'], xml_name):
            source = entries[name]
            content = source.read_bytes()
            mime = mimetypes.guess_type(name)[0] or 'application/octet-stream'
            major, minor = mime.split('/', 1)
            message.add_attachment(content, maintype=major, subtype=minor, filename=name)
            hashes[name] = hashlib.sha256(content).hexdigest()
        message.set_boundary('sw-hi-'+hashlib.sha256(invoice['id'].encode()).hexdigest()[:24])
        target = CASE/'10_Rechnungen_und_Buchhaltung/Rechnungseingang'/f'{invoice["date"]}_{invoice["id"]}_Belegzugang.eml'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(message.as_bytes())
        outputs.append({'file': str(target.relative_to(CASE)), 'invoice': invoice['id'], 'date': invoice['date'], 'attachments': hashes})
    (QUALITY/'belegzugang.json').write_text(json.dumps(outputs, ensure_ascii=False, indent=2)+'\n')
    return outputs


def organisation():
    document = new_document('Projektorganisation für Bauausführung und Abrechnung', '2027-11-29')
    document.add_paragraph('Hildesheim, 29. November 2027')
    document.add_paragraph('Die Steinbogen Wohnen GmbH bestätigt die nachstehende operative Zuordnung für die beginnende Bauausführung. Die beauftragten Unternehmen, die bestehenden Planerverträge und die Zeichnungsbefugnis der Geschäftsführerin Maren Birk bleiben maßgeblich. Die benannten Mitarbeiter unterstützen die vertraglich verantwortlichen Personen innerhalb ihrer nachstehend beschriebenen Aufgaben.')
    document.add_paragraph('1. Bauherrin und Projektsteuerung', 'Heading 1')
    document.add_paragraph('Maren Birk entscheidet für die Bauherrin über Änderungen des Leistungsumfangs, zusätzliche Vergütung, Fristvereinbarungen und Zahlungen. Friedrich Weber führt die Projektkorrespondenz, bündelt Entscheidungsvorlagen und hält die freigegebenen Planstände vor. Er darf allein weder Nachträge beauftragen noch auf Mängelrechte verzichten. Erna Wagner nimmt Rechnungen und Zahlungshinweise entgegen, archiviert die strukturierten Rechnungsdateien und führt das Projektkonto mit den Buchungsbelegen zusammen.')
    document.add_paragraph('2. Planungsleitung und Objektüberwachung', 'Heading 1')
    document.add_paragraph('Nora Feld bleibt die vertragliche Ansprechpartnerin der Konturfeld Architektur PartG mbB. Hans Müller unterstützt sie bei der örtlichen Objektüberwachung, bei Begehungen und beim fortlaufenden Bautagebuch. Seine Tagesberichte beschreiben die tatsächlich festgestellten Arbeiten und Grenzen seiner Wahrnehmung. Eine technische Freigabe, ein Rechnungsabgleich und eine rechtsgeschäftliche Beauftragung werden jeweils gesondert bezeichnet. Ein Eintrag im Bautagebuch ersetzt keine Anordnung zusätzlicher Leistungen.')
    document.add_paragraph('3. Ausführende Unternehmen', 'Heading 1')
    document.add_paragraph('Timo Wendt bleibt der verantwortliche Bauleiter der Steinwerk Hochbau GmbH. Georg Schmidt führt als Polier die örtliche Kolonne. Die Vorarbeiter der weiteren Lose stimmen Anwesenheit, Materialanlieferungen und notwendige Vorleistungen mit Hans Müller ab; ihre vertraglichen Ansprechpartner bleiben für Leistungsänderungen zuständig. Eine gegenseitige Unterschrift unter einem Lieferschein bestätigt den dort ausdrücklich bezeichneten Vorgang und enthält für sich keine Abnahme des Gesamtwerks.')
    document.add_paragraph('4. Dokumentenlauf und Entscheidungen', 'Heading 1')
    document.add_paragraph('Ein Vorgang erhält im Betreff stets die Projektkennung SW-HI-26-08 und eine eindeutige Rechnung, Plan- oder Protokollnummer. Abweichende Dateifassungen bleiben mit Datum erhalten. Erna Wagner führt die Rechnung einmal je Forderung; XML und PDF sind unterschiedliche Darstellungen desselben Belegs. Vor einer Bankfreigabe werden Empfänger, Betrag, bereits veranlasste Zahlungen und der freigegebene Leistungsstand anhand der Originalunterlagen verglichen. Die Freigabe wird mit Datum und Namen dokumentiert.')
    document.add_paragraph('Eine ausbleibende Antwort gilt weder als Planfreigabe noch als Zustimmung zu Mehrkosten. Entscheidungsbedarf mit Einfluss auf Ausführung oder Termine ist noch am selben Arbeitstag an Friedrich Weber und Nora Feld zu melden. Bei Gefahr für Personen oder bei offenkundig nicht freigegebenen Arbeiten bleibt die erforderliche sofortige Unterbrechung beziehungsweise Sicherung unberührt.')
    document.add_paragraph('Für die Steinbogen Wohnen GmbH\nMaren Birk, Geschäftsführerin')
    return save_docx(document, '00_Projektsteuerung/2027-11-29_Projektorganisation.docx')


TEMPLATES = [
    ('Rechnungseingang_und_Nachforderung', 'Rechnungseingang und Anforderung fehlender Unterlagen', [
        ('1. Bezug und Eingang', '{{ANREDE}}, wir bestätigen den Eingang Ihrer Rechnung {{RECHNUNGSNUMMER}} vom {{RECHNUNGSDATUM}} über {{RECHNUNGSBETRAG}} EUR zum Auftrag {{AUFTRAGSNUMMER}}. Die Rechnung wurde am {{EINGANGSDATUM}} im Projekt {{PROJEKT}} erfasst. Diese Eingangsbestätigung enthält noch keine Erklärung zur Berechtigung der Forderung oder zum Leistungsstand.'),
        ('2. Benötigte Unterlagen', 'Für den sachlichen Abgleich benötigen wir folgende Unterlagen: {{UNTERLAGEN}}. Die offene Zuordnung betrifft die Positionen {{POSITIONEN}} und den Plan- beziehungsweise Nachtragsstand {{BEZUGSSTAND}}. Bitte übersenden Sie die fehlenden Unterlagen bis zum {{ANTWORTTERMIN}} unter derselben Rechnungsnummer. Eine erneute Rechnung mit unveränderter Forderung ist hierfür nicht erforderlich.'),
        ('3. Weiteres Vorgehen', 'Den bereits prüfbaren Rechnungsanteil behandeln wir gesondert. Ob und in welchem Umfang ein Betrag fällig ist oder zurückbehalten werden darf, ergibt sich aus dem Vertrag und den jeweiligen gesetzlichen Voraussetzungen. Die bloße Anforderung zusätzlicher Unterlagen verschiebt keine Frist, die unabhängig hiervon läuft. Unser Ansprechpartner für die weitere Abstimmung ist {{KONTAKT}}.'),
    ]),
    ('Zahlungsfreigabe', 'Zahlungsfreigabe für eine Projektforderung', [
        ('1. Zahlungsgegenstand', 'Die Rechnung {{RECHNUNGSNUMMER}} des Unternehmens {{EMPFÄNGER}} betrifft {{LEISTUNG}} aus dem Auftrag {{AUFTRAGSNUMMER}}. Der Rechnungsbetrag beträgt {{RECHNUNGSBETRAG}} EUR. Bisherige Zahlungen und Erstattungen zu dieser Forderung wurden anhand der Bankbelege {{BANKBELEGE}} abgeglichen. Der jetzt zur Freigabe vorgelegte Betrag beträgt {{ZAHLBETRAG}} EUR.'),
        ('2. Sachlicher Abgleich', 'Die technische Zuordnung wurde am {{PRÜFDATUM}} durch {{PRÜFENDE_PERSON}} anhand von {{LEISTUNGSNACHWEISE}} vorgenommen. Abweichungen vom behaupteten Leistungsstand bestehen hinsichtlich {{ABWEICHUNGEN}}. Der zugehörige Nachtrag beziehungsweise die unveränderte Vertragsgrundlage ist {{VERTRAGSGRUNDLAGE}}. Eine technische Bestätigung erklärt keine rechtsgeschäftliche Anerkennung weiterer Vergütung.'),
        ('3. Entscheidung und Ausführung', 'Die zahlungsberechtigte Person {{FREIGEBENDE_PERSON}} entscheidet am {{FREIGABEDATUM}} wie folgt: {{ENTSCHEIDUNG}}. Als Ausführungstag ist {{AUSFÜHRUNGSTAG}} vorgesehen. Vor Übermittlung des Zahlungsauftrags sind Empfänger, Bankverbindung, offene Zahlungsaufträge und der Verwendungszweck nochmals mit den freigegebenen Originaldaten abzugleichen. Eine aus einer Rechnung abweichende Bankverbindung wird nicht allein aufgrund einer E-Mail übernommen.'),
    ]),
    ('Rechnungseinwendung', 'Einwendung gegen eine konkret bezeichnete Rechnungsposition', [
        ('1. Betroffene Forderung', '{{ANREDE}}, Ihre Rechnung {{RECHNUNGSNUMMER}} vom {{RECHNUNGSDATUM}} haben wir mit dem Auftrag {{AUFTRAGSNUMMER}} und den vorliegenden Ausführungsunterlagen verglichen. Unsere Einwendung betrifft ausschließlich die nachstehend bezeichneten Positionen und Tatsachen. Die übrigen Positionen werden gesondert bearbeitet.'),
        ('2. Abweichung und Belegbezug', 'Bei Position {{POSITION}} rechnen Sie {{ABGERECHNETE_LEISTUNG}} ab. Nach den Unterlagen {{BELEGE}} ist dagegen folgender Stand dokumentiert: {{DOKUMENTIERTER_STAND}}. Daraus ergibt sich für den von uns beanstandeten Teilbetrag zunächst eine Differenz von {{DIFFERENZ}} EUR. Bitte erläutern Sie die Abweichung und legen Sie die dazugehörige Beauftragung, Mengenermittlung oder Korrektur bis zum {{ANTWORTTERMIN}} vor.'),
        ('3. Abgrenzung der Erklärung', 'Mit dieser Mitteilung erkennen wir den bestrittenen Teil der Forderung nicht an. Ein etwaiger Zahlungsverzug, ein Zurückbehaltungsrecht und die Behandlung unstreitiger Beträge sind anhand der konkreten Vertrags- und Fälligkeitslage gesondert zu beurteilen. Soweit bereits eine Zahlung veranlasst wurde, teilen wir deren Zuordnung und einen gegebenenfalls verlangten Erstattungsbetrag in einer gesonderten Erklärung mit.'),
    ]),
    ('Doppelzahlung_Rueckforderung', 'Zuordnung und Rückforderung einer doppelten Zahlung', [
        ('1. Betroffene Zahlungen', '{{ANREDE}}, auf Ihre Forderung {{RECHNUNGSNUMMER}} haben wir am {{ERSTE_ZAHLUNG}} unter der Bankreferenz {{ERSTE_REFERENZ}} und am {{ZWEITE_ZAHLUNG}} unter der Bankreferenz {{ZWEITE_REFERENZ}} jeweils {{BETRAG}} EUR überwiesen. Die beigefügten Bankbelege weisen beide Kontobelastungen aus.'),
        ('2. Abgleich und Rückzahlung', 'Nach unserem Abgleich betrifft die zweite Zahlung dieselbe Forderung und wurde nicht auf eine weitere offenstehende Rechnung angewiesen. Bitte bestätigen Sie die Zuordnung und erstatten Sie den überzahlten Betrag von {{ÜBERZAHLUNG}} EUR bis zum {{RÜCKZAHLUNGSTERMIN}} auf das nachstehend bezeichnete Projektkonto {{PROJEKTKONTO}}. Falls Sie eine andere Zuordnung annehmen, benennen Sie bitte die konkrete Forderung und den dafür maßgeblichen Beleg.'),
        ('3. Abschluss des Vorgangs', 'Die Rückzahlung ist unter Angabe von {{ERSTATTUNGSREFERENZ}} zu leisten. Wir schließen den Vorgang erst nach dem Abgleich mit dem tatsächlichen Bankeingang. Die zutreffend erfüllte ursprüngliche Forderung wird durch diese Rückzahlungsaufforderung nicht erneut zur Zahlung gestellt.'),
    ]),
]


def templates():
    helper = Path(os.environ.get('DOCX_CONTENT_CONTROLS', str(Path.home()/'.codex/plugins/cache/openai-primary-runtime/documents/26.905.11957/skills/documents/scripts/content_controls.py')))
    if not helper.exists():
        raise RuntimeError('Der gebündelte Word-Helfer für Inhaltssteuerelemente ist erforderlich.')
    output = []
    for filename, title, sections in TEMPLATES:
        document = new_document(title, '2026-09-28')
        document.add_paragraph('Projekt {{PROJEKT}} · Bearbeitung {{BEARBEITENDE_PERSON}} · Datum {{AUSFERTIGUNGSDATUM}}')
        for heading, paragraph in sections:
            document.add_paragraph(heading, 'Heading 1')
            paragraph = re.sub(r'\{\{([^}]+)\}\}', lambda match: '{{'+match[1].translate(str.maketrans({'Ä': 'AE', 'Ö': 'OE', 'Ü': 'UE', 'ß': 'SS'}))+'}}', paragraph)
            document.add_paragraph(paragraph)
        document.add_paragraph('Mit freundlichen Grüßen')
        document.add_paragraph('{{UNTERSCHRIFT_NAME}}')
        document.add_paragraph('{{FUNKTION}}')
        target = save_docx(document, '12_Wordvorlagen/Kaufmaennisch/'+filename+'.docx')
        wrapped = target.with_name('.'+target.name)
        try:
            subprocess.run([sys.executable, str(helper), str(target), 'wrap_placeholders', '--output', str(wrapped)], check=True, capture_output=True, text=True)
            wrapped.replace(target)
            normalize_docx(target)
        finally:
            wrapped.unlink(missing_ok=True)
        output.append(str(target.relative_to(CASE)))
    return output


def main():
    QUALITY.mkdir(parents=True, exist_ok=True)
    mails = invoice_mails()
    organisation()
    forms = templates()
    print(f'{len(mails)} belegbezogene E-Mails mit Originalanlagen, Projektorganisation und {len(forms)} ausformulierte Wordvorlagen mit Inhaltssteuerelementen.')


if __name__ == '__main__':
    main()
