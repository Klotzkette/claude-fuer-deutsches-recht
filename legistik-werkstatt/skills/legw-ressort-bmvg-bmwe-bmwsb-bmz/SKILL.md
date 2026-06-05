---
name: legw-ressort-bmvg-bmwe-bmwsb-bmz
description: "Legw Ressort Bmvg Bmwe Bmwsb BMZ: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Legw Ressort Bmvg Bmwe Bmwsb BMZ

## Arbeitsbereich

Dieser Skill bündelt 8 sachlich verwandte Arbeitsschritte rund um **Legw Ressort Bmvg Bmwe Bmwsb BMZ** im Plugin Legistik-Werkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `legw-ressort-bmvg` | Heranfuehrung Ressort BMVg (Bundesministerium der Verteidigung). Schwerpunkt: Wehrrecht; militaerische Beschaffung; NATO-Bezuege; Verteidigungstechnologie; Reserve. Kernnormen: SG; WStG; UZwGBw; BwBeschG; NATO-Truppenstatut; AWG; KrWaffKG; ResG. Fuenf Spezialfelder: wehrrecht-und-soldatenstatus; militaerische-beschaffung-und-vergaberecht; nato-und-stationierungsrecht; verteidigungstechnologie-export; reservisten-und-zivilschutzrecht. Output: Ressort-Kompass mit Materie; Akteuren; Normbestand; Aufsicht und Stolpersteinen. Anschluss legw-ressortaufgaben-bmvg und legw-bmvg-Themenslug. |
| `legw-ressort-bmwe` | Heranfuehrung Ressort BMWE (Bundesministerium fuer Wirtschaft und Energie). Schwerpunkt: Energie und Netze; Erneuerbare; Industriepolitik; Aussenwirtschaft; Wettbewerb. Kernnormen: EnWG; EEG; WindBG; KWKG; BEHG; AWG; AWV; GWB; UStG; ARegV. Fuenf Spezialfelder: energie-und-netzregulierung-enwg; erneuerbare-energien-eeg-windbg; industriepolitik-foerderrecht-und-beihilfen; aussenwirtschaft-und-investitionspruefung; wettbewerb-und-kartellrecht-gwb. Output: Ressort-Kompass mit Materie; Akteuren; Normbestand; Aufsicht und Stolpersteinen. Anschluss legw-ressortaufgaben-bmwe und legw-bmwe-Themenslug. |
| `legw-ressort-bmwsb` | Heranfuehrung Ressort BMWSB (Bundesministerium fuer Wohnen; Stadtentwicklung und Bauwesen). Schwerpunkt: Bauplanung; Mietrecht; Stadtentwicklung; Bauprodukte; energetische Sanierung. Kernnormen: BauGB; BauNVO; BGB Mietrecht; StaedtebauFoerdG; BauPG; BauPVO; GEG; WoFG. Fuenf Spezialfelder: bau-und-planungsrecht-baugb-baunvo; mietrecht-und-wohnungspolitik; stadtentwicklung-und-foerderprogramme; bauproduktenrecht-und-technische-normen; energetische-sanierung-und-geg. Output: Ressort-Kompass mit Materie; Akteuren; Normbestand; Aufsicht und Stolpersteinen. Anschluss legw-ressortaufgaben-bmwsb und legw-bmwsb-Themenslug. |
| `legw-ressort-bmz` | Heranfuehrung Ressort BMZ (Bundesministerium fuer wirtschaftliche Zusammenarbeit und Entwicklung). Schwerpunkt: Entwicklungszusammenarbeit; humanitaere Hilfe; Klimafinanzierung; Lieferketten; Multilaterales. Kernnormen: Bilaterale Abkommen; LkSG; KSG; Pariser Abkommen (BGBl); EUZBLG; HBKG. Fuenf Spezialfelder: entwicklungszusammenarbeit-und-bilaterale-abkommen; humanitaere-hilfe-und-krisenpraevention; internationale-klimafinanzierung; menschenrechte-in-lieferketten-lksg; multilaterale-zusammenarbeit-und-eu. Output: Ressort-Kompass mit Materie; Akteuren; Normbestand; Aufsicht und Stolpersteinen. Anschluss legw-ressortaufgaben-bmz und legw-bmz-Themenslug. |
| `legw-ressort-router` | Ressort-Router der Legistik-Werkstatt: leitet nach Auftragsaufnahme in das richtige Bundes-Ressort. Klaert Ressort-Kuerzel BMF; BMI; AA; BMVg; BMWE; BMFTR; BMJV; BMBFSFJ; BMAS; BMDS; BMV; BMUKN; BMG; BMLEH; BMZ und BMWSB. Pro Ressort: Heranfuehrung; Ressortaufgaben; fuenf Spezialfelder. Output: gewaehltes Ressort plus Skill-Empfehlungskette. Abgrenzung: legistik-auftragsaufnahme (vorher); normhierarchie-routing (Normwahl); normenkartierung (Bestandskartierung). |
| `legw-ressortaufgaben-aa` | Ressortaufgaben AA: typische Legistik-Aufgaben im Geschaeftsbereich Auswaertiges Amt. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-aa-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-aa (Heranfuehrung). |
| `legw-ressortaufgaben-bmas` | Ressortaufgaben BMAS: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Arbeit und Soziales. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmas-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmas (Heranfuehrung). |
| `legw-ressortaufgaben-bmbfsfj` | Ressortaufgaben BMBFSFJ: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Bildung; Familie; Senioren; Frauen und Jugend. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmbfsfj-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmbfsfj (Heranfuehrung). |

## Arbeitsweg

Im Plugin Legistik-Werkstatt gilt für **Legw Ressort Bmvg Bmwe Bmwsb BMZ**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `legw-ressort-bmvg`

**Fokus:** Heranfuehrung Ressort BMVg (Bundesministerium der Verteidigung). Schwerpunkt: Wehrrecht; militaerische Beschaffung; NATO-Bezuege; Verteidigungstechnologie; Reserve. Kernnormen: SG; WStG; UZwGBw; BwBeschG; NATO-Truppenstatut; AWG; KrWaffKG; ResG. Fuenf Spezialfelder: wehrrecht-und-soldatenstatus; militaerische-beschaffung-und-vergaberecht; nato-und-stationierungsrecht; verteidigungstechnologie-export; reservisten-und-zivilschutzrecht. Output: Ressort-Kompass mit Materie; Akteuren; Normbestand; Aufsicht und Stolpersteinen. Anschluss legw-ressortaufgaben-bmvg und legw-bmvg-Themenslug.

# Ressort-Heranfuehrung BMVg

> Heranfuehrungs-Skill nach `legw-ressort-router`. Politikwissenschaftliche Legistinnen und Legisten
> bekommen hier das Sachfeld-Verstaendnis fuer das Ressort, bevor sie an Normtext und Begruendung gehen.

## Ressort-Stammdaten

- **Volltitel:** Bundesministerium der Verteidigung
- **Kuerzel:** BMVg
- **Hausleitung Stand 2026:** Boris Pistorius (SPD)
- **Dienstsitz:** Fontainengraben 150; 53123 Bonn; Zweitsitz Stauffenbergstr. 18; 10785 Berlin
- **Schwerpunkt:** Wehrrecht; militaerische Beschaffung; NATO-Bezuege; Verteidigungstechnologie; Reserve.
- **Kernnormen im Geschaeftsbereich:** SG; WStG; UZwGBw; BwBeschG; NATO-Truppenstatut; AWG; KrWaffKG; ResG.

## Materie auf einer Seite

### Worum geht es sachlich

Wehrrecht; militaerische Beschaffung; NATO-Bezuege; Verteidigungstechnologie; Reserve. Dieses Ressort ist nicht primaer Politik; es ist sachverstaendige Verwaltung
einer Lebenswelt - Behoerden; Verbaende; technische Regeln; europaeische Rechtsakte und
Vollzugspraxis greifen ineinander.

### Wer spielt mit

