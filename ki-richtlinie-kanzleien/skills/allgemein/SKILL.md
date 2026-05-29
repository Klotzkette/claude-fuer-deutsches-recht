---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im KI Richtlinie Kanzleien-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Spezial-Skills oder stellt genau eine gezielte Rückfrage."
---

<!-- konvers-stil-v1 -->

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Spezial-Skills dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# KI-Richtlinie fuer Kanzleien und Rechtsabteilungen — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **KI Richtlinie Kanzleien**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Erstellt und pflegt eine berufsrechtskonforme KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen mit Anwaelten und Syndikus-Anwaelten. Beruht auf BRAO, BORA, DSGVO, KI-Verordnung sowie BRAK- und DAV-Hinweisen.

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
| `anonymisierung-pseudonymisierung` | Anonymisierung und Pseudonymisierung von Mandatsdaten vor KI-Eingabe: Anwendungsfall Anwalt will Mandatsdokument in KI-System eingeben und muss Namen Adressen Aktenzeichen und Identifikatoren schützen. Art. 4 Nr. 5… |
| `auftragsverarbeitungsvertrag-pruefen` | Auftragsverarbeitungsvertrag nach Art. 28 DSGVO bei KI-Anbietern prüfen: Anwendungsfall Kanzlei schließt Vertrag mit KI-Dienstleister und muss AVV auf DSGVO-Konformität prüfen. Art. 28 DSGVO AVV-Pflicht, § 43e BRAO… |
| `automatisierte-entscheidungen-art-22-dsgvo` | Automatisierte Einzelentscheidungen nach Art. 22 DSGVO in Kanzleien prüfen: Anwendungsfall Kanzlei plant KI-gestützte Mandatszuordnung Honorarberechnung oder Bonitätsprüfung und muss prüfen ob automatisierte… |
| `berufsrecht-bausteine` | Berufsrechtliche Textbausteine für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei erstellt KI-Richtlinie und braucht praezise Bausteine zu Verschwiegenheit Sorgfaltspflicht und Eigenverantwortung. § 43… |
| `bias-und-diskriminierung-pruefung` | Bias und Diskriminierung in KI-Outputs für Kanzleien prüfen: Anwendungsfall Kanzlei nutzt KI-System bei Personalentscheidungen Mandantenberatung oder Rechercheaufgaben und muss sicherstellen dass keine… |
| `compliance-regelsatz-erstellen` | Compliance-Regelsatz Zehn Gebote für KI-Einsatz in Kanzleien erstellen: Anwendungsfall Kanzlei benoetigt praegnante Verhaltensregeln für alle Mitarbeitenden zu erlaubten und verbotenen KI-Nutzungen. § 43a BRAO… |
| `dienstleister-due-diligence` | KI-Dienstleister Due Diligence für Kanzleien durchführen: Anwendungsfall Kanzlei moechte neuen KI-Dienst beauftragen und muss eigenverantwortlich Datenschutz Berufsrecht und Sicherheit prüfen. § 43e BRAO… |
| `dokumentationspflichten-protokoll` | Dokumentationspflichten und beweissichere Protokollierung von KI-Nutzung in Kanzleien: Anwendungsfall Kanzlei muss KI-Inputs und KI-Outputs nachvollziehbar dokumentieren für Datenschutzbehörden, Mandanten-Beschwerden… |
| `dsgvo-compliance-bausteine` | DSGVO-Textbausteine für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei erstellt oder aktualisiert KI-Richtlinie und benoetigt prazise datenschutzrechtliche Formulierungen. Art. 2 Abs. 1 DSGVO… |
| `executive-summary-bausteine` | Executive Summary der KI-Nutzungsrichtlinie für Kanzleien erstellen: Anwendungsfall Kanzleiführung will Mitarbeitenden die wichtigsten Kernpunkte in kurzem Executive Summary vermitteln. § 43a BRAO Verschwiegenheit, §… |
| `geschgehg-bausteine` | GeschGehG-Bausteine für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei muss beim KI-Einsatz Geschäftsgeheimnisse von Mandanten und eigene Kanzleiinformationen schützen. § 1 Abs. 3 Nr. 1 GeschGehG… |
| `halluzinations-handhabung` | Halluzinationen von KI in juristischer Arbeit erkennen und Prozessbetrug vermeiden: Anwendungsfall Anwalt nutzt KI für Rechtsprechungs-Recherche und muss sicherstellen dass keine falschen Fundstellen in Schriftsatz… |
| `kanzlei-kontext-analyse` | Kanzlei-Kontext erfassen für massgeschneiderte KI-Nutzungsrichtlinie: Anwendungsfall vor Erstellung einer KI-Richtlinie muss Groesse Rechtsgebiete Mandantenstruktur IT-Infrastruktur und Syndikus-Inhouse-Besonderheiten… |
| `kennzeichnungspflichten-veroeffentlichungen` | Kennzeichnungspflichten für KI-generierte Inhalte in Kanzlei-Veröffentlichungen prüfen: Anwendungsfall Kanzlei veröffentlicht KI-unterstuetzte Artikel Blog-Posts Pressemitteilungen oder Mandantenbriefe und muss… |
| `ki-kompetenz-erwerb-plan` | KI-Kompetenz-Schulungsplan für Kanzleien nach Art. 4 KI-VO erstellen: Anwendungsfall Kanzlei muss seit 2. Februar 2025 sicherstellen dass Personal ausreichend KI-Kompetenz hat. Art. 4 KI-VO KI-Kompetenz-Pflicht… |
| `ki-vo-betreiber-pflichten` | KI-VO Betreiber-Pflichten für Kanzleien erlaeutern und umsetzen: Anwendungsfall Kanzlei als Betreiber von KI-Diensten muss Pflichten nach EU AI Act kennen und in Richtlinie umsetzen. Art. 3 Nr. 4 KI-VO… |
| `ki-vo-hochrisiko-personalwesen` | KI-VO Hochrisiko-Anforderungen für Personalwesen in Kanzleien ab August 2026: Anwendungsfall Kanzlei setzt KI im HR-Bereich ein oder beraet Mandanten zum AGG-konformen KI-Einsatz bei Bewerberauswahl. Anhang III Nr. 4… |
| `literatur-und-quellen` | Pflicht-Literatur und Aktualisierungsliste für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei will Richtlinie auf dem neuesten Stand halten und benoetigt strukturierte Quellenübersicht. BRAK-Hinweise… |
| `musterklauseln-it-vertrag` | Musterklauseln für IT-Vertraege mit KI-Dienstleistern in Kanzleien: Anwendungsfall Kanzlei verhandelt Vertrag mit KI-Anbieter und braucht Klauseln zu Verschwiegenheit Training-Opt-out Löschpflichten und Haftung. § 43e… |
| `prompting-leitfaden` | Prompting-Leitfaden für juristische KI-Nutzung in Kanzleien: Anwendungsfall Anwalt oder Mitarbeitende wollen KI effektiver nutzen und benoetigen praxiserprobte Prompt-Methoden. Mandantenkommunikation mit KI,… |
| `rdg-pruefung-chatbot` | RDG-Prüfung ob KI-Chatbot unerlaubte Rechtsdienstleistung erbringt: Anwendungsfall Kanzlei betreibt oder beraet Mandanten bei KI-Chatbot-Service und muss prüfen ob Chatbot-Output als Rechtsdienstleistung nach RDG… |
| `richtlinien-skelett-erzeugen` | KI-Nutzungsrichtlinie Skelett für Kanzleien erzeugen: Anwendungsfall Kanzlei will erstmals KI-Nutzungsrichtlinie erstellen und benoetigt vollständige Grundstruktur. § 43a BRAO Verschwiegenheit, § 43e BRAO… |
| `richtlinien-update-zyklus` | KI-Nutzungsrichtlinie regelmäßig prüfen und aktualisieren: Anwendungsfall bestehende KI-Richtlinie ist aelter als sechs Monate oder es gibt wesentliche neue Rechtsentwicklung. Art. 4 KI-VO KI-Kompetenz, KI-VO… |
| `schatten-ki-aufdeckung` | Schatten-KI in Kanzleien erkennen und konstruktiv umgehen: Anwendungsfall Kanzleiführung vermutet oder stellt fest dass Mitarbeitende nicht autorisierte KI-Dienste mit privaten Accounts nutzen. § 43a BRAO… |
| `transparenz-mandanten` | Transparenz gegenüber Mandanten bei KI-Einsatz in Kanzleien sicherstellen: Anwendungsfall Kanzlei muss Mandaten informieren dass KI-Systeme bei Mandatsbearbeitung eingesetzt werden. Art. 6 Abs. 1 lit. a DSGVO… |
| `urheberrecht-bausteine` | Urheberrechtliche Bausteine für KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei will wissen ob KI-generierte Texte urheberrechtlich schützbar sind und welche Texte als Eingabe hochgeladen werden duerfen. §… |

