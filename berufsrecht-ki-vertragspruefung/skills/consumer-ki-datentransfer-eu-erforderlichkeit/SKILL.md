---
name: consumer-ki-datentransfer-eu-erforderlichkeit
description: "Consumer KI Datentransfer EU Erforderlichkeit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Consumer KI Datentransfer EU Erforderlichkeit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Consumer KI Datentransfer EU Erforderlichkeit** im Plugin Berufsrecht Ki Vertragspruefung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `consumer-ki-vs-43e-dienstleister` | Consumer-KI, Enterprise-KI, Kanzleisoftware und §-43e-Dienstleister trennen: prüft Mandatsdaten, Vertragsbindung, Toolzweck, Subunternehmer, Anonymisierungspflicht, Mandanteninformation und Freigabeentscheidung. |
| `datentransfer-eu-drittstaat` | Datentransfer EU nach Drittstaat: Angemessenheitsbeschluss EU-US-Data-Privacy-Framework, Standardvertragsklauseln Modul 2, Transfer Impact Assessment nach EuGH Schrems II. Pruefraster fuer US-KI-Anbieter, technische Massnahmen wie Tokenisierung, Pseudonymisierung. Schriftsatzbausteine. |
| `erforderlichkeit-dokumentieren` | Prüfe die Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenüber dem KI-Dienstleister nach Absatz eins der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). Bezugspunkt ist der Zweck der konkreten Offenlegung, nicht die abstrakte KI-Strategie der Kanzlei. Erstelle einen internen Compliance-Vermerk mit Beurteilungsspielraum und Grenzen. |

## Arbeitsweg

Im Plugin Berufsrecht Ki Vertragspruefung gilt für **Consumer KI Datentransfer EU Erforderlichkeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `consumer-ki-vs-43e-dienstleister`

**Fokus:** Consumer-KI, Enterprise-KI, Kanzleisoftware und §-43e-Dienstleister trennen: prüft Mandatsdaten, Vertragsbindung, Toolzweck, Subunternehmer, Anonymisierungspflicht, Mandanteninformation und Freigabeentscheidung.

# Consumer-KI vs. §-43e-Dienstleister

## Ziel

Dieser Skill verhindert den häufigsten Denkfehler: Nicht jede KI ist berufsrechtlich gleich. Ein öffentliches Frontend ohne berufsspezifische Verpflichtung ist etwas anderes als ein bewusst beauftragter Dienstleister, der in Textform auf Berufsgeheimnisse, strafrechtliche Folgen und Subunternehmerkontrolle verpflichtet wird.

## Abfrage

1. Welches Tool, welche Produktvariante, welcher Vertrag?
2. Public Account, Team Account, Enterprise Contract, Kanzleisoftware oder eigene API?
3. Welche Daten: anonym, pseudonym, Mandatsdaten, Geschäftsgeheimnisse, besondere Kategorien, Gegnerdaten?
4. Nutzt der Anbieter Eingaben für Training, Produktverbesserung, Qualitätsanalyse, Support oder Abuse Monitoring?
5. Wo sitzen Anbieter, Hosting, Subunternehmer, Support und Muttergesellschaft?
6. Ist das Tool allgemeine Kanzleiinfrastruktur oder unmittelbar für ein Einzelmandat?

## Einordnung

| Typ | Mandatsdaten? | Kernprüfung |
|---|---:|---|
| Öffentliches Consumer-Tool | Nein, außer anonymisiert/abstrahiert | Keine §-43e-Verpflichtung; Geheimnisschutz durch Nichtoffenlegung. |
| Enterprise-Tool ohne Berufsgeheimniszusatz | Nur nach Prüfung | Vertrag kann zu dünn sein; § 43e Abs. 3 konkret nachverhandeln. |
| Kanzleisoftware mit KI-Modul | Möglich | Dienstleisterregelung, AVV, TOM, No-Training, Supportzugriff, Löschkonzept. |
| §-43e-konform verpflichteter KI-Dienstleister | Möglich | Erforderlichkeit, Textform, Belehrung, Subunternehmer, Drittstaat, Endkontrolle. |
| Mandatsspezifisches Expertentool | Möglich, aber sensibel | Zusätzlich Mandantenbezug und § 43e Abs. 5 prüfen. |

## Entscheidungssatz

Formuliere nie pauschal "KI mit Mandatsdaten ist verboten" oder "Enterprise reicht". Formuliere: Zulässig ist nur die konkret erforderliche Offenlegung an einen hinreichend gebundenen, kontrollierten und dokumentierten Dienstleister; alles andere bleibt anonymisierte Nutzung oder Sperrfall.

