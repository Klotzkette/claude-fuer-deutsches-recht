---
name: verkehrsowi-punkte-fahrverbot
description: "Punkte Fahrverbot: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Punkte Fahrverbot

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Punkte Fahrverbot** im Plugin Verkehrs-OWi-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verkehrsowi-punkte-fahrverbot-flensburg` | Punkte im Fahreignungsregister (FAER) Flensburg und Fahrverbot § 25 StVG: Mandant hat Punktewarnung erhalten oder Führerscheinentzug droht. Normen: § 4 StVG (Punktesystem: Warnung 4 Pkt, Verwarnung 6 Pkt, Entzug 8 Pkt), § 65 StVG (Tilgungsfristen), § 25 StVG (Fahrverbot als Denkzettel). Prüfraster: Punktestand, Tilgungsfristen, freiwilliger Kurs zur Punkte-Reduzierung, Abgrenzung FAER-Punkte vs. Fahrverbot. Output Punkte-Berechnungs-Übersicht, Strategie-Empfehlung. Abgrenzung: Haertefall-Fahrverbot siehe verkehrsowi-haertefall-fahrverbot; Fahrerlaubnisentzug MPU siehe fachanwalt-verkehrsrecht-Plugin. |
| `verkehrsowi-rechtsbeschwerde` | Rechtsbeschwerde im OWi-Verfahren nach § 79 OWiG einlegen: AG hat OWi-Urteil gesprochen und Mandant will Rechtsbeschwerde. Normen: § 79 OWiG (Zulassigkeit: Geldbusse über 250 EUR oder Fahrverbot), § 80 OWiG (Zulassungsbeschwerde), § 344 StPO i.V.m. § 79 Abs. 3 OWiG (Begründungspflicht), Frist 1 Woche ab Urteil. Prüfraster: Statthaftigkeit, Verfahrensruege vs. Sachruege, Formalanforderungen, OLG als Rechtsbeschwerdeinstanz. Output Rechtsbeschwerde-Schrift. Abgrenzung: Einspruch gegen Bußgeldbescheid siehe verkehrsowi-fristen-einspruch; HV vorher siehe verkehrsowi-hauptverhandlung-amtsgericht. |
| `verkehrsowi-rotlicht-abstand-handy` | Rotlicht-OWi, Abstand-OWi und Handy-OWi verteidigen: Mandant hat Bußgeldbescheid wegen Rotlicht, zu geringem Abstand oder Handynutzung erhalten. Normen: § 37 StVO (Rotlicht: einfach vs. qualifiziert 1 Sekunde), § 4 StVO (Abstand-Berechnung Tacho-Laenge), § 23 Abs. 1a StVO (Festhalten-Begriff BGH). Prüfraster: Beweisgrundlagen (Videobeweise, Polizeizeugen), typische Verteidigungsargumente je Tatvorwurf. Output Verteidigungs-Strategie, Beweisantrags-Entwurf. Abgrenzung: Geschwindigkeit siehe verkehrsowi-messverfahren-geschwindigkeit; Zeugen-Strategie siehe verkehrsowi-zeugen-polizei-strategie. |

## Arbeitsweg

Im Plugin Verkehrs-OWi-Verteidigung gilt für **Punkte Fahrverbot**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verkehrsowi-punkte-fahrverbot-flensburg`

**Fokus:** Punkte im Fahreignungsregister (FAER) Flensburg und Fahrverbot § 25 StVG: Mandant hat Punktewarnung erhalten oder Führerscheinentzug droht. Normen: § 4 StVG (Punktesystem: Warnung 4 Pkt, Verwarnung 6 Pkt, Entzug 8 Pkt), § 65 StVG (Tilgungsfristen), § 25 StVG (Fahrverbot als Denkzettel). Prüfraster: Punktestand, Tilgungsfristen, freiwilliger Kurs zur Punkte-Reduzierung, Abgrenzung FAER-Punkte vs. Fahrverbot. Output Punkte-Berechnungs-Übersicht, Strategie-Empfehlung. Abgrenzung: Haertefall-Fahrverbot siehe verkehrsowi-haertefall-fahrverbot; Fahrerlaubnisentzug MPU siehe fachanwalt-verkehrsrecht-Plugin.

