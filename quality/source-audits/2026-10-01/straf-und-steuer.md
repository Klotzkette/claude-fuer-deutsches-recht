# 1. Strafrecht und Steuerrecht: begrenzter Quellenabgleich am 01.10.2026

## 1.1. Umfang und Vorgehen

Geprüft wurden konkrete, bisher in diesen Profilen nicht belegte Anwendungspunkte in `fachanwalt-strafrecht`, `strafbefehl-verteidiger`, `strafzumessung` und `steuerrecht-anwalt-und-berater`. Vier Entscheidungen aus 2026 wurden im amtlichen Volltext nachgelesen. Die einschlägigen Einfügungen sind mit den vorhandenen Einziehungs-, Strafbefehls-, Strafzumessungs- und Schätzungsabläufen abgestimmt; vorhandene Rückfrage-, Antwortfortsetzungs- und Dokumentwege bleiben erhalten.

Dies ist keine neue Vollprüfung aller Skills dieser vier Plugins. Bereits dokumentierte Entscheidungen von 2013 bis 2026 wurden nicht durch bloße Aktualisierung des Datums erneut als geprüft ausgegeben. Neue Entscheidungen tragen in `sources` und `prompt_editorial_review.decisions` jeweils `checked_on: 2026-10-01`.

## 1.2. Amtlich gelesene Entscheidungen

