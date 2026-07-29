# Bauträgervertrag-Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Bauträgervertrag-Prüfer aus Verbrauchersicht: MaBV, Paragrafen 650u/650v BGB, Paragraf 650m Abs. 2 BGB, AGB, Baubeschreibung, Abnahme, Schlussrate, WEG, Vormerkung, Lastenfreistellung und Drei-Dokumente-Ausgabe.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/bautraegervertrag-pruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`bautraegervertrag-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertrag-pruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/bautraegervertrag-pruefer/bautraegervertrag-pruefer-werkstatt.md" download><code>bautraegervertrag-pruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/bautraegervertrag-pruefer/bautraegervertrag-pruefer-schnellstart.md" download><code>bautraegervertrag-pruefer-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Bauträgervertrag Birkenpfuhl - Wohnung 4.27](../testakten/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung/README.md) | [Gesamt-PDF](../testakten/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung/gesamt-pdf/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung_gesamt.pdf) | [`testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung.zip) | [`testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Bauträgervertrag aus Verbrauchersicht prüfen und ein direkt verwendbares Drei-Dokumente-Paket für Mandant, Bauträger und Notar erhalten.
Eigenes Plugin für die verbraucherseitige Prüfung deutscher Bauträgerverträge über Wohnungen, Häuser, Tiefgaragenstellplätze und Sondernutzungsrechte. Das Plugin arbeitet aus Sicht der Käuferin oder des Käufers: Es soll einen Notarentwurf, eine beurkundete Urkunde oder eine chaotische Mandatsakte so auswerten, dass MaBV-Zahlungen, Sicherheiten, AGB-Klauseln, Baubeschreibung, Abnahme, Teilungserklärung, Eigentumssicherung und Verhandlungsstrategie nicht nebeneinander liegen bleiben, sondern in ein belastbares Mandatsprodukt münden.

Der Kern ist aus dem langen Bauträgervertrag-Prüfer-Skill übernommen und fachlich verdichtet. Der ursprüngliche One-Shot-Gedanke bleibt erhalten: Wenn ein Vertrag oder Aktenordner vorliegt, startet die Prüfung aus dem Dokument heraus, bildet zuerst einen Fall-Fingerabdruck und stellt nur solche Rückfragen, ohne die die Bewertung objektiv falsch würde. Daneben sind die Arbeitsabschnitte als eigene Skills vorhanden, damit Plugin-Umgebung/Cowork gezielt den passenden Teil laden kann.

**Schwester-Plugin:** [`bautraegervertragspruefer`](../bautraegervertragspruefer) deckt dasselbe Mandat mit eigenem Megaprompt-Original und zwei Testakten ab; dieses Plugin hier bietet einzeln ladbare Spezial-Skills samt references-Workflow (Komplettliste unten). Für ein Mandat genügt eines von beiden.

## Wofür dieses Plugin gedacht ist

- Vorprüfung eines Bauträgervertragsentwurfs vor dem Notartermin aus Verbrauchersicht.
- Prüfung einer bereits beurkundeten Urkunde, wenn Raten, Baufortschritt, Sonderwünsche, Abnahme oder Schlussrate streitig werden.
- Aufbereitung einer Mandantenakte mit Teilungserklärung, Baubeschreibung, Ratenplan, Freistellungserklärung, Baugrund-/Technikunterlagen und E-Mail-Verkehr.
- Erstellung eines Drei-Dokumente-Pakets: kurzes Mandantenanschreiben, ausführliches Mandantengutachten und außergerichtliches Aufforderungsschreiben an Bauträger/Notariat mit konkreten Änderungsfassungen.

## Arbeitsweise

1. **Fall-Fingerabdruck:** Urkunde, Parteien, Einheit, Projekt, Preis, Ratenplan, Sicherheiten, Baubeschreibung, Teilungserklärung, Technik, WEG-Organisation und Streitstand werden aus der Akte gezogen.
2. **Pflicht-Prüfblock:** § 650u/§ 650v BGB, § 650m Abs. 2 BGB, §§ 3, 7, 12 MaBV, §§ 305 ff. BGB, Abnahme Gemeinschaftseigentum, Schlussrate und Eigentumssicherung werden immer zuerst geprüft.
3. **Klauselmatrix:** Jede problematische Klausel wird mit Originalwortlaut, Risiko, Normanker, Rechtsprechungsanker, Gegenargument und gewünschter Neufassung erfasst.
4. **Drei-Dokumente-Ausgabe:** Das Ergebnis wird nicht als lose Stichwortliste stehen gelassen, sondern in ausformulierte, verwendbare Texte überführt.

## Quellenhygiene

