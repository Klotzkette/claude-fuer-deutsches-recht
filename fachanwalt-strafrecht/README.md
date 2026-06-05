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

Automatisch generierte Komplett-Liste aller 37 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `adhaesionsverfahren-ermittlungsverfahren` | Redteam Qualitygate, Fachanwalt Strafrecht Adhaesionsverfahren, Ermittlungsverfahren Vergleich Eskalation, Orientierung Fristen Form Und Zustaendigkeit: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlag... |
| `aussagepsychologie-staatsanwaltschaft` | Strafrecht Aussagepsychologie Staatsanwaltschaft Replik, Strafrecht Aussagepsychologie Vernehmungslehre Praxis, Strafrecht Aussetzung 221 Stgb, Strafrecht Bandenbetrug 263 Stgb: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `chatcontrol-csam-einlassung-vorbereiten` | Fachanwalt Strafrecht Chatcontrol Csam Anwaltsgeheimnis 53 Stpo, Fachanwalt Strafrecht Einlassung Vorbereiten, Fachanwalt Strafrecht Hauptverhandlung Vorbereiten, Fachanwalt Strafrecht Insolvenzantrag Staatsanwaltschaft: wählt den konkre... |
| `ergaenzt-fachanwalt-insolvenzantrag-red` | Ergaenzt Mandantenkommunikation Entscheidungsvorlage, Fachanwalt Erstpruefung Und Mandatsziel, Insolvenzantrag Red Team Und Qualitaetskontrolle, Kanzlei Sonderfall Und Edge Case: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `fa-strafrecht-quellen-frist-next` | Rechtsquellen: Quellenprüfung; Fristennotiz und nächster Schritt: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `fachanwalt-strafrecht-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `fachanwalt-strafrecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `fachanwalt-strafrecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `fachanwalt-strafrecht-orientierung` | Fachanwalt Strafrecht Orientierung, Fachanwalt Strafrecht Untersuchungshaft Haftpruefung, Fachanwalt Strafrecht Verstaendigung 257c Toa 46a, Fachanwalt Strafrecht Wahlverteidiger Mandat: wählt den konkreten Prüfpfad, trennt Frist, Zustän... |
| `fachanwalt-strafrecht-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `fachanwalt-strafrecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `fachanwalt-strafrecht-strafrecht-spezial-raub-rechtsbeugung` | Strafrecht Spezial Raub Stgb / Strafrecht Spezial Raub Todesfolge Stgb / Strafrecht Spezial Rechtsbeugung Stgb / Strafrecht Spezial Schuldnerbeguenstigung 283d Stgb / 6 weitere Module: führt durch diese fachlich verbundenen Arbeitsmodule... |
| `fachanwalt-strafrecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `hauptverhandlung-quellenkarte` | Hauptverhandlung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `koerperverletzung-stgb-todesfolge` | Strafrecht Koerperverletzung 223 Stgb Grund, Strafrecht Koerperverletzung Mit Todesfolge 227 Stgb, Strafrecht Konkursrechtliche Anfechtungsbezuege, Strafrecht Kreditbetrug 265b Stgb: wählt den konkreten Prüfpfad, trennt Frist, Zuständigk... |
| `mandat-triage-plaedoyer-vorbereitung` | Mandat Triage Strafrecht, Plaedoyer Vorbereitung Strafverteidigung, Schriftsatzkern Substantiierung, Adhaesion Formular Portal Und Einreichung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lie... |
| `nebenklage-nebenstrafrecht-opfervertretung` | Nebenklage Compliance Dokumentation Und Akte, Nebenstrafrecht Behörden Gericht Und Registerweg, Opfervertretung Mehrparteien Konflikt Und Interessen, Revision Zahlen Schwellen Und Berechnung: wählt den konkreten Prüfpfad, trennt Frist, Z... |
| `steuerstrafrecht-ao-akteneinsicht-auswerten` | Strafrecht Steuerstrafrecht 371 Ao Selbstanzeige, Akteneinsicht Strafrecht Auswerten, Erstgespraech Mandatsannahme, Fachanwalt Strafrecht Akteneinsicht Beantragen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rec... |
| `stpo-strafrecht-strafverteidigung` | Stpo Dokumentenmatrix Und Lueckenliste, Strafrecht Tatbestand Beweis Und Belege, Strafverteidigung Schriftsatz Brief Und Memo Bausteine, Zeugenbeistand Internationaler Bezug Und Schnittstellen: wählt den konkreten Prüfpfad, trennt Frist,... |
| `strafprozess-antragslog-beweisantraege` | Strafprozess Antragslog Beweisantraege Und Widerspruch, Strafprozess Biometrischer Internetabgleich 98d Stpo E, Strafprozess Cockpit Taegliche Kanzleifuehrung, Strafprozess Haft Und Besuchsmanagement: wählt den konkreten Prüfpfad, trennt... |
| `strafprozess-instruktionen` | Strafprozess Mandantenkommunikation Und Instruktionen, Strafprozess Pflichtverteidigung Beiordnung Und Wechsel, Strafprozess Sitzungsprotokoll Und Revisionssicherung, Strafprozess Verhandlungslog Sta Gericht Nebenklage: wählt den konkret... |
| `strafr-dysfunk-befangenheitsantrag` | Strafr Dysfunk Befangenheitsantrag Zielgenau, Strafr Dysfunk Beistandsleistung 137 Stpo, Strafr Dysfunk Beweisantrag Fundament, Strafr Dysfunk Beweisantragsstrategie: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `strafr-dysfunk-darlegungslast-empirie-nutzen` | Strafr Dysfunk Darlegungslast Umkehren, Strafr Dysfunk Empirie Nutzen, Strafr Dysfunk Erklaerungsrecht 257 Stpo, Strafr Dysfunk Hinweis Auf Heilbaren Fehler: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgru... |
| `strafr-dysfunk-sitzungspolizei` | Strafr Dysfunk Sitzungspolizei Ordnungsmittel, Strafr Dysfunk Verschleppungsabsicht Abgrenzen, Strafr Dysfunk Vorwurf Einordnen, Strafr Dysfunk Wahlverteidigerausschluss 138a: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Be... |
| `strafr-haftpruefung` | Allgemein, Strafr Haftpruefung Haftbeschwerde Workflow, Chronologie Und Belegmatrix, Fristen Und Risikoampel: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `strafr-vermoegensabschoepfung` | Strafr Vermoegensabschoepfung Spezial, Strafr Wirtschaftsstrafrecht Leitfaden, Strafrecht Polizeifilmerei 201 Stgb Kug Verteidigung, Strafrecht 188 Stgb Anklage Und Strafbefehl: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `strafrecht-aussagepsy-suggestion-tuechtigkeit` | Strafrecht Aussagepsy Suggestion Falscherinnerung, Strafrecht Aussagepsy Tuechtigkeit Bereitschaft, Strafrecht Aussagepsy Vernehmungsfehler Falschgestand, Strafrecht Aussagepsychologie Bgh Grundsaetze: wählt den konkreten Prüfpfad, trenn... |
| `strafrecht-betrug-stgb-btmg-grundtatbestand` | Strafrecht Betrug 263 Stgb Grundtatbestand, Strafrecht Btmg 29 Grundtatbestand, Strafrecht Btmg 29a Nicht Geringe Menge, Strafrecht Btmg 30 Handeltreiben: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundl... |
| `strafrecht-computerbetrug-263a-design-designg` | Strafrecht Computerbetrug 263a Stgb, Strafrecht Design Strafrecht 51 Designg, Strafrecht Erpresserischer Menschenraub 239a 239b Stgb, Strafrecht Faktische Geschaeftsfuehrer: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Bele... |
| `strafrecht-gmbh-verletzung-insiderhandel-wphg` | Strafrecht Gmbh Verletzung Anzeigepflicht 84 Gmbhg, Strafrecht Insiderhandel 119 Wphg, Strafrecht Insolvenzverschleppung 15a Inso, Strafrecht Ip Strafrecht Grenzbeschlagnahme: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Be... |
| `strafrecht-markenrecht-143a-marktmanipulation` | Strafrecht Markenrecht 143a Markeng Bandenmaessig, Strafrecht Marktmanipulation 120 Wphg, Strafrecht Mietwucher 5 Wistg, Strafrecht Minder Schwerer Fall 213 Stgb: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rech... |
| `strafrecht-stgb-easy-social-media-amtsdelikte` | Strafrecht 188 Stgb Easy Verteidigung, Strafrecht 188 Stgb Social Media Beweise, Strafrecht Amtsdelikte 340 Stgb Koerperverletzung Im Amt, Strafrecht Amtstraegerbestechung 332 334 Stgb: wählt den konkreten Prüfpfad, trennt Frist, Zuständ... |
| `strafrecht-strafprozess-ermittlungsverfahren` | Strafprozess Ermittlungsverfahren Sofortmassnahmen, Strafprozess Rechtsmittel Und Notfristencockpit, Strafrecht Btmg Strafverfahren Praxis, Strafrecht Haeusliche Gewalt Im Strafverfahren: wählt den konkreten Prüfpfad, trennt Frist, Zustä... |
| `strafrecht-untreue-schaden` | Strafrecht Untreue Schaden Und Bezifferbarkeit, Strafrecht Verbandssanktionengesetz Stand 2026, Strafprozess Akteneinsicht Nachlieferungen Und Sonderbaende, Strafrecht Steuerstrafrecht 370 Ao Steuerhinterziehung: wählt den konkreten Prüf... |
| `strafrecht-urheberrecht-urhg-108a-gewerblich` | Strafrecht Urheberrecht 108 Urhg Unerlaubte Eingriffe, Strafrecht Urheberrecht 108a Urhg Gewerblich, Strafrecht Urheberrecht 108b Urhg Tpm, Strafrecht Vergewaltigung 177 Stgb: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Be... |
| `subventionsbetrug-stgb-toetung-verlangen` | Strafrecht Subventionsbetrug 264 Stgb, Strafrecht Toetung Auf Verlangen 216 Stgb, Strafrecht Totschlag 212 Stgb, Strafrecht Umweltstrafrecht 324 Stgb Gewaesser: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechts... |
| `versicherungsbetrug-stgb-vorenthalten` | Strafrecht Versicherungsbetrug 265 Stgb, Strafrecht Vorenthalten Arbeitgeberanteile 266a Stgb, Strafrecht Vorteilsannahme Gewaehrung 331 333 Stgb, Strafrecht Waffg Strafvorschriften 51 52: wählt den konkreten Prüfpfad, trennt Frist, Zust... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
