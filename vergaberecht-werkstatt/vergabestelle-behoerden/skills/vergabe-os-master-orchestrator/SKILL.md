---
name: vergabe-os-master-orchestrator
description: 'Primärer Kaltstart ohne Skillwahl für jeden neuen Vergabestellenfall mit Ordner, ZIP, mehreren Dateien oder Systemexport. Immer zuerst einsetzen, wenn die Aufgabe noch nicht eng abgegrenzt ist. Sichert Fristen und Regime, ordnet Quellen, LV, Bestangebot, Upload und Rechtsschutz und routet danach gezielt zu höchstens drei Fachskills.'
---

# Vergabestellen-Cockpit: sichert Verfahren, Fristen, Unterlagen, Wertung, Rechtsschutz und Veröffentlichung.

**Arbeitsname:** Neuer Vergabestellenfall automatisch vorbereiten, ordnen und in den ersten Behördenoutput führen.

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

Fokus: Vergabestellen-Cockpit für Bedarf, datenbasierte Priorisierung, Bündelung, Bekanntmachung, LV-Formate, Wertung, Rügeabwehr, VK-/OLG-Verteidigung, Berichtigung und Uploadpaket.

## Abgrenzung

Dieser Master ist der automatische Einstieg für einen vollständigen Ordner, ein ZIP, einen Portal-/DMS-Export, mehrere Dokumente oder mehrere miteinander verbundene Arbeitsfragen. Für genau ein Dokument oder eine konkrete Einzelfrage genügt `workflow-kaltstart-und-routing`; ohne Unterlagen und nur zur ersten Rollen-/Regimeorientierung gilt `einstieg-routing`.

## Null-Konfigurations-Vertrag

1. Formulierungen wie `neuer Fall`, `bitte vorbereiten`, `prüfe alles` oder `mach, was nötig ist` sind ein vollständiger Arbeitsauftrag. Nicht nach einem Skill, Modus oder Ausgabeformat fragen.
2. Zuerst alle sichtbaren Datei-, Portal- und Systemangaben auslesen. Bereits erkennbare Rolle, Frist, Auftragsgegenstand, Verfahrensstand oder Ziel nicht erneut erfragen.
3. Noch vor der Tiefenprüfung die fünf Zeilen `Lage | Rot | Akte | Rechtsweiche | Jetzt` ausgeben. Bei Unsicherheit mit gekennzeichneter Arbeitshypothese fortfahren.
4. Höchstens drei echte Blockerfragen gesammelt und erst nach dem ersten Arbeitsstand stellen. Jede Frage muss benennen, welche Behördenentscheidung ohne die Antwort offenbleibt.
5. Bei größeren Beständen vor dem vertieften Auslesen kurz Paketumfang, Prioritätsdateien und nächsten Checkpoint nennen. So bleibt der Fortschritt sichtbar und fortsetzbar.

## Routingbudget

Pro Arbeitsdurchgang diesen Master und höchstens drei Fachskills einsetzen: einen für die leitende Rechtsfrage, einen für Beleg oder Format und einen für den konkret zu erstellenden Output. Nicht den gesamten Skillbestand laden. Zu jedem geladenen Fachskill in einem Halbsatz nennen, welche Entscheidung oder Datei er in diesem Durchgang erzeugt; weitere Skills erst in einem späteren Durchgang nach einem neuen Tatsachenbefund ergänzen.

## 90-Sekunden-Erstantwort

Noch vor jeder längeren Prüfung genau diese fünf Zeilen liefern:

| Feld | Vergabestellenantwort |
|---|---|
| Lage | Verfahren, Phase, Auftraggeberrolle und erkannter Hauptkonflikt in einem Satz |
| Rot | früheste belastbare Frist oder Sperre mit Startpunkt und Aktenbeleg; sonst ausdrücklich `nicht berechenbar` |
| Akte | drei tragende Dateien/Felder und die wichtigste fehlende Unterlage |
| Rechtsweiche | anwendbares Regime plus eine entscheidende Norm oder verifizierte Leitentscheidung |
| Jetzt | genau ein erster Behördenoutput und genau eine verantwortliche Bedienhandlung |

### Vergabe-OS Master-Orchestrator

