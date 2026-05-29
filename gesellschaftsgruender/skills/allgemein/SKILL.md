---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Gesellschaftsgruender-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Spezial-Skills oder stellt genau eine gezielte Rückfrage."
---

<!-- konvers-stil-v1 -->

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Spezial-Skills dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Gesellschaftsgruender — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Gesellschaftsgruender**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Gründungsassistent deutsche Gesellschaften (GmbH UG GbR OHG KG GmbH und Co KG PartG mbB gGmbH). Von Rechtsformwahl über Gesellschaftsvertrag und Geschäftsführervertrag bis Notar Handelsregister Gewerbeamt Finanzamt Transparenzregister. MoPeG DiRUG GwG. Kein Ersatz für Anwaltsberatung.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Spezial-Skill aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
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
- **Primärer Pfad:** `skill-name` — [warum dieser Skill hilft]
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
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

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

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `gesellschaftsgruender-beirat-advisory-board` | Beirat oder Advisory Board für GmbH oder UG einrichten: Satzungsregelung, Bestellungsverfahren, Beratungsvertrag. Normen: §§ 45 52 GmbHG, §§ 95 ff. AktG analog. Prüfraster: Kompetenzen, Verguetung, Haftung, Abberufung,… |
| `gesellschaftsgruender-bilinguale-dokumente` | Gesellschaftsrechtliche Dokumente in Deutsch und Englisch erstellen: zweisprachige Satzung, Gesellschafterbeschluss, SHA. Normen: §§ 2 3 GmbHG, HGB. Prüfraster: rechtliche Verbindlichkeit der deutschen Fassung,… |
| `gesellschaftsgruender-cap-table` | Cap-Table für GmbH oder UG aufbauen und pflegen: Stammkapital, Gesellschafteranteile, Verwässerungsschutz. Normen: §§ 3 5 14 GmbHG. Prüfraster: aktuelle Anteile, Optionspools, Wandeldarlehen, Vesting-Schedule. Output:… |
| `gesellschaftsgruender-egbr-mopeg` | GbR nach MoPeG 2024 und Eintragung ins Gesellschaftsregister als eGbR vorbereiten. Normen: §§ 705 ff. BGB n.F. MoPeG, §§ 707 ff. BGB Gesellschaftsregister. Prüfraster: Eintragungsvoraussetzungen,… |
| `gesellschaftsgruender-firmenname-pruefung` | Firmenname auf Zulässigkeit und Verwechslungsgefahr prüfen: Differenzierungsgebot, Irreführungsverbot. Normen: §§ 17 18 HGB, § 4 GmbHG. Prüfraster: Unterscheidungskraft, Irreführungsverbot, Handelsregisterfähigkeit,… |
| `gesellschaftsgruender-genehmigtes-kapital` | Genehmigtes Kapital für GmbH oder AG in Satzung aufnehmen: Ermaechtigungsbeschluss, Hoechstbetrag, Bezugsrechtsausschluss. Normen: §§ 55a GmbHG, §§ 202 ff. AktG. Prüfraster: Ermaechtigungsrahmen, Fristen, Bezugsrechte,… |
| `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` | Pflichten des GmbH-Geschäftsführers in Gründungs- und Startphase: Stammkapitaleinzahlung, Insolvenzantragspflicht, Buchführung. Normen: §§ 35 43 64 GmbHG, § 15a InsO. Prüfraster: Handlungspflichten, Haftungsrisiken,… |
| `gesellschaftsgruender-geschaeftsfuehrervertrag` | Geschäftsführervertrag für GmbH-Geschäftsführer aufsetzen: Verguetung, Wettbewerbsverbot, Abberufung, Kündigungsfristen. Normen: §§ 35 38 GmbHG, BGB Dienstvertrag. Prüfraster: Verguetungsstruktur, Tantieme,… |
| `gesellschaftsgruender-geschaeftsordnung-gf` | Geschäftsordnung für GmbH-Geschäftsführung entwerfen: Ressortzuteilung, Zustimmungsvorbehalte, Berichtspflichten. Normen: §§ 35 37 GmbHG. Prüfraster: Kompetenzbereiche, interne Beschraenkungen, Zustimmungskataloge.… |
| `gesellschaftsgruender-gesellschafterstreit-eilantraege` | Eilmassnahmen im Gesellschafterstreit der GmbH: einstweilige Verfuegung gegen Mitgesellschafter oder Geschäftsführer. Normen: §§ 935 940 ZPO, §§ 37 38 GmbHG. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Arrest… |
| `gesellschaftsgruender-gesellschaftervereinbarung` | Gesellschaftervereinbarung (SHA) neben dem Gesellschaftsvertrag entwerfen: Vorkaufsrechte, Drag-Along, Tag-Along. Normen: §§ 705 ff. BGB, GmbHG. Prüfraster: schuldrechtliche Bindung, Satzungsrang, Durchsetzbarkeit,… |
| `gesellschaftsgruender-gesellschaftsvertrag-gmbh` | GmbH-Gesellschaftsvertrag aufsetzen: Mindestinhalt, Stammkapital, Beschlussfassung, Gewinnverteilung. Normen: §§ 2 3 5 GmbHG. Prüfraster: Notarerfordernis, Pflichtinhalte, Optionalklauseln, Sonderrechte. Output:… |
| `gesellschaftsgruender-gewerbeanmeldung-finanzamt` | Gewerbeanmeldung und steuerliche Ersterfassung nach GmbH-Gründung vorbereiten: Fragebogen Finanzamt, Gewerbeamt. Normen: § 14 GewO, AO, UStG. Prüfraster: Steuerklassen, USt-Voranmeldung, Betriebsstaette,… |
| `gesellschaftsgruender-gf-meeting-templates` | Vorlagen für Geschäftsführersitzungen und Protokolle erstellen: Tagesordnung, Beschlussprotokoll, Aktionsliste. Normen: §§ 35 ff. GmbHG. Prüfraster: Beschlussfähigkeit, Umlaufverfahren, Dokumentationspflichten. Output:… |
| `gesellschaftsgruender-gf-sozialversicherungs-status` | Sozialversicherungsrechtlichen Status des GmbH-Geschäftsführers klaeren: Pflichtversicherung vs. Befreiung bei beherrschendem Gesellschafter-GF. Normen: § 7 SGB IV, §§ 1 ff. SGB VI. Prüfraster: Beteiligungshoehe,… |
| `gesellschaftsgruender-gmbh-vorbereitung` | GmbH-Gründung vorbereiten: Gründerprüfung, Kapitalplanung, Notar-Auftrag, Gesellschafterliste. Normen: §§ 2 3 5 7 GmbHG. Prüfraster: Mindestkapital 25000 Euro, Einzahlungsnachweis, Gesellschafterkreis,… |
| `gesellschaftsgruender-golden-share-und-vetorechte` | Golden Shares und Vetorechte in GmbH oder AG satzungsmäßig absichern: Sonderrechte, Sperrminoritaeten. Normen: §§ 35 45 GmbHG, §§ 23 ff. AktG. Prüfraster: Satzungsgestaltung, Grenzen der Satzungsautonomie,… |
| `gesellschaftsgruender-gruender-intake` | Ersterfassung des Gründungsvorhabens: Rechtsform, Gesellschafterkreis, Kapital, Geschäftszweck. Normen: GmbHG, AktG, HGB. Prüfraster: Intake-Fragen Rechtsformwahl, Haftung, steuerliche Aspekte, Zeitplan. Output:… |
| `gesellschaftsgruender-gv-einladung-tagesordnung` | Gesellschafterversammlungs-Einladung und Tagesordnung nach GmbHG erstellen: Fristen, Formen, Mindestinhalt. Normen: §§ 49 51 GmbHG. Prüfraster: Ladungsfrist, Schriftform, Tagesordnungspunkte, Beschlussfähigkeit.… |
| `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter` | Gesellschafterversammlungs-Protokoll anfertigen und Versammlungsleitung durchführen. Normen: §§ 48 ff. GmbHG. Prüfraster: Protokollierungspflicht, Abstimmungsergebnis, Unterschriften, Formfehler. Output:… |
| `gesellschaftsgruender-handelsregister-anmeldung` | Erstanmeldung der GmbH zum Handelsregister vorbereiten: Notarauftrag, Eintragungsvoraussetzungen, Gründungsunterlagen. Normen: §§ 7 ff. GmbHG, §§ 12 ff. HGB. Prüfraster: Einzahlungsnachweis, Notarbeglaubigung,… |
| `gesellschaftsgruender-ihk-und-berufsgenossenschaft` | IHK-Pflichtmitgliedschaft und Berufsgenossenschafts-Anmeldung nach GmbH-Gründung erledigen. Normen: §§ 2 ff. IHKG, §§ 150 ff. SGB VII. Prüfraster: Branchenzuordnung BG, IHK-Beitragspflicht, Fristen. Output: Checkliste… |
| `gesellschaftsgruender-intake-decision-tree` | Entscheidungsbaum für GmbH-Gründung: Rechtsformwahl, Gründungsweg, Kapitalausstattung. Normen: GmbHG, AktG, PartGG, HGB. Prüfraster: Haftung, Steuer, Kapital, Gesellschafteranzahl. Output: Entscheidungsmatrix… |
| `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` | Kapitalerhöhung der GmbH mit und ohne Bezugsrecht der Gesellschafter durchführen. Normen: §§ 55 56 56a GmbHG. Prüfraster: Gesellschafterbeschluss, Bezugsrechtsausschluss, Einlageverpflichtung, Handelsregisteranmeldung.… |
| `gesellschaftsgruender-kg-und-gmbhcokg` | KG und GmbH und Co. KG gründen: Gesellschaftsvertrag, Haftungsstruktur, steuerliche Transparenz. Normen: §§ 161 ff. HGB, GmbHG. Prüfraster: Komplementaer-GmbH, Kommanditistenstellung, steuerliche Behandlung. Output:… |
| `gesellschaftsgruender-klauselkatalog-bilingual` | Klauselkatalog für GmbH-Satzung und SHA in Deutsch und Englisch: Standardklauseln für internationale Investoren. Normen: GmbHG, BGB. Prüfraster: Drag-Along, Tag-Along, Liquidationspräferenzen, Leaver-Klauseln. Output:… |
| `gesellschaftsgruender-kommandocenter` | Navigationszentrum für alle Gründungs-Skills: Fortschrittsanzeige, Delegierung an Fachinhalte, Status. Normen: GmbHG, AktG, HGB. Prüfraster: aktueller Gründungsstand, offene Schritte, Notartermin, Eintragungsstatus.… |
| `gesellschaftsgruender-notar-vorbereitung` | Notartermin für GmbH-Gründung vorbereiten: Unterlagencheck, Vollmachten, Ausweisanforderungen. Normen: §§ 2 7 GmbHG, BeurkG. Prüfraster: Gesellschafterliste, Musterprotokoll vs. individueller Gesellschaftsvertrag,… |
| `gesellschaftsgruender-online-gruendung-dirug` | Online-Gründung der GmbH nach DiRUG ohne persoenlichen Notartermin: Voraussetzungen, Verfahren, Grenzen. Normen: § 2 Abs. 3 GmbHG, DiRUG. Prüfraster: Musterprotokoll-Pflicht, Videoidentifikation, Beschraenkungen.… |
| `gesellschaftsgruender-rechtsformwahl` | Rechtsformwahl für Unternehmen: GmbH, UG, AG, GbR, PartG, KG, SE im Vergleich. Normen: GmbHG, AktG, PartGG, HGB, SE-VO. Prüfraster: Haftung, Steuern, Kapital, Mitbestimmung, Borsenreife. Output:… |
| `gesellschaftsgruender-sha-satzung-stimmverpflichtung` | Stimmbindungsvereinbarung und SHA-Regelungen zu Abstimmungspflichten in GmbH aufsetzen. Normen: §§ 47 48 GmbHG, BGB. Prüfraster: zulässige Stimmbindung, Durchsetzbarkeit, Vertragsstrafe, Grenze Satzungsautonomie.… |
| `gesellschaftsgruender-share-classes-a-b-c` | Anteilsklassen A, B, C in GmbH oder AG gestalten: unterschiedliche Gewinn-, Stimm- und Liquidationsrechte. Normen: §§ 29 47 GmbHG, §§ 11 12 AktG. Prüfraster: Satzungsgestaltung, steuerliche Wirkung,… |
| `gesellschaftsgruender-stammkapital-einzahlung` | Stammkapitaleinzahlung bei GmbH-Gründung nachweisen: Mindesteinzahlung, Bankbescheinigung, Sacheinlage. Normen: §§ 7 Abs. 2 und 19 GmbHG. Prüfraster: Mindesteinzahlung 50 Prozent, Bankbescheinigung, Sacheinlageprüfung,… |
| `gesellschaftsgruender-stammkapitalverlust-paragraf-49-gmbhg` | Hälftiger Stammkapitalverlust nach § 49 Abs. 3 GmbHG: Einberufungspflicht und Insolvenzprüfung. Normen: §§ 49 Abs. 3 64 GmbHG, § 15a InsO. Prüfraster: Bilanzkennzahlen, Einberufungspflicht, Haftungsrisiken GF. Output:… |
| `gesellschaftsgruender-transparenzregister` | Transparenzregister-Meldung für GmbH oder UG: wirtschaftlich Berechtigte, Fristen, Bußgelder. Normen: §§ 18 ff. GwG, GeldwäscheG. Prüfraster: Identifikation wirtschaftlich Berechtigter, Meldepflicht, Meldefristen,… |
| `gesellschaftsgruender-ug-vorbereitung` | UG haftungsbeschraenkt gründen: Musterprotokoll, Mindestkapital 1 Euro, Thesaurierungspflicht. Normen: § 5a GmbHG, §§ 2 3 GmbHG. Prüfraster: Stammkapital 1 Euro bis unter 25000 Euro, Musterprotokoll-Pflicht,… |

