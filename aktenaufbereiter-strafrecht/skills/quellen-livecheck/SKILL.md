---
name: quellen-livecheck
description: "Quellen-Live-Check für Strafrechtliche Aktenaufbereitung: prüft Normen (§§ 147 StPO Akteneinsicht, § 200 StPO Anklageschrift, § 397a StPO Nebenklage) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Staatsanwaltschaft und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Aktenaufbereiter Strafrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `aktenaufbereiter-erstpruefung-und-mandatsziel` — Aktenaufbereiter Erstpruefung und Mandatsziel
- `aktenaufbereiter-strafrecht` — Aktenaufbereiter Strafrecht
- `akteneinsicht-uebersicht-aktenvorblatt` — Akteneinsicht Uebersicht Aktenvorblatt
- `aktenlektuere-fristennotiz-und-naechster-schritt` — Aktenlektuere Fristennotiz und Naechster Schritt
- `aktenvorblatt-erstellen` — Aktenvorblatt Erstellen
- `aktenvorblatt-schriftsatz-brief-und-memo-bausteine` — Aktenvorblatt Schriftsatz Brief und Memo Bausteine
- `anklageschrift-zerlegen` — Anklageschrift Zerlegen
- `aussageanalyse-aussagepsychologie` — Aussageanalyse Aussagepsychologie
- `beweismittel-katalog-beweisverwertungsverbote` — Beweismittel Katalog Beweisverwertungsverbote
- `beweisverwertungsverbote-pruefen` — Beweisverwertungsverbote Pruefen
- `beziehungen-spezial-chronologie-ergaenzbar` — Beziehungen Spezial Chronologie Ergaenzbar
- `beziehungsmatrix-personen-taten` — Beziehungsmatrix Personen Taten
- `chronologie-compliance-dokumentation-und-akte` — Chronologie Compliance Dokumentation und Akte
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Aktenaufbereiter Strafrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
