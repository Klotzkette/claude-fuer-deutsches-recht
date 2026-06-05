---
name: gerichtsstand-rechtswahl-intwr-cisg-rom
description: "Gerichtsstand Und Rechtswahl Prüfen, Intwr Cisg Pruefraster, Intwr Rom I Ii Leitfaden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Gerichtsstand Und Rechtswahl Prüfen, Intwr Cisg Pruefraster, Intwr Rom I Ii Leitfaden

## Arbeitsbereich

Dieser Skill bündelt **Gerichtsstand Und Rechtswahl Prüfen, Intwr Cisg Pruefraster, Intwr Rom I Ii Leitfaden** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `gerichtsstand-und-rechtswahl-pruefen` | Arbeitsmodul zu gerichtsstand und rechtswahl pruefen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `intwr-cisg-pruefraster` | Pruefraster CISG / UN-Kaufrecht: sachlicher und persoenlicher Anwendungsbereich, Vertragsschluss, Lieferpflichten, Pflichtverletzung, Rechtsbehelfe. Vergleich mit BGB-Kaufrecht. |
| `intwr-rom-i-ii-leitfaden` | Leitfaden Rom I und Rom II: Anknuepfungsregeln vertragliche und ausservertragliche Schuldverhaeltnisse, Eingriffsnormen Art. 9 Rom I, ordre public. Pruefraster fuer Rechtswahl und gewoehnlicher Aufenthalt. |

## Arbeitsweg

