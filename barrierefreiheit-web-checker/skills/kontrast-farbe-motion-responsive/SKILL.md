---
name: kontrast-farbe-motion-responsive
description: "Prüft Kontrast, Farbe ohne Farbcodierung, Zoom, Reflow, Textabstände, responsives Layout, Animationen, Motion-Reduction, Hover-Fallen und mobile Nutzung. Output: visuelle Barrierefreiheitsmatrix im Barrierefreiheit Web Checker."
---

# Kontrast, Farbe, Motion, Responsive

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BFSG; WCAG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieses Fachmodul prüft visuelle und responsive Barrierefreiheit.

## Prüfungslinien

- Text- und Komponenten-Kontrast.
- Informationen nicht nur durch Farbe.
- Zoom bis 200 Prozent ohne Funktionsverlust.
- Reflow bei schmaler Ansicht.
- Textabstände und Zeilenhöhen.
- Animationen, Parallax, Autoplay, blinkende Inhalte.
- prefers-reduced-motion respektieren.
- Touch-Zielgrößen und mobile Bedienbarkeit.

## Matrix

| Komponente | Problem | Nutzerwirkung | Fix |
| --- | --- | --- | --- |
| Button | Kontrast zu niedrig | nicht erkennbar | Farbe/Border anpassen |
| Fehlermeldung | nur rot | Farbwahrnehmung | Icon + Text |
| Slider | Autoplay | Bewegung/Bedienung | Pause/Stop + Motion |

## Priorität

Kontrast und Reflow sind oft schnell zu beheben und stark nutzerwirksam. Animationsprobleme werden gern unterschätzt, weil sie nur manche Nutzerinnen und Nutzer hart treffen.

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.