## Worum geht es?

Dieses Plugin begleitet Gruender, Anwaelte und Steuerberater durch den gesamten Prozess der Gruendung einer deutschen Gesellschaft — von der ersten Rechtsformwahl bis zur vollstaendigen Anmeldung bei allen relevanten Behoerden und Registern. Es deckt GmbH, UG (haftungsbeschraenkt), GbR, OHG, KG, GmbH und Co. KG, PartG mbB sowie gGmbH ab.

Die Skills unterstuetzen sowohl die Vorbereitung des Notartermins als auch die nachgelagerten Schritte: Handelsregisteranmeldung, Gewerbeamt, Finanzamt-Fragebogen, IHK, Berufsgenossenschaft und Transparenzregister. MoPeG (2024), DiRUG (Online-Gruendung) und GwG-Anforderungen sind integriert.

## Wann brauchen Sie diese Skill?

- Sie stehen am Anfang einer Gruendung und muessen die richtige Rechtsform fuer Haftung, Steuer und Kapitalausstattung auswaehlen.
- Sie bereiten einen Notartermin fuer eine GmbH- oder UG-Gruendung vor und benoetigen Checklisten und Unterlagensets.
- Sie moechten Gesellschaftsvertrag, Geschaeftsfuehrervertrag oder Gesellschaftervereinbarung (SHA) entwerfen lassen.
- Sie muessen nach der Gruendung alle Folgemeldungen (Gewerbeamt, Finanzamt, IHK, BG, Transparenzregister) abarbeiten.
- Sie beraten Mandanten bei Gesellschafterkonflikten oder strukturellen Fragen wie Anteilsklassen, Vetorechten oder Beirat.

