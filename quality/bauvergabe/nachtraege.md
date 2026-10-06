# 1. Nachtragsmanagement – Erstellung und Eigenprüfung

Prüfdatum: 06.10.2026. Geprüfter Bereich: `bauvergabe/bauvergabe-nachtragsmanagement/` sowie `quality/evals/bauvergabe-nachtragsmanagement.json`. Das Plugin wurde mit dem offiziellen Plugin-Creator scaffoldiert; eine persönliche Marketplace-Datei wurde nicht angelegt oder verändert. Es wurden keine Git-Mutationen, globalen Generatoren oder Release-Schritte ausgeführt.

## 1.1 Umfang

Das Plugin enthält genau zehn Fachskills und einen eigenständig nutzbaren Hauptskill. Jeder Skill besitzt die vorgeschriebenen sechs nummerierten Blöcke, ein Frontmatter nur mit Name und Beschreibung, lokale Quellenverweise und den Ausgabeformatblock mit Ausformulierungspflicht, Times New Roman 11 pt und dezimaler Gliederung. Die Manifeste für Claude und Codex tragen Version 445.32.0. Der Hauptskill benötigt keine Werkstattdatei und keine Repository-Wurzel.

Der Werkstatt-Megaprompt umfasst 49.300 Unicode-Zeichen beziehungsweise 50.134 UTF-8-Bytes. Der Mini-Megaprompt umfasst 7.352 Unicode-Zeichen beziehungsweise 7.483 UTF-8-Bytes und bleibt damit unter 7.500 Bytes sowie unter 8.000 Zeichen. Die jeweilige Markdown- und Textfassung ist byteidentisch.

## 1.2 Sachliche Prüfentscheidungen

Die Vertragsbaseline geht der Preisrechnung voraus. BGB-Paragrafen 650b und 650c werden nicht mit Paragraf 2 Absatz 3, 5, 6 oder 8 VOB/B vermischt. VOB/B-Einbeziehung und konkrete Klauselwirksamkeit werden eigenständig geprüft. Technische Freigabe, rechtsgeschäftliche Anordnung, Vertretungsmacht, Mengenbestätigung und Preisvereinbarung bleiben verschiedene Feststellungen.

Bei reinen Mengenmehrungen gilt der neue Preis nur für die Teilmenge oberhalb von 110 Prozent des ursprünglichen Ansatzes; Mindermengen und Pauschalsummen werden gesondert behandelt. Der BGH-Ansatz tatsächlich erforderlicher Kosten für Mehrmengen wird nicht ohne Begründung auf alle Änderungs- und Zusatzleistungen übertragen. Die Korrektur zu Baustellengemeinkosten aus VII ZR 10/19 ist in Skills, beiden Prompts und Quellenreferenz berücksichtigt.

Fristverlängerung, Vergütungsanpassung, Entschädigung und Schadensersatz sind getrennt. Bauzeitforderungen benötigen Ereignis, Ressource, Zeitraum und Kausalität; Eigenstörungen, Zeitspielräume und alternative Ausführung werden geprüft. Die Grenze des Paragrafen 642 BGB für spätere Lohn- und Materialsteigerungen ist ausdrücklich enthalten. Arbeitseinstellung und Paragraf 650d BGB werden nicht als automatische Folgen einer streitigen Rechnung behandelt.

Die Prüfung nach Paragraf 132 GWB bleibt von der wirtschaftlichen Nachtragsberechtigung getrennt. Die 50-Prozent-Grenze für Absatz 2 Nummer 2 und 3, die kumulierte 15-Prozent-Grenze für Bauaufträge unter Absatz 3, Schwellenwert, Gesamtcharakter, Indexierung und Bekanntmachung nach Absatz 5 sind differenziert beschrieben. Es gibt keine pauschale Rückforderungsquote. Eine kommunale gGmbH wird bei Paragraf 650f BGB nicht automatisch wie eine insolvenzunfähige juristische Person des öffentlichen Rechts behandelt.

# 2. Quellenprüfung

