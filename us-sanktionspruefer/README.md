# 1. US-Sanktionsprüfer für Unternehmen und Kanzleien

Der US-Sanktionsprüfer führt die Prüfung eines Geschäftspartners, einer angehaltenen Zahlung oder eines anwaltlichen Mandats bis zum benötigten Dokument. Ein Hauptskill und neun Fachskills klären US-Bezug, Listenidentität, Eigentum, Verbote, Lizenzen und Verfahren. Das Ergebnis ist ein begründeter Vermerk, ein fertiges Schreiben oder ein Antragsentwurf, nicht bloß eine Trefferliste.

[Hauptübersicht](../README.md) · [Plugin-Dateien](.) · [Alle Skills](../SKILLS.md) · [Skills dieses Plugins](../skills-index/us-sanktionspruefer.md) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md) · [English guide](#16-english-guide)

Der Schwerpunkt liegt auf OFAC-Sanktionen sämtlicher einschlägiger Länder- und Themenprogramme, einschließlich Terrorismus. SDN, Non-SDN, FTO/SDGT und BIS-Exportkontrolle werden nicht gleichgesetzt. Ein Unternehmen kann wegen seiner Eigentümer blockiert sein, obwohl es nicht namentlich auf einer Liste steht. Die rechtliche Prüfung bleibt von einer strengeren Geschäftspolitik der Bank zu unterscheiden.

## 1.1. Mit dem vorhandenen Vorgang beginnen

Übergeben Sie die Bankmitteilung, den Vertrag oder die Beteiligungsunterlagen und nennen Sie das gewünschte Ergebnis. Zum Beispiel: „Die Bank hält diese Zahlung an. Prüfen Sie den Grund und entwerfen Sie unsere Antwort.“ Der Hauptskill `us-sanktionsmandat-steuern` liest den relevanten Bestand, fragt entscheidende Lücken nach und setzt denselben Entwurf nach Ihrer Antwort fort. Es ist nicht erforderlich, alle zehn Skills nacheinander zu starten.

| Ausgangslage | Bearbeitung | Arbeitsprodukt |
| --- | --- | --- |
| Ähnlicher Name in einem Suchergebnis | Identifikatoren, Listentyp und tatsächlichen Bankstatus abgleichen | Identitätsblatt und Bankanschreiben |
| Unübersichtliche Beteiligungskette | Eigentum stufenweise und aggregiert prüfen; Kontrolle gesondert behandeln | Beteiligungsvermerk mit Belegen und fehlenden Nachweisen |
| Unklarer US-Bezug | Personen, Leistung, Bankweg und besondere Regime unterscheiden | Begrenzter Zuständigkeits- und Transaktionsvermerk |
| Rechtsberatung für betroffenen Mandanten | Rechtsdienstleistung, Honorar und Fremdgeld separat prüfen | Mandatsbrief, Lizenzvermerk oder Lizenzantrag |
| Bereits blockiert, zurückgewiesen oder behördlich beanstandet | Richtigen Verpflichteten, Verfahrensweg und Fristen bestimmen | Meldungsentwurf, Überprüfungsantrag oder Erwiderung |

Vor jeder tatsächlichen Ausführung müssen die dafür relevanten aktuellen Listen, Regeln und Lizenzen geprüft werden. Das Plugin enthält keine dauerhaft gültige Sanktionsliste und keine eingebauten Behördenzugänge. Zahlungsanweisungen, Meldungen, Antragstellung und Versand bleiben ausdrücklich freigabepflichtig.

## 1.2. Plugin und eigenständige Prompts herunterladen

| Angebot | Verwendung | Download |
| --- | --- | --- |
| Plugin | Zehn gezielt eingesetzte Skills mit Quellenregister | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/us-sanktionspruefer.zip) |
| Portables Plugin | Derselbe Fachinhalt in einem umschließenden Plugin-Ordner | [Portables ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/us-sanktionspruefer-portable.zip) |
| Werkstatt-Prompt | Ausführlicher eigenständiger Ablauf mit Verzweigungen und Dokumentenproduktion | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/us-sanktionspruefer-werkstatt.md" download>Werkstatt als Markdown</a> |
| Mini-Prompt | Kompakter Ablauf für die konkrete US-Sanktionsprüfung | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/us-sanktionspruefer-schnellstart.md" download>Mini als Markdown</a> |
| Hauptproblem-Prompt | Angehaltenes Geschäft vom Treffer bis zum benötigten Dokument bearbeiten | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/us-sanktionspruefer-hauptproblem.md" download>Hauptproblem als Markdown</a> |
| Quellenregister | Primärquellen, geprüfte Entscheidungen und Aussagegrenzen | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/references/quellenregister.md" download>Quellen als Markdown</a> |

