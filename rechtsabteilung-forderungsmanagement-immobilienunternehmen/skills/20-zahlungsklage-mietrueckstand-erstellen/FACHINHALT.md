---
name: 20-zahlungsklage-mietrueckstand-erstellen
description: "Reine Zahlungsklage wegen Mietrückstand ohne Räumungsantrag erstellen. Mietkonto, Belegmatrix, Rubrum, Zahlungsantrag, Zinsen, Aufrechnung und Kostenpfad verarbeiten. Bei Räumung, Herausgabe, Kündigung oder Kombiklage führt Skill 24. Output Klage."
---

# Zahlungsklage Mietrückstand

## Zweck und Anwendungsfall

Dieser Skill erstellt die vollständige reine Zahlungsklage wegen Mietrückstands für das Amtsgericht. Anwendungsfall ist der titulierungsreife Rückstand nach erfolgloser außergerichtlicher Eskalation ohne Räumungsantrag. Bei Räumung, Herausgabe, Kündigung oder Kombiklage führt Skill `24-raeumungsklage-erstellen`; dieser Skill liefert dann nur Zahlungsantrag und Forderungsbaustein.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Forderungsaufstellung (Skill 03), Belegmatrix (Skill 04) und Chronologie (Skill 05).
- Stammdaten der Konzerngesellschaft und des Mieters.
- Streitwert- und Vorschussdaten aus Skill 21.
- Gewünschter Verfahrensweg und, falls das Online-Verfahren erwogen wird, aktuelle Dienstabdeckung für Gericht, Anspruch und Vertretungsrolle.

## Ablauf / Checkliste

1. Klageschrift nach folgendem Aufbau erstellen: Rubrum mit Klägerin (Konzerngesellschaft mit Anschrift und Vertretungsorgan) und Beklagtem (Mieter), Streitgegenstand, Streitwert und Gericht (Amtsgericht am Lageort, Paragraf 29a ZPO); bezifferte Zahlungsanträge nebst Zinsen ab Verzug; chronologischer Sachverhalt aus Skill 05; rechtliche Würdigung (Paragraf 535 Abs. 2 BGB Mietzahlung, Paragraf 286 BGB Verzug, Paragraf 288 BGB Zinsen); Beweisangebote mit Anlagen; Anlagen K1 bis Kn.
2. Rubrum und Antrag nach folgendem Muster ausformulieren:

```
Klage

der Wohnen Berlin Immobilien GmbH
vertreten durch den Geschäftsführer Dr. Markus Lehmann
Friedrichstraße 99 10117 Berlin
Klägerin
vertreten durch die Rechtsfachwirtin Frau Sandra Berger
prozessbevollmächtigt nach Paragraf 79 Abs. 2 ZPO

gegen

Herrn Thomas Meier
Wilhelmstraße 14 10963 Berlin
Beklagter

wegen Mietrückstand Wohnraum
Streitwert EUR 2360 (vorläufig)

Antrag:
Der Beklagte wird verurteilt, an die Klägerin EUR 2360
nebst Zinsen in Höhe von 5 Prozentpunkten über Basiszinssatz
aus EUR 1180 seit dem 04.02.2025 und
aus EUR 1180 seit dem 04.03.2025
zu zahlen.
```

