---
name: it-sicherheits-vergabe-bsi-it-sig-2
description: "Auf Bieterseite IT-Sicherheitsvergaben nach geltendem BSIG und NIS2 prüfen: Statusannahmen, Eignung, Gleichwertigkeit, C5 und ISO-Nachweise, SOC-Leistung, Melde-Zuarbeit, Lieferkette, Wertung, Rüge und Angebotsbelegmatrix."
---

# IT-Sicherheitsvergabe auf Bieterseite

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Ziel

Der Skill macht ein Angebot für SOC, Cloud, Software, Hosting oder Sicherheitsberatung abgabefähig und greift überzogene oder unklare Sicherheitsanforderungen rechtzeitig an. Er verwendet das seit 06.12.2025 geltende BSIG; die alten §§ 8a, 8b und 9b BSIG sind für Vergaben 2026 keine aktuelle Rechtsgrundlage.

## 1. Intake mit Freigabesperre

1. Auftraggeber, Leistungsempfänger und behaupteter BSIG-Status mit Beleg erfassen.
2. Bekanntmachung, Unterlagen, Sicherheitskonzept, Vertragsentwurf, Antwortkatalog und Rückgabeformat versionieren.
3. Jede Anforderung als Eignung, Mindestleistung, Zuschlagskriterium oder Ausführungsbedingung klassifizieren.
4. Angebots- und Rügefrist sowie Änderungen der Unterlagen minutengenau erfassen.
5. Zertifikate und Testate mit Inhaber, Scope, Standorten, Zeitraum, Aussteller und Gültigkeit prüfen.
6. Unterauftragnehmer, Cloud-Regionen, Fernzugriffe, Komponenten und Exit-Formate in einer Lieferkettenmatrix abbilden.

Keine Angebotsfreigabe, solange eine Muss-Anforderung keinem konkreten Nachweis und keiner Datei im Uploadpaket zugeordnet ist.

## 2. Rechtsrahmen 2026

| Thema | Norm | Bieterprüfung |
| --- | --- | --- |
| Einrichtungs- und Anlagenstatus | §§ 28 und 29 BSIG | Statusbehauptung und Größen-/Sektormerkmale des Leistungsempfängers belegen lassen |
| Risikomanagement | § 30 BSIG | geforderte Maßnahme auf konkretes Risiko und Leistungsgegenstand zurückführen |
| Kritische Anlagen und Angriffserkennung | § 31 BSIG | Funktionsanforderung statt bloßem Etikett SOC prüfen |
| Meldeprozess | § 32 BSIG | vertragliche Zuarbeit muss vor gesetzlichen Betreiberfristen möglich sein |
| Registrierung | § 33 BSIG | Betreiberverantwortung von Dienstleister-Zuarbeit trennen |
| Nachweis kritischer Anlagen | § 39 BSIG | behaupteten Dreijahreszyklus und konkreten Termin belegen |
| Kritische Komponenten | § 41 BSIG | keine pauschalen Herkunftsverbote oder erfundenen Genehmigungen akzeptieren |
| Eignung und Nachweise | § 122 Abs. 4 GWB, §§ 42 ff. VgV | Auftragsbezug, Verhältnismäßigkeit und Gleichwertigkeit prüfen |
| Zuschlag | § 127 GWB, § 58 VgV | Sicherheitsmehrwert muss messbar, auftragsbezogen und vorab beschrieben sein |

Adressat gesetzlicher Betreiberpflichten ist grundsätzlich die Einrichtung oder der Betreiber. Der Auftragnehmer schuldet nur die vertraglich übernommene Leistung und Zuarbeit. Eine Klausel, die ohne Abgrenzung alle gesetzlichen Pflichten auf den Bieter verlagert, wird als Kalkulations- und Transparenzrisiko markiert.

## 3. Nachweismatrix

| Anforderung | eigener Nachweis | Scope passt? | gleichwertige Alternative | Unterauftragnehmer | Angebotsdatei |
| --- | --- | --- | --- | --- | --- |
| ISO 27001 | Zertifikat plus Anlage | Organisation, Standort, Dienst | [Nachweis] | [ja/nein] | [Datei] |
| C5 | aktuelles Testat und Berichtstyp | Cloud-Leistung und Zeitraum | [Kontrollmapping] | [ja/nein] | [Datei] |
| SOC-Betrieb | Referenzbestätigung | 24/7, Quellen, OT/IT, Volumen | [Referenz] | [Rolle] | [Datei] |
| Angriffserkennung | Funktionskonzept | Erkennung, Protokollierung, Tests | [Beleg] | [Rolle] | [Datei] |
| Meldeunterstützung | Ablauf und SLA | Betreiberfreigabe möglich | [Beleg] | [Rolle] | [Datei] |

