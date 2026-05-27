---
name: vaf-template-erkennung
description: "Vertragsvorlage und Altvertrag erkennen und analysieren: Anwendungsfall Anwalt oder Mandant gibt unbekannte Vorlage oder alten Vertrag ein und Skill soll Vertragstyp Klauselstruktur Pflichtfelder und Wahlklauseln identifizieren. §§ 433 ff. BGB Kaufvertrag, §§ 535 ff. BGB Mietvertrag, §§ 611a ff. BGB Arbeitsvertrag. Pruefraster AGB vs. Individualvertrag, Sprache, strukturierte vs. unstrukturierte Platzhalter, Vertragstyp-Einordnung. Output Vorlage-Analyse mit Vertragstyp, Klauselliste und Pflichtfeld-Map. Abgrenzung zu DOCX-Stripper fuer rohe Textzerlegung und zu Feldinventar."
---

# Template-Erkennung


## Triage zu Beginn

1. Welcher Vertragstyp liegt vor — Kauf, Miete, Werk, Dienstleistung, Lizenz, Arbeitsvertrag?
2. Ist die Vorlage ein AGB-Formular oder ein Individualvertrag?
3. In welcher Sprache ist die Vorlage — deutsch, englisch, zweisprachig?
4. Gibt es strukturierte Platzhalter ([...], XXX, TBD) oder nur unstrukturierten Freitext?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 27.04.2016 - VIII ZR 61/15, NJW 2016, 1881 — AGB-Mustervertrag: Klauseln sind nach objektivem Empfängerhorizont auszulegen; spezifische Branchenkenntnis des Verwenders nicht zurechenbar.
- BGH, Urt. v. 14.07.2004 - VIII ZR 163/03, NJW 2004, 2884 — Essentialia negotii: Kaufgegenstand und Preis müssen im Vertragstext hinreichend bestimmt sein.
- BGH, Urt. v. 22.11.2017 - VIII ZR 83/17, NJW 2018, 394 — Formularklauseln sind eng nach ihrem Wortlaut auszulegen; Auslegungszweifel gegen den Verwender (§ 305c Abs. 2 BGB).
- BGH, Urt. v. 19.09.2018 - XII ZR 69/17, NJW 2019, 51 — Vertragstyp bestimmt anwendbares Gewährleistungsrecht; falsche Typisierung kann zu unerwarteten Haftungsfolgen führen.

## Zentrale Normen

- §§ 433, 535, 631, 611 BGB — Kauf, Miete, Werk, Dienst (Vertragstypen)
- § 305 BGB — AGB-Einbeziehung
- § 305c Abs. 2 BGB — Unklarheitenregel (gegen Verwender)

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, vor § 433 Rn. 1-10 (Vertragstypen)
- MüKo-BGB/Lorenz, 9. Aufl. 2022, § 433 Rn. 1-30 (Kaufvertrag Überblick)

## Aufgabe

Der Skill klassifiziert den Vertrag und trennt Fixtext von Variablen. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Vertragstyp, Parteien, Gegenstand, Leistung, Entgelt, Laufzeit, Kündigung, Haftung, Anlagen und Signaturen erkennen.
2. Fixe Stammdaten des Verwenders von variablen Mandatsdaten trennen.
3. Wahlklauseln als Entscheidungspunkte markieren, nicht stillschweigend streichen.
4. Feldnamen normalisieren, damit Term Sheet und Vorlage zusammengeführt werden können.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.
