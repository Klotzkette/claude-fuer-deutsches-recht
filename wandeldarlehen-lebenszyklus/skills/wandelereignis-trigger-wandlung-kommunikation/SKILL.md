---
name: wandelereignis-trigger-wandlung-kommunikation
description: "Wandelereignis Trigger Wandlung Kommunikation: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Wandelereignis Trigger Wandlung Kommunikation

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Wandelereignis Trigger Wandlung Kommunikation** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `wandelereignis-trigger-dispatcher` | Wandlungstrigger kategorisieren und an den richtigen Folge-Skill weiterleiten wenn Wandelereignis vorliegt. §§ 488 ff. BGB GmbHG SAFE-Terminologie. Prüfraster: Trigger-Typ Qualified Financing Maturity Liquidation Exit Klassifizierung. Output: Trigger-Einordnung Weiterleitung. Abgrenzung: Dispatcher-Skill; Detailarbeit in wandlungsprüfung-trigger-*. |
| `wandlung-kommunikation-paketverteilung` | Kommunikation und Dokumentenversand an alle Beteiligten nach Wandlungsentscheidung organisieren. §§ 130 132 BGB Zugang §§ 15 55 GmbHG. Prüfraster: Empfaengerliste Dokumente Zugang Fristen Bestätigung. Output: Kommunikationsplan Versandprotokoll. Abgrenzung: nicht für inhaltliche Prüfung der Wandlung (wandelereignis-eingang). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Wandelereignis Trigger Wandlung Kommunikation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `wandelereignis-trigger-dispatcher`

**Fokus:** Wandlungstrigger kategorisieren und an den richtigen Folge-Skill weiterleiten wenn Wandelereignis vorliegt. §§ 488 ff. BGB GmbHG SAFE-Terminologie. Prüfraster: Trigger-Typ Qualified Financing Maturity Liquidation Exit Klassifizierung. Output: Trigger-Einordnung Weiterleitung. Abgrenzung: Dispatcher-Skill; Detailarbeit in wandlungsprüfung-trigger-*.

# Master-Dispatcher Wandelereignis

## Zweck

Wenn mehrere Wandlungs-Trigger gleichzeitig oder kurz hintereinander vorliegen können (Qualified Financing parallel zu Exit-Verhandlung, Maturity während Finanzierungs-Phase), braucht es eine Master-Logik die zuerst klärt, welcher Trigger greift und welcher Preis gilt.

## Eingaben

- Wandeldarlehensvertrag (oder mehrere)
- Aktueller Stand pro Trigger (Eingang Vorbereitung Beschluss)
- Bewertungs-Indikatoren (Pre-Money Bewertung in jeder Konstellation)
- Lender-Stand (allein mehrere Konsortium)
- Insolvenz-Lage (drohend oder eingetreten)

## Schritt 1 — Trigger-Inventar

### Drei Standard-Trigger

1. **Qualified Financing** — Finanzierungs-Runde über Schwellenwert
2. **Maturity** — Laufzeit-Ende ohne andere Trigger
3. **Liquidation / Exit / Change of Control** — Verkauf der Gesellschaft IPO Liquidation

### Erweiterte Trigger (vertraglich)

- **Bewertungs-Event** ohne Finanzierungs-Runde (z.B. Independent Valuation)
- **Bonitätsverletzung** (Material Adverse Change)
- **Insolvenz-Eröffnung** Sondertrigger
- **Lender-Optionsrecht** zu festem Zeitpunkt

## Schritt 2 — Parallelität-Prüfung

### Konstellation 1 — Strikt sequentiell

- Nur ein Trigger zu einem Zeitpunkt
- Standard-Fall
- Anwendung einzelner Skill

### Konstellation 2 — Parallel oder eng zeitlich

#### Beispiel A: Qualified Financing in Vorbereitung + Maturity bald

- Lender will warten auf Qualified Financing für besseren Preis
- Gesellschaft will Maturity drücken
- Vertragliche Lösung erforderlich

