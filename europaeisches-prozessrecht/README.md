# Europäisches Prozessrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Europaeisches Prozessrecht vor EuGH und EuG: Klagearten, Vorlage, e-Curia, Fristen, Rechtsschutz, Rechtsmittel, Intervention, Beweis, Kosten und Strategie.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/europaeisches-prozessrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`europaeisches-prozessrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/europaeisches-prozessrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/europaeisches-prozessrecht/europaeisches-prozessrecht-werkstatt.md" download><code>europaeisches-prozessrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/europaeisches-prozessrecht/europaeisches-prozessrecht-schnellstart.md" download><code>europaeisches-prozessrecht-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Eigenes Verfahrensplugin für Verfahren vor dem Gerichtshof der Europäischen Union und dem Gericht der Europäischen Union, dem früheren Gericht erster Instanz. Es trennt Klagearten, Vorlageverfahren, e-Curia, Fristen, Verfahrenssprache, Beweis, Intervention, Rechtsmittel und Folgeverfahren so, dass aus einer Akte schnell ein belastbarer Schriftsatz-, Vermerk- oder Fristenplan wird.

## Arbeitslogik

1. Rolle, Verfahrensart und Gericht bestimmen: Gerichtshof, Gericht, EUIPO-Beschwerdeweg, Kommission oder nationales Vorlagegericht.
2. Frist und Zulässigkeit vor materieller Argumentation sichern.
3. Anlagen, Verfahrenssprache, Vertraulichkeit und e-Curia-Zustellung parallel vorbereiten.
4. Stärksten Klagegrund oder Vorlagekern zuerst ausformulieren und nur danach Nebenlinien ergänzen.
5. Am Ende immer ein Arbeitsprodukt liefern: Fristenblatt, Vorlagefrage, Klageschrift, Klagebeantwortung, Eilantrag, Rechtsmittelvermerk oder Urteilsauswertung.

## Offizielle Arbeitsquellen