C5 ist als Testat mit Prüfungsgegenstand und Berichtszeitraum zu behandeln, nicht pauschal als Zertifikat. Bei ISO 27001 entscheidet der Zertifizierungsumfang, nicht nur das Logo. Gleichwertige Bescheinigungen sind nach den einschlägigen VgV-Regeln zu prüfen.

## 4. Angebotskonzept

Das Konzept beantwortet konkret:

- welche Log- und Telemetriequellen übernommen werden,
- wie betriebliche Technik und klassische IT getrennt überwacht werden,
- welche Erkennungsregeln, Qualitätssicherung und Tests gelten,
- wie Priorität, Eskalation, Beweissicherung und Betreiberfreigabe funktionieren,
- welche Reaktions- und Wiederanlaufzeiten tatsächlich zugesagt werden,
- wo Daten und Schlüssel liegen, wer Fernzugriff hat und wie Unterauftragnehmer wechseln,
- wie vollständiger Export, Migration und Löschung am Vertragsende nachgewiesen werden.

Jede bewertete Zusage erhält Messgröße, Nachweiszeitpunkt und verantwortliche Rolle. Marketingformulierungen ohne prüfbaren Leistungswert werden gestrichen.

## 5. Rügeprüfung

Eine Anforderung ist insbesondere zu prüfen, wenn sie

1. einen bestimmten Anbieter, ein Produkt oder ein Testat ohne Gleichwertigkeitsöffnung verlangt,
2. keinen Bezug zum dokumentierten Schutzbedarf hat,
3. bereits bei Angebotsabgabe einen Nachweis verlangt, der erst zur Leistungsausführung benötigt wird,
4. Betreiberpflichten und Auftragnehmerpflichten vermischt,
5. ein pauschales Drittstaaten- oder Komponentenverbot aus § 41 BSIG ableitet oder
6. Qualitätskriterien ohne Bewertungsstufen oder überprüfbare Daten verwendet.

Erkennbare Unterlagenfehler sind nach § 160 Abs. 3 Satz 1 Nr. 3 GWB spätestens bis zum Ablauf der Angebots- oder Teilnahmefrist zu rügen. Die Rüge benennt Unterlagenstelle, Norm, Marktauswirkung, eigenen Nachteil und eine technisch präzise Abhilfe.

## 6. Rechtsprechungsanker

- EuGH, Urteil vom 10.05.2012, C-368/10: Anforderungen mit Bezug auf Gütezeichen müssen sachlich und nachweisoffen formuliert werden; Gleichwertigkeit ist mitzudenken.
- EuGH, Urteil vom 04.12.2003, C-448/01: Zuschlagskriterien müssen überprüfbar sein; nicht verifizierbare Umwelt- oder Qualitätsversprechen tragen keine rechtssichere Wertung.
- BGH, Urteil vom 20.11.2012, X ZR 108/10: Anforderungen der Vergabeunterlagen aus Sicht eines fachkundigen Bieters objektiv auslegen; interne, nicht erkennbare Verschärfungen tragen keinen Ausschluss.

Vor Verwendung werden Volltext, Randnummer und Übertragbarkeit verifiziert. Unbestätigte Vergabekammer-Aktenzeichen werden nicht zitiert.

## 7. Output

1. Status- und Normenblatt mit Quellenstand,
2. Muss-/Soll-/Wertungs-Matrix,
3. Zertifikats-, Testat- und Lieferkettenmatrix,
4. Lückenliste mit Verantwortlichen und Frist,
5. Angebotskonzept mit messbaren Zusagen,
6. gegebenenfalls Bieterfrage oder Rüge,
7. Uploadpaket mit Dateiname, Version, Hash und Portalquittung.

## Qualitätskontrolle

- Keine aktuelle Aussage stützt sich auf §§ 8a, 8b oder 9b BSIG.
- Kein Testat wird als Zertifikat und kein SOC automatisch als System zur Angriffserkennung bezeichnet.
- Status, Schutzbedarf und konkrete Anforderung sind beweisbar verbunden.
- Gesetzliche Betreiberfristen und interne Auftragnehmer-SLA sind getrennt.
- Gleichwertigkeit, Scope und Nachweiszeitpunkt sind für jedes Sicherheitskriterium geklärt.
