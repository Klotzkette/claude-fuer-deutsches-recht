# 1. KI-Verordnungs-Fachrunde vom 9. Oktober 2026

Komponentenfassung **445.35.0**, Release `ki-verordnung-v445.35.0`. Anlass sind zwei vom Nutzer bereitgestellte Bildschirmabbildungen über fehlerhafte AI-Act-Pauschalen. Die Meinungsäußerungen werden nicht als Rechtsquelle übernommen. Für die materiellen Korrekturen wurden amtliche Volltexte und die einschlägigen Kommissionsleitlinien gelesen und archiviert.

## 1.1. Umfang und tatsächliche Prüfweite

Die Ausgangssuche erfasste **1.283 Textdateien mit 5.862 Treffern**. Der [Bestandsnachweis](repo-inventar.json) benennt jede Ausgangsdatei, Trefferzahl, Bearbeitungsart und Endhash. Ein Suchtreffer belegt noch keine vollständige rechtliche Prüfung jeder Aussage der Datei. Die vertiefte Gegenprüfung betraf insbesondere Einstufung, Rollen, Anwendungsdaten, Verbote, Transparenz, Registrierung, Vorfallmeldung, Konformitätsverfahren, Risikomanagement und Folgenabschätzung.

**48 betroffene Plugins** stehen im [Release-Scope](../../scripts/data/ki-verordnung-release-scope.json). 86 Skills des großen Prüfers und Transparenzprüfers wurden individuell korrigiert; weitere 326 konkrete Änderungseinträge in Randkomponenten stehen im [Peripherieprotokoll](peripherie-korrekturen.json). Die Zahl bezeichnet Änderungseinträge, nicht 326 eigenständige Rechtsfehler. Elf einschlägige aktive Vorlagen einschließlich ihrer ODT- und Markdown-ZIP-Ausgaben wurden ebenfalls aktualisiert.

Historische Veröffentlichungen, frühere Abrufprotokolle und streitige Aussagen fiktiver Aktenbeteiligter werden nicht stillschweigend in heutige Rechtsauskünfte umgeschrieben. Bestehende Gerichts-, Arbeitsrechts-, Datenschutz- und nationale Anker außerhalb der gelesenen Quellen sind nicht als in dieser Runde vollständig neu verifiziert auszugeben. Es gibt keine pauschale juristische Neuzertifizierung des Gesamtbestands.

## 1.2. Rechtsquellen und zentrale Korrekturen

Der [Rechtsstandsvermerk](../../references/ki-verordnung-rechtsstand-2026-10-09.md), das [Quellenverzeichnis](quellen/quellen.json) und der [konkrete Fachbefund](quellen/befund-bestand.md) dokumentieren Datum, amtliche URL, Originalarchiv, Hash und tatsächliche Lesereichweite. Gelesen wurden die Konsolidierung vom 27. Juli 2026, Verordnung (EU) 2026/1744 und deren deutsche Berichtigung vom 29. September 2026 sowie die einschlägigen GPAI- und Transparenzleitlinien. Eine Konsolidierung wird nicht mit einer eigenen authentischen Verkündung gleichgesetzt.

Die Änderungen betreffen insbesondere:

- Artikel 6 Absatz 1 mit Sicherheitsbauteil, Produktbewertung und Berichtigung; davon getrennt Absatz 2 und sämtliche Anhang-III-Bereiche. Absatz 3 wird nur im richtigen Pfad angewandt; Profiling, Dokumentation und Registrierung werden gesondert geprüft.
- Artikel 9 als Systemrisikoprozess, Artikel 17 als Anbieter-Qualitätsmanagement und Artikel 27 als beschränkter Betreiber-Folgenabschätzungstatbestand. Öffentliche Finanzierung oder das Etikett FRIA ersetzen keine Voraussetzungen.
- Artikel 4 mit Kompetenzförderung und Artikel 4a mit eng begrenzter Verarbeitung sensibler Bias-Daten. Die frühere Fundstelle Artikel 10 Absatz 5 wird berichtigt.
- Aktuelle Anwendungs- und Übergangsregeln der Artikel 111 und 113; die verschobenen Abschnitte dürfen nicht mit allen sonstigen Pflichten gleichgesetzt werden. Bei Verweisungsfragen bleiben begründete Auslegungsunsicherheiten sichtbar.
- Artikel 43 mit unterschiedlichen Konformitätsrouten, tatsächliche Amtsblattfundstelle und Deckungsumfang nach Artikel 40, Erklärung, Registrierung und Änderungen. Eine ISO-Bezeichnung oder ein beliebiges Zertifikat ersetzt keine Konformitätsprüfung.
- Artikel 26 gegenüber früher unzutreffend genannten Betreiberfundstellen; Artikel 73 mit unverzüglicher Handlung und verschiedenen äußersten Fristen. Zwei, zehn und fünfzehn Tage werden nicht vertauscht oder als Wartefristen verstanden.
- Artikel 50 mit getrennten Anbieter- und Betreiberpflichten, technischer Markierung und Offenlegung. Satire und menschliche Bearbeitung sind keine allgemeine Ausnahme für sämtliche synthetischen Inhalte.
- Die Drittel-FLOP-Orientierung der GPAI-Leitlinien ist keine Ausnahme für ein fertiges KI-System. Eine Risikopyramide, Lieferantenpolicies oder das Wort Agent ersetzen keine Subsumtion.

