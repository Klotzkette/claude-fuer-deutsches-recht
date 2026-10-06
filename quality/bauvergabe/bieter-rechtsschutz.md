# 1. Umfang und Ergebnis

Die Plugins `bauvergabe/bauvergabe-bieter` und `bauvergabe/bauvergabe-rechtsschutz` wurden mit Version 445.32.0 angelegt. Jedes enthält genau zehn Fachskills und einen elften Hauptskill, beide Manifestvarianten, eine README, lokale Quellen und Zitierregeln sowie Werkstatt- und Schnellstartprompt jeweils als bytegleiche MD-/TXT-Paare. Persönliche Marketplace-Dateien, globale Generatoren und Git-Zustand wurden in diesem Teilauftrag nicht verändert.

| Plugin | Werkstattzeichen | Minizeichen | Mini UTF-8-Bytes | Skills |
| --- | ---: | ---: | ---: | ---: |
| Bauvergabe Bieter | 48.961 | 7.342 | 7.467 | 11 |
| Bauvergabe Rechtsschutz | 49.687 | 7.392 | 7.495 | 11 |

Die Hauptskills verwenden ausschließlich tatsächlich enthaltene Fachskills und lokale Referenzen. Kein installierter Skill benötigt die Werkstatt, den Schnellstart oder einen Repository-Leitfaden. Die READMEs verlinken die beiden gemeinsamen Testakten; die zentralen Downloadgruppen werden im Integrationsschritt ergänzt.

# 2. Tatsächlich ausgeführte Prüfungen

Am 06.10.2026 wurden beide Plugins mit dem offiziellen `plugin-creator/scripts/validate_plugin.py` geprüft: beide erfolgreich. Alle 22 Skills wurden mit `skill-creator/scripts/quick_validate.py` geprüft: keine Fehler. Eine zusätzliche Strukturprüfung bestätigte die sechs nummerierten Skillblöcke, exakt elf Skills je Plugin, bestehende relative Links aus sämtlichen Skills und Referenzen, fehlende Laufzeitabhängigkeit zu den Großprompts und Bytegleichheit der MD-/TXT-Paare. Die Minis unterschreiten sowohl 7.500 Zeichen als auch 7.500 UTF-8-Bytes.

Die Evaluationsprofile `quality/evals/bauvergabe-bieter.json` und `quality/evals/bauvergabe-rechtsschutz.json` enthalten jeweils elf konkrete Szenarien, redaktionelle Prüfnotizen und SHA-256-Hashes der beiden Promptfassungen. Sie dokumentieren eine redaktionelle Prüfung und die tatsächlich ausgeführten Strukturprüfungen. Es wurden keine unbeobachteten Modellläufe, Plattformeinreichungen oder automatischen Veröffentlichungen als erfolgreich bezeichnet.

# 3. Quellenprüfung und wesentliche Rechtsentscheidungen

