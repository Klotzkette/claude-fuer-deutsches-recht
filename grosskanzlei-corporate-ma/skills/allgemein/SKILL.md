---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Großkanzlei-Corporate/M&A-Plugin. Fragt Rolle, Erfahrungslevel, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Anfänger- oder First-Year-Associate-Bedarf routet der Skill in den Anfänger-Modus."
---

<!-- konvers-stil-v1 -->

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Spezial-Skills dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Grosskanzlei Corporate/M&A — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Großkanzlei Corporate/M&A**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Big-Law-Corporate/M&A-Plugin: Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, Umwandlung, StaRUG/Insolvenzplan, CP-Kalender, E-Rechnung/GoBD, PMI.

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
- **Primärer Pfad:** `grosskanzlei-corporate-ma-anfaenger-modus` oder passender Fachskill — kurze Begründung aus dem Material
- **Alternativen:** höchstens zwei weitere Plugin-Skills mit konkretem Nutzen
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Erfahrungslevel | Soll ich knapp wie für Fortgeschrittene arbeiten oder geführt wie für Anfänger/First-Year-Associates? | Anfänger-Modus einschalten, wenn Erklärung, Kleinschritte und Review-Gates gebraucht werden. |
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
3. **Arbeitsmodus wählen:** Anfänger-Modus, First-Year-Führung, Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
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
- Wenn der Nutzer Anfänger, First-Year-Associate, Trainee, Referendar oder unsicher ist, `grosskanzlei-corporate-ma-anfaenger-modus` als ersten Skill vorschlagen und die Aufgabe in Kleinschritte mit Begriffserklärungen und Senior-Review-Gates zerlegen.
- Bei neuen Chats gelegentlich kurz fragen: "Wie viel Führung brauchst du gerade: Anfänger, First-Year-Associate oder fortgeschritten?" Wenn Eilfristen erkennbar sind, diese Frage erst nach dem Fristenscan stellen.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: benennen, was als nächster verwertbarer Output entstehen soll.
- Rolle/Perspektive: Buy-side, Sell-side, Target, Vorstand/GF, Bank, Local Counsel oder unklar.
- Erfahrungslevel: Anfänger, First-Year-Associate, fortgeschritten oder nicht erkennbar.
- Eilt wegen: Frist, Closing, Signing, Filing, Q&A-Deadline oder keine Eile erkennbar.
- Fehlende Unterlagen: konkret benennen, was für den nächsten Schritt fehlt.

