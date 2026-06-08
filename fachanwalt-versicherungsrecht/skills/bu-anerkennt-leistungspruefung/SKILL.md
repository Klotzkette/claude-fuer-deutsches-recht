---
name: bu-anerkennt-leistungspruefung
description: "Versr BU Anerkennt Leistungspruefung im Plugin Fachanwalt Versicherungsrecht: prüft konkret Spezialfall Berufsunfaehigkeitsversicherung, Spezialfall BU-Leistungspruefung, BU-Anerkenntnis, Nachprüfung und Leistungseinstellung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Versr BU Anerkennt Leistungspruefung

## Arbeitsbereich

**Versr BU Anerkennt Leistungspruefung** ordnet den Fall über die tragenden Prüfungslinien: Spezialfall Berufsunfaehigkeitsversicherung, Spezialfall BU-Leistungspruefung, BU-Anerkenntnis. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `versr-bu-anerkennt-was-spezial` | Spezialfall Berufsunfaehigkeitsversicherung: Anerkennungsfaktum aktive Versicherung gegen Nachpruefung, konkrete und abstrakte Verweisung, 50-Prozent-BU. Beispielfall Streit ueber Anerkenntnis und Wiedereinsetzung der Leistung. |
| `versr-bu-leistungspruefung-spezial` | Spezialfall BU-Leistungspruefung: Berufsbeschreibung, 50-Prozent-Grenze, Mitwirkungspflichten, Nachpruefungsverfahren. Pruefraster für Versicherungsnehmer mit psychischer und somatischer Erkrankung. |
| `versr-bu-nachpruefung-anerkenntnis` | BU-Anerkenntnis, Nachprüfung und Leistungseinstellung: Vergleichszustand, Gesundheitsverbesserung, Berufswechsel, Mitwirkung und Prozessstrategie. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `versr-bu-anerkennt-was-spezial`

**Fokus:** Spezialfall Berufsunfaehigkeitsversicherung: Anerkennungsfaktum aktive Versicherung gegen Nachpruefung, konkrete und abstrakte Verweisung, 50-Prozent-BU. Beispielfall Streit ueber Anerkenntnis und Wiedereinsetzung der Leistung.

# Versr: BU-Anerkennt

## Spezialwissen: Versr: BU-Anerkennt
- **Normen-/Quellenanker:** BU.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
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
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behördenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `versr-bu-leistungspruefung-spezial`

**Fokus:** Spezialfall BU-Leistungspruefung: Berufsbeschreibung, 50-Prozent-Grenze, Mitwirkungspflichten, Nachpruefungsverfahren. Pruefraster für Versicherungsnehmer mit psychischer und somatischer Erkrankung.

# VersR: BU-Leistungspruefung

## Spezialwissen: VersR: BU-Leistungspruefung
- **Normen-/Quellenanker:** BU.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

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
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `versr-bu-nachpruefung-anerkenntnis`

**Fokus:** BU-Anerkenntnis, Nachprüfung und Leistungseinstellung: Vergleichszustand, Gesundheitsverbesserung, Berufswechsel, Mitwirkung und Prozessstrategie.

# FA Versicherungsrecht: BU-Nachprüfung

## Einsatz

Für laufende BU-Renten, die nach Nachprüfung gefährdet sind.

## Norm- und Quellenanker

VVG §§ 172–177; AVB BU; ZPO; medizinischer Sachverständigenbeweis.

## Arbeitsfragen

1. Was wurde anerkannt?
2. Welche Änderung behauptet der Versicherer?
3. Ist die Nachprüfungsmitteilung formal und materiell tragfähig?

## Output

Nachprüfungsabwehr, medizinisches Fragenraster und Klageoption.

## Red Flags

- neue Tätigkeit ohne Lebensstellungsprüfung
- Besserung nur aus Aktenlage
- befristetes Anerkenntnis falsch behandelt

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 28 VVG
- § 14 VVG
- § 19 VVG
- § 81 VVG
- § 215 VVG
- § 86 VVG
- § 1 VVG
- § 261 StGB
- § 43 GmbHG
- § 203 VVG
- § 21 VVG
- § 84 VVG

### Leitentscheidungen

- BGH IV ZR 32/24
- BGH IV ZR 70/25
- BGH IV ZR 86/24
- BGH IV ZR 153/20

