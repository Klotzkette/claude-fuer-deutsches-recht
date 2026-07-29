# Meinungsprüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Meinungsprüfer für Äußerungsrecht: Meinung oder Tatsache, Beleidigung, üble Nachrede, Verleumdung, Paragraf 188 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR/EuGH, OLG-Praxis, US-Supreme-Court-Vergleich, Zivilrecht, Plattformen, Social Media, Arbeitsplatz, Schule und kommunale Machtkritik.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/meinungspruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`meinungspruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/meinungspruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/meinungspruefer/meinungspruefer-werkstatt.md" download><code>meinungspruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/meinungspruefer/meinungspruefer-schnellstart.md" download><code>meinungspruefer-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Meinungsprüfer - Grenzfälle im Alltag](../testakten/meinungspruefer-grenzfaelle-alltag/README.md) | [Gesamt-PDF](../testakten/meinungspruefer-grenzfaelle-alltag/gesamt-pdf/meinungspruefer-grenzfaelle-alltag_gesamt.pdf) | [`testakte-meinungspruefer-grenzfaelle-alltag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-meinungspruefer-grenzfaelle-alltag.zip) | [`testakte-meinungspruefer-grenzfaelle-alltag-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-meinungspruefer-grenzfaelle-alltag-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Freistehendes Plugin für die Prüfung von Äußerungen nach einfachem Recht, Verfassungsrecht, Europarecht und Rechtsvergleich: Meinung oder Tatsachenbehauptung, Beleidigung, üble Nachrede, Verleumdung, Personen des politischen Lebens, Wahrnehmung berechtigter Interessen, zivilrechtliche Unterlassung, Widerruf, Geldentschädigung, Plattform- und Social-Media-Kontext, EGMR/EuGH/GRCh, OLG-/KG-Praxis und US-Supreme-Court-Vergleich.

**Keine Rechtsberatung.** Das Plugin erzeugt eine strukturierte Vorprüfung und dokumentierbare Arbeitsprodukte zur anwaltlichen Kontrolle. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle verwendet.

## Start

```
/meinungspruefer:allgemein
```

Der Einstieg fragt schnell ab: exakter Wortlaut, Medium, Publikum, Anlass, Vorgeschichte, Betroffene, Tatsachenkern, Belege, Wiederholungsgefahr, gewünschter Output und Risikotoleranz. Danach routet er zu den passenden Spezialskills.

## Skills (36)

