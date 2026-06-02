# Beamtenrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`beamtenrecht`) | [`beamtenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/beamtenrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Dr. Ottilie Mondsee und die verschwundene R-Besoldung** (`beamtenrecht-richterlaufbahn-besoldung-mondsee`) | [Gesamt-PDF lesen](../testakten/beamtenrecht-richterlaufbahn-besoldung-mondsee/gesamt-pdf/beamtenrecht-richterlaufbahn-besoldung-mondsee_gesamt.pdf) | [`testakte-beamtenrecht-richterlaufbahn-besoldung-mondsee.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-beamtenrecht-richterlaufbahn-besoldung-mondsee.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Beamtenrecht für Bund, Länder und Richterdienst: Status, Laufbahn, Besoldung, Versorgung, Konkurrentenstreit, Disziplinarrecht, Dienstunfähigkeit, Richterlaufbahn, Landesrecht und verständliche Mandatsführung.

## Wofür dieses Plugin da ist

Dieses Plugin führt durch beamtenrechtliche und richterdienstrechtliche Mandate: vom ersten Behördenbrief über Bewerbungs- und Konkurrentenstreit, Ernennung, Probezeit, Beurteilung, Beförderung, Umsetzung, Nebentätigkeit, Dienstunfähigkeit, Versorgung, Besoldung, Disziplinarverfahren und Richterlaufbahn bis zum gerichtlichen Eilrechtsschutz.

Der Einstieg ist bewusst freundlich: Das Plugin fragt zuerst, ob es um Bund, Land, Kommune, Gericht, Schule, Polizei, Hochschule, Finanzverwaltung, Justizvollzug, Feuerwehr, Ministerium oder Richterdienst geht. Danach klärt es Status, Amt, Dienstposten, Fristen, vorhandene Bescheide, gewünschtes Ergebnis und ob eine Anfängerführung gewünscht ist.

## Typischer Workflow

1. **Kaltstart:** Wer fragt, in welchem Dienstverhältnis, welches Bundesland, welcher Bescheid, welche Frist, welches Ziel?
2. **Status sauber trennen:** Beamter, Richter, Tarifbeschäftigter, Wahlbeamter, Professor, Anwärter, Referendar, Soldat oder Mischfall.
3. **Normen live prüfen:** Bundesrecht über gesetze-im-internet.de; Landesrecht über die amtlichen Landesportale; Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
4. **Spezial-Skill wählen:** Das Plugin schlägt passende Spezial-Skills vor und erklärt, was sie liefern.
5. **Output bauen:** Mandantenbrief, Widerspruch, Eilantrag, Konkurrentenstreit-Memo, Remonstration, Disziplinarstrategie, Besoldungs-/Versorgungsnotiz, Beihilfe-Anfrage oder Behördenanschreiben.
6. **Red-Team:** Fristen, Zuständigkeit, Landesrecht, Begründungstiefe, Beweislast, Personalaktenlage und taktische Nebenwirkungen prüfen.

## Vertiefungsmodule Beamten- und Richterrecht

Seit v60.0.1 ist das Plugin deutlich tiefer auf vier besonders fehleranfällige Bereiche zugeschnitten:

| Modul | Was es leistet | Typische Ausgaben |
| --- | --- | --- |
| Amtsangemessene Alimentation | BVerfG-Linie 2015/2020/2025, Mindestabstand, Prekaritätsschwelle, Familienalimentation, zeitnahe Geltendmachung | Widerspruch, Nachzahlungsantrag, Vorlageanregung, Jahresmatrix |
| Föderalismus und Rechtsquellen | Bund/Land/Richter/Kommune sauber trennen, BeamtStG/BBG/Landesrecht nicht verwechseln | Rechtsquellenlandkarte, Normenampel, Landesrechtsroute |
| Disziplinarrecht und Suspendierung | BDG 2024, Vollzugsmodell, § 13, § 38, § 63 BDG, Verfassungstreue und Chatgruppen | Disziplinarverfügung, Verteidigungsstellungnahme, Eilantrag |
| Richterrecht | Art. 97 GG, DRiG, Dienstaufsicht, Richterdienstgericht, Bundesrichterwahl, EU-Justizunabhängigkeit | Rechtswegmemo, Prüfungsverfahren, Auswahlvermerk-Check, Vorlagefrage |

Jeder dieser Skills ist bewusst praktisch: Er fragt zuerst die Akte ab, benennt dann die richtige Rechtsquelle und baut erst danach den Text. Wo eine Fundstelle nicht frei überprüfbar ist, stoppt das Plugin und verlangt Live-Verifikation.


## Spezialprobleme aus PR #205

Die 50 Spezial-Skills aus dem Seitenast `claude/review-german-law-skills-9LH3E` sind in dieses Plugin konsolidiert worden. Sie ergänzen die v60.0.1-Vertiefungen um neun Praxiscluster: Konkurrentenschutz und Beurteilung, Besoldung, Versorgung, Beihilfe/Heilfürsorge, Urlaub/Elternzeit, Dienstunfall/Krankheit, Disziplinarrecht, Nebenpflichten/Statusrecht und Richterrecht. Das frühere Seitenast-Plugin `beamten-richter-spezialprobleme` wird nicht als eigenes Marketplace-Plugin geführt, damit Nutzerinnen im Beamtenrecht nicht zwischen zwei fast gleichen Downloads wählen müssen.

## Quellenanker

