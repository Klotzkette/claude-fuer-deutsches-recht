---
name: 07-verjaehrung-restschadensersatz
description: "Für Verjährung, Hemmung, Kenntnis, Altkauf, Update-Streitgegenstand oder Restschadensersatz. Datiert jede Anspruchsspur und prüft Paragraf 852 BGB samt Herstellerzufluss. Nicht für eine bloße Terminchronologie."
---

# Verjährung und Restschadensersatz

## Zweck und Anwendungsfall

Dieser Skill rechnet die Fristen, an denen Dieselfälle scheitern oder gerettet werden: Regelverjährung nach §§ 195, 199 BGB, anspruchseigene Verjährung eines tatsächlich eigenständigen Update-Schadens, kenntnisunabhängige Grenzen, Kollektivhemmung und Restschadensersatz nach § 852 BGB. Dessen Zehnjahresfrist läuft ab Entstehung des geprüften Anspruchs; zusätzlich gilt die absolute Dreißigjahresgrenze. Er ist Pflichtstation vor jeder Klagevorbereitung in Altfällen.

## Bedienmodus

Arbeite für Diesel-Geschädigte und ihre Berater. Liefere zuerst die Fristenbewertung mit Ampel, präziser Lückenliste und genau einem nächsten Schritt; höchstens drei fristrelevante Fragen. Tabelle nur bei mindestens drei vergleichbaren Anspruchsspuren oder wiederkehrenden Feldern, sonst vollständige Absätze oder kurze Liste. Schwierige Rechtsfragen an eine Rechtsanwältin oder einen Rechtsanwalt eskalieren; Anwaltszwang und RDG-Grenzen wahren.

## Erste Antwort

Die erste Antwort liefert sofort eine vorläufige, aber vollständig ausformulierte Fristenkarte mit datierter Rechnung je freigegebenem Streitgegenstand. Tabelle nur bei mindestens drei vergleichbaren Spuren oder wiederkehrenden Fristfeldern, sonst getrennte Rechenabsätze. Jedes unbekannte Datum erscheint als präzise Lücke mit benötigtem Beleg, vertretbarer Spanne und Auswirkung auf frühestes und spätestes Fristende, nie als leere Zelle. Verboten sind Theorie- und Menütexte, Werkzeug-Fehlersuche und mehr als drei Rückfragen. Bei Werkzeugausfall ohne Meldungslärm manuell rechnen.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Chronologie und Fristenkarte aus Skill 03 (Kaufdatum, Rückruf, Update, Kenntnisanhaltspunkte).
- Angaben zu historischen Musterfeststellungs- oder aktuellen VDuG-Verfahren: Verfahren, Anmeldung, Rücknahme und Registerbelege mit Datum.
- Kaufkonstellation (Neu- oder Gebrauchtwagen, Händlerkette) für die Frage, was der Hersteller erlangt hat.

## Ablauf / Checkliste

1. Vor jeder Rechnung Anspruchsidentität festlegen:

| Spur | Handlung / Lebenssachverhalt | behaupteter Schaden | Entstehung | maßgebliche Kenntnistatsachen | Streitgegenstand |
| --- | --- | --- | --- | --- | --- |
| ursprünglicher Erwerbsanspruch | Inverkehrbringen und Kauf | Erwerbsschaden | Vertragsschluss | konkrete Betroffenheit, Gegner, Klagezumutbarkeit | ursprünglich |
| Update-Folge der ursprünglichen Kausalkette | Update verwirklicht oder verlängert das Ausgangsrisiko | weiterer zurechenbarer Nachteil | Eintritt des Nachteils; kein Neustart | Folge und Zurechnung zum Ausgangsrisiko | grundsätzlich ursprünglich |
| eigenständiger Update-Anspruch | spätere eigene Update-Funktion | zusätzlicher Update-Schaden | Eintritt des Zusatzschadens | Funktion, Schaden, Schuldner | eigenständig nach Update-Gate |

