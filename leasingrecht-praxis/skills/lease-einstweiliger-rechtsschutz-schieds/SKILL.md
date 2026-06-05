---
name: lease-einstweiliger-rechtsschutz-schieds
description: "Lease Einstweiliger Rechtsschutz Schieds: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Einstweiliger Rechtsschutz Schieds

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Einstweiliger Rechtsschutz Schieds** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-041-einstweiliger-rechtsschutz-herausgabe-leasingobjekt` | Einstweiliger Rechtsschutz: Herausgabeverfügung für Leasingobjekte, Verfügungsanspruch, Verfügungsgrund, Vollzug und Gegenwehr des LN. |
| `lease-042-schieds-oder-gerichtsstand-leasing` | Streitbeilegung im Leasingrecht: Schiedsverfahren vs. staatliche Gerichte, Gerichtsstandsklausel, Verbraucherrecht, Mediation und internationale Schiedsgerichte. |
| `lease-045-risiko-dashboard-leasingportfolio` | Risiko-Dashboard Leasingportfolio: KPIs, Konzentrations- und Restwertrisiken, NPL-Tracking, Stresstest und regulatorisches Reporting. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Einstweiliger Rechtsschutz Schieds**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-041-einstweiliger-rechtsschutz-herausgabe-leasingobjekt`

**Fokus:** Einstweiliger Rechtsschutz: Herausgabeverfügung für Leasingobjekte, Verfügungsanspruch, Verfügungsgrund, Vollzug und Gegenwehr des LN.

# Einstweiliger Rechtsschutz: Herausgabe des Leasingobjekts

## Zweck

Nach Kündigung des Leasingvertrags verweigert der Leasingnehmer die Herausgabe des Leasingobjekts. Der Leasinggeber braucht schnell einen Vollstreckungstitel. Dieser Skill analysiert die einstweilige Verfügung, Voraussetzungen, Vollzug und Abwehrmöglichkeiten.

## Rechtsgrundlage: §§ 935, 940 ZPO

### Einstweilige Verfügung zur Sicherung des Anspruchs (§ 935 ZPO)
Zweck: Sicherung eines dinglichen oder schuldrechtlichen Anspruchs, wenn ohne Sicherung eine wesentliche Erschwerung oder Vereitelung droht.

### Regelungsverfügung (§ 940 ZPO)
Zweck: Regelung eines einstweiligen Zustands, um wesentliche Nachteile abzuwenden oder drohende Gewalt zu verhindern.

Bei Leasingherausgabe: Häufig § 940 ZPO (Regelungsverfügung), wenn LN droht, Objekt zu verstecken oder zu veräußern.

## Voraussetzungen

### 1. Verfügungsanspruch
- Eigentumsrecht des LG am Leasingobjekt: Nachzuweisen durch Kaufvertrag, Eigentumsübertragung
- Herausgabeanspruch aus § 985 BGB (Eigentum) und aus Leasingvertrag nach wirksamer Kündigung
- Wirksamkeit der Kündigung muss glaubhaft gemacht werden (keine volle Beweisführung im einstweiligen Verfahren)

### 2. Verfügungsgrund
- Dringlichkeit: Gefahr, dass ohne sofortige Maßnahme der Anspruch vereitelt wird
- Konkreter Anhaltspunkt erforderlich: z.B. LN droht mit Weiterveräußerung, will ins Ausland verbringen, ist auf der Flucht
- Verfügungsgrund nicht schematisch aus bloßer Nichtherausgabe ableiten; konkrete Vereitelungs-, Verbringungs- oder Wertverlustrisiken belegen

### Glaubhaftmachung (§ 294 ZPO)
- Kein Vollbeweis; eidesstattliche Versicherung des LG ausreichend
- Urkunden (Kaufvertrag, Leasingvertrag, Kündigung) als Anlagen

## Antrag und Verfahren

