---
name: anspruchsgrundlage-rechtsfolgen-b2b-vs
description: "Anspruchsgrundlage Rechtsfolgen B2B VS: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anspruchsgrundlage Rechtsfolgen B2B VS

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Anspruchsgrundlage Rechtsfolgen B2B VS** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anspruchsgrundlage-und-rechtsfolgen-klauseln` | Vertragliche Klauseln nach der Wenn-Dann-Architektur bauen. Klare Trennung von Tatbestand (Wenn-Teil mit Voraussetzungen) und Rechtsfolge (Dann-Teil mit Pflichten und Fristen). Anwendungsbeispiele: Maengelhaftung Verzugsklausel Kuendigungsfolgenklausel. Anti-Pattern Mantelklausel mit verschachtelten Wenn-Tatbestaenden vermeiden. Mit Tabelle Tatbestand zu Rechtsfolge zu Frist. |
| `b2b-vs-b2c-klausel-strategie` | Strategisches Drafting in zwei Vertragswelten. B2C unter strengem Verbraucherschutz (§§ 13 und 14 BGB sowie § 305 II BGB und §§ 308 und 309 BGB direkt anwendbar). B2B im Geschäftsverkehr nach § 310 I BGB erleichtert, aber mit Ausstrahlungswirkung der Klauselverbote über § 307 BGB. Ein einziges Klauselwerk für beide Welten ist effizient, aber risikobehaftet; Alternative sind getrennte AGB-Sätze. Liefert Tabelle Klauseltyp/B2C-Risiko/B2B-Risiko/Empfehlung und Mustertexte für haftungsbegrenzte Klauseln im Vergleich beider Welten. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Anspruchsgrundlage Rechtsfolgen B2B VS**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anspruchsgrundlage-und-rechtsfolgen-klauseln`

**Fokus:** Vertragliche Klauseln nach der Wenn-Dann-Architektur bauen. Klare Trennung von Tatbestand (Wenn-Teil mit Voraussetzungen) und Rechtsfolge (Dann-Teil mit Pflichten und Fristen). Anwendungsbeispiele: Maengelhaftung Verzugsklausel Kuendigungsfolgenklausel. Anti-Pattern Mantelklausel mit verschachtelten Wenn-Tatbestaenden vermeiden. Mit Tabelle Tatbestand zu Rechtsfolge zu Frist.

# Anspruchsgrundlage und Rechtsfolgen-Klauseln

## Zweck

Vertragliche Klauseln sind kleine Anspruchsgrundlagen. Sie folgen derselben Architektur wie das Gesetz: Wenn die Voraussetzungen vorliegen (Tatbestand), dann tritt die Rechtsfolge ein. Die saubere Trennung beider Teile ist Drafting-Grundpflicht.

Dieser Skill operationalisiert die Wenn-Dann-Architektur fuer typische Vertragsklauseln: Maengelhaftung, Verzug, Kuendigungsfolgen, Schadensersatz, Aufrechnung. Er liefert das Schema und zeigt, wie Sie Mantelklauseln mit verschachtelten Bedingungen aufloesen.

## Eingaben

- Klauselzweck (welcher Tatbestand, welche Rechtsfolge)
- Vertragstyp (Kaufvertrag, Werkvertrag, Dienstvertrag, gemischter Vertrag)
- Parteienstellung (Bestellerseite oder Lieferantenseite)
- Optional: Bestehender Klauselentwurf zur Restrukturierung

## Rechtlicher und methodischer Rahmen

- BGB-Anspruchsgrundlagenpruefung als Vorbild. Tatbestand und Rechtsfolge sind die zwei Saeulen jeder Norm.
- § 280 Abs. 1 BGB: "Verletzt der Schuldner eine Pflicht aus dem Schuldverhaeltnis, so kann der Glaeubiger Ersatz des hierdurch entstehenden Schadens verlangen." Vorbild fuer Drafting.
- § 281 BGB, § 286 BGB: Verzug und Schadensersatz statt der Leistung.
- § 437 BGB, § 634 BGB: Rechte des Kaeufers und des Bestellers bei Mangel.
- AGB-Recht: Klauselverbote § 308, § 309 BGB. Bei B2B § 307 BGB.

