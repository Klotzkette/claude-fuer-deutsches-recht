---
name: pralr-schuldrecht-vertrag-deliktsrecht
description: "Schuldrecht Vertrag Deliktsrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schuldrecht Vertrag Deliktsrecht

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Schuldrecht Vertrag Deliktsrecht** im Plugin Preußisches Allgemeines Landrecht (PrALR). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pralr-015-schuldrecht-vertrag-und-form` | PrALR: Schuldrecht, Vertragsschluss, Formzwang, Schriftlichkeit und historische Verkehrssicherheit analysieren. |
| `pralr-017-deliktsrecht-generalklausel` | PrALR: deliktische Generalklausel, Vorsatz, grobes/mäßiges Versehen, Genugtuung und Schaden strukturieren. |
| `pralr-neu-016-erster-teil-titel-13-miete-pacht-dienstvertrag` | PrALR: Erster Teil Titel 13 Miete Pacht Dienstvertrag mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis. |
| `pralr-spez-aufwendungsersatz-im-vertrag` | Aufwendungsersatz im Vertrag nach ALR. Skill behandelt typische Aufwendungsersatzlagen Auftrag (mandatum) Verwahrung (depositum) Vormundschaft (tutela) sowie das Verhaeltnis zur GoA. Liefert Pruefraster. |
| `pralr-spez-vertragsaufhebung-ruecktritt-wandlung` | Vertragsaufhebung Ruecktritt und Wandlung im ALR. Skill behandelt die Aufhebungsgruende einvernehmlich gesetzlich (Wegfall der Geschaeftsgrundlage Untergang) und die Ruecktrittstradition. Liefert Quellenmatrix. |

## Arbeitsweg

Im Plugin Preußisches Allgemeines Landrecht (PrALR) gilt für **Schuldrecht Vertrag Deliktsrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pralr-015-schuldrecht-vertrag-und-form`

**Fokus:** PrALR: Schuldrecht, Vertragsschluss, Formzwang, Schriftlichkeit und historische Verkehrssicherheit analysieren.

# Vertrag und Form

## Aufgabe

Prüfe Vertragstyp, Form, Beweisfunktion, Schutzfunktion und Abgrenzung zum späteren BGB.

Dieser Skill arbeitet mit dem Allgemeinen Landrecht für die Preußischen Staaten als historischer Normquelle. Er behandelt das PrALR nicht als dekorativen Alttext, sondern als konkrete Quelle mit Ausgabejahr, Textzeugen, Geltungsraum, systematischem Ort und möglicher heutiger Fortwirkung.

## Startfragen

1. Welche Quelle liegt vor: Scan, OCR, PDF, Transkription, Sekundärtext, Urteil oder Aktenvermerk?
2. Welches Jahr, welcher Band, welcher Teil, welcher Titel und welcher Paragraph sind sicher?
3. Geht es um historische Erklärung, heutige Fortwirkung, Dogmengeschichte, Unterricht oder Schriftsatzargument?
4. Welcher Ort und welches Jahr sind für den Sachverhalt maßgeblich?
5. Brauchen wir einen Live-Check, weil heutiges Recht, Landesrecht oder Rechtsprechung betroffen ist?

## Prüfroutine

1. **Textzeuge sichern:** Ausgabe, Druck, Band, Seite/Scan, OCR-Fassung und Fundstelle erfassen.
2. **Systemstelle finden:** Einleitung, Teil, Titel, Paragraph und Nachbarvorschriften bestimmen.
3. **Geltung trennen:** historisch geltendes Recht, subsidiäre Anwendung, lokale Abweichung und heutige Fortwirkung unterscheiden.
4. **Begriffe entschlüsseln:** alte Orthographie, ständische Begriffe und heutige Übersetzung offenlegen.
5. **Anachronismus prüfen:** moderne Kategorien nur als Vergleich verwenden, nicht in den Normtext hineinlesen.
6. **Output bauen:** Quellenmatrix, Kurzvermerk, Gutachtenbaustein, Unterrichtsfolie oder Schriftsatzpassage erstellen.

## Meat on the Bone — Konkreter ALR-Stoff

