---
name: annahmen-sammeln-bilanzieller-status
description: "Annahmen Sammeln Bilanzieller Status: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Annahmen Sammeln Bilanzieller Status

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Annahmen Sammeln Bilanzieller Status** im Plugin Fortbestehensprognose (IDW S 11). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `annahmen-sammeln-fortfuehrung` | Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalitaet Auftragsbestand Kunden-Konzentration Markt- und Branchenentwicklung. Annahmen muessen konkret nachvollziehbar und mit der Vergangenheit abgleichbar sein. Eingang zur Plausibilisierung im Skill `annahmen-belastbarkeit-plausibilisieren` und zur 12-Monats-Liquiditaet im Skill `liquiditaet-12-monate`. |
| `bilanzieller-status-aufnehmen` | Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten und außerbilanzielle Verpflichtungen (Pensionsrückstellungen Buergschaften Comfortletter). Erzeugt Insolvenzstatus als Vorstufe zur Fortbestehensprognose. Wichtig — bilanzielle Überschuldung ist nicht automatisch insolvenzrechtliche Überschuldung (§ 19 Abs. 2 InsO Fortbestehensprognose). |
| `comfortletter-weich-erzeugen` | Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstuetzen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht rechtsverbindlich durchsetzbar. Wirkung Reputation und Banken-Signal. Nicht ausreichend zur Berücksichtigung im insolvenzrechtlichen Status nach § 19 Abs. 2 InsO. Skill erzeugt Dokument plus Warnhinweis dass der Comfortletter die Fortbestehensprognose nicht traegt. |

## Arbeitsweg

Im Plugin Fortbestehensprognose (IDW S 11) gilt für **Annahmen Sammeln Bilanzieller Status**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `annahmen-sammeln-fortfuehrung`

**Fokus:** Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalitaet Auftragsbestand Kunden-Konzentration Markt- und Branchenentwicklung. Annahmen muessen konkret nachvollziehbar und mit der Vergangenheit abgleichbar sein. Eingang zur Plausibilisierung im Skill `annahmen-belastbarkeit-plausibilisieren` und zur 12-Monats-Liquiditaet im Skill `liquiditaet-12-monate`.

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
 risiko: mittel # niedrig / mittel / hoch
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
horizont-monate: 12 # gesetzlicher Maßstab seit SanInsFoG 2021

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
- Empfehlung: bei einer Annahme die als unbelegt markiert ist *nicht* in die Liquidität übernehmen — oder explizit als "Modellannahme ohne Beleg" markieren.


## Aktuelle Leitentscheidungen — Annahmen-Sammlung Fortbestehensprognose

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — Annahmen-Vollstaendigkeit

1. **Einnahmen-Seite vollstaendig?** Auftragsbestand, Rahmenvertraege, Neukundenpipeline — alle konkret belegbar?
2. **Kosten-Seite vollstaendig?** Personal (inkl. SV), Material/Wareneinsatz, Fixkosten, Miete, Finanzierungskosten — alle als Einzelpositionen?
3. **Working Capital?** Debitorenlaufzeit, Kreditorenlaufzeit, Lagerbestand — als Cashflow-Auswirkung erfasst?
4. **Ausserordentliche Ereignisse?** Investitionen, Tilgungen, FA-Stundungen ablaufend, Avale faellig werdend?

## Paragrafenkette

§ 19 Abs. 2 InsO (Fortbestehensprognose) → IDW S 11 Rn. 30-65 (Annahmen-Basis) → § 43 GmbHG (Sorgfaltspflicht GF bei Prognose)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `bilanzieller-status-aufnehmen`

**Fokus:** Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten und außerbilanzielle Verpflichtungen (Pensionsrückstellungen Buergschaften Comfortletter). Erzeugt Insolvenzstatus als Vorstufe zur Fortbestehensprognose. Wichtig — bilanzielle Überschuldung ist nicht automatisch insolvenzrechtliche Überschuldung (§ 19 Abs. 2 InsO Fortbestehensprognose).

# Bilanzieller Status aufnehmen

## Zweck

