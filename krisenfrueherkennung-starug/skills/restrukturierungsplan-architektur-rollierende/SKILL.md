---
name: restrukturierungsplan-architektur-rollierende
description: "Restrukturierungsplan Architektur Rollierende: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Restrukturierungsplan Architektur Rollierende

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Restrukturierungsplan Architektur Rollierende** im Plugin Krisenfrüherkennung (StaRUG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `restrukturierungsplan-architektur-paragraph-7ff-starug` | StaRUG-Restrukturierungsplan nach §§ 7 ff. StaRUG architektieren: Schuldner oder Berater plant außergerichtliche Sanierung unter StaRUG. Normen: §§ 7 ff. StaRUG (Planbestandteile), § 9 StaRUG (Gruppenbildung), § 25 StaRUG (Mehrheitserfordernisse), § 60 StaRUG (gerichtliche Planbestätigung). Prüfraster: Planbestandteile vollständig, Gruppenbildung nach Gläubiger-Rang, Mehrheitserfordernisse, Schlechterstellungsverbot § 30 StaRUG. Output Restrukturierungsplan-Entwurf-Geruest, Gruppen-Matrix, Zeitplan. Abgrenzung: Cram-Down siehe cross-class-cram-down-und-absolute-priority; Stabilisierungsanordnung siehe stabilisierungsanordnung-und-vollstreckungssperre. |
| `rollierende-liquiditaetsplanung-24-monate-template` | Rollierende 24-Monats-Liquiditaetsplanung nach StaRUG erstellen: Sanierungsberater oder GF braucht Liquiditaets-Forecast. Normen: § 1 StaRUG (24-Monats-Horizont), Fortbestehensprognose, Sanierungskonzept. Prüfraster: Woechentliche Granularitaet Wochen 1-13, monatliche Granularitaet Monate 14-24, Stresstests, Sensitivitaetsanalysen, Maßnahmenbrücke, StaRUG-konforme Dokumentation. Output Excel-Template Liquiditaetsplanung, Stresstest-Szenarios, Dokumentationsprotokoll. Abgrenzung: Integrierte GuV/Bilanz/CF-Planung siehe integrierte-planung-guv-bilanz-cashflow; Ampel-KPIs siehe kennzahlenset-und-ampelsystem-starug-konform. |
| `spezial-ampelsystem-beweislast-und-darlegungslast` | Ampelsystem: Beweislast, Darlegungslast und Substantiierung im Plugin krisenfrueherkennung starug; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Krisenfrüherkennung (StaRUG) gilt für **Restrukturierungsplan Architektur Rollierende**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `restrukturierungsplan-architektur-paragraph-7ff-starug`

**Fokus:** StaRUG-Restrukturierungsplan nach §§ 7 ff. StaRUG architektieren: Schuldner oder Berater plant außergerichtliche Sanierung unter StaRUG. Normen: §§ 7 ff. StaRUG (Planbestandteile), § 9 StaRUG (Gruppenbildung), § 25 StaRUG (Mehrheitserfordernisse), § 60 StaRUG (gerichtliche Planbestätigung). Prüfraster: Planbestandteile vollständig, Gruppenbildung nach Gläubiger-Rang, Mehrheitserfordernisse, Schlechterstellungsverbot § 30 StaRUG. Output Restrukturierungsplan-Entwurf-Geruest, Gruppen-Matrix, Zeitplan. Abgrenzung: Cram-Down siehe cross-class-cram-down-und-absolute-priority; Stabilisierungsanordnung siehe stabilisierungsanordnung-und-vollstreckungssperre.

# Restrukturierungsplan — Architektur nach §§ 7 ff. StaRUG

Der Restrukturierungsplan ist das Herzstück des StaRUG-Verfahrens. Er ist das Instrument, mit dem Gläubigerforderungen gestundet, herabgesetzt und umstrukturiert werden können — ohne Insolvenzverfahren, ohne Publizität, ohne öffentliche Schande. Die Voraussetzungen für einen wirksamen Plan sind anspruchsvoll. Wer den Plan schlecht strukturiert, scheitert spätestens an der Abstimmung oder der gerichtlichen Bestätigung. Ein handwerklich sauberer Plan erfordert die enge Verzahnung von betriebswirtschaftlichem Sanierungskonzept und juristischer Planarchitektur.

---

## Rechtsgrundlagen

- §§ 7-14 StaRUG (Inhalt des Restrukturierungsplans)
- § 9 StaRUG (Gruppenbildung)
- §§ 17-24 StaRUG (Planabstimmung)
- § 25 StaRUG (Mehrheitserfordernisse)
- § 26 StaRUG (gerichtliche Planbestätigung — Cross-Class-Cram-Down)
- §§ 27-29 StaRUG (Bestätigungsvoraussetzungen)
- § 30 StaRUG (Schlechterstellungsverbot)
- § 31 StaRUG (Obstruktionsverbot)
- IDW S 6 (Sanierungskonzept als Plangrundlage)

---

## Pflichten

### 1. Planbestandteile — §§ 7-14 StaRUG

Der Restrukturierungsplan besteht aus zwei zwingenden Teilen:

**Darstellender Teil (§ 7 StaRUG):**
- Beschreibung der wirtschaftlichen Lage des Schuldners
- Ursachen der Krise
- Maßnahmen zur Restrukturierung
- Auswirkungen auf die Beteiligten
- Angaben zur Finanzierung des Plans

**Gestaltender Teil (§ 8 StaRUG):**
- Konkrete Gestaltung der Rechte der Planbetroffenen (Stundung, Erlass, Umwandlung)
- Gruppenbildung (§ 9 StaRUG)
- Regelungen für jeden Beteiligten

**Plananlagen (§ 14 StaRUG):**
- Vergleichsrechnung (Besserstellung gegenüber Insolvenz)
- Fortführungsprognose / integrierter Finanzplan (mind. 24 Monate)
- Erklärungen nach § 14 Abs. 1 StaRUG

### 2. Gruppenbildung — § 9 StaRUG

Die Gruppenbildung ist das rechtliche Grundgerüst des Plans:

**Pflichtgruppen:**
- Gruppe der gesicherten Gläubiger (Absonderungsrechte)
- Gruppe der nicht nachrangigen ungesicherten Gläubiger
- Gruppe der Anteilsinhaber (Gesellschafter)

**Fakultative Gruppen** (nach Interessenlage sinnvoll):
- Arbeitnehmer (wenn ihre Forderungen gestaltet werden)
- Kleingläubiger (Vereinfachungsgruppe, Grenzwert frei wählbar)
- Operationelle Gläubiger (strategisch wichtige Lieferanten)
- Nachrangige Verbindlichkeiten

**Kriterien für Gruppenbildung (§ 9 Abs. 1 StaRUG):**
- Gläubiger mit gleichartigem wirtschaftlichen Interesse in einer Gruppe
- Keine willkürliche Zersplitterung zur Mehrheitsbeschaffung
- Transparenz gegenüber Gericht

### 3. Mehrheitserfordernisse — § 25 StaRUG

In jeder Gruppe muss die Abstimmung eine **Dreiviertelmehrheit der Stimmrechte** erreichen:

```
ABSTIMMUNGSQUORUM:
 Erforderlich: ≥ 75 % der Stimmrechte in jeder Gruppe
 Stimmrechte: i.d.R. nach Forderungshöhe
 Anwesende: Kein Quorum für Anwesenheit (anders als § 76 InsO)

MEHRHEIT NICHT ERREICHT:
 → Gruppe gilt als ablehnend
 → Cross-Class-Cram-Down prüfen (§ 26 StaRUG)
```

### 4. Schlechterstellungsverbot — § 30 StaRUG

Kein Planbetroffener darf durch den Plan schlechter gestellt werden als im nächstbesten Alternativszenario (i.d.R. Regelinsolvenzverfahren oder geordnete Liquidation):

```
VERGLEICHSRECHNUNG (Plananlagen):
 Spalte A: Stellung im Plan (Zahlungen, Quoten, Besicherungen)
 Spalte B: Stellung im hypothetischen Insolvenzverfahren
 Ergebnis: Plan darf Spalte B nicht unterschreiten

 Ausnahme: Einzelner Gläubiger stimmt freiwillig zu trotz Schlechterstellung
 (§ 26 Abs. 1 S. 2 StaRUG)
```

---

## Vorgehen

### Schritt 1: Planungsphase

1. **Gläubigeranalyse:** Alle Planbetroffenen identifizieren, Forderungshöhen klären
2. **Sanierungskonzept** nach IDW S 6 als Grundlage
3. **Integrierter Finanzplan** (24 Monate) erstellen und validieren
4. **Gruppenbildung** konzipieren — Interessengleichheit prüfen
5. **Szenarien** durchrechnen: Wie viel Erlass/Stundung braucht der Plan?

### Schritt 2: Plangestaltung

**Typische Gestaltungselemente:**

| Instrument | Wirkung | Anwendungsfall |
|---|---|---|
| Stundung | Verschiebung von Fälligkeiten | Liquiditätsengpass kurzfristig |
| Teilerlass | Reduktion der Forderungshöhe | Überschuldungssituation |
| Zinssatz-Reduktion | Senkung des Schuldendienstes | Covenant-Problem |
| Umwandlung in EK | Debt-to-Equity-Swap | Eigenkapitalstärkung |
| Sicherheitentausch | Neue Sicherheiten gegen alte | Sicherheitenkonflikte |
| Anteilsübertragung | Neuer Gesellschafter | Gesellschafterwechsel als Teil der Sanierung |

### Schritt 3: Abstimmungsverfahren

Zwei Optionen:

**Option A — Außergerichtliche Abstimmung:**
- Plan wird Planbetroffenen mit Annahmefrist übermittelt
- Dreiviertelmehrheit je Gruppe erforderlich
- Bei Einigkeit: Keine gerichtliche Bestätigung nötig (aber empfehlenswert)

**Option B — Gerichtliches Abstimmungsverfahren (§§ 45 ff. StaRUG):**
- Gericht setzt Abstimmungstermin an
- Strukturiertes Verfahren mit Protokoll
- Cross-Class-Cram-Down bei ablehnenden Gruppen möglich (§ 26 StaRUG)

### Schritt 4: Gerichtliche Planbestätigung

Voraussetzungen für Bestätigung (§ 29 StaRUG):

- Dreiviertelmehrheit in jeder abstimmenden Gruppe (oder Cross-Class-Cram-Down)
- Kein Verstoß gegen Schlechterstellungsverbot (§ 30 StaRUG)
- Plan ist nicht offensichtlich ungeeignet zur nachhaltigen Restrukturierung
- Keine Stimmrechtsmissbrauch oder sittenwidrige Gruppenbildung

---

## Templates

### Muster: Planstruktur-Übersicht (Inhaltsverzeichnis)

```
RESTRUKTURIERUNGSPLAN — [FIRMA GMBH]

DARSTELLENDER TEIL
 § 1 Wirtschaftliche Lage und Krisenursachen
 § 2 Bisherige Sanierungsmaßnahmen
 § 3 Restrukturierungskonzept und Maßnahmen
 § 4 Auswirkungen auf Planbetroffene
 § 5 Finanzierung des Plans

GESTALTENDER TEIL
 § 6 Planbetroffene Gläubiger und Gruppenbildung
 § 7 Gestaltung der Rechte Gruppe 1 — Gesicherte Gläubiger
 § 8 Gestaltung der Rechte Gruppe 2 — Ungesicherte Gläubiger
 § 9 Gestaltung der Rechte Gruppe 3 — Gesellschafter
 § 10 Planbedingungen und Inkrafttreten

ANLAGEN
 Anlage 1: Vergleichsrechnung (Insolvenz vs. Plan)
 Anlage 2: Integrierter Finanzplan (24 Monate)
 Anlage 3: Fortführungsprognose
 Anlage 4: Gläubigerliste
 Anlage 5: Sanierungsgutachten [IDW S 6]
```

---

## Fallstricke

1. **Willkürliche Gruppenbildung** — Gericht prüft, ob die Gruppen nach § 9 StaRUG wirtschaftlich homogen sind. Taktische Gruppenbildung zur Mehrheitsbeschaffung ist ein Versagungsgrund.

2. **Vergleichsrechnung zu optimistisch** — unterschätzte Insolvenzquote erleichtert zwar das Schlechterstellungsverbot, ist aber angreifbar, wenn Gläubiger widersprechen.

3. **Fehlende IDW S 6-Grundlage** — ohne valides Sanierungskonzept als Basis fehlt dem darstellenden Teil die Substanz. Das Gericht und widersprechende Gläubiger werden die Pläne kritisch prüfen.

4. **Plan zu spät eingebracht** — bei eingetretener ZU ist das Verfahren nicht mehr zulässig. Plan muss bei drohender ZU gestellt werden.

5. **Kleingläubiger vergessen** — faktische Kleingläubiger, die nicht in den Plan einbezogen wurden, können außerhalb des Plans weiterhin vollstrecken.

---

## Querverweise

- → `cross-class-cram-down-und-absolute-priority` — Durchsetzung gegen ablehnende Gruppen
- → `stabilisierungsanordnung-und-vollstreckungssperre` — Schutz während Planentwicklung
- → `restrukturierungsbeauftragter-und-sachwalter` — externe Aufsicht
- → `drohende-zahlungsunfaehigkeit-paragraph-18-inso` — Zugangsvoraussetzung
- → `fortbestehensprognose-zweistufig` — Plananlage Fortführungsprognose


## Aktuelle Leitentscheidungen — StaRUG-Plan-Architektur

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Plan-Architektur

§ 7 StaRUG (Planinhalt allgemein) → § 8 StaRUG (darstellender Teil) → § 9 StaRUG (gestaltender Teil) → § 10 StaRUG (Gruppen) → § 11 StaRUG (Anlagen) → §§ 14-19 StaRUG (Planbetroffene) → §§ 60-66 StaRUG (gerichtliche Bestaetigung)

## Triage — Plan-Architektur Check

1. **Darstellender Teil vollstaendig?** Ausgangslage, Krisenursachen, Sanierungskonzept, Massnahmen, Vergleichsrechnung.
2. **Gestaltender Teil praezise?** Forderungstabelle, Quoten, Stundungen, Sicherheiten klar bezeichnen.
3. **Gruppen korrekt?** Homogenitaet je Gruppe sichergestellt?
4. **Anlagen?** Integrierten Finanzplan, Sanierungsgutachten, Beteiligten-Listen als Anlagen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `rollierende-liquiditaetsplanung-24-monate-template`

**Fokus:** Rollierende 24-Monats-Liquiditaetsplanung nach StaRUG erstellen: Sanierungsberater oder GF braucht Liquiditaets-Forecast. Normen: § 1 StaRUG (24-Monats-Horizont), Fortbestehensprognose, Sanierungskonzept. Prüfraster: Woechentliche Granularitaet Wochen 1-13, monatliche Granularitaet Monate 14-24, Stresstests, Sensitivitaetsanalysen, Maßnahmenbrücke, StaRUG-konforme Dokumentation. Output Excel-Template Liquiditaetsplanung, Stresstest-Szenarios, Dokumentationsprotokoll. Abgrenzung: Integrierte GuV/Bilanz/CF-Planung siehe integrierte-planung-guv-bilanz-cashflow; Ampel-KPIs siehe kennzahlenset-und-ampelsystem-starug-konform.

# Rollierende Liquiditätsplanung — 24-Monate-Template

Die rollierende Liquiditätsplanung ist das operative Herzstück des § 1 StaRUG-Frühwarnsystems. Sie zeigt nicht nur, wo das Unternehmen heute steht, sondern wo es in zwei Jahren stehen wird — und welche Handlungskorridore noch offen sind. Ohne eine valide 24-Monats-Liquiditätssicht ist die Behauptung, drohende Zahlungsunfähigkeit nicht rechtzeitig erkannt zu haben, im Nachhinein nicht zu entkräften.

---

## Rechtsgrundlagen

- § 1 StaRUG (Krisenfrüherkennungspflicht, 24-Monats-Horizont)
- § 18 InsO (drohende Zahlungsunfähigkeit — Prognosezeitraum)
- § 29 Abs. 2 StaRUG (Zugangsvoraussetzung: drohende ZU muss vorliegen)
- Berufsständische Methodenlogik zu Fortbestehensprognose und Sanierungskonzepten: Liquiditätsplanung ist nur ein Baustein; bei Sanierungsaussagen müssen GuV, Bilanz, Maßnahmen, Leitbild und Dokumentation hinzukommen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

### Schritt 6: Brücke zum Sanierungskonzept

Wenn der 24-Monats-Plan Bank, Gläubiger, StaRUG, Schutzschirm oder Insolvenzplan tragen soll, ergänze:

- Krisenursache je Engpass.
- Leitbild des sanierten Unternehmens.
- Maßnahmenlog mit Verantwortlichem, Kosten, Timing, GuV-/Bilanz-/Liquiditätseffekt und Nachweis.
- Plan-GuV und Planbilanz.
- Base Case und plausible Downside.
- Annahmen-, Quellen- und Planversionsregister.

Ohne diese Brücke ist die Planung ein Liquiditätsforecast, aber noch kein Sanierungskonzept.

---

## Templates

### Muster: Excel-Spaltenstruktur (Auszug Wochen 1-4 + Monat 14)

```
Kategorie | KW01 | KW02 | KW03 | KW04 | ... | M14 | M15
--------------------------|-------|-------|-------|-------|-----|-------|------
ZUFLÜSSE | | | | | | |
 Umsatzerlöse (netto) | [tsd] | [tsd] | [tsd] | [tsd] | | [tsd] | [tsd]
 Anzahlungen | [tsd] | [tsd] | [tsd] | [tsd] | | [tsd] | [tsd]
 Kreditziehung | | | | | | |
= ZUFLÜSSE GESAMT | [Sum] | [Sum] | [Sum] | [Sum] | | [Sum] | [Sum]
 | | | | | | |
ABFLÜSSE | | | | | | |
 Material | [tsd] | [tsd] | [tsd] | [tsd] | | [tsd] | [tsd]
 Personal | [tsd] | | | [tsd] | | [tsd] | [tsd]
 Miete / Leasing | [tsd] | | | | | [tsd] | [tsd]
 Zinsen | | | | | | [tsd] | [tsd]
 Tilgung | | | | | | [tsd] | [tsd]
 USt-Voranmeldung | [tsd] | | | | | [tsd] | [tsd]
 Sonstiges | [tsd] | [tsd] | [tsd] | [tsd] | | [tsd] | [tsd]
= ABFLÜSSE GESAMT | [Sum] | [Sum] | [Sum] | [Sum] | | [Sum] | [Sum]
 | | | | | | |
NETTO-CASHFLOW | [Net] | [Net] | [Net] | [Net] | | [Net] | [Net]
KASSENBESTAND (Anfang) | [K] | [K] | [K] | [K] | | [K] | [K]
KASSENBESTAND (Ende) | [K] | [K] | [K] | [K] | | [K] | [K]
FREIE KREDITLINIE | [L] | [L] | [L] | [L] | | [L] | [L]
GESAMTLIQUIDITÄT | [G] | [G] | [G] | [G] | | [G] | [G]
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

4. **Zu optimistische Planprämissen** sind keine "konservative Schätzung" — Gerichte prüfen ex post, ob die Annahmen zum Zeitpunkt der Planung plausibel waren. Überhöhte Umsatzerwartungen ohne Begründung sind Haftungsrisiko.

5. **Kreditlinie als Puffer einplanen, ohne Verlängerungsrisiko zu beachten** — ausgelaufene Kreditlinien, die stillschweigend als verlängert angenommen werden, verfälschen die Liquiditätssicht erheblich.

6. **Liquiditätsplan als Sanierungskonzept behandeln** — eine positive Liquiditätskurve belegt nicht automatisch nachhaltige Sanierungsfähigkeit. Ertragskraft, Bilanz, Krisenursachen, Leitbild und Maßnahmen müssen separat plausibilisiert werden.

---

## Querverweise

- → `fruehwarnsystem-architektur-zwei-jahres-horizont` — Systemarchitektur
- → `integrierte-planung-guv-bilanz-cashflow` — Drei-Statement-Verbindung
- → `kennzahlenset-und-ampelsystem-starug-konform` — KPI-Schwellen
- → `drohende-zahlungsunfaehigkeit-paragraph-18-inso` — Prognosezeitraum
- → `fortbestehensprognose-zweistufig` — IDW S 11-Nutzung der Liquiditätsplanung


## Weitere Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?

## 3. `spezial-ampelsystem-beweislast-und-darlegungslast`

**Fokus:** Ampelsystem: Beweislast, Darlegungslast und Substantiierung im Plugin krisenfrueherkennung starug; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Ampelsystem: Beweislast, Darlegungslast und Substantiierung

## Spezialwissen: Ampelsystem: Beweislast, Darlegungslast und Substantiierung
- **Spezialgegenstand:** Ampelsystem: Beweislast, Darlegungslast und Substantiierung / ampelsystem beweislast und darlegungslast. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StaRUG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Ampelsystem** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## Frühwarn-Ampelsystem (§ 1 StaRUG)
- **GRÜN (Normalbetrieb):**
 - Liquiditätsplan 24 Monate zeigt durchgehend Deckung > 110 Prozent.
 - Kovenanten mit > 20-Prozent-Spielraum.
 - Cash-Reichweite > 6 Monate.
- **GELB (Beobachtungspflicht erhöht):**
 - Liquiditätsdeckung 100–110 Prozent oder Kovenanten unter 20-Prozent-Spielraum.
 - Externer Schock (Großkunde verliert Bonität, Auftragseinbruch > 20 Prozent).
 - Reaktion: Maßnahmenplan mit Verantwortlichen und Fristen, Information Gesellschafter und ggf. Aufsichtsrat.
- **ROT (drohende ZU § 18 InsO):**
 - Liquiditätsdeckung in einzelnen Perioden < 100 Prozent im 24-Monats-Horizont.
 - Reaktion: StaRUG-Anzeige § 31 StaRUG erwägen, Sanierungskonzept IDW S6 starten, Restrukturierungsbeauftragter § 73 StaRUG.

## Beweislast und Darlegungslast
- **Im Innenverhältnis (§ 43 GmbHG / § 93 AktG):** Geschäftsführer trägt Darlegungs- und Beweislast für Sorgfaltspflicht-Erfüllung (Beweislastumkehr) — d. h. Geschäftsführer muss zeigen, dass er ein **Frühwarnsystem** eingerichtet, **Indikatoren überwacht** und **angemessen reagiert** hat.
- **Im Anfechtungsprozess (§§ 129 ff. InsO):** Insolvenzverwalter trägt für jeden Anfechtungstatbestand die Beweislast — Indizien-Rechtsprechung des BGH erleichtert dies für § 133 InsO.
- **Bei Haftung § 15a Abs. 4 InsO Strafverfahren:** Strafverfolgungsbehörde trägt Beweislast — aber **Indizwirkung** der dokumentierten oder fehlenden Frühwarnung.

## Substantiierungspflicht des Geschäftsführers
- Datierte Liquiditätspläne, Sensitivitäten, Maßnahmenprotokolle.
- Beschlussfassung Gesellschafter / Aufsichtsrat zu Sanierungsmaßnahmen.
- Berater-Mandate und Berichte.
- Dokumentation der ex-ante-Sicht: was war im Entscheidungszeitpunkt bekannt, welche Annahmen waren vernünftig?

## Trade-off
- Frühwarnsystem kostet Ressourcen — Mindeststandard skaliert mit Unternehmensgröße. Bei kleiner GmbH wird kein vollumfängliches BI-System verlangt, aber zumindest Quartals-Liquidität mit Ausschau.