- **Federfuehrendes Referat** (im BMVg)
- **Nachgeordnete Behoerden und Aufsichten** des Geschaeftsbereichs
- **Bundesrat-Ausschuss** (bei zustimmungs- oder einspruchspflichtigen Vorhaben)
- **Bundestags-Fachausschuss** (BMVg-Spiegel)
- **Verbaende** im Geschaeftsbereich (Beteiligung nach GGO Paragraf 47)
- **EU-Ebene** (Generaldirektion und Ratsformation)

### Welche Normen muss man lesen koennen

SG; WStG; UZwGBw; BwBeschG; NATO-Truppenstatut; AWG; KrWaffKG; ResG.

Daneben: GG-Bezuege; einschlaegige EU-Verordnungen und Richtlinien; einschlaegige Verfassungs-
gerichts-Linie und BVerwG-Linie.

## Was an diesem Ressort besonders ist

- **Sprache der Materie** - Begriffe sind oft technisch und unionsrechtlich vorgepraegt; Terminologie
 konsistent halten (siehe `terminologie-konsistenz`).
- **Vollzugskette** - Bund setzt Norm; Vollzug oft bei Laendern oder nachgeordneten Behoerden;
 Vollzugsfolgen muessen mitgedacht werden (siehe `folgenabschaetzung-erfuellungsaufwand`).
- **Anpassung an EU-Recht** - viele Materien sind EU-getrieben; Goldplating vermeiden
 (siehe `goldplating-vermeiden`).
- **Verfassungsrechtliche Empfindlichkeiten** - Eingriff in Grundrechte oder Foederalismus
 pruefen (siehe `verfassungsmaessigkeit-quercheck`).

## Fuenf Spezialfelder im Ressort

- `legw-bmvg-wehrrecht-und-soldatenstatus` - Wehrrecht und Soldatenstatus
- `legw-bmvg-militaerische-beschaffung-und-vergaberecht` - Militaerische Beschaffung und Vergaberecht
- `legw-bmvg-nato-und-stationierungsrecht` - NATO-Recht und Stationierungsrecht
- `legw-bmvg-verteidigungstechnologie-export` - Verteidigungstechnologie und Exportkontrolle
- `legw-bmvg-reservisten-und-zivilschutzrecht` - Reservistenrecht und Zivilschutzrecht

Diese fuenf Skills decken die typischen Sachfragen ab; jeder fuehrt durch Eingaben; Pruefpfad und
Output. Wer als Legist nicht Sachgebietsexperte ist; arbeitet sich ueber genau diese Skills ein.

## Stolpersteine - die fuenf haeufigsten

1. **Geschaeftsverteilung uebersehen** - Mitzeichner nicht beachtet; Vorhaben kippt in der Ressort-
 abstimmung.
2. **Vollzugsrealitaet unterschaetzt** - Norm ist sauber; Vollzug ist nicht finanziert oder nicht
 personell gedeckt; Erfuellungsaufwand falsch berechnet.
3. **EU-Vorgaben nicht passgenau** - Umsetzungsfrist verschlafen oder Mindestharmonisierung
 ueberschritten (Goldplating).
4. **Verbaendeanhoerung zu spaet** - GGO Paragraf 47 verlangt rechtzeitige Beteiligung; spaete
 Beteiligung kostet politisches Kapital.
5. **Terminologie inkonsistent** - in der Begruendung andere Begriffe als im Normtext.

## Vorgehen

### Schritt 1 - Stammdaten dieses Ressorts in das Auftragsblatt uebernehmen

Volltitel; Federfuehrung; Mitzeichner; Spiegelausschuss; verantwortliches Referat und Aufsicht
in das Auftragsblatt einpflegen.

### Schritt 2 - Spezialfeld waehlen

Aus den fuenf Spezialfeldern (siehe oben) das passende waehlen. Bei Mehrfachbezug: das
schwerpunktmaessige Feld federfuehrend; die anderen als Mitzeichnungs-Schnittstellen.

### Schritt 3 - Ressortaufgaben-Skill rufen

Anschluss an `legw-ressortaufgaben-bmvg` - dort ressortspezifische Aufgaben (Begruendung;
Verbaendeanhoerung; Bundestagsweg; Aufsicht).

### Schritt 4 - Werkstatt-Skills nutzen

`legistik-auftragsaufnahme`; `normhierarchie-routing`; `normenkartierung`;
`verfassungsmaessigkeit-quercheck`; `europarechtskonformitaet`; `folgenabschaetzung-*` und
`begruendung-allgemein-und-besonders` ergaenzen.

### Schritt 5 - Optional RuleMapping-Anschluss

Wenn das Vorhaben digital-tauglich werden soll: `legw-rmap-grundlagen` als Einstieg in die 10 RuleMapping-Skills (Abschluss mit `legw-rmap-anschluss-an-legw`).

## Output

Ressort-Kompass im Auftragsblatt:

