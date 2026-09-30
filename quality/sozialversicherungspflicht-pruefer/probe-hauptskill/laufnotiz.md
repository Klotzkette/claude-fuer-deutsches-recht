# 1. Auftrag und tatsächlicher Ablauf

Unabhängiger Anwendungslauf des Hauptskills „sozialversicherungspflicht-pruefen“ für Mila Degenhardt/Kranichspur Prozessdesign GmbH. Prüfdatum und recherchierter Stichtag: 30.09.2026. Uhrzeit gegen Ende des Laufs per Clock-Tool: 30.09.2026, 07:46:34 UTC. Der übergebene Nutzerauftrag verlangte eine verständliche Einordnung der Beteiligung/Gesellschaftervereinbarung und einen Entwurf für die Lohnstelle; kein Versand.

Es wurden keine README-, Quality-, Rubric-, Builder- oder fremden Testberichte gelesen. Die Gesamtdarstellung im Unterordner `gesamt-pdf` wurde bei der Dateiauflistung sichtbar, aber nicht geöffnet. Gelesen wurden nur die nummerierten nativen Dateien 01–32 der angegebenen Akte sowie die nachfolgend bezeichneten lokalen Arbeitsanweisungen. Es wurde weder ein Repository geändert noch eine Nachricht nach außen gesendet, ein Antrag gestellt oder eine Meldung geändert. Die Kommunikation mit dem Hauptagenten diente ausschließlich der Rückfrage/Fortführung des Testvorgangs.

Der Hauptskill verwies ausdrücklich auf die Geschäftsführervertiefung und drei allgemeine Referenzdateien. Diese wurden gelesen. Andere lokale Skills, Vorlagen oder Anweisungsdateien wurden nicht herangezogen. Die Quellenreferenz wurde vollständig ausgegeben; für die Subsumtion herangezogen wurden die Abschnitte zu GmbH, Beschäftigung, Zweigprüfung, Beiträgen und Verfahren. Das Lesen des Referenzverzeichnisses wurde nicht als eigener Abruf sämtlicher dort erwähnten Urteile behandelt. Insbesondere wurden die dortigen Angaben zu Urteilen vom Juli 2026 nicht eigenständig verifiziert oder im Ergebnis als Entscheidungsbeleg verwendet.

DOCX wurden aus `word/document.xml` gelesen, mit Absatznummern im Extrakt; XLSX aus Workbook-/Worksheet-XML einschließlich Zelladressen, Formeln und gespeicherten Werten. Die Summen für Gehalt und Beiträge wurden unabhängig mit Python Decimal nachgerechnet. PDFs wurden lokal mit `pdftotext -layout` extrahiert. EML wurden zunächst als Quelltext ausgegeben und anschließend vollständig MIME-/Quoted-Printable-dekodiert gelesen. TXT/CSV/ICS wurden als Text gelesen. Es erfolgte keine visuelle Unterschriften- oder Echtheitsprüfung. Dateisystem-Zeitstempel wurden nicht als Vertragsdatum verwendet.

Die erste gebündelte Werkzeugausgabe war gekürzt. Deshalb wurden insbesondere Dateien 05–13 nochmals gezielt als Extrakt gelesen; sämtliche EML wurden nochmals dekodiert ausgegeben. Der aus den Originalen erzeugte Text liegt in `aktenextrakt.txt`. Er ist eine Arbeitshilfe dieses Laufs, keine fremde Lösung.

# 2. Anweisung und Hash

Verwendeter Hauptskill:

`sozialversicherungspflicht-pruefer/skills/sozialversicherungspflicht-pruefen/SKILL.md`

SHA-256 bei erster Lektüre und beim Abschlussabgleich:

`d6c372c166a7dd168cc65efab9b01bbd36d24034a7de7e8803d4c0d1ccfcbb0c`

Die vollständigen Pfade und SHA-256-Hashes aller fünf gelesenen lokalen Anweisungs-/Referenzdateien stehen in `anweisungen-sha256.json`:

- `skills/sozialversicherungspflicht-pruefen/SKILL.md`
- `skills/geschaeftsfuehrer-und-gesellschaftermacht/SKILL.md`
- `references/quellen-und-entscheidungen.md`
- `references/prueflogik.md`
- `references/zitierweise.md`

