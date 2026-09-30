# 1. Umfang der unabhängigen Mini-Probe

Rechtlicher Stichtag: 30.09.2026. Nutzerrolle: Leander Vogt. Auftrag: Unterlagen zur behaupteten Beitragspflicht trotz hälftiger Beteiligung prüfen und die Antwort an die Lohnstelle vollständig ausformulieren; nichts versenden; entscheidende Lücken erfragen.

Die einzige gelesene Produktanweisung war sozialversicherungspflicht-pruefer-schnellstart.md. Keine SKILL-Datei, Werkstatt, README, Qualitätsanforderung, Builder, Rubrik oder früheres Probeergebnis wurde geöffnet. Eine anfängliche Dateiinventur zeigte auch Namen nicht zugelassener Dateien; deren Inhalte wurden nicht gelesen. Inhaltlich ausgewertet wurden ausschließlich die 32 nummerierten nativen Rohdateien im angegebenen Aktenordner sowie die nachträglich ausdrücklich simulierte Nutzerantwort. Andere Testproben oder Ergebnisse anderer Agenten wurden nicht verwendet. Es wurde kein weiterer Agent zur juristischen Prüfung eingesetzt.

# 2. Sicherung und tatsächliche Eingaben

Vor Ausgabe des Produktprompts und vor der inhaltlichen Rohaktenauswertung wurden SHA256-Werte in eingaben-sha256-vor-lesen.json gesichert. Die Liste enthält den als Text gespeicherten Delegationsauftrag, den tatsächlich verwendeten Produktprompt und alle 32 anschließend gelesenen Rohdateien. Der Delegationsauftrag war naturgemäß bereits als Nachricht zugestellt; seine Textkopie dokumentiert diesen Auftrag. Die SHA256-Sicherung der Originaldateien erfolgte vor ihrer Textauswertung.

**Tatsächlich verwendeter Produktprompt:** 7.468 UTF-8-Bytes, SHA256 4bfa1201a87b94777a0f17c7977cf15fd12c2cdd2c7ae0910b8b622e398d5f74.

Nach Erstellung des Erstbefunds teilte der Hauptagent eine redaktionelle Änderung mit: „Aktuelle amtliche Normen auf gesetze-im-internet.de und tatsächlich gelesene Entscheidungen verwenden.“ wurde durch „Normen in aktueller amtlicher Fassung und tatsächlich gelesene Entscheidungen verwenden.“ ersetzt. Nach seiner Mitteilung hat die veröffentlichte Fassung nun 7.454 Bytes. Diese geänderte Datei wurde in der Probe nicht erneut gelesen. Der ursprüngliche Hash bleibt unverändert und wird ausdrücklich nicht als Hash der später veröffentlichten Fassung ausgegeben.

Die genauen Originalpfade, Größen und Hashwerte sämtlicher Rohakten stehen in eingaben-sha256-vor-lesen.json; gelesen wurden:

| Datei | Tatsächliche Auswertung |
|---|---|
| 01_Auftrag_20260929.eml | Kopfzeilen und MIME-dekodierter Text |
| 02_Satzung_unterzeichnet.docx | Hauptdokumenttext einschließlich Beschluss-/Vertretungsregeln |
| 03_Registerchronologie_20260929.pdf | Vollständiger Text, Seite 1 |
| 04_Gesellschafterliste.pdf | Vollständiger Text, Seite 1 |
| 05_Bestellung_Geschaeftsfuehrung.docx | Hauptdokumenttext |
| 06_Geschaeftsfuehrer_Anstellungsvertrag.docx | Hauptdokumenttext |
| 07_Shareholder_Agreement.docx | Hauptdokumenttext |
| 08_Geschaeftsordnung.docx | Hauptdokumenttext |
| 09_Satzungsaenderung_Entwurf.docx | Hauptdokumenttext |
| 10_Protokoll_Budget_20260818.docx | Hauptdokumenttext |
| 11_Gehaltsnachtrag_20251212.pdf | Vollständiger Text, Seite 1 |
| 12_Abrechnung_202608.pdf | Vollständiger Text, Seite 1 |
| 13_Bankbuchung_August_2026.pdf | Vollständiger Text, Seite 1 |
| 14_Anteilsuebersicht.xlsx | Zellwerte, vorhandene Formeln und gespeicherte Formelergebnisse des einzigen Blatts |
| 15_Verguetungen_2025_2026.xlsx | Zellwerte, vorhandene Formeln und gespeicherte Formelergebnisse des einzigen Blatts; Datumserien und Summen kontrolliert |
| 16_Gesellschafterdarlehen.docx | Hauptdokumenttext |
| 17_Lohnstelle_Rueckfrage.eml | Kopfzeilen und MIME-dekodierter Text |
| 18_Antwort_Gesellschafter.eml | Kopfzeilen und MIME-dekodierter Text |
| 19_Notariat_Stand.eml | Kopfzeilen und MIME-dekodierter Text |
| 20_Budget_Widerspruch.eml | Kopfzeilen und MIME-dekodierter Text |
| 21_Urlaub_Handover.eml | Kopfzeilen und MIME-dekodierter Text |
| 22_Archivsuche_Bescheid.eml | Kopfzeilen und MIME-dekodierter Text |
| 23_Option_oder_Mediation.eml | Kopfzeilen und MIME-dekodierter Text |
| 24_Auslagen_Beleg.eml | Kopfzeilen und MIME-dekodierter Text |
| 25_Zahlungen_2026.csv | Vollständige Tabelle |
| 26_Projektzeiten_August.csv | Vollständige Tabelle |
| 27_Chat_Export_20260925.txt | Vollständiger Text |
| 28_Telefonnotiz_20260929.txt | Vollständiger Text |
| 29_Ablagenotiz_Zeitstempel.txt | Vollständiger Text |
| 30_Beratungstermin_20261007.ics | Vollständiger Kalenderdatensatz, UTC-Zeit umgerechnet |
| 31_Buchungsbeleg_Darlehen.pdf | Vollständiger Text, Seite 1 |
| 32_Uebergabe_20260930.eml | Kopfzeilen und MIME-dekodierter Text |

