# 1. Verarbeitungsverzeichnis

Dieses Plugin hilft kleinen und mittleren Unternehmen, ihr Verzeichnis von Verarbeitungstätigkeiten anzulegen, zu prüfen und im Alltag weiterzuführen. Acht abgestimmte Skills verbinden Aufnahme, Rechtsgrundlagen, Löschung, Dienstleister, technische Maßnahmen, Risikoprüfung und Datenschutz-Folgenabschätzung mit einer tatsächlich bearbeitbaren Dateiablage.

Sie können mit vorhandenen Verträgen, Prozessbeschreibungen und Tabellen beginnen oder einen neuen Bestand aufbauen. Eine neue E-Mail, ein Cloud-Dienst, eine geänderte Löschfrist oder ein weiterer Datenempfänger wird dem bestehenden Vorgang zugeordnet. Das Ergebnis sind ein aktualisiertes Register, nachvollziehbare Änderungen und konkrete offene Aufgaben.

## 1.1. Einfach anfangen

Installieren Sie das Plugin in einer unterstützten Umgebung oder verwenden Sie den Schnellstart als Projektanweisung. Geben Sie beispielsweise folgenden Auftrag:

> Wir sind ein Handwerksbetrieb mit 24 Beschäftigten. Hier sind unsere Systemliste, die Lohnabrechnungsvereinbarung und die Angaben zum geplanten Fahrzeugtracking. Legen Sie unser Verarbeitungsverzeichnis an. Erstellen Sie eine verständliche Excel-Datei und sagen Sie konkret, welche Angaben fehlen und für welche Tätigkeit eine DSFA geprüft werden muss.

Für die Fortsetzung genügt etwa:

> Zum Bewerbungsportal liegt jetzt die Anbieterantwort vor. Arbeiten Sie die belegten Änderungen in den aktuellen Registerstand ein und prüfen Sie, ob die frühere Risikobewertung weiter gilt. Geben Sie mir danach die neue Excel- und Word-Fassung.

Das System liest zunächst die vorhandenen Unterlagen und fragt nur nach entscheidenden Lücken. Die acht Skills umfassen einen steuernden Hauptskill und sieben Fachschritte. Die detaillierten Abläufe stehen in [Arbeitsweise](references/arbeitsweise.md), [Datenmodell](references/datenmodell.md) und [Dateipflege](references/dateipflege.md).

## 1.2. Was die laufende Pflege kann

Der lokale Helfer führt eine JSON-Datei als eindeutigen Arbeitsstand. Excel kann daraus exportiert, bearbeitet und kontrolliert zurückgelesen werden. Tätigkeiten haben feste Kennungen. Revision und Prüfsumme verhindern, dass ein alter Export einen neueren Stand unbemerkt überschreibt. Vorfassungen werden gesichert; Änderungen benötigen einen Namen und einen Anlass. Fehlende Excelzeilen gelten nicht als Löschauftrag.

Fachliche Änderungen machen frühere Prüfungen erkennbar veraltet. Die Dokumentation bleibt erhalten und wird erneut beurteilt. Die namentliche Eingabe ist ein organisatorischer Vermerk, kein Identitätsnachweis, keine elektronische Signatur und keine manipulationssichere Archivierung.

| Format | Verwendung | Grenze |
| --- | --- | --- |
| Excel | Bearbeitbare Tätigkeiten, Artikel-30-Angaben und Screening mit Anleitung | Rückimport prüft Herkunft, Revision und Feldstruktur |
| Word | Lesbare Verzeichnisblätter und interne Durchsicht | Änderungen werden ausdrücklich in den führenden Stand übertragen |
| JSON | Führender strukturierter Datenbestand und nachvollziehbare Fassungen | Zugriff, Sicherung und Berechtigungen bleiben organisatorisch zu regeln |
| XML | Dokumentierter Austausch mit eingebettetem strukturiertem Register | Kein behauptetes amtliches Einreichungsschema oder Fremdproduktadapter |
| HTML | Lokale Übersicht mit Suche und JSON-Download | Momentaufnahme des letzten Exports, keine automatische Cloud-Synchronisierung |

„Laufend pflegen“ bedeutet hier Arbeit am geöffneten Register nach einem konkreten Auftrag. Das Paket enthält keinen automatisch laufenden Überwachungsdienst, keinen Mehrbenutzer-Server und keine Kalendererinnerung. Für mehrere gleichzeitig schreibende Bearbeiter, zahlreiche Gesellschaften oder komplexe Berechtigungen ist eine dafür ausgelegte Plattform nötig. Die Größe allein entscheidet nicht über die rechtliche Komplexität.

## 1.3. Rechtliche Prüfung

Eigene Verantwortung und Auftragsverarbeitung werden getrennt nach Artikel 30 Absatz 1 und 2 DSGVO geführt. Eine niedrige Beschäftigtenzahl ist keine pauschale Ausnahme vom Verzeichnis. Die Erforderlichkeit eines Datenschutzbeauftragten nach Artikel 37 DSGVO und § 38 BDSG wird gesondert geprüft.

