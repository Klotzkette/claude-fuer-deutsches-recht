---
name: versr-deckungsprozess-vvg-einfuehrung-themen
description: "Versr Deckungsprozess VVG Einfuehrung Themen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Versr Deckungsprozess VVG Einfuehrung Themen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Versr Deckungsprozess VVG Einfuehrung Themen** im Plugin Fachanwalt Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `versr-deckungsprozess-215-vvg-beweislast` | Deckungsklage: Gerichtsstand § 215 VVG, Klageart, Beweislast, Sachverständige, Streitwert und Vergleichsfenster. |
| `versr-einfuehrung-themen` | Versicherungsrecht einfuehrend: Lebens-, Berufsunfaehigkeits-, Unfall-, Krankenversicherung, KFZ-Haftpflicht, Wohngebaeude, Hausrat, Rechtsschutz, gewerbliche Sparten. Entscheidungstabelle und Verweis auf Detail-Skills. |
| `versr-kreditausfall-restschuldversicherung` | Kreditausfall-, Warenkredit- und Restschuldversicherung: Limit, Ausfall, Obliegenheiten, Verbraucherdarlehen, Kopplung und Widerruf. |

## Arbeitsweg

Im Plugin Fachanwalt Versicherungsrecht gilt für **Versr Deckungsprozess VVG Einfuehrung Themen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `versr-deckungsprozess-215-vvg-beweislast`

**Fokus:** Deckungsklage: Gerichtsstand § 215 VVG, Klageart, Beweislast, Sachverständige, Streitwert und Vergleichsfenster.

# FA Versicherungsrecht: Deckungsprozess § 215 VVG

## Einsatz

Für die prozessuale Übersetzung der Deckungsprüfung in Klage oder Klageerwiderung.

## Norm- und Quellenanker

- VVG §§ 1, 14, 28, 31, 81, 82, 86, 215 je nach Deckungsstreit: Leistung, Fälligkeit, Obliegenheit, Gefahrerhöhung, Herbeiführung, Rettungskosten/Regress.
- ZPO §§ 253, 256, 286, 402 ff. für Leistungs-/Feststellungsklage, Beweiswürdigung und Sachverständige.
- AVB/Besondere Bedingungen/Police/Nachträge haben Vorrang vor Produktbezeichnungen; Deckung und Haftpflicht nicht vermischen.
- VVG § 215 ist Gerichtsstand, kein materieller Anspruch; lokale Zuständigkeit und Verbraucher-/Versicherungsnehmerrolle sauber prüfen.

## Arbeitsfragen

1. Leistung oder Feststellung?
2. Welches Gericht?
3. Welche Beweise sind anknüpfungsfähig?
4. Wer trägt Beweislast für Versicherungsfall, Ausschluss, Obliegenheitsverletzung, Kausalität und Verschulden?
5. Ist die Leistung fällig oder fehlt noch eine zulässige Auskunft/Beleganforderung?
6. Muss ein Haftpflichtprozess verteidigt, ein Deckungsprozess geführt oder beides koordiniert werden?

## Output

Klagegerüst, Beweisplan und Streitwertnotiz.

## Red Flags

- Antrag unbestimmt
- Haftung und Deckung vermischt
- falscher Gerichtsstand

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

## 2. `versr-einfuehrung-themen`

**Fokus:** Versicherungsrecht einfuehrend: Lebens-, Berufsunfaehigkeits-, Unfall-, Krankenversicherung, KFZ-Haftpflicht, Wohngebaeude, Hausrat, Rechtsschutz, gewerbliche Sparten. Entscheidungstabelle und Verweis auf Detail-Skills.

# Versicherungsrecht: Themen

## Spezialwissen: Versicherungsrecht: Themen
- **Spezialgegenstand:** Versicherungsrecht: Themen / versr einfuehrung themen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KFZ.
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

## 3. `versr-kreditausfall-restschuldversicherung`

**Fokus:** Kreditausfall-, Warenkredit- und Restschuldversicherung: Limit, Ausfall, Obliegenheiten, Verbraucherdarlehen, Kopplung und Widerruf.

# FA Versicherungsrecht: Kredit- und Restschuldversicherung

## Einsatz

Für Lieferanten, Banken und Verbraucher bei Forderungsausfall oder Darlehensabsicherung.

## Norm- und Quellenanker

VVG; BGB §§ 491 ff.; InsO; HGB; VersVermV/IDD.

## Arbeitsfragen

1. Welches Limit/versicherter Fall?
2. Welche Melde- und Inkassoobliegenheiten?
3. War Restschuldversicherung transparent gekoppelt?

## Output

Limit-/Ausfallmatrix und Widerrufs-/Leistungsprüfung.

## Red Flags

- Lieferung nach Limitstreichung
- Mahnobliegenheit verletzt
- Kosten im Darlehen versteckt

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.
