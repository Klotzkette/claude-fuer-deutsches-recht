# Verkehrs- und Infrastrukturrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verkehr-infrastrukturrecht`) | [`verkehr-infrastrukturrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehr-infrastrukturrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin** (`batteriespeicher-brandenburg-berlin-resilienz`) | [Gesamt-PDF lesen](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [`testakte-batteriespeicher-brandenburg-berlin-resilienz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) |
| **Projekt Isarlicht — Kernfusion und Transrapid am Starnberger See** (`kernfusion-transrapid-starnberger-see`) | [Gesamt-PDF lesen](../testakten/kernfusion-transrapid-starnberger-see/gesamt-pdf/kernfusion-transrapid-starnberger-see_gesamt.pdf) | [`testakte-kernfusion-transrapid-starnberger-see.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kernfusion-transrapid-starnberger-see.zip) |
| **Akte Verkehrs- und Infrastrukturrecht: Straßenbahn Linie 7, Ladezonen und Schulwegsicherheit** (`verkehr-infrastrukturrecht-strassenbahn-ladezonen`) | [Gesamt-PDF lesen](../testakten/verkehr-infrastrukturrecht-strassenbahn-ladezonen/gesamt-pdf/verkehr-infrastrukturrecht-strassenbahn-ladezonen_gesamt.pdf) | [`testakte-verkehr-infrastrukturrecht-strassenbahn-ladezonen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehr-infrastrukturrecht-strassenbahn-ladezonen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Vollständiger Assistent für Verkehrsplanung, Infrastrukturprojekte, Elektromobilität, Straßenbahn, Sondernutzung, Parkraumbewirtschaftung, Liefer- und Ladezonen, Verkehrswende, Schulwegsicherheit, Fördermittel und Vergabe.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn ein Anschluss an Register, Behördenportale, E-Mail, beA, Datenraum, Bank, GIS, Tabellen oder Kanzleisoftware fehlt, arbeitet es mit manuellen Uploads oder mit einem gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Eine neue Sache mit `verkehr-infrastrukturrecht-kommandocenter` starten.
3. Mandant, Ziel, Frist, Dokumente und gewünschtes Ergebnis nennen.
4. Bei fehlenden Systemanschlüssen `Simulation` sagen; das Plugin erzeugt dann realistische Testdaten und erklärt, welche echte Schnittstelle später ersetzt werden müsste.
5. Am Ende immer das Qualitätstor ausgeben lassen: offene Annahmen, Fristen, Rechenprüfung, Anlagen, Zuständigkeiten und nächste Schritte.

## Enthaltene Skills

- `verkehr-infrastrukturrecht-kommandocenter` - Verkehrs- und Infrastruktur-Kommandocenter
- `verkehr-infrastrukturrecht-verkehrsplanung` - Verkehrsplanung und Projektstrategie
- `verkehr-infrastrukturrecht-planfeststellung` - Planfeststellung und Abwägung
- `verkehr-infrastrukturrecht-strassenbahn` - Straßenbahn- und ÖPNV-Projekte
- `verkehr-infrastrukturrecht-ladeinfrastruktur` - Ladeinfrastruktur und Elektromobilität
- `verkehr-infrastrukturrecht-sondernutzung` - Sondernutzung, Widmung und Straßenrecht
- `verkehr-infrastrukturrecht-parkraumbewirtschaftung` - Parkraumbewirtschaftung
- `verkehr-infrastrukturrecht-wirtschaftsverkehr` - Wirtschaftsverkehr, Liefer- und Ladezonen
- `verkehr-infrastrukturrecht-verkehrswende` - Verkehrswende und Verkehrsberuhigung
- `verkehr-infrastrukturrecht-schulwegsicherheit` - Schulwegsicherheit
- `verkehr-infrastrukturrecht-verfahren` - Verkehrsrechtliche Verfahren und Streit
- `verkehr-infrastrukturrecht-foerderung-vergabe` - Förderung und Vergabe Infrastruktur

## Vorlagen

- `assets/templates/verkehr-mandatskarte.md` - Verkehrs- und Infrastruktur-Mandatskarte
- `assets/templates/infrastruktur-projektfahrplan.md` - Infrastruktur-Projektfahrplan
- `assets/templates/planfeststellung-abwaegungsmatrix.md` - Planfeststellungs- und Abwägungsmatrix
- `assets/templates/strassenbahn-workstream-plan.md` - Straßenbahn-Workstream-Plan
- `assets/templates/ladeinfrastruktur-check.md` - Ladeinfrastruktur-Check
- `assets/templates/sondernutzung-erlaubnis.md` - Sondernutzung und Straßenrecht
- `assets/templates/parkraumkonzept.md` - Parkraumbewirtschaftungskonzept
- `assets/templates/liefer-ladeflaechen-konzept.md` - Liefer- und Ladeflächenkonzept
- `assets/templates/verkehrswende-massnahmenplan.md` - Verkehrswende-Maßnahmenplan
- `assets/templates/schulwegsicherheit-check.md` - Schulwegsicherheitscheck
- `assets/templates/verkehrsverfahren-fristen.md` - Verkehrs-Verfahrens- und Fristenplan
- `assets/templates/foerderung-vergabe-matrix.md` - Förder- und Vergabematrix

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen; unsichere Normen und Rechtsprechung werden als Prüfbedarf markiert.
- Zahlen, Fristen, Schwellenwerte und Zuständigkeiten werden sichtbar hergeleitet oder als Annahme gekennzeichnet.
- Ausgabe immer so, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anschluss-router` | Einstieg, Schnelltriage und Fallrouting im Verkehr Infrastrukturrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `autonomous-driving` | Zentrales Steuerungsmodul Verkehrs- und Infrastrukturrecht: Neues Mandat im Bereich Verkehrsinfrastruktur, Routing auf passenden Subskill. Normen: FStrG, AEG, PBefG, StVO, BauGB, FStrG, GWB (je nach Sachgebiet). Prüfraster: Sachgebiet (P... |
| `autonomous-driving-interessen-grossprojekt` | Autonomous: Compliance-Dokumentation und Aktenvermerk im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr Inf... |
| `autonomous-driving-strassenrecht` | Autonomes Fahren und Strassenrecht: § 1d StVG, autonomes Fahren in Level 4, Genehmigung der zuständigen Landesbehoerden, Betrieb auf festgelegter Strecke. Schnittstelle zu KI-VO Hochrisikoanwendungen, Datenschutz, Haftungsfragen. Pruefra... |
| `buergerentscheid-strassenbahn-spezial` | Spezialfall Buergerentscheid zur Strassenbahn oder Stadtbahn: kommunalrechtliche Voraussetzungen, Verhaeltnis zum Beschluss des Gemeinderats, planungsrechtliche Folgen, Foerderfaehigkeit nach GVFG bei Verzoegerung. Pruefraster im Verkehr... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `driving-mehrparteien-konflikt-und-interessen` | Driving: Mehrparteienkonflikt und Interessenmatrix im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr Infras... |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `foerderung-vergabe-ladeinfrastruktur` | Foerderrecht und Vergabe für Verkehrsinfrastruktur-Projekte: Kommune oder Vorhabentraeger beantragt GVFG-Mittel oder schreibt öffentlichen Auftrag aus. Normen: GVFG (Bundesanteil und Länderanteil), BHO §§ 23 und 44 (Zuwendungsrecht), GWB... |
| `grossprojekt-zahlen-schwellen-und-berechnung` | Grossprojekt: Zahlen, Schwellenwerte und Berechnung im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr Infra... |
| `infrastruktur-foerderung-nachhaltige` | Foerderprogramme Verkehrsinfrastruktur uebersichtlich: GVFG, KfW, EU CEF, NIP, Foerderaufruf BMDV, Land-Programme. Pro Programm: Foerdergegenstand, Quote, Antragsweg, Berichtspflichten. Routet in verkehr-infrastrukturrecht-foerderung-ver... |
| `infrastrukturrecht-intake-ladeinfrastruktur` | Infrastrukturrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung... |
| `intake-mandantenkommunikation-entscheidungsvorlage` | Intake: Mandantenkommunikation und Entscheidungsvorlage im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr I... |
| `ladeinfrastruktur` | Ladeinfrastruktur für Elektromobilitaet rechtlich begleiten: Betreiber plant Ladepunkte oder Netzanschluss wird verweigert. Normen: AFIR-VO (EU) 2023/1804 (Mindestanforderungen Ladeinfrastruktur), Ladesaeulenverordnung LSV, § 8 EnWG (Net... |
| `ladeinfrastruktur-behoerden-gericht-und-registerweg` | Ladeinfrastruktur: Behörden-, Gerichts- oder Registerweg im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr... |
| `livecheck-sonderfall-mobilitaetsprojekt` | Livecheck: Sonderfall und Edge-Case-Prüfung im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr Infrastruktur... |
| `mobilitaetsprojekt-intake` | Mobilitätsprojekt-Intake mit Rechtsweg-, Förder- und Beteiligungsweiche: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Verkehr Infrastrukturrecht: prüft konkret die e... |
| `mobilitaetsprojekt-red-team-und-qualitaetskontrolle` | Mobilitaetsprojekt: Red-Team und Qualitätskontrolle im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr Infra... |
| `nachhaltige-bahninfrastruktur-emissionen` | Nachhaltige Bahninfrastruktur und Emissionen: Trassenpreis, Elektrifizierungsfoerderung, Verlagerung Schiene, ETS und Strassenverkehr, CBAM-Bezug für Stahl/Schienen-Lieferungen. Compliance-Roadmap für DB-Auftraggeber und Bauunternehmen i... |
| `output-waehlen` | Output wählen im Verkehrs- und Infrastrukturrecht: Diese Output-Weiche für Verkehr Infrastrukturrecht entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `parkraum-planfeststellung-strassenbahn` | Parkraum: Schriftsatz-, Brief- und Memo-Bausteine im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr Infrast... |
| `parkraumbewirtschaftung` | Parkraumbewirtschaftung kommunalrechtlich gestalten und anfechten: Kommune einführt Bewohnerparkausweis oder Abschleppung wird angefochten. Normen: § 45 StVO (Bewohnerparkausweis, Verkehrszeichen), StVG § 12 (Haltverbot), VwVfG (Verwaltu... |
| `parkraumbewirtschaftung-verkehr` | Parkraumbewirtschaftung: Formular, Portal und Einreichungslogik im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im V... |
| `planfeststellung` | Planfeststellung für Strassenbau, Schienenstrecken und OEPNV-Infrastruktur begleiten oder anfechten: Vorhabentraeger benoetigt Planfeststellungsbeschluss oder Anlieger klagt dagegen. Normen: § 17 FStrG (Bundesstrasse), § 18 AEG (Eisenbah... |
| `planfeststellung-dokumentenmatrix-und-lueckenliste` | Planfeststellung: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im... |
| `planfeststellung-grossprojekt` | Planfeststellung und Großprojektsteuerung: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Verkehr Infrastrukturrecht: prüft konkret die einschlägigen Tatbestandsmerkma... |
| `planfeststellung-grundzuege` | Planfeststellung in Grundzuegen: §§ 72 ff. VwVfG, fachgesetzliche Planfeststellung Strasse, Schiene, Wasser, Energie. Antragsunterlagen, Anhörungsverfahren, Beschluss, Klage. Verhaeltnis zur Plangenehmigung. Routet in verkehr-infrastrukt... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `schulwegsicherheit-sondernutzung-strassenbahn` | Schulwegsicherheit rechtlich verbessern oder Amtshaftung geltend machen: Schule, Eltern oder Kommune will Schulwegplan umsetzen oder gegen Unfall auf Schulweg vorgehen. Normen: § 45 StVO (Schulweghelfer, Schulstrassen, 30er-Zone), § 839... |
| `sondernutzung` | Sondernutzung öffentlicher Strassenflaechen beantragen und anfechten: Unternehmen braucht Erlaubnis für Aussengastronomie, Ladesaeule oder Baustelle. Normen: § 8 FStrG (Bundesstrassenrecht), § 16 StrWG NW (Landesstrassenrecht), BayStrWG... |
| `strassenbahn` | Strassenbahn- und OEPNV-Infrastrukturrecht: Betreiber beantragt Konzession oder Planfeststellung, oder Gemeinde will Linie neu planen. Normen: § 9 PBefG (Konzession), § 28 PBefG (Planfeststellung Strassenbahn), § 39 PBefG (Linienbuendelu... |
| `strassenbahn-risikoampel-und-gegenargumente` | Strassenbahn: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im... |
| `strassenrecht-verkehrs-verkehrswende` | Strassenrecht: Internationaler Bezug und Schnittstellen im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr I... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verfahren` | Anhörung, Widerspruch, Klage und Eilverfahren im Verkehrsinfrastrukturrecht vorbereiten: Mandant hat Bescheid erhalten oder will in laufendes Verfahren eingreifen. Normen: § 45 StVO (Verkehrsanordnungen), § 46 StVO (Ausnahmegenehmigungen... |
| `verkehr-infrastruktur-fristen-risiko-mandant` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Verkehr Infrastrukturrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung.... |
| `verkehr-infrastruktur-rechtsquellen-beweislast-darlegungslast` | Rechtsquellen: Quellenprüfung; Beweislast, Darlegungslast und Substantiierung: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verkehr-quellenkarte` | Verkehr Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verkehrs-erstpruefung-und-mandatsziel` | Verkehrs: Erstprüfung, Rollenklärung und Mandatsziel im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr Infr... |
| `verkehrsplanung-verfahren-vertragsmodell` | Verkehrsplanung: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verke... |
| `verkehrsplanung-verkehrswende` | Verkehrsplanung rechtlich begleiten: Kommune oder Verband plant Strassen- oder Radverkehrs-Massnahme und muss Beteiligung und Beschluss vorbereiten. Normen: § 45 StVO (Verkehrsanordnungen), FStrG, StrWG (Landesrecht), ROG §§ 4 ff. (Raumo... |
| `verkehrswende` | Verkehrswende-Massnahmen rechtssicher gestalten: Kommune plant Fussgaengerzone, Tempo-30-Zone oder Radverkehrs-Förderung. Normen: § 45 Abs. 1 StVO (Fussgaengerzone, Tempo-30), ERA 2010 (Empfehlungen Radverkehr), VwGO (Anfechtbarkeit durc... |
| `verkehrswende-verhandlung-vergleich-und-eskalation` | Verkehrswende: Verhandlung, Vergleich und Eskalation im Plugin verkehr infrastrukturrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr Infr... |
| `vertragsmodell-strasse-app-spezial` | Spezialfall App- und Plattform-Vertraege im öffentlichen Personennahverkehr: Mobility-as-a-Service-Vertraege, Datenraum, P2B-Verordnung, DSGVO, Verkehrsvertraege nach VO 1370/2007. Schiedsklauseln und Vergaberecht. Pruefraster für Kommun... |
| `vi-rechtsquellen-uebersicht` | Rechtsquellen Verkehrs- und Infrastrukturrecht: BFStrG, PBefG, AEG, EnWG-Trasse, BImSchG, BNatSchG, WHG, VwVfG, UVPG. Pro Norm: Anwendungsbereich, Verfahrensart, Aufsicht. Entscheidungstabelle für ein konkretes Infrastrukturvorhaben. |
| `vifr-aeg-bahnrecht-deutschlandticket` | Leitfaden AEG und Bahnrecht: Eisenbahninfrastruktur, Trassenvergabe, Netzzugang, EBA als Aufsicht. Pruefraster für EVU und EIU im Verkehr Infrastrukturrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechts... |
| `vifr-deutschlandticket-tarifrecht-spezial` | Spezialfall Deutschlandticket und Tarifrecht OePNV: Finanzierungsvereinbarungen Bund-Länder, AGB Verkehrsverbund, Verbraucherrechte. Pruefraster für Verbraucherzentrale und Verkehrsverbund im Verkehr Infrastrukturrecht: prüft konkret die... |
| `vifr-luftverkehrsrecht-flughafen-spezial` | Spezialfall Luftverkehrsrecht und Flughafenausbau: Planfeststellung LuftVG, Nachtflug, Anwohnerklagen, EU-Slot-VO. Pruefraster für Flughafenbetreiber und Anwohner im Verkehr Infrastrukturrecht: prüft konkret die einschlägigen Tatbestands... |
| `vifr-planfeststellung` | Vifr Planfeststellung im Verkehrs- und Infrastrukturrecht im Verkehr Infrastrukturrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampe... |
| `wirtschaftsverkehr` | Wirtschaftsverkehr und Lieferverkehr in der Stadt rechtlich gestalten: Logistikunternehmen oder Kommune plant Lieferzonen, Beschilderung oder Ausnahmegenehmigungen. Normen: § 12 StVO (Haltverbot), § 45 StVO (Sonderregelungen), § 46 StVO... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Verkehr Infrastrukturrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert pr... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Verkehr Infrastrukturrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechun... |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Verkehr Infrastrukturrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Recht... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Verkehr Infrastrukturrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung.... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
