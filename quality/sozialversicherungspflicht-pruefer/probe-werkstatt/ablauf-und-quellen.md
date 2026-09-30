# Tatsächlicher Ablauf und Quellenführung der Werkstattprobe

Prüfdatum: 30.09.2026. Sämtliche Ausgaben dieser Probe liegen ausschließlich unter `qa-local/probe-werkstatt/`. Kein Versand, kein Antrag, kein Behördenkontakt, keine Änderung von Repositorydateien. Die Dokumente sind Arbeitsergebnisse eines simulierten Mandats, keine getroffenen Behördenentscheidungen.

## 1. Eingaben und Abgrenzung

Produktanweisung war ausschließlich `sozialversicherungspflicht-pruefer-werkstatt.md`, SHA256 **83d1bc30282c30ae151001145c45ded9793023942c3582db280b1fdac0c843e3**. Keine anderen Produktanweisungen, SKILLs, Mini/Schnellstart, READMEs, Rubrics, Qualitätsprofile, Builder oder frühere Prüfergebnisse wurden inhaltlich gelesen. Die erste Verzeichnisinventur zeigte auch deren Dateinamen; dies war keine Inhaltslektüre. Fachabschnitte der eigenständigen Werkstatt wurden nach Relevanz verwendet. Der erste breite `cat`-Abruf wurde in der Toolausgabe gekürzt; die einschlägigen Abschnitte 7–17 wurden anschließend gezielt nachgelesen.

Rohakten waren nur die nummerierten nativen Dateien 01–27. Alle Dateipfade, Bytezahlen und SHA256 stehen in `eingabe-manifest.json`. EML 15 wurde MIME-dekodiert; ihre beiden PDF-Anhänge wurden separat extrahiert und mit den nativen Nummern 06 und 13 anhand des Hashs verglichen. Sie sind byteidentisch. Anhänge und Herkunft stehen in `anhang-manifest.json`. Die Gesamt-PDF wurde nicht verwendet.

DOCX wurde aus `word/document.xml` gelesen; PDF mittels `pdftotext -layout`; EML mit Pythons Standard-MIME-Parser; TXT/CSV nativ; XLSX unmittelbar aus Workbook- und Worksheet-XML einschließlich Zelladressen, Formeln und gespeicherten Werten. Die lesbare vollständige Zellansicht steht in `27-zellen-gelesen.txt`. Keine Dokumentkonvertierung ersetzt hier eine Behauptung, eine Unterschrift gesehen zu haben: Die DOCX-Dateien enthalten lediglich Ausfertigungs-/Dateinotizen zu Papierunterschriften.

## 2. Tatsächliche Bearbeitungsschritte

1. Rohdateiinventar und Werkstatttext gelesen; SHA256-Manifeste vor inhaltlicher Bewertung angelegt. Alle nummerierten Dateien in `/tmp` textlich erschlossen, EML-Anhänge geprüft. Keine Produktbestandteile außerhalb der Werkstatt als Anleitung verwendet.
2. Vertragsstände, Durchführung, Erinnerungen, Parteierklärungen und Behördenpost getrennt. Widersprüche bei Zustimmung, Portal, Vertretung und Januarzahlung an den zeitnächsten Belegen gewichtet.
3. Vier konkrete Rückfragen über die Testleitung gestellt: spätere Zustimmung; nachfolgende KSK-/RV-/Statusbescheide und Zahlungen; reale Reiseverbote; Beginn/Aufteilung eigener Tätigkeiten und Gewinnunterlagen. Wortlaut und Bedeutung stehen in `ergebnis-1.md`. Der Erststand wurde vor Verarbeitung der Antwort gesichert. Er hält auch den damaligen, noch nicht abgeschlossenen Quellenabruf transparent fest.
4. Erste ausdrücklich simulierte Antwort im selben Vorgang verarbeitet; exakt dokumentiert in `simulierte-antwort.md`. Keine Zustimmung, KSK nur offener Antrag, keine erzwungene Reiseverschiebung und keine feste Nachzahlungsrechnung als fortwirkende Vorgaben übernommen.
5. Amtliche Primärquellen selbst abgerufen und die nachstehend bezeichneten Passagen gelesen. Technische Fehler beim Webzugriff wurden durch direkten Download von denselben amtlichen URLs überwunden; der Quellenstand wurde nicht bloß aus der Produktanweisung übernommen.
6. Aus der Zweigprüfung entstand eine weitere konkrete Frage nach der „anderen Schule“ aus EML 17. Zweite simulierte Antwort: Musikraum Pankow, keine dritte Einrichtung; ebenfalls Rechnungen, aber kein belastbarer Beginn/Vertrag/Stundenumfang nachgereicht. Genau diese offenen Punkte bleiben im Endstand offen.
7. CSV und XLSX unabhängig nachgerechnet; Monats-/Jahreswerte, ersetzte Januarrechnung, Erstattung und 72-Euro-Zahlung abgeglichen. Keine pauschale Beitragsberechnung. Gesonderte verständliche Antwort und vollständiger Akademiebrief in Maras Namen erstellt.
8. Abschlusskontrolle: keine fiktive Zustimmung, kein behaupteter KSK-Bescheid, keine als wahr behandelte Portalheuristik, kein vorgeschobener Widerspruch gegen die Unterlagenanforderung, kein ungeprüfter Parallel-Statusantrag, kein Versand. Eingabehashs am Abschluss erneut verglichen; Ergebnis in `eingabe-integritaet-abschluss.json`.

