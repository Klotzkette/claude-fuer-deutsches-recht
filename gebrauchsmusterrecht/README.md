# gebrauchsmusterrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Eigenständiges Plugin für deutsches Gebrauchsmusterrecht: GebrMG, DPMA-Anmeldung, Recherche nach Paragraf 7 GebrMG, Abzweigung, Neuheitsschonfrist, Verletzung, Löschung, BPatG-Beschwerde, Lizenz, FTO und Schnellschutz für technische Produkte.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/gebrauchsmusterrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`gebrauchsmusterrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gebrauchsmusterrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gebrauchsmusterrecht/gebrauchsmusterrecht-werkstatt.md" download><code>gebrauchsmusterrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gebrauchsmusterrecht/gebrauchsmusterrecht-schnellstart.md" download><code>gebrauchsmusterrecht-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Schnellverschluss S-14: Sensorhalter, Gebrauchsmusterabzweigung und Messeoffenbarung](../testakten/gebrauchsmusterrecht-schnellverschluss-sensorhalter/README.md) | [Gesamt-PDF](../testakten/gebrauchsmusterrecht-schnellverschluss-sensorhalter/gesamt-pdf/gebrauchsmusterrecht-schnellverschluss-sensorhalter_gesamt.pdf) | [`testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter.zip) | [`testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin behandelt das deutsche Gebrauchsmuster als schnelles, ungeprüft eingetragenes technisches Schutzrecht. Es führt durch Anmeldung, Recherche, Abzweigung, Schutzfähigkeit, Verletzung und Löschung, ohne die gefährliche Abkürzung zu nehmen: Eintragung ist noch kein belastbarer Rechtsbestand.

## Arbeitsmodus

Der Einstieg ist bewusst niedrigschwellig: Uploads, Bilder, Verträge oder bloße Stichworte reichen. Das Plugin fragt zuerst nach den wenigen Punkten, die wirklich entscheiden: Frist, Produkt, Territorium, Registerstand, Veröffentlichungsdatum, Vertrag und gewünschter Output. Danach schlägt es passende Spezialskills aus diesem Plugin und angrenzenden Plugins vor.

## Praxisblöcke

| Block | Wofür? |
| --- | --- |
| Kaltstart | Technik, Produkt, Frist, Offenbarung, Patentbezug und Ziel klären |
| Anmeldung | Formalien, Ansprüche, Beschreibung, Zeichnungen, Abzweigung und Schonfrist |
| Rechtsbestand | Neuheit, erfinderischer Schritt, Ausschlüsse, Recherche und Löschung |
| Durchsetzung | Verletzung, eV, Abmahnung, Klage, Auskunft und Schadensersatz |
| Verwertung | Lizenzen, Übertragung, Insolvenz, Start-up-Strategie und internationale Alternativen |

## Quellen- und Zitierhygiene

- Offizielle Normtexte, Amtsinformationen und Register zuerst: keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate, keine Paywall-Literatur als scheinbare Quelle.
- Register-, Gebühren-, Formular- und Fristenfragen immer live prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugänglicher oder amtlicher Quelle verwenden.
- Bei ausländischem Recht Local-Counsel-Prüfbedarf offen kennzeichnen.

## Verhältnis zu anderen Plugins

