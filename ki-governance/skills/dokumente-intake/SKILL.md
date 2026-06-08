---
name: dokumente-intake
description: "Dokumentenintake für KI-Governance: sortiert Risikobewertung, Konformitätserklärung, Technische Dokumentation, prüft Datum, Absender, Frist und Beweiswert (Logs, Bias-Tests); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Ki Governance** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `anbieter-mehrparteien-konflikt-und-interessen` — Anbieter Mehrparteien Konflikt und Interessen
- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `anwendungsfall-triage` — Anwendungsfall Triage
- `case-dpia-drift` — Case Dpia Drift
- `dpia-risikoampel-und-gegenargumente` — Dpia Risikoampel und Gegenargumente
- `drift-verhandlung-vergleich-und-eskalation` — Drift Verhandlung Vergleich und Eskalation
- `dsgvo-governance-inventar` — DSGVO Governance Inventar
- `fristen-risikoampel-mandantenkommunikation` — Fristen Risikoampel Mandantenkommunikation
- `governance-compliance-dokumentation-und-akte` — Governance Compliance Dokumentation und Akte
- `gpai-modelle-ki-anbieter-arbeitsrecht` — Gpai Modelle KI Anbieter Arbeitsrecht
- `inventar-dokumentenmatrix-und-lueckenliste` — Inventar Dokumentenmatrix und Lueckenliste
- `inventar-kontrollen-konformitaetsbewertung` — Inventar Kontrollen Konformitaetsbewertung
- `einstieg-routing` — Einstieg Routing
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Ki Governance-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: DSGVO — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Anbieter, Betreiber, Importeur, Händler.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
