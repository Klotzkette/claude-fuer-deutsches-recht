# 1 Hochrisiko-Fachrunde vom 9. Oktober 2026

## 1.1 Ergebnis und Fachkorrekturen

Das bestehende Plugin hat jetzt zehn Fachskills und einen elften Hauptproblem-Skill. Alle neun vorhandenen Skills bleiben unter ihren bisherigen Kennungen erhalten. Der Artikel-6-Skill führt ausschließlich die Einstufung durch. Der zusätzliche Produktpfad-Skill vertieft die kumulativen Voraussetzungen, während der Hauptproblem-Skill Unterlagen, Rückfragen und ausformulierte Ergebnisdokumente zusammenführt.

Der amtliche konsolidierte Wortlaut vom 27. Juli 2026 sowie die deutsche Berichtigung vom 29. September 2026 wurden geöffnet und gelesen. Artikel 6 Absatz 1b wird nun ungeachtet des Absatzes 1a geprüft. Bloße Komfortbezeichnungen und menschliches Unterschreiben beseitigen gefährliche Ausfallfolgen nicht. Absatz 3 bleibt auf den Anhang-III-Pfad beschränkt; sämtliche vier Alternativen, der Risikokontext und die Profiling-Sperre werden konkret geprüft. Die neue Zuordnung der Maschinenverordnung zu Anhang I Abschnitt B Nummer 21 ist berücksichtigt. Artikel 6 Absatz 4 und Artikel 49 Absatz 2 bleiben erhalten.

Die Überarbeitung trennt systembezogenes Risikomanagement nach Artikel 9, Anbieter-QMS nach Artikel 17, FRIA nach Artikel 27 und technische beziehungsweise betriebliche Aufsicht. Zertifikate, ISO-Normen, allgemeine Governance-Listen und GPAI-FLOPs werden nicht als Ersatz für den jeweiligen Systemtatbestand behandelt. Artikel 111/113 wird mit den jeweils betroffenen Folgeartikeln verknüpft; keine pauschale Verschiebung sämtlicher Pflichten.

## 1.2 Quellen und Reichweite

Gelesener Kern: [amtliche Konsolidierung](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727), insbesondere Artikel 2, 3, 6, 25 bis 27, 43, 49, 111/113, Anhang I und alle Untertatbestände des Anhangs III. [Deutsche Berichtigung](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32026R1744R%2801%29): ungeachtet in Artikel 6 Absatz 1b. Amtliche Quellenkopien und Prüfsummen liegen im [zentralen Quellenverzeichnis](../quellen/). Die Konsolidierung hat keine eigene Rechtswirkung.

Für den Produktfall wurden Artikel 51/52 und Anhang VIII Regel 11 der [amtlichen MDR-Lesefassung vom 10. Januar 2025](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02017R0745-20250110) geöffnet und gelesen. Das ist keine vollständige Nachprüfung der MDR-Fassung 2026. Die Klassifizierung bleibt im Fall ausdrücklich eine Herstellerarbeitshypothese; aktuelles Produktrecht und Bewertungsweg sind gezielt nachzufordern.

Der vorhandene EuGH-Anker C-634/21 bleibt mit dem dokumentierten früheren Lesestand vom 28. September 2026 und seiner Beschränkung auf Artikel 22 DSGVO erhalten. Der erneute Volltextabruf erreichte die maßgeblichen Randnummern wegen Botabwehr nicht. Es wird keine neue Volltextlesung oder Rechtsprechung zu Artikel 6 behauptet. Diese Grenze ist im [ergänzenden Leseprotokoll](../quellen/hochrisiko-quellen.json) und im Prüfprofil ausdrücklich dokumentiert.

## 1.3 Textumfang und Konsistenz

Alle Skills haben Frontmatter mit genau name und description, eine Beschreibung von höchstens 360 Zeichen sowie sechs Hauptabschnitte. Die Links innerhalb der Laufzeittexte bleiben im Plugin. Die neue Workflow-Referenz benennt elf Skills, konkrete Produkte und Rückgaben. Die drei MD/TXT-Paare sind byteidentisch. Hashes einschließlich des neuen Hauptproblem-Skills stehen im Prüfprofil. Die folgenden Wortzahlen betreffen den Textkörper ohne Frontmatter; sie sind Umfangsangaben, kein fachlicher Qualitätsbeweis.

| Skill | Wörter vorher | Wörter nachher |
| --- | --- | --- |
| artikel-6-software-einstufen | 476 | 1019 |
| ausnahmebegruendung-artikel-6 | 442 | 690 |
| betreiberkonzept-bewerbungsauswahl | 564 | 686 |
| hochrisiko-einstufung-recruiting | 439 | 556 |
| hochrisikofrage-loesen | neu | 900 |
| hr-zweck-und-systemabgrenzung | 482 | 599 |
| konformitaet-und-registrierung | 460 | 589 |
| produktpfad-sicherheitsbauteil-pruefen | neu | 893 |
| rechtsstand-und-einfuehrungsentscheidung | 470 | 590 |
| rollenwechsel-und-shadow-ai | 491 | 614 |
| vorfallbewertung-und-meldeentwurf | 464 | 569 |