# Punkte und Fahrverbot — Fahreignungsregister Flensburg

## Triage zu Beginn

1. **Aktueller Punktestand?** — Mandant soll FAER-Auskunft beim KBA beantragen (§ 30 StVG).
2. **Neue Eintragung droht?** — Nach Bussgeldbescheid oder Verurteilung: wann wird eingetragen?
3. **Wie viele Punkte nach neuer Eintragung?** — Warnstufen nach § 4 Abs. 5 StVG: bei 4 Punkten Ermahnung, bei 6 Punkten Verwarnung, bei 8 Punkten Entzug.
4. **Tilgungsfristen laufen?** — § 65 StVG: Punktetilgung nach Ablauf der Tilgungsfrist (2,5 oder 10 Jahre je nach Eintragungsart).
5. **Freiwilliger Kurs moeglich?** — Nach § 4 Abs. 7 StVG: bei Punkt-Level 1-5 kann Kurs 1 Punkt reduzieren.

## Zentrale Normen

- **§ 4 StVG** — Fahreignungs-Bewertungssystem: Eintragungen, Warnstufen, Konsequenzen
- **§ 4 Abs. 5 StVG** — Stufensystem: 1-3 Punkte (keine Massnahme), 4-5 Punkte (Ermahnung), 6-7 Punkte (Verwarnung), 8+ Punkte (Entziehung)
- **§ 4 Abs. 7 StVG** — Freiwilliger Kurs: 1 Punkt-Reduktion moeglich bei <= 5 Punkten
- **§ 30 StVG** — Recht auf Auskunft aus dem FAER
- **§ 65 StVG** — Tilgungsfristen: Grundregel 2,5 Jahre; Ausnahme (z.B. Straftaten mit Entziehung) 10 Jahre
- **§ 66 StVG** — Tilgungshemmung bei neuer Eintragung innerhalb der Tilgungsfrist
- **§ 25 StVG** — Fahrverbot (separate Sanktion, keine Punkte-Konsequenz an sich)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Punkte-Tabelle nach BKatV (Auswahl)

| Verstos | Punkte |
|---------|--------|
| Geschwindigkeit 31-40 km/h uber Erlaubnis | 1 Punkt |
| Geschwindigkeit 41-60 km/h uber Erlaubnis | 2 Punkte |
| Geschwindigkeit 61-70 km/h uber Erlaubnis | 2 Punkte + Fahrverbot |
| Rotlicht-Verstos 1 Sekunde | 1 Punkt |
| Rotlicht-Verstos qualifiziert (> 1s) | 2 Punkte + Fahrverbot |
| Abstandsunterschreitung < 4/10 Fahrbahn (> 100 km/h) | 1 Punkt |
| Handy am Steuer | 1 Punkt |
| § 316 StGB (Trunkenheitsfahrt) | 3 Punkte + Fahrerlaubnis-Entzug |

## Tilgungsfristen (§ 65 StVG)

| Eintragungsart | Tilgungsfrist |
|---------------|--------------|
| 1-Punkt-Eintragung | 2,5 Jahre |
| 2-Punkt-Eintragung | 5 Jahre |
| Straftaten (ohne Entziehung) | 5 Jahre |
| Straftaten (mit Fahrerlaubnis-Entziehung) | 10 Jahre |

## Schritt-fuer-Schritt-Workflow

1. **FAER-Auskunft beantragen** (§ 30 StVG) — Mandant beim KBA Flensburg (Kraftfahrtbundesamt).
2. **Punktestand berechnen** nach neuer Eintragung.
3. **Tilgungsfristen pruefen:** Laufen alte Eintragungen demnachst aus?
4. **Kursoption pruefen:** <= 5 Punkte → freiwilliger Kurs nach § 4 Abs. 7 StVG.
5. **MPU-Risiko pruefen:** Bei Alkohol- oder Drogendelikten koennen Behoerden MPU anordnen.
6. **Verwaltungsrechtlichen Weg einschlagen** bei unberechtigter Eintragung (Widerspruch, VG-Klage).

