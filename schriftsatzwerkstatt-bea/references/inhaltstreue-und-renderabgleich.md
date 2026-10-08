# Inhaltstreue und Renderabgleich

Stand: 29.07.2026

Diese Referenz schützt den bereits fachlich freigegebenen Inhalt während der technischen Endfertigung. Sie enthält keine Rechtsprüfung und keine Rechtsprechungsanker.

## 1. Unveränderlicher Ausgangspunkt

Vor der Konvertierung werden Hauptfassung und Anlagenquellen über Pfad, Dateigröße, Änderungszeitpunkt und SHA-256 festgehalten. Bei mehreren Fassungen muss eine reale verantwortliche Person die führende Quelle bezeichnen. Die Werkstatt entscheidet nicht nach dem vermeintlich besseren juristischen Inhalt.

## 2. Zulässige technische Änderungen

Zulässig sind nur dokumentierte Änderungen, die für eine lesbare, eindeutige oder technisch verarbeitbare Arbeitskopie erforderlich sind:

- PDF-Erzeugung aus der gesperrten Quelle;
- Festlegung von Druckbereich, Seitengröße und Leserichtung;
- OCR als zusätzliche Textebene ohne Ersetzen des sichtbaren Bildes;
- Drehung, Entzerrung und Zuschnitt leerer Scanränder;
- sichtbare Anlagenkennzeichnung außerhalb des vorhandenen Inhalts;
- ASCII-Dateiname und geordnete Upload-Reihenfolge.

## 3. Unzulässige Inhaltsänderungen

Ohne erneute fachliche Freigabe sind insbesondere gesperrt:

- Änderung von Antrag, Betrag, Datum, Partei, Gericht, Aktenzeichen oder Frist;
- sprachliche Glättung, Ergänzung oder Kürzung juristischer Ausführungen;
- Austausch, Löschung oder Zusammenfassung von Anlagen;
- Korrektur einer vermeintlich falschen Norm, Fundstelle oder Bezeichnung;
- stilles Entfernen von Kommentaren, Änderungsverfolgung, Platzhaltern oder verstecktem Text, wenn deren Bedeutung nicht durch die verantwortliche Person geklärt ist;
- Ersetzen einer schlecht lesbaren Passage durch eine geschätzte Transkription.

Ein solcher Befund führt zum Stopp und zur Rückgabe an die verantwortliche Person.

## 4. Drei-Wege-Abgleich

Für Hauptschriftsatz und jede Anlage werden drei Zustände verglichen:

| Ebene | Prüffrage | Mindestnachweis |
|---|---|---|
| Quelle | Ist dies die freigegebene Datei? | Quellpfad, Quellhash, Freigabeperson |
| PDF-Struktur | Wurde die Datei vollständig und in richtiger Reihenfolge konvertiert? | Seitenzahl, Text-/Bildstatus, Ausgabehash |
| Sichtbild | Ist alles lesbar und unverändert sichtbar? | Seitenprotokoll mit 100-Prozent-Sichtkontrolle |

Bei Office-Dateien werden zusätzlich Überschriften, Tabellen, Fußnoten, Seitenumbrüche, Kopf-/Fußzeilen, Unterschriftsblock und Anlagenzitate stichprobenartig gegen die Quelle verglichen. Bei Tabellen sind Formelergebnis, ausgeblendete Zeilen/Spalten, Druckbereich und Wiederholungszeilen zu kontrollieren. Bei E-Mails müssen Absender, Empfänger, Datum, Betreff, Nachrichtentext und einbezogene Anhänge erkennbar bleiben.

## 5. Delta-Protokoll

Jede technische Veränderung erhält genau einen Eintrag:

| Datei | Quelle/Hash | Änderung | Grund | Werkzeugprofil | Ergebnis/Hash | Sichtstatus | Prüfer |
|---|---|---|---|---|---|---|---|

Ein leerer Delta-Eintrag bedeutet nicht automatisch Inhaltstreue. Die Sichtprüfung bleibt Pflicht.

## 6. Freigaberegel

Das Paket bleibt rot, wenn Quellfassung, Seitenvollständigkeit, Anlagenzuordnung oder sichtbarer Inhalt nicht sicher verglichen werden können. Die Werkstatt darf dann eine Fehlerkarte und konkrete Rückfrage ausgeben, aber keine fachliche Ersatzentscheidung treffen.
