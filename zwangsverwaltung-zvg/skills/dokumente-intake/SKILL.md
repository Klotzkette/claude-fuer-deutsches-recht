---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Zwangsverwaltung Zvg** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `berichte-beschlagnahme-mietverwaltung-besitz` — Berichte Beschlagnahme Mietverwaltung Besitz
- `betriebskosten-hausgeld-bieterangebot-bewertung-glaeubiger` — Betriebskosten Hausgeld Bieterangebot Bewertung Glaeubiger
- `bieterangebote-mieten-öffentliche` — Bieterangebote Mieten Oeffentliche
- `insolvenz-schnittstelle-instandhaltung-sicherung-zvg` — Insolvenz Schnittstelle Instandhaltung Sicherung Zvg
- `konten-kassenfuehrung-miet-pachtverwaltung-mieteinzug` — Konten Kassenfuehrung Miet Pachtverwaltung Mieteinzug
- `quality-recherche-rechnungslegung` — Quality Recherche Rechnungslegung
- `treuhandkonto-versteigerung-versteigerungsteilnahme` — Treuhandkonto Versteigerung Versteigerungsteilnahme
- `versicherungen-gefahren-zvg-versteigerungsteilnahme-zvg` — Versicherungen Gefahren Zvg Versteigerungsteilnahme Zvg
- `verteilung-zwangsverwaltung-aktenanlage-objektcockpit` — Verteilung Zwangsverwaltung Aktenanlage Objektcockpit
- `zvg-berichtswesen-besitzuebernahme-bestellung-beschlagnahme` — Zvg Berichtswesen Besitzuebernahme Bestellung Beschlagnahme
- `zvg-recherche-quality-gate-raeumung-kuendigung` — Zvg Recherche Quality Gate Raeumung Kündigung
- `zvg-rechnungslegung-simulation-training-verkauf-versteigerung` — Zvg Rechnungslegung Simulation Training Verkauf Versteigerung
- `zwvw-anordnung-zwangsverwaltung-kostenrechnung-verwalter` — Zwvw Anordnung Zwangsverwaltung Kostenrechnung Verwalter

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
