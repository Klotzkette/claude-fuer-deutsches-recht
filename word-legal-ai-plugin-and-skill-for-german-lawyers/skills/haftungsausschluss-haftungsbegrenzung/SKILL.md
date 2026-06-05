---
name: haftungsausschluss-haftungsbegrenzung
description: "Haftungsausschluss Haftungsbegrenzung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Haftungsausschluss Haftungsbegrenzung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Haftungsausschluss Haftungsbegrenzung** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `haftungsausschluss-und-haftungsbegrenzung` | Haftungsklauseln im deutschen Recht sauber bauen. Pflichtgrenzen § 276 Abs. 3 BGB (Vorsatz nie ausschliessbar), § 309 Nr. 7 BGB (AGB-Klauselverbote fuer Vorsatz grobe Fahrlaessigkeit Kardinalpflichten Koerperschaden), § 444 BGB (arglistig verschwiegener Mangel), § 11 ProdHaftG (zwingend bei Personenschaden). Drafting-Strategien Summenbegrenzung Zeitbegrenzung Ausschluss mittelbarer Schaeden. Mit Tabelle B2B vs B2C und Mustertexten. |
| `klageerwiderung-substantiiertes-bestreiten` | Drafting einer Klageerwiderung mit korrekter Bestreitenshöhe nach § 138 ZPO. Wahrheits- und Substantiierungslast als Drafting-Treiber. Unterscheidung zwischen einfachem Bestreiten und substantiiertem Bestreiten mit Behauptung des Gegenteils. Beweislastverteilung steuert die Architektur. Aufbau: Eingangsformel, Antrag auf Klageabweisung, Sachverhalt mit Bestreitens-Architektur, rechtliche Würdigung, Hilfsantrag (Aufrechnung; Zurückbehaltung), Beweisangebote. Mit Mustertext und Pitfalls. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Haftungsausschluss Haftungsbegrenzung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `haftungsausschluss-und-haftungsbegrenzung`

**Fokus:** Haftungsklauseln im deutschen Recht sauber bauen. Pflichtgrenzen § 276 Abs. 3 BGB (Vorsatz nie ausschliessbar), § 309 Nr. 7 BGB (AGB-Klauselverbote fuer Vorsatz grobe Fahrlaessigkeit Kardinalpflichten Koerperschaden), § 444 BGB (arglistig verschwiegener Mangel), § 11 ProdHaftG (zwingend bei Personenschaden). Drafting-Strategien Summenbegrenzung Zeitbegrenzung Ausschluss mittelbarer Schaeden. Mit Tabelle B2B vs B2C und Mustertexten.

# Haftungsausschluss und Haftungsbegrenzung

## Zweck

Haftungsklauseln sind die wirtschaftlich wichtigste Kategorie in vielen Vertraegen. Sie sind gleichzeitig die rechtlich riskanteste: Ein zu weit gefasster Ausschluss ist nichtig und reisst die gesamte Klausel mit. Ein zu enger Ausschluss laesst Haftung stehen, die kalkulatorisch nicht gewollt war.

Dieser Skill liefert die Pflichtgrenzen (was nie ausgeschlossen werden kann), die typischen Drafting-Strategien (Summenbegrenzung, Zeitbegrenzung, Ausschluss mittelbarer Schaeden) und Mustertexte fuer B2B und B2C. Er zeigt die Tabelle, in der die meisten Drafter scheitern.

## Eingaben

- Vertragstyp und Parteien (B2B oder B2C)
- AGB oder Individualabrede
- Branchenrisiko (Personenschaden, Datenschutz, IP-Risiken)
- Versicherungsschutz (Hoehe der Haftpflichtversicherung)
- Verhandlungsposition

## Rechtlicher und methodischer Rahmen

- § 276 Abs. 3 BGB: Haftung wegen Vorsatzes kann dem Schuldner im voraus nicht erlassen werden.
- § 309 Nr. 7 BGB: AGB-Klauselverbot fuer Ausschluss bei Vorsatz und grober Fahrlaessigkeit, fuer Verletzung von Leben Koerper Gesundheit und fuer Kardinalpflichten.
- § 307 BGB: AGB-Generalklausel. Auch im B2B begrenzt.
- § 444 BGB: Bei arglistig verschwiegenem Mangel kein Haftungsausschluss.
- § 11 ProdHaftG: Haftung nach Produkthaftungsgesetz kann nicht ausgeschlossen oder begrenzt werden.
- § 14 OWiG, § 75 AktG, § 43 GmbHG: Haftung der Geschaeftsleitung. Nicht beliebig ausschliessbar.

