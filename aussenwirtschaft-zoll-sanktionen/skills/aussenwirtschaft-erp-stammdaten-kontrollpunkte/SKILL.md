---
name: aussenwirtschaft-erp-stammdaten-kontrollpunkte
description: "Exportkontroll-Kontrollpunkte in ERP-Systemen (SAP GTS, Oracle GTM): Konfiguration und Qualitaetssicherung exportkontrollrelevanter Stammdaten wie Gueterklassifizierung (ECCN/Dual-Use-Code), Embargo-Blocker, Sanktionslisten-Integration und Dokumentenabruf. Identifiziert typische Konfigurationsfeh..."
---

# ERP-Stammdaten für Exportkontrolle: Konfiguration und Qualitaetssicherung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- SAP GTS gibt bei Bestellung aus Iran keine Sperrwarnung; Konfigurationsfehler suchen.
- Gueterklassifizierungen in ERP wurden seit 2 Jahren nicht aktualisiert; Dual-Use-Liste geaendert.
- ERP-System hat veraltete Sanktionsliste; Freigabe trotz aktuellem Listentreffer.

## Erste Schritte

1. Bestandsaufnahme aller exportkontrollrelevanten Stammdaten-Felder im ERP.
2. Gueterklassifizierungs-Korrektheit prüfen: ECCN, Dual-Use-Code, ALnr (Aussenwirtschaftslistennummer).
3. Embargo-Lander-Tabelle auf Aktualitaet prüfen.
4. Sanktionslisten-Update-Prozess validieren: Frequenz und Quellenverifizierung.
5. Dokumentenablage für EUC, Genehmigungen und Screening-Ergebnisse im ERP konfiguriert?
6. Test-Szenarien für bekannte Sperr-Faelle durchfuehren und Ergebnisse protokollieren.

## Rechtsrahmen

- **Art. 20 VO (EU) 2021/821**: Aufzeichnungspflicht für Exportkontrolldokumentation.
- **BAFA-Merkblatt ICP**: Anforderungen an IT-seitige Kontrollsysteme.
- **AWV § 24**: Aufbewahrungspflichten.
- **§ 14 AWG**: Auskunftspflichten gegenueber Behörden (BAFA-Audit).
- **GoBD**: Anforderungen an digitale Buchfuehrungs- und Archivsysteme.

## Prüf-Raster

- [ ] Alle Dual-Use-Codes und ECCNs aktuell und korrekt eingetragen?
- [ ] Embargo-Länder-Tabelle tagesaktuel?
- [ ] Sanktionslisten-Update-Frequenz ausreichend (taglich/wochentlich)?
- [ ] Test-Szenarios für Sperr-Faelle bestanden?
- [ ] Dokumentenablage für EUC und Genehmigungen konfiguriert?
- [ ] Audit-Log für alle exportkontrollrelevanten ERP-Änderungen vorhanden?

## Typische Fallstricke

- Gueterklassifizierungen werden bei neuen Produkten nicht automatisch gepflegt.
- Sanktionslisten-Update abonniert, aber Importfehler nicht erkannt.
- Dual-Use-Codes nach EU-Liste-Revision (jaehrlich) nicht nachgezogen.
- Komplexe Produktkonfigurationen mit Dual-Use-Komponenten nicht als Ganzes klassifiziert.

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

- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA ICP-Merkblatt](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Interne_Compliance/interne_compliance_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