## Bedienbarkeitsregel

Jeder Lauf startet mit einer Ein-Bildschirm-Lage und endet mit einer Bedienhandlung: Entscheidung, Freigabe, Datei, Upload, Schriftsatz oder Aktenvermerk. Genau einen Output empfehlen, höchstens zwei Alternativen nennen und keine längere Begründung ohne Dashboard, Matrix oder Checkliste beginnen.

## Startbildschirm

Beginne komplexe Fälle als geführte Oberfläche, nicht als Textgutachten. Kläre in dieser Reihenfolge:

1. Was liegt vor? Bedarfsanforderung, Bekanntmachung, Unterlagen, LV, GAEB, XML, Excel, PDF, Bestands-/Zustandsdaten, PMS/BMS, Planungsdaten, Bestandsplan, BIM/Fachmodell, Kosten-/Nachtragsdaten, Genehmigungsplattform, Netz-, Klima-/Umweltdaten, Normen, Bieterfrage, Rüge, VK-Schriftstück, Beschluss oder Portalnachweis.
2. Welche Rolle? Vergabestelle, Fachbereich, Justiziariat, Zentrale Vergabestelle, Fördermittelempfänger, Beigeladene oder beauftragte Stelle.
3. Welcher Verfahrensstand? Planung, Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Nachprüfung, OLG, Vertrag oder Interimsbedarf.
4. Welches Ziel? Portfolio priorisieren, Bündelung prüfen, schneller beauftragen, LV bauen, Bestangebot sichern, Risiko navigieren, Abhilfe leisten, Verfahren verteidigen, Berichtigung veröffentlichen oder Kostenrisiko begrenzen.
5. Welcher Output? Vermerk, Entscheidungsvorlage, Rügeerwiderung, VK-Stellungnahme, OLG-Erwiderung, Tabelle, Checkliste oder Uploadpaket.

Wenn Dateien vorliegen, beantworte diese fünf Punkte soweit möglich selbst und frage nur echte Lücken ab.

## Ordnerfall-Kaltstart ohne Skillwahl

Wenn der Nutzer nur einen Projektordner, ZIP, DMS-Export, Portalexport oder Dateistapel mit einer Formulierung wie `neuer Fall`, `bitte vorbereiten` oder `mach, was nötig ist` übergibt, nicht nach einem Skill fragen. Arbeite den Fall selbst an und route erst danach intern.

1. Datei- und Quelleninventar bilden: Dateiname, Typ, Datum, Version, Urheber, Portalzeitstempel, Hash, Bezug zu Bekanntmachung, LV, Angebot, Wertung, Rüge, VK/OLG oder Vertrag.
2. Marktrolle und Verfahrensstand aus Unterlagen ableiten: Vergabestelle, Fachbereich, Zentrale Vergabestelle, Justiziariat, Fördermittelempfänger oder beauftragte Stelle; Planung, Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Nachprüfung, OLG oder Vertragsphase.
3. Rote Fristen und Sperren zuerst sichern: Angebotsfrist, Bieterfragenfrist, Rüge, Nichtabhilfe, Zuschlagssperre, Beschwerdefrist, § 135 GWB, Fördermittel- oder Gremienfrist.
4. Daten- und Formatlage erkennen: GAEB, XML, Excel, PDF, BIM, SAP/ERP/AVA/DMS, PMS/BMS, Portal, API, MCP, eForms/TED/DVAL, Uploadquittung, Rückkanal. Für jedes tragende Feld führende Quelle, Stichtag, Einheit, Transformation und Fachfreigabe bestimmen.
5. Erste Output-Weiche setzen: Verfahren reparieren, Unterlagen/LV bauen, Bestangebot sichern, Bieterfrage beantworten, Rüge abhelfen/nicht abhelfen, VK verteidigen, OLG vorbereiten, Berichtigung/Uploadpaket erstellen.

Pflichtausgabe beim Ordnerfall: Fallkarte, Fristenampel, Dokumentenmatrix, Belegmatrix, Lückenliste, Quellenstatus, empfohlener erster Behördenoutput und genau eine nächste Bedienhandlung. Nutze `assets/templates/ordnerfall-startprotokoll.md` und `assets/templates/fallkarte-output-weiche.md`.

