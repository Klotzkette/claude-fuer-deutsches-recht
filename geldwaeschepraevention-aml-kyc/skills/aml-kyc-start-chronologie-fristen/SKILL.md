---
name: aml-kyc-start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Geldwaeschepraevention AML KYC-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage im Geldwaeschepraevention Aml Kyc: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Geldwaeschepraeventition AML/KYC — Allgemein

## Arbeitsbereich

Einstieg, Schnelltriage und Fallrouting im Geldwaeschepraevention AML KYC-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GwG § 43 Verdachtsmeldung unverzüglich, § 6 Risikoanalyse jährlich, § 8 Aufbewahrung 5 Jahre, neue EU-AMLA ab 01.07.2025 operativ.
- Tragende Normen verifizieren: GwG §§ 1-59, EU-Geldwäsche-RL (5. und 6. AML), EU AML-Paket 2024 (VO 2024/1624, RL 2024/1640, AMLA-VO), KWG, ZAG, BörsG, BaFin-AuA, FATF-Empfehlungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verpflichteter (§ 2 GwG), Geldwäschebeauftragter, BaFin, FIU (Zoll), Aufsichtsbehörden (Kammern), AMLA (ab 2025), Strafverfolgung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Risikoanalyse, KYC-Akte, Verdachtsmeldung an FIU, Schulungsdokumentation, Geldwäschebeauftragter-Bestellung, BaFin-Meldungen, Sanktionslisten-Check — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Geldwaeschepraevention AML KYC**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Plugin für Geldwäscheprävention, AML, KYC, GwG-Risikoanalyse, UBO, PEP, Sanktionen, FIU/goAML, Transparenzregister und Behördenverfahren.

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
| `geldwaesche-audit-internal-revision` | Interne Revision und Audit der AML/KYC-Kontrollen nach GwG. Anwendungsfall Compliance-Beauftragter oder externer Prüfer will AML-Kontrollsystem auf Wirksamkeit prüfen. Normen § 4 GwG interne Sicherungsmassnahmen § 6… |
| `geldwaesche-behoerdenverfahren` | Begleitung von Behoerdenverfahren BaFin-Prüfungen FIU-Nachfragen und Massnahmenbescheiden. Anwendungsfall Aufsichtsbehoerde hat Auskunftsersuchen gestellt oder Vor-Ort-Prüfung angekündigt. Normen § 51 GwG… |
| `geldwaesche-bussgeld-reputation` | Strukturierung von Bußgeldriskien Geschäftsleiterhaftung und Reputationsschaeden bei GwG-Verstoessen. Anwendungsfall Bußgeldbescheid nach GwG ist eingegangen oder negative Berichterstattung droht. Normen § 52 GwG… |
| `geldwaesche-datenqualitaet-register` | Prüft Datenqualitaet im KYC-System und Transparenzregister-Abgleich. Anwendungsfall KYC-Daten enthalten Dubletten fehlerhafte Schreibweisen oder unvollständige UBO-Daten. Normen § 11 GwG Identifizierungspflicht § 20… |
| `geldwaesche-gruppenweite-compliance` | Gruppenweite AML/KYC-Policies und Steuerung von Tochtergesellschaften und Dienstleistern. Anwendungsfall Muttergesellschaft will gruppenweite AML-Compliance sicherstellen und Tochtergesellschaften einbinden. Normen § 9… |
| `geldwaesche-immobilien-gueterhaendler` | AML/KYC-Prüfung für Immobilienmakler Gueterhaendler Kunsthandel Edelmetalle und sonstige Nichtfinanzunternehmen. Anwendungsfall Makler oder Gueterhaendler will prüfen ob GwG-Pflichten bestehen und wie KYC-Prozesse… |
| `geldwaesche-kommandocenter` | Kommandocenter für alle Geldwäsche- KYC- Sanktions- und Behoerdenfaelle vom Intake bis zum Massnahmenplan. Anwendungsfall Compliance-Beauftragter oder Anwalt erhaelt neuen Fall und muss schnell den richtigen Workflow… |
| `geldwaesche-krypto-zahlungsdienstleister` | AML/KYC-Prüfung für Krypto-Assets Wallets Travel Rule und Zahlungsdienstleister. Anwendungsfall Krypto-Transaktion soll bewertet oder Krypto-Dienstleister muss KYC-Prozess aufsetzen. Normen § 2 Abs. 1 Nr. 10b GwG… |
| `geldwaesche-kyc-onboarding` | KYC-Onboarding neuer Kunden mit Identifizierung Risikoklassifizierung und Freigabe nach GwG. Anwendungsfall neue Geschäftsbeziehung soll aufgenommen werden und GwG-Identifizierung muss durchgeführt werden. Normen §§ 10… |
| `geldwaesche-pep-hochrisikoland` | Verstaerkte KYC-Prüfung für PEP politisch exponierte Personen Hochrisikolaender und komplexe Strukturen nach GwG. Anwendungsfall Kunde ist PEP oder kommt aus Hochrisikoland und verstaerkte Sorgfaltspflichten greifen.… |
| `geldwaesche-risikoanalyse-unternehmen` | Risikobasierte AML/CFT-Risikoanalyse nach § 5 GwG für Verpflichtete. Anwendungsfall Unternehmen muss gesetzlich vorgeschriebene Risikoanalyse erstellen oder aktualisieren. Normen § 5 GwG Risikoanalyse § 6 GwG interne… |
| `geldwaesche-sanktionsscreening` | Sanktionsscreening von Kunden Transaktionen und Beteiligten gegen EU-US- und UN-Sanktionslisten. Anwendungsfall neues Geschäft soll abgeschlossen oder Transaktion freigegeben werden. Normen EU-Verordnungen 2580/2001… |
| `geldwaesche-schulung-awareness` | Zielgruppengerechte AML/KYC-Schulungen und Awareness-Massnahmen nach § 6 Abs. 2 Nr. 6 GwG. Anwendungsfall jaehrliche Pflichtschulung muss durchgeführt oder neue Mitarbeiter eingearbeitet werden. Normen § 6 Abs. 2 Nr. 6… |
| `geldwaesche-sicherungsmassnahmen-icp` | Aufbau und Haertung interner Sicherungsmassnahmen ICP nach § 6 GwG. Anwendungsfall Verpflichteter muss ICP aufbauen oder bestehendes Kontrollsystem verbessern. Normen § 4 GwG Bestellung GwG-Beauftragter § 6 GwG interne… |
| `geldwaesche-simulation-testlauf` | Simulation eines Compliance-Arbeitstags mit Onboarding Alerts Verdachtsprüfung und Behoerdenfragen. Anwendungsfall Team will GwG-Workflows trainieren oder Plugin demonstrieren. Deckt Onboarding Alert UBO-Luecke… |
| `geldwaesche-transaktionsmonitoring` | Erkennung auffälliger Transaktionsmuster und Red-Flags im Zahlungsverkehr nach GwG. Anwendungsfall Bank oder Zahlungsdienstleister will Transaktion auf Geldwäscherisiko prüfen. Normen § 10 Abs. 1 Nr. 5 GwG… |
| `geldwaesche-transaktionsstopp-freeze` | Transaktionsstopp Kontoeinfrierung und Nichtdurchführung bei Sanktions- oder Verdachtstreffer. Anwendungsfall Transaktion muss gestoppt oder Konto eingefroren werden weil Sanktionstreffer oder konkreter Verdacht… |
| `geldwaesche-transparenzregister` | Transparenzregister-Einsicht Abgleich und Unstimmigkeitsmeldung nach GwG. Anwendungsfall wirtschaftlich Berechtigte muessen im Transparenzregister geprüft oder Unstimmigkeit gemeldet werden. Normen § 20 GwG… |
| `geldwaesche-ubo-wirtschaftlich-berechtigte` | Ermittlung wirtschaftlich Berechtigter UBO Kontrollketten und Trust-Stiftungsstrukturen nach GwG. Anwendungsfall neue Geschäftsbeziehung mit Unternehmen und wirtschaftlich Berechtigte muessen identifiziert werden.… |
| `geldwaesche-verdachtsmeldung-fiu-goaml` | Vorbereitung und Einreichung von Verdachtsmeldungen nach § 43 GwG über goAML-Portal an die FIU. Anwendungsfall Sachverhalt mit Verdacht auf Geldwäsche oder Terrorismusfinanzierung ist festgestellt und Meldung muss… |
| `geldwaesche-verpflichteten-check` | Prüft ob und in welcher Rolle ein Unternehmen oder Berufsstraeger nach GwG verpflichtet ist. Anwendungsfall Unternehmen oder Kanzlei will wissen ob GwG-Pflichten bestehen und welche Konsequenzen das hat. Normen § 2 GwG… |

