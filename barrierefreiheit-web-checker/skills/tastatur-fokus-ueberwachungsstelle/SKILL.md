---
name: tastatur-fokus-ueberwachungsstelle
description: "Für Tastatur, Fokus, Navigation: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Tastatur, Fokus, Navigation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BFSG; WCAG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieses Fachmodul trägt die wichtigste manuelle Prüfung: Kann man die Website ohne Maus bedienen?

## Prüfpfad

1. Tab-Reihenfolge ab Startseite.
2. Skiplink oder direkter Sprung zum Hauptinhalt.
3. Sichtbarer Fokus in allen Zuständen.
4. Menüs, Submenüs, Filter, Slider, Accordions.
5. Modale, Cookie-Banner, Warenkorb, Login.
6. Fokus bleibt nicht gefangen und geht nach Schließen sinnvoll zurück.
7. Alle interaktiven Elemente sind erreichbar und auslösbar.

## Protokoll

| URL | Element | Problem | Reproduktion | Priorität | Fix |
| --- | --- | --- | --- | --- | --- |

## Red Flags

- Fokus unsichtbar.
- Cookie-Banner blockiert Tastatur.
- Menü öffnet per Hover, aber nicht per Tastatur.
- Modal lässt Fokus im Hintergrund weiterlaufen.
- Buttons sind als div gebaut.

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.
