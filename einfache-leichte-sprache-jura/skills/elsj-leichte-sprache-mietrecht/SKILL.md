---
name: elsj-leichte-sprache-mietrecht
description: "Elsj Leichte Sprache Mietrecht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Elsj Leichte Sprache Mietrecht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Elsj Leichte Sprache Mietrecht** im Plugin Einfache Leichte Sprache Jura. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `elsj-leichte-sprache` | Kanzlei oder Behoerde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur erklärte Woerter. Normen BGG § 11 BITV 2.0 Netzwerk Leichte Sprache Regeln. Prüfraster Satzlaenge max. 8 Woerter aktive Formulierung Erklärungen sichtbare Schritte Nutzergruppen-Test. Output Leichte-Sprache-Fassung Glossar. Abgrenzung zu elsj-einfache-sprache (B1-Niveau) und elsj-qualitaetsgate (Prüfung). |
| `elsj-mietrecht-kuendigungserklaerung` | Wohnungsmietrecht in einfacher Sprache fuer Mieter: Kuendigung erklaert (Frist, Form, Schriftform § 568 BGB), Schonfristzahlung § 569 Abs. 3 BGB, Mieterhoehung, Betriebskostenabrechnung. Mandantenformularsatz. |
| `elsj-pruefkriterien-fuer-qualitaet` | Qualitaetspruefung Einfache/Leichte Sprache: Pruefliste mit Wortlaenge, Satzlaenge, Verbquote, Fremdwortquote, Anteil Aktiv-/Passivsaetze. Empfehlung Tools (LIX-Index, Hohenheimer Verstaendlichkeitsindex). |

## Arbeitsweg

Im Plugin Einfache Leichte Sprache Jura gilt für **Elsj Leichte Sprache Mietrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `elsj-leichte-sprache`

**Fokus:** Kanzlei oder Behoerde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur erklärte Woerter. Normen BGG § 11 BITV 2.0 Netzwerk Leichte Sprache Regeln. Prüfraster Satzlaenge max. 8 Woerter aktive Formulierung Erklärungen sichtbare Schritte Nutzergruppen-Test. Output Leichte-Sprache-Fassung Glossar. Abgrenzung zu elsj-einfache-sprache (B1-Niveau) und elsj-qualitaetsgate (Prüfung).

# Leichte Sprache

Dieses Fachmodul, wenn ein juristischer Text für Menschen mit sehr geringer
Lesekompetenz oder hohem Barrierefreiheitsbedarf verständlich werden soll.


## Triage zu Beginn
1. Wurde sichergestellt, dass Leichte Sprache (nicht Einfache Sprache) der richtige Modus ist?
2. Gibt es eine Pruefgruppe aus der Zielgruppe — oder bleibt es beim Entwurf-Status?
3. Welche Fristen und Rechtsfolgen muessen unbedingt erhalten bleiben?
4. Sollen Bilder oder Piktogramme eingesetzt werden (Hinweis auf Grafik-Ressourcen erforderlich)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 11 BGG — Anspruch auf barrierefreie Kommunikation gegenueber Behoerden
- Art. 9 UN-BRK — Uebereinkommen ueber die Rechte von Menschen mit Behinderungen: Zugaenglichkeit von Informationen
- § 12a BGG — Webzugaenglichkeitsgesetz: Anforderungen an oeffentliche digitale Dokumente
- DIN EN ISO 9241-171 — Ergonomie der Mensch-System-Interaktion: Barrierefreiheit

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Leichte-Sprache-Fassung

**Adressat:** Personen mit Leseschwierigkeiten / Barrierefreiheitsbedarf
**Tonfall:** direkt, respektvoll, eine Information pro Satz

```
# Worum geht es?

[1-2 kurze Saetze. Kein Nebensatz.]

# Was bedeutet das fuer Sie?

[Jede Information in einem eigenen Satz.]
[Aktiv formulieren.]

# Was muessen Sie jetzt tun?

1. [Erste Handlung]
2. [Zweite Handlung]
3. [Dritte Handlung]

# Wichtiges Datum

[TAG]. [MONAT] [JAHR]

Das ist die Frist.
Wenn Sie diese Frist verpassen, dann:
[Rechtsfolge in einem Satz]

# Schwere Woerter

Wort: [FACHBEGRIFF]
Das bedeutet: [Erklaerung in 1-2 Saetzen]

# Wer kann helfen?

[Name / Stelle / Telefonnummer / Adresse]
```