### Schluesselparagraphen
- **ALR I 5 §§ 1-100**: Vertraege allgemein; Vertragsschluss durch Konsens.
- **ALR I 5 §§ 100-200**: Formerfordernisse; bei hoeheren Werten Schriftform; bei Grundstueckskauf gerichtliche Verlautbarung.
- **ALR I 5 §§ 250-300**: Erfuellung, Verzug, Unmoeglichkeit; Verschuldenstufen dolus, culpa lata, culpa levis, culpa levissima.
- **ALR I 5 §§ 400-500**: Wegfall der Geschaeftsgrundlage (clausula rebus sic stantibus) ansatzweise.

### Subsumtionsbeispiel: Mietzinsausstand 1860
Sachverhalt: Mieter zahlt seit 6 Monaten nicht.
ALR-Loesung: ALR I 21 (Miete) iVm I 5 (allgemein) — Verzug nach Mahnung; Kuendigungsrecht; Anspruch auf rueckstaendigen Mietzins plus Verzugsschaden. Mietzinspfandrecht des Vermieters an eingebrachten Sachen (ALR I 20 § ff. Pfand).

### Subsumtionsbeispiel: Schiffsverlust und Wegfall der Geschaeftsgrundlage 1870
Sachverhalt: Kaufmann verkauft Ware, Schiff sinkt vor Ablieferung.
ALR-Loesung: ALR I 5 §§ — Untergang ohne Verschulden = Befreiung von Leistungspflicht; Gefahrtragung nach Periculum-Regel ALR I 11 §§ 90 ff. (perit res emptori bei beweglichen Sachen ab Uebergabe).

### Heutige Fortwirkung
- BGB §§ 145-157 Vertragsschluss.
- §§ 275, 280-281 BGB Pflichtverletzungen.
- §§ 286-288 BGB Verzug.
- § 313 BGB Stoerung der Geschaeftsgrundlage (BGH-Linie aus ALR-Tradition gespeist).

## Ausgabeformat

- **Kurzbefund:** Was sagt die Quelle sicher?
- **Textzeugenstand:** Welche Fassung wurde benutzt und wo ist sie unsicher?
- **Historische Einordnung:** Systemstelle, Geltungsraum, gesellschaftliche Funktion.
- **Heutiger Anschluss:** Fortwirkung, Gewohnheitsrecht, bloße Dogmengeschichte oder keine heutige Relevanz.
- **Nächster Schritt:** zweite Quelle, Scan-Gegenprobe, aktuelles Landesrecht oder Rechtsprechungsrecherche.

## 2. `pralr-017-deliktsrecht-generalklausel`

**Fokus:** PrALR: deliktische Generalklausel, Vorsatz, grobes/mäßiges Versehen, Genugtuung und Schaden strukturieren.

# Deliktsrecht

## Aufgabe

Lege Verschuldensgrad, Rechtsgut, Schaden, Genugtuung und naturrechtliche Begründung getrennt offen.

Dieser Skill arbeitet mit dem Allgemeinen Landrecht für die Preußischen Staaten als historischer Normquelle. Er behandelt das PrALR nicht als dekorativen Alttext, sondern als konkrete Quelle mit Ausgabejahr, Textzeugen, Geltungsraum, systematischem Ort und möglicher heutiger Fortwirkung.

## Startfragen

1. Welche Quelle liegt vor: Scan, OCR, PDF, Transkription, Sekundärtext, Urteil oder Aktenvermerk?
2. Welches Jahr, welcher Band, welcher Teil, welcher Titel und welcher Paragraph sind sicher?
3. Geht es um historische Erklärung, heutige Fortwirkung, Dogmengeschichte, Unterricht oder Schriftsatzargument?
4. Welcher Ort und welches Jahr sind für den Sachverhalt maßgeblich?
5. Brauchen wir einen Live-Check, weil heutiges Recht, Landesrecht oder Rechtsprechung betroffen ist?

## Prüfroutine

