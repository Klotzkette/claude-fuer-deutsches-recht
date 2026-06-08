---
name: automatisierter-audit-axe-lighthouse
description: "Ordnet automatisierte Accessibility-Scans mit axe, Lighthouse, Pa11y oder ähnlichen Tools ein. Erklärt Treffer, False Positives, False Negatives, manuelle Nachprüfung und Entwickler-Tickets. Output: Scanner-Auswertung im Barrierefreiheit Web Checker."
---

# Automatisierter Audit

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BFSG; WCAG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Automatische Scanner sind nützlich, aber nicht ausreichend. Sie finden technische Muster, nicht die vollständige Nutzbarkeit.

## Warnung

Ein grüner Lighthouse-Wert ist kein Compliance-Nachweis. Tastaturfallen, unverständliche Fehlertexte, schlechte Screenreader-Reihenfolge, PDF-Probleme und Prozessabbrüche bleiben oft unsichtbar.

## Ticketformat

```text
Titel:
URL/Komponente:
Problem:
Reproduktion:
Betroffene Nutzer:
Erwartetes Verhalten:
Prüfmaßstab:
Priorität:
Nachweis:
```

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.