**Integritätsbefund am Abschluss:** Der Vergleich mit dem weiterbearbeiteten Repository ergab eine Abweichung bei Datei 03, nicht bei der Werkstatt oder den anderen 26 Rohdateien. Anfangshash: `a5e2a47557552979eb77c7cba90355e5379be1fc615e20aff0d1a2de0556c2b5`; späterer Repositoryhash: `b9989059d33688555327ad261714cb0710532bc4dea2bcc6b948ed85cddfe10f`. Die Testleitung bestätigte eine während der Probe vorgenommene redaktionelle Korrektur des Unterrichtsplans und stellte den davor gesicherten Originalstand bereit. Alle 27 Dateien in `eingabe-original-stand-1/` wurden gegen das anfängliche Manifest gehasht und stimmen überein; siehe `snapshot-abgleich.json`. Die Ergebnisse sind dem tatsächlich gelesenen **ursprünglichen** Stand zugeordnet. Die geänderte DOCX wurde nicht erneut inhaltlich gelesen und nicht rückwirkend in das Ergebnis übernommen. Die Probe selbst hat keine Repositorydatei verändert. Eine vollständige Kapazitätsprüfung des ursprünglichen Raumplans gegen die abgerechneten Septemberstunden wurde in dieser Probe nicht geleistet; die dokumentierte Zahlenkontrolle betrifft Rechnungsersetzung, Einheiten, Monatssummen und Zahlungszuordnung.

## 3. Tatsächliche Rechtsquellenabrufe

Die Downloadprotokolle `quellen/abrufe.json`, `abrufe-2.json` und `abrufe-3.json` enthalten tatsächliche UTC-Abrufzeitpunkte am 30.09.2026, Status, URL und Speicherpfad. Die gespeicherten amtlichen PDF/HTML-Originale sind in `quellen/sha256.json` gehasht. **Download allein bedeutet nicht vollständige Lektüre.** Die folgende Liste bezeichnet die tatsächlich für das Ergebnis gelesenen Passagen.

### 3.1. Zeitrecht und Lehrkräftestatus

