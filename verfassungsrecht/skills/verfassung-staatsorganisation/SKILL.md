---
name: verfassung-staatsorganisation
description: "Verfassung Staatsorganisation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verfassung Staatsorganisation

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verfassung Staatsorganisation** im Plugin Verfassungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verfassung-staatsorganisation` | Staatsorganisation des GG: Demokratieprinzip Art. 20, Rechtsstaatsprinzip, Bundesstaatsprinzip, Sozialstaatsprinzip, Republikprinzip. Bundesorgane: BT, BR, BReg, BPraes, BVerfG. Pruefraster Staatsfunktionen. |
| `verfassungsrechtliche-pruefung` | Verfassungsrechtliche Prüfung einer Massnahme oder Norm umfassend durchführen. Art. 1-20 GG Grundrechte Staatsorganisationsrecht. Prüfraster: formelle Verfassungsmäßigkeit Grundrechtsprüfung Staatsstrukturprinzipien Verhältnismäßigkeit EU-Recht. Output: umfassendes Verfassungsprüfmemo. Abgrenzung: Oberbegriff-Skill; Detailarbeit in Spezialist-Skills wie grundrechtsprüfung oder formelle-verfassungsmäßigkeit. |
| `verhaeltnismaessigkeit` | Verhältnismäßigkeitsprüfung für staatliche Massnahmen oder Gesetze durchführen. Art. 20 Abs. 3 GG Rechtsstaatsprinzip BVerfG-Stufenschema. Prüfraster: legitimer Zweck Geeignetheit Erforderlichkeit Angemessenheit Dreistufenprüfung Abwaegung. Output: Verhältnismäßigkeitsprüfschema Ergebnis Argumentationshilfe. Abgrenzung: nicht für Grundrechtsprüfung insgesamt (grundrechtsprüfung) sondern Baustein. |

## Arbeitsweg

Im Plugin Verfassungsrecht gilt für **Verfassung Staatsorganisation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verfassung-staatsorganisation`

**Fokus:** Staatsorganisation des GG: Demokratieprinzip Art. 20, Rechtsstaatsprinzip, Bundesstaatsprinzip, Sozialstaatsprinzip, Republikprinzip. Bundesorgane: BT, BR, BReg, BPraes, BVerfG. Pruefraster Staatsfunktionen.

# Staatsorganisation GG

## Fachkern: Staatsorganisation GG
- **Spezialgegenstand:** Staatsorganisation GG wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
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

## 2. `verfassungsrechtliche-pruefung`

**Fokus:** Verfassungsrechtliche Prüfung einer Massnahme oder Norm umfassend durchführen. Art. 1-20 GG Grundrechte Staatsorganisationsrecht. Prüfraster: formelle Verfassungsmäßigkeit Grundrechtsprüfung Staatsstrukturprinzipien Verhältnismäßigkeit EU-Recht. Output: umfassendes Verfassungsprüfmemo. Abgrenzung: Oberbegriff-Skill; Detailarbeit in Spezialist-Skills wie grundrechtsprüfung oder formelle-verfassungsmäßigkeit.

# Verfassungsrechtliche Prüfung — Master-Workflow

## Fachkern: Verfassungsrechtliche Prüfung — Master-Workflow
- **Spezialgegenstand:** Verfassungsrechtliche Prüfung — Master-wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

## Disclaimer-Wiederholung (vor jedem Output)

Diese Prüfung ist eine strukturierte Modellauswertung und **kein Ersatz** für anwaltliche Mandatsbearbeitung. Insbesondere die Beurteilung der Vereinbarkeit konkreter Normen mit dem GG bleibt im Streitfall dem BVerfG vorbehalten (Verwerfungsmonopol Art. 100 GG).

## 3. `verhaeltnismaessigkeit`

**Fokus:** Verhältnismäßigkeitsprüfung für staatliche Massnahmen oder Gesetze durchführen. Art. 20 Abs. 3 GG Rechtsstaatsprinzip BVerfG-Stufenschema. Prüfraster: legitimer Zweck Geeignetheit Erforderlichkeit Angemessenheit Dreistufenprüfung Abwaegung. Output: Verhältnismäßigkeitsprüfschema Ergebnis Argumentationshilfe. Abgrenzung: nicht für Grundrechtsprüfung insgesamt (grundrechtsprüfung) sondern Baustein.

