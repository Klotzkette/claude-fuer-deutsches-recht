# Claude – Deutsche rechtliche Fähigkeiten / German Legal Skills

> **Experimentelles Skill-Set** für die anwaltliche Praxis im deutschen Recht – Skills, Sub-Agenten, Workflows etc. als Anregung für Kanzlei-Arbeitsabläufe. Orientiert sich an der **deutschen Rechtspraxis** und am hohen Stellenwert von **Kommentaren und Aufsätzen**. Enthält keinerlei Fachgutachten oder Rechtsberatung, alle Angaben ohne Gewähr – jede Nutzerin und jeder Nutzer kalibriert die Skills selbst für die eigene Praxis.

## 🚨 KEINE Aussage über Berufsrecht, Datenschutz, KI-VO oder Beschlagnahmeverbote

**Lesen, bevor irgendetwas davon eingesetzt wird.** Dieses Repository ist ausschließlich ein technisches Experiment. Es trifft **keinerlei Aussage** darüber, ob der Einsatz dieser Skills in einer konkreten Praxisumgebung berufs-, datenschutz- oder KI-rechtlich zulässig ist. Alle nachstehenden Fragen muss **jede Nutzerin und jeder Nutzer in eigener Verantwortung** vor der ersten Nutzung prüfen – das Repository, seine Autorin / sein Autor und alle Mitwirkenden übernehmen dafür keinerlei Verantwortung oder Haftung:

- **Strafrechtliches Mandatsgeheimnis – §§ 203, 204 StGB.** Die Skills sagen nichts darüber aus, ob ein konkreter Einsatz mit dem strafbewehrten Geheimnisschutz des § 203 StGB (Verletzung von Privatgeheimnissen) und § 204 StGB (Verwertung fremder Geheimnisse) vereinbar ist – auch nicht in der Variante § 203 Abs. 3, 4 StGB (mitwirkende Personen, sonstige Stellen).
- **Berufsrecht – § 43e BRAO, § 2 BORA, § 53 StPO.** Es wird **nicht** geprüft, ob der Einsatz mit § 43e BRAO (Inanspruchnahme von Dienstleistern, insbesondere Cloud/KI), § 2 BORA (Verschwiegenheit), den Zeugnisverweigerungsrechten nach § 53 StPO und den Beschlagnahmeverboten nach § 97 StPO vereinbar ist. Gleiches gilt sinngemäß für andere **freie Berufe** mit eigenem Berufsrecht (StBerG für Steuerberater:innen, WPO für Wirtschaftsprüfer:innen, ÄrztInnen, Notar:innen, Patentanwält:innen u. a.).
- **Datenschutz – DSGVO, BDSG.** Es wird **nicht** beurteilt, ob die Verarbeitung personenbezogener Daten DSGVO-konform ist, ob eine ausreichende **Rechtsgrundlage** (Art. 6, 9 DSGVO) vorliegt, ob ein **Auftragsverarbeitungsvertrag** nach Art. 28 DSGVO geschlossen werden muss, ob eine **Datenschutz-Folgenabschätzung** (Art. 35 DSGVO) erforderlich ist oder ob die **Informationspflichten** nach Art. 13, 14 DSGVO erfüllt sind.
- **Drittlandtransfer – USA / Kapitel V DSGVO.** Es wird **keine** Aussage darüber getroffen, ob ein Datentransfer in die USA oder ein anderes Drittland nach Art. 44 ff. DSGVO zulässig ist, ob das **EU-US Data Privacy Framework** einschlägig ist, ob **Standardvertragsklauseln** (SCC) oder ein **Transfer Impact Assessment** (TIA) genügen – oder ob der US Cloud Act, FISA § 702 und Executive Order 12333 dem konkreten Einsatz im Sinne von Schrems II (EuGH, Urt. v. 16.07.2020 – C-311/18) entgegenstehen.
- **KI-Verordnung (KI-VO / EU AI Act, VO (EU) 2024/1689).** Es wird **nicht** entschieden, ob der Einsatz unter eine der Hochrisiko-Kategorien nach **Art. 6 KI-VO** in Verbindung mit **Anhang III KI-VO** fällt (insbesondere Zugang zur Justiz, Strafverfolgung, demokratische Prozesse), ob **Transparenzpflichten** nach Art. 50 KI-VO greifen, ob es sich um ein **General-Purpose-AI-Modell** nach Art. 51 ff. KI-VO handelt und welche **Pflichten als Betreiber** (Art. 26 KI-VO) zu erfüllen sind.
- **Beschlagnahmeverbote und auslandsrechtliche Zugriffe.** Es wird nicht geprüft, ob Eingabedaten und Modellantworten gegen Beschlagnahme nach **§§ 97, 160a StPO**, gegen **US Cloud Act**, **FISA § 702**, **CLOUD Act warrants**, **PATRIOT Act § 215** oder sonstige extraterritoriale Zugriffsbefugnisse hinreichend geschützt sind. Dafür ist die jeweilige Nutzerin / der jeweilige Nutzer allein verantwortlich.
- **Zugang, Auftragsverarbeitung, Hosting.** Wie der API-Zugang zum Modell beschafft wird (Anthropic direkt, AWS Bedrock, Google Vertex, eigenes Hosting), ob mit dem Anbieter ein **Auftragsverarbeitungsvertrag** geschlossen wird, ob ein **berufsrechtskonformer Cloud-Vertrag** vorliegt und ob die Anforderungen an die Verschwiegenheit / Mandatsgeheimnis-Header und Datenflusskontrolle in der konkreten Deployment-Konstellation eingehalten sind, bleibt vollständig in der **Eigenverantwortung der Nutzerin / des Nutzers**.

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

