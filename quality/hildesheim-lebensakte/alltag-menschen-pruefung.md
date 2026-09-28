# 1 Prüfung der Alltagskorrespondenz zu Nachbarschaft und Vermietung

Prüfdatum: 28.09.2026. Gegenstand ist ausschließlich der Datensatz `scripts/data/hildesheim-alltag-menschen.json`. Seine 16 Texte wurden vollständig semantisch gelesen und aufeinander sowie auf die vorhandenen Originale abgestimmt. Die neuen Alltagsszenen gehören zur simulierten Zukunftshandlung der Testakte.

Der Datensatz enthält vier Antwortfolgen mit je vier Dokumenten: 14 E-Mails und zwei DOCX-Vermerke. Die Texte umfassen zusammen 3.489 Wörter, je Dokument 206 bis 239 Wörter einschließlich Anrede und Gruß. Der Umfang von 150 bis 350 Wörtern wird damit für jedes Dokument eingehalten.

SHA-256 des geprüften Datensatzes: `d5f811eb5fb6c70de892336ce0bf11595209124150d1d5b03d87d8786a8d5bb2`.

## 1.1 Inhaltliche Prüfung aller 16 Dokumente

| ID | Wörter | Inhalt und geprüfter Anschluss |
|---|---:|---|
| MENSCH01 | 222 | Heinrich Schulze fragt vor den Umzügen nach Zufahrt und Ansprechpartner. Die neue Nachbarfigur wird eingeführt; keine bereits eingetretene Behinderung oder fremde Flächennutzung behauptet. |
| MENSCH02 | 219 | Friedrich Weber antwortet mit Übergabe- und Mietbeginn, fragt nach dem gemeinten Tor und benennt die Verwaltung. Keine Parkplatzreservierung oder ständige Bereitschaft zugesagt. |
| MENSCH03 | 222 | Der Nachbar klärt die Verwechslung der Tore und präzisiert die zunächst ungenaue Zeitangabe auf Montag, 02.10.2028, zwischen acht und neun Uhr. Die vorherige Nachricht wird dadurch nachvollziehbar fortgeführt. |
| MENSCH04 | 239 | Interner DOCX-Vermerk hält zwei begrenzte Beobachtungen und die Rückmeldung des Nachbarn fest. Keine lückenlose Überwachung oder zusätzliche Nutzungsvereinbarung behauptet. |
| MENSCH05 | 207 | Lea Fricke fragt Derya Aydin nach der Beschriftung; Wohnung 02 liegt im Erdgeschoss Mitte. Die Schlüsselprüfung wird angekündigt, noch nicht als durchgeführt dargestellt. |
| MENSCH06 | 215 | Derya Aydin bestätigt die Schreibweise, erklärt ihren Irrtum bei der Etage und bittet um eine Klingelprobe. Ein früherer Ton ihrer alten Wohnung wird nicht auf das neue Gebäude übertragen. |
| MENSCH07 | 206 | Die Verwaltung bestätigt Namen und Zuordnung und erläutert den konkreten Ablauf am Übergabetag. Noch keine Funktionszusage aus einer nicht erfolgten Probe. |
| MENSCH08 | 212 | Die Mietpartei bestätigt nach der Übergabe Beschriftung und Probe sowie drei Wohnungs-/Haustürschlüssel und zwei Briefkastenschlüssel. Kein neuer Mangel und keine Änderung des Mietbeginns. |
| MENSCH09 | 224 | Leon und Amira Winter unterscheiden Übergabetermin, Mietbeginn und späteren Möbeltransport. Sie fragen nach Ablauf, Anfahrt und Aufzug; eine ausschließliche Nutzung wird nicht vorausgesetzt. |
| MENSCH10 | 217 | Die Verwaltung bestätigt Freitag 29.09., 16 Uhr, und erläutert Schlüssel, Stellplatz 08 und Anfahrt zu Nummer 18. Keine Änderung des Mietbeginns oder Zusage eines Straßenstellplatzes. |
| MENSCH11 | 223 | Die Mietpartei bestätigt nach der Übergabe die fünf Schlüssel sowie sämtliche Werte aus 145 und 169. Der vorläufige mündliche Lesefehler 3,6 statt 36,0 kWh wird ausdrücklich vom richtigen abschließenden Protokoll getrennt. |
| MENSCH12 | 223 | Interner DOCX-Vermerk gleicht die Werte mit dem vorhandenen Protokoll ab und hält eine telefonische Rückmeldung zum Möbeltransport fest. Keine zusätzliche Abnahme, keine neue Zustandsbescheinigung. |
| MENSCH13 | 216 | Mika Petersen fragt nach Wohnungsstrom, PV und Ablesedatum. Der Irrtum wird als eigener Eindruck formuliert, nicht als behauptete zusätzliche Zusage der Vermieterin. |
| MENSCH14 | 212 | Die Verwaltung erläutert das vorhandene Vertrags- und Messkonzept aus 133 und 166. Der Übergabestand von 24,0 kWh bleibt dem tatsächlichen 29.09. zugeordnet. |
| MENSCH15 | 219 | Die Mietpartei hat das Missverständnis verstanden, hält den tatsächlichen Ablesetag fest und fragt offen nach der vom Versorger verlangten Kennung. Keine Anmeldung oder Lieferbestätigung erfunden. |
| MENSCH16 | 213 | Die Verwaltung dokumentiert den telefonischen Abgleich zu WE04. Der Text unterstellt nach der Nachprüfung keinen vorangegangenen falschen Formulareintrag; die Mietpartei hatte in 15 nur beinahe das falsche Datum eingesetzt. Der externe Stromvertrag wird nicht als erledigt bezeichnet. |

