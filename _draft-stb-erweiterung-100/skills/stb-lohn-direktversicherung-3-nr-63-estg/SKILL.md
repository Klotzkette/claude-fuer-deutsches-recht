---
name: stb-lohn-direktversicherung-3-nr-63-estg
description: "Direktversicherung Steuerfreiheit § 3 Nr 63 EStG bis 8 Prozent BBG SV-frei bis 4 Prozent BBG. Anwendungsfall Entgeltumwandlung Direktversicherung Konfiguration Mandant AG-Zuschuss 15 Prozent. Methodik Beitragsberechnung Beitragsbemessung Auswirkung Netto. Output Lohn-Konfiguration mit Direktversicherung."
---

# Direktversicherung — § 3 Nr. 63 EStG

## Kernsachverhalt

Die Direktversicherung ist der haeufigste bAV-Durchfuehrungsweg: AG schliesst einen Versicherungsvertrag fuer den AN ab. Beitraege bis 8 Prozent der RV-BBG (West) sind steuerfrei (§ 3 Nr. 63 EStG), bis 4 Prozent BBG SV-frei. Beim AN reduziert sich das Bruttolohn um den Beitrag, in der Auszahlungsphase ist die Rente lohnsteuerpflichtig (nachgelagerte Besteuerung). Der Steuerberater konfiguriert die Direktversicherung in DATEV LODAS und prueft die Schwellen.

## Kaltstart-Rueckfragen

1. Welche Versicherungsgesellschaft? Liegt Vertrag vor?
2. Welcher monatliche Beitrag?
3. Erfolgt durch Entgeltumwandlung (AN-Beitrag aus Brutto) oder AG-Finanzierung (zusaetzlich)?
4. AG-Zuschuss 15 Prozent nach § 1a BetrAVG vorgesehen?
5. Welcher Bruttolohn des AN (BBG-Pruefung)?
6. Sind bereits Vorvertraege ueber bAV vorhanden (kumulierte 8-Prozent-Pruefung)?
7. Wann erfolgt voraussichtlicher Renteneintritt?
8. Welche Sondersituation (Pensionsfonds-Wechsel, Beitragsfreistellung)?

## Rechtlicher Rahmen

### Primaernormen

**§ 3 Nr. 63 EStG** — Steuerfreiheit Beitraege bAV bis 8 Prozent BBG.

**§ 1a BetrAVG** — Entgeltumwandlungs-Anspruch und 15-Prozent-Zuschuss.

**§ 22 SGB IV** — SV-Behandlung bAV-Beitraege.

**§ 19 EStG** — Versorgungsbezuege Auszahlung.

**§ 40b EStG a.F.** — Pauschalbesteuerung (Altvertraege bis 31.12.2004).

### Verwaltungsanweisungen

- BMF v. 06.12.2017.
- BMF v. 18.03.2022 (BRSG-Reform).
- LStR.

## Workflow

### Phase 1 — Foerderungs-Grenzen

| Grenze | Wert (typisch derzeit ca.; 2026 verifizieren) | Wirkung |
|---|---|---|
| 8 Prozent BBG-West RV | ca. 7.728 EUR/Jahr (BBG-West RV 96.600 EUR fuer 2024 — Stand 2026 zwingend ueber DRV/BMAS-Sozialversicherungs-Rechengroessenverordnung verifizieren) | LSt-frei |
| 4 Prozent BBG-West RV | ca. 3.864 EUR/Jahr (2024) | SV-frei (zusaetzlich zur LSt-Freiheit) |
| Darueber hinaus | Vollversteuerung; SV-Pflicht | Wie regulaerer Lohn |

**Zahlenbeispiel (Stand 2024-Werte):** AN mit Entgeltumwandlung 200 EUR/Monat in Direktversicherung = 2.400 EUR/Jahr. Liegt unter 4-Prozent-BBG (3.864 EUR) — voll LSt- UND SV-frei. AG erspart SV-AG-Anteil und muss daher 15 Prozent Pflichtzuschuss nach § 1a BetrAVG leisten (= 30 EUR/Monat).

