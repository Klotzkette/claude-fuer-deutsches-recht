---
name: dokumente-intake
description: "Dokumentenintake für Kanzlei-Builder-Hub (Plugins/Skills): sortiert Plugin-Konfiguration, Skill-Definitionen, Mandanten-AVV, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Kanzlei Builder Hub** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `automatischer-aktualisierer` — Automatischer Aktualisierer
- `builder-zahlen-schwellen-und-berechnung` — Builder Zahlen Schwellen und Berechnung
- `community-leistungsmatrix-fristennotiz` — Community Leistungsmatrix Fristennotiz
- `daten-red-team-und-qualitaetskontrolle` — Daten RED Team und Qualitaetskontrolle
- `deaktivieren` — Deaktivieren
- `deinstallieren` — Deinstallieren
- `deployment-eigenen-einsteiger` — Deployment Eigenen Einsteiger
- `eigenen-formular-portal-und-einreichung` — Eigenen Formular Portal und Einreichung
- `einsteiger-mandantenkommunikation-entscheidungsvorlage` — Einsteiger Mandantenkommunikation Entscheidungsvorlage
- `findet-gate-installiert` — Findet Gate Installiert
- `fristen-risikoampel-mandantenkommunikation` — Fristen Risikoampel Mandantenkommunikation
- `einstieg-routing` — Einstieg Routing
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Kanzlei Builder Hub-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Kanzleiinhaber.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