| Skill | Zweck |
|---|---|
| `meinungspruefer-allgemein` | Schöner Einstieg, Schnelltriage, Quellenhygiene und Routing |
| `schnelltriage-aeusserung` | Erste Ampel für Strafrecht, Zivilrecht, Plattform und arbeits-/schulbezogene Risiken |
| `zitat-und-kontextaufnahme` | Wortlaut, Kontext, Adressatenkreis, Medium und Vorgeschichte sauber erfassen |
| `meinung-tatsache-abgrenzung` | Meinung, Tatsache, gemischte Äußerung und Tatsachenkern trennen |
| `mehrdeutigkeit-sinnermittlung` | Sinnermittlung, Durchschnittspublikum und nicht ehrverletzende Deutungen |
| `beleglage-tatsachenbehauptung` | Belegmatrix für Tatsachen, Verdachtsäußerung und erwiesen unwahre Behauptung |
| `strafrecht-185-beleidigung` | § 185 StGB mit Art.-5-GG-Abwägung |
| `ueble-nachrede-186` | § 186 StGB, Nichterweislichkeit und Tatsachenkern |
| `verleumdung-187` | § 187 StGB, Wissen um Unwahrheit und Belegprüfung |
| `personen-politisches-leben-188` | § 188 StGB, Person des politischen Lebens, Öffentlichkeit und Erschwerung des Wirkens |
| `wahrnehmung-berechtigter-interessen-193` | § 193 StGB, Beschwerde, Bewertung, Mandats-/Arbeits-/Bürgerkontext |
| `strafantrag-194-und-verfahren` | Strafantrag, Antragsberechtigte, Fristen, Privatklage, Einstellungsoptionen |
| `schmaehkritik-formalbeleidigung-menschenwuerde` | Enge Ausnahmen ohne Normalabwägung |
| `abwaegung-art-5-gg` | Verfassungsrechtlicher Abwägungskern nach Art. 5 GG |
| `machtkritik-amtstraeger` | Amtsträger, Behörden, Bürgermeister, Schule, Justiz und Machtkritik |
| `arbeitgeber-betrieb-kantine` | Arbeitsplatz, Kantine, Kollegium, Betriebsrat, arbeitsrechtliche Nebenfolgen |
| `schule-elternchat` | Schule, Elternchat, Lehrkräfte, Schulleitung und pädagogischer Konflikt |
| `soziale-medien-x-linkedin` | X, LinkedIn, Kommentarspalten, Sichtbarkeit, Prangerwirkung, Screenshots |
| `kommunalrecht-buergermeister` | Kommunale Debatte, Bauprojekt, Ratssitzung, Amts- und Privatrolle |
| `satire-ironisierung-pinocchio` | Satire, Überzeichnung, Pinocchio-Vergleich, Lügenvorwurf als Wertung oder Tatsache |
| `schimpfwort-lackaffe-und-spott` | Spottbegriffe wie Lackaffe im Kontext prüfen |
| `zivilrecht-unterlassung-widerruf-schadensersatz` | APR, §§ 823, 1004 BGB analog, § 824 BGB und Beseitigungsansprüche |
| `presserecht-plattformen-loeschung-dsa` | Medien, Plattformmeldungen, Löschung, Sperrung und DSA-Schnittstellen |
| `europarecht-emrk-grch` | Art. 10 EMRK, Art. 11 GRCh, unions- und konventionsfreundliche Lesart |
| `egmr-art-10-rechtsprechung` | EGMR-Leitlinien zu öffentlicher Debatte, Werturteil, Tatsachengrundlage, Art.-8-/Art.-10-Abwägung, Hyperlinks und Drittkommentaren |
| `eugh-grch-art-11-rechtsprechung` | EuGH/GRCh bei Plattformen, Suchmaschinen, Datenschutz, Uploadfiltern, De-Referenzierung und journalistischen Zwecken |
| `olg-kg-praxis-rechtsprechung` | Obergerichtliche Praxis zu Unterlassung, Sinnermittlung, Social Media, Verdachtsäußerung, Plattformlabel und Tenorrisiko |
| `rechtsvergleich-usa-supreme-court` | US-Supreme-Court-Vergleich zu First Amendment, actual malice, public concern, opinion, parody, threats und incitement |
| `beweissicherung-screenshots` | Screenshots, Metadaten, Zeugen, URLs, Löschungen, Chatverläufe |
| `risikomatrix-ampel` | Ergebnis als Grün/Gelb/Rot mit Unsicherheiten und nächstem Schritt |
| `gegendarstellung-entschuldigung-deeskalation` | Reaktionsoptionen ohne unnötige Eskalation |
| `abmahnung-strafanzeige-reaktion` | Eingang von Abmahnung, Strafanzeige, Anhörung oder Plattformmeldung bearbeiten |
| `schriftsatz-stellungnahme-verteidigung` | Verteidigungs- und Erwiderungsbausteine |
| `output-memo-pruefvermerk` | Dokumentierter Prüfvermerk mit Zitat, Kontext, Normen und Ergebnis |
| `testakte-auswertung` | Die Testakte strukturiert auswerten |
| `rechtsprechungsbank-verifiziert` | Verifizierte Rechtsprechung mit Datum, Aktenzeichen und freier Quelle |

## Quellenstand

