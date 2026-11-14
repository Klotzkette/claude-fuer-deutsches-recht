---
name: agentur-abnahme-vergabe
description: "Für Agentur, Abnahme, Vergabe: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Agentur, Abnahme, Vergabe

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BFSG; WCAG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieses Fachmodul begleitet Websites, die neu gebaut, relauncht oder von einer Agentur nachgebessert werden.

## Lastenheft-Bausteine

- Maßstab: einschlägige Norm plus EN 301 549/WCAG-Prüfung.
- Designsystem mit barrierefreien Komponenten.
- Tastaturbedienbarkeit als Abnahmekriterium.
- Formulare und Fehlermeldungen barrierefrei.
- PDFs und Downloads entweder barrierefrei oder mit HTML-Alternative.
- Automatisierter und manueller Audit vor Abnahme.
- Re-Test nach Nachbesserung.
- Redaktionelle Schulung für künftige Inhalte.

## Abnahmeprotokoll

| Bereich | Abnahmekriterium | Nachweis | Status |
| --- | --- | --- | --- |
| Navigation | Tastatur vollständig | Testprotokoll | offen/ok |
| Formulare | Labels und Fehler | Screenshot + DOM | offen/ok |
| Checkout | Vertragsschluss möglich | User Journey | offen/ok |
| PDF | getaggt oder HTML | Dokumentencheck | offen/ok |

## Warnung

Accessibility-Overlay, Plugin oder Widget ersetzt keine barrierefreie Umsetzung. Es kann ergänzen, aber nicht die eigentlichen HTML-, Design-, Content- und Prozessfehler heilen.

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.
