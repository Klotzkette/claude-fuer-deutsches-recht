---
name: dokumente-intake
description: "Dokumentenintake für Zwangsverwaltung ZVG: sortiert Anordnungsbeschluss, Verwalterbericht, Mietsachen-Akte, prüft Datum, Absender, Frist und Beweiswert (Mieteinnahmen, Reparaturen-Belege); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Zwangsverwaltung Zvg** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `aktenanlage-objektcockpit` — Aktenanlage Objektcockpit
- `berichte-beschlagnahme-mietverwaltung-besitz` — Berichte Beschlagnahme Mietverwaltung Besitz
- `berichtswesen-besitzuebernahme-bestellung` — Berichtswesen Besitzuebernahme Bestellung
- `beschlagnahme-fristen-form-und-zustaendigkeit` — Beschlagnahme Fristen Form und Zustaendigkeit
- `beschlagnahme-mietverwaltung-start` — Beschlagnahme Mietverwaltung Start
- `beschlagnahme-oeffentliche-lasten` — Beschlagnahme Oeffentliche Lasten
- `besitz-dokumentenmatrix-und-lueckenliste` — Besitz Dokumentenmatrix und Lueckenliste
- `besitzuebernahme` — Besitzuebernahme
- `bestellung-beschlagnahme` — Bestellung Beschlagnahme
- `betriebskosten-hausgeld-bieterangebot` — Betriebskosten Hausgeld Bieterangebot
- `bieterangebot-bewertung` — Bieterangebot Bewertung
- `bieterangebote-mieten-oeffentliche` — Bieterangebote Mieten Oeffentliche
- `gate-fehlerkatalog` — Gate Fehlerkatalog
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Zwangsverwaltung Zvg-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: ZVG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Gläubiger.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