- Bundesbeamtengesetz (BBG), Beamtenstatusgesetz (BeamtStG), Bundesbesoldungsgesetz (BBesG), Beamtenversorgungsgesetz (BeamtVG), Bundesdisziplinargesetz (BDG), Verwaltungsgerichtsordnung (VwGO), Deutsches Richtergesetz (DRiG).
- Landesbeamtengesetze, Landeslaufbahnrecht, Landesbesoldungsrecht, Landesdisziplinarrecht und Landesrichtergesetze immer über amtliche Landesquellen aktualisieren.
- Art. 33 Abs. 2 und 5 GG als Leitplanken für Bestenauslese und hergebrachte Grundsätze des Berufsbeamtentums.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Rechtsprechung nur nach Live-Check oder mit deutlicher Quellenunsicherheit.

## Skill-Schwerpunkte

| Gruppe | Inhalt |
| --- | --- |
| Einstieg und Anfängerführung | Kaltstart, Statusklärung, Landesrechtsrouting, Fristen, Aktenstruktur, verständliche Mandantenkommunikation |
| Status und Laufbahn | Ernennung, Probezeit, Lebenszeit, Laufbahnwechsel, Beurteilung, Beförderung, Versetzung, Abordnung, Umsetzung |
| Besoldung und Versorgung | Bund/Länder, Alimentation, Familienzuschlag, Professoren- und Richterbesoldung, Dienstunfähigkeit, Dienstunfall, Beihilfe |
| Rechtsschutz | Widerspruch, Klage, einstweiliger Rechtsschutz, Konkurrentenstreit, Personalakte, Akteneinsicht, Verfahrensstrategie |
| Pflichten und Disziplinarrecht | Remonstration, Treuepflicht, Mäßigung, Nebentätigkeit, Korruption, vorläufige Dienstenthebung, Strafverfahren-Schnittstelle |
| Richterrecht | DRiG, Richter auf Probe, Lebenszeit, Präsidialrat, Dienstaufsicht, richterliche Unabhängigkeit, Richterbeurteilung |

## Arbeitsstil