**Vorgeschlagener Workflow**
1. Frist und Deal-Phase sichern.
2. Unterlagen, Rolle und Ziel ordnen.
3. Passenden Plugin-Skill wählen und mit Review-Gate weiterarbeiten.

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `grosskanzlei-corporate-ma-anfaenger-modus` | bei Anfänger-/First-Year-Bedarf | geführter Kleinschrittplan mit Begriffen und Senior Review |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `grosskanzlei-corporate-ma-anfaenger-modus` | Anfänger- und First-Year-Associate-Modus: Wenn der Nutzer neu in M&A ist oder mehr Handführung wünscht. Fragt Erfahrungslevel, Deal-Phase, Aufgabe und Frist ab, erklärt Begriffe, zerlegt Aufgaben in Kleinschritte und setzt Senior-Review-Gates. |
| `grosskanzlei-corporate-ma-automation-monitoring` | Monitoring und Automatisierungen für laufende M&A-Mandate einrichten: Anwendungsfall Deal-Team benoetigt automatisierte Überwachung von Datenraum-Neuzugaengen Q&A-Deadlines CP-Fristen Registerupdates und MAR-Signalen.… |
| `grosskanzlei-corporate-ma-billing-narratives` | Big-Law Billing Narratives und Abrechnung für M&A-Mandate erstellen: Anwendungsfall Associate oder Partnerassistenz muss taugliche Time Narratives Phasenbudgets Workstream-Rechnungen Cap- und Success-Fee-Hinweise… |
| `grosskanzlei-corporate-ma-board-paper-business-judgment` | Board Paper und Business Judgment Rule Prüfung für M&A-Entscheidungen: Anwendungsfall Vorstand AG Geschäftsführer GmbH oder Aufsichtsrat muss Transaktionsentscheidung formal absichern. § 93 Abs. 1 Satz 2 AktG Business… |
| `grosskanzlei-corporate-ma-closing-bible-archiv` | Closing Bible und Deal-Archiv erstellen: Anwendungsfall Mandant oder Counsel braucht nach Signing/Closing vollständige Dokumentensammlung aller executed Agreements, Signaturseiten und Registerbelege. §§ 433 ff. BGB… |
| `grosskanzlei-corporate-ma-conflict-gwg-sanctions` | Mandatsannahme-Prüfung im Corporate/M&A-Mandat: Interessenkonflikte nach § 43a BRAO, Geldwäschegesetz-Prüfung wirtschaftlich Berechtigter nach § 3 GwG, Sanktionsscreening nach AWG und EU-Verordnungen. Anwendungsfall… |
| `grosskanzlei-corporate-ma-datenqualitaet-xai-qualitaetskontrolle` | KI-Qualitaetskontrolle und Halluzinations-Absicherung in M&A-Transaktionen: Anwendungsfall KI-generierte DD-Berichte, Klauseln oder Recherchen sollen auf Datenqualitaet, Bias und Black-Box-Risiken geprüft werden. Art.… |
| `grosskanzlei-corporate-ma-datenraum-aufbau` | Due Diligence Datenraum strukturieren und bestücken: Anwendungsfall Mandant bereitet Verkaufsprozess vor oder Buyer-Team benoetigt strukturierten Datenraum für Private M&A, Public M&A, Carve-out oder… |
| `grosskanzlei-corporate-ma-datenraum-gap-clean-room` | Datenraum-Lueckenanalyse und Clean-Room-Protokoll für M&A Due Diligence: Anwendungsfall Anwalt oder Mandant stellt fest dass Datenraum Luecken hat oder sensible Wettbewerbsdaten nur unter Clean-Room-Bedingungen geteilt… |
| `grosskanzlei-corporate-ma-deal-intake` | Neues M&A-Mandat aufnehmen und strukturieren: Anwendungsfall Partner oder Associate erhaelt Erstanfrage zu einer Transaktion und muss Deal-Profil, Rolle, Parteien, Zeitplan und Workstreams erfassen. §§ 3a RVG Honorar,… |
| `grosskanzlei-corporate-ma-deal-team-staffing` | Deal-Team-Besetzung und Staffing-Plan für Corporate/M&A-Transaktionen: Anwendungsfall Senior-Partner oder Team-Lead muss Workstreams Anwalt, Counsel, Associate, Paralegals und externe Spezialisten zuweisen. §§ 43a BRAO… |
| `grosskanzlei-corporate-ma-disclosure-schedules` | Disclosure Schedules und Guarantees-Abgleich im SPA/APA: Anwendungsfall Verkaeufer-Anwalt erstellt Disclosure Schedules zur Einschraenkung von Reps and Warranties oder Kaeufer prüft ob Disclosure ausreichend ist. §§… |
| `grosskanzlei-corporate-ma-distressed-ma` | Distressed M&A Transaktion begleiten: Anwendungsfall Unternehmen in Krise oder Insolvenz soll verkauft werden oder Investor prüft Erwerb notleidender Vermögenswerte. §§ 17-19 InsO Insolvenztatbestaende, § 1 StaRUG… |
| `grosskanzlei-corporate-ma-due-diligence-commercial-contracts` | Commercial Contracts Due Diligence im M&A-Datenraum: Anwendungsfall Kaeufer-Anwalt prüft wesentliche Kundenvertraege, Lieferantenvertraege, IP-Lizenzen, Change-of-Control-Klauseln und Kündigungsrechte. §§ 433 ff. BGB… |
| `grosskanzlei-corporate-ma-due-diligence-legal` | Legal Due Diligence im M&A-Prozess: Anwendungsfall Kaeufer-Anwalt prüft Corporate-Unterlagen, Rechtsstreitigkeiten, Regulatory-Status, Arbeitsrecht und IP der Zielgesellschaft. §§ 433 ff. BGB SPA-Garantien, § 93 AktG… |
| `grosskanzlei-corporate-ma-due-diligence-reporting` | Due Diligence Report erstellen und strukturieren: Anwendungsfall After DD-Phase muss Anwalt einen umfassenden DD-Bericht für Kaeufer-Management, Investitionskomitee oder Finanzierungsbank erstellen.… |
| `grosskanzlei-corporate-ma-expert-calls-transkripte` | Expert Calls und Transkript-Auswertung für M&A Due Diligence: Anwendungsfall Deal-Team hat Experteninterviews oder Management-Presentations transkribiert und muss Kernaussagen strukturiert extrahieren. MAR… |
| `grosskanzlei-corporate-ma-fair-disclosure-knowledge` | Fair Disclosure und Knowledge-Qualifikation in M&A-Vertraegen: Anwendungsfall Vertragsparteien verhandeln Wissenszurechnung, Kenntnis-Definitionen und Fair-Disclosure-Mechanismus im SPA. §§ 433 ff. BGB, § 442 BGB… |
| `grosskanzlei-corporate-ma-freundlicher-copilot` | Freundlicher M&A-Deal-Copilot für junge Anwaelte und Associates: Anwendungsfall Junior-Associate oder Trainee arbeitet an erster groesserer Corporate-Transaktion und braucht verstaendnisbasierte Begleitung ohne… |
| `grosskanzlei-corporate-ma-gesellschaftsrecht-register` | Corporate Housekeeping und Register-Prüfung im M&A-Kontext: Anwendungsfall Anwalt prüft für Kaeufer oder Verkaeufer HRB/HRA-Eintrag, Gesellschafterlisten, Satzungen, Beschluesse, Vollmachten und Organstellung der… |
| `grosskanzlei-corporate-ma-handelsregisterabruf` | Handelsregister-Abruf und Registerrecherche für M&A-Transaktionen: Anwendungsfall Anwalt recherchiert offiziellen Registerstand für Zielgesellschaft, Kaeufer-Holding, Komplementaer-GmbH oder Beteiligungsketten. §§ 8-10… |
| `grosskanzlei-corporate-ma-kaltstart` | Kanzlei- und Mandantenpraeferenzen für Corporate/M&A erfassen: Anwendungsfall bei erstem Einsatz des Plugins konfiguriert Anwalt oder Kanzlei Deal-Playbooks, Materiality-Schwellen, Reporting-Standards,… |
| `grosskanzlei-corporate-ma-kg-personengesellschaften` | KG und Personengesellschaften in M&A-Transaktionen: Anwendungsfall Mandat betrifft Kommanditanteilsuebertragung, Fondsvehikel-Struktur, Kommanditistenwechsel oder Einbringung in KG. §§ 161-177 HGB, MoPeG, §§ 20-24… |
| `grosskanzlei-corporate-ma-ki-governance-berufsrecht` | KI-Einsatz im Transaktionsmandat berufsrechtlich absichern: Anwendungsfall Anwalt moechte KI-Tools für Datenraumanalyse oder Vertragsentwurf nutzen und muss Mandatsgeheimnis, Datenschutz und KI-VO-Betreiberpflichten… |
| `grosskanzlei-corporate-ma-kommandocenter` | Deal-Kommandocenter Corporate/M&A: Schnellstart und Workflow-Routing für alle Transaktionsphasen. Anwendungsfall Anwalt gibt Kuerzel, Dokument oder Sachverhaltssatz ein und wird in richtigen Deal-Skill geleitet. SPA… |
| `grosskanzlei-corporate-ma-look-and-feel` | Corporate-Deal-Workspace Darstellung und Ausgabeformat: Anwendungsfall alle sichtbaren Outputs sollen im einheitlichen M&A-Kanzleistil erscheinen — ruhig, edel, deal-informationsdicht ohne Marketing-Ton.… |
| `grosskanzlei-corporate-ma-matter-file` | Deal-Akte und Matter-Workspace anlegen: Anwendungsfall bei Mandatsannahme wird strukturierter Matter-Workspace benoetigt mit allen Workstreams, Datenraumspiegel, Register-Links, Q&A-Tracker und Closing-Archiv. § 43a… |
| `grosskanzlei-corporate-ma-output-versand-signing` | Transaktionsoutput, Signing-Pack und Versand vorbereiten: Anwendungsfall Closing oder Signing naht und Anwalt muss Markups, Board Papers, Signing Packs, Closing Deliverables und beA/Notar/Email-Versand koordinieren. §§… |
| `grosskanzlei-corporate-ma-outside-in-target-screening` | Zielobjekt-Screening und Pipeline-Analyse aus öffentlichen Quellen: Anwendungsfall Mandant oder Deal-Team sucht geeignete Akquisitionsziele und muss fruehe Analyse aus Registern, Finanzdaten, Nachrichten und… |
| `grosskanzlei-corporate-ma-post-closing-integration` | Post-Merger-Integration planen und begleiten: Anwendungsfall nach Closing muessen DD-Findings, SPA-Pflichten und Earn-Out-Mechanismen in PMI-Plan uebersetzt und Betriebsuebergang sowie Registeranmeldungen abgewickelt… |
| `grosskanzlei-corporate-ma-public-ma-kapitalmarkt-mar` | Public M&A und Kapitalmarkt-Compliance bei boersennotierten Transaktionen: Anwendungsfall Anwalt begleitet Übernahmeangebot, Pflichtangebot oder Squeeze-Out § 327a AktG bei boersennotierter Zielgesellschaft. WpUEG… |
| `grosskanzlei-corporate-ma-qa-information-requests` | Q&A-Prozess und Information Requests in der Due Diligence steuern: Anwendungsfall Deal-Team muss aus DD-Analyse gezielte Fragen an Verkaeufer formulieren, priorisieren und Antworten gegen Datenraum-Belege prüfen. SPA… |
| `grosskanzlei-corporate-ma-rechtsprechungsrecherche` | Corporate und M\&A Rechtsprechungsrecherche: Anwendungsfall Anwalt braucht für Gutachten, Schriftsatz oder DD-Report relevante BGH-Rechtsprechung zu Organpflichten, Kapitalmarkt, Umwandlung oder Insolvenz. §§ 93 und… |
| `grosskanzlei-corporate-ma-regulatory-fdi-merger-control` | Fusionskontrolle und FDI-Investitionsprüfung für M&A-Transaktionen: Anwendungsfall Signing naht und Deal-Team prüft ob Kartellrechts-Freigabe oder AWV-Prüfung benoetigt wird. §§ 35-44 GWB inlaendische Fusionskontrolle,… |
| `grosskanzlei-corporate-ma-restructuring-starug-insolvenzplan` | StaRUG-Restrukturierung und Insolvenzplanverfahren begleiten: Anwendungsfall Unternehmen mit drohender Zahlungsunfähigkeit prüft Restrukturierungsoptionen einschließlich StaRUG-Plan, praeventiyen… |
| `grosskanzlei-corporate-ma-signing-closing-conditions` | Signing-to-Closing-Prozess mit Conditions Precedent für M&A-Transaktionen: Anwendungsfall nach Signing muessen alle Closing-Bedingungen erfuellt und Closing Deliverables koordiniert werden. SPA Closing Conditions, §… |
| `grosskanzlei-corporate-ma-simulation-bidder-process` | M&A-Bieterprozess simulieren für Training und Mandatsvorbereitung: Anwendungsfall Junior-Anwalt oder Deal-Team ueben beschleunigten Transaktions-Tag mit Datenraum Q&A SPA-Markup CP-Liste und Board-Call. SPA Share… |
| `grosskanzlei-corporate-ma-spa-apa-entwurf` | SPA Share Purchase Agreement und APA Asset Purchase Agreement entwerfen: Anwendungsfall Anwalt erstellt Kaufvertrag für Share Deal oder Asset Deal aus Term Sheet DD-Findings und Transaktionsstruktur. §§ 433 ff. BGB… |
| `grosskanzlei-corporate-ma-steps-plan-pmo` | Deal-PMO und Steps-Plan für Pre-Signing bis Post-Closing: Anwendungsfall Transaktion braucht praezisen Aufgaben- und Zeitplan aus Vertraegen, DD-Unterlagen und Gremienunterlagen extrahiert. SPA Closing Conditions, CPs… |
| `grosskanzlei-corporate-ma-tabellenreview-3d-datenraum` | 3D-Tabellenreview M&A-Datenraum: Dokumente Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft verbinden: Anwendungsfall Deal-Team prüft Datenraum-Dokumente systematisch mit internem Review-Cube nach mehreren… |
| `grosskanzlei-corporate-ma-teaser-im-processdocs` | Investment Teaser Information Memorandum und Prozessdokumente erstellen: Anwendungsfall Sell-side-Mandat braucht Teaser für erste Bieterkontakte, Information Memorandum und Process Letter für strukturierten… |
| `grosskanzlei-corporate-ma-transaktionsstruktur` | Transaktionsstruktur für M&A entwickeln und Varianten bewerten: Anwendungsfall Mandant fragt welche Transaktionsstruktur für seinen Unternehmenskauf -verkauf oder Carve-out am besten passt. Share Deal Asset Deal… |
| `grosskanzlei-corporate-ma-translations-multijurisdictional` | Multi-Jurisdiction-Koordination und Übersetzungen in grenzüberschreitenden M&A-Transaktionen: Anwendungsfall Transaktion mit mehreren Laendern erfordert Koordination lokaler Counsel, Übersetzungen und Rechtsvergleich.… |
| `grosskanzlei-corporate-ma-umwandlungsrecht` | Umwandlungsrecht Verschmelzung Spaltung Formwechsel und Carve-outs nach UmwG bearbeiten: Anwendungsfall Mandant plant Verschmelzung zweier GmbHs Ausgliederung eines Geschäftsbereichs oder Formwechsel AG zu GmbH im… |
| `grosskanzlei-corporate-ma-umwandlungssteuerrecht` | Umwandlungssteuerrecht Buchwertantrag steuerliche Rückwirkung und Verlustuntergang prüfen: Anwendungsfall Corporate-Team und Steuerteam muessen umwandlungssteuerliche Strukturentscheidung abstimmen. §§ 20-24 UmwStG… |
| `grosskanzlei-corporate-ma-vertragsmarkup-key-issues` | SPA/APA/NDA Markup analysieren und Key Issues List erstellen: Anwendungsfall Anwalt erhaelt Gegenentwurf oder Markup und muss wirtschaftlich relevante Abweichungen strukturieren und Gegenvorschlaege formulieren. §§ 433… |
| `grosskanzlei-corporate-ma-wi-insurance` | W&I-Versicherung Warranty and Indemnity in M&A-Transaktionen: Anwendungsfall Kaeufer oder Verkaeufer erwägt W&I-Versicherung für SPA-Garantien und muss Underwriting-Prozess, DD-Berichts-Anforderungen und… |
| `grosskanzlei-ma-aktenanlage` | Freistehende M&A-Aktenanlage ohne externes Plugin: Anwendungsfall neue Corporate-Transaktion wird aufgenommen und Deal-Akte mit Aktenzeichen Parteienregister Ordnerstruktur Datenraumspiegel und… |
| `grosskanzlei-ma-erechnung-gobd` | Freistehender Billing- GoBD- und E-Rechnungsworkflow für M&A-Mandate: Anwendungsfall Kanzlei muss für M&A-Mandat GoBD-konforme Rechnung XRechnung-XML und ZUGFeRD-Prüfpaket erstellen. § 3a RVG Stundenhonorar, GoBD… |
| `grosskanzlei-ma-fristen-cp-kalender` | Freistehender Deal-Fristen- und CP-Kalender für M&A-Mandate: Anwendungsfall Fristen aus Signing Closing Q&A Regulatory Register Board und Restrukturierung muessen in einem Kalender zusammengeführt werden. SPA Closing… |
| `grosskanzlei-ma-insolvenzreife` | Freistehender Insolvenzreife- und StaRUG-Schwellencheck für M&A: Anwendungsfall im Kaufprozess oder Beratungsmandat muss geprüft werden ob Zielunternehmen oder Mandant nahe an Insolvenzantragspflicht ist. §§ 17-19 InsO… |
| `grosskanzlei-ma-liquiditaetsvorschau` | Freistehende Liquiditaetsvorschau für Corporate M&A und Distressed M&A: Anwendungsfall Kaeufer Verkaeufer oder Vorstand braucht kurzfristige Zahlungsfähigkeits-Übersicht 3-Wochen bis 13-Wochen-Horizont. § 17 InsO… |
| `grosskanzlei-ma-schreibcanvas` | Freistehender Corporate-Schreibcanvas für SPA Board Paper und DD-Report: Anwendungsfall Anwalt entwirft SPA-Klausel Markup-Antwort DD-Report oder Mandatsvereinbarung und braucht substanzorientierten Schreibbegleiter… |
| `grosskanzlei-ma-tabellenreview` | Freistehender Tabellenreview für Corporate M&A-Dokumente Datenpunkte und Perspektiven: Anwendungsfall Tabellen Formeln Excel-Modelle oder Dokumentenmatrizen in Transaktionen muessen auf Formelbrueche widersprüchliche… |
| `ki-einsatz-bei-gutachten-mandatsseite` | Großkanzlei-Mandatsseite bei KI-Verdacht gegenüber gerichtlichen oder vorgerichtlichen Sachverständigengutachten in Corporate-, M&A- und Schiedsverfahren. Strategische Prüfung der höchstpersönlichen Erstellungspflicht… |

