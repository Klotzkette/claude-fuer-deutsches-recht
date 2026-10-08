# 1. Betreuungsrecht 445.33.3

Stand: 08.10.2026. Der fachliche Prüfstand der Abschnitte 1.1 bis 1.6 stammt aus 445.33.2; der Namensnachtrag für 445.33.3 steht in Abschnitt 1.7. Die ursprüngliche Runde ergänzt die Unterlagenauswertung bei Betreuungsübernahme. Sie ist keine Vollprüfung des gesamten Betreuungsrechtsbestands und kein Nachweis fehlerfreier Rechtsberatung.

## 1.1. Bestand und Ergänzung

Die vorhandene Akte Schmalfeld enthält bereits Kontounterlagen der Jahre 2023 bis 2025, Vertragsunterlagen und E-Mails. Sie und die Akte Hildegard Sauer bleiben unverändert. Neu hinzu kommt die Dreijahresakte Adelheid Pfister mit historischem Analysezeitraum 01.10.2023 bis 30.09.2026, Übernahme am 01.10.2026 und Bearbeitungsstand 08.10.2026.

Der neue Skill `unterlagen-auswerten-abrechnung-anschreiben` verbindet Belegaufnahme, Excel-Aufbereitung, Saldenabgleich, rechtliche Einordnung und adressierte Anschreiben. Er umfasst 3.645 Wörter. Der eigenständige Unterlagen-Werkstatt-Prompt umfasst 5.863 Wörter; Markdown und TXT sind byteidentisch. Allgemeine Werkstatt, Mini, Auslöser und drei Nachbarskills führen zum neuen Arbeitsweg. Die 7.500-Byte-Grenze des allgemeinen Mini-Prompts bleibt eingehalten.

## 1.2. Quellen und Fachlogik

[Quellenbericht](unterlagen-quellen-2026-10-08.md) und [Abrufnachweise](unterlagen-quellen-2026-10-08.json) dokumentieren 38 amtliche Normtexte sowie den amtlichen Volltext des BGH-Beschlusses vom 21.01.2026, XII ZB 182/25. Die Reichweite des Entscheidungsankers wird begrenzt: Sachaufklärung im jeweiligen Geschäftszeitpunkt, keine pauschale Unwirksamkeit früherer Zahlungen wegen heutiger Betreuung.

Berichtigt wurden konkrete Altnormfehler zur Rechnungslegung, Geldanlage und Akteneinsicht in den verbundenen Skills. Historische Vertragsschlüsse verlangen weiterhin die zeitlich einschlägige Fassung. Nicht untersuchte Spezialfragen des bestehenden Plugins werden nicht als neu verifiziert ausgegeben.

## 1.3. Rechnungsdaten und Dateien

Die Falldaten enthalten 584 Buchungen, zwei Konten, 72 Monatsauszüge und 83 Rechnungsbelege. Alle Buchungen haben eine tatsächliche PDF-Fundstelle. Belege und Rechnungen sind mit Zahlungen verknüpft; nicht jeder Geldabfluss hat bereits einen vollständigen Verwendungsnachweis. Fensterrechnung, Angehörigenzahlung und Teilrückzahlung dürfen gerade nicht als ein und derselbe Betrag behandelt werden.

Die Kontrollrechnung außerhalb des Aktenexports ergibt 32.300,00 EUR anfängliches Bankvermögen und 41.385,92 EUR Schlussbestand. Externe Bankzuflüsse betragen 90.403,40 EUR, externe Bankabflüsse 81.317,48 EUR. Diese Summen sind Zahlungsdaten und keine Feststellung von Einkommen, Verbrauch oder Schaden. 30 Buchungszeilen betreffen interne Transfers. Die [Kontrollwerte](pfister-kontrollwerte.json) gehören nicht zum Teilnehmerarchiv.

Die [Excel-Prüfung](excel-pruefung.md) dokumentiert die drei Arbeitsmappen, 72 ausgeglichene Monatsrechnungen, Eingabeänderungen und zusätzliche LibreOffice-Neuberechnung. Die fallneutrale Vorlage hat sechs Blätter. Alle zehn Blätter der drei Dateien wurden gerendert und visuell geprüft. Es wurde kein Live-Test in Microsoft Excel behauptet.

## 1.4. Anwendungsprobe

Eine unabhängige Agentenprobe arbeitet mit dem neuen Skill und ausgewählten Originalunterlagen, ohne die Kontrollwerte oder den Generator zu lesen. Ihr [gesonderter Bericht](anwendungsprobe-2026-10-08.md) nennt gelesene Fundstellen, erzeugte Schreiben und Grenzen. Das ist kein Test in der Benutzeroberfläche von Claude Cowork oder ChatGPT und kein Nachweis einer tatsächlich versandten Nachricht.

## 1.5. Auslieferungsgrenzen

Plugin, eigenständiger Prompt und Testakte werden getrennt angeboten. Der Komponentenrelease aktualisiert keine älteren Sammel-ZIPs. Original- und Einzel-PDF-Archive sind flach und beginnen mit der vorgeschriebenen zweisprachigen README.txt. Die Gesamtakte und Einzel-PDFs enthalten keine Warnseiten. Sämtliche Namen, Kontakte und Vorgänge des neuen Falls sind erfunden.

Die Rechnungsrekonstruktion ersetzt weder eine gerichtliche Rechnungslegung noch eine abschließende Anspruchsprüfung. Schreiben bleiben Entwürfe. Es wurden keine echten Banken, Angehörigen, Anbieter oder Gerichte kontaktiert.

