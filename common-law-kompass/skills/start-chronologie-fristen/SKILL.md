---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Common Law Kompass-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage im Common Law Kompass."
---

# Common-Law-Kompass — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: England Limitation Act 1980 (6 Jahre Contract, 6 Jahre Tort), US-Statutes of Limitations einzelstaatlich (oft 3-6 Jahre), ICC-Schiedsverfahren Antwort 30 Tage.
- Tragende Normen verifizieren: Englisches Recht (Common Law / Equity), US-Recht (Restatements, UCC), Vergleich BGB-System, IPR-Anknüpfung (Rom I, Rom II), HCCH-Konventionen, New Yorker Übereinkommen (Schiedssprüche) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant mit US/UK-Bezug, Solicitor, Barrister, US-Attorney, deutscher Anwalt, Schiedsgericht (ICC, LCIA, ICDR), High Court, Court of Appeal.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Letter of Engagement, Statement of Claim / Particulars of Claim, Defence, Affidavit, Witness Statement, Discovery/Disclosure, Settlement Agreement — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Common Law Kompass**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Common-Law-Plugin für deutsche Wirtschaftsjuristen: UK/US-False-Friends, Vertragsbegriffe, Consideration, Suretyship, Indemnity, UCC, Precedent, Discovery und bilinguale Drafting-Reviews.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `common-law-begriffe-uebersetzung` | Deutscher Anwalt uebersetzt Vertrags- oder Rechtsbegriffe ins Englische und will funktionale nicht wörtliche Übersetzung. Anwendungsfall Vertragsverhandlung mit UK/US-Gegenpartei Memo an englischsprachigen Mandanten.… |
| `common-law-bilingual-contract-review` | Anwalt prüft deutschen und englischen Vertragstext auf Bedeutungsdrift Rangfolge Definitionskonflikte Haftungsrisiken. Anwendungsfall bilingualer SPA NDA oder Lizenzvertrag. Prüfraster Bedeutungsdrift-Analyse… |
| `common-law-client-explainer` | Mandant oder Business-Team versteht Common-Law-Konzepte nicht und braucht verstaendliche Erklärung. Anwendungsfall Deutsche kaufen UK-Unternehmen oder schließen US-Vertrag ab. Prüfraster Verstaendlichkeit… |
| `common-law-contract-formation-consideration` | Anwalt oder Mandant will Vertragsschluss-Grundlagen des Common Law verstehen: offer acceptance consideration deed promissory estoppel UCC. Anwendungsfall Transaktionsvertrag oder NDA mit UK/US-Gegenpartei. Prüfraster… |
| `common-law-false-friends-scanner` | Anwalt oder Übersetzer sucht missverstaendliche deutsch-englische Rechtsbegriffe im Vertragstext oder Memo. Anwendungsfall Vertragsentwurf mit False-Friend-Risiko. Prüfraster Begriff-Scan Risikoeinstufung sichere… |
| `common-law-governing-law-jurisdiction` | Vertragsparteien muessen Rechtswahlklausel Gerichtsstand und Durchsetzbarkeit für grenzüberschreitenden Vertrag klaeren. UK US oder deutsches Recht. Prüfraster Rechtswahl-Klausel Forum-Venue-Service Arbitrations-Option… |
| `common-law-humor-coach` | Common-Law-Erklärungen sollen für Mandanten oder Team leichter lesbar werden ohne Praezision zu verlieren. Anwendungsfall Onboarding-Dokument oder Mandanten-Erklärung. Prüfraster Verstaendlichkeit Ton-Angemessenheit… |
| `common-law-interpretation-precedent` | Deutscher Anwalt liest UK oder US-Gerichtsentscheidung und versteht Praezedenzfall-Logik nicht: ratio decidendi obiter dictum stare decisis Vertragsauslegung. Normen UK Supreme Court Rules US Federal Rules. Prüfraster… |
| `common-law-kommandocenter` | Kanzlei startet Common-Law- UK- US- oder bilinguales Drafting-Mandat und braucht strukturierten Einstieg. Jurisdiktionscheck False-Friends-Scan Arbeitsplan. Prüfraster Jurisdiktion-Identifikation… |
| `common-law-litigation-discovery` | Anwalt oder Mandant ist in UK/US-Gerichtsverfahren und will pleadings discovery disclosure depositions privilege evidence settlement verstehen. Prüfraster Verfahrensphasen-Überblick Privilege-Prüfung Discovery-Scope… |
| `common-law-ma-commercial-drafting` | Anwalt draftet oder prüft SPA APA NDA LOI Disclosure Schedules oder Commercial Agreement nach Common Law. Common-Law-Risikomatrix. Prüfraster Reps-Warranties-Covenants-Abgrenzung Boilerplate-Risiken Haftungsklauseln… |
| `common-law-quality-gate` | Fertig erstelltes Common-Law-Arbeitsprodukt auf Qualitaet prüfen: Jurisdiktion Quellenstand False Friends UK/US-Trennung Review-Bedarf. Prüfraster Jurisdiktion-Konsistenz Normen-Aktualitaet False-Friends-Scan… |
| `common-law-remedies-damages-equity` | Mandant erleidet Schaden aus UK/US-Vertrag oder Delikt und fragt nach Rechtsfolgen: damages specific performance injunction rescission restitution equitable relief punitive damages. Prüfraster Remedy-Auswahl… |
| `common-law-representations-warranties-covenants` | Anwalt ordnet Klauseln in Common-Law-Transaktionsvertraegen ein: reps warranties covenants conditions undertakings indemnities. Anwendungsfall SPA NDA oder Commercial Agreement. Prüfraster Klausel-Typ-Zuordnung… |
| `common-law-simulation-negotiation` | Anwalt oder Mandant will UK/US-Vertragsverhandlung oder Mandantengespraech simulieren und False-Friends-Lernkurve absolvieren. Prüfraster Verhandlungs-Simulation Issue-List-Erstellung Mandanten-Erklärung. Output… |
| `common-law-surety-guarantee-indemnity` | Anwalt prüft Sicherheitenklausel und muss zwischen Buergschaft Garantie suretyship guarantee indemnity primary obligation accessory liability unterscheiden. Prüfraster Klausel-Typ-Identifikation Akzessorietaet… |
| `common-law-ucc-sales-goods` | Anwalt prüft Warenkaufvertrag nach UCC oder Sale of Goods Act: title risk warranties perfect tender remedies. Anwendungsfall US-Kaufvertrag oder UK-Warengeschäft. Prüfraster UCC Art. 2 Sale-of-Goods-Act-Prüfung… |
| `common-law-us-vs-uk-drafting` | Anwalt muss zwischen British English English Law US contract style Delaware/New York-Konventionen und Business-English unterscheiden. Anwendungsfall Vertrag für UK- oder US-Gegenpartei. Prüfraster… |

