---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Normenkontrolle Bauleitplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill"
---

# Normenkontrolle Bauleitplanung — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: VwGO § 47 Abs. 2 Antrag 1 Jahr nach Bekanntmachung, BauGB § 3 Abs. 2 Auslegung 1 Monat, Einwendungen 1 Monat, § 215 BauGB Rüge formeller/materieller Fehler 1 Jahr.
- Tragende Normen verifizieren: VwGO § 47, BauGB §§ 1, 1a, 2, 3, 4, 4a, 10, 13, 13a, 13b, 30, 34, 35, BImSchG, BNatSchG, UVPG, EU-Plan-UP-RL 2001/42 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Antragsteller (Eigentümer, Gemeinde, Verband), Gemeinde als Antragsgegnerin, OVG/VGH (zuständig), BVerwG (4. Senat), Träger öffentlicher Belange.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Bebauungsplan, Begründung mit Umweltbericht, Abwägungsmaterial, Beteiligungsstellungnahmen, Satzungsbeschluss, Normenkontrollantrag, Eilantrag § 47 Abs. 6 VwGO — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Normenkontrolle Bauleitplanung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Plugin für die Prüfung und Anfechtung von Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften nach § 47 VwGO vor BayVGH und OVG. Mandatsperspektive Antragstellervertretung.

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
| `abwaegungsgebot-1-abs-7-baugb` | Mandant greift Bebauungsplan wegen fehlerhafter Interessenabwaegung an. § 1 Abs. 7 BauGB Abwaegungsgebot. Prüfraster: vier Abwaegungsfehler-Stufen Abwaegungsausfall Abwaegungsdefizit Abwaegungsfehleinschaetzung… |
| `anpassungsgebot-flaechennutzungsplan` | Mandant greift Bebauungsplan an weil er nicht aus dem Flaechennutzungsplan entwickelt wurde. § 8 Abs. 2 BauGB Entwicklungsgebot und Anpassungsgebot. Prüfraster: Entwicklungssaussage des FNP bezogen auf Plangebiet… |
| `antragsbefugnis-eigentuemer-nachbar` | Grundstueckseigentuemer oder Nachbar moechte Normenkontrollantrag stellen und fragt ob er antragsbefugt ist. § 47 Abs. 2 S. 1 VwGO Antragsbefugnis Normenkontrolle. Prüfraster: Möglichkeitstheorie als Maßstab… |
| `artenschutz-naturschutz-planung` | Buerger oder Naturschutzverband greift Bebauungsplan wegen unzureichender Artenschutzprüfung an. § 44 BNatSchG Zugriffsverbote § 45 Abs. 7 BNatSchG Ausnahme. Prüfraster: spezielle artenschutzrechtliche Prüfung (saP)… |
| `aufstellungsbeschluss-bekanntmachung` | Mandant prüft ob ein Bebauungsplan an einem Verfahrensfehler beim Aufstellungsbeschluss oder der Bekanntmachung leidet. §§ 2 10 BauGB Verfahrenskette. Prüfraster: Aufstellungsbeschluss ortsuebl. Bekanntmachung § 2 Abs.… |
| `beteiligung-frueh-foermlich` | Mandant greift Bebauungsplan wegen Fehlern in der Buerger- oder Behördenbeteiligung an. §§ 3 4 BauGB Beteiligungsverfahren. Prüfraster: fruehzeitige Beteiligung § 3 Abs. 1 foermliche Auslegung § 3 Abs. 2 mindestens 1… |
| `buergerversammlung-protokoll-audit` | Mandant war bei Buergerversammlung und moechte Niederschrift auf Vollständigkeit prüfen. § 3 Abs. 1 BauGB Buergerversammlung Eroerterungstermin. Prüfraster: Einladung Tagesordnung Sitzungsleitung Wortbeitraege… |
| `einstweilige-anordnung-47-abs-6-vwgo` | Mandant hat Normenkontrollantrag eingereicht und moechte Vollzug des Bebauungsplans bis zur Entscheidung stoppen. § 47 Abs. 6 VwGO einstweilige Anordnung. Prüfraster: Vollzugsfolgenabwaegung als Maßstab… |
| `erforderlichkeit-1-abs-3-baugb` | Mandant greift Bebauungsplan als Gefälligkeitsplanung oder Verhinderungsplanung an. § 1 Abs. 3 S. 1 BauGB Erforderlichkeit Planrechtfertigung. Prüfraster: nachvollziehbares staedtebauliches Konzept erforderlich… |
| `festsetzungskatalog-9-baugb-baunvo` | Mandant greift einzelne Festsetzungen im Bebauungsplan als rechtswidrig an. § 9 BauGB abschließender Festsetzungskatalog BauNVO. Prüfraster: Festsetzungen außerhalb des Katalogs unwirksam BauNVO Art und Mass bauliche… |
| `immissionsschutz-laerm-bauleitplanung` | Mandant greift Bebauungsplan wegen unzureichendem Schallschutz oder Immissionsschutz an. DIN 18005 TA Laerm § 50 BImSchG. Prüfraster: Orientierungswerte verschiedene Gebietstypen Schallschutzgutachten Methodik… |
| `jahresfrist-47-abs-2-vwgo` | Mandant moechte Normenkontrollantrag stellen und Anwalt prüft ob die Jahresfrist noch laeuft. § 47 Abs. 2 S. 1 VwGO Jahresfrist Normenkontrolle. Prüfraster: Fristbeginn ortsuebliche Bekanntmachung § 10 Abs. 3 BauGB… |
| `mandat-erstgespraech-normenkontrolle` | Grundstueckseigentuemer oder Nachbar kommt wegen Bebauungsplan oder FNP in die Kanzlei. Erstgespraech Normenkontrollmandat. Prüfraster: Mandantenbetroffenheit Antragsbefugnis § 47 Abs. 2 VwGO Antragsfrist… |
| `muendliche-verhandlung-vgh-strategie` | Normenkontrollantrag steht vor muendlicher Verhandlung am VGH oder OVG. Vorbereitung muendliche Verhandlung Normenkontrolle. Prüfraster: Plaedoyer Einleitung Sachverhalt Rechtsausführungen Anträge schriftliche… |
| `normenkontrollantrag-schriftsatz` | Normenkontrollantrag gegen Bebauungsplan oder FNP ist zu erstellen. § 47 VwGO Normenkontrollantrag Schriftsatz. Prüfraster: Rubrum Antrag Begründung Zulässigkeit (Statthaftigkeit Befugnis Frist Rechtsschutzbedürfnis)… |
| `planerhaltung-214-215-baugb` | Gemeinde oder Vorhabentraeger prüft ob erkannte Planfehler zur Unwirksamkeit führen oder durch Planerhaltung geheilt werden. §§ 214 215 BauGB Planerhaltung und Ruegefrist. Prüfraster: § 214 Abs. 1 bis 3 beachtliche… |
| `statthaftigkeit-47-vwgo` | Mandant fragt ob Normenkontrollantrag gegen eine bestimmte Planung zulässig ist. § 47 Abs. 1 VwGO Statthaftigkeit Normenkontrolle. Prüfraster: Antragsgegenstand Bebauungsplan § 10 BauGB vorhabenbezogener B-Plan § 12… |
| `stellplatzsatzung-bay-bauordnung` | Mandant wendet sich gegen Stellplatzsatzung einer Gemeinde oder deren Anwendung bei Bauantrag. Art. 47 BayBO § 9 Abs. 1 Nr. 4 BauGB Art. 81 BayBO Stellplatzsatzung. Prüfraster: Reduzierung Stellplatzschluessel durch… |
| `umweltbericht-umweltpruefung` | Mandant greift Bebauungsplan wegen unzureichender Umweltprüfung oder fehlendem Umweltbericht an. § 2 Abs. 4 BauGB § 2a BauGB Umweltbericht. Prüfraster: Schutzgueter nach Anhang 1 BauGB Mensch Tiere Pflanzen Boden… |
| `veraenderungssperre-zurueckstellung-14-15-baugb` | Bauherr oder Investor hat Bauantrag eingereicht aber Gemeinde hat Veraenderungssperre verhaengt und Antrag wird zurückgestellt. §§ 14 15 BauGB. Prüfraster: Aufstellungsbeschluss Voraussetzung § 14 Abs. 1 BauGB Wirkung… |
| `vorhabenbezogener-bebauungsplan-12-baugb` | Mandant ist Vorhabentraeger eines VEP oder sieht sich durch vorhabenbezogenen B-Plan benachteiligt. § 12 BauGB vorhabenbezogener Bebauungsplan. Prüfraster: Drei-Saeulen-Konstruktion Vorhaben- und Erschließungs-Plan… |

