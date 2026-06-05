---
name: regr-mifid2-regrecht-einfuehrung-internal
description: "Regr Mifid2 Regrecht Einfuehrung Internal: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Regr Mifid2 Regrecht Einfuehrung Internal

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Regr Mifid2 Regrecht Einfuehrung Internal** im Plugin Regulatorisches Recht (Sektoren). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `regr-mifid2-mar-leitfaden` | Leitfaden MiFID II und MAR: Wohlverhaltenspflichten, Suitability, Ad-hoc-Publizitaet, Insiderrecht. Pruefraster fuer Emittent und Wertpapierdienstleister. |
| `regrecht-einfuehrung-sektoren` | Einfuehrung regulatorisches Recht in den wichtigsten Sektoren: Bank, Versicherung, Energie, Telekommunikation, Verkehr, Pharma, Lebensmittel. Pro Sektor: Aufsicht, Kernnormen, Lizenzpflicht, typische Compliance-Aufgaben. Entscheidungstabelle und Verweis auf passende Detail-Skills. |
| `regrecht-internal-policies-design` | Internal Policies regulatorisch design: Hierarchie (Konzernrichtlinie, Tochterrichtlinie, Arbeitsanweisung, Verfahrensbeschreibung), Pflichtbestandteile, Versionierung, Verteilung, Schulung, Wirksamkeitsmessung. Mustertemplate fuer Bank- und Versicherungskonzerne. |

## Arbeitsweg

Im Plugin Regulatorisches Recht (Sektoren) gilt für **Regr Mifid2 Regrecht Einfuehrung Internal**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `regr-mifid2-mar-leitfaden`

**Fokus:** Leitfaden MiFID II und MAR: Wohlverhaltenspflichten, Suitability, Ad-hoc-Publizitaet, Insiderrecht. Pruefraster fuer Emittent und Wertpapierdienstleister.

# RegR: MiFID II MAR

## Aufgabe
Leitfaden MiFID II und MAR: Wohlverhaltenspflichten, Suitability, Ad-hoc-Publizitaet, Insiderrecht.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster MiFID II und MAR

### A. MiFID II / WpHG — Wohlverhaltenspflichten

#### 1. Anwendungsbereich
- **RL 2014/65/EU** (MiFID II) + **VO 600/2014** (MiFIR); in DE umgesetzt v.a. im **WpHG**, KWG, WpIG.
- Adressaten: **Wertpapierdienstleistungsunternehmen** § 2 Nr. 35 WpHG (Banken mit WpDL-Erlaubnis, Wertpapierinstitute, Kapitalverwaltungsgesellschaften für gewisse Dienste).

#### 2. Kundenkategorisierung § 67 WpHG
- **Geeignete Gegenpartei** (höchste Sophistication; reduzierter Schutz).
- **Professioneller Kunde** (Anlage 1 zu § 67 II WpHG — typisch Banken, Versicherungen, große Unternehmen).
- **Privatkunde** (höchster Schutz; Standardkategorie).

#### 3. Suitability und Appropriateness
- **Geeignetheitstest (Suitability)** § 64 III WpHG: bei Anlageberatung und Finanzportfolioverwaltung — Kenntnisse, Erfahrungen, finanzielle Verhältnisse, Anlageziele.
- **Angemessenheitstest (Appropriateness)** § 63 X WpHG: bei beratungsfreiem Geschäft — Kenntnisse und Erfahrungen.
- **Execution-only** § 63 XI WpHG: nur bei "nicht-komplexen Finanzinstrumenten" auf Kundeninitiative.
- **Geeignetheitserklärung** § 64 IV WpHG: schriftliche Begründung der Empfehlung.

#### 4. Aufzeichnungs- und Informationspflichten
- **Telefonaufzeichnung** § 83 III WpHG (alle Gespräche im Zusammenhang mit Geschäftsabschluss).
- **Kostenausweis (Ex-ante und Ex-post)** § 63 VII WpHG: alle Kosten und Nebenkosten — auch Zuwendungen (Inducements) — auflisten.
- **Best Execution** § 82 WpHG: Ausführung im besten Interesse des Kunden.
- **Geeignetheitserklärung und Berichte** § 63 XII WpHG.

#### 5. Inducements / Zuwendungen
- **Verbot** § 64 V WpHG bei unabhängiger Anlageberatung und Finanzportfolioverwaltung.
- **Zulässig** bei nicht-unabhängiger Beratung, wenn Qualität verbessert und Kunden offengelegt.

### B. MAR (Marktmissbrauchsverordnung VO 596/2014)

#### 1. Anwendungsbereich
- **VO (EU) 596/2014** unmittelbar anwendbar; ergänzt durch RL 2014/57/EU (Strafrecht).
- Anwendbar auf Finanzinstrumente, die zum Handel an geregelten Märkten / MTF / OTF zugelassen sind oder beantragt werden.