## Worum geht es?

Das Plugin ist ein vollstaendiges Big-Law-Corporate/M&A-Arbeitssystem fuer Partner, Associates und Kanzleipersonal. Es deckt den gesamten Transaktionslebenszyklus ab: vom Deal-Intake und der Mandatskonflikts-Pruefung ueber Datenraum-Aufbau und Legal Due Diligence bis hin zu SPA/APA-Entwurf, Signing, Closing und Post-Merger-Integration. Hinzu kommen spezialisierte Teilmodule fuer Public M&A, Umwandlungsrecht, StaRUG-Restrukturierung, Distressed M&A und W&I-Versicherung.

Das Plugin integriert auch Querschnittsthemen der Kanzleipraxis: Billing Narratives, GoBD-konforme E-Rechnung, KI-Governance im Transaktionsmandat und einen freundlichen Copilot-Modus fuer Junior-Associates. Zielgruppe sind Corporate/M&A-Kanzleien aller Groessen sowie Inhouse-M&A-Teams.

## Wann brauchen Sie diesen Skill?

- Kanzlei nimmt neues M&A-Mandat an und muss Deal-Akte anlegen, Interessenkonflikte pruefen und Staffing planen.
- Anwalt begleitet Sell-side- oder Buy-side-Transaktion und muss Due-Diligence-Prozess strukturieren und berichten.
- SPA oder APA soll entworfen oder ein Gegenentwurf markiert und kommentiert werden.
- Transaktion naehert sich Closing; CP-Kalender, Signing-Pack und Closing-Bible muessen vorbereitet werden.
- Kanzlei muss fuer M&A-Mandat GoBD-konforme E-Rechnung erstellen oder Liquiditaetsvorschau fuer krisennahen Mandanten erbringen.