## Worum geht es?

Dieses Plugin begleitet die Prüfung und Anfechtung von Bebauungsplaenen, Flaechennutzungsplaenen und oertlichen Bauvorschriften vor dem Bayerischen Verwaltungsgerichtshof (BayVGH) und den Oberverwaltungsgerichten (OVG) nach § 47 VwGO. Es deckt das Mandat aus der Perspektive des Antragstellers (Eigentümer, Nachbar, Naturschutzverband) ab.

Das Plugin strukturiert die Zulaessigkeitsvoraussetzungen (Statthaftigkeit, Antragsbefugnis, Jahresfrist), die Fehlertypen nach dem BauGB (Verfahrensfehler, Erforderlichkeit, Abwaegungsmangel, Fehler bei Festsetzungen), die Planerhaltungsregeln der §§ 214 und 215 BauGB sowie den Eilrechtsschutz nach § 47 Abs. 6 VwGO. Es ersetzt keine individuellen Vertretungshandlungen.

## Wann brauchen Sie diese Skill?

- Grundstueckseigentuemer oder Nachbar kommt mit einem neuen Bebauungsplan in die Kanzlei und fragt nach Moeglichkeiten.
- Mandant hat eine Buergerversammlung besucht und moechte das Protokoll auf Vorfestlegungen prüfen lassen.
- Sie müssen schnell beurteilen, ob die Jahresfrist des § 47 Abs. 2 VwGO noch laeuft.
- Mandant moechte die Vollziehung eines gerade bekanntgemachten Bebauungsplans vorlaefig stoppen.
- Naturschutzverband fragt, ob er gegen einen Plan mit unzureichender Artenschutzpruefung vorgehen kann.

