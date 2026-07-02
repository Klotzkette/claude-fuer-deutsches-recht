# Urteilsbauer und Relationsmacher

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Urteils- und Beschluss-Werkstatt für Amts- Land- und Familienrichter sowie Rechtspfleger. Aktenintake Relation Beweiswürdigung mit Richter-Input Tatbestandsmerkmale Tenor Tatbestand Entscheidungsgründe Rechtsmittelbelehrung. Erzeugt DOCX nach Paragraf 313 ZPO.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`urteilsbauer-relationsmacher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/urteilsbauer-relationsmacher.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/urteilsbauer-relationsmacher/urteilsbauer-relationsmacher-werkstatt.md" download><code>urteilsbauer-relationsmacher-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/urteilsbauer-relationsmacher/urteilsbauer-relationsmacher-schnellstart.md" download><code>urteilsbauer-relationsmacher-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Solis Vision X Smartglasses: [Gesamt-PDF](../testakten/solis-vision-x-smartglasses/gesamt-pdf/solis-vision-x-smartglasses_gesamt.pdf), [`testakte-solis-vision-x-smartglasses.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-solis-vision-x-smartglasses.zip), [`testakte-solis-vision-x-smartglasses-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-solis-vision-x-smartglasses-einzelpdfs.zip); Werklohnklage Radarwarner GmbH ./. Schreinmoor Bauträger AG — Rohbaumängel Wohnanlage Spreebogen Plagwitz, Hilfsaufrechnung, Beweiswürdigung SV-Gutachten, Urteil Paragraf 313 ZPO: [Gesamt-PDF](../testakten/urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil/gesamt-pdf/urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil_gesamt.pdf), [`testakte-urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil.zip), [`testakte-urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-urteilsbau-zivilkammer-leipzig-werklohn-radarwarner-relation-mit-beweiswuerdigung-und-urteil-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine Gerichtsakte blitzschnell in ihre Bestandteile zergliedern und daraus einen Urteils- oder Beschlussentwurf nach Paragraf 313 ZPO bauen.
Technischer Plugin-Name: `urteilsbauer-relationsmacher`.

Freistehendes Plugin für **Amts-, Land- und Familienrichter sowie Rechtspfleger**. Begleitet von der Aktenintake über die Relation und die Beweiswürdigung mit Richter-Input bis zum fertigen Urteil oder Beschluss inklusive Tenor, Tatbestand, Entscheidungsgründen, Kosten- und Rechtsmittelbelehrung. Erzeugt am Ende ein DOCX nach § 313 ZPO.

## Installation

1. Plugin-Umgebung öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `urteilsbauer-relationsmacher.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte die Relation fuer eine Werklohnklage. Akte liegt vor.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install urteilsbauer-relationsmacher@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Skill-Landkarte

| Skill | Zweck |
| --- | --- |
| `aktenintake-zivil` | Erfasst Parteien, Anträge, Sachverhalt, Streitwert, Anlagen und Lage. |
| `zulaessigkeit-pruefen` | Pruft Statthaftigkeit, Zuständigkeit, Partei- und Prozessfähigkeit, Rechtsschutzbedürfnis. |
| `relation-zivil` | Baut Relation aus Klagegrund und Verteidigung mit Streitstand und Beweislage. |
| `vollrelation-langfassung` | Liefert die ausführliche Vollrelation mit Hilfserwaegungen und Eventualbegründung. |
| `anspruchsgrundlagen-pruefen` | Identifiziert und subsumiert die einschlaegigen Anspruchsgrundlagen. |
| `kollidierende-agb-pruefen` | Loest AGB-Konflikt nach Restguelitgkeits- und Knock-out-Doktrin. |
| `cisg-pruefen` | Pruft CISG-Anwendbarkeit, Anspruechs- und Aufrechnungslage. |
| `internationales-privatrecht` | Klärt anwendbares Recht nach Rom I/II und nationalem IPR. |
| `incoterms-und-gefahruebergang` | Wendet Incoterms 2020 auf Gefahrübergang und Transportkosten an. |
| `dsgvo-rechtswidriges-produkt` | Beurteilt DSGVO-Verstöße durch Produkte mit Datenverarbeitung. |
| `familienrichter-spezifika` | Familienrechtliche Besonderheiten: FamFG-Verfahren, Anhörungspflicht, Vergleichsdruck. |
| `beweisbeschluss-vorbereiten` | Formuliert Beweisthemen, Beweismittel und Beweisanordnung. |
| `beweiswuerdigung-mit-richter-input` | Holt Richter-Input zu Glaubwürdigkeit ein und baut Beweiswürdigung. |
| `tatbestand-zivil-schreiben` | Verfasst Tatbestand mit unstreitigem und streitigem Sachverhalt und Anträgen. |
| `entscheidungsgruende-zivil-schreiben` | Baut Entscheidungsgründe mit Subsumtion und juristischer Begründung. |
| `tenor-bauen-zivil` | Erstellt Tenor mit Hauptsache, Kosten, vorläufiger Vollstreckbarkeit. |
| `kostenentscheidung-bauen` | Berechnet Kostenquote nach §§ 91 ff. ZPO inklusive Vergleichswerten. |
| `vorlaeufige-vollstreckbarkeit` | Setzt Sicherheitsleistung und Abwendungsbefugnis nach §§ 708 ff. ZPO. |
| `rechtsmittelbelehrung-zivil` | Erzeugt korrekte Rechtsmittelbelehrung für Berufung, Beschwerde, Revision. |
| `beschluss-bauen-zpo` | Baut Beschlüsse statt Urteilen, etwa bei einstweiligem Rechtsschutz oder Streitwertfestsetzung. |
| `berufungsfest-pruefen` | Pruft das Urteil auf Berufungsfestigkeit und typische Aufhebungsgründe. |
| `revisionsfest-pruefen` | Pruft Urteil auf revisionsrechtliche Schwachstellen. |
| `dokumente-rendern-urteil-docx` | Rendert das fertige Urteil als DOCX nach § 313 ZPO. |
| `schulung-urteilsbauer` | Trainingsskill zur Einarbeitung neuer Richter und Rechtspfleger. |

## Typische Workflows

- Aktenintake -> Zulässigkeit -> Relation -> Anspruchsgrundlagen -> Beweisbeschluss.
- Beweiswürdigung mit Richter-Input -> Tatbestand -> Entscheidungsgründe -> Tenor.
- Kostenentscheidung -> Vorläufige Vollstreckbarkeit -> Rechtsmittelbelehrung.
- Berufungs-/Revisionsfestigkeit -> DOCX-Rendering nach § 313 ZPO.

## Haftung

Dieses Plugin ist ein Arbeitswerkzeug für die richterliche Praxis. Es ersetzt keine eigene rechtliche Prüfung und keine Beratung durch zugelassene Rechtsanwälte. Die Verantwortung für Tenor, Tatbestand und Entscheidungsgründe bleibt beim Spruchkoerper.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `aktenintake-schriftsatz-brief-und-memo-bausteine`, `aktenintake-zivil`, `amts-aktenintake-zivil-anspruchsgrundlagen`, `anschluss-routing`, `dokumente-intake`, `einstieg-routing`, `kaltstart-triage`, `schulung-urteilsbauer-aktenintake-beschluss`, `urteils-erstpruefung-und-mandatsziel`, `urteilsbauer-aktenintake-schriftsatz-brief-memo-bausteine`, `urteilsbauer-relation-start-chronologie-fristen`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `berufungsfest-beschluss-bauen-beweisbeschluss`, `beschluss-tatbestand-beweis-und-belege`, `beweisbeschluss-vorbereiten`, `beweiswuerdigung-mit-richter-input`, `beweiswuerdigung-quellenkarte`, `beweiswuerdigung-richter-cisg-dsgvo`, `chronologie-und-belegmatrix`, `dokumente-rendern-urteil-docx`, `input-compliance-dokumentation`, `input-compliance-dokumentation-und-akte`, `land-dokumentenmatrix-lueckenliste`, `quellen-livecheck`, `spezial-beweiswuerdigung-livequellen-und-rechtsprechungscheck`, `spezial-input-compliance-dokumentation-und-akte`, `tatbestand-formular-portal-und-einreichung`, `unterlagen-luecken`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `anspruchsgrundlagen-pruefen`, `beschluss-tatbestandsmerkmale`, `familienrichter-risikoampel`, `familienrichter-risikoampel-und-gegenargumente`, `fristen-und-risikoampel`, `tatbestand-zivil-schreiben`, `tatbestandsmerkmale-interessen`, `tatbestandsmerkmale-interessen-tenor-urteils`, `urb-tatbestand-entscheidungsgruende-leitfaden`, `urteils-erstpruefung-rollenklaerung` |
| 4. Gestaltung, Strategie und Verhandlung | `relation-verhandlung-vergleich`, `relation-verhandlung-vergleich-und-eskalation` |
| 5. Verfahren, Behörde und Gericht | `amts-fristen-form-zustaendigkeit`, `beschluss-bauen-zpo`, `rechtspfleger-behoerden-gericht-und-registerweg`, `rechtspfleger-behoerden-gerichts`, `schulung-urteilsbauer`, `urb-versaeumnisurteil-einspruch-spezial` |
| 6. Ergebnis, Schreiben und Kommunikation | `entscheidungsgruende-redaktion`, `entscheidungsgruende-redaktion-02`, `entscheidungsgruende-zivil-schreiben`, `output-waehlen`, `zivil-schreiben-tenor-bauen-urb-mehrere` |
| 7. Kontrolle, Qualität und Gegenprüfung | `entscheidungsgruende-fehlerkatalog`, `spezial-entscheidungsgruende-red-team-und-qualitaetskontrolle`, `urb-mehrere-streitgegenstaende-spezial` |
| 8. Spezialmodule und Schnittstellen | `99-finale-entscheidung-volltext`, `berufungsfest-pruefen`, `cisg-pruefen`, `dsgvo-rechtswidriges-produkt`, `entscheidungsgruende-zivil-familienrichter`, `familienrichter-spezifika`, `incoterms-und-gefahruebergang`, `internationales-privatrecht`, `internationales-privatrecht-kollidierende-agb`, `kollidierende-agb-pruefen`, `kostenentscheidung-bauen`, `land-rechtspfleger-relation`, `rechtsmittelbelehrung-zivil`, `rechtsmittelbelehrung-zivil-relation`, `relation-zivil`, `revisionsfest-pruefen`, `richter-richterlicher-hinweis`, `richter-zahlen-schwellenwerte`, ... plus 11 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 84 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `99-finale-entscheidung-volltext` | Wenn es um Finale Entscheidung als Volltext (Urteil oder Beschluss universell) in Urteilsbauer und Relationsmacher geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Koll... |
| `aktenintake-schriftsatz-brief-und-memo-bausteine` | Wenn es um Aktenintake: Schriftsatz-, Brief- und Memo-Bausteine in Urteilsbauer und Relationsmacher geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründun... |
| `aktenintake-zivil` | Wenn es um Aktenintake Zivilprozess in Urteilsbauer und Relationsmacher geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `amts-aktenintake-zivil-anspruchsgrundlagen` | Wenn es um Amts: Fristen, Form, Zuständigkeit und Rechtsweg in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstic... |
| `amts-fristen-form-zustaendigkeit` | Wenn es um Amts: Fristen, Form, Zuständigkeit und Rechtsweg in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstic... |
| `anschluss-routing` | Wenn es um Anschluss-Routing in Urteilsbauer und Relationsmacher geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anspruchsgrundlagen-pruefen` | Wenn es um Anspruchsgrundlagen-Prüfung in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `berufungsfest-beschluss-bauen-beweisbeschluss` | Wenn es um Berufungsfestigkeit prüfen in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Berufungsfest B... |
| `berufungsfest-pruefen` | Wenn es um Berufungsfestigkeit prüfen in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Berufungsfest P... |
| `beschluss-bauen-zpo` | Wenn es um Beschluss bauen — Zivilprozess in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beschluss-tatbestand-beweis-und-belege` | Wenn es um Beschluss: Tatbestandsmerkmale, Beweisfragen und Beleglage in Urteilsbauer und Relationsmacher geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `beschluss-tatbestandsmerkmale` | Wenn es um Beschluss: Tatbestandsmerkmale, Beweisfragen und Beleglage in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beweisbeschluss-vorbereiten` | Wenn es um Beweisbeschluss vorbereiten in Urteilsbauer und Relationsmacher geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| `beweiswuerdigung-mit-richter-input` | Wenn es um Beweiswürdigung mit haendischem Richter-Input in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwo... |
| `beweiswuerdigung-quellenkarte` | Wenn es um Beweiswuerdigung Quellenkarte in Urteilsbauer und Relationsmacher geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `beweiswuerdigung-richter-cisg-dsgvo` | Wenn es um Beweiswürdigung mit haendischem Richter-Input in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwo... |
| `chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `cisg-pruefen` | Wenn es um CISG-Prüfung in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `dokumente-intake` | Wenn es um Dokumentenintake in Urteilsbauer und Relationsmacher geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `dokumente-rendern-urteil-docx` | Wenn es um Urteil rendern - DOCX und PDF im Gerichtslayout in Urteilsbauer und Relationsmacher geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `dsgvo-rechtswidriges-produkt` | Wenn es um DSGVO-rechtswidriges Produkt in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einstieg-routing` | Wenn es um Einstieg und Routing in Urteilsbauer und Relationsmacher geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `entscheidungsgruende-fehlerkatalog` | Wenn es um Entscheidungsgruende Fehlerkatalog in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `entscheidungsgruende-redaktion` | Wenn es um Entscheidungsgründe redaktionell, beweisfest und berufungsfest bauen in Urteilsbauer und Relationsmacher geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. Auswah... |
| `entscheidungsgruende-redaktion-02` | Wenn es um Entscheidungsgründe redaktionell, beweisfest und berufungsfest bauen in Urteilsbauer und Relationsmacher geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. Auswah... |
| `entscheidungsgruende-zivil-familienrichter` | Wenn es um Entscheidungsgründe schreiben in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Entscheidung... |
| `entscheidungsgruende-zivil-schreiben` | Wenn es um Entscheidungsgründe schreiben in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Entscheidung... |
| `familienrichter-risikoampel` | Wenn es um Familienrichter: Risikoampel, Gegenargumente und Verteidigungslinien in Urteilsbauer und Relationsmacher geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sof... |
| `familienrichter-risikoampel-und-gegenargumente` | Wenn es um Familienrichter: Risikoampel, Gegenargumente und Verteidigungslinien in Urteilsbauer und Relationsmacher geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sof... |
| `familienrichter-spezifika` | Wenn es um Familienrichter Spezifika in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `incoterms-und-gefahruebergang` | Wenn es um Incoterms und Gefahrübergang in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `input-compliance-dokumentation` | Wenn es um Compliance-Dokumentation und Aktenvermerk (Urteilsbauer) in Urteilsbauer und Relationsmacher geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| `input-compliance-dokumentation-und-akte` | Wenn es um Compliance-Dokumentation und Akte (Urteilsbauer-Eingang) in Urteilsbauer und Relationsmacher geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| `internationales-privatrecht` | Wenn es um Internationales Privatrecht in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Internationale... |
| `internationales-privatrecht-kollidierende-agb` | Wenn es um Internationales Privatrecht in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Internationale... |
| `kaltstart-triage` | Wenn es um Kaltstart Triage in Urteilsbauer und Relationsmacher geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kollidierende-agb-pruefen` | Wenn es um Kollidierende AGB in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kostenentscheidung-bauen` | Wenn es um Kostenentscheidung in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `land-dokumentenmatrix-lueckenliste` | Wenn es um Land: Dokumentenmatrix, Lückenliste und Nachforderung in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `land-rechtspfleger-relation` | Wenn es um Land: Dokumentenmatrix, Lückenliste und Nachforderung in Urteilsbauer und Relationsmacher geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `output-waehlen` | Wenn es um Output wählen in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in Urteilsbauer und Relationsmacher geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `rechtsmittelbelehrung-zivil` | Wenn es um Rechtsmittelbelehrung Zivil in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Rechtsmittelbe... |
| `rechtsmittelbelehrung-zivil-relation` | Wenn es um Rechtsmittelbelehrung Zivil in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Rechtsmittelbe... |
| `rechtspfleger-behoerden-gericht-und-registerweg` | Wenn es um Rechtspfleger: Behörden-, Gerichts- oder Registerweg in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahl... |
| `rechtspfleger-behoerden-gerichts` | Wenn es um Rechtspfleger: Behörden-, Gerichts- oder Registerweg in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahl... |
| `relation-verhandlung-vergleich` | Wenn es um Relation: Verhandlung, Vergleich und Eskalation in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `relation-verhandlung-vergleich-und-eskalation` | Wenn es um Relation: Verhandlung, Vergleich und Eskalation in Urteilsbauer und Relationsmacher geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `relation-zivil` | Wenn es um Relation Zivilprozess - Vollrelation nach deutschem Standard in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `revisionsfest-pruefen` | Wenn es um Revisionsfestigkeit prüfen in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `richter-richterlicher-hinweis` | Wenn es um Richter: Zahlen, Schwellenwerte und Berechnung in Urteilsbauer und Relationsmacher geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfra... |
| `richter-zahlen-schwellenwerte` | Wenn es um Richter: Zahlen, Schwellenwerte und Berechnung in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `richterlicher-hinweis-aufklaerung` | Wenn es um Richterlicher Hinweis, Aufklärung und Parteivortrag in die Relation einbauen in Urteilsbauer und Relationsmacher geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Z... |
| `richterlicher-hinweis-und-aufklaerung` | Wenn es um Richterlicher Hinweis, Aufklärung und Parteivortrag in die Relation einbauen in Urteilsbauer und Relationsmacher geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Z... |
| `schulung-urteilsbauer` | Wenn es um Trainer-Leitfaden Schulung Urteilsbauer in Urteilsbauer und Relationsmacher geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwor... |
| `schulung-urteilsbauer-aktenintake-beschluss` | Wenn es um Trainer-Leitfaden Schulung Urteilsbauer in Urteilsbauer und Relationsmacher geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwor... |
| `spezial-beweiswuerdigung-livequellen-und-rechtsprechungscheck` | Wenn es um Beweiswuerdigung: Livequellen- und Rechtsprechungscheck in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-entscheidungsgruende-red-team-und-qualitaetskontrolle` | Wenn es um Entscheidungsgruende: Red-Team und Qualitätskontrolle in Urteilsbauer und Relationsmacher geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-input-compliance-dokumentation-und-akte` | Wenn es um Input: Compliance-Dokumentation und Aktenvermerk in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tatbestand-formular-portal-und-einreichung` | Wenn es um Tatbestand: Formular, Portal und Einreichungslogik in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `tatbestand-zivil-schreiben` | Wenn es um Tatbestand schreiben in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Tatbestand Zivil Schr... |
| `tatbestandsmerkmale-interessen` | Wenn es um Tatbestandsmerkmale: Mehrparteienkonflikt und Interessenmatrix in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritte... |
| `tatbestandsmerkmale-interessen-tenor-urteils` | Wenn es um Tatbestandsmerkmale: Mehrparteienkonflikt und Interessenmatrix in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritte... |
| `tenor-bauen-zivil` | Wenn es um Tenor bauen Zivilurteil in Urteilsbauer und Relationsmacher geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `tenor-internationaler-bezug` | Wenn es um Tenor: Internationaler Bezug und Schnittstellen in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstich... |
| `tenor-internationaler-bezug-und-schnittstellen` | Wenn es um Tenor: Internationaler Bezug und Schnittstellen in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstich... |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in Urteilsbauer und Relationsmacher geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `urb-mehrere-streitgegenstaende-spezial` | Wenn es um Urb: Mehrere Streitgegenstaende in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `urb-relationstechnik-bauleiter` | Wenn es um Urb: Relationstechnik Bauleiter in Urteilsbauer und Relationsmacher geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. A... |
| `urb-relationstechnik-entscheidungsgruende` | Wenn es um Urb: Relationstechnik Bauleiter in Urteilsbauer und Relationsmacher geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. A... |
| `urb-tatbestand-entscheidungsgruende-leitfaden` | Wenn es um Urb: Tatbestand Gruende in Urteilsbauer und Relationsmacher geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `urb-versaeumnisurteil-einspruch-spezial` | Wenn es um Urb: Versaeumnisurteil Einspruch in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `urteils-erstpruefung-rollenklaerung` | Wenn es um Urteils: Erstprüfung, Rollenklärung und Mandatsziel in Urteilsbauer und Relationsmacher geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten... |
| `urteils-erstpruefung-und-mandatsziel` | Wenn es um Urteils: Erstprüfung, Rollenklärung und Mandatsziel in Urteilsbauer und Relationsmacher geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten... |
| `urteilsbauer-aktenintake-schriftsatz-brief-memo-bausteine` | Wenn es um Aktenintake: Schriftsatz-, Brief- und Memo-Bausteine in Urteilsbauer und Relationsmacher geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründun... |
| `urteilsbauer-relation-start-chronologie-fristen` | Wenn es um Urteilsbauer und Relationsmacher — Allgemein in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `vollrelation-langfassung` | Wenn es um Vollrelation Langfassung - Schulstandard für Prüfung in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahl... |
| `vollrelation-langfassung-vorlaeufige` | Wenn es um Vollrelation Langfassung - Schulstandard für Prüfung in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahl... |
| `vorlaeufige-vollstreckbarkeit` | Wenn es um Vorläufige Vollstreckbarkeit in Urteilsbauer und Relationsmacher geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in Urteilsbauer und Relationsmacher geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in Urteilsbauer und Relationsmacher geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `zivil-schreiben-tenor-bauen-urb-mehrere` | Wenn es um Tatbestand schreiben in Urteilsbauer und Relationsmacher geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Zivil Schreiben Tenor... |
| `zulaessigkeit-pruefen` | Wenn es um Zulässigkeit der Zivilklage in Urteilsbauer und Relationsmacher geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