## Fachbegriffe (kurz erklaert)

- **GmbH** — Gesellschaft mit beschraenkter Haftung; Mindestkapital 25.000 Euro; Haftung auf Gesellschaftsvermoegen beschraenkt.
- **UG (haftungsbeschraenkt)** — Unternehmergesellschaft; Mindestkapital 1 Euro; Pflicht zur Ruecklagenbildung (25 % des Jahresueberschusses) bis Stammkapital 25.000 Euro erreicht ist.
- **Stammkapital** — Das bei Gruendung aufgebrachte Grundkapital der GmbH oder UG; bei GmbH mindestens 25.000 Euro, davon mindestens 50 % bei Anmeldung einzuzahlen.
- **SHA (Shareholders Agreement)** — Gesellschaftervereinbarung schuldrechtlich neben dem Gesellschaftsvertrag; regelt Vorkaufsrechte, Drag-Along, Tag-Along, Leaver-Klauseln.
- **DiRUG** — Gesetz zur Umsetzung der Digitalisierungsrichtlinie; ermoeglicht Online-Gruendung per Videoidentifikation ohne persoenlichen Notartermin (nur Musterprotokoll).
- **MoPeG** — Gesetz zur Modernisierung des Personengesellschaftsrechts; in Kraft seit 01.01.2024; Neuregelung GbR, OHG, KG und eGbR-Register.
- **eGbR** — Eingetragene GbR nach §§ 707 ff. BGB n.F.; freiwillige Eintragung ins Gesellschaftsregister mit Rechtstraeigereigenschaft.
- **Wirtschaftlich Berechtigter** — Person mit mehr als 25 % Anteilen oder Stimmrechten; muss im Transparenzregister gemeldet werden (§§ 18 ff. GwG).

