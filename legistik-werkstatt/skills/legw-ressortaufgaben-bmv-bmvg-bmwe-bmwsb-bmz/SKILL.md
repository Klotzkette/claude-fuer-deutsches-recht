---
name: legw-ressortaufgaben-bmv-bmvg-bmwe-bmwsb-bmz
description: "Legw Ressortaufgaben BMV Bmvg Bmwe Bmwsb BMZ: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Legw Ressortaufgaben BMV Bmvg Bmwe Bmwsb BMZ

## Arbeitsbereich

Dieser Skill bündelt 8 sachlich verwandte Arbeitsschritte rund um **Legw Ressortaufgaben BMV Bmvg Bmwe Bmwsb BMZ** im Plugin Legistik-Werkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `legw-ressortaufgaben-bmv` | Ressortaufgaben BMV: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Verkehr. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmv-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmv (Heranfuehrung). |
| `legw-ressortaufgaben-bmvg` | Ressortaufgaben BMVg: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium der Verteidigung. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmvg-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmvg (Heranfuehrung). |
| `legw-ressortaufgaben-bmwe` | Ressortaufgaben BMWE: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Wirtschaft und Energie. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmwe-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmwe (Heranfuehrung). |
| `legw-ressortaufgaben-bmwsb` | Ressortaufgaben BMWSB: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Wohnen; Stadtentwicklung und Bauwesen. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmwsb-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmwsb (Heranfuehrung). |
| `legw-ressortaufgaben-bmz` | Ressortaufgaben BMZ: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer wirtschaftliche Zusammenarbeit und Entwicklung. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmz-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmz (Heranfuehrung). |
| `legw-rmap-anschluss-an-legw` | Brueckenskill: Wie verzahnt sich die Rulemap-Arbeit mit der uebrigen Legistik-Werkstatt (Auftragsaufnahme; Ressort-Router; Heranfuehrung; Ressortaufgaben; Sachfeld-Spezialfelder; normhierarchie-routing; verfassungsmaessigkeit-quercheck; europarechtskonformitaet; folgenabschaetzung). Output Kettenpfad mit Eingaben; Ausgaben; Verantwortlichkeiten je Stufe. Abgrenzung zur fachlichen Modellierung selbst; hier wird die Werkstattkette beschrieben. |
| `legw-rmap-bestimmtheit-und-justitiabilitaet` | Verfassungsrechtliche Pruefung: hat die Rulemap-Modellierung die Bestimmtheit der Norm erhoeht (gut) oder unzulaessig verkuerzt (schlecht)? Justitiabilitaet und Begruendungspflicht im Verwaltungsverfahren. Output Bestimmtheits- und Justitiabilitaetsbericht mit Empfehlungen. Anschluss verfassungsmaessigkeit-quercheck und legw-rmap-vollzugstauglichkeit. Abgrenzung zur reinen Norminhalt-Pruefung; hier geht es um die Wechselwirkung Text und Logikmodell. |
| `legw-rmap-entscheidungsbaum-validierung` | Simulation und Verifikation der Rulemap: Faelle generieren; Pfadabdeckung messen; Soll-Ist-Vergleich gegen juristische Erwartung. Werkzeuge im Rulemap Builder: Capture; Simulate; Verify. Output Validierungsprotokoll mit Pfaddeckung; Trefferquote; offenen Punkten. Anschluss legw-rmap-bestimmtheit-und-justitiabilitaet fuer rechtliche Bewertung der Pfade. Abgrenzung zur klassischen Beweiswuerdigung im Einzelfall. |

## Arbeitsweg

Im Plugin Legistik-Werkstatt gilt für **Legw Ressortaufgaben BMV Bmvg Bmwe Bmwsb BMZ**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `legw-ressortaufgaben-bmv`

**Fokus:** Ressortaufgaben BMV: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Verkehr. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmv-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmv (Heranfuehrung).

# Ressortaufgaben BMV