# 3. Tatsächliche Rückfrage und Antwort

Vor Abschluss der ersten Stufe wurde dem Hauptagenten folgende konkrete Rückfrage zur Weiterleitung übermittelt:

> Rückantwort für die abschließende KV/PV- und Beitragsprüfung benötigt: Bitte Mila konkret fragen: (1) Wie war sie seit Beginn der Geschäftsführung am 01.04.2024 und jeweils 2025/2026 kranken- und pflegeversichert (gesetzliche Kasse, freiwillig oder Pflichtmitglied; oder privater Versicherer), mit welchen Beginn-/Wechseldaten? Bitte Mitglieds-/Versicherungsbescheinigungen, tatsächliche Zusatzbeitragssätze bzw. private Prämien und bisher selbst gezahlte Beiträge/Zuschüsse. (2) Geburtsdatum sowie Zahl/Geburtsdaten ihrer Kinder für Pflegebeitrag und mögliche Altersausnahmen. Begründung: Die dokumentierten Festgehälter 74.400 €/Jahr 2025 und 81.600 €/Jahr 2026 überschreiten die allgemeine JAEG; dies ersetzt keine Klärung des Absicherungswegs und persönlicher Beitragsmerkmale. Status, RV/ALV-Grundmodell, 85%-Katalog/Stimmbindung und Lohnstellenentwurf lassen sich unabhängig weiter bearbeiten. Keine allgemeine Neubefragung erforderlich.

Die bereits unabhängig möglichen Teile wurden weiter bearbeitet. `ergebnis-1.md` wurde mit der ersten Einschätzung, den noch offenen Rückfragen und einem integrierten Entwurf gesichert. Die dort ausgeschriebenen Rückfragen enthalten zusätzlich die konkretisierende Bitte um einen etwaigen KV/PV-Befreiungsbescheid und einen gegebenenfalls bestehenden Altersvollrentenbeginn; darauf kam kein eigenständiger zusätzlicher Rückfrageturn.

Danach übermittelte der Hauptagent folgende **ausdrücklich simulierte Mandantenantwort**:

> Ich bin am 14.06.1987 geboren, kinderlos, wohne und arbeite in Berlin. Seit 01.04.2024 unverändert freiwilliges Mitglied der Nordhafen-Krankenkasse und dort auch pflegeversichert, keine private Versicherung. Laut Kassenbescheinigung gilt seit 01.01.2026 der individuelle Zusatzbeitrag von 3,2 %. Die Bescheinigungen und meine eigenen Zahlungen für 2024/2025 muss ich noch heraussuchen. 2026 habe ich bisher selbst bezahlt; ich brauche zunächst die Rechnung für September 2026 und noch keine abschließende Nachforderung für die Vergangenheit.

Diese Antwort wurde im selben Vorgang verwendet, nicht in die Originalakte eingefügt. Die darin erwähnte Kassenbescheinigung wurde nicht tatsächlich vorgelegt. Insbesondere wurden daraus keine vorliegenden Belege für 2024/2025 gemacht. `ergebnis-2.md` und der gesonderte `lohnstellenentwurf-september-2026.md` begrenzen die konkrete Folgerechnung auf September 2026. Ergebnis 1 wurde danach nicht um die Antwort ergänzt oder überschrieben.

# 4. Originalstand und redaktionelle Änderung der Akte

Der Hauptagent kündigte während der Arbeit nach Lektüre der Originale eine redaktionelle Erweiterung der beiden GmbH-Akten an, nach seiner Nachricht ohne Änderung von Satzungs-, Stimmrechts- oder Gehaltsfakten. Daraufhin wurden unmittelbar die 32 gelesenen nummerierten Rohdateien gehasht und das Manifest in `rohdateien-sha256-stand-1.json` gesichert. Beim Hashlauf war das angekündigte Snapshotverzeichnis noch nicht vorhanden.

