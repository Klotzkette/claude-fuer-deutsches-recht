# Claude – Deutsche rechtliche Fähigkeiten / German Legal Skills

> **Experimentelles Skill-Set** für die anwaltliche Praxis im deutschen Recht – Skills, Sub-Agenten, Workflows etc. als Anregung für Kanzlei-Arbeitsabläufe. Orientiert sich an der **deutschen Rechtspraxis**, an Gesetzestexten, amtlichen Materialien und frei überprüfbarer Rechtsprechung. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr – jede Nutzerin und jeder Nutzer kalibriert die Skills selbst für die eigene Praxis.

## Über dieses Repository

Dieses Repository ist eine **experimentelle Plugin- und Skill-Sammlung für deutsches Recht** auf Basis der offenen "claude-for-legal"-Skills von Anthropic, vollständig ins Deutsche übertragen und an typische Arbeitsabläufe in Kanzleien, Rechtsabteilungen und bei Beratern angepasst. Die Struktur, Beispiele und Workflows sind inzwischen **für die deutsche Rechtspraxis überarbeitet und im Alltagseinsatz erprobt**, sie bleiben aber bewusst als Experiment gekennzeichnet: Es handelt sich **nicht** um ein geprüftes Produkt, sondern um eine technische Spielwiese zum Ausprobieren, Anpassen und Weiterentwickeln.

Ziel ist es, zu zeigen, wie sich Plugins und Skills für Arbeitsrecht, Gesellschaftsrecht, Insolvenzrecht (inklusive Liquiditätsplanung und Fortbestehensprognose), Datenschutzrecht, Prozessrecht, gewerblichen Rechtsschutz, Produkt-, Robotik- und Regulierungsrecht u. a. so strukturieren lassen, dass sie sich an der in Deutschland üblichen Methodik (Anspruchsgrundlagen, Prüfungsaufbau, Gesetzesauslegung, Rechtsprechungszitate mit Datum und Aktenzeichen) orientieren. Die Inhalte dienen ausschließlich als **Anregung für eigene Kanzlei- oder Inhouse-Plugins und -Skills**: Sie sollen zeigen, welche Prompts, Rollenbeschreibungen und Workflows in der Praxis hilfreich sein können – jede Nutzerin und jeder Nutzer passt sie an die eigenen Mandate, Branchen, Tools und Compliance-Vorgaben an.

### Bitte mit-testen und Feedback geben

Die Skills sind inzwischen deutlich verbessert und in verschiedenen Konstellationen getestet worden, können aber weiterhin Fehler, Lücken oder veraltete Rechtsstände enthalten. Deshalb:

- Nutzt die Skills aktiv im **Testbetrieb** (ohne echte Mandatsgeheimnisse) und schaut, wie gut sie zu euren Fällen, Quellenzugängen und Kanzleiprozessen passen.
- Gebt **Rückmeldungen**, eröffnet **Issues**, formuliert Verbesserungsvorschläge und schickt gerne **Pull Requests** mit eigenen Anpassungen, zusätzlichen Rechtsgebieten oder Praxis-Workflows.
- Passt die Beispiele an eure eigene **Zitierweise**, eure verifizierbaren Quellenzugänge und eure internen Vorgaben zu Berufsrecht, Datenschutz, KI-Governance und Mandatsgeheimnis an.

### Haftung, Berufsrecht, Datenschutz & KI-Recht

Dieses Repository trifft **keine Aussage** zur Zulässigkeit eines Einsatzes im konkreten Mandat oder Unternehmen – insbesondere nicht zu §§ 203, 204 StGB, § 43e BRAO, § 2 BORA, § 53, § 97, § 160a StPO, DSGVO / BDSG (inkl. Drittlandtransfer), US-Cloud-Act / FISA, der KI-VO (VO (EU) 2024/1689) oder sonstigen berufsrechtlichen, datenschutzrechtlichen und regulatorischen Vorgaben. Ob und wie ihr diese Beispiele produktiv nutzen dürft, müsst ihr **eigenverantwortlich** prüfen und in eure bestehende Governance (Mandatsgeheimnis, AVV, TOMs, KI-Richtlinien, Betriebsvereinbarungen etc.) integrieren.

> 🧪 **Übrigens — es gibt auch sehr schöne Testakten.** Im Verzeichnis [`testakten/`](./testakten) liegen mehrere umfangreiche, anonymisierte Arbeitsakten mit echten PDFs, Excel-Tabellen, Word-Entwürfen und handschriftlichen Notizen — bewusst unstrukturiert benannt wie ein realer Datenraum, damit sich die Plugins an echten Mandaten ausprobieren lassen. Details und Direkt-Downloads im [Testakten-README](./testakten/README.md).

### Klotzkettes Juristische Promptliste

Viele Skills in diesem Repo sind im Kern strukturierte **Mega-Prompts** — also nicht primär Eingangs- oder Kaltstart-Skills einer größeren agentischen Tätigkeit, sondern eigenständig nutzbare, hochstrukturierte Prompt-Bausteine. Solche Skills funktionieren auch **außerhalb von Claude Code, Codex oder Perplexity Computer**: einfach die `SKILL.md` als Markdown herunterladen, in ChatGPT, Claude, Gemini, Perplexity, Mistral, Le Chat oder ein anderes Tool kopieren und nach Bedarf anpassen.

Für diesen Anwendungsfall gibt es eine kuratierte, nach Fachanwaltschaften sortierte Liste: **[Klotzkettes Juristische Promptliste](./PROMPTLISTE.md)** — alle Angaben ohne Gewähr, mit großem Disclaimer auf der Seite. Workflow-Eingangs-Skills, generische Router und ausgesprochen historisch-exotische Inhalte (Preußisches Landrecht, Römisches Recht, Kanonisches Recht, Weltraumrecht) bleiben dort bewusst ausgespart.

## Überblick

| Kennzahl | Wert |
|---|---|
| **Plugins** | 213 |
| **Skills (SKILL.md)** | 25639 — [Gesamtübersicht](./SKILLS.md) |
| **Testakten** | 206 |
| **Fachanwalts-/-anwältinnen-Profile** | 24 |
| **Plugin-Version / Arbeitsstand** | `v327.0.0` — [latest Release auf GitHub](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) |
| **Marketplace-Definition** | [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) |

### Sammel-Downloads

| Paket | Download | Inhalt |
| --- | --- | --- |
| **Alle Plugins als MegaZIP** | [alle-plugins-megazip.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) | Alle installierbaren Plugin-ZIPs plus `marketplace.json` in einem Archiv. |
| **Alle Testakten als ZIP** | [alle-testakten.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) | Alle Testaktenordner in Originalstruktur mit PDF, DOCX, XLSX, JPEG, EML, Markdown und jeweiligem Gesamt-PDF. |
| **Alles komplett als ZIP** | [alles-komplettpaket.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alles-komplettpaket.zip) | Alle Plugin-ZIPs, alle Testakten-ZIPs, Marketplace-Manifest und Übersichtsdateien in einem Archiv. |
| **SHA-256-Prüfsummen** | [checksums-sha256.txt](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/checksums-sha256.txt) | Maschinenlesbare Prüfsummen für Release-Assets; die Release-Pipeline gleicht Größen und Hashes nach dem Upload gegen GitHub ab. |
| **Klotzkettes Juristische Promptliste** | [PROMPTLISTE.md](./PROMPTLISTE.md) | Kuratierte Übersichtsseite aller praxistauglichen Skills als Mega-Prompts — sortiert nach Fachanwaltschaften, zum Kopieren in ChatGPT, Claude, Gemini, Perplexity oder beliebige andere Tools. Mit großem Disclaimer. |
| **Alphabetischer Mega-Prompt-Index** | [testakten/megaprompts/README.md](./testakten/megaprompts/README.md) | Alle 213 Mega-Prompt-Markdowns alphabetisch nach Plugin-Slug, direkt anklickbar und separat im Release-ZIP `testakte-megaprompts.zip` enthalten. |

### Inhaltliche Cluster

- **Rechtsgebiete (materiell):** BGB Allgemeiner Teil, Arbeitsrecht, Mietrecht (Wohn-/Gewerbe), Nachbarrecht/Nachbarschaftsstreit, Erbrecht, Familienrecht, Sozialrecht, Sozialversicherungsstatus/DRV-Statusfeststellung, Strafrecht, Äußerungsrecht/Meinungsfreiheit, Verwaltungsrecht (inkl. Energieanlagen-BImSchG-Verfahren und Energietrassen-Planfeststellung), Steuerrecht, Insolvenzrecht inkl. StaRUG, Gesellschaftsrecht, Handelsregisterpraxis, Grundbuchamtspraxis, Erbbaurecht, Vertragsrecht, AGB-Recht, Markenrecht (inkl. Luxus-Fashion + USPTO/Lanham Act), Urheberrecht, Softwarerecht DE/EU/US, Wettbewerbsrecht, Kartellrecht, Datenschutzrecht, IT-Recht, digitale Barrierefreiheit, Robotikrecht, Bank- und Kapitalmarktrecht, Factoring, Bau- und Architektenrecht, Verkehrsrecht, Medizinrecht, Krankenhausrecht, GOÄ/Arzthonorar, Apothekenrecht, Migrationsrecht, Internationales Recht, Europarecht, Energierecht, Bundesnetzagentur-Verfahren, E-Commerce, Bürokratieverstehen, Vereinsrecht, Parteienrecht, Wahlkampfrecht, Bundeswehr-/Wehrrecht, Solo-Selbstständige, HOAI-Leistungsphasen, Commercial Courts/englischsprachige Wirtschaftsverfahren, Robotikrecht, Zwangsvollstreckung, Beamtenrecht/Richterrecht, US-Copyright Act und US Bankruptcy Code, NIS-2/Cybersecurity-Compliance, Hinweisgeberschutz, Handelsvertreterrecht, Schulrecht, Hochschulrecht und Hochschulprüfungsrecht.
- **Mechanik-Prüfer:** `bgb-at-pruefer` (BGB AT: Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, Anfechtung, Stellvertretung, Verjährung, qES/beA/Formfiktion), `bgb-bt-pruefer` (BGB BT: Kauf, Dienst, Werk, Geschäftsbesorgung, Auftrag, Leasing-Schnittstelle, Mischverträge, Bürgschaft, GoA, Bereicherung, Delikt, digitale Elemente und Right to Repair), `subsumtions-pruefer` (generischer Subsumtions-Workflow DE + EU), `bereicherungs-und-anfechtungsrecht-pruefer` (§§ 812 ff. BGB + AnfG + InsO-Anfechtung einschließlich KI-Schuldnerakten-Screening, § 135 InsO und Verteidigung), `ki-vo-ai-act-pruefer` (Verordnung (EU) 2024/1689 mit Anbieter/Betreiber-Entscheidungsbaum, Art. 5/6/25/51 ff.).
- **Werkstatt- und Werkstatt-Plugins:**
  - `legistik-werkstatt` — komplette Gesetzgebungs-Werkstatt für Bundesministerien, Bundestag, Fraktionen/Opposition, Landesministerien, Landtage und sonstige Normgeber (Referentenentwurf Arial-Hausstil, BT-/Landtagsdrucksache, Vorblatt A–F, Synopse, Lesefassung, Kabinettsmappe, Formulierungshilfe, Änderungsantrag, Antrag, Entschließungsantrag). DOCX/PDF im passenden offiziellen Layout.
  - `urteilsbauer-relationsmacher` — Urteils- und Beschluss-Werkstatt für Amts-, Land- und Familienrichter plus Rechtspfleger. Vollrelation (Sachbericht/Zulässigkeit/Schlüssigkeit/Erheblichkeit/Replik/Beweis/Tenorierung/Nebenentscheidungen/Selbstkontrolle) **und** Kurzrelation Praxisstandard mit Wahlfrage am Anfang. Rendert Urteile, Versäumnisurteile und Beschlüsse als DOCX im offiziellen Gerichtslayout nach § 313 ZPO. Inkl. Arbeitsakte "Solis Vision X Smartglasses" (CISG, kollidierende AGB CH/EU, Incoterm FOB Galway, DSGVO als Eingriffsnorm, Testkauf 1577 EUR).
  - `hausarbeitenmacher` — didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten im Jurastudium. Führt sokratisch durch Zivilrecht, Öffentliches Recht und Strafrecht mit Ausflügen in Europarecht und Rechtstheorie. Fragt zu Beginn nach der Lehrkraft und entwickelt eine Adressaten-Strategie **ohne Schleimerei**. Strikt lernfördernd: kein Copy-Paste-Output, sondern Fragen, Strukturen, Methodenhinweise, Zitierweise. 23 Skills von Aufgabenstellung-Erfassen über Gutachtenstil und Methodenlehre bis Selbstkontrolle vor Abgabe.
- **Workflow-Pakete:** Wandeldarlehen-Lebenszyklus (Erstellung, Beurkundung, Wandlung, Cap-Table, Notar), Kündigungsschutzklage Selbsthilfe (Laie/Anwalt, Schriftsätze, Sprechzettel, Vergleich), Entfristungsklage TzBfG (Schriftform, elektronische Signatur), KI-Richtlinie für Kanzleien, Schriftform-/Textform-Organisator, Krisenfrüherkennung StaRUG, Liquiditätsplanung, Fortbestehensprognose.
- **Querschnitt:** Aktenauszug Gerichtsverfahren, Mandantenanfragen-Assistent, Arbeitszeugnis-Analyse (Ampelsystem), Email-Umformulierer berufsrechtskonform, verifizierbare deutsche Zitierweise, Fachanwaltschafts-Übersicht.

> ⚠️ **Vorsicht: hiermit bitte nicht mogeln im Studium.**
> Die Vollrelation, der Urteilsentwurf, der Hausarbeits- und Seminararbeits-Output sowie alle Arbeitsakten sind **Trainings-, Praxis- und Lernwerkzeuge** für Studierende, Referendare/-innen, Assessoren/-innen, Berufsrichter/-innen, Tutor/-innen und Lehrkräfte. Sie sind ausdrücklich **nicht** dafür gedacht, in Hausarbeiten, Seminararbeiten, Klausuren, Aktenvorträgen oder im juristischen Vorbereitungsdienst (Z-, S-, V-, A-Klausur, mündliche Prüfung) als eigene Leistung ausgegeben zu werden. Das wäre ein Täuschungsversuch im Sinne der jeweiligen universitären Prüfungsordnung bzw. § 14 JAG NRW / § 12 JAPO Bayern / vergleichbarer Vorschriften der anderen Länder und kann zum Nichtbestehen, zur Aberkennung der Prüfung oder zu disziplinarrechtlichen Konsequenzen führen. Wer eine Relation, eine Hausarbeit oder ein Urteil üben will: zuerst selbst schreiben, danach mit dem Plugin abgleichen.

Die vollständige Plugin-Liste findest du in [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) und im Abschnitt [Was ist drin?](#was-ist-drin).

## Quickstart

```text
# Marketplace im Claude-Code-Prompt hinzufügen
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install <plugin-name>@klotzkette-german-legal-skills
```

> ⏱️ **Geduld beim ersten `marketplace add`.** Claude Code klont beim Hinzufügen das **komplette Repository** in den lokalen Plugin-Cache — inklusive der 204 Testakten mit über 600 PDFs (rund 150 MB) und der Git-History. Das sind insgesamt etwa **600 MB**, die einmalig über die GitHub-Leitung gezogen werden. Auf normaler DSL dauert das nach unserer Einschätzung **circa 2 bis 3 Minuten**, je nach Verbindung und GitHub-Edge auch mal etwas länger. Das ist kein Fehler — bitte einfach durchlaufen lassen, bis Claude die Marketplace-Übersicht öffnet. Folge-Updates (`/plugin marketplace update`) sind danach deutlich schneller, weil nur noch der Delta-Pull über die Leitung geht. Wer nur einzelne Plugins ohne Testakten will, kann alternativ einzelne Plugin-ZIPs aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) laden — siehe nächster Absatz.