### Antragsstelle
- Zuständig: Gericht am Ort des Leasingobjekts (§ 937 ZPO: Gericht der Hauptsache oder Amtsgericht)
- Bei Gefahr in Verzug: Amtsgericht am Ort des Objekts

### Ohne mündliche Verhandlung
- Eilantrag: Gericht kann ohne Anhörung des LN entscheiden (§ 937 II ZPO)
- Schutzschrift des LN: Wenn LN vorab Schutzschrift hinterlegt, muss Gericht diese berücksichtigen

### Inhalt des Beschlusses
- Auflage: LN muss das Objekt an LG herausgeben
- Vollziehungsfrist: § 929 II ZPO – Vollziehung innerhalb 1 Monat

## Vollzug der Herausgabeverfügung

- Vollstreckung: Gerichtsvollzieher holt das Objekt beim LN ab (§ 883 ZPO analog)
- LN weigert sich: Ordnungsgeld bis 250.000 €, ersatzweise Ordnungshaft (§ 890 ZPO)
- Sicherheitsleistung: LG kann verpflichtet sein, Sicherheit zu leisten (§ 921 ZPO)

## Widerspruch und Hauptsache

### Widerspruch des LN (§ 924 ZPO)
- LN kann Widerspruch einlegen → mündliche Verhandlung
- LG muss in der Hauptsacheklage seinen Anspruch vollständig beweisen

### Schadensersatz (§ 945 ZPO)
- Wenn Verfügung zu Unrecht erlassen: LG haftet für Schäden des LN

## Prüfprogramm

1. Eigentumsrecht des LG: Belege vorhanden (Kaufvertrag, kein Eigentumsübergang auf LN)?
2. Kündigung wirksam? Nachweise: Mahnungen, Verzug, Kündigungsschreiben?
3. Verfügungsgrund: Konkreter Anhaltspunkt für Veräußerungs-/Verbringungsgefahr?
4. Zuständiges Gericht: Ort des Leasingobjekts?
5. Schutzschrift des LN hinterlegt?
6. Vollziehungsfrist (1 Monat): Eingehalten?

## Typische Fallen

- Verfügungsgrund fehlt: Bloße Weigerung herausgeben reicht nicht → Gericht lehnt ab
- Kündigung unwirksam (z.B. keine Abmahnung bei Verbraucher) → Verfügungsanspruch fehlt
- Eigentumsrecht nicht nachgewiesen → Antrag scheitert
- Vollziehungsfrist versäumt (§ 929 II ZPO) → Verfügung wird wirkungslos

## Normen und Quellen

- §§ 935, 940 ZPO: https://www.gesetze-im-internet.de/zpo/__935.html
- § 937 ZPO (Zuständigkeit): https://www.gesetze-im-internet.de/zpo/__937.html
- § 945 ZPO (Schadenersatz bei unberechtigter Verfügung): https://www.gesetze-im-internet.de/zpo/__945.html
- § 985 BGB (Herausgabeanspruch): https://dejure.org/gesetze/BGB/985.html
- § 890 ZPO (Ordnungsgeld): https://www.gesetze-im-internet.de/zpo/__890.html
- Einstweiliger Rechtsschutz im Leasing nur mit konkret verifizierter Entscheidung zitieren
- openjur.de einstweilige Verfügung Leasing: https://openjur.de

## Output-Formate

- **Antrag auf einstweilige Verfügung**: Vollständige Vorlage mit Verfügungsanspruch und -grund
- **Eidesstattliche Versicherung**: Muster für LG
- **Schutzschrift-Muster**: Für LN zur Hinterlegung beim Schutzschriftenregister
- **Vollzugsprotokoll**: Gerichtsvollzieher-Vollzug einstweilige Verfügung

## 2. `lease-042-schieds-oder-gerichtsstand-leasing`

**Fokus:** Streitbeilegung im Leasingrecht: Schiedsverfahren vs. staatliche Gerichte, Gerichtsstandsklausel, Verbraucherrecht, Mediation und internationale Schiedsgerichte.