## Ablauf / Checkliste

1. **Tatbestand zerlegen.** Welche Voraussetzungen muessen kumulativ vorliegen?
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
| Aufrechnung | unbestrittene oder rechtskraeftig festgestellte Forderung | Aufrechnung zulaessig | jederzeit |

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
zurueck. Geheimhaltungspflichten gemaess § 8 bleiben fuer zwei Jahre nach
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

## Ausgabeformat

- Klauselentwurf mit klarer Wenn-Dann-Struktur.
- Tabelle Tatbestand zu Rechtsfolge zu Frist.
- Hinweis auf BGB-Vergleichsnorm.

## Beispiel

**Aufgabe:** Klausel fuer die ausserordentliche Kuendigung bei Pflichtverletzung des Lieferanten.

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

## Querverweise

- `drafting-prinzipien-klarheit-bestimmtheit-praezision`
- `haftungsausschluss-und-haftungsbegrenzung`
- `bedingungen-aufschiebend-aufloesend-fristen`
- `kuendigungsklauseln-und-vertragsbeendigung`

## Quellen (Stand 05/2026)

- § 280 BGB, § 281 BGB, § 286 BGB, § 288 BGB, § 308 BGB, § 309 BGB, § 437 BGB, § 634 BGB; § 377 HGB. gesetze-im-internet.de.
- AGB-Rechtsprechung des BGH zu Mantelklauseln: vom Nutzer mit konkretem Aktenzeichen ueber bundesgerichtshof.de zu verifizieren.

## 2. `b2b-vs-b2c-klausel-strategie`

**Fokus:** Strategisches Drafting in zwei Vertragswelten. B2C unter strengem Verbraucherschutz (§§ 13 und 14 BGB sowie § 305 II BGB und §§ 308 und 309 BGB direkt anwendbar). B2B im Geschäftsverkehr nach § 310 I BGB erleichtert, aber mit Ausstrahlungswirkung der Klauselverbote über § 307 BGB. Ein einziges Klauselwerk für beide Welten ist effizient, aber risikobehaftet; Alternative sind getrennte AGB-Sätze. Liefert Tabelle Klauseltyp/B2C-Risiko/B2B-Risiko/Empfehlung und Mustertexte für haftungsbegrenzte Klauseln im Vergleich beider Welten.

# B2B vs. B2C Klauselstrategie

## Zweck

Dieser Skill unterstützt Sie bei der Entscheidung, ob Sie ein einheitliches Klauselwerk für Verbraucher- und Unternehmergeschäfte führen oder getrennte AGB-Sätze pflegen. Die Trennung folgt aus der unterschiedlichen Anwendung der §§ 305 ff. BGB.

## Eingaben

- Kundenstruktur (rein B2B, rein B2C, gemischt).
- Vertriebskanal (Onlineshop, Außendienst, Plattform).
- Bisheriges Klauselwerk.
- Branche und Regulierung (Telekommunikation, Banking, Energie, Bau).
- Konfliktthemen (Haftungsbegrenzung, Mängelrechte, Vertragslaufzeiten, Vertragsstrafe, Aufrechnung).

## Rechtlicher und methodischer Rahmen

