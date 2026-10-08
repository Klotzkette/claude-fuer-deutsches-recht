# 1. Tatsächlicher Laufbericht zur Anwendungsprobe

Am 08.10.2026 wurde der neue Hauptskill `geldwaescheproblem-loesen` am begrenzten Fall `testakten/aml-notariat-kaufpreis-wuerzburg` angewendet. Der Arbeitsauftrag lautete, für die benannte Notarin die Originalunterlagen zu prüfen, einen nachvollziehbaren Zahlungsabgleich und einen vollständigen Schreibenentwurf zu erstellen sowie die heutige Möglichkeit der Eigentumsumschreibung zu beurteilen. Es war ausdrücklich keine Außenhandlung beauftragt.

## 1.1. Gelesene Arbeitsgrundlagen

Gelesen wurden `AGENTS.md`, `CLAUDE.md`, der Hauptskill sowie die Fachskills `verpflichtung-organisation-klaeren`, `immobilientransaktionen-pruefen`, `notarielle-vorgaenge-pruefen` und `verdachtsfaelle-meldungen-steuern`. Hinzu kamen die Pluginreferenzen `arbeitsweise.md`, `meldung-notariat-quellen.md` und `zitierweise.md`. PDF-, Dokumenten- und Tabellenlesehilfen des gebündelten Laufzeitsystems wurden ergänzend herangezogen.

Aus der Originalakte wurden folgende Dateien gelesen:

- `01_Belege/N-P01_Kaufvertrag_Auszug.pdf`
- `01_Belege/N-P02_Faelligkeitsmitteilung.pdf`
- `01_Belege/N-P03_Bankbeleg_Mutter.pdf`
- `01_Belege/N-P04_Bankbeleg_Darlehen.pdf`
- `01_Belege/N-P05_Quittungskopie.pdf`
- `01_Belege/N-P06_Brief_Verkaeufer.pdf`
- `01_Belege/N-P07_Erklaerung_Kaeuferin.pdf`
- `01_Belege/N-P08_Telefonnotizen.pdf`
- `02_Arbeitsunterlagen/N-D01_Arbeitsauftrag.docx`
- `02_Arbeitsunterlagen/N-D02_Entwurf_Nachforderung.docx`
- `02_Arbeitsunterlagen/N-D03_Offener_Pruefvermerk.docx`
- Nachgereicht als Ersatz und zusätzlich gelesen: `02_Arbeitsunterlagen/N-D03_Telefonnotiz.docx`.
- `02_Arbeitsunterlagen/N-D04_Entwurf_Erklaerung_Mutter.docx`
- Sämtliche zwölf EML-Dateien `N-E01_2026-09-25.eml` bis `N-E12_2026-10-08.eml` im Ordner `03_E-Mails`.
- `04_Tabellen/Fallregister.xlsx`, einschließlich der Blätter Übersicht, Zahlungen, Beteiligte und Verlauf.

Die acht PDF-Seiten wurden textuell und zusätzlich als gerenderte Bilder gelesen. Die vier DOCX wurden aus ihrem Dokumentinhalt gelesen; sie enthielten weder Kommentare noch Änderungsmarkierungen. Sämtliche E-Mail-Textkörper und Anhänge wurden zugeordnet. Die acht eingebetteten Beleganhänge stimmen bytegenau mit den Einzeldateien überein. Formeln und gespeicherte Ergebnisse der Arbeitsmappe wurden gelesen; die entscheidende Rechenbrücke wurde unabhängig anhand der Originalzellen nachvollzogen. Eine Excel-Neuberechnung oder grafische Excel-Prüfung wurde nicht durchgeführt und nicht behauptet.

Zur Lektüre wurde wie vorgegeben `/Users/klotzkette/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3` mit `PYTHONPATH=/tmp/kk338/pydeps` verwendet. Ein erster zu breiter `rg --files`-Aufruf lieferte unnötig viele Dateinamen aus dem Repository und wurde danach auf den Fall eingegrenzt. Dabei wurden keine Inhalte von Rubrics, Buildern, `scripts/data`-Dateien oder anderen Qualitätsberichten geöffnet. Erwartungen und Kontrollwerte wurden nicht gelesen. Der Bericht beschreibt das tatsächlich erzielte Ergebnis, keinen Abgleich mit unbekannten Bewertungskriterien.

