---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Lobbyregister Bundestag-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage."
---

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

# Lobbyregister Bundestag — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Lobbyregister Bundestag**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Lobbyregister-Bundestag-Superplugin mit 50 geführten Skills für Registrierungspflicht, Ausnahmen, Registereintrag, Regelungsvorhaben, Stellungnahmen, Finanzdaten, Aktualisierung, Verhaltenskodex, Meldung von Verstößen und Fristen nach LobbyRG.

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
| `adressatenkreis-bundestag-bundesregierung` | Kartiert Adressatinnen und Adressaten nach § 1 LobbyRG: Bundestagsorgane, Mitglieder, Fraktionen, Gruppen, Mitarbeitende, Bundesregierung und Leitungsebenen bis Referatsleitung. Output Adressatenkarte. |
| `aktualisierung-unverzueglich` | Steuert unverzuegliche Updates bei Stammdaten, Personen, Tätigkeitsbeschreibung, Vorhabenbereichen, Regelungsvorhaben, Auftraegen und Auftraggebern. Output Update-Ticket. |
| `anonymisierung-schutzantrag` | Prüft Beschraenkung der Veröffentlichung bei schutzwürdigen Interessen nach § 4 Abs. 6 LobbyRG und Altfall-Anonymisierung. Output Schutzantrag-Skizze. |
| `auftraggeber-ermitteln` | Erfasst Auftraggeberinnen und Auftraggeber bei Interessenvertretung im Auftrag Dritter und die jeweils beauftragte Interessenvertretung. Output Auftraggebermatrix. |
| `ausnahmen-bundesregierung` | Prüft Ausnahmen bei Interessenvertretung gegenüber Bundesregierung und Ministerien nach § 2 Abs. 3 LobbyRG, einschließlich Buergeranfragen, Sachverständigengremien und Ersuchen. Output Ausnahmeprüfung. |
| `ausnahmen-bundestag` | Prüft die Ausnahmen von der Registrierungspflicht bei Interessenvertretung gegenüber Bundestagsadressaten nach § 2 Abs. 2 LobbyRG. Output Ausnahmegutachten kurz mit Restpflichten. |
| `benachrichtigungskonto-monitor` | Richtet Beobachtung von Registereintraegen, Aktualisierungen und Entwicklungen über das Benachrichtigungskonto ein. Output Watchlist. |
| `bestaetigungsdokument-freigabe` | Bestimmt Unterzeichner, Leitungsperson, vertretungsberechtigte Person und interne Freigabe vor Eintragung oder Geschäftsjahresaktualisierung. Output Signaturmappe. |
| `betraute-personen` | Ermittelt Personen, die mit Interessenvertretung nicht nur bei Gelegenheit betraut sind und unmittelbar auftreten. Abgrenzung zu Backoffice, gelegentlicher Hilfe und VZAE. Output Personenliste. |
| `bussgeld-und-pruefverfahren` | Reaktionsbei RfS-Prüfung, Anhörung, Bußgeldrisiko nach § 7 LobbyRG und Kodexverstoss. Output Verteidigungs- und Remediationplan. |
| `datenschutz-nichtöffentliche-angaben` | Ordnet öffentliche und nicht öffentliche Registerangaben, personenbezogene Daten, interne Nachweise und Portalveröffentlichung. Output Datenschutzkarte. |
| `dokumentationsakte-revisionsspur` | Baut Aktenstruktur für Belege, Freigaben, Portal-Screenshots, Kontaktlogs, Kostenmethodik, RfS-Kommunikation und Jahresupdates. Output Aktenplan. |
| `drehtuer-angaben` | Führt durch Angaben zu Mandat, Amt oder Funktion in Bundestag, Bundesregierung oder Bundesverwaltung aktuell oder in den letzten fuenf Jahren. Output Drehtuer-Prüfprotokoll. |
| `end-to-end-registrierungswizard` | Geführter Gesamtmit 50-Skill-Routing: Pflicht, Datenraum, Portal, Freigabe, Aktualisierung, Kodex und Monitoring. Output vollständige Registrierungsmappe. |
| `erstkontakt-offenlegung` | Formuliert Offenlegung beim erstmaligen Kontakt: Identität, Anliegen, Auftraggeber, Registereintrag und Verhaltenskodizes. Output Kontaktbausteine. |
| `erstregistrierung-ausfuellen` | Führt Schritt für Schritt durch den Portal-Ersteintrag: Stammdaten, Personen, Tätigkeit, Finanzen, Vorhaben, Auftraege und Uploads. Output Eingabeplan. |
| `finanzaufwendungen-berechnen` | Berechnet finanzielle Aufwendungen im Bereich Interessenvertretung, Personal- und Sachkosten, Infrastruktur und Zuordnung. Output Kostenblatt. |
| `freiwillige-registrierung` | Berät zu freiwilliger Eintragung nach § 2 Abs. 5 LobbyRG: Rechte, volle Pflichten, Aktualisierung, Verhaltenskodex und Bußgeldrisiko bei falschen Angaben. Output Entscheidungsvermerk. |
| `fremdmandat-agenturfall` | Spezialfür Public-Affairs-Agenturen, Kanzleien, Beratungen und Dienstleister mit mehreren Mandanten. Output Mandanten-Trennblatt. |
| `fristen-und-quartalsmonitor` | Baut Fristenkalender für unverzuegliche Updates, Quartalsfrist für Stellungnahmen, sechs Monate Finanzdaten, jaehrliche Bestätigung und Nachholfristen. Output Fristenbuch. |
| `fruehere-interessenvertretung-exit` | Führt durch Anzeige, dass keine registrierungspflichtige Interessenvertretung mehr betrieben wird, sowie Archivierung und Monitoring der Liste frueherer Eintraege. Output Exit-Akte. |
| `geschaeftsjahresaktualisierung` | Führt durch die mindestens jaehrliche vollständige Überprüfung und Bestätigung des Registereintrags nach § 3 und § 4 LobbyRG. Output Jahresupdate-Mappe. |
| `hauptfinanzierungsquellen` | Strukturiert Hauptfinanzierungsquellen nach § 3 LobbyRG und grenzt Umsaetze, Beitraege, Zuwendungen, Schenkungen und sonstige Einnahmen ab. Output Finanzquellenmatrix. |
| `hauptstadtrepraesentanz` | Prüft, ob eine Geschäftsstelle am Sitz von Bundestag und Bundesregierung als Hauptstadtrepraesentanz anzugeben ist. Output Berlin-Anschrift-Check. |
| `hausausweis-und-anhoerung` | Prüft Auswirkungen des Registerstatus auf Tagesausweis, Gebaeudezutritt und Teilnahme an öffentlichen Anhörungen nach § 6 LobbyRG. Output Zutrittscheck. |
| `interessen-und-vorhabenbereiche` | Ordnet Interessen- und Vorhabenbereiche im Register zu und prüft, ob Themen breit genug und nicht verschleiernd beschrieben sind. Output Bereichsmatrix. |
| `interessenvertretung-begriff` | Prüft, ob eine Kontaktaufnahme unmittelbare oder mittelbare Einflussnahme auf Willensbildungs- oder Entscheidungsprozesse nach § 1 LobbyRG ist. Abgrenzung zu Information, Petition, Servicekontakt und rein lokalem… |
| `interne-lobbyregister-richtlinie` | Erstellt interne Richtlinie für Rollen, Meldewege, Kontaktfreigabe, Registerdaten, Fristen, Verhaltenskodex und Schulung. Output Richtlinienentwurf. |
| `jahresabschluss-rechenschaftsbericht` | Prüft Bereitstellung von Jahresabschluss oder Rechenschaftsbericht, Umgang mit noch nicht aufgestellten Unterlagen und Nachreichpflicht. Output Abschluss-Uploadplan. |
| `konzern-netzwerk-plattform` | Strukturiert Lobbyregisterfragen bei Konzernen, Verbaenden, losen Netzwerken, Plattformen und sonstigen kollektiven Tätigkeiten. Output Eintragungseinheiten-Map. |
| `lobbyregister-intake-mandat` | Erfasst Ausgangslage, Organisation, Kontaktplaene, Auftraggeber, Fristen und Portalstatus vor jeder Lobbyregister-Prüfung. Nutzt LobbyRG §§ 1 bis 5 und Bundestags-Handbuch. Output Intake-Protokoll und Dokumentenliste. |
| `lobbyregister-kommandocenter` | Master-Routing für Lobbyregister-Mandate: Pflichtcheck, Registrierung, Aktualisierung, Verhaltenskodex, Meldung, Sanktion, Unterlagen und naechster Skill. Normen LobbyRG §§ 1 bis 7. Output Mandatskarte, Routing und… |
| `mitgliedschaften-mitgliederzahl` | Erfasst Mitgliederzahl, mitgliedschaftliche Organisation und relevante Mitgliedschaften im Zusammenhang mit Interessenvertretung. Output Mitgliederkarte. |
| `nicht-aktualisiert-risiko` | Prüft Kennzeichnung nicht aktualisiert, Nachholfristen, Übertragung in fruehere Interessenvertreter und Reputationsfolgen. Output Rettungsplan. |
| `öffentliche-zuwendungen` | Prüft Zuwendungen und Zuschuesse der deutschen öffentlichen Hand, EU, Mitgliedstaaten oder Drittstaaten mit Schwelle je Geber. Output Zuwendungsliste. |
| `personen-organisationstyp` | Bestimmt, ob natuerliche Person, juristische Person, Personengesellschaft, Einzelkaufmann, Netzwerk, Plattform oder sonstige Organisation einzutragen ist. Output Typenentscheidung. |
| `portal-account-rollen` | Plant Administrationskonto, Rollen, Zugriffsschutz, Zwei-Personen-Freigabe und Passwortmanager für das Lobbyregisterportal. Output Account-Konzept. |
| `regelungsvorhaben-erfassen` | Erfasst konkrete aktuelle, geplante oder angestrebte Regelungsvorhaben, auch ohne vorhandenen Referentenentwurf oder Drucksache. Output Regelungsvorhaben-Karte. |
| `registereintrag-finalcheck` | Prüft vor Freigabe Vollständigkeit, Richtigkeit, Aktualitaet, Irreführungsfreiheit, Quellenstand und Plausibilitaet aller Pflichtangaben. Output Finalcheck-Protokoll. |
| `registerfuehrende-stelle-kontakt` | Bereitet Anfragen an die registerführende Stelle, Nachweisantworten, Korrekturen und Telefonnotizen vor. Output RfS-Kommunikationsakte. |
| `registrierungspflicht-schwellen` | Prüft § 2 Abs. 1 LobbyRG: regelmäßig, auf Dauer, geschäftsmäßig für Dritte, mehr als 30 Kontakte in drei Monaten, Gegenleistung oder Auftrag. Output Pflichtampel. |
| `schenkungen-sponsoring` | Prüft Schenkungen und sonstige lebzeitige Zuwendungen Dritter, Gesamtstufe, Einzelangaben, Zustimmung und Altfall-Anonymisierung. Output Sponsoring-Check. |
| `stellungnahmen-gutachten-upload` | Prüft Bereitstellungspflicht für grundlegende Stellungnahmen oder Gutachten zu Regelungsvorhaben und Quartalsfrist. Norm § 3 LobbyRG. Output Upload-Log. |
| `suche-open-data-monitor` | Nutzt Suche, Standardlisten, Open Data und API zur Markt-, Compliance- und Gegenparteienprüfung. Output Monitoring-Report. |
| `taetigkeitsbeschreibung` | Formuliert die allgemeine Tätigkeit der Interessenvertretung klar, nicht irreführend und updatefähig. Normen § 3 und § 5 LobbyRG. Output Portaltext. |
| `unterauftragnehmer-erfassen` | Prüft Unterauftragsverhältnisse, eingesetzte Organisationen und natuerliche Personen im Verantwortungsbereich. Output Unterauftragskette. |
| `verhaltenskodex-integritaet` | Operationalisiert Offenheit, Transparenz, Ehrlichkeit und Integritaet nach § 5 LobbyRG und Verhaltenskodex für Kontakte. Output Kodex-Check. |
| `verstoesse-melden` | Führt durch Meldung möglicher Verstoesse gegen Verhaltenskodex oder Registerpflichten an lobbyregister-meldung@bundestag.de. Output Meldungsentwurf. |
| `vertretungsberechtigte-personen` | Ermittelt gesetzliche Vertretungen, Leitungspersonen und Zeichnungsberechtigte für Registerangaben und Bestätigungsdokument. Normen § 3 und § 4 LobbyRG. Output Vertretungsmatrix. |
| `visitenkarte-und-nachweise` | Nutzt die Lobbyregister-Visitenkarte, Registerauszug und interne Nachweise für Kontaktaufnahme, Hausausweis, Anhörung und Compliance-Akte. Output Nachweispack. |

