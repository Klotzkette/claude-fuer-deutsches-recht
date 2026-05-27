---
name: zvg-simulation-training
description: "Simulation und Training fuer Zwangsverwaltung mit einem achtstuendigen Praxistag. Anwendungsfall Verwalter oder Kanzleimitarbeiter will Zwangsverwaltungs-Workflows trainieren oder Plugin demonstrieren. Deckt Mieterpost Objektgefahr Kontoabgleich Gericht Bericht und Verteilung ab. Output Simulationsprotokoll mit Tagesereignissen Fehlerhinweisen Lernnotizen und Leistungsbewertung. Abgrenzung zu zvg-kommandocenter (Echtbetrieb) und zvg-quality-gate."
---

# Simulation und Training

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

- BGH, Beschl. v. 04.10.2007 - IX ZB 220/06, NZI 2007, 726 Rn. 20 — Fehlerhafte Entscheidungen des Zwangsverwalters können auch dann zu Haftungsansprüchen führen, wenn sie auf Unkenntnis beruhen; die Fortbildungspflicht ist Teil der Berufsstandards eines Zwangsverwalters.
- OLG Stuttgart, Beschl. v. 25.03.2010 - 8 W 121/10, Rpfleger 2010, 456 — Simulationstraining und Fall-Übungen sind in der Ausbildung zum Zwangsverwalter als methodisches Mittel anerkannt; praxisnahe Trainings zu typischen Konfliktszenarien erhöhen die Handlungssicherheit.

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
