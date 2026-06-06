---
name: zusammenfuehren
description: "Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueberwiegende Wahrscheinlichkeit dass das Unternehmen im Prognosezeitraum zahlungsfähig bleibt (mehr als 50 Prozent). IDW S 11 Massstab. Schaltet bei Bedarf den Skill `sanierungsbausteine-vorschlagen` aus oder eskaliert über `wenn-prognose-negativ-naechste-schritte` zum Insolvenzanwalt im Fortbestehensprognose: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Fortbestehensprognose zusammenführen

## Arbeitsbereich

Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueberwiegende Wahrscheinlichkeit dass das Unternehmen im Prognosezeitraum zahlungsfähig bleibt (mehr als 50 Prozent). IDW S 11 Massstab. Schaltet bei Bedarf den Skill `sanierungsbausteine-vorschlagen` aus oder eskaliert über `wenn-prognose-negativ-naechste-schritte` zum Insolvenzanwalt. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), BGH II ZR 296/05 (Drei-Wochen-Lücke), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Maßstab

§ 19 Abs. 2 InsO seit SanInsFoG 2021: "Die Fortführung des Unternehmens ist nach den Umständen überwiegend wahrscheinlich" — Prognosezeitraum **zwölf Monate**.

**Überwiegend wahrscheinlich** bedeutet **mehr als 50 Prozent** Wahrscheinlichkeit (klassische BGH-Rspr. zur Vorhersage; bestätigt durch IDW S 11).

### Operativ — was bedeutet das?

Die abstrakte Wahrscheinlichkeitsformel ist methodisch durch die **Zahlungsfähigkeitsprognose** zu fuellen. Die Fortbestehensprognose ist genau dann positiv wenn das Unternehmen über den Zwölf-Monats-Horizont mit überwiegender Wahrscheinlichkeit **nicht in die Zahlungsunfähigkeit nach § 17 InsO gerät**. Das bedeutet konkret:

- In jedem Zeitabschnitt der zwölf Monate müssen **mindestens 90 Prozent** der dann fälligen Verbindlichkeiten aus den verfügbaren Mitteln (Liquiditätsbestand plus Kreditlinie plus rechtzeitig erzielbare Zufluesse) gedeckt werden können.
- Maßstab: BGH-Linie zum 10-%-/3-Wochen-Schema (Zahlungsstockung vs. Zahlungsunfähigkeit). Konkrete Aktenzeichen vor Ausgabe über dejure.org / openjur.de mit Datum und Randnummer verifizieren.

Wenn die Liquiditätsplanung in jedem Zeitabschnitt diese Schwelle einhaelt — auch im plausibilisierten Negativ-Szenario — ist die Fortbestehensprognose **positiv**. Wenn die Schwelle in einem oder mehreren Zeitabschnitten oder über laengere Phasen reisst und auch durch Sanierungsbausteine nicht verbindlich geschlossen werden kann ist die Prognose **negativ**.

Die "mehr als 50 Prozent Wahrscheinlichkeit" der Prognose ist also nicht abstrakt zu vermuten sondern aus dem Liquiditätsplan und seiner Sensitivitaet abzuleiten: über das Basis-Szenario hinaus muss auch das **plausible Negativ-Szenario** die Schwelle einhalten — andernfalls reicht die Wahrscheinlichkeit nicht aus.

## Abgrenzung zur Sanierungsfähigkeit

Die positive Fortbestehensprognose ist nicht automatisch ein tragfähiges Sanierungskonzept. Sie beantwortet primär die insolvenzrechtliche Zahlungsfähigkeitsfrage. Sanierungsfähigkeit geht weiter:

- **Fortbestehensprognose:** Kann das Unternehmen im Prognosezeitraum überwiegend wahrscheinlich zahlungsfähig bleiben?
- **Sanierungsfähigkeit:** Ist das Unternehmen nach Maßnahmen wieder dauerhaft wettbewerbs-, rendite- und finanzierungsfähig?
- **Sanierungskonzept:** Verbindet Ausgangslage, Krisenursachen, Leitbild, Maßnahmen, integrierte GuV-/Bilanz-/Liquiditätsplanung, Szenarien und Dokumentation.

