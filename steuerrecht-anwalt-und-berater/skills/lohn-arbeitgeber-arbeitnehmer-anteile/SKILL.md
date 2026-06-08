---
name: lohn-arbeitgeber-arbeitnehmer-anteile
description: "Arbeitgeber- und Arbeitnehmer-Anteile in der SV. Anwendungsfall Verteilung der SV-Beitraege zwischen AG und AN PV-Zuschlag Kinderlose KV-Zusatzbeitrag Sonderbeitraege Lohnabrechnung. Methodik AG-AN-Aufteilung in DATEV LODAS. Output Lohnabrechnung mit korrekter Aufteilung."
---

# AG-/AN-Anteile in der Sozialversicherung

## Fachlicher Anker

- **Normen:** § 6a, § 249 SGB V, § 168 SGB VI.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

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

| Zweig | AG-Anteil (typisch derzeit ca.) | AN-Anteil (typisch derzeit ca.) |
|---|---|---|
| KV allgemein | 7,3 Prozent | 7,3 Prozent |
| KV-Zusatzbeitrag (KK-individuell) | halftig (paritaetisch seit 01.01.2019) | halftig |
| PV (allgemein, ausserhalb Sachsen) | halftig | halftig |
| PV-Zuschlag Kinderlose ab Vollendung des 23. Lj. | 0 | 0,6 Prozent allein zu Lasten AN (Stand 2025; § 55 Abs. 3 SGB XI i.d.F. PflegeunterstuetzungsG gueltig seit 01.07.2023; jaehrlich ueber GKV-Spitzenverband pruefen) |
| PV-Abschlag mit Kindern (PUEG ab 01.07.2023) | nicht beruehrt | gestaffelter Abschlag für AN je Kind ab 2. Kind (0,25 Prozent/Kind), bis maximal 5 Kinder (max. 1,0 Prozent Abschlag); § 55 Abs. 3 SGB XI (Stand 2025; bei kuenftigen Anpassungen GKV-Spitzenverband pruefen) |
| PV Sachsen (Buss- und Bettag) | typisch geringer AG-Anteil; AN traegt zusaetzliche 0,5 Prozent (§ 58 Abs. 3 SGB XI) | typisch hoeherer AN-Anteil |
| RV | 9,3 Prozent | 9,3 Prozent (gesamt 18,6 Prozent — Stand 2025; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen) |
| AV | 1,3 Prozent je Seite (gesamt 2,6 Prozent — Stand 2025; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen) | wie AG |
| U1 (Kleinunternehmer bis 30 AN) | voll AG | 0 |
| U2 (Mutterschaft, alle AG) | voll AG | 0 |
| Insolvenzgeld-Umlage | voll AG | 0 |
| Berufsgenossenschaft | voll AG | 0 |

(Saemtliche Beitragssaetze Stand 2025; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel ueber DRV, BMAS, GKV-Spitzenverband sowie KK-individuelle Zusatzbeitragssatzungen pruefen.)

### Phase 2 — PV-Kinderlosenzuschlag

- AN ohne Kinder ab 23 Jahre: zusaetzlicher Anteil 0,6 Prozent (Stand 2025, § 55 Abs. 3 SGB XI; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen).
- AN mit Kindern: Abschlag oder Wegfall des Zuschlags.
- Bei mehreren Kindern: gestaffelter Abschlag (Reform 2023 nachgelagert).

### Phase 3 — Sachsen-PV-Sonderregelung

- Sachsen-PV: AN-Anteil hoeher als AG-Anteil (anders als anderswo).
- DATEV LODAS-Stammdaten: Bundesland-Schluessel "Sachsen".

### Phase 4 — KV-Zusatzbeitragssatz

- Jede Krankenkasse erhebt individuellen Zusatzbeitrag.
- Standard-Zusatzbeitragssatz (BMAS-Statistik) durchschnittlich 2,5 Prozent (Stand 2025; Wert 2026 ueber GKV-Spitzenverband pruefen — KK-individuell).
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
- Beitragssaetze Stand 2025: RV 18,6 Prozent, AV 2,6 Prozent, KV allgemein 14,6 Prozent + KK-Zusatzbeitrag (durchschnittlich 2,5 Prozent), PV 3,6 Prozent (Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen).
- PV-Kinderlosenzuschlag 2025: 0,6 Prozent (§ 55 Abs. 3 SGB XI; Sozialversicherungs-Rechengroessenverordnung 2026 pruefen).

<!-- AUDIT 27.05.2026 | welle 6 | 9 Marker aufgeloest: 7 bestaetigt (Fundstelle/Datum), 2 ersetzt (neu formuliert ohne Marker) -->

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
