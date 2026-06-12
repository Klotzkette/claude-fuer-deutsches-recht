---
name: anspruchsgrundlage-rechtsfolgen-b2b-vs
description: "Vertragliche Klauseln nach der Wenn-Dann-Architektur bauen. Klare Trennung von Tatbestand (Wenn-Teil mit Voraussetzungen) und Rechtsfolge (Dann-Teil mit Pflichten und Fristen). Anwendungsbeispiele: Maengelhaftung Verzugsklausel Kuendigungsfolgenklausel. Anti-Pattern Mantelklausel mit verschachtel..."
---

# Anspruchsgrundlage und Rechtsfolgen-Klauseln

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DSGVO Art. 33 Datenpanne 72h, ZPO § 130d aktive beA-Nutzung seit 01.01.2022, GwG § 8 Aufbewahrung 5 Jahre, KI-VO Art. 50 Kennzeichnung.
- Tragende Normen verifizieren: BRAO §§ 43a, 49b, DSGVO Art. 6, 28, 32, 35, BORA § 19a (technische Sorgfalt), beA-Bedingungen, ZPO § 130a (eVa), § 130d (aktive Nutzungspflicht), GwG § 8 Aufbewahrung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anwalt, Sekretariat, IT-Verantwortlicher, Datenschutzbeauftragter, KI-Anbieter (Auftragsverarbeiter), Kammer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Word-Dokumentvorlage, beA-Schriftsatz, AV-Vertrag mit KI-Anbieter, DSFA, Sicherheitskonzept, AGB-/Mandantenklauseln zu KI-Einsatz — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Klauselzweck (welcher Tatbestand, welche Rechtsfolge)
- Vertragstyp (Kaufvertrag, Werkvertrag, Dienstvertrag, gemischter Vertrag)
- Parteienstellung (Bestellerseite oder Lieferantenseite)
- Optional: Bestehender Klauselentwurf zur Restrukturierung

## Rechtlicher und methodischer Rahmen

- BGB-Anspruchsgrundlagenpruefung als Vorbild. Tatbestand und Rechtsfolge sind die zwei Saeulen jeder Norm.
- § 280 Abs. 1 BGB: "Verletzt der Schuldner eine Pflicht aus dem Schuldverhaeltnis, so kann der Gläubiger Ersatz des hierdurch entstehenden Schadens verlangen." Vorbild für Drafting.
- § 281 BGB, § 286 BGB: Verzug und Schadensersatz statt der Leistung.
- § 437 BGB, § 634 BGB: Rechte des Kaeufers und des Bestellers bei Mangel.
- AGB-Recht: Klauselverbote § 308, § 309 BGB. Bei B2B § 307 BGB.

## Ablauf / Checkliste

1. **Tatbestand zerlegen.** Welche Voraussetzungen müssen kumulativ vorliegen?
2. **Rechtsfolge formulieren.** Was ist die genaue Pflicht oder das Recht?
3. **Frist setzen.** Innerhalb welcher Frist gilt die Rechtsfolge?
4. **Beweislast bedenken.** Wer muss was darlegen?
5. **Konsistenz mit BGB-Defaults.** Weicht die Klausel ab? Wenn ja, AGB-tauglich?
6. **Tabelle erstellen.** Tatbestand, Rechtsfolge, Frist, Verweis.

### Wenn-Dann-Schema

```
WENN [Tatbestandsvoraussetzung 1]
UND [Tatbestandsvoraussetzung 2]
UND [Tatbestandsvoraussetzung 3]
DANN [Rechtsfolge]
INNERHALB [Frist]
ES SEI DENN [Ausnahme].
```

### Tabelle Tatbestand zu Rechtsfolge zu Frist

| Klausel | Tatbestand (Wenn) | Rechtsfolge (Dann) | Frist |
|---|---|---|---|
| Maengelruege | Lieferung mangelhaft | Anzeige durch Besteller | 7 Tage ab Erkennbarkeit |
| Nacherfuellung | Anzeige erfolgt, Mangel besteht | Nacherfuellung durch Lieferant | 14 Tage |
| Ruecktritt | Nacherfuellung erfolglos | Ruecktritt durch Besteller | nach erfolgloser Frist |
| Verzug | Faelligkeit, Mahnung | Verzugszinsen | ab Mahnung |
| Kuendigung wichtiger Grund | Pflichtverletzung, Abmahnung | Ausserordentliche Kuendigung | 14 Tage nach Kenntnis |
| Aufrechnung | unbestrittene oder rechtskraeftig festgestellte Forderung | Aufrechnung zulässig | jederzeit |

### Beispiel 1: Maengelhaftungsklausel (B2B-Lieferantenvertrag)

```
§ 6 Maengelhaftung

(1) Maengelruege
Lieferungen sind unverzueglich nach Erhalt zu untersuchen. Offene Maengel
sind binnen sieben Werktagen nach Lieferung, verdeckte Maengel binnen
sieben Werktagen nach Erkennbarkeit schriftlich anzuzeigen. § 377 HGB
bleibt unberuehrt.

(2) Nacherfuellung
Bei berechtigter Maengelruege hat der Lieferant nach Wahl des Bestellers
nachzuliefern oder nachzubessern. Die Nacherfuellung erfolgt innerhalb
von 14 Tagen nach Maengelruege.

(3) Ruecktritt und Minderung
Schlaegt die Nacherfuellung fehl oder ist sie dem Besteller unzumutbar,
kann der Besteller vom Vertrag zuruecktreten oder die Verguetung mindern.

(4) Schadensersatz
Schadensersatzanspruechee richten sich nach § 7 (Haftung).
```