Wählen Sie das Plugin oder eine eigenständige Markdown-Datei. Nicht alle Fassungen gleichzeitig laden. Werkstatt, Mini und Hauptproblem-Prompt sind keine zusätzlichen Wrapper-Skills. Mini und Hauptproblem bleiben jeweils unter 7.000 UTF-8-Bytes einschließlich Windows-Zeilenumbrüchen. Das [Komponentenrelease 1.0.0](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/sanktionen-eu-us-v1.0.0) bezeichnet die feste Paketversion; die Downloadhilfe liefert die aktuelle Arbeitsfassung der Markdown-Dateien.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## 1.3. Zehn Skills einzeln verwenden

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`ofac-eigentum-beteiligungsketten-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/ofac-eigentum-beteiligungsketten-pruefen/SKILL.md) | Prüft die OFAC-Eigentumsregel über mehrere Beteiligungsebenen mit Aggregation blockierter Eigentümer. Trennt Kontrolle und Vertreterhandeln von automatischer Blockierung und erstellt einen belegten Beteiligungsvermerk samt Nachforderung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/ofac-eigentum-beteiligungsketten-pruefen/SKILL.md) |
| [`ofac-fehler-rechtsschutz-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/ofac-fehler-rechtsschutz-bearbeiten/SKILL.md) | Unterscheidet fehlerhafte Blockierung, tatsächliche Listung und OFAC-Sanktionsverfahren. Bereitet Compliance Release, Delisting, Behördenantwort und US-Rechtsschutz mit Belegen und verifizierten Entscheidungsgrenzen vor. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/ofac-fehler-rechtsschutz-bearbeiten/SKILL.md) |
| [`ofac-lizenzen-rechtsberatung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/ofac-lizenzen-rechtsberatung-pruefen/SKILL.md) | Prüft General und Specific Licenses für konkrete US-Sanktionsverbote und trennt anwaltliche Leistung, Honorar und Fremdgeld. Erstellt einen belegten Lizenzvermerk oder antragsreifen Entwurf mit Nebenbestimmungen und offenen Nachweisen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/ofac-lizenzen-rechtsberatung-pruefen/SKILL.md) |
| [`ofac-sperrung-meldungen-dokumentieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/ofac-sperrung-meldungen-dokumentieren/SKILL.md) | Unterscheidet OFAC-Blockierung, Zurückweisung und reine Bankprüfung. Bereitet Meldungen, Fristen und Aufbewahrung nach Part 501 vor und erstellt konkrete Anweisungs- und Berichtsentwürfe ohne selbst Zahlungen oder Meldungen auszulösen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/ofac-sperrung-meldungen-dokumentieren/SKILL.md) |
| [`ofac-treffer-identitaet-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/ofac-treffer-identitaet-klaeren/SKILL.md) | Klärt OFAC-Namens- und Identitätstreffer mit amtlichen Datensätzen und belegten Identifikatoren. Unterscheidet echte Listung, ungeklärten Treffer und Namensgleichheit und erstellt Bankanschreiben oder dokumentierte Trefferentscheidung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/ofac-treffer-identitaet-klaeren/SKILL.md) |
| [`us-bezug-zustaendigkeit-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/us-bezug-zustaendigkeit-pruefen/SKILL.md) | Prüft den konkreten US-Bezug deutscher Unternehmen und Kanzleien, beteiligte US-Personen, Zahlungswege und besondere Programmregeln. Trennt primäre Verbote von sekundären Sanktionsrisiken und erstellt ein belastbares Zuständigkeitsmemo. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/us-bezug-zustaendigkeit-pruefen/SKILL.md) |
| [`us-eu-rechtskonflikte-loesen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/us-eu-rechtskonflikte-loesen/SKILL.md) | Bearbeitet Konflikte zwischen konkreten US-Sanktionsanforderungen und europäischem Recht für deutsche Unternehmen und Kanzleien. Prüft Blocking Statute, Vertragsgründe und Genehmigungswege und entwirft eine begründete Entscheidung statt... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/us-eu-rechtskonflikte-loesen/SKILL.md) |
| [`us-regime-transaktionen-abgrenzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/us-regime-transaktionen-abgrenzen/SKILL.md) | Ordnet konkrete Waren-, Dienstleistungs-, Finanzierungs- und Kryptogeschäfte dem einschlägigen US-Sanktionsprogramm zu. Trennt SDN, Non-SDN und Exportkontrolle und erstellt eine transaktionsbezogene Entscheidungsvorlage statt einer Lände... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/us-regime-transaktionen-abgrenzen/SKILL.md) |
| [`us-sanktionsmandat-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/us-sanktionsmandat-steuern/SKILL.md) | Führt US-Sanktionsprüfungen für Unternehmen und deutsche Kanzleien vom konkreten Geschäft über Trefferklärung und Zuständigkeit zum fertigen Vermerk, Schreiben oder Antrag. Hauptskill mit neun gezielt eingesetzten Fachschritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/us-sanktionsmandat-steuern/SKILL.md) |
| [`us-terrorismus-unterstuetzung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/us-terrorismus-unterstuetzung-pruefen/SKILL.md) | Unterscheidet FTO-Designation, SDGT-Blockierung und den Straftatbestand materieller Unterstützung. Prüft Empfänger, konkrete Leistung, Koordination und US-Zuständigkeit und erstellt eine sachliche Entscheidungsvorlage ohne Herkunftszusch... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=us-sanktionspruefer/skills/us-terrorismus-unterstuetzung-pruefen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