## 1.2 Mietparteien und Übergaben

Die Namen, Wohnungen und Lagen wurden gegen sämtliche acht vorhandenen Mietverträge gelesen und mit den acht Übergabeprotokollen abgeglichen. Alle Pfade in dieser Prüfung sind relativ zu `testakten/bauwirtschaft-hildesheim-lebensakte/`.

| Wohnung | Mietpartei exakt nach Vertrag | Lage | Vertragsquelle | Übergabequelle |
|---|---|---|---|---|
| 01 | Lena und Paul Rehm | EG links | `11_Vermietung/130_Mietvertrag_WE01.docx` | `11_Vermietung/138_Uebergabe_WE01.pdf` |
| 02 | Derya Aydin | EG Mitte | `11_Vermietung/131_Mietvertrag_WE02.docx` | `11_Vermietung/139_Uebergabe_WE02.pdf` |
| 03 | Jonas und Eva Lenz | EG rechts | `11_Vermietung/132_Mietvertrag_WE03.docx` | `11_Vermietung/140_Uebergabe_WE03.pdf` |
| 04 | Mika Petersen | 1.OG links | `11_Vermietung/133_Mietvertrag_WE04.docx` | `11_Vermietung/141_Uebergabe_WE04.pdf` |
| 05 | Sabine und Martin Hartung | 1.OG Mitte | `11_Vermietung/134_Mietvertrag_WE05.docx` | `11_Vermietung/142_Uebergabe_WE05.pdf` |
| 06 | Nora und David Klein | 1.OG rechts | `11_Vermietung/135_Mietvertrag_WE06.docx` | `11_Vermietung/143_Uebergabe_WE06.pdf` |
| 07 | Tessa Brandt | 2.OG links | `11_Vermietung/136_Mietvertrag_WE07.docx` | `11_Vermietung/144_Uebergabe_WE07.pdf` |
| 08 | Leon und Amira Winter | 2.OG rechts | `11_Vermietung/137_Mietvertrag_WE08.docx` | `11_Vermietung/145_Uebergabe_WE08.pdf` |

Alle Wohnungsübergaben fanden am 29.09.2028 statt. Der vertragliche Mietbeginn bleibt der 01.10.2028. Der neue Möbeltransport der Familie Winter am 02.10.2028 ist eine organisatorische Ergänzung und keine Änderung dieser Daten. Die betreffenden Wochentage wurden mit dem Kalender abgeglichen: 29.09. Freitag, 01.10. Sonntag, 02.10. Montag. Auch der Ortstermin am 20.09. ist ein Mittwoch.

Geprüfte Einzelwerte für Wohnung 08: SW-E-08 mit 36,0 kWh; SW-K-08 mit 2,0 m³; SW-W-08 mit 1,4 m³; SW-H-08 mit 0,064 MWh. Für Wohnung 04 stimmt SW-E-04 mit 24,0 kWh. Diese Angaben beziehen sich jeweils auf den 29.09.2028. Die Zahl von drei Wohnungs-/Haustürschlüsseln und zwei Briefkastenschlüsseln entspricht den jeweiligen Übergaben. Mietpreise, Vorauszahlungen und sonstige finanzielle Vereinbarungen wurden nicht verändert.

Die Personen Heinrich und Ursula Schulze sind neue Nachbarfiguren. Es wurden keine neuen Mieter eingesetzt oder vorhandene Mietparteien umbenannt. Sämtliche individuellen E-Mail-Adressen verwenden reservierte `.example`-Domains; die Mietadressen `wohnung02`, `wohnung04` und `wohnung08` entsprechen den bereits vorhandenen wohnungsbezogenen Korrespondenzadressen. Verwaltungs- und Projektsteuerungskontakte nutzen die bestehenden ACTORS-Schlüssel.