- **Verbraucher (§ 13 BGB):** Natürliche Person, die ein Rechtsgeschäft zu Zwecken außerhalb ihrer gewerblichen oder selbständigen beruflichen Tätigkeit abschließt.
- **Unternehmer (§ 14 BGB):** Natürliche oder juristische Person oder rechtsfähige Personengesellschaft, die in Ausübung ihrer gewerblichen oder selbständigen beruflichen Tätigkeit handelt.
- **B2C-Welt:** § 305 II BGB Einbeziehung, §§ 308 und 309 BGB direkt anwendbar, § 307 BGB inkl. Transparenzgebot.
- **B2B-Welt:** § 310 I BGB. §§ 308 und 309 BGB direkt nicht anwendbar; jedoch §§ 305c, 307 BGB direkt anwendbar. BGH wertet die §§ 308 und 309 BGB als Indizien für die Unangemessenheit nach § 307 BGB; konkrete Fundstelle vom Nutzer zu verifizieren.
- **Handelsbräuche:** § 310 I 2 BGB verlangt Berücksichtigung der im Handelsverkehr geltenden Gewohnheiten und Gebräuche.
- **Praxisfolge:** Klauseln, die in B2C eindeutig verboten sind, sind in B2B oft ebenfalls unwirksam, jedoch nicht reflexartig. Eine inhaltliche Begründung bleibt notwendig.
- **Strategieentscheidung:** Ein gemeinsames Klauselwerk vereinfacht die Pflege, birgt aber das Risiko, dass die strengere Verbraucherwertung das Geschäftskundenwerk durchschlägt (Worst-Case-Übernahme). Getrennte AGB-Sätze sind aufwendiger, aber sauberer.

## Ablauf / Checkliste

1. Kundenstruktur und Kanäle ermitteln. Wer wird tatsächlich Vertragspartner?
2. Konfliktklauseln identifizieren: Haftung, Mängelrechte (insbesondere Verjährung, Rüge), Vertragsdauer und Verlängerung, Preisanpassung, Vertragsstrafe, Aufrechnung, Zurückbehaltung, Gerichtsstand.
3. Pro Klausel B2C-Bewertung: § 308 / § 309 BGB direkt prüfen.
4. Pro Klausel B2B-Bewertung: § 307 BGB unter Berücksichtigung der Ausstrahlung der § 308 / § 309 BGB-Wertung und der Handelsbräuche.
5. Entscheidung: einheitliche Klausel, mit B2B-Variante (Switch) oder vollständige Trennung.
6. Bei Switch-Logik: technisch zuverlässig prüfen (Vertragstyp-Erkennung im Checkout) und transparent dokumentieren.
7. Bei getrennten AGB: Versionen mit klarer Bezeichnung (B2C-AGB, B2B-AGB), keine Vermischung im Vertragsschluss.
8. Bei gemischter Kundschaft (KMU als faktische Verbraucher): erhöhte Sorgfalt; viele Schutzregeln gelten ungeachtet der formalen Unternehmereigenschaft als Wertungsgrundlage.
9. Sicherstellen, dass der Geltungsumfang (§§ 13, 14 BGB) im Vertrag klar ist.
10. Schulung der Vertriebs- und Servicemitarbeitenden für die richtige AGB-Verwendung.

## Typische Drafting-Fehler

- "Gegenüber Unternehmern gilt §§ 308 / 309 BGB nicht": missverstandene Pauschalformel. Die Ausstrahlungswirkung wird ignoriert.
- Haftungsklausel aus B2C-AGB unverändert in B2B übernommen: doppelte Schutzwertung, mögliche Unwirksamkeit.
- Trennung nur formal: Verbraucher wird in B2B-Strecke gedrängt, indem ihm eine "Unternehmereigenschaft" abverlangt wird; die tatsächliche Eigenschaft entscheidet.
- Verlängerungsklausel mit zwölf Monaten Laufzeit in B2C: § 309 Nr. 9 BGB.
- Mängelfrist sechs Monate in B2C: § 309 Nr. 8 b ff BGB.
- Rügepflicht nach § 377 HGB in Verbraucher-AGB übernommen: unwirksam.
- Vertragsstrafe in B2C-AGB: § 309 Nr. 6 BGB.

## Ausgabeformat

- Strategie-Memo: B2C-only, B2B-only, gemeinsamer Korpus mit Schaltern oder getrennte AGB-Sätze.
- Tabelle Klauseltyp / B2C-Risiko / B2B-Risiko / Empfehlung.
- Mustertexte für die wichtigsten Konfliktklauseln in beiden Varianten.
- Hinweise zum operativen Einsatz (Checkout-Logik, Versionierung, Vertrieb).

## Beispiele

Tabelle (Auszug):