## 1.4. Fachliche Grenzen und Quellenstand

Redaktioneller Stand: 21.10.2026. Das Quellenregister unterscheidet gelesene amtliche Norm- und Entscheidungstexte von einer amtlichen Entscheidungsmitteilung. Zu Bank Melli ist die Mitteilung verifiziert; vor einem tragenden Schriftsatzzitat müssen die vollständigen Gründe gelesen werden. Für administrative Einzelfragen ohne passenden verifizierten Gerichtsanker wird kein Urteil erfunden.

Die Eigentumsprüfung berücksichtigt ausdrücklich OFAC-FAQ 401: 50 Prozent eines blockierten Eigentümers an einem Unternehmen und dessen 50 Prozent an einem weiteren Unternehmen bewirken die Sperrwirkung auf beiden Ebenen. Es wird nicht auf 25 Prozent durchmultipliziert. Reine Kontrolle allein löst diese Eigentumsregel nicht aus; weitere Verbote bleiben zu prüfen.

Die Aufbewahrung berücksichtigt die seit März 2025 geltenden zehn Jahre nach 31 CFR 501.601. Verfahrenshinweise berücksichtigen Part 505 aus September 2026. Van Loon wird eng auf den entschiedenen Eigentumsbegriff bezogen; weder Urteil noch spätere Entlistung garantieren die heutige Zulässigkeit eines anderen Geschäfts.

Eine alleinige FTO-Bezeichnung kann nach Part 597 eigene Pflichten für US-Finanzinstitute auslösen, auch ohne SDGT-Bezeichnung. Dessen Pflichtkreis und Vergütungsregeln werden eigenständig geprüft. Die Anfechtung einer FTO-Bezeichnung des State Department folgt 8 USC 1189, nicht einfach dem OFAC-Verfahren nach 501.807.

Erfundene Schulungslisten und Terrorlistentreffer dürfen niemals mit aktuellen amtlichen Listen oder realen Kundenbeständen zusammengeführt werden. Sie werden ausdrücklich als Simulation behandelt und nicht an Behörden oder Banken übermittelt.

Dieses experimentelle Arbeitsmittel ist keine Rechtsberatung, Zertifizierung oder Garantie. Recherchezugriff, Dateiverarbeitung und unterstützte Plugin-Funktionen hängen von der konkreten Oberfläche ab. Redaktionelle Durchsicht und technische Prüfungen sind keine beobachteten Live-Modellläufe. Bei schwierigen US-/EU-Konflikten ist qualifizierte Fachberatung einzubeziehen. Entwürfe müssen vor ihrer Verwendung fachlich und tatsächlich kontrolliert werden.

## 1.5. Zwei eigenständige Fallakten