## Fachbegriffe (kurz erklaert)

- **SPA/APA** — Share Purchase Agreement (Anteilskaufvertrag) / Asset Purchase Agreement (Vermoegensuebertragungsvertrag); zentrale Transaktionsdokumente.
- **Due Diligence (DD)** — Sorgfaeltige Pruefung aller rechtlichen, wirtschaftlichen und steuerlichen Risiken des Zielobjekts vor der Transaktion.
- **W&I-Versicherung** — Warranty and Indemnity Insurance; versichert Gewaehrleistungs- und Freistellungsansprueche aus SPA.
- **Conditions Precedent (CP)** — Vertragliche Bedingungen, die zwischen Signing und Closing erfuellt werden muessen.
- **Closing Bible** — Vollstaendiges Archiv aller Transaktionsdokumente nach Closing; Nachweis der gesamten Transaktion.
- **StaRUG** — Unternehmensstabilisierungs- und -restrukturierungsgesetz; ermoeglicht ausserinsolvenzliche Restrukturierung fuer Unternehmen mit drohender Zahlungsunfaehigkeit.
- **PMI** — Post-Merger-Integration; Umsetzung der DD-Findings und SPA-Pflichten nach Closing.
- **GoBD** — Grundsaetze ordnungsmaessiger Datenfuehrung; relevanter Rahmen fuer elektronische Buchfuehrung und E-Rechnung.
- **FDI-Pruefung** — Foreign Direct Investment; Investitionspruefung bei Erwerb strategisch bedeutsamer Unternehmen durch Auslaender (AWG, AWVO).
- **Fusionskontrolle** — Merger Control; Anmeldung und Freigabe durch Kartellbehoerden (EU-Kommission, Bundeskartellamt) vor Vollzug.