Für **Gerichtsstand Und Rechtswahl Prüfen, Intwr Cisg Pruefraster, Intwr Rom I Ii Leitfaden** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `fachanwalt-internationales-wirtschaftsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `gerichtsstand-und-rechtswahl-pruefen`

**Fokus:** Arbeitsmodul zu gerichtsstand und rechtswahl pruefen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## Mandantenfragen beim Kaltstart

1. Haben beide Parteien ihren Sitz in EU-Mitgliedstaaten (→ Brüssel Ia VO) oder ist eine Partei in der Schweiz/Norwegen/Island (→ Lugano) oder einem Drittstaat (→ §§ 12 ff. ZPO)?
2. Enthält der Vertrag eine Gerichtsstandsklausel nach Art. 25 Brüssel Ia – ist sie schriftlich, bestimmt und wirksam vereinbart?
3. Gibt es eine Schiedsklausel – welche Institution (ICC, LCIA, DIS, UNCITRAL), welcher Sitz, welches Schiedsrecht?
4. Soll deutsches Recht oder das Recht eines anderen Staates angewendet werden – wurde CISG ausdrücklich abbedungen (Art. 6 CISG)?
5. Wo soll ein Urteil vollstreckt werden – liegt ein Haager Vollstreckungsübereinkommen oder Brüssel-Ia-Mechanismus vor?
6. Handelt es sich um eine deliktische oder außervertragliche Streitigkeit – gilt Rom II VO?
7. Ist eine der Parteien Verbraucher oder Arbeitnehmer – greifen Sonderschutzmechanismen Art. 17 ff. bzw. Art. 21 ff. Brüssel Ia VO?
8. Handelt es sich um einen neuen Vertragsentwurf oder einen laufenden Streit – ist präventive Klauselgestaltung oder prozessuale Zuständigkeitsprüfung gefragt?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| Brüssel Ia VO Art. 25 | Gerichtsstandsvereinbarung: schriftlich, bestimmt, ausschließlich (Vermutung); asymmetrische Klauseln wirksam |
| Brüssel Ia VO Art. 7 Nr. 1 | Besonderer Gerichtsstand Erfüllungsort: Warenkauf → Lieferort; Dienstleistung → Erbringungsort |
| Brüssel Ia VO Art. 7 Nr. 2 | Delikt: Handlungs- oder Erfolgsort (Klägerwahlrecht) |
| Brüssel Ia VO Art. 17–23 | Verbraucherschutz-Gerichtsstände: Klage Verbraucher am Wohnsitz; gegen Verbraucher nur Wohnsitz |
| Brüssel Ia VO Art. 21–23 | Arbeitnehmer-Schutz: Klage am gewöhnlichen Arbeitsort oder Sitz Arbeitgeber |
| Brüssel Ia VO Art. 36–45 | Anerkennung + Vollstreckung ohne Exequatur (Art. 39); Versagungsgründe Art. 45 |
| Lugano-Übereinkommen 2007 | Entspricht Brüssel Ia für EFTA-Staaten (Schweiz, Norwegen, Island) |
| § 1029 ZPO | Schiedsvereinbarung: jede vermögensrechtliche Streitigkeit; Schriftform § 1031 ZPO |
| § 1031 ZPO | Schriftform Schiedsvereinbarung: Urkunde oder sonstige dauerhafter Form; Telex/Fax/E-Mail genügen |
| § 328 ZPO | Anerkennung ausländischer Urteile aus Nicht-EU: Zuständigkeit, Zustellung, Ordre public, Gegenseitigkeit |
| New Yorker Übereinkommen 1958 | Anerkennung ausländischer Schiedssprüche weltweit (ca. 170 Vertragsstaaten) |
| Rom I VO Art. 3 | Parteiautonomie: freie Rechtswahl bei Schuldverträgen; Rückausnahmen bei internem Sachverhalt Art. 3 Abs. 3 |
| Rom I VO Art. 4 | Mangels Wahl: charakteristische Leistung → Sitz des Leistenden (Verkäufer, Dienstleister) |
| Rom I VO Art. 6 | Verbraucherverträge: günstigeres zwingendes Recht des Wohnsitzstaates bleibt erhalten |
| Rom I VO Art. 8 | Arbeitsverträge: günstigeres zwingendes Recht des gewöhnlichen Arbeitsortes |
| Rom I VO Art. 9 | Eingriffsnormen (Overriding Mandatory Provisions): gelten unabhängig von Rechtswahl |
| Rom II VO Art. 4 | Außervertragliche Schuldverhältnisse: Erfolgsort; gemeinsamer Aufenthalt Art. 4 Abs. 2; engste Verbindung Art. 4 Abs. 3 |
| Rom II VO Art. 6 | Unlauterer Wettbewerb: Recht des Marktes wo Wettbewerb betroffen |
| CISG Art. 1 | Anwendungsbereich: int. Warenkauf, Parteien in verschiedenen CISG-Staaten |
| CISG Art. 6 | Abbedingung: ausdrücklich oder durch Verweis nur auf BGB/nationale Normen |

## Leitentscheidungen

| Gericht | AZ | Datum | Kernaussage |
|---------|----|-------|-------------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema

| Schritt | Prüfpunkt | Norm | Rechtsfolge |
|---------|-----------|------|-------------|
| 1 | Personeller Anwendungsbereich: Beklagter Sitz EU? | Brüssel Ia Art. 4 | Brüssel Ia gilt; sonst Lugano oder §§ 12 ff. ZPO |
| 2 | Ausschließliche Gerichtsstände Art. 24 prüfen (Grundstücke, Gesellschaften, Immaterialgüter) | Art. 24 Brüssel Ia | Verdrängen alle anderen; kein Abweichen möglich |
| 3 | Gerichtsstandsklausel Art. 25 prüfen: Form, Bestimmtheit, Ausschließlichkeit | Art. 25 Brüssel Ia | Wirksame Klausel = derogierter/prorogierter Gerichtsstand |
| 4 | Schiedsklausel § 1029 ZPO prüfen: Schriftform § 1031 ZPO, Schiedsfähigkeit § 1030 ZPO | §§ 1029–1031 ZPO | Schiedsgericht hat Vorrang; staatl. Gericht erklärt sich unzuständig § 1032 ZPO |
| 5 | Besondere Gerichtsstände Art. 7 prüfen (Erfüllungsort, Delikt, Niederlassung) | Art. 7 Brüssel Ia | Alternativ zu allgemeinem Gerichtsstand Art. 4 |
| 6 | Sonderschutz-Gerichtsstände (Verbraucher Art. 17, Arbeitnehmer Art. 21) | Art. 17–23 Brüssel Ia | Schutzzweck: schwächere Partei soll am Wohnsitz klagen können |
| 7 | Anwendbares Recht: Rechtswahl Art. 3 Rom I wirksam? | Art. 3 Rom I | Bei wirksamer Wahl gilt gewähltes Recht; Eingriffsnormen Art. 9 bleiben |
| 8 | CISG: anwendbar bei internationalem Warenkauf? Abbedungen? | CISG Art. 1, 6 | CISG gilt automatisch sofern nicht abbedungen |
| 9 | Vollstreckbarkeit: wo soll vollstreckt werden? EU → Art. 36 ff. Brüssel Ia; Nicht-EU → § 328 ZPO | Art. 36, § 328 ZPO | Vollstreckungsweg bestimmt Klagestrategie |
| 10 | Neue Klausel: Empfehlungen für Gerichtsstand, Rechtswahl, CISG-Klarstellung, Schiedsklausel formulieren | Art. 25 Brüssel Ia, § 1029 ZPO | Vertragssicherheit für Mandant |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Gerichtsstand und Rechtswahl pruefen/formulieren | Gutachten Bruessel Ia / Rom I; Template unten |
| Variante A — Kein Vertrag vorhanden | Deliktisches Anknuepfung nach Rom II Art. 4 ff. pruefen |
| Variante B — Schiedsklausel im Vertrag | Bruessel Ia nicht anwendbar; §§ 1025 ff. ZPO einschlaegig |
| Variante C — Drittstaaten ohne Bruessel Ia | Hague Judgments Convention / nationales IPR; HAVÜ 2019 |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatz-Bausteine

### Gerichtsstands- und Rechtswahlklausel (B2B, Deutschland als Gerichtsstand)

```
Gerichtsstand und anwendbares Recht

