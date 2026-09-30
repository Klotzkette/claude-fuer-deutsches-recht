# Dieselgate: das große Plugin für Diesel-Schadensersatz

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Navigation und Downloads

[Schnellstart](./diesel-schadensersatz-schnellstart.md) | [Werkstatt](./diesel-schadensersatz-werkstatt.md) | [Repository-Start](../README.md) | [Download-Index](../ASSET_INDEX.md) | [Skills](./skills/README.md) | [Fachquellen](./references/README.md) | [Werkzeuge](./tools/README.md) | [E-Akte-/beA-Assets](./assets/README.md) | [Neun Testakten](#neun-zentrale-testakten)

Dieses **große Dieselgate-Plugin** bündelt 21 installierbare Fachskills, den geprüften Rechtsprechungsbestand, Aktenstart- und beA-Werkzeuge, E-Akte-Schemas sowie neun zentrale Testakten im gemeinsamen Repository.

| Bestandteil | Verwendung | Download |
|---|---|---|
| Vollständiges Plugin | Installation in Claude, Cowork oder Claude Code | [`diesel-schadensersatz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/diesel-schadensersatz.zip) |
| Schnellstart | Kompakter eigenständiger Einstieg ohne Plugin-Installation | [Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=diesel-schadensersatz/diesel-schadensersatz-schnellstart.md) |
| Werkstatt | Vollständiger eigenständiger Arbeitsablauf für mehrstufige Akten | [Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=diesel-schadensersatz/diesel-schadensersatz-werkstatt.md) |

> Neuer Diesel-Fall. Starte den Profi-Schnelllauf. Prüfe alle beigefügten Unterlagen, beginne mit Sicherheitsstopps und Fristen, stelle höchstens drei nur wirklich blockierende Fragen und liefere dann Fallkarte, Beleglücken sowie genau einen nächsten Schritt.

<!-- END plugin-sofort-download-section (autogen) -->

Das Dieselgate-Plugin richtet sich an Diesel-Geschädigte und ihre Berater. Zielgruppe sind Rechtsanwaltskanzleien im Verbraucherrecht, Verbraucherschutzorganisationen und Legal-Tech-Anbieter, die Schadensersatzansprüche von Käufer:innen und Halter:innen betroffener Fahrzeuge gegen Fahrzeughersteller durchsetzen — von der Kaufakten-Aufnahme bis zur Klage, Kostenfestsetzung und Vollstreckung.

Der Bedienmodus ist für starke Berater gebaut, nicht für abgehobene Anwaltskommunikation: klare Menüs, kurze Entscheidungsfragen, Ampeln, Beleglücken und nächste Schritte. Tabellen erscheinen nur, wenn mindestens drei vergleichbare Werte oder wiederkehrende Felder davon wirklich profitieren. Die Bearbeitung bleibt juristisch korrekt, aber sie spricht die Arbeitssprache einer Beratungspraxis. Juristisch schwierige Punkte werden als Eskalation an eine Rechtsanwältin oder einen Rechtsanwalt markiert, nicht versteckt.

Jeder Skill besitzt eine eigene fachliche Intention und dasselbe verbindliche Argumentationsgerüst: Entscheidungssatz, Tatbestandsmerkmal, getrennte Tatsachen- und Belegspur, Norm und Rechtsprechungsrolle, fallbezogene Subsumtion, stärkstes Gegenargument, Ergebnis und nächster Schritt. Die vollständige Arbeitsnorm steht in [`references/juristische-schreib-und-argumentationsarchitektur.md`](references/juristische-schreib-und-argumentationsarchitektur.md).

## Schnellnavigation

| Ich will ... | Link | Was dort steht |
|---|---|---|
| sofort ohne Skillauswahl beginnen | [30-Sekunden-Schnellstart](./diesel-schadensersatz-schnellstart.md) | kompakter eigenständiger Startauftrag für Plugin oder Chatbot |
| Plugin installieren | [Installation](#installation) | Release-Asset, Marketplace-Datei, Pilotgruppe und Rollout-Regel |
| Prompt-Fallback nutzen | [Workflow-Prompts](#workflow-prompts) | Schnellstart- und Werkstattprompt als autarke Markdown-Dateien |
| Akten hochladen | [Welche Unterlagen die Bearbeitung braucht](#welche-unterlagen-die-bearbeitung-braucht) | Kaufvertrag, Finanzierung, Kontoauszug, Fahrzeugpapiere und Gerichtsunterlagen |
| Aktenordner vorsortieren | [Schnellstart](#schnellstart) | Ein-Befehl-Inventar mit Hashes, Dubletten, Format- und OCR-Befunden |
| Ohne Skillauswahl loslegen | [Schnellstart](#schnellstart) | Autostart für neuen Fall, Projektordner, Kaufakten-Input und Triage |
| Status und nächsten Schritt überblicken | [Kanzlei-Arbeitskopf](./assets/templates/kanzlei-arbeitskopf.md) | einheitliche Kontrollansicht für alle 21 Skills, getrennt vom Dokument |
| Juristisch präzise argumentieren | [Argumentationsarchitektur](references/juristische-schreib-und-argumentationsarchitektur.md) | vollständige Tatsachen-, Beweis-, Subsumtions- und Gegenargumentkette |
| Fachpfad finden | [Workflow-Phasen](#workflow-phasen) und [Bedienmuster im Tagesgeschäft](#bedienmuster-im-tagesgeschäft) | Pfade für großen Schadensersatz, Differenzschaden, Klage, Prozessreaktion, Kosten und Vollstreckung |
| Pilotbetrieb abnehmen | [Abnahme im Pilotbetrieb](#abnahme-im-pilotbetrieb) und [technische Strukturprüfung](../scripts/validate-plugin-structure.mjs) | Fachliche Prüffälle, Kontrollpunkte und technische Plugin-Abnahme |
| Testakten laden | [Neun zentrale Testakten](#neun-zentrale-testakten) und [zentraler Testakten-Katalog](../testakten/README.md) | acht Fachfälle, KBA-Rückrufregister-Referenz, Gesamt-PDFs und Release-ZIPs |
| Rechtsprechung filtern | [EA288 mit streitiger Betroffenheit](#ea288-mit-streitiger-betroffenheit) | 133er-Fünfjahreskorpus, 71er-Obergerichtsmatrix und 131er-EA288-Suche |
| Rechtsstand vorprüfen | [Rechtsstands-Cockpit](./tools/README.md#rechtsstand-vor-der-arbeit-prüfen) | lokale Frischeampel; danach produktive Quellen live öffnen |
| Gesetzgebung und Übergangsrecht 2026 prüfen | [Normstandsleitfaden 2026](references/rechtsstand-2026-gesetzgebung.md) | Zuständigkeit, Rechtsmittel, eCoC, Typgenehmigung und Euro 7 stichtagsbezogen trennen |
| Quellen kontrollieren | [Quellen und Konsistenz](#quellen-und-konsistenz) | Zitierweise, BGH-/EuGH-Anker und mitgelieferte Plugin-Referenzen |
| Schriftsatz für beA finalisieren | [beA-Versandpaket](#bea-versandpaket) | Endfassung, Anlagenstempel, Dateinamen, Hashes, Paketprüfung und Übergabe an Skill 16 |

## Zweck

Berater übernehmen für Diesel-Geschädigte die Anspruchsprüfung und -durchsetzung gegen Fahrzeughersteller. Nach aktuellem § 23 Nr. 1 GVG liegt die allgemeine Wertgrenze des Amtsgerichts bei 10.000 EUR einschließlich; darüber ist grundsätzlich das Landgericht zuständig (§ 71 GVG), wo Anwaltszwang gilt (§ 78 ZPO). Für vor dem 01.01.2026 anhängige Verfahren bleibt § 44 EGGVG ein Pflichtstopp; Rechtsmittelgrenzen folgen zusätzlich ihrem eigenen Übergangsrecht nach § 47 EGZPO. Nicht-anwaltliche Berater beachten ihre RDG-Grenzen.

Schwerpunkte:

- Anspruchsprüfung: großer Schadensersatz nach § 826 BGB bei Prüfstandserkennung (EA189) und Differenzschaden nach § 823 Abs. 2 BGB i.V.m. §§ 6, 27 EG-FGV bei Thermofenster und anderen fahrlässigen Verstößen
- Außergerichtliche Anspruchsstellung (Anspruchsschreiben mit Fristsetzung, Zustellungsnachweis, Vergleichsprüfung) und gerichtliche Durchsetzung (regelmäßig Schadensersatzklage; Mahnverfahren nur optional und meist ungeeignet)
- Rückabwicklung Zug um Zug beim großen Schadensersatz oder Fahrzeugerhalt beim Differenzschaden
- Musterfeststellungsklage/VDuG-Abhilfeklage gegenüber Einzelklage abwägen; Abtretung an Legal-Tech oder Prozessfinanzierer prüfen
- Klageerwiderung, Replik und Verteidigung gegen Widerklagen des Herstellers
- Kostenfestsetzung und Vollstreckung nach Urteil, Vergleich oder Kostenfestsetzungsbeschluss gegen den Hersteller
- Korrespondenz mit Autohaus, Werkstatt, Kfz-Sachverständigem, finanzierender Bank oder Leasinggeber, Hersteller-Rechtsabteilung, gegnerischem Anwalt und eigener Kanzlei

Was die Bearbeitung nicht ohne Eskalation macht: Berufung/Revision, Verjährungsstreit, Sachverständigenstreit zum Motor, hoher Streitwert und unklare Abtretung — dafür gibt es den Skill `10-vertretung-prozessfinanzierung-abtretung`.

## Installation

**Direkt aus dem öffentlichen Marketplace in Claude Code:**

```bash
claude plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
claude plugin install diesel-schadensersatz@klotzkette-german-legal-skills
```

Nach einem lokalen Klon kann das Marketplace-Verzeichnis stattdessen direkt eingebunden werden:

```bash
git clone https://github.com/Klotzkette/claude-fuer-deutsches-recht.git
cd claude-fuer-deutsches-recht
claude plugin marketplace add .
claude plugin install diesel-schadensersatz@klotzkette-german-legal-skills
```

**Manueller Plugin-Upload oder anderer Chatbot:**

1. Das [`diesel-schadensersatz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/diesel-schadensersatz.zip) aus dem aktuellen Release laden.
2. Die veröffentlichten [`checksums-sha256.txt`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/checksums-sha256.txt) prüfen.
3. Das unveränderte Plugin-ZIP in der Zielumgebung hochladen. [Schnellstart](./diesel-schadensersatz-schnellstart.md) und [Werkstatt](./diesel-schadensersatz-werkstatt.md) bleiben eigenständige Markdown-Dateien.
4. Pilotgruppe mit fachlicher Freigabeperson aktivieren und alle acht Fachfälle plus KBA-Referenzakte testen, bevor Live-Akten verarbeitet werden.

Für produktive Nutzung immer ein getaggtes Release verwenden. Branches sind Arbeitsstände und nicht der empfohlene Rollout-Stand.

## Claude Cowork

In Cowork erscheint das Plugin mit seinen 21 Skills; in Codex wird derselbe Bestand über das zusätzliche native Plugin-Manifest erkannt. Die Standalone-Prompts sind bewusst nicht Teil des Plugin-Auftritts. Das Plugin-ZIP enthält Aktenstart, Quellenleitplanken, drei Korpusabfragen, Rechtsstands-Cockpit und beA-Paketwerkzeuge. Für andere Chatbots stehen Werkstatt- und Schnellstartprompt mit denselben Kern-Gates in verdichteter Form bereit.

Für Team- oder Enterprise-Verteilung richtet eine Organisationsinhaberin oder ein Organisationsinhaber Cowork mit aktivierten Skills ein. Das Release-ZIP kann manuell hochgeladen werden und bleibt deutlich unter der Cowork-Grenze von 50 MB. Für GitHub-Synchronisierung ist ein privates oder internes Repository zu verwenden; die relative Quelle `./diesel-schadensersatz` in `marketplace.json` ist dafür vorgesehen. Automatische Cowork-Aktualisierung wird durch einen gemergten Pull Request mit erhöhter Plugin-Version ausgelöst. Nach einem direkten Push auf `main` ist in Cowork manuell **Update** anzustoßen.

## Welche Unterlagen die Bearbeitung braucht

Ein guter Upload-Satz besteht aus:

- Kaufvertrag mit Anlagen, Rechnung, Fahrzeugschein und Fahrzeug-Identifikationsnummer (FIN).
- Finanzierungs- oder Leasingvertrag samt Widerrufsinformation, sofern das Fahrzeug fremdfinanziert wurde.
- Kontoauszug oder Tilgungsplan mit Kaufpreiszahlung, Raten, Kilometerstand und Nutzungsdaten.
- KBA-Rückrufschreiben, amtlicher Rückrufcode, Bestätigung des Software-Updates und Typgenehmigungsunterlagen.
- Korrespondenz: Anspruchsschreiben, Antwort des Herstellers, Vergleichsangebot, Schreiben der Gegenseite oder deren Anwalt.
- Gerichtsunterlagen: Klage, Klageerwiderung, Verfügungen, Hinweise, Vergleich, Urteil, Kostenfestsetzungsbeschluss, Vollstreckungsunterlagen.

Unvollständige Unterlagen sind kein Abbruchgrund. Die Intake-Skills erzeugen dann eine Beleglückenliste und stellen Rückfragen an Autohaus, Werkstatt, Kfz-Sachverständigen oder finanzierende Bank.

## E-Akte- und Kanzlei-DMS-Anschluss

Für Kanzlei-DMS, Datenbankexporte, XML-Importe, Middleware und MCP-/Kontext-Gateways gilt derselbe Anschlussmodus:

1. Bei Ordnerzugriff erzeugt `tools/diesel-aktenstart.py` zuerst ein reproduzierbares Maschineninventar ohne absolute Quellpfade. Skill 01 übernimmt danach Herkunftssystem, Fremd-Aktenzeichen, Dokument-ID, Register, Exportdatum, relativen Dateipfad und Fristbezug.
2. Skill 20 erzeugt neutrale Übergabeformate: `fallakte.json`, `dms-register.csv` und `fallakte.xml` — als Import-Struktur für Kanzleisoftware wie RA-MICRO, SAP-basierte Systeme, DMS und Legal-Tech-Plattformen; bei offenen Fragen einen Mapping-Vermerk mit Rückfragen.
3. JSON und CSV führen `schema_version` 1.0.0 und werden gegen `assets/schemas/fallakte.schema.json` beziehungsweise `assets/schemas/dms-register.schema.json` geprüft. Beispiele und Vorlagen liegen unter `assets/examples/` und `assets/templates/`.
4. Originaldateien bleiben unverändert; PDF/A oder OCR-PDF wird nur als Arbeitskopie ausgewiesen.
5. Importfähigkeit wird erst grün markiert, wenn Schema, Feldmapping, Rechte, Pflichtfelder, Importweg, Testsystem, Dublettenlogik und Rückexport geprüft sind.
6. Schreibende Aktionen in Zielsystemen bleiben gesperrt, bis Freigabe, Protokollierung und Rollback geklärt sind.

## Workflow-Phasen

| Phase | Skills | Inhalt |
|---|---|---|
| 1 Aktenaufnahme | 01-05 | Kaltstart und Inventar, Kaufvertrag/Zahlungen/Belege, Chronologie und Fristen, Betroffenheit (Motor, KBA-Rückruf), Abschalteinrichtung/Thermofenster/Update |
| 2 Weichen und Vorprozessuales | 06-12 | Anspruchstriage und Fallstrategie, Verjährung/Restschadensersatz, Schadenshöhe, Anspruchsschreiben mit Zugangsnachweis, Vertretung/Prozessfinanzierung/Abtretung, Kollektivklage, Finanzierungswiderruf |
| 3 Klageentwurf | 13-15 | Klageweg/Streitwert/Zuständigkeit, Klage Rückabwicklung Zug um Zug, Klage Differenzschaden |
| 4 Prozess und Abschluss | 17-19 | Klageerwiderung/Replik/Beweis, Vergleich/Abfindung/Nachzahlung, Kosten/Vollstreckung/Monitoring |
| 5 Querschnitt | 20 | E-Akte-Export als XML, CSV, JSON für Kanzleisoftware (RA-MICRO, SAP-basiert, DMS, Legal-Tech) |
| 6 Versandabschluss | 21 -> 16 | Endfassung und Anlagenpaket prüfen; danach Signatur, tatsächliche beA-Übermittlung und gerichtliche Eingangsbestätigung |

Die Phasen sind eine Fachlandkarte, keine zwingende lineare Promptkette. Verbindlich ist der [Promptketten-Schnelllauf](./references/promptketten-schnelllauf.md): Ein valider Arbeitsstand wird wiederverwendet, der zuständige Fachskill darf direkt starten und erledigte Arbeit wird nur bei neuen Dateien, echten Widersprüchen oder geänderter Rechtslage erneut geöffnet. Höchstens zwei wirklich unabhängige Vorprüfungen laufen parallel; alle Produktions-, Frist-, Freigabe- und Versandgates bleiben bestehen.

## Schnellstart

1. Vorhandene Falldateien anhängen; die Akte darf unvollständig sein.
2. Diesen Auftrag senden:

> Neuer Diesel-Fall. Starte den Profi-Schnelllauf. Prüfe alle beigefügten Unterlagen, beginne mit Sicherheitsstopps und Fristen, stelle höchstens drei nur wirklich blockierende Fragen und liefere dann Fallkarte, Beleglücken sowie genau einen nächsten Schritt.

3. Mit dem genau einen empfohlenen Schritt fortfahren. Fallart, Klageform und Skillnummer müssen nicht vorab gewählt werden.

Der [eigenständige Schnellstart](./diesel-schadensersatz-schnellstart.md) enthält zusätzlich die Wege für beliebige Chatbots, kurze Folgeaufträge und die sichere Wiederaufnahme eines Arbeitsstands. Die [Werkstatt](./diesel-schadensersatz-werkstatt.md) führt durch die vollständige mehrstufige Bearbeitung. Bei einer neuen oder ungeordneten Akte startet das Plugin intern mit `01-kaltstart-aktenaufnahme`; dieser Skill erzeugt Startkarte, Dokumenteninventar, Fristenhinweise, Beweiswert, Lückenliste und die nächste Route. Liegt bereits ein valider Arbeitsstand vor, beginnt der verlangte Fachskill direkt.

Bei lokalem Aktenordner steht vor dem Modellaufruf ein schneller, deterministischer Lauf:

```bash
python3 "$CLAUDE_PLUGIN_ROOT/tools/diesel-aktenstart.py" /pfad/zur/akte \
  --output-dir /pfad/zum/arbeitsordner/aktenstart
```

`STARTBEREIT` erlaubt die Inhaltsaufnahme. `PRUEFUNG_NOETIG` benennt OCR-, Dubletten- oder Lückenprüfungen; `BLOCKIERT` sperrt nur die betroffenen unsicheren Dateien. Skill 01 liest anschließend `aktenstart-manifest.json`, prüft die heuristischen Kategorien am Inhalt und übernimmt Dokument-ID plus Fundstelle in die Fallakte.

Discovery-Regel: `01-kaltstart-aktenaufnahme` ist der Default für jeden neuen, ungeordneten Fall und jedes gemischte Upload-Bundle. `06-anspruchstriage-fallstrategie` startet direkt, wenn bereits eine klare Fallkarte vorliegt und die Anspruchswahl offen ist. Jeder Fachskill `02` bis `21` darf bei validem Arbeitsstand oder einem klar abgegrenzten Fachauftrag direkt starten; seine Fach- und Sicherheitsgates bleiben verbindlich. Ein bereits freigegebener Schriftsatz mit Anlagen beginnt deshalb direkt bei Skill 21.

Das Plugin routet intern nach offenen Abhängigkeiten: Nach Skill 01 werden `02`, `03` und `04` nur bei einer ergebnisrelevanten Vertrags-, Frist- oder Fahrzeuglücke zugeschaltet; `05`, `07` und `08` nur bei konkreter Technik-, Verjährungs- oder Bezifferungsfrage. Sind Fallkern und Gates belastbar, geht es unmittelbar zu Skill 06 oder in den verlangten Fachpfad. Diese Skillnummern dienen der Kontrollspur; die Bearbeiter müssen sie nicht bedienen.

Jeder Schritt soll ein bedienbares Ergebnis liefern: Ergebnis oder Engpass zuerst, Ampel, Lückenliste, Kontrollpunkte vor Versand und klare Eskalation, wenn anwaltliche Freigabe nötig ist. Tabellen sind auf echte Vergleiche mit mindestens drei Werten oder wiederkehrenden Feldern begrenzt. Die Referenz `references/bedienfuehrung-workflows.md` gibt dafür Rückfragegrenzen, Workflow-Menüs und Delta-Übergaben vor.

## Profi-Modus

Mit "Profi-Modus", "Schnelllauf", "Bulk", "nur Ergebnis", "Klagepaket", "beA fertig" oder "E-Akte fertig" verdichtet das Plugin Rückfragen und Ausgabe, nicht die Prüfung. Skill 20 erzeugt neutrale E-Akte-Exporte; Skill 21 erzeugt aus einer freigegebenen Endfassung ein kontrolliertes `original/arbeit/versand/kontrolle`-Paket. Quellenstatus, Konflikte, Fristen, Anwaltszwang, Datenschutz und Versandfreigabe bleiben harte Gates.

## Bedienmuster im Tagesgeschäft

Die folgenden Bedienmuster zeigen Abhängigkeiten, keine Pflicht zum erneuten Durchlaufen bereits erledigter Skills. Ein valider Arbeitsstand überspringt alle grünen Vorstufen; nur neue oder ergebnisrelevante Lücken lösen einen Rücksprung aus.

### Prüfstandserkennung und großer Schadensersatz

1. Skill 01 für eine neue oder ungeordnete Akte; Skills 02 und 03 nur bei offener Beleg- oder Chronologielücke.
2. Skill 04 bei offener Betroffenheit und Skill 05 nur bei konkreter Frage zur Abschalteinrichtung.
3. Skill 06 für Anspruchsgrundlage und Strategie, Skill 07 für die Verjährung, Skill 08 für die Schadenshöhe.
4. Skill 09 für Anspruchsschreiben mit Zugangsnachweis.
5. Bei fruchtlosem Fristablauf: Skill 13 für Klageweg und Streitwert, Skill 14 für die Rückabwicklungsklage, Skill 21 für Endfassung/Anlagenpaket und Skill 16 für die tatsächliche beA-Einreichung.
6. Ergebnis prüfen: Anspruchsgrundlage, Kaufpreis, Nutzungsentschädigung, Anlagen, Zinsen, Zustellung.

### Thermofenster und Differenzschaden

1. Skill 01 für eine neue oder ungeordnete Akte; Skills 02 bis 05 nur für die jeweils offene Beleg-, Frist-, Betroffenheits- oder Thermofensterfrage.
2. Skill 06 für die Strategie, Skill 08 für die Schätzung von 5 bis 15 Prozent des Kaufpreises.
3. Skill 09 für das Anspruchsschreiben, Skill 18 für ein etwaiges Vergleichsangebot.
4. Bei Klage: Skill 13 für den Klageweg, Skill 15 für die Differenzschadensklage, Skill 21 für Endfassung/Anlagenpaket und Skill 16 für die Einreichung.
5. Ergebnis prüfen: Betroffenheitsnachweis, Schätzgrundlage, Restwertanrechnung, Kostenfolge.

### EA288 mit streitiger Betroffenheit

1. Skill 04 ordnet Motor, Abgasnorm, Leistung, Abgasnachbehandlung, Typgenehmigung und Softwarestand zu; kein KBA-Treffer ist weder Legalisierung noch positiver Betroffenheitsnachweis.
2. Skill 05 behandelt Einrichtungstypen als technische Suchhypothesen und verlangt Funktion, Wirkung, Fahrzeugbezug und Beweisstatus.
3. Skill 06 trennt Fahrzeug- und Motorhersteller, Verschulden, Erwerbskausalität sowie frühe Nutzung-/Restwertaufzehrung; § 826 bleibt einer zusätzlichen Vorsatzspur vorbehalten.
4. Skill 17 nutzt Parallelvortrag nur bei belegter technischer Vergleichbarkeit und trennt verwertbare Widersprüche von nicht verifizierten Vorwürfen aus Parteimaterial.
5. Für eine fokussierte Auswahl steht `python3 "$CLAUDE_PLUGIN_ROOT/tools/ea288-corpus-query.py" --gericht Stuttgart --einrichtung umgebungsdruck --format markdown` bereit. Weitere Filter sind `--az`, `--modell`, `--norm`, `--jahr-von`, `--jahr-bis`, `--betrag-min`, `--betrag-max` und `--mit-volltext`.
6. Für höchstrichterliche Leitlinien, Gegenrechtsprechung und alle 24 OLG/KG: `python3 "$CLAUDE_PLUGIN_ROOT/tools/diesel-rechtsprechung-query.py" --query EA288 --format markdown`. Jede Fundstelle bleibt zusammen mit Status, Quellenart, Folgestatus und technischer Vergleichbarkeit zu lesen.
7. Für kleine Modellkontexte: `python3 "$CLAUDE_PLUGIN_ROOT/tools/diesel-fuenfjahre-query.py" --query EA288 --arbeitsset --format markdown`. Das Arbeitsset bleibt auf sechs Treffer mit Quellenrang, Gegenlinie und Verwendungsgrenze begrenzt.
8. Vor produktiver Quellenarbeit: `python3 "$CLAUDE_PLUGIN_ROOT/tools/rechtsstand-monitor.py" --strict --format markdown`. Eine grüne lokale Ampel bestätigt nur die Datenfrische; produktiv verwendete Volltexte und Verfahrensstände bleiben live zu prüfen.

### Klage und Prozessreaktion

1. Skill 14 oder 15 für die Klage, Skill 21 für Endfassung und Anlagenpaket, Skill 16 für Signatur und Einreichung.
2. Skill 17 wertet die Klageerwiderung aus, baut die Einwendungsmatrix, erstellt die Replik mit Beweisangeboten und wehrt Widerklagen ab; anschließend wieder Skill 21 -> Skill 16.
3. Skill 18 bewertet Vergleichssignale und verarbeitet Zahlungen nach Klageeinreichung über die Kostenpfad-Matrix.
4. Ergebnis prüfen: sekundäre Darlegungslast, Verjährungseinrede, Nutzungsvorteil, Beweislast, Vergleichsrisiko.

### beA-Versandpaket

1. Skill 21 liest Endfassung und sämtliche Anlagenbezugnahmen, fragt Gericht/Aktenzeichen/Parteirolle/Frist, letzte eingereichte K-/B-Nummer und Hausstil ab und inventarisiert alle Inputs mit SHA-256.
2. Ein strikter `bea-paketauftrag.json` bindet die freigegebene Haupt-PDF, jede Anlage, Schriftsatzfundstelle, Nummer, Bezeichnung und geplante Verarbeitung. Word-, Bild- und Scan-Inputs werden vorher als Arbeitskopie in finale PDFs überführt und visuell abgenommen.
3. `bea-paket-bauer.py` sperrt übergroße oder mehrfach per Hardlink zugeordnete Quellen vor der Produktion, erzeugt atomar `original/arbeit/versand/kontrolle`, stempelt nur Kopien, vergibt kurze ASCII-Namen und schreibt Anlagenverzeichnis, Stempel-Audits, Hashliste, Paketmanifest, Paket-Fingerprint, Prüfbericht und Freigabevorlage. Vor der Abnahme lautet der Status zwingend `FREIGABE_AUSSTEHEND`.
4. Schriftsatzbezug, sichtbarer Stempel, Dateiname und Anlagenverzeichnis werden vierfach abgeglichen. Die anwaltliche Inhalts- und Sichtfreigabe wird auf den aktuellen Paket-Fingerprint einschließlich Produktionszeitpunkt gebunden; jede spätere Datei-, Zeit- oder Metadatenänderung entwertet sie.
5. `bea-paket-pruefer.py` prüft Manifest/Freigabe, kanonische Reihenfolge auch oberhalb von 99, Hashes, tatsächliche PDF-Seitenzahlen, PDF-Struktur, aktive Inhalte, Unicode-Spoofing, Hardlinks, Symlinks/Sonderdateien, plausible Zeitstempel und die aktuelle 1.000-Dateien-/200-MB-Grenze. Nur null Fehler, null Warnungen und eine gültige Fingerprint-Freigabe ergeben `VERSANDFERTIG`.
6. Skill 16 wählt anschließend Empfänger und Nachrichtart, kontrolliert einfache/qES-Signatur und verantwortende Person, löst den persönlichen Versand aus und archiviert erst nach Prüfung der automatisierten gerichtlichen Eingangsbestätigung den Status `EINGEREICHT`.

### Kostenpfad nach Klageeinreichung

1. Bei Zahlung, Vergleichsangebot, Aufrechnung oder Wegfall des Rechtsschutzbedürfnisses nach Klageeinreichung nicht automatisch erledigen oder zurücknehmen.
2. Skill 03 trennt Klageeinreichung, Zustellung und Rechtshängigkeit; Skill 18 erkennt die Nachzahlung des Herstellers und erstellt die Kostenpfad-Matrix; Skill 17 formuliert die passende Antragsumstellung.
3. Die Matrix enthält mindestens Ereignis, Datum, vor/nach Rechtshängigkeit, vollständig/teilweise, Verzug vor Klageeinreichung, Fortbestand bei Einreichung, Kausalität der Kosten, § 91a ZPO, § 269 Abs. 3 S. 3 ZPO, Kostenfeststellung und RA-Eskalation.
4. Ampel setzen: grün bei belegtem Vorverzug und klarer Kausalität, gelb bei Beleg- oder Zeitachsenlücke, rot bei fehlendem Vorverzug oder drohendem Kostenverlust.
5. Bei unsicherem Kostenweg, streitiger Kausalität oder drohendem Kostenverlust Skill 10 einschalten, bevor eine Erklärung an das Gericht abgegeben wird.

### Kosten und Vollstreckung

1. Skill 19 führt Kostenfestsetzungsantrag, KFB-Prüfung, Forderungskonto, Vollstreckung und Monitoring in einem Pfad.
2. Bei abweisendem oder teilweise abweisendem Landgerichtsurteil keine Vollstreckung starten, sondern Tenor, Frist, Beschwer, Wert, Zulassung und Kostenrisiko als Rechtsmittel-Skizze an Skill 10 und die Stammkanzlei übergeben.
3. Bei externer Kanzlei Auftrag, Budget, Honorargrundlage, Reporting, Rechnung und Stunden-Narrative mit Skill 10 prüfen und monieren.

## Erwartete Outputs

Das Plugin soll nicht nur Text entwerfen, sondern die Akte beherrschbar machen. Typische Zwischenergebnisse sind:

- Stammdatenblatt mit Fahrzeug, Käufer:in/Halter:in, Hersteller und Bearbeitungsrolle.
- Schadensaufstellung mit Kaufpreis, Nutzungsentschädigung, Zinsen, Zeitraum und Beleganker.
- Chronologie mit Datum, Ereignis, Quelle, Frist und nächstem Schritt.
- Beleg- und Anlagenmatrix für Schriftsätze.
- Entscheidungsvermerk zu Eskalation, Mahnverfahren-Abzweigung, Klagepfad oder Vergleich.
- Kostenpfad-Matrix nach Klageeinreichung mit Rechtshängigkeit, Verzug, Kostenweg und Eskalation.
- Vollständig ausformulierter Entwurf für Anspruchsschreiben, Klage, Replik, Antrag oder Vollstreckungsauftrag.
- Rechtsmittel- und Eskalationsspur bei abweisendem oder teilweise abweisendem Urteil, getrennt von Vollstreckung.
- Kanzlei-Auftrag, Rechnungsvotum und Monierungstabelle für externe Rechtsanwälte oder Prozessfinanzierer.
- Kostenrechtsvermerk zu Kostenfestsetzungsantrag, Kostenfestsetzungsbeschluss, Streitwert, Berichtigung, Beschwerde und Frist.
- Kontrollliste für fachliche Freigabe vor Versand.
- beA-Paket mit unveränderten Originalen, gestempelten Versand-PDFs, Paketauftrag, Manifest/Fingerprint, hashgebundener Freigabe, Anlagenverzeichnis, Hashliste und technischem Prüfbericht.
- Startkarte mit Fallart, Ampel, kurzer Begründung, Frist, fehlenden Kernstücken und genau einem nächsten Schritt.

## Kontrollpunkte vor Versand

- Stimmen Namen, Anschriften, Fahrzeug-Identifikationsnummer, Vertragsnummer und Gericht?
- Sind Kaufpreis, Zahlungen, Raten und Nutzungsentschädigung nachvollziehbar?
- Gibt es Belege für jede erhebliche Tatsachenbehauptung?
- Sind Anspruchsschreiben, Zugang, Fristen und Herstellerantwort sauber dokumentiert?
- Ist die interne Kosten-Nutzen-Grenze eingehalten oder freigegeben?
- Muss wegen Berufung, Revision, Verjährungsstreit, Insolvenz des Herstellers oder Sachverständigenfrage eskaliert werden?
- Sind Datenschutz, Datenminimierung und interne Freigabe dokumentiert?
- Stimmen Anlagenbezugnahme, Stempel, Dateiname und Anlagenverzeichnis exakt überein; meldet der Paketprüfer null Fehler und Warnungen?
- Stimmen verantwortende Person, einfache/qES-Signatur und geplanter persönlicher beA-Versandweg; wird der Eingang erst nach gerichtlicher Bestätigung behauptet?

## Abnahme im Pilotbetrieb

Vor Produktivfreigabe sollte die Pilotgruppe mindestens eine Testakte je Hauptpfad bearbeiten:

1. Prüfstandserkennung bis Schadensersatzklage.
2. Thermofenster bis Differenzschaden-Anspruchsschreiben.
3. Zahlung des Herstellers nach Klageeinreichung bis Kostenpfad-Entscheidung.
4. Altfall mit offener Verjährungs- und Restschadensersatzfrage.
5. Klageerwiderung bis Replikplan.
6. Kostenfestsetzung bis Vollstreckungsmonitoring.
7. Klage oder Replik von der freigegebenen Endfassung über Skill 21 bis zum simulierten Skill-16-Eingangsnachweis.

Die fachliche Leitung prüft dabei nicht nur den Textentwurf, sondern auch Chronologie, Belegmatrix, Fristen, Eskalationsentscheidung und Kontrollliste vor Versand. Die technische Basisprüfung läuft aus der Wurzel des Zielrepositorys mit `node scripts/validate-plugin-structure.mjs`; sie ergänzt die fachliche Pilotabnahme, ersetzt sie aber nicht.

## Workflow-Prompts

Im Plugin-Verzeichnis liegen zwei vom installierten Skillbestand getrennte Steuerungs-Prompts. Ihr V2-Feldvertrag ist eigenständig lesbar; ohne Host arbeiten sie als verlustfreier Textfallback, während schema-valides V2-JSON und Hashwerte Host-/Schemaunterstützung voraussetzen:

- [diesel-schadensersatz-werkstatt.md](./diesel-schadensersatz-werkstatt.md) — Werkstatt mit Profi-Quickstart, drei Laufprofilen, aktuellem 2026-Rechtsstand, vollständiger V2-Feldgrammatik und einem Vollgate; [direkt als Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=diesel-schadensersatz/diesel-schadensersatz-werkstatt.md).
- [diesel-schadensersatz-schnellstart.md](./diesel-schadensersatz-schnellstart.md) — kompakter Einstieg für den ersten Arbeitsstand; [direkt als Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=diesel-schadensersatz/diesel-schadensersatz-schnellstart.md).

Die Release-Validatoren begrenzen den Schnellstart auf höchstens 7.500 Bytes und 7.500 Zeichen sowie die Werkstatt auf höchstens 1 MiB. Zusätzlich prüfen sie exakte Rootfelder, elf Statuscodes, sechs Kopffelder, Rechtsanker, Hash-/Reuse-Regeln, konditionale Tabellen und das Vollgate.

## Neun zentrale Testakten

Zum Dieselgate-Plugin gehören acht realitätsnahe Fachfälle und eine KBA-Referenzakte. Jede Akte ist im zentralen Testaktenbereich des Zielrepositories dokumentiert und steht als Gesamt-PDF, Originalformat-ZIP und Einzel-PDF-ZIP zur Verfügung.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Fallbild und Aktengegenstand | Gesamt-PDF | Originaldateien | Einzel-PDFs |
|---|---|---|---|
| [VW EA189 Müller: Gebrauchtwagenkauf und Rückrufunterlagen](../testakten/vw-ea189-mueller-differenzschaden/README.md) | [PDF](../testakten/vw-ea189-mueller-differenzschaden/gesamt-pdf/vw-ea189-mueller-differenzschaden_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vw-ea189-mueller-differenzschaden.zip) | [PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vw-ea189-mueller-differenzschaden-einzelpdfs.zip) |
| [Mercedes OM651 Schneider: Thermofenster und Fahrzeugnutzung](../testakten/mercedes-om651-schneider-thermofenster/README.md) | [PDF](../testakten/mercedes-om651-schneider-thermofenster/gesamt-pdf/mercedes-om651-schneider-thermofenster_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mercedes-om651-schneider-thermofenster.zip) | [PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mercedes-om651-schneider-thermofenster-einzelpdfs.zip) |
| [Audi EA288 Weber: Neuwagenkauf und Fahrzeugunterlagen](../testakten/audi-ea288-weber-neuwagen/README.md) | [PDF](../testakten/audi-ea288-weber-neuwagen/gesamt-pdf/audi-ea288-weber-neuwagen_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-audi-ea288-weber-neuwagen.zip) | [PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-audi-ea288-weber-neuwagen-einzelpdfs.zip) |
| [VW EA189 Hoffmann: Altfahrzeug und frühere Korrespondenz](../testakten/vw-ea189-hoffmann-verjaehrung-restschaden/README.md) | [PDF](../testakten/vw-ea189-hoffmann-verjaehrung-restschaden/gesamt-pdf/vw-ea189-hoffmann-verjaehrung-restschaden_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vw-ea189-hoffmann-verjaehrung-restschaden.zip) | [PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vw-ea189-hoffmann-verjaehrung-restschaden-einzelpdfs.zip) |
| [BMW Fischer: Gebrauchtwagenkauf und technische Unterlagen](../testakten/bmw-fischer-abweisungsrisiko/README.md) | [PDF](../testakten/bmw-fischer-abweisungsrisiko/gesamt-pdf/bmw-fischer-abweisungsrisiko_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bmw-fischer-abweisungsrisiko.zip) | [PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bmw-fischer-abweisungsrisiko-einzelpdfs.zip) |
| [VW Koch: Fahrzeugfinanzierung und Widerrufsunterlagen](../testakten/vw-finanzierung-koch-widerrufsjoker/README.md) | [PDF](../testakten/vw-finanzierung-koch-widerrufsjoker/gesamt-pdf/vw-finanzierung-koch-widerrufsjoker_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vw-finanzierung-koch-widerrufsjoker.zip) | [PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vw-finanzierung-koch-widerrufsjoker-einzelpdfs.zip) |
| [Fiat Bauer: Wohnmobilkauf und Beteiligtenunterlagen](../testakten/fiat-wohnmobil-bauer/README.md) | [PDF](../testakten/fiat-wohnmobil-bauer/gesamt-pdf/fiat-wohnmobil-bauer_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fiat-wohnmobil-bauer.zip) | [PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fiat-wohnmobil-bauer-einzelpdfs.zip) |
| [VW Richter: Titel, Teilzahlung und Vollstreckungsunterlagen](../testakten/vollstreckung-vw-richter-titel/README.md) | [PDF](../testakten/vollstreckung-vw-richter-titel/gesamt-pdf/vollstreckung-vw-richter-titel_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckung-vw-richter-titel.zip) | [PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckung-vw-richter-titel-einzelpdfs.zip) |
| [KBA-Rückrufregister: Codes, Quellen und FIN-Angaben](../testakten/rueckrufregister-kba/README.md) | [PDF](../testakten/rueckrufregister-kba/gesamt-pdf/rueckrufregister-kba_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rueckrufregister-kba.zip) | [PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rueckrufregister-kba-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen im zentralen Katalog](../testakten/README.md)

Für Schulungen ist das Einzel-PDF-ZIP besonders nützlich, weil es die typische Situation abbildet: viele einzelne Unterlagen, sauber benannt, aber noch nicht zu einer Prozessakte verschmolzen.

Die Akten sind nicht glattgebügelt: E-Mail-Nachträge, Dublettenhinweise, Rückrufnotizen, unscharfe Zahlungsbehauptungen und angekündigte fehlende Anlagen bilden einen realistischen Akteneingang ab. Sie enthalten keine vorweggenommene Lösung oder Freigabeentscheidung; Sachverhalt, Beweiswert, Lücken, Anspruchsweg und nächster Schritt sind eigenständig zu erarbeiten. `01-kaltstart-aktenaufnahme` erstellt bei ungeordnetem Eingang das Dokumenteninventar; `02-kaufvertrag-zahlungen-belege` und `03-chronologie-rueckruf-fristen` werden nur bei entsprechender Beleg- oder Zeitachsenlücke ergänzt. Sobald der Arbeitsstand belastbar ist, kann `06-anspruchstriage-fallstrategie` oder der konkret verlangte Fachskill direkt übernehmen.

## Quellen und Konsistenz

Das Dieselgate-Plugin ist vollständiger Bestandteil von [`claude-fuer-deutsches-recht`](../README.md) und folgt dessen Qualitätsstandards:

- Keine BeckRS-, kommerziellen juris- oder Aufsatz-Blindzitate
- Quellenstatus sichtbar; produktive Rechtsprechungszitate nur nach Live-Verifikation
- Quellenhygiene wie im Mutter-Repo
- Quellenleitplanken im Plugin-ZIP unter `references/`
- Geprüfte EuGH-/BGH-Kontrollspur, Stand 26.08.2026: [`references/gepruefte-anker-dieselgate.md`](references/gepruefte-anker-dieselgate.md)
- 133 Entscheidungen/Statusakten im exakten Fünfjahresfenster mit Quellenrang und Verwendungsgrenze: [`references/diesel-rechtsprechung-2021-2026.md`](references/diesel-rechtsprechung-2021-2026.md)
- Gesetzgebung und Übergangsrecht 2026 zu Zuständigkeit, Rechtsmitteln, eCoC, Typgenehmigungsrahmen und Euro 7: [`references/rechtsstand-2026-gesetzgebung.md`](references/rechtsstand-2026-gesetzgebung.md)
- 71-Datensätze-Matrix mit allen 24 OLG/KG auf Gerichtsebene: [`references/diesel-rechtsprechung-obergerichte.md`](references/diesel-rechtsprechung-obergerichte.md)
- KBA- und Gansel/Caba-Quellen mit Rang und Verwendungsgrenzen: [`references/behoerden-und-praxisquellen-diesel.md`](references/behoerden-und-praxisquellen-diesel.md)
- ERVV/ERVB-, Signatur-, Dateinamen- und Eingangskontrolle für Skill 21/16: [`references/bea-versandfertig.md`](references/bea-versandfertig.md)
- Verbindliche Schreib- und Argumentationsarchitektur für alle 21 Skills: [`references/juristische-schreib-und-argumentationsarchitektur.md`](references/juristische-schreib-und-argumentationsarchitektur.md)
- Projektspezifische Korpus-, Stammdaten-, ZIP- und Reproduzierbarkeitsvalidatoren
- Markdown-Skills mit YAML-Frontmatter `name` und `description`

## Lizenz

Apache-2.0 oder MIT; siehe [`LICENSE-APACHE`](../LICENSE-APACHE), [`LICENSE-MIT`](../LICENSE-MIT) und [`NOTICE`](../NOTICE) im Repository-Root.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 21 Skills in diesem Plugin. Die technische Skill-ID bleibt stabil; der Arbeitsname macht die fachliche Zuordnung lesbar. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Arbeitsname | Beschreibung |
| --- | --- | --- |
| `01-kaltstart-aktenaufnahme` | Kaltstart und Aktenaufnahme | Default für neue oder ungeordnete Dieselakten und gemischte Uploads. Sichert Dateien und Fundstellen, bildet Fallkern, Lücken und Arbeitsstand und nennt genau einen nächsten Skill. Nicht für Anspruchs- oder Klageentwürfe. |
| `02-kaufvertrag-zahlungen-belege` | Kaufvertrag, Zahlungen und Belege | Für unklare Kauf-, Finanzierungs-, Leasing-, Zahlungs-, Kilometer- oder Anlagenbelege. Rekonstruiert die beleggebundene Erwerbs- und Zahlungslage. Nicht für Anspruchswahl oder Schriftsatzproduktion. |
| `03-chronologie-rueckruf-fristen` | Chronologie, Rückruf und Fristen | Für ungeklärte Zeitfolge, Zugänge, Rückruf-, Update- oder Verfahrensdaten. Erstellt eine fundstellengebundene Chronologie und Fristenkarte. Materielle Verjährungsfragen gehen an Skill 07. |
| `04-betroffenheit-motor-kba-rueckruf` | Betroffenheit: Motor und KBA-Rückruf | Für offene Fahrzeug-, Motor-, FIN-, KBA-, Typgenehmigungs- oder Maßnahmenzuordnung. Klärt den konkreten Betroffenheitsbezug und seine Beleggrenzen. Keine Haftungsannahme allein aus Motorfamilie oder Modell. |
| `05-abschalteinrichtung-thermofenster-update` | Abschalteinrichtung, Thermofenster, Update | Für eine konkret behauptete Prüfstandserkennung, ein Thermofenster oder eine Update-Funktion. Ordnet Funktion, Unzulässigkeit, Kausalität und Update-Dreispur ein. Nicht für bloße Motor- oder Modellvermutungen. |
| `06-anspruchstriage-fallstrategie` | Anspruchstriage und Fallstrategie | Zentrale Weiche nach vorhandenem Fallkern. Wählt Anspruchsspur und wirtschaftliche Strategie, zeigt Stopps und nennt genau einen nächsten Skill. Fehlende Einzeldaten lösen nur den dafür zuständigen Fachskill aus. |
| `07-verjaehrung-restschadensersatz` | Verjährung und Restschadensersatz | Für Verjährung, Hemmung, Kenntnis, Altkauf, Update-Streitgegenstand oder Restschadensersatz. Datiert jede Anspruchsspur und prüft Paragraf 852 BGB samt Herstellerzufluss. Nicht für eine bloße Terminchronologie. |
| `08-schadenshoehe-nutzungsentschaedigung` | Schadenshöhe und Nutzungsentschädigung | Für Bezifferung, Nutzung, Restwert, Differenzschaden und Wirtschaftlichkeit. Rechnet großen Schadensersatz oder den Rahmen von 5 bis 15 Prozent samt Vorteilsausgleich und Aufzehrung. Benötigt belegte Stichtagswerte. |
| `09-anspruchsschreiben-zugangsnachweis` | Anspruchsschreiben und Zugangsnachweis | Für ein vorprozessuales, beziffertes Anspruchsschreiben an den Hersteller. Erstellt vollständigen Text, bestimmte Frist, gegebenenfalls Rückgabeangebot und Zugangsnachweis. Nicht für eine Klage oder prozessuale Replik. |
| `10-vertretung-prozessfinanzierung-abtretung` | Vertretung, Prozessfinanzierung, Abtretung | Für Anwaltszwang, RDG, Rechtsschutz, Prozessfinanzierung, Abtretung oder Kanzleiübergabe. Klärt Rolle, Vollmacht, Kostenmodell und Datenschutz. Nicht für die materielle Anspruchswahl. |
| `11-musterfeststellung-vdug-kollektivklage` | Musterfeststellung, VDuG, Kollektivklage | Für Musterfeststellung, VDuG, Abhilfeklage oder kollektiven Rechtsschutz. Prüft Anmeldung, Bindung, Hemmung und Vor- oder Nachteile gegenüber der Einzelspur. Keine automatische Empfehlung einer Sammelspur. |
| `12-finanzierungswiderruf-verbundgeschaeft` | Finanzierungswiderruf und Verbund | Für Kfz-Kredit, Leasing, Widerruf oder verbundenes Geschäft. Prüft zuerst die Vollerfüllung, dann Originalvertrag, Norm, Muster und Pflichtangabe. Hält Widerrufs- und Herstellerdeliktsspur strikt getrennt. |
| `13-klageweg-streitwert-zustaendigkeit` | Klageweg, Streitwert, Zuständigkeit | Für Klageweg, Streitwert, Kosten, Amts- oder Landgericht, örtliche Zuständigkeit und Klageform. Liefert eine Antragsempfehlung vor Skill 14 oder 15. Nicht für die eigentliche Klageschrift. |
| `14-klage-rueckabwicklung-zug-um-zug` | Klage: Rückabwicklung Zug um Zug | Für eine freigegebene Klage auf großen Schadensersatz und Rückabwicklung Zug um Zug. Erstellt Rubrum, Anträge, Sachverhalt, Subsumtion, Beweise und Anlagen vollständig. Nicht für bloßen Differenzschaden. |
| `15-klage-differenzschaden` | Klage: Differenzschaden | Für eine freigegebene, bezifferte Differenzschadensklage bei verbleibendem Fahrzeug. Erstellt Rubrum, Antrag, Streitgegenstand, Subsumtion, Beweise und Vorteilsausgleich vollständig. Keine Zug-um-Zug-Rückabwicklung. |
| `16-klage-einreichen-bea-egvp` | Klage einreichen über beA/EGVP | Nur für die tatsächliche beA- oder EGVP-Einreichung eines durch Skill 21 freigegebenen Pakets. Prüft Empfänger, Signaturweg, persönliche Übermittlung und gerichtlichen Eingang. Ohne grünes Paket zurück zu Skill 21. |
| `17-klageerwiderung-replik-beweis` | Klageerwiderung, Replik und Beweis | Für Klageerwiderung, gerichtlichen Hinweis, Widerklage oder Replik. Ordnet Einwendungen und erstellt eine vollständige Replik mit Beweisangeboten. Nicht für bloße vorgerichtliche Herstellerkorrespondenz. |
| `18-vergleich-abfindung-nachzahlung` | Vergleich, Abfindung, Nachzahlung | Für Vergleich, Abfindung oder Zahlung nach Klage. Rechnet Nettoergebnis, Kosten und Prozessfolge und formuliert bei Freigabe den Vergleich vollständig. Keine automatische Erledigung oder Klagerücknahme. |
| `19-kosten-vollstreckung-monitoring` | Kosten, Vollstreckung, Monitoring | Für Urteil, Vergleichstitel, KFA, KFB, Zahlung oder Vollstreckung. Führt Forderung, Kosten, Rechtsbehelf, Zug-um-Zug-Leistung und Wiedervorlage fort. Nicht ohne Titel oder vollstreckbare Grundlage. |
| `20-eakte-export-kanzleisoftware` | E-Akte-Export und Kanzleisoftware | Für E-Akte, DMS, Kanzleisoftware, RA-MICRO, XML, CSV oder JSON. Normalisiert oder exportiert beleggebundene Falldaten mit Schema, Mapping und Datenschutzkontrolle. Kehrt danach zum gespeicherten Fachskill zurück. |
| `21-bea-versandfertig-schriftsatz-anlagen` | Schriftsatz und Anlagen beA-versandfertig | Für eine fachlich freigegebene Endfassung mit Anlagen, die beA-versandfertig werden soll. Schützt Originale, bindet Hashes, Stempel, Namen und Fingerprint. Versendet nie selbst; erst grünes Paket geht an Skill 16. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
