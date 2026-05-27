---
name: stb-lohn-sv-beitraege-grundlagen
description: "Sozialversicherungs-Beitraege Grundlagen RV KV PV AV Umlagen. Anwendungsfall monatliche Lohnabrechnung mit SV-Berechnung Beitragsbemessungsgrenzen AG-AN-Aufteilung Sonderfaelle. Methodik Beitragsberechnung mit JAEG BBG Zusatzbeitrag KV. Output Pruefraster SV-Beitraege."
---

# SV-Beitraege Grundlagen — RV KV PV AV und Umlagen

## Kernsachverhalt

Die Sozialversicherung umfasst vier Hauptzweige: Rentenversicherung (RV), Krankenversicherung (KV), Pflegeversicherung (PV), Arbeitslosenversicherung (AV). Hinzu kommen Umlagen U1 (Krankheit), U2 (Mutterschaft), U3 (Insolvenzgeld) und ggf. Berufsgenossenschaft. Die Beitragsberechnung erfolgt prozentual vom Bruttolohn bis zur Beitragsbemessungsgrenze (BBG); ueber BBG beitragsfrei.

## Kaltstart-Rueckfragen

1. SV-Status des AN — versicherungspflichtig, gerinfgfuegig, kurzfristig, Werkstudent, freiwillig versichert?
2. Bruttolohn ueber JAEG (Jahresarbeitsentgeltgrenze) KV — Wechsel in PKV moeglich?
3. Bruttolohn ueber BBG — Beitragsfrei oberhalb?
4. PV: Kind oder kinderlos (Kinderlosenzuschlag)?
5. KV: Wahl Krankenkasse, Zusatzbeitragssatz individuell?
6. Bundesland: Beitragssatz PV unterschiedlich (Saarland anders)?
7. Sondersituation: Mehrfachbeschaeftigung, Bezug Arbeitslosengeld, Saison-AN?
8. Berufsgenossenschaft: Gefahrtarif, Beitragsklasse?

## Rechtlicher Rahmen

### Primaernormen

**SGB IV §§ 14, 17, 18** — Arbeitsentgelt, Pauschalierungen, BBG.

**SGB V** — Krankenversicherung.

**SGB VI** — Rentenversicherung.

**SGB XI** — Pflegeversicherung.

**SGB III** — Arbeitsfoerderung (AV).

**§ 7 SGB IV** — Beschaeftigung.

**§ 8 SGB IV** — geringfuegige Beschaeftigung.

**§ 28d SGB IV** — Gesamt-SV-Beitrag.

**§ 28e SGB IV** — Beitragspflicht AG.

### Verwaltungsanweisungen

- Gemeinsame Rundschreiben Spitzenverbaende KK.
- Sachbezugswerte-Verordnung (jaehrliche Anpassung).
- BMF/BMAS Rundschreiben.

## Workflow

### Phase 1 — BBG und Beitragssaetze 2026 (verifizieren)

| Zweig | West/Ost | BBG (verifizieren) | Beitragssatz (verifizieren) |
|---|---|---|---|
| RV | West/Ost | aktuelle BBG 2026 verifizieren | 18,6 Prozent (oder aktuell verifizieren) |
| AV | West/Ost | gleich RV-BBG | aktuell verifizieren |
| KV | bundeseinheitlich | JAEG / BBG verifizieren | allgemein 14,6 + Zusatzbeitrag (KK-individuell) |
| PV | bundeseinheitlich | BBG KV | aktuell verifizieren; Kinderlosenzuschlag aktuell verifizieren |

(Saemtliche Werte sind in den Lohnabrechnungs-Programmen hinterlegt; bei Mandantengespraech aktuelle Werte 2026 verifizieren ueber DRV, GKV-Spitzenverband, BMAS.)

### Phase 2 — Beitragsaufteilung AG/AN

- Grundsatz: halbe-halbe Aufteilung.
- PV-Zuschlag Kinderlose: 0,6 Prozent (Stand 2025 verifizieren fuer 2026) zu Lasten AN allein.
- KV-Zusatzbeitrag: in der Regel paritaetisch.
- U1 (Krankheit): nur AG.
- U2 (Mutterschaft): nur AG.
- Insolvenzgeld-Umlage: nur AG.
- Berufsgenossenschaft: nur AG.

