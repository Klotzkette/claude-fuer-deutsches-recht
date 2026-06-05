---
name: elsj-familienrecht-erstgespraech-juristische
description: "Elsj Familienrecht Erstgespraech Juristische: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Elsj Familienrecht Erstgespraech Juristische

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Elsj Familienrecht Erstgespraech Juristische** im Plugin Einfache Leichte Sprache Jura. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `elsj-familienrecht-erstgespraech` | Familienrecht Erstgespraech in Einfacher Sprache: Trennung, Scheidung, Unterhalt, Sorgerecht, Umgang. Vorlage Memo fuer den Mandanten: 'Was muessen Sie wissen, was muessen Sie entscheiden?' Sprachlich barrierearm. |
| `elsj-juristische-sicherung` | Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit Pflichten-Sicherung Fristen-Erhalt Rechtsfolgen-Klarheit Ausnahmen-Abbildung. Output juristische Sicherungs-Checkliste gesicherte Fassung. Abgrenzung zu elsj-einfache-sprache (Übertragung) und elsj-qualitaetsgate (Endprüfung). |
| `elsj-kommunikation-mandant` | Mandantenkommunikation in Einfacher Sprache: Telefon-Leitfaden, E-Mail-Templates, schriftliche Information ueber das Verfahren. Pruefliste: Verstehen Sie das? Brauchen Sie eine Wiederholung? Notizen fuer den naechsten Termin. |

## Arbeitsweg

Im Plugin Einfache Leichte Sprache Jura gilt für **Elsj Familienrecht Erstgespraech Juristische**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `elsj-familienrecht-erstgespraech`

**Fokus:** Familienrecht Erstgespraech in Einfacher Sprache: Trennung, Scheidung, Unterhalt, Sorgerecht, Umgang. Vorlage Memo fuer den Mandanten: 'Was muessen Sie wissen, was muessen Sie entscheiden?' Sprachlich barrierearm.

# ELS-J Familienrecht-Erstgespraech

## Spezialwissen: ELS-J Familienrecht-Erstgespraech
- **Spezialgegenstand:** ELS-J Familienrecht-Erstgespraech / elsj familienrecht erstgespraech. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ELS.
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

## 2. `elsj-juristische-sicherung`

**Fokus:** Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit Pflichten-Sicherung Fristen-Erhalt Rechtsfolgen-Klarheit Ausnahmen-Abbildung. Output juristische Sicherungs-Checkliste gesicherte Fassung. Abgrenzung zu elsj-einfache-sprache (Übertragung) und elsj-qualitaetsgate (Endprüfung).

# Juristische Sicherung

Dieses Fachmodul vor und nach jeder Übertragung.

## Triage zu Beginn
1. Welche Fristen kommen im Originaltext vor — Datum, Fristbeginn, Fristende, Folgen?
2. Welche Pflichten (Muss-Handlungen) und welche Rechte (Kann-Optionen) sind enthalten?
3. Gibt es Ausnahmen oder Vorbehalte, die praktisch wichtig sein koennen?
4. Sind rechtliche Unsicherheiten oder offene Pruefungen im Originaltext erkennbar?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 58 VwGO — Rechtsbehelfsbelehrung und Fristverlaengerung bei fehlerhafter Belehrung
- § 355 BGB — Widerrufsrecht: Frist, Belehrung, Folgen bei fehlender Belehrung
- § 214 BGB — Wirkung der Verjährung
- § 130 BGB — Zugang als Fristbeginn

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Juristische Sicherungs-Matrix

```
## Juristische Sicherung — Pruefvermerk

Dokument: [TITEL / AKTENZEICHEN]
Geprueft am: [DATUM]

| Kategorie | Original | Erhalten? | Bemerkung |
|---|---|---|---|
| Frist | [Datum/Dauer] | ja/nein | [Fristbeginn, -ende, Folge] |
| Pflicht | [Muss-Handlung] | ja/nein | [Nicht abgeschwaecht?] |
| Recht | [Kann-Option] | ja/nein | [Als Option formuliert?] |
| Risiko | [Rechtsfolge] | ja/nein | [Klar aber nicht drohend?] |
| Ausnahme | [wenn vorhanden] | ja/nein | [Gesondert erklaert?] |
| Unsicherheit | [offene Fragen] | ja/nein | [Nicht als sicher dargestellt?] |

Gesamtbefund: freigabereif / nacharbeiten
Offene Punkte: [...]
```
## Bedeutungs-Matrix

Erstelle eine Tabelle:

| Original | Bedeutung | Muss erhalten bleiben? | Umsetzung |
| --- | --- | --- | --- |
| Frist | Datum, Beginn, Ende, Folge bei Versäumnis | immer | sichtbar und einfach |
| Pflicht | was die Person tun muss | immer | nicht abschwächen |
| Recht | was die Person tun darf oder kann | immer | als Option erklären |
| Risiko | Kosten, Klage, Vollstreckung, Sanktion | immer | klar, aber nicht drohend |
| Ausnahme | wann etwas nicht gilt | wenn praktisch relevant | gesondert erklären |
| Unsicherheit | Streit, fehlende Tatsachen, Prüfung offen | immer | nicht als sicher darstellen |

## Modalwörter sichern

Prüfe jedes Modalwort:

- **muss** bleibt muss.
- **kann** bleibt Möglichkeit.
- **darf** bleibt Erlaubnis.
- **soll** wird nicht automatisch zu muss.
- **unverzüglich** wird nicht einfach zu "bald", sondern erklärt.

## Fristen sichern

Bei jeder Frist:

- Datum nennen, wenn bekannt.
- Fristbeginn nennen.
- Fristende nennen.
- Folge nennen.
- Kontakt nennen, wenn die Person handeln soll.

## Rechtsbegriffe

Ein Rechtsbegriff darf ersetzt werden, wenn die Bedeutung vollständig erhalten
bleibt. Wenn nicht, bleibt der Begriff stehen und wird erklärt.

Beispiele für erklärungsbedürftige Wörter:

- Bescheid
- Widerspruch
- Klage
- Rechtskraft
- Vollstreckung
- Kündigung
- Widerruf
- Anfechtung
- Haftung
- Verjährung

## Prüfvermerk

Gib am Ende einen Vermerk aus:

```markdown
## Juristische Sicherung

- Fristen geprüft: ...
- Rechte und Pflichten geprüft: ...
- Risiken geprüft: ...
- Begriffe erklärt: ...
- Nicht geklärt: ...
```

## 3. `elsj-kommunikation-mandant`

**Fokus:** Mandantenkommunikation in Einfacher Sprache: Telefon-Leitfaden, E-Mail-Templates, schriftliche Information ueber das Verfahren. Pruefliste: Verstehen Sie das? Brauchen Sie eine Wiederholung? Notizen fuer den naechsten Termin.

# ELS-J: Mandantenkommunikation

## Spezialwissen: ELS-J: Mandantenkommunikation
- **Spezialgegenstand:** ELS-J: Mandantenkommunikation / elsj kommunikation mandant. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ELS.
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
