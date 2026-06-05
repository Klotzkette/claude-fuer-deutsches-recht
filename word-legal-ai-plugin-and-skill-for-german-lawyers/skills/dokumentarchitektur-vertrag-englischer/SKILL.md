---
name: dokumentarchitektur-vertrag-englischer
description: "Dokumentarchitektur Vertrag Englischer: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dokumentarchitektur Vertrag Englischer

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Dokumentarchitektur Vertrag Englischer** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dokumentarchitektur-vertrag-und-schriftsatz` | Dokumentarchitektur juristischer Texte sauber bauen. Vertrag mit Rubrum/Parteien, Praeambel, Definitionen, Hauptleistungspflichten, Nebenpflichten, Bedingungen, Beendigung, Boilerplate, Anlagen. Schriftsatz nach § 253 Abs. 2 ZPO mit Rubrum, Antraegen, Sachverhalt, rechtlicher Wuerdigung, Beweisangeboten, Schlussformel, Anlagenverzeichnis. Mit Strukturbaeumen je Dokumenttyp als Tabelle. |
| `englischer-vertrag-deutsches-recht` | Draftet oder prüft englischsprachige Verträge mit deutschem Recht als anwendbarem Recht. Verhindert ungewollten Import von Common-Law-Konzepten, klärt governing language, German-law concepts, Gewährleistung, Garantie, Haftung, Indemnity, Vertragsstrafe, Schriftform, Gerichtsstand und Anlagenlogik. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Dokumentarchitektur Vertrag Englischer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dokumentarchitektur-vertrag-und-schriftsatz`

**Fokus:** Dokumentarchitektur juristischer Texte sauber bauen. Vertrag mit Rubrum/Parteien, Praeambel, Definitionen, Hauptleistungspflichten, Nebenpflichten, Bedingungen, Beendigung, Boilerplate, Anlagen. Schriftsatz nach § 253 Abs. 2 ZPO mit Rubrum, Antraegen, Sachverhalt, rechtlicher Wuerdigung, Beweisangeboten, Schlussformel, Anlagenverzeichnis. Mit Strukturbaeumen je Dokumenttyp als Tabelle.

# Dokumentarchitektur: Vertrag und Schriftsatz

## Zweck

Juristisches Drafting beginnt mit der Architektur, nicht mit dem Klauseltext. Wer einen Vertrag ohne Inhaltsverzeichnis schreibt, baut ein Haus ohne Statik. Dieser Skill liefert die Standardstruktur für die beiden wichtigsten Dokumenttypen: Vertrag und Schriftsatz. Daneben kurz: Memo, Anwaltsschreiben, AGB.

Die Struktur ist Konvention, keine Mode. Gerichte erwarten sie. Geschaeftsleitung erwartet sie. Wer abweicht, soll wissen warum.

Der Skill liefert je Dokument einen Strukturbaum als Tabelle und ein Skelett. Klauseltext entsteht in den Fachmodule.

## Eingaben

- Dokumenttyp und Untertyp (Kaufvertrag, Lieferantenvertrag, Klage, Klageerwiderung, Antrag)
- Komplexitaetsgrad (einfach, mittel, M&A-Niveau)
- Parteien und Rollen
- Vorliegende Vorentwuerfe oder Term Sheet

## Rechtlicher und methodischer Rahmen

- § 253 Abs. 2 ZPO: Pflichtbestandteile der Klageschrift.
- § 130 ZPO: Allgemeiner Schriftsatz-Inhalt.
- § 311b BGB: Beurkundungspflicht fuer bestimmte Vertraege (Grundstueck, GmbH-Geschaeftsanteile).
- § 126 BGB, § 126a BGB, § 126b BGB: Schriftform, elektronische Form, Textform.
- § 305 Abs. 1 BGB: AGB-Begriff. Vertraege mit AGB-Anteil brauchen zusaetzliche Strukturelemente.

## Ablauf / Checkliste

1. **Dokumenttyp wahlen.** Vertrag, Klage, Klageerwiderung, AGB, Memo, Anwaltsschreiben.
2. **Standardstruktur waehlen.** Siehe Tabellen unten.
3. **Anpassen.** Streichen Sie nicht benoetigte Bloecke, ergaenzen Sie Sonderkapitel.
4. **Nummerierung festlegen.** § (Paragraph) oder Ziffer. M&A-Vertraege ueblich mit Ziffern, BGB-Vertraege ueblich mit Paragraphen.
5. **Inhaltsverzeichnis und Gliederung pragmatisch prüfen.** Bei längeren Dokumenten eine lesbare Übersicht vorsehen; technische Word-Automatisierung ist nicht Gegenstand dieses Skills.
6. **Querverweise vorbereiten.** Siehe `verweis-und-querverweis-technik`.

### Strukturbaum Vertrag (Standardfall)

