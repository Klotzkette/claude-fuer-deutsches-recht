# 1. Verarbeitungsverzeichnis: Prüfbericht 1.0.0

Das Plugin unterstützt die tatsächliche Aufnahme und Fortschreibung eines Unternehmensverzeichnisses. Dieser Bericht unterscheidet fachliche Redaktion, lokale Programmausführung, Dateiprüfung und Veröffentlichung. Prüfdatum: 10.10.2026. Ein erfolgreicher technischer Test ist keine Bestätigung der Rechtmäßigkeit eines realen Verarbeitungsvorgangs.

## 1.1. Fachlicher Bestand

Acht Skills enthalten jeweils 984 bis 1056 Wörter; die [Einzelprüfung](skills-pruefung.json) hält Umfang und Prüfsummen fest. Die Werkstatt hat 22 Kapitel und acht PDF-Seiten. Mini und Hauptproblem umfassen jeweils drei PDF-Seiten und bleiben unter 7500 UTF-8-Bytes. Markdown und Text sind byteidentisch. Die aktuellen Hashes stehen im [Prüfprofil](../evals/verarbeitungsverzeichnis.json).

Geprüft wurden insbesondere die unterschiedliche Verzeichnisstruktur für Verantwortliche und Auftragsverarbeiter, der eingeschränkte Artikel 30 Absatz 5, die eigenständige Benennungspflicht nach Artikel 37 DSGVO und § 38 BDSG sowie DSFA-Auslöser nach Artikel 35 und der einschlägigen Pflichtliste. Der vorgeschlagene Schwellenwert von 750 Personen wird nicht als geltendes Recht verwendet. Interne Prioritäten 1 bis 3 sind keine gesetzlichen Risikoklassen.

Die [Quellenreferenz](../../verarbeitungsverzeichnis/references/rechtsquellen.md) dokumentiert tatsächlich gelesene amtliche Normtexte, den Gesetzgebungsstand, DSK-/EDSA-Hilfen und zwei EuGH-Volltexte mit geprüften Randnummern. Die [Abrufprüfsummen](quellen-pruefsummen.json) erfassen die heruntergeladenen Quellen. Die gerichtlichen Aussagen werden jeweils durch „Trägt“ und „Trägt nicht“ begrenzt. Eine einschlägige Rechtsprechung aus 2026 wurde nicht erfunden; die aktuelle EDSA-Vorlageninitiative ist mit ihrem gelesenen Verfahrensstand eingeordnet.

## 1.2. Technische Laufprüfung

`scripts/test-verarbeitungsverzeichnis-runtime.py` führt 27 Tests aus. Geprüft werden unter anderem echte Excel-/XML-Rundläufe, native Datumswerte, Revision und Hash, Doppelschlüssel, fehlende Zeilen, offene Pflichttrigger, Entwertung früherer Prüfungen, Organisationswechsel, atomarer Fehlerabbruch, Sicherungsvorfassungen, Sperrdateien, Formelverarbeitung, XML-Entitäten, HTML-Escaping und das Word-Grundformat. Alle 27 Tests bestanden.

In der [zusätzlichen Anwendungsprobe](anwendungsprobe.json) wurde eine Kopie der Praxisakte in allen fünf Formaten exportiert, die Zuständigkeit im Excelblatt geändert und erfolgreich zurückgelesen. Der alte Rücklauf wurde anschließend ohne Änderung der führenden Datei abgewiesen. Eine negative DSFA-Entscheidung trotz offener Fragen scheiterte ebenfalls ohne Teiländerung. Der erneute XML-Export entsprach dem aktuellen Register vollständig. Der KI-Pilot blieb als geplant erfasst. Die genannte Person ist fiktiv; der Lauf stellt keine tatsächliche Freigabe dar.

Der Helfer arbeitet lokal. Er führt weder Benutzerkonten noch Cloud-Synchronisation, rechtliche Quellenüberwachung, automatische Meldungen oder Kalendererinnerungen aus. Namen und Hashes sind keine Authentisierung oder manipulationssichere Archivierung. Der technische Rahmen beträgt 5000 Tätigkeiten und 25 MiB je Eingabedatei; er ist keine gesetzliche Größenfreistellung. Der Verantwortliche muss Zugriff, Aufbewahrung und Schutz der Dateien eigenständig organisieren.

## 1.3. Akten, Vorlagen und Lesefassungen

