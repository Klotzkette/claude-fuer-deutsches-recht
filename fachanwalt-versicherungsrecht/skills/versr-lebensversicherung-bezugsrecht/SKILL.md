---
name: versr-lebensversicherung-bezugsrecht
description: "Versr Lebensversicherung Bezugsrecht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Versr Lebensversicherung Bezugsrecht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Versr Lebensversicherung Bezugsrecht** im Plugin Fachanwalt Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `versr-lebensversicherung-bezugsrecht-bewertungsreserven` | Lebensversicherung: Bezugsrecht, Erbfall, Scheidung, Sicherungsabtretung, Rückkaufswert, Überschüsse und Bewertungsreserven. |
| `versr-obliegenheit-28-quotelung-kausalitaet` | Obliegenheitsverletzung nach § 28 VVG mit Vorsatz/grober Fahrlässigkeit, Rechtsfolgenbelehrung, Kausalitätsgegenbeweis und Quote. |
| `versr-obliegenheitsverletzung-praxis` | Obliegenheitsverletzung in der Praxis: § 28 VVG, Aufklaerungspflicht, Anzeigepflicht. Folgen Leistungsfreiheit bei Vorsatz, Quotelung bei grober Fahrlaessigkeit, Kausalitaetsgegenbeweis Versicherungsnehmer. Pruefraster Mandant. |

## Arbeitsweg

Im Plugin Fachanwalt Versicherungsrecht gilt für **Versr Lebensversicherung Bezugsrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `versr-lebensversicherung-bezugsrecht-bewertungsreserven`

**Fokus:** Lebensversicherung: Bezugsrecht, Erbfall, Scheidung, Sicherungsabtretung, Rückkaufswert, Überschüsse und Bewertungsreserven.

# FA Versicherungsrecht: Lebensversicherung Auszahlung

## Einsatz

Für Streit um Auszahlung, Kündigung oder Wertentwicklung von Lebensversicherungen.

## Norm- und Quellenanker

VVG §§ 150–171, §§ 159, 169; BGB Erbrecht/Abtretung; InsO.

## Arbeitsfragen

1. Wer ist bezugsberechtigt?
2. Welche Änderung/Abtretung gilt?
3. Wie wurde Rückkaufswert/Überschuss berechnet?

## Output

Bezugsrechts- und Wertememo mit Unterlagenanforderung.

## Red Flags

- alte Ehegattenbezeichnung
- Bankabtretung übersehen
- Schlussüberschuss als garantiert verstanden

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

## 2. `versr-obliegenheit-28-quotelung-kausalitaet`

**Fokus:** Obliegenheitsverletzung nach § 28 VVG mit Vorsatz/grober Fahrlässigkeit, Rechtsfolgenbelehrung, Kausalitätsgegenbeweis und Quote.

# FA Versicherungsrecht: § 28 VVG Quotierung

## Einsatz

Für Fälle, in denen Versicherer wegen verspäteter Anzeige, fehlender Mitwirkung oder Rettungsobliegenheit kürzen.

## Norm- und Quellenanker

VVG §§ 28, 30, 31, 82; AVB; BGB § 242.

## Arbeitsfragen

1. Welche Obliegenheit besteht wirklich?
2. Welche Belehrung gab es?
3. Welche Kausalität und Quote sind belegbar?

## Output

Quotierungs- und Beweislastmatrix mit Schriftsatzbaustein.

## Red Flags

- Totalablehnung ohne Kausalität
- Obliegenheit aus Kulanzbrief erfunden
- Quote ohne Tatsachen

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

## 3. `versr-obliegenheitsverletzung-praxis`

**Fokus:** Obliegenheitsverletzung in der Praxis: § 28 VVG, Aufklaerungspflicht, Anzeigepflicht. Folgen Leistungsfreiheit bei Vorsatz, Quotelung bei grober Fahrlaessigkeit, Kausalitaetsgegenbeweis Versicherungsnehmer. Pruefraster Mandant.

# Versr: Obliegenheitsverletzung

## Spezialwissen: Versr: Obliegenheitsverletzung
- **Spezialgegenstand:** Versr: Obliegenheitsverletzung / versr obliegenheitsverletzung praxis. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** VVG.
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