## Worum geht es?

Das Plugin unterstuetzt Kanzleien und Rechtsabteilungen bei der Erstellung, Anpassung und regelmaessigen Aktualisierung einer berufsrechtskonformen KI-Nutzungsrichtlinie. Eine solche Richtlinie ist seit Inkrafttreten der KI-Kompetenz-Pflicht nach Art. 4 KI-VO (2. Februar 2025) und angesichts zunehmender KI-Nutzung in anwaltlichen Workflows keine Kuer mehr, sondern ein berufsrechtliches Erfordernis.

Das Plugin verbindet DSGVO-Anforderungen, berufsrechtliche Vorgaben aus BRAO und BORA, die neuen Pflichten aus dem EU AI Act sowie die aktuellen Hinweise von BRAK und DAV zu einer praxistauglichen Richtlinienstruktur. Es richtet sich an Kanzleiinhaber, Compliance-Verantwortliche und Datenschutzbeauftragte.

## Wann brauchen Sie diese Skill?

- Sie wollen erstmals eine KI-Nutzungsrichtlinie fuer Ihre Kanzlei oder Rechtsabteilung erstellen.
- Ihre bestehende Richtlinie ist aelter als sechs Monate und Sie wollen sie auf den aktuellen Rechtsstand bringen.
- Sie haben einen neuen KI-Dienstleister vertraglich gebunden und muessen die Richtlinie anpassen.
- Mitarbeitende nutzen offenbar nicht genehmigte KI-Dienste (Schatten-KI) und Sie wollen dagegen steuern.
- Sie beraten einen Mandanten beim Aufbau seiner eigenen Kanzlei oder Rechtsabteilung und brauchen eine Richtlinienvorlage.