Eine interne Priorität oder „Risikoklasse 1“ ist keine gesetzliche DSGVO-Kategorie. Das Plugin prüft den DSFA-Bedarf anhand von Artikel 35, der einschlägigen behördlichen Liste und den konkreten Umständen. Ein niedriger Score kann einen gesetzlichen Pflichtgrund nicht überstimmen. Offene Tatsachen führen zu einer offenen Prüfung. Bei erforderlicher DSFA unterstützt der Workflow auch den gesonderten Bericht, die Maßnahmen und erforderlichenfalls die Prüfung einer vorherigen Konsultation nach Artikel 36.

Ein vollständiger Datensatz bedeutet nicht automatisch rechtmäßige Verarbeitung. Rechtsgrundlagen, Informationen, Auftragsverarbeitung, internationale Zugriffe, Löschung und technische Umsetzung müssen inhaltlich stimmen. Die [Rechtsquellen](references/rechtsquellen.md) dokumentieren gelesene amtliche Texte, Leitlinien, Entscheidungen und ihre Grenzen; Gesetzgebungsvorschläge werden nicht als geltendes Recht behandelt.

## 1.4. Downloads und Betrieb

Komponentenfassung **1.0.0**, Quellen- und Bearbeitungsstand 10. Oktober 2026. Die [Releasebeschreibung](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/verarbeitungsverzeichnis-v1.0.0) enthält die Dateien und Prüfsummen. Das bestehende Gesamtrelease v445.35.3 wird nicht überschrieben und enthält dieses Plugin noch nicht.

| Angebot | Inhalt | Download |
| --- | --- | --- |
| Plugin | Acht Skills, Referenzen, vier Startbefehle und lokaler Dateihilfe-Code | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/verarbeitungsverzeichnis-v1.0.0/verarbeitungsverzeichnis.zip) · [Portable ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/verarbeitungsverzeichnis-v1.0.0/verarbeitungsverzeichnis-portable.zip) |
| Startvorlagen | Neutrale Beispieldateien für die Formate und Pflege | [Vorlagen-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/verarbeitungsverzeichnis-v1.0.0/verarbeitungsverzeichnis-vorlagen.zip) |
| Werkstatt | 22 Kapitel mit vollständiger Aufnahme, Bewertung und Fortsetzung | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/verarbeitungsverzeichnis-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/verarbeitungsverzeichnis-werkstatt.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/verarbeitungsverzeichnis-v1.0.0/verarbeitungsverzeichnis-werkstatt.pdf) |
| Mini | Eigenständiger kompakter Ablauf | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/verarbeitungsverzeichnis-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/verarbeitungsverzeichnis-schnellstart.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/verarbeitungsverzeichnis-v1.0.0/verarbeitungsverzeichnis-schnellstart.pdf) |
| Hauptproblem | Ist der Bestand aktuell und was ist jetzt nötig? | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/verarbeitungsverzeichnis-hauptproblem.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/verarbeitungsverzeichnis-hauptproblem.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/verarbeitungsverzeichnis-v1.0.0/verarbeitungsverzeichnis-hauptproblem.pdf) |

Claude-Code-/Cowork-Befehle: `/vvt`, `/vvt-aenderung`, `/vvt-risiko` und `/vvt-export`. In Codex oder ChatGPT können diese als normale Arbeitsaufträge verwendet werden, wenn die Oberfläche keine Slash-Befehle anbietet. Für ChatGPT eignet sich der Mini-Prompt als Projektanweisung; Werkstatt und Referenzen kommen als Projektdateien hinzu. Dateizugriff und Ausführung des lokalen Python-Helfers hängen von der Umgebung ab. Ein Plugin-ZIP allein startet keinen Dienst und garantiert keinen direkten Import in jede ChatGPT-Oberfläche.

Der Helfer benötigt Python 3.10 oder neuer sowie `openpyxl` und `python-docx` für die Officeformate. Die genaue Bedienung steht in der Dateipflege-Referenz. Ein neues Unternehmensregister erhält über `init` eine eigene Registerkennung; die Startvorlage wird nicht ungeprüft als bereits geführter Unternehmensbestand übernommen. Sichere Ordner, Zugriffsrechte und Backups sind vor produktiver Nutzung festzulegen.

## 1.5. Drei Testakten

