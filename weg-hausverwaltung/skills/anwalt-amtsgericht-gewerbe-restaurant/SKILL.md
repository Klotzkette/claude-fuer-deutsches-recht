---
name: anwalt-amtsgericht-gewerbe-restaurant
description: "Anwalt Amtsgericht Gewerbe Restaurant: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anwalt Amtsgericht Gewerbe Restaurant

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Anwalt Amtsgericht Gewerbe Restaurant** im Plugin WEG / Hausverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `eskalation-anwalt-amtsgericht` | Erkennt, wann ein WEG-/Hausverwaltungsvorgang nicht mehr nur Verwaltung ist (Stand 05/2026): Anwalt, Beschlussklage, Hausgeldklage, einstweiliger Rechtsschutz, Beweissicherung, Verwalterhaftung über GdWE oder Vergleich; berücksichtigt Fristen aus § 45 WEG, BGH V ZR 17/24 (Erkundigungsobliegenheit) und V ZR 139/23 (Prozesskostenverteilung). |
| `gewerbe-restaurant-geruch-laerm-hof` | Bearbeitet Restaurant- und Gewerbekonflikte in WEG-Anlagen: Geruch, Lüftung, Lärm, Müll, Lieferverkehr, Fettabscheider, Sondernutzung, Brandschutz und Mieter-/Eigentümerrollen. Output: Eskalations- und Beschlussplan. |
| `grossakte-konfliktlandkarte` | Ordnet unübersichtliche WEG- und Hausverwaltungsakten mit vielen Konflikten: Heizung, Dach, Gewerbe, Geruch, Tauben, Fahrrad, Kinder, Wallbox, Steckersolar, Nebenkosten, Protokolle und Beschlüsse. Output: Konfliktlandkarte, Prioritätenplan und Skill-Routing. |

## Arbeitsweg

Im Plugin WEG / Hausverwaltung gilt für **Anwalt Amtsgericht Gewerbe Restaurant**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `eskalation-anwalt-amtsgericht`

**Fokus:** Erkennt, wann ein WEG-/Hausverwaltungsvorgang nicht mehr nur Verwaltung ist (Stand 05/2026): Anwalt, Beschlussklage, Hausgeldklage, einstweiliger Rechtsschutz, Beweissicherung, Verwalterhaftung über GdWE oder Vergleich; berücksichtigt Fristen aus § 45 WEG, BGH V ZR 17/24 (Erkundigungsobliegenheit) und V ZR 139/23 (Prozesskostenverteilung).

# Eskalation: Anwalt und Amtsgericht

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Eskalation: Anwalt und Amtsgericht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Eskalation: Anwalt und Amtsgericht
- **Spezialgegenstand:** Eskalation: Anwalt und Amtsgericht wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Stand: 05/2026.

## Ziel

Rechtzeitig markieren, wann die Verwaltung nicht weiter allein handeln sollte. Für Eigentümer und Verwalter klare Übergaben an Rechtsanwalt und Gericht ermöglichen.

## Zuständigkeit

- **Amtsgericht** der belegenen Sache, ausschließliche sachliche und örtliche Zuständigkeit für WEG-Streitigkeiten — § 43 Abs. 1 WEG i. V. m. § 23 Nr. 2c GVG.

## Eskalationsgründe

- **Beschlussklage**: drohende oder laufende Klagefrist (1 Monat, § 45 WEG), Klagebegründung (2 Monate, BGH V ZR 33/23 vom 09.02.2024).
- **Erkundigungsobliegenheit**: bei verzögerter Klagezustellung muss der Kläger spätestens binnen 1 Jahr beim Gericht den Sachstand erfragen — BGH, Urteil vom 25.10.2024, V ZR 17/24 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.10.2024&Aktenzeichen=V+ZR+17/24).
- **Nichtigkeitsrisiko**, fehlende Beschlusskompetenz, massive Kostenverschiebung.
- **Hausgeldrückstände**, Sonderumlage, Liquiditätskrise; bei Verweigerung der Vorschusszahlung: kein Zurückbehaltungsrecht des Eigentümers, BGH V ZR 190/24 vom 14.11.2025 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=14.11.2025&Aktenzeichen=V+ZR+190/24).
- **Handwerkermängel**, hoher Schaden, Gewährleistungsfrist drohend (Vermeidung Verjährung).
- **Verwalterabberufung**, Haftung, Interessenkonflikt.
- **Datenschutzvorfall** (Meldepflicht 72h, Art. 33 DSGVO) oder strafrechtlicher Vorwurf.
- **Bauliche Veränderungen** ohne Beschluss durch Eigentümer oder Mieter (mittelbare Handlungsstörerhaftung vermietender Eigentümer, BGH V ZR 1/24 vom 21.03.2025: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=21.03.2025&Aktenzeichen=V+ZR+1/24).