## Harte Leitplanken

- Punkte koennen nicht "verhandelt" werden — Eintragung ist automatisch nach Rechtskraft.
- Tilgungshemmung durch neue Eintragung beachten.
- Freiwilliger Kurs nur bei <= 5 Punkten wirksam.
- Anwaltliche Endkontrolle bei Kursempfehlung und Verwaltungsrechtsstrategie.

## 2. `verkehrsowi-rechtsbeschwerde`

**Fokus:** Rechtsbeschwerde im OWi-Verfahren nach § 79 OWiG einlegen: AG hat OWi-Urteil gesprochen und Mandant will Rechtsbeschwerde. Normen: § 79 OWiG (Zulassigkeit: Geldbusse über 250 EUR oder Fahrverbot), § 80 OWiG (Zulassungsbeschwerde), § 344 StPO i.V.m. § 79 Abs. 3 OWiG (Begründungspflicht), Frist 1 Woche ab Urteil. Prüfraster: Statthaftigkeit, Verfahrensruege vs. Sachruege, Formalanforderungen, OLG als Rechtsbeschwerdeinstanz. Output Rechtsbeschwerde-Schrift. Abgrenzung: Einspruch gegen Bußgeldbescheid siehe verkehrsowi-fristen-einspruch; HV vorher siehe verkehrsowi-hauptverhandlung-amtsgericht.

# Rechtsbeschwerde im OWi-Verfahren — § 79 OWiG

## Triage zu Beginn

1. **Ist Rechtsbeschwerde zulaessig?** — § 79 Abs. 1 OWiG: zulaessig bei Geldbusse > 250 EUR ODER Fahrverbot; ansonsten nur Zulassungsbeschwerde nach § 80 OWiG.
2. **Welches Gericht ist zustaendig?** — OLG im jeweiligen Bundesland (Ausnahme: bei Grundsatzfragen auch BGH denkbar, sehr selten).
3. **Was soll angegriffen werden?** — Rechtsfehler (Verfahrensruege oder Sachruge); keine Tatsachenpruefung in der Rechtsbeschwerde!
4. **Frist beachten?** — 1 Woche ab Urteilsverkuendung; Begründungsfrist 1 Monat ab Urteilszustellung (§ 79 Abs. 3 OWiG i.V.m. § 345 StPO).
5. **Kostenrisiko?** — Bei erfolgloser Rechtsbeschwerde: Gebuehren + ggf. Kosten der Gegenpartei.

## Zentrale Normen

- **§ 79 Abs. 1 OWiG** — Rechtsbeschwerde: Geldbusse > 250 EUR oder Fahrverbot
- **§ 79 Abs. 3 OWiG i.V.m. § 344 StPO** — Ruegeformen: Verfahrensruege und Sachruge
- **§ 79 Abs. 3 OWiG i.V.m. § 345 StPO** — Begründungsfrist 1 Monat ab Zustellung Urteilsgruende
- **§ 80 OWiG** — Zulassungsbeschwerde: bei Geldbusse <= 250 EUR; nur bei grundsaetzlicher Bedeutung oder Fortbildung des Rechts
- **§ 341 StPO i.V.m. § 79 Abs. 3 OWiG** — Einlegungsfrist 1 Woche ab Urteilsverkuendung
- **§ 338 StPO i.V.m. § 79 OWiG** — Absolute Revisionsgründe gelten auch in der Rechtsbeschwerde

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pruefschema Rechtsbeschwerde-Zulaessigkeit

```
§ 79 Abs. 1 OWiG — Zulaessigkeit:
□ Geldbusse > 250 EUR ODER Fahrverbot? → Rechtsbeschwerde zulaessig
□ Geldbusse <= 250 EUR, kein Fahrverbot? → Nur Zulassungsbeschwerde § 80 OWiG

Fristen:
□ Einlegungsfrist: 1 Woche ab Urteilsverkuendung
□ Begründungsfrist: 1 Monat ab Zustellung der Urteilsgruende
□ Urteilszustellung abwarten (ergibt Begründungsfrist-Start)

Ruegeformen:
□ Verfahrensruege: konkreter Verfahrensverstos (Sachverstaendigenantrag, Belehrung)
□ Sachrüge: Fehler bei der Anwendung des materiellen Rechts
```

