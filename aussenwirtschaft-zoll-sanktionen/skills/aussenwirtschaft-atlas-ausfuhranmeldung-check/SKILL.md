---
name: aussenwirtschaft-atlas-ausfuhranmeldung-check
description: "Qualitaetssicherung und Fehleranalyse von ATLAS-Ausfuhranmeldungen (EXA): Pruefung der Pflichtfelder nach UZK Art. 162-163 und DA Anhang B, Einreihung (KN-Code), Warenwerttaetigung, Verfahrenscodes, Lizenz- und Genehmigungshinweise sowie MRN-Status. Identifiziert typische Ablehnungsgruende in ATLAS. Output: Fehler-Korrekturliste und freigegebene Anmeldung im Außenwirtschaft/Zoll/Sanktionen: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# ATLAS-Ausfuhranmeldung: Qualitaetscheck und Fehlerkorrektur

## Arbeitsbereich

Qualitaetssicherung und Fehleranalyse von ATLAS-Ausfuhranmeldungen (EXA): Pruefung der Pflichtfelder nach UZK Art. 162-163 und DA Anhang B, Einreihung (KN-Code), Warenwerttaetigung, Verfahrenscodes, Lizenz- und Genehmigungshinweise sowie MRN-Status. Identifiziert typische Ablehnungsgruende in ATLAS. Output: Fehler-Korrekturliste und freigegebene Anmeldung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- ATLAS-Anmeldung wird mit Fehlercode H7A7 zurueckgewiesen; Exporteur weiss nicht warum.
- Zollagent stellt fest, dass Genehmigungshinweis (BAFA-Nr.) in der Anmeldung fehlt.
- Ausfuhranmeldung mit falschem Verfahrenscode (10 00 statt 10 21) erstellt; Rueckforderung droht.

## Erste Schritte

1. ATLAS-Fehlerprottokoll und MRN-Status sichten; Fehlercode-Glossar des Zolls heranziehen.
2. Pflichtfelder Anhaenge B UZK-DA pruefen: KN-Code, Ursprung, Wert, Menge, Empfaenger, Verfahren.
3. Genehmigungshinweise (BAFA-Genehmigungsnummer, Verwendungszweck) korrekt eingetragen?
4. Verfahrenscode und Unterverfahrenscode gegenueber Warenfluss und Bewilligungen pruefen.
5. Statistischer Wert und Zollwert gegenueber Rechnung abgleichen.
6. Korrekturmoeglichkeiten in ATLAS nutzen; bei Abgangsanmeldung Korrekturfenster beachten.

## Rechtsrahmen

- **UZK Art. 162-163**: Pflichtfelder und Form der Ausfuhranmeldung.
- **UZK-DA Anhang B**: Datensatz der Ausfuhranmeldung.
- **UZK-IA Art. 221-236**: Elektronische Ausfuhranmeldungspflichten.
- **§ 11a ZollVG**: Auskunftspflichten bei ATLAS-Fehler.
- **AWV § 77**: Statistikmeldepflicht (Intrastat) bei EU-internem Verbringen.

## Pruef-Raster

- [ ] Alle Pflichtfelder laut DA-Anhang B ausgefuellt?
- [ ] KN-Code und Beschreibung konsistent?
- [ ] Genehmigungsnummer korrekt und gueltiger Zeitraum?
- [ ] Verfahrenscode und Unterverfahrenscode korrekt?
- [ ] Statistischer Wert plausibel gegenueber Rechnung?
- [ ] MRN-Status und Abfertigungsergebnis geprueft?

## Typische Fallstricke

- Falscher KN-Code loest falsche TARIC-Massnahmen und Genehmigungserfordernisse aus.
- Fehlendes Genehmigungshinweis-Feld fuehrt zur Ablehnung kontrollpflichtiger Waren.
- Verfahrenscode 10 00 bei Veredelungsgutern falsch; richtig ist spezifischer Bewilligungscode.
- Statistischer Wert muss Incoterms-bereinigter FOB-Wert sein; oft unrichtig.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
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
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

Fehler-Korrekturliste mit Feld-Referenz und Korrekturvorschlag, freigegebene Anmeldungs-Datei und Freigabe-Protokoll fuer Compliance.

## Quellen

- [UZK-DA Anhang B auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [Zoll.de ATLAS-Ausfuhr](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollanmeldung-Zollverfahren/Elektronische-Zollanmeldung/ATLAS/atlas_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [BAFA Genehmigungsdokumentation](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
