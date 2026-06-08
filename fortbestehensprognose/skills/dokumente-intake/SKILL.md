---
name: dokumente-intake
description: "Dokumentenintake für Fortbestehensprognose StaRUG/InsO: sortiert Liquiditätsplan 24 Monate, Erfolgsplan, Bilanz, prüft Datum, Absender, Frist und Beweiswert (Bankbestätigungen, Forderungslisten); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fortbestehensprognose** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `annahmen-behoerden-gericht-und-registerweg` — Annahmen Behoerden Gericht und Registerweg
- `annahmen-belastbarkeit-plausibilisieren` — Annahmen Belastbarkeit Plausibilisieren
- `annahmen-sammeln-bilanzieller-status` — Annahmen Sammeln Bilanzieller Status
- `ausloesendes-ereignis-erfassen` — Ausloesendes Ereignis Erfassen
- `bilanzieller-status-aufnehmen` — Bilanzieller Status Aufnehmen
- `bilanzstatus-risikoampel-und-gegenargumente` — Bilanzstatus Risikoampel und Gegenargumente
- `comfortletter-sonderfall-edge` — Comfortletter Sonderfall Edge
- `comfortletter-weich-erzeugen` — Comfortletter Weich Erzeugen
- `eskalation-sonderfall-und-edge-case` — Eskalation Sonderfall und Edge Case
- `fbp-bankenkommunikation-waiver-integrierte` — FBP Bankenkommunikation Waiver Integrierte
- `fbp-integrierte-planung-bauleiter` — FBP Integrierte Planung Bauleiter
- `fbp-stresstest-szenarien-leitfaden` — FBP Stresstest Szenarien Leitfaden
- `fbp-zahlungsunfaehigkeit` — FBP Zahlungsunfaehigkeit
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fortbestehensprognose-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: InsO, StaRUG, § 19 Abs — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Geschäftsführung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
