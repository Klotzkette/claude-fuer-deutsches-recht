---
name: jahresfrist-abs-nkbl-verfahren
description: "Jahresfrist ABS Nkbl Verfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Jahresfrist ABS Nkbl Verfahren

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Jahresfrist ABS Nkbl Verfahren** im Plugin Normenkontrolle Bauleitplanung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin normenkontrolle-bauleitplanung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `jahresfrist-47-abs-2-vwgo` | Mandant moechte Normenkontrollantrag stellen und Anwalt prüft ob die Jahresfrist noch laeuft. § 47 Abs. 2 S. 1 VwGO Jahresfrist Normenkontrolle. Prüfraster: Fristbeginn ortsuebliche Bekanntmachung § 10 Abs. 3 BauGB fehlerhafte Bekanntmachung kein Fristbeginn Wiedereinsetzung § 60 VwGO ergaenzendes Verfahren § 214 Abs. 4 BauGB setzt neue Frist. Ruegefrist § 215 BauGB ein Jahr parallel. Output: Fristberechnung Normenkontrolle und Fristenbuch-Eintrag. Abgrenzung zu antragsbefugnis-eigentuemer-nachbar (Befugnis) und planerhaltung-214-215-baugb. |
| `nkbl-normenkontrolle-verfahren-leitfaden` | Leitfaden Normenkontrollverfahren § 47 VwGO: Antragsbefugnis, Antragsfrist, Pruefungsumfang. Pruefraster fuer Antragsteller und Gemeinde. |

## Arbeitsweg

Im Plugin Normenkontrolle Bauleitplanung gilt für **Jahresfrist ABS Nkbl Verfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin normenkontrolle-bauleitplanung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin normenkontrolle-bauleitplanung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `jahresfrist-47-abs-2-vwgo`

**Fokus:** Mandant moechte Normenkontrollantrag stellen und Anwalt prüft ob die Jahresfrist noch laeuft. § 47 Abs. 2 S. 1 VwGO Jahresfrist Normenkontrolle. Prüfraster: Fristbeginn ortsuebliche Bekanntmachung § 10 Abs. 3 BauGB fehlerhafte Bekanntmachung kein Fristbeginn Wiedereinsetzung § 60 VwGO ergaenzendes Verfahren § 214 Abs. 4 BauGB setzt neue Frist. Ruegefrist § 215 BauGB ein Jahr parallel. Output: Fristberechnung Normenkontrolle und Fristenbuch-Eintrag. Abgrenzung zu antragsbefugnis-eigentuemer-nachbar (Befugnis) und planerhaltung-214-215-baugb.

# Jahresfrist § 47 Abs. 2 VwGO

## Zweck

Die Jahresfrist ist die dritte Zulässigkeitssäule und zugleich die schärfste materielle Falle. Wer sie versäumt, kann nur noch über fehlerhafte Bekanntmachung oder Wiedereinsetzung retten.

## Schritt 1 — Wortlaut und Grundregel

### § 47 Abs. 2 S. 1 VwGO
- Der Antrag kann innerhalb eines Jahres nach Bekanntmachung der Rechtsvorschrift gestellt werden

### Frist-Verkürzung 2007
- Vor dem 1.1.2007 zwei Jahre
- Durch Gesetz vom 22.12.2006 auf ein Jahr verkürzt
- Übergangsfristen längst abgelaufen

## Schritt 2 — Fristbeginn Bekanntmachung

### Bekanntmachung des B-Plans § 10 Abs. 3 BauGB
- Der Beschluss als Satzung ist ortsüblich bekanntzumachen
- In Bayern regelmäßig Veröffentlichung im Amtsblatt der Gemeinde
- Oder in der Tageszeitung, wenn Hauptsatzung dies vorsieht
- Online-Veröffentlichung zusätzlich, aber nicht allein konstitutiv

### Was wird bekanntgemacht
- Beschluss als Satzung
- Anstoßfunktion: Hinweis wo der Plan einsehbar ist
- Hinweis auf Beachtlichkeit der Verletzung von Vorschriften nach § 215 BauGB
- Hinweis auf Voraussetzungen für Entschädigungsanspruch § 44 BauGB
- Hinweis auf nachträgliche Geltendmachung

