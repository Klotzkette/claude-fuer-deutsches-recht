---
name: legw-aa-konsular-bmas-arbeitsrecht
description: "Legw AA Konsular Bmas Arbeitsrecht: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Legw AA Konsular Bmas Arbeitsrecht

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Legw AA Konsular Bmas Arbeitsrecht** im Plugin Legistik Werkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `legw-aa-konsular-und-passrecht` | Sachbereich Konsularrecht und Passrecht im Geschaeftsbereich AA: Normbestand (KonsG; PassG; PAuswG; EWG-VO 1683/95 (Visa).); Akteure (Auslandsvertretungen; Bundesverwaltungsamt; BAMF (Visa).); EU-Bezug (Visa-Kodex; Schengen; ETIAS.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-aa (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-aa (Heranfuehrung). |
| `legw-bmas-arbeitsrecht-und-arbeitsschutz` | Sachbereich Arbeitsrecht und Arbeitsschutz im Geschaeftsbereich BMAS: Normbestand (BGB-Arbeitsrecht; KSchG; TzBfG; ArbZG; ArbSchG; BetrVG; SprAuG; MiLoG.); Akteure (BMAS; BAuA; ArbGericht; LAG; BAG; Arbeitsschutzbehoerden der Laender.); EU-Bezug (Arbeitsschutz-RL; Arbeitszeit-RL; Plattformarbeit-RL; ArbeitnehmerInfo-RL.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmas (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmas (Heranfuehrung). |
| `legw-bmas-arbeitsschutz-und-arbeitssicherheit` | Sachbereich Arbeitsschutz und Arbeitssicherheit im Geschaeftsbereich BMAS: Normbestand (ArbSchG; ArbStaettV; BetrSichV; BiostoffV; LasthandhabV; PSA-BV; ArbMedVV.); Akteure (BAuA; UVT (Berufsgenossenschaften); Laender-Arbeitsschutzbehoerden; KomNet.); EU-Bezug (Arbeitsschutz-Rahmenrichtlinie 89/391/EWG; Tochterrichtlinien.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmas (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmas (Heranfuehrung). |
| `legw-bmas-sozialversicherungsrecht-sgb` | Sachbereich Sozialversicherungsrecht (SGB) im Geschaeftsbereich BMAS: Normbestand (SGB I bis SGB XII; ASVG-Aequivalent; AsylbLG (mit BMI).); Akteure (DRV Bund; BA; GKV-Spitzenverband; BAS (Bundesamt fuer Soziale Sicherung); SGericht.); EU-Bezug (VO 883/2004 (Koordinierung); EFTA; bilaterale Abkommen.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmas (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmas (Heranfuehrung). |

## Arbeitsweg

Im Plugin Legistik-Werkstatt gilt für **Legw AA Konsular Bmas Arbeitsrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `legw-aa-konsular-und-passrecht`

**Fokus:** Sachbereich Konsularrecht und Passrecht im Geschaeftsbereich AA: Normbestand (KonsG; PassG; PAuswG; EWG-VO 1683/95 (Visa).); Akteure (Auslandsvertretungen; Bundesverwaltungsamt; BAMF (Visa).); EU-Bezug (Visa-Kodex; Schengen; ETIAS.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-aa (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-aa (Heranfuehrung).


# Konsularrecht und Passrecht (AA)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Konsularrecht und Passrecht im Geschaeftsbereich AA. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-aa`
- Aufgabenmatrix aus `legw-ressortaufgaben-aa`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: KonsG; PassG; PAuswG; EWG-VO 1683/95 (Visa).

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

Auslandsvertretungen; Bundesverwaltungsamt; BAMF (Visa).

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

Visa-Kodex; Schengen; ETIAS.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Konsularische Aufgaben praezisieren; Pass- und Ausweisbestimmungen; Notfallhilfe; Beurkundungen; Personenstandssachen im Ausland.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Doppelstaatsangehoerigkeit; Datenschutz konsularischer Datenbanken; Schengen-Visumzwang.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld: Konsularrecht und Passrecht
Ressort: AA
Kernnormen: KonsG; PassG; PAuswG; EWG-VO 1683/95 (Visa).
Akteure/Aufsicht: Auslandsvertretungen; Bundesverwaltungsamt; BAMF (Visa).
EU/Voelkerrecht: Visa-Kodex; Schengen; ETIAS.
Pruefpunkte: <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine: <Sachfeld-spezifisch>
Naechste Skills: legw-ressortaufgaben-aa; normhierarchie-routing;
 normenkartierung; verfassungsmaessigkeit-quercheck;
 europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-aa` -> `legw-ressortaufgaben-aa` -> `legw-aa-konsular-und-passrecht` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 2. `legw-bmas-arbeitsrecht-und-arbeitsschutz`

**Fokus:** Sachbereich Arbeitsrecht und Arbeitsschutz im Geschaeftsbereich BMAS: Normbestand (BGB-Arbeitsrecht; KSchG; TzBfG; ArbZG; ArbSchG; BetrVG; SprAuG; MiLoG.); Akteure (BMAS; BAuA; ArbGericht; LAG; BAG; Arbeitsschutzbehoerden der Laender.); EU-Bezug (Arbeitsschutz-RL; Arbeitszeit-RL; Plattformarbeit-RL; ArbeitnehmerInfo-RL.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmas (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmas (Heranfuehrung).


# Arbeitsrecht und Arbeitsschutz (BMAS)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Arbeitsrecht und Arbeitsschutz im Geschaeftsbereich BMAS. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmas`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmas`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: BGB-Arbeitsrecht; KSchG; TzBfG; ArbZG; ArbSchG; BetrVG; SprAuG; MiLoG.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

BMAS; BAuA; ArbGericht; LAG; BAG; Arbeitsschutzbehoerden der Laender.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

Arbeitsschutz-RL; Arbeitszeit-RL; Plattformarbeit-RL; ArbeitnehmerInfo-RL.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Tatbestaende des Arbeitsrechts; Kuendigungsschutz; Befristungsrecht; Arbeitszeit; Mindestlohn; Mitbestimmung.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Tarifautonomie; Befristungsketten; Plattformarbeit; EU-Mindeststandards.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld: Arbeitsrecht und Arbeitsschutz
Ressort: BMAS
Kernnormen: BGB-Arbeitsrecht; KSchG; TzBfG; ArbZG; ArbSchG; BetrVG; SprAuG; MiLoG.
Akteure/Aufsicht: BMAS; BAuA; ArbGericht; LAG; BAG; Arbeitsschutzbehoerden der Laender.
EU/Voelkerrecht: Arbeitsschutz-RL; Arbeitszeit-RL; Plattformarbeit-RL; ArbeitnehmerInfo-RL.
Pruefpunkte: <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine: <Sachfeld-spezifisch>
Naechste Skills: legw-ressortaufgaben-bmas; normhierarchie-routing;
 normenkartierung; verfassungsmaessigkeit-quercheck;
 europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmas` -> `legw-ressortaufgaben-bmas` -> `legw-bmas-arbeitsrecht-und-arbeitsschutz` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 3. `legw-bmas-arbeitsschutz-und-arbeitssicherheit`

**Fokus:** Sachbereich Arbeitsschutz und Arbeitssicherheit im Geschaeftsbereich BMAS: Normbestand (ArbSchG; ArbStaettV; BetrSichV; BiostoffV; LasthandhabV; PSA-BV; ArbMedVV.); Akteure (BAuA; UVT (Berufsgenossenschaften); Laender-Arbeitsschutzbehoerden; KomNet.); EU-Bezug (Arbeitsschutz-Rahmenrichtlinie 89/391/EWG; Tochterrichtlinien.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmas (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmas (Heranfuehrung).


# Arbeitsschutz und Arbeitssicherheit (BMAS)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Arbeitsschutz und Arbeitssicherheit im Geschaeftsbereich BMAS. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmas`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmas`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: ArbSchG; ArbStaettV; BetrSichV; BiostoffV; LasthandhabV; PSA-BV; ArbMedVV.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

BAuA; UVT (Berufsgenossenschaften); Laender-Arbeitsschutzbehoerden; KomNet.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

Arbeitsschutz-Rahmenrichtlinie 89/391/EWG; Tochterrichtlinien.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Gefaehrdungsbeurteilung; Schutzmassnahmen; Unterweisung; ArbMed; Ueberwachung.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Sektor-spezifische Vorgaben; Vollzugsdefizit; Mehrfachzustaendigkeiten Land und UVT.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld: Arbeitsschutz und Arbeitssicherheit
Ressort: BMAS
Kernnormen: ArbSchG; ArbStaettV; BetrSichV; BiostoffV; LasthandhabV; PSA-BV; ArbMedVV.
Akteure/Aufsicht: BAuA; UVT (Berufsgenossenschaften); Laender-Arbeitsschutzbehoerden; KomNet.
EU/Voelkerrecht: Arbeitsschutz-Rahmenrichtlinie 89/391/EWG; Tochterrichtlinien.
Pruefpunkte: <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine: <Sachfeld-spezifisch>
Naechste Skills: legw-ressortaufgaben-bmas; normhierarchie-routing;
 normenkartierung; verfassungsmaessigkeit-quercheck;
 europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmas` -> `legw-ressortaufgaben-bmas` -> `legw-bmas-arbeitsschutz-und-arbeitssicherheit` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 4. `legw-bmas-sozialversicherungsrecht-sgb`

**Fokus:** Sachbereich Sozialversicherungsrecht (SGB) im Geschaeftsbereich BMAS: Normbestand (SGB I bis SGB XII; ASVG-Aequivalent; AsylbLG (mit BMI).); Akteure (DRV Bund; BA; GKV-Spitzenverband; BAS (Bundesamt fuer Soziale Sicherung); SGericht.); EU-Bezug (VO 883/2004 (Koordinierung); EFTA; bilaterale Abkommen.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmas (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmas (Heranfuehrung).


# Sozialversicherungsrecht (SGB) (BMAS)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Sozialversicherungsrecht (SGB) im Geschaeftsbereich BMAS. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmas`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmas`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: SGB I bis SGB XII; ASVG-Aequivalent; AsylbLG (mit BMI).

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

DRV Bund; BA; GKV-Spitzenverband; BAS (Bundesamt fuer Soziale Sicherung); SGericht.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

VO 883/2004 (Koordinierung); EFTA; bilaterale Abkommen.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Versicherungspflicht; Leistungen; Beitragsrecht; Mitwirkungspflichten; Statusfeststellung (Scheinselbststaendigkeit).

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Schnittstellen zwischen SGB-Buechern; EU-Koordinierung; Statusfeststellung.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld: Sozialversicherungsrecht (SGB)
Ressort: BMAS
Kernnormen: SGB I bis SGB XII; ASVG-Aequivalent; AsylbLG (mit BMI).
Akteure/Aufsicht: DRV Bund; BA; GKV-Spitzenverband; BAS (Bundesamt fuer Soziale Sicherung); SGericht.
EU/Voelkerrecht: VO 883/2004 (Koordinierung); EFTA; bilaterale Abkommen.
Pruefpunkte: <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine: <Sachfeld-spezifisch>
Naechste Skills: legw-ressortaufgaben-bmas; normhierarchie-routing;
 normenkartierung; verfassungsmaessigkeit-quercheck;
 europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmas` -> `legw-ressortaufgaben-bmas` -> `legw-bmas-sozialversicherungsrecht-sgb` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