## Rechtsgrundlagen

- §§ 433 ff. BGB — Kaufvertragsrecht (SPA)
- §§ 311b 925 BGB — Formpflicht bei Grundstuecks- und Anteilsuebertragung
- GmbHG, AktG, UmwG — Gesellschaftsrecht, Umwandlung
- WpUeG — Wertpapiererwerbs- und Uebernahmegesetz (Public M&A)
- MAR (EU-Marktmissbrauchsverordnung) — Kapitalmarktrecht bei boersennotierten Zielunternehmen
- StaRUG — Restrukturierungsgesetz
- InsO — Insolvenzrecht (Distressed M&A)
- AWG / AWVO — Investitionspruefung fuer FDI
- §§ 35 ff. GWB, Art. 1 ff. FKVO — Fusionskontrolle (national und EU)
- GoBD-Schreiben des BMF — Elektronische Buchfuehrung

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Deal-Intake: Transaktionstyp, Parteien und Timeline erfassen; Interessenkonflikt und GwG-Pruefung starten.
2. Aktenanlage und Staffing: Matter-Workspace anlegen, Deal-Team besetzen und Look-and-Feel festlegen.
3. Transaktionsstruktur festlegen: Share Deal oder Asset Deal; Umwandlungsrecht; steuerliche Rueckwirkung.
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. CP-Kalender fuehren und Closing Bible nach Abschluss archivieren.

