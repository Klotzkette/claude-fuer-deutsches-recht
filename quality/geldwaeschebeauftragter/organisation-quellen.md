# Prüfung der Organisationsskills

## 1. Umfang und Stand

Stand: 08.10.2026. Bearbeitet wurden fünf neue Skills: Verpflichtung und Organisation, Risikoanalyse, KYC, wirtschaftlich Berechtigte sowie PEP/Sanktionen. Die praktische Quellenreferenz befindet sich unter [Organisation und Quellen](../../geldwaeschebeauftragter/references/organisation-quellen.md). Das [Abrufprotokoll](organisation-quellen.json) enthält URLs, bezeichnete gelesene Passagen, lokale Belegpfade und SHA-256-Werte.

Geprüft wurden amtliche GwG-Einzelnormen, Art. 90 der Verordnung (EU) 2024/1624, vier amtliche deutsche EuGH-Volltexte und die amtliche Bundesbank-FAQ mit Stand Juni 2026. Das ist eine gezielte Quellenprüfung der verwendeten Aussagen, keine Behauptung, sämtliche Geldwäscheentscheidungen des Jahres 2026 vollständig erfasst zu haben.

## 2. Abruf und tatsächliche Lektüre

Die amtlichen GwG-Seiten zu §§ 1, 2, 3, 4, 5, 6, 7, 10, 12, 14 und 23a wurden im Webwerkzeug geöffnet und im ausgegebenen Normtext gelesen. §§ 11, 15 und 50 liefen dort wiederholt in einen Timeout; dieselben amtlichen URLs waren direkt erreichbar. Ihre vollständigen Texte wurden nach korrekter Zeichensatzdekodierung gelesen. Die übrigen Normen wurden für das Quellenprotokoll ebenfalls direkt gesichert.

Bei EUR-Lex lieferte das Webwerkzeug für C-84/24, C-483/23 und C-562/20 zeitweise eine Bot-Prüfseite. Ein direkter Abruf derselben amtlichen deutschen HTML-Seiten lieferte dagegen die Urteilsvolltexte. Die Randnummern wurden aus den HTML-Tabellen extrahiert und gelesen. Eine zunächst zu umfangreiche Ausgabe wurde für EM System Rn. 112 und T Trust Rn. 55 bis 81 gezielt wiederholt, um abgeschnittene Ausgabe nicht als Lektüre zu behandeln.

## 3. Fachliche Korrekturpunkte

1. Bestellpflicht nach § 7 Abs. 1, aufsichtliche Anordnung und freiwillige organisatorische Funktion werden unterschieden. Kanzleien und beliebige Unternehmen werden nicht pauschal Banken gleichgestellt.
2. Leitungsgenehmigung der Risikoanalyse und der Sicherungsmaßnahmen nach § 4 Abs. 3 ist von Geschäftszustimmung und unabhängiger Meldungsentscheidung getrennt. § 7 Abs. 5 darf nicht durch eine Geschäftsleitungserlaubnis zur Verdachtsmeldung entwertet werden.
3. Güterhändlerstatus, Schwellen für Risikomanagement, Schwellen für besondere Sorgfaltspflichten und verdachtsbezogene Prüfung werden nicht vermischt. Verbundene Zahlungen sind anhand des Transaktionsbegriffs zu betrachten.
4. Eigene Erhebung der WB-Angaben nach § 11 Abs. 5 und deren Überprüfung nach § 12 Abs. 3 bleiben getrennt. Die Erleichterung des § 12 Abs. 3 Satz 3 wird ausdrücklich abgebildet; ein pauschaler Satz „Register reicht nie“ wurde vermieden.
5. Fiktive wirtschaftlich Berechtigte sind kein Ersatz für nicht ausgeführte Prüfungen oder vorhandene Verdachtstatsachen. Bei mittelbarer Kontrolle wird die wirtschaftliche Durchrechnungsquote nicht allein als rechtlicher Nachweis behandelt.
6. PEP ist keine Schuldzuweisung. Das Mindestintervall nach Amtsende wird nicht als automatische Entwarnung missverstanden. Besondere Risiko- und Herkunftsprüfungen richten sich nach dem jeweiligen Tatbestand des § 15.
7. Sanktionskontrolle ist nicht mit der GwG-Eigenschaft wirtschaftlich Berechtigter gleichgesetzt. Einfrieren, Bereitstellung, Unstimmigkeitsmeldung, FIU-Meldung und Sanktionsgenehmigung bleiben eigenständige Schritte.
8. Die Anwendung der AML-Verordnung ab 2027 wird als künftiger Umstellungsbedarf getrennt vom Rechtsstand 2026 dargestellt.