## 1.2. Rechtliche Verifikation

Die tragenden aktuellen amtlichen Volltexte wurden während des Laufs geöffnet: §§ 2, 16a, 43, 46, 47 und 50 GwG, §§ 1, 6 und 7 GwGMeldV-Immobilien sowie § 3 GwGMeldV. Die amtliche Seite des Landgerichts Würzburg zur Geldwäscheaufsicht wurde ebenfalls gelesen. Eine parallel beauftragte, auf die genannten Normen begrenzte Gegenprüfung erhielt keine Repositoryunterlagen und lieferte ausschließlich Normabgrenzungen. Es wurde keine Rechtsprechung aus Modellwissen ergänzt. Die vollständigen URLs stehen im Entscheidungsvermerk.

## 1.3. Gelieferte Arbeitsprodukte und Ergebnis

Die Arbeitsprodukte der Probe entstanden unter `/tmp/aml-anwendungsprobe` und sind hier im Unterordner `anwendungsprobe-ergebnisse` unverändert archiviert:

| Datei | Tatsächlicher Inhalt |
| --- | --- |
| [Entscheidungsvermerk.txt](anwendungsprobe-ergebnisse/Entscheidungsvermerk.txt) | Der ausformulierte Vermerk beantwortet die heutige Vollzugsfrage, würdigt die gegensätzlichen Angaben, prüft die Meldegründe und enthält zusätzlich einen geschützten Sachverhaltsentwurf für die bei unverändertem Stand empfohlene Meldung. |
| [Zahlungsabgleich.csv](anwendungsprobe-ergebnisse/Zahlungsabgleich.csv) | Die vier Spalten trennen Vertragssoll, Bankabgänge, behauptete Eingänge, unbekannten unabhängigen Empfängernachweis, streitige Barbehauptung und geplante Restleistung. |
| [Schreiben.txt](anwendungsprobe-ergebnisse/Schreiben.txt) | Der Verkäuferbrief ist vollständig formuliert. Ergänzend liegen die Antwort an die Käuferin sowie das Anschreiben und der ausdrücklich erst zu prüfende Erklärungsentwurf für die Mutter vor. |

Die Rechenbrücke lautet 580.000,00 EUR minus 450.000,00 EUR minus 110.000,00 EUR gleich 20.000,00 EUR. Die 560.000,00 EUR sind Bankabgänge; ein unabhängiger Nachweis der Empfängerkontogutschriften fehlt. Dessen unbekannter Betrag wurde nicht als null behandelt. Die behaupteten 20.000,00 EUR wurden nicht als weitere belegte Leistung addiert. Das Ergebnis lautet, dass die Eigentumsumschreibung am 08.10.2026 auf dieser Grundlage nicht veranlasst werden kann.

Der Vermerk hält das Barzahlungsverbot von den Schwellen des typisierten Melderechts getrennt. Er berücksichtigt die Angehörigenausnahme für die Mutter, die Vorauszahlungsausnahme bis einschließlich 20.000,00 EUR, die absolute Nachweislückentoleranz von höchstens 10.000,00 EUR sowie die noch nicht erfolglos abgelaufene besondere Nachweisaufforderung. Der jetzige Meldevorschlag beruht auf der konkreten wiederholten Barzahlungsbehauptung mit Kopie und der noch nicht ausreichend gesicherten Entkräftung. Er stellt weder Barübergabe noch Straftat als bewiesen dar. Die Anforderung der Belege darf diese gesonderte unverzügliche Entscheidung nicht bis zum vorgeschlagenen 15.10.2026 verschieben.

