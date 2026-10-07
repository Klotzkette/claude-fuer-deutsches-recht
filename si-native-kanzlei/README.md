# SI-native Kanzlei

Eine Kanzlei, die KI mitdenken lässt und ihre Arbeit im Griff behält: Mandat annehmen, Unterlagen ausarbeiten, tatsächliche Zeit erfassen und den Rechnungsentwurf fortschreiben. „SI-native“ ist ein augenzwinkernder Name. Das Plugin verspricht keine Superintelligenz und ersetzt keine anwaltliche Verantwortung.

## 0. Downloads und Verwendung

Stand: **v445.33.3**, Rechtsquellen geprüft am **7. Oktober 2026**.

| Bestandteil | Direktdownload |
| --- | --- |
| Claude/Codex – Plugin mit 16 Skills | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/si-native-kanzlei.zip) |
| Portables Agent-Plugins-Paket | [Portables ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/si-native-kanzlei-portable.zip) |
| Großer Werkstatt-Prompt | [MD herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=si-native-kanzlei/si-native-kanzlei-werkstatt.md) · [TXT herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=si-native-kanzlei/si-native-kanzlei-werkstatt.txt) |
| Mini-Prompt | [MD herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=si-native-kanzlei/si-native-kanzlei-schnellstart.md) · [TXT herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=si-native-kanzlei/si-native-kanzlei-schnellstart.txt) |
| Hauptproblem-Prompt | [MD herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=si-native-kanzlei/si-native-kanzlei-hauptproblem.md) · [TXT herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=si-native-kanzlei/si-native-kanzlei-hauptproblem.txt) |

Das portable Paket enthält denselben Pluginordner mit Agent-Plugins-1.0-Manifest; die Freischaltung und der Importweg hängen vom jeweiligen ChatGPT-/Codex-Konto ab. Die Standalone-Prompts können ohne Installation mit den verfügbaren Werkzeugen verwendet werden. Lokale Python-Hilfen benötigen tatsächlich ausführbaren Dateizugriff; es gibt keinen automatisch gestarteten Hintergrunddienst. Prompts und Testakten sind separate Downloads und nicht Teil des installierbaren Plugin-ZIPs.

