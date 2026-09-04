# Claude – Deutsche rechtliche Fähigkeiten / German Legal Skills

> **Experimentelles Skill-Set** für die anwaltliche Praxis im deutschen Recht – Skills, Sub-Agenten, Workflows etc. als Anregung für Kanzlei-Arbeitsabläufe. Orientiert sich an der **deutschen Rechtspraxis**, an Gesetzestexten, amtlichen Materialien und frei überprüfbarer Rechtsprechung. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr – jeder Nutzer kalibriert die Skills selbst für die eigene Praxis.

## Über dieses Repository

Dieses Repository ist eine **experimentelle Plugin- und Skill-Sammlung für deutsches Recht** auf Basis der offenen "claude-for-legal"-Skills von Anthropic, vollständig ins Deutsche übertragen und an typische Arbeitsabläufe in Kanzleien, Rechtsabteilungen und bei Beratern angepasst. Die Struktur, Beispiele und Workflows sind inzwischen **für die deutsche Rechtspraxis überarbeitet und im Alltagseinsatz erprobt**, sie bleiben aber bewusst als Experiment gekennzeichnet: Es handelt sich **nicht** um ein geprüftes Produkt, sondern um eine technische Spielwiese zum Ausprobieren, Anpassen und Weiterentwickeln.

Ziel ist es, zu zeigen, wie sich Plugins und Skills für Arbeitsrecht, Gesellschaftsrecht, Insolvenzrecht (inklusive Liquiditätsplanung und Fortbestehensprognose), Datenschutzrecht, Prozessrecht, gewerblichen Rechtsschutz, Produkt-, Robotik- und Regulierungsrecht u. a. so strukturieren lassen, dass sie sich an der in Deutschland üblichen Methodik (Anspruchsgrundlagen, Prüfungsaufbau, Gesetzesauslegung, Rechtsprechungszitate mit Datum und Aktenzeichen) orientieren. Die Inhalte dienen ausschließlich als **Anregung für eigene Kanzlei- oder Inhouse-Plugins und -Skills**: Sie sollen zeigen, welche Prompts, Rollenbeschreibungen und Workflows in der Praxis hilfreich sein können – jeder Nutzer passt sie an die eigenen Mandate, Branchen, Tools und Compliance-Vorgaben an.

## Deutsch: Dateien und Downloads

