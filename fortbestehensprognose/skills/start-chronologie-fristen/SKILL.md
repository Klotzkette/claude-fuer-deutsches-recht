---
name: start-chronologie-fristen
description: "Wenn es um Fortbestehensprognose — Allgemein in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste."
---

# Fortbestehensprognose — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: IDW S 11 12-Monats-Prognose ab Stichtag, § 15a InsO 6 Wochen bei Überschuldung, Drei-Wochen-Liquiditätsstockungs-Test, jährliche Aktualisierung.
- Tragende Normen verifizieren: InsO § 19 Abs. 2 (zweistufige Prüfung), IDW S 11 (Anforderungen), IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), StaRUG §§ 1, 102 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Restrukturierungsberater, IV (falls beauftragt), Bank, Gesellschafter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Fortbestehensprognose-Bericht, Integrierte Planung (P&L, BS, CF) 12+ Monate, Stresstest-Szenarien, Sanierungskonzept IDW S 6, Sanierungsgutachten, GF-Erklärung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fortbestehensprognose**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Fortbestehensprognose § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwoelf-Monats-Liquiditaet. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose.

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
- **Primärer Pfad:** Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Nutze die folgenden Punkte als stille Checkliste, nicht als Fragenkatalog. Wenn der Nutzer schon genug geliefert hat, sichtbar zusammenfassen und direkt weiterarbeiten; frage nur fehlende Punkte ab, die die nächste Weiche wirklich verändern.

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
4. **Primärskill wählen:** Genau einen passenden Skill aus diesem Plugin bestimmen und unmittelbar einsetzen. Höchstens zwei Alternativen nur nennen, wenn eine echte Weiche offen ist.
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

### 5. Fachmodule gezielt und sparsam laden

1. Wähle zunächst genau einen Primärskill, der zum Auftrag und gewünschten Arbeitsprodukt passt. Weitere Skills kommen nur bei einer konkreten Schnittstelle hinzu.
2. Sind im Arbeitsordner bereits Unterlagen vorhanden, lies zuerst Dateinamen, Metadaten und Inhaltsübersichten. Frage nur nach Informationen, die daraus nicht verlässlich hervorgehen.
3. Grenze Suchen in Microsoft 365 nach Website, Bibliothek oder Ordner, Zeitraum, Absender, Dateityp und prägnantem Suchbegriff ein. Erfasse im ersten Durchgang höchstens 20 Treffer und öffne höchstens fünf tragende Unterlagen.
4. Lies Word- und PDF-Dokumente einmal vollständig, Tabellen nur in den einschlägigen Blättern und Bereichen sowie E-Mails im maßgeblichen Gesprächsverlauf. Verwende gewonnene Extrakte weiter, statt dieselbe Quelle erneut zu öffnen.
5. Die [vollständige Fachmodulkarte](references/fachmodule.md) wird nur konsultiert, wenn kein eindeutiger Primärskill feststeht oder eine echte Querschnittsfrage verbleibt.

## Worum geht es?

Dieses Plugin begleitet Geschäftsführer und Vorstande bei der Erstellung einer Fortbestehensprognose nach § 19 Abs. 2 InsO. Es dokumentiert Schritt für Schritt: ausloesende Ereignisse, bilanziellen Status, Fortfuehrungsannahmen, Plausibilisierung, rollende Zwoelf-Monats-Liquiditaet, Sensitivitaetsszenarien und Sanierungsbausteine (Patronatserklaerung, Comfortletter, Rangrücktritt, Stundung, Forderungsverzicht). Wenn die Prognose negativ ausfaellt, eskaliert das Plugin zum Pflichtenkatalog des Geschäftsführers nach §§ 15a, 15b InsO.

Das Plugin richtet sich an Eigenverantwortliche: Geschäftsführer, Vorstande und Finanzleiter — nicht als Ersatz für die Beauftragung eines Insolvenzrechtsanwalts.

## Wann brauchen Sie diese Skill?

- Ein Berufsträger weist bei der Jahresabschlusserstellung unter den Voraussetzungen des Paragrafen 102 StaRUG auf einen möglichen Insolvenzgrund hin; daneben kommen vertragliche Hinweise aus anderen Mandaten in Betracht.
- Das Unternehmen zeigt Liquiditaetsengpaesse und Sie als Geschäftsführer müssen dokumentieren, dass Sie aktiv gehandelt haben.
- Gesellschafter oder Banken verlangen eine Fortbestehensprognose als Voraussetzung für Unterstuetzungsmassnahmen.
- Sie prüfe Sanierungsbausteine (Gesellschafterdarlehen, Rangrücktritt, Patronatserklaerung) und wollen die insolvenzrechtliche Wirkung verstehen.
- Die Prognose ist knapp positiv oder negativ und Sie benoetigen den Pflichtenkatalog für die naechsten Schritte.

