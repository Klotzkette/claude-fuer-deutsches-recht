# 1. EU-Sanktionsprüfer

Dieses Fachpaket begleitet Unternehmen und Kanzleien von einer konkreten Zahlungs-, Liefer- oder Mandatsfrage bis zum begründeten Schreiben, Genehmigungsantrag oder Entscheidungsvorschlag. Es unterscheidet echte Listentreffer, Namensverwechslungen, Eigentum und Kontrolle sowie sektorale Verbote, die auch nicht gelistete Geschäftspartner betreffen können. Terrorismus- und andere Themenregime werden ebenso berücksichtigt wie Länderregime.

[Einstieg](#11-so-beginnen-sie) · [Zehn Skills](#12-die-zehn-skills) · [Downloads](#13-downloads) · [Quellen und Grenzen](#14-quellen-und-grenzen) · [Fallakten](#15-vierzig-prozent-kontrolle-und-mandatsgeld) · [English](#2-english)

[Repository](../README.md) · [Alle Skills](../SKILLS.md) · [Skillübersicht dieses Plugins](../skills-index/eu-sanktionspruefer.md) · [Dateiübersicht](../ASSET_INDEX.md) · [Testaktenübersicht](../testakten/README.md) · [Plugin-Dateien](.)

## 1.1. So beginnen Sie

Stellen Sie die Bankmitteilung, den Vertrag oder die geplante Transaktion und vorhandene Belege bereit. Nennen Sie das benötigte Dokument, beispielsweise: „Prüfe die zurückgehaltene Zahlung und entwirf die Antwort an unsere Bank.“ Der Hauptskill `eu-sanktionsfall-steuern` liest den Bestand, fragt nur entscheidende fehlende Angaben nach und führt in den passenden Fachschritt.

Ein einzelner Treffer kann eine Identitätsklärung benötigen; ein komplexer Geschäftsvorgang zusätzlich eine Beteiligungs-, Waren- oder Dienstleistungsprüfung. Es müssen nicht alle zehn Skills nacheinander abgearbeitet werden. Nach einer Antwort wird derselbe Entwurf fortgeführt. Das Ergebnis soll ein verwendbares Dokument sein, keine bloße Aufzählung möglicher Probleme.

Ohne Plugin genügt eine der drei Markdown-Dateien: Der Werkstatt-Prompt enthält die ausführlichen Prüfwege. Der Schnellstart führt kompakt durch einen neuen Vorgang. Der Hauptproblem-Prompt konzentriert sich auf die Klärung einer zurückgehaltenen Geschäftstransaktion. Schnellstart und Hauptproblem bleiben jeweils unter 7.000 UTF-8-Bytes einschließlich Windows-Zeilenumbrüchen. Die drei Dateien sind eigenständige Arbeitsanweisungen, keine zusätzlichen installierten Skills.

## 1.2. Die zehn Skills

| Schritt | Skill | Konkretes Arbeitsprodukt |
| --- | --- | --- |
| 1 | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-sanktionsfall-steuern/SKILL.md" download>EU-Sanktionsfall steuern</a> | Hauptskill: Auftrag und Fachwege bis zum fertigen Schreiben zusammenführen. |
| 2 | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-anwendungsbereich-regime-bestimmen/SKILL.md" download>Anwendungsbereich und Regime bestimmen</a> | Handlung, Beteiligte, Zeitpunkt und einschlägige Verbote begründet zuordnen. |
| 3 | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-listentreffer-identitaet-klaeren/SKILL.md" download>Listentreffer und Identität klären</a> | Belegte Trefferklärung, Nachforderung oder Korrekturschreiben. |
| 4 | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-eigentum-kontrolle-pruefen/SKILL.md" download>Eigentum und Kontrolle prüfen</a> | Beteiligungs- und Kontrollvermerk mit Gegenbelegen und konkreten Lücken. |
| 5 | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-gelder-ressourcen-sichern/SKILL.md" download>Gelder und Ressourcen sichern</a> | Abgrenzung von Einfrieren, Bereitstellung, Gutschrift und Verfügung. |
| 6 | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-handel-dienstleistungen-pruefen/SKILL.md" download>Handel und Dienstleistungen prüfen</a> | Transaktionsbezogene Prüfung auch ohne persönlichen Listentreffer. |
| 7 | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-ausnahmen-genehmigungen-vorbereiten/SKILL.md" download>Ausnahmen und Genehmigungen vorbereiten</a> | Bestimmter Antrag mit Zweck, Betrag, Zahlungsweg und Anlagen. |
| 8 | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-meldung-verschwiegenheit-klaeren/SKILL.md" download>Meldung und Verschwiegenheit klären</a> | Abgegrenzter Informations- oder Meldungsentwurf nach Pflichtnorm. |
| 9 | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-vertraege-drittstaatenkonflikte-bearbeiten/SKILL.md" download>Verträge und Drittstaatenkonflikte bearbeiten</a> | Bankbrief, Vertragsantwort oder Antrag zum konkreten Normkonflikt. |
| 10 | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-rechtsschutz-entlistung-vorbereiten/SKILL.md" download>Rechtsschutz und Entlistung vorbereiten</a> | Passender Rechtsbehelf gegen EU-Listung, nationale Maßnahme oder Bankentscheidung. |

Die Reihenfolge zeigt den fachlichen Zusammenhang, keine Pflicht zur Vollprüfung aller Themen. Jeder Skill lässt sich auch einzeln verwenden; sein Abschnitt „Eingaben“ nennt die benötigten Unterlagen.

## 1.3. Downloads

| Datei | Verwendung | Download |
| --- | --- | --- |
| Plugin 1.0.0 | Zehn installierbare Skills samt lokalen Quellenhinweisen | [eu-sanktionspruefer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/eu-sanktionspruefer.zip) |
| Portables Paket | Anbieterneutrales Manifest und Skills | [eu-sanktionspruefer-portable.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/eu-sanktionspruefer-portable.zip) |
| Werkstatt | Ausführlicher eigenständiger Workflow | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/eu-sanktionspruefer-werkstatt.md" download><code>eu-sanktionspruefer-werkstatt.md</code></a> |
| Schnellstart | Kompakter Einstieg in einen konkreten Vorgang | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/eu-sanktionspruefer-schnellstart.md" download><code>eu-sanktionspruefer-schnellstart.md</code></a> |
| Hauptproblem | Eine zurückgehaltene Transaktion rechtlich klären | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/eu-sanktionspruefer-hauptproblem.md" download><code>eu-sanktionspruefer-hauptproblem.md</code></a> |

Die Paketlinks verwenden den gemeinsamen Release-Tag `sanktionen-eu-us-v1.0.0`. Die Markdown-Downloads führen über die Downloadseite des Repositories und liefern den aktuellen Inhalt der jeweiligen Datei.

## 1.4. Quellen und Grenzen

Das [Quellenregister](references/quellenregister.md) nennt amtliche Fundstellen, Prüfdatum 21.10.2026 und Aussagegrenzen. Die [Zitierweise](references/zitierweise.md) verlangt eine konkrete Norm- und Belegzuordnung. Berücksichtigt werden unter anderem EM System, T Trust, Inter Rao Lietuva und Bank Melli Iran sowie die Terrorismusänderung durch Verordnung 2026/456. EU-Eigentum, aggregierte Beteiligungen und Kontrolle werden nicht mit der US-50-Percent-Rule gleichgesetzt.

Das Paket enthält keinen laufend synchronisierten Sanktionsdatenbestand und behauptet keinen automatischen Live-Abgleich. Vor einer realen Handlung sind aktuelle Rechtsakte, Listungen und Eigentumsverhältnisse zu prüfen. Fehlt der Zugang, entsteht eine gezielte Nachforderung mit begrenztem Entwurf, keine Freigabe. BAFA-Direktabrufe waren bei der Quellenprüfung teilweise gesperrt; diese Zugriffslücke ist ausdrücklich dokumentiert.

Keine selbständige Zahlung, Lieferung, Entsperrung, Meldung oder Antragstellung. Ein verantwortlicher Mensch prüft die konkrete Handlung. Erfundene Schulungslistungen bleiben vollständig außerhalb produktiver Listen, Kundenregister und realer Meldungen. Das Paket ersetzt keine verantwortliche rechtliche Einzelfallprüfung. Importstruktur und redaktionelle Prüfung belegen keine beobachtete Laufzeitqualität in jeder Oberfläche.

## 1.5. Vierzig Prozent, Kontrolle und Mandatsgeld

Die beiden Akten enthalten jeweils zwölf vollständige Originale: fünf Word-Dokumente, vier E-Mails mit tatsächlich beigefügten Anlagen, zwei Zahlentabellen und einen Gesprächs- oder Nachrichtenverlauf. Alle Personen, Unternehmen, Staaten und Listungsentscheidungen sind erfunden. Die Listungsdokumente sind ausdrücklich als unechte Rechtsakte gekennzeichnet. Keine Musterlösung und keine Einordnung realer Personen als Sanktionierte.

### 1.5.1. Zwirnmark: Ersatzteile und Gesellschafterpost

Ein Ersatzteilauftrag über 86.400 EUR, eine noch nicht gutgeschriebene Anzahlung, eine Gesellschafterkartei und besondere Besetzungsrechte im Verwaltungsrat treffen auf widersprüchliche Auskünfte aus Einkauf und Bank. [Unterlagenverzeichnis](../testakten/sanktionen-eu-zwirnmark-beteiligung/README.md).

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamtakte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/sanktionen-eu-zwirnmark-beteiligung_gesamt.pdf) |
| Einzel-PDF-ZIP / Individual PDFs | [Einzelne Dokumente](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/testakte-sanktionen-eu-zwirnmark-beteiligung-einzelpdfs.zip) |
| Originalformat-ZIP / Native documents | [DOCX, EML, CSV und TXT](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/testakte-sanktionen-eu-zwirnmark-beteiligung.zip) |

