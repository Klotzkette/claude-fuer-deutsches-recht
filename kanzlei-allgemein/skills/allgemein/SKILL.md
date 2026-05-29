---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Kanzlei Allgemein-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Spezial-Skills oder stellt genau eine gezielte Rückfrage."
---

<!-- konvers-stil-v1 -->

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Spezial-Skills dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Kanzlei Allgemein — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Kanzlei Allgemein**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Kanzlei-Allgemein-Plugin (fusioniert mit Cowork): edles Kommandocenter Mandatsannahme/GwG Klage/Replik Vertrag Rechtsprechung Handelsregister beA-Journal Rechnung UStVA Fristenbuch Timesheet RVG Versand-Vor-Check Posteingang Mandantenakte Mahnwesen Tagesbrief Geburtstage Weihnachtskarten.

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
| `aktenbestand-pflege` | Laufende Pflege des Aktenbestands der Kanzlei — Aktualisierung Aktenstatus (laufend / ruhend / abgeschlossen) Mandatsende mit Schlussrechnung und Aktenherausgabe an Mandant Archivierung nach Aufbewahrungspflicht (§ 50… |
| `bea-versand-pruefen` | Prüft den beA-Versand nach Pflichten des § 130a ZPO § 32d StPO § 65d SGG § 55a VwGO § 52d FGO sowie § 31a BRAO. Erforderliche Beachtung sicherer Übermittlungsweg (sUW durch persoenliches Versenden des beA-Inhabers)… |
| `fristenbuch-fuehren` | Zentrales Fristenbuch für die Kanzlei mit Haupt- und Vorfristen über alle Rechtsgebiete. Berechnet Fristbeginn nach den jeweiligen Verfahrensordnungen (ZPO StPO SGG FGO VwGO FamFG AO BGB) Vier-Tages-Fiktionen bei… |
| `geburtstage-feiertage` | Pflegt einen Mandanten- und Geschäftspartner-Geburtstagsverteiler. Reminders einige Tage vor dem Tag. Vorlagen für kurze persoenliche Glueckwunsch-E-Mail (formell-warm). Bei Geschäftspartnern auch Firmenjubilaeen.… |
| `kanzlei-allgemein-abwesenheiten-urlaub` | Verwaltung von Abwesenheiten in der Kanzlei — Urlaub Krankmeldung Elternzeit Pflegezeit Fortbildung. Anwendungsfall Anwalt oder Mitarbeiter meldet Urlaub oder Krankheit und Kanzlei muss Vertretung für Fristen beA… |
| `kanzlei-allgemein-akte` | Anlage oder Zuordnung einer Kanzleiakte bei neuer Mandatsanfrage oder eingehendem Schriftstueck. Anwendungsfall Mandant erteilt neuen Auftrag oder Eingang ist keiner Akte zugeordnet. Normen § 43a Abs. 4 BRAO… |
| `kanzlei-allgemein-aktenzeichen` | Erkennung Normalisierung und Verknuepfung von Aktenzeichen in der Kanzlei. Anwendungsfall beA-Nachricht oder Brief enthaelt Aktenzeichen das einer Akte zugeordnet werden muss. Normen § 51 BRAO Organisationspflicht §… |
| `kanzlei-allgemein-automationen` | Plant und dokumentiert wiederkehrende Kanzlei-Routinen als sichere automatisierte Ablaeufe. Anwendungsfall Kanzlei will Postlauf Fristencheck UStVA-Vorbereitung oder Payroll automatisieren. Normen Art. 6 Art. 28 Art.… |
| `kanzlei-allgemein-bea-journal` | Dokumentation von beA-Verbindungen Nachrichten Versand und Empfangsbekenntnissen. Anwendungsfall beA-Eingang oder Versand muss nachvollziehbar protokolliert werden mit Screenshot ZIP-Export und EB-Workflow. Normen §… |
| `kanzlei-allgemein-buchhaltung-konten` | Kanzlei-Buchhaltung mit Geschäftskonto offenen Posten Debitoren Kreditoren und Bankmatching. Anwendungsfall Anwalt oder Kanzleibuero will Zahlungseingang prüfen offene Posten abgleichen oder Buchhaltungsuebergabe an… |
| `kanzlei-allgemein-erechnung` | Elektronische Kanzleirechnung in XRechnung oder ZUGFeRD vorbereiten und validieren. Anwendungsfall Mandant oder öffentliche Hand verlangt Rechnung im Format XRechnung oder ZUGFeRD. Normen EN 16931 GoBD § 14 UStG… |
| `kanzlei-allgemein-freundlicher-copilot` | Führt junge Anwaelte freundlich durch alle Kanzlei-Workflows mit Nachhilfemodus. Anwendungsfall Berufsanfaenger oder Quereinsteiger weiss nicht wie er Akte anlegen Rechnung schreiben oder beA nutzen soll. Prüft Luecken… |
| `kanzlei-allgemein-fristen-monitor` | Scannt Akteninhalt auf Fristen Action-Items Wiedervorlagen und Zustellungen. Anwendungsfall Schriftsatz beA-Nachricht oder Urteil wurde hochgeladen und Fristen sollen automatisch erkannt werden. Normen § 222 ZPO §§ 187… |
| `kanzlei-allgemein-handelsregisterabruf` | Handelsregisterabruf über offizielle Quellen für Unternehmensprüfung in Mandaten. Anwendungsfall Mandant oder Gegner ist eine GmbH und Vertretung Gesellschafterstruktur und Prokura muessen geprüft werden. Normen §§ 15… |
| `kanzlei-allgemein-hr-personal` | Verwaltung von Kanzlei-Personal mit Stammdaten Arbeitsvertraegen Onboarding und Offboarding. Anwendungsfall neue Kanzleimitarbeiterin wird eingestellt oder Mitarbeiter scheidet aus und HR-Dokumentation muss gepflegt… |
| `kanzlei-allgemein-intake` | Strukturiert jeden Kanzlei-Eingang aus Brief Fax beA E-Mail SMS iMessage WhatsApp Telegram Teams Screenshot Upload oder Telefonnotiz. Erkennt Absender Akte Aktenzeichen Fristen Action-Items Datenschutzrisiken und… |
| `kanzlei-allgemein-integrationen-simulation` | Prüft Kanzlei-Integrationen und führt Workflows im Simulationsmodus weiter. Anwendungsfall E-Mail Outlook beA Fax Telefon DMS oder Buchhaltung ist nicht verbunden und Kanzlei will trotzdem Workflows testen. Normen Art.… |
| `kanzlei-allgemein-kaltstart` | Kaltstart des Kanzlei-Allgemein-Plugins und Erfassung des Kanzleiprofils. Anwendungsfall erstes Oeffnen des Plugins oder Kanzlei will Stammprofil neu einrichten. Abfrageraster Kanzleiprofil Aktenzeichen-Konvention… |
| `kanzlei-allgemein-kanzleikalender` | Führt einen Kanzleikalender für Termine Fristen Postlauf HR und Jour fixe. Anwendungsfall Anwalt will tagesaktuelle Übersicht über Termine Fristen Abwesenheiten UStVA-Fälligkeiten und interne Abstimmungen. Normen § 517… |
| `kanzlei-allgemein-kanzleitag-simulation` | Führt im Simulationsmodus durch einen achtstuendigen Kanzleitag für Training und Demo. Anwendungsfall Kanzlei will Arbeitsablaeufe testen neue Mitarbeiter einarbeiten oder Plugin-Workflow vorhalten. Abdeckt… |
| `kanzlei-allgemein-kommandocenter` | Schnellstart und Command Center für Kanzlei-Allgemein-Plugin. Erkennt aus einem Satz den passenden Kanzlei-Workflow, routet zu Mandatsannahme GwG Klage Replik Vertrag Rechtsprechung beA Fristen Rechnung Buchhaltung HR… |
| `kanzlei-allgemein-lohn-sv` | Bereitet Lohnabrechnung Sozialversicherungsmeldungen und Payroll-Übergabe für Kanzleimitarbeiter vor. Anwendungsfall monatliche Lohnabrechnung muss vorbereitet oder Daten für DATEV-Lohnsoftware oder Steuerkanzlei… |
| `kanzlei-allgemein-look-and-feel` | Gestaltet Ausgaben des Kanzlei-Allgemein-Plugins hochwertig ruhig und edel. Anwendungsfall Plugin-Output soll innerhalb Cowork-Grenzen professionell aussehen ohne CSS-Abhaengigkeit. Werkzeuge Markdown-Dashboards… |
| `kanzlei-allgemein-mandatsannahme-gwg` | Führt Mandatsannahme und Geldwäscheprüfung für Kanzleien: Intake, Aktenanlage, Aktenzeichen, Kontoblatt, Konfliktcheck, Kataloggeschäft nach § 2 Abs. 1 Nr. 10 GwG, Identifizierung, Ausweiskopie, Handelsregister,… |
| `kanzlei-allgemein-mandatsvereinbarung` | Erstellt Mandatsvereinbarung Vollmacht Datenschutzhinweis Honorarvereinbarung und Vorschuss. Anwendungsfall neues Mandat soll foermlich begründet werden mit allen Pflichtdokumenten nach BRAO. Normen § 3a RVG… |
| `kanzlei-allgemein-output-versand` | Steuert Output und Versand für Schriftsatz Brief E-Mail Fax beA SMS Messenger Teams und Mandantenportal. Fragt vor beA-Versand ausdrücklich nach Freigabe warnt vor PIN Token und Geheimnissen und dokumentiert Journal… |
| `kanzlei-allgemein-postlauf` | Führt den täglichen Postlauf ideal um 11 Uhr. Prüft neue Eingänge beA-Journal Fristen Action-Items nicht zugeordnete Akten Versandbedarf EB und Rückfragen. Erstellt ein Postlauf-Journal und übergibt an Akten Fristen… |
| `kanzlei-allgemein-qualitaetsgate-hardening` | Haertet Kanzlei-Outputs mit mehrstufigen Qualitaetsgates für Anfaenger und Profis. Anwendungsfall Schriftsatz Vertrag oder beA-Versand soll vor Abgang auf Substanz Vollständigkeit und Haftungsrisiken geprüft werden.… |
| `kanzlei-allgemein-rechnung` | Bereitet Kanzleirechnungen Vorschussrechnungen RVG-Abrechnungen und Stundenhonorare vor. Anwendungsfall Mandat ist abgeschlossen oder Zeitpunkt für Zwischenrechnung ist gekommen. Normen § 10 RVG Pflichtangaben § 14… |
| `kanzlei-allgemein-rechtsprechungsrecherche` | Recherchiert Rechtsprechung zu einer konkreten Sache in amtlichen Datenbanken der Bundesgerichte und Länder, ergänzt OpenJur und dejure.org, bewertet Treffer, erstellt Zitier- und Verwertungsnotizen und legt… |
| `kanzlei-allgemein-schreibcanvas` | Bietet ein freies Schreib-Canvas für Schriftsaetze Briefe Rechnungen beA-Nachrichten und Mandantenkommunikation. Anwendungsfall Anwalt will einen Entwurf strukturieren oder schwache Stellen in einem laufenden Text… |
| `kanzlei-allgemein-schriftsatz-turbo` | Erstellt schnell Klage Replik Antrag Klageerwiderung oder Schriftsatzantwort mit Anlagenlogik. Anwendungsfall Frist laeuft und Schriftsatz muss schnell mit allen Pflichtbestandteilen erstellt werden. Normen § 253 ZPO… |
| `kanzlei-allgemein-ustva-buchhaltung` | Sammelt Rechnungsdaten und Belege für die monatliche Umsatzsteuervoranmeldung. Anwendungsfall Monat ist vorbei und UStVA-Unterlagen muessen für ELSTER oder Steuerkanzlei zusammengestellt werden. Normen §§ 18 21 UStG… |
| `kanzlei-allgemein-ustva-simulation` | Fallback bei ELSTER-Stoerung oder fehlendem Steuersoftware-Zugang für UStVA-Simulation. Anwendungsfall ELSTER-Verbindung funktioniert nicht oder UStVA muss ohne Fachsoftware simuliert werden. Normen § 18 Abs. 1 UStG… |
| `kanzlei-allgemein-vertragsentwurf` | Erstellt Vertragsentwuerfe aus Term Sheet Mandantenangaben oder Vorlagen für jede Vertragsart. Anwendungsfall Mandant braucht Vertragsentwurf und Ausgangsmaterial liegt als Term Sheet Stichpunkte oder Muster vor.… |
| `kanzlei-allgemein-zeitnarrative` | Zeiterfassung mit abrechenbaren Narrativen für Kanzlei-Mandate. Anwendungsfall Anwalt hat Tätigkeit ausgeubt und will Zeit mit praezisem Narrativ erfassen für spaetere Rechnungsstellung. Normen § 10 RVG Pflichtangaben… |
| `kanzlei-cowork-kaltstart-interview` | Kaltstart-Interview für das generische Kanzlei-Cowork-Plugin. Erfragt Kanzleiprofil (Solo / Sozietaet / GmbH / Partnerschaft) Rechtsgebiete-Mix Sekretariat (vorhanden Stellen) Aktenstruktur-Konvention beA-Profil… |
| `mahnwesen-honorar` | Mahnwesen für eigene Honorarforderungen der Kanzlei gegenüber Mandanten. Anwendungsfall Mandant hat Rechnung nicht bezahlt und Kanzlei muss mahnen oder klagen. Normen § 286 BGB Verzugsbeginn § 288 BGB Verzugszinsen §… |
| `mandantenakte-anlegen` | Legt eine Mandantenakte nach Kanzleikonvention an. Erfasst Stammdaten Bevollmaechtigte Mandatsumfang Konfliktprüfung (§ 43a Abs. 4 BRAO § 3 BORA) Datenschutzhinweis (Art. 13 DSGVO) Geldwäsche-Identifizierung (§§ 10 11… |
| `mandantenbrief-vorlagen` | Standardvorlagen für den Mandantenbrief der Kanzlei. Aufbau Anrede Bezug Sachstand Empfehlung naechste Schritte Frist Kostenhinweis Unterschrift mit Berufsbezeichnung. Verschiedene Vorlagen für Mandatseroeffnung… |
| `posteingang-ausgang` | Postein- und Postausgangsbuch führen. Posteingang erfasst Empfangstag (relevant für Fristbeginn nach BRAO Berufsregeln und § 188 ZPO § 122 AO § 37 SGB X) Absender Inhalt Akte Aktion (zur Akte / Antwort durch / Frist… |
| `rechnungserstellung-rvg` | Erstellt Honorarrechnungen nach RVG (Anlage 1 VV RVG Anlage 2 RVG Gebührentabelle) oder nach Honorarvereinbarung mit Stundensatz. Pflichtangaben § 10 RVG (Aktenzeichen Mandant Gegenstand der Tätigkeit… |
| `sekretariats-tagesbrief` | Erzeugt morgens den Tagesbrief der Kanzlei mit allen Informationen die Anwalt und Sekretariat für den Tag brauchen — Fristen heute und in der naechsten Woche Vorfristen aus dem Fristenbuch eingegangene Post vom Vortag… |
| `timesheet-aktenzeitung` | Zeiterfassung pro Mandat (Aktenzeitung) — taegliche Erfassung mit Datum Anwalt Akte Tätigkeit Dauer in 6-Minuten-Bloecken Abrechenbarkeit (abrechenbar / pro bono / nicht abrechenbar) Honorarsatz und Notiz. Reports nach… |
| `umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten` | Anwaltliche Strategie bei dem Vorwurf, ein gerichtliches Sachverständigengutachten sei unter Einsatz künstlicher Intelligenz erstellt worden. Höchstpersönliche Erstellungspflicht (§ 407a Abs. 1 ZPO), keine generelle… |
| `versand-vor-check` | Pflicht-Pre-Check vor jedem ausgehenden Versand — prüft Dokumentidentität (das richtige PDF? Stand vom richtigen Datum? Aktenzeichen passt?) Unterschrift (durch berechtigte Person? eigenhaendig oder qualifizierte… |
| `weihnachtskarten` | Pflegt den Weihnachtskartenversand der Kanzlei. Verteiler mit Empfaenger Anschrift E-Mail Versandart (postalisch / digital) Anredeform Bezug zur Kanzlei. Texte für formell-zurückhaltend warm und persoenlich. Druckliste… |

## Worum geht es?

Das Kanzlei-Allgemein-Plugin (fusioniert mit Cowork) ist das zentrale Workflow-Plugin fuer den gesamten Kanzleibetrieb. Es vereint alle wesentlichen Tagesoperationen einer Anwaltskanzlei: von der Mandatsannahme mit GwG-Pruefung ueber die Erstellung von Klagen, Repliken und Vertraegen bis zur Zeiterfassung, Rechnungsstellung, Buchhaltung und UStVA-Vorbereitung. Hinzu kommen beA-Versand, Postlauf, Fristenbuch, HR und Sekretariatsfunktionen.

Das Plugin folgt einem nachtblauen Kanzleidesign mit silberner Grundstruktur und orangenem Akzent (Cowork-Designsprache) und gibt alle Outputs als Markdown-Dashboards mit Freigabeampeln und Statuskarten aus. Es richtet sich an Einzelanwaelte, Sozietaeten und anwaltliche GmbHs jeder Groesse.

## Wann brauchen Sie diese Skill?

- Sie erhalten eine neue Mandatsanfrage und wollen Intake, GwG-Pruefung, Konfliktcheck und Aktenanlage in einem strukturierten Ablauf durchfuehren.
- Eine Frist laeuft ab und Sie benoetigen schnellen Zugriff auf Fristenbuch, beA-Versand und Schriftsatzerstellung.
- Der Monat endet und Sie wollen Zeiterfassung, Rechnungserstellung, UStVA-Vorbereitung und DATEV-Uebergabe koordinieren.
- Ein Mitarbeiter ist abwesend und Sie muessen Vertretungsregelungen fuer Postlauf, Fristen und beA sicherstellen.
- Sie moechten Kanzlei-Routinen automatisieren oder im Simulationsmodus testen.

## Fachbegriffe (kurz erklaert)

- **beA** — Besonderes elektronisches Anwaltspostfach; Pflichtkanal fuer elektronischen Schriftverkehr mit Gerichten nach § 31a BRAO.
- **GwG** — Geldwaeschegesetz; verpflichtet Kanzleien bei Kataloggeschaeften zur Identifizierung von Mandanten und wirtschaftlich Berechtigten.
- **EB** — Empfangsbekenntnis; Bestaetigung des Empfangs nach § 174 ZPO bei sicherem Uebermittlungsweg.
- **sUW** — Sicherer Uebermittlungsweg im Sinne des § 130a ZPO; beA-Versand zaehlt nur als sUW, wenn der Inhaber selbst versendet.
- **XRechnung / ZUGFeRD** — Elektronische Rechnungsformate nach EN 16931; bei oeffentlichen Auftraggebern Pflicht.
- **RVG** — Rechtsanwaltsvergaetungsgesetz; regelt gesetzliche Gebuehren nach Streitwert und Gebuehrentatbestaenden.
- **DATEV** — Buchhaltungssoftware-System; Plugin bereitet DATEV-Uebergabepakete fuer Steuerberater vor.
- **GoBD** — Grundsaetze zur ordnungsmaessigen Buchfuehrung; gelten fuer die gesamte digitale Aktenfuehrung der Kanzlei.

## Rechtsgrundlagen

- § 43a BRAO — Allgemeine Berufspflichten (Sorgfalt, Verschwiegenheit)
- § 50 BRAO — Aktenaufbewahrungspflicht (sechs Jahre nach Mandatsende)
- § 31a BRAO — Besonderes elektronisches Anwaltspostfach
- §§ 130a 130d ZPO — Elektronische Schriftsaetze und sicherer Uebermittlungsweg
- §§ 2 10 11 GwG — Anwendungsbereich, Identifizierungspflicht, wirtschaftlich Berechtigte
- § 10 RVG — Pflichtangaben der Rechtsanwaltsrechnung
- §§ 14 18 21 UStG — Rechnungsanforderungen und UStVA-Pflicht
- GoBD — Grundsaetze ordnungsmaessiger Buchfuehrung
- Art. 5 Art. 13 Art. 28 Art. 35 DSGVO — Datenschutz in der Kanzlei
- § 7 BUrlG, § 3 PflegeZG, §§ 16 ff. BEEG — Abwesenheitsregelungen

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Kaltstart-Interview: Kanzleiprofil, Aktenzeichen-Konvention, Eingangskanale und Integrationen einrichten.
2. Kommandocenter: Tages-Routing aus einem Satz; Workflow automatisch bestimmen.
3. Mandatsannahme und GwG-Pruefung bei neuem Mandat durchfuehren.
4. Tagesoperationen: Postlauf, beA-Journal, Fristencheck, Schriftsatzerstellung, Zeiterfassung.
5. Monatliche Abschlussarbeiten: Rechnung, UStVA-Vorbereitung, Payroll, DATEV-Uebergabe.

## Skill-Tour (was gibt es hier?)

**Aktenmanagement und Mandatsannahme**
- `aktenbestand-pflege` — Laufende Pflege des Aktenbestands: Aktenstatus, Mandatsende, Archivierung und DSGVO-Speicherbegrenzung.
- `kanzlei-allgemein-akte` — Anlage oder Zuordnung einer Akte bei neuer Mandatsanfrage oder eingehendem Schriftstueck.
- `kanzlei-allgemein-aktenzeichen` — Erkennung, Normalisierung und Verknuepfung von Aktenzeichen.
- `kanzlei-allgemein-intake` — Strukturiertes Einlesen von Eingaengen aus Brief, Fax, beA, E-Mail, Telefon und Upload.
- `kanzlei-allgemein-mandatsannahme-gwg` — Mandatsannahme und GwG-Pruefung: Intake, Aktenanlage, Konfliktcheck, Identifizierung, PEP, BRAK-Dokumentation.
- `kanzlei-allgemein-mandatsvereinbarung` — Mandatsvereinbarung, Vollmacht, Datenschutzhinweis, Honorarvereinbarung und Vorschuss erstellen.
- `mandantenakte-anlegen` — Mandantenakte nach Kanzleikonvention anlegen: Stammdaten, Konfliktcheck, GwG, Honorar.
- `kanzlei-allgemein-kaltstart` — Kaltstart des Plugins: Kanzleiprofil und Stammprofil einrichten.
- `kanzlei-cowork-kaltstart-interview` — Erweitertes Kaltstart-Interview mit Kanzleiprofil-Datei fuer Cowork-Konfiguration.

**Kommandocenter und Navigation**
- `kanzlei-allgemein-kommandocenter` — Schnellstart: erkennt Workflow aus einem Satz und routet zu Mandatsannahme, Klage, Rechnung, HR und mehr.
- `kanzlei-allgemein-freundlicher-copilot` — Fuehrt junge Anwaelte freundlich durch alle Kanzlei-Workflows mit Nachhilfemodus.
- `kanzlei-allgemein-look-and-feel` — Gestaltet Ausgaben hochwertig im nachtblauen Cowork-Design mit Freigabeampeln.

**Schriftsatz, Vertrag und Schreiben**
- `kanzlei-allgemein-schriftsatz-turbo` — Schnellerstellung von Klage, Replik, Antrag und Klageerwiderung mit Anlagenlogik.
- `kanzlei-allgemein-schreibcanvas` — Freies Canvas fuer Schriftsaetze, Briefe und Mandantenkommunikation mit Substanzcheck.
- `kanzlei-allgemein-vertragsentwurf` — Vertragsentwuerfe aus Term Sheet, Stichpunkten oder Vorlagen erstellen.
- `mandantenbrief-vorlagen` — Standardvorlagen fuer Mandantenbriefe: Mandat, Zwischenbericht, Abschluss, Schlussrechnung.
- `umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten` — Anwaltliche Strategie bei Vorwurf des KI-Einsatzes in gerichtlichen Sachverstaendigengutachten.

**Rechtsprechung und Handelsregister**
- `kanzlei-allgemein-rechtsprechungsrecherche` — Rechtsprechungsrecherche in amtlichen Datenbanken und OpenJur mit Zitier- und Quellenprotokoll.
- `kanzlei-allgemein-handelsregisterabruf` — Handelsregisterabruf fuer GmbH-Vertretung, Gesellschafterstruktur und GwG-Dokumentation.

**beA, Versand und Postlauf**
- `bea-versand-pruefen` — beA-Versand pruefen: sicherer Uebermittlungsweg, qeS, Versandquittung, Wiedereinsetzung.
- `kanzlei-allgemein-bea-journal` — beA-Verbindungen, Nachrichten und EB-Workflow dokumentieren.
- `kanzlei-allgemein-output-versand` — Output und Versand steuern: Schriftsatz, Brief, E-Mail, Fax, beA, Messenger.
- `kanzlei-allgemein-postlauf` — Taeglich um 11 Uhr: neue Eingaenge, beA-Journal, Fristen, Action-Items, Versandbedarf.
- `posteingang-ausgang` — Postein- und Postausgangsbuch mit Audit-Trail und Aktenverknuepfung fuehren.
- `versand-vor-check` — Pflicht-Pre-Check vor jedem Versand: Dokumentidentitaet, Unterschrift, Adressat, Anlagen, Versandweg.

**Fristen und Kalender**
- `fristenbuch-fuehren` — Zentrales Fristenbuch: Haupt- und Vorfristen, PostModG-Fiktionen, Eskalation.
- `kanzlei-allgemein-fristen-monitor` — Akteninhalt auf Fristen, Action-Items und Wiedervorlagen scannen.
- `kanzlei-allgemein-kanzleikalender` — Kanzleikalender fuer Termine, Fristen, HR, Jour fixe und UStVA-Faelligkeiten.
- `sekretariats-tagesbrief` — Tagesbrief: Fristen, Vorfristen, Post, Rueckrufe, Termine, Geburtstage, Honorarrueckstaende.

**Zeiterfassung und Rechnung**
- `kanzlei-allgemein-zeitnarrative` — Zeiterfassung mit abrechenbaren Narrativen im 6-Minuten-Takt.
- `timesheet-aktenzeitung` — Zeiterfassung pro Mandat mit Reports nach Mandat, Anwalt und Zeitraum.
- `kanzlei-allgemein-rechnung` — Kanzleirechnungen, Vorschussrechnungen und Stundenhonorare vorbereiten.
- `rechnungserstellung-rvg` — Honorarrechnungen nach RVG oder Honorarvereinbarung mit Pflichtangaben nach § 10 RVG erstellen.
- `kanzlei-allgemein-erechnung` — XRechnung oder ZUGFeRD vorbereiten und validieren.
- `mahnwesen-honorar` — Mahnwesen fuer eigene Honorarforderungen: gestufte Mahnschreiben, Klageentwurf.

**Buchhaltung und UStVA**
- `kanzlei-allgemein-buchhaltung-konten` — Kanzlei-Buchhaltung: Geschaeftskonto, offene Posten, Debitoren, Bankmatching, DATEV-Export.
- `kanzlei-allgemein-ustva-buchhaltung` — UStVA-Unterlagen fuer ELSTER oder Steuerkanzlei zusammenstellen.
- `kanzlei-allgemein-ustva-simulation` — UStVA-Simulation bei ELSTER-Stoerung oder fehlendem Fachsystem-Zugang.

**HR und Abwesenheiten**
- `kanzlei-allgemein-hr-personal` — Kanzlei-Personal: Stammdaten, Arbeitsvertraege, Onboarding, Offboarding.
- `kanzlei-allgemein-lohn-sv` — Lohnabrechnung, Sozialversicherungsmeldungen und Payroll-Uebergabe vorbereiten.
- `kanzlei-allgemein-abwesenheiten-urlaub` — Abwesenheiten verwalten: Urlaub, Krankheit, Elternzeit, Vertretungsregelungen.

**Qualitaetssicherung und Automationen**
- `kanzlei-allgemein-qualitaetsgate-hardening` — Mehrstufige Qualitaetsgates vor Versand: Substanz, Fristen, Zustaendigkeit, Antraege.
- `kanzlei-allgemein-automationen` — Wiederkehrende Kanzlei-Routinen als datenschutzkonforme Automationen planen.
- `kanzlei-allgemein-integrationen-simulation` — Kanzlei-Integrationen pruefen und Workflows im Simulationsmodus testen.
- `kanzlei-allgemein-kanzleitag-simulation` — Achtstuendigen Kanzleitag fuer Training und Demo simulieren.

**Mandantenpflege und Sonstiges**
- `geburtstage-feiertage` — Mandanten-Geburtstagsverteiler und Glueckwunsch-E-Mail-Vorlagen pflegen.
- `weihnachtskarten` — Weihnachtskartenversand: Verteiler, Texte, Druckliste, Datenschutz.

## Worauf besonders achten

- **beA sicherer Uebermittlungsweg**: Nur der persoenliche Versand durch den beA-Inhaber zaehlt als sUW; Versand durch Mitarbeitende erfordert qeS.
- **PostModG seit 1.1.2025**: Die Zustellungsfiktion bei Brief betraegt jetzt vier Werktage (vorher drei); alle Fristberechnungen anpassen.
- **GwG-Kataloggeschaefte nicht uebersehen**: Truhand, Immobilientransaktionen und Gesellschaftsgruendungen loesen GwG-Pflichten aus, auch wenn kein Gerichtsverfahren anhangig ist.
- **DSGVO-Speicherbegrenzung bei Aktenarchivierung**: Nach Ablauf der sechs-jaehrigen Aufbewahrungsfrist (§ 50 BRAO) muessen Akten geloescht werden.
- **Qualitaetsgate vor beA-Versand immer aktivieren**: Ein einmal versandtes beA-Dokument kann nicht zurueckgezogen werden.

## Typische Fehler

- Fristbeginn bei gerichtlicher Post falsch berechnet; PostModG-Fiktion (vier Tage seit 2025) wird nicht beruecksichtigt.
- GwG-Identifizierung bei Mandatsannahme vergessen; Bussgeldrisiko bei Kataloggeschaeft.
- Rechnung ohne Aktenzeichen und Tatigkeitsbeschreibung versandt; verstosst gegen § 10 RVG.
- beA-Versand ohne Empfangsbekenntnis bei Fristen; Fristnachweis fehlt.
- Zeiterfassung tagesverspaetet nachgetragen; GoBD-Zeitstempel-Anforderung nicht erfuellt.

## Querverweise

- `berufsrecht-ki-vertragspruefung` — Berufsrechtliche Pruefung von KI-Diensten, die in Kanzlei-Workflows eingesetzt werden.
- `ki-richtlinie-kanzleien` — KI-Nutzungsrichtlinie als Rahmen fuer den KI-Einsatz im Kanzleibetrieb.
- `kanzlei-builder-hub` — Installation und Verwaltung weiterer Skills.
- `insolvenzverwaltung` — Wenn Mandate in ein Insolvenzverfahren muenden.
- `selbstvertreter-amtsgericht` — Wenn Mandanten ohne Anwalt vor dem Amtsgericht auftreten wollen.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- PostModG: Zustellungsfiktion vier Werktage seit 01.01.2025
- § 23 Nr. 1 GVG: AG-Wertgrenze 10.000 EUR seit 01.01.2026
