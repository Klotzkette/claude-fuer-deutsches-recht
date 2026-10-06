# 1. Qualitätsbericht Auftraggeber-Plugins Bauvergabe

Prüfdatum: 06.10.2026. Verantworteter Umfang: `bauvergabe/bauvergabe-unterlagen`, `bauvergabe/bauvergabe-verfahren` sowie die zugehörigen Profile unter `quality/evals`. Version der beiden Manifeste: 445.32.0. Keine Commits, Releases, Marketplace-Änderungen oder globalen Generatoren wurden durch diesen Teilauftrag ausgeführt.

## 1.1. Struktur und Nutzbarkeit

Beide Plugins wurden mit dem offiziellen Plugin-Creator-Gerüst initialisiert und enthalten jeweils genau zehn Fachskills plus einen elften Hauptskill. Jeder Skill hat ausschließlich `name` und `description` im Frontmatter und sechs nummerierte Innenblöcke, eine eigene Quellenpflicht sowie die ausdrückliche Ausformulierungspflicht und A4 / Times New Roman 11 pt / dezimale Gliederung im Ausgabeblock.

Die Skills verweisen ausschließlich auf innerhalb des jeweiligen Plugins mitgelieferte Referenzen und Fachskills. Beide offiziellen Plugin-Manifeste sind vorhanden. Die vollständige Zitierweise ist jeweils lokal kopiert. Die eigenständigen Werkstatt- und Schnellstartdateien sind keine Skillabhängigkeit und werden als separate Prompts beschrieben. README-Verweise auf andere Plugins und zentrale Testakten sind Navigation; zur Ausführung der elf Skills sind sie nicht erforderlich.

| Plugin | Skills | Werkstatt Zeichen | Werkstatt UTF-8-Bytes | Schnellstart Zeichen | Schnellstart UTF-8-Bytes |
| --- | ---: | ---: | ---: | ---: | ---: |
| bauvergabe-unterlagen | 11 | 49.899 | 50.572 | 7.367 | 7.475 |
| bauvergabe-verfahren | 11 | 49.287 | 50.032 | 7.328 | 7.450 |

Alle vier MD-/TXT-Paare sind bytegleich. Die Werkstätten erfüllen den vereinbarten Zeichenkorridor von ungefähr 35.000 bis 50.000 Zeichen. Beide Schnellstarts bleiben unter 7.500 Zeichen und unter 7.500 UTF-8-Bytes.

## 1.2. Tatsächlich ausgeführte Prüfungen

Die offiziellen `validate_plugin.py`-Aufrufe waren für beide Plugins erfolgreich. Der offizielle `quick_validate.py` wurde für sämtliche 22 Skillverzeichnisse ausgeführt und war ohne Fehler. Zusätzlich geprüft wurden die genaue Anzahl der Skills, die sechs Innenblöcke und sämtliche relativen Links aus den Skills; kein Ziel fehlt. Die Prompt-Paare wurden binär verglichen und ihre Zeichen- und Bytezahlen ermittelt.

Je Plugin liegt ein Evaluationsprofil mit elf konkreten Szenarien vor: zehn Fachfälle und eine Fortsetzung über den Hauptskill. Die Profile enthalten redaktionelle und Ablaufprüfung, konkrete Ergebnisdateien und Prüfkriterien sowie SHA-256 der endgültigen Werkstatt und des endgültigen Schnellstarts. Diese Profile sind redaktionelle Prüfszenarien, keine behaupteten beobachteten Modellläufe. Eine unabhängige Ausführung dieser Szenarien ist nicht Bestandteil der hier behaupteten Prüfung.

## 1.3. Rechtliche Quellenkontrolle

Die amtliche VOB/A-Ausgabe vom 22.07.2026, BAnz AT 24.08.2026 B6, wurde als PDF abgerufen und der Volltext extrahiert. Gelesen wurden insbesondere Paragrafen 5a EU, 5b EU, 6b EU, 7 EU, 7a EU, 10 EU, 10a EU, 12a EU, 13 EU, 14 EU, 15 EU, 16 EU bis 16d EU und die Anschlussregeln. Dadurch werden gerade die Änderungen zu Losen, Eigenerklärungen, Öffnung, Nachforderung und Prüfungsreihenfolge berücksichtigt.