## Stabiler Großakten- und Fortsetzungsmodus

1. Ab 50 Dateien oder 250 MB zuerst einen reinen Metadatenlauf ausführen; Bekanntmachung, Fristdokumente, Rügen und Beschlüsse priorisieren.
2. Danach Pakete von höchstens 20 Dateien oder 100 MB verarbeiten. Große PDF-, Office-, GAEB- oder BIM-Dateien einzeln öffnen; nicht gleichzeitig rendern, konvertieren und exportieren.
3. Nach jedem Paket ein Checkpoint-Register `Datei | Hash | Status | Ergebnis | Fehler | nächster Lauf` fortschreiben. Eine Datei mit unverändertem Hash nicht erneut auslesen.
4. Beschädigte, verschlüsselte oder nicht unterstützte Dateien als Lücke mit Ersatzanforderung protokollieren. Der übrige Fall wird weiterbearbeitet.
5. Bei Abbruch am letzten vollständigen Checkpoint fortsetzen. Upload-, PDF- und Gesamtpakete erst nach fachlicher Freigabe der zugrunde liegenden Einzelprodukte erzeugen.

## Sofortmodus

1. Rolle klären: Vergabestelle, Fachbereich, Justiziariat, Zentrale Vergabestelle, Fördermittelempfänger, Beigeladene oder beauftragte Stelle.
2. Verfahrensstand klären: Markterkundung, Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Zuschlag, Vertrag, Nachprüfung, Beschwerde oder Schadensersatz.
3. Schwellenwert und Rechtsweg prüfen: Oberschwelle, Unterschwelle, Sektoren, Konzession, Verteidigung/Sicherheit, Fördermittel oder Sonderregime.
4. Quellen- und Systemlage prüfen: Bauwerksregister, PMS/BMS, Planungsdaten, Bestandspläne, BIM, Nachträge, Kosten, Behördenfeedback, Bundesvergabe, Genehmigungsplattformen, Netzdaten, Klima-/Umweltdaten, Normen, Rechtsprechung, SAP/ERP/AVA/DMS, Portal, API oder MCP. Tatsache, Annahme und Entscheidung getrennt führen.
5. Fristen sichern: Rüge, Angebotsfrist, Stillhaltefrist, 15-Kalendertage-Frist nach Nichtabhilfe, Beschwerdefrist, § 135 GWB-Fristen.
6. Erst danach in die materielle Prüfung gehen.

## Pflicht-Output

- Entscheidungssatz mit Go, Go unter Auflage oder Stop.
- Fristen-, Akten- und Freigabeampel.
- Prüfmatrix aus Tatsache, Norm, Aktenbeleg, Gegenargument und Rechtsfolge.
- Vollständiges Arbeitsprodukt plus verantwortlicher nächster Schritt.
- Keine Textwüste: vor längerer Begründung zuerst eine Tabelle, ein Dashboard oder ein Output-Menü liefern.

## Antwortstandard

Starte umfangreiche Antworten in dieser Struktur:

| Abschnitt | Inhalt |
|---|---|
| Kurzlage | drei Sätze zu Verfahren, Stand, Behördenziel |
| Rote Fristen | Frist, Startpunkt, Ablauf, Aktenbeleg, Sofortmaßnahme |
| Arbeitsdashboard | relevante Applets mit wichtigstem Befund, Aktenlücke, nächstem Schritt |
| Output-Auswahl | eine Empfehlung und maximal zwei Alternativen |

## Dashboard- und Applet-Modus

Wenn der Fall mehr als einen Rügepunkt, mehrere Lose, mehrere Datenformate oder ein laufendes VK-/OLG-Verfahren betrifft, nicht mit Fließtext starten. Zuerst ein kompaktes Arbeits-Dashboard ausgeben:

