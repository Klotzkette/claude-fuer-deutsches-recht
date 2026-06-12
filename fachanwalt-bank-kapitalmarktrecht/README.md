# Fachanwalt Bank Kapitalmarktrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-bank-kapitalmarktrecht`) | [`fachanwalt-bank-kapitalmarktrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-bank-kapitalmarktrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Cybertrading-Anlagebetrug Wittfeldt – Bremen** (`cybertrading-anlagebetrug-wittfeldt-bremen`) | [Gesamt-PDF lesen](../testakten/cybertrading-anlagebetrug-wittfeldt-bremen/gesamt-pdf/cybertrading-anlagebetrug-wittfeldt-bremen_gesamt.pdf) | [`testakte-cybertrading-anlagebetrug-wittfeldt-bremen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-cybertrading-anlagebetrug-wittfeldt-bremen.zip) |
| **Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio** (`private-equity-buyout-schuldschein-npl-heidelberg`) | [Gesamt-PDF lesen](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf) | [`testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin Fachanwalt für Bank- und Kapitalmarktrecht. Orientierung KWG ZAG WpHG WpIG MiFID-II MAR Marktmissbrauch MiCAR Verbraucherkredit Vermögensanlage Beratungshaftung. Schnittstellen gesellschaftsrecht und regulatorisches-recht.

Der bankrechtliche Teil deckt nun ausdrücklich auch die klassischen Sicherungs- und Liquiditätsinstrumente ab: Bürgschaft, kaufmännische Bürgschaft, Aval, Kautionsaval, Bankgarantie, Bürgschaft auf erstes Anfordern, Akkreditiv, Standby Letter of Credit, Dokumentenstreit, Abruf, Eilrechtsschutz und Regress. Das ist der praktische Kern vieler Mandate: Die Bank sichert den Geschäftsverkehr ab, verschafft Liquidität, und im Streit entscheidet die genaue Formulierung des Sicherungsmittels.

Beginne bei solchen Mandaten mit `bankrecht-buergschaft-aval-garantie-routing`; der Skill ordnet Rolle, Dokumenttyp, Frist, Einwendung und nächsten Output.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-bank-kapitalmarktrecht-orientierung` | Orientierung im Bank- und Kapitalmarktrecht — FAO Voraussetzungen Normen typische Mandate Quellenprüfung. KWG (Kreditwesengesetz) ZAG (Zahlungsdiensteaufsichtsgesetz) WpHG (Wertpapierhandelsgesetz) WpIG (Wertpapier… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 72 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anlageberatung-fehlerhaft` | Fachanwalt Bank Kapitalmarktrecht Anlageberatung Fehlerhaft: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Bank Kapitalmarktrecht Anlageberatung Fehlerhaft: ordnet... |
| `anlageberatungsfehler-pruefen` | Anlageberatungsfehler Prüfen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Anlageberatungsfehler Prüfen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rech... |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Bank- und Kapitalmarktrecht: wählt den nächsten Spezial-Skill nach Engpass (Widerrufsfrist Verbraucherdarlehen 14 Tage § 355 BGB, Darlehensvertrag, Wertpapierorder, Beratungsprotokoll), dokumentiert Route... |
| `bank-tatbestand-beweis-und-belege` | Bank: Tatbestandsmerkmale, Beweisfragen und Beleglage: Bank: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `bankaufsicht-erlaubnis-und-vertrieb` | Bankaufsichtliche Erlaubnis-, Vertriebs- und Organisationsrisiken: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output: Bankaufsichtliche Erlaubnis-, Vertriebs- und Organisati... |
| `bankrecht-akkreditiv-standby-lc-dokumentenstreit` | Akkreditiv, Standby Letter of Credit und Dokumentenstreit im Bankmandat prüfen: Dokumentenstrenge, Discrepancies, Fraud, Sanktionen, Zahlungsstopp, Begünstigtenrechte und Bankhaftung: Akkreditiv, Standby Letter of Credit und Dokumentenst... |
| `bankrecht-buergschaft-auf-erste-anforderung` | Bürgschaft oder Bankgarantie auf erste Anforderung im Mandat prüfen: Zahlungsmechanik, Einwendungen, offensichtlicher Missbrauch, einstweiliger Rechtsschutz, Rückforderung und Regress: Bürgschaft oder Bankgarantie auf erste Anforderung i... |
| `bankrecht-buergschaft-aval-garantie-routing` | Mandat zu Bürgschaft, Aval oder Bankgarantie im Bankrecht routen: Bürge, Bank, Begünstigter oder Kunde: §§ 765 ff. BGB, §§ 349 und 350 HGB, erstes Anford... |
| `bankrecht-garantieabruf-eilrechtsschutz` | Eilrechtsschutz bei Abruf aus Bankgarantie, Aval oder Bürgschaft auf erstes Anfordern vorbereiten: Verfügungsanspruch, Verfügungsgrund, Missbrauchsbelege, Zustellung, Vollziehung und Bankkommunikation: Eilrechtsschutz bei Abruf aus Bankg... |
| `bankrecht-kaufmaennische-buergschaft-hgb-349-350` | Kaufmännische Bürgschaft prüfen: Handelsgeschäft des Bürgen, § 349 HGB ohne Vorausklage, § 350 HGB ohne BGB-Schriftform, Abgrenzung zu privater Mithaftung, AGB und Prozessstrategie: Kaufmännische Bürgschaft prüfen: Handelsgeschäft des Bü... |
| `bankrecht-privatbuergschaft-sittenwidrigkeit` | Privat-, Ehegatten- und Angehörigenbürgschaft prüfen: § 138 BGB, krasse finanzielle Überforderung, emotionaler Druck, Eigeninteresse, Bankkenntnis, Schriftform und Vergleichsstrategie: Privat-, Ehegatten- und Angehörigenbürgschaft prüfen... |
| `bankrecht-regress-nach-avalzahlung` | Regress nach Aval-, Bürgschafts- oder Garantiezahlung im Bankmandat prüfen: § 774 BGB, Aufwendungsersatz, Kontobelastung, Sicherheiten, Mitbürgen, Insolvenz, Anfechtung und Vergleich: Regress nach Aval-, Bürgschafts- oder Garantiezahlung... |
| `bausparvertrag-zinsanpassung-bgh-xi-zr-78-22` | Bausparvertrag Zinsanpassung BGH Xi Zr 78 22: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `beratungshaftung-zahlen-schwellen-und-berechnung` | Beratungshaftung: Zahlen, Schwellenwerte und Berechnung: Beratungshaftung: Zahlen, Schwellenwerte und Berechnung. |
| `bk-aufsicht-zag-dora-inhkontrolle-crr-arbeitskern` | Fachanwalts-Fachmodul für Bankaufsicht: ZAG-Erlaubnis, DORA-IKT-Risiko, KWG-Anzeigen nach AnzV, Inhaberkontrolle und CRR-Folgen in Mandatsvermerken, Behördenantworten und Prozessstrategie verknüpfen: Fachanwalts-Fachmodul für Bankaufsich... |
| `bk-bafin-beschwerdeverfahren-workflow` | BaFin-Beschwerdeverfahren Workflow: Schritte einfache Beschwerde, Anhörung, Beanstandung, Maßnahme: Inhalt und Beweismittel. Mustertext für Mandanten und A... |
| `bk-bankenfehlberatung-grundzuege` | Bankenfehlberatungs-Anspruch in Grundzuegen: § 280 BGB, anlegergerechte Beratung, anlagegerechte Beratung, MiFID II Geeignetheit, Aufklaerung Provision (Kick-back): Bankenfehlberatungs-Anspruch in Grundzuegen: § 280 BGB, anlegergerechte... |
| `bk-cum-ex-mandant-strafrecht-spezial` | Spezialfall Cum-Ex und Cum-Cum Mandate: Steuerstrafrecht § 370 AO, Verjährung, Selbstanzeige, Anrechnung KapErtSt: Verhältnis zu Schadensersa... |
| `bk-einfuehrung-aufsichtsstruktur` | Aufsichtsstruktur einfuehrend: EZB-SSM, BaFin, Bundesbank, ESMA: KWG, ZAG, WpIG, WpHG, KAGB, MAR. Welche Behörde ist wofür zuständig, wie kommunizieren wir. Tabellarische Übersicht und Beispi... |
| `bk-emissionsprospekt-haftung-spezial` | Spezialfall Emissionsprospekthaftung: WpPG, ProspektG, Verantwortliche, Gewaehrleistungserklaerung, fehlerhafte Angaben, Schaden, Kausalitaet: Spezialfall Emissionsprospekthaftung: WpPG, ProspektG, Verantwortliche, Gewaehrleistungserklae... |
| `bk-mandantenrouting-anlegeranspruch` | Routing-Tabelle Anlegeranspruch: Lebensversicherung, Geschlossener Fonds, Zertifikat, ETF, Cum-Ex / Cum-Cum, Krypto: Pro Produktart typische... |
| `bk-mifid-suitability-spezial` | Spezialfall MiFID II Geeignetheits- und Angemessenheitspruefung: Anlegerprofil, Ziele, Risikobereitschaft, Verlusttragfaehigkeit: Spezialfall MiFID II Geeignetheits- und Angemessenheitspruefung: Anlegerprofil, Ziele, Risikobereitschaft,... |
| `bk-prip-kid-fehlerhaft-spezial` | Spezialfall PRIIPs-KID fehlerhaft: PRIIPs-VO, Inhalt Basisinformationsblatt, Haftung Hersteller und Vertrieb bei irrefuehrenden Angaben, Prüfung Kosten- und Risikoangabe: Spezialfall PRIIPs-KID fehlerhaft: PRIIPs-VO, Inhalt Basisinforma... |
| `cum-ex-beihilfe-bgh-1-str-519-20` | Cum-Ex Phantom-Verluste Beihilfe Paragraf 263 StGB und BGH 1 StR 519/20. |
| `cybertrading-anlagebetrug` | Mandant ist Opfer eines Online-Trading-Betrugs (Cybertrading fake Plattform) und will Geld zurück: § 263 StGB Betrug Zivilansprüche gegen Vermittler Bank. Nor... |
| `dispokredit-zinsanpassung-bgh-xi-zr-78-08` | Dispokredit Zinsanpassungsklausel ohne Referenzbindung mit BGH XI ZR 78/08. |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Bank- und Kapitalmarktrecht: sortiert Darlehensvertrag, Wertpapierorder, Beratungsprotokoll, prüft Datum, Absender, Frist und Beweiswert (Beratungsprotokoll, Geeignetheitsprüfung); markiert Lücken; berücks... |
| `einstieg-routing` | Einstieg, Triage und Routing für Fachanwalt Bank- und Kapitalmarktrecht: ordnet Rolle (Anleger/Kunde, Bank/WPI, BaFin), markiert Frist (Widerrufsfrist Verbraucherdarlehen 14 Tage § 355 BGB), wählt Norm (BGB §§ 488/491-505, WpHG, KAGB) un... |
| `einstieg-schnelltriage-fallrouting` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Bank Kapitalmarktrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende... |
| `emissionsprospekt-mandantenentscheidung` | Emissionsprospekt: Mandantenkommunikation und Entscheidungsvorlage: Emissionsprospekt: Mandantenkommunikation und Entscheidungsvorlage. |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Bank-, Kapitalmarkt- und Wertpapierrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturier... |
| `erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel. |
| `fehlerhaft-fristennotiz-und-naechster-schritt` | Fehlerhaft: Fristennotiz und nächster Schritt: Fehlerhaft: Fristennotiz und nächster Schritt. |
| `gesellschaftsrecht-mehrparteien-konflikt-und-interessen` | Gesellschaftsrecht: Mehrparteienkonflikt und Interessenmatrix: Gesellschaftsrecht: Mehrparteienkonflikt und Interessenmatrix. |
| `haftung-beweislast-und-darlegungslast` | Haftung: Beweislast, Darlegungslast und Substantiierung: Haftung: Beweislast, Darlegungslast und Substantiierung. |
| `immobiliendarlehen-fehlerkatalog` | Immobiliendarlehen Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `kapitalmarktrecht-fristen-form-und-zustaendigkeit` | Kapitalmarktrecht: Fristen, Form, Zuständigkeit und Rechtsweg: Kapitalmarktrecht: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `kreditkuendigung` | Fachanwalt Bank Kapitalmarktrecht Kreditkuendigung: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Bank Kapitalmarktrecht Kreditkuendigung: ordnet Normen, Nutzeranga... |
| `kreditkuendigung-490-bgb` | Bank kündigt Kredit nach § 490 BGB wegen wesentlicher Vermögensverschlechterung und Mandant braucht Sofort-Strategie: AGB-Banken Nr. 19. No... |
| `lehman-zertifikat-kickback-bgh-xi-zr-33-10` | Lehman Zertifikat Kickback BGH Xi Zr 33 10: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `mandat-triage-bank-kapitalmarktrecht` | Bank- oder Kapitalmarktrechts-Mandat trifft ein und muss strukturiert erfasst werden: Sachgebiet Mandantenrolle Sofort-Fristen: V... |
| `mica-stablecoin-art-16-bafin` | Krypto-Unternehmen beantragt MiCA-Lizenz für Stablecoin (ART oder EMT) bei BaFin: MiCA VO 2023/1114 Art. 16-21 Whitepaper-Pflicht Art. 19 Eigenmittel Art. 35 Reserveaktiva Art... |
| `micar-schriftsatz-brief-und-memo-bausteine` | Micar: Schriftsatz-, Brief- und Memo-Bausteine: Micar: Schriftsatz-, Brief- und Memo-Bausteine. |
| `mietkaution-insolvenzfest-bgh-viii-zr-75-20` | Mietkaution insolvenzfeste Anlage Paragraf 551 BGB mit BGH VIII ZR 75/20. |
| `mifid-behoerden-gericht-und-registerweg` | Mifid: Behörden-, Gerichts- oder Registerweg: Mifid: Behörden-, Gerichts- oder Registerweg. |
| `ombudsmann-bafin-schlichtung` | Mandant will vor Klage Bank-Streit durch Ombudsmann-Verfahren oder BaFin-Beschwerde lösen: Ombudsmann private Banken Sparkassen BaFin-Beschwerde § 4b FinDAG. Normen §... |
| `orientierung-fachanwaltschaft-mandat` | Anwalt will Fachanwaltschaft Bank-Kapitalmarktrecht erwerben oder Mandat bearbeiten und braucht Normen-Überblick: KWG ZAG WpHG WpIG MiFID-II MA... |
| `output-waehlen` | Output-Wahl für Fachanwalt Bank- und Kapitalmarktrecht: stimmt Adressat (Anleger/Kunde, Bank/WPI, BaFin), Frist (Widerrufsfrist Verbraucherdarlehen 14 Tage § 355 BGB) und Form auf den Zweck ab — typische Outputs: Klage Falschberatung, Wi... |
| `p-konto-pfaendung-bgh-vii-zb-25-21` | P Konto Pfaendung BGH Vii Zb 25 21: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `praemiensparvertrag-zinsanpassung-bgh-xi-zr-234-20` | Praemiensparvertrag variable Verzinsung mit BGH XI ZR 234/20 und Bundesbank-Referenzzins WX4260. |
| `prip-sonderfall-edge-case` | Prip: Sonderfall und Edge-Case-Prüfung: Prip: Sonderfall und Edge-Case-Prüfung. |
| `prospekthaftung-inflationsanleihe-bgh-xi-zr-442-16` | Prospekthaftung inflationsindexierte Anleihe Paragraf 21 WpPG mit BGH XI ZR 442/16. |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Bank- und Kapitalmarktrecht: prüft Normen (BGB §§ 488/491-505, WpHG, KAGB) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt BaFin und Quellenhygiene nach references/quellenhygiene.md. |
| `regulatorisches-internationaler-bezug-und-schnittstellen` | Regulatorisches: Internationaler Bezug und Schnittstellen: Regulatorisches: Internationaler Bezug und Schnittstellen. |
| `riester-foerderschaedlich-pflege-bfh-x-r-19-19` | Riester foerderschaedliche Verwendung bei Pflegekosten mit BFH X R 19/19. |
| `schnittstellen-compliance-dokumentation-und-akte` | Schnittstellen: Compliance-Dokumentation und Aktenvermerk: Schnittstellen: Compliance-Dokumentation und Aktenvermerk. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Klage auf Schadensersatz aus Falschberatung, Widerrufsklage Verbraucherdarlehen: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau: Substanti... |
| `schufa-eintrag` | Fachanwalt Bank Kapitalmarktrecht Schufa Eintrag: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Bank Kapitalmarktrecht Schufa Eintrag: ordnet Normen, Nutzerangaben,... |
| `schufa-loeschungsanspruch` | Fachanwalt Bank Kapitalmarktrecht Schufa Loeschungsanspruch: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Bank Kapitalmarktrecht Schufa Loeschungsanspruch: ordnet... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Bank- und Kapitalmarktrecht: trennt fehlende Tatsachen von fehlenden Belegen (Darlehensvertrag, Wertpapierorder, Beratungsprotokoll), nennt pro Lücke Beweisthema, Beschaffungsweg (BaFin), Fris... |
| `verbraucherkredit-verhandlung-vergleich-und-eskalation` | Verbraucherkredit: Verhandlung, Vergleich und Eskalation: Verbraucherkredit: Verhandlung, Vergleich und Eskalation. |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Bank-, Kapitalmarkt- und Wertpapierrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich): Vergleichsverha... |
| `vermoegensanlage-quellenkarte` | Vermögensanlage Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `widerrufsjoker-formular-portal-und-einreichung` | Widerrufsjoker: Formular, Portal und Einreichungslogik: Widerrufsjoker: Formular, Portal und Einreichungslogik. |
| `widerrufsjoker-immobiliardarlehen-bgh-xi-zr-564-15` | Widerrufsjoker Immobiliardarlehen mit BGH XI ZR 564/15 und Art 247 EGBGB. |
| `widerrufsjoker-immobiliendarlehen` | Widerrufsjoker Immobiliendarlehen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Widerrufsjoker Immobiliendarlehen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizie... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `wphg-dokumentenmatrix-und-lueckenliste` | Wphg: Dokumentenmatrix, Lückenliste und Nachforderung: Wphg: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `wpig-risikoampel-und-gegenargumente` | Wpig: Risikoampel, Gegenargumente und Verteidigungslinien: Wpig: Risikoampel, Gegenargumente und Verteidigungslinien. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`fachanwalt-bank-kapitalmarktrecht.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/fachanwalt-bank-kapitalmarktrecht.md) (56 KB)
- Im Repo: [`testakten/megaprompts/fachanwalt-bank-kapitalmarktrecht.md`](../testakten/megaprompts/fachanwalt-bank-kapitalmarktrecht.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->
