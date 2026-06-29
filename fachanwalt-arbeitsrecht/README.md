# Fachanwalt Arbeitsrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Fachanwalt-Arbeitsrecht nach FAO Paragraf 10: KSchG, BetrVG, TzBfG, AGG, EntgTranspG, Urlaub, Betriebsrat, Befristung und Vergleichspraxis. Rechtsprechung nur mit Datum, Aktenzeichen und verifizierter Quelle.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`fachanwalt-arbeitsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-arbeitsrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-arbeitsrecht-werkstatt.md" download><code>fachanwalt-arbeitsrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-arbeitsrecht-schnellstart.md" download><code>fachanwalt-arbeitsrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-arbeitsrecht-kuendigungsdrama-koerber-werk.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitsrecht-kuendigungsdrama-koerber-werk.zip) (Kündigungsdrama Körber / Steinhoff Präzisionsguss); [`testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain.zip) (Klingenhain Musikschule / DRV-Statusprüfung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine Kuendigung rechtssicher angreifen oder aussprechen und die Klagefrist sichern.
## Anwalts-Dashboard für den Schnelleinstieg

Der Skill `einstieg-routing` ist das Anwalts-Dashboard zu diesem Plugin:
Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch,
Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs,
Norm-Radar, Leitentscheidungs-Anker und genau eine Rueckfrage - bei
klarer Faktenlage sofort zum Spezial-Skill. Der Anwalt bleibt im Driver Seat.

Konvention: [`references/anwalts-dashboard-konvention.md`](../references/anwalts-dashboard-konvention.md)
| Quellen-Anker: [`references/leitentscheidungen-anker.md`](../references/leitentscheidungen-anker.md)
| Quellenhygiene: [`Install from .zip`](../references/quellenhygiene.md).


Plugin Fachanwalt für Arbeitsrecht nach FAO § 10. Orientierung, Kündigungsschutzklage, Betriebsratsanhörung, Befristung. Schnittstellen zum Plugin `arbeitsrecht` (operative Mandatsführung) und `kanzlei-allgemein`.

## Befristung: Schriftform, qES und Entfristungsrisiko

Bei jeder Befristungsabrede ist § 14 Abs. 4 TzBfG als harter Form-Stop vor alle Sachgrund- und Vorbeschäftigungsfragen zu ziehen. Zulässig sind nur Papieroriginale mit eigenhändiger Unterschrift beider Vertragsparteien oder die elektronische Form mit echter qualifizierter elektronischer Signatur beider Parteien nach § 126a BGB. Eine E-Mail, ein Scan, ein Unterschriftsbild, eine einfache elektronische Signatur, eine fortgeschrittene Signatur ohne qualifiziertes Zertifikat oder ein Standard-Signaturportal ohne qES-Stufe wahrt die Form nicht.

Fehlt die Form, gilt der Arbeitsvertrag nach § 16 Satz 1 TzBfG als unbefristet. Für Arbeitnehmer läuft die Befristungskontrollklage nach § 17 TzBfG drei Wochen ab dem vereinbarten Befristungsende. Arbeitsvertragsmuster und Mandantenmemos müssen diese Rechtsfolge ausdrücklich nennen und die Signaturdokumentation als Belegposition abfragen.