| Quelle | Tatsächlich gelesene Passage und verwendete Aussage |
| --- | --- |
| [§ 127 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__127.html) | Alle Absätze 1–4. 2027/2028; zwei Konstellationen mit/ohne Feststellung; Zustimmung; Lehrerfiktion ab März 2025; gesonderte KSVG-Regel; frühere Pflichtbeiträge und § 28a SGB III. |
| [BGBl. 2026 I Nr. 107](https://www.recht.bund.de/bgbl/1/2026/107/regelungstext.pdf?__blob=publicationFile&v=2) | Titel/Ausgabe vom 22.04.2026, Art. 3 Nr. 2 auf PDF-S. 13 und Art. 12 Abs. 2 auf PDF-S. 19. Verlängerung und Inkrafttreten am Folgetag verifiziert, nicht alle übrigen Gesetzesänderungen ausgewertet. |
| [§ 7 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7.html) | Im Webtool vollständig angezeigt; für die Prüfung Abs. 1 verwendet. |
| [BSG 28.06.2022 – B 12 R 3/20 R](https://www.bsg.bund.de/SharedDocs/Downloads/DE/Entscheidungen/2022/2022_06_28_B_12_R_03_20_R.pdf?__blob=publicationFile&v=2) | Sachverhalt Rn. 1–11, Gründe Rn. 12–23 im amtlichen PDF gelesen. Einzelfallabwägung, Institution, Freiheiten, Vertretung, Kundenbeziehungen; keine Generalisierung auf alle Musiklehrenden. |
| [BSG 13.11.2025 – B 12 BA 2/23 R](https://www.bsg.bund.de/SharedDocs/Downloads/DE/Entscheidungen/2025/2025_11_13_B_12_BA_02_23_R.pdf?__blob=publicationFile&v=2) | Amtliches PDF, insbesondere Rn. 19–33 im Zusammenhang gelesen; Rn. 20 Vertretung, Rn. 21 Status/Fiktion, Rn. 24–30 offene Altfälle und unentschiedene Bestandskraftfrage, Rn. 31–33 Voraussetzungen und Zustimmung. Alte Enddaten ausdrücklich nicht übernommen. |
| [BSG 05.11.2024 – B 12 BA 3/23 R](https://www.bsg.bund.de/SharedDocs/Downloads/DE/Entscheidungen/2024/2024_11_05_B_12_BA_03_23_R.pdf?__blob=publicationFile&v=2) | Rn. 17–26 im Zusammenhang gelesen. Institutionelles Gesamtkonzept, pädagogische Freiheit und fehlendes substantielles Unternehmerhandeln. Rn. 35–40 nur Suchstellen, nicht als eigenständig vollständig gelesene Belegpassage zitiert. |
| [BSG Terminbericht 24/2026 vom 24.07.2026](https://www.bsg.bund.de/SharedDocs/Downloads/DE/Terminberichte/2026/2026_24_Terminbericht.pdf?__blob=publicationFile&v=2) | Nr. 5, PDF-S. 5–6 vollständig gelesen. B 12 BA 12/24 R vom 23.07.2026: VHS-Schulabschlusskurse; begrenzter Vergleich zur privaten Musikakademie. Kein Urteilsvolltext behauptet. Die unmittelbar vorher ausgegebenen Berichtsteile betrafen andere Themen und tragen das Ergebnis nicht. |

### 3.2. Versicherungszweige, Beiträge und Verfahren

| Quelle | Tatsächlich gelesene Passage / Verwendung |
| --- | --- |
| [§ 7a SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7a.html) | Volltext im Webtool, speziell Abs. 1, 2, 5–7. Vorrang bereits eingeleiteter Verfahren; keine pauschale neue Statusanfrage. Die besondere Einmonatsregel wird nicht auf den 2022 begonnenen Fall fingiert. |
| [§ 28p SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28p.html) | Abs. 1–1c und weitere angezeigte Verfahrenssätze. Prüfbescheidkompetenz, KSA und UV als gesonderte Fragen. |
| [§ 28e SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28e.html) | Abs. 1 gelesen und verwendet. Nachfolgende mitausgegebene Haftungsregeln außerhalb des Falls nicht verwendet. |
| [§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html) | Vollständig, einschließlich Ausnahmen von der begrenzten Nachholung des Arbeitnehmerabzugs. |
| [§ 25 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__25.html) | Abs. 1–2 vollständig. Regelverjährung, Vorsatz nicht unterstellt, Hemmung differenziert. |
| [§ 15 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__15.html) | Volltext; Arbeitseinkommen ist Gewinn, nicht Einnahmensumme. |
| [§ 5 SGB V](https://www.gesetze-im-internet.de/sgb_5/__5.html) | Abs. 1 Nr. 1 und 4 sowie Abs. 5. KV bei Beschäftigung/KSVG und Hauptberuflichkeitsvorbehalt. |
| [§ 20 SGB XI](https://www.gesetze-im-internet.de/sgb_11/__20.html) | Abs. 1 Nr. 1 und 4, Abs. 3. Soziale PV bei Pflicht- und freiwilliger GKV. |
| [§ 1 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__1.html) | Satz 1 Nr. 1; Beschäftigten-RV. Andere im Abruf sichtbare Personengruppen nicht übertragen. |
| [§ 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__2.html) | Volltext, entscheidend Satz 1 Nr. 1 und 5 sowie Arbeitnehmerbegriff. Mehrere Auftraggeber beseitigen Lehrerpflicht nicht. |
| [§ 5 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__5.html) | Abs. 2 im Zusammenhang; geringfügige Selbständigkeit. Keine aktuellen Grenzbeträge als historische Werte verwendet. |
| [§ 169 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__169.html), [§ 190a SGB VI](https://www.gesetze-im-internet.de/sgb_6/__190a.html) | Volltext; Beitragstragung und Meldung. Nur nach festgestelltem Pflichtmodell anwenden. |
| [§ 25 SGB III](https://www.gesetze-im-internet.de/sgb_3/__25.html) | Abs. 1, Beschäftigten-ALV. Kein automatischer ALV-Schutz durch KSVG behauptet. |
| [§ 2](https://www.gesetze-im-internet.de/sgb_7/__2.html), [§ 3](https://www.gesetze-im-internet.de/sgb_7/__3.html), [§ 6](https://www.gesetze-im-internet.de/sgb_7/__6.html), [§ 150 SGB VII](https://www.gesetze-im-internet.de/sgb_7/__150.html) | § 2 Abs. 1 Nr. 1; § 3 Abs. 1 Nr. 1; § 6 Abs. 1 Nr. 1/Abs. 2; § 150 Abs. 1. UV gesondert, konkrete Satzung/Zuständigkeit nicht erfunden. |
| KSVG [§ 1](https://www.gesetze-im-internet.de/ksvg/__1.html), [§ 2](https://www.gesetze-im-internet.de/ksvg/__2.html), [§ 3](https://www.gesetze-im-internet.de/ksvg/__3.html), [§ 4](https://www.gesetze-im-internet.de/ksvg/__4.html), [§ 5](https://www.gesetze-im-internet.de/ksvg/__5.html), [§ 8](https://www.gesetze-im-internet.de/ksvg/__8.html), [§ 11](https://www.gesetze-im-internet.de/ksvg/__11.html), [§ 15](https://www.gesetze-im-internet.de/ksvg/__15.html) | Volltexte gelesen. Künstlerbegriff, Einkommen/Ausnahmen, zweigweise Konkurrenz, Beginn bei Meldungseingang, Mitwirkung, RV-Versichertenanteil. Kein April-Antragsdatum als bewiesener Eingang umgedeutet. |
| KSVG [§ 24](https://www.gesetze-im-internet.de/ksvg/__24.html), [§ 25](https://www.gesetze-im-internet.de/ksvg/__25.html) | § 24 Abs. 1 Nr. 9 und § 25 Abs. 1–2, weitere Sätze mitangezeigt. Potenzielle Abgabe der Einrichtung gesondert; keine feste KSA-Rechnung, keine aktuelle Bagatellgrenze auf Altjahre übertragen. |

### 3.3. Fehler, Suchtreffer und Grenzen

Die ersten `web.run`-Aufrufe von § 127 lieferten Timeouts; BGBl-PDF und BSG-HTML lieferten zunächst HTTP 403. § 7 und § 7a wurden im ersten Webaufruf erfolgreich gelesen. Ein amtlicher Suchtreffer zeigte danach den vollständigen aktuellen § 127; ein anderer Suchtreffer zur älteren SGB-IV-Gesamt-PDF enthielt noch 2026/2027. Dieser Widerspruch wurde durch Download der aktuellen Einzelnorm und des verkündeten Änderungsgesetzes aufgelöst. BSG-PDFs wurden anschließend direkt von der amtlichen Domain erfolgreich heruntergeladen, nicht aus den Suchschnipseln als gelesen behandelt.

Breite Suchen lieferten daneben Sekundärtreffer. Diese wurden nicht als fachliche Grundlage verwendet. Gezielt auf BSG beziehungsweise KSK/DRV-Domains begrenzte spätere Suchen nach dem jüngsten Urteil und ergänzender KSVG-Verwaltungspraxis ergaben keine Treffer. Daraus wurde keine Behauptung abgeleitet, es gebe noch keinen Urteilsvolltext oder keine Verwaltungshinweise. Für den jüngsten Fall wurde ausschließlich die begrenzte amtliche Berichtsaussage genutzt.

Bei einem Downloadlauf brachen KSVG §§ 11, 24 und 25 zunächst mit „Connection reset by peer“ ab; der erneute Abruf war erfolgreich. Ein HTML-Leseversuch scheiterte zunächst an UTF-8; danach wurde der deklarierte ISO-8859-1-Text korrekt gelesen. Diese Fehler verursachten keine inhaltliche Ersetzung durch andere Quellen. Die gespeicherten `web01.json` bis `web04.json` dokumentieren die entsprechenden späteren Webwerkzeug-Ergebnisse; die erfolgreiche Direktbeschaffung ist zusätzlich separat protokolliert.

Es wurde keine Beitragsberechnung vorgenommen, für die historische Bemessungsgrenzen oder Beitragssätze hätten übernommen werden müssen. Die Statusentscheidung ist eine begründete Einschätzung, keine bindende Feststellung. Für Pankow, den KSK-Beginn, Gewinne und die genaue Zuordnung der Versicherungszweige bleiben die ausdrücklich bezeichneten Nachweise offen.

## 4. Ergebnisse

- `ergebnis-1.md`: gesicherter Erststand mit den tatsächlichen ersten Rückfragen.
- `simulierte-antwort.md`: beide simulierten Antworten und die zusätzliche Rückfrage, mit Auswirkungen.
- `ergebnis-2.md`: fortgeführte verständliche und belegte Mandantenantwort.
- `antwortschreiben-akademie.md`: vollständig formulierter Brief in Maras Namen, ohne Zustimmung und ohne behaupteten Versand.
- `aktenregister.md`: interner Beleg- und Fassungsnachweis.
- `eingabe-manifest.json`, `anhang-manifest.json`, `eingabe-integritaet-abschluss.json`, `quellen/sha256.json`: Integritätsnachweise.