Der unbestätigte Mutterentwurf wurde nicht als abgegebene Erklärung behandelt. Die Briefe nennen keine FIU-Meldung oder interne Meldeüberlegung. Die Nachforderung enthält einen konkreten Belegzeitraum, Wahrnehmungsfragen zur Quittung, Erhaltung des Originals und eine vorgeschlagene Vorlagefrist. Der 12.10.2026 bleibt von dieser als organisatorische Rückmeldung getrennt. Der Vermerk nennt die zugrunde gelegte zeitnahe Zustellung ausdrücklich als noch zu prüfende Voraussetzung.

## 1.4. Beobachtete Übergaben und Produktprobleme

Der Hauptskill führte in dieser Anwendung zum bestellten Ergebnis und nicht zu einer erneuten Mandatsaufnahme oder Abschlussfrage an die Nutzerin. Die Arbeit wurde nicht wegen fehlender allgemeiner Organisationsdaten oder wegen einer Versandfreigabe abgebrochen. Interne Bearbeitung und Außenhandlung blieben getrennt. Eine fehlende technische FIU-Schnittstelle wurde nicht als erfolgreicher Versand überspielt.

Beim tatsächlichen Lesen fiel ein konkreter fehlerhafter Verweis auf: `geldwaeschebeauftragter/skills/notarielle-vorgaenge-pruefen/SKILL.md`, Abschnitt 3.5, verwies für die Ausnahme bei nachlaufender Gegenleistung auf § 16a Abs. 5 Satz 2 GwG. Die vertragsgestaltungsbezogene Ausnahme steht im gelesenen amtlichen Volltext in Satz 3; Satz 2 betrifft die Nachweislücke bis 10.000,00 EUR. Der Fehler wurde an den übergeordneten Bearbeiter gemeldet. In diesem Fall ohne vereinbarte nachlaufende Fälligkeit beeinflusste er das Ergebnis nicht. Die Probe hat den Produkttext nicht geändert. Dieser Bericht bezieht sich auf die bei der Anwendung gelesene Fassung; spätere Korrekturen durch den Produktbearbeiter werden damit nicht vorweggenommen.

Die Produktnamen der Übergaben waren nicht vollständig einheitlich: Der Hauptskill nennt `rolle` und `notarvollzug`, während die Fachskills `verpflichtungsprofil` beziehungsweise `notarieller-pruefstand` verwenden. Da hier keine maschinell erzwungene Schnittstelle bestand, konnten die fachlichen Ergebnisse im Vermerk zusammengeführt werden. Eine verlorene fachliche Übergabe trat nicht ein.

Die Originalarbeitsmappe enthält zwei knappe Quellenzuordnungen, die für die Fallbearbeitung ergänzt werden mussten: `Verlauf!C10` nennt für beide Bankabgänge nur N-P03, obwohl N-P04 die Darlehenszahlung trägt. `Verlauf!A12:C12` verbindet den Käuferinnenwiderspruch mit N-E11 vom 08.10.; die tatsächlichen Quellen sind N-E06 vom 06.10. sowie N-E08/N-P07 vom 07.10. Diese Beobachtungen wurden im Ergebnis offengelegt. Die Quelldatei wurde nicht verändert. Es handelt sich um Befunde der Fallakte, nicht um durch den Skill verursachte neue Zahlungsfehler.

## 1.5. Tatsächliche Prüfung und Grenzen

Die CSV wurde erneut eingelesen: zwölf Zeilen einschließlich Kopfzeile, jeweils vier Spalten. Die Berechnung wurde mit den Originalzellen `Zahlungen!C7:C9` abgeglichen. Die getrennte Empfängerdatei wurde auf das Ausbleiben der Begriffe „FIU“ und „Verdachtsmeldung“ kontrolliert und inhaltlich hinsichtlich der Trennung von interner Meldungsentscheidung und sachlicher Nachforderung gelesen.

Die finalen Dateien dieser Fassung haben folgende SHA-256-Werte:

