---
name: elsj-aufenthaltsrecht-mandant-betreuung
description: "Elsj Aufenthaltsrecht Mandant Betreuung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Elsj Aufenthaltsrecht Mandant Betreuung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Elsj Aufenthaltsrecht Mandant Betreuung** im Plugin Einfache Leichte Sprache Jura. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `elsj-aufenthaltsrecht-mandant` | Aufenthaltsrechtliche Mandantenkommunikation: AufenthG, Asyl, Familiennachzug. Anschreiben Auslaenderbehoerde Begleitschreiben fuer Mandanten. Vorlage Bescheid-Erklaerung. |
| `elsj-betreuung-vormundschaft` | Mandanten in Betreuung oder Vormundschaft: spezifische Regeln BGB §§ 1814 ff., Beruecksichtigung Wuensche § 1821, Genehmigungspflichten. Sprache muss die Person selbst erreichen. Vorlage Anschreiben Betreuter. |
| `elsj-einfache-sprache` | Kanzlei oder Behoerde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11 Leichte Sprache Behindertenrecht BITV 2.0. Prüfraster Satzlaenge Aktiv-Passiv-Balance Glossar Fristen-Sicherung Rechtsinhalt-Vollständigkeit. Output Einfache-Sprache-Version mit Erklärungen. Abgrenzung zu elsj-leichte-sprache (noch staerkere Vereinfachung B2/A2) und elsj-qualitaetsgate (Prüfung). |

## Arbeitsweg

Im Plugin Einfache Leichte Sprache Jura gilt für **Elsj Aufenthaltsrecht Mandant Betreuung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `elsj-aufenthaltsrecht-mandant`

**Fokus:** Aufenthaltsrechtliche Mandantenkommunikation: AufenthG, Asyl, Familiennachzug. Anschreiben Auslaenderbehoerde Begleitschreiben fuer Mandanten. Vorlage Bescheid-Erklaerung.

# ELS-J Aufenthaltsrecht

## Spezialwissen: ELS-J Aufenthaltsrecht
- **Spezialgegenstand:** ELS-J Aufenthaltsrecht / elsj aufenthaltsrecht mandant. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AufenthG, ELS.
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

## 2. `elsj-betreuung-vormundschaft`

**Fokus:** Mandanten in Betreuung oder Vormundschaft: spezifische Regeln BGB §§ 1814 ff., Beruecksichtigung Wuensche § 1821, Genehmigungspflichten. Sprache muss die Person selbst erreichen. Vorlage Anschreiben Betreuter.

# ELS-J fuer Betreute/Muendel

## Spezialwissen: ELS-J fuer Betreute/Muendel
- **Spezialgegenstand:** ELS-J fuer Betreute/Muendel / elsj betreuung vormundschaft. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB, ELS.
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

## 3. `elsj-einfache-sprache`

**Fokus:** Kanzlei oder Behoerde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11 Leichte Sprache Behindertenrecht BITV 2.0. Prüfraster Satzlaenge Aktiv-Passiv-Balance Glossar Fristen-Sicherung Rechtsinhalt-Vollständigkeit. Output Einfache-Sprache-Version mit Erklärungen. Abgrenzung zu elsj-leichte-sprache (noch staerkere Vereinfachung B2/A2) und elsj-qualitaetsgate (Prüfung).

# Einfache Sprache

Dieses Fachmodul, wenn ein juristischer Text für ein allgemeines Publikum
verständlich werden soll, ohne die Standardsprache vollständig zu verlassen.


## Triage zu Beginn
1. Welche Zielgruppe soll den Text lesen (allgemeines Publikum, Personen mit geringer Lesekompetenz, Verbraucher mit Behördenkontakt)?
2. Welches Medium: Brief, Bescheid, Website, Formular, E-Mail?
3. Darf der Text stark gekürzt werden oder muss der vollständige Rechtsinhalt erhalten bleiben?
4. Gibt es bereits einen Hausstil oder eine Vorlage für Einfache Sprache in der Einrichtung?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 11 BGG — Barrierefreiheit von Bescheiden und oeffentlichen Dokumenten
- § 9 EBV — Einfache Sprache in Bescheiden der Erbenberatung
- § 242 BGB — Treu und Glauben als Grundlage des Transparenzgebots
- BITV 2.0 — Barrierefreie-Informationstechnik-Verordnung, Anhang 1 (Verstaendlichkeit digitaler Dokumente)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Einfache-Sprache-Fassung

**Adressat:** Mandant / Buerger — **Tonfall:** klar, direkt, respektvoll

```
# Kurze Antwort

[1-2 Saetze: Das Wichtigste zuerst]

# Was ist passiert?

[Sachverhalt ohne Fachjargon]

# Was bedeutet das fuer Sie?

[Rechtliche Konsequenzen in verstaendlichen Worten]

# Was koennen Sie jetzt tun?

Option A: [Handlung 1 — Frist: DD.MM.JJJJ]
Option B: [Handlung 2]

# Frist

Wichtig: Bis [DATUM] muessen Sie handeln.
Wenn Sie nichts tun, dann: [Rechtsfolge kurz]

# Schwere Woerter kurz erklaert

- Widerspruch: Sie sagen der Behoerde, dass Sie nicht einverstanden sind.
- Verjährung: Nach Ablauf dieser Frist koennen Sie nichts mehr verlangen.
```
## Ziel

Der Text soll schnell beantworten:

- Worum geht es?
- Was bedeutet das für die lesende Person?
- Was muss oder kann sie tun?
- Bis wann?
- Was passiert, wenn sie nichts tut?

## Regeln für die Übertragung

- Stelle die wichtigste Information an den Anfang.
- Verwende klare Überschriften.
- Halte Absätze kurz.
- Schreibe aktiv.
- Nutze Verben statt Substantivierungen.
- Vermeide verschachtelte Sätze.
- Erkläre Fachwörter beim ersten Auftreten.
- Verwende denselben Begriff immer gleich.
- Ersetze Amts- und Kanzleistil durch direkte, respektvolle Sprache.
- Lass Rechtsgrundlagen stehen, wenn sie wichtig sind, aber erkläre ihre
 Bedeutung.

## Juristische Struktur

Für Mandantenbriefe und Verbraucherinformationen verwende bevorzugt:

```markdown
# Kurze Antwort

...

# Was ist passiert?

...

# Was bedeutet das für Sie?

...

# Was können Sie jetzt tun?

...

# Frist

...

# Schwere Wörter kurz erklärt

...
```

## Was nicht passieren darf

- Keine Frist verkürzen oder verlängern.
- Keine Pflicht in eine bloße Empfehlung umformulieren.
- Kein Wahlrecht unterschlagen.
- Keine Ausnahme weglassen, wenn sie praktisch wichtig sein kann.
- Keine ungesicherte Rechtsberatung hinzufügen.
- Keine rechtliche Unsicherheit als sicher darstellen.

## Stilhinweise

Schlecht:

> Gegen den Bescheid kann binnen eines Monats nach Bekanntgabe Widerspruch
> erhoben werden.

Besser:

> Sie können Widerspruch einlegen.
> Dafür haben Sie 1 Monat Zeit.
> Die Frist beginnt, wenn Sie den Bescheid bekommen haben.

## Ausgabe

Gib am Ende eine Mini-Prüfung aus:

| Punkt | Ergebnis |
| --- | --- |
| Zielgruppe genannt | ja/nein |
| Fristen erhalten | ja/nein |
| Rechtsfolgen erhalten | ja/nein |
| schwere Wörter erklärt | ja/nein |
| weiterer Prüfbedarf | kurz |