## 1.6. Abschlussprüfungen

Die neue Akte umfasst 207 Originaldateien: 161 PDFs, acht Word-Dateien, vier PNG-Bildschirmabbildungen, 32 EML und zwei XLSX. Die Gesamtfassung hat 436 Seiten. Sämtliche Seiten wurden auf Text außerhalb der Seitengrenzen geprüft; es gab keinen Treffer. Repräsentative Seiten aus E-Mail, Excel und Original-PDF wurden zusätzlich visuell geprüft. Die Originalprüfung ist im [Aktenbericht](pfister-aktenpruefung.md) dokumentiert.

Erfolgreich ausgeführt:

1. `python3 scripts/test-betreuungsrecht-unterlagen.py --dist /tmp/betreuung-release-445.33.2`: neun Tests ohne Überspringen. Der Pakettest ruft die unveränderten Kernfunktionen beider zentraler ZIP-Validatoren für genau diese Akte auf. Geprüft werden auch A4-Format, vollständiger Dateibestand und Warntextregeln; globale Sammelarchive sind kein Bestandteil dieses Releases.
2. `python3 scripts/validate-yaml-frontmatter.py`, `python3 scripts/audit-skill-activation.py`, `python3 scripts/test-marketplace-import.py` und `python3 scripts/validate-markdown-structure.py`.
3. `python3 scripts/validate-root-readme-overview.py`, `python3 scripts/test-readme-navigation.py` mit 41 Tests und `python3 scripts/test-scoped-release-routing.py`.
4. `python3 scripts/quality-lab.py audit`: alle 290 Profile strukturell vollständig. Das ist keine inhaltliche Bewertung aller Plugins durch ein Modell.
5. Quellen-, Excel-, EML-, Word- und unabhängige Anwendungsprüfung gemäß den verlinkten Einzelberichten. Die Schmalfeld- und Sauer-Dateien weisen gegenüber dem Ausgangscommit keinerlei Änderung auf.

Die umfassenden Repo-Prüfungen wurden auch gegen den unveränderten Ausgangscommit `4f22d1fd58965cb5c617dfd68ea8aa08e3e7fbbd` gegengeprüft. Zwei bekannte Altbefunde bleiben außerhalb dieser Komponente bestehen:

1. `validate-runtime-performance.py` meldet bereits im Ausgangsstand 23.158 Skills bei einem globalen Budget von 23.000 und 3.679.448 Beschreibungszeichen bei 3.630.000. Mit der Ergänzung sind es 23.159 und 3.679.706. Die Einzelplugin-Grenzen werden eingehalten; Budgets wurden nicht angehoben oder deaktiviert.
2. `validate-testakten-readme-downloads.py` meldet in beiden Ständen dieselben fünf Befunde zur Akte `it-sig-2-vergabe-landeshauptstadt-schwerin-nachpruefung` und zur Fachanwaltsseite Vergaberecht. Für die neue Pfister-Akte verbleibt kein Downloadblock-Befund. Die bestehenden Vergaberecht-Links wurden in dieser fachlich getrennten Runde nicht verändert.

Damit wird ausdrücklich kein vollständig grüner Gesamtzustand aller Repository-Prüfungen behauptet. Die Komponentenprüfung enthält keine pauschalen Ausnahmen für unbekannte Fehler.

## 1.7. Namensumstellung auf Adelheid Pfister

Auf Nutzerwunsch trägt die Akte in 445.33.3 den Familiennamen Pfister. Zugehörige Angehörige heißen Ruprecht Pfister und Juna Özdemir-Pfister. Aktuelle Dateipfade, Kontaktangaben, Skillbeispiel, Unterlagen-Werkstatt und Qualitätskopien verwenden denselben Namen. Die Umstellung ändert weder die Buchungen und Rechenergebnisse noch den Sachverhalt oder die rechtliche Methodik.

Die verlinkten Probeprodukte wurden ausschließlich redaktionell auf die neuen Namen und Pfade umgestellt. Die unabhängige Agentenprobe und die amtliche Quellenprüfung aus 445.33.2 wurden nicht wiederholt; ihre damaligen Grenzen gelten fort. Die neuen Prompt- und Skillhashes sind im [Prüfprofil](../evals/betreuungsrecht.json) dokumentiert. Historische Releasebeschreibungen und der Changelog-Eintrag für 445.33.2 bleiben als damaliger Stand erhalten.

Die neu erzeugte Gesamt-PDF enthält 436 Seiten aus 207 Originaldateien. Nach Ersetzung ausschließlich des Familiennamens sind die kanonischen Daten mit der Vorfassung vollständig identisch, einschließlich aller 584 Buchungen. Der Vergleich sämtlicher Excel-Bestandteile bestätigt unveränderte Zahlen, Formeln und Formatierungen; die fallneutrale Vorlage bleibt bytegleich. Alle neun Komponentenprüfungen einschließlich der beiden ZIP-Varianten sind bestanden. Frontmatter, Pluginstruktur, Marketplace, Release-Routing, Markdownstruktur, Hauptübersicht und Profilvollständigkeit sind geprüft. In der neuen Gesamt-PDF erscheint der alte Familienname nicht; alle Textbegrenzungen liegen innerhalb der Seiten. Die historische Aktenverknüpfung der Releasebeschreibung 445.33.2 ist auf den damaligen Tag festgeschrieben.
