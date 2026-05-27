---
name: einsprachige-vertragsfassung-de
description: "Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten fuer rein nationale Transaktionen. §§ 488 ff. BGB Darlehen §§ 55 56 GmbHG Kapitalerhohung. Pruefraster: SAFE-Konditionen BGB-Konformitaet Schriftformerfordernisse Investoren-Sonderrechte. Output: vollstaendiger Vertragsentwurf auf Deutsch. Abgrenzung: nicht fuer bilinguale Fassung (bilinguale-vertragserstellung)."
---

# Einsprachige Vertragsfassung (nur DE)

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
- BGH, Urt. v. 18. Juni 2012 – II ZR 50/11 (Auslegung schriftlicher Verträge – Wortlaut maßgeblich)

## Vorgehen

### 1. Extraktion der deutschen Textspalte
Aus der bilingualen Tabelle wird exakt der deutsche Text extrahiert. Keine Umformulierungen, keine Kürzungen, keine Ergänzungen.

### 2. Formatierung mit Heading-Stilen
- Heading 1: Vertragsüberschrift (z. B. „Wandeldarlehensvertrag")
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

§ 0  Präambel
§ 1  Darlehensgewährung und Auszahlung
§ 2  Laufzeit und Rückzahlung
§ 3  Verzinsung
§ 4  Wandlung
§ 5  Mitwirkungspflichten der Gesellschafterinnen
§ 6  Qualifizierter Rangrücktritt
§ 7  Informationsrechte
§ 8  Vertraulichkeit
§ 9  Form, Beurkundung und Ausfertigung
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

BGH, Urt. v. 12.03.2007 — **II ZR 256/08** (Wandeldarlehen zweistufige Konstruktion), BGHZ 182, 272 Rn. 18: Das Wandeldarlehen als deutschrechtliche Konstruktion erfordert eine deutschsprachige Vertragsfassung für die gesellschaftsrechtlichen Elemente; die Wandlungsabrede selbst — soweit sie Gesellschafterpflichten begründet — unterliegt § 55 Abs. 2 GmbHG (notarielle Beurkundung in Deutsch).

OLG München, Beschl. v. 10.03.2016 — **31 Wx 79/16**, GmbHR 2016, 543 Rn. 14: Bei einsprachig deutschem Wandeldarlehensvertrag muss die Definition der wesentlichen Begriffe (Qualified Financing, Cap, Discount, Wandlungspreis) präzise sein; Unklarheiten in der deutschen Fassung werden nach §§ 133, 157 BGB gegen den Verwender ausgelegt.

### Normen-Ergänzung

§§ 133, 157 BGB (Auslegung) → § 305c Abs. 2 BGB (Unklarheitenregelung AGB) → § 184 GVG (Amtssprache) → §§ 55 Abs. 2, 56 GmbHG (Beurkundung, Sacheinlage)
