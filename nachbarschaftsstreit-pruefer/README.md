# Nachbarschaftsstreit-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`nachbarschaftsstreit-pruefer`) | [`nachbarschaftsstreit-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nachbarschaftsstreit-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Nachbarschaftsstreit Rosengartenstraße** (`nachbarschaftsstreit-horrorfall-rosengarten`) | [Gesamt-PDF lesen](../testakten/nachbarschaftsstreit-horrorfall-rosengarten/gesamt-pdf/nachbarschaftsstreit-horrorfall-rosengarten_gesamt.pdf) | [`testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für Nachbarrecht und eskalierte Grundstückskonflikte: Überbau, Überhang, Äste und Wurzeln, Grenzbäume, Einfriedung, Zaun, Mauer, Hecke, Immissionen, Vertiefung, drohender Einsturz, Notweg, Hammerschlags- und Leiterrecht, Beweissicherung, Aufforderungsschreiben, einstweilige Verfügung, Klage und Vergleich.

**Keine Rechtsberatung.** Das Plugin erzeugt strukturierte Prüfungen, Entwürfe und Workflows zur anwaltlichen Kontrolle. Landesnachbarrecht, Baumschutzsatzungen, Bebauungspläne und örtliche Satzungen müssen im konkreten Fall geprüft werden.

## Direkt-Download

