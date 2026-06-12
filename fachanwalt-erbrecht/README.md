# Fachanwalt Erbrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`fachanwalt-erbrecht.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/fachanwalt-erbrecht.md) (66 KB)
- Im Repo: [`testakten/megaprompts/fachanwalt-erbrecht.md`](../testakten/megaprompts/fachanwalt-erbrecht.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

### Formatvorlagen (Markdown + ODT)

Sofort verwendbare Vorlagen (Times Roman 11pt, A4, mit Disclaimer und Feldern in [Klammern]). Markdown zum Lesen / Anpassen, ODT zum Bearbeiten in LibreOffice/Word.

| Vorlage | Markdown | ODT |
| --- | --- | --- |
| Erbscheinantrag Paragraf 2353 Bgb | [`.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-erbrecht/erbscheinantrag-paragraf-2353-bgb.md) | [`.odt`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-erbrecht/erbscheinantrag-paragraf-2353-bgb.odt) |

*Experimentelle KI-Vorlagen — keine Haftung. Vor Verwendung im Mandat anwaltlich prüfen und an konkreten Fall anpassen.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-erbrecht`) | [`fachanwalt-erbrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-erbrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Erbstreit Edelmann — Multisig, Pflichtteil, Patchworkfamilie** (`erbstreit-krypto-multisig-edelmann-stuttgart`) | [Gesamt-PDF lesen](../testakten/erbstreit-krypto-multisig-edelmann-stuttgart/gesamt-pdf/erbstreit-krypto-multisig-edelmann-stuttgart_gesamt.pdf) | [`testakte-erbstreit-krypto-multisig-edelmann-stuttgart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-erbstreit-krypto-multisig-edelmann-stuttgart.zip) |

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


Plugin Fachanwalt für Erbrecht. Orientierung BGB Erbrecht §§ 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaft- und Schenkungsteuer ErbStG EU-ErbVO. Schnittstellen steuerrecht-anwalt-und-berater und gesellschaftsrecht.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-erbrecht-orientierung` | Orientierung im Erbrecht — FAO Voraussetzungen Normen typische Mandate Fristen Quellenprüfung. BGB Erbrecht §§ 1922 ff. (Erbfolge gesetzliche und gewillkürte Erbfolge Testament Erbvertrag Pflichtteil Vermächtnis)… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 70 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Erbrecht: wählt den nächsten Spezial-Skill nach Engpass (Ausschlagung 6 Wochen § 1944 BGB, Testament/Erbvertrag, Erbschein-Antrag, Nachlassverzeichnis), dokumentiert Router-Entscheidung mit Begründung. |
| `belegmatrix-sonderfall-edge-case` | Belegmatrix: Sonderfall und Edge-Case-Prüfung im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitspr... |
| `berater-mehrparteien-konflikt-und-interessen` | Berater: Mehrparteienkonflikt und Interessenmatrix im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbe... |
| `bgb-fristen-form-und-zustaendigkeit` | BGB: Fristen, Form, Zuständigkeit und Rechtsweg im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeits... |
| `chronologie-beweislast-und-darlegungslast` | Chronologie: Beweislast, Darlegungslast und Substantiierung im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzb... |
| `digitaler-nachlass-facebook-bgh-iii-zr-183-17` | Digitaler Nachlass Facebook BGH Iii Zr 183 17: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Erbrecht: sortiert Testament/Erbvertrag, Erbschein-Antrag, Nachlassverzeichnis, prüft Datum, Absender, Frist und Beweiswert (Originaltestament, Eröffnungsprotokoll); markiert Lücken; berücksichtigt Mandats... |
| `ehegattentestament-bindungswirkung` | Ehegattentestament Bindungswirkung: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `einstieg-routing` | Anwalts-Dashboard Fachanwalt Erbrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt blei... |
| `einstieg-schnelltriage-fallrouting` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Erbrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin... |
| `erb-einfuehrung-erbfolge-system` | Erbfolge-System einfuehrend: gesetzliche Erbfolge §§ 1924 ff: BGB, Verwandtenerbrecht in Ordnungen, Ehegattenerbrecht § 1931 BGB mit Zugewinngemeinschaft § 1371 BGB, Pflichtteil §§ 2303 ff. BGB.... |
| `erb-erbschaftsteuer-progressionsoptimierung-spezial` | Spezialfall Erbschaftsteuer-Optimierung: Freibetraege § 16 ErbStG, Steuerklassen I / II / III, Bewertung Betriebsvermoegen §§ 13a / 13b ErbStG, Familienheim § 13 ErbStG: Spezialfall Erbschaftsteuer-Optimierung: Freibetraege § 16 ErbStG,... |
| `erb-erstgespraech-checkliste` | Erstgespraechs-Checkliste Erbrecht: Familienverhaeltnisse, vorhandene Testamente, Nachlassbestand, Schulden, internationaler Bezug, Pflichtteilsberechtigte, Streitlage: Erstgespraechs-Checkliste Erbrecht: Familienverhaeltnisse, vorhanden... |
| `erb-internationales-erbrecht-spezial` | Spezialfall internationales Erbrecht: EuErbVO 650/2012, gewoehnlicher Aufenthalt als Anknuepfungspunkt, Rechtswahl, Europaeisches Nachlasszeugnis ENZ: Spezialfall internationales Erbrecht: EuErbVO 650/2012, gewoehnlicher Aufenthalt als A... |
| `erb-nachlassinventar-erstellung` | Nachlassinventar erstellen: Aktiva (Konten, Immobilien, Beteiligungen, Hausrat), Passiva (Schulden, Pflichtteile, Vermaechtnisse), Stichtagsbewertung, Sicherung des Nachlasses: Nachlassinventar erstellen: Aktiva (Konten, Immobilien, Bete... |
| `erb-pflichtteilsanspruch-berechnung-spezial` | Spezialfall Pflichtteilsberechnung detailliert: § 2303 BGB, Höhe Pflichtteil = halbe gesetzliche Erbquote, Pflichtteilsergaenzungsanspruch § 2325 BGB für Schenkungen 10-Jahres-Frist mit Abschmelzung: Spezialfall Pflichtteilsberechnung d... |
| `erb-testamentsformen-grundzuege` | Testamentsformen Grundzuege: eigenhaendiges Testament § 2247 BGB, öffentliches Testament § 2232 BGB, Nottestament § 2249 BGB, Berliner Testament § 2269 BGB: Testamentsformen Grundzuege: eigenhaendiges Testament § 2247 BGB, öffentliches T... |
| `erb-unternehmensnachfolge-spezial` | Spezialfall Unternehmensnachfolge: Vorab-Nachfolgeklauseln in Gesellschaftsvertrag, Pflichtteilsverzicht durch Erben, Stiftungsloesung, Verschonungsregelung §§ 13a / 13b / 19a ErbStG, Nachversteuerung Behaltensfrist: Spezialfall Unterneh... |
| `erbauseinandersetzung-textbausteine` | Erbauseinandersetzung: Schriftsatz-, Brief- und Memo-Bausteine im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nu... |
| `erbengemeinschaft-blockade-auseinandersetzung` | Erbengemeinschaft: Verwaltung, Blockade, Teilungsversteigerung, Nachlasskonto, Auskunft und Auseinandersetzungsplan: Normanker: BGB §§ 203... |
| `erbfall-intake-und-nachlassordnung` | Erbfall-Intake, Nachlassordnung und erste Fristen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output: Erbfall-Intake, Nachlassordnung und erste Fristen: führt schnell durch... |
| `erbrecht-tatbestand-beweis-und-belege` | Erbrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbar... |
| `erbschaftsausschlagung` | Erbschaftsausschlagung erläutern und Erklärung formulieren wenn Erbe ueberschuldet ist oder sonstige Gründe vorliegen: §§ 1942 1944 1945... |
| `erbschaftsteuer-verhandlung-vergleich-und-eskalation` | Erbschaftsteuer: Verhandlung, Vergleich und Eskalation im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem... |
| `erbschein-antrag` | Erbschein beantragen wenn Erbfolge nachgewiesen werden muss: §§ 2353 2356 BGB Erbschein §§ 352 353 FamFG Verfahren. Prüfraster: Erbscheinsart gesetzliche oder testamentarische Erbfolge Quoten Vorl... |
| `erbschein-behoerden-gericht-und-registerweg` | Erbschein: Behörden-, Gerichts- oder Registerweg im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeit... |
| `erbschein-einziehung-paragraf-2361-bgb-olg-muenchen-31-wx-275-19` | Erbschein Einziehung Paragraf 2361 BGB Olg Muenchen 31 Wx 275 19: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `erbverzicht-pflichtteilsverzicht` | Erbverzicht Pflichtteilsverzicht: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `erbvo-quellenkarte` | Erbvo Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `erstgespraech-mandatsannahme` | Erstgespraech im Erbrechtmandat strukturieren und Sachverhalt vollständig aufnehmen: §§ 1922 ff. BGB Erbfolge § 43a BRAO. Prüfraster: Erblasser Testament gesetzliche Erben... |
| `erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem... |
| `internationaler-erbfall-eu-erbvo` | Internationaler Erbfall: gewöhnlicher Aufenthalt, Rechtswahl, Europäisches Nachlasszeugnis, Auslandsvermögen und Grundbuch: Normank... |
| `kanzlei-internationaler-bezug-und-schnittstellen` | Kanzlei: Internationaler Bezug und Schnittstellen im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbei... |
| `krypto-wallet-nachlass-multisig` | Krypto-Vermögenswerte und digitale Wallets im Erbfall sichern und auf Erben uebertragen: §§ 1922 1967 BGB digitale Nachlasswerte. Prüfraster: Wallet-Zugang Private Keys... |
| `livecheck-mandantenkommunikation-entscheidungsvorlage` | Livecheck: Mandantenkommunikation und Entscheidungsvorlage im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzba... |
| `mandat-einordnen-bearbeitungsroute` | Erbrechtsmandat einordnen Bearbeitungsroute bestimmen und erste Prioritaeten setzen: §§ 1922 2229 2303 BGB § 43a BRAO. Prüfraster: Erbfolge Testament Pflichtteil Ausschlagu... |
| `mandat-triage-erbrecht` | Erbrechtsmandat schnell einordnen und Sofortmassnahmen bestimmen: §§ 1922 1944 2303 BGB §§ 342 ff. FamFG. Prüfraster: Erbfolge Testament Ausschlagungsfrist Pflichtteil Nachlassinsolvenz. Outp... |
| `nachlassinsolvenz-erbenhaftung-begrenzen` | Nachlassinsolvenz beantragen oder Erbenhaftung auf den Nachlass begrenzen wenn Nachlass ueberschuldet ist: §§ 1975 1980 2059 BGB Nachlassinsolvenz §§... |
| `nachlassinsolvenz-paragraf-1980-bgb-bgh-ix-zb-118-17` | Nachlassinsolvenz Paragraf 1980 BGB BGH Ix Zb 118 17: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `output-waehlen` | Output-Wahl für Fachanwalt Erbrecht: stimmt Adressat (Erblasser (Beratung), Erben, Vermächtnisnehmer), Frist (Ausschlagung 6 Wochen § 1944 BGB) und Form auf den Zweck ab — typische Outputs: Testamentsentwurf, Erbscheinantrag, Pflichtteil... |
| `pflegevermaechtnis-paragraf-2057a-bgb-bgh-iv-zr-318-13` | Pflegevermaechtnis Paragraf 2057a BGB BGH Iv Zr 318 13: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `pflichtteil-auskunft-wertermittlung` | Pflichtteil: Auskunft, notarielles Nachlassverzeichnis, Wertermittlung, Ergänzung und taktische Stufenklage: Normanker: BGB §§ 2303 und 2314 und 2... |
| `pflichtteil-berechnen` | Pflichtteilsanspruch und Pflichtteilsergaenzungsanspruch berechnen: §§ 2303 2311 2325 BGB Pflichtteil. Prüfraster: Pflichtteilsquote Nachlasswert Bewertungsstichtag Abzuege Ergaenzungsanspr... |
| `pflichtteil-dokumentenmatrix-und-lueckenliste` | Pflichtteil: Dokumentenmatrix, Lückenliste und Nachforderung im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutz... |
| `pflichtteil-vaterschaft-verjaehrung-und-auskunft` | Führt durch Pflichtteilsfälle mit später festgestellter Vaterschaft, § 1600d Abs: 5 BGB, § 2317 BGB, § 199 BGB und Auskunftsansprüchen nach § 2314 BGB. |
| `pflichtteilsberechnung` | Pflichtteilsanspruch berechnen wenn Erblasser nahe Angehoerige vom Erbe ausgeschlossen hat: §§ 2303 2311 2314 BGB Pflichtteil. Prüfraster: Pflichtteilsberechtigter N... |
| `pflichtteilsergaenzung-2325` | Pflichtteilsergaenzungsanspruch nach § 2325 BGB berechnen wenn Erblasser Schenkungen gemacht hat: § 2325 BGB Pflichtteilsergaenzung § 2329 BGB. Prüfraster: Sch... |
| `pflichtteilsergaenzung-frist-naechster-schritt` | Pflichtteilsergaenzung: Fristennotiz und nächster Schritt im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbar... |
| `pflichtteilsergaenzung-zehnjahresfrist-bgh-iv-zr-249-15` | Pflichtteilsergaenzung Zehnjahresfrist BGH Iv Zr 249 15: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `progressionsoptimierung-formular-portal-und-einreichung` | Progressionsoptimierung: Formular, Portal und Einreichungslogik im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt n... |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Erbrecht: prüft Normen (BGB §§ 1922 ff., ErbStG, FamFG §§ 342 ff.) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Nachlassgericht (AG) und Quellenhygiene nach references/quellenh... |
| `rechtsquellen-fehlerkatalog` | Rechtsquellen Fehlerkatalog: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `schnittstellen-zahlen-schwellen-und-berechnung` | Schnittstellen: Zahlen, Schwellenwerte und Berechnung im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem A... |
| `schriftsatzkern-substantiierung` | Erbrechtsklage oder erbrechtlichen Antrag substantiiert formulieren: §§ 2303 2353 BGB §§ 253 286 ZPO. Prüfraster: Anspruchsgrundlage Sachverhalt Beweisangebot Antrag Streitwert Fristen. Ou... |
| `steuerrecht-compliance-dokumentation-und-akte` | Steuerrecht: Compliance-Dokumentation und Aktenvermerk im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem... |
| `testament-auslegung-und-andeutung` | Testamentsauslegung: Andeutung, Erblasserwille, Wortlautgrenzen, laienhafte Begriffe und Beweisquellen: Normanker: BGB §§ 133 und 2084 und 2065; FamFG... |
| `testament-risikoampel-und-gegenargumente` | Testament: Risikoampel, Gegenargumente und Verteidigungslinien im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nu... |
| `testamentsentwurf` | Testament oder Erbvertrag entwerfen wenn Mandant Nachlassplanung vornehmen moechte: §§ 2229 2231 2247 BGB Testament §§ 2274 ff. BGB Erbvertrag. Prüfraster: Testierfähigkeit... |
| `testamentsvollstrecker-kontrolle-haftung` | Testamentsvollstrecker: Amt, Zeugnis, Auskunft, ordnungsgemäße Verwaltung, Entlassung und Haftung: Normanker: BGB §§ 2197 ff., 2218 und 2227 und 2219; fragt... |
| `testamentsvollstreckung` | Testamentsvollstreckung einrichten oder bei Streit über Vollstreckerbefugnisse beraten: §§ 2197 ff. BGB Testamentsvollstreckung. Prüfraster: Anordnung Befugnisse Aufgabe... |
| `testamentsvollstreckung-vergutung` | Testamentsvollstreckung Vergutung: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `testierfaehigkeit-demenz-olg-koeln-2-wx-128-17` | Testierfaehigkeit Demenz Olg Koeln 2 Wx 128 17: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Erbrecht: trennt fehlende Tatsachen von fehlenden Belegen (Testament/Erbvertrag, Erbschein-Antrag, Nachlassverzeichnis), nennt pro Lücke Beweisthema, Beschaffungsweg (Nachlassgericht (AG)), Fr... |
| `vergleichsverhandlung-strategie` | Erbrechtlichen Streit durch Vergleich lösen und Verhandlungsstrategie entwickeln: §§ 2303 2042 BGB §§ 779 BGB Vergleich. Prüfraster: Vergleichsziele BATNA Nachlasswert Kosten... |
| `verhandlung-mediation-erbengemeinschaft` | Streit in der Erbengemeinschaft durch Verhandlung oder Mediation lösen: §§ 2032 2042 2047 BGB Erbengemeinschaft. Prüfraster: Erbteile Nachlassbestand Verwaltungsmassnahmen Teilungsklage... |
| `vor-und-nacherbschaft-paragraf-2113-bgb-bgh-iv-zr-201-13` | Vor Und Nacherbschaft Paragraf 2113 BGB BGH Iv Zr 201 13: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