## Rechtsgrundlagen

- §§ 2 ff. GmbHG — Gruendung und Gesellschaftsvertrag der GmbH
- § 5a GmbHG — UG (haftungsbeschraenkt)
- §§ 7 ff. GmbHG — Anmeldung und Eintragung
- §§ 35 ff. GmbHG — Geschaeftsfuehrer, Vertretung
- §§ 43 ff. GmbHG — Haftung des Geschaeftsfuehrers
- §§ 47 ff. GmbHG — Gesellschafterversammlung, Beschlussfassung
- §§ 705 ff. BGB n.F. — GbR nach MoPeG
- §§ 161 ff. HGB — Kommanditgesellschaft
- §§ 17 ff. HGB — Firma (Firmenrecht)
- §§ 18 ff. GwG — Transparenzregister
- § 14 GewO — Gewerbeanmeldung
- § 7 SGB IV — Sozialversicherungsrechtlicher Status GF

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Wer gruendet, welcher Zweck, wie viele Gesellschafter, Kapitalausstattung.
2. Phase des Mandats bestimmen: Rechtsformwahl, Vertragsgestaltung, Notarvorbereitung oder Folgemeldungen.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Transparenzregister-Meldung innerhalb von zwei Wochen nach Eintragung; Gewerbeanmeldung vor Aufnahme des Betriebs.
5. Anschluss-Skill bestimmen: nach Notartermin folgen Handelsregisteranmeldung, Gewerbeanmeldung und Finanzamt-Fragebogen parallel.