## Skill-Tour (was gibt es hier?)

**Deal-Setup und Mandatsfuehrung**
- `grosskanzlei-corporate-ma-kommandocenter` — Deal-Kommandocenter: Schnellstart und Workflow-Routing fuer alle Transaktionsphasen.
- `grosskanzlei-corporate-ma-kaltstart` — Kanzlei- und Mandantenpraeferenzen erfassen; erstes Plugin-Setup konfigurieren.
- `grosskanzlei-corporate-ma-deal-intake` — Neues M&A-Mandat aufnehmen und strukturieren; Erstanfrage bearbeiten.
- `grosskanzlei-ma-aktenanlage` — M&A-Aktenanlage und Deal-Workspace anlegen.
- `grosskanzlei-corporate-ma-matter-file` — Deal-Akte und Matter-Workspace strukturieren.
- `grosskanzlei-corporate-ma-deal-team-staffing` — Deal-Team besetzen und Staffing-Plan erstellen.
- `grosskanzlei-corporate-ma-look-and-feel` — Einheitliches Ausgabeformat fuer alle Deal-Outputs konfigurieren.
- `grosskanzlei-corporate-ma-conflict-gwg-sanctions` — Interessenkonflikte, GwG-Pruefung und Sanktions-Screening bei Mandatsannahme.

