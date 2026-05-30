# Prozessrecht-Plugin

Unterstützung für Prozessanwälte und Syndikusrechtsanwälte bei der Führung eines Mandatsportfolios im deutschen Zivil-, Straf-, Verwaltungs- und Arbeitsrecht. Der Kaltstart-Interview erfasst Risikobereitschaft, Mandatslandschaft und Kanzleistil – der Rahmen, gegen den jedes neue Mandat eingeordnet wird. Einheitliche Aufnahme (Intake) überführt neue Mandate in strukturierte Logeinträge und mandatsbezogene Historiendateien. Statusübersichten und Tiefenbriefings lesen aus dem Log.

Konzipiert für Anwälte, die viele Mandate gleichzeitig betreuen, von denen die meisten durch externe Kanzleien oder Korrespondenzanwälte bearbeitet werden. Dieses Plugin ist ein Denkpartner, kein Mandatsverwaltungssystem. Wenn Sie LawVu, SimpleLegal oder eine vergleichbare Software einsetzen, ersetzt dieses Plugin diese nicht – es ergänzt sie als strukturierte Argumentations- und Analyseschicht.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, markiert und abgesichert –, keine rechtliche Schlussfolgerung.** Das Plugin erledigt die Arbeit: liest die Dokumente, wendet Ihr Playbook an, findet die Probleme, entwirft das Memo. Ein Anwalt prüft, verifiziert und entscheidet. Zitate sind nach Quelle gekennzeichnet, damit klar ist, welche aus einem Recherchetool stammen und welche noch zu überprüfen sind. Mandatsgeheimnismarker werden konservativ angewendet, damit keine unbeabsichtigte Offenbarung erfolgt (§ 43a Abs. 2 BRAO, § 203 StGB). Folgenreiche Handlungen – Einreichen, Versenden, Vollstrecken – sind durch ausdrückliche Bestätigung abgesichert.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Prozessrecht (`prozessrecht`, dieses Plugin) | [prozessrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


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
- **Verwaltungsrecht** – VwGO, Widerspruchsverfahren
- **Arbeitsrecht** – ArbGG, einstweiliger Rechtsschutz
- **Familienrecht** – FamFG
- **Steuerrecht** – FGO, BFH
- **Sozialrecht** – SGG, BSG
- **Zwangsvollstreckung** – §§ 704 ff. ZPO
- **Einstweilige Verfügung** – §§ 935, 940 ZPO
- **Mahnverfahren** – §§ 688 ff. ZPO
- **Verkehrsunfallrecht** – StVG, § 115 VVG

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

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 26 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Prozessrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei D... |
| `anspruchstabelle` | Anspruchstabelle für zivilprozessuales Mandat erstellen: alle Ansprüche und Gegenansprüche tabellarisch erfassen. Normen: §§ 253 261 ZPO. Prüfraster: Anspruchsgrundlage, Betrag, Verjaebrung, Beweisstatus. Output: Anspruchstabelle als Gru... |
| `anwaltsgeheimnis-pruefung` | Anwaltsgeheimnis und Verschwiegenheitspflicht bei Weitergabe von Mandatsinformationen prüfen. Normen: § 43a BRAO, § 203 StGB, § 102 ZPO. Prüfraster: Offenbarungsbefugnis, Zeugnisverweigerungsrecht, strafrechtliche Grenzen. Output: Prüfer... |
| `beweissicherung` | Beweissicherungsantrag im selbständigen Beweisverfahren vorbereiten: Sachverständigengutachten vor Klageerhebung sichern. Normen: §§ 485 ff. ZPO. Prüfraster: Beweissicherungsinteresse, Antragstellung, Gutachterauswahl, Verfahrensablauf.... |
| `chronologie` | Sachverhaltschronologie für Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: §§ 253 138 ZPO. Prüfraster: Ereignisse, Zeitpunkte, Dokumente, Normbezug, streitige vs. unstreitige Tatsachen. Output: Tabe... |
| `einstweilige-verfuegung` | Antrag auf einstweilige Verfuegung zur Sicherung zivilrechtlicher Ansprüche formulieren. Normen: §§ 935 940 ZPO. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Glaubhaftmachung, Zuständigkeit, Arrest-Abgrenzung. Output: Antragsschrif... |
| `gegenseite-status` | Prozessualen Status der Gegenseite erfassen: Bevollmaechtigung, Zustelladresse, Insolvenzantrag, Kostensicherheit. Normen: §§ 78 85 ZPO. Prüfraster: Vertreternachweis, Prozessvollmacht, Beklagteninsolvenz, Sicherheitsleistung. Output: St... |
| `mahnbescheid` | Mahnbescheid im gerichtlichen Mahnverfahren beantragen: Voraussetzungen, Formulierung, Übergang zum Streitverfahren. Normen: §§ 688 ff. ZPO. Prüfraster: Zuständigkeit Mahngericht, bestimmte Geldforderung, Widerspruchsrecht des Schuldners... |
| `mahnschreiben-aufnahme` | Erhaltenes Mahnschreiben der Gegenseite aufnehmen und einordnen: Anerkennungsgefahr, Verjaebrungshemmung. Normen: §§ 204 212 BGB, § 93 ZPO. Prüfraster: Fristenlauf, Anerkennungsrisiko, Reaktionsoptionen. Output: Einordnungsnotiz und Empf... |
| `mahnschreiben-entwurf` | Vorgerichtliches Mahnschreiben entwerfen: Zahlungsaufforderung mit Frist und Klageankündigung. Normen: §§ 286 288 BGB, §§ 204 ff. BGB. Prüfraster: Verjaebrungshemmung, Verzugsbeginn, Schadensersatz, Klageandrohung. Output: Mahnschreiben-... |
| `mahnschreiben-erhalten` | Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: §§ 286 287 BGB, §§ 203 204 BGB. Prüfraster: Forderungsprüfung, Verjaebrungsrisiko, Verteidigungsoptionen. Output: Antwort... |
| `mandat-aktualisierung` | Laufendes Prozessmandat aktualisieren: neue Schriftsaetze, Beschluesse, Fristen eintragen. Normen: §§ 233 ff. ZPO. Prüfraster: Fristverfolgung, Sachstandsaktualisierung, offene Handlungspunkte. Output: Aktualisiertes Mandats-Protokoll. A... |
| `mandat-aufnahme` | Prozessmandat aufnehmen: Sachverhalt erfassen, Zuständigkeit prüfen, Klagekonzept skizzieren. Normen: §§ 253 261 ZPO, BRAO. Prüfraster: Sachverhaltserfassung, Anspruchsgrundlage, Zuständigkeit, Kosten-Risiko-Analyse. Output: Mandatsaufna... |
| `mandat-briefing` | Mandantenbriefing für Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen. Normen: §§ 373 ff. ZPO. Prüfraster: Beweislast, Zeugenvorbereitung, Verhandlungsstrategien. Output: Briefingdokument für Mandanten vor Termin. Abgr... |
| `mandat-schliessen` | Mandat nach Prozessabschluss formal schließen: Kostenfestsetzung, Archivierung, Mandanteninformation. Normen: §§ 103 ff. ZPO, RVG. Prüfraster: Kostenfestsetzungsantrag, Ergebnismitteilung, Handaktenfreigabe. Output: Abschlussbericht Mand... |
| `portfolio-status` | Statusuebersicht aller laufenden Prozessmandate: Fristen, Verfahrensstand, naechste Schritte. Normen: ZPO, RVG. Prüfraster: Fristenliste, offene Anträge, Termine, Mahnfristen. Output: Portfolio-Statusbericht Prozessmandate. Abgrenzung: n... |
| `prozessrecht-anpassen` | Prozessrechtliche Strategie im laufenden Verfahren anpassen: Klageaenderung, Widerklage, Rücknahme. Normen: §§ 263 264 269 ZPO. Prüfraster: Klageaenderungsvoraussetzungen, Rücknahmefolgen, Widerklagemöglichkeiten. Output: Strategieanpass... |
| `prozessrecht-kaltstart-interview` | Prozessrechtliches Erstinterview strukturiert durchführen: Sachverhalt, Klagebegehren, Fristen, Kosten. Normen: §§ 253 261 ZPO, BRAO. Prüfraster: Anspruchsgrundlage, Zuständigkeit, Verjaebrung, Kostenrisiko. Output: Interviewprotokoll mi... |
| `prozessrecht-mandat-arbeitsbereich` | Digitaler Arbeitsbereich für Prozessmandate: Dokumentenablage, Aufgabenverteilung, Fristentracking. Normen: ZPO, BRAO. Prüfraster: Dokumentenstruktur, Aufgabenliste, Fristverwaltung. Output: Mandats-Arbeitsbereich-Struktur. Abgrenzung: n... |
| `schriftsatz-abschnitt` | Einzelne Abschnitte eines Schriftsatzes erstellen: Tatbestand, Begründung, Beweisangebot nach ZPO-Schema. Normen: §§ 253 313 ZPO. Prüfraster: Schluessigskeit, Beweisangebot, Normzitat. Output: Schriftsatz-Abschnitt für Einbau in Klagesch... |
| `strafverteidigung-ersttermin` | Ersttermin bei Strafverteidigung vorbereiten: Akteneinsicht, Schweigepflicht, prozessuale Schritte. Normen: §§ 137 147 StPO. Prüfraster: Akteneinsichtsrecht, Mandatsverhältnis, erste Verteidigungsoptionen. Output: Checkliste Ersttermin S... |
| `streitwert` | Streitwert für zivilrechtliche Klagen berechnen: Hauptforderung, Nebenforderungen, Gerichts- und Anwaltsgebühren. Normen: §§ 3 9 ZPO, GKG, RVG. Prüfraster: Streitwertbemessung, Nebenforderungen, Kostenfolge. Output: Streitwertberechnung... |
| `verkehrsunfall` | Verkehrsunfall-Mandat im Zivilprozess vorbereiten: Schadensersatz, Schmerzensgeld, Versicherungskorrespondenz. Normen: §§ 7 18 StVG, §§ 823 253 BGB, § 115 VVG. Prüfraster: Haftungsquote, Schadensposten, Verjaebrung, Regulierungsablauf. O... |
| `vollstreckung` | Zwangsvollstreckung aus Zivilurteil vorbereiten und einleiten: Pfaendung, Sachpfaendung, Forderungspfaendung. Normen: §§ 704 ff. ZPO. Prüfraster: vollstreckbarer Titel, Klausel, Zustellungsnachweis, Vollstreckungsarten. Output: Vollstrec... |
| `vorlageanordnung` | Vorlageanordnung nach § 142 ZPO beantragen: Vorlage von Urkunden durch Gegner oder Dritte. Normen: §§ 142 143 ZPO. Prüfraster: urkundliche Beweise, Pflicht zur Vorlage, Sanktionen bei Weigerung. Output: Antrag auf Urkundenvorlageanordnun... |
| `zeuge-vorbereitung` | Zeuge für Gerichtstermin vorbereiten: Aussagerecht, Zeugnisverweigerung, Vernehmungsablauf. Normen: §§ 373 ff. 383 ff. ZPO. Prüfraster: Zeugnisverweigerungsrecht, Glaubwürdigkeitsfragen, Vernehmungsthemen. Output: Zeugenvorbereitungsprot... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