Das Plugin soll die Nutzerin nicht klein machen, sondern schneller stark machen: Es erklärt Fachbegriffe, benennt taktische Optionen, zeigt die nächste sinnvolle Frage und hält die Ausgabe knapp genug, damit man damit wirklich arbeiten kann.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 125 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agg-gleichstellung-und-frauenvertretung` | AGG, Gleichstellung, Frauenvertretung, Diversität und diskriminierungsfreie Auswahl im öffentlichen Dienst. |
| `agg-vs-9-bbg-auswahlverfahren` | Skill zum Verhaeltnis von AGG-Diskriminierungsschutz und beamtenrechtlichem Bewerbungsverfahrensanspruch nach § 9 BBG bzw. § 9 BeamtStG. Klaert Anwendbarkeit der AGG-Vorschriften auf Auswahlverfahren der oeffentlichen Hand Beweislastrege... |
| `aktenstruktur-und-dokumentenintake` | Sortiert Bescheide, Beurteilungen, Ausschreibungen, Auswahlvermerke, Personalaktenauszüge, ärztliche Gutachten, Beihilfebescheide und Disziplinarakten. |
| `allgemein` | Einstieg, Kaltstart und Workflow-Routing im Beamtenrecht-Plugin: klärt Status, Dienstherr, Bundesland, Frist, Ziel, Unterlagen, Anfänger-/Profi-Modus und schlägt passende Spezial-Skills vor. |
| `altersteilzeit-93-bbg-blockmodell` | Skill zur Altersteilzeit der Beamten nach § 93 BBG bzw. § 9 BeamtStG i.V.m. den Landesregelungen. Klaert die zwei Modelle Teilzeitmodell und Blockmodell die Bezuegehoehe waehrend Aktiv- und Freistellungsphase die Auswirkungen auf das Ruh... |
| `amtsangemessene-alimentation` | Amtsangemessene Alimentation: Mindestabstand, Familienzuschläge, Nachzahlung, Widerspruch und Musterverfahren. |
| `amtsangemessene-alimentation-bverfg` | Skill zur Pruefung der amtsangemessenen Alimentation der Beamten Richter und Soldaten nach Art. 33 Abs. 5 GG. Skill arbeitet das fuenfstufige Pruefungsschema des BVerfG ab mit den Indikatoren Tarifabstand Preisentwicklung Versorgungsempf... |
| `amtsangemessene-beschaeftigung` | Amtsangemessene Beschäftigung und Unterbeschäftigung: Statusamtgerechte Aufgaben, Degradierungsgefühl, Organisationsgewalt. |
| `anfaenger-modus-beamtenrecht` | Anfängerführung für Beamte, Richter, Bewerber und Anwälte: erklärt Begriffe, Verfahrenswege und typische Denkfehler ohne juristische Überwältigung. |
| `anforderungsprofil-konstitutiv-deklaratorisch` | Skill zur Unterscheidung konstitutives Anforderungsprofil und deklaratorisches Anforderungsprofil bei der beamtenrechtlichen Auswahlentscheidung. Klaert wann ein im Anforderungsprofil aufgestelltes Merkmal die Vergleichsbasis verengt und... |
| `anlassbeurteilung-vs-regelbeurteilung` | Klaert das Verhaeltnis von Regelbeurteilung und Anlassbeurteilung im Auswahlverfahren des oeffentlichen Dienstes. Skill pruef Beurteilungsstichtag Aktualitaet der Beurteilungsgrundlage und Vergleichbarkeit der konkurrierenden Beurteilung... |
| `anrechnung-55-beamtvg-mehrere-renten` | Skill zur Anrechnungsregelung von Renten auf die Beamtenversorgung nach § 55 BeamtVG. Klaert das Zusammenwirken der Beamtenversorgung mit gesetzlicher Rente Altersrente Erwerbsminderungsrente sowie Renten aus berufsstaendischer oder zwis... |
| `anwaltliche-mandatsstrategie-beamtenrecht` | Mandatsstrategie im Beamtenrecht: leise Lösung, Widerspruch, Eilverfahren, Presse-/Personalratsrisiken und Vergleich. |
| `arbeitszeit-mehrarbeit-und-ruhezeiten` | Arbeitszeit, Mehrarbeit, Bereitschaftsdienst, Ruhezeiten und Zeitausgleich. |
| `auslandsdienstbezuege-bbesg` | Skill zu Auslandsdienstbezuegen im Auswaertigen Dienst und in der Auslandsverwendung. Klaert Auslandszuschlag Kaufkraftausgleich Mietzuschuss Auslandskinderzuschlag Bewertung der Auslandsdienstpostenkategorie und Bezuege bei Hardship-Pos... |
| `auswahlgespraech-dokumentationspflicht` | Skill zu Anforderungen an strukturierte Auswahlgespraeche und Assessment Center im beamtenrechtlichen Auswahlverfahren. Klaert die Dokumentationspflicht das Erfordernis gleicher Bedingungen fuer alle Bewerber die Beweislast bei Gespraech... |
| `beamtstg-bbg-landesrecht-abgrenzung` | Trennt BeamtStG, BBG, Landesbeamtengesetze und kommunale Sonderregeln; verhindert falsche Normenwahl bei Status, Pflichten, Versetzung, Entlassung und Dienstvergehen. |
| `beforderung-und-erprobung` | Beförderung, Erprobung, Sperrzeiten, Wartezeiten und Beförderungsdienstposten. |
| `begrenzte-dienstfaehigkeit-27-bbg` | Skill zur begrenzten Dienstfaehigkeit nach § 27 BBG bzw. § 27 BeamtStG. Klaert die Voraussetzungen fuer die Reduzierung der Arbeitszeit anstatt Versetzung in den Ruhestand das Verhaeltnis zu § 26 BBG Dienstunfaehigkeit die Bezuegehoehe b... |
| `begrenzte-dienstfaehigkeit-und-reaktivierung` | Begrenzte Dienstfähigkeit, Wiedereingliederung, Reaktivierung und Untersuchungsanordnung. |
| `beihilfe-chronische-krankheit` | Skill zur Beihilfe bei schwerer chronischer Krankheit nach den Beihilfeverordnungen des Bundes und der Laender. Klaert Definition chronische Krankheit Belastungsgrenze und Eigenbehalt Befreiung von Zuzahlungen Pflegestufe und Pflegegrad... |
| `beihilfe-heilbehandlung-ausland` | Skill zur beamtenrechtlichen Beihilfefaehigkeit von Heilbehandlung im Ausland nach BBhV und den Landesbeihilfeverordnungen. Klaert die Konstellationen geplante Behandlung im EU-Ausland Notfallbehandlung Beihilfehoehe und Begrenzung auf d... |
| `beihilfe-implantatfaehige-hoergeraete` | Skill zur Beihilfefaehigkeit von hochwertigen Hilfsmitteln wie implantatfaehigen Hoergeraeten Cochlea-Implantaten elektronischen Sehhilfen orthopaedischen Spezialschuhen und Prothesen. Klaert das Erstattungsmodell unter der BBhV und den... |
| `beihilfe-und-heilfuersorge` | Beihilfe, Heilfürsorge, Erstattungsbescheid, Fristen und medizinische Notwendigkeit. |
| `besoldung-bund-bbesg` | Bundesbesoldung nach BBesG: Grundgehalt, Stufen, Zulagen, Familienzuschlag, Rückforderung und Verlust der Besoldung. |
| `besoldung-bverfg-dreischritt-2025` | Vertiefung amtsangemessene Alimentation nach Art. 33 Abs. 5 GG: BVerfG-Linie 2015/2020/2025, Mindestabstand, Prekaritätsschwelle, Drei-Schritt-Prüfung, Reparaturgesetz und Output für Widerspruch, Vorlageanregung und Mandantenmemo. |
| `besoldung-laender-check` | Länderbesoldung: Landesbesoldungsgesetz, Stufen, Sonderzahlungen, Familienzuschläge und landesspezifische Abweichungen. |
| `besoldung-verfassungswidrig-a-besoldung` | Skill zur Geltendmachung verfassungswidriger A-Besoldung im Land. Pruefschema fuer den Verstoss gegen die amtsangemessene Alimentation in der A-Besoldung unter Beruecksichtigung des Mindestabstandsgebots zum sozialhilferechtlichen Grunds... |
| `besoldung-versorgung-familienzuschlag` | Überträgt Alimentationsfragen vorsichtig auf Versorgungsempfänger, Hinterbliebene, kinderreiche Beamtenfamilien und Familienzuschlag-Rückforderungen, mit ausdrücklicher Unsicherheits- und Landesrechtsprüfung. |
| `besoldung-zeitnahe-geltendmachung-und-musterverfahren` | Besoldungsnachzahlung praktisch sichern: zeitnahe Geltendmachung, Widerspruch, Antrag, Musterverfahren, Ruhendstellung, Verjährung, Haushaltsjahrlogik und sichere Mandantenkommunikation. |
| `bestenauslese-art-33-ii-gg` | Bestenauslese nach Art. 33 Abs. 2 GG: Eignung, Befähigung, fachliche Leistung, Anforderungsprofil und Auswahlvermerk. |
| `beurteilungsbeitrag-heilung-maengel` | Skill zur rechtlichen Pruefung von Beurteilungsbeitraegen Dritter im beamtenrechtlichen Beurteilungsverfahren. Klaert wer einen Beitrag liefern muss wann ein fehlender Beitrag die Beurteilung rechtswidrig macht und wie eine fehlende Hera... |
| `bindungswirkung-strafurteil-23-bdg` | Skill zur Bindungswirkung des rechtskraeftigen Strafurteils im Disziplinarverfahren nach § 23 BDG und den Landesdisziplinargesetzen. Klaert den Umfang der tatsaechlichen Feststellungen den Loesungsbeschluss bei Anhaltspunkten fuer Fehler... |
| `bverfg-resilienz-und-bundesverfassungsgerichtswahl-2024-2025` | Resilienz des Bundesverfassungsgerichts: Art. 93/94 GG, BVerfGG, Wahlblockaden, Selbstvorschlagsmechanismus, institutionelle Sicherung und Bedeutung für Richterrecht und Justizverfassung. |
| `dienstgericht-richter-disziplinar-63-drig` | Skill zum Dienstgericht fuer Richter nach §§ 61 ff. DRiG und den Landesrichtergesetzen. Klaert die Zustaendigkeit des Dienstgerichts in Statussachen Disziplinarsachen und Versetzungs- und Pruefverfahren die Besetzung des Spruchkoerpers m... |
| `dienstliche-beurteilung-angriff` | Dienstliche Beurteilung angreifen: Beurteilungsmaßstab, Beurteilerzuständigkeit, Beiträge, Plausibilität, Quoten und Nachzeichnung. |
| `dienstpflichten-treue-maessigung-neutralitaet` | Dienstpflichten: Treuepflicht, Mäßigung, Neutralität, Wahrheitspflicht, Amtsverschwiegenheit und Social Media. |
| `dienstunfaehigkeit-amtsaerztliches-gutachten` | Skill zum amtsaerztlichen Gutachten im Verfahren der Dienstunfaehigkeit. Klaert die Mitwirkungspflicht des Beamten an der Untersuchung den Vorrang des amtsaerztlichen Gutachtens vor dem Privatgutachten die Anforderungen an Begruendung un... |
| `dienstunfaehigkeit-zurruhesetzung` | Dienstunfähigkeit und Zurruhesetzung: Prognose, amtsärztliches Gutachten, anderweitige Verwendung, Beteiligung und Rechtsschutz. |
| `dienstunfall-anerkennung` | Dienstunfall, Wegeunfall, psychische Dienstunfallfolgen und Unfallfürsorge. |
| `dienstunfall-anerkennung-45-beamtvg` | Skill zur Anerkennung von Dienstunfaellen nach § 31 BeamtVG und zur Einhaltung der Meldefristen nach § 45 BeamtVG. Klaert den Begriff des Dienstunfalls die Konstellation Wegeunfall die Behandlung von Spaetfolgen die Zwei-Jahres-Frist und... |
| `dienstvergehen-ausser-dienst-47-beamtstg` | Skill zur disziplinarrechtlichen Beurteilung von Verhalten ausserhalb des Dienstes nach § 47 BeamtStG bzw. § 77 BBG. Klaert die Voraussetzung der Eignung zur Beeintraechtigung des Vertrauens den Bezug zur Statusrelevanz und das Verhaeltn... |
| `disziplinar-bemessung-13-bdg-stufenfolge` | Maßnahmebemessung im Disziplinarrecht: § 13 BDG, Schwere des Dienstvergehens, Vertrauensverlust, Persönlichkeitsbild, Entlastung, Milderung, Zeitablauf und Stufenfolge. |
| `disziplinarmassnahmebemessung-13-bdg` | Skill zur Bemessung der Disziplinarmassnahme nach § 13 BDG und den Landesdisziplinargesetzen. Klaert die Stufen Verweis Geldbusse Kuerzung der Dienstbezuege Zuruecksstufung Entfernung aus dem Beamtenverhaeltnis. Pruef die Bemessungskrite... |
| `disziplinarrecht-bdg-2024-vollzugsmodell` | Bundesdisziplinarrecht nach der BDG-Novelle 2024: Vollzugsmodell, Disziplinarverfügung, Entfernung, Rechtsschutz, fehlende automatische Suspensivwirkung, Verfassungstreue und Verfahrensbeschleunigung. |
| `disziplinarrecht-bund-bdg` | Bundesdisziplinarrecht nach BDG: Dienstvergehen, Ermittlungsverfahren, Disziplinarverfügung, Klage und Maßnahmebemessung. |
| `disziplinarrecht-laender` | Länderdisziplinarrecht: landesspezifische Verfahren, Maßnahmen und Rechtsschutz. |
| `einstweiliger-rechtsschutz-vwgo` | Einstweiliger Rechtsschutz: § 80, § 80a, § 123 VwGO, Sicherungsanordnung und Regelungsanordnung. |
| `elternzeit-versorgungsanwartschaft` | Skill zur Elternzeit der Beamten und ihren Auswirkungen auf Versorgungsanwartschaft Stufenaufstieg und Beihilfeberechtigung. Klaert die Beruecksichtigung der Kindererziehungszeiten im Ruhegehalt die Frage des ruhegehaltfaehigen Charakter... |
| `entfernung-aus-dem-beamtenverhaeltnis-unterhalt` | Skill zur Entfernung aus dem Beamtenverhaeltnis als schaerfster Disziplinarmassnahme und zum Anspruch auf Unterhaltsbeitrag. Klaert das Verhaeltnis von Statusverlust und Versorgungsverlust den Anspruch auf Unterhaltsbeitrag nach § 10 BDG... |
| `entlassung-und-statusbeendigung` | Entlassung, Verlust der Beamtenrechte, Altersgrenze, einstweiliger Ruhestand und Statusbeendigung. |
| `erholungsurlaub-verfall-eugh-c518-20` | Skill zum Verfall des Erholungsurlaubs im Beamtenverhaeltnis nach Massgabe der EuGH-Rechtsprechung Schultz-Hoff und Folgesachen. Klaert die Voraussetzung der Mitwirkungsobliegenheit des Dienstherrn die Konstellation langer Krankheit und... |
| `ernennung-wirksamkeit-ruecknahme-widerruf` | Ernennung, Wirksamkeit, Form, Rücknahme und Widerruf: prüft Urkunde, Zuständigkeit, Nichtigkeit, Täuschung und Fehlerfolgen. |
| `erschwerniszulage-vollzugsdienst` | Skill zu Erschwerniszulagen fuer Polizei Justizvollzug Feuerwehr Bundeswehr und Zoll nach der Erschwerniszulagenverordnung und den Landesvorschriften. Klaert Anspruchsvoraussetzungen Schichtdienst Wechselschichtdienst Nachtdienst Sonn- u... |
| `eu-justizunabhaengigkeit-art-19-euv-art-47-grch` | EU-rechtliche Justizunabhängigkeit: Art. 19 Abs. 1 EUV, Art. 47 GRCh, EuGH-Linien zu Disziplinarregimen, Ernennung, Dienstaufsicht und nationalem Richterrecht. |
| `familienzuschlag-drittes-kind-bverfg` | Skill zum verfassungsrechtlichen Mindeststandard des Familienzuschlags fuer das dritte und jedes weitere Kind nach Art. 33 Abs. 5 GG. Klaert das BVerfG-Pruefschema fuer den Mehrkinderzuschlag mit Vergleich zur sozialhilferechtlichen Beda... |
| `familienzuschlag-kinder-und-rueckforderung` | Familienzuschlag, Kinderanteile, Konkurrenzen, Teilzeit, Trennung, Rückforderung und Mitteilungspflichten. |
| `foederalismusreform-kompetenzmatrix-beamtenrecht` | Kompetenzmatrix seit der Föderalismusreform 2006: Bund, Länder, Art. 70/73/74 Abs. 1 Nr. 27, Art. 125a GG, BeamtStG, BBG, Besoldung, Versorgung, Laufbahn und Richterrecht sauber trennen. |
| `formular-generator-beamtenrecht` | Formular- und Textgenerator für Widerspruch, Akteneinsicht, Beihilfe, Personalakte, Dienstunfall, Remonstration und Eilantrag. |
| `fristen-und-sofortmassnahmen` | Fristen- und Sofortmaßnahmencheck für Widerspruch, Klage, Eilverfahren, Konkurrentenstreit, Disziplinarverfügung, Beurteilung und Zurruhesetzung. |
| `fuersorgepflicht-mobbing-konflikt` | Fürsorgepflicht, Mobbing, Konflikte, Überlastung und Schutzpflichten des Dienstherrn. |
| `geschaeftsverteilung-richter-21e-gvg` | Skill zur richterlichen Geschaeftsverteilung nach § 21e GVG und zum verfassungsrechtlichen Anspruch auf den gesetzlichen Richter aus Art. 101 Abs. 1 Satz 2 GG. Klaert das Praesidium die Aufstellung des Geschaeftsverteilungsplans zu Begin... |
| `geschenke-korruption-compliance` | Geschenke, Einladungen, Sponsoring und Korruptionsprävention im öffentlichen Dienst. |
| `heilfuersorge-vs-beihilfe-vollzugsdienst` | Skill zur Abgrenzung Heilfuersorge und Beihilfe im Vollzugsdienst. Klaert die Systemunterschiede zwischen freier Heilfuersorge fuer Polizeibeamte und Soldaten und der Beihilfe der Verwaltungsbeamten. Behandelt die Konstellation Krankenve... |
| `hinterbliebenenversorgung-witwen-waisen` | Skill zur Hinterbliebenenversorgung in der Beamtenversorgung Witwen- und Witwergeld Halbwaisengeld und Vollwaisengeld nach §§ 19 ff. BeamtVG. Klaert die Anspruchsvoraussetzungen Heiratsklauseln vor Eintritt in den Ruhestand und vor Volle... |
| `hochschule-professoren-w-besoldung` | Hochschulbeamte und Professoren: Berufung, W-Besoldung, Leistungsbezüge, Nebentätigkeit und Freiheit von Forschung und Lehre. |
| `kommunalbeamte-und-wahlbeamte` | Kommunalbeamte und Wahlbeamte: Amtszeit, Abwahl, Bürgermeister, Beigeordnete, Nebentätigkeiten und Versorgung. |
| `konkurrentenklage-einstweiliger-rechtsschutz` | Eilrechtsschutz nach § 123 VwGO im beamtenrechtlichen Konkurrentenstreit. Skill liefert Schriftsatzgeruest fuer Antrag auf einstweilige Anordnung mit dem Begehren die Ernennung des ausgewaehlten Konkurrenten zu untersagen bis ueber die B... |
| `konkurrentenschutz-bestenauslese-art-33-ii-gg` | Pruefschema zum Grundsatz der Bestenauslese aus Art. 33 Abs. 2 GG bei Auswahlentscheidungen im oeffentlichen Dienst. Liefert Bausteine fuer Konkurrentenwiderspruch und Konkurrentenklage. Klaert die drei Auswahlkriterien Eignung Befaehigu... |
| `konkurrentenstreit-eilverfahren` | Konkurrentenstreit und einstweiliger Rechtsschutz gegen Beförderung oder Stellenbesetzung. |
| `krankheitsbedingte-urlaubsuebertragung` | Skill zur Uebertragung und Abgeltung des Erholungsurlaubs bei laenger andauernder Erkrankung im Beamtenverhaeltnis. Klaert die 15-Monats-Frist nach EuGH-Rechtsprechung den unionsrechtlichen Mindesturlaub die Unterscheidung zwischen union... |
| `landesrecht-16-laender-routenplan` | Routenplan für Landesbeamtenrecht aller 16 Länder: Landesbeamtengesetz, Laufbahn, Besoldung, Versorgung, Beihilfe, Disziplinarrecht und Landesrichterrecht ohne falsches Bundesrechts-Autopilotieren. |
| `laufbahnrecht-bund` | Laufbahnrecht Bund: Laufbahngruppen, Vorbereitungsdienst, Aufstieg, Laufbahnwechsel, Anerkennung von Zeiten und Qualifikation. |
| `laufbahnrecht-laender-matrix` | Länder-Laufbahnrecht-Matrix: fragt Bundesland, Laufbahngruppe, Fachrichtung, Vorbildung und Zielamt ab. |
| `lehrer-schule-beamtenrecht` | Lehrerbeamtenrecht: Abordnung, Versetzung, Unterrichtspflicht, Dienstunfähigkeit, Elternkonflikte und Schulaufsicht. |
| `live-quellencheck-bund-land-richter` | Live-Quellencheck für Bundesrecht, Landesrecht und Richterrecht mit Sperre gegen nicht prüfbare Fundstellen. |
| `mandantenbrief-verstaendlich-beamtenrecht` | Verständlicher Mandantenbrief: erklärt Beamtenrecht ohne Amtsdeutsch und mit klarer Handlungsliste. |
| `mehrarbeitsverguetung-88-bbg` | Skill zur Mehrarbeitsverguetung der Beamten nach § 88 BBG bzw. § 60 BeamtStG i.V.m. dem Landesrecht und der Mehrarbeitsverguetungsverordnung. Klaert Anordnung der Mehrarbeit Ausgleich durch Freizeit Verguetung in Geld Begrenzung der Mehr... |
| `mobbing-fuersorgepflicht-78-bbg` | Skill zu Mobbing im oeffentlichen Dienst und zur Fuersorgepflicht des Dienstherrn nach § 78 BBG bzw. § 45 BeamtStG. Klaert den Mobbingbegriff die Pflicht zur Aufklaerung und zur Massnahme im Konfliktfall die Beweislast bei systematischer... |
| `nebentaetigkeit-99-bbg-anzeige-genehmigung` | Skill zum Nebentaetigkeitsrecht der Beamten nach §§ 97 ff. BBG bzw. § 40 BeamtStG i.V.m. Landesrecht. Klaert die Unterscheidung anzeigepflichtige und genehmigungspflichtige Nebentaetigkeiten den Versagungs- und Widerrufsgrund das Verbot... |
| `nebentaetigkeit-genehmigung-und-untersagung` | Nebentätigkeit, Anzeige, Genehmigung, Untersagung, Ablieferungspflichten und Richter-Sonderregeln. |
| `output-waehlen-memo-widerspruch-eilantrag` | Output-Navigator: Mandantenbrief, Behördenanschreiben, Widerspruch, Klage, Eilantrag, Gegenvorstellung, Remonstration oder Verhandlungsnotiz. |
| `personalakte-einsicht-datenschutz` | Personalakte, Einsicht, Datenschutz, Berichtigung und Entfernung belastender Unterlagen. |
| `plausibilisierung-gleicher-gesamtnoten` | Skill zur rechtlich sauberen Aufloesung von Notengleichstand bei der beamtenrechtlichen Auswahlentscheidung. Klaert die Stufenfolge ausschoepfender Beurteilungswert Binnendifferenzierung Einzelmerkmale Reihenfolge und Gewichtung sowie da... |
| `politische-maessigung-60-bbg` | Skill zur politischen Maessigungspflicht nach § 60 BBG bzw. § 33 BeamtStG. Klaert die Pflicht zur Maessigung und Zurueckhaltung im politischen Bereich die Reichweite bei privater Aeusserung in sozialen Medien die Grenze zur Verfassungstr... |
| `polizei-feuerwehr-vollzug-sonderdienst` | Polizei, Feuerwehr, Justizvollzug und sonstige Sonderdienste: Dienstfähigkeit, Schichtdienst, Disziplin und Gefahrennähe. |
| `praesidialrat-mitwirkung-richterernennung` | Skill zur Mitwirkung des Praesidialrats bei Richterernennungen und Beförderungen nach §§ 54 ff. DRiG und den Landesrichtergesetzen. Klaert die Beteiligungspflichten die Inhalte der Stellungnahme die Folgen unterlassener Beteiligung und d... |
| `probezeit-und-lebenszeiternennung` | Probezeit, Bewährung, Verlängerung und Ernennung auf Lebenszeit für Beamte und Richter auf Probe. |
| `ptbs-polizei-anerkennung-dienstunfall` | Skill zur Anerkennung der posttraumatischen Belastungsstoerung als Dienstunfall bei Polizei Justizvollzug Feuerwehr und Soldaten. Klaert die Anforderungen an die Glaubhaftmachung eines auslosenden Ereignisses die Anforderungen an den Kau... |
| `quellenhygiene-beamtenrecht-fundstellen-red-team` | Quellenhygiene-Red-Team für Beamten- und Richterrecht: erkennt verrutschte Fundstellen, private Datenbankzitate, falsche Entscheidungsdaten, Landesrechtsfallen und alte Rechtslage. |
| `reaktivierung-29-bbg-rechtsanspruch` | Skill zur Reaktivierung eines Ruhestandsbeamten nach § 29 BBG bzw. § 29 BeamtStG i.V.m. Landesrecht. Klaert die Voraussetzungen der wiedererlangten Dienstfaehigkeit Rechtsanspruch auf Reaktivierung Spielraum des Dienstherrn dienstliche B... |
| `red-team-beamtenrecht` | Red-Team gegen typische Fehler: falsches Landesrecht, falscher Status, übersehene Frist, unzulässiger Antrag, fehlende Glaubhaftmachung, falsche Besoldungsordnung. |
| `remonstration-rechtswidrige-weisung` | Remonstration bei rechtswidriger Weisung: Pflichten, Ablauf, Dokumentation und Schutz des Beamten. |
| `richter-praesidium-und-geschaeftsverteilung` | Präsidium, Geschäftsverteilungsplan, Abordnung und Besetzung mit Proberichtern. |
| `richteranklage-art-98-gg` | Skill zur Richteranklage nach Art. 98 Abs. 2 und Abs. 5 GG i.V.m. den landesrechtlichen Vorschriften. Klaert die Voraussetzungen fuer ein Verfahren beim Bundesverfassungsgericht gegen einen Bundesrichter den verfassungsrechtlichen Tatbes... |
| `richterbeurteilung-praesidialrat` | Richterbeurteilung, Präsidialrat, Richterwahlausschuss und Beteiligung vor Ernennung. |
| `richterdienst-drig-grundlagen` | Richterdienst nach DRiG: Rechtsformen, Voraussetzungen, Richter auf Probe, Lebenszeit und Unvereinbarkeiten. |
| `richterdienstgericht-und-rechtswegabgrenzung` | Richterdienstgerichte und Rechtsweg: DRiG, Landesrichterrecht, Dienstaufsichtsmaßnahme, Statusstreit, Beurteilung, Beihilfe, Versorgung, Präsidium und Verwaltungsgerichtsbarkeit trennen. |
| `richterliche-unabhaengigkeit-dienstaufsicht` | Richterliche Unabhängigkeit, Dienstaufsicht, Ermahnung, Geschäftsprüfung und unzulässige Einflussnahme. |
| `richterliche-unabhaengigkeit-drig-26-pruefungsverfahren` | Richterliche Unabhängigkeit und Dienstaufsicht: Art. 97 GG, § 25, § 26, § 39 DRiG, Prüfungsverfahren, Erledigungsdruck, Geschäftsprüfung und zulässige Verwaltungskontrolle. |
| `richterwahl-art-33-ii-und-praesidialrat` | Richterwahl, Art. 33 Abs. 2 GG, Richterwahlausschuss, Präsidialrat, Bundesrichterwahl, Begründungspflichten, Konkurrentenstreit und politische Wahlspielräume. |
| `ruhensregelung-53-beamtvg` | Skill zur Ruhensregelung von Versorgungsbezuegen bei Erwerbseinkommen nach § 53 BeamtVG. Klaert Hinzuverdienstgrenze fuer Ruhestandsbeamte unterschiedliche Grenzen vor und nach Erreichen der Regelaltersgrenze Anrechnung von Verwendungsei... |
| `schadensersatz-nichtbefoerderung` | Skill zur Pruefung des beamtenrechtlichen Schadensersatzanspruchs bei rechtswidriger Nichtbefoerderung. Klaert Anspruchsgrundlage Pflichtverletzung Verschulden Schaden Kausalitaet und die hypothetische Befoerderungslage. Behandelt die Ko... |
| `schwerbehinderte-bewerber-165-sgb-9` | Skill zur Pruefung der Pflichten oeffentlicher Arbeitgeber bei Bewerbungen schwerbehinderter Menschen nach § 165 SGB IX. Klaert Einladungspflicht zum Vorstellungsgespraech Pruefpflicht bei interner Besetzung Beruecksichtigung der Eignung... |
| `schwerbehinderung-bem-gleichstellung` | Schwerbehinderung, Gleichstellung, BEM, Nachteilsausgleich und Beteiligung der Schwerbehindertenvertretung. |
| `soldaten-und-beamte-abgrenzung` | Abgrenzung Soldatenrecht, Beamtenrecht und zivile Bundeswehrverwaltung. |
| `status-und-rechtsquellenfinder` | Statusklärung und Rechtsquellenfinder für Bund, Länder, Kommunen, Richterdienst, Professoren, Anwärter, Wahlbeamte und Tarifbeschäftigte. |
| `statusamt-funktionsamt-dienstposten` | Statusamt, Funktionsamt und Dienstposten unterscheiden: wichtig für Umsetzung, Beförderung, amtsangemessene Beschäftigung und Bewerbungsverfahren. |
| `strafverfahren-und-disziplinarverfahren` | Schnittstelle Strafverfahren und Disziplinarverfahren: Aussageverhalten, Aussetzung, Bindungswirkung, Akteneinsicht und Verteidigungsstrategie. |
| `stufenfeststellung-besoldung-27-bbesg` | Skill zur erstmaligen Stufenfeststellung in der Besoldungsgruppe nach § 27 BBesG bzw. den landesrechtlichen Parallelvorschriften. Klaert Anerkennung beruflicher Vorzeiten Wartezeiten Stufenaufstieg Verzoegerungstatbestaende Hemmungen dur... |
| `suspendierung-38-bdg-63-bdg-eilrechtsschutz` | Vorläufige Dienstenthebung und Bezügeeinbehalt: § 38 BDG, § 63 BDG, Prognose der Entfernung, Härteprüfung, Anhörung, Eilrechtsschutz und Nachzahlungsrisiko. |
| `tarifbeschaeftigte-abgrenzung-tv-l` | Abgrenzung Beamte zu Tarifbeschäftigten nach TVöD/TV-L und Folgen für Rechtsschutz. |
| `teilzeit-beurlaubung-familienpflege` | Teilzeit, Beurlaubung, Elternzeit, Pflegezeit und Rückkehr in den Dienst. |
| `umsetzung-versetzung-abordnung-zuweisung` | Umsetzung, Versetzung, Abordnung und Zuweisung: Eingriffsintensität, Ermessen, Fürsorge, Pendelbelastung und Familienbezug. |
| `unfallruhegehalt-36-beamtvg` | Skill zum Unfallruhegehalt nach § 36 BeamtVG bei Dienstbeschaedigung. Klaert Anspruchsvoraussetzung qualifizierter Dienstunfall Bemessungsgrundlage und erhoehter Ruhegehaltssatz Verhaeltnis zum regulaeren Ruhegehalt sowie Sonderfaelle wi... |
| `urlaub-erkrankung-und-verfall` | Erholungsurlaub, Erkrankung, Verfall, Übertragung, Langzeiterkrankung und europarechtliche Linien. |
| `verfassungstreue-7-bbg-reichsbuerger` | Skill zur beamtenrechtlichen Verfassungstreue nach § 7 BBG bzw. § 33 BeamtStG insbesondere in Fallgestaltungen Reichsbuerger Extremismus und der Verfassungsschutzbeobachteten Parteien. Klaert die Anforderungen an die Feststellung mangeln... |
| `verfassungstreue-extremismus-chatgruppen-disziplinarrecht` | Verfassungstreue im Beamten- und Richterdienst: Reichsbürger, extremistische Bezüge, Chatgruppen, Social Media, Parteitätigkeit, Mäßigungspflicht, Beweiswürdigung und disziplinarische Reaktion. |
| `versetzung-gegen-willen-28-bbg` | Skill zur Versetzung des Beamten gegen seinen Willen nach § 28 BBG bzw. § 15 BeamtStG i.V.m. Landesrecht. Klaert die Voraussetzungen dienstliche Belange Anhoerung Beruecksichtigung der persoenlichen Verhaeltnisse und das Verhaeltnis zur... |
| `versorgung-ruhegehalt-beamtvg` | Versorgung und Ruhegehalt: ruhegehaltfähige Dienstzeit, Versorgungsabschlag, Mindestversorgung, Hinterbliebenenversorgung. |
| `versorgungsabschlag-14-beamtvg` | Skill zum Versorgungsabschlag bei vorzeitigem Eintritt in den Ruhestand nach § 14 Abs. 3 BeamtVG. Klaert die Hoehe des Abschlags die Konstellationen Antragsruhestand vor Erreichen der Regelaltersgrenze und Ruhestand wegen Dienstunfaehigk... |
| `versorgungslastenteilung-107b-beamtvg` | Skill zur Versorgungslastenteilung bei Dienstherrenwechsel nach § 107b BeamtVG bzw. dem Versorgungslastenteilungs-Staatsvertrag. Klaert die Berechnung der Abfindung den Wechsel zwischen Bund und Land und zwischen Bundeslaendern die Hoehe... |
| `vorlaeufige-dienstenthebung-38-bdg` | Skill zur vorlaeufigen Dienstenthebung und zum Einbehalt von Dienstbezuegen nach § 38 BDG und den Landesdisziplinargesetzen. Klaert die Voraussetzungen die Pruefdichte des Antrags nach § 63 BDG die Beschwerde gegen Dienstenthebung das Ei... |
| `vorlaeufige-dienstenthebung-bezuege` | Vorläufige Dienstenthebung und Einbehaltung von Bezügen im Disziplinarverfahren. |
| `widerspruch-klage-vwgo` | Widerspruch, Klage und VwGO-Rechtsschutz in beamtenrechtlichen Streitigkeiten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
