---
name: dateinamen-und-paketgrenzen-pruefen
description: "Vergibt robuste, sprechende beA-Dateinamen mit ASCII, Unterstrichen, logischer Reihenfolge und höchstens 80 Zeichen einschließlich Endung, prüft jede Datei gegen die ERVB-Höchstgrenze von 90 Zeichen sowie die Nachrichtengrenzen von 1.000 Dateien und 200 MB und erstellt bei Bedarf einen lückenlosen, quittierbaren Mehrteil-Versandplan."
---

# Dateinamen und Paketgrenzen prüfen

## 1. Regeln

Die ERVB 2025 erlaubt höchstens 90 Zeichen einschließlich Dateiendung, höchstens 1.000 Dateien und höchstens 200 MB je Nachricht. Dieses Plugin nutzt vorsorglich:

1. höchstens 80 Zeichen einschließlich `.pdf`,
2. ausschließlich `A-Z`, `a-z`, `0-9` und Unterstrich im Stamm,
3. keine Leerzeichen, Umlaute, scharfes S, Klammern oder Sonderzeichen,
4. zweistellige, bei mindestens 100 Dateien dreistellige logische Reihenfolge,
5. sprechenden Inhalt nach Dokumentart oder Anlagenkennung.

## 2. Transliteration

Das beA-Handbuch nennt für gewöhnliche Anhänge eine engere Anwendungsgrenze von 84 Zeichen, für Signaturdateien 90 Zeichen einschließlich aller Endungen. Das interne 80-Zeichen-Profil bleibt für PDFs darunter. Eine anschließende Signaturendung ebenfalls mitzählen; nicht auf eine automatische Umbenennung im Versanddialog vertrauen.

`ä` wird `ae`, `ö` wird `oe`, `ü` wird `ue`, `ß` wird `ss`. Mehrere Trennzeichen werden zu einem Unterstrich. Kürze zuerst Füllwörter und erst danach die Sachbezeichnung. Anlagenkennung und Dateiendung dürfen nie abgeschnitten werden.

## 3. Muster

```text
00_20260714_Klageerwiderung_12_O_34_26.pdf
01_20260714_AnlageB1_Kaufvertrag.pdf
02_20260714_AnlageB2_E_Mail_Abnahme.pdf
```

## 4. Paketierung

Berechne Anzahl und Bytes aus den finalen Dateien, nicht aus Quellen oder Schätzungen. Wird eine Grenze erreicht, bilde Teilnachrichten mit Sicherheitsreserve. Teile keine mehrseitige Anlage. Halte Hauptdokument, Anlagenverzeichnis und den zuerst benötigten Anlagenbereich logisch zusammen.

Strukturdaten, Nachrichtentext und Signaturdateien zählen mit. Die Ordnergröße allein prüft daher noch nicht die fertige Nachricht. Das Werkzeug rechnet vorsorglich mit 200 Millionen Bytes und warnt ab 190 Millionen Bytes oder 950 Dateien; diese Reserve ist eine Kanzleiregel, keine zusätzliche gesetzliche Grenze. Eine darüber hinaus nötige Aufteilung im Versanddialog kontrollieren.

| Teil | Dateien | Anlagenbereich | Bytes | Begleittext | Eingangsbestätigung |
| --- | --- | --- | --- | --- | --- |
| 1 von 2 | Zahl | B 1 bis B 40 | Zahl | fertig | offen |

Für jede Nachricht ist eine eigene Eingangskontrolle nötig. Übergib Dateiliste und Versandplan an `versandfreigabe-und-eingang-sichern`.