# Schiedsverfahren und Gerichtsstand im Leasingrecht

## Zweck

Leasingverträge enthalten häufig Klauseln zu Gerichtsstand und Streitbeilegung. Im internationalen und B2B-Bereich sind Schiedsverfahren attraktiv. Im B2C-Bereich sind Gerichtsstandsklauseln eingeschränkt. Dieser Skill analysiert die Optionen.

## Gerichtsstandsklauseln

### B2B (Unternehmensleasing)
- § 38 ZPO: Gerichtsstandsvereinbarung zwischen Kaufleuten zulässig
- Formerfordernis: Schriftlich oder in Textform (§ 40 ZPO analog)
- Wirkung: Ausschließlicher oder nicht-ausschließlicher Gerichtsstand

### B2C (Verbraucherleasing)
- § 29c ZPO: Beim Verbraucher nur Gerichtsstand am Wohnort des Verbrauchers
- Gerichtsstandsklauseln zulasten des Verbrauchers: AGB-widrig (§ 307 BGB)
- Ausnahme: Vereinbarung nach Entstehung des Rechtsstreits (§ 38 III ZPO)

### EU: EuGVO (VO 1215/2012)
- Art. 7 EuGVO: Besonderer Gerichtsstand am Erfüllungsort
- Art. 19 ff. EuGVO: Verbraucher hat besondere Schutzgerichtsstand (Wohnsitzland)
- Gerichtsstandsklauseln gegen Verbraucher: Nur eingeschränkt zulässig (Art. 25 EuGVO)

## Schiedsverfahren

### Vorteile
- Vertraulichkeit: Kein öffentliches Verfahren
- Schnelligkeit: Flexible Verfahrensordnung
- Internationale Vollstreckung: New Yorker Übereinkommen (1958) in 170+ Ländern
- Spezialisierung: Branchenkundige Schiedsrichter

### Nachteile
- Kosten: Höher als staatliche Gerichte (Schiedsrichterhonorar)
- Kein einstweiliger Rechtsschutz direkt (Schiedsgericht kann vorsorgliche Maßnahmen anordnen, aber staatliches Gericht vollstreckt)
- Kein gesetzlicher Instanzenzug

### Schiedsklausel (§ 1029 ZPO)
Formerfordernis: Schriftliche Vereinbarung (§ 1031 ZPO); Textform bei Verbrauchern (§ 1031 V ZPO).

Inhalt:
- Schiedsgerichtsordnung (DIS, ICC, LCIA)
- Schiedsort (maßgeblich für Anfechtungsverfahren)
- Schiedsrichteranzahl (1 oder 3)
- Schiedssprache

### DIS-Schiedsregeln (Deutsche Institution für Schiedsgerichtsbarkeit)
- Neue DIS-Regeln 2018
- Expedited Proceedings: Schnellverfahren für Ansprüche bis 2 Mio. €

### Verbraucher und Schiedsverfahren
- § 1031 V ZPO: Bei Verbrauchern muss Schiedsklausel separat unterzeichnet sein
- AGB-Einbeziehung reicht nicht; Überraschungsverbot (§ 305c BGB)
- Schiedsklausel in B2C-AGB praktisch unwirksam

## Mediation und ADR

### Mediationsklausel
- Vor Schiedsverfahren: Mediation (§ 36 VSBG: Verbraucherstreitbeilegungsgesetz)
- Freiwillig; schnell; günstig

### VSBG (Verbraucherstreitbeilegungsgesetz)
- LG muss Verbraucher über Möglichkeit der außergerichtlichen Streitbeilegung informieren (§ 36 VSBG)
- Keine Pflicht zur Teilnahme; aber Information ist Pflicht

## Prüfprogramm