## Ablauf / Checkliste

1. **Was wird ausgeschlossen?** Schadensersatz, Schadensersatz statt der Leistung, Mangelfolgeschaden, mittelbarer Schaden?
2. **Wessen Haftung?** Schuldner selbst, Erfuellungsgehilfen (§ 278 BGB), gesetzliche Vertreter?
3. **Verschuldungsgrad?** Einfache Fahrlaessigkeit, grobe Fahrlaessigkeit, Vorsatz?
4. **Welche Pflicht?** Kardinalpflicht oder Nebenpflicht?
5. **AGB oder Individualabrede?** Im AGB-Verhaeltnis gelten Klauselverbote.
6. **Hoehe der Begrenzung?** Summenmaessig, deckungsgleich mit Haftpflichtversicherung?
7. **Zeitliche Begrenzung?** Verkuerzung der Verjaehrung nach § 202 BGB beachten.

### Pflichtgrenzen-Tabelle

| Tatbestand | B2B (AGB) | B2C (AGB) | Individualvertrag |
|---|---|---|---|
| Vorsatz | nie ausschliessbar (§ 276 Abs. 3 BGB) | nie ausschliessbar | nie ausschliessbar |
| Grobe Fahrlaessigkeit eigener Personen | grundsaetzlich nicht in AGB (§ 309 Nr. 7 BGB analog) | nie ausschliessbar | nur eingeschraenkt |
| Grobe Fahrlaessigkeit Erfuellungsgehilfen | begrenzt zulaessig | nie ausschliessbar | begrenzt zulaessig |
| Leben Koerper Gesundheit | nie ausschliessbar | nie ausschliessbar | nie ausschliessbar |
| Kardinalpflichten leicht fahrlaessig | nur summenmaessig auf vorhersehbaren Schaden | nur summenmaessig auf vorhersehbaren Schaden | summenmaessige Begrenzung zulaessig |
| Sonstige leichte Fahrlaessigkeit | ausschliessbar | begrenzt ausschliessbar | ausschliessbar |
| Arglistig verschwiegener Mangel | § 444 BGB | § 444 BGB | § 444 BGB |
| Produkthaftung Personenschaden | § 11 ProdHaftG | § 11 ProdHaftG | § 11 ProdHaftG |

### Drafting-Strategien

1. **Differenzierte Klausel:** Trennen Sie nach Verschuldensgrad und Pflichtart.
2. **Summenmaessige Begrenzung:** "Begrenzt auf den vorhersehbaren typischen Schaden, maximal Euro X."
3. **Zeitliche Begrenzung:** Verjaehrungsverkuerzung nach § 202 BGB; auf ein Jahr im B2B, im B2C nicht unter zwei Jahre fuer neue Sachen.
4. **Ausschluss mittelbarer Schaeden:** Konkret formulieren: "Indirekte Schaeden, entgangener Gewinn, Datenverlust." Vorsicht bei AGB.

### Mustertext B2B (AGB-fest)

```
§ 7 Haftung

(1) Der Lieferant haftet unbeschraenkt:
 a) bei Vorsatz und grober Fahrlaessigkeit der Geschaeftsleitung oder
 leitender Angestellter;
 b) bei Verletzung von Leben Koerper Gesundheit, auch durch
 Erfuellungsgehilfen;
 c) bei Arglist (§ 444 BGB);
 d) nach Produkthaftungsgesetz (§ 11 ProdHaftG).

(2) Bei leicht fahrlaessiger Verletzung wesentlicher Vertragspflichten
 (Kardinalpflichten) ist die Haftung begrenzt auf den bei Vertrags-
 schluss vorhersehbaren typischen Schaden, hoechstens jedoch auf
 [Betrag in Euro] je Schadensfall.

(3) Im Uebrigen ist die Haftung des Lieferanten ausgeschlossen, insbesondere
 fuer indirekte Schaeden, entgangenen Gewinn und Datenverlust.

(4) Ansprueche verjaehren in zwei Jahren ab gesetzlichem Verjaehrungsbeginn,
 Anspruechee aus Vorsatz und nach Produkthaftungsgesetz nach den
 gesetzlichen Vorschriften.
```

### Mustertext B2C (AGB-Verbraucher)

```
§ 7 Haftung

(1) Wir haften unbeschraenkt:
 a) bei Vorsatz und grober Fahrlaessigkeit;
 b) bei Verletzung von Leben Koerper Gesundheit;
 c) nach Produkthaftungsgesetz;
 d) im Umfang einer uebernommenen Garantie.

(2) Bei leicht fahrlaessiger Verletzung wesentlicher Vertragspflichten
 haften wir auf den bei Vertragsschluss vorhersehbaren typischen Schaden.

(3) Eine weitergehende Haftung ist ausgeschlossen.
```

