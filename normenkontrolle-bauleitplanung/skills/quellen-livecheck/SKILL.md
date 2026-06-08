---
name: quellen-livecheck
description: "Quellen-Live-Check für Normenkontrolle Bauleitplanung: prüft Normen (BauGB §§ 1/2/10, § 47 VwGO Normenkontrolle) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt OVG/VGH und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Normenkontrolle Bauleitplanung** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `abwaegung-formular-portal` — Abwaegung Formular Portal
- `abwaegung-formular-portal-und-einreichung` — Abwaegung Formular Portal und Einreichung
- `abwaegungsgebot-1-abs-7-baugb` — Abwaegungsgebot 1 ABS 7 Baugb
- `anfechtung-antragsbefugnis-red-team-korrektur` — Anfechtung Antragsbefugnis RED Team Korrektur
- `anfechtung-tatbestandsmerkmale` — Anfechtung Tatbestandsmerkmale
- `anpassungsgebot-flaechennutzungsplan` — Anpassungsgebot Flaechennutzungsplan
- `antragsbefugnis-eigentuemer-nachbar` — Antragsbefugnis Eigentuemer Nachbar
- `antragsbefugnis-fehlerkatalog` — Antragsbefugnis Fehlerkatalog
- `antragsbefugnis-red-team-und-qualitaetskontrolle` — Antragsbefugnis RED Team und Qualitaetskontrolle
- `antragstellervertretung-zahlen-schwellen-und-berechnung` — Antragstellervertretung Zahlen Schwellen und Berechnung
- `artenschutz-naturschutz-aufstellungsbeschluss` — Artenschutz Naturschutz Aufstellungsbeschluss
- `artenschutz-naturschutz-planung` — Artenschutz Naturschutz Planung
- `aufstellungsbeschluss-bekanntmachung` — Aufstellungsbeschluss Bekanntmachung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (§ 47 VwGO vor BayVGH und OVG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Normenkontrolle Bauleitplanung (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
