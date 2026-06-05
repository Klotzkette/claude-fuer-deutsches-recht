---
name: brki-rag-bro-grundlagen-cloud-act
description: "Brki RAG BRO Grundlagen Cloud ACT: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Brki RAG BRO Grundlagen Cloud ACT

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Brki RAG BRO Grundlagen Cloud ACT** im Plugin Berufsrecht Ki Vertragspruefung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `brki-rag-vertraulichkeit-spezial` | Spezialfall RAG-Architekturen mit Mandantenakten: Embedding-Speicher, Vektor-DB im EU-Hosting, Loeschkonzept Embedding bei Mandantenwiderruf, Trennung pro Mandat. Pruefraster und technische Mindestanforderungen. |
| `bro-grundlagen-ki-einsatz` | BRAO-Grundlagen fuer KI-Einsatz in der Kanzlei einfuehrend: § 43a BRAO Verschwiegenheit, § 43e BRAO IT-Dienste, § 203 StGB Strafbarkeit Geheimnisverletzung, Datenschutz nach DSGVO und BDSG. Strukturierte Uebersicht zur Pflichtenkette beim Outsourcing an KI-Anbieter. |
| `cloud-act-und-drittstaat-pruefen` | Prüfe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). EU/EWR sind regelmäßig leichter vertretbar; Drittstaaten benötigen eine eigene Berufsgeheimnisprüfung. US-CLOUD Act, FISA, Supportzugriffe, EU-US-DPF, SCC und Professional Secrecy Addendum sauber trennen. |

## Arbeitsweg

Im Plugin Berufsrecht Ki Vertragspruefung gilt für **Brki RAG BRO Grundlagen Cloud ACT**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `brki-rag-vertraulichkeit-spezial`

**Fokus:** Spezialfall RAG-Architekturen mit Mandantenakten: Embedding-Speicher, Vektor-DB im EU-Hosting, Loeschkonzept Embedding bei Mandantenwiderruf, Trennung pro Mandat. Pruefraster und technische Mindestanforderungen.

# BRKI: RAG-Vertraulichkeit

## Spezialwissen: BRKI: RAG-Vertraulichkeit
- **Spezialgegenstand:** BRKI: RAG-Vertraulichkeit / brki rag vertraulichkeit spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** RAG, DB, EU, BRKI.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Verträge, Auszuege liegen vor?
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

## 2. `bro-grundlagen-ki-einsatz`

**Fokus:** BRAO-Grundlagen fuer KI-Einsatz in der Kanzlei einfuehrend: § 43a BRAO Verschwiegenheit, § 43e BRAO IT-Dienste, § 203 StGB Strafbarkeit Geheimnisverletzung, Datenschutz nach DSGVO und BDSG. Strukturierte Uebersicht zur Pflichtenkette beim Outsourcing an KI-Anbieter.

# BRAO und KI: Grundlagen

## Spezialwissen: BRAO und KI: Grundlagen
- **Spezialgegenstand:** BRAO und KI: Grundlagen / bro grundlagen ki einsatz. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BRAO, KI, IT, DSGVO, BDSG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Verträge, Auszuege liegen vor?
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

## 3. `cloud-act-und-drittstaat-pruefen`

**Fokus:** Prüfe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). EU/EWR sind regelmäßig leichter vertretbar; Drittstaaten benötigen eine eigene Berufsgeheimnisprüfung. US-CLOUD Act, FISA, Supportzugriffe, EU-US-DPF, SCC und Professional Secrecy Addendum sauber trennen.

# Cloud Act und Drittstaat prüfen

## Fachkern: Cloud Act und Drittstaat prüfen

- **KI-/Berufsrechtsproblem (Cloud Act und Drittstaat prüfen):** Prüfe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). EU/EWR sind regelmäßig leichter vertretbar; Drittstaaten benötigen eine eigene Berufsgeheimnisprüfung. US-CLOUD Act, FISA, Supportzugriffe, EU-US-DPF, SCC und Professional Secrecy Addendum sauber trennen.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Norm

