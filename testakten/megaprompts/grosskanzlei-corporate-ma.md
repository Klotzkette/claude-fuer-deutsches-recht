# Megaprompt: grosskanzlei-corporate-ma

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 272 Skills (gekuerzt fuer Chat-Fenster) des Plugins `grosskanzlei-corporate-ma`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Großkanzlei-Corporate/M&A-Plugin. Fragt Rolle, Erfahrungslevel, Ziel, Fristen…
2. **automation** — Monitoring und Automatisierungen für laufende M&A-Mandate einrichten: Anwendungsfall Deal-Team benoetigt automatisierte …
3. **billing-narratives** — Big-Law Billing Narratives und Abrechnung für M&A-Mandate erstellen: Anwendungsfall Associate oder Partnerassistenz muss…
4. **closing-bible** — Closing Bible und Deal-Archiv erstellen: Anwendungsfall Mandant oder Counsel braucht nach Signing/Closing vollständige D…
5. **corporate-rechtsprechungsrecherche** — Corporate und M&A Rechtsprechungsrecherche: Anwendungsfall Anwalt braucht für Gutachten, Schriftsatz oder DD-Report rele…
6. **datenqualitaet-xai** — KI-Qualitaetskontrolle und Halluzinations-Absicherung in M&A-Transaktionen: Anwendungsfall KI-generierte DD-Berichte, Kl…
7. **datenraum-aufbau** — Due Diligence Datenraum strukturieren und bestücken: Anwendungsfall Mandant bereitet Verkaufsprozess vor oder Buyer-Team…
8. **datenraum-gap-clean** — Datenraum-Lueckenanalyse und Clean-Room-Protokoll für M&A Due Diligence: Anwendungsfall Anwalt oder Mandant stellt fest …

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Großkanzlei-Corporate/M&A-Plugin. Fragt Rolle, Erfahrungslevel, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Anfänger- oder First-Year-Associate-Beda..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Grosskanzlei Corporate Ma** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grosskanzlei Corporate/M&A — Allgemein` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Großkanzlei Corporate/M&A**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Big-Law-Corporate/M&A-Plugin: Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, Umwandlung, StaRUG/Insolvenzplan, CP-Kalender, E-Rechnung/GoBD, PMI.

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

### 5. Fachmodule in diesem Plugin

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
| `grosskanzlei-corporate-ma-kommandocenter` | Deal-Kommandocenter Corporate/M&A: Schnellstart und Fallrouting für alle Transaktionsphasen. Anwendungsfall Anwalt gibt Kuerzel, Dokument oder Sachverhaltssatz ein und wird in richtigen Deal-Skill geleitet. SPA… |
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
| `grosskanzlei-corporate-ma-translations-multijurisdictional` | Multi-Jurisdiction-Koordination und Übersetzungen in grenzüberschreitenden M&A-Transaktionen: Anwendungsfall Transaktion mit mehreren Ländern erfordert Koordination lokaler Counsel, Übersetzungen und Rechtsvergleich.… |
| `grosskanzlei-corporate-ma-umwandlungsrecht` | Umwandlungsrecht Verschmelzung Spaltung Formwechsel und Carve-outs nach UmwG bearbeiten: Anwendungsfall Mandant plant Verschmelzung zweier GmbHs Ausgliederung eines Geschäftsbereichs oder Formwechsel AG zu GmbH im… |
| `grosskanzlei-corporate-ma-umwandlungssteuerrecht` | Umwandlungssteuerrecht Buchwertantrag steuerliche Rückwirkung und Verlustuntergang prüfen: Anwendungsfall Corporate-Team und Steuerteam muessen umwandlungssteuerliche Strukturentscheidung abstimmen. §§ 20-24 UmwStG… |
| `grosskanzlei-corporate-ma-vertragsmarkup-key-issues` | SPA/APA/NDA Markup analysieren und Key Issues List erstellen: Anwendungsfall Anwalt erhaelt Gegenentwurf oder Markup und muss wirtschaftlich relevante Abweichungen strukturieren und Gegenvorschlaege formulieren. §§ 433… |
| `grosskanzlei-corporate-ma-wi-insurance` | W&I-Versicherung Warranty and Indemnity in M&A-Transaktionen: Anwendungsfall Kaeufer oder Verkaeufer erwägt W&I-Versicherung für SPA-Garantien und muss Underwriting-Prozess, DD-Berichts-Anforderungen und… |
| `grosskanzlei-ma-aktenanlage` | Freistehende M&A-Aktenanlage ohne externes Plugin: Anwendungsfall neue Corporate-Transaktion wird aufgenommen und Deal-Akte mit Aktenzeichen Parteienregister Ordnerstruktur Datenraumspiegel und… |
| `grosskanzlei-ma-erechnung-gobd` | Freistehender Billing- GoBD- und E-Rechnungsfür M&A-Mandate: Anwendungsfall Kanzlei muss für M&A-Mandat GoBD-konforme Rechnung XRechnung-XML und ZUGFeRD-Prüfpaket erstellen. § 3a RVG Stundenhonorar, GoBD… |
| `grosskanzlei-ma-fristen-cp-kalender` | Freistehender Deal-Fristen- und CP-Kalender für M&A-Mandate: Anwendungsfall Fristen aus Signing Closing Q&A Regulatory Register Board und Restrukturierung muessen in einem Kalender zusammengeführt werden. SPA Closing… |
| `grosskanzlei-ma-insolvenzreife` | Freistehender Insolvenzreife- und StaRUG-Schwellencheck für M&A: Anwendungsfall im Kaufprozess oder Beratungsmandat muss geprüft werden ob Zielunternehmen oder Mandant nahe an Insolvenzantragspflicht ist. §§ 17-19 InsO… |
| `grosskanzlei-ma-liquiditaetsvorschau` | Freistehende Liquiditaetsvorschau für Corporate M&A und Distressed M&A: Anwendungsfall Kaeufer Verkaeufer oder Vorstand braucht kurzfristige Zahlungsfähigkeits-Übersicht 3-Wochen bis 13-Wochen-Horizont. § 17 InsO… |
| `grosskanzlei-ma-schreibcanvas` | Freistehender Corporate-Schreibcanvas für SPA Board Paper und DD-Report: Anwendungsfall Anwalt entwirft SPA-Klausel Markup-Antwort DD-Report oder Mandatsvereinbarung und braucht substanzorientierten Schreibbegleiter… |
| `grosskanzlei-ma-tabellenreview` | Freistehender Tabellenreview für Corporate M&A-Dokumente Datenpunkte und Perspektiven: Anwendungsfall Tabellen Formeln Excel-Modelle oder Dokumentenmatrizen in Transaktionen muessen auf Formelbrueche widersprüchliche… |
| `ki-einsatz-bei-gutachten-mandatsseite` | Großkanzlei-Mandatsseite bei KI-Verdacht gegenüber gerichtlichen oder vorgerichtlichen Sachverständigengutachten in Corporate-, M&A- und Schiedsverfahren. Strategische Prüfung der höchstpersönlichen Erstellungspflicht… |

## Worum geht es?

Das Plugin ist ein vollstaendiges Big-Law-Corporate/M&A-Arbeitssystem für Partner, Associates und Kanzleipersonal. Es deckt den gesamten Transaktionslebenszyklus ab: vom Deal-Intake und der Mandatskonflikts-Pruefung ueber Datenraum-Aufbau und Legal Due Diligence bis hin zu SPA/APA-Entwurf, Signing, Closing und Post-Merger-Integration. Hinzu kommen spezialisierte Teilmodule für Public M&A, Umwandlungsrecht, StaRUG-Restrukturierung, Distressed M&A und W&I-Versicherung.

Das Plugin integriert auch Querschnittsthemen der Kanzleipraxis: Billing Narratives, GoBD-konforme E-Rechnung, KI-Governance im Transaktionsmandat und einen freundlichen Copilot-Modus für Junior-Associates. Zielgruppe sind Corporate/M&A-Kanzleien aller Groessen sowie Inhouse-M&A-Teams.

## Wann dieses Modul hilft?

- Kanzlei nimmt neues M&A-Mandat an und muss Deal-Akte anlegen, Interessenkonflikte pruefen und Staffing planen.
- Anwalt begleitet Sell-side- oder Buy-side-Transaktion und muss Due-Diligence-Prozess strukturieren und berichten.
- SPA oder APA soll entworfen oder ein Gegenentwurf markiert und kommentiert werden.
- Transaktion naehert sich Closing; CP-Kalender, Signing-Pack und Closing-Bible muessen vorbereitet werden.
- Kanzlei muss für M&A-Mandat GoBD-konforme E-Rechnung erstellen oder Liquiditaetsvorschau für krisennahen Mandanten erbringen.

## Fachbegriffe (kurz erklaert)

- **SPA/APA** — Share Purchase Agreement (Anteilskaufvertrag) / Asset Purchase Agreement (Vermoegensuebertragungsvertrag); zentrale Transaktionsdokumente.
- **Due Diligence (DD)** — Sorgfaeltige Pruefung aller rechtlichen, wirtschaftlichen und steuerlichen Risiken des Zielobjekts vor der Transaktion.
- **W&I-Versicherung** — Warranty and Indemnity Insurance; versichert Gewaehrleistungs- und Freistellungsansprueche aus SPA.
- **Conditions Precedent (CP)** — Vertragliche Bedingungen, die zwischen Signing und Closing erfuellt werden muessen.
- **Closing Bible** — Vollstaendiges Archiv aller Transaktionsdokumente nach Closing; Nachweis der gesamten Transaktion.
- **StaRUG** — Unternehmensstabilisierungs- und -restrukturierungsgesetz; ermoeglicht ausserinsolvenzliche Restrukturierung für Unternehmen mit drohender Zahlungsunfaehigkeit.
- **PMI** — Post-Merger-Integration; Umsetzung der DD-Findings und SPA-Pflichten nach Closing.
- **GoBD** — Grundsaetze ordnungsmäßiger Datenfuehrung; relevanter Rahmen für elektronische Buchfuehrung und E-Rechnung.
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
- AWG / AWVO — Investitionspruefung für FDI
- §§ 35 ff. GWB, Art. 1 ff. FKVO — Fusionskontrolle (national und EU)
- GoBD-Schreiben des BMF — Elektronische Buchfuehrung

## Schritt-für-Schritt: Einstieg ins Plugin

1. Deal-Intake: Transaktionstyp, Parteien und Timeline erfassen; Interessenkonflikt und GwG-Pruefung starten.
2. Aktenanlage und Staffing: Matter-Workspace anlegen, Deal-Team besetzen und Look-and-Feel festlegen.
3. Transaktionsstruktur festlegen: Share Deal oder Asset Deal; Umwandlungsrecht; steuerliche Rueckwirkung.
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. CP-Kalender fuehren und Closing Bible nach Abschluss archivieren.

## Skill-Tour (was gibt es hier?)

**Deal-Setup und Mandatsfuehrung**
- `grosskanzlei-corporate-ma-kommandocenter` — Deal-Kommandocenter: Schnellstart und Fallrouting für alle Transaktionsphasen.
- `grosskanzlei-corporate-ma-kaltstart` — Kanzlei- und Mandantenpraeferenzen erfassen; erstes Plugin-Setup konfigurieren.
- `grosskanzlei-corporate-ma-deal-intake` — Neues M&A-Mandat aufnehmen und strukturieren; Erstanfrage bearbeiten.
- `grosskanzlei-ma-aktenanlage` — M&A-Aktenanlage und Deal-Workspace anlegen.
- `grosskanzlei-corporate-ma-matter-file` — Deal-Akte und Matter-Workspace strukturieren.
- `grosskanzlei-corporate-ma-deal-team-staffing` — Deal-Team besetzen und Staffing-Plan erstellen.
- `grosskanzlei-corporate-ma-look-and-feel` — Einheitliches Ausgabeformat für alle Deal-Outputs konfigurieren.
- `grosskanzlei-corporate-ma-conflict-gwg-sanctions` — Interessenkonflikte, GwG-Pruefung und Sanktions-Screening bei Mandatsannahme.

**Target-Screening und Due Diligence**
- `grosskanzlei-corporate-ma-outside-in-target-screening` — Zielobjekt-Screening aus öffentlichen Quellen; Pipeline-Analyse.
- `grosskanzlei-corporate-ma-datenraum-aufbau` — Due-Diligence-Datenraum strukturieren und besetzen.
- `grosskanzlei-corporate-ma-datenraum-gap-clean-room` — Datenraum-Lueckenanalyse und Clean-Room-Protokoll.
- `grosskanzlei-corporate-ma-due-diligence-legal` — Legal Due Diligence: Corporate, Rechtsstreitigkeiten, Regulierung.
- `grosskanzlei-corporate-ma-due-diligence-commercial-contracts` — Commercial Contracts DD: Kundenvertraege, Lieferantenvertraege.
- `grosskanzlei-corporate-ma-due-diligence-reporting` — DD-Report erstellen und strukturieren.
- `grosskanzlei-corporate-ma-qa-information-requests` — Q&A-Prozess und Information Requests steuern.
- `grosskanzlei-corporate-ma-tabellenreview-3d-datenraum` — 3D-Tabellenreview: Dokumente, Datenpunkte und Recht/Steuer/Wirtschaft-Perspektiven verbinden.
- `grosskanzlei-ma-tabellenreview` — Freistehender Tabellenreview für Corporate-M&A-Dokumente.
- `grosskanzlei-corporate-ma-expert-calls-transkripte` — Expert Calls und Transkript-Auswertung für DD.
- `grosskanzlei-corporate-ma-datenqualitaet-xai-qualitaetskontrolle` — KI-Qualitaetskontrolle und Halluzinations-Absicherung in DD-Berichten.

**Transaktionsstruktur und Vertraege**
- `grosskanzlei-corporate-ma-transaktionsstruktur` — Transaktionsstruktur entwickeln und Varianten bewerten.
- `grosskanzlei-corporate-ma-spa-apa-entwurf` — SPA und APA entwerfen: Kaufvertrag für Share Deal oder Asset Deal.
- `grosskanzlei-corporate-ma-vertragsmarkup-key-issues` — SPA/APA/NDA Markup analysieren und Key Issues List erstellen.
- `grosskanzlei-corporate-ma-disclosure-schedules` — Disclosure Schedules und Guarantees-Abgleich erstellen.
- `grosskanzlei-corporate-ma-fair-disclosure-knowledge` — Fair Disclosure und Wissenszurechnung in M&A-Vertraegen klaeren.
- `grosskanzlei-corporate-ma-wi-insurance` — W&I-Versicherung strukturieren; Buy-side oder Sell-side Policy.
- `grosskanzlei-ma-schreibcanvas` — Freistehender Schreibcanvas für SPA-Klausel, Board Paper und DD-Report.

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
- `grosskanzlei-ma-liquiditaetsvorschau` — Liquiditaetsvorschau für Corporate M&A und Distressed.
- `grosskanzlei-corporate-ma-gesellschaftsrecht-register` — Corporate Housekeeping und Register-Pruefung.
- `grosskanzlei-corporate-ma-handelsregisterabruf` — Handelsregister-Abruf und Registerrecherche.

**Prozess und Kommunikation**
- `grosskanzlei-corporate-ma-teaser-im-processdocs` — Investment Teaser, Information Memorandum und Prozessdokumente erstellen.
- `grosskanzlei-corporate-ma-simulation-bidder-process` — Bieterprozess simulieren für Training und Mandatsvorbereitung.
- `grosskanzlei-corporate-ma-translations-multijurisdictional` — Multi-Jurisdiction-Koordination und Uebersetzungen.
- `grosskanzlei-corporate-ma-rechtsprechungsrecherche` — Rechtsprechungsrecherche für Gutachten, Schriftsatz oder DD-Report.
- `grosskanzlei-corporate-ma-board-paper-business-judgment` — Board Paper und Business Judgment Rule Pruefung.
- `grosskanzlei-corporate-ma-automation-monitoring` — Monitoring und Automatisierungen für laufende M&A-Mandate einrichten.

**Kanzlei-Querschnitt**
- `grosskanzlei-corporate-ma-billing-narratives` — Billing Narratives und Abrechnung für M&A-Mandate erstellen.
- `grosskanzlei-ma-erechnung-gobd` — GoBD-konformer Billing- und E-Rechnungsworkflow.
- `grosskanzlei-corporate-ma-ki-governance-berufsrecht` — KI-Einsatz im Transaktionsmandat berufsrechtlich absichern.
- `grosskanzlei-corporate-ma-freundlicher-copilot` — Freundlicher Copilot-Modus für Junior-Associates und Trainees.
- `ki-einsatz-bei-gutachten-mandatsseite` — Grosskanzlei-Mandatsseite bei KI-Verdacht gegenueber Sachverstaendigengutachten.

## Worauf besonders achten

- Signing ohne erfuellte CPs schafft schwebende Unwirksamkeit; CP-Checkliste muss lueckenlos sein.
- W&I-Versicherungsschlupfloecher: Policy deckt typischerweise keine Steuern, keine Pensionsverpflichtungen und keine bekannten Risiken ab; DD-Ergebnis und Policy-Schutzbereich muessen abgeglichen werden.
- FDI-Pruefung und Fusionskontrolle laufen parallel; unterschiedliche Fristen bei EU-Kommission, Bundeskartellamt und BMWK erfordern sorgfaeltige Koordination.
- GoBD-konforme E-Rechnung ist seit 2025 für B2B-Transaktionen Pflicht (gestaffelt); Kanzlei muss eigene Rechnungen anpassen.
- KI-generierte DD-Berichte und Schriftsaetze muessen vor Versand auf Halluzinationen und Quellenangaben geprueft werden (§ 43a BRAO Sorgfaltspflicht).

## Typische Fehler

- Datenraum-Indexierung vergessen: Ohne klare Nummerierung und Kategorien koennen Datenpunkte in DD-Berichten nicht zugeordnet werden.
- Knowledge-Qualifier zu grosszuegig: Breite Wissensdefinition im SPA erhoht Haeftungsrisiko des Verkaeufers erheblich.
- Anteilsvinkulierung uebersehen: Bei GmbH-Anteilen kann Satzung Zustimmungserfordernis der Gesellschaft vorsehen; fehlende Zustimmung macht Abtretung unwirksam.
- Umwandlungssteuerliche Rueckwirkung versaeumt: Stichtag für steuerliche Rueckwirkung bei Verschmelzung ist maximal acht Monate vor Anmeldung; spaetere Einreichung schliesst Rueckwirkung aus.
- PMI-Planung vernachlaessigt: Earn-Out-Mechanismen, Carve-out-Restaufgaben und Mitarbeitertransfer werden nach Closing haeufig nicht geplant und fuehren zu SPA-Streitigkeiten.

## Quellen und Aktualitaet

- Stand: 05/2026
- BGB, GmbHG, AktG, UmwG, UmwStG, WpUeG, StaRUG, InsO, GWB, FKVO, AWG in aktuell geltender Fassung
- GoBD-Schreiben BMF (Stand 2019; aktuell keine Neufassung)

---

## Skill: `automation`

_Monitoring und Automatisierungen für laufende M&A-Mandate einrichten: Anwendungsfall Deal-Team benoetigt automatisierte Überwachung von Datenraum-Neuzugaengen Q&A-Deadlines CP-Fristen Registerupdates und MAR-Signalen. §§ 35 ff. GWB Kartellrechtsfristen, §§ 55 ff. AWV FDI-Fristen, Art. 17 MAR Ad-h..._

# Automationen und Monitoring (Corporate M&A)

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Automationen und Monitoring (Corporate M&A)
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Triage zu Beginn

Vor dem Entwurf eines Monitoring-Plans klaeren:

1. **Deal-Phase:** Pre-Signing (Datenraum, Q&A, LOI-Frist) oder Post-Signing (CP-Deadlines, Regulatorie, § 613a BGB) oder PMI?
2. **Insiderinformationen betroffen?** Monitoring von boersenrelevanten Informationen erfordert MAR-Freigabe (Art. 17 MAR); automatische Aussenkommunikation ist verboten.
3. **Datenquellen identifiziert?** VDR (Intralinks, Datasite), Handelsregister, Bundesanzeiger, BKartA-Datenbank, DPMA, Nachrichtendienste?
4. **Owner-Matrix vorhanden?** Wer ist verantwortlich für welchen Workstream? Ohne Owner kein Monitoring-Plan.
5. **Eskalationsregeln definiert?** Ab wann wird eskaliert? (CP-Frist < 14 Tage, Datenraum-Neuzugang kritische Kategorie, MAR-Signal erkannt)
6. **Vertraulichkeitsrahmen geklaert?** Monitoring von externen Quellen muss Mandatsgeheimnis (§ 43a Abs. 2 BRAO) und DSGVO (Art. 5 DSGVO) beachten.

## Zentrale Normen

Art. 17 MAR (Ad-hoc-Publizitaet; Insiderinformationen) — §§ 33 ff. WpHG (Stimmrechtsmitteilungen bei boersennotierter Zielgesellschaft) — §§ 35 ff. GWB (Fusionskontrolle BKartA; Vollzugsverbot bis Freigabe) — §§ 55 ff. AWV (FDI-Screening BMWK) — § 40 GmbHG (Gesellschafterliste; aktuelle Registerpublizitaet) — § 15 HGB (Handelsregisterpublizitaet; negative Publizitaet) — Art. 28 DSGVO (Auftragsverarbeitungsvertrag bei Monitoring-Dienstleistern) — § 43a Abs. 2 BRAO (Verschwiegenheitspflicht bei Monitoring-Datenverarbeitung)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Monitoring-Kategorien und Pruefliste

### A: Datenraum-Monitoring (Pre-Signing)

| Monitor | Quelle | Frequenz | Owner | Eskalation |
|---|---|---|---|---|
| Neuzugaenge kritische Kategorie | VDR-API / Aktivitaetslog | Stundlich | DD-Lead | Sofort bei neuen Finanzunterlagen oder Material Adverse Change |
| Q&A-Antworten mit NDA-Implikation | VDR-Q&A | Taeglich | Legal | Bei Ablehnung oder Ausweichen |
| VDR-Zugriffsprotokoll | VDR-Admin | Woechentlich | IT-Security | Bei unberechtigtem Zugriff |

### B: CP-Deadline-Monitoring (Post-Signing)

| Monitor | Norm | Frist | Owner | Eskalation bei |
|---|---|---|---|---|
| Fusionskontrolle BKartA | §§ 35 ff. GWB | Vertraglich (typisch 3-6 Monate) | Regulatory-Lead | < 14 Tage bis Frist |
| FDI-Screening BMWK | §§ 55 ff. AWV | Vertraglich / gesetzlich | Regulatory-Lead | Behördenanfrage unbeantwortet |
| AR-Zustimmungsbeschluss | § 179a AktG | Vor Closing | Corporate-Lead | 21 Tage vor Closing |
| CoC-Zustimmungen (Tier 1-3) | Vertragliche Klauseln | SPA-Frist | Vertragslegal | Verweigerung oder Schweigen |
| Gesellschafterliste § 40 GmbHG | § 40 GmbHG | Unverzueglich nach Closing | Corporate-Lead | > 14 Tage nach Closing |

### C: Register-Monitoring (Laufend)

| Monitor | Quelle | Frequenz | Owner |
|---|---|---|---|
| Handelsregister Zielgesellschaft | www.handelsregister.de | Woechentlich | Corporate-Ass. |
| Bundesanzeiger Zielgesellschaft | Bundesanzeiger.de | Monatlich | Corporate-Ass. |
| DPMA IP-Register | dpma.de | Monatlich | IP-Counsel |

### D: Kapitalmarkt-Monitoring (bei boersennotierter Zielgesellschaft)

| Monitor | Norm | Eskalation |
|---|---|---|
| Ad-hoc-Mitteilungen Zielgesellschaft | Art. 17 MAR | Sofort — MAR-Freigabe erforderlich |
| Stimmrechtsmitteilungen | §§ 33 ff. WpHG | Bei Annaehern an 30 % WpUEG-Schwelle |
| Short-Selling-Positionen | EU-Leerverkaufs-VO | Bei ungewoehnlichem Anstieg |

## Schritt-für-Schritt-Workflow

1. **Deal-Phase und Monitoring-Bedarf erfassen:** Welche Workstreams laufen? Welche CPs sind offen? Deadline-Uebersicht aus SPA erstellen.
2. **Owner-Matrix festlegen:** Fuer jeden Monitoring-Bereich einen verantwortlichen Owner (Person + Eskalation) benennen. Kein Monitor ohne Owner.
3. **Technische Quellen definieren:** VDR-API, RSS-Feeds Bundesanzeiger, Handelsregister-Benachrichtigungen aktivieren, MAR-Alert-System konfigurieren.
4. **Eskalationsregeln dokumentieren:** Schwellenwerte (Frist < 14 Tage, kritischer Datenraum-Zugang, MAR-Signal) mit Eskalationsstufe (Owner → Senior Partner → Mandant) verknuepfen.
5. **Stop-Schwellen benennen:** Insiderinformation erkannt → manueller Review vor jeder automatischen Ausgabe. Externer Datenzugriff unklar → Monitoring pausieren.
6. **Monitoring-Plan dokumentieren:** Monitoring-Automation-Plan (Template unten) erstellen und mit Deal-PMO verknuepfen.
7. **Woechentlicher Check:** CP-Status, offene Q&A, neue Registereintraege, MAR-Alerts in Deal-PMO-Wochenbericht einspeisen.

## Output-Template

**Adressat:** Deal-PMO / Senior Partner — Tonfall: sachlich-strukturiert, risikoorientiert

```
MONITORING-AUTOMATION-PLAN
Mandat: [MANDATSCODE]
Zielgesellschaft: [NAME]
Deal-Phase: [PRE-SIGNING / POST-SIGNING / PMI]
Erstellt: [TT.MM.JJJJ]
Owner Monitoring: [NAME]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.
> Insiderinformationen: Freigabe durch [COMPLIANCE-OFFICER] erforderlich.