Rechtsprechung wird nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle verwendet. Zulässige Startquellen sind insbesondere offizielle Bundes-/Landesgerichtsseiten, `rechtsprechung-im-internet.de`, `rechtsinformationen.bund.de`, `dejure.org` und `openjur.de`. BeckRS-, juris-, Kommentar- und Aufsatzfundstellen werden nicht als Beleg zitiert.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Umgebung oder Cowork → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Bei einer Prüfung zusätzlich die Testakte oder eigene Vertragsunterlagen als PDF/DOCX/Markdown hochladen.

> Hinweis: Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`fall-fingerabdruck-und-schnelltriage`](skills/fall-fingerabdruck-und-schnelltriage/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`agb-klauselkontrolle-beweislast-und-tatsachenbestaetigung`](skills/agb-klauselkontrolle-beweislast-und-tatsachenbestaetigung/SKILL.md), [`kfw-geg-foerderung-und-unterlagenpflicht-650n`](skills/kfw-geg-foerderung-und-unterlagenpflicht-650n/SKILL.md), [`mabv-agb-klauselmatrix-rot-orange-gruen`](skills/mabv-agb-klauselmatrix-rot-orange-gruen/SKILL.md), [`mabv-ratenplan-sicherheiten-und-notaranderkonto`](skills/mabv-ratenplan-sicherheiten-und-notaranderkonto/SKILL.md), [`quellenhygiene-rechtsprechungsanker-und-bughunt`](skills/quellenhygiene-rechtsprechungsanker-und-bughunt/SKILL.md), [`verbraucherbauvertrag-650i-650u-widerruf-und-unterlagen`](skills/verbraucherbauvertrag-650i-650u-widerruf-und-unterlagen/SKILL.md), [`verhandlung-drei-dokumente-paket`](skills/verhandlung-drei-dokumente-paket/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`geschaeftsfuehrer-architekt-und-bautenstandshaftung`](skills/geschaeftsfuehrer-architekt-und-bautenstandshaftung/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`notarhaftung-belehrung-und-streitverkuendung`](skills/notarhaftung-belehrung-und-streitverkuendung/SKILL.md), [`workflow-one-shot-verbraucherpruefung`](skills/workflow-one-shot-verbraucherpruefung/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`bauzeit-verzug-vertragsstrafe-und-hoehere-gewalt`](skills/bauzeit-verzug-vertragsstrafe-und-hoehere-gewalt/SKILL.md), [`nachzuegler-altbau-sanierung-und-kaufrecht-werkrecht`](skills/nachzuegler-altbau-sanierung-und-kaufrecht-werkrecht/SKILL.md), [`prozessstrategie-zahlung-feststellung-und-vorschuss`](skills/prozessstrategie-zahlung-feststellung-und-vorschuss/SKILL.md), [`unwirksame-abnahmeklauseln-dreissig-jahre-und-nachholung`](skills/unwirksame-abnahmeklauseln-dreissig-jahre-und-nachholung/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`beurkundung-verbraucherfrist-notar-und-bezugsurkunden`](skills/beurkundung-verbraucherfrist-notar-und-bezugsurkunden/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`abnahme-gemeinschaftseigentum-schlussrate-und-maengelrechte`](skills/abnahme-gemeinschaftseigentum-schlussrate-und-maengelrechte/SKILL.md), [`baubeschreibung-bausoll-und-wohnflaeche`](skills/baubeschreibung-bausoll-und-wohnflaeche/SKILL.md), [`baugruppen-gbr-beurkundung-mopeg-und-mabv-abgrenzung`](skills/baugruppen-gbr-beurkundung-mopeg-und-mabv-abgrenzung/SKILL.md), [`din-anerkannte-regeln-technik-und-standardwechsel`](skills/din-anerkannte-regeln-technik-und-standardwechsel/SKILL.md), [`druckmuster-schluessel-vormerkung-und-zahlung`](skills/druckmuster-schluessel-vormerkung-und-zahlung/SKILL.md), [`eigentumssicherung-vormerkung-lastenfreistellung-und-insolvenz`](skills/eigentumssicherung-vormerkung-lastenfreistellung-und-insolvenz/SKILL.md), [`hoai-technik-baugrund-und-objektueberwachung`](skills/hoai-technik-baugrund-und-objektueberwachung/SKILL.md), [`preisanpassung-315-saldierung-und-loesungsrecht`](skills/preisanpassung-315-saldierung-und-loesungsrecht/SKILL.md), [`sicherheit-650m-fuenf-prozent-einbehalt-und-buergschaft`](skills/sicherheit-650m-fuenf-prozent-einbehalt-und-buergschaft/SKILL.md), [`sonderwuensche-preisanpassung-und-ausstattungswahl`](skills/sonderwuensche-preisanpassung-und-ausstattungswahl/SKILL.md), [`verzugsschadenspositionen-berechnung-und-zinsen`](skills/verzugsschadenspositionen-berechnung-und-zinsen/SKILL.md), [`vollstaendige-fertigstellung-schlussrate-und-aussenanlagen`](skills/vollstaendige-fertigstellung-schlussrate-und-aussenanlagen/SKILL.md), [`wohnflaeche-toleranz-methode-und-minderung`](skills/wohnflaeche-toleranz-methode-und-minderung/SKILL.md), [`wohnungseigentum-teilungserklaerung-und-erstverwalter`](skills/wohnungseigentum-teilungserklaerung-und-erstverwalter/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 31 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`abnahme-gemeinschaftseigentum-schlussrate-und-maengelrechte`](skills/abnahme-gemeinschaftseigentum-schlussrate-und-maengelrechte/SKILL.md) | Wenn es um Abnahme, Gemeinschaftseigentum, Schlussrate und Mängelrechte in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkt... |
| [`agb-klauselkontrolle-beweislast-und-tatsachenbestaetigung`](skills/agb-klauselkontrolle-beweislast-und-tatsachenbestaetigung/SKILL.md) | Wenn es um AGB-Klauselkontrolle, Beweislast und Tatsachenbestätigung in Bauträgervertrag-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`baubeschreibung-bausoll-und-wohnflaeche`](skills/baubeschreibung-bausoll-und-wohnflaeche/SKILL.md) | Wenn es um Baubeschreibung, Bausoll und Wohnfläche in Bauträgervertrag-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`baugruppen-gbr-beurkundung-mopeg-und-mabv-abgrenzung`](skills/baugruppen-gbr-beurkundung-mopeg-und-mabv-abgrenzung/SKILL.md) | Wenn es um Baugruppen-GbR, Beurkundung, MoPeG und MaBV-Abgrenzung in Bauträgervertrag-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bauzeit-verzug-vertragsstrafe-und-hoehere-gewalt`](skills/bauzeit-verzug-vertragsstrafe-und-hoehere-gewalt/SKILL.md) | Wenn es um Bauzeit, Verzug, Vertragsstrafe und höhere Gewalt in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken... |
| [`beurkundung-verbraucherfrist-notar-und-bezugsurkunden`](skills/beurkundung-verbraucherfrist-notar-und-bezugsurkunden/SKILL.md) | Wenn es um Beurkundung, Verbraucherfrist, Notar und Bezugsurkunden in Bauträgervertrag-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`din-anerkannte-regeln-technik-und-standardwechsel`](skills/din-anerkannte-regeln-technik-und-standardwechsel/SKILL.md) | Wenn es um DIN, anerkannte Regeln der Technik und Standardwechsel in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumen... |
| [`druckmuster-schluessel-vormerkung-und-zahlung`](skills/druckmuster-schluessel-vormerkung-und-zahlung/SKILL.md) | Wenn es um Druckmuster, Schlüssel, Vormerkung und Zahlung in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| [`eigentumssicherung-vormerkung-lastenfreistellung-und-insolvenz`](skills/eigentumssicherung-vormerkung-lastenfreistellung-und-insolvenz/SKILL.md) | Wenn es um Eigentumssicherung, Vormerkung, Lastenfreistellung und Insolvenz in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfp... |
| [`fall-fingerabdruck-und-schnelltriage`](skills/fall-fingerabdruck-und-schnelltriage/SKILL.md) | Wenn es um Fall-Fingerabdruck und Schnelltriage in Bauträgervertrag-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| [`geschaeftsfuehrer-architekt-und-bautenstandshaftung`](skills/geschaeftsfuehrer-architekt-und-bautenstandshaftung/SKILL.md) | Wenn es um Geschäftsführer-, Architekten- und Bautenstandshaftung in Bauträgervertrag-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`hoai-technik-baugrund-und-objektueberwachung`](skills/hoai-technik-baugrund-und-objektueberwachung/SKILL.md) | Wenn es um HOAI, Technik, Baugrund und Objektüberwachung in Bauträgervertrag-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Bauträgervertrag Prüfer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kfw-geg-foerderung-und-unterlagenpflicht-650n`](skills/kfw-geg-foerderung-und-unterlagenpflicht-650n/SKILL.md) | Wenn es um KfW/GEG, Förderung und Unterlagenpflicht Paragraf 650n BGB in Bauträgervertrag-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`mabv-agb-klauselmatrix-rot-orange-gruen`](skills/mabv-agb-klauselmatrix-rot-orange-gruen/SKILL.md) | Wenn es um MaBV-/AGB-Klauselmatrix Rot-Orange-Grün in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| [`mabv-ratenplan-sicherheiten-und-notaranderkonto`](skills/mabv-ratenplan-sicherheiten-und-notaranderkonto/SKILL.md) | Wenn es um MaBV-Ratenplan, Sicherheiten und Notaranderkonto in Bauträgervertrag-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nachzuegler-altbau-sanierung-und-kaufrecht-werkrecht`](skills/nachzuegler-altbau-sanierung-und-kaufrecht-werkrecht/SKILL.md) | Wenn es um Nachzügler, Altbau, Sanierung und Kaufrecht/Werkrecht in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Ris... |
| [`notarhaftung-belehrung-und-streitverkuendung`](skills/notarhaftung-belehrung-und-streitverkuendung/SKILL.md) | Wenn es um Notarhaftung, Belehrung und Streitverkündung in Bauträgervertrag-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| [`preisanpassung-315-saldierung-und-loesungsrecht`](skills/preisanpassung-315-saldierung-und-loesungsrecht/SKILL.md) | Wenn es um Preisanpassung, Paragraf 315 BGB, Saldierung und Lösungsrecht in Bauträgervertrag-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nä... |
| [`prozessstrategie-zahlung-feststellung-und-vorschuss`](skills/prozessstrategie-zahlung-feststellung-und-vorschuss/SKILL.md) | Wenn es um Prozessstrategie Zahlung, Feststellung und Vorschuss in Bauträgervertrag-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anl... |
| [`quellenhygiene-rechtsprechungsanker-und-bughunt`](skills/quellenhygiene-rechtsprechungsanker-und-bughunt/SKILL.md) | Wenn es um Quellenhygiene, Rechtsprechungsanker und Bug-Hunt in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`sicherheit-650m-fuenf-prozent-einbehalt-und-buergschaft`](skills/sicherheit-650m-fuenf-prozent-einbehalt-und-buergschaft/SKILL.md) | Wenn es um Paragraf 650m-Sicherheit, Einbehalt und Bürgschaft in Bauträgervertrag-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`sonderwuensche-preisanpassung-und-ausstattungswahl`](skills/sonderwuensche-preisanpassung-und-ausstattungswahl/SKILL.md) | Wenn es um Sonderwünsche, Bemusterung und Ausstattungswahl in Bauträgervertrag-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`unwirksame-abnahmeklauseln-dreissig-jahre-und-nachholung`](skills/unwirksame-abnahmeklauseln-dreissig-jahre-und-nachholung/SKILL.md) | Wenn es um Unwirksame Abnahmeklauseln, 30-Jahres-Grenze und Nachholung in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkte... |
| [`verbraucherbauvertrag-650i-650u-widerruf-und-unterlagen`](skills/verbraucherbauvertrag-650i-650u-widerruf-und-unterlagen/SKILL.md) | Wenn es um Verbraucherbauvertrag, Bauträgervertrag, Widerruf und Unterlagen in Bauträgervertrag-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`verhandlung-drei-dokumente-paket`](skills/verhandlung-drei-dokumente-paket/SKILL.md) | Wenn es um Verhandlung und Drei-Dokumente-Paket in Bauträgervertrag-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`verzugsschadenspositionen-berechnung-und-zinsen`](skills/verzugsschadenspositionen-berechnung-und-zinsen/SKILL.md) | Wenn es um Verzugsschäden, Berechnung und Zinsen in Bauträgervertrag-Prüfer geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`vollstaendige-fertigstellung-schlussrate-und-aussenanlagen`](skills/vollstaendige-fertigstellung-schlussrate-und-aussenanlagen/SKILL.md) | Wenn es um Vollständige Fertigstellung, Schlussrate und Außenanlagen in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| [`wohnflaeche-toleranz-methode-und-minderung`](skills/wohnflaeche-toleranz-methode-und-minderung/SKILL.md) | Wenn es um Wohnfläche, Toleranz, Methode und Minderung in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`wohnungseigentum-teilungserklaerung-und-erstverwalter`](skills/wohnungseigentum-teilungserklaerung-und-erstverwalter/SKILL.md) | Wenn es um Wohnungseigentum, Teilungserklärung und Erstverwalter in Bauträgervertrag-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Ris... |
| [`workflow-one-shot-verbraucherpruefung`](skills/workflow-one-shot-verbraucherpruefung/SKILL.md) | Wenn es um One-Shot-Verbraucherprüfung Bauträgervertrag in Bauträgervertrag-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