> Dritter Skill in der Ressort-Kette. Nach `legw-ressort-bmv` (Heranfuehrung) und vor den
> fuenf Spezialfeldern. Bricht die typische Legistik-Aufgabe auf das BMV herunter.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme` mit Ressort-Eintrag BMV
- Ressort-Kompass aus `legw-ressort-bmv`
- Geplante Vorhabenart (Gesetz; Rechtsverordnung; Eckpunktepapier; Aenderungsantrag; Vorlage)
- Politische Zielvorgabe (Koalitionsvertrag; Kabinettsbeschluss; Pruefauftrag)

## Vorgehen

### Schritt 1 - Vorhabenart einordnen

| Vorhabenart | Zustaendigkeit im BMV | Vorlageweg |
|---|---|---|
| Eckpunktepapier | Fachreferat plus Hausleitung | Hausintern; ggf. Ressortbesprechung |
| Referentenentwurf | Fachreferat fuehrt; Hauspruefung (Z; ZA; ZB) | Verbaendeanhoerung; Ressortabstimmung |
| Kabinettsentwurf | Hausleitung legt vor | Staatssekretaersausschuss; Kabinettsvorlage |
| Rechtsverordnung | Fachreferat plus ggf. Bundesrat-Zustimmung | RV-Vorlage; ggf. Bundesrat |
| Aenderungsantrag aus der Mitte | Fraktion zusammen mit BMV | Bundestagsausschuss |

### Schritt 2 - Begruendungspflichten klaeren

- **Allgemeiner Teil:** Anlass; Zielsetzung; wesentliche Inhalte; Alternativen; Erfuellungsaufwand
 (Buerger; Wirtschaft; Verwaltung); weitere Kosten; KMU-Belange; Nachhaltigkeit; weitere Folgen.
- **Besonderer Teil:** Begruendung je Artikel und Absatz; Bezug zu Kernnormen (StVG; StVO; FeV; AEG; ERegG; LuftVG; SeeAufgG; BinSchG; PBefG.).
- Skill-Anschluss: `begruendung-allgemein-und-besonders` und `folgenabschaetzung-erfuellungsaufwand`.

### Schritt 3 - Verbaendeanhoerung nach GGO Paragraf 47

Im Geschaeftsbereich BMV sind typische Beteiligte:

- Spitzenverbaende der Materie (siehe `legw-bmv-strassenverkehrsrecht-und-stvg-stvo` und folgende)
- Laender (Bundesrat-Spiegel; KOM-Vertreter)
- Wissenschaftliche Sachverstaendige und Beiraete des BMV
- EU-Generaldirektion (bei EU-Bezug)
- Bei Eingriff in Grundrechte: Datenschutzkonferenz; Bundesbeauftragte; ggf. EDSA

Anhoerungsfrist regelmaessig vier Wochen; verkuerzte Frist nur mit Begruendung.

### Schritt 4 - Ressortabstimmung und Mitzeichnung

- **Mitzeichnende Ressorts** typisch fuer BMV-Vorhaben: BMI (Verwaltung), BMF
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
- **Fachausschuss im Bundestag** (BMV-Spiegel).

### Schritt 8 - Aufsicht und Vollzug im Geschaeftsbereich

Nachgeordnete Behoerden des BMV im Vollzug einbinden. Vollzugsfolgen pruefen.

## Output

Aufgabenmatrix:

```
Ressort: BMV
Vorhabenart: <Eckpunktepapier|Referenten|Kabinett|RV|AendAntrag>
Begruendungspflicht: allgemein und besonders; Aufwand; Nachhaltigkeit; KMU; Alternativen
Verbaende: <Liste>; Frist 4 Wochen
Mitzeichner: <BMF;BMI;BMJV;...>
NKR-Vorlage: ja|nein; Aufwand <Buerger|Wirtschaft|Verwaltung>
Kabinett: ja|nein; Vorlage-Schwerpunkt
Bundesrat: Zustimmung|Einspruch|nicht erforderlich
Fachausschuss BT: BMV-Spiegel
Aufsicht/Vollzug: <Behoerde>; Vollzugsfolgen
Naechste Skills: legw-bmv-<thema>; normhierarchie-routing
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 2. `legw-ressortaufgaben-bmvg`

