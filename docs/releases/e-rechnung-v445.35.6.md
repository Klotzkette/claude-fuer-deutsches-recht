# E-Rechnung-Werkstatt

Die E-Rechnung-Werkstatt erstellt ZUGFeRD-Rechnungen und XRechnungen aus vorhandenen Rechnungsentwürfen, Verträgen, Leistungsnachweisen, Tabellen, E-Mails und Scans. Sie klärt fehlende Angaben und widersprüchliche Quellen, prüft Steuerbehandlung und Beträge und führt bis zur tatsächlich erzeugten Rechnungsdatei.

Das Paket enthält sieben Fachskills, einen lokalen Generator mit dokumentierter Einrichtung sowie eigenständig nutzbare Werkstatt-, Mini-, Schwerpunkt- und Master-Prompts. Die Formaterstellung verwendet getrennte Prüfwege für ZUGFeRD und das aktuelle KoSIT-XRechnung-Regelwerk. Versionsstände, tatsächliche Prüfergebnisse und der unterstützte Funktionsumfang werden ausdrücklich ausgewiesen.

- [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/e-rechnung-v445.35.6/e-rechnung-werkstatt.zip)
- [Werkstatt-Prompt](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/e-rechnung-v445.35.6/e-rechnung-werkstatt-werkstatt.md)
- [Mini-Prompt](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/e-rechnung-v445.35.6/e-rechnung-werkstatt-schnellstart.md)
- [Hauptproblem-Prompt](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/e-rechnung-v445.35.6/e-rechnung-werkstatt-hauptproblem.md)
- [Master-Prompt](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/e-rechnung-v445.35.6/e-rechnung-werkstatt-master-prompt.md)
- [Prüfsummen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/e-rechnung-v445.35.6/checksums-sha256.txt)

Eine erfolgreiche Dateiprüfung ersetzt weder die Prüfung der tatsächlichen Rechnungstatsachen noch den Eingangsnachweis beim Empfänger. Die Veröffentlichung enthält keinen Nachweis einer Live-Übermittlung an ein Rechnungsportal.

Das Beispielpaket dokumentiert die tatsächlich ausgeführte Erzeugung einer Rechnung mit Positionen zu 7 und 19 Prozent. KoSIT akzeptiert die XRechnung; die Hybriddatei enthält das bytegleiche geprüfte XML und besteht die PDF/A-3u-Prüfung. Das einseitige Rechnungsformular wurde gerendert und visuell geprüft. Zehn Regressionen einschließlich tatsächlich verworfener fehlerhafter XML- und PDF-Dateien sind bestanden.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

[Beispielpaket als ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/e-rechnung-v445.35.6/E-Rechnung_Beispielpaket.zip)