Absatz 4 der jeweiligen Dienstleisterregelung. Wortlaut (am Beispiel § 43e Abs. 4 BRAO; identisch in § 62a Abs. 4 StBerG, § 50a Abs. 4 WPO, § 39c Abs. 4 PAO; bei § 26a BNotO entsprechend):

"Bei der Inanspruchnahme von Dienstleistungen, die im Ausland erbracht werden, darf der Rechtsanwalt dem Dienstleister den Zugang zu fremden Geheimnissen unbeschadet der übrigen Voraussetzungen dieser Vorschrift nur dann eröffnen, wenn der dort bestehende Schutz der Geheimnisse dem Schutz im Inland vergleichbar ist, es sei denn, dass der Schutz der Geheimnisse dies nicht gebietet."

## Berufsrechtliche Auslegungslinie

EU-/EWR-Konstellationen sind wegen gemeinsamer Datenschutz- und Berufsrechtsnähe regelmäßig leichter vertretbar. Außerhalb der EU/des EWR ist die Vergleichbarkeit des Geheimnisschutzes einzelfallabhängig zu prüfen.

Wichtig: Die Vergleichbarkeit bezieht sich auf den Schutz der Geheimnisse, nicht auf das allgemeine Rechtsschutzniveau. Selbst wenn ein Land eine funktionierende Justiz hat, kann der Schutz von Berufsgeheimnissen mangelhaft sein.

## Problemzone USA

Die USA stellen die größte praktische Herausforderung dar, weil die meisten KI-Anbieter dort ansässig sind oder dort verarbeiten lassen.

### CLOUD Act (2018)

Der US-Clarifying Lawful Overseas Use of Data Act verpflichtet US-Anbieter und ihre weltweiten Töchter, US-Behörden auf Anordnung Zugang zu Daten zu gewähren, auch wenn diese außerhalb der USA gespeichert sind. Eine deutsche Hostinglokation schützt also nicht.

### FISA Section 702

FISA Section 702 kann unter bestimmten Voraussetzungen Zugriffe auf elektronische Kommunikation von Nicht-US-Personen über US-Dienste ermöglichen. Für die Kanzlei genügt deshalb nicht die Frage "Wo steht der Server?", sondern es sind Konzern-, Support-, Administrations- und Herausgabezugriffe mitzudenken.

### Konsequenz

Bei US-Anbietern kann ein struktureller Restzugriff durch US-Behörden bestehen, der mit dem deutschen Berufsgeheimnis kollidieren kann. Daraus folgt nicht automatisch ein Totalverbot; erforderlich sind aber eine sorgfältige Abwägung, Datenminimierung, Vertragszusätze und dokumentierte Restrisikoentscheidung.

## Professional Secrecy Addendum

Bei US-Anbietern empfehlenswert: ein eigenes Berufsgeheimnis-Addendum zum Hauptvertrag, das

- die berufsrechtlichen Anforderungen explizit übernimmt
- den Anbieter zur Anfechtung jedes US-Auskunftsverlangens verpflichtet
- den Anbieter zur unverzüglichen Information der Kanzlei verpflichtet, soweit gesetzlich zulässig
- den Anbieter zur Datenminimierung in Richtung USA verpflichtet (keine US-Backups, keine US-Logs)
- Gerichtsstand und anwendbares Recht in Deutschland

Ob ein Anbieter solche Zusätze akzeptiert, muss am konkreten Vertragsstand live geprüft werden. Keine Produktbehauptung aus Modellwissen übernehmen.

## Prüfschema

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.


| Punkt | Status | Ampel | Bemerkung |
|---|---|---|---|
| Sitz Anbieter (Hauptvertragspartei) | | | |
| Konzernzugehörigkeit (US-Konzern?) | | | |
| Verarbeitungsstandort | | | |
| Backup-Standort | | | |
| Modellanbieter (etwa OpenAI) Standort | | | |
| Hoster Standort | | | |
| CLOUD-Act-Anwendbarkeit | | | |
| FISA-Anwendbarkeit | | | |
| Professional Secrecy Addendum | | | |
| Gerichtsstand Deutschland | | | |
| Anwendbares deutsches Recht | | | |
| Standardvertragsklauseln (SCC) | | | |
| Adequacy decision (EU-US-DPF) | | | |

