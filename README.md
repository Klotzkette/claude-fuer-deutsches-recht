# Claude – Deutsche rechtliche Fähigkeiten / German Legal Skills

> **Experimentelles Skill-Set** für die anwaltliche Praxis im deutschen Recht – Skills, Sub-Agenten, Workflows etc. als Anregung für Kanzlei-Arbeitsabläufe. Orientiert sich an der **deutschen Rechtspraxis** und am hohen Stellenwert von **Kommentaren und Aufsätzen**. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr – jede Nutzerin und jeder Nutzer kalibriert die Skills selbst für die eigene Praxis.
## Über dieses Repository

Dieses Repository ist eine **experimentelle Plugin- und Skill-Sammlung für deutsches Recht** auf Basis der offenen „claude-for-legal"-Skills von Anthropic, vollständig ins Deutsche übertragen und an typische Arbeitsabläufe in Kanzleien, Rechtsabteilungen und bei Beratern angepasst. Die Struktur, Beispiele und Workflows sind inzwischen **für die deutsche Rechtspraxis überarbeitet und im Alltagseinsatz erprobt**, sie bleiben aber bewusst als Experiment gekennzeichnet: Es handelt sich **nicht** um ein geprüftes Produkt, sondern um eine technische Spielwiese zum Ausprobieren, Anpassen und Weiterentwickeln.

Ziel ist es, zu zeigen, wie sich Plugins und Skills für Arbeitsrecht, Gesellschaftsrecht, Insolvenzrecht (inklusive Liquiditätsplanung und Fortbestehensprognose), Datenschutzrecht, Prozessrecht, gewerblichen Rechtsschutz, Produkt- und Regulierungsrecht u. a. so strukturieren lassen, dass sie sich an der in Deutschland üblichen Methodik (Anspruchsgrundlagen, Prüfungsaufbau, Kommentarliteratur, Rechtsprechungszitate im BGH-Stil) orientieren. Die Inhalte dienen ausschließlich als **Anregung für eigene Kanzlei- oder Inhouse-Plugins und -Skills**: Sie sollen zeigen, welche Prompts, Rollenbeschreibungen und Workflows in der Praxis hilfreich sein können – jede Nutzerin und jeder Nutzer passt sie an die eigenen Mandate, Branchen, Tools und Compliance-Vorgaben an.

### Bitte mit-testen und Feedback geben

Die Skills sind inzwischen deutlich verbessert und in verschiedenen Konstellationen getestet worden, können aber weiterhin Fehler, Lücken oder veraltete Rechtsstände enthalten. Deshalb:

- Nutzt die Skills aktiv im **Testbetrieb** (ohne echte Mandatsgeheimnisse) und schaut, wie gut sie zu euren Fällen, Kommentaren und Kanzleiprozessen passen.
- Gebt **Rückmeldungen**, eröffnet **Issues**, formuliert Verbesserungsvorschläge und schickt gerne **Pull Requests** mit eigenen Anpassungen, zusätzlichen Rechtsgebieten oder Praxis-Workflows.
- Passt die Beispiele an eure eigene **Zitierweise**, eure bevorzugten Standardkommentare und eure internen Vorgaben zu Berufsrecht, Datenschutz, KI-Governance und Mandatsgeheimnis an.

### Haftung, Berufsrecht, Datenschutz & KI-Recht

Dieses Repository trifft **keine Aussage** zur Zulässigkeit eines Einsatzes im konkreten Mandat oder Unternehmen – insbesondere nicht zu §§ 203, 204 StGB, § 43e BRAO, § 2 BORA, § 53, § 97, § 160a StPO, DSGVO / BDSG (inkl. Drittlandtransfer), US-Cloud-Act / FISA, der KI-VO (VO (EU) 2024/1689) oder sonstigen berufsrechtlichen, datenschutzrechtlichen und regulatorischen Vorgaben. Ob und wie ihr diese Beispiele produktiv nutzen dürft, müsst ihr **eigenverantwortlich** prüfen und in eure bestehende Governance (Mandatsgeheimnis, AVV, TOMs, KI-Richtlinien, Betriebsvereinbarungen etc.) integrieren.

## Überblick

| Kennzahl | Wert |
|---|---|
| **Plugins** | 98 |
| **Skills (SKILL.md)** | über 1600 |
| **Testakten** | 43 |
| **Fachanwalts-/-anwältinnen-Profile** | 23 |
| **Letzter Release** | [v9.0.0](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/v9.0.0) |
| **Marketplace-Definition** | [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) |

> 🧪 **Übrigens — es gibt auch sehr schöne Testakten.** Im Verzeichnis [`testakten/`](./testakten) liegen mehrere umfangreiche, fiktive Mandatsakten mit echten PDFs, Excel-Tabellen, Word-Entwürfen und handschriftlichen Notizen — bewusst unstrukturiert benannt wie ein realer Datenraum, damit sich die Plugins an echten Mandaten ausprobieren lassen. Details und Direkt-Downloads im [Testakten-README](./testakten/README.md).

### Inhaltliche Cluster

- **Rechtsgebiete (materiell):** Arbeitsrecht, Mietrecht (Wohn-/Gewerbe), Erbrecht, Familienrecht, Sozialrecht, Strafrecht, Verwaltungsrecht (inkl. Energieanlagen-BImSchG-Verfahren und Energietrassen-Planfeststellung), Steuerrecht, Insolvenzrecht inkl. StaRUG, Gesellschaftsrecht, Vertragsrecht, Markenrecht (inkl. Luxus-Fashion + USPTO/Lanham Act), Urheberrecht, Wettbewerbsrecht, Kartellrecht, Datenschutzrecht, IT-Recht, Bank- und Kapitalmarktrecht, Bau- und Architektenrecht, Verkehrsrecht, Medizinrecht, Migrationsrecht, Internationales Recht, Europarecht, Energierecht, Zwangsvollstreckung.
- **Mechanik-Prüfer:** `subsumtions-pruefer` (generischer Subsumtions-Workflow DE + EU), `bereicherungs-und-anfechtungsrecht-pruefer` (§§ 812 ff. BGB + AnfG + InsO-Anfechtung), `ki-vo-ai-act-pruefer` (Verordnung (EU) 2024/1689 mit Anbieter/Betreiber-Entscheidungsbaum, Art. 5/6/25/51 ff.).
- **Werkstatt- und Lehr-Plugins:**
  - `legistik-werkstatt` — komplette Gesetzgebungs-Werkstatt für Bundes- und Landesministerien (Referentenentwurf Arial-Hausstil, BT-Drucksache Times+Sperrsatz, Vorblatt A–F, Synopse, Lesefassung, Kabinettsmappe, Formulierungshilfe). DOCX/PDF im HdR-Layout.
  - `urteilsbauer-relationsmacher` — Urteils- und Beschluss-Werkstatt für Amts-, Land- und Familienrichter plus Rechtspfleger. Vollrelation (Sachbericht/Zulässigkeit/Schlüssigkeit/Erheblichkeit/Replik/Beweis/Tenorierung/Nebenentscheidungen/Selbstkontrolle) **und** Kurzrelation Praxisstandard mit Wahlfrage am Anfang. Rendert Urteile, Versäumnisurteile und Beschlüsse als DOCX im offiziellen Gerichtslayout nach § 313 ZPO. Inkl. Schulungsakte „Solis Vision X Smartglasses" (CISG, kollidierende AGB CH/EU, Incoterm FOB Galway, DSGVO als Eingriffsnorm, Testkauf 1577 EUR).
  - `hausarbeitenmacher` — didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten im Jurastudium. Führt sokratisch durch Zivilrecht, Öffentliches Recht und Strafrecht mit Ausflügen in Europarecht und Rechtstheorie. Fragt zu Beginn nach der Lehrkraft und entwickelt eine Adressaten-Strategie **ohne Schleimerei**. Strikt lernfördernd: kein Copy-Paste-Output, sondern Fragen, Strukturen, Methodenhinweise, Zitierweise. 22 Skills von Aufgabenstellung-Erfassen über Gutachtenstil und Methodenlehre bis Selbstkontrolle vor Abgabe.
- **Workflow-Pakete:** Wandeldarlehen-Lebenszyklus (Erstellung, Beurkundung, Wandlung, Cap-Table, Notar), Kündigungsschutzklage Selbsthilfe (Laie/Anwalt, Schriftsätze, Sprechzettel, Vergleich), Entfristungsklage TzBfG (Schriftform, elektronische Signatur), KI-Richtlinie für Kanzleien, Schriftform-/Textform-Organisator, Krisenfrüherkennung StaRUG, Liquiditätsplanung, Fortbestehensprognose.
- **Querschnitt:** Aktenauszug Gerichtsverfahren, Mandantenanfragen-Assistent, Arbeitszeugnis-Analyse (Ampelsystem), Email-Umformulierer berufsrechtskonform, Zitierweise im BGH-Stil, Fachanwaltschafts-Übersicht.

> ⚠️ **Vorsicht: hiermit bitte nicht mogeln im Studium.**
> Die Vollrelation, der Urteilsentwurf, der Hausarbeits- und Seminararbeits-Output sowie alle Schulungsakten sind **Trainings-, Praxis- und Lernwerkzeuge** für Studierende, Referendare/-innen, Assessoren/-innen, Berufsrichter/-innen, Tutor/-innen und Lehrkräfte. Sie sind ausdrücklich **nicht** dafür gedacht, in Hausarbeiten, Seminararbeiten, Klausuren, Aktenvorträgen oder im juristischen Vorbereitungsdienst (Z-, S-, V-, A-Klausur, mündliche Prüfung) als eigene Leistung ausgegeben zu werden. Das wäre ein Täuschungsversuch im Sinne der jeweiligen universitären Prüfungsordnung bzw. § 14 JAG NRW / § 12 JAPO Bayern / vergleichbarer Vorschriften der anderen Länder und kann zum Nichtbestehen, zur Aberkennung der Prüfung oder zu disziplinarrechtlichen Konsequenzen führen. Wer eine Relation, eine Hausarbeit oder ein Urteil üben will: zuerst selbst schreiben, danach mit dem Plugin abgleichen.

