---
name: stb-bwa-soll-ist-vergleich
description: "Soll-Ist-Vergleich in der BWA. Anwendungsfall Monats- oder Quartals-BWA mit Plan-Werten aus Wirtschaftsplan Unternehmensplanung Forecast. Methodik Planeingabe Abweichungsanalyse Steuerungsempfehlung. Output BWA mit Spalte Plan Ist Abweichung Erlaeuterungstext für Mandant Querverweis stb-bwa-mandantenreport-monatlich."
---

# Soll-Ist-Vergleich in der BWA

## Kernsachverhalt

Der Soll-Ist-Vergleich legt unterjaehrige Planwerte des Mandanten neben die tatsaechlich gebuchten Werte und zeigt Abweichungen. Er ist Voraussetzung fuer professionelles Controlling und wird besonders bei groesseren Mandanten, Bankreporting und Sanierungsmandaten erwartet. Der Steuerberater leitet den Mandanten beim Aufstellen des Plans an und integriert die Werte in das DATEV/Addison-System.

## Kaltstart-Rueckfragen

1. Liegt ein Wirtschaftsplan / Budget des Mandanten vor, oder muss er erst erstellt werden?
2. Detailgrad des Plans — Jahres-Plan, Quartals-Plan, Monats-Plan?
3. Welche Position muss geplant werden — nur Umsatz und EBIT, oder gesamte GuV?
4. Welche Annahmen gelten — Preise, Mengen, Tarife, Personalentwicklung?
5. Liegen historische Daten fuer Plausibilitaet vor (mindestens 12 Monate)?
6. Reportingzweck — interne Steuerung, Bankgespraech, Investorenreport, Konzernreporting?
7. Wie oft wird der Plan ueberarbeitet (rollierend, Quartal, Jahr)?
8. Wer ist Plan-Verantwortlicher beim Mandanten (GF, kfm. Leitung, externer Berater)?

## Rechtlicher Rahmen

### Primaernormen

**§ 1 StaRUG** — Krisenfrueherkennung der Geschaeftsleitung; Planung ist Pflichtbestandteil.

**§ 91 Abs. 2 AktG / analog GmbH** — Ueberwachungs- und Risikomanagementsystem.

**§ 252 HGB** — Going-concern; positive Fortbestehensprognose setzt belastbaren Plan voraus.

**§ 19 Abs. 2 InsO** — Fortbestehensprognose; Prognosezeitraum (regulaer 12 Monate; durch SanInsKG zeitweise auf vier Monate verkuerzt). Aktuelle Geltungsdauer der SanInsKG-Verkuerzung in juris pruefen.

### Standards

- IDW S 6 — Anforderungen an Sanierungskonzepte (integrierter Finanzplan).
- IDW S 11 — Beurteilung Insolvenzeroeffnungsgruende.
- IDW PS 305 — Pruefung Risikofrueherkennungssystem § 91 Abs. 2 AktG.

## Workflow

### Phase 1 — Planbasis bereitstellen

- Wenn kein Plan vorhanden: Mandant zur Erstellung anleiten oder eigenstaendig erstellen lassen (StBVV-Zusatzauftrag § 35).
- Datengrundlage: Historische Werte (12-36 Monate) als Ausgangsbasis.
- Annahmen schriftlich dokumentieren: Umsatzwachstum, Preisentwicklung, Personalplanung, Investitionsplanung.
- Plan auf Jahres-, Quartals- und Monatsebene herunterbrechen (Top-down oder Bottom-up).

### Phase 2 — Planeingabe in DATEV/Addison

- DATEV: Plan-Werte ueber DATEV Kanzlei-Rechnungswesen → Plan-Stammdaten erfassen.
- Addison: Budget-Modul aktivieren, Werte einlesen.
- Saisonalitaet abbilden: Jahresplan auf 12 Monate verteilen mit branchentypischen Schwankungsmustern.
- Plausibilitaetspruefung: Plan-Werte mit Vorjahres-Ist abgleichen.

### Phase 3 — Monatliche Soll-Ist-Auswertung

- BWA-Form mit Spalten konfigurieren: Plan, Ist, Abweichung absolut, Abweichung in Prozent.
- Kumulierter Year-to-Date-Vergleich Plan vs. Ist parallel.
- Periodengerecht abgrenzen — auch der Plan muss saisonbereinigt sein.

### Phase 4 — Abweichungsanalyse

| Abweichung | Bewertung | Handlungsbedarf |
|---|---|---|
| < 5 Prozent | Normaler Streubereich | Beobachten |
| 5-15 Prozent | Signifikante Abweichung | Ursache klaeren, Mandant ansprechen |
| > 15 Prozent | Wesentliche Abweichung | Bericht an GF, ggf. Planrevision |
| > 25 Prozent ueber mehrere Monate | Krisensignal | stb-bwa-sus-bilanz-pruefung pruefen |

### Phase 5 — Planrevision

- Bei groesseren Abweichungen ueber 2-3 Monate: Plan-Revision erforderlich.
- Mandant in Entscheidung einbinden — keine eigenmaechtige Planaenderung ohne Mandantenfreigabe.
- Dokumentation der Planaenderungen in Mandantenakte mit Datum und Begruendung.

### Phase 6 — Reporting an externe Stakeholder

- Bei Banken-Reporting: Plan-Ist-Bericht mit Erlaeuterung und Gegenmassnahmen.
- Bei Konzernreporting: Konzern-Reporting-Form (oft UKV-Format, internationale Lesart).
- Sanierungsmandate: Plan-Ist als Teil des IDW-S-6-Reports.

## Output

- BWA mit Plan-Ist-Vergleich (Monat und kumuliert).
- Abweichungsanalyse mit Erlaeuterungen.
- Planrevisions-Vorschlag bei wesentlichen Abweichungen.
- Bericht an externe Stakeholder (Bank, Investor, Konzern).

## Strategie und Praxis-Tipps

- Plan-Ist macht nur Sinn, wenn der Plan ernsthaft erarbeitet wurde — sonst wird der Vergleich Spielerei.
- Mindestens Quartalsweise Planrevision; rollierende Forecasts (Quartal + 4-Quartals-Horizont) sind heute Standard.
- Bei sanierungsbeduerftigen Mandanten: Plan ist Pflichtbestandteil der Fortbestehensprognose nach § 19 InsO und IDW S 6.
- Honorar fuer Plan-Erstellung gesondert vereinbaren — die Buchfuehrungspauschale deckt das nicht ab.
- Bei wesentlichen Abweichungen: Mandantengespraech terminieren, nicht nur per E-Mail kommunizieren.
- DATEV-Tipp: Plan-Stammdaten zentral pflegen, damit die BWA automatisch Plan-Spalten ausweist.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — Vorjahresvergleich.
- `stb-bwa-mandantenreport-monatlich` — Mandantenreport.
- `stb-liquiditaetsvorschau-3-6-12-monate` — Liquiditaetsplanung.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 252, 265.
- StaRUG § 1.
- InsO § 19 (Prognosezeitraum 12 Monate; die SanInsKG-Sonderregelung mit verkuerztem 4-Monats-Zeitraum galt befristet vom 09.11.2022 bis 31.12.2023 und ist ausgelaufen; es gilt wieder der gesetzliche Standard-Prognosezeitraum von 12 Monaten).
- IDW S 6, IDW S 11, IDW PS 305.
- DATEV Kanzlei-Rechnungswesen Plan-Modul.
- Addison Budget-Modul.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 bestaetigt (SanInsKG-Sonderregelung ausgelaufen 31.12.2023, Standardzeitraum 12 Monate bestaetigt) -->