## 2.1 Amtliche Normen

Geöffnet wurden insbesondere Paragrafen 132 GWB, 650b, 650c, 650d, 650f, 650g, 310, 640, 641 und 650a BGB sowie die amtliche VOB/B Ausgabe 2016. Paragraf 642 und die BGB-Änderungsnormen wurden ergänzend per HTTP-Abruf im Originaltext gelesen. Die zentrale konkrete Quellenreferenz liegt im Plugin unter `references/quellen-und-rechtsprechung.md`; die verbindliche Zitierweise ist als lokale Kopie enthalten.

Die aktuelle amtliche Fassung des Paragrafen 132 GWB wurde am 06.10.2026 geöffnet. Ihre Absatzstruktur und die beschriebenen Wert- und Bekanntmachungsregeln wurden unmittelbar am Normtext geprüft. Die VOB/B wurde auf `verwaltungsvorschriften-im-internet.de/bsvwvbund_26062012_B15816361.htm` im Volltext gelesen; ihre Anwendung als Vertragsbedingungenwerk wurde nicht mit der VOB/A-Fassung verwechselt.

## 2.2 Entscheidungen und tatsächlicher Verifikationsweg

| Entscheidung | Geprüfte Stelle und Aussage | Grenze |
|---|---|---|
| BGH, Urt. v. 08.08.2019 – Az. VII ZR 34/18 | Amtliches PDF, Rn. 17–20 und 27–29: Vorrang einer Preisabrede und tatsächlich erforderliche Kosten bei reinen Mehrmengen. | Keine pauschale Gleichsetzung mit Paragraf 2 Absatz 5 oder 6 VOB/B. |
| BGH, Urt. v. 21.11.2019 – Az. VII ZR 10/19 | Amtliches PDF, Rn. 15 und 21–24: Voraussetzungen des Preisverlangens sowie BGK-/AGK-Klarstellung. | Keine Abschaffung konkret erforderlicher Baustellenkosten; keine automatische Angemessenheit des kalkulierten Zuschlags. |
| BGH, Versäumnisurt. v. 26.10.2017 – Az. VII ZR 16/17 | Amtliches PDF, Rn. 18–21 und 25–28: zeitliche Grenze der Entschädigung nach Paragraf 642 BGB. | Andere Anspruchsgrundlagen werden nicht ausgeschlossen; Anspruchsvoraussetzungen bleiben zu prüfen. |
| EuGH, Urt. v. 19.06.2008 – Az. C-454/06, pressetext Nachrichtenagentur | Amtlicher EUR-Lex-Volltext, Rn. 34–37: wesentliche Änderungen und Wettbewerb. | Ausgangsfall nach alter Richtlinie; aktuelle Ausnahmen eigenständig prüfen. |
| EuGH, Urt. v. 07.09.2016 – Az. C-549/14, Finn Frogne | Amtlicher EUR-Lex-Volltext, Rn. 28–32 und 36–40: Vergleich, Reduzierung und Änderung. | Kein Verbot jedes Vergleichs; kein Ersatz für Paragraf 132 GWB. |

Die alten `juris.bundesgerichtshof.de`-Adressen leiteten beim unmittelbaren HTTP-Abruf zur Entscheidungsstartseite um. Die neuen SharedDocs-PDF-Adressen wurden erfolgreich per Python-HTTP abgerufen und mit `pdftotext -layout` gelesen; es handelt sich um echte PDF-Dateien. Gericht, Entscheidungsform, Datum, Aktenzeichen und die oben genannten Randnummern wurden am Volltext geprüft. Der Jahresordner für VII ZR 34/18 lautet 2018; das Datum im PDF lautet 08.08.2019. Der versuchte Jahresordner 2019 lieferte 404 und wird nicht zitiert. Suchtreffer dienten nur dem Auffinden. Keine Literaturstellen oder angeblichen Entscheidungen aus 2026 wurden zur Aktualitätserzeugung ergänzt.

# 3. Validierung und rechnerischer Abgleich