# Verhältnismäßigkeit (Vier-Stufen-Prüfung)

## Fachkern: Verhältnismäßigkeit (Vier-Stufen-Prüfung)
- **Spezialgegenstand:** Verhältnismäßigkeit (Vier-Stufen-Prüfung) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Disclaimer

Verhältnismäßigkeitsprüfungen sind regelmäßig der Kern jeder Grundrechtsprüfung und im Streitfall nur durch das BVerfG verbindlich entscheidbar. Diese Prüfung ist eine Unterstützung, **kein Ersatz** für anwaltliche Beratung.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst. Pinpoint pro tragender Aussage.

## Grundsätzliches

- Die Verhältnismäßigkeit ist die **wichtigste Schranken-Schranke**.
- Sie wurzelt im **Rechtsstaatsprinzip** (Art. 20 Abs. 3 GG) und im Wesen der Grundrechte selbst.
- **Stufenverhältnis:** Die vier Prüfungspunkte stehen in einem Stufenverhältnis. Wird ein Punkt verneint, ist die Prüfung beendet — der Eingriff ist unverhältnismäßig.

## Die vier Stufen

### Stufe 1 — Legitimer Zweck

**Frage:** Verfolgt der Eingriff einen verfassungsrechtlich nicht missbilligten Zweck?

- Bei einfachem Gesetzesvorbehalt: jeder Zweck, der das Grundgesetz nicht verbietet.
- Bei qualifiziertem Vorbehalt: nur Zwecke, die der qualifizierte Vorbehalt erlaubt (z. B. "Schutz der Jugend" und "Schutz der persönlichen Ehre" bei Art. 5 Abs. 2 GG).
- Bei vorbehaltlosem Grundrecht: nur **kollidierendes Verfassungsrecht** (verfassungsimmanente Schranken).
- **Wichtig:** Nicht der subjektive, sondern der **objektive** Zweck der Norm zählt.

**Häufige Fehler:** Zweck als bloße Wiederholung des Eingriffs ("Verbot von X zum Zweck, X zu verbieten") — das ist kein legitimer Zweck.

### Stufe 2 — Geeignetheit

**Frage:** Ist das Mittel zur Erreichung des Zwecks geeignet?

- **Maßstab:** Das Mittel muss den Zweck **fördern können** (nicht: vollständig erreichen).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Eingeschränkter Maßstab: **Evident ungeeignet** bedeutet verfassungswidrig.

### Stufe 3 — Erforderlichkeit

**Frage:** Gibt es kein milderes, gleich wirksames Mittel?

- **Maßstab:** ein anderes Mittel muss
 - die Grundrechte des Betroffenen **weniger intensiv** einschränken **und**
 - den Zweck **gleich wirksam** erreichen.
- Strikter Maßstab — Einschätzungsspielraum des Gesetzgebers ist hier geringer als bei Geeignetheit.
- Häufiger Knackpunkt: Sind Selbstregulierung, Aufklärungspflichten, Erlaubnisvorbehalt mit Auflagen, mildere Sanktion etc. gleich wirksam wie das gewählte Mittel?

### Stufe 4 — Angemessenheit (Verhältnismäßigkeit im engeren Sinne)

**Frage:** Steht der Eingriff in angemessenem Verhältnis zum verfolgten Zweck?

**Gesamtabwägung** zwischen:

- Schwere des Eingriffs (Tiefe, Breite, Dauer, Reversibilität)
- Gewicht der durch den Eingriff geschützten Belange
- Wahrscheinlichkeit des Schadenseintritts ohne den Eingriff
- Eingriffsintensität auf Grundrechtsseite

**Indikatoren für hohe Eingriffsintensität** (Verschärfung der Anforderungen):

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Heimliche Eingriffe ohne Kenntnis des Betroffenen
- Streubreite (viele Unbeteiligte betroffen)
- Lange Dauer / Dauerwirkung
- Irreversibilität
- Doppelte oder kumulative Belastung

