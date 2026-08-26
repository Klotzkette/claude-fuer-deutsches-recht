---
name: start-chronologie-fristen
description: "Für Normenkontrolle Bauleitplanung — Allgemein: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix."
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