Stand: 05/2026. Kernnormen: Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, §§ 185-188, 192-194 StGB, §§ 823, 824, 1004 BGB analog, § 22 KUG bei Bildern und DSA-Schnittstellen bei Plattformen. Leitentscheidungen sind im Skill `rechtsprechungsbank-verifiziert` dokumentiert; der USA-Vergleich ist ausdrücklich nur Vergleich, kein Import amerikanischer Standards in die deutsche Prüfung.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md), [`meinungspruefer-erstpruefung-und-mandatsziel`](skills/meinungspruefer-erstpruefung-und-mandatsziel/SKILL.md), [`schmaehkritik-formalbeleidigung-schnelltriage`](skills/schmaehkritik-formalbeleidigung-schnelltriage/SKILL.md), [`schnelltriage-aeusserung`](skills/schnelltriage-aeusserung/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`aeusserungsrecht-tatbestand-beweis-und-belege`](skills/aeusserungsrecht-tatbestand-beweis-und-belege/SKILL.md), [`beleglage-tatsachenbehauptung-beweissicherung`](skills/beleglage-tatsachenbehauptung-beweissicherung/SKILL.md), [`beweissicherung-screenshots`](skills/beweissicherung-screenshots/SKILL.md), [`rechtsvergleich-usa-risikomatrix-ampel`](skills/rechtsvergleich-usa-risikomatrix-ampel/SKILL.md), [`risikomatrix-ampel`](skills/risikomatrix-ampel/SKILL.md), [`spezial-stgb-livequellen-und-rechtsprechungscheck`](skills/spezial-stgb-livequellen-und-rechtsprechungscheck/SKILL.md), [`stgb-quellenkarte`](skills/stgb-quellenkarte/SKILL.md), [`strafrecht-beleidigung-testakte-auswertung`](skills/strafrecht-beleidigung-testakte-auswertung/SKILL.md), [`tatsache-dokumentenmatrix-und-lueckenliste`](skills/tatsache-dokumentenmatrix-und-lueckenliste/SKILL.md), [`testakte-auswertung`](skills/testakte-auswertung/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`beleidigung-meinungspruefer`](skills/beleidigung-meinungspruefer/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`verleumdung-verhandlung-vergleich-und-eskalation`](skills/verleumdung-verhandlung-vergleich-und-eskalation/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`chronologie-fristen`](skills/chronologie-fristen/SKILL.md), [`meinung-strafantrag-verfahren`](skills/meinung-strafantrag-verfahren/SKILL.md), [`strafantrag-194-und-verfahren`](skills/strafantrag-194-und-verfahren/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`output-memo-pruefvermerk`](skills/output-memo-pruefvermerk/SKILL.md), [`stellungnahme-verteidigung-schule-elternchat`](skills/stellungnahme-verteidigung-schule-elternchat/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`europarecht-emrk-gegendarstellung`](skills/europarecht-emrk-gegendarstellung/SKILL.md), [`gegendarstellung-entschuldigung-deeskalation`](skills/gegendarstellung-entschuldigung-deeskalation/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`abmahnung-strafanzeige-reaktion`](skills/abmahnung-strafanzeige-reaktion/SKILL.md), [`abwaegung-art-arbeitgeber-betrieb`](skills/abwaegung-art-arbeitgeber-betrieb/SKILL.md), [`arbeitgeber-betrieb-kantine`](skills/arbeitgeber-betrieb-kantine/SKILL.md), [`egmr-art-eugh-grch`](skills/egmr-art-eugh-grch/SKILL.md), [`eugh-grch-art-11-rechtsprechung`](skills/eugh-grch-art-11-rechtsprechung/SKILL.md), [`kommunalrecht-buergermeister-machtkritik`](skills/kommunalrecht-buergermeister-machtkritik/SKILL.md), [`machtkritik-amtstraeger`](skills/machtkritik-amtstraeger/SKILL.md), [`mehrdeutigkeit-sinnermittlung-meinung`](skills/mehrdeutigkeit-sinnermittlung-meinung/SKILL.md), [`meinung-tatsache-abgrenzung`](skills/meinung-tatsache-abgrenzung/SKILL.md), [`nachrede-tatsache`](skills/nachrede-tatsache/SKILL.md), [`olg-kg-rechtsprechungsbank-verifiziert`](skills/olg-kg-rechtsprechungsbank-verifiziert/SKILL.md), [`personen-politisches-presserecht-plattformen`](skills/personen-politisches-presserecht-plattformen/SKILL.md), [`presserecht-plattformen-loeschung-dsa`](skills/presserecht-plattformen-loeschung-dsa/SKILL.md), [`rechtsprechungsbank-verifiziert`](skills/rechtsprechungsbank-verifiziert/SKILL.md), [`satire-ironisierung-schimpfwort-lackaffe`](skills/satire-ironisierung-schimpfwort-lackaffe/SKILL.md), [`schimpfwort-lackaffe-und-spott`](skills/schimpfwort-lackaffe-und-spott/SKILL.md), [`schule-elternchat`](skills/schule-elternchat/SKILL.md), [`soziale-medien-aeusserungsrecht`](skills/soziale-medien-aeusserungsrecht/SKILL.md), ... plus 6 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`abmahnung-strafanzeige-reaktion`](skills/abmahnung-strafanzeige-reaktion/SKILL.md) | Wenn es um Reaktion auf Abmahnung oder Strafanzeige in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`abwaegung-art-arbeitgeber-betrieb`](skills/abwaegung-art-arbeitgeber-betrieb/SKILL.md) | Wenn es um Art. 5 GG - Abwägung in Meinungsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`aeusserungsrecht-tatbestand-beweis-und-belege`](skills/aeusserungsrecht-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Aeusserungsrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage in Meinungsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`arbeitgeber-betrieb-kantine`](skills/arbeitgeber-betrieb-kantine/SKILL.md) | Wenn es um Betrieb, Kantine und Arbeitgeber in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`beleglage-tatsachenbehauptung-beweissicherung`](skills/beleglage-tatsachenbehauptung-beweissicherung/SKILL.md) | Wenn es um Beleglage bei Tatsachenbehauptungen in Meinungsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`beleidigung-meinungspruefer`](skills/beleidigung-meinungspruefer/SKILL.md) | Wenn es um Beleidigung: Risikoampel, Gegenargumente und Verteidigungslinien in Meinungsprüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`beweissicherung-screenshots`](skills/beweissicherung-screenshots/SKILL.md) | Wenn es um Beweissicherung in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`chronologie-fristen`](skills/chronologie-fristen/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`egmr-art-eugh-grch`](skills/egmr-art-eugh-grch/SKILL.md) | Wenn es um EGMR-Art.-10-Rechtsprechung in Meinungsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Meinungsprüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`eugh-grch-art-11-rechtsprechung`](skills/eugh-grch-art-11-rechtsprechung/SKILL.md) | Wenn es um EuGH und Art. 11 GRCh in Meinungsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`europarecht-emrk-gegendarstellung`](skills/europarecht-emrk-gegendarstellung/SKILL.md) | Wenn es um Europarecht: EMRK und Grundrechtecharta in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gegendarstellung-entschuldigung-deeskalation`](skills/gegendarstellung-entschuldigung-deeskalation/SKILL.md) | Wenn es um Gegendarstellung, Entschuldigung, Deeskalation in Meinungsprüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Meinungsprüfer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md) | Wenn es um Meinungsprüfer - Allgemein in Meinungsprüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kommunalrecht-buergermeister-machtkritik`](skills/kommunalrecht-buergermeister-machtkritik/SKILL.md) | Wenn es um Kommunalrechtlicher Grenzfall: Bürgermeister und Bauprojekt in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`machtkritik-amtstraeger`](skills/machtkritik-amtstraeger/SKILL.md) | Wenn es um Machtkritik und Amtsträger in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mehrdeutigkeit-sinnermittlung-meinung`](skills/mehrdeutigkeit-sinnermittlung-meinung/SKILL.md) | Wenn es um Mehrdeutigkeit und Sinnermittlung in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`meinung-strafantrag-verfahren`](skills/meinung-strafantrag-verfahren/SKILL.md) | Wenn es um Meinung: Fristen, Form, Zuständigkeit und Rechtsweg in Meinungsprüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`meinung-tatsache-abgrenzung`](skills/meinung-tatsache-abgrenzung/SKILL.md) | Wenn es um Meinung oder Tatsachenbehauptung in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`meinungspruefer-erstpruefung-und-mandatsziel`](skills/meinungspruefer-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Meinungspruefer: Erstprüfung, Rollenklärung und Mandatsziel in Meinungsprüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nachrede-tatsache`](skills/nachrede-tatsache/SKILL.md) | Wenn es um Nachrede: Schriftsatz-, Brief- und Memo-Bausteine in Meinungsprüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`olg-kg-rechtsprechungsbank-verifiziert`](skills/olg-kg-rechtsprechungsbank-verifiziert/SKILL.md) | Wenn es um OLG-/KG-Praxis zur Äußerungsprüfung in Meinungsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`output-memo-pruefvermerk`](skills/output-memo-pruefvermerk/SKILL.md) | Wenn es um Output: Memo und Prüfvermerk in Meinungsprüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`personen-politisches-presserecht-plattformen`](skills/personen-politisches-presserecht-plattformen/SKILL.md) | Wenn es um Paragraf 188 StGB - Personen des politischen Lebens in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`presserecht-plattformen-loeschung-dsa`](skills/presserecht-plattformen-loeschung-dsa/SKILL.md) | Wenn es um Presse, Plattformen und DSA-Schnittstelle in Meinungsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`rechtsprechungsbank-verifiziert`](skills/rechtsprechungsbank-verifiziert/SKILL.md) | Wenn es um Rechtsprechungsbank - verifiziert in Meinungsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`rechtsvergleich-usa-risikomatrix-ampel`](skills/rechtsvergleich-usa-risikomatrix-ampel/SKILL.md) | Wenn es um Rechtsvergleich USA: Supreme Court in Meinungsprüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`risikomatrix-ampel`](skills/risikomatrix-ampel/SKILL.md) | Wenn es um Risikomatrix Ampel in Meinungsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`satire-ironisierung-schimpfwort-lackaffe`](skills/satire-ironisierung-schimpfwort-lackaffe/SKILL.md) | Wenn es um Satire, Ironie und Pinocchio-Vergleich in Meinungsprüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`schimpfwort-lackaffe-und-spott`](skills/schimpfwort-lackaffe-und-spott/SKILL.md) | Wenn es um \"Lackaffe\" und ähnliche Spottbegriffe in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schmaehkritik-formalbeleidigung-schnelltriage`](skills/schmaehkritik-formalbeleidigung-schnelltriage/SKILL.md) | Wenn es um Schmähkritik, Formalbeleidigung, Menschenwürde in Meinungsprüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schnelltriage-aeusserung`](skills/schnelltriage-aeusserung/SKILL.md) | Wenn es um Schnelltriage Äußerung in Meinungsprüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schule-elternchat`](skills/schule-elternchat/SKILL.md) | Wenn es um Schule und Elternchat in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`soziale-medien-aeusserungsrecht`](skills/soziale-medien-aeusserungsrecht/SKILL.md) | Wenn es um Soziale Medien: X, LinkedIn, Bewertungsportale in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-stgb-livequellen-und-rechtsprechungscheck`](skills/spezial-stgb-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Stgb: Livequellen- und Rechtsprechungscheck in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stellungnahme-verteidigung-schule-elternchat`](skills/stellungnahme-verteidigung-schule-elternchat/SKILL.md) | Wenn es um Stellungnahme und Verteidigung in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stgb-quellenkarte`](skills/stgb-quellenkarte/SKILL.md) | Wenn es um Stgb Quellenkarte in Meinungsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`strafantrag-194-und-verfahren`](skills/strafantrag-194-und-verfahren/SKILL.md) | Wenn es um Strafantrag und Verfahren in Meinungsprüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafrecht-beleidigung-testakte-auswertung`](skills/strafrecht-beleidigung-testakte-auswertung/SKILL.md) | Wenn es um Paragraf 185 StGB - Beleidigung in Meinungsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`tatsache-dokumentenmatrix-und-lueckenliste`](skills/tatsache-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Tatsache: Dokumentenmatrix, Lückenliste und Nachforderung in Meinungsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`testakte-auswertung`](skills/testakte-auswertung/SKILL.md) | Wenn es um Testakte auswerten in Meinungsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`ueble-nachrede-verleumdung`](skills/ueble-nachrede-verleumdung/SKILL.md) | Wenn es um Paragraf 186 StGB - üble Nachrede in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ueble-verleumdung`](skills/ueble-verleumdung/SKILL.md) | Wenn es um Ueble: Behörden-, Gerichts- oder Registerweg in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verleumdung-187`](skills/verleumdung-187/SKILL.md) | Wenn es um Paragraf 187 StGB - Verleumdung in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verleumdung-verhandlung-vergleich-und-eskalation`](skills/verleumdung-verhandlung-vergleich-und-eskalation/SKILL.md) | Wenn es um Verleumdung: Verhandlung, Vergleich und Eskalation in Meinungsprüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`wahrnehmung-berechtigter-zitat`](skills/wahrnehmung-berechtigter-zitat/SKILL.md) | Wenn es um Paragraf 193 StGB - Wahrnehmung berechtigter Interessen in Meinungsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel in Meinungsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Meinungsprüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Meinungsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`zitat-und-kontextaufnahme`](skills/zitat-und-kontextaufnahme/SKILL.md) | Wenn es um Zitat und Kontextaufnahme in Meinungsprüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`zivilrecht-unterlassung-abmahnung`](skills/zivilrecht-unterlassung-abmahnung/SKILL.md) | Wenn es um Zivilrechtliche Äußerungsansprüche in Meinungsprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
