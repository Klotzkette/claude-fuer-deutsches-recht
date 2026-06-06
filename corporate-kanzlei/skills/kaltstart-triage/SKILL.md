---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Corporate Kanzlei-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage."
---

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

# Corporate-Kanzlei — Allgemein

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Corporate-Kanzlei — Allgemein` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Corporate Kanzlei**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Corporate-Kanzlei-Plugin: Deal-Kommandocenter, Datenraum, Due Diligence, SPA/APA, Umwandlung, StaRUG, Insolvenzplan, W&I, Signing/Closing, PMI.

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
| `corporate-kanzlei-automation-monitoring` | Automationen und Monitoring: Entwirft Monitore für Datenraum-Neuzugaenge, Q&A-Status, CP-Deadlines, Registerupdates, MAR-Signale und PMI-Aufgaben im Corporate/M&A-Kontext. Normen: MAR Art. 17, § 41 GWB… |
| `corporate-kanzlei-billing-narratives` | Corporate Billing Narratives: Erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. Normen: RVG (wenn anwendbar), Stundenhonorar-Vereinbarung,… |
| `corporate-kanzlei-board-paper-business-judgment` | Board Paper und Business Judgment Rule (§ 93 AktG, § 43 GmbHG) erstellen: Vorlage für Vorstand/Geschäftsführung/Aufsichtsrat bei M&A-Entscheidungen, Strukturwahl, Risikotransaktionen. Prüfraster: Informationsgrundlage,… |
| `corporate-kanzlei-closing-bible-archiv` | Closing Bible und Deal-Archiv nach M&A-Closing erstellen: Mandant oder Partner benoetigt vollständige Vertragsdokumentation mit Signaturketten, Registerbelegen, Notarbestätigungen und Anlagen. Normen: SPA… |
| `corporate-kanzlei-conflict-gwg-sanctions` | Konflikt-, GwG- und Sanktionscheck: Mandatsannahmeprüfung für Corporate/M&A: Interessenkonflikte (§ 43a BRAO), wirtschaftlich Berechtigte (§§ 2 ff. GwG), Sanktionen (EU/US OFAC), PEP, Mittelherkunft, Sektor- und… |
| `corporate-kanzlei-datenqualitaet-xai-qualitaetskontrolle` | Qualitaetskontrolle und Quellenvalidierung im Corporate/M&A-Mandat: Partner oder Counsel prüft KI-generierte DD-Findings auf fehlerhafte Quellen, Luecken in der Belegkette und Black-Box-Schluesse. Normen: BRAO § 43a… |
| `corporate-kanzlei-datenraum-aufbau` | Virtuellen Datenraum strukturieren und befuellen für Private M&A, Public M&A, Carve-out und Distressed-Prozesse. Anwendungsfall: Verkaeuferkanzlei richtet DR ein oder Kaeufer hat Zugang erhalten. Normen: DSGVO Art. 28… |
| `corporate-kanzlei-datenraum-gap-clean-room` | Gap-Analyse des Datenraums und Clean-Room-Protokoll für M&A-Transaktionen: Identifiziert fehlende Dokumente, verwaltet IRL-Status (Information Request List), trennt sensible Wettbewerberdaten. Normen: DSGVO, GWB… |
| `corporate-kanzlei-deal-intake` | Neues Transaktionsmandat strukturiert aufnehmen aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message oder DR-Einladung. Anwendungsfall: Erster Mandantenkontakt oder Deal-Beauftragung eingetroffen. Normen: BRAO § 43a, GwG… |
| `corporate-kanzlei-deal-team-staffing` | Transaktionsteam zusammenstellen und Workstreams verteilen für M&A-Mandate: Senior Associate braucht Team-Plan oder Partner will Kapazitaeten ueberprüfen. Normen: BRAO § 43a (Interessenkonflikte), RVG/Stundenhonorar,… |
| `corporate-kanzlei-disclosure-schedules` | Disclosure Schedules zum SPA erstellen und prüfen: Verkaeufer offenbart bekannte Risiken um Warranty-Verletzungen nach § 444 BGB (Arglist) zu verhindern; Kaeufer prüft Vollständigkeit. Normen: § 444 BGB, § 311 Abs. 2… |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| `corporate-kanzlei-due-diligence-commercial-contracts` | Commercial Contracts Due Diligence: Prüft wesentliche Vertraege im M&A-Datenraum auf Change-of-Control-Klauseln, Kündigungsrechte, Exklusivitaet, Haftungsgrenzen und Material-Contract-Risiken für SPA-Reps. Normen: §§… |
| `corporate-kanzlei-due-diligence-legal` | Legal Due Diligence für M&A-Transaktionen: Prüft Corporate, Vertragswerk, HR, IP, Litigation und Compliance im Datenraum. Normen: §§ 311 Abs. 2 und 444 BGB sowie GmbHG, AktG, einschlaegige Sondergesetze. Prüfraster:… |
| `corporate-kanzlei-due-diligence-reporting` | DD-Reporting: Konsolidiert Legal, Tax, Financial und Commercial Due-Diligence-Workstreams zu einem integrierten DD-Bericht für M&A-Transaktionen. Normen: §§ 311 Abs. 2 und 444 BGB; SPA Representations & Warranties.… |
| `corporate-kanzlei-expert-calls-transkripte` | Expert Calls und Transkript-Auswertung in M&A-Due-Diligence: DD-Team führt Experten-Interviews durch und will strukturierte Findings extrahieren. Normen: § 17 UWG (Geschäftsgeheimnis), DSGVO Art. 6, MAR… |
| `corporate-kanzlei-fair-disclosure-knowledge` | Fair Disclosure und Knowledge Management: Steuert Informationsfluss in M&A-Transaktionen nach MAR, Kartellrecht-Clean-Team und Insider-Regelungen. Normen: Art. 17-18 MAR, §§ 1 und 41 GWB, § 43a BRAO. Insider-Log,… |
| `corporate-kanzlei-freundlicher-copilot` | Freundlicher Corporate-Copilot: Einstiegshilfe für alle Corporate/M&A-Aufgaben. Erklärt Fachbegriffe, gibt Überblicke zu Transaktionsstrukturen, beantwortet Erstfragen und leitet zu passenden Fach-Skills weiter. |
| `corporate-kanzlei-gesellschaftsrecht-register` | Gesellschaftsrechtliche Registeranmeldungen und Satzungsaenderungen durchführen: Handelsregister-Anmeldung von GF-Bestellung, Kapitalerhoehung, Satzungsaenderung, Verschmelzung. Normen: §§ 39-45 GmbHG, §§ 36-39 AktG,… |
| `corporate-kanzlei-handelsregisterabruf` | Handelsregister-Daten abrufen und analysieren: Anwalt oder Mandant benoetigt Gesellschaftsstruktur, Haftungsverhältnisse, Offenlegungspflichten aus HRA/HRB, Bundesanzeiger und Transparenzregister. Normen: §§ 8-15 HGB,… |
| `corporate-kanzlei-kaltstart` | Kaltstart Corporate-Kanzlei: Strukturiert den Einstieg in ein neues Corporate/M&A-Mandat mit Schnellerfassung von Parteien, Dealtyp, Phase, ersten Risiken und naechsten Schritten. Normen: BRAO §§ 43a, 49b; GwG § 10… |
| `corporate-kanzlei-kg-personengesellschaften` | KG und Personengesellschaften im Corporate/M&A-Kontext begleiten: Anteilsuebertragung, Haftungsstruktur, Ergebnisverwendung bei KG, GmbH & Co. KG, Partnerschaft und GbR nach MoPeG 2024. Normen: HGB §§ 105-177a, MoPeG… |
| `corporate-kanzlei-ki-governance-berufsrecht` | KI-Governance und Berufsrecht: Rechtliche Rahmenbedingungen für den Einsatz von KI-Werkzeugen in Kanzleien. EU-KI-VO (AI Act), BRAO-Verschwiegenheit, Mandanteninformation, Haftung, Qualitaetssicherung. Dokumentation… |
| `corporate-kanzlei-kommandocenter` | Deal-Kommandocenter Corporate/M&A: Schnellstart für Mandate. Erkennt Dealtyp, Phase und Parteiperspektive; erzeugt Deal-Karte mit Ampel, Rollen, naechster Aktion und Freigabegrad. Routet an passenden Fachmodul (SPA,… |
| `corporate-kanzlei-look-and-feel` | Corporate-Cowork-Design: Definiert die visuelle Oberflaeche für Partner, Counsel und Associates. Ruhig, edel, blaeulich-silbern; Orange für Entscheidungspunkte. Statuskarten, Ampeln und dichte Deal-Information statt… |
| `corporate-kanzlei-matter-file` | Transaktionsakte strukturieren und verwalten für Corporate/M&A-Mandate: Anwalt benoetigt Dokument-Klassifizierung, Versionskontrolle, Zugriffsrechteverwaltung und Aufbewahrungsplanung. Normen: §§ 257 HGB, 147 AO… |
| `corporate-kanzlei-output-versand-signing` | Signing-Management und Output-Verteilung für M&A-Vertraege: Koordiniert physisches und virtuelles Signing, Signaturseiten-Protokoll, qualifizierte eSignatur (QES), Exekution und Verteilung. Normen: §§ 126 und 126a und… |
| `corporate-kanzlei-outside-in-target-screening` | Outside-In-Zielunternehmen-Screening aus öffentlichen Quellen für M&A-Vorprüfung: M&A-Team benoetigt schnellen Überblick über Target ohne Datenraumzugang. Normen: § 3 GwG (UBO-Identifikation), DSGVO, WpHG §§ 33 ff.… |
| `corporate-kanzlei-post-closing-integration` | Post-Closing-Integration (PMI) rechtlich begleiten: Unmittelbar nach Closing muessen Handelsregister, Vertraege, Organ-Strukturen und Steuereinheiten angepasst werden. Normen: GmbHG, AktG, UmwStG, KStG (Organschaft), §… |
| `corporate-kanzlei-public-ma-kapitalmarkt-mar` | Public M&A und Kapitalmarkt: Begleitet Öffentliche Angebote (WpueG), Pflichtangebote, Squeeze-Out und Delisting. Normen: WpueG, AktG §§ 327a-f, WpHG/MAR Ad-hoc, §§ 39a-c WpueG. Leitsaetze BGH und BaFin-Praxis. |
| `corporate-kanzlei-qa-information-requests` | Q&A- und Information-Request-Management in M&A-Transaktionen: DD-Team erhaelt schriftliche Datenraum-Fragen und muss konsistente Antworten mit Disclosure-Wirkung erstellen. Normen: § 311 Abs. 2 BGB, Disclosure-Praxis… |
| `corporate-kanzlei-rechtsprechungsrecherche` | Corporate-Rechtsprechungsrecherche: Sucht und bewertet Urteile für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung. Liefert Fundstellenliste mit Aktenzeichen, Datum,… |
| `corporate-kanzlei-regulatory-fdi-merger-control` | Anmeldepflichten Fusionskontrolle und FDI prüfen: M&A-Transaktion erfordert Clearance. Normen: §§ 35 ff. GWB (deutsches Fusionskontrollrecht), Art. 1 ff. FKVO (EU-Fusionskontrolle), AWG/AWV (Investitionsprüfung),… |
| `corporate-kanzlei-restructuring-starug-insolvenzplan` | StaRUG-Restrukturierungsplan und Insolvenzplan für distressed Unternehmen: Schuldner oder Berater plant außergerichtliche Sanierung oder Insolvenzplanverfahren. Normen: §§ 7 ff. StaRUG (Planarchitektur), §§ 217 ff.… |
| `corporate-kanzlei-signing-closing-conditions` | Signing und Closing Conditions verwalten: M&A-Transaktion naehert sich Signing oder Closing und alle CPs muessen erledigt sein. Normen: § 158 BGB (Bedingungseintritt), SPA Conditions Precedent, § 41 GWB… |
| `corporate-kanzlei-simulation-bidder-process` | Auktionsprozess und Bieter-Perspektive in M&A-Transaktionen simulieren: Verkaeufer-Kanzlei plant Bieter-Prozess oder Kaeufer bereitet NBO/BO vor. Normen: SPA, WpueG (Public M&A), Marktstandard M&A-Auktion. Prüfraster:… |
| `corporate-kanzlei-spa-apa-entwurf` | SPA (Share Purchase Agreement) oder APA (Asset Purchase Agreement) entwerfen und strukturieren aus Term Sheet und DD-Findings. Normen: §§ 433 ff. BGB (Kaufrecht), § 444 BGB (Gewaehrleistung), §§ 311 Abs. 2 und 280 BGB.… |
| `corporate-kanzlei-steps-plan-pmo` | Steps Plan und Transaktions-PMO für M&A-Mandate erstellen: Deal-Team benoetigt Gesamtprojektplan mit Workstream-Koordination, CP-Tracking und Status-Reporting. Normen: SPA Closing Conditions, § 158 BGB. Prüfraster:… |
| `corporate-kanzlei-tabellenreview-3d-datenraum` | Strukturierte Datentabellen aus M&A-Datenräumen prüfen und qualitaetssichern: Vertragslisten, Litigation-Tracker, IP-Register, HR-Listen auf Luecken, Inkonsistenzen und Offenlegungsrisiken. Normen: § 311 Abs. 2 BGB,… |
| `corporate-kanzlei-teaser-im-processdocs` | Teaser, Information Memorandum und Prozessdokumente für M&A-Auktionsprozesse erstellen: Verkaeuferkanzlei oder Investmentbank benoetigt anonymisierten Teaser, IM und VDD. Normen: § 311 Abs. 2 BGB (vorvertragliche… |
| `corporate-kanzlei-transaktionsstruktur` | Transaktionsstruktur: Entwickelt und bewertet Transaktionsstrukturen für M&A (Share Deal, Asset Deal, Merger, Carve-out, Holding-Interposition). Normen: KStG, UmwStG, GrEStG, GmbHG, AktG. Leitentscheidungen BGH und BFH. |
| `corporate-kanzlei-translations-multijurisdictional` | Mehrsprachige Transaktionsdokumente in DE/EN erstellen und prüfen: Internationale M&A-Transaktion erfordert konsistente Terminologie in beiden Sprachen. Normen: § 184 GVG (Deutsch als Gerichtssprache), EGBGB Art. 10… |
| `corporate-kanzlei-umwandlungsrecht` | Umwandlungsrecht: Begleitet Verschmelzung, Spaltung, Formwechsel und Vermögensuebertragung nach UmwG. Normen: §§ 2-122 UmwG (Verschmelzung), §§ 123-173 UmwG (Spaltung), §§ 190-304 UmwG (Formwechsel).… |
| `corporate-kanzlei-umwandlungssteuerrecht` | Umwandlungssteuerrecht: Begleitet Verschmelzung, Spaltung und Formwechsel nach UmwStG auf Steuerneutralitaet, Buchwertfortführung, Sperrfristen, Verlustnutzung und Grunderwerbsteuer. Normen: §§ 11-25 UmwStG, §§ 1 ff.… |
| `corporate-kanzlei-vertragsmarkup-key-issues` | Juristischen Markup für M&A-Vertraege und Key-Issues-Memo erstellen: Gegenpartei hat SPA/SHA/NDA/LOI-Entwurf uebersandt und muss kommentiert werden. Normen: §§ 305 ff. BGB (AGB-Kontrolle im B2B), Marktstandard DE/UK… |
| `corporate-kanzlei-wi-insurance` | W&I-Versicherung (Warranty & Indemnity Insurance) strukturieren und prüfen: M&A-Berater braucht Policen-Analyse oder Underwriting-Vorbereitung. Normen: SPA Reps & Warranties, VVG, englisches Insurance-Recht… |

## Worum geht es?

Das Corporate-Kanzlei-Plugin ist das zentrale Arbeitswerkzeug fuer Corporate/M&A-Anwaeltinnen und -Anwaelte. Es deckt den vollstaendigen Transaktionszyklus ab: vom ersten Mandatseingang ueber Due Diligence, Vertragsentwurf, Regulatory Clearance, Signing und Closing bis zur Post-Merger-Integration.

Zusaetzlich unterstuetzt das Plugin bei gesellschaftsrechtlichen Registeranmeldungen, StaRUG-Restrukturierungsplaenen, Distressed-M&A, Public M&A und Kapitalmarkttransaktionen. Es richtet sich an Partner, Counsel und Senior Associates in Transaktionskanzleien sowie an Corporate-Inhouse-Juristen.

## Wann brauchen Sie diese Skill?

- Ein neues M&A-Mandat geht ein und muss strukturiert aufgenommen, auf Konflikte gepruefsft und mit einer Deal-Karte versehen werden.
- Eine Due-Diligence-Phase beginnt und Datenraum, Q&A-Management und DD-Reporting muessen koordiniert werden.
- Ein SPA-Entwurf der Gegenseite muss in Markup-Form mit Key-Issues-Memo kommentiert werden.
- Ein Closing naehert sich und alle Conditions Precedent sowie Closing-Deliverables muessen getrackt werden.
- Ein Unternehmen befindet sich in der Krise und ein StaRUG-Restrukturierungsplan oder Insolvenzplan wird benoetigt.

## Fachbegriffe (kurz erklaert)

- **SPA** — Share Purchase Agreement; Anteilskaufvertrag bei Share Deals.
- **APA** — Asset Purchase Agreement; Vermoegensuebertragungsvertrag bei Asset Deals.
- **Due Diligence** — Sorgfaeltige Pruefung des Zielunternehmens in rechtlichen, steuerlichen und wirtschaftlichen Bereichen vor Transaktionsabschluss.
- **W&I-Versicherung** — Warranty & Indemnity Insurance; Versicherung gegen Garantieverletzungen im SPA.
- **CP** — Condition Precedent; aufschiebende Bedingung, die vor Closing erfuellt sein muss.
- **StaRUG** — Unternehmensstabilisierungs- und -restrukturierungsgesetz; aussergerichltiches Restrukturierungsverfahren fuer Unternehmen in der Krise.
- **PMI** — Post-Merger-Integration; rechtliche Nachlaufarbeiten nach Closing (Registeranmeldungen, Vertragsanpassungen, Organschaft).
- **MAR** — EU-Marktmissbrauchsverordnung; regelt Insiderinformationen und Ad-hoc-Meldepflichten bei Public M&A.

## Rechtsgrundlagen

- §§ 433 ff. BGB (Kaufrecht, Gewaehrleistung)
- § 444 BGB (Arglistige Verschweigung)
- §§ 311 Abs. 2 und 280 BGB (Vorvertragliche Pflichten)
- §§ 35 ff. GWB (Fusionskontrolle)
- §§ 1 ff. WpueG (Wertpapiererwerbs- und Uebernahmegesetz)
- §§ 7 ff. StaRUG (Restrukturierungsplan)
- §§ 217 ff. InsO (Insolvenzplan)
- Art. 17-18 MAR (Ad-hoc-Publizitaet, Insider-Register)
- §§ 2-122 UmwG (Verschmelzung), §§ 123-173 UmwG (Spaltung)
- §§ 11-25 UmwStG (Steuerliche Behandlung Umwandlung)

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandatseingang strukturiert aufnehmen: Dealtyp, Phase, Parteiperspektive bestimmen (`corporate-kanzlei-deal-intake`).
2. Konflikt-, GwG- und Sanktionscheck durchfuehren (`corporate-kanzlei-conflict-gwg-sanctions`).
3. Passenden Prüfungslinie auswaehlen (Due Diligence, SPA, Regulatory, StaRUG, Kapitalmarkt).
4. Eilfristen pruefen: Vollzugsverbot § 41 GWB, MAR-Fristen, Anmeldepflichten FDI.
5. Anschluss-Skill bestimmen: Closing, Archivierung oder PMI?

## Skill-Tour (was gibt es hier?)

- `corporate-kanzlei-kommandocenter` — Deal-Kommandocenter: Schnellstart, Deal-Karte erstellen, Routing an Fachmodule.
- `corporate-kanzlei-kaltstart` — Kaltstart fuer neues Corporate/M&A-Mandat mit Schnellerfassung und Ampel.
- `corporate-kanzlei-deal-intake` — Neues Transaktionsmandat aus E-Mail, Teaser, NDA oder DR-Einladung strukturiert aufnehmen.
- `corporate-kanzlei-deal-team-staffing` — Transaktionsteam zusammenstellen und Workstreams verteilen.
- `corporate-kanzlei-conflict-gwg-sanctions` — Konflikt-, GwG- und Sanktionscheck bei Mandatsannahme.
- `corporate-kanzlei-outside-in-target-screening` — Zielunternehmen aus oeffentlichen Quellen screenen ohne Datenraumzugang.
- `corporate-kanzlei-teaser-im-processdocs` — Teaser, Information Memorandum und Prozessdokumente fuer M&A-Auktionen erstellen.
- `corporate-kanzlei-simulation-bidder-process` — Auktionsprozess und Bieter-Perspektive simulieren.
- `corporate-kanzlei-transaktionsstruktur` — Transaktionsstrukturen (Share Deal, Asset Deal, Merger, Carve-out) entwickeln und bewerten.
- `corporate-kanzlei-datenraum-aufbau` — Virtuellen Datenraum strukturieren und befuellen fuer Private und Public M&A.
- `corporate-kanzlei-datenraum-gap-clean-room` — Gap-Analyse des Datenraums und Clean-Room-Protokoll erstellen.
- `corporate-kanzlei-qa-information-requests` — Q&A- und Information-Request-Management in M&A-Transaktionen.
- `corporate-kanzlei-due-diligence-legal` — Legal Due Diligence: Corporate, Vertragswerk, HR, IP, Litigation und Compliance pruefen.
- `corporate-kanzlei-due-diligence-commercial-contracts` — Commercial Contracts Due Diligence: Change-of-Control-Klauseln, Kuendigungsrechte, Haftungsgrenzen pruefen.
- `corporate-kanzlei-due-diligence-reporting` — DD-Reporting: Legal, Tax, Financial und Commercial Workstreams konsolidieren.
- `corporate-kanzlei-expert-calls-transkripte` — Expert Calls und Transkript-Auswertung in der M&A-Due-Diligence.
- `corporate-kanzlei-tabellenreview-3d-datenraum` — Strukturierte Datentabellen aus Datenraeumen pruefen und qualitaetssichern.
- `corporate-kanzlei-fair-disclosure-knowledge` — Fair Disclosure und Knowledge Management: Informationsfluss nach MAR und Kartellrecht steuern.
- `corporate-kanzlei-spa-apa-entwurf` — SPA oder APA aus Term Sheet und DD-Findings entwerfen und strukturieren.
- `corporate-kanzlei-disclosure-schedules` — Disclosure Schedules zum SPA erstellen und pruefen.
- `corporate-kanzlei-vertragsmarkup-key-issues` — Juristischen Markup fuer M&A-Vertraege und Key-Issues-Memo erstellen.
- `corporate-kanzlei-wi-insurance` — W&I-Versicherung strukturieren und Police auf Deckungsluecken pruefen.
- `corporate-kanzlei-regulatory-fdi-merger-control` — Anmeldepflichten Fusionskontrolle und FDI-Investitionspruefung pruefen.
- `corporate-kanzlei-public-ma-kapitalmarkt-mar` — Public M&A, Pflichtangebote, Squeeze-Out und MAR-Ad-hoc begleiten.
- `corporate-kanzlei-signing-closing-conditions` — Signing und Closing Conditions verwalten und CP-Tracker fuehren.
- `corporate-kanzlei-output-versand-signing` — Signing-Management und Output-Verteilung fuer M&A-Vertraege koordinieren.
- `corporate-kanzlei-closing-bible-archiv` — Closing Bible und Deal-Archiv nach M&A-Closing erstellen.
- `corporate-kanzlei-post-closing-integration` — Post-Closing-Integration rechtlich begleiten: Register, Vertraege, Organschaft, § 613a BGB.
- `corporate-kanzlei-steps-plan-pmo` — Steps Plan und Transaktions-PMO fuer M&A-Mandate erstellen.
- `corporate-kanzlei-automation-monitoring` — Monitore fuer Datenraum-Neuzugaenge, Q&A-Status, CP-Deadlines und Registerupdates entwerfen.
- `corporate-kanzlei-restructuring-starug-insolvenzplan` — StaRUG-Restrukturierungsplan und Insolvenzplan fuer distressed Unternehmen erstellen.
- `corporate-kanzlei-distressed-ma` — Unternehmenskaeufe aus Insolvenz oder Krise begleiten.
- `corporate-kanzlei-umwandlungsrecht` — Verschmelzung, Spaltung, Formwechsel und Vermoegensuebertragung nach UmwG begleiten.
- `corporate-kanzlei-umwandlungssteuerrecht` — Umwandlungen auf Steuerneutralitaet, Buchwertfortfuehrung und Sperrfristen pruefen.
- `corporate-kanzlei-gesellschaftsrecht-register` — Handelsregister-Anmeldungen und Satzungsaenderungen durchfuehren.
- `corporate-kanzlei-handelsregisterabruf` — Handelsregister-Daten abrufen und Gesellschaftsstruktur analysieren.
- `corporate-kanzlei-kg-personengesellschaften` — KG und Personengesellschaften im Corporate/M&A-Kontext begleiten (MoPeG 2024).
- `corporate-kanzlei-translations-multijurisdictional` — Mehrsprachige Transaktionsdokumente in DE/EN erstellen und pruefen.
- `corporate-kanzlei-rechtsprechungsrecherche` — Corporate/M&A-Rechtsprechung suchen und fuer Vertraege und Board Papers aufbereiten.
- `corporate-kanzlei-matter-file` — Transaktionsakte strukturieren, versionieren und Aufbewahrungsplanung erstellen.
- `corporate-kanzlei-billing-narratives` — Time Narratives, Phasenbudgets und Workstream-Rechnungen erstellen.
- `corporate-kanzlei-datenqualitaet-xai-qualitaetskontrolle` — KI-generierte DD-Findings auf fehlerhafte Quellen und Luecken pruefen.
- `corporate-kanzlei-ki-governance-berufsrecht` — KI-Governance und Berufsrecht fuer den Einsatz von KI-Werkzeugen in der Kanzlei.
- `corporate-kanzlei-board-paper-business-judgment` — Board Paper und Business Judgment Rule-Dokumentation fuer M&A-Entscheidungen erstellen.
- `corporate-kanzlei-freundlicher-copilot` — Einstiegshilfe fuer Corporate/M&A-Aufgaben: Fachbegriffe erklaeren, Erstfragen beantworten, Skills verweisen.
- `corporate-kanzlei-look-and-feel` — Corporate-Cowork-Design: visuelle Oberflaeche fuer Partner, Counsel und Associates.

## Worauf besonders achten

- Konflikt- und GwG-Check ist vorgelagert: Kein Mandat starten, bevor Interessenkonflikte und wirtschaftlich Berechtigte geprueft sind.
- Fusionskontrolle-Vollzugsverbot nach § 41 GWB gilt bis zur Freigabe: Closing ohne Clearance ist bussgeldrelevant.
- MAR-Insider-Abgrenzung bei Public-M&A: Alle Deal-Team-Mitglieder muessen im Insider-Register erfasst werden.
- W&I-Versicherung beeinflusst Disclosure-Strategie: Underwriting-Prozess laeuft parallel zur DD — fruehzeitig koordinieren.
- StaRUG setzt Anzeigepflicht voraus: Drohende Zahlungsunfaehigkeit muss dem Restrukturierungsgericht angezeigt werden.

## Typische Fehler

- Deal-Intake ohne CP-Tracking-Aufbau: Closing-Bedingungen werden spaeter nicht strukturiert verwaltet.
- Disclosure Schedules als Formalitaet behandelt: Lueckenhafte Offenbarung kann zu Warrany-Haftung nach § 444 BGB fuehren.
- PMI unterschaetzt: Registeranmeldungen und § 613a-Informationen nach Closing werden verzoegert — Fristen laufen.
- Umwandlungssteuerrecht getrennt von Umwandlungsrecht betrachtet: Sperrfristen koennen rueckwirkend ausgeloest werden.
- Expert Calls ohne Insider-Abgrenzungs-Check: Informationsaustausch mit Experten kann MAR-pflichtig sein.

## Querverweise

- `geldwaeschepraevention-aml-kyc` — GwG-Konfliktrack und Sanktionscheck bei M&A-Mandaten.
- `datenschutzrecht` — DSGVO-Schnittstellen bei Datenraeumen und DD-Dokumentation.
- `regulatorisches-recht` — Fusionskontrolle (GWB) und FDI-Investitionspruefung (AWG/AWV) als Regulatory-Workstream.
- `vertragsrecht` — Allgemeine Vertragspruefung fuer nicht-M&A-Vertraege im Transaktionsumfeld.
- `energierecht` — Energiesektor-Transaktionen mit regulatorischen Sonderanforderungen.

## Quellen und Aktualitaet

- Stand: 05/2026
- BGB in der zum Stand-Datum geltenden Fassung
- GWB in der geltenden Fassung
- UmwG und UmwStG in der geltenden Fassung
- StaRUG in der geltenden Fassung
- MAR (EU 596/2014) in der geltenden Fassung
