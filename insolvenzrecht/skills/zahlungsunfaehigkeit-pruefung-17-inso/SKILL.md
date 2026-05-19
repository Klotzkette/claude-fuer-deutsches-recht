---
name: zahlungsunfaehigkeit-pruefung-17-inso
description: >
  Erstellt ein strukturiertes Prüfgutachten zum Eröffnungsgrund der Zahlungsunfähigkeit
  nach § 17 InsO. Berechnet den Liquiditätsstatus zum Stichtag, wendet das
  10-%-/3-Wochen-Schema des BGH an und würdigt Indizien der Zahlungseinstellung.
  Lädt, wenn der Nutzer Zahlungsunfähigkeit, Liquiditätsstatus, Insolvenzeröffnungsgrund
  oder § 17 InsO prüfen möchte.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Zahlungsunfähigkeit
  - § 17 InsO
  - Liquiditätsstatus
  - Liquiditätsbilanz
  - 10-Prozent-Schwelle
  - Zahlungseinstellung
  - Zahlungsstockung
  - Insolvenzeröffnungsgrund
  - fällige Verbindlichkeiten
  - Eröffnungsgrund prüfen
---

# Gerichtsfeste Prüfung des Eröffnungsgrundes § 17 InsO (Zahlungsunfähigkeit)

## Zweck

Dieser Skill führt eine strukturierte, an der BGH-Rechtsprechung und IDW S 11 ausgerichtete
Prüfung durch, ob zum maßgeblichen Stichtag Zahlungsunfähigkeit i.S.d. § 17 InsO vorliegt.
Das Ergebnis ist ein dokumentierbares Gutachten, das vor Insolvenzgerichten, im Anfechtungs-
und Haftungsprozess sowie gegenüber dem vorläufigen Insolvenzverwalter Stand hält.

## Eingaben

Der Nutzer stellt folgende Informationen bereit (fehlende Angaben werden abgefragt):

- **Stichtag**: konkretes Datum der Prüfung (i.d.R. Tag der Antragstellung oder ein früherer
  Zeitpunkt für Haftungszwecke)
- **Fällige Verbindlichkeiten (Passiva I)**: Betrag und Gläubiger aller zum Stichtag fälligen,
  nicht gestundeten Verbindlichkeiten
- **Liquide Mittel (Aktiva I)**: Kassenbestand, Bankguthaben, sofort verwertbare Aktiva
- **Zuflüsse innerhalb von 3 Wochen (Aktiva II. Stufe)**: konkret zu erwartende Zahlungseingänge
  aus bestehenden Forderungen, zugesagten Kreditlinien u.Ä.
- **Stundungsvereinbarungen**: ob schriftlich dokumentiert, glaubhaft und ernstlich gewollt
- **Indizien** (soweit vorhanden): Lohnrückstände, SV-Beitragsrückstände, Stundungsbitten,
  Wechselproteste, Pfändungsmaßnahmen, Insolvenzanträge anderer Gläubiger

## Rechtlicher Rahmen

### Gesetzliche Grundlagen

**§ 17 Abs. 1 InsO** bestimmt Zahlungsunfähigkeit als allgemeinen Eröffnungsgrund.

**§ 17 Abs. 2 S. 1 InsO** definiert: Der Schuldner ist zahlungsunfähig, wenn er nicht in der
Lage ist, die fälligen Zahlungspflichten zu erfüllen.

**§ 17 Abs. 2 S. 2 InsO** normiert die gesetzliche Vermutung: Zahlungsunfähigkeit ist in der
Regel anzunehmen, wenn der Schuldner seine Zahlungen eingestellt hat.

### Rechtsprechung

**BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 19 ff.**
Grundlegendes Urteil zum 10-%-/3-Wochen-Schema: Zahlungsunfähigkeit liegt vor, wenn der
Schuldner zum Stichtag seine fälligen Verbindlichkeiten nicht zu mindestens 90 % erfüllen kann
und die Lücke nicht innerhalb von 3 Wochen zu schließen ist. Eine Unterdeckung von weniger als
10 % begründet lediglich eine Zahlungsstockung, wenn die Lücke in absehbarer Zeit beseitigt
werden kann. Ab 10 % ist auch bei kurzfristiger Behebbarkeit Zahlungsunfähigkeit anzunehmen,
sofern die Unterdeckung mehr als 3 Wochen andauert (Rn. 19–27).

