---
name: rollierende-liquiditaetsplanung-24-monate-template
description: "Rollierende 24-Monats-Liquiditaetsplanung nach StaRUG erstellen: Sanierungsberater oder GF braucht Liquiditaets-Forecast. Normen: § 1 StaRUG (24-Monats-Horizont), IDW S 11 (Fortbestehensprognose), IDW S 6 (Sanierungskonzept). Pruefraster: Woechentliche Granularitaet Wochen 1-13, monatliche Granularitaet Monate 14-24, Stresstests, Sensitivitaetsanalysen, StaRUG-konforme Dokumentation. Output Excel-Template Liquiditaetsplanung, Stresstest-Szenarios, Dokumentationsprotokoll. Abgrenzung: Integrierte GuV/Bilanz/CF-Planung siehe integrierte-planung-guv-bilanz-cashflow; Ampel-KPIs siehe kennzahlenset-und-ampelsystem-starug-konform."
---

# Rollierende Liquiditätsplanung — 24-Monate-Template

Die rollierende Liquiditätsplanung ist das operative Herzstück des § 1 StaRUG-Frühwarnsystems. Sie zeigt nicht nur, wo das Unternehmen heute steht, sondern wo es in zwei Jahren stehen wird — und welche Handlungskorridore noch offen sind. Ohne eine valide 24-Monats-Liquiditätssicht ist die Behauptung, drohende Zahlungsunfähigkeit nicht rechtzeitig erkannt zu haben, im Nachhinein nicht zu entkräften.

---

## Rechtsgrundlagen

- § 1 StaRUG (Krisenfrüherkennungspflicht, 24-Monats-Horizont)
- § 18 InsO (drohende Zahlungsunfähigkeit — Prognosezeitraum)
- § 29 Abs. 2 StaRUG (Zugangsvoraussetzung: drohende ZU muss vorliegen)
- IDW S 11 Tz. 23 ff. (Liquiditätsstatus und -planung als Basis der Fortbestehensprognose)
- IDW S 6 (integrierte Planung als Teil des Sanierungskonzepts)
- BGH IX ZR 285/14 (Planungspflicht als Sorgfaltsanforderung)

---

## Pflichten

### 1. Warum zwei Granularitätsstufen?

Die Unterscheidung zwischen wöchentlicher (Wochen 1-13) und monatlicher (Monate 14-24) Granularität ist kein Zufall, sondern Ausdruck der Planungssicherheit:

- **Wochen 1-13 (kurzfristig):** Fälligkeiten, Überweisungen, Lohnzahlungen, Steuertermine sind konkret und kurzfristig planbar. Wöchentliche Granularität ist hier Standard und von Banken/Gläubigern erwartet.
- **Monate 14-24 (mittelfristig):** Annahmenbasierte Prognose. Monatsgenauigkeit ausreichend und methodisch vertretbar. Zeigt strukturelle Liquiditätsreserven und Refinanzierungsbedarfe.

### 2. Mindestinhalt der Planung

Der Liquiditätsplan muss enthalten:

**Zuflüsse:**
- Umsatzerlöse (nach Debitorenlaufzeiten)
- Anzahlungen, Vorauszahlungen
- Fremdfinanzierungen (Kredit-Ziehungen)
- Subventionen, Förderungen
- Sonstige betriebliche Erträge mit Zahlungswirkung

**Abflüsse:**
- Material-/Wareneinkauf (nach Kreditorenlaufzeiten)
- Lohn- und Gehaltskosten (inkl. Sozialabgaben)
- Miete, Leasing
- Zinsen und Tilgungen
- Investitionsauszahlungen
- Steuern und Abgaben (Umsatzsteuer-Vorauszahlung, Körperschaftsteuer, Gewerbesteuer)
- Sonstige Auszahlungen

**Saldo und Kassenbestand:**
- Wöchentlicher/monatlicher Cash-Flow (netto)
- Kumulierter Kassenbestand
- Verfügbare Kreditlinien
- Gesamtliquidität (Kassenbestand + freie Linien)

---

## Vorgehen

### Schritt 1: Strukturaufbau des 24-Monats-Plans