## EU-US-Data Privacy Framework

Das 2023 in Kraft getretene Data Privacy Framework regelt den datenschutzrechtlichen Datentransfer in die USA. **Es regelt nicht das Berufsgeheimnis.** Es schützt nicht vor CLOUD-Act-Zugriffen. Der DPF ist datenschutzrechtlich relevant, berufsrechtlich nur als Indiz für ein gewisses Schutzniveau, nicht als Genehmigung.

## Empfehlungen

- Bei EU/EWR-Anbietern: Auslandsbezug grundsätzlich unproblematisch
- Bei US-Anbietern: Professional Secrecy Addendum, EU-Hosting-Zusicherung, kein US-Backup
- Bei Anbietern aus sonstigen Drittstaaten (China, Indien): in der Regel rote Ampel — Vergleichbarkeit muss positiv nachgewiesen werden

## Output

Tabellarische Bewertung. Bei US-Bezug: Vorlage für Professional Secrecy Addendum aus dem Skill `klauselvorschlaege`.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- Art. 44–49 DSGVO — Drittlandsübermittlung, SCC, Adequacy Decisions, CBPR
- Art. 46 Abs. 2 lit. c DSGVO — Standardvertragsklauseln als geeignete Garantien
- § 43e Abs. 4 BRAO, § 62a Abs. 4 StBerG, § 50a Abs. 4 WPO — Drittstaat-Klausel Berufsrecht
- US CLOUD Act 2018, 18 U.S.C. § 2713 — Zugriff auf Daten unabhängig vom Speicherort
- FISA Section 702, 50 U.S.C. § 1881a — Überwachung elektronischer Kommunikation von Nicht-US-Personen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage-Frage (Entscheidungsbaum)

```
Anbieter Sitz EU/EWR?
 Ja → Auslandsbezug unproblematisch (DAV S. 15)
 Nein → US-Konzern oder US-Tochter?
 Ja → CLOUD Act anwendbar → Professional Secrecy Addendum erforderlich
 EU-Hosting-Zusicherung vorhanden?
 Ja → gelbe Ampel (struktureller Restzugriff bleibt)
 Nein → rote Ampel
 Nein → Sonstiges Drittland (CN, IN, RU)?
 → Vergleichbarkeitsnachweis positiv erforderlich → i.d.R. rote Ampel
```
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)


## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — US-Anbieter in Kanzleiinfrastruktur pruefen | Cloud-Act-Risikobewertung nach Schema unten |
| Variante A — kein US-Bezug erkennbar | Drittstaat-Kapitel trotzdem pruefen (UK TIOPA, CN DSL) |
| Variante B — Mandant will trotz Risiko US-Anbieter nutzen | Risikohinweis dokumentieren; Mandant schriftlich bestaetigen lassen |
| Variante C — staatliche Ermittlung laeuft bereits | Sofortiger Wechsel; Datensicherung und Incident-Response pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Drittstaat-Prüfvermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Drittstaat-Prüfvermerk [DATUM]
Anbieter: [NAME, LAND]
Konzernstruktur: [US-Konzern ja/nein; Mutter: NAME]

A) DSGVO-Drittlandsübermittlung (Art. 44 DSGVO)
Adequacy Decision: [ja/nein; EU-US-DPF ja/nein]
SCC vorhanden: [ja/nein; Datum]
TIA (Transfer Impact Assessment) durchgefuehrt: [ja/nein]

B) Berufsrechtlicher Drittstaat-Check (§ 43e Abs. 4 BRAO)
Vergleichbarkeit Schutzniveau: [ja/eingeschraenkt/nein]
CLOUD-Act-Risiko: [ja/nein/unklar]
Professional Secrecy Addendum: [vorhanden/nicht vorhanden/beantragt]

C) Ampel
DSGVO-Transfer: GRUEN / GELB / ROT
Berufsrecht Drittstaat: GRUEN / GELB / ROT
Empfehlung: [Nutzung freigegeben / Addendum erforderlich / Anbieterwechsel]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]