## Worum geht es?

Dieses Plugin deckt das gesamte Geldwaesche-Praeventionsrecht nach dem Geldwaeschegesetz (GwG) ab. Es richtet sich an Compliance-Beauftragte, Rechtsanwaelte und Geldwaeschebeauftragte bei Banken, Zahlungsdienstleistern, Kreditinstituten, Immobilienmaklern, Gueterhaendlern und anderen Verpflichteten nach § 2 GwG.

Das Plugin unterstuetzt bei der risikobasierten Risikoanalyse, dem KYC-Onboarding neuer Kunden, der Pruefung politisch exponierter Personen (PEP), dem Sanktionsscreening, der Ermittlung wirtschaftlich Berechtigter (UBO), der Vorbereitung von Verdachtsmeldungen an die FIU ueber goAML sowie bei Behoerdenverfahren und internen Audits.

## Wann brauchen Sie diese Skill?

- Eine Bank oder ein Zahlungsdienstleister nimmt einen neuen Geschaeftskunden auf und muss KYC-Pruefungen nach § 10 GwG durchfuehren.
- Ein Compliance-Beauftragter entdeckt verdaechtige Transaktionen und prueft, ob eine Verdachtsmeldung nach § 43 GwG an die FIU eingereicht werden muss.
- Ein Immobilienmakler fragt, ob er nach § 2 Abs. 1 Nr. 14 GwG verpflichtet ist und welche Sorgfaltspflichten gelten.
- Ein Unternehmen will seine interne GwG-Risikoanalyse nach § 5 GwG aktualisieren.
- Eine Aufsichtsbehoerde (BaFin, Zollkriminalamt) fuehrt eine Pruefung durch und das Unternehmen braucht Verfahrensbegleitung.