Wenn der Nutzer Bankgespräch, StaRUG, Schutzschirm, Eigenverwaltung, Insolvenzplan oder Sanierungskonzept nennt, nach der Fortbestehensprognose ausdrücklich den Sanierungsfähigkeits-Check empfehlen. Eine einmalige Finanzierungszusage kann die Fortbestehensprognose tragen, aber trotzdem kein nachhaltig saniertes Geschäftsmodell ergeben.

## Prüfablauf

### Schritt 1 — Bilanzielle Überschuldung gegeben?

Aus Skill `bilanzieller-status-aufnehmen`:

- Bilanzielle Überschuldung gegeben? Wenn nein: § 19 InsO nicht erfüllt — Fortbestehensprognose **nicht erforderlich** (aber häufig sinnvoll als Krisendokumentation).
- Wenn ja: weiter zu Schritt 2.

### Schritt 2 — Annahmen plausibilisiert?

Aus Skill `annahmen-belastbarkeit-plausibilisieren`:

- Annahmen überwiegend **realistisch** oder **konservativ**?
- Maximal eine oder zwei **ambitionierte** Annahmen die nicht tragend sind?
- **Nicht-belastbare** Annahmen ausgeschlossen?

Wenn die Annahmen die das Ergebnis tragen ambitioniert oder nicht-belastbar sind: Prognose **nicht positiv**.

### Schritt 3 — Liquidität über 12 Monate positiv

Aus Skill `liquiditaet-12-monate`:

- **Basis-Szenario** positiv über alle zwölf Monate?
- **Negativ-Szenario** mit zumutbaren Maßnahmen abdeckbar?
- **Stress-Szenario** zumindest mit zusätzlichen Maßnahmen (Patronatserklärung Gesellschafterdarlehen) abdeckbar?

### Schritt 4 — Gesamtbewertung

Drei mögliche Ergebnisse:

#### A. Prognose positiv

- Bilanzbild trotz Überschuldung positiv (stille Reserven Rangrücktritt).
- Liquidität über zwölf Monate positiv im Basis-Szenario und im Negativ-Szenario.
- Annahmen plausibel und überwiegend belegt.
- Sanierungsmaßnahmen falls noch erforderlich umgesetzt oder vertraglich gesichert.

**Folge**: Keine insolvenzrechtliche Überschuldung nach § 19 Abs. 2 InsO. Antragspflicht entfaellt insoweit. **Aber**: Zahlungsfähigkeit § 17 InsO und drohende Zahlungsunfähigkeit § 18 InsO bleiben **eigene** Prüfungspunkte — siehe Plugin `insolvenzrecht`.

#### B. Prognose positiv mit Sanierungsmaßnahmen

- Ohne Maßnahmen waere die Prognose negativ.
- Mit konkreten umsetzbaren Maßnahmen ist die Prognose positiv.

**Folge**: Maßnahmen müssen tatsächlich umgesetzt werden. Skill `sanierungsbausteine-vorschlagen` mit konkreten Vorschlägen.

**Wichtig**: Maßnahmen müssen **rechtzeitig** umgesetzt und **verbindlich** sein:

- Patronatserklärung **schriftlich unterzeichnet** und vom Patron einsehbar.
- Gesellschafterdarlehen **mit qualifiziertem Rangrücktritt** notariell.
- Stundungsvereinbarungen **schriftlich** mit Gläubigern.
- Forderungsverzichte **schriftlich** ggf. mit Besserungsschein.

#### C. Prognose negativ

- Liquidität über zwölf Monate **nicht sicherstellbar**.
- Sanierungsmaßnahmen reichen nicht.
- Keine ausreichende Patronage- / Gesellschafterstuetzung.

**Folge**:
- **Insolvenzrechtliche Überschuldung gegeben** (§ 19 InsO).
- **Antragspflicht** sechs Wochen nach Eintritt § 15a Abs. 1 S. 2 InsO.
- **Sofort Insolvenzanwalt** einschalten — Skill `wenn-prognose-negativ-naechste-schritte`.
- Prüfung **drohende Zahlungsunfähigkeit** § 18 InsO mit StaRUG-Option (Prognosezeitraum 24 Monate).

## Stichtag und Dokumentation

Die Prognose ist immer auf den **Stichtag des Tages** zu beziehen an dem sie erstellt wird. Das Verhältnis Stichtag → 12 Monate ist rollierend.

