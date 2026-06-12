---
name: lohn-direktversicherung-3-nr-63-estg
description: "Direktversicherung Steuerfreiheit § 3 Nr 63 EStG bis 8 Prozent BBG SV-frei bis 4 Prozent BBG. Anwendungsfall Entgeltumwandlung Direktversicherung Konfiguration Mandant AG-Zuschuss 15 Prozent. Methodik Beitragsberechnung Beitragsbemessung Auswirkung Netto. Output Lohn-Konfiguration mit Direktversi..."
---

# Direktversicherung — § 3 Nr. 63 EStG

## Fachlicher Anker

- **Normen:** § 3 Nr. 63 EStG, § 6a, § 1a.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Die Direktversicherung ist der haeufigste bAV-Durchfuehrungsweg: AG schliesst einen Versicherungsvertrag für den AN ab. Beitraege bis 8 Prozent der RV-BBG (West) sind steuerfrei (§ 3 Nr. 63 EStG), bis 4 Prozent BBG SV-frei. Beim AN reduziert sich das Bruttolohn um den Beitrag, in der Auszahlungsphase ist die Rente lohnsteuerpflichtig (nachgelagerte Besteuerung). Der Steuerberater konfiguriert die Direktversicherung in DATEV LODAS und prüft die Schwellen.

## Kaltstart-Rueckfragen

1. Welche Versicherungsgesellschaft? Liegt Vertrag vor?
2. Welcher monatliche Beitrag?
3. Erfolgt durch Entgeltumwandlung (AN-Beitrag aus Brutto) oder AG-Finanzierung (zusaetzlich)?
4. AG-Zuschuss 15 Prozent nach § 1a BetrAVG vorgesehen?
5. Welcher Bruttolohn des AN (BBG-Prüfung)?
6. Sind bereits Vorvertraege über bAV vorhanden (kumulierte 8-Prozent-Prüfung)?
7. Wann erfolgt voraussichtlicher Renteneintritt?
8. Welche Sondersituation (Pensionsfonds-Wechsel, Beitragsfreistellung)?

## Rechtlicher Rahmen

### Primaernormen

**§ 3 Nr. 63 EStG** — Steuerfreiheit Beitraege bAV bis 8 Prozent BBG.

**§ 1a BetrAVG** — Entgeltumwandlungs-Anspruch und 15-Prozent-Zuschuss.

**§ 1 Abs. 1 Nr. 9 SvEV** — SV-Freiheit bAV-Beitraege bis 4 Prozent BBG-West RV (kumuliert).

**§ 19 EStG** — Versorgungsbezuege Auszahlung.

**§ 40b EStG a.F.** — Pauschalbesteuerung (Altvertraege bis 31.12.2004).

### Verwaltungsanweisungen

- BMF v. 06.12.2017.
- BMF v. 18.03.2022 (BRSG-Reform).
- LStR.

## Workflow

### Phase 1 — Förderungs-Grenzen

| Grenze | Wert (Stand 2025) | Wirkung |
|---|---|---|
| 8 Prozent BBG-West RV | 7.728 EUR/Jahr (BBG-West RV 2025: 96.600 EUR; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel prüfen) | LSt-frei |
| 4 Prozent BBG-West RV | ca. 3.864 EUR/Jahr (2024) | SV-frei (zusaetzlich zur LSt-Freiheit) |
| Darueber hinaus | Vollversteuerung; SV-Pflicht | Wie regulaerer Lohn |

**Zahlenbeispiel (Stand 2024-Werte):** AN mit Entgeltumwandlung 200 EUR/Monat in Direktversicherung = 2.400 EUR/Jahr. Liegt unter 4-Prozent-BBG (3.864 EUR) — voll LSt- UND SV-frei. AG erspart SV-AG-Anteil und muss daher 15 Prozent Pflichtzuschuss nach § 1a BetrAVG leisten (= 30 EUR/Monat).

(BBG-Werte 2025: West RV 96.600 EUR/Jahr; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel prüfen.)

