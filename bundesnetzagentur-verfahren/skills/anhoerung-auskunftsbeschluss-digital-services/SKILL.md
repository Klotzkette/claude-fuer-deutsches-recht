---
name: anhoerung-auskunftsbeschluss-digital-services
description: "Anhoerung Auskunftsbeschluss Digital Services: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anhoerung Auskunftsbeschluss Digital Services

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Anhoerung Auskunftsbeschluss Digital Services** im Plugin Bundesnetzagentur Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anhoerung-auskunftsbeschluss-fristenplan` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Anhörung Auskunftsbeschluss Fristenplan. |
| `digital-services-melde-und-abhilfeverfahren-notice-and-action` | Digital Services / Melde- und Abhilfeverfahren Notice and Action: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: DDG, DSA VO (EU) 2022/2065. |
| `eilverfahren-verwaltungsgericht-strategie` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Eilverfahren Verwaltungsgericht Strategie. |
| `energie-regulierungsakte-bbplg-leitungsvorhaben-fristen-und-besc` | BBPlG Leitungsvorhaben: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |

## Arbeitsweg

Im Plugin Bundesnetzagentur-Verfahren gilt für **Anhoerung Auskunftsbeschluss Digital Services**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anhoerung-auskunftsbeschluss-fristenplan`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Anhörung Auskunftsbeschluss Fristenplan.


# Anhörung, Auskunftsbeschluss, Fristenplan

## Zweck und Anwendungsfall
Anwaltliche Steuerung von Anhörungen und Auskunftsverlangen der Bundesnetzagentur. Die BNetzA fordert in fast jedem Verfahren strukturiert Auskünfte an: § 206 TKG (Auskunfts- und Prüfrechte), § 69 EnWG, § 45 PostG 2024, § 67 ERegG, § 18 DDG i. V. m. DSA. Daneben besteht die formale Anhörung nach § 28 VwVfG vor belastenden Verwaltungsakten. Anhörung, Auskunftsbeschluss und Verfahrensfrist greifen ineinander und müssen anwaltlich integriert geplant werden. Der Skill trägt den Fristenplan, die strategische Auswahl der Antworttiefe und die Verteidigungslinie für spätere gerichtliche Prüfung.

## Eingaben
- Beschlusskammer und Az. (BK1–BK11).
- Art des Verlangens: schriftliche Anhörung, mündliche Anhörung, formloser Fragenkatalog, Auskunftsbeschluss mit Zwangsgeldandrohung.
- Rechtsgrundlage des Verlangens (TKG, EnWG, PostG, ERegG, DDG).
- Frist (Standardfrist 2–4 Wochen, in Eilfällen kürzer).
- Vorliegende interne Unterlagen, Datenbestand, IT-Auszüge.
- Vorgeschichte (Konsultationsphase, Marktdefinition, Marktanalyse, Entgeltprüfung, Aufsichtsverfahren).

## Rechtsrahmen

- § 28 VwVfG (allgemeine Anhörung vor Verwaltungsakt; Heilung nach § 45 Abs. 1 Nr. 3 VwVfG, Unbeachtlichkeit nach § 46 VwVfG nur bei klarer Alternativlosigkeit).
- §§ 134 ff. BNetzAG, §§ 71–73 TKG, §§ 67–73 EnWG (Beschlusskammerverfahren).
- § 206 TKG (Auskunfts- und Prüfrechte BNetzA, Selbstbelastungsschutz § 206 Abs. 3 TKG, Zwangsgeld § 206 Abs. 5 TKG).
- § 69 EnWG (Auskunftsverlangen, Betretungsrechte, Mitwirkungspflicht).
- § 45 PostG 2024, § 67 ERegG (Auskunftsverlangen Post bzw. Eisenbahn).
- § 18 DDG i. V. m. Art. 67 ff. DSA (Auskunftsverlangen DSC; Befragung Art. 68 DSA; Vor-Ort-Untersuchung Art. 69 DSA).
- § 17 OWiG, nemo tenetur, § 136 StPO analog: Schutz vor Selbstbelastung in bußgeldnahen Verfahren.
- Art. 47 GRCh, Art. 6 EMRK (faires Verfahren, Selbstbelastungsschutz).
- §§ 35 ff. VwVfG (Verwaltungsakt, Begründungspflicht, Anhörungspflicht).
- § 1 Abs. 4 VwVfG (Anwendbarkeit auf BNetzA-Verfahren).