Rechtsprechungsanker: ArbG Berlin, Urteil vom 28.09.2021 - 36 Ca 15296/20; LAG Berlin-Brandenburg, Urteil vom 16.03.2022 - 23 Sa 1133/21; ArbG Gera, Urteil vom 07.03.2024 - 2 Ca 936/23.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
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

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 120 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-loeschung-personalakte-bag-2-azr-782-11` | Abmahnung Entfernung aus Personalakte mit Paragraf 242 BGB und Art 17 DSGVO; Verbrauch der Warnfunktion. |
| `aktenzeichen-fehlerkatalog` | Aktenzeichen Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Arbeitsrecht: wählt den nächsten Spezial-Skill nach Engpass (Paragraf 4 KSchG 3 Wochen Kündigungsschutzklage, Arbeitsvertrag, Kündigung, Aufhebungsvertrag), dokumentiert Router-Entscheidung mit Begründung. |
| `ar-abfindungs-rechner-modular` | Abfindungsrechner modular: Faustformel 0 und5 Monatsgehälter pro Beschäftigungsjahr nach BAG-Linie, Anpassung nach Verhandlungsmacht, Sperrzeit ALG I Paragraf 159 SGB III, steuerliche Fünftelregelung Paragraf 34 EStG: Abfindungsrechner m... |
| `ar-aufhebungsvertrag-praxis` | Aufhebungsvertrag in der Praxis: Sperrzeit ALG I Paragraf 159 SGB III, steuerliche Fünftelregelung Paragraf 34 EStG, AGB-Kontrolle von Klauseln Paragrafen 305 ff: Aufhebungsvertrag in der Praxis: Sperrzeit ALG I Paragraf 159 SGB III, ste... |
| `ar-betriebsuebergang-spezial` | Betriebsübergang Paragraf 613a BGB im M&A-Kontext: Asset-Deal vs: Share-Deal, identitätswahrender Übergang (EuGH/BAG-Linie), Unterrichtungsschreiben Mindestinhalt, Widerspruchsrecht 1 Monat, Haftungsfolgen... |
| `ar-einfuehrung-mandantenanliegen` | Arbeitsrecht einführend: typische Mandantenanliegen — Kündigung, Abfindung, Zeugnis, Befristung, Maßregelungsverbot, Diskriminierung AGG, Lohn, Urlaub, BR-Mitbestimmung: Arbeitsrecht einführend: typische Mandantenanliegen — Kündigung, Ab... |
| `ar-konkurrenzklausel-spezial` | Nachvertragliches Wettbewerbsverbot Paragrafen 74–75d HGB analog: Karenzentschädigung ≥ 50 %, Schriftform, Verbindlichkeit, Freistellung durch Arbeitgeber, Verwirkung, Verstoß und Vertragsstrafe: Nachvertragliches Wettbewerbsverbot Parag... |
| `ar-kuendigungspruefung-workflow` | Kündigungsprüfung: Schritt-für-Schritt vom Zugang der Kündigung bis zur Klageerhebung oder Vergleichsstrategie: Schriftform Paragraf 623 BGB, KSchG-Anwe... |
| `ar-leiharbeit-equal-pay-spezial` | Leiharbeit: Equal-Pay-Anspruch Paragraf 8 AÜG, Überlassungshöchstdauer 18 Monate Paragraf 1 Absatz 1b AÜG, Verbot verdeckter Arbeitnehmerüberlassung, Arbeitsverhältnis kraft Gesetzes Paragraf 10 AÜ... |
| `arbeitsrecht-tatbestand-beweis-und-belege` | Tatbestand, Beweis und Belege im Arbeitsrechtsprozess: Darlegungs- und Beweislastverteilung nach Normen, abgestufte Darlegungslast BAG-Linie, Beweismittel im Arbeitsgerichtsverfahren, DSGVO-konforme Beweiserhebung Paragraf 26 BDSG: Tatbe... |
| `aufhebungsvertrag-faires-verhandeln-bag-6-azr-333-21` | Aufhebungsvertrag und Gebot fairen Verhandelns nach BAG 6 AZR 333/21. Prüfraster Ueberrumpelung Bedenkzeit Schadensersatz durch Naturalrestitution. |
| `aufhebungsvertrag-sperrzeit` | Aufhebungsvertrag mit Sperrzeit-Vermeidung nach Paragraf 159 SGB III bei Eigeninitiative oder drohender Kündigung: Anwendungsfall Arbeitgeber und Arbeitnehm... |
| `bag-equal-pay-paarvergleich` | Fachanwalt Arbeitsrecht Bag Equal Pay Paarvergleich: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Bag Equal Pay Paarvergleich: ordnet Normen, Nutzeran... |
| `bag-freistellungsklausel-unwirksam` | Fachanwalt Arbeitsrecht Bag Freistellungsklausel Unwirksam: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Bag Freistellungsklausel Unwirksam: ordnet No... |
| `bag-mindesturlaub-kein-verzicht` | Fachanwalt Arbeitsrecht Bag Mindesturlaub Kein Verzicht: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Bag Mindesturlaub Kein Verzicht: ordnet Normen,... |
| `befristung-compliance-dokumentation-und-akte` | Befristungscompliance und Aktenführung: TzBfG Paragrafen 14–17, Schriftformzwang vor Dienstantritt, Sachgrundbefristung-Dokumentation, Anschlussverbot Paragraf 14 Absatz Befristungscompliance und Aktenführung: TzBfG Paragrafen 14–17, Sch... |
| `befristung-tzbfg` | Befristungskontrolle und Befristungsgestaltung nach TzBfG für Arbeitgeber und Arbeitnehmer: Anwendungsfall befristeter Arbeitsvertrag soll geprüft oder neuer Befrist... |
| `bem-verfahren` | Fachanwalt Arbeitsrecht Bem Verfahren: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Bem Verfahren: ordnet Normen, Nutzerangaben, Fristen, Belege und v... |
| `beteiligung-betriebsrat-102-betrvg` | Betriebsratsanhörung vor Kündigung: Sachverhalt, Sozialdaten, Kündigungsgrund, Nachschieben und Fehlerfolgen: Normanker: BetrVG Paragraf 102; KSchG; BAG... |
| `betriebsrat-zahlen-schwellen-und-berechnung` | Betriebsrat: Schwellenwerte für Größe, Zusammensetzung und Freistellungen Paragrafen 9 und 38 BetrVG, Wahlrecht Paragraf 7 BetrVG, Betriebsbegriff, geteilte und gemeinsame Betriebe, Gesamtbetriebsrat, Konzernbetriebsrat, Betriebsratswahl... |
| `betriebsratsanhoerung` | Betriebsratsanhoerung nach Paragraf 102 BetrVG vor jeder Kündigung: Anwendungsfall Kündigung soll ausgesprochen werden und BR-Anhörung muss korrekt durchgeführt werden. Normen Paragraf 102 BetrVG Anhörungs- und... |
| `betriebsratsbeschluss-heilung` | Fachanwalt Arbeitsrecht Betriebsratsbeschluss Heilung: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Betriebsratsbeschluss Heilung: ordnet Normen, Nutz... |
| `betriebsratswahl-anfechtung-leiharbeit-bag-7-abr-4-21` | Betriebsratswahl Anfechtung bei Wahlfehler Leiharbeiter mit BAG 7 ABR 4/21. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `betriebsuebergang-widerspruch-paragraf-613a-bgb-spaetlauf` | Betriebsuebergang Widerspruchsrecht bei mangelhafter Unterrichtung mit Paragraf 613a VI BGB und BAG 8 AZR 336/19. |
| `betrvg-behoerden-gericht-und-registerweg` | BetrVG: Behörden, Gerichte und Registerwege — Beschlussverfahren Paragrafen 80 ff: ArbGG, Einigungsstelle Paragrafen 76 BetrVG, Wahlanfechtung Paragraf 19 BetrVG, Zustimmungsersetzung Paragraf 99 Abs. 4 BetrVG, B... |
| `datum-formular-portal-und-einreichung` | Datum, Formular, Portal und Einreichung im arbeitsrechtlichen Verfahren: Fristenkalender, elektronische Einreichung ERV/beA, Gerichtsportale Arbeitsgericht, Formulare Klage ArbG, Antragsformulare ELAN-K2, Massenentlassung-Anzeige, BA-For... |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Arbeitsrecht: sortiert Arbeitsvertrag, Kündigung, Aufhebungsvertrag, prüft Datum, Absender, Frist und Beweiswert (Zugangs-Nachweis Kündigung, Lohnzettel); markiert Lücken; berücksichtigt Mandatsgeheimnis P... |
| `einstieg-routing` | Anwalts-Dashboard Fachanwalt Arbeitsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt... |
| `einstieg-schnelltriage-fallrouting` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Arbeitsrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diese... |
| `entgeltgleichheit-paarvergleich-agg-entgtranspg` | Setzt BAG 23.10.2025 - 8 AZR 300/24 in einen arbeitsrechtlichen Prüffür Equal Pay, variable Vergütung, Vergleichsperson, Paragraf 22 AGG, EntgTranspG und Dokumentationsstrategie um: Setzt BAG 23.10.2025 - 8 AZR 300/24 in einen arbeitsrec... |
| `entgtranspg-verhandlung-vergleich-und-eskalation` | EntgTranspG Entgelttransparenzgesetz: Auskunftsanspruch Paragraf 10, Verfahren, Fristen, Verhandlungsstrategie bei Lohnlücke, Eskalation zu AGG-Klage Paragrafen 15 und 22 AGG, Paarvergleich BAG 8 AZR 300/24, EU-Lohntransparenz-RL 2023/97... |
| `equal-pay-leiharbeit-bag-5-azr-143-19-eugh-timepartner` | Equal Pay Leiharbeit Tarifabweichung mit BAG 5 AZR 143/19 und EuGH TimePartner. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturier... |
| `erstpruefung-und-mandatsziel` | Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielformulierung, Interessenkonflikt-Check, Mandatsumfang, Kostenhinweis RVG, erste Risikoampel: Fachanwalt Erstprüfung und M... |
| `fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit` | Aufhebungsvertrag mit Sperrzeit-Vermeidung nach Paragraf 159 SGB III bei Eigeninitiative oder drohender Kündigung. Anwendungsfall Arbeitgeber und Arbeitnehmer wollen Arbeitsverhältnis auflösen ohne Sperrzeit für Arbeitslosengeld. Normen... |
| `fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich` | Workflow-Skill zu fachanwalt arbeitsrecht bag equal pay paarvergleich. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam` | Workflow-Skill zu fachanwalt arbeitsrecht bag freistellungsklausel unwirksam. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht` | Workflow-Skill zu fachanwalt arbeitsrecht bag mindesturlaub kein verzicht. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-arbeitsrecht-befristung-tzbfg` | Befristungskontrolle und Befristungsgestaltung nach TzBfG für Arbeitgeber und Arbeitnehmer. Anwendungsfall befristeter Arbeitsvertrag soll geprüft oder neuer Befristungsvertrag gestaltet werden. Normen Paragraf 14 TzBfG Sachgrundbefristu... |
| `fachanwalt-arbeitsrecht-bem-verfahren` | Workflow-Skill zu fachanwalt arbeitsrecht bem verfahren. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-arbeitsrecht-betriebsratsanhoerung` | Betriebsratsanhoerung nach Paragraf 102 BetrVG vor jeder Kündigung. Anwendungsfall Kündigung soll ausgesprochen werden und BR-Anhoerung muss korrekt durchgeführt werden. Normen Paragraf 102 BetrVG Anhoerungs- und Widerspruchsrecht Paragr... |
| `fachanwalt-arbeitsrecht-betriebsratsbeschluss-heilung` | Workflow-Skill zu fachanwalt arbeitsrecht betriebsratsbeschluss heilung. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-arbeitsrecht-hinschg-whistleblower-repressalie` | Verteidigung von Hinweisgebern nach HinSchG gegen Repressalien durch Arbeitgeber. Anwendungsfall Arbeitnehmer hat intern oder extern Hinweis gegeben und wurde daraufhin gekündigt versetzt oder gemobbt. Normen Paragrafen 35-37 HinSchG Ver... |
| `fachanwalt-arbeitsrecht-kuendigungsschutzklage` | Kündigungsschutzklage nach Paragraf 4 KSchG mit Drei-Wochen-Frist ab Zugang der schriftlichen Kündigung. Anwendungsfall Arbeitnehmer erhaelt Kündigung und will Klage erheben oder Arbeitgeber prüft Kündigungsrisiko. Normen Paragraf 4 KSch... |
| `fachanwalt-arbeitsrecht-massenentlassung-17-kschg` | Workflow-Skill zu fachanwalt arbeitsrecht massenentlassung 17 kschg. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-arbeitsrecht-orientierung` | Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach Paragraf 10 FAO. Anwendungsfall Kanzlei will Arbeitsrechtsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung vor. N... |
| `fachanwalt-arbeitsrecht-verhandlung-guete-abfindung-arbg` | Gueteverhandlung im Arbeitsgerichtsverfahren nach Paragraf 54 ArbGG mit Auflösungsantrag und Abfindungsstrategie. Anwendungsfall Guetetermin steht an und Vergleich oder Auflösungsantrag soll vorbereitet werden. Normen Paragraf 54 ArbGG G... |
| `fao-fristen-form-und-zustaendigkeit` | Fachanwalt für Arbeitsrecht (FAO Paragraf 10): Verfahrensrecht ArbGG, Zuständigkeit Paragrafen 2 und 2a ArbGG, Urteilsverfahren vs: Beschlussverfahren, Ins... |
| `fazugang-neu-001-kuendigung-durch-boten-beweisvermerk` | Fachanwalt Arbeitsrecht: Kündigung durch Boten Beweisvermerk und Prozessstrategie mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis. |
| `fazugang-neu-001-kuendigung-durch-boten-beweisvermerk-und-prozes` | Zugang der Kündigung durch Boten: Beweisvermerk-Erstellung, Zeugenbenennung, Prozessstrategie bei bestritenem Zugang: Beweislast des Arbeit... |
| `fazugang-neu-002-einwurf-einschreiben-risiko-aktueller-bag-linie` | Fachanwalt Arbeitsrecht: Einwurf-Einschreiben Risiko nach aktueller BAG-Linie mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis. |
| `fazugang-neu-002-einwurf-einschreiben-risiko-nach-aktueller-bag` | Einschreiben-Zustellung bei Kündigung: Risiken des Einwurf-Einschreibens (kein Zugang bei Nichtabholung), Übergabe-Einschreiben vs: Einschreiben-Zustellung bei Kündigung: Risiken des Einwurf-Einschreibens (kein Zugang bei Nichtabholung),... |
| `fazugang-neu-003-zugang-bei-urlaub-krankheit-klinik-und-auslands` | Zugang bei Abwesenheit: Urlaub, Krankheit, Klinikaufenthalt, Auslandsaufenthalt — BAG-Linie zur Kenntnisnahmemöglichkeit, Zugangszeitpunkt, Sorgfaltspflicht des Empfängers, Empfangsbevollmächtigung, taktische Beratung: Zugang bei Abwesen... |
| `fazugang-neu-003-zugang-urlaub-krankheit-klinik` | Fachanwalt Arbeitsrecht: Zugang bei Urlaub Krankheit Klinik und Auslandsaufenthalt mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis. |
| `fazugang-neu-004-inhalt-des-umschlags-bestreiten-und-beweisangeb` | Bestreiten des Inhalts eines zugestellten Umschlags: zulässige Einwände, Beweislast des Arbeitgebers für Schriftform und Inhalt, Gegenbeweis-Möglichkeiten, Prozessstrategie, Abgrenzung zu unzulässiger Schutzbehauptung: Bestreiten des Inh... |
| `fazugang-neu-004-inhalt-umschlag-bestreiten-beweisangebot` | Fachanwalt Arbeitsrecht: Inhalt des Umschlags bestreiten und Beweisangebot mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis. |
| `fazugang-neu-005-frist-berechnen-unsicher-zugang` | Fachanwalt Arbeitsrecht: Kündigungsfrist berechnen bei unsicherem Zugang mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis. |
| `fazugang-neu-005-kuendigungsfrist-berechnen-bei-unsicherem-zugan` | Kündigungsfrist berechnen bei unsicherem Zugangsdatum: frühest- und spätestmöglicher Zugang, Fristberechnung Paragrafen 187 ff: BGB, Drei-Wochen-... |
| `fazugang-neu-006-arbeitgeber-zustellworkflow-rechtssicher` | Fachanwalt Arbeitsrecht: Arbeitgeber-Zustellworkflow rechtssicher organisieren mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis. |
| `fazugang-neu-006-arbeitgeber-zustellworkflow-rechtssicher-organi` | Arbeitgeber-Zustellworkflow: rechtssichere Organisation der Kündigungszustellung, Parallelwege (Bote + Einschreiben + Gerichtsvollzieher), Checklisten, Kuvertierungsprotokoll, Risikomanagement bei mehreren Empfängern (Massenentlassung):... |
| `fazugang-neu-007-arbeitnehmerverteidigung-zugang-bestreiten-ohne` | Arbeitnehmerverteidigung: Zugang bestreiten ohne unwahre Behauptungen — zulässige Einwände, Beweislastverteilung, Paragraf 138 ZPO-Wahrheitspflicht, Strategie für Fristverteidigung, nachträgliche Zulassung Paragraf 5 KSchG: Arbeitnehmerv... |
| `fazugang-neu-008-schriftform-kuendigung-original-elektronisch` | Fachanwalt Arbeitsrecht: Schriftform Kündigung Original und elektronische Kommunikation mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis. |
| `fazugang-neu-008-schriftform-kuendigung-original-und-elektronisc` | Schriftform Kündigung Paragraf 623 BGB: Originalunterschrift zwingend, Faksimile unzulässig, elektronische Kommunikation (E-Mail, WhatsApp, Fax, Teams) genügt nicht: Schriftform Kündigung Paragraf 623 BGB: Originalunterschrift zwingend,... |
| `freistellungsklausel-sonderfall-edge-case` | Freistellungsklausel im Arbeitsvertrag: BAG 5 AZR 108/25 (pauschale Klausel unwirksam), anlassbezogene Formulierung, Vergütungsfortzahlung, Urlaubsverfall während Freistellung, Verrechnung mit Urlaubsabgeltung, Edge Cases: Freistellungsk... |
| `hinschg-whistleblower-repressalie` | Verteidigung von Hinweisgebern nach HinSchG gegen Repressalien durch Arbeitgeber: Anwendungsfall Arbeitnehmer hat intern oder extern Hinweis gegeben und wurde daraufhin gekünd... |
| `homeoffice-kontrollrecht-paragraf-106-gewo-lag-rheinland-pfalz` | Homeoffice Kontrollrecht Arbeitgeber Paragraf 106 GewO und Art 8 EMRK. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `kschg-risikoampel-und-gegenargumente` | KSchG Risikoampel: systematische Bewertung der Kündigung nach betriebsbedingten, personenbedingten und verhaltensbedingten Gründen, Sozialauswahl, BR-Anhörung, Massenentlassung — Grün/Gelb/Rot mit Gegenargumenten und nächstem Handgriff:... |
| `kuendigung-per-einschreiben-risiken` | Einschreiben, Post und Zugang: warum Einwurf-/Übergabe-Einschreiben oft nicht genügt und wie man Beweis sauber führt: Normanker: BGB Paragraf 13... |
| `kuendigungsschutzklage` | Kündigungsschutzklage nach Paragraf 4 KSchG mit Drei-Wochen-Frist ab Zugang der schriftlichen Kündigung: Anwendungsfall Arbeitnehmer erhaelt Kündigung und will Klage... |
| `low-performer-kuendigung-bag-2-azr-359-02` | Verhaltensbedingte Kuendigung Low Performer mit BAG 2 AZR 359/02; Vergleichsmassstab Kollegen. |
| `massenentlassung-17-kschg` | Fachanwalt Arbeitsrecht Massenentlassung 17 KSchG: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Arbeitsrecht Massenentlassung 17 KSchG: ordnet Normen, Nutzerangabe... |
| `massenentlassung-17-kschg-realitaetscheck` | Massenentlassung: Anzeige, Konsultation, Agentur für Arbeit, Fehlerfolgen, neue Rechtsprechung und Rettungsstrategie: Normanker: KSchG Paragraf... |
| `massenentlassung-anzeige-eugh-junk-bag-6-azr-155-21` | Massenentlassung Anzeigeverfahren Paragraf 17 KSchG mit EuGH Junk und BAG 6 AZR 155/21 als Prüfraster Anzeigezeitpunkt. |
| `orientierung-mandat-fachanwaltschaft` | Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach Paragraf 10 FAO: Anwendungsfall Kanzlei wi... |
| `output-waehlen` | Output-Wahl für Fachanwalt Arbeitsrecht: stimmt Adressat (Arbeitnehmer, Arbeitgeber, Betriebsrat), Frist (Paragraf 4 KSchG 3 Wochen Kündigungsschutzklage) und Form auf den Zweck ab — typische Outputs: Kündigungsschutzklage, Aufhebungsver... |
| `paragraf-dokumentenmatrix-und-lueckenliste` | Paragraf-Dokumentenmatrix und Lückenliste: für jeden Streitgegenstand die einschlägigen Normen, erforderlichen Dokumente und fehlenden Belege tabellarisch aufbereiten — Kündigung, Befristung, Abfindung, Vergütung, Betriebsrat, AGG: Parag... |
| `quelle-beweislast-und-darlegungslast` | Quellenregel, Beweislast und Darlegungslast im Arbeitsrecht: abgestufte Darlegungslast BAG-Linie, Normenübersicht zu Beweislastverteilungen, Umkehr nach AGG Paragraf 22, zulässige und unzulässige Fundstellen, Quellenprotokoll für Schrift... |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Arbeitsrecht: prüft Normen (BGB Paragrafen 611a ff., 623, KSchG Paragrafen 1/4/7, AGG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Arbeitsgericht (1. Instanz) und Quellenhygie... |
| `rechtsprechung-internationaler-bezug-und-schnittstellen` | Internationaler Bezug im Arbeitsrecht: EuGH-Rechtsprechung (Massenentlassung, Befristung, Diskriminierung, Urlaub), EU-Richtlinien (RL 2023/970, RL 2001/23, RL 2008/94, RL 2003/88), Entsendung AEntG, internationales Privatrecht Rom I: In... |
| `rechtsprechung-livecheck-arbeitsrecht` | Live-Check für arbeitsrechtliche Rechtsprechung: Prüfprotokoll für BAG-, LAG- und EuGH-Zitate, Verifizierungswege über bundesarbeitsgericht.de, openjur.de, dejure.org, curia.europa.eu, Umgang mit nicht verifizierbaren Quellen: Live-Check... |
| `scheinselbststaendigkeit-statusfeststellung-bsg-b-12-r-11-18` | Scheinselbststaendigkeit Statusfeststellung nach Paragraf 7a SGB IV und BSG B 12 R 11/18 R. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Kündigungsschutzklage, Befristungskontrollklage, Zahlungsklage Arbeitsgericht: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau: Substantiie... |
| `spezial-aktenzeichen-red-team-und-qualitaetskontrolle` | Aktenzeichen: Red-Team und Qualitätskontrolle. |
| `spezial-arbeitsrecht-tatbestand-beweis-und-belege` | Arbeitsrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `spezial-befristung-compliance-dokumentation-und-akte` | Befristung: Compliance-Dokumentation und Aktenvermerk. |
| `spezial-betriebsrat-zahlen-schwellen-und-berechnung` | Betriebsrat: Zahlen, Schwellenwerte und Berechnung. |
| `spezial-betrvg-behoerden-gericht-und-registerweg` | Betrvg: Behörden-, Gerichts- oder Registerweg. |
| `spezial-datum-formular-portal-und-einreichung` | Datum: Formular, Portal und Einreichungslogik. |
| `spezial-entgtranspg-verhandlung-vergleich-und-eskalation` | Entgtranspg: Verhandlung, Vergleich und Eskalation. |
| `spezial-fao-fristen-form-und-zustaendigkeit` | FAO: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `spezial-freistellungsklausel-sonderfall-und-edge-case` | Freistellungsklausel: Sonderfall und Edge-Case-Prüfung. |
| `spezial-kschg-risikoampel-und-gegenargumente` | Kschg: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `spezial-paragraf-dokumentenmatrix-und-lueckenliste` | Paragraf: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `spezial-quelle-beweislast-und-darlegungslast` | Quelle: Beweislast, Darlegungslast und Substantiierung. |
| `spezial-rechtsprechung-internationaler-bezug-und-schnittstellen` | Rechtsprechung: Internationaler Bezug und Schnittstellen. |
| `spezial-rechtsprechung-livecheck-arbeitsrecht` | Livecheck verifizierter Arbeitsrechtsprechung: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-tzbfg-schriftsatz-brief-und-memo-bausteine` | Tzbfg: Schriftsatz-, Brief- und Memo-Bausteine. |
| `spezial-unwirksam-fristennotiz-und-naechster-schritt` | Unwirksam: Fristennotiz und nächster Schritt. |
| `spezial-urlaub-livequellen-und-rechtsprechungscheck` | Urlaub: Livequellen- und Rechtsprechungscheck. |
| `spezial-vergleichspraxis-mehrparteien-konflikt-und-interessen` | Vergleichspraxis: Mehrparteienkonflikt und Interessenmatrix. |
| `spezial-verifizierter-mandantenentscheidung` | Verifizierter: Mandantenkommunikation und Entscheidungsvorlage. |
| `tzbfg-schriftsatz-brief-und-memo-bausteine` | TzBfG Schriftsatz-, Brief- und Memo-Bausteine: Klageschrift Entfristungsklage Paragraf 17 TzBfG, Klageantrag, Sachverhaltsaufbau, Beweisangebote, Mandantenbrief zur Befristungsbeendigung, Arbeitgeberantwortbrief, Vergleichsformel: TzBfG... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Arbeitsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Arbeitsvertrag, Kündigung, Aufhebungsvertrag), nennt pro Lücke Beweisthema, Beschaffungsweg (Arbeitsgericht (1. Instanz)), Frist... |
| `unwirksam-fristennotiz-und-naechster-schritt` | Unwirksamkeit erkannt — Fristennotiz und nächster Schritt: sofortige Handlungsanleitung nach erkanntem Unwirksamkeitsgrund (Schriftform, BR-Anhörung, Sonderkündigungsschutz, Massenentlassung, Befristungsfehler) — Fristberechnung, Klagewe... |
| `urlaub-quellenkarte` | Urlaub Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `urlaubsabgeltung-verjaehrung-eugh-c-518-20` | Urlaubsabgeltung Verjaehrung Mitwirkungsobliegenheit nach EuGH C-518/20 und BAG 9 AZR 266/20. |
| `v392-fachanwaltsblick-fachanwalt-arbeitsrecht` | Fachanwaltsblick für Arbeitsrecht: Mandantengespräch, typische Fallkonstellationen, FAO-geprägte Themenbreite, Belegbedarf, Schriftsatzstruktur und taktischer nächster Schritt werden zusammengeführt. |
| `vergleich-arbeitsgericht-abrechnung` | Arbeitsgerichtlicher Vergleich: Beendigungsdatum, Zeugnis, Turboklausel, Urlaubsabgeltung, Sprinter, Sperrzeit und Abrechnung: N... |
| `vergleichspraxis-mehrparteien-konflikt-und-interessen` | Vergleichspraxis bei Mehrparteienkonstellationen und komplexen Interessenlagen: Dreiparteienvergleich (AG, AN, BR), Sozialplanverhandlung, Interessenausgleich Paragraf 111 BetrVG, Vergleich mit Namensliste Paragraf 1 Absatz Vergleichspra... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Individual- und kollektives Arbeitsrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich): Vergleichsverha... |
| `verhandlung-guete-abfindung-arbg` | Gueteverhandlung im Arbeitsgerichtsverfahren nach Paragraf 54 ArbGG mit Auflösungsantrag und Abfindungsstrategie: Anwendungsfall Guetetermin steht an und Ver... |
| `verifizierter-mandantenentscheidung` | Verifizierte Mandantenentscheidung: strukturierter Entscheidungsprozess für Mandanten vor rechtlich verbindlichen Schritten — Klage, Aufhebungsvertrag, Vergleich, Widerspruch: Verifizierte Mandantenentscheidung: strukturierter Entscheidu... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix für arbeitsrechtliche Mandate: zeitliche Sachverhaltsaufbereitung, Ereignis-Zeitachse, Dokumentenzuordnung nach Datum, Lückenidentifikation, Erstellung einer strukturierten Fallchronologie als Arbeitsgrundlage... |
| `workflow-fristen-und-risikoampel` | Fristen und Risikoampel: vollständige Fristenübersicht für arbeitsrechtliche Mandate, Ampelbewertung nach Dringlichkeit, Fristenkalender, Wiedervorlagensystem, kritische Fristen Kündigung KSchG, Befristung TzBfG, AGG, Berufung ArbGG: Fri... |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Arbeitsrechtsmandat: Mandantenbriefe, E-Mails, Gesprächsvorbereitung, Informationspflichten, Kostenhinweis RVG, Akteneinsicht, Verfahrensstandsmeldungen, Aufklärungsbrief vor Klageerhebung: Mandantenkommunikatio... |
| `workflow-redteam-qualitygate` | Red-Team Qualitätsgate: abschließende Qualitätskontrolle vor Ausgabe eines Schriftsatzes, Memos, Mandantenbriefs oder Vergleichs — Quellenverifikation, Gegenargument-Check, Fristencheck, Scheingenauigkeit-Scan, Mandatsziel-Abgleich: Red-... |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zugang-kuendigung-bote-beweis` | Zugang der Kündigung: Bote, Einwurf, Umschlaginhalt, Zugangstag, Beweis im Kündigungsschutzprozess: Normanker: KSchG Paragraf 4; BGB Paragrafen 130 und 623; ZPO Beweis; B... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