## Worum geht es?

Dieses Plugin unterstuetzt deutsche Wirtschaftsjuristen beim Umgang mit englischem und US-amerikanischem Recht: Vertragsverhandlungen, bilinguale Drafting-Reviews, Jurisdiction-Auswahl, Common-Law-Konzepte (Consideration, Suretyship, Indemnity, UCC) und Prozessverfahren (Discovery, Pleadings). Es hilft, haeufige False-Friends zu erkennen, Klauseltypen korrekt einzuordnen und Mandanten verstaendlich ueber Common-Law-Risiken zu informieren.

Das Plugin ersetzt keine anwaltliche Zulassung im UK oder US-Recht, gibt aber strukturierte Orientierungshilfe und deckt die praxisrelevantesten Schnittstellen zwischen deutschem Recht und Common Law ab.

## Wann brauchen Sie diese Skill?

- Sie verhandeln einen SPA, APA, NDA oder Commercial Agreement mit einer UK- oder US-Gegenpartei und muessen Klauseln korrekt einordnen.
- Sie oder Ihr Mandant lesen ein englisches Gerichtsurteil und verstehen die Praezedenz-Logik nicht.
- Sie suchen einen bilingualen Vertragstext auf Bedeutungsdrift, Rangfolge-Konflikte und Definitions-Inkonsistenzen.
- Sie wollen Mandanten ueber Common-Law-Risiken informieren und benoetigen eine verstaendliche Erklaerung.
- Sie draften einen Vertrag für eine UK- oder US-Gegenpartei und muessen den richtigen Drafting-Stil waehlen.