#### 2. Insiderrecht
- **Insiderinformation** Art. 7 MAR: nicht öffentlich, präzise, Bezug zu Emittenten / Finanzinstrumenten, eignet sich erheblich Kursbeeinflussung.
- **Insidergeschäft-Verbot** Art. 14, 8 MAR: Erwerb / Veräußerung auf Basis Insiderinformation.
- **Stop-Loss-Buy-Order** ist nicht zwingend Insiderhandel; bei vorhandener Order ggf. Ausnahme Art. 9 MAR.
- **Empfehlung / Aufforderung** zum Insiderhandel verboten Art. 14 lit. b MAR.

#### 3. Marktmanipulation
- Art. 12 MAR: Geschäftsabschluss mit falschem oder irreführendem Signal; Verbreitung falscher Informationen; Verhalten zur Beeinflussung Marktpreis.
- Beispiele: Layering, Spoofing, Wash Sales, Pump-and-Dump.

#### 4. Ad-hoc-Publizität Art. 17 MAR
- **Unverzüglich** alle Insiderinformationen veröffentlichen, die Emittenten unmittelbar betreffen.
- **Verschiebung** Art. 17 IV MAR möglich, wenn: legitimes Interesse, keine Irreführung, Vertraulichkeit gewährleistet (Selbstkontrolle).
- **Form**: Veröffentlichung an europäischen Standard; in DE an BaFin und Bundesanzeiger.

#### 5. Directors' Dealings Art. 19 MAR
- Geschäfte Führungspersonen und nahestehender Personen: Meldepflicht ab 5.000 Euro / Kalenderjahr binnen 3 Geschäftstagen.
- Veröffentlichung durch Emittenten.
- **Closed Periods** Art. 19 XI MAR: 30 Tage vor Veröffentlichung Zwischenbericht — Handelsverbot.

#### 6. Insiderlisten Art. 18 MAR
- Emittent muss alle Personen erfassen, die Zugang zu Insiderinformationen haben.
- Aktualisierung; Aufbewahrung 5 Jahre.

### Sanktionen
- **OWi** § 120 WpHG mit Bußgeld bis 5 Mio. Euro / 10 % Jahresumsatz / dreifaches wirtschaftliches Vorteil.
- **Strafrecht** § 119 WpHG: Insiderhandel, Marktmanipulation — bis 5 Jahre Freiheitsstrafe.
- **BaFin-Maßnahmen**: Verwarnung, Untersagung, Lizenzentzug.

## Praxisfallen

- **Inducements** in Wertpapierberatung: Verbot bei unabhängiger Beratung; sonst Offenlegung im Ex-ante-Kostenausweis.
- **Ad-hoc-Verschiebung** muss dokumentiert sein; BaFin prüft im Nachgang.
- **Closed Periods** Art. 19 XI MAR: Notfallkommunikation Stakeholder Vorsicht.
- **Kryptohandel**: MiCA seit 30.12.2024 separat zur MiFID/MAR; ART/EMT eigenständige Regeln.
- **Front Running**, **Tippgeber-Geschäfte**: oft schwerwiegender als reine Insiderkenntnis.
- **Telefonaufzeichnung**: 5 Jahre Aufbewahrung; BaFin-Anforderung an Auslandsanrufe Adressaten beachten.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

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

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `regrecht-einfuehrung-sektoren`

**Fokus:** Einfuehrung regulatorisches Recht in den wichtigsten Sektoren: Bank, Versicherung, Energie, Telekommunikation, Verkehr, Pharma, Lebensmittel. Pro Sektor: Aufsicht, Kernnormen, Lizenzpflicht, typische Compliance-Aufgaben. Entscheidungstabelle und Verweis auf passende Detail-Skills.

# Regrecht: Sektoren-Einfuehrung

## Spezialwissen: Regrecht: Sektoren-Einfuehrung
- **Spezialgegenstand:** Regrecht: Sektoren-Einfuehrung / regrecht einfuehrung sektoren. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
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

## 3. `regrecht-internal-policies-design`

**Fokus:** Internal Policies regulatorisch design: Hierarchie (Konzernrichtlinie, Tochterrichtlinie, Arbeitsanweisung, Verfahrensbeschreibung), Pflichtbestandteile, Versionierung, Verteilung, Schulung, Wirksamkeitsmessung. Mustertemplate fuer Bank- und Versicherungskonzerne.

# Regrecht: Internal Policies

## Spezialwissen: Regrecht: Internal Policies
- **Spezialgegenstand:** Regrecht: Internal Policies / regrecht internal policies design. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
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