**Fokus:** Ressortaufgaben BMVg: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium der Verteidigung. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmvg-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmvg (Heranfuehrung).

# Ressortaufgaben BMVg

> Dritter Skill in der Ressort-Kette. Nach `legw-ressort-bmvg` (Heranfuehrung) und vor den
> fuenf Spezialfeldern. Bricht die typische Legistik-Aufgabe auf das BMVg herunter.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme` mit Ressort-Eintrag BMVg
- Ressort-Kompass aus `legw-ressort-bmvg`
- Geplante Vorhabenart (Gesetz; Rechtsverordnung; Eckpunktepapier; Aenderungsantrag; Vorlage)
- Politische Zielvorgabe (Koalitionsvertrag; Kabinettsbeschluss; Pruefauftrag)

## Vorgehen

### Schritt 1 - Vorhabenart einordnen

| Vorhabenart | Zustaendigkeit im BMVg | Vorlageweg |
|---|---|---|
| Eckpunktepapier | Fachreferat plus Hausleitung | Hausintern; ggf. Ressortbesprechung |
| Referentenentwurf | Fachreferat fuehrt; Hauspruefung (Z; ZA; ZB) | Verbaendeanhoerung; Ressortabstimmung |
| Kabinettsentwurf | Hausleitung legt vor | Staatssekretaersausschuss; Kabinettsvorlage |
| Rechtsverordnung | Fachreferat plus ggf. Bundesrat-Zustimmung | RV-Vorlage; ggf. Bundesrat |
| Aenderungsantrag aus der Mitte | Fraktion zusammen mit BMVg | Bundestagsausschuss |

### Schritt 2 - Begruendungspflichten klaeren

- **Allgemeiner Teil:** Anlass; Zielsetzung; wesentliche Inhalte; Alternativen; Erfuellungsaufwand
 (Buerger; Wirtschaft; Verwaltung); weitere Kosten; KMU-Belange; Nachhaltigkeit; weitere Folgen.
- **Besonderer Teil:** Begruendung je Artikel und Absatz; Bezug zu Kernnormen (SG; WStG; UZwGBw; BwBeschG; NATO-Truppenstatut; AWG; KrWaffKG; ResG.).
- Skill-Anschluss: `begruendung-allgemein-und-besonders` und `folgenabschaetzung-erfuellungsaufwand`.

### Schritt 3 - Verbaendeanhoerung nach GGO Paragraf 47

Im Geschaeftsbereich BMVg sind typische Beteiligte:

- Spitzenverbaende der Materie (siehe `legw-bmvg-wehrrecht-und-soldatenstatus` und folgende)
- Laender (Bundesrat-Spiegel; KOM-Vertreter)
- Wissenschaftliche Sachverstaendige und Beiraete des BMVg
- EU-Generaldirektion (bei EU-Bezug)
- Bei Eingriff in Grundrechte: Datenschutzkonferenz; Bundesbeauftragte; ggf. EDSA

Anhoerungsfrist regelmaessig vier Wochen; verkuerzte Frist nur mit Begruendung.

### Schritt 4 - Ressortabstimmung und Mitzeichnung

- **Mitzeichnende Ressorts** typisch fuer BMVg-Vorhaben: BMI (Verwaltung), BMF
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
- **Fachausschuss im Bundestag** (BMVg-Spiegel).

### Schritt 8 - Aufsicht und Vollzug im Geschaeftsbereich

Nachgeordnete Behoerden des BMVg im Vollzug einbinden. Vollzugsfolgen pruefen.

## Output

Aufgabenmatrix:

```
Ressort: BMVg
Vorhabenart: <Eckpunktepapier|Referenten|Kabinett|RV|AendAntrag>
Begruendungspflicht: allgemein und besonders; Aufwand; Nachhaltigkeit; KMU; Alternativen
Verbaende: <Liste>; Frist 4 Wochen
Mitzeichner: <BMF;BMI;BMJV;...>
NKR-Vorlage: ja|nein; Aufwand <Buerger|Wirtschaft|Verwaltung>
Kabinett: ja|nein; Vorlage-Schwerpunkt
Bundesrat: Zustimmung|Einspruch|nicht erforderlich
Fachausschuss BT: BMVg-Spiegel
Aufsicht/Vollzug: <Behoerde>; Vollzugsfolgen
Naechste Skills: legw-bmvg-<thema>; normhierarchie-routing
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 3. `legw-ressortaufgaben-bmwe`