## Typische Drafting-Fehler

- **Pauschal-Ausschluss "jede Haftung wird ausgeschlossen".** Nichtig nach § 307 BGB und § 309 Nr. 7 BGB.
- **Vorsatz vergessen.** Ohne Klarstellung wird die Klausel als Versuch gewertet, auch Vorsatz auszuschliessen.
- **Kardinalpflichten nicht definiert.** Begriff aus BGH-Rspr. Definition in der Klausel klarstellen.
- **Summenbegrenzung ohne Bezug.** "Maximal 1000 Euro" bei einem Vertragsvolumen von 5 Mio Euro ist Indikator fuer Unwirksamkeit.
- **Verjaehrungsverkuerzung unter zwei Jahre im B2C.** Bei neuen Sachen nach § 309 Nr. 8 lit. b ff BGB Klauselverbot.
- **Arglistklausel umgangen.** § 444 BGB kann nicht abbedungen werden.

## Ausgabeformat

- Haftungsklausel fertig formuliert, gegliedert nach Verschuldensgrad.
- Tabelle B2B vs. B2C mit Vergleich.
- Hinweis auf Versicherungsdeckung.

## Beispiel

**Aufgabe:** Haftungsklausel fuer einen IT-Dienstleistervertrag (B2B) mit Vertragsvolumen 200.000 Euro pro Jahr, Berufshaftpflicht des Dienstleisters mit Deckungssumme 5 Mio Euro je Schadensfall.

**Loesung:**

```
§ 7 Haftung

(1) Unbeschraenkte Haftung
Der Dienstleister haftet unbeschraenkt bei Vorsatz, grober Fahrlaessigkeit,
Verletzung von Leben Koerper Gesundheit, Arglist sowie nach Produkthaftungs-
gesetz.

(2) Kardinalpflichten
Bei leicht fahrlaessiger Verletzung von Kardinalpflichten ist die Haftung
begrenzt auf den bei Vertragsschluss vorhersehbaren typischen Schaden,
hoechstens jedoch auf 500.000 Euro je Schadensfall und 1.000.000 Euro pro
Jahr. Kardinalpflichten sind solche, deren Erfuellung den Vertrag erst
ermoeglicht und auf deren Einhaltung der Auftraggeber regelmaessig vertrauen
darf.

(3) Im Uebrigen ist die Haftung ausgeschlossen, insbesondere fuer mittelbare
Schaeden, entgangenen Gewinn und Datenverlust.

(4) Verjaehrung
Schadensersatzanspruechee verjaehren in zwei Jahren ab gesetzlichem
Verjaehrungsbeginn. Anspruechee nach Abs. 1 verjaehren nach den
gesetzlichen Vorschriften.
```

## Querverweise

- `anspruchsgrundlage-und-rechtsfolgen-klauseln`
- `agb-konforme-klauseln-305-310-bgb`
- `b2b-vs-b2c-klausel-strategie`
- `boilerplate-klauseln-katalog`

## Quellen (Stand 05/2026)

- § 276 Abs. 3 BGB, § 278 BGB, § 307 BGB, § 309 Nr. 7 BGB, § 309 Nr. 8 BGB, § 444 BGB, § 202 BGB. gesetze-im-internet.de.
- § 11 ProdHaftG. gesetze-im-internet.de/prodhaftg/.
- BGH-Rspr. zu Kardinalpflichten und summenmaessiger Begrenzung: vom Nutzer mit konkretem Aktenzeichen ueber bundesgerichtshof.de zu verifizieren.

## 2. `klageerwiderung-substantiiertes-bestreiten`

**Fokus:** Drafting einer Klageerwiderung mit korrekter Bestreitenshöhe nach § 138 ZPO. Wahrheits- und Substantiierungslast als Drafting-Treiber. Unterscheidung zwischen einfachem Bestreiten und substantiiertem Bestreiten mit Behauptung des Gegenteils. Beweislastverteilung steuert die Architektur. Aufbau: Eingangsformel, Antrag auf Klageabweisung, Sachverhalt mit Bestreitens-Architektur, rechtliche Würdigung, Hilfsantrag (Aufrechnung; Zurückbehaltung), Beweisangebote. Mit Mustertext und Pitfalls.

# Klageerwiderung und substantiiertes Bestreiten

## Zweck