Der **bilanzielle** Überschuldungsstatus ist die Voraussetzung um in die Prüfung der **insolvenzrechtlichen** Überschuldung nach § 19 Abs. 2 InsO einzusteigen. Beide Schritte sind zu trennen:

1. **Bilanzieller Überschuldungsstatus** (Stichtagsbetrachtung). Aktiva kleiner als Passiva?
2. **Insolvenzrechtliche Überschuldung** (§ 19 InsO). Nur wenn bilanzielle Überschuldung vorliegt UND keine positive Fortbestehensprognose.

## Stichtagsbilanz

```yaml
stichtag: 2026-05-20 # oder Bilanzstichtag des letzten Jahresabschlusses
bilanzansatz: hgb # hgb / ifrs / mischung

aktiva:
 a-anlagevermoegen:
 immaterielle: 50000
 sachanlagen: 320000
 finanzanlagen: 0
 b-umlaufvermoegen:
 vorraete: 180000
 forderungen-laul: 120000
 sonstige-forderungen: 15000
 fluessige-mittel: 18000
 c-rechnungsabgrenzung: 5000
 aktiva-summe: 708000

passiva:
 a-eigenkapital:
 gezeichnetes-kapital: 25000
 kapitalruecklage: 0
 gewinnruecklagen: 0
 bilanzergebnis: -107000 # negativ
 eigenkapital-summe: -82000 # negativ
 b-rueckstellungen:
 pensionen: 0
 sonstige: 22000
 c-verbindlichkeiten:
 banken: 250000
 lieferanten: 410000
 sonstige: 38000
 steuern: 25000
 sozialversicherung: 45000
 d-rechnungsabgrenzung: 0
 passiva-summe: 708000

bilanzielle-ueberschuldung: ja # Aktiva = Passiva aber EK negativ = bilanzielle Überschuldung
hoehe-bilanzielle-ueberschuldung: 82000
```

## Stille Reserven

Vermögenswerte deren Buchwert geringer ist als der Verkehrswert. Im Status zu addieren (heben die bilanzielle Überschuldung).

```yaml
stille-reserven:
 - position: CNC-Anlage
 buchwert: 95000
 verkehrswert: 180000
 stille-reserve: 85000
 - position: Betriebsgrundstueck
 buchwert: 120000
 verkehrswert: 210000
 stille-reserve: 90000
summe-stille-reserven: 175000
```

## Stille Lasten

Verpflichtungen die in der Handelsbilanz nicht oder zu niedrig passiviert sind. Im Status zu addieren (verschärfen die bilanzielle Überschuldung).

```yaml
stille-lasten:
 - position: Drohende Inanspruchnahme aus Bürgschaft
 bilanziell: 0
 insolvenzrechtlich: 50000
 - position: Pensionsrückstellung Erfüllungsbetrag versus Bilanzwert
 bilanziell: 0
 insolvenzrechtlich: 30000
summe-stille-lasten: 80000
```

## Bereits qualifizierter Rangrücktritt

Forderungen mit qualifiziertem Rangrücktritt (§ 19 Abs. 2 S. 2 InsO) werden im Überschuldungsstatus **nicht passiviert**.

```yaml
qualifizierter-rangruecktritt:
 - glaeubiger: Hauptgesellschafter Karl Mueller
 forderung: Gesellschafterdarlehen vom 15.03.2024
 nennbetrag: 120000
 rangruecktritt-erklaert-am: 2026-05-22
 rangruecktritt-form: notarielle Urkunde # idealtypisch
 bgh-konform: ja # siehe Skill gesellschafterdarlehen-rangrücktritt
```

## Insolvenzrechtlicher Überschuldungsstatus

```
Aktiva (Handelsbilanz) 708.000 EUR
+ stille Reserven 175.000 EUR
- stille Lasten -80.000 EUR
= Insolvenzrechtliche Aktiva 803.000 EUR

Passiva (Handelsbilanz) 790.000 EUR (Aktiva minus EK)
- qualifizierter Rangrücktritt -120.000 EUR
= Insolvenzrechtliche Passiva 670.000 EUR

Differenz 133.000 EUR positiv
```