```
PLANSTRUKTUR — ÜBERBLICK

Spalten: [Datum / Woche / Monat]

ZUFLÜSSE
  + Umsatzerlöse brutto
  - USt-Abführung (auf Umsatz)
  + Anzahlungen Kunden
  + Kreditziehungen
  + Sonstige Zuflüsse
  = ZUFLÜSSE GESAMT

ABFLÜSSE
  - Materialeinkauf
  - Personal (netto + AG-Anteile SV)
  - Miete / Leasing
  - Zinsen
  - Tilgung
  - USt-Voranmeldung
  - Investitionen
  - Sonstige Abflüsse
  = ABFLÜSSE GESAMT

NETTO-CASHFLOW = Zuflüsse - Abflüsse

KASSENBESTAND
  + Anfangsbestand
  + Netto-Cashflow
  = Endbestand

KREDITLINIE
  + Verfügbarer Rahmen
  - Inanspruchnahme
  = Freie Kreditlinie

GESAMTLIQUIDITÄT = Endbestand + Freie Kreditlinie
```

### Schritt 2: Wöchentliche Planung (Wochen 1-13)

Für die ersten 13 Wochen wird jede Woche einzeln geplant:

1. **Basis:** Offene-Posten-Listen Debitoren und Kreditoren (Stichtag aktuell)
2. **Zahlungsverhalten:** Historische DSO (Days Sales Outstanding) und DPO (Days Payable Outstanding) anwenden
3. **Fälligkeiten:** Steuertermine, Lohnläufe, Kreditorenzahlungsziele eintragen
4. **Kontokorrent-Check:** Wöchentlich prüfen, ob Überziehung droht

### Schritt 3: Monatliche Planung (Monate 14-24)

Für den Zeitraum Monat 14-24:

1. **Planprämissen dokumentieren:** Umsatzwachstum/-rückgang, Kostenentwicklung, Investitionspläne
2. **Mindestens zwei Szenarien:** Base Case + Bear Case (oder mehr)
3. **Refinanzierungsbedarfe** explizit kennzeichnen: Wann läuft welche Kreditlinie aus?
4. **Covenants einblenden:** Wann werden Finanzkennzahl-Anforderungen überprüft?

### Schritt 4: Stresstests definieren und durchrechnen

| Stresstest | Annahme | Typische Auswirkung |
|---|---|---|
| Umsatzeinbruch | Umsatz minus 20 % über 6 Monate | Liquiditätsreichweite reduziert sich um ca. 4-6 Monate |
| Debitorenlaufzeit | DSO steigt von 45 auf 75 Tage | Sofortige Liquiditätslücke von ca. 2 Monatsumsätzen |
| Kreditlinienkündigung | Hausbankkredit wird nicht verlängert | Refinanzierungslücke in EUR [x] sichtbar |
| Kostenexplosion | Material-/Energiekosten plus 30 % | EBITDA-Erosion, ab wann DSCR unter 1,0? |

### Schritt 5: Plan-Ist-Abweichungsanalyse

Monatlicher Vergleich: Was wurde geplant, was ist eingetreten?

- Abweichungen > 10 % müssen kommentiert werden
- Systematische Abweichungen führen zur Planrevision
- Planrevision wird dokumentiert und von GF unterschrieben

---

## Templates

### Muster: Excel-Spaltenstruktur (Auszug Wochen 1-4 + Monat 14)

```
Kategorie                 | KW01  | KW02  | KW03  | KW04  | ... | M14   | M15
--------------------------|-------|-------|-------|-------|-----|-------|------
ZUFLÜSSE                  |       |       |       |       |     |       |
  Umsatzerlöse (netto)    | [tsd] | [tsd] | [tsd] | [tsd] |     | [tsd] | [tsd]
  Anzahlungen             | [tsd] | [tsd] | [tsd] | [tsd] |     | [tsd] | [tsd]
  Kreditziehung           |       |       |       |       |     |       |
= ZUFLÜSSE GESAMT         | [Sum] | [Sum] | [Sum] | [Sum] |     | [Sum] | [Sum]
                          |       |       |       |       |     |       |
ABFLÜSSE                  |       |       |       |       |     |       |
  Material                | [tsd] | [tsd] | [tsd] | [tsd] |     | [tsd] | [tsd]
  Personal                | [tsd] |       |       | [tsd] |     | [tsd] | [tsd]
  Miete / Leasing         | [tsd] |       |       |       |     | [tsd] | [tsd]
  Zinsen                  |       |       |       |       |     | [tsd] | [tsd]
  Tilgung                 |       |       |       |       |     | [tsd] | [tsd]
  USt-Voranmeldung        | [tsd] |       |       |       |     | [tsd] | [tsd]
  Sonstiges               | [tsd] | [tsd] | [tsd] | [tsd] |     | [tsd] | [tsd]
= ABFLÜSSE GESAMT         | [Sum] | [Sum] | [Sum] | [Sum] |     | [Sum] | [Sum]
                          |       |       |       |       |     |       |
NETTO-CASHFLOW            | [Net] | [Net] | [Net] | [Net] |     | [Net] | [Net]
KASSENBESTAND (Anfang)    | [K]   | [K]   | [K]   | [K]   |     | [K]   | [K]
KASSENBESTAND (Ende)      | [K]   | [K]   | [K]   | [K]   |     | [K]   | [K]
FREIE KREDITLINIE         | [L]   | [L]   | [L]   | [L]   |     | [L]   | [L]
GESAMTLIQUIDITÄT          | [G]   | [G]   | [G]   | [G]   |     | [G]   | [G]
```

