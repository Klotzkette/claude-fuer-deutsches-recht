# aktenauszug-gerichtsverfahren


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`aktenauszug-gerichtsverfahren`) | [`aktenauszug-gerichtsverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenauszug-gerichtsverfahren.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Strukturierter Aktenauszug für deutsche Gerichtsverfahren: Verfahrensidentifikation Einleitungssatz Verfahrenszusammenfassung Sachverhaltschronologie Verfahrensgeschichte tabellarische Gegenüberstellung der Parteivorträge Beweismittel und Rechtsargumente für schnelle Einarbeitung in Akten.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`aktenauszug-gerichtsverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenauszug-gerichtsverfahren.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/aktenauszug-gerichtsverfahren/aktenauszug-gerichtsverfahren-werkstatt.md" download><code>aktenauszug-gerichtsverfahren-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/aktenauszug-gerichtsverfahren/aktenauszug-gerichtsverfahren-schnellstart.md" download><code>aktenauszug-gerichtsverfahren-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
**Version:** 3.2.1
**Autor:** Klotzkette

---

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Plugin erscheint in der Plugin-Liste; alle 21 Skills sind sofort verfügbar.
4. Für Updates: neues ZIP herunterladen und Plugin ersetzen.
5. Hinweis: Das Plugin-ZIP muss direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten — nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Überblick

Das Plugin `aktenauszug-gerichtsverfahren` generiert strukturierte Aktenauszüge für deutsche Gerichtsverfahren. Es richtet sich an Rechtsanwältinnen und Rechtsanwälte, die sich schnell in ein neues oder übernommenes Mandat einarbeiten müssen.

**Einsatzgebiete:**

- Mandatswechsel und Übernahme von laufenden Verfahren
- Einarbeitung neuer Sachbearbeiter in komplexe Akten
- Vorbereitung auf mündliche Verhandlungen
- Strukturierung umfangreicher Akten vor Beratungsgesprächen
- Erstellung von Mandantenberichten zum Verfahrensstand

**Verfahrensarten:**

- Zivilverfahren (ZPO) inkl. Berufung, Revision, einstweilige Verfügung
- Strafverfahren (StPO) inkl. Revision und Wiederaufnahme
- Verwaltungsverfahren (VwGO) inkl. Berufung und Revision
- Arbeitsgerichtsverfahren (ArbGG) inkl. Urteilsverfahren und Beschlussverfahren
- Sozialgerichtsverfahren (SGG) inkl. Berufung und Eilrechtsschutz

## Skills-Übersicht

| Skill | Zweck |
| --- | --- |
| `aktenauszug-erstellen` | Hauptworkflow: erzeugt alle sechs Bausteine des strukturierten Aktenauszugs aus PDFs und Schriftsätzen |
| `verfahrensidentifikation` | Extrahiert Gericht Kammer Aktenzeichen Streitwert Parteien Instanz und Verfahrensart |
| `einleitungssatz-generator` | Verfasst einen prägnanten ein- bis zweiSatz-Kern des Rechtsstreits mit Hauptnorm |
| `verfahrenszusammenfassung-absatz` | Schreibt zusammenfassenden Absatz mit acht bis zehn Sätzen zu Hintergrund Streitstand prozessualer Lage und nächsten Schritten |
| `sachverhaltschronologie` | Chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen mit Datum und Fundstelle |
| `verfahrenschronologie` | Chronologische Bullet-Liste aller prozessualen Schritte mit hervorgehobenen Fristen |
| `parteivortrag-gegenueberstellung` | Tabelle mit Kläger- und Beklagtenposition zu jedem Streitpunkt |
| `beweismittel-gegenueberstellung` | Tabelle aller Beweisangebote (Zeugen Urkunden Sachverständige) nach Partei und Beweisthema |
| `rechtsargumente-gegenueberstellung` | Tabelle der Rechtsargumente beider Parteien mit Anspruchsgrundlagen Einwendungen Einreden und Rechtsprechungsnachweisen |
| `fristen-und-terminkalender` | Identifiziert und hebt alle prozessrelevanten Fristen und Termine hervor |
| `anlagenverzeichnis-extrakt` | Vollständiges Anlagenverzeichnis aller K-/B-Anlagen mit Inhalt und Fundstelle |
| `schwerpunktthemen-identifikation` | Identifiziert drei bis fünf zentrale Rechtsfragen ohne Erfolgsprognose |
| `neutralitaetspruefung` | Prüft den Aktenauszug auf unzulässige Wertungen und Prognosen und schlägt Korrekturen vor |
| `aktenauszug-strukturpruefung` | Vollständigkeitsprüfung aller sechs Bausteine und Qualitätsgrundsätze |
| `zivilprozess-modus` | ZPO-spezifische Einstellungen für ordentliche Klage Berufung Revision und einstweilige Verfügung |
| `strafprozess-modus` | StPO-spezifische Einstellungen für Anklageverfahren Hauptverhandlung und Revision |
| `verwaltungsprozess-modus` | VwGO-spezifische Einstellungen mit Vorverfahren aufschiebender Wirkung und Berufungszulassung |
| `arbeitsgerichtsverfahren-modus` | ArbGG-spezifische Einstellungen mit Gütetermin KSchG-Dreiwochenfrist und Beschlussverfahren |
| `sozialgerichtsverfahren-modus` | SGG-spezifische Einstellungen mit Widerspruchsverfahren Amtsermittlung und Eilrechtsschutz |
| `anwaltsschriftsatz-stilrichtlinie` | Verbindliche Stilregeln für Sprache Gliederung Nomenklatur und Markdown-Formatierung |

## Methodik

Ausführliche Erläuterung der Methodik unter [references/methodik.md](references/methodik.md).

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beispielprompt

```
Erstelle einen strukturierten Aktenauszug für das anhängende Verfahren vor dem Landgericht Frankfurt am Main (Az. 3 O 456/23). Die Akte enthält Klageschrift, Klageerwiderung und den Beweisbeschluss vom 15.09.2023. Verwende den Zivilprozess-Modus.
```

## Disclaimer

Dieses Plugin erstellt keine Rechtsberatung und gibt keine Erfolgsprognose ab. Die erstellten Aktenauszüge sind Arbeitsinstrumente, die der Prüfung und Freigabe durch den zuständigen Rechtsanwalt bedürfen. Das Plugin ersetzt nicht die eigene Aktenlektüre.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anschluss-routing`, `dokumente-intake`, `einstieg-routing`, `start-chronologie-fristen`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `akten-mandantenkommunikation-entscheidungsvorlage`, `aktenauszug-erstellen`, `aktenauszug-strukturpruefung-akzg-bauleiter`, `aktenauszug-tatbestand-beweis-und-belege`, `aktenauszug-verfahrensidentifikation-gericht`, `akzg-aktenauszug-bauleiter`, `anwaltsschriftsatz-beweislast-beweismittel`, `beweismittel-gegenueberstellung`, `beweismittel-mehrparteien-konflikt-und-interessen`, `parteivortraege-compliance-dokumentation-und-akte`, `quellen-livecheck`, `sachverhaltschronologie`, `sachverhaltschronologie-textbausteine`, `schnelle-formular-portal-und-einreichung`, `schwerpunktthemen-identifikation-akten`, `spezial-tabellarische-livequellen-und-rechtsprechungscheck`, `tabellarische-quellenkarte`, `unterlagen-luecken`, ... plus 2 weitere |
| 3. Prüfung, Anspruch und Subsumtion | `einleitungssatz-risikoampel-und-gegenargumente`, `neutralitaetspruefung`, `workflow-fristen-und-risikoampel` |
| 4. Gestaltung, Strategie und Verhandlung | `strukturierter-strafprozess-modus`, `verfahrensgeschichte-vergleich-eskalation` |
| 5. Verfahren, Behörde und Gericht | `akzg-multiparteienverfahren-konsolidierung-spezial`, `anwaltsschriftsatz-stilrichtlinie`, `arbeitsgerichtsverfahren-modus-terminkalender`, `erstellen-fristennotiz-gerichtsverfahren`, `fristen-und-terminkalender`, `gerichtsverfahren-fristen-form-und-zustaendigkeit`, `sozialgerichtsverfahren-modus`, `verfahrenschronologie`, `verfahrensidentifikation`, `verfahrenszusammenfassung-absatz`, `verfahrenszusammenfassung-rechtsweg-register` |
| 6. Ergebnis, Schreiben und Kommunikation | `output-waehlen` |
| 7. Kontrolle, Qualität und Gegenprüfung | `einarbeitung-fehlerkatalog`, `gegenueberstellung-parteivortraege`, `mandantenkommunikation-redteam-qualitygate-akzg`, `parteivortrag-gegenueberstellung`, `rechtsargumente-gegenueberstellung`, `spezial-einarbeitung-red-team-und-qualitaetskontrolle`, `workflow-redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `akzg-vertraulichkeit-redaction-spezial`, `akzg-zeitstrahl-anlagenverzeichnis-extrakt`, `anlagenverzeichnis-extrakt`, `einleitungssatz-generator`, `rechtsargumente-internationaler-bezug-und-schnittstellen`, `stilrichtlinie-sonderfall-und-edge-case`, `strafprozess-modus`, `verwaltungsprozess-modus`, `zivilprozess-modus` |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 58 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `akten-mandantenkommunikation-entscheidungsvorlage` | Wenn es um Akten: Mandantenkommunikation und Entscheidungsvorlage in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `aktenauszug-erstellen` | Wenn es um Aktenauszug Erstellen — Hauptworkflow in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `aktenauszug-strukturpruefung-akzg-bauleiter` | Wenn es um Aktenauszug — Strukturprüfung in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aktenauszug-tatbestand-beweis-und-belege` | Wenn es um Aktenauszug: Tatbestandsmerkmale, Beweisfragen und Beleglage in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `aktenauszug-verfahrensidentifikation-gericht` | Wenn es um Verfahrensidentifikation in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `akzg-aktenauszug-bauleiter` | Wenn es um AkzG: Aktenauszug Bauleiter in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `akzg-multiparteienverfahren-konsolidierung-spezial` | Wenn es um AkzG: Multipartei Konsolidierung in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `akzg-vertraulichkeit-redaction-spezial` | Wenn es um AkzG: Vertraulichkeit Redaction in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `akzg-zeitstrahl-anlagenverzeichnis-extrakt` | Wenn es um AkzG: Zeitstrahl-Checkliste in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anlagenverzeichnis-extrakt` | Wenn es um Anlagenverzeichnis-Extrakt in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anschluss-routing` | Wenn es um Anschluss-Routing in aktenauszug-gerichtsverfahren geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anwaltsschriftsatz-beweislast-beweismittel` | Wenn es um Anwaltsschriftsatz: Beweislast, Darlegungslast und Substantiierung in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen... |
| `anwaltsschriftsatz-stilrichtlinie` | Wenn es um Anwaltsschriftsatz-Stilrichtlinie in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `arbeitsgerichtsverfahren-modus-terminkalender` | Wenn es um Arbeitsgerichtsverfahren-Modus (ArbGG) in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beweismittel-gegenueberstellung` | Wenn es um Beweismittel — Gegenüberstellung in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beweismittel-mehrparteien-konflikt-und-interessen` | Wenn es um Beweismittel: Mehrparteienkonflikt und Interessenmatrix in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `dokumente-intake` | Wenn es um Dokumentenintake in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einarbeitung-fehlerkatalog` | Wenn es um Einarbeitung Fehlerkatalog in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einleitungssatz-generator` | Wenn es um Einleitungssatz-Generator in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `einleitungssatz-risikoampel-und-gegenargumente` | Wenn es um Einleitungssatz: Risikoampel, Gegenargumente und Verteidigungslinien in aktenauszug-gerichtsverfahren geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofort... |
| `einstieg-routing` | Wenn es um Einstieg und Routing in aktenauszug-gerichtsverfahren geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erstellen-fristennotiz-gerichtsverfahren` | Wenn es um Erstellen: Fristennotiz und nächster Schritt in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fristen-und-terminkalender` | Wenn es um Fristen und Terminkalender in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gegenueberstellung-parteivortraege` | Wenn es um Gegenueberstellung: Zahlen, Schwellenwerte und Berechnung in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `gerichtsverfahren-fristen-form-und-zustaendigkeit` | Wenn es um Gerichtsverfahren: Fristen, Form, Zuständigkeit und Rechtsweg in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mandantenkommunikation-redteam-qualitygate-akzg` | Wenn es um Mandantenkommunikation in aktenauszug-gerichtsverfahren geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `neutralitaetspruefung` | Wenn es um Neutralitätsprüfung in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `output-waehlen` | Wenn es um Output wählen in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `parteivortraege-compliance-dokumentation-und-akte` | Wenn es um Parteivortraege: Compliance-Dokumentation und Aktenvermerk in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und... |
| `parteivortrag-gegenueberstellung` | Wenn es um Parteivortrag — Gegenüberstellung in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `rechtsargumente-gegenueberstellung` | Wenn es um Rechtsargumente — Gegenüberstellung in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rechtsargumente-internationaler-bezug-und-schnittstellen` | Wenn es um Rechtsargumente: Internationaler Bezug und Schnittstellen in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sachverhaltschronologie` | Wenn es um Sachverhaltschronologie in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `sachverhaltschronologie-textbausteine` | Wenn es um Sachverhaltschronologie: Schriftsatz-, Brief- und Memo-Bausteine in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Wide... |
| `schnelle-formular-portal-und-einreichung` | Wenn es um Schnelle: Formular, Portal und Einreichungslogik in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schwerpunktthemen-identifikation-akten` | Wenn es um Schwerpunktthemen-Identifikation in aktenauszug-gerichtsverfahren geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sozialgerichtsverfahren-modus` | Wenn es um Sozialgerichtsverfahren-Modus (SGG) in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-einarbeitung-red-team-und-qualitaetskontrolle` | Wenn es um Einarbeitung: Red-Team und Qualitätskontrolle in aktenauszug-gerichtsverfahren geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-tabellarische-livequellen-und-rechtsprechungscheck` | Wenn es um Tabellarische: Livequellen- und Rechtsprechungscheck in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `start-chronologie-fristen` | Wenn es um Aktenauszug Gerichtsverfahren — Allgemein in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `stilrichtlinie-sonderfall-und-edge-case` | Wenn es um Stilrichtlinie: Sonderfall und Edge-Case-Prüfung in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strafprozess-modus` | Wenn es um Strafprozess-Modus (StPO) in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `strukturierter-strafprozess-modus` | Wenn es um Strukturierter: Erstprüfung, Rollenklärung und Mandatsziel in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tabellarische-quellenkarte` | Wenn es um Tabellarische Quellenkarte in aktenauszug-gerichtsverfahren geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verfahrenschronologie` | Wenn es um Verfahrenschronologie in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `verfahrensgeschichte-vergleich-eskalation` | Wenn es um Verfahrensgeschichte: Verhandlung, Vergleich und Eskalation in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `verfahrensidentifikation` | Wenn es um Verfahrensidentifikation: Dokumentenmatrix, Lückenliste und Nachforderung in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `verfahrenszusammenfassung-absatz` | Wenn es um Verfahrenszusammenfassung — Absatz in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `verfahrenszusammenfassung-rechtsweg-register` | Wenn es um Verfahrenszusammenfassung: Behörden-, Gerichts- oder Registerweg in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verwaltungsprozess-modus` | Wenn es um Verwaltungsprozess-Modus (VwGO) in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `workflow-fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in aktenauszug-gerichtsverfahren geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-redteam-qualitygate` | Wenn es um Red-Team Qualitygate in aktenauszug-gerichtsverfahren geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `zivilprozess-modus` | Wenn es um Zivilprozess Modus in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
