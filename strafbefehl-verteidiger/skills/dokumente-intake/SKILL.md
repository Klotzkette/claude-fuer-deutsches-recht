---
name: dokumente-intake
description: "Dokumentenintake für Strafbefehl-Verteidigung: sortiert Strafbefehl, Ermittlungsakte, Einspruchsschrift, prüft Datum, Absender, Frist und Beweiswert (Vernehmungen, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Strafbefehl Verteidiger** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `aktenanlage-fehlerkatalog` — Aktenanlage Fehlerkatalog
- `akteneinsicht-behoerden-gericht-und-registerweg` — Akteneinsicht Behoerden Gericht und Registerweg
- `deal-beweislast-einspruch` — Deal Beweislast Einspruch
- `einspruch-risikoampel-und-gegenargumente` — Einspruch Risikoampel und Gegenargumente
- `einspruchsentscheidung-und-folgen` — Einspruchsentscheidung und Folgen
- `einstellung-153a-hauptverhandlung` — Einstellung 153a Hauptverhandlung
- `einstellung-fahrerlaubnis` — Einstellung Fahrerlaubnis
- `fahrerlaubnis-mandantenentscheidung` — Fahrerlaubnis Mandantenentscheidung
- `hauptverhandlung-international-schnittstellen` — Hauptverhandlung International Schnittstellen
- `mandantenkommunikation-redteam-qualitygate` — Mandantenkommunikation Redteam Qualitygate
- `nebenfolgen-fahrerlaubnis-strafbefehl` — Nebenfolgen Fahrerlaubnis Strafbefehl
- `nebenfolgen-strafbefehl-strafbefehls` — Nebenfolgen Strafbefehl Strafbefehls
- `pflichtverteidigung-quellenkarte` — Pflichtverteidigung Quellenkarte
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Strafbefehl Verteidiger-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Beschuldigter.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