| Block | Inhalt | Optional |
|---|---|---|
| Rubrum | Bezeichnung der Parteien mit Anschrift, ggf. Handelsregister, Vertretung | nein |
| Praeambel | Hintergrund, Anlass, Zweck. Auch "Whereas-Klauseln" | im Standardvertrag entbehrlich, im M&A ueblich |
| Definitionen | alphabetisch oder thematisch gegliedert | bei kurzem Vertrag inline |
| Vertragsgegenstand | Hauptleistungspflicht in einer Klausel | nein |
| Hauptleistungspflichten | Pflichten der Parteien im Detail | nein |
| Nebenpflichten | Mitwirkung, Information, Schutz | je nach Vertragstyp |
| Verguetung | Hoehe, Faelligkeit, Zahlweise, Verzug | nein, wenn entgeltlich |
| Maengelhaftung | Pflichten bei Mangel, Fristen, Rechte | je nach Vertragstyp |
| Haftung | Begrenzung, Ausschluss, Versicherung | siehe `haftungsausschluss-und-haftungsbegrenzung` |
| Geheimhaltung | NDA-Baustein oder Verweis auf NDA | je nach Mandat |
| Laufzeit und Beendigung | Erstlaufzeit, Verlaengerung, ordentliche und ausserordentliche Kuendigung | nein |
| Boilerplate | Schriftform, Salvatorisch, Gerichtsstand, Rechtswahl, Erfuellungsort | siehe `boilerplate-klauseln-katalog` |
| Unterschriften | Ort, Datum, Unterzeichner mit Funktion | nein |
| Anlagen | Anlagenverzeichnis, durchnummeriert | wenn vorhanden |

### Strukturbaum Klageschrift (§ 253 Abs. 2 ZPO)

| Block | Inhalt | Quelle |
|---|---|---|
| Rubrum | Gericht, Parteien mit gesetzlicher Vertretung, Aktenzeichen | § 253 Abs. 2 Nr. 1 ZPO |
| Antraege | bestimmte Antraege | § 253 Abs. 2 Nr. 2 ZPO |
| Sachverhalt | Tatsachenvortrag, chronologisch oder thematisch | § 253 Abs. 2 Nr. 2 ZPO |
| Rechtliche Wuerdigung | Anspruchsgrundlagen in der Reihenfolge Vertrag, c.i.c., GoA, dinglich, Delikt, Bereicherung | freie Gliederung |
| Beweisangebote | Zeugen, Urkunden, Sachverstaendige, Augenschein | § 130 Nr. 5 ZPO |
| Streitwert | Vorschlag fuer Streitwertfestsetzung | § 61 GKG |
| Schlussformel | Unterschrift des Rechtsanwalts | § 130 Nr. 6 ZPO |
| Anlagenverzeichnis | K1, K2 usw. | freie Konvention |

### Strukturbaum Klageerwiderung

| Block | Inhalt |
|---|---|
| Rubrum | wie Klage, mit Aktenzeichen |
| Antraege | Klageabweisung, ggf. Widerklage |
| Bestreiten | substantiiertes Bestreiten der Klagebehauptungen |
| Eigener Sachverhalt | abweichende Darstellung |
| Rechtliche Wuerdigung | Einwendungen, Einreden |
| Beweisangebote | wie Klage |
| Schlussformel | Unterschrift |

### Strukturbaum Memo (Standardstruktur Repository)

1. Sachverhalt
2. Frage(n)
3. Kurzantwort
4. Rechtliche Bewertung
5. Gesamtergebnis
6. Risiken / offene Punkte
7. Quellenverzeichnis

## Typische Drafting-Fehler

- **Definitionen nach hinten.** Defined Terms gehoeren nach vorne, nicht in den Anhang.
- **Praeambel als Vertrag.** Praeambel ist Auslegungshilfe, nicht Pflicht. Klauseln nicht in Praeambel-Saetze verstecken.
- **Boilerplate vergessen.** Salvatorisch, Schriftform, Gerichtsstand sind Pflicht im B2B-Vertrag.
- **Antraege unbestimmt.** § 253 Abs. 2 Nr. 2 ZPO. Unbestimmter Antrag ist unzulaessig.
- **Sachverhalt vermischt mit Rechtsmeinung.** Sachverhalt ist Faktentafel, kein Schlagabtausch.
- **Anlagen ohne Verzeichnis.** Anlage K7 ohne Verzeichnis ist im Prozess nicht auffindbar.

## Ausgabeformat

- Strukturbaum als Tabelle.
- Skelett-Dokument mit Ueberschriften und Platzhaltern in eckigen Klammern.
- Hinweis auf einschlaegige Fachmodule je Block.

## Beispiel

**Skelett Liefer- und Werkvertrag (mittlere Komplexitaet):**