1. B2B oder B2C? Verbraucher → eingeschränkte Gerichtsstandswahl
2. Gerichtsstandsklausel: Wirksam nach § 38 ZPO oder AGB-widrig?
3. Schiedsklausel: Formgültig (§ 1031 ZPO)? Verbraucher separat unterschrieben?
4. Schiedsgericht gewählt: DIS, ICC oder ad hoc? Schiedsort?
5. Einstweiliger Rechtsschutz: Staatliches Gericht parallel?
6. VSBG-Information: Auf Webseite und in AGB erteilt?

## Typische Fallen

- Gerichtsstandsklausel gegen Verbraucher: AGB-widrig; staatliche Gerichte zuständig
- Schiedsklausel in B2C-AGB ohne gesonderte Unterschrift: Unwirksam
- Kein einstweiliger Rechtsschutz über Schiedsgericht vorgesehen: Verzögerung
- VSBG-Informationspflicht verletzt: OLG-Urteile: Abmahnrisiko

## Normen und Quellen

- §§ 1029–1066 ZPO (Schiedsverfahren): https://www.gesetze-im-internet.de/zpo/__1029.html
- § 38 ZPO (Gerichtsstandsvereinbarung): https://www.gesetze-im-internet.de/zpo/__38.html
- EuGVO (VO 1215/2012): https://eur-lex.europa.eu
- New Yorker Übereinkommen 1958: https://www.uncitral.org
- VSBG (Verbraucherstreitbeilegungsgesetz): https://www.gesetze-im-internet.de/vsbg/
- DIS-Schiedsregeln 2018: https://www.dis-arb.de

## Output-Formate

- **Schiedsklausel-Muster B2B**: DIS-Schiedsklausel für Leasingverträge
- **Gerichtsstandsklausel-Muster B2B**: Ausschließlicher Gerichtsstand
- **VSBG-Informationstext**: Pflichthinweis für LG-Website und AGB
- **Mediationsklausel**: Stufenklausel (erst Mediation, dann Schiedsgericht)

## 3. `lease-045-risiko-dashboard-leasingportfolio`

**Fokus:** Risiko-Dashboard Leasingportfolio: KPIs, Konzentrations- und Restwertrisiken, NPL-Tracking, Stresstest und regulatorisches Reporting.

# Risiko-Dashboard: Leasingportfolio

## Zweck

Ein Leasingportfolio muss kontinuierlich überwacht werden. Dieses Skill-Modul definiert die KPIs, zeigt Risikokategorien und beschreibt das Reporting-Format für Management und Regulatoren.

## Portfolio-KPIs

### Volumenmetriken
| KPI | Definition | Zielwert (Richtwert) |
|---|---|---|
| Portfoliovolumen (EAD) | Summe ausstehender Raten + Restwert | Fortlaufend |
| Vertragszahl | Anzahl aktiver Leasingverträge | Fortlaufend |
| Ø-Vertragsgröße | EAD / Vertragszahl | Branchen-Benchmark |
| Laufzeit-Restdauer | Ø Monate bis Vertragsende | < 48 Monate (Richtwert) |

### Ausfallmetriken
| KPI | Definition | Ampelgrenze |
|---|---|---|
| NPL-Quote | NPL-EAD / Gesamt-EAD | < 3 % (grün), 3–7 % (gelb), > 7 % (rot) |
| Rückstandsquote 30+ | EAD mit > 30 Tage Verzug / Gesamt | < 5 % |
| Verwertungsquote | Erzielter Erlös / Buchwert bei Verwertung | > 85 % (grün) |
| Recovery Rate | Eingezogener Betrag / Ausgefallener EAD | > 60 % (grün) |

### Restwertrisiko
| KPI | Definition |
|---|---|
| Portfoliogewichteter Restwert | Ø Restwert-Quote: Restwert / Anschaffungskosten |
| Restwert-Gap | Aktueller Marktwert – kalkulierter Restwert (positiv = gut) |
| Konzentration in Objektklasse | % EAD in Kfz / Maschinen / IT / Immobilien |

## Konzentrationsrisiken