## Fachbegriffe (kurz erklaert)

- **Normenkontrolle (§ 47 VwGO)** — Abstraktes Kontrollinstrument; das OVG/VGH prüft die Rechtmaeßigkeit eines Bebauungsplans oder einer oertlichen Bauvorschrift auf Antrag.
- **Antragsbefugnis** — Nur wer in eigenen Rechten verletzt sein koennte, kann Antrag stellen (Moeglichkeitstheorie, § 47 Abs. 2 S. 1 VwGO).
- **Jahresfrist** — Normenkontrollantrag muss innerhalb eines Jahres ab ortsuebl. Bekanntmachung gestellt werden (§ 47 Abs. 2 S. 1 VwGO).
- **Abwaegungsgebot** — Die Gemeinde muss alle betroffenen Belange ermitteln, bewerten und gegeneinander abwaegen (§ 1 Abs. 7 BauGB); vier Fehlerstufen.
- **Planerhaltung** — §§ 214 und 215 BauGB beschraenken, welche Fehler zur Unwirksamkeit fuehren; Verfahrensfehler sind oft heilbar, Ergebnisfehler nicht.
- **Erforderlichkeit** — Bebauungsplan muss einem nachvollziehbaren staedtebaulichen Konzept dienen (§ 1 Abs. 3 BauGB); Gefaelligkeits- und Verhinderungsplanung sind unzulaessig.
- **Veraenderungssperre** — Sicherungsinstrument der Gemeinde nach § 14 BauGB; hemmt Baugenehmigungen waehrend des Aufstellungsverfahrens.
- **VEP** — Vorhabenbezogener Bebauungsplan nach § 12 BauGB mit Vorhaben- und Erschliessungsplan und Durchfuehrungsvertrag.