```
Ressort: BMVg - Bundesministerium der Verteidigung
Hausleitung: Boris Pistorius (SPD)
Materie: Wehrrecht; militaerische Beschaffung; NATO-Bezuege; Verteidigungstechnologie; Reserve.
Kernnormen: SG; WStG; UZwGBw; BwBeschG; NATO-Truppenstatut; AWG; KrWaffKG; ResG.
Spezialfeld: <gewaehlter Slug>
Mitzeichner: <Liste>
Spiegelausschuss: <Bundestags-Ausschuss>
Verbaendekreis: <Listen-Liste>
EU-Bezug: <Generaldirektion und Rechtsakt>
Naechster Skill: legw-ressortaufgaben-bmvg
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 2. `legw-ressort-bmwe`

**Fokus:** Heranfuehrung Ressort BMWE (Bundesministerium fuer Wirtschaft und Energie). Schwerpunkt: Energie und Netze; Erneuerbare; Industriepolitik; Aussenwirtschaft; Wettbewerb. Kernnormen: EnWG; EEG; WindBG; KWKG; BEHG; AWG; AWV; GWB; UStG; ARegV. Fuenf Spezialfelder: energie-und-netzregulierung-enwg; erneuerbare-energien-eeg-windbg; industriepolitik-foerderrecht-und-beihilfen; aussenwirtschaft-und-investitionspruefung; wettbewerb-und-kartellrecht-gwb. Output: Ressort-Kompass mit Materie; Akteuren; Normbestand; Aufsicht und Stolpersteinen. Anschluss legw-ressortaufgaben-bmwe und legw-bmwe-Themenslug.

# Ressort-Heranfuehrung BMWE

> Heranfuehrungs-Skill nach `legw-ressort-router`. Politikwissenschaftliche Legistinnen und Legisten
> bekommen hier das Sachfeld-Verstaendnis fuer das Ressort, bevor sie an Normtext und Begruendung gehen.

## Ressort-Stammdaten

- **Volltitel:** Bundesministerium fuer Wirtschaft und Energie
- **Kuerzel:** BMWE
- **Hausleitung Stand 2026:** Katherina Reiche (CDU)
- **Dienstsitz:** Scharnhorststr. 34-37; 10115 Berlin; Zweitsitz Villemombler Str. 76; 53123 Bonn
- **Schwerpunkt:** Energie und Netze; Erneuerbare; Industriepolitik; Aussenwirtschaft; Wettbewerb.
- **Kernnormen im Geschaeftsbereich:** EnWG; EEG; WindBG; KWKG; BEHG; AWG; AWV; GWB; UStG; ARegV.

## Materie auf einer Seite

### Worum geht es sachlich

Energie und Netze; Erneuerbare; Industriepolitik; Aussenwirtschaft; Wettbewerb. Dieses Ressort ist nicht primaer Politik; es ist sachverstaendige Verwaltung
einer Lebenswelt - Behoerden; Verbaende; technische Regeln; europaeische Rechtsakte und
Vollzugspraxis greifen ineinander.

### Wer spielt mit

- **Federfuehrendes Referat** (im BMWE)
- **Nachgeordnete Behoerden und Aufsichten** des Geschaeftsbereichs
- **Bundesrat-Ausschuss** (bei zustimmungs- oder einspruchspflichtigen Vorhaben)
- **Bundestags-Fachausschuss** (BMWE-Spiegel)
- **Verbaende** im Geschaeftsbereich (Beteiligung nach GGO Paragraf 47)
- **EU-Ebene** (Generaldirektion und Ratsformation)

### Welche Normen muss man lesen koennen

EnWG; EEG; WindBG; KWKG; BEHG; AWG; AWV; GWB; UStG; ARegV.

Daneben: GG-Bezuege; einschlaegige EU-Verordnungen und Richtlinien; einschlaegige Verfassungs-
gerichts-Linie und BVerwG-Linie.

## Was an diesem Ressort besonders ist

- **Sprache der Materie** - Begriffe sind oft technisch und unionsrechtlich vorgepraegt; Terminologie
 konsistent halten (siehe `terminologie-konsistenz`).
- **Vollzugskette** - Bund setzt Norm; Vollzug oft bei Laendern oder nachgeordneten Behoerden;
 Vollzugsfolgen muessen mitgedacht werden (siehe `folgenabschaetzung-erfuellungsaufwand`).
- **Anpassung an EU-Recht** - viele Materien sind EU-getrieben; Goldplating vermeiden
 (siehe `goldplating-vermeiden`).
- **Verfassungsrechtliche Empfindlichkeiten** - Eingriff in Grundrechte oder Foederalismus
 pruefen (siehe `verfassungsmaessigkeit-quercheck`).

## Fuenf Spezialfelder im Ressort

- `legw-bmwe-energie-und-netzregulierung-enwg` - Energierecht und Netzregulierung (EnWG)
- `legw-bmwe-erneuerbare-energien-eeg-windbg` - Erneuerbare Energien (EEG; WindBG)
- `legw-bmwe-industriepolitik-foerderrecht-und-beihilfen` - Industriepolitik; Foerderrecht; EU-Beihilfen
- `legw-bmwe-aussenwirtschaft-und-investitionspruefung` - Aussenwirtschaft und Investitionspruefung
- `legw-bmwe-wettbewerb-und-kartellrecht-gwb` - Wettbewerbsrecht und Kartellrecht (GWB)

Diese fuenf Skills decken die typischen Sachfragen ab; jeder fuehrt durch Eingaben; Pruefpfad und
Output. Wer als Legist nicht Sachgebietsexperte ist; arbeitet sich ueber genau diese Skills ein.

## Stolpersteine - die fuenf haeufigsten

1. **Geschaeftsverteilung uebersehen** - Mitzeichner nicht beachtet; Vorhaben kippt in der Ressort-
 abstimmung.
2. **Vollzugsrealitaet unterschaetzt** - Norm ist sauber; Vollzug ist nicht finanziert oder nicht
 personell gedeckt; Erfuellungsaufwand falsch berechnet.
3. **EU-Vorgaben nicht passgenau** - Umsetzungsfrist verschlafen oder Mindestharmonisierung
 ueberschritten (Goldplating).
4. **Verbaendeanhoerung zu spaet** - GGO Paragraf 47 verlangt rechtzeitige Beteiligung; spaete
 Beteiligung kostet politisches Kapital.
5. **Terminologie inkonsistent** - in der Begruendung andere Begriffe als im Normtext.

## Vorgehen

### Schritt 1 - Stammdaten dieses Ressorts in das Auftragsblatt uebernehmen

Volltitel; Federfuehrung; Mitzeichner; Spiegelausschuss; verantwortliches Referat und Aufsicht
in das Auftragsblatt einpflegen.

### Schritt 2 - Spezialfeld waehlen

Aus den fuenf Spezialfeldern (siehe oben) das passende waehlen. Bei Mehrfachbezug: das
schwerpunktmaessige Feld federfuehrend; die anderen als Mitzeichnungs-Schnittstellen.

### Schritt 3 - Ressortaufgaben-Skill rufen

Anschluss an `legw-ressortaufgaben-bmwe` - dort ressortspezifische Aufgaben (Begruendung;
Verbaendeanhoerung; Bundestagsweg; Aufsicht).

### Schritt 4 - Werkstatt-Skills nutzen

`legistik-auftragsaufnahme`; `normhierarchie-routing`; `normenkartierung`;
`verfassungsmaessigkeit-quercheck`; `europarechtskonformitaet`; `folgenabschaetzung-*` und
`begruendung-allgemein-und-besonders` ergaenzen.

### Schritt 5 - Optional RuleMapping-Anschluss

Wenn das Vorhaben digital-tauglich werden soll: `legw-rmap-grundlagen` als Einstieg in die 10 RuleMapping-Skills (Abschluss mit `legw-rmap-anschluss-an-legw`).

## Output

Ressort-Kompass im Auftragsblatt:

```
Ressort: BMWE - Bundesministerium fuer Wirtschaft und Energie
Hausleitung: Katherina Reiche (CDU)
Materie: Energie und Netze; Erneuerbare; Industriepolitik; Aussenwirtschaft; Wettbewerb.
Kernnormen: EnWG; EEG; WindBG; KWKG; BEHG; AWG; AWV; GWB; UStG; ARegV.
Spezialfeld: <gewaehlter Slug>
Mitzeichner: <Liste>
Spiegelausschuss: <Bundestags-Ausschuss>
Verbaendekreis: <Listen-Liste>
EU-Bezug: <Generaldirektion und Rechtsakt>
Naechster Skill: legw-ressortaufgaben-bmwe
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 3. `legw-ressort-bmwsb`

**Fokus:** Heranfuehrung Ressort BMWSB (Bundesministerium fuer Wohnen; Stadtentwicklung und Bauwesen). Schwerpunkt: Bauplanung; Mietrecht; Stadtentwicklung; Bauprodukte; energetische Sanierung. Kernnormen: BauGB; BauNVO; BGB Mietrecht; StaedtebauFoerdG; BauPG; BauPVO; GEG; WoFG. Fuenf Spezialfelder: bau-und-planungsrecht-baugb-baunvo; mietrecht-und-wohnungspolitik; stadtentwicklung-und-foerderprogramme; bauproduktenrecht-und-technische-normen; energetische-sanierung-und-geg. Output: Ressort-Kompass mit Materie; Akteuren; Normbestand; Aufsicht und Stolpersteinen. Anschluss legw-ressortaufgaben-bmwsb und legw-bmwsb-Themenslug.

# Ressort-Heranfuehrung BMWSB

> Heranfuehrungs-Skill nach `legw-ressort-router`. Politikwissenschaftliche Legistinnen und Legisten
> bekommen hier das Sachfeld-Verstaendnis fuer das Ressort, bevor sie an Normtext und Begruendung gehen.

## Ressort-Stammdaten

- **Volltitel:** Bundesministerium fuer Wohnen; Stadtentwicklung und Bauwesen
- **Kuerzel:** BMWSB
- **Hausleitung Stand 2026:** Verena Hubertz (SPD)
- **Dienstsitz:** Krausenstr. 17-18; 10117 Berlin; Zweitsitz Deichmanns Aue 31-37; 53179 Bonn
- **Schwerpunkt:** Bauplanung; Mietrecht; Stadtentwicklung; Bauprodukte; energetische Sanierung.
- **Kernnormen im Geschaeftsbereich:** BauGB; BauNVO; BGB Mietrecht; StaedtebauFoerdG; BauPG; BauPVO; GEG; WoFG.

## Materie auf einer Seite

### Worum geht es sachlich

Bauplanung; Mietrecht; Stadtentwicklung; Bauprodukte; energetische Sanierung. Dieses Ressort ist nicht primaer Politik; es ist sachverstaendige Verwaltung
einer Lebenswelt - Behoerden; Verbaende; technische Regeln; europaeische Rechtsakte und
Vollzugspraxis greifen ineinander.

### Wer spielt mit