Die Klageerwiderung ist die erste schriftliche Verteidigung der Beklagtenseite. Sie entscheidet über die Bestreitenshöhe und damit über die Beweislast. § 138 ZPO ist die zentrale Norm: Tatsachen sind vollständig und der Wahrheit gemäß zu erklären; Bestreiten muss substantiiert sein, wo dem Beklagten ein eigener Vortrag möglich und zumutbar ist.

Dieser Skill führt Sie durch den Aufbau, hilft bei der Bestreitens-Architektur und liefert einen Mustertext. Er richtet sich an Drafter, die eine Erwiderung in der Klageschrift-Frist erstellen oder ein Konzept für die mündliche Verhandlung schreiben.

## Eingaben

- Klageschrift (Antrag, Begründung, Anlagen)
- Beklagtenmandat und dessen Sicht des Sachverhalts
- Frist nach § 277 ZPO (Klageerwiderungsfrist nach gerichtlicher Anordnung)
- Eigene Beweismittel (Urkunden, Zeugen, Sachverständige)
- Gegenforderungen (für Aufrechnung oder Hilfsantrag)
- Risiko-Einschätzung des Mandanten

## Rechtlicher und methodischer Rahmen

- § 138 Abs. 1 ZPO: Wahrheitspflicht. Erklärung über tatsächliche Umstände vollständig und wahrheitsgemäß.
- § 138 Abs. 2 ZPO: Erklärungspflicht zu jeder vom Gegner behaupteten Tatsache.
- § 138 Abs. 3 ZPO: Nicht ausdrücklich bestrittene Tatsachen gelten als zugestanden.
- § 138 Abs. 4 ZPO: Erklärung mit Nichtwissen nur zulässig, soweit die Tatsachen weder eigene Handlungen der Partei noch Gegenstand eigener Wahrnehmung sind.
- § 277 ZPO: Klageerwiderungsfrist; Verspätung kann zur Präklusion nach §§ 296, 296a ZPO führen.
- § 33 ZPO: Widerklage am Gerichtsstand der Klage.
- § 145 Abs. 3 ZPO: Hilfsaufrechnung; Höhe muss bestimmt sein.
- §§ 273, 320, 348, 1000 BGB: Materielle Grundlagen für Zurückbehaltungsrechte.
- Beweislast: Anspruchsteller trägt für die anspruchsbegründenden Tatsachen, Beklagter für rechtshindernde, rechtsvernichtende und rechtshemmende.
- Methodik: Urteilsstil. Bestreiten muss klar formuliert sein.

## Ablauf / Checkliste

1. **Klageschrift segmentieren.** Jeder Tatsachenvortrag bekommt eine Nummer. Jeder Nummer ein Status: zugestanden, einfach bestritten, substantiiert bestritten, mit Nichtwissen erklärt.
2. **Bestreitenshöhe wählen.** Substantiiert bestreiten, wo eigene Wahrnehmung oder eigenes Handeln möglich ist. Einfach bestreiten nur, wo § 138 Abs. 4 ZPO greift.
3. **Beweislastrolle prüfen.** Bei rechtshindernden, rechtsvernichtenden, rechtshemmenden Tatsachen liegt die Last bei der Beklagtenseite. Diese müssen voll substantiiert behauptet werden.
4. **Antrag formulieren.** Hauptantrag: Klageabweisung. Hilfsantrag nur bei Aufrechnung mit Gegenforderung oder Zurückbehaltungsrecht.
5. **Sachverhalt darstellen.** Eigene Version der Geschehnisse. Streitig dargestellte Tatsachen mit Beweisangebot belegen.
6. **Rechtliche Würdigung.** Anspruch verneinen oder einwendungsweise einschränken. Klare Subsumtion ohne Lehrbuchprosa.
7. **Aufrechnung dosieren.** Hilfsweise Aufrechnung erst nach Begründung des Hauptverteidigungsgrunds. Aufrechnungshöhe konkret beziffern.
8. **Beweisangebote setzen.** Hinter jeder eigenen Tatsachenbehauptung. Keine Pauschalbeweise.
9. **Anlagenverzeichnis B1 ff.** Fortlaufend nummerieren.

### Bestreitens-Architektur Tabelle

| Klagebehauptung | Eigene Wahrnehmung möglich? | Bestreitenshöhe | Beispiel |
|---|---|---|---|
| Liefertermin | Ja | Substantiiert | "Die Lieferung erfolgte am 5. Februar, nicht am 1. Februar. Beweis: Lieferschein, Anlage B1" |
| Inhalt einer Telefonkonferenz mit Dritten | Nein | Mit Nichtwissen § 138 Abs. 4 ZPO | "Die behauptete Telefonkonferenz wird mit Nichtwissen bestritten." |
| Höhe einer Marktpreisangabe | Ggf. ja | Substantiiert mit Gegenbehauptung | "Der Marktpreis lag bei höchstens 18.000 Euro. Beweis: Sachverständigengutachten" |
| Ein interner Vorgang bei der Klägerseite | Nein | Mit Nichtwissen | "Die internen Vorgänge auf Klägerseite werden mit Nichtwissen bestritten." |

