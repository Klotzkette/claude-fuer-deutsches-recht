---
name: konkurrenzrechtsschutz-orchestrator
description: 'Primärer Kaltstart ohne Skillwahl für jeden Konkurrentenfall mit Aktenordner, ZIP, Informationsschreiben oder Portalbeleg. Immer zuerst einsetzen, wenn der Angriff noch nicht eng abgegrenzt ist. Sichert Rüge- und Zuschlagsfristen, ordnet Tatsachenkern, Beweiskette, Akteneinsicht und Antrag und routet danach zu höchstens drei Fachskills.'
---

# Konkurrenzrechtsschutz Orchestrator

**Arbeitsname:** Neuer Konkurrentenfall automatisch vorbereiten, stärksten Angriff finden und Rechtsschutzpfad starten.

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Start

Immer zuerst das Konkurrenten-Dashboard bilden:

| Feld | Prüfung |
| --- | --- |
| Rolle | Konkurrent, unterlegener Bieter, ausgeschlossener Bieter, Bewerber, Zuschlagsprätendent, Kanzlei |
| Verfahrensstand | Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Nichtabhilfe, VK, OLG, Zuschlag, Vertrag |
| Ziel | Unterlagen ändern, Frist verlängern, Zuschlag stoppen, Konkurrent ausschließen, neue Wertung, Akteneinsicht, Unwirksamkeit, Schadensersatz |
| Rote Frist | Angebotsfrist, Rügefrist, 15-Tage-Frist nach Nichtabhilfe, Stillhaltefrist, OLG-Frist |
| Systembeweis | Herkunftszone, TED/eForms/Portal, eigene ERP/AVA/DMS-Daten, Akteneinsicht, API/MCP, Original, Transformation, Hash |
| Nächster Output | Rüge, VK-Antrag, Eilantrag, Akteneinsichtsantrag, OLG-Beschwerde, Vergleichsvorschlag, Kostenmemo |

## Abgrenzung

Dieser Orchestrator ist der einzige automatische Kaltstart für Ordner, ZIP, Akteneinsichts-, Portal- oder Systemexporte und unklare Mehrfachlagen. `startbildschirm-konkurrentenangriff` wird erst nach dieser Triage geladen, um deren Ergebnisse als Dashboard darzustellen; er ersetzt weder Quelleninventar noch Fristen- und Zulässigkeitsprüfung.

## Null-Konfigurations-Vertrag

1. Formulierungen wie `neuer Konkurrentenfall`, `neuer Fall`, `bitte vorbereiten`, `prüfe alles` oder `mach, was nötig ist` sind ein vollständiger Arbeitsauftrag. Nicht nach einem Skill, Angriffsmodus oder Schriftsatztyp fragen.
2. Zuerst alle sichtbaren Unterlagen, Portalbelege und zulässig verfügbaren Systemdaten auslesen. Bereits erkennbare Kenntniszeit, Nichtabhilfe, Stillhaltefrist, Angriffsziel oder eigene Bieterstellung nicht erneut erfragen.
3. Noch vor der Tiefenprüfung die fünf Zeilen `Lage | Rot | Angriff | Rechtsweiche | Jetzt` ausgeben. Bei Unsicherheit mit gekennzeichneter Arbeitshypothese fortfahren.
4. Höchstens drei echte Blockerfragen gesammelt und erst nach dem ersten Arbeitsstand stellen. Jede Frage muss benennen, welche Frist, Antragsbefugnis, Kausalität oder Rechtsfolge ohne die Antwort offenbleibt.
5. Bei größeren Beständen vor dem vertieften Auslesen kurz Paketumfang, Prioritätsdateien und nächsten Checkpoint nennen. So bleibt der Fortschritt sichtbar und fortsetzbar.

## Routingbudget

Pro Arbeitsdurchgang diesen Orchestrator und höchstens drei Fachskills einsetzen: einen für die leitende Angriffslinie, einen für Beweis oder Akteneinsicht und einen für den konkret zu erstellenden Rechtsbehelf. Nicht den gesamten Skillbestand laden. Zu jedem geladenen Fachskill in einem Halbsatz nennen, welchen Antrag, Beleg oder Fristenschritt er in diesem Durchgang erzeugt; weitere Skills erst in einem späteren Durchgang nach einem neuen Tatsachenbefund ergänzen.

