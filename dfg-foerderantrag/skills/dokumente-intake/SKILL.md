---
name: dokumente-intake
description: "Dokumentenintake für DFG-Förderantrag: sortiert Projektbeschreibung, Finanzierungsplan, Lebenslauf, prüft Datum, Absender, Frist und Beweiswert (Publikationsverzeichnis, Vorarbeiten); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Dfg Foerderantrag** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `adaptive-dokumentenmatrix-lueckenliste` — Adaptive Dokumentenmatrix Lueckenliste
- `adaptive-dokumentenmatrix-und-lueckenliste` — Adaptive Dokumentenmatrix und Lueckenliste
- `anfaenger-antraege-dfg` — Anfaenger Antraege DFG
- `anfaenger-risikoampel-gegenargumente` — Anfaenger Risikoampel Gegenargumente
- `antraege-zahlen-schwellen-und-berechnung` — Antraege Zahlen Schwellen und Berechnung
- `antraege-zahlen-schwellenwerte-berechnung` — Antraege Zahlen Schwellenwerte Berechnung
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `dfg-bis-200k-begutachtung-light` — DFG BIS 200k Begutachtung Light
- `dfg-eigenanteil-und-grundausstattung` — DFG Eigenanteil und Grundausstattung
- `dfg-eigene-vorarbeiten-darstellen` — DFG Eigene Vorarbeiten Darstellen
- `dfg-erstantragsteller-besondere-checks` — DFG Erstantragsteller Besondere Checks
- `dfg-erstpruefung-und-mandatsziel` — DFG Erstpruefung und Mandatsziel
- `dfg-finanzplan-module-personal-geraete` — DFG Finanzplan Module Personal Geraete
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Regelungs- und Quellenanker

Arbeitsfokus: **Dokumentenintake**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 91b Abs. 1 GG` — Forschungsförderung im Bund-Länder-System.
- `§ 23 BHO` — Zuwendungsvoraussetzungen.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit und Sparsamkeit.
- `§ 48 Abs. 1 VwVfG` — Rücknahme rechtswidriger Bewilligungen.
- `§ 49 Abs. 1 VwVfG` — Widerruf rechtmäßiger Bewilligungen.
- `DFG-Kodex Leitlinie 1` — Redlichkeit.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung.
- `DFG-Kodex Leitlinie 14` — Autorschaft.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Dfg Foerderantrag-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: DFG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Antragsteller.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
