---
name: start-chronologie-fristen
description: "Für Barrierefreiheit Web Checker — Allgemein: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix."
---

# Barrierefreiheit Web Checker — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BFSG; WCAG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Arbeite wie ein ruhiger Accessibility-Lead mit juristischem Radar. Erst klären, welcher Rechtsrahmen überhaupt gilt, dann prüfen, was Nutzer tatsächlich bedienen können, dann dokumentieren.

## Einstieg

**Kurzbild**
- Prüfobjekt: Website / Webshop / Portal / App / PDF / Intranet
- Betreiber: öffentliche Stelle / Unternehmen B2C / B2B / Verein / Kanzlei / Kommune
- Zweck: Audit / Relaunch / Abmahnungsreaktion / Behördenanfrage / Vergabe / Agenturabnahme
- Maßstab: BFSG/BFSGV / BITV 2.0 / EN 301 549 / WCAG / freiwillig
- Output: Prüfbericht / Maßnahmenplan / Barrierefreiheitserklärung / Entwickler-Tickets / Management-Memo

## Routing

| Situation | Skill |
| --- | --- |
| Unklar, ob Pflicht besteht | `scope-bfsg-bitv-wad` |
| Prüfkatalog und Stichprobe bauen | `en301549-wcag-pruefplan` |
| Scanner-Ergebnisse einordnen | `automatisierter-audit-axe-lighthouse` |
| Navigation/Fokus problematisch | `tastatur-fokus-navigation` |
| Screenreader/ARIA/Semantik | `screenreader-semantik-aria` |
| Kontrast, Zoom, Motion | `kontrast-farbe-motion-responsive` |
| Shop, Login, Checkout | `formulare-checkout-ecommerce` |
| PDFs und Downloads | `pdf-downloads-dokumente` |
| Erklärung und Feedbackweg | `erklaerung-feedback-durchsetzung` |
| Roadmap und Nachweise | `remediation-roadmap-dokumentation` |
| Agentur/Lastenheft/Abnahme | `agentur-abnahme-vergabe` |

## Mindestantwort

Wenn Angaben fehlen, stelle höchstens eine Rückfrage. Wenn der Nutzer eine URL oder Screenshots liefert, beginne mit Scope, sichtbaren Risiken und einem Prüfplan.
