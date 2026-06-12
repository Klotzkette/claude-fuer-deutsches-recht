# Prozessrecht-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`prozessrecht.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/prozessrecht.md) (110 KB)
- Im Repo: [`testakten/megaprompts/prozessrecht.md`](../testakten/megaprompts/prozessrecht.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`prozessrecht`) | [`prozessrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Kita Mühlenhof Lichtenrade - HOAI-Leistungsphasen und Bauüberwachung 2026** (`hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026`) | [Gesamt-PDF lesen](../testakten/hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026/gesamt-pdf/hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026_gesamt.pdf) | [`testakte-hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026.zip) |
| **Werkvertragsstreit Pohlmann / Saalbau Rosenheim — Baumängel, BGH-Revision, Zurückverweisung** (`zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann`) | [Gesamt-PDF lesen](../testakten/zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann/gesamt-pdf/zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann_gesamt.pdf) | [`testakte-zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Unterstützung für Prozessanwälte und Syndikusrechtsanwälte bei der Führung eines Mandatsportfolios im deutschen Zivil-, Straf-, Verwaltungs- und Arbeitsrecht. Der Kaltstart-Interview erfasst Risikobereitschaft, Mandatslandschaft und Kanzleistil – der Rahmen, gegen den jedes neue Mandat eingeordnet wird. Einheitliche Aufnahme (Intake) überführt neue Mandate in strukturierte Logeinträge und mandatsbezogene Historiendateien. Statusübersichten und Tiefenbriefings lesen aus dem Log.

Konzipiert für Anwälte, die viele Mandate gleichzeitig betreuen, von denen die meisten durch externe Kanzleien oder Korrespondenzanwälte bearbeitet werden. Dieses Plugin ist ein Denkpartner, kein Mandatsverwaltungssystem. Wenn Sie LawVu, SimpleLegal oder eine vergleichbare Software einsetzen, ersetzt dieses Plugin diese nicht – es ergänzt sie als strukturierte Argumentations- und Analyseschicht.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, markiert und abgesichert –, keine rechtliche Schlussfolgerung.** Das Plugin erledigt die Arbeit: liest die Dokumente, wendet Ihr Playbook an, findet die Probleme, entwirft das Memo. Ein Anwalt prüft, verifiziert und entscheidet. Zitate sind nach Quelle gekennzeichnet, damit klar ist, welche aus einem Recherchetool stammen und welche noch zu überprüfen sind. Mandatsgeheimnismarker werden konservativ angewendet, damit keine unbeabsichtigte Offenbarung erfolgt (§ 43a Abs. 2 BRAO, § 203 StGB). Folgenreiche Handlungen – Einreichen, Versenden, Vollstrecken – sind durch ausdrückliche Bestätigung abgesichert.

## Voraussetzungen

Einige Funktionen verweisen auf Outlook- und Kalender-Integrationen. Diese erfordern MCP-Server in Ihrer Umgebung – sie sind nicht im Plugin enthalten. Ohne sie werden Ausgaben als Dateien gespeichert:

- **Outlook MCP** – `/gegenseite-status` erstellt Outlook-Entwürfe, sofern authentifiziert; andernfalls Markdown-Entwürfe in `gegenseite-status/[JJJJ-MM-TT]/[slug].md`.
- **Kalender-MCP** – keine automatische Terminplanung enthalten. Richten Sie eine Wiederholungserinnerung ein, um wöchentliche Befehle aufzurufen.

Das Plugin funktioniert vollständig ohne beide Integrationen; diese sind additiv.

## Für wen ist das?

| Rolle | Hauptverwendung |
|---|---|
| **Prozessanwalt (Kanzlei oder Syndikus)** | Alles – Intake, Triage, Status, Historie, Briefings |
| **Stellvertretender Justiziar / leitender Syndikus** | Portfolio-Übersicht, Vorstandsberichterstattung |
| **Hauptjustiziar / Leiter Rechtsabteilung** | Schneller Portfoliostatus, Tiefeneinblick in einzelne Mandate |
| **Außenanwalt** | Per-Mandat-Verlaufsdokumentation, Schriftsatzentwürfe, Fristen |

## Anwendungsbereich

Das Plugin deckt das **deutsche Zivilprozessrecht (ZPO)** als Kernbereich ab und enthält spezialisierte Skills für:

- **Strafrecht / Strafverteidigung** – StPO, Pflichtverteidigung, Akteneinsicht
- **Digitale StPO-Ermittlungsmaßnahmen** – biometrischer Internetabgleich, KI-Analyseplattformen, Akteneinsicht, Benachrichtigung, Löschung und Verwertungsangriffe
- **Verwaltungsrecht** – VwGO, Widerspruchsverfahren
- **Arbeitsrecht** – ArbGG, einstweiliger Rechtsschutz
- **Familienrecht** – FamFG
- **Steuerrecht** – FGO, BFH
- **Sozialrecht** – SGG, BSG
- **Zwangsvollstreckung** – §§ 704 ff. ZPO
- **Einstweilige Verfügung** – §§ 935, 940 ZPO
- **Mahnverfahren** – §§ 688 ff. ZPO
- **Verkehrsunfallrecht** – StVG, § 115 VVG

Für harte ZPO-Fakten gibt es den Spezialskill `amtlicher-zpo-verfahrenscheck`. Er nutzt den aktuellen amtlichen ZPO-Normkern und trennt Zuständigkeit, Form, Zustellung, Fristen, Klage, Beweis, Mahnverfahren, Vollstreckung, Arrest und einstweilige Verfügung.

## Vorprozessuale Beweiserhebung im deutschen Recht

Informationsbeschaffung erfolgt durch:
- §§ 142, 144 ZPO (gerichtliche Urkundenvorlegung und Augenschein)
- § 810 BGB (Einsichtnahme in Urkunden)
- §§ 242, 259, 260, 666 BGB (Auskunftsansprüche)
- Art. 15 DSGVO (Auskunftsrecht)
- § 254 ZPO (Stufenklage)
- §§ 485 ff. ZPO (Selbständiges Beweisverfahren)

Zum Schutz anwaltlicher Unterlagen: § 43a Abs. 2 BRAO, § 203 StGB; Zeugnisverweigerungsrecht § 383 Abs. 1 Nr. 6 ZPO; Beschlagnahmefreiheit §§ 97, 53 StPO; Editionsverweigerung §§ 142, 383 ZPO.

Urteile sind nicht bindend (außer § 31 BVerfGG). Literatur und Kommentare sind tragende Argumentationsquellen.

## Rechtsgebiete und Verfahrensordnungen

| Verfahren | Rechtsgrundlage |
|---|---|
| Zivilprozess | ZPO, GVG, RVG, GKG |
| Strafprozess | StPO, GVG, RVG |
| Verwaltungsstreit | VwGO, VwVfG |
| Finanzgerichtsbarkeit | FGO, AO |
| Sozialgerichtsbarkeit | SGG, SGB |
| Arbeitsgerichtsbarkeit | ArbGG, KSchG |
| Familiensachen | FamFG, BGB |
| Zwangsvollstreckung | §§ 704–915h ZPO |

## Dateistruktur

```
prozessrecht/
├── CLAUDE.md              # Praxisprofil (vom Kaltstart geschrieben)
├── README.md              # Diese Datei
├── mandate/               # Pro-Mandat-Ordner: mandat.md + verlauf.md
│   └── _log.yaml          # Portfolio-Log aller Mandate
├── demand-letters/        # Ausgehende Schreiben und Entwürfe
├── inbound/               # Eingegangene Schreiben, Mahnungen, Beschlüsse
├── gegenseite-status/             # Korrespondenz mit Gegenseite / Außenanwälten
└── skills/                # Plugin-Skills (automatisch geladen)
```

## Nutzungshinweis

Alle Ausgaben des Plugins sind **Entwürfe zur anwaltlichen Prüfung**. Das Plugin ersetzt keine Rechtsberatung und trifft keine Entscheidungen. Berufsrechtliche Pflichten nach BRAO, BORA, RVG und die anwaltliche Verschwiegenheit nach § 43a Abs. 2 BRAO bleiben unberührt. Für die Überprüfung und Freigabe jedes Dokuments ist stets der verantwortliche Anwalt zuständig.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 56 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtlicher-zpo-proz-bauleiter-eilverfahren` | Amtlicher ZPO-Verfahrenscheck: ordnet Zuständigkeit, Schriftsatzform, Zustellung, Fristen, Klage, Beweis, Mahnverfahren, Vollstreckung, Arrest und einstweilige Verfügung anhand der aktuellen ZPO-Fassung im Prozessrecht. |
| `anschluss-routing` | Anschluss-Routing für Prozessrecht (ZPO/VwGO/StPO/SGG): wählt den nächsten Spezial-Skill nach Engpass (Berufung 1 Mon. § 517 ZPO, Klageschrift, Klageerwiderung, Schriftsätze), dokumentiert Router-Entscheidung mit Begründung. |
| `anspruchstabelle-beweislast` | Anspruchstabelle für zivilprozessuales Mandat erstellen: alle Ansprüche und Gegenansprüche tabellarisch erfassen. Normen: §§ 253 261 ZPO. Prüfraster: Anspruchsgrundlage, Betrag, Verjaebrung, Beweisstatus. Output: Anspruchstabelle als Gru... |
| `anspruchstabelle-gegenseite-interessen` | Anspruchstabelle: Compliance-Dokumentation und Aktenvermerk im Prozessrecht. |
| `anwaltsgeheimnis-pruefung` | Anwaltsgeheimnis und Verschwiegenheitspflicht bei Weitergabe von Mandatsinformationen prüfen. Normen: § 43a BRAO, § 203 StGB, § 102 ZPO. Prüfraster: Offenbarungsbefugnis, Zeugnisverweigerungsrecht, strafrechtliche Grenzen. Output: Prüfer... |
| `argumentationsverbesserung-red-team` | Verbessert prozessuale Argumentation in Klage, Erwiderung, Replik, Berufung, Eilantrag oder Mandatsmemo. Prüft These, Beweis, Subsumtion, Gegenargumente, Richterperspektive, Antragsfassung und Ton im Prozessrecht. |
| `beweissicherung-einstweilige-verfuegung` | Beweissicherungsantrag im selbständigen Beweisverfahren vorbereiten: Sachverständigengutachten vor Klageerhebung sichern. Normen: §§ 485 ff. ZPO. Prüfraster: Beweissicherungsinteresse, Antragstellung, Gutachterauswahl, Verfahrensablauf.... |
| `chronologie` | Sachverhaltschronologie für Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: §§ 253 138 ZPO. Prüfraster: Ereignisse, Zeitpunkte, Dokumente, Normbezug, streitige vs. unstreitige Tatsachen. Output: Tabe... |
| `dokumente-intake` | Dokumentenintake für Prozessrecht (ZPO/VwGO/StPO/SGG): sortiert Klageschrift, Klageerwiderung, Schriftsätze, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `eilverfahren-risikoampel-und-gegenargumente` | Eilverfahren: Risikoampel, Gegenargumente und Verteidigungslinien im Prozessrecht. |
| `einstieg-routing` | Einstieg, Triage und Routing für Prozessrecht (ZPO/VwGO/StPO/SGG): ordnet Rolle (Mandant, Gegner, Gericht), markiert Frist (Berufung 1 Mon. § 517 ZPO), wählt Norm (ZPO, VwGO, StPO, SGG, FGO, FamFG) und Zuständigkeit (Erste Instanz / Rech... |
| `einstweilige-verfuegung` | Antrag auf einstweilige Verfuegung zur Sicherung zivilrechtlicher Ansprüche formulieren. Normen: §§ 935 940 ZPO. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Glaubhaftmachung, Zuständigkeit, Arrest-Abgrenzung. Output: Antragsschrif... |
| `gegenseite-mehrparteien-konflikt-und-interessen` | Gegenseite: Mehrparteienkonflikt und Interessenmatrix im Prozessrecht. |
| `gegenseite-status-mahnbescheid-mahnschreiben` | Prozessualen Status der Gegenseite erfassen: Bevollmaechtigung, Zustelladresse, Insolvenzantrag, Kostensicherheit. Normen: §§ 78 85 ZPO. Prüfraster: Vertreternachweis, Prozessvollmacht, Beklagteninsolvenz, Sicherheitsleistung. Output: St... |
| `kaltstart-interview` | Prozessrechtliches Erstinterview strukturiert durchführen: Sachverhalt, Klagebegehren, Fristen, Kosten. Normen: §§ 253 261 ZPO, BRAO. Prüfraster: Anspruchsgrundlage, Zuständigkeit, Verjaebrung, Kostenrisiko. Output: Interviewprotokoll mi... |
| `mahnbescheid` | Mahnbescheid im gerichtlichen Mahnverfahren beantragen: Voraussetzungen, Formulierung, Übergang zum Streitverfahren. Normen: §§ 688 ff. ZPO. Prüfraster: Zuständigkeit Mahngericht, bestimmte Geldforderung, Widerspruchsrecht des Schuldners... |
| `mahnbescheid-dokumentenmatrix-und-lueckenliste` | Mahnbescheid: Dokumentenmatrix, Lückenliste und Nachforderung im Prozessrecht. |
| `mahnschreiben-aufnahme` | Erhaltenes Mahnschreiben der Gegenseite aufnehmen und einordnen: Anerkennungsgefahr, Verjaebrungshemmung. Normen: §§ 204 212 BGB, § 93 ZPO. Prüfraster: Fristenlauf, Anerkennungsrisiko, Reaktionsoptionen. Output: Einordnungsnotiz und Empf... |
| `mahnschreiben-entwurf-anwaltsgeheimnis` | Vorgerichtliches Mahnschreiben entwerfen: Zahlungsaufforderung mit Frist und Klageankündigung. Normen: §§ 286 288 BGB, §§ 204 ff. BGB. Prüfraster: Verjaebrungshemmung, Verzugsbeginn, Schadensersatz, Klageandrohung. Output: Mahnschreiben-... |
| `mahnschreiben-erhalten-aktualisierung` | Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: §§ 286 287 BGB, §§ 203 204 BGB. Prüfraster: Forderungsprüfung, Verjaebrungsrisiko, Verteidigungsoptionen. Output: Antwort... |
| `mandat-aktualisierung` | Laufendes Prozessmandat aktualisieren: neue Schriftsaetze, Beschlüsse, Fristen eintragen. Normen: §§ 233 ff. ZPO. Prüfraster: Fristverfolgung, Sachstandsaktualisierung, offene Handlungspunkte. Output: Aktualisiertes Mandats-Protokoll. A... |
| `mandat-arbeitsbereich` | Digitaler Arbeitsbereich für Prozessmandate: Dokumentenablage, Aufgabenverteilung, Fristentracking. Normen: ZPO, BRAO. Prüfraster: Dokumentenstruktur, Aufgabenliste, Fristverwaltung. Output: Mandats-Arbeitsbereich-Struktur. Abgrenzung: n... |
| `mandat-arbeitsbereich-abschnitt` | Prozessrechtliche Strategie im laufenden Verfahren anpassen: Klageaenderung, Widerklage, Rücknahme. Normen: §§ 263 264 269 ZPO. Prüfraster: Klageaenderungsvoraussetzungen, Rücknahmefolgen, Widerklagemöglichkeiten. Output: Strategieanpass... |
| `mandat-aufnahme` | Prozessmandat aufnehmen: Sachverhalt erfassen, Zuständigkeit prüfen, Klagekonzept skizzieren. Normen: §§ 253 261 ZPO, BRAO. Prüfraster: Sachverhaltserfassung, Anspruchsgrundlage, Zuständigkeit, Kosten-Risiko-Analyse. Output: Mandatsaufna... |
| `mandat-briefing-schliessen-portfolio-status` | Mandantenbriefing für Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen. Normen: §§ 373 ff. ZPO. Prüfraster: Beweislast, Zeugenvorbereitung, Verhandlungsstrategien. Output: Briefingdokument für Mandanten vor Termin. Abgr... |
| `mandat-mandate-prozessrecht` | Mandat: Formular, Portal und Einreichungslogik im Prozessrecht. |
| `mandat-schliessen` | Mandat nach Prozessabschluss formal schließen: Kostenfestsetzung, Archivierung, Mandanteninformation. Normen: §§ 103 ff. ZPO, RVG. Prüfraster: Kostenfestsetzungsantrag, Ergebnismitteilung, Handaktenfreigabe. Output: Abschlussbericht Mand... |
| `mandate-tatbestand-beweis-und-belege` | Mandate: Tatbestandsmerkmale, Beweisfragen und Beleglage im Prozessrecht. |
| `output-waehlen` | Output-Wahl für Prozessrecht (ZPO/VwGO/StPO/SGG): stimmt Adressat (Mandant, Gegner, Gericht), Frist (Berufung 1 Mon. § 517 ZPO) und Form auf den Zweck ab — typische Outputs: Klage, Klageerwiderung, Beweisantrag. |
| `portfolio-status` | Statusuebersicht aller laufenden Prozessmandate: Fristen, Verfahrensstand, naechste Schritte. Normen: ZPO, RVG. Prüfraster: Fristenliste, offene Anträge, Termine, Mahnfristen. Output: Portfolio-Statusbericht Prozessmandate. Abgrenzung: n... |
| `proz-beweismittel-leitfaden-mediationsklage` | Leitfaden Beweismittel ZPO: Urkundenbeweis, Zeugenbeweis, Sachverstaendigenbeweis, Parteivernehmung, Augenscheinsbeweis. Prüfraster für Beweisangebot im Prozessrecht. |
| `proz-mediationsklage-guete-spezial` | Spezialfall obligatorisches Gueteverfahren § 15a EGZPO und Mediation: zuständige Stelle, Verlauf, Vergleich, Folgen. Prüfraster für Klägervorbereitung im Prozessrecht. |
| `proz-prozessfinanzierung-spezial` | Spezialfall Prozessfinanzierung: Anbieter, Quotenmodelle, RDG-Implikationen, Berufsrecht. Prüfraster für Mandant und Anwalt im Prozessrecht. |
| `proz-quellenkarte` | Proz Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `proz-zustaendigkeit-bauleiter` | Bauleiter Zuständigkeit ZPO: sachlich, oertlich, funktionell, internationale Zuständigkeit. Prüfraster typische Klagearten im Prozessrecht. |
| `prozessrecht-verhandlung-vergleich-und-eskalation` | Prozessrecht: Verhandlung, Vergleich und Eskalation im Prozessrecht. |
| `prozessrechtliche-schriftsaetze-status` | Prozessrechtliche: Erstprüfung, Rollenklärung und Mandatsziel im Prozessrecht. |
| `quellen-livecheck` | Quellen-Live-Check für Prozessrecht (ZPO/VwGO/StPO/SGG): prüft Normen (ZPO, VwGO, StPO, SGG, FGO, FamFG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Erste Instanz / Rechtsmittelgerichte und Quellenhygiene nach... |
| `schriftsaetze-schriftsatz-brief-und-memo-bausteine` | Schriftsaetze: Schriftsatz-, Brief- und Memo-Bausteine im Prozessrecht. |
| `schriftsatz-abschnitt` | Einzelne Abschnitte eines Schriftsatzes erstellen: Tatbestand, Begründung, Beweisangebot nach ZPO-Schema. Normen: §§ 253 313 ZPO. Prüfraster: Schluessigskeit, Beweisangebot, Normzitat. Output: Schriftsatz-Abschnitt für Einbau in Klagesch... |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Prozessrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-U... |
| `status-internationaler-bezug-und-schnittstellen` | Status: Internationaler Bezug und Schnittstellen im Prozessrecht. |
| `stpo-biometrischer-internetabgleich-und-ki-ermittlung` | StPO-Spezialprüfung zu digitalen Ermittlungsmaßnahmen: § 98d StPO-E biometrischer Internetabgleich, § 98e StPO-E Analyseplattform, § 101 StPO-E Benachrichtigung, §§ 161 163 StPO als Grenzen manueller OSINT, KI-VO-Hochrisiko, Grundrechte,... |
| `strafverteidigung-ersttermin` | Ersttermin bei Strafverteidigung vorbereiten: Akteneinsicht, Schweigepflicht, prozessuale Schritte. Normen: §§ 137 147 StPO. Prüfraster: Akteneinsichtsrecht, Mandatsverhältnis, erste Verteidigungsoptionen. Output: Checkliste Ersttermin S... |
| `streitwert-verkehrsunfall-vollstreckung` | Streitwert für zivilrechtliche Klagen berechnen: Hauptforderung, Nebenforderungen, Gerichts- und Anwaltsgebühren. Normen: §§ 3 9 ZPO, GKG, RVG. Prüfraster: Streitwertbemessung, Nebenforderungen, Kostenfolge. Output: Streitwertberechnung... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Prozessrecht (ZPO/VwGO/StPO/SGG): trennt fehlende Tatsachen von fehlenden Belegen (Klageschrift, Klageerwiderung, Schriftsätze), nennt pro Lücke Beweisthema, Beschaffungsweg (Erste Instanz / Rechtsmittel... |
| `verfahrensart-rechtsweg` | Fristen: Fristen, Form, Zuständigkeit und Rechtsweg im Prozessrecht. |
| `verfahrensart-rechtsweg-zustaendigkeit` | Verfahrensart, Rechtsweg und Zuständigkeit als Startweiche: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Prozessrecht. |
| `verkehrsunfall` | Verkehrsunfall-Mandat im Zivilprozess vorbereiten: Schadensersatz, Schmerzensgeld, Versicherungskorrespondenz. Normen: §§ 7 18 StVG, §§ 823 253 BGB, § 115 VVG. Prüfraster: Haftungsquote, Schadensposten, Verjaebrung, Regulierungsablauf. O... |
| `vollstreckung` | Zwangsvollstreckung aus Zivilurteil vorbereiten und einleiten: Pfaendung, Sachpfaendung, Forderungspfaendung. Normen: §§ 704 ff. ZPO. Prüfraster: vollstreckbarer Titel, Klausel, Zustellungsnachweis, Vollstreckungsarten. Output: Vollstrec... |
| `vollstreckung-stpo-biometrischer` | Vollstreckung: Behörden-, Gerichts- oder Registerweg im Prozessrecht. |
| `vorlageanordnung-zeuge-vorbereitung` | Vorlageanordnung nach § 142 ZPO beantragen: Vorlage von Urkunden durch Gegner oder Dritte. Normen: §§ 142 143 ZPO. Prüfraster: urkundliche Beweise, Pflicht zur Vorlage, Sanktionen bei Weigerung. Output: Antrag auf Urkundenvorlageanordnun... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Prozessrecht. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Prozessrecht. |
| `zeuge-vorbereitung` | Zeuge für Gerichtstermin vorbereiten: Aussagerecht, Zeugnisverweigerung, Vernehmungsablauf. Normen: §§ 373 ff. 383 ff. ZPO. Prüfraster: Zeugnisverweigerungsrecht, Glaubwürdigkeitsfragen, Vernehmungsthemen. Output: Zeugenvorbereitungsprot... |
| `zustaendigkeit-zahlen-schwellen-und-berechnung` | Zuständigkeit: Zahlen, Schwellenwerte und Berechnung im Prozessrecht. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