## Worum geht es?

Das Lobbyregister-Bundestag-Plugin unterstuetzt Unternehmen, Verbaende, Agenturen und deren Berater bei der vollstaendigen Erfullung der Pflichten nach dem Lobbyregistergesetz (LobbyRG). Es begleitet den gesamten Lebenszyklus eines Registereintrags: von der Registrierungspflichtpruefung ueber die Erstregistrierung und laufende Aktualisierung bis zur Meldung von Verstoessen und der Erstellung interner Compliance-Strukturen.

Das Plugin adressiert alle Normen der §§ 1 bis 7 LobbyRG sowie ergaenzende Materialien wie das Handbuch der registerfuehrenden Stelle (Bundestag-Verwaltung). Es ist kein Rechtsberatungsersatz, sondern ein strukturiertes Pruefwerkzeug.

## Wann brauchen Sie diese Skill?

- Sie wollen pruefen, ob Ihre Organisation ueberhaupt registrierungspflichtig ist (§ 2 LobbyRG).
- Sie stehen am Anfang eines neuen Lobbyregister-Mandats und suchen den richtigen Einstiegspunkt.
- Sie wollen verstehen, welcher der 50 Skills für Ihre aktuelle Fragestellung zuständig ist.
- Sie haben eine Frist (unverzuegliche Aktualisierung, Quartalsfrist, Jahresbestaetigung) und muessen schnell handeln.
- Sie sind Public-Affairs-Agentur oder Kanzlei und verwalten mehrere Mandate gleichzeitig.

