---
name: verfassung-grundgesetz-organstreitverfahren
description: "Verfassung Grundgesetz Organstreitverfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verfassung Grundgesetz Organstreitverfahren

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verfassung Grundgesetz Organstreitverfahren** im Plugin Verfassungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verfassung-grundgesetz-verfahren` | Verfahren der Verfassungsaenderung Art. 79 GG: Zwei-Drittel-Mehrheit BT und BR, Ewigkeitsklausel Art. 79 Abs. 3 GG. Beispiele unzulaessiger Aenderungen. |
| `verfassung-organstreitverfahren` | Organstreitverfahren Art. 93 Abs. 1 Nr. 1 GG, § 13 Nr. 5, §§ 63 ff. BVerfGG: Antragsteller (Verfassungsorgane, mit eigenen Rechten ausgestattete Teile), Antragsgegenstand Massnahme Verfassungsorgan, Frist 6 Monate. Pruefraster. |
| `gesetzentwurf-gg-konformitaet-pruefen` | Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzipien Art. 70-80 GG Gesetzgebung. Prüfraster: formelle Verfassungsmäßigkeit Grundrechte Art. 20 GG Rechtsstaatsprinzip Verhältnismäßigkeit EU-Recht-Konformität. Output: Verfassungsprüfmemo Risikobewertung. Abgrenzung: nicht für laufende Normenkontrolle (normenkontrolle ist separates Plugin). |

## Arbeitsweg

Im Plugin Verfassungsrecht gilt für **Verfassung Grundgesetz Organstreitverfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verfassung-grundgesetz-verfahren`

**Fokus:** Verfahren der Verfassungsaenderung Art. 79 GG: Zwei-Drittel-Mehrheit BT und BR, Ewigkeitsklausel Art. 79 Abs. 3 GG. Beispiele unzulaessiger Aenderungen.

# GG-Aenderung Art. 79 GG

## Fachkern: GG-Aenderung Art. 79 GG
- **Spezialgegenstand:** GG-Aenderung Art. 79 GG wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
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

## 2. `verfassung-organstreitverfahren`

**Fokus:** Organstreitverfahren Art. 93 Abs. 1 Nr. 1 GG, § 13 Nr. 5, §§ 63 ff. BVerfGG: Antragsteller (Verfassungsorgane, mit eigenen Rechten ausgestattete Teile), Antragsgegenstand Massnahme Verfassungsorgan, Frist 6 Monate. Pruefraster.

# Organstreitverfahren

## Fachkern: Organstreitverfahren
- **Spezialgegenstand:** Organstreitverfahren wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
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

## 3. `gesetzentwurf-gg-konformitaet-pruefen`

**Fokus:** Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzipien Art. 70-80 GG Gesetzgebung. Prüfraster: formelle Verfassungsmäßigkeit Grundrechte Art. 20 GG Rechtsstaatsprinzip Verhältnismäßigkeit EU-Recht-Konformität. Output: Verfassungsprüfmemo Risikobewertung. Abgrenzung: nicht für laufende Normenkontrolle (normenkontrolle ist separates Plugin).

# Gesetzentwurf — GG-Konformität prüfen (Gesetzgebersicht)

## Fachkern: Gesetzentwurf — GG-Konformität prüfen (Gesetzgebersicht)
- **Spezialgegenstand:** Gesetzentwurf — GG-Konformität prüfen (Gesetzgebersicht) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Disclaimer

Diese Prüfung dient der Gesetzgebungsvorbereitung in Ministerien und Regierungsstellen. Die verbindliche Klärung der Verfassungsmäßigkeit eines Gesetzes erfolgt im Streitfall ausschließlich durch das BVerfG (Art. 100 GG; Art. 93 Abs. 1 Nr. 2, 2a GG). Diese Prüfung ist eine Unterstützung und **kein Ersatz** für externe gutachterliche Beratung durch eine verfassungsrechtliche Spezialkanzlei.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst. Jede Aussage benötigt BVerfG-Pinpoint.

## Workflow

### Schritt 1 — Regelungsziel und Mittel bestimmen

- **Regelungsziel:** welcher Zustand soll erreicht / welche Gefahr abgewehrt werden?
- **Regelungsmittel:** welche Normen sollen erlassen werden?
- **Adressatenkreis:** wer wird betroffen?
- **Bestehende Regelungslage:** was gibt es bereits?

### Schritt 2 — Gesetzgebungskompetenz (Aufruf Skill `gesetzgebungskompetenz-pruefen`)

- Materiebestimmung (Schwerpunkt)
- Art. 70–74 GG durchgehen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bei Abweichungsgesetzgebung Art. 72 Abs. 3 GG: Verhältnis Bund/Land klären.

### Schritt 3 — Formelle Verfassungsmäßigkeit (Aufruf Skill `formelle-verfassungsmaessigkeit`)

- Verfahren Art. 76–82 GG planen.
- **Zustimmungs- oder Einspruchsgesetz?** Prüfung früh, da Mehrheitsverhältnisse im Bundesrat berücksichtigt werden müssen.
- **Bestimmtheit:** Tatbestandsmerkmale, Rechtsfolgen, Zuständigkeiten klar regeln. Generalklauseln vermeiden, soweit Grundrechtsrelevanz hoch.
- **Zitiergebot Art. 19 Abs. 1 S. 2 GG:** Falls ein Grundrecht eingeschränkt wird, im Eingangsabschnitt das eingeschränkte Grundrecht unter Angabe des Artikels nennen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Schritt 4 — Materielle Verfassungsmäßigkeit pro betroffenes Grundrecht