## Rechtsgrundlagen

- § 47 VwGO — Normenkontrollverfahren, Statthaftigkeit, Antragsbefugnis, Jahresfrist, einstweilige Anordnung.
- §§ 1 bis 13a BauGB — Aufstellungsverfahren, Erforderlichkeit, Abwaegungsgebot, Beteiligung, Veraenderungssperre.
- §§ 214 und 215 BauGB — Planerhaltung: beachtliche Fehler, Ruegefrist, ergaenzendes Verfahren.
- § 9 BauGB — Festsetzungskatalog.
- BauNVO — Art und Mass der baulichen Nutzung, Hoechtsgrenzen.
- § 44 BNatSchG — Artenschutzrechtliche Zugriffsverbote.
- Art. 47 BayBO, Art. 81 BayBO — Stellplaetze und oertliche Bauvorschriften in Bayern.
- § 2 Abs. 4 BauGB, § 2a BauGB — Umweltpruefung und Umweltbericht.

## Schritt-für-Schritt: Einstieg ins Plugin

1. Erstgespraech und Mandatsannahme-Prüfung: Skill `mandat-erstgespraech-normenkontrolle`.
2. Statthaftigkeit und Antragsbefugnis klären: `statthaftigkeit-47-vwgo` und `antragsbefugnis-eigentuemer-nachbar`.
3. Jahresfrist berechnen: `jahresfrist-47-abs-2-vwgo`.
4. Fehlersuche nach Prioritaet: Verfahrensfehler, Erforderlichkeit, Abwaegung, Festsetzungen.
5. Eilantrag prüfen bei drohenden Genehmigungen: `einstweilige-anordnung-47-abs-6-vwgo`.
6. Normenkontrollantrag formulieren: `normenkontrollantrag-schriftsatz`.

## Skill-Tour (was gibt es hier?)

**Einstieg und Mandat**

- `mandat-erstgespraech-normenkontrolle` — Erstgespraech, Mandatsannahme-Empfehlung, vorläufige Erfolgsaussichten.
- `statthaftigkeit-47-vwgo` — Statthaftigkeit der Normenkontrolle gegen Bebauungsplan, VEP, oertliche Bauvorschriften.
- `antragsbefugnis-eigentuemer-nachbar` — Antragsbefugnis für Eigentümer, Nachbar, Verband.
- `jahresfrist-47-abs-2-vwgo` — Jahresfrist berechnen, Fristbeginn, fehlerhafte Bekanntmachung.

**Verfahrensfehler**

- `aufstellungsbeschluss-bekanntmachung` — Fehler beim Aufstellungsbeschluss und der Bekanntmachung.
- `beteiligung-frueh-foermlich` — Fehler in der fruehzeitigen und foermlichen Beteiligung.
- `buergerversammlung-protokoll-audit` — Niederschrift der Buergerversammlung auf Vollstaendigkeit prüfen.
- `umweltbericht-umweltpruefung` — Umweltpruefung und Umweltbericht auf Fehler prüfen.
- `artenschutz-naturschutz-planung` — Artenschutzpruefung (saP), CEF-Maßnahmen, FFH-Vertraeglichkeit.

**Materielle Fehler**