## 1.3 Genaue Bestandsbezüge im Datensatz

Alle neun unterschiedlichen `references`-Pfade wurden auf Existenz innerhalb des Aktenordners geprüft:

1. `01_Grundlagen_und_Erwerb/005_Lageplan_LP01.pdf`
2. `08_Bauausfuehrung/04_Lieferungen_und_Pruefungen/Bestandsnachweise/166_PV_Ladepunkte_Inbetriebnahme.pdf`
3. `08_Bauausfuehrung/04_Lieferungen_und_Pruefungen/Bestandsnachweise/169_Zaehlerregister_Bezug.csv`
4. `11_Vermietung/131_Mietvertrag_WE02.docx`
5. `11_Vermietung/133_Mietvertrag_WE04.docx`
6. `11_Vermietung/137_Mietvertrag_WE08.docx`
7. `11_Vermietung/139_Uebergabe_WE02.pdf`
8. `11_Vermietung/141_Uebergabe_WE04.pdf`
9. `11_Vermietung/145_Uebergabe_WE08.pdf`

Die PV-Aussage wurde zusätzlich im Text des Original-PDFs 166 geprüft: Allgemeinstromversorgung und Überschusseinspeisung, kein Mieterstromliefervertrag mit den einzelnen Wohnungsnutzern. Die neuen Schreiben erfinden weder einen Stromtarif noch eine abgeschlossene Anmeldung. Die Kennung im Übergabeprotokoll wird nicht ungeprüft als jede vom externen Anbieter benötigte Markt- oder Gerätenummer ausgegeben.

Der Lageplan dient der Einordnung des Projektgrundstücks. Die neuen Beschreibungen von Toren, persönlichen Terminen und kurzen Gesprächen werden durch die neuen Schreiben selbst in die Akte eingeführt; sie werden nicht als bereits im Lageplan dokumentierte Tatsachen ausgegeben.

## 1.4 Technische und redaktionelle Prüfung

Der JSON-Datensatz wurde mit dem gebündelten Python erfolgreich eingelesen. Geprüft wurden die 16 eindeutigen IDs, vier Threads mit je vier Dokumenten, zulässige Formate und Ordner, alle Pflichtfelder, nichtleere ausformulierte Absätze und sämtliche Wortumfänge. Jede Antwort verweist auf eine frühere ID im gleichen Thread; die Datumsreihenfolge ist jeweils strikt aufsteigend. Individuelle Absender und Empfänger sind mit Namen und reservierter E-Mail-Adresse belegt, bestehende Personen mit ACTORS-Schlüsseln.

Die Absätze enthalten ihre eigenen Anreden und Grußformeln. Der Root-Generator soll diese unverändert übernehmen und keine zusätzlichen Anreden erzeugen. Die zwei DOCX-Datensätze sind MENSCH04 und MENSCH12; beide enthalten einen internen Vollzugsvermerk statt einer zweiten, nur umformatierten E-Mail.

Es wurden keine neuen Rechnungsbeträge, Preisminderungen, kostenpflichtigen Beauftragungen oder Vertragsänderungen eingeführt. Bekannte Mängelvorgänge, insbesondere der Belag in Wohnung 07 und die spätere Feuchtemeldung, werden weder erledigt noch neu erklärt. Es gibt keine neue Rechtsprechung, Normbehauptung oder vorweggenommene technische Mangelursache.

Die Datenerstellung ist abgeschlossen. In diesem Arbeitsschritt wurden keine Originale generiert, keine PDFs gerendert und kein Commit oder Push vorgenommen. Die visuelle Prüfung der später vom Root-Generator erzeugten EML-/DOCX-Lesefassungen erfolgt nach deren Bereitstellung gesondert; dieser Bericht behauptet dafür noch keine Freigabe.

## 1.5 Vollständige visuelle Endprüfung nach der Generierung

Nach Bereitstellung der eingefrorenen Originale wurden am 28.09.2026 sämtliche 16 Lesefassungen vollständig geprüft. Jede PDF umfasst genau eine Seite. Alle 16 Seitenbilder unter `/tmp/hildesheim-lebensakte-alltag/page-qa/MENSCH01/` bis `MENSCH16/` wurden tatsächlich einzeln mit `view_image` in Originalgröße geöffnet und gelesen. Die Sichtprüfung umfasste sämtliche Texte einschließlich Dateikopf, Absender-/Empfängertabelle, Datum, Anrede, Gruß und Fußzeile. Die DOCX-Vermerke MENSCH04 und MENSCH12 wurden anhand ihrer bereitgestellten kanonischen Renderfassung geprüft.