| Datei | SHA-256 |
| --- | --- |
| Entscheidungsvermerk.txt | `540b5af55acbc77ff628915dc948d88fe6beb7acbf2c193c1c9fcde6928f0e8a` |
| Zahlungsabgleich.csv | `f50ca7a1a5af6a2b1722cf3b7f16935ec15475db990eba600762a9eb9dc7e377` |
| Schreiben.txt | `37376e3b7d9d831bbf1f7b32762f9e3b006b282d1e615380fbba689231024e80` |

Es war kein Realmandat, keine Client-UI-Probe und kein Nachweis einer Installation oder automatischen Skillaktivierung. Es gab keine echte Anmeldung, FIU-Meldung, Bankabfrage, Registereinreichung, E-Mail, Unterschrift oder behördliche Rückmeldung. Die Akte enthält bewusst nur fiktive Daten und keinen prüfbaren Originalschriftzug. Eine technisch versandfertige Portalnachricht kann aus diesen fehlenden Echtdaten nicht behauptet werden. DOCX/PDF-Endfassungen und eine neue XLSX waren nicht beauftragt und wurden nicht erstellt. Die allgemeinen übrigen Vollzugsvoraussetzungen wurden wegen des begrenzten Vertragsauszugs nicht als erfüllt bestätigt. Die Probe umfasst nur diesen Fall und keinen Repositoryaudit.

## 1.6. Nachtrag zur während des Laufs nachgereichten Fassung

Der Produktbearbeiter ersetzte nach der ersten Probe den offenen Prüfvermerk N-D03 durch eine Telefonnotiz mit Gesprächsangaben. Die Probe hatte den vorherigen Prüfvermerk bereits gelesen; eine vollständig unbeeinflusste Wiederholung mit ausschließlich der neuen Notiz wird deshalb nicht behauptet. Die Ersatzdatei wurde gezielt gegengelesen. Eine erste Zwischenfassung enthielt unbeabsichtigt abweichende Angaben zu Fundort und Erkenntnisquelle des Verkäufers. Diese wurden gemeldet und durch den Aktenbearbeiter wieder an N-P06 angeglichen. Die Endprodukte enthalten die zwischenzeitlichen Abweichungen nicht als Tatsachen.

Die bestätigte Telefonnotiz hat SHA-256 `6a43f871f969e236ea4537b3628f6f3a6bb7634ce6e46e40ec1a332aa602f33b`. Sie hält Keksdose und behauptete selbst gesehene Bankgutschriften aufrecht, ergänzt den Banktermin am 09.10.2026 sowie die Ankündigung eines aktuellen Käuferinnenkontoauszugs und bestätigt den fortbestehenden Widerspruch. Diese Angaben wurden in Vermerk, Abgleich und Schreiben eingearbeitet. Rechenbrücke, heutiges Vollzugsergebnis und differenzierte Meldewägung ändern sich nicht.

Der Aktenbearbeiter korrigierte außerdem den Excel-Verlauf. Die neue gelesene Fassung trennt nun die Bankabgänge mit N-P03 und N-P04 sowie Käuferinnenwiderspruch am 07.10./N-E08 und Mutterangabe am 08.10./N-E11. Eine verbleibende Formulierung in `Verlauf!B13`, wonach bereits N-E08 Kontobelege ankündige, wurde ebenfalls gemeldet und vor Abschluss berichtigt. Beim abschließenden Gegenlesen lautete B13 nur noch „Käuferin bekräftigt ihren Widerspruch gegen eine Barzahlung.“ Die Ankündigung des eigenen Auszugs ist erst durch N-D03 vom 08.10. belegt und im Entscheidungsvermerk so zugeordnet. Der vorherige Befund in Abschnitt 1.4 bleibt als tatsächliche Laufhistorie erhalten.

Der Produktbearbeiter teilte zudem die Korrektur des Satzverweises auf § 16a Abs. 5 Satz 3 und die Vereinheitlichung der Produktkennungen mit. Diese Änderungen sind Produktpflege nach dem beobachteten Erstlauf. Die Probe selbst hat weder Skilltexte noch Aktenbestand verändert. Die endgültigen Textprodukte sind Fassung 1.1; die oben aufgeführten Hashes beziehen sich auf diese nachgeführte Fassung.
