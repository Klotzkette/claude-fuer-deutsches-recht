---
name: dokumente-intake
description: "Dokumentenintake für Berufsrechts-KI bei Vertragsprüfung: sortiert AVV-Vertrag, Mandatsvertrag, Datenschutzfolgeabschätzung, prüft Datum, Absender, Frist und Beweiswert (Tool-Dokumentation, Auftragsverarbeitungs-Verzeichnis); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Berufsrecht Ki Vertragspruefung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `ai-act-rollen-kanzlei-provider-deployer-api` — AI ACT Rollen Kanzlei Provider Deployer API
- `anbietern-belehrung-sonderfall-edge` — Anbietern Belehrung Sonderfall Edge
- `anbietern-schriftsatz-brief-memo-bausteine` — Anbietern Schriftsatz Brief Memo Bausteine
- `art-50-ki-vo-schriftsatz-marketing-chatbot` — ART 50 KI VO Schriftsatz Marketing Chatbot
- `avv-grenzpruefung-brki-anbieter-eu` — AVV Grenzpruefung Brki Anbieter EU
- `avv-grenzpruefung-datenschutz` — AVV Grenzpruefung Datenschutz
- `belehrung-abschlussprodukt-uebergabe` — Belehrung Abschlussprodukt Uebergabe
- `belehrung-abschlussprodukt-und-uebergabe` — Belehrung Abschlussprodukt und Uebergabe
- `berufsrecht-sonderfall-edge-case` — Berufsrecht Sonderfall Edge Case
- `berufsrecht-sonderfall-und-edge-case` — Berufsrecht Sonderfall und Edge Case
- `berufsrechtliche-bnoto-interessen-brao` — Berufsrechtliche Bnoto Interessen BRAO
- `bnoto-interessen` — Bnoto Interessen
- `bnoto-mehrparteien-konflikt-und-interessen` — Bnoto Mehrparteien Konflikt und Interessen
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Berufsrecht Ki Vertragspruefung-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: § 203 StGB, Consumer, § 43e BRAO, — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Anwalt/Kanzlei.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
