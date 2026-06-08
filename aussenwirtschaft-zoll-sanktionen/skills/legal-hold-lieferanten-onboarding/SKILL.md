---
name: legal-hold-lieferanten-onboarding
description: "Legal Hold und digitale Datenextraktion bei Exportkontroll- und Sanktionsermittlungen: Sicherung von ATLAS-Daten, ERP-Exportdaten, E-Mail-Archiven und Zollanmeldungen, DSGVO-Konformitaet der Datensicherung, eDiscovery-Anforderungen bei US-Behörden. Output: Legal-Hold-Anordnung und Datensicherungsprotokoll im Außenwirtschaft/Zoll/Sanktionen: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung."
---

# Legal Hold und Datenextraktion bei Aussenwirtschafts-Ermittlungen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- BAFA kuendigt Aussenpruefung an; Legal Hold für alle Exportdaten der letzten 5 Jahre notwendig.
- OFAC-Anfrage zu Transaktionen; US-eDiscovery-Standards und deutsches Datenschutzrecht kollidieren.
- Interne Investigation nach Hinweisgeber-Meldung; IT-forensische Sicherung vor regulaerer Loeschung noetig.

## Erste Schritte

1. Legal-Hold-Anordnung formulieren und an IT, Compliance, Archiv und betroffene Abteilungen senden.
2. Datenkategorien definieren: ATLAS-Daten, ERP-Exportmodule, E-Mails, Vertraege, EUC, Sanktionsscreening-Logs.
3. Technische Sicherungsmassnahmen einrichten: Backup-Stopp für relevante Datenbereiche.
4. DSGVO-Rechtsgrundlage für Datensicherung pruefen (Art. 6 Abs. 1 lit. c für gesetzliche Pflicht).
5. Bei US-eDiscovery: Datenschutzkonforme Transfer-Grundlage beachten (SCCs, DSGVO Art. 49).
6. Protokollierung der gesicherten Datenbestaende mit Hash-Werten für Integritaetssicherung.

## Rechtsrahmen

- **AWV § 24**: Aufbewahrungspflicht für Ausfuhrunterlagen (10 Jahre).
- **UZK Art. 51**: Aufbewahrungspflicht für Zollanmeldungen.
- **DSGVO Art. 6**: Rechtsgrundlage für Datensicherung.
- **§ 146 AO**: Buchfuehrungsunterlagen-Aufbewahrungspflicht.
- **§ 97 StPO**: Beschlagnahmefreiheit anwaltlicher Unterlagen.

## Pruef-Raster

- [ ] Legal-Hold-Anordnung alle relevante Datenkategorien erfassend?
- [ ] IT-Sicherungsmassnahmen zeitnah eingeleitet?
- [ ] DSGVO-Rechtsgrundlage für Datenzugriff geprueft?
- [ ] US-eDiscovery-Anforderungen mit deutschem Datenschutzrecht abgestimmt?
- [ ] Integritaets-Hash-Werte für gesicherte Datenbestaende erstellt?
- [ ] Aufbewahrungsfristen (AWV 10 Jahre) gegen Legal-Hold-Anforderungen abgeglichen?

## Typische Fallstricke

- Legal Hold zu spaet: regulaere Loeschroutinen haben Daten vernichtet.
- US-eDiscovery und DSGVO kollidieren direkt; ohne datenschutzkonforme Grundlage keine Uebertragung.
- Hash-Werte fehlen; Integritaet der gesicherten Daten nicht nachweisbar.
- ERP-Daten enthalten keine Exportkontroll-spezifischen Felder; separate ATLAS-Sicherung noetig.

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
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [UZK Art. 51 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [DSGVO auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679)
- [AO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/index.html)

