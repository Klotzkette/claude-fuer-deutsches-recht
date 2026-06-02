---
name: legw-ressortaufgaben-bmwe
description: "Ressortaufgaben BMWE: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Wirtschaft und Energie. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behoerden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmwe-Themenslug fuer Sachfragen und normhierarchie-routing fuer Normwahl. Abgrenzung zu legw-ressort-bmwe (Heranfuehrung)."
---

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
Ressort:              BMWE
Vorhabenart:          <Eckpunktepapier|Referenten|Kabinett|RV|AendAntrag>
Begruendungspflicht:  allgemein und besonders; Aufwand; Nachhaltigkeit; KMU; Alternativen
Verbaende:            <Liste>; Frist 4 Wochen
Mitzeichner:          <BMF;BMI;BMJV;...>
NKR-Vorlage:          ja|nein; Aufwand <Buerger|Wirtschaft|Verwaltung>
Kabinett:             ja|nein; Vorlage-Schwerpunkt
Bundesrat:            Zustimmung|Einspruch|nicht erforderlich
Fachausschuss BT:     BMWE-Spiegel
Aufsicht/Vollzug:     <Behoerde>; Vollzugsfolgen
Naechste Skills:      legw-bmwe-<thema>; normhierarchie-routing
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
