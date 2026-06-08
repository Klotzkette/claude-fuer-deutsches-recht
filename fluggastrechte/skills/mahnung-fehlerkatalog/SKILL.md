---
name: mahnung-fehlerkatalog
description: "Mahnung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Mahnung Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Fluggastrechte** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `abtretung-an-fluggastportal-spezial`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `airline-bonitaet-und-vollstreckung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `airline-standardausreden-annullierung-verspaetung-anschlussflug`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `airline-standardausreden-pruefen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `allgemein-anschluss-router-workflow-chronologie`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `annullierung-oder-verspaetung-einordnen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `anschlussflug-und-reiseplan`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `ausnahmen-aussergewoehnliche-aussergewoehnliche-umstaende`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `ausnahmen-aussergewoehnliche-umstaende-pruefen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `aussergewoehnliche-distanz-interessen-erfassen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.

## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)