**BGH, Urt. v. 19.07.2007 – IX ZR 81/06, NJW 2007, 78 Rn. 36 ff.**
Indizienkatalog für die Zahlungseinstellung i.S.d. § 17 Abs. 2 S. 2 InsO: Als Indizien gelten
insbesondere verspätete Lohnzahlungen, offene Sozialversicherungsbeiträge, erfolglose
Stundungsbitten gegenüber Gläubigern, Wechselproteste, Pfändungsmaßnahmen von Gläubigern,
Insolvenzanträge anderer Gläubiger sowie der eigene Insolvenzantrag des Schuldners (Rn. 36–41).
Die Zahlungseinstellung setzt kein allgemeines Unvermögen voraus; es genügt, dass der Schuldner
den wesentlichen Teil seiner Verbindlichkeiten nicht mehr zahlt.

**BGH, Urt. v. 14.07.2006 – IX ZR 92/04, BGHZ 168, 158 Rn. 21 ff.**
Zur Behandlung von Stundungen in der Liquiditätsbilanz: In die Passiva I (fällige Verbindlichkeiten)
sind nur Verbindlichkeiten aufzunehmen, die tatsächlich fällig und nicht wirksam gestundet sind.
Echter Stundung (beiderseitig gewollt, glaubhaft dokumentiert) ist Folge zu geben; sie beseitigt
die Fälligkeit. Erzwungene oder faktische Stundungen — d.h. bloßes Dulden des Zahlungsverzugs
durch den Gläubiger ohne Einigung — beseitigen die Fälligkeit nicht und sind weiterhin Passiva I
(Rn. 21–29). Im Anfechtungsprozess trifft den Schuldner die Darlegungs- und Beweislast für das
Vorliegen einer echten Stundungsvereinbarung.

**BGH, Urt. v. 05.12.2013 – IX ZR 88/11, NJW 2013, 940 Rn. 23 ff.**
Zur Verschuldensfrage bei Antragspflichtverletzung: Kenntnis der Zahlungsunfähigkeit ist dann zu
bejahen, wenn dem Schuldner die die Zahlungsunfähigkeit begründenden Tatsachen bekannt waren
oder bekannt sein mussten. Dieses Urteil unterstreicht, dass eine Berufung auf Unkenntnis dann
ausscheidet, wenn die Indizien nach dem Katalog des BGH IX ZR 81/06 objektiv vorlagen (Rn. 23 f.).

### Kommentarliteratur

- Mock, in: Uhlenbruck, InsO, 16. Aufl. 2024, § 17 Rn. 10 ff., 30 ff. (Liquiditätsbilanz,
  Stichtagsprinzip, Abgrenzung Stockung/Unfähigkeit)
- Schmerbach, in: K. Schmidt, InsO, 20. Aufl. 2023, § 17 Rn. 5 ff., 22 ff. (Indizienwürdigung,
  erzwungene Stundung, Beweislast)

### IDW-Standard

**IDW S 11 (Stand 12.08.2021), Tz. 31 ff.** regelt die Beurteilung des Eröffnungsgrundes der
Zahlungsunfähigkeit durch den Sachverständigen oder Wirtschaftsprüfer: Aufzustellen ist ein
Liquiditätsstatus auf den Prüfungsstichtag, der liquide Mittel (Aktiva I, ggf. ergänzt um Aktiva II)
den fälligen Verbindlichkeiten (Passiva I) gegenüberstellt. Übersteigen Passiva I die Aktiva I und II
um mehr als 10 %, ist bei fehlender kurzfristiger Beseitigungsperspektive Zahlungsunfähigkeit
festzustellen (Tz. 31–37). IDW S 11 Tz. 16 f. zur Abgrenzung gegenüber Zahlungsstockung und
Überschuldung.

## Ablauf

