---
name: quellen-livecheck
description: "Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Jveg Kostenpruefer** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `beschwerde-dolmetscher-sonderfall-dolmetscherkosten` — Beschwerde Dolmetscher Sonderfall Dolmetscherkosten
- `fahrtkosten-festsetzung-interessen-freistehender` — Fahrtkosten Festsetzung Interessen Freistehender
- `gate-beweislast-jveg-quality` — Gate Beweislast Jveg Quality
- `jveg-anspruchsberechtigung-antragsgenerator-dolmetscher` — Jveg Anspruchsberechtigung Antragsgenerator Dolmetscher
- `jveg-dolmetscher-uebersetzer-fahrtkosten-festsetzung-beschwerde` — Jveg Dolmetscher Uebersetzer Fahrtkosten Festsetzung Beschwerde
- `jveg-gate-rechenblatt-sachverstaendigenrechnung` — Jveg Gate Rechenblatt Sachverstaendigenrechnung
- `jveg-gerichtsschreiben-jveg-kuerzung-wegfall` — Jveg Gerichtsschreiben Jveg Kuerzung Wegfall
- `jveg-sonstige-aufwendungen-uebernachtung-aufwand` — Jveg Sonstige Aufwendungen Uebernachtung Aufwand
- `jveg-vorschuss-kostenrisiko-zeugenentschaedigung` — Jveg Vorschuss Kostenrisiko Zeugenentschaedigung
- `jveg-zeugenentschaedigung-sachverstaendigengutachten-ki` — Jveg Zeugenentschaedigung Sachverstaendigengutachten Ki
- `uebernachtung-verdienstausfall-vorschuss` — Uebernachtung Verdienstausfall Vorschuss
- `uebersetzer-fristennotiz-jveg-sachverstaendigenrechnung` — Uebersetzer Fristennotiz Jveg Sachverstaendigenrechnung
- `zeugenentschaedigung` — Zeugenentschaedigung

## Arbeitsweg

- Tragende Normen (JVEG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Jveg Kostenpruefer (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
