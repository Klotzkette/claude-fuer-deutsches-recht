---
name: transparenzbericht-erstellung-trusted-flagger
description: "Transparenzbericht Erstellung Trusted Flagger: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Transparenzbericht Erstellung Trusted Flagger

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Transparenzbericht Erstellung Trusted Flagger** im Plugin DSA/DMA Digitalregulierung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dsa-transparenzbericht-erstellung` | Transparenzbericht nach Art. 15 DSA jaehrlich erstellen: Behoerdenanordnungen (Loeschung, Auskunft), Nutzermeldungen, eigene Inhaltsmoderation, automatisierte Tools, Statement of Reasons, Beschwerden. Format-Anforderungen der EU-Kommission, Excel-Templates, Veroeffentlichungspflichten. Fuer VLOP zusaetzlich Halbjahresbericht. |
| `dsa-trusted-flagger-anerkennung` | Trusted Flagger nach Art. 22 DSA: Voraussetzungen, Anerkennung durch nationalen Digital Services Coordinator, Vorrangstellung bei Meldungen, Pflichten der Plattform zur prioritaeren Bearbeitung. Antragsverfahren bei der BNetzA (DSC Deutschland) inkl. Anhoerung. Pruefraster fuer Vereine und NGOs die sich anerkennen lassen wollen. |
| `dsa-vlop-vlose-einordnung-und-pflichten` | VLOP (sehr grosse Online-Plattform) oder VLOSE (sehr grosse Suchmaschine) Einordnung und Pflichten-Katalog: Plattform prüft ob Designation droht oder besteht. Normen: DSA (EU) 2022/2065 Art. 33 (Designation Kommission), Art. 24 Abs. 3 (Meldepflicht halbjaeehrlich), Art. 34-43 (Pflichtenkatalog: Risikobewertung, Audits, Compliance-Funktion, Transparenz, Werbung, Empfehlungssysteme, Forschungsdatenzugang, Krisenmechanismus). Prüfraster: 45 Mio. monatlich aktive Nutzer Schwelle, Meldepflicht, Pflichtenkatalog je Art. Output Designation-Prüfschema, Compliance-Roadmap. Abgrenzung: Gatekeeper DMA siehe dma-gatekeeper-schwellen-und-kernplattformdienste; Art. 34 Risikobewertung siehe dsa-art-34-systemische-risikobewertung. |

## Arbeitsweg

Im Plugin DSA/DMA Digitalregulierung gilt für **Transparenzbericht Erstellung Trusted Flagger**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dsa-transparenzbericht-erstellung`

**Fokus:** Transparenzbericht nach Art. 15 DSA jaehrlich erstellen: Behoerdenanordnungen (Loeschung, Auskunft), Nutzermeldungen, eigene Inhaltsmoderation, automatisierte Tools, Statement of Reasons, Beschwerden. Format-Anforderungen der EU-Kommission, Excel-Templates, Veroeffentlichungspflichten. Fuer VLOP zusaetzlich Halbjahresbericht.

# DSA Transparenzbericht

## Spezialwissen: DSA Transparenzbericht
- **Spezialgegenstand:** DSA Transparenzbericht / dsa transparenzbericht erstellung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** Art. 15, DSA, EU, VLOP.
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

## 2. `dsa-trusted-flagger-anerkennung`

**Fokus:** Trusted Flagger nach Art. 22 DSA: Voraussetzungen, Anerkennung durch nationalen Digital Services Coordinator, Vorrangstellung bei Meldungen, Pflichten der Plattform zur prioritaeren Bearbeitung. Antragsverfahren bei der BNetzA (DSC Deutschland) inkl. Anhoerung. Pruefraster fuer Vereine und NGOs die sich anerkennen lassen wollen.

# Trusted Flagger Anerkennung

## Spezialwissen: Trusted Flagger Anerkennung
- **Spezialgegenstand:** Trusted Flagger Anerkennung / dsa trusted flagger anerkennung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** Art. 22, DSA, DSC.
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

## 3. `dsa-vlop-vlose-einordnung-und-pflichten`

**Fokus:** VLOP (sehr grosse Online-Plattform) oder VLOSE (sehr grosse Suchmaschine) Einordnung und Pflichten-Katalog: Plattform prüft ob Designation droht oder besteht. Normen: DSA (EU) 2022/2065 Art. 33 (Designation Kommission), Art. 24 Abs. 3 (Meldepflicht halbjaeehrlich), Art. 34-43 (Pflichtenkatalog: Risikobewertung, Audits, Compliance-Funktion, Transparenz, Werbung, Empfehlungssysteme, Forschungsdatenzugang, Krisenmechanismus). Prüfraster: 45 Mio. monatlich aktive Nutzer Schwelle, Meldepflicht, Pflichtenkatalog je Art. Output Designation-Prüfschema, Compliance-Roadmap. Abgrenzung: Gatekeeper DMA siehe dma-gatekeeper-schwellen-und-kernplattformdienste; Art. 34 Risikobewertung siehe dsa-art-34-systemische-risikobewertung.

