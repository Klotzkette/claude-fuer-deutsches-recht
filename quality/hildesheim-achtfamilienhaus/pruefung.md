<!-- decimal-headings -->

<!-- decimal-anchor --> <a id="technische-prüfung-des-finanzpakets-hildesheim"></a>

# 1. Prüfung der Hildesheimer Bauakte

Prüfstand: 27.09.2026. Dieser Bericht betrifft die tatsächlich ausgeführten Prüfungen des Finanzpakets der fiktiven Bauakte. Er enthält keine Modellbewertung, Zertifizierung oder Zusicherung künftiger Rechtskonformität. Die folgenden Abschnitte unterscheiden die Finanzprüfung von der Prüfung der übrigen Akte und ihrer Exportfassungen.

<!-- decimal-anchor --> <a id="bestand-und-beträge"></a>

## 1.1. Bestand und Beträge

Die kanonische Zahlenquelle ist [finanzdaten.json](finanzdaten.json). Alle darin verzeichneten 79 Finanzdateien wurden auf Vorhandensein geprüft.

| Dateiformat | Anzahl |
| --- | ---: |
| PDF | 42 |
| DOCX | 2 |
| EML | 4 |
| XLSX | 3 |
| XML | 28 |
| **Gesamt** | **79** |

Es liegen 38 Kostenbelege und 46 Bewegungen des Projektkontos vor. Die 28 XML-Dateien sind strukturierte Fassungen bereits vorhandener Rechnungen bzw. einer Rechnungskorrektur; sie begründen keine weiteren Kostenpositionen. Die PDF-Datei und ihre zugehörige XML-Datei werden nur einmal in der Belegrechnung erfasst.

| Kontrollgröße | EUR |
| --- | ---: |
| Ausgangskalkulation | 3.463.770,41 |
| Rohbaunachtrag einschließlich Umsatzsteuer | 21.420,00 |
| Entgeltminderung Innenausbau einschließlich Umsatzsteuer | −2.975,00 |
| Fortgeschriebene Belegsumme | **3.482.215,41** |
| Eigenkapital und Darlehensmittel | 3.700.000,00 |
| Projektkontorest nach letzter Zahlung | **217.784,59** |

Diese Werte wurden aus den Beleg- und Zahlungsdaten sowie in der nativen Tabellenrechnung gegengeprüft. Die Unterlagen sind eine Projektmittel- und Belegkontrolle. Die Kostenbereiche übernehmen gemischte Rechnungen zunächst als ganze Belege; insbesondere enthalten die Notar- und Grundbuchbelege auch Grundschuldkosten. Die Tabellen sind keine abschließende steuerliche Zuordnung oder AfA-Bemessungsgrundlage.

<!-- decimal-anchor --> <a id="strukturierte-rechnungen"></a>

## 1.2. Strukturierte Rechnungen