| Kachel | Inhalt |
|---|---|
| Fristenampel | Angebotsfrist, Bieterfragen, Rügen, § 134 GWB, Nichtabhilfe, Zuschlagssperre, OLG-Beschwerde, § 135 GWB |
| Dokumentenmatrix | Bekanntmachung, Vergabeunterlagen, LV/GAEB/XML/Excel/PDF, Angebote, Wertung, Portalprotokolle, Anlagen |
| Belegmatrix | Entscheidung, Aktenstelle, Datei, Seite/Position, Begründung, Nachweiswert, Lücke |
| Wirklichkeitsdaten | Quelle/Feldautorität, Originalschlüssel, Objekt, Befund, Stand/Einheit, Transformation, Datenqualität, Vergabefolge, Fachfreigabe |
| Portfolio | Objekt, Zustand, Ausfallwirkung, Korridor, Budget, Priorität, Bündelung |
| Beschleunigung | Auftragswert, Landeswertgrenze, Anbieterfeld, Dringlichkeit, Binnenmarktrelevanz, Dokumentation |
| Mobilität/Tragfähigkeit | Bauwerk, Netz, Korridor, Tragfähigkeit, Sperrfenster, Nutzungsrisiko |
| Varianten | Einzelvergabe, Bündelung, Rahmen, ÖPP, CAPEX, Fertigteil/Serie, Lebenszyklus |
| Angriffslinien | Rügepunkt, Tatsache, Norm, behauptete Kausalität, begehrte Abhilfe, Eilrisiko |
| Verteidigungslinien | Dokumentationsbeleg, Wertungsspielraum, Gleichbehandlung, Transparenz, Präklusion, Heilung |
| Wertungsmatrix | Kriterium, Gewicht, Bewertung, Dokumentation, Fehlerverdacht, Reparaturpfad |
| Legacy-/MCP-Integrationscheck | Herkunft, Quellsystem, Feldautorität, Schlüssel, Stand/Zeitzone, Schema/Einheit, Hash, Transformation, Rechtszweck, Zielsystem, Freigabe, Rückmeldung |
| Upload-/Formatexport-Check | Zielformat, Portal, Feldliste, Dateiname, Hash, Freigabe, Uploadnachweis |
| Output-Weiche | Abhilfe, Nichtabhilfe, Berichtigung, Fristverlängerung, Stellungnahme VK, Vergleich, OLG-Erwiderung, Uploadauftrag |

Nutze für umfangreiche Fälle `assets/templates/ordnerfall-startprotokoll.md`, `assets/templates/fallkarte-output-weiche.md`, `assets/templates/startbildschirm-applet-dashboard.md`, `assets/templates/vergabe-master-padlet.md` oder `assets/templates/vk-olg-streitdashboard.md` als Vorlage. Das Dashboard ist ein Arbeitsprodukt, kein dekorativer Zusatz.

## Aktuelle Rechtsprechungsweichen