Für DOCX und XLSX wurde der native ZIP/XML-Inhalt mit Python-Standardbibliotheken extrahiert; die EML-Dateien wurden mit der Python-E-Mail-Bibliothek dekodiert. PDFs wurden einzeln mit pdftotext gelesen. Es gab keine Gesamt-PDF-Nutzung, OCR, visuelle Unterschriftenprüfung oder eigene Echtheitsprüfung der Registerabschriften. Die im Aktenbestand enthaltenen Abschriften wurden als solche gewürdigt. Die Arbeitsmappen wurden nicht in einer Tabellenanwendung neu berechnet; die relevanten Vergütungs-/Anteilsrechnungen wurden unabhängig arithmetisch kontrolliert. Ein durch Ausgabegrenzen abgeschnittener Textblock wurde durch gezielte Folgeausgaben der betroffenen Dateien vervollständigt.

Ein Hashvergleich aller 32 Rohdateien vor der später mitgeteilten Vertragskorrektur ergab keine Veränderung. Keine Repositorydatei wurde durch diese Probe bearbeitet. Alle Extraktionen, Downloads und Ergebnisse liegen ausschließlich unter qa-local/probe-mini.

## 2.1 Nachträgliche redaktionelle Vertragskorrektur und Originalsnapshot

Nach Fertigstellung des Briefs teilte der Hauptagent eine redaktionelle Korrektur der Präambel von Datei 06 mit: Die Gesellschaft wird zum Vertragsschluss am 06.05.2019 nun als GmbH in Gründung mit vorgesehener Eintragung beim Amtsgericht Jena bezeichnet; ursprünglich hatte die Abschrift bereits die spätere Registereintragung bezeichnet. Die Registerchronologie nennt die Eintragung am 27.05.2019, der Tätigkeitsbeginn bleibt 01.06.2019. Der hier geprüfte Zeitraum beginnt 2025. Inhaltliche Regelungen zu Tätigkeit, Entgelt und Stimmrechten wurden nach Mitteilung nicht geändert. Die geänderte Vertragsdatei wurde nicht erneut inhaltlich gelesen; der Rechtsbefund wurde nicht rückwirkend als Prüfung dieser späteren Datei ausgegeben.

Der Hauptagent sicherte danach den vorher gebauten Original-ZIP-Stand im Unterordner eingabe-original-stand-1. Alle 32 dort gesicherten nativen Dateien wurden gegen das vor der ersten Inhaltslektüre erstellte SHA256-Manifest geprüft: **32 von 32 stimmen exakt überein**. Das umfasst die ursprünglich gelesenen DOCX-Bytes der Datei 06. Der maschinenlesbare Abgleich ist original-snapshot-hashabgleich.json. Der tatsächlich geprüfte Eingabestand ist damit trotz späterer Veröffentlichungskorrekturen vollständig nachprüfbar. Die frühere Texteextraktion bleibt ebenfalls erhalten.

# 3. Rückfrage und Fortführung

