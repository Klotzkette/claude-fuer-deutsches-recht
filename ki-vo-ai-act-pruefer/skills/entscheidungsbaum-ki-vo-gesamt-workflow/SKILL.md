---
name: entscheidungsbaum-ki-vo-gesamt-workflow
description: "Master-Workflow fuer die vollstaendige KI-VO-Pruefung. Fuehrt von Art. 3 KI-System-Definition ueber Anwendungsbereich, Rollen, Art. 6 Abs. 2/Anhang III-Hochrisiko, Rueckausnahme, GPAI/Chatbot-Abgrenzung, Betreiber-Fehlgebrauch, Pflichten, Standards und Output-Dokumentation. Schwerpunkt: allgemeine Chatbots sind nicht automatisch Hochrisiko; Zweckbestimmung und tatsaechlicher Einsatz entscheiden. Output: strukturierter Pruefpfad mit Folge-Skills."
---

# Master-Workflow: KI-VO-Gesamtprüfung

## Zweck

Dieser Skill ist der zentrale Entscheidungsbaum des KI-VO-Prüfers. Er führt vom ersten Art.-3-Check bis zum dokumentierbaren Endvermerk. Er soll nicht nur klassifizieren, sondern den Prüfpfad so steuern, dass Zweckbestimmung, tatsächliche Nutzung und Off-label-Risiken sauber sichtbar werden.

## Grundsatz

Nicht der Produktname entscheidet, sondern der geprüfte Funktionszuschnitt und die Zweckbestimmung. Ein allgemeiner Chatbot oder ein GPAI-System ist nicht automatisch Hochrisiko. Wird er aber für Bewerberbewertung, Beschäftigtenmanagement, Kreditwürdigkeit, Bildung, Justiz, Migration, Strafverfolgung, Notfalltriage oder andere Anhang-III-Zwecke bestimmt oder faktisch eingesetzt, muss Art. 6 Abs. 2 i.V.m. Anhang III vertieft geprüft werden.

## Schritt 0 — Intake

Starte bei unklarer Lage mit `triage-ki-vo-vorpruefung` oder `allgemein`.

Mindestfragen:
1. Was genau ist das System oder die Komponente?
2. Wer ist Anbieter, Betreiber oder sonstiger Akteur?
3. Wofür ist das System bestimmt?
4. Wie wird es tatsächlich genutzt?
5. Sind natürliche Personen, kritische Infrastruktur oder öffentliche Aufgaben betroffen?
6. Soll ein Vermerk, Memo, Checkliste oder Maßnahmenplan entstehen?

## Schritt 1 — KI-System nach Art. 3 Nr. 1

Skill: `liegt-ki-system-vor-art-3-nr-1`

Prüfe:
- Maschinenbasiert
- Autonomiegrad ohne Überhöhung
- Adaptivität als optionales Indiz
- explizite/implizite Ziele
- Inferenz aus Eingaben
- Output-Typ
- Einfluss auf physische oder virtuelle Umgebung

Wenn Grenzfall: `abgrenzung-konventionelle-software-vs-ki-system`.

## Schritt 2 — Anwendungsbereich

Skills:
- `territorialer-anwendungsbereich-art-2`
- `sachlicher-ausschluss-art-2-abs-3-bis-12`

Prüfe EU-Bezug, Ausgaben in der EU, Inverkehrbringen, Betrieb und sachliche Ausnahmen.

## Schritt 3 — Rollen

Skills:
- `persoenlicher-anwendungsbereich-rollen-art-3`
- `rolle-anbieter-pruefen-art-3-nr-3`
- `rolle-betreiber-pruefen-art-3-nr-4`
- bei Zweckänderung: `anbieter-werden-art-25`

Besonders prüfen:
- Wer bestimmt den Zweck?
- Wer nimmt das System in eigener Verantwortung in Betrieb?
- Ändert ein Betreiber Zweck oder System wesentlich?
- Gibt es mehrere Rollen nebeneinander?

## Schritt 4 — Verbote kurz screenen

Skill: `verbotene-praktiken-art-5`

Nur wenn Treffer möglich, vertiefen. Der Fokus dieses Workflows liegt danach auf Art. 6 Abs. 2/Anhang III.

