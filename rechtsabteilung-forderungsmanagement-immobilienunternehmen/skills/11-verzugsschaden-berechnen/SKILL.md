---
name: 11-verzugsschaden-berechnen
description: "Verzugsschaden nach Paragraf 280 und 286 BGB. Zinsen, Inkasso- und Anwaltskosten, Bonitätsauskunft und Prozesskosten nach erledigendem Ereignis prüfen. Mahnpauschale nicht bei Verbrauchern. Output Schadenstabelle."
---

# Verzugsschaden berechnen

## Zweck und Anwendungsfall

Dieser Skill beziffert den Verzugsschaden und trennt Hauptforderung, Zinsen, Nebenforderungen und ersatzfähige Rechtsverfolgungskosten. Anwendungsfälle sind Mahnung, letzte Frist, Zahlungsklage und die Kostenprüfung nach einem erledigenden Ereignis im laufenden Prozess.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Forderungsaufstellung mit Saldo und Verzugsbeginn pro Monatsmiete aus Skill 03.
- Aktueller Basiszinssatz der Bundesbank.
- Belege etwaiger externer Rechtsverfolgungskosten.
- Prozessstand, Rechtshängigkeit, Zahlungen, Aufrechnung oder andere erledigende Ereignisse nach Klageeinreichung.

## Ablauf / Checkliste

1. Anspruchsgrundlagen zuordnen:

| Schaden | Norm |
|---|---|
| Verzugszinsen Verbraucher | Paragraf 288 Abs. 1 BGB |
| Verzugszinsen Unternehmer | Paragraf 288 Abs. 2 BGB |
| Mahnpauschale 40 EUR Unternehmer | Paragraf 288 Abs. 5 BGB |
| Externe RA-Kosten außergerichtlich | Paragraf 280 Abs. 1 und 2, Paragraf 286 BGB |
| Gerichtliche Rechtsverfolgungskosten nach erledigendem Ereignis | Paragraf 280 Abs. 1 und 2, Paragraf 286 BGB; prozessual Paragraf 263, 264 und 269 ZPO |
| Inkassokosten | Paragraf 280 Abs. 1 und 2, Paragraf 286 BGB; Höchstgrenze nach Paragraf 13e RDG |
| Vorprozessuale Bonitätsauskunft | grundsätzlich nicht ersatzfähig; Ausnahme nach Paragraf 280 Abs. 1 und 2, Paragraf 286 BGB konkret darlegen |

2. Zinsen pro Monatsmiete berechnen:

| Monat | Saldo | Verzugsbeginn | Zinssatz | Zinsen bis heute |
|---|---|---|---|---|