Nach Aktenauswertung wurden persönliche KV/PV-Absicherung, die für selbständige RV-Pflicht relevanten Arbeitnehmer-/Auftraggeberdaten und persönlicher UV-/ALV- sowie neuer Behördenstand beim Hauptagenten erfragt. Die Statusbegründung wurde währenddessen unabhängig recherchiert; eine endgültige Aussage über die persönlichen Zweige wurde zunächst nicht getroffen.

Der Zwischenstand wurde in zwischenstand-rueckfrage.md und anschließend als ergebnis-1.md gesichert. Auf diese Rückfragen folgte eine ausdrücklich simulierte Nutzerantwort, gespeichert in simulierte-nutzerantwort.txt mit eigenem Hash in simulierte-nutzerantwort-sha256.json. Sie ist keine nachträgliche Änderung der Originalakte. Der Erstbefund bleibt erhalten. Die Antwort wurde für ergebnis-2.md und den Brief im selben Vorgang ausgewertet.

Die Folgeantwort bestätigt private KV/PV seit 01.06.2019, eigene Prämienzahlung, drei durchgehend voll versicherungspflichtige Arbeitnehmer seit Januar 2025, 14 unabhängige gewerbliche Kunden und 31 Prozent Umsatzanteil des größten Kunden 2025. Sie verneint eine weitere persönliche Tätigkeit und einen gefundenen Antrag auf freiwillige ALV sowie neue Behördenpost. Persönliche BG-Erfassung und Belege bleiben offen. Die ausdrückliche Vorgabe, keine konkreten Privatprämien oder Zuschüsse zu berechnen, wurde beachtet.

# 4. Tatsächlich gelesene Primärquellen

Die Prüfung verwendete die amtlichen Normtexte von Gesetze im Internet und die unten bezeichneten amtlichen BSG-Texte. Allgemeine Suchergebnislisten enthielten zum Teil fremde Webseiten; sie wurden nicht als Entscheidungsgrundlage verwendet. Der Schnellstart diente nur als Recherchehinweis. Keine nicht gelesene Entscheidung wurde als eigener Beleg ausgegeben.

## 4.1 Rechtsprechung

| Gericht / Dokument | Tatsächlich geprüfte Fundstelle | Aussage / Zugriff |
|---|---|---|
| BSG, Urteil vom 14.03.2018, B 12 KR 13/17 R | Rn. 17–24, besonders Rn. 21–22 | Amtliches HTML und anschließend amtliches Urteils-PDF gelesen; das PDF sichert die Randnummern. Kapital-/Stimmrechtsmacht, exakt 50 Prozent, außerstatutarische Abreden und Gegenindizien. |
| BSG, Terminbericht Nr. 24/2026 vom 24.07.2026 über die Sitzung vom 23.07.2026, Nr. 4, B 12 BA 10/24 R | PDF-Seite 4, Abschnitt Nr. 4 | Tatsächlich heruntergeladener amtlicher Bericht: hälftige Beteiligung mit wirksamem bindendem Stichentscheid. Kein Volltexturteil dieser Entscheidung und keine erfundenen Urteilsrandnummern. |