--- AKTIVE MONITORE ---
| Monitor | Quelle | Frequenz | Owner | Letzter Check | Status |
|---|---|---|---|---|---|
| [MONITOR 1] | [QUELLE] | [FREQUENZ] | [PERSON] | [DATUM] | [OK / ALARM / OFFEN] |

--- OFFENE CP-DEADLINES ---
| CP | Norm | Frist | Status | Eskalation faellig ab |
|---|---|---|---|---|
| Fusionskontrolle | §§ 35 ff. GWB | [DATUM] | [OFFEN / EINGEREICHT / FREIGABE] | [DATUM] |
| FDI BMWK | §§ 55 ff. AWV | [DATUM] | [OFFEN / EINGEREICHT] | [DATUM] |

--- ALARME (Aktuelle Woche) ---
[KEIN ALARM]
oder:
ALARM: [BESCHREIBUNG] — Eskalation an: [PERSON] — Frist: [DATUM]

--- NAECHSTE SCHRITTE ---
1. [AKTION] — Owner: [PERSON] — Frist: [DATUM]
2. [AKTION] — Owner: [PERSON] — Frist: [DATUM]
```

## Rote Schwellen

- **CP-Frist Fusionskontrolle < 7 Tage, kein Freigabestatus** — Vollzugsverbot § 41 GWB; Deal-Coordinator sofort informieren; Pre-Filing-Gespraeche initiieren.
- **MAR-Signal ohne manuellen Review** — automatische Aussenkommunikation verboten; alle MAR-relevanten Ausgaben manuell freigeben lassen.
- **Monitoring ohne Owner** — kein Monitor ohne benannte verantwortliche Person; ohne Owner-Matrix Monitoring-Plan zurueckhalten.
- **Vertrauliche Monitoring-Daten an unautorisierten Dritten** — § 43a Abs. 2 BRAO; sofortiger Stopp; Kanzlei-Compliance informieren.

## Arbeitsmodus

- Nur Vorschlaege für Automationen machen, keine vertraulichen Daten ungefragt beobachten.
- Monitoringziel, Frequenz, Quelle, Owner und Output definieren.
- Eskalationsregeln und Stoppschwellen festlegen.
- Automationsvorschlaege mit Deal-PMO verknuepfen.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, naechster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Uebergabe an andere Skills

- Komplexe Eingaenge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurueckspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknuepfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams fuehren.

## Vorlagen

- assets/templates/monitoring-automation-plan.md
- assets/templates/deal-pmo-weekly.md

## Quellen und Vertiefung

- Art. 17 MAR (Ad-hoc-Publizitaet; Insider-Monitoring)
- §§ 35, 41 GWB (Fusionskontrolle; Vollzugsverbot)
- §§ 55 ff. AWV (FDI-Screening)
- § 40 GmbHG (Gesellschafterliste; Registerpublizitaet)
- Art. 28 DSGVO (Datenschutz bei Monitoring-Dienstleistern)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mestmäcker/Veelken, in: Immenga/Mestmäcker, GWB, 6. Aufl. 2021, § 41 Rn. 1 ff.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- §§ 705 ff. BGB (GbR)
- §§ 105 ff. HGB (OHG)
- §§ 161 ff. HGB (KG)
- §§ 13, 15 GmbHG (Anteilsübertragung)
- § 53 GmbHG (Satzungsänderung)
- § 33 GWB, FKVO 139/2004 (Fusionskontrolle)
- § 311 BGB i.V.m. §§ 433, 453 BGB (Unternehmenskauf, share/asset deal)
- §§ 25, 28 HGB (Firmenfortführung, Haftung)
- §§ 2-4 UmwG (Verschmelzung)
- § 1 InvKG, AWG/AWV §§ 55-62 (Investitionsprüfung)

### Leitentscheidungen

- BGH II ZR 17/19 (Earn-Out-Klauseln, Kontrolle)
- BGH II ZR 280/14 (Gewährleistungsausschluss share deal)
- BGH II ZR 109/13 (W&I-Versicherung, Sale and Purchase)
- EuGH C-93/13 P (FKVO-Verfahren)
- BGH II ZR 71/11 (Auskunftsrechte Datenraum)

### Anwendung im Skill

- Share Deal vs. Asset Deal Wahl an Steuer-, Haftungs- und Genehmigungsfolgen, nicht am LMA-Standard ausrichten.
- W&I-Versicherung nach BGH II ZR 109/13 ergaenzt, ersetzt aber keine Garantien.
- Fusionskontrolle § 39 GWB und FKVO 139/2004: Anmeldepflicht vor Closing pruefen, sonst § 41 GWB-Vollzugsverbot.

---

## Skill: `billing-narratives`

_Big-Law Billing Narratives und Abrechnung für M&A-Mandate erstellen: Anwendungsfall Associate oder Partnerassistenz muss taugliche Time Narratives Phasenbudgets Workstream-Rechnungen Cap- und Success-Fee-Hinweise erstellen. § 3a RVG Stundenhonorar, GoBD Buchungsanforderungen, XRechnung ZUGFeRD. P..._

# Big-Law Billing Narratives (Corporate M&A)

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Big-Law Billing Narratives (Corporate M&A)
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Triage zu Beginn

Vor der Erstellung von Billing Narratives klaeren:

1. **Honorarvereinbarung vorhanden?** Stundenhonorar (§ 3a RVG) oder Pauschalhonorar oder Success Fee oder Cap + Success Fee? Kein Narrative ohne klar definiertes Abrechnungsmodell.
2. **Taetigkeiten vollstaendig erfasst?** Alle Time Entries nach Phase, Workstream und Deliverable vorliegend? Fehlende Entries flaggen.
3. **Budgetstatus geprueft?** Aktuelles WIP gegen Budget halten; Scope Creep und Abweichungen markieren bevor Narrative erstellt wird.
4. **Mandantenvertraulichkeit:** Narrative darf kein Mandatsgeheimnis unnoetig offen legen (§ 43a Abs. 2 BRAO); Formulierungen muessen pruefbar aber nicht erlaeuternd sein.
5. **Rechnungsreife?** Sind alle Bedingungen erfuellt (Leistungsstand, SPA-Meilenstein, vereinbarter Faelligkeitspunkt)? Bei Unsicherheit nicht abrechnen.
6. **E-Rechnung erforderlich?** Oeffentlicher Auftraggeber oder SPA-Klausel zu XRechnung/ZUGFeRD? Dann an `grosskanzlei-ma-erechnung-gobd` uebergeben.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Billing-Narrative-Struktur für M&A-Deals

### Time-Entry-Kategorien

| Phase | Workstream | Typische Taetigkeit |
|---|---|---|
| Pre-DD | Transaction Setup | Mandatsanlage, NDA-Verhandlung, VDR-Einrichtung |
| Due Diligence | Legal DD | Vertragsreview, Issue-Extraktion, Red-Flag-Report |
| Due Diligence | Corporate DD | Handelsregister-Auswertung, Gesellschafterliste |
| Signing | SPA-Verhandlung | Vertragsverhandlung, Kommentierung, Signing-Prep |
| Closing | Vollzug | CP-Tracking, Closing-Actions, Notartermin |
| Post-Closing | PMI | Vertragsuebernahmen, § 613a BGB, Gesellschafterliste |

### Narrative-Formulierungsregeln

1. **Mandantentauglich:** Keine Rechtsbegriffe ohne Erklaerung; kein unnoetig detaillierter Sachverhalt.
2. **Pruefbar:** Jede Taetigkeit muss einem Workstream und Deliverable zugeordnet sein.
3. **Vertraulich:** Kein Inhalt aus privilegierten Dokumenten (anwaltliche Stellungnahmen, DD-Reports) in externe Narrative.
4. **Zeitgenau:** Time Entries tagesgenau; keine rueckwirkenden Grosskorrekturen ohne Erklaerung.
5. **Budget-Delta markieren:** Abweichungen > 10 % zum vereinbarten Budget kommentieren.

### Narrative-Muster nach Workstream

```
Due Diligence — Legal: Vertragsreview (Commercial Contracts)
Pruefen und Analysieren von [N] Lieferantenvertraegen im Datenraum; Erstellung eines
Issue-Summary für [N] Material-Contract-Eintraege; Identifizierung von [N] Change-of-
Control-Klauseln mit Zustimmungserfordernis; Abstimmung mit Deal-Team zu CP-Implikationen.
[N.N h]
```

```
Signing — SPA-Verhandlung: Kommentierung § [Klausel] / Garantiekatalog
Erarbeitung der Kanzleiposition zu Abschnitt [X] des SPA-Entwurfs (Garantiekatalog);
Abstimmung mit Mandant zu akzeptablem Risikoprofil; Einarbeitung in Track-Changes-Version;
Verhandlungssitzung [DATUM] mit Gegenseite.
[N.N h]
```

## Schritt-für-Schritt-Workflow

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Time Entries importieren:** Alle Zeiteintragungen für den Abrechnungszeitraum nach Phase und Workstream sortieren.
2. **Budget-Abgleich:** WIP gegen vereinbartes Budget halten; Abweichungen > 10 % markieren und begruenden.
3. **Narrative verfassen:** Pro Workstream ein Narrative-Block nach Formulierungsregeln oben.
4. **Mandantenvertraulichkeit pruefen:** Kein Mandatsgeheimnis unnoetig offen gelegt? Narratives mandantentauglich formuliert?
5. **Rechnungspflichtangaben pruefen:** § 14 UStG-Angaben vollstaendig (Leistungsbeschreibung, Zeitraum, Steuernummer, USt-ID)?
6. **Cap-/Success-Fee-Check:** Gesamthonorar gegen vereinbarten Cap pruefen; Success-Fee-Bedingungen eingetreten?
7. **E-Rechnungspflicht pruefen:** Oeffentlicher Auftraggeber? XRechnung/ZUGFeRD erforderlich? → an `grosskanzlei-ma-erechnung-gobd` uebergeben.
8. **Rechnungsreife-Ampel ausgeben:** Gruen (alle Bedingungen erfuellt), Gelb (offene Punkte), Rot (Rechnung zurueckhalten).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Billing Narrative für M-and-A-Mandat erstellen | Narrative nach Schema; Template unten |
| Variante A — Mandant will kurzere Rechnungen weniger Detail | Kurzform-Narrative ohne Einzelleistungsaufstellung |
| Variante B — Stuendliche Abrechnung vs Pauschalhonorar | Bei Pauschalhonorar vereinfachtes Narrative ohne Stundenangaben |
| Variante C — Mehrteiliges Projekt Abrechnung in Phasen | Phasen-Narrative separat; Gesamtnachweis am Ende |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template

**Adressat:** Mandant / Matter-Controller — Tonfall: knapp, pruefbar, mandantentauglich

```
BILLING NARRATIVE LEDGER
Mandat: [MANDATSCODE] / [ZIELGESELLSCHAFT]
Abrechnungszeitraum: [DATUM] bis [DATUM]
Erstellt: [TT.MM.JJJJ]
Matter-Controller: [NAME]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.

