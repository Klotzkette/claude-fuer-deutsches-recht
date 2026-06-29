# Nachbarschaftsstreit-Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Nachbarrecht und Nachbarschaftsstreit: Überbau, Überhang, Äste/Wurzeln, Grenzbaum, Zaun/Mauer/Hecke, Immissionen, Vertiefung, Notweg, Hammerschlagsrecht, Beweise, Aufforderung, Klage und Vergleich.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`nachbarschaftsstreit-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nachbarschaftsstreit-pruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nachbarschaftsstreit-pruefer-werkstatt.md" download><code>nachbarschaftsstreit-pruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nachbarschaftsstreit-pruefer-schnellstart.md" download><code>nachbarschaftsstreit-pruefer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip) (Nachbarschaftsstreit Rosengartenstraße); [`testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip) (Akte Wusterhagen: Mühlenstau, Chaussee und Aufopferung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Freistehendes Plugin für Nachbarrecht und eskalierte Grundstückskonflikte: Überbau, Überhang, Äste und Wurzeln, Grenzbäume, Einfriedung, Zaun, Mauer, Hecke, Immissionen, Vertiefung, drohender Einsturz, Notweg, Hammerschlags- und Leiterrecht, Beweissicherung, Aufforderungsschreiben, einstweilige Verfügung, Klage und Vergleich.

