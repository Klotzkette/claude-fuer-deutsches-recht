---
name: simulation-training
description: "Simulation und Training für Zwangsverwaltung mit einem achtstuendigen Praxistag. Anwendungsfall Verwalter oder Kanzleimitarbeiter will Zwangsverwaltungs-Workflows trainieren oder Plugin demonstrieren. Deckt Mieterpost Objektgefahr Kontoabgleich Gericht Bericht und Verteilung ab. Output Simulationsprotokoll mit Tagesereignissen Fehlerhinweisen Lernnotizen und Leistungsbewertung. Abgrenzung zu zvg-kommandocenter (Echtbetrieb) und zvg-quality-gate im Zwangsverwaltung Zvg: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Simulation und Training

## Arbeitsbereich

Simulation und Training für Zwangsverwaltung mit einem achtstuendigen Praxistag. Anwendungsfall Verwalter oder Kanzleimitarbeiter will Zwangsverwaltungs-Workflows trainieren oder Plugin demonstrieren. Deckt Mieterpost Objektgefahr Kontoabgleich Gericht Bericht und Verteilung ab. Output Simulationsprotokoll mit Tagesereignissen Fehlerhinweisen Lernnotizen und Leistungsbewertung. Abgrenzung zu zvg-kommandocenter (Echtbetrieb) und zvg-quality-gate. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe

Erzeugt einen realistischen Trainingslauf für Zwangsverwaltungsfälle, wenn echte Schnittstellen oder Akten fehlen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- das Plugin ausprobiert werden soll
- keine echten Objekt- oder Gerichtsdaten genutzt werden dürfen
- ein neuer Mitarbeiter den Ablauf trainiert

## Eingaben

- gewünschter Schwierigkeitsgrad
- optional Testakte oder eigener Objektsteckbrief
- Simulationsdauer

## Workflow

1. **Szenario wählen** - Wohnhaus, Gewerbe, WEG, Leerstand oder gemischtes Objekt auswählen.
2. **Tageslauf** - Mieterpost, Kontoeingänge, Gefahrmeldung, Gerichtsanfrage und Gläubigerdruck simulieren.
3. **Entscheidungen** - Nutzer durch Rückfragen, Entwürfe und Korrekturen führen.
4. **Auswertung** - Fehler, bessere Reihenfolge und Folgeaufgaben ausgeben.

## Ausgabe

- Simulationsakte
- Tagesprotokoll
- Lern- und Fehlerliste

## Qualitätsgates

- Simulation klar markiert
- keine echten personenbezogenen Daten
- Auswertung mit Rechtsquellen

## Rote Schwellen

- Nutzer verwechselt Simulation mit echter Akte
- fehlende Freigabe für echte Daten
- unzulässige Selbsthilfeidee

## Interne Vorlagen

- assets/templates/simulationstag.md
- assets/templates/quality-gate.md

## Amtliche Erstquellen

- ZVG Gesamtfassung
- ZwVwV Gesamtfassung

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Aus-/Fortbildung ZVG

§ 152 ZVG (Sorgfaltspflicht ordnungsgemäße Verwaltung) → § 280 BGB (Haftung Pflichtverletzung) → ZwVwV vollständig (Pflichtenprogramm)

## Typische Trainingsszenarien

1. **Mieter zahlt nicht:** Mahnverfahren, Kündigung, Klage — Schritt für Schritt
2. **Schuldner verweigert Zutritt:** Antrag auf gerichtliche Hilfe, § 154 ZVG
3. **Wasserschaden im Objekt:** Sofortmaßnahmen, Versicherungsmeldung, Gerichtsantrag Instandhaltung
4. **Insolvenzantrag des Schuldners kommt während Verwaltung:** Koordination mit Insolvenzverwalter
5. **Gläubiger fordert sofortige Ausschüttung:** Verteilungsplan § 155 ZVG, Rücklagen-Check
6. **Mieter kündigt und hinterlässt Schäden:** Dokumentation, Kautionseinbehalt, ggf. Klage

## Trainings-Template: Fallaufbau

```
Szenario: [TITEL]
Ausgangslage: [SACHVERHALT IN 3-5 SÄTZEN]
Handlungsdruck: [WAS PASSIERT WENN NICHTS GETAN WIRD]
Aufgabe: [KONKRETE HANDLUNG]
Lösung: [VORGEHEN SCHRITT FÜR SCHRITT]
Normen: [EINSCHLÄGIGE PARAGRAPHEN]
Häufige Fehler: [TYPISCHE FEHLER IN DIESER SITUATION]
```