1. Für alle Streitigkeiten aus oder im Zusammenhang mit diesem Vertrag,
 einschließlich Streitigkeiten über dessen Gültigkeit, Auslegung oder
 Beendigung, sind ausschließlich die Gerichte in [München/Frankfurt/Hamburg]
 zuständig (§ 38 ZPO; Art. 25 Brüssel Ia VO).

2. Dieser Vertrag unterliegt dem Recht der Bundesrepublik Deutschland
 unter Ausschluss der Kollisionsnormen des Internationalen Privatrechts
 und unter ausdrücklichem Ausschluss des UN-Kaufrechts (CISG).
```

### Schiedsklausel (ICC)

```
Schiedsvereinbarung

Alle Streitigkeiten aus oder im Zusammenhang mit diesem Vertrag, einschließlich
Streitigkeiten über seine Begründung, Wirksamkeit oder Beendigung, werden
abschließend durch Schiedsgerichtsbarkeit nach den ICC-Schiedsregeln entschieden.
Schiedsort ist [Frankfurt am Main / Zürich]. Anzahl der Schiedsrichter: [ein/drei].
Schiedssprache: [Deutsch / Englisch].
Auf das Schiedsverfahren findet das Recht des Schiedsortes (lex arbitri) Anwendung.
```

### Rüge der Unzuständigkeit (Einrede der Schiedsvereinbarung)

```
An das [Landgericht Ort], Az. [O XX/YY]

Klageerwiderung – Unzuständigkeitsrüge

Die Beklagte rügt die internationale Zuständigkeit des angerufenen Gerichts.

I. Der Vertrag vom [Datum] (Anlage B1) enthält in Ziffer [X] eine wirksame
 Schiedsvereinbarung i.S.v. § 1029 Abs. 1 ZPO zugunsten der ICC (Paris),
 Schiedsort [Ort].

II. Die Schiedsvereinbarung ist formwirksam gemäß § 1031 ZPO (unterzeichnetes
 Vertragsdokument; alternativ per E-Mail dokumentiert Anlage B2).

III. Gemäß § 1032 Abs. 1 ZPO ist das staatliche Gericht auf Rüge der Beklagten
 für unzuständig zu erklären.

Antrag: Das Gericht möge die Klage als unzulässig abweisen.
```

### Vollstreckungsantrag Brüssel Ia (EU-Urteil)

```
An das Amtsgericht [Vollstreckungsgericht]

Antrag auf Vollstreckung eines ausländischen Titels gemäß Art. 39 Brüssel Ia VO

Gläubigerin: [Firma], Sitz [EU-Staat]
Schuldner: [Name], Wohnsitz [Deutschland]

