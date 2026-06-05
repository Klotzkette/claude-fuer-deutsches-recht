---
name: betreuung-strafverfahren-kalender-reminder
description: "Betreuung Strafverfahren Kalender Reminder: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Betreuung Strafverfahren Kalender Reminder

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Betreuung Strafverfahren Kalender Reminder** im Plugin Betreuungsrecht (§§ 1814 ff. BGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `betreuung-im-strafverfahren` | Betreuung im Strafverfahren des Betroffenen: Schuldfaehigkeit nach §§ 20 und 21 StGB, Verteidigerbestellung, Vertretung Betreuer im Hauptverfahren. Schnittstelle Strafrecht und Betreuungsrecht. |
| `kalender-reminder-und-fristenmanagement` | Kalender- und Reminder-Skill für Betreuungen: legt Berichtstermine, Vermögensverzeichnis, Rechnungslegung, Gerichtstermine, Bescheidfristen, Arzt-/Pflege-/Heimtermine, Genehmigungsentscheidungen und wiederkehrende Zahlungen als klare Erinnerungsliste an. |
| `spezial-livecheck-fristennotiz-und-naechster-schritt` | Livecheck: Fristennotiz und nächster Schritt im Plugin betreuungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Betreuungsrecht (§§ 1814 ff. BGB) gilt für **Betreuung Strafverfahren Kalender Reminder**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `betreuung-im-strafverfahren`

**Fokus:** Betreuung im Strafverfahren des Betroffenen: Schuldfaehigkeit nach §§ 20 und 21 StGB, Verteidigerbestellung, Vertretung Betreuer im Hauptverfahren. Schnittstelle Strafrecht und Betreuungsrecht.

# Betreuung im Strafverfahren

## Spezialwissen: Betreuung im Strafverfahren
- **Spezialgegenstand:** Betreuung im Strafverfahren / betreuung im strafverfahren. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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

## 2. `kalender-reminder-und-fristenmanagement`

**Fokus:** Kalender- und Reminder-Skill für Betreuungen: legt Berichtstermine, Vermögensverzeichnis, Rechnungslegung, Gerichtstermine, Bescheidfristen, Arzt-/Pflege-/Heimtermine, Genehmigungsentscheidungen und wiederkehrende Zahlungen als klare Erinnerungsliste an.

# Kalender, Reminder und Fristenmanagement

## Zweck

Dieser Skill sorgt dafür, dass der Betreuer nichts Wichtiges vergisst: nicht die gerichtlichen Berichte, nicht die Bescheidfristen, nicht den Heimvertrag, nicht die Pflegekasse, nicht die nächste Rücksprache mit der betreuten Person.

## Fristenquellen

Prüfe:

- Betreuungsbeschluss und gerichtliche Schreiben,
- Berichtspflicht nach § 1863 BGB,
- Vermögensverzeichnis nach § 1835 BGB,
- Rechnungslegung/Vermögensübersicht bei Vermögenssorge,
- sozialrechtliche Bescheide mit Widerspruchsfrist,
- Miet-/Heim-/Kündigungsfristen,
- Zahlungsziele und Mahnungen,
- gerichtliche Genehmigungsfristen und Anhörungstermine,
- Arzt-, Pflege-, Reha- und Entlassmanagement-Termine.

## Reminder-Logik

Erzeuge drei Ebenen:

| Ebene | Zweck | Beispiel |
| --- | --- | --- |
| Sofort | Frist droht oder Schaden wahrscheinlich | Widerspruch bis 14.06.2026 |
| Vorbereitung | Unterlagen müssen rechtzeitig gesammelt werden | Jahresbericht 6 Wochen vor Fälligkeit starten |
| Routine | Betreuung gut führen | monatlicher Konto- und Besuchscheck |

## Standard-Reminder

- Monatlich: Kontakt zur betreuten Person dokumentieren.
- Monatlich bei Vermögenssorge: Kontoauszüge prüfen und Belege sichern.
- Quartalsweise: Wohn-/Pflege-/Gesundheitslage prüfen.
- Halbjährlich: Aufgabenkreise noch erforderlich? Weniger Betreuung möglich?
- Jährlich: Jahresbericht vorbereiten; bei Vermögenssorge Vermögensübersicht/Rechnungslegung prüfen.
- Bei jedem neuen Bescheid: Rechtsbehelfsfrist sofort notieren.

## Ausgabeformat

```text
Fristen- und Erinnerungsliste

Rot:
- [Datum] [Aufgabe] [Folge bei Versäumnis] [zuständige Stelle]

Gelb:
- [Datum] [Vorbereitung] [fehlende Unterlagen]

Routine:
- [Rhythmus] [Aufgabe] [Beleg/Notiz]
```

## Arbeitsregel

Wenn ein echter Kalenderzugriff vorhanden ist, nur nach ausdrücklichem Auftrag Termine anlegen. Sonst eine exportierbare Liste im Klartext liefern.

## 3. `spezial-livecheck-fristennotiz-und-naechster-schritt`

**Fokus:** Livecheck: Fristennotiz und nächster Schritt im Plugin betreuungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Livecheck: Fristennotiz und nächster Schritt

## Spezialwissen: Livecheck: Fristennotiz und nächster Schritt
- **Spezialgegenstand:** Livecheck: Fristennotiz und nächster Schritt / livecheck fristennotiz und naechster schritt. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BtOG, BGB.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Livecheck** prüfen.
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