Alternativ: über die Claude-Desktop-/Cowork-GUI unter **Customize → Skills / Plugins** → ZIP aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) hochladen. Schritt-für-Schritt unter [Schnellstart](#schnellstart), [Für Einsteiger](#für-einsteiger-schritt-für-schritt-anleitung) und besonders für Mac-Probleme in [INSTALLATION_EINFACH.md](./INSTALLATION_EINFACH.md).

## 🚨 KEINE Aussage über Berufsrecht, Datenschutz, KI-VO oder Beschlagnahmeverbote

**Lesen, bevor irgendetwas davon eingesetzt wird.** Dieses Repository ist ausschließlich ein technisches Experiment. Es trifft **keinerlei Aussage** darüber, ob der Einsatz dieser Skills in einer konkreten Praxisumgebung berufs-, datenschutz- oder KI-rechtlich zulässig ist. Alle nachstehenden Fragen muss **jede Nutzerin und jeder Nutzer in eigener Verantwortung** vor der ersten Nutzung prüfen – das Repository, seine Autorin / sein Autor und alle Mitwirkenden übernehmen dafür keinerlei Verantwortung oder Haftung:

- **Strafrechtliches Mandatsgeheimnis – §§ 203, 204 StGB.** Die Skills sagen nichts darüber aus, ob ein konkreter Einsatz mit dem strafbewehrten Geheimnisschutz des § 203 StGB (Verletzung von Privatgeheimnissen) und § 204 StGB (Verwertung fremder Geheimnisse) vereinbar ist – auch nicht in der Variante § 203 Abs. 3, 4 StGB (mitwirkende Personen, sonstige Stellen).
- **Berufsrecht – § 43e BRAO, § 2 BORA, § 53 StPO.** Es wird **nicht** geprüft, ob der Einsatz mit § 43e BRAO (Inanspruchnahme von Dienstleistern, insbesondere Cloud/KI), § 2 BORA (Verschwiegenheit), den Zeugnisverweigerungsrechten nach § 53 StPO und den Beschlagnahmeverboten nach § 97 StPO vereinbar ist. Gleiches gilt sinngemäß für andere **freie Berufe** mit eigenem Berufsrecht (StBerG für Steuerberater:innen, WPO für Wirtschaftsprüfer:innen, ÄrztInnen, Notar:innen, Patentanwält:innen u. a.).
- **Datenschutz – DSGVO, BDSG.** Es wird **nicht** beurteilt, ob die Verarbeitung personenbezogener Daten DSGVO-konform ist, ob eine ausreichende **Rechtsgrundlage** (Art. 6, 9 DSGVO) vorliegt, ob ein **Auftragsverarbeitungsvertrag** nach Art. 28 DSGVO geschlossen werden muss, ob eine **Datenschutz-Folgenabschätzung** (Art. 35 DSGVO) erforderlich ist oder ob die **Informationspflichten** nach Art. 13, 14 DSGVO erfüllt sind.
- **KI-Verordnung (KI-VO / EU AI Act, VO (EU) 2024/1689).** Es wird **nicht** entschieden, ob der Einsatz unter eine der Hochrisiko-Kategorien nach **Art. 6 KI-VO** in Verbindung mit **Anhang III KI-VO** fällt (insbesondere Zugang zur Justiz, Strafverfolgung, demokratische Prozesse), ob **Transparenzpflichten** nach Art. 50 KI-VO greifen, ob es sich um ein **General-Purpose-AI-Modell** nach Art. 51 ff. KI-VO handelt und welche **Pflichten als Betreiber** (Art. 26 KI-VO) zu erfüllen sind.
- **Beschlagnahmeverbote und auslandsrechtliche Zugriffe.** Es wird nicht geprüft, ob Eingabedaten und Modellantworten gegen Beschlagnahme nach **§§ 97, 160a StPO**, gegen **US Cloud Act**, **FISA § 702**, **CLOUD Act warrants**, **PATRIOT Act § 215** oder sonstige extraterritoriale Zugriffsbefugnisse hinreichend geschützt sind. Dafür ist die jeweilige Nutzerin / der jeweilige Nutzer allein verantwortlich.
- **Zugang, Auftragsverarbeitung, Hosting.** Wie der API-Zugang zum Modell beschafft wird (Anthropic direkt, AWS Bedrock, Google Vertex, eigenes Hosting), ob mit dem Anbieter ein **Auftragsverarbeitungsvertrag** geschlossen wird, ob ein **berufsrechtskonformer Cloud-Vertrag** vorliegt und ob die Anforderungen an die Verschwiegenheit / Mandatsgeheimnis-Header und Datenflusskontrolle in der konkreten Deployment-Konstellation eingehalten sind, bleibt vollständig in der **Eigenverantwortung der Nutzerin / des Nutzers**.

## Eigene API oder einen Zwischenanbieter anbinden (Stand Juni 2026)

Anwältinnen, Anwälte und andere Berufsgeheimnisträgerinnen/-träger müssen vor jeder produktiven Nutzung selbst prüfen, ob die konkrete Anbieter-, Hosting- und Datenflusskonstellation mit Mandatsgeheimnis, Berufsrecht und Datenschutz vereinbar ist. Dieses Repository bestätigt keinen Anbieter und ersetzt keine Prüfung von § 203 StGB, § 43e BRAO, Art. 28 DSGVO, Kapitel V DSGVO, TOMs, Löschkonzept, Audit-Rechten, Subunternehmern, Datenresidenz und vertraglicher Verschwiegenheit.

Technisch gibt es zwei saubere Wege. Welche davon in deiner installierten Oberfläche verfügbar ist, hängt von der jeweiligen Claude-/Cowork-Version und vom Anbieter ab.

### Weg A — Claude Code im Terminal

Für Claude Code ist die robuste Variante die Konfiguration über Umgebungsvariablen. Der Anbieter muss dafür eine Claude-/Anthropic-kompatible API bereitstellen und dokumentieren, welche Authentifizierung verwendet wird.

1. Beim Anbieter Vertrag, AVV/TOMs, Verschwiegenheitszusagen und Subunternehmerliste prüfen und dokumentieren.
2. API-Schlüssel erzeugen und nur im Passwort-Manager bzw. in der lokalen Shell-Konfiguration speichern. Keine Schlüssel ins Repo, in Testakten oder in Screenshots schreiben.
3. Base URL, Auth-Schema und Modellnamen exakt aus der Anbieterdokumentation übernehmen.
4. Auf dem Mac für die aktuelle grafische Sitzung setzen:

```
launchctl setenv ANTHROPIC_BASE_URL https://api.<anbieter>.de/anthropic
launchctl setenv ANTHROPIC_AUTH_TOKEN <Ihr-Schluessel>
launchctl unsetenv ANTHROPIC_API_KEY
```

5. Terminal neu öffnen und mit einem harmlosen Testsatz prüfen. Im Anbieter-Dashboard muss der Aufruf erscheinen; im falschen Anbieter-/Anthropic-Konto darf er nicht auftauchen.

Für reine Terminal-Nutzung reicht alternativ eine Shell-Datei außerhalb des Repos, z. B. `~/.zshrc.local` oder `direnv`, wenn eure IT das freigibt:

```
export ANTHROPIC_BASE_URL="https://api.<anbieter>.de/anthropic"
export ANTHROPIC_AUTH_TOKEN="<Ihr-Schluessel>"
unset ANTHROPIC_API_KEY
```

### Weg B — Claude Desktop / Cowork-Oberfläche

Falls deine Cowork- oder Claude-Desktop-Version einen eigenen Gateway-/Third-Party-Inference-Dialog anbietet, gilt derselbe Prüfpfad:

1. Anbieterunterlagen rechtlich und technisch prüfen.
2. Base URL und API-Schlüssel aus dem Anbieter-Dashboard übernehmen.
3. Auth-Schema nur so einstellen, wie der Anbieter es dokumentiert, typischerweise `x-api-key` oder `Authorization: Bearer`.
4. Erlaubte ausgehende Hosts auf die Anbieter-Domain beschränken, wenn die Oberfläche ein solches Feld anbietet.
5. Mit Dummy-Daten testen und die Provider-Logs kontrollieren.

Wenn der Dialog in deiner Oberfläche nicht vorhanden ist oder anders heißt, nicht raten: dann Weg A nutzen oder die aktuelle Dokumentation der App/des Anbieters prüfen. Menübezeichnungen ändern sich schneller als dieses README.

### Kontrollliste vor echtem Mandatsmaterial

- Vertragliche Grundlage: AVV, TOMs, Verschwiegenheit, Unterauftragsverarbeiter, Audit-/Löschrechte.
- Datenfluss: Region, Protokollierung, Trainings-/Retention-Regeln, Support-Zugriffe.
- Technik: Base URL, Auth-Schema, Modellname, erlaubte Hosts, Provider-Logs.
- Kanzlei-Governance: KI-Richtlinie, Mandatsfreigabe, Betriebsvereinbarung, Dokumentation in der Akte.
- Test: nur Dummy-Daten, Provider-Logs geprüft, keine Schlüssel im Repo.

Die Anleitung ist bewusst anbieterneutral. Sie beschreibt nur den technischen Anschlussweg und die zu dokumentierenden Prüfpunkte, nicht die rechtliche Zulässigkeit eines bestimmten Setups.

### Professioneller Betrieb über Gateway, Enterprise-Proxy oder andere KI-Umgebungen

Die Skills in diesem Repository sind im Kern große, strukturierte Markdown-Workflows. Sie sind nicht magisch an eine einzige Oberfläche gebunden: Wer ein berufsrechts-, datenschutz- und organisationskonformes Setup hat, kann sie auch in anderen KI-Systemen, in internen Gateways, in Codex-/ChatGPT-Workspaces oder in eigenen RAG-/Agentenoberflächen ausprobieren. Entscheidend ist nicht der Dateiname, sondern ob die Umgebung Mandatsgeheimnis, Zugriffsrechte, Logging, Retention, Modelltraining, Subunternehmer, Datenresidenz und Export-/Auditpfade sauber beherrscht.

Für Claude Code beschreibt Anthropic offiziell Enterprise-Proxy, eigene Zertifikate, mTLS und Allowlisting sowie LLM-Gateway-Varianten mit `ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL` oder vergleichbaren Provider-Konfigurationen. Für kommerzielle Claude-for-Work/API-Nutzung beschreibt Anthropic außerdem, dass Organisationen unter den kommerziellen Bedingungen die Kontrolle über Nutzer- und Organisationsdaten behalten und Anthropic nicht ohne Opt-in mit diesen Daten trainiert. Diese Aussagen ersetzen keine berufsrechtliche Prüfung, sind aber wichtige Prüfpunkte für die IT-/Compliance-Akte.

Für Codex gilt entsprechend: OpenAI beschreibt Codex als ChatGPT-/Workspace-gebundene Agentenoberfläche mit Workspace-App-Kontrollen, RBAC/Permissions und Datenkontrollen. Wer diese Skills in Codex oder ChatGPT nutzt, muss insbesondere prüfen, welcher Plan, welche Workspace-Regeln, welche Trainingsdatenkontrollen und welche verbundenen Apps aktiv sind. Berufsrechtlich gilt weiter: erst Dummy-Daten, dann Freigabe durch Kanzlei-/Unternehmens-IT und Datenschutz, und erst danach überhaupt echte Fälle.

Egal welches System verwendet wird: Der Mensch macht weiter Jura. Die Skills können strukturieren, nachfragen, routen, Textentwürfe bauen und Kontrolllisten führen; die rechtliche Verantwortung, Quellenprüfung, Einordnung von Rechtsprechung, Literatur, Normstand und Tatsachen bleibt bei der Nutzerin oder dem Nutzer.

**Worum es hier geht.** Dieses Repository ist eine **technische Spielwiese**, die zeigt, was mit Claude Code und Plugin-Skills im Kontext deutschen Rechts überhaupt **technisch machbar** ist. Es geht **nicht** darum, eine produktiv einsetzbare, rechtskonforme Lösung anzubieten. Jede einzelne Nutzerin und jeder einzelne Nutzer prüft selbst und in eigener Verantwortung, ob, wie und unter welchen Schutzmaßnahmen ein Einsatz im konkreten Mandat oder Berufsumfeld zulässig ist – inklusive Mandatsgeheimnis, Datenschutz, Zeugnisverweigerungsrecht und Beschlagnahmeschutz, unabhängig von der einschlägigen Rechtsordnung.

> ⚠️ **WICHTIGER HINWEIS**
>
> Diese Skills sind eine **KI-gestützte Übersetzung und Adaption** der ursprünglichen "claude-for-legal"-Skills von Anthropic, angepasst an deutsches Recht.
>
> - ✅ **Ausprobieren ausdrücklich erwünscht** – aber auf eigene Verantwortung
> - ⚠️ **Alle Angaben ohne Gewähr** – keine Haftung für Vollständigkeit oder Richtigkeit
> - 🔍 **Quellen immer prüfen** – LLM-Ausgaben können halluzinieren, insbesondere bei Rechtsprechung
> - ⚖️ **Ersetzt keine anwaltliche Beratung** – nur Werkzeug für Jurist:innen
> - 🎓 **Lernkurve einplanen** – erste Schritte können holprig sein
>
> **Viel Spaß beim Experimentieren!**

> 💡 **Bitte beachten: Die Skills sind generalisierte Beispiele**
>
> Die Inhalte sind **bewusst generalisiert** und an das deutsche Recht angepasst, aber sie verstehen sich als **Beispiele und Startpunkte zum Ausprobieren** – nicht als Fachgutachten.
>
> Es kann gut sein, dass
>
> - eine Frist nicht (mehr) so stimmt, wie sie hier abgebildet ist,
> - eine zitierte Vorschrift in der Zwischenzeit geändert wurde,
> - eine Spezialistin oder ein Spezialist im jeweiligen Rechtsgebiet einzelne Punkte anders bewerten würde,
> - eine Randnummer, ein Aktenzeichen oder ein Quellenbeleg im Einzelfall unzutreffend ist,
> - eine Behandlung für eine bestimmte Konstellation zu generisch oder zu kanzleitypisch ist.
>
> **In diesem Fall bitte nicht auf die Autorin / den Autor "dreinschlagen".** Forken, anpassen, einen Pull Request einreichen oder einen Issue öffnen – das ist ausdrücklich gewollt. Das Repository soll genau so weiterentwickelt werden: durch die Praxis derjenigen, die damit arbeiten.

Diese Sammlung lässt sich u. a. in Claude Code, Claude Desktop und vergleichbaren Skill-fähigen KI-Umgebungen einsetzen. Inspiriert von und adaptiert nach Anthropics offenem Projekt `claude-for-legal`, vollständig auf das deutsche Recht und die Arbeitsweise deutscher Kanzleien zugeschnitten.

## Was ist drin?

> 🧭 **Querschnitts-Plugins zum Mitladen:** Drei Plugins liefern die methodische Grundlage, die in den anderen Plugins vorausgesetzt wird. Sie gehören in jede Konfiguration mit hinein, weil sie den deutschen Stil tragen:
>
> - [`methodenlehre-buergerliches-recht`](./methodenlehre-buergerliches-recht) — Methodenlehre und Falllösung im deutschen bürgerlichen Recht aus Anwaltsperspektive. Anspruchsaufbau, Auslegung, Abwägung, Präzedenzarbeit, Rechtsfortbildung, Methodenwahl, EU-Methodik und Begründungskontrolle.
> - [`rechtstheorie-rechtsphilosophie`](./rechtstheorie-rechtsphilosophie) — Rechtsbegriff, Kelsen-orientierte Normgeltung, Kompetenz- und Stufenbauprüfung, Demokratie, Besitzdogmatik, Law-and-Economics, Hayek-Wissensproblem, spontane Ordnung, Machtkritik und anti-dezisionistisches Red-Team gegen Ausnahme-, Souveränitäts- und Freund-Feind-Rhetorik.
> - [`zitierweise-deutsches-recht`](./zitierweise-deutsches-recht) — Hauszitierweise mit Datum, Aktenzeichen, frei prüfbarer Quelle, Pinpoint-Randnummer und Sperre gegen BeckRS-/Literatur-Blindzitate. Pflicht-Checkliste vor jeder Ausgabe.
>
> Diese Plugins sind in jedem Modus (Claude Code, Cowork, Desktop) einzeln zuschaltbar und greifen quer in alle Rechtsgebiets-Plugins ein. Wer mit dem Marketplace startet, sollte sie zuerst aktivieren — alle anderen Skills referenzieren ihre Regeln (siehe [`references/methodik-buergerliches-recht.md`](./references/methodik-buergerliches-recht.md) und [`references/zitierweise.md`](./references/zitierweise.md)).

> 🧪 **Testakten zum Ausprobieren:** Im Ordner [`testakten/`](./testakten) liegen mehrere umfangreiche, anonymisierte Arbeitsakten mit echten PDFs, Excel-Tabellen, Word-Entwürfen und Mandantennotizen — bewusst unstrukturiert benannt wie ein realer Datenraum. Eine Akte pro typischem Anwendungsfall: Fluggastrechte (Familie Bräutigam-Zaytuna), Betreuung (Frau Sauer, 87, Demenz; Schmalfeld, Kontodaten und verdächtige Verträge), Einfache/Leichte Sprache, Sozialrecht, Fortbestehensprognose, Grundsteuer-Bescheidkette, Grunderwerbsteuer-Share-Deal-Closing und Kanzlei-Lebenszyklus-Alltag. Jede Akte ist als eigenes ZIP am Release angehängt und wird **nicht** mit den Plugins ausgeliefert; zusätzlich gibt es [alle-testakten.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) als Sammelarchiv. Details und Direkt-Downloads im [Testakten-README](./testakten/README.md).

Plugins (in Claude-Code-Terminologie) für die wichtigsten Rechtsgebiete der deutschen Beratungspraxis, alphabetisch sortiert:

| Plugin | Beschreibung |
| --- | --- |
| [`agb-recht-pruefer`](./agb-recht-pruefer) | Gigantischer AGB-Rechtsprüfer und Klausel-Entwerfer für deutsches Recht: §§ 305 bis 310 BGB, UKlaG, B2C/B2B, Branchen-AGB, Redlining, Klauselrisiko und rechtssichere Entwurfsworkflows. |
| [`aktenaufbereiter-strafrecht`](./aktenaufbereiter-strafrecht) | Aktenaufbereiter für die Strafverteidigung. Sechs Excel-fähige Übersichten — Aktenvorblatt; Personenverzeichnis; Tatkomplexe; Beziehungen; Chronologie; Fristen. Fortlaufend ergaenzbar. Erkennt Luecken und Widersprueche. Kein Ersatz für Aktenlektuere. |
| [`aktenauszug-gerichtsverfahren`](./aktenauszug-gerichtsverfahren) | Strukturierter Aktenauszug für deutsche Gerichtsverfahren: Verfahrensidentifikation Einleitungssatz Verfahrenszusammenfassung Sachverhaltschronologie Verfahrensgeschichte tabellarische Gegenüberstellung der Parteivortraege Beweismittel und Rechtsargumente für schnelle Einarbeitung in Akten. |
| [`aktienrecht-hauptversammlung-ag-se`](./aktienrecht-hauptversammlung-ag-se) | Hauptversammlungs-Vorbereiter, Leitfaden-Ersteller und Durchführungsplugin für kleine AG, normale AG, börsennotierte AG und SE: Einberufung, Tagesordnung, virtuelle HV, Q&A, Abstimmung, Niederschrift, Anfechtungsrisiko und Post-HV. |
| [`anlagen-zu-schriftsaetzen`](./anlagen-zu-schriftsaetzen) | Anlagenmanagement fuer gerichtliche Schriftsaetze: sortiert chaotische Mandantenordner, E-Mails, Scans, Tabellen und Vorversionen zu beA-tauglichen K/B/AST/AG-Anlagen mit Verzeichnis, Konvolutdeckblaettern, Stempel-/Dateinamenregeln, Hashlog, Lueckenliste und Qualitygate. |
| [`apothekenrecht`](./apothekenrecht) | Super-Plugin für Apothekenrecht: Betriebserlaubnis, ApBetrO, Versand, E-Rezept, BtM, Retaxation, Aufsicht und Compliance. |
| [`arbeitsrecht`](./arbeitsrecht) | Arbeitsrechtliche Workflows fuer Kuendigung, Befristung, Urlaub, AGG, Aufhebungsvertrag, Betriebsrat, Arbeitszeit, Lohn und Expansion. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und verifizierbarer Quelle verwendet. |
| [`arbeitszeugnis-analyse`](./arbeitszeugnis-analyse) | Analyse deutscher Arbeitszeugnisse nach Ampelsystem (Rot/Orange/Grün). Geheimcodes, Schaufenster-Drift, negative Codeworte, Steigerungsadverbien. Satzweise Notenmatrix, begründete Gesamtnotenspanne. Vollständiger Mandatsablauf: Erstgespräch, Mandantenbericht, Aufforderungsschreiben, Klagestrategie. |
| [`aufsichtsrat-ag-se-praxis`](./aufsichtsrat-ag-se-praxis) | Praxisplugin für Aufsichtsräte in AG und SE: Überwachung, Informationsrechte, Vorstand bestellen/abberufen, Vergütung, Ausschüsse, Protokoll, Business Judgment, Haftungsvermeidung, Börse, SE und Mitbestimmung. |
| [`aussenwirtschaft-zoll-sanktionen`](./aussenwirtschaft-zoll-sanktionen) | Freistehendes Plugin für Außenwirtschaft, Sanktionen, Zoll, Exportkontrolle, BAFA, TARIC, CBAM, Verbrauchsteuer, AWV, AML/KYC und Ermittlungen. |
| [`bank-rechtsabteilung`](./bank-rechtsabteilung) | Rechtsabteilung einer mittelgroßen deutschen Bank: Aufsicht, Kredit, Avale, Bürgschaften, Garantien, Trade Finance, ZAG/PSD2, PSD3/PSR-Vorschau, eWpG, MiCAR, Tokenisierung, BaFin, Vorstand, HV und Kanzleisteuerung. |
| [`barrierefreiheit-web-checker`](./barrierefreiheit-web-checker) | Web-Barrierefreiheits-Checker für BFSG, BFSGV, BITV 2.0, EN 301 549 und WCAG: Scope, Audit, Tastatur, Screenreader, Formulare, PDFs, Erklärung, Roadmap und Abnahme. |
| [`bav-strategie-konzern`](./bav-strategie-konzern) | Strategische Beratung zur betrieblichen Altersversorgung in Konzernen: Pensionsmodelle alle fuenf Durchführungswege CTA Pension Buyouts Drei-Stufen-Theorie Versorgungssystem-Harmonisierung internationale Benefits Restrukturierung DB-zu-DC im Duesseldorfer Boutique-Stil. |
| [`beamtenrecht`](./beamtenrecht) | Beamtenrecht für Bund, Länder und Richterdienst: Status, Laufbahn, Besoldung, Versorgung, Konkurrentenstreit, Disziplinarrecht, Dienstunfähigkeit, Richterlaufbahn, Landesrecht und verständliche Mandatsführung. |
| [`bereicherungs-und-anfechtungsrecht-pruefer`](./bereicherungs-und-anfechtungsrecht-pruefer) | Mechanisches Durchprüfen von Bereicherungsrecht §§ 812 ff. BGB, AnfG und Insolvenzanfechtung §§ 129-147 InsO. Mit KI-Screening von Schuldnerakten, § 135 Gesellschafterdarlehen, Bargeschäft § 142 und Verteidigung des Anfechtungsgegners. Keine Rechtsberatung. |
| [`berichtspflichten-erlediger`](./berichtspflichten-erlediger) | Berichtspflichten-Erlediger für mittelständische Unternehmen: amtliche Statistik, Portale, Umwelt-, Produkt-, Steuer-, Sozial-, Lieferketten-, Datenschutz- und Aufsichtsmeldungen mit Fristenboard, Datenquellen, Plausibilitätscheck und Behördenkommunikation. |
| [`berufsgerichtliche-verfahren-freie-berufe`](./berufsgerichtliche-verfahren-freie-berufe) | Plugin für anwaltsgerichtliche und berufsgerichtliche Verfahren gegen Anwälte, Patentanwälte, Steuerberater, Wirtschaftsprüfer und Notare: Kammeraufsicht, Rüge, Disziplinarverfahren, Zulassung, Vermögensverfall, beA, Werbung, Sachlichkeit und Rechtsmittel. |
| [`berufsrecht-anwaelte`](./berufsrecht-anwaelte) | Plugin für anwaltliches Berufsrecht: BRAO, BORA, FAO, beA, Kanzleisitz, Werbung, Interessenkollision, Verschwiegenheit, KI-/Cloud-Outsourcing, Schatten-KI, Berufsausübungsgesellschaft, Gebühren, Kammeraufsicht und anwaltsgerichtliche Risiken. |
| [`berufsrecht-ki-vertragspruefung`](./berufsrecht-ki-vertragspruefung) | Berufsrechtliche und strafrechtliche Vorprüfung von Verträgen mit Legal-AI-Anbietern: § 43e BRAO, § 203 StGB, Consumer-Tool-Abgrenzung, No-Training, Telemetrie, Drittstaat, KI-VO-Rollen, Art.-50-Transparenz, Schatten-KI und Klauselvorschläge. |
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
| [`commercial-courts-deutschland`](./commercial-courts-deutschland) | Commercial-Courts-Plugin für englischsprachige Wirtschaftsverfahren in Deutschland: Zuständigkeit, Wahlklauseln, Klage, Case Management, Beweis, Geheimnisschutz, Wortprotokoll/Transcript, Rechtsmittel, BGH, Kosten, Vollstreckung und bilingualer Schriftsatz-/Hearing-Workflow. |
| [`common-law-kompass`](./common-law-kompass) | Freistehendes Common-Law-Plugin für deutsche Wirtschaftsjuristen: UK/US-False-Friends, Vertragsbegriffe, Consideration, Suretyship, Indemnity, UCC, Precedent, Discovery und bilinguale Drafting-Reviews. |
| [`corporate-kanzlei`](./corporate-kanzlei) | Corporate-Kanzlei-Plugin: Deal-Kommandocenter, Datenraum, Due Diligence, SPA/APA, Umwandlung, StaRUG, Insolvenzplan, W&I, Signing/Closing, PMI. |
| [`datenbankrecht`](./datenbankrecht) | Großes Plugin zum deutschen und europäischen Datenbankrecht: UrhG §§ 87a ff., Datenbankrichtlinie, Investitionsschutz, Scraping, API, KI-Training, Vertrags- und Plattformkonflikte. |
| [`datenschutz-sanktionsverfahren-verteidigung`](./datenschutz-sanktionsverfahren-verteidigung) | Spezialplugin für Vertretung und Verteidigung in datenschutzrechtlichen Sanktionsverfahren: DSGVO-Bußgeld, OWiG/StPO, Art.-58-Anordnung, Verwaltungsgericht, Aufsichtsbehördenkommunikation, EuGH/EDPB und Behördenstrategie. |
| [`datenschutzrecht`](./datenschutzrecht) | DSGVO/BDSG/TDDDG – PIA/DPIA, AVV-Review, Auskunft Art. 15, Datenpanne Art. 33/34, Drittlandstransfer Art. 44 ff. inkl. US-Transfer, DPF, SCC, TIA, Behördenpaket und Brückenskills zur Sanktionsverteidigung. |
| [`designrecht-geschmacksmusterrecht`](./designrecht-geschmacksmusterrecht) | Eigenständiges Plugin für deutsches und europäisches Designrecht: DesignG, EU-Design, DPMA, EUIPO, WIPO-Hague, Neuheit, Eigenart, Anmeldung, Nichtigkeit, Verletzung, Eilrechtsschutz, Zoll, Plattformen und Designverträge. |
| [`deutsche-rechtsgeschichte`](./deutsche-rechtsgeschichte) | Mega-Plugin zur deutschen Rechtsgeschichte: Epochen, Quellenkritik, Rezeption, Reichsrecht, BGB, Weimar, NS-Unrecht, DDR/BRD und rechtsgeschichtliche Argumentation. |
| [`dfg-foerderantrag`](./dfg-foerderantrag) | DFG-Förderantragssteller für Sachbeihilfe, adaptive Anfänger-/Profi-Führung, kleine schnelle Anträge, große Koselleck-Strategien, elan-Formalia, Finanzplan, Reviewer-Red-Team, Forschungsdaten, KI-/Ethik-Check und Wiedereinreichung. |
| [`dsa-dma-digitalregulierung`](./dsa-dma-digitalregulierung) | Digitalregulierung der EU: DSA (VO 2022/2065) und DMA (VO 2022/1925) plus Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO und § 19a GWB. Gatekeeper-Schwellen VLOP-Einordnung Risikobewertung Art. 34 Forschungsdatenzugang Art. 40 Account-Sperre Art. 20-23 Zustellung Art. 13 DSA Klagewege. |
| [`ecommerce-recht`](./ecommerce-recht) | Super-Plugin für Online-Shops, Plattformen, Marktplätze und digitale Verbraucherprozesse. |
| [`einfache-leichte-sprache-jura`](./einfache-leichte-sprache-jura) | Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Standard-Annäherung, Zielgruppe klären, Rechtsinhalt sichern und Qualitätsgate nutzen. |
| [`einigungsvertrag-vermoegensrecht`](./einigungsvertrag-vermoegensrecht) | Einigungsvertrag-Plugin für DDR/BRD-Übergangsrecht, Volksvermögen, Parteivermögen, Treuhand, Bodenreform, Mauergrundstücke, VermG und Restitution. |
| [`email-umformulierer-berufsrecht`](./email-umformulierer-berufsrecht) | Formuliert unfreundliche, emotionale oder unsachliche E-Mails in hoefliche, sachliche und berufsrechtskonform formulierte Texte um. Fokus auf BRAO/BORA-Konformität, mit Varianten für Steuerberater, Notare und allgemeine berufliche Korrespondenz. |
| [`energierecht`](./energierecht) | Freistehendes Energierecht-Plugin für Stadtwerke, Versorger, Wärme, Netze, Vertrieb, Industrie, EEG, KWKG, Verfahren, Transaktionen und Projektfinanzierung. |
| [`erbbaurecht-praxis`](./erbbaurecht-praxis) | Praxisplugin für Erbbaurecht und Erbbaugrundbuch: Erbbaurechtsvertrag, Erbbauzins, Wertsicherung, Heimfall, Zustimmung, Belastung, Finanzierung, Veräußerung, Laufzeit, Entschädigung, Zwangsversteigerung, Rang und Grundbuchvollzug. |
| [`europarecht-kompass`](./europarecht-kompass) | Freistehendes Europarecht-Plugin gegen deutsche Denkfehler: Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Charta, Grundfreiheiten, Beihilfen, Vorlageverfahren und EU-Drafting. |
| [`fachanwalt-agrarrecht`](./fachanwalt-agrarrecht) | Plugin Fachanwalt für Agrarrecht. Höferecht (HöfeO Anerbenrecht Länder) Landpachtrecht BGB §§ 581 ff. GAP EU-Direktzahlungen Cross-Compliance Düngeverordnung Pflanzenschutz Tierschutz Forstrecht. Schnittstelle Plugin fachanwalt-erbrecht. |
| [`fachanwalt-arbeitsrecht`](./fachanwalt-arbeitsrecht) | Fachanwalt-Arbeitsrecht nach FAO Paragraf 10: KSchG, BetrVG, TzBfG, AGG, EntgTranspG, Urlaub, Betriebsrat, Befristung und Vergleichspraxis. Rechtsprechung nur mit Datum, Aktenzeichen und verifizierter Quelle. |
| [`fachanwalt-bank-kapitalmarktrecht`](./fachanwalt-bank-kapitalmarktrecht) | Plugin Fachanwalt für Bank- und Kapitalmarktrecht. KWG ZAG WpHG WpIG MiFID-II MAR MiCAR Verbraucherkredit, Bürgschaft, Aval, Bankgarantie, Vermögensanlage und Beratungshaftung. |
| [`fachanwalt-bau-architektenrecht`](./fachanwalt-bau-architektenrecht) | Plugin Fachanwalt für Bau- und Architektenrecht. BGB Werkvertrag VOB-A VOB-B VOB-C HOAI Bauordnungsrecht. Bauvertrag Maengelhaftung Abnahme Vergaberecht. Schnittstellen Plugin fachanwalt-vergaberecht kanzlei-allgemein. |
| [`fachanwalt-erbrecht`](./fachanwalt-erbrecht) | Plugin Fachanwalt für Erbrecht. BGB Erbrecht §§ 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaftsteuer EU-ErbVO. Schnittstellen Plugin steuerrecht-anwalt-und-berater kanzlei-allgemein. |
| [`fachanwalt-familienrecht`](./fachanwalt-familienrecht) | Plugin Fachanwalt für Familienrecht. Orientierung Normen Mandate Fristen Literatur. Familiengericht FamFG Scheidung Sorge Umgang Unterhalt Zugewinn Ehevertrag eingetragene Lebenspartnerschaft. Ergaenzend zum Plugin kanzlei-allgemein. |
| [`fachanwalt-gewerblicher-rechtsschutz`](./fachanwalt-gewerblicher-rechtsschutz) | Plugin Fachanwalt für gewerblichen Rechtsschutz nach FAO § 14k. MarkenG. DesignG. UWG. PatG GebrMG. UrhG-Bezuege. Markenanmeldung DPMA EUIPO. UWG-Abmahnung §§ 8 ff. UWG. Designverletzung. Einstweilige Verfuegung Verletzungsklage Lizenzanaloger Schadensersatz. |
| [`fachanwalt-handels-gesellschaftsrecht`](./fachanwalt-handels-gesellschaftsrecht) | Plugin Fachanwalt für Handels- und Gesellschaftsrecht nach FAO § 14i. HGB. AktG. GmbHG. PartGG. UmwG. Geschäftsführerhaftung §§ 43 GmbHG 93 AktG. Gesellschafterstreit Beschlussanfechtung. Handelsvertreterausgleich § 89b HGB. MoPeG GbR seit 2024. Schnittstellen kanzlei-allgemein. |
| [`fachanwalt-insolvenz-sanierungsrecht`](./fachanwalt-insolvenz-sanierungsrecht) | Plugin Fachanwalt für Insolvenz- und Sanierungsrecht nach FAO § 14. InsO Eroeffnung Antragspflicht § 15a Gläubigerantrag § 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung §§ 129 ff. InsO. Schnittstellen insolvenzrecht und steuerrecht-anwalt-und-berater. |
| [`fachanwalt-internationales-wirtschaftsrecht`](./fachanwalt-internationales-wirtschaftsrecht) | Plugin Fachanwalt für Internationales Wirtschaftsrecht. CISG Bruessel Ia Rom I Rom II Schiedsverfahren ICC UNCITRAL Investitionsschutz ICSID WTO EU-Aussenhandel LkSG. Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-it-recht`](./fachanwalt-it-recht) | Plugin Fachanwalt für Informationstechnologierecht. SaaS Software-Lizenz DSGVO BDSG TTDSG TKG NIS2 DDG DSA DMA EU-KI-VO Open-Source. Schnittstellen Plugin datenschutzrecht ki-governance kanzlei-allgemein. |
| [`fachanwalt-medizinrecht`](./fachanwalt-medizinrecht) | Plugin Fachanwalt für Medizinrecht. Arzthaftung §§ 630a ff. BGB Patientenrechte Vertragsarztrecht Berufsrecht Aerzte SGB V Krankenversicherung MPDG Apothekenrecht. Schnittstellen Plugin fachanwalt-sozialrecht und kanzlei-allgemein. |
| [`fachanwalt-miet-wohnungseigentumsrecht`](./fachanwalt-miet-wohnungseigentumsrecht) | Großer Fachanwalt-Kompass Miet- und Wohnungseigentumsrecht mit über 200 Skills für Wohnraum, Gewerberaum, Betriebskosten, WEG, Hausverwaltung, Beschlüsse, GEG, Beweise, Fristen und Workflows. |
| [`fachanwalt-migrationsrecht`](./fachanwalt-migrationsrecht) | Großer Fachanwalt-Kompass Migrationsrecht mit über 200 Skills für Aufenthalt, Blaue Karte EU, Fachkräfte, Asyl, Dublin/GEAS, Einbürgerung, Staaten-/Gebietschecks und spanische/einfache Erklärung. |
| [`fachanwalt-sozialrecht`](./fachanwalt-sozialrecht) | Plugin Fachanwalt für Sozialrecht nach FAO § 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch § 84 SGG Klage § 87 SGG Eilantrag § 86b SGG. Buergergeld Erwerbsminderung GdB Pflegegrad Hilfsmittel Eingliederungshilfe. Bescheidanalyse Akteneinsicht PKH Fristenbuch. |
| [`fachanwalt-sportrecht`](./fachanwalt-sportrecht) | Plugin Fachanwalt für Sportrecht. Verbandsrecht (DFB FIFA UEFA IOC DOSB) CAS Schiedsverfahren Spielerverträge Doping WADA-Code NADA Sponsoring Persönlichkeitsrechte Veranstalterhaftung. Schnittstelle Plugin gesellschaftsrecht. |
| [`fachanwalt-strafrecht`](./fachanwalt-strafrecht) | Plugin Fachanwalt Strafrecht: StPO/StGB, Nebenstrafrecht, Verteidigung, Ermittlungsverfahren, HV, Revision, Nebenklage und Zeugenbeistand plus Strafprozess-Cockpit fuer Fristen, Aktenlog, U-Haft, Akteneinsicht, HV-Tagesmappe, Antragslog und Mandanteninstruktionen. |
| [`fachanwalt-transport-speditionsrecht`](./fachanwalt-transport-speditionsrecht) | Plugin Fachanwalt für Transport- und Speditionsrecht. HGB §§ 407 ff. Frachtvertrag §§ 453 ff. Spedition CMR COTIF Montrealer Übereinkommen Haager Visby Regeln ADSp. Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-urheber-medienrecht`](./fachanwalt-urheber-medienrecht) | Plugin Fachanwalt für Urheber- und Medienrecht. UrhG UWG KUG Recht am eigenen Bild Presserecht Persoenlichkeitsrecht Medienstaatsvertrag. Schnittstellen Plugin gewerblicher-rechtsschutz verlagsredaktion kanzlei-allgemein. |
| [`fachanwalt-vergaberecht`](./fachanwalt-vergaberecht) | Plugin Fachanwalt fuer Vergaberecht als Vergabe-Workbench: GWB 97 ff., VgV, UVgO, SektVO, KonzVgV, VOB/A, Schwellenwerte 2026/2027, Vergabeakte, Ruge, Nachpruefung, TED/eForms, Wettbewerbsregister und Foerdermittel. |
| [`fachanwalt-verkehrsrecht`](./fachanwalt-verkehrsrecht) | Plugin Fachanwalt für Verkehrsrecht. StVG StVO PflVG VVG-Bezuege. Verkehrsunfall Personen- und Sachschaden Bußgeld Fahrerlaubnis Verkehrsstrafrecht (§§ 315c 316 StGB). Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-versicherungsrecht`](./fachanwalt-versicherungsrecht) | Plugin Fachanwalt für Versicherungsrecht. VVG VAG Berufsunfähigkeit private Krankenversicherung Lebens- und Rentenversicherung Sachversicherung Haftpflicht D-und-O. Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-verwaltungsrecht`](./fachanwalt-verwaltungsrecht) | Plugin Fachanwalt für Verwaltungsrecht. VwGO VwVfG. Anfechtungs- und Verpflichtungsklage Eilrechtsschutz § 80 Abs 5 VwGO einstweilige Anordnung Normenkontrolle Polizei- und Ordnungsrecht. Schnittstelle Plugin kanzlei-allgemein. |
| [`factoring-recht`](./factoring-recht) | Super-Plugin für Factoring, Forderungskauf, Aufsichtsrecht, Vertragsgestaltung, Debitorenkommunikation, Insolvenz- und Sanierungsfragen. |
| [`fahrgastrechte`](./fahrgastrechte) | Fahrgastrechte im Eisenbahnverkehr nach VO (EU) 2021/782 und EVO 2023: Verspätung und Ausfall einordnen, Entschädigung berechnen (25/50 Prozent), Forderung an die DB, Widerspruch, Schlichtung und Klage zum Amtsgericht. Katalog der DB-Ablehnungsgründe. |
| [`fashion-law-moderecht`](./fashion-law-moderecht) | Praxisplugin Fashion Law/Moderecht für Modeunternehmen, Designer, Händler und Kanzleien: IP, Designs, Marken, Textilkennzeichnung, Produktsicherheit, Nachhaltigkeit, Lieferkette, Plattformen, E-Commerce, Vertrieb, Influencer und Krisen. |
| [`festlandchina-wirtschaftsverkehr`](./festlandchina-wirtschaftsverkehr) | Mega-Plugin für wirtschaftlichen Umgang mit Festlandchina: Fabrik, Import, Export, Investition, De-Risking, Lieferkette, IP, Daten, Exportkontrolle und politisches Risiko. |
| [`fluggastrechte`](./fluggastrechte) | Fluggastrechte selber geltend machen nach VO (EG) Nr. 261/2004. Tickets erfassen, Annullierung oder Verspaetung pruefen, aussergewoehnliche Umstaende, Distanz, Ausgleich, Forderungsschreiben, Mahnung und Klage. Rechtsprechung nur nach Live-Verifikation. |
| [`forderungsmanagement-klagewerkstatt`](./forderungsmanagement-klagewerkstatt) | Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben. |
| [`forschungszulage-antragstellung`](./forschungszulage-antragstellung) | Forschungszulage-Antragstellung nach FZulG: adaptiver Fördercheck, BSFZ-Portaltexte mit Zeichenbudgets, Finanzamt-Antrag, FuE-Abgrenzung, Bemessungsgrundlage 2026, Auszahlung, Verlust-/Insolvenzlage, Dokumentation, Beihilfen, Einspruch und Mehrjahresroadmap. |
| [`fortbestehensprognose`](./fortbestehensprognose) | Fortbestehensprognose § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwoelf-Monats-Liquiditaet. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose. |
| [`franchiserecht-praxis`](./franchiserecht-praxis) | Wirtschaftsrechtliches Plugin für Franchise-Systeme: vorvertragliche Aufklärung, Handbuch, Gebühren, Gebietsschutz, Kartellrecht, Kündigung, Expansion, Streit und Insolvenz. |
| [`gebrauchsmusterrecht`](./gebrauchsmusterrecht) | Eigenständiges Plugin für deutsches Gebrauchsmusterrecht: GebrMG, DPMA-Anmeldung, Recherche nach § 7 GebrMG, Abzweigung, Neuheitsschonfrist, Verletzung, Löschung, BPatG-Beschwerde, Lizenz, FTO und Schnellschutz für technische Produkte. |
| [`geldwaeschepraevention-aml-kyc`](./geldwaeschepraevention-aml-kyc) | Freistehendes Plugin für Geldwäscheprävention, AML, KYC, GwG-Risikoanalyse, UBO, PEP, Sanktionen, FIU/goAML, Transparenzregister und Behördenverfahren. |
| [`gesellschaftsgruender`](./gesellschaftsgruender) | Anfängerfreundlicher Gründungsassistent für deutsche Gesellschaften: Rechtsformwahl, Satzung, SHA, Cap Table, Notar, Handelsregister, Bank/KYC, Behörden, Steuerstart, IP, Datenschutz, erste 100 Tage und Streitprävention. |
| [`gesellschaftsrecht`](./gesellschaftsrecht) | Gesellschaftsrecht – GmbH/AG/Personengesellschaften, M&A-Due-Diligence ohne Discovery (Q&A + Datenraum), Gesellschafterbeschlüsse, HRB/HRA-Anmeldungen, Closing Checklists, Compliance-Fristen. |
| [`gesellschaftsrecht-legal-english`](./gesellschaftsrecht-legal-english) | Didaktisches Gesellschaftsrecht — English Business Terms: Corporate Legal English fuer Big-Law-Anfaenger. Dealroom: Cap Table vs Gesellschafterliste; Term Sheet; SHA; Vesting; Drag/Tag; Liquidation Preference; Anti-Dilution; SPA; DD; Notar/HR; Multi-Format-Auswertung; Frankfurt-Startup-Akte. |
| [`gesellschaftsrechtliche-treuepflicht`](./gesellschaftsrechtliche-treuepflicht) | Großes Prüfplugin zur gesellschaftsrechtlichen Treuepflicht in GmbH, AG, SE, Personengesellschaft, Familiengesellschaft und Konzern: Stimmrecht, Minderheitenschutz, Gesellschafterliste, Einziehung, Ausschluss, Konkurrenz, Sanierung, Treuepflichtverletzung und Rechtsfolgen. |
| [`gewerblicher-rechtsschutz`](./gewerblicher-rechtsschutz) | Gewerblicher Rechtsschutz – DPMA/EUIPO-Markenrecherche und -anmeldung, Freedom-to-Operate, Patentscreening, UWG- und Urheberrechts-Abmahnung (Versand und Reaktion), Open-Source-Compliance, IP-Klausel-Review, Schutzrechts-Fristen. |
| [`goae-gebuehrenordnung-aerzte`](./goae-gebuehrenordnung-aerzte) | Super-Plugin zur GOÄ: private Arztrechnungen prüfen, erstellen, begründen, beanstanden und prozessual verwerten. |
| [`grosskanzlei-corporate-ma`](./grosskanzlei-corporate-ma) | Freistehendes Big-Law-Corporate/M&A-Plugin: Deal-OS, Padlet-Canvas, Anfänger-/First-Year-Coach, Aktenanlage, Datenraum, Legal DD, Tabellenreview, SPA/APA, W&I, Public M&A, UmwG/UmwStG, StaRUG, Fusionskontrolle, FDI, FSR, Signing/Closing, PMI und 125 Spezial-Skills. |
| [`grundbuchamt-praxis`](./grundbuchamt-praxis) | Praxisplugin für Grundbuchamt, Grundbuchauszug und grundbuchtaugliche Nachweise: Abteilung I/II/III lesen, Bewilligung, Antrag, Auflassung, Rang, Zwischenverfügung, Beschwerde, Grundschuldbrief, Aufgebot, Dienstbarkeiten, Vormerkung, Vorkaufsrecht, Teilung und Vollzug. |
| [`handelsrecht-hgb`](./handelsrecht-hgb) | Reines HGB-Plugin für Handelsrecht: Kaufmann, Handelsregister, Firma, Prokura, Handlungsvollmacht, Handelsgeschäfte, Handelskauf, Handelsvertreter, Makler, Kommission, Fracht, Spedition, Lager, Handelsbücher sowie OHG/KG einschließlich MoPeG-Statuswechsel von GbR zu OHG. |
| [`handelsregister-praxis`](./handelsregister-praxis) | Praxisplugin für den Umgang mit dem Handelsregister: Anmeldung, Registergericht, Rechtspfleger, Registerrichter, Beanstandung, Zwischenverfügung, Beschwerde, Gesellschafterliste, Kapitalmaßnahmen, Firma, Vertretung, Prokura, Löschung, Insolvenzvermerk und registerfeste Nachweise. |
| [`handelsvertreterrecht`](./handelsvertreterrecht) | Handelsvertreterrecht nach HGB: Status, Provision, Buchauszug, Kündigung, Ausgleich § 89b, Wettbewerbsverbot § 90a und Vertriebsmodelle. |
| [`hausarbeitenmacher`](./hausarbeitenmacher) | Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten. Führt sokratisch durch Zivilrecht öffentliches Recht Strafrecht mit Ausfluegen in Europarecht und Rechtstheorie. Adressaten-Strategie ohne Schleimerei. Liefert keine fertigen Lösungen sondern führt zur eigenen Subsumtion. |
| [`haushaltsrecht-bho-bund-laender`](./haushaltsrecht-bho-bund-laender) | Großes Haushaltsrecht-Plugin für BHO, HGrG, Bundeshaushalt, Länderhaushalte, Titelanalyse, Umschichtung, Sondervermögen, Szenarien und Dashboard. |
| [`hinweisgeberschutz-compliance`](./hinweisgeberschutz-compliance) | Hinweisgeberschutzgesetz in der Praxis: interne/externe Meldestelle, NDA-Konflikte, Repressalien, Untersuchungen, Datenschutz und Governance. |
| [`hoai-leistungsphasen-praxis`](./hoai-leistungsphasen-praxis) | Großplugin für HOAI-Leistungsphasen 1 bis 9: Grundlagenermittlung, Vorplanung, Entwurf, Genehmigung, Ausführungsplanung, Vergabe, Bauüberwachung, Objektbetreuung, Honorar, Vertrag, Haftung, Nachträge und Bauprojektsteuerung. |
| [`hochschulrecht-laender`](./hochschulrecht-laender) | Hochschulrecht der Länder: Hochschulgesetze, Satzungen, Gremien, Zulassung, Exmatrikulation, Berufung, Drittmittel, Promotion und Aufsicht. |
| [`immobilienrechtspraxis`](./immobilienrechtspraxis) | Werkzeuge fuer immobilienrechtliche Rechtsabteilungen: musterbasierte Vertragserstellung mit Klauselschutz, Vertragspruefung gegen Playbook, Grundbuchanalyse, Sachverhaltsermittlung, Mieteranfragen, Case Management und AVV-Pruefung. Rechtsprechung nur nach Live-Verifikation. |
| [`influencer-recht`](./influencer-recht) | Plugin für Influencer, Creator, Agenturen und Unternehmen: Werbekennzeichnung, Steuer, Umsatzsteuer, Sachleistungen, Plattformrecht, Medienrecht, Marken, Urheberrecht, Datenschutz und Verträge. |
| [`informationsfreiheit-presseauskunft`](./informationsfreiheit-presseauskunft) | IFG-, Transparenz-, UIG-, VIG- und Presseauskunfts-Plugin für Bund, Länder und Behörden: Antrag, Kosten, Fristen, Widerspruch, Klage und Tracking. |
| [`insiderrecht-compliance`](./insiderrecht-compliance) | Insiderrecht- und Marktmissbrauchs-Plugin für Emittenten, Vorstände, Aufsichtsräte, IR, Banken und Kanzleien: MAR Art. 7/8/10/14/17/18/19, Ad-hoc, Aufschub, Insiderliste, Handelsverbote, Directors' Dealings, Market Sounding, Leaks und BaFin-Kommunikation. |
| [`insolvenzforderungsanmeldungspruefung`](./insolvenzforderungsanmeldungspruefung) | Freistehendes Plugin für die Insolvenzforderungsanmeldungsprüfung: Intake, § 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Prüfungstermin, Bestreiten, Feststellung, Tabellenauszug und Verteilung. |
| [`insolvenzplan-starug-planwerkstatt`](./insolvenzplan-starug-planwerkstatt) | Freistehendes Plugin für Insolvenzplan und StaRUG-Restrukturierungsplan: Intake, Sanierungskonzept, Vergleichsrechnung, Gruppen, Klassen, darstellender und gestaltender Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Planvollzug. |
| [`insolvenzrecht`](./insolvenzrecht) | Insolvenzrechtliche Skills zu Zahlungsunfähigkeit, Überschuldung, Antragspflicht und Gläubigerantrag. |
| [`insolvenzverwaltung`](./insolvenzverwaltung) | Freistehendes Insolvenzverwaltungs-Plugin aus Sicht von Insolvenzverwalter, Sachwalter und vorläufiger Verwaltung: Regelverfahren, Eigenverwaltung, Schutzschirm, Anfechtung, § 15b InsO, Masse, Forderungsprüfung, Insolvenzplan, StaRUG-Planwerkstatt, Gutachten, Berichte und Schlussrechnung. |
| [`internal-investigations-praxis`](./internal-investigations-praxis) | Praxisplugin für interne Untersuchungen: Auftrag und Scope, Honeypot-Risiko, Legal Hold, Interviews, Arbeitsrecht, Betriebsrat, Datenschutz, Geschäftsgeheimnisse, Beschlagnahme, Behördenstrategie, Privilege, Reporting und US-Discovery. |
| [`internationales-handelsrecht-lex-mercatoria`](./internationales-handelsrecht-lex-mercatoria) | Mega-Plugin für internationales Handelsrecht, CISG, Incoterms, UNIDROIT Principles, Lex Mercatoria, Schiedsverfahren, Trade Finance und Lieferkettenverträge. |
| [`jurastudium`](./jurastudium) | Studium und Referendariat – Prüfungsgespräch nach AG-Tradition, Subsumtionslehre, Methodenlehre (Zivilrecht, Strafrecht, Öffentliches Recht), Rechtsgeschichte, Lernstrategien, Lösungsschemata, Gutachtenstil, Klausurkorrektur, Lernplanung. |
| [`juristische-sprache-deutsch-als-zweitsprache`](./juristische-sprache-deutsch-als-zweitsprache) | Plugin fuer Menschen im deutschen Recht mit anderer Herkunftssprache: einfache Erklaerungen, Juristendeutsch, Bescheide, Schriftsaetze, Grammatik, Fristen und Verfahrenslogik. |
| [`jveg-kostenpruefer`](./jveg-kostenpruefer) | Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle. |
| [`kanzlei-allgemein`](./kanzlei-allgemein) | Kanzlei-Allgemein-Plugin (fusioniert mit Cowork): edles Kommandocenter Mandatsannahme/GwG Klage/Replik Vertrag Rechtsprechung Handelsregister beA-Journal Rechnung UStVA Fristenbuch Timesheet RVG Versand-Vor-Check Posteingang Mandantenakte Mahnwesen Tagesbrief Geburtstage Weihnachtskarten. |
| [`kanzlei-builder-hub`](./kanzlei-builder-hub) | Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Deployment in die Kanzleiumgebung. |
| [`kanzlei-management`](./kanzlei-management) | Mega-Plugin für Kanzlei-Management aus Sicht Managing Partner/Management Committee: Partnerkreis, Cashflow, Pricing, UBT, FTE, Utilization, WIP, Associate-Retention, Operations, Risiko und Dashboards. |
| [`kanzlei-mandant-lifecycle`](./kanzlei-mandant-lifecycle) | Lifecycle-Plugin für Kanzlei, Mandant und Rechtsabteilung: Mandatsstart, OCG, Budget, Dashboard, Rechnung, Litigation, Erwartungsmanagement und Relationship-Governance. |
| [`kartellrecht-marktabgrenzung-pruefung`](./kartellrecht-marktabgrenzung-pruefung) | Globales Kartellrecht/Competition Law: GWB, Art 101/102 AEUV, Fusionskontrolle, BKartA, DG Competition, FTC/DOJ, ICN-Jurisdiktionen, Dawn Raids, Marktabgrenzung, Missbrauch, Private Enforcement. |
| [`ki-governance`](./ki-governance) | EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie. |
| [`ki-richtlinie-kanzleien`](./ki-richtlinie-kanzleien) | Erstellt und pflegt eine berufsrechtskonforme KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen mit Anwaelten und Syndikus-Anwaelten. Beruht auf BRAO, BORA, DSGVO, KI-Verordnung sowie BRAK- und DAV-Hinweisen. |
| [`ki-vo-ai-act-pruefer`](./ki-vo-ai-act-pruefer) | Mechanik-Workflow zur KI-VO (EU 2024/1689): KI-System-Definition, Rollen, Risikoklassen, Hochrisiko-Diagnose, GPAI, Art. 43-Konformitätsbewertung, CE/EU-DB, Marktbeobachtung und Konformitäts-Evidence-Pack. |
| [`kommunalrecht-laender`](./kommunalrecht-laender) | Großes Kommunalrecht-Plugin für Gemeinden, Städte, Landkreise, Satzungen, Räte, Bürgerbegehren, Kommunalfinanzen, Aufsicht und Landesrecht. |
| [`krankenhausrecht`](./krankenhausrecht) | Super-Plugin für deutsches Krankenhausrecht: Planung, Finanzierung, Entgelte, Reform, Qualität, MD-Prüfung, Klinikbetrieb und Rechtsstreit. |
| [`krankenkassenrecht-krankenversicherung`](./krankenkassenrecht-krankenversicherung) | Plugin für GKV, PKV, Beihilfe-Schnittstellen und Krankenversicherungsrecht: Leistungen, Beiträge, Krankengeld, Hilfsmittel, Widerspruch, MD, Versicherungsvertrag und Kostenerstattung. |
| [`kriegsdienstverweigerung-wehrdienst`](./kriegsdienstverweigerung-wehrdienst) | Praxisplugin für Kriegsdienstverweigerung und Wehrdienst aus Gewissensgründen: Art. 4 Abs. 3 GG, KDVG n. F. 2026, Antrag über BAPersBw, BAFzA-Entscheidung, Gewissensbegründung, Soldaten, Reservisten, Rechtsschutz und saubere Abgrenzung zur Totalverweigerung. |
| [`krisenfrueherkennung-starug`](./krisenfrueherkennung-starug) | Krisenfrüherkennung und Krisenmanagement nach StaRUG: Pflicht zum 24-Monats-Frühwarnsystem nach § 1 StaRUG, § 102 StaRUG Warnpflicht der Berater, Geschäftsführerhaftung, drohende Zahlungsunfähigkeit, integrierte Planung, Restrukturierungsplan und Stabilisierungsanordnung. |
| [`leasingrecht-praxis`](./leasingrecht-praxis) | Wirtschaftsrechtliches Praxisplugin für Leasing, Sale-and-lease-back, Equipment Finance, Fahrzeugflotten, IT-Leasing, Insolvenz, Restwert, Sicherheiten und Vertragsgestaltung. |
| [`legistik-werkstatt`](./legistik-werkstatt) | Legistik-Werkstatt für Ministerien, Bundestag, Fraktionen/Opposition, Länder, Landtage und Normgeber. Baut Referenten- und Kabinettsentwürfe, Vorlagen aus der Mitte, Änderungs-/Entschließungsanträge, Rechtsverordnungen und Satzungen mit Begründung, Synopse, XML und Prüfpfaden. |
| [`liquiditaetsplanung`](./liquiditaetsplanung) | Liquiditaetsplanung nach deutschem Recht: 3-Wochen-Vorschau, 13/26/52-Wochen-Forecast, Excel-Export, Quote/Luecken-Ampel, Dokumentationspaket und Schnittstellen zu Fortbestehensprognose und Insolvenzrecht. Rechtsprechung nur nach Live-Verifikation. |
| [`lizenzvertragsersteller`](./lizenzvertragsersteller) | Baukastensystem für IP-Lizenzverträge nach deutschem, europäischem und internationalem Recht: Urheberrecht, Software, Patent, Marke, Design, Gebrauchsmuster, Geschäftsgeheimnis, Know-how, Escrow, TT-GVO, DSGVO, Exportkontrolle, Quellensteuer und fertige DE/EN-Vertragsentwürfe. |
| [`lobbyregister-bundestag`](./lobbyregister-bundestag) | Lobbyregister-Bundestag-Superplugin mit 50 geführten Skills für Registrierungspflicht, Ausnahmen, Registereintrag, Regelungsvorhaben, Stellungnahmen, Finanzdaten, Aktualisierung, Verhaltenskodex, Meldung von Verstoessen und Fristen nach LobbyRG. |
| [`luftrecht-flughafenrecht`](./luftrecht-flughafenrecht) | Luftrecht-Plugin für LuftVG, LuftSiG, LBA, Flughäfen, Airlines, Slots, Flugzeugpfandrechte, Beschlagnahme, Insolvenz, Drohnen und Aviation-Compliance. |
| [`mandantenanfragen-assistent`](./mandantenanfragen-assistent) | Assistent für Anwaltskanzleien zur Erstantwort auf Mandantenanfragen per E-Mail: dankt foermlich übernimmt die Anrede aus der eingehenden E-Mail nennt die telefonische Terminvergabe bittet um Sachverhalt per E-Mail oder bietet eine Telefon-Transkription mit DSGVO-Einwilligungshinweis an. |
| [`markenrecht-fashion-luxus`](./markenrecht-fashion-luxus) | Großes Markenrechts-Plugin für DE/EU/US und internationale Portfolios: DPMA, EUIPO, WIPO/Madrid, USPTO, Markenarten, Schutzhindernisse, Benutzung, Widerspruch, Verfall/Nichtigkeit, Enforcement, Plattformen, Zoll, Lizenzen und Luxus-Fashion-Spezialfälle. |
| [`meinungspruefer`](./meinungspruefer) | Meinungsprüfer für Äußerungsrecht: Meinung oder Tatsache, Beleidigung, üble Nachrede, Verleumdung, § 188 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR/EuGH, OLG-Praxis, US-Supreme-Court-Vergleich, Zivilrecht, Plattformen, Social Media, Arbeitsplatz, Schule und kommunale Machtkritik. |
| [`memorandums-ersteller`](./memorandums-ersteller) | Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral. Alias Memorandumsmacher. |
| [`methodenlehre-buergerliches-recht`](./methodenlehre-buergerliches-recht) | Methodenlehre und Rechtsanwendung im deutschen buergerlichen Recht aus Anwaltsperspektive: Anspruchsaufbau, Auslegung, Abwaegung, Praezedenzarbeit, Rechtsfortbildung, Methodenwahl, EU-Methodik und methodenehrliche Begruendungskontrolle. |
| [`mietrecht`](./mietrecht) | Mietrecht für Mieter und Vermieter mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitaetsstaedte. Datenerhebung Mieterhoehungs-Widerspruch Mietsenkungsverlangen Nebenkostenprüfung und Erstellung Mieteranfragen Klageentwurf zum Amtsgericht. |
| [`mittelstand-corporate-ma`](./mittelstand-corporate-ma) | Freistehendes Mittelstandsmandat-Corporate/M&A-Plugin: Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, Umwandlung, StaRUG/Insolvenzplan, CP-Kalender, E-Rechnung/GoBD, PMI. |
| [`nachbarschaftsstreit-pruefer`](./nachbarschaftsstreit-pruefer) | Nachbarrecht und Nachbarschaftsstreit: Überbau, Überhang, Äste/Wurzeln, Grenzbaum, Zaun/Mauer/Hecke, Immissionen, Vertiefung, Notweg, Hammerschlagsrecht, Beweise, Aufforderung, Klage und Vergleich. |
| [`nda-abgleich`](./nda-abgleich) | Gleicht NDA-Entwurf der Gegenseite gegen eigenen Standard ab und setzt Haltelinien chirurgisch im Word-Aenderungsmodus durch. Ampelmatrix ROT/GELB/GRUEN. Ausgabe .docx mit echten Tracked Changes. Keine Absatzlöschungen, keine Klausel-Neufassungen. |
| [`nda-verschwiegenheit-generator-checker`](./nda-verschwiegenheit-generator-checker) | Allgemeiner NDA-Ersteller und NDA-Prüfer für deutsche und internationale Verschwiegenheitsvereinbarungen: Entwurf, Redline, GeschGehG, HinSchG, AGB, Arbeitsrecht, M&A, Forschung, Software, Datenraum und Verletzungsreaktion. |
| [`nis2-cybersecurity-compliance`](./nis2-cybersecurity-compliance) | NIS-2, BSIG 2025, BSI, IT-Grundschutz, Cloud, Incident Response und technische Security-Compliance für Geschäftsleitung, CISO und Legal. |
| [`normenkontrolle-bauleitplanung`](./normenkontrolle-bauleitplanung) | Freistehendes Plugin für die Prüfung und Anfechtung von Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften nach § 47 VwGO vor BayVGH und OVG. Mandatsperspektive Antragstellervertretung. |
| [`normenkontrollrat-nkr`](./normenkontrollrat-nkr) | Plugin fuer den Nationalen Normenkontrollrat (NKR): Pruefung von Referentenentwuerfen Formulierungshilfen und Gesetzentwuerfen auf Erfuellungsaufwand Erforderlichkeit Verhaeltnismaessigkeit One-in-one-out Digitalcheck Mittelstandsfreundlichkeit und Praktikabilitaet im Vollzug. |
| [`notariat-alltag`](./notariat-alltag) | Alltagsplugin für Notariat, Notariatsmitarbeitende und Notarinnen/Notare: Beurkundung, Vollzug, Register, Grundbuch, Geldwäsche, Kosten, Fristen und Mandantenkommunikation. |
| [`oeffentliches-wirtschaftsrecht`](./oeffentliches-wirtschaftsrecht) | Öffentliches-Wirtschaftsrecht-Plugin für Scheinprivatisierung, ÖPP, Projektfinanzierung, kommunale Unternehmen, Beihilfen, Vergabe und Regulierung. |
| [`ordnungswidrigkeitenrecht`](./ordnungswidrigkeitenrecht) | Allgemeines OWiG-Plugin für Bußgeldverfahren: Anhörung, Bescheid, Einspruch, Behörde, Akteneinsicht, Gericht, Verjährung, Einziehung und Nebenfolgen. |
| [`parteienrecht-parteiorganisation`](./parteienrecht-parteiorganisation) | Parteienrechts- und Parteiorganisations-Plugin für formale Parteiarbeit: Parteiengesetz, Satzung, Mitgliederrechte, Parteitage, Kreis- und Bezirksversammlungen, Kandidatenaufstellung, Wahlvorschläge, Parteigerichte, Spenden, Rechenschaft, Abgeordnetenrecht und Wahlleiterkommunikation. |
| [`patentrecherche`](./patentrecherche) | Patentrecherche für Patentanwaelte agentisch in Espacenet Google Patents DPMAregister DEPATISnet EPO Register WIPO USPTO. Stand der Technik Neuheit § 3 PatG Art. 54 EPUe erfinderische Tätigkeit § 4 PatG Art. 56 EPUe Problem-Solution-Approach FTO CPC IPC INPADOC Recherchebericht. |
| [`patentrecht`](./patentrecht) | Großes Patentrechts-Plugin für Erfindungsaufnahme, Patentanmeldung, Anspruchsentwurf, Recherche, Neuheit, erfinderische Tätigkeit, FTO, Abmahnung, Claim Chart, Vorbenutzungsrecht, Lizenz, Erfinderbenennung, Einspruch, Nichtigkeit, Register und Fristen. |
| [`phishing-vorfall-pruefer`](./phishing-vorfall-pruefer) | Freistehender Phishing-Vorfall-Prüfer für Online-Banking: BGB § 675u, § 675v, § 675w, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Bankpflichten, Schlichtung und Klage. |
| [`preussisches-allgemeines-landrecht-pralr`](./preussisches-allgemeines-landrecht-pralr) | PrALR-Plugin zum Allgemeinen Landrecht für die Preußischen Staaten: Quellenkritik, Textzeugen, Zivilrecht, Staats-/Polizeirecht, Strafrecht, Ständerecht, Aufopferung und Rezeptionsgeschichte. |
| [`private-equity-praxis`](./private-equity-praxis) | Private-Equity-Praxis-Plugin für deutsche Kanzleien, Investoren, Fonds, Family Offices und Unternehmen: Fund Formation, KAGB/AIF, ELTIF, Deal Execution, Private Credit, Schuldschein, LMA, NPL, Portfolio, Exit und Distressed. |
| [`produktrecht`](./produktrecht) | Produkthaftung und Produktrecht: Produktsicherheit, GPSR, ProdHaftG, deliktische Produzentenhaftung, Right to Repair, Software-/OTA-Updates, digitale Produktlebenszyklen, Rückruf, Marktüberwachung und Launch-Review. |
| [`prozessrecht`](./prozessrecht) | Prozessrechtliche Skills für Mandate, Fristen, Mahnbescheid, Eilverfahren, Vollstreckung und Schriftsätze. |
| [`pruefungsrecht-hochschule`](./pruefungsrecht-hochschule) | Hochschulprüfungsrecht: Prüfungsordnung, Bewertungsspielraum, Akteneinsicht, Krankheit, Nachteilsausgleich, Täuschung, KI, Drittversuch und Eilrechtsschutz. |
| [`rechtsberatungsstelle`](./rechtsberatungsstelle) | Pro-Bono- und Rechtsberatungsstellen (RDG-konform): Mandantenintake, Fristenkontrolle, Übergabe am Semesterende, mandantenfreundliche Briefe. |
| [`rechtstheorie-rechtsphilosophie`](./rechtstheorie-rechtsphilosophie) | Rechtstheorie- und Rechtsphilosophie-Plugin fuer juristische Praxis: Rechtsbegriff, Kelsen-orientierte Normgeltung, Demokratie, Rechtsrealismus, Systemdenken, Besitzdogmatik, Law-and-Economics, Hayek-Wissensproblem, spontane Ordnung, Machtkritik und anti-dezisionistische Red-Team-Pruefung. |
| [`regulatorisches-recht`](./regulatorisches-recht) | Aufsichtsrecht – KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds, Wochendigest. |
| [`rentenpruefer`](./rentenpruefer) | Rentenprüfer für gesetzliche Rente, Versorgungswerk und internationale Versicherungszeiten: Kontenklärung, Rentenantrag, Nachversicherung, Auslandszeiten, Bescheide, Widerspruch und verständliche Dokumentation. |
| [`robotik-recht`](./robotik-recht) | Robotik-Recht Deutschland/EU: Maschinenverordnung, KI-VO, Produkthaftung, ProdSG, Datenschutz, CRA, Data Act, CE, Marktüberwachung, Unfälle, Rückruf, Verträge und Robotik-Testakte. |
| [`roemisch-katholisches-kirchenrecht`](./roemisch-katholisches-kirchenrecht) | Römisch-katholisches Kirchenrecht nach CIC und Katechismus: papsttreue Workflows für Sakramente, Ehe, Kirchenaustritt, Verfahren, Disziplin, Pfarrei, Diözese, Kurie, Gericht/Hölle/Umkehr und mehrsprachige Kommunikation. |
| [`roemisches-recht`](./roemisches-recht) | Mega-Plugin zum römischen Recht: Zwölftafelgesetz, Institutionensystem, Sachenrecht, Obligationen, Aktionenrecht, Erbrecht, Juristenrecht, Justinian, byzantinisches Recht und Rezeption. |
| [`schoeffen-handelsrichter-praxis`](./schoeffen-handelsrichter-praxis) | Plugin für Schöffen, Jugendschöffen, ehrenamtliche Richter und Handelsrichter: Rolle, Rechte, Pflichten, Sitzung, Beratung, Befangenheit, Beweiswürdigung, Handelskammer, Verwaltungsgericht und sichere praktische Orientierung. |
| [`schriftform-und-textform-bgb`](./schriftform-und-textform-bgb) | Formerfordernisse im deutschen Zivilrecht: Schriftform, Textform, qES, Zugang, beA/ERV und Prozessordnungen. Mit Checklisten, Dokumentation und Rechtsprechung nur nach Live-Verifikation. |
| [`schulrecht-laender`](./schulrecht-laender) | Schulrecht der Länder: Schulpflicht, Aufnahme, Inklusion, Noten, Versetzung, Ordnungsmaßnahmen, Datenschutz, Elternrechte und Eilrechtsschutz. |
| [`seerecht-schifffahrtsrecht`](./seerecht-schifffahrtsrecht) | See- und Schifffahrtsrecht-Plugin für Schiffskauf, Schiffbau, Werften, Schiffshypothek, Schiffsregister, Arrest, Wrack, Bergung, Charter und ITLOS. |
| [`selbstvertreter-amtsgericht`](./selbstvertreter-amtsgericht) | Selbstvertretung vor dem Amtsgericht ohne Anwalt: Anfänger-Workflow, Fristen, Zuständigkeit, §23 GVG/§511 ZPO-Grenzen, Klage/Erwiderung/Replik, Beweise, PKH, Termin, Sanity-Check, Rechtsprechungschat, Berufung. |
| [`selbstvertreter-sozialgericht`](./selbstvertreter-sozialgericht) | Selbstvertretung vor dem Sozialgericht ohne Anwalt: Anfänger-Workflow, Widerspruch, Klage, Eilantrag, Pflegegrad, Krankenkasse, Bürgergeld, EM-Rente, GdB, Belege, Gutachten, Kostenfreiheit, Sanity-Check, Rechtsprechungschat, Berufung. |
| [`softwarerecht-de-eu-us`](./softwarerecht-de-eu-us) | Softwarerecht Deutschland/EU/International/USA: Entwicklung, Lizenzen, SaaS, Open Source, Arbeitnehmer/Freelancer, Softwarepatente, AI-Code und Streit. |
| [`solo-selbststaendige-praxis`](./solo-selbststaendige-praxis) | Praxisplugin für Solo-Selbstständige in Deutschland: Start, Anmeldung, Steuern, Verträge, Rechnungen, Datenschutz, Statusfeststellung, KSK, Versicherungen, Zahlungsausfall, Krise, Wachstum und Alltag ohne juristische Überforderung. |
| [`sozialversicherungsstatus-pruefer`](./sozialversicherungsstatus-pruefer) | Sozialversicherungsstatus und DRV-Statusfeststellung: Geschäftsführer, Freelancer, Anwälte, Lehrkräfte, Musikschulen, Plattformarbeit und Scheinselbständigkeit. |
| [`staatsanwaltschaft-praxis-einstieg`](./staatsanwaltschaft-praxis-einstieg) | Praxisplugin für neue Staatsanwältinnen, Staatsanwälte und Sitzungsdienst: Ermittlungsverfahren, Polizei, RiStBV, Vermerke, Beschlagnahme, digitale Beweise, Anklage, Strafbefehl, Hauptverhandlung, Plädoyer und Rechtsmittel. |
| [`startup-hr-personalabteilung-berlin`](./startup-hr-personalabteilung-berlin) | Personalabteilungs- und HR-Operations-Plugin für ein Berliner Start-up mit ca. 100 Beschäftigten: Arbeitsverträge, Payroll/DATEV-Schnittstelle, Personalakten, Datenschutz, AGG-Vorfälle, Betriebsrat, Benefits, Fehlzeiten, Kündigungen, Happiness-Management und Chef-Briefings. |
| [`status-navigator-step-plan`](./status-navigator-step-plan) | Status-Navigator und Step-Plan-Macher als bewusst normfreies Dokumentenverarbeitungs-Plugin: sortiert chaotische Akten, baut Excel-/Padlet-Statuspläne, markiert vorhandene und fehlende Unterlagen, Lücken, Fristen, Unterschriften, Zustellungen und nächste Arbeitsschritte ohne rechtliche Bewertung. |
| [`steuerrecht-anwalt-und-berater`](./steuerrecht-anwalt-und-berater) | Steuerrecht für Anwalt (anw- FAO § 9) und Steuerberater (stb-): Einspruch Klage FG Aussenprüfung Selbstanzeige, Grundsteuer, Grunderwerbsteuer, Share Deals, Signing Closing, BWA SuSa Lohnbuchhaltung Jahresabschluss. |
| [`strafanzeige-vorbereiter`](./strafanzeige-vorbereiter) | Vorsichtiger Strafanzeigen-Vorbereiter: prüft Anfangsverdacht, Beweise, Strafantrag, Risiken falscher Verdächtigung, Alternativen und erstellt nur bei tragfähiger Tatsachengrundlage eine nüchterne Strafanzeige. |
| [`strafbefehl-verteidiger`](./strafbefehl-verteidiger) | Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung. |
| [`strafzumessung`](./strafzumessung) | Strafzumessung nach deutschem Strafrecht vom Strafbefehl bis zur grossen Strafkammer. § 46 StGB Strafzumessungstatsachen Tagessatz Geldstrafe Freiheitsstrafe Bewaehrung § 56 § 49 Regelbeispiele besonders schwerer Fall Verstaendigung § 257c StPO TOA § 46a Gesamtstrafe § 55 JGG. |
| [`strassenrecht-infrastruktur`](./strassenrecht-infrastruktur) | Straßenrecht-Plugin für Bundesfernstraßen, Landesstraßen, Gemeindestraßen, Widmung, Planfeststellung, Sondernutzung, Baulast und Erhaltung. |
| [`strassenverkehrsrecht-stvo`](./strassenverkehrsrecht-stvo) | StVO-/Straßenverkehrsrecht-Plugin für Verkehrsregeln, Zeichen, Anordnungen, Ausnahmegenehmigungen, Fahrerlaubnis, Bußgeld-Schnittstellen und Behördenpraxis. |
| [`subsumtions-pruefer`](./subsumtions-pruefer) | Interaktiver Subsumtions-Workflow für deutsches Recht und Europarecht: Tatbestandsmerkmale zerlegen, Vier-Schritt-Schema anwenden, Rechtsfolgen und Einreden prüfen. Keine Rechtsberatung. |
| [`tabellenreview-3d`](./tabellenreview-3d) | 3D-Tabellenreview als Wuerfel: Spaltenprompts pro Datenpunkt x Zeilenprompts pro Dokument x Arbeitsblatt-Perspektiven (Recht / Steuer / Wirtschaft) gestapelt. Massenprüfung Vertragsstapel M&A-DD Immobilien Vendor-Onboarding mit Excel-Mehrblatt Kreuzblatt-Konsistenz Audit-Trail Belegkette. |
| [`telekommunikationsrecht`](./telekommunikationsrecht) | Großes Telekommunikationsrecht-Plugin für TKG, Bundesnetzagentur, Internetanschlüsse, Anbieterwechsel, Kundenschutz, Netzregulierung, Frequenzen, Nummerierung, Sonderkartellrecht, Datenschutz und Sicherheitsanforderungen. |
| [`tierschutzrecht`](./tierschutzrecht) | Tierschutzrecht-Plugin für TierSchG, BGB § 90a, Haltung, Zucht, Transport, Tierversuche, Behördenverfahren, Strafrecht, Bußgeld und zivilrechtliche Tierfälle. |
| [`umweltrecht`](./umweltrecht) | Freistehendes Umweltrecht-Plugin für BImSchG, TEHG, Abfall, Wasser, Boden, Naturschutz, UIG, Verfahren, Bußgeld, Umwelt-Due-Diligence, Klimaklagen UmwRG, Lieferkettensorgfalt LkSG/CSDDD und ESG-Greenwashing/CSRD. |
| [`umweltschutzverband-verbandsklage`](./umweltschutzverband-verbandsklage) | Plugin für Umweltverbände: UmwRG, Aarhus, UIG, UVP, BImSchG, Planfeststellung, § 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz. |
| [`urheberrecht-de-eu`](./urheberrecht-de-eu) | Deutsches und EU-Urheberrecht fuer Werkhoehe, Musik, KI, TDM, Software, Lizenzen, Abmahnung, Schranken, Leistungsschutz und Rechteclearing. |
| [`urteilsbauer-relationsmacher`](./urteilsbauer-relationsmacher) | Urteils- und Beschluss-Werkstatt für Amts- Land- und Familienrichter sowie Rechtspfleger. Aktenintake Relation Beweiswürdigung mit Richter-Input Tatbestandsmerkmale Tenor Tatbestand Entscheidungsgründe Rechtsmittelbelehrung. Erzeugt DOCX nach Paragraf 313 ZPO. |
| [`us-bankruptcy-code`](./us-bankruptcy-code) | US Bankruptcy Code Title 11: Chapters 7/9/11/12/13/15, Automatic Stay, Claims, DIP, 363 Sales, Plans und Cross-Border. |
| [`us-copyright-registrierung-verlag`](./us-copyright-registrierung-verlag) | US Copyright Act fuer deutsche Verlage und Rechteinhaber: Title 17, Registrierung, Rechte, Fair Use, DMCA, Musik, AI, Litigation und Deals. |
| [`venture-capital-geber`](./venture-capital-geber) | VC-Geber-Plugin für deutsche Venture-Capital-Investoren, Family Offices, Angels und junge VCs: Sourcing, Deal-Tracking, Wandeldarlehen, SAFE, Pre-Seed, Series A/B, Cap Table, Follow-on, Portfolio-Updates, KAGB/BaFin-Grenzen, EU/CH/UK/US-Brücken und legitime Deal-Taktik. |
| [`verbraucher-rechtsstaat-alltag`](./verbraucher-rechtsstaat-alltag) | Kleines, hilfreiches Plugin für Verbraucher: E-Commerce, Kaufrecht, Reparaturen, kleine Dienstleistungen, Rechnungen, Inkasso, Plattformen, Behördenbriefe und Gerichtspost verständlich einordnen und vorsichtig reagieren. |
| [`verbraucherinsolvenz-schuldenbereinigung`](./verbraucherinsolvenz-schuldenbereinigung) | Verbraucherinsolvenz und Schuldenbereinigung nach InsO: außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, Antrag, Restschuldbefreiung, P-Konto, ehemalige Selbstständige und lebensnahe Verfahrensführung. |
| [`verbraucherschutzrecht-pruefer`](./verbraucherschutzrecht-pruefer) | Großer Verbraucherschutz-Prüfer für BGB, EGBGB, UWG, UKlaG, VSBG, E-Commerce, digitale Produkte, Reise, Finanzen, Energie, Gesundheit und Alltag. |
| [`verbraucherschutzverband-durchsetzung`](./verbraucherschutzverband-durchsetzung) | Plugin für Verbraucherverbände: VDuG, UKlaG, UWG, Abhilfeklage, Musterfeststellung, Unterlassung, Register, Finanzierung, Vergleich und Kampagnenakte. |
| [`vereinsrecht-vereinsmanager`](./vereinsrecht-vereinsmanager) | Vereinsrechts- und Vereinsmanagement-Plugin für eingetragene und nicht eingetragene Vereine: Gründung, Satzung, Mitgliederversammlung, Vorstand, Protokolle, Beschlüsse, Gemeinnützigkeit, Register, Haftung, Datenschutz, Finanzen, Veranstaltungen und Spezialvereine. |
| [`verfassungsrecht`](./verfassungsrecht) | Deutsches Verfassungsrecht unter dem Grundgesetz aus Sicht einer Spezialkanzlei. Rechtsprechungsgetrieben mit Live-Recherche auf bundesverfassungsgericht.de. Acht Skills für Gesetzgebungskompetenz formelle und materielle Verfassungsmäßigkeit Grundrechte und Verfassungsbeschwerde. |
| [`verhaeltnismaessigkeitspruefer`](./verhaeltnismaessigkeitspruefer) | Verhältnismäßigkeitsprüfer mit 61 Skills zur vierstufigen Schranken-Schranke: Vorprüfung Schutzbereich/Eingriff/Rechtfertigung, absolute Grenzen (Wesensgehalt, Menschenwürde), Bestimmtheit, Wesentlichkeitstheorie, BVerfG-Leitentscheidungen, PrOVG-Kreuzberg-Linie sowie Rechtsvergleich zu Südafrika Section 36, Kanada Oakes, EGMR/EMRK, EuGH/Charta, USA und 12 europäischen Rechtsordnungen (FR IT ES NL BE AT LU DK PL CZ GR IE), audiovisuelle Leitentscheidungen-Sammlung, Padlet- und ASCII-/Mermaid-Visualisierung. |
| [`verkehr-infrastrukturrecht`](./verkehr-infrastrukturrecht) | Freistehendes Verkehrs- und Infrastrukturrecht-Plugin für Verkehrsplanung, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Parkraum und Verkehrswende. |
| [`verkehrsowi-verteidiger`](./verkehrsowi-verteidiger) | Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht. |
| [`verlagsrecht-buchpreisbindung`](./verlagsrecht-buchpreisbindung) | Plugin für Verlagsrecht, Verlagsgesetz, Autoren- und Herausgeberverträge, Buchpreisbindung, Titelschutz, Vertrieb, E-Book, Hörbuch und verlagsnahe Compliance. |
| [`verlagsredaktion`](./verlagsredaktion) | Verlagsdesk fuer juristische und fachliche Verlage: Eingangskorb, Manuskript, Redaktion, Rechtecheck, Zitate, Bildrechte, Autorenkommunikation, Heftplanung, Buchprojekte, Satzfahnen, Metadaten, Marketing und Produktionsuebergabe. |
| [`versammlungsrecht`](./versammlungsrecht) | Praxisplugin für Versammlungsrecht und Versammlungsfreiheit: Anzeige unter freiem Himmel, Landesrecht, Behörde, Fristen, Spontan- und Eilversammlung, Ordner, Kooperationsgespräch, Auflagen, Verbot, Eilrechtsschutz und Durchführung ohne vorauseilende Selbstzensur. |
| [`versicherungsrecht`](./versicherungsrecht) | Großes Versicherungsrecht-Plugin für VVG, VAG, europäische Versicherungsaufsicht, Lebensversicherung, BU, PKV, Rechtsschutz, Kreditversicherung, D&O, Cyber, Sach- und Haftpflichtdeckung. |
| [`vertragsausfueller`](./vertragsausfueller) | Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten. |
| [`vertragsrecht`](./vertragsrecht) | Vertragsrecht – Lieferanten- und Vertriebsverträge, AGB §§ 305 ff. BGB, NDA, SaaS-/MSA-Review, Renewal-Tracking, Eskalations-Routing, Business-Zusammenfassungen. |
| [`wahlkampfrecht-praxis`](./wahlkampfrecht-praxis) | Wahlkampfrecht und Wahlkampfpraxis fuer Parteien, Kandidierende und Kampagnenteams: Strategie, Plakatierung, Social Media, Datenschutz, politische Werbung, Parteienfinanzierung, Desinformation, Veranstaltungen, Schulen, Podien, Wahltag und Compliance. |
| [`wandeldarlehen-lebenszyklus`](./wandeldarlehen-lebenszyklus) | Begleitet den vollständigen Lebenszyklus eines Wandeldarlehens für GmbH und UG: Vertragserstellung (bilingual/einsprachig), Beurkundungsprüfung, Wandelereignisse, Wandlungsberechnung, Cap-Table-Update, Gesellschafterbeschluss und Notar-Paket. |
| [`weg-hausverwaltung`](./weg-hausverwaltung) | Operatives WEG- und Hausverwaltungs-Plugin fuer Beschluesse, Eigentuemerversammlung, Protokoll, Beschlusssammlung, Wirtschaftsplan, Jahresabrechnung, Hausgeld, Sonderumlage, Betriebskosten, Handwerker, bauliche Veraenderungen, Steckersolar, Wallbox, Verwalter, Beirat und Anwalt-Eskalation. |
| [`weltraumrecht`](./weltraumrecht) | Großes Plugin für deutsches, europäisches und internationales Weltraumrecht: Raumfahrtverträge, Satelliten, Haftung, Weltraumbahnhof, Raketen, Raumstationen, Frequenzen, Exportkontrolle und Space Property. |
| [`word-legal-ai-plugin-and-skill-for-german-lawyers`](./word-legal-ai-plugin-and-skill-for-german-lawyers) | Word Legal AI for German Lawyers: Kaltstart, Kanzleistil, makrofreies Word-Finish, Verträge, Schriftsätze, Memos, Redlines, Klauselbibliothek, Defensive Drafting, Term Sheet, DE-EN Bilingual, US/UK Legal Writing und englische Verträge nach deutschem Recht. |
| [`zitierweise-deutsches-recht`](./zitierweise-deutsches-recht) | Deutsche juristische Hauszitierweise v4.0: Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. |
| [`zwangsverwaltung-zvg`](./zwangsverwaltung-zvg) | Freistehendes ZVG-Plugin für Zwangsverwaltung und Versteigerung: Beschlagnahme, Besitz, Mieten, Treuhandkonto, Berichte, Verteilung, ZVG-Portal-Recherche, Bieterangebote und Versteigerungsteilnahme. |
| [`zwangsvollstreckung`](./zwangsvollstreckung) | Plugin Zwangsvollstreckung §§ 704 ff. ZPO: Mahn-/Vollstreckungsbescheid, PfÜB Bank/Arbeit, § 802l Kontensuche, Vermögensauskunft, Räumung, § 800 ZPO Notar, § 201 InsO, ZVG, EU-Kontenpfändung VO 655/2014, § 765a Härtefall, Schuldnerschutz. |

