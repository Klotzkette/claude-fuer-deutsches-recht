<!-- decimal-anchor --> <a id="weg--und-hausverwaltung"></a>

# 1. WEG- und Hausverwaltung

<!-- BEGIN direkt-loslegen (autogen) -->
<!-- decimal-anchor --> <a id="was-ist-das-hier"></a>

## 1.1. Was ist das hier?

WEG-Hausverwaltung von Belegen und Bankbewegungen über Jahresabrechnung, Eigentümerrückfragen und Mietüberleitung bis zu Beschlüssen, Handwerkeraufträgen und Schadenfällen einschließlich Diebstahl und Bettwanzen.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

<!-- decimal-anchor --> <a id="welche-datei-wofür--which-file-should-i-use"></a>

## 1.2. Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`weg-hausverwaltung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/weg-hausverwaltung.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/weg-hausverwaltung.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-schnellstart.txt) |
| Schwerpunkt-Prompt | Eigenständiger, eng abgegrenzter Mandatsauftrag bis 7500 Zeichen. Der zugehörige Fachskill ist auch im Plugin vorhanden. | Standalone workflow for one demanding practice problem, up to 7500 characters. Its corresponding skill is also part of the plugin. | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-hauptproblem.md" download>MD herunterladen / Download MD</a> · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-hauptproblem.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/weg-hausverwaltung.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

<!-- decimal-anchor --> <a id="in-30-sekunden-starten"></a>

## 1.3. In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/weg-hausverwaltung.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für WEG- und Hausverwaltung:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

<!-- decimal-anchor --> <a id="downloads"></a>

