---
name: ustva-aufsichtskommunikation-grundregeln-dora
description: "Ustva Aufsichtskommunikation Grundregeln Dora: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ustva Aufsichtskommunikation Grundregeln Dora

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ustva Aufsichtskommunikation Grundregeln Dora** im Plugin Regulatorisches Recht (Sektoren). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ustva` | Umsatzsteuervoranmeldung im regulatorischen Kontext prüfen wenn Finanzunternehmen oder regulierte Entitaeten USt-Fragen haben. §§ 14 14a 18 UStG Voranmeldungspflicht. Prüfraster: Voranmeldungspflicht Steuerklasse Vorsteuer Fristen Sondervorauszahlung. Output: USt-Prüfprotokoll Voranmeldungs-Checkliste. Abgrenzung: nicht für allgemeines Steuerrecht. |
| `aufsichtskommunikation-grundregeln` | Grundregeln Aufsichtskommunikation: Mitteilungspflichten, Auskunftsrechte, Sonderpruefung, Anhoerung, Bussgeldverfahren. Tonfall, Tempo, Vollstaendigkeit, Konsistenz Schriftverkehr. Pruefraster fuer Antworten an BaFin, BNetzA, Bundeskartellamt. Mustertexte. |
| `dora-stellvertreter-und-konzern` | DORA-Spezial: Stellvertreter, Konzernregelungen, Outsourcing zum gruppeneigenen IT-Dienstleister, kritische TPP-Registrierung bei ESAs. Pruefraster und Klauseln in Konzern-IT-Vertraegen. Schnittstelle zu Aufsichtsrecht der Toechter im Ausland. |

## Arbeitsweg

Im Plugin Regulatorisches Recht (Sektoren) gilt für **Ustva Aufsichtskommunikation Grundregeln Dora**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ustva`

**Fokus:** Umsatzsteuervoranmeldung im regulatorischen Kontext prüfen wenn Finanzunternehmen oder regulierte Entitaeten USt-Fragen haben. §§ 14 14a 18 UStG Voranmeldungspflicht. Prüfraster: Voranmeldungspflicht Steuerklasse Vorsteuer Fristen Sondervorauszahlung. Output: USt-Prüfprotokoll Voranmeldungs-Checkliste. Abgrenzung: nicht für allgemeines Steuerrecht.

# Umsatzsteuer-Voranmeldung (§ 18 UStG)

## Zweck

Dieser Skill begleitet die fristgerechte und inhaltlich korrekte Abgabe von Umsatzsteuer-Voranmeldungen (UStVA) nach § 18 UStG. Er deckt die Bestimmung des richtigen Voranmeldungszeitraums, die Dauerfristverlängerung nach § 46 UStDV, die Berichtigung nach §§ 153 AO und 17 UStG sowie die technische Abgabe über ELSTER ab. Anwendungsfälle: monatliche oder quartalsweise UStVA erstellen, Dauerfristverlängerung beantragen, versehentlich falsche UStVA berichtigen, Übergang zwischen Voranmeldungszeiträumen.

## Eingaben

Das Modell benötigt:

- **Voranmeldungszeitraum des Mandanten**: monatlich, quartalsweise oder jährlich (Befreiung)?
- **Vorjahres-Zahllast**: Wie hoch war die USt-Zahllast des Vorjahres? (Maßgeblich für Zeitraum-Bestimmung)
- **Aktueller Zeitraum**: Welcher Monat/welches Quartal wird gemeldet?
- **Abzugebende Daten**: Umsätze (Steuersatz, steuerfreie Umsätze), Vorsteuer, innergemeinschaftliche Erwerbe, Reverse Charge?
- **Dauerfristverlängerung**: Beantragt? Sondervorauszahlung bereits entrichtet?
- **Berichtigungsbedarf**: Liegt ein Fehler in einer bereits abgegebenen UStVA vor? Welcher Art (Betrag, Steuersatz, Vorsteuer)?
- **ELSTER-Zugang**: Besteht ein zertifizierter ELSTER-Zugang (Unternehmen)?

## Rechtlicher Rahmen

### Primärnormen