| Lage | Sofortanker |
|---|---|
| Verfahrensart ohne Bekanntmachung | EuGH C-578/23, Generální finanční ředitelství |
| Typ-, Produkt-, Maß-, Material- oder Schnittstellenvorgabe | EuGH C-568/24, Sof Medica; EuGH C-424/23, DYKA Plastics |
| Planungswettbewerb, Anonymität, Anhörung | EuGH C-888/24, Adão da Fonseca: kein Anhörungsanspruch vor der endgültigen Rangfolge; Klarstellungen nur im vorgesehenen anonymen Dialog |
| Bestandskompatibilität und gewachsene IT | OLG Düsseldorf Verg 2/24; konkreter Bestands-, Migrations-, Sicherheits- und Gewährleistungsbefund |
| Unterlagenzugang und fristfester Upload | OLG Düsseldorf Verg 47/18; § 53 VgV und Portalvorgabe; C-534/23 P/C-539/23 P Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe |
| qualitative und datenbasierte Wertung | BGH X ZB 3/17 und OLG Düsseldorf Verg 34/20; offene Punkteskala nicht vorschnell verwerfen, aber Angebotsfundstelle, konkrete Gründe, Quervergleich und Punktefolge dokumentieren |
| Netto-Null-Technologie, Windrotorblatt oder Resilienz | Art. 25 VO (EU) 2024/1735 und VO (EU) 2026/718; `netto-null-technologien-vergabe` laden |
| Bundeswehr-, Verteidigungs-, Sicherheits- oder VSVgV-Beschaffung | seit 14.02.2026 geltendes BwBBG einschließlich § 19-Übergang, Drittstaaten- und Sonderrechtsschutz; `bundeswehrbeschaffung-bwbbg-2026` laden |
| privater Initiator einer Konzession oder Projektfinanzierung | EuGH C-810/24 Urban Vision: kein nachträgliches Matching- oder Anpassungsprivileg; private Initiative und Kostenerstattung nicht pauschal verbieten |
| Personalintensive Nur-Preis-Wertung | EuGH C-769/23, Mara, nur zur Zulässigkeit einer nationalen Beschränkung; anwendbare Sonderregel zuerst |
| Vertragsänderung, Rahmenvereinbarung, Konzession | EuGH C-454/06 pressetext, C-282/24 Polismyndigheten, C-452/23 Fastned Deutschland |
| Ende der Vertragslaufzeit vor § 132 | EuGH C-820/24 Strominator: vollständige Leistung, endgültige Abnahme und Schlussrechnung; offene Zahlung unerheblich |
| Auftragnehmerwechsel nach Insolvenz | EuGH C-461/20 Advania Sverige und § 132 Abs. 2 Satz 1 Nr. 4 Buchstabe b GWB |
| Inhouse-Konzernmutter | EuGH C-692/23 AVR-Afvalverwerking: Gruppenumsätze und gegebenenfalls konsolidierten Umsatz einbeziehen |
| Bus-ÖPNV an internen Betreiber | EuGH C-856/24 Sad Trasporto Locale II: für die Sonderroute nach Art. 5 Abs. 1 und 2 VO (EG) 1370/2007 tatsächliche Betriebsrisikoübertragung prüfen; allgemeines Inhouse-Recht getrennt halten |
| EU-Sanktionskontrolle | EuGH C-313/24 Opera Laboratori: faktische Kontrolle und plausible Mittelumleitung statt Nationalitätsautomatismus |
| bußgeldbezogene Register- oder Ausschlussfolge | EuGH C-590/24 AK Dlhopolec nur für Rechtssicherheit und Sanktionsbemessung; Vorlagefragen zum Vergabeausschluss waren unzulässig |
| EU-finanzierte Vergabe und Finanzkorrektur | EuGH C-186/25 Institut po ribni resursi Varna: Förderregime, Vertragsvollzug, Finanzbezug, Begründung und Verhältnismäßigkeit individualisieren; kein allgemeiner Rückforderungsautomatismus |
| Bietergemeinschaft, Steuer-/Sozialabgabenverstoß | GA Kokott C-268/25 nur als Schlussanträge |
| VK-Praxis der letzten zehn Jahre | `references/praxisrechtsprechung-vk-2016-2026.md` für Rügepräklusion, Substantiierung, Wertungsdokumentation, Preisaufklärung, Akteneinsicht und Rahmenvereinbarungen |

## Rechtsprechungsfeste Hauptarbeit

Diese Weichen sind nicht nur Fundstellen. Jede Antwort muss sie in eine behördliche Prüfhandlung übersetzen:

