# 1. Geldwäschebeauftragter – Prüfbericht 445.34.0

Stand: 08.10.2026. Geprüft wurde die neue Komponente mit zehn Fachskills und einem Hauptproblem-Skill, drei eigenständigen Prompts und drei Fallakten. Dies ist kein Nachweis der fehlerfreien Prüfung des gesamten Repositorys oder sämtlicher Mandate.

## 1.1. Fachliche Quellen

[Organisation und KYC](organisation-quellen.md) und [Meldung und Notariat](meldung-notariat-quellen.md) dokumentieren die tatsächlich geöffneten amtlichen Normtexte und Entscheidungsstellen. Die dazugehörigen JSON-Register enthalten URLs, gelesene Passagen und Abruf-Hashes. Unveränderte HTML-Abrufe sind platzsparend als GZIP archiviert; das Register unterscheidet Original- und Archivhash. Schrift- und Zeilenformat der amtlichen Rohdaten wurden nicht nachbearbeitet. Amtliche Entscheidungsanker sind die EuGH-Urteile C-84/24 und C-483/23 aus 2026 sowie C-562/20, C-37/20 mit C-601/20, C-694/20 und C-305/05. Jede Verwendung enthält Aussage und Grenze. Verwaltungs- und Portalhinweise werden von Normtext und Rechtsprechung getrennt.

Besonders kontrolliert wurden Verpflichtetenstatus statt pauschaler Unternehmenspflicht, weisungsfreier Meldeweg, registergestützte Identitätsprüfung unter ihren Voraussetzungen, tatsächliche Kontrolle, Schwellen des Güterhandels, Beratungsschutz mit Rückausnahmen, GwGMeldV gegenüber GwGMeldV-Immobilien, Barzahlungsverbot gegenüber Nachweistoleranz und der besondere notarielle Vollzug. § 16a Absatz 5 Satz 3 wurde nach einem Befund der unabhängigen Probe berichtigt.

## 1.2. Arbeitsabläufe und Prompts

Die Fachskills liefern benannte Produkte an den Hauptskill zurück. Verpflichtungsprofil, KYC-Vermerk, Screening-Vermerk und notarieller Prüfstand verwenden einheitliche Kennungen. Der Kontrollplan gehört zur Risikoanalyse; der Kontrollbericht belegt die tatsächliche Durchführung. Noch fehlende Informationen stoppen nur den abhängigen Arbeitsschritt. Eine technische Versandautorisierung erzeugt keinen Geschäftsleitungsvorbehalt für die unabhängige Meldeentscheidung.

Das [Prüfprofil](../evals/geldwaeschebeauftragter.json) enthält individuelle Prüfaufträge, Quellen, fachliche Kriterien und SHA-256-Werte der Prompts. Die dokumentierte Redaktion ist eine Schreibtischprüfung. [Umfang und PDF-Quellhashes](umfang.json) erlauben den Abgleich mit den Lesefassungen. Mini und Hauptproblem bleiben unter 7.500 UTF-8-Bytes; MD und TXT sind jeweils identisch.

## 1.3. Tatsächliche Anwendungsprobe

Ein unabhängiger Modelllauf erhielt den Notariatsfall, den Hauptskill und die benötigten Fachreferenzen, aber keine Bewertungsdateien oder kanonischen Builderdaten. [Laufbericht](anwendungsprobe.md) und seine archivierten Ergebnisse dokumentieren den tatsächlichen Umfang. Die Probe unterschied Bankabgänge, behauptete Gutschriften, eine streitige Barzahlung und erst geplante Leistung. Sie lieferte einen begründeten Vermerk und vollständige Schreiben ohne Offenlegung interner Meldeüberlegungen. Der zuerst gefundene Satzverweis und die Belegzuordnung im Excel-Verlauf wurden korrigiert.

Diese einzelne Probe ersetzt weder eine statistische Wirksamkeitsmessung noch einen Test in Claude Cowork, Codex, ChatGPT oder einem FIU-Portal. Kein externer Zugang, keine reale Meldung, keine Unterschrift und kein Versand wurden ausgeführt.

## 1.4. Testakten und Rechenprüfung

Erfurt, Berlin und Würzburg enthalten jeweils 25 native Arbeitsstücke: acht PDF-Belege, vier Word-Dateien, zwölf E-Mails und eine Excel-Arbeitsmappe. Die 36 E-Mails enthalten zusammen 22 binäre Anhänge, die mit den Originaldateien abgeglichen werden. Die Ausgangsunterlagen enthalten keine rechtliche Musterlösung. Drei zunächst als offene Prüfvermerke angelegte Stücke wurden vor Veröffentlichung durch tatsächliche Telefonnotizen ersetzt; der zentrale Exportfilter bleibt unverändert.

Die Arbeitsmappen trennen Vertragssoll, Kassenbeleg, Bankabgang, Planwert und Behauptung. Unbekannte Beträge stehen als „keine Angabe“, nicht als null. Berechnete Zusammenfassungen wurden mit unabhängig vorgegebenen Fallbeträgen und einem Ein-Euro-Änderungsversuch geprüft. Alle zwölf Blattansichten wurden gerendert und angesehen. Bei der Würzburger Chronologie wurden die beiden Bankbelege und die datierten Aussagen von Käuferin und Mutter einzelnen Quellen zugeordnet.