Das [Gericht, Staat, Datum] verurteilte den Schuldner durch rechtskräftiges Urteil
vom [Datum], Az. [XX], zur Zahlung von EUR [Betrag] an die Gläubigerin.

Gemäß Art. 39 Brüssel Ia VO ist das Urteil in anderen EU-Mitgliedstaaten ohne
Exequatur vollstreckbar. Wir übersenden beglaubigte Ausfertigung (Art. 37 Abs. 1)
sowie die Bescheinigung nach Art. 53 Brüssel Ia (Anlage 1).

Wir beantragen: Zwangsvollstreckung aus diesem Titel anzuordnen.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast

| Frage | Beweislast |
|-------|-----------|
| Wirksamkeit Gerichtsstandsklausel Art. 25 | Diejenige Partei, die sich auf die Klausel beruft; Form und Bestimmtheit nachweisen |
| Schiedsvereinbarung § 1029 ZPO | Beklagte: Schriftformnachweis § 1031; Kläger kann Unwirksamkeit der Schiedsvereinbarung geltend machen |
| Anwendbarkeit Brüssel Ia | Gericht prüft von Amts wegen (Klausel/Sitz Beklagter) |
| Versagungsgrund Art. 45 Brüssel Ia (Ordre public) | Vollstreckungsschuldner: behaupten und darlegen |
| Anwendbarkeit CISG | Vertragspartei, die CISG geltend macht; Abbedingung ist von Gegner zu beweisen |

## Fristen

| Verfahrensschritt | Frist |
|-------------------|-------|
| Rüge der Schiedseinrede § 1032 ZPO | Vor erster mündlicher Verhandlung (§ 1032 Abs. 1 ZPO) |
| Vollstreckungsantrag Brüssel Ia | Keine Frist; Rechtskraft des ausländ. Urteils muss vorliegen |
| Vollstreckungsversagung Art. 46 Brüssel Ia | Unverzüglich nach Kenntnis der Vollstreckungsmaßnahme |
| Anerkennung § 328 ZPO (Nicht-EU) | Klage auf Anerkennung oder Einrede; Verjährung nach Recht des Auslandsurteils |
| Beschwerde gegen Schiedsspruch § 1059 ZPO | 3 Monate ab Zustellung des Schiedsspruchs |
| Schiedsklageerhebung vor Schiedsgericht | Verjährung nach anwendbarem Sachrecht; hemmt Verjährung bei Einleitung |

## Gegenargumente und Reaktion

| Gegenargument | Rechtliche Grundlage | Reaktion |
|---------------|---------------------|---------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Schiedsklausel unwirksam (Überraschungsklausel AGB) | § 305c BGB, § 1029 ZPO | Im B2B gilt AGB-Kontrolle eingeschränkt; Klausel nicht überraschend bei handelsüblichen Vertragsbedingungen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Ordre-public-Einwand gegen ausländ. Urteil | Art. 45 Abs. 1 lit. a Brüssel Ia, § 328 Abs. 1 Nr. 4 ZPO | Nur bei Kernverstoß gegen dt. Grundwertungen; bloße Rechtsabweichung genügt nicht |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Eingriffsnormen vereiteln gewähltes Recht | Art. 9 Rom I | Auftrag an Vertragspartner: Eingriffsnormen (z.B. Embargorecht, Wettbewerbsrecht) ausdrücklich im Vertrag adressieren |

## Streitwert und Kosten

Gerichtsstand-Rüge (§ 1032 ZPO-Antrag): Gegenstandswert = Hauptsachewert; Gebühren nach GKG/RVG.

Schiedsverfahren ICC: Registrierungsgebühr 5.000 USD + administrative Kosten nach Streitwertskala; ab 1 Mio. EUR Streitwert ca. 15.000–80.000 EUR Schiedsgerichtskosten.

DIS-Verfahren: günstigere Kostenstruktur als ICC; Verwaltungsgebühr nach § 7 DIS-Kostenordnung.

Vollstreckung Brüssel Ia: Gerichtskosten gering (Anlagekosten ca. 200–500 EUR); Hauptaufwand: beglaubigte Übersetzungen, Rechtsanwaltshonorar.

Vollstreckung § 328 ZPO (Nicht-EU): Anerkennungsklage erforderlich; volle Gerichts- und Anwaltskosten nach Streitwert.