--- BUDGET-STATUS ---
Vereinbartes Budget: [BETRAG EUR]
WIP aktuell: [BETRAG EUR]
Abweichung: [+ / - BETRAG EUR] ([%])
Scope-Creep-Flag: [KEIN / JA: BESCHREIBUNG]

--- TIME ENTRIES NACH WORKSTREAM ---

WORKSTREAM: Due Diligence — Legal
[DATUM] | [TIMEKEEPER] | [N.N h] | [NARRATIVE]
[DATUM] | [TIMEKEEPER] | [N.N h] | [NARRATIVE]
Gesamt Workstream: [N.N h] / [BETRAG EUR]

WORKSTREAM: SPA-Verhandlung
[Analog]
Gesamt Workstream: [N.N h] / [BETRAG EUR]

WORKSTREAM: Closing
[Analog]
Gesamt Workstream: [N.N h] / [BETRAG EUR]

--- RECHNUNGS-ZUSAMMENFASSUNG ---
Honorar netto: [BETRAG EUR]
Umsatzsteuer 19 %: [BETRAG EUR]
Auslagen: [BETRAG EUR]
Summe brutto: [BETRAG EUR]
Cap-Pruefung: [UNTER CAP / CAP ERREICHT]
Success Fee: [NICHT FAELLIG / FAELLIG: BETRAG EUR]

