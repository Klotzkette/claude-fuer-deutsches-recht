---
name: vergabe-os-master-orchestrator
description: 'Primärer Kaltstart ohne Skillwahl für jeden neuen Bieterfall mit Vergabeordner, ZIP, mehreren Dateien oder Portalexport. Immer zuerst einsetzen, wenn die Aufgabe noch nicht eng abgegrenzt ist. Sichert Abgabe- und Rügefristen, ordnet LV, Nachweise, Freeze, Upload und Rechtsschutz und routet danach gezielt zu höchstens drei Fachskills.'
---

# Bieter-Cockpit: prüft Unterlagen, Formate, Fristen, Angebotsabgabe, Rüge, VK-Antrag und OLG-Strategie.

**Arbeitsname:** Neuer Bieterfall automatisch vorbereiten, Angebotsfähigkeit prüfen und nächsten Bieteroutput bauen.

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

Fokus: Bieter-Cockpit für Bekanntmachung, LV/GAEB/XML/Excel/PDF, Angebotsformat, Ausschlussrisiken, Rüge, Nachprüfung, Vergleich, OLG und Schadensersatz.

## Abgrenzung

Dieser Master ist der automatische Einstieg für einen vollständigen Ordner, ein ZIP, einen Portal-/Unternehmensexport, mehrere Dokumente oder mehrere verbundene Angebots- und Rechtsschutzfragen. Für genau ein Dokument oder eine konkrete Einzelfrage genügt `workflow-kaltstart-und-routing`; ohne Unterlagen und nur zur Rollen-/Regimeorientierung gilt `einstieg-routing`.

## Null-Konfigurations-Vertrag

1. Formulierungen wie `neue Bewerbung`, `neuer Fall`, `bitte vorbereiten`, `prüfe alles` oder `mach, was nötig ist` sind ein vollständiger Arbeitsauftrag. Nicht nach einem Skill, Modus oder Ausgabeformat fragen.
2. Zuerst alle sichtbaren Vergabe-, Unternehmens-, Portal- und Systemangaben auslesen. Bereits erkennbare Frist, Los, Eignungsanforderung, Rückgabeformat oder Angebotsziel nicht erneut erfragen.
3. Noch vor der Tiefenprüfung die fünf Zeilen `Lage | Rot | Angebot | Rechtsweiche | Jetzt` ausgeben. Bei Unsicherheit mit gekennzeichneter Arbeitshypothese fortfahren.
4. Höchstens drei echte Blockerfragen gesammelt und erst nach dem ersten Arbeitsstand stellen. Jede Frage muss benennen, welcher Angebots-, Freigabe- oder Rechtsschutzschritt ohne die Antwort offenbleibt.
5. Bei größeren Beständen vor dem vertieften Auslesen kurz Paketumfang, Prioritätsdateien und nächsten Checkpoint nennen. So bleibt der Fortschritt sichtbar und fortsetzbar.

## Routingbudget

Pro Arbeitsdurchgang diesen Master und höchstens drei Fachskills einsetzen: einen für die leitende Angebots- oder Rechtsfrage, einen für Beleg oder Format und einen für den konkret zu erstellenden Output. Nicht den gesamten Skillbestand laden. Zu jedem geladenen Fachskill in einem Halbsatz nennen, welche Angebotsdatei oder Verfahrenshandlung er in diesem Durchgang erzeugt; weitere Skills erst in einem späteren Durchgang nach einem neuen Tatsachenbefund ergänzen.

## 90-Sekunden-Erstantwort

Noch vor jeder längeren Prüfung genau diese fünf Zeilen liefern:

| Feld | Bieterantwort |
|---|---|
| Lage | Verfahren, Bieterrolle, Phase und Angebots- oder Rechtsschutzproblem in einem Satz |
| Rot | früheste Angebots-, Frage-, Rüge-, Stillhalte- oder Beschwerdefrist mit Startpunkt und Beleg; sonst `nicht berechenbar` |
| Abgabe | Leitdatei, Rückgabeformat, Portalweg, Freeze-Stand und wichtigste Lücke |
| Rechtsweiche | Regime plus entscheidende Norm, veröffentlichte Vorgabe oder verifizierte Leitentscheidung |
| Jetzt | genau ein erster Bieteroutput und genau eine verantwortliche Bedienhandlung |