Später wurde das vom Hauptagenten bereitgestellte Verzeichnis `eingabe-original-stand-1/` ausschließlich per Dateihash gegen das Manifest geprüft: **alle 32 Dateien stimmen überein, keine Abweichung**. Die redaktionell geänderte Akte wurde nicht erneut gelesen. Beide Ergebnisse sind damit dem ursprünglichen, im Snapshot gesicherten Eingabestand zugeordnet. Der Agent hat keine redaktionelle Aktenänderung selbst vorgenommen.

# 5. Tatsächliche Rechtsquellenlektüre

Die Recherche erfolgte am 30.09.2026 über das Webwerkzeug und ergänzende direkte Abrufe amtlicher Seiten/PDFs mit Python urllib. Suchtreffer wurden zum Auffinden verwendet, nicht automatisch als Volltextlektüre ausgegeben. Die im Ergebnis verwendeten 32 Quellenlinks sind zusätzlich in `beleglinks-verwendete-quellen.txt` gespeichert.

## 5.1. Gerichtliche Volltexte

- BSG, Urteil vom 14.03.2018 – B 12 KR 13/17 R: amtliches PDF direkt heruntergeladen, als `quellen/bsg2018.pdf` und Text gespeichert. Für den Befund tatsächlich gelesen und verwendet: Rn. 18 und 21–24. Rn. 21–24 wurden nach einer gekürzten Sammelausgabe nochmals gezielt ausgegeben. Link: https://www.bsg.bund.de/SharedDocs/Downloads/DE/Entscheidungen/2018/2018_03_14_B_12_KR_13_17_R.pdf?__blob=publicationFile&v=3
- BSG, Urteil vom 01.02.2022 – B 12 KR 37/19 R: amtliches PDF in Version v=2 direkt heruntergeladen, als `quellen/bsg2022.pdf` und Text gespeichert. Tatsächlich sichtbare/gelese­ne Gründe insbesondere Rn. 12–27; verwendet Rn. 13–18. Link: https://www.bsg.bund.de/SharedDocs/Downloads/DE/Entscheidungen/2022/2022_02_01_B_12_KR_37_19_R.pdf?__blob=publicationFile&v=2

Die ersten Webabrufe der BSG-PDF-/HTML-Adressen scheiterten mit 403. Danach funktionierte der unmittelbare Download der amtlichen PDFs. Ein erfolgreicher Download wird nicht als vollständige geistige Lektüre aller Seiten bezeichnet; zitiert sind nur tatsächlich gelesene Passagen.

## 5.2. Gesetzestexte

Tatsächlich als Text gelesen wurden folgende amtliche Einzelnormen (jeweils `https://www.gesetze-im-internet.de/`):

- SGB IV: § 7 Abs. 1, § 7a Abs. 1–7, § 23 Abs. 1 sowie übriger Text, § 24 Abs. 1–2, § 25 Abs. 1–2, § 28e Abs. 1, § 28g vollständig, § 28h Abs. 1–2.
- GmbHG: §§ 16, 47 und 54; für den Befund insbesondere § 16 Abs. 1, § 47 Abs. 1–2 und § 54 Abs. 3.
- SGB VI: § 1 (Beschäftigungstatbestand und AG-Vorstandssonderregel); § 168, insbesondere Abs. 1 Nr. 1.
- SGB III: § 25 Abs. 1, § 341 Abs. 1–4 und § 346 einschließlich hälftiger Beitragstragung.
- SGB V: § 6, insbesondere Abs. 1 Nr. 1 und Abs. 4; § 257 Abs. 1–2; § 241; § 250 Abs. 2. § 223 wurde zusätzlich gelesen; die Abruffassung enthält bereits eine besondere Regel für 2027. Für die Septemberrechnung wurden die gesondert geprüften Werte 2026 und die GKV-Grundsätze verwendet, keine 2027-Grenze.
- SGB XI: § 20, insbesondere Abs. 3; § 23; § 61, insbesondere Abs. 1–2; § 55 Abs. 1–3; § 58 Abs. 1 und 3. Die im § 55 Abs. 1 genannte gesetzliche Ausgangszahl von 3,4 Prozent wurde nicht ungeprüft verwendet, sondern die geltende Erhöhung auf 3,6 Prozent über § 1 PBAV 2025 geprüft.
- SGB VII: § 2 Abs. 1 Nr. 1 und § 150 Abs. 1.
- § 2 der Sozialversicherungsrechengrößen-Verordnungen 2025 und 2026; § 1 PBAV 2025; §§ 1–2 Beitragsverfahrensverordnung.