## 90-Sekunden-Erstantwort

Noch vor jeder längeren Prüfung genau diese fünf Zeilen liefern:

| Feld | Konkurrentenantwort |
|---|---|
| Lage | Verfahren, Rolle, Phase und gewünschte Rechtsfolge in einem Satz |
| Rot | früheste Rüge-, Nichtabhilfe-, Stillhalte-, VK-, §-135- oder OLG-Frist mit Startpunkt und Beleg; sonst `nicht berechenbar` |
| Angriff | stärkste vorläufige Rechtsverletzung mit Fundstelle, Kausalität und Zuschlagschance |
| Beweis | stärkster vorhandener Beleg, Herkunftszone und wichtigste Akteneinsichtslücke |
| Jetzt | genau ein erster Streitoutput und genau eine Zustellungs-, Beweis- oder Freigabehandlung |

## Ordnerfall-Kaltstart ohne Skillwahl

Wenn der Nutzer nur einen Projektordner, ZIP, Portalexport, Akteneinsichtsordner oder Dateistapel mit einer Formulierung wie `neuer Fall`, `bitte vorbereiten` oder `mach, was nötig ist` übergibt, nicht nach einem Skill fragen. Arbeite den Fall selbst an und route erst danach intern.

1. Datei- und Quelleninventar bilden: Dateiname, Typ, Datum, Version, Urheber, Portalzeitstempel, Hash, Bezug zu Bekanntmachung, Unterlagen, LV, Wertung, § 134 GWB, Rüge, Nichtabhilfe, VK/OLG oder Vertrag.
2. Angriffslage aus Unterlagen ableiten: Billigzuschlag, Unterlagenfehler, Produkt-/Formatsperre, Wertungsfehler, Eignungs-/Ausschlussangriff, de-facto-Vergabe, Akteneinsicht/Schwärzung, Auftragnehmerwechsel oder Kostenrisiko.
3. Rote Fristen zuerst sichern: Angebotsfrist, Rügefrist, Nichtabhilfe, Stillhaltefrist, Zuschlagssperre, VK-Zustellung, Beschwerdefrist, § 135 GWB.
4. Beweis- und Formatlage erkennen: Herkunftszone, Portalprotokoll, Uploadquittung, Screenshot, GAEB/XML/Excel/PDF, eigene SAP/ERP/AVA/DMS-Daten, API/MCP, Original/Arbeitskopie, Transformation, Hash, E-Mail, Zeuge, Akteneinsichtslücke.
5. Erste Output-Weiche setzen: Rüge, VK-Antrag, Zuschlagssperre, Akteneinsicht, Schwärzungsangriff, OLG, Vergleich, Kostenmemo oder Schadensersatzspur.

Pflichtausgabe beim Ordnerfall: Fallkarte, Fristenampel, Dokumentenmatrix, Belegmatrix, Angriffslinien, Lückenliste, Quellenstatus, empfohlener erster Streitoutput und genau eine nächste Bedienhandlung. Nutze `assets/templates/ordnerfall-startprotokoll.md` und `assets/templates/fallkarte-output-weiche.md`.

## Stabiler Großakten- und Fortsetzungsmodus

1. Ab 50 Dateien oder 250 MB zuerst einen reinen Metadatenlauf ausführen; Frist-, Zugangs-, Nichtabhilfe- und Zuschlagsbelege priorisieren.
2. Danach Pakete von höchstens 20 Dateien oder 100 MB verarbeiten. Große PDF-, Office- oder GAEB-Dateien einzeln öffnen; nicht gleichzeitig rendern, konvertieren und als Anlagenpaket ausgeben.
3. Nach jedem Paket ein Checkpoint-Register `Datei | Hash | Status | Ergebnis | Fehler | nächster Lauf` fortschreiben. Eine Datei mit unverändertem Hash nicht erneut auslesen.
4. Beschädigte, verschlüsselte oder nicht unterstützte Dateien als Beweislücke und gegebenenfalls als Akteneinsichtsziel protokollieren. Fristsicherung und übrige Angriffslinien laufen weiter.
5. Bei Abbruch am letzten vollständigen Checkpoint fortsetzen. Schriftsatz- und Anlagenpakete erst nach Kontrolle von Frist, Antrag, Belegzuordnung und Geheimnisschutz erzeugen.

