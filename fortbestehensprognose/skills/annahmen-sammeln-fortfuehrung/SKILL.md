---
name: annahmen-sammeln-fortfuehrung
description: "Sammelt die Annahmen die der Geschaeftsfuehrer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalitaet Auftragsbestand Kunden-Konzentration Markt- und Branchenentwicklung. Annahmen muessen konkret nachvollziehbar und mit der Vergangenheit abgleichbar sein. Eingang zur Plausibilisierung im Skill `annahmen-belastbarkeit-plausibilisieren` und zur 12-Monats-Liquiditaet im Skill `liquiditaet-12-monate`."
---

# Annahmen sammeln (Fortführung)

## Zweck

Die Fortbestehensprognose ist eine **Prognose** — sie steht und faellt mit den Annahmen. Wer die Annahmen klar dokumentiert kann sie später prüfen verteidigen oder anpassen. Wer sie nicht dokumentiert hat **keine** Prognose.

IDW S 11 (Beurteilung von Insolvenzeröffnungsgründen) und IDW S 6 (Sanierungskonzepte) fordern jeweils eine **integrierte Planung** mit klaren Annahmen.

## Pflichtfelder pro Annahme

```yaml
annahmen:
  - bezeichnung: Umsatzentwicklung Hauptgeschaeft
    art: umsatz
    horizont-monate: 12
    werte:
      - monat: 2026-06
        wert: 195000
      - monat: 2026-07
        wert: 180000
      # ...
    begruendung: |
      Vorjahreswerte plus 3% Wachstum bei stabiler Auftragslage.
      Auftragsbestand zum 20.05.2026 deckt bis September 2026.
    belege:
      - auftragsbestand-2026-05-20.xlsx
      - kundenbestätigung-grossauftrag-X.pdf
    risiko: mittel  # niedrig / mittel / hoch
    sensitivitaet: 
      negativ-szenario: -15% Umsatz waehrend zweier Monate
      positiv-szenario: +10% Umsatz
```

## Annahmebereiche

### 1. Umsatzentwicklung

- **Auftragsbestand** zum Stichtag.
- **Kundenpipeline** quasi-sichere Folgeaufträge.
- **Saisonalität** historisch über drei Jahre.
- **Top-Kunden-Konzentration** Risiko bei Wegfall.

### 2. Kostenentwicklung

- **Materialkosten** Lieferantenpreise Energie.
- **Personalkosten** Tarifsteigerungen Sozialabgaben.
- **Mieten** Vertragsprüfung Indexmiete.
- **Energie** aktueller Preis und Vertragslaufzeit.

### 3. Working Capital

- **Forderungslaufzeiten** Tage Outstanding (DSO).
- **Vorrats-Reichweite** Umschlagsdauer.
- **Lieferanten-Zahlungsziele** ggf. verschlechtert wegen Krise (DPO).

### 4. Investitionen und Desinvestitionen

- **Geplante Investitionen** und ihre Finanzierung.
- **Desinvestitionen** Verkauf nicht-betriebsnotwendiger Vermögenswerte.

### 5. Finanzierung

- **Bestehende Kreditlinien** Volumen Ausnutzung Endfälligkeit.
- **Tilgungspläne** der bestehenden Darlehen.
- **Neue Finanzierungsangebote** Bank schriftliche Zusagen.
- **Gesellschafterzusagen** Patronatserklärungen Comfortletter.

### 6. Sanierungsmaßnahmen

- **Bereits eingeleitete** Maßnahmen (Kostensenkung Personalreduzierung Standortschliessungen).
- **Geplante** Maßnahmen mit Zeitplan und Effekt.
- **Gegenfinanzierung** der Sanierungskosten.

## Abgrenzung zwischen Annahmen und Wünschen

**Annahme**: Eine konkrete nachvollziehbare Erwartung mit Begründung und Beleg.

**Wunsch**: Eine optimistische Hoffnung ohne Beleg.

Im Streit (z. B. späteren Haftungsprozess) wird genau geprüft ob es Wünsche oder Annahmen waren. Wer optimistisch ohne Belege geplant hat ist haftungsexponiert (§ 43 GmbHG, § 15b InsO).

## Konkretheit

Jede Annahme braucht:

- **Zahl** (in EUR oder Prozent oder Tagen) — keine Spannweiten außer bei Sensitivitaet.
- **Zeitraum** — Monat oder Quartal.
- **Begründung** — woher kommt die Zahl?
- **Beleg** — Excel Auftragsbestand Bestätigung Kunde Mietvertrag etc.

## Sammlung der Annahmen