## Strategische Empfehlung

| Situation | Empfehlung |
|-----------|-----------|
| Neuer B2B-Vertrag, internationaler Partner | Art. 25 Brüssel Ia-Klausel mit dt. Gerichtsstand + CISG-Ausschluss; alternativ DIS-Schiedsklausel |
| Hochwertiger Vertrag mit US-Partner | ICC-Schiedsklausel; Sitz Frankfurt oder Zürich; Englisch als Schiedssprache; kein dt. Staatsgerichtsstand |
| Vollstreckung eines dt. Urteils in Frankreich | Art. 39 Brüssel Ia direkt; Bescheinigung Art. 53 beim Ausgangsgericht beantragen |
| Vollstreckung in USA/Schweiz/UK | § 328 ZPO-Anerkennungsklage; Gegenseitigkeit und Ordre-public prüfen |
| Schiedseinrede vergessen | § 1032 ZPO: Einrede vor erster mündlicher Verhandlung; sonst Rügerecht verloren |
| Verbraucher-Gegenpartei | Gerichtsstandsklausel unwirksam; Verbraucher klagt am Wohnsitz; Schiedsklausel nach § 1031 Abs. 5 eigenhändig unterschreiben lassen |
| CISG unklar | Amendment zum Vertrag: ausdrückliche CISG-Ausschlussklausel "The CISG shall not apply" |

## Anschluss-Skills

- `fachanwalt-internationales-wirtschaftsrecht-cisg-pruefung` — CISG Prüfung Anwendungsbereich, Mängelrecht, Schadensersatz
- `sanktions-compliance-pruefung` — bei internationalen Verträgen Sanktionsrecht prüfen
- `fachanwalt-handels-gesellschaftsrecht-gesellschafterstreit` — Gesellschafterstreit mit ausländischem Bezug

## Quellen

- Brüssel Ia VO (EU) Nr. 1215/2012, ABl. L 351/1
- Rom I VO (EG) Nr. 593/2008, ABl. L 177/6
- Rom II VO (EG) Nr. 864/2007, ABl. L 199/40
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Geimer, Internationales Zivilprozessrecht, 8. Aufl. 2020
- Schack, Internationales Zivilverfahrensrecht, 7. Aufl. 2021
- New Yorker Übereinkommen v. 10.06.1958, BGBl. 1961 II S. 121
- ZPO §§ 1029 ff., § 328

<!-- AUDIT 27.05.2026: BGH VII ZR 167/13 (12.06.2014) NOT_FOUND auf dejure.org – ersetzt durch BGH VII ZR 139/17 (26.04.2018), NJW 2019, 76, verifiziert auf dejure.org. Kernaussage: Erfüllungsort Dienstleistung Art. 7 Nr. 1 Buchst. b Brüssel Ia. -->

## Vertiefung: Triage und Output-Template Gerichtsstand

### Triage — Bevor losgelegt wird, klaere:

1. Gibt es Gerichtsstandsklausel im Vertrag (Art. 25 Bruessel Ia)? → Schriftform, ausschliesslich?
2. Haben beide Parteien EU-Sitz? → Bruessel Ia; sonst: nationales IPR oder Hague Convention
3. Wurde Schiedsklausel vereinbart? → §§ 1025 ff. ZPO; nicht Bruessel Ia
4. Verbraucher oder Arbeitnehmer beteiligt? → Art. 17-22 Bruessel Ia Schutzgerichtsstand
5. Welches Recht anwendbar? → Unabhaengig von Zustaendigkeit: Rom I / Rom II

### Output-Template Gerichtsstand- und Rechtswahlgutachten
**Adressat:** Mandant oder Gericht — Tonfall: praezis-juristisch

