# 1. Quellenadressen und Entscheidungsidentität am 01.10.2026

## 1.1. Repositoryweiter Profilabgleich

Ausgangsstand main `3fcd595306f` (v445.20.2) mit 258 Pluginprofilen. Erfasst wurden alle 412 Zuordnungen in `prompt_editorial_review.decisions` mit insgesamt 343 verschiedenen URLs. Nicht jeder Eintrag ist eine Gerichtsentscheidung; technische und historische Quellen bleiben als solche erkennbar. Nicht jede in einem Spezialskill erwähnte Fundstelle steht in diesen Profilen. Der zusätzliche Markdown-Bestandsabgleich ist deshalb gesondert dokumentiert.

Alle 343 URLs wurden einmal parallel abgerufen. Für PDFs wurden die ersten drei Seiten technisch ausgelesen, für HTML sichtbare Textbestandteile angenähert. 206 Quellen enthielten automatisch das erwartete Aktenzeichen. 35 Quellen hatten kein vom begrenzten Muster erkanntes Aktenzeichen; 82 verlangten eine weitere Prüfung. 18 HTTP-Fehler und zwei sonstige Abruf-/Extraktionsfehler wurden protokolliert. **Keines dieser technischen Ergebnisse beweist die materielle Richtigkeit oder Unrichtigkeit einer Rechtsaussage.** Ein Zahlentreffer irgendwo im Dokument ist insbesondere keine sichere Identitätsprüfung.

[Abrufregister](quellen-erreichbarkeit.json): URL, zugeordnete Profile, HTTP-Status, Weiterleitungsziel, Abrufumfang, PDF-/Inhaltsprüfsumme und technische Fundstellen. 49 EUR-Lex-Abrufe lieferten HTTP 202 ohne Inhalt. Ein zusätzlicher Browserabruf zeigte eine JavaScript-/Robot-Prüfung. Diese Zugriffsgrenze wurde nicht durch erfundene Aussagen oder pauschales Löschen korrekter Anker ersetzt. Auch 403-Antworten des Gerichtsportals beweisen keine falsche Entscheidung.

## 1.2. 39 konkrete BGH-Linkreparaturen

Die alten `juris.bundesgerichtshof.de`-Adressen lieferten überwiegend nur eine allgemeine BGH-Seite; vier Abrufe schlugen fehl. Für alle 39 betroffenen Entscheidungsadressen wurde ein direktes amtliches SharedDocs-PDF erfolgreich geladen. Gericht, Aktenzeichen und Datum wurden im extrahierten Kopf abgeglichen; die 39 Köpfe wurden zusätzlich tatsächlich gelesen. Bei Berichtigungen und Sonderaktenzeichen bleibt die vollständige Identität erhalten. Die PDF-Prüfsumme dokumentiert genau die abgerufene Datei.

Die bestätigten URLs wurden in 68 Fachdateien von 32 Plugins sowie in insgesamt 36 Pluginprofilen ersetzt. Inhaltliche Prüfdatierungen der früheren Quellenprüfungen bleiben erhalten. `source_link_audit_2026_10_01` kennzeichnet den engeren heutigen Umfang. Prompt- und vorhandene Schwerpunkt-Hashes wurden nachgeführt; daraus folgt keine neue juristische Gesamtfreigabe. Historische Prüfberichte und Akten wurden nicht umgeschrieben.

Die vollständige Zuordnung steht in [bgh-linkersatz.json](bgh-linkersatz.json), betroffene Dateien in [linkaenderungen.json](linkaenderungen.json). Die folgende Tabelle zeigt jede Entscheidungsidentität und ihr neues amtliches Abrufziel.

Eine unabhängige Leseprüfung hat alle 39 gespeicherten PDF-Prüfsummen und Entscheidungsköpfe sowie die 68 Dateidiffs gegengeprüft: In diesen Fachdateien wurden ausschließlich die bestätigten URLs ersetzt. Die zugehörigen Profilzitate bleiben erhalten und die betroffenen Prompt-Hashes stimmen. Die Gegenprüfung ist ebenfalls auf Identität und Linkersatz begrenzt.