## Fachbegriffe (kurz erklaert)

- **LobbyRG** — Lobbyregistergesetz; Bundesgesetz, das Interessenvertreter verpflichtet, sich beim Deutschen Bundestag zu registrieren.
- **Interessenvertretung** — Jede Kontaktaufnahme zur unmittelbaren oder mittelbaren Einflussnahme auf Willensbildungs- oder Entscheidungsprozesse nach § 1 LobbyRG.
- **Registrierungspflicht** — Besteht bei regelmäßiger, auf Dauer angelegter oder geschaeftsmäßiger Interessenvertretung oder mehr als 30 Kontakten in drei Monaten (§ 2 Abs. 1 LobbyRG).
- **Registerfuehrende Stelle (RfS)** — Die Verwaltung des Deutschen Bundestags; sie prueft Eintraege, fuehrt Bussgeldverfahren durch und ist Ansprechpartnerin bei Korrekturen.
- **Verhaltenskodex** — Verpflichtende Selbstverpflichtung nach § 5 LobbyRG zu Offenheit, Transparenz und Integritaet bei jedem Kontakt mit Adressaten.
- **Drehtuer** — Regelung, die frueheres Amt oder Mandat in Bundestag oder Bundesregierung offenzulegen verlangt (§ 3 LobbyRG).
- **Finanzielle Aufwendungen** — Alle Personal- und Sachkosten im Bereich Interessenvertretung; Angabepflicht in Bandbreiten nach § 3 LobbyRG.
- **Hausausweis** — Tagesausweis für Bundestagsgebaeude; nach § 6 LobbyRG nur für registrierte Interessenvertreter zugaenglich.