**Fokus:** Ressortaufgaben BMWE: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Wirtschaft und Energie. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmwe-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmwe (Heranfuehrung).

# Ressortaufgaben BMWE

> Dritter Skill in der Ressort-Kette. Nach `legw-ressort-bmwe` (Heranfuehrung) und vor den
> fuenf Spezialfeldern. Bricht die typische Legistik-Aufgabe auf das BMWE herunter.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme` mit Ressort-Eintrag BMWE
- Ressort-Kompass aus `legw-ressort-bmwe`
- Geplante Vorhabenart (Gesetz; Rechtsverordnung; Eckpunktepapier; Aenderungsantrag; Vorlage)
- Politische Zielvorgabe (Koalitionsvertrag; Kabinettsbeschluss; Pruefauftrag)

## Vorgehen

### Schritt 1 - Vorhabenart einordnen

| Vorhabenart | Zustaendigkeit im BMWE | Vorlageweg |
|---|---|---|
| Eckpunktepapier | Fachreferat plus Hausleitung | Hausintern; ggf. Ressortbesprechung |
| Referentenentwurf | Fachreferat fuehrt; Hauspruefung (Z; ZA; ZB) | Verbaendeanhoerung; Ressortabstimmung |
| Kabinettsentwurf | Hausleitung legt vor | Staatssekretaersausschuss; Kabinettsvorlage |
| Rechtsverordnung | Fachreferat plus ggf. Bundesrat-Zustimmung | RV-Vorlage; ggf. Bundesrat |
| Aenderungsantrag aus der Mitte | Fraktion zusammen mit BMWE | Bundestagsausschuss |

### Schritt 2 - Begruendungspflichten klaeren

- **Allgemeiner Teil:** Anlass; Zielsetzung; wesentliche Inhalte; Alternativen; Erfuellungsaufwand
 (Buerger; Wirtschaft; Verwaltung); weitere Kosten; KMU-Belange; Nachhaltigkeit; weitere Folgen.
- **Besonderer Teil:** Begruendung je Artikel und Absatz; Bezug zu Kernnormen (EnWG; EEG; WindBG; KWKG; BEHG; AWG; AWV; GWB; UStG; ARegV.).
- Skill-Anschluss: `begruendung-allgemein-und-besonders` und `folgenabschaetzung-erfuellungsaufwand`.

### Schritt 3 - Verbaendeanhoerung nach GGO Paragraf 47

Im Geschaeftsbereich BMWE sind typische Beteiligte:

- Spitzenverbaende der Materie (siehe `legw-bmwe-energie-und-netzregulierung-enwg` und folgende)
- Laender (Bundesrat-Spiegel; KOM-Vertreter)
- Wissenschaftliche Sachverstaendige und Beiraete des BMWE
- EU-Generaldirektion (bei EU-Bezug)
- Bei Eingriff in Grundrechte: Datenschutzkonferenz; Bundesbeauftragte; ggf. EDSA

Anhoerungsfrist regelmaessig vier Wochen; verkuerzte Frist nur mit Begruendung.

### Schritt 4 - Ressortabstimmung und Mitzeichnung

- **Mitzeichnende Ressorts** typisch fuer BMWE-Vorhaben: BMI (Verwaltung), BMF
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
- **Fachausschuss im Bundestag** (BMWE-Spiegel).

### Schritt 8 - Aufsicht und Vollzug im Geschaeftsbereich

Nachgeordnete Behoerden des BMWE im Vollzug einbinden. Vollzugsfolgen pruefen.

## Output

Aufgabenmatrix:

```
Ressort: BMWE
Vorhabenart: <Eckpunktepapier|Referenten|Kabinett|RV|AendAntrag>
Begruendungspflicht: allgemein und besonders; Aufwand; Nachhaltigkeit; KMU; Alternativen
Verbaende: <Liste>; Frist 4 Wochen
Mitzeichner: <BMF;BMI;BMJV;...>
NKR-Vorlage: ja|nein; Aufwand <Buerger|Wirtschaft|Verwaltung>
Kabinett: ja|nein; Vorlage-Schwerpunkt
Bundesrat: Zustimmung|Einspruch|nicht erforderlich
Fachausschuss BT: BMWE-Spiegel
Aufsicht/Vollzug: <Behoerde>; Vollzugsfolgen
Naechste Skills: legw-bmwe-<thema>; normhierarchie-routing
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 4. `legw-ressortaufgaben-bmwsb`