--- RECHNUNGSREIFE-AMPEL ---
Status: [GRUEN / GELB / ROT]
Offene Punkte: [KEINE / LISTE]
Freigabe durch: [PARTNER-NAME]

--- E-RECHNUNG ---
XRechnung/ZUGFeRD erforderlich: [JA → Uebergabe grosskanzlei-ma-erechnung-gobd / NEIN]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Rote Schwellen

- **Honorarvereinbarung § 3a RVG muendlich oder fehlend** — Formverstos; Anwalt kann nur RVG-Pflichtgebuehren verlangen; Vereinbarung unverzueglich schriftlich nachholen.
- **Narrative enthaelt Mandatsgeheimnis** — § 43a Abs. 2 BRAO; Formulierungen vor Versand pruefen; keine anwaltlichen Stellungnahmen, keine Parteiinterna in externen Narratives.
- **WIP ueberschreitet Cap ohne Mandanteninformation** — Haftungsrisiko; Mandant informieren und Scope-Abgleich durchfuehren bevor weitergearbeitet wird.
- **Rechnungspflichtangaben § 14 UStG unvollstaendig** — kein Vorsteuerabzug für Mandant; Rechnung korrigieren; Mahngebueehr-Risiko.
- **Leistung ohne Akte / Workstream** — GoBD-Verstos; Time Entry kann nicht verbucht werden; Nacherfassung nur mit Erklaerung.