## Ablauf

1. **Frist sichern.**
 - Frist in den Kalender, Eingangsbestätigung an BNetzA.
 - Antrag auf Fristverlängerung mit konkreter Begründung (Datenmenge, Tochtergesellschaften, Konzernfreigabe).
 - Bei Konzernen: Freigabe-Kette mit Compliance, Datenschutz, Geschäftsführung.

2. **Rechtsgrundlage prüfen.**
 - Stützt sich das Verlangen auf eine taugliche Norm (TKG, EnWG, PostG, ERegG, DDG)?
 - Ist das Verfahren bereits bußgeldnah (dann § 206 Abs. 3 TKG, Selbstbelastungsschutz)?
 - Ist die Beschlusskammer im Beschlusskammerverfahren oder die Abteilung im Aufsichtsverfahren tätig?

3. **Verhältnismäßigkeit prüfen.**
 - Erforderlichkeit der Daten.
 - Bestimmtheit der Fragen.
 - Zumutbarkeit der Datenaufbereitung.
 - Bei Unbestimmtheit: Nachfrage, Eingrenzung, ggf. Stufung der Datenlieferung.

4. **Datenbestand inventarisieren.**
 - Quellen, Verantwortliche, Datenschutzfragen.
 - Geschäftsgeheimnisse identifizieren.
 - Konzernkommunikation und Anwaltskorrespondenz aussondern (Legal Privilege).

5. **Antwortstrategie wählen.**
 - Vollantwort, Teilantwort mit Schwärzung, Verweigerung mit Begründung.
 - Verweigerungen sind nur bei Selbstbelastung, fehlender Rechtsgrundlage oder Unverhältnismäßigkeit tragfähig.
 - Risiko der Beugehaft- bzw. Zwangsgeldverhängung gegen Geschäftsleitung beachten.

6. **Anhörungstext entwerfen.** Sachverhalt, Tatsachenbasis, rechtliche Bewertung, Alternativvorschläge. Klare Trennung Tatsache/Bewertung.

7. **Verteidigungslinie dokumentieren.** Was wurde gesagt, was bewusst nicht. Spätere Klage beim VG Köln stützt sich auf diese Akte.

8. **Rechtsschutz parallel.**
 - Gegen den Auskunftsbeschluss selbst ist Widerspruch (sofern nicht ausgeschlossen) und Klage zum VG Köln statthaft (§ 51 Abs. 1 Nr. 7 VwGO).
 - Aufschiebende Wirkung kann nach § 80 Abs. 5 VwGO beantragt werden, sofern nicht spezialgesetzlich ausgeschlossen (vgl. § 137 TKG, § 76 EnWG, § 79 ERegG, § 22 DDG).
 - Bei drohendem Zwangsgeld parallel Einspruch und Eilantrag.

## Mustertexte

- **Empfangsbestätigung mit Fristverlängerungsantrag (1 Seite).** Begründung mit Datenmenge, Konzernfreigabe, Urlaubszeit, Auslands-Tochtergesellschaften.
- **Strukturierte Stellungnahme nach § 28 VwVfG** mit Gliederung A. Sachverhalt, B. Rechtliche Würdigung, C. Anträge, D. Beweismittel.
- **Antwort auf Auskunftsverlangen** mit tabellarischem Antwortteil (Fragenummer, Antwort, Quelle, Schwärzung, Anlage). Begleitschreiben mit Schutzanträgen nach § 71 TKG / § 71 EnWG.
- **Eilantrag VG Köln gegen Auskunftsbeschluss** (§ 80 Abs. 5 VwGO bzw. § 123 VwGO) mit Glaubhaftmachung der irreparablen Folgen.
- **Verweigerungsschreiben mit Selbstbelastungsvorbehalt** bei bußgeldnahen Verfahren (§ 206 Abs. 3 TKG).

## Quellenpflicht
- Verweis auf aktuelle BNetzA-Verfahrensgrundsätze auf der BNetzA-Konsultationsseite.
- BNetzA-Beschluss-Az. (BK-Format) nur generisch; konkrete Beschlüsse vom Anwender zu verifizieren.
- VG Köln und BVerwG (insbesondere zu § 206 TKG und § 69 EnWG) nur mit konkretem Az., Datum und freier Fundstelle.
- Zitierweise gemäß `references/zitierweise.md`.