Ein Teil der Gesetzesabrufe scheiterte zunächst im Webwerkzeug mit Timeout. Der unmittelbare Abruf funktionierte; die erste UTF-8-Dekodierung misslang, worauf mit der vom Server angegebenen Kodierung beziehungsweise ISO-8859-1 gelesen wurde. Mehrere so gelesene Texte sind unter `quellen/` gespeichert. Der irrtümlich probierte Pfad `/bvv/__2.html` ergab 404; der richtige Pfad `/beitrvv/__2.html` wurde anschließend gelesen. Es wurden konsolidierte Normtexte und ausdrücklich jahresbezogene Quellen 2025/2026 gelesen. Eine lückenlose Sammlung sämtlicher historischer Änderungsgesetze zu jeder stabilen Grundnorm erfolgte nicht.

## 5.3. Jahreswerte und Verwaltungsquellen

- BMAS, Sozialversicherungsrechengrößen-Verordnung 2025: Text zu 8.050 Euro RV-BBG und 5.512,50 Euro KV-BBG/6.150 Euro monatlicher JAEG gelesen. https://www.bmas.de/DE/Service/Gesetze-und-Gesetzesvorhaben/sozialversicherungs-rechengroessenverordnung-2025.html
- BMAS, Sozialversicherungsrechengrößen-Verordnung 2026: Wertetabelle mit 8.450 Euro RV/ALV-BBG, 5.812,50 Euro KV/PV-BBG und 77.400 Euro allgemeiner JAEG gelesen (Treffer/Seitenausgabe der amtlichen Domain `bmas.bund.de`). https://www.bmas.bund.de/DE/Service/Gesetze-und-Gesetzesvorhaben/sozialversicherungs-rechengroessenverordnung-2026.html
- DRV Rheinland, Fachinfo 04/2024: Abschnitt „Beiträge 2025“, 18,6 Prozent RV, per Find nochmals gezielt ausgegeben; keine Anwendung dortiger Rentner-KV-Regeln auf die Geschäftsführerin. https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Traeger/Rheinland/Fachinformationen/Rundschreiben/2024/4_2024.html
- DRV Knappschaft-Bahn-See, Rechengrößen 2026 vom 02.01.2026: Zahlen zu RV, ALV, Jahresgrenzen, hälftiger Beitragstragung gelesen. https://www.deutsche-rentenversicherung.de/KnappschaftBahnSee/DE/Aktuelles/Meldungen/2026/2026_01_02_Sozialversicherungsrechengroessen2026.html
- BMG, Finanzierung der Pflegeversicherung: Passage/Tabelle zu 3,6 Prozent, 0,6 Prozent Kinderlosenzuschlag sowie 1,8/2,4 Prozent außerhalb Sachsens gelesen. https://www.bundesgesundheitsministerium.de/themen/pflege/online-ratgeber-pflege/die-pflegeversicherung/finanzierung/?L=1
- GKV-Spitzenverband, Beitragsbemessungsseite und von dort amtlich verlinkte Beitragsverfahrensgrundsätze Selbstzahler, Stand 01.01.2025, zuletzt geändert 20.03.2024: Gelesen wurden insbesondere § 1 Abs. 1–3, § 7 Abs. 1, §§ 9–11 (PDF-Seiten 2, 9, 11–12). Sie tragen die konkrete getrennte Berechnung von allgemeinem KV-Beitrag/Zusatzbeitrag, die Rundung und den Selbstzahler-Fälligkeitstermin. https://www.gkv-spitzenverband.de/media/dokumente/krankenversicherung_1/grundprinzipien_1/finanzierung/beitragsbemessung/2025-01-01_Einheitliche_Grundsaetze_zur_Beitragsbemessung_freiwilliger_Mitglieder_Stand_01_01_2025.pdf
- Zur Gegenprüfung gelesen: TK-Seite über freiwillig versicherte Beschäftigte, einschließlich Betragstabelle und Hinweis auf getrennte Teilbeitragsberechnung. Die ausgegebenen Tabellenbeträge/Summen waren teilweise centweise inkonsistent; deshalb wurden die Beträge nicht übernommen. Berechnet wurde anhand der GKV-Grundsätze und der im Test genannten 3,2 Prozent. https://www.tk.de/techniker/versicherung/gut-versichert-in-jeder-lebenslage/freiwillige-krankenversicherung-tk/beitragshoehe-arbeitnehmer-2006954