## Arbeitsmodus

- Taetigkeiten nach Phase, Workstream und Deliverable erfassen.
- Narratives knapp, mandantentauglich und pruefbar formulieren.
- Budgetabweichungen und Scope Creep markieren.
- WIP, Cap, Success Fee, Auslagen, Rabatte und Steuerlogik als eigene Pruefpunkte fuehren.
- Bei Rechnungsreife an `grosskanzlei-ma-erechnung-gobd` uebergeben.

## Standardausgabe

- Billing Narrative Ledger.
- Budgetstatus nach Workstream.
- Rechnungsreife-Ampel.
- Uebergabe an E-Rechnung/GoBD mit Belegkette.

## Vorlagen

- assets/templates/billing-narrative-ledger.md
- assets/templates/erechnung-gobd-billing.md

## Quellen und Vertiefung

- § 3a RVG (Stundenhonorar-Vereinbarung; Formerfordernis)
- § 49b BRAO (Vergaetungsvereinbarung)
- § 4a RVG (Erfolgshonorar)
- § 14 UStG (Rechnungspflichtangaben)
- § 146 AO / §§ 238 ff. HGB (GoBD; Buchfuehrungspflicht)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mayer, in: Gerold/Schmidt, RVG, 26. Aufl. 2023, § 3a Rn. 5 ff.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---
<!-- AUDIT 27.05.2026 bundle_004 -->
**Halluzinations-Audit 27.05.2026**

---

## Skill: `closing-bible`

_Closing Bible und Deal-Archiv erstellen: Anwendungsfall Mandant oder Counsel braucht nach Signing/Closing vollständige Dokumentensammlung aller executed Agreements, Signaturseiten und Registerbelege. §§ 433 ff. BGB SPA-Pflichten, Notarrecht. Prüfraster Vollständigkeit Signaturketten, Versionierun..._

# Closing Bible und Archiv

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Closing Bible und Archiv
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Closing Bible und Archiv und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- aktueller Vertragsentwurf, Markup, Term Sheet und Annex-/Schedule-Struktur.
- CP-Tracker, Closing Deliverables, Board-/Shareholder-Approvals.
- Disclosure Letter, Knowledge-Definition, W&I-Underwriting-Liste.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Rechts- und Workstream-Schnittstellen trennen.** Ordne Punkte in Corporate, Commercial, Tax, Regulatory, Finance, IP/IT, HR, Litigation, Real Estate, ESG und PMO. Vermische DD-Finding, Vertragsfolge und Closing-Aufgabe nicht in einem Satz.
4. **Materiality-Schwelle setzen.** Übernimm Schwellen aus LOI, SPA, DD-Scope oder Kanzlei-Playbook. Fehlt sie, schlage eine vorläufige qualitative Ampel vor: Dealbreaker, Price/Indemnity, Signing/Closing Condition, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen nicht abstrakt, sondern bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht ausdrücklich `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein Senior-Review-Memo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Board Paper, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 133, 157, 241 Abs. 2, 280, 311 Abs. 2, 433 und 453 für Kaufvertrag und Auslegung.
- GmbHG §§ 15 und 16 für Anteilsübertragung und Gesellschafterliste.
- AktG §§ 76, 93, 111 und 179a für Leitungs-/Kontrollpflichten und Strukturmaßnahmen.
- BGB § 158 für Closing Conditions und Bedingungseintritt.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs- oder Aufsichtsratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für die Pflicht zur eigenverantwortlichen Prüfung von Ansprüchen und Organverantwortung ist BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, als Leitentscheidung zu markieren: https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, abrufbar über BGH-Datenbank und dejure: https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Regulatory und Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen oder branchenspezifische Genehmigungen berührt sind, lautet der Zwischensatz nicht nur „Risiko“, sondern: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld- oder Nichtigkeitsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah: Jede rechtliche Annahme bekommt eine Tatsachenquelle. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Das Ergebnis ist als Ampel zu formulieren: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet in M&A regelmäßig: nicht signen, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner/Spezialist freigegeben hat.

## Output-Module
- **Deal-Vermerk:** Executive Summary, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Tabelle mit Finding, Quelle, Risiko, Vertragsfolge, Preis-/Indemnity-Folge, Owner, Deadline.
- **Information Request:** präzise Fragen an Mandant, Gegenseite oder Datenraum-Team, jeweils mit Grund und Priorität.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Board-Paper-Abschnitt.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-spa-apa-entwurf` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-vertragsmarkup-key-issues` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-disclosure-schedules` - wenn Garantien, Knowledge und Disclosure Letter abgeglichen werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Closing Bible und Archiv

## Triage — klaere vor Zusammenstellung

1. Welche Dokumente sind als "final executed" markiert — SPA, aller Anhange, Disclosure Schedules?
2. Liegen alle Signaturseiten im Original oder als beglaubigte Kopie vor?
3. Welche Registeranmeldungen sind erforderlich — GmbH-Anteilsuebertragung, Handelsregistereintrag, Transparenzregister-Update?
4. Sind Notarkosten und Vollzugspflichten aus dem beurkundeten SPA bereits abgearbeitet (§ 15 Abs. 3 GmbHG, § 2 GmbHG)?
5. Welche Closing-Deliverables sind noch offen — Resolutions, Closing Certificates, Funds Flow, Bankfreigaben?

## Zentrale Rechtsgrundlagen

- § 15 Abs. 3 u. 4 GmbHG — notarielle Beurkundungspflicht für GmbH-Anteils- und SPA-Uebertragungen
- § 40 GmbHG — Gesellschafterliste nach Anteilsuebertragung innerhalb eines Monats; Pflicht des Notars oder Geschaeftsfuehrers
- § 20 TranspRG i.V.m. § 19 Abs. 1 GwG — Transparenzregistermeldung nach Gesellschafterwechsel innerhalb von zwei Wochen
- § 41 GmbHG — Pflicht zur Buchfuehrung nach Registereintragung
- § 179 AktG — Satzungsaenderung erfordert notarielle Beurkundung und HR-Anmeldung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

1. **Closing-Deliverables-Register anlegen:** alle SPA-Deliverables aus Schedule/Annex extrahieren, Owner und Faelligkeitsdatum zuordnen
2. **Signaturketten pruefen:** für jeden signierten Vertrag: Originalunterschriften, Vollmachten, Vertretungsmacht gemaess Handelsregisterstand pruefen
3. **Notarpflichten abarbeiten:** SPA-Beurkundung, Anteilsuebertragung gemaess § 15 Abs. 3 GmbHG, Anlagen mitbeurkundet?
4. **Registeranmeldungen:** Gesellschafterliste gemaess § 40 GmbHG, HR-Anmeldung Geschaeftsfuehrerwechsel/Satzungsaenderung, Transparenzregister gemaess § 20 TranspRG
5. **Funds Flow und Closing Payments pruefen:** Kaufpreistransfernachweise, Bankbestaetigung, Freistellung von Sicherheiten
6. **Closing Bible zusammenstellen:** Inhaltsverzeichnis mit Tab-Struktur, je Dokument: Bezeichnung, Parteien, Datum, Fassung, Datenraum-Referenz
7. **Offene Punkte als Post-Closing Obligations:** Fristen, Owner, Eskalationsstufe
8. **Archivierung:** Deal-Archiv anlegen mit Zugriffskonzept, Vertraulichkeitsstufen, Retention Policy (§ 257 HGB: 10 Jahre)

## Entscheidungsbaum

- GmbH-Anteilsuebertragung → § 15 Abs. 3 GmbHG → notarielle Beurkundung erforderlich → ohne Beurkundung: Nichtigkeit
- AG-Aktien vinkuliert → Zustimmung Hauptversammlung/AR-Beschluss pruefen → Eintrag Aktienbuch
- Transparenzregisterpflicht → § 19 GwG Wirtschaftlich Berechtigte neu? → Frist 2 Wochen ab Closing
- Registeranmeldung Namenswechsel/Satzungsaenderung → notarielle Form → Registergericht

## Output-Template: Closing Bible Index

**Adressat:** Deal-Team intern und Notar — Tonfall sachlich-strukturiert