## Fachbegriffe (kurz erklaert)

- **GwG** — Geldwaeschegesetz; setzt die 6. EU-Geldwaescherichtlinie um und regelt Sorgfaltspflichten fuer Verpflichtete.
- **KYC** — Know Your Customer; Kundenpruefungspflichten nach §§ 10-17 GwG: Identifizierung, Risikoklassifizierung, Monitoring.
- **UBO** — Ultimate Beneficial Owner (wirtschaftlich Berechtigter); Person mit mehr als 25 Prozent Beteiligung oder Kontrolle nach § 3 GwG.
- **PEP** — Politically Exposed Person (politisch exponierte Person); Personen in herausgehobenen oeffentlichen Aemtern mit erhoehtem Risikoprofil.
- **FIU** — Financial Intelligence Unit (Zentralstelle fuer Finanztransaktionsuntersuchungen); staatliche Behoerde, die Verdachtsmeldungen entgegennimmt.
- **goAML** — Meldeportal der FIU fuer elektronische Verdachtsmeldungen nach § 43 GwG.
- **ICP** — Internal Control Program (interne Sicherungsmassnahmen); Pflicht nach § 6 GwG fuer Verpflichtete ab bestimmter Groesse.
- **Transparenzregister** — Nationales Register der wirtschaftlich Berechtigten nach §§ 18-20 GwG.

