# 1. Umfang und Stand

Geprüft am 2026-09-28T03:40:28+02:00: `scripts/data/hildesheim-alltag-kaufmaennisch.json` enthält zwölf vollständig ausformulierte Datensätze in drei Ketten mit je vier Dokumenten. Vorgesehen sind neun E-Mails und drei interne Telefonnotizen. Die Absatztexte umfassen 213–247 Wörter je Dokument.

SHA-256 der geprüften JSON-Datei:

`5258140558ccbe14b3840b284c4c604dbbc3717141f8f8563f0cfedcd2a91ceb`

# 2. Quellen- und Semantikprüfung

Vor dem Schreiben wurden die referenzierten Rechnungen, Kontoauszüge, Bestands-E-Mails, der Nachtragsauftrag, das Aufmaß und die Belagsvereinbarung gelesen. Sämtliche zwölf Texte wurden anschließend semantisch mit diesen Unterlagen abgeglichen. Eine unabhängige zweite Prüfung präzisierte die Zusammenführung auf demselben Debitorenkonto in KAUF03 und die historische Restforderung in KAUF07; beide Punkte sind eingearbeitet. Die abschließende sprachliche Prüfung entfernte redaktionelle Prüfvermerke aus KAUF09/11.

| ID | Datum | Wörter | Geprüfter Sachverhalt |
|---|---|---:|---|
| KAUF01 | 2028-09-27T09:12:00 | 218 | Rückfrage nach zwei Juni-Überweisungen; Kenntnis aus 113 vom 26.09.; keine Guthabenbestätigung. |
| KAUF02 | 2028-09-28T16:38:00 | 213 | Lichtkreis unterscheidet Rechnung und Bankzuordnung; Klärung noch offen, ohne Rückzahlungszusage. |
| KAUF03 | 2028-12-14T11:05:00 | 235 | Telefonnotiz nach 114: Debitorenkonto zusammengeführt, Rückzahlung für 15.12. angewiesen; kein behaupteter Kontoeingang. |
| KAUF04 | 2029-01-03T10:17:00 | 221 | Erstattung 89.250,00 EUR mit Valuta 15.12. und Referenz LE-RET-20281215; Bestätigung erst nach Ausstellungsdatum des Jahresauszugs. |
| KAUF05 | 2028-10-16T08:46:00 | 237 | Rechnungskorrektur IA-G-28-017 zu IA-28-095; 2.500,00 EUR netto + 475,00 EUR = 2.975,00 EUR; 15.11. nur Wiedervorlage nach 115. |
| KAUF06 | 2028-10-17T17:22:00 | 227 | Keine neue Schlussrechnung; Umfang bleibt die vereinbarte Materialabweichung in Wohnung 07; keine Kontoeingangsbestätigung. |
| KAUF07 | 2028-11-06T14:35:00 | 237 | Telefonnotiz vor angekündigtem Rückzahlungstermin; keine neue Frist, keine Behauptung offener ursprünglicher Schlusszahlung. |
| KAUF08 | 2029-01-04T11:08:00 | 222 | Erstattung 2.975,00 EUR mit Valuta 15.11. und Referenz SW-106-20281115; Januarabgleich des Jahresauszugs. |
| KAUF09 | 2028-03-06T10:03:00 | 226 | Interne Zuordnungsfrage zu Nachtrag 01 / SH-N01 / SH-28-N01; keine erfundene fehlerhafte Projektkennung auf der Rechnung. |
| KAUF10 | 2028-03-07T16:11:00 | 215 | Bestehendes Angebot, Auftrag, Aufmaß und Rechnung verbunden; 57 × 50,00 EUR = 2.850,00 EUR im Pauschalumfang enthalten. |
| KAUF11 | 2028-03-08T09:48:00 | 247 | Telefonische Fundstellenklärung; vorhandene Unterzeichner Nora Feld/Timo Wendt und technischer Befund Dr. Venn zutreffend wiedergegeben. |
| KAUF12 | 2028-03-09T12:06:00 | 228 | Ablagefrage abgeschlossen; Rechnung 21.420,00 EUR nur einmal erfasst; kein neuer Auftrag, Zahltermin oder Zahlungseingang erklärt. |

Alle 17 unterschiedlichen referenzierten Originale existieren. Für jeden Verweis wurde das Datum im Original gegen das Datum des neuen Dokuments geprüft; keine Quelle ist dort vor ihrem Ausstellungs-/Versanddatum als bereits vorliegend verwendet. Der Jahreskontoauszug 111 vom 31.12.2028 wird ausschließlich in KAUF04 vom 03.01.2029 und KAUF08 vom 04.01.2029 verwendet. Seine Spalte weist Valuta aus; die neuen Eingangbestätigungen nennen deshalb Valutadaten.