| Klauseltyp | B2C-Risiko | B2B-Risiko | Empfehlung |
|---|---|---|---|
| Haftungsbegrenzung auf Vorsatz | unwirksam: § 309 Nr. 7 a/b BGB | unwirksam nach § 307 BGB (Ausstrahlung) | Vorsatz, grobe Fahrlässigkeit, Verletzung Leben Körper Gesundheit ausnehmen; einfache Fahrlässigkeit nur bei wesentlichen Vertragspflichten, Höhe auf vertragstypischen Schaden begrenzt |
| Verkürzung Verjährungsfrist Mängel auf sechs Monate | unwirksam: § 309 Nr. 8 b ff BGB | bei B2B-Kaufverträgen Verkürzung auf zwölf Monate üblich, aber im Einzelfall Ausstrahlung; je nach Branche differenziert | im B2B zwölf Monate, in B2C keine Verkürzung |
| Aufrechnungsverbot | unwirksam: § 309 Nr. 3 BGB | grundsätzlich unwirksam, Ausstrahlung | Aufrechnung nur ausschließen für streitige, nicht rechtskräftig festgestellte Forderungen |
| Vertragsverlängerung um zwölf Monate ohne Kündigung | unwirksam: § 309 Nr. 9 BGB | im B2B häufig zulässig, aber transparent | in B2C maximal stillschweigende Verlängerung um drei Monate mit einmonatiger Kündigungsfrist |
| Vertragsstrafe | unwirksam: § 309 Nr. 6 BGB | im B2B individuell, AGB-tauglich nur eng | vgl. `vertragsstrafe-339-bgb` |

Mustertext (Haftungsbegrenzung, gegenübergestellt):

B2C-Variante:

> § X Haftung
> (1) Der Anbieter haftet unbeschränkt für Schäden aus der Verletzung des Lebens, des Körpers oder der Gesundheit, soweit er die Pflichtverletzung zu vertreten hat.
> (2) Im Übrigen haftet der Anbieter für Vorsatz und grobe Fahrlässigkeit unbeschränkt. Bei einfacher Fahrlässigkeit haftet der Anbieter nur für die Verletzung einer wesentlichen Vertragspflicht (Kardinalpflicht), deren Erfüllung die ordnungsgemäße Durchführung des Vertrages überhaupt erst ermöglicht und auf deren Einhaltung der Kunde regelmäßig vertrauen darf, und der Höhe nach begrenzt auf den vertragstypischen, vorhersehbaren Schaden.

B2B-Variante:

> § X Haftung
> (1) Der Anbieter haftet unbeschränkt für Vorsatz, grobe Fahrlässigkeit, für die Verletzung des Lebens, des Körpers und der Gesundheit, für Ansprüche nach dem Produkthaftungsgesetz und im Umfang einer übernommenen Garantie.
> (2) Bei leicht fahrlässiger Verletzung wesentlicher Vertragspflichten haftet der Anbieter der Höhe nach begrenzt auf den vertragstypischen, vorhersehbaren Schaden. Eine weitergehende Haftung für leichte Fahrlässigkeit ist ausgeschlossen.
> (3) Die Verjährung der Ansprüche des Kunden wegen Mängeln beträgt zwölf Monate ab Gefahrübergang, soweit nicht zwingende gesetzliche Vorschriften entgegenstehen.

## Querverweise

- `agb-konforme-klauseln-305-310-bgb` – Grundprüfung.
- `transparenzgebot-307-bgb` – Verständlichkeit.
- `haftungsausschluss-und-haftungsbegrenzung` – Tiefe der Haftungs-Drafting.
- `vertragsstrafe-339-bgb` – § 309 Nr. 6 BGB im Vergleich.
- `kuendigungsklauseln-und-vertragsbeendigung` – § 309 Nr. 9 BGB.

## Quellen (Stand 05/2026)

- §§ 13, 14, 305, 305c, 306, 307, 308, 309, 310 BGB.
- § 377 HGB (Rügepflicht im Handelskauf).
- BGH-Linie zur Ausstrahlung des § 309 BGB auf § 307 BGB im B2B ist vom Nutzer fundstellengenau zu verifizieren.
- Zitierweise: `references/zitierweise.md`.
