---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Insolvenzforderungsanmeldungspruefung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `feststellung-forderungsgrund-rang-grund` — Feststellung Forderungsgrund Rang Grund
- `iap-anmeldepruefung-bauleiter-aussonderung-absonderung` — Iap Anmeldepruefung Bauleiter Aussonderung Absonderung
- `iap-rangordnung-ifap-aktenanlage-ifap-beleg` — Iap Rangordnung Ifap Aktenanlage Ifap Beleg
- `ifap-dubletten-serienforderungen-formalpruefung-grund-betrag` — Ifap Dubletten Serienforderungen Formalpruefung Grund Betrag
- `ifap-insolvenzforderungsanmeldungspruefung-intake` — Ifap Insolvenzforderungsanmeldungspruefung Intake
- `ifap-intake-kanalcheck-masseverbindlichkeit-abgrenzen` — Ifap Intake Kanalcheck Masseverbindlichkeit Abgrenzen
- `ifap-nachtraegliche-anmeldung-pruefungstermin-gate` — Ifap Nachtraegliche Anmeldung Pruefungstermin Gate
- `ifap-pruefentscheidung-vbuh` — Ifap Pruefentscheidung Vbuh
- `ifap-rang-nachrang-schuldnerwiderspruch-streitige-forderung` — Ifap Rang Nachrang Schuldnerwiderspruch Streitige Forderung
- `ifap-tabellenauszug-tabellenimport-verteilung-bestrittene` — Ifap Tabellenauszug Tabellenimport Verteilung Bestrittene
- `kanalcheck-beweislast-masseverbindlichkeit-sonderfall` — Kanalcheck Beweislast Masseverbindlichkeit Sonderfall
- `rang-tabellenauszug-tabellenimport` — Rang Tabellenauszug Tabellenimport
- `vbuh` — Vbuh

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Insolvenzforderungsanmeldungspruefung-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: § 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Pr — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Gläubiger.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