[Alle 16 Skills mit Einzeldownloads](../skills-index/si-native-kanzlei.md) · [Reproduzierbare Ausführung](references/mandatsordner-und-cli.md) · [Testakten auswählen](#7-die-24-kurzfälle)

## 1. Direkt anfangen

> Bearbeite dieses Mandat im ausgewählten Ordner. Beginne mit dem konkret verlangten Dokument. Halte bei jedem wesentlichen Schritt die gespeicherte Honorargrundlage kurz vor. Frage nach tatsächlicher Zeit und Narrativ, soweit diese fehlen, und aktualisiere nach meinen Angaben den Rechnungsentwurf.

Ein kleiner Einzelauftrag funktioniert ebenso:

> Im Mandat M-26-104: heute 18 Minuten Telefonat mit der Mandantin zur Kündigung, abrechenbar. Bitte passend formulieren, eintragen und den Rechnungsentwurf aktualisieren.

Das Plugin übernimmt vorhandene Antworten. Es fragt weder bei jedem Absatz die komplette Honorarvereinbarung neu ab noch erfindet es Zeiten, wenn eine Antwort fehlt.

## 2. Sechzehn Skills

| Skill | Ergebnis |
| --- | --- |
| `si-kanzlei-steuern` | Hauptskill: konkretes Produkt, Aktenstand, Honorar- und Zeitanschluss. |
| `mandatsannahme-interessenkollision` | Richtiger Mandant, Konfliktprüfung und Annahme oder Absage. |
| `akte-fristen-anlegen` | Geordnete Akte und belegte Fristen. |
| `geldwaesche-pruefen` | Anlassbezogene GwG-Prüfung und gezielte Nachweise. |
| `honorar-budget-vereinbaren` | RVG, Stundenhonorar, Festpreis, Quote, Estimate und Deckel konkret klären. |
| `zeiten-erfassen` | Tatsächliche Minuten und Narrativ speichern; Entwurf fortschreiben. |
| `workflow-uebergabe` | Quellen, Fassung, Zuständigkeit und nächsten Schritt übergeben. |
| `recht-recherchieren` | Passende Normen und überprüfte Entscheidungsanker. |
| `schriftsaetze-entwerfen` | Ausformulierter Schriftsatz mit konkreten Anträgen und Belegen. |
| `vertraege-agb-pruefen` | Befunde und vollständige Ersatzklauseln. |
| `vertraege-gestalten` | Kohärenter Vertragsentwurf mit gezielten offenen Fragen. |
| `mandantenkommunikation` | Verständliches Schreiben mit Empfehlung, Frist und Kostenwirkung. |
| `bea-anlagen-vorbereiten` | Zugeordnete, kontrollierte PDF-Kopien und passende Anlagenstempel. |
| `abrechnung-e-rechnung` | Prüffähiger Entwurf und tatsächlicher strukturierter Export, soweit möglich. |
| `zahlungen-buchhaltung` | Belegte Geldflüsse und nachvollziehbarer Buchhaltungsvorschlag. |
| `mandat-abschliessen` | Abschlussbrief, Restpflichten, Abrechnung und Aufbewahrung. |

## 3. Werkstatt, Mini und Hauptproblem

Die Werkstatt führt ausführlich durch den ganzen Ablauf, einschließlich konkreter Dialoge. Der Mini-Prompt ist der kompakte Einstieg. Der Hauptproblem-Prompt konzentriert sich auf das Zusammenspiel von Sacharbeit, Honorarumfang, tatsächlicher Zeit und Rechnungsentwurf. Alle drei funktionieren als eigenständige Texte; die jeweilige TXT-Fassung ist mit der Markdown-Fassung identisch.

In Claude und Codex können die installierten Skills und lokalen Skripte eingesetzt werden. In ChatGPT werden die eigenständigen Prompts mit den dort verfügbaren Dateien und Funktionen verwendet. Kein Prompt schafft automatisch einen dauerhaften Dateizugriff oder einen Hintergrunddienst.

## 4. Was tatsächlich fortgeschrieben wird

Der optionale [lokale Mandatshelfer](references/mandatsordner-und-cli.md) verwaltet bestätigte Angaben mit IDs, Quellen, Korrekturgrund und Honorarphasen. Nach tatsächlichem Aufruf aktualisiert er Zeitliste und Rechnungsentwurf. Er ist keine universelle RVG-, Steuer- oder Finanzbuchhaltungssoftware. Zahlungen und Fremdgelder werden nicht ungeprüft verrechnet.

Eine Festpreisakte kann Zeit für die Nachkalkulation enthalten, ohne dass dadurch die Forderung steigt. Bei Stundenhonorar werden keine hypothetischen Stunden für die Zeitersparnis durch KI erfunden. Gebührenmodell und Budget werden kurz vorgehalten; zusätzliche Aufgaben bleiben gegen den vereinbarten Umfang prüfbar.

## 5. Kleine Fälle für alle Fachanwaltschaften

Zu jedem der 24 Fachgebiete der FAO gehört eine kleine Testakte mit genau zehn Originalstücken: vier E-Mails, eine erklärende Excel-Tabelle, drei PDFs und zwei Word-Dateien. Jede enthält einen konkreten, weiter auszufüllenden Dokumententwurf. So lassen sich Mandatsarbeit und Abrechnung in überschaubaren Fällen gemeinsam üben.

Die Fälle sind fiktiv und bilden keinen vollständigen Fachrechtskommentar. Die [Rechtsquellen](references/rechtsquellen.md) betreffen den Kanzleibetrieb und die fachliche Übergabe; für den konkreten fachlichen Entwurf werden dessen eigene Normen und aktuelle Rechtsprechung geprüft.

## 6. Quellen und Ausführung

Quellenstand: 7. Oktober 2026. Enthalten sind unter anderem die BGH-Urteile vom 19. Februar 2026 zur Reichweite der Honorarvereinbarung und zu Zeitaufstellungen, aktuelle Rechnungsvorgaben, ERVB/beA-Regeln und die anlassbezogene GwG-Prüfung. Die [Arbeitsweise](references/arbeitsweise.md) beschreibt Honoraranschluss, Dateistand und konkrete Grenzen.

Eine vorbereitete Anlage ist noch keine Einreichung. Ein Rechnungsentwurf ist noch keine ausgegebene Rechnung. Eine E-Rechnung wird nur mit tatsächlich erzeugter Datei und passender Validierung als technisch geprüft bezeichnet. Externe Handlungen erfolgen nur mit entsprechendem Auftrag; normale beauftragte Dateiarbeit kann unmittelbar erledigt werden.

## 7. Die 24 Kurzfälle

Jede Akte hat genau zehn Originalstücke: 4 EML, 1 XLSX, 3 PDF und 2 DOCX. Eine Word-Datei enthält den fachlichen Entwurf mit gezielten offenen Stellen, die andere den Mandats- und Honorarvermerk. Gesamt-PDF und Einzel-PDFs sind zusätzliche Lesefassungen.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

[Alle 24 Akten in Originalformaten herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/si-native-kanzlei-24-testakten.zip)

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Fachgebiet und Fall | Weiterzubearbeitender Entwurf | Downloads |
| --- | --- | --- |
| [Agrarrecht: Die feuchte Apfelwiese](../testakten/si-kanzlei-agrarrecht/README.md) | Aufforderung zur Instandsetzung | [Gesamt-PDF](../testakten/si-kanzlei-agrarrecht/gesamt-pdf/si-kanzlei-agrarrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-agrarrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-agrarrecht-einzelpdfs.zip) |
| [Arbeitsrecht: Kündigung im Fahrradladen](../testakten/si-kanzlei-arbeitsrecht/README.md) | Kündigungsschutzklage | [Gesamt-PDF](../testakten/si-kanzlei-arbeitsrecht/gesamt-pdf/si-kanzlei-arbeitsrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-arbeitsrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-arbeitsrecht-einzelpdfs.zip) |
| [Bank und Kapitalmarktrecht: Das verschwundene Tagesgeld](../testakten/si-kanzlei-bank-kapitalmarktrecht/README.md) | Erstattungsaufforderung | [Gesamt-PDF](../testakten/si-kanzlei-bank-kapitalmarktrecht/gesamt-pdf/si-kanzlei-bank-kapitalmarktrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-bank-kapitalmarktrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-bank-kapitalmarktrecht-einzelpdfs.zip) |
| [Bau und Architektenrecht: Das Wasser im Proberaum](../testakten/si-kanzlei-bau-architektenrecht/README.md) | Nacherfüllungsverlangen | [Gesamt-PDF](../testakten/si-kanzlei-bau-architektenrecht/gesamt-pdf/si-kanzlei-bau-architektenrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-bau-architektenrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-bau-architektenrecht-einzelpdfs.zip) |
| [Erbrecht: Die Uhr im Nachlass](../testakten/si-kanzlei-erbrecht/README.md) | Auskunftsverlangen zum Pflichtteil | [Gesamt-PDF](../testakten/si-kanzlei-erbrecht/gesamt-pdf/si-kanzlei-erbrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-erbrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-erbrecht-einzelpdfs.zip) |
| [Familienrecht: Ferien zwischen zwei Kalendern](../testakten/si-kanzlei-familienrecht/README.md) | Umgangsvereinbarung | [Gesamt-PDF](../testakten/si-kanzlei-familienrecht/gesamt-pdf/si-kanzlei-familienrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-familienrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-familienrecht-einzelpdfs.zip) |
| [Gewerblicher Rechtsschutz: Zwei Kioske namens Knusperfunk](../testakten/si-kanzlei-gewerblicher-rechtsschutz/README.md) | Abmahnungsentwurf | [Gesamt-PDF](../testakten/si-kanzlei-gewerblicher-rechtsschutz/gesamt-pdf/si-kanzlei-gewerblicher-rechtsschutz_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-gewerblicher-rechtsschutz.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-gewerblicher-rechtsschutz-einzelpdfs.zip) |
| [Handels und Gesellschaftsrecht: Schraubenglück mit Stimmgabel](../testakten/si-kanzlei-handels-gesellschaftsrecht/README.md) | Gesellschafterbeschluss zur Kapitalerhöhung | [Gesamt-PDF](../testakten/si-kanzlei-handels-gesellschaftsrecht/gesamt-pdf/si-kanzlei-handels-gesellschaftsrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-handels-gesellschaftsrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-handels-gesellschaftsrecht-einzelpdfs.zip) |
| [Insolvenz und Sanierungsrecht: Das knappe Papierlager](../testakten/si-kanzlei-insolvenz-sanierungsrecht/README.md) | Stundungsvereinbarung | [Gesamt-PDF](../testakten/si-kanzlei-insolvenz-sanierungsrecht/gesamt-pdf/si-kanzlei-insolvenz-sanierungsrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-insolvenz-sanierungsrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-insolvenz-sanierungsrecht-einzelpdfs.zip) |
| [Internationales Wirtschaftsrecht: Kaffeeröster über die Grenze](../testakten/si-kanzlei-internationales-wirtschaftsrecht/README.md) | Nachtrag zum Liefervertrag | [Gesamt-PDF](../testakten/si-kanzlei-internationales-wirtschaftsrecht/gesamt-pdf/si-kanzlei-internationales-wirtschaftsrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-internationales-wirtschaftsrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-internationales-wirtschaftsrecht-einzelpdfs.zip) |
| [Informationstechnologierecht: Der Kalender in der Wolke](../testakten/si-kanzlei-it-recht/README.md) | Nachtrag zur Auftragsverarbeitung | [Gesamt-PDF](../testakten/si-kanzlei-it-recht/gesamt-pdf/si-kanzlei-it-recht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-it-recht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-it-recht-einzelpdfs.zip) |
| [Medizinrecht: Der Befund im falschen Fach](../testakten/si-kanzlei-medizinrecht/README.md) | Anforderung der Behandlungsunterlagen | [Gesamt-PDF](../testakten/si-kanzlei-medizinrecht/gesamt-pdf/si-kanzlei-medizinrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-medizinrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-medizinrecht-einzelpdfs.zip) |
| [Miet und Wohnungseigentumsrecht: Die doppelte Treppenhausreinigung](../testakten/si-kanzlei-miet-wohnungseigentumsrecht/README.md) | Einwendungen gegen die Betriebskostenabrechnung | [Gesamt-PDF](../testakten/si-kanzlei-miet-wohnungseigentumsrecht/gesamt-pdf/si-kanzlei-miet-wohnungseigentumsrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-miet-wohnungseigentumsrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-miet-wohnungseigentumsrecht-einzelpdfs.zip) |
| [Migrationsrecht: Die neue Stelle und der alte Titel](../testakten/si-kanzlei-migrationsrecht/README.md) | Antrag zum Arbeitgeberwechsel | [Gesamt-PDF](../testakten/si-kanzlei-migrationsrecht/gesamt-pdf/si-kanzlei-migrationsrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-migrationsrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-migrationsrecht-einzelpdfs.zip) |
| [Sozialrecht: Die Musikstunden mit Stundenplan](../testakten/si-kanzlei-sozialrecht/README.md) | Stellungnahme im Statusfeststellungsverfahren | [Gesamt-PDF](../testakten/si-kanzlei-sozialrecht/gesamt-pdf/si-kanzlei-sozialrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-sozialrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-sozialrecht-einzelpdfs.zip) |
| [Sportrecht: Vier Spiele auf der Tribüne](../testakten/si-kanzlei-sportrecht/README.md) | Verbandsinterner Einspruch | [Gesamt-PDF](../testakten/si-kanzlei-sportrecht/gesamt-pdf/si-kanzlei-sportrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-sportrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-sportrecht-einzelpdfs.zip) |
| [Steuerrecht: Das Lastenrad im Steuerbescheid](../testakten/si-kanzlei-steuerrecht/README.md) | Einspruch gegen den Einkommensteuerbescheid | [Gesamt-PDF](../testakten/si-kanzlei-steuerrecht/gesamt-pdf/si-kanzlei-steuerrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-steuerrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-steuerrecht-einzelpdfs.zip) |
| [Strafrecht: Ein Paket zu viel](../testakten/si-kanzlei-strafrecht/README.md) | Verteidigungsanzeige und Akteneinsichtsgesuch | [Gesamt-PDF](../testakten/si-kanzlei-strafrecht/gesamt-pdf/si-kanzlei-strafrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-strafrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-strafrecht-einzelpdfs.zip) |
| [Transport und Speditionsrecht: Die Keramik mit nassen Ecken](../testakten/si-kanzlei-transport-speditionsrecht/README.md) | Schadensanzeige an den Frachtführer | [Gesamt-PDF](../testakten/si-kanzlei-transport-speditionsrecht/gesamt-pdf/si-kanzlei-transport-speditionsrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-transport-speditionsrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-transport-speditionsrecht-einzelpdfs.zip) |
| [Urheber und Medienrecht: Das Foto unter fremdem Namen](../testakten/si-kanzlei-urheber-medienrecht/README.md) | Unterlassungs und Auskunftsaufforderung | [Gesamt-PDF](../testakten/si-kanzlei-urheber-medienrecht/gesamt-pdf/si-kanzlei-urheber-medienrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-urheber-medienrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-urheber-medienrecht-einzelpdfs.zip) |
| [Vergaberecht: Ein Preisblatt mit leerer Zeile](../testakten/si-kanzlei-vergaberecht/README.md) | Rüge im Vergabeverfahren | [Gesamt-PDF](../testakten/si-kanzlei-vergaberecht/gesamt-pdf/si-kanzlei-vergaberecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-vergaberecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-vergaberecht-einzelpdfs.zip) |
| [Verkehrsrecht: Der Spiegel vor dem Bäcker](../testakten/si-kanzlei-verkehrsrecht/README.md) | Schadensersatzforderung | [Gesamt-PDF](../testakten/si-kanzlei-verkehrsrecht/gesamt-pdf/si-kanzlei-verkehrsrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-verkehrsrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-verkehrsrecht-einzelpdfs.zip) |
| [Versicherungsrecht: Das Wasser unter der Spüle](../testakten/si-kanzlei-versicherungsrecht/README.md) | Einwendungen gegen die Leistungsablehnung | [Gesamt-PDF](../testakten/si-kanzlei-versicherungsrecht/gesamt-pdf/si-kanzlei-versicherungsrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-versicherungsrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-versicherungsrecht-einzelpdfs.zip) |
| [Verwaltungsrecht: Der Tisch vor der Buchhandlung](../testakten/si-kanzlei-verwaltungsrecht/README.md) | Antrag auf erneute Entscheidung | [Gesamt-PDF](../testakten/si-kanzlei-verwaltungsrecht/gesamt-pdf/si-kanzlei-verwaltungsrecht_gesamt.pdf) · [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-verwaltungsrecht.zip) · [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/si-native-kanzlei-v445.33.3/testakte-si-kanzlei-verwaltungsrecht-einzelpdfs.zip) |

Die bisherigen allgemeinen Sammel-ZIPs enthalten dieses Komponentenrelease noch nicht. Bis zum nächsten Komplettrelease diese direkten Downloads nutzen.