Die amtlichen Texte wurden am 06.10.2026 online gelesen. Besonders berücksichtigt sind [Paragraf 187 Absatz 2 GWB](https://www.gesetze-im-internet.de/gwb/__187.html), das Ende des Zuschlagsverbots bei Obsiegen des Auftraggebers schon mit Bekanntgabe nach [Paragraf 169 Absatz 1 Satz 2 GWB](https://www.gesetze-im-internet.de/gwb/__169.html) und die fehlende aufschiebende Wirkung nach Ablehnung gemäß [Paragraf 173 Absatz 1 GWB](https://www.gesetze-im-internet.de/gwb/__173.html). Die Beschwerdefrist wird nicht mit einer zusätzlichen Sperre gleichgesetzt. Alte Anträge auf Verlängerung einer automatisch eintretenden aufschiebenden Wirkung werden nicht als neues Recht ausgegeben.

Die Auslöser der [Wartefrist nach Paragraf 134](https://www.gesetze-im-internet.de/gwb/__134.html) und der [Rüge-/Antragsfristen nach Paragraf 160](https://www.gesetze-im-internet.de/gwb/__160.html) bleiben getrennt. Der amtliche HTML-Text zu Paragraf 134 wurde bei einem vorübergehend fehlerhaften Web-Abruf zusätzlich direkt gelesen. Paragraf 160 wird einschließlich seiner aktuellen Sonderregel im Absatz 2 und des Missbrauchstatbestands behandelt.

Die [VOB/A-Bekanntmachung vom 22.07.2026](https://www.bundesanzeiger.de/pub/publication/73xO0rpP1jfX5HRt0Ja/content/73xO0rpP1jfX5HRt0Ja/BAnz%20AT%2024.08.2026%20B6.pdf) wurde im amtlich gewonnenen Volltext gelesen. Berücksichtigt sind insbesondere Eigenerklärungen, Eignungsleihe, Leistungsbeschreibung, Haupt- und Nebenangebote, Nachforderungspflicht mit Grenzen, die Sollfrist von sechs Kalendertagen, die Prüfungsreihenfolge im offenen Verfahren sowie die getrennte Behandlung von Aufklärung und neuem Angebot. Der Losgrundsatz liegt im geltenden Paragraf 97a GWB; eine klassische Bauvergabe wird nicht pauschal zur Sektorenvergabe.

Für Unterschwellenstreitigkeiten wurde [Paragraf 71 Absatz 2 Nummer 8 GVG](https://www.gesetze-im-internet.de/gvg/__71.html) mit ausschließlicher Landgerichtszuständigkeit unabhängig vom Streitwert geprüft, ohne Rechtsweg und örtliche Zuständigkeit zu überspringen. [Paragraf 135 GWB](https://www.gesetze-im-internet.de/gwb/__135.html) wird mit qualifizierten Fristauslösern und Absatz 4 behandelt. [Paragraf 165 GWB](https://www.gesetze-im-internet.de/gwb/__165.html) berücksichtigt die sichere elektronische Einsicht und konkrete Geheimniskennzeichnung.

BGH, Urt. v. 18.06.2019 – Az. X ZR 86/17, wurde über die amtlich indexierten Leitsätze geprüft; der alte Datenbankendpunkt war später wechselhaft erreichbar. Deshalb werden keine nicht erneut geprüften Randnummern behauptet. EuGH, Urt. v. 29.03.2012 – Az. C-599/10, Rn. 40–44, wurde anhand des amtlichen Textes geprüft. Für Rechtsschutz wurden EuGH, Urt. v. 17.11.2022 – Az. C-54/21, Rn. 64–66 und 83–85, sowie die amtlichen Entscheidungsdaten und Zusammenfassung von EuGH, Urt. v. 12.02.2004 – Az. C-230/02, mit deren Randnummernverweisen geprüft. Die Quellenreferenzen benennen die technischen Abrufgrenzen und fachlichen Übertragungsgrenzen ausdrücklich.

# 4. Unabhängige Prüfung der Auftraggeberplugins

Nach der eigenen Erstellung wurden `bauvergabe-unterlagen` und `bauvergabe-verfahren` unabhängig gelesen und strukturell geprüft. Beide enthalten elf Skills. Ihre Minis liegen bei 7.475 beziehungsweise 7.450 UTF-8-Bytes; die Werkstätten bei 49.899 beziehungsweise 49.287 Zeichen. Alle geprüften relativen Skill- und Referenzlinks lösen innerhalb des Plugins auf; es besteht keine Laufzeitabhängigkeit von Werkstatt oder Repository-Wurzel. MD-/TXT-Paare sind jeweils bytegleich.

Die beiden Minis, Hauptskills, Quellenkarten sowie die kritischen Fachskills zu Rechtsregime, Nachforderung und Zuschlag wurden gelesen. Es wurde kein blockierender Befund gefunden. VOB/A 2026, Paragrafen 97a, 169, 173 und 187 GWB sowie getrennte Wartefristen sind sachgerecht berücksichtigt. Der Bauauftragsschwellenwert wurde unabhängig in der amtlich indexierten Verordnung (EU) 2025/2152 bestätigt; Paragraf 97a GWB und Paragraf 2 VgV wurden erneut amtlich geöffnet. Borta, Rn. 68–69 und 76, sowie die amtlichen Entscheidungsdaten und Zusammenfassung zu Roche Lietuva wurden unabhängig abgeglichen. Die Dokumentation über zeitweilige Volltextzugriffsgrenzen ist angemessen und behauptet keine umfassendere Lektüre als tatsächlich belegt.

Diese Prüfung ist eine Quellen-, Struktur- und gezielte Inhaltsprüfung. Sie ist kein beobachteter Modelllauf und keine vollständige technische Validierung aller künftigen Fallausgaben. DOCX-/PDF-Rendering und zentrale Releaseintegration erfolgen getrennt.

## Ergänzende Profilvalidierung

Nach dem zunächst erkannten fehlenden dritten Ergebniskriterium wurden am 06.10.2026 beide Evalprofile um elf jeweils fallbezogene fachliche Kriterien ergänzt. Beide Profile enthalten nun elf Fälle mit je drei Kriterien. `quality_lab.validate_profile(d, slug, root/'bauvergabe'/slug, root)` wurde für beide Profile mit `PYTHONPATH=/tmp/bauvergabe-20261006/deps` tatsächlich ausgeführt und bestand. Das ist eine Profil- und Strukturvalidierung, kein beobachteter Modelllauf.

## Abschließende Strukturkorrektur und globale Prüfläufe

Die vier Promptdateien besitzen nach Korrektur genau eine Titel-H1 und fortlaufende dezimale H2-Abschnitte; Unterabschnitte der Werkstatt stehen als H3. Die MD/TXT-Paare bleiben bytegleich. Aktuelle Maße: Bieter-Werkstatt 49.030 Zeichen / 49.827 Bytes, Bieter-Mini 7.369 Zeichen / 7.494 Bytes; Rechtsschutz-Werkstatt 49.759 Zeichen / 50.576 Bytes, Rechtsschutz-Mini 7.391 Zeichen / 7.495 Bytes. Beide Manifesttypen enthalten die Autoradresse `39582916+Klotzkette@users.noreply.github.com`. Beide Evalprofile erhielten die neuen Prompt-Prüfsummen und bestanden die erneut tatsächlich ausgeführte `quality_lab.validate_profile`-Prüfung.

Tatsächlich vollständig ausgeführt wurden `test-portable-starts.py` (11 Tests, PASS), `audit-quickstart-usability.py` (279 Schnellstarts, PASS), `audit-prompt-profile-routing.py` und `node scripts/validate-marketplace-import.mjs`. Die letzten beiden Läufe fanden ausschließlich außerhalb der beiden Plugins noch ein fehlendes globales Fachprofil beziehungsweise eine abweichende sichtbare Version in `startup-gruender/README.md`; diese globale Integration bearbeitet der Hauptagent. Logs liegen unter `/tmp/bauvergabe-20261006/logs/bieter-rechtsschutz-*.log`. Diese Aussage ersetzt keinen späteren erneuten globalen Prüflauf nach Integration.

Die Wohnhaus-Bildprüfung wurde auf alle 27 Seiten der 21 DOCX-Dokumente erweitert. Quellenhashes stimmen mit dem aktuellen Render-Manifest überein; keine verbliebenen Layoutblocker. Der konkrete Bildbeleg liegt unter `/tmp/bauvergabe-20261006/evidence/word-wohnhaus-visual.json`.

Nach der globalen Integrationskorrektur erneut vollständig ausgeführt: `audit-prompt-profile-routing.py` PASS (280 Plugins, 581 Prompts) und `node scripts/validate-marketplace-import.mjs` PASS (280 Plugins, 22.797 Skills, 280 README-Dateien). Logs: `bieter-rechtsschutz-profile-routing-final.log` und `bieter-rechtsschutz-marketplace-import-final.log` im genannten temporären Logordner.

Das Wohnhaus-Gesamt-PDF wurde anschließend vollständig auf allen 50 gerenderten Seiten visuell geprüft. Seine 45 Lesezeichen und 39 Registereinträge stimmen in Anfangsseiten und lückenlosen Seitenbereichen überein; alle 21 eingebundenen DOCX-Abschnitte stimmen im extrahierten Text mit den Einzelrenderungen überein. Keine Layoutblocker; kosmetische Notiz zum US-Zahlenformat der Excel-Druckseiten 26, 27 und 46. PDF-Prüfsumme und Einzelbildbelege: `/tmp/bauvergabe-20261006/evidence/pdf-wohnhaus-visual.json`.