**Target-Screening und Due Diligence**
- `grosskanzlei-corporate-ma-outside-in-target-screening` — Zielobjekt-Screening aus oeffentlichen Quellen; Pipeline-Analyse.
- `grosskanzlei-corporate-ma-datenraum-aufbau` — Due-Diligence-Datenraum strukturieren und besetzen.
- `grosskanzlei-corporate-ma-datenraum-gap-clean-room` — Datenraum-Lueckenanalyse und Clean-Room-Protokoll.
- `grosskanzlei-corporate-ma-due-diligence-legal` — Legal Due Diligence: Corporate, Rechtsstreitigkeiten, Regulierung.
- `grosskanzlei-corporate-ma-due-diligence-commercial-contracts` — Commercial Contracts DD: Kundenvertraege, Lieferantenvertraege.
- `grosskanzlei-corporate-ma-due-diligence-reporting` — DD-Report erstellen und strukturieren.
- `grosskanzlei-corporate-ma-qa-information-requests` — Q&A-Prozess und Information Requests steuern.
- `grosskanzlei-corporate-ma-tabellenreview-3d-datenraum` — 3D-Tabellenreview: Dokumente, Datenpunkte und Recht/Steuer/Wirtschaft-Perspektiven verbinden.
- `grosskanzlei-ma-tabellenreview` — Freistehender Tabellenreview fuer Corporate-M&A-Dokumente.
- `grosskanzlei-corporate-ma-expert-calls-transkripte` — Expert Calls und Transkript-Auswertung fuer DD.
- `grosskanzlei-corporate-ma-datenqualitaet-xai-qualitaetskontrolle` — KI-Qualitaetskontrolle und Halluzinations-Absicherung in DD-Berichten.

**Transaktionsstruktur und Vertraege**
- `grosskanzlei-corporate-ma-transaktionsstruktur` — Transaktionsstruktur entwickeln und Varianten bewerten.
- `grosskanzlei-corporate-ma-spa-apa-entwurf` — SPA und APA entwerfen: Kaufvertrag fuer Share Deal oder Asset Deal.
- `grosskanzlei-corporate-ma-vertragsmarkup-key-issues` — SPA/APA/NDA Markup analysieren und Key Issues List erstellen.
- `grosskanzlei-corporate-ma-disclosure-schedules` — Disclosure Schedules und Guarantees-Abgleich erstellen.
- `grosskanzlei-corporate-ma-fair-disclosure-knowledge` — Fair Disclosure und Wissenszurechnung in M&A-Vertraegen klaeren.
- `grosskanzlei-corporate-ma-wi-insurance` — W&I-Versicherung strukturieren; Buy-side oder Sell-side Policy.
- `grosskanzlei-ma-schreibcanvas` — Freistehender Schreibcanvas fuer SPA-Klausel, Board Paper und DD-Report.

**Signing, Closing und PMI**
- `grosskanzlei-corporate-ma-signing-closing-conditions` — Signing-to-Closing mit Conditions Precedent managen.
- `grosskanzlei-ma-fristen-cp-kalender` — Deal-Fristen- und CP-Kalender fuehren.
- `grosskanzlei-corporate-ma-output-versand-signing` — Signing-Pack und Versand vorbereiten; Markup-Finalisierung.
- `grosskanzlei-corporate-ma-closing-bible-archiv` — Closing Bible erstellen und Deal-Archiv pflegen.
- `grosskanzlei-corporate-ma-steps-plan-pmo` — Deal-PMO und Steps-Plan von Pre-Signing bis Post-Closing.
- `grosskanzlei-corporate-ma-post-closing-integration` — PMI planen; DD-Findings und Earn-Out-Pflichten umsetzen.

**Spezialthemen**
- `grosskanzlei-corporate-ma-public-ma-kapitalmarkt-mar` — Public M&A; Uebernahmeangebotsregulierung; Kapitalmarkt-Compliance und MAR.
- `grosskanzlei-corporate-ma-regulatory-fdi-merger-control` — Fusionskontrolle und FDI-Investitionspruefung.
- `grosskanzlei-corporate-ma-umwandlungsrecht` — Umwandlung: Verschmelzung, Spaltung, Formwechsel, Carve-out nach UmwG.
- `grosskanzlei-corporate-ma-umwandlungssteuerrecht` — Umwandlungssteuerrecht: Buchwertantrag, steuerliche Rueckwirkung, Verlustuntergang.
- `grosskanzlei-corporate-ma-kg-personengesellschaften` — KG und Personengesellschaften in M&A-Transaktionen.
- `grosskanzlei-corporate-ma-distressed-ma` — Distressed M&A: Unternehmenskauf in Krise oder Insolvenz.
- `grosskanzlei-corporate-ma-restructuring-starug-insolvenzplan` — StaRUG-Restrukturierung und Insolvenzplanverfahren begleiten.
- `grosskanzlei-ma-insolvenzreife` — Insolvenzreife- und StaRUG-Schwellencheck.
- `grosskanzlei-ma-liquiditaetsvorschau` — Liquiditaetsvorschau fuer Corporate M&A und Distressed.
- `grosskanzlei-corporate-ma-gesellschaftsrecht-register` — Corporate Housekeeping und Register-Pruefung.
- `grosskanzlei-corporate-ma-handelsregisterabruf` — Handelsregister-Abruf und Registerrecherche.