```
CLOSING BIBLE
Transaction: [DEALNAME]
Closing Date: [DATUM]
Prepared by: [KANZLEI/PARTNER]

TAB A — TRANSACTION DOCUMENTS
 A-1 SPA, datiert [DATUM], Parteien: [KAEUFER] / [VERKAEUFER]
 A-2 Disclosure Schedules
 A-3 Signing Protocol / Notarakt Nr. [XX/XXXX]

TAB B — CORPORATE APPROVALS
 B-1 Gesellschafterbeschluss Verkaeufer [DATUM]
 B-2 Aufsichtsratsbeschluss [DATUM]
 B-3 Board Resolution Erwerber

TAB C — CLOSING DELIVERABLES
 C-1 Gesellschafterliste neu (§ 40 GmbHG), eingereicht [DATUM]
 C-2 Transparenzregister-Meldung [DATUM]
 C-3 Funds Flow Confirmation [DATUM]
 C-4 Freigabe Bankpfandrecht [DATUM]

TAB D — POST-CLOSING OBLIGATIONS
 D-1 [MASSNAHME] — Owner: [NAME] — Faellig: [DATUM]
```

## Rote Schwellen

- Signaturseite ohne Original-Vollmacht: Human-in-the-loop verlangen, vor Archivabschluss Senior Review
- Gesellschafterliste nicht eingereicht (§ 40 GmbHG): Frist laeuft; Stimmrecht des Erwerbers gefaehrdet (§ 16 Abs. 1 GmbHG)
- Transparenzregistermeldung unterlassen: Bussgeld bis 100.000 EUR (§ 56 GwG)
- Funds Flow nicht belegt: Zahlungsnachweis zwingend vor Closing-Bible-Freigabe

## Standardausgabe

- Closing Bible Index mit Tab-Struktur, Parteien, Datum, Datenraum-ID
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe
- Belegkette: Dokument, Datum, Version, Fundstelle
- Bei hohem Risiko immer Human-in-the-loop und Senior Review

## Uebergabe an andere Skills

- Registerpunkte → `grosskanzlei-corporate-ma-gesellschaftsrecht-register`
- Notartermin, Beurkundungsfragen → `grosskanzlei-corporate-ma-output-versand-signing`
- Transparenzregister, GwG → `grosskanzlei-corporate-ma-conflict-gwg-sanctions`

## Vorlagen

- assets/templates/closing-bible-index.md
- assets/templates/closing-deliverables-register.md

---

## Skill: `corporate-rechtsprechungsrecherche`

_Corporate und M&A Rechtsprechungsrecherche: Anwendungsfall Anwalt braucht für Gutachten, Schriftsatz oder DD-Report relevante BGH-Rechtsprechung zu Organpflichten, Kapitalmarkt, Umwandlung oder Insolvenz. §§ 93 und 179a AktG, § 15 AktG Verfahren. Prüfraster amtliche Bundes- und Landesquellen, Akt..._

# Corporate-Rechtsprechungsrecherche

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Corporate-Rechtsprechungsrecherche
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Corporate-Rechtsprechungsrecherche und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- aktueller Vertragsentwurf, Markup, Term Sheet und Annex-/Schedule-Struktur.
- CP-Tracker, Closing Deliverables, Board-/Shareholder-Approvals.
- Disclosure Letter, Knowledge-Definition, W&I-Underwriting-Liste.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Rechts- und Workstream-Schnittstellen trennen.** Ordne Punkte in Corporate, Commercial, Tax, Regulatory, Finance, IP/IT, HR, Litigation, Real Estate, ESG und PMO. Vermische DD-Finding, Vertragsfolge und Closing-Aufgabe nicht in einem Satz.
4. **Materiality-Schwelle setzen.** Übernimm Schwellen aus LOI, SPA, DD-Scope oder Kanzlei-Playbook. Fehlt sie, schlage eine vorläufige qualitative Ampel vor: Dealbreaker, Price/Indemnity, Signing/Closing Condition, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen nicht abstrakt, sondern bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht ausdrücklich `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein Senior-Review-Memo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Board Paper, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 133, 157, 241 Abs. 2, 280, 311 Abs. 2, 433 und 453 für Kaufvertrag und Auslegung.
- GmbHG §§ 15 und 16 für Anteilsübertragung und Gesellschafterliste.
- AktG §§ 76, 93, 111 und 179a für Leitungs-/Kontrollpflichten und Strukturmaßnahmen.
- BGB § 158 für Closing Conditions und Bedingungseintritt.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs- oder Aufsichtsratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für die Pflicht zur eigenverantwortlichen Prüfung von Ansprüchen und Organverantwortung ist BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, als Leitentscheidung zu markieren: https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, abrufbar über BGH-Datenbank und dejure: https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Regulatory und Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen oder branchenspezifische Genehmigungen berührt sind, lautet der Zwischensatz nicht nur „Risiko“, sondern: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld- oder Nichtigkeitsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah: Jede rechtliche Annahme bekommt eine Tatsachenquelle. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Das Ergebnis ist als Ampel zu formulieren: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet in M&A regelmäßig: nicht signen, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner/Spezialist freigegeben hat.

## Output-Module
- **Deal-Vermerk:** Executive Summary, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Tabelle mit Finding, Quelle, Risiko, Vertragsfolge, Preis-/Indemnity-Folge, Owner, Deadline.
- **Information Request:** präzise Fragen an Mandant, Gegenseite oder Datenraum-Team, jeweils mit Grund und Priorität.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Board-Paper-Abschnitt.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-spa-apa-entwurf` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-vertragsmarkup-key-issues` - wenn der Befund in Vertragsentwurf, Markup oder Key-Issues-Liste einfließen soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-disclosure-schedules` - wenn Garantien, Knowledge und Disclosure Letter abgeglichen werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-closing-bible-archiv` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Corporate-Rechtsprechungsrecherche

## Arbeitsmodus

- Amtliche Bundes- und Landesquellen bevorzugen.
- OpenJur/dejure nur ergänzend nutzen und Fundstellen verifizieren.
- Entscheidungen mit Datum, Aktenzeichen, Fundstelle und Randnummer erfassen.
- Verwertungsnotiz für Vertrag, Memo, Board Paper oder Schriftsatz schreiben.

## Rote Schwellen

- Nicht verifizierte Fundstelle.
- Halluziniertes Aktenzeichen.
- Keine Übertragung auf Deal-Kontext.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Rechtsprechungsrecherche für M-and-A-Fragestellung | Rechercheprotokoll nach Schema; Template unten |
| Variante A — Mandant will nur drei aktuelle BGH-Entscheidungen | Kompaktrecherche ohne erschoepfende Darstellung |
| Variante B — Forschungsfrage im Auslandsrecht | Common-Law-Kompass Skill parallel für auslaendische Rechtsprechung |
| Variante C — Schnellrecherche in 30 Minuten noetig | Priorisierte Suche in JurisPlus Lexis ohne Vollauswertung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Vorlagen

- assets/templates/rechtsprechungsrecherche-deal.md

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Rechtliche Einbettung und Praxiswissen

### Normen und Quellen im M&A-Kontext
- § 43a BRAO — anwaltliche Pflichten: Sorgfalt, Vollstaendigkeit, Unabhaengigkeit
- §§ 675, 280 BGB — Beraterhaftung bei Pflichtverletzung
- § 17 GeschGehG — Schutz von Geschäftsgeheimnissen; gilt für alle Mandatsinhalte
- Art. 17 MAR — bei boersennotierten Zielobjekten: Ad-hoc-Pflicht und Vertraulichkeit

### Leitsaetze aus der Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Human-in-the-loop bei allen hochrisikorelevanten Ausgaben
- Dokumentation: Datum, Bearbeiter, Freigabe durch Senior

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- §§ 705 ff. BGB (GbR)
- §§ 105 ff. HGB (OHG)
- §§ 161 ff. HGB (KG)
- §§ 13, 15 GmbHG (Anteilsübertragung)
- § 53 GmbHG (Satzungsänderung)
- § 33 GWB, FKVO 139/2004 (Fusionskontrolle)
- § 311 BGB i.V.m. §§ 433, 453 BGB (Unternehmenskauf, share/asset deal)
- §§ 25, 28 HGB (Firmenfortführung, Haftung)
- §§ 2-4 UmwG (Verschmelzung)
- § 1 InvKG, AWG/AWV §§ 55-62 (Investitionsprüfung)

### Leitentscheidungen

- BGH II ZR 17/19 (Earn-Out-Klauseln, Kontrolle)
- BGH II ZR 280/14 (Gewährleistungsausschluss share deal)
- BGH II ZR 109/13 (W&I-Versicherung, Sale and Purchase)
- EuGH C-93/13 P (FKVO-Verfahren)
- BGH II ZR 71/11 (Auskunftsrechte Datenraum)

### Anwendung im Skill

- Share Deal vs. Asset Deal Wahl an Steuer-, Haftungs- und Genehmigungsfolgen, nicht am LMA-Standard ausrichten.
- W&I-Versicherung nach BGH II ZR 109/13 ergaenzt, ersetzt aber keine Garantien.
- Fusionskontrolle § 39 GWB und FKVO 139/2004: Anmeldepflicht vor Closing pruefen, sonst § 41 GWB-Vollzugsverbot.

---

## Skill: `datenqualitaet-xai`

_KI-Qualitaetskontrolle und Halluzinations-Absicherung in M&A-Transaktionen: Anwendungsfall KI-generierte DD-Berichte, Klauseln oder Recherchen sollen auf Datenqualitaet, Bias und Black-Box-Risiken geprüft werden. Art. 22 DSGVO automatisierte Entscheidungen, KI-VO Risikoklassen. Prüfraster Halluzi..._

# Datenqualität und XAI-Qualitätskontrolle

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Datenqualität und XAI-Qualitätskontrolle
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Datenqualität und XAI-Qualitätskontrolle und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- Datenraumindex, Q&A-Tracker, IRL und Disclosure-Log.
- NDA, Clean-Room-Protokoll, MAR-Insiderliste falls Public-M&A-Bezug.
- Registerauszüge, wesentliche Verträge, Litigation-Liste, IP/IT- und HR-Unterlagen.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Rechts- und Workstream-Schnittstellen trennen.** Ordne Punkte in Corporate, Commercial, Tax, Regulatory, Finance, IP/IT, HR, Litigation, Real Estate, ESG und PMO. Vermische DD-Finding, Vertragsfolge und Closing-Aufgabe nicht in einem Satz.
4. **Materiality-Schwelle setzen.** Übernimm Schwellen aus LOI, SPA, DD-Scope oder Kanzlei-Playbook. Fehlt sie, schlage eine vorläufige qualitative Ampel vor: Dealbreaker, Price/Indemnity, Signing/Closing Condition, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen nicht abstrakt, sondern bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht ausdrücklich `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein Senior-Review-Memo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Board Paper, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 311 Abs. 2, 241 Abs. 2 und 280 für vorvertragliche Aufklärungspflichten.
- GeschGehG §§ 2, 4, 6 und 17 für Geschäftsgeheimnisse im Datenraum.
- GWB §§ 35 ff. und § 41 sowie Art. 7 FKVO für Gun-Jumping und Clean-Room-Fragen.
- MAR Art. 7, 17 und 18 für Insiderinformationen, Ad-hoc-Prüfung und Insiderlisten.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs- oder Aufsichtsratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für die Pflicht zur eigenverantwortlichen Prüfung von Ansprüchen und Organverantwortung ist BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, als Leitentscheidung zu markieren: https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, abrufbar über BGH-Datenbank und dejure: https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Regulatory und Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen oder branchenspezifische Genehmigungen berührt sind, lautet der Zwischensatz nicht nur „Risiko“, sondern: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld- oder Nichtigkeitsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah: Jede rechtliche Annahme bekommt eine Tatsachenquelle. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Das Ergebnis ist als Ampel zu formulieren: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet in M&A regelmäßig: nicht signen, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner/Spezialist freigegeben hat.