**Fokus:** Ressortaufgaben BMWSB: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Wohnen; Stadtentwicklung und Bauwesen. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmwsb-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmwsb (Heranfuehrung).

# Ressortaufgaben BMWSB

> Dritter Skill in der Ressort-Kette. Nach `legw-ressort-bmwsb` (Heranfuehrung) und vor den
> fuenf Spezialfeldern. Bricht die typische Legistik-Aufgabe auf das BMWSB herunter.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme` mit Ressort-Eintrag BMWSB
- Ressort-Kompass aus `legw-ressort-bmwsb`
- Geplante Vorhabenart (Gesetz; Rechtsverordnung; Eckpunktepapier; Aenderungsantrag; Vorlage)
- Politische Zielvorgabe (Koalitionsvertrag; Kabinettsbeschluss; Pruefauftrag)

## Vorgehen

### Schritt 1 - Vorhabenart einordnen

| Vorhabenart | Zustaendigkeit im BMWSB | Vorlageweg |
|---|---|---|
| Eckpunktepapier | Fachreferat plus Hausleitung | Hausintern; ggf. Ressortbesprechung |
| Referentenentwurf | Fachreferat fuehrt; Hauspruefung (Z; ZA; ZB) | Verbaendeanhoerung; Ressortabstimmung |
| Kabinettsentwurf | Hausleitung legt vor | Staatssekretaersausschuss; Kabinettsvorlage |
| Rechtsverordnung | Fachreferat plus ggf. Bundesrat-Zustimmung | RV-Vorlage; ggf. Bundesrat |
| Aenderungsantrag aus der Mitte | Fraktion zusammen mit BMWSB | Bundestagsausschuss |

### Schritt 2 - Begruendungspflichten klaeren

- **Allgemeiner Teil:** Anlass; Zielsetzung; wesentliche Inhalte; Alternativen; Erfuellungsaufwand
 (Buerger; Wirtschaft; Verwaltung); weitere Kosten; KMU-Belange; Nachhaltigkeit; weitere Folgen.
- **Besonderer Teil:** Begruendung je Artikel und Absatz; Bezug zu Kernnormen (BauGB; BauNVO; BGB Mietrecht; StaedtebauFoerdG; BauPG; BauPVO; GEG; WoFG.).
- Skill-Anschluss: `begruendung-allgemein-und-besonders` und `folgenabschaetzung-erfuellungsaufwand`.

### Schritt 3 - Verbaendeanhoerung nach GGO Paragraf 47

Im Geschaeftsbereich BMWSB sind typische Beteiligte:

- Spitzenverbaende der Materie (siehe `legw-bmwsb-bau-und-planungsrecht-baugb-baunvo` und folgende)
- Laender (Bundesrat-Spiegel; KOM-Vertreter)
- Wissenschaftliche Sachverstaendige und Beiraete des BMWSB
- EU-Generaldirektion (bei EU-Bezug)
- Bei Eingriff in Grundrechte: Datenschutzkonferenz; Bundesbeauftragte; ggf. EDSA

Anhoerungsfrist regelmaessig vier Wochen; verkuerzte Frist nur mit Begruendung.

### Schritt 4 - Ressortabstimmung und Mitzeichnung

- **Mitzeichnende Ressorts** typisch fuer BMWSB-Vorhaben: BMI (Verwaltung), BMF
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
- **Fachausschuss im Bundestag** (BMWSB-Spiegel).

### Schritt 8 - Aufsicht und Vollzug im Geschaeftsbereich

Nachgeordnete Behoerden des BMWSB im Vollzug einbinden. Vollzugsfolgen pruefen.

## Output

Aufgabenmatrix:

```
Ressort: BMWSB
Vorhabenart: <Eckpunktepapier|Referenten|Kabinett|RV|AendAntrag>
Begruendungspflicht: allgemein und besonders; Aufwand; Nachhaltigkeit; KMU; Alternativen
Verbaende: <Liste>; Frist 4 Wochen
Mitzeichner: <BMF;BMI;BMJV;...>
NKR-Vorlage: ja|nein; Aufwand <Buerger|Wirtschaft|Verwaltung>
Kabinett: ja|nein; Vorlage-Schwerpunkt
Bundesrat: Zustimmung|Einspruch|nicht erforderlich
Fachausschuss BT: BMWSB-Spiegel
Aufsicht/Vollzug: <Behoerde>; Vollzugsfolgen
Naechste Skills: legw-bmwsb-<thema>; normhierarchie-routing
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 5. `legw-ressortaufgaben-bmz`

