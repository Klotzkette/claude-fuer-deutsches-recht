---
name: anlagen-duplikate-versionen-hashlog
description: "Erkennt doppelte Dateien, verschiedene Fassungen desselben Dokuments, OCR-Kopien, E-Mail-Anhänge und manipulativ wirkende Metadatenbrüche; erzeugt ein Hash- und Versionenprotokoll."
---

# Duplikate, Fassungen und Hashlog

## Normenanker

Arbeitsfokus: **Duplikate, Fassungen und Hashlog**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — Schriftsatzanforderungen.
- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 131 Abs. 1 ZPO` — Beifügung von Abschriften/Anlagen.
- `§ 133 Abs. 1 ZPO` — Abschriften für Zustellung.
- `§ 138 Abs. 1 ZPO` — Tatsachenvortrag.
- `§ 253 Abs. 2 ZPO` — Klageinhalt.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.
- `§ 371 Abs. 1 ZPO` — Augenschein.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Zweck

Dieser Skill macht die stille technische Kontrolle hinter dem Anlagenverzeichnis. Er entscheidet nicht materiell-rechtlich, aber er zeigt, ob die Anlagenbasis stabil genug ist, um gerichtsfest verwendet zu werden.

## Mindestinput

- Dateiliste mit Größe, Datum, Quelle und optional Hash.
- Hinweis, welche Fassungen bereits im Schriftsatz zitiert sind.
- Optional: E-Mail-Header oder DMS-Export.

## Arbeitsablauf

1. Gruppiere identische, ähnliche und wahrscheinlich zusammengehörige Dateien.
2. Trenne Original, Arbeitskopie, OCR, Scan, Vorschau, Screenshot und E-Mail-Anhang.
3. Markiere widersprüchliche Datums-/Versionssignale.
4. Bestimme die gerichtliche Fassung pro Dokumentfamilie.
5. Erzeuge Hashlog und Änderungsnotiz.

## Ausgabe

- Hash-/Duplikatlog als CSV/Markdown-Tabelle.
- Fassungsentscheidung pro Dokumentfamilie.
- Warnliste für Metadaten-/Authentizitätsrisiken.
- Vorschlag, welche Dateien nicht eingereicht werden.

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.