## Bedienbarkeitsregel

Jeder Lauf startet mit einer Ein-Bildschirm-Lage und endet mit einer Streit- oder Beweishandlung: Rüge, Antrag, Anlage, Freigabe, Akteneinsicht, OLG-Schritt oder Kostenentscheidung. Genau einen Output empfehlen, höchstens zwei Alternativen nennen und keine längere Begründung ohne Fristenampel, Belegmatrix oder Angriffslinie beginnen.

## Vorlagen-Weiche

Nutze für umfangreiche Fälle `assets/templates/ordnerfall-startprotokoll.md`, `assets/templates/fallkarte-output-weiche.md`, `assets/templates/startbildschirm-konkurrenten-dashboard.md` oder `assets/templates/streitfall-dashboard-konkurrent.md` als Vorlage. Die Fallkarte steht vor der Begründung und übersetzt Verdacht in Norm, Beweislast, Quellenstatus, Rechtsfolge und Antrag.

## Vorgehen

1. Rechtsweg klären: Oberschwelle/Vergabekammer oder Unterschwelle/Aufsicht/Schadensersatz. Schwellenwerte 2026/2027 nach VO (EU) 2025/2152 klassisch, 2025/2150 Sektoren, 2025/2151 Konzessionen und 2025/2487 Verteidigung/Sicherheit live verifizieren; bei Unterschwelle Landeswertgrenzen prüfen.
2. Fristen sichern: § 134, § 135, § 160, § 169, § 171, § 172 und § 173 GWB prüfen.
3. Angriffsziel in einen Antrag übersetzen: Berichtigung, Rückversetzung, Ausschluss Konkurrent, neue Wertung, Zuschlagsverbot, Unwirksamkeit.
4. Belegmatrix erstellen: Datei, Seite, Position, Portalzeitstempel, Zeuge, Gegenargument.
5. System- oder Portalbelege als Beweiskette sichern: Zugangsgrund, Original, Arbeitskopie, Transformation, Tatsachenkern, Gegenhypothese, Angriff, Hash, Anlage, Geheimnisschutz und Rückmeldung.
6. Rügeobliegenheit und Antragsbefugnis nie überspringen.
7. Bei drohendem Zuschlag sofort Zuschlagssperre und Zustellung an Vergabekammer priorisieren.

## Spezialskill laden, wenn

| Auslöser | Arbeitsmodul |
|---|---|
| Triage ist abgeschlossen und soll als kompakter Startbildschirm oder Streitdashboard dargestellt werden | `startbildschirm-konkurrentenangriff` |
| Rüge, Präklusion, Kenntnis, Erkennbarkeit oder Abhilfe verlangt wird | `ruege-konkurrent-160-gwb` |
| Nichtabhilfe, Stillhaltefrist oder VK-Antrag vorbereitet wird | `nachpruefungsantrag-konkurrent-vk` |
| § 134 GWB-Schreiben, Zuschlag heute oder morgen, Gestattungsantrag oder Eilbedarf vorliegt | `eilantrag-zuschlagssperre-169` |
| Wertung, Bewertungsvermerk, Punktedifferenz, Dokumentationslücke oder neue Wertung angegriffen wird | `wertungsangriff-und-dokumentationsluecken` |
| billigstes Angebot gewinnt trotz Qualitäts-, Tempo-, Servicelevel- oder Lebenszyklusrelevanz | `billigzuschlag-angreifen` |
| Hersteller-, Typ-, Material-, System-, Schnittstellen- oder Gleichwertigkeitsvorgabe vorliegt | `produktneutralitaet-und-leistungsbeschreibung` |
| Netto-Null-Technologie, Windrotorblatt, Rezyklierbarkeit, Resilienz, Herkunft oder GPA betroffen ist | `netto-null-technologien-vergabe` |
| Bundeswehr-, Verteidigungs-, Sicherheits-, VSVgV- oder BwBBG-Vergabe betroffen ist | `bundeswehrbeschaffung-bwbbg-2026` |
| Konkurrent wegen Eignung, Ausschlussgründen, Steuern, Sozialabgaben, Referenzen oder Selbstreinigung angreifbar ist | `eignungs-und-ausschlussangriff-konkurrent` |
| Akteneinsicht, Schwärzung, Geschäftsgeheimnis oder Replikplan gebraucht wird | `akteneinsicht-schwaerzung-belegmatrix` |
| Uploadquittung, Portalnachricht, Zeitstempel, Hash, Dateiversion, Screenshot oder Zustellung zu sichern ist | `beweisstrategie-und-portalnachweise` |
| SAP, ERP, AVA, DMS, Plattform, API oder MCP als Systemquelle ausgewertet oder angebunden wird | `legacy-systeme-integration` |
| Direktauftrag, fehlende Bekanntmachung, Interimsauftrag, unterschriebener Vertrag, laufende Leistung, Verlängerung oder Nachtrag betroffen ist | `de-facto-vergabe-135-gwb` |
| Unterlagen, LV, GAEB, XML, Excel, PDF, Formatvorgabe oder Uploadformat fehlerhaft sind | `unterlagen-lv-formatangriff` |
| Bekanntmachung, Frist, Zugang, Portalveröffentlichung oder Fristverlängerung angegriffen wird | `bekanntmachung-fristen-und-zugang` |
| Abhilfe, Rückversetzung, Vergleich, Reparatur, Protokollierung oder Verhandlungsfenster möglich ist | `vergleich-und-abstellungsstrategie` |
| Gebühren, Streitwert, Vorschuss, Kostenerstattung, Schadensersatz oder entgangener Gewinn bewertet werden | `kosten-und-schadensersatzrisiko` |
| VK-Beschluss angegriffen, OLG-Notfrist berechnet oder Beschwerdeziel formuliert werden muss | `sofortige-beschwerde-olg-vergabesenat` |

