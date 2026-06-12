# Fachanwalt Arbeitsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-arbeitsrecht`) | [`fachanwalt-arbeitsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-arbeitsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Kündigungsdrama Körber / Steinhoff Präzisionsguss** (`arbeitsrecht-kuendigungsdrama-koerber-werk`) | [Gesamt-PDF lesen](../testakten/arbeitsrecht-kuendigungsdrama-koerber-werk/gesamt-pdf/arbeitsrecht-kuendigungsdrama-koerber-werk_gesamt.pdf) | [`testakte-arbeitsrecht-kuendigungsdrama-koerber-werk.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitsrecht-kuendigungsdrama-koerber-werk.zip) |
| **Klingenhain Musikschule / DRV-Statusprüfung** (`statusfeststellung-drv-musikschule-gf-freelancer-klingenhain`) | [Gesamt-PDF lesen](../testakten/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain/gesamt-pdf/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain_gesamt.pdf) | [`testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

## Anwalts-Dashboard für den Schnelleinstieg

Der Skill `einstieg-routing` ist das Anwalts-Dashboard zu diesem Plugin:
Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch,
Zustaendigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs,
Norm-Radar, Leitentscheidungs-Anker und genau eine Rueckfrage - bei
klarer Faktenlage sofort zum Spezial-Skill. Der Anwalt bleibt im Driver Seat.

Konvention: [`references/anwalts-dashboard-konvention.md`](../references/anwalts-dashboard-konvention.md)
| Quellen-Anker: [`references/leitentscheidungen-anker.md`](../references/leitentscheidungen-anker.md)
| Quellenhygiene: [`references/quellenhygiene.md`](../references/quellenhygiene.md).


Plugin Fachanwalt für Arbeitsrecht nach FAO § 10. Orientierung, Kündigungsschutzklage, Betriebsratsanhörung, Befristung. Schnittstellen zum Plugin `arbeitsrecht` (operative Mandatsführung) und `kanzlei-allgemein`.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-arbeitsrecht-orientierung` | Orientierung — FAO § 10, Normen, Mandate, Fristen, Quellenprüfung. |
| `fachanwalt-arbeitsrecht-kuendigungsschutzklage` | Kündigungsschutzklage § 4 KSchG, Frist drei Wochen ab Zugang. |
| `fachanwalt-arbeitsrecht-betriebsratsanhoerung` | Anhörung des Betriebsrats § 102 BetrVG vor jeder Kündigung. |
| `fachanwalt-arbeitsrecht-befristung-tzbfg` | Befristungsrecht TzBfG, Schriftform, Sachgrund, Vorbeschäftigung. |

### Aktuelle BAG-Rechtsprechung 2025/2026

| Skill | Zweck |
| --- | --- |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 78 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-loeschung-personalakte-bag-2-azr-782-11` | Abmahnung Entfernung aus Personalakte mit Paragraf 242 BGB und Art 17 DSGVO; Verbrauch der Warnfunktion. |
| `aktenzeichen-fehlerkatalog` | Aktenzeichen Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Arbeitsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 4 KSchG 3 Wochen Kündigungsschutzklage, Arbeitsvertrag, Kündigung, Aufhebungsvertrag), dokumentiert Router-Entscheidung mit Begründung. |
| `ar-abfindungs-rechner-modular` | Abfindungsrechner modular: Faustformel 0 und5 Monatsgehälter pro Beschäftigungsjahr nach BAG-Linie, Anpassung nach Verhandlungsmacht, Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG: Abfindungsrechner modular: Faustf... |
| `ar-aufhebungsvertrag-praxis` | Aufhebungsvertrag in der Praxis: Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34 EStG, AGB-Kontrolle von Klauseln §§ 305 ff: Aufhebungsvertrag in der Praxis: Sperrzeit ALG I § 159 SGB III, steuerliche Fünftelregelung § 34... |
| `ar-betriebsuebergang-spezial` | Betriebsübergang § 613a BGB im M&A-Kontext: Asset-Deal vs: Share-Deal, identitätswahrender Übergang (EuGH/BAG-Linie), Unterrichtungsschreiben Mindestinhalt, Widerspruchsrecht 1 Monat, Haftungsfolgen... |
| `ar-einfuehrung-mandantenanliegen` | Arbeitsrecht einführend: typische Mandantenanliegen — Kündigung, Abfindung, Zeugnis, Befristung, Maßregelungsverbot, Diskriminierung AGG, Lohn, Urlaub, BR-Mitbestimmung: Arbeitsrecht einführend: typische Mandantenanliegen — Kündigung, Ab... |
| `ar-konkurrenzklausel-spezial` | Nachvertragliches Wettbewerbsverbot §§ 74–75d HGB analog: Karenzentschädigung ≥ 50 %, Schriftform, Verbindlichkeit, Freistellung durch Arbeitgeber, Verwirkung, Verstoß und Vertragsstrafe: Nachvertragliches Wettbewerbsverbot §§ 74–75d HGB... |
| `ar-kuendigungspruefung-workflow` | Kündigungsprüfung: Schritt-für-Schritt vom Zugang der Kündigung bis zur Klageerhebung oder Vergleichsstrategie: Schriftform § 623 BGB, KSchG-Anwe... |
| `ar-leiharbeit-equal-pay-spezial` | Leiharbeit: Equal-Pay-Anspruch § 8 AÜG, Überlassungshöchstdauer 18 Monate § 1 Abs: 1b AÜG, Verbot verdeckter Arbeitnehmerüberlassung, Arbeitsverhältnis kraft Gesetzes § 10 AÜ... |
| `arbeitsrecht-tatbestand-beweis-und-belege` | Tatbestand, Beweis und Belege im Arbeitsrechtsprozess: Darlegungs- und Beweislastverteilung nach Normen, abgestufte Darlegungslast BAG-Linie, Beweismittel im Arbeitsgerichtsverfahren, DSGVO-konforme Beweiserhebung § 26 BDSG: Tatbestand,... |
| `aufhebungsvertrag-faires-verhandeln-bag-6-azr-333-21` | Aufhebungsvertrag und Gebot fairen Verhandelns nach BAG 6 AZR 333/21. Prüfraster Ueberrumpelung Bedenkzeit Schadensersatz durch Naturalrestitution. |
| `aufhebungsvertrag-sperrzeit` | Aufhebungsvertrag mit Sperrzeit-Vermeidung nach § 159 SGB III bei Eigeninitiative oder drohender Kündigung: Anwendungsfall Arbeitgeber und Arbeitnehm... |
| `bag-equal-pay-paarvergleich` | Fachanwalt Arbeitsrecht Bag Equal Pay Paarvergleich: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Bag Equal Pay Paarvergleich: ordnet Normen, Nutzeran... |
| `bag-freistellungsklausel-unwirksam` | Fachanwalt Arbeitsrecht Bag Freistellungsklausel Unwirksam: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Bag Freistellungsklausel Unwirksam: ordnet No... |
| `bag-mindesturlaub-kein-verzicht` | Fachanwalt Arbeitsrecht Bag Mindesturlaub Kein Verzicht: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Bag Mindesturlaub Kein Verzicht: ordnet Normen,... |
| `befristung-compliance-dokumentation-und-akte` | Befristungscompliance und Aktenführung: TzBfG §§ 14–17, Schriftformzwang vor Dienstantritt, Sachgrundbefristung-Dokumentation, Anschlussverbot § 14 Abs: Befristungscompliance und Aktenführung: TzBfG §§ 14–17, Schriftformzwang vor Diensta... |
| `befristung-tzbfg` | Befristungskontrolle und Befristungsgestaltung nach TzBfG für Arbeitgeber und Arbeitnehmer: Anwendungsfall befristeter Arbeitsvertrag soll geprüft oder neuer Befrist... |
| `bem-verfahren` | Fachanwalt Arbeitsrecht Bem Verfahren: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Bem Verfahren: ordnet Normen, Nutzerangaben, Fristen, Belege und v... |
| `beteiligung-betriebsrat-102-betrvg` | Betriebsratsanhörung vor Kündigung: Sachverhalt, Sozialdaten, Kündigungsgrund, Nachschieben und Fehlerfolgen: Normanker: BetrVG § 102; KSchG; BAG... |
| `betriebsrat-zahlen-schwellen-und-berechnung` | Betriebsrat: Schwellenwerte für Größe, Zusammensetzung und Freistellungen §§ 9 und 38 BetrVG, Wahlrecht § 7 BetrVG, Betriebsbegriff, geteilte und gemeinsame Betriebe, Gesamtbetriebsrat, Konzernbetriebsrat, Betriebsratswahl-Kalender: Betr... |
| `betriebsratsanhoerung` | Betriebsratsanhoerung nach § 102 BetrVG vor jeder Kündigung: Anwendungsfall Kündigung soll ausgesprochen werden und BR-Anhörung muss korrekt durchgeführt werden. Normen § 102 BetrVG Anhörungs- und... |
| `betriebsratsbeschluss-heilung` | Fachanwalt Arbeitsrecht Betriebsratsbeschluss Heilung: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Betriebsratsbeschluss Heilung: ordnet Normen, Nutz... |
| `betriebsratswahl-anfechtung-leiharbeit-bag-7-abr-4-21` | Betriebsratswahl Anfechtung bei Wahlfehler Leiharbeiter mit BAG 7 ABR 4/21. |
| `betriebsuebergang-widerspruch-paragraf-613a-bgb-spaetlauf` | Betriebsuebergang Widerspruchsrecht bei mangelhafter Unterrichtung mit Paragraf 613a VI BGB und BAG 8 AZR 336/19. |
| `betrvg-behoerden-gericht-und-registerweg` | BetrVG: Behörden, Gerichte und Registerwege — Beschlussverfahren §§ 80 ff: ArbGG, Einigungsstelle §§ 76 BetrVG, Wahlanfechtung § 19 BetrVG, Zustimmungsersetzung § 99 Abs. 4 BetrVG, B... |
| `datum-formular-portal-und-einreichung` | Datum, Formular, Portal und Einreichung im arbeitsrechtlichen Verfahren: Fristenkalender, elektronische Einreichung ERV/beA, Gerichtsportale Arbeitsgericht, Formulare Klage ArbG, Antragsformulare ELAN-K2, Massenentlassung-Anzeige, BA-For... |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Arbeitsrecht: sortiert Arbeitsvertrag, Kündigung, Aufhebungsvertrag, prüft Datum, Absender, Frist und Beweiswert (Zugangs-Nachweis Kündigung, Lohnzettel); markiert Lücken; berücksichtigt Mandatsgeheimnis §... |
| `einstieg-routing` | Anwalts-Dashboard Fachanwalt Arbeitsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt... |
| `einstieg-schnelltriage-fallrouting` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Arbeitsrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diese... |
| `entgeltgleichheit-paarvergleich-agg-entgtranspg` | Setzt BAG 23.10.2025 - 8 AZR 300/24 in einen arbeitsrechtlichen Prüffür Equal Pay, variable Vergütung, Vergleichsperson, § 22 AGG, EntgTranspG und Dokumentationsstrategie um: Setzt BAG 23.10.2025 - 8 AZR 300/24 in einen arbeitsrechtliche... |
| `entgtranspg-verhandlung-vergleich-und-eskalation` | EntgTranspG Entgelttransparenzgesetz: Auskunftsanspruch § 10, Verfahren, Fristen, Verhandlungsstrategie bei Lohnlücke, Eskalation zu AGG-Klage §§ 15 und 22 AGG, Paarvergleich BAG 8 AZR 300/24, EU-Lohntransparenz-RL 2023/970: EntgTranspG... |
| `equal-pay-leiharbeit-bag-5-azr-143-19-eugh-timepartner` | Equal Pay Leiharbeit Tarifabweichung mit BAG 5 AZR 143/19 und EuGH TimePartner. |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturier... |
| `erstpruefung-und-mandatsziel` | Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielformulierung, Interessenkonflikt-Check, Mandatsumfang, Kostenhinweis RVG, erste Risikoampel: Fachanwalt Erstprüfung und M... |
| `fao-fristen-form-und-zustaendigkeit` | Fachanwalt für Arbeitsrecht (FAO § 10): Verfahrensrecht ArbGG, Zuständigkeit §§ 2 und 2a ArbGG, Urteilsverfahren vs: Beschlussverfahren, Ins... |
| `fazugang-neu-001-kuendigung-durch-boten-beweisvermerk-und-prozes` | Zugang der Kündigung durch Boten: Beweisvermerk-Erstellung, Zeugenbenennung, Prozessstrategie bei bestritenem Zugang: Beweislast des Arbeit... |
| `fazugang-neu-002-einwurf-einschreiben-risiko-nach-aktueller-bag` | Einschreiben-Zustellung bei Kündigung: Risiken des Einwurf-Einschreibens (kein Zugang bei Nichtabholung), Übergabe-Einschreiben vs: Einschreiben-Zustellung bei Kündigung: Risiken des Einwurf-Einschreibens (kein Zugang bei Nichtabholung),... |
| `fazugang-neu-003-zugang-bei-urlaub-krankheit-klinik-und-auslands` | Zugang bei Abwesenheit: Urlaub, Krankheit, Klinikaufenthalt, Auslandsaufenthalt — BAG-Linie zur Kenntnisnahmemöglichkeit, Zugangszeitpunkt, Sorgfaltspflicht des Empfängers, Empfangsbevollmächtigung, taktische Beratung: Zugang bei Abwesen... |
| `fazugang-neu-004-inhalt-des-umschlags-bestreiten-und-beweisangeb` | Bestreiten des Inhalts eines zugestellten Umschlags: zulässige Einwände, Beweislast des Arbeitgebers für Schriftform und Inhalt, Gegenbeweis-Möglichkeiten, Prozessstrategie, Abgrenzung zu unzulässiger Schutzbehauptung: Bestreiten des Inh... |
| `fazugang-neu-005-kuendigungsfrist-berechnen-bei-unsicherem-zugan` | Kündigungsfrist berechnen bei unsicherem Zugangsdatum: frühest- und spätestmöglicher Zugang, Fristberechnung §§ 187 ff: BGB, Drei-Wochen-... |
| `fazugang-neu-006-arbeitgeber-zustellworkflow-rechtssicher-organi` | Arbeitgeber-Zustellworkflow: rechtssichere Organisation der Kündigungszustellung, Parallelwege (Bote + Einschreiben + Gerichtsvollzieher), Checklisten, Kuvertierungsprotokoll, Risikomanagement bei mehreren Empfängern (Massenentlassung):... |
| `fazugang-neu-007-arbeitnehmerverteidigung-zugang-bestreiten-ohne` | Arbeitnehmerverteidigung: Zugang bestreiten ohne unwahre Behauptungen — zulässige Einwände, Beweislastverteilung, § 138 ZPO-Wahrheitspflicht, Strategie für Fristverteidigung, nachträgliche Zulassung § 5 KSchG: Arbeitnehmerverteidigung: Z... |
| `fazugang-neu-008-schriftform-kuendigung-original-und-elektronisc` | Schriftform Kündigung § 623 BGB: Originalunterschrift zwingend, Faksimile unzulässig, elektronische Kommunikation (E-Mail, WhatsApp, Fax, Teams) genügt nicht: Schriftform Kündigung § 623 BGB: Originalunterschrift zwingend, Faksimile unzu... |
| `freistellungsklausel-sonderfall-edge-case` | Freistellungsklausel im Arbeitsvertrag: BAG 5 AZR 108/25 (pauschale Klausel unwirksam), anlassbezogene Formulierung, Vergütungsfortzahlung, Urlaubsverfall während Freistellung, Verrechnung mit Urlaubsabgeltung, Edge Cases: Freistellungsk... |
| `hinschg-whistleblower-repressalie` | Verteidigung von Hinweisgebern nach HinSchG gegen Repressalien durch Arbeitgeber: Anwendungsfall Arbeitnehmer hat intern oder extern Hinweis gegeben und wurde daraufhin gekünd... |
| `homeoffice-kontrollrecht-paragraf-106-gewo-lag-rheinland-pfalz` | Homeoffice Kontrollrecht Arbeitgeber Paragraf 106 GewO und Art 8 EMRK. |
| `kschg-risikoampel-und-gegenargumente` | KSchG Risikoampel: systematische Bewertung der Kündigung nach betriebsbedingten, personenbedingten und verhaltensbedingten Gründen, Sozialauswahl, BR-Anhörung, Massenentlassung — Grün/Gelb/Rot mit Gegenargumenten und nächstem Handgriff:... |
| `kuendigung-per-einschreiben-risiken` | Einschreiben, Post und Zugang: warum Einwurf-/Übergabe-Einschreiben oft nicht genügt und wie man Beweis sauber führt: Normanker: BGB § 13... |
| `kuendigungsschutzklage` | Kündigungsschutzklage nach § 4 KSchG mit Drei-Wochen-Frist ab Zugang der schriftlichen Kündigung: Anwendungsfall Arbeitnehmer erhaelt Kündigung und will Klage... |
| `low-performer-kuendigung-bag-2-azr-359-02` | Verhaltensbedingte Kuendigung Low Performer mit BAG 2 AZR 359/02; Vergleichsmassstab Kollegen. |
| `massenentlassung-17-kschg` | Fachanwalt Arbeitsrecht Massenentlassung 17 KSchG: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Massenentlassung 17 KSchG: ordnet Normen, Nutzerangabe... |
| `massenentlassung-17-kschg-realitaetscheck` | Massenentlassung: Anzeige, Konsultation, Agentur für Arbeit, Fehlerfolgen, neue Rechtsprechung und Rettungsstrategie: Normanker: KSchG §... |
| `massenentlassung-anzeige-eugh-junk-bag-6-azr-155-21` | Massenentlassung Anzeigeverfahren Paragraf 17 KSchG mit EuGH Junk und BAG 6 AZR 155/21 als Prüfraster Anzeigezeitpunkt. |
| `orientierung-mandat-fachanwaltschaft` | Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO: Anwendungsfall Kanzlei wi... |
| `output-waehlen` | Output-Wahl für Fachanwalt Arbeitsrecht: stimmt Adressat (Arbeitnehmer, Arbeitgeber, Betriebsrat), Frist (§ 4 KSchG 3 Wochen Kündigungsschutzklage) und Form auf den Zweck ab — typische Outputs: Kündigungsschutzklage, Aufhebungsvertrag-Ma... |
| `paragraf-dokumentenmatrix-und-lueckenliste` | Paragraf-Dokumentenmatrix und Lückenliste: für jeden Streitgegenstand die einschlägigen Normen, erforderlichen Dokumente und fehlenden Belege tabellarisch aufbereiten — Kündigung, Befristung, Abfindung, Vergütung, Betriebsrat, AGG: Parag... |
| `quelle-beweislast-und-darlegungslast` | Quellenregel, Beweislast und Darlegungslast im Arbeitsrecht: abgestufte Darlegungslast BAG-Linie, Normenübersicht zu Beweislastverteilungen, Umkehr nach AGG § 22, zulässige und unzulässige Fundstellen, Quellenprotokoll für Schriftsätze:... |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Arbeitsrecht: prüft Normen (BGB §§ 611a ff., 623, KSchG §§ 1/4/7, AGG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Arbeitsgericht (1. Instanz) und Quellenhygiene nach referenc... |
| `rechtsprechung-internationaler-bezug-und-schnittstellen` | Internationaler Bezug im Arbeitsrecht: EuGH-Rechtsprechung (Massenentlassung, Befristung, Diskriminierung, Urlaub), EU-Richtlinien (RL 2023/970, RL 2001/23, RL 2008/94, RL 2003/88), Entsendung AEntG, internationales Privatrecht Rom I: In... |
| `rechtsprechung-livecheck-arbeitsrecht` | Live-Check für arbeitsrechtliche Rechtsprechung: Prüfprotokoll für BAG-, LAG- und EuGH-Zitate, Verifizierungswege über bundesarbeitsgericht.de, openjur.de, dejure.org, curia.europa.eu, Umgang mit nicht verifizierbaren Quellen: Live-Check... |
| `scheinselbststaendigkeit-statusfeststellung-bsg-b-12-r-11-18` | Scheinselbststaendigkeit Statusfeststellung nach Paragraf 7a SGB IV und BSG B 12 R 11/18 R. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Kündigungsschutzklage, Befristungskontrollklage, Zahlungsklage Arbeitsgericht: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau: Substantiie... |
| `tzbfg-schriftsatz-brief-und-memo-bausteine` | TzBfG Schriftsatz-, Brief- und Memo-Bausteine: Klageschrift Entfristungsklage § 17 TzBfG, Klageantrag, Sachverhaltsaufbau, Beweisangebote, Mandantenbrief zur Befristungsbeendigung, Arbeitgeberantwortbrief, Vergleichsformel: TzBfG Schrift... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Arbeitsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Arbeitsvertrag, Kündigung, Aufhebungsvertrag), nennt pro Lücke Beweisthema, Beschaffungsweg (Arbeitsgericht (1. Instanz)), Frist... |
| `unwirksam-fristennotiz-und-naechster-schritt` | Unwirksamkeit erkannt — Fristennotiz und nächster Schritt: sofortige Handlungsanleitung nach erkanntem Unwirksamkeitsgrund (Schriftform, BR-Anhörung, Sonderkündigungsschutz, Massenentlassung, Befristungsfehler) — Fristberechnung, Klagewe... |
| `urlaub-quellenkarte` | Urlaub Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `urlaubsabgeltung-verjaehrung-eugh-c-518-20` | Urlaubsabgeltung Verjaehrung Mitwirkungsobliegenheit nach EuGH C-518/20 und BAG 9 AZR 266/20. |
| `vergleich-arbeitsgericht-abrechnung` | Arbeitsgerichtlicher Vergleich: Beendigungsdatum, Zeugnis, Turboklausel, Urlaubsabgeltung, Sprinter, Sperrzeit und Abrechnung: N... |
| `vergleichspraxis-mehrparteien-konflikt-und-interessen` | Vergleichspraxis bei Mehrparteienkonstellationen und komplexen Interessenlagen: Dreiparteienvergleich (AG, AN, BR), Sozialplanverhandlung, Interessenausgleich § 111 BetrVG, Vergleich mit Namensliste § 1 Abs: Vergleichspraxis bei Mehrpart... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Individual- und kollektives Arbeitsrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich): Vergleichsverha... |
| `verhandlung-guete-abfindung-arbg` | Gueteverhandlung im Arbeitsgerichtsverfahren nach § 54 ArbGG mit Auflösungsantrag und Abfindungsstrategie: Anwendungsfall Guetetermin steht an und Ver... |
| `verifizierter-mandantenentscheidung` | Verifizierte Mandantenentscheidung: strukturierter Entscheidungsprozess für Mandanten vor rechtlich verbindlichen Schritten — Klage, Aufhebungsvertrag, Vergleich, Widerspruch: Verifizierte Mandantenentscheidung: strukturierter Entscheidu... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix für arbeitsrechtliche Mandate: zeitliche Sachverhaltsaufbereitung, Ereignis-Zeitachse, Dokumentenzuordnung nach Datum, Lückenidentifikation, Erstellung einer strukturierten Fallchronologie als Arbeitsgrundlage... |
| `workflow-fristen-und-risikoampel` | Fristen und Risikoampel: vollständige Fristenübersicht für arbeitsrechtliche Mandate, Ampelbewertung nach Dringlichkeit, Fristenkalender, Wiedervorlagensystem, kritische Fristen Kündigung KSchG, Befristung TzBfG, AGG, Berufung ArbGG: Fri... |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Arbeitsrechtsmandat: Mandantenbriefe, E-Mails, Gesprächsvorbereitung, Informationspflichten, Kostenhinweis RVG, Akteneinsicht, Verfahrensstandsmeldungen, Aufklärungsbrief vor Klageerhebung: Mandantenkommunikatio... |
| `workflow-redteam-qualitygate` | Red-Team Qualitätsgate: abschließende Qualitätskontrolle vor Ausgabe eines Schriftsatzes, Memos, Mandantenbriefs oder Vergleichs — Quellenverifikation, Gegenargument-Check, Fristencheck, Scheingenauigkeit-Scan, Mandatsziel-Abgleich: Red-... |
| `zugang-kuendigung-bote-beweis` | Zugang der Kündigung: Bote, Einwurf, Umschlaginhalt, Zugangstag, Beweis im Kündigungsschutzprozess: Normanker: KSchG § 4; BGB §§ 130 und 623; ZPO Beweis; B... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`fachanwalt-arbeitsrecht.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/fachanwalt-arbeitsrecht.md) (91 KB)
- Im Repo: [`testakten/megaprompts/fachanwalt-arbeitsrecht.md`](../testakten/megaprompts/fachanwalt-arbeitsrecht.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

### Formatvorlagen (Markdown + ODT)

Sofort verwendbare Vorlagen (Times Roman 11pt, A4, mit Disclaimer und Feldern in [Klammern]). Markdown zum Lesen / Anpassen, ODT zum Bearbeiten in LibreOffice/Word.

| Vorlage | Markdown | ODT |
| --- | --- | --- |
| Aufhebungsvertrag Arbeitsverhaeltnis | [`.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-arbeitsrecht/aufhebungsvertrag-arbeitsverhaeltnis.md) | [`.odt`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-arbeitsrecht/aufhebungsvertrag-arbeitsverhaeltnis.odt) |
| Kuendigungsschutzklage Paragraf 4 Kschg | [`.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-arbeitsrecht/kuendigungsschutzklage-paragraf-4-kschg.md) | [`.odt`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-arbeitsrecht/kuendigungsschutzklage-paragraf-4-kschg.odt) |

*Experimentelle KI-Vorlagen — keine Haftung. Vor Verwendung im Mandat anwaltlich prüfen und an konkreten Fall anpassen.*

<!-- END megaprompt-und-vorlagen (autogen) -->