## Ausgabeformat

- Fristenkalender mit Eskalationspunkten (Zwischenfristen für interne Freigabe, Datenextraktion, Schwärzungsprüfung).
- Stellungnahme-Entwurf (3–10 Seiten je nach Komplexität).
- Risikomatrix für Verweigerungsstrategien (Selbstbelastung, Unverhältnismäßigkeit, Datenschutzbedenken).
- Anlagenverzeichnis mit Schwärzungs-Versionsstand.

## Beispiele

- **TK-Marktanalyse BK3.** BK3 fordert Marktdaten zum SMP-Test. Antwort: vollständige Datenlieferung unter Schwärzung der Margen, Begleitschreiben mit Bezug auf § 71 TKG.
- **Energie-Anreizregulierung BK6.** BK6 verlangt Effizienzdaten für die ARegV-Erlösobergrenze. Antwort: vollständige Lieferung mit Geheimhaltungsantrag, Bezug auf § 71 EnWG.
- **DSA-Plattform.** DSC fordert von einer Online-Plattform Algorithmen-Dokumentation nach Art. 27 DSA. Antwort: vollständige Beschreibung, Schwärzung sicherheitsrelevanter Details.
- **Eisenbahn BK10.** BK10 fordert Trassen-Anmelddaten von DB InfraGO. Antwort: Lieferung im strukturierten Format, Bezug auf § 67 ERegG.
- **Post BK10.** BK10 verlangt Briefporto-Kostenkalkulation. Antwort: Bandbreitendarstellung, Schwärzung der Margen.

## Verhältnis zu anderen Skills im Plugin

- Verzahnung mit `aktenzugang-geschaeftsgeheimnisse-schwaerzung` für Schwärzungsstrategie.
- Verzahnung mit den Sektor-Skills (TK-Marktdefinition, Energie-ARegV, ERegG-Beschwerde, DSA) für die fachliche Tiefe.
- Bei drohendem Bußgeld Übergabe an den Bußgeld-Verteidigungs-Skill im Plugin.

## Häufige Fehler

- Fristverlängerungsantrag pauschal ("Komplexität") ohne konkrete Angaben.
- Unklare Trennung zwischen Tatsache und rechtlicher Wertung in der Stellungnahme.
- Beifügung von Anlagen ohne Schwärzungsstrategie.
- Selbstbelastung in bußgeldnahen Verfahren ohne Belehrung des Mandanten.
- Zwangsgeld-Risiko unterschätzt; bei Verweigerung sind hohe Beträge je Tag möglich.

## Qualitätsgate

Vor Absendung prüfen:
- Frist gewahrt und im Kalender mehrfach gesichert?
- Vollmacht im Original?
- Konsistenz mit früheren Stellungnahmen?
- Selbstbelastungsrisiko bewertet?
- Schwärzungen begründet?
- Anlagenverzeichnis vollständig?
- Versandnachweis (Empfangsbestätigung)?

## 2. `digital-services-melde-und-abhilfeverfahren-notice-and-action`

**Fokus:** Digital Services / Melde- und Abhilfeverfahren Notice and Action: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: DDG, DSA VO (EU) 2022/2065.


# Melde- und Abhilfeverfahren ("Notice and Action") nach Art. 16 DSA

## Zweck und Anwendungsfall
Anwaltliche Arbeit am Art. 16 DSA-Verfahren ("Notice and Action"), d. h. der Pflicht von Hosting-Anbietern, leicht zugängliche und nutzerfreundliche Meldekanäle für mutmaßlich illegale Inhalte bereitzustellen und diese unverzüglich zu bearbeiten. Dieser Skill begleitet drei Rollen: (1) Hosting-Anbieter bei der Compliance-Implementierung; (2) Meldende (Verbraucher, Verbände, Rechteinhaber, Trusted Flagger) bei der Erstellung wirksamer Meldungen; (3) Beschwerdeführer bei der Anrufung der BNetzA als DSC bei mangelhafter Plattform-Bearbeitung.

## Eingaben
- Plattform-Typ (Hosting-Anbieter, Online-Plattform, VLOP).
- Konkrete Meldung (Inhalt, URL, Datum, Meldungstext, Rechtsgrundlage des Vorwurfs).
- Reaktion der Plattform (Löschung, Sperrung, Demonetarisierung, keine Reaktion, ablehnende Begründung).
- Frist (in der Praxis "unverzügliche" Bearbeitung, in der Regel 24 Stunden bis wenige Tage).
- Rolle des Mandanten.