### 1.5.2. Faltenfels: Mandatspost und Lieferkisten

Eine Kanzlei vertritt ein erfundenes gelistetes Unternehmen. Ein selbständiger Hilfsverein organisiert gleichzeitig eine Lieferung über dessen Lager; Honorar, Spendenmittel und Transportkosten werden in den Schreiben unterschiedlich zugeordnet. [Unterlagenverzeichnis](../testakten/sanktionen-eu-faltenfels-mandat/README.md).

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamtakte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/sanktionen-eu-faltenfels-mandat_gesamt.pdf) |
| Einzel-PDF-ZIP / Individual PDFs | [Einzelne Dokumente](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/testakte-sanktionen-eu-faltenfels-mandat-einzelpdfs.zip) |
| Originalformat-ZIP / Native documents | [DOCX, EML, CSV und TXT](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/sanktionen-eu-us-v1.0.0/testakte-sanktionen-eu-faltenfels-mandat.zip) |

Die ZIPs enthalten keine Unterordner. Gesamt-PDF und Einzel-PDFs geben dieselben zwölf Originale wieder; die Archive enthalten zusätzlich eine zweisprachige Hinweisdatei. Die Akten werden nicht mit dem Plugin installiert.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## 1.6. Alle Skills alphabetisch

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`eu-anwendungsbereich-regime-bestimmen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-anwendungsbereich-regime-bestimmen/SKILL.md) | Bestimmt für eine Zahlung, Lieferung oder Beratung die einschlägigen EU-Sanktionsregime und deren persönlichen, räumlichen und zeitlichen Geltungsbereich. Trennt Terrorismus, Ländermaßnahmen und thematische Sanktionen und erstellt eine k... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-anwendungsbereich-regime-bestimmen/SKILL.md) |
| [`eu-ausnahmen-genehmigungen-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-ausnahmen-genehmigungen-vorbereiten/SKILL.md) | Trennt unmittelbar geltende Ausnahmen von vorheriger behördlicher Genehmigung bei EU-Sanktionen. Erstellt konkrete Anträge für Grundbedarf, Rechtskosten oder andere belegte Ausnahmetatbestände und prüft Zuständigkeit, Betrag, Zahlungsweg... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-ausnahmen-genehmigungen-vorbereiten/SKILL.md) |
| [`eu-eigentum-kontrolle-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-eigentum-kontrolle-pruefen/SKILL.md) | Untersucht Beteiligungsketten, zusammengerechnete gelistete Anteile, Stimmrechte und tatsächliche Kontrolle nach EU-Sanktionsrecht. Verarbeitet EM System, T Trust und Inter Rao Lietuva und erstellt einen belegten Kontrollvermerk oder ein... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-eigentum-kontrolle-pruefen/SKILL.md) |
| [`eu-gelder-ressourcen-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-gelder-ressourcen-sichern/SKILL.md) | Prüft Einfrieren und Bereitstellungsverbote für Zahlungen, Konten, Sicherheiten und wirtschaftliche Ressourcen. Erstellt einen konkreten Sicherungs- und Bankkommunikationsentwurf und trennt Gutschrift, Verfügung, Rückzahlung und Beschlag... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-gelder-ressourcen-sichern/SKILL.md) |
| [`eu-handel-dienstleistungen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-handel-dienstleistungen-pruefen/SKILL.md) | Prüft EU-Beschränkungen für Waren, Software, technische Hilfe und Beratungsleistungen auch ohne Listentreffer. Ordnet Produkt, Empfänger, Endverwendung und Leistungsart zu und erstellt eine begründete Liefer- oder Mandatsauskunft mit kon... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-handel-dienstleistungen-pruefen/SKILL.md) |
| [`eu-listentreffer-identitaet-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-listentreffer-identitaet-klaeren/SKILL.md) | Klärt EU-Sanktionslistentreffer anhand konkreter Personen- und Unternehmensidentifikatoren. Unterscheidet bestätigten Treffer, Verwechslung und offenen Befund und erstellt eine gezielte Nachforderung oder Bankenantwort ohne Namensähnlich... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-listentreffer-identitaet-klaeren/SKILL.md) |
| [`eu-meldung-verschwiegenheit-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-meldung-verschwiegenheit-klaeren/SKILL.md) | Prüft fallbezogen Informations- und Mitwirkungspflichten bei EU-Sanktionen sowie anwaltliche Vertraulichkeit. Erstellt einen begründeten Meldeentwurf oder Abgrenzungsvermerk mit richtigem Adressaten und notwendigem Umfang statt pauschale... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-meldung-verschwiegenheit-klaeren/SKILL.md) |
| [`eu-rechtsschutz-entlistung-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-rechtsschutz-entlistung-vorbereiten/SKILL.md) | Unterscheidet EU-Listung, nationale Einfriermaßnahme und privatrechtliche Bankensperre und bereitet den passenden Rechtsschutz vor. Erstellt Entlistungseingabe, Bankenschreiben oder verfahrensbezogenen Entwurf mit Beweisen, Fristen und G... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-rechtsschutz-entlistung-vorbereiten/SKILL.md) |
| [`eu-sanktionsfall-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-sanktionsfall-steuern/SKILL.md) | Führt die EU-Sanktionsprüfung für Unternehmen und Kanzleien vom konkreten Geschäft oder Mandat über Identität und Kontrolle bis zum begründeten Schreiben oder Antrag. Verbindet neun Fachskills und trennt ungeklärte Treffer von gesetzlich... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-sanktionsfall-steuern/SKILL.md) |
| [`eu-vertraege-drittstaatenkonflikte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-vertraege-drittstaatenkonflikte-bearbeiten/SKILL.md) | Bearbeitet sanktionsbedingte Vertragsstörungen und Konflikte mit Drittstaatenrecht einschließlich EU-Blocking-Verordnung. Prüft Leistungsstopp, Kündigung, Bankenforderung und Klauseln und erstellt einen begründeten Brief oder Nachtrag un... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=eu-sanktionspruefer/skills/eu-vertraege-drittstaatenkonflikte-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

