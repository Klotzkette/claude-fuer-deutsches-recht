# Kanzleistart und Posteingang: Komponentenprüfung 445.34.0

## 1. Ziel und begrenzter Umfang

Eine neu beginnende Kanzlei braucht vor der ersten produktiven Automatisierung eine klare Organisation: verantwortliche Berufsträger, führende Akte und Fristenkalender, Kontorechte, Vertretung und erprobte Wiederherstellung. Danach soll der Posteingang zügig zum beauftragten Dokument führen, ohne Mandate zu vermischen oder eine nur vorbereitete Handlung als erledigt zu melden.

Zwei neue Skills und der Befehl `/kanzlei-starten` ergänzen die achtzehn bisherigen Skills. Hauptskill, Organisationsvorlage, Werkstatt, Mini und Hauptproblem verweisen auf dieselbe Trennung von Einrichtung und laufender Mandatsarbeit. Eine widersprüchliche pauschale Versanduntersagung in der Vorlage wurde an die bestehenden Regeln für ausdrücklich freigegebene Außenhandlungen angepasst. Der persönlich erforderliche beA-Schlussakt und das eEB bleiben davon unberührt.

## 2. Quellenabgleich am 8. Oktober 2026

Die neuen Berufsrechtsaussagen wurden an den amtlichen Texten zu [Paragraf 27 BRAO](https://www.gesetze-im-internet.de/brao/__27.html), [31a BRAO](https://www.gesetze-im-internet.de/brao/__31a.html), [43e BRAO](https://www.gesetze-im-internet.de/brao/__43e.html), [51 BRAO](https://www.gesetze-im-internet.de/brao/__51.html) und [59f BRAO](https://www.gesetze-im-internet.de/brao/__59f.html) abgeglichen. Kanzleisitz, Empfangspflicht, Dienstleisterzugang, persönliche Versicherung und Gesellschaftszulassung werden nicht miteinander gleichgesetzt. Für gesellschaftsbezogene Versicherungsdetails bleibt die gesonderte Berufsrechtsprüfung erforderlich; hier wurden keine ungeprüften Versicherungssummen ergänzt.

[Paragraf 23 RAVPV](https://www.gesetze-im-internet.de/ravpv/__23.html), [26 RAVPV](https://www.gesetze-im-internet.de/ravpv/__26.html) und [130a ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html) tragen die Unterscheidung von Zugangsrechten, Geheimnisschutz und Übermittlungsweg. [BVerwG, Beschluss vom 16.05.2025, 5 B 8.25, Randnummern 3 bis 5](https://www.bverwg.de/160525B5B8.25.0) betrifft die gerichtliche Eingangskontrolle im dortigen Verwaltungsprozess. Der Anker ist keine Freigabe autonomer Kanzleiführung.

Die aktuellen Herstellerdokumentationen zur [Computersteuerung in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) und zu [Computer Use](https://learn.chatgpt.com/docs/computer-use) wurden gelesen. Insbesondere bleibt die ausdrückliche Warnung vor sensibler juristischer Computerarbeit sichtbar. Die Installation verändert weder Betriebssystemrechte noch Appberechtigungen und stellt keinen eigenen Postfachtransport bereit. Unveränderte Normanker anderer Skills wurden in dieser Runde nicht erneut vollständig recherchiert.

## 3. Inhaltliche Gegenproben

Das Prüfprofil enthält jetzt 15 definierte Fälle mit 60 Kriterien. Die zwei neuen Fälle betreffen die ungeklärte Gesellschaftszulassung bei vorhandener Kanzleisoftware sowie zwei Mandate desselben Absenders, gleichnamige Anhänge, unvollständige Suchseiten und einen unklaren Versandversuch. Diese Kriterien sind redaktionelle Abnahmemaßstäbe, keine behaupteten externen Modellläufe.

Im Einzelnen verlangen die Abläufe: bestehende Systeme nicht ungefragt ersetzen, private Konten ausnehmen, Geheimnisse nicht abfragen, Sicherungen isoliert erproben, nur belegte Betriebsbereitschaft melden, Quellnachrichten und Anlagenversionen erhalten und Wiederholungen nach Timeout verhindern. Der Ausfall eines Zugangs stoppt nur davon abhängige Schritte; ein ausdrücklich erteilter Auftrag für unabhängige Dokumentarbeit läuft weiter.

## 4. Technische Prüfungen

Folgende Prüfungen wurden lokal ausgeführt:

| Prüfung | Ergebnis |
| --- | --- |
| `test-ki-native-kanzlei-start.py` | 5 redaktionelle Regressionstests bestanden |
| `test-ki-native-kanzlei-computerlauf.py` | 35 Laufzeitprüfungen bestanden |
| `test-ki-native-kanzlei-lauf.py` | 30 Prüfungen bestanden |
| `test-ki-native-kanzlei-fristen.py` | 18 Prüfungen bestanden |
| `test-si-native-kanzlei.py` | 19 Prüfungen bestanden |
| `test-si-native-kanzlei-exporte.py` | 16 Prüfungen bestanden |
| `test-marketplace-import.py` | 5 Prüfungen bestanden |
| `test-ki-native-kanzlei-source.py` | 20 Skills, Format, relative Skilllinks, Promptgrenzen und Quellprüfsummen bestanden |
| `test-ki-native-kanzlei-pakete.py` | Installationspakete quellidentisch, PDF-Prüfsummen korrekt, alle 240 Falloriginale unverändert |
| `validate-marketplace-import.mjs` | 290 Plugins und 23161 Skills strukturell geprüft |
| `validate-plugin-structure.mjs` | Struktur und relative Verweise bestanden |
| `validate-yaml-frontmatter.py` | Keine Fehler oder Warnungen |
| `validate-markdown-structure.py` | Dezimale Dokumentstruktur geprüft |
| `quality-lab.py audit` | 290 vollständige Prüfprofile; keine automatische Aussage über Modellqualität |

Mini und Hauptproblem umfassen 7419 beziehungsweise 7497 UTF-8-Bytes. Die zugehörigen TXT-Dateien sind byteidentisch. Die Werkstatt enthält 14710 Wörter. Die neu erzeugte lokale Lesefassung umfasst 300 A4-Seiten in Times New Roman 11 pt, davon je vier Seiten für die beiden neuen Skills. Quell- und Dateiprüfsummen stehen in [umfang.json](umfang.json), Struktur- und Paketnachweise in [struktur-pruefung.json](struktur-pruefung.json) und [paket-pruefung.json](paket-pruefung.json).

Die erste Seite des Einrichtungsskills und die zweite Seite des Posteingangsskills wurden als gerenderte Bilder visuell geprüft: Tabellen, deutsche Zeichen, Kopf- und Fußzeilen sowie Absatzabstände sind lesbar und ohne Überdeckung. Der bestehende PDF-Builder kontrolliert zusätzlich die Textübernahme. Der Release-Satz verwendet Liberation Serif; dessen Prüfsummen und Umfang stehen im tatsächlich ausgelieferten Einzel-PDF-Paket.

## 5. Veröffentlichungs- und Einsatzgrenzen

Der Komponentenworkflow checkt bei manuellem Start den angegebenen Tag aus und prüft dessen Zugehörigkeit zu `main`. Ein öffentliches Release wird nicht nachträglich überschrieben. Neue Dateien werden zunächst in einen Entwurf geladen; erst nach vollständigem Download und SHA-256-Abgleich wird dieser veröffentlicht. Die allgemeine Latest-Zuordnung bleibt unverändert.

Es wurden keine echten Postfächer, beA-Konten, Mandantenakten oder produktiven Kalender geöffnet. Es gab keinen Live-Sendeversuch und keine autonome Mandatsannahme. Weder die neuen Texttests noch die vorhandenen Laufzeitprüfungen beweisen die Zuverlässigkeit fremder Oberflächen. Das lokale Journal ist keine vom Betriebssystem erzwungene Sicherheitsgrenze. Vor dem Echtbetrieb bleiben Herstellergrenzen, organisatorische Prüfung, geeignete Kontorechte und ein kontrollierter Probelauf erforderlich.