**Keine Rechtsberatung.** Das Plugin erzeugt strukturierte Prüfungen, Entwürfe und Workflows zur anwaltlichen Kontrolle. Landesnachbarrecht, Baumschutzsatzungen, Bebauungspläne und örtliche Satzungen müssen im konkreten Fall geprüft werden.

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

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aeste-risikoampel-und-gegenargumente` | Aeste: Risikoampel, Gegenargumente und Verteidigungslinien. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `akten-und-grundstuecksaufnahme` | Grundstücks- und Aktenaufnahme im Nachbarrechtsfall: Grundbuch, Flurkarte, Grenzzeichen, Baulasten, Dienstbarkeiten, Bauakte, Fotos, Chronologie, Besitzverhältnisse und Dokumentenlücken erfassen im Nachbarschaftsstreit Prüfer. |
| `anschluss-router` | Einstieg, Schnelltriage und Fallrouting im Nachbarschaftsstreit-Prüfer. Fragt Grundstücke, Grenze, Bundesland, Streitgegenstand, Gefahr, Fristen, Beweise, bisherige Kommunikation und Ziel ab; schlägt passende Fachmodule zu Überbau, Überh... |
| `anspruchslandkarte-bgb-aufforderungsschreiben` | Anspruchslandkarte für Nachbarschaftsstreit erstellen: BGB-Eigentumsansprüche, Besitzschutz, Überbau, Überhang, Immissionen, Notweg, Landesnachbarrecht, öffentliches Recht, Beweise, Einwendungen und Rechtsfolge trennen im Nachbarschaftss... |
| `aufforderung-beweise-red-grenzbaum` | Aufforderung: Mandantenkommunikation und Entscheidungsvorlage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `aufforderungsschreiben-nachbar` | Aufforderungsschreiben im Nachbarschaftsstreit erstellen: sachlich, beweisstark, fristgebunden, deeskalierend oder druckvoll; für Überbau, Überhang, Einfriedung, Immission, Notweg, Baugrube und Duldung im Nachbarschaftsstreit Prüfer. |
| `beweise-red-team-und-qualitaetskontrolle` | Beweise: Red-Team und Qualitätskontrolle. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `beweissicherung-ortstermin-fotos` | Beweissicherung im Nachbarrechtsfall planen: Ortstermin, Fotodokumentation, Messpunkte, Zeugen, Vermessung, Sachverständige, Lärm-/Geruchsprotokoll, Rissmonitoring und selbständiges Beweisverfahren im Nachbarschaftsstreit Prüfer. |
| `dokumente-intake` | Dokumentenintake für Nachbarschaftsstreit: sortiert Schiedsamtsprotokoll, Lärmaufzeichnung, Lichtbilder Grenzbau, prüft Datum, Absender, Frist und Beweiswert (Lärmprotokoll, Lichtbilder); markiert Lücken; berücksichtigt Mandatsgeheimnis... |
| `drohender-einsturz-einfriedung-zaun` | Gefährliche Anlagen und drohenden Gebäudeeinsturz prüfen: §§ 907 und 908 BGB, Verkehrssicherung, Beseitigung/Sicherung, Ordnungsamt/Bauaufsicht, Eilrechtsschutz und Beweisplan im Nachbarschaftsstreit Prüfer. |
| `einfriedung-zaun-mauer-hecke` | Einfriedung, Zaun, Mauer, Sichtschutz und Hecke prüfen: Landesnachbarrecht, Ortsüblichkeit, Standort, Höhe, Kosten, Unterhaltung, Grenzabstand, Bauordnungsrecht, kommunale Satzungen und Schreiben im Nachbarschaftsstreit Prüfer. |
| `einstieg-routing` | Einstieg, Triage und Routing für Nachbarschaftsstreit: ordnet Rolle (Mandant, Nachbar, Schiedsamt), markiert Frist (§ 906 II 2 BGB jährliche Berechnung), wählt Norm (BGB §§ 906/1004, Landesnachbarrechtsgesetze, BauO Länder) und Zuständig... |
| `einstweilige-verfuegung-und-klage` | Gerichtliche Eskalation im Nachbarschaftsstreit prüfen: einstweilige Verfügung, Klage, Unterlassung, Beseitigung, Duldung, Feststellung, selbständiges Beweisverfahren, Zuständigkeit, Streitwert und Anträge im Nachbarschaftsstreit Prüfer. |
| `fristennotiz-naechster-ueberbau-akten` | Prüfer: Fristennotiz und nächster Schritt. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `grenzbaum-grenzanlage-hammerschlags` | Grenzbaum, Grenzstrauch und gemeinschaftliche Grenzanlagen prüfen: §§ 921-923 BGB, Früchte, Beseitigung, Unterhaltung, Kosten, Grenzzeichen, Eigentum und Beweise im Nachbarschaftsstreit Prüfer. |
| `grenzbaum-schriftsatz-brief-und-memo-bausteine` | Grenzbaum: Schriftsatz-, Brief- und Memo-Bausteine. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `hammerschlags-und-leiterrecht` | Hammerschlags- und Leiterrecht prüfen: vorübergehendes Betreten und Benutzen des Nachbargrundstücks für Bau-, Instandhaltungs- oder Reparaturarbeiten nach Landesnachbarrecht; Ankündigung, Schonung, Sicherheit, Entschädigung im Nachbarsch... |
| `hammerschlagsrecht-hecke-immissionen` | Hammerschlagsrecht: Formular, Portal und Einreichungslogik. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `hecke-zahlen-schwellen-und-berechnung` | Hecke: Zahlen, Schwellenwerte und Berechnung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `horrorfall-aktenauswertung` | Große, unordentliche Nachbarschaftsstreit-Akten auswerten: viele Dokumente, Fotos, Chatverläufe, Bauamt, Baum, Überbau, Immissionen, Baugrube und Vergleichsversuche in Streitstränge, Beweise, Risiken und nächste Schritte zerlegen im Nach... |
| `immissionen-compliance-dokumentation-und-akte` | Immissionen: Compliance-Dokumentation und Aktenvermerk. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `immissionen-laerm-landesnachbarrecht` | Nachbarliche Immissionen prüfen: Lärm, Geruch, Rauch, Grill, Kamin, Licht, Erschütterung, § 906 BGB, Wesentlichkeit, Ortsüblichkeit, Richtwerte, Duldung, Unterlassung, Ausgleich und Beweissicherung im Nachbarschaftsstreit Prüfer. |
| `kaltstart-abschlussprodukt-und-uebergabe` | Kaltstart: Einstieg und Routing; Abschlussprodukt und Übergabe: klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad |
| `klage-beweislast-nachbarrecht` | Klage: Beweislast, Darlegungslast und Substantiierung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `laermimmissionen-mediation-vorrang` | Spezialfall Laermimmissionen TA Laerm und LAI-Hinweise: Beurteilungspegel, Schutzgebiete, Spitzenpegel, Prüfraster zur Schadensersatz- und Unterlassungsklage im Nachbarschaftsstreit Prüfer. |
| `landesnachbarrecht-router` | Bundesland-Router für Landesnachbarrecht: Einfriedung, Pflanzenabstände, Hammerschlagsrecht, Nachbarwand, Fenster/Licht, Ausschlussfristen, kommunale Satzungen und Recherchebedarf je Land identifizieren im Nachbarschaftsstreit Prüfer. |
| `mauer-quellenkarte` | Mauer Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `nach-grenzbebauung-ueberhang-spezial` | Spezialfall Grenzbebauung und Überhang § 910 BGB / Landesrecht: Abstandsflaechen, Rueckschnitt, Vorrang des Naturschutzes. Prüfraster für Eigentuemer und Mieter im Nachbarschaftsstreit Prüfer. |
| `nach-mediation-vorrang-leitfaden` | Leitfaden Mediation und obligatorisches Gueteverfahren § 15a EGZPO: zuständige Stellen, Verlauf, Vergleich. Prüfraster für Streitwert unter 750 Euro und Nachbarschaftsstreit im Nachbarschaftsstreit Prüfer. |
| `nach-nachbarrechtsuebersicht-bauleiter` | Bauleiter Uebersicht Nachbarrecht: BGB §§ 903 ff., Landesnachbarrechtsgesetze, BImSchG. Prüfraster Immissionen, Grenzbebauung, Einfriedung. Mustertext Aufforderungsschreiben im Nachbarschaftsstreit Prüfer. |
| `nachbarrecht-erstpruefung-und-mandatsziel` | Nachbarrecht: Erstprüfung, Rollenklärung und Mandatsziel. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `nachbarrecht-kaltstart-triage` | Erstaufnahme eines Nachbarrechtsfalls: Beteiligte, Grundstücke, Bundesland, Grenze, Streitgegenstand, Gefahr, Fristen, Beweise, bisherige Eskalation und Ziel klären; danach in die passenden Fachmodule routen. |
| `nachbarschaftsstreit-fristen-risiko-mandant` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Nachbarschaftsstreit Prüfer. |
| `nachbarschaftsstreit-tatbestand-beweis-und-belege` | Nachbarschaftsstreit: Tatbestandsmerkmale, Beweisfragen und Beleglage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `notweg-ueberhang-sonderfall-edge` | Notweg: Internationaler Bezug und Schnittstellen. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `notweg-zufahrt-selbsthilfe-eskalationsgrenzen` | Notweg, Zufahrt und Wegerecht prüfen: §§ 917 und 918 BGB, Grunddienstbarkeit, Baulast, tatsächliche Nutzung, willkürliche Absperrung, Notwegrente, Umfang, Richtung und gerichtliche Bestimmung im Nachbarschaftsstreit Prüfer. |
| `output-waehlen` | Output-Wahl für Nachbarschaftsstreit: stimmt Adressat (Mandant, Nachbar, Schiedsamt), Frist (§ 906 II 2 BGB jährliche Berechnung) und Form auf den Zweck ab — typische Outputs: Schiedsamtsantrag, Klage AG, Unterlassung/Beseitigung-Antrag. |
| `quellen-livecheck` | Quellen-Live-Check für Nachbarschaftsstreit: prüft Normen (BGB §§ 906/1004, Landesnachbarrechtsgesetze, BauO Länder) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Amtsgericht und Quellenhygiene nach references/q... |
| `selbsthilfe-und-eskalationsgrenzen` | Selbsthilfe im Nachbarrecht prüfen: Rückschnitt, Betreten, Beseitigung, Besitzschutz, Sachbeschädigungsrisiko, Naturschutz, Fristsetzung, Verhältnismäßigkeit und sichere Eskalationsreihenfolge im Nachbarschaftsstreit Prüfer. |
| `spezial-mauer-livequellen-und-rechtsprechungscheck` | Mauer: Livequellen- und Rechtsprechungscheck. |
| `spezial-pruefer-fristennotiz-und-naechster-schritt` | Pruefer: Fristennotiz und nächster Schritt. |
| `spezial-ueberhang-dokumentenmatrix-und-lueckenliste` | Ueberhang: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `ueberbau-fristen-form-und-zustaendigkeit` | Ueberbau: Fristen, Form, Zuständigkeit und Rechtsweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `ueberbau-ueberhang-aeste-mediation` | Überbau nach §§ 912-916 BGB prüfen: Gebäude oder Gebäudeteil über Grenze, Vorsatz/grobe Fahrlässigkeit, Widerspruch, Duldungspflicht, Beseitigung, Überbaurente, Abkauf, Beweise und Schreiben im Nachbarschaftsstreit Prüfer. |
| `ueberhang-aeste-wurzeln` | Überhängende Äste, eindringende Wurzeln, Laub, Früchte und Verschattung prüfen: § 910 BGB, Beeinträchtigung, Fristsetzung, Selbsthilfe, Beseitigungsanspruch, Baumschutzsatzung, Naturschutz und Landesnachbarrecht im Nachbarschaftsstreit P... |
| `ueberhang-dokumentenmatrix-und-lueckenliste` | Überhang: Dokumentenmatrix, Lückenliste und Nachforderung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Nachbarschaftsstreit: trennt fehlende Tatsachen von fehlenden Belegen (Schiedsamtsprotokoll, Lärmaufzeichnung, Lichtbilder Grenzbau), nennt pro Lücke Beweisthema, Beschaffungsweg (Amtsgericht), Frist und... |
| `vergleich-mediation-nachbarschaftsfrieden` | Vergleich und Befriedung im Nachbarschaftsstreit entwerfen: Rückschnittplan, Bau-/Grenzregelung, Kostenquote, Betretensrechte, Lärmzeiten, Pflegepflichten, Vertragsstrafe, Dokumentation und Vollzug im Nachbarschaftsstreit Prüfer. |
| `vergleich-sonderfall-und-edge-case` | Vergleich: Sonderfall und Edge-Case-Prüfung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `vertiefung-baugrube-stuetzverlust` | Vertiefung und Baugrube nach § 909 BGB prüfen: Verlust der Bodenstütze, Unterfangung, Risse, Setzung, Sicherungsmaßnahmen, Baustopp, Beweise, Sachverständige und Eilrechtsschutz: Vertiefung und Baugrube nach § 909 BGB prüfen: Verlust der... |
| `vertiefung-interessen-wurzeln-zaun` | Vertiefung: Mehrparteienkonflikt und Interessenmatrix. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Nachbarschaftsstreit Prüfer. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Nachbarschaftsstreit Prüfer. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Nachbarschaftsstreit Prüfer. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Nachbarschaftsstreit Prüfer. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `wurzeln-behoerden-gericht-und-registerweg` | Wurzeln: Behörden-, Gerichts- oder Registerweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `zaun-verhandlung-vergleich-und-eskalation` | Zaun: Verhandlung, Vergleich und Eskalation. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