Ergebnis: trotz **bilanzieller Überschuldung von 82.000 EUR** ist die **insolvenzrechtliche Bilanzbasis positiv** weil stille Reserven und Rangrücktritt dies neutralisieren. Reine Vermögensbilanz **ist nicht ausreichend** — die Fortbestehensprognose ist zusätzlich erforderlich (Skill `annahmen-sammeln-fortfuehrung`).

## Wichtige Hinweise

- Bei **Personengesellschaften ohne natürlich-personige Vollhafter** (z. B. GmbH und Co. KG mit ausschließlich Komplementär-GmbH) gilt § 19 InsO entsprechend.
- Bei **Einzelkaufmann** oder Personengesellschaft mit natürlich-personiger Vollhafter ist § 19 InsO **nicht anwendbar** — Insolvenzantragspflicht ergibt sich nur aus Zahlungsunfähigkeit § 17 InsO.
- Die Erstellung des Status ist **Geschäftsleiter-Pflicht**. Bei Buchführungsmängeln (kein aktueller Stand kein Status möglich) kommt **Bankrott** § 283b StGB in Betracht.

## Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

- `bilanzieller-status.yaml` mit Stichtag Bilanzwerten stillen Reserven Lasten Rangrücktritt und insolvenzrechtlicher Bilanzbasis.
- Erste Ergebnisaussage (insolvenzrechtliche Bilanzbasis positiv / negativ).
- Empfehlung: bei negativer Bilanzbasis ohne Aussicht auf Fortbestehensprognose **sofort** Insolvenzanwalt — § 15a InsO Sechs-Wochen-Frist beginnt zu laufen.


## Aktuelle Leitentscheidungen — Bilanzieller Status

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Bilanzieller Status

§ 19 Abs. 2 InsO (Ueberschuldungsbegriff) → § 19 Abs. 2 S. 2 InsO (qualifizierter Rangruecktritt) → § 35 Abs. 1 InsO (Massebegriff stille Reserven) → HGB §§ 252-255 (Bewertungsgrundsaetze) → IDW S 11 Rn. 20-42 (Status-Ermittlung)

## Triage — Bilanzieller Status

1. **Stichtag festlegen:** Welches Datum hat der Status? (aktuellstes Datum mit verlaesslichen Daten)
2. **Stille Reserven identifizieren:** Grundstuecke zum Buchwert vs. Verkehrswert; Forderungen vs. Marktpreis; Beteiligungen.
3. **Ausserbilanzielle Verpflichtungen:** Pensionen, Buergschaften, noch nicht ausgewiesene Verluste aus schwebenden Geschaeften.
4. **Sanierungsmassnahmen einbeziehen?** Gesellschafterdarlehen mit Rangruecktritt, Patronatserklaerung, Kapitalzufuhr — bereits vorhanden oder noch planerisch?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `comfortletter-weich-erzeugen`

**Fokus:** Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstuetzen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht rechtsverbindlich durchsetzbar. Wirkung Reputation und Banken-Signal. Nicht ausreichend zur Berücksichtigung im insolvenzrechtlichen Status nach § 19 Abs. 2 InsO. Skill erzeugt Dokument plus Warnhinweis dass der Comfortletter die Fortbestehensprognose nicht traegt.

# Comfortletter (weich)

## Wirkung und Grenze

Der Comfortletter ist eine **moralische Unterstützungserklärung** ohne rechtliche Bindung. Er wirkt im Geschäftsverkehr (Bank Lieferant Investor) als **Reputations-Signal**.

**Wirkung im Status der Gesellschaft**:

- **Keine** Berücksichtigung als Aktivposten.
- **Keine** Wirkung auf die Fortbestehensprognose.
- **Reine** Unterstützungsabsichtserklärung.

Wer den Comfortletter mit einer harten externen Patronatserklärung verwechselt schiebt eine **Selbsttaeuschung** in den Status hinein. Bei späterer Insolvenz wird das aufgedeckt; Haftungsrisiko des Geschäftsleiters § 15b InsO und § 43 GmbHG.

## Wann sinnvoll