**Fokus:** Ressortaufgaben BMZ: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer wirtschaftliche Zusammenarbeit und Entwicklung. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmz-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmz (Heranfuehrung).

# Ressortaufgaben BMZ

> Dritter Skill in der Ressort-Kette. Nach `legw-ressort-bmz` (Heranfuehrung) und vor den
> fuenf Spezialfeldern. Bricht die typische Legistik-Aufgabe auf das BMZ herunter.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme` mit Ressort-Eintrag BMZ
- Ressort-Kompass aus `legw-ressort-bmz`
- Geplante Vorhabenart (Gesetz; Rechtsverordnung; Eckpunktepapier; Aenderungsantrag; Vorlage)
- Politische Zielvorgabe (Koalitionsvertrag; Kabinettsbeschluss; Pruefauftrag)

## Vorgehen

### Schritt 1 - Vorhabenart einordnen

| Vorhabenart | Zustaendigkeit im BMZ | Vorlageweg |
|---|---|---|
| Eckpunktepapier | Fachreferat plus Hausleitung | Hausintern; ggf. Ressortbesprechung |
| Referentenentwurf | Fachreferat fuehrt; Hauspruefung (Z; ZA; ZB) | Verbaendeanhoerung; Ressortabstimmung |
| Kabinettsentwurf | Hausleitung legt vor | Staatssekretaersausschuss; Kabinettsvorlage |
| Rechtsverordnung | Fachreferat plus ggf. Bundesrat-Zustimmung | RV-Vorlage; ggf. Bundesrat |
| Aenderungsantrag aus der Mitte | Fraktion zusammen mit BMZ | Bundestagsausschuss |

### Schritt 2 - Begruendungspflichten klaeren

- **Allgemeiner Teil:** Anlass; Zielsetzung; wesentliche Inhalte; Alternativen; Erfuellungsaufwand
 (Buerger; Wirtschaft; Verwaltung); weitere Kosten; KMU-Belange; Nachhaltigkeit; weitere Folgen.
- **Besonderer Teil:** Begruendung je Artikel und Absatz; Bezug zu Kernnormen (Bilaterale Abkommen; LkSG; KSG; Pariser Abkommen (BGBl); EUZBLG; HBKG.).
- Skill-Anschluss: `begruendung-allgemein-und-besonders` und `folgenabschaetzung-erfuellungsaufwand`.

### Schritt 3 - Verbaendeanhoerung nach GGO Paragraf 47

Im Geschaeftsbereich BMZ sind typische Beteiligte:

- Spitzenverbaende der Materie (siehe `legw-bmz-entwicklungszusammenarbeit-und-bilaterale-abkommen` und folgende)
- Laender (Bundesrat-Spiegel; KOM-Vertreter)
- Wissenschaftliche Sachverstaendige und Beiraete des BMZ
- EU-Generaldirektion (bei EU-Bezug)
- Bei Eingriff in Grundrechte: Datenschutzkonferenz; Bundesbeauftragte; ggf. EDSA

Anhoerungsfrist regelmaessig vier Wochen; verkuerzte Frist nur mit Begruendung.

### Schritt 4 - Ressortabstimmung und Mitzeichnung

- **Mitzeichnende Ressorts** typisch fuer BMZ-Vorhaben: BMI (Verwaltung), BMF
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
- **Fachausschuss im Bundestag** (BMZ-Spiegel).

### Schritt 8 - Aufsicht und Vollzug im Geschaeftsbereich

Nachgeordnete Behoerden des BMZ im Vollzug einbinden. Vollzugsfolgen pruefen.

## Output

Aufgabenmatrix:

```
Ressort: BMZ
Vorhabenart: <Eckpunktepapier|Referenten|Kabinett|RV|AendAntrag>
Begruendungspflicht: allgemein und besonders; Aufwand; Nachhaltigkeit; KMU; Alternativen
Verbaende: <Liste>; Frist 4 Wochen
Mitzeichner: <BMF;BMI;BMJV;...>
NKR-Vorlage: ja|nein; Aufwand <Buerger|Wirtschaft|Verwaltung>
Kabinett: ja|nein; Vorlage-Schwerpunkt
Bundesrat: Zustimmung|Einspruch|nicht erforderlich
Fachausschuss BT: BMZ-Spiegel
Aufsicht/Vollzug: <Behoerde>; Vollzugsfolgen
Naechste Skills: legw-bmz-<thema>; normhierarchie-routing
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 6. `legw-rmap-anschluss-an-legw`

