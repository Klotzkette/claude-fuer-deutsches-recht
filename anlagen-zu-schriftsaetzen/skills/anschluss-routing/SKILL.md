---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Anlagen Zu Schriftsaetzen** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `anlage-red-anlagen-anlagenkonvolut-sonderfall-arial` — Anlage Red Anlagen Anlagenkonvolut Sonderfall Arial
- `anlagen-an-assistenz-uebersetzungspflicht-vorlagepflicht-zpo` — Anlagen An Assistenz Uebersetzungspflicht Vorlagepflicht Zpo
- `anlagen-aus-datenraum-und-sharepoint` — Anlagen Aus Datenraum Und Sharepoint
- `anlagen-aus-edv-systemen` — Anlagen Aus Edv Systemen
- `anlagen-aus-mandantenmaterial` — Anlagen Aus Mandantenmaterial
- `anlagen-bei-berufung-revision` — Anlagen Bei Berufung Revision
- `anlagen-bei-eilantrag-eu-arrest` — Anlagen Bei Eilantrag Eu Arrest
- `anlagen-berufung-revision-eilantrag-eu-bilder-screenshots` — Anlagen Berufung Revision Eilantrag Eu Bilder Screenshots
- `anlagen-bilder-screenshots` — Anlagen Bilder Screenshots
- `anlagen-check-zustellung-redaktion-dsgvo-schwaerzen-stempel` — Anlagen Check Zustellung Redaktion Dsgvo Schwaerzen Stempel
- `anlagen-duplikate-versionen-hashlog` — Anlagen Duplikate Versionen Hashlog
- `anlagen-elektronische-dokumente-format-dateinamen-bea-versand` — Anlagen Elektronische Dokumente Format Dateinamen Bea Versand
- `anlagen-elektronische-dokumente-spezial` — Anlagen Elektronische Dokumente Spezial
- `anlagen-format-und-dateinamen` — Anlagen Format Und Dateinamen

## Normenanker

Arbeitsfokus: **Anschluss-Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — Schriftsatzanforderungen.
- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 131 Abs. 1 ZPO` — Beifügung von Abschriften/Anlagen.
- `§ 133 Abs. 1 ZPO` — Abschriften für Zustellung.
- `§ 138 Abs. 1 ZPO` — Tatsachenvortrag.
- `§ 253 Abs. 2 ZPO` — Klageinhalt.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.
- `§ 371 Abs. 1 ZPO` — Augenschein.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Ergebnis sichten: Welche Anlagen Zu Schriftsaetzen-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Anlagen zu Schriftsätzen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