### Vergabe-OS Master-Orchestrator

## Bedienbarkeitsregel

Jeder Lauf startet mit einer Ein-Bildschirm-Lage und endet mit einer Bieterhandlung: Angebotsteil, Freigabe, Datei, Upload, Rüge, Schriftsatz oder Entscheidung. Genau einen Output empfehlen, höchstens zwei Alternativen nennen und keine längere Begründung ohne Dashboard, Matrix oder Checkliste beginnen.

## Startbildschirm

Beginne komplexe Fälle als geführte Oberfläche, nicht als Textgutachten. Kläre in dieser Reihenfolge:

1. Was liegt vor? Bekanntmachung, Unterlagen, LV, GAEB, XML, Excel, PDF, Bieterfrage, Nachforderung, Ausschlussschreiben, Angebotsöffnung, Preisblattfehler, Rüge, Nichtabhilfe, Informationsschreiben, VK-Schriftstück, Beschluss oder Portalnachweis.
2. Welche Rolle? Bewerber, Bieter, Beigeladener, Zuschlagsprätendent, Nachunternehmer oder Kanzlei.
3. Welcher Verfahrensstand? Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Nachprüfung, OLG, Vertrag oder Schadensersatz.
4. Welches Ziel? Angebot retten, Unterlagen ändern, Ausschluss angreifen, Konkurrent ausschließen, Zuschlag stoppen, Akteneinsicht, Vergleich oder Kostenrisiko begrenzen.
5. Welcher Output? Schriftsatz, Rüge, Nachprüfungsantrag, Eilantrag, Tabelle, Checkliste, Memo, Angebotspaket oder Uploadpaket.

Wenn Dateien vorliegen, beantworte diese fünf Punkte soweit möglich selbst und frage nur echte Lücken ab.

## Ordnerfall-Kaltstart ohne Skillwahl

Wenn der Nutzer nur einen Projektordner, ZIP, Portalexport, Angebotsordner oder Dateistapel mit einer Formulierung wie `neuer Fall`, `bitte vorbereiten` oder `mach, was nötig ist` übergibt, nicht nach einem Skill fragen. Arbeite den Fall selbst an und route erst danach intern.

1. Datei- und Quelleninventar bilden: Dateiname, Typ, Datum, Version, Urheber, Portalzeitstempel, Hash, Bezug zu Bekanntmachung, LV, Angebotsbestandteil, Nachweis, Rüge, Nichtabhilfe, VK/OLG oder Vertrag.
2. Marktrolle und Verfahrensstand aus Unterlagen ableiten: Bewerber, Bieter, Zuschlagsprätendent, Beigeladener, Nachunternehmer oder Kanzlei; Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Nachprüfung, OLG, Zuschlag oder Schadensersatz.
3. Rote Fristen zuerst sichern: Angebotsfrist, Bieterfragenfrist, Rügefrist, Nichtabhilfe, Stillhaltefrist, Zuschlagssperre, Beschwerdefrist, § 135 GWB.
4. Angebots- und Formatlage erkennen: GAEB, XML, Excel, PDF, Portalformular, Signatur, Hash, SAP/ERP/CRM/HR/AVA/DMS, API/MCP, Nebenangebote, Referenzen, Konzepte, Eignungsnachweise. Verbindlichen Upload, nur ergänzenden Link, Quellstand, Gültigkeit und Freeze-Bedarf unterscheiden.
5. Erste Output-Weiche setzen: Go-No-Go, Bieterfrage, Angebotsmapping, Qualitätsvorsprung, Preisaufklärung, Rüge, VK-Antrag, Akteneinsicht, Vergleich, OLG, Uploadpaket.

Pflichtausgabe beim Ordnerfall: Fallkarte, Fristenampel, Dokumentenmatrix, Belegmatrix, Lückenliste, Quellenstatus, empfohlener erster Bieteroutput und genau eine nächste Bedienhandlung. Nutze `assets/templates/ordnerfall-startprotokoll.md` und `assets/templates/fallkarte-output-weiche.md`.

