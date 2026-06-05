---
name: legw-ressort-verbaendeanhoerung
description: "Legw Ressort Verbaendeanhoerung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Legw Ressort Verbaendeanhoerung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Legw Ressort Verbaendeanhoerung** im Plugin Legistik Werkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `legw-ressort-bmf` | Heranfuehrung Ressort BMF (Bundesministerium der Finanzen). Schwerpunkt: Steuer- und Fiskalrecht; Haushalts- und Zuwendungsrecht; Finanzmarkt; Zoll und Aussenwirtschaft; Geldwaesche. Kernnormen: AO; EStG; KStG; UStG; BHO; FinStabG; KWG; WpHG; ZollVG; GwG. Fuenf Spezialfelder: steuerrecht-und-fiskalnormen; haushalts-und-zuwendungsrecht; finanzmarktaufsicht-bafin-kwg-wpig; zoll-und-aussenwirtschaftsrecht; geldwaesche-und-sanktionsrecht. Output: Ressort-Kompass mit Materie; Akteuren; Normbestand; Aufsicht und Stolpersteinen. Anschluss legw-ressortaufgaben-bmf und legw-bmf-Themenslug. |
| `verbaendeanhoerung-ressortabstimmung` | Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten. Anwendungsfall Referentenentwurf ist fertig und muss Verbaenden und Ressorts zugeleitet werden vor Kabinettsbefassung. Anschreiben Liste zu beteiligender Verbaende Ressorts Fristsetzung drei bis sechs Wochen. Auswertung Stellungnahmen zustimmend kritisch ablehnend mit konkreten Aenderungsvorschlaegen. Eigene Stellungnahme je kritischer Position Aenderungen dokumentiert. Output Auswertungsmatrix geaenderter Entwurf bereit für Kabinett. Abgrenzung zu begründung-allgemein-und-besonders inhaltliche Begründung. |
| `begruendung-allgemein-und-besonders` | Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder Kabinettsentwurf ist fertig und Begründung muss nach HdR-Schema aufgebaut werden. Allgemeiner Teil A Anlass und Ziel B wesentlicher Inhalt C Alternativen D Erfuellungsaufwand E weitere Kosten F weitere Folgen. Besonderer Teil Erlaeuterung je geaendertem Paragrafen was geaendert wird warum wie es zu verstehen ist absehbare Auslegungsfragen Bezug BVerfG BVerwG BGH BSG BFH BAG EuGH-Rechtsprechung. Output vollständige Begründung. Anschluss synopse-erstellen xml-paralleldarstellung. |
| `europarechtskonformitaet` | Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht prüfen. Anwendungsfall Referent oder Verband fragt ob nationales Vorhaben mit EU-Recht vereinbar ist oder ob Notifizierungspflicht besteht. Primaerrecht EUV AEUV Grundrechtecharta Sekundaerrecht Verordnungen Richtlinien. Prüfung Anwendungsbereich Schutzbereich Eingriff Rechtfertigung Verhältnismäßigkeit. Notifizierungspflicht Richtlinie 2015/1535 technische Vorschriften IT-Vorschriften. Subsidiaritaet Verhältnismäßigkeit Art. 5 EUV Vorlagepflicht Art. 267 AEUV. Output Prüfgutachten ein bis drei Seiten Notifizierungs-Vermerk Empfehlung. Abgrenzung zu verfassungsmäßigkeit-quercheck nationales Verfassungsrecht. |

## Arbeitsweg

Im Plugin Legistik-Werkstatt gilt für **Legw Ressort Verbaendeanhoerung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `legw-ressort-bmf`

**Fokus:** Heranfuehrung Ressort BMF (Bundesministerium der Finanzen). Schwerpunkt: Steuer- und Fiskalrecht; Haushalts- und Zuwendungsrecht; Finanzmarkt; Zoll und Aussenwirtschaft; Geldwaesche. Kernnormen: AO; EStG; KStG; UStG; BHO; FinStabG; KWG; WpHG; ZollVG; GwG. Fuenf Spezialfelder: steuerrecht-und-fiskalnormen; haushalts-und-zuwendungsrecht; finanzmarktaufsicht-bafin-kwg-wpig; zoll-und-aussenwirtschaftsrecht; geldwaesche-und-sanktionsrecht. Output: Ressort-Kompass mit Materie; Akteuren; Normbestand; Aufsicht und Stolpersteinen. Anschluss legw-ressortaufgaben-bmf und legw-bmf-Themenslug.


