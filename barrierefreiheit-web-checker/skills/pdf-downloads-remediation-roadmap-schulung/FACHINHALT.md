---
name: pdf-downloads-remediation-roadmap-schulung
description: "Für PDFs, Downloads und Dokumente: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# PDFs, Downloads und Dokumente

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BFSG; WCAG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieses Fachmodul prüft Fälle, in denen eine Website barrierefrei wirkt, wichtige Informationen aber in PDFs, Word-Dateien oder Formularen stecken.

## Prüfpunkte

- Ist das Dokument überhaupt notwendig oder gibt es eine HTML-Alternative?
- PDF getaggt?
- Lesereihenfolge korrekt?
- Überschriften und Listen strukturiert?
- Tabellen mit Kopfzellen?
- Bilder mit Alternativtext?
- Formularfelder benannt?
- Sprache gesetzt?
- Scan-PDF mit OCR?

## Priorität

AGB, Preislisten, Produktinformationen, Formulare, Widerrufsbelehrung, Barrierefreiheitserklärung und behördliche Bescheide sind hoch zu priorisieren. Rein dekorative Broschüren können niedriger priorisiert werden, wenn die wesentlichen Informationen barrierefrei anderweitig vorliegen.

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.