3. Lead-Abgrenzung prüfen: Bei Räumung, Herausgabe, Kündigung, Schonfristzahlung oder kombinierter Zahlungs- und Räumungsklage sofort Skill 24 als Lead setzen; Skill 20 liefert nur Zahlungsantrag, Forderungsaufstellung, Zinsstaffel und Anlagenbaustein.
4. Betriebskosten abgrenzen: Bei Betriebskostenabrechnung, Nebenkostennachforderung, Vorauszahlungsanpassung, Belegeinsicht oder Wirtschaftlichkeitseinwand zuerst Skill `44-betriebskosten-rueckstand-streit` laden; erst nach dessen Matrix eine Zahlungsklage bilden.
5. Mahnverfahren abgrenzen: Bei ausdrücklichem Mahnbescheid-, Mahnverfahren-, Vollstreckungsbescheid- oder VB-Wording zuerst Skill `17-mahnbescheid-online-antrag`; nach Widerspruch oder Einspruch Skill 18.
6. Online-Verfahren nur als echte Alternative prüfen: reine Geldzahlungsklage bis 10.000 EUR, nach allgemeinen Regeln zuständiges teilnehmendes Amtsgericht, vom aktuellen amtlichen Eingabedienst abgedeckter Anspruch und unterstützte tatsächliche Vertretungsrolle. In Berlin nimmt seit 15.04.2026 das Amtsgericht Schöneberg nur für seinen Gerichtsbezirk teil. Räumung, Herausgabe oder sonstige Nichtgeldanträge sperren den Sonderweg. Der am 09.08.2026 veröffentlichte Dienst bildet die Eigenvertretung einer privaten GmbH durch Beschäftigte nicht automatisch ab; dann reguläre Klage nach Paragraf 253 ZPO vorbereiten. Paragrafen 1122 bis 1125 ZPO und `references/rechtsstand-2026-verfahren-vollstreckung.md` live prüfen.
7. Streitwert bestimmen: Bei reiner Zahlungsklage ist die bezifferte Hauptforderung Ausgangspunkt; Gerichtskosten und Spezialwerte werden in Skill `21-klage-streitwert-gerichtskosten` geprüft. Bei Kombiklage mit Räumung kommt der Räumungswert nach Paragraf 41 Abs. 2 GKG gesondert hinzu.
8. Freigabecheck durchführen: offene Beleglücken, Fristen, interne 10.000-EUR-Grenze, gewählter regulärer oder Online-Verfahrensweg und Eskalationsgründe.
9. Nach Einreichung Wiedervorlage für erledigende Ereignisse setzen: Zahlung, Aufrechnung, dauernde Einrede, Unmöglichkeit oder Wegfall des Rechtsschutzbedürfnisses. Dann Skill `11-verzugsschaden-berechnen`, `37-klageerwiderung-auswerten` und bei Unsicherheit Skill `08-eskalation-an-anwalt` anstoßen.
10. Kostenpfad nicht reflexhaft festlegen: Vor Erledigungserklärung oder Rücknahme Vorverzug, Forderungsstatus bei Einreichung sowie Erforderlichkeit und Kausalität der Klagekosten prüfen. Grün ist die bei Einreichung noch offene Forderung. Eine unmittelbar zuvor eingegangene, objektiv noch nicht erkennbare Zahlung bleibt gelb und verlangt RA-Freigabe. BGH III ZR 156/12 ist der geprüfte Basisanker; die konkrete Gestaltung erfordert einen live geöffneten Volltext.
11. Bei bestrittenem Verzugsbeginn nicht allein den SAP-Kontoeingang vortragen. Für Wohnraummiete Sonnabend aus der Zahlungsfrist herausrechnen und bei Überweisung Zahlungsauftrag, Kontodeckung, Rückgabe und Storno würdigen; BGH VIII ZR 129/09, VIII ZR 291/09 und VIII ZR 222/15 prüfen.
12. Getrennte Freigabekarte erstellen: Gericht, Parteien, Vertretung, Antrag, Forderungsstichtag, Hauptsumme, Zinsstaffel, Zahlungen, Tatsachen-Beweis-Zuordnung, Anlagen K1 bis Kn, Vorschuss, regulärer oder Online-Verfahrensweg und Freigabeperson. Status bis zur dokumentierten Freigabe `ENTWURF - NICHT VERSENDEN/EINREICHEN`.

## Argumentationsstandard

Vor dem Fließtext entsteht eine Tatbestandsmatrix für Vertrag, Miethöhe, Fälligkeit, Zahlung, Tilgung, offenen Rest, Verzug und Zins. In der Klage erhält jede streitige erhebliche Tatsache einen eigenen kurzen Tatsachensatz und unmittelbar danach ihr Beweisangebot; Mietkonto, SAP-Saldo und rechtliche Wertung werden nicht vermischt. Einwendungen zu Zahlung, Minderung, Aufrechnung oder Verjährung werden mit Zugeständnis, konkretem Bestreiten, Gegenbeleg und Rechtsfolge beantwortet. Der vollständige Maßstab steht in `references/schriftsatz-und-argumentationsstandard.md`.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen. Für das Online-Verfahren ist zusätzlich `references/rechtsstand-2026-verfahren-vollstreckung.md` einschließlich Rollen- und Dienstgate anzuwenden.

## Ausgabeformat

Getrennte interne Freigabekarte, Klageschrift als Word oder PDF, Anlagen-Konvolut, Gerichtskostenvorschuss-Daten, Beleglückenstatus und Einreichungscheck. Die Klageschrift wird in vollständigen, ausformulierten Sätzen im Urteilsstil geliefert; Stichwort-Skelette sind als Endprodukt unzulässig (Ausformulierungspflicht).

## Beispiele

- Rückstand aus zwei Monatsmieten je 1180 EUR: Zahlungsklage über 2360 EUR nebst gestaffelten Verzugszinsen.
- Kombiklage Zahlung und Räumung: Skill 24 führt; dieser Skill liefert nur den Zahlungsbaustein.
- Zahlung kurz nach Einreichung: Kostenpfad-Matrix statt automatischer Rücknahme.
- Reine Zahlungsklage über 4.800 EUR im Bezirk des Amtsgerichts Schöneberg: Online-Verfahren nur dann wählen, wenn der amtliche Dienst die wirkliche Kläger- und Vertretungsrolle unterstützt; andernfalls reguläre Klage.