## Rechtsrahmen
- Art. 16 DSA (Meldekanäle bei Hosting-Anbietern).
- Art. 17 DSA (Begründung von Moderationsmaßnahmen "Statement of Reasons").
- Art. 18 DSA (Meldung bei Verdacht auf Straftaten gegen Leben oder Leib).
- Art. 20 DSA (internes Beschwerdesystem der Online-Plattform).
- Art. 21 DSA (außergerichtliche Streitbeilegung).
- Art. 22 DSA (Trusted Flagger).
- Art. 23 DSA (Schutz vor Missbrauch).
- §§ 18, 19 DDG (BNetzA als DSC).
- § 7 TMG a. F. übergangsweise / DSA-konforme Auslegung; Haftungsprivilegierung Art. 5–6 DSA.
- StGB-Bezüge: §§ 130, 131, 184b, 185 ff. StGB; UrhG (insbesondere § 19a UrhG bei urheberrechtlichen Meldungen).

## Ablauf
1. **Meldung formulieren.** Erforderliche Bestandteile gem. Art. 16 Abs. 2 DSA: hinreichend begründete Erklärung der Illegalität; präzise URL-Angabe; Name und E-Mail des Meldenden (außer bei §§ 184a–b StGB-Konstellationen); Verzichtserklärung auf rechtsmissbräuchliche Verwendung.
2. **Kenntnisbegründung.** Eine ordnungsgemäße Meldung begründet "Kenntnis" der Plattform und beendet das Haftungsprivileg (Art. 6 DSA).
3. **Bearbeitungspflicht der Plattform.** "Zeitnah, sorgfältig, nicht-willkürlich, objektiv" (Art. 16 Abs. 6 DSA); konkrete Frist regulatorisch unbestimmt, faktisch wenige Tage.
4. **Begründungspflicht Art. 17 DSA.** Bei jeder Moderationsmaßnahme klare, spezifische Begründung an den betroffenen Nutzer und an die Transparenzdatenbank der EU-Kommission ("DSA Transparency Database").
5. **Beschwerdesystem Art. 20 DSA.** Plattform muss internes, kostenfreies, leicht zugängliches Beschwerdesystem mit menschlicher Überprüfung anbieten.
6. **Eskalation.** Art. 21 DSA (außergerichtliche Streitbeilegung), Art. 53 DSA (Beschwerde an DSC), Klage vor ordentlichem Gericht.
7. **Aufsichtsverfahren bei der BNetzA.** § 18 DDG-Anzeige bei systemischen Mängeln; § 19 DDG-Untersagung; Verpflichtungszusagen Art. 73 DSA.
8. **Rechtsschutz.** Plattform: VG Köln gegen Verfügung; Meldender: Zivilklage auf Unterlassung gegen Plattform (§§ 1004 BGB analog, 823 BGB).

## Mustertexte
- Meldung nach Art. 16 DSA: Identifizierung, URL, Rechtsgrundlage des Vorwurfs (StGB/UrhG/UWG), Begründung, Verzichtserklärung.
- "Statement of Reasons" nach Art. 17 DSA: Beschreibung der Maßnahme, Begründung, Hinweis auf Beschwerderecht Art. 20, Hinweis auf Art. 21-Streitbeilegung und Art. 53-Beschwerde.
- DSC-Anzeige bei systemischen Mängeln: Plattform, Belegketten (mehrere Meldungen ohne Reaktion), Anträge.

## Quellenpflicht
- DSA-Originaltext (EUR-Lex) und Leitlinien der EU-Kommission.
- Transparency Database der EU-Kommission als Belegquelle.
- BGH/EuGH-Rechtsprechung zu Hostprovider-Haftung mit Datum, Az., freier Fundstelle (z. B. EuGH C-682/18 Peterson/Cyando, BGH-Rechtsprechung zu Notice-and-Stay-Down).
- Zitierweise nach `references/zitierweise.md`.

## Ausgabeformat
- Meldungstext für den Mandanten.
- Compliance-Workflow-Diagramm für Plattformen (Eingang Meldung > Triage > Bearbeitung > Statement of Reasons > Beschwerdesystem).
- Anzeige an die BNetzA als DSC.