## 4. Gerichtliche Anker mit geprüfter Reichweite

| Entscheidung | Tatsächlich verwendete Randnummern | Trägt | Trägt nicht |
|---|---|---|---|
| EuGH 12.03.2026, C-84/24, EM System | 86 bis 93, 96 bis 97, 112 | Kontrollkriterien und widerlegbare Vermutung bei der behandelten 50-Prozent-Beteiligung; getrenntes Einfrieren | Allgemeine GwG-Quote oder unwiderlegbarer Automatismus |
| EuGH 21.05.2026, C-483/23, T Trust | 69 bis 73 | Tatsächliche Nutzungs- und Einflussbefugnisse trotz formaler Trust-Struktur | Einfrieren jedes Trusts ohne Prüfung |
| EuGH 17.11.2022, C-562/20, Rodl & Partner | 61 bis 64, 78, 82 bis 91 | Risikobezug, geeignete Dokumentation und Aktualisierung bei Bestandskunden | Verzicht auf gesetzliche KYC-Nachweise oder ignorierte Hochrisikotatbestände |
| EuGH 22.11.2022, C-37/20 und C-601/20 | 40 bis 44, 74, 83 bis 88 | Begrenzung allgemeinen Öffentlichkeitszugangs; legitime Zugänge getrennt | Wegfall von Register- oder Identifizierungspflichten |

Die Anker enthalten in Skill und Referenz ausdrücklich ihre Reichweitengrenzen. Neue Behauptungen über eine Präjudizienbindung wurden nicht aufgenommen. Die Bundesbank-FAQ wurde zur aktuellen Verwaltungssicht herangezogen; die 2026-Urteile wurden zusätzlich am Volltext gelesen.

## 5. Redaktion und Selbstprüfung

Alle fünf Dateien verwenden genau die sechs vorgesehenen Hauptabschnitte. Frontmatter enthält nur `name` und `description`; die Beschreibungen liegen unter 360 Zeichen. Die Skills benennen konkrete Produkte und Rückgaben an die Nachbarskills. Formatstandard und Ausformulierungspflicht stehen jeweils im Ausgabeabschnitt. Kein fachlich nicht geprüfter Name wird als realer Sanktions- oder PEP-Treffer ausgegeben.

| Skill | Wörter im Textkörper | Zeilen insgesamt | Beschreibung: Zeichen |
|---|---|---|---|
| verpflichtung-organisation-klaeren | 1.348 | 82 | 254 |
| risikoanalyse-massnahmen-planen | 1.421 | 88 | 255 |
| identifizierung-kyc-durchfuehren | 1.473 | 90 | 268 |
| wirtschaftlich-berechtigte-klaeren | 1.355 | 90 | 255 |
| pep-sanktionen-risiken-pruefen | 1.440 | 90 | 248 |

Die lokale Strukturprüfung bestätigte alle relativen Links dieser fünf Skills, die genau sechs Hauptabschnitte, die Frontmatter-Grenzen und weniger als 500 Zeilen je Skill. Für alle 20 gesicherten Quellen wurden SHA-256-Werte nachgerechnet; kein gespeicherter Abruf besteht aus der zuvor im Webwerkzeug gesehenen Bot-Ersatzseite.

Die fachliche Selbstprüfung wurde an den in den Skills ausgeschriebenen Fällen vorgenommen: gesplittete Barzahlungen, ungeklärte Gesamtvertretung, vier Beteiligungen von genau 25 Prozent mit besonderer Stimmrechtsabrede, Drittfinanzierung versus Treuhand, bestätigter PEP-Status mit belegter Erbschaft sowie eine nicht gelistete Gesellschaft mit gelistetem 50-Prozent-Anteilseigner. Dies ist eine redaktionelle Selbstprüfung, kein unabhängiger Modelltest. Eine gesonderte Anwendungsprobe des Gesamtplugins kann darauf aufbauen.

## 6. Bekannte Grenzen

Lokale Kammeranordnungen, konkrete Behördenbescheide, einzelne Identifizierungsverfahren und konkrete aktuelle Sanktionslisteneinträge wurden nicht pauschal vorab geprüft. Die Skills verlangen diese Prüfung dort, wo sie für die Bearbeitung entscheidend ist. Das Plugin behauptet keinen technischen Register-, Identitäts- oder Sperrvollzug, den ein angeschlossener Dienst nicht tatsächlich bestätigt hat.
