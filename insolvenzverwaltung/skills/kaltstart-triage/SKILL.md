---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Insolvenzverwaltung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständi..."
---

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Insolvenzverwaltung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzverwaltung — Allgemein` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Insolvenzverwaltung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Insolvenzverwaltungs-Plugin aus Sicht von Insolvenzverwalter, Sachwalter und vorläufiger Verwaltung: Regelverfahren, Eigenverwaltung, Schutzschirm, Anfechtung, § 15b InsO, Masse, Forderungsprüfung, Insolvenzplan, StaRUG-Planwerkstatt, Gutachten, Berichte und Schlussrechnung.

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
| `iv-aktenanlage-verfahrenscockpit` | Neue Verfahrensakte anlegen und Verfahrenscockpit strukturieren wenn Insolvenzverwalter oder Sachwalter bestellt wird. §§ 56 80 InsO Verwalterbestellung und Verwaltungsbefugnis. Prüfraster: Aktenzeichen… |
| `iv-anfechtung-129ff` | Insolvenzanfechtungsansprüche nach §§ 129-147 InsO aus Verwaltersicht prüfen und verfolgen. Enthält KI-gestütztes Schuldnerakten-Screening, Kandidatenmatrix, §§ 130/131/133/134/135, Bargeschäft § 142, Rechtsfolgen §§… |
| `iv-arbeitsrecht-insolvenzgeld` | Personalthemen im Insolvenzverfahren bearbeiten: Lohnrückstaende Insolvenzgeld Kündigungen Betriebsuebergang Betriebsrat. §§ 113 125 InsO § 165 SGB III Insolvenzgeld. Prüfraster: Arbeitnehmerbestand Rückstaende… |
| `iv-berichte-gericht-glaeubiger` | Zwischenberichte Sachstandsberichte und Beschlussvorlagen für Insolvenzgericht Gläubiger­ausschuss und Gläubiger­versammlung erstellen. §§ 58 66 79 InsO Berichtspflichten. Prüfraster: Stichtag Massestand Tabelle… |
| `iv-eigenverwaltung-sachwaltung` | Sachwalter­kontrolle und Schnittstellenmanagement bei Eigenverwaltung nach §§ 270 ff. InsO. §§ 270 274 275 InsO Sachwalterbefugnisse und Kontrollrechte. Prüfraster: Rollenabgrenzung Finanzplankontrolle Rechnungslegung… |
| `iv-eroeffnungsgutachten` | Eroeffnungsgutachten als Sachverständiger oder vorläufiger Insolvenzverwalter erstellen wenn Gericht Prüfauftrag erteilt. §§ 17 18 19 InsO Eroffnungsgründe §§ 26 54 InsO Massekostendeckung. Prüfraster:… |
| `iv-forderungsanmeldung-pruefung` | Eingehende Forderungsanmeldungen nach § 174 InsO prüfen und Tabelle für Prüfungstermin vorbereiten. §§ 174 175 176 InsO §§ 38 39 InsO Rang. Prüfraster: Schriftform Beleg Grund Betrag Rang Absonderungsrechte… |
| `iv-idw-s6-sanierungsfaehigkeit-gate` | Sanierungskonzept auf IDW-S-6-Niveau aus Insolvenzverwalter-, Sachwalter- oder vorläufiger Verwaltungsperspektive prüfen: Fortbestehensprognose, nachhaltige Sanierungsfähigkeit, Leitbild, Maßnahmen, integrierte Planung, Dokumentation und Go/No-go. |
| `iv-kommandocenter` | Einstiegspunkt für neue Insolvenzverwaltungsmandate: Verfahrensart bestimmen Prioritaeten setzen naechste Workstreams planen. §§ 56 80 InsO Verwalterbestellung § 270d Schutzschirm StaRUG. Prüfraster: Verfahrensrolle… |
| `iv-masseeinsammlung` | Massepositionen erfassen und realisieren: Bankguthaben Debitoren Herausgabeansprüche Versicherungen Rückstaende. §§ 80 148 InsO Verwaltungsbefugnis und Massezugehoerigkeit. Prüfraster: Massekarte Priorisierung… |
| `iv-massemehrung-asset-realisation` | Verwertungsstrategie und Massemehrung entwickeln wenn Masse niedrig oder Quote ungewiss ist. §§ 159 160 InsO Verwertung § 133 InsO Vorsatzanfechtung § 15b InsO Haftungsansprüche. Prüfraster: Werthebel Assets Prozesse… |
| `iv-masseunzulaenglichkeit-208` | Masseunzulaenglichkeit anzeigen und Zahlungsrangfolge steuern wenn Masseverbindlichkeiten nicht für alle ausreichen. § 208 InsO §§ 53 54 InsO Massekosten. Prüfraster: Ist- oder Prognoseunzulaenglichkeit Alt- und… |
| `iv-plan-abstimmung-mehrheiten` | Abstimmungsmehrheiten für Insolvenzplan und StaRUG-Plan simulieren und Abstimmungstermin vorbereiten. §§ 244 245 InsO Kopf- und Summenmehrheit §§ 25 26 StaRUG Klassenmehrheit. Prüfraster: Stimmberechtigte… |
| `iv-plan-anlagenpaket` | Anlagenpaket für Insolvenzplan oder StaRUG-Plan vollständig zusammenstellen. §§ 229 230 InsO Plananlagen §§ 14 15 StaRUG Unterlagen. Prüfraster: Pflichtanlagen je Route Vermögensuebersicht Finanzplan Erklärungen… |
| `iv-plan-cramdown-obstruktion` | Obstruktionsverbot und gruppenuebergreifende Mehrheitsentscheidung prüfen wenn ablehnende Gruppen oder Klassen vorhanden sind. § 245 InsO § 27 StaRUG Cramdown. Prüfraster: Schlechterstellung angemessene Beteiligung… |
| `iv-plan-darstellender-teil` | Darstellenden Teil des Insolvenzplans oder StaRUG-Plans vollständig und widerspruchsfrei verfassen. § 220 InsO § 6 StaRUG Darstellungspflichten. Prüfraster: Krisengeschichte Maßnahmen Vergleichsrechnung Sonderaktiva… |
| `iv-plan-datenraum-register` | Planbegleitenden Datenraum aufbauen und Dokumentenregister führen wenn alle Planbausteine belegbar sein müssen. §§ 218 229 InsO §§ 14 15 StaRUG Planunterlagen. Prüfraster: Pflichtunterlagen Jahresabschluesse BWA OPOS… |
| `iv-plan-gerichtliche-schritte` | Gerichtliche Verfahrensschritte für Insolvenzplan und StaRUG-Plan steuern von Einreichung bis Bestätigung. §§ 231 232 248 InsO Vorprüfung Bestätigung §§ 45 ff. StaRUG Gerichtsverfahren. Prüfraster: Einreichungsantrag… |
| `iv-plan-gestaltender-teil` | Gestaltenden Teil des Insolvenzplans mit konkreten Rechtsaenderungen Quoten und Vollstreckungsgrundlagen formulieren. § 221 InsO § 7 StaRUG Planwirkungen. Prüfraster: Rechtsaenderungen je Gruppe Quoten Stundungen… |
| `iv-plan-gruppen-klassenbildung` | Abstimmungsgruppen nach InsO und Klassen nach StaRUG sachgerecht bilden um Planbestätigungsrisiken zu minimieren. §§ 222 223 InsO Gruppenbildung §§ 9 10 StaRUG Klassenbildung. Prüfraster: Rechtsstellung wirtschaftliche… |
| `iv-plan-insolvenzplan-architektur` | Vollständigen Insolvenzplan nach §§ 217 ff. InsO von Grund auf strukturieren. §§ 217 220 221 InsO Planarchitektur. Prüfraster: Planvorlageberechtigung darstellender gestaltender Teil Anlagen Gruppen Sicherheiten… |
| `iv-plan-integrierte-planung` | Integrierte Planrechnung aus GuV Liquiditaet und Bilanz für Insolvenzplan oder StaRUG erstellen. §§ 220 229 InsO Finanzplanung § 14 StaRUG. Prüfraster: Ist-Zahlen Planannahmen Base-Case Stressszenarien Brückenrechnung… |
| `iv-plan-kaltstart-interview` | Erstes Mandatsgespräch strukturieren wenn Insolvenzplan oder StaRUG-Verfahren startet und kaum Unterlagen vorliegen. §§ 13 15a 17 InsO §§ 29 42 StaRUG Antragspflichten. Prüfraster: Basisdaten Krisenursachen… |
| `iv-plan-kommandocenter` | Insolvenzplan- oder StaRUG-Mandat starten Verfahrensroute bestimmen Ampelstatus setzen. §§ 217 218 InsO §§ 29 ff. StaRUG. Prüfraster: Rolle Verfahrensziel Datenraumstand Zahlenstand Stakeholder Fristen naechste Aktion.… |
| `iv-plan-minderheitenschutz` | Schlechterstellungsrisiken und Beschwerderisiken einzelner opponierender Beteiligter analysieren und Planverbesserungen vorschlagen. § 251 InsO § 64 StaRUG Minderheitenschutz. Prüfraster: individuelle… |
| `iv-plan-planbetroffene-auswahl` | Planbetroffene im StaRUG-Verfahren sachgerecht auswaehlen und Nichteinbeziehung begründen. §§ 2 4 StaRUG Gestaltbarkeit. Prüfraster: gestaltbare Rechtsverhältnisse Ausnahmen Arbeitnehmer deliktische Forderungen… |
| `iv-plan-planvollzug-monitoring` | Planvollzug nach Bestätigung ueberwachen Zahlungen kontrollieren und Abweichungen dokumentieren. §§ 248 261 InsO Planueberwachung §§ 69 72 StaRUG. Prüfraster: Bedingungen Fälligkeiten Quoten Zahlstellen Covenants… |
| `iv-plan-redteam-qualitygate` | Insolvenzplan oder StaRUG-Plan vor Einreichung hart auf Fehler prüfen aus Sicht opponierender Gläubiger und Gericht. §§ 231 245 251 InsO Versagungsgründe. Prüfraster: Vollständigkeit Bewertungswiderspruch… |
| `iv-plan-sanierungskonzept` | Sanierungskonzept als wirtschaftliche Grundlage für Insolvenzplan oder StaRUG erstellen oder prüfen. §§ 220 229 InsO §§ 6 14 StaRUG Fortbestehensfähigkeit. Prüfraster: Krisenstadium Ursachen Leitbild Maßnahmenpakete… |
| `iv-plan-sicherheiten-drittsicherheiten` | Absonderungsrechte und Drittsicherheiten im Insolvenzplan und StaRUG planfest behandeln und Ausfallwerte bestimmen. §§ 49 50 51 224 InsO Absonderung § 2 Abs. 4 StaRUG Drittsicherheiten. Prüfraster: Sicherheitenregister… |
| `iv-plan-stabilisierung-starug` | StaRUG-Stabilisierungsmassnahmen und Vollstreckungssperre beantragen wenn Vollstreckungsdruck die Sanierung gefaehrdet. §§ 49 50 51 StaRUG Stabilisierungsanordnung. Prüfraster: Stabilisierungsbedarf Verhältnismäßigkeit… |
| `iv-plan-stakeholder-kommunikation` | Gläubiger Banken Arbeitnehmer Lieferanten Gericht und Investoren zielgruppengerecht über Insolvenzplan oder StaRUG informieren. §§ 232 235 InsO Planeroerterung §§ 17 20 StaRUG Gläubigerinfo. Prüfraster:… |
| `iv-plan-starug-plan-architektur` | StaRUG-Restrukturierungsplan vollständig strukturieren von Planbetroffenenauswahl bis Bestätigungspfad. §§ 6 7 8 StaRUG Planinhalt §§ 60 ff. StaRUG Abstimmung und Gerichtsverfahren. Prüfraster:… |
| `iv-plan-steuern-bilanz-folgen` | Steuerliche und bilanzielle Folgen des Insolvenzplans oder StaRUG prüfen damit Planwirkungen nicht an Nebenwirkungen scheitern. §§ 3a 3c EStG Sanierungsgewinn § 8c KStG Verlustvortrag. Prüfraster: Erlass Stundung… |
| `iv-plan-verfahrenswahl` | Passenden Sanierungsrahmen auswaehlen und Insolvenzplan Eigenverwaltung Schutzschirm StaRUG und außergerichtliche Einigung vergleichen. §§ 270 270a 270d InsO §§ 29 42 StaRUG. Prüfraster: Zahlungsunfähigkeit… |
| `iv-plan-vergleichsrechnung` | Vergleichsrechnung als Herzstück des Insolvenzplans oder StaRUG-Plans erstellen: Planfall gegen Ohne-Plan-Szenario. §§ 220 229 InsO Vergleichsdarstellung § 6 Abs. 2 StaRUG. Prüfraster: Masse Kosten Sicherheiten… |
| `iv-qualitaets-und-plausibilitaetsgate` | IV-Arbeitsergebnisse vor Versand oder Entscheidung auf Widersprueche Rechenfehler fehlende Belege und Rollenfehler prüfen. §§ 58 66 InsO Prüfungspflichten des Gerichts. Prüfraster: Rollencheck Zahlencheck Normencheck… |
| `iv-regelverfahren-eroeffnung` | Regelinsolvenzverfahren nach Eroffnungsbeschluss umsetzen: Besitzuebergang Masse Tabelle Berichtstermin Verwertung. §§ 80 148 149 InsO §§ 151 ff. InsO Masseberechnung. Prüfraster: Verfuegungsbefugnis Bekanntmachungen… |
| `iv-schutzschirm-270d` | Schutzschirmverfahren nach § 270d InsO begleiten von Antrag und Bescheinigung bis Planvorlageschluss. § 270d InsO Schutzschirm §§ 270 274 InsO Eigenverwaltung Sachwaltung. Prüfraster: Voraussetzungen Bescheinigung… |
| `iv-sicherung-betriebsfortfuehrung` | Betrieb in Insolvenz fortführen wenn Massemehrung oder Sanierung geplant ist und Lohn Lieferanten und Auftraege gesichert werden müssen. §§ 22 55 InsO Massebegrundung §§ 113 120 InsO Arbeitsverhältnisse. Prüfraster:… |
| `iv-steuern-sozialversicherung` | Steuerliche und sozialversicherungsrechtliche Verbindlichkeiten im Insolvenzverfahren klassifizieren und bearbeiten. §§ 38 55 InsO Rangklassen §§ 34 35 AO Haftung. Prüfraster: Insolvenzforderung Masseverbindlichkeit… |
| `iv-tabelle-pruefungstermin` | Insolvenztabelle konsolidieren und Prüfungstermin nach §§ 175 ff. InsO vorbereiten. §§ 175 176 177 InsO Tabellenführung und Widersprueche. Prüfraster: Tabellenbereinigung Doubletten Rang Zinsen Widersprueche nach Grund… |
| `iv-verteilung-schlussrechnung` | Abschlussphase des Insolvenzverfahrens durchführen: Schlussrechnung Schlussbericht Verteilungsverzeichnis Quote Nachtragsverteilung. §§ 196 197 InsO Schlussverteilung §§ 66 67 InsO Schlussrechnung. Prüfraster:… |
| `iv-vorläufige-verwaltung` | Erste Maßnahmen als vorlaeufliger Insolvenzverwalter nach § 21 InsO umsetzen: Bankkonten Besitz Post Drittschuldner Betrieb. § 21 InsO Sicherungsmassnahmen § 22 InsO Pflichten des vorl. Verwalters. Prüfraster:… |
| `iv-zahlungsklagen-15b` | Zahlungsklagen nach § 15b InsO gegen Geschäftsleiter vorbereiten wenn Zahlungen nach Insolvenzreife erfolgt sind. § 15b InsO §§ 17 19 InsO Insolvenzreife. Prüfraster: Insolvenzreifedatum Zahlungen nach Stichtag… |

## Worum geht es?

Das Plugin unterstuetzt Insolvenzverwalter, Sachwalter und vorlaeufliger Verwalter bei der vollstaendigen Durchfuehrung von Insolvenzverfahren nach der Insolvenzordnung (InsO) sowie bei Restrukturierungen nach dem StaRUG. Es bildet den gesamten Verfahrenslebenszyklus ab: von der Antragspruefung und dem Eroeffnungsgutachten über Betriebsfortfuehrung, Masseeinsammlung, Forderungspruefung, Insolvenzplan und StaRUG-Planwerkstatt bis zur Schlussrechnung und Nachtragsverteilung.

Besonderer Schwerpunkt liegt auf dem mehrstufigen Insolvenzplan: Das Plugin enthaelt spezialisierte Bausteine für Architektur, darstellenden und gestaltenden Teil, Gruppen- und Klassenbildung, Vergleichsrechnung, Cramdown-Prüfung, Stakeholder-Kommunikation und gerichtliche Schritte.

## Wann brauchen Sie diese Skill?

- Sie wurden als Insolvenzverwalter bestellt und müssen das Verfahren strukturieren, Prioritaeten setzen und erste Maßnahmen einleiten.
- Sie prüfen Anfechtungsansprueche nach §§ 129 ff. InsO und benoetigen einen strukturierten Prüfrahmen mit Fristen und Vergleichspotenzial.
- Sie erstellen ein Eroeffnungsgutachten für das Insolvenzgericht: Zahlungsunfaehigkeit, Ueberschuldung, Massekostendeckung.
- Sie sollen einen Insolvenzplan oder StaRUG-Restrukturierungsplan vollstaendig aufbauen und vor Einreichung Quality-Gate durchfuehren.
- Die Verfahrensschlussphase naht: Schlussrechnung, Schlussbericht, Verteilungsverzeichnis und Quote müssen erstellt werden.

## Fachbegriffe (kurz erklaert)

- **Regelverfahren** — Standardinsolvenzverfahren nach §§ 80 ff. InsO; Insolvenzverwalter uebernimmt Verwaltungs- und Verfuegungsbefugnis.
- **Eigenverwaltung** — Schuldner verbleibt in der Verfuegungsmacht; Sachwalter kontrolliert (§§ 270 ff. InsO).
- **Schutzschirm** — Besondere Form der Eigenverwaltung bei drohender Zahlungsunfaehigkeit (§ 270d InsO).
- **Masseunzulaenglichkeit** — Situation, in der Masseverbindlichkeiten die Masse uebersteigen; Anzeige nach § 208 InsO.
- **StaRUG** — Unternehmensstabilisierungs- und -restrukturierungsgesetz; vorinsolvenzliches Sanierungsverfahren.
- **Cramdown** — Gruppenuebergreifende Mehrheitsentscheidung nach § 245 InsO / § 27 StaRUG; Plan kann über ablehnende Klassen hinweggesetzt werden.
- **Vergleichsrechnung** — Gegenueberstellen von Plan-Fall und Liquidationsszenario zur Demonstration des Planmehrwerts.
- **PSV** — Pensionssicherungsverein; sichert Pensionsansprueche der Arbeitnehmer bei Insolvenz des Arbeitgebers.
- **§ 15b InsO** — Zahlungsverbote nach Insolvenzreife; Haftung des Geschäftsleiters für nicht privilegierte Zahlungen.

## Rechtsgrundlagen

- §§ 17 18 19 InsO — Insolvenzeroeffnungsgruende
- §§ 21 22 InsO — Vorlaeufliger Verwalter und Sicherungsmassnahmen
- §§ 26 54 InsO — Massekostendeckung und Verfahrenskosten
- §§ 56 80 InsO — Verwalterbestellung und Verwaltungsbefugnis
- §§ 129 131 133 135 InsO — Insolvenzanfechtung
- §§ 148 151 InsO — Masseberechnung
- §§ 174-177 InsO — Forderungsanmeldung und Tabelle
- §§ 208 209 InsO — Masseunzulaenglichkeit
- §§ 217-261 InsO — Insolvenzplan
- §§ 270 270d 274 InsO — Eigenverwaltung und Schutzschirm
- §§ 29 42 45 60 StaRUG — StaRUG-Verfahren
- § 15b InsO — Zahlungsverbote nach Insolvenzreife
- §§ 3a 3c EStG — Sanierungsgewinn

## Schritt-für-Schritt: Einstieg ins Plugin

1. Kommandocenter: Verfahrensrolle, Sicherungsmassnahmen, Betriebsfortfuehrung und Masseampel bestimmen.
2. Aktenanlage und Verfahrenscockpit aufbauen; Beteiligtenregister und Fristenliste anlegen.
3. Vorlaeufige Verwaltung oder Eroeffnungsgutachten durchfuehren.
4. Laufende Verwaltung: Masse einsammeln, Forderungen prüfen, berichten.
5. Abschlussphase: Plan, Schlussrechnung oder Verteilung je nach Verfahrensziel.

## Skill-Tour (was gibt es hier?)

- `iv-aktenanlage-verfahrenscockpit` — Neue Verfahrensakte anlegen und Verfahrenscockpit mit Gliederung, Rollenplan und Fristenliste strukturieren.
- `iv-anfechtung-129ff` — Insolvenzanfechtungsansprueche nach §§ 129 ff. InsO prüfen und verfolgen.
- `iv-arbeitsrecht-insolvenzgeld` — Personalthemen in der Insolvenz bearbeiten: Lohnrueckstaende, Insolvenzgeld, Kuendigungen.
- `iv-berichte-gericht-glaeubiger` — Zwischenberichte und Beschlussvorlagen für Insolvenzgericht und Gläubiger erstellen.
- `iv-eigenverwaltung-sachwaltung` — Sachwalter-Kontrolle und Schnittstellenmanagement bei Eigenverwaltung nach §§ 270 ff. InsO.
- `iv-eroeffnungsgutachten` — Eroeffnungsgutachten als Sachverstaendiger oder vorläufiger Verwalter erstellen.
- `iv-forderungsanmeldung-pruefung` — Forderungsanmeldungen nach § 174 InsO prüfen und Tabelle für Prüfungstermin vorbereiten.
- `iv-idw-s6-sanierungsfaehigkeit-gate` — Sanierungskonzept und Sanierungsfähigkeit vor Planroute, Schutzschirm oder StaRUG hart plausibilisieren.
- `iv-kommandocenter` — Einstiegspunkt: Verfahrensart bestimmen, Prioritaeten setzen und Workstreams planen.
- `iv-masseeinsammlung` — Massepositionen erfassen und realisieren: Bankguthaben, Debitoren, Herausgabeansprueche.
- `iv-massemehrung-asset-realisation` — Verwertungsstrategie und Massemehrung entwickeln: Werthebel, Anfechtung, Vergleich.
- `iv-masseunzulaenglichkeit-208` — Masseunzulaenglichkeit anzeigen und Zahlungsrangfolge nach § 208 InsO steuern.
- `iv-plan-abstimmung-mehrheiten` — Abstimmungsmehrheiten für Insolvenzplan und StaRUG-Plan simulieren.
- `iv-plan-anlagenpaket` — Anlagenpaket für Insolvenzplan oder StaRUG-Plan vollstaendig zusammenstellen.
- `iv-plan-cramdown-obstruktion` — Obstruktionsverbot und gruppenuebergreifende Mehrheitsentscheidung prüfen.
- `iv-plan-darstellender-teil` — Darstellenden Teil des Insolvenzplans oder StaRUG-Plans vollstaendig verfassen.
- `iv-plan-datenraum-register` — Planbegleitenden Datenraum aufbauen und Dokumentenregister fuehren.
- `iv-plan-gerichtliche-schritte` — Gerichtliche Verfahrensschritte von Einreichung bis Bestaetigung steuern.
- `iv-plan-gestaltender-teil` — Gestaltenden Teil mit konkreten Rechtsaenderungen, Quoten und Vollstreckungsgrundlagen formulieren.
- `iv-plan-gruppen-klassenbildung` — Abstimmungsgruppen nach InsO und Klassen nach StaRUG sachgerecht bilden.
- `iv-plan-insolvenzplan-architektur` — Vollstaendigen Insolvenzplan nach §§ 217 ff. InsO von Grund auf strukturieren.
- `iv-plan-integrierte-planung` — Integrierte Planrechnung aus GuV, Liquiditaet und Bilanz erstellen.
- `iv-plan-kaltstart-interview` — Erstes Mandatsgespraech strukturieren: Basisdaten, Krisenursachen, Gläubigerlandschaft.
- `iv-plan-kommandocenter` — Insolvenzplan- oder StaRUG-Mandat starten und Verfahrensroute bestimmen.
- `iv-plan-minderheitenschutz` — Schlechterstellungsrisiken einzelner Beteiligter analysieren und Planverbesserungen vorschlagen.
- `iv-plan-planbetroffene-auswahl` — Planbetroffene im StaRUG-Verfahren sachgerecht auswaehlen und Nichteinbeziehung begruenden.
- `iv-plan-planvollzug-monitoring` — Planvollzug nach Bestaetigung ueberwachen: Zahlungen, Covenants, Abweichungen.
- `iv-plan-redteam-qualitygate` — Insolvenzplan vor Einreichung hart auf Fehler prüfen aus Sicht opponierender Gläubiger.
- `iv-plan-sanierungskonzept` — Sanierungskonzept als wirtschaftliche Grundlage für Plan erstellen oder prüfen.
- `iv-plan-sicherheiten-drittsicherheiten` — Absonderungsrechte und Drittsicherheiten im Plan planfest behandeln.
- `iv-plan-stabilisierung-starug` — StaRUG-Stabilisierungsmassnahmen und Vollstreckungssperre beantragen.
- `iv-plan-stakeholder-kommunikation` — Gläubiger, Banken, Arbeitnehmer und Gericht zielgruppengerecht informieren.
- `iv-plan-starug-plan-architektur` — StaRUG-Restrukturierungsplan vollstaendig strukturieren.
- `iv-plan-steuern-bilanz-folgen` — Steuerliche und bilanzielle Folgen des Plans prüfen: Sanierungsgewinn, Verlustvortraege.
- `iv-plan-verfahrenswahl` — Passenden Sanierungsrahmen auswaehlen: Insolvenzplan, Eigenverwaltung, Schutzschirm, StaRUG.
- `iv-plan-vergleichsrechnung` — Vergleichsrechnung Plan-Fall vs. Liquidationsszenario als Herzstuck des Plans erstellen.
- `iv-qualitaets-und-plausibilitaetsgate` — IV-Arbeitsergebnisse vor Versand auf Widersprueche, Rechenfehler und Rollenfehler prüfen.
- `iv-regelverfahren-eroeffnung` — Regelinsolvenzverfahren nach Eroeffnungsbeschluss umsetzen: Besitz, Masse, Tabelle.
- `iv-schutzschirm-270d` — Schutzschirmverfahren nach § 270d InsO von Antrag bis Planvorlageschluss begleiten.
- `iv-sicherung-betriebsfortfuehrung` — Betrieb in Insolvenz fortfuehren: Cash-Bridge, Insolvenzgeld, kritische Lieferanten.
- `iv-steuern-sozialversicherung` — Steuerliche und sozialversicherungsrechtliche Verbindlichkeiten im Verfahren klassifizieren.
- `iv-tabelle-pruefungstermin` — Insolvenztabelle konsolidieren und Prüfungstermin nach §§ 175 ff. InsO vorbereiten.
- `iv-verteilung-schlussrechnung` — Abschlussphase: Schlussrechnung, Schlussbericht, Verteilungsverzeichnis und Quote.
- `iv-vorläufige-verwaltung` — Erste Maßnahmen als vorläufiger Insolvenzverwalter nach § 21 InsO umsetzen.
- `iv-zahlungsklagen-15b` — Zahlungsklagen nach § 15b InsO gegen Geschäftsleiter nach Insolvenzreife vorbereiten.

## Worauf besonders achten

- **Masseunzulaenglichkeit fruehzeitig prüfen**: Wird sie uebersehen, entstehen Haftungsrisiken für den Insolvenzverwalter wegen bevorzugter Befriedigung von Neuglaeubirn.
- **§ 15b InsO-Haftungsrisiken genau datieren**: Das Insolvenzreifdatum bestimmt, welche Zahlungen angreifbar sind; ungenaue Datierung gefaehrdet den Klagerfolg.
- **Gruppen- und Klassenbildung sorgfaeltig**: Fehlerhafte Gruppenbildung ist ein haeufiger Versagungsgrund bei der Planbestaetigung nach § 231 InsO.
- **StaRUG setzt drohende Zahlungsunfaehigkeit voraus**: Bei eingetretener Zahlungsunfaehigkeit muss Insolvenzantrag gestellt werden; StaRUG ist dann nicht mehr anwendbar.
- **Quality Gate vor Gerichtseinreichung**: Planfehler werden vom Gericht bei der Vorpruefung zurueckgewiesen; Korrektur kostet wertvolle Zeit.

## Typische Fehler

- Betriebsfortfuehrungs-Masse nicht abgegrenzt: Alt- und Neumasseverbindlichkeiten werden vermischt.
- Anfechtungsfristen nach § 129 InsO verschlafen; Ansprueche verjahren in drei Jahren ab Verfahrenseroeffnung.
- Insolvenzplan ohne Vergleichsrechnung eingereicht; Gericht weist bei Vorpruefung zurueck.
- StaRUG-Planbetroffene ohne Begruendung ausgewaehlt; Anfechtungsrisiko durch uebergangene Gläubiger.
- Sachwalter-Kontrolle bei Eigenverwaltung vernachlaessigt; Haftungsrisiko des Sachwalters bei unterlassener Beanstandung.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- InsO in der geltenden Fassung; bei Anfechtung zusätzlich Reform 2017 und Übergangsrecht prüfen
- StaRUG (Gesetz zur Fortentwicklung des Sanierungs- und Insolvenzrechts)