## Zulässigkeitsdreieck

Vor jedem Rügeschreiben, Nachprüfungsantrag oder OLG-Briefing drei Achsen getrennt prüfen:

1. Antragsbefugnis: Interesse am Auftrag, behauptete Verletzung bieterschützender Vergabevorschriften, drohender Schaden und plausible Zuschlagschance.
2. Präklusion: Kenntnis, Erkennbarkeit aus Bekanntmachung oder Vergabeunterlagen, rechtzeitige Rüge, Nichtabhilfe und 15-Kalendertage-Frist.
3. Kausalität und Rechtsfolge: Der Fehler muss die Wettbewerbsposition berühren; der Antrag muss eine konkrete Maßnahme erreichen können, etwa Rückversetzung, neue Wertung, Ausschluss, Berichtigung oder Zuschlagsverbot.

Zuschlagssperre nicht nur behaupten: Zeitpunkt des § 134 GWB-Schreibens, Eingang des VK-Antrags, Information der Vergabekammer an den Auftraggeber, Ablauf der Stillhalte- und Beschwerdefrist sowie etwaige Gestattungsanträge getrennt in die Fristenampel aufnehmen.

## Rechtsprechungsrouting

| Angriff | Anker |
|---|---|
| Typ-, Produkt-, Maß-, System- oder Formatvorgabe | EuGH C-568/24, Sof Medica; EuGH C-424/23, DYKA Plastics |
| Planungswettbewerb | EuGH C-888/24, Adão da Fonseca: kein allgemeines Anhörungsrecht; Anonymitätsbruch, Kriterienabweichung oder ungleicher Klarstellungsdialog prüfen |
| Bestandskompatibilität als Gegenargument | OLG Düsseldorf Verg 2/24; funktionale Anschluss- und Migrationsalternative nötig |
| Unterlagen-/Uploadbeweis | OLG Düsseldorf Verg 47/18; § 53 VgV und Portalvorgabe; C-534/23 P/C-539/23 P Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe |
| Wertungsdaten oder begrenzter Einblick | BGH X ZB 3/17, OLG Düsseldorf Verg 34/20 und Verg 36/23: offene Punkteskala nicht pauschal angreifen; Maßstabsabweichung, Indiz, Dokumentationsziel und Punktwirkung konkretisieren |
| Direktvergabe, Exklusivrecht, technischer Alleinanbieter | EuGH C-578/23, Generální finanční ředitelství |
| privater Projektinitiator mit zweiter Zuschlagschance | EuGH C-810/24 Urban Vision: nachträgliches Matching-/Anpassungsprivileg angreifen; Markterkundung oder private Initiative nicht pauschal verbieten |
| Bus-ÖPNV an internen Betreiber | EuGH C-856/24 Sad Trasporto Locale II: Betriebsrisiko der Art.-5-Abs.-2-Route und allgemeine Inhouse-Ausnahme getrennt prüfen |
| Wechselseitiger Angebotsangriff | EuGH C-100/12 Fastweb, C-689/13 PFE, C-497/20 Randstad Italia |
| Nur-Preis-Wertung bei personalintensiver Leistung | EuGH C-769/23, Mara, nur wenn eine konkrete nationale Sonderregel als Rechtsbrücke besteht |
| Rahmenvereinbarung, Konzession, Auftragnehmerwechsel | EuGH C-282/24 Polismyndigheten, C-452/23 Fastned Deutschland, C-461/20 Advania Sverige |
| Änderung nach möglichem Vertragsende | EuGH C-820/24 Strominator: vollständige Leistung, endgültige Abnahme und Schlussrechnung belegen |
| Sanktionsangriff | EuGH C-313/24 Opera Laboratori: konkrete Kontroll- oder Mittelumleitungsindizien statt Nationalitätsvortrag |
| bußgeldbezogene Register-/Ausschlussfolge | EuGH C-590/24 AK Dlhopolec nur zur Sanktionsbemessung; Vergabeausschlussfragen waren unzulässig |
| Bietergemeinschaft und Steuer-/Sozialabgabenproblem | GA Kokott C-268/25, nur Schlussanträge |
| VK-Praxis der letzten zehn Jahre | `references/praxisrechtsprechung-vk-2016-2026.md` für Rügepräklusion, Substantiierung, Wertungsdokumentation, Preisaufklärung, Akteneinsicht und Rahmenvereinbarungen |

