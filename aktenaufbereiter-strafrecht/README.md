# Aktenaufbereiter Strafrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`aktenaufbereiter-strafrecht`) | [`aktenaufbereiter-strafrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenaufbereiter-strafrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **EG Juwel Stuttgart — Sammelverfahren bandenmaessiger schwerer Raub, Koenigstrasse** (`sammelakte-bandentaeter-eg-juwel-stuttgart-koffer-raub`) | [Gesamt-PDF lesen](../testakten/sammelakte-bandentaeter-eg-juwel-stuttgart-koffer-raub/gesamt-pdf/sammelakte-bandentaeter-eg-juwel-stuttgart-koffer-raub_gesamt.pdf) | [`testakte-sammelakte-bandentaeter-eg-juwel-stuttgart-koffer-raub.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sammelakte-bandentaeter-eg-juwel-stuttgart-koffer-raub.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Aktenaufbereiter für die Strafverteidigung. Bringt große Strafakten in den Griff durch sechs Excel-fähige Übersichten — Aktenvorblatt; Personenverzeichnis; Tatkomplexe; Beziehungen; Chronologie; Fristen. Fortlaufend ergänzbar. Erkennt Lücken und Widersprüche. Kein Ersatz für Aktenlektüre.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Aktenaufbereiter Strafrecht (`aktenaufbereiter-strafrecht`, dieses Plugin) | [aktenaufbereiter-strafrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenaufbereiter-strafrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `aktenaufbereiter-strafrecht` | Strukturierte Aufbereitung strafrechtlicher Akten für die Verteidigung. Erzeugt sechs Übersichten — Aktenvorblatt mit Blattangaben; Personenverzeichnis mit Rolle und Erstnennung; Tatkomplex- und Vorwurfsverzeichnis … |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenaufbereiter-strafrecht` | Strafverteidiger erhaelt Strafakte nach § 147 StPO Akteneinsicht und will diese strukturiert aufbereiten. Wirtschaftsstrafverfahren BtM-Verfahren Vermögensdelikte komplexe Strafverfahren. Sechs Übersichten: Aktenvorblatt Personenverzeich... |
| `akteneinsicht-uebersicht` | Akteneinsicht systematisch auswerten: Aktenbestandteile (Haupt-, Sonder-, Beweismittelakte), Bandzaehlung, Aktenblattzahl je Band, fehlende Aktenstuecke, Verschluss-Sachen, Tonbaender/Datentraeger, polizeiliche Spurenakten. Fuehrt Pruef-... |
| `aktenvorblatt-erstellen` | Erstes Aktenvorblatt fuer eine Strafakte erstellen: Mandant, Vorwurf nach Anklageschrift oder Strafanzeige, Tatzeitraum, zustaendiges Gericht/Staatsanwaltschaft, Aktenzeichen, Verteidiger, U-Haft-Status, naechste Termine, Hauptrisiken. A... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Aktenaufbereiter Strafrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arb... |
| `anklageschrift-zerlegen` | Anklageschrift in arbeitsfaehige Bausteine zerlegen: Tatvorwurf je Anklagepunkt, vorgeworfene Norm, wesentliche Tatsachen, Beweismittel je Punkt, Liste der Beweismittel, Verteidigungsansatzpunkte je Punkt. Output Tabelle und kommentierte... |
| `aussageanalyse-aussagepsychologie` | Zeugenaussage mit aussagepsychologischen Realkennzeichen analysieren: logische Konsistenz, quantitative Detailfuelle, Detailverknuepfung, Selbstbelastung, ungewoehnliche Details, Nichtsteuerungsmerkmale. Hypothesentest Falschaussage. Sin... |
| `beweismittel-katalog` | Beweismittel-Katalog fuer die Verteidigung: Urkunden, Augenschein, Zeugen, Sachverstaendige, Beschuldigtenaussage, Spuren, Datentraeger, Telekommunikationsueberwachung, Observation. Beweisthema, Beweismittel, Fundstelle in der Akte, Bewe... |
| `beweisverwertungsverbote-pruefen` | Beweisverwertungsverbote pruefen: § 136a StPO (verbotene Vernehmungsmethoden), § 252 StPO (Aussageverweigerung Angehoeriger), § 100a/d StPO (TKUe ohne Voraussetzungen), Belehrungsfehler § 136 StPO, Zufallsfunde § 108 StPO, Kernbereich pr... |
| `beziehungsmatrix-personen-taten` | Beziehungen zwischen Personen und Tatkomplexen sichtbar machen: Wer hat wem etwas getan, wer war wann wo, wer sagt was zu welchem Tatkomplex. Matrix-Tabelle mit Tatkomplexen als Spalten und Personen als Zeilen. Markiert Beziehungstyp (Ta... |
| `chronologie-strafverfahren` | Chronologie aller Verfahrensschritte: Tatzeitpunkt, Anzeige, Vernehmungen, Durchsuchungen, Festnahme, U-Haft-Befehle, Anklage, Hauptverhandlungstermine, Urteile, Rechtsmittel. Datum, Zeit, Behoerde/Gericht, Art, Beleg in der Akte (Aktenb... |
| `fristenliste-strafverfahren` | Fristenliste fuer ein Strafverfahren: Einspruch gegen Strafbefehl § 410 StPO, Berufung § 314 StPO, Revision § 341 sowie § 345 StPO, Rechtsmittel § 311 StPO, Wiedereinsetzung § 44 StPO, Untersuchungshaft-Pruefung § 117 sowie § 121 StPO. D... |
| `kronzeugen-regelung-spezial` | Spezialfall Kronzeugenregelung § 46b StGB: Aufklaerungshilfe oder Verhinderung schwerer Straftaten, Voraussetzungen Konnex, Ausschluss von § 100a StPO Katalogtaten, Strafrahmenverschiebung. Pruefraster fuer Verteidigerstrategie und Verha... |
| `opferzeugen-besondere-faelle` | Opferzeugen bei Sexualdelikten, Kindern, Schutzschriftsachen behandeln: Nebenklage § 395 StPO, Verletztenrechte §§ 406d ff. StPO, audiovisuelle Vernehmung § 58a StPO, Zeugenbeistand § 68b StPO, Ausschluss des Beschuldigten § 247 StPO. Ve... |
| `personenverzeichnis-aufbau` | Personenverzeichnis fuer eine Strafakte systematisch aufbauen: Beschuldigte, Mitbeschuldigte, Zeugen, Geschaedigte, Sachverstaendige, Dolmetscher, Vertreter. Fuer jede Person Rolle, Aussagestatus, Adresse, Verteidiger, Verbindung zu Tatk... |
| `revision-rechtsfehler-katalog` | Revisionsschrift vorbereiten: § 344 StPO Revisionsantraege, § 337 StPO Rechtsfehler. Sachruege und Verfahrensruege. Typische Verfahrensruegen: § 244 Abs. 2 StPO (Aufklaerungsruege), § 261 StPO (Beweiswuerdigung), § 265 StPO (Hinweispflic... |
| `spezial-aktenaufbereiter-erstpruefung-und-mandatsziel` | Aktenaufbereiter: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-aktenlektuere-fristennotiz-und-naechster-schritt` | Aktenlektuere: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-aktenvorblatt-schriftsatz-brief-und-memo-bausteine` | Aktenvorblatt: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-beziehungen-zahlen-schwellen-und-berechnung` | Beziehungen: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-chronologie-compliance-dokumentation-und-akte` | Chronologie: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ergaenzbar-formular-portal-und-einreichung` | Ergaenzbar: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-erkennt-red-team-und-qualitaetskontrolle` | Erkennt: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ersatz-sonderfall-und-edge-case` | Ersatz: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-excel-dokumentenmatrix-und-lueckenliste` | Excel: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-faehige-risikoampel-und-gegenargumente` | Faehige: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fortlaufend-internationaler-bezug-und-schnittstellen` | Fortlaufend: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fristen-mehrparteien-konflikt-und-interessen` | Fristen: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-luecken-mandantenkommunikation-entscheidungsvorlage` | Luecken: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-personenverzeichnis-verhandlung-vergleich-und-eskalation` | Personenverzeichnis: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-sechs-fristen-form-und-zustaendigkeit` | Sechs: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-strafrecht-abschlussprodukt-und-uebergabe` | Strafrecht: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-strafverteidigung-tatbestand-beweis-und-belege` | Strafverteidigung: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-tatkomplexe-livequellen-und-rechtsprechungscheck` | Tatkomplexe: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-uebersichten-behoerden-gericht-und-registerweg` | Uebersichten: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-widersprueche-beweislast-und-darlegungslast` | Widersprueche: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `strafakte-quality-gate` | Quality-Gate fuer eine aufbereitete Strafakte: Vollstaendigkeit (alle Baende, Aktenblattzahl), Konsistenz (Personenverzeichnis gegen Anklageschrift), Suchbarkeit (OCR, Volltext), Sensibilitaet (verschluss-Sachen separat). Output Prueflis... |
| `strafakte-uebergabe-vorbereiten` | Strafakte fuer Uebergabe an Sozietaetskollegin, Wahlverteidiger oder Pflichtverteidiger sauber vorbereiten: Inhaltsverzeichnis, Personenverzeichnis, Tatkomplex-Liste, Chronologie, offene Fristen, naechste Termine. Output kompaktes Handov... |
| `strafbefehl-einspruchsstrategie` | Strafbefehl § 410 StPO: Einspruchsstrategie pruefen. 2-Wochen-Frist, vollstaendiger oder beschraenkter Einspruch (nur Rechtsfolgenausspruch), Folge: Hauptverhandlung. Pruefraster: Beweislage, Verschlechterungsverbot § 411 Abs. 4 StPO gre... |
| `strafzumessung-deutsches-strafrecht` | Strafzumessung § 46 StGB systematisch: Schuld, Strafmilderungs- und Strafschaerfungsgruende, § 46a StGB Taeter-Opfer-Ausgleich, § 46b StGB Aufklaerungshilfe, § 49 StGB besondere gesetzliche Milderungsgruende, Verhaeltnis Geld-/Freiheitss... |
| `tatkomplexe-uebersicht` | Tatkomplexe einer Strafakte gliedern: bei mehreren Taten oder Serienvorwurf jede Tat als eigenen Komplex mit Tatzeit, Tatort, Tathandlung, beteiligten Personen, Beweismitteln, Verfahrensstand. Fuer eine Anklageschrift werden die Anklagep... |
| `u-haft-fristenwacht` | U-Haft-Fristen ueberwachen: 6-Monats-Pruefung § 121 StPO durch das OLG, Haftpruefung § 117 StPO und Haftbeschwerde § 117 Abs. 1 StPO, Aussetzung gegen Auflagen § 116 StPO. Pruefraster: dringender Tatverdacht, Haftgrund, Verhaeltnismaessi... |
| `vermoegensabschoepfung-dritt-arrest` | Spezialfall Dritt-Arrest in der Vermoegensabschoepfung §§ 111e ff. StPO: Arrest gegen Konten Dritter (Ehepartner, Briefkasten-Gesellschaft), Glaubhaftmachung, Verhaeltnismaessigkeit, einstweilige Beschwerde § 304 StPO. Pruefraster und Sc... |
| `vermoegensabschoepfung-einziehung` | Vermoegensabschoepfung §§ 73 ff. StGB pruefen und angreifen: Brutto-Prinzip, erweiterte Einziehung § 73a StGB, Wertersatzeinziehung § 73c StGB, gutglaeubige Dritte § 73e StGB. Pruefraster, Antragsentwurf gegen Einziehung, Saemtliche Sich... |
| `verstaendigung-deal-strategie` | Verstaendigung im Strafverfahren § 257c StPO vorbereiten: Anregung an das Gericht, Ober- und Untergrenze Strafe, Gestaendnis-Inhalt, kein Geschaeft ueber Schuldspruch. Pruefraster: BGH 1 StR 70/13 und BVerfG 2 BvR 2628/10. Output Verstae... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin aktenaufbereiter-strafrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin aktenaufbereiter-strafrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin aktenaufbereiter-strafrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin aktenaufbereiter-strafrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin aktenaufbereiter-strafrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin aktenaufbereiter-strafrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin aktenaufbereiter-strafrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin aktenaufbereiter-strafrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin aktenaufbereiter-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin aktenaufbereiter-strafrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