Das Prüfgutachten folgt diesen sieben Schritten:

**Schritt 1 – Stichtagsbestimmung**
Festlegung des maßgeblichen Prüfungsstichtags. Bei Antragspflicht (§ 15a InsO) ist dies der Eintritt
der Zahlungsunfähigkeit; im Anfechtungsrecht (§§ 129 ff. InsO) kann ein früherer Zeitpunkt relevant
sein. Alle weiteren Prüfungsschritte erfolgen stichtagsbezogen.

**Schritt 2 – Erfassung fälliger Verbindlichkeiten (Passiva I)**
Vollständige Erfassung aller am Stichtag fälligen, nicht wirksam gestundeten Verbindlichkeiten.
Einzubeziehen sind: Lieferantenverbindlichkeiten, Darlehensverbindlichkeiten (inkl. gekündigter
oder fälliger Teile), Lohn- und Gehaltsrückstände, Sozialversicherungsbeiträge (SV-Beiträge),
Steuerschulden mit abgelaufener Zahlungsfrist, sonstige fällige Forderungen. Stundungen sind auf
ihre rechtliche Wirksamkeit hin zu überprüfen (s. BGH IX ZR 92/04).

**Schritt 3 – Aktiva-Erfassung**
- *Aktiva I*: sofort verfügbare liquide Mittel zum Stichtag (Kassenbestand, Bankguthaben,
  debitorische Konten ohne Ausschöpfung des Rahmens)
- *Aktiva II. Stufe* (innerhalb 3 Wochen zugehend): konkret erwartete Zahlungseingänge aus
  bestehenden Forderungen (nach vorsichtiger Einschätzung der Ausfallwahrscheinlichkeit),
  freie Kreditlinien, erwartete Darlehensauszahlungen mit schriftlicher Zusage

**Schritt 4 – Aufstellung des Liquiditätsstatus**
Gegenüberstellung in tabellarischer Form:

```
Aktiva I (sofort verfügbar)          EUR ______
+ Aktiva II (innerhalb 3 Wochen)     EUR ______
= Summe liquide Mittel               EUR ______

./. Passiva I (fällige Verbindlichkeiten)  EUR ______

= Unterdeckung / Überdeckung         EUR ______
```

**Schritt 5 – Quotenberechnung**
Berechnung der Liquiditätsquote:

  Quote = (Summe liquide Mittel / Passiva I) × 100

Eine Quote ≥ 100 % schließt Zahlungsunfähigkeit aus. Eine Quote zwischen 90 % und 99 %
(Unterdeckung < 10 %) begründet bei kurzfristiger Behebbarkeit nur Zahlungsstockung.

**Schritt 6 – Subsumtion nach dem 10-%-/3-Wochen-Schema (BGH IX ZR 123/04)**
- Unterdeckung < 10 % und Beseitigung innerhalb 3 Wochen absehbar → Zahlungsstockung,
  keine Zahlungsunfähigkeit
- Unterdeckung < 10 %, aber Beseitigung nicht innerhalb 3 Wochen → Zahlungsunfähigkeit
- Unterdeckung ≥ 10 % → Zahlungsunfähigkeit unabhängig von der Perspektive der Beseitigung

**Schritt 7 – Würdigung der Indizien für Zahlungseinstellung (§ 17 Abs. 2 S. 2 InsO)**
Liegen rechnerisch Zweifelsfälle vor oder fehlen vollständige Daten, sind die Indizien nach
BGH IX ZR 81/06 Rn. 36 ff. zu würdigen: verspätete Lohnzahlungen, offene SV-Beiträge,
Stundungsbitten, Wechselproteste, Pfändungen, Insolvenzanträge anderer Gläubiger, eigener
Antrag. Häufen sich mehrere Indizien, ist Zahlungseinstellung und damit Zahlungsunfähigkeit
zu bejahen. Die Vermutung des § 17 Abs. 2 S. 2 InsO ist widerlegbar; die Beweislast liegt beim
Schuldner (Mock, in: Uhlenbruck, InsO, 16. Aufl. 2024, § 17 Rn. 72).

## Ausgabeformat