## Fachbegriffe (kurz erklaert)

- **KI-Verordnung (EU AI Act)** — Verordnung (EU) 2024/1689; legt Pflichten fuer Anbieter und Betreiber von KI-Systemen fest.
- **Art. 4 KI-VO** — KI-Kompetenz-Pflicht: Betreiber von KI-Systemen muessen sicherstellen, dass ihr Personal ausreichend KI-Kompetenz hat (seit 2. Februar 2025).
- **Hochrisiko-KI** — KI-Systeme nach Anhang III KI-VO mit besonderen Anforderungen; z. B. KI in Personalentscheidungen.
- **Schatten-KI** — Nicht genehmigte KI-Dienste, die Mitarbeitende mit privaten Accounts nutzen; Verschwiegenheitsrisiko.
- **§ 43e BRAO** — Berufsrechtliche Dienstleisterregelung fuer Rechtsanwaelte; verpflichtet zur Sorgfalt bei IT-Diensten.
- **AVV** — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO; Pflicht bei KI-Dienstleistern, die personenbezogene Daten verarbeiten.
- **BRAK-Hinweise 12/2024** — Hinweise des Bundesrechtsanwaltskammer-Praesidiums zum KI-Einsatz in Kanzleien.
- **DAV-Stellungnahme 32/2025** — Stellungnahme des Deutschen Anwaltvereins zur berufsrechtlichen Einordnung von KI-Diensten.

