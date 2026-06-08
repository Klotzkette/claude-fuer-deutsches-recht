---
name: gate-fehlerkatalog
description: "Gate Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Gate Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Zwangsverwaltung Zvg** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `berichte-beschlagnahme-mietverwaltung-besitz`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `betriebskosten-hausgeld-bieterangebot-bewertung-glaeubiger`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `bieterangebote-mieten-öffentliche`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `insolvenz-schnittstelle-instandhaltung-sicherung-zvg`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `konten-kassenfuehrung-miet-pachtverwaltung-mieteinzug`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `quality-recherche-rechnungslegung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `treuhandkonto-versteigerung-versteigerungsteilnahme`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `versicherungen-gefahren-zvg-versteigerungsteilnahme-zvg`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `verteilung-zwangsverwaltung-aktenanlage-objektcockpit`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
