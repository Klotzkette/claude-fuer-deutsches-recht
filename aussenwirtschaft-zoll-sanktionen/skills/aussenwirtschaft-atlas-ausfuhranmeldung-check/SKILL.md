---
name: aussenwirtschaft-atlas-ausfuhranmeldung-check
description: "Für ATLAS-Ausfuhranmeldung: Qualitätscheck und Fehlerkorrektur: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# ATLAS-Ausfuhranmeldung: Qualitaetscheck und Fehlerkorrektur

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- ATLAS-Anmeldung wird mit Fehlercode H7A7 zurueckgewiesen; Exporteur weiss nicht warum.
- Zollagent stellt fest, dass Genehmigungshinweis (BAFA-Nr.) in der Anmeldung fehlt.
- Ausfuhranmeldung mit falschem Verfahrenscode (10 00 statt 10 21) erstellt; Rueckforderung droht.

## Erste Schritte

1. ATLAS-Fehlerprottokoll und MRN-Status sichten; Fehlercode-Glossar des Zolls heranziehen.
2. Pflichtfelder Anhaenge B UZK-DA prüfen: KN-Code, Ursprung, Wert, Menge, Empfaenger, Verfahren.
3. Genehmigungshinweise (BAFA-Genehmigungsnummer, Verwendungszweck) korrekt eingetragen?
4. Verfahrenscode und Unterverfahrenscode gegenueber Warenfluss und Bewilligungen prüfen.
5. Statistischer Wert und Zollwert gegenueber Rechnung abgleichen.
6. Korrekturmoeglichkeiten in ATLAS nutzen; bei Abgangsanmeldung Korrekturfenster beachten.

## Rechtsrahmen

- **UZK Art. 162-163**: Pflichtfelder und Form der Ausfuhranmeldung.
- **UZK-DA Anhang B**: Datensatz der Ausfuhranmeldung.
- **UZK-IA Art. 221-236**: Elektronische Ausfuhranmeldungspflichten.
- **§ 11a ZollVG**: Auskunftspflichten bei ATLAS-Fehler.
- **AWV § 77**: Statistikmeldepflicht (Intrastat) bei EU-internem Verbringen.

## Prüf-Raster

- [ ] Alle Pflichtfelder laut DA-Anhang B ausgefuellt?
- [ ] KN-Code und Beschreibung konsistent?
- [ ] Genehmigungsnummer korrekt und gueltiger Zeitraum?
- [ ] Verfahrenscode und Unterverfahrenscode korrekt?
- [ ] Statistischer Wert plausibel gegenueber Rechnung?
- [ ] MRN-Status und Abfertigungsergebnis geprueft?

## Typische Fallstricke

- Falscher KN-Code loest falsche TARIC-Maßnahmen und Genehmigungserfordernisse aus.
- Fehlendes Genehmigungshinweis-Feld fuehrt zur Ablehnung kontrollpflichtiger Waren.
- Verfahrenscode 10 00 bei Veredelungsgutern falsch; richtig ist spezifischer Bewilligungscode.
- Statistischer Wert muss Incoterms-bereinigter FOB-Wert sein; oft unrichtig.

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

- [UZK-DA Anhang B auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [Zoll.de ATLAS-Ausfuhr](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollanmeldung-Zollverfahren/Elektronische-Zollanmeldung/ATLAS/atlas_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [BAFA Genehmigungsdokumentation](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