**Fokus:** Brueckenskill: Wie verzahnt sich die Rulemap-Arbeit mit der uebrigen Legistik-Werkstatt (Auftragsaufnahme; Ressort-Router; Heranfuehrung; Ressortaufgaben; Sachfeld-Spezialfelder; normhierarchie-routing; verfassungsmaessigkeit-quercheck; europarechtskonformitaet; folgenabschaetzung). Output Kettenpfad mit Eingaben; Ausgaben; Verantwortlichkeiten je Stufe. Abgrenzung zur fachlichen Modellierung selbst; hier wird die Werkstattkette beschrieben.

# Anschluss der Rulemap-Arbeit an die Legistik-Werkstatt

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Auftragsblatt aus legistik-auftragsaufnahme
- Ergebnis aus legw-ressort-router
- Sachfeld-Kompass aus legw-<ressort>-<thema>

## Kern der Methode

Die Rulemap-Skills bilden eine eigene Subkette; sie werden nach der Ressort- und Sachfeld-Klaerung in das Werkstatt-eingehaengt. Die Quercheckskills (verfassungsmaessigkeit; europarechtskonformitaet) wirken weiter; die rmap-Skills liefern zusaetzlich die maschinenlesbare Fassung.

## Vorgehen

1. Auftragsblatt um Rulemap-Erfordernis ergaenzen
2. Nach Sachfeld-Kompass legw-rmap-grundlagen anstossen
3. Vorgehensmodell aus legw-rmap-norm-zu-rulemap durchlaufen
4. Quercheckskills (verfassungs- und europarechtlich) parallel arbeiten lassen
5. Rulemap mit Begruendung; NKR-Bericht und Vollzugsplan zusammenfuehren
6. Akte schliessen; Builder-Export ablegen

## Pruefpunkte

Pruefen: ist die Werkstattkette vollstaendig durchlaufen? Sind Querprueferei und Rulemap-Erstellung sauber verzahnt? Liegt am Ende ein Aktenstand mit Text- und Logikfassung der Norm vor?

## Output

