---
name: 03-kontoauszug-mietkonto-auslesen
description: "Mietkonto, OP-Liste, Buchungsjournal oder neuen Zahlungseingang auslesen und fortschreiben. Saldo, Teilzahlung, Storno, Guthaben, Tilgungsbestimmung und Paragraf 366 BGB prüfen. Bei laufender Akte Alt-Neu-Delta ausgeben, bei Betriebskosten zu Skill 44. Output Forderungstabelle."
---

# Kontoauszug Mietkonto auslesen

## Zweck und Anwendungsfall

Aus dem SAP-Mietkonto (FBL5N) die monatlichen Sollstellungen und Zahlungen in eine klagefähige Forderungsaufstellung übertragen. Anwendungsfall ist die Bezifferung des Rückstands vor Mahnung, Kündigung oder Zahlungsklage.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- SAP-Mietkonto-Auszug (FBL5N) für den Klagezeitraum.
- Etwaige Tilgungsbestimmungen des Mieters zu Teilzahlungen.
- Soll-Werte aus der SAP-Akte (Skill 01) zur Abgleichung.
- Bei laufender Akte: letzte geprüfte Forderungstabelle, Akten-ID, Stichtag und neue Buchungen oder Zahlungsbelege.

## Ablauf / Checkliste

1. Forderungsaufstellung Monat für Monat aufbauen:

| Monat | Soll EUR | Ist EUR | Saldo EUR | Verzugsbeginn | Quelle | Sicherheit |
|---|---|---|---|---|---|---|

2. Verrechnung nach Paragraf 366 BGB vornehmen. Eine bei Leistung getroffene Tilgungsbestimmung des Mieters nach Paragraf 366 Abs. 1 BGB geht vor. Ohne Bestimmung gilt nach Abs. 2 vollständig: zuerst die fällige, unter mehreren fälligen die weniger gesicherte, dann die für den Schuldner lästigere, dann die ältere Schuld; erst bei gleichem Rang anteilig. Innerhalb einer Schuld ordnet Paragraf 367 Abs. 1 BGB grundsätzlich Kosten, Zinsen und Hauptleistung. Abweichende Vertrags-, Titel- oder Insolvenzlage gesondert prüfen.
3. Verzugsbeginn nicht allein aus dem SAP-Kontoeingang ableiten. Bei Wohnraummiete zählt Sonnabend für die Zahlungsfrist nicht; bei gedecktem Konto genügt der bis zum dritten Werktag erteilte Überweisungsauftrag. Nur wenn die rechtzeitige Leistungshandlung fehlt, den Verzug nach Paragraf 286 Abs. 2 Nr. 1 BGB ab dem Folgetag berechnen. BGH VIII ZR 129/09, VIII ZR 291/09 und VIII ZR 222/15 prüfen; Zinssatz gegenüber Verbrauchern nach Paragraf 288 Abs. 1 BGB.
4. Plausibilität sichern: Buchungsdatum und Wertstellung trennen.
5. Teilzahlungen mit Tilgungsbestimmung gesondert markieren.
6. Guthaben, Umbuchungen, Storno und Verrechnung nicht in die offene Forderung einrechnen, bevor die Buchungslogik geklärt ist.
7. Bei neuer Zahlung in einer laufenden Akte nur die betroffenen Zeilen fortschreiben: Alt-Saldo, Zahlung, Tilgungsbestimmung, Verrechnung, Neu-Saldo und Quelle offen zeigen.
8. Prüfen, welche frühere Bewertung durch die Zahlung überholt ist: Mahnbetrag, Kündigungsschwelle, Klageantrag, Erledigungsumfang, KFA oder Vollstreckungsrest. Den betroffenen Folgeskill benennen.

## Zahlungsbeleg ist nicht gleich zusätzlicher Zahlung

Ein Avis, der Bankauszug und die SAP-Zeile können dieselbe Zahlung belegen. Vergleiche Betrag, Buchungs-/Wertstellungstag, Referenz, Vertrag und Gegenkonto; summiere wirtschaftliche Zahlungsvorgänge, nicht Dateien. Ein zweiter Export desselben Belegs erzeugt keine zweite Gutschrift. Geplanter oder freigegebener Zahlungsauftrag bleibt bis zur Ausführung vom Geldeingang getrennt.

Bei Zahlung auf einem Klärungskonto liefere Zuordnung und Nachweisbedarf, ohne Buchungen selbst zu ändern. Eine spätere Erklärung des Mieters wird nicht ungeprüft zur Tilgungsbestimmung bei Leistung. Zeige bei Streit zwei ausdrücklich bedingte Rechenstände; versandfähige Forderung erst nach Klärung. Das erste Ergebnis lautet konkret: Stand vor Zahlung, einmal angerechneter Betrag, betroffene Monate, Rest und Folge für den vorhandenen Entwurf.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen.

## Ausgabeformat

Forderungsaufstellung mit Zahlungsauftrag, Kontoeingang, Verzugsbeginn pro Monatsmiete, Gesamtsaldo, Quellenstatus und Lückenliste. Bei Fortschreibung zusätzlich Änderungskarte mit Alt-Saldo, Zahlung, Neu-Saldo, überholter Bewertung und Folgeskill. Die Aufstellung bleibt tabellarisch; begleitende Bewertungen und Vermerke werden in vollständigen Sätzen ausformuliert (Ausformulierungspflicht).

## Beispiele

- Eine Teilzahlung von 200 EUR ohne Tilgungsbestimmung wird bei gleicher Fälligkeit, Sicherheit und Lästigkeit auf die älteste Monatsforderung verrechnet; innerhalb dieser Schuld sind Kosten und Zinsen zu prüfen.
- Eine Storno-Buchung im Mietkonto wird zunächst nicht saldowirksam berücksichtigt und als zu klärende Lücke ausgewiesen.