## Rechtsgrundlagen

- § 1 LobbyRG — Begriff der Interessenvertretung und Adressatenkreis.
- § 2 LobbyRG — Registrierungspflicht und Ausnahmen.
- § 3 LobbyRG — Pflichtinhalt des Registereintrags.
- § 4 LobbyRG — Registerführung, öffentliche/nicht öffentliche Inhalte, Jahresbestätigung und Bestätigungsvermerk.
- § 5 LobbyRG — Verhaltenskodex.
- § 6 LobbyRG — Rechtsfolgen der Registrierung (Hausausweis, Anhörungen).
- § 7 LobbyRG — Bussgeldtatbestaende und Sanktionen.

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Unternehmenstyp, Kontaktplaene, Auftraggeber, bestehender Portaleintrag oder Erstregistrierung.
2. Registrierungspflicht pruefen: Skill `registrierungspflicht-schwellen` und `interessenvertretung-begriff` verwenden.
3. Falls Ausnahme moeglich: `ausnahmen-bundestag` oder `ausnahmen-bundesregierung` pruefen.
4. Passendes Themen-Cluster auswaehlen (siehe Skill-Tour unten).
5. Eilfristen beachten: unverzuegliche Aktualisierung oder Quartalsfrist via `fristen-und-quartalsmonitor`.

