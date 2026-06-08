---
name: quellen-livecheck
description: "Quellen-Live-Check für Zitierweise deutsches Recht: prüft Normen (Standardzitierregeln (Gericht, Datum, Az, Fundstelle, Rn)) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt zuständige Stelle und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Zitierweise Deutsches Recht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `aktenzeichen-schriftsatz-brief-und-memo-bausteine` — Aktenzeichen Schriftsatz Brief und Memo Bausteine
- `aufsatz-interessen` — Aufsatz Interessen
- `aufsatz-interessen-beckrs-blindzitate` — Aufsatz Interessen Beckrs Blindzitate
- `beckrs-zahlen-schwellen-und-berechnung` — Beckrs Zahlen Schwellen und Berechnung
- `blindzitate-internationaler-bezug-und-schnittstellen` — Blindzitate Internationaler Bezug und Schnittstellen
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `datum-entscheidungsform-spezial-gericht` — Datum Entscheidungsform Spezial Gericht
- `entscheidungsform-risikoampel-und-gegenargumente` — Entscheidungsform Risikoampel und Gegenargumente
- `fristen-und-risikoampel` — Fristen und Risikoampel
- `gericht-dokumentenmatrix-und-lueckenliste` — Gericht Dokumentenmatrix und Lueckenliste
- `hauszitierweise-juristische-kommentar` — Hauszitierweise Juristische Kommentar
- `juristische-erstpruefung-und-mandatsziel` — Juristische Erstpruefung und Mandatsziel
- `kaltstart-triage` — Kaltstart Triage
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Regelungs- und Quellenanker

Arbeitsfokus: **Rechtsquellen-Livecheck**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — verantworteter Schriftsatz.
- `§ 138 Abs. 1 ZPO` — Wahrheit und Vollständigkeit.
- `§ 253 Abs. 2 ZPO` — bestimmter Klagegrund.
- `§ 313 Abs. 3 ZPO` — Entscheidungsgründe.
- `§ 540 Abs. 1 ZPO` — Berufungsurteil.
- `§ 267 Abs. 1 StPO` — strafgerichtliche Urteilsgründe.
- `§ 117 Abs. 2 VwGO` — verwaltungsgerichtliche Urteilsgründe.
- `§ 51 UrhG` — zulässiges Zitieren fremder Texte.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Zitierweise Deutsches Recht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