## Anwaltspaket (Mindestinhalt)

1. **Sachverhalt** (Chronologie, Stichdaten, Beteiligte, Rollen).
2. **Dokumentenliste** mit Quellen und Stand: Beschluss(e), Einladung, Protokoll, Beschlusssammlung, Wirtschaftsplan, Jahresabrechnung, Vermögensbericht, Angebote, Rechnungen, Korrespondenz, Mahnungen, Gutachten, Fotos.
4. **Fristen-Übersicht** (Klagefristen, Begründungsfrist, Mahnfristen, Verjährung, Gewährleistung, Erkundigungsobliegenheit).
5. **Rechtsfragen** mit Vorbewertung: Anfechtung/Nichtigkeit, Beschlusskompetenz, Kostenfolge, Haftung.
6. **Zielszenarien**: Klage, Eilrechtsschutz, Vergleich, Neubeschluss, Aussetzung.
7. **Mandantenseitige Klärungspunkte** (Vollmacht, Beirats-Beschluss zur Anwaltsbeauftragung, Kostenfolge).

## Prozesskostenrisiko transparent machen

- Prozesskosten der unterliegenden GdWE = Verwaltungskosten, alle Eigentümer tragen anteilig — auch der obsiegende Anfechtungskläger: BGH, Urteil vom 19.07.2024, V ZR 139/23 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.07.2024&Aktenzeichen=V+ZR+139/23).
- Im Anwaltspaket Kostenrisiko realistisch beziffern (RVG-Streitwert, Gebühren, Eigenkostenanteil).

## Mustertext Vorlage Anwalt

> Sehr geehrte Frau/Herr Rechtsanwalt,
> wir bitten um anwaltliche Begleitung in folgender Angelegenheit:
> 1. **Gegenstand**: [...]
> 2. **Fristen**: Beschluss am [...]; Anfechtungsfrist [..]; Begründungsfrist [...]; weiteres: [...]
> 3. **Rolle der GdWE**: [Beklagte / Klägerin / Streithelferin]
> 4. **Beigefügt**: Beschluss-Sammlung, Protokoll, Wirtschaftsplan, Jahresabrechnung, Sachverständigengutachten, Korrespondenz (Anlagen 1-...).
> 5. **Mandantenwünsche / offene Fragen**: [...]
> 6. **Vollmacht**: liegt bei (Anlage X), Beschluss der GdWE / Bestellung Beirat unter TOP [...] vom [Datum].
> Wir bitten um Erstbewertung mit Kostenschätzung bis [Datum].

## Output

- Anwaltspaket gemäß Mindestinhalt
- Klage-/Eilrechtsschutz-Risikoübersicht
- Vergleichs- oder Neubeschluss-Option
- Mandantenfreundliche Kurznotiz für Beirat/Eigentümer
- Hinweis auf Prozesskostenanteil (V ZR 139/23) und Hausgeld-Vorschuss-Logik (V ZR 190/24)

## Cross-Refs

- Anfechtungsrisiko / Heilung → `beschlussanfechtung-risiko`
- Hausgeldklage → `hausgeld-sonderumlage-liquiditaet`
- Verwalterhaftung → `verwalterpflichten-26-27-weg`
- Datenschutz → `datenschutz-dokumentenfreigabe`

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. §§ 43, 44, 45 WEG: https://www.gesetze-im-internet.de/woeigg/__43.html, https://www.gesetze-im-internet.de/woeigg/__44.html, https://www.gesetze-im-internet.de/woeigg/__45.html .


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `gewerbe-restaurant-geruch-laerm-hof`

**Fokus:** Bearbeitet Restaurant- und Gewerbekonflikte in WEG-Anlagen: Geruch, Lüftung, Lärm, Müll, Lieferverkehr, Fettabscheider, Sondernutzung, Brandschutz und Mieter-/Eigentümerrollen. Output: Eskalations- und Beschlussplan.

# Gewerbe, Restaurant, Geruch, Lärm und Hofnutzung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gewerbe, Restaurant, Geruch, Lärm und Hofnutzung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Gewerbe, Restaurant, Geruch, Lärm und Hofnutzung
- **Spezialgegenstand:** Gewerbe, Restaurant, Geruch, Lärm und Hofnutzung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieses Fachmodul greift, wenn in der Anlage ein Restaurant, Café, Laden oder sonstiges Gewerbe Konflikte auslöst: Gerüche, Abluft, Fett, Lieferverkehr, Müll, Hofnutzung, Außengastronomie, Brandschutz oder nächtlicher Lärm.

## Prüfraster