**Prozess und Kommunikation**
- `grosskanzlei-corporate-ma-teaser-im-processdocs` — Investment Teaser, Information Memorandum und Prozessdokumente erstellen.
- `grosskanzlei-corporate-ma-simulation-bidder-process` — Bieterprozess simulieren fuer Training und Mandatsvorbereitung.
- `grosskanzlei-corporate-ma-translations-multijurisdictional` — Multi-Jurisdiction-Koordination und Uebersetzungen.
- `grosskanzlei-corporate-ma-rechtsprechungsrecherche` — Rechtsprechungsrecherche fuer Gutachten, Schriftsatz oder DD-Report.
- `grosskanzlei-corporate-ma-board-paper-business-judgment` — Board Paper und Business Judgment Rule Pruefung.
- `grosskanzlei-corporate-ma-automation-monitoring` — Monitoring und Automatisierungen fuer laufende M&A-Mandate einrichten.

**Kanzlei-Querschnitt**
- `grosskanzlei-corporate-ma-billing-narratives` — Billing Narratives und Abrechnung fuer M&A-Mandate erstellen.
- `grosskanzlei-ma-erechnung-gobd` — GoBD-konformer Billing- und E-Rechnungsworkflow.
- `grosskanzlei-corporate-ma-ki-governance-berufsrecht` — KI-Einsatz im Transaktionsmandat berufsrechtlich absichern.
- `grosskanzlei-corporate-ma-freundlicher-copilot` — Freundlicher Copilot-Modus fuer Junior-Associates und Trainees.
- `ki-einsatz-bei-gutachten-mandatsseite` — Grosskanzlei-Mandatsseite bei KI-Verdacht gegenueber Sachverstaendigengutachten.

## Worauf besonders achten

- Signing ohne erfuellte CPs schafft schwebende Unwirksamkeit; CP-Checkliste muss lueckenlos sein.
- W&I-Versicherungsschlupfloecher: Policy deckt typischerweise keine Steuern, keine Pensionsverpflichtungen und keine bekannten Risiken ab; DD-Ergebnis und Policy-Schutzbereich muessen abgeglichen werden.
- FDI-Pruefung und Fusionskontrolle laufen parallel; unterschiedliche Fristen bei EU-Kommission, Bundeskartellamt und BMWK erfordern sorgfaeltige Koordination.
- GoBD-konforme E-Rechnung ist seit 2025 fuer B2B-Transaktionen Pflicht (gestaffelt); Kanzlei muss eigene Rechnungen anpassen.
- KI-generierte DD-Berichte und Schriftsaetze muessen vor Versand auf Halluzinationen und Quellenangaben geprueft werden (§ 43a BRAO Sorgfaltspflicht).

## Typische Fehler

- Datenraum-Indexierung vergessen: Ohne klare Nummerierung und Kategorien koennen Datenpunkte in DD-Berichten nicht zugeordnet werden.
- Knowledge-Qualifier zu grosszuegig: Breite Wissensdefinition im SPA erhoht Haeftungsrisiko des Verkaeufers erheblich.
- Anteilsvinkulierung uebersehen: Bei GmbH-Anteilen kann Satzung Zustimmungserfordernis der Gesellschaft vorsehen; fehlende Zustimmung macht Abtretung unwirksam.
- Umwandlungssteuerliche Rueckwirkung versaeumt: Stichtag fuer steuerliche Rueckwirkung bei Verschmelzung ist maximal acht Monate vor Anmeldung; spaetere Einreichung schliesst Rueckwirkung aus.
- PMI-Planung vernachlaessigt: Earn-Out-Mechanismen, Carve-out-Restaufgaben und Mitarbeitertransfer werden nach Closing haeufig nicht geplant und fuehren zu SPA-Streitigkeiten.

## Querverweise

- Plugin `liquiditaetsplanung` — Bei Distressed-Transaktionen oder krisennahen Zielunternehmen Liquiditaetsvorschau parallel erstellen.
- Plugin `aussenwirtschaft-zoll-sanktionen` — Exportkontroll-DD und Sanktions-Screening bei Transaktionen mit internationalem Bezug.
- Plugin `umweltrecht` — Umwelt-DD und Altlasten bei Transaktionen mit Produktions- oder Industriestandorten.
- Plugin `patentrecherche` — IP-DD: Patentportfolio und FTO-Analyse bei technologiegetriebenen Targets.
- Plugin `wandeldarlehen-lebenszyklus` — Brueckenfinanzierung per Wandeldarlehen vor M&A-Exit oder Kapitalrunde.

## Quellen und Aktualitaet

- Stand: 05/2026
- BGB, GmbHG, AktG, UmwG, UmwStG, WpUeG, StaRUG, InsO, GWB, FKVO, AWG in aktuell geltender Fassung
- GoBD-Schreiben BMF (Stand 2019; aktuell keine Neufassung)