- `erforderlichkeit-1-abs-3-baugb` — Erforderlichkeit und Planrechtfertigung; Gefaelligkeits- und Verhinderungsplanung.
- `abwaegungsgebot-1-abs-7-baugb` — Vier Abwaegungsfehler-Stufen nach § 1 Abs. 7 BauGB.
- `anpassungsgebot-flaechennutzungsplan` — Entwicklungsgebot aus dem Flaechennutzungsplan.
- `festsetzungskatalog-9-baugb-baunvo` — Unzulaessige Festsetzungen ausserhalb des Katalogs.
- `immissionsschutz-laerm-bauleitplanung` — Schallschutz, TA Laerm, § 50 BImSchG.

**Planerhaltung und Ruegefrist**

- `planerhaltung-214-215-baugb` — Welche Fehler fuehren zur Unwirksamkeit, welche sind heilbar? Ruegefrist ein Jahr.

**Spezialkonstellationen**

- `vorhabenbezogener-bebauungsplan-12-baugb` — VEP-Prüfung für Vorhabentraeger und Drittbetroffene.
- `veraenderungssperre-zurueckstellung-14-15-baugb` — Anfechtung und Entschaedigung bei Veraenderungssperre.
- `stellplatzsatzung-bay-bauordnung` — Stellplatzsatzung nach Art. 47 BayBO und § 9 Abs. 1 Nr. 4 BauGB.

**Schriftsaetze und Verhandlung**

- `normenkontrollantrag-schriftsatz` — Vollstaendiger Normenkontrollantrag mit Zulaessigkeit, Fehleranalyse, Hilfsantrag.
- `einstweilige-anordnung-47-abs-6-vwgo` — Eilantrag nach § 47 Abs. 6 VwGO gegen Vollziehung des Bebauungsplans.
- `muendliche-verhandlung-vgh-strategie` — Vorbereitung der muendlichen Verhandlung am VGH oder OVG.

## Worauf besonders achten

- **Jahresfrist ist absolut** — Ab ortsuebl. Bekanntmachung laeuft die Jahresfrist unabhaengig von Kenntnis; bei fehlerhafter Bekanntmachung beginnt sie nicht.
- **Planerhaltung filtert viele Fehler** — Nicht jeder Verfahrensfehler fuehrt zur Unwirksamkeit; § 214 Abs. 1 BauGB und die Ruegefrist des § 215 BauGB müssen immer mitbeachtet werden.
- **Ergebnisfehler immer beachtlich** — Fehler bei der Festsetzung ausserhalb des Katalogs oder bei der Erforderlichkeit sind nicht heilbar und nicht ruegepflichtig.
- **Teilunwirksamkeit beantragen** — Bei fehlerhaften Einzelfestsetzungen kann Teilunwirksamkeit Erfolg haben, selbst wenn der Gesamtplan sonst Bestand haelt.
- **Eilantrag und Hauptsache koordinieren** — § 47 Abs. 6 VwGO setzt keinen vor dem Antrag in der Hauptsache voraus; Antragsbefugnis muss aber gegeben sein.

## Typische Fehler

- Normenkontrolle gegen Flaechennutzungsplan beantragt, obwohl dieser grundsätzlich nicht statthafter Gegenstand ist (Ausnahme: Konzentrationsflaechen).
- Ruegefrist des § 215 BauGB versaeumnt; Verfahrensfehler können danach nicht mehr geltend gemacht werden.
- Naturschutzverband meldet sich ohne Verbandsklagebefugnis nach § 64 BNatSchG oder § 2 UmwRG.
- Abwaegungsfehler-Argument wird auf Vorgangs- statt auf Ergebnis-Ebene gefuehrt; § 214 Abs. 3 BauGB filtert nur Vorgangsfehler.
- Eilantrag nach § 47 Abs. 6 VwGO wird eingereicht, obwohl Bebauungsplan noch nicht in Kraft ist.

## Quellen und Aktualitaet

- Stand: 05/2026
- BauGB in der geltenden Fassung
- BauNVO in der geltenden Fassung
- VwGO § 47 in der geltenden Fassung
- BNatSchG §§ 44 und 45 in der geltenden Fassung