## Rechtsgrundlagen

- §§ 1-4 GwG (Begriffsbestimmungen, Risikobasierter Ansatz)
- § 2 GwG (Verpflichtete)
- § 3 GwG (Wirtschaftlich Berechtigte)
- §§ 5-8 GwG (Risikoanalyse, Risikomanagement, interne Sicherungsmassnahmen)
- §§ 10-17 GwG (Allgemeine, vereinfachte und verstaerkte Sorgfaltspflichten)
- §§ 18-20 GwG (Transparenzregister)
- §§ 43-47 GwG (Meldepflichten, Verdachtsmeldung an FIU)
- EU-Sanktionsverordnungen (EU 2580/2001, EU 881/2002, EU 765/2006 u. a.)

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Verpflichteten-Status pruefen: Ist das Unternehmen nach § 2 GwG verpflichtet? (`geldwaesche-verpflichteten-check`)
2. Risikoprofil bestimmen: Risikoanalyse nach § 5 GwG erstellen oder aktualisieren (`geldwaesche-risikoanalyse-unternehmen`).
3. Konkreten Anwendungsfall einordnen: KYC-Onboarding, Verdachtspruefung, Sanktionsscreening, Behoerdenverfahren?
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Eilpflichten pruefen: Verdachtsmeldung unverzueglich, Transaktionsstopp sofortig.

## Skill-Tour (was gibt es hier?)

- `geldwaesche-kommandocenter` — Zentrales Steuerungsmodul fuer alle AML/KYC-Faelle vom Intake bis zum Massnahmenplan.
- `geldwaesche-verpflichteten-check` — Prueft ob und in welcher Rolle ein Unternehmen oder Berufsstraeger nach GwG verpflichtet ist.
- `geldwaesche-risikoanalyse-unternehmen` — Risikobasierte AML/CFT-Risikoanalyse nach § 5 GwG erstellen fuer Verpflichtete.
- `geldwaesche-kyc-onboarding` — KYC-Onboarding neuer Kunden mit Identifizierung, Risikoklassifizierung und Freigabe nach GwG.
- `geldwaesche-ubo-wirtschaftlich-berechtigte` — Wirtschaftlich Berechtigte, Kontrollketten und Trust-/Stiftungsstrukturen ermitteln nach GwG.
- `geldwaesche-pep-hochrisikoland` — Verstaerkte KYC-Pruefung fuer PEP, Hochrisikolaender und komplexe Strukturen nach GwG.
- `geldwaesche-sanktionsscreening` — Sanktionsscreening von Kunden, Transaktionen und Beteiligten gegen EU-, US- und UN-Sanktionslisten.
- `geldwaesche-transaktionsmonitoring` — Auffaellige Transaktionsmuster und Red-Flags im Zahlungsverkehr erkennen nach GwG.
- `geldwaesche-transaktionsstopp-freeze` — Transaktionsstopp, Kontosperrung und Nichtdurchfuehrung bei Sanktions- oder Verdachtstreffer.
- `geldwaesche-verdachtsmeldung-fiu-goaml` — Verdachtsmeldungen nach § 43 GwG vorbereiten und ueber goAML-Portal an die FIU einreichen.
- `geldwaesche-transparenzregister` — Transparenzregister-Einsicht, Abgleich und Unstimmigkeitsmeldung nach GwG.
- `geldwaesche-sicherungsmassnahmen-icp` — Interne Sicherungsmassnahmen (ICP) nach § 6 GwG aufbauen und haerten.
- `geldwaesche-gruppenweite-compliance` — Gruppenweite AML/KYC-Policies und Steuerung von Tochtergesellschaften und Dienstleistern.
- `geldwaesche-krypto-zahlungsdienstleister` — AML/KYC-Pruefung fuer Krypto-Assets, Wallets, Travel Rule und Zahlungsdienstleister.
- `geldwaesche-immobilien-gueterhaendler` — AML/KYC-Pruefung fuer Immobilienmakler, Gueterhaendler, Kunsthandel und Edelmetalle.
- `geldwaesche-datenqualitaet-register` — Datenqualitaet im KYC-System und Transparenzregister-Abgleich auf Dubletten und Fehler pruefen.
- `geldwaesche-schulung-awareness` — Zielgruppengerechte AML/KYC-Schulungen und Awareness-Massnahmen nach § 6 Abs. 2 Nr. 6 GwG.
- `geldwaesche-simulation-testlauf` — Simulation eines Compliance-Arbeitstags mit Onboarding, Alerts, Verdachtspruefung und Behoerdenfragen.
- `geldwaesche-behoerdenverfahren` — Begleitung von BaFin-Pruefungen, FIU-Nachfragen und Massnahmenbescheiden.
- `geldwaesche-bussgeld-reputation` — Bussgeldriskien, Geschaeftsleiterhaftung und Reputationsschaeden bei GwG-Verstoessen strukturieren.
- `geldwaesche-audit-internal-revision` — Interne Revision und Audit der AML/KYC-Kontrollen nach GwG durch Compliance-Beauftragten oder externen Pruefer.