## Schritt 5 — Hochrisiko Pfad 1

Skill: `hochrisiko-art-6-abs-1-sicherheitsbauteil`

Prüfe Sicherheitsbauteil/Produkt, Anhang-I-Sektorrecht und Dritt-Konformitätsbewertung.

## Schritt 6 — Hochrisiko Pfad 2: Art. 6 Abs. 2 i.V.m. Anhang III

Skill: `hochrisiko-art-6-abs-2-anhang-iii`

Pflichtfragen:
- In welchem Anhang-III-Bereich wird das System eingesetzt?
- Geht es um Bewertung, Zugang, Ranking, Entscheidung, Priorisierung, Risiko, Rechtsanwendung oder Überwachung?
- Ist der Einsatz ausdrücklich intendiert, technisch angelegt, organisatorisch geduldet oder nur theoretisch möglich?
- Ist ein allgemeiner Chatbot/GPAI-System nur Hilfsmittel oder in einen sensiblen Entscheidungsprozess eingebettet?
- Wie werden Mitarbeitenden-Fehlgebrauch und Zweckabweichung verhindert?

## Schritt 7 — Rückausnahme Art. 6 Abs. 3

Skill: `rueckausnahme-art-6-abs-3`

Prüfe eng:
- Profiling natürlicher Personen sperrt die Rückausnahme.
- Kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte.
- Eine der vier Fallgruppen liegt wirklich vor.
- Dokumentation nach Art. 6 Abs. 4.

## Schritt 8 — GPAI und Chatbot

Skills:
- `gpai-vorliegen-art-3-nr-63`
- `gpai-modelle-art-51-bis-55`
- `gpai-systemisches-risiko-schwelle-10e25-flop`
- `begrenztes-risiko-art-50-transparenzpflichten`

Leitsatz:
- Allgemeiner Chatbot: typischerweise Art. 50/GPAI prüfen, nicht automatisch Hochrisiko.
- Konkreter Fachworkflow in Anhang III: Hochrisiko-Prüfung aktivieren.

## Schritt 9 — Pflichten und Standards

Bei Hochrisiko:
- `hochrisiko-bestaetigt-end-to-end-roadmap`
- Art. 9 bis 15 Skills
- `hochrisiko-konformitaetsbewertung-art-43-bis-49`
- `eu-datenbank-registrierung-art-49-und-71`

Bei Betreiber:
- `betreiber-deployer-pflichten-art-26`
- `output-betreiber-checkliste-und-folgenabschaetzung`

Bei Standards:
- `code-of-practice-und-harmonisierte-normen`

## Schritt 10 — Prüfdokument

Skill: `output-pruefdokument-ki-vo-mit-warnhinweisen`

Das Enddokument muss enthalten:
- KI-System-Einordnung nach Art. 3
- Zweckbestimmung und tatsächliche Nutzung
- GPAI/Chatbot-Abgrenzung
- Anhang-III-Matrix
- Art. 6 Abs. 3-Bewertung
- Rollen und Pflichten
- Off-label-/Mitarbeitenden-Nutzungsplan
- Standards-/Normenhinweis
- offene Tatsachen und Re-Evaluation-Trigger

## Kompakter Routing-Plan

```text
1. triage-ki-vo-vorpruefung / allgemein
2. liegt-ki-system-vor-art-3-nr-1
3. territorialer-anwendungsbereich-art-2
4. persoenlicher-anwendungsbereich-rollen-art-3
5. risikoklassen-uebersicht-und-triage
6. hochrisiko-art-6-abs-2-anhang-iii (wenn Zwecknaehe)
7. rueckausnahme-art-6-abs-3 (bei Anhang-III-Treffer)
8. gpai-vorliegen-art-3-nr-63 / begrenztes-risiko-art-50-transparenzpflichten (bei Chatbot/GPAI)
9. betreiber-deployer-pflichten-art-26 / anbieter-werden-art-25 (bei Zweckabweichung)
10. output-pruefdokument-ki-vo-mit-warnhinweisen
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 2, 3, 5, 6, 25, 26, 27, 40, 50, 51 bis 56 und Anhang III KI-VO. Keine Rechtsberatung.
