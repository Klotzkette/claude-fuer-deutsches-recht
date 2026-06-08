---
name: quellen-livecheck
description: "Quellen-Live-Check für E-Mail-Umformulierung im Berufsrecht: prüft Normen (§ 43a BRAO, § 49b BRAO, BORA) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt RAK und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Email Umformulierer Berufsrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `allgemeine-sonderfall-edge-case` — Allgemeine Sonderfall Edge Case
- `anrede-und-grussformeln` — Anrede und Grussformeln
- `berufliche-fristennotiz-emotionale` — Berufliche Fristennotiz Emotionale
- `berufliche-fristennotiz-naechster-schritt` — Berufliche Fristennotiz Naechster Schritt
- `berufsrechtskonform-verhandlung-vergleich-und-eskalation` — Berufsrechtskonform Verhandlung Vergleich und Eskalation
- `bora-internationaler-bezug-und-schnittstellen` — BORA Internationaler Bezug und Schnittstellen
- `bora-konformitaetspruefung` — BORA Konformitaetspruefung
- `bora-konformitaetspruefung-brao-email` — BORA Konformitaetspruefung BRAO Email
- `brao-interessen-fokus-formuliert` — BRAO Interessen Fokus Formuliert
- `brao-konformitaetspruefung` — BRAO Konformitaetspruefung
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `edge-case-verhandlung-bora-international` — Edge Case Verhandlung BORA International
- `email-berufsrecht-berufliche-korrespondenz` — Email Berufsrecht Berufliche Korrespondenz
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Email Umformulierer Berufsrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
