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
| **Akte Wusterhagen: Mühlenstau, Chaussee und Aufopferung** (`preussisches-landrecht-wusterhagen-muehlenstau-aufopferung`) | [Gesamt-PDF lesen](../testakten/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung/gesamt-pdf/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung_gesamt.pdf) | [`testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anspruchslandkarte-bgb-aufforderungsschreiben` | Anspruchslandkarte Bgb Nachbarrecht, Aufforderungsschreiben Nachbar, Beweissicherung Ortstermin Fotos: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `aufforderung-beweise-red-grenzbaum` | Aufforderung Mandantenkommunikation Entscheidungsvorlage, Beweise Red Team Und Qualitaetskontrolle, Grenzbaum Schriftsatz Brief Und Memo Bausteine: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und... |
| `drohender-einsturz-einfriedung-zaun` | Drohender Einsturz Gefahranlage, Einfriedung Zaun Mauer Hecke, Einstweilige Verfuegung Und Klage: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `fristennotiz-naechster-ueberbau-akten` | Prüfer Fristennotiz Und Naechster Schritt, Ueberbau Fristen Form Und Zustaendigkeit, Akten Und Grundstuecksaufnahme: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbar... |
| `grenzbaum-grenzanlage-hammerschlags` | Grenzbaum Und Grenzanlage, Hammerschlags Und Leiterrecht, Horrorfall Aktenauswertung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `hammerschlagsrecht-hecke-immissionen` | Hammerschlagsrecht Formular Portal Und Einreichung, Hecke Zahlen Schwellen Und Berechnung, Immissionen Compliance Dokumentation Und Akte: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert d... |
| `immissionen-laerm-landesnachbarrecht` | Immissionen Laerm Geruch Rauch Licht, Landesnachbarrecht Router, Nach Grenzbebauung Ueberhang Spezial: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `kaltstart-abschlussprodukt-und-uebergabe` | Kaltstart: Einstieg und Routing; Abschlussprodukt und Übergabe: klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `klage-beweislast-nachbarrecht` | Klage Beweislast Und Darlegungslast, Nachbarrecht Erstpruefung Und Mandatsziel, Nachbarschaftsstreit Tatbestand Beweis Und Belege: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den näch... |
| `laermimmissionen-mediation-vorrang` | Nach Laermimmissionen Spezial, Nach Mediation Vorrang Leitfaden, Nach Nachbarrechtsuebersicht Bauleiter: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `mauer-quellenkarte` | Mauer Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `nachbarrecht-kaltstart-triage` | Erstaufnahme eines Nachbarrechtsfalls: Beteiligte, Grundstücke, Bundesland, Grenze, Streitgegenstand, Gefahr, Fristen, Beweise, bisherige Eskalation und Ziel klären; danach in die passenden Fachmodule routen. |
| `nachbarschaftsstreit-fristen-risiko-mandant` | Fristen Und Risikoampel, Mandantenkommunikation, Redteam Qualitygate: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `nachbarschaftsstreit-pruefer-anschluss-router` | Allgemein, Anschluss Skills Router, Chronologie Und Belegmatrix: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `nachbarschaftsstreit-pruefer-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `nachbarschaftsstreit-pruefer-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `nachbarschaftsstreit-pruefer-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `nachbarschaftsstreit-pruefer-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `nachbarschaftsstreit-pruefer-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `notweg-ueberhang-sonderfall-edge` | Notweg Internationaler Bezug Und Schnittstellen, Ueberhang Dokumentenmatrix Und Lueckenliste, Vergleich Sonderfall Und Edge Case: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächs... |
| `notweg-zufahrt-selbsthilfe-eskalationsgrenzen` | Notweg Zufahrt Wegerecht, Selbsthilfe Und Eskalationsgrenzen, Aeste Risikoampel Und Gegenargumente: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `ueberbau-ueberhang-aeste-mediation` | Ueberbau Prüfung, Ueberhang Aeste Wurzeln, Vergleich Mediation Nachbarschaftsfrieden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `vertiefung-baugrube` | Vertiefung Baugrube Stuetzverlust: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `vertiefung-interessen-wurzeln-zaun` | Vertiefung Mehrparteien Konflikt Und Interessen, Wurzeln Behörden Gericht Und Registerweg, Zaun Verhandlung Vergleich Und Eskalation: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den n... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
