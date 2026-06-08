---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Zitierweise deutsches Recht: ordnet Rolle (Autor, Korrektor, Mandant), markiert Frist (keine harten Fristen), wählt Norm (Standardzitierregeln (Gericht, Datum, Az, Fundstelle, Rn)) und Zuständigkeit (zuständige Stelle), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Zitierweise Deutsches Recht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


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

Arbeitsfokus: **Einstieg und Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

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

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Zitierweise Deutsches Recht sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Zitierweise deutsches Recht typische Eskalationsstufen: Zitiernachweis, Quellenverzeichnis, Korrektur falsch zitierter Stellen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