Plugins (in Claude-Code-Terminologie) für die wichtigsten Rechtsgebiete der deutschen Beratungspraxis:

| Plugin | Beschreibung |
| --- | --- |
| [`arbeitsrecht`](./arbeitsrecht) | Individual- und Kollektivarbeitsrecht – Kündigung, Aufhebungsvertrag, Abmahnung, Anhörung Betriebsrat, KSchG-Klage, internationale Entsendungen |
| [`datenschutzrecht`](./datenschutzrecht) | DSGVO, BDSG, TTDSG, Auskunft, Datenpanne, AVV |
| [`gesellschaftsrecht`](./gesellschaftsrecht) | GmbH, AG, Personengesellschaften, M&A, Due Diligence, Gesellschafterbeschluss, Handelsregister |
| [`gewerblicher-rechtsschutz`](./gewerblicher-rechtsschutz) | Marke, Design, Patent, Urheberrecht, UWG-Abmahnung |
| [`jurastudium`](./jurastudium) | Werkzeuge für Studium und Referendariat |
| [`kanzlei-builder-hub`](./kanzlei-builder-hub) | Werkzeuge zum Bauen eigener kanzleiinterner Skills |
| [`ki-governance`](./ki-governance) | EU-KI-VO, KI-Inventar, AIA, Vendor Review |
| [`produktrecht`](./produktrecht) | Produktrecht, AGB, Impressum, PAngV, Marketing-Claims |
| [`prozessrecht`](./prozessrecht) | Zivil-, Straf- und Verwaltungsprozess, Mahnverfahren, einstweilige Verfügung, Zwangsvollstreckung, Verkehrsunfall |
| [`rechtsberatungsstelle`](./rechtsberatungsstelle) | Pro-Bono-Beratungsstellen, Mandantenakte, Mandantenbrief |
| [`regulatorisches-recht`](./regulatorisches-recht) | Aufsichtsrecht, KWG, GwG, EnWG, TKG, Inkasso/RDG, UStVA, DORA-IKT-Vertragsprüfung |
| [`insolvenzrecht`](./insolvenzrecht) | Zahlungsunfähigkeit § 17 InsO (BGHZ 163, 134), zweistufige Überschuldungsprüfung § 19 InsO mit Fortbestehensprognose (IDW S 11), Antragspflicht § 15a InsO und Haftung wegen Insolvenzverschleppung, Gläubigerantrag § 14 InsO, gerichtsfähige Liquiditätsvorschau. |
| [Liquiditätsplanung](./liquiditaetsplanung) | Bündel-Plugin für die rollierende Liquiditätsplanung: 3-Wochen-Test § 17 InsO (BGH BGHZ 163, 134), 13/26/52-Wochen-Forecast mit Ampel, Fortführungsprognose IDW S 6/S 11 und insolvenzrechtliche Liquiditätsbilanz. Verweist auf die Skills in `steuerberater-werkzeuge` und `insolvenzrecht`. |
| [`steuerberater-werkzeuge`](./steuerberater-werkzeuge) | Werkzeugbox für Steuerberater und GmbH-Geschäftsleitung: BWA-/SuSa-/Bilanz-Krisenprüfung (§§ 17, 19 InsO, § 102 StaRUG-Hinweispflicht). Die rollierende Liquiditätsplanung steht im Schwester-Plugin Liquiditätsplanung (`liquiditaetsplanung`). |
| [`vertragsrecht`](./vertragsrecht) | NDA, SaaS-/MSA-Review, Lieferanten-AGB, Renewal-Tracking |
| [`betreuungsrecht`](./betreuungsrecht) | Skills für berufliche Betreuer nach BtOG und §§ 1814 ff. BGB (Reform 2023): Jahresbericht ans Betreuungsgericht (§ 1863 BGB), Vermögensverzeichnis und Rechnungslegung (§§ 1835, 1865 BGB), Genehmigungspflicht-Prüfung (§§ 1848 ff., 1831, 1832 BGB). |