## Verfahrensruegen — typische Angriffspunkte

```
1. Ablehnung Sachverstaendigenantrag (§ 77 OWiG) ohne Begruendung
2. Verletzung rechtliches Gehoer (Art. 103 GG): Rohmessdaten verweigert
3. Keine ordnungsgemaesse Belehrung ueber Schweigerecht (§ 55 OWiG)
4. Messgeraet nicht gesetzlich geeicht (§ 6 MessEG)
5. Urteilsbegruendung widerspricht sich selbst (§ 267 StPO i.V.m. § 71 OWiG)
6. Letztes Wort verweigert (§ 258 Abs. 3 StPO i.V.m. § 71 OWiG)
```

## Output-Template Rechtsbeschwerdeschrift

```
An das OLG [ORT]
[Anschrift]

In der OWi-Sache gegen [NAME]
Az. AG: [AKTENZEICHEN]

Rechtsbeschwerde nach § 79 OWiG

Namens des Betroffenen [NAME] lege ich gegen das Urteil des
Amtsgerichts [ORT] vom [DATUM] frist- und formgerecht

Rechtsbeschwerde

ein. Die Urteilsgruende sind noch nicht zugestellt; die Begründung
erfolgt innerhalb der gesetzlichen Frist nach § 79 Abs. 3 OWiG.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Rechtsbeschwerde nur bei Rechtsfehler — keine Tatsachenpruefung!
- Begründungsfrist 1 Monat nach Urteilszustellung — nicht nach Verkuendung!
- Zulassungsbeschwerde bei Geldbusse <= 250 EUR: Grundsatzrechtsfrage benennen.
- Anwaltliche Endkontrolle bei Ruge-Formulierung.

## 3. `verkehrsowi-rotlicht-abstand-handy`

**Fokus:** Rotlicht-OWi, Abstand-OWi und Handy-OWi verteidigen: Mandant hat Bußgeldbescheid wegen Rotlicht, zu geringem Abstand oder Handynutzung erhalten. Normen: § 37 StVO (Rotlicht: einfach vs. qualifiziert 1 Sekunde), § 4 StVO (Abstand-Berechnung Tacho-Laenge), § 23 Abs. 1a StVO (Festhalten-Begriff BGH). Prüfraster: Beweisgrundlagen (Videobeweise, Polizeizeugen), typische Verteidigungsargumente je Tatvorwurf. Output Verteidigungs-Strategie, Beweisantrags-Entwurf. Abgrenzung: Geschwindigkeit siehe verkehrsowi-messverfahren-geschwindigkeit; Zeugen-Strategie siehe verkehrsowi-zeugen-polizei-strategie.

# Rotlicht, Abstand und Handy — §§ 23, 37, 4 StVO

## Triage zu Beginn

1. **Rotlicht oder Abstand oder Handy?** — Verschiedene Normen, verschiedene Beweisgruende.
2. **Rotlicht:** Einfach (bis 1 Sekunde Rotphase, 1 Punkt) oder qualifiziert (> 1 Sekunde, 2 Punkte + Fahrverbot)?
3. **Abstand:** Stationaere Messung (Videomessung) oder Nachfahrmessung? Berechnung: Abstand in Meter / 2 = Mindestpflicht bei km/h (Faustformel).
4. **Handy:** Tatsaechliches Festhalten am Geraet? BGH: bewusstes Aufnehmen in die Hand und Halten; "Aufheben vom Boden" oder "Einlegen in die Halterung" = kein § 23 Abs. 1a StVG.
5. **Beweislage?** — Video, Foto, Polizeiaussage — welche Beweismittel liegen vor?

## Zentrale Normen

- **§ 37 StVO** — Wechsellichtzeichen; Rotlicht-Verstos
- **§ 4 StVO** — Abstandspflicht; Sicherheitsabstand
- **§ 23 Abs. 1a StVO** — Verbot des Festhaltens elektronischer Geraete beim Fahren
- **§ 24 StVG i.V.m. Anlage BKatV** — Geldbusse und Punkte fuer die genannten Delikte
- **§ 49 StVO** — Bussgeldbewehrung der StVO-Verstösse

## Aktuelle Rechtsprechung

- OLG Frankfurt a.M., Beschl. v. 29.1.2021 - 2 Ss OWi 800/20 (NZV 2021, 210 — Volltext über openjur.de oder offene Justizdatenbank Hessen verifizieren): Rotlicht-Video-Beweis: Kalibrierung der Messanlage muss nachgewiesen sein; ohne Kalibrier-Nachweis ist Messung in der Rechtsbeschwerde angreifbar.
- OLG-Linien zu § 23 Abs. 1a StVO (Handynutzung): vor Versand in openjur.de und offenen Landesjustiz-Datenbanken verifizieren — insbesondere zur Abgrenzung "Halten" vs. "blosses Berühren".
- Abstandsverstoss § 4 StVO: standardisiertes Messverfahren mit Videoabstandsmessung VAMA/VKS und ProViDa; konkrete OLG-Aktenzeichen vor Versand in offener Quelle aufrufen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Besonderheiten je Verstos-Typ

### Rotlicht (§ 37 StVO)

```
Einfaches Rotlicht (Ampel seit < 1s rot):
- 1 Punkt, 90 EUR Geldbusse (Fahrzeugfuehrer)
- Kein Regelfahrverbot

