---
name: quellen-livecheck
description: "Quellen-Live-Check für Einfache/Leichte Sprache Jura: prüft Normen (BGG § 11 Leichte Sprache, UN-BRK Art. 9/21, BFSG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Behörden mit Verständlichkeitspflicht und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Einfache Leichte Sprache Jura** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `annaeherung-quellenkarte` — Annaeherung Quellenkarte
- `aufenthaltsrecht-mandant` — Aufenthaltsrecht Mandant
- `aufenthaltsrecht-mandant-betreuung` — Aufenthaltsrecht Mandant Betreuung
- `bauen-fristennotiz-naechster-schritt` — Bauen Fristennotiz Naechster Schritt
- `bauen-fristennotiz-und-naechster-schritt` — Bauen Fristennotiz und Naechster Schritt
- `bescheidmodus` — Bescheidmodus
- `bescheidmodus-02` — Bescheidmodus 02
- `betreuung-vormundschaft` — Betreuung Vormundschaft
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `einfache-sprache` — Einfache Sprache
- `experimentelle-glossar-sonderfall-jura` — Experimentelle Glossar Sonderfall Jura
- `experimentelle-schriftsatz-brief-memo-bausteine` — Experimentelle Schriftsatz Brief Memo Bausteine
- `familienrecht-erstgespraech` — Familienrecht Erstgespraech
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Einfache Leichte Sprache Jura (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.


## Normen & Rechtsprechung

Konkret zu prüfen:

- § 11 SGB I (Verständlichkeit)
- BGG (Behindertengleichstellungsgesetz) § 11
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21
## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
