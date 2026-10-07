---
name: 18-widerspruch-vollstreckungsbescheid
description: "Mahnbescheid-Widerspruch oder Einspruch gegen Vollstreckungsbescheid auswerten. Abgabe an Streitgericht, Anspruchsbegründung, Fristsetzung, Einwendungen, Anlagenplan und Rücksprung zur Zahlungsklage vorbereiten. Output Anspruchsbegründung."
---

# Widerspruch und Einspruch nach Mahnverfahren

## Zweck und Anwendungsfall

Reagiert der Mieter gegen Mahnbescheid oder Vollstreckungsbescheid, wird nicht weiter im Formularmodus gearbeitet, sondern die Akte in den normalen Klageworkflow überführt. Anwendungsfall ist jeder Widerspruch oder Einspruch.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Mahnbescheid, Zustellnachweis, Widerspruch oder Einspruch.
- Mietkonto, Mietvertrag, Belegmatrix und bisherige Korrespondenz.
- Gerichtliche Fristsetzung zur Anspruchsbegründung.

## Ablauf / Checkliste

1. Rechtsbehelf bestimmen. Gegen den Mahnbescheid ist Widerspruch nach Paragraf 694 Abs. 1 ZPO möglich, solange der Vollstreckungsbescheid noch nicht verfügt ist; die im Mahnbescheid bezeichneten zwei Wochen sind deshalb keine Ausschluss- oder Notfrist. Ein später Widerspruch wird nach Paragraf 694 Abs. 2 ZPO als Einspruch behandelt.
2. Beim Vollstreckungsbescheid die Einspruchsfrist nach Paragraf 700 Abs. 1 in Verbindung mit Paragraf 339 Abs. 1 ZPO notieren: zwei Wochen ab Zustellung, Notfrist. Nach Einspruch gibt das Mahngericht den Rechtsstreit nach Paragraf 700 Abs. 3 ZPO von Amts wegen ab.
3. Beim Widerspruch gegen den Mahnbescheid nicht dieselbe Automatik annehmen: Nach Paragraf 696 Abs. 1 ZPO wird das streitige Verfahren erst durchgeführt, wenn eine Partei es beantragt; der Antrag kann bereits im Mahnantrag enthalten sein. Abgabeantrag, Gerichtskostenanforderung und das im Mahnbescheid bezeichnete Streitgericht kontrollieren.
4. Rechtshängigkeit nach Paragraf 696 Abs. 3 ZPO gesondert dokumentieren: Sie wirkt auf die Zustellung des Mahnbescheids zurück, wenn die Sache alsbald nach Widerspruch abgegeben wird. Verzögerungen, Zahlungen und Anspruchsänderungen bis zum Akteneingang beim Streitgericht offen ausweisen.
5. Zustellung, Eingangsdatum, Umfang und Rechtzeitigkeit des Rechtsbehelfs dokumentieren und das Streitgericht nach Paragraf 29a ZPO einschließlich der Ausnahmen in Absatz 2 prüfen.
6. Nach Akteneingang beim Streitgericht die gerichtliche Aufforderung nach Paragraf 697 Abs. 1 ZPO überwachen: Anspruchsbegründung in klageschriftentsprechender Form binnen zwei Wochen; Fristende, Vorfrist und Eingangsnachweis erfassen.
7. Einwendungen des Mieters erfassen und in den Beweis- und Anlagenplan übernehmen.
8. Anspruchsbegründung aus Skill `20-zahlungsklage-mietrueckstand-erstellen` ableiten. Bleibt sie hinter dem Mahnantrag zurück, die Rücknahmefolge nach Paragraf 697 Abs. 2 ZPO und den gerichtlichen Hinweis prüfen.
9. Bei komplexen Einwendungen zu Skill `37-klageerwiderung-auswerten` oder `38-replik-erstellen` wechseln.
10. Bei interner 10.000-EUR-Grenze oder Landgerichtssignalen Skill `08-eskalation-an-anwalt` prüfen.
11. Vor Abgabeantrag oder Anspruchsbegründung eine getrennte Freigabekarte erstellen: Rechtsbehelf, Zustellung, Eingangsdatum, Notfriststatus, Abgabeantrag, Rechtshängigkeitsstatus, Abgabegericht, Aktenzeichen, Parteien, Antrag, Forderung, Zinsen, Einwendungen, Anlagen und Vertretungsbefugnis. Status bleibt `ENTWURF - NICHT VERSENDEN/EINREICHEN` bis zur realen Freigabe.

## Argumentationsstandard

Die Anspruchsbegründung wird nicht aus dem Mahnantrag hochgerechnet. Sie bildet für jeden Anspruchsposten den vollständigen Tatsachenkern, die konkrete Einwendung, den Prozessstatus und das Beweisangebot ab. Mahnbescheidsdaten, aktueller Forderungsstand und Klageantrag werden auf Abweichungen kontrolliert; jede Reduzierung, Erweiterung oder Zahlung erhält eine ausdrückliche prozessuale Folge. Maßgeblich ist `references/schriftsatz-und-argumentationsstandard.md`.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst); Normanker sind insbesondere Paragrafen 694, 696, 697 und 700 ZPO, Paragraf 29a ZPO und Paragraf 79 ZPO. Leitentscheidungen werden über `references/leitentscheidungen-anker.md` gesucht und live verifiziert; Rechtsprechung nur verifiziert zitieren.

## Ausgabeformat

Getrennte interne Freigabekarte, vollständig ausformulierte Anspruchsbegründung, Fristenblatt, Einwendungsübersicht und Anlagenliste. Die Anspruchsbegründung wird in vollständigen, ausformulierten Sätzen geliefert (Ausformulierungspflicht).

## Beispiele

- Mieter legt Widerspruch ohne Begründung ein: Umstellung auf die Anspruchsbegründung mit vollständigem Anlagenplan.
- Einspruch mit Aufrechnungseinwand: Wechsel in den Replik-Workflow nach Skill 38.
