---
name: fortbestehensprognose-zusammenfuehren
description: Fuehrt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueberwiegende Wahrscheinlichkeit dass das Unternehmen im Prognosezeitraum zahlungsfaehig bleibt (mehr als 50 Prozent). IDW S 11 Massstab. Schaltet bei Bedarf den Skill `sanierungsbausteine-vorschlagen` aus oder eskaliert ueber `wenn-prognose-negativ-naechste-schritte` zum Insolvenzanwalt.
---

# Fortbestehensprognose zusammenführen

## Maßstab

§ 19 Abs. 2 InsO seit SanInsFoG 2021: "Die Fortführung des Unternehmens ist nach den Umständen überwiegend wahrscheinlich" — Prognosezeitraum **zwölf Monate**.

**Überwiegend wahrscheinlich** bedeutet **mehr als 50 Prozent** Wahrscheinlichkeit (klassische BGH-Rspr. zur Vorhersage; bestätigt durch IDW S 11).

### Operativ — was bedeutet das?

Die abstrakte Wahrscheinlichkeitsformel ist methodisch durch die **Zahlungsfähigkeitsprognose** zu fuellen. Die Fortbestehensprognose ist genau dann positiv wenn das Unternehmen über den Zwölf-Monats-Horizont mit überwiegender Wahrscheinlichkeit **nicht in die Zahlungsunfähigkeit nach § 17 InsO gerät**. Das bedeutet konkret:

- In jedem Zeitabschnitt der zwölf Monate müssen **mindestens 90 Prozent** der dann fälligen Verbindlichkeiten aus den verfügbaren Mitteln (Liquiditätsbestand plus Kreditlinie plus rechtzeitig erzielbare Zufluesse) gedeckt werden können.
- **Vorübergehende Unterdeckungen** über zehn Prozent dürfen höchstens **drei Wochen** dauern und müssen mit überwiegender Wahrscheinlichkeit binnen dieser Frist wieder geschlossen werden (BGH IX ZR 123/04, BGHZ 163, 134).

Wenn die Liquiditätsplanung in jedem Zeitabschnitt diese Schwelle einhaelt — auch im plausibilisierten Negativ-Szenario — ist die Fortbestehensprognose **positiv**. Wenn die Schwelle in einem oder mehreren Zeitabschnitten oder über laengere Phasen reisst und auch durch Sanierungsbausteine nicht verbindlich geschlossen werden kann ist die Prognose **negativ**.

Die „mehr als 50 Prozent Wahrscheinlichkeit" der Prognose ist also nicht abstrakt zu vermuten sondern aus dem Liquiditätsplan und seiner Sensitivitaet abzuleiten: über das Basis-Szenario hinaus muss auch das **plausible Negativ-Szenario** die Schwelle einhalten — andernfalls reicht die Wahrscheinlichkeit nicht aus.

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