# Ressort-Heranfuehrung BMF

> Heranfuehrungs-Skill nach `legw-ressort-router`. Politikwissenschaftliche Legistinnen und Legisten
> bekommen hier das Sachfeld-Verstaendnis fuer das Ressort, bevor sie an Normtext und Begruendung gehen.

## Ressort-Stammdaten

- **Volltitel:** Bundesministerium der Finanzen
- **Kuerzel:** BMF
- **Hausleitung Stand 2026:** Lars Klingbeil (SPD)
- **Dienstsitz:** Wilhelmstr. 97; 10117 Berlin; Zweitsitz Am Propsthof 78a; 53121 Bonn
- **Schwerpunkt:** Steuer- und Fiskalrecht; Haushalts- und Zuwendungsrecht; Finanzmarkt; Zoll und Aussenwirtschaft; Geldwaesche.
- **Kernnormen im Geschaeftsbereich:** AO; EStG; KStG; UStG; BHO; FinStabG; KWG; WpHG; ZollVG; GwG.

## Materie auf einer Seite

### Worum geht es sachlich

Steuer- und Fiskalrecht; Haushalts- und Zuwendungsrecht; Finanzmarkt; Zoll und Aussenwirtschaft; Geldwaesche. Dieses Ressort ist nicht primaer Politik; es ist sachverstaendige Verwaltung
einer Lebenswelt - Behoerden; Verbaende; technische Regeln; europaeische Rechtsakte und
Vollzugspraxis greifen ineinander.

### Wer spielt mit

- **Federfuehrendes Referat** (im BMF)
- **Nachgeordnete Behoerden und Aufsichten** des Geschaeftsbereichs
- **Bundesrat-Ausschuss** (bei zustimmungs- oder einspruchspflichtigen Vorhaben)
- **Bundestags-Fachausschuss** (BMF-Spiegel)
- **Verbaende** im Geschaeftsbereich (Beteiligung nach GGO Paragraf 47)
- **EU-Ebene** (Generaldirektion und Ratsformation)

### Welche Normen muss man lesen koennen

AO; EStG; KStG; UStG; BHO; FinStabG; KWG; WpHG; ZollVG; GwG.

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

- `legw-bmf-steuerrecht-und-fiskalnormen` - Steuerrecht und Fiskalnormen
- `legw-bmf-haushalts-und-zuwendungsrecht` - Haushaltsrecht und Zuwendungen
- `legw-bmf-finanzmarktaufsicht-bafin-kwg-wpig` - Finanzmarktaufsicht (BaFin; KWG; WpIG)
- `legw-bmf-zoll-und-aussenwirtschaftsrecht` - Zollrecht und Aussenwirtschaftsrecht
- `legw-bmf-geldwaesche-und-sanktionsrecht` - Geldwaescherecht und Sanktionsrecht

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