Die Fälle enthalten fiktive Unterlagen aus dem Betriebsalltag. Sie führen von einer ersten Aufnahme zu einer konkreten Änderungsmeldung mit offenen Nachweisen. Die Originalformate bleiben bearbeitbar; parallel stehen Einzel-PDFs und Gesamt-PDF bereit.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Fall | Aufgabe | Unterlagen und Downloads |
| --- | --- | --- |
| Finkenbeil in Erfurt | Regelmäßige Personal- und Kundenverarbeitung, geplantes Fahrzeugtracking und Bewerbungsportal | [Handwerksakte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/vvt-handwerk-finkenbeil-erfurt/README.md) |
| Wolkengarn in Berlin | Eigene Verantwortung und Auftragsverarbeitung, Unterauftragnehmer und unklarer Auslandszugriff | [Cloudservice-Akte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/vvt-cloudservice-wolkengarn-berlin/README.md) |
| Rosenquell in Bamberg | Gesundheitsdaten, geplanter Video-/KI-Pilot und neue DSFA-Prüfung | [Praxisakte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/testakten/vvt-praxis-rosenquell-bamberg/README.md) |

## 1.6. Prüfumfang

Technische Tests prüfen insbesondere Importkonflikte, Kennungen, erhaltene Vorfassungen, unvollständige Angaben, getrennte Rollen, DSFA-Pflichttrigger und die Exportformate. Redaktionelle Fachprüfung und automatisierte Bestandstests sind von einem beobachteten Modelllauf zu unterscheiden. Der [Prüfbericht](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/quality/verarbeitungsverzeichnis/README.md) dokumentiert die tatsächlich ausgeführten Prüfungen und verbleibende Grenzen. Das Angebot ist keine Zertifizierung und kein Ersatz für erforderliche betriebliche Entscheidungen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 8 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 8 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`aenderungen-nachhalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/aenderungen-nachhalten/SKILL.md) | Pflegt Änderungen an Tätigkeiten, Quellen und Prüfständen mit Revisionen und Konfliktabgleich. Erkennt erneuten DSFA-Prüfbedarf, veraltete Angaben und offene Maßnahmen, ohne bestehende Daten stillschweigend zu überschreiben. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/aenderungen-nachhalten/SKILL.md) |
| [`dienstleister-transfers-tom-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/dienstleister-transfers-tom-pruefen/SKILL.md) | Prüft die tatsächlichen Datenschutzrollen von Dienstleistern, Unterauftragnehmer und Drittlandszugriffe sowie die nachgewiesenen Schutzmaßnahmen. Überführt konkrete Befunde und Nachforderungen in das Verarbeitungsverzeichnis. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/dienstleister-transfers-tom-pruefen/SKILL.md) |
| [`rechtsgrundlagen-loeschung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/rechtsgrundlagen-loeschung-pruefen/SKILL.md) | Prüft je Verarbeitung den konkreten Zweck, die tragende Rechtsgrundlage und die Löschlogik. Unterscheidet Erlaubnis, Informationspflicht, Aufbewahrung und technische Umsetzung und dokumentiert offene Nachweise. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/rechtsgrundlagen-loeschung-pruefen/SKILL.md) |
| [`risiken-dsfa-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/risiken-dsfa-pruefen/SKILL.md) | Bewertet konkrete Risiken einer Verarbeitung für betroffene Menschen und prüft die DSFA-Pflicht anhand der DSGVO und einschlägiger Aufsichtslisten. Hält interne Priorität, begründete Entscheidung und erneute Prüfung getrennt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/risiken-dsfa-pruefen/SKILL.md) |
| [`verarbeitungen-erheben`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/verarbeitungen-erheben/SKILL.md) | Ermittelt konkrete Verarbeitungstätigkeiten aus Betriebsabläufen, Verträgen und Systemlisten. Trennt Zwecke, Datenschutzrollen und Beleglücken und übergibt belastbare Angaben für das Verarbeitungsverzeichnis. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/verarbeitungen-erheben/SKILL.md) |
| [`verarbeitungsverzeichnis-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/verarbeitungsverzeichnis-steuern/SKILL.md) | Steuert das Verarbeitungsverzeichnis eines Unternehmens von der Erhebung über Rollenprüfung und DSFA-Vorprüfung bis zur laufenden Änderung und Ausgabe. Verbindet belastbare Nachweise mit einer versionierten Datei und konkreten nächsten A... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/verarbeitungsverzeichnis-steuern/SKILL.md) |
| [`verzeichnis-ausgeben`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/verzeichnis-ausgeben/SKILL.md) | Erzeugt konsistente Ausgaben des Verarbeitungsverzeichnisses mit Rollenansichten, Quellenstand und offenen Aufgaben. Prüft lesbare Dateien, Excel-Rückimport und Formatgrenzen und bereitet eine konkrete interne oder behördliche Vorlage vor. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/verzeichnis-ausgeben/SKILL.md) |
| [`verzeichnis-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/verzeichnis-erstellen/SKILL.md) | Erstellt aus geprüften Angaben ein versioniertes Verzeichnis mit getrennten Verantwortlichen- und Auftragsverarbeiteransichten. Ordnet Mindestangaben, Zusatzprüfungen, Quellen und offene Aufgaben eindeutigen Tätigkeiten zu. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=verarbeitungsverzeichnis/skills/verzeichnis-erstellen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
