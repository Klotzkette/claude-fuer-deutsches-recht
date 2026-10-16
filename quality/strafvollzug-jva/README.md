# Strafvollzug in der JVA: Prüfbericht

## 1. Umfang und Abgrenzung

Prüfstand 16.10.2026, Komponentenfassung 1.0.0. Zehn Fachskills und ein Hauptskill, fünf Befehle, drei eigenständige Prompts und vier vollständige Übungsakten für Erwachsenenstrafhaft. Die Perspektiven Gefangene, anwaltliche Vertretung, Anstalt und Gericht werden ausdrücklich getrennt.

Die vertiefte Landesprüfung betrifft fallrelevante Normen in Berlin, Nordrhein-Westfalen, Bayern und Niedersachsen. Für die übrigen Länder enthält der Wegweiser amtliche Rechercheeinstiege. Eine umfassende Prüfung sämtlicher Landesnormen und aller vollzugsrechtlichen Entscheidungen ist nicht behauptet.

## 2. Primärquellen und fachliche Korrekturen

Die [Bundesreferenz](../../strafvollzug-jva/references/bundesrecht-rechtsschutz.md) und die [Entscheidungsreferenz](../../strafvollzug-jva/references/rechtsprechung.md) dokumentieren tatsächliche Volltextlektüre und gelesene Randnummern. [Abrufhashes](bundesquellen-abruf.json) sichern die abgerufenen Bundesquellen. Suchauszüge werden nicht als gelesener Volltext behandelt.

- Berlin: zusätzliche Kinderbesuchszeit seit 25.06.2026 zwei Stunden; frühe Fassungen nennen noch eine. Inkrafttreten der einzelnen Reformteile getrennt geprüft. Keine allgemeine Rechtsbehelfsbelehrungspflicht nach § 98a behauptet.
- Bayern und NRW: aktuelle Vergütungsregeln nicht aus dem Verfassungsgerichtsurteil von 2023 fortgeschrieben. Unterschiede bei Arbeitszeit und Stufensystem beachtet.
- Niedersachsen: amtlicher VORIS-Text tatsächlich abgerufen, fallrelevante Vorschriften gelesen. Die dort weiterhin genannte Vergütung nicht automatisch an Bayern oder NRW angeglichen.
- Rechtsschutz: Zweiwochenfrist nach schriftlicher Bekanntgabe, Unterlassen, Eilverfahren und Rechtsbeschwerde getrennt. Keine automatische Fristwahrung durch interne Beschwerde. Die alte landesrechtliche Vorverfahrenslage nicht ungeprüft fortgeschrieben.
- Sachprüfung: kein pauschaler Laptopanspruch, keine allgemeine Haftraum-Flächenfreigrenze und keine stereotype Gefahrenbewertung aus Herkunft, Religion oder Geschlecht.

Sechs Entscheidungen wurden mit konkreter Tragweite und ausdrücklich benannter Grenze erfasst, darunter Entscheidungen aus 2024 und 2025. Eine passende Entscheidung aus 2026 wurde nicht erfunden. Der Sonderfall der Entscheidung aus 2025 wird nicht als allgemeine medizinische Anspruchsregel verwendet.

## 3. Vier Testakten

64 Originaldateien: je vier Word-Dokumente, sechs PDFs, fünf E-Mails und eine Excel-Arbeitsmappe. Die vier gerichtlichen Parteientwürfe enthalten konkrete Begehren, Tatsachen, rechtliche Begründung und Anlagenzuordnung A1 bis A8. Die fiktiven Einrichtungen werden nicht als echte Behörden dargestellt. Tatsächliche Gerichtsübermittlung findet nicht statt.

Der Aktenbericht dokumentiert die native Dokument- und Tabellenprüfung. Das Gesamt-PDF wird aus genau den veröffentlichten Einzel-PDF-Seiten zusammengesetzt. Die Originaldateien bleiben im ZIP byteidentisch; E-Mail-Anhänge werden mit ihren zugrunde liegenden Dateien abgeglichen.

## 4. Standalone-Prompts

Werkstatt mit 24 Kapiteln und konkreten Länder- und Entscheidungsankern. Mini und Hauptproblem bleiben unter 7.500 UTF-8-Bytes; MD und TXT sind byteidentisch. Hashes im [Prüfprofil](../evals/strafvollzug-jva.json) halten den tatsächlich geprüften Stand fest. Das Profil enthält fünf konkrete Szenarien mit 21 Kriterien. Eine redaktionelle Prüfung wird nicht als beobachteter Modelllauf ausgegeben.