Beide Akten enthalten jeweils zwölf Originale: fünf Word-Dokumente, vier E-Mails mit tatsächlich beigefügten Anlagen, zwei Zahlentabellen und einen Gesprächs- oder Nachrichtenverlauf. Sämtliche Beteiligten, Fantasiestaaten und Listungen sind erfunden. Die angeblichen Listungsentscheidungen sind deutlich als unechte Rechtsakte gekennzeichnet. Keine Musterlösung und kein Bezug zu real gelisteten Personen.

### 1.5.1. Klingelgau: Zwei Bestellungen und ein wartender Zahlungsauftrag

Eine Gesellschaft bestellt Komponenten für 48.000 US-Dollar und Ersatzmaterial für 9.600 Euro. Zwei voneinander unabhängige Anteilseigner erscheinen in einem erfundenen US-Listungsdatensatz. Die Bank hält einen Auftrag an; Gesellschaftsunterlagen, Bestellung und Nachrichten dokumentieren den noch offenen Stand. [Unterlagenverzeichnis](../testakten/sanktionen-us-klingelgau-eigentum/README.md).

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamtakte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/sanktionen-us-klingelgau-eigentum_gesamt.pdf) |
| Einzel-PDF-ZIP / Individual PDFs | [Einzelne Dokumente](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/testakte-sanktionen-us-klingelgau-eigentum-einzelpdfs.zip) |
| Originalformat-ZIP / Native documents | [DOCX, EML, CSV und TXT](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/testakte-sanktionen-us-klingelgau-eigentum.zip) |

### 1.5.2. Sonnenquast: Spendenpost mit ähnlich geschriebenen Namen

Eine Stiftung sammelt Spenden für eine Einrichtung im erfundenen Sonnenquast. Ein Spendername ähnelt einem ausschließlich erfundenen Terrorlisteneintrag. Zum vorgesehenen Empfänger liegen eine alte Adresse und verkürzte Bankfelder vor; zum Spender andere Identitätsangaben. [Unterlagenverzeichnis](../testakten/sanktionen-us-sonnenquast-namensgleichheit/README.md).

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamtakte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/sanktionen-us-sonnenquast-namensgleichheit_gesamt.pdf) |
| Einzel-PDF-ZIP / Individual PDFs | [Einzelne Dokumente](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/testakte-sanktionen-us-sonnenquast-namensgleichheit-einzelpdfs.zip) |
| Originalformat-ZIP / Native documents | [DOCX, EML, CSV und TXT](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/testakte-sanktionen-us-sonnenquast-namensgleichheit.zip) |

Alle ZIPs sind flach. Die PDF-Fassungen bilden denselben Dokumentenbestand ab; jedes Original bleibt ein eigenständiges PDF. Die Archive enthalten zusätzlich eine zweisprachige Hinweisdatei. Die Akten werden nicht zusammen mit dem Plugin installiert.

## 1.6. English Guide

This plugin supports companies and German law firms in reviewing a business relationship, a held payment or a sanctions-sensitive engagement. One coordinating skill and nine specialist skills lead to a reasoned memorandum, a bank letter, a licensing application or a response draft. Existing documents are read first; targeted questions continue the same draft rather than restarting intake.

Use the plugin or one standalone Markdown prompt from section 1.2. Section 1.3 lists all ten skills alphabetically with individual downloads. The workshop provides the detailed workflow. The quick-start and main-problem prompts each remain below 7,000 UTF-8 bytes, including Windows line endings. Standalone prompts are not additional installed wrapper skills. Section 1.5 provides two entirely fictional case files, each with twelve native documents, a combined PDF and a flat archive of individual PDFs; they remain separate from the installed plugin.

Review the actual US nexus, program, identity, ownership and transaction. USD alone is not a complete jurisdictional analysis. SDN, non-SDN, FTO/SDGT and BIS controls are different. OFAC's ownership rule requires aggregation and a step-by-step analysis; a blocked person's 50% ownership of A and A's 50% ownership of B blocks both A and B. Control alone is not automatic blocking under that rule.

Current official sources must be checked for each relevant transaction. The source register states the scope and limits of the verified authorities, including Van Loon, the 2025 recordkeeping change and the 2026 Part 505 procedures. Fictional training listings must remain isolated from production screening and external reports. Payments, filings and communications require explicit approval. This experimental aid is not legal advice, and no live performance or universal host compatibility is claimed.