(2026 BBG-Werte und Hoechstgrenzen zwingend ueber Sozialversicherungs-Rechengroessenverordnung verifizieren.)

### Phase 2 — Vergleich Entgeltumwandlung vs. AG-Finanzierung

- Entgeltumwandlung: AN-Beitrag aus Brutto; AG spart SV-Beitraege; § 1a BetrAVG 15-Prozent-Zuschuss-Pflicht.
- AG-Finanzierung: zusaetzlich zum Lohn; volle Foerderung § 3 Nr. 63 EStG; § 100 EStG fuer Geringverdiener.

### Phase 3 — § 1a BetrAVG 15-Prozent-Zuschuss

- Bei Entgeltumwandlung: AG muss 15 Prozent des Beitrags zuschiessen, wenn er SV-Beitraege erspart.
- Geltung Direktversicherung/Pensionskasse/Pensionsfonds (nicht Direktzusage).
- Seit 2019; fuer Altvertraege bis Ende 2021 noch Uebergangsregelung; seit 2022 voll wirksam.

### Phase 4 — Lohnabrechnung-Konfiguration

- DATEV LODAS: Konto fuer Direktversicherung anlegen.
- Beitrag aus Brutto reduzieren (Entgeltumwandlung) oder zusaetzlich (AG-Finanzierung).
- LSt-frei bis 8 Prozent BBG.
- SV-frei bis 4 Prozent BBG.
- Buchung im Hauptbuch (Konto 4380 oder 6380 SKR 03).

### Phase 5 — Auszahlungsphase

- Rente lohnsteuerpflichtig (nachgelagerte Besteuerung) nach § 19 EStG.
- KV/PV-Beitragspflicht (Freibetrag fuer Pflichtversicherte aktuell 2026 verifizieren).
- Bei Kapitalauszahlung Sondertarif § 34 EStG Fuenftel-Regel pruefen.

### Phase 6 — Bei Insolvenz

- Direktversicherung mit Sicherungsmechanismus durch Versicherungsaufsicht.
- Bei Insolvenz des AG: AN-Anspruch bleibt (Vertragsuebertragung an AN moeglich).
- PSVaG (Pensions-Sicherungs-Verein) bei Direktzusage relevant, NICHT bei Direktversicherung.

## Output

- Konfigurierte Direktversicherung in DATEV LODAS.
- Lohnabrechnung mit korrektem Sachbezug.
- AG-Zuschuss 15 Prozent dokumentiert.

## Strategie und Praxis-Tipps

- 4-Prozent-SV-Grenze pruefen — daruber LSt-frei, aber SV-pflichtig.
- AG-Zuschuss 15 Prozent ist GESETZLICHE PFLICHT — bei Entgeltumwandlung nicht verhandelbar.
- Bei Altvertraegen (vor 2005) § 40b EStG a.F. pauschal versteuert; in Auszahlung anders behandelt.
- Bei Wechsel des AG: Vertrag uebertragen lassen, sonst Beitragsfreistellung.
- StBVV: in Lohnpauschale; Beratung Direktversicherungs-Wahl Zusatzauftrag.
- DATEV-Tipp: DATEV LODAS Direktversicherungs-Modul mit Versicherer-Schnittstelle (z.B. Allianz, R+V).

## Querverweise

- `stb-lohn-betriebliche-altersversorgung-grundlagen` — bAV-Grundlagen.
- `stb-lohn-bav-doppelversorgung-foerderung` — Doppelfoerderung.
- `stb-lohn-vermoegenswirksame-leistungen` — VL.
- `stb-lohn-sv-beitraege-grundlagen` — SV.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 3 Nr. 63, 19, 22 Nr. 5, 34, 40b a.F.
- BetrAVG §§ 1, 1a.
- SGB IV § 22.
- SvEV.
- BMF v. 06.12.2017, v. 18.03.2022.
- Verifikations-Hinweis: BBG 2026 verifizieren.
