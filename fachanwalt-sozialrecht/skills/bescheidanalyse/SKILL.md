---
name: bescheidanalyse
description: "Mandant hat Sozialleistungsbescheid erhalten und Anwalt muss dessen Inhalt rechtlich aufschluesseln. §§ 33 35 SGB X Form und Begruendungspflicht § 24 SGB X Anhoerung. Pruefraster: Behoerde Aktenzeichen Bescheiddatum Zugangsdatum Bescheidart (Ablehnung/Aufhebung/Rueckforderung/Sanktion) angewandte Rechtsgrundlagen Anhaltspunkte fuer Widerspruchsgruende. Output: Analyseprotokoll Bescheidanalyse als Vorstufe fuer Widerspruchsentwurf. Abgrenzung zu bescheid-frist-quick-check (Frist) und fachanwalt-sozialrecht-widerspruch-sozialleistung (Widerspruchsentwurf)."
---

# Bescheidanalyse Sozialrecht

## Aktuelle Rechtsprechung
- BSG, Urt. v. 26.09.2019 - B 9 SB 1/18 R, SozR 4-3250 § 2 Nr. 22 Rn. 14 — Begründungspflicht (§ 35 SGB X): ein Bescheid muss die wesentlichen tatsächlichen und rechtlichen Gründe enthalten, die die Behörde zur ihrer Entscheidung bewogen haben; fehlt die Begründung, ist der Bescheid aufhebbar.
- BSG, Urt. v. 27.10.2020 - B 14 AS 31/19 R, SozR 4-4200 § 11 Nr. 91 Rn. 18 — Fehlende Anhörung (§ 24 SGB X) führt zur Aufhebbarkeit (nicht Nichtigkeit) des Bescheids; Heilung im Widerspruchsverfahren nach § 41 Abs. 1 Nr. 3 SGB X nur wenn Behörde im Widerspruchsbescheid auf Vortrag eingeht.
- BSG, Urt. v. 11.12.2019 - B 14 AS 37/18 R, SozR 4-1300 § 33 Nr. 6 Rn. 16 — Bestimmtheit des Bescheids (§ 33 SGB X): Bescheid muss inhaltlich hinreichend bestimmt sein; unklarer Tenor führt zur Rechtswidrigkeit unabhängig von der sachlichen Richtigkeit.

## Zweck

Vor dem Widerspruch steht die Analyse. Dieser Skill liest einen Bescheid systematisch und extrahiert das, was der Anwalt für den nächsten Schritt braucht.

## Eingaben

- Bescheid als PDF Foto oder Text (auch gescannt mit OCR).
- Mandantenangaben aus `mandanten-intake`.
- Optional: vorangegangene Bescheide derselben Sache.

## Prüfraster

### Formale Prüfung

- **Behörde** zuständig (sachlich oertlich)?
- **Adressat** korrekt bezeichnet (Vor- und Nachname; bei Bedarfsgemeinschaft alle Mitglieder)?
- **Bescheiddatum** und **Zugangsdatum** klar (Zugang nach § 37 SGB X n.F. — Vier-Tages-Fiktion bei Post seit 1.1.2025 PostModG; bei Aufgabe zur Post vor dem 1.1.2025 weiterhin Drei-Tages-Fiktion alter Fassung)?
- **Tenor** eindeutig?
- **Begründung** nach § 35 SGB X mit wesentlichen tatsächlichen und rechtlichen Gründen vorhanden?
- **Rechtsbehelfsbelehrung** vollständig (Behörde Frist Form Adressat)?
- **Anhörung** nach § 24 SGB X erfolgt bei belastenden Bescheiden?
- **Unterschrift / Namenswiedergabe** vorhanden (§ 33 SGB X)?

### Materielle Vorprüfung

- **Anspruchsgrundlage** korrekt bezeichnet?
- **Tatbestandsmerkmale** in der Begründung vollständig abgehandelt?
- **Ermessen** ausgeuebt wo erforderlich (§ 39 SGB I)?
- **Mitwirkungsobliegenheiten** § 60 ff. SGB I — wurden sie korrekt eingefordert?
- **Bestandskraft** vorheriger Bescheide?

### Besondere Bescheidarten

- **Aufhebung und Erstattung** §§ 45 / 48 / 50 SGB X — Prüfung von Vertrauensschutz Atypik Ermessen.
- **Sanktion / Leistungsminderung** § 31 SGB II / § 32 SGB II — Schwere Wiederholung Mitverschulden.
- **Aufrechnung** § 43 SGB I / § 51 SGB I — Schwellenwerte.

## Ausgabe

Analyseprotokoll mit:

1. Stammdaten Bescheid (Behörde Az Datum Zugang)
2. Tenor und Höhe der Beschwer
3. Rechtsbehelfsbelehrung mit Fristberechnung (Widerspruchsfrist ein Monat § 84 SGG)
4. Formelle Fehler (Anhörung Begründung Rechtsbehelfsbelehrung)
5. Materielle Angriffspunkte sortiert nach Erfolgsaussicht
6. Empfehlung: Widerspruch / Überprüfungsantrag § 44 SGB X / Untätigkeitsklage / nichts
7. Frist im Fristenbuch eintragen — Verweis auf `fristenbuch-sozialrecht`

## Grenzen

Die Analyse ersetzt nicht die anwaltliche Entscheidung. Sie strukturiert die Vorbereitung.