```
GERICHTSSTAND- UND RECHTSWAHLGUTACHTEN
======================================
Vertrag: [BEZEICHNUNG] / [DATUM]
Parteien:
 Klaeger: [NAME, SITZ: EU / NICHT-EU]
 Beklagter: [NAME, SITZ: EU / NICHT-EU]

I. INTERNATIONALE ZUSTAENDIGKEIT
---------------------------------
1. Gerichtsstandsklausel (Art. 25 Bruessel Ia):
 [JA — [GERICHT, ORT] / NEIN]
2. Beklagter in EU: [JA: Art. 4 Bruessel Ia / NEIN: nationales Recht]
3. Besonderer Gerichtsstand (Art. 7):
 Vertrag: Erfuellungsort = [ORT] → Gerichtsstand [GERICHT]
 Delikt: Schadensort = [ORT] → Gerichtsstand [GERICHT]
4. Empfehlung Gerichtsstand: [GERICHT, ORT]

II. ANWENDBARES RECHT
----------------------
1. Rechtswahl (Art. 3 Rom I):
 [JA — [RECHTSORDNUNG] / NEIN]
2. Objektive Anknuepfung (Art. 4 Rom I):
 Charakteristische Leistung: [VERKAEUFER/DIENSTLEISTER, SITZ: LAND]
 → Anwendbares Recht: [RECHTSORDNUNG]
3. CISG: [ANWENDBAR / AUSGESCHLOSSEN]
4. Ergebnis: Anwendbares Recht: [RECHTSORDNUNG]
======================================
```

## 2. `intwr-cisg-pruefraster`

**Fokus:** Pruefraster CISG / UN-Kaufrecht: sachlicher und persoenlicher Anwendungsbereich, Vertragsschluss, Lieferpflichten, Pflichtverletzung, Rechtsbehelfe. Vergleich mit BGB-Kaufrecht.

# IntWR: CISG-Pruefraster

## Aufgabe
Pruefraster CISG / UN-Kaufrecht: sachlicher und persoenlicher Anwendungsbereich, Vertragsschluss, Lieferpflichten, Pflichtverletzung, Rechtsbehelfe.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster CISG (Wiener UN-Kaufrechtsuebereinkommen)

### 1. Anwendungsbereich

- **Sachlich** Art. 1-5 CISG
 - Kaufvertraege ueber Waren zwischen Parteien mit Niederlassung in verschiedenen Staaten (Art. 1 I lit. a CISG: beide Vertragsstaaten; lit. b: Verweisung des IPR auf Recht eines Vertragsstaats).
 - Ausnahmen Art. 2 CISG: Konsumgueterkauf, Auktion, Zwangsvollstreckung, Wertpapiere, Geld, Schiffe/Luftfahrzeuge, Strom.
 - Werklieferungsvertrag Art. 3 CISG: erfasst, wenn nicht wesentlicher Teil aus vom Besteller zu liefernden Stoffen.
 - Keine Anwendung auf Wirksamkeit/Vertragsschlusserforderlichkeit Art. 4 CISG.
- **Persoenlich** Art. 1, 10 CISG — Niederlassung; Sitz des engsten Zusammenhangs.
- **Opt-out** Art. 6 CISG — vollstaendiger oder teilweiser Ausschluss durch Parteivereinbarung moeglich (typische Praxis: "Es gilt deutsches Recht unter Ausschluss des UN-Kaufrechts").

### 2. Vertragsschluss Art. 14-24 CISG

- Angebot Art. 14: bestimmt, an Empfaenger gerichtet, Bindungswille.
- Annahme Art. 18: Erklaerung oder Handlung; Schweigen grds. nicht.
- Battle of forms: Modifizierte Annahme Art. 19 — bei wesentlicher Aenderung kein Vertragsschluss; bei nicht wesentlicher Aenderung Zustimmung des Anbietenden fingiert.

### 3. Pflichten der Parteien

- **Verkaeufer** Art. 30-44 CISG: Lieferung (Art. 31: am Ort gewerblicher Niederlassung), vertragsgemaesse Beschaffenheit (Art. 35), frei von Rechten Dritter (Art. 41-43).
- **Kaeufer** Art. 53-60 CISG: Kaufpreiszahlung, Abnahme, Untersuchungs- und Anzeigeobliegenheit Art. 38, 39 CISG.

### 4. Pflichtverletzung und Rechtsbehelfe