#### Beispiel B: Liquidation/Exit-Verhandlung + Qualified Financing

- Beide könnten innerhalb von Wochen abschließen
- Lender will den günstigeren Preis
- Cap vs. Discount vs. 1x-Liquidation-Preference

#### Beispiel C: Maturity erreicht + simultane Insolvenz-Eröffnung

- Maturity-Trigger Standard-Bewertung
- Insolvenz reduziert Forderung auf Quote
- Rangrücktritt-Wirkung

## Schritt 3 — Vertragsklausel-Prüfung Master-Logik

### Standard-Klauseln (häufig)

#### "First to Close" / "First to Trigger"

- Der zuerst abschließende / auslösende Trigger gewinnt
- Risiko bei sehr enger Zeit-Lage

#### "Lender Option" (Investor-freundlich)

- Lender wählt zwischen verschiedenen Triggern den günstigsten
- MIN-Preis-Berechnung
- Bei mehreren Lender separate Option pro Lender

#### "MIN-Preis-Formel" (häufig in DE)

- Bei Qualified Financing: MIN(Cap-Preis; Discount-Preis)
- Bei Exit: MIN(Cap-Preis; 1x-Liquidation-Preference)
- Bei Maturity: Fall-back-Bewertung
- → Vergleichs-Rechnung pro Trigger

### Vertragslücke

- Wenn nicht explizit geregelt: ergänzende Vertragsauslegung
- Übung der Branche prüfen
- Anhängige Klage-Risiko hoch — daher Klärung vor Trigger ratsam

## Schritt 4 — Cap-Table-Simulation

### Pre-Money / Post-Money Berechnung pro Trigger

#### Qualified Financing — Cap-Preis

```
Wandlungspreis = Bewertung Cap / Voll-verwaesserte Anteile
oder
Wandlungspreis = Bewertung Investor-Runde × (1 - Discount)

MIN davon = effektiver Wandlungspreis
```

#### Maturity — Fall-back

```
Wandlungspreis = Fall-back-Bewertung / Voll-verwaesserte Anteile
```

#### Liquidation — 1x-Liquidation-Preference

```
Lender-Rückzahlung = Darlehens-Nennwert × 1.0 (non-participating)
oder
Lender-Rückzahlung = Darlehens-Nennwert × 1.0 + Anteils-Beteiligung (participating)

Vergleich:
- Auszahlung als Darlehen (Liquidation-Pref)
- Wandlung zu Cap-Preis und dann Anteils-Beteiligung
- MIN bzw. besser → Lender-Wahl
```

### Beispiel-Rechnung

```
Wandeldarlehen: EUR 500.000
Cap: EUR 5 Mio Pre-Money
Discount: 20 %

Szenario A: Qualified Financing mit Pre-Money EUR 4 Mio
- Cap-Preis: nicht greift (Pre-Money unter Cap)
- Discount-Preis: 4 Mio × 0.80 = effektive Pre-Money 3.2 Mio
- Wandlungspreis Discount günstiger
- Wandlungs-Quote = 500k / 3.2M = 15.6 %

Szenario B: Qualified Financing mit Pre-Money EUR 10 Mio
- Cap-Preis: 5 Mio Pre-Money
- Discount-Preis: 10 Mio × 0.80 = 8 Mio
- Cap-Preis günstiger
- Wandlungs-Quote = 500k / 5M = 10 %

Szenario C: Exit mit Erloes EUR 20 Mio
- Liquidation-Pref: 500k (zurückgezahlt als Darlehen)
- Wandlungs-Alternative: 10 % Anteil = 2 Mio
- Wandlung günstiger → Lender wählt Wandlung

Szenario D: Exit mit Erloes EUR 2 Mio
- Liquidation-Pref: 500k zurückgezahlt
- Wandlungs-Alternative: 10 % Anteil = 200k
- Liquidation-Pref günstiger → Lender nicht wandeln
```

## Schritt 5 — MFN-Kaskade bei mehreren Lender

