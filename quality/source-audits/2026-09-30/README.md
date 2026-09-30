# 1. Rechtsprechungsanker: repoübergreifender Schnelldurchgang vom 30.09.2026

## 1.1. Umfang und Aussagekraft

Ausgangsstand ist `cf6d91a3bebc07767e538622ba237702eb83a8ae` auf main. Der automatisierte Bestandsabgleich umfasst alle **255 Marketplace-Plugins** und **24.663 Markdown-Fachdateien**: Skills einschließlich ihrer Referenzen, pluginlokale Referenzen, Werkstatt-, Mini- und vorhandene Hauptproblem-Prompts sowie abgeleitete Vollprüfungen. Testakten und Vorlagensammlungen sind keine umfassend neu bewerteten Rechtsprechungsquellen dieses Durchgangs.

Als Ausgangsbasis dient die [Quellenprüfung vom 25.09.2026](../2026-09-25/README.md) mit 245 Pluginprofilen und 343 Quellenzuordnungen. Vor Beginn dieser Änderung waren 240 Profile und 480 der 490 erfassten Werkstatt-/Mini-Dateien bytegleich; fünf Profile und zehn Prompts waren verändert, zehn Pluginprofile neu. Unveränderter Text erhält dadurch **keine neue rechtliche Freigabe**: Er behält den damals dokumentierten Prüfungsumfang. Die neuen und geänderten Profile wurden gezielt auf Quellenidentität, Anwendung und Grenzen durchgesehen; einzelne Abrufgrenzen bleiben in den Fachberichten offen ausgewiesen.

Dieser Auftrag war ein schneller repoübergreifender Abgleich, **keine neue Volltextprüfung jeder Entscheidung in jedem der über 24.000 Fachtexte**. Die Aktenzeichenerkennung fand im integrierten Bestand 1.666 unterschiedliche Zeichenfolgen; sie kann Gerichte, Mehrfachentscheidungen unter demselben Aktenzeichen oder nicht erkannte Schreibweisen nicht abschließend auflösen. Daher wird weder eine Vollständigkeit der Rechtsprechung bis zum Stichtag noch eine Fehlerfreiheit sämtlicher Spezialskills behauptet. Es wurden keine Live-Modelltests durchgeführt.

Während der Abschlussprüfung wurde zusätzlich der zwischenzeitlich auf main veröffentlichte Commit `44b0d3cb2c658b345392bc90cbdea7217266b9ce` (Pflegerecht, v445.18.1) konfliktfrei übernommen. Das Bestandsregister bildet diesen integrierten Stand ab. Die dortigen Pflegeänderungen werden nicht nachträglich als eigene vollständige Quellenprüfung dieses Durchgangs ausgegeben; die technischen Integrationsprüfungen sind gesondert protokolliert.

## 1.2. Fachliche Nachweise

Konkrete Korrekturen betreffen **16 Plugins und 23 vorhandene Werkstatt-/Mini-Promptdateien**, dazu ihre einschlägigen Skills, Referenzen und abgeleiteten Texte. Beispiele: nicht existierende Randnummer bei BGH II ZR 71/24, falsche DSGVO-Empfängerentscheidung, 2026-Entscheidungen zu Unterhalt, Teilzeit-Zuschlägen und Rohmessdaten sowie falsch zugeordnete Energieentscheidungen. Hauptproblem-Prompts bleiben bei ihrem jeweiligen Fachgegenstand; ein neuer sachfremder Anker wird nicht nur wegen der Jahreszahl aufgenommen.

| Bereich | Tatsächlich geprüfte Entscheidungen, Änderungen und Grenzen |
| --- | --- |
| Arbeits-, Sozial- und Pflegerecht | [Fachbericht](arbeit-sozial.md) |
| Zivilrecht, WEG, Familie, Gesellschaft und Insolvenz | [Fachbericht](zivil-wirtschaft.md) |
| Öffentliches Recht, Steuer, Datenschutz und Verkehrsordnungswidrigkeiten | [Fachbericht](oeffentlich-straf-steuer.md), [Konsistenznachtrag zu StVG/OWiG](stvg-konsistenz.md) |
| Zentrales Suchregister, Versand, Präsentationen und Heizungsrecht | [Fachbericht](zentrale-anker-und-versand.md) |

Die neuen Anker nennen Gericht, Entscheidungsdatum, Aktenzeichen, konkrete Rechtsfolge und Übertragungsgrenze. Amtliche Pressemitteilungen, Urteilsvolltexte, Normen und technische Herstellerhinweise werden als verschiedene Quellentypen behandelt. Ein veröffentlichtes Dokument aus 2026 wird nicht allein deshalb als Urteil aus 2026 bezeichnet. Neue Entscheidungen werden an den passenden Arbeitsabläufen ergänzt; es gibt keinen universellen Ankerblock für alle Plugins.

## 1.3. Reproduzierbarer Bestand

Das [Bestandsregister](bestand.json) nennt jedes Plugin mit erkannten Aktenzeichen, Profilankern, Promptdateien, Prüfsummen und dem Unterschied zum September-25-Register. Es ist ein technisches Inventar, kein maschinelles Rechtsgutachten. Die Prüfsumme `file_inventory_sha256` bezieht sich auf die deterministisch sortierte vollständige Dateiliste einschließlich ihrer Einzelprüfsummen und erkannten Aktenzeichen; mit `--include-files` lässt sich diese vollständige Liste zusätzlich ausgeben.

```sh
python3 scripts/audit-rechtsprechungsbestand.py --output /tmp/rechtsprechungsbestand.json
python3 scripts/audit-rechtsprechungsbestand.py --output /tmp/rechtsprechungsbestand-detail.json --include-files
```

Die technischen Abschlussprüfungen stehen in [pruefungen.json](pruefungen.json). Dateiscan, Hashvergleich und Strukturtests beweisen keine juristische Richtigkeit; die inhaltliche Evidenz steht ausschließlich in den oben verlinkten Einzelberichten.

## 1.4. Veröffentlichung

Dieser Durchgang aktualisiert die Fachquellen und daraus abgeleiteten Textfassungen im Repository. Er löscht keine Testakte und legt keine zusätzlichen Skills an. Ein vollständiger neuer Release sämtlicher Installations-ZIPs und Aktenpakete ist davon getrennt; aus einem Merge auf main folgt nicht, dass alte Release-Dateien neue Inhalte enthalten.