2. Update-Gate anwenden: Das Update heilt den Erwerbsschaden nicht und startet dessen Verjährung nicht neu. Eine Folge kann nach `VIa ZR 419/21` Teil der ursprünglichen Kausalkette sein; nur bei eigener Update-Handlung, eigenem Schaden und Kausalität wird ein anderer Streitgegenstand freigegeben (`VII ZR 283/20` erkennt die Trennung, bejaht aber keine erneute Haftung).
3. Kenntnis für jede freigegebene Spur gesondert datieren. Für den Erwerbsanspruch: konkrete Fahrzeugbetroffenheit und Zumutbarkeit. Für den Update-Anspruch: konkrete Update-Funktion, eigener Schaden und Schuldner. Die VW-Offenlegung vom 22.09.2015 zur EA189-Umschaltlogik ist keine Kenntnis einer damals noch nicht installierten Update-Funktion. Update-Einladung und Werkstatttermin sind Indizien, kein automatischer Fristbeginn.
4. Regelverjährung nach §§ 195, 199 BGB je Anspruch rechnen: Entstehung, Kenntnis oder grob fahrlässige Unkenntnis, Schluss des maßgeblichen Jahres, Fristende und heutiger Status. Keine automatische neue Dreijahresfrist ab Update-Installation behaupten.
5. Hemmung und Neubeginn mit Normstand prüfen: für die historische VW-Musterfeststellung § 204 Abs. 1 Nr. 1a BGB a.F.; für seit 13.10.2023 erhobene Musterfeststellungs- und Abhilfeklagen § 204a Abs. 1 Satz 1 Nr. 3 und 4 BGB, §§ 46, 47 VDuG und Art. 229 § 65 EGBGB. Verfahren, Lebenssachverhalt, wirksame Anmeldung, Rücknahme und Registerbeleg tagesgenau abgleichen. Verhandlungen (§ 203 BGB) und Neubeginn (§ 212 BGB) nur anhand konkreter Tatsachen prüfen; die Update-Installation ist kein Anerkenntnis.
6. Bei verjährtem Anspruch die §-852-Spur anspruchsbezogen prüfen: unerlaubte Handlung, Entstehung dieses Schadensersatzanspruchs, zehnjährige Frist, absolute Dreißigjahresgrenze und konkretes Erlangtes. Die Zehnjahresfrist beginnt nicht erst mit Verjährung (`X ZR 83/20`). Beim ursprünglichen Gebrauchtkauf fehlt regelmäßig Herstellerzufluss (`VII ZR 365/21`); beim Neuwagen-Ersterwerb kann er begrenzt vorliegen (`VIa ZR 8/21`, `VIa ZR 57/21`). Für einen Update-Anspruch nicht den Kaufpreiszufluss wiederverwenden, sondern aus der Update-Handlung Erlangtes feststellen; fehlt es, ist § 852 insoweit rot.
7. Fristenkarte ausgeben: Je freigegebener Spur Streitgegenstand, Handlung, Schaden, Entstehung, Kenntnis, Ende nach §§ 195, 199 BGB, Hemmung oder § 212 BGB, § 852 samt Erlangtem, Beleg und Ergebnis ausformulieren. Grob fahrlässige Unkenntnis gesondert würdigen. Tabelle nur bei mindestens drei vergleichbaren Spuren oder wiederkehrenden Fristfeldern; sonst Rechenabsätze. Keine leeren Felder.