- **Federfuehrendes Referat** (im BMWSB)
- **Nachgeordnete Behoerden und Aufsichten** des Geschaeftsbereichs
- **Bundesrat-Ausschuss** (bei zustimmungs- oder einspruchspflichtigen Vorhaben)
- **Bundestags-Fachausschuss** (BMWSB-Spiegel)
- **Verbaende** im Geschaeftsbereich (Beteiligung nach GGO Paragraf 47)
- **EU-Ebene** (Generaldirektion und Ratsformation)

### Welche Normen muss man lesen koennen

BauGB; BauNVO; BGB Mietrecht; StaedtebauFoerdG; BauPG; BauPVO; GEG; WoFG.

Daneben: GG-Bezuege; einschlaegige EU-Verordnungen und Richtlinien; einschlaegige Verfassungs-
gerichts-Linie und BVerwG-Linie.

## Was an diesem Ressort besonders ist

- **Sprache der Materie** - Begriffe sind oft technisch und unionsrechtlich vorgepraegt; Terminologie
 konsistent halten (siehe `terminologie-konsistenz`).
- **Vollzugskette** - Bund setzt Norm; Vollzug oft bei Laendern oder nachgeordneten Behoerden;
 Vollzugsfolgen muessen mitgedacht werden (siehe `folgenabschaetzung-erfuellungsaufwand`).
- **Anpassung an EU-Recht** - viele Materien sind EU-getrieben; Goldplating vermeiden
 (siehe `goldplating-vermeiden`).
- **Verfassungsrechtliche Empfindlichkeiten** - Eingriff in Grundrechte oder Foederalismus
 pruefen (siehe `verfassungsmaessigkeit-quercheck`).

## Fuenf Spezialfelder im Ressort

- `legw-bmwsb-bau-und-planungsrecht-baugb-baunvo` - Bau- und Planungsrecht (BauGB; BauNVO)
- `legw-bmwsb-mietrecht-und-wohnungspolitik` - Mietrecht und Wohnungspolitik
- `legw-bmwsb-stadtentwicklung-und-foerderprogramme` - Stadtentwicklung und Foerderprogramme
- `legw-bmwsb-bauproduktenrecht-und-technische-normen` - Bauproduktenrecht und technische Normen
- `legw-bmwsb-energetische-sanierung-und-geg` - Energetische Sanierung (GEG)

Diese fuenf Skills decken die typischen Sachfragen ab; jeder fuehrt durch Eingaben; Pruefpfad und
Output. Wer als Legist nicht Sachgebietsexperte ist; arbeitet sich ueber genau diese Skills ein.

## Stolpersteine - die fuenf haeufigsten

1. **Geschaeftsverteilung uebersehen** - Mitzeichner nicht beachtet; Vorhaben kippt in der Ressort-
 abstimmung.
2. **Vollzugsrealitaet unterschaetzt** - Norm ist sauber; Vollzug ist nicht finanziert oder nicht
 personell gedeckt; Erfuellungsaufwand falsch berechnet.
3. **EU-Vorgaben nicht passgenau** - Umsetzungsfrist verschlafen oder Mindestharmonisierung
 ueberschritten (Goldplating).
4. **Verbaendeanhoerung zu spaet** - GGO Paragraf 47 verlangt rechtzeitige Beteiligung; spaete
 Beteiligung kostet politisches Kapital.
5. **Terminologie inkonsistent** - in der Begruendung andere Begriffe als im Normtext.

## Vorgehen

### Schritt 1 - Stammdaten dieses Ressorts in das Auftragsblatt uebernehmen

Volltitel; Federfuehrung; Mitzeichner; Spiegelausschuss; verantwortliches Referat und Aufsicht
in das Auftragsblatt einpflegen.

### Schritt 2 - Spezialfeld waehlen

Aus den fuenf Spezialfeldern (siehe oben) das passende waehlen. Bei Mehrfachbezug: das
schwerpunktmaessige Feld federfuehrend; die anderen als Mitzeichnungs-Schnittstellen.

### Schritt 3 - Ressortaufgaben-Skill rufen

Anschluss an `legw-ressortaufgaben-bmwsb` - dort ressortspezifische Aufgaben (Begruendung;
Verbaendeanhoerung; Bundestagsweg; Aufsicht).

### Schritt 4 - Werkstatt-Skills nutzen

`legistik-auftragsaufnahme`; `normhierarchie-routing`; `normenkartierung`;
`verfassungsmaessigkeit-quercheck`; `europarechtskonformitaet`; `folgenabschaetzung-*` und
`begruendung-allgemein-und-besonders` ergaenzen.

### Schritt 5 - Optional RuleMapping-Anschluss

Wenn das Vorhaben digital-tauglich werden soll: `legw-rmap-grundlagen` als Einstieg in die 10 RuleMapping-Skills (Abschluss mit `legw-rmap-anschluss-an-legw`).

## Output

Ressort-Kompass im Auftragsblatt:

```
Ressort: BMWSB - Bundesministerium fuer Wohnen; Stadtentwicklung und Bauwesen
Hausleitung: Verena Hubertz (SPD)
Materie: Bauplanung; Mietrecht; Stadtentwicklung; Bauprodukte; energetische Sanierung.
Kernnormen: BauGB; BauNVO; BGB Mietrecht; StaedtebauFoerdG; BauPG; BauPVO; GEG; WoFG.
Spezialfeld: <gewaehlter Slug>
Mitzeichner: <Liste>
Spiegelausschuss: <Bundestags-Ausschuss>
Verbaendekreis: <Listen-Liste>
EU-Bezug: <Generaldirektion und Rechtsakt>
Naechster Skill: legw-ressortaufgaben-bmwsb
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 4. `legw-ressort-bmz`

**Fokus:** Heranfuehrung Ressort BMZ (Bundesministerium fuer wirtschaftliche Zusammenarbeit und Entwicklung). Schwerpunkt: Entwicklungszusammenarbeit; humanitaere Hilfe; Klimafinanzierung; Lieferketten; Multilaterales. Kernnormen: Bilaterale Abkommen; LkSG; KSG; Pariser Abkommen (BGBl); EUZBLG; HBKG. Fuenf Spezialfelder: entwicklungszusammenarbeit-und-bilaterale-abkommen; humanitaere-hilfe-und-krisenpraevention; internationale-klimafinanzierung; menschenrechte-in-lieferketten-lksg; multilaterale-zusammenarbeit-und-eu. Output: Ressort-Kompass mit Materie; Akteuren; Normbestand; Aufsicht und Stolpersteinen. Anschluss legw-ressortaufgaben-bmz und legw-bmz-Themenslug.

# Ressort-Heranfuehrung BMZ

> Heranfuehrungs-Skill nach `legw-ressort-router`. Politikwissenschaftliche Legistinnen und Legisten
> bekommen hier das Sachfeld-Verstaendnis fuer das Ressort, bevor sie an Normtext und Begruendung gehen.

## Ressort-Stammdaten

- **Volltitel:** Bundesministerium fuer wirtschaftliche Zusammenarbeit und Entwicklung
- **Kuerzel:** BMZ
- **Hausleitung Stand 2026:** Reem Alabali Radovan (SPD)
- **Dienstsitz:** Stresemannstr. 94; 10963 Berlin; Zweitsitz Dahlmannstr. 4; 53113 Bonn
- **Schwerpunkt:** Entwicklungszusammenarbeit; humanitaere Hilfe; Klimafinanzierung; Lieferketten; Multilaterales.
- **Kernnormen im Geschaeftsbereich:** Bilaterale Abkommen; LkSG; KSG; Pariser Abkommen (BGBl); EUZBLG; HBKG.

## Materie auf einer Seite

### Worum geht es sachlich

Entwicklungszusammenarbeit; humanitaere Hilfe; Klimafinanzierung; Lieferketten; Multilaterales. Dieses Ressort ist nicht primaer Politik; es ist sachverstaendige Verwaltung
einer Lebenswelt - Behoerden; Verbaende; technische Regeln; europaeische Rechtsakte und
Vollzugspraxis greifen ineinander.

### Wer spielt mit

- **Federfuehrendes Referat** (im BMZ)
- **Nachgeordnete Behoerden und Aufsichten** des Geschaeftsbereichs
- **Bundesrat-Ausschuss** (bei zustimmungs- oder einspruchspflichtigen Vorhaben)
- **Bundestags-Fachausschuss** (BMZ-Spiegel)
- **Verbaende** im Geschaeftsbereich (Beteiligung nach GGO Paragraf 47)
- **EU-Ebene** (Generaldirektion und Ratsformation)

### Welche Normen muss man lesen koennen

Bilaterale Abkommen; LkSG; KSG; Pariser Abkommen (BGBl); EUZBLG; HBKG.

Daneben: GG-Bezuege; einschlaegige EU-Verordnungen und Richtlinien; einschlaegige Verfassungs-
gerichts-Linie und BVerwG-Linie.

## Was an diesem Ressort besonders ist

- **Sprache der Materie** - Begriffe sind oft technisch und unionsrechtlich vorgepraegt; Terminologie
 konsistent halten (siehe `terminologie-konsistenz`).
- **Vollzugskette** - Bund setzt Norm; Vollzug oft bei Laendern oder nachgeordneten Behoerden;
 Vollzugsfolgen muessen mitgedacht werden (siehe `folgenabschaetzung-erfuellungsaufwand`).
- **Anpassung an EU-Recht** - viele Materien sind EU-getrieben; Goldplating vermeiden
 (siehe `goldplating-vermeiden`).
- **Verfassungsrechtliche Empfindlichkeiten** - Eingriff in Grundrechte oder Foederalismus
 pruefen (siehe `verfassungsmaessigkeit-quercheck`).

## Fuenf Spezialfelder im Ressort

- `legw-bmz-entwicklungszusammenarbeit-und-bilaterale-abkommen` - Entwicklungszusammenarbeit und bilaterale Abkommen
- `legw-bmz-humanitaere-hilfe-und-krisenpraevention` - Humanitaere Hilfe und Krisenpraevention
- `legw-bmz-internationale-klimafinanzierung` - Internationale Klimafinanzierung
- `legw-bmz-menschenrechte-in-lieferketten-lksg` - Menschenrechte in Lieferketten (LkSG)
- `legw-bmz-multilaterale-zusammenarbeit-und-eu` - Multilaterale Zusammenarbeit und EU

Diese fuenf Skills decken die typischen Sachfragen ab; jeder fuehrt durch Eingaben; Pruefpfad und
Output. Wer als Legist nicht Sachgebietsexperte ist; arbeitet sich ueber genau diese Skills ein.

## Stolpersteine - die fuenf haeufigsten

1. **Geschaeftsverteilung uebersehen** - Mitzeichner nicht beachtet; Vorhaben kippt in der Ressort-
 abstimmung.
2. **Vollzugsrealitaet unterschaetzt** - Norm ist sauber; Vollzug ist nicht finanziert oder nicht
 personell gedeckt; Erfuellungsaufwand falsch berechnet.
3. **EU-Vorgaben nicht passgenau** - Umsetzungsfrist verschlafen oder Mindestharmonisierung
 ueberschritten (Goldplating).
4. **Verbaendeanhoerung zu spaet** - GGO Paragraf 47 verlangt rechtzeitige Beteiligung; spaete
 Beteiligung kostet politisches Kapital.
5. **Terminologie inkonsistent** - in der Begruendung andere Begriffe als im Normtext.

## Vorgehen

### Schritt 1 - Stammdaten dieses Ressorts in das Auftragsblatt uebernehmen

Volltitel; Federfuehrung; Mitzeichner; Spiegelausschuss; verantwortliches Referat und Aufsicht
in das Auftragsblatt einpflegen.

### Schritt 2 - Spezialfeld waehlen

Aus den fuenf Spezialfeldern (siehe oben) das passende waehlen. Bei Mehrfachbezug: das
schwerpunktmaessige Feld federfuehrend; die anderen als Mitzeichnungs-Schnittstellen.

### Schritt 3 - Ressortaufgaben-Skill rufen

Anschluss an `legw-ressortaufgaben-bmz` - dort ressortspezifische Aufgaben (Begruendung;
Verbaendeanhoerung; Bundestagsweg; Aufsicht).

### Schritt 4 - Werkstatt-Skills nutzen

`legistik-auftragsaufnahme`; `normhierarchie-routing`; `normenkartierung`;
`verfassungsmaessigkeit-quercheck`; `europarechtskonformitaet`; `folgenabschaetzung-*` und
`begruendung-allgemein-und-besonders` ergaenzen.

### Schritt 5 - Optional RuleMapping-Anschluss

Wenn das Vorhaben digital-tauglich werden soll: `legw-rmap-grundlagen` als Einstieg in die 10 RuleMapping-Skills (Abschluss mit `legw-rmap-anschluss-an-legw`).

## Output

Ressort-Kompass im Auftragsblatt:

```
Ressort: BMZ - Bundesministerium fuer wirtschaftliche Zusammenarbeit und Entwicklung
Hausleitung: Reem Alabali Radovan (SPD)
Materie: Entwicklungszusammenarbeit; humanitaere Hilfe; Klimafinanzierung; Lieferketten; Multilaterales.
Kernnormen: Bilaterale Abkommen; LkSG; KSG; Pariser Abkommen (BGBl); EUZBLG; HBKG.
Spezialfeld: <gewaehlter Slug>
Mitzeichner: <Liste>
Spiegelausschuss: <Bundestags-Ausschuss>
Verbaendekreis: <Listen-Liste>
EU-Bezug: <Generaldirektion und Rechtsakt>
Naechster Skill: legw-ressortaufgaben-bmz
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 5. `legw-ressort-router`

**Fokus:** Ressort-Router der Legistik-Werkstatt: leitet nach Auftragsaufnahme in das richtige Bundes-Ressort. Klaert Ressort-Kuerzel BMF; BMI; AA; BMVg; BMWE; BMFTR; BMJV; BMBFSFJ; BMAS; BMDS; BMV; BMUKN; BMG; BMLEH; BMZ und BMWSB. Pro Ressort: Heranfuehrung; Ressortaufgaben; fuenf Spezialfelder. Output: gewaehltes Ressort plus Skill-Empfehlungskette. Abgrenzung: legistik-auftragsaufnahme (vorher); normhierarchie-routing (Normwahl); normenkartierung (Bestandskartierung).

# Legistik-Werkstatt - Ressort-Router

> Zweiter Skill nach legistik-auftragsaufnahme. Leitet auf den fachlich richtigen Ressort-Kompass.

## Wozu

Legistinnen und Legisten kommen oft aus den Politikwissenschaften, dem oeffentlichen Recht oder aus
Verwaltungslaufbahnen - das Ressort und seine Materie sind dabei zunaechst nicht ihr Heimspielfeld.
Dieser Skill macht den Sprung vom abstrakten Vorhaben zur ressortspezifischen Arbeitsumgebung:
**welches Ministerium - welche Materie - welche Skills.**

## Ressort-Matrix Bundesregierung Kabinett Merz Stand 2026

