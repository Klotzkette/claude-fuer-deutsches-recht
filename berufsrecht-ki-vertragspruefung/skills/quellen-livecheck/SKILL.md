---
name: quellen-livecheck
description: "Quellen-Live-Check für Berufsrechts-KI bei Vertragsprüfung: prüft Normen (§ 43a BRAO, § 50 BRAO Aktenführung, DSGVO Art. 28 AVV) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt RAK und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Berufsrecht Ki Vertragspruefung** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


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
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (§ 203 StGB, Consumer, § 43e BRAO,) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Berufsrecht Ki Vertragspruefung (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
