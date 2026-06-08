# Fachanwalt Strafrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-strafrecht`) | [`fachanwalt-strafrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-strafrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BtM-Akte** (`betaeubungsmittelrecht-apotheke-substitution-festival`) | [Gesamt-PDF lesen](../testakten/betaeubungsmittelrecht-apotheke-substitution-festival/gesamt-pdf/betaeubungsmittelrecht-apotheke-substitution-festival_gesamt.pdf) | [`testakte-betaeubungsmittelrecht-apotheke-substitution-festival.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betaeubungsmittelrecht-apotheke-substitution-festival.zip) |
| **Grossbankrott und Zeugenstreit — Mehrere Deliktszweige, Pellbach Logistik & Spedition GmbH, LG Koeln** (`grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln`) | [Gesamt-PDF lesen](../testakten/grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln/gesamt-pdf/grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln_gesamt.pdf) | [`testakte-grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln.zip) |
| **Vertriebsbonus und staatsanwaltschaftlicher Honeypot** (`internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot`) | [Gesamt-PDF lesen](../testakten/internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot/gesamt-pdf/internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot_gesamt.pdf) | [`testakte-internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot.zip) |
| **Wirtschaftsstrafsache Bankert — U-Haft, Betrug, Steuerhinterziehung, LG Frankfurt** (`wirtschaftsstrafsache-uhaft-bankert-frankfurt`) | [Gesamt-PDF lesen](../testakten/wirtschaftsstrafsache-uhaft-bankert-frankfurt/gesamt-pdf/wirtschaftsstrafsache-uhaft-bankert-frankfurt_gesamt.pdf) | [`testakte-wirtschaftsstrafsache-uhaft-bankert-frankfurt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wirtschaftsstrafsache-uhaft-bankert-frankfurt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

## Was dieses Plugin im Strafprozess leistet

Dieses Plugin ist als Arbeitscockpit für Strafverteidigung gedacht: nicht nur für die große Strategie, sondern für die täglichen Schritte einer laufenden Strafakte. Es ordnet Eingänge, markiert Fristen, baut Aktenlog und Wiedervorlagen, steuert Akteneinsicht, U-Haft, Pflichtverteidigung, Hauptverhandlung, Antragslog, Mandanteninstruktionen, Rechtsmittel und Vollstreckungsnachlauf.

Der Kaltstart soll sofort praktisch werden: Was ist heute gefährlich, welche Frist läuft, welcher Schriftsatz oder Anruf muss raus, welche Aktenbestandteile fehlen, was darf der Mandant keinesfalls ohne Rücksprache tun? Danach schlägt das Plugin die passenden Strafprozess-Skills aus diesem Plugin vor und hält das Ergebnis als Checkliste, Matrix, Memo, Mandantenbrief oder Schriftsatzbaustein fest.

Neu aufgenommen ist ein vertiefter Prüfpfad für digitale Ermittlungsmaßnahmen: biometrischer Internetabgleich, KI-gestützte Trefferlisten, verfahrensübergreifende Analyseplattformen, Akteneinsicht in technische Protokolle, Löschung, Benachrichtigung, KI-VO-Konformität und Verwertungsangriffe. Der Skill behandelt solche Maßnahmen ausdrücklich als rechtsstandsabhängig: Entwurf, Inkrafttreten und aktueller Wortlaut sind vor jeder tragenden Aussage live zu prüfen.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `strafprozess-cockpit-taegliche-kanzleifuehrung` | Laufendes Verteidigungs-Cockpit mit Verfahrensstand, Fristen, Haftlage, Akteneinsicht, offenen Anträgen, Terminen und nächstem Schritt. |
| `strafprozess-aktenlog-fristen-und-wiedervorlagen` | Macht aus beA-/EGVP-Eingängen, Beschlüssen, Ladungen, Strafbefehlen, Urteilen und Nachlieferungen ein belastbares Fristen- und Aufgabenlog. |
| `strafprozess-haft-und-besuchsmanagement` | Organisiert U-Haft, Haftprüfung, Haftbeschwerde, Haftverschonung, Akteneinsicht, Besuch, Telefon, Familie, Arbeitgeber und Beschleunigungskontrolle. |
| `strafprozess-hv-tagesmappe-und-sitzungsplan` | Baut für jeden Sitzungstag eine Hauptverhandlungs-Tagesmappe mit Zeugenprogramm, Fragelisten, Einlassungsfenster, Antragsentwürfen und Nachbereitung. |
| `strafprozess-sitzungsprotokoll-und-revisionssicherung` | Sichert Protokollierung, Anträge, Belehrungen, Verständigung, letztes Wort und mögliche Revisionsrügen während und nach der Hauptverhandlung. |
| `fachanwalt-strafrecht-orientierung` | Orientierung im Strafrecht — FAO-Voraussetzungen Normen typische Mandate Notfristen Quellenprüfung. Plugin für schnelle Verortung. Strafverteidigung im Ermittlungsverfahren (Akteneinsicht § 147 StPO) H… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 47 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `adhaesionsverfahren-ermittlungsverfahren` | Adhaesionsverfahren Ermittlungsverfahren im Strafrecht: prüft konkret Red-Team Qualitygate im Plugin fachanwalt-strafrecht, Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten, Ermittlungsverfahren, Orientierung. |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Strafrecht: wählt den nächsten Spezial-Skill nach Engpass (Revision 1 Woche/1 Mon. § 341 StPO, Anklageschrift, Strafbefehl, Ermittlungsakte), dokumentiert Router-Entscheidung mit Begründung. |
| `aussagepsychologie-staatsanwaltschaft` | Aussagepsychologie Staatsanwaltschaft im Strafrecht: prüft konkret Verteidigerwerkzeug, Vernehmungsmethodik, Aussetzung nach § 221 StGB, Bandenbetrug § 263 Abs. |
| `chatcontrol-csam-einlassung-vorbereiten` | Chatcontrol Csam Einlassung Vorbereiten im Strafrecht: prüft konkret Chat-Control CSAM Anwaltsgeheimnis und § 53 StPO, Schriftliche Einlassung des Beschuldigten vorbereiten oder, Hauptverhandlung im Strafverfahren vorbereiten, Insolvenza... |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Strafrecht: sortiert Anklageschrift, Strafbefehl, Ermittlungsakte, prüft Datum, Absender, Frist und Beweiswert (Vernehmungsprotokolle, Spurenakte); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `einstieg-routing` | Einstieg, Triage und Routing für Fachanwalt Strafrecht: ordnet Rolle (Beschuldigter/Angeklagter, Staatsanwaltschaft, Verletzte/Nebenkläger), markiert Frist (Revision 1 Woche/1 Mon. § 341 StPO), wählt Norm (StGB, StPO, JGG) und Zuständigk... |
| `ergaenzt-fachanwalt-insolvenzantrag-red-team-korrektur` | Ergaenzt Fachanwalt Insolvenzantrag RED im Strafrecht: prüft konkret Ergaenzt, Fachanwalt, Insolvenzantrag, Kanzlei. |
| `fa-strafrecht-quellen-frist-next` | Rechtsquellen: Quellenprüfung; Fristennotiz und nächster Schritt: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `freiheitsstrafe-paragraf-57-stgb` | Freiheitsstrafe § 57 StGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `hauptverhandlung-quellenkarte` | Hauptverhandlung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `koerperverletzung-stgb-todesfolge` | Koerperverletzung Stgb Todesfolge im Strafrecht: prüft konkret Koerperverletzung nach § 223 StGB Grundtatbestand, Koerperverletzung mit Todesfolge nach § 227 StGB, Schnittstelle zwischen Insolvenzanfechtung Paragraphen 129, Kreditbetrug... |
| `mandat-triage-plaedoyer-vorbereitung` | Mandat Triage Plaedoyer Vorbereitung im Strafrecht: prüft konkret Strukturierte Eingangs-Abfrage für Strafmandate, Plaedoyer für Strafverteidigung vorbereiten und, Substantiierter Schriftsatzkern für Strafverfahren, Adhaesion. |
| `nebenklage-nebenstrafrecht-opfervertretung` | Nebenklage Nebenstrafrecht Opfervertretung im Strafrecht: prüft konkret Nebenklage, Nebenstrafrecht, Opfervertretung, Revision. |
| `notwehr-paragraf-32-stgb` | Notwehr § 32 StGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `orientierung` | Orientierung im Strafrecht: prüft konkret Orientierung im Strafrecht-Mandat und Fallrouting, Untersuchungshaft und Haftprüfung nach §§ 112 ff, Verständigung § 257c StPO und Taeter-Opfer-Ausgleich § 46a, Wahlverteidiger-Mandat im Strafrec... |
| `output-waehlen` | Output-Wahl für Fachanwalt Strafrecht: stimmt Adressat (Beschuldigter/Angeklagter, Staatsanwaltschaft, Verletzte/Nebenkläger), Frist (Revision 1 Woche/1 Mon. § 341 StPO) und Form auf den Zweck ab — typische Outputs: Akteneinsicht-Antrag,... |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Strafrecht: prüft Normen (StGB, StPO, JGG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Staatsanwaltschaft und Quellenhygiene nach references/quellenhygiene.md. |
| `raub-rechtsbeugung` | Spezial Raub Rechtsbeugung im Strafrecht: prüft konkret Raub nach § 249 StGB, Raub mit Todesfolge nach § 251 StGB, Rechtsbeugung nach Paragraph 339 StGB, Schuldnerbeguenstigung nach Paragraph 283d StGB. |
| `rauschgift-paragraf-29-btmg` | Rauschgift § 29 BtMG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `revisionsbegruendung-paragraf-344-stpo` | Revisionsbegruendung § 344 StPO: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `steuerstrafrecht-ao-akteneinsicht-auswerten` | Steuerstrafrecht AO Akteneinsicht Auswerten im Strafrecht: prüft konkret Selbstanzeige nach Paragraph 371 AO, Strukturierte Auswertung der Strafakte nach Akteneinsicht §, Erstgespraeach und Mandatsannahme im Strafrecht, Akteneinsicht § 1... |
| `stpo-strafrecht-strafverteidigung` | Stpo Strafrecht Strafverteidigung im Strafrecht: prüft konkret StPO, Strafrecht, Strafverteidigung, Zeugenbeistand. |
| `strafprozess-antragslog-beweisantraege` | Strafprozess Antragslog Beweisantraege im Strafrecht: prüft konkret Antragslog für die Hauptverhandlung, Verteidigung gegen automatisierten biometrischen, Tägliches Strafprozess-Cockpit für Verteidiger, Haft- und Besuchsmanagement für Un... |
| `strafprozess-instruktionen` | Strafprozess Instruktionen im Strafrecht: prüft konkret Mandantenkommunikation im Strafverfahren, Pflichtverteidigung operativ prüfen und durchsetzen, Sitzungsprotokoll und Revisionssicherung, Verhandlungslog für Kontakte mit Staatsanwal... |
| `strafr-dysfunk-befangenheitsantrag` | Strafr Dysfunk Befangenheitsantrag im Strafrecht: prüft konkret Befangenheitsantrag nach § 24 StPO zielgenau formulieren, § 137 Abs, Beweisantrag so begruenden dass er gegen den, Beweisantragsstrategie so aufbauen dass der. |
| `strafr-dysfunk-darlegungslast-empirie-nutzen` | Strafr Dysfunk Darlegungslast Empirie Nutzen im Strafrecht: prüft konkret Darlegungs- und Substantiierungslast für den, Empirische Datenlage zur Strafverteidigungspraxis als, Erklaerungsrecht § 257 Abs, Hinweis auf einen heilbaren Fehler... |
| `strafr-dysfunk-sitzungspolizei` | Strafr Dysfunk Sitzungspolizei im Strafrecht: prüft konkret Sitzungspolizei §§ 176 ff, Verschleppungsabsicht nach § 244 Abs, Erste Reaktion wenn Gericht oder Staatsanwaltschaft den, Wahlverteidigerausschluss nach § 138a StPO abwehren. |
| `strafr-haftpruefung` | Strafr Haftpruefung im Strafrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Haftpruefung und Haftbeschwerde §§ 117 ff, Chronologie und Belegmatrix im Plugin fachanwalt-strafrecht. |
| `strafr-vermoegensabschoepfung` | Strafr Vermoegensabschoepfung im Strafrecht: prüft konkret Spezialfall Vermoegensabschoepfung §§ 73 ff, Leitfaden Wirtschaftsstrafrecht, Strafverteidigung bei Vorwurf wegen Filmens von, Reaktion auf Anklage. |
| `strafrecht-aussagepsy-suggestion-tuechtigkeit` | Aussagepsy Suggestion Tuechtigkeit im Strafrecht: prüft konkret Suggestion und Falscherinnerung, Aussagetuechtigkeit als kognitiv-emotionale Faehigkeit zur, Falschgestaendnisse, BGH-Grundsaetze zur aussagepsychologischen Begutachtung. |
| `strafrecht-betrug-stgb-btmg-grundtatbestand` | Betrug Stgb Btmg Grundtatbestand im Strafrecht: prüft konkret Betrug § 263 StGB Grundtatbestand, BtMG-Grundtatbestand § 29 Abs, BtMG-Qualifikation § 29a BtMG, § 30 BtMG. |
| `strafrecht-computerbetrug-263a-design-designg` | Computerbetrug 263a Design Designg im Strafrecht: prüft konkret Computerbetrug § 263a StGB, Strafvorschriften des Designgesetzes Paragraph 51 DesignG, Erpresserischer Menschenraub § 239a StGB und Geiselnahme §, Faktische Geschaeftsfuehre... |
| `strafrecht-gmbh-verletzung-insiderhandel-wphg` | Gmbh Verletzung Insiderhandel Wphg im Strafrecht: prüft konkret Unterlassene Verlustanzeige nach Paragraph 84 GmbHG bei, Insiderhandel § 119 WpHG iVm Art, Insolvenzverschleppung nach Paragraph 15a InsO, Grenzbeschlagnahme bei IP-Verletzu... |
| `strafrecht-markenrecht-143a-marktmanipulation` | Markenrecht 143a Marktmanipulation im Strafrecht: prüft konkret Bandenmäßige Markenrechtsverletzung Paragraph 143a, Marktmanipulation § 120 WpHG iVm Art, Mietpreisueberhoehung § 5 WiStrG 1954, Minder schwerer Fall des Totschlags nach § 2... |
| `strafrecht-stgb-easy-social-media-amtsdelikte` | Stgb Easy Social Media Amtsdelikte im Strafrecht: prüft konkret Easy-Verteidigung gegen § 188 StGB, Beweis- und Kontextverteidigung bei § 188 StGB auf X, Facebook, Instagram. |
| `strafrecht-strafprozess-ermittlungsverfahren` | Strafprozess Ermittlungsverfahren im Strafrecht: prüft konkret Sofortmaßnahmen im Ermittlungsverfahren, Rechtsmittel- und Notfristencockpit im Strafverfahren, BtMG-Verteidigungspraxis, Verteidigung in Verfahren mit dem Tatkomplex haeusli... |
| `strafrecht-untreue-schaden` | Untreue Schaden im Strafrecht: prüft konkret Vermoegensschaden bei Paragraph 266 StGB Untreue, Verbandssanktionen Stand 06/2026, Akteneinsicht operativ steuern, Steuerhinterziehung nach Paragraph 370 AO. |
| `strafrecht-urheberrecht-urhg-108a-gewerblich` | Urheberrecht Urhg 108a Gewerblich im Strafrecht: prüft konkret Unerlaubte Eingriffe in verwandte Schutzrechte nach, Gewerbsmäßige unerlaubte Verwertung nach Paragraph 108a, Unerlaubte Eingriffe in technische Schutzmassnahmen und zur, Sex... |
| `strafzumessung-paragraf-46-stgb` | Strafzumessung § 46 StGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `subventionsbetrug-stgb-toetung-verlangen` | Subventionsbetrug Stgb Toetung Verlangen im Strafrecht: prüft konkret Subventionsbetrug § 264 StGB, Toetung auf Verlangen nach § 216 StGB, Totschlag nach § 212 StGB, Gewaesserverunreinigung nach Paragraph 324 StGB. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Strafrecht: trennt fehlende Tatsachen von fehlenden Belegen (Anklageschrift, Strafbefehl, Ermittlungsakte), nennt pro Lücke Beweisthema, Beschaffungsweg (Staatsanwaltschaft), Frist und Ersatzn... |
| `untreue-paragraf-266-stgb-bverfg-2-bvr-105-09` | Untreue Paragraf 266 StGB BVerfG 2 Bvr 105 09: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `vermoegensabschoepfung-paragraf-73-stgb` | Vermoegensabschoepfung § 73 StGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `vermoegensschaden-betrug-paragraf-263-stgb` | Vermoegensschaden Betrug § 263 StGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `versicherungsbetrug-stgb-vorenthalten` | Versicherungsbetrug Stgb Vorenthalten im Strafrecht: prüft konkret Versicherungsmissbrauch § 265 StGB, Vorenthalten und Veruntreuen von Arbeitsentgelt nach, Vorteilsannahme § 331 StGB und Vorteilsgewaehrung § 333 StGB, Strafvorschriften... |
| `verstaendigung-paragraf-257c-stpo-bverfg-2-bvr-2628-10` | Verstaendigung Paragraf 257c StPO BVerfG 2 Bvr 2628 10: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `verteidiger-aussage-paragraf-148-stpo` | Verteidiger Aussage § 148 StPO: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
