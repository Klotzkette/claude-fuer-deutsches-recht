---
name: 02-mietakte-rekonstruieren
description: "Mietvertrag mit Nachträgen rekonstruieren. Wohnraum und Gewerberaum, Form, Indexklausel, Staffelmiete, Schönheitsreparaturen und Betriebskostenkatalog prüfen. Fehlende Anlagen aus SAP DMS erkennen. Output Anlagenverzeichnis für spätere Klage."
---

# Mietakte rekonstruieren

## Zweck und Anwendungsfall

Der Mietvertrag liegt in SAP DMS als gescannte PDF. Dieser Skill baut daraus eine vollständige, durchsuchbare Akte und ein Anlagenverzeichnis, das eine spätere Klage tragen kann. Anwendungsfall ist die Vorbereitung jedes streitigen Vorgangs.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Gescannter Hauptmietvertrag und alle Nachträge aus SAP DMS.
- Begleitunterlagen (Wohnflächenberechnung, Übergabeprotokoll, Kautionsquittung, Betriebskostenabrechnungen).
- SAP-Stammdaten aus Skill 01 zur Abgleichung.

## Ablauf / Checkliste

1. Vorhandene Komponenten erfassen und auf Pflichtstatus prüfen:

| Dokument | Pflicht |
|---|---|
| Hauptmietvertrag | ja |
| Nachträge chronologisch | wenn vorhanden |
| Wohnflächenberechnung | ja |
| Übergabeprotokoll | ja |
| Hausordnung | wenn vereinbart |
| Kautionsquittung | ja |
| Betriebskostenabrechnungen 3 Jahre | ja |
| Historische Mieterhöhungen | wenn vorhanden |

2. Vertragsparteien mit den SAP-Stammdaten abgleichen.
3. Mietobjekt auf eindeutige Bezeichnung prüfen.
4. Fälligkeit und Rechtzeitigkeit nach Paragraf 556b BGB getrennt prüfen. Bei Wohnraummiete zählt Sonnabend für diese Zahlungsfrist nicht. Im Überweisungsverkehr genügt bei gedecktem Konto der bis zum dritten Werktag erteilte Zahlungsauftrag; ein späterer Kontoeingang beweist allein keine Verspätung. BGH VIII ZR 129/09, VIII ZR 291/09 und VIII ZR 222/15 als Kontrollanker nutzen.
5. Nutzungsart vor der Formprüfung festlegen. Bei Wohnraum gilt für eine Vertragsdauer von mehr als einem Jahr die Schriftformfolge aus Paragraf 550 BGB. Bei Grundstücks- und Gewerberaummiete gilt über Paragraf 578 Abs. 1 und 2 BGB die Textform; die Übergangsfrist für vor dem 01.01.2025 entstandene Verträge nach Art. 229 Paragraf 70 Abs. 1 EGBGB ist seit Ablauf des 01.01.2026 beendet. Hauptvertrag, Nachtrag, Laufzeitänderung, Optionsausübung und Bezugsurkunden chronologisch auf die jeweils einschlägige Form prüfen; keine Wohnraumregel auf Gewerberaum übertragen.
6. Gesetzgebungsstatus bei Sondermietformen sperren: BT-Drs. 21/6807 ist am 09.08.2026 nur an die Ausschüsse überwiesener Entwurf. Die dort vorgeschlagene Sechsmonatsgrenze mit möglicher Verlängerung auf acht Monate für vorübergehenden Gebrauch und die geplante Indexmietbegrenzung sind nicht geltendes Recht. Aktuelle Paragrafen 549 und 557b BGB anwenden; Ergebnis mit Normabrufdatum dokumentieren.
7. Mietanpassung nach Nutzungsart trennen. Bei Wohnraum Staffelmiete nach Paragraf 557a BGB und Indexmiete nach Paragraf 557b BGB prüfen. Bei Gewerberaum formularmäßige Indexklauseln zusätzlich zum Preisklauselgesetz nach Paragraf 307 BGB kontrollieren: Nach BGH XII ZR 51/25 ist eine AGB-rechtlich unwirksame Klausel ex tunc unwirksam; Paragraf 8 PrKG verdrängt diese Rechtsfolge nicht. Bei unklarer Klausel, Rückforderung oder erheblicher Rückwirkung rote RA-Eskalation.
8. Betriebskostenkatalog im Vertrag oder per Verweis prüfen.
9. Jede Vertragsfassung mit Datum, Quelle und Version markieren.
10. Widerspruch zwischen SAP-Stammdaten und Vertragsurkunde als rote Lücke ausweisen.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen. Für Gewerberaum-Indexklauseln BGH XII ZR 51/25 aus `references/gepruefte-bgh-anker-mietrecht.md` verwenden und ausdrücklich als Gewerberaumentscheidung kennzeichnen. Für den Status von BT-Drs. 21/6807 gilt `references/rechtsstand-2026-verfahren-vollstreckung.md`.

## Ausgabeformat

Anlagenverzeichnis K1 bis Kn mit Beweisbehauptung, Dateiquelle, Version, Pflichtstatus und Lückenampel pro Anlage. Das Verzeichnis bleibt tabellarisch; begleitende Bewertungen und Vermerke werden in vollständigen Sätzen ausformuliert (Ausformulierungspflicht).

## Beispiele

- Fehlt das Übergabeprotokoll, wird die betreffende Zeile mit roter Ampel und einer Beschaffungsaufgabe an die Hausverwaltung versehen.
- Eine im Vertrag vereinbarte Staffelmiete wird als eigene Anlage geführt und für die spätere Forderungsaufstellung markiert.