## 1.3. Vier Spezialplugins

| Komponente | Ergebnis |
| --- | --- |
| [Verbotene Praktiken](../../ki-verordnung-verbotene-praktiken/README.md) | Neu: zehn Fachskills und Hauptproblem-Skill; drei Fälle zu Beeinflussung, Emotionserkennung und Social Scoring. |
| [Hochrisikoprüfer](../../ki-verordnung-hochrisiko-pruefer/README.md) | Bestehendes Plugin auf elf Skills erweitert; ein eigener Einstufungsskill, Produktpfad und vollständige Absatz-3-Prüfung; zwei neue Fälle neben der erhaltenen Recruitingakte. |
| [Register und Meldungen](../../ki-verordnung-register-meldungen/README.md) | Neu: elf Skills mit Datenbank-, Korrektur-, Betreiber-, Modell-, Realtest- und Vorfallwegen; zwei Fälle. |
| [Konformitätsprüfung](../../ki-verordnung-konformitaet/README.md) | Neu: elf Skills für konkrete Bewertungsroute, Nachweisführung, Qualitätsmanagement, Erklärung und Änderungen; zwei Fälle. |

Je Spezialplugin gibt es Werkstatt, Mini und Hauptproblem als byteidentische MD/TXT-Paare. Mini und Hauptproblem bleiben jeweils unter 7.500 UTF-8-Bytes. Die Werkstätten enthalten eigenständige Abläufe, konkrete Unterlagenanforderungen, Rückfragen, Fortsetzung und fertige Ergebnisprodukte. Portalversand ist ohne tatsächliche Werkzeugverbindung, Berechtigung und konkrete menschliche Freigabe nicht als erfolgt darzustellen.

## 1.4. Akten, Formeln und Lesefassungen

Die neun neuen Akten enthalten **108 Originaldateien**: 27 DOCX, 27 PDF, 36 EML, neun XLSX und neun Chats. **19 E-Mail-Anhänge** stimmen bytegenau mit den separat vorliegenden Originalen überein. Daten und Personen sind fiktiv. Zukunftsdaten sind Planungen oder ausdrücklich eingefrorene Übungen; sie werden nicht als am Bearbeitungsstichtag tatsächlich eingetretene Ereignisse ausgegeben.

Die [Artikel-5-Dateiprüfung](artikel5/README.md) deckt sieben Akten und die [Hochrisikoprüfung](hochrisiko/README.md) zwei weitere ab. Die nativen Excel-Rechenproben einschließlich geänderter Eingaben sind dort dokumentiert. Word/PDF-Inhaltsgleichheit und Seitenansichten wurden bei der Erstellung geprüft.

Die neun Gesamtakten haben zusammen **173 Seiten**. Acht zusätzliche Handbuch-/Werkstatt-PDFs haben zusammen **164 Seiten**. [Umfang und Textdeckung](umfang.json) binden die Skill- und Werkstatt-Lesefassungen an ihre Quellen. Sie wurden mit der installierten Times New Roman gesetzt. [PDF-Prüfung](pdf-pruefung.json): sämtliche Seiten auf Text außerhalb der Seite kontrolliert; je PDF die dokumentierten zwei Seiten als gerenderte Bilder visuell geprüft. Die nativen Einzelstücke wurden zusätzlich durch die jeweiligen Aktenbearbeiter visuell kontrolliert. Eine lückenlose manuelle Sichtprüfung aller zusammengesetzten Seiten wird nicht behauptet.

Der zentrale Exportfilter schloss zunächst zwei offen angelegte Word-Entwürfe wegen des Dateinamens „Pruefvermerk“ aus. Die Dateien wurden bei identischem Inhalt eindeutig in „Stellungnahme_Arbeitsentwurf“ umbenannt, Bezüge und Hashlisten angepasst und die Gesamtakten neu gebaut. Die zentralen Filter wurden nicht aufgeweicht.

## 1.5. Technische Prüfungen und bekannte Fremdbefunde