| Kuerzel | Ressort | Schwerpunkt |
|---|---|---|
| BMF | Finanzen | Steuern; Haushalt; Finanzmarkt; Zoll; Geldwaesche |
| BMI | Innern | Sicherheit; Migration; Verwaltung; Bevoelkerungsschutz; oeffentlicher Dienst |
| AA | Auswaertiges Amt | Voelkerrecht; Konsular; Aussenwirtschaft; EU-Verfahren; Sanktionen |
| BMVg | Verteidigung | Wehrrecht; Beschaffung; NATO; Wehrtechnik; Reserve |
| BMWE | Wirtschaft und Energie | Energie und Netze; Erneuerbare; Industrie; Kartellrecht |
| BMFTR | Forschung; Technologie; Raumfahrt | Hochschule; Raumfahrt; Forschungsfoerderung; KI; Biotech |
| BMJV | Justiz und Verbraucherschutz | BGB; StGB; Prozessrecht; Verbraucherschutz; Rechtsstaat |
| BMBFSFJ | Bildung; Familie; Senioren; Frauen; Jugend | Schule; Jugendhilfe; Familie; Gleichstellung; Senioren |
| BMAS | Arbeit und Soziales | Arbeitsrecht; SGB; Rente; Arbeitsschutz; Teilhabe |
| BMDS | Digitales und Staatsmodernisierung | OZG; IT-Sicherheit; Datenrecht; Register; KI-VO |
| BMV | Verkehr | Strasse; Schiene; Luft; Wasser; Fuehrerschein |
| BMUKN | Umwelt; Klimaschutz; Naturschutz; nukleare Sicherheit | BImSchG; Wasser; Abfall; Naturschutz; Nukleares |
| BMG | Gesundheit | Arzneimittel; SGB V; IfSG; Heilberufe; Krankenhaus |
| BMLEH | Landwirtschaft; Ernaehrung; Heimat | Agrar; Tierschutz; Lebensmittel; Forst; Oekolandbau |
| BMZ | Wirtschaftliche Zusammenarbeit und Entwicklung | Bilaterale Abkommen; humanitaere Hilfe; Klimafinanzierung |
| BMWSB | Wohnen; Stadtentwicklung; Bauwesen | BauGB; Mietrecht; Stadtentwicklung; Bauprodukte; GEG |

## Vorgehen

### Schritt 1 - Ressort waehlen

Der Auftrag wurde in `legistik-auftragsaufnahme` aufgenommen. Frage:

> Welches Bundesressort fuehrt federfuehrend (BMF; BMI; AA; BMVg; BMWE; BMFTR; BMJV; BMBFSFJ;
> BMAS; BMDS; BMV; BMUKN; BMG; BMLEH; BMZ; BMWSB)?

Bei Mitzeichnung oder ressortuebergreifenden Vorhaben: federfuehrendes Ressort + alle Mitzeichner
festhalten. Federfuehrung steuert HdR-Vorlage; Mitzeichner steuern Inhalte.

### Schritt 2 - Heranfuehrungs-Skill rufen

Jedes Ressort hat einen Heranfuehrungs-Skill `legw-ressort-<kuerzel>`. Beispiel:
- Federfuehrer BMUKN -> `legw-ressort-bmukn` (Atomrecht; Immissionsschutz; Wasser; Abfall; Naturschutz)
- Federfuehrer BMLEH -> `legw-ressort-bmleh` (Agrar; Tierschutz; Lebensmittel; Forst; Oekolandbau)

Diese Skills erklaeren in kurzer Form **Materie; Akteure; Normbestand; typische Stolpersteine**.

### Schritt 3 - Ressortaufgaben-Skill rufen

Pro Ressort gibt es `legw-ressortaufgaben-<kuerzel>`. Er bricht die typische Legistik-Aufgabe
auf das Ressort herunter: welche Begruendungsteile; welche Verbaende; welche Befassung im
Bundestag; welche Ausschuesse; welche Aufsicht; welche Fristen.

### Schritt 4 - Spezialfeld-Skill rufen

Jedes Ressort hat fuenf Spezialfeld-Skills `legw-<kuerzel>-<thema>`. Beispiel BMLEH:
- `legw-bmleh-agrar-und-foerderungsrecht-gak-gap`
- `legw-bmleh-tierschutz-und-tiergesundheitsrecht`
- `legw-bmleh-lebensmittelrecht-und-futtermittelrecht`
- `legw-bmleh-forst-und-jagdrecht`
- `legw-bmleh-oekolandbau-und-pflanzenschutzrecht`

Diese decken sachliche Detailfragen ab und sind das Brett, auf dem der Politikwissenschaftler steht,
wenn er an eine fremde Materie heran muss.

### Schritt 5 - Optional RuleMapping-Anschluss

Wenn das Vorhaben digital-tauglich werden soll (BMJ-Initiative; SPRIND-Foerderung; Rulemap-Builder):
weiter zu `legw-rmap-grundlagen` als didaktischem Einstieg in die RuleMapping-Methodik. Von dort fuehren insgesamt 10 RuleMapping-Skills durch den Workflow: `legw-rmap-grundlagen`, `legw-rmap-norm-zu-rulemap`, `legw-rmap-tatbestand-und-rechtsfolge`, `legw-rmap-verweisungen-und-ausnahmen`, `legw-rmap-bestimmtheit-und-justitiabilitaet`, `legw-rmap-entscheidungsbaum-validierung`, `legw-rmap-vollzugstauglichkeit`, `legw-rmap-evaluierung-und-aenderung`, `legw-rmap-export-und-systemintegration` und `legw-rmap-anschluss-an-legw` als Rueckkopplung in die Legistik-Werkstatt.

## Output

Ein Routing-Block fuer das Auftragsblatt:

```
Ressort federfuehrend: <kuerzel> - <Volltitel>
Mitzeichnende Ressorts: <Liste>
Empfohlene Skill-Kette:
 1. legw-ressort-<kuerzel> (Heranfuehrung)
 2. legw-ressortaufgaben-<kuerzel> (Ressortaufgaben)
 3. legw-<kuerzel>-<thema> (Spezialfeld)
 4. normhierarchie-routing (Normwahl)
 5. <weitere Spezial- und Werkstattskills>
Optional RuleMapping-Anschluss: legw-rmap-grundlagen (Einstieg in 10 RuleMapping-Skills)
```

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 6. `legw-ressortaufgaben-aa`

**Fokus:** Ressortaufgaben AA: typische Legistik-Aufgaben im Geschaeftsbereich Auswaertiges Amt. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-aa-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-aa (Heranfuehrung).

# Ressortaufgaben AA