### Phase 2 — Vergleich Entgeltumwandlung vs. AG-Finanzierung

- Entgeltumwandlung: AN-Beitrag aus Brutto; AG spart SV-Beitraege; § 1a BetrAVG 15-Prozent-Zuschuss-Pflicht.
- AG-Finanzierung: zusaetzlich zum Lohn; volle Förderung § 3 Nr. 63 EStG; § 100 EStG für Geringverdiener.

### Phase 3 — § 1a BetrAVG 15-Prozent-Zuschuss

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Geltung Direktversicherung/Pensionskasse/Pensionsfonds (nicht Direktzusage).
- Seit 2019; für Altvertraege bis Ende 2021 noch Uebergangsregelung; seit 2022 voll wirksam.

### Phase 4 — Lohnabrechnung-Konfiguration

- DATEV LODAS: Konto für Direktversicherung anlegen.
- Beitrag aus Brutto reduzieren (Entgeltumwandlung) oder zusaetzlich (AG-Finanzierung).
- LSt-frei bis 8 Prozent BBG.
- SV-frei bis 4 Prozent BBG.
- Buchung im Hauptbuch (Konto 4380 oder 6380 SKR 03).

### Phase 5 — Auszahlungsphase

- Rente lohnsteuerpflichtig (nachgelagerte Besteuerung) nach § 22 Nr. 5 EStG (Vertrag der bAV) bzw. § 19 EStG (bei Direktzusage / Unterstuetzungskasse).
- KV/PV-Beitragspflicht in der KVdR (Freibetrag für Pflichtversicherte Rentner nach § 226 Abs. 2 SGB V; aktuellen Freibetrag über GKV-Spitzenverband prüfen).
- Bei Kapitalauszahlung Sondertarif § 34 Abs. 2 Nr. 4 i.V.m. § 24 Nr. 1 EStG Fuenftel-Regel prüfen — Voraussetzung: Zusammenballung in einem Veranlagungszeitraum.

### Phase 6 — Bei Insolvenz

- Direktversicherung mit Sicherungsmechanismus durch Versicherungsaufsicht.
- Bei Insolvenz des AG: AN-Anspruch bleibt (Vertragsuebertragung an AN möglich).
- PSVaG (Pensions-Sicherungs-Verein) bei Direktzusage relevant, NICHT bei Direktversicherung.

## Strategie und Praxis-Tipps

- 4-Prozent-SV-Grenze prüfen — daruber LSt-frei, aber SV-pflichtig.
- AG-Zuschuss 15 Prozent ist GESETZLICHE PFLICHT — bei Entgeltumwandlung nicht verhandelbar.
- Bei Altvertraegen (vor 2005) § 40b EStG a.F. pauschal versteuert; in Auszahlung anders behandelt.
- Bei Wechsel des AG: Vertrag uebertragen lassen, sonst Beitragsfreistellung.
- StBVV: in Lohnpauschale; Beratung Direktversicherungs-Wahl Zusatzauftrag.
- DATEV-Tipp: DATEV LODAS Direktversicherungs-Modul mit Versicherer-Schnittstelle (z.B. Allianz, R+V).

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 3 Nr. 63, 19, 22 Nr. 5, 34, 40b a.F.
- BetrAVG §§ 1, 1a.
- SvEV § 1 Abs. 1 Nr. 9.
- BMF v. 06.12.2017 (IV C 5 - S 2333/17/10002), v. 18.03.2022 (IV C 5 - S 2333/19/10005).
- BBG-West RV 2025: 96.600 EUR; 8 Prozent = 7.728 EUR LSt-frei; 4 Prozent = 3.864 EUR SV-frei (Sozialversicherungs-Rechengroessenverordnung 2026 prüfen).

<!-- AUDIT 27.05.2026 | welle 6 | 6 Marker aufgeloest: 4 bestaetigt (BBG 2025 eingesetzt, BMF-GZ recherchiert), 2 ersetzt (Prüfhinweise ohne Marker) -->