# DSA — VLOP/VLOSE-Einordnung und Pflichten

## Schwellenwert (Art. 33 Abs. 1 DSA)

Sehr große Online-Plattform oder sehr große Online-Suchmaschine: **monatlich durchschnittlich mindestens 45 Millionen aktive Empfänger des Dienstes in der Union**.

Berechnung nach Methodikleitfaden der Kommission (Empfehlung 2023): unique users; Bot-Filterung; mindestens 45 Mio. über sechs Monate hinweg.

## Meldepflicht (Art. 24 Abs. 2 DSA)

- Alle Anbieter von Online-Plattformen und Online-Suchmaschinen müssen die durchschnittliche monatliche Nutzerzahl in der EU **halbjährlich öffentlich machen** (per 17.02. und 17.08.)
- Auf Anfrage der Kommission detaillierte Angaben

## Designation

1. Kommission stellt Schwellenüberschreitung fest (Art. 33 Abs. 4)
2. **Förmlicher Designations-Beschluss** der Kommission
3. Pflichten greifen **vier Monate nach Notifikation** des Beschlusses (Art. 33 Abs. 6)
4. Veröffentlichung im Amtsblatt

Stand 2026: bereits designiert sind u.a. mehrere große soziale Netzwerke, Videoplattformen, Marktplätze, Suchmaschinen, Pornoportale (zweite Tranche April 2024) sowie eine Reisebuchungsplattform.

## Pflichten-Katalog VLOP/VLOSE (Art. 34 bis 43 DSA)

| Norm | Pflicht |
|---|---|
| Art. 34 | Jährliche **systemische Risikobewertung** |
| Art. 35 | **Risikominderungsmaßnahmen** |
| Art. 36 | **Krisenreaktionsmechanismus** (Kommission kann auslösen) |
| Art. 37 | **Unabhängige jährliche Audits** |
| Art. 38 | Empfehlungssysteme: **mindestens eine Option ohne Profiling** |
| Art. 39 | **Werbearchiv**, öffentlich zugänglich |
| Art. 40 | **Datenzugang für DSC, Kommission und vetted researchers** |
| Art. 41 | **Compliance-Funktion** in der Organisation, unabhängig |
| Art. 42 | **Transparenzberichte** halbjährlich (statt jährlich) |
| Art. 43 | **Aufsichtsgebühr** an die Kommission |

## Sanktionen

- Geldbußen bis **6 % des weltweiten Jahresumsatzes** (Art. 74 DSA)
- Zwangsgelder bis 5 % des durchschnittlichen täglichen Umsatzes (Art. 76)
- Bei wiederholten schwerwiegenden Verstößen: Zugangssperre möglich (Art. 82 — supervisory measures)

## Anwaltliche Prüfschritte

### Für Plattform-Mandanten

1. **Nutzerzählung verifizieren** — Methodik, Datengrundlage, Audit-fähig?
2. **Vier-Monats-Frist nach Designation** dokumentieren — Compliance-Programm steht?
3. **Compliance-Funktion personell besetzen** (Art. 41 — Berichtspflicht an Geschäftsleitung, unabhängig)
4. **Risikobewertung methodisch absichern** (siehe Skill `dsa-art-34-systemische-risikobewertung`)
5. **Audit-Vertrag** vorbereiten (unabhängige Auditoren, Art. 37, Delegierte VO)
6. Bei Streit über Designation: **Klage zum EuG nach Art. 263 AEUV** prüfen (siehe Skill `klage-gegen-vlop-einordnung-art-263-aeuv`)

### Für Nutzer / Wettbewerber

- VLOPs haben **schärfere Pflichten als normale Online-Plattformen** — Verstoß = stärkere Hebel
- Forschungsdatenzugang nur gegen VLOPs/VLOSEs (Art. 40 Abs. 4)
- Beschwerde bei DSC am Sitzstaat oder bei Kommission

## Praktische Fallstricke

- **Nutzerzählung manipuliert oder fehlerhaft**: Risiko der Aufsichtsmaßnahme nach Art. 79 DSA
- **Konzernstruktur**: maßgeblich ist die rechtliche Einheit, die den Dienst anbietet; in Konzernen oft die EU-Tochter
- **Plattform mit mehreren Diensten**: jeder Dienst wird einzeln gemessen (z. B. ein Marktplatz mit separater Karten-/Reise-Funktion)
- **Pflichten gelten unionsweit** — One-Stop-Shop existiert für DSA **nicht** in der DSGVO-Form; Kommission ist allein zuständig für VLOPs (Art. 56 Abs. 2 DSA)

