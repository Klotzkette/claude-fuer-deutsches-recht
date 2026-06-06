---
name: br-ki-vertragspruefung-brki-rollout-chronologie
description: "Einstieg, Schnelltriage und Fallrouting im Berufsrecht KI Vertragspruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage im Berufsrecht KI-Vertragsprüfung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Berufsrecht KI-Vertragspruefung — Allgemein

## Arbeitsbereich

Einstieg, Schnelltriage und Fallrouting im Berufsrecht KI Vertragspruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 43e BRAO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Berufsrecht KI Vertragspruefung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Berufsrechtliche und strafrechtliche Vorprüfung von Verträgen mit privaten Legal-AI-Anbietern. Für Rechtsanwälte Steuerberater Wirtschaftsprüfer Patentanwälte Notare. §§ 43e BRAO 62a StBerG 50a WPO 39c PAO 26a BNotO § 203 StGB. Maßstab sind Gesetz, Gesetzesmaterialien, verifizierbare Kammerpraxis, Rechtsprechung und aktueller Debattenstand. Gutachten Rückfragebrief Klauselvorschläge.

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
| `avv-grenzpruefung-datenschutz` | Kanzlei nutzt KI-Dienstleister und prüft ob AVV nach Art. 28 DSGVO die berufsrechtliche Prüfung ersetzt. Berufsrecht laeuft parallel und ist strenger als Datenschutzrecht. Normen Art. 28 DSGVO §§ 43e BRAO 62a StBerG.… |
| `berufsrecht-ki-vertragspruefung-kaltstart-interview` | Erfasse Beruf des Auftraggebers (Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar) Anbieter Produktname Vertragsdokument Datenarten Verarbeitungszweck Hostingland und Subunternehmerstruktur. Bilde daraus… |
| `cloud-act-und-drittstaat-pruefen` | Prüfe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). EU/EWR werden als gleichwertig unterstellt. Drittstaaten benoetigen vergleichbares… |
| `erforderlichkeit-dokumentieren` | Prüfe die Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenüber dem KI-Dienstleister nach Absatz eins der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). Bezugspunkt ist nach… |
| `gutachten-erstellen` | Erstelle das zusammenfassende Vorprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat… |
| `klauselvorschlaege` | Liefere konkrete Mustertexte für Vertragsklauseln mit dem KI-Anbieter. Bausteine Verschwiegenheit Belehrung §§ 203 204 StGB Subunternehmer no training Zero-Retention EU-Hosting Audit-Recht Löschkonzept Professional… |
| `parallelnormen-andere-berufe` | Norm-Adapter-Referenz für alle fuenf Berufsgeheimnistraeger Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar. Mapping der Dienstleisterregelungen Verschwiegenheitspflichten und § 203 StGB-Tatbestaende.… |
| `rueckfragebrief-an-anbieter` | Erstelle einen strukturierten Rückfragebrief an den KI-Anbieter zur Klaerung der berufsrechtlichen und strafrechtlichen Pflichten. Aufbau Anschreiben Kontext drei Fragenbloecke (Verschwiegenheit Subunternehmer TOM und… |
| `strafprozessuale-regelung-pruefen` | Prüfe die strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO. Zeugnisverweigerungsrecht der mitwirkenden Personen Beschlagnahmeverbot für Mandatsdaten Widerspruchspflicht des Dienstleisters bei… |
| `strafrechtliche-belehrung-pruefen` | Prüfe die strafrechtliche Belehrung des Dienstleisters nach Absatz drei Satz zwei Nummer eins der einschlaegigen Dienstleisterregelung. Pflichtinhalte § 203 Absatz eins drei vier und sechs StGB und § 204 StGB.… |
| `subunternehmer-regelung-pruefen` | Prüfe die Subunternehmerklausel im KI-Anbietervertrag. Norm Absatz drei Satz zwei Nummer drei der einschlaegigen Dienstleisterregelung. Pflichtinhalte Zustimmungsvorbehalt der Kanzlei Subunternehmerliste… |
| `tom-und-zertifizierungen-pruefen` | Prüfe technische und organisatorische Massnahmen des KI-Anbieters und seine Zertifizierungen. Maßstab Art. 32 DS-GVO ISO 27001 BSI C5 (Cloud Computing Compliance Criteria Catalogue) SOC zwei Typ zwei TISAX. Zentral für… |
| `verschwiegenheitsklausel-pruefen` | Prüfe die vertragliche Verpflichtung des Dienstleisters auf Verschwiegenheit nach Absatz drei der einschlaegigen Dienstleisterregelung (§§ 43e BRAO 62a StBerG 50a WPO 39c PAO 26a BNotO). Anforderungen Textform (§ 126b… |

## Worum geht es?

Dieses Plugin unterstuetzt Anwälte, Steuerberater, Wirtschaftsprüfer, Patentanwälte und Notare bei der berufsrechtlichen und strafrechtlichen Pruefung von Verträgen mit privaten Legal-AI-Anbietern. Der Einsatz von KI-Diensten in Kanzleien unterliegt strengen berufsrechtlichen Vorgaben, insbesondere den Verschwiegenheitspflichten und den gesetzlichen Dienstleister-Regelungen der jeweiligen Berufsordnung.

Kernproblem ist das Spannungsfeld zwischen dem Wunsch nach KI-Effizienzgewinnen und der Pflicht, Mandatsdaten vor unberechtigtem Zugriff zu schuetzen. § 203 StGB stellt die unbefugte Offenbarung von Berufsgeheimnissen unter Strafe; die berufsrechtlichen Normen verpflichten Kanzleien, Dienstleister explizit zu belehren und vertraglich auf Verschwiegenheit zu verpflichten.

## Wann brauchen Sie diese Skill?

- Sie prufen erstmals einen Vertrag mit einem KI-Anbieter und benoetigen einen strukturierten Pruefrahmen fuer Ihren Berufsstand.
- Ein KI-Dienstleister hat seinen Server in den USA und Sie wollen pruefen, ob der US CLOUD Act oder FISA ein Risiko darstellt.
- Sie moechten einen Rueckfragebrief an den Anbieter schreiben, um fehlende Vertragsklauseln zu Verschwiegenheit, Subunternehmern und Datenloeschung nachzufordern.
- Sie sollen ein zusammenfassendes Gutachten fuer die Kanzleifuehrung erstellen, bevor ein KI-Tool eingefuehrt wird.
- Ihr Kanzleiteam nutzt bereits ein KI-Tool und Sie wollen rueckwirkend pruefen, ob alle berufsrechtlichen Anforderungen erfuellt sind.

## Fachbegriffe (kurz erklaert)

- **§ 203 StGB** — Strafvorschrift zum Schutz von Privatgeheimnissen; erfasst Berufsgeheimnisraeger wie Anwälte, Aerzte und Steuerberater.
- **Dienstleister-Regelung** — Berufsgruppenspezifische Norm (z. B. § 43e BRAO), die Kanzleien verpflichtet, KI-Anbieter auf Verschwiegenheit zu verpflichten und zu belehren.
- **AVV** — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO; laeuft parallel zur berufsrechtlichen Pruefung, ersetzt diese aber nicht.
- **No-Training-Klausel** — Vertragliche Zusage des Anbieters, Mandatsdaten nicht zum Trainieren von KI-Modellen zu verwenden.
- **Zero-Retention** — Zusage, Daten nicht dauerhaft zu speichern; relevant fuer Loeschkonzept und Audit-Rechte.
- **Cloud Act** — US-amerikanisches Gesetz, das US-Behoerden Zugriff auf bei US-Unternehmen gespeicherte Daten ermoeglichen kann, auch wenn Server in der EU stehen.
- **BSI C5** — Cloud Computing Compliance Criteria Catalogue des Bundesamts fuer Sicherheit in der Informationstechnik; anerkannter Pruefstandard.
- **Norm-Adapter** — Mechanismus im Plugin, der je nach Berufsstand (BRAO, StBerG, WPO, PAO, BNotO) die einschlaegige Dienstleisterregelung auswaehlt.

## Rechtsgrundlagen

- § 43e BRAO — Rechtsanwalt: Inanspruchnahme von Dienstleistern
- § 62a StBerG — Steuerberater: Inanspruchnahme von Dienstleistern
- § 50a WPO — Wirtschaftsprüfer: Inanspruchnahme von Dienstleistern
- § 39c PAO — Patentanwalt: Inanspruchnahme von Dienstleistern
- § 26a BNotO — Notar: Inanspruchnahme von Dienstleistern
- § 203 Abs. 1 Abs. 3 Abs. 4 und Abs. 6 StGB — Verletzung von Privatgeheimnissen
- § 204 StGB — Verwertung fremder Geheimnisse
- Art. 28 DSGVO — Auftragsverarbeitung
- Art. 32 DSGVO — Technisch-organisatorische Massnahmen
- §§ 53a 97 StPO — Zeugnisverweigerungsrecht und Beschlagnahmeverbot

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Berufsstand und Anbieter im Kaltstart-Interview erfassen; Norm-Adapter bestimmen.
2. Erforderlichkeit der Offenlegung von Mandatsdaten pruefen und dokumentieren.
3. Verschwiegenheitsklausel im Vertrag lokalisieren und bewerten.
4. Subunternehmer-Regelung, strafrechtliche Belehrung und TOM pruefen.
5. Drittstaat-Risiko (US CLOUD Act, Nicht-EU-Hosting) einschaetzen; ggf. Rueckfragebrief versenden und Gutachten erstellen.

## Skill-Tour (was gibt es hier?)

- `avv-grenzpruefung-datenschutz` — Pruefen ob AVV nach Art. 28 DSGVO die berufsrechtliche Pruefung ersetzt (tut er nicht).
- `berufsrecht-ki-vertragspruefung-kaltstart-interview` — Berufsstand, Anbieter, Vertragsdokument und Normen erfassen; Norm-Adapter aktivieren.
- `cloud-act-und-drittstaat-pruefen` — Auslandsbezug und Drittstaatrisiko (US CLOUD Act, FISA) pruefen; Professional Secrecy Addendum empfehlen.
- `erforderlichkeit-dokumentieren` — Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenueber dem KI-Dienstleister pruefen und dokumentieren.
- `gutachten-erstellen` — Zusammenfassendes Berufsrechts-Gutachten zum KI-Anbietervertrag erstellen.
- `klauselvorschlaege` — Mustertexte fuer Vertragsklauseln zu Verschwiegenheit, No-Training, Zero-Retention und Subunternehmern liefern.
- `parallelnormen-andere-berufe` — Norm-Adapter-Referenz fuer alle fuenf Berufsgeheimnistraeger mit Mapping der Dienstleisterregelungen.
- `rueckfragebrief-an-anbieter` — Strukturierten Rueckfragebrief an den KI-Anbieter zu offenen berufsrechtlichen Punkten erstellen.
- `strafprozessuale-regelung-pruefen` — Strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO pruefen.
- `strafrechtliche-belehrung-pruefen` — Belehrung des Dienstleisters ueber § 203 StGB im Vertrag pruefen.
- `subunternehmer-regelung-pruefen` — Subunternehmerklausel auf Zustimmungsvorbehalt, Weiterverpflichtung und Belehrung pruefen.
- `tom-und-zertifizierungen-pruefen` — TOM und Zertifizierungen des Anbieters (ISO 27001, BSI C5, SOC 2) pruefen.
- `verschwiegenheitsklausel-pruefen` — Vertragliche Verpflichtung des Dienstleisters auf Verschwiegenheit lokalisieren und bewerten.

## Worauf besonders achten

- **Berufsrecht und Datenschutzrecht laufen parallel**: Ein vorhandener AVV erfuellt nicht automatisch die berufsrechtlichen Anforderungen nach § 43e BRAO und den Parallelvorschriften.
- **Textformerfordernis**: Die Verschwiegenheitspflicht muss nach § 43e Abs. 3 BRAO in Textform (§ 126b BGB) vereinbart werden; muendliche Zusagen genuegen nicht.
- **Subunternehmer oft uebersehen**: Viele KI-Anbieter nutzen Sprachmodelle grosser US-Konzerne als Subunternehmer; diese muessen ebenfalls verpflichtet werden.
- **Drittstaatrisiko eigenstaendig bewerten**: EU-Sitz des Anbieters genuegt nicht, wenn Muttergesellschaft in den USA dem Cloud Act unterliegt.
- **Strafrechtliche Konsequenzen**: Ein Verstoss gegen § 203 StGB ist eine Straftat, keine Ordnungswidrigkeit.

## Typische Fehler

- Nur den AVV pruefen und berufsrechtliche Parallelvorschriften uebersehen.
- Subunternehmerliste nicht anfordern; Anbieter setzt grosse Sprachmodelle ein, ohne dies offenzulegen.
- Vertrag ohne No-Training-Zusage annehmen; Mandatsdaten koennen in KI-Training einfliessen.
- Erforderlichkeit der Datenweitergabe nicht dokumentieren; interner Compliance-Vermerk fehlt.
- US-Anbieter mit EU-Rechenzentrum als unbedenklich eingestuft, ohne Cloud-Act-Analyse.

## Querverweise

- `ki-richtlinie-kanzleien` — KI-Nutzungsrichtlinie als Rahmen, der die Ergebnisse der Vertragspruefung umsetzt.
- `kanzlei-builder-hub` — Verwaltet und installiert Skills, die ihrerseits KI-Dienste nutzen koennen.
- `kanzlei-allgemein` — Kanzlei-Workflow-Plugin, fuer das KI-Dienste berufsrechtskonform eingebunden werden muessen.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- aktueller berufsrechtlicher Debattenstand zur Einordnung von KI-Tools
- BRAK-Hinweise 12/2024

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
