---
name: quellen-livecheck
description: "Quellen-Live-Check für Forschungszulage FZulG: prüft Normen (FZulG, EStG § 3 Nr. 26b) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Bescheinigungsstelle Forschungszulage (BSFZ) und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Forschungszulage Antragstellung** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `abgrenzung-adaptiver-antrag` — Abgrenzung Adaptiver Antrag
- `abgrenzung-compliance` — Abgrenzung Compliance
- `ablehnung-nachbesserung-einspruch` — Ablehnung Nachbesserung Einspruch
- `adaptiver-dokumentenmatrix` — Adaptiver Dokumentenmatrix
- `adaptiver-dokumentenmatrix-und-lueckenliste` — Adaptiver Dokumentenmatrix und Lueckenliste
- `antrag-zahlen-schwellen-und-berechnung` — Antrag Zahlen Schwellen und Berechnung
- `antrag-zahlen-schwellenwerte` — Antrag Zahlen Schwellenwerte
- `antragstellung-auszahlung-beihilfen` — Antragstellung Auszahlung Beihilfen
- `auftragsforschung-vertragsgestaltung` — Auftragsforschung Vertragsgestaltung
- `auszahlung-internationaler-bezug` — Auszahlung Internationaler Bezug
- `auszahlung-internationaler-bezug-und-schnittstellen` — Auszahlung Internationaler Bezug und Schnittstellen
- `beihilfen-beweislast-darlegungslast` — Beihilfen Beweislast Darlegungslast
- `beihilfen-beweislast-und-darlegungslast` — Beihilfen Beweislast und Darlegungslast
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Normenanker

Arbeitsfokus: **Rechtsquellen-Livecheck**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1 FZulG` — Anspruchsberechtigung.
- `§ 2 Abs. 1 FZulG` — begünstigtes F&E-Vorhaben.
- `§ 3 FZulG` — förderfähige Aufwendungen.
- `§ 4 FZulG` — Höhe der Zulage.
- `§ 5 FZulG` — Antrag.
- `§ 6 FZulG` — Bescheinigung.
- `§ 10 FZulG` — Festsetzung/Auszahlung.
- `§ 90 Abs. 1 AO` — Mitwirkung und Belege.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Tragende Normen (FZulG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Forschungszulage Antragstellung (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