### Klumpenrisiken
- **LN-Konzentration**: Größter LN als % des Gesamtportfolios (< 10 % empfohlen)
- **Branchenkonzentration**: Branchen-BIP-Gewicht vs. Portfolio-Gewicht
- **Objektkonzentration**: Einzelne Objektklasse > 40 % (erhöhtes Marktwertrisiko)
- **Geografische Konzentration**: Region oder Land > 30 %

### Herfindahl-Hirschman-Index (HHI)
Konzentrationsmaß: Summe der quadrierten Marktanteile.
- HHI < 1.500: Geringe Konzentration (grün)
- HHI 1.500–2.500: Mäßige Konzentration (gelb)
- HHI > 2.500: Hohe Konzentration (rot)

## Stresstest

### Szenarien
1. **Fahrzeug-Restwert-Einbruch**: -20 % auf Kfz-Restwerte (z.B. Verbrenner-Verbot)
2. **Massenausfall**: NPL-Quote steigt auf 15 % (Rezession)
3. **Zinssteigerung**: +200 Basispunkte → Refinanzierungskosten steigen
4. **Objektklassen-Wertverlust**: IT -40 % (technologische Disruption)

### Stresstest-Methodik
- Basis: Aktuelles Portfolio (EAD, Laufzeiten, Restwerte)
- Schock: Szenario auf Verwertungserlöse anwenden
- Verlust: Erwartet Loss = EAD × PD × (1 – LGD)

## Regulatorisches Reporting

### CRR/CRD IV (EU 575/2013)
- Finanzierungsleasing: KSA-Risikogewichtung nach Forderungsklasse (Unternehmen 100 %, Verbraucher 75 %)
- IRB: Wenn LG IRB-Ansatz: interne PD/LGD-Schätzungen für Leasingforderungen

### IFRS 9: ECL (Expected Credit Loss)
- Stage 1: 12-Monats-ECL (keine erhebliche Verschlechterung)
- Stage 2: Lifetime-ECL (erhebliche Verschlechterung)
- Stage 3: Lifetime-ECL (Ausfall/NPL)

## Prüfprogramm

1. Portfolio-KPIs aktuell berechnet? NPL-Quote, Rückstand, Restwert-Gap?
2. Konzentrationsrisiken: HHI, Klumpen-LN, Objektklassen?
3. Stresstest durchgeführt? Szenarien definiert und berechnet?
4. IFRS 9: Stage-Klassifizierung aktuell? ECL berechnet?
5. CRR-Meldungen fristgerecht?
6. Management-Reporting: Ampel-Dashboard erstellt?

## Typische Fallen

- NPL-Quote nach zu optimistischer Definition: Tatsächlich höher → Risikokapital unterschätzt
- IFRS 9 Stage-Migration zu spät → Rückstellungen zu niedrig
- Konzentrationsrisiko übersehen: Eine Branche macht 60 % aus → Korrelationsrisiko
- Stresstest mit unrealistischen Szenarien → Management wiegt sich in falscher Sicherheit

## Normen und Quellen

- CRR (EU 575/2013, Capital Requirements Regulation): https://eur-lex.europa.eu
- IFRS 9 (Finanzinstrumente): https://eur-lex.europa.eu
- EBA/GL/2018/06 (NPL-Leitlinien): https://eur-lex.europa.eu
- KWG § 25a (Risikomanagement): https://www.gesetze-im-internet.de/kredwg/__25a.html
- BGH, Urteil vom 28.05.2014 - VIII ZR 179/13 und VIII ZR 241/13 (Restwertgarantie): https://www.bgh.de

## Output-Formate

- **Portfolio-Dashboard**: Excel-Vorlage mit KPIs und Ampelfarben
- **Stresstest-Modell**: Szenarien und Verlustberechnung
- **IFRS-9-Stage-Migration-Tracker**: Monatliche Überprüfung
- **Regulatorisches Reporting**: CRR-Meldung Leasingforderungen