Die Gesamt-PDFs und die ZIPs entstehen mit den zentralen Repository-Werkzeugen. Die Original-ZIPs enthalten die 25 Arbeitsstücke plus Gesamt-PDF, die Einzel-PDF-ZIPs 25 Dokumentfassungen. Beide erhalten die vorgeschriebene README.txt zuerst; die Hinweise werden nicht in die PDFs eingeschoben. Die native Excel-Datei bleibt unverändert. Ein ausschließlich auf diese drei Fallregister begrenzter PDF-Renderer teilt die neun Zahlungsspalten in zuordenbare Blöcke und setzt Tabellen in 9,5 pt. Ein Regressionstest kontrolliert sämtliche sichtbaren Zellinhalte, Schriftgrößen, Seitenbegrenzungen, fehlende Formelcaches und unveränderte Originalhashes. [Layoutprüfung](pdf-layout.md): 179 finale Seiten technisch geprüft; alle 384 Excel-Textzellen erhalten. Die zuvor zu kleine Druckschrift ist behoben.

## 1.5. Technische Abnahme

Die aktuelle Abnahme wird mit `scripts/test-geldwaeschebeauftragter.py --dist <Verzeichnis>` durchgeführt. Sie kontrolliert Inhaltsbezüge, Anhänge, Tabellen, Versionen, Links, Promptgrenzen, Exportvollständigkeit, die unveränderten zentralen ZIP-Regeln und die Prüfsummen aller 19 Release-Dateien. Ergänzend werden YAML-Frontmatter, Pluginstruktur, Marketplace, Markdownstruktur, Navigation, Komponentenrouten und Qualitätsprofile geprüft. Die Ergebnisse des abschließenden Laufs stehen unten.

Der Release-Workflow baut die Pakete aus main, erzeugt den Komponententag selbst und veröffentlicht erst nach bytegleichem Downloadabgleich. Historische allgemeine Sammelarchive werden nicht als aktualisiert ausgegeben.


## 1.6. Ergebnis der lokalen Abnahme am 08.10.2026

| Prüfung | Ergebnis |
| --- | --- |
| `test-geldwaeschebeauftragter.py --dist /tmp/aml-dist-final` | 9 Tests bestanden, keine übersprungene Paketprüfung; 19 Assets, alle Originalbytes und Prüfsummen abgeglichen |
| `test-aml-fallregister-pdf.py` | 5 Regressionstests bestanden; Blattinhalte und lesbare Druckfassung |
| `test-office-resilience.py` | 11 Tests bestanden; bestehende Office-Pfade und begrenzte Verarbeitung |
| `test-registerakten-print-profile.py` | 7 Tests bestanden; andere Druckprofile unverändert |
| `validate-yaml-frontmatter.py` | Keine Fehler oder Warnungen |
| `validate-plugin-structure.mjs` und Codex-Pluginvalidator | Bestanden |
| `validate-marketplace-import.mjs` und `test-marketplace-import.py` | Bestand geprüft; 5 Tests bestanden |
| `validate-markdown-structure.py` | Bestanden am Komponenten-Ausgangsstand |
| `validate-root-readme-overview.py` | Zähler und Verweise für 291 Plugins und 490 zentrale Akten stimmig |
| `test-readme-navigation.py` | 41 Tests bestanden; kuratierte Promptliste ergänzt |
| `test-scoped-release-routing.py` | 6 Tests bestanden |
| `quality-lab.py audit` | 291 individuelle Profile vollständig; keine pauschale Modellbewertung behauptet |
| `git diff --check` | Keine Whitespacefehler |

Der repositoryweite Aktivierungs-Audit meldete daneben eine bereits im Ausgangscommit vorhandene Beschreibung mit 382 Zeichen im Skill `ki-native-kanzlei/skills/posteingang-mandate-zuordnen`. Die elf neuen Beschreibungen halten die Grenze von 360 Zeichen ein. Der bestehende Fremdbefund wurde nicht durch eine gelockerte Prüfschwelle verdeckt. Ein vollständiger globaler Sammelrelease wurde nicht gebaut.

Beim Pakettest wurde eine unzutreffende Testannahme korrigiert: Word-Dokumente enthalten ihre Kennung im Dateinamen, nicht zwingend im Textkörper. Für deren Einzel-PDFs prüft der Test jetzt den tatsächlichen Titel und sämtliche Absätze statt einer erfundenen Pflicht zur Kennung im Brieftext. Die zentralen Paketvalidatoren blieben unverändert.

## 1.7. Nachlauf des Linux-Release-Builds

Der erste GitHub-Lauf am 08.10.2026 bestand die Quellen- und Rendererprüfungen, stoppte aber vor der Veröffentlichung beim Word/PDF-Inhaltsvergleich: LibreOffice brach das Aktenzeichen `NF-2026-0915` nach `NF-` um; die Textextraktion enthielt dadurch zusätzlichen Leerraum. Der Vergleich glättet nun ausschließlich Leerraum nach einem Bindestrich zwischen Wortzeichen. Sämtliche Buchstaben, Zahlen und Satzzeichen bleiben erhalten; Titel und alle Absätze werden weiterhin vollständig verglichen. Ein zusätzlicher Regressionstest prüft verschiedene Umbrüche sowie abweichende, fehlende und doppelte Zeichen. Die Komponentensuite umfasst damit zehn Tests. Akten, PDFs, Prompts und zentrale Paketvalidatoren wurden für diese Korrektur nicht geändert.