### Most-Favored-Nation-Klausel

- Lender A bekommt automatisch beste Konditionen aller Lender
- Bei Lender B mit besserem Cap → A bekommt Update

### Berechnungs-Reihenfolge

1. Beste Cap-Konditionen identifizieren
2. Beste Discount-Konditionen identifizieren
3. Pro Lender Vertrags-Update prüfen
4. Cap-Table-Simulation mit aktualisierten Werten

### Bei Konflikt MFN — neu eingetretene Lender mit besserem Cap

- Alte Lender werden besser-gestellt
- Vertragsanpassung erforderlich (oder automatisches Update)

## Schritt 6 — Insolvenz-Sonderfall

### Maturity erreicht + drohende Insolvenz

#### Wenn Insolvenz noch nicht eröffnet

- Maturity-Trigger gilt
- Wandlung zu Fall-back-Bewertung
- Lender Anteilseigner

#### Wenn Insolvenz eröffnet

- **Rangrücktritt** § 39 Abs. 2 InsO gilt
- Lender erhält Quote nachrangig
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Wandlungsoptik problematisch

#### Strategische Optionen

- **Vor Insolvenz** wandeln (Lender wird Anteilseigner — kein Forderungs-Verlust)
- **Aber:** Wandlung kurz vor Insolvenz kann Anfechtungs-Risiko § 130 ff. InsO
- **Bei begründeter Wertvermutung** wandeln = Wahl zwischen Forderungs-Quote und Anteils-Beteiligung

### Praktische Empfehlung

- Frühe Wandlung vor Insolvenz wenn Bewertung gerechtfertigt
- Anwalts-Beratung Anfechtungs-Risiko
- Skill `mandat-triage-insolvenzrecht` parallel

## Schritt 7 — Dispatcher-Logik (Pseudocode)

```
Eingangs-Pruefung:
1. Welche Trigger sind aktiv oder unmittelbar bevorstehend?
2. Vertrags-Klausel zur Prioritaet existent?

Wenn nur ein Trigger:
 Weiterleitung an einzelnen Trigger-Skill

Wenn mehrere Trigger parallel:
 Vertrags-Klausel Prioritaet:
 "First to Close" → naechster abschliessender Trigger
 "Lender Option" → MIN-Preis-Berechnung pro Trigger
 + Lender-Wahl
 "MIN-Preis-Formel" → Vergleichs-Berechnung
 + automatische Wahl
 Vertragsluecke → Auslegungs-Empfehlung
 + Klage-Risiko-Warnung

Wenn Maturity + Insolvenz:
 Sonderpruefung Rangruecktritt
 + Anfechtungs-Risiko
 + Skill Schnittstelle zu Insolvenz

Cap-Table-Simulation pro Option:
 - Pre-Money / Post-Money
 - Lender-Anteils-Quote
 - Verwaesserungs-Effekt Gruender
 - Vergleichs-Tabelle aller Optionen
```

## Schritt 8 — Output-Empfehlung an Mandant

### Beratungs-Memo

```
1. Trigger-Analyse: Welche Trigger aktiv / bevorstehend?
2. Vertrags-Klausel-Pruefung: Prioritaets-Regelung?
3. Cap-Table-Simulation alle Trigger-Optionen
4. Empfehlung guenstigste Option (Lender-Sicht)
 oder strategischste Option (Gesellschaft-Sicht)
5. Form-Anforderungen § 15 GmbHG iVm zu Wandlung
6. Zeit-Plan und naechste Schritte
7. Risiko-Hinweise (Anfechtung Insolvenz Steuer)
```

### Schriftsatz-Bausteine

- Wandlungs-Erklärung Lender
- Gesellschafterbeschluss-Vorbereitung
- HR-Anmeldung-Skelett

## Schritt 9 — Zeitlicher Ablauf bei Parallel-Trigger

### Beispiel Qualified Financing + Maturity

