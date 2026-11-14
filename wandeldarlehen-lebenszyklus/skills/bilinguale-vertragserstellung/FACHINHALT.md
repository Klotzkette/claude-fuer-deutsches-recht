---
name: bilinguale-vertragserstellung
description: "Für Bilinguale Vertragserstellung DE/EN: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Bilinguale Vertragserstellung DE/EN

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB-Formvorschriften oder GmbHG aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Normen-Ergänzung

Paragrafen 133 und 157 BGB (Auslegung mehrdeutiger Verträge) → Artikel 3 Rom-I-VO (Rechtswahl) → Paragraf 5 BeurkG (Urkundssprache) → Paragraf 55 Absatz 1 GmbHG (Form der Übernahmeerklärung). Gerichtssprache nach Paragraf 184 GVG und Urkundssprache nicht vermischen.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