Anschluss an `legw-ressortaufgaben-bmf` - dort ressortspezifische Aufgaben (Begruendung;
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
Ressort: BMF - Bundesministerium der Finanzen
Hausleitung: Lars Klingbeil (SPD)
Materie: Steuer- und Fiskalrecht; Haushalts- und Zuwendungsrecht; Finanzmarkt; Zoll und Aussenwirtschaft; Geldwaesche.
Kernnormen: AO; EStG; KStG; UStG; BHO; FinStabG; KWG; WpHG; ZollVG; GwG.
Spezialfeld: <gewaehlter Slug>
Mitzeichner: <Liste>
Spiegelausschuss: <Bundestags-Ausschuss>
Verbaendekreis: <Listen-Liste>
EU-Bezug: <Generaldirektion und Rechtsakt>
Naechster Skill: legw-ressortaufgaben-bmf
```

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

## 2. `verbaendeanhoerung-ressortabstimmung`

**Fokus:** Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten. Anwendungsfall Referentenentwurf ist fertig und muss Verbaenden und Ressorts zugeleitet werden vor Kabinettsbefassung. Anschreiben Liste zu beteiligender Verbaende Ressorts Fristsetzung drei bis sechs Wochen. Auswertung Stellungnahmen zustimmend kritisch ablehnend mit konkreten Aenderungsvorschlaegen. Eigene Stellungnahme je kritischer Position Aenderungen dokumentiert. Output Auswertungsmatrix geaenderter Entwurf bereit für Kabinett. Abgrenzung zu begründung-allgemein-und-besonders inhaltliche Begründung.


# Verbändeanhörung und Ressortabstimmung

> Bevor das Kabinett entscheidet, muss man andere haben sprechen lassen.

## Verbändeanhörung

### Schritt 1 - Liste der Verbände

Verbandsliste je nach Sachgebiet. Beispiele:
- DIHK, ZDH, BDI, BDA, DGB (Wirtschaft, Arbeit)
- DAV, BRAK, BNotK (Anwälte, Notare)
- Sozialverband VdK, Sozialverband Deutschland (Sozialrecht)
- BvD, Stiftung Datenschutz (Datenschutz)
- Verbraucherzentrale Bundesverband (Verbraucherschutz)
- Stiftung Familienunternehmen
- Bitkom, eco, ZVEI (IT, Telekommunikation)
- HDE (Handel)
- Gewerkschaft Verdi etc.

### Schritt 2 - Anschreiben

"Anbei der Referentenentwurf eines Gesetzes zur ... Wir bitten um Stellungnahme bis ..."

### Schritt 3 - Fristen

- Standard: vier Wochen
- bei umfangreichen Entwuerfen: sechs Wochen
- bei Eile: zwei Wochen (mit Begründung)

### Schritt 4 - Auswertung

Tabelle:

| Verband | Position | Begründung | Vorschlag | Bewertung MinRef | Änderung |
|---|---|---|---|---|---|
| DIHK | kritisch | Erfüllungsaufwand | Schwellenwert anheben | erwogen | nein |
| Bitkom | zustimmend | Klare Regelung | - | - | - |
| Verbraucherzentrale | ablehnend | Goldplating | RL-Mindeststandard | abgelehnt | nein |

### Schritt 5 - Eigene Stellungnahme

Zu jeder kritischen Position eine eigene Position formulieren - das vermeidet politische Angriffsflaeche.

## Ressortabstimmung

GGO-Verfahren:

### Schritt 1 - Federführendes Ressort

Bestimmung durch Geschäftsordnung der Bundesregierung.

### Schritt 2 - Mitzeichnungsfähige Ressorts

Alle Ressorts, deren Geschäftsbereich betroffen ist. Auch nur am Rande - eher mitzeichnen lassen.

### Schritt 3 - Mitzeichnungs-Verfahren

- Standard: schriftlich
- bei Streit: Staatssekretaers-Runde
- bei nicht aufloesbaren Streit: Bundeskanzleramt entscheidet

### Schritt 4 - Dokumentation

Pro Änderungswunsch des Ressorts: Wer wollte was warum, wie wurde damit umgegangen.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 47-50 GGO (Ressortabstimmung, Verbands-Anhoerung) — § 63 BNatSchG (Verbandsbeteiligung Umwelt-NGOs) — § 47 Abs. 2 GGO (Fristen Ressortbeteiligung) — §§ 28, 29 VwVfG (Anhoerungsrecht Betroffener, Parallele zu Verbands-Beteiligung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

- Verbandsliste (Excel)
- Anschreiben (DOCX)
- Auswertungsmatrix (Excel + Markdown)
- Änderungs-Dokumentation (Markdown)

## Anschluss

`gesetzesentwurf-kabinett`.

## 3. `begruendung-allgemein-und-besonders`

**Fokus:** Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder Kabinettsentwurf ist fertig und Begründung muss nach HdR-Schema aufgebaut werden. Allgemeiner Teil A Anlass und Ziel B wesentlicher Inhalt C Alternativen D Erfuellungsaufwand E weitere Kosten F weitere Folgen. Besonderer Teil Erlaeuterung je geaendertem Paragrafen was geaendert wird warum wie es zu verstehen ist absehbare Auslegungsfragen Bezug BVerfG BVerwG BGH BSG BFH BAG EuGH-Rechtsprechung. Output vollständige Begründung. Anschluss synopse-erstellen xml-paralleldarstellung.


# Begründung allgemein und besonders

> Eine gute Begründung erleichtert Auslegung und Vollzug, eine schlechte führt zu Streit.

## Aufbau

### Teil A - Allgemeiner Teil

#### A.I. Zielsetzung und Notwendigkeit der Regelungen

Was soll erreicht werden? Warum ist eine Regelung erforderlich?

#### A.II. Wesentlicher Inhalt des Entwurfs

In zehn bis zwanzig Sätzen den Kern des Entwurfs darstellen.

#### A.III. Alternativen

Welche Alternativen wurden erwogen, warum verworfen?

#### A.IV. Gesetzgebungskompetenz

Verweis auf Art. 70 ff. GG bzw. Landeskompetenz. Erforderlichkeitsklausel Art. 72 Abs. 2 GG, falls einschlaegig.

#### A.V. Vereinbarkeit mit dem Recht der Europaeischen Union und mit völkerrechtlichen Verträgen

Bezug zu Primärrecht (EUV / AEUV / Charta), Sekundärrecht (RL / VO), EuGH-Rechtsprechung. Notifizierungspflicht 2015/1535?

#### A.VI. Gesetzesfolgen

- A.VI.1. Rechts- und Verwaltungsvereinfachung
- A.VI.2. Nachhaltigkeitsaspekte (SDG-Bezug)
- A.VI.3. Haushaltsausgaben ohne Erfüllungsaufwand
- A.VI.4. Erfüllungsaufwand (Bürger / Wirtschaft / Verwaltung)
- A.VI.5. Weitere Kosten
- A.VI.6. Weitere Gesetzesfolgen (gleichstellungspolitisch, demografisch, geschlechtsspezifisch, oekologisch)

#### A.VII. Befristung, Evaluierung

#### A.VIII. Vereinbarkeit mit den Zielen des Klimaschutzgesetzes

### Teil B - Besonderer Teil

Pro Artikel und pro Paragraf:

- Was wird geändert?
- Warum?
- Wie ist die Änderung zu verstehen (Auslegungshinweise)?
- Welche bestehende Rechtsprechung war Hintergrund?
- Welche Auslegungsfragen sind absehbar?

**Beispiel - Zu Artikel 1 Nummer 2 (Paragraf 33a HGB - neu):**

"Mit Paragraf 33a HGB wird die Pflicht zur Vorhaltung eines elektronischen Pflichtpostfachs eingeführt. Adressaten sind alle im Handelsregister eingetragenen Unternehmen sowie Unternehmen, die nach Artikel 33 DSA als sehr große Online-Plattform (VLOP) oder sehr große Online-Suchmaschine (VLOSE) eingestuft sind. Die Norm konkretisiert die seit der ZPO-Reform 2024 bestehenden Zustellverpflichtungen. ... Die Auswahl der Adressaten über den DSA-Schwellenwert von 45 Millionen Nutzern stellt sicher, dass die Pflicht keine kleinen und mittleren Unternehmen überraschend trifft. ..."

## Stilfragen

- Vergangenheitsform vermeiden, Praesens verwenden
- Keine politischen Bewertungen ("ist dringend notwendig"), nur sachliche Begründung
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine überfluessigen Floskeln

## Prüfliste

- [ ] Teil A.I bis A.VIII vollständig
- [ ] Teil B für jeden geänderten Paragrafen
- [ ] Rechtsprechung zitiert wo passend
- [ ] Erfüllungsaufwand mit Zahlen
- [ ] EU-Bezug und Notifizierung adressiert

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 39 VwVfG (Begruendungspflicht Verwaltungsakt) — § 41 VwVfG (Heilung von Begruendungsmaengeln) — § 76 GGO (Begruendung Referentenentwurf) — §§ 1-4 UVPG (Umwelt-Begruendungspflichten) — § 35 BauGB (Begruendung Abwaegungsergebnis Bauleitplanung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Markdown-Datei "Begruendung.md".

## Anschluss

`synopse-erstellen`.

## 4. `europarechtskonformitaet`

**Fokus:** Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht prüfen. Anwendungsfall Referent oder Verband fragt ob nationales Vorhaben mit EU-Recht vereinbar ist oder ob Notifizierungspflicht besteht. Primaerrecht EUV AEUV Grundrechtecharta Sekundaerrecht Verordnungen Richtlinien. Prüfung Anwendungsbereich Schutzbereich Eingriff Rechtfertigung Verhältnismäßigkeit. Notifizierungspflicht Richtlinie 2015/1535 technische Vorschriften IT-Vorschriften. Subsidiaritaet Verhältnismäßigkeit Art. 5 EUV Vorlagepflicht Art. 267 AEUV. Output Prüfgutachten ein bis drei Seiten Notifizierungs-Vermerk Empfehlung. Abgrenzung zu verfassungsmäßigkeit-quercheck nationales Verfassungsrecht.


# Europarechtskonformität

> EU-Recht läuft im Hintergrund mit. Wer es übersieht, riskiert EuGH-Vertragsverletzungsverfahren.

## Pruefstation 1 - EU-Anwendungsbereich

Beruehrt das Vorhaben einen unionsrechtlich harmonisierten oder mitgeregelten Bereich? Beispiele:

- DSA (Digital Services Act, VO 2022/2065) - Plattformregulierung
- DMA (Digital Markets Act, VO 2022/1925) - Gatekeeper
- AI Act (VO 2024/1689) - KI-Systeme
- eIDAS 2.0 (VO 2024/1183) - elektronische Identifizierung
- GDPR (VO 2016/679) - Datenschutz
- VO 1215/2012 (Brussel Ia) - Gerichtsstand
- VO 1393/2007 (Zustellungs-VO)

## Pruefstation 2 - Primärrecht

- Grundfreiheiten Warenverkehr, Personenverkehr, Niederlassung, Dienstleistung, Kapitalverkehr (Art. 28 ff., 45 ff., 49 ff., 56 ff., 63 ff. AEUV)
- Diskriminierungsverbot Art. 18 AEUV
- Grundrechte-Charta (insbesondere Art. 7 und Art. 8 - Privatleben und Datenschutz; Art. 11 - Freiheit der Meinungsaeusserung; Art. 16 - unternehmerische Freiheit; Art. 47 - effektiver Rechtsschutz)

## Pruefstation 3 - Sekundärrecht

- Welche Richtlinien und Verordnungen sind einschlaegig?
- Bei Richtlinien: Hat die nationale Umsetzungsfrist abgelaufen? Erfüllt das deutsche Recht bereits die RL?
- Bei VO: Direkt anwendbar - keine Umsetzung erforderlich, aber Ausführungsbestimmungen möglich.

## Pruefstation 4 - Verhältnismaessigkeit nach EU-Massstab

- legitimer Zweck
- geeignet
- erforderlich (mildestes Mittel)
- angemessen

EuGH ist im Massstab oft strenger als BVerfG.

## Pruefstation 5 - Notifizierungspflicht 2015/1535

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Prüfen: Faellt das Vorhaben unter:
- "technische Vorschrift" iSd Art. 1 Nr. 11 RL 2015/1535
- "Vorschrift betreffend Dienste" iSd Art. 1 Nr. 5 (Dienste der Informationsgesellschaft)

Bei elektronischen Postfaechern, technischen Datenformaten, IT-Schnittstellen: in der Regel notifizierungspflichtig.

## Pruefstation 6 - Subsidiaritaet Art. 5 EUV

Auch wenn die EU zustaendig waere - hat sie tatsächlich Recht gesetzt? Wenn nicht, kann der Mitgliedstaat regeln, soweit keine Sperrwirkung.

## Pruefstation 7 - Vorlagepflicht Art. 267 AEUV

Anwendung im Vollzug: Wenn das nationale Gesetz zu EU-Recht Auslegungszweifel weckt, wird das Tatgericht ggf. den EuGH anrufen müssen.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 288 AEUV (Rechtsakte, Verordnung, Richtlinie) — Art. 5 EUV (Subsidiaritaet, Verhaeltnismaessigkeit) — Art. 267 AEUV (Vorlagepflicht) — RL 2015/1535/EU Art. 1, 5 (Notifizierungspflicht) — Art. 51 Charta (Anwendungsbereich Grundrechte-Charta)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Pruefgutachten ein bis drei Seiten:

1. EU-Bezug ja / nein / unsicher
2. Einschlaegiges Primärrecht
3. Einschlaegiges Sekundärrecht
4. Verhältnismaessigkeit
5. Notifizierungspflicht ja / nein
6. Empfehlung: Notifizierung einleiten / nicht erforderlich
7. Empfehlung: bestimmte Änderungen am Entwurf

## Anschluss

`goldplating-vermeiden`, `verfassungsmaessigkeit-quercheck`.