```
Tag -30: Qualified Financing Term Sheet
Tag -14: Maturity Frist beginnt Zwei-Wochen-Mahnung
Tag 0: Maturity-Zeitpunkt

Strategie Lender:
- Vor Tag -14 entscheiden ob Maturity-Wandlung guenstiger
- Sonst auf Qualified Financing warten
- Beachten: bei Cap unter Qualified Financing
 Pre-Money → Qualified Financing automatisch besser

Strategie Gesellschaft:
- Maturity nicht unnoetig durch Verzoegerung gefaehrden
- Qualified Financing nicht durch Wandlungs-Diskussion stoppen
- Mediation moeglich
```

## Schritt 10 — Beratungs-Konstellationen

### Lender-Sicht

- Optimieren Wandlungs-Preis
- Beste Anteils-Quote
- Rang in Cap-Table
- Verwässerungs-Schutz

### Gesellschaft-Sicht

- Cap-Table-Bereinigung
- Folge-Finanzierung erleichtern
- Gründer-Verwässerung begrenzen
- Compliance Form-Anforderungen

### Konflikt-Mediation

- Bei Lender vs. Gesellschaft uneinige Trigger-Wahl
- Vertragsauslegung
- Schiedsklausel-Aktivierung

## Verzahnung mit anderen Skills

- `wandlungspruefung-trigger-qualified-financing` — Detail-Berechnung
- `wandlungspruefung-trigger-maturity` — Detail Maturity
- `wandlungspruefung-trigger-liquidation` — Detail Exit
- `cap-table-update-pre-post` — nach Wandlung
- `wandlungsmechanik-konzipieren` — Vertrags-Klausel-Design vor Trigger
- `mehrere-wandeldarlehen-parallel` — MFN-Kaskade
- `mandat-triage-wandeldarlehen` — Eingangs-Routing
- `mandat-triage-insolvenzrecht` — Insolvenz-Sonderfall

## Ausgabe

- `wandelereignis-master-{az}.md` mit Trigger-Inventar Vertragsklausel-Prüfung Cap-Table-Simulation
- Vergleichs-Tabelle Optionen
- Empfehlung mit Begründung
- Schriftsatz-Bausteine
- Frist im Fristenbuch (Maturity-Datum Qualified-Financing-Closing-Datum etc.)
- Risiko-Memo Insolvenz Anfechtung Steuer

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- BGB §§ 133 157 § 15 GmbHG
- InsO §§ 39 130 131 133
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- IDW S 11
- Weitnauer Handbuch VC
- Greuer Wandeldarlehensvertrag

## 2. `wandlung-kommunikation-paketverteilung`

**Fokus:** Kommunikation und Dokumentenversand an alle Beteiligten nach Wandlungsentscheidung organisieren. §§ 130 132 BGB Zugang §§ 15 55 GmbHG. Prüfraster: Empfaengerliste Dokumente Zugang Fristen Bestätigung. Output: Kommunikationsplan Versandprotokoll. Abgrenzung: nicht für inhaltliche Prüfung der Wandlung (wandelereignis-eingang).

# Wandlung – Kommunikation und Paketverteilung

## Zweck

Dieser Skill koordiniert alle Kommunikationsmaßnahmen nach der Wandlungsentscheidung: Bestätigungsschreiben, Mitwirkungsaufforderungen und Buchungsanweisungen an alle beteiligten Stellen. Phase C des Lebenszyklus.

## Eingaben

- Bestätigte Wandlungsberechnung (aus `wandlungspreis-berechnung`)
- Adressen aller Parteien (Lender, Gesellschaft, Gesellschafterinnen, Steuerberater, Buchhaltung)
- Datum der Wandlungserklärung und der Bestätigung
- Cap-Table Post-Money (aus `cap-table-update-pre-post`)
- Buchungsanweisungen: Ausbuchung Verbindlichkeit (Darlehensbetrag + Zinsen), Einbuchung Eigenkapital

## Rechtlicher Rahmen