## Skill-Tour (was gibt es hier?)

**Pflicht und Abgrenzung**

- `registrierungspflicht-schwellen` — Prueft § 2 Abs. 1 LobbyRG: Schwellen für Registrierungspflicht (regelmaessig, auf Dauer, 30-Kontakte-Regel).
- `interessenvertretung-Begriff` — Klaert, ob ein Kontakt ueberhaupt Interessenvertretung nach § 1 LobbyRG ist.
- `ausnahmen-bundestag` — Prueft Ausnahmen von der Registrierungspflicht gegenueber Bundestagsadressaten.
- `ausnahmen-bundesregierung` — Prueft Ausnahmen gegenueber Bundesregierung und Ministerien.
- `freiwillige-registrierung` — Beraet zu Rechten und Pflichten bei freiwilliger Eintragung nach § 2 Abs. 5 LobbyRG.
- `adressatenkreis-bundestag-bundesregierung` — Kartiert, wer Adressat nach § 1 LobbyRG ist.

**Erstregistrierung und Portalworkflow**

- `lobbyregister-intake-mandat` — Strukturiertes Erstgespraech vor jeder Lobbyregister-Pruefung.
- `lobbyregister-kommandocenter` — Master-Routing für alle Lobbyregister-Mandate.
- `end-to-end-registrierungswizard` — Gefuehrter Gesamtfür die komplette Registrierungsmappe.
- `erstregistrierung-ausfuellen` — Schritt-für-Schritt durch den Portal-Ersteintrag.
- `portal-account-rollen` — Plant Administrationskonto, Rollen und Zugriffsschutz.
- `personen-organisationstyp` — Bestimmt, welcher Organisationstyp einzutragen ist.
- `bestaetigungsdokument-freigabe` — Unterzeichner, Leitungsperson und Freigabe vor Eintragung.
- `registereintrag-finalcheck` — Prueft vor Freigabe Vollstaendigkeit, Richtigkeit und Aktualitaet.

**Stammdaten und Inhalt**

- `taetigkeitsbeschreibung` — Formuliert die allgemeine Taetigkeitsbeschreibung der Interessenvertretung.
- `interessen-und-vorhabenbereiche` — Ordnet Interessen- und Vorhabenbereiche zu.
- `regelungsvorhaben-erfassen` — Erfasst konkrete Regelungsvorhaben für den Eintrag.
- `betraute-personen` — Ermittelt Personen, die mit Interessenvertretung betraut sind.
- `vertretungsberechtigte-personen` — Ermittelt gesetzliche Vertretungen und Zeichnungsberechtigte.
- `mitgliedschaften-mitgliederzahl` — Erfasst Mitgliederzahl und relevante Mitgliedschaften.
- `hauptstadtrepraesentanz` — Prueft, ob eine Berliner Geschaeftsstelle anzugeben ist.