## Output-Module
- **Deal-Vermerk:** Executive Summary, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Tabelle mit Finding, Quelle, Risiko, Vertragsfolge, Preis-/Indemnity-Folge, Owner, Deadline.
- **Information Request:** präzise Fragen an Mandant, Gegenseite oder Datenraum-Team, jeweils mit Grund und Priorität.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Board-Paper-Abschnitt.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-datenraum-gap-clean-room` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-due-diligence-legal` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-qa-information-requests` - wenn Findings in Information Requests und Seller-Q&A übersetzt werden müssen.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-due-diligence-reporting` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Datenqualität und XAI-Qualitätskontrolle

## Arbeitsmodus

- Datenqualität, Quellenstatus, Stichprobe und Plausibilisierung festhalten.
- Explainability-Anforderungen für jedes Ergebnis markieren.
- Human-in-the-loop und Senior Review dokumentieren.
- Fehler, Annahmen und nicht geprüfte Bereiche offenlegen.

## Rote Schwellen

- Keine Belegkette.
- Nicht erklärbares Ergebnis bei hohem Risiko.
- Bias oder Datenlücke wird nicht benannt.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/data-quality-gate.md
- assets/templates/xai-quality-control-log.md

## Triage

1. Welche Datenquellen wurden für die M&A-Analyse genutzt — Datenraum, Handelsregister, Pressemitteilungen, Expert Calls?
2. Welche Ergebnisse basieren auf automatisierter Verarbeitung — DD-Analyse, Vertragsmarkup, Risikobewertung?
3. Gibt es Bereiche, die nicht geprueft wurden — fehlende Daten, eingeschraenkter Datenraum, nicht zugaengliche Unterlagen?
4. Welche Ergebnisse haben hohes Risiko und erfordern Senior Review?

## Zentrale Rechtsgrundlagen

- Art. 22 DSGVO — automatisierte Einzelentscheidungen: bei rechtlich bedeutsamen Entscheidungen darf keine vollautomatische Entscheidung ohne menschliche Ueberpruefung getroffen werden
- Art. 13, 14 EU-KI-Verordnung (in Kraft ab 2024/2025) — KI-Systeme mit hohem Risiko muessen transparent, pruefbar und erklaerbar sein; Dokumentationspflichten
- §§ 675, 280 BGB — Beraterhaftung: Ergebnisse, die auf unzuverlaessigen Daten basieren, koennen Schadensersatz ausloesen; Anwalt muss Datenbasis offenlegen
- § 43a BRAO — Unabhaengigkeit: Anwalt darf sich nicht auf Ergebnisse verlassen, die er nicht nachpruefen kann

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

1. **Datenquellen dokumentieren:** alle verwendeten Quellen mit Datum, Version, Zugaenglichkeit; Luecken explizit benennen
2. **Stichprobe und Plausibilisierung:** 10-20 % der Ergebnisse manuell querprufen
3. **Explainability-Flag setzen:** je Ergebnis mit hohem Risiko: Human muss Ergebnis nachvollziehen koennen
4. **Halluzinations-Check:** Leitsatz-Zitate, Normen, Aktenzeichen — alle Faktenangaben verifizieren
5. **Human-in-the-loop-Protokoll:** wer hat geprueft, wann, Ergebnis der Pruefung

## Rote Schwellen

- Keine Belegkette für wesentliche Ergebnisse: Haftungsrisiko
- Nicht erklaerbares Ergebnis bei hohem Risiko: sofortige Senior Review; kein Versand
- Bias oder Datenlücke nicht benannt: moeglicherweise fehlerhafte Mandatsberatung

---

## Skill: `datenraum-aufbau`

_Due Diligence Datenraum strukturieren und bestücken: Anwendungsfall Mandant bereitet Verkaufsprozess vor oder Buyer-Team benoetigt strukturierten Datenraum für Private M&A, Public M&A, Carve-out oder Distressed-Prozesse. §§ 433 ff. BGB, SPA DD-Pflichten, MAR Vertraulichkeit. Prüfraster Ordnerstru..._