### Beispiel 2: Verzugsklausel

```
§ 4 Verguetung und Zahlung

(3) Verzug
Bei Zahlungsverzug schuldet der Besteller Verzugszinsen in Hoehe von neun
Prozentpunkten ueber dem Basiszinssatz (§ 288 Abs. 2 BGB). Die Geltend-
machung weiteren Verzugsschadens bleibt vorbehalten.
```

### Beispiel 3: Kuendigungsfolgenklausel

```
§ 9 Laufzeit und Kuendigung

(3) Folgen der Kuendigung
Mit Wirksamwerden der Kuendigung sind bereits erbrachte Leistungen vom
Besteller anteilig zu verguten. Der Lieferant gibt saemtliche zur
Verfuegung gestellten Unterlagen, Daten und Geraete innerhalb von 14 Tagen
zurueck. Geheimhaltungspflichten gemaess § 8 bleiben für zwei Jahre nach
Beendigung des Vertrages bestehen.
```

### Mantelklausel-Anti-Pattern

**Schlecht (Mantelklausel):**

```
Sollte der Lieferant die Leistung nicht oder nicht rechtzeitig erbringen,
und sollte der Besteller dies dem Lieferanten unter Setzung einer
angemessenen Frist nicht zumindest mittelbar anzeigen, so soll, sofern
nicht ausnahmsweise andere Umstaende dem entgegenstehen, ein Schadensersatz
zu leisten sein, wobei die Hoehe sich nach billigem Ermessen richtet.
```

**Gut (zerlegt):**

```
(1) Liefert der Lieferant nicht oder nicht rechtzeitig, gilt § 5 (Verzug).
(2) Der Besteller setzt dem Lieferanten eine Nachfrist von 14 Tagen.
(3) Nach erfolglosem Fristablauf kann der Besteller Schadensersatz statt
 der Leistung verlangen (§ 281 BGB).
(4) Die Hoehe des Schadensersatzes richtet sich nach § 7 (Haftung).
```

## Typische Drafting-Fehler

- **Tatbestand und Rechtsfolge in einem Schachtelsatz.** Trennen.
- **Mehrere Rechtsfolgen ohne Reihenfolge.** Klar regeln, ob alternativ oder kumulativ.
- **Frist offen.** "Angemessene Frist" nur, wenn unausweichlich. Sonst konkret beziffern.
- **Ausnahmen ohne Tatbestand.** "Es sei denn, andere Umstaende stehen entgegen" ist keine Ausnahme.
- **Klauseln ohne Verweis auf BGB-Defaults.** Wer abweicht, soll wissen wovon.
- **AGB-Klauselverbote ignoriert.** § 308, § 309 BGB lesen.

## Beispiel

**Aufgabe:** Klausel für die ausserordentliche Kuendigung bei Pflichtverletzung des Lieferanten.

**Loesung:**

```
§ 9 Kuendigung aus wichtigem Grund

(1) Tatbestand
Eine Partei kann diesen Vertrag aus wichtigem Grund ohne Einhaltung einer
Kuendigungsfrist kuendigen, wenn:
 a) die andere Partei eine wesentliche Vertragspflicht trotz Abmahnung
 mit Fristsetzung von mindestens 14 Tagen wiederholt verletzt; oder
 b) ueber das Vermoegen der anderen Partei ein Insolvenzverfahren eroeffnet
 oder mangels Masse abgelehnt wird; oder
 c) die andere Partei ihre Zahlungen einstellt.

(2) Form
Die Kuendigung bedarf der Schriftform und ist innerhalb von 14 Tagen ab
Kenntnis des wichtigen Grundes auszusprechen.

(3) Rechtsfolge
Mit Zugang der Kuendigung endet der Vertrag. § 9 Abs. 3 (Folgen) gilt.
```

| Wenn | Dann | Frist |
|---|---|---|
| wesentliche Pflichtverletzung trotz Abmahnung | Ausserordentliche Kuendigung | 14 Tage ab Kenntnis |
| Insolvenz | Ausserordentliche Kuendigung | 14 Tage ab Kenntnis |
| Zahlungseinstellung | Ausserordentliche Kuendigung | 14 Tage ab Kenntnis |

## Quellen (Stand 05/2026)

- § 280 BGB, § 281 BGB, § 286 BGB, § 288 BGB, § 308 BGB, § 309 BGB, § 437 BGB, § 634 BGB; § 377 HGB. gesetze-im-internet.de.
- AGB-Rechtsprechung des BGH zu Mantelklauseln: vom Nutzer mit konkretem Aktenzeichen über bundesgerichtshof.de zu verifizieren.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 203 StGB
- Art. 28 DSGVO
- § 11 ProdHaftG
- § 41 UrhG
- § 31a UrhG
- § 32 UrhG
- § 35 UrhG
- Art. 32 DSGVO
- § 2 GeschGehG
- § 29 UrhG
- § 31 UrhG
- § 34 UrhG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