[Paragraf 2 VgV](https://www.gesetze-im-internet.de/vgv_2016/__2.html) wurde einschließlich Bauverweisung und Planungslose-Regel geprüft. [GWB Gesamttext](https://www.gesetze-im-internet.de/gwb/BJNR252110998.html) wurde insbesondere für den neuen Paragraf 97a und die Auftraggebereigenschaft herangezogen. [Paragraf 187 Absatz 2](https://www.gesetze-im-internet.de/gwb/__187.html), [Paragraf 169](https://www.gesetze-im-internet.de/gwb/__169.html) und [Paragraf 173 GWB](https://www.gesetze-im-internet.de/gwb/__173.html) wurden direkt amtlich geöffnet. [Delegierte Verordnung (EU) 2025/2152](https://eur-lex.europa.eu/eli/reg_del/2025/2152/oj) bestätigt 5.404.000 EUR netto als klassischen Bauschwellenwert für 2026/2027.

Beide Plugins enthalten mindestens zwei echte Entscheidungsanker. Unterlagen: EuGH, Urt. v. 25.10.2018 – Az. C-413/17, Roche Lietuva, Rn. 34 bis 40; EuGH, Urt. v. 05.04.2017 – Az. C-298/15, Borta, Rn. 68 bis 69 und 76. Verfahren: Borta sowie EuGH, Urt. v. 29.03.2012 – Az. C-599/10, SAG ELV Slovensko, Rn. 40 bis 45. Die amtlich indexierten Entscheidungsdaten und Randnummernpassagen wurden geprüft. Zeitweilige EUR-Lex-Zugriffssperren verhinderten teilweise den direkten Volltextabruf; deshalb wird in den Referenzen ausdrücklich keine lückenlose Volltextlektüre aller Urteile behauptet. Übertragungsgrenzen stehen im jeweiligen Anker und verhindern eine pauschale Anwendung des alten Richtlinienrechts oder technischer Lieferfälle auf neue Bauverfahren.

## 1.4. Fachliche Schwerpunkte

Unterlagen enthält Regime und Wert, Planungsreife, Lose/GU, LV/GAEB, technische Spezifikationen, Eignung, Zuschlag, Bauvertrag, Bauarten und Freigabe. Verfahren enthält Verfahrenswahl, Bekanntmachung, Fragen/Berichtigung, Teilnehmerauswahl, Öffnung, Nachforderung, Eignung/Ausschluss, Wertung, Abschluss und Rüge-/Dokumentationsarbeit.

Kliniken und Krankenhausapothekenbauteile, Hallen, Wohnungen, Tunnel, Straßen, Autobahnen und Schutzplanken werden projektbezogen behandelt. Der Text unterscheidet rechtliche Prüfung von technischer Fachplanung, lesbarem LV und technischer GAEB-Validierung. Keine neuen technischen Messwerte, Normklassen oder Sicherheitsnachweise werden aus Modellwissen angeordnet.

## 1.5. Kanonische Akten und verbleibende Integration

Die gemeinsam festgelegten Stammdaten wurden aus `scripts/bauvergabe_falldaten.py` gelesen. Die Texte verwenden Klinikum Lindenbogen Münster gGmbH und Soziales Wohnen Bielefeld gGmbH, die Gesamtwerte 40 Mio. EUR und 8.4 Mio. EUR netto sowie die fünf getrennten Aktenstufen. Die Klinik-Mittellücke von 23.200 EUR vor Zuschlag und die unterschiedliche Streitfrage beider Verfahren sind berücksichtigt. Rechtsstand ist für die bis 2027 fiktiv fortgesetzten Akten auf 06.10.2026 eingefroren und vor echter Verwendung erneut zu prüfen.

Zentrale Akten, tatsächliche Downloads, Verpackung, Marketplace-Registrierung und Gesamttests werden durch die Integration verantwortet. Die READMEs behaupten keine bereits erzeugten Release-ZIPs. Die zentralen Testaktenlinks verwenden den korrekten relativen Pfad `../../testakten/...`.

Offene Quellenfragen betreffen nur den späteren Mandatsfall: konkrete landes- und haushaltsrechtliche Regeln unterhalb der Schwelle, tatsächliche technische Normausgaben, Betreiber- und Genehmigungsanforderungen sowie eine erneute Prüfung der tragenden Rechtsprechung vor Verwendung. Diese Grenzen sind in den Plugins ausdrücklich enthalten; es besteht keine offene normative 2026-Kernfrage, die durch eine alte SektVO-Regel ersetzt wurde.