| Arbeitslage | Normen | Prüffrage | Behördenoutput |
|---|---|---|---|
| Zuschlagsarchitektur | § 127 GWB, § 58 VgV, Art. 67 RL 2014/24/EU; BGH X ZB 3/17; EuGH C-769/23 Mara nur zur Zulässigkeit nationaler Beschränkungen; EuGH C-210/24 AESTE für ein enges Sozialkriterium | Verbietet eine Sonderregel Preis allein? Tragen Qualität, Personal, Reaktionszeit, Verfügbarkeit, Termin oder Lebenszykluskosten den Auftragserfolg, und lässt sich die qualitative Würdigung konkret dokumentieren? | Bestwertungsplan mit Rechtsgrund, Gewichtung, Preisformeltest, Punkteankern, Dokumentationsblatt und Szenario Billig-schwach/teurer-stark |
| Netto-Null-Technologien | Art. 25 VO (EU) 2024/1735; VO (EU) 2026/718 | Richtlinienbereich, Buchstaben a bis k, Starttag, Windrotorblattquote, Bau-Zusatzpflicht, Kommissionsfeststellung, GPA und Ausnahme belegt? | Anwendungsampel, LV-/Komponentenmatrix, veröffentlichungsreife Klausel, Nachweis-/Kontrollplan und Ausnahme- oder Reparaturvermerk |
| Bundeswehrbeschaffung | §§ 1 bis 19 BwBBG, GWB und VSVgV; § 19-Übergang und aktueller Normtext | Sind Bedarf, Auftraggeber, Schwelle und Zeit erfasst; welche einzelne Sondernorm verdrängt welchen regulären Ausgang; sind Ausnahme, Lose, Nachweise, Drittstaaten, Vorab-Rüge und Vertragsänderung belegt? | BwBBG-Freigabevermerk mit Anwendungsbereich, Sonderroute, Qualität/Tempo, Drittstaatenmatrix, Rechtsschutzfristen und Vertragsklauseln |
| Leistungsbeschreibung und Datenformat | § 31 VgV, § 121 GWB; EuGH 16.04.2026 C-568/24 Sof Medica; EuGH 16.01.2025 C-424/23 DYKA Plastics | Folgt der Detaillierungsgrad unvermeidbar aus dem Auftragsgegenstand, oder sperren Typ, Maß, Material, Produkt, GAEB/XML/Excel/PDF, Pflichtfeld oder Schnittstelle eine funktional gleichwertige Lösung? | Unvermeidbarkeits- und LV-Reparaturblatt mit Feldautorität, Sachgrund, Gleichwertigkeitsklausel, Alternative und Roundtrip-Test |
| Planungswettbewerb | §§ 78 bis 80 VgV; EuGH C-888/24 Adão da Fonseca | Bleiben Entwurf und Klarstellungsdialog anonym; wird statt eines vermeintlichen Anhörungsrechts nur das vorgesehene Preisgerichtsverfahren genutzt? | Wettbewerbsprotokoll mit Anonymitätscheck, Klarstellungsfragen und Rangfolgebegründung |
| Bestands- und Systemdaten | § 8, § 31, § 41 und § 53 VgV; OLG Düsseldorf Verg 2/24, Verg 47/18 und Verg 34/20; Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe | Trägt ein konkreter Bestandsbefund die Vorgabe, sind Datenanlagen direkt zugänglich, Uploads portal- und fristfest und Punkte durch Eingaben und Gründe nachvollziehbar? | Systemübergabe-Vermerk mit Bestands-/Migrationsmatrix, Unterlagenzugang, Eingabebelegen, Freeze und Rückkanal |
| Ausnahme vom Wettbewerb | § 14 VgV, § 135 GWB; EuGH 09.01.2025 C-578/23 | Ist technische Exklusivität fremd verursacht oder durch frühere Beschaffung, Rechte, Datenhaltung oder Schnittstellen selbst geschaffen? | Ausnahmevermerk mit Lock-in-Historie, Marktsuche, Alternativen und Bekanntmachungsentscheidung |
| Preisaufklärung | § 60 VgV; BGH 31.01.2017 X ZB 10/16 | Besteht Preisabstand, Kalkulationsbruch oder Ausführungsrisiko, und ist die Aufklärung geheimnisschonend verwertbar dokumentiert? | Aufklärungsanforderung, Auswertungsvermerk und Wertungsfolge |
| Nachprüfung und Akteneinsicht | §§ 160, 165, 169, 171 GWB; EuGH C-54/21 Antea Polska, C-450/06 Varec | Welche Informationen sind entscheidungserheblich, welche sind Geschäftsgeheimnisse, und welcher Begründungsersatz ist nötig? | Aktenverzeichnis, Schwärzungsmatrix, Verteidigungslinie, VK-/OLG-Fristenblatt |
| Auftragnehmerwechsel/Insolvenz | § 132 Abs. 2 Satz 1 Nr. 4 Buchstabe b GWB; EuGH C-461/20 Advania Sverige, C-454/06 pressetext | Bleiben Gesamtcharakter, Leistung und Wettbewerbslage gleich, ist der Erwerber geeignet und liegt keine Umgehung vor? | § 132-Vermerk mit Eignungs-Recheck, Änderungsgrenze und Bekanntmachungsentscheidung |
| Laufzeit/Inhouse/Sanktion | §§ 108, 132 GWB; C-820/24 Strominator, C-692/23 AVR-Afvalverwerking, C-313/24 Opera Laboratori | Läuft der Auftrag noch; stimmt die Konzernumsatzquote; bestehen faktische Kontrolle oder Mittelumleitung statt bloßer Organ-Nationalität? | Laufzeit-Gate, Inhouse-Berechnungsblatt oder Kontroll-/Zahlungsflussmatrix |
| Bus-ÖPNV-Direktvergabe | Art. 5 Abs. 1 und 2 VO (EG) 1370/2007; § 108 GWB; EuGH C-856/24 Sad Trasporto Locale II | Geht echtes Nachfrage-, Kosten-, Erlös- oder Verlustrisiko über; welche Direktvergabe- oder Inhouse-Route wird tatsächlich genutzt? | Risikotransfer-, Rechtsweg- und Direktvergabe-Vermerk |
| EU-Förderkorrektur | konkreter Förderrechtsakt, Bescheid, Vergaberecht und Vertragsklausel; EuGH C-186/25 Institut po ribni resursi Varna | Sind Pflicht, Vollzugsverstoß, Finanzbezug, Korrekturmethode und Verhältnismäßigkeit konkret belegt; verändert die Nichtdurchsetzung einer Vertragsstrafe die Gesamtart? | individualisierte Korrektur- und Verteidigungsmatrix ohne pauschale §-132- oder Rückforderungsfolge |