- **§ 18 Abs. 1 UStG**: Pflicht zur Abgabe der UStVA; Voranmeldungszeitraum grundsätzlich das Kalendervierteljahr; bei Jahres-Zahllast > 7.500 EUR: Kalendermonat (§ 18 Abs. 2 Satz 2 UStG); bei Jahres-Zahllast ≤ 1.000 EUR: Finanzamt kann von monatlicher/quartalsweiser Abgabe befreien (§ 18 Abs. 2 Satz 3 UStG).
- **§ 18 Abs. 1 Satz 4 UStG**: Abgabefrist: 10. Tag nach Ablauf des Voranmeldungszeitraums (10. Folgemonat).
- **§ 18 Abs. 2a UStG**: Neugründer: In den ersten zwei Jahren Monatsmeldung, unabhängig von Zahllast.
- **§ 18 Abs. 9 UStG**: Vergütungsverfahren für ausländische Unternehmer.
- **§ 46 UStDV (Dauerfristverlängerung)**: Verlängerung der Abgabe- und Zahlungsfrist um einen Monat auf Antrag; Voraussetzung für Monatszahler: Sondervorauszahlung i.H.v. 1/11 der Jahresvorauszahlung des Vorjahres bis zum 10. Februar des laufenden Jahres (§ 47 Abs. 1 UStDV); Quartalszahler: kein Sondervorauszahlungserfordernis.
- **§ 153 Abs. 1 AO**: Berichtigungspflicht bei erkanntem Fehler in einer Steuererklärung/-anmeldung; unverzügliche Anzeige beim Finanzamt, kein Verschulden erforderlich; Berichtigung = Selbstanzeige i.S.d. § 371 AO bei vorsätzlicher Verkürzung (Abgrenzung!).
- **§ 17 UStG**: Berichtigung des Steuerbetrags bei nachträglicher Änderung der Bemessungsgrundlage (z.B. Entgeltminderung, Rechnungskorrektur, Uneinbringlichkeit).

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

**Schritt 1 – Voranmeldungszeitraum bestimmen**
- Vorjahres-Zahllast ≤ 1.000 EUR: Befreiung möglich (§ 18 Abs. 2 Satz 3 UStG); Finanzamt entscheidet.
- Vorjahres-Zahllast > 1.000 EUR und ≤ 7.500 EUR: Quartalsmeldung (§ 18 Abs. 2 Satz 1 UStG).
- Vorjahres-Zahllast > 7.500 EUR: Monatsmeldung (§ 18 Abs. 2 Satz 2 UStG).
- Neugründer: erste zwei Kalenderjahre stets monatlich (§ 18 Abs. 2a UStG).

**Schritt 2 – Abgabefrist ermitteln**
- Regulär: 10. Tag nach Ablauf des Voranmeldungszeitraums (§ 18 Abs. 1 Satz 4 UStG).
- Beispiel: Januar-UStVA → Abgabe bis 10. Februar.
- Dauerfristverlängerung (§ 46 UStDV): Frist verschiebt sich um einen Monat (Januar → 10. März).
- Samstag/Sonntag/Feiertag: nächster Werktag (§ 108 Abs. 3 AO).

**Schritt 3 – Dauerfristverlängerung beantragen/sichern (§ 46 UStDV)**
- Antrag über ELSTER (Formular "Antrag auf Dauerfristverlängerung/Anmeldung der Sondervorauszahlung").
- Monatszahler: Sondervorauszahlung bis 10. Februar des Jahres entrichten (1/11 der Vorjahres-Zahllast).
- Quartalszahler: Antrag genügt, keine Sondervorauszahlung erforderlich.
- Sondervorauszahlung wird in der Dezember-UStVA/Jahreserklärung angerechnet.

**Schritt 4 – UStVA erstellen und abgeben**
- Ausfüllen über ELSTER (Pflicht zur elektronischen Abgabe, § 18 Abs. 1 Satz 1 UStG i.V.m. § 87a AO).
- Kennzahlen (KZ) korrekt zuordnen: KZ 81 (19 % USt), KZ 86 (7 % USt), KZ 66 (Vorsteuer), KZ 21 (ig Erwerbe), KZ 52 (Reverse Charge).
- Zahlungseingang beim Finanzamt spätestens am Fälligkeitstag (nicht nur Abgabe der Meldung).

**Schritt 5 – Berichtigung einer fehlerhaften UStVA**
- § 153 AO: Erkannter Fehler → unverzügliche Berichtigung, bevor der Fehler dem Finanzamt auffällt.
- Vorgehen: Korrigierte UStVA über ELSTER für den betreffenden Zeitraum einreichen (ersetzt vorherige Anmeldung).
- Abgrenzung § 371 AO: Berichtigung nur als Selbstanzeige wirksam, wenn der Fehler auf Vorsatz zur Steuerverkürzung zurückgeht; bloß fahrlässige Fehler = § 153 AO, keine Selbstanzeige erforderlich.
- § 17 UStG: Bei Änderung der Bemessungsgrundlage (Storno, Rechnungskorrektur, Skonto) Berichtigung in dem UStVA-Zeitraum, in dem die Änderung eingetreten ist (nicht rückwirkend).

**Schritt 6 – Folgen verspäteter oder fehlerhafter Abgabe**
- Verspätungszuschlag: bis zu 10 % der Steuer, max. 25.000 EUR (§ 152 AO); Ermessen des Finanzamts.
- Schätzung: Finanzamt kann Besteuerungsgrundlagen schätzen (§ 162 AO).
- Säumniszuschlag auf verspätete Zahlung: 1 % pro angefangenem Monat (§ 240 AO).

