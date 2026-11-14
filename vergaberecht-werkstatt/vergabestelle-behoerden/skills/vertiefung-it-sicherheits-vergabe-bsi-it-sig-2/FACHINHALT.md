---
name: vertiefung-it-sicherheits-vergabe-bsi-it-sig-2
description: "Auf Auftraggeberseite IT-Sicherheitsvergaben vertieft absichern: aktuelles BSIG, Anforderungsarchitektur, funktionale Angriffserkennung, Gleichwertigkeit, Qualitätswertung, Komponenten- und Lieferkette, Melde-SLA, Audit, Exit und Rügeverteidigung."
---

# Vertiefung: IT-Sicherheitsvergabe verteidigungsfest gestalten

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## 1. Anforderungskette

Jede Sicherheitsvorgabe erhält vor Veröffentlichung eine vollständige Kette:

| Risiko | Betreiberpflicht | benötigte Funktion | Vergabeebene | Nachweis | Kontrolle im Betrieb |
| --- | --- | --- | --- | --- | --- |
| [Risiko] | [§ 30/31/32/39/41 BSIG] | [konkret] | [Eignung/Mindestleistung/Zuschlag/Vertrag] | [Beleg] | [Test/KPI/Audit] |

Fehlt ein Glied, wird die Vorgabe nicht freigegeben. So verhindert die Vergabestelle, dass NIS2 oder KRITIS nur als Schlagwort für ein gewünschtes Produkt oder einen bestimmten Anbieter dient.

## 2. Rechtsstand und Verantwortlichkeit

Das seit 06.12.2025 geltende BSIG verwendet insbesondere §§ 28 bis 33, 39 und 41. Die früheren §§ 8a, 8b und 9b BSIG sind in einer 2026 veröffentlichten Vergabe keine aktuellen Normenanker. Die Vergabeakte enthält einen Stichtag und einen Link zum amtlichen Normtext.

Betreiberpflicht und Auftragnehmerleistung werden getrennt. Beispielsweise bleibt die Entscheidung über eine Meldung nach § 32 BSIG beim Normadressaten; der Auftragnehmer schuldet eine schnellere interne Information, Mindestdaten, Aktualisierung und fachliche Zuarbeit. Gleiches gilt für Registrierung und Nachweisführung.

## 3. Markterkundung und Gleichwertigkeit

Die Markterkundung nach § 28 VgV prüft mindestens drei technisch unterschiedliche Leistungsmodelle und hält fest:

- welche Anbieter und offenen Standards verfügbar sind,
- welche Zertifikate oder Testate mit passendem Scope existieren,
- welche gleichwertigen Nachweise kleinere oder neue Anbieter erbringen können,
- welcher Vorlauf für Nachweise bis Leistungsbeginn erforderlich ist,
- welche Daten- und Exit-Formate Lock-in vermeiden.

Die Ergebnisse dürfen keinem teilnehmenden Unternehmen einen Informationsvorsprung verschaffen. Vorbefassung wird durch vollständige Informationsweitergabe und angemessene Fristen neutralisiert.

## 4. Zuschlagsmatrix mit Sicherheitsmehrwert

Qualität wird nur oberhalb der Mindestleistung bewertet. Beispiel:

| Kriterium | Gewicht | Null Punkte | volle Punkte | Verifikation |
| --- | ---: | --- | --- | --- |
| Erkennungsqualität | [x] | Behauptung ohne Test | definierte Abdeckung im Testdatensatz | reproduzierbarer Test |
| Incident Response | [x] | nur Eskalationsgrafik | qualifizierte Fallbearbeitung im Szenario | Protokoll und Zeitstempel |
| Wiederanlauf | [x] | Rollen ungeklärt | belastbarer Plan mit Ressourcen | Planspiel |
| Exit und Portabilität | [x] | proprietärer Export | vollständiger offener Probeexport | Abnahmetest |

Preisformel, Qualitätsstufen und Mindestpunktzahl werden vorab festgelegt. Der Wertungsvermerk zitiert die konkrete Angebotsstelle und erklärt, warum sie eine Stufe erfüllt. Doppelte Wertung von Zertifikat oder Referenz als Eignung und Qualität wird vermieden.

## 5. Vertragsarchitektur

Der Vertrag regelt:

1. interne Meldefristen mit Sicherheitsabstand vor § 32 BSIG,
2. Mindestinhalt und sicheren Kanal jeder Vorfallinformation,
3. Audit- und Nachweisrechte einschließlich Unterauftragnehmern,
4. Schwachstellen-, Patch- und Komponentenmanagement,
5. Datenstandort, privilegierte Zugriffe und Schlüssel,
6. Wechsel von Unterauftragnehmern und kritischen Komponenten,
7. Business Continuity, Wiederanlauf und Notbetriebsunterstützung,
8. Exit, Migration, offenen Export und Löschbestätigung,
9. abgestufte Abhilfe, Kündigung und verhältnismäßige Sanktionen.

§ 41 BSIG wird risikobezogen umgesetzt. Herkunft ist ein Datenpunkt, aber kein automatischer Ausschlussgrund. Bestehende behördliche Untersagungen oder Anordnungen werden als objektive Vertragsereignisse behandelt.

## 6. Rügeantwort und Selbstkorrektur

Eine Rügeantwort enthält für jeden Punkt:

- Wortlaut der gerügten Vorgabe,
- Status- und Risikobeleg,
- Auftragsbezug und Marktprüfung,
- Gleichwertigkeitsweg,
- konkrete Wettbewerbswirkung,
- Entscheidung: Abhilfe, Teilabhilfe oder Nichtabhilfe,
- gegebenenfalls neue Fassung und angemessene Fristverlängerung.

Ist die Anforderung nicht zu verteidigen, wird sie transparent für alle Unternehmen geändert. Die Vergabestelle schützt den Wettbewerb durch rechtzeitige Selbstkorrektur, nicht durch nachträgliche Umdeutung in der Wertung.

## 7. Rechtsprechungsanker

- EuGH, Urteil vom 10.05.2012, C-368/10: technische und qualitative Anforderungen müssen den Auftragsgegenstand sachlich beschreiben und gleichwertige Nachweise zulassen.
- EuGH, Urteil vom 04.12.2003, C-448/01: Zuschlagskriterien müssen überprüfbar sein und tatsächlich kontrolliert werden können.
- BGH, Urteil vom 20.11.2012, X ZR 108/10: Anforderungen der Vergabeunterlagen aus Sicht eines fachkundigen Bieters objektiv auslegen; keine nachträgliche Verschärfung aus einem nur intern gemeinten Maßstab.

Volltext, Randnummer und Aussage werden vor Freigabe geprüft. Eine nicht verifizierte Kammerentscheidung wird nicht in Bekanntmachung, Rügeantwort oder VK-Stellungnahme zitiert.

## 8. Output

Der Skill liefert Anforderungskette, Markterkundungsvermerk, funktionales Sicherheits-LV, Nachweis- und Gleichwertigkeitsmatrix, Qualitätsleitfaden, Vertragsklauseln, Rügeantwort und verteidigungsfähigen Vergabevermerk. Jede Tabelle ist in CSV oder XLSX exportierbar und erhält stabile IDs für Legacy-Systeme und spätere Prüfprotokolle.
