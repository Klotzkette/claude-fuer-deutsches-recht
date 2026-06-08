---
name: einstieg-routing
description: "Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Insolvenzforderungsanmeldungspruefung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `feststellung-forderungsgrund-rang-grund` — Feststellung Forderungsgrund Rang Grund
- `iap-anmeldepruefung-bauleiter-aussonderung-absonderung` — Iap Anmeldepruefung Bauleiter Aussonderung Absonderung
- `iap-rangordnung-ifap-aktenanlage-ifap-beleg` — Iap Rangordnung Ifap Aktenanlage Ifap Beleg
- `ifap-dubletten-serienforderungen-formalpruefung-grund-betrag` — Ifap Dubletten Serienforderungen Formalpruefung Grund Betrag
- `ifap-insolvenzforderungsanmeldungspruefung-intake` — Ifap Insolvenzforderungsanmeldungspruefung Intake
- `ifap-intake-kanalcheck-masseverbindlichkeit-abgrenzen` — Ifap Intake Kanalcheck Masseverbindlichkeit Abgrenzen
- `ifap-nachtraegliche-anmeldung-pruefungstermin-gate` — Ifap Nachtraegliche Anmeldung Pruefungstermin Gate
- `ifap-pruefentscheidung-vbuh` — Ifap Pruefentscheidung Vbuh
- `ifap-rang-nachrang-schuldnerwiderspruch-streitige-forderung` — Ifap Rang Nachrang Schuldnerwiderspruch Streitige Forderung
- `ifap-tabellenauszug-tabellenimport-verteilung-bestrittene` — Ifap Tabellenauszug Tabellenimport Verteilung Bestrittene
- `kanalcheck-beweislast-masseverbindlichkeit-sonderfall` — Kanalcheck Beweislast Masseverbindlichkeit Sonderfall
- `rang-tabellenauszug-tabellenimport` — Rang Tabellenauszug Tabellenimport
- `vbuh` — Vbuh

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Insolvenzforderungsanmeldungspruefung sind § 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Pr. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Insolvenzforderungsanmeldung typische Eskalationsstufen: Forderungsanmeldung mit Rang, Widerspruchsschreiben, Klage auf Feststellung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