## Rechtsprechungsfeste Hauptarbeit

Jeder Konkurrentenangriff braucht Frist, Aktenbeleg, Norm, Rechtsprechungsanker, Kausalität, Zuschlagschance und Antrag. Ohne diese sieben Punkte keinen Schriftsatz ausformulieren.

| Angriffslage | Normen | Prüffrage | Pflichtoutput |
|---|---|---|---|
| Billigzuschlag/Preisautomatismus | §§ 127, 160 GWB, § 60 VgV; BGH X ZB 3/17 und X ZB 10/16; C-769/23 Mara nur bei konkreter Sonderregel | Wurden veröffentlichte Qualitätskriterien unverändert und konkret begründet angewandt, besteht ein Sonderverbot der Nur-Preis-Wertung oder wurde ein auffälliger Preis nicht aufgeklärt? | Getrennte Rüge-/VK-Bausteine für konkrete Qualitätswertung, Sonderregel und Niedrigpreisaufklärung mit jeweiliger Kausalität |
| Produkt-/Formatbindung | § 31 VgV; EuGH C-568/24 Sof Medica; EuGH C-424/23 DYKA Plastics; OLG Düsseldorf Verg 2/24 | Sperrt Typ, Maß, Hersteller, Material, Schnittstelle, GAEB/XML/Excel/PDF oder Pflichtfeld ohne gleichwertige Öffnung; ist Bestandskompatibilität konkret belegt? | Gleichwertigkeitsangriff mit LV-Fundstelle, funktionaler Anschluss-/Migrationsalternative, Risikowiderlegung und Berichtigungsantrag |
| Netto-Null-Technologien | Art. 25 VO (EU) 2024/1735; VO (EU) 2026/718 | Fehlen Windrotorblattquote oder Bau-Zusatzpflicht, wird die Windregel überschießend übertragen, oder fehlen Kommissionsfeststellung, GPA-Prüfung beziehungsweise Ausnahmebeleg? | Rüge-/VK-Matrix mit Technologie, Starttag, LV-Fundstelle, Kausalität und passender Berichtigung oder Rückversetzung |
| Bundeswehrbeschaffung | §§ 1 bis 19 BwBBG, GWB und VSVgV; § 11 und § 15 Abs. 2 BwBBG | Ist der Auftrag erfasst und der Antragsteller zugangsberechtigt; sind Ausnahme, Dringlichkeit, Losroute, Nachforderung, Drittstaatenfilter und Vorab-Rüge tragfähig? | Zulässigkeits-Gate, Kenntnis-/Rügechronologie, Akteneinsicht, VK-Bund-Antrag, §-10-Sanktionsposition und OLG-Reserve |
| Planungswettbewerb | §§ 78 bis 80 VgV; EuGH C-888/24 Adão da Fonseca | Wurden Anonymität, Kriterienbindung und gleicher protokollierter Klarstellungsdialog gewahrt? | Rüge-/VK-Baustein zum konkreten Verfahrensfehler; kein Antrag auf allgemeine Anhörung vor der Rangfolge |
| System-/Portalbeweis | § 41, § 53 VgV, § 165 GWB; Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe; OLG Düsseldorf Verg 47/18, Verg 34/20 und Verg 36/23 | Ist die Herkunft zulässig, das Original unverändert, der Tatsachenkern konkret und die fehlende interne Information als Akteneinsichtsziel benannt? | Beweiskette, Hash-/Transformationsmanifest, Gegenhypothese, Akteneinsichtsantrag und Anlagenpaket |
| Direktauftrag/Exklusivität | §§ 135, 160 GWB; EuGH C-578/23 | Ist Alleinstellung durch frühere Verträge, Datenhaltung, Rechte oder Schnittstellen des Auftraggebers selbst geschaffen? | § 135-/Eilantragspfad mit Lock-in-Historie, Marktalternative und Frist |
| Änderung nach Vertragsende | §§ 132, 135, 160 GWB; C-820/24 Strominator | Sind vollständige Leistung, endgültige Abnahme und Schlussrechnung belegt, sodass eine offene Zahlung die Laufzeit nicht verlängert? | Laufzeit-Beweismatrix und Unwirksamkeits-/Neuvergabeantrag |
| Eignung/Ausschluss/Sanktion | §§ 123 bis 125 GWB; Vossloh; C-268/25 nur Schlussanträge; C-313/24 Opera Laboratori | Gibt es belastbare Hinweise zu Register, Selbstreinigung, BG-Mitglied, faktischer Kontrolle oder Mittelumleitung? | Akteneinsichtsziel, Beweismatrix und passende Ausschluss-/Neuwertungsfolge |
| Akteneinsicht/Schwärzung | § 165 GWB; EuGH C-54/21 Antea Polska, C-927/19 Klaipedos, C-450/06 Varec | Welche Information ist für Antragsbefugnis, Kausalität oder Zuschlagschance entscheidungserheblich? | Akteneinsichtsantrag mit Schwärzungsangriff und Begründungsersatz |