## 1.4. Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`weg-hausverwaltung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/weg-hausverwaltung.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`weg-hausverwaltung-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-schnellstart.md) · [`weg-hausverwaltung-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`weg-hausverwaltung-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-werkstatt.md) · [`weg-hausverwaltung-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-werkstatt.txt) |
| Schwerpunkt-Prompt (Hauptproblem) | Markdown / identisches TXT | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-hauptproblem.md" download>weg-hausverwaltung-hauptproblem.md</a> · [`weg-hausverwaltung-hauptproblem.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-hauptproblem.txt) |
| Zugeordnete Testakten | PDF / ZIP | [8 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

<!-- decimal-anchor --> <a id="zugeordnete-testakten"></a>

## 1.5. Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Bauträgervertrag Birkenpfuhl - Wohnung 4.27](../testakten/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung/README.md) | [Gesamt-PDF](../testakten/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung/gesamt-pdf/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung_gesamt.pdf) | [`testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung.zip) | [`testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung-einzelpdfs.zip) |
| [Betriebskosten 2025: Vermietete Eigentumswohnung in Berlin-Schöneberg](../testakten/betriebskosten-2025-weg-schoeneberg/README.md) | [Gesamt-PDF](../testakten/betriebskosten-2025-weg-schoeneberg/gesamt-pdf/betriebskosten-2025-weg-schoeneberg_gesamt.pdf) | [`testakte-betriebskosten-2025-weg-schoeneberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-pflegerecht-v1.0.0/testakte-betriebskosten-2025-weg-schoeneberg.zip) | [`testakte-betriebskosten-2025-weg-schoeneberg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-betriebskosten-2025-weg-schoeneberg-einzelpdfs.zip) |
| [WEG Hohenzollernhof — Hausverwaltung unter Druck](../testakten/weg-hausverwaltung-hohenzollernhof/README.md) | [Gesamt-PDF](../testakten/weg-hausverwaltung-hohenzollernhof/gesamt-pdf/weg-hausverwaltung-hohenzollernhof_gesamt.pdf) | [`testakte-weg-hausverwaltung-hohenzollernhof.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-weg-hausverwaltung-hohenzollernhof.zip) | [`testakte-weg-hausverwaltung-hohenzollernhof-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-weg-hausverwaltung-hohenzollernhof-einzelpdfs.zip) |
| [1. Kastanienhof und die offene Kellertür](../testakten/weg-kastanienhof-kellerdiebstahl/README.md) | [Gesamt-PDF](../testakten/weg-kastanienhof-kellerdiebstahl/gesamt-pdf/weg-kastanienhof-kellerdiebstahl_gesamt.pdf) | [`testakte-weg-kastanienhof-kellerdiebstahl.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-weg-kastanienhof-kellerdiebstahl.zip) | [`testakte-weg-kastanienhof-kellerdiebstahl-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-weg-kastanienhof-kellerdiebstahl-einzelpdfs.zip) |
| [1. Kleinhausen](../testakten/weg-kleinhausen/README.md) | [Gesamt-PDF](../testakten/weg-kleinhausen/gesamt-pdf/weg-kleinhausen_gesamt.pdf) | [`testakte-weg-kleinhausen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-weg-kleinhausen.zip) | [`testakte-weg-kleinhausen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-weg-kleinhausen-einzelpdfs.zip) |
| [1. Lindenhof und die zweite Abrechnungsfassung](../testakten/weg-lindenhof-jahresabrechnung-2025/README.md) | [Gesamt-PDF](../testakten/weg-lindenhof-jahresabrechnung-2025/gesamt-pdf/weg-lindenhof-jahresabrechnung-2025_gesamt.pdf) | [`testakte-weg-lindenhof-jahresabrechnung-2025.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-weg-lindenhof-jahresabrechnung-2025.zip) | [`testakte-weg-lindenhof-jahresabrechnung-2025-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-weg-lindenhof-jahresabrechnung-2025-einzelpdfs.zip) |
| [1. Sonnenwinkel und die ungeklärte Befallsquelle](../testakten/weg-sonnenwinkel-bettwanzen/README.md) | [Gesamt-PDF](../testakten/weg-sonnenwinkel-bettwanzen/gesamt-pdf/weg-sonnenwinkel-bettwanzen_gesamt.pdf) | [`testakte-weg-sonnenwinkel-bettwanzen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-weg-sonnenwinkel-bettwanzen.zip) | [`testakte-weg-sonnenwinkel-bettwanzen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-weg-sonnenwinkel-bettwanzen-einzelpdfs.zip) |
| [1. Spreebogen und das weitergereichte Hausgeld](../testakten/weg-spreebogen-mieterumlage-belege/README.md) | [Gesamt-PDF](../testakten/weg-spreebogen-mieterumlage-belege/gesamt-pdf/weg-spreebogen-mieterumlage-belege_gesamt.pdf) | [`testakte-weg-spreebogen-mieterumlage-belege.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-weg-spreebogen-mieterumlage-belege.zip) | [`testakte-weg-spreebogen-mieterumlage-belege-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-weg-spreebogen-mieterumlage-belege-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

<!-- decimal-headings -->
<!-- decimal-anchor --> <a id="abrechnungen-und-alltagsfälle-vollständig-bearbeiten"></a>

## 1.6. Abrechnungen und Alltagsfälle vollständig bearbeiten

Die bestehende WEG-Werkstatt führt die Belegkette bis zum fertigen Ergebnis: Lieferantenrechnung, Leistungsnachweis, Bankbewegung, Verteilungsschlüssel, Einzelabrechnung, Beschluss und Antwort an den Eigentümer. Für vermietete Einheiten folgt eine eigene Prüfung der mietrechtlichen Umlage. Rücklagen, Verwaltungsvergütung, Reparaturen und Hausgeld werden nicht unverändert an Mieter weitergereicht.

Die 93 vorhandenen Skills bleiben erhalten. Aktualisierte Fachrouten behandeln insbesondere Sollvorschüsse und Istzahlungen, Belegeinsicht, gemischte Hausmeisterkosten, notwendige Sicherungsmaßnahmen, Versicherungen und Bettwanzen. Der neue Hauptproblem-Prompt bündelt die Bearbeitung eines Abrechnungsvorgangs; Werkstatt und Mini führen auch durch die weiteren Verwaltungsaufgaben.

| Arbeitsform | Passender Einstieg |
| --- | --- |
| Einzelabrechnung und Eigentümerrückfrage | Hauptproblem-Prompt als [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-hauptproblem.md) oder [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-hauptproblem.txt) mit den zugehörigen Belegen verwenden. |
| Vielseitige Verwaltungsanfrage | [Mini-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-schnellstart.md) für den konkreten Auftrag laden. |
| Mehrstufige Abrechnung oder Schadenakte | [Werkstatt-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/weg-hausverwaltung-werkstatt.md) mit vorhandener Korrespondenz und Rechnungen verwenden. |
| Werkstatt bearbeiten oder ausdrucken | [Word-Datei](./assets/weg-hausverwaltung-werkstatt.docx) oder [PDF-Lesefassung](./assets/weg-hausverwaltung-werkstatt.pdf). |

Alle drei Prompts stehen zusätzlich als unveränderte UTF-8-Textdateien bereit. Ein Einstieg genügt; die drei Fassungen brauchen nicht gemeinsam in denselben Auftrag geladen zu werden.

<!-- decimal-anchor --> <a id="einfach-einsteigen-und-weitere-verwaltungsfälle-bearbeiten"></a>

## 1.7. Einfach einsteigen und weitere Verwaltungsfälle bearbeiten

- **[Kleinhausen – einfacher Einstieg](../testakten/weg-kleinhausen/README.md):** fünf Wohnungen mit gleichen Anteilen, ein übersichtliches Abrechnungsjahr, normale Belege und freundliche Rückfragen. Eine bearbeitbare Tabelle und fünf Einzelabrechnungen ermöglichen die praktische Bearbeitung weniger kleiner Übertragungsfehler.
- [Lindenhof](../testakten/weg-lindenhof-jahresabrechnung-2025/README.md): acht Eigentümereinheiten, Jahresabrechnung 2025, Rücklage, Einzelabrechnungen und Rückfragen nach dem Versand.
- [Spreebogen](../testakten/weg-spreebogen-mieterumlage-belege/README.md): vermietete Eigentumswohnung, Kostenüberleitung, Heiz- und CO2-Unterlagen, Belegeinsicht und Mietereinwendungen.
- [Kastanienhof](../testakten/weg-kastanienhof-kellerdiebstahl/README.md): Kellerdiebstahl, beschädigte Schließanlage, getrennte Versicherungsfragen und ein Kameraangebot.
- [Sonnenwinkel](../testakten/weg-sonnenwinkel-bettwanzen/README.md): Befund, Behandlung, Nachkontrolle, Terminprobleme und streitige Kostenzuordnung ohne vorschnelle Verursacherbehauptung.

Die bisherige große Akte Hohenzollernhof und die bereits zugeordneten Fälle bleiben verfügbar. Die neuen Arbeitsunterlagen enthalten keine Musterlösung; Nachweise, Entwürfe und Aussagen der Beteiligten sind selbst auszuwerten.

<!-- decimal-anchor --> <a id="quellenstand-und-überprüfte-grenzen"></a>

## 1.8. Quellenstand und überprüfte Grenzen

Rechtsstand der Überarbeitung: 2. Oktober 2026. Die [WEG-Referenz](./references/rechtsstand-oktober-2026.md) ordnet amtlich geprüfte Entscheidungen nach ihrer konkreten Aussage und Reichweite ein. Aktuelle Anker betreffen unter anderem Handwerkerangebote, Kostenschlüssel und Schäden am Sondereigentum. Die Werkstatt unterscheidet die jeweils einschlägige Normfassung von erst später eintretenden Kostenfolgen.

[Prüfunterlagen](../quality/source-audits/weg-hausverwaltung-2026-10-02/) trennen Quellenlektüre, redaktionelle Gegenlese, technische Kontrollen und tatsächliche Anwendungsproben. Eine technische Prüfung ersetzt keine rechtliche Bewertung des späteren Einzelfalls. Historische Rechtsprechung wird mit WEMoG, DSGVO und der seit 2025 möglichen elektronischen Belegbereitstellung abgeglichen.


Aus Rechnungen, Bankbewegungen, Abrechnungsfassungen und Eigentümerrückfragen entstehen abgestimmte Zahlen, verständliche Antwortbriefe und konkrete Verwaltungsschritte.
Operatives Plugin für Wohnungseigentümergemeinschaften, Hausverwaltungen, Verwaltungsbeiräte und anwaltliche Begleitung. Der Schwerpunkt liegt nicht auf abstrakter Dogmatik, sondern auf den täglichen Vorgängen: Eigentümerversammlung vorbereiten, Beschlussvorlagen schreiben, Beschlüsse protokollieren, Beschlusssammlung pflegen, Wirtschaftsplan und Jahresabrechnung prüfen, Hausgeld und Sonderumlagen verfolgen, Betriebskosten/Nebenkosten kontrollieren, Handwerker beauftragen, Erhaltungsmaßnahmen steuern, Restaurant- und Hausordnungskonflikte sortieren, E-Mobilität/Steckersolar/PV beschlussreif machen und rechtliche Eskalationen rechtzeitig erkennen.

Das Plugin arbeitet paralegal-praktisch: Es erstellt keine "Rechtsberatung aus dem Nichts", sondern strukturiert Akten, formuliert Beschluss- und Anschreibenentwürfe, baut Prüfmatrizen, markiert Fristen, trennt kaufmännische Verwaltung von Rechtsfragen und schlägt bei Risiko den passenden Anwalts- oder Gerichtspfad vor.

<!-- decimal-anchor --> <a id="installation-in-der-plugin-umgebung"></a>

## 1.9. Installation in der Plugin-Umgebung

1. ZIP herunterladen.
2. Plugin-Umgebung -> **Customize → Plugins** -> **Upload plugin** -> Datei wählen.
3. Plugin aktivieren und eine neue Aufgabe öffnen; den passenden Skill ausdrücklich auswählen.

> Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code -> Download ZIP" verwenden.

<!-- decimal-anchor --> <a id="quellen--und-rollenregel"></a>

## 1.10. Quellen- und Rollenregel

- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Bei streitigen Beschlüssen, Verjährung, Anfechtung, Schadensersatz, Verwalterhaftung oder gerichtlichen Schritten immer anwaltliche Eskalation markieren.
- Verwaltungspraxis, kaufmännische Kontrolle und juristische Bewertung werden sichtbar getrennt.

<!-- decimal-anchor --> <a id="enthaltene-skills"></a>

## 1.11. Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `kaltstart-triage` | Einstieg, Unterlagensichtung und Wahl des Fachwegs im WEG-/Hausverwaltungsalltag. |
| `rechtsstand-mai-2026-faktenbank` | Quellen-Gate mit WEG/BGB/BetrKV-Ankern und frei verifizierten BGH-Linien. |
| `mandat-objekt-triage` | Objekt, Gemeinschaft, Rollen, Verwaltervertrag, Teilungserklärung, Fristen und Aktenlage erfassen. |
| `grossakte-konfliktlandkarte` | Große unübersichtliche Verwaltungsakten clustern, priorisieren und in passende Spezial-Skills routen. |
| `eigentuemerversammlung-vorbereiten` | Versammlung vom Themenstapel bis zur Beschlussreife planen. |
| `einladung-tagesordnung-fristen` | Einladung, Tagesordnung, Ladungsfristen und Vollmachten prüfen. |
| `beschlussvorlagen-erstellen` | Rechtssichere und verständliche Beschlussvorlagen mit Alternativen formulieren. |
| `protokollwerkstatt-top-marathon` | Lange Eigentümerversammlungen mit vielen TOPs protokollfähig strukturieren. |
| `beschlusssammlung-protokoll` | Protokoll, Beschlusssammlung, Verkündung, Anlagen und Nachversand strukturieren. |
| `beschlussanfechtung-risiko` | Anfechtungs- und Nichtigkeitsrisiken nach §§ 44 und 45 WEG erkennen. |
| `wirtschaftsplan-jahresabrechnung-28-weg` | Wirtschaftsplan, Jahresabrechnung, Vermögensbericht, Nachschüsse und Vorschüsse prüfen. |
| `abrechnung-ist-plan-mieterschnittstelle` | Ist-/Plan-Kosten, Verteilerschlüssel, Betriebskosten und vermietende Eigentümer zusammenführen. |
| `hausgeld-sonderumlage-liquiditaet` | Hausgeldrückstände, Sonderumlagen, Liquidität, Mahnung und Klagepfad ordnen. |
| `betriebskosten-nebenkostenabrechnung` | Betriebskosten/Nebenkosten nach BetrKV, Mietvertrag und WEG-Abrechnung kontrollieren. |
| `handwerker-beauftragung-vergabe` | Angebote einholen, vergleichen, beauftragen, Nachträge prüfen und Dokumentation sichern. |
| `erhaltung-modernisierung-baumaengel` | Erhaltung, Modernisierung, Mängel, Gewährleistung und Bauüberwachung verwalten. |
| `heizung-schaden-versicherung-notmassnahme` | Heizungsstörung, Wasserschaden, Versicherung, Sofortmaßnahme und Beschlussnachlauf ordnen. |
| `bauliche-veraenderungen-20-weg` | Bauliche Veränderungen nach §§ 20 und 21 WEG beschlussfähig vorbereiten. |
| `steckersolar-wallbox-barrierefreiheit` | Privilegierte Maßnahmen: Steckersolar, E-Mobilität, Einbruchsschutz, Glasfaser, Barrierefreiheit. |
| `e-mobilitaet-steckersolar-kellerstrom` | Wallbox, Ladeinfrastruktur, Dach-PV, Steckersolar und riskante Kellerstrom-Provisorien prüfen. |
| `verwalterpflichten-26-27-weg` | Bestellung, Abberufung, Vertretungsmacht, Maßnahmenkatalog, Verwaltervertrag. |
| `eigentuemerkommunikation-beschwerde` | Eigentümerkommunikation, Beschwerden, Eskalationsmails und transparente Antwortbausteine. |
| `stoerung-hausordnung-mieter-eigentuemer` | Lärm, Müll, Feuchtigkeit, Gemeinschaftsflächen, Mieter als Störer, Hausordnung. |
| `gewerbe-restaurant-geruch-laerm-hof` | Restaurant-/Gewerbekonflikte mit Geruch, Lärm, Müll, Lieferverkehr, Hofnutzung und Betreiberrollen. |
| `hausordnung-tauben-fahrrad-kinder-weihnachtsbaum` | Alltagssachen sauber sortieren: Tauben, Fahrraddiebstahl, Kinder, Weihnachtsbaum, Fluchtwege. |
| `beirat-controlling-verwalter` | Verwaltungsbeirat: Rechnungsprüfung, Angebotskontrolle, Protokollcheck, Eskalationsnotiz. |
| `datenschutz-dokumentenfreigabe` | DSGVO, Eigentümerlisten, Belegeinsicht, Schwärzungen, Cloud-Freigaben. |
| `eskalation-anwalt-amtsgericht` | Wann Anwalt, Amtsgericht, Beschlussklage, Hausgeldklage oder einstweiliger Rechtsschutz nötig wird. |

<!-- decimal-anchor --> <a id="typische-workflows"></a>

## 1.12. Typische Workflows

**Eigentümerversammlung:** `grossakte-konfliktlandkarte` -> `eigentuemerversammlung-vorbereiten` -> `einladung-tagesordnung-fristen` -> `beschlussvorlagen-erstellen` -> `protokollwerkstatt-top-marathon` -> `beschlussanfechtung-risiko`.

**Jahresabrechnung:** `wirtschaftsplan-jahresabrechnung-28-weg` -> `abrechnung-ist-plan-mieterschnittstelle` -> `beirat-controlling-verwalter` -> `hausgeld-sonderumlage-liquiditaet` -> bei vermieteten Wohnungen zusätzlich `betriebskosten-nebenkostenabrechnung`.

**Handwerkermaßnahme:** `erhaltung-modernisierung-baumaengel` -> `handwerker-beauftragung-vergabe` -> `beschlussvorlagen-erstellen` -> `eigentuemerkommunikation-beschwerde` -> bei Streit `eskalation-anwalt-amtsgericht`.

**Alltagskonflikt:** `grossakte-konfliktlandkarte` -> `hausordnung-tauben-fahrrad-kinder-weihnachtsbaum` oder `gewerbe-restaurant-geruch-laerm-hof` -> `eigentuemerkommunikation-beschwerde` -> bei hartem Konflikt `eskalation-anwalt-amtsgericht`.

<!-- decimal-anchor --> <a id="grenzen"></a>

## 1.13. Grenzen

Das Plugin ersetzt keine anwaltliche Beratung, keine WEG-Spezialkanzlei, keine Steuerberatung und keine technische Bauleitung. Es hilft, die Verwaltung so zu dokumentieren, dass Anwälte, Beiräte, Verwalter und Eigentümer sauber weiterarbeiten können.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **15 auswählbare Skills**. Die **93 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

<!-- decimal-anchor --> <a id="orientierung-nach-arbeitslogik"></a>

## 1.14. Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/juristischer-argumentationskern/SKILL.md), [`wirtschaftsplan-jahresabrechnung-28-weg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/wirtschaftsplan-jahresabrechnung-28-weg/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Gemeinschaft und Gegenstand | [`gemeinschaft-und-gegenstand-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/gemeinschaft-und-gegenstand-bearbeiten/SKILL.md) |
| 3. Beleg und Bank | [`beleg-und-bank-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/beleg-und-bank-bearbeiten/SKILL.md) |
| 4. Abrechnung und Eigentümerkonto | [`abrechnung-und-eigentuemerkonto-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/abrechnung-und-eigentuemerkonto-bearbeiten/SKILL.md) |
| 5. Fassung und Antwort | [`fassung-und-antwort-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/fassung-und-antwort-bearbeiten/SKILL.md) |
| 6. Mietüberleitung | [`mietueberleitung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/mietueberleitung-bearbeiten/SKILL.md) |
| 7. Beschlussarbeit | [`beschlussarbeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/beschlussarbeit-bearbeiten/SKILL.md) |
| 8. Maßnahme und Pflicht | [`massnahme-und-pflicht-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/massnahme-und-pflicht-bearbeiten/SKILL.md) |
| 9. Diebstahl und Befall | [`diebstahl-und-befall-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/diebstahl-und-befall-bearbeiten/SKILL.md) |
| 10. Rechtsschutz und Output | [`rechtsschutz-und-output-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/rechtsschutz-und-output-bearbeiten/SKILL.md) |
| 11. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 12. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

<!-- decimal-anchor --> <a id="alle-skills-im-überblick"></a>

## 1.15. Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 15 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 15 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`abrechnung-und-eigentuemerkonto-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/abrechnung-und-eigentuemerkonto-bearbeiten/SKILL.md) | WEG- und Hausverwaltung: Abrechnung und Eigentümerkonto: Verteilbare Jahreskosten gegen beschlossene Sollvorschüsse rechnen; offene Vorschüsse, Rücklagenbeiträge und spätere Ausgleichszahlungen getrennt verfolgen. Jede Einzelabrechnung a... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/abrechnung-und-eigentuemerkonto-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Für Wohnungseigentums- und Hausverwaltungsrecht: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`beleg-und-bank-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/beleg-und-bank-bearbeiten/SKILL.md) | WEG- und Hausverwaltung: Beleg und Bank: Leistung, Rechnung, Zahlung, Buchungsjahr und Konto verbinden; Betriebskonto, Rücklagenkonto und Umbuchungen abstimmen. Ein Angebot ist keine Rechnung, ein Kontotransfer kein neuer Aufwand und ein... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/beleg-und-bank-bearbeiten/SKILL.md) |
| [`beschlussarbeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/beschlussarbeit-bearbeiten/SKILL.md) | Für Wohnungseigentums- und Hausverwaltungsrecht: Beschlussarbeit: Beschlusskompetenz, Einberufung, Tagesordnung, Bestimmtheit, Mehrheit, Verkündung, Niederschrift und Beschlusssammlung lückenlos prüfen. Vollständige Fachanweisungen und l... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/beschlussarbeit-bearbeiten/SKILL.md) |
| [`diebstahl-und-befall-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/diebstahl-und-befall-bearbeiten/SKILL.md) | WEG- und Hausverwaltung: Diebstahl und Befall anhand belegter Tatsachen klären, private Gegenstände und Gemeinschaftsmaßnahmen trennen. Bettwanzen fachkundig feststellen, Zugang und Kosten eines Ausbruchs prüfen; keine Schuldzuweisung au... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/diebstahl-und-befall-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: WEG- und Hausverwaltung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/einstieg-routing/SKILL.md) |
| [`fassung-und-antwort-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/fassung-und-antwort-bearbeiten/SKILL.md) | WEG- und Hausverwaltung: Fassung und Antwort: Versandte Vorfassung, Rückfrage, ergänzter Nachweis und Korrektur nachvollziehbar verbinden. Anschreiben, Abrechnung, Belegliste, Zugangstermin und Beschlussvorlage je Empfänger passend zusam... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/fassung-und-antwort-bearbeiten/SKILL.md) |
| [`gemeinschaft-und-gegenstand-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/gemeinschaft-und-gegenstand-bearbeiten/SKILL.md) | Für Wohnungseigentums- und Hausverwaltungsrecht: Gemeinschaft und Gegenstand: Einheit, Gemeinschafts- oder Sondereigentum, Gemeinschaftsordnung, Beteiligte, Vertretung und konkretes Verwaltungsziel feststellen. Vollständige Fachanweisung... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/gemeinschaft-und-gegenstand-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/juristischer-argumentationskern/SKILL.md) | WEG-Verwaltungsvorgang bis zum wirksamen Beschluss oder Anspruchstext führen. Nutzt vorhandene Falldaten, entscheidet die maßgeblichen rechtlichen Abzweigungen und verbindet passende Fachprüfungen mit einem vollständig ausgearbeiteten Er... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/juristischer-argumentationskern/SKILL.md) |
| [`massnahme-und-pflicht-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/massnahme-und-pflicht-bearbeiten/SKILL.md) | Für Wohnungseigentums- und Hausverwaltungsrecht: Maßnahme und Pflicht: Erhaltung, bauliche Veränderung, privilegierte Maßnahme, Verwalterhandlung, Handwerkerauftrag, Versicherung und Kostenfolge trennen. Vollständige Fachanweisungen und... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/massnahme-und-pflicht-bearbeiten/SKILL.md) |
| [`mietueberleitung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/mietueberleitung-bearbeiten/SKILL.md) | WEG- und Hausverwaltung: Mietüberleitung: Auftrag und Mietvertrag prüfen, Kostenarten bereinigen, Hausmeisteranteile belegen, Wärme und CO2 für das betreffende Jahr rechnen sowie Vorauszahlungen, Zugang, Fristen und Belegeinsicht gesonde... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/mietueberleitung-bearbeiten/SKILL.md) |
| [`rechtsschutz-und-output-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/rechtsschutz-und-output-bearbeiten/SKILL.md) | Für Wohnungseigentums- und Hausverwaltungsrecht: Rechtsschutz und Output: Monats- und Zweimonatsfrist, Klagegegner, Amtsgericht, Antrag, Begründungsstoff und sofort nutzbaren Beschluss-, Protokoll-, Abrechnungs- oder Schriftsatzentwurf e... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/rechtsschutz-und-output-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Für Wohnungseigentums- und Hausverwaltungsrecht: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. Vollständige Fachanweisungen und... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`wirtschaftsplan-jahresabrechnung-28-weg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/wirtschaftsplan-jahresabrechnung-28-weg/SKILL.md) | Erstellt oder prüft Wirtschaftsplan, Jahresabrechnung und Vermögensbericht einer GdWE; trennt Sollvorschüsse, Zahlungen und Nachschüsse und formuliert Abrechnungsbeschluss oder Eigentümerbrief. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/wirtschaftsplan-jahresabrechnung-28-weg/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: WEG- und Hausverwaltung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weg-hausverwaltung/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
