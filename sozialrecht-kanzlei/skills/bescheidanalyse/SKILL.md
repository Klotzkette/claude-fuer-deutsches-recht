---
name: bescheidanalyse
description: Strukturierte Auswertung eines sozialrechtlichen Bescheids — erfasst Behoerde Aktenzeichen Bescheiddatum Zugangsdatum Bescheidart (Ablehnung / teilweise Bewilligung / Aufhebung / Rueckforderung / Sanktion) Tenor Begruendungs-Kernpunkte angewandte Rechtsgrundlagen Rechtsbehelfsbelehrung. Prueft formale Anforderungen (§§ 33 ff. SGB X) Anhoerung (§ 24 SGB X) Begruendungspflicht (§ 35 SGB X) und identifiziert Anhaltspunkte fuer Widerspruchsgruende. Erzeugt Analyseprotokoll als Vorstufe fuer den Widerspruchsentwurf.
---

# Bescheidanalyse Sozialrecht

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