```yaml
prognose-id: FP-2026-0001
stichtag: 2026-05-20
horizont-monate: 12  # gesetzlicher Maßstab seit SanInsFoG 2021

annahmen:
  umsatz:
    - bezeichnung: Hauptsegment Produktion
      monatswerte: [195000, 180000, 220000, 240000, 230000, 200000, 190000, 195000, 210000, 220000, 215000, 225000]
      begruendung: Auftragsbestand bis September 2026; Mai-Oktober historisch +10% über Schnitt
      belege: [auftragsbestand-2026-05-20.xlsx]
      risiko: mittel

  kosten:
    - bezeichnung: Material und Energie
      basismonats-wert: 95000
      jahressteigerung: 3%
      begruendung: Lieferantenverträge bis 06/2027 Indexbindung 3%
      belege: [lieferantenverträge-übersicht.xlsx]
      risiko: niedrig
    - bezeichnung: Personalkosten
      basismonats-wert: 78000
      jahressteigerung: 4%
      begruendung: Tarifabschluss Metall 04/2026 4% per 01.07.2026
      belege: [tarifabschluss-04-2026.pdf]
      risiko: niedrig

  working-capital:
    forderungstage-soll: 30
    forderungstage-ist: 42
    vorratsreichweite-soll: 60
    vorratsreichweite-ist: 75
    begruendung-abweichung: kundenseits verzoegerte Zahlungen seit Q1 2026
    massnahmen: Mahnwesen verschärft

  investitionen:
    - bezeichnung: Ersatzinvestition CNC
      betrag: 80000
      monat: 2026-09
      finanzierung: Sale-and-Lease-back

  finanzierung:
    bank-kreditlinie: 150000
    ausnutzung-ist: 92%
    gesellschafterdarlehen-mit-rangruecktritt: 120000
    weitere-massnahmen: keine

  sanierungsmassnahmen:
    - bezeichnung: Standortschliessung Nebenwerk
      effekt-monatlich: 12000
      ab-monat: 2026-08
      einmalkosten: 60000
      einmalkosten-monat: 2026-07
```

## Ausgabe

- `annahmen.yaml` mit allen Pflichtfeldern.
- Hinweis auf Skill `annahmen-belastbarkeit-plausibilisieren` als nächsten Schritt.
- Liste fehlender Belege als Prüfer-Flag.
- Empfehlung: bei einer Annahme die als unbelegt markiert ist *nicht* in die Liquidität übernehmen — oder explizit als „Modellannahme ohne Beleg" markieren.


## Aktuelle Leitentscheidungen — Annahmen-Sammlung Fortbestehensprognose

- BGH, Urt. v. 19.12.2017 — IX ZR 285/14, BGHZ 217, 1 — Fortbestehensprognose: konkrete, nachvollziehbare Annahmen fuer den 12-Monats-Prognosehorizont erforderlich; pauschale Annahmen oder blosse Hoffnungen genuegen nicht; Geschaeftsfuehrer traegt Verantwortung fuer Annahmen-Qualitaet.
- BGH, Urt. v. 06.06.2013 — IX ZR 204/12, NZI 2013, 793 — Umsatz-Prognose als Fortbestehensprognose-Kernannahme: Auftragsbestand und Kundenvertraege als belastbarste Grundlage; Annahmen ohne konkreten Auftragsbestand sind kritisch zu wuerdigen.
- BGH, Urt. v. 07.03.2013 — IX ZR 64/12, NZI 2013, 477 — Sanierungskonzept-Qualitaet: Annahmen muessen auf konkreten betriebswirtschaftlichen Daten basieren; externe Markt-Analyse ersetzbarer fuer neue Maerkte, nicht fuer Stammageschaeft.

## Triage — Annahmen-Vollstaendigkeit

1. **Einnahmen-Seite vollstaendig?** Auftragsbestand, Rahmenvertraege, Neukundenpipeline — alle konkret belegbar?
2. **Kosten-Seite vollstaendig?** Personal (inkl. SV), Material/Wareneinsatz, Fixkosten, Miete, Finanzierungskosten — alle als Einzelpositionen?
3. **Working Capital?** Debitorenlaufzeit, Kreditorenlaufzeit, Lagerbestand — als Cashflow-Auswirkung erfasst?
4. **Ausserordentliche Ereignisse?** Investitionen, Tilgungen, FA-Stundungen ablaufend, Avale faellig werdend?

## Paragrafenkette

§ 19 Abs. 2 InsO (Fortbestehensprognose) → IDW S 11 Rn. 30-65 (Annahmen-Basis) → § 43 GmbHG (Sorgfaltspflicht GF bei Prognose)

## Kommentarliteratur

- IDW S 11, Stand 11/2022 Rn. 30-65 — Annahmen-Sammlung und Dokumentation.
- MüKo InsO/Drukarczyk § 19 InsO Rn. 50 ff. — Prognose-Annahmen und Prognosehorizont.
- K. Schmidt/Uhlenbruck, GmbH in Krise Sanierung und Insolvenz, § 5 Rn. 5.10 — Fortbestehensprognose in der Praxis.