## Ausgabeformat

- **Fristenübersicht** (Tabelle): Voranmeldungszeitraum × Reguläre Frist × Frist mit Dauerfristverlängerung.
- **Checkliste UStVA-Erstellung**: Kennzahlen-Mapping für häufige Geschäftsvorfälle.
- **Berichtigungsanleitung** (Schritt-für-Schritt via ELSTER).
- **Dauerfristverlängerungs-Memo**: Voraussetzungen, Sondervorauszahlungshöhe, ELSTER-Pfad.

## Beispiel

**Sachverhalt**: GmbH G hatte im Jahr 2024 eine USt-Zahllast von 14.000 EUR. G hat keine Dauerfristverlängerung beantragt. Die Januar-2025-UStVA enthält einen Vorsteuerfehler (KZ 66 um 1.200 EUR zu hoch), den G am 15.03.2025 erkennt.

**Gutachtenstil**:

*Voranmeldungszeitraum*: Jahres-Zahllast 2024 = 14.000 EUR > 7.500 EUR → G ist zur monatlichen Voranmeldung verpflichtet (§ 18 Abs. 2 Satz 2 UStG).

*Abgabefrist Januar*: Ohne Dauerfristverlängerung: 10. Februar 2025 (§ 18 Abs. 1 Satz 4 UStG). Frist bereits abgelaufen.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Dauerfristverlängerung für Zukunft*: G sollte für 2025 Dauerfristverlängerung beantragen (§ 46 UStDV); Sondervorauszahlung = 14.000/11 = 1.272,73 EUR (fällig bis 10.02.2025 – für 2025 ist Frist versäumt; ab 2026 beantragen).

## Risiken und typische Fehler

- **Voranmeldungszeitraum falsch**: Bei Überschreiten der 7.500-EUR-Schwelle im Vorjahr automatischer Wechsel zu monatlicher Meldepflicht – kein gesonderter Bescheid; viele Unternehmen erkennen den Wechsel nicht rechtzeitig.
- **Dauerfristverlängerung ohne Sondervorauszahlung**: Monatszahler, die keine Sondervorauszahlung leisten, haben keine wirksame Dauerfristverlängerung (BFH BFH/NV 2015, 569 Rn. 14); reguläre Frist gilt.
- **§ 153 AO vs. § 371 AO verwechseln**: Irrtümliche Behandlung als Selbstanzeige bei bloß fahrlässigen Fehlern ist unnötig; umgekehrt: bei Vorsatz reicht § 153 AO nicht.
- **§ 17 UStG-Berichtigungszeitpunkt**: Berichtigung bei Änderung der Bemessungsgrundlage gehört in den Zeitraum des Änderungsereignisses, nicht in den Ursprungszeitraum.
- **ELSTER-Pflicht**: Papieranmeldungen sind grundsätzlich nicht zulässig; nur in Härtefällen nach § 150 Abs. 8 AO ausnahmsweise möglich.
- **Zahlung ≠ Abgabe**: Fristwahrung erfordert sowohl rechtzeitige Abgabe der Meldung als auch rechtzeitigen Zahlungseingang beim Finanzamt (§ 18 Abs. 1 Satz 4 UStG).

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 18 UStG (UStVA-Pflicht, Fristen, Dauerfreistellung) — § 152 AO (Verspätungszuschlag) — § 370 AO (Steuerhinterziehung bei falscher UStVA) — ELSTER-Verfahren (elektronische Uebermittlungs-Pflicht) — § 233a AO (Zinsen bei Umsatzsteuer-Nachzahlung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `aufsichtskommunikation-grundregeln`

**Fokus:** Grundregeln Aufsichtskommunikation: Mitteilungspflichten, Auskunftsrechte, Sonderpruefung, Anhoerung, Bussgeldverfahren. Tonfall, Tempo, Vollstaendigkeit, Konsistenz Schriftverkehr. Pruefraster fuer Antworten an BaFin, BNetzA, Bundeskartellamt. Mustertexte.

# Aufsichtskommunikation Grundregeln

## Spezialwissen: Aufsichtskommunikation Grundregeln
- **Spezialgegenstand:** Aufsichtskommunikation Grundregeln / aufsichtskommunikation grundregeln. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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

## 3. `dora-stellvertreter-und-konzern`

**Fokus:** DORA-Spezial: Stellvertreter, Konzernregelungen, Outsourcing zum gruppeneigenen IT-Dienstleister, kritische TPP-Registrierung bei ESAs. Pruefraster und Klauseln in Konzern-IT-Vertraegen. Schnittstelle zu Aufsichtsrecht der Toechter im Ausland.

# DORA: Konzern und Stellvertreter

## Spezialwissen: DORA: Konzern und Stellvertreter
- **Spezialgegenstand:** DORA: Konzern und Stellvertreter / dora stellvertreter und konzern. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DORA, IT, TPP.
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
