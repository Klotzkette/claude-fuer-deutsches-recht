---
name: belegkette-rueckverfolgung
description: "Sichert die Belegkette jeder Zelle des Wuerfels — von der Antwort ueber das woertliche Zitat bis zur Originalstelle im Quelldokument mit Seite Absatz und Datei-Hash. Erkennt Belegkette-Brueche (Datei-Hash weicht ab / Zitat nicht im Originaltext auffindbar / Fundstelle ausserhalb des Dokuments). Erlaubt umgekehrte Suche: 'welche Zellen zitieren Seite 14 von Vertrag-042?' Generiert `belegkette.csv` mit allen Zitaten plus Fundstellen plus Dokumenten-Hashes als Pflichtanhang zur Mandatsuebergabe."
---

# /tabellenreview-3d:belegkette-rueckverfolgung

## Zweck

Eine Tabellenzelle die behauptet etwas zu sagen ohne dass man die Stelle im Dokument findet ist wertlos. Schlimmer: gefährlich. Dieser Skill macht jede Zellaussage rückverfolgbar.

## Komponenten der Belegkette

1. **Antwort** — was in der Zelle steht
2. **Woertliches Zitat** — in Anführungszeichen, exakter Wortlaut aus dem Dokument
3. **Fundstelle** — Datei-ID, Seite, Absatz, ggf. Ziffer und Buchstabe
4. **Datei-Hash** — SHA-256 der Quelldatei zum Zeitpunkt der Befuellung
5. **OCR-Konfidenz** — bei gescannten Dokumenten, für die Seite der Fundstelle
6. **Prompt-Version** — welcher Spaltenprompt zur Befuellung verwendet wurde

## Prüfung gegen Original

Beim Erstellen oder beim späteren Audit:

- **Hash-Prüfung:** ist der Datei-Hash der Quelldatei noch derselbe wie beim Befuellzeitpunkt? Wenn nein: `hash-bruch` im `audit-trail-protokoll`.
- **Volltext-Suche:** ist das wörtliche Zitat noch im Volltext der Datei auffindbar? Wenn nein: `zitat-nicht-mehr-im-original`.
- **Seitenkonsistenz:** existiert die angegebene Seite überhaupt in der Datei? Wenn nein: `fundstelle-außerhalb-dokument`.

## Umgekehrte Suche

Frage: 'Welche Zellen zitieren aus Seite 14 von Vertrag-042?' — der Index erlaubt diese Suche in beide Richtungen.

Anwendungsfälle:
- Vertrag wird geändert: welche Zellen müssen neu geprüft werden?
- Prüfer findet Fehler in Zelle X: welche anderen Zellen könnten aus derselben Stelle abgeleitet sein?
- Dokument wird nachgereicht: gibt es bereits Zellen die diese Stelle hatten?

## Pflichtanhang zur Mandatsübergabe

`belegkette.csv` mit Spalten:

```
zelle-id, arbeitsblatt, zeile, spalte, antwort, woertliches-zitat, datei-id, datei-hash, seite, absatz, ocr-konfidenz, prompt-version
```

Diese Datei MUSS bei jeder Mandatsübergabe mitgehen. Sie ist die Reproduzierbarkeits-Bescheinigung des Würfels.

## Grenzen

- Bei geänderten Dokumenten (Vertragsversion 2 überschreibt Version 1) erhält die Belegkette die alte Fassung — der Prüfer entscheidet ob neu zu rechnen ist.
- Bei OCR-Fehlern (Zitat hat OCR-Wortwahl die im Original anders steht) kann die Volltextsuche fehlschlagen — das ist ein bekannter OCR-Falschalarm, kein Belegkette-Bruch.