### Phase 3 — Sonderfaelle

| Sonderfall | SV-Behandlung |
|---|---|
| Minijob (538 EUR-Grenze, Stand 01.01.2024 — bei MiLo-Anhebung dynamisch) | Pauschal 30 Prozent (15 RV + 13 KV + 2 LSt) |
| Werkstudent | Nur RV-Pflicht, keine KV/AV (sofern Werkstudent-Status) |
| Aushilfskraft kurzfristig (max. 3 Monate / 70 Tage) | SV-frei (nur KSt-Pauschal) |
| Gesellschafter-GF GmbH | SV-Pflichtfrage einzelfallabhaengig |
| Pensionaer | Nur KV/PV; RV und AV befreit |
| Mehrfachbeschaeftigung | Beitragspflicht nur ein Mal bis BBG |

### Phase 4 — JAEG und KV-PV-Wahl

- JAEG (Jahresarbeitsentgeltgrenze) ueber 3 Jahre ueberschritten: AN kann in PKV wechseln.
- JAEG 2026 verifizieren (BMAS).
- Wechsel-Pruefung gemeinsam mit AN, ggf. AG-Zuschuss zur PKV.

### Phase 5 — Berufsgenossenschaft

- Gefahrtarif je nach Branche.
- Beitragssatz Promille der Lohnsumme.
- Jaehrlicher Lohnnachweis im Februar des Folgejahres.
- BG-Mitglied im StB-Stammblatt erfassen.

### Phase 6 — Buchung und Abrechnung

- SV-AG-Anteil als Lohnnebenkosten (Konto 4138/4140 SKR 03).
- SV-AN-Anteil als Abzug vom Brutto.
- Gesamtsumme an Krankenkasse (Gesamt-SV-Beitrag).
- Faelligkeit: drittletzter Bankarbeitstag des laufenden Monats (§ 23 Abs. 1 SGB IV).

## Output

- SV-Berechnung im DATEV LODAS / Lohn und Gehalt.
- AG-AN-Aufteilung pruefen.
- Pauschalbetraege Minijob separat.
- Buchung im Hauptbuch.

## Strategie und Praxis-Tipps

- SV-Faelligkeit drittletzter Bankarbeitstag — bei Verspaetung Saeumniszuschlag, ab 1 Jahr § 266a StGB-Risiko (Vorenthalten SV-Beitraege).
- BBG und Beitragssaetze jaehrlich pruefen — DATEV-Updates zum 1. Januar Pflicht.
- Bei Werkstudent: Status pruefen (20-Stunden-Regel; in der vorlesungsfreien Zeit ggf. mehr).
- Bei Mehrfachbeschaeftigung: AG-Pflicht zur Pruefung der BBG-Ueberschreitung.
- StBVV: SV-Berechnung in Lohnpauschale; komplexe Sonderfaelle (Werkstudent-Pruefung) Zeithonorar.
- DATEV-Tipp: DATEV LODAS mit automatischen Beitragssatz-Updates; Plausibilitaets-Pruefung Beitragssumme.

## Querverweise

- `stb-lohn-lohnsteuer-monatsabschluss` — Monatsabschluss.
- `stb-lohn-arbeitgeber-arbeitnehmer-anteile` — AG-AN-Anteile.
- `stb-lohn-umlage-u1-u2-insogeld-umlage` — Umlagen.
- `stb-lohn-minijob-538-euro-2024-anpassung` — Minijob.
- `stb-lohn-werkstudent-pauschalen` — Werkstudent.
- `stb-lohn-berufsgenossenschaft-bg-meldung-jahresende` — BG.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 7, 8, 14, 17, 18, 23, 28d, 28e.
- SGB V, VI, XI, III.
- Gemeinsame Rundschreiben Spitzenverbaende KK.
- StGB § 266a.
- Verifikations-Hinweis: BBG, JAEG, Beitragssaetze 2026 ueber DRV/BMAS/GKV-Spitzenverband.
- Verifikations-Hinweis: PV-Kinderlosenzuschlag aktuell verifizieren (Reform 2023 nachgelagert).