```yaml
prognose-zusammenfassung:
 prognose-id: FP-2026-0001
 stichtag: 2026-05-20
 geschaeftsleiter: Mueller, Hans (GF GmbH XYZ)
 prognose-horizont: 2026-06 bis 2027-05

 bilanzbild:
 bilanzielle-ueberschuldung: ja (Höhe 82000 EUR)
 insolvenzrechtliche-bilanzbasis: positiv (133000 EUR)
 rangruecktritt: Gesellschafterdarlehen 120000 EUR
 stille-reserven: 175000 EUR

 liquiditaet:
 basis-szenario: positiv
 negativ-szenario: positiv knapp (Endbestand Monat 11 bei 8000 EUR)
 stress-szenario: negativ ohne Patronatserklärung positiv mit

 annahmen-belastbarkeit:
 realistisch: 7
 konservativ: 2
 ambitioniert: 1 (Kostensenkung Standortschliessung)
 nicht-belastbar: 0

 sanierungsmassnahmen-erforderlich: ja
 konkret-belegt:
 - Patronatserklärung Hauptgesellschafter 200000 EUR (unterzeichnet)
 - Gesellschafterdarlehen 120000 EUR mit Rangrücktritt (notariell)
 - Stundungsvereinbarungen Lieferanten (schriftlich von 5 Lieferanten)
 noch-offen:
 - Stundung Bank Tilgung (in Verhandlung — noch nicht schriftlich)

 ergebnis: positiv-mit-maßnahmen
 bewertung-wahrscheinlichkeit: überwiegend (mehr als 50 Prozent)

 pflicht-ueberpruefung: vierteljaehrlich oder bei wesentlicher Änderung
```

## Sonderfall — der konkrete Tag der Erstellung zählt

- Die Prognose ist **stichtagsbezogen**.
- Bei einer wesentlichen Änderung der Annahmen (Wegfall Hauptkunde Verlust Kreditlinie) muss die Prognose **neu erstellt** werden.
- Bei vierteljaehrlicher Routineprüfung — Dokumentation der laufenden Prüfung als Beweis für aktive Pflichterfüllung des Geschäftsleiters.

## Ausgabe

- `prognose-zusammenfassung.md` mit Stichtag Bewertung Beleg-Status.
- Weiterleitung an:
 - `sanierungsbausteine-vorschlagen` wenn Maßnahmen erforderlich.
 - `wenn-prognose-negativ-naechste-schritte` wenn Ergebnis negativ.
 - `prognose-dokumentation-stichtag` zur abschließenden Dokumentation.

## Aktuelle Leitentscheidungen — Zusammenfuehren der Prognose (Stand Mai 2026)

- **BGH IX ZR 285/14 vom 26.01.2017** — Steuerberater haftet bei verfehlter Fortbestehensprognose auf Insolvenzvertiefungsschaden. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>
- **BGH IX ZR 56/22 vom 29.06.2023** — Drittschutzwirkung der Hinweis- und Warnpflicht des Beraters zugunsten des (faktischen) GF. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen GF; bei negativer Prognose nach Amtsniederlegung weiterhin Haftungsexposition. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- Konkrete BGH-Linie zu IDW S 11-konformer Prognose-Plausibilität und qualifiziertem Rangrücktritt vor Ausgabe über dejure.org / openjur.de verifizieren.

## Paragrafenkette Prognose-Zusammenfuehren

§ 19 Abs. 2 InsO (Fortbestehensprognose als zweite Stufe Ueberschuldung) → IDW S 11 Rn. 60-90 (Ergebnis und Dokumentation) → § 15a InsO (Antragspflicht bei negativer Prognose) → § 15b InsO (Haftungsrisiko)

## Triage — Prognose-Ergebnis

1. **Positiv (Prognose grueen)?** → Dokumentieren (IDW S 11 Vorlage), Wiedervorlage in 3 Monaten, Sanierungsbausteine weiterverfolgen.
2. **Knapp positiv (mit Massnahmen)?** → Massnahmen konkretisieren und terminieren; Sicherheitsmarge pruefen.
3. **Negativ?** → Sofort `wenn-prognose-negativ-naechste-schritte` ausfuehren; Anwalt einschalten; Antragspflicht pruefen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