### Primärnormen
- § 4.9 Wandeldarlehensvertrag (Gesellschaft beruft unverzüglich Gesellschafterversammlung ein)
- § 5 Wandeldarlehensvertrag (Mitwirkungspflichten Gesellschafterinnen)
- § 272 Abs. 2 Nr. 4 HGB (Kapitalrücklage nach Einlage der Forderung)
- § 246 HGB (Vollständigkeit der Buchführung)
- § 8 Wandeldarlehensvertrag (Vertraulichkeit – an wen darf kommuniziert werden?)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Bestätigungsschreiben an Lender
Inhalt: Bestätigung der Wandlungserklärung, Wandlungssumme (Darlehen + Zinsen), berechnete neue Anteile (Zahl, Nennwert), vorgesehener Termin Kapitalerhöhungsbeschluss, vorgesehener Notar.

### 2. Aufforderungsschreiben an Gesellschaft (Geschäftsführerin)
Inhalt: Einberufungspflicht gemäß § 4.9, Frist (unverzüglich, spätestens innerhalb zwei Wochen), Tagesordnungspunkte (Kapitalerhöhung gegen Sacheinlage, Bezugsrechtsverzicht, Aufnahme Lender), Notar-Beauftragung.

### 3. Schreiben an Gesellschafterinnen (Mitwirkungspflicht)
Inhalt: Hinweis auf § 5 des Wandeldarlehensvertrags (Mitwirkungspflicht), Einladung zur Gesellschafterversammlung, Beschlussthemen, Bitte um Anwesenheitsbestätigung oder Vollmacht.

### 4. Mitteilung an Steuerberater
Inhalt: Wandlungsdaten (Betrag, Datum, neue Gesellschafterstruktur), neue Cap-Table als Anlage, Bitte um steuerliche Würdigung (Wandlung als Tausch nach § 20 UmwStG analog?).

### 5. Buchungsanweisung an Buchhaltung
Soll-Buchung: Verbindlichkeit Wandeldarlehen (Darlehen + aufgelaufene Zinsen) auflösen. Haben-Buchung: Stammkapital (Nennbetrag neue Anteile) und Kapitalrücklage (Rest) erhöhen. Buchungssatz: per Verbindlichkeit Wandeldarlehen an Gezeichnetes Kapital und Kapitalrücklage.

### 6. Dokumentation und Archivierung
Alle Schreiben mit Sendenachweis archivieren (Textform-Anforderung). Kommunikationsstatus im Aktenstammblatt vermerken.

## Beispiel-Buchungssatz

```
Buchungstag: [Eintragungsdatum Handelsregister]

Soll:
 Verbindlichkeit Wandeldarlehen Northstar: EUR 275694

Haben:
 Gezeichnetes Kapital (§ 272 Abs. 1 HGB): EUR 7
 Kapitalrücklage (§ 272 Abs. 2 Nr. 4 HGB): EUR 275687
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Buchhaltung bucht Darlehen erst nach Fälligkeit aus | Bilanzunklarheit | Buchung verzögert | Buchung zeitnah mit Eintragung |
| Steuerberater nicht informiert | Steuerliche Risiken unerkannt | Informiert nach HR-Eintragung | Sofort informiert |
| Gesellschafterinnen nicht eingeladen | Mitwirkungspflicht verletzt | Einladung verspätet | Rechtzeitige Einladung |
| Kommunikation gegen Vertraulichkeitsklausel | § 8-Verstoß | Empfänger nicht § 8-berechtigt | Alle Empfänger § 8 lit. a berechtigt |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/gesellschafterversammlung-einberufen/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/post-eintragung-checkliste/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung HGB § 272 oder UmwStG § 20 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 47 Abs. 4 GmbHG (Stimmverbot eigene Sache) → § 40 GmbHG (Gesellschafterliste nach Wandlung) → § 53 Abs. 1 GmbHG (Zustimmung Gesellschafter zur Satzungsänderung) → § 16 GmbHG (Legitimationswirkung) → §§ 130, 132 BGB (Zugang Erklärungen)
