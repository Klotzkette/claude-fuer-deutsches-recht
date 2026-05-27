---
name: stb-lohn-arbeitgeber-arbeitnehmer-anteile
description: "Arbeitgeber- und Arbeitnehmer-Anteile in der SV. Anwendungsfall Verteilung der SV-Beitraege zwischen AG und AN PV-Zuschlag Kinderlose KV-Zusatzbeitrag Sonderbeitraege Lohnabrechnung. Methodik AG-AN-Aufteilung in DATEV LODAS. Output Lohnabrechnung mit korrekter Aufteilung."
---

# AG-/AN-Anteile in der Sozialversicherung

## Kernsachverhalt

Die SV-Beitraege werden grundsaetzlich paritaetisch zwischen AG und AN aufgeteilt. Es gibt aber Sonderregelungen: PV-Kinderlosenzuschlag (AN allein), U1/U2-Umlagen (AG allein), Insolvenzgeld-Umlage (AG allein), Berufsgenossenschaft (AG allein), Sachsen-PV-Sonderregelung. Der Steuerberater konfiguriert die Aufteilung im DATEV LODAS / Lohn und Gehalt korrekt.

## Kaltstart-Rueckfragen

1. Welcher Mandant — Standardfall oder Sonderkonstellation?
2. Welche AN-Konstellation (Kinder, Bundesland)?
3. Welche Krankenkassen — Zusatzbeitragssatz individuell?
4. Welche Umlage-Pflichten — U1 (Kleinunternehmer), U2, Insolvenzgeld?
5. Berufsgenossenschaft mit welchem Beitrag?
6. Sondersituation Sachsen-PV?
7. Welche Sonderbeitraege (z.B. zusaetzliche BG)?
8. Welche tarifliche Sonderregelungen?

## Rechtlicher Rahmen

### Primaernormen

**§ 249 SGB V** — KV-Beitragsverteilung.

**§ 168 SGB VI** — RV-Beitragsverteilung.

**§ 346 SGB III** — AV-Beitragsverteilung.

**§ 58 SGB XI** — PV-Beitragsverteilung; § 55 Abs. 3 SGB XI PV-Zuschlag Kinderlose.

**AAG** — U1/U2-Umlage.

**§ 358 SGB III** — Insolvenzgeld-Umlage (Beitrag AG).

### Verwaltungsanweisungen

- Gemeinsame Rundschreiben Spitzenverbaende KK.

## Workflow

### Phase 1 — Standard-Aufteilung

| Zweig | AG-Anteil (typisch) | AN-Anteil (typisch) |
|---|---|---|
| KV allgemein | 7,3 Prozent | 7,3 Prozent |
| KV-Zusatzbeitrag (KK individuell) | halftig (paritaetisch) | halftig |
| PV (allgemein) | halftig | halftig |
| PV-Zuschlag Kinderlose | 0 | 0,6 Prozent (Stand 2025; aktualisieren) |
| PV Sachsen | 1,025 Prozent | 1,025 Prozent (nicht paritaetisch) |
| RV | 9,3 Prozent | 9,3 Prozent |
| AV | aktuell verifizieren | aktuell verifizieren |
| U1 (Kleinunternehmer) | voll AG | 0 |
| U2 (Mutterschaft) | voll AG | 0 |
| Insolvenzgeld-Umlage | voll AG | 0 |
| Berufsgenossenschaft | voll AG | 0 |

(Beitragssaetze 2026 zwingend verifizieren ueber DRV/BMAS/GKV-Spitzenverband.)

### Phase 2 — PV-Kinderlosenzuschlag

- AN ohne Kinder ab 23 Jahre: zusaetzlicher Anteil 0,6 Prozent (Stand 2025; aktueller Wert 2026 verifizieren).
- AN mit Kindern: Abschlag oder Wegfall des Zuschlags.
- Bei mehreren Kindern: gestaffelter Abschlag (Reform 2023 nachgelagert).

### Phase 3 — Sachsen-PV-Sonderregelung

- Sachsen-PV: AN-Anteil hoeher als AG-Anteil (anders als anderswo).
- DATEV LODAS-Stammdaten: Bundesland-Schluessel "Sachsen".

### Phase 4 — KV-Zusatzbeitragssatz

- Jede Krankenkasse erhebt individuellen Zusatzbeitrag.
- Standard-Zusatzbeitragssatz (BMAS-Statistik) ca. 1,7 Prozent (Stand 2024; 2026 verifizieren).
- Bei KK-Wechsel: Umstellung im Lohn-Programm.

### Phase 5 — Umlagen U1/U2

- U1 (Krankheit): nur Kleinunternehmer (bis 30 AN) pflichtig.
- U2 (Mutterschaft): alle AG pflichtig.
- Insolvenzgeld-Umlage: alle AG pflichtig (Ausnahme: Privathaushalte).

### Phase 6 — DATEV LODAS-Konfiguration

- Mandantenstammdaten: Bundesland, BG-Schluessel, U1-Pflicht.
- AN-Stammdaten: Kinderlosen-Status, KK-Wahl.
- Automatische Berechnung der Anteile.

## Output

- Korrekt aufgeteilte SV-Beitraege.
- Lohnabrechnung mit AG- und AN-Anteilen.
- Buchung im Hauptbuch (AG-Anteile als Lohnnebenkosten).

## Strategie und Praxis-Tipps

- PV-Kinderlosenzuschlag und Sachsen-PV sind haeufige Fehlerquellen — sorgfaeltig konfigurieren.
- KV-Zusatzbeitrag KK-individuell — bei KK-Wechsel des AN sofort anpassen.
- BG-Mitgliedschaft regelmaessig aktualisieren (Gefahrtarif-Aenderungen).
- StBVV: Standardkonfiguration in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS automatische Beitragssatz-Aktualisierung zum Jahresbeginn.

## Querverweise

- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-umlage-u1-u2-insogeld-umlage` — Umlagen.
- `stb-lohn-mandantenaufnahme-onboarding` — Onboarding.
- `stb-lohn-lohnsteuer-monatsabschluss` — Monatsabschluss.

## Quellen und Updates

Stand: 05/2026.

- SGB V § 249.
- SGB VI § 168.
- SGB III §§ 346, 358.
- SGB XI §§ 55, 58.
- AAG.
- Verifikations-Hinweis: Beitragssaetze 2026 verifizieren.
- Verifikations-Hinweis: PV-Kinderlosenzuschlag 2026 verifizieren.