- `markenrecht-fashion-luxus` für tiefe Marken-, Plattform- und Counterfeit-Fragen.
- `gewerblicher-rechtsschutz` und `fachanwalt-gewerblicher-rechtsschutz` für breiten IP-Kontext.
- `patentrecht` und `gebrauchsmusterrecht` für technische Schutzrechte.
- `produktrecht`, `ecommerce-recht` und `datenschutzrecht` für Produkt-, Shop- und Datenfragen.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`auslandsroute-kein-beschreibung-zeichnungen`](skills/auslandsroute-kein-beschreibung-zeichnungen/SKILL.md), [`gebrauchsmuster-kaltstart-interview`](skills/gebrauchsmuster-kaltstart-interview/SKILL.md), [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md), [`patent-oder-gebrauchsmuster-route`](skills/patent-oder-gebrauchsmuster-route/SKILL.md), [`stand-technik-startup-schnellschutz`](skills/stand-technik-startup-schnellschutz/SKILL.md), [`startup-schnellschutz`](skills/startup-schnellschutz/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`auskunft-schadensersatz-geheimhaltung`](skills/auskunft-schadensersatz-geheimhaltung/SKILL.md), [`besichtigung-beschlagnahme-und-beweissicherung`](skills/besichtigung-beschlagnahme-und-beweissicherung/SKILL.md), [`gutachten-rechtsbestand-insolvenz-verwertung`](skills/gutachten-rechtsbestand-insolvenz-verwertung/SKILL.md), [`recherche-nach-schutzgegenstand-ausschluesse`](skills/recherche-nach-schutzgegenstand-ausschluesse/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`anspruchsfassung-gebrauchsmuster`](skills/anspruchsfassung-gebrauchsmuster/SKILL.md), [`cross-license-verletzung-anspruchsmerkmale`](skills/cross-license-verletzung-anspruchsmerkmale/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`verletzung-anspruchsmerkmale`](skills/verletzung-anspruchsmerkmale/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`china-utility-model-vergleich`](skills/china-utility-model-vergleich/SKILL.md), [`lizenzvertrag-gebrauchsmuster`](skills/lizenzvertrag-gebrauchsmuster/SKILL.md), [`mandantenmemo-gebrauchsmusterstrategie`](skills/mandantenmemo-gebrauchsmusterstrategie/SKILL.md), [`muendliche-verhandlung-dpma`](skills/muendliche-verhandlung-dpma/SKILL.md), [`registerstand-aufrechterhaltung-lizenzvertrag`](skills/registerstand-aufrechterhaltung-lizenzvertrag/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`computerprogramm-verfahrensausschluss`](skills/computerprogramm-verfahrensausschluss/SKILL.md), [`einstweilige-verfuegung-fto-schutzbereich`](skills/einstweilige-verfuegung-fto-schutzbereich/SKILL.md), [`japan-utility-klageantraege-verletzung`](skills/japan-utility-klageantraege-verletzung/SKILL.md), [`klageantraege-verletzung`](skills/klageantraege-verletzung/SKILL.md), [`loeschungsantrag-dpma-mandantenmemo`](skills/loeschungsantrag-dpma-mandantenmemo/SKILL.md), [`neuheitsschonfrist-eigene-offenbarung`](skills/neuheitsschonfrist-eigene-offenbarung/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`qualitygate-gebrmg`](skills/qualitygate-gebrmg/SKILL.md), [`schutzgegenstand-und-ausschluesse`](skills/schutzgegenstand-und-ausschluesse/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`abmahnung-gebrauchsmuster-abzweigung`](skills/abmahnung-gebrauchsmuster-abzweigung/SKILL.md), [`abzweigung-aus-patentanmeldung`](skills/abzweigung-aus-patentanmeldung/SKILL.md), [`arbeitnehmererfindung-und-inhaberschaft`](skills/arbeitnehmererfindung-und-inhaberschaft/SKILL.md), [`beschreibung-und-zeichnungen`](skills/beschreibung-und-zeichnungen/SKILL.md), [`beschwerde-bpatg-besichtigung-beschlagnahme`](skills/beschwerde-bpatg-besichtigung-beschlagnahme/SKILL.md), [`chemie-biotech-china-utility`](skills/chemie-biotech-china-utility/SKILL.md), [`doppelschutz-patent-dpma-anmeldung`](skills/doppelschutz-patent-dpma-anmeldung/SKILL.md), [`dpma-anmeldung-formalien`](skills/dpma-anmeldung-formalien/SKILL.md), [`fto-und-schutzbereich`](skills/fto-und-schutzbereich/SKILL.md), [`geheimhaltung-vor-anmeldung`](skills/geheimhaltung-vor-anmeldung/SKILL.md), [`insolvenz-und-verwertung`](skills/insolvenz-und-verwertung/SKILL.md), [`local-counsel-loeschung-erwiderung`](skills/local-counsel-loeschung-erwiderung/SKILL.md), [`loeschung-erwiderung-inhaber`](skills/loeschung-erwiderung-inhaber/SKILL.md), [`messeveroeffentlichung-prototyp-muendliche`](skills/messeveroeffentlichung-prototyp-muendliche/SKILL.md), [`neuheit-erfinderischer-patent-gebrauchsmuster`](skills/neuheit-erfinderischer-patent-gebrauchsmuster/SKILL.md), [`prioritaet-anmeldetag-produktlaunch-neuheit`](skills/prioritaet-anmeldetag-produktlaunch-neuheit/SKILL.md), [`produktlaunch-und-neuheit`](skills/produktlaunch-und-neuheit/SKILL.md), [`technische-laborbuch-teilloeschung`](skills/technische-laborbuch-teilloeschung/SKILL.md), ... plus 6 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 51 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`abmahnung-gebrauchsmuster-abzweigung`](skills/abmahnung-gebrauchsmuster-abzweigung/SKILL.md) | Wenn es um Abmahnung Gebrauchsmuster Verteidigung in gebrauchsmusterrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`abzweigung-aus-patentanmeldung`](skills/abzweigung-aus-patentanmeldung/SKILL.md) | Wenn es um Abzweigung Aus Patentanmeldung in gebrauchsmusterrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anspruchsfassung-gebrauchsmuster`](skills/anspruchsfassung-gebrauchsmuster/SKILL.md) | Wenn es um Anspruchsfassung Gebrauchsmuster in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`arbeitnehmererfindung-und-inhaberschaft`](skills/arbeitnehmererfindung-und-inhaberschaft/SKILL.md) | Wenn es um Arbeitnehmererfindung Und Inhaberschaft in gebrauchsmusterrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`auskunft-schadensersatz-geheimhaltung`](skills/auskunft-schadensersatz-geheimhaltung/SKILL.md) | Wenn es um Auskunft Schadensersatz Und Rechnungslegung in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| [`auslandsroute-kein-beschreibung-zeichnungen`](skills/auslandsroute-kein-beschreibung-zeichnungen/SKILL.md) | Wenn es um Auslandsroute Kein Eu Gebrauchsmuster in gebrauchsmusterrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`beschreibung-und-zeichnungen`](skills/beschreibung-und-zeichnungen/SKILL.md) | Wenn es um Beschreibung Und Zeichnungen in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`beschwerde-bpatg-besichtigung-beschlagnahme`](skills/beschwerde-bpatg-besichtigung-beschlagnahme/SKILL.md) | Wenn es um Beschwerde Bpatg in gebrauchsmusterrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`besichtigung-beschlagnahme-und-beweissicherung`](skills/besichtigung-beschlagnahme-und-beweissicherung/SKILL.md) | Wenn es um Besichtigung Beschlagnahme Und Beweissicherung in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`chemie-biotech-china-utility`](skills/chemie-biotech-china-utility/SKILL.md) | Wenn es um Chemie Biotech Und Stoffschutz in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`china-utility-model-vergleich`](skills/china-utility-model-vergleich/SKILL.md) | Wenn es um China Utility Model Vergleich in gebrauchsmusterrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`computerprogramm-verfahrensausschluss`](skills/computerprogramm-verfahrensausschluss/SKILL.md) | Wenn es um Computerprogramm Und Verfahrensausschluss in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächst... |
| [`cross-license-verletzung-anspruchsmerkmale`](skills/cross-license-verletzung-anspruchsmerkmale/SKILL.md) | Wenn es um Vergleich Und Cross License in gebrauchsmusterrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`doppelschutz-patent-dpma-anmeldung`](skills/doppelschutz-patent-dpma-anmeldung/SKILL.md) | Wenn es um Doppelschutz Patent Gebrauchsmuster in gebrauchsmusterrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`dpma-anmeldung-formalien`](skills/dpma-anmeldung-formalien/SKILL.md) | Wenn es um Dpma Anmeldung Formalien in gebrauchsmusterrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`einstweilige-verfuegung-fto-schutzbereich`](skills/einstweilige-verfuegung-fto-schutzbereich/SKILL.md) | Wenn es um Einstweilige Verfuegung Gebrauchsmuster in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| [`fto-und-schutzbereich`](skills/fto-und-schutzbereich/SKILL.md) | Wenn es um Fto Und Schutzbereich in gebrauchsmusterrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`gebrauchsmuster-kaltstart-interview`](skills/gebrauchsmuster-kaltstart-interview/SKILL.md) | Wenn es um Gebrauchsmuster Kaltstart Interview in gebrauchsmusterrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`geheimhaltung-vor-anmeldung`](skills/geheimhaltung-vor-anmeldung/SKILL.md) | Wenn es um Geheimhaltung Vor Anmeldung in gebrauchsmusterrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`gutachten-rechtsbestand-insolvenz-verwertung`](skills/gutachten-rechtsbestand-insolvenz-verwertung/SKILL.md) | Wenn es um Gutachten Rechtsbestand in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`insolvenz-und-verwertung`](skills/insolvenz-und-verwertung/SKILL.md) | Wenn es um Insolvenz Und Verwertung in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`japan-utility-klageantraege-verletzung`](skills/japan-utility-klageantraege-verletzung/SKILL.md) | Wenn es um Japan Utility Model Vergleich in gebrauchsmusterrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Gebrauchsmusterrecht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md) | Wenn es um Allgemein in gebrauchsmusterrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`klageantraege-verletzung`](skills/klageantraege-verletzung/SKILL.md) | Wenn es um Klageantraege Verletzung in gebrauchsmusterrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`lizenzvertrag-gebrauchsmuster`](skills/lizenzvertrag-gebrauchsmuster/SKILL.md) | Wenn es um Lizenzvertrag Gebrauchsmuster in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`local-counsel-loeschung-erwiderung`](skills/local-counsel-loeschung-erwiderung/SKILL.md) | Wenn es um Local Counsel Briefing Ausland in gebrauchsmusterrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`loeschung-erwiderung-inhaber`](skills/loeschung-erwiderung-inhaber/SKILL.md) | Wenn es um Loeschung Erwiderung Inhaber in gebrauchsmusterrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`loeschungsantrag-dpma-mandantenmemo`](skills/loeschungsantrag-dpma-mandantenmemo/SKILL.md) | Wenn es um Loeschungsantrag Dpma in gebrauchsmusterrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`mandantenmemo-gebrauchsmusterstrategie`](skills/mandantenmemo-gebrauchsmusterstrategie/SKILL.md) | Wenn es um Mandantenmemo Gebrauchsmusterstrategie in gebrauchsmusterrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`messeveroeffentlichung-prototyp-muendliche`](skills/messeveroeffentlichung-prototyp-muendliche/SKILL.md) | Wenn es um Messeveroeffentlichung Und Prototyp in gebrauchsmusterrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`muendliche-verhandlung-dpma`](skills/muendliche-verhandlung-dpma/SKILL.md) | Wenn es um Muendliche Verhandlung Dpma in gebrauchsmusterrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`neuheit-erfinderischer-patent-gebrauchsmuster`](skills/neuheit-erfinderischer-patent-gebrauchsmuster/SKILL.md) | Wenn es um Neuheit Und Erfinderischer Schritt in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`neuheitsschonfrist-eigene-offenbarung`](skills/neuheitsschonfrist-eigene-offenbarung/SKILL.md) | Wenn es um Neuheitsschonfrist Eigene Offenbarung in gebrauchsmusterrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`patent-oder-gebrauchsmuster-route`](skills/patent-oder-gebrauchsmuster-route/SKILL.md) | Wenn es um Patent Oder Gebrauchsmuster Route in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`prioritaet-anmeldetag-produktlaunch-neuheit`](skills/prioritaet-anmeldetag-produktlaunch-neuheit/SKILL.md) | Wenn es um Prioritaet Und Anmeldetag in gebrauchsmusterrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`produktlaunch-und-neuheit`](skills/produktlaunch-und-neuheit/SKILL.md) | Wenn es um Produktlaunch Und Neuheit in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`qualitygate-gebrmg`](skills/qualitygate-gebrmg/SKILL.md) | Wenn es um Qualitygate Gebrmg in gebrauchsmusterrecht geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`recherche-nach-schutzgegenstand-ausschluesse`](skills/recherche-nach-schutzgegenstand-ausschluesse/SKILL.md) | Wenn es um Recherche Nach Paragraph 7 Gebrmg in gebrauchsmusterrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`registerstand-aufrechterhaltung-lizenzvertrag`](skills/registerstand-aufrechterhaltung-lizenzvertrag/SKILL.md) | Wenn es um Registerstand Fristen Aufrechterhaltung in gebrauchsmusterrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schutzgegenstand-und-ausschluesse`](skills/schutzgegenstand-und-ausschluesse/SKILL.md) | Wenn es um Schutzgegenstand Und Ausschluesse in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`stand-technik-startup-schnellschutz`](skills/stand-technik-startup-schnellschutz/SKILL.md) | Wenn es um Stand Der Technik Belegpaket in gebrauchsmusterrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`startup-schnellschutz`](skills/startup-schnellschutz/SKILL.md) | Wenn es um Startup Schnellschutz in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`technische-laborbuch-teilloeschung`](skills/technische-laborbuch-teilloeschung/SKILL.md) | Wenn es um Technische Dokumentation Laborbuch in gebrauchsmusterrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`teilloeschung-und-hilfsantraege`](skills/teilloeschung-und-hilfsantraege/SKILL.md) | Wenn es um Teilloeschung Und Hilfsantraege in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`uebertragung-sicherheit-us-provisional`](skills/uebertragung-sicherheit-us-provisional/SKILL.md) | Wenn es um Uebertragung Und Sicherheit in gebrauchsmusterrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`us-provisional-vs-gebrauchsmuster`](skills/us-provisional-vs-gebrauchsmuster/SKILL.md) | Wenn es um Us Provisional Vs Gebrauchsmuster in gebrauchsmusterrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verletzung-anspruchsmerkmale`](skills/verletzung-anspruchsmerkmale/SKILL.md) | Wenn es um Verletzung Anspruchsmerkmale in gebrauchsmusterrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`vernichtung-rueckruf-vorbenutzungsrecht`](skills/vernichtung-rueckruf-vorbenutzungsrecht/SKILL.md) | Wenn es um Vernichtung Rueckruf Und Entfernung in gebrauchsmusterrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`vorbenutzungsrecht`](skills/vorbenutzungsrecht/SKILL.md) | Wenn es um Vorbenutzungsrecht in gebrauchsmusterrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`zoll-und-plattformdurchsetzung`](skills/zoll-und-plattformdurchsetzung/SKILL.md) | Wenn es um Zoll Und Plattformdurchsetzung in gebrauchsmusterrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
