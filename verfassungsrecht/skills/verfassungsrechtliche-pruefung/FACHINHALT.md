---
name: verfassungsrechtliche-pruefung
description: "Für Verfassungsrechtliche Prüfung — Master-Workflow: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix."
---

# Verfassungsrechtliche Prüfung — Master-Workflow

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die für diese verfassungsrechtliche Prüfung einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Verfassungsrechtliche Prüfung — Master-Workflow
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Disclaimer (Schlüsselstelle, mehrfach)

Verfassungsrechtliche Prüfungen sind hochspezialisiert und haben existentielle Folgen für Mandanten und Allgemeinheit. Diese Prüfung ist **kein Ersatz** für anwaltliche Mandatsbearbeitung durch eine verfassungsrechtliche Spezialkanzlei. Bei konkreten Vorhaben (Verfassungsbeschwerde, Stellungnahme, Gutachten) ist eine Spezialkanzlei einzuschalten.

## Quellenpflicht

Vor jeder verfassungsrechtlichen Aussage ist Skill `bverfg-rechtsprechung-recherchieren` aufzurufen. Jede tragende Aussage benötigt einen BVerfG-Pinpoint (Az. + Rn. + URL).

## Prüfungsgegenstand klären

Vor Beginn der Prüfung ist zu klären, was eigentlich geprüft wird:

- **Formelles Gesetz** (Bundes- oder Landesgesetz)
- **Rechtsverordnung** (Prüfung gegen Ermächtigungsnorm und unmittelbar gegen GG)
- **Satzung**
- **Verwaltungsakt** oder sonstige Maßnahme der vollziehenden Gewalt

## Gesamtschema

### A. Formelle Verfassungsmäßigkeit

**Skill aufrufen:** `gesetzgebungskompetenz-pruefen` und `formelle-verfassungsmaessigkeit`.

1. **Zuständigkeit (Gesetzgebungskompetenz)**
 - Art. 70 GG (Grundregel: Länder, soweit GG nicht Bund)
 - Art. 71–72 GG (ausschließliche und konkurrierende Gesetzgebung)
 - Art. 73 GG (Katalog Bund ausschließlich)
 - Art. 74 GG (Katalog konkurrierend) ggf. mit Art. 72 Abs. 2 GG (Erforderlichkeitsklausel) oder Art. 72 Abs. 3 GG (Abweichungsgesetzgebung)
 - Art. 75 GG a.F. (Rahmengesetzgebung) — **seit Föderalismusreform 2006 abgeschafft**
 - Bei Verwaltungskompetenzen: Art. 83 ff. GG

2. **Verfahren (Art. 76–82 GG)**
 - Einbringung (Art. 76 GG)
 - Drei Lesungen im Bundestag (§§ 78–86 GOBT)
 - Beteiligung Bundesrat (Art. 77, 78 GG — Zustimmungs- vs. Einspruchsgesetz)
 - Ausfertigung durch Bundespräsidenten (Art. 82 Abs. 1 S. 1 GG)
 - Verkündung im Bundesgesetzblatt (Art. 82 Abs. 1 S. 1 GG)

3. **Form**
 - Bestimmtheitsgebot (rechtsstaatliches Erfordernis)
 - Zitiergebot (Art. 19 Abs. 1 S. 2 GG bei Grundrechtseinschränkungen)

### B. Materielle Verfassungsmäßigkeit

**Skill aufrufen:** `grundrechtspruefung` und `verhaeltnismaessigkeit`.

Pro betroffenem Grundrecht und pro betroffener Verfassungsnorm separat:

1. **Schutzbereichseröffnung** — persönlich und sachlich
2. **Eingriff** — modern: jede Beeinträchtigung des Schutzbereichs, klassisch: final, unmittelbar, rechtsförmig, mit Befehl/Zwang
3. **Verfassungsrechtliche Rechtfertigung**
 - Schranke (einfacher Gesetzesvorbehalt, qualifizierter Vorbehalt, verfassungsimmanente Schranken bei vorbehaltlosen Grundrechten)
 - Schranken-Schranken (Verhältnismäßigkeit, Wesensgehalt Art. 19 Abs. 2 GG, Zitiergebot Art. 19 Abs. 1 S. 2 GG, allgemeine Geltung Art. 19 Abs. 1 S. 1 GG, Wechselwirkung)
 - **Verhältnismäßigkeit** (Skill `verhaeltnismaessigkeit`): legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit

4. **Sonstige verfassungsrechtliche Bindungen**
 - Bundesstaatsprinzip Art. 20 Abs. 1 GG
 - Demokratieprinzip Art. 20 Abs. 1, 2 GG
 - Rechtsstaatsprinzip Art. 20 Abs. 3 GG (Vertrauensschutz, Rückwirkungsverbot, Bestimmtheit)
 - Sozialstaatsprinzip Art. 20 Abs. 1 GG

### C. Gesamtergebnis

- Wenn formell **und** materiell verfassungsgemäß: Norm/Maßnahme bestätigt.
- Wenn ein Prüfungspunkt scheitert: Norm/Maßnahme verfassungswidrig.
- Bei verfassungskonformer Auslegung: Auslegung formulieren, die Norm und GG vereinbart (Grenzen: Wortlaut und gesetzgeberischer Wille).

## Output-Format

```
VERFASSUNGSRECHTLICHE PRÜFUNG

Prüfungsgegenstand: <Norm / Maßnahme>

A. Formelle Verfassungsmäßigkeit
1. Gesetzgebungskompetenz
 - Einschlägig: Art. ___ GG
 - Ergebnis: [vereinbar / unvereinbar]
 - BVerfG-Pinpoint: ___
2. Verfahren
 - Einbringung Art. 76 GG: ___
 - Drei Lesungen: ___
 - Bundesrat (Art. 77, 78 GG): ___
 - Ausfertigung Art. 82 GG: ___
3. Form
 - Bestimmtheit: ___
 - Zitiergebot Art. 19 Abs. 1 S. 2 GG: ___

B. Materielle Verfassungsmäßigkeit
1. Grundrecht ___
 - Schutzbereich: ___
 - Eingriff: ___
 - Rechtfertigung: Schranke ___ / Schranken-Schranken
 - Verhältnismäßigkeit:
 - Legitimer Zweck: ___
 - Geeignetheit: ___
 - Erforderlichkeit: ___
 - Angemessenheit: ___
 - BVerfG-Pinpoint: ___

C. Gesamtergebnis
[verfassungsgemäß / verfassungswidrig / verfassungskonform auslegbar]

Quellen
- [Liste aller BVerfG-Entscheidungen mit Az., Rn., URL]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Disclaimer-Wiederholung (vor jedem Output)

Diese Prüfung ist eine strukturierte Modellauswertung und **kein Ersatz** für anwaltliche Mandatsbearbeitung. Insbesondere die Beurteilung der Vereinbarkeit konkreter Normen mit dem GG bleibt im Streitfall dem BVerfG vorbehalten (Verwerfungsmonopol Art. 100 GG).

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