## Fachbegriffe (kurz erklaert)

- **Consideration** — Im Common Law Grundvoraussetzung für einen bindenden Vertrag; beide Seiten muessen etwas versprechen oder leisten.
- **Deed** — Formvertrag im Common Law; erfordert Schriftform, Unterzeichnung und Uebergabe (delivery); benoetigt keine Consideration.
- **Indemnity** — Erstattungsversprechen; eigenstaendige Zahlungspflicht unabhaengig davon, ob der Hauptschuldner zahlt; nahezu § 311 BGB-fremd.
- **Guarantee** — Buergschaftsaehnlich akzessorisch; der Garant haftet nur wenn der Hauptschuldner nicht leistet.
- **Warranty** — Garantieversprechen im Vertrag; Verletzung loest Schadensersatz aus, aber keine Anfechtung des Vertrags.
- **Representation** — Tatsachenerklaerung; Verletzung kann Anfechtung (rescission) und Schadensersatz ausloesen.
- **Covenant** — Zukunftsgerichtetes vertragliches Versprechen (Tun oder Unterlassen); laufende Verhaltenspflicht.

## Rechtsgrundlagen

- Art. 267 AEUV — Vorabentscheidungsverfahren (Abgrenzung EU- zu nationalem Recht)
- Regulation (EC) 593/2008 (Rome I) — Rechtswahlfreiheit bei internationalen Vertraegen
- § 305 ff. BGB — AGB-Recht (Abgrenzung zu Common-Law-Boilerplate)
- UCC Art. 2 (US) — Sale of Goods
- UK Sale of Goods Act 1979 — Warenkauf England/Wales
- Contracts (Rights of Third Parties) Act 1999 (UK) — Drittbeguenstigung

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: UK-Recht, US-Recht (welcher Staat) oder bilinguale Situation; Vertragstyp und Gegenpartei.
2. Phase des Mandats bestimmen: Vertragsschluss, Drafting/Review, Verhandlung, Litigation/Discovery oder Mandanten-Erklaerung.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Limitation Periods (UK: Contracts Act 1980: sechs Jahre), Statute of Limitations (US: variiert nach Staat).
5. Anschluss-Skill bestimmen: nach False-Friends-Scan folgt typischerweise bilinguales Review oder Klauselkorrektur.

## Skill-Tour (was gibt es hier?)

**Einstieg und Navigation**

- `common-law-kommandocenter` — Schnellstart für Common-Law-Mandate; Jurisdiktionscheck und Routing zum passenden Einzel-Skill.
- `common-law-quality-gate` — Fertig erstelltes Common-Law-Arbeitsprodukt auf Jurisdiktion, Normen-Aktualitaet und False Friends pruefen.

**Sprachhilfen und False Friends**

- `common-law-false-friends-scanner` — Scan eines Vertragstexts oder Memos auf missverstaendliche deutsch-englische Rechtsbegriffe.
- `common-law-begriffe-uebersetzung` — Funktionale (nicht woertliche) Uebersetzung von Rechts- und Vertragsbegriffen ins Englische.
- `common-law-us-vs-uk-drafting` — Unterscheidung British English/English Law und US-Drafting-Konventionen.

**Vertragsrecht und Klauseln**