Die drei Akten enthalten jeweils 14 Originaldateien: drei DOCX, vier PDF, vier EML, eine XLSX und zwei JSON-Stände. Zusammen sind dies 42 Originaldateien. Sechs E-Mails enthalten zusätzlich bytegenau geprüfte PDF-Anhänge. Eine neutrale Startvorlage steht in JSON, XLSX, DOCX, XML und HTML bereit. Der [Aktenprüfnachweis](akten-pruefung.json) enthält Originalhashes, MIME-Prüfung, vier erfolgreiche Excel-Rundläufe und die visuelle Prüfung von zehn Word-Seiten, zwölf Original-PDF-Seiten und 28 Tabellenblättern.

Die Gesamtakten haben 25 Seiten (Handwerk), 23 Seiten (Cloudservice) und 25 Seiten (Praxis). Sie entstehen aus genau den zugehörigen 14 Einzel-PDFs. Der Pakettest vergleicht jede Seite textlich und die ursprünglichen Arbeitsdateien bytegenau. Die Warnhinweise stehen auf den Downloadseiten und an der ZIP-Wurzel; die PDF-Akten enthalten keine Warnseiten.

Word-Dateien werden nativ durch LibreOffice gerendert. Für die breiten Arbeitsmappen gibt es feldweise PDF-Druckansichten mit Zellkoordinaten und vollständigen Werten, einschließlich der technischen Metadaten. Das vermeidet winzige Drucktabellen. Die Arbeitsmappen selbst bleiben als Tabellen bearbeitbar. Alle Zellwerte, Mindestschriftgröße und Seitenränder dieser Druckansichten werden automatisch geprüft. Die 14 Promptseiten und die sieben Seiten der Handwerks-Tabellenansicht wurden zusätzlich visuell kontrolliert; es wurden keine Überlagerungen oder abgeschnittenen Textblöcke gefunden. Die lokalen PDF-Fassungen verwenden Times New Roman 11 pt; der Linux-Build benennt gegebenenfalls Liberation Serif als Ersatz.

## 1.4. Reproduzierbare Prüfungen

Die folgenden Aufrufe wurden mit dem finalen Quellstand erfolgreich ausgeführt. Die Komponentenprüfung umfasst zehn Tests einschließlich der fertigen 22 Release-Dateien; kein Pakettest wird im vollständigen Aufruf übersprungen.

```bash
python3 scripts/test-verarbeitungsverzeichnis-runtime.py
python3 scripts/build-verarbeitungsverzeichnis-release.py --dist /tmp/vvt-release-final
python3 scripts/test-verarbeitungsverzeichnis.py --dist /tmp/vvt-release-final
claude plugin validate verarbeitungsverzeichnis --strict
node scripts/validate-plugin-structure.mjs
node scripts/validate-marketplace-import.mjs
python3 scripts/validate-yaml-frontmatter.py
python3 scripts/audit-skill-activation.py
python3 scripts/validate-markdown-structure.py
python3 scripts/validate-root-readme-overview.py
python3 scripts/validate-testakten-readme-downloads.py
python3 scripts/test-scoped-release-routing.py
python3 scripts/quality-lab.py audit --require-editorial --require-workflow
```

Die Markdownstruktur, Auswahlbeschreibungen, lokalen Referenzlinks, drei Manifestfassungen, vier Befehle, Promptpaare, Quellhashes und Archivzusammensetzung wurden geprüft. Die fünf redaktionellen Prüfszenarien enthalten 21 fachspezifische Kriterien. Es handelt sich um ein Prüfprofil, nicht um den behaupteten Erfolg eines nicht ausgeführten Modelllaufs in Claude, Cowork oder ChatGPT.

## 1.5. Veröffentlichungsumfang

Das Komponentenrelease heißt `verarbeitungsverzeichnis-v1.0.0`. Es enthält Plugin-ZIP, Portable-ZIP, Vorlagen-ZIP, neun Promptdateien, neun Aktendownloads und die Prüfsummenliste. Das Gesamtrelease `v445.35.3` bleibt unverändert. Die Downloadzuordnung schützt zusätzlich sechs bestehende ZIP-Ziele dreier WEG-Akten vor einer durch die neue alphabetische Aufteilung verursachten Fehlverlinkung. Alle 1030 zuvor vorhandenen Akten-ZIP-Ziele bleiben gleich.

Eine Veröffentlichung erfolgt erst nach den Dateiprüfungen. Der Veröffentlichungshelfer lädt sämtliche Release-Dateien erneut herunter und vergleicht sie bytegenau, bevor er den Entwurf öffentlich schaltet. Bestehende Tags und Archive werden nicht überschrieben. Eine spätere Änderung der Rechtslage oder Unternehmensprozesse muss erneut geprüft werden; das Paket bescheinigt keine dauerhafte Datenschutzkonformität.