8. Gegenprobe dokumentieren: `Update nur Folgeschaden` gegen `Update eigener Anspruch`; `Kenntnis 2015` gegen `Kenntnis der späteren Funktion`; `kein neuer Schaden` gegen konkret belegte Differenzhypothese. Dieselbe Schadensposition darf nicht mehrfach zugeordnet werden.
9. Ampel und Spurempfehlung an Skill `06-anspruchstriage-fallstrategie` zurückgeben; bei streitiger Anspruchsidentität, Entstehung oder Kenntnis rote Ampel und anwaltliche Eskalation.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Jede Anspruchsgrundlage mit eigener Entstehung, Kenntnis, Hemmung, Neubeginn und Fristgrenze berechnen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Kein Fristergebnis ohne datierte Ereignistabelle, Belegstatus, Rechenweg und Prüfung der Gegenannahme.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 17.12.2020 - VI ZR 739/20 | Im EA189-Fall ist die Regelverjährung anhand der Kenntnis von der konkreten Fahrzeugbetroffenheit und der Zumutbarkeit der Klage zu bestimmen; die Wertung ist nicht schematisch auf andere Motoren oder Anspruchsgrundlagen zu übertragen. | Amtlich geprüft |
| BGH, Urt. v. 27.01.2022 - VII ZR 303/20; Urt. v. 26.09.2022 - VIa ZR 124/22 | Für die historische VW-Musterfeststellung gelten § 204 Abs. 1 Nr. 1a BGB a.F. und die damaligen Anmeldevoraussetzungen; die heutige Verbandsklagehemmung richtet sich nach § 204a BGB. | Amtlich geprüft |
| BGH, Urt. v. 06.02.2023 - VIa ZR 419/21 | Wird eine Update-Folge der ursprünglichen Kausalkette zugeordnet, beginnt die Verjährung des Erwerbsanspruchs dadurch nicht neu. | Amtlich geprüft |
| BGH, Urt. v. 02.06.2022 - VII ZR 283/20; Beschl. v. 09.03.2021 - VI ZR 889/20 | Ein eigener Update-Anspruch ist als anderer Streitgegenstand mit eigener Entstehung und Kenntnis nach §§ 195, 199 BGB zu rechnen; bloßes Update-Datum genügt nicht. | Amtlich geprüft |
| BGH, Urt. v. 10.02.2022 - VII ZR 365/21; Urt. v. 21.02.2022 - VIa ZR 8/21 und VIa ZR 57/21 | § 852 BGB setzt konkreten Herstellerzufluss voraus: beim Gebrauchtkauf regelmäßig negativ, beim Neuwagen-Ersterwerb begrenzt möglich. | Bestätigt |
| BGH, Urt. v. 28.11.2023 - X ZR 83/20 | Die Zehnjahresfrist des § 852 Satz 2 BGB beginnt mit Entstehung des ursprünglichen Schadensersatzanspruchs, nicht erst mit dessen Verjährung; zusätzlich gilt die absolute Dreißigjahresgrenze. | Amtlich geprüft |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

**Baustein 1 — Verjährungsvortrag der Klägerseite:**

Der Anspruch ist nicht verjährt. Die dreijährige Frist des § 195 BGB begann nach § 199 Abs. 1 BGB mit dem Schluss des Jahres [JJJJ], weil die Klägerin erst am [Datum TT.MM.JJJJ] durch [Ereignis, z. B. Zugang des Rückrufschreibens] Kenntnis von der konkreten Betroffenheit ihres Fahrzeugs erlangte; grob fahrlässige Unkenntnis lag zuvor nicht vor, weil [Begründung]. Die Frist endete daher frühestens mit Ablauf des 31.12.[JJJJ] und war bei Klageerhebung am [Datum TT.MM.JJJJ] nicht abgelaufen.

**Baustein 2 — Erwiderung auf die Verjährungseinrede des Herstellers:**

Die Beklagte beruft sich ohne Erfolg auf Verjährung. Die Ad-hoc-Mitteilung vom 22.09.2015 verschaffte der Klägerseite keine Kenntnis im Sinne des § 199 Abs. 1 Nr. 2 BGB, weil [dieser Anspruch die erst am [Datum TT.MM.JJJJ] bekannt gewordene Funktion betrifft / die konkrete Betroffenheit gerade dieses Fahrzeugs erst durch das Schreiben vom [Datum TT.MM.JJJJ] erkennbar wurde]; Kenntnis ist je Streitgegenstand gesondert festzustellen.
Überdies war die Verjährung vom [Datum TT.MM.JJJJ] bis zum [Datum TT.MM.JJJJ] durch die wirksame Anmeldung zur Musterfeststellungsklage gehemmt (§ 204 Abs. 1 Nr. 1a BGB a.F.); der Hemmungszeitraum von [Zahl] Tagen ist hinzuzurechnen, sodass die Frist erst am [Datum TT.MM.JJJJ] endete.

### Rechenbeispiel: Verjährung vollständig durchgerechnet

Fall: Neuwagenkauf eines EA189-Fahrzeugs am 12.03.2014 für 32.500,00 EUR; Rückrufschreiben mit konkreter Betroffenheit zugegangen am 15.02.2016; keine Anmeldung zur Musterfeststellungsklage; Thermofenster-Betroffenheit desselben Fahrzeugs erst am 05.07.2023 erkennbar. Prüfungsstichtag 24.08.2026.

1 Regelverjährung des EA189-Anspruchs (§ 826 BGB)

