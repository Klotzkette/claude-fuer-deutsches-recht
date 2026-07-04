# Datenschutz-Sanktionsverfahren und Verteidigung


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`datenschutz-sanktionsverfahren-verteidigung`) | [`datenschutz-sanktionsverfahren-verteidigung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/datenschutz-sanktionsverfahren-verteidigung.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Spezialplugin für Vertretung und Verteidigung in datenschutzrechtlichen Sanktionsverfahren: DSGVO-Bußgeld, OWiG/StPO, Art.-58-Anordnung, Verwaltungsgericht, Aufsichtsbehördenkommunikation, EuGH/EDPB und Behördenstrategie.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`datenschutz-sanktionsverfahren-verteidigung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/datenschutz-sanktionsverfahren-verteidigung.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/datenschutz-sanktionsverfahren-verteidigung/datenschutz-sanktionsverfahren-verteidigung-werkstatt.md" download><code>datenschutz-sanktionsverfahren-verteidigung-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/datenschutz-sanktionsverfahren-verteidigung/datenschutz-sanktionsverfahren-verteidigung-schnellstart.md" download><code>datenschutz-sanktionsverfahren-verteidigung-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Datenschutzverstoss bewerten und die richtige Reaktion gegenüber Aufsicht und Betroffenen aufsetzen.
Dieses Plugin ist die Spezialwerkstatt für Mandate, in denen Datenschutzaufsicht nicht mehr nur Beratung ist, sondern Druck macht: Anhörung, Auskunftsverlangen, Art.-58-Anordnung, Bußgeldbescheid, Einspruch, Hauptverhandlung, Rechtsbeschwerde, Verwaltungsgericht und EuGH-Frage. Es ergänzt `datenschutzrecht`, ist aber bewusst eigenständig, weil solche Verfahren prozessual anders funktionieren als AVV, DSFA oder Datenschutzerklärung.

## Wofür es gedacht ist

- Verteidigung gegen DSGVO-Geldbußen nach Art. 83 DSGVO.
- Vertretung im OWiG-Verfahren nach § 41 BDSG, einschließlich Akteneinsicht, Einspruch, Zwischenverfahren, gerichtlicher Hauptverhandlung, Beschlussverfahren und Rechtsbeschwerde.
- Abwehr oder Verhandlung von Aufsichtsmaßnahmen nach Art. 58 Abs. 2 DSGVO: Verwarnung, Anordnung, Löschung, Verarbeitungsstopp, Drittlandtransfer-Stopp, Zwangsmittel und Veröffentlichungsrisiken.
- Verwaltungsgerichtlicher Rechtsschutz nach Art. 78 DSGVO und § 20 BDSG, wenn es nicht um die Geldbuße selbst geht.
- Koordination mit Datenpanne, Art.-82-Schadensersatz, Strafrecht, Geschäftsführung, D&O, Presse und internationalem One-Stop-Shop.

## Der wichtigste erste Satz im Mandat

Nicht sofort "kooperativ" alles erzählen. Erst verstehen, welche Spur läuft. Datenschutzrechtliche Mitwirkung, OWiG-Verteidigung und verwaltungsgerichtlicher Rechtsschutz haben unterschiedliche Regeln. Das Plugin fragt deshalb zuerst:

1. Liegt nur ein Auskunftsverlangen, eine Anhörung, ein Bußgeldbescheid oder eine Art.-58-Anordnung vor?
2. Wer ist Adressat und welche Behörde ist zuständig: Landesaufsicht, BfDI, kirchliche Datenschutzaufsicht oder federführende EU-Aufsicht?
3. Welche Frist läuft und wie wurde zugestellt?
4. Geht es um Geldbuße, Maßnahme, beides oder Folgerisiken?
5. Was ist belegt und was behauptet die Behörde nur?

## Zwei Hauptspuren

| Spur | Typischer Rechtsweg | Typische Arbeit |
| --- | --- | --- |
| **Bußgeld** | Art. 83 DSGVO, § 41 BDSG, OWiG/StPO sinngemäß; Einspruch nach § 67 OWiG; Zuständigkeit nach § 68 OWiG, modifiziert durch § 41 BDSG | Anhörung, Akteneinsicht, Bußgeldbescheid, Einspruch, Zwischenverfahren, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde |
| **Aufsichtsmaßnahme** | Art. 58/78 DSGVO, § 20 BDSG, VwGO | Anordnung prüfen, Bestimmtheit/Ermessen/Verhältnismäßigkeit, Anfechtungsklage, Eilrechtsschutz, Umsetzung/Verhandlung |

## Leitentscheidungen und Stand

Stand: Juni 2026. Besonders wichtig sind EuGH, Urteil vom 05.12.2023, C-807/21 (Deutsche Wohnen), und EuGH, Urteil vom 05.12.2023, C-683/21 (Nacionalinis visuomenės sveikatos centras). Die Linie ist: Ein Unternehmen kann unmittelbar Adressat einer DSGVO-Geldbuße sein; die Aufsicht muss nicht zuerst eine natürliche Person identifizieren. Zugleich bleibt Vorsatz oder Fahrlässigkeit erforderlich. Das Plugin behandelt diese Linie als Prüfprogramm, nicht als Freibrief für schematische Unternehmenshaftung.

## Quellenhygiene

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Normen und Rechtsprechung werden vor Ausgabe mit amtlichen oder frei zugänglichen Quellen geprüft, insbesondere:

- DSGVO über EUR-Lex.
- BDSG und OWiG über gesetze-im-internet.de.
- EuGH über CURIA/EUR-Lex.
- EDPB Guidelines 04/2022 über edpb.europa.eu.
- Deutsche Gerichtsentscheidungen nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier/amtlicher Quelle.

## Typische Outputs

- Behördenpost-Analyse: Was ist das, was droht, welche Frist läuft?
- Akteneinsichtsantrag und fristwahrender Einspruch.
- Stellungnahme vor Bußgeldbescheid.
- Art.-83-Bemessungsgegenrechnung nach EDPB 04/2022.
- Verschuldens- und Organisationsmemo nach EuGH C-807/21/C-683/21.
- Klage-/Eilantragsgerüst gegen Art.-58-Anordnung.
- Terminsmappe für Hauptverhandlung im Bußgeldverfahren.
- Management-Briefing für Vorstand/Geschäftsführung.
- Schlussmemo mit Remediation, Wiedervorlagen und Lessons Learned.

## Gute Startbefehle

```text
/datenschutz-sanktionsverfahren-verteidigung:kaltstart-verfahrensstand-und-mandatsziel
/datenschutz-sanktionsverfahren-verteidigung:bescheid-oder-anhoerung-richtig-lesen
/datenschutz-sanktionsverfahren-verteidigung:akteneinsicht-49-owig-147-stpo
/datenschutz-sanktionsverfahren-verteidigung:zustaendigkeit-amtsgericht-landgericht-41-bdsg
/datenschutz-sanktionsverfahren-verteidigung:art-58-anordnung-verwaltungsakt
/datenschutz-sanktionsverfahren-verteidigung:edpb-04-2022-bemessungsmethodik
```

## Skill-Logik

Die 100 Skills sind nicht als lose Liste gedacht, sondern als Verteidigungsmaschine: Kaltstart, Behördenvorfeld, Bußgeld/OWiG, Art.-83-Bemessung, Verwaltungsgericht, EU-One-Stop-Shop, Beweise/Forensik und Output. Jeder Skill soll die Mandantin handlungsfähiger machen und nicht bloß Normen aufsagen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `kaltstart-verfahrensstand-und-mandatsziel`, `privilege-und-mandatsgeheimnis`, `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren`, `sanktionsmandat-schlussprodukt-planen` |
| 2. Unterlagen, Sachverhalt und Quellen | `akteneinsicht-49-owig-147-stpo`, `arbeitnehmerdaten-und-betriebsrat-im-sanktionsverfahren`, `aufsichtsbehoerden-auskunftsverlangen-art-58-1`, `besondere-datenkategorien-art-9`, `beweisrecht-stpo-im-owig-datenschutz`, `datenloeschung-vs-beweissicherung`, `datenpanne-vor-bussgeld-selbstmeldung`, `dokumentenmatrix-akteneinsicht-vorlage-und-luecken`, `durchsuchung-beschlagnahme-und-datenzugriff`, `einstweilige-anordnung-123-vwgo-datenschutz`, `internationale-datenpanne-und-multi-notification`, `kirchliche-datenschutzaufsicht-sanktionen`, `loeschungsanordnung-und-datenbestand`, `logfiles-und-technische-beweise`, `normenkollision-geheimnisse-und-datenschutzaufsicht` |
| 3. Prüfung, Anspruch und Subsumtion | `bussgeldbescheid-65-owig-analyse`, `edsa-und-dsk-praxis-livecheck`, `kosten-auslagen-und-d-und-o-risiko`, `mandantenreport-regulatorische-risikolage` |
| 4. Gestaltung, Strategie und Verhandlung | `behoerdenstrategie-kooperation-oder-schweigen`, `behoerdenvergleich-erledigung-und-auflagen`, `bussgeldreduzierung-verhandlungspaket`, `hauptverhandlung-71-owig`, `loeschkonzept-und-aufbewahrungsfehler`, `massnahmenplan-als-sanktionsminderung`, `milderung-durch-compliance-vor-dem-vorfall` |
| 5. Verfahren, Behörde und Gericht | `aufsichtsbehoerden-antwortschreiben`, `behoerdenkommunikation-reputationsschutz`, `behoerdenuntaetigkeit-und-beschwerdegegner`, `bescheid-oder-anhoerung-richtig-lesen`, `beschlussverfahren-72-owig`, `beschwerde-betroffener-behoerdenverfahren`, `einspruch-67-owig-frist-und-form`, `einstellung-anregen-vor-bescheid`, `fristenzentrale-zustellung-und-wiedervorlage`, `fristverlaengerung-behoerde-ohne-nachteile`, `fruehstellungnahme-vor-bussgeldbescheid`, `gerichtstermin-sprechzettel`, `grch-verfahrensgrundrechte`, `ki-tools-im-sanktionsverfahren`, `parallelverfahren-art-82-massenklagen`, `parallelverfahren-strafrecht-42-bdsg`, `sachverstaendige-it-forensik-im-bussgeldverfahren`, `scope-cut-behoerdenfragen-einhegen`, ... plus 5 weitere |
| 6. Ergebnis, Schreiben und Kommunikation | `schlussmemo-und-lessons-learned`, `vorstands-und-gf-briefing` |
| 7. Kontrolle, Qualität und Gegenprüfung | `red-team-vor-jeder-einreichung` |
| 8. Spezialmodule und Schnittstellen | `anhoerung-55-owig`, `anwesenheit-73-owig-vertretung`, `art-58-anordnung-verwaltungsakt`, `art-78-rechtsschutz-und-betroffenenbeschwerde`, `art-83-abs-2-kriterien-einzeln`, `aufsicht-in-regulierten-branchen`, `aufsichtliche-anordnung-plus-bussgeld-doppelspur`, `auslaendische-mutter-und-deutsche-tochter`, `bestimmtheit-und-ermessen-art-58`, `bfdi-vs-landesaufsicht`, `edpb-04-2022-bemessungsmethodik`, `edpb-art-65-streitbeilegung`, `eugh-vorlage-art-267`, `gewinnabschoepfung-und-finanzieller-vorteil`, `interne-untersuchung-legal-hold`, `irische-dpc-und-deutsche-aufsicht`, `kinder-und-schutzbeduerftige-betroffene`, `lieferanten-und-auftragsverarbeiter-regress`, ... plus 26 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 100 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `akteneinsicht-49-owig-147-stpo` | Wenn es um Akteneinsicht Paragraf 49 OWiG und Paragraf 147 StPO in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `anhoerung-55-owig` | Wenn es um Anhörung nach Paragraf 55 OWiG in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| `anwesenheit-73-owig-vertretung` | Wenn es um Anwesenheit und Entbindung Paragraf 73 OWiG in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitnehmerdaten-und-betriebsrat-im-sanktionsverfahren` | Wenn es um Beschäftigtendaten und Betriebsrat in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `art-58-anordnung-verwaltungsakt` | Wenn es um Art.-58-Anordnung als Verwaltungsakt in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkt... |
| `art-78-rechtsschutz-und-betroffenenbeschwerde` | Wenn es um Art. 78 Rechtsschutz in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und... |
| `art-83-abs-2-kriterien-einzeln` | Wenn es um Art. 83 Abs. 2 Kriterien einzeln prüfen in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpu... |
| `aufsicht-in-regulierten-branchen` | Wenn es um Regulierte Branchen Bank Gesundheit Energie in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Pr... |
| `aufsichtliche-anordnung-plus-bussgeld-doppelspur` | Wenn es um Anordnung plus Bußgeld Doppelspur in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `aufsichtsbehoerden-antwortschreiben` | Wenn es um Antwortschreiben an Aufsichtsbehörde in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `aufsichtsbehoerden-auskunftsverlangen-art-58-1` | Wenn es um Auskunftsverlangen Art. 58 Abs. 1 DSGVO beantworten in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsproduk... |
| `auslaendische-mutter-und-deutsche-tochter` | Wenn es um Ausländische Mutter und deutsche Tochter in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zus... |
| `behoerdenkommunikation-reputationsschutz` | Wenn es um Behördenkommunikation mit Reputationsschutz in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Pr... |
| `behoerdenstrategie-kooperation-oder-schweigen` | Wenn es um Kooperation oder Schweigen strategisch wählen in Datenschutz-Sanktionsverfahren und Verteidigung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, B... |
| `behoerdenuntaetigkeit-und-beschwerdegegner` | Wenn es um Behördenuntätigkeit und Beschwerdegegner in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `behoerdenvergleich-erledigung-und-auflagen` | Wenn es um Erledigung mit der Aufsicht verhandeln in Datenschutz-Sanktionsverfahren und Verteidigung geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `bescheid-oder-anhoerung-richtig-lesen` | Wenn es um Behördenpost richtig lesen in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risike... |
| `beschlussverfahren-72-owig` | Wenn es um Beschlussverfahren Paragraf 72 OWiG in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beschwerde-betroffener-behoerdenverfahren` | Wenn es um Beschwerde eines Betroffenen als Auslöser in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zu... |
| `besondere-datenkategorien-art-9` | Wenn es um Besondere Datenkategorien Art. 9 in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `bestimmtheit-und-ermessen-art-58` | Wenn es um Bestimmtheit und Ermessen Art. 58 in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `beweisrecht-stpo-im-owig-datenschutz` | Wenn es um Beweisrecht im Datenschutz-OWiG in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `bfdi-vs-landesaufsicht` | Wenn es um BfDI oder Landesaufsicht in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bussgeldbescheid-65-owig-analyse` | Wenn es um Bußgeldbescheid Paragraf 65 OWiG analysieren in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mi... |
| `bussgeldreduzierung-verhandlungspaket` | Wenn es um Bußgeldreduzierung Verhandlungspaket in Datenschutz-Sanktionsverfahren und Verteidigung geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `datenloeschung-vs-beweissicherung` | Wenn es um Datenlöschung vs. Beweissicherung in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `datenpanne-vor-bussgeld-selbstmeldung` | Wenn es um Datenpanne vor Bußgeld Selbstmeldung taktisch nutzen in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widers... |
| `dokumentenmatrix-akteneinsicht-vorlage-und-luecken` | Wenn es um Dokumentenmatrix vor Akteneinsicht in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `durchsuchung-beschlagnahme-und-datenzugriff` | Wenn es um Durchsuchung Beschlagnahme und Datenzugriff in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `edpb-04-2022-bemessungsmethodik` | Wenn es um EDPB 04/2022 Bemessungsmethodik in Datenschutz-Sanktionsverfahren und Verteidigung geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfra... |
| `edpb-art-65-streitbeilegung` | Wenn es um EDPB-Streitbeilegung Art. 65 in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risi... |
| `edsa-und-dsk-praxis-livecheck` | Wenn es um EDPB und DSK Praxis Livecheck in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einspruch-67-owig-frist-und-form` | Wenn es um Einspruch Paragraf 67 OWiG Frist und Form in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einstellung-anregen-vor-bescheid` | Wenn es um Einstellung vor Bescheid anregen in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargum... |
| `einstweilige-anordnung-123-vwgo-datenschutz` | Wenn es um Einstweilige Anordnung Paragraf 123 VwGO in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfp... |
| `eugh-vorlage-art-267` | Wenn es um EuGH-Vorlagefragen entwickeln in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fristenzentrale-zustellung-und-wiedervorlage` | Wenn es um Fristenzentrale Zustellung und Wiedervorlage in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fristverlaengerung-behoerde-ohne-nachteile` | Wenn es um Fristverlängerung gegenüber Aufsicht in Datenschutz-Sanktionsverfahren und Verteidigung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fruehstellungnahme-vor-bussgeldbescheid` | Wenn es um Frühstellungnahme vor Bußgeldbescheid in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gerichtstermin-sprechzettel` | Wenn es um Gerichtstermin-Sprechzettel in Datenschutz-Sanktionsverfahren und Verteidigung geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| `gewinnabschoepfung-und-finanzieller-vorteil` | Wenn es um Finanzieller Vorteil und Gewinnabschöpfung in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prü... |
| `grch-verfahrensgrundrechte` | Wenn es um GRCh-Verfahrensgrundrechte in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hauptverhandlung-71-owig` | Wenn es um Hauptverhandlung Paragraf 71 OWiG in Datenschutz-Sanktionsverfahren und Verteidigung geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| `internationale-datenpanne-und-multi-notification` | Wenn es um Internationale Datenpanne und Multi-Notification in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Verhandlungs- oder Eskalationsli... |
| `interne-untersuchung-legal-hold` | Wenn es um Interne Untersuchung und Legal Hold in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| `irische-dpc-und-deutsche-aufsicht` | Wenn es um Irische DPC und deutsche Aufsicht in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-verfahrensstand-und-mandatsziel` | Wenn es um Kaltstart Verfahrensstand und Mandatsziel in Datenschutz-Sanktionsverfahren und Verteidigung geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschr... |
| `ki-tools-im-sanktionsverfahren` | Wenn es um digitale Werkzeuge-Tools im Sanktionsverfahren in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kinder-und-schutzbeduerftige-betroffene` | Wenn es um Kinder und vulnerable Betroffene in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `kirchliche-datenschutzaufsicht-sanktionen` | Wenn es um Kirchliche Datenschutzaufsicht in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kosten-auslagen-und-d-und-o-risiko` | Wenn es um Kosten Auslagen und D&O-Risiko in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lieferanten-und-auftragsverarbeiter-regress` | Wenn es um Lieferanten und Auftragsverarbeiter Regress in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `loeschkonzept-und-aufbewahrungsfehler` | Wenn es um Löschkonzept und Aufbewahrungsfehler in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkt... |
| `loeschungsanordnung-und-datenbestand` | Wenn es um Löschungsanordnung und Datenbestand in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `logfiles-und-technische-beweise` | Wenn es um Logfiles und technische Beweise in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mandanteninterview-ohne-selbstbelastung` | Wenn es um Mandanteninterview ohne Selbstbelastung in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nac... |
| `mandantenreport-regulatorische-risikolage` | Wenn es um Mandantenreport regulatorische Risikolage in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `massnahmenplan-als-sanktionsminderung` | Wenn es um Maßnahmenplan als Sanktionsminderung in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkt... |
| `mehrere-verstoesse-und-art-83-3` | Wenn es um Mehrere Verstöße und Art. 83 Abs. 3 in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkte... |
| `milderung-durch-compliance-vor-dem-vorfall` | Wenn es um Milderung durch Compliance vor dem Vorfall in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken u... |
| `milderung-durch-remediation-nach-dem-vorfall` | Wenn es um Milderung durch Remediation nach dem Vorfall in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken... |
| `normenkollision-geheimnisse-und-datenschutzaufsicht` | Wenn es um Geheimnisse gegenüber Datenschutzaufsicht in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit G... |
| `oeffentliche-stellen-bussgeldprivilegien` | Wenn es um Öffentliche Stellen und Bußgeldfähigkeit in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `one-stop-shop-art-56-60` | Wenn es um One-Stop-Shop Art. 56 und 60 in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risi... |
| `organisationsverschulden-ersteinschaetzung` | Wenn es um Organisationsverschulden ersteinschätzen in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zus... |
| `parallelverfahren-art-82-massenklagen` | Wenn es um Parallelverfahren Art. 82 DSGVO und Massenklagen in Datenschutz-Sanktionsverfahren und Verteidigung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen... |
| `parallelverfahren-strafrecht-42-bdsg` | Wenn es um Parallelverfahren Paragraf 42 BDSG und Strafrecht in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt... |
| `privilege-und-mandatsgeheimnis` | Wenn es um Privilege Mandatsgeheimnis und Vertraulichkeit in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `profiling-und-automatisierte-entscheidungen` | Wenn es um Profiling und automatisierte Entscheidungen in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `public-sector-und-vergabefolgen` | Wenn es um Public Sector und Vergabefolgen in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| `rechtsbeschwerde-79-owig` | Wenn es um Rechtsbeschwerde Paragraf 79 OWiG in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rechtsweg-router-bussgeld-verwaltungsgericht-zivilverfahren` | Wenn es um Rechtsweg-Router Bußgeld Verwaltungsgericht Zivilverfahren in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert ein direkt nutzbares Arbeitsprodukt m... |
| `red-team-vor-jeder-einreichung` | Wenn es um Red Team vor jeder Einreichung in Datenschutz-Sanktionsverfahren und Verteidigung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sachverstaendige-it-forensik-im-bussgeldverfahren` | Wenn es um IT-Forensik und Sachverständige in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sanktionsmandat-schlussprodukt-planen` | Wenn es um Schlussprodukt des Sanktionsmandats planen in Datenschutz-Sanktionsverfahren und Verteidigung geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Opti... |
| `schlussmemo-und-lessons-learned` | Wenn es um Schlussmemo und Lessons Learned in Datenschutz-Sanktionsverfahren und Verteidigung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und... |
| `scope-cut-behoerdenfragen-einhegen` | Wenn es um Scope Cut Behördenfragen einhegen in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `selbstbelastungsfreiheit-und-mitwirkungspflichten` | Wenn es um Selbstbelastung und Mitwirkungspflichten in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `staatsanwaltschaft-im-dsgvo-owig` | Wenn es um Staatsanwaltschaft im DSGVO-OWiG-Verfahren in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken u... |
| `tracking-cookies-und-ttddg-schnittstelle` | Wenn es um Tracking Cookies und TDDDG-Schnittstelle in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfp... |
| `transferstopp-drittland-art-58` | Wenn es um Drittland-Transferstopp Art. 58 in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| `umsatz-und-wirtschaftliche-einheit` | Wenn es um Umsatz und wirtschaftliche Einheit in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unternehmensgruppe-und-federfuehrende-aufsicht` | Wenn es um Unternehmensgruppe und federführende Aufsicht in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `untersagung-und-verarbeitungsstopp` | Wenn es um Untersagung und Verarbeitungsstopp in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten... |
| `unverhaeltnismaessigkeit-und-existenzgefahr` | Wenn es um Verhältnismäßigkeit und Existenzgefahr in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verhaeltnismaessigkeit-aufsichtsmassnahme` | Wenn es um Verhältnismäßigkeit der Aufsichtsmaßnahme in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `veroeffentlichung-von-bussgeldentscheidungen` | Wenn es um Veröffentlichung von Bußgeldentscheidungen in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verteidigerrolle-dsb-gf-und-externe-berater` | Wenn es um Rollenklärung Verteidiger DSB Geschäftsleitung externe Berater in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Ar... |
| `verwarnung-art-58-2-b` | Wenn es um Verwarnung Art. 58 Abs. 2 lit. b in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `vg-anfechtungsklage-20-bdsg` | Wenn es um Anfechtungsklage nach Paragraf 20 BDSG in Datenschutz-Sanktionsverfahren und Verteidigung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründu... |
| `vg-eilrechtsschutz-80-5-vwgo` | Wenn es um Eilrechtsschutz Paragraf 80 Abs. 5 VwGO in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpu... |
| `videoueberwachung-und-biometrie` | Wenn es um Videoüberwachung und Biometrie in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vorbelastungen-und-wiederholungstaeter` | Wenn es um Vorbelastungen und Wiederholungstäter in Datenschutz-Sanktionsverfahren und Verteidigung geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `vorsatz-fahrlaessigkeit-unternehmen` | Wenn es um Vorsatz und Fahrlässigkeit des Unternehmens in Datenschutz-Sanktionsverfahren und Verteidigung geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Opt... |
| `vorstands-und-gf-briefing` | Wenn es um Vorstands- und Geschäftsführungsbriefing in Datenschutz-Sanktionsverfahren und Verteidigung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `wiedereinsetzung-nach-fristversaeumnis` | Wenn es um Wiedereinsetzung nach Fristversäumnis in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zeugeninterviews-mitarbeiter` | Wenn es um Mitarbeiterinterviews im Sanktionsverfahren in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-,... |
| `zustaendigkeit-amtsgericht-landgericht-41-bdsg` | Wenn es um Zuständigkeit Amtsgericht Landgericht Paragraf 41 BDSG in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Schnittstellenkarte mit Kollisions-,... |
| `zwangsgeld-und-vollstreckung-aufsicht` | Wenn es um Zwangsgeld und Vollstreckung der Aufsicht in Datenschutz-Sanktionsverfahren und Verteidigung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zwischenverfahren-69-owig` | Wenn es um Zwischenverfahren Paragraf 69 OWiG in Datenschutz-Sanktionsverfahren und Verteidigung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