> Dritter Skill in der Ressort-Kette. Nach `legw-ressort-aa` (Heranfuehrung) und vor den
> fuenf Spezialfeldern. Bricht die typische Legistik-Aufgabe auf das AA herunter.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme` mit Ressort-Eintrag AA
- Ressort-Kompass aus `legw-ressort-aa`
- Geplante Vorhabenart (Gesetz; Rechtsverordnung; Eckpunktepapier; Aenderungsantrag; Vorlage)
- Politische Zielvorgabe (Koalitionsvertrag; Kabinettsbeschluss; Pruefauftrag)

## Vorgehen

### Schritt 1 - Vorhabenart einordnen

| Vorhabenart | Zustaendigkeit im AA | Vorlageweg |
|---|---|---|
| Eckpunktepapier | Fachreferat plus Hausleitung | Hausintern; ggf. Ressortbesprechung |
| Referentenentwurf | Fachreferat fuehrt; Hauspruefung (Z; ZA; ZB) | Verbaendeanhoerung; Ressortabstimmung |
| Kabinettsentwurf | Hausleitung legt vor | Staatssekretaersausschuss; Kabinettsvorlage |
| Rechtsverordnung | Fachreferat plus ggf. Bundesrat-Zustimmung | RV-Vorlage; ggf. Bundesrat |
| Aenderungsantrag aus der Mitte | Fraktion zusammen mit AA | Bundestagsausschuss |

### Schritt 2 - Begruendungspflichten klaeren

- **Allgemeiner Teil:** Anlass; Zielsetzung; wesentliche Inhalte; Alternativen; Erfuellungsaufwand
 (Buerger; Wirtschaft; Verwaltung); weitere Kosten; KMU-Belange; Nachhaltigkeit; weitere Folgen.
- **Besonderer Teil:** Begruendung je Artikel und Absatz; Bezug zu Kernnormen (GG Art. 32 und Art. 59; WVK; KonsG; PassG; AWG; AWV; EUZBLG; IntZG.).
- Skill-Anschluss: `begruendung-allgemein-und-besonders` und `folgenabschaetzung-erfuellungsaufwand`.

### Schritt 3 - Verbaendeanhoerung nach GGO Paragraf 47

Im Geschaeftsbereich AA sind typische Beteiligte:

- Spitzenverbaende der Materie (siehe `legw-aa-voelkerrecht-und-vertragsgesetzgebung` und folgende)
- Laender (Bundesrat-Spiegel; KOM-Vertreter)
- Wissenschaftliche Sachverstaendige und Beiraete des AA
- EU-Generaldirektion (bei EU-Bezug)
- Bei Eingriff in Grundrechte: Datenschutzkonferenz; Bundesbeauftragte; ggf. EDSA

Anhoerungsfrist regelmaessig vier Wochen; verkuerzte Frist nur mit Begruendung.

### Schritt 4 - Ressortabstimmung und Mitzeichnung

- **Mitzeichnende Ressorts** typisch fuer AA-Vorhaben: BMI (Verwaltung), BMF
 (Haushalt), BMJV (Pruefung Rechtsfoermlichkeit), BMWE (Wirtschaftsbezug), BMDS (Digital);
 weitere ressortabhaengig.
- **Streitschlichtung:** Staatssekretaersrunde; im Ernstfall Chefsache.
- Skill-Anschluss: `verbaendeanhoerung-ressortabstimmung`.

### Schritt 5 - NKR und Erfuellungsaufwand

- **Nationaler Normenkontrollrat:** Stellungnahme nach Paragraf 4 NKRG; Stellungnahme drueckt die
 Berechnung des Erfuellungsaufwands auf Plausibilitaet.
- Skill-Anschluss: `normenkontrollrat-kmu-check` und `legw-rechtsfolgenabschaetzung-leitfaden`.

### Schritt 6 - Kabinettsweg

- Kabinettsvorlage gemaess GGO Paragraf 22 mit Begruendung; Verbaendeauswertung; Ressort-
 abstimmungsergebnis; NKR-Stellungnahme; ggf. Beschlussfassung im Staatssekretaersausschuss.
- Skill-Anschluss: `gesetzesentwurf-kabinett` und `spezial-kabinettsentwuerfe-compliance-dokumentation-und-akte`.

### Schritt 7 - Bundestag und Bundesrat

- **Initiativweg:** Bundesregierung (Art. 76 Abs. 1 GG) oder aus der Mitte (Fraktion).
- **Bundesrat-Beteiligung:** Zustimmungs- oder Einspruchsgesetz; pruefen ueber
 `spezial-bundestag-fristen-form-und-zustaendigkeit` und `gesetzgebungskompetenz-pruefen`.
- **Fachausschuss im Bundestag** (AA-Spiegel).

### Schritt 8 - Aufsicht und Vollzug im Geschaeftsbereich

Nachgeordnete Behoerden des AA im Vollzug einbinden. Vollzugsfolgen pruefen.

## Output

Aufgabenmatrix:

```
Ressort: AA
Vorhabenart: <Eckpunktepapier|Referenten|Kabinett|RV|AendAntrag>
Begruendungspflicht: allgemein und besonders; Aufwand; Nachhaltigkeit; KMU; Alternativen
Verbaende: <Liste>; Frist 4 Wochen
Mitzeichner: <BMF;BMI;BMJV;...>
NKR-Vorlage: ja|nein; Aufwand <Buerger|Wirtschaft|Verwaltung>
Kabinett: ja|nein; Vorlage-Schwerpunkt
Bundesrat: Zustimmung|Einspruch|nicht erforderlich
Fachausschuss BT: AA-Spiegel
Aufsicht/Vollzug: <Behoerde>; Vollzugsfolgen
Naechste Skills: legw-aa-<thema>; normhierarchie-routing
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 7. `legw-ressortaufgaben-bmas`

**Fokus:** Ressortaufgaben BMAS: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Arbeit und Soziales. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmas-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmas (Heranfuehrung).

# Ressortaufgaben BMAS

> Dritter Skill in der Ressort-Kette. Nach `legw-ressort-bmas` (Heranfuehrung) und vor den
> fuenf Spezialfeldern. Bricht die typische Legistik-Aufgabe auf das BMAS herunter.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme` mit Ressort-Eintrag BMAS
- Ressort-Kompass aus `legw-ressort-bmas`
- Geplante Vorhabenart (Gesetz; Rechtsverordnung; Eckpunktepapier; Aenderungsantrag; Vorlage)
- Politische Zielvorgabe (Koalitionsvertrag; Kabinettsbeschluss; Pruefauftrag)

## Vorgehen

### Schritt 1 - Vorhabenart einordnen

| Vorhabenart | Zustaendigkeit im BMAS | Vorlageweg |
|---|---|---|
| Eckpunktepapier | Fachreferat plus Hausleitung | Hausintern; ggf. Ressortbesprechung |
| Referentenentwurf | Fachreferat fuehrt; Hauspruefung (Z; ZA; ZB) | Verbaendeanhoerung; Ressortabstimmung |
| Kabinettsentwurf | Hausleitung legt vor | Staatssekretaersausschuss; Kabinettsvorlage |
| Rechtsverordnung | Fachreferat plus ggf. Bundesrat-Zustimmung | RV-Vorlage; ggf. Bundesrat |
| Aenderungsantrag aus der Mitte | Fraktion zusammen mit BMAS | Bundestagsausschuss |

### Schritt 2 - Begruendungspflichten klaeren

- **Allgemeiner Teil:** Anlass; Zielsetzung; wesentliche Inhalte; Alternativen; Erfuellungsaufwand
 (Buerger; Wirtschaft; Verwaltung); weitere Kosten; KMU-Belange; Nachhaltigkeit; weitere Folgen.
- **Besonderer Teil:** Begruendung je Artikel und Absatz; Bezug zu Kernnormen (ArbZG; TVG; ArbSchG; SGB I bis SGB XII; SGB IX; SGB VI; BetrVG.).
- Skill-Anschluss: `begruendung-allgemein-und-besonders` und `folgenabschaetzung-erfuellungsaufwand`.

### Schritt 3 - Verbaendeanhoerung nach GGO Paragraf 47

Im Geschaeftsbereich BMAS sind typische Beteiligte:

- Spitzenverbaende der Materie (siehe `legw-bmas-arbeitsrecht-und-arbeitsschutz` und folgende)
- Laender (Bundesrat-Spiegel; KOM-Vertreter)
- Wissenschaftliche Sachverstaendige und Beiraete des BMAS
- EU-Generaldirektion (bei EU-Bezug)
- Bei Eingriff in Grundrechte: Datenschutzkonferenz; Bundesbeauftragte; ggf. EDSA

Anhoerungsfrist regelmaessig vier Wochen; verkuerzte Frist nur mit Begruendung.

### Schritt 4 - Ressortabstimmung und Mitzeichnung

- **Mitzeichnende Ressorts** typisch fuer BMAS-Vorhaben: BMI (Verwaltung), BMF
 (Haushalt), BMJV (Pruefung Rechtsfoermlichkeit), BMWE (Wirtschaftsbezug), BMDS (Digital);
 weitere ressortabhaengig.
- **Streitschlichtung:** Staatssekretaersrunde; im Ernstfall Chefsache.
- Skill-Anschluss: `verbaendeanhoerung-ressortabstimmung`.

### Schritt 5 - NKR und Erfuellungsaufwand

- **Nationaler Normenkontrollrat:** Stellungnahme nach Paragraf 4 NKRG; Stellungnahme drueckt die
 Berechnung des Erfuellungsaufwands auf Plausibilitaet.
- Skill-Anschluss: `normenkontrollrat-kmu-check` und `legw-rechtsfolgenabschaetzung-leitfaden`.

### Schritt 6 - Kabinettsweg

- Kabinettsvorlage gemaess GGO Paragraf 22 mit Begruendung; Verbaendeauswertung; Ressort-
 abstimmungsergebnis; NKR-Stellungnahme; ggf. Beschlussfassung im Staatssekretaersausschuss.
- Skill-Anschluss: `gesetzesentwurf-kabinett` und `spezial-kabinettsentwuerfe-compliance-dokumentation-und-akte`.

### Schritt 7 - Bundestag und Bundesrat

- **Initiativweg:** Bundesregierung (Art. 76 Abs. 1 GG) oder aus der Mitte (Fraktion).
- **Bundesrat-Beteiligung:** Zustimmungs- oder Einspruchsgesetz; pruefen ueber
 `spezial-bundestag-fristen-form-und-zustaendigkeit` und `gesetzgebungskompetenz-pruefen`.
- **Fachausschuss im Bundestag** (BMAS-Spiegel).

### Schritt 8 - Aufsicht und Vollzug im Geschaeftsbereich

Nachgeordnete Behoerden des BMAS im Vollzug einbinden. Vollzugsfolgen pruefen.

## Output

Aufgabenmatrix:

```
Ressort: BMAS
Vorhabenart: <Eckpunktepapier|Referenten|Kabinett|RV|AendAntrag>
Begruendungspflicht: allgemein und besonders; Aufwand; Nachhaltigkeit; KMU; Alternativen
Verbaende: <Liste>; Frist 4 Wochen
Mitzeichner: <BMF;BMI;BMJV;...>
NKR-Vorlage: ja|nein; Aufwand <Buerger|Wirtschaft|Verwaltung>
Kabinett: ja|nein; Vorlage-Schwerpunkt
Bundesrat: Zustimmung|Einspruch|nicht erforderlich
Fachausschuss BT: BMAS-Spiegel
Aufsicht/Vollzug: <Behoerde>; Vollzugsfolgen
Naechste Skills: legw-bmas-<thema>; normhierarchie-routing
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 8. `legw-ressortaufgaben-bmbfsfj`

