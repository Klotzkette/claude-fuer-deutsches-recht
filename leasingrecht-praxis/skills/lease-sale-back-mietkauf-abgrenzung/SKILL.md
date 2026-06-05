---
name: lease-sale-back-mietkauf-abgrenzung
description: "Lease Sale Back Mietkauf Abgrenzung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Sale Back Mietkauf Abgrenzung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Sale Back Mietkauf Abgrenzung** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-010-sale-and-lease-back-liquiditaet-und-insolvenzanfechtun` | Sale-and-Lease-Back: Strukturierung, Liquiditätswirkung, Bilanzierung, Insolvenzanfechtung (§§ 129 ff. InsO) und steuerliche Behandlung. |
| `lease-011-mietkauf-abgrenzung-eigentumsuebergang` | Mietkauf vs. Leasing: Abgrenzung, automatischer Eigentumsübergang, steuerliche und bilanzielle Folgen, AGB-Wirksamkeit. |
| `lease-020-bilanzierung-hgb-ifrs-und-wirtschaftliches-eigentum` | Leasingbilanzierung: HGB (BMF-Erlass, wirtschaftliches Eigentum § 39 AO), IFRS 16 (Right-of-Use-Asset), steuerliche Folgen und Bilanzoptimierung. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Sale Back Mietkauf Abgrenzung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-010-sale-and-lease-back-liquiditaet-und-insolvenzanfechtun`

**Fokus:** Sale-and-Lease-Back: Strukturierung, Liquiditätswirkung, Bilanzierung, Insolvenzanfechtung (§§ 129 ff. InsO) und steuerliche Behandlung.

# Sale-and-Lease-Back: Liquidität, Bilanzierung und Insolvenzanfechtung

## Zweck

Sale-and-Lease-Back (SLB) ermöglicht es Unternehmen, bereits vorhandene Anlagegüter zu verkaufen und gleichzeitig zu leasen. Ziel ist meist Liquiditätsbeschaffung ohne Betriebsunterbrechung. Dieser Skill analysiert die Struktur, Bilanzierungsfolgen, Insolvenzanfechtungsrisiken und steuerliche Auswirkungen.

## Struktur einer SLB-Transaktion

### Grundkonstruktion
1. **Verkauf**: Unternehmen (künftiger LN) verkauft Objekt an LG (§ 433 BGB, Kaufvertrag)
2. **Leasing**: LG vermietet/verleast das Objekt zurück an Verkäufer als LN
3. **Effekt**: Unternehmen erhält Kaufpreis (Liquidität), behält aber Nutzung

### Wirtschaftliche Funktion
- Bilanzbereinigung (Off-Balance, wenn Finanzierungsleasing beim LG verbleibt)
- Freisetzung stiller Reserven
- Finanzierung ohne Kreditaufnahme im klassischen Sinn
- Alternative zu Asset-backed Security oder Factoring

## Zivilrechtliche Einordnung

### Kaufvertrag und Eigentumsübergang
- Vollständiger Eigentumsübergang erforderlich (§§ 929–931 BGB)
- Bei beweglichen Sachen: Übergabe oder Abtretung des Herausgabeanspruchs (§ 931 BGB)
- Bei Immobilien: Auflassung und Grundbucheintragung (§§ 873, 925 BGB)

### Scheingeschäft-Risiko (§ 117 BGB)
Falls die Parteien in Wirklichkeit keinen Eigentumsübergang wollen, sondern nur eine Kreditbesicherung: Scheingeschäft nichtig. Dahinter liegendes Sicherungsgeschäft nach §§ 1204 ff. BGB (Pfandrecht) oder Sicherungsübereignung beachten.

## Insolvenzanfechtung (§§ 129 ff. InsO)

### Anfechtungsrisiken bei SLB

**§ 133 InsO (Vorsätzliche Benachteiligung)**: 10-Jahresfrist
- Wenn SLB mit Benachteiligungsvorsatz gegenüber Gläubigern abgeschlossen wurde
- Insolvenzverwalter kann Eigentumsübergang anfechten → Objekt fällt zurück in Masse
- LG verliert Eigentum und hat nur Insolvenzforderung (Kaufpreisrückzahlung)

**§ 134 InsO (Unentgeltliche Leistung)**: 4-Jahresfrist
- SLB zum symbolischen Kaufpreis (unter Verkehrswert) kann anfechtbar sein

**§ 131 InsO (Inkongruente Deckung)**: 3-Monatsfrist
- SLB kurz vor Insolvenz → inkongruente Sicherung?

### Schutzmaßnahmen für LG
- Due Diligence: Finanzlage des LN zum Zeitpunkt der SLB prüfen
- Kaufpreis: Marktgerechter Preis (nicht unter Buchwert)
- Zeitpunkt: Je weiter von Insolvenz entfernt, desto geringer das Anfechtungsrisiko
- Gutachten: Marktwertgutachten für Kaufpreisnachweis

## Bilanzierung

### HGB (beim LN)
- Wenn wirtschaftliches Eigentum bei LG (BMF-Erlass): Off-Balance für LN; Kauferlös = Liquidität, kein Anlagevermögen mehr
- Wenn wirtschaftliches Eigentum beim LN: Rückkauf ins Anlagevermögen, Kauferlös = Verbindlichkeit

### IFRS 16 (SLB-Regelung)
IFRS 16 §§ 98–103 regeln SLB gesondert:
- Wenn Verkauf ein echter Verkauf ist (§ 15 IFRS 9): RoU-Asset + Leasingverbindlichkeit beim LN; Gewinn nur anteilig erfasst
- Wenn kein echter Verkauf (Finanzierungstransaktion): Keine Ausbuchung; Zufluss als Darlehen behandeln

### Steuerliche Behandlung
- Verkauf: Steuerpflichtiger Veräußerungsgewinn, wenn Buchwert < Marktpreis
- Leasing: Raten als Betriebsausgabe beim LN (wenn LG wirtschaftlicher Eigentümer)
- Stille Reserven werden aufgedeckt → Steuerlast im Verkaufsjahr!

## Prüfprogramm

1. Eigentumsübergang rechtswirksam vollzogen? (§§ 929–931 BGB)
2. Kaufpreis marktgerecht? Gutachten vorhanden?
3. Scheingeschäft-Risiko: Wollen Parteien wirklich Eigentümer wechseln?
4. Insolvenzanfechtung: Zeitpunkt, Finanzlage LN, Benachteiligungsvorsatz?
5. Bilanzierung HGB vs. IFRS 16: Echter Verkauf oder Finanzierungstransaktion?
6. Steuerpflichtiger Veräußerungsgewinn eingeplant?

## Typische Fallen

- SLB als Krisenmaßnahme kurz vor Insolvenz → Anfechtungsrisiko § 133 InsO hoch
- Kaufpreis unter Verkehrswert → unentgeltliche Leistung (§ 134 InsO)
- IFRS 16 unterschätzt: Gewinn nicht vollständig realisierbar
- Stille Reservenauflösung steuerlich nicht geplant

## Normen und Quellen

- §§ 929–931 BGB (Eigentumsübertragung): https://dejure.org/gesetze/BGB/929.html
- §§ 129–134 InsO (Anfechtung): https://www.gesetze-im-internet.de/inso/__129.html
- § 117 BGB (Scheingeschäft): https://dejure.org/gesetze/BGB/117.html
- IFRS 16 §§ 98–103 (SLB): https://eur-lex.europa.eu
- BMF-Schreiben Leasingerlass: https://www.bundesfinanzministerium.de
- BGH IX ZR 250/05 (Insolvenzanfechtung SLB): https://www.bgh.de

## Output-Formate

- **SLB-Strukturübersicht**: Kaufvertrag, Leasingvertrag, Eigentümerfluss
- **Anfechtungsrisiko-Matrix**: Zeitpunkt – Anfechtungsgrund – Frist – Schutzmaßnahme
- **IFRS-16-Buchung**: Echte vs. unechte SLB-Transaktion
- **Steuer-Memo**: Veräußerungsgewinn, AfA, Leasingraten-Abzug

## 2. `lease-011-mietkauf-abgrenzung-eigentumsuebergang`

**Fokus:** Mietkauf vs. Leasing: Abgrenzung, automatischer Eigentumsübergang, steuerliche und bilanzielle Folgen, AGB-Wirksamkeit.

# Mietkauf und Leasing: Abgrenzung und Eigentumsübergang

## Zweck

Mietkauf und Finanzierungsleasing werden im Alltag oft verwechselt. Die rechtliche und steuerliche Unterscheidung ist jedoch erheblich: Beim Mietkauf geht das Eigentum kraft Vertragsrecht über; beim Leasing (Regelfall) verbleibt es beim Leasinggeber. Dieser Skill klärt die Abgrenzungskriterien, den Eigentumsübergangsmechanismus und die steuerlichen Konsequenzen.

## Rechtliche Abgrenzung

### Leasing (Regelfall)
- LG bleibt zivilrechtlicher und (steuerlich) wirtschaftlicher Eigentümer
- LN nutzt das Objekt gegen Zahlung von Leasingraten
- Am Ende: Rückgabe, Kaufoption (zu marktgerechtem Preis) oder Andienungsrecht

### Mietkauf
- LN wird kraft Vertrages Eigentümer nach Zahlung der vereinbarten Raten (automatischer Eigentumsübergang)
- Oder: Kaufoption zu symbolischem Preis (nahe Null oder weit unter Restwert)
- Wirtschaftlicher Zweck: Kreditkauf in Raten

**Steuerrechtlich**: Wenn wirtschaftliches Eigentum schon von Beginn beim LN → Aktivierung beim LN (§ 39 AO, BMF-Leasingerlass)

## Abgrenzungskriterien (BMF-Erlass, BFH-Rspr.)

| Kriterium | Leasing | Mietkauf |
|---|---|---|
| Eigentumsübergang | Nicht automatisch | Automatisch nach Ratenzahlung |
| Kaufoption | Zu marktgerechtem Preis | Zu symbolischem/weit unter Buchwert |
| Laufzeit | 40–90 % der Nutzungsdauer | Oft entspricht ND |
| Bilanzierung LN | Beim LG (Regelfall) | Beim LN |
| AfA | Beim LG | Beim LN |
| Finanzierungsleasing-BGH | Amortisationsrisiko bei LN | LN erwirbt wirtschaftliches Eigentum |

## BGH-Rechtsprechung

**BGH VIII ZR 26/03**: Kaufoption zu einem Preis, der weit unter dem zu erwartenden Restwert liegt, begründet wirtschaftliches Eigentum des LN → steuerlich Mietkauf, nicht Leasing.

**BGH VIII ZR 220/08**: Automatischer Eigentumsübergang bei vollständiger Ratenzahlung = Mietkauf; § 433 BGB (Kaufrecht) anwendbar, nicht nur Mietrecht.

## Steuerliche Konsequenzen

### Wenn wirtschaftliches Eigentum beim LN (Mietkauf)
- LN aktiviert das Wirtschaftsgut (§ 246 HGB, § 39 AO)
- LN nimmt AfA vor
- Leasingraten (oder Mietkaufraten) = Tilgung + Zinsanteil
- Nur Zinsanteil ist Betriebsausgabe (wie bei Darlehen)

### Wenn wirtschaftliches Eigentum beim LG (Leasing)
- LG aktiviert, nimmt AfA vor
- LN: Gesamte Leasingrate als Betriebsausgabe
- Bilanzsumme beim LN geringer (Off-Balance)

## AGB-Wirksamkeit

### Eigentumsübergangsklauseln
- Automatischer Eigentumsübergang nach AGB-Recht grundsätzlich zulässig
- Bei Verbrauchern: Muss transparent sein (§ 307 I 2 BGB)
- Kaufpreis nahe Null: Steuerlich als Schenkung zu bewerten?

### Verbraucher-Mietkauf
- §§ 506–509 BGB: Verbraucherleasing als entgeltliche Finanzierungshilfe
- Mietkauf gegenüber Verbrauchern: §§ 491 ff. BGB (Verbraucherdarlehen) gelten analog
- Pflichtangaben: Gesamtbetrag, effektiver Jahreszins, Zahlungsplan

## Prüfprogramm

1. Wie ist der Eigentumsübergang vertraglich geregelt? Automatisch oder durch Kaufoption?
2. Kaufoptionspreis: Marktgerecht oder symbolisch?
3. Verhältnis Laufzeit zu Nutzungsdauer?
4. BMF-Erlass-Zurechnung: LG oder LN?
5. Steuerliche Buchführung: Wer aktiviert, wer nimmt AfA?
6. Verbraucher: Pflichtangaben nach §§ 506–509 BGB oder §§ 491 ff. BGB?

## Typische Fallen

- Vertrag als „Leasing" bezeichnet, ist aber steuerlich Mietkauf → Nachaktivierung
- AfA fälschlicherweise beim LN oder LG → steuerliche Korrekturen und Nachzahlungen
- Verbraucher: Fehlendes Widerrufsrecht, weil Vertrag falsch klassifiziert
- Insolvenz: Mietkauf-LN hat Aussonderungsrecht? Nein – Eigentumsübergang erst nach Ratenzahlung abgeschlossen

## Normen und Quellen

- § 39 AO (wirtschaftliches Eigentum): https://www.gesetze-im-internet.de/ao_1977/__39.html
- § 433 BGB (Kaufvertrag): https://dejure.org/gesetze/BGB/433.html
- §§ 491 ff. BGB (Verbraucherdarlehen): https://dejure.org/gesetze/BGB/491.html
- §§ 506–509 BGB (Verbraucherleasing): https://dejure.org/gesetze/BGB/506.html
- BGH VIII ZR 26/03 (Kaufoption unter Restwert): https://www.bgh.de
- BMF-Schreiben 19.04.1971 (Leasingerlass): https://www.bundesfinanzministerium.de
- BFH IX R 14/15: https://www.bfh.de

## Output-Formate

- **Abgrenzungsmatrix**: Leasing vs. Mietkauf nach 8 Kriterien
- **Steuer-Memo**: Aktivierung, AfA, Betriebsausgaben im Vergleich
- **Vertrags-Redline**: Eigentumsübergangsklausel rechtskonform formulieren

## 3. `lease-020-bilanzierung-hgb-ifrs-und-wirtschaftliches-eigentum`

**Fokus:** Leasingbilanzierung: HGB (BMF-Erlass, wirtschaftliches Eigentum § 39 AO), IFRS 16 (Right-of-Use-Asset), steuerliche Folgen und Bilanzoptimierung.

# Leasingbilanzierung: HGB, § 39 AO und IFRS 16

## Zweck

Die Bilanzierungsfrage – bei wem wird das Leasingobjekt aktiviert – hat direkte Auswirkungen auf Bilanzkennzahlen, Steuerlast und Rating. Dieser Skill erklärt die HGB-Bilanzierungsgrundsätze (BMF-Erlasse, § 39 AO), die IFRS-16-Methodik und die Optimierungsmöglichkeiten.

## HGB-Bilanzierung: Wirtschaftliches Eigentum

### § 39 AO: Wirtschaftliches Eigentum
Wirtschaftsgüter sind demjenigen zuzurechnen, der die tatsächliche Herrschaft ausübt, wenn er den zivilrechtlichen Eigentümer für die gewöhnliche Nutzungsdauer ausschließen kann.

### BMF-Leasingerlasse

**Erlass 19.04.1971 (Vollamortisation)**:
- Zurechnung beim **LG** (Regelfall) wenn:
 - Grundmietzeit 40–90 % der betriebsgewöhnlichen Nutzungsdauer UND
 - Kein Anzeichen für wirtschaftliches Eigentum des LN
- Zurechnung beim **LN** wenn:
 - Grundmietzeit < 40 % oder > 90 % der Nutzungsdauer ODER
 - Kaufoption zu Preis erheblich unter Buchwert

**Erlass 22.12.1975 (Teilamortisation)**:
- Grundsatz: Zurechnung beim LG
- Ausnahme (Zurechnung beim LN):
 - Andienungsrecht führt zu Erwerbspflicht des LN
 - Kündigung und Restwert führen wirtschaftlich zu Eigentumsübergang

### Bilanzausweis HGB

**Zurechnung beim LG (Regelfall)**:
- LG: Aktivierung Anlagegüter; AfA; Leasingforderungen als Umlaufvermögen
- LN: Keine Aktivierung; Leasingraten als Aufwand; Off-Balance

**Zurechnung beim LN (Ausnahme)**:
- LN: Aktivierung + AfA; Verbindlichkeit gegenüber LG
- LG: Forderung gegen LN (Darlehenscharakter)

## IFRS 16: Right-of-Use-Asset (ab 01.01.2019)

### Grundkonzept
IFRS 16 verpflichtet **alle Leasingnehmer** (unabhängig vom Leasingtyp), ein Nutzungsrecht (Right-of-Use Asset, RoU) und eine Leasingverbindlichkeit anzusetzen.

### Erstansatz
**RoU-Asset** (Erstbewertung):
= Barwert der Leasingzahlungen + Vorauszahlungen + anfängliche direkte Kosten + Rückbaukosten (soweit zu schätzen)

**Leasingverbindlichkeit** (Erstbewertung):
= Barwert der künftigen Leasingzahlungen, diskontiert mit dem Grenzfremdkapitalzinssatz

**Folgebewertung**:
- RoU: Linearer Abschreibung (oder nach Nutzungsintensität)
- Verbindlichkeit: Effektivzinsmethode (ähnlich Amortisationstabelle); Zinsen = Aufwand

### Ausnahmen (kein RoU/Verbindlichkeit)
1. Kurzfristige Verträge (Laufzeit ≤ 12 Monate, § IFRS 16.B34)
2. Geringwertige Objekte (praktische Grenze: ≤ 5.000 USD Neupreis)

### Auswirkungen auf Kennzahlen
| Kennzahl | Auswirkung IFRS 16 |
|---|---|
| Bilanzsumme | Steigt (RoU + Verbindlichkeit) |
| Eigenkapitalquote | Sinkt (Bilanzsumme wächst) |
| EBITDA | Steigt (Raten → Abschreibung + Zinsen, nicht in EBITDA) |
| EBIT | Neutral bis leicht positiv (Abschreibung < alte Ratengröße) |
| Verschuldungsgrad | Steigt (Leasingverbindlichkeit) |

## Steuerliche Bilanzierung

- §§ 4, 5 EStG: Steuerliche Bilanzierung folgt Handelsbilanz (Maßgeblichkeit, modifiziert)
- § 39 AO-Zurechnung ist für Steuerbilanz maßgeblich
- AfA nur bei demjenigen, dem wirtschaftliches Eigentum zugerechnet wird
- Gewerbesteuer: 25 % der Finanzierungsanteile der Leasingraten werden hinzugerechnet (§ 8 Nr. 1d GewStG): faktische Hinzurechnung von 1/4 der Raten

## Prüfprogramm

1. Anwendbares Rechnungslegungsstandard: HGB oder IFRS?
2. BMF-Erlass: Welche Fallgruppe? Grundmietzeit / Nutzungsdauer / Option?
3. IFRS 16: Ausnahmen (kurzfristig, geringwertig) anwendbar?
4. Erstansatz RoU-Asset und Verbindlichkeit berechnen: Barwert, Zinssatz
5. Gewerbesteuerliche Hinzurechnung (§ 8 Nr. 1d GewStG) eingeplant?
6. Bilanzkennzahlen nach Erstansatz IFRS 16 – Rating-Auswirkungen?

## Typische Fallen

- IFRS 16 nicht angewendet → Bilanz inkorrekt, Prüfer bemängeln
- Grenzfremdkapitalzinssatz zu niedrig angesetzt → Leasingverbindlichkeit zu hoch
- Gewerbesteuerliche Hinzurechnung übersehen → Steuernachzahlung
- RoU-Asset zu hoch (Rückbaukosten überschätzt) → Wertberichtigung später

## Normen und Quellen

- § 39 AO (wirtschaftliches Eigentum): https://www.gesetze-im-internet.de/ao_1977/__39.html
- BMF-Schreiben 19.04.1971: https://www.bundesfinanzministerium.de
- BMF-Schreiben 22.12.1975: https://www.bundesfinanzministerium.de
- IFRS 16 (EU-konsolidiert): https://eur-lex.europa.eu
- § 8 Nr. 1d GewStG (Hinzurechnung): https://www.gesetze-im-internet.de/gewstg/__8.html
- BFH IX R 14/15 (Leasingerlass): https://www.bfh.de

## Output-Formate

- **Bilanzierungs-Entscheidungsbaum**: HGB oder IFRS → Zurechnung LG oder LN
- **IFRS-16-Erstansatz-Berechnung**: Tabellenvorlage mit Barwert und Zinssatz
- **Gewerbesteuer-Memo**: Hinzurechnung § 8 Nr. 1d GewStG
- **Kennzahlen-Auswirkungsanalyse**: Vorher/Nachher IFRS 16