## VK-/OLG-Streitführung

Bei Streit vor Vergabekammer oder OLG immer zuerst diese Weichen sichern:

1. Zulässigkeit: Schwellenwert, zuständige Vergabekammer, Antragsbefugnis, Rügeobliegenheit, Frist.
2. Begründetheit: Rügepunkt, Aktenstelle, Dokumentationsbeleg, Wertungsspielraum, Kausalität, mögliche Heilung.
3. Eilbedarf: VK-Unterrichtung, Zuschlagsverbot und Ausnahmeantrag nach § 169 GWB, Interimsbedarf, Beschleunigungsinteresse und Beschwerdeausgang nach § 173 GWB.
4. Akteneinsicht und Geheimnisschutz: Aktenverzeichnis, Schwärzungen, Geschäftsgeheimnisse, Beigeladene.
5. Eskalation: Vergleichsfenster, sofortige Beschwerde, Schadensersatz, Kostenrisiko und Gremienfreigabe.

## Juristische Argumentationsarchitektur

Jede behördliche Entscheidung in dieser Reihenfolge schreiben:

1. Rechtsgrund und veröffentlichter Maßstab.
2. zum Entscheidungszeitpunkt festgestellte Tatsache mit Aktenfundstelle.
3. Subsumtion und fachliche Würdigung.
4. gleicher Maßstab für die Vergleichsgruppe.
5. stärkstes Bieterargument und aktenbasierte Antwort.
6. mildere Alternative, Kausalität und vollziehbare Rechtsfolge.

Jede entscheidende Fundstelle zusätzlich als `Quellenstatus | Aussagegehalt und Bindungsstatus | Tatsachenvergleich | Übertragungsgrenze | Aktenanschluss | Behördenfolge` ausweisen. Bei einem anhängigen Verfahren ohne Entscheidung nur Vorlagefrage und Verfahrensstand angeben. Eine unverifizierte Quelle oder bloße Sekundärwiedergabe wird zum Rechercheauftrag.

Prozessvortrag darf vorhandene Erwägungen und damalige Tatsachengrundlagen erläutern und Dokumentationslücken fallbezogen ergänzen. Die in BGH X ZB 4/10, Rn. 73, als gerichtlicher Hinweis entwickelte und in OLG Düsseldorf VII-Verg 28/14 als obiter dictum eingeordnete sowie angewandte Linie verlangt dabei Transparenz, Gleichbehandlung, Manipulationsschutz und wettbewerbskonforme Auftragserteilung; ein neues Unterkriterium, eine erst im Streit gebildete Entscheidung oder eine manipulativ nachgeschobene Tatsache bleiben unzulässig. Für diese Prüfung `vergaberecht-tatbestand-beweis-und-belege` laden.

## Typische Outputs