Qualifiziertes Rotlicht (Ampel seit > 1s rot):
- 2 Punkte + Fahrverbot 1 Monat, 200 EUR Geldbusse
- NACHWEIS: Ampelphasendauer muss exakt gemessen sein

Angriffspunkte:
- Messung der Rotphasendauer (Video-Kalibrierung?)
- Sichtbarkeit der Ampel (Sichtbehinderung, Sonne)
- Stich-Zeuge des Polizeibeamten (aus dem Gedaechtnis oder Protokoll?)
```

### Abstandsverstos (§ 4 StVO)

```
Berechnung Mindestabstand (Faustformel):
- Bei 100 km/h: mind. 50 m Abstand
- Bei 130 km/h: mind. 65 m Abstand
(= halbe Tachoanzeige in Metern)

Messverfahren:
- Videomessung: Tacholange-Methode; Kalibrierung notwendig
- Nachfahrmessung: Abstand konstant gehalten?

Angriffspunkte:
- Kalibrierung der Messanlage
- Berechnungsgrundlagen im Urteil nicht erlaeutert
- Kurzfristiger Abstandsverstoss nach Einscheren anderer Fahrzeuge
```

### Handy am Steuer (§ 23 Abs. 1a StVO)

```
Verboten: Bewusstes Festhalten eines elektronischen Geraets beim Fahren
Erlaubt: Einlegen in die Halterung, Ablegen, kurzzeitiges Anfassen

BGH 2019: Kein Verstoss bei:
- Aufheben vom Boden
- Einlegen in eine Halterung
- Reichen an Mitfahrer

Angriffspunkte:
- War das Fahrzeug tatsaechlich in Bewegung? (Haltepflicht an roter Ampel: DENNOCH verboten!)
- Handelte es sich um bewusstes Festhalten oder nur kurzzeitiges Anfassen?
- Polizeibeamten-Aussage: konkrete Wahrnehmung oder Schlussfolgerung?
```

## Harte Leitplanken

- Qualifiziertes Rotlicht erfordert Nachweis der > 1-Sekunden-Phase — immer angreifen wenn unklar.
- Handy-Verstos-Definition nach BGH 2019 kennen und anwenden.
- Abstandsberechnung immer selbst nachrechnen.
- Anwaltliche Endkontrolle bei Rechtsbeschwerde-Begründung.