## Stabiler Großakten- und Fortsetzungsmodus

1. Ab 50 Dateien oder 250 MB zuerst einen reinen Metadatenlauf ausführen; Bekanntmachung, Angebotsfrist, Pflichtformulare und Portalvorgaben priorisieren.
2. Danach Pakete von höchstens 20 Dateien oder 100 MB verarbeiten. Große PDF-, Office- oder GAEB-Dateien einzeln öffnen; nicht gleichzeitig rendern, konvertieren und exportieren.
3. Nach jedem Paket ein Checkpoint-Register `Datei | Hash | Status | Ergebnis | Fehler | nächster Lauf` fortschreiben. Eine Datei mit unverändertem Hash nicht erneut auslesen.
4. Beschädigte, verschlüsselte oder nicht unterstützte Dateien als Angebots- oder Beweislücke mit Ersatzanforderung protokollieren. Fristprüfung und übriges Angebot laufen weiter.
5. Bei Abbruch am letzten vollständigen Checkpoint fortsetzen. Freeze-, Upload- und Gesamtpakete erst nach fachlicher Freigabe der zugrunde liegenden Einzelprodukte erzeugen.

## Sofortmodus

1. Rolle klären: Bewerber, Bieter, Beigeladener, Zuschlagsprätendent, Nachunternehmer oder Kanzlei.
2. Verfahrensstand klären: Markterkundung, Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Zuschlag, Vertrag, Nachprüfung, Beschwerde oder Schadensersatz.
3. Schwellenwert und Rechtsweg prüfen: Oberschwelle, Unterschwelle, Sektoren, Konzession, Verteidigung/Sicherheit, Fördermittel oder Sonderregime.
4. Bei Betrag, Losen, Optionen, Vertragslaufzeit, Rahmenvereinbarung, Wertgrenze oder unklarer Oberschwelle zuerst `schnittstelle-zahlen-schwellen-und-berechnung`, danach `schwellenwerte-2026-2027-livecheck` nutzen.
5. Fristen sichern: Rüge, Angebotsfrist, Stillhaltefrist, 15-Kalendertage-Frist nach Nichtabhilfe, Beschwerdefrist, § 135 GWB-Fristen.
6. Erst danach in die materielle Prüfung gehen.

## Pflicht-Output

- Handlungsempfehlung mit spätestem sicheren Zeitpunkt.
- Fristen-, Dokumenten- und Belegampel.
- Prüfmatrix aus Fundstelle, Norm, Betroffenheit, Schaden, Gegenargument und Abhilfe.
- Vollständiges Arbeitsprodukt plus Anlagen-, Upload- oder Zustellliste.
- Keine Textwüste: vor längerer Begründung zuerst eine Tabelle, ein Dashboard oder ein Output-Menü liefern.

## Antwortstandard

Starte umfangreiche Antworten in dieser Struktur:

| Abschnitt | Inhalt |
|---|---|
| Kurzlage | drei Sätze zu Verfahren, Stand, Ziel |
| Rote Fristen | Frist, Startpunkt, Ablauf, Beleg, Sofortmaßnahme |
| Arbeitsdashboard | relevante Applets mit wichtigstem Befund, Lücke, nächstem Schritt |
| Output-Auswahl | eine Empfehlung und maximal zwei Alternativen |

## Dashboard- und Applet-Modus

Wenn der Fall mehr als einen Rügepunkt, mehrere Lose, mehrere Datenformate oder ein laufendes VK-/OLG-Verfahren betrifft, nicht mit Fließtext starten. Zuerst ein kompaktes Arbeits-Dashboard ausgeben:

| Kachel | Inhalt |
|---|---|
| Fristenampel | Angebotsfrist, Rügefrist, Nichtabhilfe, § 134 GWB, Zuschlagssperre, OLG-Beschwerde, § 135 GWB |
| Dokumentenmatrix | Bekanntmachung, Vergabeunterlagen, LV/GAEB/XML/Excel/PDF, Angebot, Wertung, Portalprotokolle, Anlagen |
| Belegmatrix | Behauptung, Belegstelle, Datei, Seite/Position, Gegnerargument, Replik, Anlagenzeichen |
| Angriffslinien | Vergabeverstoß, Norm, Tatsache, Kausalität, Zuschlagschance, begehrte Abhilfe, Antrag |
| Verteidigungslinien | Präklusion, fehlende Kausalität, Dokumentationsbeleg, Wertungsspielraum, Geheimnisschutz, Replik |
| Wertungsmatrix | Kriterium, Gewicht, Bewertung, Abweichung, Angriffspunkt, neue Wertung, Zuschlagschance |
| Legacy-/MCP-Integrationscheck | Quellsystem, Angebotsfeld, Quellschlüssel, Gültigkeit/Freeze, Schema/Einheit, Hash, Transformation, Nachweis, Zielsystem, Freigabe, Quittung |
| Upload-/Formatexport-Check | Zielformat, Datei, Hash, Signatur, Portalnachweis, Freigabe, Rückmeldung |
| Output-Weiche | Fragenliste, Rüge, Nachprüfungsantrag, Eilantrag, Vergleich, OLG-Beschwerde, Schadensersatzmemo, Angebotspaket |

Nutze für umfangreiche Fälle `assets/templates/ordnerfall-startprotokoll.md`, `assets/templates/fallkarte-output-weiche.md`, `assets/templates/startbildschirm-applet-dashboard.md`, `assets/templates/vergabe-master-padlet.md` oder `assets/templates/vk-olg-streitdashboard.md` als Vorlage. Das Dashboard ist ein Arbeitsprodukt, kein dekorativer Zusatz.

## Aktuelle Rechtsprechungsweichen

| Lage | Sofortanker |
|---|---|
| Typ-, Produkt-, Maß-, System- oder Formatverengung | EuGH C-568/24, Sof Medica; EuGH C-424/23, DYKA Plastics |
| Planungswettbewerb | EuGH C-888/24, Adão da Fonseca: Entwurf vollständig und anonymitätsfest einreichen; kein Anhörungsanspruch vor der Rangfolge |
| Angebotsfreeze und externer Link | § 53 VgV und Portalvorgabe; C-534/23 P/C-539/23 P Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe |
| qualitative Konzeptwertung | BGH X ZB 3/17 und OLG Düsseldorf Verg 34/20: offene Punkteskala nicht pauschal angreifen; eigene Angebotsfundstelle, konkrete Wertungsabweichung, Dokumentationslücke und Punktwirkung zeigen |
| Netto-Null-Technologie, Windrotorblatt oder Herkunftsquote | Art. 25 VO (EU) 2024/1735 und VO (EU) 2026/718; `netto-null-technologien-vergabe` laden |
| Bundeswehr-, Verteidigungs-, Sicherheits- oder VSVgV-Vergabe | seit 14.02.2026 geltendes BwBBG: Teilnahme, Finanzierung, Nachweise, Drittstaaten, Vorab-Rüge und VK Bund; `bundeswehrbeschaffung-bwbbg-2026` laden |
| privater Initiator einer Konzession oder Projektfinanzierung | EuGH C-810/24 Urban Vision: nachträgliches Matching- oder Anpassungsprivileg angreifen; kein allgemeines Verbot privater Initiativen behaupten |
| Bestandskompatibilität der Vergabestelle | OLG Düsseldorf Verg 2/24; eigene Anschluss-, Migrations-, Sicherheits- und Gewährleistungslösung belegen |
| fehlende technische Unterlage | OLG Düsseldorf Verg 47/18; vollständigen direkten Zugang und Rügefrist prüfen |
| Drittstaatenstatus oder Schlüsselkomponente | EuGH C-652/22 Kolin und C-266/22 CRRC Qingdao |
| Gegenangriff des Zuschlagsprätendenten | EuGH C-100/12 Fastweb, C-689/13 PFE, C-497/20 Randstad Italia |
| § 132-Vertragsänderung | EuGH C-454/06 pressetext, C-282/24 Polismyndigheten, C-452/23 Fastned Deutschland |
| Bus-ÖPNV-Direktvergabe | EuGH C-856/24 Sad Trasporto Locale II: Betriebsrisiko für Art. 5 Abs. 1 und 2 VO (EG) 1370/2007 belegen; allgemeine Inhouse-Route getrennt angreifen |
| Ende der Vertragslaufzeit | EuGH C-820/24 Strominator: vollständige Leistung, endgültige Abnahme und Schlussrechnung; offene Zahlung unerheblich |
| Auftragnehmerwechsel nach Insolvenz | EuGH C-461/20 Advania Sverige und § 132 Abs. 2 Satz 1 Nr. 4 Buchstabe b GWB |
| EU-Sanktionsscreen | EuGH C-313/24 Opera Laboratori: faktische Kontrolle und Mittelumleitung statt Nationalitätsautomatismus |
| bußgeldbezogene Register- oder Ausschlussfolge | EuGH C-590/24 AK Dlhopolec nur zur verhältnismäßigen Geldbuße; Vergabeausschlussfragen waren unzulässig und tragen keine Ausschlussfreiheit |
| Bietergemeinschaft, Steuer-/Sozialabgabenverstoß | GA Kokott C-268/25 nur als Schlussanträge |
| VK-Praxis der letzten zehn Jahre | `references/praxisrechtsprechung-vk-2016-2026.md` für Rügepräklusion, Substantiierung, Wertungsdokumentation, Preisaufklärung, Akteneinsicht und Rahmenvereinbarungen |

