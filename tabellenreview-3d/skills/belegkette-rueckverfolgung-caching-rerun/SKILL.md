---
name: belegkette-rueckverfolgung-caching-rerun
description: "Belegkette für Forderungen und Zahlungen zurückverfolgen: Originalbeleg, Buchung, Zahlung. Normen: §§ 238 257 HGB, §§ 174 ff. InsO. Prüfraster: Belegverknuepfung, fehlende Belege, Doppelbuchungen. Output: Belegketten-Übersicht. Abgrenzung: nicht Excel-Export im Tabellenreview 3d."
---

# /tabellenreview-3d:belegkette-rueckverfolgung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

