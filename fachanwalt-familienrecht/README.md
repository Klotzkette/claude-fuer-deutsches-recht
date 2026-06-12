# Fachanwalt Familienrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`fachanwalt-familienrecht.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/fachanwalt-familienrecht.md) (53 KB)
- Im Repo: [`testakten/megaprompts/fachanwalt-familienrecht.md`](../testakten/megaprompts/fachanwalt-familienrecht.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

### Formatvorlagen (Markdown + ODT)

Sofort verwendbare Vorlagen (Times Roman 11pt, A4, mit Disclaimer und Feldern in [Klammern]). Markdown zum Lesen / Anpassen, ODT zum Bearbeiten in LibreOffice/Word.

| Vorlage | Markdown | ODT |
| --- | --- | --- |
| Scheidungsantrag Paragraf 133 Famfg | [`.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-familienrecht/scheidungsantrag-paragraf-133-famfg.md) | [`.odt`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/fachanwalt-familienrecht/scheidungsantrag-paragraf-133-famfg.odt) |

*Experimentelle KI-Vorlagen — keine Haftung. Vor Verwendung im Mandat anwaltlich prüfen und an konkreten Fall anpassen.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-familienrecht`) | [`fachanwalt-familienrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-familienrecht.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

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


Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-familienrecht-orientierung` | Orientierung im Familienrecht — FAO-Voraussetzungen Fachanwaltsbezeichnung Normen typische Mandate Fristen Quellenprüfung. Plugin für schnelle Verortung. Tiefe Bearbeitung erfordert weiterhin Fachanwal… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 125 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abaenderung-versorgungsausgleich-51-versausglg` | Abänderung Versorgungsausgleich § 51 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Que... |
| `aerztliche-versorgungswerke-berufsstaendische-versorgung` | Ärztliche Versorgungswerke berufsständische Versorgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Ärztliche Versorgungswerke berufsständische Versorgung: prüft die einschlägigen Voraussetzungen, Dokumente... |
| `allgemein-familienrecht-normenradar` | Fachanwalt Familienrecht — Allgemein im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitspro... |
| `anpassung-wegen-invaliditaet-oder-besonderer-haerte` | Anpassung wegen Invalidität oder besonderer Härte: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-... |
| `anpassung-wegen-unterhalt-33-ff-versausglg` | Anpassung wegen Unterhalt §§ 33 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellen... |
| `anrechte-dokumentenintake` | Anrechte Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `anwartschaft-dynamisch-statisch-bewertung` | Anwartschaft dynamisch statisch Bewertung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: V... |
| `ausgleich-nach-der-scheidung-20-ff-versausglg` | Ausgleich nach der Scheidung §§ 20 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Q... |
| `auslaendische-anrechte-versorgungsausgleich` | Ausländische Anrechte Versorgungsausgleich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker:... |
| `ausschluss-grobe-unbilligkeit-27-versausglg` | Ausschluss grobe Unbilligkeit § 27 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellen... |
| `beamtenrechtliche-kuerzung-und-rueckausnahme` | Beamtenrechtliche Kürzung und Rückausnahme: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker:... |
| `beamtenversorgung-versorgungsausgleich` | Beamtenversorgung Versorgungsausgleich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAus... |
| `beschwerde-gegen-va-beschluss-famfg` | Beschwerde gegen VA-Beschluss FamFG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, F... |
| `betriebliche-altersversorgung-direktzusage-pensionskasse-fonds` | Betriebliche Altersversorgung Direktzusage Pensionskasse Fonds: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Betriebliche Altersversorgung Direktzusage Pensionskasse Fonds: prüft die einschlägigen Voraussetz... |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Familienrecht: sortiert Heiratsurkunde, Scheidungsantrag, Vermögensauseinandersetzung, prüft Datum, Absender, Frist und Beweiswert (Einkommensnachweise, Vermögensauskunft); markiert Lücken; berücksichtigt... |
| `duesseldorfer-abschlussprodukt-und-uebergabe` | Duesseldorfer: Abschlussprodukt und Übergabe im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Ar... |
| `duesseldorfer-tabelle-unterhalt` | Fachanwalt Familienrecht Duesseldorfer Tabelle Unterhalt: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Familienrecht Duesseldorfer Tabelle Unterhalt: ordnet Normen... |
| `ehegattenrecht-internationales-art-13-egbgb` | Ehegattenrecht Internationales Art 13 Egbgb: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `ehevertrag-red-team-und-qualitaetskontrolle` | Ehevertrag: Red-Team und Qualitätskontrolle im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arb... |
| `ehevertrag-scheidungsfolgenkontrolle` | Ehevertrag und Scheidungsfolgenkontrolle: Wirksamkeit, Ausübungskontrolle, Kernbereichslehre und Verhandlungsdokumentation: Normank... |
| `ehevertrag-sittenwidrigkeit-bgh-xii-zr-129-04` | Ehevertrag Sittenwidrigkeit BGH Xii Zr 129 04: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `ehezeit-bestimmen-3-versausglg` | Ehezeit bestimmen § 3 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, FamFG S... |
| `eingetragene-mandantenkommunikation-entscheidungsvorlage` | Eingetragene: Mandantenkommunikation und Entscheidungsvorlage im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und di... |
| `einstieg-routing` | Anwalts-Dashboard Fachanwalt Familienrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt... |
| `ergaenzend-sonderfall-edge-case` | Ergaenzend: Sonderfall und Edge-Case-Prüfung im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Ar... |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweiche... |
| `erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nu... |
| `eu-auslandsrenten-und-scheidung` | EU-Auslandsrenten und Scheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, FamFG Sch... |
| `excel-pruefmatrix-anrechte` | Excel-Prüfmatrix Anrechte: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbu... |
| `externe-teilung-14-versausglg` | Externe Teilung § 14 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, FamFG Sch... |
| `famfg-quellenkarte` | Famfg Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `familiengericht-verhandlung-vergleich-und-eskalation` | Familiengericht: Verhandlung, Vergleich und Eskalation im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nu... |
| `familienrecht-tatbestand-beweis-und-belege` | Familienrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und d... |
| `famr-einfuehrung-themen` | Familienrecht einfuehrend: Ehe, Scheidung, Zugewinn, Versorgungsausgleich, Unterhalt (Trennungs-, Ehegatten-, Kindes-, Volljaehrigen-), Sorgerecht, Umgangsrecht, Vaterschaft, Adoption: Familienrecht einfuehrend: Ehe, Scheidung, Zugewinn,... |
| `famr-kindeswohlgefaehrdung-eilantrag-spezial` | Spezialfall Kindeswohlgefaehrdung und Eilantrag: § 1666 BGB, Anordnungen Familiengericht, einstweilige Anordnung § 49 FamFG, Inobhutnahme Jugendamt § 42 SGB VIII: Spezialfall Kindeswohlgefaehrdung und Eilantrag: § 1666 BGB, Anordnungen F... |
| `famr-mandantenaufnahme-spezial` | Mandantenaufnahme im Familienrecht: emotionale Lage, Eilbedarf (Gewaltschutz, Kindeswohlgefaehrdung, Wegnahme Kind), Vertraulichkeit Familienangehoerige, Verfahrenskostenhilfe: Mandantenaufnahme im Familienrecht: emotionale Lage, Eilbeda... |
| `famr-regenbogenfamilien-recht-spezial` | Spezialfall Regenbogenfamilien: rechtliche Elternschaft nach BGH, Stiefkindadoption, Co-Mutter-Anerkennung, Reform des Abstammungsrechts (Entwurf 2024 ff.), Sorgerecht bei Trennung: Spezialfall Regenbogenfamilien: rechtliche Elternschaft... |
| `famr-trennungsfolgen-workflow` | Trennungsfolgen: Unterhalt (Trennung, Kind), Hausrat, Wohnungszuweisung, Sorgerecht, Umgang, Versorgungsausgleich-Vorab: Prüfraster und... |
| `famr-trennungsjahr-praxis` | Trennungsjahr in der Praxis § 1565 BGB: Voraussetzungen, Beleg, Trennung innerhalb der Ehewohnung, Ausnahmen Haertefall: Praxistipps für... |
| `famr-vermoegensauseinandersetzung-workflow` | Vermögensauseinandersetzung im Scheidungsfall: Zugewinnausgleich Anfangs- und Endvermoegen, Auskunftsanspruch § 1379 BGB, Bewertungsstichtag, gemeinsame Konten und Immobilien: Vermögensauseinandersetzung im Scheidungsfall: Zugewinnausg... |
| `famr-versorgungsausgleich-spezial` | Spezialfall Versorgungsausgleich: VersAusglG, Anrechte Berechnung pro Versorgungstraeger, externe Teilung, interne Teilung, Anpassung wegen Unterhaltszahlung: Spezialfall Versorgungsausgleich: VersAusglG, Anrechte Berechnung pro Versorgu... |
| `fehlerhafte-auskunft-versorgungstraeger` | Fehlerhafte Auskunft Versorgungsträger: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAus... |
| `fragebogen-versorgungsausgleich-ausfuellen` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Fragebogen Versorgungsausgleich ausfüllen: zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Fragebogen Versorgungsausgleich ausfüllen. |
| `fristen-behoerden-gericht-und-registerweg` | Fristen: Behörden-, Gerichts- oder Registerweg im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem... |
| `geringfuegigkeit-18-versausglg` | Geringfügigkeit § 18 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, FamFG Sch... |
| `gesetzliche-rentenversicherung-entgeltpunkte` | Gesetzliche Rentenversicherung Entgeltpunkte: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenan... |
| `gewaltschutz-und-umgang-schnittstelle` | Gewaltschutz und Umgang: Schutzanordnung, Näherungsverbot, Umgangsausschluss, begleiteter Umgang und Beweisführung: Normanker: GewSchG; BGB... |
| `grundprinzip-versorgungsausgleich-halbteilung-1-versausglg` | Grundprinzip Versorgungsausgleich Halbteilung § 1 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Grundprinzip Versorgungsausgleich Halbteilung § 1 VersAusglG: prüft die einschlägigen Voraussetzunge... |
| `interne-teilung-10-versausglg` | Interne Teilung § 10 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, FamFG Sch... |
| `kanzlei-fristennotiz-und-naechster-schritt` | Kanzlei: Fristennotiz und nächster Schritt im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbe... |
| `kapitalwert-korrespondierender-kapitalwert-pruefen` | Kapitalwert korrespondierender Kapitalwert prüfen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-... |
| `kindesunterhalt-mindestsatz-paragraf-1612a-bgb` | Kindesunterhalt Mindestsatz Paragraf 1612a BGB: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `kindeswohl-hochkonflikt-wechselmodell` | Hochkonflikt und Wechselmodell: Kindeswohl, Bindungstoleranz, Kontinuität, Anhörung, Verfahrensbeistand und Beweis: Normanker: BGB §§ 1626... |
| `kindeswohlgefaehrdung-eilantrag` | Kindeswohlgefaehrdung nach § 1666 BGB: Eilantrag auf Sorgerechtsentzug oder Schutzanordnung stellen oder dagegen verteidigen: Norme... |
| `kindeswohlpruefung-paragraf-1697a-bgb-bgh-xii-zb-186-15` | Kindeswohlpruefung Paragraf 1697a BGB BGH Xii Zb 186 15: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `kirchliche-zusatzversorgung` | Kirchliche Zusatzversorgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, FamFG Scheidungsv... |
| `kosten-versorgungstraeger-teilungskosten` | Kosten Versorgungsträger Teilungskosten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersA... |
| `kurze-ehezeit-3-abs-3-versausglg` | Kurze Ehezeit § 3 Abs 3 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, Fam... |
| `lebenspartnerschaft-beweislast-und-darlegungslast` | Lebenspartnerschaft: Beweislast, Darlegungslast und Substantiierung im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse... |
| `lebensversicherung-abgrenzung-zugewinn-va` | Lebensversicherung Abgrenzung Zugewinn VA: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: V... |
| `literatur-schriftsatz-brief-und-memo-bausteine` | Literatur: Schriftsatz-, Brief- und Memo-Bausteine im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzba... |
| `mandantenblatt-versorgungsausgleich-in-einfacher-sprache` | Mandantenblatt Versorgungsausgleich in einfacher Sprache: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Mandantenblatt Versorgungsausgleich in einfacher Sprache: prüft die einschlägigen Voraussetzungen, Dokum... |
| `mandantenkommunikation-rentenfolgen` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Mandantenkommunikation Rentenfolgen: zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Mandantenkommunikation Rentenfolgen. |
| `mandat-triage-familienrecht` | Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgungsausgleich: Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn... |
| `mandate-risikoampel-und-gegenargumente` | Mandate: Risikoampel, Gegenargumente und Verteidigungslinien im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und dir... |
| `mediation-156-famfg-cochemer` | Familienrechtliche Mediation nach § 156 FamFG und Cochemer Modell: Vermittlungsverfahren § 165 FamFG bei Umgangsverweigerung, ADR-Pfade (Familienmediation DGFM, Familiengerichts-Mediation § 278a ZPO analog, Cochemer Praxis), Hochkonflikt... |
| `nachtraegliche-auskunft-und-vollstreckung` | Nachträgliche Auskunft und Vollstreckung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: Ver... |
| `nicht-ausgleichsreife-anrechte-19-versausglg` | Nicht ausgleichsreife Anrechte § 19 VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quell... |
| `normen-dokumentenmatrix-und-lueckenliste` | Normen: Dokumentenmatrix, Lückenliste und Nachforderung im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt n... |
| `notarielle-scheidungsfolgenvereinbarung-va` | Notarielle Scheidungsfolgenvereinbarung VA: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker:... |
| `oeffentlicher-dienst-zusatzversorgung-vbl` | Öffentlicher Dienst Zusatzversorgung VBL: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: Ver... |
| `orientierung-fristen-form-und-zustaendigkeit` | Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt... |
| `orientierung-mandat-fachanwaltschaft` | Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB überblicken: Normen:... |
| `output-waehlen` | Output-Wahl für Fachanwalt Familienrecht: stimmt Adressat (Ehegatten, Kinder, Jugendamt), Frist (Trennungsjahr § 1565 BGB) und Form auf den Zweck ab — typische Outputs: Scheidungsantrag, Unterhaltsklage, Umgangsregelung. |
| `pensionszusage-bewertung-insolvenzrisiko` | Pensionszusage Bewertung Insolvenzrisiko: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: Ver... |
| `private-rentenversicherung-kapitalwahlrecht` | Private Rentenversicherung Kapitalwahlrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanke... |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Familienrecht: prüft Normen (BGB §§ 1297 ff., FamFG, VersAusglG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Familiengericht (AG) und Quellenhygiene nach references/quellenhyg... |
| `red-team-va-beschluss-rechnerisch` | Red-Team VA-Beschluss rechnerisch: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, FamFG... |
| `rentenluecke-nach-scheidung-handlungsoptionen` | Rentenlücke nach Scheidung Handlungsoptionen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenan... |
| `rentnerfall-beide-beziehen-rente` | Rentnerfall beide beziehen Rente: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, FamFG S... |
| `riester-ruerup-versorgungsausgleich` | Riester Rürup Versorgungsausgleich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, Fam... |
| `sbgg-personenstandswechsel-folgen` | Fachanwalt Familienrecht Sbgg Personenstandswechsel Folgen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Familienrecht Sbgg Personenstandswechsel Folgen: ordnet No... |
| `scheidung-zahlen-schwellen-und-berechnung` | Scheidung: Zahlen, Schwellenwerte und Berechnung im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbare... |
| `scheidungsantrag-stellen` | Fachanwalt Familienrecht Scheidungsantrag Stellen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Familienrecht Scheidungsantrag Stellen: ordnet Normen, Nutzerangabe... |
| `scheidungsverbund-va-fristenplan` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Scheidungsverbund VA Fristenplan: zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Scheidungsverbund VA Fristenplan. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Scheidungsantrag, Unterhaltsklage, Sorgerechtsantrag, VA-Beschwerde: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau: Substantiierter Schri... |
| `soldatenversorgung-bundeswehr-schnittstelle` | Soldatenversorgung Bundeswehr Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanke... |
| `sorge-compliance-dokumentation-und-akte` | Sorge: Compliance-Dokumentation und Aktenvermerk im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbare... |
| `sorgerecht-elterliche-verantwortung-bgh-xii-zb-72-19` | Sorgerecht Elterliche Verantwortung BGH Xii Zb 72 19: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `steuerliche-folgen-externe-teilung` | Steuerliche Folgen externe Teilung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, Fam... |
| `tod-eines-ehegatten-anpassung-37-ff-versausglg` | Tod eines Ehegatten Anpassung §§ 37 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-... |
| `tod-nach-rechtskraft-vor-umsetzung` | Tod nach Rechtskraft vor Umsetzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, Fam... |
| `trennungsunterhalt-bedarfspruefung-bgh-xii-zr-181-22` | Trennungsunterhalt Bedarfspruefung BGH Xii Zr 181 22: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `umgang-mehrparteien-konflikt-und-interessen` | Umgang: Mehrparteienkonflikt und Interessenmatrix im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbar... |
| `umgangsrecht-grosseltern-paragraf-1685-bgb-bverfg-1-bvr-1178-14` | Umgangsrecht Grosseltern Paragraf 1685 BGB BVerfG 1 Bvr 1178 14: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `umgangsregelung-mustervorlagen` | Umgangsregelungen nach §§ 1684 und 1685 BGB formulieren: Regelmäßiger Umgang oder Streit um Umgangsrecht soll durch Vereinbarung oder Beschluss gelöst werden: Umgangsregelungen nach §§ 1684 und 1685 BGB formulieren: Regelmäßiger Umgang o... |
| `unterhalt-duesseldorfer-tabelle` | Kindes- und Ehegattenunterhalt nach Duesseldorfer Tabelle berechnen: Praktische Berechnungsaufgabe mit konkreten Einkommensdaten: Kindes- und Ehegattenunterhalt nach Duesseldorfer Tabelle berechnen: Praktische Berechnungsaufgabe mit konk... |
| `unterhalt-internationaler-bezug-und-schnittstellen` | Unterhalt: Internationaler Bezug und Schnittstellen im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzb... |
| `unterhalt-selbstaendige-einkommensaufklaerung` | Unterhalt bei Selbstständigen: Einkommensermittlung, Privatentnahmen, Steuerbescheid, BWA, Wohnvorteil und fiktives Einkommen: N... |
| `unterhaltsberechnung` | Kindes- und Ehegattenunterhalt vollständig berechnen: Mandant trennt sich oder wurde getrennt und will Unterhaltshoehe festlegen: Kindes- und Ehegattenunterhalt vollständig berechnen: Mandant trennt sich oder wurde getrennt und will Unte... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Familienrecht: trennt fehlende Tatsachen von fehlenden Belegen (Heiratsurkunde, Scheidungsantrag, Vermögensauseinandersetzung), nennt pro Lücke Beweisthema, Beschaffungsweg (Familiengericht (A... |
| `unternehmerversorgung-gesellschafter-geschaeftsfuehrer` | Unternehmerversorgung Gesellschafter-Geschäftsführer: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: ... |
| `va-bei-lebenspartnerschaft` | VA bei Lebenspartnerschaft: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG, FamFG Scheidungsver... |
| `va-im-internationalen-scheidungsfall` | VA im internationalen Scheidungsfall: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusglG,... |
| `va-und-insolvenz-eines-versorgungstraegers` | VA und Insolvenz eines Versorgungsträgers: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: V... |
| `vaterschaftsanfechtung-frist-paragraf-1600b-bgb-bverfg` | Vaterschaftsanfechtung Frist Paragraf 1600b BGB mit BVerfG 1 BvR 2007/10. |
| `verbundabtrennung-versorgungsausgleich` | Verbundabtrennung Versorgungsausgleich: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAus... |
| `vereinbarung-ueber-versorgungsausgleich-6-ff-versausglg` | Vereinbarung über Versorgungsausgleich §§ 6 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Vereinbarung über Versorgungsausgleich §§ 6 ff VersAusglG: prüft die einschlägigen Voraussetzungen, Dok... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Familien-, Kindschafts- und Versorgungsausgleichsrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich): V... |
| `versorgungsausgleich` | Versorgungsausgleich im Scheidungsverbund durchführen: Rentenanrechte aus Ehe aufteilen: Normen: VersAusglG (seit 2009), §§ 1 und 10 VersAusglG (Hin- und Herrechnung),... |
| `versorgungsausgleich-kaltstart` | Versorgungsausgleich Kaltstart: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `versorgungsausgleich-rentenmix-inland-ausland` | Versorgungsausgleich bei gesetzlicher Rente, Beamtenversorgung, Versorgungswerk, Ausland und privaten Anrechten: Normanker: VersAusglG; FamFG;... |
| `versorgungsausgleich-totalrevision-und-tod` | Prüft Abänderungsverfahren nach § 51 VersAusglG, Besitzschutz in der gesetzlichen Rentenversicherung, Tod eines Ehegatten und die Grenze zwischen Änderungsgrund und Fehlerkorrektur: Prüft Abänderungsverfahren nach § 51 VersAusglG, Besitz... |
| `versorgungsausgleich-und-versorgungsausgleichskasse` | Versorgungsausgleich und Versorgungsausgleichskasse: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: N... |
| `versorgungsausgleich-verstorbener-paragraf-31-versausglg` | Versorgungsausgleich Verstorbener Paragraf 31 Versausglg: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `versorgungstraeger-antwort-pruefen` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Versorgungsträger Antwort prüfen: zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Versorgungsträger Antwort prüfen. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `zielversorgung-waehlen-externe-teilung` | Zielversorgung wählen externe Teilung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen: Norm-/Quellenanker: VersAusgl... |
| `zugewinn-formular-portal-und-einreichung` | Zugewinn: Formular, Portal und Einreichungslogik im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbare... |
| `zugewinnausgleich-anfangsvermoegen` | Zugewinnausgleich Anfangsvermoegen: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `zugewinnausgleich-berechnen` | Zugewinnausgleich nach §§ 1372-1390 BGB berechnen: Trennung oder Scheidung erfordert Aufstellung von Anfangs- und Endvermögen: Nor... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