Amtliche Links: [BSG-Urteil 2018](https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2018/2018_03_14_B_12_KR_13_17_R.html), [Urteils-PDF 2018](https://www.bsg.bund.de/SharedDocs/Downloads/DE/Entscheidungen/2018/2018_03_14_B_12_KR_13_17_R.pdf?__blob=publicationFile&v=2), [Terminbericht 24/2026](https://www.bsg.bund.de/SharedDocs/Downloads/DE/Terminberichte/2026/2026_24_Terminbericht.pdf?__blob=publicationFile&v=2).

Der erste Webtool-Abruf des BSG-Berichts und des Urteils-HTML scheiterte jeweils mit HTTP 403. Ein anschließender direkter Abruf derselben amtlichen URLs mittels Python urllib war erfolgreich (HTTP 200). Das war ein technischer Abrufwechsel, kein Wechsel auf fremde Entscheidungswiedergaben. Die Dateien und ihre Download-Hashwerte stehen im Unterordner quellen, abruf-1.json beziehungsweise abruf-2.json. Die anfänglich offene Quellenlage in ergebnis-1.md wurde durch die danach erfolgreiche Primärquellenlektüre aufgelöst.

## 4.2 Normen

| Norm / amtlicher Link | Gelesener entscheidungstragender Bereich |
|---|---|
| [§ 7 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7.html) | Abs. 1 |
| [§ 7a SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7a.html) | Abs. 1–7, im Ergebnis insbesondere Abs. 1, 2 und 5 |
| [§ 28h SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28h.html) | Abs. 2 |
| [§ 28p SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28p.html) | Abs. 1 |
| [§ 16 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__16.html) | Abs. 1 |
| [§ 47 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__47.html) | Abs. 1–4 |
| [§ 53 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__53.html) | Abs. 1–4 |
| [§ 54 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__54.html) | Amtlicher Suchabruf mit vollständigem Normtext, besonders Abs. 3; erster Direktabruf Timeout |
| [§ 5 SGB V](https://www.gesetze-im-internet.de/sgb_5/__5.html) | Abs. 1 Nr. 1 und Abs. 5; erster Webtool-Abruf Timeout, direkter Download erfolgreich |
| [§ 193 VVG](https://www.gesetze-im-internet.de/vvg_2008/__193.html) | Abs. 3 |
| [§ 20 SGB XI](https://www.gesetze-im-internet.de/sgb_11/__20.html) | Abs. 1 |
| [§ 23 SGB XI](https://www.gesetze-im-internet.de/sgb_11/__23.html) | Volltext, tragend Abs. 1; erster Webtool-Abruf Timeout, direkter Download erfolgreich |
| [§ 1 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__1.html) | Insbesondere Satz 1 Nr. 1 |
| [§ 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__2.html) | Volltext, insbesondere Satz 1 Nr. 9 und Satz 2 Nr. 3 |
| [§ 25 SGB III](https://www.gesetze-im-internet.de/sgb_3/__25.html) | Insbesondere Abs. 1 |
| [§ 28a SGB III](https://www.gesetze-im-internet.de/sgb_3/__28a.html) | Abs. 1–2; keine Behauptung eines heute voraussetzungslos möglichen Versicherungsbeitritts |
| [§ 2 SGB VII](https://www.gesetze-im-internet.de/sgb_7/__2.html) | Abs. 1 Nr. 1 |
| [§ 3 SGB VII](https://www.gesetze-im-internet.de/sgb_7/__3.html) | Volltext, insbesondere Abs. 1 Nr. 1 |
| [§ 6 SGB VII](https://www.gesetze-im-internet.de/sgb_7/__6.html) | Volltext, insbesondere Abs. 1 Nr. 2; erster Webtool-Abruf Timeout, direkter Download erfolgreich |

Die Gesetzesfassungen wurden für den vorgegebenen Stichtag auf den live erreichbaren amtlichen Seiten geprüft. Nicht durchgeführt wurde eine zusätzliche vollständige historische Bundesgesetzblatt-Differenzprüfung jedes im Zeitraum gültigen Absatzes; im Ergebnis werden die für diese Tätigkeit maßgeblichen Grundtatbestände verwendet, keine ungeprüften Rechengrößen behauptet. Der persönliche Versicherungsnachweis bleibt von der Normprüfung getrennt.

# 5. Liefergegenstände und Kontrolle

- ergebnis-1.md: gesicherter Erstbefund mit entscheidenden Rückfragen.
- ergebnis-2.md: fortgeschriebene Prüfung mit belegter Subsumtion, Zweig-/Zeitraummatrix, Vergütungsprüfung, Verfahrenseinordnung und offenen Belegen.
- schreiben-lohnstelle.md: vollständig ausgearbeiteter Entwurf in Leander Vogts Namen.
- schreiben-lohnstelle.html: identischer Brieftext, druckbare HTML-Fassung mit Times New Roman 11 pt, ohne garantierte geräteübergreifende Seitenumbrüche.
- probeprotokoll.md sowie Hashdateien: Eingaben-/Quellen- und Ablaufnachweis.

Kontrolliert wurden 50 Prozent aus 25.000/50.000 Euro, 78.000 Euro Jahresvergütung 2025, 64.800 Euro für Januar–September 2026, Gesamtsumme 142.800 Euro und Augustauszahlung 5.521,80 Euro. Die Excel-Datumserien entsprechen Januar/Dezember 2025 und Januar/September 2026. Aktenfundstellen und tragende BSG-Fundstellen wurden am gelesenen Text abgeglichen. Die Textdateien enthalten keine offenen Namens-/Datumsplatzhalter. HTML und Markdown wurden aus demselben Brieftext erzeugt; eine visuelle PDF-/Druckansicht wurde nicht erzeugt oder behauptet.

Nichts wurde versandt, bei einer Behörde beantragt oder in einem fremden System geändert. Die noch fehlenden persönlichen Versicherungs- und BG-Belege werden ausdrücklich nicht als beschafft ausgegeben.
