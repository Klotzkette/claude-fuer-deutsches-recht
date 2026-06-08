---
name: quellen-livecheck
description: "Quellen-Live-Check für Fachanwalt Verkehrsrecht: prüft Normen (StGB §§ 142/315c, 316, StVG, StVO) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt AG (Bußgeld + Straf) und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Fachanwalt Verkehrsrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `autonom-bezuege-fachanwalt` — Autonom Bezuege Fachanwalt
- `blitzer-messung-paragraf-3-stvo` — Blitzer Messung Paragraf 3 Stvo
- `bussgeld-unfall-haftungsquote-vkr` — Bussgeld Unfall Haftungsquote VKR
- `dieselskandal-paragraf-826-bgb` — Dieselskandal Paragraf 826 BGB
- `erstgespraech-mandatsannahme-verkehr-autonom` — Erstgespraech Mandatsannahme Verkehr Autonom
- `fa-verkehrsrecht-fristen-risiko-mandant` — FA Verkehrsrecht Fristen Risiko Mandant
- `fahrerlaubnis-entzug-paragraf-3-stvg` — Fahrerlaubnis Entzug Paragraf 3 Stvg
- `fahrerlaubnis-kanzlei-personen` — Fahrerlaubnis Kanzlei Personen
- `haftpflicht-paragraf-115-vvg` — Haftpflicht Paragraf 115 VVG
- `kaskoversicherung-paragraf-81-vvg-bgh-iv-zr-25-21` — Kaskoversicherung Paragraf 81 VVG BGH IV ZR 25 21
- `kfz-handel-paragraf-434-bgb` — KFZ Handel Paragraf 434 BGB
- `mandat-triage-schriftsatzkern-substantiierung` — Mandat Triage Schriftsatzkern Substantiierung
- `mpu-vorbereitung-orientierung` — MPU Vorbereitung Orientierung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (PflVG, StVG, VVG, §§ 315c 316 StGB) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Fachanwalt Verkehrsrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