Ergebnis: 16 von 16 Seiten ohne offenen Sicht- oder Inhaltsbefund. Keine abgeschnittenen Zeichen, fehlenden Umlaute, Überlagerungen, herausragenden Tabellen oder abgetrennten Grußformeln festgestellt. Die langen Dateipfade in den E-Mail-Köpfen werden vollständig umbrochen. Beide Word-Vermerke passen vollständig auf je eine Seite; Titel, Zeitangaben, Absender, Adressaten und Seitenfüße sind lesbar.

Die sichtbaren Namen und Anreden passen zu den jeweiligen Absendern und Empfängern. Die Datumsangaben setzen die dokumentierte Antwortfolge unverändert um. Wohnung 08 bleibt mit 36,0 kWh Strom, 2,0 m³ Kaltwasser, 1,4 m³ Warmwasser und 0,064 MWh Wärme zum 29.09.2028 wiedergegeben; der davon getrennte vorläufige Lesefehler 3,6 kWh ist ausdrücklich als solcher kenntlich. Für Wohnung 04 stehen unverändert 24,0 kWh am 29.09.2028. Die finale Formulierung in MENSCH16 enthält keinen widersprüchlichen zwischenzeitlichen Datumswechsel.

Die Quellen- und Renderzuordnung stammt aus `/tmp/hildesheim-lebensakte-alltag/new-pages.json`; die Quellpfade sind zusätzlich über die IDs im Repository-Manifest `quality/hildesheim-lebensakte/alltag-manifest.json` auffindbar. Sämtliche Quellhashes wurden gegen die tatsächlichen Originaldateien erneut geprüft. Die nachstehenden PDF-Hashes wurden unmittelbar nach Abschluss der vollständigen Sichtprüfung berechnet. Die Originale, PDFs und Daten wurden während dieser Nachprüfung nicht geändert.

| ID | Gesehene Seite | Quellformat | SHA-256 der final geprüften PDF |
|---|---|---|---|
| MENSCH01 | 1 von 1 | EML | `c7f52e91e2a5afbf6f4b91d3acd9bf0f1b05bffb200a549b0827266bfe45e6ad` |
| MENSCH02 | 1 von 1 | EML | `145b97ef332a4b843e6cfb31be253ed4815c0fda5b8bfe2cc3e8c71186321af6` |
| MENSCH03 | 1 von 1 | EML | `ae7f19c5adae96abcb7d50df5749c18e7117303bad94bfaaea497c4eaf03af63` |
| MENSCH04 | 1 von 1 | DOCX | `f8a0930d193eb36a122710fc352d2304c01eaa5ea2fb3d2dc375fcb8e4b2c153` |
| MENSCH05 | 1 von 1 | EML | `f0abb0b91e226a858995910e4a2ead2949f23d75e978d6c90350a93b7c671920` |
| MENSCH06 | 1 von 1 | EML | `dbabe5e8738277435deff05d8b9f29820f1ac7663f2029e3867eaee577633d2d` |
| MENSCH07 | 1 von 1 | EML | `ad827f477f8bed88d12ae2405084c6d696a11b05e884b525da8f08472b38330c` |
| MENSCH08 | 1 von 1 | EML | `9b1a5f18c24c0322e15495e9aaa4f67261d2030a723391074f79d2e2f3a3cc6d` |
| MENSCH09 | 1 von 1 | EML | `8ba85840ecb31c198e7d64bd9f5cc799059484003df95cc2f4f42ba10f4af21e` |
| MENSCH10 | 1 von 1 | EML | `fa34b2fa6f6bccc07cfe141c03e9a125e35e1672e5daa071bf3f6dae961ec516` |
| MENSCH11 | 1 von 1 | EML | `4fc181bcd06d275ce0503362966d8f0ff9f693faf4dc7a59dc6de9deb8246120` |
| MENSCH12 | 1 von 1 | DOCX | `f312866a39366330839d490cd4bbb602e338eb35d45bdecfada661620a661280` |
| MENSCH13 | 1 von 1 | EML | `66fa43729858a144cd104c256a3640f93cb90a78ec5ed16caeb6b7ee385c29d9` |
| MENSCH14 | 1 von 1 | EML | `ced966bf41eb1f0c9d21fd3aafe18867af5071aa472f4ae838c4aa862ea59549` |
| MENSCH15 | 1 von 1 | EML | `bf6bd79e9ba2a211fdbecdb75d7e9f749002a3b181ce6b4b3c094e38c113ec29` |
| MENSCH16 | 1 von 1 | EML | `875265a5ca6b5a0e69979301fc73dcceb1e0267e5554c0a881cf64650685335f` |

Die vor der Generierung in Abschnitt 1.4 noch ausstehende Sichtprüfung ist damit abgeschlossen. Die Freigabe bezieht sich genau auf die hier dokumentierten 16 PDF-Dateien und die per Manifest zugeordneten unveränderten Originale.