1. **Textzeuge sichern:** Ausgabe, Druck, Band, Seite/Scan, OCR-Fassung und Fundstelle erfassen.
2. **Systemstelle finden:** Einleitung, Teil, Titel, Paragraph und Nachbarvorschriften bestimmen.
3. **Geltung trennen:** historisch geltendes Recht, subsidiäre Anwendung, lokale Abweichung und heutige Fortwirkung unterscheiden.
4. **Begriffe entschlüsseln:** alte Orthographie, ständische Begriffe und heutige Übersetzung offenlegen.
5. **Anachronismus prüfen:** moderne Kategorien nur als Vergleich verwenden, nicht in den Normtext hineinlesen.
6. **Output bauen:** Quellenmatrix, Kurzvermerk, Gutachtenbaustein, Unterrichtsfolie oder Schriftsatzpassage erstellen.

## Meat on the Bone — Konkreter ALR-Stoff

### Schluesselparagraphen
- **ALR I 6 § 1**: "Wer einen anderen ohne Recht und Befugniss vorsetzlich beleidiget, ist zum Ersatze des dadurch entstandenen Schadens verpflichtet."
- **ALR I 6 §§ 8 ff.**: Generelle Fahrlaessigkeitshaftung.
- **ALR I 6 §§ 10-12**: Verschuldensstufen — dolus (Vorsatz), culpa lata (grobe Fahrlaessigkeit), culpa levis (leichte Fahrlaessigkeit), culpa levissima (allergeringste Fahrlaessigkeit).
- **ALR I 6 §§ 50-92**: Sonderdelikte — Beleidigung, Koerperverletzung, Sachbeschaedigung, Tierhalter.
- **ALR I 6 §§ 56-58**: Tierhalterhaftung — Hund, Pferd; Differenzierung Wachhund vs. Hofhund.
- **ALR I 6 §§ 78-92**: Beruehmt sind die kasuistischen Brieftauben- und Pferderegelungen.

### Subsumtionsbeispiel: Hofhund beisst Postboten 1880
Sachverhalt: Postbote von Hofhund gebissen.
ALR-Loesung: ALR I 6 §§ 56-58 — Tierhalterhaftung; bei Wachhund mit deutlichem Warnsignal Haftung gemindert; bei freilaufendem Hund volle Haftung. Schaden umfasst Heilkosten und Verdienstausfall. Heute § 833 BGB Tierhalterhaftung — strenger als ALR.

### Subsumtionsbeispiel: Brieftaubendiebstahl 1850
Sachverhalt: Brieftaube fliegt ins Nachbarschloss; Nachbar faengt sie und behaelt sie.
ALR-Loesung: ALR I 6 § — eigener Tatbestand fuer Brieftauben! Pflicht zur Rueckgabe; Schadenersatz bei verzoegerter Rueckgabe.

### Heutige Fortwirkung
- § 823 Abs. 1 BGB generelle Deliktshaftung — moderner gefasst als ALR.
- § 826 BGB sittenwidrige Schaedigung.
- § 833 BGB Tierhalter.
- Verschuldensstufen in ALR-Tradition: bis heute "grobe Fahrlaessigkeit" als Aufschwellgrad fuer Haftungsschaerfung (z. B. § 309 Nr. 7 BGB, § 277 BGB).

## Ausgabeformat

- **Kurzbefund:** Was sagt die Quelle sicher?
- **Textzeugenstand:** Welche Fassung wurde benutzt und wo ist sie unsicher?
- **Historische Einordnung:** Systemstelle, Geltungsraum, gesellschaftliche Funktion.
- **Heutiger Anschluss:** Fortwirkung, Gewohnheitsrecht, bloße Dogmengeschichte oder keine heutige Relevanz.
- **Nächster Schritt:** zweite Quelle, Scan-Gegenprobe, aktuelles Landesrecht oder Rechtsprechungsrecherche.

## 3. `pralr-neu-016-erster-teil-titel-13-miete-pacht-dienstvertrag`

**Fokus:** PrALR: Erster Teil Titel 13 Miete Pacht Dienstvertrag mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.

# Pralr Erster Teil Titel 13 Miete Pacht Dienstvertrag

## Aufgabe

ALR I 21 (Miete) und I 11 (Pacht/Dienstvertrag) — Gebrauchs- und Dienstleistungsvertraege.

## Wichtige Paragraphen