**Indikatoren für hohes Gewicht des Zwecks:**

- Schutz überragend wichtiger Gemeinschaftsgüter (Leben, Gesundheit, äußere und innere Sicherheit)
- Hohe Wahrscheinlichkeit schwerer Schäden bei Untätigkeit

### Praktische Konkordanz (bei vorbehaltlosen Grundrechten)

Bei Eingriff in ein vorbehaltlos gewährtes Grundrecht und kollidierendem Verfassungsrecht:

- **Praktische Konkordanz** als Methode der Abwägung: Beide Rechtsgüter sind so zu balancieren, dass jedes größtmögliche Wirksamkeit entfaltet.
- Kein vorrangiges Verfassungsgut. Es gibt keine Hierarchie zwischen Grundrechten.

## Spezielle Fallgruppen

### Klimaschutz und intertemporale Freiheitssicherung

BVerfG, Beschl. v. 24.03.2021 — 1 BvR 2656/18 u. a. (Klimabeschluss) — Schutzauftrag aus Art. 20a GG; eingriffsähnliche Vorwirkung gegenwärtiger Untätigkeit auf künftige Freiheitsräume; Maßstab der intertemporalen Freiheitssicherung — [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2021/03/rs20210324_1bvr265618.html). EGMR-Linie ergänzend: KlimaSeniorinnen gegen Schweiz, Urt. v. 09.04.2024 — Bf-Nr. 53600/20 (Verletzung Art. 8 EMRK durch unzureichende Klimamaßnahmen) — [hudoc.echr.coe.int](https://hudoc.echr.coe.int).

### Triage

Rechtsprechung zur "Triage" (Pandemie-Priorisierung) live über [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) verifizieren — keine Aktenzeichen aus Modellwissen. Methodisch zentral: Verhältnismäßigkeit von Schutzpflichten aus Art. 3 Abs. 3 S. 2 GG (Verbot der Benachteiligung wegen Behinderung) und Art. 2 Abs. 2 S. 1 GG.

### Online-Durchsuchung / IT-Grundrecht / Quellen-TKÜ

- BVerfG, Beschl. v. 07.08.2025 — 1 BvR 2466/19 (Trojaner I) — präventiv-polizeirechtliche Quellen-TKÜ und Online-Durchsuchung nach PolG NRW im Wesentlichen verfassungskonform — vor Ausgabe live verifizieren.
- BVerfG, Beschl. v. 07.08.2025 — 1 BvR 180/23 (Trojaner II) — strafprozessuale Quellen-TKÜ für Niedrig-Strafrahmen teilweise nichtig.
- BVerfG, Beschl. v. 14.11.2024 — 1 BvL 3/22 (PolG NRW Observation) — Eingriffsschwelle für längerfristige Observation mit Bildaufnahmen.

## Output-Format

```
VERHÄLTNISMÄSSIGKEITSPRÜFUNG

Eingriff: ___
Betroffenes Grundrecht: Art. ___ GG

1. Legitimer Zweck
 - Verfolgter Zweck: ___
 - Verfassungsrechtlich nicht missbilligt: [ja / nein]
 - BVerfG-Pinpoint: ___

2. Geeignetheit
 - Zweckförderung: ___
 - Einschätzungsspielraum: ___
 - Ergebnis: [geeignet / evident ungeeignet]

3. Erforderlichkeit
 - Mildere Mittel geprüft: ___
 - Gleich wirksam: [ja / nein]
 - Ergebnis: [erforderlich / nicht erforderlich]

4. Angemessenheit
 - Eingriffstiefe: ___
 - Geschützte Belange: ___
 - Abwägung: ___
 - BVerfG-Pinpoint: ___
 - Ergebnis: [angemessen / unangemessen]

Gesamtergebnis: [verhältnismäßig / unverhältnismäßig auf Stufe ___]
```

## Disclaimer-Wiederholung

Die Verhältnismäßigkeitsabwägung ist im konkreten Einzelfall hochsensibel und wird im Streitfall verbindlich nur durch das BVerfG entschieden.
