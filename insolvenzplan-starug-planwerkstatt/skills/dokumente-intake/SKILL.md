---
name: dokumente-intake
description: "Dokumentenintake für Insolvenzplan / StaRUG: sortiert Insolvenzplan, Restrukturierungsplan, Gruppenbildung, prüft Datum, Absender, Frist und Beweiswert (Liquiditätsplan, Sanierungskonzept); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Insolvenzplan Starug Planwerkstatt** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `abstimmung-anlagen-interessen-cram` — Abstimmung Anlagen Interessen Cram
- `abstimmung-mehrheiten-anlagenpaket` — Abstimmung Mehrheiten Anlagenpaket
- `anlagen-mehrparteien-konflikt-und-interessen` — Anlagen Mehrparteien Konflikt und Interessen
- `anlagenpaket` — Anlagenpaket
- `asset-deals-im-plan-grundstuecke-marken-kundendaten` — Asset Deals im Plan Grundstuecke Marken Kundendaten
- `cram-formular-portal-und-einreichung` — Cram Formular Portal und Einreichung
- `cramdown-obstruktion-datenraum-register` — Cramdown Obstruktion Datenraum Register
- `darstellender-quellenkarte` — Darstellender Quellenkarte
- `darstellender-teil` — Darstellender Teil
- `datenraum-register` — Datenraum Register
- `down-red-gestaltender-gruppen` — Down RED Gestaltender Gruppen
- `gerichtliche-schritte-kommandocenter` — Gerichtliche Schritte Kommandocenter
- `gestaltender-teil` — Gestaltender Teil
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Insolvenzplan Starug Planwerkstatt-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: StaRUG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Schuldnerunternehmen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