# Datenraum-Aufbau

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Datenraum-Aufbau
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Datenraum-Aufbau und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- Datenraumindex, Q&A-Tracker, IRL und Disclosure-Log.
- NDA, Clean-Room-Protokoll, MAR-Insiderliste falls Public-M&A-Bezug.
- Registerauszüge, wesentliche Verträge, Litigation-Liste, IP/IT- und HR-Unterlagen.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Rechts- und Workstream-Schnittstellen trennen.** Ordne Punkte in Corporate, Commercial, Tax, Regulatory, Finance, IP/IT, HR, Litigation, Real Estate, ESG und PMO. Vermische DD-Finding, Vertragsfolge und Closing-Aufgabe nicht in einem Satz.
4. **Materiality-Schwelle setzen.** Übernimm Schwellen aus LOI, SPA, DD-Scope oder Kanzlei-Playbook. Fehlt sie, schlage eine vorläufige qualitative Ampel vor: Dealbreaker, Price/Indemnity, Signing/Closing Condition, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen nicht abstrakt, sondern bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht ausdrücklich `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein Senior-Review-Memo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Board Paper, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 311 Abs. 2, 241 Abs. 2 und 280 für vorvertragliche Aufklärungspflichten.
- GeschGehG §§ 2, 4, 6 und 17 für Geschäftsgeheimnisse im Datenraum.
- GWB §§ 35 ff. und § 41 sowie Art. 7 FKVO für Gun-Jumping und Clean-Room-Fragen.
- MAR Art. 7, 17 und 18 für Insiderinformationen, Ad-hoc-Prüfung und Insiderlisten.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs- oder Aufsichtsratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für die Pflicht zur eigenverantwortlichen Prüfung von Ansprüchen und Organverantwortung ist BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, als Leitentscheidung zu markieren: https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, abrufbar über BGH-Datenbank und dejure: https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Regulatory und Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen oder branchenspezifische Genehmigungen berührt sind, lautet der Zwischensatz nicht nur „Risiko“, sondern: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld- oder Nichtigkeitsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah: Jede rechtliche Annahme bekommt eine Tatsachenquelle. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Das Ergebnis ist als Ampel zu formulieren: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet in M&A regelmäßig: nicht signen, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner/Spezialist freigegeben hat.

## Output-Module
- **Deal-Vermerk:** Executive Summary, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Tabelle mit Finding, Quelle, Risiko, Vertragsfolge, Preis-/Indemnity-Folge, Owner, Deadline.
- **Information Request:** präzise Fragen an Mandant, Gegenseite oder Datenraum-Team, jeweils mit Grund und Priorität.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Board-Paper-Abschnitt.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-datenraum-gap-clean-room` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-due-diligence-legal` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-qa-information-requests` - wenn Findings in Information Requests und Seller-Q&A übersetzt werden müssen.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-due-diligence-reporting` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Datenraum-Aufbau

## Arbeitsmodus

- Datenraumindex aus IRL, Deal-Typ und Workstreams erzeugen.
- Dokumente klassifizieren: Vertrag, Register, Steuer, HR, IP, IT, Litigation, ESG, Finance.
- Hauptdokumente, Anlagen und Verwandtschaftsgrade verknuepfen.
- Clean-Room- und Need-to-know-Zonen vorschlagen.

## Rote Schwellen

- Sensible Informationen im falschen Bereich.
- Datenraum ohne Inhaltslogik.
- Offenlegung wesentlicher Informationen an ungewoehnlicher Stelle ohne Hinweis.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/datenraum-index.md
- assets/templates/clean-room-access-log.md

## Triage — klaere vor Datenraum-Aufbau

1. Welcher Deal-Typ — Private M&A, Public M&A, Carve-out, Distressed, SPAC?
2. Sell-side oder Buy-side Datenraum? (Sell-side: strukturierter Bieterprozess; Buy-side: Gegenpruefung)
3. Clean Room erforderlich — bei sensiblen Wettbewerberinfos (Kartellrecht)?
4. Welche Datenraum-Plattform — Datasite, Intralinks, Merrill, Box, SharePoint?
5. Welche Zugangsgruppen sind vorgesehen — Bieter A/B/C, Management, Berater, Konsortien?

## Zentrale Rechtsgrundlagen

- Art. 7 FKVO; § 41 GWB — Vollzugsverbot und Clean-Room-Pflicht für kartellrechtlich sensibler Informationsaustausch vor Freigabe
- Art. 7, 17, 18 MAR — Vertraulichkeit von Insiderinformationen im Datenraum bei boersennotierten Zielunternehmen; Insiderliste bei Datenraumzugang
- § 47 GwG — Verschwiegenheitspflicht; keine Offenlegung geldwaescherelevanter Informationen
- §§ 17, 18 GeschGehG — Schutz von Geschäftsgeheimnissen; Geheimhaltungsvereinbarung muss vor Datenraumzugang vorliegen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

1. **Deal-Typ und Zugriffsstruktur festlegen:** Bieter-Gruppen, Clean-Room-Bereich, Management-Zugang
2. **Index-Struktur erstellen:** Hauptkategorien Corporate, Legal, Finance/Tax, Commercial, HR, IP/IT, Litigation, Real Estate, ESG
3. **Dokumente hochladen und klassifizieren:** je Dokument: Vertragstyp, Parteien, Datum, Relevanz-Flag (High/Medium/Low)
4. **Geheimhaltungsprotokoll:** NDA-Liste, MAR-Insiderliste (falls boersennotiert), Clean-Room-Zugangspro tokoll
5. **IRl-Management:** fehlende Dokumente als Information Request List erfassen; Seller-Response verfolgen
6. **Datenraum-Gap-Analyse:** Vollstaendigkeit gegen Standard-DD-Checkliste pruefen

## Rote Schwellen

- Sensibler Wettbewerber-Datenraum ohne Clean Room: Kartellrechtsverstoss (Art. 7 FKVO)
- Datenraumzugang ohne NDA: Geschaeftsgeheimnisschutz verletzt (GeschGehG)
- Insiderinformationen ohne MAR-Insiderliste: Aufsichtsrisiko (MAR Art. 18)

---

## Skill: `datenraum-gap-clean`

_Datenraum-Lueckenanalyse und Clean-Room-Protokoll für M&A Due Diligence: Anwendungsfall Anwalt oder Mandant stellt fest dass Datenraum Luecken hat oder sensible Wettbewerbsdaten nur unter Clean-Room-Bedingungen geteilt werden koennen. §§ 35 ff. GWB Fusionskontrolle, Kartellrecht. Prüfraster fehle..._

# Datenraum-Gap-Analyse und Clean Room

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Datenraum-Gap-Analyse und Clean Room
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Datenraum-Gap-Analyse und Clean Room und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für ein M&A-Mandat aus Sicht von Buy-side, Sell-side oder Target."
- "Mach daraus eine Partner-/Mandantenunterlage mit Risiken, Annahmen und offenen Punkten."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-kommandocenter` oder `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-deal-intake`. Wenn der Nutzer ausdrücklich nur eine kurze Sprachfassung, Übersetzung oder E-Mail will, arbeite knapp und route nicht in einen Deep-Dive.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/grosskanzlei-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle der Kanzlei, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Jurisdiktionen, Signing-/Closing-Zeitplan, Vertraulichkeitsstufe und gewünschtes Output-Format.

Benötigte Unterlagen:
- Datenraumindex, Q&A-Tracker, IRL und Disclosure-Log.
- NDA, Clean-Room-Protokoll, MAR-Insiderliste falls Public-M&A-Bezug.
- Registerauszüge, wesentliche Verträge, Litigation-Liste, IP/IT- und HR-Unterlagen.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Rechts- und Workstream-Schnittstellen trennen.** Ordne Punkte in Corporate, Commercial, Tax, Regulatory, Finance, IP/IT, HR, Litigation, Real Estate, ESG und PMO. Vermische DD-Finding, Vertragsfolge und Closing-Aufgabe nicht in einem Satz.
4. **Materiality-Schwelle setzen.** Übernimm Schwellen aus LOI, SPA, DD-Scope oder Kanzlei-Playbook. Fehlt sie, schlage eine vorläufige qualitative Ampel vor: Dealbreaker, Price/Indemnity, Signing/Closing Condition, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen nicht abstrakt, sondern bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht ausdrücklich `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein Senior-Review-Memo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Board Paper, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite taktisch sinnvoll ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 311 Abs. 2, 241 Abs. 2 und 280 für vorvertragliche Aufklärungspflichten.
- GeschGehG §§ 2, 4, 6 und 17 für Geschäftsgeheimnisse im Datenraum.
- GWB §§ 35 ff. und § 41 sowie Art. 7 FKVO für Gun-Jumping und Clean-Room-Fragen.
- MAR Art. 7, 17 und 18 für Insiderinformationen, Ad-hoc-Prüfung und Insiderlisten.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs- oder Aufsichtsratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für die Pflicht zur eigenverantwortlichen Prüfung von Ansprüchen und Organverantwortung ist BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, als Leitentscheidung zu markieren: https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, abrufbar über BGH-Datenbank und dejure: https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Regulatory und Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen oder branchenspezifische Genehmigungen berührt sind, lautet der Zwischensatz nicht nur „Risiko“, sondern: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld- oder Nichtigkeitsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah: Jede rechtliche Annahme bekommt eine Tatsachenquelle. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Das Ergebnis ist als Ampel zu formulieren: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet in M&A regelmäßig: nicht signen, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner/Spezialist freigegeben hat.

## Output-Module
- **Deal-Vermerk:** Executive Summary, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Tabelle mit Finding, Quelle, Risiko, Vertragsfolge, Preis-/Indemnity-Folge, Owner, Deadline.
- **Information Request:** präzise Fragen an Mandant, Gegenseite oder Datenraum-Team, jeweils mit Grund und Priorität.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Board-Paper-Abschnitt.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-datenraum-aufbau` - wenn Dokumente, Datenraumlücken oder Clean-Room-Fragen der nächste Engpass sind.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-due-diligence-legal` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-qa-information-requests` - wenn Findings in Information Requests und Seller-Q&A übersetzt werden müssen.
- `/grosskanzlei-corporate-ma:grosskanzlei-corporate-ma-due-diligence-reporting` - wenn aus Unterlagen ein Legal-DD-Befund oder DD-Report gebaut werden soll.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Datenraum-Gap-Analyse und Clean Room

## Arbeitsmodus

- Datenraum gegen IRL und IM abgleichen.
- Referenzierte, aber fehlende Dokumente finden.
- Widersprüche zwischen Legal, Tax, Finance, ESG und Commercial markieren.
- Clean-Room-Zugriffe und kartellrechtliche Sensibilitaet protokollieren.

## Rote Schwellen

- Antitrust-sensible Daten offen zugänglich.
- Wichtige Dokumente nur implizit oder unklar benannt.
- KI-sortierter Datenraum ohne menschliches Gate.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/datenraum-gap-analysis.md
- assets/templates/clean-room-access-log.md
- assets/templates/data-quality-gate.md

## Triage

1. Liegt ein vollstaendiger Datenraum-Index vor oder muss dieser erst erstellt werden?
2. Gibt es einen Information Request Letter (IRL) — welche Dokumente fehlen noch?
3. Sind kartellrechtlich sensible Informationen im Datenraum (Preise, Kundenlisten, Marktanteile) — ist ein Clean Room erforderlich?
4. Stimmen Teaser und IM mit dem Datenraum-Inhalt ueberein — gibt es wesentliche Abweichungen?

## Zentrale Rechtsgrundlagen

- Art. 7 FKVO; § 41 GWB — Clean-Room-Pflicht bei kartellrechtlich sensiblen Informationen vor Fusionskontrollfreigabe
- §§ 17-18 GeschGehG — Schutz von Geschäftsgeheimnissen: Datenraum-Inhalte unterliegen Geheimhaltung; Clean Room schutzt Wettbewerber-Informationen
- §§ 311, 241 Abs. 2 BGB — Offenbarungspflicht des Verkaeuf ers: wesentliche Risiken muessen offengelegt werden; Fair Disclosure nach BGH
- Art. 7, 17 MAR — bei boersennotiertem Zielobjekt: Insiderinformationen im Datenraum erfordern MAR-konforme Zugangsprotokollierung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

1. **Datenraum-Index auswerten:** Kategorien, Vollstaendigkeit, Duplikate, Versionierung
2. **IRL-Luecken identifizieren:** fehlende Dokumente je Workstream aufführen; Prioritaet High/Medium
3. **Widerspruchsanalyse:** Teaser vs. IM vs. Datenraum — wesentliche Abweichungen → Red Flag
4. **Clean Room pruefen:** kartellrechtlich sensitive Informationen? → Clean Room einrichten; Zugangsproto koll
5. **Disclosure-Konzept bewerten:** allgemeine Disclosure vs. spezifische Disclosure; Fair-Disclosure-Standard pruefen

## Rote Schwellen

- Kartellrechtlich sensible Infos im normalen Datenraum: Clean-Room-Pflicht verletzt
- IM-Widersprueche: Misrepresentation-Risiko des Verkaeuf ers
- Fehlende wesentliche Dokumente ohne IRL: DD unvollstaendig; Garantierisiko

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