```
Skill: legw-rmap-anschluss-an-legw
Thema: Anschluss der Rulemap-Arbeit an die Legistik-Werkstatt
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.

## 7. `legw-rmap-bestimmtheit-und-justitiabilitaet`

**Fokus:** Verfassungsrechtliche Pruefung: hat die Rulemap-Modellierung die Bestimmtheit der Norm erhoeht (gut) oder unzulaessig verkuerzt (schlecht)? Justitiabilitaet und Begruendungspflicht im Verwaltungsverfahren. Output Bestimmtheits- und Justitiabilitaetsbericht mit Empfehlungen. Anschluss verfassungsmaessigkeit-quercheck und legw-rmap-vollzugstauglichkeit. Abgrenzung zur reinen Norminhalt-Pruefung; hier geht es um die Wechselwirkung Text und Logikmodell.

# Bestimmtheit und Justitiabilitaet bei Rulemap-Normen

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Rulemap (Block 5 Schritte 1 bis 5)
- Verfassungsrechtliche Pruefskizze aus verfassungsmaessigkeit-quercheck

## Kern der Methode

Bestimmtheitsgebot (Art. 20 Abs. 3 GG und einschlaegige Spezialvorbehalte) verlangt klare Tatbestaende und vorhersehbare Rechtsfolgen. Eine Rulemap zwingt zur Explizitheit und erhoeht regelmaessig die Bestimmtheit; sie darf jedoch unbestimmte Rechtsbegriffe nicht durch verdeckte Schwellenwerte ersetzen. Justitiabilitaet: jede automatisierte Entscheidung muss begruendbar und ueberpruefbar sein.

## Vorgehen

1. Jede unbestimmte Rechtsbegriff-Stelle in der Rulemap markieren
2. Pruefen: Konkretisierung gerechtfertigt oder unzulaessige Verschiebung
3. Justitiabilitaet jeder Rechtsfolge sichern (Bescheid mit Begruendung)
4. Begruendungspflicht und Akteneinsicht modellieren
5. Bericht fuer NKR und Justitiariat erstellen

## Pruefpunkte

Pruefen: bleibt der Beurteilungs- oder Ermessensspielraum der Verwaltung erhalten? Sind automatisierte Entscheidungen vor Gericht reproduzierbar? Greifen Datenschutz-Vorgaben (Art. 22 DSGVO; vollautomatisierte Entscheidung)?

## Output

```
Skill: legw-rmap-bestimmtheit-und-justitiabilitaet
Thema: Bestimmtheit und Justitiabilitaet bei Rulemap-Normen
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.

## 8. `legw-rmap-entscheidungsbaum-validierung`

**Fokus:** Simulation und Verifikation der Rulemap: Faelle generieren; Pfadabdeckung messen; Soll-Ist-Vergleich gegen juristische Erwartung. Werkzeuge im Rulemap Builder: Capture; Simulate; Verify. Output Validierungsprotokoll mit Pfaddeckung; Trefferquote; offenen Punkten. Anschluss legw-rmap-bestimmtheit-und-justitiabilitaet fuer rechtliche Bewertung der Pfade. Abgrenzung zur klassischen Beweiswuerdigung im Einzelfall.

# Entscheidungsbaum-Simulation und Verifikation

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Vollstaendige Rulemap (Knoten; Verweisungen; Ausnahmen)
- Fallkatalog (realistische Sachverhalte und Grenzfaelle)

## Kern der Methode

Validierung ueber drei Achsen: Vollstaendigkeit (jeder Pfad erreichbar); Konsistenz (keine widerspruechlichen Pfade); Korrektheit (juristisch korrekte Ergebnisse). Im Builder werden Faelle simuliert und Entscheidungen automatisch verifiziert.

## Vorgehen

1. Fallkatalog mit realistischen und Grenzfallszenarien aufbauen
2. Simulation laufen lassen; Pfadabdeckung messen
3. Verifikation: jeden Pfad gegen juristische Soll-Antwort spiegeln
4. Abweichungen aufnehmen; in legw-rmap-tatbestand-und-rechtsfolge zurueckspielen
5. Validierungsprotokoll fuer Akte und NKR ablegen

## Pruefpunkte

Pruefen: ist jeder Pfad mindestens einmal gepruefte? Sind systematisch Grenz- und Ausnahmefaelle erfasst? Sind die juristischen Soll-Antworten autorisiert (durch Fachreferat oder externe Begutachtung)?

## Output

```
Skill: legw-rmap-entscheidungsbaum-validierung
Thema: Entscheidungsbaum-Simulation und Verifikation
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.