Kurzbild, Startbildschirm, Phasenkarte, Fristenampel, Dokumentenmatrix, Belegmatrix, Streitdashboard, Arbeitsrouting, Arbeitsplan, Vergabevermerk, Stellungnahme VK, OLG-Erwiderung, Uploadpaket, nächster Behörden-/Justiziariatsschritt.

## Daten- und Szenario-Weiche

Wenn vorhandene Datenquellen Bedarf, Priorisierung, Bündelung, LV, Budget oder Qualitätskriterien beeinflussen, `wirklichkeitsdaten-beschaffung-steuern` laden. Danach immer ausgeben:

- Quellen- und Datenqualitätsmatrix.
- Szenariovergleich mit Einzelvergabe, Bündelung, Rahmenvereinbarung, Abruf oder Verschiebung.
- Applet-Auswahl: Portfolio/Planung, beschleunigte Beauftragung, Vergaberechtsnavigation, Mobilität/Tragfähigkeit, Ausschreibungsstudio, ÖPP/CAPEX oder Fertigteil/Serie.
- Vergaberechtliche Wirkung: Bedarf, Schätzung, Losbildung, Leistungsbeschreibung, Eignung, Zuschlag oder Dokumentation.
- Nächster Freigabe- und Portalschritt.

## Nutzungscheck

- Ist die rote Frist berechnet oder als Lücke markiert?
- Ist der Freigabeinhaber benannt?
- Ist die nächste Datei, Aktenstelle oder Portalhandlung klar?
- Ist der empfohlene Output sofort als Vermerk, Tabelle, Schriftsatz oder Uploadauftrag nutzbar?

## Qualitätsgates

- Nur veröffentlichte Maßstäbe und nachweisbare Tatsachen verwenden.
- Rechtsstand, Fristen und tragende Entscheidungen gegen prüfbare Quellen absichern.
- Gleichbehandlung und dokumentierte Vergleichsgruppe kontrollieren.
- Freigabe erst bei reproduzierbarer Entscheidung und vollständigem Rückkanal.

## Anschlussmodule

- `vergabe-os-master-orchestrator` für Gesamtsteuerung.
- `quellen-livecheck`, `schnittstelle-zahlen-schwellen-und-berechnung` und `schwellenwerte-2026-2027-livecheck` für tragende Normen, Rechtsprechung, Beträge, Lose, Wertgrenzen und Rechtsweg.
- `workflow-chronologie-und-belegmatrix` für Aktenarbeit.
- `legacy-systeme-integration` für Feldautorität, SAP, ERP, AVA, DMS, Bauwerks-/PMS-/BIM-Daten, Portal, API, MCP, Datenumschlag, Entscheidungsbrücke, Hash, Delta, Freigabe und Rückkanal.
- `wirklichkeitsdaten-beschaffung-steuern` für Quelleninventar, gemeinsame Fachsprache, Priorisierung, Bündelung, Szenario, LV, Kriterien und Aktenvermerk.
- `bestangebot-durchsetzen`, `10-zuschlagsmatrix-aufbauen`, `17-wertung-leistung-preis` und `18-wertungsvermerk-erstellen` für Bestwertung statt Preisautomatismus.
- `vergabeunterlagen-lv-datenformate-bereitstellen`, `05-bekanntmachung-erstellen` und `bekanntmachung-berichtigung-und-upload-routing` für Unterlagen, eForms/TED/DVAL, Plattformen, Berichtigung und Quittung.
- `bieterfragen-antworten-management`, `22-ruegeerwiderung`, `23-stellungnahme-vergabekammer`, `26-akteneinsicht-vergabekammer` und `24-vorlage-an-den-vergabesenat` für Rüge, VK, Akteneinsicht, OLG und Vergleichslage.
- `markterkundung-und-vorbefassung`, `losbildung-mittelstandsfoerderung`, `rahmenvereinbarung-abrufe-mini-wettbewerb` und `inhouse-interkommunal` für Vorbereitung, Bündelung und Beschaffungsstruktur.
- `uvgo-unterschwellenvergabe`, `sektorenvergabe-sektvo`, `konzessionsvergabe-konzvgv` und `vob-a-bauvergabe` für Sonderregime.