Der offizielle `validate_plugin.py` lief erfolgreich. Der offizielle `quick_validate.py` lief für alle elf Skills mit Exitcode 0. Die zusätzliche strukturbezogene Kontrolle bestätigte sechs nummerierte Blöcke pro Skill, 32 gültige lokale Skillverweise, elf Evaluationsfälle für elf unterschiedliche Zielskills, byteidentische Promptpaare und die Übereinstimmung der SHA-256-Werte im Evaluationsprofil mit den tatsächlichen Promptdateien.

Die Rechenkontrollen ergaben für die Klinik bei ursprünglichen Vertragspreisen 220 × 260 + 34.000 × 2,45 + 920 × 74 = 208.580 EUR netto. Der Vergleichswert beträgt 2,6661724103 Prozent des ursprünglichen Rohbauauftrags von 7.823.200 EUR netto. Für das Wohnhaus ergeben 140 × 180 + 44 × 250 + 8.000 × 2,40 = 55.400 EUR netto und 3,1200369448 Prozent des Auftrags von 1.775.620 EUR netto. Beide Werte sind im Prompt ausdrücklich Vergleichswerte, keine automatisch geschuldete Nachtragshöhe.

Die später bereitgestellten N01-Angebotstexte rechnen mit abweichenden direkten Kostenansätzen: Klinik 216.400 EUR netto und Wohnhaus 57.188 EUR netto vor beantragten Zuschlägen. Das widerspricht den ausdrücklich als Altpreisvergleich gekennzeichneten Promptwerten nicht. Die technische Anordnung vom 05.03.2027, Preisoffenheit und streitige Bauzeit sind mit dem Plugin konsistent. Im Anordnungsmailtext wurde der Schreibfehler „Sehrhrte“ an die Integration gemeldet; eine Änderung der fremd verantworteten Quelldatei wurde nicht vorgenommen.

# 4. Evaluationsstatus und Grenzen

Das Profil enthält elf konkrete Szenarien mit erwartbaren Dokumenten und jeweils drei sachlichen Bewertungskriterien. Es umfasst unter anderem fehlende Vollmacht, BGK-Doppelansatz, reine Leitplankenmehrmenge, spätere Preissteigerung nach Annahmeverzug, Prüffähigkeitsfiktion, kommunale gGmbH, widersprüchlichen Zeitvorbehalt und falschen Prozentnenner. Das sind redaktionelle Prüfspezifikationen. Es wurden keine Modellläufe ausgeführt oder als beobachtet behauptet.

Die Validierung beweist Struktur, lokale Verweise, Dateigleichheit und ausgewählte Recheninvarianten. Sie ersetzt keine unabhängige fachliche Prüfung und keine Erprobung an vollständigen Mandatsunterlagen. Die beiden Lebensakten und ihre Downloads werden durch die Integration erzeugt; ihre Root-README-Verweise sind Repository-Komfortlinks und keine Laufzeitabhängigkeit des installierten Plugins. Es wurden in diesem Teilauftrag keine DOCX- oder PDF-Dateien erzeugt.

# 5. Nachfolgender Tabellenauftrag

Für beide Lebensakten wurden zusätzlich `03-bieterarbeit/02_Angebotskalkulation.xlsx` und `05-nachtragsmanagement/06_Nachtragskosten.xlsx` erstellt. Autor ist ausschließlich die gebündelte Bibliothek `@oai/artifact-tool`; der reproduzierbare Builder liegt unter `scripts/build-bauvergabe-tabellen.mjs`. Die Python-Spezifikation unter `/tmp/bauvergabe-20261006/tabellen-spec.json` übernimmt die 16 LV-Positionen, Mengen und eigenen Preise aus `scripts/bauvergabe_falldaten.py`. Die N01-Ansätze stammen aus Abschnitt 2 des Nachtragsangebots in `scripts/bauvergabe_aktentexte.py`. Keine konkurrierenden Angebotspreise sind enthalten. Die Angebote tragen den 22. beziehungsweise 29. November 2026; die Nachträge kennzeichnen den 10. März 2027 ausdrücklich als Kalkulationsstand.

