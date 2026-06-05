---
name: cl-mandantenuebersicht-cl-prozesskostenrisiko
description: "CL Mandantenuebersicht CL Prozesskostenrisiko: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# CL Mandantenuebersicht CL Prozesskostenrisiko

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **CL Mandantenuebersicht CL Prozesskostenrisiko** im Plugin Common Law Kompass. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `cl-mandantenuebersicht-englisch` | Mandantenuebersicht englischsprachig vorbereiten: typische Mandantenfragen zu Common-Law-Unterschieden, Vertragsverhandlung mit US-/UK-Counterparties, Litigation in DE gegenueber Common-Law-Gerichtsbarkeit. Strukturierte Beratungsnotiz Englisch / Deutsch parallel. |
| `cl-prozesskostenrisiko-each-party-bears-own` | Spezialfall Prozesskostenregime in USA: each party bears its own costs als Grundregel, Fee Shifting nur per Vertrag oder bei statute. Kontrast zur deutschen kostenpflichtigen Loser-pays-Regel. Pruefraster fuer Mandanten-Risikoanalyse. |
| `cl-spezial-precedent-vs-statute` | Spezialfall Precedent gegen Statute: Verhaeltnis Case Law und Gesetzgebung in England und USA, ratio decidendi gegen obiter dictum, Distinguishing, Overruling. Pruefraster fuer Vergleich mit deutscher Methode und Beispiel-Faelle. |

## Arbeitsweg

Im Plugin Common Law Kompass gilt für **CL Mandantenuebersicht CL Prozesskostenrisiko**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `cl-mandantenuebersicht-englisch`

**Fokus:** Mandantenuebersicht englischsprachig vorbereiten: typische Mandantenfragen zu Common-Law-Unterschieden, Vertragsverhandlung mit US-/UK-Counterparties, Litigation in DE gegenueber Common-Law-Gerichtsbarkeit. Strukturierte Beratungsnotiz Englisch / Deutsch parallel.

# Common Law: Mandantenuebersicht EN

## Aufgabe
Mandantenuebersicht englischsprachig vorbereiten: typische Mandantenfragen zu Common-Law-Unterschieden, Vertragsverhandlung mit US-/UK-Counterparties, Litigation in DE gegenueber Common-Law-Gerichtsbarkeit.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## False-Friends-Liste (Common Law vs. deutsches Recht)

| Common-Law-Begriff | Klingt wie | Tatsaechliche Bedeutung |
|---|---|---|
| **Discovery** | Beweisermittlung | Vorprozessuale Beweis- und Tatsachenausforschung mit Zwangsmitteln (FRCP 26-37; in DE nur eng beschraenkt §§ 142, 144, 421-432 ZPO; § 810 BGB; § 242 BGB; Art. 15 DSGVO) |
| **Consideration** | Erwaegung, Ueberlegung | Gegenleistung als Wirksamkeitsvoraussetzung des contract; deutsches Recht kennt keine consideration |
| **Indemnity** | Entschaedigung, Versicherung | Freistellungsvertrag, oft verschuldensunabhaengig und primaer; nicht identisch mit § 257 BGB |
| **Warranty** | Garantie | Vertragliche Zusicherung mit Schadensersatzfolge bei Verletzung; nicht ident mit § 443 BGB Garantie |
| **Representation** | Vertretung | Tatsachenbehauptung; misrepresentation fuehrt zu rescission / damages, im Unterschied zu Anfechtung § 119 II BGB |
| **Equity** | Kapital, Eigenkapital | Billigkeitsrechtsprechung mit eigenen Rechtsbehelfen (injunction, specific performance, rescission) |
| **Specific performance** | Konkrete Leistung | Naturalerfuellungsanspruch — im Common Law Ausnahme, im deutschen Recht Regel (§ 241 I BGB) |
| **Liquidated damages** | Liquidierter Schaden | Vertraglich vereinbarte Schadenspauschale; nur wirksam wenn "genuine pre-estimate of loss" (UK Cavendish v. Makdessi 2015) |
| **Penalty** | Strafe | Unzulaessig im Common Law als nicht-genuine pre-estimate; in DE Vertragsstrafe §§ 339 ff. BGB zulaessig |
| **Tort** | Unrecht | Deliktsrecht ohne Generalklausel; einzelne torts (negligence, nuisance, defamation) — vgl. § 823 ff. BGB |
| **Estoppel** | Sperre | Treu-und-Glauben-Konstrukt fuer Vertrauensschutz; vergleichbar § 242 BGB, aber technischer |
| **Privity of contract** | Vertraulichkeit | Vertragsbindung nur fuer Parteien; UK seit 1999 Contracts (Rights of Third Parties) Act gelockert |
| **Statute of limitations** | Limitierung | Verjaehrung; abweichend vom deutschen 3-Jahres-Regel (§ 195 BGB) je nach Staat unterschiedlich |
| **Punitive / exemplary damages** | Punktive Schaeden | Strafschadensersatz; nicht im deutschen Recht; nicht vollstreckbar wegen ordre public § 328 I Nr. 4 ZPO |

