# aktenauszug-gerichtsverfahren

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Strukturierter Aktenauszug für deutsche Gerichtsverfahren: Verfahrensidentifikation Einleitungssatz Verfahrenszusammenfassung Sachverhaltschronologie Verfahrensgeschichte tabellarische Gegenüberstellung der Parteivorträge Beweismittel und Rechtsargumente für schnelle Einarbeitung in Akten.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/aktenauszug-gerichtsverfahren.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill aus der Skill-Liste wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart als Markdown laden und zusammen mit den Unterlagen öffnen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für aktenauszug-gerichtsverfahren:

> Lies zuerst alle Dateien im ausgewählten Ordner. Bearbeite den Vorgang mit diesem Fachgebiet und liefere als Erstes Relationszeile: Anspruch, Klägertatsache, Bestreiten, Einwendung, Replik, Beweislast, Beweismittel und Entscheidung als Tabelle. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`aktenauszug-gerichtsverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenauszug-gerichtsverfahren.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/aktenauszug-gerichtsverfahren/aktenauszug-gerichtsverfahren-schnellstart.md" download><code>aktenauszug-gerichtsverfahren-schnellstart.md</code></a> |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/aktenauszug-gerichtsverfahren/aktenauszug-gerichtsverfahren-werkstatt.md" download><code>aktenauszug-gerichtsverfahren-werkstatt.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
**Version:** 439.0.1
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
| 1. Einstieg und Fallrouting | [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`akten-mandantenkommunikation-entscheidungsvorlage`](skills/akten-mandantenkommunikation-entscheidungsvorlage/SKILL.md), [`aktenauszug-erstellen`](skills/aktenauszug-erstellen/SKILL.md), [`aktenauszug-strukturpruefung-akzg-bauleiter`](skills/aktenauszug-strukturpruefung-akzg-bauleiter/SKILL.md), [`aktenauszug-tatbestand-beweis-und-belege`](skills/aktenauszug-tatbestand-beweis-und-belege/SKILL.md), [`aktenauszug-verfahrensidentifikation-gericht`](skills/aktenauszug-verfahrensidentifikation-gericht/SKILL.md), [`akzg-aktenauszug-bauleiter`](skills/akzg-aktenauszug-bauleiter/SKILL.md), [`anwaltsschriftsatz-beweislast-beweismittel`](skills/anwaltsschriftsatz-beweislast-beweismittel/SKILL.md), [`beweismittel-gegenueberstellung`](skills/beweismittel-gegenueberstellung/SKILL.md), [`beweismittel-mehrparteien-konflikt-und-interessen`](skills/beweismittel-mehrparteien-konflikt-und-interessen/SKILL.md), [`parteivortraege-compliance-dokumentation-und-akte`](skills/parteivortraege-compliance-dokumentation-und-akte/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`sachverhaltschronologie`](skills/sachverhaltschronologie/SKILL.md), [`sachverhaltschronologie-textbausteine`](skills/sachverhaltschronologie-textbausteine/SKILL.md), [`schnelle-formular-portal-und-einreichung`](skills/schnelle-formular-portal-und-einreichung/SKILL.md), [`schwerpunktthemen-identifikation-akten`](skills/schwerpunktthemen-identifikation-akten/SKILL.md), [`spezial-tabellarische-livequellen-und-rechtsprechungscheck`](skills/spezial-tabellarische-livequellen-und-rechtsprechungscheck/SKILL.md), [`tabellarische-quellenkarte`](skills/tabellarische-quellenkarte/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), ... plus 2 weitere |
| 3. Prüfung, Anspruch und Subsumtion | [`einleitungssatz-risikoampel-und-gegenargumente`](skills/einleitungssatz-risikoampel-und-gegenargumente/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`neutralitaetspruefung`](skills/neutralitaetspruefung/SKILL.md), [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`strukturierter-strafprozess-modus`](skills/strukturierter-strafprozess-modus/SKILL.md), [`verfahrensgeschichte-vergleich-eskalation`](skills/verfahrensgeschichte-vergleich-eskalation/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`akzg-multiparteienverfahren-konsolidierung-spezial`](skills/akzg-multiparteienverfahren-konsolidierung-spezial/SKILL.md), [`anwaltsschriftsatz-stilrichtlinie`](skills/anwaltsschriftsatz-stilrichtlinie/SKILL.md), [`arbeitsgerichtsverfahren-modus-terminkalender`](skills/arbeitsgerichtsverfahren-modus-terminkalender/SKILL.md), [`erstellen-fristennotiz-gerichtsverfahren`](skills/erstellen-fristennotiz-gerichtsverfahren/SKILL.md), [`fristen-und-terminkalender`](skills/fristen-und-terminkalender/SKILL.md), [`gerichtsverfahren-fristen-form-und-zustaendigkeit`](skills/gerichtsverfahren-fristen-form-und-zustaendigkeit/SKILL.md), [`sozialgerichtsverfahren-modus`](skills/sozialgerichtsverfahren-modus/SKILL.md), [`verfahrenschronologie`](skills/verfahrenschronologie/SKILL.md), [`verfahrensidentifikation`](skills/verfahrensidentifikation/SKILL.md), [`verfahrenszusammenfassung-absatz`](skills/verfahrenszusammenfassung-absatz/SKILL.md), [`verfahrenszusammenfassung-rechtsweg-register`](skills/verfahrenszusammenfassung-rechtsweg-register/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`output-waehlen`](skills/output-waehlen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`einarbeitung-fehlerkatalog`](skills/einarbeitung-fehlerkatalog/SKILL.md), [`gegenueberstellung-parteivortraege`](skills/gegenueberstellung-parteivortraege/SKILL.md), [`mandantenkommunikation-redteam-qualitygate-akzg`](skills/mandantenkommunikation-redteam-qualitygate-akzg/SKILL.md), [`parteivortrag-gegenueberstellung`](skills/parteivortrag-gegenueberstellung/SKILL.md), [`rechtsargumente-gegenueberstellung`](skills/rechtsargumente-gegenueberstellung/SKILL.md), [`spezial-einarbeitung-red-team-und-qualitaetskontrolle`](skills/spezial-einarbeitung-red-team-und-qualitaetskontrolle/SKILL.md), [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`akzg-vertraulichkeit-redaction-spezial`](skills/akzg-vertraulichkeit-redaction-spezial/SKILL.md), [`akzg-zeitstrahl-anlagenverzeichnis-extrakt`](skills/akzg-zeitstrahl-anlagenverzeichnis-extrakt/SKILL.md), [`anlagenverzeichnis-extrakt`](skills/anlagenverzeichnis-extrakt/SKILL.md), [`einleitungssatz-generator`](skills/einleitungssatz-generator/SKILL.md), [`rechtsargumente-internationaler-bezug-und-schnittstellen`](skills/rechtsargumente-internationaler-bezug-und-schnittstellen/SKILL.md), [`stilrichtlinie-sonderfall-und-edge-case`](skills/stilrichtlinie-sonderfall-und-edge-case/SKILL.md), [`strafprozess-modus`](skills/strafprozess-modus/SKILL.md), [`verwaltungsprozess-modus`](skills/verwaltungsprozess-modus/SKILL.md), [`zivilprozess-modus`](skills/zivilprozess-modus/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`akten-mandantenkommunikation-entscheidungsvorlage`](skills/akten-mandantenkommunikation-entscheidungsvorlage/SKILL.md) | Wenn es um Akten: Mandantenkommunikation und Entscheidungsvorlage in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| [`aktenauszug-erstellen`](skills/aktenauszug-erstellen/SKILL.md) | Wenn es um Aktenauszug Erstellen — Hauptworkflow in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`aktenauszug-strukturpruefung-akzg-bauleiter`](skills/aktenauszug-strukturpruefung-akzg-bauleiter/SKILL.md) | Wenn es um Aktenauszug — Strukturprüfung in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`aktenauszug-tatbestand-beweis-und-belege`](skills/aktenauszug-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Aktenauszug: Tatbestandsmerkmale, Beweisfragen und Beleglage in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`aktenauszug-verfahrensidentifikation-gericht`](skills/aktenauszug-verfahrensidentifikation-gericht/SKILL.md) | Wenn es um Verfahrensidentifikation in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`akzg-aktenauszug-bauleiter`](skills/akzg-aktenauszug-bauleiter/SKILL.md) | Wenn es um AkzG: Aktenauszug Bauleiter in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`akzg-multiparteienverfahren-konsolidierung-spezial`](skills/akzg-multiparteienverfahren-konsolidierung-spezial/SKILL.md) | Wenn es um AkzG: Multipartei Konsolidierung in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`akzg-vertraulichkeit-redaction-spezial`](skills/akzg-vertraulichkeit-redaction-spezial/SKILL.md) | Wenn es um AkzG: Vertraulichkeit Redaction in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`akzg-zeitstrahl-anlagenverzeichnis-extrakt`](skills/akzg-zeitstrahl-anlagenverzeichnis-extrakt/SKILL.md) | Wenn es um AkzG: Zeitstrahl-Checkliste in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`anlagenverzeichnis-extrakt`](skills/anlagenverzeichnis-extrakt/SKILL.md) | Wenn es um Anlagenverzeichnis-Extrakt in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in aktenauszug-gerichtsverfahren geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`anwaltsschriftsatz-beweislast-beweismittel`](skills/anwaltsschriftsatz-beweislast-beweismittel/SKILL.md) | Wenn es um Anwaltsschriftsatz: Beweislast, Darlegungslast und Substantiierung in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen... |
| [`anwaltsschriftsatz-stilrichtlinie`](skills/anwaltsschriftsatz-stilrichtlinie/SKILL.md) | Wenn es um Anwaltsschriftsatz-Stilrichtlinie in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`arbeitsgerichtsverfahren-modus-terminkalender`](skills/arbeitsgerichtsverfahren-modus-terminkalender/SKILL.md) | Wenn es um Arbeitsgerichtsverfahren-Modus (ArbGG) in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`beweismittel-gegenueberstellung`](skills/beweismittel-gegenueberstellung/SKILL.md) | Wenn es um Beweismittel — Gegenüberstellung in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`beweismittel-mehrparteien-konflikt-und-interessen`](skills/beweismittel-mehrparteien-konflikt-und-interessen/SKILL.md) | Wenn es um Beweismittel: Mehrparteienkonflikt und Interessenmatrix in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einarbeitung-fehlerkatalog`](skills/einarbeitung-fehlerkatalog/SKILL.md) | Wenn es um Einarbeitung Fehlerkatalog in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einleitungssatz-generator`](skills/einleitungssatz-generator/SKILL.md) | Wenn es um Einleitungssatz-Generator in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`einleitungssatz-risikoampel-und-gegenargumente`](skills/einleitungssatz-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Einleitungssatz: Risikoampel, Gegenargumente und Verteidigungslinien in aktenauszug-gerichtsverfahren geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofort... |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in aktenauszug-gerichtsverfahren geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`erstellen-fristennotiz-gerichtsverfahren`](skills/erstellen-fristennotiz-gerichtsverfahren/SKILL.md) | Wenn es um Erstellen: Fristennotiz und nächster Schritt in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fristen-und-terminkalender`](skills/fristen-und-terminkalender/SKILL.md) | Wenn es um Fristen und Terminkalender in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gegenueberstellung-parteivortraege`](skills/gegenueberstellung-parteivortraege/SKILL.md) | Wenn es um Gegenueberstellung: Zahlen, Schwellenwerte und Berechnung in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`gerichtsverfahren-fristen-form-und-zustaendigkeit`](skills/gerichtsverfahren-fristen-form-und-zustaendigkeit/SKILL.md) | Wenn es um Gerichtsverfahren: Fristen, Form, Zuständigkeit und Rechtsweg in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Aktenauszug Gerichtsverfahren ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`mandantenkommunikation-redteam-qualitygate-akzg`](skills/mandantenkommunikation-redteam-qualitygate-akzg/SKILL.md) | Wenn es um Mandantenkommunikation in aktenauszug-gerichtsverfahren geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| [`neutralitaetspruefung`](skills/neutralitaetspruefung/SKILL.md) | Wenn es um Neutralitätsprüfung in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`parteivortraege-compliance-dokumentation-und-akte`](skills/parteivortraege-compliance-dokumentation-und-akte/SKILL.md) | Wenn es um Parteivortraege: Compliance-Dokumentation und Aktenvermerk in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und... |
| [`parteivortrag-gegenueberstellung`](skills/parteivortrag-gegenueberstellung/SKILL.md) | Wenn es um Parteivortrag — Gegenüberstellung in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`rechtsargumente-gegenueberstellung`](skills/rechtsargumente-gegenueberstellung/SKILL.md) | Wenn es um Rechtsargumente — Gegenüberstellung in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`rechtsargumente-internationaler-bezug-und-schnittstellen`](skills/rechtsargumente-internationaler-bezug-und-schnittstellen/SKILL.md) | Wenn es um Rechtsargumente: Internationaler Bezug und Schnittstellen in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`sachverhaltschronologie`](skills/sachverhaltschronologie/SKILL.md) | Wenn es um Sachverhaltschronologie in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`sachverhaltschronologie-textbausteine`](skills/sachverhaltschronologie-textbausteine/SKILL.md) | Wenn es um Sachverhaltschronologie: Schriftsatz-, Brief- und Memo-Bausteine in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Wide... |
| [`schnelle-formular-portal-und-einreichung`](skills/schnelle-formular-portal-und-einreichung/SKILL.md) | Wenn es um Schnelle: Formular, Portal und Einreichungslogik in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schwerpunktthemen-identifikation-akten`](skills/schwerpunktthemen-identifikation-akten/SKILL.md) | Wenn es um Schwerpunktthemen-Identifikation in aktenauszug-gerichtsverfahren geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`sozialgerichtsverfahren-modus`](skills/sozialgerichtsverfahren-modus/SKILL.md) | Wenn es um Sozialgerichtsverfahren-Modus (SGG) in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-einarbeitung-red-team-und-qualitaetskontrolle`](skills/spezial-einarbeitung-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Einarbeitung: Red-Team und Qualitätskontrolle in aktenauszug-gerichtsverfahren geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-tabellarische-livequellen-und-rechtsprechungscheck`](skills/spezial-tabellarische-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Tabellarische: Livequellen- und Rechtsprechungscheck in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md) | Wenn es um Aktenauszug Gerichtsverfahren — Allgemein in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`stilrichtlinie-sonderfall-und-edge-case`](skills/stilrichtlinie-sonderfall-und-edge-case/SKILL.md) | Wenn es um Stilrichtlinie: Sonderfall und Edge-Case-Prüfung in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafprozess-modus`](skills/strafprozess-modus/SKILL.md) | Wenn es um Strafprozess-Modus (StPO) in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strukturierter-strafprozess-modus`](skills/strukturierter-strafprozess-modus/SKILL.md) | Wenn es um Strukturierter: Erstprüfung, Rollenklärung und Mandatsziel in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`tabellarische-quellenkarte`](skills/tabellarische-quellenkarte/SKILL.md) | Wenn es um Tabellarische Quellenkarte in aktenauszug-gerichtsverfahren geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verfahrenschronologie`](skills/verfahrenschronologie/SKILL.md) | Wenn es um Verfahrenschronologie in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`verfahrensgeschichte-vergleich-eskalation`](skills/verfahrensgeschichte-vergleich-eskalation/SKILL.md) | Wenn es um Verfahrensgeschichte: Verhandlung, Vergleich und Eskalation in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`verfahrensidentifikation`](skills/verfahrensidentifikation/SKILL.md) | Wenn es um Verfahrensidentifikation: Dokumentenmatrix, Lückenliste und Nachforderung in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`verfahrenszusammenfassung-absatz`](skills/verfahrenszusammenfassung-absatz/SKILL.md) | Wenn es um Verfahrenszusammenfassung — Absatz in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`verfahrenszusammenfassung-rechtsweg-register`](skills/verfahrenszusammenfassung-rechtsweg-register/SKILL.md) | Wenn es um Verfahrenszusammenfassung: Behörden-, Gerichts- oder Registerweg in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verwaltungsprozess-modus`](skills/verwaltungsprozess-modus/SKILL.md) | Wenn es um Verwaltungsprozess-Modus (VwGO) in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel in aktenauszug-gerichtsverfahren geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in aktenauszug-gerichtsverfahren geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in aktenauszug-gerichtsverfahren geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in aktenauszug-gerichtsverfahren geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`zivilprozess-modus`](skills/zivilprozess-modus/SKILL.md) | Wenn es um Zivilprozess Modus in aktenauszug-gerichtsverfahren geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