Das Gutachten wird im Gutachtenstil formuliert:

1. **Sachverhalt** (kurze Sachverhaltsdarstellung)
2. **Rechtliche Grundlagen** (§ 17 Abs. 2 S. 1 und S. 2 InsO, BGH-Schema)
3. **Liquiditätsstatus** (Tabelle nach Schritt 4)
4. **Quotenberechnung** (Schritt 5)
5. **Subsumtion** (Schritt 6 mit Zwischenergebnis)
6. **Indizienanalyse** (Schritt 7, wenn relevant)
7. **Ergebnis** (Feststellung: Zahlungsunfähigkeit liegt vor / liegt nicht vor / Zahlungsstockung)
8. **Quellennachweis** (BGH-Entscheidungen, IDW S 11, Kommentare mit Randnummern)

## Beispiel

### Sachverhalt

Die Muster GmbH (Schuldnerin) weist zum Stichtag 31.03.2025 folgende Situation auf:

**Variante A** (Zahlungsstockung):
- Liquide Mittel (Aktiva I): 25.000 EUR (Bankguthaben)
- Zuflüsse innerhalb 3 Wochen (Aktiva II): 0 EUR (keine gesicherten Eingänge)
- Fällige Verbindlichkeiten (Passiva I): 320.000 EUR

**Variante B** (Zahlungsunfähigkeit):
- Liquide Mittel (Aktiva I): 40.000 EUR
- Zuflüsse innerhalb 3 Wochen (Aktiva II): 0 EUR
- Fällige Verbindlichkeiten (Passiva I): 320.000 EUR
- Keine Aussicht auf Schließung der Lücke innerhalb von 3 Wochen

---

### Subsumtion Variante A

**Liquiditätsstatus:**

```
Aktiva I                    25.000 EUR
+ Aktiva II                      0 EUR
= Summe liquide Mittel      25.000 EUR
./. Passiva I              320.000 EUR
= Unterdeckung             295.000 EUR
```

**Quote:** 25.000 / 320.000 × 100 = **7,8 %**

Die Unterdeckung beträgt 92,2 % und übersteigt damit nicht die 10-%-Schwelle im Sinne von BGH,
Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 19.

**Zwischenergebnis:** Die Unterdeckung liegt unter 10 %. Es ist zu prüfen, ob die Lücke von
295.000 EUR innerhalb von 3 Wochen zu schließen ist. Fehlen konkrete Zuflüsse, liegt nach Ablauf
der 3-Wochen-Frist Zahlungsunfähigkeit vor. Bestehen hinreichend konkrete Zuflusserwartungen
(Aktiva II), ist lediglich Zahlungsstockung anzunehmen; die Prüfung ist in 3 Wochen zu wiederholen.

---

### Subsumtion Variante B

**Liquiditätsstatus:**

```
Aktiva I                    40.000 EUR
+ Aktiva II                      0 EUR
= Summe liquide Mittel      40.000 EUR
./. Passiva I              320.000 EUR
= Unterdeckung             280.000 EUR
```

**Quote:** 40.000 / 320.000 × 100 = **12,5 %**

Die Unterdeckung beläuft sich auf 87,5 % und übersteigt die 10-%-Schwelle.

**Subsumtion:** Nach BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 19 ff. ist bei
einer Unterdeckung von ≥ 10 % Zahlungsunfähigkeit anzunehmen, sobald keine kurzfristige
Beseitigung in Sicht ist. Die Schuldnerin kann keine Zuflüsse innerhalb von 3 Wochen nachweisen.
Die Unterdeckung wird nicht innerhalb von 3 Wochen beseitigt.

**Ergebnis:** Die Muster GmbH ist zum Stichtag 31.03.2025 zahlungsunfähig i.S.d. § 17 Abs. 2
S. 1 InsO. Die Pflicht zur Stellung eines Insolvenzantrags nach § 15a InsO ist ausgelöst.

## Risiken und typische Fehler