Die ergänzten Gespräche, Rückfragen und Bürohandlungen sind neue fiktive Korrespondenz innerhalb der Testakte. Sie ergänzen den bekannten Vorgang, ohne neue Leistungsbeträge, Zahlungen, Zahlungsfristen, Bankverbindungen oder Verzichtserklärungen einzuführen. Die vollständigen Angaben zur Projektkennung in der bestehenden Rechnung werden nicht als fehlend dargestellt.

# 3. Datenprüfung und unveränderte Finanzgrundlage

Geprüft wurden zwölf eindeutige IDs, drei Ketten zu je vier Dokumenten, neun EML-/drei DOCX-Vorgaben, Wortzahlen, ISO-Datumswerte, bestehende Akteursschlüssel einschließlich Kopieempfängern, frühere Antwortbezüge innerhalb derselben Kette und relative vorhandene Quellenpfade. Alle Prüfungen bestanden.

Die kanonischen Finanzdaten `quality/hildesheim-achtfamilienhaus/finanzdaten.json` sind byteidentisch zu `HEAD`. Der dortige Investitionsbetrag bleibt 3.482.215,41 EUR; die Differenz zum Finanzierungsrahmen von 3.700.000,00 EUR bleibt 217.784,59 EUR. Originale, Arbeitsmappen, Generatoren und PDF-/ZIP-Ausgaben wurden durch diese Aufgabe nicht bearbeitet.

# 4. Einzelquellen

Die SHA-256-Werte dokumentieren die tatsächlich gelesenen Originale. Die Referenzen in jedem Datensatz bilden die Zuordnung zum jeweiligen Text.

| Originalpfad relativ zur Lebensakte | Ausstellungs-/Versanddatum | SHA-256 |
|---|---|---|
| `08_Bauausfuehrung/Bestandsunterlagen/053_Nachtragsangebot_Filterpackung.pdf` | 2028-02-04 | `896b24a1bf18becf74b8de217d5f2b4bdedb913a4548352ad24a90b35c20d306` |
| `08_Bauausfuehrung/Bestandsunterlagen/054_Nachtragsauftrag_01.eml` | 2028-02-05 | `b5caa8800e65720758e22a81d359a86ba9e548983320b010bcede9c4d754f6c5` |
| `08_Bauausfuehrung/Bestandsunterlagen/055_Gemeinsames_Aufmass_Nachtrag.pdf` | 2028-02-11 | `6f1663c3b935568590f0d20b617fcb0ef6119bdf21f1de8499cb72101b822fa9` |
| `08_Bauausfuehrung/Bestandsunterlagen/147_Belagsvereinbarung_Wohnung07.docx` | 2028-10-15 | `018270cc9bd96ff85e3362738ae3324c2466ab01e5adf9eaf2b12272bf24410b` |
| `10_Rechnungen_und_Buchhaltung/Belege/098_Elektro_Abschlag.pdf` | 2028-06-01 | `765bffa6763f75f07df243c91cc7f94af96f7664cd7e1821a13f334557b3398c` |
| `10_Rechnungen_und_Buchhaltung/Belege/099_Elektro_PV_Schlussrechnung.pdf` | 2028-09-30 | `2d81df7a4085db0cd5f3d18964511facce8ba54851c6e83a4324f7625b5f92d5` |
| `10_Rechnungen_und_Buchhaltung/Belege/101_Innenausbau_Schlussrechnung.pdf` | 2028-09-30 | `2937a72f0922a2fa673572e592f1a4f4e47468f788259f29a21c5d680bd78d5e` |
| `10_Rechnungen_und_Buchhaltung/Belege/105_Rohbau_Nachtrag_Draenpackung.pdf` | 2028-03-05 | `7090b82a5bd9a7b66161b68b68b6d396a28abea21813438918c94dd284762cd1` |
| `10_Rechnungen_und_Buchhaltung/Belege/106_Innenausbau_Rechnungskorrektur.pdf` | 2028-10-15 | `b8d847091f4a356e56f90708969c24e612364d7a40eb228c84ae8e3042c505a9` |
| `10_Rechnungen_und_Buchhaltung/Belege/111_Projektkonto_2028.pdf` | 2028-12-31 | `d4a724286eac53cfd3f5ef3d50776209f936984923d15750a04e745069485b9d` |
| `10_Rechnungen_und_Buchhaltung/Belege/113_Rueckfrage_Elektrozahlung.eml` | 2028-09-26 | `a4e9d7c5bf6b61952b8fa823276578fc2ea8dfdc2e990c877c52d4188bab9771` |
| `10_Rechnungen_und_Buchhaltung/Belege/114_Elektro_Rueckzahlung.eml` | 2028-12-13 | `00294647f5b7940f1b9f9041ceb9ea51138f1f3b02392b690f2499ee82ae077c` |
| `10_Rechnungen_und_Buchhaltung/Belege/115_Innenausbau_Belagsvereinbarung.eml` | 2028-10-15 | `fec5ddb4eb2d359f24c2ab416f8c4c25474b04014b12842f9bd025189bf0a61b` |
| `10_Rechnungen_und_Buchhaltung/Belege/119_PV_Lieferung_Montage_Nullsteuersatz.pdf` | 2028-09-30 | `4a4824596380d6b54eee4c07260cdb81d3e8b177ecc1104e084788c8f54ac441` |
| `10_Rechnungen_und_Buchhaltung/Rechnungseingang/2028-03-05_SH-28-N01_Belegzugang.eml` | 2028-03-05 | `9b7b745c45ee9e5242e779c17d7199a7b4f487424385183b778658a622bf1562` |
| `10_Rechnungen_und_Buchhaltung/Rechnungseingang/2028-06-01_LE-28-061_Belegzugang.eml` | 2028-06-01 | `6e38fdabce4be47a1153f258ef62eee4df23e8be14e3695a951fcb8004c63278` |
| `10_Rechnungen_und_Buchhaltung/Rechnungseingang/2028-10-15_IA-G-28-017_Belegzugang.eml` | 2028-10-15 | `fb70469f90b9574b00df58e0ec391772c15b9e43c7fba2f03f5c85abf1808979` |