**Finanzdaten**

- `finanzaufwendungen-berechnen` — Berechnet finanzielle Aufwendungen nach § 3 LobbyRG.
- `hauptfinanzierungsquellen` — Strukturiert Hauptfinanzierungsquellen und grenzt Einnahmearten ab.
- `öffentliche-zuwendungen` — Prueft Zuwendungen der öffentlichen Hand mit Schwellenwerten.
- `schenkungen-sponsoring` — Prueft Schenkungen und Zuwendungen Dritter.
- `jahresabschluss-rechenschaftsbericht` — Prueft Bereitstellungspflicht für Jahresabschluss oder Rechenschaftsbericht.

**Spezialkonstellationen**

- `auftraggeber-ermitteln` — Erfasst Auftraggeber bei Interessenvertretung für Dritte.
- `fremdmandat-agenturfall` — Spezialfür Public-Affairs-Agenturen mit mehreren Mandanten.
- `konzern-netzwerk-plattform` — Lobbyregisterfragen bei Konzernen, Verbaenden, Netzwerken.
- `unterauftragnehmer-erfassen` — Prueft Unterauftragsverhaeltnisse und eingesetzte Personen.
- `drehtuer-angaben` — Fuehrt durch Angaben zu frueherem Amt oder Mandat in Politik und Verwaltung.
- `anonymisierung-schutzantrag` — Prueft Beschraenkung der Veroeffentlichung bei schutzwuerdigen Interessen.
- `datenschutz-nichtöffentliche-angaben` — Ordnet öffentliche und nicht öffentliche Angaben.

**Aktualisierung und Fristen**

- `aktualisierung-unverzueglich` — Steuert unverzuegliche Updates bei Stammdaten und Personenaenderungen.
- `geschaeftsjahresaktualisierung` — Jaehrliche vollstaendige Ueberpruefung und Bestaetigung.
- `fristen-und-quartalsmonitor` — Baut Fristenkalender für alle Updatepflichten und Nachholfristen.
- `nicht-aktualisiert-risiko` — Prueft Kennzeichnung nicht aktualisiert und Rettungsplan.

**Stellungnahmen und Gutachten**

- `stellungnahmen-gutachten-upload` — Prueft Bereitstellungspflicht und Quartalsfrist für Stellungnahmen.

**Verhaltenskodex und Compliance**

- `verhaltenskodex-integritaet` — Operationalisiert Offenheit, Transparenz und Integritaet nach § 5 LobbyRG.
- `erstkontakt-offenlegung` — Formuliert Offenlegung beim erstmaligen Kontakt mit Adressaten.
- `hausausweis-und-anhoerung` — Prueft Auswirkungen des Registerstatus auf Tagesausweis und Anhörungen.
- `interne-lobbyregister-richtlinie` — Erstellt interne Richtlinie für Rollen, Meldewege und Schulung.
- `visitenkarte-und-nachweise` — Nutzt Registerauszug und interne Nachweise für Compliance-Akte.

**Sanktionen und Meldungen**

- `bussgeld-und-pruefverfahren` — Reaktionsbei RfS-Pruefung, Anhörung und Bussgeldrisiko.
- `verstoesse-melden` — Fuehrt durch Meldung moeglicher Verstoesse an die registerfuehrende Stelle.
- `registerfuehrende-stelle-kontakt` — Bereitet Anfragen an die RfS und Korrekturen vor.

**Monitoring und Dokumentation**

- `benachrichtigungskonto-monitor` — Richtet Beobachtung von Registereintraegen und Entwicklungen ein.
- `suche-open-data-monitor` — Nutzt Suche und Open-Data-API für Compliance- und Gegenpruefung.
- `dokumentationsakte-revisionsspur` — Baut Aktenstruktur für Belege, Freigaben und Portal-Screenshots.