## Beispiele
- Rechteinhaber meldet urheberrechtsverletzendes Video. Plattform reagiert nicht binnen 7 Tagen. Klage vor LG plus DSC-Anzeige.
- Verband meldet Hassrede gegen Minderjährige. Plattform sperrt; Statement of Reasons mangelhaft. Beschwerde Art. 20 DSA, dann DSC.
- Online-Plattform optimiert Notice-and-Action-auf Compliance. Implementierungsplan inkl. Trusted-Flagger-Priorisierung.

## Qualitätsgate
Meldung enthält alle Art. 16 Abs. 2-Bestandteile? Begründung der Illegalität rechtssicher (konkrete Norm)? Transparenz-Datenbank-Eintrag erfolgt? Beschwerdeweg Art. 20 reflektiert? Frist für Folgemaßnahmen kalendarisiert?

## 3. `eilverfahren-verwaltungsgericht-strategie`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Eilverfahren Verwaltungsgericht Strategie.


# Eilverfahren beim Verwaltungsgericht in BNetzA-Sachen

## Zweck und Anwendungsfall
Strategische Steuerung verwaltungsgerichtlichen Eilrechtsschutzes gegen Maßnahmen der Bundesnetzagentur. Verwaltungsgericht ist nach § 51 Abs. 1 Nr. 7 VwGO grundsätzlich das VG Köln. Spezialgesetzlich kann das OVG Münster (z. B. § 233 TKG) oder das BVerwG (Instanzverkürzungen z. B. § 50 Abs. 1 Nr. 6 VwGO bei Leitungs-Planfeststellungen) erstinstanzlich zuständig sein. Der Skill steuert die Wahl zwischen § 80 Abs. 5 VwGO (Wiederherstellung/Anordnung der aufschiebenden Wirkung) und § 123 VwGO (einstweilige Anordnung) und die Eilantragsschrift.

## Eingaben
- Angegriffener Akt: Verwaltungsakt (Bußgeld, Untersagung, Anordnung) oder Realhandeln/Unterlassen.
- Sofortige Vollziehbarkeit angeordnet (§ 80 Abs. 2 Nr. 4 VwGO) oder kraft Gesetzes ausgeschlossene Suspensiveffekt (z. B. § 137 Abs. 1 TKG).
- Hauptsacheverfahren bereits anhängig?
- Drohender Schaden, Reversibilität, Marktwirkung, Verbraucherbezug.
- Frist (in der Regel keine starre Eilfrist, aber Rechtsschutzbedürfnis erlischt bei Untätigkeit).

## Rechtsrahmen
- § 80 Abs. 5 VwGO (Anordnung/Wiederherstellung der aufschiebenden Wirkung).
- § 80a VwGO (Drittwirkung; bei mehrpoligen Verhältnissen).
- § 123 VwGO (einstweilige Anordnung bei Verpflichtungs- oder Leistungsbegehren).
- § 137 TKG (sofortige Vollziehbarkeit von BNetzA-TK-Verfügungen), § 76 EnWG (gesetzlich angeordnete sofortige Vollziehbarkeit Energie), § 41 PostG, § 79 ERegG, § 22 DDG.
- § 47 VwGO (Normenkontrolle: in BNetzA-Sachen selten relevant).
- §§ 51 Abs. 1 Nr. 7, 49 Abs. 4 VwGO (VG Köln erstinstanzlich), § 6 ARegV.
- Spezielle Instanzverkürzungen: §§ 50, 48 VwGO; OVG Münster nach § 233 TKG; § 1 EnWG-Beschleunigungsgesetz für Energieleitungen.

