---
name: quellen-livecheck
description: "Quellen-Live-Check für KI-Richtlinie für Kanzleien: prüft Normen (BRAO § 43e, BORA, DSGVO Art. 28) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt RAK und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Ki Richtlinie Kanzleien** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `anonymisierung-pseudonymisierung` — Anonymisierung Pseudonymisierung
- `anwaelten-berufsrechtskonforme-beruht` — Anwaelten Berufsrechtskonforme Beruht
- `auftragsverarbeitungsvertrag-pruefen` — Auftragsverarbeitungsvertrag Pruefen
- `automatisierte-entscheidungen-art-22-dsgvo` — Automatisierte Entscheidungen ART 22 DSGVO
- `berufsrecht-bausteine` — Berufsrecht Bausteine
- `berufsrechtskonforme-tatbestand-beweis-und-belege` — Berufsrechtskonforme Tatbestand Beweis und Belege
- `beruht-verhandlung-vergleich-und-eskalation` — Beruht Verhandlung Vergleich und Eskalation
- `bias-diskriminierung-regelsatz-erstellen` — Bias Diskriminierung Regelsatz Erstellen
- `bora-brak-dsgvo` — BORA Brak DSGVO
- `brak-internationaler-bezug-und-schnittstellen` — Brak Internationaler Bezug und Schnittstellen
- `brao-quellenkarte` — BRAO Quellenkarte
- `compliance-regelsatz-erstellen` — Compliance Regelsatz Erstellen
- `dienstleister-due-diligence` — Dienstleister DUE Diligence
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (DSGVO) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Ki Richtlinie Kanzleien (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
