# 1. Integration der Bauvergabe-Reihe

Prüfstand: 06.10.2026. Version: 445.32.0.

## 1.1. Lieferumfang

Fünf verschachtelte, eigenständig installierbare Plugins mit jeweils zehn Fachskills und einem Hauptskill; zusammen 55 Skills. Jedes Plugin enthält lokal verfügbare Referenzen, einen eigenständigen Werkstatt-Prompt von rund 49.000 Zeichen und einen Mini-Prompt innerhalb des Budgets von 7.500 UTF-8-Bytes. Die TXT-Fassungen sind identische Kopien der redaktionellen Markdown-Quelle. Der gemeinsame Ordner ist eine Übersicht und kein sechstes Plugin. Große Prompts und zentrale Akten werden nicht als Skillabhängigkeit installiert.

Die zwei zusammenhängenden Fälle enthalten 77 native Dateien: 41 Word-Dokumente, zehn zusätzliche Brief-PDFs, 16 E-Mails, sechs CSV-Listen und vier Excel-Arbeitsmappen. Klinik und Wohnhaus behalten in beiden ZIP-Fassungen ihre fünf Arbeitsstationen. Die Gesamt-PDFs haben 49 beziehungsweise 50 Seiten, je ein Seitenregister, fünf Stufenlesezeichen und 38 beziehungsweise 39 Dokumentlesezeichen.

## 1.2. Fachliche und visuelle Prüfung

Die drei Fachberichte in diesem Ordner dokumentieren die tatsächlich geöffneten amtlichen Quellen, die geprüften Rechtsänderungen 2026 und die Grenzen der jeweiligen Entscheidungsanker. Ein zusätzliches unabhängiges Gegenlesen prüfte die Auftraggeber- und Nachtragsplugins sowie die Fallchronologie. Korrigiert wurden insbesondere Angebotserstellungsdaten, die Preisaufklärung vor der Vorabinformation, die Datierung des Nachtrags und die eigenständige Verpflichtungserklärung des Eignungsleihers. Ein kommunales Unternehmen wird nicht allein wegen seiner Beteiligungsverhältnisse als öffentlicher Auftraggeber behandelt.

Alle 53 Seiten der 41 Word-Dokumente wurden visuell geprüft. Sichtbare Markdownzeichen im LV wurden entfernt und die geänderten Seiten erneut geprüft. Alle vier Tabellenblätter und sechs native Druckseiten wurden angesehen. Vier Originalberechnungen und zwölf Änderungen mit normalen, leeren und Null-Eingaben wurden mit dem Tabellenwerkzeug und LibreOffice geprüft. Die Angebotsbeträge betragen 7.823.200,00 beziehungsweise 1.775.620,00 EUR netto; die streitigen Nachtragsforderungen 244.532,00 beziehungsweise 64.622,44 EUR netto. Zuschläge sind Forderungen und keine unterstellte Anerkennung.

Alle 99 Gesamt-PDF-Seiten wurden visuell geprüft; Seitenbereiche, Dokumentinhalte und Lesezeichen wurden zusätzlich maschinell abgeglichen. CSV-Tabellen verwenden teilweise dichte Wortumbrüche; die Excel-Druckansicht verwendet teils US-Zahlenseparatoren. Die Inhalte bleiben vollständig lesbar und die Beträge eindeutig. Diese Darstellungsgrenzen werden nicht als Inhaltsfehler oder als fehlende Prüfung verschwiegen.

## 1.3. Automatische Prüfungen

Der Bauvergabe-Integrationstest kontrolliert unter anderem die fünf tatsächlichen Marketplace-Quellen, exakt elf installierbare Skills je Plugin, innerhalb des Plugins auflösbare Ressourcen, Promptbudgets und Profilhashes. Er gleicht die native Akte unabhängig gegen Exportfilter und ZIP-Dateien ab. Ein absichtlich ausgefiltertes Excel-Dokument muss sowohl im Test als auch im Gesamt-PDF-Builder scheitern. E-Mail-Anhänge müssen bytegleich mit den bezeichneten Aktenstücken sein. Fristen, Aufklärung, Angebotsbeträge und Nachtragssummen werden über die Dateiformate hinweg kontrolliert.

Die gesetzlichen Prüfszenarien sind redaktionelle Evaluationen. Sie werden nicht als beobachtete Modellläufe oder als Garantie der Richtigkeit späterer Ausgaben bezeichnet. Struktur-, Laufzeit-, YAML-, Marketplace-, Prompt-, Link-, Downloadhinweis- und Rechtsstandprüfungen erfolgen zusätzlich mit den allgemeinen Repositorywerkzeugen.

## 1.4. Reproduktion und Veröffentlichung

Die nativen Textakten entstehen aus `bauvergabe_falldaten.py` und `bauvergabe_aktentexte.py` über `build-bauvergabe-akten.py`. Die Tabellen-Spec wird mit `bauvergabe-tabellen-spec.py` aus denselben Stammdaten erzeugt; `build-bauvergabe-tabellen.mjs` erstellt daraus die Arbeitsmappen. Der kanonische Gesamt-PDF-Builder ruft für beide Akten `build-bauvergabe-pakete.py` auf; die ZIPs werden von den allgemeinen Testakten-Buildern erzeugt.

Die Veröffentlichung verwendet die geprüften PDF-Dateien und unveränderten Vorversionakten. Alte PDF- und Originalarchive werden vor der Wiederverwendung vollständig gegen ihre Quellen und veröffentlichten Prüfsummen kontrolliert. Alle aktuellen Plugin- und Skillsarchive werden aus dem aktuellen Quellstand erstellt. Das vermeidet eine ungeprüfte erneute Konvertierung fremder Akten.

Bei der abschließenden Repositoryprüfung wurden zwei bereits vorhandene Darstellungsmehrdeutigkeiten präzisiert: Das Urteil II ZR 91/21 und sein gesonderter Berichtigungsbeschluss stehen in getrennten Absätzen; der produktive Playbook-Fundstatus wird deutsch bezeichnet. Die rechtlichen Aussagen, die Prüfengine und die Sperrregeln wurden dabei nicht verändert.