| Gericht, Entscheidung, Datum, Aktenzeichen | Tatsächlich gelesene Passagen | Aussage und konkrete Anwendung | Grenze |
| --- | --- | --- | --- |
| BGH, Urteil vom 08.01.2026 – 3 StR 203/25, [amtliches PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Strafsenate/3_StS/2025/3_StR_203-25.pdf?__blob=publicationFile&v=1) | Kopf, Tenor und Rn. 1–19; Einfügungen auf Rn. 7–15 gestützt | Einvernehmliche Zwischenlagerung von Beute im frei zugänglichen Schreibtisch der allein bewohnten Wohnung kann umfassende faktische Mitverfügung begründen. Konkludentes Einvernehmen und praktische Handhabung genügen; keine ausdrückliche Abrede aller unbekannten Hinterleute nötig. Ablauf erfasst Zugang, Zugriffssperren, Dauer und tatsächliche Kontrolle vor Ort. | Wohnungsinhaberschaft und Mittäterschaft allein sind keine Zurechnungsautomatik. Eine Ablieferungspflicht beseitigt tatsächlich erlangte Herrschaft nicht; nicht jeder kurze Besitz ist damit erfasst. |
| BGH, Beschluss vom 24.02.2026 – 5 StR 623/25, [amtliches PDF](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Strafsenate/5_StS/2025/5_StR_623-25.pdf?__blob=publicationFile&v=1) | Kopf, Tenor und vollständige Gründe Rn. 1–5; Änderung auf Rn. 4 gestützt | Strafschärfung allein mit gemeinschaftlicher Begehung, die nur Mittäterschaft beschreibt, verletzt § 46 Abs. 3 StGB. Die entsprechende pauschale Position im bisherigen Faktorenkatalog ist berichtigt; Werkstatt und Mini verlangen den Abgleich der konkreten Urteilsformulierung. | Keine feste prozentuale Strafminderung und kein allgemeines Verbot der Würdigung zusätzlicher Ausführungsmerkmale. Konkurrenzkorrektur in Rn. 2–3 gelesen, aber nicht als neuer allgemeiner Workflow ausgebaut. |
| LG Nürnberg-Fürth, Beschluss vom 24.07.2026 – 12 Qs 43/26, [amtlicher Volltext](https://www.gesetze-bayern.de/Content/Document/Y-300-Z-BECKRS-B-2026-N-17546?hl=true) | Kopf, Tenor und vollständige Gründe Rn. 1–14; Anwendung Rn. 9–13 | Kumulativ fehlende Tatbezeichnung und Vorschriften dürfen nach Rechtskraft nicht durch Berichtigung ergänzt werden, wenn der tatsächlich beschlossene rechtliche Inhalt unklar bleibt. Original und Änderung sowie klare Anhaltspunkte für den ursprünglichen Entscheidungsinhalt abgleichen. | Die Entscheidung verwirft die Beschwerde gegen die abgelehnte Berichtigung. Sie hebt nicht den Strafbefehl auf, erklärt ihn nicht allgemein für nichtig und ersetzt keine Einspruchs- oder Wiedereinsetzungsprüfung. Revisionsrechtliche Korrekturbefugnisse sind weiter als schlichte Berichtigung. |
| BFH, Urteil vom 15.04.2026 – X R 14/24, [amtlicher Volltext](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202650130/) | Kopf, Leitsätze, Tatbestand und Gründe Rn. 1–38; tragende Einfügung Rn. 28–33, Abgrenzung Rn. 19–27 und 34–37 | Bereits das fehlende erkennbare Erwägen eines möglichen inneren Betriebsvergleichs ist ein Fehler der Methodenwahl. Einkaufs-, Bestands- und Preisdaten gegenüber der Richtsatzrechnung konkret benennen. | Schätzungsbefugnis bestand fort; keine automatische Übernahme der erklärten Werte. Frostverderb, mögliche Vernehmung der Betriebsleiterin trotz früheren Verzichts und fortbestehende Richtsatzkritik sind Hinweise für den zweiten Rechtsgang ohne Bindungswirkung, keine weiteren tragenden Aufhebungsgründe. |

Die amtlichen PDFs wurden direkt geladen und als Text gelesen; bei den BGH-Seiten scheiterte der Web-Reader teilweise, der direkte amtliche Download war erfolgreich. Der Volltext von Bayern.Recht war nach vorübergehend fehlgeschlagenem Web-Abruf direkt abrufbar. BFH-Randnummern wurden am PDF kontrolliert, weil die nummerierte HTML-Darstellung im Reader in Unterabschnitten neu beginnt.

Ein weiterer recherchierter BFH-Treffer unter der Dokumentkennung `STRE202650047` führte im amtlichen PDF zu **12.11.2018 – X B 88/18**, nicht zu einer Entscheidung von 2026. Dieser Treffer wurde nicht als neuer 2026-Anker übernommen. Datum und Aktenzeichen wurden aus dem Entscheidungskopf bestimmt, nicht aus Dokumentkennung oder Suchmaschinenalter.

## 1.3. Konkrete Normkorrekturen in den berührten Fachskills

### 1.3.1. Strafbefehlszulässigkeit

Der bislang vorhandene Skill `strafbefehl-zulaessigkeit-407` behauptete pauschal einen Ausschluss bei Untersuchungshaft und beim Schöffengericht, enthielt Verfall und allgemeines Berufsverbot im aktuellen Sanktionskatalog, ordnete § 408 falsch zu und behauptete Nichtigkeit bei Zulässigkeitsmängeln. Diese Aussagen wurden anhand der unmittelbar einschlägigen Normen ersetzt; der Arbeitsweg wurde fachlich konkretisiert und um Folgen neuer Unterlagen ergänzt.

Am 01.10.2026 vollständig amtlich gelesen:

- [§ 407 StPO](https://www.gesetze-im-internet.de/stpo/__407.html): erfasste Verfahren, aktueller abschließender Rechtsfolgenkatalog einschließlich Tierhaltungs-/Betreuungsverbot nach Absatz 2 Nr. 2a, Sperrenobergrenze bei Fahrerlaubnisentziehung, Voraussetzungen der Freiheitsstrafe und keine erforderliche vorherige gerichtliche Anhörung. Daraus folgt kein pauschaler Ausschluss bei Untersuchungshaft.
- [§ 408 StPO](https://www.gesetze-im-internet.de/stpo/__408.html): Zuständigkeitswege, Ablehnung mangels hinreichenden Tatverdachts und Anberaumung der Hauptverhandlung bei Bedenken beziehungsweise fortbestehender Abweichung vom Antrag.
- [§ 408b StPO](https://www.gesetze-im-internet.de/stpo/__408b.html): Pflichtverteidigerbestellung bei erwogener Bewährungsfreiheitsstrafe ohne vorhandenen Verteidiger.
- [§ 409 StPO](https://www.gesetze-im-internet.de/stpo/__409.html): Pflichtinhalt und besondere Belehrungen.

Der unüberprüfte alte KCanG-Verweis und der pauschale Verweis auf eine nicht bezeichnete BVerfG-Linie wurden aus diesem Zulässigkeitsskill entfernt. Daraus wird keine fachliche Neubewertung des KCanG abgeleitet. Nichtberichtigungsfähigkeit wurde nicht mit allgemeiner Nichtigkeit gleichgesetzt.

### 1.3.2. Strafzumessung

Im Skill `paragraph-46-stgb-grundsatz-strafzumessung` wurde die vermischte Normzeile fachbezogen korrigiert: § 257c StPO betrifft Verständigung, § 46a StGB Täter-Opfer-Ausgleich/Schadenswiedergutmachung, § 49 StGB besondere gesetzliche Milderung und § 55 StGB nachträgliche Gesamtstrafe. Regelbeispiele stehen in der jeweiligen Deliktsnorm. Der neue BGH-Anker ersetzt die pauschale Strafschärfung durch mehrere Tatbeteiligte. Die unzutreffende pauschale Zuordnung aller heutigen geschlechtsbezogenen Beweggründe zur Fassung von 2015 wurde entfernt.

Am 01.10.2026 gelesen: [§ 46 StGB](https://www.gesetze-im-internet.de/stgb/__46.html), [§ 46a StGB](https://www.gesetze-im-internet.de/stgb/__46a.html), [§ 49 StGB](https://www.gesetze-im-internet.de/stgb/__49.html), [§ 55 StGB](https://www.gesetze-im-internet.de/stgb/__55.html), [§ 257c StPO](https://www.gesetze-im-internet.de/stpo/__257c.html). § 46 wurde nach Reader-Timeout direkt vom amtlichen Server geladen und gelesen. Die unbelegte pauschale Freigabe von „Lüg-Verhalten“ als Schärfungsgrund wurde ebenfalls entfernt; an ihre Stelle tritt die Prüfung konkreter Äußerung, Verteidigungsbezugs und zusätzlicher Rechtsverletzung. Hierfür wird keine zusätzliche neu verifizierte Entscheidung behauptet. Historische Rechtsentwicklung und andere Strafzumessungsfragen wurden nicht umfassend neu recherchiert.

## 1.4. Geänderte fachliche Dateien

- `fachanwalt-strafrecht`: Werkstatt, Schnellstart, Hauptproblem und `skills/einziehung-geldfluss-mitverfuegung-arrestabgleich/SKILL.md`.
- `strafbefehl-verteidiger`: Werkstatt, Schnellstart und `skills/strafbefehl-zulaessigkeit-407/SKILL.md`.
- `strafzumessung`: Werkstatt, Schnellstart und `skills/paragraph-46-stgb-grundsatz-strafzumessung/SKILL.md`.
- `steuerrecht-anwalt-und-berater`: Werkstatt, Schnellstart, Hauptproblem und `skills/hinzuschaetzung-kasse-wareneinsatz-gegenkalkulation/SKILL.md`.
- Vier zugehörige `quality/evals/*.json`: konkrete Quellen, einzelne neue Entscheidungsprüfdaten, begrenzte Review-Beschreibung und betroffene Rohdatei-Hashes aktualisiert.

Vorhandene TXT-Spiegel zu diesen Dateien wurden mit Dateisuche geprüft; keine gefunden. Keine neuen Skills, Testakten, Versionen oder generierten Gesamtausgaben.

## 1.5. Prüfung und verbleibende Grenzen

Alle vier Minis bleiben unter 7.500 Zeichen und UTF-8-Bytes:

| Plugin | Zeichen | Bytes |
| --- | ---: | ---: |
| fachanwalt-strafrecht | 6.343 | 6.422 |
| strafbefehl-verteidiger | 6.121 | 6.210 |
| strafzumessung | 7.096 | 7.236 |
| steuerrecht-anwalt-und-berater | 6.303 | 6.409 |

`quality-lab.py audit --require-editorial --require-workflow` meldete beim gemeinsamen Zwischenstand ausschließlich vier Mini-Hashabweichungen in fremden, parallel bearbeiteten Plugins (Bauwirtschaft, Fachanwalt Bau-/Architektenrecht, Fachanwalt Miet-/WEG-Recht, Mietrecht). In den hier bearbeiteten vier Profilen trat kein Fehler auf. Der globale Abschlusscheck bleibt beim Hauptagenten. Fachliche Diffs, JSON-Lesbarkeit, Zeichen-/Bytegrenzen und betroffene Hashes werden lokal kontrolliert; keine neue Live-Modellprüfung und keine Aussage, sämtliche weiteren Anker des Repositories seien damit geprüft.

Der anschließende Schwerpunkt-Generator erkannte zu lange Hauptproblem-Prompts. Nach Kürzung redundanter Formulierungen bei Erhaltung der Anker und Arbeitsabläufe liegen Strafrecht bei 7.470 Bytes und Steuerrecht bei 7.475 Bytes. Beide Profilhashes wurden aktualisiert; der Generator lief danach erfolgreich. Der abschließende globale Qualitätslabor-Audit erfasste alle 258 Profile ohne Hashfehler; die vollständigen technischen Ergebnisse stehen in `pruefungen.json`.