## Schnellstart

Dieses Skill-Set lässt sich auf drei Wegen einbinden. Empfohlen ist **Weg 1** über die grafische Oberfläche; **Weg 2** für gezielten ZIP-Upload einer bestimmten Version; **Weg 3** für Claude Code im Terminal.

> 📆 **Release- vs. main-Stand.** Den **letzten Release-Tag** findest du auf der Seite [Releases](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Über **Weg 1 (Marketplace-Sync)** und **Weg 3 (Marketplace-Kommando)** wird der `main`-Branch geladen — das ist meist **neuer** als der letzte Release-Tag (Zwischen-Commits mit Fixes, neuen Tests, kleinen Ergänzungen). Über **Weg 2 (ZIP-Upload aus Release)** bekommst du den **getaggten, validierten Stand**. Für Stabilität → Weg 2; für neueste Korrekturen → Weg 1/3.

> 💡 **Findest du in Cowork kein Feld für den GitHub-Pfad oder macht der Mac beim ZIP-Upload Ärger?** Dann ist in deiner Oberfläche der Marketplace-Weg vermutlich noch nicht freigeschaltet oder macOS hat die ZIP anders behandelt als erwartet. Lade die Plugin-ZIPs einzeln aus dem [Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) herunter und installiere sie über denselben Dialog, mit dem du z. B. "Legal Plugin" installierst. Mac-Hinweise zu Safari-Auto-Entpacken, iCloud-Platzhaltern, MegaZIP vs. Einzel-ZIP und Terminal-Check: **[INSTALLATION_EINFACH.md](./INSTALLATION_EINFACH.md)**.

### Voraussetzungen

- Ein **Claude-Account** (Free oder Pro) – https://claude.ai/login
- Entweder **Claude Desktop** (https://claude.com/download) **oder** **Claude Code** (`npm install -g @anthropic-ai/claude-code`, danach `claude` im Terminal).
- Für Weg 3 zusätzlich `git`.

### Weg 1 — Installation über "Customize → Skills" (GUI, empfohlen)

Einfachster Weg in Claude Desktop oder der Cowork-Oberfläche:

1. Claude Desktop öffnen und in der linken Seitenleiste auf **Customize** klicken.
2. Auf **Skills** wechseln und neben "Personal plugins" das **+**-Symbol anklicken.
3. Im Dialogfeld den Pfad des GitHub-Repositorys im Format `owner/repo` eingeben: **`Klotzkette/claude-fuer-deutsches-recht`**.
4. Auf **Sync** klicken. Cowork liest daraufhin den Marketplace und listet alle Plugins (z. B. `arbeitsrecht`, `vertragsrecht`, Liquiditätsplanung (`liquiditaetsplanung`), `insolvenzrecht`, `steuerrecht-anwalt-und-berater` ...).
5. Beim gewünschten Plugin auf **Install** klicken. Nach erfolgreicher Installation wechselt der Button zu **Manage**.
6. Eine neue Konversation starten — die Skills stehen ab sofort zur Verfügung. Tipp: Mit `/skill` oder freier Eingabe (z. B. "Erstelle eine 3-Wochen-Liquiditätsvorschau") wird der passende Skill automatisch erkannt.

### Weg 2 — Manueller ZIP-Upload als Plugin

Wenn kein Marketplace-Manifest verwendet werden soll oder eine bestimmte Version festgehalten werden muss:

1. Das gewünschte einzelne Plugin-ZIP aus dem neuesten Release herunterladen, z. B. `liquiditaetsplanung.zip` von https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest.
2. In Cowork **Customize → Skills / Plugins** öffnen und über **+ → Create → Upload plugin** dieses einzelne Plugin-ZIP hochladen.
3. Nach dem Upload erscheint das Plugin in der Plugin-Liste und kann aktiviert werden.

**Wichtig:** Nicht das komplette Repository-ZIP aus **Code → Download ZIP** hochladen. Ein Upload-ZIP muss direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` usw. im ZIP-Root enthalten.

### Weg 3 — Marketplace-Kommando (Claude Code im Terminal)

Claude Code starten (`claude` im Terminal) und dann:

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install arbeitsrecht@klotzkette-german-legal-skills
/plugin install vertragsrecht@klotzkette-german-legal-skills
/plugin install liquiditaetsplanung@klotzkette-german-legal-skills
/plugin install insolvenzrecht@klotzkette-german-legal-skills
/plugin install steuerrecht-anwalt-und-berater@klotzkette-german-legal-skills
```

Einzelne Plugins lassen sich auch später mit `/plugin install <name>@klotzkette-german-legal-skills` nachinstallieren; `/plugin list` zeigt den aktuellen Stand.

Alternativ ein lokal geklontes Repository nutzen:

```bash
git clone https://github.com/Klotzkette/claude-fuer-deutsches-recht.git
cd claude-fuer-deutsches-recht
claude
```

Und dann im Claude-Code-Prompt:

```text
/plugin marketplace add .
/plugin install <plugin-name>@klotzkette-german-legal-skills
```

### Mac-Hinweise für Cowork / Claude Desktop

Wenn Nutzerinnen und Nutzer auf dem Mac scheitern, liegt es häufig an der heruntergeladenen Datei:

- Safari kann ZIP-Dateien nach dem Download automatisch entpacken. Für Cowork muss aber die **einzelne Plugin-ZIP** hochgeladen werden, nicht der entpackte Ordner.
- `alle-plugins-megazip.zip` ist nur ein Sammelarchiv. Es muss zuerst entpackt werden; anschließend die darin enthaltenen Plugin-ZIPs einzeln hochladen.
- Nicht das GitHub-Repository-ZIP aus **Code → Download ZIP** verwenden. Das ist Quellcode, kein direkt installierbares Plugin-ZIP.
- Bei iCloud-Desktop/Downloads die ZIP erst lokal vollständig laden. Im Zweifel nach `~/Downloads/claude-plugins/` verschieben und dann aus diesem lokalen Ordner auswählen.
- Beim Cowork-Organisations-Upload müssen Plugin-ZIPs gültige ZIP-Dateien unter 50 MB sein; für alle 213 Plugins ist GitHub-Sync/Marketplace robuster als manueller Einzelupload.
- Technischer Check im Terminal:

```bash
file ~/Downloads/claude-plugins/liquiditaetsplanung.zip
unzip -l ~/Downloads/claude-plugins/liquiditaetsplanung.zip | head
```

Der ZIP-Root muss `.claude-plugin/plugin.json` und `skills/` enthalten. Wenn das Upload-Fenster stattdessen einen GitHub-Pfad verlangt, ist das der Marketplace-Dialog; für ZIPs zurückgehen und **Upload from .zip / Create → Upload plugin** wählen.

### Überprüfen, ob die Installation funktioniert hat

- In Claude Desktop: in der Plugin-Liste muss neben dem Plugin **Manage** statt **Install** stehen.
- In Claude Code: `/plugin list` zeigt das Plugin als aktiviert.
- Funktionstest: in einer neuen Konversation einen typischen Auftrag stellen, z. B. "Mache eine 3-Wochen-Liquiditätsvorschau für meine GmbH" → der Skill `liquiditaetsvorschau-3wochen` sollte sichtbar geladen werden.

Details und Fehlersuche siehe [`QUICKSTART.md`](./QUICKSTART.md).

## Schwerpunkte für die deutsche Praxis

Dieses Repository ist vollständig auf das deutsche Recht und die Arbeitsweise deutscher Kanzleien zugeschnitten:

- Urteile sind nicht bindend; Ausnahme: § 31 BVerfGG.
- Vorprozessuale Beweiserhebung ist auf eng begrenzte gesetzliche Instrumente beschränkt: §§ 142, 144 ZPO; § 810 BGB; § 242 BGB; Art. 15 DSGVO; Auskunfts- und Stufenklage (§ 254 ZPO).
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und verifizierbarer Quelle zitieren; BeckRS-, Kommentar- und Aufsatz-Blindzitate sind gesperrt.
- Zitierweise und Quellenprüfung: verbindlich in [`references/zitierweise.md`](./references/zitierweise.md).
- Due Diligence läuft über Q&A, Datenraum und anwaltliche Sachverhaltsaufklärung.
- Kündigungsschutz: Regelfall nach KSchG ab 6 Monate / mehr als 10 Arbeitnehmer.

### Materielle Rechtsgebiete

- **Zivilrecht & Vertragsrecht** – `bgb-at-pruefer`, `bgb-bt-pruefer`, `vertragsrecht`, `nda-abgleich`, `agb-pruefung` (in `vertragsrecht`), `produktrecht`, `fluggastrechte`
- **Arbeitsrecht** – `arbeitsrecht`, `fachanwalt-arbeitsrecht` (Kündigungsschutzklage § 4 KSchG, Aufhebungsvertrag mit Sperrzeit-Prüfung, BR-Anhörung § 102 BetrVG, Massenentlassung § 17 KSchG)
- **Gesellschafts- & Wirtschaftsrecht** – `gesellschaftsrecht`, `gesellschaftsrecht-legal-english`, `fachanwalt-handels-gesellschaftsrecht`, `grosskanzlei-corporate-ma`, `mittelstand-corporate-ma`, `corporate-kanzlei`, `private-equity-praxis`, `venture-capital-geber`, `fachanwalt-internationales-wirtschaftsrecht`
- **Bank-, Kapitalmarkt- & Aufsichtsrecht** – `bank-rechtsabteilung`, `fachanwalt-bank-kapitalmarktrecht`, `private-equity-praxis`, `venture-capital-geber`, `regulatorisches-recht`, `berichtspflichten-erlediger`, `geldwaeschepraevention-aml-kyc`, `aussenwirtschaft-zoll-sanktionen`
- **Insolvenz & Sanierung** – `insolvenzrecht` (Gläubiger/Schuldner), `insolvenzverwaltung` (Verwalter-Sicht, § 270d, § 15b, § 129 ff.), `zwangsverwaltung-zvg` (ZVG-Verwalter, § 155 Verteilungsplan), `insolvenzforderungsanmeldungspruefung`, `insolvenzplan-starug-planwerkstatt`, `fortbestehensprognose`, `fachanwalt-insolvenz-sanierungsrecht`
- **Liquidität, Forderung & Inkasso** – `liquiditaetsplanung`, `forderungsmanagement-klagewerkstatt`, `phishing-vorfall-pruefer`, `vertragsausfueller`, Inkasso nach RDG / § 43d BRAO (in `regulatorisches-recht`)
- **Steuerrecht und Förderung** – `steuerrecht-anwalt-und-berater` (Bescheidanalyse, Einspruch, Außenprüfung, Selbstanzeige, Grundsteuer, Grunderwerbsteuer, Share Deals, weltweite DBA-Matrix, Signing/Closing, Steuerberater-Werkzeuge), `berichtspflichten-erlediger`, `forschungszulage-antragstellung`, `dfg-foerderantrag`
- **Strafrecht & OWi** – `aktenaufbereiter-strafrecht`, `fachanwalt-strafrecht`, `strafanzeige-vorbereiter`, `strafbefehl-verteidiger`, `strafzumessung`, `verkehrsowi-verteidiger`
- **Verwaltungs- & Verfassungsrecht** – `verfassungsrecht`, `verhaeltnismaessigkeitspruefer`, `versammlungsrecht`, `wahlkampfrecht-praxis`, `fachanwalt-verwaltungsrecht` (Eilantrag § 80 V VwGO), `verkehr-infrastrukturrecht`, `umweltrecht`, `energierecht`, `normenkontrollrat-nkr`, `fachanwalt-vergaberecht`
- **Familien-, Erb-, Sozial- & Betreuungsrecht** – `fachanwalt-familienrecht` (Düsseldorfer Tabelle, Sorge, Umgang, Unterhalt), `fachanwalt-erbrecht` (Pflichtteilsberechnung), `fachanwalt-sozialrecht`, `rentenpruefer`, `betreuungsrecht`, `fachanwalt-migrationsrecht`
- **Miet- & Immobilienrecht** – `mietrecht`, `weg-hausverwaltung`, `nachbarschaftsstreit-pruefer`, `fachanwalt-miet-wohnungseigentumsrecht`, `immobilienrechtspraxis`
- **Gewerblicher Rechtsschutz & Medien** – `gewerblicher-rechtsschutz` (Markenanmeldung DPMA, UWG-Abmahnung), `fachanwalt-gewerblicher-rechtsschutz`, `fachanwalt-urheber-medienrecht` (Gegendarstellung), `patentrecht`, `patentrecherche`, `gebrauchsmusterrecht`, `designrecht-geschmacksmusterrecht`, `markenrecht-fashion-luxus` (DPMA/EUIPO/WIPO/USPTO, Markenarten, Klassen, Benutzung, Verfall/Nichtigkeit, Enforcement, Plattformen, Zoll, Lizenzen, Luxus-Fashion und US-Trade-Dress), `fashion-law-moderecht` (Mode-Lifecycle, Textilkennzeichnung, Produktsicherheit, Nachhaltigkeit, Lieferkette, Plattformen und Retail)
- **Insolvenz, Sanierung und Krisenmanagement (erweitert)** – `krisenfrueherkennung-starug` (§ 1 StaRUG mit Vier-und-zwanzig-Monats-Horizont, § 102 StaRUG-Warnpflicht, Restrukturierungsplan, Stabilisierungsanordnung, Cross-Class-Cram-Down), ergänzt durch `insolvenzplan-starug-planwerkstatt` und `fachanwalt-insolvenz-sanierungsrecht`
- **Arbeits- und Vergütungsrecht (erweitert)** – `bav-strategie-konzern` (betriebliche Altersversorgung als Konzern-Architektur: alle fünf Durchführungswege, CTA-Doppeltreuhand, Pension Buyouts, Drei-Stufen-Prüfung, internationale Benefits, Düsseldorf-Kyoto-Profil)
- **IT-Recht, Datenschutz, Telekommunikation, digitale Barrierefreiheit, Robotik & KI-Governance** – `datenschutzrecht` (Art. 15 DSGVO, Art. 33/34 DSGVO), `telekommunikationsrecht` (TKG/Bundesnetzagentur/Internetanschluss), `barrierefreiheit-web-checker` (BFSG/BFSGV/BITV/WCAG), `fachanwalt-it-recht` (Cyber-Incident 72 h), `ki-governance` (EU AI Act), `robotik-recht` (Maschinenverordnung, KI-VO, CRA, Produkthaftung), DORA-IKT-Vertragsprüfung in `regulatorisches-recht`, `berufsrecht-ki-vertragspruefung`
- **Verkehr, Transport, Versicherung, Medizin** – `fachanwalt-verkehrsrecht`, `fachanwalt-transport-speditionsrecht` (CMR/HGB), `versicherungsrecht`, `fachanwalt-versicherungsrecht`, `fachanwalt-medizinrecht`, `fachanwalt-bau-architektenrecht` (VOB/B)
- **Sportrecht, Agrarrecht** – `fachanwalt-sportrecht` (CAS-Berufung), `fachanwalt-agrarrecht` (GAP-Sammelantrag)
- **Europa- & Common-Law-Kompass** – `europarecht-kompass`, `common-law-kompass`

### Querschnittliche Werkzeuge

- **Prozess- & Schriftsatz-Werkstatt** – `prozessrecht` (Mahnbescheid §§ 688 ff. ZPO, einstweilige Verfügung §§ 935/940 ZPO + Schutzschrift, Vollstreckung), `anlagen-zu-schriftsaetzen`, `status-navigator-step-plan`, `memorandums-ersteller`, `tabellenreview-3d`
- **Kanzleibetrieb** – `kanzlei-allgemein`, `kanzlei-builder-hub`, `kanzlei-mandant-lifecycle`, `rechtsberatungsstelle`, `verlagsredaktion`
- **Methode & Lehre** – `jurastudium` (Methodenlehre ZR/StR/ÖR, Subsumtion, Rechtsgeschichte, Lernstrategien, Lösungsschemata, Prüfungsgespräch nach AG-Tradition), `methodenlehre-buergerliches-recht`, `rechtstheorie-rechtsphilosophie`, `preussisches-allgemeines-landrecht-pralr`, `zitierweise-deutsches-recht`, `einfache-leichte-sprache-jura`
- **Drafting & Sprache** – `word-legal-ai-plugin-and-skill-for-german-lawyers` (39 Skills: Kaltstart-Triage, deutscher Kanzleistil, makrofreies Word-Finish, Verträge, Schriftsätze, Memos, Klauselbibliothek, Defensive Drafting, Entwurfscheck/Red Team, Term Sheet, DE-EN Bilingual, US/UK Legal Writing, englische Verträge nach deutschem Recht), `juristische-sprache-deutsch-als-zweitsprache` (Juristendeutsch, Bescheide, Fristen und Formulare für Nichtmuttersprachler)

Eine vollständige Übersicht aller Plugins und Rechtsgebiete steht in [`references/rechtsgebiete-uebersicht.md`](./references/rechtsgebiete-uebersicht.md). Die kompakte Plugin-Liste findest du im Abschnitt ["Was ist drin?"](#was-ist-drin) weiter oben.

## Verbindliche Zitierweise

Jeder Skill verweist auf [`references/zitierweise.md`](./references/zitierweise.md). Die Kernregeln in Kurzfassung:

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Kostenlose Quelle:** Wo möglich Link zu offizieller Datenbank oder frei zugänglichem Volltext ergänzen; Datenbankkürzel wie BeckRS nicht ausdenken.
- **Literatur:** Kommentare, Bücher und Aufsätze nur zitieren, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert. Keine Blindzitate.

Pflicht: Datum + Aktenzeichen + verifizierbare Fundstelle + Randnummer bei Rechtsprechung. Unverifizierte Rechtsprechung wird als Prüfbedarf markiert oder weggelassen.

### Methodenlehre und Zitierweise als zuschaltbare Plugins

Die Inhalte aus [`references/methodik-buergerliches-recht.md`](./references/methodik-buergerliches-recht.md) und [`references/zitierweise.md`](./references/zitierweise.md) liegen zusätzlich als zwei eigenständige, einzeln aktivierbare Plugins im Marketplace:

- [`methodenlehre-buergerliches-recht`](./methodenlehre-buergerliches-recht) — Gutachtenstil, Anspruchsgrundlagen-Reihenfolge, Auslegungskanones, Abwägung, Präzedenzarbeit, Generalklauseln und Rechtsfortbildung als reale Werkzeuge.
- [`rechtstheorie-rechtsphilosophie`](./rechtstheorie-rechtsphilosophie) — Rechtsbegriff, Kelsen-orientierte Normgeltung, Kompetenzketten, Gesetzesbindung, Demokratie, Systemkritik, Verwaltungsrealismus, Besitzdogmatik, Law-and-Economics, Hayek-Wissensproblem, spontane Ordnung und anti-dezisionistische Machtkritik.
- [`zitierweise-deutsches-recht`](./zitierweise-deutsches-recht) — Hauszitierweise mit Pinpoint-Randnummer, Rechtsprechungs-Verifikationsregel, BeckRS-Sperre und Literatur-Sperre ohne Nutzerquelle oder lizenzierten Live-Zugriff.

Beide Plugins enthalten die gleichen Inhalte wie die Referenzdateien, sind aber als Skill ausgeführt: Sobald sie in Cowork aktiviert sind, gilt die Methodik bzw. die Zitierweise als ausdrückliche Pflicht für jede Antwort — unabhängig davon, ob ein Rechtsgebietsplugin geladen ist.

Aktivierung in Cowork: `Customize → Skills → Persönliche Plugins → +` und das jeweilige Plugin hinzuschalten.

## Für Einsteiger: Schritt-für-Schritt-Anleitung

### Was brauche ich?

1. **Einen Claude-Account** (kostenlos oder Pro) – Registrierung unter https://claude.ai
2. **Claude Desktop** (empfohlen) oder **Claude Code** – Download: https://claude.com/download
3. **Für GUI-Installation:** ein einzelnes Plugin-ZIP aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). **Für Entwickler:** dieses Repository mit Git klonen.

### Installation in Claude Desktop (für absolute Einsteiger)

**Schritt 1: Claude Desktop installieren**

1. Gehe zu https://claude.com/download
2. Lade die Version für dein Betriebssystem herunter (Windows / Mac / Linux)
3. Installiere die Anwendung und melde dich mit deinem Claude-Account an

**Schritt 2: Plugin-ZIP herunterladen**

1. Öffne den [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest).
2. Lade **ein einzelnes Plugin-ZIP** herunter, z. B. `arbeitsrecht.zip`, `vertragsrecht.zip` oder `liquiditaetsplanung.zip`.
3. Auf dem Mac darauf achten: die ZIP nicht entpacken; falls Safari sie automatisch entpackt, erneut als ZIP laden oder die Safari-Auto-Entpackung deaktivieren.

**Schritt 3: Skills in Claude Desktop aktivieren**

1. Öffne Claude Desktop
2. Klicke auf das Zahnrad-Symbol ⚙️ (Einstellungen) oben rechts
3. Gehe zu **Capabilities** (Funktionen)
4. Aktiviere **Code execution** und **Skills**

**Schritt 4: Einen Skill hochladen**

1. In den Einstellungen: gehe zu **Skills / Plugins**.
2. Öffne **Personal plugins / Persönliche Plugins**.
3. Klicke auf **+** und wähle **Upload from .zip** bzw. **Create → Upload plugin**.
4. Wähle das einzelne Plugin-ZIP aus, z. B. `arbeitsrecht.zip` oder `vertragsrecht.zip`.
5. Bestätige und starte danach eine neue Konversation.

**Schritt 5: Skill verwenden**

1. Starte einen neuen Chat in Claude Desktop
2. Der Skill wird automatisch erkannt, wenn du relevante Fragen stellst
3. Beispiel: "Erstelle mir einen Entwurf für eine ordentliche Kündigung nach § 622 BGB"

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

**F: Kostet Claude Geld?**
A: Es gibt einen kostenlosen Plan mit Limits. Für intensive Nutzung empfiehlt sich Claude Pro (ca. 20 $/Monat). Details: https://claude.ai/pricing

**F: Kann ich die Skills in meiner Kanzlei-Software nutzen?**
A: Derzeit funktionieren Skills nur in Claude Desktop, Claude Code und über die API. Direkte Integration in Kanzleisoftware erfordert Eigenentwicklung.

**F: Sind die Skills DSGVO-konform?**
A: Das hängt von Ihrer Nutzung ab. Anthropic ist DSGVO-zertifiziert, aber Sie müssen sicherstellen, dass Sie keine Mandantendaten ohne AVV hochladen. Siehe: https://www.anthropic.com/legal/privacy

**F: Kann ich die Skills anpassen?**
A: Ja. Alle Skills sind Open Source (Apache-2.0 OR MIT, nach Wahl der Nutzerin / des Nutzers). Sie können sie nach Belieben anpassen – siehe [`CONTRIBUTING.md`](CONTRIBUTING.md).

**F: Was mache ich, wenn ein Skill nicht funktioniert?**
A: Öffnen Sie einen Issue auf GitHub oder schauen Sie in die Skill-Datei – oft sind Abhängigkeiten oder Formate dokumentiert.

**F: Wie zuverlässig sind die Rechtszitate?**
A: **Nicht sehr**. LLMs erfinden oft Zitate. Rechtsprechung darf nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei/amtlich oder per lizenziertem Live-Zugriff verifizierter Quelle ausgegeben werden. Kommentar-, Aufsatz- und BeckRS-Blindzitate sind gesperrt.

## Hinweise zur Nutzung

⚠️ **Bitte beachten Sie:**

1. **Übersetzungsarbeit**: Diese Skills sind eine **KI-gestützte Übersetzung und Anpassung** der englischsprachigen "claude-for-legal"-Skills von Anthropic. Sie wurden für das deutsche Rechtssystem adaptiert, aber **nicht von Juristen final geprüft**.
2. **Alle Angaben ohne Gewähr**: Die Skills können Fehler, Ungenauigkeiten oder veraltete Rechtsinformationen enthalten. Eine **eigenständige Prüfung** aller Ausgaben ist zwingend erforderlich.
3. **Kein Ersatz für anwaltliche Beratung**: Diese Werkzeuge liefern Vorlagen und Strukturierungshilfen für Juristinnen und Juristen – sie ersetzen **keine** fundierte anwaltliche Beratung oder Recherche.
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

Doppellizenziert unter **Apache License, Version 2.0** ODER **MIT License**, nach Wahl der Nutzerin / des Nutzers (`SPDX-License-Identifier: Apache-2.0 OR MIT`) – siehe [`LICENSE`](./LICENSE), [`LICENSE-APACHE`](./LICENSE-APACHE), [`LICENSE-MIT`](./LICENSE-MIT) und [`NOTICE`](./NOTICE).

Die ursprüngliche Vorlage `claude-for-legal` von Anthropic steht unter der MIT-Lizenz; diese Adaption erweitert, ersetzt und ergänzt die ursprünglichen Inhalte und wird unter dem oben genannten Doppellizenz-Modell veröffentlicht.

## Mitwirken

Beiträge willkommen – siehe [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## English Summary

This repository provides a large German-law plugin and skill collection for Claude, Codex and similar AI workflows. The plugins are structured as practical legal workbenches: they help read messy files, build checklists, draft letters and pleadings, review contracts, prepare tables, track deadlines and keep legal reasoning tied to statutes and verifiable case law.

The focus is German legal practice: civil law, labour law, tax, insolvency, corporate, tenancy and WEG, family, inheritance, social law, public law, criminal defence, data protection, AI governance and many specialist business-law areas. Test case files are available separately as realistic document bundles and searchable Gesamt-PDFs.

The material is experimental and does not replace legal advice. Every output must be checked by a qualified human against current statutes, official materials and independently verifiable court decisions. Do not upload confidential client data unless your provider setup, professional duties and data-protection framework allow it.
