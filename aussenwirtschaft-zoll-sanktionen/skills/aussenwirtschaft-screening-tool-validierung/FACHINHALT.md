---
name: aussenwirtschaft-screening-tool-validierung
description: "Für Screening-Tool-Validierung: Trefferqualität und Audit-Readiness: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Screening-Tool-Validierung: Trefferqualitaet und Audit-Readiness

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Compliance-Abteilung muss gegenueber BAFA nachweisen, dass Screening-Tool Sanktionslisten vollstaendig abdeckt.
- Bank prüft neues Screening-System vor Go-live; Testfall-Set gesucht.
- Bestehendes Tool liefert zu viele False Positives; Schwellenwert-Kalibrierung noetig.

## Erste Schritte

1. Scope festlegen: Welche Listen soll das Tool abdecken (EU-Konsolidierte, OFAC-SDN, UN, BAFA-Embargo)?
2. Testfall-Set erstellen: Bekannte Listeneintraege, Namensvarationen, bekannte False-Positive-Faelle.
3. False-Positive- und False-Negative-Rate messen und dokumentieren.
4. Fuzzy-Match-Schwellenwert analysieren; Einfluss von Umlaut-Normalisierung und Transliteration.
5. Aktualitaet der Listen prüfen: Wie haeufig wird die Listendatenbank aktualisiert?
6. Validierungsbericht erstellen und Schwachstellen mit Korrekturmanahmen priorisieren.

## Rechtsrahmen

- **Art. 2 VO (EU) 2016/679 (DSGVO)**: Datenschutzanforderungen beim Verarbeiten von Personendaten im Screening.
- **OFAC Sanctions Compliance Guidance (2019)**: Empfehlungen zur Screening-Tool-Kalibrierung.
- **BaFin Rundschreiben 08/2021 (GW)**: Mindestanforderungen an Transaktionsmonitoring und Screening.
- **AWV § 24**: Aufbewahrungspflichten für Screening-Ergebnisse.
- **Art. 20 VO (EU) 2021/821**: Aufzeichnungspflichten für Exportkontrollentscheidungen.

## Prüf-Raster

- [ ] Alle relevanten Sanktionslisten im Tool integriert und aktuell?
- [ ] False-Positive-Rate dokumentiert und tolerierbar?
- [ ] False-Negative-Test mit bekannten Listentreffer durchgefuehrt?
- [ ] Fuzzy-Match-Schwellenwert kalibriert und begruendet?
- [ ] Update-Frequenz der Listendatenbank ausreichend?
- [ ] Audit-Dokumentation für BAFA-/BaFin-Prüfung vorhanden?

## Typische Fallstricke

- Zu hoher Fuzzy-Schwellenwert erzeugt Tausende False Positives und laehmt Operations.
- Zu niedriger Schwellenwert uebersieht Namensvarationen sanktionierter Personen.
- Testfall-Sets veraltert und decken neue Listeneintraege nicht ab.
- Transliteration aus kyrillischen oder arabischen Schriften unzureichend.

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

- [EU-Konsolidierte Finanzsanktionsliste](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0044)
- [BAFA Sanktionen und Embargos](https://www.bafa.de/DE/Aussenwirtschaft/Embargos/embargos_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