## Rechtsgrundlagen

- § 43 BRAO — Allgemeine Berufspflichten; Sorgfalt und Gewissenhaftigkeit
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht
- § 43e BRAO — Inanspruchnahme von Dienstleistern
- § 203 StGB — Verletzung von Privatgeheimnissen; Berufsgeheimnis
- Art. 4 KI-VO — KI-Kompetenz-Pflicht
- Art. 6 KI-VO — Abgrenzung Hochrisiko-KI
- Art. 50 Abs. 4 KI-VO — Kennzeichnungspflicht fuer KI-generierte Inhalte
- Art. 22 DSGVO — Automatisierte Einzelentscheidungen
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag
- §§ 1 3 GeschGehG — Schutz von Geschaeftsgeheimnissen

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Kanzlei-Kontext analysieren: Groesse, Rechtsgebiete, bestehende Tools und Mandantenstruktur erfassen.
2. Richtlinien-Skelett erzeugen mit allen Pflichtbausteinen.
3. Bausteine berufsrechtlich, datenschutzrechtlich und nach KI-VO befuellen.
4. Executive Summary und Compliance-Regelsatz fuer Mitarbeitende erstellen.
5. Aktualisierungszyklus einrichten (mindestens alle sechs Monate oder bei wesentlicher Rechtsaenderung).

## Skill-Tour (was gibt es hier?)

- `anonymisierung-pseudonymisierung` — Mandatsdaten vor KI-Eingabe anonymisieren oder pseudonymisieren.
- `auftragsverarbeitungsvertrag-pruefen` — AVV bei KI-Anbietern auf DSGVO-Konformitaet pruefen.
- `automatisierte-entscheidungen-art-22-dsgvo` — Automatisierte Einzelentscheidungen nach Art. 22 DSGVO im Kanzleiumfeld pruefen.
- `berufsrecht-bausteine` — Berufsrechtliche Textbausteine (Verschwiegenheit, Sorgfalt, Eigenverantwortung) fuer KI-Richtlinien.
- `bias-und-diskriminierung-pruefung` — Bias und Diskriminierung in KI-Outputs fuer AGG-relevante Kanzleiprozesse pruefen.
- `compliance-regelsatz-erstellen` — Zehn-Gebote-Regelsatz fuer erlaubte und verbotene KI-Nutzungen erstellen.
- `dienstleister-due-diligence` — KI-Dienstleister-Due-Diligence: Datenschutz, Berufsrecht, Sicherheit und Zertifizierungen.
- `dokumentationspflichten-protokoll` — KI-Nutzung beweissicher protokollieren fuer Datenschutzbehoerden und Berufspruefungen.
- `dsgvo-compliance-bausteine` — DSGVO-Textbausteine fuer KI-Nutzungsrichtlinien: Rechtsgrundlagen, AVV, Drittlandtransfer.
- `executive-summary-bausteine` — Kurzes Executive Summary der KI-Richtlinie fuer Kanzleifuehrung und Mitarbeitende.
- `geschgehg-bausteine` — GeschGehG-Bausteine zum Schutz von Geschaeftsgeheimnissen beim KI-Einsatz.
- `halluzinations-handhabung` — Halluzinationen in KI-Outputs erkennen und Prozessbetrug durch falsche Fundstellen vermeiden.
- `kanzlei-kontext-analyse` — Kanzlei-Kontext fuer massgeschneiderte KI-Richtlinie erfassen und analysieren.
- `kennzeichnungspflichten-veroeffentlichungen` — Kennzeichnungspflichten fuer KI-generierte Inhalte in Kanzlei-Veroeffentlichungen pruefen.
- `ki-kompetenz-erwerb-plan` — KI-Kompetenz-Schulungsplan nach Art. 4 KI-VO erstellen und dokumentieren.
- `ki-vo-betreiber-pflichten` — KI-VO-Betreiber-Pflichten fuer Kanzleien erlaeutern und in Richtlinie umsetzen.
- `ki-vo-hochrisiko-personalwesen` — Hochrisiko-Anforderungen fuer KI im HR-Bereich ab August 2026 pruefen.
- `literatur-und-quellen` — Pflicht-Literatur und Aktualisierungsliste fuer KI-Nutzungsrichtlinien.
- `musterklauseln-it-vertrag` — Musterklauseln fuer IT-Vertraege mit KI-Dienstleistern (Verschwiegenheit, Training-Opt-out).
- `prompting-leitfaden` — Prompting-Leitfaden fuer juristische KI-Nutzung mit Vorlagen und Checkliste.
- `rdg-pruefung-chatbot` — RDG-Pruefung ob KI-Chatbot unerlaubte Rechtsdienstleistung erbringt.
- `richtlinien-skelett-erzeugen` — Vollstaendiges KI-Richtlinien-Skelett mit allen Pflichtbausteinen und Platzhaltern erzeugen.
- `richtlinien-update-zyklus` — KI-Nutzungsrichtlinie regelmaessig pruefen und aktualisieren mit Aenderungslog.
- `schatten-ki-aufdeckung` — Nicht autorisierte KI-Dienste erkennen und konstruktiv mit Mitarbeitenden umgehen.
- `transparenz-mandanten` — Transparenz gegenueber Mandanten bei KI-Einsatz sicherstellen: Mandatsvertragsklauseln.
- `urheberrecht-bausteine` — Urheberrechtliche Bausteine fuer KI-Richtlinien: Schutz und Upload-Verbote.

