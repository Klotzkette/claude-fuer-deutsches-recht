---
name: elsj-qualitaetsgate-rechtsnormen-einfach
description: "Elsj Qualitaetsgate Rechtsnormen Einfach: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Elsj Qualitaetsgate Rechtsnormen Einfach

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Elsj Qualitaetsgate Rechtsnormen Einfach** im Plugin Einfache Leichte Sprache Jura. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `elsj-qualitaetsgate` | Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 Netzwerk Leichte Sprache. Prüfraster Verstaendlichkeits-Score Gliederungs-Check Glossar-Vollständigkeit Rechtsinhalt-Sicherung. Output Prüfergebnis-Bericht Verbesserungshinweise. Abgrenzung zu elsj-juristische-sicherung (Inhalt) und elsj-einfache-sprache/elsj-leichte-sprache (Übertragung). |
| `elsj-rechtsnormen-einfach` | Rechtsnormen in Einfacher/Leichter Sprache wiedergeben: § 17 InsO wird zu 'Eine Firma muss Insolvenz anmelden, wenn sie ihre Rechnungen nicht mehr bezahlen kann. Das gilt drei Wochen nach dem Tag, an dem klar wurde, dass kein Geld da ist.' Vorgehensweise und Beispiele. |
| `elsj-satzbau-regeln` | Satzbau-Regeln: maximal ein Komma pro Satz in Einfacher Sprache, ueberhaupt keine Kommata in Leichter Sprache, kurze Saetze, aktive Formulierung, Subjekt vor Praedikat. Vermeidung Passiv, Substantivketten, Genitiv. |

## Arbeitsweg

Im Plugin Einfache Leichte Sprache Jura gilt für **Elsj Qualitaetsgate Rechtsnormen Einfach**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `elsj-qualitaetsgate`

**Fokus:** Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 Netzwerk Leichte Sprache. Prüfraster Verstaendlichkeits-Score Gliederungs-Check Glossar-Vollständigkeit Rechtsinhalt-Sicherung. Output Prüfergebnis-Bericht Verbesserungshinweise. Abgrenzung zu elsj-juristische-sicherung (Inhalt) und elsj-einfache-sprache/elsj-leichte-sprache (Übertragung).

# Qualitätsgate

Dieses Fachmodul vor jeder Herausgabe.


## Triage zu Beginn
1. In welchem Modus wurde der Text erstellt: Einfache Sprache oder Leichte Sprache?
2. Fuer welche Zielgruppe und welches Medium ist der Text bestimmt?
3. Gibt es bekannte Risikostellen (Fristen, Wahlrechte, Ausnahmen), die besonders geprueft werden muessen?
4. Liegt ein Pruefgruppen-Protokoll vor oder soll das Gate nur einen Entwurfs-Check durchfuehren?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 11 BGG — Pruefpflicht der oeffentlichen Hand fuer barrierefreie Kommunikation
- § 58 VwGO — Fehlerhafte Rechtsbehelfsbelehrung fuehrt zur Fristverlaengerung
- BITV 2.0 Anhang 1 — Pruefanforderungen fuer digitale Barrierefreiheit
- DIN 33430 — Qualitaetsanforderungen an Testverfahren (analog heranziehbar fuer Verstaendlichkeitspruefungen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Qualitaetsgate-Ergebnis

```
## Qualitaetsgate

Geprueft am: [DATUM]
Modus: Einfache Sprache / Leichte Sprache
Zielgruppe: [Bezeichnung]

Status: freigabereif / ueberarbeiten / Nutzergruppe-Pruefung offen

### Staerken
- [...]

### Risiken
- [...]

### Muss vor Herausgabe korrigiert werden
- [...]

### Kann verbessert werden
- [...]

### Harte Stopps (falls zutreffend)
- [ ] Frist oder Rechtsfolge fehlt
- [ ] Pflicht als bloss Empfehlung dargestellt
- [ ] Rechtsmittel falsch bezeichnet
- [ ] Leichte Sprache: Pruefung durch Zielgruppe faelschlich behauptet
- [ ] Text wirkt herablassend
```
## Pflichtprüfung

| Prüffeld | Frage |
| --- | --- |
| Zielgruppe | Ist klar, für wen der Text geschrieben ist? |
| Zielhandlung | Ist klar, was die Person tun soll oder tun kann? |
| Struktur | Sind Überschriften aussagekräftig? |
| Fristen | Sind alle Fristen sichtbar und richtig? |
| Rechtsfolgen | Sind Risiken und Folgen klar genannt? |
| Wörter | Sind Fachwörter erklärt? |
| Satzbau | Sind Sätze kurz und eindeutig? |
| Ton | Ist der Text respektvoll? |
| Recht | Wurde nichts rechtlich Wichtiges weggelassen? |
| Prüfung | Ist eine Nutzerprüfung erforderlich oder offen? |

## Automatischer Vorcheck

Optional:

```bash
python einfache-leichte-sprache-jura/scripts/verstaendlichkeitscheck.py <datei> --mode einfache
python einfache-leichte-sprache-jura/scripts/verstaendlichkeitscheck.py <datei> --mode leichte
```

Bewerte das Skript nur als Warnsystem. Ein kurzer Text kann trotzdem schlecht
sein. Ein längerer Satz kann ausnahmsweise nötig sein.

## Ergebnisformat

```markdown
## Qualitätsgate

Status: freigabereif / überarbeiten / Nutzerprüfung offen

### Stärken

- ...

### Risiken

- ...

### Muss vor Herausgabe korrigiert werden

- ...

### Kann verbessert werden

- ...
```

## Harte Stopps

Stoppe die Herausgabe, wenn:

- Frist oder Rechtsfolge fehlt.
- eine Pflicht als bloße Empfehlung dargestellt wird.
- ein Rechtsmittel falsch bezeichnet ist.
- bei Leichter Sprache fälschlich behauptet wird, es habe eine Prüfung durch
 Zielgruppenpersonen gegeben.
- der Text herablassend wirkt.

## 2. `elsj-rechtsnormen-einfach`

**Fokus:** Rechtsnormen in Einfacher/Leichter Sprache wiedergeben: § 17 InsO wird zu 'Eine Firma muss Insolvenz anmelden, wenn sie ihre Rechnungen nicht mehr bezahlen kann. Das gilt drei Wochen nach dem Tag, an dem klar wurde, dass kein Geld da ist.' Vorgehensweise und Beispiele.

# ELS-J: Rechtsnormen einfach

## Spezialwissen: ELS-J: Rechtsnormen einfach
- **Spezialgegenstand:** ELS-J: Rechtsnormen einfach / elsj rechtsnormen einfach. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO, ELS.
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

## 3. `elsj-satzbau-regeln`

**Fokus:** Satzbau-Regeln: maximal ein Komma pro Satz in Einfacher Sprache, ueberhaupt keine Kommata in Leichter Sprache, kurze Saetze, aktive Formulierung, Subjekt vor Praedikat. Vermeidung Passiv, Substantivketten, Genitiv.

# ELS-J: Satzbau-Regeln

## Spezialwissen: ELS-J: Satzbau-Regeln
- **Spezialgegenstand:** ELS-J: Satzbau-Regeln / elsj satzbau regeln. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