## Skill-Tour (was gibt es hier?)

**Einstieg und Navigation**

- `gesellschaftsgruender-kommandocenter` — Navigationszentrum fuer alle Gruendungs-Skills mit Fortschrittsanzeige und Naechste-Schritte-Liste.
- `gesellschaftsgruender-gruender-intake` — Ersterfassung des Gruendungsvorhabens: Rechtsform, Gesellschafterkreis, Kapital, Geschaeftszweck.
- `gesellschaftsgruender-intake-decision-tree` — Entscheidungsbaum fuer Rechtsformwahl, Gruendungsweg und Kapitalausstattung.
- `gesellschaftsgruender-rechtsformwahl` — Vergleich GmbH, UG, AG, GbR, PartG, KG und SE mit Empfehlungsmatrix.

**GmbH-Gruendung**

- `gesellschaftsgruender-gmbh-vorbereitung` — Vorbereitung der GmbH-Gruendung mit Gruenderprüfung, Kapitalplanung und Notarauftrag.
- `gesellschaftsgruender-gesellschaftsvertrag-gmbh` — GmbH-Gesellschaftsvertrag mit Mindestinhalt, Stammkapital und Gewinnverteilungsregelung.
- `gesellschaftsgruender-stammkapital-einzahlung` — Nachweis der Stammkapitaleinzahlung und Bankbescheinigung fuer die Handelsregisteranmeldung.
- `gesellschaftsgruender-notar-vorbereitung` — Unterlagencheck, Vollmachten und Ausweisanforderungen fuer den Notartermin.
- `gesellschaftsgruender-online-gruendung-dirug` — Online-Gruendung nach DiRUG per Videoidentifikation ohne persoenlichen Notartermin.
- `gesellschaftsgruender-handelsregister-anmeldung` — Vorbereitung der Erstanmeldung beim Handelsregister mit Einzahlungsnachweis und HR-Formblatt.

