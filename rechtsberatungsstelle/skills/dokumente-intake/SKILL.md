---
name: dokumente-intake
description: "Dokumentenintake für Rechtsberatungsstelle (RDG): sortiert Beratungshilfeschein, Vermögenserklärung, Bescheide Sozialleistungen, prüft Datum, Absender, Frist und Beweiswert (Einkommensnachweise, Bescheide); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Rechtsberatungsstelle** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `anlaufstellen-beweislast-anleiter-bono` — Anlaufstellen Beweislast Anleiter Bono
- `anleiter-formular-portal-und-einreichung` — Anleiter Formular Portal und Einreichung
- `anleiter-pruefwarteschlange` — Anleiter Pruefwarteschlange
- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `bono-erstpruefung-und-mandatsziel` — Bono Erstpruefung und Mandatsziel
- `briefe-erstberatung-rdg-konform` — Briefe Erstberatung RDG Konform
- `einarbeitung` — Einarbeitung
- `einfache-sprache-briefe` — Einfache Sprache Briefe
- `entwurf-einarbeitung-einfache-sprache` — Entwurf Einarbeitung Einfache Sprache
- `erstberatung-rdg-grenzen-und-triage` — Erstberatung RDG Grenzen und Triage
- `erzeugung-leitfaden-erstellen-mandanten` — Erzeugung Leitfaden Erstellen Mandanten
- `fristen-fristenkontrolle-rdg` — Fristen Fristenkontrolle RDG
- `einstieg-routing` — Einstieg Routing
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Rechtsberatungsstelle-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: RDG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Hilfesuchender.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