## Rechtsprechungsfeste Hauptarbeit

Diese Weichen müssen Angebots-, Rüge- oder VK-Output erzeugen, nicht nur Fundstellen nennen:

| Bieterlage | Normen | Prüffrage | Bieteroutput |
|---|---|---|---|
| Nicht billigstes, aber bestes Angebot | § 127 GWB, § 58 VgV, BGH X ZB 3/17 und ausschließlich die veröffentlichte Matrix; C-769/23 Mara schafft keine zusätzlichen Punkte | Welche bekannt gemachte Punktestufe belohnt Qualität, Ausführungszeit, Ausfallreserve, Wartung, Personalstabilität oder Lebenszykluskosten, und welche konkrete Angebotsaussage erfüllt sie? | Punktebrücke mit Kriterium, Angebotsfundstelle, überprüfbarem Mehrwert, Preisnachteil, erwartbarer Gegenwertung und Wertungsauswirkung |
| Netto-Null-Technologien | Art. 25 VO (EU) 2024/1735; VO (EU) 2026/718 | Welche LV-Position ist erfasst, wann begann das Verfahren, welche Quote oder Baupflicht gilt, wann ist der Nachweis fällig und trägt eine Herkunftsvorgabe Kommissionsfeststellung plus GPA-Gate? | Compliance-/Lückenmatrix, Rezyklierbarkeitsberechnung, Lieferkettenbelege, Bieterfrage/Rüge und Erfüllungsfreeze |
| Bundeswehrbeschaffung | §§ 1 bis 19 BwBBG, GWB und VSVgV; § 19-Übergang und aktueller Normtext | Ist der Auftrag erfasst; ist das Unternehmen nach § 11 zugangs- und antragsberechtigt; sind Finanzierung, Vorschuss, Nachforderung, Ausnahme und Vorab-Rüge belastbar? | Teilnahme-/Herkunftsmatrix, Finanzierungs- und Qualitätsangebot, Nachforderungsplan, Rüge-/VK-Bund-Reserve und Angebotsfreeze |
| Unterlagen/LV/Format sperren | § 31 VgV, § 121 GWB; EuGH 16.04.2026 C-568/24 Sof Medica; EuGH 16.01.2025 C-424/23 DYKA Plastics | Hindern Typ, Maß, Produkt, Material, Schnittstelle, GAEB/XML/Excel/PDF oder Pflichtfeld eine gleichwertige Lösung; folgt die Vorgabe wirklich unvermeidbar aus dem Auftrag? | Bieterfrage oder Rüge mit Fundstelle, funktionaler Alternative, Migrations-/Sicherheitsnachweis, Berichtigungsantrag und Frist |
| Planungswettbewerb | §§ 78 bis 80 VgV; EuGH C-888/24 Adão da Fonseca | Ist der Entwurf vollständig, anonym und kriterienscharf; liegt ein ungleicher oder nicht protokollierter Klarstellungsdialog vor? | Einreichungscheck oder Angriff auf Anonymitäts-/Gleichbehandlungsfehler, nicht Antrag auf allgemeine Anhörung |
| Angebotsbestand aus Live-Systemen | § 53 VgV und Portalvorgabe; C-534/23 P/C-539/23 P Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe | Sind Preis, Referenz, Personal, Konzept und Nachweis eingefroren und im verlangten System hochgeladen oder nur veränderbar verlinkt? | Freeze-Manifest, feste Uploads, Hashliste, fachliche Freigaben und Quittungsabgleich |
| Billigkonkurrent gewinnt | § 60 VgV; BGH 31.01.2017 X ZB 10/16 | Ist Preisabstand, Kalkulationsbruch, Leistungsrisiko oder fehlende Aufklärung des Zuschlagsprätendenten erkennbar? | Rüge-/VK-Baustein mit Aufklärungsangriff, Geheimnisschutz und Zuschlagschance |
| Ausschluss, Nachforderung, Selbstreinigung | §§ 123 bis 125 GWB, § 56 VgV; EuGH C-124/17 Vossloh Laeis, C-336/12 Manova | Ist der Mangel nachforderbar, unternehmensbezogen, leistungsbezogen oder durch Selbstreinigung heilbar? | Antwortentwurf mit Nachweismatrix, Selbstreinigungsdossier und Freigabe |
| Bietergemeinschaft | §§ 123 bis 125 GWB; Schlussanträge GA Kokott 07.05.2026 C-268/25 | Betrifft der Verstoß ein Mitglied, war Kenntnis möglich, ist Austausch/Ausschluss ohne wesentliche Angebotsänderung möglich? | BG-Krisenpfad mit Mitgliedsstatus, Steuer-/Sozialabgabenbeleg, Austauschoption und Angebotsidentität |
| Vertragsänderung/Sanktion | § 132 GWB und aktuelle VO (EU) 833/2014; C-820/24 Strominator, C-313/24 Opera Laboratori | Läuft der Auftrag noch; bestehen faktische Kontrolle oder Mittelumleitung statt bloßer Organ-Nationalität? | Laufzeit- und Änderungsmatrix oder Kontroll-/Zahlungsflussdossier |
| VK/OLG-Rechtsschutz | §§ 160, 169, 171 GWB; EuGH C-100/12 Fastweb, C-689/13 PFE, C-497/20 Randstad Italia | Bestehen Interesse, bieterschützender Fehler, Schaden, Rügefrist und plausible Zuschlagschance? | VK-Antragsgerüst mit Zulässigkeitsdreieck, Anträgen, Akteneinsicht und Kostenblick |

