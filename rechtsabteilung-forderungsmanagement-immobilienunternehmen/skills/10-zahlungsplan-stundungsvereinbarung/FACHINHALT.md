---
name: 10-zahlungsplan-stundungsvereinbarung
description: "Zahlungsplan, Ratenplan, Teilzahlungsvereinbarung, Stundung, Schuldanerkenntnis und Verfallklausel aufsetzen oder gebrochenen Ratenplan auswerten. Restbetrag, laufende Miete und Wiedervorlage steuern. Output Vereinbarung."
---

# Ratenvereinbarung Stundung

## Zweck und Anwendungsfall

Dieser Skill setzt eine Raten- und Stundungsvereinbarung auf, mit der ein Rückstand geordnet getilgt und die gerichtliche Geltendmachung zeitweise gestundet wird. Anwendungsfall ist ein zahlungswilliger, vorübergehend zahlungsunfähiger Mieter.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Bezifferte Hauptforderung aus der Forderungsaufstellung.
- Vorschlag zu Ratenhöhe und Laufzeit.
- Interne Freigabe für ein Forderungsanerkenntnis und für Laufzeiten über zwölf Monate.

## Ablauf / Checkliste

1. Regelungspunkte prüfen: bezifferte Hauptforderung; Anerkenntnis nur nach Freigabe, weil es nach Paragraf 212 Abs. 1 Nr. 1 BGB einen Verjährungsneubeginn auslösen kann; Fälligkeit jeder Rate; genaue Stundungswirkung; laufende Miete; bestehende Kündigung; künftige Kündigungsrechte; Kosten; Sicherheit. Eine Gesamtfälligkeits- oder Verfallklausel ist optional und darf nicht automatisch eingefügt werden. Sie braucht transparente Voraussetzungen, gesonderte Freigabe und bei Formularverwendung eine AGB-Prüfung nach Paragrafen 305c und 307 BGB.
2. Vereinbarung nach folgendem Aufbau ausformulieren:

```
Ratenzahlungsvereinbarung
zwischen Vermieterin und Mieter

1. Hauptforderung Mietrückstand Stand [Datum] EUR [S] nebst Zinsen.
2. [Nur nach Freigabe:] Der Mieter erkennt die Forderung dem Grunde und der Höhe nach an.
3. Tilgung in [n] Raten je EUR [R], fällig zum 15. eines Monats.
4. [Nur nach gesonderter Freigabe:] Bleibt eine Rate länger als 14 Tage nach Fälligkeit offen, kann die Vermieterin den noch offenen Rest nach schriftlicher Erklärung fällig stellen. Gesetzliche und vertragliche Wirksamkeitsgrenzen bleiben geprüft.
5. Die laufende Miete bleibt unberührt.
6. Die Vermieterin stundet die in Nummer 1 bezeichnete Restforderung nach Maßgabe des Ratenplans, solange vertragsgemäß gezahlt wird. Die Wirkung auf bereits erklärte oder erwogene Kündigungen wird in einer gesonderten Freigabekarte festgehalten.
```

3. Renofa-Praxis beachten: wirtschaftliche Plausibilitätsprüfung nur aus vorhandenen, zweckgebundenen Akten- und Zahlungsdaten; bei wiederholtem Ratenbruch Kündigungs- und Klagepfad neu prüfen; Maximalfrist zwölf Monate ohne Abteilungsleitung; Ratenplan immer in Monitoring und Wiedervorlage übergeben. Keine Klausel darf suggerieren, eine Stundung lasse Fälligkeit, Verzug oder Kündigungsgrund unverändert.
4. Getrennte Freigabekarte erstellen: anerkannter Ausgangsbetrag, aktuelle Zahlungen, Rate, Fälligkeit, laufende Miete, Verfallklausel, Kosten, Laufzeit, Zeichnungsbefugnis und Wiedervorlagen. Bis zur dokumentierten Freigabe Status `ENTWURF - NICHT VERSENDEN/EINREICHEN`.

## Argumentationsstandard

Jede Klausel muss Auslöser, Handlungspflicht und Rechtsfolge eindeutig verbinden. Ausgangsforderung, Stundungsumfang, laufende Miete, Zahlungszuordnung und Folgen eines Ratenbruchs werden getrennt geregelt; eine bloße Überschrift wie Verfall oder Anerkenntnis ersetzt keine ausformulierte Regelung. Tatsächliche Annahmen und Rechtsfolgen werden nach `references/schriftsatz-und-argumentationsstandard.md` geprüft.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen.

## Ausgabeformat

Getrennte interne Freigabekarte, Vereinbarung als PDF zur Gegenzeichnung, DMS-Ablage, Mahnstopp, Wiedervorlage und Verzugsauslöser für Skill `50-vollstreckungsakte-monitoring`. Die Vereinbarung wird in vollständigen, ausformulierten Sätzen geliefert; leere Klauselrümpfe sind als Endprodukt unzulässig (Ausformulierungspflicht).

## Beispiele

- Rückstand von 3.600 EUR, zwölf Raten je 300 EUR: Vereinbarung mit Verfallklausel und Mahnstopp, Wiedervorlage zu jeder Ratenfälligkeit.
- Mieter mit wiederholtem Ratenbruch in der Vergangenheit: Empfehlung zur Kündigung statt erneuter Stundung, Aktenvermerk an die Abteilungsleitung.