## Worauf besonders achten

- **Art. 4 KI-VO-Pflicht seit 2. Februar 2025**: Kanzleien als Betreiber von KI-Systemen muessen nachweisbare KI-Kompetenz sicherstellen; fehlende Schulungsnachweise sind ein Compliance-Risiko.
- **Schatten-KI ist das groesste Praxisproblem**: Viele Mitarbeitende nutzen private ChatGPT-Accounts; Mandatsdaten gelangen ohne AVV und ohne Belehrung an Drittanbieter.
- **DSGVO und Berufsrecht parallel pruefen**: Ein AVV reicht fuer die berufsrechtliche Konformitaet nach § 43e BRAO nicht aus.
- **Richtlinie mindestens alle sechs Monate aktualisieren**: KI-VO, BRAK-Stellungnahmen und neue Rechtsprechung aendern sich schnell.
- **Hochrisiko-Klassifizierung fuer HR-KI ab August 2026**: Kanzleien, die KI in Personalentscheidungen nutzen, muessen bis dahin Konformitaetsbewertungen abschliessen.

## Typische Fehler

- Richtlinie einmalig erstellen und nie aktualisieren; sie ist nach sechs Monaten veraltet.
- Executive Summary ohne Verbindlichkeit: Mitarbeitende sehen die Richtlinie als unverbindliche Empfehlung.
- Nur DSGVO-Anforderungen beachten, berufsrechtliche Anforderungen nach BRAO und StBerG ignorieren.
- Halluzinationspruefung nicht als Pflichtprozess in die Richtlinie aufnehmen; falsche Fundstellen in Schriftsaetzen sind ein Haftungsrisiko.
- Keine klaren Sanktionen fuer Verstoss gegen die Richtlinie definieren; Durchsetzungskraft fehlt.

## Querverweise

- `berufsrecht-ki-vertragspruefung` — Vertragspruefung fuer den einzelnen KI-Anbietervertrag.
- `kanzlei-builder-hub` — Verwaltet und prueft Skills, die KI-Dienste einsetzen.
- `kanzlei-allgemein` — Kanzlei-Workflow-Plugin, das unter der KI-Richtlinie betrieben wird.
- `rechtsberatungsstelle` — KI-Nutzung in der Beratungsstelle ebenfalls regelungspflichtig.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- KI-Verordnung (EU) 2024/1689, gueltig seit 2. August 2024; KI-Kompetenz-Pflicht seit 2. Februar 2025
- BRAK-Hinweise 12/2024
- DAV-Stellungnahme Nr. 32/2025