# 5. Abgrenzung

Dieser Vermerk betrifft Inhalt und Datenstruktur der zwölf neuen Korrespondenzen. Die Erzeugung und Sichtprüfung der EML-/DOCX-/PDF-Ausgaben und Releasepakete erfolgt anschließend durch den Hauptprozess; dafür wird hier kein bereits bestandenes Ergebnis behauptet.

# 6. Visuelle Endprüfung der zwölf Ausgaben

Abgeschlossen am 2026-09-28T03:47:24+02:00. Alle zwölf endgültigen Seitenbilder `KAUF01/page-1.png` bis `KAUF12/page-1.png` unter `/tmp/hildesheim-lebensakte-alltag/page-qa/` wurden einzeln mit `view_image` in Originalgröße geöffnet und vollständig gelesen. Der Umfang beträgt zwölf von zwölf PDF-Seiten: neun EML-Lesefassungen und die drei kanonisch gerenderten DOCX-Telefonnotizen KAUF03, KAUF07 und KAUF11. Grundlage der Zuordnung ist `/tmp/hildesheim-lebensakte-alltag/new-pages.json`.

Es bestehen keine offenen Sichtbefunde. Textkörper, Anreden und Abschlüsse sind vollständig und lesbar; weder abgeschnittene Zeichen noch Überlagerungen, Randüberläufe oder zusätzliche Leerseiten sind sichtbar. Mehrzeilige Titel und Metadaten sind sauber umbrochen. Die beiden Kopieempfänger in KAUF04 stehen vollständig in der Metadatentabelle. Die freien unteren Seitenbereiche ergeben sich aus den einseitigen Schreiben und Telefonnotizen; es gibt keine störenden Leerflächen innerhalb zusammengehörender Textabschnitte.

Beträge, Belegnummern und die Ausgabe der Dokument-, Gesprächs- und Valutadaten wurden auf sämtlichen Seiten mit den eingefrorenen Absätzen abgeglichen. Besonders geprüft wurden die angekündigten gegenüber den erst später bestätigten Rückflüssen von 89.250,00 EUR und 2.975,00 EUR sowie die Zuordnung von 21.420,00 EUR und 57 Stunden zum Nachtrag SH-28-N01. Die Datumszeilen der E-Mails geben Sommer-/Winterzeit passend zu den jeweiligen Daten wieder.

