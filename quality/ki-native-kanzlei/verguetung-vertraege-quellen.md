# 1. Quellenprüfung für Vergütung, Abrechnung und Verträge

Prüfstand: 7. Oktober 2026. Gegenstand sind ausschließlich die sechs Skills `honorar-budget-vereinbaren`, `zeiten-erfassen`, `abrechnung-e-rechnung`, `zahlungen-buchhaltung`, `vertraege-agb-pruefen` und `vertraege-gestalten`. Dieses Protokoll dokumentiert die tatsächlich verwendeten Rechercheanker, ihre Grenzen und den Abgleich mit den vorhandenen lokalen Werkzeugen. Es ist keine individuelle Vertragsfreigabe und keine Behauptung, jeder künftige Mandatsfall sei bereits abschließend geprüft.

## 1.1. Methode und Abrufgrenzen

Die vorhandenen Repository-Regeln, die Rechtsquellenreferenz und die vollständigen Schnittstellen von `scripts/kanzlei.py` und `scripts/xrechnung.py` wurden gelesen. Amtliche BGH-PDFs wurden direkt aus dem SharedDocs-Angebot heruntergeladen, mit `pdftotext` erschlossen und die verwendeten Passagen kontrolliert. Der Webabruf einzelner BGH-Adressen gab 403 zurück; derselbe amtliche Direktabruf über die lokale Python-Laufzeit lieferte echte PDFs. Ein Zugriffsschutztext wurde nicht als Entscheidung behandelt. Die temporären Recherchedateien liegen unter `/tmp/ki-honorar-recherche`; sie sind kein Bestandteil des ausgelieferten Plugins.

Für BFH-Entscheidungen wurden amtliche HTML-Seiten und, zur zuverlässigen Randnummernkontrolle, amtliche PDFs gelesen. Dabei wurde eine wichtige Abweichung zwischen nummerierten Webabschnitten und echten Entscheidungsrandnummern korrigiert: VIII R 14/17 wird mit Rn. 20–32 zitiert, nicht mit der Nummerierung von Weblisten. V R 26/15 trägt die verwendete Aussage in Rn. 19–23; nicht existierende spätere Randnummern wurden entfernt. Für BGH I ZR 202/25 wurden Rn. 20–24, 31–40, für den Vertragsdokumentengenerator Rn. 19–39 kontrolliert.

EuGH C-395/21 ist bereits in der vorhandenen Quellenprüfung dieses Projekts mit Rn. 35–50 dokumentiert. Der erneute EUR-Lex-Aufruf lieferte in dieser Teilprüfung keinen auswertbaren lokalen Volltext; die Such- und Weiterleitungsseiten wurden nicht als neuer Volltextnachweis ausgegeben. Seine in den beiden Skills verwendete knappe Aussage wurde zusätzlich mit dem tatsächlich erneut gelesenen amtlichen BGH-Volltext IX ZR 65/23, Rn. 17–23, abgeglichen. Für eine konkrete unionsrechtliche Streitfrage bleibt der erneute unmittelbare EuGH-Volltextabruf erforderlich. Die anderen jeweils vier Honoraranker wurden als Originalentscheidungen überprüft.

## 1.2. Honorar, Reichweite und Zeitnachweis

