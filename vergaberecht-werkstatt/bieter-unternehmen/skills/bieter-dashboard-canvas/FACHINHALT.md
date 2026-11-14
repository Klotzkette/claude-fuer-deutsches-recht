---
name: bieter-dashboard-canvas
description: "Bieter-Dashboard aus vorhandener Vergabeakte erzeugen: verbindet Termine, Unterlagenstand, Angebotsaufgaben, Eignungsbelege, Qualitätsargumente, Portalabgabe, Rügepunkte, Rechtsweg und Verantwortliche in einer täglichen Steuerungsansicht."
---

# Bieter-Dashboard für den laufenden Vergabefall

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Akte automatisch erfassen

Vor Rückfragen Ordner, ZIP, Portalexport, Bekanntmachung, Unterlagen, Antworten, Angebotsentwürfe, Quittungen und Schreiben auslesen. Dubletten nach Hashwert erkennen, Dokumentversionen ordnen und Widersprüche markieren. Nur echte Lücken abfragen.

## Dashboard-Ansichten

### 1. Fristenleiste

| Ereignis | Datum/Uhrzeit | Zeitzone | Auslöser | sichere interne Frist | Beleg | Status |
|---|---|---|---|---|---|---|

Angebots-, Frage-, Bindefrist, §-134-Stillhaltefrist, Rügefristen des § 160 Abs. 3 GWB und etwaige Rechtsbehelfsfristen getrennt führen. Änderungen überschreiben nicht den bisherigen Stand.

### 2. Dokumenten- und Anforderungsmatrix

| Anforderung | Fundstelle | Muss/Wertung/Vertrag | Eigentümer | Datei/Angebotsstelle | Prüfung | offen |
|---|---|---|---|---|---|---|

### 3. Bestangebots-Board

Preis, Qualität, Geschwindigkeit, Personal, Nachhaltigkeit, Betrieb und Risiko je Kriterium mit zugesagtem Mehrwert, Beleg und Punktprognose ausweisen. Nicht nur den Preis optimieren; keine Eignung als Angebotsqualität doppelt verwerten.

### 4. Rechtsschutz-Board

| Angriff | Kenntnis/Erkennbarkeit | subjektives Recht | Schaden | Beleg | Abhilfe | Rüge bis |
|---|---|---|---|---|---|---|

### 5. Abgabe-Board

Dateiname, Format, Größe, Signatur, Portalziel, Uploadstatus, Vier-Augen-Prüfung und Quittung. Nach Angebotsfreeze jede Inhaltsänderung sperren; nur technisch identische Enddateien hochladen.

## Ampellogik

`rot` bedeutet Frist, Muss-Anforderung oder Rechtsverlust unmittelbar gefährdet; `gelb` bedeutet fehlender Beleg oder ungelöster Widerspruch; `grün` setzt geprüfte Datei und Fundstelle voraus. Jede Kachel zeigt genau einen Verantwortlichen und nächsten Termin.

## Pflichtoutput

1. Kompaktes Startdashboard und fünf Detailansichten.
2. Priorisierte Aufgabenliste für heute, nächste 48 Stunden und Restlaufzeit.
3. Entscheidungsliste `Go | Klärungsfrage | Rüge | No-Go`.
4. Download-/Uploadmanifest mit Versionen und Hashwerten.
5. Änderungsprotokoll, damit kein stiller Statusverlust eintritt.