## Typische Drafting-Fehler

- **Pauschales Bestreiten.** "Es wird alles bestritten" verstößt gegen § 138 ZPO und kann zur Geständnisfiktion führen.
- **Fehlende Substanz bei eigener Behauptung.** Wer behauptet, muss vortragen und beweisen. "Es war anders" reicht nicht.
- **Hilfsaufrechnung ohne Höhe.** Die Gegenforderung muss nach Grund und Höhe bestimmt sein.
- **Nichtwissen-Erklärung trotz eigener Wahrnehmung.** § 138 Abs. 4 ZPO gilt nicht für eigene Vorgänge.
- **Reihenfolgefehler.** Aufrechnung vor Verteidigung. Erst gewinnen wollen, dann hilfsweise rechnen.
- **Präklusion durch Fristversäumnis.** § 296 ZPO greift hart. Frist beachten.

## Ausgabeformat

- Vollständige Klageerwiderung im Schriftsatzformat.
- Bei Konzeptphase: tabellarische Bestreitens-Matrix plus Skizze der Anträge.
- Stets Anlagenverzeichnis B1 ff.

## Beispiele

### Mustertext Klageerwiderung (Auszug)

```
Landgericht Berlin Berlin, den 5. Juni 2026
Az.: 12 O 345/26

 Klageerwiderung

In dem Rechtsstreit Anna Muster gegen Beklagt GmbH

zeigen wir namens und in Vollmacht der Beklagten an, dass wir sie
vertreten. Wir werden beantragen:

Die Klage wird abgewiesen.

Hilfsweise: Die Klägerin wird verurteilt, an die Beklagte 4.000 Euro zu
zahlen Zug um Zug gegen Rücknahme der Maschinen Typ A-100.

 Begründung

I. Sachverhalt

1. Der Abschluss des Kaufvertrags vom 15. Januar 2026 (Klageschrift S. 2)
wird zugestanden.

2. Die behauptete Lieferung am 1. Februar 2026 wird bestritten.
Die Lieferung erfolgte erst am 5. Februar 2026.
Beweis: Lieferschein vom 5. Februar 2026, Anlage B1.

3. Es wird bestritten, dass die gelieferten Maschinen mangelfrei waren.
Drei der zehn Maschinen wiesen bereits bei Lieferung Korrosion am Antrieb
auf. Die Klägerin wurde am 8. Februar 2026 schriftlich gerügt.
Beweis: Mängelanzeige vom 8. Februar 2026, Anlage B2.

4. Die internen Vorgänge auf Klägerseite zur Kaufpreisberechnung werden
mit Nichtwissen bestritten (§ 138 Abs. 4 ZPO).

II. Rechtliche Würdigung

Der Kaufpreisanspruch nach § 433 Abs. 2 BGB ist nicht fällig, weil die
Beklagte ein Zurückbehaltungsrecht aus § 320 BGB hat. Die Mangelhaftigkeit
dreier Maschinen begründet Nacherfüllungsanspruch nach § 437 Nr. 1, § 439
BGB. Die Beklagte hat ihrerseits Rückzahlung des bezahlten Anteils zu
fordern (Anlage B2).

Anlagenverzeichnis:
B1 Lieferschein vom 5. Februar 2026
B2 Mängelanzeige vom 8. Februar 2026

Marta Verteidiger
Rechtsanwalt
```

## Querverweise

- `klage-drafting-253-zpo` für die Klägerseite
- `dokumentarchitektur-vertrag-und-schriftsatz`
- `gutachten-memo-internes-drafting` für die interne Vorbereitung
- `revisions-prozess-redlines-comparison` für Abstimmung mit dem Mandanten

## Quellen (Stand 05/2026)

- §§ 138, 145 Abs. 3, 277, 296 ZPO; gesetze-im-internet.de.
- §§ 320, 273, 387 ff. BGB für Zurückbehaltung und Aufrechnung.
- BGH-Rechtsprechung zum substantiierten Bestreiten und zur sekundären Darlegungslast: vom Nutzer zu verifizieren. Keine Aktenzeichen aus Modellwissen.
- `references/zitierweise.md` für Belegpflicht.
