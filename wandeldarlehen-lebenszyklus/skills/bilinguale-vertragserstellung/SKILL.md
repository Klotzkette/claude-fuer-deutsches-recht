---
name: bilinguale-vertragserstellung
description: "Bilinguale Erstellung DE/EN des Wandeldarlehensvertrags in zweispaltiger Tabelle (links DE verbindlich, rechts EN zur Orientierung), Sprachklausel mit Vorrang DE, standardisierte englische Uebersetzung aller Paragrafen, Unterschriftsblock mit DocuSign-Hinweis. Fuer GmbH und UG (haftungsbeschraenkt)."
---

# Bilinguale Vertragserstellung DE/EN

## Zweck

Dieser Skill erstellt den vollständigen Wandeldarlehensvertrag in bilingualer Fassung (DE/EN) als zweispaltige Word-Tabelle. Die deutsche Fassung ist allein verbindlich (§ 10.1 Sprachklausel). Phase A des Lebenszyklus.

## Eingaben

- Vollständige Parteidaten aus `parteien-erfassen`
- Konditionen aus `darlehenshoehe-konditionen`
- Wandlungsmechanik aus `wandlungsmechanik-konzipieren`
- Rangrücktrittsklausel aus `rangruecktritt-formulieren`
- Erweiterte Klauseln (Pro-rata, MFN, Liquidationspräferenz, Schiedsklausel) falls vereinbart
- Dateiformat: DOCX (python-docx), Zielordner

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform – ausreichend für Vertragsschluss)
- § 126 BGB (Schriftform – auf Verlangen zusätzlich)
- § 128 BGB (Notarielle Beurkundung – nur falls erforderlich)
- § 15 Abs. 3, Abs. 4 GmbHG (Beurkundungspflicht Anteilsübertragung)
- § 10.1 Standardklausel: Vorrang der deutschen Fassung

### Rechtsprechung
- BGH, Urt. v. 29. April 2002 – II ZR 330/00 (Formerfordernisse Gesellschafterbeschluss)
- OLG München, Beschl. v. 10. März 2016 – 31 Wx 79/16 (zweistufige Wandlung, Textform ausreichend)

## Vorgehen

### 1. Dokumentstruktur festlegen
Zweispaltige Word-Tabelle ohne Rahmenlinie: linke Spalte DE (breiter, ca. 55 %), rechte Spalte EN (ca. 45 %). Überschriften als Heading 2 in beiden Spalten. Paragrafen 0 bis 10 plus Signaturblock.

### 2. Präambel (§ 0) – beide Sprachen
DE: Gesellschaft (UG-Hintergrund, Stammkapital, Gesellschafterinnen), Unternehmensgegenstand, Finanzierungsbedarf, Wandeldarlehensstruktur, geplante Finanzierungsrunde. EN: Entsprechung mit deutschen Rechtsbegriffen in Klammern.

### 3. §§ 1 bis 3 – Darlehen, Laufzeit, Zinsen
Exakte Zahlen eintragen; keine Platzhalter [●] im ausgefüllten Vertrag. Zinssatz fünf Prozent p.a. act/360. Bankverbindung in Tabelle.

### 4. § 4 Wandlung – alle Trigger und Formel
Qualified Financing mit Schwellenwerten, Maturity, Liquidation Event. Wandlungspreis-Formel bilingual ausformulieren: CS = GK × (C / CV); alternativer Cap-Preis explizit.

### 5. §§ 5 bis 10 – Mitwirkung, Rangrücktritt, Informationsrechte, Vertraulichkeit, Form, Schluss
Vollständige Texte beidsprachig. § 6 mit BGH-Verweis auf Urt. v. 5. März 2015 – IX ZR 133/14.

### 6. Signaturblock
Vier Blöcke: Gesellschaft (Geschäftsführerin), Gesellschafterin 1, Gesellschafterin 2, Darlehensgeber. DocuSign-Hinweis: „Dieser Vertrag kann mittels qualifizierter elektronischer Signatur (z. B. DocuSign) unterzeichnet werden."

## Beispiel-Sprachklausel (§ 10.1)

```
§ 10.1 Sprachklausel. Dieser Vertrag wird in deutscher und englischer Sprache ausgefertigt.
Die deutsche Sprachfassung ist allein verbindlich. Die englische Fassung dient ausschließlich
der besseren Verständlichkeit. Im Fall von Widersprüchen geht die deutsche Fassung vor.
Die in der englischen Fassung in Klammern verwendeten deutschen Begriffe sind verbindliche
Bezugnahmen auf die deutschen Rechtsbegriffe.

Section 10.1 Language clause. This Agreement is executed in German and English.
The German version shall be the only binding version. The English version is for
convenience only. In case of inconsistency, the German version prevails.
German terms in parentheses in the English version are binding references.
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Englische Fassung weicht inhaltlich ab | Auslegungsstreit | Kleinere Abweichungen | Paralleltext konsistent |
| Fehlende Sprachklausel | Unklare Maßgeblichkeit | Mündliche Verständigung | Sprachklausel vorhanden |
| Platzhalter [●] verbleiben | Vertrag nicht unterzeichnungsreif | Einzelne Felder offen | Alle Felder ausgefüllt |
| DocuSign-Hinweis fehlt | Unterzeichner unsicher über Verfahren | Hinweis nur mündlich | Schriftlicher Hinweis |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/einsprachige-vertragsfassung-de/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/textform-vs-schriftform-vs-notariell/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/beurkundungserfordernis-pruefung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB-Formvorschriften oder GmbHG aktualisieren.
