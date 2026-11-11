#!/usr/bin/env python3
"""Baut die nativen Unterlagen zu den Hamelner Fällen ME-38 und ME-39."""
from __future__ import annotations

import argparse
import csv
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def section(heading, *paragraphs, table=None, page_break=False):
    data = {"heading": heading, "paragraphs": paragraphs}
    if table:
        data["table"] = {"headers": table[0], "rows": table[1:]}
    if page_break:
        data["page_break_before"] = True
    return data


def document(filename, title, issuer, date, *sections):
    return dict(filename=filename, title=title, issuer=issuer, date=date, sections=sections)


def mail(filename, sender, to, date, subject, *paragraphs, attachments=(), reply_to=None):
    name, address = sender
    return dict(filename=filename, from_name=name, from_email=address, to_email=to,
                date=date, subject=subject, paragraphs=paragraphs, attachments=attachments,
                reply_to=reply_to)


def table(filename, headers, *rows):
    return dict(filename=filename, headers=headers, rows=rows)


GIFT = {
    "id": "ME-38",
    "slug": "compliance-hameln-geschenk-geschaeftsfuehrung",
    "company": "Merrensteg Leistungsmodule GmbH",
    "project": "Merrensteg Leistungsmodule · Hameln",
    "message_domain": "merrensteg.example",
    "documents": [
        mail(
            "01_Freigabeanfrage_Einkauf.eml", ("Enna Barlach", "enna.barlach@merrensteg.example"),
            "integritaet@merrensteg.example", "2026-11-03T08:18:00+01:00",
            "ME-38 | Kann Bestellung KW 45 heute in die Freigabe?",
            "Guten Morgen, ich brauche bis 13.00 Uhr eine Entscheidung für PK-447. Die Merrensteg Leistungsmodule GmbH baut in Hameln Stromrichter für Roboterlinien. Wir benötigen ab KW 49 Kupferschienen, die im Stromrichter den Strom zwischen Netzteil und Antrieb führen. Ohne sie stehen im Dezember zwei Montagelinien. Der Einkauf hat drei Unternehmen zur Angebotsabgabe eingeladen. Die technische Erprobung ist abgeschlossen. Eine Bestellung gibt es noch nicht.",
            "Mein Dashboard zeigt seit gestern einen grünen Haken für die von Altesiel angebotene Schulung. Im Postfach des Geschäftsführerbüros liegt jetzt eine Reservierung für ein Hotelwochenende mit Konzertkarten. Der Lieferant hat mich am Telefon gefragt, ob sein Geschäftsführer am Freitag für die Verkündung unserer Entscheidung vorbeikommen könne. Ich habe ihm gesagt, dass die Unterschrift offen ist.",
            "Sven Lorberg ist unser Geschäftsführer und zeichnet allein ab 250.000 EUR. Ich erstelle die Vergabeempfehlung. Seine Assistenz verwaltet seinen Kalender. Wenn Lorberg wegen eines persönlichen Interesses ausfällt, brauche ich heute eine belastbare Zeichnungsregel und eine Entscheidung zur Zwischenversorgung.",
            "Enna Barlach · Strategischer Einkauf",
            attachments=("02_Vergabevermerk_und_Kontrollregel.docx",),
        ),
        document(
            "02_Vergabevermerk_und_Kontrollregel.docx", "Beschaffungsstand und Freigaberegel",
            "Strategischer Einkauf", "2026-11-03",
            section("Bedarf und Vergleichsgrundlage",
                    "Der private Beschaffungsvorgang PK-447 betrifft 12.000 fertigungsspezifische Kupferschienen für das erste Halbjahr 2027. Die ersten 800 Stück werden bis 4. Dezember 2026 benötigt, damit ein Anlagenkunde im Januar abgenommen werden kann. Der erste Teiltermin und die vollständige Einhaltung des technischen Freigabestands Zeichnung K-17 sind als Mussbedingungen dokumentiert. Der bestehende Rahmenvertrag mit Okerbucht läuft aus. Restmaterial deckt die Montage bis 1. Dezember.",
                    "Alle folgenden Preise beziehen sich auf 12.000 Stück, netto einschließlich Verpackung und Anlieferung. Der Einkauf hat die Lieferzusagen schriftlich abgefragt und nach Erprobung der jeweiligen Muster dokumentiert. Die Entscheidung ist offen.",
                    table=[
                        ["Unternehmen", "Preis EUR", "Erste 800 Stück", "Zeichnung K-17"],
                        ["Altesiel Metallform GmbH", "384.600", "03.12.2026", "Freigegeben"],
                        ["Okerbucht Verbindungstechnik GmbH", "393.200", "04.12.2026", "Freigegeben"],
                        ["Deisterstrom Präzision GmbH", "368.900", "15.12.2026", "Freigegeben"],
                    ]),
            section("Zeichnungsordnung und Zwischenversorgung",
                    "Sven Lorberg zeichnet für die Gesellschaft im Regelfall Bestellungen über 250.000 EUR. Nach Zeichnungsordnung ZO-06 Abschnitt 4 legt der Einkauf einen dokumentierten Interessenkonflikt dem Vorsitz der Gesellschafterversammlung zur Entscheidung über eine unbefangene Vertretung und deren Zeichnungsbefugnis vor. Die Konzern-Compliance kann eine Kurzsperre im Einkaufssystem veranlassen. Sie erteilt keinen Auftrag.",
                    "Okerbucht kann nach schriftlicher Bestätigung bis 5. November 12.00 Uhr 800 Stück für 28.400 EUR zum 4. Dezember liefern. Die Option ist bis dahin ohne Gebühr reserviert. Bei einem Folgeauftrag werden die 800 Stück auf Menge und Preis von dessen Rahmenauftrag angerechnet. Der Einkauf bestätigt die Option erst nach schriftlicher Freigabe und dokumentiert den verbleibenden Bedarf."),
            section("Auszug aus Richtlinie Zuwendungen ZW 04",
                    "Beschäftigte und Geschäftsführung melden angebotene private Vorteile im Zuwendungsregister. Während laufender Lieferantenauswahlen gilt die Vorabklärung mit Compliance unabhängig vom Wert. Eine fachliche Veranstaltung ohne private Begleitung wird anhand von Zweck, Teilnehmerkreis und Kosten geprüft. Ändern sich diese Angaben nach der Freigabe wesentlich, ist eine erneute Prüfung erforderlich. Ein Kalendertermin ersetzt die Prüfung nicht.",
                    "Stand der Richtlinie: 01.09.2026. Bei einem Angebot an die Geschäftsführung ist die lokale Geschäftsleitung aus der Einzelfreigabe herauszuhalten. Der Fachbereich dokumentiert Einladungszweck, Wert, Beteiligte und Entscheidungsbezug. Die interne Richtlinie regelt die unternehmensinterne Prüfung."),
        ),
        mail(
            "03_Einladung_Fachschulung.eml", ("Martina Stuve", "martina.stuve@altesiel.example"),
            "assistenz.lorberg@merrensteg.example", "2026-10-22T10:16:00+02:00",
            "Zwei Plätze für K-17 Messtechnik am 6. November",
            "Guten Tag Frau Wiemken, wir haben zwei Plätze für die Vorführung am Prüfstand reserviert. Am 6. November von 14.00 bis 17.00 Uhr zeigen wir am Standort Altesiel, wie wir die Oberflächenmessung bei Ihrer Schiene K-17 reproduzieren. Namentlich haben wir Herrn Lorberg und Frau Barlach eingetragen. Der Gegenwert beträgt insgesamt 160 EUR. Anreise und Übernachtung organisieren und zahlen Sie gegebenenfalls selbst.",
            "Mit freundlichen Grüßen, Martina Stuve · Vertriebsleitung Altesiel Metallform GmbH",
        ),
        mail(
            "04_Nachricht_des_Bieters.eml", ("Martina Stuve", "martina.stuve@altesiel.example"),
            "assistenz.lorberg@merrensteg.example", "2026-11-02T11:14:00+01:00",
            "Re: Zwei Plätze für K-17 Messtechnik am 6. November",
            "Hallo Frau Wiemken, die Schulung fällt wegen Stillstands am Prüfstand aus. Stattdessen haben wir das Wochenende 6. bis 8. November im Hotel Sandbucht für Herrn Lorberg und seine Begleitung reserviert. Es gibt vier Plätze für das Abendkonzert am Samstag. Zwei weitere Gäste kann er selbst benennen. Zimmer, Abendessen und Konzert gehen auf uns. Im Portal haben wir nur die bestehende Anmeldung EF-511 geändert.",
            "Für PK-447 wäre die Bekanntgabe am Freitag hilfreich. Könnten Sie uns bis zum Mittag einen Termin mit Herrn Lorberg einstellen? Wir würden den Lieferplan dann direkt bei dem Abendessen mit ihm durchgehen. Für die Hotelreservierung brauchen wir eine Bestätigung der beiden Namen bis Mittwoch 18.00 Uhr.",
            "Viele Grüße, Martina Stuve",
            attachments=("05_Hotel_Reservierungsauszug.pdf",),
            reply_to="03_Einladung_Fachschulung.eml",
        ),
        document(
            "05_Hotel_Reservierungsauszug.pdf", "Reservierungsbestätigung Sandbucht",
            "Hotel Sandbucht · Reservierung", "2026-11-02",
            section("Buchungsstand SB 16604",
                    "Auftraggeberin und Kostenübernehmerin ist die Altesiel Metallform GmbH. Die Reservierung betrifft den 6. bis 8. November 2026. Das Hotel führt Sven Lorberg als angefragten Hauptgast. Der Name der Begleitung und die Namen für zwei weitere Konzertkarten sind offen. Die Buchung wurde auf Anforderung der Vertriebskontaktperson angelegt.",
                    table=[
                        ["Leistung", "Menge", "Betrag einschließlich Steuern"],
                        ["Wochenendpaket einschließlich Abendessen", "2 Gäste", "1.280,00 EUR"],
                        ["Abendkonzert am 7. November", "4 Karten", "310,00 EUR"],
                        ["Gesamtbetrag laut Reservierung", "", "1.590,00 EUR"],
                    ]),
            section("Bestätigung und Zahlung",
                    "Status im Hotelprogramm am 2. November 2026 um 10.52 Uhr: Option. Bis 4. November 18.00 Uhr kann die Auftraggeberin die Namen bestätigen oder die Option kostenfrei freigeben. Es liegt noch keine Zimmerliste oder persönliche Bestätigung der benannten Gäste vor. Nach Bestätigung rechnet das Hotel mit der Auftraggeberin ab. In dieser Bestätigung ist kein Zahlungseingang vermerkt."),
        ),
        table(
            "06_Freigabeportal_Ereignisse.csv",
            ["Zeit CET/CEST", "Vorgang", "Version", "Ereignis", "Konto", "Wert EUR", "Gegenstand", "Freigabeverweis"],
            ["2026-10-22T10:21:11+02:00", "EF-511", "1", "erstellt", "einkauf.barlach", "160.00", "Prüfstandschulung für Lorberg und Barlach", ""],
            ["2026-10-23T08:42:29+02:00", "EF-511", "1", "genehmigt", "compliance.breede", "160.00", "fachliche Schulung ohne Begleitperson, ohne Hotel", "ZW-2026-119"],
            ["2026-11-02T09:31:08+01:00", "EF-511", "2", "Import Lieferantenportal", "svc.vendor-sync", "1590.00", "Hotel für zwei Personen und vier Konzertkarten", ""],
            ["2026-11-02T09:31:09+01:00", "EF-511", "2", "Hinweisstatus auf Karte synchronisiert", "svc.dashboard", "1590.00", "Kartenstatus grün aus Vorgangsversion 1", "ZW-2026-119"],
            ["2026-11-02T11:45:05+01:00", "EF-511", "2", "Kalendereintrag vorläufig", "assistenz.wiemken", "1590.00", "Gastgebertermin vorgemerkt", ""],
            ["2026-11-03T07:55:01+01:00", "EF-511", "2", "Revision exportiert", "audit.readonly", "1590.00", "kein neues Prüfereignis im Export", ""],
        ),
        mail(
            "07_Notiz_der_Assistenz.eml", ("Wiebke Wiemken", "wiebke.wiemken@merrensteg.example"),
            "integritaet@merrensteg.example", "2026-11-03T09:12:00+01:00",
            "ME-38 | Mein Kontakt mit Altesiel und Kalenderstand",
            "Ich habe gestern um 11.45 Uhr einen unverbindlichen Termin für Freitag in Herrn Lorbergs Kalender gelegt. Ich habe Frau Stuve am Telefon gesagt, dass ich die Nachricht erhalten habe und intern Rücksprache halte. Als Gast habe ich außer dem vorausgefüllten Namen niemanden genannt. Ich habe das Hotel nicht kontaktiert. Die Reservierung habe ich erst heute Morgen ganz gelesen.",
            "Herr Lorberg schrieb gestern auf dem Diensthandy: „Setzen Sie Altesiel bitte Freitagmittag auf die Liste. Den Rest klären wir noch.“ Ich weiß nicht, ob er die Nachricht mit der Reservierung gesehen hatte. Die Terminnotiz im Kalender lautet nur „Altesiel PK-447, Entscheidung offen“. Wenn ihr mit ihm sprecht, er ist heute bis 10.30 Uhr in einer Kundenabnahme.",
            "Wiebke Wiemken · Geschäftsführungsassistenz",
        ),
        document(
            "08_Anwendungsprotokoll_Freigabeportal.docx", "Prüfstand des Freigabeportals",
            "Interne Revision · Arved Kern", "2026-11-03",
            section("Was der grüne Kartenstatus zeigt",
                    "Die Startansicht führt pro Vorgang eine grüne oder graue Statuskarte. Der grüne Status beruht auf dem letzten vorhandenen Freigabeobjekt für die Vorgangsnummer. In der Versionsansicht führt das System die Inhalte des Imports sowie Freigabeobjekte mit Versionsbezug. Nach automatischen Lieferantenänderungen kann die Startkarte bis zur erneuten Prüfung den früheren Status anzeigen.",
                    "Die Revision exportierte am 3. November um 7.55 Uhr die Ereignisse zu EF-511 seit Eröffnung. Der Export weist die Freigabe ZW-2026-119 nur für Version 1 aus. Version 2 enthält die neue Beschreibung und den neuen Gesamtwert. Ob eine Freigabe außerhalb des Systems erteilt wurde, ergibt sich aus dem Export nicht. Der Aktenstand enthält bis 9.00 Uhr dazu keine separate Erklärung."),
            section("Revisionssicherung und Grenzen der Zuordnung",
                    "Der Export enthält die Kontokennung, wie sie der Dienst zum Ereigniszeitpunkt erfasst hat. Der Import unter svc.vendor-sync nennt keine natürliche Person. Beim Auswerten sind Zeitzonen, Aktivität des Dienstkontos und der Originalinhalt des Importereignisses zu sichern. Eine Änderung der Darstellung am laufenden Vorgang sollte erst nach Erhalt der Originalprotokolle vorgenommen werden.",
                    "Anrufnotiz, Kalender und Hotelreservierung bilden eigene Quellen. Aus dem technischen Ablauf lässt sich nicht ableiten, ob Lorberg vom Inhalt wusste, die Leistungen annahm oder seine Vergabeentscheidung tatsächlich danach richtete."),
        ),
        document(
            "09_Vorlage_Entscheidungsvorlage.docx", "Entscheidung über Beschaffung und Zuwendung",
            "Recht und Compliance · Arbeitsvorlage", "2026-11-03",
            section("Entscheidungsfrage",
                    "Bis [Datum und Uhrzeit] soll [zuständige und unbefangene Stelle] über [vorläufige Beschaffungsmaßnahme] und [Behandlung der Zuwendung] entscheiden. Die betroffenen Bestell- und Registervorgänge lauten [Kennungen]."),
            section("Belegter Sachverhalt und offene Punkte",
                    "Die Unterlage [Fundstelle mit Version und Datum] belegt [konkrete Tatsache]. Die Behauptung [widersprechende Aussage] ergibt sich aus [Quelle]. Zur Klärung wird [zuständige Funktion] bis [Zeit] [konkreten Beleg] anfordern."),
            section("Behandlung der Zuwendung",
                    "Wir schlagen vor, dass [zuständige Funktion] die [noch bestehende Option oder Leistung] bis [Zeit] auf dem Weg [Kontaktweg] behandelt. Die zuständige Stelle dokumentiert getrennt [Richtlinienprüfung], [Prüfbedarf zum Entscheidungsbezug] und [Ermittlungsschritt]."),
            section("Lieferkontinuität und Entscheidungsschutz",
                    "Die Versorgung bis [Datum] wird durch [Option mit Preis, Menge und Vorbehalt] gesichert. Die endgültige Bestellung bleibt bei [Stelle] zur Freigabe. [Funktion] sichert die relevanten Dateien, das Änderungsprotokoll und die Originalnachrichten bis [Zeit]."),
        ),
    ],
}


