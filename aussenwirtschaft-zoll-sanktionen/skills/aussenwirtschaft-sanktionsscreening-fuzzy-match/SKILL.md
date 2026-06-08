---
name: aussenwirtschaft-sanktionsscreening-fuzzy-match
description: "Technische und rechtliche Anforderungen an Sanktionslistenscreening mit Fuzzy-Matching: Schwellenwerte für Namensaehnlichkeit, Algorithmen (Levenshtein, phonetisch), False-Positive-Management, Dokumentation und Validierungspflicht des Screening-Tools nach EU-Sanktionsrecht. Output: Screening-Methodikbeschreibung und Validierungsprotokoll im Außenwirtschaft/Zoll/Sanktionen: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Sanktionsscreening mit Fuzzy-Match: Methodik, Schwellenwerte und Validierung

## Arbeitsbereich

Technische und rechtliche Anforderungen an Sanktionslistenscreening mit Fuzzy-Matching: Schwellenwerte für Namensaehnlichkeit, Algorithmen (Levenshtein, phonetisch), False-Positive-Management, Dokumentation und Validierungspflicht des Screening-Tools nach EU-Sanktionsrecht. Output: Screening-Methodikbeschreibung und Validierungsprotokoll. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Screening-Tool gibt 80 False Positives pro Tag aus; Compliance-Kapazitaet ueberlastet; Optimierung.
- Neues Screening-Tool wird implementiert; Validierung der Erkennungsleistung vor Go-Live.
- BAFA-Pruefung beanstandet, dass Screening-Schwellenwert zu hoch gesetzt war und Treffer verpasst wurden.

## Erste Schritte

1. Screening-Algorithmen des Tools dokumentieren (Levenshtein-Distanz, Soundex, Metaphon etc.).
2. Schwellenwerte für Namensaehnlichkeit festlegen und begruenden (z.B. 80 % als Minimum).
3. Test-Datensatz mit bekannten Treffern und bekannten Nicht-Treffern aufbauen.
4. Erkennungsleistung messen: Sensitivity (korrekte Treffer) und Specificity (False Positives).
5. Validierungsprotokoll erstellen und periodisch wiederholen (mindestens jaehrlich).
6. False-Positive-Management: eskalationsbasiertes Workflow-System.

## Rechtsrahmen

- **VO (EU) 269/2014 und 833/2014**: Bereitstellungsverbote erfordern effektives Screening.
- **BAFA-Informationssystem Sanktionen**: Anforderungen an Screening-Qualitaet.
- **GwG § 10 Abs. 1 Nr. 4**: Transaktionsmonitoring mit Namensabgleich.
- **§ 130 OWiG**: Organisationspflichtverletzung bei unzureichendem Screening.
- **AWG § 18**: Strafbarkeit bei Bereitstellung an gelistete Personen.**

## Pruef-Raster

- [ ] Screening-Algorithmen dokumentiert und begruendet?
- [ ] Schwellenwert für Fuzzy-Match definiert und schriftlich festgelegt?
- [ ] Validierungstest mit bekannten Treffern durchgefuehrt?
- [ ] False-Positive-Rate gemessen und dokumentiert?
- [ ] Validierungsprotokoll erstellt und im ICP hinterlegt?
- [ ] Periodische Re-Validierung geplant?

## Typische Fallstricke

- Zu hoher Schwellenwert (95 %) verpasst Treffer bei Schreibvarianten oder Transliterationen.
- Zu niedriger Schwellenwert erzeugt unbearbeitbare False-Positive-Last.
- Screening nur auf Name, nicht auf Geburtsdaten und Adressen; False-Negative-Risiko.
- Validierungstest fehlt; Tool wurde nie auf Erkennungsleistung geprueft.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Länder und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

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

## Output

Screening-Methodikbeschreibung, Schwellenwert-Begruendung, Validierungsprotokoll mit Sensitivity/Specificity-Kennzahlen und False-Positive-Workflow.

## Quellen

- [EU-Finanzsanktionsliste FSAP](https://eeas.europa.eu/topics/sanctions-policy/8442/consolidated-list-sanctions_en)
- [BAFA Finanzsanktionen](https://www.bafa.de/DE/Aussenwirtschaft/Finanzsanktionen/finanzsanktionen_node.html)
- [GwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/index.html)
- [VO (EU) 269/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0269)