**1. Stille Stundungen und erzwungene Duldung (BGH IX ZR 92/04)**
Häufig wird ein bloßes Nichtklagen des Gläubigers als Stundung gewertet. Nach BGH,
Urt. v. 14.07.2006 – IX ZR 92/04, BGHZ 168, 158 Rn. 21 ff. beseitigt eine erzwungene
oder faktische Duldung des Zahlungsverzuges die Fälligkeit nicht. Nur beiderseitig vereinbarte,
schriftlich belegbare echte Stundungen dürfen aus den Passiva I herausgenommen werden. Ohne
Dokumentation besteht das Risiko, dass das Insolvenzgericht oder ein Sachverständiger die
Fälligkeit gleichwohl bejaht und eine frühere Zahlungsunfähigkeit feststellt.

**2. Vergessene Sozialversicherungsbeiträge**
SV-Beiträge werden in der Praxis häufig nicht in die Passiva I aufgenommen, obwohl sie
gesetzlich sofort fällig sind (§ 23 SGB IV). Rückständige SV-Beiträge sind zugleich ein gewichtiges
Indiz für Zahlungseinstellung nach BGH, Urt. v. 19.07.2007 – IX ZR 81/06, NJW 2007, 78 Rn. 37.
Fehler hier führen sowohl zur Unterschätzung der Passiva I als auch zur Übersehung eines
Zahlungseinstellungsindizes.

**3. Unzulässige Berücksichtigung künftiger Forderungen (Aktiva III. Stufe)**
Erlöse aus erst künftig abzuschließenden Verträgen, erhoffte Investorengelder ohne verbindliche
Zusage oder hypothetische Verwertungserlöse gehören nicht in die Liquiditätsbilanz (Aktiva I oder II),
sondern allenfalls in eine Liquiditätsplanung (Aktiva III. Stufe). Ihre Einbeziehung in die
Liquiditätsbilanz ist methodisch unzulässig und führt zu einer unzutreffend negativen Feststellung
der Zahlungsunfähigkeit (Mock, in: Uhlenbruck, InsO, 16. Aufl. 2024, § 17 Rn. 38 f.).

**4. Stichtagsverschiebung im Haftungskontext**
Im Anfechtungs- und Haftungsprozess ist nicht der Antragstag, sondern der tatsächliche Eintritt
der Zahlungsunfähigkeit maßgeblich. Wird der Stichtag zu spät angesetzt, werden Haftungs-
oder Anfechtungszeiträume unzutreffend verkürzt (Schmerbach, in: K. Schmidt, InsO, 20. Aufl.
2023, § 17 Rn. 32).

**5. Fehlende Indiziengesamtwürdigung**
Einzelne Indizien (z.B. nur eine verspätete Lohnzahlung) begründen für sich allein noch keine
Zahlungseinstellung. Erst das Zusammentreffen mehrerer Indizien aus dem Katalog des BGH
IX ZR 81/06 Rn. 36 ff. rechtfertigt die Vermutung des § 17 Abs. 2 S. 2 InsO. Eine isolierte
Betrachtung führt zu Fehlsubsumtionen.

## Quellenpflicht

Jedes auf diesem Skill basierende Gutachten muss mindestens folgende Quellen ausweisen:

- BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 19 ff. (10-%-/3-Wochen-Schema)
- BGH, Urt. v. 19.07.2007 – IX ZR 81/06, NJW 2007, 78 Rn. 36 ff. (Indizienkatalog)
- BGH, Urt. v. 14.07.2006 – IX ZR 92/04, BGHZ 168, 158 Rn. 21 ff. (echte vs. erzwungene Stundung)
- BGH, Urt. v. 05.12.2013 – IX ZR 88/11, NJW 2013, 940 Rn. 23 ff. (Verschulden Antragspflicht)
- Mock, in: Uhlenbruck, InsO, 16. Aufl. 2024, § 17 Rn. 10 ff., 30 ff., 38 f., 72
- Schmerbach, in: K. Schmidt, InsO, 20. Aufl. 2023, § 17 Rn. 5 ff., 22 ff., 32
- IDW S 11 (Stand 12.08.2021), Tz. 16 f., 31–37

---

*Dieser Skill ersetzt keine konkrete anwaltliche Beratung im Einzelfall.*