3. Basiszinssatz nach Paragraf 247 BGB ansetzen (halbjährlich von der Bundesbank festgelegt).
4. Grenzen beachten: Die Mahnpauschale von 40 EUR nach Paragraf 288 Abs. 5 BGB greift NICHT bei Verbrauchern. Die rein interne Bearbeitung durch die Renofa erzeugt keine erstattungsfähigen Anwaltskosten. Externe Rechtsverfolgungskosten nur ansetzen, wenn sie nach Eintritt des Verzugs erforderlich und belegt sind. Inkassokosten dürfen nach Paragraf 13e Abs. 1 RDG höchstens bis zur entsprechenden RVG-Vergütung als Schaden verlangt werden.
5. Bonitätsauskunft gesondert aussondern: Nach BGH VII ZR 93/25 sind Kosten einer vor Einleitung des gerichtlichen Erkenntnisverfahrens eingeholten Bonitätsauskunft grundsätzlich kein Verzugsschaden. Nicht mit Inkassogrundvergütung oder Auslagenpauschale vermischen. Nur bei dokumentierten besonderen Umständen aufnehmen: Zweck und Zeitpunkt der Auskunft, damals unbekannte und für die Anspruchsdurchsetzung benötigte Daten, mildere verfügbare Informationsquelle, konkrete Erforderlichkeit, Rechnung sowie Tatsachen für Darlegung und Beweis. Eine bloße Prüfung, ob sich Klage oder spätere Vollstreckung wirtschaftlich lohnt, reicht regelmäßig nicht.
6. Nach Klageeinreichung sofort Kostenpfad prüfen, wenn der Mieter zahlt, aufrechnet, eine dauernde Einrede erhebt, Leistung unmöglich wird oder das Rechtsschutzbedürfnis wegfällt. Nicht automatisch Erledigung oder Rücknahme empfehlen.
7. Matrix ausgeben: Ereignis, Datum, vor/nach Rechtshängigkeit, vollständig/teilweise, Vorverzug, Forderungsstatus bei Einreichung, Wertstellung/Buchung, damaliger Kenntnisstand, Kausalität und Erforderlichkeit der Kosten, offener Betrag, Kostenweg und Eskalation.
8. Materiell-rechtliche Kostenerstattungsklage nur bei Vorverzug und aus damaliger Sicht erforderlichen, kausalen Klagekosten prüfen; einen unbezifferten Feststellungsantrag nicht ohne gesonderte Zulässigkeitsprüfung wählen. Kosten vor Verzug oder nach vermeidbarer Fortführung ausscheiden. BGH III ZR 156/12 nennt als einfachen Fall den bereits in Verzug befindlichen Beklagten, der zwischen Einreichung und Zustellung zahlt. Grün ist deshalb die bei Einreichung noch offene Forderung. Ging die Zahlung unmittelbar zuvor ein, war aber objektiv noch nicht erkennbar, gelbe Ampel setzen und Zahlungsweg, Buchungszeitpunkt sowie Kenntnisstand mit dem amtlichen Volltext zur RA-Freigabe geben.
9. Bei Wohnraummiete den Verzugsbeginn aus Skill 03 kontrollieren: Sonnabend zählt für die Zahlungsfrist nicht; ein gedeckter Überweisungsauftrag bis zum dritten Werktag kann trotz späterem Geldeingang rechtzeitig sein. Ohne geklärten Zahlungsauftrag keine Zinsen oder Rechtsverfolgungskosten allein aus dem SAP-Buchungstag ableiten; BGH VIII ZR 222/15 prüfen.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen. Für Bonitätsauskünfte BGH VII ZR 93/25 aus `references/gepruefte-bgh-anker-mietrecht.md` heranziehen; VII ZR 96/25 ist die Parallelentscheidung.

## Ausgabeformat

Forderungsaufstellung mit getrennter Ausweisung von Hauptforderung, Zinsen, Nebenforderungen und prozessualem Kostenpfad. Die Aufstellung bleibt tabellarisch; begleitende Bewertungen und Vermerke werden in vollständigen Sätzen ausformuliert (Ausformulierungspflicht). Ampel: grün bei Vorverzug, offener Forderung bei Einreichung und klarer Kausalität; gelb bei Erkennbarkeits- oder Beleglücken; rot bei fehlendem Vorverzug oder vermeidbaren Kosten.

## Beispiele

- Wohnraummieter als Verbraucher: Verzugszinsen mit fünf Prozentpunkten über Basiszins, keine 40-EUR-Pauschale.
- Externe Anwaltskosten erst nach Verzugseintritt und mit Kostenbeleg: nur dann als Nebenforderung ausgewiesen, sonst weggelassen.
- Routinemäßige Bonitätsauskunft vor Klage: Kosten aus der Schadenstabelle entfernen und nur bei konkret belegtem Ausnahmebedarf erneut prüfen.
- Mieter zahlt nach Klageeinreichung vor Zustellung: Vorverzug, Einreichungs- und Zahlungszeitpunkt, Erforderlichkeit sowie Kausalität prüfen; erst dann materiell-rechtliche Kostenerstattung erwägen.
