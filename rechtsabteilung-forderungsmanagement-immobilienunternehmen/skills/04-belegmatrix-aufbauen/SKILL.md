---
name: 04-belegmatrix-aufbauen
description: "Belegmatrix nach Mietkonto und Aktenrekonstruktion aufbauen, wenn Forderungsposten, Tatsachen, SAP- oder DMS-Fundstellen und spätere K-/B-Anlagen verknüpft werden müssen. Nicht für Rohdatenintake oder PDF-Finalisierung. Output Beweis- und Beschaffungsmatrix."
---

# Belegmatrix aufbauen

## Zweck und Anwendungsfall

Jeder erhebliche Forderungsposten und jede tragende Tatsache brauchen eine auffindbare Quelle. Dieser Skill verbindet den bereits strukturierten Anspruch mit Beleg, Fundstelle, Beweisstatus und vorgesehener K-/B-Anlage. Er startet nach Mietkonto und Aktenrekonstruktion, nicht bei einem unsortierten Upload und nicht zur technischen PDF-Finalisierung.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Forderungsaufstellung aus Skill 03.
- Anlagenverzeichnis aus Skill 02.
- SAP-Belegnummern und DMS-Fundstellen zu Sollstellungen, Zahlungen, Mahnungen und Kündigung.

## Ablauf / Checkliste

1. Jeden Forderungsposten und jede streitige Anspruchsvoraussetzung einem Beweismittel und einer vorgesehenen Klage-Anlage zuordnen:

| Forderungsposten | Beweismittel | SAP-Beleg | Klage-Anlage | Beweisstatus |
|---|---|---|---|---|
| Miete 02 2025 | Sollstellung | KS 00347 | K3 | tragfähig |
| Teilzahlung 15.03 | Kontoauszug | BA 04 | K5 | prüfen |
| Mahnung 1 | Mahnschreiben | DMS 9832 | K6 | Zugang fehlt |

2. Pflichtbelege fallbezogen prüfen: Mietvertrag samt Nachträgen, Mietkonto für den Anspruchszeitraum, Sollgrund, Zahlungen, Zugangsbelege und die für den konkreten Antrag erheblichen Schreiben. Wohnflächenberechnung oder Kündigung nur verlangen, wenn sie tatsächlich anspruchserheblich sind.
3. Originalquelle, Datei, Seite oder Tabellenzeile, Datenstichtag und Konfliktstatus festhalten. Eine bloße SAP-Buchungszeile nicht als Beweis für Zugang oder rechtzeitige Zahlung behandeln.
4. Fehlende oder widersprüchliche Belege mit verantwortlicher Stelle, konkreter Beschaffungsfrage und Vorfrist in die Lückenliste aufnehmen.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen.

## Ausgabeformat

Belegmatrix mit Tatsache, Beleg, Quelle, Anlage, Beweisstatus, Lücke und nächster Beschaffung. Die Matrix bleibt tabellarisch; begleitende Bewertungen und Vermerke werden in vollständigen Sätzen ausformuliert (Ausformulierungspflicht).

## Beispiele

- Zur Mahnung 1 fehlt der Zugangsnachweis: Der Beweisstatus wird auf Zugang fehlt gesetzt und die Beschaffung des Einlieferungs- oder Zustellbelegs angestossen.
- Eine Sollstellung ist nur im SAP-Status, nicht im DMS belegt: Der Posten wird als prüfen markiert, bis die Belegquelle gesichert ist.
