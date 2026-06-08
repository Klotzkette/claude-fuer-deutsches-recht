---
name: ressortaufgaben-bmleh
description: "Ressortaufgaben BMLEH: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium für Landwirtschaft; Ernaehrung und Heimat. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundestagsweg; Bundesrat-Befassung und nachgeordnete Behörden. Output: Aufgabenmatrix mit Akteuren; Fristen und Pruefpfaden. Anschluss legw-bmleh-Themenslug für Sachfragen und normhierarchie-routing für Normwahl. Abgrenzung zu legw-ressort-bmleh (Heranfuehrung)."
---

# Ressortaufgaben BMLEH

> Dritter Skill in der Ressort-Kette. Nach `legw-ressort-bmleh` (Heranfuehrung) und vor den
> fuenf Spezialfeldern. Bricht die typische Legistik-Aufgabe auf das BMLEH herunter.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme` mit Ressort-Eintrag BMLEH
- Ressort-Kompass aus `legw-ressort-bmleh`
- Geplante Vorhabenart (Gesetz; Rechtsverordnung; Eckpunktepapier; Aenderungsantrag; Vorlage)
- Politische Zielvorgabe (Koalitionsvertrag; Kabinettsbeschluss; Pruefauftrag)

## Vorgehen

### Schritt 1 - Vorhabenart einordnen

| Vorhabenart | Zuständigkeit im BMLEH | Vorlageweg |
|---|---|---|
| Eckpunktepapier | Fachreferat plus Hausleitung | Hausintern; ggf. Ressortbesprechung |
| Referentenentwurf | Fachreferat fuehrt; Hauspruefung (Z; ZA; ZB) | Verbaendeanhoerung; Ressortabstimmung |
| Kabinettsentwurf | Hausleitung legt vor | Staatssekretaersausschuss; Kabinettsvorlage |
| Rechtsverordnung | Fachreferat plus ggf. Bundesrat-Zustimmung | RV-Vorlage; ggf. Bundesrat |
| Aenderungsantrag aus der Mitte | Fraktion zusammen mit BMLEH | Bundestagsausschuss |

### Schritt 2 - Begruendungspflichten klaeren

- **Allgemeiner Teil:** Anlass; Zielsetzung; wesentliche Inhalte; Alternativen; Erfuellungsaufwand
 (Buerger; Wirtschaft; Verwaltung); weitere Kosten; KMU-Belange; Nachhaltigkeit; weitere Folgen.
- **Besonderer Teil:** Begruendung je Artikel und Absatz; Bezug zu Kernnormen (GAKG; TierSchG; LFGB; BWaldG; BJagdG; OeLG; PflSchG; DueV; AgrarZahlG.).
- Skill-Anschluss: `begruendung-allgemein-und-besonders` und `folgenabschaetzung-erfuellungsaufwand`.

### Schritt 3 - Verbaendeanhoerung nach GGO Paragraf 47

Im Geschaeftsbereich BMLEH sind typische Beteiligte:

- Spitzenverbaende der Materie (siehe `legw-bmleh-agrar-und-foerderungsrecht-gak-gap` und folgende)
- Länder (Bundesrat-Spiegel; KOM-Vertreter)
- Wissenschaftliche Sachverstaendige und Beiraete des BMLEH
- EU-Generaldirektion (bei EU-Bezug)
- Bei Eingriff in Grundrechte: Datenschutzkonferenz; Bundesbeauftragte; ggf. EDSA

Anhörungsfrist regelmaessig vier Wochen; verkuerzte Frist nur mit Begruendung.

### Schritt 4 - Ressortabstimmung und Mitzeichnung

- **Mitzeichnende Ressorts** typisch für BMLEH-Vorhaben: BMI (Verwaltung), BMF
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
 `spezial-bundestag-fristen-form-und-zuständigkeit` und `gesetzgebungskompetenz-pruefen`.
- **Fachausschuss im Bundestag** (BMLEH-Spiegel).

### Schritt 8 - Aufsicht und Vollzug im Geschaeftsbereich

Nachgeordnete Behörden des BMLEH im Vollzug einbinden. Vollzugsfolgen pruefen.

## Normenanker

Arbeitsfokus: **Ressortaufgaben BMLEH**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Output

Aufgabenmatrix:

```
Ressort: BMLEH
Vorhabenart: <Eckpunktepapier|Referenten|Kabinett|RV|AendAntrag>
Begruendungspflicht: allgemein und besonders; Aufwand; Nachhaltigkeit; KMU; Alternativen
Verbaende: <Liste>; Frist 4 Wochen
Mitzeichner: <BMF;BMI;BMJV;...>
NKR-Vorlage: ja|nein; Aufwand <Buerger|Wirtschaft|Verwaltung>
Kabinett: ja|nein; Vorlage-Schwerpunkt
Bundesrat: Zustimmung|Einspruch|nicht erforderlich
Fachausschuss BT: BMLEH-Spiegel
Aufsicht/Vollzug: <Behörde>; Vollzugsfolgen
Naechste Skills: legw-bmleh-<thema>; normhierarchie-routing
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis für den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
