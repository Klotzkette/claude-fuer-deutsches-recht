---
name: belegkette-rueckverfolgung
description: "Belegkette fuer Forderungen und Zahlungen zurueckverfolgen: Originalbeleg, Buchung, Zahlung. Normen: §§ 238 257 HGB, §§ 174 ff. InsO. Pruefraster: Belegverknuepfung, fehlende Belege, Doppelbuchungen. Output: Belegketten-Uebersicht. Abgrenzung: nicht Excel-Export."
---

# /tabellenreview-3d:belegkette-rueckverfolgung


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- BGH, Urt. v. 26.01.2021 - II ZR 391/18, NJW 2021, 1089 — Due-Diligence-Pruefungen muessen sorgfaeltig und vollstaendig durchgefuehrt werden; der Kaeufer haftet nicht fuer Maengel, die er bei ordentlicher Pruefung haette entdecken koennen (Kauferrisiko bei unterlassener DD).
- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Der Anwalt muss das Ergebnis einer automatisierten Pruefung verantworten; er haftet fuer Fehler auch wenn er ein Hilfsmittel eingesetzt hat; die abschliessende Pruefung obliegt dem zugelassenen BerufsTraeger.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Pruefberichte muessen hinreichend dokumentiert sein; Bausteine die spaeter nicht mehr nachvollzogen werden koennen, belasten die Haftungslage des Anwalts.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Das Gebot der Nachvollziehbarkeit rechtlicher Dokumentation gilt auch im wirtschaftsrechtlichen Due-Diligence-Kontext; lueckenlose Belegketten schuetzen vor Haftungsrisiken.


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