1. Satzung des Gerichtshofs der Europäischen Union.
2. Verfahrensordnung des Gerichtshofs in konsolidierter Fassung.
3. Verfahrensordnung des Gerichts und Praktische Durchführungsbestimmungen.
4. e-Curia-Beschlüsse zu Einreichung und Zustellung.
5. Empfehlungen an nationale Gerichte zum Vorabentscheidungsverfahren.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`euipo-eu-gericht-route`](skills/euipo-eu-gericht-route/SKILL.md), [`kaltstart-verfahrensrouting`](skills/kaltstart-verfahrensrouting/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`vertraulichkeit-beweis-anlagen`](skills/vertraulichkeit-beweis-anlagen/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`amtshaftung-art-268-340`](skills/amtshaftung-art-268-340/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`kosten-und-prozessrisiko`](skills/kosten-und-prozessrisiko/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`muendliche-verhandlung-plaedoyer`](skills/muendliche-verhandlung-plaedoyer/SKILL.md), [`vergleich-ruecknahme-erledigung`](skills/vergleich-ruecknahme-erledigung/SKILL.md), [`vertragsverletzung-art-258-260`](skills/vertragsverletzung-art-258-260/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`eug-nichtigkeitsklage-art-263`](skills/eug-nichtigkeitsklage-art-263/SKILL.md), [`fristberechnung-verfahrenssprache`](skills/fristberechnung-verfahrenssprache/SKILL.md), [`klagebefugnis-private-plaumann`](skills/klagebefugnis-private-plaumann/SKILL.md), [`schriftsatzbau-eugh-eug`](skills/schriftsatzbau-eugh-eug/SKILL.md), [`untatigkeitsklage-art-265`](skills/untatigkeitsklage-art-265/SKILL.md), [`urteilsauswertung-folgeverfahren`](skills/urteilsauswertung-folgeverfahren/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`e-curia-versandmappe-endfertigen`](skills/e-curia-versandmappe-endfertigen/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`e-curia-einreichung-zustellung`](skills/e-curia-einreichung-zustellung/SKILL.md), [`einstweiliger-rechtsschutz-art-278-279`](skills/einstweiliger-rechtsschutz-art-278-279/SKILL.md), [`eugh-vorabentscheidung-art-267`](skills/eugh-vorabentscheidung-art-267/SKILL.md), [`intervention-streithelfer`](skills/intervention-streithelfer/SKILL.md), [`rechtsmittel-eug-eugh`](skills/rechtsmittel-eug-eugh/SKILL.md), [`vorlage-transfer-eug-2024`](skills/vorlage-transfer-eug-2024/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 22 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`amtshaftung-art-268-340`](skills/amtshaftung-art-268-340/SKILL.md) | Prüft Schadensersatzklagen wegen außervertraglicher Haftung der Union nach Art. 268 und 340 AEUV mit qualifiziertem Rechtsverstoß, Schaden, Kausalität und Bezifferung. |
| [`e-curia-einreichung-zustellung`](skills/e-curia-einreichung-zustellung/SKILL.md) | Führt durch e-Curia-Einreichung, Anlagen, Zustellung, Dateibenennung, Vertreterrolle, Fristenkontrolle und Empfangsprüfung vor EuGH und Gericht der Europäischen Union. |
| [`e-curia-versandmappe-endfertigen`](skills/e-curia-versandmappe-endfertigen/SKILL.md) | Endfertigt Klageschrift, Rechtsmittel, Streithilfeantrag und sonstige Verfahrensschrift vor Gericht und Gerichtshof der Europäischen Union: bestimmt Spruchkörper, Klageart, Frist und Verfahrenssprache, prüft Anträge und Vertretungsnachwe... |
| [`einstweiliger-rechtsschutz-art-278-279`](skills/einstweiliger-rechtsschutz-art-278-279/SKILL.md) | Baut Anträge auf Aussetzung und einstweilige Anordnung nach Art. 278 und 279 AEUV mit Dringlichkeit, fumus boni iuris, Interessenabwägung und Belegpflicht. |
| [`eug-nichtigkeitsklage-art-263`](skills/eug-nichtigkeitsklage-art-263/SKILL.md) | Prüft Nichtigkeitsklagen vor dem Gericht der Europäischen Union gegen EU-Rechtsakte: Klagebefugnis, Frist, anfechtbarer Akt, Klagegründe, Anlagenlogik und Antragssatz. |
| [`eugh-vorabentscheidung-art-267`](skills/eugh-vorabentscheidung-art-267/SKILL.md) | Entwickelt Vorlagefragen, Vorlagebeschluss, Parteivortrag und nationale Verfahrensstrategie nach Art. 267 AEUV, inklusive Entscheidungserheblichkeit, acte clair, acte éclairé und Vorlagepflicht letzter Instanzen. |
| [`euipo-eu-gericht-route`](skills/euipo-eu-gericht-route/SKILL.md) | Routet Marken- und Designverfahren vom EUIPO über Beschwerdekammer, Gericht der Europäischen Union und Gerichtshof mit Fristen, Prüfungsumfang und Anfechtungszielen. |
| [`fristberechnung-verfahrenssprache`](skills/fristberechnung-verfahrenssprache/SKILL.md) | Berechnet unionsprozessuale Fristen, Entfernungsfrist, Verfahrenssprache, Zustellungsfolgen und interne Review-Termine für EuGH- und EuG-Verfahren. |
| [`intervention-streithelfer`](skills/intervention-streithelfer/SKILL.md) | Plant Streitbeitritt und Intervention nach Satzung und Verfahrensordnungen: Interesse am Ausgang, Frist, Rolle, Schriftsatzgrenzen, Vertraulichkeit und Koordination mit Hauptpartei. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Europäisches Prozessrecht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-verfahrensrouting`](skills/kaltstart-verfahrensrouting/SKILL.md) | Routet unionsprozessuale Mandate schnell auf Vorlage, Nichtigkeitsklage, Untätigkeit, Vertragsverletzung, Amtshaftung, einstweiligen Rechtsschutz oder Rechtsmittel und liefert sofort Fristen-, Zuständigkeits- und Dokumentenplan. |
| [`klagebefugnis-private-plaumann`](skills/klagebefugnis-private-plaumann/SKILL.md) | Prüft individuelle und unmittelbare Betroffenheit Privater nach Art. 263 AEUV, einschließlich Plaumann-Linie, regulatorischer Akt, Durchführungsmaßnahmen und Belegstrategie. |
| [`kosten-und-prozessrisiko`](skills/kosten-und-prozessrisiko/SKILL.md) | Erstellt Kosten-, Dauer- und Risikomatrix für unionsprozessuale Verfahren, inklusive Vergleichsfenster, reputationssensibler Punkte und Folgeentscheidungen. |
| [`muendliche-verhandlung-plaedoyer`](skills/muendliche-verhandlung-plaedoyer/SKILL.md) | Bereitet mündliche Verhandlung, Richterfragen, Minutenplan, Sprachfassung, Replikpunkte und Entscheidungsbitten vor, ohne die schriftliche Linie zu verlassen. |
| [`rechtsmittel-eug-eugh`](skills/rechtsmittel-eug-eugh/SKILL.md) | Prüft Rechtsmittel gegen Urteile des Gerichts der Europäischen Union: Rechtsfragen, Zulässigkeit, Klagegründe, keine neue Tatsacheninstanz, Frist und Antrag. |
| [`schriftsatzbau-eugh-eug`](skills/schriftsatzbau-eugh-eug/SKILL.md) | Erstellt Klage, Klagebeantwortung, Streithilfeschriftsatz, Rechtsmittel, Antrag auf einstweilige Anordnung und mündliche Notes im Stil der Unionsgerichte. |
| [`untatigkeitsklage-art-265`](skills/untatigkeitsklage-art-265/SKILL.md) | Bereitet Untätigkeitsklagen gegen Organe, Einrichtungen und sonstige Stellen der Union vor, mit Aufforderung zum Tätigwerden, Fristenkontrolle, Rechtsschutzbedürfnis und Antragsfassung. |
| [`urteilsauswertung-folgeverfahren`](skills/urteilsauswertung-folgeverfahren/SKILL.md) | Wertet EuGH- und EuG-Entscheidungen in Umsetzungsplan, nationales Folgeverfahren, Vollzug, Kommunikation und weitere Rechtsmitteloptionen aus. |
| [`vergleich-ruecknahme-erledigung`](skills/vergleich-ruecknahme-erledigung/SKILL.md) | Prüft prozessuale Beendigung: Rücknahme, Erledigung, Vergleichslösung, Kostenfolge, Wiederholungsrisiko und Kommunikation mit Gericht oder Gegenseite. |
| [`vertragsverletzung-art-258-260`](skills/vertragsverletzung-art-258-260/SKILL.md) | Ordnet Vertragsverletzungsverfahren nach Art. 258 bis 260 AEUV: Kommissionsbeschwerde, Vorverfahren, mit Gründen versehene Stellungnahme, Klage, Zwangsgeld und strategische Parallelverfahren. |
| [`vertraulichkeit-beweis-anlagen`](skills/vertraulichkeit-beweis-anlagen/SKILL.md) | Steuert vertrauliche Fassungen, Anlagenverzeichnis, Geschäftsgeheimnisse, Beweisangebote, Aktenauszüge und Schwärzungen in Verfahren vor Gerichtshof, Gericht und Beschwerdekammern. Aktivieren bei e-Curia-Einreichung, Art.-103-Vertraulich... |
| [`vorlage-transfer-eug-2024`](skills/vorlage-transfer-eug-2024/SKILL.md) | Berücksichtigt die seit 2024 praktisch wichtige Verteilung bestimmter Vorabentscheidungsbereiche zwischen Gerichtshof und Gericht und baut eine Zuständigkeits- und Transferprüfung ein. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
