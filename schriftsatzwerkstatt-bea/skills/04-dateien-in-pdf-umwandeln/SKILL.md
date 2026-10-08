---
name: 04-dateien-in-pdf-umwandeln
description: 'Erzeugt aus einem fertigen Schriftsatz und gemischten Anlagen separate gerichtstaugliche PDF-Arbeitskopien. Verwenden für DOCX, ODT, XLSX, CSV, EML, MSG, JPEG, PNG, TIFF, Scan und vorhandene PDF. Behandelt Office-Layout, Tabellen-Druckbereiche, E-Mail-Kopfzeilen, Bildausrichtung, OCR und Anhänge formatspezifisch. Originale bleiben unverändert; Dateiendungen werden niemals nur umbenannt.'
---

# Dateien in einzelne PDFs umwandeln

## Zweck und Anwendungsfall

Dieser Skill produziert die PDF-Arbeitskopien für Hauptschriftsatz und Anlagen. Jede Quelle bleibt unverändert. Konvertierung bedeutet echtes Rendern mit anschließender Sichtprüfung, niemals das Austauschen einer Dateiendung.

## Eingaben

- gesperrte Hauptquelle aus Skill 02.
- Anlagenplan aus Skill 03.
- gewünschtes beziehungsweise vorhandenes Layout.
- verfügbare Office-, PDF-, Bild- und OCR-Werkzeuge.
- Entscheidung zu E-Mail-Anhängen, ausgeblendeten Tabellenblättern und bereits signierten PDFs.

## Ablauf / Checkliste

1. Für jede Quelle Format, Dateizustand, erwartete Seiten und geeignetes Konvertierungswerkzeug festlegen.
2. Ausgabe ausschließlich unter `_bea_ausgabe`; keine Quelle überschreiben.
3. **DOC/DOCX/ODT/RTF:** mit einem stabilen Renderer und verfügbaren Schriften rendern; Briefkopf, Kopf-/Fußzeilen, Seitenzahlen, Tabellen, Fußnoten, Felder, verknüpfte Bilder und Umbrüche vergleichen. Änderungsverfolgung und Kommentare müssen vorher geklärt sein.
4. **XLS/XLSX/ODS/CSV:** relevante und ausgeblendete Blätter, Zeilen und Spalten, Formeln, externe Datenverbindungen, Druckbereich, Orientierung, Skalierung, wiederholte Kopfzeile und Seitenumbrüche prüfen. Keine Tabelle bis zur Unlesbarkeit auf eine Seite verkleinern.
5. **EML/MSG:** Absender, Empfänger, CC, Datum, Zeitzone, Betreff und Nachrichtentext lesbar rendern. Relevante Anhänge und eingebettete Nachrichten separat inventarisieren und konvertieren; nicht unbemerkt in der E-Mail-PDF verschwinden lassen.
6. **JPEG/PNG/TIFF/HEIC:** EXIF-Ausrichtung, Zuschnitt, Auflösung, Farbkontrast und vollständige Bildfläche prüfen; proportional auf PDF-Seite setzen.
7. **Scan:** Seiten drehen, Reihenfolge prüfen und OCR-Schicht ergänzen, ohne sichtbares Bild zu ersetzen. Unsichere OCR ändert den Bildinhalt nicht.
8. **Vorhandene PDF:** nicht unnötig neu rendern. Passwort, Verschlüsselung, eingebettete Dateien, Skripte, Formulare und Signaturen prüfen. Signierte PDFs nur nach dokumentierter Entscheidung verändern.
9. **ZIP/sonstige Container:** im Arbeitsbereich entpacken und Inhalte einzeln behandeln; Container nicht als Gerichtsdatei übernehmen.
10. **PPT/PPTX und sonstige Formate:** nur mit verlässlichem Renderer und Seitenvergleich übernehmen. Andernfalls rot stoppen und das benötigte Exportformat konkret nennen.
11. Unveränderte grüne Arbeitskopien nur bei identischem Quellhash, Konvertierungsprofil, Werkzeugstand und Ausgabehash wiederverwenden. Neue oder geänderte Quellen neu rendern.
12. Jede Arbeitskopie zunächst unter einem eindeutigen temporären Namen im Arbeitsordner schreiben, vollständig schließen und prüfen und erst danach atomar auf den Zielnamen verschieben. Teil- oder Timeout-Dateien gelangen nie in `upload`.
13. Externe Konverter mit einem vor dem Lauf festgelegten Zeitlimit je Datei und eigenem temporären Arbeitsverzeichnis starten. Bei Timeout Prozess beenden, Quelle und Werkzeug rot protokollieren und mit der nächsten unabhängigen Datei fortfahren.
14. Voneinander unabhängige Dateien mit höchstens vier Arbeitsaufträgen parallel bearbeiten. Ein Konvertierungsstapel umfasst höchstens 20 Dateien; Fehler einer Datei als Einzelbefund zurückgeben, ohne den Lauf der übrigen Dateien hängen zu lassen.
15. Nach jedem Stapel die Fortsetzungsmarke aus Skill 01 mit verarbeiteten Zielhashes und offenen Dateien aktualisieren. Cachetreffer nicht erneut rendern oder als Volltext ausgeben.
16. Konvertierungsprotokoll nach der [Vorlage](../../templates/konvertierungsprotokoll.md) mit Quelle, Quellhash, Werkzeug/Version, Profil, Ausgabe, Seiten vor/nach, Warnungen, Ausgabehash und Delta-Entscheidung erzeugen.

## Quellenpflicht

Format und Paketgrenzen folgen dem [ERV-Versandstandard](../../references/erv-versandstandard.md); Delta-Regeln dem [Dateinamen- und Manifeststandard](../../references/dateinamen-und-manifest.md); Quellbindung und Sichtvergleich dem [Inhaltstreue- und Renderabgleich](../../references/inhaltstreue-und-renderabgleich.md); formatspezifische Stopps dem [100-Punkte-Fehlerkatalog](../../references/100-punkte-fehlerkatalog.md). Es gibt keine fachrechtliche Prüfung und keine Rechtsprechungsanker.

## Ausgabeformat

1. eine separate PDF-Arbeitskopie je Hauptdokument und Anlage.
2. kompakte Konvertierungstabelle mit höchstens sieben Spalten; Quell-/Ausgabehash und Werkzeugdetails stehen getrennt im technischen Protokoll.
3. Liste separat behandelter E-Mail-/Containeranhänge.
4. rote Fehler und gelbe Sichtprüfpunkte.
5. Fortsetzungsmarke und Übergabe an Skill 05.

Das Konvertierungsprotokoll beschreibt Abweichungen in vollständigen Sätzen. Ein bloßes `konvertiert` ohne Seiten- und Sichtkontrolle ist kein fertiges Ergebnis.

## Beispiele

- Excel-Mietkonto mit zwölf Spalten: Querformat und lesbare mehrseitige Ausgabe statt Ein-Seiten-Miniatur.
- EML mit zwei Anhängen: E-Mail-Körper als PDF plus beide Anhänge als eigene Anlagenkandidaten.
- signierte Bestands-PDF: unverändert behalten; Anlagenkennzeichnung nur nach Signaturentscheidung.