| Prompt | UTF-8-Bytes |
| --- | --- |
| schnellstart | 7392 |
| hauptproblem | 7497 |
| werkstatt | 43218 |

## 1.4 Native Testakten und Dateiprüfung

Die zwei neuen Fälle Jena und Saalfeld bestehen jeweils aus zwölf Originaldateien: vier E-Mails, drei DOCX, drei PDF, eine XLSX mit zwei Arbeitsblättern und ein TXT-Chat. Insgesamt wurden 24 native Dateien, acht E-Mails und vier tatsächlich eingebettete Anhänge geprüft. Jeder Anhang ist byteidentisch mit seiner separaten Originaldatei. Absender, Empfänger, Datum und Message-ID sind vorhanden; sämtliche E-Mail-Domains sind reservierte .example-Adressen. Die ursprüngliche Kasseler Recruitingakte wurde nicht verändert.

Die sechs Word-Dateien wurden mit LibreOffice gerendert und sämtliche sechs Seiten angesehen. Die sechs Original-PDF-Seiten wurden gerendert und angesehen; der Text jeder Quellpassage wurde mit der PDF-Textschicht verglichen. Times New Roman 11 pt ist in den Word-Normalstilen gesetzt und für die PDF-Texte eingebettet. Beide Arbeitsmappen wurden mit dem Artifact-Tool erstellt und ihre vier Blattansichten angesehen. Zusätzlich wurde jede XLSX nativ mit LibreOffice als PDF gerendert: zwei A4-Querformatseiten je Mappe, kleinste native Schrift rund 10 pt. Keine abgeschnittenen oder überlaufenden Inhalte wurden festgestellt.

Die 16 Formelzellen berechnen Testquotienten und Angebote. Vierzehn Rechenproben umfassen Ausgangswerte, Mengenänderung, Nullmenge, Nullumsatzsteuer und leere Testgruppe. Die Ursprungswerte wurden vor dem Export wiederhergestellt. Jena: 9.030,00 Euro netto und 10.745,70 Euro brutto. Saalfeld: 9.660,00 Euro netto und 11.495,40 Euro brutto. Angebote sind in den Unterlagen ausdrücklich keine fälligen Rechnungen. Ein Nullwert bei leerer Testgruppe wird als Rechenkonvention erläutert, nicht als bestandener Test.

[Dateinachweis mit Originalhashes, MIME-Prüfung und Rechenproben](native-pruefung.json). Die Fallkriterien liegen getrennt im Prüfprofil; die Nutzerakten enthalten keine Musterlösung. Offene Tatsachen im Arbeitsentwurf werden nicht als bereits geklärt ausgegeben.

## 1.5 Ausgeführte Prüfungen

`python3 scripts/test-ki-verordnung-hochrisiko-pruefer.py`: 15 Tests, grün; ein optionaler Renderabgleich der alten Kasseler Akte wurde mangels erneut aufgebautem altem QA-Verzeichnis übersprungen. Alle übrigen bestehenden Regressionen einschließlich unverändertem Kasseler Dateibestand liefen durch. Der neue native Nachtrag wurde zusätzlich wie vorstehend tatsächlich gerendert, rechnerisch geprüft und visuell kontrolliert. Diese Ergebnisse dürfen nicht als übersprungene neue Fallprüfung missverstanden werden.

Globale Marketplace-, Navigations-, Release- und PDF-Gesamtprüfungen gehören zur anschließenden gemeinsamen Integration. Die Qualitätsprofile enthalten neue konkrete Arbeitsaufträge für Jena und Saalfeld, aber keinen behaupteten Live-Modelllauf. Eine tatsächliche Client-Ausführung in Cowork, Codex oder ChatGPT wurde in dieser Teilrunde nicht durchgeführt.

## 1.6 Paketnachlauf

Die beiden offenen Word-Arbeitsentwürfe heißen `10_Stellungnahme_Arbeitsentwurf.docx`. Die Umbenennung vermeidet den Ausschluss durch den allgemeinen Filter für Prüf- und Lösungsvermerke; der Nutzer hatte diese offenen Entwürfe ausdrücklich als Fallmaterial bestellt. Die Inhaltsbytes und SHA-256-Werte sind unverändert. Je Fall bleiben zwölf Originaldateien einschließlich dieses Arbeitsentwurfs für den zentralen Export vorgesehen. Der allgemeine Exportfilter wurde nicht verändert.