Ergänzend zur Sichtprüfung wurde der extrahierte PDF-Text jedes Dokuments mit sämtlichen JSON-Absätzen verglichen: nach Zusammenführung von Leerraum und Entfernung weicher Trennzeichen sind alle Absätze vollständig enthalten. Alle zwölf PDFs haben jeweils genau eine Seite. Die zwölf Originaldateien entsprechen weiterhin den Quellhashes des Renderindex; der JSON-Hash entspricht unverändert Abschnitt 1. Die nachstehenden SHA-256-Werte wurden unmittelbar aus den tatsächlich geprüften PDF-Dateien berechnet. Die in Abschnitt 5 zum ursprünglichen Prüfzeitpunkt noch ausstehende Sichtprüfung ist damit für diese zwölf Ausgaben abgeschlossen; eine Prüfung sämtlicher Releasepakete wird hierdurch nicht behauptet.

| ID | Geprüfte Seite | Ausgabe | PDF-SHA-256 |
|---|---:|---|---|
| KAUF01 | 1 von 1 | `2028-09-27_KAUF01_LE_28_061_Ich_bekomme_die_beiden_Juni_Zahlungen_nicht_zusammen.pdf` | `4a3ca859877f1d46ba1aa56ad9692a6ee40b026e7069d16781e55db426cb5133` |
| KAUF02 | 1 von 1 | `2028-09-28_KAUF02_AW_LE_28_061_Die_Suche_laeuft_bei_uns_ueber_das_Debitorenkonto.pdf` | `580c9766f97ee454d84600a2c8ba9309ebb4e1a3234f3c62c08559f86f6c53f9` |
| KAUF03 | 1 von 1 | `2028-12-14_KAUF03_Telefonnotiz_Rueckzahlung_Lichtkreis_ist_angekuendigt_Kontoeingang_noch.pdf` | `65636bf500c79f776ff0f2885be9b9bbabd21374f67a9b47e399dfdc06e0b68b` |
| KAUF04 | 1 von 1 | `2029-01-03_KAUF04_LE_28_061_Rueckfluss_im_Jahresauszug_gefunden_und_zugeordnet.pdf` | `cb5f2d8db22c9d7325bdf28e0610085582b5ec1bb00504bc2bf8e055beb66760` |
| KAUF05 | 1 von 1 | `2028-10-16_KAUF05_Wohnung_07_Bitte_IA_G_28_017_und_die_Schlussrechnung_zusammenlassen.pdf` | `d50966330b5627357c917d732c9cab35d2c0022541d16155a50057f15bbd153c` |
| KAUF06 | 1 von 1 | `2028-10-17_KAUF06_AW_Wohnung_07_Es_bleibt_bei_der_einen_Rechnungskorrektur.pdf` | `7833ca40e99daf796f5a8fe039fe0c6bd8b6fe567e9b6547054f440feaf9b09c` |
| KAUF07 | 1 von 1 | `2028-11-06_KAUF07_Telefonnotiz_Herr_Merz_zur_Wiedervorlage_fuer_die_Belagskorrektur.pdf` | `58a63180a2b042b2d2244d2ffb8dbd311f009b87bae09dc6369212f0cb772f00` |
| KAUF08 | 1 von 1 | `2029-01-04_KAUF08_IA_G_28_017_Erstattung_der_Wohnung_07_im_Projektkonto_abgeglichen.pdf` | `1f8f51799656c7eec681542e5fdbfde3b9f08f324ee2b6f372340eda677e65f8` |
| KAUF09 | 1 von 1 | `2028-03-06_KAUF09_SH_28_N01_Welche_Unterlagen_gehoeren_in_unseren_Freigabeumlauf.pdf` | `611e1170d33338b628f1e7a4b53ca8f66145c3ab3869da19fd32bb89925ad241` |
| KAUF10 | 1 von 1 | `2028-03-07_KAUF10_AW_SH_28_N01_Angebot_Auftrag_und_Aufmass_gehoeren_zusammen.pdf` | `9db29b379bacc4d28487270b73606f0941f6c8015c94dd82ae48d3fea0faf488` |
| KAUF11 | 1 von 1 | `2028-03-08_KAUF11_Telefonnotiz_Fundstellen_fuer_Rechnung_SH_28_N01_mit_Hans_Mueller_abgegl.pdf` | `6af9596fece04e8d16b405ab7155cbd5a5894d12d62720058b2e62d8af3e36fe` |
| KAUF12 | 1 von 1 | `2028-03-09_KAUF12_SH_28_N01_ist_jetzt_eindeutig_abgelegt_keine_weitere_Fassung_noetig.pdf` | `83400dade5fea5a6e181c0b484a8e8c98054434ca81bba8f95f933edc91b735e` |

Im Rahmen dieser Endprüfung wurde ausschließlich dieser Prüfvermerk ergänzt. Eingefrorene Datensätze, Originale und PDF-Ausgaben wurden nicht verändert.
