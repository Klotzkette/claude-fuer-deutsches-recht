---
name: remediation-roadmap-dokumentation
description: "Erstellt Maßnahmenplan für Barrierefreiheits-Fixes: Priorisierung, Nutzerimpact, Rechtsrisiko, Aufwand, Owner, Tickets, Re-Test, Nachweisakte und Management-Reporting. Output: Roadmap und Dokumentation im Barrierefreiheit Web Checker."
---

# Remediation-Roadmap und Dokumentation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BFSG; WCAG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieses Fachmodul arbeitet nach Audit oder Beschwerde einen Plan aus, der Entwickler, Management, Rechtsabteilung und Nutzerkontakt zusammenbringt.

## Priorisierung

1. Blocker in Kernprozessen: Login, Checkout, Antrag, Zahlung, Terminbuchung.
2. Tastaturfallen und Fokusverlust.
3. Fehlende Labels und Fehlermeldungen.
4. Kontrast/Reflow.
5. Dokumente mit rechtlich wesentlichen Informationen.
6. Kosmetische oder seltene Barrieren.

## Roadmap

| Ticket | Problem | Nutzerimpact | Rechtsrisiko | Owner | Frist | Re-Test |
| --- | --- | --- | --- | --- | --- | --- |

## Nachweisakte

- Auditdatum
- Maßstab
- Stichprobe
- Toolversionen
- manuelle Prüfprotokolle
- Tickets
- Re-Test
- offene Restbarrieren mit Begründung
- Kommunikationsnachweise

## Merksatz

Ein Maßnahmenplan ist kein Ausredenpapier. Er muss zeigen, was wann behoben wird, wer verantwortlich ist und wie der Fix geprüft wird.

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.

