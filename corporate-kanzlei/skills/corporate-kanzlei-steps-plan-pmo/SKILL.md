---
name: corporate-kanzlei-steps-plan-pmo
description: "Steps Plan und Transaktions-PMO fuer M&A-Mandate erstellen: Deal-Team benoetigt Gesamtprojektplan mit Workstream-Koordination, CP-Tracking und Status-Reporting. Normen: SPA Closing Conditions, § 158 BGB. Pruefraster: Workstream-Matrix (Legal, Tax, Financial, Regulatory, Commercial), Zeitplan, CP-Tracker, Weekly-Status-Template. Output Steps-Plan, Workstream-Matrix, CP-Tracker, Weekly-Status-Report. Abgrenzung: Monitoring einzelner Fristen siehe automation-monitoring; Signing-Closing siehe signing-closing-conditions."
---

# Steps Plan und Deal-PMO

## Triage — klaere vor Beginn

1. Transaktionsphase: Pre-Signing, Zwischen Signing und Closing, Post-Closing Integration?
2. Welche Workstreams sind aktiv: Legal, Tax, Financial, Regulatory, Commercial?
3. Wer ist das Core-Deal-Team: federf. Partner, Senior/Junior, Investmentbank, Steuerberater?
4. Signing- und Closing-Zieldaten bekannt? Long Stop Date?
5. Kartellrecht und FDI: Anmeldedaten und Pruefdauern bekannt?
6. Weekly-Meeting Turnus und Status-Report-Empfaenger?

## Zentrale Normen & Fristen

- **§§ 35-43 GWB** — Fusionskontrolle; Phase I 4-6 Wochen; Phase II bis 5 Monate
- **§ 56 AWV** — FDI-Pruefung; Anmeldefrist 2 Monate nach Vertragsschluss; Pruefdauer 4 Monate
- **§§ 158, 162 BGB** — Closing Conditions; Fristen und Bedingungen; treuwidrige Verhinderung
- **§ 41 GWB** — Vollzugsverbot; gun jumping; Bussgeld bis 10 % Weltumsatz
- **Art. 7 FKVO** — EU-Vollzugsverbot

## Aktuelle Rechtsprechung

- BGH, Urt. v. 21.06.2019 - V ZR 244/17, NJW 2019, 2988 — CP-Owner-Pflicht: Partei muss aktiv fuer Erfullung der aufschiebenden Bedingung eintreten; reine Abwarteposition genuegt nicht
- OLG Frankfurt, Urt. v. 13.10.2021 - 4 U 162/20, NZG 2022, 213 — Kaeufer muss Kartell-Freigabe aktiv befoerdern; passive Haltung verletzt Kooperationspflicht im SPA

## Kommentarliteratur

- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 9 — Deal-PMO und Closing
- Beisel/Klumpp, Unternehmenskauf (7. Aufl. 2016) Kap. 11 — Transaktionsmanagement

## Steps Plan Struktur

Ein Steps Plan listet alle Aktionen zur vollstaendigen Transaktionsdurchfuehrung:

| Schritt | Beschreibung | Owner | Abhaengigkeit | Datum |
|---|---|---|---|---|
| 1 | Term Sheet / LOI unterzeichnen | Deal-Team | — | [Datum] |
| 2 | NDA unterzeichnen | Beide Parteien | — | [Datum] |
| 3 | DD starten (Legal, Tax, FIN, COM) | DD-Teams | NDA | [Datum] |
| 4 | DD-Reports finalisieren | Workstream-Leads | DD-Daten | [Datum] |
| 5 | SPA-Entwurf erstellen | Legal Team | DD-Reports | [Datum] |
| 6 | SPA verhandeln | Parteien / Anwaelte | SPA-Entwurf | [Datum] |
| 7 | Signing | Parteien, Notar | Alle CPs pre-Signing | [Datum] |
| 8 | Kartellrecht anmelden | Kaeufer / Legal | Signing | [Datum] |
| 9 | FDI-Anmeldung | Kaeufer / Legal | Signing | [Datum] |
| 10 | CP-Tracking und Monitoring | PMO | Laufend | Bis Closing |
| 11 | Closing | Notar, Parteien | Alle CPs erfuellt | [Datum] |
| 12 | Post-Closing-Massnahmen | PMO, Recht, Tax | Closing | [Datum] |