Entstehung mit dem Erwerb am 12.03.2014; Kenntnis am 15.02.2016; Fristbeginn nach der Jahresende-Regel des § 199 Abs. 1 BGB mit Ablauf des 31.12.2016; Fristende nach § 195 BGB mit Ablauf des 31.12.2019. Ohne Hemmung ist der Anspruch seit dem 01.01.2020 verjährt.

2 Restschadensersatz (§ 852 BGB)

Die Zehnjahresfrist des § 852 Satz 2 BGB läuft ab Entstehung des Anspruchs am 12.03.2014, nicht erst ab dessen Verjährung, und endete mit Ablauf des 12.03.2024; auf den beim Neuwagen-Ersterwerb denkbaren Herstellerzufluss kommt es nicht mehr an. Ergebnis: rote Ampel auch für § 852.

3 Getrennte Frist der Differenzschadensspur

Die Thermofensterspur hat eine eigene Kenntniszeile: Kenntnis am 05.07.2023, Fristbeginn mit Ablauf des 31.12.2023, Fristende mit Ablauf des 31.12.2026. Ergebnis-Satz: Am Stichtag ist die Differenzschadensspur unverjährt; Klage oder wirksame Anmeldung muss bis zum 31.12.2026 erfolgen, sonst kippt auch diese Spur.

### Entscheidungstabelle: Fristweiche

| Befund | Rechtsfolge / Pfad | Weiter |
| --- | --- | --- |
| Kenntnisjahr plus drei Jahre (Jahresende-Regel) nicht abgelaufen | unverjährt; Spur freigeben (§§ 195, 199 BGB) | 06, dann 13 |
| Regelfrist abgelaufen, Neuwagen-Ersterwerb, Erwerb unter zehn Jahren | §-852-Spur prüfen; Herstellerzufluss begrenzt möglich (VIa ZR 8/21, VIa ZR 57/21) | Ablauf 6, dann 06 |
| Regelfrist abgelaufen, ursprünglicher Gebrauchtkauf | § 852 regelmäßig rot; kein Herstellerzufluss (VII ZR 365/21) | 06 mit Abraten-Prüfung |
| Erwerb über zehn Jahre zurück | § 852 abgelaufen (X ZR 83/20); rote Ampel | 06 mit Abraten-Prüfung |
| Anmeldung zu Musterfeststellungs- oder VDuG-Klage belegt | Hemmung tagesgenau einrechnen (§ 204 Abs. 1 Nr. 1a BGB a.F.; § 204a BGB) | Ablauf 5 |
| eigener Update-Anspruch behauptet | eigene Entstehungs- und Kenntniszeile, kein Neustart (VII ZR 283/20, VIa ZR 419/21) | 05, dann 07 erneut |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Jede Frist mit Anspruch, Entstehungsdatum, Kenntnistatsachen, einschlägiger Normfassung, Hemmung und Berechnung ausweisen. Rechtsprechung aus `references/gepruefte-anker-dieselgate.md` und der Statusmatrix live verifizieren; § 852 nie als pauschale Zehnjahresverlängerung des vollen Schadens darstellen und den Endkundenkaufpreis nie ungeprüft mit dem Herstellerzufluss gleichsetzen.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Fristenkarte mit Normcheck, datierter Rechnung und Spurempfehlung in vollständigen, ausformulierten Sätzen; Stichwort-Skelette sind als Endprodukt unzulässig.

## Beispiele

- Eingang: Kauf 2014, Rückrufschreiben 2016, keine Anmeldung zur Musterfeststellungsklage. Kernbefund: § 826 seit 01.01.2020 verjährt, §-852-Frist 2024 abgelaufen. Erste Antwort: Fristenkarte mit zwei roten Zeilen und ausformulierter Risikodarstellung.
- Eingang: Kauf 2019, Thermofenster-Kenntnis erst 2023. Kernbefund: Differenzschadensspur unverjährt bis Ablauf des 31.12.2026. Erste Antwort: Fristenkarte mit grüner Zeile, Fristende als Wiedervorlage, Route zurück an Skill 06.
- Eingang: Anmeldung zur Musterfeststellungsklage 2018, Abmeldung 2020. Kernbefund: Hemmung nach § 204 Abs. 1 Nr. 1a BGB a.F. Erste Antwort: tagesgenau eingerechneter Hemmungszeitraum mit neuem Fristende, Baustein 2 als Erwiderungsentwurf.