Die Formeln ergeben 7.823.200,00 EUR beziehungsweise 1.775.620,00 EUR Angebotsnetto und 9.309.608,00 EUR beziehungsweise 2.112.987,80 EUR brutto. Im Nachtrag werden 216.400,00 EUR beziehungsweise 57.188,00 EUR direkte Kosten um 8 Prozent AGK und 5 Prozent Wagnis/Gewinn ergänzt; beide Zuschläge beziehen sich additiv auf direkte Kosten. Daraus folgen 244.532,00 EUR beziehungsweise 64.622,44 EUR beanspruchtes Netto und 290.993,08 EUR beziehungsweise 76.900,70 EUR brutto. Anerkennung, Vereinbarung der Zuschläge und Vergütung der Bauzeit werden nicht unterstellt.

Alle vier Dateien bestehen aus jeweils einem Blatt, enthalten aktive Formeln und editierbare farblich bezeichnete Eingaben und besitzen keine externen Workbook-Verknüpfungen. Die belegten OZ bleiben als fünfstellige Textwerte erhalten. Sämtliche befüllten Zellen sind Times New Roman 11 pt. Ein fehlender Zahlenwert führt zu `n.a.` in Positionsbetrag und Gesamtsummen; eine echte Null wird berechnet. Pro Datei wurden eine normale Mengenänderung, eine leere Menge und Menge null getestet, insgesamt zwölf Mutationen. Sowohl der Artefakt-Rechenkern als auch das gebündelte native LibreOffice ergaben die separat berechneten Sollwerte; sämtliche Originalsummen, Mehrkosten-Zuschlagsbasen, Formeltypen und Fehlerzellen wurden kontrolliert. Openpyxl und XML wurden ausschließlich lesend verwendet.

Alle vier letzten Blatt-PNGs und alle sechs Seiten des nativen PDF-Drucks wurden visuell geöffnet. Die beiden Angebote drucken auf je zwei Seiten, beide Nachträge auf je eine Seite. Zu schmale Zahlenfelder wurden nach dem ersten nativen Druck verbreitert; die abschließende Kontrolle fand weder `###` noch abgeschnittene Beschreibungen oder Überschriften. Die Artefakt-PNG-Vorschau stellt führende OZ-Nullen trotz Textformat verkürzt dar; die gespeicherten XLSX-Textwerte und der native Druck enthalten sie korrekt. Die Druck-PDFs sind ausschließlich QA-Zwischenstände, keine zusätzlichen Lieferdateien.

Es lief ausschließlich die gebündelte LibreOffice-Version unter `dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/MacOS/soffice` mit separatem temporären Profil. Die native Neuberechnung erfolgte an Wegwerfkopien. Nachweise stehen unter `/tmp/bauvergabe-20261006/tabellen/verification.json` und `verification.log`; die vier ausgelieferten XLSX blieben Artefakt-Exporte. Der Artefakt-Marker wurde für vier Ausgaben genau einmal ausgeführt.

Nach dem Integrationshinweis wurden die internen Testakten-Kennzeichnungen aus den Tabellen entfernt. Die Angebotsblätter verweisen nun auf die mitgelieferte `01-vergabeunterlagen/07_Mengen_Preisblatt.csv` für OZ und Mengen sowie auf eigene editierbare Kalkulationsansätze. Die Nachtragsblätter nennen `05-nachtragsmanagement/04_Aufmass_N01.csv` und das native Nachtragsangebot. Diese Quellen existieren in der Fallakte; die Arbeitsmappen sind nicht von der Python-Stammdatendatei abhängig. Danach wurden alle vier Dateien erneut exportiert, alle zwölf Mutationen in beiden Rechenkernen wiederholt und alle vier letzten Blattbilder sowie alle sechs letzten nativen Druckseiten erneut geöffnet. Die finalen SHA-256-Werte stehen in `delivery-evidence.json` im selben QA-Verzeichnis.