| Bestandteil | Was ist das? | Wann ist es richtig? | Wo liegt es? |
| --- | --- | --- | --- |
| **Plugin-ZIP** | Das installierbare Gesamtpaket eines Rechtsgebiets mit Skills, Referenzen und Hilfsdateien. | Wenn das Rechtsgebiet dauerhaft als Plugin eingerichtet werden soll. | Oben in jeder Plugin-README und im [Asset-Index](./ASSET_INDEX.md). |
| **Skill** | Ein eng abgegrenzter Arbeitsablauf für eine bestimmte Aufgabe innerhalb eines Plugins. | Wenn ein einzelner Prüfungsschritt, Entwurf oder Fachworkflow benötigt wird. | In der [Skill-Gesamtübersicht](./SKILLS.md), auf den [Plugin-Detailseiten](./skills-index/) und in jeder Plugin-README. |
| **Werkstatt-Prompt** | Eine ausführliche eigenständige Markdown-Datei für komplexe und mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Wenn ohne Installation möglichst viel fachliche Tiefe in einer einzigen Datei benötigt wird. | In der [Werkstatt-Übersicht](./docs/werkstatt-und-schnellstart-coverage.md#werkstatt-prompts) und oben in jeder Plugin-README. |
| **Schnellstart- oder Mini-Prompt** | Eine kompakte eigenständige Markdown-Datei für den schnellen Einstieg und ein erstes belastbares Arbeitsprodukt. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Wenn ein Fall schnell begonnen werden soll und der ausführliche Werkstattmodus noch nicht nötig ist. | In der [Schnellstart-Übersicht](./docs/werkstatt-und-schnellstart-coverage.md#schnellstart-prompts) und oben in jeder Plugin-README. |
| **Testakte** | Eine separate Dokumentensammlung zum Ausprobieren der Arbeitsabläufe; sie wird nicht mit einem Plugin installiert. | Wenn ein Workflow ohne eigenes Mandatsmaterial geprüft werden soll. | In der [Testakten-Übersicht](./testakten/README.md). |

**Klickverhalten:** README-, Index- und Übersichtslinks öffnen weiterhin eine GitHub-Seite zur Navigation. Links mit **MD herunterladen** laden dagegen die unveränderte Markdown-Arbeitsdatei auf den Rechner. Bei einzelnen Skills erhält die Datei einen eindeutigen Namen aus Plugin und Skill, damit mehrere Downloads nicht alle `SKILL.md` heißen.

[Jump to the English quick guide](#english-quick-guide)

> **Cowork mit eigenem Modellzugang:** Wenn du die Plugins in einer Cowork-Oberfläche über eine eigene Schnittstelle, einen Gateway-Anbieter oder einen Enterprise-Proxy nutzen willst, spring direkt zu [Eigene Schnittstelle oder Zwischenanbieter anbinden](#eigene-schnittstelle-oder-zwischenanbieter-anbinden-stand-juli-2026).

## Alle vollständigen Listen von A bis Z

<!-- BEGIN HAUPTVERZEICHNIS (auto-generated) -->
Die fünf vollständigen Register sind alphabetisch sortiert und werden bei jedem Release gegen Marketplace und Dateibestand geprüft. Jede Liste nennt zu jedem Eintrag eine Kurzbeschreibung und führt von dort unmittelbar zur Datei, zum Download oder zur passenden Detailseite.

| Bestand | Umfang | Kurzbeschreibung | Vollständige alphabetische Liste |
| --- | ---: | --- | --- |
| **Plugins** | 235 | Installierbare Pakete für Rechtsgebiete und Arbeitsbereiche; jede Zeile beschreibt Zweck und fachlichen Zuschnitt. | [Plugin-Katalog mit Kurzbeschreibungen](#was-ist-drin) · [ZIPs und Einzeldateien](./ASSET_INDEX.md) |
| **Skills** | 22729 | Eng abgegrenzte Arbeitsabläufe; die Detailseiten führen jeden Skill mit Kurzbeschreibung und einzelnem Markdown-Download auf. | [Skill-Gesamtübersicht](./SKILLS.md) · [Detailseiten je Plugin](./skills-index/) |
| **Werkstatt-Prompts** | 235 | Ausführliche eigenständige Arbeitsmodi für komplexe Vorgänge; je Plugin mit Kurzbeschreibung und direktem Markdown-Download. | [Werkstatt-Prompts von A bis Z](./docs/werkstatt-und-schnellstart-coverage.md#werkstatt-prompts) |
| **Schnellstart-/Mini-Prompts** | 235 | Kompakte eigenständige Einstiege für den Kernworkflow und ein erstes belastbares Arbeitsprodukt. | [Schnellstart-Prompts von A bis Z](./docs/werkstatt-und-schnellstart-coverage.md#schnellstart-prompts) |
| **Testakten** | 323 zentral / 326 gesamt | Praxisnahe Dokumentensammlungen; jede Zeile skizziert den Fall, nennt passende Plugins und bietet drei Downloadformen. Drei weitere Akten liegen unmittelbar bei ihren Plugins. | [Zentrale Testakten mit Kurzbeschreibungen von A bis Z](./testakten/README.md#verfügbare-akten) · [pluginlokale Akten über den Plugin-Katalog](#was-ist-drin) |

Sortierlogik: Plugins, Werkstatt- und Schnellstart-Prompts folgen dem Plugin-Slug; Skills sind zuerst nach Plugin und dort nach Skill-Slug sortiert; Testakten folgen dem Aktenordner. Die großen Bestände bleiben auf eigenen, schnell ladenden Registerseiten, damit der Haupt-README trotz 22729 Skills benutzbar bleibt.

Plugin-Schnellwahl: [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Z](#z)
<!-- END HAUPTVERZEICHNIS (auto-generated) -->

Weitere direkte Wege: [Schnellstart](#schnellstart) · [einfache Installationshilfe](./INSTALLATION_EINFACH.md) · [Kurzanleitung](./QUICKSTART.md) · [kuratierte Promptliste](./PROMPTLISTE.md) · [Rechtsgebietsübersicht](./references/rechtsgebiete-uebersicht.md) · [aktueller Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) · [English quick guide](#english-quick-guide)

### Bitte mit-testen und Feedback geben

Die Skills sind inzwischen deutlich verbessert und in verschiedenen Konstellationen getestet worden, können aber weiterhin Fehler, Lücken oder veraltete Rechtsstände enthalten. Deshalb:

- Nutzt die Skills aktiv im **Testbetrieb** (ohne echte Mandatsgeheimnisse) und schaut, wie gut sie zu euren Fällen, Quellenzugängen und Kanzleiprozessen passen.
- Gebt **Rückmeldungen**, eröffnet **Issues**, formuliert Verbesserungsvorschläge und schickt gerne **Pull Requests** mit eigenen Anpassungen, zusätzlichen Rechtsgebieten oder Praxis-Workflows.
- Passt die Beispiele an eure eigene **Zitierweise**, eure verifizierbaren Quellenzugänge und eure internen Vorgaben zu Berufsrecht, Datenschutz, KI-Governance und Mandatsgeheimnis an.

### Nutzungshinweis

Vor einem produktiven Einsatz sind Berufsrecht, Mandatsgeheimnis, Datenschutz, technischer Datenfluss und der fachliche Rechtsstand eigenverantwortlich zu prüfen. Die gebündelten Prüfpunkte stehen unter [Berufsrecht, Datenschutz und technischer Einsatz](#berufsrecht-datenschutz-und-technischer-einsatz).

> **Testakten zum Ausprobieren:** Im Verzeichnis [`testakten/`](./testakten) liegen mehrere umfangreiche, anonymisierte Arbeitsakten mit PDFs, Tabellen, Textdokumenten, E-Mails und Bilddateien, bewusst wie ein realer Datenraum zusammengestellt. Details und Direktdownloads stehen in der [Testakten-Übersicht](./testakten/README.md).

### Klotzkettes Juristische Promptliste

Viele Skills in diesem Repo sind strukturierte Markdown-Arbeitsabläufe. Sie können einzeln heruntergeladen und in einer geeigneten Arbeitsoberfläche als Datei verwendet oder aus der Datei kopiert werden. Werkstatt und Schnellstart sind davon getrennte Ein-Datei-Prompts: Die Werkstatt bietet die ausführliche Fachroute, der Schnellstart den kompakten Einstieg.

Für den Einsatz ohne Plugin-Installation gibt es pro Plugin zwei reine Markdown-Dateien: einen ausführlichen **Werkstatt-Prompt** und einen kompakten **Schnellstart-Prompt** mit höchstens 7.500 Zeichen. Beide werden als einzelne Markdown-Dateien angeboten, nicht als ZIP. Die Downloadlinks stehen oben in jeder Plugin-README und auf jeder Plugin-Detailseite; sie führen über die statische Downloadseite, weil GitHub das HTML-Attribut `download` in gerenderten README-Dateien entfernt.

### Formatstandard für erzeugte Dokumente

Alle Skills, Werkstatt-Prompts und Schnellstart-Prompts sind darauf ausgerichtet, verwertbare Endprodukte nicht nur inhaltlich, sondern auch formal sauber auszugeben. Für Schriftsätze, Klagen, Klageerwiderungen, Repliken, Dupliken, Anträge, Memos, Vermerke, Verträge, Beschlussentwürfe, Verfügungen und Mandantenbriefe gilt deshalb als Standard: **Times New Roman, Schriftgröße 11 pt, vollständig ausformulierte Sätze und ausschließlich dezimale Gliederung** (`1`, `1.1`, `1.1.1`). Wenn ein amtliches Formular, ein Gerichtslayout, ein Mandantentemplate oder ein Tabellenformat davon abweicht, soll der Prompt die Abweichung ausdrücklich benennen.

Für diesen Anwendungsfall gibt es eine kuratierte, nach Fachanwaltschaften sortierte Liste: **[Klotzkettes Juristische Promptliste](./PROMPTLISTE.md)** — alle Angaben ohne Gewähr, mit großem Disclaimer auf der Seite. Workflow-Eingangs-Skills, generische Router und ausgesprochen historisch-exotische Inhalte (Preußisches Landrecht, Römisches Recht, Kanonisches Recht, Weltraumrecht) bleiben dort bewusst ausgespart.

## Überblick

| Kennzahl | Wert |
|---|---|
| **Plugins** | 235 (inkl. 15 Gerichts- und Staatsanwalts-Plugins im Sammelordner [`gerichtsplugins/`](./gerichtsplugins/) und 11 Insolvenz-Plugins im Sammelordner [`insolvenzrecht-plugins/`](./insolvenzrecht-plugins/)) |
| **Skills (SKILL.md)** | 22729 — [Gesamtübersicht](./SKILLS.md) |
| **Testakten** | 323 zentral / 326 gesamt |
| **Fachanwalts-Profile** | 24 |
| **Plugin-Version / Arbeitsstand** | `v442.0.0` — [latest Release auf GitHub](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) |
| **Marketplace-Definition** | [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) |

### Sammel-Downloads

| Paket | Download | Inhalt |
| --- | --- | --- |
| **Alle Plugins als MegaZIP** | [alle-plugins-megazip.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) | Alle installierbaren Plugin-ZIPs plus `marketplace.json` in einem Archiv. |
| **Marketplace-Manifest** | [marketplace.json](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/marketplace.json) | Marketplace-Definition für Kommandozeilen-Nutzung oder ein privates beziehungsweise internes Organisations-Spiegelrepository; kein Einzel-Plugin und kein manueller ZIP-Upload. |
| **Alle Skills als Markdown-ZIP** | [alle-skills-markdown.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) | `SKILL.md`-Dateien, zugehörige Markdown-Referenzen und Plugin-READMEs. Werkstatt und Schnellstart sind bewusst nicht enthalten, sondern bleiben einzelne Markdown-Direktdownloads. Die einzelnen Skill-Markdown-Bundles liegen im Komplettpaket, nicht mehr als eigene Release-Assets. |
| **Alle Testakten als ZIP** | [alle-testakten.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) | Sammelarchiv der einzelnen Akten-ZIPs. In jedem Akten-ZIP liegen PDF, DOCX, XLSX, JPEG, EML und weitere Originalformate flach auf der Wurzelebene; Markdown und Unterordner sind ausgeschlossen. Eine zweisprachige `README.txt` weist auf die experimentelle Erzeugung und Nutzung auf eigene Verantwortung und Gefahr hin. |
| **Alle Testakten als Einzel-PDF-ZIP** | [alle-testakten-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) | Sammelarchiv der einzelnen PDF-ZIPs. In jedem Akten-ZIP liegt jede Unterlage als separate, sauber gerenderte PDF flach auf der Wurzelebene. Jedes PDF beginnt mit dem zweisprachigen Hinweis; pro Testakte gibt es zusätzlich ein eigenes `testakte-<name>-einzelpdfs.zip` im Release. |
| **Alles komplett als ZIP** | [alles-komplettpaket.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alles-komplettpaket.zip) | Alle Plugin-ZIPs, alle Skill-Markdown-ZIPs, alle Testakten-ZIPs (inklusive Einzel-PDF-ZIPs), Marketplace-Manifest und Übersichtsdateien in einem Archiv. Werkstatt und Schnellstart sind nicht Bestandteil der Archive; sie bleiben pro Plugin einzelne Markdown-Direktdownloads. |
| **SHA-256-Prüfsummen** | [checksums-sha256.txt](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/checksums-sha256.txt) | Maschinenlesbare Prüfsummen für Release-Assets; die Release-Pipeline gleicht Größen und Hashes nach dem Upload gegen GitHub ab. |
| **Klotzkettes Juristische Promptliste** | [PROMPTLISTE.md](./PROMPTLISTE.md) | Kuratierte Übersichtsseite praxistauglicher Prompt-Bausteine — sortiert nach Fachanwaltschaften, zum Kopieren in ChatGPT, Claude, Gemini, Perplexity oder beliebige andere Tools. Mit großem Disclaimer. |
| **Werkstatt- und Schnellstart-Coverage** | [docs/werkstatt-und-schnellstart-coverage.md](./docs/werkstatt-und-schnellstart-coverage.md) | Prüfliste, welches Plugin welche Werkstatt- und Schnellstart-Markdown-Dateien besitzt, mit Markdown-Direkt-Download-Links. |
| **Vollständiger Asset-Index** | [ASSET_INDEX.md](./ASSET_INDEX.md) | Pro Plugin: README, Skill-Detailseite, Plugin-ZIP sowie Werkstatt- und Schnellstart-Markdown. |

### Inhaltliche Cluster

- **Rechtsgebiete (materiell):** BGB Allgemeiner Teil, Arbeitsrecht, Mietrecht (Wohn-/Gewerbe), Nachbarrecht/Nachbarschaftsstreit, Erbrecht, Familienrecht, Sozialrecht, Sozialversicherungsstatus/DRV-Statusfeststellung, Strafrecht, Äußerungsrecht/Meinungsfreiheit, Verwaltungsrecht (inkl. Energieanlagen-BImSchG-Verfahren und Energietrassen-Planfeststellung), Steuerrecht, Insolvenzrecht inkl. StaRUG, Gesellschaftsrecht, Handelsregisterpraxis, Grundbuchamtspraxis, Erbbaurecht, Vertragsrecht, AGB-Recht, Markenrecht (inkl. Luxus-Fashion + USPTO/Lanham Act), Urheberrecht, Softwarerecht DE/EU/US, Wettbewerbsrecht, Kartellrecht, Datenschutzrecht, IT-Recht, digitale Barrierefreiheit, Robotikrecht, Bank- und Kapitalmarktrecht, Factoring, Bau- und Architektenrecht, Verkehrsrecht, Medizinrecht, Krankenhausrecht, GOÄ/Arzthonorar, Apothekenrecht, Migrationsrecht, Internationales Recht, Europarecht, Energierecht, Bundesnetzagentur-Verfahren, E-Commerce, Bürokratieverstehen, Vereinsrecht, Parteienrecht, Wahlkampfrecht, Bundeswehr-/Wehrrecht, Solo-Selbstständige, HOAI-Leistungsphasen, Commercial Courts/englischsprachige Wirtschaftsverfahren, Robotikrecht, Zwangsvollstreckung, Beamtenrecht/Richterrecht, US-Copyright Act und US Bankruptcy Code, NIS-2/Cybersecurity-Compliance, Hinweisgeberschutz, Handelsvertreterrecht, Schulrecht, Hochschulrecht und Hochschulprüfungsrecht.
- **Mechanik-Prüfer:** `bgb-at-pruefer` (BGB AT: Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, Anfechtung, Stellvertretung, Verjährung, qES/beA/Formfiktion), `bgb-bt-pruefer` (BGB BT: Kauf, Dienst, Werk, Geschäftsbesorgung, Auftrag, Leasing-Schnittstelle, Mischverträge, Bürgschaft, GoA, Bereicherung, Delikt, digitale Elemente und Right to Repair), `subsumtions-pruefer` (generischer Subsumtions-Workflow DE + EU), `bereicherungs-und-anfechtungsrecht-pruefer` (§§ 812 ff. BGB + AnfG + InsO-Anfechtung einschließlich KI-Schuldnerakten-Screening, § 135 InsO und Verteidigung), `ki-vo-ai-act-pruefer` (Verordnung (EU) 2024/1689 mit Anbieter/Betreiber-Entscheidungsbaum, Art. 5/6/25/51 ff.).
- **Werkstatt- und Werkstatt-Plugins:**
  - `legistik-werkstatt` — komplette Gesetzgebungs-Werkstatt für Bundesministerien, Bundestag, Fraktionen/Opposition, Landesministerien, Landtage und sonstige Normgeber (Referentenentwurf Arial-Hausstil, BT-/Landtagsdrucksache, Vorblatt A–F, Synopse, Lesefassung, Kabinettsmappe, Formulierungshilfe, Änderungsantrag, Antrag, Entschließungsantrag). DOCX/PDF im passenden offiziellen Layout.
  - `urteilsbauer-relationsmacher` — Urteils- und Beschluss-Werkstatt für Amts-, Land- und Familienrichter plus Rechtspfleger. Vollrelation (Sachbericht/Zulässigkeit/Schlüssigkeit/Erheblichkeit/Replik/Beweis/Tenorierung/Nebenentscheidungen/Selbstkontrolle) **und** Kurzrelation Praxisstandard mit Wahlfrage am Anfang. Rendert Urteile, Versäumnisurteile und Beschlüsse als DOCX im offiziellen Gerichtslayout nach § 313 ZPO. Inkl. Arbeitsakte "Solis Vision X Smartglasses" (CISG, kollidierende AGB CH/EU, Incoterm FOB Galway, DSGVO als Eingriffsnorm, Testkauf 1577 EUR).
  - `hausarbeitenmacher` — didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten im Jurastudium. Führt sokratisch durch Zivilrecht, Öffentliches Recht und Strafrecht mit Ausflügen in Europarecht und Rechtstheorie. Fragt zu Beginn nach der Lehrkraft und entwickelt eine Adressaten-Strategie **ohne Schleimerei**. Strikt lernfördernd: kein Copy-Paste-Output, sondern Fragen, Strukturen, Methodenhinweise, Zitierweise. 23 Skills von Aufgabenstellung-Erfassen über Gutachtenstil und Methodenlehre bis Selbstkontrolle vor Abgabe.
- **Workflow-Pakete:** Wandeldarlehen-Lebenszyklus (Erstellung, Beurkundung, Wandlung, Cap-Table, Notar), Kündigungsschutzklage Selbsthilfe (Laie/Anwalt, Schriftsätze, Sprechzettel, Vergleich), Entfristungsklage TzBfG (Schriftform, elektronische Signatur), KI-Richtlinie für Kanzleien, Schriftform-/Textform-Organisator, Krisenfrüherkennung StaRUG, Liquiditätsplanung, Fortbestehensprognose.
- **Querschnitt:** Aktenauszug Gerichtsverfahren, Mandantenanfragen-Assistent, Arbeitszeugnis-Analyse (Ampelsystem), Email-Umformulierer berufsrechtskonform, verifizierbare deutsche Zitierweise, Fachanwaltschafts-Übersicht.

> **Hinweis für Studium und Ausbildung:**
> Die Vollrelation, der Urteilsentwurf, der Hausarbeits- und Seminararbeits-Output sowie alle Arbeitsakten sind **Trainings-, Praxis- und Lernwerkzeuge** für Studenten, Referendare, Assessoren, Berufsrichter, Tutoren und Lehrkräfte. Sie sind ausdrücklich **nicht** dafür gedacht, in Hausarbeiten, Seminararbeiten, Klausuren, Aktenvorträgen oder im juristischen Vorbereitungsdienst (Z-, S-, V-, A-Klausur, mündliche Prüfung) als eigene Leistung ausgegeben zu werden. Das wäre ein Täuschungsversuch im Sinne der jeweiligen universitären Prüfungsordnung bzw. § 14 JAG NRW / § 12 JAPO Bayern / vergleichbarer Vorschriften der anderen Länder und kann zum Nichtbestehen, zur Aberkennung der Prüfung oder zu disziplinarrechtlichen Konsequenzen führen. Wer eine Relation, eine Hausarbeit oder ein Urteil üben will: zuerst selbst schreiben, danach mit dem Plugin abgleichen.

Die vollständige Plugin-Liste findest du in [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) und im Abschnitt [Was ist drin?](#was-ist-drin).

## Schnellstart

| Ich will ... | Schnellster Weg |
| --- | --- |
| sofort mit einem Fall beginnen | Plugin im [Katalog](#was-ist-drin) öffnen, Schnellstart-Markdown laden und mit den Unterlagen verwenden |
| ein Rechtsgebiet dauerhaft nutzen | `<plugin>.zip` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) unter **Customize → Plugins** hochladen |
| viele Rechtsgebiete zentral bereitstellen | Marketplace aus einer privaten oder internen Organisations-Spiegelung dieses Repositorys synchronisieren |
| einen komplexen Vorgang vertieft bearbeiten | Werkstatt-Markdown aus der jeweiligen Plugin-README laden |

Jede Plugin-README beginnt mit **In 30 Sekunden starten**. Dort stehen der direkte Schnellstart, die ausführliche Werkstatt, das installierbare Einzel-ZIP, passende Testakten und ein fertiger Startsatz.

Für den Organisations-Sync verlangt die aktuelle Oberfläche ein privates oder internes Repository. Das öffentliche Original wird dafür in ein Organisationsrepository gespiegelt; der manuelle Marketplace nimmt nur einzelne Plugin-ZIPs und höchstens 100 Plugins auf. Die genaue, aktuelle Route steht in [Installation in einfach](./INSTALLATION_EINFACH.md#4-marketplace-für-eine-organisation).

> Erfasse zuerst alle Dateien im ausgewählten Ordner nach Name, Datum und Typ. Öffne zunächst höchstens fünf tragende Unterlagen und beginne unmittelbar mit dem verlangten Arbeitsprodukt. Wenn nur der Prompt oder Skill gestartet wurde, bestimme daraus die Fachroute und liefere einen ersten belastbaren Stand. Erweitere die Lektüre nur für eine benannte Beleglücke; frage einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre.

Für Folgewünsche gilt: Den bisherigen Aktenstand fortführen, Tatsachen und Quellen nicht erneut abfragen und nur die verlangte Dimension ändern. Ausführlich: [Schnellstart in fünf Minuten](./QUICKSTART.md). ZIP-Probleme und Organisations-Sync: [Installation in einfach](./INSTALLATION_EINFACH.md).

**Wenn ein Lauf langsam startet:** Nur das benötigte Plugin aktiv lassen und nach Aktivierung oder Update eine neue Aufgabe öffnen. Innerhalb großer Plugins zuerst den sachnächsten Skill über `/` oder `+` wählen; die neuen Fachrouter laden bei Leistungsphasen, Länder-, Behörden-, Lohn-, BWA-, Sanierungsgewinn-, Beirats- und BHO-Fragen nur noch die tatsächlich benötigte Vertiefung. Für Microsoft 365 zuerst Website, Bibliothek oder Ordner, Zeitraum, Absender, Dateityp und Suchbegriff eingrenzen; im ersten Durchgang höchstens 20 Treffer erfassen und fünf tragende Unterlagen öffnen. Der vollständige [Schnellpfad für große Akten](./QUICKSTART.md#6-große-akten-und-microsoft-365-beschleunigen) vermeidet breite Suchen und wiederholte Dateilektüre.

## Berufsrecht, Datenschutz und technischer Einsatz

**Lesen, bevor irgendetwas davon eingesetzt wird.** Dieses Repository ist ausschließlich ein technisches Experiment. Es trifft **keinerlei Aussage** darüber, ob der Einsatz dieser Skills in einer konkreten Praxisumgebung berufs-, datenschutz- oder KI-rechtlich zulässig ist. Alle nachstehenden Fragen muss **jeder Nutzer in eigener Verantwortung** vor der ersten Nutzung prüfen – das Repository, sein Autor und alle Mitwirkenden übernehmen dafür keinerlei Verantwortung oder Haftung:

- **Strafrechtliches Mandatsgeheimnis – §§ 203, 204 StGB.** Die Skills sagen nichts darüber aus, ob ein konkreter Einsatz mit dem strafbewehrten Geheimnisschutz des § 203 StGB (Verletzung von Privatgeheimnissen) und § 204 StGB (Verwertung fremder Geheimnisse) vereinbar ist – auch nicht in der Variante § 203 Abs. 3, 4 StGB (mitwirkende Personen, sonstige Stellen).
- **Berufsrecht – § 43e BRAO, § 2 BORA, § 53 StPO.** Es wird **nicht** geprüft, ob der Einsatz mit § 43e BRAO (Inanspruchnahme von Dienstleistern, insbesondere Cloud/KI), § 2 BORA (Verschwiegenheit), den Zeugnisverweigerungsrechten nach § 53 StPO und den Beschlagnahmeverboten nach § 97 StPO vereinbar ist. Gleiches gilt sinngemäß für andere **freie Berufe** mit eigenem Berufsrecht (StBerG für Steuerberater, WPO für Wirtschaftsprüfer, Ärzte, Notare, Patentanwälte u. a.).
- **Datenschutz – DSGVO, BDSG.** Es wird **nicht** beurteilt, ob die Verarbeitung personenbezogener Daten DSGVO-konform ist, ob eine ausreichende **Rechtsgrundlage** (Art. 6, 9 DSGVO) vorliegt, ob ein **Auftragsverarbeitungsvertrag** nach Art. 28 DSGVO geschlossen werden muss, ob eine **Datenschutz-Folgenabschätzung** (Art. 35 DSGVO) erforderlich ist oder ob die **Informationspflichten** nach Art. 13, 14 DSGVO erfüllt sind.
- **KI-Verordnung (KI-VO / EU AI Act, VO (EU) 2024/1689).** Es wird **nicht** entschieden, ob der Einsatz unter eine der Hochrisiko-Kategorien nach **Art. 6 KI-VO** in Verbindung mit **Anhang III KI-VO** fällt (insbesondere Zugang zur Justiz, Strafverfolgung, demokratische Prozesse), ob **Transparenzpflichten** nach Art. 50 KI-VO greifen, ob es sich um ein **General-Purpose-AI-Modell** nach Art. 51 ff. KI-VO handelt und welche **Pflichten als Betreiber** (Art. 26 KI-VO) zu erfüllen sind.
- **Beschlagnahmeverbote und auslandsrechtliche Zugriffe.** Es wird nicht geprüft, ob Eingabedaten und Modellantworten gegen Beschlagnahme nach **§§ 97, 160a StPO**, gegen **US Cloud Act**, **FISA § 702**, **CLOUD Act warrants**, **PATRIOT Act § 215** oder sonstige extraterritoriale Zugriffsbefugnisse hinreichend geschützt sind. Dafür ist der jeweilige Nutzer allein verantwortlich.
- **Zugang, Auftragsverarbeitung, Hosting.** Wie der API-Zugang zum Modell beschafft wird (Anthropic direkt, AWS Bedrock, Google Vertex, eigenes Hosting), ob mit dem Anbieter ein **Auftragsverarbeitungsvertrag** geschlossen wird, ob ein **berufsrechtskonformer Cloud-Vertrag** vorliegt und ob die Anforderungen an die Verschwiegenheit / Mandatsgeheimnis-Header und Datenflusskontrolle in der konkreten Deployment-Konstellation eingehalten sind, bleibt vollständig in der **Eigenverantwortung des Nutzers**.

## Eigene Schnittstelle oder Zwischenanbieter anbinden (Stand Juli 2026)

Anwälte und andere Berufsgeheimnisträger müssen vor jeder produktiven Nutzung selbst prüfen, ob die konkrete Anbieter-, Hosting- und Datenflusskonstellation mit Mandatsgeheimnis, Berufsrecht und Datenschutz vereinbar ist. Dieses Repository bestätigt keinen Anbieter und ersetzt keine Prüfung von § 203 StGB, § 43e BRAO, Art. 28 DSGVO, Kapitel V DSGVO, TOMs, Löschkonzept, Audit-Rechten, Subunternehmern, Datenresidenz und vertraglicher Verschwiegenheit.

Für kleine Kanzleien gibt es diese Anleitung zusätzlich als bearbeitbares ODT-Dokument zum direkten Herunterladen: <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/docs/anbieterneutrale-schnittstelle-kanzlei.odt" download><code>anbieterneutrale-schnittstelle-kanzlei.odt</code></a>. Sie führt vom Anschlussmodell über Schlüsselverwaltung und Dummy-Test bis zum unterschriftsreifen Freigabevermerk.

Technisch gibt es drei mögliche Wege. Welcher davon verfügbar ist, hängt von der installierten Arbeitsoberfläche, dem freigegebenen Anschlussmodell und der Dokumentation des Schnittstellenanbieters ab. Ein Eingabefeld oder eine bestimmte Menübezeichnung darf nicht vorausgesetzt werden.

### Weg A — dokumentierte Schnittstellenmaske in der Oberfläche

Dieser Weg ist für eine kleine Kanzlei am einfachsten, setzt aber voraus, dass die installierte Cowork-Oberfläche einen eigenen Endpunkt oder ein verwaltetes Gateway ausdrücklich unterstützt.

1. In der aktuellen Dokumentation der Oberfläche prüfen, ob ein eigener Endpunkt unterstützt wird.
2. Beim Schnittstellenanbieter Vertrag, Auftragsverarbeitung, technische und organisatorische Maßnahmen, Verschwiegenheit, Datenstandorte und Unterauftragnehmer prüfen.
3. Endpunktadresse, Authentifizierungsart und Modellkennung exakt aus der Anbieterdokumentation übernehmen.
4. Den Schlüssel ausschließlich in das dafür vorgesehene geschützte Feld eintragen. Niemals in das Repository, eine Testakte, einen Prompt oder einen Bildschirmabzug schreiben.
5. Ausgehende Zieladressen auf die erforderlichen Anbieter-Domains beschränken, wenn die Oberfläche dies ermöglicht.
6. Oberfläche neu starten und zunächst nur einen harmlosen Satz mit erfundenen Daten senden.
7. Im Anbieterprotokoll prüfen, ob Nutzer, Zeit, Modellkennung und Zielendpunkt stimmen.

Fehlt eine dokumentierte Schnittstellenmaske, wird nicht mit ähnlich klingenden Menüs experimentiert. Dann kommt Weg B oder Weg C in Betracht.

### Weg B — verwaltetes Kanzlei-Gateway

Ein Gateway der Kanzlei oder ihres IT-Dienstleisters verwaltet den eigentlichen Anbieterschlüssel zentral. Die Arbeitsoberfläche erhält nur eine interne Endpunktadresse und einen widerrufbaren Kanzleizugang. Dieser Weg erleichtert Rechtevergabe, Kostenlimits, Protokollierung, Schlüsselwechsel und eine sofortige Sperre, benötigt aber eine dokumentierte technische Einrichtung.

Vor der Freigabe werden Datenfluss, Zertifikate, erlaubte Zieladressen, Zeitlimits, Protokollinhalt, Aufbewahrung und Notfallsperre getestet. Der Hauptschlüssel wird nicht auf einzelnen Arbeitsplätzen verteilt.

### Weg C — Markdown-Arbeitsablauf in einer anderen freigegebenen Oberfläche

Unterstützt die Cowork-Oberfläche keinen eigenen Endpunkt, lassen sich die Werkstatt- und Schnellstart-Prompts als Markdown-Dateien in einer anderen freigegebenen Arbeitsoberfläche verwenden. Dabei muss vorher geklärt werden, ob diese Oberfläche Dateien lesen, Arbeitsprodukte speichern und die im jeweiligen Workflow benötigten Werkzeuge ausführen kann. Ein reiner Textimport ersetzt solche Funktionen nicht.

Für den Einstieg genügt ein einzelnes Plugin und eine kleine Akte mit vollständig erfundenen PDF-Dateien. Erst wenn Dateizugriff, Quellenanzeige, Ausgabeordner und Anbieterprotokoll stimmen, werden weitere Plugins oder der vollständige Marketplace freigegeben.

### Kontrollliste vor echtem Mandatsmaterial

- Vertragliche Grundlage: AVV, TOMs, Verschwiegenheit, Unterauftragsverarbeiter, Audit-/Löschrechte.
- Datenfluss: Region, Protokollierung, Trainings-/Retention-Regeln, Support-Zugriffe.
- Technik: Endpunktadresse, Authentifizierung, Modellkennung, erlaubte Zieladressen und Anbieterprotokolle.
- Kanzleiorganisation: Nutzungsrichtlinie, Mandatsfreigabe, Rollen, Betriebsvereinbarung und Dokumentation in der Akte.
- Test: nur erfundene Daten, Anbieterprotokolle geprüft, keine Schlüssel im Repository.

Die Anleitung ist bewusst anbieterneutral. Sie beschreibt nur den technischen Anschlussweg und die zu dokumentierenden Prüfpunkte, nicht die rechtliche Zulässigkeit eines bestimmten Setups.

### Professioneller Betrieb über Gateway oder eine andere Arbeitsumgebung

Die Skills sind strukturierte Markdown-Arbeitsabläufe. Sie können in einer anderen freigegebenen Umgebung funktionieren, wenn diese die benötigten Datei-, Werkzeug- und Ausgabefunktionen bereitstellt. Entscheidend sind ein nachvollziehbarer Datenweg, klare Zugriffsrechte, kontrollierte Protokollierung und Aufbewahrung, dokumentierte Unterauftragnehmer, Datenresidenz sowie Export- und Prüfpfade.

Unabhängig von der Oberfläche bleibt die fachliche Verantwortung beim Nutzer. Normstand, Rechtsprechung, Tatsachen, Fristen, Berechnungen und die versandfertige Endfassung sind vor Verwendung zu prüfen.

## Einordnung und Qualitätsvorbehalt

Dieses Repository ist ein technisches Experiment und keine Aussage zur Eignung oder Zulässigkeit in einem konkreten Mandat. Vor jeder Verwendung sind Rechtsstand, Fristen, Tatsachen, Berechnungen und Quellen am Original zu prüfen; die Hinweise zu Berufsrecht, Datenschutz und technischer Einbindung stehen gebündelt in den vorstehenden Abschnitten.

Die Plugins, Skills und Prompts sind Ausgangspunkte für eigene, fachlich kontrollierte Arbeitsabläufe. Fehler, unpassende Fachrouten oder veraltete Bezüge können über [Issues](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues) gemeldet oder mit einem Pull Request korrigiert werden.

## Was ist drin?

> **Querschnitts-Plugins zum Mitladen:** Drei Plugins liefern die methodische Grundlage, die in den anderen Plugins vorausgesetzt wird. Sie gehören in jede Konfiguration mit hinein, weil sie den deutschen Stil tragen:
>
> - [`methodenlehre-buergerliches-recht`](./methodenlehre-buergerliches-recht) — Methodenlehre und Falllösung im deutschen bürgerlichen Recht aus Anwaltsperspektive. Anspruchsaufbau, Auslegung, Abwägung, Präzedenzarbeit, Rechtsfortbildung, Methodenwahl, EU-Methodik und Begründungskontrolle.
> - [`rechtstheorie-rechtsphilosophie`](./rechtstheorie-rechtsphilosophie) — Rechtsbegriff, Kelsen-orientierte Normgeltung, Kompetenz- und Stufenbauprüfung, Demokratie, Besitzdogmatik, Law-and-Economics, Hayek-Wissensproblem, spontane Ordnung, Machtkritik und anti-dezisionistisches Red-Team gegen Ausnahme-, Souveränitäts- und Freund-Feind-Rhetorik.
> - [`zitierweise-deutsches-recht`](./zitierweise-deutsches-recht) — Hauszitierweise mit Datum, Aktenzeichen, frei prüfbarer Quelle, Pinpoint-Randnummer und Sperre gegen BeckRS-/Literatur-Blindzitate. Pflicht-Checkliste vor jeder Ausgabe.
>
> Diese Plugins sind in jedem Modus (Claude Code, Cowork, Desktop) einzeln zuschaltbar und greifen quer in alle Rechtsgebiets-Plugins ein. Wer mit dem Marketplace startet, sollte sie zuerst aktivieren — alle anderen Skills referenzieren ihre Regeln (siehe [`references/methodik-buergerliches-recht.md`](./references/methodik-buergerliches-recht.md) und [`references/zitierweise.md`](./references/zitierweise.md)).

> **Testakten zum Ausprobieren:** Im Ordner [`testakten/`](./testakten) liegen umfangreiche Arbeitsakten mit PDFs, Tabellen, Textdokumenten, E-Mails, Bildern und weiteren Originalformaten. Jede Akte ist als Gesamt-PDF, flaches Einzel-PDF-ZIP und flaches Originalformat-ZIP verfügbar; zusätzlich gibt es [alle-testakten.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) als Sammelarchiv. Alle drei Fassungen tragen auf Deutsch und Englisch den Hinweis, dass die Testakte mit KI generiert wurde, experimentell ist und auf eigene Verantwortung und Gefahr benutzt wird. Details und Direktdownloads stehen in der [Testakten-Übersicht](./testakten/README.md).

> **🎁 Goodie – Testakte zum Ausprobieren der Claude Cowork-Funktion:** Die Sonderfall-Akte [ModeFuchs Cowork](./testakten/inkasso-modefuchs-cowork-sonderfall/README.md) simuliert einen unsortierten Desktop-Übergabeordner eines Inkassounternehmens: E-Mails als echte `.eml`-Dateien, Mahnungen als Scans ohne Textebene, ein Beleg-Foto, ein rohes Forderungskonto als Excel und ein Klageentwurf mit Anlagenverzeichnis K 1 bis K 7 – alle Dateinamen absichtlich nichtssagend (`Scan007.pdf`, `mail (2).eml`, `Dokument1.pdf`). Cowork soll in jede Datei hineinschauen, sprechend umbenennen, die Anlagen gestempelt als PDF für beA/eBO zusammenstellen und die Forderungsaufstellung prüfen. Direkt-Download: [`testakte-inkasso-modefuchs-cowork-sonderfall.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-modefuchs-cowork-sonderfall.zip)

Die folgende Tabelle enthält alle 235 installierbaren Plugins einzeln und alphabetisch sortiert. Auch Plugins in den Sammelordnern [`gerichtsplugins/`](./gerichtsplugins/) und [`insolvenzrecht-plugins/`](./insolvenzrecht-plugins/) erscheinen mit ihrem eigenen Namen und tatsächlichen Pfad. Thematische Einstiegsknoten stehen zusätzlich unter [`plugin-gruppen/`](./plugin-gruppen/); die vollständigen Downloadwege finden sich im [Asset-Index](./ASSET_INDEX.md).

<!-- BEGIN PLUGIN-KATALOG (auto-generated) -->
Alphabetisch: [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Z](#z)

### A

| Plugin | Beschreibung |
| --- | --- |
| [`agb-recht-pruefer`](./agb-recht-pruefer) | Gigantischer AGB-Rechtsprüfer und Klausel-Entwerfer für deutsches Recht: Paragrafen 305 bis 310 BGB, UKlaG, B2C/B2B, Branchen-AGB, Redlining, Klauselrisiko und rechtssichere Entwurfsworkflows. |
| [`aktenaufbereiter-strafrecht`](./aktenaufbereiter-strafrecht) | Aktenaufbereiter für die Strafverteidigung. Sechs Excel-fähige Übersichten — Aktenvorblatt; Personenverzeichnis; Tatkomplexe; Beziehungen; Chronologie; Fristen. Fortlaufend ergänzbar. Erkennt Lücken und Widersprüche. Kein Ersatz für Aktenlektüre. |
| [`aktenauszug-gerichtsverfahren`](./aktenauszug-gerichtsverfahren) | Strukturierter Aktenauszug für deutsche Gerichtsverfahren: Verfahrensidentifikation Einleitungssatz Verfahrenszusammenfassung Sachverhaltschronologie Verfahrensgeschichte tabellarische Gegenüberstellung der Parteivorträge Beweismittel und Rechtsargumente für schnelle Einarbeitung in Akten. |
| [`aktienrecht-hauptversammlung-ag-se`](./aktienrecht-hauptversammlung-ag-se) | Hauptversammlungs-Vorbereiter, Leitfaden-Ersteller und Durchführungsplugin für kleine AG, normale AG, börsennotierte AG und SE: Einberufung, Tagesordnung, virtuelle HV, Q&A, Abstimmung, Niederschrift, Anfechtungsrisiko und Post-HV. |
| [`anlagen-zu-schriftsaetzen`](./anlagen-zu-schriftsaetzen) | Gerichtsprozess-Dokumentenproduktion bis zur beA-fertigen Versandmappe: liest Schriftsatz und Anlagenordner, führt K/B/AST/AG fort, konvertiert und stempelt jede PDF-Seite, prüft ERVV, Signatur, Dateinamen, Empfänger und Eingang und liefert Verzeichnis, Manifest und Freigabevermerk. |
| [`apothekenrecht`](./apothekenrecht) | Super-Plugin für Apothekenrecht: Betriebserlaubnis, ApBetrO, Versand, E-Rezept, BtM, Retaxation, Aufsicht und Compliance. |
| [`arbeitsrecht`](./arbeitsrecht) | Arbeitsrechtliche Workflows für Kündigung, Befristung, Urlaub, AGG, Aufhebungsvertrag, Betriebsrat, Arbeitszeit, Lohn und Expansion. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und verifizierbarer Quelle verwendet. |
| [`arbeitszeugnis-analyse`](./arbeitszeugnis-analyse) | Analyse deutscher Arbeitszeugnisse nach Ampelsystem. Prüft Geheimcodes, Schaufenster-Drift, negative Codeworte, Steigerungsadverbien, Satznoten und Gesamtnotenspanne. Führt vom Erstgespräch über Mandantenbericht und Aufforderungsschreiben bis zur Klagestrategie. |
| [`arbeitszeugnisgenerator`](./arbeitszeugnisgenerator) | Erstellt, prüft und berichtigt einfache, qualifizierte, Zwischen- und Ausbildungszeugnisse aus vorhandenen Unterlagen. Verknüpft Tätigkeitsbild, Tatsachenbelege, Beweislast, klare Formulierungen, Vergleich und Vollstreckung zu einem verwendbaren Arbeitsprodukt. |
| [`arbeitszeugnispruefer`](./arbeitszeugnispruefer) | Prüft bestehende deutsche Arbeitszeugnisse Schritt für Schritt: Notenstufen, Zufriedenheits- und Verhaltensformeln, Geheimcodes, Auslassungen, Steigerungsadverbien, Schlussformel. Liefert Ampel-Einschätzung pro Satz, Gesamtnote, Aufforderungsschreiben oder Klagestrategie zur Berichtigung. |
| [`aufsichtsrat-ag-se-praxis`](./aufsichtsrat-ag-se-praxis) | Praxisplugin für Aufsichtsräte in AG und SE: Überwachung, Informationsrechte, Vorstand bestellen/abberufen, Vergütung, Ausschüsse, Protokoll, Business Judgment, Haftungsvermeidung, Börse, SE und Mitbestimmung. |
| [`aussenwirtschaft-zoll-sanktionen`](./aussenwirtschaft-zoll-sanktionen) | Freistehendes Plugin für Außenwirtschaft, Sanktionen, Zoll, Exportkontrolle, BAFA, TARIC, CBAM, Verbrauchsteuer, AWV, AML/KYC und Ermittlungen. |

### B

| Plugin | Beschreibung |
| --- | --- |
| [`bank-rechtsabteilung`](./bank-rechtsabteilung) | Rechtsabteilung einer mittelgroßen deutschen Bank: Aufsicht, Kredit, Avale, Bürgschaft, Garantien, Trade Finance, ZAG/PSD2, PSD3/PSR-Vorschau, eWpG, MiCAR, Tokenisierung, BaFin, Vorstand, HV und Kanzleisteuerung. |
| [`barrierefreiheit-web-checker`](./barrierefreiheit-web-checker) | Web-Barrierefreiheits-Checker für BFSG, BFSGV, BITV 2.0, EN 301 549 und WCAG: Scope, Audit, Tastatur, Screenreader, Formulare, PDFs, Erklärung, Roadmap und Abnahme. |
| [`bautraegervertrag-pruefer`](./bautraegervertrag-pruefer) | Bauträgervertrag-Prüfer aus Verbrauchersicht: MaBV, Paragrafen 650u/650v BGB, Paragraf 650m Abs. 2 BGB, AGB, Baubeschreibung, Abnahme, Schlussrate, WEG, Vormerkung, Lastenfreistellung und Drei-Dokumente-Ausgabe. |
| [`bautraegervertragspruefer`](./bautraegervertragspruefer) | Prüft deutsche Bauträgerverträge: MaBV-Ratenplan und Sicherheiten, Paragrafen 650u und 650v BGB, AGB-Kontrolle, Baubeschreibung, Abnahme Gemeinschaftseigentum, Bauzeit, Preisanpassung, Teilungserklärung. Liefert Mandantengutachten und Aufforderungsschreiben an Bauträger und Notar. |
| [`bav-strategie-konzern`](./bav-strategie-konzern) | Strategische Beratung zur betrieblichen Altersversorgung in Konzernen: Pensionsmodelle alle fünf Durchführungswege CTA Pension Buyouts Drei-Stufen-Theorie Versorgungssystem-Harmonisierung internationale Benefits Restrukturierung DB-zu-DC im Düsseldorfer Boutique-Stil. |
| [`beamtenrecht`](./beamtenrecht) | Beamtenrecht für Bund, Länder und Richterdienst: Status, Laufbahn, Besoldung, Versorgung, Konkurrentenstreit, Disziplinarrecht, Dienstunfähigkeit, Richterlaufbahn, Landesrecht und verständliche Mandatsführung. |
| [`bereicherungs-und-anfechtungsrecht-pruefer`](./bereicherungs-und-anfechtungsrecht-pruefer) | Mechanisches Durchprüfen von Bereicherungsrecht Paragrafen 812 ff. BGB, AnfG und Insolvenzanfechtung Paragrafen 129-147 InsO. Mit KI-Screening von Schuldnerakten, Paragraf 135 Gesellschafterdarlehen, Bargeschäft Paragraf 142 und Verteidigung des Anfechtungsgegners. Keine Rechtsberatung. |
| [`berichtspflichten-erlediger`](./berichtspflichten-erlediger) | Berichtspflichten-Erlediger für mittelständische Unternehmen: amtliche Statistik, Portale, Umwelt-, Produkt-, Steuer-, Sozial-, Lieferketten-, Datenschutz- und Aufsichtsmeldungen mit Fristenboard, Datenquellen, Plausibilitätscheck und Behördenkommunikation. |
| [`berufsgerichtliche-verfahren-freie-berufe`](./berufsgerichtliche-verfahren-freie-berufe) | Plugin für anwaltsgerichtliche und berufsgerichtliche Verfahren gegen Anwälte, Patentanwälte, Steuerberater, Wirtschaftsprüfer und Notare: Kammeraufsicht, Rüge, Disziplinarverfahren, Zulassung, Vermögensverfall, beA, Werbung, Sachlichkeit und Rechtsmittel. |
| [`berufsrecht-anwaelte`](./berufsrecht-anwaelte) | Plugin für anwaltliches Berufsrecht: BRAO, BORA, FAO, beA, Kanzleisitz, Werbung, Interessenkollision, Verschwiegenheit, KI-/Cloud-Outsourcing, Schatten-KI, Berufsausübungsgesellschaft, Gebühren, Kammeraufsicht und anwaltsgerichtliche Risiken. |
| [`berufsrecht-ki-vertragspruefung`](./berufsrecht-ki-vertragspruefung) | Berufsrechtliche und strafrechtliche Vorprüfung von Verträgen mit Legal-AI-Anbietern: Paragraf 43e BRAO, Paragraf 203 StGB, Consumer-Tool-Abgrenzung, No-Training, Telemetrie, Drittstaat, KI-VO-Rollen, Art.-50-Transparenz, Schatten-KI und Klauselvorschläge. |
| [`berufsrecht-notare`](./berufsrecht-notare) | Plugin für Notarrecht: BNotO, BeurkG, DONot, Dienstaufsicht, Urkundspflichten, Neutralität, Verwahrung, Amtspflichten, Vertreter/Verwalter, Disziplinarverfahren und notarielle Berufspraxis. |
| [`berufsrecht-patentanwaelte`](./berufsrecht-patentanwaelte) | Plugin für Patentanwaltsrecht: PAO, Patentanwaltskammer, Vertretungsbefugnis, Schutzrechtsmandate, Verschwiegenheit, Interessenkollision, Werbung, Berufsausübungsgesellschaft und berufsgerichtliche Risiken. |
| [`berufsrecht-steuerberater`](./berufsrecht-steuerberater) | Plugin für Steuerberaterrecht: StBerG, BOStB, Steuerberaterkammer, Vorbehaltsaufgaben, Werbung, Verschwiegenheit, Gebühren, Geldwäsche, Berufsgericht, Berufsausübungsgesellschaft und Haftungsprävention. |
| [`berufsrecht-wirtschaftspruefer`](./berufsrecht-wirtschaftspruefer) | Plugin für Wirtschaftsprüferrecht: WPO, Berufssatzung, WPK, APAS, Unabhängigkeit, Qualitätskontrolle, Abschlussprüfung, Bestätigungsvermerk, PIE, Berufsaufsicht und berufsgerichtliche Risiken. |
| [`betaeubungsmittelrecht`](./betaeubungsmittelrecht) | Betäubungsmittelrecht-Plugin für BtMG, BtMVV, KCanG/MedCanG-Schnittstellen, Strafverfahren, Therapie, ärztliche Praxis, Apotheken und Compliance. |
| [`betreuungsrecht`](./betreuungsrecht) | Betreuungsrechtliche Skills für ehrenamtliche Familienbetreuer, Berufs- und Vereinsbetreuer: Kaltstart, Scan-Akte, Kalender, Gerichtskommunikation, Jahresbericht, Vermögensverzeichnis, Genehmigungspflichten, Wunschermittlung, Kontoanalyse und Schutzplan nach BtOG und BGB. |
| [`bgb-at-pruefer`](./bgb-at-pruefer) | Großes Prüfplugin zum BGB Allgemeiner Teil: Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, qES, beA, Anfechtung, Stellvertretung, Fristen, Verjährung und Routing für digitale Elemente, Update- und Reparaturrecht. |
| [`bgb-bt-pruefer`](./bgb-bt-pruefer) | Großer BGB-BT-Prüfer für Schuldrecht Besonderer Teil: Kauf einschließlich Verbrauchsgüterkauf, Waren mit digitalen Elementen, Updatepflichten und Right-to-Repair-Schnittstellen, außerdem Miete, Werk, Bürgschaft, GoA, Bereicherung, Delikt und Rückabwicklung. |
| [`buerokratieversteher-entbuerokratisierer`](./buerokratieversteher-entbuerokratisierer) | Allgemeiner Bürokratieversteher und Entbürokratisierer für Laien, Menschen mit Deutsch als Zweitsprache und alle, die Bescheide, Anträge, Vorladungen, Behördenbriefe, Jugendamt-, Schul-, Bau-, Sozial-, Familien- oder Kommunalverfahren verstehen und vorsichtig bearbeiten wollen. |
| [`bundesnetzagentur-verfahren`](./bundesnetzagentur-verfahren) | Großes Regulierungs-Plugin für anwaltliche Arbeit mit der Bundesnetzagentur in Energie, Telekommunikation, Post, Eisenbahn und Digital Services. |
| [`bundeswehrrecht-wehrrecht`](./bundeswehrrecht-wehrrecht) | Super-Plugin für Soldatenrecht, Wehrbeschwerde, Disziplinarrecht, Wehrpflicht, Reservisten, Versorgung und Bundeswehrverwaltung. |

### C

| Plugin | Beschreibung |
| --- | --- |
| [`commercial-courts-deutschland`](./commercial-courts-deutschland) | Commercial-Courts-Plugin für englischsprachige Wirtschaftsverfahren in Deutschland: Zuständigkeit, Wahlklauseln, Klage, Case Management, Beweis, Geheimnisschutz, Wortprotokoll/Transcript, Rechtsmittel, BGH, Kosten, Vollstreckung und bilingualer Schriftsatz-/Hearing-Workflow. |
| [`common-law-kompass`](./common-law-kompass) | Freistehendes Common-Law-Plugin für deutsche Wirtschaftsjuristen: UK/US-False-Friends, Vertragsbegriffe, Consideration, Suretyship, Indemnity, UCC, Precedent, Discovery und bilinguale Drafting-Reviews. |
| [`corporate-kanzlei`](./corporate-kanzlei) | Corporate-Kanzlei-Plugin: Deal-Kommandocenter, Datenraum, Due Diligence, SPA/APA, Umwandlung, StaRUG, Insolvenzplan, W&I, Signing/Closing, PMI. |

### D

| Plugin | Beschreibung |
| --- | --- |
| [`datenbankrecht`](./datenbankrecht) | Großes Plugin zum deutschen und europäischen Datenbankrecht: UrhG Paragrafen 87a ff., Datenbankrichtlinie, Investitionsschutz, automatisiertes Auslesen, API, Training digitaler Systeme, Vertrags- und Plattformkonflikte. |
| [`datenschutz-sanktionsverfahren-verteidigung`](./datenschutz-sanktionsverfahren-verteidigung) | Spezialplugin für Vertretung und Verteidigung in datenschutzrechtlichen Sanktionsverfahren: DSGVO-Bußgeld, OWiG/StPO, Art.-58-Anordnung, Verwaltungsgericht, Aufsichtsbehördenkommunikation, EuGH/EDPB und Behördenstrategie. |
| [`datenschutzrecht`](./datenschutzrecht) | DSGVO/BDSG/TDDDG – PIA/DPIA, AVV-Review, Auskunft Art. 15, Datenpanne Art. 33/34, Drittlandstransfer Art. 44 ff. inkl. US-Transfer, DPF, SCC, TIA, Behördenpaket und Brückenskills zur Sanktionsverteidigung. |
| [`denkmalschutzrecht`](./denkmalschutzrecht) | Denkmalschutzrecht in Deutschland: Art. 14 und Art. 70 GG als bundesstaatlicher Rahmen plus alle sechzehn Landesgesetze. Skills für Eintragung Erlaubnis Bußgeld steuerliche Förderung nach Paragraf 7i EStG und Welterbestätten — länderübergreifende Grundlagen und Landesrecht klar getrennt. |
| [`designrecht-geschmacksmusterrecht`](./designrecht-geschmacksmusterrecht) | Eigenständiges Plugin für deutsches und europäisches Designrecht: DesignG, EU-Design, DPMA, EUIPO, WIPO-Hague, Neuheit, Eigenart, Anmeldung, Nichtigkeit, Verletzung, Eilrechtsschutz, Zoll, Plattformen und Designverträge. |
| [`deutsche-rechtsgeschichte`](./deutsche-rechtsgeschichte) | Mega-Plugin zur deutschen Rechtsgeschichte: Epochen, Quellenkritik, Rezeption, Reichsrecht, BGB, Weimar, NS-Unrecht, DDR/BRD und rechtsgeschichtliche Argumentation. |
| [`dfg-foerderantrag`](./dfg-foerderantrag) | DFG-Förderantragssteller für Sachbeihilfe, adaptive Anfänger-/Profi-Führung, kleine schnelle Anträge, große Koselleck-Strategien, elan-Formalia, Finanzplan, Reviewer-Red-Team, Forschungsdaten, KI-/Ethik-Check und Wiedereinreichung. |
| [`dsa-dma-digitalregulierung`](./dsa-dma-digitalregulierung) | Digitalregulierung der EU: DSA (VO 2022/2065) und DMA (VO 2022/1925) plus Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO und Paragraf 19a GWB. Gatekeeper-Schwellen VLOP-Einordnung Risikobewertung Art. 34 Forschungsdatenzugang Art. 40 Account-Sperre Art. 20-23 Zustellung Art. 13 DSA Klagewege. |

### E

| Plugin | Beschreibung |
| --- | --- |
| [`ecommerce-recht`](./ecommerce-recht) | Super-Plugin für Online-Shops, Plattformen, Marktplätze und digitale Verbraucherprozesse. |
| [`einfache-leichte-sprache-jura`](./einfache-leichte-sprache-jura) | Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Standard-Annäherung, Zielgruppe klären, Rechtsinhalt sichern und Qualitätsgate nutzen. |
| [`einigungsvertrag-vermoegensrecht`](./einigungsvertrag-vermoegensrecht) | Einigungsvertrag-Plugin für DDR/BRD-Übergangsrecht, Volksvermögen, Parteivermögen, Treuhand, Bodenreform, Mauergrundstücke, VermG und Restitution. |
| [`email-umformulierer-berufsrecht`](./email-umformulierer-berufsrecht) | Formuliert unfreundliche, emotionale oder unsachliche E-Mails in höfliche, sachliche und berufsrechtskonform formulierte Texte um. Fokus auf BRAO/BORA-Konformität, mit Varianten für Steuerberater, Notare und allgemeine berufliche Korrespondenz. |
| [`energierecht`](./energierecht) | Freistehendes Energierecht-Plugin für Stadtwerke, Versorger, Wärme, Netze, Vertrieb, Industrie, EEG, KWKG, Verfahren, Transaktionen und Projektfinanzierung. |
| [`erbbaurecht-praxis`](./erbbaurecht-praxis) | Praxisplugin für Erbbaurecht und Erbbaugrundbuch: Erbbaurechtsvertrag, Erbbauzins, Wertsicherung, Heimfall, Zustimmung, Belastung, Finanzierung, Veräußerung, Laufzeit, Entschädigung, Zwangsversteigerung, Rang und Grundbuchvollzug. |
| [`europaeisches-prozessrecht`](./europaeisches-prozessrecht) | Europäisches Prozessrecht vor EuGH und EuG: Klagearten, Vorlage, e-Curia, Fristen, Rechtsschutz, Rechtsmittel, Intervention, Beweis, Kosten und Strategie. |
| [`europarecht-kompass`](./europarecht-kompass) | Freistehendes Europarecht-Plugin gegen deutsche Denkfehler: Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Charta, Grundfreiheiten, Beihilfen, Vorlageverfahren und EU-Drafting. |

### F

| Plugin | Beschreibung |
| --- | --- |
| [`fachanwalt-agrarrecht`](./fachanwalt-agrarrecht) | Plugin Fachanwalt für Agrarrecht. Höferecht (HöfeO Anerbenrecht Länder) Landpachtrecht BGB Paragrafen 581 ff. GAP EU-Direktzahlungen Cross-Compliance Düngeverordnung Pflanzenschutz Tierschutz Forstrecht. Schnittstelle Plugin fachanwalt-erbrecht. |
| [`fachanwalt-arbeitsrecht`](./fachanwalt-arbeitsrecht) | Fachanwalt-Arbeitsrecht nach FAO Paragraf 10: KSchG, BetrVG, TzBfG, AGG, EntgTranspG, Urlaub, Betriebsrat, Befristung und Vergleichspraxis. Rechtsprechung nur mit Datum, Aktenzeichen und verifizierter Quelle. |
| [`fachanwalt-bank-kapitalmarktrecht`](./fachanwalt-bank-kapitalmarktrecht) | Plugin Fachanwalt für Bank- und Kapitalmarktrecht. KWG ZAG WpHG WpIG MiFID-II MAR MiCAR Verbraucherkredit Bürgschaft Aval Bankgarantie Vermögensanlage Beratungshaftung. Schnittstellen Plugin gesellschaftsrecht regulatorisches-recht. |
| [`fachanwalt-bau-architektenrecht`](./fachanwalt-bau-architektenrecht) | Plugin Fachanwalt für Bau- und Architektenrecht. BGB Werkvertrag VOB-A VOB-B VOB-C HOAI Bauordnungsrecht. Bauvertrag Mängelhaftung Abnahme Vergaberecht. Schnittstellen Plugin fachanwalt-vergaberecht kanzlei-allgemein. |
| [`fachanwalt-erbrecht`](./fachanwalt-erbrecht) | Plugin Fachanwalt für Erbrecht. BGB Erbrecht Paragrafen 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaftsteuer EU-ErbVO. Schnittstellen Plugin steuerrecht-anwalt-und-berater kanzlei-allgemein. |
| [`fachanwalt-familienrecht`](./fachanwalt-familienrecht) | Plugin Fachanwalt für Familienrecht. Orientierung Normen Mandate Fristen Literatur. Familiengericht FamFG Scheidung Sorge Umgang Unterhalt Zugewinn Ehevertrag eingetragene Lebenspartnerschaft. Ergänzend zum Plugin kanzlei-allgemein. |
| [`fachanwalt-gewerblicher-rechtsschutz`](./fachanwalt-gewerblicher-rechtsschutz) | Plugin Fachanwalt für gewerblichen Rechtsschutz nach FAO Paragraf 14k. MarkenG. DesignG. UWG. PatG GebrMG. UrhG-Bezüge. Markenanmeldung DPMA EUIPO. UWG-Abmahnung Paragrafen 8 ff. UWG. Designverletzung. Einstweilige Verfügung Verletzungsklage Lizenzanaloger Schadensersatz. |
| [`fachanwalt-handels-gesellschaftsrecht`](./fachanwalt-handels-gesellschaftsrecht) | Plugin Fachanwalt für Handels- und Gesellschaftsrecht nach FAO Paragraf 14i. HGB. AktG. GmbHG. PartGG. UmwG. Geschäftsführerhaftung Paragrafen 43 GmbHG 93 AktG. Gesellschafterstreit Beschlussanfechtung. Handelsvertreterausgleich Paragraf 89b HGB. MoPeG GbR seit 2024. Schnittstellen kanzlei-allgemein. |
| [`fachanwalt-insolvenz-sanierungsrecht`](./fachanwalt-insolvenz-sanierungsrecht) | Plugin Fachanwalt für Insolvenz- und Sanierungsrecht nach FAO Paragraf 14. InsO Eröffnung Antragspflicht Paragraf 15a Gläubigerantrag Paragraf 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung Paragrafen 129 ff. InsO. Schnittstellen insolvenzrecht und steuerrecht-anwalt-und-berater. |
| [`fachanwalt-internationales-wirtschaftsrecht`](./fachanwalt-internationales-wirtschaftsrecht) | Plugin Fachanwalt für Internationales Wirtschaftsrecht. CISG Brüssel Ia Rom I Rom II Schiedsverfahren ICC UNCITRAL Investitionsschutz ICSID WTO EU-Außenhandel LkSG. Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-it-recht`](./fachanwalt-it-recht) | Plugin Fachanwalt für Informationstechnologierecht. SaaS Software-Lizenz DSGVO BDSG TTDSG TKG NIS2 DDG DSA DMA EU-KI-VO Open-Source. Schnittstellen Plugin datenschutzrecht ki-governance kanzlei-allgemein. |
| [`fachanwalt-medizinrecht`](./fachanwalt-medizinrecht) | Plugin Fachanwalt für Medizinrecht. Arzthaftung Paragrafen 630a ff. BGB Patientenrechte Vertragsarztrecht Berufsrecht Ärzte SGB V Krankenversicherung MPDG Apothekenrecht. Schnittstellen Plugin fachanwalt-sozialrecht und kanzlei-allgemein. |
| [`fachanwalt-miet-wohnungseigentumsrecht`](./fachanwalt-miet-wohnungseigentumsrecht) | Großer Fachanwalt-Kompass Miet- und Wohnungseigentumsrecht mit über 200 Skills für Wohnraum, Gewerberaum, Betriebskosten, WEG, Hausverwaltung, Beschlüsse, GEG, Beweise, Fristen und Workflows. |
| [`fachanwalt-migrationsrecht`](./fachanwalt-migrationsrecht) | Großer Fachanwalt-Kompass Migrationsrecht mit über 200 Skills für Aufenthalt, Blaue Karte EU, Fachkräfte, Asyl, Dublin/GEAS, Einbürgerung, Staaten-/Gebietschecks und spanische/einfache Erklärung. |
| [`fachanwalt-sozialrecht`](./fachanwalt-sozialrecht) | Plugin Fachanwalt für Sozialrecht nach FAO Paragraf 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch Paragraf 84 SGG Klage Paragraf 87 SGG Eilantrag Paragraf 86b SGG. Bürgergeld Erwerbsminderung GdB Pflegegrad Hilfsmittel Eingliederungshilfe. Bescheidanalyse Akteneinsicht PKH Fristenbuch. |
| [`fachanwalt-sportrecht`](./fachanwalt-sportrecht) | Plugin Fachanwalt für Sportrecht. Verbandsrecht (DFB FIFA UEFA IOC DOSB) CAS Schiedsverfahren Spielerverträge Doping WADA-Code NADA Sponsoring Persönlichkeitsrechte Veranstalterhaftung. Schnittstelle Plugin gesellschaftsrecht. |
| [`fachanwalt-strafrecht`](./fachanwalt-strafrecht) | Plugin Fachanwalt Strafrecht: StPO/StGB, Nebenstrafrecht, Verteidigung, Ermittlungsverfahren, HV, Revision, Nebenklage und Zeugenbeistand plus Strafprozess-Cockpit für Fristen, Aktenlog, U-Haft, Akteneinsicht, HV-Tagesmappe, Antragslog und Mandanteninstruktionen. |
| [`fachanwalt-transport-speditionsrecht`](./fachanwalt-transport-speditionsrecht) | Plugin Fachanwalt für Transport- und Speditionsrecht. HGB Paragrafen 407 ff. Frachtvertrag Paragrafen 453 ff. Spedition CMR COTIF Montrealer Übereinkommen Haager Visby Regeln ADSp. Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-urheber-medienrecht`](./fachanwalt-urheber-medienrecht) | Plugin Fachanwalt für Urheber- und Medienrecht. UrhG UWG KUG Recht am eigenen Bild Presserecht Persönlichkeitsrecht Medienstaatsvertrag. Schnittstellen Plugin gewerblicher-rechtsschutz verlagsredaktion kanzlei-allgemein. |
| [`fachanwalt-vergaberecht`](./fachanwalt-vergaberecht) | Fachanwalt Vergaberecht als Vergabe-Workbench: GWB 97 ff., VgV, UVgO, SektVO, KonzVgV, VOB/A, Schwellenwerte, Vergabeakte, Rüge, vorgerichtliche Abhilfe, Nachprüfungsantrag, Vergabekammer-Sachverhalt, Paragraf 168-GWB-Abstellungsanträge, TED/eForms und Wettbewerbsregister. |
| [`fachanwalt-verkehrsrecht`](./fachanwalt-verkehrsrecht) | Plugin Fachanwalt für Verkehrsrecht. StVG StVO PflVG VVG-Bezüge. Verkehrsunfall Personen- und Sachschaden Bußgeld Fahrerlaubnis Verkehrsstrafrecht (Paragrafen 315c 316 StGB). Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-versicherungsrecht`](./fachanwalt-versicherungsrecht) | Plugin Fachanwalt für Versicherungsrecht. VVG VAG Berufsunfähigkeit private Krankenversicherung Lebens- und Rentenversicherung Sachversicherung Haftpflicht D-und-O. Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-verwaltungsrecht`](./fachanwalt-verwaltungsrecht) | Plugin Fachanwalt für Verwaltungsrecht. VwGO VwVfG. Anfechtungs- und Verpflichtungsklage Eilrechtsschutz Paragraf 80 Abs 5 VwGO einstweilige Anordnung Normenkontrolle Polizei- und Ordnungsrecht. Schnittstelle Plugin kanzlei-allgemein. |
| [`factoring-recht`](./factoring-recht) | Super-Plugin für Factoring, Forderungskauf, Aufsichtsrecht, Vertragsgestaltung, Debitorenkommunikation, Insolvenz- und Sanierungsfragen. |
| [`fahrgastrechte`](./fahrgastrechte) | Fahrgastrechte im Eisenbahnverkehr nach VO (EU) 2021/782 und EVO 2023: Verspätung/Ausfall einordnen, Entschädigung berechnen (25/50 Prozent), Forderung an die DB, Widerspruch, Schlichtung und Klage zum AG. Katalog DB-Ablehnungsgründe. |
| [`fashion-law-moderecht`](./fashion-law-moderecht) | Praxisplugin Fashion Law/Moderecht für Modeunternehmen, Designer, Händler und Kanzleien: IP, Designs, Marken, Textilkennzeichnung, Produktsicherheit, Nachhaltigkeit, Lieferkette, Plattformen, E-Commerce, Vertrieb, Influencer und Krisen. |
| [`festlandchina-wirtschaftsverkehr`](./festlandchina-wirtschaftsverkehr) | Mega-Plugin für wirtschaftlichen Umgang mit Festlandchina: Fabrik, Import, Export, Investition, De-Risking, Lieferkette, IP, Daten, Exportkontrolle und politisches Risiko. |
| [`fluggastrechte`](./fluggastrechte) | Fluggastrechte selber geltend machen nach VO (EG) Nr. 261/2004. Tickets erfassen, Annullierung oder Verspätung prüfen, außergewöhnliche Umstände, Distanz, Ausgleich, Forderungsschreiben, Mahnung und Klage. Rechtsprechung nur nach Live-Verifikation. |
| [`forderungsmanagement-klagewerkstatt`](./forderungsmanagement-klagewerkstatt) | Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben. |
| [`forschungszulage-antragstellung`](./forschungszulage-antragstellung) | Forschungszulage-Antragstellung nach FZulG: adaptiver Fördercheck, BSFZ-Portaltexte mit Zeichenbudgets, Finanzamt-Antrag, FuE-Abgrenzung, Bemessungsgrundlage 2026, Auszahlung, Verlust-/Insolvenzlage, Dokumentation, Beihilfen, Einspruch und Mehrjahresroadmap. |
| [`fortbestehensprognose`](./fortbestehensprognose) | Fortbestehensprognose Paragraf 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwölf-Monats-Liquidität. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose. |
| [`franchiserecht-praxis`](./franchiserecht-praxis) | Wirtschaftsrechtliches Plugin für Franchise-Systeme: vorvertragliche Aufklärung, Handbuch, Gebühren, Gebietsschutz, Kartellrecht, Kündigung, Expansion, Streit und Insolvenz. |

### G

| Plugin | Beschreibung |
| --- | --- |
| [`gebrauchsmusterrecht`](./gebrauchsmusterrecht) | Eigenständiges Plugin für deutsches Gebrauchsmusterrecht: GebrMG, DPMA-Anmeldung, Recherche nach Paragraf 7 GebrMG, Abzweigung, Neuheitsschonfrist, Verletzung, Löschung, BPatG-Beschwerde, Lizenz, FTO und Schnellschutz für technische Produkte. |
| [`geldwaeschepraevention-aml-kyc`](./geldwaeschepraevention-aml-kyc) | Freistehendes Plugin für Geldwäscheprävention, AML, KYC, GwG-Risikoanalyse, UBO, PEP, Sanktionen, FIU/goAML, Transparenzregister und Behördenverfahren. |
| [`gesellschaftsgruender`](./gesellschaftsgruender) | Gründungsassistent für deutsche Gesellschaften: Rechtsformwahl, Satzung, Notar, Handelsregister, Bank/KYC, Steuerstart, IP, Erlaubnisse, erste Verträge, Budget und Streitprävention. |
| [`gesellschaftsrecht`](./gesellschaftsrecht) | Gesellschaftsrecht für GmbH, AG und Personengesellschaften: Beschlüsse, Gesellschafterliste, Satzung, Organhaftung, Streit, Kapitalerhaltung, Umwandlung, Register und Transaktionen. |
| [`gesellschaftsrecht-legal-english`](./gesellschaftsrecht-legal-english) | Didaktisches Gesellschaftsrecht — English Business Terms: Corporate Legal English für Big-Law-Anfänger. Dealroom: Cap Table vs Gesellschafterliste; Term Sheet; SHA; Vesting; Drag/Tag; Liquidation Preference; Anti-Dilution; SPA; DD; Notar/HR; Multi-Format-Auswertung; Frankfurt-Startup-Akte. |
| [`gesellschaftsrechtliche-treuepflicht`](./gesellschaftsrechtliche-treuepflicht) | Großes Prüfplugin zur gesellschaftsrechtlichen Treuepflicht in GmbH, AG, SE, Personengesellschaft, Familiengesellschaft und Konzern: Stimmrecht, Minderheitenschutz, Gesellschafterliste, Einziehung, Ausschluss, Konkurrenz, Sanierung, Treuepflichtverletzung und Rechtsfolgen. |
| [`gewerblicher-rechtsschutz`](./gewerblicher-rechtsschutz) | Gewerblicher Rechtsschutz – DPMA/EUIPO-Markenrecherche und -anmeldung, Freedom-to-Operate, Patentscreening, UWG- und Urheberrechts-Abmahnung (Versand und Reaktion), Open-Source-Compliance, IP-Klausel-Review, Schutzrechts-Fristen. |
| [`goae-gebuehrenordnung-aerzte`](./goae-gebuehrenordnung-aerzte) | Super-Plugin zur GOÄ: private Arztrechnungen prüfen, erstellen, begründen, beanstanden und prozessual verwerten. |
| [`grosskanzlei-corporate-ma`](./grosskanzlei-corporate-ma) | Corporate/M&A-Plugin für Kanzlei- und Inhouse-Praxis: Deal-Intake, Datenraum, Legal DD, SPA/APA, Kaufpreis, W&I, Regulatory, Signing, Closing, Integration, Board Papers und Spezial-Workflows. |
| [`grundbuchamt-praxis`](./grundbuchamt-praxis) | Praxisplugin für Grundbuchamt, Grundbuchauszug und grundbuchtaugliche Nachweise: Abteilung I/II/III lesen, Bewilligung, Antrag, Auflassung, Rang, Zwischenverfügung, Beschwerde, Grundschuldbrief, Aufgebot, Dienstbarkeiten, Vormerkung, Vorkaufsrecht, Teilung und Vollzug. |

### H

| Plugin | Beschreibung |
| --- | --- |
| [`handelsrecht-hgb`](./handelsrecht-hgb) | Reines HGB-Plugin für Handelsrecht: Kaufmann, Handelsregister, Firma, Prokura, Handlungsvollmacht, Handelsgeschäfte, Handelskauf, Handelsvertreter, Makler, Kommission, Fracht, Spedition, Lager, Handelsbücher sowie OHG/KG einschließlich MoPeG-Statuswechsel von GbR zu OHG. |
| [`handelsregister-praxis`](./handelsregister-praxis) | Praxisplugin für den Umgang mit dem Handelsregister: Anmeldung, Registergericht, Rechtspfleger, Registerrichter, Beanstandung, Zwischenverfügung, Beschwerde, Gesellschafterliste, Kapitalmaßnahmen, Firma, Vertretung, Prokura, Löschung, Insolvenzvermerk und registerfeste Nachweise. |
| [`handelsvertreterrecht`](./handelsvertreterrecht) | Handelsvertreterrecht nach HGB: Status, Provision, Buchauszug, Kündigung, Ausgleich Paragraf 89b, Wettbewerbsverbot Paragraf 90a und Vertriebsmodelle. |
| [`hausarbeitenmacher`](./hausarbeitenmacher) | Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten. Führt sokratisch durch Zivilrecht öffentliches Recht Strafrecht mit Ausflügen in Europarecht und Rechtstheorie. Adressaten-Strategie ohne Schleimerei. Liefert keine fertigen Lösungen sondern führt zur eigenen Subsumtion. |
| [`haushaltsrecht-bho-bund-laender`](./haushaltsrecht-bho-bund-laender) | Großes Haushaltsrecht-Plugin für BHO, HGrG, Bundeshaushalt, Länderhaushalte, Titelanalyse, Umschichtung, Sondervermögen, Szenarien und Dashboard. |
| [`hinweisgeberschutz-compliance`](./hinweisgeberschutz-compliance) | Hinweisgeberschutzgesetz in der Praxis: interne/externe Meldestelle, NDA-Konflikte, Repressalien, Untersuchungen, Datenschutz und Governance. |
| [`hoai-leistungsphasen-praxis`](./hoai-leistungsphasen-praxis) | Großplugin für HOAI-Leistungsphasen 1 bis 9: Grundlagenermittlung, Vorplanung, Entwurf, Genehmigung, Ausführungsplanung, Vergabe, Bauüberwachung, Objektbetreuung, Honorar, Vertrag, Haftung, Nachträge und Bauprojektsteuerung. |
| [`hochschulrecht-laender`](./hochschulrecht-laender) | Hochschulrecht der Länder: Hochschulgesetze, Satzungen, Gremien, Zulassung, Exmatrikulation, Berufung, Drittmittel, Promotion und Aufsicht. |

### I

| Plugin | Beschreibung |
| --- | --- |
| [`immobilienrechtspraxis`](./immobilienrechtspraxis) | Werkzeuge für immobilienrechtliche Rechtsabteilungen: musterbasierte Vertragserstellung mit Klauselschutz, Vertragsprüfung gegen Playbook, Grundbuchanalyse, Sachverhaltsermittlung, Mieteranfragen, Case Management und AVV-Prüfung. Rechtsprechung nur nach Live-Verifikation. |
| [`influencer-recht`](./influencer-recht) | Plugin für Influencer, Creator, Agenturen und Unternehmen: Werbekennzeichnung, Steuer, Umsatzsteuer, Sachleistungen, Plattformrecht, Medienrecht, Marken, Urheberrecht, Datenschutz und Verträge. |
| [`informationsfreiheit-presseauskunft`](./informationsfreiheit-presseauskunft) | IFG-, Transparenz-, UIG-, VIG- und Presseauskunfts-Plugin für Bund, Länder und Behörden: Antrag, Kosten, Fristen, Widerspruch, Klage und Tracking. |
| [`insiderrecht-compliance`](./insiderrecht-compliance) | Insiderrecht- und Marktmissbrauchs-Compliance nach MAR, WpHG und BaFin-Praxis: Insiderinformationen, Ad-hoc, Insiderlisten, Handelsverbote, Aufschub, Directors Dealings, Aufklärung und Verteidigung. |
| [`insolvenzforderungsanmeldungspruefung`](./insolvenzforderungsanmeldungspruefung) | Freistehendes Plugin für die Insolvenzforderungsanmeldungsprüfung: Intake, Paragraf 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Prüfungstermin, Bestreiten, Feststellung, Tabellenauszug und Verteilung. |
| [`insolvenzplan-starug-planwerkstatt`](./insolvenzplan-starug-planwerkstatt) | Freistehendes Plugin für Insolvenzplan und StaRUG-Restrukturierungsplan: Intake, Sanierungskonzept, Vergleichsrechnung, Gruppen, Klassen, darstellender und gestaltender Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Planvollzug. |
| [`insolvenzrecht`](./insolvenzrecht) | Insolvenzrechtliche Skills zu Zahlungsunfähigkeit, Überschuldung, Antragspflicht und Gläubigerantrag. |
| [`insolvenzverwaltung`](./insolvenzverwaltung) | Freistehendes Insolvenzverwaltungs-Plugin aus Sicht von Insolvenzverwalter, Sachwalter und vorläufiger Verwaltung: Regelverfahren, Eigenverwaltung, Schutzschirm, Anfechtung, Paragraf 15b InsO, Masse, Forderungsprüfung, Insolvenzplan, StaRUG-Planwerkstatt, Gutachten, Berichte und Schlussrechnung. |
| [`internal-investigations-praxis`](./internal-investigations-praxis) | Internal-Investigations-Praxisplugin für Kanzleien und Unternehmen: Untersuchungsauftrag, Scope, Interviews, Arbeitsrecht, Datenschutz, Privilege-Risiko, StPO-Beschlagnahme, HinSchG, Dokumentation und Verteidigung. |
| [`internationales-handelsrecht-lex-mercatoria`](./internationales-handelsrecht-lex-mercatoria) | Mega-Plugin für internationales Handelsrecht, CISG, Incoterms, UNIDROIT Principles, Lex Mercatoria, Schiedsverfahren, Trade Finance und Lieferkettenverträge. |

### J

| Plugin | Beschreibung |
| --- | --- |
| [`jurastudium`](./jurastudium) | Studium und Referendariat – Prüfungsgespräch nach AG-Tradition, Subsumtionslehre, Methodenlehre (Zivilrecht, Strafrecht, Öffentliches Recht), Rechtsgeschichte, Lernstrategien, Lösungsschemata, Gutachtenstil, Klausurkorrektur, Lernplanung. |
| [`juristische-presseberichterstattung`](./juristische-presseberichterstattung) | Plugin für juristische Presseberichterstattung: Gerichtsbericht, Entscheidungsnews, Verdachtsbericht, Pressemitteilung, Headline, Bildprüfung, Quellenmatrix und Redaktionsschluss-Qualitygate. |
| [`juristische-sprache-deutsch-als-zweitsprache`](./juristische-sprache-deutsch-als-zweitsprache) | Plugin für Menschen im deutschen Recht mit anderer Herkunftssprache: einfache Erklärungen, Juristendeutsch, Bescheide, Schriftsätze, Grammatik, Fristen und Verfahrenslogik. |
| [`jveg-kostenpruefer`](./jveg-kostenpruefer) | Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle. |

### K

| Plugin | Beschreibung |
| --- | --- |
| [`kanzlei-allgemein`](./kanzlei-allgemein) | Kanzlei-Allgemein-Plugin (fusioniert mit Cowork): edles Kommandocenter Mandatsannahme/GwG Klage/Replik Vertrag Rechtsprechung Handelsregister beA-Journal Rechnung UStVA Fristenbuch Timesheet RVG Versand-Vor-Check Posteingang Mandantenakte Mahnwesen Tagesbrief Geburtstage Weihnachtskarten. |
| [`kanzlei-builder-hub`](./kanzlei-builder-hub) | Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Deployment in die Kanzleiumgebung. |
| [`kanzlei-management`](./kanzlei-management) | Mega-Plugin für Kanzlei-Management: Managing Partner, Management Committee, Cashflow, Pricing, UBT, FTE, Utilization, WIP, Associates, Partnerkreis und Dashboards. |
| [`kanzlei-mandant-lifecycle`](./kanzlei-mandant-lifecycle) | Lifecycle-Plugin für Kanzlei, Mandant und Rechtsabteilung: Mandatsstart, OCG, Budget, Dashboard, Rechnung, Litigation, Erwartungsmanagement und Relationship-Governance. |
| [`kartellrecht-marktabgrenzung-pruefung`](./kartellrecht-marktabgrenzung-pruefung) | Globales Kartellrecht/Competition Law: GWB, Art 101/102 AEUV, Fusionskontrolle, BKartA, DG Competition, FTC/DOJ, ICN-Jurisdiktionen, Dawn Raids, Marktabgrenzung, Missbrauch, Private Enforcement. |
| [`ki-governance`](./ki-governance) | EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie. |
| [`ki-richtlinie-kanzleien`](./ki-richtlinie-kanzleien) | Erstellt und pflegt eine berufsrechtskonforme KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen mit Anwälten und Syndikus-Anwälten. Beruht auf BRAO, BORA, DSGVO, KI-Verordnung sowie BRAK- und DAV-Hinweisen. |
| [`ki-vo-ai-act-pruefer`](./ki-vo-ai-act-pruefer) | Mechanik-Workflow zur KI-VO (EU 2024/1689): KI-System-Definition, Rollen, Risikoklassen, Hochrisiko-Diagnose, GPAI, Art. 43-Konformitätsbewertung, CE/EU-DB, Marktbeobachtung, Konformitäts-Evidence-Pack, KI-Kompetenz, Shadow-AI, Berufsrecht, Hochschul- und Behördenpraxis. |
| [`kommunalrecht-laender`](./kommunalrecht-laender) | Großes Kommunalrecht-Plugin für Gemeinden, Städte, Landkreise, Satzungen, Räte, Bürgerbegehren, Kommunalfinanzen, Aufsicht und Landesrecht. |
| [`krankenhausrecht`](./krankenhausrecht) | Super-Plugin für deutsches Krankenhausrecht: Planung, Finanzierung, Entgelte, Reform, Qualität, MD-Prüfung, Klinikbetrieb und Rechtsstreit. |
| [`krankenkassenrecht-krankenversicherung`](./krankenkassenrecht-krankenversicherung) | Plugin für GKV, PKV, Beihilfe-Schnittstellen und Krankenversicherungsrecht: Leistungen, Beiträge, Krankengeld, Hilfsmittel, Widerspruch, MD, Versicherungsvertrag und Kostenerstattung. |
| [`kriegsdienstverweigerung-wehrdienst`](./kriegsdienstverweigerung-wehrdienst) | Praxisplugin für Kriegsdienstverweigerung und Wehrdienst aus Gewissensgründen: Art. 4 Abs. 3 GG, KDVG n. F. 2026, Antrag über BAPersBw, BAFzA-Entscheidung, Gewissensbegründung, Soldaten, Reservisten, Rechtsschutz und saubere Abgrenzung zur Totalverweigerung. |
| [`krisenfrueherkennung-starug`](./krisenfrueherkennung-starug) | Krisenfrüherkennung nach Paragraf 1 StaRUG, Warnpflicht bei Jahresabschlusserstellung nach Paragraf 102 StaRUG, 24-Monats-Prognose nach Paragraf 18 InsO, Haftung, integrierte Planung, Restrukturierungsplan und Stabilisierungsanordnung. |

### L

| Plugin | Beschreibung |
| --- | --- |
| [`leasingrecht-praxis`](./leasingrecht-praxis) | Wirtschaftsrechtliches Praxisplugin für Leasing, Sale-and-lease-back, Equipment Finance, Fahrzeugflotten, IT-Leasing, Insolvenz, Restwert, Sicherheiten und Vertragsgestaltung. |
| [`legistik-werkstatt`](./legistik-werkstatt) | Legistik-Werkstatt für Ministerien, Bundestag, Fraktionen/Opposition, Länder, Landtage und Normgeber. Baut Referenten- und Kabinettsentwürfe, Vorlagen aus der Mitte, Änderungs-/Entschließungsanträge, Rechtsverordnungen und Satzungen mit Begründung, Synopse, XML und Prüfpfaden. |
| [`liquiditaetsplanung`](./liquiditaetsplanung) | Liquiditätsplanung nach deutschem Recht: 3-Wochen-Vorschau, 13/26/52-Wochen-Forecast, Excel-Export, Quote/Lücken-Ampel, Dokumentationspaket und Schnittstellen zu Fortbestehensprognose und Insolvenzrecht. Rechtsprechung nur nach Live-Verifikation. |
| [`lizenzvertragsersteller`](./lizenzvertragsersteller) | Baukastensystem für IP-Lizenzverträge deutsches und internationales Recht. 32 Skills: Urheber Patent Marken Design Gebrauchsmuster Geschäftsgeheimnis Know-how; Klausel-Bausteine, Quellcode-Escrow, Insolvenz-Klausel, Sicherungslizenz, TT-GVO, DSGVO, Quellensteuer, Output DE EN bilingual. |
| [`lobbyregister-bundestag`](./lobbyregister-bundestag) | Lobbyregister-Bundestag-Superplugin mit 50 geführten Skills für Registrierungspflicht, Ausnahmen, Registereintrag, Regelungsvorhaben, Stellungnahmen, Finanzdaten, Aktualisierung, Verhaltenskodex, Meldung von Verstößen und Fristen nach LobbyRG. |
| [`luftrecht-flughafenrecht`](./luftrecht-flughafenrecht) | Luftrecht-Plugin für LuftVG, LuftSiG, LBA, Flughäfen, Airlines, Slots, Flugzeugpfandrechte, Beschlagnahme, Insolvenz, Drohnen und Aviation-Compliance. |

### M

| Plugin | Beschreibung |
| --- | --- |
| [`mandantenanfragen-assistent`](./mandantenanfragen-assistent) | Assistent für Anwaltskanzleien zur Erstantwort auf Mandantenanfragen per E-Mail: dankt förmlich übernimmt die Anrede aus der eingehenden E-Mail nennt die telefonische Terminvergabe bittet um Sachverhalt per E-Mail oder bietet eine Telefon-Transkription mit DSGVO-Einwilligungshinweis an. |
| [`markenrecht-fashion-luxus`](./markenrecht-fashion-luxus) | Großes Markenrechts-Plugin für DE/EU/US und internationale Portfolios: DPMA, EUIPO, WIPO/Madrid, USPTO, Markenarten, Schutzhindernisse, Benutzung, Widerspruch, Verfall/Nichtigkeit, Enforcement, Plattformen, Zoll, Lizenzen und Luxus-Fashion-Spezialfälle. |
| [`meinungspruefer`](./meinungspruefer) | Meinungsprüfer für Äußerungsrecht: Meinung oder Tatsache, Beleidigung, üble Nachrede, Verleumdung, Paragraf 188 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR/EuGH, OLG-Praxis, US-Supreme-Court-Vergleich, Zivilrecht, Plattformen, Social Media, Arbeitsplatz, Schule und kommunale Machtkritik. |
| [`memorandums-ersteller`](./memorandums-ersteller) | Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral. Alias Memorandumsmacher. |
| [`methodenlehre-buergerliches-recht`](./methodenlehre-buergerliches-recht) | Methodenlehre und Rechtsanwendung im deutschen bürgerlichen Recht aus Anwaltsperspektive: Anspruchsaufbau, Auslegung, Abwägung, Präzedenzarbeit, Rechtsfortbildung, Methodenwahl, EU-Methodik und methodenehrliche Begründungskontrolle. |
| [`mietrecht`](./mietrecht) | Mietrecht für Mieter und Vermieter mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitätsstädte. Datenerhebung Mieterhöhungs-Widerspruch Mietsenkungsverlangen Nebenkostenprüfung und Erstellung Mieteranfragen Klageentwurf zum Amtsgericht. |
| [`mittelstand-corporate-ma`](./mittelstand-corporate-ma) | Freistehendes Mittelstandsmandat-Corporate/M&A-Plugin: Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, Umwandlung, StaRUG/Insolvenzplan, CP-Kalender, E-Rechnung/GoBD, PMI. |

### N

| Plugin | Beschreibung |
| --- | --- |
| [`nachbarschaftsstreit-pruefer`](./nachbarschaftsstreit-pruefer) | Nachbarrecht und Nachbarschaftsstreit: Überbau, Überhang, Äste/Wurzeln, Grenzbaum, Zaun/Mauer/Hecke, Immissionen, Vertiefung, Notweg, Hammerschlagsrecht, Beweise, Aufforderung, Klage und Vergleich. |
| [`nda-abgleich`](./nda-abgleich) | Gleicht NDA-Entwurf der Gegenseite gegen eigenen Standard ab und setzt Haltelinien chirurgisch im Word-Änderungsmodus durch. Ampelmatrix ROT/GELB/GRUEN. Ausgabe .docx mit echten Tracked Changes. Keine Absatzlöschungen, keine Klausel-Neufassungen. |
| [`nda-verschwiegenheit-generator-checker`](./nda-verschwiegenheit-generator-checker) | Allgemeiner NDA-Ersteller und NDA-Prüfer für deutsche und internationale Verschwiegenheitsvereinbarungen: Entwurf, Redline, GeschGehG, HinSchG, AGB, Arbeitsrecht, M&A, Forschung, Software, Datenraum und Verletzungsreaktion. |
| [`nis2-cybersecurity-compliance`](./nis2-cybersecurity-compliance) | NIS-2, BSIG 2025, BSI, IT-Grundschutz, Cloud, Incident Response und technische Security-Compliance für Geschäftsleitung, CISO und Legal. |
| [`normenkontrolle-bauleitplanung`](./normenkontrolle-bauleitplanung) | Freistehendes Plugin für die Prüfung und Anfechtung von Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften nach Paragraf 47 VwGO vor BayVGH und OVG. Mandatsperspektive Antragstellervertretung. |
| [`normenkontrollrat-nkr`](./normenkontrollrat-nkr) | Plugin für den Nationalen Normenkontrollrat (NKR): Prüfung von Referentenentwürfen Formulierungshilfen und Gesetzentwürfen auf Erfüllungsaufwand Erforderlichkeit Verhältnismäßigkeit One-in-one-out Digitalcheck Mittelstandsfreundlichkeit und Praktikabilität im Vollzug. |
| [`notariat-alltag`](./notariat-alltag) | Alltagsplugin für Notariat, Notariatsmitarbeiter und Notare: Beurkundung, Vollzug, Register, Grundbuch, Geldwäsche, Kosten, Fristen und Mandantenkommunikation. |

### O

| Plugin | Beschreibung |
| --- | --- |
| [`oeffentliches-wirtschaftsrecht`](./oeffentliches-wirtschaftsrecht) | Öffentliches-Wirtschaftsrecht-Plugin für Scheinprivatisierung, ÖPP, Projektfinanzierung, kommunale Unternehmen, Beihilfen, Vergabe und Regulierung. |
| [`ordnungswidrigkeitenrecht`](./ordnungswidrigkeitenrecht) | Allgemeines OWiG-Plugin für Bußgeldverfahren: Anhörung, Bescheid, Einspruch, Behörde, Akteneinsicht, Gericht, Verjährung, Einziehung und Nebenfolgen. |

### P

| Plugin | Beschreibung |
| --- | --- |
| [`parteienrecht-parteiorganisation`](./parteienrecht-parteiorganisation) | Parteienrechts- und Parteiorganisations-Plugin für formale Parteiarbeit: Parteiengesetz, Satzung, Mitgliederrechte, Parteitage, Kreis- und Bezirksversammlungen, Kandidatenaufstellung, Wahlvorschläge, Parteigerichte, Spenden, Rechenschaft, Abgeordnetenrecht und Wahlleiterkommunikation. |
| [`patentrecherche`](./patentrecherche) | Patentrecherche für Patentanwälte agentisch in Espacenet Google Patents DPMAregister DEPATISnet EPO Register WIPO USPTO. Stand der Technik Neuheit Paragraf 3 PatG Art. 54 EPÜ erfinderische Tätigkeit Paragraf 4 PatG Art. 56 EPÜ Problem-Solution-Approach FTO CPC IPC INPADOC Recherchebericht. |
| [`patentrecht`](./patentrecht) | Großes Patentrechts-Plugin für Erfindungsaufnahme, Patentanmeldung, Anspruchsentwurf, Recherche, Neuheit, erfinderische Tätigkeit, FTO, Abmahnung, Claim Chart, Vorbenutzungsrecht, Lizenz, Erfinderbenennung, Einspruch, Nichtigkeit, Register und Fristen. |
| [`phishing-vorfall-pruefer`](./phishing-vorfall-pruefer) | Freistehender Phishing-Vorfall-Prüfer für Online-Banking: BGB Paragraf 675u, Paragraf 675v, Paragraf 675w, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Bankpflichten, Schlichtung und Klage. |
| [`preussisches-allgemeines-landrecht-pralr`](./preussisches-allgemeines-landrecht-pralr) | PrALR-Plugin zum Allgemeinen Landrecht für die Preußischen Staaten: Quellenkritik, Textzeugen, Zivilrecht, Staats-/Polizeirecht, Strafrecht, Ständerecht, Aufopferung und Rezeptionsgeschichte. |
| [`private-equity-praxis`](./private-equity-praxis) | Private-Equity-Praxis-Plugin für deutsche Kanzleien, Investoren, Fonds, Family Offices und Unternehmen: Fund Formation, KAGB/AIF, ELTIF, Deal Execution, Private Credit, Schuldschein, LMA, NPL, Portfolio, Exit und Distressed. |
| [`produktrecht`](./produktrecht) | Produkthaftung und Produktrecht: Produktsicherheit, GPSR, ProdHaftG, deliktische Produzentenhaftung, Right to Repair, Software-/OTA-Updates, digitale Produktlebenszyklen, Rückruf, Marktüberwachung und Launch-Review. |
| [`prozessrecht`](./prozessrecht) | Prozessrechtliche Skills für Mandate, Fristen, Mahnbescheid, Eilverfahren, Vollstreckung und Schriftsätze. |
| [`pruefungsrecht-hochschule`](./pruefungsrecht-hochschule) | Hochschulprüfungsrecht: Prüfungsordnung, Bewertungsspielraum, Akteneinsicht, Krankheit, Nachteilsausgleich, Täuschung, KI, Drittversuch und Eilrechtsschutz. |

### R

| Plugin | Beschreibung |
| --- | --- |
| [`rechtsberatungsstelle`](./rechtsberatungsstelle) | Pro-Bono- und Rechtsberatungsstellen (RDG-konform): Mandantenintake, Fristenkontrolle, Übergabe am Semesterende, mandantenfreundliche Briefe. |
| [`rechtstheorie-rechtsphilosophie`](./rechtstheorie-rechtsphilosophie) | Rechtstheorie- und Rechtsphilosophie-Plugin für juristische Praxis: Rechtsbegriff, Kelsen-orientierte Normgeltung, Demokratie, Rechtsrealismus, Systemdenken, Besitzdogmatik, Law-and-Economics, Hayek-Wissensproblem, spontane Ordnung, Machtkritik und anti-dezisionistische Red-Team-Prüfung. |
| [`regulatorisches-recht`](./regulatorisches-recht) | Aufsichtsrecht – KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds, Wochendigest. |
| [`relationstechnik-zivilrecht`](./gerichtsplugins/relationstechnik-zivilrecht) | Relationstechnik Zivilrecht: Klägerstation, Beklagtenstation, Beweisstation und Entscheidungsstation mit Schlüssigkeit, Erheblichkeit, Beweislast, Hinweisen und Urteilsvotum. |
| [`rentenpruefer`](./rentenpruefer) | Rentenprüfer für Arbeitnehmer: DRV-Kontenklärung, Alters- und Erwerbsminderungsrente, Betriebsrente, private Renten, Versorgungswerk-Schnittstellen, Bescheid, Widerspruch und Klage. |
| [`richter-amtsgericht-handelsregister`](./gerichtsplugins/richter-amtsgericht-handelsregister) | Handelsregisterrichter und Rechtspfleger: Ersteintragung Änderungen Löschung Zwischenverfügung Beschwerde Eintragungsfähigkeit Firmenrecht Vertretungsmacht Liquidation und Löschung von Amts wegen |
| [`richter-amtsgericht-insolvenz-restrukturierung`](./gerichtsplugins/richter-amtsgericht-insolvenz-restrukturierung) | Insolvenz- und Restrukturierungsgericht: Eröffnungsverfahren Sicherungsmaßnahmen Verwalterauswahl Gläubigerversammlung Prüfungstermin Schlusstermin Restschuldbefreiung Restrukturierungssache nach StaRUG mit Stabilisierungsanordnung und Planbestätigung |
| [`richter-amtsgericht-straf`](./gerichtsplugins/richter-amtsgericht-straf) | Strafrichter Amtsgericht: Eröffnungsentscheidung Hauptverhandlung Beweiswürdigung Strafzumessung Urteilsbegründung Rechtsmittelbelehrung Strafbefehl beschleunigtes Verfahren mit Tenorvorschlag |
| [`richter-amtsgericht-zivil`](./gerichtsplugins/richter-amtsgericht-zivil) | Amtsrichter Zivilsachen: Schlüssigkeit Erheblichkeit Beweis Tenor Kostenentscheidung Streitwertbeschluss vorläufige Vollstreckbarkeit Rechtsmittelbelehrung Versäumnisurteil und Anerkenntnisurteil mit echter Relation und Entscheidungsvorschlag |
| [`richter-arbeitsgericht`](./gerichtsplugins/richter-arbeitsgericht) | Arbeitsgericht: Gütetermin Kammertermin Kündigungsschutzklage Zahlungsklage einstweilige Verfügung Beschlussverfahren Betriebsverfassung Streitwert mit Tenorvorschlag |
| [`richter-bverfg-verfassungsbeschwerden`](./gerichtsplugins/richter-bverfg-verfassungsbeschwerden) | BVerfG Kammer und wissenschaftliche Mitarbeiter: Annahmeprüfung Verfassungsbeschwerde Paragraf 93a BVerfGG Substantiierung Subsidiarität Grundrechtsverletzung Rechtswegerschöpfung Voten Kammerbeschluss Nichtannahmebeschluss |
| [`richter-familiengericht`](./gerichtsplugins/richter-familiengericht) | Familiengericht: Ehesachen Scheidung Versorgungsausgleich Kindschaftssachen elterliche Sorge Umgang Kindesunterhalt Trennungs- und Ehegattenunterhalt Gewaltschutz Adoption Vormundschaft Betreuungsteile mit Verfahrenskostenhilfe und Tenorvorschlag |
| [`richter-finanzgericht`](./gerichtsplugins/richter-finanzgericht) | Finanzgericht: Sachprüfung Anfechtungsklage Verpflichtungsklage Aussetzung der Vollziehung Paragraf 69 FGO Beweiswürdigung im Amtsermittlungsgrundsatz und Urteilsentwurf mit Tenorvorschlag |
| [`richter-landgericht-strafkammer`](./gerichtsplugins/richter-landgericht-strafkammer) | Strafkammer LG: Eröffnungsentscheidung Hauptverhandlung Beweiswürdigung Strafzumessung schwere und mittlere Kriminalität Berufung gegen Amtsgerichtsurteil Sicherungsverwahrung und Maßnahmen mit Tenorvorschlag |
| [`richter-landgericht-zivilkammer`](./gerichtsplugins/richter-landgericht-zivilkammer) | Zivilkammer LG: erste Instanz und Berufung, große Relation, Schlüssigkeit Erheblichkeit Beweis, Hinweisverfügung Paragraf 139 ZPO, Beweisbeschluss, Sachverständigenbeweis, Urteil Paragraf 313 ZPO, Berufungsentscheidung Paragrafen 522-540 ZPO mit Tenorvorschlag |
| [`richter-sozialgericht`](./gerichtsplugins/richter-sozialgericht) | Sozialgericht: Klagearten Anfechtungs- und Leistungsklage einstweiliger Rechtsschutz Paragraf 86b SGG Amtsermittlung sozialrechtliche Prüfungsschemata Krankenversicherung Rente Unfall Bürgergeld Schwerbehinderung Urteilsentwurf mit Tenorvorschlag |
| [`richter-verwaltungsgericht`](./gerichtsplugins/richter-verwaltungsgericht) | Verwaltungsgericht: Sachprüfung Anfechtungs- und Verpflichtungsklage einstweiliger Rechtsschutz Paragraf 80 Abs. 5 VwGO Hauptsacheentscheidung Beweiswürdigung im Amtsermittlungsgrundsatz und Tenorvorschlag |
| [`robotik-recht`](./robotik-recht) | Robotik-Recht Deutschland/EU: Maschinenverordnung, KI-VO, Produkthaftung, ProdSG, Datenschutz, CRA, Data Act, CE, Marktüberwachung, Unfälle, Rückruf, Verträge und Robotik-Testakte. |
| [`roemisch-katholisches-kirchenrecht`](./roemisch-katholisches-kirchenrecht) | Großes, lehramts- und papsttreues Arbeitsplugin zum Recht der römisch-katholischen Kirche: CIC, Katechismus, Sakramente, Ehe, Kirchenaustritt, Verfahren, Disziplin, Pfarrei, Diözese, Kurie und mehrsprachige Kommunikation. |
| [`roemisches-recht`](./roemisches-recht) | Mega-Plugin zum römischen Recht: Zwölftafelgesetz, Institutionensystem, Sachenrecht, Obligationen, Aktionenrecht, Erbrecht, Juristenrecht, Justinian, byzantinisches Recht und Rezeption. |

### S

| Plugin | Beschreibung |
| --- | --- |
| [`schoeffen-handelsrichter-praxis`](./schoeffen-handelsrichter-praxis) | Plugin für Schöffen, Jugendschöffen, ehrenamtliche Richter und Handelsrichter: Rolle, Rechte, Pflichten, Sitzung, Beratung, Befangenheit, Beweiswürdigung, Handelskammer, Verwaltungsgericht und sichere praktische Orientierung. |
| [`schriftform-und-textform-bgb`](./schriftform-und-textform-bgb) | Formerfordernisse im deutschen Zivilrecht: Schriftform, Textform, qES, Zugang, beA/ERV und Prozessordnungen. Mit Checklisten, Dokumentation und Rechtsprechung nur nach Live-Verifikation. |
| [`schriftsatz-versandwerkstatt`](./schriftsatz-versandwerkstatt) | Fokussierte Versandwerkstatt für fertige Schriftsätze und Anlagen: konvertiert Dateien in PDF, stempelt Anlagen, prüft Dateinamen, Paketgrenzen, Absender, Signaturweg und Eingang und liefert eine kontrollierte beA-Mappe. |
| [`schulrecht-laender`](./schulrecht-laender) | Schulrecht der Länder: Schulpflicht, Aufnahme, Inklusion, Noten, Versetzung, Ordnungsmaßnahmen, Datenschutz, Elternrechte und Eilrechtsschutz. |
| [`seerecht-schifffahrtsrecht`](./seerecht-schifffahrtsrecht) | See- und Schifffahrtsrecht-Plugin für Schiffskauf, Schiffbau, Werften, Schiffshypothek, Schiffsregister, Arrest, Wrack, Bergung, Charter und ITLOS. |
| [`selbstvertreter-amtsgericht`](./selbstvertreter-amtsgericht) | Selbstvertretung vor dem Amtsgericht ohne Anwalt: Anfänger-Workflow, Fristen, Zuständigkeit, Paragraf23 GVG/Paragraf511 ZPO-Grenzen, Klage/Erwiderung/Replik, Beweise, PKH, Termin, Sanity-Check, Rechtsprechungschat, Berufung. |
| [`selbstvertreter-sozialgericht`](./selbstvertreter-sozialgericht) | Selbstvertretung vor Sozialbehörden Krankenkassen Pflegekassen BG Versorgungsamt Jobcenter Rente Familienkasse und Sozialgericht: Anhörung Akteneinsicht Mitwirkung Widerspruch Klage Eilantrag Pflegegrad Hilfsmittel Krankengeld EM-Rente GdB Bürgergeld Wohngeld Eingliederungshilfe. |
| [`softwarerecht-de-eu-us`](./softwarerecht-de-eu-us) | Softwarerecht Deutschland/EU/International/USA: Entwicklung, Lizenzen, SaaS, Open Source, Arbeitnehmer/Freelancer, Softwarepatente, AI-Code und Streit. |
| [`solo-selbststaendige-praxis`](./solo-selbststaendige-praxis) | Praxisplugin für Solo-Selbstständige in Deutschland: Start, Anmeldung, Steuern, Verträge, Rechnungen, Datenschutz, Statusfeststellung, KSK, Versicherungen, Zahlungsausfall, Krise, Wachstum und Alltag ohne juristische Überforderung. |
| [`sozialversicherungsstatus-pruefer`](./sozialversicherungsstatus-pruefer) | Sozialversicherungsstatus und DRV-Statusfeststellung: Geschäftsführer, Freelancer, Anwälte, Lehrkräfte, Musikschulen, Plattformarbeit und Scheinselbständigkeit. |
| [`staatsanwaltschaft-amtsanwaltschaft`](./gerichtsplugins/staatsanwaltschaft-amtsanwaltschaft) | Staatsanwaltschaft und Amtsanwaltschaft: Ermittlungsführung, Durchsuchung, Haft, Einstellung, Strafbefehl, Anklage, Einziehung, Plädoyer, Rechtsmittel und Vollstreckung. |
| [`staatsanwaltschaft-praxis-einstieg`](./gerichtsplugins/staatsanwaltschaft-praxis-einstieg) | Praxisplugin für neue Staatsanwälte: Aktenstart, Anfangsverdacht, Ermittlungsauftrag, Eingriffe, Anklage, Strafbefehl, Einstellung, Sitzungsdienst, Rechtsmittel und OWiG. |
| [`startup-hr-personalabteilung-berlin`](./startup-hr-personalabteilung-berlin) | Personalabteilungs- und HR-Operations-Plugin für ein Berliner Start-up mit ca. 100 Beschäftigten: Arbeitsverträge, Payroll/DATEV-Schnittstelle, Personalakten, Datenschutz, AGG-Vorfälle, Betriebsrat, Benefits, Fehlzeiten, Kündigungen, Happiness-Management und Chef-Briefings. |
| [`status-navigator-step-plan`](./status-navigator-step-plan) | Status-Navigator und Step-Plan-Macher. Reine Dokumentenverarbeitung mit 35 Skills. Strukturiert disparate Dokumentenlagen in eine mehrseitige Excel-Arbeitsmappe und optional ein Padlet-Shelf mit Reitern Überblick, Vorhanden, Fehlend und Workflow. Keine rechtliche Bewertung. |
| [`steuerrecht-anwalt-und-berater`](./steuerrecht-anwalt-und-berater) | Steuerrecht für Anwalt (anw- FAO Paragraf 9) und Steuerberater (stb-): Einspruch Klage FG Außenprüfung Selbstanzeige, Grundsteuer, Grunderwerbsteuer, Share Deals, Signing Closing, BWA SuSa Lohnbuchhaltung Jahresabschluss. |
| [`strafanzeige-vorbereiter`](./strafanzeige-vorbereiter) | Vorsichtiger Strafanzeigen-Vorbereiter: prüft Anfangsverdacht, Beweise, Strafantrag, Risiken falscher Verdächtigung, Alternativen und erstellt nur bei tragfähiger Tatsachengrundlage eine nüchterne Strafanzeige. |
| [`strafbefehl-verteidiger`](./strafbefehl-verteidiger) | Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung. |
| [`strafzumessung`](./strafzumessung) | Strafzumessung nach deutschem Strafrecht vom Strafbefehl bis zur großen Strafkammer. Paragraf 46 StGB Strafzumessungstatsachen Tagessatz Geldstrafe Freiheitsstrafe Bewährung Paragraf 56 Paragraf 49 Regelbeispiele besonders schwerer Fall Verständigung Paragraf 257c StPO TOA Paragraf 46a Gesamtstrafe Paragraf 55 JGG. |
| [`strassenrecht-infrastruktur`](./strassenrecht-infrastruktur) | Straßenrecht-Plugin für Bundesfernstraßen, Landesstraßen, Gemeindestraßen, Widmung, Planfeststellung, Sondernutzung, Baulast und Erhaltung. |
| [`strassenverkehrsrecht-stvo`](./strassenverkehrsrecht-stvo) | StVO-/Straßenverkehrsrecht-Plugin für Verkehrsregeln, Zeichen, Anordnungen, Ausnahmegenehmigungen, Fahrerlaubnis, Bußgeld-Schnittstellen und Behördenpraxis. |
| [`subsumtions-pruefer`](./subsumtions-pruefer) | Interaktiver Subsumtions-Workflow für deutsches Recht und Europarecht: Tatbestandsmerkmale zerlegen, Vier-Schritt-Schema anwenden, Rechtsfolgen und Einreden prüfen. Keine Rechtsberatung. |

### T

| Plugin | Beschreibung |
| --- | --- |
| [`tabellenreview-3d`](./tabellenreview-3d) | 3D-Tabellenreview als Würfel: Spaltenprompts pro Datenpunkt x Zeilenprompts pro Dokument x Arbeitsblatt-Perspektiven (Recht / Steuer / Wirtschaft) gestapelt. Massenprüfung Vertragsstapel M&A-DD Immobilien Vendor-Onboarding mit Excel-Mehrblatt Kreuzblatt-Konsistenz Audit-Trail Belegkette. |
| [`telekommunikationsrecht`](./telekommunikationsrecht) | Großes Telekommunikationsrecht-Plugin für TKG, Bundesnetzagentur, Internetanschlüsse, Anbieterwechsel, Kundenschutz, Netzregulierung, Frequenzen, Nummerierung, Sonderkartellrecht, Datenschutz und Sicherheitsanforderungen. |
| [`tierschutzrecht`](./tierschutzrecht) | Tierschutzrecht-Plugin für TierSchG, BGB Paragraf 90a, Haltung, Zucht, Transport, Tierversuche, Behördenverfahren, Strafrecht, Bußgeld und zivilrechtliche Tierfälle. |

### U

| Plugin | Beschreibung |
| --- | --- |
| [`umweltrecht`](./umweltrecht) | Freistehendes Umweltrecht-Plugin für BImSchG, TEHG, Abfall, Wasser, Boden, Naturschutz, UIG, Verfahren, Bußgeld, Umwelt-Due-Diligence, Klimaklagen UmwRG, Lieferkettensorgfalt LkSG/CSDDD und ESG-Greenwashing/CSRD. |
| [`umweltschutzverband-verbandsklage`](./umweltschutzverband-verbandsklage) | Plugin für Umweltverbände: UmwRG, Aarhus, UIG, UVP, BImSchG, Planfeststellung, Paragraf 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz. |
| [`urheberrecht-de-eu`](./urheberrecht-de-eu) | Deutsches und EU-Urheberrecht für Werkhöhe, Musik, KI, TDM, Software, Lizenzen, Abmahnung, Schranken, Leistungsschutz und Rechteclearing. |
| [`urteilsbauer-relationsmacher`](./urteilsbauer-relationsmacher) | Urteils- und Beschluss-Werkstatt für Amts- Land- und Familienrichter sowie Rechtspfleger. Aktenintake Relation Beweiswürdigung mit Richter-Input Tatbestandsmerkmale Tenor Tatbestand Entscheidungsgründe Rechtsmittelbelehrung. Erzeugt DOCX nach Paragraf 313 ZPO. |
| [`us-bankruptcy-code`](./us-bankruptcy-code) | US Bankruptcy Code Title 11: Chapters 7/9/11/12/13/15, Automatic Stay, Claims, DIP, 363 Sales, Plans und Cross-Border. |
| [`us-copyright-registrierung-verlag`](./us-copyright-registrierung-verlag) | US Copyright Act für deutsche Verlage und Rechteinhaber: Title 17, Registrierung, Rechte, Fair Use, DMCA, Musik, AI, Litigation und Deals. |

### V

| Plugin | Beschreibung |
| --- | --- |
| [`venture-capital-geber`](./venture-capital-geber) | VC-Geber-Plugin für deutsche Venture-Capital-Investoren, Family Offices, Angels und junge VCs: Sourcing, Deal-Tracking, Wandeldarlehen, SAFE, Pre-Seed, Series A/B, Cap Table, Follow-on, Portfolio-Updates, KAGB/BaFin-Grenzen, EU/CH/UK/US-Brücken und legitime Deal-Taktik. |
| [`verbraucher-rechtsstaat-alltag`](./verbraucher-rechtsstaat-alltag) | Kleines, hilfreiches Plugin für Verbraucher: E-Commerce, Kaufrecht, Reparaturen, kleine Dienstleistungen, Rechnungen, Inkasso, Plattformen, Behördenbriefe und Gerichtspost verständlich einordnen und vorsichtig reagieren. |
| [`verbraucherinsolvenz-schuldenbereinigung`](./verbraucherinsolvenz-schuldenbereinigung) | Verbraucherinsolvenz und Schuldenbereinigung nach InsO: außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, Antrag, Restschuldbefreiung, P-Konto, ehemalige Selbstständige und lebensnahe Verfahrensführung. |
| [`verbraucherschutzrecht-pruefer`](./verbraucherschutzrecht-pruefer) | Großer Verbraucherschutz-Prüfer für BGB, EGBGB, UWG, UKlaG, VSBG, E-Commerce, digitale Produkte, Reise, Finanzen, Energie, Gesundheit und Alltag. |
| [`verbraucherschutzverband-durchsetzung`](./verbraucherschutzverband-durchsetzung) | Plugin für Verbraucherverbände: VDuG, UKlaG, UWG, Abhilfeklage, Musterfeststellung, Unterlassung, Register, Finanzierung, Vergleich und Kampagnenakte. |
| [`vereinsrecht-vereinsmanager`](./vereinsrecht-vereinsmanager) | Vereinsrechts- und Vereinsmanagement-Plugin für eingetragene und nicht eingetragene Vereine: Gründung, Satzung, Mitgliederversammlung, Vorstand, Protokolle, Beschlüsse, Gemeinnützigkeit, Register, Haftung, Datenschutz, Finanzen, Veranstaltungen und Spezialvereine. |
| [`verfassungsrecht`](./verfassungsrecht) | Deutsches Verfassungsrecht: BVerfG-Recherche, Prozessarten-Navigator nach Paragraf 13 BVerfGG, Verfassungsbeschwerde, Paragraf 32-BVerfGG-Eilrechtsschutz, Organstreit, Bund-Länder-Streit, Parteienverfahren, Normenkontrolle, Grundrechte, EU-Grundrechte und Gesetzgebungskompetenz. |
| [`verhaeltnismaessigkeitspruefer`](./verhaeltnismaessigkeitspruefer) | 85 Skills zur Schranken-Schranke: BVerfG-Leitentscheidungen, Drittwirkung, Gleichheitsdogmatik, PrOVG-Kreuzberg, Südafrika/Kanada/EGMR/EuGH/USA und 12 europäische Ordnungen; mit Alexy, Schnellprüfung, Klausurschema, Streitstellen, Subsumtionshelfer und Visualisierung. |
| [`verkehr-infrastrukturrecht`](./verkehr-infrastrukturrecht) | Freistehendes Verkehrs- und Infrastrukturrecht-Plugin für Verkehrsplanung, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Parkraum und Verkehrswende. |
| [`verkehrsowi-verteidiger`](./verkehrsowi-verteidiger) | Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht. |
| [`verlagsrecht-buchpreisbindung`](./verlagsrecht-buchpreisbindung) | Plugin für Verlagsrecht, Verlagsgesetz, Autoren- und Herausgeberverträge, Buchpreisbindung, Titelschutz, Vertrieb, E-Book, Hörbuch und verlagsnahe Compliance. |
| [`verlagsredaktion`](./verlagsredaktion) | Verlagsdesk für juristische und fachliche Verlage: Eingangskorb, Manuskript, Redaktion, Rechtecheck, Zitate, Bildrechte, Autorenkommunikation, Heftplanung, Buchprojekte, Satzfahnen, Metadaten, Marketing und Produktionsübergabe. |
| [`versammlungsrecht`](./versammlungsrecht) | Praxisplugin für Versammlungsrecht und Versammlungsfreiheit: Anzeige unter freiem Himmel, Landesrecht, Behörde, Fristen, Spontan- und Eilversammlung, Ordner, Kooperationsgespräch, Auflagen, Verbot, Eilrechtsschutz und Durchführung ohne vorauseilende Selbstzensur. |
| [`versicherungsrecht`](./versicherungsrecht) | Großes Versicherungsrecht-Plugin für VVG, VAG, europäische Versicherungsaufsicht, Lebensversicherung, BU, PKV, Rechtsschutz, Kreditversicherung, D&O, Cyber, Sach- und Haftpflichtdeckung. |
| [`vertragsausfueller`](./vertragsausfueller) | Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten. |
| [`vertragsrecht`](./vertragsrecht) | Vertragsrecht – Lieferanten- und Vertriebsverträge, AGB Paragrafen 305 ff. BGB, NDA, SaaS-/MSA-Review, Renewal-Tracking, Eskalations-Routing, Business-Zusammenfassungen. |

### W

| Plugin | Beschreibung |
| --- | --- |
| [`wahlkampfrecht-praxis`](./wahlkampfrecht-praxis) | Wahlkampfrecht und Wahlkampfpraxis für Parteien, Kandidierende und Kampagnenteams: Strategie, Plakatierung, Social Media, Datenschutz, politische Werbung, Parteienfinanzierung, Desinformation, Veranstaltungen, Schulen, Podien, Wahltag und Compliance. |
| [`wandeldarlehen-lebenszyklus`](./wandeldarlehen-lebenszyklus) | Begleitet den vollständigen Lebenszyklus eines Wandeldarlehens für GmbH und UG: Vertragserstellung (bilingual/einsprachig), Beurkundungsprüfung, Wandelereignisse, Wandlungsberechnung, Cap-Table-Update, Gesellschafterbeschluss und Notar-Paket. |
| [`weg-hausverwaltung`](./weg-hausverwaltung) | Operatives WEG- und Hausverwaltungs-Plugin für Beschlüsse, Eigentümerversammlung, Protokoll, Beschlusssammlung, Wirtschaftsplan, Jahresabrechnung, Hausgeld, Sonderumlage, Betriebskosten, Handwerker, bauliche Veränderungen, Steckersolar, Wallbox, Verwalter, Beirat und Anwalt-Eskalation. |
| [`weltraumrecht`](./weltraumrecht) | Großes Plugin für deutsches, europäisches und internationales Weltraumrecht: Raumfahrtverträge, Satelliten, Haftung, Weltraumbahnhof, Raketen, Raumstationen, Frequenzen, Exportkontrolle und Space Property. |
| [`word-legal-ai-plugin-and-skill-for-german-lawyers`](./word-legal-ai-plugin-and-skill-for-german-lawyers) | Word Legal AI for German Lawyers: Kaltstart, Kanzleistil, makrofreies Word-Finish, Verträge, Schriftsätze, Memos, Redlines, Klauselbibliothek, Defensive Drafting, Term Sheet, DE-EN Bilingual, US/UK Legal Writing und englische Verträge nach deutschem Recht. |

### Z

| Plugin | Beschreibung |
| --- | --- |
| [`zitierweise-deutsches-recht`](./zitierweise-deutsches-recht) | Deutsche juristische Hauszitierweise v4.0: Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. |
| [`zwangsverwaltung-zvg`](./zwangsverwaltung-zvg) | Freistehendes ZVG-Plugin für Zwangsverwaltung und Versteigerung: Beschlagnahme, Besitz, Mieten, Treuhandkonto, Berichte, Verteilung, ZVG-Portal-Recherche, Bieterangebote und Versteigerungsteilnahme. |
| [`zwangsvollstreckung`](./zwangsvollstreckung) | Plugin Zwangsvollstreckung Paragrafen 704 ff. ZPO: Mahn-/Vollstreckungsbescheid, PfÜB Bank/Arbeit, Paragraf 802l Kontensuche, Vermögensauskunft, Räumung, Paragraf 800 ZPO Notar, Paragraf 201 InsO, ZVG, EU-Kontenpfändung VO 655/2014, Paragraf 765a Härtefall, Schuldnerschutz. |

<!-- END PLUGIN-KATALOG (auto-generated) -->

## Weitere Installationshilfe

Die kompakte Anleitung mit den drei Nutzungswegen steht im [Schnellstart](./QUICKSTART.md). Hinweise zu automatisch entpackten ZIPs, zur richtigen Dateiauswahl und zum Organisations-Marketplace stehen in [Installation in einfach](./INSTALLATION_EINFACH.md).

## Repo-interner Release-Check

Vor einem Release sollten mindestens diese Prüfungen grün sein:

```bash
node scripts/validate-marketplace-import.mjs
node scripts/validate-plugin-structure.mjs
python3 scripts/validate-yaml-frontmatter.py
```

## Schwerpunkte für die deutsche Praxis

Dieses Repository ist vollständig auf das deutsche Recht und die Arbeitsweise deutscher Kanzleien zugeschnitten:

- Urteile sind nicht bindend; Ausnahme: § 31 BVerfGG.
- Vorprozessuale Beweiserhebung ist auf eng begrenzte gesetzliche Instrumente beschränkt: §§ 142, 144 ZPO; § 810 BGB; § 242 BGB; Art. 15 DSGVO; Auskunfts- und Stufenklage (§ 254 ZPO).
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und verifizierbarer Quelle zitieren; BeckRS-, Kommentar- und Aufsatz-Blindzitate sind gesperrt.
- Zitierweise und Quellenprüfung: verbindlich in der [Referenz zur Zitierweise](./references/zitierweise.md).
- Due Diligence läuft über Q&A, Datenraum und anwaltliche Sachverhaltsaufklärung.
- Kündigungsschutz: Regelfall nach KSchG ab 6 Monate / mehr als 10 Arbeitnehmer.

### Materielle Rechtsgebiete

- **Zivilrecht & Vertragsrecht** – `bgb-at-pruefer`, `bgb-bt-pruefer`, `vertragsrecht`, `nda-abgleich`, `agb-pruefung` (in `vertragsrecht`), `produktrecht`, `fluggastrechte`
- **Arbeitsrecht** – `arbeitsrecht`, `fachanwalt-arbeitsrecht` (Kündigungsschutzklage § 4 KSchG, Aufhebungsvertrag mit Sperrzeit-Prüfung, BR-Anhörung § 102 BetrVG, Massenentlassung § 17 KSchG)
- **Gesellschafts- & Wirtschaftsrecht** – `gesellschaftsrecht`, `gesellschaftsrecht-legal-english`, `fachanwalt-handels-gesellschaftsrecht`, `grosskanzlei-corporate-ma`, `mittelstand-corporate-ma`, `corporate-kanzlei`, `private-equity-praxis`, `venture-capital-geber`, `fachanwalt-internationales-wirtschaftsrecht`
- **Bank-, Kapitalmarkt- & Aufsichtsrecht** – `bank-rechtsabteilung`, `fachanwalt-bank-kapitalmarktrecht`, `private-equity-praxis`, `venture-capital-geber`, `regulatorisches-recht`, `berichtspflichten-erlediger`, `geldwaeschepraevention-aml-kyc`, `aussenwirtschaft-zoll-sanktionen`
- **Insolvenz & Sanierung** – Einstieg über die [Insolvenzrecht-Übersicht](./insolvenzrecht-plugins/) mit Routing nach Krise, Forderungsanmeldung, Insolvenzverwaltung, Insolvenzplan/StaRUG, Verbraucherinsolvenz, Fortbestehensprognose und US-Bankruptcy-Schnittstelle; die Einzelplugins bleiben `insolvenzrecht`, `insolvenzverwaltung`, `zwangsverwaltung-zvg`, `insolvenzforderungsanmeldungspruefung`, `insolvenzplan-starug-planwerkstatt`, `fortbestehensprognose`, `krisenfrueherkennung-starug`, `liquiditaetsplanung`, `verbraucherinsolvenz-schuldenbereinigung`, `fachanwalt-insolvenz-sanierungsrecht` und `us-bankruptcy-code`.
- **Liquidität, Forderung & Inkasso** – `liquiditaetsplanung`, `forderungsmanagement-klagewerkstatt`, `phishing-vorfall-pruefer`, `vertragsausfueller`, Inkasso nach RDG / § 43d BRAO (in `regulatorisches-recht`)
- **Steuerrecht und Förderung** – `steuerrecht-anwalt-und-berater` (Bescheidanalyse, Einspruch, Außenprüfung, Selbstanzeige, Grundsteuer, Grunderwerbsteuer, Share Deals, weltweite DBA-Matrix, Signing/Closing, Steuerberater-Werkzeuge), `berichtspflichten-erlediger`, `forschungszulage-antragstellung`, `dfg-foerderantrag`
- **Strafrecht & OWi** – `aktenaufbereiter-strafrecht`, `fachanwalt-strafrecht`, `strafanzeige-vorbereiter`, `strafbefehl-verteidiger`, `strafzumessung`, `verkehrsowi-verteidiger`
- **Verwaltungs- & Verfassungsrecht** – `verfassungsrecht`, `verhaeltnismaessigkeitspruefer`, `versammlungsrecht`, `wahlkampfrecht-praxis`, `fachanwalt-verwaltungsrecht` (Eilantrag § 80 V VwGO), `verkehr-infrastrukturrecht`, `umweltrecht`, `energierecht`, `normenkontrollrat-nkr`, `fachanwalt-vergaberecht`
- **Familien-, Erb-, Sozial- & Betreuungsrecht** – `fachanwalt-familienrecht` (Düsseldorfer Tabelle, Sorge, Umgang, Unterhalt), `fachanwalt-erbrecht` (Pflichtteilsberechnung), `fachanwalt-sozialrecht`, `rentenpruefer`, `betreuungsrecht`, `fachanwalt-migrationsrecht`
- **Miet- & Immobilienrecht** – `mietrecht`, `weg-hausverwaltung`, `nachbarschaftsstreit-pruefer`, `fachanwalt-miet-wohnungseigentumsrecht`, `immobilienrechtspraxis`
- **Gewerblicher Rechtsschutz & Medien** – `gewerblicher-rechtsschutz` (Markenanmeldung DPMA, UWG-Abmahnung), `fachanwalt-gewerblicher-rechtsschutz`, `fachanwalt-urheber-medienrecht` (Gegendarstellung), `patentrecht`, `patentrecherche`, `gebrauchsmusterrecht`, `designrecht-geschmacksmusterrecht`, `markenrecht-fashion-luxus` (DPMA/EUIPO/WIPO/USPTO, Markenarten, Klassen, Benutzung, Verfall/Nichtigkeit, Enforcement, Plattformen, Zoll, Lizenzen, Luxus-Fashion und US-Trade-Dress), `fashion-law-moderecht` (Mode-Lifecycle, Textilkennzeichnung, Produktsicherheit, Nachhaltigkeit, Lieferkette, Plattformen und Retail)
- **Insolvenz, Sanierung und Krisenmanagement (erweitert)** – gebündelt in der [Insolvenzrecht-Übersicht](./insolvenzrecht-plugins/): Frühwarnung nach § 1 StaRUG, Beraterwarnpflicht § 102 StaRUG, Zahlungsunfähigkeit, Überschuldung, Restrukturierungsplan, Insolvenzplan, Eigenverwaltung, Schutzschirm, Forderungstabelle, Verwalterberichte und Cross-Border-Fälle.
- **Arbeits- und Vergütungsrecht (erweitert)** – `bav-strategie-konzern` (betriebliche Altersversorgung als Konzern-Architektur: alle fünf Durchführungswege, CTA-Doppeltreuhand, Pension Buyouts, Drei-Stufen-Prüfung, internationale Benefits, Düsseldorf-Kyoto-Profil)
- **IT-Recht, Datenschutz, Telekommunikation, digitale Barrierefreiheit, Robotik & KI-Governance** – `datenschutzrecht` (Art. 15 DSGVO, Art. 33/34 DSGVO), `telekommunikationsrecht` (TKG/Bundesnetzagentur/Internetanschluss), `barrierefreiheit-web-checker` (BFSG/BFSGV/BITV/WCAG), `fachanwalt-it-recht` (Cyber-Incident 72 h), `ki-governance` (EU AI Act), `robotik-recht` (Maschinenverordnung, KI-VO, CRA, Produkthaftung), DORA-IKT-Vertragsprüfung in `regulatorisches-recht`, `berufsrecht-ki-vertragspruefung`
- **Verkehr, Transport, Versicherung, Medizin** – `fachanwalt-verkehrsrecht`, `fachanwalt-transport-speditionsrecht` (CMR/HGB), `versicherungsrecht`, `fachanwalt-versicherungsrecht`, `fachanwalt-medizinrecht`, `fachanwalt-bau-architektenrecht` (VOB/B)
- **Sportrecht, Agrarrecht** – `fachanwalt-sportrecht` (CAS-Berufung), `fachanwalt-agrarrecht` (GAP-Sammelantrag)
- **Europa- & Common-Law-Kompass** – `europarecht-kompass`, `common-law-kompass`

### Querschnittliche Werkzeuge

- **Prozess- & Schriftsatz-Werkstatt** – `prozessrecht` (Mahnbescheid §§ 688 ff. ZPO, einstweilige Verfügung §§ 935/940 ZPO + Schutzschrift, Vollstreckung), `anlagen-zu-schriftsaetzen`, `schriftsatz-versandwerkstatt` (fokussierte PDF-, Anlagen-, Signatur- und beA-Endfertigung mit neun Skills), `status-navigator-step-plan`, `memorandums-ersteller`, `tabellenreview-3d`
- **Kanzleibetrieb** – `kanzlei-allgemein`, `kanzlei-builder-hub`, `kanzlei-mandant-lifecycle`, `rechtsberatungsstelle`, `verlagsredaktion`
- **Methode & Lehre** – `jurastudium` (Methodenlehre ZR/StR/ÖR, Subsumtion, Rechtsgeschichte, Lernstrategien, Lösungsschemata, Prüfungsgespräch nach AG-Tradition), `methodenlehre-buergerliches-recht`, `rechtstheorie-rechtsphilosophie`, `preussisches-allgemeines-landrecht-pralr`, `zitierweise-deutsches-recht`, `einfache-leichte-sprache-jura`
- **Drafting & Sprache** – `word-legal-ai-plugin-and-skill-for-german-lawyers` (39 Skills: Kaltstart-Triage, deutscher Kanzleistil, makrofreies Word-Finish, Verträge, Schriftsätze, Memos, Klauselbibliothek, Defensive Drafting, Entwurfscheck/Red Team, Term Sheet, DE-EN Bilingual, US/UK Legal Writing, englische Verträge nach deutschem Recht), `juristische-sprache-deutsch-als-zweitsprache` (Juristendeutsch, Bescheide, Fristen und Formulare für Nichtmuttersprachler)

Eine vollständige Übersicht aller Plugins und Rechtsgebiete steht in [references/rechtsgebiete-uebersicht.md](./references/rechtsgebiete-uebersicht.md). Die kompakte Plugin-Liste findest du im Abschnitt ["Was ist drin?"](#was-ist-drin) weiter oben.

## Verbindliche Zitierweise

Jeder Skill verweist auf die [verbindliche Zitierweise](./references/zitierweise.md). Die Kernregeln in Kurzfassung:

- Rechtsprechung: Vor Ausgabe über eine amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage prüfen.
- **Kostenlose Quelle:** Wo möglich Link zu offizieller Datenbank oder frei zugänglichem Volltext ergänzen; Datenbankkürzel wie BeckRS nicht ausdenken.
- **Literatur:** Kommentare, Bücher und Aufsätze nur zitieren, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert. Keine Blindzitate.

Pflicht: Datum + Aktenzeichen + verifizierbare Fundstelle + Randnummer bei Rechtsprechung. Unverifizierte Rechtsprechung wird als Prüfbedarf markiert oder weggelassen.

### Methodenlehre und Zitierweise als zuschaltbare Plugins

Die Inhalte aus [references/methodik-buergerliches-recht.md](./references/methodik-buergerliches-recht.md) und [references/zitierweise.md](./references/zitierweise.md) liegen zusätzlich als zwei eigenständige, einzeln aktivierbare Plugins im Marketplace:

- [methodenlehre-buergerliches-recht](./methodenlehre-buergerliches-recht) — Gutachtenstil, Anspruchsgrundlagen-Reihenfolge, Auslegungskanones, Abwägung, Präzedenzarbeit, Generalklauseln und Rechtsfortbildung als reale Werkzeuge.
- [rechtstheorie-rechtsphilosophie](./rechtstheorie-rechtsphilosophie) — Rechtsbegriff, Kelsen-orientierte Normgeltung, Kompetenzketten, Gesetzesbindung, Demokratie, Systemkritik, Verwaltungsrealismus, Besitzdogmatik, Law-and-Economics, Hayek-Wissensproblem, spontane Ordnung und anti-dezisionistische Machtkritik.
- [zitierweise-deutsches-recht](./zitierweise-deutsches-recht) — Hauszitierweise mit Pinpoint-Randnummer, Rechtsprechungs-Verifikationsregel, BeckRS-Sperre und Literatur-Sperre ohne Nutzerquelle oder lizenzierten Live-Zugriff.

Alle drei Plugins enthalten die einschlägigen Inhalte als Skills: Sobald sie aktiviert sind, stehen Methodik, Rechtstheorie und Zitierweise als ausdrückliche Arbeitsmaßstäbe neben dem jeweiligen Rechtsgebietsplugin bereit.

Aktivierung in Cowork: zuerst den Cowork-Bereich öffnen, dann `Customize → Plugins`; dort die drei Plugins installieren oder aktivieren.

## Für Einsteiger: Schritt-für-Schritt-Anleitung

### Was brauche ich?

1. **Einen kostenpflichtigen Claude-Plan** für Plugins; die reinen Markdown-Schnellstarts funktionieren auch ohne Plugin-Installation.
2. **Claude im Web, Claude Desktop oder Cowork**; für die Kommandozeilen-Installation Claude Code.
3. **Für die Einzelinstallation:** ein Plugin-ZIP aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). **Für Entwickler:** dieses Repository mit Git klonen.

### Einzelinstallation in Claude Desktop oder Cowork

**Schritt 1: Claude Desktop installieren**

1. Gehe zu https://claude.com/download
2. Lade die Version für dein Betriebssystem herunter (Windows / Mac / Linux)
3. Installiere die Anwendung und melde dich mit deinem Claude-Account an

**Schritt 2: Plugin-ZIP herunterladen**

1. Öffne den [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest).
2. Lade **ein einzelnes Plugin-ZIP** herunter, z. B. `arbeitsrecht.zip`, `vertragsrecht.zip` oder `liquiditaetsplanung.zip`.
3. Auf dem Mac darauf achten: die ZIP nicht entpacken; falls Safari sie automatisch entpackt, erneut als ZIP laden oder die Safari-Auto-Entpackung deaktivieren.

**Schritt 3: Plugin hochladen**

1. In Cowork zuerst den Cowork-Bereich öffnen; im Web oder Desktop direkt fortfahren.
2. In der linken Seitenleiste **Customize** öffnen.
3. Den Reiter **Plugins** wählen und die Funktion zum Hochladen eines eigenen Plugin-ZIPs öffnen.
4. Das einzelne Plugin-ZIP auswählen, zum Beispiel `arbeitsrecht.zip` oder `vertragsrecht.zip`.
5. Nach erfolgreichem Upload eine neue Aufgabe oder Konversation öffnen.

**Schritt 4: Skill verwenden**

1. Eine neue Aufgabe oder Konversation starten.
2. `/` eingeben oder den `+`-Schalter wählen und den passenden Skill kontrolliert auswählen; bei eindeutigem Auftrag kann er auch automatisch vorgeschlagen werden.
3. Beispiel: "Erstelle mir einen Entwurf für eine ordentliche Kündigung nach Paragraf 622 BGB. Lies zuerst die beigefügten Unterlagen."

### Installation in Claude Code (für Entwickler / Terminal-Nutzer)

```bash
# Repository klonen
git clone https://github.com/Klotzkette/claude-fuer-deutsches-recht.git
cd claude-fuer-deutsches-recht

# Als Marketplace hinzufügen
claude plugin marketplace add .

# Skills installieren
claude plugin install arbeitsrecht@klotzkette-german-legal-skills
claude plugin install vertragsrecht@klotzkette-german-legal-skills
claude plugin install prozessrecht@klotzkette-german-legal-skills
```

## FAQ für Einsteiger

**F: Muss ich programmieren können?**
A: Nein. Für Claude Desktop reicht es, Dateien hochzuladen. Nur für Claude Code sind Terminal-Grundkenntnisse hilfreich.

**F: Kostet die Plugin-Nutzung Geld?**
A: Plugins stehen nach aktuellem Produktstand in kostenpflichtigen Plänen zur Verfügung. Die Markdown-Schnellstarts und Werkstätten können unabhängig davon als normale Arbeitsdateien genutzt werden. Aktuelle Planangaben stehen unter https://claude.ai/pricing.

**F: Wo funktionieren installierte Plugins?**
A: Plugins lassen sich im Web-Chat, im Chat-Bereich von Claude Desktop und in Cowork nutzen. Die enthaltenen Skills funktionieren in allen drei Bereichen; Hooks und Sub-Agenten laufen nur in Cowork. Eine direkte Integration in Kanzleisoftware erfordert einen gesonderten, dokumentierten Anschlussweg.

**F: Sind die Skills datenschutzkonform?**
A: Das lässt sich nicht pauschal beantworten. Anbieter, Plan, Vertrag, Datenfluss, Auftragsverarbeitung, Unterauftragnehmer, Speicherfristen und das konkrete Material müssen vor produktiver Nutzung eigenständig geprüft werden; dieses Repository erteilt keine Freigabe.

**F: Kann ich die Skills anpassen?**
A: Ja. Alle Skills sind Open Source (Apache-2.0 OR MIT, nach Wahl des Nutzers). Sie können sie nach Belieben anpassen – siehe [Beitragsleitfaden](./CONTRIBUTING.md).

**F: Was mache ich, wenn ein Skill nicht funktioniert?**
A: Öffnen Sie einen Issue auf GitHub oder schauen Sie in die Skill-Datei – oft sind Abhängigkeiten oder Formate dokumentiert.

**F: Wie zuverlässig sind die Rechtszitate?**
A: **Nicht sehr**. LLMs erfinden oft Zitate. Rechtsprechung darf nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei/amtlich oder per lizenziertem Live-Zugriff verifizierter Quelle ausgegeben werden. Kommentar-, Aufsatz- und BeckRS-Blindzitate sind gesperrt.

## Hinweise zur Nutzung

⚠️ **Bitte beachten Sie:**

1. **Übersetzungsarbeit**: Diese Skills sind eine **KI-gestützte Übersetzung und Anpassung** der englischsprachigen "claude-for-legal"-Skills von Anthropic. Sie wurden für das deutsche Rechtssystem adaptiert, aber **nicht von Juristen final geprüft**.
2. **Alle Angaben ohne Gewähr**: Die Skills können Fehler, Ungenauigkeiten oder veraltete Rechtsinformationen enthalten. Eine **eigenständige Prüfung** aller Ausgaben ist zwingend erforderlich.
3. **Kein Ersatz für anwaltliche Beratung**: Diese Werkzeuge liefern Vorlagen und Strukturierungshilfen für Juristen – sie ersetzen **keine** fundierte anwaltliche Beratung oder Recherche.
4. **Mandantengeheimnis**: Skills greifen ausschließlich auf den Datenraum des jeweiligen Mandats zu. Die Wahrung des Mandantengeheimnisses (§ 43a Abs. 2 BRAO, § 203 StGB) liegt in Ihrer Verantwortung.
5. **Halluzinationsrisiko**: LLMs können plausibel klingende, aber **erfundene** Urteile, Aktenzeichen, Fundstellen und Kommentarstellen generieren. **Jede Quelle muss verifiziert werden** – insbesondere bei Rechtsprechung.
6. **Fristen**: Skills können Fristberechnungen durchführen (z. B. für Mahnbescheid, einstweilige Verfügung, Kündigungsschutzklage), aber die **anwaltliche Kontrolle** und Verantwortung bleibt bei Ihnen.
7. **Experimentieren erwünscht**: Probieren Sie die Skills aus, testen Sie verschiedene Prompts, passen Sie die Vorlagen an Ihre Kanzlei an – aber immer mit der gebotenen **Sorgfalt und Skepsis**.

**Viel Erfolg beim Ausprobieren – auf eigene Verantwortung.**

## Hinweise für Mitwirkende: Cross-Plugin-Bezüge und doppelte Referenzen

Einige Plugins verweisen in ihren Skills auf Skills oder Pläne **anderer** Plugins. Wer ein **Einzelplugin** als ZIP zieht, hat diese Begleitplugins nicht automatisch dabei. Das neue `grosskanzlei-corporate-ma` ist hiervon ausdrücklich ausgenommen: Aktenanlage, Tabellenreview, Liquiditätsvorschau, Insolvenzreifecheck, CP-Kalender und Billing/E-Rechnung sind darin freistehend enthalten.

Zwei zentrale Methodik- und Zitierreferenzen liegen **doppelt** im Repo:

- `references/methodik-buergerliches-recht.md` und `methodenlehre-buergerliches-recht/references/methodik-buergerliches-recht.md`
- `references/zitierweise.md` und `zitierweise-deutsches-recht/references/zitierweise.md`

Das ist gewollt: Die Querschnittsplugins `methodenlehre-buergerliches-recht` und `zitierweise-deutsches-recht` werden auch einzeln als ZIP ausgeliefert und müssen autark sein. Wer die Repo-Root-Datei ändert, muss den Spiegel im Plugin-Ordner mitziehen, sonst driften die Plugins gegen die anderen Skills, die per relativem Pfad auf die Root-Referenz zeigen. Dafür gibt es ein Hilfsskript:

```bash
python3 scripts/sync-references.py
```

Das Skript kopiert die Root-Referenzen ggf. in die Plugin-Spiegel und meldet, was synchronisiert wurde. Vor jedem Commit, der die beiden Root-Dateien anfasst, einmal aufrufen.

## Lizenz

Doppellizenziert unter **Apache License, Version 2.0** ODER **MIT License**, nach Wahl des Nutzers (`SPDX-License-Identifier: Apache-2.0 OR MIT`) – siehe [Lizenzhinweis](./LICENSE), [Apache-2.0-Lizenz](./LICENSE-APACHE), [MIT-Lizenz](./LICENSE-MIT) und [Notice](./NOTICE).

Die ursprüngliche Vorlage `claude-for-legal` von Anthropic steht unter der MIT-Lizenz; diese Adaption erweitert, ersetzt und ergänzt die ursprünglichen Inhalte und wird unter dem oben genannten Doppellizenz-Modell veröffentlicht.

## Mitwirken

Beiträge willkommen – siehe [Beitragsleitfaden](./CONTRIBUTING.md).

## English Quick Guide

This repository provides a large German-law plugin and skill collection for practical legal workflows. It supports document review, structured legal analysis, drafting, deadline work, evidence mapping and source-controlled research across civil, labour, corporate, insolvency, family, inheritance, social, public, criminal and specialist business law.

### What is what?

| Component | Meaning | Best use | Location |
| --- | --- | --- | --- |
| **Plugin ZIP** | The installable package for one legal field, including skills, references and supporting files. | Use it when the legal field should be available as an installed plugin. | At the top of each plugin README and in the [asset index](./ASSET_INDEX.md). |
| **Skill** | A focused workflow for one task inside a plugin. | Use it for a specific review, drafting step or specialist task. | In the [complete skill index](./SKILLS.md), the [per-plugin index](./skills-index/) and each plugin README. |
| **Workshop prompt** | A detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | Use it when one file should provide the deepest standalone workflow without installation. | In the [workshop index](./docs/werkstatt-und-schnellstart-coverage.md#werkstatt-prompts) and each plugin README. |
| **Quick-start or mini prompt** | A compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | Use it when the matter should start quickly and the full workshop is not yet needed. | In the [quick-start index](./docs/werkstatt-und-schnellstart-coverage.md#schnellstart-prompts) and each plugin README. |
| **Practice file** | A separate document bundle for trying a workflow without client material. It is not installed with a plugin. | Use it to test file handling and legal workflows. | In the [practice-file index](./testakten/README.md). |

**Click behaviour:** README, index and overview links remain normal GitHub navigation pages. Links labelled **Download MD** save the unchanged Markdown work file instead of opening a source preview. Individual skills receive a unique plugin-and-skill filename so that multiple downloads do not overwrite one another.

All five complete indexes are alphabetically sorted and provide a short description for every plugin, skill, workshop prompt, quick-start prompt or practice file. Start with the [five A-to-Z indexes](#alle-vollständigen-listen-von-a-bis-z), the [plugin catalogue](#was-ist-drin), the [complete skill index](./SKILLS.md), the [workshop and quick-start index](./docs/werkstatt-und-schnellstart-coverage.md), the [practice-file index](./testakten/README.md), or the [latest release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest).

The material is experimental and does not replace legal advice. Every output must be checked by a qualified human against current statutes, official materials and independently verifiable court decisions. Do not upload confidential client data unless the technical setup, professional duties and data-protection framework permit it.