Weitere Suchresultate (etwa andere DRV-Tabellen, BSG-Jahresbericht, GKV-Einnahmenkatalog, BMG-Reformhinweise, Wikipedia oder Foren) wurden angezeigt, aber nicht als tragende Quelle verwendet. Insbesondere wurde die fiktive Nordhafen-Krankenkasse nicht mit einer realen Kasse gleichgesetzt und kein im Netz recherchierter Kassensatz behauptet. Der Satz 3,2 Prozent stammt ausschließlich aus der simulierten Antwort.

# 6. Rechenkontrolle und Grenzen

Erste Stufe: 12 × 6.200 × (0,186 + 0,026) = 15.772,80 Euro; 9 × 6.800 × (0,186 + 0,026) = 12.974,40 Euro; zusammen 28.747,20 Euro. Als Modellbetrag ausgewiesen, ohne festgestellte Nachforderung, KV/PV/UV/Umlagen/Säumniszuschläge.

Zweite Stufe: Python Decimal, kaufmännische Cent-Rundung. KV 848,63 + 186,00 = 1.034,63; KV-Zuschuss 424,31 + 93,00 = 517,31; PV 244,13; PV-Zuschuss 104,63. KV/PV-Selbstzahlerbetrag 1.278,76, Zuschüsse 621,94. RV/ALV je Partei 632,40 + 88,40 = 720,80. Milas Eigenbelastung 1.377,62; GmbH-Zusatzlast 1.342,74. Die Differenz von einem Cent bei der KV-Eigenlast wurde erläutert. Kein Netto wurde vorgetäuscht; keine bereits bezahlten Beiträge wurden als erneut offen unterstellt.

Alle Dokumente sind Text-/Markdown-Ausgaben, keine erzeugten Word- oder PDF-Enddokumente. Die fehlenden persönlichen Originalbescheinigungen und Zahlungsnachweise der Vergangenheit bleiben ausdrücklich offen. Es erfolgte kein eigener Handelsregisterabruf, keine Anfrage bei einer Krankenkasse und keine behördliche Statusfeststellung.

# 7. Gelesene Rohdateien

Die folgende Liste wird aus dem gesicherten Hashmanifest ergänzt. Alle Dateien wurden inhaltlich als Text beziehungsweise Zellinhalt gelesen; die Hashes identifizieren den ursprünglichen Stand.

