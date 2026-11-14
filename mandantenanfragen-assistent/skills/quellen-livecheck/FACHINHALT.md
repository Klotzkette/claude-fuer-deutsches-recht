---
name: quellen-livecheck
description: "Für Rechtsquellen-Livecheck: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: mandantenanfragen-assistent."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Mandantenanfragen Assistent** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `anfrage-eingang-parser` — Anfrage Eingang Parser
- `anrede-anwaltskanzleien-bittet` — Anrede Anwaltskanzleien Bittet
- `anrede-uebernehmen` — Anrede Uebernehmen
- `anwaltskanzleien-erstpruefung-und-mandatsziel` — Anwaltskanzleien Erstpruefung und Mandatsziel
- `bietet-fehlerkatalog` — Bietet Fehlerkatalog
- `bittet-internationaler-bezug-und-schnittstellen` — Bittet Internationaler Bezug und Schnittstellen
- `dankt-dsgvo-sonderfall-e-mail` — Dankt DSGVO Sonderfall E Mail
- `dringlichkeitsmarker-einwilligung-hinweis` — Dringlichkeitsmarker Einwilligung Hinweis
- `dsgvo-sonderfall-und-edge-case` — DSGVO Sonderfall und Edge Case
- `e-mail-erstantwort-und-terminrouting` — E Mail Erstantwort und Terminrouting
- `eingehenden-quellenkarte` — Eingehenden Quellenkarte
- `einwilligung-hinweis-datenschutz` — Einwilligung Hinweis Datenschutz
- `einwilligungshinweis-fristennotiz-und-naechster-schritt` — Einwilligungshinweis Fristennotiz und Naechster Schritt
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (DSGVO) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Mandantenanfragen Assistent (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
