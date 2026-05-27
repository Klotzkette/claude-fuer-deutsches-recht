---
name: stb-lohn-umlage-u1-u2-insogeld-umlage
description: "Umlagen U1 U2 Insolvenzgeld-Umlage. Anwendungsfall AG-Umlagen monatlich Erstattung Krankheit Mutterschaft Insolvenz Berechnung Saetze Variabilitaet KK. Methodik Pruefung Pflicht Kleinunternehmer 30 AN. Output Umlage-Berechnung."
---

# Umlagen U1, U2, Insolvenzgeld

## Kernsachverhalt

Drei Umlagen lasten ausschliesslich auf dem AG (AN-Anteil null):
- **U1** (Aufwendungsausgleich Krankheit): Erstattung Entgeltfortzahlung im Krankheitsfall; Pflicht fuer Kleinunternehmer bis 30 AN; Erstattung 80 Prozent.
- **U2** (Aufwendungsausgleich Mutterschaft): Erstattung Mutterschutzlohn und AG-Zuschuss Mutterschaftsgeld; Pflicht aller AG; Erstattung 100 Prozent.
- **Insolvenzgeld-Umlage**: Beitrag zur Finanzierung des Insolvenzgeldes; Pflicht aller AG (Ausnahme Privathaushalte).

## Kaltstart-Rueckfragen

1. Mitarbeiterzahl im Mandantenbetrieb (U1-Pflicht-Pruefung)?
2. Welche Krankenkassen vertreten (Beitragssatz U1 KK-individuell)?
3. Welche AN sind in Erstattungsbasis einbezogen (Vollzeit, Teilzeit, Minijob)?
4. Wann letzte Erstattungs-Antraege gestellt?
5. Bei drohendem AG-Wechsel: Datenuebernahme Umlage-Beitraege?
6. BG-Beitrag Insolvenzgeld-Umlage aktualisiert?
7. Welche jaehrliche Anpassung?
8. Welche Privathaushalts-Konstellation (Minijob-Sonderfall)?

## Rechtlicher Rahmen

### Primaernormen

**AAG (Aufwendungsausgleichsgesetz)** — U1/U2.

**§ 1 AAG** — Geltungsbereich U1.

**§ 7 AAG** — Berechnung Umlage.

**§ 358 SGB III** — Insolvenzgeld-Umlage.

**§ 165 SGB III** — Insolvenzgeld.

### Verwaltungsanweisungen

- KK-individuelle Satzungen.
- BMAS Rundschreiben.

## Workflow

### Phase 1 — U1-Pflicht-Pruefung

- AG mit max. 30 AN ist U1-pflichtig.
- Pruefung jaehrlich zum 1. Januar (Berechnung Durchschnitt Vorjahr).
- Minijobs werden mit Faktor 0,75 angerechnet.
- Pflicht-Wechsel mit naechstem Kalenderjahr.

### Phase 2 — Berechnungs-Basis

- Umlagebeitrag = Bemessungsgrundlage x Umlagesatz.
- Bemessungsgrundlage U1/U2: rentenversicherungspflichtiges Brutto bis zur BBG der RV (§ 7 AAG).
- U1 Satz: KK-individuell (variiert nach KK-Satzung); typisch 1,0-3,0 Prozent.
- U2 Satz: KK-individuell; typisch 0,2-0,5 Prozent.
- Insolvenzgeld-Umlage: bundeseinheitlich, festgesetzt durch Verordnung (Insolvenzgeldumlageverordnung); aktueller Wert 2026 verifizieren (Vergleich: 2024 0,06 Prozent).

### Phase 3 — Erstattungsantraege

- U1 bei Krankheit: AG zahlt Entgeltfortzahlung weiter; beantragt Erstattung 80 Prozent bei KK.
- U2 bei Mutterschaft: AG zahlt Zuschuss zum Mutterschaftsgeld; beantragt Erstattung 100 Prozent bei KK.
- Antrag: ueber sv.net oder DAKOTA.
- Frist: 3 Monate nach Beendigung des Ereignisses (KK-Satzung).

### Phase 4 — Insolvenzgeld-Umlage

- Bundeseinheitlich; aktuellen Satz 2026 verifizieren.
- Faellig zusammen mit SV-Beitragsnachweis.
- Wird ueber die Krankenkassen eingezogen.

### Phase 5 — Buchung im Hauptbuch

- Lohnnebenkosten Umlagen (Konto 4140 oder 6140 SKR 03).
- AG-Aufwand.
- Bei Erstattung: Gegenbuchung (Konto 4141 oder Verbuchung zu Lohnnebenkosten).

### Phase 6 — Dokumentation

- Erstattungsantraege archivieren.
- KK-Bescheide ueber Erstattung.
- Beleg im Lohnordner.

## Output

- Korrekt berechnete Umlagen.
- Erstattungsantraege bei Krankheit/Mutterschaft.
- Buchung im Hauptbuch.

## Strategie und Praxis-Tipps

- U1-Pflicht-Pruefung jaehrlich zum 1. Januar — nicht vergessen.
- U2 ist UNABHAENGIG von Betriebsgroesse Pflicht.
- Insolvenzgeld-Umlage entfaellt fuer Privathaushalte (Privathaushalts-Minijob).
- Erstattungsantraege rechtzeitig stellen — Frist max. 4 Jahre.
- Bei wechselnder Mitarbeiterzahl ueber 30: U1-Wechsel zum Jahreswechsel.
- StBVV: in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS Umlage-Konfiguration mit jaehrlicher Pflicht-Aktualisierung.

## Querverweise

- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-krankheit-entgeltfortzahlung-efzg` — Krankheit.
- `stb-lohn-elternzeit-mutterschutz` — Mutterschaft.
- `stb-lohn-arbeitgeber-arbeitnehmer-anteile` — AG-/AN-Anteile.

## Quellen und Updates

Stand: 05/2026.

- AAG §§ 1, 7.
- SGB III §§ 165, 358.
- KK-Satzungen.
- BMAS Rundschreiben.
- Verifikations-Hinweis: Insolvenzgeld-Umlage 2026 verifizieren.
