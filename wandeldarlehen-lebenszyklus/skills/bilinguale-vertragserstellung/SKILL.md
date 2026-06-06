---
name: bilinguale-vertragserstellung
description: "Wandeldarlehensvertrag zweisprachig deutsch und englisch erstellen für internationale Transaktionen oder ausl. Investoren. BGB Darlehen §§ 488 ff. BGB GmbHG Kapitalerhohung. Prüfraster: Terminologie-Konsistenz Rechtswahl governing-law jurisdiction. Output: bilingualer Vertragsentwurf mit Gegenüberstell. Abgrenzung: nicht für einsprachige Fassung (einsprachige-vertragsfassung-de) im Wandeldarlehen Lebenszyklus: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Bilinguale Vertragserstellung DE/EN

## Arbeitsbereich

Wandeldarlehensvertrag zweisprachig deutsch und englisch erstellen für internationale Transaktionen oder ausl. Investoren. BGB Darlehen §§ 488 ff. BGB GmbHG Kapitalerhohung. Prüfraster: Terminologie-Konsistenz Rechtswahl governing-law jurisdiction. Output: bilingualer Vertragsentwurf mit Gegenüberstell. Abgrenzung: nicht für einsprachige Fassung (einsprachige-vertragsfassung-de). Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 6. Signaturblock
Vier Blöcke: Gesellschaft (Geschäftsführerin), Gesellschafterin 1, Gesellschafterin 2, Darlehensgeber. DocuSign-Hinweis: "Dieser Vertrag kann mittels qualifizierter elektronischer Signatur (z. B. DocuSign) unterzeichnet werden."

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

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 133, 157 BGB (Auslegung mehrdeutiger Verträge) → Art. 3 Rom-I-VO (Rechtswahl im Vertrag) → § 184 Abs. 2 GVG (Amtssprache Deutsch bei Gericht) → § 55 Abs. 2 GmbHG (notarielle Beurkundung auf Deutsch)

<!-- AUDIT 27.05.2026
Problem : BGH VI ZR 232/09 (NJW 2010, 2812) – WRONG_TOPIC; tatsächlich: Schadensabrechnung und Restwert nach Kfz-Unfall (§ 249 Abs. 2 BGB), kein Bezug zu zweisprachigen Verträgen. Korrekte Fundstelle: NJW 2010, 2724.
Maßnahme: Leitsatz-Zitat entfernt. Kein verifizierter BGH-Ersatz zur Sprachpriorität in zweisprachigen Verträgen gefunden; OLG München 31 Wx 79/16 (GmbHR 2016, 543) verbleibt als valide Quelle.
Quelle: https://dejure.org/2010,477
-->
