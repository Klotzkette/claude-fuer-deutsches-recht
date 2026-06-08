---
name: quellen-livecheck
description: "Quellen-Live-Check für Produktrecht (ProdSG/CE): prüft Normen (ProdSG, GPSR EU 2023/988, ProdHaftG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Marktüberwachung Länder und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Produktrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `belegmatrix-mandantenkommunikation-entscheidungsvorlage` — Belegmatrix Mandantenkommunikation Entscheidungsvorlage
- `bewertungen-red-team-impressumspflicht` — Bewertungen RED Team Impressumspflicht
- `ce-kennzeichnung-routenplan` — CE Kennzeichnung Routenplan
- `chronologie-red-team-und-qualitaetskontrolle` — Chronologie RED Team und Qualitaetskontrolle
- `dual-use-produktrecht` — Dual USE Produktrecht
- `eu-produktsicherheitsverordnung-feature` — EU Produktsicherheitsverordnung Feature
- `feature-risikobewertung` — Feature Risikobewertung
- `fristen-risikoampel-mandantenkommunikation` — Fristen Risikoampel Mandantenkommunikation
- `impressum-pflicht` — Impressum Pflicht
- `impressumspflicht-dokumentenmatrix-und-lueckenliste` — Impressumspflicht Dokumentenmatrix und Lueckenliste
- `ist-ki-act-marktueberwachung-kommunikation` — IST KI ACT Marktueberwachung Kommunikation
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Tragende Normen (ProdHaftG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Produktrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
