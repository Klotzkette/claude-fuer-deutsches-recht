---
name: hauptdokument-pdf-endfertigen
description: "Endfertigt den bereits freigegebenen Schriftsatz technisch als separates PDF: sichert die maßgebliche Quelldatei, konvertiert ohne inhaltliche Umschreibung, prüft Rubrum, Anträge, Seitenfolge, einfache Signatur, Schriften, Umbrüche, Metadaten und aktive Inhalte und liefert die visuell kontrollierte Datei mit dokumentiertem Hash."
---

# Hauptdokument als PDF endfertigen

## 1. Grenze

Bearbeite nur die technische Endfassung. Ändere keinen Antrag, Tatsachenvortrag, Betrag, Namen oder Termin ohne ausdrückliche Freigabe. Ein entdeckter Inhaltswiderspruch wird gemeldet, nicht still korrigiert.

## 2. Konvertierung

1. Quellhash und Fassungsstand protokollieren.
2. DOC, DOCX, ODT oder RTF mit LibreOffice headless in PDF ausgeben; vorhandene PDF unverändert in den Arbeitsbereich kopieren.
3. keine Druckdialoge verwenden, die Kommentare, Änderungsverfolgung oder ausgeblendete Ebenen unkontrolliert einbeziehen.
4. Ergebnis erneut öffnen und mit der Quelle vergleichen.

## 3. Sichtkontrolle

Prüfe jede Seite, mindestens aber systematisch:

| Kontrollpunkt | Erwartung |
| --- | --- |
| Rubrum | Gericht, Parteien, Aktenzeichen und Parteistellung vollständig sichtbar |
| Anträge | keine abgeschnittene Zeile, keine verlorene Nummerierung |
| Seiten | richtige Reihenfolge, keine Leer- oder Doppelseite |
| Fußzeile | Seitenzahl und Kanzleiangaben nicht überlagert |
| Tabellen/Bilder | vollständig, lesbar und nicht über den Rand verschoben |
| Formroute | bei einfacher Signatur Name der verantwortenden Person am Dokumentende; bei qES gesonderter Prüfnachweis für die finale Datei |
| PDF | unverschlüsselt, druckbar, ohne eingebettete Dateien oder ausführbare Inhalte |

## 4. Benennung

Das Hauptdokument beginnt mit `00_`, enthält Datum und Dokumentart und endet mit `.pdf`, etwa `00_20260714_Klageerwiderung_12_O_34_26.pdf`. Nutze ASCII, Unterstriche und höchstens 80 Zeichen einschließlich Endung.

## 5. Übergabe

Liefere Dateiname, Seitenzahl, Bytes, SHA-256, Quellfassung, Sichtprüfer und Prüfergebnis. Leite die Formentscheidung an `signaturweg-und-absender-pruefen` weiter; ein sichtbarer Namenszug allein entscheidet die Signaturroute nicht.