**Fokus:** Ressortaufgaben BMBFSFJ: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Bildung; Familie; Senioren; Frauen und Jugend. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmbfsfj-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmbfsfj (Heranfuehrung).

# Ressortaufgaben BMBFSFJ

> Dritter Skill in der Ressort-Kette. Nach `legw-ressort-bmbfsfj` (Heranfuehrung) und vor den
> fuenf Spezialfeldern. Bricht die typische Legistik-Aufgabe auf das BMBFSFJ herunter.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme` mit Ressort-Eintrag BMBFSFJ
- Ressort-Kompass aus `legw-ressort-bmbfsfj`
- Geplante Vorhabenart (Gesetz; Rechtsverordnung; Eckpunktepapier; Aenderungsantrag; Vorlage)
- Politische Zielvorgabe (Koalitionsvertrag; Kabinettsbeschluss; Pruefauftrag)

## Vorgehen

### Schritt 1 - Vorhabenart einordnen

| Vorhabenart | Zustaendigkeit im BMBFSFJ | Vorlageweg |
|---|---|---|
| Eckpunktepapier | Fachreferat plus Hausleitung | Hausintern; ggf. Ressortbesprechung |
| Referentenentwurf | Fachreferat fuehrt; Hauspruefung (Z; ZA; ZB) | Verbaendeanhoerung; Ressortabstimmung |
| Kabinettsentwurf | Hausleitung legt vor | Staatssekretaersausschuss; Kabinettsvorlage |
| Rechtsverordnung | Fachreferat plus ggf. Bundesrat-Zustimmung | RV-Vorlage; ggf. Bundesrat |
| Aenderungsantrag aus der Mitte | Fraktion zusammen mit BMBFSFJ | Bundestagsausschuss |

### Schritt 2 - Begruendungspflichten klaeren

- **Allgemeiner Teil:** Anlass; Zielsetzung; wesentliche Inhalte; Alternativen; Erfuellungsaufwand
 (Buerger; Wirtschaft; Verwaltung); weitere Kosten; KMU-Belange; Nachhaltigkeit; weitere Folgen.
- **Besonderer Teil:** Begruendung je Artikel und Absatz; Bezug zu Kernnormen (BAfoeG; BBiG; KJHG (SGB VIII); BEEG; UnterhVG; AGG; LFGB; LPartG.).
- Skill-Anschluss: `begruendung-allgemein-und-besonders` und `folgenabschaetzung-erfuellungsaufwand`.

### Schritt 3 - Verbaendeanhoerung nach GGO Paragraf 47

Im Geschaeftsbereich BMBFSFJ sind typische Beteiligte:

- Spitzenverbaende der Materie (siehe `legw-bmbfsfj-schul-und-berufsbildungsrecht` und folgende)
- Laender (Bundesrat-Spiegel; KOM-Vertreter)
- Wissenschaftliche Sachverstaendige und Beiraete des BMBFSFJ
- EU-Generaldirektion (bei EU-Bezug)
- Bei Eingriff in Grundrechte: Datenschutzkonferenz; Bundesbeauftragte; ggf. EDSA

Anhoerungsfrist regelmaessig vier Wochen; verkuerzte Frist nur mit Begruendung.

### Schritt 4 - Ressortabstimmung und Mitzeichnung

- **Mitzeichnende Ressorts** typisch fuer BMBFSFJ-Vorhaben: BMI (Verwaltung), BMF
 (Haushalt), BMJV (Pruefung Rechtsfoermlichkeit), BMWE (Wirtschaftsbezug), BMDS (Digital);
 weitere ressortabhaengig.
- **Streitschlichtung:** Staatssekretaersrunde; im Ernstfall Chefsache.
- Skill-Anschluss: `verbaendeanhoerung-ressortabstimmung`.

### Schritt 5 - NKR und Erfuellungsaufwand

- **Nationaler Normenkontrollrat:** Stellungnahme nach Paragraf 4 NKRG; Stellungnahme drueckt die
 Berechnung des Erfuellungsaufwands auf Plausibilitaet.
- Skill-Anschluss: `normenkontrollrat-kmu-check` und `legw-rechtsfolgenabschaetzung-leitfaden`.

### Schritt 6 - Kabinettsweg

- Kabinettsvorlage gemaess GGO Paragraf 22 mit Begruendung; Verbaendeauswertung; Ressort-
 abstimmungsergebnis; NKR-Stellungnahme; ggf. Beschlussfassung im Staatssekretaersausschuss.
- Skill-Anschluss: `gesetzesentwurf-kabinett` und `spezial-kabinettsentwuerfe-compliance-dokumentation-und-akte`.

### Schritt 7 - Bundestag und Bundesrat

- **Initiativweg:** Bundesregierung (Art. 76 Abs. 1 GG) oder aus der Mitte (Fraktion).
- **Bundesrat-Beteiligung:** Zustimmungs- oder Einspruchsgesetz; pruefen ueber
 `spezial-bundestag-fristen-form-und-zustaendigkeit` und `gesetzgebungskompetenz-pruefen`.
- **Fachausschuss im Bundestag** (BMBFSFJ-Spiegel).

### Schritt 8 - Aufsicht und Vollzug im Geschaeftsbereich

Nachgeordnete Behoerden des BMBFSFJ im Vollzug einbinden. Vollzugsfolgen pruefen.

## Output

Aufgabenmatrix:

```
Ressort: BMBFSFJ
Vorhabenart: <Eckpunktepapier|Referenten|Kabinett|RV|AendAntrag>
Begruendungspflicht: allgemein und besonders; Aufwand; Nachhaltigkeit; KMU; Alternativen
Verbaende: <Liste>; Frist 4 Wochen
Mitzeichner: <BMF;BMI;BMJV;...>
NKR-Vorlage: ja|nein; Aufwand <Buerger|Wirtschaft|Verwaltung>
Kabinett: ja|nein; Vorlage-Schwerpunkt
Bundesrat: Zustimmung|Einspruch|nicht erforderlich
Fachausschuss BT: BMBFSFJ-Spiegel
Aufsicht/Vollzug: <Behoerde>; Vollzugsfolgen
Naechste Skills: legw-bmbfsfj-<thema>; normhierarchie-routing
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