### Fehlerhafte Bekanntmachung
- Bei Fehlen der Hinweise auf § 215 BauGB läuft die Rügefrist nicht (§ 215 Abs. 2 BauGB)
- Bei vollständig fehlerhafter Bekanntmachung (z.B. unrichtiger Ort, fehlende Anstoßfunktion) kein Fristbeginn der Jahresfrist
- BVerwG ständige Rechtsprechung — gute Angriffsfläche

## Schritt 3 — Fristberechnung

### Fristbeginn
- Tag der Bekanntmachung zählt nicht mit (§ 187 Abs. 1 BGB analog)
- Bei Veröffentlichung 12.6.2024 läuft die Frist ab 13.6.2024

### Fristende
- Genau ein Jahr nach Beginn (§ 188 Abs. 2 BGB analog)
- Bekanntmachung 12.6.2024 — Fristende 12.6.2025, 24 Uhr
- Wenn Fristende auf Samstag, Sonntag oder Feiertag fällt — nächster Werktag (§ 222 Abs. 2 ZPO i.V.m. § 173 VwGO)

### Praxis Fristenkalender
- Eintrag Hauptfrist
- Vorfrist 1: 2 Wochen vor Ablauf
- Vorfrist 2: 4 Wochen vor Ablauf
- Drei-Augen-Kontrolle Vorlage Anwältin

## Schritt 4 — Antragseingang § 47 VwGO

### Form
- Schriftsatz an das zuständige OVG/VGH (Bayern: BayVGH)
- Eingang Original oder elektronischer Schriftsatz § 55a VwGO über beA
- Eingangsstempel maßgeblich

### Adressat
- BayVGH-Geschäftsstelle München
- bei elektronischer Übermittlung beA an die jeweilige Senatsgeschäftsstelle

## Schritt 5 — Wiedereinsetzung in den vorigen Stand

### § 60 VwGO
- Wiedereinsetzung bei unverschuldeter Versäumung
- Antrag innerhalb von zwei Wochen nach Wegfall des Hindernisses
- Glaubhaftmachung der Wiedereinsetzungstatsachen
- Nachholung der versäumten Handlung innerhalb der Antragsfrist

### Verschulden Mandant / Anwalt
- Anwaltsverschulden wird Mandanten zugerechnet § 173 VwGO i.V.m. § 85 Abs. 2 ZPO
- Bei Fristversäumung durch Anwältin Wiedereinsetzung in der Regel ausgeschlossen — Haftungsfrage

### Höhere Gewalt
- Plötzliche schwere Erkrankung
- Postsendung durch Naturkatastrophe vereitelt
- Betrug oder Täuschung durch Behörde

## Schritt 6 — Heilung durch ergänzendes Verfahren

### § 214 Abs. 4 BauGB
- Mängel können durch ergänzendes Verfahren behoben werden
- Erneuter Beschluss, erneute Bekanntmachung
- Neue Jahresfrist beginnt mit neuer Bekanntmachung
- Aber nur soweit der ergänzte Plan reicht

### Strategische Konsequenz
- Wenn Plan kurz vor Klagefrist nochmals "geheilt" wird — Frist beginnt neu
- Wenn Heilungsversuch unzureichend ist — Angriffspunkt im Hauptsacheverfahren

## Schritt 7 — Parallelfrist § 215 BauGB

### Rügefrist Verfahrensfehler
- Beachtliche Mängel des Verfahrens und der Form werden unbeachtlich, wenn sie nicht innerhalb eines Jahres nach Bekanntmachung schriftlich gegenüber der Gemeinde gerügt werden
- § 215 Abs. 1 Nr. 1 BauGB
- Gilt für formelle Mängel, die nicht ohnehin nach § 214 Abs. 1 BauGB unbeachtlich sind