Die vollständige Plugin-Liste findest du in [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) und im Abschnitt [Was ist drin?](#was-ist-drin).

## Quickstart

```bash
# Marketplace im Claude-Code-CLI hinzufügen
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install <plugin-name>@claude-fuer-deutsches-recht
```

Alternativ: über die Claude-Desktop-GUI unter **Customize → Skills** → ZIP aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) hochladen. Schritt-für-Schritt unter [Schnellstart](#schnellstart) und [Für Einsteiger](#für-einsteiger-schritt-für-schritt-anleitung).

## 🚨 KEINE Aussage über Berufsrecht, Datenschutz, KI-VO oder Beschlagnahmeverbote

**Lesen, bevor irgendetwas davon eingesetzt wird.** Dieses Repository ist ausschließlich ein technisches Experiment. Es trifft **keinerlei Aussage** darüber, ob der Einsatz dieser Skills in einer konkreten Praxisumgebung berufs-, datenschutz- oder KI-rechtlich zulässig ist. Alle nachstehenden Fragen muss **jede Nutzerin und jeder Nutzer in eigener Verantwortung** vor der ersten Nutzung prüfen – das Repository, seine Autorin / sein Autor und alle Mitwirkenden übernehmen dafür keinerlei Verantwortung oder Haftung:

- **Strafrechtliches Mandatsgeheimnis – §§ 203, 204 StGB.** Die Skills sagen nichts darüber aus, ob ein konkreter Einsatz mit dem strafbewehrten Geheimnisschutz des § 203 StGB (Verletzung von Privatgeheimnissen) und § 204 StGB (Verwertung fremder Geheimnisse) vereinbar ist – auch nicht in der Variante § 203 Abs. 3, 4 StGB (mitwirkende Personen, sonstige Stellen).
- **Berufsrecht – § 43e BRAO, § 2 BORA, § 53 StPO.** Es wird **nicht** geprüft, ob der Einsatz mit § 43e BRAO (Inanspruchnahme von Dienstleistern, insbesondere Cloud/KI), § 2 BORA (Verschwiegenheit), den Zeugnisverweigerungsrechten nach § 53 StPO und den Beschlagnahmeverboten nach § 97 StPO vereinbar ist. Gleiches gilt sinngemäß für andere **freie Berufe** mit eigenem Berufsrecht (StBerG für Steuerberater:innen, WPO für Wirtschaftsprüfer:innen, ÄrztInnen, Notar:innen, Patentanwält:innen u. a.).
- **Datenschutz – DSGVO, BDSG.** Es wird **nicht** beurteilt, ob die Verarbeitung personenbezogener Daten DSGVO-konform ist, ob eine ausreichende **Rechtsgrundlage** (Art. 6, 9 DSGVO) vorliegt, ob ein **Auftragsverarbeitungsvertrag** nach Art. 28 DSGVO geschlossen werden muss, ob eine **Datenschutz-Folgenabschätzung** (Art. 35 DSGVO) erforderlich ist oder ob die **Informationspflichten** nach Art. 13, 14 DSGVO erfüllt sind.
- **Drittlandtransfer – USA / Kapitel V DSGVO.** Es wird **keine** Aussage darüber getroffen, ob ein Datentransfer in die USA oder ein anderes Drittland nach Art. 44 ff. DSGVO zulässig ist, ob das **EU-US Data Privacy Framework** einschlägig ist, ob **Standardvertragsklauseln** (SCC) oder ein **Transfer Impact Assessment** (TIA) genügen – oder ob der US Cloud Act, FISA § 702 und Executive Order 12333 dem konkreten Einsatz im Sinne von Schrems II (EuGH, Urt. v. 16.07.2020 – C-311/18) entgegenstehen.
- **KI-Verordnung (KI-VO / EU AI Act, VO (EU) 2024/1689).** Es wird **nicht** entschieden, ob der Einsatz unter eine der Hochrisiko-Kategorien nach **Art. 6 KI-VO** in Verbindung mit **Anhang III KI-VO** fällt (insbesondere Zugang zur Justiz, Strafverfolgung, demokratische Prozesse), ob **Transparenzpflichten** nach Art. 50 KI-VO greifen, ob es sich um ein **General-Purpose-AI-Modell** nach Art. 51 ff. KI-VO handelt und welche **Pflichten als Betreiber** (Art. 26 KI-VO) zu erfüllen sind.
- **Beschlagnahmeverbote und auslandsrechtliche Zugriffe.** Es wird nicht geprüft, ob Eingabedaten und Modellantworten gegen Beschlagnahme nach **§§ 97, 160a StPO**, gegen **US Cloud Act**, **FISA § 702**, **CLOUD Act warrants**, **PATRIOT Act § 215** oder sonstige extraterritoriale Zugriffsbefugnisse hinreichend geschützt sind. Dafür ist die jeweilige Nutzerin / der jeweilige Nutzer allein verantwortlich.
- **Zugang, Auftragsverarbeitung, Hosting.** Wie der API-Zugang zum Modell beschafft wird (Anthropic direkt, AWS Bedrock, Google Vertex, eigenes Hosting), ob mit dem Anbieter ein **Auftragsverarbeitungsvertrag** geschlossen wird, ob ein **berufsrechtskonformer Cloud-Vertrag** vorliegt und ob die Anforderungen an die Verschwiegenheit / Mandatsgeheimnis-Header und Datenflusskontrolle in der konkreten Deployment-Konstellation eingehalten sind, bleibt vollständig in der **Eigenverantwortung der Nutzerin / des Nutzers**.

## Wieso überhaupt ein Zwischenanbieter (Stand Mai 2026)

Anwältinnen und Anwälte sind nach § 203 StGB und § 43a BRAO zur Verschwiegenheit verpflichtet. Wer Mandantendaten in Claude eintippt, gibt sie technisch an Anthropic in den USA weiter — zulässig ist das nur, wenn dieser Empfänger sich vorher schriftlich zur Verschwiegenheit verpflichtet hat (§ 203 Abs. 4 StGB; § 43e BRAO). Anthropic unterschreibt eine solche Erklärung Stand Mai 2026 **nicht**. Bis sich das ändert, führt der Weg über einen deutschen Zwischenanbieter, der § 203 vertraglich zusagt — etwa Langdock oder einen vergleichbaren Anbieter ([nextAIM zu § 203-LLM-Hosting](https://www.nextaim.de/llm-hosting-203/); [anymize.ai zu Anonymisierung und EU-Servern](https://anymize.ai/blog/eu-server-keine-firewall-anonymisierung-ki); [Langdock Trust Center](https://trust.langdock.com/resources)).

Die nachstehende Anleitung beschreibt den vollständigen Einrichtungsweg — vom Vertrag bis zur Funktionsprüfung. Die Feldnamen können je nach App-Version leicht abweichen; im Zweifel mit Dummy-Daten vortesten.

### Vorbereitung beim Anbieter

**Schritt 1 — Anbieter wählen und Vertrag unterschreiben.** Anbieter mit § 203-Zusatzvereinbarung wählen, Vereinbarung unterschreiben, in die Akte legen.

**Schritt 2 — Beim Anbieter einloggen.** Browser öffnen, Anbieterseite aufrufen, Konto-Login.

**Schritt 3 — Zum API-Bereich wechseln.** Im Anbieter-Dashboard auf Profilbild oder Zahnrad klicken, Punkt „API Keys“ (manchmal „Tokens“ oder „Developer“) öffnen ([Langdock API Introduction](https://docs.langdock.com/api-endpoints/api-introduction)).

**Schritt 4 — Neuen Schlüssel anlegen.** Auf „Create new key“ / „Neuen Schlüssel erstellen“ klicken.

**Schritt 5 — Namen vergeben.** Sprechenden Namen eintragen, etwa „Claude-Cowork-Kanzlei-PC“.

**Schritt 6 — Schlüssel kopieren.** Den langen Zeichenstring (beginnt meist mit `sk-…`) **einmal** anzeigen lassen und sofort in den Passwort-Manager kopieren — er wird später nicht mehr im Klartext angezeigt.

**Schritt 7 — Adresse der Schnittstelle notieren.** In der Hilfe des Anbieters die „Anthropic-kompatible Base URL“ suchen, Muster `https://api.<anbieter>.de/anthropic`, mitkopieren ([BentoML zur Anthropic-kompatiblen API](https://bentoml.com/llm/model-interaction/anthropic-compatible-api)).

**Schritt 8 — Modellnamen notieren.** Im Modellkatalog des Anbieters den genauen Namen für Claude 4.7 Opus oder Sonnet aufschreiben (etwa `claude-sonnet-4-7-…`).

### Schlüssel in die Cowork-App einhängen

**Schritt 9 — Claude-App aktualisieren.** Claude Desktop öffnen, „Auf Updates prüfen“, neu starten.

**Schritt 10 — Abmelden.** Oben rechts auf das Profil klicken, „Log out“ wählen.

**Schritt 11 — Einstellungs-Dialog öffnen.** Menüleiste: „Menu“ → „Developer“ → „Configure Third-Party Inference“. Falls der Eintrag fehlt oder ausgegraut ist: „Help“ → „Troubleshooting“ → „Enable Developer Mode“ ([Product Compass zu Cowork-3P-LLM](https://www.productcompass.pm/p/cowork-on-3p-any-llm)).

**Schritt 12 — Verbindungsart wählen.** Feld „Connection“ auf „Gateway“ stellen.

**Schritt 13 — Adresse einfügen.** In „Gateway base URL“ die in Schritt 7 notierte Adresse einfügen.

**Schritt 14 — Schlüssel einfügen.** In „Gateway API key“ den in Schritt 6 kopierten Schlüssel einfügen (komplett, ohne Leerzeichen am Anfang oder Ende).

**Schritt 15 — Anmelde-Verfahren wählen.** Im Feld „Gateway auth scheme“ zuerst „x-api-key“ auswählen; bei Fehler „Invalid API key“ später auf „Authorization: Bearer“ umschalten.

**Schritt 16 — Erlaubte Verbindungen eintragen.** In „Allowed egress hosts“ nur die Domain des Anbieters eintragen, etwa `api.<anbieter>.de`, sonst nichts.

**Schritt 17 — Speichern.** „Apply locally“ anklicken.

**Schritt 18 — App neu starten.** „Relaunch now“ anklicken und warten, bis die App wieder oben ist.

**Schritt 19 — Über Gateway einloggen.** Im Login-Fenster nicht „Continue with Anthropic“ wählen, sondern „Continue with Gateway“.

**Schritt 20 — Modell auswählen.** Oben im Chat das Modell aufklappen und Claude 4.7 Opus oder Sonnet (Schreibweise wie in Schritt 8) wählen.

### Falls die Felder im Menü nicht greifen

**Schritt 21 — Mac über Terminal.** Terminal öffnen und nacheinander eingeben:

```
launchctl setenv ANTHROPIC_BASE_URL https://api.<anbieter>.de/anthropic
launchctl setenv ANTHROPIC_AUTH_TOKEN <Ihr-Schluessel>
launchctl setenv ANTHROPIC_API_KEY ""
```

Danach Cmd+Q und Claude wieder öffnen ([OpenAI-Hub zur Drittanbieter-Anbindung](https://www.openai-hub.com/news/203); [Fazm zur Anthropic-Base-URL-Konfiguration](https://fazm.ai/blog/route-claude-api-through-custom-endpoint-anthropic-base-url)).

**Schritt 22 — Windows 11 über Systemeinstellungen.** „Systemsteuerung → System → Erweiterte Systemeinstellungen → Umgebungsvariablen“. Drei neue Benutzervariablen anlegen: `ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_API_KEY` (letzte leer lassen). Ab- und neu anmelden, dann Claude starten ([Claude-Code-Doku zu Environment-Variablen](https://code.claude.com/docs/en/env-vars)).

### Funktionsprüfung

**Schritt 23 — Test-Anfrage.** Einen harmlosen Satz an Claude schicken („Sag Hallo“).

**Schritt 24 — Im Anbieter-Konto prüfen.** Im Dashboard des Anbieters unter „Logs“ muss die Anfrage erscheinen.

**Schritt 25 — Im Anthropic-Konto prüfen.** Im alten Anthropic-Konto darf **nichts** auftauchen.

**Schritt 26 — Verbindungen prüfen.** Mit Little Snitch (Mac) oder Windows-Firewall kontrollieren, dass die App nur die Anbieter-Adresse anspricht.

**Schritt 27 — Telemetrie aus.** In den App-Einstellungen Fehlerberichte und Nutzungsdaten ausschalten.

**Schritt 28 — Dokumentieren.** Anbieter, Adresse, Modell, Datum und § 203-Schreiben in die Compliance-Akte.

### Hinweis

Stand Mai 2026 funktioniert dieser Weg nur über einen Zwischenanbieter. Sobald Anthropic selbst eine § 203-Vereinbarung anbietet, wäre der Umweg entbehrlich. Die Feldbezeichnungen können je nach App-Version leicht abweichen; ohne Gewähr, im Zweifel vorab mit Dummy-Daten testen.

**Worum es hier geht.** Dieses Repository ist eine **technische Spielwiese**, die zeigt, was mit Claude Code und Plugin-Skills im Kontext deutschen Rechts überhaupt **technisch machbar** ist. Es geht **nicht** darum, eine produktiv einsetzbare, rechtskonforme Lösung anzubieten. Jede einzelne Nutzerin und jeder einzelne Nutzer prüft selbst und in eigener Verantwortung, ob, wie und unter welchen Schutzmaßnahmen ein Einsatz im konkreten Mandat oder Berufsumfeld zulässig ist – inklusive Mandatsgeheimnis, Datenschutz, Zeugnisverweigerungsrecht und Beschlagnahmeschutz, unabhängig von der einschlägigen Rechtsordnung.

> ⚠️ **WICHTIGER HINWEIS**
>
> Diese Skills sind eine **KI-gestützte Übersetzung und Adaption** der ursprünglichen „claude-for-legal"-Skills von Anthropic, angepasst an deutsches Recht.
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
> - eine Randnummer, ein Aktenzeichen oder ein Kommentarbeleg im Einzelfall unzutreffend ist,
> - eine Behandlung für eine bestimmte Konstellation zu generisch oder zu kanzleitypisch ist.
>
> **In diesem Fall bitte nicht auf die Autorin / den Autor „dreinschlagen".** Forken, anpassen, einen Pull Request einreichen oder einen Issue öffnen – das ist ausdrücklich gewollt. Das Repository soll genau so weiterentwickelt werden: durch die Praxis derjenigen, die damit arbeiten.

Diese Sammlung lässt sich u. a. in Claude Code, Claude Desktop und vergleichbaren Skill-fähigen KI-Umgebungen einsetzen. Inspiriert von und adaptiert nach Anthropics offenem Projekt `claude-for-legal`, vollständig auf das deutsche Recht und die Arbeitsweise deutscher Kanzleien zugeschnitten.

## Was ist drin?

> 🧭 **Querschnitts-Plugins zum Mitladen:** Zwei Plugins liefern die methodische Grundlage, die in den anderen Plugins vorausgesetzt wird. Sie gehören in jede Konfiguration mit hinein, weil sie den deutschen Stil tragen:
>
> - [`methodenlehre-buergerliches-recht`](./methodenlehre-buergerliches-recht) — Methodenlehre und Falllösung im deutschen bürgerlichen Recht aus Anwaltsperspektive. Gutachtenstil, Anspruchsgrundlagen-Reihenfolge, Auslegung Wortlaut/Systematik/Historie/Telos ohne starre Rangfolge (pragmatische BGH-Praxis), unions- und verfassungskonforme Auslegung, Rechtsfortbildung als reales Werkzeug. Breaking Change in v3.0: umbenannt von `methodenlehre-deutsches-recht`.
> - [`zitierweise-deutsches-recht`](./zitierweise-deutsches-recht) — Hauszitierweise mit Pinpoint-Randnummer, Grüneberg/MüKo-Regel, BGH-Stil, Typografiestandards. Pflicht-Checkliste vor jeder Ausgabe.
>
> Beide Plugins sind in jedem Modus (Claude Code, Cowork, Desktop) einzeln zuschaltbar und greifen quer in alle Rechtsgebiets-Plugins ein. Wer mit dem Marketplace startet, sollte diese beiden zuerst aktivieren — alle anderen Skills referenzieren ihre Regeln (siehe [`references/methodik-buergerliches-recht.md`](./references/methodik-buergerliches-recht.md) und [`references/zitierweise.md`](./references/zitierweise.md)).

> 🧪 **Testakten zum Ausprobieren:** Im Ordner [`testakten/`](./testakten) liegen mehrere umfangreiche, fiktive Mandatsakten mit echten PDFs, Excel-Tabellen, Word-Entwürfen und Mandantennotizen — bewusst unstrukturiert benannt wie ein realer Datenraum. Eine Akte pro typischem Anwendungsfall: Fluggastrechte (Familie Bräutigam-Zaytuna), Betreuung (Frau Sauer, 87, Demenz; Schmalfeld, Kontodaten und verdächtige Verträge), Einfache/Leichte Sprache (juristischer Mandantenbrief), Sozialrecht (Herr Tannenberg, Rollstuhl-Ablehnung), Fortbestehensprognose (Paragrafix GmbH, Legal-AI-Startup Berlin-Moabit), Kanzlei-Lebenszyklus-Alltag plus die bestehende Insolvenzakte Edelholz Berlin. Jede Akte ist als eigenes ZIP am Release angehängt und wird **nicht** mit den Plugins ausgeliefert. Details und Direkt-Downloads im [Testakten-README](./testakten/README.md).

Plugins (in Claude-Code-Terminologie) für die wichtigsten Rechtsgebiete der deutschen Beratungspraxis, alphabetisch sortiert:

| Plugin | Beschreibung |
| --- | --- |
| [`aktenaufbereiter-strafrecht`](./aktenaufbereiter-strafrecht) | Aktenaufbereiter für die Strafverteidigung. Bringt große Strafakten in den Griff durch sechs Excel-fähige Übersichten (Personen, Zeitachse, Beweismittel, Vorwürfe, Schriftsätze, Anlagen). |
| [`aktenauszug-gerichtsverfahren`](./aktenauszug-gerichtsverfahren) | Strukturierter Aktenauszug für deutsche Gerichtsverfahren: Verfahrensidentifikation, Einleitungssatz, Zusammenfassung, Sachverhaltschronologie, Verfahrenschronologie, tabellarische Gegenüberstellung Parteivortrag/Beweismittel/Rechtsargumente. Alle Verfahrensarten (ZPO, StPO, VwGO, ArbGG, SGG). |
| [`anlagen-zu-schriftsaetzen`](./anlagen-zu-schriftsaetzen) | Zuordnung von Anlagen zu gerichtlichen Schriftsätzen. Sortiert PDF/Word/Excel nach Schriftsatz-Logik (Klage, Erwiderung, Replik, Duplik) und erstellt das Anlagenverzeichnis. |
| [`arbeitsrecht`](./arbeitsrecht) | Individual- und Kollektivarbeitsrecht – Kündigung, Aufhebungsvertrag, Abmahnung, Anhörung Betriebsrat, KSchG-Klage, internationale Entsendungen. |
| [`arbeitszeugnis-analyse`](./arbeitszeugnis-analyse) | Analyse deutscher Arbeitszeugnisse nach Ampelsystem (Rot/Orange/Grün). Erkennt den Geheimcode der Zeugnissprache, identifiziert notenrelevante Sätze und klassifiziert sie mit Interpretation der versteckten Bewertung. |
| [`aussenwirtschaft-zoll-sanktionen`](./aussenwirtschaft-zoll-sanktionen) | Freistehendes Außenwirtschafts-, Sanktions-, Zoll- und CBAM-Plugin: Exportkontrolle, BAFA, Dual-Use, Embargos, TARIC, Ursprung, Zollwert, Verbrauchsteuer, Antidumping, AWV, AML/KYC, Ermittlungen und Krisenkommunikation. |
| [`bav-strategie-konzern`](./bav-strategie-konzern) | Strategische Beratung zur betrieblichen Altersversorgung in Konzernen: Pensionsmodelle alle fünf Durchführungswege CTA Pension Buyouts Drei-Stufen-Theorie Versorgungssystem-Harmonisierung internationale Benefits Restrukturierung DB-zu-DC im Düsseldorfer Boutique-Stil. |
| [`bereicherungs-und-anfechtungsrecht-pruefer`](./bereicherungs-und-anfechtungsrecht-pruefer) | Mechanisches Durchprüfen von Bereicherungsrecht SS 812 ff. BGB sowie Anfechtung nach AnfG und SS 129-147 InsO. Weichenstellung Rechtsgrund, Insolvenz, Vollstreckungstitel. Keine Rechtsberatung. |
| [`berufsrecht-ki-vertragspruefung`](./berufsrecht-ki-vertragspruefung) | Berufsrechtliche und strafrechtliche Vorprüfung von Verträgen mit privaten Legal-AI-Anbietern. Für Rechtsanwälte, Steuerberater, Wirtschaftsprüfer, Patentanwälte, Notare. §§ 43e BRAO, 62a StBerG, 50a WPO, 39c PAO, 26a BNotO i.V.m. § 203 StGB. Maßstab DAV-Stellungnahme Nr. 32/2025. Gutachten, Rückfragebrief, Klauselvorschläge. |
| [`betreuungsrecht`](./betreuungsrecht) | Skills für berufliche Betreuer nach BtOG und §§ 1814 ff. BGB (Reform 2023): Jahresbericht ans Betreuungsgericht (§ 1863 BGB), Vermögensverzeichnis und Rechnungslegung (§§ 1835, 1865 BGB), Genehmigungspflicht-Prüfung (§§ 1848 ff., 1831, 1832 BGB), Kontoanalyse und verdächtige Verträge in der Vermögenssorge. |
| [`common-law-kompass`](./common-law-kompass) | Freistehender Common-Law-Kompass für deutsche Wirtschaftsjuristen: UK/US-False-Friends, Vertragsbegriffe, Consideration, Suretyship, Indemnity, UCC, Precedent, Discovery und bilinguale Drafting-Reviews. |
| [`corporate-kanzlei`](./corporate-kanzlei) | Corporate/M&A-Plugin (46 Skills) für transaktionsstarke Kanzleien: Deal-Kommandocenter, Datenraum, Due Diligence, Tabellenreview, SPA/APA, Disclosure Schedules, Signing/Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, StaRUG, Insolvenzplan, PMI. |
| [`datenschutzrecht`](./datenschutzrecht) | DSGVO, BDSG, TDDDG, Auskunft, Datenpanne, AVV. |
| [`einfache-leichte-sprache-jura`](./einfache-leichte-sprache-jura) | Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Annäherung an einschlägige Standards, Zielgruppe klären, Rechtsinhalt sichern, schwere Wörter erklären und Qualitätsgate laufen lassen. |
| [`email-umformulierer-berufsrecht`](./email-umformulierer-berufsrecht) | Formuliert unfreundliche, emotionale oder unsachliche E-Mails in höfliche, sachliche und berufsrechtskonforme Texte um. Fokus auf BRAO/BORA, mit Modi für Steuerberater, Notare und allgemeine Korrespondenz. |
| [`energierecht`](./energierecht) | Freistehender Energierechts-Assistent für Stadtwerke, Energieversorger, Wärme, Netze, Vertrieb, Industriekunden, EEG/KWKG, Quartiere, E-Mobility, Wasserstoff, Verfahren, Transaktionen und Projektfinanzierung. |
| [`europarecht-kompass`](./europarecht-kompass) | Freistehender Europarecht-Kompass gegen deutsche Denkfehler: Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Charta, Grundfreiheiten, Beihilfen, Vorlageverfahren und EU-Drafting. |
| [`fachanwalt-agrarrecht`](./fachanwalt-agrarrecht) | Light-Touch-Plugin Fachanwalt für Agrarrecht. Höfeordnung, Anerbenrechte, Landpachtrecht (BGB §§ 581 ff.), GrdstVG, EU-GAP-Direktzahlungen, Cross-Compliance, Düngeverordnung, Pflanzenschutz, Tierschutz, Forstrecht. |
| [`fachanwalt-arbeitsrecht`](./fachanwalt-arbeitsrecht) | Light-Touch-Plugin Fachanwalt für Arbeitsrecht nach FAO § 10. KSchG Kündigungsschutzklage Frist drei Wochen § 4 KSchG, BetrVG Betriebsratsanhörung § 102, TzBfG Befristung, AGG. Schnittstellen zu `arbeitsrecht` und `kanzlei-cowork`. |
| [`fachanwalt-bank-kapitalmarktrecht`](./fachanwalt-bank-kapitalmarktrecht) | Light-Touch-Plugin Fachanwalt für Bank- und Kapitalmarktrecht. KWG, ZAG, WpHG, WpIG, MiFID II, MAR Marktmissbrauch, MiCAR, Verbraucherkredit, Vermögensanlage, Beratungshaftung. |
| [`fachanwalt-bau-architektenrecht`](./fachanwalt-bau-architektenrecht) | Light-Touch-Plugin Fachanwalt für Bau- und Architektenrecht. BGB Werkvertragsrecht §§ 650a ff. Bauvertrag, VOB/A, VOB/B, VOB/C, HOAI, Bauordnungsrecht der Länder. |
| [`fachanwalt-erbrecht`](./fachanwalt-erbrecht) | Light-Touch-Plugin Fachanwalt für Erbrecht. BGB Erbrecht §§ 1922 ff., Pflichtteil, Testament, Erbschein, Erbauseinandersetzung, Erbschaft- und Schenkungsteuer (ErbStG), EU-ErbVO. |
| [`fachanwalt-familienrecht`](./fachanwalt-familienrecht) | Light-Touch-Plugin Fachanwalt für Familienrecht. Familiengericht, FamFG, Scheidung, Sorgerecht, Umgangsrecht, Unterhalt, Zugewinn, Ehevertrag. |
| [`fachanwalt-gewerblicher-rechtsschutz`](./fachanwalt-gewerblicher-rechtsschutz) | Light-Touch-Plugin Fachanwalt für gewerblichen Rechtsschutz nach FAO § 14k. MarkenG, DesignG, UWG, PatG, GebrMG, UrhG-Bezüge. Markenanmeldung DPMA EUIPO, UWG-Abmahnung §§ 8 ff. UWG, Designverletzung, einstweilige Verfügung, lizenzanaloger Schadensersatz. |
| [`fachanwalt-handels-gesellschaftsrecht`](./fachanwalt-handels-gesellschaftsrecht) | Light-Touch-Plugin Fachanwalt für Handels- und Gesellschaftsrecht nach FAO § 14i. HGB, AktG, GmbHG, PartGG, UmwG. Geschäftsführerhaftung §§ 43 GmbHG, 93 AktG, Gesellschafterstreit Beschlussanfechtung, Handelsvertreterausgleich § 89b HGB, MoPeG-GbR seit 2024. |
| [`fachanwalt-insolvenz-sanierungsrecht`](./fachanwalt-insolvenz-sanierungsrecht) | Light-Touch-Plugin Fachanwalt für Insolvenz- und Sanierungsrecht nach FAO § 14. InsO Eröffnung, Antragspflicht § 15a, Gläubigerantrag § 14 InsO, StaRUG Restrukturierungsplan, Insolvenzanfechtung §§ 129 ff. InsO. Schnittstellen zu `insolvenzrecht` und `steuerrecht-anwalt-und-berater`. |
| [`fachanwalt-internationales-wirtschaftsrecht`](./fachanwalt-internationales-wirtschaftsrecht) | Light-Touch-Plugin Fachanwalt für Internationales Wirtschaftsrecht. CISG, Brüssel Ia, Rom I, Rom II, grenzüberschreitende Vertragspraxis, Schiedsverfahren (ICC, UNCITRAL), Investitionsschutz (ICSID), WTO, EU-Außenhandel, LkSG. |
| [`fachanwalt-it-recht`](./fachanwalt-it-recht) | Light-Touch-Plugin Fachanwalt für IT-Recht. SaaS-Verträge, Software-Lizenz, DSGVO/BDSG/TDDDG, TKG, NIS2, DDG, Open-Source-Compliance, Plattformhaftung (DSA, DMA), EU-KI-VO. |
| [`fachanwalt-medizinrecht`](./fachanwalt-medizinrecht) | Light-Touch-Plugin Fachanwalt für Medizinrecht. Arzthaftung §§ 630a ff. BGB, Patientenrechte, Vertragsarztrecht, Berufsrecht Ärzte und Heilberufe, SGB V, MPDG, Apothekenrecht. |
| [`fachanwalt-miet-wohnungseigentumsrecht`](./fachanwalt-miet-wohnungseigentumsrecht) | Light-Touch-Plugin Fachanwalt für Miet- und Wohnungseigentumsrecht nach FAO § 14e. BGB §§ 535 ff. Wohnraum- und Gewerberaummiete, Mieterhöhung §§ 558 ff., Kündigung §§ 543, 569, 573 BGB, WEG-Beschlussanfechtung § 44 WEG, BetrKV. |
| [`fachanwalt-migrationsrecht`](./fachanwalt-migrationsrecht) | Light-Touch-Plugin Fachanwalt für Migrationsrecht. AufenthG, AsylG, GFK, Dublin-VO, EU-Verfahrensrichtlinie, Qualifikations-RL, StAG Einbürgerung, Aufenthaltsverfestigung, Familiennachzug. Notfrist § 36 AsylG (eine Woche). |
| [`fachanwalt-sozialrecht`](./fachanwalt-sozialrecht) | Light-Touch-Plugin Fachanwalt für Sozialrecht nach FAO § 11. SGB I bis XII, Sozialgerichtsbarkeit SGG, Widerspruch § 84 SGG (Monatsfrist), Klage Sozialgericht § 87 SGG, Erwerbsminderungsrente, SGB II Bürgergeld-Bescheid. Schnittstellen zu `sozialrecht-kanzlei`. |
| [`fachanwalt-sportrecht`](./fachanwalt-sportrecht) | Light-Touch-Plugin Fachanwalt für Sportrecht. Verbandsrecht der Sportverbände (DFB, FIFA, UEFA, IOC, DOSB), CAS-Schiedsverfahren, Spielerverträge, Doping (WADA-Code, NADA), Sponsoring, Persönlichkeitsrechte Sportler, Veranstalterhaftung. |
| **Fachanwalt für Steuerrecht** (nicht separat) | ⚠️ Es gibt **kein** eigenes Light-Touch-Plugin `fachanwalt-steuerrecht`. Steuerrecht ist konsolidiert im Power-Plugin [`steuerrecht-anwalt-und-berater`](./steuerrecht-anwalt-und-berater). **Zweiteilung** der Skills: `anw-` für die gesamte Anwaltschaft im Steuerrecht (Fachanwältinnen und Fachanwälte inklusive — die FAO § 9-Voraussetzungen sind Anhang in `anw-orientierung`) und `stb-` für die Steuerberatung. Dieses Plugin enthält damit alle früheren `fachanwalt-steuerrecht`-Skills plus die Anwalts- und Steuerberater-Workflows. Hintergrund: Steuerrecht ist anders als die übrigen FAO-Felder zwischen Anwalt und Steuerberater eng verzahnt; ein gemeinsames Plugin vermeidet Doppelungen. |
| [`fachanwalt-strafrecht`](./fachanwalt-strafrecht) | Light-Touch-Plugin Fachanwalt für Strafrecht. StPO, StGB, Nebenstrafrecht. Strafverteidigung, Ermittlungsverfahren, Hauptverhandlung, Berufung, Revision, Verfassungsbeschwerde. Ergänzend zum Plugin `aktenaufbereiter-strafrecht`. |
| [`fachanwalt-transport-speditionsrecht`](./fachanwalt-transport-speditionsrecht) | Light-Touch-Plugin Fachanwalt für Transport- und Speditionsrecht. HGB §§ 407 ff. Frachtvertrag, §§ 425 ff. Haftung, §§ 453 ff. Speditionsvertrag, CMR, COTIF, Montrealer Übereinkommen, Haager Visby Regeln, ADSp. |
| [`fachanwalt-urheber-medienrecht`](./fachanwalt-urheber-medienrecht) | Light-Touch-Plugin Fachanwalt für Urheber- und Medienrecht. UrhG, VGG Verwertungsgesellschaften, KUG Recht am eigenen Bild, Presserecht, Persönlichkeitsrecht, Medienstaatsvertrag, InfoSoc-RL, DSM-RL. |
| [`fachanwalt-vergaberecht`](./fachanwalt-vergaberecht) | Light-Touch-Plugin Fachanwalt für Vergaberecht. GWB §§ 97 ff., VgV, UVgO, SektVO, KonzVgV, VOB/A, EU-Vergabe-RL, Nachprüfungsverfahren vor Vergabekammer und OLG-Vergabesenat. |
| [`fachanwalt-verkehrsrecht`](./fachanwalt-verkehrsrecht) | Light-Touch-Plugin Fachanwalt für Verkehrsrecht. StVG, StVO, PflVG, VVG-Bezüge. Verkehrsunfall, Personenschaden, Sachschaden, Bußgeld, Fahrerlaubnis, OWi-Verfahren, Verkehrsstrafrecht (§§ 315c, 316 StGB). |
| [`fachanwalt-versicherungsrecht`](./fachanwalt-versicherungsrecht) | Light-Touch-Plugin Fachanwalt für Versicherungsrecht. VVG, VAG, Berufsunfähigkeit, private Krankenversicherung, Lebens- und Rentenversicherung, Sachversicherung, Haftpflicht, D&O. |
| [`fachanwalt-verwaltungsrecht`](./fachanwalt-verwaltungsrecht) | Light-Touch-Plugin Fachanwalt für Verwaltungsrecht. VwGO, VwVfG (Bund/Länder), Anfechtungs- und Verpflichtungsklage, Eilrechtsschutz, Normenkontrolle, Polizei- und Ordnungsrecht. |
| [`fluggastrechte`](./fluggastrechte) | Fluggastrechte selber geltend machen — VO (EG) Nr. 261/2004 plus EuGH-Rechtsprechung. Tickets erfassen, Annullierung vs. Verspätung prüfen, außergewöhnliche Umstände, Distanz und Ausgleich berechnen, Forderungsschreiben, Mahnung, Klage zum Amtsgericht. Vollmacht Familie. Katalog Airline-Standardausreden. |
| [`forderungsmanagement-klagewerkstatt`](./forderungsmanagement-klagewerkstatt) | Generalisierter Klage-Assistent für Forderungsmanagement-Klagen mit eigenem Plugin-Generator. Lernlauf aus eigenen Mustern, Laufzeit-Skill und direkter Inkasso-Zahlungsklage-Ersteller mit Mahnvorlauf, Anspruchs-Gatekeeper, Gerichtsortprüfung und der Regel: nur klare, fällige und belegte Ansprüche einklagen. |
| [`fortbestehensprognose`](./fortbestehensprognose) | Fortbestehensprognose nach § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Prüfablauf Bilanzstatus, Annahmen, Plausibilisierung, 12-Monats-Liquidität. Sanierungsbausteine: harte Patronatserklärung, Comfortletter, Gesellschafterdarlehen mit Rangrücktritt, Stundung, Forderungsverzicht. IDW S 11, IDW S 6, StaRUG. 90-Prozent-Maßstab nach BGHZ 163, 134. |
| [`geldwaeschepraevention-aml-kyc`](./geldwaeschepraevention-aml-kyc) | Freistehendes Geldwäscheprävention-/AML-/KYC-Plugin: GwG-Risikoanalyse, Kundenprüfung, wirtschaftlich Berechtigte, PEP, Sanktionen, FIU/goAML, Transparenzregister, Monitoring, Schulung, Audit, Behördenverfahren und Remediation. |
| [`gesellschaftsgruender`](./gesellschaftsgruender) | Gründungsassistent für deutsche Gesellschaften. Führt von Rechtsformwahl GmbH UG GbR OHG KG GmbH und Co KG PartG mbB gGmbH eK über Gesellschaftsvertrag und Geschäftsführeranstellungsvertrag bis Notar Handelsregister Gewerbeamt Finanzamt Transparenzregister IHK Berufsgenossenschaft. MoPeG 2024 DiRUG Online-Gründung GwG TraFinG. Erste-100-Tage-Pflichten für Geschäftsführer. |
| [`gesellschaftsrecht`](./gesellschaftsrecht) | GmbH, AG, Personengesellschaften, M&A, Due Diligence, Gesellschafterbeschluss, Handelsregister. |
| [`gewerblicher-rechtsschutz`](./gewerblicher-rechtsschutz) | Marke, Design, Patent, Urheberrecht, UWG-Abmahnung. |
| [`grosskanzlei-corporate-ma`](./grosskanzlei-corporate-ma) | Freistehendes Big-Law-Corporate/M&A-Plugin mit Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, internem Tabellenreview, Liquiditätsvorschau, Insolvenzreifecheck, CP-Kalender, SPA/APA, W&I, Public M&A, Umwandlungsrecht, StaRUG/Insolvenzplan, Billing, XRechnung/ZUGFeRD, GoBD und Closing Bible. |
| [`hausarbeitenmacher`](./hausarbeitenmacher) | Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten im Jurastudium. Führt Studierende sokratisch durch die Lösung in Zivilrecht öffentlichem Recht Strafrecht mit Ausflügen in Europarecht und Rechtstheorie. Fragt zu Beginn nach der Lehrkraft und entwickelt Adressaten-Strategie ohne Schleimerei. Bei Seminararbeit Modus-Wechsel zum wissenschaftlichen Aufsatz mit eigener These. Strikt lernfördernd nicht zum Abschreiben. Behutsam-frech-wertschätzender Dialog-Stil am Rande. |
| [`immobilienrechtspraxis`](./immobilienrechtspraxis) | Werkzeuge für immobilienrechtliche Rechtsabteilungen — musterbasierte Vertragserstellung mit Klauselschutz, Vertragsprüfung, Übergabeprotokolle. |
| [`insolvenzforderungsanmeldungspruefung`](./insolvenzforderungsanmeldungspruefung) | Freistehende Insolvenzforderungsanmeldungsprüfung: Intake, § 174 InsO, Belegkette, Grund/Betrag/Rang, vbuH, Nachforderungen, Tabellenimport, Prüfungstermin, Bestreiten, Feststellung, Schuldnerwiderspruch und § 189-Nachlauf. |
| [`insolvenzplan-starug-planwerkstatt`](./insolvenzplan-starug-planwerkstatt) | Freistehende Insolvenzplan- und StaRUG-Planwerkstatt: Kaltstart, Sanierungskonzept, integrierte Planung, Vergleichsrechnung, Gruppen/Klassen, darstellender und gestaltender Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Planvollzug. |
| [`insolvenzrecht`](./insolvenzrecht) | Zahlungsunfähigkeit § 17 InsO (BGHZ 163, 134), zweistufige Überschuldungsprüfung § 19 InsO mit Fortbestehensprognose (IDW S 11), Antragspflicht § 15a InsO und Haftung wegen Insolvenzverschleppung, Gläubigerantrag § 14 InsO, gerichtsfähige Liquiditätsvorschau. |
| [`insolvenzverwaltung`](./insolvenzverwaltung) | Freistehendes Insolvenzverwaltungs-Cockpit aus IV-/Sachwalter-Sicht: Eröffnungsgutachten, Regelverfahren, Eigenverwaltung, Schutzschirm, Masse, Anfechtung, § 15b InsO, Forderungsprüfung, Insolvenzplan-/StaRUG-Planwerkstatt, § 208 InsO, Berichte, Schlussrechnung und Verteilung. |
| [`jurastudium`](./jurastudium) | Werkzeuge für Studium und Referendariat: Prüfungsgespräch nach AG-Tradition, Subsumtionslehre, Methodenlehre (Zivilrecht, Strafrecht, Öffentliches Recht), Rechtsgeschichte (röm. Recht/BGB-Genese, NS-Justiz/Radbruchsche Formel, SED-Unrecht, GG 1949, Unionsrecht), Lernstrategien, Tatbestände lernen, Lösungsschemata, Gutachtenstil, Klausurkorrektur, Lernplanung. Lernmodus, kein Antwortmodus. |
| [`jveg-kostenpruefer`](./jveg-kostenpruefer) | Freistehender JVEG-Kostenprüfer: Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen-/Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle. |
| [`kanzlei-allgemein`](./kanzlei-allgemein) | Kanzlei-Allgemein-Plugin mit edlem Cowork-Kommandocenter, Nachtblau/Silber/Orange-Look, Copilot, Mandatsannahme/GwG, KYC, PEP, Aktenanlage, Kontoblatt, Schreib-Canvas, Klage/Replik-Turbo, Vertragsentwurf, Rechtsprechungsrecherche, Handelsregisterabruf, beA, Fristen, Rechnung, Geschäftskonto, Bankmatching, XRechnung, UStVA und Simulation. |
| [`kanzlei-builder-hub`](./kanzlei-builder-hub) | Werkzeuge zum Bauen eigener kanzleiinterner Skills. |
| [`kanzlei-cowork`](./kanzlei-cowork) | Cowork-Assistent für die deutsche Anwaltskanzlei. Fristenbuch, Timesheet, Rechnungserstellung nach RVG, Versand-Vor-Check (PDF, beA, Signatur, Adressat, Anlagen), beA-Versand-Prüfung, Postein- und ausgang, Mandantenakte, Aktenbestandspflege, Honorar-Mahnwesen, Mandantenbrief-Vorlagen, Geburtstags- und Weihnachtskarten, Sekretariats-Tagesbrief. |
| [`kartellrecht-marktabgrenzung-pruefung`](./kartellrecht-marktabgrenzung-pruefung) | Hochspezialisierte kartellrechtliche Prüfinstanz für vorgelegte Marktabgrenzungen (eigenes Team, gegnerische Partei, Behörde). § 18 GWB, Art. 101 und Art. 102 AEUV, EU-Bekanntmachung Marktdefinition 2024. SSNIP-Test, Nachfrage-/Angebotssubstitution, räumlicher Markt, Evidenzbasierung, Konsistenzcheck, EuGH-Leitentscheidungen, Red Flags, alternative Marktdefinitionen, Marktbeherrschung. 24 Skills. |
| [`ki-governance`](./ki-governance) | EU-KI-VO, KI-Inventar, AIA, Vendor Review. |
| [`ki-richtlinie-kanzleien`](./ki-richtlinie-kanzleien) | Erstellt und pflegt eine berufsrechtskonforme KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen. 26 Skills zu BRAO, BORA, DSGVO, KI-Verordnung, Berufsrecht, Datenschutz, Halluzinations-Handhabung und Prompting. |
| [`ki-vo-ai-act-pruefer`](./ki-vo-ai-act-pruefer) | Vollständiger Mechanik-Workflow zur Verordnung (EU) 2024/1689 (KI-VO): KI-System-Definition, Rollen, Risikoklassen, Hochrisiko-Pflichten, GPAI-Modelle, Sanktionen. Kein Rechtsrat. |
| [`krisenfrueherkennung-starug`](./krisenfrueherkennung-starug) | Krisenfrüherkennung und Krisenmanagement nach StaRUG: Pflicht zum 24-Monats-Frühwarnsystem nach § 1 StaRUG, § 102 StaRUG Warnpflicht der Berater, Geschäftsführerhaftung, drohende Zahlungsunfähigkeit, integrierte Planung, Restrukturierungsplan und Stabilisierungsanordnung. |
| [`legistik-werkstatt`](./legistik-werkstatt) | Legistik-Werkstatt für Bundes- und Landesministerien. Vom politischen Auftrag über Normhierarchie Kompetenzprüfung Normenkartierung Terminologie zu Referentenentwurf Kabinettsmappe Formulierungshilfe Rechtsverordnung Satzung. Inkl. Begründung Synopse Lesefassung XML Folgenabschätzung Goldplating-Check und Schulungstrainings. Erzeugt am Ende DOCX und PDF im offiziellen HdR-Layout (Times New Roman BT-Drucksachen, Arial Referentenentwurf). |
| [`liquiditaetsplanung`](./liquiditaetsplanung) | Bündel-Plugin für die rollierende Liquiditätsplanung: 3-Wochen-Test § 17 InsO (BGH BGHZ 163, 134), 13/26/52-Wochen-Forecast mit Ampel, Fortführungsprognose IDW S 6/S 11 und insolvenzrechtliche Liquiditätsbilanz. Verweist auf die Skills in `steuerrecht-anwalt-und-berater` und `insolvenzrecht`. |
| [`mandantenanfragen-assistent`](./mandantenanfragen-assistent) | Assistent für Anwaltskanzleien zur Erstantwort auf Mandantenanfragen per E-Mail: dankt förmlich, übernimmt die Anrede aus der eingehenden E-Mail, nennt die telefonische Terminvergabe, bittet um Sachverhalt per E-Mail oder bietet eine Telefon-Transkription mit DSGVO-Einwilligungshinweis an. |
| [`markenrecht-fashion-luxus`](./markenrecht-fashion-luxus) | Markenrecht-Boutique für Luxus-Modehäuser - DPMA/EUIPO Alicante/USPTO Lanham Act via NYC-Korrespondenz, alle Markenarten (Wort/Bild/Slogan/Sound/Duft/3D/Position/Haptik/Anti-KI), Widerspruch, Löschung, Verletzung, Produktpiraterie, Selektivvertrieb. |
| [`memorandums-ersteller`](./memorandums-ersteller) | Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung: Sachverhalt mit Quellenreferenz, Rechtsfrage, rechtliche Würdigung, Ergebnis und Empfehlung. |
| [`methodenlehre-buergerliches-recht`](./methodenlehre-buergerliches-recht) | Methodenlehre und Falllösung im deutschen bürgerlichen Recht aus Anwaltsperspektive. Gutachtenstil, Anspruchsgrundlagen-Reihenfolge, Auslegung Wortlaut/Systematik/Historie/Telos pragmatisch ohne starre Rangfolge (BGH-Praxis), unions- und verfassungskonforme Auslegung, Rechtsfortbildung. Breaking Change in v3.0 umbenannt. |
| [`mietrecht`](./mietrecht) | Mietrecht für Mieter und Vermieter mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitätsstädte. Acht Skills: Datenerhebung, Mieterhöhungs-Widerspruch, Mietsenkungsverlangen, Nebenkostenprüfung, Mieteranfragen, Klageentwurf Amtsgericht. |
| [`mittelstand-corporate-ma`](./mittelstand-corporate-ma) | Freistehendes Corporate/M&A-Plugin für mittelständische Kanzleien mit Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, internem Tabellenreview, Liquiditätsvorschau, Insolvenzreifecheck, CP-Kalender, SPA/APA, W&I, Public M&A, Umwandlungsrecht, StaRUG/Insolvenzplan, Billing, XRechnung/ZUGFeRD, GoBD und Closing Bible. |
| [`nda-abgleich`](./nda-abgleich) | NDA-Verhandlungshilfe für die empfangende Seite. Modus A: Standard-Destillation aus 1–n NDAs. Modus B: Redlining gegen den eigenen Standard. |
| [`normenkontrolle-bauleitplanung`](./normenkontrolle-bauleitplanung) | Freistehendes Verwaltungsrecht-Plugin für die Prüfung und Anfechtung von Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften nach § 47 VwGO. Mandatsperspektive Antragstellervertretung. 18 Skills für vier Phasen: Mandatsaufnahme und Antragsbefugnis, Verfahrensprüfung (Aufstellung, Beteiligung, Umweltbericht, Planerhaltung), materielle Prüfung (Erforderlichkeit, Abwägungsgebot, Stellplatzsatzung BayBO, Immissionsschutz, Artenschutz, Anpassungsgebot) sowie Schriftsatz und mündliche Verhandlung beim BayVGH (Normenkontrollantrag, einstweilige Anordnung § 47 Abs. 6 VwGO). |
| [`patentrecherche`](./patentrecherche) | Patentrecherche für Patentanwälte – agentisch in Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE, USPTO. Stand der Technik, Neuheit (§ 3 PatG, Art. 54 EPÜ), erfinderische Tätigkeit (§ 4 PatG, Art. 56 EPÜ) im Problem-Solution-Approach, Freedom-to-Operate, CPC-/IPC-Klassifikation, INPADOC-Patentfamilie, Recherchebericht. |
| [`phishing-vorfall-pruefer`](./phishing-vorfall-pruefer) | Freistehender Prüfer für Online-Banking-Phishing: § 675u/§ 675v BGB, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Banklogs, Ombudsmann und Klage. |
| [`produktrecht`](./produktrecht) | Produktrecht, AGB, Impressum, PAngV, Marketing-Claims. |
| [`prozessrecht`](./prozessrecht) | Zivil-, Straf- und Verwaltungsprozess, Mahnverfahren, einstweilige Verfügung, Zwangsvollstreckung, Verkehrsunfall. Streitwertgrenzen ab 1.1.2026 angepasst (AG bis 10.000 € nach § 23 Nr. 1 GVG n.F.). |
| [`rechtsberatungsstelle`](./rechtsberatungsstelle) | Pro-Bono-Beratungsstellen, Mandantenakte, Mandantenbrief. |
| [`regulatorisches-recht`](./regulatorisches-recht) | Aufsichtsrecht, KWG, GwG, EnWG, TKG, Inkasso/RDG, UStVA, DORA-IKT-Vertragsprüfung. |
| [`schriftform-und-textform-bgb`](./schriftform-und-textform-bgb) | Workflow-Organisator zu Form-Erfordernissen im deutschen Zivilrecht: Schriftform § 126 BGB qES § 126a Textform § 126b Zugang § 130 BGB lernt aus BGH I ZR 202/25 Maklervertrag und BGH VIII ZR 159/23 Mietkündigung Klauselgenerator Mandantenmemos. |
| [`sozialrecht-kanzlei`](./sozialrecht-kanzlei) | Vollassistenz für die sozialrechtliche Kanzlei: Bescheidanalyse, Widerspruch, Klage zum Sozialgericht, Eilantrag, Akteneinsicht, Anlagenerstellung. Spezialisiert auf Bürgergeld (SGB II), SGB IX Schwerbehinderung, Pflege, Hilfsmittel (Rollstuhl, Hörhilfe, Vorlesekraft), Eingliederungshilfe, SGB VIII Schulbegleitung. Fristenbuch und PKH. |
| [`steuerrecht-anwalt-und-berater`](./steuerrecht-anwalt-und-berater) | Steuerberater und Fachanwalt für Steuerrecht: Bescheidanalyse, Einspruch nach AO, Klage zum Finanzgericht, Außenprüfung, Selbstanzeige § 371 AO, Verbindliche Auskunft, Akteneinsicht Steuerakte. BWA-/SuSa-/Bilanz-Krisenprüfung für Steuerberater. Skills mit Präfixen `anw-` (Anwalt), `fa-` (Fachanwalt), `stb-` (Steuerberater). |
| [`strafbefehl-verteidiger`](./strafbefehl-verteidiger) | Freistehender Strafbefehls-Verteidiger: Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung. |
| [`subsumtions-pruefer`](./subsumtions-pruefer) | Interaktiver Subsumtions-Workflow für deutsches Recht und Europarecht: Tatbestandsmerkmale zerlegen, Vier-Schritt-Schema je TBM, Beweisbedarf erfassen, Rechtsfolgen und Einreden prüfen. Ausgabe als Schriftsatz oder Memo. Keine Rechtsberatung. |
| [`tabellenreview-3d`](./tabellenreview-3d) | 3D-Tabellenreview als Würfel: Spaltenprompts pro Datenpunkt × Zeilenprompts pro Dokument × Arbeitsblatt-Perspektiven (Rollen, Adressaten). |
| [`umweltrecht`](./umweltrecht) | Freistehender Umweltrechts-Assistent für Emissionshandel, BImSchG, Störfall, Abfall/Circular Economy, Wasser, Boden, Naturschutz, UIG/IFG, Verfahren, Bußgeld, Schulung und Umwelt-Due-Diligence. |
| [`urteilsbauer-relationsmacher`](./urteilsbauer-relationsmacher) | Werkstatt-Plugin für Amts-, Land- und Familienrichter: Aktenintake, Relation (Voll- oder Kurzfassung mit Wahlfrage), Zulässigkeit, Anspruchsgrundlagen, CISG, kollidierende AGB, Incoterms, Beweiswürdigung mit Richter-Input, Tenor, Tatbestand, Entscheidungsgründe, Kosten, vorläufige Vollstreckbarkeit, Rechtsmittelbelehrung, Berufungs- und Revisionsfestigkeit, Beschlüsse, Familienspezifika sowie Renderer für DOCX und PDF im Gerichtslayout. Inklusive Schulungsakte Solis Vision X Smartglasses. |
| [`verfassungsrecht`](./verfassungsrecht) | Deutsches Verfassungsrecht unter dem Grundgesetz aus Sicht einer Spezialkanzlei. Rechtsprechungsgetrieben mit verpflichtender Live-Recherche auf bundesverfassungsgericht.de. Acht Skills für Gesetzgebungskompetenz, formelle und materielle Verfassungsmäßigkeit, Grundrechte und Verfassungsbeschwerde. |
| [`verkehr-infrastrukturrecht`](./verkehr-infrastrukturrecht) | Freistehender Assistent für Verkehrsplanung, Infrastrukturprojekte, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Sondernutzung, Parkraum, Wirtschaftsverkehr, Verkehrswende, Schulwegsicherheit, Förderung und Vergabe. |
| [`verkehrsowi-verteidiger`](./verkehrsowi-verteidiger) | Freistehender Verteidiger für Verkehrsordnungswidrigkeiten: Bußgeld, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol/Drogen, Messakte, Einspruch, Zeugenstrategie und Amtsgericht. |
| [`verlagsredaktion`](./verlagsredaktion) | Verlegerischer Redaktionsassistent. Modus A macht aus disparaten Inputs (Transkripte, PPT, Screenshots, Videos, Notizen) einen redaktionellen Text. Modus B redigiert vorhandene Texte. |
| [`vertragsausfueller`](./vertragsausfueller) | Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, Clean-Verträge erzeugen und Track Changes nur nach ausdrücklicher Nachfrage vorbereiten. |
| [`vertragsrecht`](./vertragsrecht) | NDA, SaaS-/MSA-Review, Lieferanten-AGB, Renewal-Tracking. |
| [`wandeldarlehen-lebenszyklus`](./wandeldarlehen-lebenszyklus) | Vollständiger Lebenszyklus eines Wandeldarlehens für GmbH und UG: Erstellung (bilingual/einsprachig), Beurkundungsprüfung, Wandelereignisse, Wandlungsberechnung, Cap-Table-Update, Gesellschafterbeschluss und Notar-Paket. |
| [`zitierweise-deutsches-recht`](./zitierweise-deutsches-recht) | Deutsche juristische Hauszitierweise als zuschaltbares Plugin. Rechtsprechung mit Datum, Aktenzeichen, Fundstelle, Randnummer. Kommentar- und Aufsatzzitate. |
| [`zwangsverwaltung-zvg`](./zwangsverwaltung-zvg) | Freistehendes ZVG-Cockpit für Zwangsverwaltung und Versteigerung: Bestellung, Beschlagnahme, Besitz, Mietverwaltung, Treuhandkonto, Berichte, § 155 ZVG-Verteilung, ZVG-Portal-Recherche, Bieterangebote und Versteigerungsteilnahme. |

Zusätzlich:
- [`verwaltete-agentenrezepte`](./verwaltete-agentenrezepte) – wiederverwendbare Vorlagen für Multi-Agent-Arbeitsabläufe (Aufsichts-Monitor, Gerichtskalender-Monitor, Verlängerungs-Monitor, Due-Diligence-Tabelle).
- [`references/zitierweise.md`](./references/zitierweise.md) – die deutsche Zitierweise (BGH-Stil), an der sich alle Skills orientieren.
- [`references/methodik-buergerliches-recht.md`](./references/methodik-buergerliches-recht.md) – Methodenlehre, Anspruchsgrundlagenreihenfolge, Beweislast, Fristen.

## Reifegrade der Plugins

Die Plugins unterscheiden sich darin, wie weit ihre Werkzeugkette über reinen Skill-Text hinausgeht. Drei Reifegrade:

| Reifegrad | Bedeutung | Beispiele |
|---|---|---|
| **L1 — skilltext-only** | Skill liefert strukturierte Texte (Schreiben, Schriftsätze, Memos, Gutachten-Skizzen). Keine eigenen Werkzeuge. | Großteil der 24 Fachanwalts-Plugins (`fachanwalt-erbrecht`, `fachanwalt-arbeitsrecht`, …), `methodenlehre-buergerliches-recht`, `zitierweise-deutsches-recht`, `jurastudium`. |
| **L2 — mit Werkzeugen** | Skill ruft Python- oder XLSX-Werkzeuge im Plugin-Ordner auf, die kalkulieren, Dateien bauen oder Vorlagen generieren. | `liquiditaetsplanung`, `insolvenzrecht`, `steuerrecht-anwalt-und-berater` (build_liquiditaetsplan.py); `anlagen-zu-schriftsaetzen` (build_anlagenkonvolut.py); `kanzlei-cowork/rechnungserstellung-rvg` (rvg_gebuehrenrechner.py); `forderungsmanagement-klagewerkstatt` (verzugszins_rechner.py); `phishing-vorfall-pruefer` (phishing_case_gate.py); `einfache-leichte-sprache-jura` (verstaendlichkeitscheck.py); `aktenaufbereiter-strafrecht` (aktenuebersicht_template.xlsx). |
| **L3 — mit Tests** | Plugin ist zusätzlich durch einen Smoke-Test in [`tests/smoke-tests.md`](./tests/smoke-tests.md) abgedeckt — Eingang, Kaltstart-Skill, erwarteter Output, Abbruchkriterium. | Aktuell: `liquiditaetsplanung`, `insolvenzrecht`, `fluggastrechte`, `sozialrecht`, `betreuungsrecht`, `berufsrecht-ki-vertragspruefung`, `anlagen-zu-schriftsaetzen`, `forderungsmanagement-klagewerkstatt`, `phishing-vorfall-pruefer`, `einfache-leichte-sprache-jura`, `kanzlei-cowork`. |

Für einen neuen Plugin gilt: L1 ist der akzeptable Start, L2 wird angestrebt, sobald wiederkehrende Berechnungen oder Dateigenerate sichtbar werden, und L3 wird vor einem Release gesetzt, wenn der Plugin fachlich-substanziell beansprucht wird.

## Schnellstart

Dieses Skill-Set lässt sich auf drei Wegen einbinden. Empfohlen ist **Weg 1** über die grafische Oberfläche; **Weg 2** für gezielten ZIP-Upload einer bestimmten Version; **Weg 3** für Claude Code im Terminal.

> 📆 **Release- vs. main-Stand.** Den **letzten Release-Tag** findest du auf der Seite [Releases](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Über **Weg 1 (Marketplace-Sync)** und **Weg 3 (Marketplace-Kommando)** wird der `main`-Branch geladen — das ist meist **neuer** als der letzte Release-Tag (Zwischen-Commits mit Fixes, neuen Tests, kleinen Ergänzungen). Über **Weg 2 (ZIP-Upload aus Release)** bekommst du den **getaggten, validierten Stand**. Für Stabilität → Weg 2; für neueste Korrekturen → Weg 1/3.

> 💡 **Findest du in Cowork kein Feld für den GitHub-Pfad?** Dann ist in deiner Oberfläche der Marketplace-Weg vermutlich noch nicht freigeschaltet. Lade die Plugin-ZIPs einzeln aus dem [Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) herunter und installiere sie über denselben Dialog, mit dem du z. B. „Legal Plugin" installierst. Schritt für Schritt erklärt: **[INSTALLATION_EINFACH.md](./INSTALLATION_EINFACH.md)**.

### Voraussetzungen

- Ein **Claude-Account** (Free oder Pro) – https://claude.ai/login
- Entweder **Claude Desktop** (https://claude.com/download) **oder** **Claude Code** (`npm install -g @anthropic-ai/claude-code`, danach `claude` im Terminal).
- Für Weg 3 zusätzlich `git`.

### Weg 1 — Installation über „Customize → Skills" (GUI, empfohlen)

Einfachster Weg in Claude Desktop oder der Cowork-Oberfläche:

1. Claude Desktop öffnen und in der linken Seitenleiste auf **Customize** klicken.
2. Auf **Skills** wechseln und neben „Personal plugins" das **+**-Symbol anklicken.
3. Im Dialogfeld den Pfad des GitHub-Repositorys im Format `owner/repo` eingeben: **`Klotzkette/claude-fuer-deutsches-recht`**.
4. Auf **Sync** klicken. Cowork liest daraufhin den Marketplace und listet alle Plugins (z. B. `arbeitsrecht`, `vertragsrecht`, Liquiditätsplanung (`liquiditaetsplanung`), `insolvenzrecht`, `steuerrecht-anwalt-und-berater` ...).
5. Beim gewünschten Plugin auf **Install** klicken. Nach erfolgreicher Installation wechselt der Button zu **Manage**.
6. Eine neue Konversation starten — die Skills stehen ab sofort zur Verfügung. Tipp: Mit `/skill` oder freier Eingabe (z. B. „Erstelle eine 3-Wochen-Liquiditätsvorschau") wird der passende Skill automatisch erkannt.

### Weg 2 — Manueller ZIP-Upload als Plugin

Wenn kein Marketplace-Manifest verwendet werden soll oder eine bestimmte Version festgehalten werden muss:

1. Das gewünschte einzelne Plugin-ZIP aus dem neuesten Release herunterladen, z. B. `liquiditaetsplanung.zip` von https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest.
2. In Cowork **Customize → Plugin** öffnen und über **+ → Create → Upload plugin** dieses einzelne Plugin-ZIP hochladen.
3. Nach dem Upload erscheint das Plugin in der Plugin-Liste und kann aktiviert werden.

**Wichtig:** Nicht das komplette Repository-ZIP aus **Code → Download ZIP** hochladen. Ein Upload-ZIP muss direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` usw. im ZIP-Root enthalten.

### Weg 3 — Marketplace-Kommando (Claude Code im Terminal)

Claude Code starten (`claude` im Terminal) und dann:

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install arbeitsrecht
/plugin install vertragsrecht
/plugin install liquiditaetsplanung
/plugin install insolvenzrecht
/plugin install steuerrecht-anwalt-und-berater
```

Einzelne Plugins lassen sich auch später mit `/plugin install <name>` nachinstallieren; `/plugin list` zeigt den aktuellen Stand.

Alternativ ein lokal geklontes Repository nutzen:

```bash
git clone https://github.com/Klotzkette/claude-fuer-deutsches-recht.git
cd claude-fuer-deutsches-recht
claude
```

Und dann im Claude-Code-Prompt:

```text
/plugin marketplace add .
/plugin install <plugin-name>
```

### Überprüfen, ob die Installation funktioniert hat

- In Claude Desktop: in der Plugin-Liste muss neben dem Plugin **Manage** statt **Install** stehen.
- In Claude Code: `/plugin list` zeigt das Plugin als aktiviert.
- Funktionstest: in einer neuen Konversation einen typischen Auftrag stellen, z. B. „Mache eine 3-Wochen-Liquiditätsvorschau für meine GmbH" → der Skill `liquiditaetsvorschau-3wochen` sollte sichtbar geladen werden.

Details und Fehlersuche siehe [`QUICKSTART.md`](./QUICKSTART.md).

## Schwerpunkte für die deutsche Praxis

Dieses Repository ist vollständig auf das deutsche Recht und die Arbeitsweise deutscher Kanzleien zugeschnitten:

- Urteile sind nicht bindend; Ausnahme: § 31 BVerfGG.
- Vorprozessuale Beweiserhebung ist auf eng begrenzte gesetzliche Instrumente beschränkt: §§ 142, 144 ZPO; § 810 BGB; § 242 BGB; Art. 15 DSGVO; Auskunfts- und Stufenklage (§ 254 ZPO).
- Kommentare und Aufsätze sind argumentativ tragend – jeder Skill belegt mit Bearbeiter, Kommentar, Auflage, Norm, Rn.
- Zitierweise: BGH-Stil – verbindlich in [`references/zitierweise.md`](./references/zitierweise.md).
- Due Diligence läuft über Q&A, Datenraum und anwaltliche Sachverhaltsaufklärung.
- Kündigungsschutz: Regelfall nach KSchG ab 6 Monate / mehr als 10 Arbeitnehmer.

Aktueller Stand: **97 Plugins, über 1600 Skills, 43 Testakten**. Abgedeckt sind klassische Mandantenpraxis, alle 24 Fachanwaltschaften, Großkanzlei- und Mittelstandsformate sowie Spezialdisziplinen wie Insolvenzverwaltung, Zwangsverwaltung, Zwangsversteigerung, Markenrecht für Luxus-Fashion mit USPTO-Lanham-Act-Modul, betriebliche Altersversorgung in Konzernen mit Düsseldorf-Kyoto-Profil, StaRUG-Krisenfrüherkennung mit Vier-und-zwanzig-Monats-Horizont, Schriftform-/Textform-Workflow-Organisator nach BGH I ZR 202/25 und BGH VIII ZR 159/23, Wandeldarlehen-Lebenszyklus mit Cap-Table-Mechanik sowie generische Mechanik-Prüfer für Subsumtion, Bereicherungs-/Anfechtungsrecht und die KI-VO (Verordnung (EU) 2024/1689).

### Materielle Rechtsgebiete

- **Zivilrecht & Vertragsrecht** – `vertragsrecht`, `nda-abgleich`, `agb-pruefung` (in `vertragsrecht`), `produktrecht`, `fluggastrechte`
- **Arbeitsrecht** – `arbeitsrecht`, `fachanwalt-arbeitsrecht` (Kündigungsschutzklage § 4 KSchG, Aufhebungsvertrag mit Sperrzeit-Prüfung, BR-Anhörung § 102 BetrVG, Massenentlassung § 17 KSchG)
- **Gesellschafts- & Wirtschaftsrecht** – `gesellschaftsrecht`, `fachanwalt-handels-gesellschaftsrecht`, `grosskanzlei-corporate-ma`, `mittelstand-corporate-ma`, `corporate-kanzlei`, `fachanwalt-internationales-wirtschaftsrecht`
- **Bank-, Kapitalmarkt- & Aufsichtsrecht** – `fachanwalt-bank-kapitalmarktrecht`, `regulatorisches-recht`, `geldwaeschepraevention-aml-kyc`, `aussenwirtschaft-zoll-sanktionen`
- **Insolvenz & Sanierung** – `insolvenzrecht` (Gläubiger/Schuldner), `insolvenzverwaltung` (Verwalter-Sicht, § 270d, § 15b, § 129 ff.), `zwangsverwaltung-zvg` (ZVG-Verwalter, § 155 Verteilungsplan), `insolvenzforderungsanmeldungspruefung`, `insolvenzplan-starug-planwerkstatt`, `fortbestehensprognose`, `fachanwalt-insolvenz-sanierungsrecht`
- **Liquidität, Forderung & Inkasso** – `liquiditaetsplanung`, `forderungsmanagement-klagewerkstatt`, `phishing-vorfall-pruefer`, `vertragsausfueller`, Inkasso nach RDG / § 43d BRAO (in `regulatorisches-recht`)
- **Steuerrecht** – `steuerrecht-anwalt-und-berater` (USt-Voranmeldung, Korrektur § 153 AO, Bescheidanalyse, Einspruch, Außenprüfung, Selbstanzeige, Steuerberater-Werkzeuge)
- **Strafrecht & OWi** – `aktenaufbereiter-strafrecht`, `fachanwalt-strafrecht`, `strafbefehl-verteidiger`, `verkehrsowi-verteidiger`
- **Verwaltungs- & Verfassungsrecht** – `verfassungsrecht`, `fachanwalt-verwaltungsrecht` (Eilantrag § 80 V VwGO), `verkehr-infrastrukturrecht`, `umweltrecht`, `energierecht`, `fachanwalt-vergaberecht`
- **Familien-, Erb-, Sozial- & Betreuungsrecht** – `fachanwalt-familienrecht` (Düsseldorfer Tabelle), `fachanwalt-erbrecht` (Pflichtteilsberechnung), `sozialrecht-kanzlei`, `fachanwalt-sozialrecht`, `betreuungsrecht`, `fachanwalt-migrationsrecht`
- **Miet- & Immobilienrecht** – `mietrecht`, `fachanwalt-miet-wohnungseigentumsrecht`, `immobilienrechtspraxis`
- **Gewerblicher Rechtsschutz & Medien** – `gewerblicher-rechtsschutz` (Markenanmeldung DPMA, UWG-Abmahnung), `fachanwalt-gewerblicher-rechtsschutz`, `fachanwalt-urheber-medienrecht` (Gegendarstellung), `patentrecherche`, `markenrecht-fashion-luxus` (Luxus-Fashion-IP mit Anmeldung allerlei Markenarten inkl. Haptik- und Soundmarken, EUIPO Alicante, Selektivvertrieb Coty, USPTO/Lanham Act, TTAB, NYC-Korrespondenzkanzlei)
- **Insolvenz, Sanierung und Krisenmanagement (erweitert)** – `krisenfrueherkennung-starug` (§ 1 StaRUG mit Vier-und-zwanzig-Monats-Horizont, § 102 StaRUG-Warnpflicht, Restrukturierungsplan, Stabilisierungsanordnung, Cross-Class-Cram-Down), ergänzt durch `insolvenzplan-starug-planwerkstatt` und `fachanwalt-insolvenz-sanierungsrecht`
- **Arbeits- und Vergütungsrecht (erweitert)** – `bav-strategie-konzern` (betriebliche Altersversorgung als Konzern-Architektur: alle fünf Durchführungswege, CTA-Doppeltreuhand, Pension Buyouts, Drei-Stufen-Theorie BAG, internationale Benefits, Düsseldorf-Kyoto-Profil)
- **Form und Zugang im Zivilrecht** – `schriftform-und-textform-bgb` (Workflow-Organisator zu §§ 126/126a/126b BGB, Zugang § 130 BGB, lernt aus BGH I ZR 202/25 Maklervertrag und BGH VIII ZR 159/23 Mietkündigung, Klauselgenerator, Mandantenwarnungen zu qES-Zugang per E-Mail/WhatsApp)
- **IT-Recht, Datenschutz & KI-Governance** – `datenschutzrecht` (Art. 15 DSGVO, Art. 33/34 DSGVO), `fachanwalt-it-recht` (Cyber-Incident 72 h), `ki-governance` (EU AI Act), DORA-IKT-Vertragsprüfung in `regulatorisches-recht`, `berufsrecht-ki-vertragspruefung`
- **Verkehr, Transport, Versicherung, Medizin** – `fachanwalt-verkehrsrecht`, `fachanwalt-transport-speditionsrecht` (CMR/HGB), `fachanwalt-versicherungsrecht`, `fachanwalt-medizinrecht`, `fachanwalt-bau-architektenrecht` (VOB/B)
- **Sportrecht, Agrarrecht** – `fachanwalt-sportrecht` (CAS-Berufung), `fachanwalt-agrarrecht` (GAP-Sammelantrag)
- **Europa- & Common-Law-Kompass** – `europarecht-kompass`, `common-law-kompass`

### Querschnittliche Werkzeuge

- **Prozess- & Schriftsatz-Werkstatt** – `prozessrecht` (Mahnbescheid §§ 688 ff. ZPO, einstweilige Verfügung §§ 935/940 ZPO + Schutzschrift, Vollstreckung), `anlagen-zu-schriftsaetzen`, `memorandums-ersteller`, `tabellenreview-3d`
- **Kanzleibetrieb** – `kanzlei-allgemein`, `kanzlei-cowork`, `kanzlei-builder-hub`, `rechtsberatungsstelle`, `verlagsredaktion`
- **Methode & Lehre** – `jurastudium` (Methodenlehre ZR/StR/ÖR, Subsumtion, Rechtsgeschichte, Lernstrategien, Lösungsschemata, Prüfungsgespräch nach AG-Tradition), `methodenlehre-buergerliches-recht`, `zitierweise-deutsches-recht`, `einfache-leichte-sprache-jura`

Eine vollständige Übersicht aller Plugins und Rechtsgebiete steht in [`references/rechtsgebiete-uebersicht.md`](./references/rechtsgebiete-uebersicht.md). Die kompakte Plugin-Liste mit Reifegrad findest du im Abschnitt ["Was ist drin?"](#was-ist-drin) weiter oben.

## Verbindliche Zitierweise

Jeder Skill verweist auf [`references/zitierweise.md`](./references/zitierweise.md). Die Kernregeln in Kurzfassung:

- **Urteile:** `BGH, Urt. v. 13.07.2022 – VIII ZR 317/21, NJW 2022, 2754 Rn. 21.`
- **Beschlüsse:** `BVerfG, Beschl. v. 06.11.2019 – 1 BvR 16/13, BVerfGE 152, 152 Rn. 78 – "Recht auf Vergessen I".`
- **Kommentare:** `Ernst, in: MüKoBGB, 9. Aufl. 2022, § 280 Rn. 154.`
- **Online-Kommentare:** `Sutschet, in: Online-Kommentar BGB, 70. Ed. (Stand 01.02.2025), § 311 Rn. 45.`
- **Aufsätze:** `Grigoleit, NJW 2020, 1873 (1876).`

Pflicht: Datum + Aktenzeichen + Fundstelle + Randnummer bei Rspr.; Bearbeiter + Werk + Auflage + Norm + Rn. bei Kommentaren.

### Methodenlehre und Zitierweise als zuschaltbare Plugins

Die Inhalte aus [`references/methodik-buergerliches-recht.md`](./references/methodik-buergerliches-recht.md) und [`references/zitierweise.md`](./references/zitierweise.md) liegen zusätzlich als zwei eigenständige, einzeln aktivierbare Plugins im Marketplace:

- [`methodenlehre-buergerliches-recht`](./methodenlehre-buergerliches-recht) — Gutachtenstil, Anspruchsgrundlagen-Reihenfolge, Auslegungskanones ohne starre Rangfolge (pragmatische BGH-Praxis: Teleologie dominiert), Generalklauseln und Rechtsfortbildung als reale Werkzeuge.
- [`zitierweise-deutsches-recht`](./zitierweise-deutsches-recht) — Hauszitierweise mit Pinpoint-Randnummer, Palandt/Grüneberg-Regel, Typografiestandards, Pflicht-Checkliste vor jeder Ausgabe.

Beide Plugins enthalten die gleichen Inhalte wie die Referenzdateien, sind aber als Skill ausgeführt: Sobald sie in Cowork aktiviert sind, gilt die Methodik bzw. die Zitierweise als ausdrückliche Pflicht für jede Antwort — unabhängig davon, ob ein Rechtsgebietsplugin geladen ist.

Aktivierung in Cowork: `Customize → Skills → Persönliche Plugins → +` und das jeweilige Plugin hinzuschalten.

## Für Einsteiger: Schritt-für-Schritt-Anleitung

### Was brauche ich?

1. **Einen Claude-Account** (kostenlos oder Pro) – Registrierung unter https://claude.ai
2. **Claude Desktop** (empfohlen) oder **Claude Code** – Download: https://claude.com/download
3. **Dieses Repository** – als ZIP herunterladen oder mit Git klonen

### Installation in Claude Desktop (für absolute Einsteiger)

**Schritt 1: Claude Desktop installieren**

1. Gehe zu https://claude.com/download
2. Lade die Version für dein Betriebssystem herunter (Windows / Mac / Linux)
3. Installiere die Anwendung und melde dich mit deinem Claude-Account an

**Schritt 2: Repository herunterladen**

1. Klicke oben auf dieser GitHub-Seite auf den grünen Button „Code"
2. Wähle „Download ZIP"
3. Entpacke die ZIP-Datei an einem Ort deiner Wahl (z. B. `Dokumente/Claude-Skills`)

**Schritt 3: Skills in Claude Desktop aktivieren**

1. Öffne Claude Desktop
2. Klicke auf das Zahnrad-Symbol ⚙️ (Einstellungen) oben rechts
3. Gehe zu **Capabilities** (Funktionen)
4. Aktiviere **Code execution** und **Skills**

**Schritt 4: Einen Skill hochladen**

1. In den Einstellungen: gehe zu **Skills**
2. Klicke auf **Upload skill**
3. Navigiere zum entpackten Ordner `claude-fuer-deutsches-recht`
4. Wähle einen Skill-Ordner aus (z. B. `arbeitsrecht` oder `vertragsrecht`)
5. Bestätige – fertig. Der Skill ist jetzt aktiv.

**Schritt 5: Skill verwenden**

1. Starte einen neuen Chat in Claude Desktop
2. Der Skill wird automatisch erkannt, wenn du relevante Fragen stellst
3. Beispiel: „Erstelle mir einen Entwurf für eine ordentliche Kündigung nach § 622 BGB"

### Installation in Claude Code (für Entwickler / Terminal-Nutzer)

```bash
# Repository klonen
git clone https://github.com/Klotzkette/claude-fuer-deutsches-recht.git
cd claude-fuer-deutsches-recht

# Als Marketplace hinzufügen
claude /plugin marketplace add .

# Skills installieren
claude /plugin install arbeitsrecht
claude /plugin install vertragsrecht
claude /plugin install prozessrecht
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
A: **Nicht sehr**. LLMs erfinden oft Zitate. Die Skills sind so konzipiert, dass sie die korrekte BGH-Zitierweise verwenden, aber Sie müssen **jede Fundstelle** selbst prüfen (juris, einschlägige Datenbanken etc.).

## Hinweise zur Nutzung

⚠️ **Bitte beachten Sie:**

1. **Übersetzungsarbeit**: Diese Skills sind eine **KI-gestützte Übersetzung und Anpassung** der englischsprachigen „claude-for-legal"-Skills von Anthropic. Sie wurden für das deutsche Rechtssystem adaptiert, aber **nicht von Juristen final geprüft**.
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
