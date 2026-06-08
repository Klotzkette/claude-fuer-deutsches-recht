---
name: dokumente-intake
description: "Dokumentenintake für Energierecht (EnWG, EEG): sortiert Netzanschlussvertrag, EEG-Vergütungsbescheid, Marktstammdatenregister-Eintrag, prüft Datum, Absender, Frist und Beweiswert (Messdaten, Anschlussberichte); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Energierecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `anfrage-mehrparteien-konflikt-und-interessen` — Anfrage Mehrparteien Konflikt und Interessen
- `anschluss` — Anschluss
- `bess-abfall-recycling-rueckbau` — Bess Abfall Recycling Rueckbau
- `bess-abstandsflaechen-baurecht-brandenburg` — Bess Abstandsflaechen Baurecht Brandenburg
- `bess-baurecht-brandenburg` — Bess Baurecht Brandenburg
- `bess-behoerdenstrategie` — Bess Behoerdenstrategie
- `bess-bimschg-und-4-bimschv` — Bess Bimschg und 4 Bimschv
- `bess-brandschutz-co-location-datenschutz` — Bess Brandschutz CO Location Datenschutz
- `bess-co-location-pv-wind` — Bess CO Location PV Wind
- `bess-datenschutz-video-leitwarte` — Bess Datenschutz Video Leitwarte
- `bess-dieselgenerator-notstrom` — Bess Dieselgenerator Notstrom
- `bess-epc-fca-agnes-finanzierung` — Bess EPC FCA Agnes Finanzierung
- `bess-fca-agnes-bnetza` — Bess FCA Agnes BNETZA
- `einstieg-routing` — Einstieg Routing
- `quellen-livecheck` — Quellen Livecheck

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Energierecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: EEG, KWKG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Erzeuger.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