- **Bank-Signal**: Die Bank verlangt eine schriftliche Unterstützungsabsicht des Mutterunternehmens — nicht als Sicherheit aber als Indikator.
- **Lieferanten-Signal**: Beim Verhandeln mit Lieferanten kann der Comfortletter Vertrauen schaffen.
- **Investor-Signal**: Bei Verhandlungen mit potenziellen Investoren als "Soft Backing".

## Wann NICHT sinnvoll

- Als **alleinige** Maßnahme im Status der Gesellschaft.
- Wenn die Fortbestehensprognose ohne den Comfortletter negativ ist.
- Wenn der Patron tatsächlich bonitaer ist und eine harte Erklärung abgeben könnte (dann sollte er auch).

## Mustervorlage

```
COMFORTLETTER

[Briefkopf des Patrons]

[Datum]

An die Geschäftsführung
der [Firma der Gesellschaft]
[Anschrift]

Sehr geehrte(r) [Anrede Geschäftsführer],

als [Hauptgesellschafter / Mutterunternehmen / Patron] der [Firma der
Gesellschaft] übermitteln wir Ihnen hiermit die folgende
Unterstuetzungsabsichtserklärung:

1. Wir verfolgen mit Interesse die wirtschaftliche Entwicklung der Gesellschaft
und beobachten ihre Lage.

2. Wir beabsichtigen die Gesellschaft für die Erfüllung ihrer wirtschaftlichen
und finanziellen Verpflichtungen im Rahmen unseres unternehmerischen
Beurteilungsspielraums und nach unseren Möglichkeiten zu unterstützen.

3. Diese Erklärung stellt KEINE rechtsverbindliche Garantie und KEINE harte
Patronatserklärung dar. Sie begründet keine einklagbare Verpflichtung uns
gegenüber der Gesellschaft oder ihren Gläubigern.

4. Diese Erklärung kann jederzeit ohne Begründung schriftlich widerrufen
werden.

[Optionale Ergänzung — sehr behutsam]:

5. Wir werden im Falle einer akuten Liquiditätsenge unser unternehmerisches
Urteil dahingehend ausueben möglichst rechtzeitig Maßnahmen zu prüfen.

Mit freundlichen Grüßen

[Patron]
[Position]
```

## Hinweise

- Comfortletter sollte **klar als solchen** bezeichnet werden — keine missverständlichen Formulierungen die als Patronatserklärung gewertet werden könnten (im Streit wird das anhand des Wortlauts geprüft).
- **Schriftlich** und unterzeichnet.
- Im Geschäftsverkehr klar als unverbindlich kommunizieren.

## Ausgabe

- `comfortletter.docx` und PDF.
- Warnhinweis im Sanierungsbausteine-Tracker dass dieser Comfortletter die Prognose NICHT trägt.
- Empfehlung: parallel zum Comfortletter eine harte externe Patronatserklärung mit konkretem Höchstbetrag (Skill `patronatserklaerung-extern-hart-erzeugen`).


## Aktuelle Leitentscheidungen — Comfortletter

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Comfortletter

§ 19 Abs. 2 S. 2 InsO (Passivierungsverbot nur fuer qualifizierten Rangruecktritt) → § 311 BGB (vorvertragliche Haftung aus Comfortletter) → § 241 Abs. 2 BGB (Schutzpflichten) → § 43 GmbHG (Haftung der Konzernmutter)

## Triage — Comfortletter vs. Patronatserklaerung

1. **Zweck?** Bankgespraech, Fortbestehensprognose oder echte rechtliche Sicherung? → Banken akzeptieren oft Comfortletter; Prognose benoetigt harte Patronatserklaerung.
2. **Rechtsbindungswillen?** Comfortletter = keine Rechtsbindung; Patronatserklaerung = verbindlich.
3. **Formulierung?** Vage Formulierungen ("werden unterstuetzen") koennen trotzdem Haftung ausloesen.
4. **Alternative?** Ersetze Comfortletter durch qualifizierten Rangruecktritt oder harte Patronatserklaerung wenn Fortbestehensprognose abgesichert werden soll.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