- **Wesentliche Vertragsverletzung** Art. 25 CISG: erheblicher Nachteil + Vorhersehbarkeit.
- **Rechtsbehelfe Kaeufer** Art. 45 ff. CISG: Erfuellung (Art. 46), Nachfrist (Art. 47), Minderung (Art. 50), Aufhebung (Art. 49 — nur bei wesentlicher Vertragsverletzung), Schadensersatz (Art. 74-77).
- **Rechtsbehelfe Verkaeufer** Art. 61 ff. CISG.
- **Beschraenkung des Schadensersatzes** Art. 74 CISG: nur vorhersehbarer Schaden; Schadensminderung Art. 77.

## Vergleich CISG vs. BGB-Kaufrecht (§§ 433 ff. BGB)

| Punkt | CISG | BGB |
|---|---|---|
| Mangelbegriff | Art. 35 (objektive und subjektive Erwartung) | § 434 |
| Anzeigeobliegenheit | Art. 38, 39: angemessene Frist nach Erkennen; 2-Jahres-Ausschlussfrist Art. 39 II | §§ 377, 378 HGB (im Handelskauf); BGB ohne Pflicht |
| Ruecktritt | Art. 49: nur bei wesentlicher Vertragsverletzung | § 323 BGB: Fristsetzung |
| Verjaehrung | UN-Verjaehrungsuebereinkommen 1974 (in DE nicht ratifiziert) -> Rueckgriff auf IPR | § 438 BGB: 2 Jahre |
| Hardship / Frustration | Art. 79: Befreiung bei Hinderungsgrund ausserhalb Einflussbereichs | § 313 BGB (Stoerung der Geschaeftsgrundlage) |

## Praxisfallen

- **Stillschweigender Ausschluss** des CISG bei "deutschem Recht" wird oft falsch angenommen — die Rechtswahl deutschen Rechts schliesst CISG NICHT aus; CISG ist Bestandteil des deutschen Rechts. **Ausdruecklicher Ausschluss noetig.**
- **Art. 39 CISG-Frist** zur Mangelanzeige: "innerhalb einer angemessenen Frist" — BGH zur Auslegung (BGHZ 129, 75 — Mussel-Wash). Bei Standardware: ca. ein Monat. Bei verderblicher Ware: Tage.
- **CISG-Ausschluss** vs. **Schiedsvereinbarung**: bei Schiedsvereinbarung CISG nicht automatisch ausgeschlossen.
- **OR Schweiz** und **CISG**: Schweiz Vertragsstaat seit 1991; bei Lieferungen DE-CH greift CISG ohne Opt-out.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `fachanwalt-internationales-wirtschaftsrecht`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `intwr-rom-i-ii-leitfaden`

**Fokus:** Leitfaden Rom I und Rom II: Anknuepfungsregeln vertragliche und ausservertragliche Schuldverhaeltnisse, Eingriffsnormen Art. 9 Rom I, ordre public. Pruefraster fuer Rechtswahl und gewoehnlicher Aufenthalt.

# IntWR: Rom I + II Leitfaden

## Aufgabe
Leitfaden Rom I-VO (593/2008) und Rom II-VO (864/2007): Anknuepfungsregeln vertragliche und ausservertragliche Schuldverhaeltnisse, Eingriffsnormen Art. 9 Rom I, ordre public Art. 21 Rom I / Art. 26 Rom II. Pruefraster fuer Rechtswahl und gewoehnlichen Aufenthalt.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster Rom I (vertragliche Schuldverhaeltnisse)

### 1. Anwendungsbereich Art. 1 Rom I

- Vertragliche Schuldverhaeltnisse in Zivil- und Handelssachen mit Auslandsbezug; Ausnahmen Art. 1 II (z. B. Status, Familienrecht, Schiedsvereinbarung).
- Universelle Anwendung Art. 2 — gilt auch ohne Bezug zu EU-Recht.

### 2. Rechtswahl Art. 3 Rom I

- Ausdrueckliche oder konkludente Rechtswahl moeglich, fuer Gesamtvertrag oder Teile (depecage Art. 3 I 3).
- Aenderung der Rechtswahl Art. 3 II.
- Schutz vor reinen Binnensachverhalten Art. 3 III (zwingende Vorschriften des Sachstaats bleiben anwendbar).
- Innergemeinschaftlicher Sachverhalt + Wahl drittstaatlichen Rechts: zwingendes Unionsrecht (Art. 3 IV).

### 3. Mangels Rechtswahl Art. 4 Rom I

