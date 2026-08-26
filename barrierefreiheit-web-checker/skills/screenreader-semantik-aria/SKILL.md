---
name: screenreader-semantik-aria
description: "Für Screenreader, Semantik, ARIA: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Screenreader, Semantik, ARIA

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BFSG; WCAG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Anwendungsfall: die Website optisch funktioniert, aber semantisch unklar ist.

## Prüfschritte

1. Seitentitel und Sprache.
2. Landmarken: header, nav, main, footer, aside.
3. Überschriftenstruktur.
4. Links und Buttons mit verständlichem Namen.
5. Formularlabels und Fehlermeldungen.
6. Bilder und Icons mit sinnvollen Alternativen oder dekorativer Ausblendung.
7. ARIA nur dort, wo native HTML-Semantik nicht reicht.
8. Live-Regionen für dynamische Statusmeldungen.

## Merksatz

Schlechtes HTML wird durch ARIA selten besser. Erst native Semantik, dann ARIA gezielt.

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.