| Plugin | Direkt-Download |
|---|---|
| Nachbarschaftsstreit-Prüfer (`nachbarschaftsstreit-pruefer`) | [nachbarschaftsstreit-pruefer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nachbarschaftsstreit-pruefer.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Nachbarschaftsstreit Rosengartenstraße** ([`testakten/nachbarschaftsstreit-horrorfall-rosengarten/`](../testakten/nachbarschaftsstreit-horrorfall-rosengarten/)).

Direkt-Download als ZIP: [testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Start

```
/nachbarschaftsstreit-pruefer:allgemein
```

Der Einstieg fragt in kurzer Zeit ab: Grundstücke, Grenze, Bundesland, Streitgegenstand, Gefahr, Beweislage, bisherige Schreiben, gewünschter Ton und Ziel. Danach routet er zu den Spezialskills.

## Skills (20)

| Skill | Zweck |
|---|---|
| `allgemein` | Schöner Einstieg, Fristen-/Gefahrenscan, Routing und Arbeitsplan |
| `nachbarrecht-kaltstart-triage` | Erstaufnahme des Konflikts mit Bundesland, Grundstück, Beteiligten und Risiko |
| `akten-und-grundstuecksaufnahme` | Grundbuch, Liegenschaftskarte, Baulast, Dienstbarkeit, Fotos und Chronologie erfassen |
| `anspruchslandkarte-bgb-nachbarrecht` | Anspruchsgrundlagen nach BGB und Landesrecht sortieren |
| `ueberbau-pruefung` | Überbau nach §§ 912-916 BGB, Widerspruch, Duldung, Rente, Abkauf |
| `ueberhang-aeste-wurzeln` | Überhängende Äste, Wurzeln, Fristsetzung, Selbsthilfe nach § 910 BGB |
| `grenzbaum-und-grenzanlage` | Grenzbaum, Grenzsträucher und gemeinschaftliche Grenzanlagen §§ 921-923 BGB |
| `einfriedung-zaun-mauer-hecke` | Zaun, Mauer, Hecke, Kosten, Standort, Ortsüblichkeit und Landesrecht |
| `immissionen-laerm-geruch-rauch-licht` | Geräusche, Gerüche, Rauch, Licht, Erschütterungen, § 906 BGB |
| `vertiefung-baugrube-stuetzverlust` | Baugrube, Unterfangung, Stütze des Nachbargrundstücks, § 909 BGB |
| `drohender-einsturz-gefahranlage` | Gefährliche Anlagen und Einsturzrisiken, §§ 907, 908 BGB |
| `notweg-zufahrt-wegerecht` | Notweg, Zufahrt, Grunddienstbarkeit, Baulast, §§ 917, 918 BGB |
| `hammerschlags-und-leiterrecht` | Betreten des Nachbargrundstücks für Bau-/Instandhaltungsarbeiten nach Landesrecht |
| `landesnachbarrecht-router` | Bundesland auswählen und landesrechtliche Prüfmodule planen |
| `beweissicherung-ortstermin-fotos` | Ortstermin, Fotoplan, Messpunkte, Sachverständige und selbständiges Beweisverfahren |
| `selbsthilfe-und-eskalationsgrenzen` | Was darf man selbst tun, was nicht, und wann drohen Besitz-/Eigentumsverletzungen? |
| `aufforderungsschreiben-nachbar` | Sachliches, druckvolles Anspruchs- und Fristsetzungsschreiben |
| `einstweilige-verfuegung-und-klage` | Eilrechtsschutz, Unterlassung, Beseitigung, Duldung, Feststellung, Streitwert |
| `vergleich-mediation-nachbarschaftsfrieden` | Vergleich, Nutzungsregelung, Rückschnittplan, Kosten- und Zugangslösung |
| `horrorfall-aktenauswertung` | Große unordentliche Nachbarschaftsakte auswerten und in Arbeitsstränge zerlegen |

## Quellenstand

Stand: 05/2026. Kernnormen: BGB §§ 903, 906-923, 823, 862, 1004; Landesnachbarrechtsgesetze und kommunale Satzungen nach Bundesland/Gemeinde.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `akten-und-grundstuecksaufnahme` | Grundstücks- und Aktenaufnahme im Nachbarrechtsfall: Grundbuch, Flurkarte, Grenzzeichen, Baulasten, Dienstbarkeiten, Bauakte, Fotos, Chronologie, Besitzverhältnisse und Dokumentenlücken erfassen. |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Nachbarschaftsstreit-Prüfer. Fragt Grundstücke, Grenze, Bundesland, Streitgegenstand, Gefahr, Fristen, Beweise, bisherige Kommunikation und Ziel ab; schlägt passende Spezial-Skills zu Überb... |
| `anspruchslandkarte-bgb-nachbarrecht` | Anspruchslandkarte für Nachbarschaftsstreit erstellen: BGB-Eigentumsansprüche, Besitzschutz, Überbau, Überhang, Immissionen, Notweg, Landesnachbarrecht, öffentliches Recht, Beweise, Einwendungen und Rechtsfolge trennen. |
| `aufforderungsschreiben-nachbar` | Aufforderungsschreiben im Nachbarschaftsstreit erstellen: sachlich, beweisstark, fristgebunden, deeskalierend oder druckvoll; für Überbau, Überhang, Einfriedung, Immission, Notweg, Baugrube und Duldung. |
| `beweissicherung-ortstermin-fotos` | Beweissicherung im Nachbarrechtsfall planen: Ortstermin, Fotodokumentation, Messpunkte, Zeugen, Vermessung, Sachverständige, Lärm-/Geruchsprotokoll, Rissmonitoring und selbständiges Beweisverfahren. |
| `drohender-einsturz-gefahranlage` | Gefährliche Anlagen und drohenden Gebäudeeinsturz prüfen: §§ 907 und 908 BGB, Verkehrssicherung, Beseitigung/Sicherung, Ordnungsamt/Bauaufsicht, Eilrechtsschutz und Beweisplan. |
| `einfriedung-zaun-mauer-hecke` | Einfriedung, Zaun, Mauer, Sichtschutz und Hecke prüfen: Landesnachbarrecht, Ortsüblichkeit, Standort, Höhe, Kosten, Unterhaltung, Grenzabstand, Bauordnungsrecht, kommunale Satzungen und Schreiben. |
| `einstweilige-verfuegung-und-klage` | Gerichtliche Eskalation im Nachbarschaftsstreit prüfen: einstweilige Verfügung, Klage, Unterlassung, Beseitigung, Duldung, Feststellung, selbständiges Beweisverfahren, Zuständigkeit, Streitwert und Anträge. |
| `grenzbaum-und-grenzanlage` | Grenzbaum, Grenzstrauch und gemeinschaftliche Grenzanlagen prüfen: §§ 921-923 BGB, Früchte, Beseitigung, Unterhaltung, Kosten, Grenzzeichen, Eigentum und Beweise. |
| `hammerschlags-und-leiterrecht` | Hammerschlags- und Leiterrecht prüfen: vorübergehendes Betreten und Benutzen des Nachbargrundstücks für Bau-, Instandhaltungs- oder Reparaturarbeiten nach Landesnachbarrecht; Ankündigung, Schonung, Sicherheit, Entschädigung. |
| `horrorfall-aktenauswertung` | Große, unordentliche Nachbarschaftsstreit-Akten auswerten: viele Dokumente, Fotos, Chatverläufe, Bauamt, Baum, Überbau, Immissionen, Baugrube und Vergleichsversuche in Streitstränge, Beweise, Risiken und nächste Schritte zerlegen. |
| `immissionen-laerm-geruch-rauch-licht` | Nachbarliche Immissionen prüfen: Lärm, Geruch, Rauch, Grill, Kamin, Licht, Erschütterung, § 906 BGB, Wesentlichkeit, Ortsüblichkeit, Richtwerte, Duldung, Unterlassung, Ausgleich und Beweissicherung. |
| `landesnachbarrecht-router` | Bundesland-Router für Landesnachbarrecht: Einfriedung, Pflanzenabstände, Hammerschlagsrecht, Nachbarwand, Fenster/Licht, Ausschlussfristen, kommunale Satzungen und Recherchebedarf je Land identifizieren. |
| `nach-grenzbebauung-ueberhang-spezial` | Spezialfall Grenzbebauung und Ueberhang § 910 BGB / Landesrecht: Abstandsflaechen, Rueckschnitt, Vorrang des Naturschutzes. Pruefraster fuer Eigentuemer und Mieter. |
| `nach-laermimmissionen-spezial` | Spezialfall Laermimmissionen TA Laerm und LAI-Hinweise: Beurteilungspegel, Schutzgebiete, Spitzenpegel, Pruefraster zur Schadensersatz- und Unterlassungsklage. |
| `nach-mediation-vorrang-leitfaden` | Leitfaden Mediation und obligatorisches Gueteverfahren § 15a EGZPO: zustaendige Stellen, Verlauf, Vergleich. Pruefraster fuer Streitwert unter 750 Euro und Nachbarschaftsstreit. |
| `nach-nachbarrechtsuebersicht-bauleiter` | Bauleiter Uebersicht Nachbarrecht: BGB §§ 903 ff., Landesnachbarrechtsgesetze, BImSchG. Pruefraster Immissionen, Grenzbebauung, Einfriedung. Mustertext Aufforderungsschreiben. |
| `nachbarrecht-kaltstart-triage` | Erstaufnahme eines Nachbarrechtsfalls: Beteiligte, Grundstücke, Bundesland, Grenze, Streitgegenstand, Gefahr, Fristen, Beweise, bisherige Eskalation und Ziel klären; danach in die passenden Spezialskills routen. |
| `notweg-zufahrt-wegerecht` | Notweg, Zufahrt und Wegerecht prüfen: §§ 917 und 918 BGB, Grunddienstbarkeit, Baulast, tatsächliche Nutzung, willkürliche Absperrung, Notwegrente, Umfang, Richtung und gerichtliche Bestimmung. |
| `selbsthilfe-und-eskalationsgrenzen` | Selbsthilfe im Nachbarrecht prüfen: Rückschnitt, Betreten, Beseitigung, Besitzschutz, Sachbeschädigungsrisiko, Naturschutz, Fristsetzung, Verhältnismäßigkeit und sichere Eskalationsreihenfolge. |
| `spezial-aeste-risikoampel-und-gegenargumente` | Aeste: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-aufforderung-mandantenkommunikation-entscheidungsvorlage` | Aufforderung: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-beweise-red-team-und-qualitaetskontrolle` | Beweise: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-grenzbaum-schriftsatz-brief-und-memo-bausteine` | Grenzbaum: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-hammerschlagsrecht-formular-portal-und-einreichung` | Hammerschlagsrecht: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-hecke-zahlen-schwellen-und-berechnung` | Hecke: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-immissionen-compliance-dokumentation-und-akte` | Immissionen: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kaltstart-abschlussprodukt-und-uebergabe` | Kaltstart: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-klage-beweislast-und-darlegungslast` | Klage: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mauer-livequellen-und-rechtsprechungscheck` | Mauer: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-nachbarrecht-erstpruefung-und-mandatsziel` | Nachbarrecht: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-nachbarschaftsstreit-tatbestand-beweis-und-belege` | Nachbarschaftsstreit: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-notweg-internationaler-bezug-und-schnittstellen` | Notweg: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pruefer-fristennotiz-und-naechster-schritt` | Pruefer: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ueberbau-fristen-form-und-zustaendigkeit` | Ueberbau: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ueberhang-dokumentenmatrix-und-lueckenliste` | Ueberhang: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vergleich-sonderfall-und-edge-case` | Vergleich: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vertiefung-mehrparteien-konflikt-und-interessen` | Vertiefung: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-wurzeln-behoerden-gericht-und-registerweg` | Wurzeln: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zaun-verhandlung-vergleich-und-eskalation` | Zaun: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `ueberbau-pruefung` | Überbau nach §§ 912-916 BGB prüfen: Gebäude oder Gebäudeteil über Grenze, Vorsatz/grobe Fahrlässigkeit, Widerspruch, Duldungspflicht, Beseitigung, Überbaurente, Abkauf, Beweise und Schreiben. |
| `ueberhang-aeste-wurzeln` | Überhängende Äste, eindringende Wurzeln, Laub, Früchte und Verschattung prüfen: § 910 BGB, Beeinträchtigung, Fristsetzung, Selbsthilfe, Beseitigungsanspruch, Baumschutzsatzung, Naturschutz und Landesnachbarrecht. |
| `vergleich-mediation-nachbarschaftsfrieden` | Vergleich und Befriedung im Nachbarschaftsstreit entwerfen: Rückschnittplan, Bau-/Grenzregelung, Kostenquote, Betretensrechte, Lärmzeiten, Pflegepflichten, Vertragsstrafe, Dokumentation und Vollzug. |
| `vertiefung-baugrube-stuetzverlust` | Vertiefung und Baugrube nach § 909 BGB prüfen: Verlust der Bodenstütze, Unterfangung, Risse, Setzung, Sicherungsmaßnahmen, Baustopp, Beweise, Sachverständige und Eilrechtsschutz. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin nachbarschaftsstreit-pruefer: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin nachbarschaftsstreit-pruefer: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin nachbarschaftsstreit-pruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin nachbarschaftsstreit-pruefer: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin nachbarschaftsstreit-pruefer: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin nachbarschaftsstreit-pruefer: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin nachbarschaftsstreit-pruefer: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin nachbarschaftsstreit-pruefer: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin nachbarschaftsstreit-pruefer: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin nachbarschaftsstreit-pruefer: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