RELAY = {
    "id": "ME-39",
    "slug": "compliance-hameln-sicherheitsrelais-hinweis",
    "company": "Merrensteg Elektrosysteme SE",
    "project": "Merrensteg Elektrosysteme · Hameln",
    "message_domain": "merrensteg.example",
    "documents": [
        mail(
            "01_Kundenmeldung_Beinaheunfall.eml", ("Falk Westermann", "falk.westermann@leinetakt.example"),
            "produktservice@merrensteg.example", "2026-11-04T07:46:00+01:00",
            "P1 | SR-24X2 bei geöffneter Schutztür noch freigegeben",
            "Guten Morgen, wir bauen Verpackungsmaschinen. Gestern gegen 16.20 Uhr bewegte sich der Kartonschieber der Zelle LT-V9 im Automatikbetrieb nach einem Stopp wieder. Die seitliche Schutztür stand noch offen. Eine Einrichterin hatte sich gerade zurückgezogen. Nach unseren bisherigen Informationen wurde niemand verletzt. Die Anlage steht seit 16.24 Uhr verriegelt. Wir brauchen bis 9.00 Uhr eine belastbare Zwischeninformation für unseren Produktionskunden.",
            "Auf dem Foto im gesicherten Serviceportal ist die Seriennummer SR26-10318 zu erkennen. Auf dem Schaltschrankplan ist das Bauteil als separates Merrensteg-Sicherheitsrelais SR-24X2 ausgewiesen. Es soll verhindern, dass die Maschine bei offener Schutztür einen neuen Fahrbefehl ausführt. In unserem Protokoll waren Tür und Anzeige offen, obwohl die Freigabe des Antriebs noch anlag. Wir sichern Schaltplan, Konfiguration und Steuerungslog. Eine zweite Zelle mit Relais aus derselben Lieferung halten wir bis zur Klärung außer Betrieb.",
            "Falk Westermann · Leitung Inbetriebnahme Leinetakt Anlagenbau GmbH",
        ),
        document(
            "02_Produktblatt_und_Verantwortung.docx", "Sicherheitsrelais SR 24X2 in Maschinenzellen",
            "Produkttechnik · Nika Rottkamp", "2026-11-04",
            section("Welche Aufgabe das Relais erfüllt",
                    "Die Merrensteg Elektrosysteme SE entwickelt und fertigt in Hameln ein separat verkauftes Sicherheitsrelais für gewerbliche Maschinenintegratoren. Es überwacht zwei Signale derselben Schutztür. Das Relais gibt den angeschlossenen Maschinenantrieb nur frei, wenn beide Signale plausibel geschlossen sind und die Steuerung nach dem Stopp ordnungsgemäß zurückgesetzt wurde. Wird die Schutztür geöffnet oder wird ein Fehler erkannt, muss der Ausgang in den sicheren Zustand wechseln. Eine einfache Standardsteuerung könnte die Maschine bewegen, würde aber die hier geschuldete Schutzfunktion nicht gewährleisten.",
                    "Das Relais wird als eigenständiger Artikel SR-24X2 unter eigenem Namen in Deutschland und der EU erstmals bereitgestellt. Die dreistellige Baugruppenkennung auf dem Lieferschein reicht nicht aus, um die Softwareversion zu bestimmen. Die Gerätekennung am Typenschild lässt sich dagegen mit der Softwareversion und dem Produktionslos im ERP verknüpfen."),
            section("Freigabe und Nachweis im Werk",
                    "Produkttechnik verantwortet die Sollfunktion und den Prüfplan, Qualität den verbindlichen Freigabestatus für das einzelne Los. Produktionsplanung koordiniert Termine und Lager. Die Logistik darf aus dem Status FREI kommissionieren. Für das Relais gibt es technische Unterlagen und eine EG-Konformitätserklärung aus der ursprünglichen Produktfreigabe. Ob der in der aktuellen Geräteversion enthaltene Prüfmodus von der Risikobeurteilung und der Änderungsfreigabe erfasst wurde, muss geprüft werden.",
                    "Die Serien-Endprüfung erfasst im Los L261026 die Sicherheitssignale beim ersten Einschalten. Ein weiterer Fall des Wiederanlaufs nach einem kurzzeitigen Spannungsausfall mit Tür geöffnet ist im Prüfplan für die Entwicklungsfreigabe vorgesehen. Im Ordner zu Version 2.6.4 ist bis zur Aktenübergabe kein unterschriebener Datensatz für diese Prüfung auffindbar. Die Produktionsdatei weist Version 2.6.4 für das ganze Los aus."),
            section("Zuständigkeiten bei einem Vorfall",
                    "Der interne Produktsicherheitskreis unter Leitung von Nika Rottkamp nimmt technische Befunde auf und verfolgt den Warenweg. Lieferanten und Integratoren bekommen eine technische Sachstandsinformation über Produktservice. Recht bewertet die einschlägigen Maßnahmen und Behördenkontakte je Rolle und Land mit der Produktsicherheit. Die interne Meldestelle führt Eingänge und Identitätsdaten getrennt. Personalmaßnahmen werden von einer unabhängigen Personalstelle bearbeitet."),
        ),
        document(
            "03_Prueflabor_Kurzbericht.pdf", "Reproduktionsversuch zum Wiederanlauf",
            "Prüflabor Hameln · Laborleitung", "2026-11-04",
            section("Prüfumfang und Befund",
                    "Im Werkslabor wurden um 9.05 Uhr zwei Rückstellmuster des Loses L261026 mit Geräteversion 2.6.4 in einem abgesperrten Prüfaufbau untersucht. Das Ergebnis betrifft einen spezifischen Wiederanlauf nach einer kurzen Spannungsunterbrechung bei geöffneter Schutztür. Der Prüfaufbau nutzt einen Prüfverbraucher und keinen Bewegungsantrieb.",
                    table=[
                        ["Gerät", "Merkmal", "Ergebnis"],
                        ["SR26-10401", "L261026 · Version 2.6.4", "Sicherer Ausgang blieb im Versuch unzulässig freigegeben."],
                        ["SR26-10402", "L261026 · Version 2.6.4", "Sicherer Ausgang blieb im Versuch unzulässig freigegeben."],
                        ["SR26-09821", "Vorlos L191026 · Version 2.6.3", "Sicherer Ausgang schaltete ab. Einzelner Vergleichsversuch."],
                    ]),
            section("Grenzen des Befunds",
                    "Im normalen Einschaltversuch ohne die Ausfallfolge reagierten alle drei Geräte bestimmungsgemäß. Der Befund ist mit einem im Gerät verbliebenen Werksprüfzustand vereinbar. Welche Änderung ihn ausgelöst hat und wie weit er sich auf andere Lose erstreckt, ist offen. Das beim Kunden eingesetzte Gerät war bei Berichtsabschluss um 9.35 Uhr noch nicht im Labor. Die Logdaten des Kunden müssen gesichert und abgeglichen werden.",
                    "Die beiden Rückstellmuster liegen seit Abschluss im gesperrten Laborschrank. Originalprüfdaten und Versionsabbilder werden unter P-39-118 gesichert. Bericht elektronisch freigegeben durch Paula Erxleben, Leitung Prüflabor, am 4. November um 9.42 Uhr."),
        ),
        table(
            "04_ERP_Losbewegungen.csv",
            ["Datum", "Beleg", "Los", "Seriennummer von", "Seriennummer bis", "Ort oder Abnehmer", "Menge", "davon eingebaut bestätigt", "Stand bestätigt am"],
            ["2026-10-29", "LS-8112", "L261026", "SR26-10001", "SR26-10120", "Nesselholm Automation GmbH, DE", "120", "28", "2026-11-04 10:18"],
            ["2026-10-30", "LS-8126", "L261026", "SR26-10121", "SR26-10230", "Zavelpoort Industrie NV, BE", "110", "21", "2026-11-04 10:26"],
            ["2026-11-02", "LS-8140", "L261026", "SR26-10231", "SR26-10320", "Leinetakt Anlagenbau GmbH, DE", "90", "15", "2026-11-04 10:41"],
            ["2026-11-04", "WH-1307", "L261026", "SR26-10321", "SR26-10480", "Werksbestand Hameln einschließlich Rückstellmuster", "160", "0", "2026-11-04 09:56"],
        ),
        table(
            "05_ERP_Freigabeereignisse.csv",
            ["Zeit CET", "Los", "Konto", "Ereignis", "Vorher", "Nachher", "Referenz", "Belegtext"],
            ["2026-10-28T13:21:04+01:00", "L261026", "qa.pruefstand", "Prüflos angelegt", "", "QA_HOLD", "P-39-102", "Fehlender Wiederanlauftest"],
            ["2026-10-28T16:47:13+01:00", "L261026", "planung_nacht", "Status manuell gesetzt", "QA_HOLD", "FREI", "", "Auslieferung KW 44, Laborbefund wird nachgereicht"],
            ["2026-10-28T16:47:20+01:00", "L261026", "svc.warehouse", "Status synchronisiert", "QA_HOLD", "FREI", "QUEUE-131", "Kommissionierung möglich"],
            ["2026-10-29T08:31:15+01:00", "L261026", "lager.scan", "Warenausgang", "FREI", "FREI", "LS-8112", "Teilmenge 120"],
            ["2026-10-30T11:05:51+01:00", "L261026", "lager.scan", "Warenausgang", "FREI", "FREI", "LS-8126", "Teilmenge 110"],
            ["2026-11-02T10:32:11+01:00", "L261026", "lager.scan", "Warenausgang", "FREI", "FREI", "LS-8140", "Teilmenge 90"],
            ["2026-11-04T08:14:39+01:00", "L261026", "qa.hinrichs", "Chargensperre gesetzt", "FREI", "QA_HOLD", "P-39-118", "Werksbestand sperren, Kundenstatus noch ungeklärt"],
        ),
        mail(
            "06_ERP_Beweissicherung.eml", ("Janka Thormann", "janka.thormann@merrensteg.example"),
            "produktsicherheit@merrensteg.example", "2026-11-04T11:14:00+01:00",
            "ME-39 | Auszüge gesichert, Benutzerzuordnung offen",
            "Die Anlagen enthalten den Warenausgang für Los L261026 und den Statusverlauf mit Zeitstempeln. Die 160 im Werk erfassten Stücke schließen die beiden im Labor geprüften Rückstellmuster ein. Die drei bestätigten Einbauzahlen stammen aus Rückrufen des Produktservice. Es ist noch offen, ob weitere Geräte an Betreiber geliefert oder inzwischen in Maschinen eingebaut wurden.",
            "Am 28. Oktober nutzte die Produktionsplanung das Funktionskonto planung_nacht an zwei Schichtterminals. Der Export weist für die Statusänderung um 16.47 Uhr dieses Konto aus. Er enthält keine personenbezogene Anmeldung oder eindeutige Zuordnung zu einem Terminal. Ich kann auf dieser Basis keine Person als Verursacherin benennen. Die Rolle besaß durch eine Migrationszuordnung technisch die Möglichkeit, eine Qualitätsblockade zu lösen. Diese Berechtigung ist inzwischen entzogen.",
            "Gesichert sind Rohereignisse und Warehouse-Warteschlange für den Zeitraum 27. Oktober bis 4. November sowie die damalige Rollenkonfiguration. Der Dateisatz liegt im geschützten Revisionsspeicher. Der Auszug enthält bewusst nur dieses Los. Bis heute 15.00 Uhr prüfe ich weitere Nutzungen derselben Rolle an anderen Losen.",
            attachments=("04_ERP_Losbewegungen.csv", "05_ERP_Freigabeereignisse.csv"),
        ),
        mail(
            "07_Meldestelle_Geschuetzter_Eingang.eml",
            ("Interne Meldestelle", "meldestelle@merrensteg.example"),
            "folgepruefung.meldestelle@merrensteg.example", "2026-11-04T08:05:00+01:00",
            "Geschützt | ML-2026-039 | Erstmeldung und Ergänzung",
            "Zugriff nur für Meldestelle und benannte Folgebearbeitung. In diesem Auszug wird die hinweisgebende Person als H-039 geführt. Die interne Meldestelle hat die Meldung am 30. Oktober um 07.38 Uhr über den sicheren Kanal erhalten und noch am selben Tag bestätigt. In der Meldung heißt es: „Ich habe nach dem Schichtwechsel im ERP gesehen, dass das Relaislos trotz fehlendem Wiederanlauftest als frei angezeigt wurde. Meine Rückfrage in der Schichtübergabe wurde mit Lieferdruck beantwortet. Den eingetragenen Status habe ich nicht gesetzt.“",
            "Am 3. November um 17.42 Uhr schrieb H-039 erneut: „Seit Montag bin ich für vier Nachtschichten eingeteilt. Im ausgehängten Plan von Freitagmorgen hatte ich diese Woche Tagschichten in der Endprüfung. Nacht passt wegen meiner Betreuungspflichten kaum. Ich glaube, das hängt mit meiner Meldung zusammen. Meine Schichtleitung sagte beim Kaffee, dass ich von jetzt an aus der Freigaberunde raus sei. Ich will wissen, ob die Änderung überprüft werden kann.“",
            "Die Meldestelle gibt an die Produktsicherheit zunächst nur Los, Fehlersymptom und Prüfhinweis weiter. Die Kenntnis der Schichtleitung von der Meldung und die Gründe für die konkrete Einteilung sind ungeklärt. Der Vorgang enthält keine Freigabe zur Weitergabe von Identitätsdaten. Auch in der Produktionsorganisation dürfen keine Rückschlüsse aus Zugangsdaten, Schichtlisten oder Ausdruckmerkmalen provoziert werden.",
        ),
        document(
            "08_Personalvermerk_Schichtversionen.docx", "Abgleich der Schichtpläne für Woche 45",
            "Personalrevision · geschützter Auszug", "2026-11-04",
            section("Quellen und tatsächliche Einteilung",
                    "In der Werksendprüfung arbeiten zwölf Beschäftigte mit Qualifikation für die Relaisprüfung. Der am 30. Oktober um 06.50 Uhr ausgehängte Plan weist für die in diesem Auszug als H-039 geführte Person vier Tagschichten in der Endprüfung vom 3. bis 6. November aus. Die im Schichtplanungsdienst am 2. November um 11.06 Uhr publizierte Version weist H-039 für dieselben Tage vier Nachtschichten in der Nachprüfung zu. Ein Änderungsvermerk zu individuellen Gründen steht in beiden Versionen nicht.",
                    "Der Planungsvorschlag vom 29. Oktober um 16.05 Uhr nennt zwei zusätzliche Nachtplätze für eine befristete Nachprüfung. Er enthält keine Namen. Der für die Einteilung zuständige Schichtleiter erklärt am 4. November auf Nachfrage, er habe H-039 wegen Erfahrung mit Relaisprüfungen ausgewählt. Nach dem anonymisierten Qualifikationsauszug kommen drei weitere Beschäftigte in Betracht. Wer kurzfristig zur Verfügung stand und wie die Auswahl dokumentiert wurde, ist offen."),
            section("Kenntnis, Dienstplan und Betriebsrat",
                    "Der Meldestellen-Auszug weist keine Weitergabe der Identität an die Schichtleitung aus. Nach der Erstmeldung hat die Produktsicherheit eine allgemeine Anforderung zu Los L261026 gestellt. Die Schichtleitung war in der Runde, in der diese Anforderung erläutert wurde. Zeitpunkt und Inhalt der mündlichen Information sind zu klären. Der Zeitabgleich alleine belegt keine Kenntnis der Meldung oder der meldenden Person.",
                    "Im Personalbereich liegt die Betriebsvereinbarung BV-07 zur Schichtplanung. Sie sieht für veröffentlichte Planänderungen ein dokumentiertes Verfahren unter Einbeziehung des Betriebsrats vor. Für Version 2 ist bisher nur eine allgemeine Nachricht über zusätzlichen Nachtbedarf gefunden worden. Eine Beteiligung zur konkreten Planänderung ist im bereitgestellten Auszug noch nicht nachgewiesen. Die geplante Nachprüfung läuft auch dann weiter, wenn die konkrete Personeneinteilung überprüft wird."),
            section("Vertrauliche Bearbeitung",
                    "Der Personenkreis für die Prüfung erhält nur die jeweils erforderlichen Angaben. Die Produktunterlagen tragen keinen Beschäftigtenbezug. Der vorliegende Auszug ist innerhalb der Personalrevision und der zuständigen Folgebearbeitung zu halten."),
        ),
        document(
            "09_Vorlage_Sofortmassnahmen.docx", "Entscheidung zu einem Produktsicherheitsvorfall",
            "Produktsicherheit und Recht · Arbeitsvorlage", "2026-11-04",
            section("Vorläufiger Befund",
                    "Das Produkt [Bezeichnung und Funktion] kann unter [belegte Betriebsbedingung] die Funktion [Schutzfunktion] verfehlen. [Fundstellen] belegen [Befund]. Bis [Zeit] prüft [Funktion] die offenen Fragen [konkret angeben]."),
            section("Warenweg und Maßnahmen",
                    "Von [Anzahl] Geräten des Loses [Kennung] sind [Anzahl] im Werk, [Anzahl] ausgeliefert und davon [Anzahl] bestätigt eingebaut. [Funktion] veranlasst bis [Zeit] [Maßnahme im Werk]. [Funktion] legt für den Warenweg [Adressaten und Länder] die vorläufigen Schutz- und Informationsmaßnahmen vor. Der nächste Rücklauf ist bis [Zeit] vorgesehen."),
            section("Information und Wiederfreigabe",
                    "Die zuständige Stelle bewertet anhand von [Rechtsstand, Rolle, Risiko und Land], ob und wann eine Information an [Behörde, Integrator oder Betreiber] abzugeben ist. Die Freigabe zum weiteren Vertrieb und Einsatz erfordert [technische Nachweise und Freigabestelle]."),
            section("Vertraulicher Personalvorgang",
                    "Die zuständige Folgebearbeitung prüft [offene Personalfrage] im geschützten Vorgang. [Funktion] sichert [konkrete Quellen] und bewertet bis [Zeit] eine vorläufige Maßnahme zum Schutz der betroffenen Person. Für den Produktsicherheitskreis werden allein [erforderliche Sachinformationen] bereitgestellt."),
        ),
    ],
}


def build(output_root, fonts):
    spec = importlib.util.spec_from_file_location(
        "hameln_native_writer", ROOT / "scripts" / "build-projekteinkauf-baubranche-akten.py"
    )
    writer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(writer)
    writer.set_fonts(fonts)
    for case in (GIFT, RELAY):
        directory = output_root / "testakten" / case["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        documents = {record["filename"]: record for record in case["documents"]}
        emails = []
        for filename, record in documents.items():
            path = directory / filename
            match path.suffix:
                case ".docx":
                    writer.write_docx(path, record, case)
                case ".pdf":
                    writer.write_pdf(path, record, case)
                case ".csv":
                    with path.open("w", newline="", encoding="utf-8") as stream:
                        csv.writer(stream, lineterminator="\n").writerows(writer.rows(record))
                case ".eml":
                    emails.append((path, record))
        for path, record in emails:
            writer.write_eml(path, record, case, directory, documents)
        print(f"{case['id']}: {len(documents)} native Unterlagen in {directory}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=ROOT)
    parser.add_argument("--fonts", type=Path, required=True)
    args = parser.parse_args()
    build(args.output_root.resolve(), args.fonts.resolve())
