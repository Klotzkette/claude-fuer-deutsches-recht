---
name: risiko-dashboard-leasingportfolio
description: "Risiko-Dashboard Leasingportfolio: KPIs, Konzentrations- und Restwertrisiken, NPL-Tracking, Stresstest und regulatorisches Reporting im Leasingrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Risiko-Dashboard: Leasingportfolio

## Arbeitsbereich

Risiko-Dashboard Leasingportfolio: KPIs, Konzentrations- und Restwertrisiken, NPL-Tracking, Stresstest und regulatorisches Reporting. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
