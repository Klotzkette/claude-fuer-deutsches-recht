# Prozessrecht-Plugin

Unterstützung für Prozessanwälte und Syndikusrechtsanwälte bei der Führung eines Mandatsportfolios im deutschen Zivil-, Straf-, Verwaltungs- und Arbeitsrecht. Der Cold-Start-Interview erfasst Risikobereitschaft, Mandatslandschaft und Kanzleistil – der Rahmen, gegen den jedes neue Mandat eingeordnet wird. Einheitliche Aufnahme (Intake) überführt neue Mandate in strukturierte Logeinträge und mandatsbezogene Historiendateien. Statusübersichten und Tiefenbriefings lesen aus dem Log.

Konzipiert für Anwälte, die viele Mandate gleichzeitig betreuen, von denen die meisten durch externe Kanzleien oder Korrespondenzanwälte bearbeitet werden. Dieses Plugin ist ein Denkpartner, kein Mandatsverwaltungssystem. Wenn Sie LawVu, SimpleLegal oder eine vergleichbare Software einsetzen, ersetzt dieses Plugin diese nicht – es ergänzt sie als strukturierte Argumentations- und Analyseschicht.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, markiert und abgesichert –, keine rechtliche Schlussfolgerung.** Das Plugin erledigt die Arbeit: liest die Dokumente, wendet Ihr Playbook an, findet die Probleme, entwirft das Memo. Ein Anwalt prüft, verifiziert und entscheidet. Zitate sind nach Quelle gekennzeichnet, damit klar ist, welche aus einem Recherchetool stammen und welche noch zu überprüfen sind. Mandatsgeheimnismarker werden konservativ angewendet, damit keine unbeabsichtigte Offenbarung erfolgt (§ 43a Abs. 2 BRAO, § 203 StGB). Folgenreiche Handlungen – Einreichen, Versenden, Vollstrecken – sind durch ausdrückliche Bestätigung abgesichert.

## Voraussetzungen

Einige Funktionen verweisen auf Outlook- und Kalender-Integrationen. Diese erfordern MCP-Server in Ihrer Umgebung – sie sind nicht im Plugin enthalten. Ohne sie werden Ausgaben als Dateien gespeichert:

- **Outlook MCP** – `/gegenseite-status` erstellt Outlook-Entwürfe, sofern authentifiziert; andernfalls Markdown-Entwürfe in `oc-status/[JJJJ-MM-TT]/[slug].md`.
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
├── CLAUDE.md              # Praxisprofil (vom Cold-Start geschrieben)
├── README.md              # Diese Datei
├── matters/               # Pro-Mandat-Ordner: matter.md + history.md
│   └── _log.yaml          # Portfolio-Log aller Mandate
├── demand-letters/        # Ausgehende Schreiben und Entwürfe
├── inbound/               # Eingegangene Schreiben, Mahnungen, Beschlüsse
├── oc-status/             # Korrespondenz mit Gegenseite / Außenanwälten
└── skills/                # Plugin-Skills (automatisch geladen)
```

## Nutzungshinweis

Alle Ausgaben des Plugins sind **Entwürfe zur anwaltlichen Prüfung**. Das Plugin ersetzt keine Rechtsberatung und trifft keine Entscheidungen. Berufsrechtliche Pflichten nach BRAO, BORA, RVG und die anwaltliche Verschwiegenheit nach § 43a Abs. 2 BRAO bleiben unberührt. Für die Überprüfung und Freigabe jedes Dokuments ist stets der verantwortliche Anwalt zuständig.
