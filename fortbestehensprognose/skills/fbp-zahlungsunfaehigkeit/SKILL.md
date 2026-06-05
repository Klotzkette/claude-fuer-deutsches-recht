---
name: fbp-zahlungsunfaehigkeit
description: "FBP Zahlungsunfaehigkeit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# FBP Zahlungsunfaehigkeit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **FBP Zahlungsunfaehigkeit** im Plugin Fortbestehensprognose (IDW S 11). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fbp-zahlungsunfaehigkeit-ueberschuldungsabgrenzung-spezial` | Spezialfall Abgrenzung Zahlungsunfaehigkeit und Ueberschuldung § 17 / § 19 InsO: Liquiditaetsstatus 21-Tage-Frist, Fortfuehrungsprognose, BGH-Rechtsprechung. Pruefraster fuer Geschaeftsleitung. |
| `fortbestehensprognose-zusammenfuehren` | Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueberwiegende Wahrscheinlichkeit dass das Unternehmen im Prognosezeitraum zahlungsfähig bleibt (mehr als 50 Prozent). IDW S 11 Massstab. Schaltet bei Bedarf den Skill `sanierungsbausteine-vorschlagen` aus oder eskaliert über `wenn-prognose-negativ-naechste-schritte` zum Insolvenzanwalt. |
| `fp-cash-flow-modell-spezial` | Spezialfall Cash-Flow-Modell: monatliche Liquiditaetsplanung mindestens fuer 12 Monate, Plausibilitaetskontrollen, Sensitivitaetsanalysen. Pflichten Geschaeftsfuehrer und Pruefer. Pruefraster und Praxistipps. |

## Arbeitsweg

Im Plugin Fortbestehensprognose (IDW S 11) gilt für **FBP Zahlungsunfaehigkeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fbp-zahlungsunfaehigkeit-ueberschuldungsabgrenzung-spezial`

**Fokus:** Spezialfall Abgrenzung Zahlungsunfaehigkeit und Ueberschuldung § 17 / § 19 InsO: Liquiditaetsstatus 21-Tage-Frist, Fortfuehrungsprognose, BGH-Rechtsprechung. Pruefraster fuer Geschaeftsleitung.

# FBP: Zahlungsunfaehigkeit Ueberschuldung

## Spezialwissen: FBP: Zahlungsunfaehigkeit Ueberschuldung
- **Spezialgegenstand:** FBP: Zahlungsunfaehigkeit Ueberschuldung / fbp zahlungsunfaehigkeit ueberschuldungsabgrenzung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO, BGH, FBP.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `fortbestehensprognose-zusammenfuehren`

**Fokus:** Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueberwiegende Wahrscheinlichkeit dass das Unternehmen im Prognosezeitraum zahlungsfähig bleibt (mehr als 50 Prozent). IDW S 11 Massstab. Schaltet bei Bedarf den Skill `sanierungsbausteine-vorschlagen` aus oder eskaliert über `wenn-prognose-negativ-naechste-schritte` zum Insolvenzanwalt.

# Fortbestehensprognose zusammenführen

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

## 3. `fp-cash-flow-modell-spezial`

**Fokus:** Spezialfall Cash-Flow-Modell: monatliche Liquiditaetsplanung mindestens fuer 12 Monate, Plausibilitaetskontrollen, Sensitivitaetsanalysen. Pflichten Geschaeftsfuehrer und Pruefer. Pruefraster und Praxistipps.

# FP: Cash-Flow-Modell

## Spezialwissen: FP: Cash-Flow-Modell
- **Spezialgegenstand:** FP: Cash-Flow-Modell / fp cash flow modell spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FP.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