## Aktuelle Rechtsprechung

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Faktische Updates (Stand 05/2026)

- **VLOP/VLOSE-Designation-Liste der Kommission:** Aktuelle Liste der designierten sehr grossen Online-Plattformen / Suchmaschinen live ueber digital-strategy.ec.europa.eu/en/policies/dsa-very-large-online-platforms-and-search-engines pruefen. Stand 2026: mehrere Tranchen designiert (soziale Netzwerke, Marktplaetze, Videoplattformen, App-Stores, Suchmaschinen, Pornoportale, Reiseplattformen).
- **Art. 40 DSA — Forschungsdatenzugang:** Delegierter Rechtsakt zum Forschungsdatenzugang (Art. 40 Abs. 13 DSA) ist im Verfahren / in Kraft (live pruefen ueber eur-lex.europa.eu). Vetted-researcher-Verfahren wird vom Digital Services Coordinator (DSC) am Sitzstaat administriert.
- **Art. 37 DSA — Audits:** Delegierte VO (EU) 2023/2832 ueber unabhaengige Audits ist anwendbar; Auditoren benoetigen fachliche Kompetenz, Unabhaengigkeit, ethische Standards. Audit-Methodik ISA / IFAC-Anlehnung empfohlen.
- **EuG- und EuGH-Linie zu DSA-Designation:** Mehrere VLOPs haben gegen die Designation und gegen die Aufsichtsgebuehr Klage beim EuG erhoben (Art. 263 AEUV). Konkrete Aktenzeichen und Verfahrensstand live pruefen ueber curia.europa.eu (Suche "DSA" / "VLOP").
- **DSA-Sanktionen:** Erste Bussgeldentscheidungen der Kommission gegen VLOPs sind moeglich; Verfahren live ueber digital-strategy.ec.europa.eu sowie EU-Amtsblatt pruefen.
- **DSC in Deutschland:** Federfuehrend ist die Bundesnetzagentur (Digital Services Coordinator) nach DDG (Digitale-Dienste-Gesetz), Koordinierungsmechanismen mit BfDI, KJM, Landesmedienanstalten geregelt. Quelle: bundesnetzagentur.de.

## Zentrale Normen (Paragrafenkette)

- Art. 33 DSA — Designation VLOPs/VLOSEs; 45-Mio.-Schwelle; halbjährliche Nutzerzahl-Meldepflicht Art. 24 Abs. 3 DSA
- Art. 34–43 DSA — Pflichtenkatalog: Risikobewertung, Audit, Compliance-Funktion, Werbetransparenz, Empfehlungssysteme, Forschungsdatenzugang, Krisenprotokoll
- Art. 52–53 DSA — Sanktionen bis 6 % Jahresumsatz
- Art. 65 DSA — Durchsetzung durch Kommission

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn

1. Überschreitet die Plattform 45 Mio. monatlich aktive EU-Nutzer (Art. 33 Abs. 1 DSA)?
2. Ist die Plattform bereits designiert (Kommissionsbeschluss abrufbar)?
3. Welche Pflichten aus Art. 34–43 DSA sind fällig (Fristen: 4 Monate nach Designation für Erstbewertung)?
4. Beratungsrichtung: Compliance-Beratung (Plattform) oder Durchsetzung (Nutzer/Behörde)?

## Output-Template — VLOP/VLOSE-Pflichten-Übersicht

**Adressat:** Compliance-Abteilung (VLOP) / Kanzlei intern — Tonfall: sachlich-strukturiert

```
VLOP/VLOSE-Pflichten-Check [DATUM]
Plattform: [NAME]
Designation: [DATUM] / ausstehend
Monatliche EU-Nutzer: [ANZAHL] >= 45 Mio.: ja / nein

Kernpflichten-Status:
| Pflicht (Norm) | Frist | Status |
|------------------------------------|-----------|------------|
| Risikobewertung Art. 34 | +4 Monate | |
| Unabh. Audit Art. 37 | jaehrlich | |
| Compliance-Funktion Art. 41 | laufend | |
| Transparenz Werbung Art. 39 | laufend | |
| Empfehlungssystem-Optionen Art. 38 | laufend | |
| Forschungsdatenzugang Art. 40 | auf Anfrag| |
| Krisenprotokoll Art. 48 | im Krisenf| |

Sanktionsrisiko: Art. 52 DSA — bis 6 % Jahresumsatz
```
