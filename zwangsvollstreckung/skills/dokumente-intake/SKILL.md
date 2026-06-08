---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Zwangsvollstreckung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `bank-haertefall-inso` — Bank Haertefall Inso
- `kontenpfaendung-notar-interessen-online` — Kontenpfaendung Notar Interessen Online
- `mahnbescheid-fristennotiz-zv-titel-zv-kontensuche` — Mahnbescheid Fristennotiz Zv Titel Zv Kontensuche
- `pfueb-raeumung-schuldnerschutz-beweislast` — Pfueb Raeumung Schuldnerschutz Beweislast
- `vermoegensauskunft-vollstreckungsbescheid-vollstreckungstitel` — Vermoegensauskunft Vollstreckungsbescheid Vollstreckungstitel
- `zpo-zwangsvollstreckung-zv-abwehr` — Zpo Zwangsvollstreckung Zv Abwehr
- `zv-elektronische-zv-eu-zv` — Zv Elektronische Zv Eu Zv
- `zv-mahnbescheid-zv-mobiliar-zv-notarielle` — Zv Mahnbescheid Zv Mobiliar Zv Notarielle
- `zv-pfaendungstabelle-zv-pfueb-zv-pfueb` — Zv Pfaendungstabelle Zv Pfueb Zv Pfueb
- `zv-pfueb-802l-arbeit` — Zv Pfueb 802l Arbeit
- `zv-raeumung-zv-tabellenauszug-zv-vermoegensauskunft` — Zv Raeumung Zv Tabellenauszug Zv Vermoegensauskunft
- `zv-vollstreckungsbescheid-zv-vollstreckungsschutz-zv-zvg` — Zv Vollstreckungsbescheid Zv Vollstreckungsschutz Zv Zvg
- `zwv-pfaendung-konto-vollstreckungsschutz-billigkeit` — Zwv Pfaendung Konto Vollstreckungsschutz Billigkeit

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Zwangsvollstreckung-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: ZPO, § 201 InsO, ZVG, EU, § 765a H, § 800 ZPO Notar,, § 802l Kontensuche, Verm, §§ 704 ff — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Gläubiger.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