- `common-law-contract-formation-consideration` — Vertragsschluss-Grundlagen: offer, acceptance, consideration, deed und promissory estoppel.
- `common-law-representations-warranties-covenants` — Einordnung von Klauseltypen: reps, warranties, covenants, conditions, undertakings, indemnities.
- `common-law-surety-guarantee-indemnity` — Unterscheidung zwischen Buesch-aft (guarantee) und eigenstaendiger Erstattungspflicht (indemnity).
- `common-law-ucc-sales-goods` — Warenkaufvertraege nach UCC Art. 2 (US) und Sale of Goods Act (UK).
- `common-law-remedies-damages-equity` — Rechtsfolgen bei Vertragsverletzung: damages, specific performance, injunction, rescission.
- `common-law-governing-law-jurisdiction` — Rechtswahlklausel, Gerichtsstand und Schiedsverfahren für grenzueberschreitende Vertraege.

**Drafting und Review**

- `common-law-ma-commercial-drafting` — Drafting und Review von SPA, APA, NDA, LOI und Commercial Agreements nach Common Law.
- `common-law-bilingual-contract-review` — Bilinguale Vertragspruefung auf Bedeutungsdrift, Rangfolge-Konflikte und Haftungsrisiken.

**Praezedenz und Litigation**

- `common-law-interpretation-precedent` — Praezedenzfall-Logik: ratio decidendi, obiter dictum, stare decisis und Vertragsauslegung.
- `common-law-litigation-discovery` — Einfuehrung in UK/US-Prozessverfahren: pleadings, discovery, privilege, depositions, settlement.

**Mandantenkommunikation**

- `common-law-client-explainer` — Verstaendliche Erklaerung von Common-Law-Konzepten für Mandanten ohne rechtliche Ausbildung.
- `common-law-humor-coach` — Auflockerung von Common-Law-Erklaerungen ohne Verlust der Praezision.
- `common-law-simulation-negotiation` — Simulation einer UK/US-Vertragsverhandlung als Trainings- und Lernformat.

## Worauf besonders achten

- **Jurisdiktion vor allem anderen klaeren.** UK (England/Wales, Schottland, Nordirland) und US (welcher Bundesstaat) haben unterschiedliche Regelungen; kein generisches Common-Law.
- **Consideration-Pruefung bei jedem Vertrag.** Ohne Consideration ist ein Common-Law-Vertrag nicht bindend, es sei denn er ist als Deed ausgefuehrt.
- **Indemnity ist kein Schadensersatz.** Eine Indemnity-Klausel begrenzt Rechtsbehelfe auf Erstattung; Vergleich mit deutschem § 311 BGB fuehrt in die Irre.
- **Bilinguale Vertraege koennen Widersprueche erzeugen.** Prioritaet einer Sprachfassung muss explizit geregelt sein; Skill `common-law-bilingual-contract-review` schon bei Erstellung einsetzen.
- **Discovery ist deutlich umfangreicher als deutsches Beweisrecht.** US-Mandanten unterschaetzen haeufig die Kosten und den Umfang; Skill `common-law-litigation-discovery` für fruehe Aufklaerung.

## Typische Fehler

- Deutsche Anwaelte uebersetzen Begriffe woertlich und erzeugen False-Friend-Risiken (z.B. guarantee statt indemnity).
- Drafting-Stil wird nicht jurisdiktionsspezifisch angepasst; UK und US haben unterschiedliche Konventionen.
- Consideration-Element fehlt in selbst entworfenen Vertraegen; Vertrag wird im Streitfall als unverbindlich behandelt.
- Governing Law und Jurisdiction werden im gleichen Satz vermengt; das sind zwei separate Klauseln.
- Arbitration-Option wird nicht geprueft; bei Transaktionen mit US-Gegenpartei kann Schiedsgericht kostenguenstiger sein.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (UCC, Sale of Goods Act, Contracts Act 1980, Rome I, BGB)