| Entscheidung und amtlicher Nachweis | Gelesene Passage | Konkrete Verwendung und Grenze |
|---|---|---|
| [BGH, Urteil vom 19.02.2026 – IX ZR 226/22](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_226-22.pdf?__blob=publicationFile&v=1) | Rn. 8–18, 23–32 und 34 | Reichweite auslegen und Form getrennt prüfen; keine automatische Erstreckung auf neue Aufträge. Anerkenntnisfiktion auch im Unternehmerverkehr unwirksam; Restvertrag gesondert beurteilen. |
| [BGH, Urteil vom 19.02.2026 – IX ZR 227/22](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_227-22.pdf?__blob=publicationFile&v=1) | Rn. 8–13 | Parallelentscheidung zur Reichweite und Klauselkontrolle. Gleichartiger Lebenssachverhalt oder Aktenname ersetzt keine Umfangsfeststellung. |
| [BGH, Urteil vom 12.09.2024 – IX ZR 65/23](https://curia.europa.eu/site/upload/docs/application/pdf/2025-04/ix_zr__65-23_2025-04-16_15-06-53_148.pdf) | Rn. 16–35, 37 und 51 | Transparenz, Benachteiligung und Rechtsfolge getrennt; konkrete Zeitdarlegung bleibt erforderlich. Kein Freibrief für unbestimmte Abrechnung. |
| [EuGH, Urteil vom 12.01.2023 – C-395/21, EU:C:2023:14](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0395) | Vorhandener Projektbeleg Rn. 35–50; erneuter inhaltlicher Abgleich über BGH IX ZR 65/23 | Wirtschaftliche Verständlichkeit gegenüber Verbrauchern. Kein allgemeines Verbot anwaltlicher Stundenhonorare; begrenzter erneuter Direktabruf wie in 1.1 dokumentiert. |
| [BGH, Urteil vom 13.02.2020 – IX ZR 140/19](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2019/IX_ZR_140-19.pdf?__blob=publicationFile&v=1) | Rn. 27–35 | Formularmäßige Viertelstundenabrechnung jedenfalls gegenüber Verbrauchern beanstandet. Keine pauschale Aussage über jede andere denkbare Taktklausel. |

Die Regeln gegen erfundene KI-Ersparnisstunden, über doppelte Zeiterfassung und über die getrennte Dokumentation nicht berechenbarer Arbeit sind eigene Workflowumsetzungen des vereinbarten Zeitpreises und wahrheitsgemäßer Leistungsdokumentation. Es wird hierfür kein besonderes „KI-Abrechnungsurteil“ behauptet. Die aktuelle Suche berücksichtigte die Entscheidungen vom Februar 2026. Ein höherer automatischer Preis für technische Beschleunigung wird nicht erfunden; Festpreis und Zeithonorar bleiben wirtschaftlich getrennt.

## 1.3. Rechnungsberichtigung und Stand des Verfahrens 2026

| Entscheidung und amtlicher Nachweis | Gelesene Passage | Konkrete Verwendung und Grenze |
|---|---|---|
| [BFH, Urteil vom 20.10.2016 – V R 26/15](https://www.bundesfinanzhof.de/en/entscheidungen/entscheidungen-online/decision-detail/STRE201610285/) | Rn. 19–23 | Mindestangaben und zeitliche Möglichkeit der Berichtigung. Materielle Vorsteuervoraussetzungen bleiben erforderlich; keine pauschale Rückwirkung jedes beliebigen Dokuments. |
| [BFH, Beschluss vom 26.02.2026 – V B 11/25](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202650044/) | Rn. 2, Leitsatz und Tenor | Zulassung einer Revision zur Frage ursprünglich nicht berichtigungsfähiger Dokumente. Keine Sachentscheidung über die offene Rechtsfrage. |
| [BFH, anhängiges Verfahren V R 7/26](https://www.bundesfinanzhof.de/de/anhaengige-verfahren/aktuelle-verfahren/detail/STAH260500007/) | Amtlicher Registereintrag, Aufnahme 19.06.2026 | Der Folgestand wurde gezielt gesucht und als anhängig gefunden. Daraus folgt keine Aussage über einen späteren Ausgang. |

Der Abrechnungsskill verwendet zusätzlich die passenden Zeitnachweisanker IX ZR 65/23 und IX ZR 226/22. Die Rechnungsanforderungen nach § 10 RVG und die Anforderungen einer strukturierten Rechnung werden nicht verwechselt. Ein erfolgreicher XML-Validator beweist weder den materiellen Honoraranspruch noch eine tatsächlich erbrachte Leistung.

## 1.4. Fremdgeld, Steuer und Insolvenz

| Entscheidung und amtlicher Nachweis | Gelesene Passage | Konkrete Verwendung und Grenze |
|---|---|---|
| [BFH, Urteil vom 29.09.2020 – VIII R 14/17](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202110029/) | Rn. 20–32, insbesondere 23 und 28–31 | Eine nach außen erklärte Behandlung als eigenes Honorar kann die für den durchlaufenden Posten maßgebliche Verbindung lösen. Keine berufsrechtliche Erlaubnis zur Aufrechnung. |
| [BFH, Urteil vom 16.12.2014 – VIII R 19/12](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE201510153/) | Rn. 17–25 und Leitsätze | Steuerliche Behandlung und rechtswidrige Verwendung bleiben getrennt. Keine Gestattung der Vermischung oder Eigennutzung fremder Gelder. |
| [BGH, Urteil vom 27.04.2017 – IX ZR 198/16](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2016/IX_ZR_198-16.pdf?__blob=publicationFile&v=1) | Rn. 14–16 | Aussonderung und Vermischung im konkreten Treuhand-/Insolvenzfall. Kein anwaltlicher Standardabrechnungsfall; Übertragung erfordert Prüfung von Konto und Rechtsgrund. |

Die Suche nach neueren amtlichen Fremdgeldentscheidungen wurde durchgeführt; aus dem Suchergebnis wird keine Vollständigkeitsbehauptung abgeleitet. Der zusätzliche BFH-Anker aus 2026 betrifft eine eigenständige Vorsteuerfrage und wird nicht künstlich als Fremdgeldentscheidung dargestellt. Aktuell steht die Fremdgeldpflicht in § 43a Absatz 7 BRAO. Die Absatznummer 5 in älteren Entscheidungen wird als historischer Normstand erkannt und nicht in die heutige Handlungsregel übernommen.

## 1.5. AGB, Vertragsgestaltung und Automatisierung

| Entscheidung und amtlicher Nachweis | Gelesene Passage | Konkrete Verwendung und Grenze |
|---|---|---|
| [BGH, Urteil vom 11.03.2026 – I ZR 202/25](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/I_ZS/2025/I_ZR_202-25.pdf?__blob=publicationFile&v=1) | Rn. 20–24, 31–40; ergänzend 41–43 und 49–52 | Textform kann durch getrennte E-Mails erfüllt werden; Bestimmbarkeit und erkennbarer Erklärungsabschluss bleiben wichtig. Spezieller Maklerfall nach § 656a BGB, keine allgemeine Abschaffung von Formvorschriften. |
| [BGH, Urteil vom 20.03.2014 – VII ZR 248/13](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2013/VII_ZR_248-13.pdf?__blob=publicationFile&v=1) | Rn. 26–30 | Tatsächliches Aushandeln statt formularmäßiger Bestätigung. Der besondere Sicherheitenfall wird von der allgemeinen AGB-Aussage getrennt. |
| [BGH, Urteil vom 07.04.2011 – VII ZR 209/07](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2007/VII_ZR_209-07.pdf?__blob=publicationFile&v=1) | Rn. 15–21 | Grenzen eines Aufrechnungsverbots bei eng verbundenen Gegenansprüchen im Architektenvertrag. Keine pauschale Unwirksamkeit jeder Aufrechnungsbeschränkung. |
| [BGH, Urteil vom 09.09.2021 – I ZR 113/20](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/I_ZS/2020/I_ZR_113-20.pdf?__blob=publicationFile&v=1) | Rn. 19–39 | Standardisierter Vertragsdokumentengenerator und konkrete fremde Angelegenheit. Kein allgemeiner Freibrief für generative individuelle Rechtsberatung. |

Die neue Textformentscheidung aus 2026 wurde gezielt gesucht und aus dem amtlichen PDF überprüft. Die Skills nennen daneben die aktuell erforderliche Normprüfung: § 309 BGB für einzelne Klauselverbote, § 310 für den persönlichen Anwendungsbereich, § 312k für Kündigungsfunktionen, § 356a für die elektronische Widerrufsfunktion und § 578 für langfristige Grundstücks-/Gewerberaummiete. Diese Normen wurden unmittelbar abgerufen und gelesen. Die geänderte Textformregel wird nicht auf alle Miet- oder sonstigen Vertragstypen übertragen. Kündigung und Widerruf bleiben getrennt.

## 1.6. Technischer Quellen- und Funktionsabgleich

Die [amtliche KoSIT-Versionsseite](https://xeinkauf.de/xrechnung/versionen-und-bundles/) bestätigt zum Prüfstand die normative Version 3.0 und das Bundle 3.0.2 Summer 2026 Bugfix vom 31.08.2026. XRechnung 4.0 vom September 2026 wird als Vorversion ausgewiesen. Die Skills machen daraus keine bereits gültige Produktionsversion. Für konkrete Rechnungen wird eine erneute Prüfung des akzeptierten Empfängerprofils verlangt.

[§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html) wurde im aktuellen Wortlaut gelesen: Textform und Mitteilung durch den Anwalt oder auf seine Veranlassung. Eine allgemeine eigenhändige Unterschriftpflicht wurde nicht übernommen. [§ 27 Absatz 38 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html) wurde als Übergangsquelle geöffnet; die Detailroute berücksichtigt zusätzlich die vorhandene Rechtsquellenreferenz des Projekts. Der erneute Abruf der BMF-FAQ gab zeitweise 503 zurück und wird deshalb nicht als erfolgreich neu gelesener Volltext protokolliert.

`kanzlei.py` wurde auf seine tatsächlichen Eingaben, Korrekturen und Grenzen geprüft. Bestätigte verwendete Grundlagen werden nicht rückwirkend umgeschrieben. Ein neuer Phasenschlüssel darf keinen Gesamtdeckel umgehen. Unbekannte Zeiten bleiben unbekannt. Zahlungen werden getrennt dokumentiert, nicht automatisch verrechnet oder als Erlös gebucht. `manual-fee` setzt ein tatsächlich geprüftes RVG-Blatt voraus; das Werkzeug ist kein RVG-Automat. Die Geldberechnung ist auf ausdrücklich geprüfte inländische 19-Prozent-Fälle begrenzt.

`xrechnung.py` unterstützt EUR, inländische Parteien, positive Positionen und 19 Prozent Umsatzsteuer. Es unterstützt insbesondere keine Vorschussverrechnung, Rabatte, Gutschriften oder Reverse Charge. Es prüft weder ein kanzleiweites Rechnungsnummernregister noch die Echtheit von Steuer- oder Kontodaten. Es erzeugt eine Datei, keine KoSIT-Validierung und keinen Versand. Diese Grenzen stehen in den betreffenden Skills ausdrücklich. Die CLI-Beschreibungen wurden mit dem Code abgeglichen; es wurden keine Skripte verändert.

## 1.7. Hashes tatsächlich erneut gelesener Original-PDFs

| Dokument | Bytes | SHA-256 |
|---|---:|---|
| BGH IX ZR 226/22 | 156238 | `55667d1503d1f25b4bc1f08823f38ca2dd27a098d4ed581d848eaa279776cc92` |
| BGH IX ZR 227/22 | 116315 | `3ce30d8c299353dd0add169ce4d8fae54e3d97ae0140914eec489979040f8095` |
| BGH IX ZR 140/19 | 236643 | `8d8f292028042004b3a4a29bbe88ef8da0e22f5a66e93172e0486bc57e1c40a7` |
| BGH IX ZR 65/23 | 249031 | `13e2dff0a2822b15f0c3fdc1f81ea613398f82bff841ef9a1fdea0d0f21f4d71` |
| BGH I ZR 202/25 | 160575 | `1b3819d47d50f7acf176d19ca1c8d81a88bf27721b7223f628afd5b0e07f26d0` |
| BGH VII ZR 248/13 | 243007 | `4a835c89d9a72df07140c77a24c5e2c95cdee5192b781edb9fdbe669c17144fb` |
| BGH VII ZR 209/07 | 104884 | `6573a21a3a000b519dd1957a0752c94f2f4474ee3d5996943c9dd90c69f9d8c6` |
| BGH I ZR 113/20 | 276404 | `84701b9b96dff9067d3df69e635fc0efedcdcd85b54100e8a8fc946661fbfc77` |
| BGH IX ZR 198/16 | 127243 | `d1acd918d88e76fb37d0204703f86518da8ddff5174d180e866b48c8872e2a39` |
| BFH V R 26/15 | 55776 | `1046e043dd9d55b9685c5b09a8e014e952d4657def74ae54a18023de2d85f5b6` |
| BFH VIII R 14/17 | 62599 | `8a70dc75ac9985da4c5cd8c48fde1ca9ffe822c30cf41d3e87c5aca070e1ef3c` |
| BFH VIII R 19/12 | 65538 | `107981505587bdfcbb99f516f893fca48fb00bea349a3c35abcbdce22efde6ae` |

## 1.8. Redaktionelle und strukturelle Kontrolle

Alle sechs Skills enthalten genau die sechs vorgesehenen Hauptabschnitte und ausschließlich dezimale Untergliederung. Das Frontmatter enthält nur `name` und `description`. Die Texte halten bestehende Honorargrundlagen vor, fragen nur entscheidende fehlende Angaben und schreiben ausschließlich bestätigte Tatsachen fort. Sie enthalten vollständige Klauseln und Briefe statt Satzgerüsten. Interne Vermerke, Empfängertexte und technische Eingaben werden unterschieden.

Die abschließende Wortzählung erfolgt automatisiert über die tatsächlichen Dateien. Die physische A4-Seitenmessung übernimmt der zentrale Renderlauf; hier wird keine ungemessene Seitenzahl behauptet. Es wurden weder Verträge versandt noch Rechnungen gestellt, Zahlungen ausgeführt oder Produktivbuchungen vorgenommen. Geändert wurden nur die sechs zugewiesenen Skilldateien und dieses Quellenprotokoll; es wurden keine Commits erzeugt.