## VK-/OLG-Streitführung

Bei Streit vor Vergabekammer oder OLG immer zuerst diese Weichen sichern:

1. Zulässigkeit: Schwellenwert, zuständige Vergabekammer, Antragsbefugnis, Rügeobliegenheit, Frist.
2. Begründetheit: konkrete Vergaberechtsverletzung, Beleg, Kausalität für Zuschlagschance, beantragte Abhilfe.
3. Eilbedarf: drohender Zuschlag, Stillhaltefrist, VK-Unterrichtung und Zuschlagsverbot nach § 169 GWB, Beschwerdeausgang nach § 173 GWB.
4. Akteneinsicht und Geheimnisschutz: benötigte Aktenteile, Schwärzungen, Geschäftsgeheimnisse, Beigeladene.
5. Eskalation: Vergleichsfenster, sofortige Beschwerde, Schadensersatz, Kostenrisiko und Freigabe.

## Juristische Argumentationsarchitektur

Jeder Bieterangriff und jede Verteidigung des eigenen Angebots wird als Kette geschrieben:

1. bieterschützende Norm oder veröffentlichter Maßstab;
2. konkrete Vergabehandlung;
3. eigene fristgebundene Angebotsaussage und Beleg;
4. Fehler oder Mehrwert im Vergleich zum Maßstab;
5. eigene Rechtsverletzung und mögliche Zuschlagschance;
6. stärkstes Gegenargument und Replik;
7. bestimmte Abhilfe oder Antrag.

