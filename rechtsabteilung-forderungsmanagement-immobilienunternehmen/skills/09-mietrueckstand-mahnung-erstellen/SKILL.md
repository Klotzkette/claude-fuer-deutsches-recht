---
name: 09-mietrueckstand-mahnung-erstellen
description: "Mahnung wegen Mietrückstand. Erste Mahnung freundlich. Zweite Mahnung mit Klageandrohung. Verzugszinsen Paragraf 288 BGB. Konkrete Forderungsaufstellung Monat für Monat. Output Mahnschreiben als Brief mit Zugangsnachweis-Protokoll."
---

# Mahnschreiben Mietrückstand

## Zweck und Anwendungsfall

Dieser Skill erstellt das Mahnschreiben wegen Mietrückstands in zwei Stufen und sichert den Zugang. Anwendungsfall ist die erste außergerichtliche Eskalation, sobald der Verzug feststeht.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Forderungsaufstellung Monat für Monat aus Skill 03.
- Stammdaten des Mietverhältnisses aus Skill 01.
- Angabe, ob es sich um die erste oder zweite Mahnstufe handelt.

## Ablauf / Checkliste

1. Verzug feststellen: Bei Wohnraummiete zählt Sonnabend für die Zahlungsfrist des Paragrafen 556b BGB nicht. Im Überweisungsverkehr genügt bei gedecktem Konto der bis zum dritten Werktag erteilte Zahlungsauftrag; der spätere Kontoeingang allein macht die Zahlung nicht verspätet. Bei streitiger Pünktlichkeit Zahlungsauftrag, Deckung, Rückgabe und Storno klären. Erst danach Paragraf 286 Abs. 2 Nr. 1 BGB und BGH VIII ZR 129/09, VIII ZR 291/09 sowie VIII ZR 222/15 anwenden.
2. Kündigungsschwelle vor Mahnstufe prüfen. Ist Paragraf 543 Abs. 2 Nr. 3 BGB erreicht, die Mahnung nicht als gesetzliche Voraussetzung oder automatische Wartephase darstellen; Skill `13-fristlose-kuendigung-zahlungsverzug` und interne Freigabeentscheidung eröffnen. Eine freundliche Zahlungsaufforderung darf nur bewusst neben dem Kündigungscheck laufen.
3. Erste Mahnung sachlich-freundlich formulieren mit Forderungsaufstellung, kalendarisch bestimmter Zahlungsfrist und Hinweis auf die Möglichkeit einer Ratenvereinbarung. Die Frist wird nach Zugangslauf, Zahlungsweg, bisheriger Kommunikation und Dringlichkeit festgelegt; es gibt hierfür keine starre gesetzliche 14-Tage-Frist. Aufbau:

```
Mietverhältnis Objekt X Vertrag Y
Zahlungsstörung Mieten Monat A bis B

Sehr geehrte Frau Müller,
wir müssen feststellen, dass folgende Mieten nicht vollständig
gezahlt wurden:

  02 2025  EUR 1180.00 offen
  03 2025  EUR  680.00 offen
  Summe    EUR 1860.00

Wir bitten um Zahlung bis zum [Datum]. Bei Zahlungsschwierigkeiten
melden Sie sich bitte für eine Ratenvereinbarung.
```

4. Zweite Mahnung ausformuliert mit folgenden Pflichtbestandteilen: ausdrücklicher Hinweis auf den eingetretenen Verzug; bezifferte Verzugszinsen; angemessene kalendarische Letztfrist mit dokumentiertem Rechenweg; ausdrückliche Klageandrohung; Hinweis nur auf mögliche gesetzliche Verzugszinsen, Gerichts- und Vollstreckungskosten. Interne Bearbeitungskosten oder angebliche Kosten einer Kündigung werden nicht angedroht.
5. Zustellung sichern: Regelweg ist der Bote mit Einwurfvermerk, Datum, Uhrzeit und Foto; das Einwurf-Einschreiben dient nur ergänzend. Das Übergabe-Einschreiben nicht als alleinigen Nachweis verwenden, wenn Annahmeverweigerung oder Nichtabholung droht.
6. Vor Ausgabe eine getrennte Freigabekarte erstellen: Datenstichtag, Mieter und Objekt, Monatsbeträge, letzter Zahlungseingang, berechneter Verzug, Fristdatum, Zustellweg und Freigabeperson. Status bleibt `ENTWURF - NICHT VERSENDEN/EINREICHEN`, bis eine reale Freigabeperson entscheidet.

## Argumentationsstandard

Das Schreiben nennt nicht nur einen Gesamtsaldo. Es verbindet für jeden offenen Monat Soll, Fälligkeit, gebuchte Zahlung, Tilgungszuordnung, offenen Rest und Verzugsfolge. Eine bestrittene Zahlung wird als Klärungspunkt mit dem konkret fehlenden Bank- oder Buchungsbeleg bezeichnet; sie darf nicht durch die pauschale Formulierung ersetzt werden, laut System sei nichts eingegangen. Maßgeblich ist `references/schriftsatz-und-argumentationsstandard.md`.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen.

## Ausgabeformat

Getrennte interne Freigabekarte, Mahnschreiben als Word oder PDF, Forderungstabelle, Zahlungsfrist, Zustellprotokoll und DMS-Ablagehinweis. Das Mahnschreiben wird in vollständigen, ausformulierten Sätzen geliefert; Stichwort-Skelette und reine Aufzählungen sind als Endprodukt unzulässig (Ausformulierungspflicht).

## Beispiele

- Rückstand unterhalb der Kündigungsschwelle und erkennbare Zahlungsschwierigkeit: freundliche erste Mahnung mit Ratenangebot und anhand von Zugang und Zahlungsweg berechneter Frist.
- Qualifizierter Rückstand nach Paragraf 543 Abs. 2 Nr. 3 BGB: Mahnung nicht als Pflichtwartezeit behandeln; Kündigungscheck nach Skill 13 parallel eröffnen.
- Trotz erster Mahnung keine Zahlung: zweite Mahnung mit bezifferten Verzugszinsen, letzter Frist und ausdrücklicher Klageandrohung.