- Acht typisierte Vertraege Art. 4 I (Kauf -> Verkaeufer; Dienstleistung -> Dienstleister; Grundstueck -> Lex rei sitae; etc.).
- Wenn nicht typisiert: charakteristische Leistung Art. 4 II.
- Ausweichklausel Art. 4 III (offensichtlich engere Verbindung).

### 4. Sondernormen

- **Befoerderungsvertraege** Art. 5.
- **Verbrauchervertraege** Art. 6: gewoehnlicher Aufenthalt des Verbrauchers, soweit Unternehmer Taetigkeit dorthin ausrichtet; Rechtswahl moeglich, aber zwingender Verbraucherschutz greift weiter.
- **Versicherungsvertraege** Art. 7.
- **Individualarbeitsvertraege** Art. 8: gewoehnlicher Arbeitsort; zwingender AN-Schutz bei Rechtswahl.

### 5. Eingriffsnormen Art. 9 Rom I

- "Overriding mandatory provisions" der lex fori (Art. 9 II) immer anwendbar.
- Eingriffsnormen eines Drittstaates: nur Wirkungsverleihung (Art. 9 III).
- Beispiel DE: § 138 BGB nicht; aber Devisen-, Embargo-, Kartellrecht.

### 6. Ordre public Art. 21 Rom I

- Anwendung auslaendischen Rechts darf "offensichtlich" mit ordre public des Forumstaats unvereinbar nicht sein. Hohe Schwelle.

## Pruefraster Rom II (ausservertragliche Schuldverhaeltnisse)

### 1. Anwendungsbereich Art. 1 Rom II

- Ausservertragliche Schuldverhaeltnisse (unerlaubte Handlung, ungerechtfertigte Bereicherung, GoA, c.i.c. Art. 12).
- Ausnahmen Art. 1 II (Familien-, Erb-, Gesellschafts-, Wertpapierrecht etc.).
- Universelle Anwendung Art. 3.

### 2. Anknuepfung unerlaubter Handlungen Art. 4 Rom II

- **Erfolgsort** (Art. 4 I) — wo Schaden eintritt.
- **Gemeinsamer gewoehnlicher Aufenthalt** (Art. 4 II) — vorrangig.
- **Ausweichklausel** Art. 4 III — offensichtlich engere Verbindung.

### 3. Sondertatbestaende

- **Produkthaftung** Art. 5.
- **Unlauterer Wettbewerb** Art. 6 (Marktortprinzip).
- **Kartelldelikte** Art. 6 III — Marktort.
- **Umweltschaedigung** Art. 7 — Wahlrecht Geschaedigter.
- **IP-Verletzung** Art. 8 (Schutzlandprinzip).
- **Streikfolgen** Art. 9.
- **C.i.c.** Art. 12.

### 4. Rechtswahl Art. 14 Rom II

- Grundsaetzlich nach Schadenseintritt; bei kommerzieller Taetigkeit auch vorher.
- Verbraucher- und AN-Schutz bleiben.

## Pruefraster fuer den Skill

1. **Sachverhalt fixieren** — Wer, was, wo, welcher Auslandsbezug?
2. **Anwendbarkeit Rom I/II** pruefen.
3. **Rechtswahl** existiert? Wenn ja: Wirksamkeit pruefen.
4. **Objektive Anknuepfung** als Fallback.
5. **Eingriffsnormen** der lex fori pruefen.
6. **Ordre public** als letztes Sieb.

## Praxisfallen

- **Rom I gilt nicht** fuer Schiedsvereinbarungen (Art. 1 II lit. e Rom I); IPR der Schiedsvereinbarung folgt eigenen Regeln (NYÜ Art. V).
- **Brexit**: UK seit 1.1.2021 nicht mehr an Rom I/II gebunden; UK hat aber Rom I/II in nationales Recht uebernommen (Retained EU Law).
- **Vertragsstatut vs. Geschaeftsfaehigkeit**: Vertragsstatut nur fuer Vertragsinhalt; Geschaeftsfaehigkeit nach Personalstatut.
- **Form** Art. 11 Rom I: alternative Anknuepfung; Vertragsstatut oder Ortsrecht.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `fachanwalt-internationales-wirtschaftsrecht`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