- **ALR I 21**: Miete (locatio conductio rei).
- **ALR I 11 §§ 350-450**: Pacht (locatio conductio rei mit Fruchtziehung).
- **ALR I 11 §§ 500-600**: Dienstvertrag (locatio conductio operarum) — Lohnarbeit.

## Mietzinspfandrecht

- Vermieter hat stillschweigendes Pfandrecht an eingebrachten Sachen (invecta et illata).

## Kuendigung

- Bestimmte Zeit: mit Ablauf.
- Unbestimmte Zeit: Kuendigung nach Frist (typisch ein Quartal).

## Subsumtionsbeispiel: Mieter zahlt nicht 1860

Mieter X zahlt 6 Monate nicht.
- **ALR I 21**: Mahnung, dann Kuendigung; Pfandrecht an Hausrat.
- **BGB**: § 543 BGB ausserordentliche Kuendigung bei 2 Monatsraten Zahlungsverzug.

## Heutige Fortwirkung

- §§ 535-580a BGB Miete.
- §§ 581-597 BGB Pacht.
- §§ 611-630h BGB Dienstvertrag.
- § 562 BGB Vermieterpfandrecht.

## Pruefraster

1. Welcher Vertragstyp?
2. Kuendigung?
3. Pfandrecht?

## Output

- Mietverhaeltnis-Analyse.
- Kuendigungsschreiben.

## 4. `pralr-spez-aufwendungsersatz-im-vertrag`

**Fokus:** Aufwendungsersatz im Vertrag nach ALR. Skill behandelt typische Aufwendungsersatzlagen Auftrag (mandatum) Verwahrung (depositum) Vormundschaft (tutela) sowie das Verhaeltnis zur GoA. Liefert Pruefraster.

# Pralr Aufwendungsersatz Im Vertrag

## Anwendungsfaelle

### Mandatum
- ALR I 13 — Auftraggeber muss notwendige Aufwendungen des Beauftragten ersetzen.
- Erstreckt sich auch auf eingegangene Verbindlichkeiten.

### Depositum
- Verwahrer hat Anspruch auf Ersatz seiner Aufwendungen.
- ALR I 14 — Verwahrung.

### Tutela (Vormundschaft)
- Vormund kann Aufwendungen aus dem Muendelvermoegen entnehmen.
- ALR II 18.

### Pfandnehmer
- Aufwendungen zur Erhaltung des Pfandes ersatzfaehig.

## Fortwirkung BGB

- § 670 BGB Aufwendungsersatz.
- § 683 BGB GoA.

## Pruefraster

1. Welcher Vertragstyp?
2. Aufwendung "fuer den anderen"?
3. Erforderlich?
4. Ersatzfaehig?

## 5. `pralr-spez-vertragsaufhebung-ruecktritt-wandlung`

**Fokus:** Vertragsaufhebung Ruecktritt und Wandlung im ALR. Skill behandelt die Aufhebungsgruende einvernehmlich gesetzlich (Wegfall der Geschaeftsgrundlage Untergang) und die Ruecktrittstradition. Liefert Quellenmatrix.

# Pralr Vertragsaufhebung Ruecktritt Wandlung

## Aufhebungsgruende

### Einvernehmlich
- ALR I 5 — Aufhebungsvertrag.

### Gesetzlich
- Bei Wegfall der Vertragsgrundlage (clausula rebus sic stantibus).
- Bei Unmoeglichkeit.
- Bei dolus malus.

### Ruecktritt
- Bei vereinbartem Ruecktrittsrecht.
- Bei Verzug.

## Wandlung

- Beim Kauf mit Mangel der Sache (vgl. roemisches Recht aedilizische Aktionen).
- Heute § 437 Nr. 2 BGB Ruecktritt.

## Fortwirkung BGB

- § 313 BGB Stoerung der Geschaeftsgrundlage.
- § 323 BGB Ruecktritt wegen Nichterfuellung.
- §§ 346-354 BGB Ruecktrittsfolgen.

## Pruefraster

1. Welcher Aufhebungsgrund?
2. Rueckabwicklung?
3. Wertersatz?

## Output

- Quellenmatrix.
- Synopse.
