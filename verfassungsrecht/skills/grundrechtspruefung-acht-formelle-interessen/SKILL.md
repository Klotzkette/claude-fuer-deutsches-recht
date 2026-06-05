---
name: grundrechtspruefung-acht-formelle-interessen
description: "Grundrechtspruefung Acht Formelle Interessen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Grundrechtspruefung Acht Formelle Interessen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Grundrechtspruefung Acht Formelle Interessen** im Plugin Verfassungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `grundrechtspruefung` | Grundrechtsprüfung nach dem Drei-Stufen-Schema durchführen wenn staatliche Massnahme Grundrecht beruehrt. Art. 1-19 GG Grundrechte Art. 20 Abs. 3 GG Verhältnismäßigkeit. Prüfraster: Schutzbereich Eingriff Rechtfertigung verfassungsrechtliche Schranken Wesensgehalt Art. 19 Abs. 2 GG Verhältnismäßigkeit. Output: Grundrechtsprüfschema Prüfergebnis. Abgrenzung: nicht für formelle Verfassungsmäßigkeit (formelle-verfassungsmäßigkeit). |
| `spezial-acht-zahlen-schwellen-und-berechnung` | Acht: Zahlen, Schwellenwerte und Berechnung im Plugin verfassungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-formelle-mehrparteien-konflikt-und-interessen` | Formelle: Mehrparteienkonflikt und Interessenmatrix im Plugin verfassungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Verfassungsrecht gilt für **Grundrechtspruefung Acht Formelle Interessen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `grundrechtspruefung`

**Fokus:** Grundrechtsprüfung nach dem Drei-Stufen-Schema durchführen wenn staatliche Massnahme Grundrecht beruehrt. Art. 1-19 GG Grundrechte Art. 20 Abs. 3 GG Verhältnismäßigkeit. Prüfraster: Schutzbereich Eingriff Rechtfertigung verfassungsrechtliche Schranken Wesensgehalt Art. 19 Abs. 2 GG Verhältnismäßigkeit. Output: Grundrechtsprüfschema Prüfergebnis. Abgrenzung: nicht für formelle Verfassungsmäßigkeit (formelle-verfassungsmäßigkeit).

# Grundrechtsprüfung

## Fachkern: Grundrechtsprüfung
- **Spezialgegenstand:** Grundrechtsprüfung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Disclaimer

Grundrechtsprüfungen sind hochkomplex und in der konkreten Anwendung nur durch das BVerfG verbindlich klärbar. Diese Prüfung ist eine Unterstützung, **kein Ersatz** für anwaltliche Beratung durch eine verfassungsrechtliche Spezialkanzlei.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst aufrufen. Pinpoint Az. + Rn. + URL pro tragender Aussage.

## Grundschema: Schutzbereich – Eingriff – Rechtfertigung

### Schritt 1 — Schutzbereichseröffnung

#### 1a. Persönlicher Schutzbereich

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Jedermanngrundrechte:** Art. 1, 2, 3, 4, 5, 10, 13, 14, 17 GG — alle natürlichen Personen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### 1b. Sachlicher Schutzbereich

Was schützt das Grundrecht? Wortlaut, Systematik, Telos. Bei der Bestimmung **nicht restriktiv** vorgehen (in dubio pro libertate).

**Standard-Schutzbereiche** (mit Pinpoint live nachrecherchieren):

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Art. 4 Abs. 1, 2 GG:** Glaubens-, Gewissens- und Bekenntnisfreiheit — vorbehaltlos.
- **Art. 5 Abs. 1 GG:** Meinungs-, Informations-, Presse-, Rundfunk- und Filmfreiheit.
- **Art. 5 Abs. 3 GG:** Kunst- und Wissenschaftsfreiheit — vorbehaltlos.
- **Art. 8 GG:** Versammlungsfreiheit (Deutsche).
- **Art. 9 GG:** Vereinigungsfreiheit (Deutsche), Art. 9 Abs. 3 GG Koalitionsfreiheit (jedermann).
- **Art. 10 GG:** Brief-, Post- und Fernmeldegeheimnis.
- **Art. 12 GG:** Berufsfreiheit (Deutsche).
- **Art. 13 GG:** Unverletzlichkeit der Wohnung.
- **Art. 14 GG:** Eigentum und Erbrecht — Eigentumsbegriff weit (alle vermögenswerten Rechtspositionen, kraft Gesetz oder Gewohnheit anerkannt).

### Schritt 2 — Eingriff

#### 2a. Klassischer Eingriffsbegriff

Final, unmittelbar, rechtsförmig, mit Befehl und Zwang.

#### 2b. Moderner Eingriffsbegriff

Jede dem Staat zurechenbare Beeinträchtigung des grundrechtlich geschützten Verhaltens. Erfasst auch:

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Faktische Eingriffe** (Maßnahmen ohne Zwang, die das geschützte Verhalten erschweren).
- **Schutzpflicht-Verletzungen** (untermaß-Verbot bei Schutz vor Dritten).

#### 2c. Eingriffsqualifikation

- Welcher Grundrechtsträger ist betroffen?
- Wie schwer ist der Eingriff (für Verhältnismäßigkeit relevant)?
- Bei mehreren Grundrechten: spezielleres Grundrecht vorrangig, Art. 2 Abs. 1 GG subsidiär.

### Schritt 3 — Verfassungsrechtliche Rechtfertigung

#### 3a. Schranke

**Klassifikation:**

- **Einfacher Gesetzesvorbehalt** — z. B. Art. 2 Abs. 2 S. 3 GG, Art. 11 Abs. 2 GG (für bestimmte Fälle), Art. 12 Abs. 1 S. 2 GG.
- **Qualifizierter Gesetzesvorbehalt** — Schranke nur unter bestimmten zusätzlichen Voraussetzungen. Z. B. Art. 5 Abs. 2 GG ("allgemeine Gesetze", Schutz der Jugend, Recht der persönlichen Ehre); Art. 8 Abs. 2 GG (Versammlungen unter freiem Himmel); Art. 13 GG (Eingriffsstaffel).
- **Vorbehaltlos gewährtes Grundrecht** — z. B. Art. 4, Art. 5 Abs. 3 GG, Glaubensfreiheit, Kunst- und Wissenschaftsfreiheit. Eingriff nur durch **verfassungsimmanente Schranken** rechtfertigbar (kollidierendes Verfassungsrecht, insbesondere Grundrechte Dritter und Verfassungsgüter mit Verfassungsrang).

#### 3b. Schranken-Schranken

Die Schranke darf ihrerseits nicht gegen Verfassungsrecht verstoßen:

1. **Verhältnismäßigkeit** (Skill `verhaeltnismaessigkeit`): legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit.
2. **Wesensgehaltsgarantie** (Art. 19 Abs. 2 GG): absoluter Kernbereich darf nicht verletzt werden.
3. **Zitiergebot** (Art. 19 Abs. 1 S. 2 GG, nur bei einschränkenden Gesetzen mit Wirkungsabsicht auf das Grundrecht).
4. **Allgemeinheit** (Art. 19 Abs. 1 S. 1 GG).
5. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
6. **Spezifische Vorgaben des qualifizierten Vorbehalts** (z. B. Allgemeinheit des Gesetzes bei Art. 5 Abs. 2 GG).
7. **Bestimmtheitsgebot, Wesentlichkeit** (siehe Skill `formelle-verfassungsmaessigkeit`).

### Schritt 4 — Spezielle Strukturen einzelner Grundrechte

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

| Stufe | Charakter | Rechtfertigungsanforderung |
| --- | --- | --- |
| 1 — Berufsausübungsregelung | Wie / Art und Weise der Berufstätigkeit | Jeder vernünftige Gemeinwohlgrund genügt |
| 2 — Subjektive Berufszulassungsschranke | Anknüpfung an persönliche Eigenschaften (Qualifikation, Prüfung) | Schutz wichtiger Gemeinschaftsgüter |
| 3 — Objektive Berufszulassungsschranke | Vom Bewerber unabhängige Voraussetzungen (Bedürfnisprüfung) | Schutz **überragend wichtiger** Gemeinschaftsgüter vor **nachweisbaren oder höchstwahrscheinlichen schweren** Gefahren |

Eingriff stets auf der **geringstmöglichen Stufe**.

#### 4b. Art. 14 GG — Eigentum

- Drei Eingriffsformen: **Inhalts- und Schrankenbestimmung** (Art. 14 Abs. 1 S. 2 GG), **Enteignung** (Art. 14 Abs. 3 GG), **ausgleichspflichtige Inhalts- und Schrankenbestimmung**.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### 4c. Art. 8 GG — Versammlung

- Versammlungsbegriff: gemeinsame Erörterung oder Kundgabe auf Teilnahme an öffentlicher Meinungsbildung gerichtet.
- Versammlungen **unter freiem Himmel:** qualifizierter Gesetzesvorbehalt Art. 8 Abs. 2 GG.
- **In geschlossenen Räumen:** vorbehaltlos.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### 4d. Art. 5 Abs. 1 GG — Meinungsfreiheit

- Tatsachenbehauptungen sind geschützt, **soweit** sie Voraussetzung der Meinungsbildung sind; **unwahre und bewusst unwahre** Tatsachenbehauptungen sind nicht geschützt.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Wechselwirkungslehre Lüth.

### Schritt 5 — Konkurrenzen

- Spezielleres vor allgemeinem Grundrecht (Art. 2 Abs. 1 GG subsidiär).
- Kombinations-Grundrecht aus Art. 2 Abs. 1 i.V.m. Art. 1 Abs. 1 GG (APR).
- Bei Idealkonkurrenz: parallele Prüfung beider Grundrechte; Eingriff muss in beiden gerechtfertigt sein.

## Output-Format

```
GRUNDRECHTSPRÜFUNG