## Ablauf
1. **Antragsart wählen.** Verwaltungsakt mit sofortiger Vollziehbarkeit: § 80 Abs. 5 VwGO. Verpflichtungsbegehren: § 123 VwGO. Drittangriff: § 80a VwGO.
2. **Zuständigkeit klären.** Regel: VG Köln. Besonderheit TK: ggf. OVG Münster nach § 233 TKG. Bei Planfeststellungen Energie: BVerwG.
3. **Sofortige Vollziehbarkeit prüfen.** Bei kraft Gesetzes vollziehbaren Verfügungen (z. B. § 137 TKG) genügt Verweisung; bei behördlicher Anordnung Begründungsprüfung nach § 80 Abs. 3 VwGO.
4. **Anordnungsanspruch und Anordnungsgrund.** § 123 VwGO erfordert beides; § 80 Abs. 5 VwGO erfordert Interessenabwägung mit Erfolgsaussicht in der Hauptsache.
5. **Glaubhaftmachung.** § 920 ZPO i. V. m. § 123 Abs. 3 VwGO; eidesstattliche Versicherungen, Bescheinigungen, Belegketten.
6. **Marktwirkung darstellen.** In TK/Energie/Post oft Schlüssel: irreversible Markteingriffe, Wettbewerbsverzerrungen, Investitionsentscheidungen, Versorgungssicherheit.
7. **Verbindung mit Hauptsache.** Eilantrag fördert Hauptsacheverfahren; ggf. Aussetzung des Eilverfahrens bis zur Hauptsache.
8. **Rechtsmittel.** Beschwerde zum OVG/BVerwG binnen 2 Wochen § 147 VwGO; Beschwerdebegründung nach § 146 Abs. 4 VwGO im Eilbeschluss-Verfahren strenger Substantiierungsmaßstab.

## Mustertexte
- Eilantrag § 80 Abs. 5 VwGO: Antrag, Sachverhalt, Anordnungsanspruch, Anordnungsgrund, Interessenabwägung, Bescheidkopie, eidesstattliche Versicherung.
- Eilantrag § 123 VwGO: Antrag (in Form Sicherungs- oder Regelungsanordnung), Anordnungsanspruch, Anordnungsgrund, Glaubhaftmachung.
- Drittanfechtungs-Eilantrag § 80a VwGO bei Wettbewerberverfahren.

## Quellenpflicht
- VwGO und Spezialgesetze (TKG, EnWG, PostG, ERegG, DDG) im aktuellen Stand.
- VG Köln, OVG Münster, BVerwG-Rechtsprechung mit Datum, Az., freier Fundstelle.
- Keine erfundenen Az.; verifizierbare Verfahren bevorzugen.
- Zitierweise nach `references/zitierweise.md`.

## Ausgabeformat
- Strategie-Memo (Wahl der Antragsart, Erfolgswahrscheinlichkeit, Kostenrisiko).
- Eilantragsschrift (10–25 Seiten je nach Komplexität).
- Anlagenverzeichnis (Bescheid, Glaubhaftmachungs-Anlagen, Wirtschaftlichkeits-Belege).

## Beispiele
- TK-Unternehmen erhält Untersagungsverfügung der BNetzA (BK1) zu einem Vertriebspraxisproblem. Eilantrag § 80 Abs. 5 VwGO beim VG Köln.
- Wettbewerber will Marktdefinition (BK3) sperren lassen. Drittangriff über § 80a VwGO.
- Hosting-Anbieter erhält DSC-Untersagung wegen fehlender Notice-and-Action-Schnittstelle. Eilantrag § 80 Abs. 5 VwGO.

## Qualitätsgate
Antragsart begründet gewählt? Zuständigkeit beim richtigen Gericht? Sofortige Vollziehbarkeit identifiziert? Glaubhaftmachung mit Anlagen vollständig? Beschwerdefrist § 147 VwGO im Kalender? Mandant über Kostenrisiko (Streitwert) informiert?

## 4. `energie-regulierungsakte-bbplg-leitungsvorhaben-fristen-und-besc`

**Fokus:** BBPlG Leitungsvorhaben: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG.


# Energie-Regulierungsakte: BBPlG Leitungsvorhaben — Fristen- und Bescheidanalyse

## Fachkern: Energie-Regulierungsakte: BBPlG Leitungsvorhaben — Fristen- und Bescheidanalyse
- **Spezialgegenstand:** Energie-Regulierungsakte: BBPlG Leitungsvorhaben — Fristen- und Bescheidanalyse - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** EnWG, ARegV, StromNEV/GasNEV, MsbG, EEG, KWKG, REMIT, NABEG und die einschlägige Beschlusskammerpraxis der BNetzA.
- **Spezifische Weiche:** Zerlege Netzbetreiberrolle, Erlösobergrenze/Kostenbasis, Regulierungskonto, Investitionsmaßnahme, Netzzugang, Anschlussbegehren, Bilanzkreis oder Marktmissbrauch; Zahlen müssen aus Bescheid, Datenmeldung oder Erhebungsbogen kommen.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?
