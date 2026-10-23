"""Falldaten: Filmrechte, Sicherheiten und Asset Deal in der Insolvenz.

Das Modul enthält ausschließlich fiktive Eingangs- und Originalunterlagen. Die
Unterlagen bilden unterschiedliche Sicherungsgegenstände und eine lückenhafte
Rechtekette ab, nehmen deren rechtliche Einordnung aber nicht vorweg.
"""

from __future__ import annotations

from typing import Any


def _section(title: str, *paragraphs: str) -> dict[str, Any]:
    return {"heading": title, "paragraphs": list(paragraphs)}


def _doc(
    path: str,
    kind: str,
    title: str,
    *,
    paragraphs: list[str] | None = None,
    sections: list[dict[str, Any]] | None = None,
    tables: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {"path": path, "kind": kind, "title": title}
    if paragraphs:
        item["paragraphs"] = paragraphs
    if sections:
        item["sections"] = sections
    if tables:
        item["tables"] = tables
    return item


def _mail(
    path: str,
    title: str,
    *,
    sender: str,
    to: list[str],
    date: str,
    subject: str,
    body: str,
    cc: list[str] | None = None,
    attachments: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "path": path,
        "kind": "eml",
        "title": title,
        "from": sender,
        "to": to,
        "cc": cc or [],
        "date": date,
        "subject": subject,
        "body": [body],
        "attachments": attachments or [],
    }


def _xlsx(path: str, title: str, sheets: list[dict[str, Any]]) -> dict[str, Any]:
    return {"path": path, "kind": "xlsx", "title": title, "sheets": sheets}


def _csv(
    path: str,
    title: str,
    headers: list[str],
    rows: list[list[Any]],
) -> dict[str, Any]:
    return {
        "path": path,
        "kind": "csv",
        "title": title,
        "headers": headers,
        "rows": rows,
    }


CASE: dict[str, Any] = {
    "slug": "filmrechte-sicherungsuebertragung-insolvenz-schwetzingen",
    "title": "Die letzte Rieslingspur zwischen Filmsicherheiten und Insolvenzverkauf",
    "short_title": "Die letzte Rieslingspur – Filmrechte in der Insolvenz",
    "plugin": "fachanwalt-urheber-medienrecht",
    "summary": (
        "Die Mannheimer Palatina Medienbank AG finanzierte den Spielfilm Die letzte "
        "Rieslingspur der Schwetzinger Kurpfalz Lichtbild GmbH. Körperliche Mastermedien, "
        "Lizenzforderungen und Film- sowie Nutzungsrechte wurden in getrennten Urkunden "
        "als Sicherheiten bezeichnet. Nach Insolvenzeröffnung hat die Verwalterin einen "
        "Asset Deal mit der Deidesheimer Weintor Streamworks GmbH unterzeichnet und die "
        "Übergabe des gesamten Filmpakets einschließlich Master und Kundenforderungen angekündigt."
    ),
    "scenario": (
        "Die Sicherheitennehmerin erhält am 22. Oktober 2026 eine heterogene Produktions-, "
        "Rechte- und Transaktionsakte. Neben einem LTO-Mastersatz und physischen Arbeitsplatten "
        "bestehen Cloud-Kopien, laufende Lizenzforderungen gegen Streamer und Sender sowie eine "
        "Rechtekette aus Drehbuch, Romanvorlage, Musik, Darstellerleistungen, Archivmaterial und "
        "Filmherstellerrechten. Der Kaufvertrag ist bereits unterzeichnet; Closing und technische "
        "Auslieferung sollen am 29. Oktober beginnen. Eine Freigabe der Bank liegt nach deren Akte "
        "nicht vor. Zu klären sind Rechtslage und rechtlich mögliche Reaktionen, ohne dass die "
        "Unterlagen selbst eine Lösung vorgeben."
    ),
    "parties": [
        {
            "name": "Palatina Medienbank AG",
            "role": "Darlehensgeberin und Sicherheitennehmerin",
            "address": "L 9, 11, 68161 Mannheim",
            "email": "workout@palatina-medienbank.example",
        },
        {
            "name": "Kurpfalz Lichtbild GmbH",
            "role": "Insolvenzschuldnerin und Filmproduzentin",
            "address": "Carl-Theodor-Straße 21, 68723 Schwetzingen",
            "email": "produktion@kurpfalz-lichtbild.example",
        },
        {
            "name": "Dr. Marlene Berthold",
            "role": "Insolvenzverwalterin über das Vermögen der Produzentin",
            "address": "Kanzlei Berthold & Heller, Kurfürsten-Anlage 34, 69115 Heidelberg",
            "email": "berthold@bh-insolvenz.example",
        },
        {
            "name": "Weintor Streamworks GmbH",
            "role": "Unterzeichnete Erwerberin des Filmpakets",
            "address": "Weinstraße 37, 67146 Deidesheim",
            "email": "closing@weintor-streamworks.example",
        },
        {
            "name": "Konrad Riemenschneider",
            "role": "Geschäftsführer und Produzent der Insolvenzschuldnerin",
            "address": "Friedrichstraße 18, 68723 Schwetzingen",
            "email": "riemenschneider@kurpfalz-lichtbild.example",
        },
        {
            "name": "Bettina Karg",
            "role": "Leiterin Spezialfinanzierungen der Palatina Medienbank AG",
            "address": "L 9, 11, 68161 Mannheim",
            "email": "bettina.karg@palatina-medienbank.example",
        },
        {
            "name": "Jonna Zobel",
            "role": "Drehbuchautorin und Bearbeiterin der Romanvorlage",
            "address": "Bergheimer Straße 72, 69115 Heidelberg",
            "email": "j.zobel@wortwerk-heidelberg.example",
        },
        {
            "name": "Dr. Alban Rösch",
            "role": "Urheber der Romanvorlage Reben im Nebel",
            "address": "Niederkircher Straße 8, 67146 Deidesheim",
            "email": "alban.roesch@autor.example",
        },
        {
            "name": "Mara Götz",
            "role": "Regisseurin",
            "address": "Seckenheimer Straße 46, 68165 Mannheim",
            "email": "mara@goetz-film.example",
        },
        {
            "name": "Rheinbild Mediathek GmbH",
            "role": "Lizenznehmerin für deutschsprachiges Streaming",
            "address": "Vangerowstraße 20, 69115 Heidelberg",
            "email": "rights@rheinbild-mediathek.example",
        },
    ],
    "questions": [
        "Welche körperlichen Datenträger, Geräte, Forderungen, urheberrechtlichen Nutzungsrechte, Filmherstellerrechte und sonstigen Rechte sind jeweils Gegenstand welcher Sicherheitenurkunde?",
        "Wie lässt sich die Rechtekette an Romanvorlage, Drehbuch, Regie, Darstellerleistungen, Filmmusik, Archivaufnahmen, Drohnenbildern, Standfotos und Endfassung anhand der Originalunterlagen rekonstruieren?",
        "Welche Unterschiede bestehen zwischen dem LTO-Mastersatz, den Arbeitsfestplatten, den Cloud-Kopien, den Forderungen aus Lizenzverträgen und den immateriellen Filmrechten?",
        "Welche Vermögenspositionen will der unterschriebene Asset Deal konkret übertragen, und welche Einschränkungen, Vollzugsvoraussetzungen oder Freistellungen enthält er?",
        "Welche Bedeutung haben die gesonderte Sicherungsabtretung der Lizenzforderungen, Zahlungsanzeigen an Lizenznehmer und Zahlungen auf das operative Konto für die Positionen der Beteiligten?",
        "Welche kurzfristigen gerichtlichen und außergerichtlichen Möglichkeiten sind vor der angekündigten Übergabe zu prüfen, und gegen wen wären Tatsachen, Verfügungen oder Unterlassungen zu adressieren?",
        "Welche Originaldateien, Metadaten, Datenträger, Kontobelege, Zustimmungen und Rechteerklärungen müssen vor Vollzug gesichert oder nachgefordert werden?",
        "Welche Auswirkungen können fehlende Zustimmungen, zeitlich oder territorial begrenzte Rechte, Rückrufklauseln und Musik- oder Archivlizenzen auf Verwertung und Kaufpreiszuordnung haben?",
        "Welche verhandlungsorientierten Lösungen kommen neben streitigen Maßnahmen in Betracht, ohne eine rechtliche Genehmigung oder Freigabe vorwegzunehmen?",
    ],
    "ambiguities": [
        "Die Datenträgerliste bezeichnet zwei LTO-Bänder als Final Master, während das Laborprotokoll eines davon als Sicherungskopie und die Cloud-Fassung als maßgeblichen Mezzanine Master ausweist.",
        "Die Sicherungsübereignungsanlage nennt Seriennummern von zwei RAID-Gehäusen, nicht aber einzelne darin ausgetauschte SSDs oder den Cloud-Speicher.",
        "Der IP-Sicherungsvertrag verwendet die Begriffe Filmrechte, Nutzungsrechte und Herstellerrechte nebeneinander, verweist aber auf eine nur teilweise ausgefüllte Anlage B.",
        "Die Romanoption wurde verlängert; der Verlängerungsnachtrag trägt nur eine eingescannte Unterschrift des Autors, während die Gegenzeichnung der Produzentin als separate PDF vorliegt.",
        "Der Drehbuchvertrag nennt weltweite Rechte für die Schutzdauer, eine spätere E-Mail der Autorin spricht dagegen von einer Beschränkung auf deutschsprachige Auswertungen.",
        "Für zwei historische Archivsequenzen liegt eine Lizenz bis 31. Dezember 2027 vor; der Asset Deal kalkuliert mit einer unbefristeten internationalen Bibliotheksauswertung.",
        "Die Komponistin räumte Rechte am Score ein; ein in der Festivalfassung verwendetes Jazzstück stammt von einem Dritten und erscheint nicht in Anlage 1 des Musikvertrags.",
        "Die Globalzession erfasst Lizenz-, Vertriebs- und Nebenforderungen, während die Debitorenliste einzelne Mindestgarantien als Kaufpreisbestandteil des Asset Deals ausweist.",
        "Rheinbild zahlte eine Rate nach Verfahrenseröffnung auf das operative Konto; die Buchhaltung ordnete sie dem zweiten Lizenzjahr zu, die Erwerberin bezeichnet sie als Closing Working Capital.",
        "Der APA nimmt Datenträger und Rechte als ein Filmpaket auf, verteilt den Kaufpreis intern aber auf Hardware, Rechtebibliothek und Forderungen.",
        "Die Closing-Checkliste bezeichnet eine Zustimmung der Bank als entbehrlich, während ein älterer Datenraumindex eine Freigabeerklärung als noch einzuholendes Dokument führt.",
        "Noch ist nicht belegt, ob der Erwerberin bereits Download-Token, Verschlüsselungsschlüssel oder physische LTO-Bänder übergeben wurden; angekündigt ist die technische Übergabe ab 29. Oktober 2026 um 09:00 Uhr.",
    ],
    "documents": [],
}


CASE["documents"].extend(
    [
        _mail(
            "01_Mandat/01_Anfrage_Palatina_Medienbank.eml",
            "Eilige Mandatsanfrage der Palatina Medienbank",
            sender="Bettina Karg <bettina.karg@palatina-medienbank.example>",
            to=["ip-insolvenz@kanzlei-kornmarkt.example"],
            cc=["vorstandsstab@palatina-medienbank.example"],
            date="Thu, 22 Oct 2026 07:52:00 +0200",
            subject="Eilig: Die letzte Rieslingspur – unterzeichneter Verkauf und Übergabe am 29.10.",
            body=(
                "Guten Morgen,\n\nwir haben die Produktion Die letzte Rieslingspur finanziert. "
                "Unsere Sicherheitendokumentation trennt körperliche Mastermedien, Lizenzforderungen "
                "und die Film- beziehungsweise Nutzungsrechte. Gestern Abend übersandte Frau Dr. "
                "Berthold einen bereits unterzeichneten Kaufvertrag mit Weintor Streamworks. Die "
                "technische Übergabe soll am 29. Oktober beginnen. Wir haben keine Freigabe erklärt.\n\n"
                "Bitte ordnen Sie die Unterlagen gegenstandsbezogen, rekonstruieren Sie die Rechtekette "
                "und prüfen Sie die Rechtslage sowie die noch rechtzeitig verfügbaren Handlungsoptionen. "
                "Wir benötigen außerdem eine Liste fehlender Originalnachweise. In der Akte liegen "
                "mehrere widersprüchliche Master- und Forderungslisten.\n\nMit freundlichen Grüßen\n"
                "Bettina Karg\nLeiterin Spezialfinanzierungen"
            ),
            attachments=[
                "04_Finanzierung_Sicherheiten/02_IP_Sicherungsvertrag_Filmrechte.docx",
                "04_Finanzierung_Sicherheiten/03_Sicherungsuebereignung_Mastermedien.pdf",
                "04_Finanzierung_Sicherheiten/04_Sicherungsabtretung_Lizenzforderungen.docx",
                "06_Insolvenz_AssetDeal/04_Asset_Purchase_Agreement_unterschrieben.docx",
            ],
        ),
        _doc(
            "01_Mandat/02_Interne_Fallnotiz_Bank.docx",
            "docx",
            "Interne Fallnotiz der Bank",
            sections=[
                _section(
                    "1. Anlass",
                    "Bearbeiterin: Bettina Karg. Stand: 22. Oktober 2026, 07:15 Uhr. Die Notiz dokumentiert den bankintern bekannten Sachstand; sie enthält keine rechtliche Bewertung.",
                    "Die Kurpfalz Lichtbild GmbH befindet sich seit 30. September 2026 im eröffneten Insolvenzverfahren. Die Verwalterin hat am 20. Oktober einen Vertrag über das Filmpaket unterzeichnet und am 21. Oktober den Vollzug angekündigt.",
                ),
                _section(
                    "2. Finanzierung und Dokumentensätze",
                    "Die Bank stellte 2024 eine Produktionslinie über 1.850.000 EUR und 2025 eine Fertigstellungstranche über 420.000 EUR bereit. Der Saldo laut Kreditbuch beträgt zum 30. September 2026 einschließlich Zinsen 1.476.830,44 EUR.",
                    "Im Sicherheitentresor liegen drei gesonderte Urkunden: IP-Sicherungsvertrag, Sicherungsübereignung von Mastermedien und Technik sowie Sicherungsabtretung von Lizenzforderungen. Ob alle Anlagen in der Schlussfassung gegengezeichnet wurden, ist offen.",
                ),
                _section(
                    "3. Produktionsstand",
                    "Der Film hatte am 12. März 2026 Festivalpremiere in Heidelberg. Eine Kinofassung, eine Festivalfassung und eine barrierefreie Fassung werden in den Listen unterschieden. Die Bank erhielt bislang keine forensische Kopie der Masterdateien.",
                    "Die laufende Auswertung erfolgt über Rheinbild Mediathek, Südwest-Fernsehkontor und Pfalzstern Filmverleih. Zahlungsanzeigen wurden nicht für alle Verträge bestätigt.",
                ),
                _section(
                    "4. Angekündigte Transaktion",
                    "Der APA nennt einen Gesamtkaufpreis von 1.180.000 EUR. Davon sollen laut Kaufpreisallokation 30.000 EUR auf Hardware und Datenträger, 910.000 EUR auf die Rechtebibliothek und 240.000 EUR auf ausgewählte Forderungen entfallen.",
                    "Die Erwerberin kündigt bereits eine Wiederveröffentlichung und internationale Untertitelung an. Der Bank ist weder eine Freigabeanforderung vor Signing noch ein belastbarer Vollzugsnachweis zugegangen.",
                ),
            ],
        ),
        _xlsx(
            "01_Mandat/03_Chronologie.xlsx",
            "Chronologie Produktion, Finanzierung und Insolvenz",
            [
                {
                    "name": "Chronologie",
                    "headers": ["Datum", "Vorgang", "Beteiligte", "Beleg", "Offener Punkt"],
                    "rows": [
                        ["06.02.2023", "Romanoption vereinbart", "Rösch / Kurpfalz Lichtbild", "03_Rechtekette_Vertraege/01_Option_Romanvorlage.docx", "Verlängerung und Reichweite"],
                        ["14.09.2023", "Drehbuchvertrag", "Zobel / Kurpfalz Lichtbild", "03_Rechtekette_Vertraege/03_Drehbuchvertrag_Jonna_Zobel.docx", "Widerspruch zur E-Mail vom 04.08.2025"],
                        ["18.04.2024", "Produktionsdarlehen", "Palatina / Kurpfalz Lichtbild", "04_Finanzierung_Sicherheiten/01_Produktionsdarlehen.pdf", "Fertigstellungstranche"],
                        ["19.04.2024", "IP-Sicherheit und Mastermedien", "Palatina / Kurpfalz Lichtbild", "04_Finanzierung_Sicherheiten/02_IP_Sicherungsvertrag_Filmrechte.docx", "Anlage B unvollständig"],
                        ["07.05.2024", "Drehbeginn Deidesheim", "Produktionsteam", "02_Produktion_Medien/02_Produktionsdossier.docx", "Rohmaterialbestand"],
                        ["22.11.2024", "Rohschnitt abgenommen", "Produzent / Regie", "Schnittprotokoll", "keine Originaldatei in Akte"],
                        ["21.02.2025", "Sicherungsabtretung Forderungen", "Palatina / Kurpfalz Lichtbild", "04_Finanzierung_Sicherheiten/04_Sicherungsabtretung_Lizenzforderungen.docx", "Anzeige an alle Debitoren?"],
                        ["04.08.2025", "Autorin beanstandet Verwertungsumfang", "Zobel / Produktion", "03_Rechtekette_Vertraege/09_Mail_Autorin_Rechteumfang.eml", "Einordnung der Korrespondenz"],
                        ["12.03.2026", "Festivalpremiere Heidelberg", "Produktion / Publikum", "Presseunterlagen", "verwendete Filmfassung"],
                        ["18.08.2026", "Zahlungsstockung angezeigt", "Produktion / Bank", "Bankakte", "vollständige Liquiditätsdaten"],
                        ["30.09.2026", "Insolvenzverfahren eröffnet", "AG Heidelberg / Dr. Berthold", "06_Insolvenz_AssetDeal/01_Insolvenzeroeffnungsbeschluss.pdf", "Rechtskraftvermerk"],
                        ["14.10.2026", "Bewertung Filmpaket", "Neckarblick Valuation", "06_Insolvenz_AssetDeal/03_Bewertung_Filmpaket.pdf", "Rechteannahmen"],
                        ["20.10.2026", "APA unterzeichnet", "Verwalterin / Weintor", "06_Insolvenz_AssetDeal/04_Asset_Purchase_Agreement_unterschrieben.docx", "Verfügungs- und Zustimmungslage"],
                        ["21.10.2026", "Vollzug Bank angekündigt", "Dr. Berthold / Palatina", "06_Insolvenz_AssetDeal/06_Mail_Verwalterin_Vollzugsankuendigung.eml", "Bankreaktion offen"],
                        ["29.10.2026", "technische Übergabe geplant", "Verwalterin / Erwerberin", "06_Insolvenz_AssetDeal/05_Closing_Checkliste.xlsx", "Token, Master und Forderungslisten"],
                    ],
                },
                {
                    "name": "Termine",
                    "headers": ["Datum", "Uhrzeit", "Anlass", "Teilnehmer", "Status"],
                    "rows": [
                        ["23.10.2026", "15:30", "Datenraumfragen bündeln", "Bank und externe Beratung", "intern vorgesehen"],
                        ["26.10.2026", "11:00", "Closing-Vorbereitung", "Verwalterin und Erwerberin", "laut Checkliste"],
                        ["28.10.2026", "16:00", "Verschlüsselungsschlüssel prüfen", "Labor und Erwerberin", "angefragt"],
                        ["29.10.2026", "09:00", "Übergabe Master und Datenraum", "Verwalterin und Erwerberin", "angekündigt"],
                        ["29.10.2026", "14:00", "Kaufpreiszahlung", "Erwerberin", "vertraglich vorgesehen"],
                    ],
                },
            ],
        ),
        _xlsx(
            "01_Mandat/04_Beteiligte_Kontakte.xlsx",
            "Beteiligte und Kommunikationswege",
            [
                {
                    "name": "Beteiligte",
                    "headers": ["Organisation", "Person", "Rolle", "Ort", "E-Mail", "Letzter Kontakt"],
                    "rows": [
                        ["Palatina Medienbank AG", "Bettina Karg", "Spezialfinanzierungen", "Mannheim", "bettina.karg@palatina-medienbank.example", "22.10.2026"],
                        ["Kurpfalz Lichtbild GmbH", "Konrad Riemenschneider", "Produzent", "Schwetzingen", "riemenschneider@kurpfalz-lichtbild.example", "05.10.2026"],
                        ["Berthold & Heller", "Dr. Marlene Berthold", "Insolvenzverwalterin", "Heidelberg", "berthold@bh-insolvenz.example", "21.10.2026"],
                        ["Weintor Streamworks GmbH", "Vincent Bundschuh", "Geschäftsführer", "Deidesheim", "bundschuh@weintor-streamworks.example", "21.10.2026"],
                        ["Wortwerk Heidelberg", "Jonna Zobel", "Drehbuch", "Heidelberg", "j.zobel@wortwerk-heidelberg.example", "04.08.2025"],
                        ["Rösch Autorenbüro", "Dr. Alban Rösch", "Romanvorlage", "Deidesheim", "alban.roesch@autor.example", "13.02.2025"],
                        ["Rheinbild Mediathek GmbH", "Saskia Thoma", "Lizenznehmerin", "Heidelberg", "rights@rheinbild-mediathek.example", "09.10.2026"],
                        ["Komet Postproduction GmbH", "Nils Emmerling", "Postproduktion", "Mannheim", "mastering@komet-post.example", "19.10.2026"],
                    ],
                },
                {
                    "name": "Kommunikation",
                    "headers": ["Thema", "Primärkontakt", "Vertretung", "Kanal", "Hinweis"],
                    "rows": [
                        ["Sicherheiten", "Bettina Karg", "Hanno Seubert", "Bankdatenraum", "Originalurkunden im Tresor Mannheim"],
                        ["Insolvenzakte", "Dr. Marlene Berthold", "RA Pia Hofmeister", "Berthold-Datenraum", "Fragen gesammelt einreichen"],
                        ["Mastermedien", "Nils Emmerling", "Selma Heinrich", "verschlüsselte Transferplattform", "physische Lagerung getrennt prüfen"],
                        ["Rechtekette", "Konrad Riemenschneider", "Jonna Zobel", "Produktionsarchiv", "mehrere Anlagen nur als Scan"],
                        ["Closing", "Pia Hofmeister", "Vincent Bundschuh", "Videokonferenz", "29.10.2026"],
                    ],
                },
            ],
        ),
        _doc(
            "02_Produktion_Medien/01_Unternehmensprofil_und_Filmografie.pdf",
            "pdf",
            "Unternehmensprofil und Filmografie",
            sections=[
                _section(
                    "1. Gesellschaft",
                    "Die Kurpfalz Lichtbild GmbH wurde 2016 gegründet und produziert Spiel- und Dokumentarfilme mit regionalem Stoffbezug. Sitz und Produktionsbüro befinden sich in Schwetzingen. Geschäftsführer ist Konrad Riemenschneider.",
                    "Zum Bestand gehören drei fertiggestellte Kurzfilme, der Dokumentarfilm Neckarbogen bei Nacht und der 104-minütige Spielfilm Die letzte Rieslingspur. Letzterer ist der einzige Titel mit laufenden internationalen Vertriebsanfragen.",
                ),
                _section(
                    "2. Film Die letzte Rieslingspur",
                    "Der Film erzählt von einer Heidelberger Restauratorin, die in Deidesheim eine verschollene Tonaufnahme und ein familiäres Geheimnis sucht. Drehorte waren Deidesheim, Schwetzingen, Heidelberg und Mannheim.",
                    "Produktion: Kurpfalz Lichtbild GmbH. Regie: Mara Götz. Drehbuch: Jonna Zobel nach Motiven des Romans Reben im Nebel von Dr. Alban Rösch. Musik: Livia Scheuerlein. Bildgestaltung: Pascal Nowak.",
                ),
                _section(
                    "3. Fassungen",
                    "Dokumentiert sind eine Kinofassung mit 104 Minuten, eine Festivalfassung mit 108 Minuten, eine barrierefreie deutsche Fassung und ein internationaler Mezzanine Master ohne eingebrannte Untertitel.",
                    "Nicht abschließend geklärt ist, welche Musik- und Archivsequenzen in den jeweiligen Fassungen enthalten sind und welche Fassung dem Streamer übergeben wurde.",
                ),
            ],
        ),
        _doc(
            "02_Produktion_Medien/02_Produktionsdossier.docx",
            "docx",
            "Produktionsdossier Die letzte Rieslingspur",
            sections=[
                _section(
                    "1. Produktionsdaten",
                    "Arbeitstitel: Rieslingnacht. Finaler Titel: Die letzte Rieslingspur. Herstellungszeitraum: Februar 2023 bis März 2026. Hauptdreh: 7. Mai bis 28. Juni 2024. Nachdrehs: 17. und 18. Oktober 2024.",
                    "Herstellungsbudget laut Abschlusskalkulation: 3.480.600 EUR. Finanzierungsbestandteile: Bankdarlehen, regionale Filmförderung, Eigenmittel, Mindestgarantien von Verleih und Streamer sowie ein Koproduktionsbeitrag.",
                ),
                _section(
                    "2. Produktionsworkflow",
                    "Kamerarohdaten wurden täglich auf zwei Shuttle-SSDs und ein Arbeits-RAID kopiert. Nach Bildsperre erzeugte Komet Postproduction ein DCP, ProRes-Mezzanine, IMF-Paket und zwei LTO-9-Sicherungen.",
                    "Das Produktionsbüro erhielt LTO-KL-001 und das RAID-Gehäuse KL-RAID-02. Komet Postproduction verwahrte LTO-KL-002 zunächst als Sicherheitsexemplar. Ein verschlüsseltes IMF-Paket liegt zusätzlich im Cloud-Bucket kurpfalz-master-prod.",
                ),
                _section(
                    "3. Rechteunterlagen",
                    "Die Produktionsleitung führte eine Rechtecheckliste. Genannt werden Romanoption, Drehbuch, Regie, Haupt- und Nebendarsteller, Musik, Archivmaterial, Kunstwerke im Bild, Drehgenehmigungen, Standfoto und Drohnenaufnahme.",
                    "Im Abschlussordner fehlen nach Vermerk vom 9. Februar 2026 die Originalfreigabe des Jazz-Trios, eine gegengezeichnete Anlage B zum IP-Sicherungsvertrag und die Langfassung des Drohnenvertrags.",
                ),
                _section(
                    "4. Vertrieb",
                    "Pfalzstern Filmverleih übernahm den deutschen Kinoverleih. Rheinbild Mediathek erhielt ein deutschsprachiges Streamingfenster. Südwest-Fernsehkontor erwarb zwei lineare Ausstrahlungen. Weitere Gebiete wurden auf Märkten angeboten, aber noch nicht verbindlich lizenziert.",
                ),
            ],
        ),
        _xlsx(
            "02_Produktion_Medien/03_Medien_und_Geraeteinventar.xlsx",
            "Medien- und Geräteinventar",
            [
                {
                    "name": "Physische_Medien",
                    "headers": ["ID", "Gegenstand", "Seriennummer", "Inhalt", "Lagerort", "Besitz am 20.10.2026", "Urkunde"],
                    "rows": [
                        ["KL-LTO-001", "LTO-9-Band", "L9P-773418", "IMF, ProRes, Audio-Stems", "Schwetzingen, Tresor 2", "Verwalterin", "Sicherungsübereignung Anlage 1"],
                        ["KL-LTO-002", "LTO-9-Band", "L9P-773419", "Backup laut Labor", "Komet Postproduction Mannheim", "Komet", "Sicherungsübereignung Anlage 1"],
                        ["KL-RAID-02", "RAID-Gehäuse", "R6-88201", "Schnittprojekt und Exporte", "Schwetzingen, Technikraum", "Verwalterin", "Sicherungsübereignung Anlage 1"],
                        ["KL-SSD-A", "Shuttle-SSD", "SSDX-00411", "Drehtag 1 bis 26", "unbekannt", "unklar", "nicht in Anlage"],
                        ["KL-SSD-B", "Shuttle-SSD", "SSDX-00412", "Drehtag 27 bis 41", "Regiearchiv Mannheim", "Mara Götz", "nicht in Anlage"],
                        ["KL-DCP-01", "verschlüsselte DCP-Festplatte", "DCP-14018", "Kinofassung", "Pfalzstern Lager Mannheim", "Pfalzstern", "Leihprotokoll"],
                    ],
                },
                {
                    "name": "Nichtkoerperliche_Kopien",
                    "headers": ["Bezeichnung", "Plattform", "Account", "Format", "Schlüsselinhaber", "Stand"],
                    "rows": [
                        ["kurpfalz-master-prod", "CloudVault EU", "Kurpfalz Lichtbild", "IMF", "Verwalterteam und Komet", "18.10.2026"],
                        ["Rheinbild Delivery", "Aspera", "Rheinbild", "ProRes + Untertitel", "Rheinbild", "03.04.2026"],
                        ["Festival Screener", "ScreenPass", "Produktion", "H.264", "Verwalterteam", "30.09.2026"],
                        ["Audio Sessions", "StudioCloud", "Scheuerlein Musik", "WAV / DAW", "Komponistin", "15.01.2026"],
                    ],
                },
                {
                    "name": "Pruefpunkte",
                    "headers": ["Thema", "Quelle A", "Quelle B", "Abweichung"],
                    "rows": [
                        ["Final Master", "Inventar: KL-LTO-001", "Labor: Cloud-IMF maßgeblich", "Masterbegriff uneinheitlich"],
                        ["LTO-KL-002", "Anlage: Sicherungseigentum", "Komet: Zurückbehalt bis Rechnung", "Besitz und Herausgabe offen"],
                        ["RAID-Inhalt", "Produktion: vollständig", "Labor: Proxy-Dateien fehlen", "Integrität ungeklärt"],
                        ["Cloudzugang", "Checkliste: zu übertragen", "Sicherheitenurkunde: nicht benannt", "rechtliche Zuordnung offen"],
                    ],
                },
            ],
        ),
        _doc(
            "02_Produktion_Medien/04_Laborprotokoll_Mastering.pdf",
            "pdf",
            "Laborprotokoll Mastering und Archivierung",
            sections=[
                _section(
                    "1. Auftrag",
                    "Auftraggeberin: Kurpfalz Lichtbild GmbH. Dienstleisterin: Komet Postproduction GmbH, Mannheim. Projekt: KLP-2417. Abschluss des Masterings: 16. Februar 2026.",
                    "Eingangsmaterial: 6K-Kamerarohdaten, Schnittprojekt Version 53, deutsche und internationale Tonmischung, Untertiteldateien, Audiodeskription und Musik-Stems.",
                ),
                _section(
                    "2. Ausgaben",
                    "Erzeugt wurden DCP Kinofassung 104:12, DCP Festivalfassung 108:04, IMF-App-2E-Paket, ProRes 4444 XQ, M&E-Tonspur, deutsche Untertitel und barrierefreie Zusatzfassungen.",
                    "Der technische Referenzmaster ist nach Laborworkflow das verschlüsselte IMF-Paket im CloudVault-Bucket. LTO-KL-001 enthält eine vollständige Exportkopie. LTO-KL-002 wurde als zweite Sicherung geschrieben und verbleibt bis zum schriftlichen Auslagerungsauftrag im klimatisierten Archiv der Komet Postproduction GmbH.",
                ),
                _section(
                    "3. Prüfsummen und Schlüssel",
                    "Für das IMF-Paket wurde die Prüfsummenliste KLP-2417-HASH.csv erstellt. Die Schlüsseldatei liegt im Passworttresor des Produktionsaccounts; der zweite Wiederherstellungsschlüssel wurde dem technischen Leiter der Produktion in einem versiegelten Umschlag übergeben.",
                    "Die in der Akte vorliegende Kopie des Protokolls enthält die Prüfsummenliste nicht. Auch der Empfang des versiegelten Umschlags ist nicht quittiert.",
                ),
            ],
        ),
        _csv(
            "02_Produktion_Medien/05_Datei_und_Masterregister.csv",
            "Datei- und Masterregister",
            ["Asset-ID", "Dateiname", "Format", "Laufzeit", "Speicherort", "Hashstatus", "Bemerkung"],
            [
                ["M-001", "Rieslingspur_Kino_DE_v53.mxf", "MXF/IMF", "104:12", "CloudVault", "laut Labor geprüft", "Referenzmaster"],
                ["M-002", "Rieslingspur_Festival_v41.mxf", "MXF", "108:04", "LTO-KL-001", "Liste fehlt", "Jazzszene enthalten"],
                ["M-003", "Rieslingspur_INTL_clean_v53.mov", "ProRes 4444 XQ", "104:12", "LTO-KL-001", "laut Labor geprüft", "ohne Titelkarten"],
                ["M-004", "Rieslingspur_MandE_51.wav", "WAV", "104:12", "StudioCloud/LTO", "unbekannt", "internationale Mischung"],
                ["M-005", "Rieslingspur_DE_AD.wav", "WAV", "104:12", "CloudVault", "laut Labor geprüft", "Audiodeskription"],
                ["M-006", "Rieslingspur_DE_HOH.srt", "SRT", "104:12", "CloudVault", "n/a", "Untertitel"],
                ["M-007", "DCP_Kino_SMPTE", "DCP", "104:12", "DCP-Festplatte/Pfalzstern", "KDM-bezogen", "verschlüsselt"],
                ["M-008", "Schnittprojekt_v53", "DaVinci Projekt", "n/a", "KL-RAID-02", "nicht dokumentiert", "Proxy-Verknüpfungen prüfen"],
            ],
        ),
        _doc(
            "03_Rechtekette_Vertraege/01_Option_Romanvorlage.docx",
            "docx",
            "Options- und Verfilmungsvertrag Romanvorlage",
            sections=[
                _section(
                    "1. Parteien und Werk",
                    "Zwischen Dr. Alban Rösch, Deidesheim, als Autor und der Kurpfalz Lichtbild GmbH, Schwetzingen, als Produzentin wird am 6. Februar 2023 eine Option an dem Roman Reben im Nebel vereinbart.",
                    "Der Autor versichert, über die für die vereinbarte Nutzung erforderlichen Rechte am Romantext zu verfügen. Ausgenommen sind die separat verlegten Hörbuchrechte.",
                ),
                _section(
                    "2. Option",
                    "Die Produzentin erhält bis 31. Januar 2024 das ausschließliche Recht, die Verfilmungsrechte nach Maßgabe dieses Vertrags auszuüben. Die Option kann einmal gegen Zahlung von 7.500 EUR um zwölf Monate verlängert werden.",
                    "Die Ausübung bedarf einer eindeutigen Erklärung in Textform und der Gutschrift der ersten Kaufpreisrate. Der vorliegenden Vertragskopie ist weder eine Ausübungserklärung noch ein Kontoauszug beigefügt.",
                ),
                _section(
                    "3. Rechte bei Ausübung",
                    "Nach wirksamer Ausübung räumt der Autor für die Dauer der gesetzlichen Schutzfrist ausschließliche Rechte zur Herstellung und weltweiten Auswertung eines abendfüllenden Spielfilms ein. Bühnen-, Hörbuch- und eigenständige Serienrechte bleiben beim Autor.",
                    "Fortsetzungen und Remakes bedürfen einer gesonderten Vereinbarung. Der Autor erhält eine Titel- und Namensnennung sowie eine erfolgsabhängige Beteiligung nach Erreichen definierter Nettoerlöse.",
                ),
                _section(
                    "4. Übertragung und Sicherung",
                    "Die Produzentin darf die eingeräumten Rechte im Rahmen der Finanzierung zur Sicherheit übertragen und im Rahmen einer Veräußerung des Filmprojekts auf einen branchenerfahrenen Erwerber übertragen. Der Autor ist hierüber vor Vollzug in Textform zu unterrichten.",
                    "Eine Entbindung der Produzentin von offenen Abrechnungs- und Beteiligungspflichten ist mit einer Übertragung nicht verbunden.",
                ),
                _section(
                    "5. Unterschriften",
                    "Deidesheim, 6. Februar 2023 — Dr. Alban Rösch, handschriftlich unterzeichnet.",
                    "Schwetzingen, 6. Februar 2023 — Kurpfalz Lichtbild GmbH, Konrad Riemenschneider, handschriftlich unterzeichnet.",
                ),
            ],
        ),
        _doc(
            "03_Rechtekette_Vertraege/02_Nachtrag_Romanoption.pdf",
            "pdf",
            "Nachtrag zur Romanoption",
            sections=[
                _section(
                    "1. Bezug",
                    "Der Nachtrag vom 22. Januar 2024 bezieht sich auf den Vertrag vom 6. Februar 2023. Die Optionsfrist soll bis 31. Januar 2025 verlängert werden. Als Verlängerungsentgelt sind 7.500 EUR ausgewiesen.",
                ),
                _section(
                    "2. Dokumentenstand",
                    "Die vorliegende Datei enthält auf Seite 2 eine eingefügte Bildsignatur mit dem Namen Dr. Alban Rösch und dem Datum 22. Januar 2024. Eine qualifizierte elektronische Signatur ist in der PDF nicht ausgewiesen.",
                    "Eine separate Gegenzeichnungsseite der Kurpfalz Lichtbild GmbH vom 24. Januar 2024 befindet sich im Datenraum. Aus der Datei ist nicht erkennbar, ob beide Seiten dieselbe Fassung erhalten haben.",
                ),
                _section(
                    "3. Ergänzung",
                    "Im Übrigen sollen alle Bestimmungen des Options- und Verfilmungsvertrags unverändert fortgelten. Insbesondere werden keine eigenständigen Serien-, Fortsetzungs- oder Remakerechte ergänzt.",
                ),
            ],
        ),
        _doc(
            "03_Rechtekette_Vertraege/03_Drehbuchvertrag_Jonna_Zobel.docx",
            "docx",
            "Drehbuchvertrag Jonna Zobel",
            sections=[
                _section(
                    "1. Auftrag",
                    "Die Kurpfalz Lichtbild GmbH beauftragt Jonna Zobel am 14. September 2023 mit Exposé, Treatment und drei Drehbuchfassungen für den Spielfilm Die letzte Rieslingspur nach Motiven des Romans Reben im Nebel.",
                    "Das Gesamthonorar beträgt 82.000 EUR zuzüglich Umsatzsteuer und wird in fünf werkbezogenen Raten gezahlt. Eine Schlussrate von 8.200 EUR ist laut Buchhaltung offen.",
                ),
                _section(
                    "2. Rechtseinräumung",
                    "Die Autorin räumt der Produzentin an den vertragsgemäß geschaffenen Fassungen ausschließliche, räumlich unbeschränkte und für die Dauer der gesetzlichen Schutzfrist bestehende Nutzungsrechte für Herstellung, Bearbeitung, Vervielfältigung, Verbreitung, Vorführung, Sendung, Abruf, Werbung, Synchronisation und Untertitelung des Films ein.",
                    "Nicht umfasst sind eine eigenständige Bühnenfassung und eine Veröffentlichung des Drehbuchs als Buch vor Ablauf von zwei Jahren nach Kinostart. Änderungen, welche die Grundaussage des Werks wesentlich entstellen, sollen vorher mit der Autorin besprochen werden.",
                ),
                _section(
                    "3. Weiterübertragung und Sicherheiten",
                    "Die Produzentin darf die vertragsgegenständlichen Rechte auf Koproduzenten, Verleiher, Sender, Plattformen und Finanzierer übertragen oder Unterrechte einräumen, soweit dies der Herstellung, Finanzierung oder Auswertung des Films dient.",
                    "Die Autorin soll von einer vollständigen Übertragung des Filmprojekts auf einen Dritten unterrichtet werden. Offene Honoraransprüche bleiben gegen die Produzentin bestehen, soweit nicht ausdrücklich etwas anderes vereinbart wird.",
                ),
                _section(
                    "4. Vorbestehende Beiträge",
                    "Die Autorin weist darauf hin, dass einzelne Dialogskizzen aus ihrem unveröffentlichten Kurztext Der Keller unter den Reben übernommen werden. Nach ihrer Erklärung ist sie alleinige Rechteinhaberin dieses Textes.",
                    "Die Anlage 2 soll die übernommenen Passagen kennzeichnen. In der vorliegenden Vertragsfassung ist Anlage 2 mit der Überschrift versehen, enthält aber keine Passagenliste.",
                ),
                _section(
                    "5. Unterschriften",
                    "Heidelberg, 14. September 2023 — Jonna Zobel, handschriftlich unterzeichnet.",
                    "Schwetzingen, 15. September 2023 — Kurpfalz Lichtbild GmbH, Konrad Riemenschneider, handschriftlich unterzeichnet.",
                ),
            ],
        ),
        _doc(
            "03_Rechtekette_Vertraege/04_Regievertrag_Mara_Goetz.docx",
            "docx",
            "Regievertrag Mara Götz",
            sections=[
                _section(
                    "1. Leistung",
                    "Mara Götz übernimmt Regievorbereitung, Dreharbeiten, Rohschnittabnahme und künstlerische Endabnahme des Films. Das Pauschalhonorar beträgt 145.000 EUR zuzüglich Umsatzsteuer.",
                    "Die Regisseurin arbeitet selbstständig und organisiert ihre Tätigkeit im Rahmen von Drehplan, Budget und Sicherheitsvorgaben. Die Produzentin stellt Produktionsmittel und Team.",
                ),
                _section(
                    "2. Rechte",
                    "Soweit durch die Regieleistung urheberrechtlich geschützte Beiträge entstehen, räumt die Regisseurin der Produzentin ausschließliche, räumlich und zeitlich unbeschränkte Nutzungsrechte zur Herstellung und Auswertung des Films in allen bekannten Nutzungsarten ein.",
                    "Die Produzentin darf Rechte im Zusammenhang mit Finanzierung und Verwertung weiterübertragen. Die Regisseurin behält das Recht auf Namensnennung und erhält eine Konsultationsmöglichkeit bei wesentlichen nachträglichen Kürzungen.",
                ),
                _section(
                    "3. Materialien und private Arbeitskopie",
                    "Arbeitsmaterialien sind nach Produktionsende herauszugeben. Eine verschlüsselte private Arbeitskopie darf ausschließlich zu Archiv- und Bewerbungszwecken aufbewahrt werden und nicht ohne vorherige Freigabe öffentlich zugänglich gemacht werden.",
                    "Die Produktionsakte nennt eine Shuttle-SSD im Regiearchiv; ein gesondertes Übergabe- oder Löschprotokoll liegt nicht bei.",
                ),
                _section(
                    "4. Unterschriften",
                    "Mannheim, 12. Februar 2024 — Mara Götz, handschriftlich unterzeichnet.",
                    "Schwetzingen, 13. Februar 2024 — Kurpfalz Lichtbild GmbH, Konrad Riemenschneider, handschriftlich unterzeichnet.",
                ),
            ],
        ),
        _doc(
            "03_Rechtekette_Vertraege/05_Filmmusikvertrag_Livia_Scheuerlein.docx",
            "docx",
            "Kompositions- und Filmmusikvertrag",
            sections=[
                _section(
                    "1. Kompositionsauftrag",
                    "Die Komponistin Livia Scheuerlein schafft einen Originalscore von voraussichtlich 42 Minuten, liefert Partitur, Stereo- und Mehrkanalmischungen sowie getrennte Stems. Honorar: 68.000 EUR zuzüglich Umsatzsteuer.",
                    "Die Einspielung erfolgt mit dem Pfälzer Kammerensemble. Rechte der ausübenden Musiker sollen nach einem gesonderten Ensemblevertrag geklärt werden; dieser ist im Datenraum nicht enthalten.",
                ),
                _section(
                    "2. Rechtseinräumung",
                    "Die Komponistin räumt der Produzentin ausschließliche Synchronisations- und filmbezogene Nutzungsrechte am Originalscore für weltweite und zeitlich unbeschränkte Auswertung des Films ein. Die isolierte Tonträgerauswertung bedarf einer gesonderten Zustimmung.",
                    "Soweit Wahrnehmungsverträge mit einer Verwertungsgesellschaft entgegenstehen, bleiben deren Rechte und Vergütungsansprüche unberührt. Cue-Sheet und Werknummern sind nachzuliefern.",
                ),
                _section(
                    "3. Fremdmusik",
                    "Nicht Gegenstand dieses Vertrags sind vorbestehende Musikwerke und die im Club-Motiv erwogene Aufnahme Abendzug des Trios Blauglas. Deren Nutzung ist von der Produzentin gesondert zu klären.",
                    "Die Festivalfassung enthält laut Schnittliste 78 Sekunden Abendzug. Für die Kinofassung ist in der Musikliste ein Ersatzscore vermerkt; die Masterregister unterscheiden dies nicht durchgängig.",
                ),
                _section(
                    "4. Unterschriften",
                    "Heidelberg, 9. Juli 2024 — Livia Scheuerlein, handschriftlich unterzeichnet.",
                    "Schwetzingen, 10. Juli 2024 — Kurpfalz Lichtbild GmbH, Konrad Riemenschneider, handschriftlich unterzeichnet.",
                ),
            ],
        ),
        _doc(
            "03_Rechtekette_Vertraege/06_Darsteller_und_Nebenrechte.pdf",
            "pdf",
            "Darsteller- und Nebenrechteübersicht",
            sections=[
                _section(
                    "1. Hauptrollen",
                    "Nele Hassan spielt die Restauratorin Miriam Velten. Vertrag vom 3. März 2024: 24 Drehtage, Pauschalgage 96.000 EUR, filmbezogene Nutzungsrechte für alle bekannten Nutzungsarten, gesonderte Zustimmung für digitale Nachbildung der Stimme.",
                    "Matthias von Scherenberg spielt Winzer Friedrich Auer. Vertrag vom 5. März 2024: 18 Drehtage, Pauschalgage 58.500 EUR, vergleichbare Nutzungsrechte; eine Option für Fortsetzungen ist nicht ausgefüllt.",
                ),
                _section(
                    "2. Nebenrollen und Komparserie",
                    "Für sieben Nebenrollen liegen unterschriebene Einzelverträge vor. Die Komparsenagentur RheinCasting bestätigte pauschal die Einholung von Einwilligungen; Einzelbelege für zwei Weinfest-Szenen sind in der gelieferten Datei nicht enthalten.",
                ),
                _section(
                    "3. Zusätzliche Leistungen",
                    "Für Audiodeskription und deutsche Untertitel bestehen Werkverträge mit TextBarriere Heidelberg. Der Einsatz eines synthetischen Stimmen-Doubles wurde intern diskutiert, nach Produktionsvermerk aber nicht umgesetzt.",
                    "Die Erwerberin fragt in der Due-Diligence-Liste nach Rechten für Trailer-Neuschnitt und KI-gestützte Synchronfassung. Eine ausdrückliche Freigabe dieser Nutzung ist in der Übersicht nicht vermerkt.",
                ),
            ],
        ),
        _doc(
            "03_Rechtekette_Vertraege/07_Archiv_und_Drohnenlizenzen.pdf",
            "pdf",
            "Archiv- und Drohnenlizenzen",
            sections=[
                _section(
                    "1. Historische Filmaufnahmen",
                    "Das Stadtarchiv Deidesheim gestattet die Nutzung der Sequenz Weinlese 1964 für den Film, Trailer und Pressearbeit in Deutschland, Österreich und der Schweiz bis 31. Dezember 2027. Laufzeitverlängerung und weltweite Plattformauswertung sind nicht enthalten.",
                    "Das Rhein-Neckar-Filmarchiv gestattet die Nutzung von 34 Sekunden Bahnhof Heidelberg 1978 weltweit bis 31. Dezember 2027. Für eine weitere Nutzung ist ein neues Lizenzentgelt vorgesehen.",
                ),
                _section(
                    "2. Drohnenaufnahmen",
                    "Die Firma Pfalzflug Media übergab am 19. Juni 2024 fünf Luftbildsequenzen. Das vorliegende Deal Memo nennt ein einfaches, weltweites Recht für den Film und dessen Werbung. Die angekündigte Langfassung mit Regelungen zu Rohmaterial und Weiterübertragung fehlt.",
                    "Die Rohdaten liegen nach Inventar bei Pfalzflug Media; im Master enthalten sind nur die final verwendeten Einstellungen.",
                ),
                _section(
                    "3. Standfotos",
                    "Fotografin Bea Kandel räumte Rechte an 85 freigegebenen Standfotos für Werbung, Festivals, Presse und Plattformdarstellung ein. Merchandising ist ausgeschlossen. In der Kaufvertragsanlage werden Standfotos ohne diese Einschränkung als Teil des Filmpakets aufgeführt.",
                ),
            ],
        ),
        _xlsx(
            "03_Rechtekette_Vertraege/08_Rechtekettenmatrix.xlsx",
            "Rechtekettenmatrix Filmprojekt",
            [
                {
                    "name": "Rechtekette",
                    "headers": ["Beitrag", "Rechtegeber", "Dokument", "Territorium", "Laufzeit", "Übertragung/Sicherung", "Offener Punkt"],
                    "rows": [
                        ["Romanvorlage", "Dr. Alban Rösch", "Option 06.02.2023 + Nachtrag", "weltweit laut Hauptvertrag", "Schutzdauer bei Ausübung", "Sicherung erlaubt; Erwerberinformation", "Ausübung und Verlängerung belegen"],
                        ["Drehbuch", "Jonna Zobel", "Vertrag 14.09.2023", "weltweit", "Schutzdauer", "Finanzierer/Erwerber genannt", "Anlage 2 leer; E-Mail widerspricht"],
                        ["Regie", "Mara Götz", "Vertrag 12.02.2024", "weltweit", "Schutzdauer", "Finanzierung/Verwertung genannt", "private SSD"],
                        ["Originalscore", "Livia Scheuerlein", "Vertrag 09.07.2024", "weltweit", "unbeschränkt filmbezogen", "filmbezogen weiterübertragbar", "Ensemblevertrag/Cue-Sheet"],
                        ["Jazzstück Abendzug", "Trio Blauglas", "kein Vertrag in Akte", "unbekannt", "unbekannt", "unbekannt", "Festivalfassung betroffen"],
                        ["Hauptdarsteller", "Hassan/Scherenberg", "Verträge März 2024", "weltweit", "Schutzdauer/vertraglich", "Filmverwertung", "digitale Bearbeitung begrenzt"],
                        ["Archiv Deidesheim", "Stadtarchiv", "Lizenz 18.04.2024", "D/A/CH", "bis 31.12.2027", "keine klare Weiterübertragung", "internationale Nutzung"],
                        ["Archiv Heidelberg", "Rhein-Neckar-Filmarchiv", "Lizenz 22.04.2024", "weltweit", "bis 31.12.2027", "projektbezogen", "Verlängerung"],
                        ["Drohnenbilder", "Pfalzflug Media", "Deal Memo", "weltweit", "unbekannt", "filmbezogen", "Langvertrag fehlt"],
                        ["Standfotos", "Bea Kandel", "Freigabe 03.08.2024", "weltweit", "fünfzehn Jahre", "kein Merchandising", "APA-Anlage weiter"],
                        ["Filmherstellerleistung", "Kurpfalz Lichtbild", "Produktionsakten", "nicht anwendbar", "gesetzlich/vertraglich", "IP-Sicherungsvertrag", "genaue Reichweite Anlage B"],
                    ],
                },
                {
                    "name": "Fassungen",
                    "headers": ["Fassung", "Laufzeit", "Musik", "Archiv", "Ausgeliefert an", "Klärung"],
                    "rows": [
                        ["Kinofassung v53", "104:12", "Ersatzscore", "beide Archive", "Pfalzstern", "Archivlizenzen 2027"],
                        ["Festivalfassung v41", "108:04", "Abendzug enthalten", "beide Archive", "Festivals", "Fremdmusik"],
                        ["Rheinbild Stream v53s", "103:48", "Ersatzscore", "Deidesheim-Sequenz gekürzt", "Rheinbild", "Abweichung zu Masterliste"],
                        ["International clean", "104:12", "M&E", "beide Archive", "noch nicht verbindlich", "weltweite Archivlizenz"],
                    ],
                },
            ],
        ),
        _mail(
            "03_Rechtekette_Vertraege/09_Mail_Autorin_Rechteumfang.eml",
            "Korrespondenz der Drehbuchautorin zum Rechteumfang",
            sender="Jonna Zobel <j.zobel@wortwerk-heidelberg.example>",
            to=["Konrad Riemenschneider <riemenschneider@kurpfalz-lichtbild.example>"],
            cc=["Mara Götz <mara@goetz-film.example>"],
            date="Mon, 4 Aug 2025 10:26:00 +0200",
            subject="Rieslingspur – internationale Fassung und mein Kurztext",
            body=(
                "Lieber Konrad,\n\nbei unserem Gespräch hatte ich verstanden, dass zunächst eine "
                "deutschsprachige Auswertung geplant ist. Nun lese ich in den Vertriebsunterlagen "
                "von weltweiten Fassungen und möglicher Serienentwicklung. Bitte bestätige mir, dass "
                "mein Kurztext Der Keller unter den Reben nicht außerhalb des Kinofilms verwendet wird "
                "und eine Serie gesondert verhandelt wird.\n\nAuch Anlage 2 zum Vertrag war bei meiner "
                "Unterschrift noch nicht mit Passagen gefüllt. Ich möchte vermeiden, dass daraus später "
                "ein Missverständnis entsteht.\n\nViele Grüße\nJonna"
            ),
        ),
        _doc(
            "04_Finanzierung_Sicherheiten/01_Produktionsdarlehen.pdf",
            "pdf",
            "Produktionsdarlehensvertrag",
            sections=[
                _section(
                    "1. Darlehen",
                    "Die Palatina Medienbank AG gewährt der Kurpfalz Lichtbild GmbH am 18. April 2024 eine revolvierende Produktionslinie bis 1.850.000 EUR. Die Mittel sind ausschließlich für den Film Die letzte Rieslingspur zu verwenden.",
                    "Mit Nachtrag vom 10. Januar 2025 wird eine Fertigstellungstranche bis 420.000 EUR zugesagt. Auszahlungen setzen Budgetnachweise, Fertigstellungsberichte und wirksame Bestellung der vereinbarten Sicherheiten voraus.",
                ),
                _section(
                    "2. Rückzahlung",
                    "Die Rückführung erfolgt aus Fördermitteln, Mindestgarantien, Lizenzerlösen und sonstigen Verwertungseinnahmen. Endfälligkeit ist der 30. Juni 2027; bei wesentlichen Vertragsverletzungen, Zahlungseinstellung oder Insolvenzantrag kann die Bank kündigen.",
                ),
                _section(
                    "3. Sicherheiten",
                    "Vereinbart werden gesonderte Urkunden über Film- und Nutzungsrechte, körperliche Mastermedien und Produktionsgeräte sowie gegenwärtige und künftige Forderungen aus Vertrieb und Lizenzierung. Rang und Freigabe richten sich nach den jeweiligen Sicherheitenverträgen.",
                ),
                _section(
                    "4. Kontenführung",
                    "Verwertungserlöse sollen auf das Projektkonto IBAN DE00 0000 0000 0000 0000 00 bei der Palatina Medienbank fließen. Abweichende Konten dürfen nur mit Zustimmung der Bank als Erlöskonten verwendet werden.",
                ),
                _section(
                    "5. Unterschriften",
                    "Mannheim, 18. April 2024 — Palatina Medienbank AG, Bettina Karg und Hanno Seubert, handschriftlich unterzeichnet.",
                    "Schwetzingen, 19. April 2024 — Kurpfalz Lichtbild GmbH, Konrad Riemenschneider, handschriftlich unterzeichnet.",
                ),
            ],
        ),
        _doc(
            "04_Finanzierung_Sicherheiten/02_IP_Sicherungsvertrag_Filmrechte.docx",
            "docx",
            "Sicherungsvertrag Film- und Nutzungsrechte",
            sections=[
                _section(
                    "1. Sicherungszweck",
                    "Die Kurpfalz Lichtbild GmbH bestellt der Palatina Medienbank AG zur Sicherung sämtlicher gegenwärtiger und künftiger Ansprüche aus der Produktionsfinanzierung die in Anlage A und B bezeichneten Rechte und Rechtspositionen.",
                    "Der Sicherungszweck endet erst nach vollständiger und endgültiger Befriedigung der gesicherten Ansprüche. Freigaben bedürfen einer Erklärung der Bank in Textform.",
                ),
                _section(
                    "2. Erfasste Positionen",
                    "Erfasst werden nach dem Vertrag sämtliche der Sicherungsgeberin zustehenden ausschließlichen Nutzungsrechte am Filmprojekt, Rechte an Drehbuchfassungen und Bearbeitungen, Rechte des Filmherstellers, Rechte an Filmaufnahmen, Titel- und Kennzeichenpositionen sowie Ansprüche auf Herausgabe und Zugang zu produktionsbezogenen Unterlagen und Mastermaterialien, soweit übertragbar.",
                    "Rechte, die nur einfach, zeitlich begrenzt oder unter Zustimmungsvorbehalt eingeräumt wurden, sollen nur in diesem Umfang erfasst sein. Nicht übertragbare höchstpersönliche Rechte werden ausdrücklich ausgenommen.",
                ),
                _section(
                    "3. Nutzung bis Sicherungsfall",
                    "Bis zum Sicherungsfall darf die Sicherungsgeberin die Rechte im ordnungsgemäßen Geschäftsgang auswerten, Lizenzen erteilen und technisch bearbeiten. Verfügungen über das gesamte Projekt, ausschließliche Gebietslizenzen über zehn Jahre und weitere Sicherheiten bedürfen der vorherigen Zustimmung der Bank.",
                    "Als Sicherungsfall gelten insbesondere Kündigung des Darlehens, Insolvenzantrag und wesentliche Gefährdung der Sicherheiten. Nach Sicherungsfall soll die Bank die Verwertung im eigenen Namen oder durch einen von ihr beauftragten Dritten durchführen dürfen.",
                ),
                _section(
                    "4. Mitwirkung und Unterlagen",
                    "Die Sicherungsgeberin hält die Rechtekette, Verträge, Zustimmungen, Cue Sheets, Masterlisten und Zugangsdaten aktuell und stellt der Bank auf Verlangen Kopien bereit. Sie unterrichtet die Bank über Ansprüche von Rechtegebern und drohende Rechtsverluste.",
                ),
                _section(
                    "5. Anlage A",
                    "Anlage A nennt das Projekt Die letzte Rieslingspur, Arbeitstitel Rieslingnacht, Drehbuchfassungen 1 bis 7, Filmaufnahmen, Schnittfassungen, Ton- und Musikbestandteile, Trailer, Standfotos, Artwork, Untertitel, Audiodeskription und die Rechte des Filmherstellers.",
                    "Als Produktionskennzeichen wird KLP-2417 genannt. Verweise auf konkrete Verträge enthalten nur Datum und Vertragspartner, nicht immer die jeweilige Anlage oder Nachtragsfassung.",
                ),
                _section(
                    "6. Anlage B",
                    "Anlage B soll nicht uneingeschränkt übertragbare Fremdrechte, Laufzeiten und Territorien aufführen. In der vorliegenden unterzeichneten Ausfertigung sind lediglich Romanvorlage und Archivmaterial als Zeilen angelegt; die Spalten Laufzeit und Zustimmung sind teilweise leer.",
                ),
                _section(
                    "7. Unterschriften",
                    "Mannheim, 19. April 2024 — Palatina Medienbank AG, Bettina Karg und Hanno Seubert, handschriftlich unterzeichnet.",
                    "Schwetzingen, 19. April 2024 — Kurpfalz Lichtbild GmbH, Konrad Riemenschneider, handschriftlich unterzeichnet.",
                ),
            ],
        ),
        _doc(
            "04_Finanzierung_Sicherheiten/03_Sicherungsuebereignung_Mastermedien.pdf",
            "pdf",
            "Sicherungsübereignung Mastermedien und Geräte",
            sections=[
                _section(
                    "1. Gegenstände",
                    "Die Kurpfalz Lichtbild GmbH überträgt der Palatina Medienbank AG am 19. April 2024 das Sicherungseigentum an den in Anlage 1 einzeln bezeichneten beweglichen Sachen. Bei Austausch sollen Ersatzgegenstände nach den vertraglichen Voraussetzungen einbezogen werden.",
                    "Anlage 1 nennt LTO-KL-001, LTO-KL-002, RAID-Gehäuse KL-RAID-02, zwei Schnittrechner und einen Referenzmonitor mit Seriennummern. Shuttle-SSDs und Cloudspeicher werden nicht genannt.",
                ),
                _section(
                    "2. Besitz und Nutzung",
                    "Die Sachen verbleiben im unmittelbaren Besitz der Sicherungsgeberin, soweit sie nicht bei einem beauftragten Labor lagern. Die Sicherungsgeberin darf sie bis zum Sicherungsfall produktionsbezogen nutzen, muss sie kennzeichnen, versichern und in einer Inventarliste führen.",
                    "Für bei Dienstleistern lagernde Sachen soll die Sicherungsgeberin eine Besitzmittlungsbestätigung oder Herausgabevereinbarung beschaffen. Eine solche Erklärung der Komet Postproduction GmbH liegt der Urkunde nicht bei.",
                ),
                _section(
                    "3. Verwertung",
                    "Nach Eintritt des Sicherungsfalls darf die Bank Herausgabe verlangen und die Sachen nach angemessener Ankündigung verwerten. Die Sicherungsgeberin soll alle zum Lesen der Daten erforderlichen Passwörter und Dokumentationen herausgeben.",
                    "Die Urkunde trifft keine eigenständige Regelung darüber, wem urheberrechtliche oder sonstige immaterielle Rechte an den auf den Datenträgern gespeicherten Inhalten zustehen.",
                ),
                _section(
                    "4. Nachtrag vom 17. Februar 2026",
                    "Der Nachtrag ersetzt die ursprünglich vorgesehenen LTO-8-Bänder durch LTO-9-Bänder mit den Seriennummern L9P-773418 und L9P-773419. Die Gegenzeichnung der Bank ist vorhanden; die Produzentin unterzeichnete eine separate Seite.",
                ),
            ],
        ),
        _doc(
            "04_Finanzierung_Sicherheiten/04_Sicherungsabtretung_Lizenzforderungen.docx",
            "docx",
            "Sicherungsabtretung von Lizenz- und Vertriebsforderungen",
            sections=[
                _section(
                    "1. Abtretung",
                    "Die Kurpfalz Lichtbild GmbH tritt der Palatina Medienbank AG am 21. Februar 2025 alle gegenwärtigen und künftigen Forderungen aus Verleih-, Vertriebs-, Lizenz-, Sende-, Abruf-, Förder- und Auswertungsverträgen zum Film Die letzte Rieslingspur zur Sicherheit ab.",
                    "Erfasst werden Hauptforderungen, Nebenforderungen, Mindestgarantien, Umsatzbeteiligungen, Schadensersatz- und Abrechnungsansprüche. Reine Rückzahlungsansprüche aus Produktionsdienstleistungen sollen nicht erfasst sein.",
                ),
                _section(
                    "2. Einziehung vor Offenlegung",
                    "Die Sicherungsgeberin bleibt bis zum Widerruf ermächtigt, abgetretene Forderungen im eigenen Namen einzuziehen. Zahlungen sind auf das Projektkonto bei der Bank zu lenken. Die Bank darf die Abtretung jederzeit offenlegen und selbst Zahlung verlangen.",
                    "Die Einziehungsermächtigung endet nach dem Vertragswortlaut spätestens mit Insolvenzantrag oder Kündigung der Finanzierung, ohne dass es eines gesonderten Widerrufs bedarf.",
                ),
                _section(
                    "3. Forderungslisten",
                    "Die Sicherungsgeberin übermittelt monatlich eine Forderungsliste mit Vertrag, Schuldner, Fälligkeit, Währung, Einwendungen, Zahlweg und bereits eingegangenen Beträgen. Die letzte von der Bank archivierte Liste trägt den Stand 31. Juli 2026.",
                    "Die im Insolvenz-Datenraum befindliche Liste vom 18. Oktober 2026 enthält zusätzliche Forderungen und eine Gutschrift, deren Vertragsbezug nicht eindeutig ist.",
                ),
                _section(
                    "4. Unterschriften",
                    "Mannheim, 21. Februar 2025 — Palatina Medienbank AG, Bettina Karg und Hanno Seubert, handschriftlich unterzeichnet.",
                    "Schwetzingen, 21. Februar 2025 — Kurpfalz Lichtbild GmbH, Konrad Riemenschneider, handschriftlich unterzeichnet.",
                ),
            ],
        ),
        _xlsx(
            "04_Finanzierung_Sicherheiten/05_Sicherheitenregister_Bank.xlsx",
            "Sicherheitenregister der Bank",
            [
                {
                    "name": "Sicherheiten",
                    "headers": ["ID", "Sicherheit", "Urkunde", "Bestand/Umfang", "Letzte Prüfung", "Dokumentenstatus", "Bemerkung"],
                    "rows": [
                        ["S-01", "Film- und Nutzungsrechte", "19.04.2024", "Projekt KLP-2417", "02.09.2026", "Original im Tresor", "Anlage B lückenhaft"],
                        ["S-02", "Mastermedien und Geräte", "19.04.2024 + Nachtrag", "6 Positionen", "02.09.2026", "Original im Tresor", "LTO-KL-002 bei Komet"],
                        ["S-03", "Lizenzforderungen", "21.02.2025", "Globalzession projektbezogen", "31.07.2026", "Original im Tresor", "aktuelle Liste fehlt"],
                        ["S-04", "Projektkonto", "Kontovertrag", "Guthaben und Eingänge", "30.09.2026", "bankintern", "Rheinbild zahlte abweichend"],
                    ],
                },
                {
                    "name": "Freigaben",
                    "headers": ["Datum", "Anfrage", "Gegenstand", "Entscheidung", "Bedingung", "Beleg"],
                    "rows": [
                        ["14.03.2025", "Pfalzstern Filmverleih", "deutscher Kinoverleih", "Zustimmung zur Lizenz", "Zahlungen Projektkonto", "Bankmail archiviert"],
                        ["22.08.2025", "Rheinbild Mediathek", "Streaming D/A/CH", "Zustimmung zur Lizenz", "Abtretungsanzeige", "Anzeige bestätigt"],
                        ["05.04.2026", "Südwest-Fernsehkontor", "zwei Ausstrahlungen", "keine gesonderte Freigabe gefunden", "offen", "nicht vorhanden"],
                        ["18.10.2026", "Asset Deal Weintor", "gesamtes Filmpaket", "keine Entscheidung erfasst", "n/a", "Anfrage vor Signing nicht gefunden"],
                    ],
                },
            ],
        ),
        _mail(
            "04_Finanzierung_Sicherheiten/06_Abtretungsanzeige_Rheinbild.eml",
            "Abtretungsanzeige und Bestätigung Rheinbild",
            sender="Bettina Karg <bettina.karg@palatina-medienbank.example>",
            to=["Saskia Thoma <rights@rheinbild-mediathek.example>"],
            cc=["finanzen@kurpfalz-lichtbild.example"],
            date="Fri, 22 Aug 2025 09:11:00 +0200",
            subject="Offenlegung Sicherungsabtretung – Die letzte Rieslingspur",
            body=(
                "Sehr geehrte Frau Thoma,\n\nwir zeigen an, dass die gegenwärtigen und künftigen "
                "Forderungen der Kurpfalz Lichtbild GmbH aus dem Lizenzvertrag Die letzte Rieslingspur "
                "vom 18. August 2025 an die Palatina Medienbank AG zur Sicherheit abgetreten wurden. "
                "Bis zu einer abweichenden schriftlichen Weisung bitten wir um Zahlung auf das im "
                "Vertrag bezeichnete Projektkonto bei uns.\n\nBitte bestätigen Sie Erhalt und teilen "
                "Sie uns bestehende Einwendungen oder Gegenrechte mit.\n\nMit freundlichen Grüßen\n"
                "Bettina Karg"
            ),
            attachments=["04_Finanzierung_Sicherheiten/04_Sicherungsabtretung_Lizenzforderungen.docx"],
        ),
        _doc(
            "05_Lizenz_Forderungen/01_Lizenzvertrag_Rheinbild.docx",
            "docx",
            "Streaming-Lizenzvertrag Rheinbild Mediathek",
            sections=[
                _section(
                    "1. Lizenz",
                    "Die Kurpfalz Lichtbild GmbH räumt der Rheinbild Mediathek GmbH am 18. August 2025 für Deutschland, Österreich und die Schweiz ein ausschließliches Streamingrecht im Abonnement- und werbefinanzierten Abrufdienst ein.",
                    "Die Lizenzzeit beginnt am 1. April 2026 und endet am 31. März 2029. Kino-, lineare Sende-, Download-to-own- und physische Rechte bleiben unberührt.",
                ),
                _section(
                    "2. Vergütung",
                    "Rheinbild zahlt eine Mindestgarantie von 360.000 EUR in vier Raten zu je 90.000 EUR: bei Lieferung, zum Lizenzstart, am 1. April 2027 und am 1. April 2028. Zusätzlich sind nutzungsabhängige Erlöse nach Überschreiten der Mindestgarantie abzurechnen.",
                    "Rheinbild kann dokumentierte Kosten für technische Nachlieferungen bis 12.000 EUR verrechnen. Die Rate zum Lizenzstart wurde am 6. April 2026 gezahlt.",
                ),
                _section(
                    "3. Rechtegarantie und Lieferung",
                    "Die Lizenzgeberin gewährleistet im Vertrag, die eingeräumten Rechte für die Lizenzzeit ausüben zu dürfen. Für Archivmaterial mit kürzerer Laufzeit soll sie rechtzeitig Verlängerungen beschaffen oder eine ersatzweise Fassung liefern.",
                    "Geliefert werden ein ProRes-Mezzanine, M&E, deutsche Untertitel, Audiodeskription, Standfotos und Metadaten. Rheinbild bestätigt technischen Erhalt am 3. April 2026.",
                ),
                _section(
                    "4. Übertragung",
                    "Rheinbild darf den Vertrag auf verbundene Plattformgesellschaften übertragen. Eine Übertragung der Lizenzgeberstellung bedarf der vorherigen Zustimmung von Rheinbild, die nicht unbillig verweigert werden darf.",
                    "Sicherungsabtretungen von Zahlungsforderungen sind zulässig; eine Abtretungsanzeige soll den Zahlungsweg eindeutig bezeichnen.",
                ),
                _section(
                    "5. Unterschriften",
                    "Heidelberg, 18. August 2025 — Rheinbild Mediathek GmbH, Saskia Thoma, handschriftlich unterzeichnet.",
                    "Schwetzingen, 18. August 2025 — Kurpfalz Lichtbild GmbH, Konrad Riemenschneider, handschriftlich unterzeichnet.",
                ),
            ],
        ),
        _doc(
            "05_Lizenz_Forderungen/02_Sendevertrag_Suedwest.pdf",
            "pdf",
            "Sendevertrag Südwest-Fernsehkontor",
            sections=[
                _section(
                    "1. Rechteumfang",
                    "Das Südwest-Fernsehkontor erwirbt am 2. Februar 2026 das Recht zu zwei linearen Ausstrahlungen und je einer Wiederholung in Deutschland zwischen 1. Dezember 2026 und 30. November 2028.",
                    "Ein begleitender Abruf für sieben Tage nach jeder Erstausstrahlung ist eingeschlossen. Sonstige Abruf- und internationale Rechte sind nicht umfasst.",
                ),
                _section(
                    "2. Vergütung",
                    "Das Lizenzentgelt beträgt 210.000 EUR. 70.000 EUR sind 30 Tage nach Vertragsschluss fällig, 70.000 EUR nach technischer Abnahme und 70.000 EUR 30 Tage vor der ersten Ausstrahlung.",
                    "Die dritte Rate ist nach der aktuellen Programmplanung am 2. November 2026 fällig. Einwendungen wegen Archivlaufzeiten wurden in einem technischen Begleitschreiben vorbehalten.",
                ),
                _section(
                    "3. Vertragsübernahme",
                    "Eine Übertragung der Lizenzgeberstellung oder des gesamten Vertrags bedarf der vorherigen schriftlichen Zustimmung des Südwest-Fernsehkontors. Die Abtretung fälliger Zahlungsansprüche an ein Kreditinstitut ist zulässig.",
                ),
            ],
        ),
        _doc(
            "05_Lizenz_Forderungen/03_Verleih_Deal_Memo_Pfalzstern.pdf",
            "pdf",
            "Deal Memo Pfalzstern Filmverleih",
            sections=[
                _section(
                    "1. Verleihrechte",
                    "Pfalzstern Filmverleih GmbH erhält die exklusiven deutschen Kinorechte vom 1. Februar 2026 bis 31. Januar 2031. Festivalvorführungen bis zu zwanzig Termine bleiben der Produzentin vorbehalten.",
                    "Der Verleih darf DCP-Kopien herstellen und an Kinos liefern. Das physische DCP-Laufwerk KL-DCP-01 wird leihweise zur technischen Vervielfältigung übergeben und bleibt laut Deal Memo im Eigentum der Produzentin oder ihrer Sicherheitengeberin.",
                ),
                _section(
                    "2. Mindestgarantie und Kosten",
                    "Die Mindestgarantie beträgt 180.000 EUR, zahlbar 90.000 EUR bei Unterzeichnung und 90.000 EUR bei technischer Abnahme. Verleihvorkosten bis 240.000 EUR werden vor Erlösbeteiligung zurückgeführt.",
                    "Der Verleih berichtet quartalsweise. Die Abrechnung zum 30. Juni 2026 weist einen negativen Verleihstand aus; eine Forderung aus Erlösbeteiligung besteht danach noch nicht.",
                ),
                _section(
                    "3. Formstatus",
                    "Das Deal Memo ist von beiden Parteien unterschrieben und sieht die Erstellung eines Langvertrags bis 31. März 2026 vor. Ein Langvertrag befindet sich nicht in der vorliegenden Akte.",
                ),
            ],
        ),
        _xlsx(
            "05_Lizenz_Forderungen/04_Offene_Posten_Lizenzen.xlsx",
            "Offene Lizenz- und Vertriebsforderungen",
            [
                {
                    "name": "Offene_Posten",
                    "headers": ["Debitor", "Vertrag", "Rechnung", "Fälligkeit", "Brutto EUR", "Zahlweg", "Status", "Einwand"],
                    "rows": [
                        ["Rheinbild Mediathek", "18.08.2025", "KL-2026-118", "01.04.2027", 107100.00, "Projektkonto", "zukünftig", "keiner mitgeteilt"],
                        ["Südwest-Fernsehkontor", "02.02.2026", "KL-2026-204", "02.11.2026", 83300.00, "Projektkonto", "offen", "Archivnachweis angefragt"],
                        ["Festival Lumière du Rhin", "12.01.2026", "KL-2026-087", "15.03.2026", 3800.00, "operatives Konto", "überfällig", "Quellensteuerbescheinigung"],
                        ["Heidelberger Filmnacht e.V.", "05.02.2026", "KL-2026-101", "30.04.2026", 1428.00, "operatives Konto", "teilbezahlt", "Gutschrift 238 EUR"],
                        ["Pfalzstern Filmverleih", "Deal Memo", "Abrechnung Q2", "noch nicht fällig", 0.00, "n/a", "negativer Verleihstand", "Vorkosten"],
                        ["Rheinbild Mediathek", "18.08.2025", "KL-2026-119", "01.04.2026", 107100.00, "operatives Konto", "bezahlt 06.04.2026", "abweichender Zahlweg"],
                    ],
                },
                {
                    "name": "Zahlungseingaenge",
                    "headers": ["Datum", "Zahler", "Betrag EUR", "Konto", "Zuordnung Buchhaltung", "Abweichung"],
                    "rows": [
                        ["19.08.2025", "Rheinbild", 90000.00, "Projektkonto", "Mindestgarantie Rate 1 netto", "keine"],
                        ["06.04.2026", "Rheinbild", 107100.00, "operatives Konto", "Rate 2 brutto", "nicht Projektkonto"],
                        ["10.02.2026", "Südwest", 83300.00, "Projektkonto", "Rate 1 brutto", "keine"],
                        ["18.05.2026", "Südwest", 83300.00, "Projektkonto", "Rate 2 brutto", "keine"],
                        ["06.10.2026", "Rheinbild", 17850.00, "Massekonto", "technische Nachvergütung", "Vertragsposten unklar"],
                    ],
                },
                {
                    "name": "Abgrenzungen",
                    "headers": ["Position", "Buchhaltung", "APA-Anlage", "Bankliste", "Klärung"],
                    "rows": [
                        ["Südwest Rate 3", "Forderung", "übertragene Forderung", "sicherungsabgetreten", "Zahlungsempfänger"],
                        ["Rheinbild Rate 2027", "zukünftige Forderung", "Erwerbererlös", "sicherungsabgetreten", "Vertragsübernahme"],
                        ["Festival Lumière", "Forderung", "nicht aufgeführt", "sicherungsabgetreten", "Auslandsbeleg"],
                        ["Pfalzstern Abrechnung", "kein Aktivposten", "Vertrag übertragen", "Globalzession bei Entstehen", "Vorkosten prüfen"],
                    ],
                },
            ],
        ),
        _mail(
            "05_Lizenz_Forderungen/05_Mail_Rheinbild_Zahlweg.eml",
            "Rheinbild fragt nach Zahlungsempfänger",
            sender="Saskia Thoma <rights@rheinbild-mediathek.example>",
            to=["Dr. Marlene Berthold <berthold@bh-insolvenz.example>"],
            cc=["Bettina Karg <bettina.karg@palatina-medienbank.example>", "finanzen@kurpfalz-lichtbild.example"],
            date="Fri, 9 Oct 2026 14:08:00 +0200",
            subject="Rieslingspur: künftige Raten / Abtretungsanzeige und Erwerberwechsel",
            body=(
                "Sehr geehrte Frau Dr. Berthold,\n\nuns liegt seit August 2025 eine Anzeige der "
                "Palatina Medienbank zur Abtretung der Lizenzforderungen vor. Zugleich teilte Ihr Büro "
                "mit, ein Erwerber solle in den Vertrag eintreten. Bitte teilen Sie uns vor Ausstellung "
                "der nächsten Rechnung verbindlich mit, an wen mit schuldbefreiender Wirkung zu zahlen "
                "ist und wer unsere Zustimmung zur Vertragsübernahme einholt.\n\nDie Archivlizenzen "
                "laufen vor Ende unserer Lizenzzeit aus. Wir benötigen ferner die zugesagten "
                "Verlängerungsnachweise oder eine Ersatzfassung.\n\nMit freundlichen Grüßen\nSaskia Thoma"
            ),
            attachments=["05_Lizenz_Forderungen/01_Lizenzvertrag_Rheinbild.docx"],
        ),
        _csv(
            "05_Lizenz_Forderungen/06_Rechnungsregister.csv",
            "Rechnungsregister Filmverwertung",
            ["Belegnummer", "Datum", "Debitor", "Leistung", "Netto EUR", "USt EUR", "Brutto EUR", "Fälligkeit", "Status"],
            [
                ["KL-2025-144", "18.08.2025", "Rheinbild Mediathek", "Mindestgarantie Rate 1", "90000.00", "17100.00", "107100.00", "28.08.2025", "bezahlt"],
                ["KL-2026-032", "03.02.2026", "Südwest-Fernsehkontor", "Lizenzrate 1", "70000.00", "13300.00", "83300.00", "05.03.2026", "bezahlt"],
                ["KL-2026-087", "15.02.2026", "Festival Lumière du Rhin", "Festivalvorführung", "3200.00", "0.00", "3200.00", "15.03.2026", "offen"],
                ["KL-2026-101", "31.03.2026", "Heidelberger Filmnacht", "Vorführung", "1400.00", "266.00", "1666.00", "30.04.2026", "Teilzahlung"],
                ["KL-2026-119", "01.04.2026", "Rheinbild Mediathek", "Mindestgarantie Rate 2", "90000.00", "17100.00", "107100.00", "11.04.2026", "bezahlt operatives Konto"],
                ["KL-2026-161", "18.04.2026", "Südwest-Fernsehkontor", "Lizenzrate 2", "70000.00", "13300.00", "83300.00", "18.05.2026", "bezahlt"],
                ["KL-2026-204", "02.10.2026", "Südwest-Fernsehkontor", "Lizenzrate 3", "70000.00", "13300.00", "83300.00", "02.11.2026", "offen"],
            ],
        ),
        _doc(
            "06_Insolvenz_AssetDeal/01_Insolvenzeroeffnungsbeschluss.pdf",
            "pdf",
            "Beschluss über die Eröffnung des Insolvenzverfahrens",
            sections=[
                _section(
                    "1. Gericht und Verfahrensdaten",
                    "Aktenzeichen: 51 IN 217/26. Beschluss vom 30. September 2026, 09:00 Uhr.",
                    "Über das Vermögen der Kurpfalz Lichtbild GmbH, Carl-Theodor-Straße 21, 68723 Schwetzingen, wird wegen Zahlungsunfähigkeit und Überschuldung das Insolvenzverfahren eröffnet.",
                ),
                _section(
                    "2. Bestellung",
                    "Zur Insolvenzverwalterin wird Rechtsanwältin Dr. Marlene Berthold, Kurfürsten-Anlage 34, 69115 Heidelberg, bestellt. Forderungen sind bis 20. November 2026 anzumelden.",
                    "Berichtstermin und Prüfungstermin werden gesondert bekannt gemacht. Der Beschluss enthält keine Feststellung zur dinglichen oder urheberrechtlichen Zuordnung einzelner Filmassets.",
                ),
                _section(
                    "3. Hinweise",
                    "Schuldner der Schuldnerin werden aufgefordert, nur unter Beachtung der gesetzlichen Wirkungen der Verfahrenseröffnung zu leisten. Personen, die Sachen der Schuldnerin besitzen, werden auf ihre Auskunftspflichten hingewiesen.",
                ),
            ],
        ),
        _doc(
            "06_Insolvenz_AssetDeal/02_Inventarvermerk_Verwalterin.docx",
            "docx",
            "Inventar- und Datenraumvermerk der Insolvenzverwalterin",
            sections=[
                _section(
                    "1. Aufnahme vor Ort",
                    "Am 1. Oktober 2026 nahmen RA Pia Hofmeister und Sachbearbeiter Johann Neuner die Räume der Kurpfalz Lichtbild GmbH in Schwetzingen auf. LTO-KL-001 und RAID KL-RAID-02 wurden im Technikraum vorgefunden und mit Inventaretiketten versehen.",
                    "LTO-KL-002 befindet sich nach Auskunft von Komet Postproduction in Mannheim. Eine Shuttle-SSD soll bei der Regisseurin liegen; eine weitere ist nicht auffindbar. Physische Herausgaben an Dritte sind bis Closing nicht dokumentiert.",
                ),
                _section(
                    "2. Digitale Zugänge",
                    "Das Verwalterteam übernahm Administratorzugriff auf CloudVault, Produktionsserver und ScreenPass. Zwei Wiederherstellungsschlüssel liegen vor; die Übereinstimmung mit den Masterverschlüsselungen wurde noch nicht vollständig getestet.",
                    "Für StudioCloud der Komponistin und das Regiearchiv bestehen keine Administrationsrechte der Schuldnerin.",
                ),
                _section(
                    "3. Verträge und Forderungen",
                    "Im Datenraum wurden 47 Rechte-, Produktions- und Lizenzverträge erfasst. Die Rechtekettenmatrix weist vier offene Punkte aus. Eine gesonderte Forderungsmatrix nennt 321.628 EUR nominelle offene oder zukünftige Posten.",
                    "Die Palatina Medienbank meldete telefonisch Rechte an IP, Mastermedien und Forderungen. Eine abschließende Abstimmung oder Freigabe fand bis zum Vermerk vom 18. Oktober nicht statt.",
                ),
                _section(
                    "4. Bieterverfahren",
                    "Vier Interessenten erhielten einen anonymisierten Teaser, zwei einen Datenraumzugang. Weintor Streamworks legte das höchste Paketangebot vor und verlangte Closing bis Ende Oktober sowie Übergabe aller Master und Kundenbeziehungen.",
                ),
            ],
        ),
        _doc(
            "06_Insolvenz_AssetDeal/03_Bewertung_Filmpaket.pdf",
            "pdf",
            "Bewertung Filmpaket Neckarblick Valuation",
            sections=[
                _section(
                    "1. Auftrag und Stichtag",
                    "Neckarblick Valuation Partners GmbH bewertet zum 12. Oktober 2026 den wirtschaftlichen Wert des Filmpakets Die letzte Rieslingspur für Zwecke eines beschleunigten Verkaufs im Insolvenzverfahren.",
                    "Die Bewertung stellt keine rechtliche Due Diligence dar. Sie unterstellt, dass die für die geplante Auswertung erforderlichen Rechte wirksam bei der Verkäuferseite gebündelt und übertragbar sind.",
                ),
                _section(
                    "2. Ertragswertannahmen",
                    "Berücksichtigt werden vertraglich erwartete Einnahmen aus Rheinbild und Südwest, eine internationale Plattformlizenz ab 2027, Bibliotheksauswertung über zehn Jahre und Erlöse aus Bildungslizenzen.",
                    "Der abgezinste Wert der Rechtebibliothek wird in einer Bandbreite von 780.000 EUR bis 1.060.000 EUR angegeben. Offene Forderungen werden mit 195.000 EUR bis 230.000 EUR bewertet. Hardware und Datenträger werden mit 22.000 EUR bis 38.000 EUR angesetzt.",
                ),
                _section(
                    "3. Sensitivitäten",
                    "Bei fehlender internationaler Auswertbarkeit der Archivsequenzen sinkt der Rechtewert nach Modell um 110.000 EUR. Eine fehlende Musikfreigabe für die Festivalfassung betrifft nach Annahme nur diese Fassung.",
                    "Die Bewertung setzt die Verlängerung der Archivlizenzen, eine vollständige Rechtekette, Zugang zu den Masterdateien und Zustimmung wesentlicher Lizenznehmer zum Vertragsübergang voraus.",
                ),
                _section(
                    "4. Nicht geprüfte Sicherheiten",
                    "Die Gutachterin hat Sicherheitenurkunden zur Kenntnis genommen, aber weder deren Wirksamkeit noch Rang, Verwertungsbefugnis oder Freigabeanforderungen geprüft. Der Bericht ordnet den Kaufpreis daher ausschließlich wirtschaftlich zu.",
                ),
            ],
        ),
        _doc(
            "06_Insolvenz_AssetDeal/04_Asset_Purchase_Agreement_unterschrieben.docx",
            "docx",
            "Asset Purchase Agreement",
            sections=[
                _section(
                    "1. Parteien und Signing",
                    "Verkäuferin ist Dr. Marlene Berthold als Insolvenzverwalterin über das Vermögen der Kurpfalz Lichtbild GmbH. Käuferin ist die Weintor Streamworks GmbH, Deidesheim, vertreten durch Geschäftsführer Vincent Bundschuh.",
                    "Der Vertrag wird am 20. Oktober 2026 in Heidelberg beiderseits handschriftlich unterzeichnet. Signing und Closing fallen auseinander; Vollzug ist für den 29. Oktober 2026 vorgesehen.",
                ),
                _section(
                    "2. Kaufgegenstände",
                    "Verkauft werden, soweit der Verkäuferin zugehörig und übertragbar, sämtliche vermögenswerten Positionen zum Film Die letzte Rieslingspur: Filmherstellerrechte, ausschließliche und einfache Nutzungsrechte, Titelpositionen, Drehbuch- und Musikunterlagen, Master und Arbeitsmaterialien, Trailer, Artwork, Standfotos, Metadaten und produktionsbezogene Dokumentationen.",
                    "Ferner werden die in Anlage 2 bezeichneten körperlichen Gegenstände einschließlich LTO-KL-001, LTO-KL-002 und RAID KL-RAID-02 sowie die in Anlage 3 bezeichneten Forderungen verkauft. Rechte Dritter und Sicherheiten werden in einer Offenlegungsliste erwähnt.",
                ),
                _section(
                    "3. Kundenverträge",
                    "Die Käuferin soll in Rheinbild-, Südwest- und Pfalzstern-Verträge eintreten, soweit erforderliche Zustimmungen vorliegen. Bis dahin soll die Verkäuferin Abrechnungen wirtschaftlich für Rechnung der Käuferin weiterleiten.",
                    "Die Käuferin übernimmt ab Closing Kosten für Verlängerung der Archivlizenzen. Eine Garantie, dass alle Vertragsübernahmen wirksam werden, wird nicht abgegeben.",
                ),
                _section(
                    "4. Kaufpreis",
                    "Der Kaufpreis beträgt 1.180.000 EUR. Anlage 4 ordnet 910.000 EUR der Rechtebibliothek, 240.000 EUR ausgewählten Forderungen und 30.000 EUR Hardware und Datenträgern zu.",
                    "Zahlung erfolgt auf das Massekonto nach Bestätigung der technischen Übergabebereitschaft. Ein Einbehalt von 80.000 EUR ist für fehlende Vertragszustimmungen bis 31. Januar 2027 vorgesehen.",
                ),
                _section(
                    "5. Sicherheiten und Belastungen",
                    "Die Verkäuferin legt in Anlage 5 die Sicherheiten der Palatina Medienbank offen. Die Parteien halten fest, die Verkäuferin gehe davon aus, zur Verwertung des Filmpakets im Rahmen des Insolvenzverfahrens befugt zu sein.",
                    "Die Käuferin erhält keine Garantie einer lastenfreien Übertragung, soweit Rechte oder Forderungen wirksam zugunsten Dritter belastet sind. Sie erwartet jedoch eine Übergabe aller verfügbaren Gegenstände und Zugangsmittel am Closing-Tag.",
                ),
                _section(
                    "6. Vollzugsbedingungen",
                    "Vollzugsbedingungen sind Kaufpreiszahlung, Übergabe der Masterzugänge, Unterzeichnung des Übergabeprotokolls und Vorlage mindestens der Rheinbild-Zustimmung. Eine ausdrückliche Freigabe der Palatina Medienbank ist in der Liste nicht als Bedingung bezeichnet.",
                    "Die Verkäuferin darf auf nicht erfüllte Bedingungen verzichten, soweit diese allein ihrem Schutz dienen. Die Käuferin darf bei wesentlichem Fehlen des Referenzmasters zurücktreten.",
                ),
                _section(
                    "7. Gewährleistung",
                    "Der Verkauf erfolgt aus der Insolvenzmasse im gegenwärtigen Zustand. Garantiert werden nur Vertretungsmacht der Unterzeichnenden, Existenz der aufgelisteten Dateien nach Kenntnis und Offenlegung wesentlicher Ansprüche Dritter. Weitergehende Rechts- und Sachmängelhaftung wird soweit zulässig ausgeschlossen.",
                ),
                _section(
                    "8. Anlagenstatus",
                    "Anlagen 1 bis 6 sind paraphiert. Anlage 2 nennt körperliche Gegenstände, Anlage 3 Forderungen, Anlage 4 Kaufpreisallokation, Anlage 5 Sicherheiten und Anlage 6 Übergabeplan. Die Rechtekettenmatrix ist als Datenraumdokument referenziert, aber nicht körperlich angeheftet.",
                ),
                _section(
                    "9. Unterschriften",
                    "Heidelberg, 20. Oktober 2026 — Dr. Marlene Berthold als Insolvenzverwalterin, handschriftlich unterzeichnet.",
                    "Deidesheim, 20. Oktober 2026 — Weintor Streamworks GmbH, Vincent Bundschuh, handschriftlich unterzeichnet.",
                ),
            ],
        ),
        _xlsx(
            "06_Insolvenz_AssetDeal/05_Closing_Checkliste.xlsx",
            "Closing- und Übergabecheckliste",
            [
                {
                    "name": "Closing",
                    "headers": ["Nr.", "Vorgang", "Verantwortlich", "Fällig", "Status 21.10.", "Nachweis", "Bemerkung"],
                    "rows": [
                        [1, "Kaufpreiszahlungsfreigabe", "Weintor", "29.10. 12:00", "vorbereitet", "Bankbestätigung", "nach Übergabebereitschaft"],
                        [2, "LTO-KL-001 übergeben", "Verwalterin", "29.10. 09:00", "geplant", "Übergabeprotokoll", "liegt in Schwetzingen"],
                        [3, "LTO-KL-002 herausgeben", "Komet", "29.10. 10:00", "angefragt", "Kurierquittung", "offene Rechnung Komet"],
                        [4, "CloudVault-Admin übertragen", "Verwalterin/Komet", "29.10. 09:30", "Token erstellt", "Systemprotokoll", "zweiter Schlüssel offen"],
                        [5, "Rheinbild-Zustimmung", "Weintor", "28.10.", "Entwurf", "unterzeichnete Zustimmung", "wesentliche Bedingung"],
                        [6, "Südwest-Zustimmung", "Weintor", "nach Closing", "nicht begonnen", "Zustimmung", "nicht Closing-Bedingung"],
                        [7, "Bankfreigabe Filmrechte", "Verkäuferin", "n/a", "laut Verkäuferseite nicht erforderlich", "kein Dokument", "Bank widerspricht bislang nicht schriftlich"],
                        [8, "Bankfreigabe Datenträger", "Verkäuferin", "n/a", "laut Verkäuferseite nicht erforderlich", "kein Dokument", "Sicherungsübereignung offengelegt"],
                        [9, "Forderungsliste Stichtag", "Verwalterin", "28.10.", "in Arbeit", "Excel final", "Rheinbild-Zahlweg klären"],
                        [10, "Schlüssel- und Hashprüfung", "Komet/Weintor", "28.10.", "Termin bestätigt", "Prüfprotokoll", "Hashliste fehlt im Datenraum"],
                    ],
                },
                {
                    "name": "Uebergabe",
                    "headers": ["Paket", "Inhalt", "Ort/Kanal", "Übergabeart", "Empfänger", "Offen"],
                    "rows": [
                        ["P-01", "LTO-KL-001 und RAID", "Schwetzingen", "Kurier persönlich", "Weintor", "Identitätskontrolle"],
                        ["P-02", "LTO-KL-002", "Mannheim", "Kurier", "Weintor", "Herausgabe Komet"],
                        ["P-03", "CloudVault", "online", "Adminwechsel", "Weintor", "Recovery Key"],
                        ["P-04", "Vertrags- und Rechteordner", "Datenraum", "Export", "Weintor", "fehlende Langverträge"],
                        ["P-05", "Forderungsdaten", "verschlüsselt", "Excel/CSV", "Weintor", "Abtretungsanzeigen"],
                        ["P-06", "Marketingmaterial", "Datenraum", "Download", "Weintor", "Standfotoeinschränkung"],
                    ],
                },
            ],
        ),
        _mail(
            "06_Insolvenz_AssetDeal/06_Mail_Verwalterin_Vollzugsankuendigung.eml",
            "Vollzugsankündigung der Insolvenzverwalterin",
            sender="Dr. Marlene Berthold <berthold@bh-insolvenz.example>",
            to=["Bettina Karg <bettina.karg@palatina-medienbank.example>"],
            cc=["Pia Hofmeister <hofmeister@bh-insolvenz.example>", "Vincent Bundschuh <bundschuh@weintor-streamworks.example>"],
            date="Wed, 21 Oct 2026 18:42:00 +0200",
            subject="Kurpfalz Lichtbild / Vollzug Filmpaket Die letzte Rieslingspur am 29.10.",
            body=(
                "Sehr geehrte Frau Karg,\n\nbeigefügt übersende ich den gestern beiderseits "
                "unterzeichneten Unternehmenskaufvertrag. Das Angebot von Weintor Streamworks war im "
                "Bieterverfahren wirtschaftlich überlegen und wahrt die laufenden Auswertungsverträge. "
                "Wir werden den Vertrag am 29. Oktober vollziehen und die in den Anlagen bezeichneten "
                "Mastermedien, Rechteunterlagen, Zugänge und Forderungsdaten übergeben.\n\nIhre "
                "Sicherheiten sind in Anlage 5 offengelegt. Nach unserer derzeitigen Auffassung steht "
                "dies dem vorgesehenen Vollzug nicht entgegen. Erlöszuordnung und Abrechnung können im "
                "Anschluss geklärt werden. Bitte lassen Sie etwaige tatsächliche Einwände gegen die "
                "Inventarliste bis 26. Oktober, 12:00 Uhr, gesammelt zukommen.\n\nMit freundlichen "
                "Grüßen\nDr. Marlene Berthold\nInsolvenzverwalterin"
            ),
            attachments=[
                "06_Insolvenz_AssetDeal/04_Asset_Purchase_Agreement_unterschrieben.docx",
                "06_Insolvenz_AssetDeal/05_Closing_Checkliste.xlsx",
                "02_Produktion_Medien/03_Medien_und_Geraeteinventar.xlsx",
            ],
        ),
        _mail(
            "06_Insolvenz_AssetDeal/07_Mail_Erwerberin_Vorfreude.eml",
            "Nachricht der Erwerberin zur bevorstehenden Übernahme",
            sender="Vincent Bundschuh <bundschuh@weintor-streamworks.example>",
            to=["Dr. Marlene Berthold <berthold@bh-insolvenz.example>", "Konrad Riemenschneider <riemenschneider@kurpfalz-lichtbild.example>"],
            cc=["closing@weintor-streamworks.example", "mastering@komet-post.example"],
            date="Wed, 21 Oct 2026 19:06:00 +0200",
            subject="Willkommen Rieslingspur – Technikteam steht für den 29.10. bereit",
            body=(
                "Liebe Frau Dr. Berthold, lieber Herr Riemenschneider,\n\nwir freuen uns sehr, dass "
                "der Vertrag unterzeichnet ist. Unser Technikteam steht am 29. Oktober ab 09:00 Uhr in "
                "Schwetzingen bereit und hat den Import in unsere Bibliothek vorbereitet. Wir würden "
                "unmittelbar nach Hashprüfung mit den französischen und englischen Untertiteln beginnen "
                "und Rheinbild noch am selben Tag die neue Ansprechpartnerin vorstellen.\n\nBitte sorgen "
                "Sie dafür, dass beide LTO-Bänder, das RAID, der CloudVault-Adminzugang und die finale "
                "Forderungsliste bereitliegen. Für die Bankthemen verlassen wir uns auf die im Vertrag "
                "abgebildete Abwicklung durch die Verkäuferseite.\n\nHerzliche Grüße aus Deidesheim\n"
                "Vincent Bundschuh\nGeschäftsführer"
            ),
        ),
        _doc(
            "06_Insolvenz_AssetDeal/08_Datenraum_und_DD_Fragen.pdf",
            "pdf",
            "Datenraumindex und offene Due-Diligence-Fragen",
            sections=[
                _section(
                    "1. Datenraumstand",
                    "Stand des Index: 19. Oktober 2026, 22:15 Uhr. Enthalten sind Gesellschaftsunterlagen, Produktionsakten, Finanzierungsverträge, Rechtekettenmatrix, Masterinventar, Lizenzverträge, Forderungslisten, Bewertungsbericht und Kaufvertragsentwürfe.",
                    "Als fehlend markiert sind der Ensemblevertrag Filmmusik, die Langfassung des Drohnenvertrags, zwei Komparsenfreigaben, die aktuelle Hashliste und eine Erklärung der Palatina Medienbank zur geplanten Verwertung.",
                ),
                _section(
                    "2. Käuferfragen",
                    "Weintor fragte nach weltweiter Archivnutzung über 2027, Recht zur Herstellung weiterer Sprachfassungen, Fortsetzungs- und Serienrechten, KI-gestützter Synchronisation, Rohmaterialzugang und Übertragung offener Forderungen.",
                    "Die Verkäuferseite antwortete, Rechte würden nur im vorhandenen und übertragbaren Umfang verkauft; fehlende Archivverlängerungen werde die Käuferin auf eigene Kosten beschaffen. Zur Bankfreigabe verwies sie auf die Offenlegung im APA.",
                ),
                _section(
                    "3. Bankbezogene Einträge",
                    "Eine DD-Frage vom 16. Oktober lautet: Sind Sicherungsrechte der Palatina wirksam freigegeben? Antwort Verkäuferseite vom 18. Oktober: Freigabe aus Sicht Verkäuferseite für Verwertung nicht erforderlich; Erlösrechte bleiben gesondert zu klären.",
                    "Ein früherer Index vom 10. Oktober führte Bankfreigabe oder Verwertungsvereinbarung als Closing-Dokument C-14. Im aktuellen Index ist C-14 mit dem Status entfällt gekennzeichnet.",
                ),
                _section(
                    "4. Endstand der Akte",
                    "Eine Reaktion der Palatina Medienbank auf die Vollzugsankündigung, ein anwaltliches Gutachten, ein gerichtlicher Antrag, eine Genehmigung der Verwertung oder eine vertragliche Einigung sind nicht Bestandteil der übergebenen Unterlagen.",
                ),
            ],
        ),
    ]
)
