---
name: mandat-schliessen
description: "Mandat abschließen – Ergebnis, Endexposition und Erkenntnisse festhalten, dann aus dem aktiven Portfolio archivieren ohne den Datensatz zu löschen. Verwenden, wenn der Nutzer ein Mandat schließen möchte, sagt „[Mandat] ist abgeschlossen\", oder ein Vergleich, Klagerücknahme, Urteil, Rücknahme oder Konsolidierung als Ergebnis dokumentieren will."
---

# Mandat schließen

## Zweck

Strukturierter Abschluss eines Mandats im Portfolio: Ergebnis dokumentieren, Kosten und Honorar abrechnen, Lehren festhalten, Mandat aus dem aktiven Portfolio in den Archivstatus überführen. Der Datensatz bleibt dauerhaft erhalten (Aufbewahrungspflicht § 50 Abs. 1 BRAO: 6 Jahre nach Mandatsende).

## Eingaben

- Mandat-Slug
- Abschlusstyp: `--urteil`, `--vergleich`, `--klageruecknahme`, `--erledigungserklaerung`, `--einstellung`, `--sonstiges`
- Ergebnis (kurz): Wer hat gewonnen, was wurde vereinbart, welcher Betrag?

## Ablauf

1. **Abschlusstype und Ergebnis erfassen:**

   | Typ | Relevante Normen |
   |---|---|
   | Urteil (Endurteil) | §§ 300 ff. ZPO; Rechtskraft § 322 ZPO |
   | Anerkenntnisurteil | § 307 ZPO |
   | Versäumnisurteil | §§ 330 ff. ZPO |
   | Vergleich | §§ 794 Abs. 1 Nr. 1, 278 ZPO; vollstreckbar |
   | Klagerücknahme | §§ 269, 270 ZPO; Kostenfolge § 269 Abs. 3 ZPO |
   | Erledigungserklärung | § 91a ZPO; Kostenbeschluss |
   | Einstellung (Strafrecht) | §§ 153, 153a, 170 Abs. 2, 204 StPO |
   | Verfahrensvergleich (Verwaltungsrecht) | § 106 VwGO |

2. **Endexposition berechnen:**
   - Gezahlter Betrag / auferlegte Leistung
   - Kostenfestsetzung (§§ 103 ff. ZPO): eigene Kosten + erstattete / zu erstattende Kosten
   - Vergleich mit ursprünglicher Risikoschätzung (Intake-Wert)

3. **Honorar und Gebühren:**
   - Letzte Abrechnung nach RVG (§ 8 RVG: Fälligkeit mit Mandatsbeendigung)
   - Offene Vorschüsse (§ 9 RVG) zurückerstatten oder verrechnen
   - Fremdgelder abwickeln (§ 43a Abs. 5 BRAO: unverzügliche Weiterleitung)

4. **Lessons Learned:**
   - Was lief gut / schlecht?
   - Prozessführungsempfehlung für künftige vergleichbare Mandate?
   - BGH- oder OLG-Urteile, die im Mandat relevant waren und für spätere Mandate zu merken sind?

5. **Handakte archivieren (§ 50 BRAO):**
   - Handakte für mind. 6 Jahre nach Mandatsende aufbewahren
   - Elektronische Akte: gleichwertige Sicherung (§ 50 Abs. 2 BRAO)
   - Herausgabepflicht auf Verlangen (§ 50 Abs. 3 BRAO)

6. **Portfolio-Log aktualisieren:** Status in `_log.yaml` auf `archiv` setzen; Abschlussdatum, Ergebnis, Endexposition eintragen.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- BGH, Urt. v. 10.02.2021 – VIII ZR 64/20, NJW 2021, 1161 Rn. 19 (Rechtskraft des Urteils: Umfang, § 322 ZPO).
- BGH, Beschl. v. 30.05.2018 – XII ZB 308/16, NJW 2018, 2794 Rn. 14 (Prozessvergleich: Vollstreckbarkeit und Widerrufsvorbehalt).
- Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 269 Rn. 1 ff. (Klagerücknahme: Einwilligung, Kostenfolge).
- Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 91a Rn. 1 ff. (Erledigungserklärung: übereinstimmende Erklärungen, Kostentragungspflicht nach bisherigem Sach- und Streitstand).
- BRAO § 50 (Aufbewahrungspflicht Handakten: 6 Jahre); § 43a Abs. 5 BRAO (Fremdgelder).
- BGH, Beschl. v. 19.09.2018 – IX ZB 16/17, NJW 2018, 3710 Rn. 22 (Kostenfestsetzungsverfahren §§ 103 ff. ZPO: Antragsfrist, sofortige Beschwerde).

## Ausgabeformat

```
MANDAT-ABSCHLUSS
──────────────────────────────────────
Mandat-Slug:    [slug]
Schließungsdatum: TT.MM.JJJJ
Typ:            [z. B. Vergleich]
MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

──────────────────────────────────────
ERGEBNIS
──────────────────────────────────────
[Kurzbeschreibung: z. B. „Vergleich: Beklagter zahlt EUR 25.000; gegenseitige Erledigung aller Ansprüche. Protokolliert am TT.MM.JJJJ vor LG Frankfurt a. M., Az. 2-08 O 123/23."]

──────────────────────────────────────
ENDEXPOSITION
──────────────────────────────────────
Eingeklagter Betrag:       EUR XX.XXX
Vergleichszahlung:         EUR XX.XXX
Kostenerstattung:          EUR X.XXX (§§ 103 ff. ZPO)
Ursprüngliche Schätzung:   EUR XX.XXX – EUR XX.XXX

──────────────────────────────────────
LESSONS LEARNED
──────────────────────────────────────
[Freitext]

──────────────────────────────────────
ARCHIVIERUNG
──────────────────────────────────────
Handakte aufzubewahren bis: TT.MM.JJJJ (§ 50 Abs. 1 BRAO: 6 Jahre)
_log.yaml-Status: archiv
```

## Risiken / typische Fehler

- **Aufbewahrungsfrist übersehen:** § 50 Abs. 1 BRAO: mindestens 6 Jahre nach Mandatsende; kürzere Vernichtung ist Berufsrechtsverletzung.
- **Fremdgelder nicht abgewickelt:** § 43a Abs. 5 BRAO – Fremdgelder (Kostenvorschüsse, Schadensersatzbeträge) unverzüglich weiterleiten; Verzögerung kann zur Strafbarkeit führen (§ 266 StGB).
- **Rechtsmittelfrist läuft noch:** Vor dem Schließen prüfen, ob Berufungs- (§ 517 ZPO: 1 Monat) oder Revisionsfrist (§ 548 ZPO: 1 Monat) noch offen ist; Mandat erst nach Eintritt der Rechtskraft schließen oder Mandanten ausdrücklich auf Verzicht hinweisen.
- **Vollstreckungsverjährung:** Vollstreckungstitel verjähren nach § 197 Abs. 1 Nr. 3 BGB in 30 Jahren; Abschluss nicht ohne Dokumentation der Vollstreckungsmaßnahmen.