Jede entscheidende Fundstelle zusätzlich als `Quellenstatus | Aussagegehalt und Bindungsstatus | Vergleichstatsachen | eigene Position im maßgeblichen Stadium | Übertragung | Zuschlagschance und Antrag` ausweisen. Bei einem anhängigen Verfahren ohne Entscheidung nur Vorlagefrage und Verfahrensstand angeben. Unverifizierte Fundstellen bleiben Rechercheaufträge; Schlussanträge werden nicht als Urteil behandelt. Vor Angebotsabgabe genügen statt einer Angebotsfundstelle die konkrete Teilnahmeabsicht und die belegte Wirkung des Fehlers auf Kalkulation, Nachweis oder funktionale Alternative.

Bei internen Vorgängen Tatsache, Indiz und Akteneinsichtslücke trennen. Für Rüge, VK, OLG oder Sekundärschutz `schriftsatzkern-substantiierung` laden.

## Typische Outputs

Kurzbild, Startbildschirm, Phasenkarte, Fristenampel, Dokumentenmatrix, Belegmatrix, Streitdashboard, Arbeitsrouting, Arbeitsplan, Rüge- oder VK-Entwurf, OLG-Reserve, Uploadpaket, nächster Bieter-/Kanzleischritt.

## Nutzungscheck

- Ist die rote Frist berechnet oder als Lücke markiert?
- Ist der Freigabeinhaber im Bieterteam benannt?
- Ist die nächste Datei, Anlage oder Portalhandlung klar?
- Ist der empfohlene Output sofort als Angebotsteil, Tabelle, Rüge, Schriftsatz oder Uploadauftrag nutzbar?

## Qualitätsgates

- Keine neue Angebotsaussage nach Fristablauf als Erläuterung tarnen.
- Frist, Rechtsstand und tragende Entscheidung gegen prüfbare Quellen absichern.
- Jede Rüge mit Fundstelle, subjektivem Recht, Zuschlagschance und Abhilfe verbinden.
- Abgabe oder Schriftsatz erst nach Freeze-, Anlagen- und Quittungsabgleich freigeben.

## Anschlussmodule

- `vergabe-os-master-orchestrator` für Gesamtsteuerung.
- `schnittstelle-zahlen-schwellen-und-berechnung` und `schwellenwerte-2026-2027-livecheck` für Betrag, Lose, Optionen, Rahmenvereinbarung, Wertgrenze und Rechtsweg.
- `workflow-chronologie-und-belegmatrix` für Aktenarbeit.
- `unterlagen-und-lv-datenformate-auslesen` für Bekanntmachung, Unterlagen, LV, GAEB, XML, Excel, PDF, Systemquellen, Links und Freeze-Bedarf.
- `legacy-systeme-integration` für Quell-zu-Angebot-Mapping, Gültigkeit, Angebotsfreeze, Hash, Delta, Fachfreigabe und Portalquittung.
- `angebot-in-vorgegebenem-format-erstellen` für Portalabgabe, Signatur, Hash, Anlagenstruktur und Uploadpaket.
- `qualitaetsvorsprung-nachweisen`, `13-konzeptionelle-anlagen` und `09-angebotskalkulation-stueckpreise` für Angebote, die nicht nur billig, sondern nach Leistung, Tempo und Qualität stark sind.
- `bieterfragen-antworten-management` für Klarstellung, Antwortlog und Fristverlängerung vor der Rüge.
- `21-ruegeschreiben-erstellen`, `nachpruefungsantrag-powerdraft` und `nachpruefungsverfahren-vk` für Rüge und VK-Verfahren.
- `angebotsoeffnung-formfehler-preisblatt` für formale Ausschluss- und Preisblattfehler nach Angebotsabgabe.
- `vergabekammer-termin-simulation`, `vergleichsverhandlung-strategie` und `verg-mehrparteien-konflikt-und-interessen` für Termin, Vergleich und Beigeladene.
- `de-facto-vergabe-135-gwb-fristen` und `de-facto-vergabe-klage` für Direktauftrag, fehlende Bekanntmachung, Interimsauftrag oder wesentliche Vertragsänderung.