Zusätzlich:
- [`verwaltete-agentenrezepte`](./verwaltete-agentenrezepte) – wiederverwendbare Vorlagen für Multi-Agent-Arbeitsabläufe (Aufsichts-Monitor, Gerichtskalender-Monitor, Verlängerungs-Monitor, Due-Diligence-Tabelle).
- [`references/zitierweise.md`](./references/zitierweise.md) – die deutsche Zitierweise (BGH-Stil), an der sich alle Skills orientieren.
- [`references/methodik-deutsches-recht.md`](./references/methodik-deutsches-recht.md) – Methodenlehre, Anspruchsgrundlagenreihenfolge, Beweislast, Fristen.

## Schnellstart

Dieses Skill-Set lässt sich auf drei Wegen einbinden. Empfohlen ist **Weg 1** über die grafische Oberfläche; **Weg 2** für gezielten ZIP-Upload einer bestimmten Version; **Weg 3** für Claude Code im Terminal.

### Voraussetzungen

- Ein **Claude-Account** (Free oder Pro) – https://claude.ai/login
- Entweder **Claude Desktop** (https://claude.com/download) **oder** **Claude Code** (`npm install -g @anthropic-ai/claude-code`, danach `claude` im Terminal).
- Für Weg 3 zusätzlich `git`.

### Weg 1 — Installation über „Customize → Skills" (GUI, empfohlen)

Einfachster Weg in Claude Desktop oder der Cowork-Oberfläche:

1. Claude Desktop öffnen und in der linken Seitenleiste auf **Customize** klicken.
2. Auf **Skills** wechseln und neben „Personal plugins" das **+**-Symbol anklicken.
3. Im Dialogfeld den Pfad des GitHub-Repositorys im Format `owner/repo` eingeben: **`Klotzkette/claude-fuer-deutsches-recht`**.
4. Auf **Sync** klicken. Cowork liest daraufhin den Marketplace und listet alle Plugins (z. B. `arbeitsrecht`, `vertragsrecht`, Liquiditätsplanung (`liquiditaetsplanung`), `insolvenzrecht`, `steuerberater-werkzeuge` ...).
5. Beim gewünschten Plugin auf **Install** klicken. Nach erfolgreicher Installation wechselt der Button zu **Manage**.
6. Eine neue Konversation starten — die Skills stehen ab sofort zur Verfügung. Tipp: Mit `/skill` oder freier Eingabe (z. B. „Erstelle eine 3-Wochen-Liquiditätsvorschau") wird der passende Skill automatisch erkannt.

### Weg 2 — Manueller ZIP-Upload als Plugin

Wenn kein Marketplace-Manifest verwendet werden soll oder eine bestimmte Version festgehalten werden muss:

1. Auf https://github.com/Klotzkette/claude-fuer-deutsches-recht das Release **v1.0** öffnen (oder **Code → Download ZIP** vom `main`-Branch).
2. In Cowork **Customize → Plugin** öffnen und über **+ → Create → Upload plugin** das ZIP hochladen.
3. Nach dem Upload erscheint das Plugin in der Plugin-Liste und kann aktiviert werden.

**Wichtig:** Das ZIP muss die korrekte Verzeichnisstruktur enthalten — `SKILL.md` auf der jeweils obersten Skill-Ebene (z. B. `arbeitsrecht/skills/<skill-name>/SKILL.md`). Andernfalls vor dem Upload neu komprimieren.

### Weg 3 — Marketplace-Kommando (Claude Code im Terminal)

Claude Code starten (`claude` im Terminal) und dann:

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install arbeitsrecht
/plugin install vertragsrecht
/plugin install liquiditaetsplanung
/plugin install insolvenzrecht
/plugin install steuerberater-werkzeuge
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
- Zitierweise: BGH-/Beck-Stil – verbindlich in [`references/zitierweise.md`](./references/zitierweise.md).
- Due Diligence läuft über Q&A, Datenraum und anwaltliche Sachverhaltsaufklärung.
- Kündigungsschutz: Regelfall nach KSchG ab 6 Monate / mehr als 10 Arbeitnehmer.

Ergänzend über 20 Skills zu typisch deutschen Themen, u. a.:

- **Kündigungsschutzklage** nach § 4 KSchG (3-Wochen-Frist)
- **Mahnbescheid** §§ 688 ff. ZPO
- **Einstweilige Verfügung & Schutzschrift**
- **Aufhebungsvertrag** inkl. Sperrzeit-Prüfung
- **Anhörung des Betriebsrats** § 102 BetrVG
- **Verkehrsunfall**-Abwicklung
- **UWG-Abmahnung** und **Urheberrechts-Abmahnung**
- **AGB-Prüfung** §§ 305 ff. BGB
- **Widerruf im Fernabsatz** §§ 312g, 355 BGB
- **GmbH-Gründung** und **Handelsregisteranmeldung**
- **DSGVO-Auskunft** Art. 15 DSGVO und **Datenpanne** Art. 33/34 DSGVO
- **Umsatzsteuer-Voranmeldung** und Korrektur nach § 153 AO
- **Inkasso** nach RDG / § 43d BRAO
- **DORA-IKT-Vertragsprüfung** (VO (EU) 2022/2554) mit Tabular Review, EUR-Lex-Live-Snapshot und Klausel-Patch-Liste
- **Markenanmeldung** beim DPMA
- **Impressumspflicht** §§ 5, 6 DDG
- **PAngV-Prüfung**

Eine vollständige Übersicht steht in [`references/rechtsgebiete-uebersicht.md`](./references/rechtsgebiete-uebersicht.md).

## Verbindliche Zitierweise

Jeder Skill verweist auf [`references/zitierweise.md`](./references/zitierweise.md). Die Kernregeln in Kurzfassung:

- **Urteile:** `BGH, Urt. v. 13.07.2022 – VIII ZR 317/21, NJW 2022, 2754 Rn. 21.`
- **Beschlüsse:** `BVerfG, Beschl. v. 06.11.2019 – 1 BvR 16/13, BVerfGE 152, 152 Rn. 78 – "Recht auf Vergessen I".`
- **Kommentare:** `Ernst, in: MüKoBGB, 9. Aufl. 2022, § 280 Rn. 154.`
- **BeckOK:** `Sutschet, in: BeckOK BGB, 70. Ed. (Stand 01.02.2025), § 311 Rn. 45.`
- **Aufsätze:** `Grigoleit, NJW 2020, 1873 (1876).`

Pflicht: Datum + Aktenzeichen + Fundstelle + Randnummer bei Rspr.; Bearbeiter + Werk + Auflage + Norm + Rn. bei Kommentaren.

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
A: **Nicht sehr**. LLMs erfinden oft Zitate. Die Skills sind so konzipiert, dass sie die korrekte BGH-Zitierweise verwenden, aber Sie müssen **jede Fundstelle** selbst prüfen (Beck-Online, juris etc.).

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

## Lizenz

Doppellizenziert unter **Apache License, Version 2.0** ODER **MIT License**, nach Wahl der Nutzerin / des Nutzers (`SPDX-License-Identifier: Apache-2.0 OR MIT`) – siehe [`LICENSE`](./LICENSE), [`LICENSE-APACHE`](./LICENSE-APACHE), [`LICENSE-MIT`](./LICENSE-MIT) und [`NOTICE`](./NOTICE).

Die ursprüngliche Vorlage `claude-for-legal` von Anthropic steht unter der MIT-Lizenz; diese Adaption erweitert, ersetzt und ergänzt die ursprünglichen Inhalte und wird unter dem oben genannten Doppellizenz-Modell veröffentlicht.

## Mitwirken

Beiträge willkommen – siehe [`CONTRIBUTING.md`](./CONTRIBUTING.md).