Alle 28 XML-Dateien wurden mit dem offiziellen [KoSIT Validator 1.6.3](https://github.com/itplr-kosit/validator/releases/tag/v1.6.3) und der [XRechnung-Konfiguration 3.0.2 vom 31.08.2026](https://github.com/itplr-kosit/validator-configuration-xrechnung/releases/tag/v2026-08-31) geprüft. Ergebnis: **28 akzeptiert, 0 abgewiesen**. Die Berichte bestätigen für jede Datei die UBL-2.1-Schemaprüfung, die EN16931-Schematronprüfung und die XRechnung-Schematronprüfung. Die Konfiguration verwendet EN16931-Regeln 1.3.16 sowie XRechnung-Schematron 2.6.0.

Zusätzlich wurden Rechnungsnummer, Rechnungsdatum, Gutschrift-/Rechnungstyp und verbleibender Zahlbetrag mit `finanzdaten.json` abgeglichen. Bei Schlussrechnungen bleibt der strukturierte Gesamtleistungsbetrag kumuliert; die bereits vereinnahmten Abschläge werden als `PrepaidAmount` abgesetzt.

Eine nur im temporären Prüfverzeichnis angelegte Negativprobe erhöhte `PayableAmount` um 1,00 EUR. Der Validator wies diese Datei erwartungsgemäß mit **BR-CO-16** ab. Die manipulierte Datei gehört nicht zur Testakte.

SHA-256 der verwendeten Originalpakete:

- `validator-1.6.3-standalone.jar`: `799e64befca97d4080e03608c80b85dd5a5ecc5f4ae4f35d1116ec2855b9a7c9`
- `xrechnung-3.0.2-validator-configuration-2026-08-31.zip`: `2530cd107c414511c5d0462ec10f886910395abfca820db82e83d70bf01221a8`

Dies dokumentiert eine Prüfung mit dem am Prüfstand verfügbaren Regelsatz. Es wird keine unverändert geltende Validatorversion für die fiktiven Rechnungsjahre bis 2033 behauptet.

<!-- decimal-anchor --> <a id="tabellenrechnung"></a>

## 1.3. Tabellenrechnung

Die drei XLSX-Dateien wurden mit Artifact Tool erstellt, berechnet, inspiziert und gerendert. Anschließend wurden ihre Formel-Caches entfernt und die Dateien mit der gebündelten nativen LibreOffice-Laufzeit neu berechnet. Die Formeln blieben nach dem nativen Durchlauf erhalten; die nativ berechneten Werte enthalten keine Excel-Fehlerzellen.

| Arbeitsmappe | Formelzellen |
| --- | ---: |
| 120 Kostenentwicklung | 60 |
| 121 Rechnungen und Zahlungen | 204 |
| 122 Finanzierung und Vermietung | 334 |
| **Gesamt** | **598** |

Alle acht folgenden Eingabeänderungen wurden zuerst in Artifact Tool und danach erneut nach nativer LibreOffice-Neuberechnung geprüft. Die ausgelieferten Arbeitsmappen enthalten jeweils wieder den unveränderten Ausgangszustand.

| Eingabeänderung in einer Prüfkopie | Geprüftes Ergebnis |
| --- | --- |
| Belege `E27`: 200.000 auf 201.000 EUR | Kostenstand `D13`: 3.483.215,41 EUR |
| OP-Stichtag: 17.06.2028 | Saldo Elektroabschlag `E34`: 0,00 EUR |
| OP-Stichtag: 20.06.2028 | Saldo Elektroabschlag `E34`: −89.250,00 EUR |
| OP-Stichtag: 05.10.2033 | Gesamtsaldo aller offenen Posten: 0,00 EUR |
| Mietansatz Wohnung 01: 0 EUR/m² | Jahreskaltmiete: 90.984,00 EUR |
| Mietansatz Wohnung 01: leeres Feld | Liquiditätsergebnis: `offen` |
| Mietausfall: 5 Prozent | Jahresliquidität vor Ertragsteuern: −2.700,00 EUR |
| Sollzins: 4 Prozent | Erster monatlicher Zinsbetrag: 5.333,33 EUR |

Zusätzliche Basiskontrollen: Jahreskaltmiete 102.000,00 EUR, Jahresliquidität vor Ertragsteuern 2.400,00 EUR, erster monatlicher Zinsbetrag 4.800,00 EUR, Darlehensrest nach erster Annuität 1.598.000,00 EUR. Diese Ergebnisse betreffen die dokumentierten Planannahmen, keine Marktpreisfeststellung.

<!-- decimal-anchor --> <a id="dokumente-und-e-mails"></a>

## 1.4. Dokumente und E-Mails

Die 42 Finanz-PDF, die vier gerenderten DOCX-Seiten und die 22 nativen PDF-Seiten der Arbeitsmappen wurden visuell geprüft. Ein verwaister Schlussabsatz im Kostenblatt und eine weitgehend leere Schlussseite des Kontoauszugs 2027 wurden korrigiert und erneut gerendert.

Bei jeder der vier EML-Dateien wurden genau eine Absender- und eine Empfängeradresse, die `.example`-Adressdomäne, fehlerfreie MIME-Verarbeitung und die vollständige Übereinstimmung der eingebetteten Anlagen mit den jeweiligen Originaldateien geprüft.

Nach der zentralen Umstellung des Paragrafzeichens auf ausgeschriebenes „Paragraf“ wurden die Finanzbelege 072, 073, 075, 077, 078, 079 und 119 erneut gerendert und alle acht betroffenen PDF-Seiten geprüft. Die anschließend neu erzeugten EML-Dateien bestanden die Header- und Anlagenprüfung erneut. Die Rechnungsbeträge blieben unverändert.

<!-- decimal-anchor --> <a id="reproduktion-und-releasepfad"></a>

## 1.5. Reproduktion und Releasepfad

Die finanzbezogenen Prüfungen sind in [bauwirtschaft_hildesheim_finanz.py](../../scripts/bauwirtschaft_hildesheim_finanz.py) reproduzierbar. `--qa` benötigt `SOFFICE` als Pfad zu einer bereitgestellten Office-Laufzeit. `--invoice-qa` benötigt `KOSIT_JAVA` als Pfad zu Java ab Version 11 sowie `KOSIT_HOME` mit Validator-JAR und entpackter Konfiguration im Unterverzeichnis `configuration`. Standard-Prüfverzeichnis ist `/tmp/hildesheim/finanz`; die KoSIT-Dateien werden dort im Unterverzeichnis `kosit` erwartet, wenn `KOSIT_HOME` nicht gesetzt ist.

Der [Tabellengenerator](../../scripts/build-bauwirtschaft-hildesheim-workbooks.mjs) ermittelt das Repository relativ zu seiner eigenen Datei und verwendet den vorhandenen Runtime-Loader mit optionalem `AKTEN_NODE_MODULES`. Nach Entfernung des früheren persönlichen SOFFICE-Standardpfads enthalten die beiden Finanzgeneratoren und `finanzdaten.json` keine Pfade unter `/Users/`, `/home/` oder `C:\Users`. Externe Laufzeiten werden nicht als Bestandteil der Akte ausgeliefert.

Die lesende Prüfung von [.github/workflows/release-plugin-zips.yml](../../.github/workflows/release-plugin-zips.yml) ergab: Der Releaseworkflow verwendet die im Checkout vorhandenen Originale, baut daraus mit den allgemeinen PDF-/ZIP-Buildern die Downloads und ruft die Finanzgeneratoren nicht auf. Für die PDF-Konvertierung stellt der Workflow LibreOffice unter Ubuntu bereit. Die optionalen lokalen Erzeugungs- und Prüfwerkzeuge sind daher keine zusätzliche Laufzeitabhängigkeit beim Benutzen der Testakte. Diese Beobachtung ist kein Nachweis eines bereits erfolgreich abgeschlossenen GitHub-Actions-Laufs.

Lokale Detailprotokolle des ausgeführten Prüflaufs: `abschluss-qa.json`, `native-recalculation.json`, `workbook-qa.json`, `xrechnung-qa.json` und `eml-qa.json` unter `/tmp/hildesheim/finanz`. Sie enthalten unter anderem die konkreten Zellprüfungen, Eingabemutationen und Dateiprüfsummen.

## 1.7. Planung, Bau, Vermietung und Gesamtbestand

Der finale Originalbestand umfasst 198 Dateien: 101 PDF, 39 DOCX, 21 EML, drei CSV, eine TXT, 28 XML, drei XLSX und zwei PNG. Das Gesamt-PDF enthält 353 Seiten einschließlich Dokumentenregister. Alle neun HOAI-Phasen sind im [Akten-README](../../testakten/bauwirtschaft-neubau-achtfamilienhaus-hildesheim/README.md) konkret den Unterlagen zugeordnet.

Die 32 Seiten des Planungsmoduls, 45 DOCX-Seiten und 46 übrige Leseseiten des Bau- und Vermietungsmoduls, zwölf technische Prüf- und Registerseiten sowie die 19 Seiten des Erwerbs- und Freistellungsmoduls wurden visuell geprüft. Bei der Querprüfung wurden die Nordorientierung des Fensters in Wohnung 05, die Positionsnummern der sieben Angebote, die Planbezeichnungen im Portalbild und die zeitliche Übergabe des Zählerregisters berichtigt. Die Heizungs- und Elektroprotokolle enthalten konkrete Prüfabschnitte, Messbedingungen und Werte anstelle von Verweisen auf nicht gelieferte Einzelblätter.

Die sieben Planoriginale bleiben im Originalformat-ZIP A3. Für die beiden PDF-Lesefassungen werden sie auf A4 verkleinert; Maßzahlen und Text bleiben erhalten. Der Maßstabsaufdruck gilt nur bei unverändertem A3-Ausdruck der Originaldatei. Die Bilder zeigen selbst erstellte Ansichten einer fiktiven Projektablage und Korrespondenz.

Die allgemeine Dokumentqualitätsprüfung bestand für 78 erfasste Akten mit 1.806 formalen Dokumenten und 9.069 Exportdateien. Zusätzlich bestanden die Format-, CSV-, Downloadhinweis-, Frontmatter-, Marketplace-, Laufzeit- und Versionsprüfungen. Der Bauwirtschaftstest bestand mit allen 14 zugeordneten Akten und den weiterhin 29 Skills. Diese Prüfungen sind Struktur- und Konsistenzprüfungen, keine vollständige technische Bauprüfung und keine Bewertung von Modellantworten.

Die [unabhängige Hildesheim-Regression](../../scripts/test-bauwirtschaft-hildesheim.py) liest fertige Originale statt der Generatorfunktionen. Sie prüft unter anderem Kosten- und Zahlungsbrücken, die acht Mietverhältnisse, die einmalige Erfassung der XML-/PDF-Rechnungen, native Dateiinhalte, Formel-Caches, E-Mail-Anlagen sowie die Übereinstimmung der Exportarchive mit den Originalen. Office-Seitenumbrüche dürfen zwischen Betriebssystemen abweichen; Inhaltserhaltung bleibt das Prüfkriterium.


## 1.8. Finaler Archivvergleich

Die acht Prüfgruppen der Hildesheim-Regression bestanden sowohl für die lokal erzeugten Pakete als auch für eine unabhängig mit den allgemeinen Release-Buildern erzeugte Exportprobe. Verglichen wurden sämtliche 198 Originaldateien bytegenau, die Inhaltszuordnung beider PDF-Fassungen, alle Rechnungszwillinge und die Archivstruktur. Der zweisprachige Hinweis steht an erster Stelle der ZIPs; die Originalakten enthalten keine Musterlösung.

Drei absichtlich verfälschte Datenstände wurden erwartungsgemäß abgewiesen: eine um 1 EUR erhöhte Kostensumme, ein um 1 EUR veränderter Bankumsatz und eine E-Mail mit zwei Absenderadressen. Diese Prüfkopien wurden nicht in die Akte übernommen.

Das sechsseitige Gesamtregister und die vierseitige Lesefassung des fallinternen Dokumentenregisters wurden vollständig visuell kontrolliert. Eine zuvor nahezu leere fünfte Registerseite wurde durch einen kürzeren Kopf vermieden. Nach der Änderung bestanden beide Archivprüfungen erneut mit acht von acht Prüfgruppen.

## 1.9. Sichtprüfung der XML-PDF-Lesefassungen

Alle 28 zusätzlich aus den strukturierten Rechnungen erzeugten PDF-Lesefassungen wurden vollständig als Rasteransichten geprüft: 57 Seiten der Belege 080–093 und 54 Seiten der Belege 094–106 sowie 119, insgesamt **111 Seiten**. Es wurden keine abgeschnittenen Tags, Überlagerungen oder Randüberschreitungen festgestellt. Überlange XML-Zeilen werden vollständig auf Folgezeilen fortgesetzt; auch kurze Schlussseiten enthalten die End-Tags. Diese Sichtprüfung erfolgte zusätzlich zur XML-Schemavalidierung, ohne Originale zu verändern.

Ein vollständiger Textabgleich ergab für alle 28 PDF-Dateien eine exakte Übereinstimmung mit dem serialisierten Quell-XML, nachdem ausschließlich Seitenkopf, Seitenfuß und Layout-Leerzeichen entfernt wurden. Die Exportprüfung hat somit keinen verlorenen XML-Tag oder Rechnungswert gefunden. Raster, Seitenmanifeste und der Textabgleich liegen unter `/tmp/hildesheim/finanz/xml-pdf-qa`.


## 1.10. Zentraler Release-Build der Gesamtakte

Der allgemeine Gesamt-PDF-Builder ruft für diese Akte den geordneten Hildesheim-Builder auf. Der Release-Einstieg verwendet die bereits bereitgestellte native Office-Konvertierung und benötigt keinen gesonderten DOCX-Skill-Renderer. Er erzeugt atomar nur die Gesamtakte; die üblichen Release-Builder erstellen danach die beiden ZIPs.

Der tatsächliche zentrale CLI-Aufruf ohne `DOCX_RENDERER` wurde ausgeführt. Ergebnis: 353 Seiten und ein Lesezeichen für jede der 198 Originaldateien. Gegenüber der zuvor vollständig geprüften Fassung waren auf allen 353 Seiten der extrahierte Text, die Seitengeometrie und die dekodierten PDF-Inhaltsstreams identisch. Die Originale blieben unverändert. Beide erneuerten Archive bestanden die acht Regressionen erneut; die allgemeine PDF-Builder-Regression bestand ebenfalls. Die erzeugten Textverzeichnisse wurden mit der Release-Generatorfolge neu aufgebaut und blieben unverändert.
