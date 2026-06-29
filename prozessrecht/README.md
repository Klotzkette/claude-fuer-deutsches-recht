# Prozessrecht-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prozessrechtliche Skills für Mandate, Fristen, Mahnbescheid, Eilverfahren, Vollstreckung und Schriftsätze.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`prozessrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht-werkstatt.md" download><code>prozessrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht-schnellstart.md" download><code>prozessrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hoai-leistungsphasen-kita-muehlenhof-lichtenrade-2026.zip) (Kita Mühlenhof Lichtenrade - HOAI-Leistungsphasen und Bauüberwachung 2026); [`testakte-zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann.zip) (Werkvertragsstreit Pohlmann / Saalbau Rosenheim — Baumängel, BGH-Revision, Zurückverweisung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
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

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 64 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtlicher-zpo-proz-bauleiter-eilverfahren` | Amtlicher ZPO-Verfahrenscheck: ordnet Zuständigkeit, Schriftsatzform, Zustellung, Fristen, Klage, Beweis, Mahnverfahren, Vollstreckung, Arrest und einstweilige Verfügung anhand der aktuellen ZPO-Fassung im Prozessrecht. |
| `anschluss-routing` | Anschluss-Routing für Prozessrecht (ZPO/VwGO/StPO/SGG): wählt den nächsten Spezial-Skill nach Engpass (Berufung 1 Mon. Paragraf 517 ZPO, Klageschrift, Klageerwiderung, Schriftsätze), dokumentiert Router-Entscheidung mit Begründung. |
| `anspruchstabelle` | Anspruchstabelle fuer Zivilprozesse erstellen: Anspruchsgrundlagen, Tatsachen, Beweisangebote, Einwendungen, Fristen, Streitwert und Schriftsatzfundstellen tabellarisch ordnen und in eine prozessuale Arbeitsliste ueberfuehren. |
| `anspruchstabelle-beweislast` | Anspruchstabelle für zivilprozessuales Mandat erstellen: alle Ansprüche und Gegenansprüche tabellarisch erfassen. Normen: Paragrafen 253 261 ZPO. Prüfraster: Anspruchsgrundlage, Betrag, Verjaebrung, Beweisstatus. Output: Anspruchstabelle... |
| `anspruchstabelle-gegenseite-interessen` | Anspruchstabelle: Compliance-Dokumentation und Aktenvermerk im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `anwaltsgeheimnis-pruefung` | Anwaltsgeheimnis und Verschwiegenheitspflicht bei Weitergabe von Mandatsinformationen prüfen. Normen: Paragraf 43a BRAO, Paragraf 203 StGB, Paragraf 102 ZPO. Prüfraster: Offenbarungsbefugnis, Zeugnisverweigerungsrecht, strafrechtliche Gr... |
| `argumentationsverbesserung-red-team` | Verbessert prozessuale Argumentation in Klage, Erwiderung, Replik, Berufung, Eilantrag oder Mandatsmemo. Prüft These, Beweis, Subsumtion, Gegenargumente, Richterperspektive, Antragsfassung und Ton im Prozessrecht. |
| `bea-wiedereinsetzung-ersatzeinreichung-2026` | Prozessrechtlicher Spezialskill zu beA-Störung, Ersatzeinreichung, Wiedereinsetzung und Glaubhaftmachung nach aktueller BGH-Rechtsprechung 2025/2026. |
| `beweissicherung-einstweilige-verfuegung` | Beweissicherungsantrag im selbständigen Beweisverfahren vorbereiten: Sachverständigengutachten vor Klageerhebung sichern. Normen: Paragrafen 485 ff. ZPO. Prüfraster: Beweissicherungsinteresse, Antragstellung, Gutachterauswahl, Verfahrens... |
| `chronologie` | Sachverhaltschronologie für Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: Paragrafen 253 138 ZPO. Prüfraster: Ereignisse, Zeitpunkte, Dokumente, Normbezug, streitige vs. unstreitige Tatsachen. Outp... |
| `dokumente-intake` | Dokumentenintake für Prozessrecht (ZPO/VwGO/StPO/SGG): sortiert Klageschrift, Klageerwiderung, Schriftsätze, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis Paragraf 43a BRAO. |
| `eilverfahren-risikoampel-und-gegenargumente` | Eilverfahren: Risikoampel, Gegenargumente und Verteidigungslinien im Prozessrecht. |
| `einstieg-routing` | Einstieg, Triage und Routing für Prozessrecht (ZPO/VwGO/StPO/SGG): ordnet Rolle (Mandant, Gegner, Gericht), markiert Frist (Berufung 1 Mon. Paragraf 517 ZPO), wählt Norm (ZPO, VwGO, StPO, SGG, FGO, FamFG) und Zuständigkeit (Erste Instanz... |
| `einstweilige-verfuegung` | Antrag auf einstweilige Verfuegung zur Sicherung zivilrechtlicher Ansprüche formulieren. Normen: Paragrafen 935 940 ZPO. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Glaubhaftmachung, Zuständigkeit, Arrest-Abgrenzung. Output: Antra... |
| `gegenseite-mehrparteien-konflikt-und-interessen` | Gegenseite: Mehrparteienkonflikt und Interessenmatrix im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `gegenseite-status-mahnbescheid-mahnschreiben` | Prozessualen Status der Gegenseite erfassen: Bevollmaechtigung, Zustelladresse, Insolvenzantrag, Kostensicherheit. Normen: Paragrafen 78 85 ZPO. Prüfraster: Vertreternachweis, Prozessvollmacht, Beklagteninsolvenz, Sicherheitsleistung. Ou... |
| `kaltstart-interview` | Prozessrechtliches Erstinterview strukturiert durchführen: Sachverhalt, Klagebegehren, Fristen, Kosten. Normen: Paragrafen 253 261 ZPO, BRAO. Prüfraster: Anspruchsgrundlage, Zuständigkeit, Verjaebrung, Kostenrisiko. Output: Interviewprot... |
| `kostenfeststellungsklage-verzugsschaden-erledigung` | Kostenfeststellungsklage nach Erledigung des ursprünglichen Klagebegehrens: Wahl zwischen Paragraf 91a ZPO, Paragraf 269 Abs. 3 S. 3 ZPO und materiell-rechtlicher Kostenerstattung als Verzugsschaden nach Paragrafen 280 und 286 BGB. Prüft... |
| `mahnbescheid` | Mahnbescheid im gerichtlichen Mahnverfahren beantragen: Voraussetzungen, Formulierung, Übergang zum Streitverfahren. Normen: Paragrafen 688 ff. ZPO. Prüfraster: Zuständigkeit Mahngericht, bestimmte Geldforderung, Widerspruchsrecht des Sc... |
| `mahnbescheid-dokumentenmatrix-und-lueckenliste` | Mahnbescheid: Dokumentenmatrix, Lückenliste und Nachforderung im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `mahnschreiben-aufnahme` | Erhaltenes Mahnschreiben der Gegenseite aufnehmen und einordnen: Anerkennungsgefahr, Verjaebrungshemmung. Normen: Paragrafen 204 212 BGB, Paragraf 93 ZPO. Prüfraster: Fristenlauf, Anerkennungsrisiko, Reaktionsoptionen. Output: Einordnung... |
| `mahnschreiben-entwurf-anwaltsgeheimnis` | Vorgerichtliches Mahnschreiben entwerfen: Zahlungsaufforderung mit Frist und Klageankündigung. Normen: Paragrafen 286 288 BGB, Paragrafen 204 ff. BGB. Prüfraster: Verjaebrungshemmung, Verzugsbeginn, Schadensersatz, Klageandrohung. Output... |
| `mahnschreiben-erhalten-aktualisierung` | Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: Paragrafen 286 287 BGB, Paragrafen 203 204 BGB. Prüfraster: Forderungsprüfung, Verjaebrungsrisiko, Verteidigungsoptionen.... |
| `mandat-aktualisierung` | Laufendes Prozessmandat aktualisieren: neue Schriftsaetze, Beschluesse, Fristen eintragen. Normen: Paragrafen 233 ff. ZPO. Prüfraster: Fristverfolgung, Sachstandsaktualisierung, offene Handlungspunkte. Output: Aktualisiertes Mandats-Prot... |
| `mandat-arbeitsbereich` | Digitaler Arbeitsbereich für Prozessmandate: Dokumentenablage, Aufgabenverteilung, Fristentracking. Normen: ZPO, BRAO. Prüfraster: Dokumentenstruktur, Aufgabenliste, Fristverwaltung. Output: Mandats-Arbeitsbereich-Struktur. Abgrenzung: n... |
| `mandat-arbeitsbereich-abschnitt` | Prozessrechtliche Strategie im laufenden Verfahren anpassen: Klageaenderung, Widerklage, Rücknahme. Normen: Paragrafen 263 264 269 ZPO. Prüfraster: Klageaenderungsvoraussetzungen, Rücknahmefolgen, Widerklagemöglichkeiten. Output: Strateg... |
| `mandat-aufnahme` | Prozessmandat aufnehmen: Sachverhalt erfassen, Zuständigkeit prüfen, Klagekonzept skizzieren. Normen: Paragrafen 253 261 ZPO, BRAO. Prüfraster: Sachverhaltserfassung, Anspruchsgrundlage, Zuständigkeit, Kosten-Risiko-Analyse. Output: Mand... |
| `mandat-briefing-schliessen-portfolio-status` | Mandantenbriefing für Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen. Normen: Paragrafen 373 ff. ZPO. Prüfraster: Beweislast, Zeugenvorbereitung, Verhandlungsstrategien. Output: Briefingdokument für Mandanten vor Term... |
| `mandat-mandate-prozessrecht` | Mandat: Formular, Portal und Einreichungslogik im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `mandat-schliessen` | Mandat nach Prozessabschluss formal schließen: Kostenfestsetzung, Archivierung, Mandanteninformation. Normen: Paragrafen 103 ff. ZPO, RVG. Prüfraster: Kostenfestsetzungsantrag, Ergebnismitteilung, Handaktenfreigabe. Output: Abschlussberi... |
| `mandate-tatbestand-beweis-und-belege` | Mandate: Tatbestandsmerkmale, Beweisfragen und Beleglage im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `output-waehlen` | Output-Wahl für Prozessrecht (ZPO/VwGO/StPO/SGG): stimmt Adressat (Mandant, Gegner, Gericht), Frist (Berufung 1 Mon. Paragraf 517 ZPO) und Form auf den Zweck ab — typische Outputs: Klage, Klageerwiderung, Beweisantrag. |
| `portfolio-status` | Statusuebersicht aller laufenden Prozessmandate: Fristen, Verfahrensstand, naechste Schritte. Normen: ZPO, RVG. Prüfraster: Fristenliste, offene Anträge, Termine, Mahnfristen. Output: Portfolio-Statusbericht Prozessmandate. Abgrenzung: n... |
| `proz-beweismittel-leitfaden-mediationsklage` | Leitfaden Beweismittel ZPO: Urkundenbeweis, Zeugenbeweis, Sachverstaendigenbeweis, Parteivernehmung, Augenscheinsbeweis. Prüfraster für Beweisangebot im Prozessrecht. |
| `proz-mediationsklage-guete-spezial` | Spezialfall obligatorisches Gueteverfahren Paragraf 15a EGZPO und Mediation: zuständige Stelle, Verlauf, Vergleich, Folgen. Prüfraster für Klägervorbereitung im Prozessrecht. |
| `proz-prozessfinanzierung-spezial` | Spezialfall Prozessfinanzierung: Anbieter, Quotenmodelle, RDG-Implikationen, Berufsrecht. Prüfraster für Mandant und Anwalt im Prozessrecht. |
| `proz-quellenkarte` | Proz Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `proz-zustaendigkeit-bauleiter` | Bauleiter Zuständigkeit ZPO: sachlich, oertlich, funktionell, internationale Zuständigkeit. Prüfraster typische Klagearten im Prozessrecht. |
| `prozessmandat-dokumente-fristen-aufgaben-workspace` | Digitaler Arbeitsbereich für Prozessmandate: Dokumentenablage, Aufgabenverteilung, Fristentracking. Normen: ZPO, BRAO. Prüfraster: Dokumentenstruktur, Aufgabenliste, Fristverwaltung. Output: Mandats-Arbeitsbereich-Struktur. Abgrenzung: n... |
| `prozessrecht-verhandlung-vergleich-und-eskalation` | Prozessrecht: Verhandlung, Vergleich und Eskalation im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `prozessrechtliche-schriftsaetze-status` | Prozessrechtliche: Erstprüfung, Rollenklärung und Mandatsziel im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `quellen-livecheck` | Quellen-Live-Check für Prozessrecht (ZPO/VwGO/StPO/SGG): prüft Normen (ZPO, VwGO, StPO, SGG, FGO, FamFG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Erste Instanz / Rechtsmittelgerichte und Quellenhygiene nach... |
| `schriftsaetze-schriftsatz-brief-und-memo-bausteine` | Schriftsaetze: Schriftsatz-, Brief- und Memo-Bausteine im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `schriftsatz-abschnitt` | Einzelne Abschnitte eines Schriftsatzes erstellen: Tatbestand, Begründung, Beweisangebot nach ZPO-Schema. Normen: Paragrafen 253 313 ZPO. Prüfraster: Schluessigskeit, Beweisangebot, Normzitat. Output: Schriftsatz-Abschnitt für Einbau in... |
| `spezial-proz-livequellen-und-rechtsprechungscheck` | Proz: Livequellen- und Rechtsprechungscheck. |
| `spezial-zustaendigkeit-zahlen-schwellen-und-berechnung` | Zustaendigkeit: Zahlen, Schwellenwerte und Berechnung. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Prozessrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-U... |
| `status-internationaler-bezug-und-schnittstellen` | Status: Internationaler Bezug und Schnittstellen im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `stpo-biometrischer-internetabgleich-und-ki-ermittlung` | StPO-Spezialprüfung zu digitalen Ermittlungsmaßnahmen: Paragraf 98d StPO-E biometrischer Internetabgleich, Paragraf 98e StPO-E Analyseplattform, Paragraf 101 StPO-E Benachrichtigung, Paragrafen 161 163 StPO als Grenzen manueller OSINT, K... |
| `strafverteidigung-ersttermin` | Ersttermin bei Strafverteidigung vorbereiten: Akteneinsicht, Schweigepflicht, prozessuale Schritte. Normen: Paragrafen 137 147 StPO. Prüfraster: Akteneinsichtsrecht, Mandatsverhältnis, erste Verteidigungsoptionen. Output: Checkliste Erst... |
| `streitwert-verkehrsunfall-vollstreckung` | Streitwert für zivilrechtliche Klagen berechnen: Hauptforderung, Nebenforderungen, Gerichts- und Anwaltsgebühren. Normen: Paragrafen 3 9 ZPO, GKG, RVG. Prüfraster: Streitwertbemessung, Nebenforderungen, Kostenfolge. Output: Streitwertber... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Prozessrecht (ZPO/VwGO/StPO/SGG): trennt fehlende Tatsachen von fehlenden Belegen (Klageschrift, Klageerwiderung, Schriftsätze), nennt pro Lücke Beweisthema, Beschaffungsweg (Erste Instanz / Rechtsmittel... |
| `verfahrensart-rechtsweg` | Fristen: Fristen, Form, Zuständigkeit und Rechtsweg im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `verfahrensart-rechtsweg-zustaendigkeit` | Verfahrensart, Rechtsweg und Zuständigkeit als Startweiche: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Prozessrecht. |
| `verkehrsunfall` | Verkehrsunfall-Mandat im Zivilprozess vorbereiten: Schadensersatz, Schmerzensgeld, Versicherungskorrespondenz. Normen: Paragrafen 7 18 StVG, Paragrafen 823 253 BGB, Paragraf 115 VVG. Prüfraster: Haftungsquote, Schadensposten, Verjaebrung... |
| `vollstreckung` | Zwangsvollstreckung aus Zivilurteil vorbereiten und einleiten: Pfaendung, Sachpfaendung, Forderungspfaendung. Normen: Paragrafen 704 ff. ZPO. Prüfraster: vollstreckbarer Titel, Klausel, Zustellungsnachweis, Vollstreckungsarten. Output: V... |
| `vollstreckung-stpo-biometrischer` | Vollstreckung: Behörden-, Gerichts- oder Registerweg im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `vorlageanordnung-zeuge-vorbereitung` | Vorlageanordnung nach Paragraf 142 ZPO beantragen: Vorlage von Urkunden durch Gegner oder Dritte. Normen: Paragrafen 142 143 ZPO. Prüfraster: urkundliche Beweise, Pflicht zur Vorlage, Sanktionen bei Weigerung. Output: Antrag auf Urkunden... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Prozessrecht. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Prozessrecht. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zeuge-vorbereitung` | Zeuge für Gerichtstermin vorbereiten: Aussagerecht, Zeugnisverweigerung, Vernehmungsablauf. Normen: Paragrafen 373 ff. 383 ff. ZPO. Prüfraster: Zeugnisverweigerungsrecht, Glaubwürdigkeitsfragen, Vernehmungsthemen. Output: Zeugenvorbereit... |
| `zustaendigkeit-zahlen-schwellen-und-berechnung` | Zuständigkeit: Zahlen, Schwellenwerte und Berechnung im Prozessrecht. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
