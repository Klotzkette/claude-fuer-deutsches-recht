---
name: mangelhaftung-symptomtheorie-bautraeger
description: "Mangelhaftung Symptomtheorie Bautraeger: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mangelhaftung Symptomtheorie Bautraeger

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Mangelhaftung Symptomtheorie Bautraeger** im Plugin Fachanwalt Bau- und Architektenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bau-mangelhaftung-spezial-symptomtheorie` | Spezialfall Symptomtheorie BGH zur Mangelruege: Beschreibung Symptom statt Ursache reicht, Bauherr muss nicht Ursache benennen. Konkretisierung der Mangelruege, Ausuebung Recht der Mangelbeseitigung. Pruefraster fuer Schriftsatz. |
| `bautraeger-haftungsausschluss-307-bgb` | Bautraeger-Haftungsausschluss und § 307 BGB. Skill klaert welche Haftungsklauseln im Bautraegervertrag wirksam und welche unwirksam sind insbesondere Maengelausschluss Haftungsbegrenzung Kardinalpflichten-Verletzung. Liefert Pruefraster. |
| `bautraeger-maengelhaftung-fuenf-jahre-634a` | Bautraeger-Maengelhaftung 5 Jahre nach § 634a BGB. Skill klaert die Verjaehrungsfrist Bauwerk Beginn der Frist (Abnahme) Hemmung Unterbrechung sowie die Kategorisierung der Maengel offene und versteckte. Liefert Pruefraster. |
| `spezial-maengelhaftung-verhandlung-vergleich-und-eskalation` | Maengelhaftung: Verhandlung, Vergleich und Eskalation im Plugin fachanwalt bau architektenrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Fachanwalt Bau- und Architektenrecht gilt für **Mangelhaftung Symptomtheorie Bautraeger**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bau-mangelhaftung-spezial-symptomtheorie`

**Fokus:** Spezialfall Symptomtheorie BGH zur Mangelruege: Beschreibung Symptom statt Ursache reicht, Bauherr muss nicht Ursache benennen. Konkretisierung der Mangelruege, Ausuebung Recht der Mangelbeseitigung. Pruefraster fuer Schriftsatz.

# Bau: Symptomtheorie-Mangelruege

## Spezialwissen: Bau: Symptomtheorie-Mangelruege
- **Spezialgegenstand:** Bau: Symptomtheorie-Mangelruege / bau mangelhaftung symptomtheorie. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGH.
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

## 2. `bautraeger-haftungsausschluss-307-bgb`

**Fokus:** Bautraeger-Haftungsausschluss und § 307 BGB. Skill klaert welche Haftungsklauseln im Bautraegervertrag wirksam und welche unwirksam sind insbesondere Maengelausschluss Haftungsbegrenzung Kardinalpflichten-Verletzung. Liefert Pruefraster.

# Bautraeger Haftungsausschluss 307 Bgb

## Norm

§ 307 BGB Inhaltskontrolle.

## Unwirksame Klauseln

### Pauschaler Haftungsausschluss
- "Wir haften nicht fuer Maengel, soweit sie nicht erkennbar waren."
- Unwirksam — Maengelhaftung darf nicht ueber § 634 BGB hinausgehend ausgeschlossen werden.

### Maengelpauschalierung
- "Bei Maengeln ist statt Beseitigung nur eine Pauschale zu zahlen."
- Unwirksam.

### Verkuerzung der Verjaehrung
- "Maengelansprueche verjaehren in 2 Jahren."
- Unwirksam — § 634a BGB beim Bauwerk 5 Jahre zwingend.

### Ausschluss fuer einfache Fahrlaessigkeit
- "Wir haften nur fuer Vorsatz und grobe Fahrlaessigkeit."
- Unwirksam bei Verletzung Leben Koerper Gesundheit (§ 309 Nr. 7a BGB).
- Bei sonstigen Schaeden: unwirksam, wenn Kardinalpflicht beruehrt.

## Wirksame Klauseln

### Haftungsbegrenzung auf Versicherungsdeckung
- "Wir haften nur in Hoehe der Versicherungsdeckung." — meist unwirksam.

### Begrenzung auf vertragstypische vorhersehbare Schaeden
- Wirksam bei einfacher Fahrlaessigkeit.

## Pruefraster

1. Welche Klausel?
2. § 307 / § 309 / § 634a BGB Verstoss?
3. Kardinalpflicht beruehrt?

## 3. `bautraeger-maengelhaftung-fuenf-jahre-634a`

**Fokus:** Bautraeger-Maengelhaftung 5 Jahre nach § 634a BGB. Skill klaert die Verjaehrungsfrist Bauwerk Beginn der Frist (Abnahme) Hemmung Unterbrechung sowie die Kategorisierung der Maengel offene und versteckte. Liefert Pruefraster.

# Bautraeger Maengelhaftung Fuenf Jahre 634A

## Norm