```
RUBRUM
zwischen [Verkaeufer GmbH, Anschrift, HRB] (Lieferant)
und [Besteller AG, Anschrift, HRB] (Besteller)

§ 1 Definitionen
§ 2 Vertragsgegenstand
§ 3 Lieferung und Abnahme
§ 4 Verguetung und Zahlung
§ 5 Eigentumsvorbehalt
§ 6 Maengelhaftung
§ 7 Haftung
§ 8 Geheimhaltung
§ 9 Laufzeit und Kuendigung
§ 10 Schriftform und Aenderungen
§ 11 Salvatorische Klausel
§ 12 Gerichtsstand und Rechtswahl
§ 13 Anlagen

Anlage 1: Leistungsbeschreibung
Anlage 2: Preisliste
Anlage 3: Lieferplan
```

## Querverweise

- `definitionen-klauseln-stringent`
- `boilerplate-klauseln-katalog`
- `haftungsausschluss-und-haftungsbegrenzung`
- `verweis-und-querverweis-technik`
- `klage-drafting-253-zpo`
- `gutachten-memo-internes-drafting`

## Quellen (Stand 05/2026)

- § 253 Abs. 2 ZPO; § 130 ZPO; gesetze-im-internet.de.
- § 311b BGB; § 126 BGB; § 126a BGB; § 126b BGB; § 305 Abs. 1 BGB.
- Memo-Struktur: CLAUDE.md im Repository-Wurzelverzeichnis.
- Vertragsstruktur folgt der Konvention deutscher Wirtschaftskanzleien. Konkrete Klauselmuster vom Nutzer mit aktueller Literatur zu validieren.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `englischer-vertrag-deutsches-recht`

**Fokus:** Draftet oder prüft englischsprachige Verträge mit deutschem Recht als anwendbarem Recht. Verhindert ungewollten Import von Common-Law-Konzepten, klärt governing language, German-law concepts, Gewährleistung, Garantie, Haftung, Indemnity, Vertragsstrafe, Schriftform, Gerichtsstand und Anlagenlogik.

# Englischer Vertrag nach Deutschem Recht

## Zweck

Ein englischer Vertrag mit deutschem Recht ist kein Common-Law-Vertrag mit deutschem Gerichtsstand. Dieser Skill hilft, englische Vertragssprache so zu verwenden, dass sie deutsches Recht trägt, statt versehentlich fremde Institute zu importieren.

## Kernfragen

1. Ist der Vertrag vollständig auf Englisch oder bilingual?
2. Gilt deutsches Recht wirklich?
3. Soll ein deutsches Gericht, ein Schiedsgericht oder ein ausländisches Forum entscheiden?
4. Sind Begriffe wie indemnity, warranty, representation, best efforts, liquidated damages und penalty funktional definiert?
5. Gibt es deutsche AGB-Kontrolle?
6. Ist die Vertragssprache zugleich Verhandlungssprache oder nur Mandantenkomfort?

## Begriffskontrolle

| Begriff | Risiko bei deutschem Recht | Empfehlung |
|---|---|---|
| representation | kann als Garantie oder Wissenserklärung missverstanden werden | definieren, ob selbstständige Garantie gemeint ist |
| warranty | nicht schlicht Gewährleistung | bei deutschem Recht als contractual guarantee oder Beschaffenheitsvereinbarung strukturieren |
| indemnity | weiter als Schadensersatz | als Freistellung mit Auslöser, Umfang und Verfahren formulieren |
| best efforts | unklarer Maßstab | konkreten Handlungsmaßstab definieren |
| liquidated damages | Nähe zu pauschaliertem Schadensersatz | AGB-Risiko und Gegenbeweisöffnung prüfen |
| penalty | im Common Law kritisch, im deutschen Recht Vertragsstrafe möglich | bewusst als contractual penalty unter deutschem Recht formulieren |
| entire agreement | kollidiert praktisch mit Individualabrede-Vorrang | § 305b BGB mitdenken |

## Ablauf

1. Governing Law und Forum prüfen.
2. Sprach- und Auslegungsklausel festlegen.
3. Deutsche Rechtsinstitute identifizieren.
4. Common-Law-Begriffe entweder vermeiden oder definieren.
5. Haftung, Freistellung, Gewährleistung und Garantien separat strukturieren.
6. AGB-Risiko prüfen.
7. Word- und Anlagenlogik prüfen.

## Output

- Klauselvorschläge auf Englisch.
- Deutsche Kontrollnotiz mit rechtlicher Funktion.
- Red-Flag-Liste für importierte Common-Law-Begriffe.
- Empfehlung für Folge-Skills: `bilingual-drafting-deutsch-englisch`, `haftungsausschluss-und-haftungsbegrenzung`, `agb-konforme-klauseln-305-310-bgb`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