**Beendigung und Archivierung**

- `fruehere-interessenvertretung-exit` — Fuehrt durch Anzeige, dass keine Pflicht mehr besteht, und Archivierung.

## Worauf besonders achten

- **Unverzueglichkeitspflicht** — Jede wesentliche Aenderung (Personen, Taetigkeitsbeschreibung, Auftraggeber) muss ohne schuldhaftes Zoegern im Portal aktualisiert werden; Versaeumnisse erzeugen Bussgeldrisiko nach § 7 LobbyRG.
- **Ausnahmepruefung zuerst** — Viele Kanzleien und Beratungen gehen reflexartig von Registrierungspflicht aus; eine sorgfaeltige Ausnahmepruefung nach § 2 Abs. 2 und 3 LobbyRG spart Aufwand.
- **Irrefuehrungs-Verbot** — Eintraege muessen pruefbar und nicht irrefuehrend formuliert sein; zu allgemeine Taetigkeitsbeschreibungen koennen als Verschleierung gewertet werden.
- **Agenturfall trennen** — Bei Fremdmandaten muessen Auftraggeber und die jeweils beauftragte Interessenvertretung klar getrennt sein; das Vermischen von Mandaten im selben Eintrag ist ein klassischer Fehler.
- **Bereitstellung Stellungnahmen** — Grundlegende Stellungnahmen oder Gutachten zu Regelungsvorhaben sind nach § 3 LobbyRG registertauglich bereitzustellen; Frist und Portalpraxis vor Ausgabe live prüfen.

## Typische Fehler

- Kontakte, die tatsaechlich Serviceanfragen oder rein lokale Anliegen sind, werden faelschlicherweise als registrierungspflichtige Interessenvertretung behandelt.
- Die Drehtuer-Angaben werden vergessen oder zu eng ausgelegt (nur letzter Job statt alle relevanten fuenf Jahre).
- Schutzantraege werden nicht gestellt, obwohl schutzwuerdige Interessen von Personen vorliegen.
- Finanzdaten werden ohne Pruefung der aktuellen Schwellenwerte und Bandbreiten eingetragen.
- Portal-Konten werden ohne Zwei-Personen-Freigabeprozess betrieben, was bei Personalwechseln zu Kontrollverlust fuehrt.

## Querverweise

- `insolvenzrecht` — Wenn Auftraggeber insolvent ist und Mandatsbasis wegfaellt.
- `kartellrecht-marktabgrenzung-pruefung` — Wenn Interessenvertretung zu laufenden Kartellverfahren erfolgt.
- `europarecht-kompass` — Bei Interessenvertretung gegenueber EU-Institutionen (kein LobbyRG, aber EU-Transparenzregister).
- `bereicherungs-und-anfechtungsrecht-pruefer` — Bei Rueckabwicklung von Vergutungen aus Lobbymandat.

## Quellen und Aktualitaet

- Stand: 05/2026
- Lobbyregistergesetz (LobbyRG) in der Fassung nach dem Aenderungsgesetz vom 15.01.2024 (in Kraft 01.03.2024). Wesentliche Neuerungen: Adressatenkreis ab Referatsleiterebene; konkrete Angabe der Regelungsvorhaben und betroffenen Bereiche; Upload-Pflicht für Stellungnahmen und Gutachten von grundsaetzlicher Bedeutung; Uebergangsfrist Bestandseintraege 01.03.2024 bis 30.06.2024.
- Konsolidierte Fassung LobbyRG 2024: https://www.bundestag.de/resource/blob/991838/Konsolidierte-Fassung-LobbyRG-2024.pdf
- Handbuch der registerfuehrenden Stelle des Deutschen Bundestags
- Bundestag Hinweise zur Rechtslage ab 01.03.2024: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-zur-neuen-rechtslage-ab-dem-1-maerz-2024-955618
- Lobbyregister-Portal: https://www.lobbyregister.bundestag.de

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