## Fachbegriffe (kurz erklaert)

- **Fortbestehensprognose** — Einschaetzung, ob das Unternehmen im Prognosezeitraum (ueblicherweise 12 Monate) ueberwiegend wahrscheinlich zahlungsfaehig bleiben wird (§ 19 Abs. 2 InsO, Maßstab IDW S 11).
- **Ueberschuldung** — Passiva uebersteigen Aktiva nach bilanzieller Bewertung; bei positiver Fortbestehensprognose kein Insolvenzgrund nach § 19 Abs. 2 InsO.
- **Rangrücktritt** — Erklaerung des Gesellschafters, seine Darlehensforderung hinter alle anderen Gläubiger zurueckzustellen; fuehrt zur Nichtpassivierung im insolvenzrechtlichen Status.
- **Patronatserklaerung (hart)** — Rechtsverbindliche Erklaerung des Gesellschafters oder Mutterunternehmens, die Tochtergesellschaft so auszustatten, dass sie zahlungsfaehig bleibt; beruecksichtigungsfaehig im Status.
- **Comfortletter** — Weiche Erklaerung des Patrons; nicht rechtsverbindlich; nicht ausreichend für insolvenzrechtlichen Status.
- **IDW S 11** — Institut der Wirtschaftspruefer, Standard 11: Maßstab und Methodik für die Fortbestehensprognose.
- **StaRUG** — Gesetz über den Stabilisierungs- und Restrukturierungsrahmen; Option vor formeller Insolvenz.

## Rechtsgrundlagen

- § 17 InsO — Zahlungsunfaehigkeit (Insolvenzgrund)
- § 18 InsO — Drohende Zahlungsunfaehigkeit (nur Eigenantrag; Prognosezeitraum 24 Monate)
- § 19 InsO — Ueberschuldung und Fortbestehensprognose (Prognosezeitraum **12 Monate** seit 01.01.2024; SanInsKG-Verkürzung auf 4 Monate galt nur bis 31.12.2023, ist nicht verlängert worden)
- § 15a InsO — Insolvenzantragspflicht (sechs Wochen bei Ueberschuldung, drei Wochen bei Zahlungsunfaehigkeit)
- § 15b InsO — Zahlungsverbot und Haftung bei Insolvenzverschleppung
- § 43 GmbHG — Haftung des Geschäftsführers
- §§ 1-93 StaRUG — Restrukturierungsrahmen
- **BGH IX ZR 285/14 vom 26.01.2017** — Steuerberater-Hinweispflicht bei Krisensignalen; bei verfehlter Fortbestehensprognose haftet Berater. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>
- **BGH IX ZR 56/22 vom 29.06.2023** — Drittschutzwirkung zugunsten des (faktischen) GF. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen GF. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- § 3a EStG — Steuerliche Behandlung Sanierungsgewinn

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klären: Wer nutzt das Plugin (GF, Vorstand, Finanzleiter), Rechtsform, Geschäftsjahr, Buchhaltungssystem.
2. Phase des Mandats bestimmen: Ausloeser erfassen, bilanzieller Status, Annahmen, Plausibilisierung, Liquiditaetsplanung oder Sanierungsbaustein-Erstellung.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen prüfen: Dreiwochenfrist Zahlungsunfaehigkeit, Sechswochenfrist Ueberschuldung nach § 15a InsO.
5. Anschluss-Skill bestimmen: Wenn Prognose negativ, sofort `wenn-prognose-negativ-naechste-schritte` und Insolvenzanwalt einbinden.

## Skill-Tour (was gibt es hier?)

**Konfiguration und Einstieg**

- `fortbestehensprognose-kaltstart-interview` — Ersteinrichtung: Rolle, Rechtsform, Ansprechpartner, Buchhaltungssystem und Profil schreiben.

**Aufnahme und Analyse**