## Worauf besonders achten

- Verdachtsmeldepflicht nach § 43 GwG ist unverzueglich — eine verzoegerte Meldung ist selbst bussgeldrelevant.
- Transaktionsstopp nach § 46 GwG greift vor dem Vollzug einer Transaktion — die Pflicht zur Nichtdurchfuehrung muss bekannt sein.
- UBO-Ermittlung bei Kettenstrukturen (Holding-Pyramiden, Trusts) ist besonders komplex; einfaches Gesellschaftsregister reicht nicht.
- Sanktionsscreening muss auch bei Bestandskunden bei neuen Sanktionsereignissen erneut durchgefuehrt werden.
- Krypto-Assets sind seit MiCA und den GwG-Aenderungen 2023 vollumfaenglich verpflichtet — Travel Rule (Art. 14 ff. MiCA-VO) beachten.

## Typische Fehler

- KYC-Onboarding ohne PEP-Screening: Neukunde ist politisch exponiert, wird aber als Standardkunde eingestuft.
- Keine regelmäßige Aktualisierung der Kundendaten: Risikoeinstufung veraltet, obwohl sich Eigentumsstruktur geaendert hat.
- Verdachtsmeldung verzoegert eingereicht: Interne Rechts- und Compliance-Schleife verzoegert Meldung ueber 24 Stunden hinaus.
- Gruppenweite Richtlinien nicht auf Tochterlandniveau heruntergebrochen: Lokale GwG-Anforderungen abweichend zu Gruppenpolicy.
- Immobilienmakler-Pflichten unterschaetzt: Barzahlungsverbot und KYC-Pflicht ab 10.000 Euro werden uebersehen.

## Querverweise

- `corporate-kanzlei` — GwG-Confliktcheck und Sanktionspruefung bei M&A-Transaktionen.
- `regulatorisches-recht` — BaFin-Aufsicht und MaRisk-Anforderungen fuer Finanzunternehmen.
- `datenschutzrecht` — KYC-Datenverarbeitung unterliegt DSGVO; Aufbewahrungspflichten versus Loeschpflicht.
- `vertragsrecht` — Geheimhaltungsklauseln und AML-Representations in Transaktionsvertraegen.

## Quellen und Aktualitaet

- Stand: 05/2026
- GwG in der zum Stand-Datum geltenden Fassung
- Gesetzesfassungen zum Stand-Datum
- FATF Recommendations (2023)
- EU-Geldwaescheverordnung (MLD6) in der Uebergangsphase

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
