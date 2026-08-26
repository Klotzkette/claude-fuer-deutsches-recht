---
name: gerichtliche-versandmappe-endfertigen
description: "Endfertigt einen vorhandenen gerichtlichen Schriftsatz mit Anlagen zur kontrollierten beA-Versandmappe: liest Aktenordner und gerichtliche Vorgaben zuerst, prüft Anträge, Tatsachenfundstellen und Beweisbezüge, führt K-, B-, AST- oder AG-Nummern fort, erzeugt einzelne gestempelte PDFs, wählt das dokumentierte Dateinamensprofil und liefert Manifest."
---

# Gerichtliche Versandmappe endfertigen

## 1. Direktstart

Lies zuerst den neuesten Schriftsatz, das Anlagenverzeichnis, alle im Schriftsatz genannten Dateien, gerichtliche Verfügungen und vorhandene Kanzleivorlagen. Erzeuge unmittelbar eine Produktionsmatrix. Frage nicht erneut nach Tatsachen, die aus dem Ordner hervorgehen.

Fehlt ein erkennbarer Gestaltungsstandard, frage nach der ersten Sichtung in einem Satz nach Briefkopf, Schrift, Rand, Datum und gewünschter Anlagenbezeichnung. Fehlen Gericht, Aktenzeichen oder Frist, behandle dies als Sperrpunkt.

## 2. Produktionsmatrix

| Position | Schriftsatzfundstelle | Beweisthema | Quelldatei | Nummer | PDF- und Sichtstatus | offener Punkt |
| --- | --- | --- | --- | --- | --- | --- |
| Hauptdokument | gesamte Fassung | Anträge und Vortrag | Datei | 00 | final oder Entwurf | Freigabe |
| Anlage | Seite und Absatz | konkrete Tatsache | Datei | K 1 oder B 1 | offen, geprüft oder fertig | Lücke |

Prüfe jeden Antrag gegen Rubrum, Sachantrag, Hilfsantrag, Zinsbeginn, Kostenantrag und Vollstreckungsbezug. Eine Anlage heilt keinen unverständlichen oder unsubstantiierten Vortrag.

## 3. Nummernkreis

1. Kläger verwendet regelmäßig K, Beklagter B.
2. Antragsteller und Antragsgegner verwenden nur dann AST und AG, wenn Gericht oder Kanzleistandard dies vorsieht.
3. Replik, Duplik und nachgelassener Schriftsatz führen den höchsten bestehenden Nummernkreis fort.
4. Unteranlagen erhalten nur bei einem einheitlichen Beweisthema eine erkennbare Untergliederung.
5. Jede Seite einer Anlage trägt rechts oben dieselbe sichtbare Bezeichnung; Inhalt darf nicht überdeckt werden.

## 4. PDF- und Dateiproduktion

Konvertiere Hauptdokument und Anlagen einzeln in PDF. Vergleiche jede konvertierte Seite visuell mit dem Original. Prüfe Seitenzahl, Ausrichtung, OCR, Anhänge, aktive Inhalte, Kennwortschutz, Schwärzungen, Unterschriftsseiten und Hashwerte.

Gerichtshinweis geht vor. Fehlt er, verwende den dokumentierten strengen Kanzleistandard: ASCII, Unterstriche, logische Reihenfolge und höchstens 60 Zeichen einschließlich Endung. Beispiel: `03_20260710_AnlageK3_Nachtrag.pdf`. Stelle nicht dar, Umlaute seien bundesrechtlich verboten; die ERVB 2025 erlaubt sie und begrenzt Dateinamen auf 90 Zeichen.

Eine Nachricht betrifft genau ein Verfahren. Hauptdokument und Anlagen werden als einzelne PDFs beigefügt, nicht als ZIP und nicht kennwortgeschützt. Nach ERVB 2025 sind höchstens 1000 Dateien und insgesamt 200 MB vorgesehen.

## 5. Signatur und Eingang

Das formbedürftige Hauptdokument benötigt entweder eine qualifizierte elektronische Signatur der verantwortenden Person oder deren einfache Signatur mit persönlichem Versand über den eigenen sicheren Übermittlungsweg. Anlagen benötigen keine eigene Signatur.

Verifizierte Anker:

- BGH, Beschluss vom 7. Mai 2024, VI ZB 22/23: Bei einfacher Signatur müssen verantwortende Person und tatsächlicher Versender übereinstimmen.
- BGH, Beschluss vom 30. Januar 2024, VIII ZB 85/22: Ausgangskontrolle muss die gerichtliche Eingangsbestätigung erfassen.
- BGH, Beschluss vom 24. April 2025, III ZB 12/24: Die Eingangsbestätigung ist mit ausreichender Reaktionsreserve abzurufen und zu prüfen.
- BGH, Beschluss vom 25. Februar 2025, VI ZB 19/24: Eine Ersatzeinreichung verlangt eine geschlossene technische Darstellung; eine pauschale Störungsformel genügt nicht.
- OLG Brandenburg, Beschluss vom 23. August 2022, 12 U 113/22: Frist erst löschen, wenn `request executed` und `erfolgreich` dokumentiert sind.

## 6. Auslieferung

Liefere `versandfertig/` mit Hauptdokument und Einzelanlagen sowie `intern/` mit Anlagenverzeichnis, Zuordnungsmatrix, Hashmanifest, Preflight-Bericht, Freigabevermerk und Vorlage für die Eingangskontrolle. Grün bedeutet nur bereit für die anwaltliche Schlussprüfung und den persönlichen Versand; löse keinen Versand aus.