# 2. English

## 2.1. Purpose and starting point

This package helps companies and law firms assess a specific payment, supply, service or asset transaction under EU restrictive measures. It moves from the available documents to a reasoned bank letter, authorisation application or internal decision proposal. It covers country-based and thematic regimes, including terrorism, rather than treating Russia sanctions as the whole field.

Start with the bank notice, contract or proposed transaction and state the required output. The main skill, `eu-sanktionsfall-steuern`, selects only the necessary specialist steps, asks targeted questions and continues the same document after new evidence arrives. A negative name match does not rule out ownership, control or sectoral restrictions.

## 2.2. Files and use

The table above lists ten installed skills: one coordinator and nine specialist workflows. The workshop Markdown is the detailed standalone instruction; the quick-start is the compact entry point; the main-problem prompt addresses a transaction held back on sanctions grounds. Both compact files remain below 7,000 UTF-8 bytes even with CRLF line endings. Standalone prompts are not additional installed skills.

Download links are in [section 1.3](#13-downloads). The two fictional case files in [section 1.5](#15-vierzig-prozent-kontrolle-und-mandatsgeld) each provide twelve native documents, a combined PDF and a flat archive of individual PDFs. They are separate from the installed plugin. Package assets use release tag `sanktionen-eu-us-v1.0.0`. Import support and available tools depend on the host application; no universal runtime or live-screening test is claimed.

## 2.3. Evidence and safeguards

The local source register records official references checked on 21 October 2026, the scope of each proposition and access limitations. EU ownership aggregation, rebuttable control assessments and indirect availability must not be replaced with the US OFAC rule. Sectoral prohibitions can apply to an unlisted counterparty.

Current legislation, list entries and transaction evidence must be obtained for the actual matter. Missing access produces a targeted evidence request and a limited draft, not clearance. A human must approve any external filing, payment, delivery or release of assets. Fictional training designations must never enter production screening data, client records or real reports.