- `ausloesendes-ereignis-erfassen` — Dokumentiert Anlass, Datum, Hinweisgeber und Mitteilungsform der Fortbestehenspruefung.
- `bilanzieller-status-aufnehmen` — Nimmt Aktiva, Passiva, Eigenkapital und ausserbilanzielle Verpflichtungen auf; prüft bilanziellen Ueberschuldungsverdacht.
- `annahmen-sammeln-fortfuehrung` — Sammelt Fortfuehrungsannahmen zu Umsatz, Kosten, Personal, Investitionen und Working Capital.
- `annahmen-belastbarkeit-plausibilisieren` — Plausibilisiert Annahmen gegen Vergangenheit und Marktentwicklung; erzeugt Plausibilitaetsprotokoll.
- `liquiditaet-12-monate` — Rollende Zwoelf-Monats-Liquiditaetsvorschau mit Einzahlungen, Auszahlungen und Linienverbleib.

**Sanierungsbausteine (Dokumente erzeugen)**

- `sanierungsbausteine-vorschlagen` — Empfehlungsmatrix für Sanierungsmassnahmen nach Effekt und Umsetzungszeit.
- `patronatserklaerung-extern-hart-erzeugen` — Harte externe Patronatserklaerung als DOCX zur Unterzeichnung erzeugen.
- `comfortletter-weich-erzeugen` — Comfortletter (weich, nicht rechtsverbindlich) erstellen mit Warnhinweis zur insolvenzrechtlichen Wirkung.
- `gesellschafterdarlehen-rangruecktritt` — BGH-konforme Rangruecktrittserklaerung nach § 19 Abs. 2 S. 2 InsO erzeugen.
- `forderungsverzicht-besserungsschein` — Forderungsverzicht mit Besserungsschein erstellen mit steuerlichen Hinweisen.
- `stundungsanfrage-glaeubiger` — Stundungsanfragen an Gläubiger (Lieferanten, Bank, Finanzamt, Sozialversicherung) individuell erstellen.

**Prognose und Dokumentation**

- `fortbestehensprognose-zusammenfuehren` — Alle Bausteine zusammenfuehren und Gesamtbewertung nach IDW S 11 erstellen.
- `prognose-dokumentation-stichtag` — Abschliessende Selbstdokumentation zum Stichtag als Haftungsbeleg.

**Eskalation**

- `wenn-prognose-negativ-naechste-schritte` — Pflichtenkatalog bei negativer Prognose: § 15a InsO, § 15b InsO, StaRUG-Option, Insolvenzanwalt.

## Worauf besonders achten

- **Selbstdokumentation ersetzt keinen Insolvenzrechtsanwalt.** Das Plugin hilft GF bei Eigenverantwortung; bei negativer oder knapp positiver Prognose ist Fachanwaltskonsultation zwingend.
- **Rangrücktritt muss BGH-konform formuliert sein.** Fehlformulierungen sind insolvenzrechtlich wirkungslos; Skill `gesellschafterdarlehen-rangruecktritt` liefert BGH-konforme Formulierung.
- **Nur harte Patronatserklaerung ist beruecksichtigungsfaehig.** Comfortletter reicht nicht aus; das Plugin weist explizit darauf hin.
- **Dreiwochenfrist laeuft ohne Hemmung.** Sobald Zahlungsunfaehigkeit eingetreten ist, laeuft § 15a InsO-Frist ohne Moeglichkeit der Verlaengerung.
- **Steuerliche Folgen von Sanierungsgewinn beachten.** Forderungsverzicht loest beim Schuldner Ertrag aus; Skill `forderungsverzicht-besserungsschein` enthaelt entsprechenden Hinweis.

## Typische Fehler

- Prognose wird auf der Basis zu optimistischer Annahmen erstellt ohne Plausibilisierung gegen Vergangenheit und Markt.
- Bilanzieller Status wird mit insolvenzrechtlichem Status gleichgesetzt; beide können abweichen (stille Reserven, Rangrücktritt).
- Comfortletter wird als ausreichend für positiven Status behandelt; fuehrt zu fehlerhafter Prognose.
- Dokumentation erfolgt nach dem Ereignis (nachtraeglich), nicht zum Stichtag; Haftungsschutz entfaellt.
- Steuerwirkung des Sanierungsgewinns (§ 3a EStG) wird nicht beachtet; unerwartete Steuerlast.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (InsO, StaRUG, GmbHG, EStG, BGB)
- IDW S 11 (Fortbestehensprognose) und IDW S 6 (Sanierungskonzept) in geltender Fassung
