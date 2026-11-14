---
name: anlagen-fuer-bea-versand
description: "Bereitet vorhandene Anlagen tatsächlich für den beA-Versand vor: liest zuerst Schriftsatz und Ordner, setzt den bisherigen Nummernkreis fort, konvertiert jede Anlage kontrolliert in eine eigene PDF, stempelt sämtliche Seiten oben rechts, erstellt sichere Dateinamen und liefert Versandordner, Anlagenverzeichnis, Preflight-Bericht und Lückenliste."
---

# Anlagen für beA-Versand

## 1. Direktstart

Liegt Material vor, beginne mit der Zuordnung und nicht mit einem Interview. Lies sämtliche Anlagenzitate aus dem Schriftsatz, ordne die vorhandenen Dateien zu und liefere die erste Belegmatrix. Frage nur nach der Prozessrolle oder der letzten bereits eingereichten Anlagenziffer, wenn dies nicht aus der Akte folgt.

## 2. Produktionsfolge

1. Schriftsatzbezug und Beweisthema jeder Anlage festhalten.
2. Fehlende, doppelte, alte oder widersprüchliche Dateien ausweisen.
3. K-, B-, AST- oder AG-Nummern fortsetzen; bei Replik oder Duplik nicht neu beginnen.
4. Arbeitsdateien kontrolliert in PDF konvertieren und das Ergebnis visuell prüfen.
5. Auf jeder Seite oben rechts die vollständige Anlagenbezeichnung anbringen.
6. Dateinamen nach Gerichtshinweis oder dokumentiertem Sicherheitsprofil erzeugen.
7. Einzel-PDFs, Anlagenverzeichnis, Hashmanifest und Preflight-Bericht ausgeben.

## 3. Technikwerkzeug

Für lokale Dateien nutze `../anlagen-zu-schriftsaetzen/werkzeuge/build_anlagenkonvolut.py`. Ein typischer Lauf lautet:

```bash
python3 werkzeuge/build_anlagenkonvolut.py \
  --eingang ./anlagen \
  --hauptdokument ./Schriftsatz_final.docx \
  --ausgang ./bea-versandmappe \
  --praefix K \
  --dokumentart Replik \
  --profil berlin \
  --datum 20260710 \
  --gericht "Landgericht Berlin II" \
  --aktenzeichen "12 O 34/26" \
  --strict
```

Der Eingangsname einer Anlage folgt `Anlage_K-01_Kaufvertrag.pdf` oder derselben Kennung mit einer unterstützten Office- oder Bildendung. Das Werkzeug versendet nichts und ersetzt keine Sichtkontrolle.

## 4. Formanker

- ZPO Paragraf 130a Absatz 3: Signatur des Hauptdokuments; Anlagen benötigen keine eigene Signatur.
- ZPO Paragraf 130a Absatz 5: Eingang und automatisierte Eingangsbestätigung.
- ZPO Paragraf 130d: Nutzungspflicht und Ersatzeinreichung bei vorübergehender technischer Unmöglichkeit.
- ERVV Paragraf 2 und ERVB 2025: PDF, technische Eignung und Nachrichtengrenzen.

## 5. Abschluss

Wechsle für Signaturweg, Freigabevermerk und Eingangskontrolle unmittelbar in `bea-versandmappe-endfertigung`. Ein grüner technischer Preflight allein bedeutet noch keine anwaltliche Versandfreigabe.