Geprüftes Grundrecht: Art. ___ GG

1. Schutzbereich
 - Persönlich: ___
 - Sachlich: ___
 - Eröffnet: [ja / nein]

2. Eingriff
 - Art: [klassisch / mittelbar / faktisch]
 - Maßnahme: ___
 - Vorliegen: [ja / nein]

3. Verfassungsrechtliche Rechtfertigung
 - Schranke: [einfacher / qualifizierter Vorbehalt / vorbehaltlos]
 - Einschränkungsgesetz: ___
 - Schranken-Schranken:
 - Verhältnismäßigkeit: [siehe Skill verhältnismäßigkeit]
 - Wesensgehalt Art. 19 Abs. 2 GG: ___
 - Zitiergebot Art. 19 Abs. 1 S. 2 GG: ___
 - Wechselwirkung (Lüth): ___
 - Bestimmtheit, Wesentlichkeit: ___

BVerfG-Pinpoints
- ___

Ergebnis: [Grundrecht verletzt / nicht verletzt]
```

## Disclaimer-Wiederholung

Diese Prüfung ist eine strukturierte Modellauswertung und **kein Ersatz** für anwaltliche Bearbeitung durch eine verfassungsrechtliche Spezialkanzlei.

## 2. `spezial-acht-zahlen-schwellen-und-berechnung`

**Fokus:** Acht: Zahlen, Schwellenwerte und Berechnung im Plugin verfassungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Acht: Zahlen, Schwellenwerte und Berechnung

## Fachkern: Acht: Zahlen, Schwellenwerte und Berechnung
- **Spezialgegenstand:** Acht: Zahlen, Schwellenwerte und Berechnung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Acht** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `spezial-formelle-mehrparteien-konflikt-und-interessen`

**Fokus:** Formelle: Mehrparteienkonflikt und Interessenmatrix im Plugin verfassungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Formelle: Mehrparteienkonflikt und Interessenmatrix

## Fachkern: Formelle: Mehrparteienkonflikt und Interessenmatrix
- **Spezialgegenstand:** Formelle: Mehrparteienkonflikt und Interessenmatrix wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Formelle** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