> **Hinweis:** Dieser Entwurf ist in Leichter Sprache formuliert.
> Eine Pruefung durch Personen aus der Zielgruppe steht noch aus.
## Grundhaltung

Leichte Sprache ist kein "netter Ton". Sie ist ein eigenständiges
barrierearmes Textformat. Der Text darf einfacher wirken als normale
Standardsprache. Er muss trotzdem respektvoll und rechtlich richtig bleiben.

## Arbeitsregeln

- Schreibe sehr kurze Sätze.
- Schreibe möglichst nur eine Information pro Satz.
- Nutze viele Absätze.
- Setze wichtige Schritte untereinander.
- Sprich die Person direkt an.
- Verwende bekannte Wörter.
- Erkläre schwere Wörter sofort.
- Vermeide Passiv.
- Vermeide Genitiv.
- Vermeide Konjunktiv, wenn er nicht nötig ist.
- Vermeide doppelte Verneinungen.
- Teile lange Wörter, wenn das Lesen leichter wird.
- Zeige Fristen, Beträge und Termine einzeln.
- Nutze Beispiele nur, wenn sie nicht verwirren.

## Juristische Sicherung

Bei juristischen Begriffen gilt:

- Der schwere Begriff darf stehen bleiben, wenn er rechtlich wichtig ist.
- Danach kommt eine kurze Erklärung.
- Der Originalbegriff kann in Klammern stehen.
- Fristen und Rechtsfolgen bleiben sichtbar.

Beispiel:

```markdown
Sie können Widerspruch machen.

Widerspruch heißt:
Sie sagen der Behörde:
Ich bin mit dem Bescheid nicht einverstanden.
Bitte prüfen Sie den Bescheid noch einmal.
```

## Empfohlene Form

```markdown
# Worum geht es?

...

# Was bedeutet das für Sie?

...

# Was müssen Sie jetzt tun?

1. ...
2. ...
3. ...

# Wichtiges Datum

...

# Schwere Wörter

...

# Wer kann helfen?

...
```

## Prüfgruppen-Hinweis

Behaupte nie:

> Dieser Text ist in Leichter Sprache geprüft.

Das darf nur gesagt werden, wenn tatsächlich Personen aus der Zielgruppe den
Text geprüft haben und die Prüfung dokumentiert ist.

Wenn keine Prüfung stattgefunden hat, schreibe:

> Dieser Entwurf ist in Leichter Sprache formuliert.
> Eine Prüfung durch Personen aus der Zielgruppe steht noch aus.

## 2. `elsj-mietrecht-kuendigungserklaerung`

**Fokus:** Wohnungsmietrecht in einfacher Sprache fuer Mieter: Kuendigung erklaert (Frist, Form, Schriftform § 568 BGB), Schonfristzahlung § 569 Abs. 3 BGB, Mieterhoehung, Betriebskostenabrechnung. Mandantenformularsatz.

# ELS-J Wohnungsmietrecht

## Spezialwissen: ELS-J Wohnungsmietrecht
- **Spezialgegenstand:** ELS-J Wohnungsmietrecht / elsj mietrecht kuendigungserklaerung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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

## 3. `elsj-pruefkriterien-fuer-qualitaet`

**Fokus:** Qualitaetspruefung Einfache/Leichte Sprache: Pruefliste mit Wortlaenge, Satzlaenge, Verbquote, Fremdwortquote, Anteil Aktiv-/Passivsaetze. Empfehlung Tools (LIX-Index, Hohenheimer Verstaendlichkeitsindex).

# ELS-J Qualitaetspruefung

## Spezialwissen: ELS-J Qualitaetspruefung
- **Spezialgegenstand:** ELS-J Qualitaetspruefung / elsj pruefkriterien fuer qualitaet. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** LIX, ELS.
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