### Rügefrist Abwägungsfehler
- § 215 Abs. 1 Nr. 3 BauGB
- Mängel im Abwägungsvorgang werden unbeachtlich, wenn nicht binnen Jahresfrist gerügt
- Materielle Abwägungsergebnis-Fehler bleiben unbeachtlich-Frei

### Rüge-Adressat
- Schriftliche Rüge gegenüber der Gemeinde, nicht gegenüber dem Gericht
- Eingang bei der Stadtverwaltung zählt
- Trotzdem zeitgleich mit Normenkontrollantrag vorbereiten

### Hinweis-Erfordernis
- Frist läuft nur, wenn auf sie in Bekanntmachung hingewiesen wurde
- Fehlt Hinweis — keine Rügefrist (§ 215 Abs. 2 BauGB)

## Schritt 8 — Praxisablauf

### Tag 0 — Mandatsannahme
- Bekanntmachungsdatum erfassen
- Hauptfrist und Rügefrist berechnen
- Fristenkalender Eintrag mit Vorfristen

### Phase 1 — Verfahrenskette und Akteneinsicht
- Akteneinsicht bei der Gemeinde § 29 VwVfG (BayVwVfG)
- Vorbereitung Rügeschreiben § 215 BauGB

### Phase 2 — Rüge absenden
- 4 Wochen vor Ablauf Jahresfrist: Rüge per Einschreiben an Gemeinde
- Rüge enthält alle erkannten Verfahrens- und Abwägungsfehler
- Aufbewahrung Postzustellungsurkunde

### Phase 3 — Normenkontrollantrag
- 2 Wochen vor Ablauf Jahresfrist: Schriftsatz bei BayVGH
- Eingang über beA mit Empfangsbekenntnis

## Schritt 9 — Häufige Fristfehler

- Fristbeginn auf Aufstellungsbeschluss statt Bekanntmachung gesetzt — falsch
- Bekanntmachung im Internet statt Amtsblatt als Fristbeginn — abhängig von Hauptsatzung
- Rügefrist § 215 BauGB übersehen — materielle Präklusion
- Vorfristen nicht eingetragen — Risiko bei Krankheit
- Eingang per Fax am Freitagabend ohne Eingangsbestätigung — Beweisproblem

## Quellen

- VwGO § 47 Abs. 2, § 55a, § 60, § 173
- BauGB § 10 Abs. 3, § 214, § 215, § 44
- ZPO § 85 Abs. 2, § 222 Abs. 2
- BGB § 187 Abs. 1, § 188 Abs. 2
- BVerwG, Urteil vom 26.4.2007 – 4 CN 3.06 (Bekanntmachung)
- BVerwG, Beschluss vom 15.4.1988 – 4 N 4.87 (Anstoßfunktion)

## Ergänzende Rechtsprechung (Stand 05/2026)

- **BVerwG 17.06.2020, 4 CN 6.18**: Anforderungen an die Bekanntmachung von Bebauungsplaenen — Anstossfunktion und Fristbeginn § 47 Abs. 2 VwGO. Quelle: bverwg.de.
- **BVerwG 03.04.2020, 4 CN 2.19** (Erhaltungssatzung): Bekanntmachung und Fristbeginn fuer den Normenkontrollantrag. Quelle: bverwg.de.
- **OVG NRW** und andere OVG/VGH: laufende Rspr. zu Bekanntmachungsmaengeln und Frist; konkrete Aktenzeichen ueber landesrecht-nrw.de bzw. die jeweilige Landesjustiz-Datenbank verifizieren.

Vor Ausgabe per bverwg.de mit Datum und Aktenzeichen verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `nkbl-normenkontrolle-verfahren-leitfaden`

**Fokus:** Leitfaden Normenkontrollverfahren § 47 VwGO: Antragsbefugnis, Antragsfrist, Pruefungsumfang. Pruefraster fuer Antragsteller und Gemeinde.

# NkBl: Normenkontrolle-Verfahren

## Spezialwissen: NkBl: Normenkontrolle-Verfahren
- **Spezialgegenstand:** NkBl: Normenkontrolle-Verfahren / nkbl normenkontrolle verfahren leitfaden. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** VwGO, BGH, BVerfG.
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