| Entscheidung | Amtliche Quelle |
| --- | --- |
| BGH, Urteil vom 23.09.2009, VIII ZR 336/08 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIII_ZS/2008/VIII_ZR_336-08.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 15. Februar 2024, VII ZR 42/22, amtlicher Leitsatz | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2022/VII_ZR__42-22.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 03.02.2009, VI ZR 183/08 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VI_ZS/2008/VI_ZR_183-08.pdf?__blob=publicationFile&v=1) |
| BGH, Beschluss vom 03.11.2011, IX ZR 49/09, Randnummer 3 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2009/IX_ZR__49-09.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 09.01.2013, IV ZR 197/11 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IV_ZS/2011/IV_ZR_197-11.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 18.04.2013, III ZR 156/12 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/III_ZS/2012/III_ZR_156-12.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 18.02.2014, VI ZR 383/12 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VI_ZS/2012/VI_ZR_383-12.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 20.03.2014, Az. VII ZR 248/13, amtlich indexierte Leitsaetze | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2013/VII_ZR_248-13.pdf?__blob=publicationFile&v=1) |
| BGH, Beschluss vom 15.06.2016, VII ZB 58/15 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2015/VII_ZB__58-15.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 19.01.2017, Az. VII ZR 301/13, amtlich indexierte Leitsaetze | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2013/VII_ZR_301-13.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 19.07.2017, IV ZR 535/15 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IV_ZS/2015/IV_ZR_535-15.pdf?__blob=publicationFile&v=1) |
| BGH, Beschluss vom 17.11.2022, V ZR 25/22 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/V_ZS/2022/V_ZR__25-22.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 06.12.2022, VI ZR 168/21 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VI_ZS/2021/VI_ZR_168-21.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 20.12.2022, VI ZR 375/21 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VI_ZS/2021/VI_ZR_375-21.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 28.06.2022, Az. II ZR 112/21, Randnummern 12 bis 17 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/II_ZS/2021/II_ZR_112-21.pdf?__blob=publicationFile&v=1) |
| BGH, Beschluss vom 21.03.2023, VIII ZB 80/22 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIII_ZS/2022/VIII_ZB__80-22.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 23.06.2023, V ZR 89/22, amtliche Leitsätze | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/V_ZS/2022/V_ZR__89-22.pdf?__blob=publicationFile&v=1) |
| BGH, Beschluss vom 20.11.2024, VII ZR 191/23 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2023/VII_ZR_191-23.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 6. Oktober 2022, VII ZR 895/21, amtlicher Leitsatz | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2021/VII_ZR_895-21.pdf?__blob=publicationFile&v=1) |
| BGH, Beschluss vom 02.12.2025, II ZR 134/24 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/II_ZS/2024/II_ZR_134-24.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 06.11.2020, Az. LwZR 5/19 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/UebrigeSenate/LdwS/2019/LwZR___5-19.pdf?__blob=publicationFile&v=1) |
| BGH, Beschluss vom 23.11.2012, Az. BLw 12/11 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/UebrigeSenate/LdwS/2011/BLw__12-11.pdf?__blob=publicationFile&v=1) |
| BGH, Beschluss vom 29.04.2016, Az. BLw 2/15 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/UebrigeSenate/LdwS/2015/BLw___2-15.pdf?__blob=publicationFile&v=1) |
| BGH, Beschluss vom 20.06.2006, Az. X ZB 27/05, Demonstrationsschrank, Leitsätze a und c | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/X_ZS/2005/X_ZB__27-05.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 08.11.2007, III ZR 54/07 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/III_ZS/2007/III_ZR__54-07.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 22.06.2011, IV ZR 225/10 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IV_ZS/2010/IV_ZR_225-10.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 18.11.2014, Az. VI ZR 76/14, amtlicher Leitsatz | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VI_ZS/2014/VI_ZR__76-14.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 08.01.2015, I ZR 123/13 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/I_ZS/2013/I_ZR_123-13.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 07.02.2018, Az. VIII ZR 148/17 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIII_ZS/2017/VIII_ZR_148-17.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 15.02.2022, VI ZR 937/20, berichtigt am 23.02.2022 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VI_ZS/2020/VI_ZR_937-20.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 6. März 2025, I ZR 32/24, amtliche Leitsätze | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/I_ZS/2024/I_ZR__32-24.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 18.06.2020, Az. I ZR 93/19, Nachlizenzierung, amtlicher Leitsatz | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/I_ZS/2019/I_ZR__93-19.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 09.09.2021, Az. I ZR 90/20, Influencer I, Leitsatz c | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/I_ZS/2020/I_ZR__90-20.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 16.09.2021, IX ZR 165/19, Randnummern 28 bis 31 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2019/IX_ZR_165-19.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 16.11.2021, Az. VI ZR 1241/20, amtliche Leitsätze | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VI_ZS/2020/VI_ZR_1241-20.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 27.06.2024, Az. I ZR 98/23, klimaneutral, amtliche Leitsätze | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/I_ZS/2023/I_ZR__98-23.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 10.04.2025, III ZR 431/23, Randnummern 17 bis 20 | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/III_ZS/2023/III_ZR_431-23.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 02.11.2000, Az. I ZR 246/98, Gemeinkostenanteil, amtliche Leitsätze | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/I_ZS/1998/I_ZR_246-98.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 07.09.2017, III ZR 71/17, amtlicher Leitsatz | [PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/III_ZS/2017/III_ZR__71-17.pdf?__blob=publicationFile&v=1) |

## 1.3. Unterschiedliche Daten unter einem Grundaktenzeichen

Der interne Abgleich mehrerer Datumsangaben ergab bei `2 AZR 96/24` einen Prüfpunkt, aber keinen Fehler: [BAG, Urteil vom 30.07.2026](https://www.bundesarbeitsgericht.de/entscheidung/2-azr-96-24/), Kopf und Rn. 4, 9–12, unterscheidet selbst das frühere [Teilurteil vom 18.06.2025 – 2 AZR 96/24 (B)](https://www.bundesarbeitsgericht.de/entscheidung/2-azr-96-24-b/). Das spätere Urteil behandelt Annahmeverzugslohn nach dem Anfrageverfahren, das Teilurteil weitere Streitgegenstände. Die bestehenden fachbezogenen Verweise bleiben daher erhalten. Gleiche Grundaktenzeichen wurden nicht automatisch auf ein einziges Datum vereinheitlicht.

## 1.4. Verbesserter Änderungsabgleich

`scripts/audit-rechtsprechungsbestand.py` kann nun mit `--baseline-inventory` unmittelbar gegen das letzte Bestandsregister prüfen. Der bisherige Standardvergleich mit 25.09.2026 bleibt verfügbar. Beide Wege wurden am wirklichen Repository ausgeführt. Vor Beginn der heutigen Fachänderungen zeigte der neue Vergleich 256 unveränderte Profile und genau zwei neue Profile, passend zu den zwischenzeitlichen Veröffentlichungen. Das Startregister liegt nur im lokalen Arbeitsverzeichnis; der abschließende Stand wird im Repository archiviert. Die Zahl eines Aktenzeichenfundes ist weiterhin keine rechtliche Freigabe.

```sh
python3 scripts/audit-rechtsprechungsbestand.py --baseline-inventory quality/source-audits/2026-09-30-zweiter-durchgang/bestand.json --output quality/source-audits/2026-10-01/bestand.json
```