Für jedes betroffene Grundrecht (Aufruf Skill `grundrechtspruefung`):

- Schutzbereich identifizieren.
- Eingriff bestimmen — auch mittelbare und faktische Eingriffe einbeziehen.
- Schranke benennen.
- **Schranken-Schranken** prüfen:
 - **Verhältnismäßigkeit** (Aufruf Skill `verhaeltnismaessigkeit`) — vier Stufen.
 - Wesensgehalt Art. 19 Abs. 2 GG.
 - Zitiergebot.
 - Allgemeinheit Art. 19 Abs. 1 S. 1 GG.
 - Wechselwirkungslehre bei Art. 5 Abs. 2 GG.
- Spezielle Strukturen einzelner Grundrechte berücksichtigen (Drei-Stufen-Theorie bei Art. 12 GG, Eingriffsformen bei Art. 14 GG, usw.).

### Schritt 5 — Sonstige verfassungsrechtliche Bindungen

#### 5a. Rechtsstaatsprinzip (Art. 20 Abs. 3 GG)

- **Bestimmtheitsgebot** (s. Schritt 3).
- **Vertrauensschutz und Rückwirkungsverbot:**
 - **Echte Rückwirkung** (Rückbewirkung von Rechtsfolgen) — grundsätzlich unzulässig.
 - **Unechte Rückwirkung** (tatbestandliche Rückanknüpfung) — zulässig, soweit Vertrauensschutz nicht überwiegt.
- **Faires Verfahren.**

#### 5b. Demokratieprinzip (Art. 20 Abs. 1, 2 GG)

- Lückenlose demokratische Legitimationskette für hoheitliches Handeln.
- Parlamentsvorbehalt (s. Wesentlichkeit).

#### 5c. Sozialstaatsprinzip (Art. 20 Abs. 1 GG)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Gleichmäßige Lastenverteilung.

#### 5d. Bundesstaatsprinzip (Art. 20 Abs. 1 GG)

- Beachtung der Länderkompetenzen.
- Bundestreue / Verfassungstreue.

#### 5e. Europarechtsfreundlichkeit

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mit Unionsrecht vereinbar? Verstoß gegen Grundrechtecharta?

### Schritt 6 — Begründung des Entwurfs

Die Gesetzesbegründung sollte folgende Punkte zur Verfassungsmäßigkeit explizit ausführen:

1. **Gesetzgebungskompetenz** — einschlägige Norm benennen; bei Art. 72 Abs. 2 GG: Erforderlichkeit substantiiert dartun.
2. **Eingeschränkte Grundrechte** — explizit benennen, Zitiergebot wahren.
3. **Verhältnismäßigkeit** — Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit pro Grundrecht durchargumentieren.
4. **Bezugnahme auf einschlägige BVerfG-Rechtsprechung** — Pinpoint mit Az. + Rn. + URL.
5. **Alternativen** — geprüfte mildere Mittel und Gründe für ihre Ablehnung.
6. **Folgenabschätzung** — auch zur Wahrung der Verhältnismäßigkeit.

### Schritt 7 — Risikoeinschätzung

- **Klassifikation:**
 - **Niedrig** — keine erkennbaren verfassungsrechtlichen Bedenken.
 - **Mittel** — auslegungsbedürftige Streitfragen; Stellungnahme aus Wissenschaft, Rechtsausschuss erwartbar.
 - **Hoch** — substantielle Bedenken; abstrakte Normenkontrolle oder Verfassungsbeschwerde wahrscheinlich.

- **Empfehlung bei mittlerem/hohem Risiko:** externe verfassungsrechtliche Begutachtung; Anpassungen am Entwurf, um Risiko zu reduzieren.

## Output-Format

```
GG-KONFORMITÄT GESETZENTWURF

Entwurf: ___
Regelungsziel: ___

1. Gesetzgebungskompetenz
 - Einschlägige Norm: Art. ___ GG
 - Bei Art. 72 Abs. 2 GG: Erforderlichkeit ___
 - BVerfG-Pinpoint: ___

2. Formelle Verfassungsmäßigkeit
 - Verfahren: ___
 - Zustimmungs-/Einspruchsgesetz: ___
 - Bestimmtheit: ___
 - Zitiergebot: ___
 - Wesentlichkeit (Kalkar): ___

3. Materielle Verfassungsmäßigkeit
 Pro betroffenes Grundrecht:
 - Art. ___ GG
 - Schutzbereich: ___
 - Eingriff: ___
 - Rechtfertigung: ___
 - Verhältnismäßigkeit: [4 Stufen]
 - BVerfG-Pinpoint: ___

4. Sonstige verfassungsrechtliche Bindungen
 - Rechtsstaat, Rückwirkung: ___
 - Demokratie / Parlamentsvorbehalt: ___
 - Sozialstaat: ___
 - Bundesstaat: ___
 - Unionsrecht: ___

5. Empfehlung Gesetzesbegründung
 - ___

6. Risikoeinschätzung
 - [niedrig / mittel / hoch]
 - Empfehlung: ___

BVerfG-Pinpoints
- ___
```

## Disclaimer-Wiederholung

Diese Prüfung ersetzt nicht die externe verfassungsrechtliche Begutachtung. Insbesondere die abschließende Beurteilung der Verfassungsmäßigkeit obliegt im Streitfall allein dem BVerfG.