**UG-Gruendung**

- `gesellschaftsgruender-ug-vorbereitung` — UG haftungsbeschraenkt gruenden mit Musterprotokoll, Mindestkapital und Thesaurierungspflicht.

**KG und Personengesellschaften**

- `gesellschaftsgruender-kg-und-gmbhcokg` — KG und GmbH und Co. KG gruenden mit Gesellschaftsvertrag und steuerlicher Transparenz.
- `gesellschaftsgruender-egbr-mopeg` — GbR nach MoPeG 2024 und Eintragung als eGbR vorbereiten.

**Gesellschaftsorgane und Innenrecht**

- `gesellschaftsgruender-geschaeftsfuehrervertrag` — Geschaeftsfuehrervertrag mit Verguetung, Wettbewerbsverbot und Abberufungsregelung.
- `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` — Pflichten des GF in der Gruendungs- und Startphase: Stammkapitaleinzahlung, Insolvenzantragspflicht, Buchfuehrung.
- `gesellschaftsgruender-geschaeftsordnung-gf` — Geschaeftsordnung fuer die GF mit Ressortzuteilung und Zustimmungsvorbehalten.
- `gesellschaftsgruender-gf-sozialversicherungs-status` — Sozialversicherungsrechtlichen Status des GF klaeren (Pflichtversicherung vs. Befreiung).
- `gesellschaftsgruender-beirat-advisory-board` — Beirat oder Advisory Board einrichten mit Satzungsregelung und Beratungsvertrag.
- `gesellschaftsgruender-gesellschaftervereinbarung` — Gesellschaftervereinbarung (SHA) mit Vorkaufsrechten, Drag-Along und Tag-Along.
- `gesellschaftsgruender-sha-satzung-stimmverpflichtung` — Stimmbindungsvereinbarung und SHA-Regelungen zu Abstimmungspflichten.
- `gesellschaftsgruender-golden-share-und-vetorechte` — Golden Shares und Vetorechte satzungsmaessig absichern.
- `gesellschaftsgruender-share-classes-a-b-c` — Anteilsklassen A, B, C mit unterschiedlichen Gewinn-, Stimm- und Liquidationsrechten.
- `gesellschaftsgruender-genehmigtes-kapital` — Genehmigtes Kapital in der Satzung aufnehmen mit Ermaechtigungsbeschluss und Bezugsrecht.
- `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` — Kapitalerhöhung der GmbH mit und ohne Bezugsrecht der Gesellschafter.
- `gesellschaftsgruender-stammkapitalverlust-paragraf-49-gmbhg` — Haelftiger Stammkapitalverlust nach § 49 Abs. 3 GmbHG: Einberufungspflicht und Insolvenzpruefung.

**Gesellschafterversammlung**

- `gesellschaftsgruender-gv-einladung-tagesordnung` — Gesellschafterversammlungs-Einladung und Tagesordnung nach §§ 49 ff. GmbHG.
- `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter` — GV-Protokoll anfertigen und Versammlungsleitung durchfuehren.
- `gesellschaftsgruender-gf-meeting-templates` — Vorlagen fuer GF-Sitzungen, Protokolle und Aktionslisten.

**Finanzierung und Cap-Table**

- `gesellschaftsgruender-cap-table` — Cap-Table aufbauen und pflegen mit Anteilsuebersicht und Verwässerungsrechnung.

**Streit und Eilmassnahmen**

- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — Eilmassnahmen im Gesellschafterstreit: einstweilige Verfuegung gegen Mitgesellschafter oder GF.