## Output

- Toolklassifikation
- Datenfreigabeentscheidung
- Lückenliste für Anbieterfragen
- Hinweis, ob Mandanteninformation oder Einwilligung zu prüfen ist

## 2. `datentransfer-eu-drittstaat`

**Fokus:** Datentransfer EU nach Drittstaat: Angemessenheitsbeschluss EU-US-Data-Privacy-Framework, Standardvertragsklauseln Modul 2, Transfer Impact Assessment nach EuGH Schrems II. Pruefraster fuer US-KI-Anbieter, technische Massnahmen wie Tokenisierung, Pseudonymisierung. Schriftsatzbausteine.

# EU- nach Drittstaat-Datentransfer

## Spezialwissen: EU- nach Drittstaat-Datentransfer
- **Spezialgegenstand:** EU- nach Drittstaat-Datentransfer / datentransfer eu drittstaat. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU, US, II, KI.
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

## 3. `erforderlichkeit-dokumentieren`

**Fokus:** Prüfe die Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenüber dem KI-Dienstleister nach Absatz eins der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). Bezugspunkt ist der Zweck der konkreten Offenlegung, nicht die abstrakte KI-Strategie der Kanzlei. Erstelle einen internen Compliance-Vermerk mit Beurteilungsspielraum und Grenzen.

# Erforderlichkeit dokumentieren

## Fachkern: Erforderlichkeit dokumentieren

- **KI-/Berufsrechtsproblem (Erforderlichkeit dokumentieren):** Prüfe die Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenüber dem KI-Dienstleister nach Absatz eins der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). Bezugspunkt ist der Zweck der konkreten Offenlegung, nicht die abstrakte KI-Strategie der Kanzlei. Erstelle einen internen Compliance-Vermerk mit Beurteilungsspielraum und Grenzen.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Norm

Pro Beruf wird auf Absatz 1 der jeweiligen Dienstleisterregelung verwiesen. Diese Vorschriften sind nahezu wortgleich:

- § 43e Abs. 1 BRAO: Der Rechtsanwalt darf Dienstleistern den Zugang zu Tatsachen eröffnen, auf die sich die Verpflichtung zur Verschwiegenheit gemäß § 43a Abs. 2 BRAO bezieht, soweit dies für die Inanspruchnahme der Dienstleistung erforderlich ist.
- § 62a Abs. 1 StBerG — wortgleich für Steuerberater bezogen auf § 57 Abs. 1 StBerG.
- § 50a Abs. 1 WPO — wortgleich für Wirtschaftsprüfer.
- § 39c Abs. 1 PAO — wortgleich für Patentanwalt bezogen auf § 39a Abs. 2 Satz 1 PAO.
- § 26a Abs. 1 BNotO — wortgleich für Notar bezogen auf § 18 BNotO. Beim Notar wird ausdrücklich klargestellt, dass die Eröffnung "ohne Einwilligung der Beteiligten" zulässig ist (Abs. 1 Satz 1).

## Bezugspunkt der Erforderlichkeit

Maßgeblich ist nicht, ob die Kanzlei KI braucht — diese unternehmerische Entscheidung wird vorausgesetzt. Maßgeblich ist, ob die konkrete Offenlegung der Mandatsdaten gegenüber dem konkreten Dienstleister für den konkreten Zweck erforderlich ist. Der Beurteilungsspielraum der Kanzlei ist nicht grenzenlos, aber praktisch relevant.

Praktisch heißt das: Wer ein Tool zur Vertragsanalyse einsetzt, muss nicht begründen, warum er überhaupt KI nutzt. Er muss begründen, warum die Offenlegung der Mandatsdaten gegenüber genau diesem Anbieter zur Erfüllung dieses Zwecks erforderlich ist.

## Erforderlich ≠ unerlässlich

Erforderlichkeit verlangt nicht, dass das Tool der einzig denkbare Weg ist. Es darf eine sinnvolle, fachlich gerechtfertigte Wahl sein. Die Kanzlei darf zwischen verschiedenen Anbietern abwägen — Preis, Funktionsumfang, Sicherheit. Diese Abwägung ist Teil der Berufsausübungsfreiheit, muss bei Mandatsgeheimnissen aber dokumentierbar bleiben.

## Grenzen

Bei zwei Konstellationen verlässt der Vorgang den Bereich des nach Abs. 1 Erforderlichen:

1. **KI-Training mit Mandatsdaten** — Die Übermittlung von Mandatsdaten zu allgemeinen Trainings- oder Modellverbesserungszwecken überschreitet regelmäßig den beauftragten Dienstleistungszweck. Hier muss vertraglich "no training" zugesichert sein.
2. **Datenmengen weit jenseits des Zwecks** — Wird das Tool nur für Recherche eingesetzt, müssen nicht alle Aktenbestandteile hochgeladen werden.