### Muster: Planprämissen-Dokumentation

```
Planprämissen — 24-Monats-Liquiditätsplanung
Gesellschaft: [Firma GmbH]
Erstellt: [Datum]
Freigegeben: [GF-Name], [Datum]

UMSATZ
  Basis: [EUR Vorjahresumsatz]
  Annahme Base Case: [+/- x% p.a.]
  Annahme Bear Case: [+/- x% p.a.]
  Begründung: [___]

DEBITORENLAUFZEIT (DSO)
  Historisch (Ø letzte 12 Monate): [x] Tage
  Annahme Planung: [x] Tage
  Begründung: [___]

KREDITORENLAUFZEIT (DPO)
  Historisch: [x] Tage
  Annahme: [x] Tage

KREDITLINIEN
  Hausbankkredit: EUR [Betrag], läuft bis [Datum]
  Kontokorrentlinie: EUR [Betrag]
  Verlängerungsannahme: [ja/nein/in Verhandlung]

INVESTITIONEN
  Geplante Investitionen: EUR [Betrag] in [Zeitraum]
  Finanzierung: [Eigenmittel / Fremdfinanzierung]
```

---

## Fallstricke

1. **Plan ohne Planprämissen ist wertlos** — Richter und Insolvenzverwalter fragen als erstes: Auf welchen Annahmen beruht dieser Plan? Fehlende Prämissendokumentation ist ein Warnzeichen.

2. **Statischer Plan statt rollierender** — ein einmal erstellter 24-Monats-Plan, der nie aktualisiert wird, zeigt nicht den aktuellen Stand. Rollen bedeutet: monatliche Aktualisierung mit Ist-Werten und Neuvorschau.

3. **Nur Ergebnis-Plan ohne Cashflow** — viele Unternehmen haben GuV-Planungen, aber keinen Cashflow-Plan. Für § 1 StaRUG und § 18 InsO ist der Cashflow entscheidend, nicht das bilanzielle Ergebnis.

4. **Zu optimistische Planprämissen** sind keine „konservative Schätzung" — Gerichte prüfen ex post, ob die Annahmen zum Zeitpunkt der Planung plausibel waren. Überhöhte Umsatzerwartungen ohne Begründung sind Haftungsrisiko.

5. **Kreditlinie als Puffer einplanen, ohne Verlängerungsrisiko zu beachten** — ausgelaufene Kreditlinien, die stillschweigend als verlängert angenommen werden, verfälschen die Liquiditätssicht erheblich.

---

## Querverweise

- → `fruehwarnsystem-architektur-zwei-jahres-horizont` — Systemarchitektur
- → `integrierte-planung-guv-bilanz-cashflow` — Drei-Statement-Verbindung
- → `kennzahlenset-und-ampelsystem-starug-konform` — KPI-Schwellen
- → `drohende-zahlungsunfaehigkeit-paragraph-18-inso` — Prognosezeitraum
- → `fortbestehensprognose-zweistufig` — IDW S 11-Nutzung der Liquiditätsplanung


## Weitere Leitentscheidungen

- BGH, Urt. v. 19.12.2017 — IX ZR 285/14, BGHZ 217, 1 — Fortbestehensprognose § 19 Abs. 2 InsO und Handlungspflichten: positive Prognose heilt Ueberschuldung; negative Prognose loest Antragspflicht aus; Dokumentation ist Haftungsschutz.
- BGH, Urt. v. 15.03.2016 — II ZR 119/14, NJW 2016, 2493 — § 43 GmbHG / § 15b InsO: Geschaeftsfuehrer haftet persoenlich; ordnungsgemaesse Krisenfrueherkennung und Dokumentation als Entlastungsbeweis.
- BGH, Urt. v. 26.01.2017 — IX ZR 285/14 — Antragspflicht § 15a InsO: Fristbeginn mit Kenntnis; spaeteres Handeln erhoht Haftungsrisiko erheblich.
- BGH, Urt. v. 06.05.2021 — IX ZR 72/20, NZI 2021, 631 — Sanierungs-Konzept-Pflicht: echter Sanierungsversuch mit dokumentiertem Konzept schutzt vor Strafbarkeit und Anfechtung.


## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?