**Firmierung**

- `gesellschaftsgruender-firmenname-pruefung` — Firmenname auf Zulaessigkeit, Unterscheidungskraft und Irrefuehrungsverbot pruefen.

**Folgemeldungen und Register**

- `gesellschaftsgruender-gewerbeanmeldung-finanzamt` — Gewerbeanmeldung und steuerliche Ersterfassung nach GmbH-Gruendung.
- `gesellschaftsgruender-ihk-und-berufsgenossenschaft` — IHK-Pflichtmitgliedschaft und Berufsgenossenschafts-Anmeldung erledigen.
- `gesellschaftsgruender-transparenzregister` — Transparenzregister-Meldung fuer GmbH oder UG mit wirtschaftlich Berechtigten und Fristen.

**Dokumentation und bilinguale Unterlagen**

- `gesellschaftsgruender-bilinguale-dokumente` — Gesellschaftsrechtliche Dokumente in Deutsch und Englisch erstellen.
- `gesellschaftsgruender-klauselkatalog-bilingual` — Klauselkatalog fuer GmbH-Satzung und SHA in Deutsch und Englisch fuer internationale Investoren.

## Worauf besonders achten

- **Transparenzregister-Frist.** Nach Handelsregistereintragung besteht eine Meldefrist von zwei Wochen fuer wirtschaftlich Berechtigte (§ 20 GwG); bei Versaetzen drohen empfindliche Bussgelder.
- **Stammkapitaleinzahlung vor Anmeldung.** Mindestens 50 % des Stammkapitals muessen nachweislich eingezahlt sein, bevor die Handelsregisteranmeldung beim Notar unterzeichnet wird (§ 7 Abs. 2 GmbHG).
- **GF-Sozialversicherungsstatus klaeren.** Beherrschende Gesellschafter-GF sind haeufig nicht sozialversicherungspflichtig; Fehleinstufungen fuehren zu Nachzahlungen und Strafbarkeit.
- **Online-Gruendung nur mit Musterprotokoll.** DiRUG-Online-Gruendung ist nur zulassig bei Verwendung des gesetzlichen Musterprotokolls; individuelle Satzungsgestaltung erfordert Praesenz beim Notar.
- **MoPeG-Aenderungen beachten.** Seit 01.01.2024 gelten neue Regeln fuer GbR, OHG und KG; Alt-Gesellschaftsvertraege koennen Anpassungsbedarf haben.

## Typische Fehler

- Gesellschaftsvertrag wird ohne steuerliche Pruefung beim Notar beurkundet; Gewinnverteilung und Verguetungsregelungen koennen steuerlich nachteilig sein.
- Transparenzregister-Meldung wird als optional behandelt und vergessen; Bussgelder nach § 56 GwG sind erheblich.
- Geschaeftsfuehrervertrag wird nicht gleichzeitig mit dem Gesellschaftsvertrag abgeschlossen; spaetere Rueckwirkung ist problematisch.
- Kapitalerhöhungen werden ohne Pruefung des Bezugsrechts beschlossen; Gesellschafter koennen Anfechtungsklage erheben.
- DiRUG-Online-Gruendung scheitert, weil individuelle Klauseln aufgenommen werden sollen; Pruefung vor Notarbeauftragung vermeidet Doppelkosten.

## Querverweise

- `gesellschaftsrecht` — Fuer laufende gesellschaftsrechtliche Fragen nach der Gruendung (Beschluesse, Haftung, M&A).
- `mittelstand-corporate-ma` — Wenn die frisch gegruendete Gesellschaft Kaeufer oder Zielunternehmen in einer Transaktion ist.
- `insolvenzforderungsanmeldungspruefung` — Bei Insolvenz der Gesellschaft und Forderungsanmeldung.
- `subsumtions-pruefer` — Fuer rechtliche Einzelfragen im Gruendungsprozess (Normanwendung und Tatbestandsmerkmale).

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (GmbHG, AktG, HGB, BGB n.F. nach MoPeG, GwG, DiRUG, SGB IV, GewO)
