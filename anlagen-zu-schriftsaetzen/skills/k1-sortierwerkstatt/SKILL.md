---
name: k1-sortierwerkstatt
description: "K1-Leitanlage sortieren: Vertrag, Auftrag, Nachtrag, E-Mail-Anhang, Scan, OCR-Fassung und spätere Ergänzungen zu einer gerichtstauglichen Anlage K1 oder einem K1-Konvolut ordnen."
---

# K1-Sortierwerkstatt

## Normenanker

Arbeitsfokus: **K1-Sortierwerkstatt**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

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

Dieser Skill entscheidet, was bei einer großen Akte wirklich `Anlage K1` sein soll. Er verhindert, dass die wichtigste Anlage aus fünf Fassungen, einem schlechten Scan und einer halb vergessenen Bestätigungsmail besteht, ohne dass Gericht oder Gegner verstehen, welche Fassung maßgeblich ist.

## Mindestinput

- Ziel-Schriftsatz und Parteirolle.
- Alle potentiellen K1-Dateien mit Dateinamen, Datum, Quelle und kurzer Inhaltsbeschreibung.
- Angabe, welche Tatsachenbehauptung K1 beweisen soll.
- Hinweis, ob Einzelanlage oder Konvolut gewünscht ist.

## Arbeitsablauf

1. Bestimme den Beweiszweck von K1 in einem Satz.
2. Trenne gerichtliche Fassung, bloße Vorversion, E-Mail-Transporthülle, OCR-Arbeitsfassung und interne Notiz.
3. Entscheide Einzelanlage oder Konvolut; bei Konvolut Reihenfolge und Untergliederung festlegen.
4. Formuliere einen Schriftsatzanker, der K1 im Vortrag sauber einführt.
5. Erzeuge Dateinamen, Deckblatttext, Anlagenverzeichniszeile und interne Versionennotiz.

## Ausgabe

- K1-Entscheidung mit kurzer Begründung.
- Deckblatt für `Anlage K1` oder `K1-Konvolut`.
- Tabelle: Datei, Rolle, Status, gerichtliche Fassung ja/nein.
- Schriftsatzbaustein zur Einführung der Anlage.

## Typische Fehler, die du aktiv suchst

- K1 enthält mehrere Dokumente ohne gemeinsamen Beweiszweck.
- Unterschriebene Fassung und Entwurf werden verwechselt.
- Scan und OCR-Fassung werden als zwei verschiedene Anlagen gezählt.
- Der Schriftsatz zitiert nur K1, braucht aber K1.3.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.