§ 634a Abs. 1 Nr. 2 BGB: Verjaehrungsfrist fuer Maengelansprueche bei Bauwerk 5 Jahre.

## Beginn

- Mit Abnahme (foerm- oder konkludent).
- Bei Verweigerung der Abnahme: keine Verjaehrung.

## Hemmung

- §§ 203, 204 BGB: Verhandlungen, Mahnverfahren, Klage, selbstaendiges Beweisverfahren.

## Maengelarten

### Offene Maengel
- Bei Abnahme erkennbar.
- Bei Abnahme ohne Vorbehalt: rechte verloren.

### Versteckte Maengel
- Bei Abnahme nicht erkennbar.
- Verjaehrung erst mit Entdeckung beginnt nicht — die 5 Jahre laufen ab Abnahme.

### Arglistig verschwiegene Maengel
- Verjaehrung in 10 Jahren (§ 634a Abs. 3 BGB iVm § 199 BGB).

## Pruefraster

1. Wann wurde abgenommen?
2. Wann wurde Mangel entdeckt?
3. Vorbehalt erklaert?
4. Arglist vermutet?

## 4. `spezial-maengelhaftung-verhandlung-vergleich-und-eskalation`

**Fokus:** Maengelhaftung: Verhandlung, Vergleich und Eskalation im Plugin fachanwalt bau architektenrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Maengelhaftung: Verhandlung, Vergleich und Eskalation

## Spezialwissen: Maengelhaftung: Verhandlung, Vergleich und Eskalation
- **Spezialgegenstand:** Maengelhaftung: Verhandlung, Vergleich und Eskalation / maengelhaftung verhandlung vergleich und eskalation. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB, VOB, HOAI.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Maengelhaftung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen Mängelhaftung Bauvertrag
- **Mangelbegriff (§ 633 BGB):** Sach- oder Rechtsmangel. Sachmangel: Werk weicht von vereinbarter Beschaffenheit ab, ist für vertragliche oder gewöhnliche Verwendung nicht geeignet, fehlerhafte Montage. Rechtsmangel: Dritte können Rechte gegen den Besteller geltend machen.
- **Mängelansprüche-Kaskade (§ 634 BGB):** (1) Nacherfüllung (§ 635 BGB) - vorrangig. (2) Selbstvornahme (§ 637 BGB) nach Fristsetzung. (3) Rücktritt (§ 636 i.V.m. §§ 323, 326 Abs. 5 BGB). (4) Minderung (§ 638 BGB). (5) Schadenersatz statt der Leistung (§§ 280, 281 BGB) oder neben (§ 280 Abs. 1 BGB).
- **Fristsetzung erforderlich:** Vor Selbstvornahme, Rücktritt, Minderung und Schadensersatz statt der Leistung muss dem AN eine angemessene Nachfrist zur Nacherfüllung gesetzt werden. Entbehrlich bei ernsthafter und endgültiger Erfüllungsverweigerung (§ 281 Abs. 2 BGB) oder Unzumutbarkeit der Nacherfüllung (§ 636 BGB).
- **Verjährung (§ 634a BGB):** Bauwerke 5 Jahre, sonstige Werke 2 Jahre, geistige Werke 2 Jahre. Beginn mit Abnahme. Bei arglistig verschwiegenen Mängeln 3 Jahre ab Kenntnis, höchstens 10 Jahre ab Abnahme (§ 634a Abs. 3 BGB).
- **VOB/B (§ 13 VOB/B):** Modifizierte Mängelhaftung. Verjährung Bauwerke 4 Jahre, Außenanlagen 2 Jahre, sonstige 2 Jahre (§ 13 Abs. 4 VOB/B). VOB/B muss als Ganzes vereinbart sein - jede Abweichung im Einzelfall führt zur AGB-Kontrolle der einzelnen Klausel.
- **Beweislast vor Abnahme:** AN trägt Beweis der vertragsgemäßen Erbringung. Nach Abnahme: AG trägt Mangelbeweis (§ 363 BGB Beweislastumkehr durch Abnahme; BGH ständige Rspr.).
- **Symptomtheorie (BGH ständige Rspr.):** Mängelrüge muss nur das Symptom (z. B. "Wasser dringt ein") benennen, nicht die Ursache. Die Suche nach der Ursache ist Sache des AN. Wichtig: Es genügt nicht "Mängelbehebung wird verlangt", konkrete Symptombeschreibung ist erforderlich.
- **Vorschuss für Mangelbeseitigung (§ 637 Abs. 3 BGB):** AG kann nach erfolgloser Fristsetzung Vorschuss für die voraussichtlichen Kosten verlangen. Wichtige Praxisoption zur Liquiditätssicherung.
- **Selbständiges Beweisverfahren (§§ 485 ff. ZPO):** Empfohlen bei drohendem Beweisverlust (Sanierung, Veränderung des Mangels). Hemmt die Verjährung. Anwaltszwang nur ab LG.

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
