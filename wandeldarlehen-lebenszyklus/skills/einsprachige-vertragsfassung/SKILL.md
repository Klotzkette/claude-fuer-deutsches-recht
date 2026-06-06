---
name: einsprachige-vertragsfassung
description: "Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten für rein nationale Transaktionen. §§ 488 ff. BGB Darlehen §§ 55 56 GmbHG Kapitalerhohung. Prüfraster: SAFE-Konditionen BGB-Konformität Schriftformerfordernisse Investoren-Sonderrechte. Output: vollständiger Vertragsentwurf auf Deutsch. Abgrenzung: nicht für bilinguale Fassung (bilinguale-vertragserstellung) im Wandeldarlehen Lebenszyklus: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Einsprachige Vertragsfassung (nur DE)

## Arbeitsbereich

Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten für rein nationale Transaktionen. §§ 488 ff. BGB Darlehen §§ 55 56 GmbHG Kapitalerhohung. Prüfraster: SAFE-Konditionen BGB-Konformität Schriftformerfordernisse Investoren-Sonderrechte. Output: vollständiger Vertragsentwurf auf Deutsch. Abgrenzung: nicht für bilinguale Fassung (bilinguale-vertragserstellung). Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Dieser Skill erzeugt aus der bilingualen Fassung eine rein deutsche Vertragsfassung in einspaltigem, lesefreundlichem Word-Dokument. Der materielle Inhalt ist identisch – keine inhaltlichen Unterschiede. Phase A des Lebenszyklus.

## Eingaben

- Fertiger Inhalt der deutschen Spalte der bilingualen Fassung (aus `bilinguale-vertragserstellung`)
- Zieldatei: DOCX, einspaltig
- Gewünschte Schriftgröße und Zeilenabstand (Standard: Times New Roman 12 pt, 1.5-facher Zeilenabstand)
- Seitenränder: Standard 2.5 cm ringsum

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform), § 126 BGB (Schriftform)
- § 10.1 Sprachklausel (nur DE-Fassung ohne EN-Spalte – dennoch materiell identisch mit bilingualer Fassung)
- Keine gesonderten Anforderungen: Die einsprachige Fassung unterliegt denselben Formregeln wie die bilinguale Fassung.

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Extraktion der deutschen Textspalte
Aus der bilingualen Tabelle wird exakt der deutsche Text extrahiert. Keine Umformulierungen, keine Kürzungen, keine Ergänzungen.

### 2. Formatierung mit Heading-Stilen
- Heading 1: Vertragsüberschrift (z. B. "Wandeldarlehensvertrag")
- Heading 2: Paragrafenüberschriften (§ 0 Präambel, § 1 Darlehensgewährung, …)
- Heading 3: Unterabschnitte
- Normal: Vertragstext
- Tabellen: nur für Bankverbindung und Berechnungsformeln

### 3. Signaturblock
Vier separate Signaturblöcke mit Platz für Ort, Datum und Unterschrift. DocuSign-Hinweis beibehalten.

### 4. Abschließende Qualitätsprüfung
Prüfen: Alle Paragrafenverweise korrekt? Keine Querverweise auf englische Begriffe? Alle Zahlen konsistent mit bilingualer Fassung?

### 5. Dokument speichern und benennen
Dateiname nach Konvention: `Wandeldarlehen-[Gesellschaft]-[Darlehensgeber]-nur-deutsch.docx`.

### 6. Vergleich mit bilingualer Fassung
Automatischer Abgleich: Jede inhaltlich tragende Aussage der DE-Spalte muss in der einsprachigen Fassung vorhanden sein (1:1-Übertragung). Abweichungen sind Fehler.

## Beispiel-Dokumentstruktur

```
WANDELDARLEHENSVERTRAG
zwischen
[Parteien]

§ 0 Präambel
§ 1 Darlehensgewährung und Auszahlung
§ 2 Laufzeit und Rückzahlung
§ 3 Verzinsung
§ 4 Wandlung
§ 5 Mitwirkungspflichten der Gesellschafterinnen
§ 6 Qualifizierter Rangrücktritt
§ 7 Informationsrechte
§ 8 Vertraulichkeit
§ 9 Form, Beurkundung und Ausfertigung
§ 10 Schlussbestimmungen

[Signaturblock: Gesellschaft, Gesellschafterin 1, Gesellschafterin 2, Darlehensgeber]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Inhalt weicht von bilingualer Fassung ab | Zwei verschiedene Vertragsfassungen in Umlauf | Einzelne Formulierungen abweichend | Identischer Inhalt |
| Paragrafenverweise falsch | Lückenhaftes Dokument | Ein Verweis fehlerhaft | Alle Verweise korrekt |
| Signaturblock unvollständig | Unterzeichnung verhindert | Ein Block fehlend | Alle vier Blöcke vollständig |
| Schriftgröße und Layout unleserlich | Professioneller Eindruck fehlt | Geringfügige Formatmängel | Lesefreundliches Layout |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/bilinguale-vertragserstellung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/unterzeichnung-elektronisch-docusign/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/textform-vs-schriftform-vs-notariell/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB-Formvorschriften aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 133, 157 BGB (Auslegung) → § 305c Abs. 2 BGB (Unklarheitenregelung AGB) → § 184 GVG (Amtssprache) → §§ 55 Abs. 2, 56 GmbHG (Beurkundung, Sacheinlage)
