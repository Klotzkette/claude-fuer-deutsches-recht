# vergaberecht-werkstatt

<!-- BEGIN top-readme-intro (manual) -->

[Start](#vergaberecht-werkstatt) | [Dateikatalog](#dateikatalog) | [Downloads](#sofort-downloads) | [Vergabestelle](vergabestelle-behoerden/README.md) | [Bieter](bieter-unternehmen/README.md) | [Konkurrent](konkurrenten-rechtsschutz/README.md) | [Skills](SKILLS.md) | [Testakten](testakten/README.md) | [Rechtsprechung](references/leitentscheidungen-anker.md) | [Qualität](#validatoren) | [Mitwirken](CONTRIBUTING.md)

Die Vergaberecht-Werkstatt bündelt drei rollenfeste Arbeitsumgebungen für das deutsche und europäische Vergaberecht: für Vergabestellen, Bieter beziehungsweise Bewerber und Konkurrenten. Jedes Plugin verbindet fachlich konkrete Skills, autarke Prompts, Vorlagen, Rechtsprechungsanker und realistische Testakten vom Akteneingang bis zu Vergabekammer und OLG.

## In 20 Sekunden starten

Claude Desktop oder Cowork: Rollen-ZIP herunterladen und unter `Customize`, `Plugins`, `+` als eigenes Plugin hochladen. Claude Code: einmal `/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht`, danach den Rollenbefehl aus der Tabelle und `/reload-plugins` ausführen. [Offizielle Installationshinweise](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

| Rolle | Desktop/Cowork | Claude Code | Danach Unterlagen anhängen und senden |
| --- | --- | --- | --- |
| Vergabestelle | [`vergabestelle-behoerden.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergabestelle-behoerden.zip) | `/plugin install vergabestelle-behoerden@klotzkette-german-legal-skills` | `Neuer Vergabestellenfall. Prüfe die beigefügten Unterlagen vollständig, sichere Fristen und Rechtsregime und erstelle den nächsten entscheidungsreifen Behördenoutput.` |
| Bieter | [`bieter-unternehmen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/bieter-unternehmen.zip) | `/plugin install bieter-unternehmen@klotzkette-german-legal-skills` | `Neue Bewerbung. Prüfe die beigefügten Vergabeunterlagen vollständig, sichere Abgabefrist und Ausschlussrisiken und erstelle den nächsten abgabefertigen Angebotsoutput.` |
| Konkurrent | [`konkurrenten-rechtsschutz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/konkurrenten-rechtsschutz.zip) | `/plugin install konkurrenten-rechtsschutz@klotzkette-german-legal-skills` | `Neuer Konkurrentenfall. Prüfe die beigefügten Unterlagen vollständig, sichere sofort Rüge- und Zuschlagsfristen und erstelle den stärksten fristgerechten Rechtsbehelf.` |

Das Plugin genügt: kein zusätzlicher Prompt, keine Skillnamen und keine Vorabwahl des Outputs. Es liest sichtbare Daten selbst, antwortet zuerst in fünf Zeilen und fragt erst danach höchstens drei echte Blocker gesammelt ab. Für Chats ohne Plugin ist der rollenpassende Arbeitsprompt die Vollfassung; der Unified Mini Prompt ist nur für knappen Kontext gedacht.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

Wer alles lokal benötigt, nimmt direkt das [`alles-komplettpaket.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/alles-komplettpaket.zip). Alle weiteren Einzel- und Sammeldownloads stehen im Abschnitt [Sofort-Downloads](#sofort-downloads).

## Rechtsstand-Lotse Sommer 2026

| Stand | Was jetzt gilt | Direkter Arbeitsweg |
| --- | --- | --- |
| seit 30.06.2026 | VO (EU) 2026/718 konkretisiert Art. 25 VO (EU) 2024/1735 für erfasste Windvergaben; Rotorblätter müssen mindestens 70 Prozent nach Gewicht rezyklierbar sein | [gemeinsame Prüfkarte](references/netto-null-technologien-vergabe-2026.md) · [Vergabestelle](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/vergabestelle-behoerden/skills/netto-null-technologien-vergabe/SKILL.md) · [Bieter](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/bieter-unternehmen/skills/netto-null-technologien-vergabe/SKILL.md) · [Konkurrent](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vergaberecht-werkstatt/konkurrenten-rechtsschutz/skills/netto-null-technologien-vergabe/SKILL.md) |
| seit 01.07.2026 | GWB-/VgV-Reform nur für Neuverfahren; § 187 Abs. 2 GWB hält Altverfahren einschließlich Rechtsschutz im alten Recht | [Geltungs- und Entscheidungsanker](references/leitentscheidungen-anker.md#zeitliche-geltungsweiche-zum-1-juli-2026) |
| Urteil vom 09.07.2026 | EuGH C-856/24 verlangt für die ÖPNV-Direktvergabe an einen internen Betreiber auf der Sonderroute der VO (EG) 1370/2007 übertragenes Betriebsrisiko | [Leitentscheidungen](references/leitentscheidungen-anker.md#eu--und-unionsrechtsanker) |
| Entwurf vom 30.06.2026 | Die geplante UVgO-Neufassung ist noch nicht geltendes Recht; Einführungsakt und Bestandsrecht von Bund oder Land bleiben maßgeblich | [Status- und Quellenhinweis](references/leitentscheidungen-anker.md#uvgo-reformentwurf-vom-30-juni-2026) |

## Rollenkarte

| Marktrolle | Arbeitsumgebung ansehen | Plugin herunterladen | Ohne Plugin starten | Testakten |
| --- | --- | --- | --- | --- |
| Vergabestelle | [`vergabestelle-behoerden`](vergabestelle-behoerden/README.md) | [`vergabestelle-behoerden.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergabestelle-behoerden.zip) | [Arbeitsprompt](vergaberecht-arbeitsprompt-vergabestelle.md) · [Kurzprompt](vergaberecht-kurzprompt-vergabestelle.md) · [Mini bis 7.500 Zeichen](unified-mini-prompts/vergabestelle-behoerden.md) | [Reinigung](testakten/01-reinigung-grundschule-musterstadt/README.md) · [Laptops](testakten/02-laptopbeschaffung-landesamt-musterland/README.md) · [§ 132 GWB](testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/README.md) |
| Bieter | [`bieter-unternehmen`](bieter-unternehmen/README.md) | [`bieter-unternehmen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/bieter-unternehmen.zip) | [Arbeitsprompt](vergaberecht-arbeitsprompt-bieter.md) · [Kurzprompt](vergaberecht-kurzprompt-bieter.md) · [Mini bis 7.500 Zeichen](unified-mini-prompts/bieter-unternehmen.md) | [Bauleistung](testakten/03-bauleistung-stadthalle-musterstadt/README.md) · [IT-Beratung](testakten/04-it-beratung-ministerium-musterland/README.md) · [IT-SIG-2](testakten/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung/README.md) |
| Konkurrent | [`konkurrenten-rechtsschutz`](konkurrenten-rechtsschutz/README.md) | [`konkurrenten-rechtsschutz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/konkurrenten-rechtsschutz.zip) | [Arbeitsprompt](vergaberecht-arbeitsprompt-konkurrenten.md) · [Kurzprompt](vergaberecht-kurzprompt-konkurrenten.md) · [Mini bis 7.500 Zeichen](unified-mini-prompts/konkurrenten-rechtsschutz.md) | [Rechenzentrum](testakten/06-konkurrentenrechtsschutz-rechenzentrum-musterkreis/README.md) · [IT-SIG-2](testakten/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung/README.md) |

## Dateikatalog

Die öffentliche Einbettung, unveränderten Quellen und Build-Befehle sind in [PUBLIC-INTEGRATION.md](PUBLIC-INTEGRATION.md) dokumentiert. Installierbar sind nur die Rollen-Plugin-ZIPs. Quellcode- und Komplettarchive dienen der Dokumentation und Entwicklung, nicht der Plugin-Installation.

### Optionaler externer Entwicklungshelfer

`scripts/llm-judge-eval.py` gehört ausschließlich zur Entwicklung, ist kein Installationsschritt und wird nicht in die Plugin-ZIPs aufgenommen. Beim gesonderten Aufruf mit eingerichtetem SDK und API-Schlüssel übermittelt der Helfer die eingelesene Ausgabedatei und die Prüfkriterien an einen externen API-Dienst. Das kann Kosten auslösen. Keine vertraulichen oder personenbezogenen Inhalte ohne geklärte Berechtigung und Datenschutzgrundlage übermitteln. Die lokalen Validatoren und Smoke-Tests benötigen diesen externen Aufruf nicht.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

Jede Nutzdatei ist über mindestens eine der folgenden Übersichten erreichbar. Der [vollständige GitHub-Dateibaum](https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/vergaberecht-werkstatt) zeigt ausnahmslos alle versionierten Dateien; [`main.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/archive/refs/heads/main.zip) lädt den gesamten Branch herunter.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Bereich | Ansehen und einzeln öffnen | Sammeldownload |
| --- | --- | --- |
| Plugins | [Vergabestelle](vergabestelle-behoerden/README.md) · [Bieter](bieter-unternehmen/README.md) · [Konkurrent](konkurrenten-rechtsschutz/README.md) | [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/alle-plugins-megazip.zip) |
| Alle 255 Skills | [`SKILLS.md`](SKILLS.md) · [Detailseiten je Plugin](skills-index/README.md) mit Browser- und Raw-Link für jede `SKILL.md` | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/alle-skills-markdown.zip) |
| Arbeits- und Werkstattprompts | [Vergabestelle](vergaberecht-arbeitsprompt-vergabestelle.md) · [Bieter](vergaberecht-arbeitsprompt-bieter.md) · [Konkurrent](vergaberecht-arbeitsprompt-konkurrenten.md) | [Einzelne Markdown-Downloads](#arbeits--und-kurzprompts-je-marktseite-einzelne-markdown-dateien) |
| Unified Mini Prompts | [Vergabestelle](unified-mini-prompts/vergabestelle-behoerden.md) · [Bieter](unified-mini-prompts/bieter-unternehmen.md) · [Konkurrent](unified-mini-prompts/konkurrenten-rechtsschutz.md) | [Einzelne Markdown-Downloads](unified-mini-prompts/README.md) |
| Werkstatt-Gesamtprompts | [Vergabestelle](testakten/megaprompts/vergabestelle-behoerden.md) · [Bieter](testakten/megaprompts/bieter-unternehmen.md) · [Konkurrent](testakten/megaprompts/konkurrenten-rechtsschutz.md) | im [`alles-komplettpaket.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/alles-komplettpaket.zip) |
| Testakten | [`testakten/README.md`](testakten/README.md) mit jeder Akte, jedem Gesamt-PDF, Einzel-PDFs und Akten-ZIP | [`testakten-vergaberecht-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakten-vergaberecht-werkstatt.zip) |
| Rechtsprechung und Quellen | [`Leitentscheidungen`](references/leitentscheidungen-anker.md) · [`Netto-Null-Technologien 2026`](references/netto-null-technologien-vergabe-2026.md) · [`VK-Praxis`](references/praxisrechtsprechung-vk-2016-2026.md) · [`Quellenhygiene`](references/quellenhygiene.md) · [`Zitierweise`](references/zitierweise.md) · [`Veröffentlichungswege`](references/veroeffentlichungswege.md) | im [`main.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/archive/refs/heads/main.zip) |
| Ausgabe- und Arbeitsstandard | [`OUTPUT-FORMAT.md`](references/OUTPUT-FORMAT.md) · [`Bestangebot`](references/zuschlag-nicht-nur-preis.md) | im [`main.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/archive/refs/heads/main.zip) |
| Entwicklung und Prüfung | [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`Smoke-Tests`](tests/smoke-tests.md) · [`Skripte`](scripts/) · [`Release-Workflow`](.github/workflows/release-plugin-zips.yml) | [`main.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/archive/refs/heads/main.zip) |

Schwellenwerte, Wertgrenzen, Aktenzeichen, Fundstellen und Fristen sind vor Verwendung anhand amtlicher Quellen live zu verifizieren. Bei abweichenden Formvorgaben einer Vergabestelle, Vergabekammer oder eines Gerichts haben deren Vorgaben Vorrang.

<!-- END top-readme-intro (manual) -->

<!-- BEGIN top-readme-downloads-section (autogen) -->

## Sofort-Downloads

Die Links in der Spalte `Herunterladen` sind stabile Release-Downloads und gehören zum angegebenen Komponentenstand. Links in der Spalte `Ansehen` öffnen dagegen die jeweilige Datei oder Übersicht im Browser.

### Alles mit einem Klick

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Paket | Inhalt | Herunterladen |
| --- | --- | --- |
| Vollständiges Quellarchiv (nicht installierbar) | Komponentenquellen unter `vergaberecht-werkstatt/`, einschließlich Prompts, Testakten, Audits, Skripten und Lizenzen; README.txt mit Warnhinweis | [`alles-komplettpaket.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/alles-komplettpaket.zip) |
| Quellcode | Vollständiger Stand des Branches `main` | [`main.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/archive/refs/heads/main.zip) |
| Prüfsummen | SHA-256-Prüfsummen aller Release-Dateien | [`checksums-sha256.txt`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/checksums-sha256.txt) |
| Release-Seite | Versionshinweise, Einzeldateien und Quellcode-Snapshots | [Komponenten-Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/vergaberecht-werkstatt-v445.33.1) |

### Welche Datei brauche ich?

| Lage | Einstieg | Link |
| --- | --- | --- |
| Ich suche eine bestimmte Repo-Datei | Vollständigen Dateikatalog oder GitHub-Dateibaum öffnen | [Dateikatalog](#dateikatalog) |
| Ich arbeite in Claude Desktop oder Cowork | Rollenpassendes Plugin-ZIP in `Customize`, `Plugins`, `+` hochladen | [Plugin-ZIPs](#plugins-installation) |
| Ich arbeite in Claude Code | Repo als Marketplace hinzufügen und genau ein Rollenplugin installieren | [Installationsbefehle](#plugins-installation) |
| Ich arbeite ohne Plugin in einem normalen Chatbot | Arbeitsprompt als empfohlene Vollfassung anhängen | [Arbeitsprompts](#arbeits--und-kurzprompts-je-marktseite-einzelne-markdown-dateien) |
| Mein Chat hat wenig Kontextplatz | Rollenpassenden Unified Mini Prompt anhängen | [Mini-Prompts](unified-mini-prompts/README.md) |
| Ich will nur einzelne Spezialfähigkeiten nutzen | Skills-Markdown-ZIP nehmen oder einzelne `SKILL.md` aus dem Index öffnen | [SKILLS.md](SKILLS.md) |
| Ich will realistische Unterlagen testen | Testakte als ZIP laden oder Gesamt-PDF lesen | [Testakten](testakten/README.md) |
| Ich prüfe Release- oder Marketplace-Fähigkeit | Validatoren und Smoke-Tests ausführen | [tests/smoke-tests.md](tests/smoke-tests.md) |

<a id="plugins-installation"></a>

### Plugins für Claude Code, Desktop und Cowork

In Claude Code zuerst einmal `/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht` ausführen, danach `/plugin install [plugin-name]@klotzkette-german-legal-skills` und `/reload-plugins`. In Claude Desktop oder Cowork das Plugin-ZIP über `Customize`, `Plugins`, `+` hochladen. Danach weder einen Arbeitsprompt zusätzlich laden noch einen Skill auswählen: Fallunterlagen anhängen und den Startsatz oben senden. [Offizielle Installationshinweise](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

| Plugin | Rolle | Zweck | Ansehen | Plugin-ZIP | Skills-ZIP | Mini-Prompt |
| --- | --- | --- | --- | --- | --- | --- |
| vergabestelle-behoerden | Vergabestelle | Verfahren planen, Bestangebot gestalten, werten, dokumentieren und verteidigen | [README](vergabestelle-behoerden/README.md) | [`vergabestelle-behoerden.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergabestelle-behoerden.zip) | [`vergabestelle-behoerden-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergabestelle-behoerden-skills-markdown.zip) | [`vergabestelle-behoerden-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergabestelle-behoerden-unified-mini-prompt.md) |
| bieter-unternehmen | Bieter | Unterlagen prüfen, Angebot bauen, Qualitätsvorsprung belegen und Rechtsschutz führen | [README](bieter-unternehmen/README.md) | [`bieter-unternehmen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/bieter-unternehmen.zip) | [`bieter-unternehmen-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/bieter-unternehmen-skills-markdown.zip) | [`bieter-unternehmen-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/bieter-unternehmen-unified-mini-prompt.md) |
| konkurrenten-rechtsschutz | Konkurrent | Billigzuschlag, Unterlagen, Wertung, Eignung und De-facto-Lagen angreifen | [README](konkurrenten-rechtsschutz/README.md) | [`konkurrenten-rechtsschutz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/konkurrenten-rechtsschutz.zip) | [`konkurrenten-rechtsschutz-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/konkurrenten-rechtsschutz-skills-markdown.zip) | [`konkurrenten-rechtsschutz-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/konkurrenten-rechtsschutz-unified-mini-prompt.md) |
| Alle Plugins zusammen | alle | Komplettpaket der installierbaren Arbeitsumgebung | [`SKILLS.md`](SKILLS.md) | [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/alle-plugins-megazip.zip) | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/alle-skills-markdown.zip) | [Einzelne Markdown-Dateien](unified-mini-prompts/README.md) |

### Arbeits- und Kurzprompts je Marktseite (einzelne Markdown-Dateien)

Jeder Prompt ist eine einzelne `.md`-Datei zum direkten Datei-Download. In jedem Chatbot (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat, Perplexity, Claude) als Anhang nutzbar oder per Copy & Paste.
Der Kurzprompt ist ein ausführlicher Fachworkflow ohne starres Zeichenlimit. Nur der Unified Mini Prompt ist auf höchstens 7.500 Zeichen begrenzt.
Diese Prompts sind eigenständige Alternativen für Chats ohne Plugin; bei installiertem Plugin werden sie nicht zusätzlich benötigt.

| Prompt | Inhalt | Direkt-Download |
| --- | --- | --- |
| Vergaberecht-Arbeitsprompt - Vergabestelle | Vollworkflow für öffentliche Auftraggeber | [`vergaberecht-arbeitsprompt-vergabestelle.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergaberecht-arbeitsprompt-vergabestelle.md) |
| Vergaberecht-Arbeitsprompt - Bieter | Vollworkflow für Bieter, Bewerber, Kanzleien | [`vergaberecht-arbeitsprompt-bieter.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergaberecht-arbeitsprompt-bieter.md) |
| Vergaberecht-Arbeitsprompt - Konkurrenten | Vollworkflow für Konkurrentenrechtsschutz, Nachprüfung, OLG | [`vergaberecht-arbeitsprompt-konkurrenten.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergaberecht-arbeitsprompt-konkurrenten.md) |
| Vergaberecht-Kurzprompt - Vergabestelle | Kompakter Fachworkflow für die Vergabestelle ohne 7.500-Zeichenlimit | [`vergaberecht-kurzprompt-vergabestelle.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergaberecht-kurzprompt-vergabestelle.md) |
| Vergaberecht-Kurzprompt - Bieter | Kompakter Fachworkflow für Bieter und Bewerber ohne 7.500-Zeichenlimit | [`vergaberecht-kurzprompt-bieter.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergaberecht-kurzprompt-bieter.md) |
| Vergaberecht-Kurzprompt - Konkurrenten | Kompakter Fachworkflow für Konkurrentenrechtsschutz ohne 7.500-Zeichenlimit | [`vergaberecht-kurzprompt-konkurrenten.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergaberecht-kurzprompt-konkurrenten.md) |
| Unified Mini Prompt — vergabestelle-behoerden | Verdichteter Workflow bis 7.500 Zeichen | [`vergabestelle-behoerden-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/vergabestelle-behoerden-unified-mini-prompt.md) |
| Unified Mini Prompt — bieter-unternehmen | Verdichteter Workflow bis 7.500 Zeichen | [`bieter-unternehmen-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/bieter-unternehmen-unified-mini-prompt.md) |
| Unified Mini Prompt — konkurrenten-rechtsschutz | Verdichteter Workflow bis 7.500 Zeichen | [`konkurrenten-rechtsschutz-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/konkurrenten-rechtsschutz-unified-mini-prompt.md) |

### Testakten (anonymisierte Demonstrations-Vergabeakten)

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Aktenübersicht | PDF ansehen | PDF herunterladen | Akten-ZIP | Einzel-PDF-ZIP |
| --- | --- | --- | --- | --- | --- |
| Testakte 01 - Reinigungsdienstleistung Grundschule Musterstadt (`01-reinigung-grundschule-musterstadt`) | [`README`](testakten/01-reinigung-grundschule-musterstadt/README.md) | [Gesamt-PDF](testakten/01-reinigung-grundschule-musterstadt/gesamt-pdf/01-reinigung-grundschule-musterstadt_gesamt.pdf) | [`01-reinigung-grundschule-musterstadt_gesamt.pdf`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/01-reinigung-grundschule-musterstadt_gesamt.pdf) | [`testakte-01-reinigung-grundschule-musterstadt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-01-reinigung-grundschule-musterstadt.zip) | [`testakte-01-reinigung-grundschule-musterstadt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-01-reinigung-grundschule-musterstadt-einzelpdfs.zip) |
| Testakte 02 - Laptopbeschaffung Landesamt Musterland (`02-laptopbeschaffung-landesamt-musterland`) | [`README`](testakten/02-laptopbeschaffung-landesamt-musterland/README.md) | [Gesamt-PDF](testakten/02-laptopbeschaffung-landesamt-musterland/gesamt-pdf/02-laptopbeschaffung-landesamt-musterland_gesamt.pdf) | [`02-laptopbeschaffung-landesamt-musterland_gesamt.pdf`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/02-laptopbeschaffung-landesamt-musterland_gesamt.pdf) | [`testakte-02-laptopbeschaffung-landesamt-musterland.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-02-laptopbeschaffung-landesamt-musterland.zip) | [`testakte-02-laptopbeschaffung-landesamt-musterland-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-02-laptopbeschaffung-landesamt-musterland-einzelpdfs.zip) |
| Testakte 03 - Bauleistung Sanierung Stadthalle Musterstadt (Bieterseite) (`03-bauleistung-stadthalle-musterstadt`) | [`README`](testakten/03-bauleistung-stadthalle-musterstadt/README.md) | [Gesamt-PDF](testakten/03-bauleistung-stadthalle-musterstadt/gesamt-pdf/03-bauleistung-stadthalle-musterstadt_gesamt.pdf) | [`03-bauleistung-stadthalle-musterstadt_gesamt.pdf`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/03-bauleistung-stadthalle-musterstadt_gesamt.pdf) | [`testakte-03-bauleistung-stadthalle-musterstadt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-03-bauleistung-stadthalle-musterstadt.zip) | [`testakte-03-bauleistung-stadthalle-musterstadt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-03-bauleistung-stadthalle-musterstadt-einzelpdfs.zip) |
| Testakte 04 - IT-Beratung Ministerium Musterland (Bieterseite, Verhandlungsverfahren) (`04-it-beratung-ministerium-musterland`) | [`README`](testakten/04-it-beratung-ministerium-musterland/README.md) | [Gesamt-PDF](testakten/04-it-beratung-ministerium-musterland/gesamt-pdf/04-it-beratung-ministerium-musterland_gesamt.pdf) | [`04-it-beratung-ministerium-musterland_gesamt.pdf`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/04-it-beratung-ministerium-musterland_gesamt.pdf) | [`testakte-04-it-beratung-ministerium-musterland.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-04-it-beratung-ministerium-musterland.zip) | [`testakte-04-it-beratung-ministerium-musterland-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-04-it-beratung-ministerium-musterland-einzelpdfs.zip) |
| Testakte 05: Insolvenz und Auftragnehmerwechsel nach § 132 GWB (`05-insolvenz-auftragnehmerwechsel-132-gwb`) | [`README`](testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/README.md) | [Gesamt-PDF](testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/gesamt-pdf/05-insolvenz-auftragnehmerwechsel-132-gwb_gesamt.pdf) | [`05-insolvenz-auftragnehmerwechsel-132-gwb_gesamt.pdf`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/05-insolvenz-auftragnehmerwechsel-132-gwb_gesamt.pdf) | [`testakte-05-insolvenz-auftragnehmerwechsel-132-gwb.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-05-insolvenz-auftragnehmerwechsel-132-gwb.zip) | [`testakte-05-insolvenz-auftragnehmerwechsel-132-gwb-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-05-insolvenz-auftragnehmerwechsel-132-gwb-einzelpdfs.zip) |
| Testakte 06 - Konkurrentenrechtsschutz Rechenzentrum Musterkreis (`06-konkurrentenrechtsschutz-rechenzentrum-musterkreis`) | [`README`](testakten/06-konkurrentenrechtsschutz-rechenzentrum-musterkreis/README.md) | [Gesamt-PDF](testakten/06-konkurrentenrechtsschutz-rechenzentrum-musterkreis/gesamt-pdf/06-konkurrentenrechtsschutz-rechenzentrum-musterkreis_gesamt.pdf) | [`06-konkurrentenrechtsschutz-rechenzentrum-musterkreis_gesamt.pdf`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/06-konkurrentenrechtsschutz-rechenzentrum-musterkreis_gesamt.pdf) | [`testakte-06-konkurrentenrechtsschutz-rechenzentrum-musterkreis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-06-konkurrentenrechtsschutz-rechenzentrum-musterkreis.zip) | [`testakte-06-konkurrentenrechtsschutz-rechenzentrum-musterkreis-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-06-konkurrentenrechtsschutz-rechenzentrum-musterkreis-einzelpdfs.zip) |
| IT-Sicherheitsvergabe Landeshauptstadt Schwerin - Nachprüfungsverfahren (`it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung`) | [`README`](testakten/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung/README.md) | [Gesamt-PDF](testakten/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung/gesamt-pdf/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung_gesamt.pdf) | [`it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung_gesamt.pdf`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung_gesamt.pdf) | [`testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung.zip) | [`testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakte-it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung-einzelpdfs.zip) |
| Alle Testakten zusammen | [`testakten/README.md`](testakten/README.md) | — | — | [`testakten-vergaberecht-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/testakten-vergaberecht-werkstatt.zip) | - |

### Konfiguration und Einzel-Skills

- Marketplace-Manifest für Claude Code: [`marketplace.json`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/marketplace.json)
- Pro Skill ein eigener Download: siehe [`SKILLS.md`](SKILLS.md) (Gesamtübersicht) oder die [Plugin-Detailseiten](skills-index/README.md). Jede `SKILL.md` ist als `[Raw .md]`-Link verfügbar und einzeln abrufbar.
- Vollständige Asset-Prüfliste: [`checksums-sha256.txt`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/checksums-sha256.txt).

---

<!-- END top-readme-downloads-section (autogen) -->

## Rechtsregime

### Oberhalb EU-Schwellenwert

- GWB Teil 4 (§§ 97 ff. GWB)
- VgV (Liefer- und Dienstleistungsaufträge)
- SektVO (Sektorenbereiche Wasser Energie Verkehr Post)
- KonzVgV (Konzessionsvergabe)
- VSVgV (Verteidigung und Sicherheit)
- VOB/A Abschnitt 2 und 3 (Bauleistungen)

Nachprüfung vor Vergabekammern Bund/Land § 156 GWB und vor OLG-Vergabesenaten § 171 GWB.

### Unterhalb EU-Schwellenwert

- BHO/LHO § 55 und UVgO (Bund)
- Landesrechtliche Vergabegesetze (z.B. Hessisches Vergabegesetz, Bayerisches Mittelstandsgesetz)
- VOB/A Abschnitt 1 (Bauleistungen Unterschwelle)

Unterhalb der EU-Schwellenwerte besteht kein bundesweit einheitliches Nachprüfungsverfahren nach §§ 155 ff. GWB. Je nach Bundesland und Auftraggeber kommen jedoch landesrechtliche Nachprüfungsstellen, vergaberechtliche Informations- und Wartepflichten, zivil- oder verwaltungsgerichtlicher Eilrechtsschutz, Aufsicht, Fördermittelkontrolle und Schadensersatz in Betracht. BVerfG, Beschluss vom 13.06.2006, 1 BvR 1160/03, verneint eine verfassungsrechtliche Pflicht zu einem besonderen vergaberechtlichen Primärrechtsschutz; der konkrete Rechtsweg ist damit nicht pauschal ausgeschlossen.

### Aktuelle EU-Schwellenwerte

Schwellenwerte werden alle zwei Jahre angepasst. Für 2026/2027 gilt die Delegierte Verordnung (EU) 2025/2152 für klassische Vergaben, 2025/2150 für Sektoren, 2025/2151 für Konzessionen und 2025/2487 für Verteidigungs- und Sicherheitsvergaben. Zuordnung, Geltungszeitraum und Wert live über EUR-Lex und § 106 GWB verifizieren.

## Plugin 1: vergabestelle-behoerden

122 Skills: 30 Kernskills plus verwertete Vertiefungen aus dem Legal-Repo in 8 Phasen:

- Phase A — Bedarf und Schätzung (3 Skills): Bedarfsermittlung, Auftragswertschätzung, Schwellenwertprüfung
- Phase B — Verfahrenswahl (3 Skills): Verfahrensart, Bekanntmachung, Eignung- und Zuschlagskriterien
- Phase C — Unterlagen (7 Skills): Vergabeunterlagen, Leistungsbeschreibung, ESPD, Zuschlagsmatrix, Bestangebot-Durchsetzung, LV-/Datenformate, Legacy-Systeme-Integration
- Phase D — Verfahrensdurchführung (4 Skills): Eignungsprüfung, Ausschluss, Angebotsöffnung, Aufklärung niedriger Preise
- Phase E — Wertung (4 Skills): Rechnerische und formelle Prüfung, Wertung, Wertungsvermerk
- Phase F — Zuschlag (3 Skills): Vorabinformation § 134 GWB, Zuschlag, Aufhebung
- Phase G — Nachprüfung (3 Skills): Rügeerwiderung, Stellungnahme VK, Beschwerdeerwiderung OLG
- Phase H — Dokumentation Querschnitt (8 Skills): Vergabevermerk § 8 VgV, Akteneinsicht, Selbstreinigung, Vergabesperre, Fristberechnung, Datenschutz, Bekanntmachungs-/Uploadrouting, Insolvenz- und Auftragnehmerwechsel nach § 132 GWB

## Plugin 2: bieter-unternehmen

113 Skills: 30 Kernskills plus verwertete Vertiefungen aus dem Legal-Repo in 8 Phasen:

- Phase A — Markterfassung Go-No-Go (5 Skills): Bekanntmachung lesen, Vergabeunterlagen prüfen, Unterlagen-/LV-Datenformate, Legacy-Systeme-Integration, Go-No-Go
- Phase B — Eignung (5 Skills): Eignungsanforderungen, ESPD, Präqualifikation, Eignungsleihe, Bietergemeinschaft
- Phase C — Angebotsaufbau (7 Skills): Kalkulation, LV bepreisen, Nebenangebote, Referenzen, Konzepte, Qualitätsvorsprung, EU-Erklärungen
- Phase D — Abgabe (4 Skills): Angebot im vorgegebenen Format, Formgerechte Abgabe mit elektronischer Signatur, Fristprüfung, Bietergemeinschaftserklärung
- Phase E — Aufklärung (2 Skills): Aufklärung niedriger Preise § 60, Inhaltsaufklärung § 15
- Phase F — Rüge (3 Skills): Rügefrist 10 Kalendertage, Rügeschreiben, Nicht-Abhilfe-Folgeschritt
- Phase G — Nachprüfung (3 Skills): Nachprüfungsantrag, Eilantrag Zuschlagssperre, sofortige Beschwerde
- Phase H — Vertrag und Querschnitt (6 Skills): Zuschlagsannahme, Vertragsanpassung § 132 GWB, Insolvenz- und Auftragnehmerwechsel, Selbstreinigung, Schadensersatz, Datenschutz

## Plugin 3: konkurrenten-rechtsschutz

20 Skills als fokussierte Streit-Workbench für unterlegene Bieter, Wettbewerber und Zuschlagsgegner:

- Start und Routing: Startbildschirm, Rollenklärung, Fristenampel, Zielauswahl und Output-Menü.
- Unterlagen und Formate: Bekanntmachung, Vergabeunterlagen, LV, GAEB/XML/Excel/PDF, Legacy-IT, SAP/ERP/AVA/DMS, MCP, Portalprotokolle und Belegmatrix prüfen.
- Rüge und Nachprüfung: Rüge nach § 160 GWB, Nichtabhilfe, Nachprüfungsantrag, Zuschlagssperre, De-facto-Vergabe und Akteneinsicht.
- Angriffslinien: Billigzuschlag, Wertung, Dokumentation, Eignung des Zuschlagsprätendenten, Ausschlussgründe, Produktneutralität und Leistungsbeschreibung.
- Eskalation und Risiko: OLG-Beschwerde, Vergleichsfenster, Abstellungsstrategie, Kosten- und Schadensersatzrisiko.

## Testakten

Testakten mit vollständigen Vergabeunterlagen, Bieterunterlagen und Streitakten. Anonymisierte Beispiele aus realistischen Branchen (Reinigungsdienstleistung, IT-Beschaffung, Bauleistungen, Beratungsleistung, Rechenzentrumsbetrieb) sowie eine umfangreiche IT-SIG-2-Nachprüfungsakte für die Marktrollen.

## Dashboard- und Applet-Arbeitsweise

Alle drei Plugins sind als geführte Workbench angelegt. Bei komplexen Vergaben oder Streitfällen sollen sie nicht mit langen allgemeinen Erläuterungen starten, sondern mit einem kompakten Arbeitsdashboard:

- Fristenampel für Angebotsfrist, Rüge, § 134 GWB, Nichtabhilfe, Zuschlagssperre, OLG-Beschwerde und § 135 GWB.
- Startbildschirm mit fünf Eingaben: Was liegt vor, welche Rolle, welcher Verfahrensstand, welches Ziel, welcher Output.
- Antwortstandard für umfangreiche Fälle: Kurzlage, rote Fristen, Arbeitsdashboard, Output-Auswahl.
- Schnellwahl für typische Lagen wie unklare Unterlagen, Rüge, Wertungsangriff, Zuschlagsblockade, Akteneinsicht und Upload.
- Dokumentenmatrix für Bekanntmachung, Vergabeunterlagen, LV/GAEB/XML/Excel/PDF, Legacy-IT, SAP/ERP/AVA/DMS, MCP, Angebot, Wertung, Portalprotokolle und Anlagen.
- Belegmatrix für Behauptung oder Behördenentscheidung, Aktenstelle, Datei, Seite/Position, Gegenargument und Replik.
- Angriffs-/Verteidigungslinien mit Tatsache, Norm, Beleg, Kausalität, Zuschlagschance, Abhilfe und Gegenargument.
- Wertungsmatrix für Kriterium, Gewicht, Bewertung, Dokumentation, Fehlerverdacht, Reparaturpfad und Zuschlagschance.
- Rollenfester Systemcheck: Vergabestellen verbinden Bauwerk, PMS/BMS, Planung/BIM, Kosten, Termine, Umwelt, Normen und Vergabeakte über Feldautorität und Entscheidungsbrücke; Bieter verbinden ERP/AVA, Technik, Personal, Referenzen und Nachweise über Source-to-Offer-Mapping und Angebotsfreeze; Konkurrenten sichern Portal- und Systembelege über Herkunftszone, Tatsachenkern, Gegenhypothese und Akteneinsichtsziel.
- Legacy-/MCP-Integrationscheck für SAP, ERP, CRM, AVA, DMS, SIB-Bauwerke, Heller/PMS, EPING, BIM/IFC, OKSTRA, SFTP/API, OData, IDoc, CSV/JSON/XML, Hash, Mapping, Delta, Freigabe und Rückkanal.
- Upload-/Formatexport-Check für GAEB/XML/Excel/PDF/ZIP, eForms/TED/DVAL, Portalnachweise, Hashes und Freigabe.
- VK-/OLG-Streitdashboard für Nachprüfungsantrag, Eilantrag, Akteneinsicht, Schwärzung, Beiladung, Vergleich, Beschwerde und Kostenrisiko.
- Output-Weiche für Schriftsatz, Vergabevermerk, Gremienvorlage, Uploadauftrag, Vergleichsvorschlag, Schadensersatzmemo oder Angebotspaket.

## Validatoren

```bash
python3 -m pip install -r requirements-dev.txt
node scripts/validate-plugin-structure.mjs
python3 scripts/validate-yaml-frontmatter.py
python3 scripts/validate-skill-discovery.py
python3 scripts/sync-references.py --check
python3 scripts/validate-rechtsstand-2026.py
python3 scripts/validate-system-integration.py
python3 scripts/run-smoke-tests.py
```

Die Prüfungen sichern Manifest und Marketplace, Skill-Frontmatter und Routing, synchrone Kernreferenzen, den Rechtsstand 2026, die drei rollenspezifischen Systemverträge sowie die vollständigen Smoke-Tests.

## Quellenhygiene

- Keine Blindzitate aus BeckRS Kommentaren Aufsätzen
- Rechtsprechung nur mit Aktenzeichen + Datum + Verfahrensbezeichnung
- Schwellenwerte 2026/2027 nach VO (EU) 2025/2152 klassisch, 2025/2150 Sektoren, 2025/2151 Konzessionen und 2025/2487 Verteidigung/Sicherheit live verifizieren
- Bei Unsicherheit: Lückenliste statt Erfindung

## Anker-Rechtsprechung

Siehe `references/leitentscheidungen-anker.md`. Wichtigste Anker:

- EuGH 28.10.1999 C-81/98 Alcatel Austria — Vorabinformation § 134 GWB
- EuGH 24.10.2018 C-124/17 Vossloh Laeis — Selbstreinigung § 125 GWB
- EuGH 17.11.2022 C-54/21 Antea Polska — Vertraulichkeit und Akteneinsicht
- EuGH 14.01.2016 C-234/14 Ostas celtnieks — Eignungsleihe § 47 VgV
- EuGH 16.01.2025 C-424/23 DYKA Plastics — technische Spezifikationen, Produktneutralität, Gleichwertigkeit
- EuGH 16.04.2026 C-568/24 Sof Medica — technische Typvorgaben, Gleichwertigkeitszugang und Verhältnismäßigkeit
- EuGH 03.07.2025 C-534/23 P und C-539/23 P Instituto Cervantes — EU-Eigenvergabe; Integritätsanker für den unveränderbaren Angebotszustand bei vorgeschriebenem Upload
- EuGH 09.01.2025 C-578/23 Generální finanční ředitelství — Verfahren ohne vorherige Bekanntmachung und Lock-in
- EuGH 22.01.2026 C-590/24 AK Dlhopolec u. a. — verhältnismäßige Geldbuße; keine Sachentscheidung zum Vergabeausschluss
- EuGH 05.02.2026 C-810/24 Urban Vision — kein nachträgliches Matching-Privileg eines privaten Projektinitiators
- EuGH 09.07.2026 C-186/25 Institut po ribni resursi Varna — EU-Fördervergaben, Vertragsvollzug und individualisierte Finanzkorrektur
- BwBBG seit 14.02.2026 — eigenes Anwendungs-, Drittstaaten-, Rechtsschutz- und Vertragsänderungsgate für Bundeswehrbeschaffungen; [Arbeitsreferenz](references/bundeswehrbeschaffung-bwbbg-2026.md)
- EuGH 16.10.2025 C-282/24 Polismyndigheten und EuGH 29.04.2025 C-452/23 Fastned Deutschland — Vertrags-/Konzessionsänderungen
- EuGH 04.07.2013 C-100/12 Fastweb, EuGH 05.04.2016 C-689/13 PFE und EuGH 21.12.2021 C-497/20 Randstad Italia — Konkurrentenrechtsschutz
- BGH 31.01.2017 X ZB 10/16 — Aufklärung ungewöhnlich niedriger Angebote
- BGH 08.12.2020 XIII ZR 19/19 — Schadensersatz bei rechtswidriger Aufhebung
- BVerfG 13.06.2006 1 BvR 1160/03 — Unterschwellenrechtsschutz
- OLG Düsseldorf 10.07.2024 Verg 2/24 — Bestandskompatibilität, Systemsicherheit und dokumentierte Umstellungsrisiken
- OLG Düsseldorf 13.05.2019 Verg 47/18 — vollständiger und unmittelbarer elektronischer Zugang zu Vergabeunterlagen
- OLG Düsseldorf 24.03.2021 Verg 34/20 — konkrete Begründung qualitativer Wertungen statt bloßer Punktzahlen
- OLG Düsseldorf 12.06.2024 Verg 36/23 — Tatsachenkern und plausible Erkenntnisgrundlage bei begrenzter Einsicht

## Lizenz

Dual-lizenziert MIT und Apache-2.0. Siehe LICENSE, LICENSE-MIT, LICENSE-APACHE, NOTICE.

## Status

Aktueller Stand: **Version 445.33.1**.

- **Drei Rollen:** Vergabestelle, Bieter und Konkurrent mit eigenen Skills, Testakten, Werkstatt- und Schnellstartprompts sowie VK-/OLG-Streitworkflows.
- **Systempfade:** GAEB, XML, Excel, PDF, SIB, PMS, BIM, OKSTRA, SAP, ERP, AVA, DMS, API, MCP, eForms, TED und DVAL mit Originalschutz, Mapping, Hash, Delta, Freigabe und Rückkanal.
- **Rechtsstand:** GWB-Fassungen werden über § 187 Abs. 2 GWB nach Einleitungsdatum getrennt. Das seit 14. Februar 2026 geltende BwBBG, die Bundes-Verwaltungsvorschriften vom 18. Juni 2026 sowie EuGH C-590/24, C-810/24 und C-186/25 sind mit Anwendungs- und Übertragungsgrenzen eingebaut. Art. 25 VO (EU) 2024/1735 und VO (EU) 2026/718 bleiben als eigene Netto-Null-Pflichtschicht erhalten; C-268/25 bleibt korrekt als Schlussanträge, die UVgO-Neufassung vom 30.06.2026 als Entwurf gekennzeichnet.
- **Zugriff:** Dateikatalog, Rollenmenüs sowie Einzel- und Sammeldownloads erschließen sämtliche Arbeitsmittel. Prüfprotokolle: [`Bug Hunt v2.10.0`](audits/BUG-HUNT-v2.10.0.md), [`Sweep 2026-07-15`](audits/MIKROBUG-USABILITY-SWEEP-2026-07-15.md) und [`100/100-Sweep 2026-07-26`](audits/MIKROBUG-USABILITY-SWEEP-2026-07-26.md).

### Änderungslog (Patches)

- v445.33.1 — Rechtsstand August 2026 ergänzt: Drei rollenfeste Skills operationalisieren das seit 14. Februar 2026 geltende BwBBG mit Anwendungsbereich, §-19-Übergang, punktuellen Verfahrens- und Losregeln, Drittstaatenzugang, Vorab-Rüge, VK Bund, OLG, alternativen Sanktionen und Vertragsänderung. Der redaktionell inkonsistente Verweis in § 16 Abs. 4 auf einen nicht vorhandenen § 15 Abs. 7 wird ausdrücklich offengehalten. EuGH C-590/24, C-810/24 und C-186/25 sind mit präzisen Negativgrenzen in Ausschluss-, Konzessions-, Fördermittel-, Wertungs- und Rechtsschutzworkflows eingebaut. Die drei Bundes-Verwaltungsvorschriften BAnz AT 18.06.2026 B3 bis B5 ergänzen den Bundes-Wertgrenzencheck. Routing, autarke Werkstatt- und Schnellstartprompts, Referenzen und Regressionstests wurden auf 255 Skills aktualisiert.
- v2.18.0 — Null-Konfigurations-Start für alle drei Marktrollen: Ein rollenpassendes Plugin, ein Fallordner und ein fertiger Startsatz genügen; zusätzliche Prompts, Skillnamen und Outputwahl entfallen. Orchestratoren, Arbeits-, Kurz-, Werkstatt- und Mini-Prompts liefern zunächst einen einheitlichen Fünf-Zeilen-Stand, arbeiten mit gekennzeichneten Annahmen weiter und bündeln höchstens drei echte Blockerfragen am Ende. Ein Routingbudget aus Orchestrator plus höchstens drei Fachskills pro Durchgang reduziert Kontextlast, verbessert die Skilltreffer und hält Großakten durch sichtbare Checkpoints fortsetzbar. Rollen-READMEs trennen den ZIP-Upload in Claude Desktop/Cowork korrekt von der Marketplace-Installation in Claude Code, klappen Spezialdownloads und Testakten ein und zeigen wieder die korrekten Skillzahlen. Neue Usability-Regressionen sperren Startsatz-, Prompt-Autarkie-, Skillzahl-, Routingbudget- und Fünf-Zeilen-Rückfälle.
- v2.17.0 — Rechtsstand und Startlogik auf Sommer 2026 aktualisiert: Drei rollenfeste Skills operationalisieren Art. 25 VO (EU) 2024/1735 und VO (EU) 2026/718 mit Richtlinien-/Technologiegate, 70-Prozent-Rezyklierbarkeit von Windrotorblättern, Bau-Zusatzpflichten, Resilienz-/Kommissionsfeststellung, GPA, Ausnahmen, Nachweisen und passender Rechtsfolge. EuGH C-856/24, Sad Trasporto Locale II, steuert die getrennte Prüfung von Betriebsrisiko, ÖPNV-Sonderroute und allgemeinem Inhouse-Recht. Der UVgO-Vorschlag vom 30.06.2026 ist ausdrücklich nur als Entwurf gesperrt. Ein bisher unentdeckter Regelfallfehler bei offenem beziehungsweise öffentlichem Verfahren wurde in Prompt, Skill und lebensnaher Testakte beseitigt und durch eine breitere Regression gesichert. Routing, autarke Prompts, Referenzen, Übersichten und Releasepakete führen unmittelbar in die neuen Arbeitswege.
- v2.16.0 — Beweisprüfung, Quellenübertragung und Aktenzugriff gehärtet: Alle 115 nummerierten Aktenstücke sind aus ihrer jeweiligen Fallübersicht direkt erreichbar; der Navigationsvalidator wertet echte Markdown-Links aus und sperrt fehlende Aktenlinks sowie abweichende Gesamtzahlen. Die sieben Fallrubriken prüfen nun mit 85 automatisierten Kontrollen auch Objektbegehung, Formelfehler, Servicefälle, PDF-/GAEB-Abgleich, Reaktionssimulation, Lizenz- und Eignungskontinuität, Failover-Indizien, Referenzmaßstab sowie Einzel- und Konsenswertung. Vergabestelle, Bieter und Konkurrent arbeiten mit einem rollenspezifischen Zitier- und Falltransfer-Gate aus Quellenstatus, Aussagegehalt, Bindungsstatus, Vergleichstatsachen, Übertragungsgrenze, Beleganschluss und vollziehbarer Rechtsfolge; Vorab-Rügen bleiben ohne fertiges Angebot möglich, anhängige Verfahren erzeugen keinen vermeintlichen Rechtssatz und unverifizierte Fundstellen bleiben Rechercheaufträge. Die in BGH X ZB 4/10, Rn. 73, als gerichtlicher Hinweis entwickelte und von OLG Düsseldorf VII-Verg 28/14 als obiter dictum eingeordnete sowie angewandte Linie steuert die fallbezogene Heilung von Dokumentationsmängeln ohne neue Entscheidung oder manipulative Tatsachen. Werkstattprompts liegen nun nachweisbar im Prompt-Sammelarchiv und Komplettpaket; der ZIP-Validator blockiert veraltete Manifestkopien und unvollständige Promptpakete.
- v2.15.0 — Beweisnähe und juristische Argumentationsführung vertieft: Acht neue Aktenstücke ergänzen alle sieben Testakten um Objektaufmaß, Personalbedarfsrechnung, Service-Kontrollfälle, GAEB-/Bestandsaufmaß, Reaktionssimulation, Closing- und Lizenztransfer, Failover-Monitoring, Referenzrückrufe sowie Einzel- und Konsenswertung. Alle Stücke liegen als realistisch gesetzte DOCX-, XLSX- und Einzel-PDF-Fassungen vor und sind in die Gesamt-PDFs integriert. Die drei Rollen-Orchestratoren und die zentralen Schriftsatzskills arbeiten nun mit geschlossenen Argumentationsketten aus Norm, bekannt gemachter Regel, Tatsache, Beleg, Rechtsverletzung, Zuschlagschance, Gegenargument und Rechtsfolge. BGH X ZB 3/17 sowie OLG Düsseldorf Verg 34/20 und Verg 36/23 steuern Qualitätswertung, Dokumentation und Tatsachenvortrag; visuelle Satzprüfungen beseitigen isolierte Rest- und Leerseiten.
- v2.14.0 — 100 Mikrodefekte und 100 Bedienflächen systematisch geprüft und verbessert: alle Gesamt-PDFs besitzen fachliche Metadaten, Aktenstück-Lesezeichen und eine automatische Lesezeichenansicht; 166 Einzel-PDFs sowie sämtliche Office- und Scan-Artefakte tragen verständliche Titel, Betreffe, Autoren und Aktenzeichen. Ressourcenlimits, transaktionaler PDF-Bau und neue Schlussseitenprüfungen verhindern Überläufe, Hänger und isolierte Restzeilen. 90 DOCX-Dateien wurden in 130 Seiten, 45 XLSX-Dateien in 134 Druckseiten und alle Präsentations-/Scan-Fassungen vollständig gerendert. Die unscharfe Bestandsdateierkennung wurde durch vier explizite Gegenstücke ersetzt; dadurch stehen Beiladungs- und OLG-Beschluss der IT-SIG-2-Akte nun auch als eigenständige Word-Dateien bereit. Präsentationstabellen erhalten fachliche Titel und kontrollierte Fortsetzungsfolien. Vollständige Bilanz: [`100/100-Sweep 2026-07-26`](audits/MIKROBUG-USABILITY-SWEEP-2026-07-26.md).
- v2.13.0 — Testaktenketten bis zur belastbaren Umsetzung vervollständigt: 17 zusätzliche Aktenstücke und zwei realistisch neu gefasste Dokumente bilden Aktenvorlage, VK-Stellungnahme und -Beschluss, OLG-Beschwerde und -Entscheidung, Neuwertung, erneutes §-134-Schreiben, Kostenentscheidung, Rückversetzung, Änderungsbekanntmachung, Vergleichsumsetzung sowie Auftragnehmerwechsel und Monitoring ab. Die Beschwerdekette der Vergabekammer Westfalen ist korrekt dem Vergabesenat des OLG Düsseldorf zugeordnet. Ein neuer Falllogikvalidator prüft Nummernfolgen, README-Verlinkung, §-134-Mindestangaben und Stillhaltefrist, Rechtsschutzchronologie, Beschwerdegericht, GAEB-Positionen sowie didaktikfreie Aktenstücke. Einzel-PDFs erhalten eine adaptive Satzkontrolle gegen fast leere Schlussseiten; breite Matrizen bleiben tabellarisch, und Excel-Druckfassungen besitzen kollisionsfreie Kopf- und Fußzeilen. Alle sieben Gesamtakten und Echtformate wurden vollständig neu gebaut und visuell geprüft.
- v2.12.0 — Testakten und Auslieferung grundlegend aufgewertet: sieben Fallakten um 28 lebensnahe Aktenstücke zu § 134, Rüge, Nachprüfung, Akteneinsicht, VK-/OLG-Verfahren, Wertungsfehlern und Auftragnehmerwechsel nach § 132 GWB erweitert. DOCX-Briefköpfe, ungeteilte Tabellenzeilen, inhaltsabhängige Spalten, Excel-Quellenblätter, Einzel-PDFs und deduplizierte Gesamt-PDFs wurden neu gesetzt und visuell geprüft. Testakten-ZIPs sind flach, kollisionsfrei und enthalten ausschließlich DOCX, XLSX und PDF einschließlich Gesamtakte. Reproduzierbare Plugin- und Testaktenarchive, strengere Release- und Usabilityvalidatoren, aktuelle GWB-/BTTG-/BSIG- sowie EuGH-Anker und rollenfesteres Skill-Routing sichern Marketplace-, Cowork- und Standalone-Nutzung.
- v2.11.0 — Rechtsstand, Fallakten und Zugriff weiter gehärtet: GWB-Übergangsrecht nach § 187 Abs. 2, Rügepräklusion, VgV-Mindestfristen, Zuständigkeit der Landesvergabekammer Mecklenburg-Vorpommern und Beschwerdeweg zum OLG Rostock fachlich korrigiert. Der Rechtsregressionslauf prüft nun auch DOCX-, XLSX-, PPTX- und PDF-Artefakte. Ein zentraler Dateikatalog, rollenübergreifende Menüs, direkte Browser- und Downloadwege sowie Navigationstests für Root, Plugins, Skill-Indizes, Schnellstarts und jede Testakte sichern den Zugriff auf sämtliche Inhalte.
- v2.10.0 — 201-Befund-Bug-Hunt: rollenübergreifende Skill-Kollisionen beseitigt und dauerhaft gesperrt; sieben fallbezogene Testakten-Rubrics mit strengem Eval-Harness eingeführt; Schweriner Testakte auf Landesvergabekammer und OLG Rostock korrigiert; § 135-, § 160-, § 181- und § 126-Fristen und Rechtsfolgen bereinigt; die neue Missbrauchssperre aus § 160 Abs. 3 Satz 1 Nr. 5 GWB ergänzt; IT-Sicherheits-Skills auf das seit 06.12.2025 geltende BSIG umgestellt; Kostenrecht, Unterschwellenrechtsschutz, Qualitätswertung, vollständiger Regressionsscan, Echtformat-Migration und Release-CI gehärtet. Vollständige Bilanz: [`BUG-HUNT-v2.10.0`](audits/BUG-HUNT-v2.10.0.md).
- v2.9.1 — README und Menüführung neu geordnet: rollenfester 30-Sekunden-Einstieg, klare Trennung von Browser-Ansicht und Datei-Download, vollständige Verlinkung aller 30 Release-Dateien sowie direkte Wege zu allen 249 Skills, Plugin-Vorlagen und Referenzen. Testakten erhalten Gesamtübersicht, direkte PDF- und ZIP-Downloads sowie Vor-/Zurück-Navigation. Neue Validatoren prüfen lokale Links, Menüs, Einzeldateizugriff und den aktuellen Release-Dateisatz.
- v2.9.0 — Daten- und Systemintegration rechtlich operationalisiert: Vergabestellen erhalten Feldautorität, Konfliktauflösung, Entscheidungsbrücke und Rückkanal; Bieter Source-to-Offer-Mapping, Angebotsfreeze und Quittungsabgleich; Konkurrenten Herkunftszonen, Tatsachenkern, Gegenhypothese und Beweiskette. SIB-/PMS-/BIM-/OKSTRA-, SAP-/ERP-/AVA-/DMS-, GAEB-/XML-/Portal- und API-/MCP-Pfade sind mit rollenspezifischen Vorlagen verbunden. EuGH C-568/24, C-534/23 P/C-539/23 P als Integritätsanker für EU-Eigenvergaben sowie OLG Düsseldorf Verg 2/24, Verg 47/18, Verg 34/20 und Verg 36/23 steuern technische Spezifikation, Kompatibilität, elektronischen Zugang, Angebotszustand, Wertungsbegründung und Beweissubstantiierung. Ein neuer Validator verhindert Rollen- und Promptdrift; VK-Einreichungen erhalten einen aktuellen Kanal-, Signatur-, Format- und Empfangscheck.
- v2.8.0 — Rechtsschutz und Skill-Routing grundlegend gehärtet: seit 1. Juli 2026 geltende §§ 169, 172 und 173 GWB in VK-, OLG-, Werkstatt- und Schnellstartabläufen korrigiert; falsche EuGH-Zuordnungen und fachfremde Vergleichsbausteine entfernt; Bieter-, Behörden- und Konkurrenteneinstiege rollenfest neu gefasst; gemeinsame Referenzen über alle Plugin-ZIPs synchronisiert; neue Validatoren gegen generische Skill-Descriptions, Referenzdrift, veraltete Rechtsmuster und fehlzugeordnete Fallanker ergänzt.
- v2.7.17 — Release-ZIP-Validator verschärft: `scripts/validate-release-zips.py` prüft jetzt direkt in jedem Plugin-ZIP die sieben gemeinsamen Kernreferenzen, verbietet alte Repo-Root-Referenzpfade in `SKILL.md` und stellt sicher, dass jeder Skill-Verweis auf `references/*.md` im installierbaren ZIP auflösbar ist.
- v2.7.16 — Plugin-Autarkie nachgezogen: gemeinsame Kernreferenzen zu Output-Format, Quellenhygiene, Zitierweise, Leitentscheidungen, VK-Praxisrechtsprechung, Veröffentlichungswegen und Bestangebot liegen jetzt zusätzlich in allen drei Plugin-Referenzordnern. Skill-Links zeigen auf plugininterne Referenzen; Smoke-Tests sichern, dass Plugin-ZIPs diese Arbeitsgrundlagen künftig nicht verlieren.
- v2.7.15 — Vergabekammer-Praxisrechtsprechung der letzten zehn Jahre vertieft: neue Referenz `references/praxisrechtsprechung-vk-2016-2026.md` mit frei/amtlich erreichbaren VK-Bund- und VK-Westfalen-Ankern zu Rügepräklusion, Substantiierung, Wertungsdokumentation, Konzeptwertung, Preisaufklärung, Akteneinsicht, Nachschieben von Dokumentation und Rahmenvereinbarungen. VK-Stellungnahme, Akteneinsicht, Bieter-Nachprüfungsantrag, Konkurrenten-Nachprüfungsantrag und alle Orchestratoren routen diese Praxisanker jetzt in konkrete Output-Handlungen.

<details>
<summary>Ältere Versionshistorie bis v2.7.14</summary>

- v2.7.14 — Ordnerfall-Kaltstart und Skill-Zuordnung verbessert: technische Skill-Slugs bleiben linkstabil, die Detailseiten zeigen zusätzlich sprechende Arbeitsnamen aus der jeweiligen H1. Alle drei Marktrollen erhalten `assets/templates/ordnerfall-startprotokoll.md`; Orchestrator- und Kaltstart-Skills starten Projektordner, ZIPs, Portalexporte und Dateistapel ohne manuelle Skillwahl mit Fallkarte, Fristenampel, Dokumentenmatrix, Belegmatrix, Lückenliste, Output-Weiche und erstem Arbeitsauftrag.
- v1.0.1 — EuGH SIAC Aktenzeichen korrigiert (C-19/00)
- v1.0.2 — 3 nicht verifizierbare BGH-Aktenzeichen durch OLG-Düsseldorf-Anker ersetzt
- v1.0.3 — CLAUDE.md Schwellenwert-Periode neutral formuliert
- v1.0.4 — Nicht verifizierbaren BGH-Anker in 3 Skills ersetzt
- v1.0.5 — Rügefrist-Anker thematisch entzerrt in 3 Skills
- v1.0.6 — Beschwerde-Anker thematisch entzerrt in 2 Skills
- v1.0.7 — Schwellenwert-Formulierung repo-weit konsistent
- v1.0.8 — Spitzklammer-Platzhalter durch eckige Klammern ersetzt
- v1.0.9 — Mindestfristen § 15 VgV explizit aufgenommen
- v1.0.10 — Final-Hygiene und Versionshinweis aktualisiert
- v1.1.0 — Manifest-Versionen auf README-Stand synchronisiert (plugin.json und marketplace.json jetzt 1.1.0); neuere EU-Anker ergänzt (C-54/21 Antea Polska zu Vertraulichkeit und Akteneinsicht, C-66/22 Infraestruturas de Portugal und Futrifer zu fakultativen Ausschlussgründen); Mandant-Bezug aus Bieter-Skill 22 entfernt (Bieter führt eigenes Verfahren); Smoke-Test-Versionsprüfung auf Semver verallgemeinert
- v1.1.1 — Top-Level-Description in marketplace.json auf das 300-Zeichen-Marketplace-Limit gekürzt (war 314); Versionsstand repo-weit auf 1.1.1 gehoben
- v1.1.2 — Zwei-Plugin-Ausbau mit verwerteten Skills, Testakten, Release-Bundles, Unified-Mini-Prompts und bereinigten Rechtsprechungsankern
- v1.1.3 — Rechtsprechungsanker anhand amtlicher BGH-/BVerfG-Fundstellen nachgeschärft; nicht belastbare Einzelzitate durch Live-Verifikationsregeln ersetzt
- v1.1.4 — Leitentscheidungsanker auf Vergaberecht fokussiert und EU-Schwellenwerte 2026/2027 repo-weit nachgezogen
- v1.1.5 — GAEB/XML/Excel/PDF-Workflows, Angebotspaket, bieterfreundliche Unterlagenbereitstellung und eForms-/Portal-Uploadrouting in beide Plugins integriert
- v1.1.6 — Root-Prompts dezimal gegliedert, Smoke-Tests auf 224 Skills und Datenformat-/Uploadrouting erweitert, Megaprompt-Generator gegen lokale Suffixdateien gehärtet
- v1.2.0 — Praxistauglichkeit für Fachpraktiker gestärkt: adressatengerechte Klartext-Führung in allen vier Mega- und Miniprompts; neue Referenz references/veröffentlichungswege.md (Veröffentlichungswege je Regime) mit korrekter Fristanknüpfung ab Absendung der Bekanntmachung (§ 15 VgV); Skill 05-bekanntmachung-erstellen um Veröffentlichungsweg und die Reihenfolge-Regel § 40 VgV (erst EU-Amtsblatt, dann national) erweitert; Bieter-Skill 01-bekanntmachung-lesen um Prüfhinweise ergänzt
- v1.2.1 — Smoke-Test-Struktur bereinigt, Skillzahltests maschinenfest gemacht, Mini-Prompt-Generator gegen lokale Suffixdateien gehärtet und eForms-Schreibweise in Routing-Hilfen vereinheitlicht
- v1.2.2 — Validatoren und Smoke-Tests gegen lokale Suffixartefakte wie SKILL 2.md, Megaprompt-Kopien und Gesamt-PDF-Duplikate gehärtet; Release-ZIPs prüfen Skill-Suffixdateien vor Upload
- v1.2.3 — Insolvenz- und Auftragnehmerwechsel nach § 132 GWB für Vergabestelle und Bieter eingebaut; neue Referenzen, Skills, Prompt-Priorisierung, EuGH C-461/20 Advania Sverige und Korrektur des Auftragnehmerwechsels auf § 132 Abs. 2 Satz 1 Nr. 4 GWB
- v1.2.4 — Insolvenzfall nach § 132 GWB weiter strukturiert: neue Testakte mit Insolvenzplan, Asset Deal, Share Deal, Nachunternehmer- und Interimsvarianten; VK-Antragsmatrix für Vergabestelle, Erwerber, insolventen Auftragnehmer und Konkurrenten in beide Plugins ergänzt
- v1.2.5 — Sanity-Bugfixes: Auftragnehmerwechsel konsequent auf § 132 Abs. 2 Satz 1 Nr. 4 Buchstabe b GWB nachgezogen, 15-Kalendertage-Frist im VK-Verfahren korrigiert, alte Schwellenwertüberschrift aktualisiert und Validator auf Versionsgleichlauf zwischen marketplace.json und plugin.json erweitert
- v1.2.6 — Vergabebeschleunigungsgesetz 2026 und aktuelle Bund-Länder-Wertgrenzen in beide Plugins eingebaut; neue Referenzmatrix für Direktauftrag, Verfahrenswahl, Landesreformen, Stichtag, Verkündung, Fördermittel und Binnenmarktrelevanz; Schwellenwert-Skills von generischen BGB-Ankern auf Vergaberecht-Anker umgestellt; Generatoren priorisieren den Wertgrenzen-Livecheck
- v1.2.7 — UVgO-Direktauftrag und Unterschwellen-Arbeitswege bereinigt: alte 1000-Euro-Pauschale entfernt, Bund-Länder-Wertgrenzen-Livecheck als Vorlage für beide Marktseiten ergänzt, generische Widerspruch-/BGB-Fristen in importierten Skills durch vergaberechtliche Fristen-, Adressaten- und Aktenlogik ersetzt, 15-Kalendertage-Formulierungen geschärft
- v1.2.8 — Sofort-Download-Sektion im Top-README mit stabilen `releases/latest/download/`-Links für Plugins, Skill-Markdowns, Megaprompts, Miniprompts, Unified Mini Prompts und Testakten; Megaprompts und Miniprompts werden als einzelne `.md`-Release-Assets ausgeliefert (echter Datei-Download, kein Browser-Rendering); neue Sammelpakete `alle-mega-miniprompts.zip`, `alle-plugins-megazip.zip` und `alles-komplettpaket.zip` im Release; neues Skript `scripts/inject-top-readme-downloads.py` hält die Top-Sektion idempotent aktuell; Plugin-Unterseiten bekommen Megaprompt-/Miniprompt- und Einzel-Skill-Hinweisblöcke
- v1.2.9 — Umlaute und ß in sichtbaren deutschen Texten nachgezogen; technische Slugs, Pfade, URLs und Plugin-Namen bleiben ASCII-stabil; abgeleitete Prompts, Skill-Übersichten, Testakten-PDFs und Release-Bundles neu gebaut
- v1.3.0 — Workbench-Qualitätsschub: VK-/OLG-Streitdashboard, Rüge-/Eilantrags-/Beschwerde-Applets, Akteneinsichts- und Schwärzungsmatrix, deutlichere Output-Weichen und Dashboard-Start in Mega-/Mini-Prompts für beide Marktseiten ergänzt
- v1.3.1 — Nutzungsschicht ausgebaut: Startbildschirm-Applets, Belegmatrix, Wertungsmatrix, Upload-/Formatexport-Check, Output-Menü und geführte VK-/OLG-Streitführung in beide Plugins und Prompts integriert
- v1.3.2 — Nutzungsschicht verdichtet: Antwortstandard, Schnellwahl-Applets, neutralisierte Altlabels, entdoppelte Belegmatrix-Beschreibungen und bereinigte Vollprüfungs-Beschreibung ergänzt
- v1.3.3 — Testaktenkorpus aufgewertet: 01 bis 04 als echte Arbeitsakten mit Vermerken, Bekanntmachung, LV, Rüge/VK-Material, CSV/XML/GAEB-Datenanlagen; Gesamt-PDFs und Einzel-PDFs mit Aktenkopf, Briefkopf-Logik, sauberer Typografie, §-Normverweisen und Release-ZIP-Einbindung neu gebaut
- v1.4.0 — Konkurrentenrechtsschutz als dritte Marktrolle ergänzt: neues Plugin mit Skills, Referenzen, Dashboard-Templates, Rüge-/VK-/OLG-Workflow, eigener Testakte, Mega-/Mini-Prompts, Unified-Mini-Prompt und Release-Bundles
- v1.4.1 — Mega-, Mini- und Unified-Mini-Prompts autark gemacht: keine internen Skill-, Plugin- oder Referenzpfad-Verweise in den Ein-Datei-Prompts; Generatoren und Smoke-Tests entsprechend gehärtet
- v1.4.2 — Sprechende Promptnamen, globales Output-Format und Release-Workflow für Arbeits-/Kurzprompts nachgezogen
- v2.0.0 — C-268/25 als aktueller Prüfanker für Bietergemeinschaften integriert: Schlussanträge GA Kokott vom 07.05.2026, ECLI:EU:C:2026:382; Einzelfallprüfung statt Ausschlussautomatismus, Zurechnung, Sorgfalt, Kenntnis, Austauschbarkeit und nicht wesentliche Angebotsänderung in allen drei Marktrollen verankert; Prompt-Autarkie und Smoke-Tests auf neue Dateinamen gehärtet
- v2.0.1 — Konkurrentenrechtsschutz auf das Niveau der anderen Marktrollen gehoben: Arbeitsprompt um adressatengerechte Klartext-Führung, Schwellenwerte 2026/2027, Eskalations-Trigger, Leitentscheidungs-Anker, Ausformulierungspflicht und Sicherheitshinweis ergänzt; Kurzprompt um Quellenhygiene mit Schwellenwert- und Praktikerhinweis erweitert
- v2.1.0 — Aktuelle Rechtsprechungsanker thematisch in alle drei Marktrollen eingezogen: DYKA Plastics für Leistungsbeschreibung und Formate, Generální finanční ředitelství für Verfahrensausnahmen, Mara für personalintensive Wertungen, Polismyndigheten und Fastned Deutschland für § 132-/Konzessionsänderungen sowie Fastweb/PFE/Randstad Italia für Konkurrentenrechtsschutz; Testaktenhinweise bereinigt und Prompt-/Generatorrouting geschärft
- v2.2.0 — Sanity- und Kohärenzrelease: Eignungsprüfung, ESPD, Bieter-Eignungsanforderungen und Arbeitsprompt sprachlich bereinigt, Skill- und Prompt-Übersichten neu generiert, Manifest-Versionen synchronisiert
- v2.3.0 — Bestwertung statt Preisautomatismus: § 127 GWB, § 58 VgV und Art. 67 RL 2014/24/EU in allen drei Marktrollen geschärft; Qualitäts-, Tempo-, Servicelevel- und Lebenszykluskriterien in Vergabestellenmatrix, Bieterangebot und Konkurrentenangriff verankert
- v2.3.1 — Bestangebot-Durchsetzung ergänzt: neue Kernskills für Vergabestelle, Bieter und Konkurrenten; Bestangebots-Stresstest, Wirtschaftlichkeitsbrücke und Billigzuschlag-Angriff in Skills, Mega-Prompts, Mini-Prompts und Arbeitsprompts verankert
- v2.3.2 — Finaler Sanity- und Kohärenz-Sweep: Mara-Prüfanker für Nur-Preis-Wertungen präzisiert, Bestwertungs-Routing in Kaltstart und Startbildschirm geschärft, Rollenanker für Bieter und Konkurrenten nachgezogen und Generator-/Validierungsrunde erneuert
- v2.3.3 — Legacy-IT-Integrationsschicht ergänzt: drei neue Skills für Vergabestelle, Bieter und Konkurrenten, SAP/ERP/CRM/AVA/DMS/MCP-Adapterlogik, Hash-Cluster, Mapping-Manifest, Delta-Protokoll, Freigabeauftrag und Push-/Upload-Routing in Prompts, Dashboards und Release-Bundles verankert
- v2.3.4 — Usability-Schicht geschärft: Ein-Bildschirm-Lage, Output-Weiche, Nutzungscheck, nächste Bedienhandlung und vollständigeres Konkurrenten-Dashboard in Startskills, Applets, Mega- und Kurzprompts verankert
- v2.3.5 — Sanity- und Kohärenz-Sweep: Smoke-Test-Skill-Zahlen auf den aktuellen Stand 119/111/18 (248 gesamt) nachgezogen und die Megaprompt-Größenschwelle an das gewachsene Arbeitsprompt-Niveau (unter 16000 Zeichen) angepasst; alle 15 Smoke-Tests verifiziert
- v2.3.6 — Kohärenz-Sweep der generierten Übersichten: SKILLS.md und alle skills-index-Detailseiten mit dem Release-Generator neu erzeugt, sodass Versionsstand (v2.3.6), Skill-Zahlen und Skill-Beschreibungen wieder synchron zu den SKILL.md-Frontmattern sind; zuvor hingen die Stand-Labels auf v2.3.4 zurück
- v2.3.7 — Vergabestellen-Plugin um Wirklichkeitsdaten-Steuerung ergänzt: Bestands-, Zustands-, Kosten-, Bauzeit-, Plan-, BIM-, Umwelt-, Normen- und Rechtsdaten werden in Bedarf, Bündelung, LV, Budget, Szenarien, Bestwertung und Vergabeakte übersetzt
- v2.3.8 — Wirklichkeitsdaten-Applets für Vergabestellen vertieft: Portfolio, beschleunigte Beauftragung, Vergaberechtsnavigation, Mobilität/Tragfähigkeit, Ausschreibungsstudio, ÖPP/CAPEX und Serienlösungen in Quellen-, Szenario-, LV- und Aktenworkflows ergänzt
- v2.4.0 — Skill-Discovery und Nutzungsschicht geschärft: gemeinsame Rollenprioritäten für Mega-/Mini-Prompts, Top-18-Megaprompts für Vergabestelle und Bieter, konkrete Kaltstart-Routingtabellen, stärkere Spezialfall-Trigger, Vergabestellen-Datensilo-Workflow mit gemeinsamer Fachsprache sowie bessere Portal-, Beweis-, Bestangebots- und Rechtsschutz-Routen
- v2.5.0 — Skill-Routing auf realistische Startsignale geschärft: exakte Skill-Slugs in Mega-, Mini- und Kurzprompts, role-spezifische Trigger für Vergabestelle, Bieter und Konkurrent, stärkere VK-/OLG-, Register-, Bietergemeinschafts-, Bestangebots-, Legacy- und Portal-Beweisrouten sowie bereinigte Fachlandkarten ohne verkümmernde Spezialskills
- v2.5.1 — Prompt-QS nachgezogen: neuer Validator für Dual-Mode-Prompts mit exaktem Skill-Routing und autarkem Fallback, Smoke-Test-Regel an v2.5-Routing angepasst, Release-Workflow um Prompt-Routing-Prüfung erweitert und alte Importphrase in Unterlagen-/Lückenlisten bereinigt
- v2.5.2 — Kohärenz-Sweep: Smoke-Test-Größenschwellen an die durch das Claude-Skill-Routing gewachsenen Root-Prompts angepasst (Megaprompts unter 18000, Miniprompts unter 9000 Zeichen); SKILLS.md und skills-index mit dem Release-Generator auf Stand v2.5.2 regeneriert; alle 34 Routing-Slugs gegen reale Skill-Verzeichnisse verifiziert, alle drei Validatoren und Smoke-Tests grün
- v2.5.3 — Struktur-Validator auf Einmal-Traversierung mit Lese- und Zeilen-Cache umgebaut: statt sechs vollständigen Verzeichnisbaum-Durchläufen und Mehrfach-Reads nur noch ein Durchlauf mit gecachten Inhalten (Datei-Syscalls im Repo von 3348 auf 752 reduziert, Prüflogik und Fehlermeldungen per A/B-Test byte-identisch nachgewiesen); Kohärenz-Sweep ohne weitere Befunde, alle drei Validatoren und Smoke-Tests grün
- v2.5.4 — Smoke-Tests automatisiert: neuer Runner scripts/run-smoke-tests.py führt alle bash-Blöcke aus tests/smoke-tests.md mit einem Befehl aus (14 automatisierte Abschnitte in unter einer halben Sekunde statt manueller Copy-Paste-Kette; die Markdown-Datei bleibt einzige Quelle der Wahrheit). Der erste Lauf fand sofort einen echten Fehler: Smoke 11 verwies auf 05_nachprüfungsantrag mit Umlaut-ü statt des realen Dateinamens mit ue — korrigiert. Alle Pfade der Prüfkette systematisch verifiziert
- v2.5.5 — Manuelle Smoke-Abschnitte nachgeprüft und Lücken geschlossen: Die Schwellenwert-VOen 2025/2150, 2025/2151 und 2025/2152 fehlten entgegen Smoke 8 in allen drei Kurzprompts und im generierten Konkurrenten-Megaprompt; VO-Zitat in den Kurzprompts und im Orchestrator-Skill des Konkurrentenrechtsschutzes ergänzt (Megaprompt daraus regeneriert). Smoke 8 hat jetzt einen eigenen bash-Block und läuft automatisch mit — 15 von 17 Abschnitten automatisiert
- v2.5.6 — Smoke 7 (Anker-Rechtsprechung) automatisiert: bash-Block prüft mechanisch die Präsenz der sechs Kernanker aus CLAUDE.md und lehnt fehlgeformte Aktenzeichen-Jahresteile ab (beide Fehlerpfade per Negativ-Test verifiziert; ein set-e-Sonderfall bei negierten Kommandos wurde dabei gefunden und durch Umstellung der Blockreihenfolge behoben). Prüfkette jetzt 16 von 17 Abschnitten automatisiert; die inhaltliche Live-Verifikation der Rechtsprechung bleibt bewusst manuelle Quellenhygiene-Pflicht
- v2.6.0 — Testakten lebensecht gemacht (Datenwusel-Grundregel): Die Release-ZIPs aller sieben Testakten enthalten kein Markdown mehr, sondern nur Lebenslage-Formate — 46 Word-Dokumente mit Briefkopf in Times New Roman 11 pt, 11 echte .eml-Mails mit vollständigen Headern und 14 Excel-Anlagen, deterministisch aus den Markdown-Quellen erzeugt (neuer Generator scripts/build-testakten-echtformate.py, inhaltsidentisch mit Gesamt- und Einzel-PDFs, handgefertigte Gegenstücke der IT-SIG-2-Akte respektiert). Export-Filter, ZIP-Validierung und neuer Smoke-Abschnitt 17 erzwingen die Markdown-Freiheit mechanisch; Grundregel für künftige Testakten in CLAUDE.md und testakten/README.md verankert
- v2.7.0 — Datenwusel komplettiert: 12 rein grafische Scan-PDFs (Bild-PDF ohne Textebene, mit Papierrauschen, leichter Rotation und Scannerschatten — wie vom Multifunktionsgerät) und 7 PowerPoint-Präsentationen je Akte ergänzt, deterministisch aus denselben Markdown-Quellen (Generator erweitert, Pillow und python-pptx in requirements-dev.txt aufgenommen). Smoke-Abschnitt 17 verlangt jetzt je Testakten-ZIP mindestens ein docx, ein Scan-PDF und eine pptx; Grundregel in CLAUDE.md und testakten/README.md entsprechend erweitert
- v2.7.1 — Skill-Routing und Release-QS geschärft: Root- und Kurzprompts zeigen die zentralen Trigger-Skills jetzt vollständig je Marktrolle, insbesondere Dashboard, Legacy, Bestangebot, Bieterfragen, Bietergemeinschaft, VK/OLG, De-facto-Vergabe und Kostenrisiko. Der Prompt-Routing-Validator prüft nun zentrale Router- und Prioritätslisten gegen reale Skills und sichtbare Prompt-Slugs; der GitHub-Release-Workflow führt zusätzlich die komplette Smoke-Test-Kette aus.
- v2.7.2 — Release-Workflow für die komplette Smoke-Kette gehärtet: GitHub Actions installiert `ripgrep`, damit die rechtsprechungs-, wertgrenzen-, Datenformat- und Rechtsschutz-Smoke-Tests auch im Linux-Runner laufen und nicht nur lokal.
- v2.7.3 — Release-Integrität nach dem Upload abgesichert: Der Workflow erzeugt `checksums-sha256.txt`, lädt das Prüfsummenmanifest mit hoch und validiert anschließend die veröffentlichten GitHub-Release-Assets gegen die lokal gebaute `dist/`-Fassung nach Name, Upload-Status, Größe und SHA-256-Digest.
- v2.7.4 — Prüfsummenmanifest in der Release-QS verschärft: `validate-release-assets.py` parst `checksums-sha256.txt` und stellt sicher, dass jedes veröffentlichte Asset außer dem Manifest genau einmal mit korrektem SHA-256 enthalten ist.
- v2.7.5 — Testakten realistischer ausgebaut: Jede Akte erhält deterministischen Aktenbeifang mit interner Weiterleitung, loser Bearbeitungsnotiz, Portal-/Uploadprotokoll, PNG-Fristenskizze und eigenen Einzel-PDFs; Smoke-Tests erzwingen diese Datenwusel-Schicht.
- v2.7.6 — Testakten-QS verschärft: Neuer Validator `validate-testakten-echtformate.py` prüft Aktenbeifang, Portalprotokolle, interne Weiterleitungen, Fristenskizzen, Gesamt-PDFs und Beifang-Einzel-PDFs vor Release.
- v2.7.7 — Schnellzugriff und Link-QS finalisiert: Root-README, Plugin-READMEs, SKILLS.md, skills-index, Testakten-README und Unified-Mini-Prompt-README führen jetzt rollenbezogen zu Plugin, Prompt, Einzel-Skill, Gesamt-PDF und Release-ZIP; neuer Validator `validate-doc-links.py` prüft lokale Übersichtslinks in der Smoke-Test-Kette.
- v2.7.8 — Mini- und Werkstattprompts workflowartig geschärft: Unified-Mini-Prompts, Kurzprompts, Arbeitsprompts und Megaprompt-Generator führen jetzt mit Sofortworkflow, Werkstattmodus, Output-Weiche, Beleg-/Format-/Fristenkontrolle und konkretem nächsten Arbeitsprodukt je Marktrolle.
- v2.7.9 — Werkstatt- und Schnellstartprompts rechtsprechungsfest geschärft: Rollenprompts führen jetzt mit konkreten Prüfankern zu Mara, DYKA Plastics, C-578/23, BGH X ZB 10/16, C-268/25, Fastweb/PFE/Randstad und Akteneinsichtsrechtsprechung. Jeder Anker steuert Tatsachentest, Normbezug und Pflichtoutput statt bloßer Fundstellenliste.
- v2.7.10 — Werkstatt- und Mini-Einstiegskerne weiter konkretisiert: zentrale Orchestrator-, Kaltstart-, Arbeitsprompt- und Unified-Mini-Prompt-Schichten enthalten je Marktrolle Norm-/Rechtsprechungsweichen mit ECLI, Falltyp, Tatsachentest und Pflichtoutput zu Bestangebot, LV-/Formatneutralität, Direktvergabe/Lock-in, Billigpreis, Ausschluss/Bietergemeinschaft, Akteneinsicht sowie VK/OLG. Die Unified-Mini-Prompts bleiben unter 7.500 Zeichen und liefern autarke Hauptarbeit statt generischer Workflow-Texte.
- v2.7.11 — Regression-Sicherung für rechtsprechungsfeste Mini-Einstiege ergänzt: neuer Validator `validate-mini-prompt-entrypoints.py` prüft je Marktrolle Länge, Sofortworkflow, Output-Weiche, Norm-/Rechtsprechungskern, ECLI-Anker, Pflichtarbeitsbegriffe und verbietet generische Altbausteine. Smoke-Tests und GitHub-Release-Workflow führen den Check vor jedem Release aus.
- v2.7.12 — Werkstatt- und Schnellstartprompts weiter entgeneralisiert: Arbeitsprompts, Kurzprompts, Unified-Mini-Prompts und generierte Megaprompts starten jetzt mit rollenbezogener Fallkarte zu Falltyp, Normenanker, Tatbestandswichtigkeiten, Beweislast/Darlegungslast, BGH-/BVerfG-/EuGH-Ankern, Quellenstatus, Rechtsfolge und gewünschter Outputvariante. Der Mini-Prompt-Validator erzwingt diese Fallkarten-Schicht und die Smoke-Test-Erläuterung trennt Root-Kurzprompts von den hart begrenzten Unified-Mini-Prompts.
- v2.7.13 — Vorlagenebene nachgezogen: Alle drei Pluginrollen erhalten `assets/templates/fallkarte-output-weiche.md` mit ausfüllbarer Fallkarte, Output-Weiche und Schlusskontrolle. Startdashboard-Templates und Orchestrator-Skills verlinken die neue Vorlage; Smoke-Tests prüfen Existenz, Verlinkung, Normenanker und Quellenstatus der Fallkarten-Vorlagen.

</details>