## Prüfpunkte am Vertrag

- Beschreibt der Vertrag den Verarbeitungszweck präzise?
- Ist der Zweck mit dem konkret geplanten Einsatz konsistent?
- Werden Daten erkennbar über den Zweck hinaus verarbeitet (Training, Statistik, Modellverbesserung)?
- Gibt es Zweckbindungsklauseln im Vertrag?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output

Interner Compliance-Vermerk mit:

- Beschreibung des konkreten Einsatzzwecks
- Begründung, warum die Offenlegung erforderlich ist
- Alternativen, die abgewogen wurden
- "no training"-Aussage im Vertrag (Fundstelle oder Lücke)
- Beurteilung Ampel: grün/gelb/rot

Der Vermerk geht zu den Kanzleiunterlagen. Er ist im Streitfall (etwa berufsrechtliches Verfahren) der zentrale Nachweis der Erforderlichkeit.

## Sonderfall Notar

Bei Dienstleistungen, die unmittelbar einem einzelnen Amtsgeschäft dienen (§ 26a Abs. 4 BNotO), ist die Einwilligung des Beteiligten erforderlich. Die Erforderlichkeit nach Abs. 1 bleibt davon unberührt, tritt aber neben das Einwilligungserfordernis.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- § 43e Abs. 1 BRAO, § 62a Abs. 1 StBerG, § 50a Abs. 1 WPO, § 39c Abs. 1 PAO, § 26a Abs. 1 BNotO — Erforderlichkeitsschwelle Berufsrecht
- Art. 5 Abs. 1 lit. c DSGVO — Datenminimierung (entsprechender Grundsatz)
- Art. 6 Abs. 1 DSGVO — Zulässigkeit der Verarbeitung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Einsatzzweck konkret benennen:** Was soll das Tool leisten? (Vertragsanalyse, Recherche, Schriftsatzentwurf, Dokumentenprüfung)
2. **Datenkategorien inventarisieren:** Welche Daten werden tatsächlich eingegeben? Mandatsschriftsätze? Urkunden? Bilanzen?
3. **Minimierungsprüfung:** Können Mandantendaten vor Eingabe anonymisiert oder pseudonymisiert werden, ohne Zweck zu verfehlen?
4. **Training-Prüfung:** Vertrag auf "no training"-Klausel prüfen (§ 5 AVV oder dedizierte Klausel). Falls fehlt → rote Ampel Training.
5. **Alternativen abwägen:** Gibt es EU-Anbieter ohne Drittlandrisiko? Ist der Vorteil des gewählten Anbieters sachlich gerechtfertigt?
6. **Vermerk schreiben:** Interne Dokumentation für Kanzleiunterlagen (Beweissicherung im berufsrechtlichen Verfahren).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Erforderlichkeit einer Verarbeitung dokumentieren | Zwei-Stufen-Pruefung nach Art. 5 Abs. 1 lit. c DSGVO; Template unten |
| Variante A — Verarbeitung klar nicht erforderlich | Stoppen empfehlen; Alternative vorschlagen |
| Variante B — Grenzfall mit starkem Interesse | Interessenabwaegung vertiefen; ausfuehrlichere Dokumentation |
| Variante C — besondere Kategorie (Art. 9 DSGVO) | Erhoehter Massstab; gesonderte Rechtsgrundlage noetig |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Compliance-Vermerk Erforderlichkeit

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Interner Compliance-Vermerk Erforderlichkeit
Datum: [DATUM] | Verfasser: [SACHBEARBEITER]
Anbieter: [NAME] | Produkt: [PRODUKT]
Norm-Basis: § [NORM] [GESETZ] Abs. 1

1. Einsatzzweck
[BESCHREIBUNG DES KONKRETEN EINSATZZWECKS]

2. Daten die eingegeben werden
[AUFLISTUNG DER DATENKATEGORIEN]

3. Begruendung Erforderlichkeit
[WARUM IST DIESE OFFENLEGUNG ERFORDERLICH]

4. Alternativen geprueft
[ALTERNATIVE ANBIETER ODER METHODEN; WARUM ABGELEHNT]

5. Training-Klausel
Vertrag Abschnitt [X]: "no training" zugesichert: ja / nein / Luecke
Falls Luecke: Handlungsbedarf [...]

6. Ampel
Erforderlichkeit: GRUEN / GELB / ROT
Begruendung: [...]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]