Reproduzierbare Kernprüfungen:

```text
python3 scripts/test-ki-verordnung-fachrunde.py
python3 scripts/test-ki-verordnung-fachrunde.py --dist <Ausgabeordner>
python3 scripts/test-ki-verordnung-artikel5-testakten.py
python3 scripts/test-ki-verordnung-hochrisiko-pruefer.py
python3 quality/ki-verordnung-2026-10-09/quellen/pruefe-bestand.py
python3 scripts/validate-yaml-frontmatter.py
node scripts/validate-plugin-structure.mjs
python3 scripts/test-marketplace-import.py
python3 scripts/validate-markdown-structure.py
python3 scripts/test-release-routing.py
python3 scripts/test-scoped-release-routing.py
python3 scripts/test-office-resilience.py
```

Der Komponentenprüfer kontrolliert Versionsgleichheit, vier Skill-/Prompt-Profile, Quellenhashes, alle Originale und Anhänge, Formelcaches, Lesefassungen und Paketbytes. Der Generatorregressionstest verhindert, dass eine Komponentenversion wieder durch die ältere globale Katalogversion ersetzt wird. Die Paketierung verwendet die bestehenden zentralen Aktenbuilder. Ein optionaler Renderingtest der unveränderten alten Kasseler Akte wird im alten Hochrisikoprüfer ohne bereitgestelltes Altartefakt übersprungen; die neun neuen Akten werden gesondert tatsächlich gebaut und geprüft.

Zwei globale Altbefunde bleiben ausdrücklich bestehen: `audit-skill-activation.py` beanstandet die bereits im Ausgangscommit zu lange Beschreibung des außerhalb dieser Fachrunde liegenden Skills `ki-native-kanzlei/skills/posteingang-mandate-zuordnen`. `quality-lab.py audit` beanstandet die bereits fehlenden individuellen Profile für `agb-werkstatt` und `kanzlei-website-redaktion`. Diese Lücken werden weder durch leere Profile kaschiert noch als erfolgreiche Prüfungen ausgegeben. Die in dieser Runde bearbeiteten Profile sind gültig. Der globale Navigationsnachlauf hat außerdem sieben unveränderte Altbefunde: ein außerhalb des Repositorys liegendes historisches Proben-Ziel und sechs direkte Markdown-Verweise bei Betreuung/Geldwäsche. Die KI-Verordnungs-Downloadwege und alle 505 Akten-Downloadseiten sind im Nachlauf fehlerfrei. Der vollständige Hauptproblem-Indexgenerator hängt an dem fehlenden Fremdprofil; die vier neuen bzw. erweiterten Einträge sind gezielt synchronisiert.

## 1.6. Unabhängige Anwendungsprobe

Eine getrennte Modellinstanz erhält nur den jeweiligen Mini-Prompt, die tatsächlich benötigten Rechtsquellen und Fallmaterial, keine Musterlösung oder Bewertungskriterien. Die erste Probe behandelt HRRank 4.2 mit Bewerberbewertung, ISO-Zertifikat, menschlicher Shortlistbestätigung, Drittel-FLOP-Behauptung und einer pauschalen FRIA. Die zweite behandelt die Notrufakte Mainbogen. [Ergebnisprodukte und Werkzeugbericht](anwendungsprobe/Werkzeugbericht.md) sind archiviert; Prüfvermerk, Lieferantenbrief, Meldeentscheidung und Erstbericht liegen im selben Unterordner. Die Gegenprobe führte zu einer weiteren materiellen Ergänzung: Artikel 75 Absätze 1, 1a und 1e wurden nochmals am archivierten amtlichen Wortlaut gelesen. Europäische Sonderaufsicht, abweichender Vorfallempfänger und besondere Drittbewertungsroute sind nun ausdrücklich in beiden Spezialabläufen und zwei Bestandsskills enthalten; Absätze und Ausnahmen werden getrennt geprüft.

Diese Prüfung ist eine Modellanwendung mit lokalen Dateien. Sie ist kein durchgeführter Import-/Bedienungstest in Claude Cowork, Codex und ChatGPT, keine technische Konformitätsbewertung eines wirklichen KI-Systems und keine tatsächliche Behördenmeldung.

## 1.7. Veröffentlichung

Das Komponentenrelease enthält 215 Dateien. Der manuelle Workflow prüft zunächst Quellen und Pakete, erzeugt dann Tag und Release, lädt alle Assets hoch und verifiziert sie durch erneuten Download. Erst nach erfolgreichem Abgleich wird der zunächst technisch angelegte Entwurf öffentlich. Ältere allgemeine Sammelarchive bleiben unverändert und werden nicht als aktuelle Fassung beworben.