## 5. Anwendungsprobe und technische Prüfung

Die abschließende Paketprüfung hat **10 von 10 Tests bestanden**; siehe [Protokoll](paket-tests.txt). Geprüft wurden 24 Release-Dateien, 23 SHA-256-Summen, beide Plugin-ZIPs gegen die aktuellen Quellen, alle 64 Originaldateien, 20 eindeutige E-Mails mit acht bytegleichen Anhängen, zwölf Excel-Blätter mit echten Datumszellen und Formel-Caches sowie der exakte Seiteninhalt zwischen Einzel- und Gesamt-PDFs.

Die vier Gesamtakten haben 20, 20, 19 und 20 Seiten, zusammen 79 Seiten. Die Werkstatt umfasst zehn Seiten, die beiden kompakten Prompts je zwei. [Umfang und Hashes](umfang.json) dokumentieren den genauen Stand. Alle Promptseiten wurden visuell kontrolliert; Word-, Original-PDF- und Tabellenprüfung steht im [Aktenbericht](akten-pruefung.json).

Zwei tatsächliche PDF-Extraktionsprobleme wurden im lokalen Test korrigiert: Poppler berücksichtigt die in nativen Excel-PDFs enthaltene ActualText-Markierung, während andere Extraktoren dabei einzelne Ligaturen verdoppeln. Lange URLs werden in den Prompt-PDFs zeichengetreu unter Bereinigung reiner Layoutumbrüche geprüft; der übrige Text bleibt im strengen Wortvergleich. Negativproben sichern die Erkennung wirklichen Inhaltsverlusts. Weder Produktinhalte noch globale Validatoren wurden für diese Korrektur abgeschwächt.

Bestandene Prüfungen:

- `claude plugin validate strafvollzug-jva --strict`
- `python3 scripts/test-strafvollzug-jva.py --dist /tmp/jva-release-final`
- `node scripts/validate-plugin-structure.mjs`
- `node scripts/validate-marketplace-import.mjs`
- `python3 scripts/validate-yaml-frontmatter.py`
- `python3 scripts/audit-skill-activation.py`
- `python3 scripts/validate-markdown-structure.py`
- `python3 scripts/validate-root-readme-overview.py`
- `python3 scripts/validate-testakten-readme-downloads.py`
- `python3 scripts/test-scoped-release-routing.py` mit elf Tests
- `python3 scripts/quality-lab.py audit --require-editorial --require-workflow`

Der globale Bestand umfasst 301 Plugins und 23.289 Skills. Alle 1.036 bisherigen Akten-ZIP-Ziele bleiben erhalten; die vier neuen Akten und zwei neuen Pluginpakete erhalten eigene Komponentenziele. Die [textuelle Anwendungsprobe](anwendungsprobe/Leseprotokoll.md) wurde nach einer Unterbrechung anhand des vorgefundenen Entwurfs abgeschlossen und gegengeprüft. Sie ist deshalb ausdrücklich keine rekonstruierte vollständige Blindprobe. Der [Gerichtsantrag](anwendungsprobe/Antrag.md) und die [Frist- und Eilnotiz](anwendungsprobe/Fristnotiz-und-Eilpruefung.md) liefern vollständige interne Arbeitsprodukte. Die Fristberechnung ergibt bei den vorgegebenen Annahmen den 19.10.2026. Der unmittelbare Nutzungsantrag bleibt schwächer belegt als Neubescheidung: Sicherheitsbefund, Nachholbarkeit des Kurses, tatsächliche Anstalt und Originalbelege sind offen. Hilfsantrag und Vorwegnahmeprüfung wurden in der Probe präzisiert. Es fand keine Außenhandlung und kein beobachteter Import in eine Endnutzer-App statt.

## 6. Veröffentlichung

Eigenständiges Komponentenrelease mit 24 Dateien. Die Gesamtversion 445.35.3 und alle früher veröffentlichten Archive bleiben unverändert. Paketinhalt, Prüfsummen und Downloadziele werden vor der Veröffentlichung abgeglichen. Ein echter Import in Claude Cowork, Codex oder ChatGPT wird nicht als getestet behauptet.