## Struktur fuer englische Mandantennotiz

1. **Issue** — Was ist die Rechtsfrage?
2. **Rule** — Welche Rechtssaetze, welche Rechtsordnung?
3. **Application** — Subsumtion unter die Tatsachen.
4. **Conclusion** — Ergebnis und Empfehlung.

(IRAC-Methode statt Gutachtenstil; Mandant-Englisch ist deutlich knapper als deutsche Memo-Struktur.)

## Praxisfallen

- **Choice-of-law** wird oft mit choice-of-forum verwechselt; trennen.
- **Trust**-Strukturen im US/UK-Recht haben kein direktes Aequivalent in DE; § 1922 BGB Erbfolge greift anders.
- **At-will employment** in US-Staaten: deutsche Mandanten sind irritiert; Hinweis auf US-Realitaet.
- **Anti-suit injunctions** UK gegen DE-Klagen — seit Brexit wieder moeglich; Vollstreckbarkeit in DE problematisch.

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

## 2. `cl-prozesskostenrisiko-each-party-bears-own`

**Fokus:** Spezialfall Prozesskostenregime in USA: each party bears its own costs als Grundregel, Fee Shifting nur per Vertrag oder bei statute. Kontrast zur deutschen kostenpflichtigen Loser-pays-Regel. Pruefraster fuer Mandanten-Risikoanalyse.

# Common Law: Each-party-bears-own

## Aufgabe
Spezialfall Prozesskostenregime in USA: each party bears its own costs als Grundregel, Fee Shifting nur per Vertrag oder bei statute.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Kostenregime im Vergleich

| Rechtsordnung | Grundregel | Ausnahmen |
|---|---|---|
| **USA ("American Rule")** | Each party bears its own attorney's fees | Vertragsklausel (fee shifting); statutorische Anspruchsgrundlage (z. B. 42 U.S.C. § 1988 civil rights, § 285 Patent Act); Bad-faith litigation; common fund doctrine |
| **UK ("English Rule") / Loser-pays** | Loser pays winner's costs, aber nur "reasonable and proportionate"; Standard- oder Indemnity-Basis | Wasted costs; conditional fee agreements (CFA); damages-based agreements (DBA); after-the-event insurance |
| **Deutschland** | § 91 ZPO Unterliegender traegt Kosten | Quotelung § 92 ZPO; Vergleich § 98 ZPO; RVG-/JVEG-Hoechstsaetze begrenzen Erstattung |
| **Schiedsgerichtsbarkeit** | Schiedsspruch entscheidet ueber Kosten (Art. 38 ICC Rules, § 1057 ZPO) | Oft "costs follow the event" wie englisches Recht |

## Pruefraster Mandanten-Risikoanalyse

1. **Forum bestimmen** — wo wird das Gericht zustaendig sein? Welche Kostenregel gilt dort?
2. **Streitwert / amount in controversy** — bei US-Gerichten Bundeszustaendigkeit ab 75.000 USD diversity (28 U.S.C. § 1332).
3. **Anwaltskosten schaetzen** — US-Stundensaetze typischer Partner 600 bis 1.500 USD; Discovery-Kosten kalkulieren.
4. **Vertragliche Fee-Shifting-Klausel** pruefen: "prevailing party shall be entitled to recover reasonable attorneys' fees and costs".
5. **Drittfinanzierung** — Litigation Funding ist in den USA verbreitet; in DE seit BGH zulaessig, aber RDG-Grenzen.
6. **Punitive damages** in den USA pro Klaeger relevant; nicht vollstreckbar im deutschen ordre public (§ 328 I Nr. 4 ZPO).

## Praxisfallen

- **"Loser-pays-Trugschluss"** im US-Verfahren: deutsche Mandanten erwarten, im Erfolgsfall Kosten erstattet zu bekommen — das ist die seltene Ausnahme.
- **Discovery-Kosten** koennen in den USA das Hauptkostenrisiko sein (E-Discovery, depositions), nicht Anwaltskosten.
- **Class actions / collective actions:** asymmetrisches Kostenrisiko fuer Beklagten.
- **Anti-suit injunctions** — UK-Gerichte koennen Vollstreckung in DE behindern; in der EU vor Brexit unzulaessig (West Tankers).
- **Pre-action protocols** UK Civil Procedure Rules: vor Klage bestimmte Schritte einhalten, sonst Kostenstrafe.

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

## 3. `cl-spezial-precedent-vs-statute`

**Fokus:** Spezialfall Precedent gegen Statute: Verhaeltnis Case Law und Gesetzgebung in England und USA, ratio decidendi gegen obiter dictum, Distinguishing, Overruling. Pruefraster fuer Vergleich mit deutscher Methode und Beispiel-Faelle.

# Common Law: Precedent gegen Statute

## Spezialwissen: Common Law: Precedent gegen Statute
- **Spezialgegenstand:** Common Law: Precedent gegen Statute / cl precedent vs statute. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** USA.
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