## Outputstandard

Liefere zuerst Kurzlage, rote Fristen, Angriffsziel, Zulässigkeit, Belege, Risiko und genau einen empfohlenen nächsten Output.

## Juristische Argumentationsarchitektur

Jeden Konkurrentenangriff in acht Stufen bauen:

1. veröffentlichter Maßstab oder bieterschützende Norm;
2. objektiv feststellbarer Tatsachenkern;
3. daraus gezogener Indizschluss;
4. stärkste rechtmäßige Gegenhypothese;
5. eigenes Angebot und verletzte Wettbewerbsposition;
6. mögliche Punkt-, Rang- oder Ausschlussfolge;
7. konkret bezeichnetes Akteneinsichtsziel;
8. erreichbarer Antrag.

Jede entscheidende Fundstelle zusätzlich als `Quellenstatus | Aussagegehalt und Bindungsstatus | Referenzfall | eigener Tatsachenkern | Übertragung | Wettbewerbs- und Rechtsschutzfolge` ausweisen. Bei einem anhängigen Verfahren ohne Entscheidung nur Vorlagefrage und Verfahrensstand angeben. Unverifizierte Fundstellen bleiben Rechercheaufträge; Schlussanträge werden nicht als Urteil behandelt und eine passende Entscheidung ersetzt keinen greifbaren Tatsachenkern.

Fehlt eine Stufe, keine ausformulierte Behauptung erzeugen. Stattdessen die offene Stufe als Belegauftrag ausgeben und `nachpruefungsantrag-konkurrent-vk` laden.

## Nutzungscheck

- Ist die rote Frist berechnet oder als Lücke markiert?
- Gibt es für jeden Angriff Beleg, Akteneinsichtsziel oder Beweis-Cluster?
- Ist der Antrag eindeutig als Rüge, VK-Antrag, Eilantrag, Akteneinsicht, OLG oder Kostenmemo geroutet?
- Ist die nächste Anlage, Freigabe oder Gerichtshandlung klar?
