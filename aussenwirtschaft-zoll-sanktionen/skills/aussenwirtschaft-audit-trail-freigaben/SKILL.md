---
name: aussenwirtschaft-audit-trail-freigaben
description: "Aufbau und Pflege revisionssicherer Audit-Trails für Exportkontroll-Freigaben: Dokumentationsstandards nach AWG § 14 und AWV § 24 (Aufbewahrungsfristen) sowie Anforderungen der EU-Dual-Use-VO Art. 20. Sichert Freigabeprotokolle, Screening-Logs, Genehmigungsunterlagen und Kommunikation für Prüfun..."
---

# Audit-Trail: Revisionssichere Freigabedokumentation im Aussenhandel

## Arbeitsbereich

Aufbau und Pflege revisionssicherer Audit-Trails für Exportkontroll-Freigaben: Dokumentationsstandards nach AWG § 14 und AWV § 24 (Aufbewahrungsfristen) sowie Anforderungen der EU-Dual-Use-VO Art. 20. Sichert Freigabeprotokolle, Screening-Logs, Genehmigungsunterlagen und Kommunikation für Prüfungssituationen. Output: Audit-Trail-Struktur und Dokumentationsrichtlinie. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- BAFA prüft Exporteur nach wiederholten Genehmigungsantraegen; Auditoren verlangen vollstaendigen Freigabe-Trail.
- Hauptzollamt fordert bei Aussen-prüfung lueckenlosen Nachweis für Sanktionsscreening der letzten 3 Jahre.
- Unternehmensberatung hilft KMU beim Aufbau ersttauglicher Exportkontroll-Dokumentation für ICP.

## Erste Schritte

1. Pflicht zur Aufbewahrung von Exportkontrolldokumentation nach AWV § 24 und UZK Art. 51 feststellen (in der Regel 5-10 Jahre).
2. Kategorien von Freigabedokumenten inventarisieren: Screening-Logs, Klassifizierungsdossiers, Genehmigungen, Endverwendungserklaerungen.
3. Elektronisches Ablagesystem mit Zeitstempeln und Versionierung aufbauen.
4. Freigabeprozess mit Vier-Augen-Prinzip und Unterschriftenregelung etablieren.
5. Automatische Backup- und Loeschroutinen gem. DSGVO abstimmen.
6. Regelmäßige interne Audit-Tests zum Vollstaendigkeitsnachweis einplanen.

## Rechtsrahmen

- **AWV § 24**: Aufzeichnungs- und Aufbewahrungspflichten.
- **UZK Art. 51**: Aufbewahrung zollrelevanter Unterlagen (3 Jahre + Verlaehngerung).
- **Art. 20 VO (EU) 2021/821**: Aufzeichnungspflichten des Ausfuehrers.
- **§ 14 AWG**: Auskunftspflichten und Kontrollbefugnisse der Behörden.
- **GoBD (BMF-Schreiben 2019)**: Grundsaetze ordnungsmäßiger Buchfuehrung für digitale Unterlagen.

## Prüf-Raster

- [ ] Aufbewahrungspflicht je Dokument-Kategorie bekannt und umgesetzt?
- [ ] Zeitstempel und Versionierung für alle elektronischen Dokumente sichergestellt?
- [ ] Vier-Augen-Prinzip bei Freigabeentscheidungen dokumentiert?
- [ ] Zugriffsberechtigungen und Protokollierung eingerichtet?
- [ ] Backup und Wiederherstellbarkeit getestet?
- [ ] DSGVO-Kompatibilitaet der Langzeitarchivierung sichergestellt?

## Typische Fallstricke

- Papier-Dokumente ungeschuetzt archiviert; im Prüfungsfall nicht auffindbar.
- Screening-Logs ohne Datum oder Quellangabe sind als Nachweis wertlos.
- Zugriffsberechtigungen nicht protokolliert; Manipulationsrisiko im Audit.
- Aufbewahrungsfristen je Dokumenttyp verschieden; pauschale 5-Jahres-Regel reicht nicht.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erläuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [VO (EU) 2021/821 Art. 20 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [UZK Art. 51 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [BAFA Kontrollpflichten](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