## Weekly-Status-Report Vorlage

```
WEEKLY DEAL-STATUS-REPORT
Transaktion: [DEAL-NAME]
KW: [Nr.] / Datum: [DATUM]
Erstellt von: [PMO-Lead]

1. AMPELSTATUS: [GRUEN / GELB / ROT]
   GRUEN: Alle Workstreams planmaessig
   GELB: [Beschreibung des Problems / Risikos]
   ROT: [Kritisches Problem; sofortige Eskalation]

2. MILESTONE-STATUS
   | Milestone | Faellig | Status | Naechste Aktion |
   |-----------|---------|--------|----------------|
   | Signing | [Datum] | [On track / Delayed] | [Massnahme] |
   | Kartellfreigabe | [Datum] | [Angemeldet / Phase I] | [Follow-up] |
   | FDI-Nichtuntersagung | [Datum] | [Angemeldet] | [...] |
   | Closing | [Datum] | [Auf Kurs] | [...] |

3. WORKSTREAM-STATUS
   | Workstream | Lead | Status | Offene Punkte |
   |-----------|------|--------|---------------|
   | Legal DD | [Name] | Abgeschlossen | Litigation-Frage offen |
   | Tax DD | [Name] | 90 % | Betriebspruefungs-Details ausstehend |
   | Regulatory | [Name] | Phase I | BKartA-Rueckfrage am [Datum] |

4. RISIKEN
   | Risiko | Eintrittswahr. | Auswirkung | Massnahme |
   |--------|----------------|-----------|-----------|
   | [Risiko 1] | [%] | [Hoch] | [Massnahme] |

5. ENTSCHEIDUNGSBEDARF
   - [Offener Punkt] → Entscheidung durch [NAME] bis [DATUM]

6. NAECHSTE WOCHE
   | Aktion | Owner | Datum |
   |--------|-------|-------|
   | [Aktion 1] | [Name] | [Datum] |
```

## Schritt-fuer-Schritt-Workflow

1. **Kickoff-Meeting** — alle Workstream-Leads; Steps Plan erstellen; Rollen klaeren
2. **Steps Plan finalisieren** — Abhaengigkeiten kartieren; kritischer Pfad identifizieren
3. **Wochentakt** — Weekly-Call; Status-Update; Risiken; Entscheidungen
4. **CP-Tracker fuehren** — taeglich aktualisieren; Ampelstatus; Eskalation
5. **Signing-Vorbereitung** — Pre-Closing-Checkliste 1 Woche vorher; alles checken
6. **Closing-Koordination** — Notartermin; Kaufpreis-Zahlung; Deliverables-Exchange
7. **Post-Closing-Protokoll** — Closing-Bestaetigung; PMI-Plan uebergeben

## Output-Template Workstream-Matrix

```
WORKSTREAM-MATRIX
Transaktion: [DEAL-NAME]
Stand: [DATUM]

| Workstream | Lead Kaeufer | Lead Verkaefer | Scope | Status |
|-----------|-------------|---------------|-------|--------|
| Legal DD | [Name, Kanzlei] | [Name, Kanzlei] | Full Scope | [%] |
| Tax DD | [Steuerberater] | [Steuerberater] | Full | [%] |
| Financial DD | [WP-Gesellschaft] | — | Limited | [%] |
| SPA-Verhandlung | [Name] | [Name] | Full | [Version] |
| Regulatory | [Name] | [Name] | Kartell, FDI | Phase I |
| HR/PMI | [Name] | [Name] | Post-Closing | Nicht gestartet |
```

## Rote Schwellen

- Steps Plan ohne kritischen Pfad → Zeitplan-Fehler bei Abhaengigkeiten nicht erkannt
- Kein Weekly-Meeting → Workstream-Divergenz; unerkannte Risiken
- CP-Tracker veraltet → Closing-Ueberraschung bei nicht erfuellter Bedingung
- Gun-Jumping wegen falscher Timeline → § 41 GWB; Bussgeld
- PMI-Plan fehlt → Post-Closing-Chaos; Vertragspflichten verpasst

## Quellen

- §§ 35-43 GWB; § 56 AWV; §§ 158, 162 BGB; Art. 7 FKVO
- BGH V ZR 244/17 (CP-Owner-Pflicht); OLG Frankfurt 4 U 162/20 (Kartell-Foerderpflicht)
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 9
