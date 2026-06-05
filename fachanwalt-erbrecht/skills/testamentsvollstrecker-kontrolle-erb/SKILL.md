---
name: testamentsvollstrecker-kontrolle-erb
description: "Testamentsvollstrecker Kontrolle ERB: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Testamentsvollstrecker Kontrolle ERB

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Testamentsvollstrecker Kontrolle ERB** im Plugin Fachanwalt Erbrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `testamentsvollstrecker-kontrolle-haftung` | Testamentsvollstrecker: Amt, Zeugnis, Auskunft, ordnungsgemäße Verwaltung, Entlassung und Haftung.; Normanker: BGB §§ 2197 ff., 2218 und 2227 und 2219; fragt Unterlagen, Beweisstand, Fristen und taktische nächste Schritte konkret ab. |
| `erb-erbschaftsteuer-progressionsoptimierung-spezial` | Spezialfall Erbschaftsteuer-Optimierung: Freibetraege § 16 ErbStG, Steuerklassen I / II / III, Bewertung Betriebsvermoegen §§ 13a / 13b ErbStG, Familienheim § 13 ErbStG. Pruefraster fuer Steuer- und Erbrechtspraxis. |
| `erb-unternehmensnachfolge-spezial` | Spezialfall Unternehmensnachfolge: Vorab-Nachfolgeklauseln in Gesellschaftsvertrag, Pflichtteilsverzicht durch Erben, Stiftungsloesung, Verschonungsregelung §§ 13a / 13b / 19a ErbStG, Nachversteuerung Behaltensfrist. Pruefraster. |

## Arbeitsweg

Im Plugin Fachanwalt Erbrecht gilt für **Testamentsvollstrecker Kontrolle ERB**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `testamentsvollstrecker-kontrolle-haftung`

**Fokus:** Testamentsvollstrecker: Amt, Zeugnis, Auskunft, ordnungsgemäße Verwaltung, Entlassung und Haftung.; Normanker: BGB §§ 2197 ff., 2218 und 2227 und 2219; fragt Unterlagen, Beweisstand, Fristen und taktische nächste Schritte konkret ab.

# Testamentsvollstrecker: Amt, Zeugnis, Auskunft, ordnungsgemäße Verwaltung, Entlassung und Haftung.

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Testamentsvollstrecker: Amt, Zeugnis, Auskunft, ordnungsgemäße Verwaltung, Entlassung und Haftung.` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Testamentsvollstrecker: Amt, Zeugnis, Auskunft, ordnungsgemäße Verwaltung, Entlassung und Haftung.

- **Akte (Testamentsvollstrecker: Amt, Zeugnis, Auskunft, ordnungsgemäße Verwaltung, Entlassung und Haftung.):** Amt, Zeugnis, Auskunft, ordnungsgemäße Verwaltung, Entlassung und Haftung.
- **Prüfachse:** Anspruchsziel, Frist, Beweis, Gegenseite, Gericht/Zuständigkeit, Kostenrisiko und wirtschaftliches Ergebnis werden getrennt.
- **Arbeitsprodukt:** Schriftsatzkern, Stufenplan, Vergleichslinie oder Mandantenbrief mit Beleg- und Fristenmatrix.

## Normanker

BGB §§ 2197 ff., 2218, 2227, 2219. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle genannt; bei unsicherem Stand wird ausdrücklich ein Live-Check verlangt.

## Arbeitsfragen

1. Was ist das konkrete Ziel und welche Frist läuft?
2. Welche Urkunde, Mail, Zustellung, Berechnung oder Aussage belegt den entscheidenden Punkt?
3. Welche typische Gegenposition ist zu erwarten?
4. Welche prozessuale Form ist richtig: Schreiben, Antrag, Klage, Eilantrag, Vergleich, Red-Team?
5. Welche Formulierung vermeidet unnötige Zugeständnisse und hält den Fall offen?

## 2. `erb-erbschaftsteuer-progressionsoptimierung-spezial`

**Fokus:** Spezialfall Erbschaftsteuer-Optimierung: Freibetraege § 16 ErbStG, Steuerklassen I / II / III, Bewertung Betriebsvermoegen §§ 13a / 13b ErbStG, Familienheim § 13 ErbStG. Pruefraster fuer Steuer- und Erbrechtspraxis.

# Erb: Steuer-Optimierung

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erb: Steuer-Optimierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Erb: Steuer-Optimierung
- **Spezialgegenstand:** Erb: Steuer-Optimierung / erb erbschaftsteuer progressionsoptimierung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ErbStG, II, III.
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
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
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

## 3. `erb-unternehmensnachfolge-spezial`

**Fokus:** Spezialfall Unternehmensnachfolge: Vorab-Nachfolgeklauseln in Gesellschaftsvertrag, Pflichtteilsverzicht durch Erben, Stiftungsloesung, Verschonungsregelung §§ 13a / 13b / 19a ErbStG, Nachversteuerung Behaltensfrist. Pruefraster.

# Erbrecht: Unternehmensnachfolge

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erbrecht: Unternehmensnachfolge` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Erbrecht: Unternehmensnachfolge
- **Spezialgegenstand:** Erbrecht: Unternehmensnachfolge / erb unternehmensnachfolge spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ErbStG.
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