| Datei | SHA-256 |
| --- | --- |
| 01_Auftrag_20260929.eml | `7d5f7a5531b769685cfe569f860b510665025f0bcfb0b40f62564a86d4252edc` |
| 02_Satzung_unterzeichnet.docx | `055c089ac3deed90df7a4ce72748a121e6f95e4bb884619140f385ec1c3e586d` |
| 03_Registerchronologie_20260929.pdf | `110df756382c6ef05d387d0370e17785eaa79388ef182bc872f66aed32ee4aba` |
| 04_Gesellschafterliste.pdf | `9252dfac1c5de1ac93ed790745df7b849a49d09d61f50ffec2f999e90f8c6f36` |
| 05_Bestellung_Geschaeftsfuehrung.docx | `6e6058765d8bd9a3f4727473d21cf0e544332c7619ffb8ddb4cff3daa8ea48af` |
| 06_Geschaeftsfuehrer_Anstellungsvertrag.docx | `bf67ff5c6cd28d2828a98077f684a15f6ba715d8f551198b5a76fd6235a5b221` |
| 07_Shareholder_Agreement.docx | `71d03ee1a80cac67af98a6c3385f92b03670594c8f56fed35a3ca4db6ec6f0d9` |
| 08_Geschaeftsordnung.docx | `39793db1003bc8d9763ad99e07e782ca58e62fefd00ff71b9c1507eb6e1085aa` |
| 09_Satzungsaenderung_Entwurf.docx | `29f3996348998bb0f0810f59ff1236c1ac6cc27899fb22235e005dbea1b9b1fe` |
| 10_Protokoll_Budget_20260818.docx | `d969b5d8e5ca66cf94c5af5371935545d7889b5aa28361b3ebc9bb3ff894e9dc` |
| 11_Gehaltsnachtrag_20251212.pdf | `e27ff7bf654c171d9dab31a0c41edc5fc8153a33f11735ade36602f9658296dd` |
| 12_Abrechnung_202608.pdf | `f2d01a16686f2d9da1e25816c579ef808226a7280110640e4409fb3fb2467fe8` |
| 13_Bankbuchung_August_2026.pdf | `7eabdad4fb6a33164be745626e7925e6a8167d6a6f8115db3fde66ef41e02fab` |
| 14_Anteilsuebersicht.xlsx | `2ec1b18f9b64359ea66fc9b4b2658f052ad192700d3ced044a2c4abb5518edc9` |
| 15_Verguetungen_2025_2026.xlsx | `19e867bc92f44af13116bf02a4224eb7073816e22ed2e5e9744ee43de2f1a413` |
| 16_Gesellschafterdarlehen.docx | `cee7351145080c75d5a9f702670c7b09dcdfd442c51f68291ca7eeffe5545bfc` |
| 17_Lohnstelle_Rueckfrage.eml | `c4c9a3fe502f9e901df6a948be4c140b97dedb4498561f4eb9a119d9f310715c` |
| 18_Antwort_Gesellschafter.eml | `88d781e3d16ed9f30e6bed9cc797585c100deb9d0f0b38c26c8f88b4a59e2bee` |
| 19_Notariat_Stand.eml | `2a2ccc5759a12a7443f3794a6986d38fecaf318bc5068bbaaf478c05b64a31eb` |
| 20_Budget_Widerspruch.eml | `1d622c711a690f710d9357cd6c707ff49c6c8dc78366f431d3ef676e9892eb03` |
| 21_Urlaub_Handover.eml | `4470b9dde4ce6c39e9a83a330a678453f92311980c8781b954cb9ee7b0695780` |
| 22_Archivsuche_Bescheid.eml | `4f105744bdd692f0ed060aca038d71b19f081e474472d3757b4c6a49d00ecb6f` |
| 23_Option_oder_Mediation.eml | `925669374099f96b892e6b44071ab242a567bd9b90a1fb8d2ffb88bd9bbad194` |
| 24_Auslagen_Beleg.eml | `7521e4a02661c582dd6b7f1b8ba5104571929efe37c146154837edec560732fd` |
| 25_Zahlungen_2026.csv | `904603beff8285d3acd13674a3677265e603499e0503fa1f9cfdfb79836713ca` |
| 26_Projektzeiten_August.csv | `8c4c5c9ba59d391f2f3bae822b578fe2d76d085b3ca30e4f419870288c86252b` |
| 27_Chat_Export_20260925.txt | `e5048fe13a390f403317b556392deaaaced2dc447f2de68ee68ef2d01a3cfa4d` |
| 28_Telefonnotiz_20260929.txt | `833c335e4ed4dd07fef249edb93b581a72fd2b3430027b7b3d7626cf4c082711` |
| 29_Ablagenotiz_Zeitstempel.txt | `6023d31dc70e7d29bd7a528a4fab7a215e22006761aa4f046b1b0b5e383ff740` |
| 30_Beratungstermin_20261007.ics | `01b8be57683fc617c82377be897c65faab54a9a8da14799bc256f3163d5abc1b` |
| 31_Buchungsbeleg_Darlehen.pdf | `0659d3c7c395924bbedc78c24572d19b6a78d79ac5281d4fb9f529d828857a34` |
| 32_Uebergabe_20260930.eml | `f320b0833add22eae4a09b705999f7b82572f22ca2a380cf2030d6bc32bd59ae` |
