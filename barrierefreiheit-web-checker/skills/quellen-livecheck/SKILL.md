---
name: quellen-livecheck
description: "Quellen-Live-Check für Barrierefreiheit Web BFSG/WCAG: prüft Normen (BFSG, BFSG-Verordnung, WCAG 2.1 AA) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt BFA (Bundesfachstelle Barrierefreiheit) und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Barrierefreiheit Web Checker** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `abnahme-formular-portal-und-einreichung` — Abnahme Formular Portal und Einreichung
- `agentur-abnahme-vergabe` — Agentur Abnahme Vergabe
- `audit-barrierefreiheits-bfsg` — Audit Barrierefreiheits Bfsg
- `automatisierter-audit-axe-lighthouse` — Automatisierter Audit AXE Lighthouse
- `barrierefreiheit-fehlerkatalog` — Barrierefreiheit Fehlerkatalog
- `barrierefreiheits-erstpruefung-und-mandatsziel` — Barrierefreiheits Erstpruefung und Mandatsziel
- `bf-kanzleiwebsite-konkret` — BF Kanzleiwebsite Konkret
- `bf-kiosk-selbstbedienung-mediendienste` — BF Kiosk Selbstbedienung Mediendienste
- `bf-mediendienste-untertitel-spezial` — BF Mediendienste Untertitel Spezial
- `bf-pdf-schriftsaetze-versand` — BF PDF Schriftsaetze Versand
- `bfsg-tatbestand-beweis-und-belege` — Bfsg Tatbestand Beweis und Belege
- `bfsg-zeitleiste-ecommerce-checkout-en301549` — Bfsg Zeitleiste Ecommerce Checkout En301549
- `bfsgv-schulung-fristennotiz-agentur-abnahme` — Bfsgv Schulung Fristennotiz Agentur Abnahme
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (BFSG, BITV 2.0, EU 2016/2102, EAA-RL 2019/882, WCAG 2.1 / 2.2 (AA), DIN EN 301 549) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Web-Barrierefreiheit (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