1. **Rechtsverhältnis trennen:** Gewerbemieter, Teileigentümer, Sondereigentümer, Gemeinschaft, Verwalter.
2. **Teilungserklärung prüfen:** Nutzungszweck, Sondernutzungsrechte, Öffnungszeiten, bauliche Anlagen.
3. **Störung konkretisieren:** Geruch, Lärm, Müll, Lieferverkehr, Schädlingsrisiko, Brandschutz, Fettabscheider.
4. **Beweise sichern:** Geruchsprotokoll, Fotos, Zeugen, Messung, Ordnungsamt, Schornsteinfeger, Lüftungsfirma.
5. **Verwaltungspfad:** Gespräch, Abmahnung, Beschluss, technische Prüfung, Behördenkontakt, Anwalt.
6. **Mietrechtliche Schnittstelle:** Vermietender Eigentümer muss ggf. auf seinen Gewerbemieter einwirken.

## Maßnahmenstufen

| Stufe | Maßnahme | Zweck |
| --- | --- | --- |
| 1 | Sachverhalt und Belege sammeln | keine Stimmungslage entscheiden |
| 2 | Betreiber/Eigentümer anhören | freiwillige Abhilfe |
| 3 | Fachprüfung Abluft/Fett/Müll | technische Ursache |
| 4 | Beschluss mit Auflagen | Verwaltung handlungsfähig machen |
| 5 | Anwalt/Behörde | Unterlassung oder öffentlich-rechtliche Prüfung |

## Beschlussbaustein

```text
Die Verwaltung wird beauftragt, die durch den Betrieb der Gewerbeeinheit Nr. [...] gemeldeten Geruchs-, Müll- und Lärmbelastungen aufzuklären, den Teileigentümer und den Betreiber anzuhören, eine fachtechnische Prüfung der Abluft- und Entsorgungssituation einzuholen und der Gemeinschaft bis zum [...] einen Maßnahmenvorschlag vorzulegen. Der Kostenrahmen für die Erstprüfung beträgt [...] EUR brutto.
```

## Red Flags

- Beschwerden werden als Nachbarschaftsstreit abgetan, obwohl Gemeinschaftseigentum betroffen ist.
- Gewerbemieter wird direkt in Anspruch genommen, obwohl zunächst der Teileigentümer Ansprechpartner ist.
- Ordnungsrecht, Brandschutz und WEG-Recht werden vermischt.
- Geruchsbeschwerden ohne Protokoll und Belege werden sofort eskaliert.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `grossakte-konfliktlandkarte`

**Fokus:** Ordnet unübersichtliche WEG- und Hausverwaltungsakten mit vielen Konflikten: Heizung, Dach, Gewerbe, Geruch, Tauben, Fahrrad, Kinder, Wallbox, Steckersolar, Nebenkosten, Protokolle und Beschlüsse. Output: Konfliktlandkarte, Prioritätenplan und Skill-Routing.

# Großakte und Konfliktlandkarte

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Großakte und Konfliktlandkarte` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Großakte und Konfliktlandkarte
- **Spezialgegenstand:** Großakte und Konfliktlandkarte wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieses Fachmodul greift, wenn eine WEG-Akte aus vielen kleinen Konflikten besteht und niemand mehr weiß, was dringend, was beschlussreif und was bloß Stimmung ist.

## Vorgehen

1. **Dokumente stapeln:** Einladung, Protokoll, Teilungserklärung, Abrechnung, Angebote, E-Mails, WhatsApp, Fotos, Rechnungen, Versicherungen, Mieterschreiben.
2. **Konflikte trennen:** Technik, Geld, Beschluss, Hausordnung, Mietrecht, Gewerbe, Datenschutz, Versicherung, Anfechtung.
3. **Fristen zuerst:** Beschlussklage § 45 WEG, Einladungsfristen, Abrechnungsfristen, Angebotsbindungen, Gewährleistung, Versicherungsanzeige.
4. **Eigentümer-/Mieterrollen klären:** GdWE, Sondereigentümer, vermietender Eigentümer, Mieter, Gewerbemieter, Verwalter, Beirat.
5. **Beschlussfähigkeit prüfen:** Was braucht Beschluss, was darf Verwaltung laufend erledigen, was ist Notmaßnahme?
6. **Skill-Routing:** Pro Konflikt einen passenden Fachmodul vorschlagen.

## Output

| Cluster | Thema | Eilt? | Zuständigkeit | Nächster Skill | Nächster Schritt |
| --- | --- | --- | --- | --- | --- |
| Technik | [...] | [...] | [...] | [...] | [...] |
| Abrechnung | [...] | [...] | [...] | [...] | [...] |
| Hausordnung | [...] | [...] | [...] | [...] | [...] |
| Beschluss | [...] | [...] | [...] | [...] | [...] |

## Leitlinie

Nicht alles juristisch eskalieren. Erst sortieren, beweisen, beschlussfähig machen und kommunizieren. Anwaltliche Eskalation nur dort markieren, wo Fristen, Beschlussmängel, Zahlungsausfälle, Gewährleistung oder Unterlassung ernsthaft im Raum stehen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
