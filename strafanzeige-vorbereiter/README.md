# Strafanzeige-Vorbereiter

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strafanzeige-vorbereiter`) | [`strafanzeige-vorbereiter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafanzeige-vorbereiter.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist ausdrücklich keine Strafanzeigenkanone. Es soll Gerichte und Staatsanwaltschaften nicht mit wütenden, unbelegten Anzeigen fluten und niemanden durch haltlose Vorwürfe unter Druck setzen. Wenn eine Strafanzeige aber nötig ist, führt es zu einem sauberen, nüchternen, beweisnahen Entwurf.

## Leitplanke

Wehe, es werden Dinge behauptet, die nicht stimmen. Das Plugin zwingt zur Trennung von eigener Wahrnehmung, Dokument, Zeuge, Vermutung und rechtlicher Bewertung. Bei eigener Beteiligung, Unternehmensfällen, schweren Gewalt-/Sexualdelikten, Wirtschaftsstrafsachen oder Berufsgeheimnissen: anwaltliche Hilfe einschalten.

## Was dieses Plugin gut kann

- Trennt Strafanzeige, Strafantrag, zivilrechtliche Alternativen und bloße Beschwerde.
- Prüft vorab § 164 StGB, §§ 186/187 StGB, § 824 BGB und Druckmittelrisiken.
- Baut Sachverhalt, Beweismatrix, Anlagenverzeichnis und Strafantragsfristen auf.
- Erzeugt erst am Ende einen Anzeigeentwurf, wenn die Tatsachenbasis trägt.

## Startlogik

Beginne mit dem allgemeinen Kaltstart-Skill. Er fragt Rolle, Ziel, Frist, Unterlagen, Risiken und gewünschten Output ab. Danach werden nur passende Spezial-Skills vorgeschlagen.

## Quellenhygiene

Normtexte werden aus amtlichen Quellen geprüft. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle verwendet. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 56 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `akteneinsicht-verletzter-406e` | Akteneinsicht für Verletzte und ihre Anwälte: Voraussetzungen, Schutzinteressen, Datenschutz und Taktik im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priori... |
| `anfangsverdacht-anlagenverzeichnis` | Anfangsverdacht strukturieren: zureichende tatsächliche Anhaltspunkte, Ermittlungsauftrag der StA, keine bloße Spekulation im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprech... |
| `anlagenverzeichnis-hashlog` | Anlagen zu Strafanzeigen: Nummerierung, Hashwerte, Originale, Kopien, Versandnachweis und digitale Kette im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prior... |
| `antragsdelikte-strafantrag` | Strafantragsfrist und Antragsberechtigung bei Beleidigung, Hausfriedensbruch, einfacher Körperverletzung und weiteren Antragsdelikten im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und... |
| `anwalt-arbeitsplatz` | Schwellen für anwaltliche Hilfe: eigene Beteiligung, Wirtschaftsstrafrecht, Sexual-/Gewaltdelikte, Berufsgeheimnisse, Unternehmen, Presse im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege... |
| `arbeitsplatz-sexuelle-belaestigung` | Arbeitsplatzvorfälle: strafrechtliche Anzeige, AGG/Arbeitsrecht, Beweise, Schutz, interne Untersuchung und Betroffenenrechte im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtspre... |
| `bankrott-bedrohung` | Bankrott und Buchführungsdelikte: Vermögensverschiebung, Buchführung, Krise, Gläubigerbenachteiligung und Insolvenzakten im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechun... |
| `bedrohung-241` | Bedrohung anzeigen: Inhalt, Ernstlichkeit, Adressat, Beweise, Schutzmaßnahmen im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pi... |
| `beleidigung-betrug` | Beleidigung anzeigen: Kontext, Meinungsfreiheit, Strafantrag, Beweise, Plattform/Arbeitsplatz im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Ou... |
| `betrug-263` | Betrugsanzeige: Täuschung, Irrtum, Vermögensverfügung, Schaden, Vorsatz, Belege und zivilrechtliche Parallelspur im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefe... |
| `beweismatrix-chatverlaeufe` | Ordnet jedes Element der Anzeige nach Tatsachenwissen, Beleg, Zeuge, Dokument, Meinung und Vermutung im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisie... |
| `chatverlaeufe-emails-header` | Chatverläufe, EML-Dateien, E-Mail-Header, Messenger-Screenshots, Export und Kontext sichern im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Outp... |
| `computerbetrug-phishing` | Computerbetrug/Phishing anzeigen: Zahlungsdaten, TAN, Social Engineering, Bankkommunikation, Logs und Sofortmaßnahmen im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung.... |
| `datenstraftaten-diebstahl` | Ausspähen, Abfangen, Datenveränderung, Computersabotage: technische Beweise, Logs, Forensik und ZAC im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisier... |
| `diebstahl-unterschlagung` | Diebstahl/Unterschlagung anzeigen: Gewahrsam, Eigentum, Wegnahme, Zueignung, Beweise, Herausgabeverlangen im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prio... |
| `druckmittel-falsche` | Prüft, ob Drohung mit Strafanzeige oder Anzeige selbst als unzulässiges Druckmittel/Nötigung wirken kann im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prior... |
| `falsche-verdaechtigung-164` | Warn- und Prüfskill zu § 164 StGB: niemanden sicher beschuldigen, wenn nur Verdachtsmomente oder Hörensagen vorliegen im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung.... |
| `gegenanzeige-geldwaesche` | Risiko der Gegenanzeige wegen falscher Verdächtigung, Verleumdung, Nötigung, Datenschutzverstoß oder Prozessbetrug im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lie... |
| `geldwaesche-261` | Geldwäscheverdacht: Tatertrag, Verschleierung, Transaktionen, GwG-Verdachtsmeldung vs Strafanzeige im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisiert... |
| `geschgehg-haeusliche` | Geschäftsgeheimnis-Strafanzeige: Geheimnisqualität, angemessene Geheimhaltungsmaßnahmen, Erlangen/Nutzen/Offenlegen, Strafantrag im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Recht... |
| `haeusliche-gewalt-gewschg` | Strafanzeige bei häuslicher Gewalt plus Schutzanordnung, Beweissicherung, medizinische Dokumentation und Sicherheitsplan im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechun... |
| `hausfriedensbruch` | Hausfriedensbruch anzeigen: befriedetes Besitztum, Wohnung/Geschäft, Aufforderung zu gehen, Strafantrag im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priori... |
| `insolvenzverschleppung-15a` | Insolvenzverschleppung anzeigen: Organstellung, Zahlungsunfähigkeit/Überschuldung, Fristen, Gläubigerschaden und Belege im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung... |
| `international-klageerzwingung` | Internationale Sachverhalte: Tatort, Zuständigkeit, Europol/Interpol nicht direkt, ausländische Behörden, Übersetzungen und Beweise im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Re... |
| `kaltstart-routing` | Geführter Einstieg für Strafanzeigen: Sachverhalt, Beweise, Straftatverdacht, Strafantrag, Risiken falscher Verdächtigung, Alternativen und anwaltliche Eskalationsschwelle. |
| `klageerzwingung-172-stpo` | Nach Einstellung: Beschwerde, Klageerzwingung, Fristen, Verletztenstellung und anwaltliche Schwelle im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisier... |
| `koerperverletzung-korruption` | Körperverletzung: Verletzung, Arztbericht, Fotos, Zeugen, Strafantrag bei § 223 und besonderes öffentliches Interesse im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung.... |
| `korruption-299-331ff` | Korruptionsanzeige: Bestechlichkeit/Bestechung im geschäftlichen Verkehr oder Amt, Vorteil, Unrechtsvereinbarung, Belege, Selbstbelastung im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege... |
| `kreditgefaehrdung-minderjaehrige` | Zivilrechtliches Haftungsrisiko bei Behauptungen über Insolvenz, Betrug, Zahlungsunfähigkeit oder Unzuverlässigkeit im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Li... |
| `minderjaehrige-schule` | Strafanzeige bei Minderjährigen/Schule: Jugendstrafrecht, Schutz, Schulrecht, Eltern, Jugendamt und Deeskalation im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefe... |
| `muster-noetigung` | Erzeugt eine nüchterne Strafanzeige mit optionalem Strafantrag, Anlagen, Beweismatrix und Risikoformulierungen im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `nicht-anzeigen-redteam` | Red-Team prüft, ob eine Strafanzeige unnötig, riskant, zivilrechtlich kontraproduktiv oder straf-/haftungsrechtlich gefährlich wäre. |
| `noetigung-240` | Nötigung prüfen: Gewalt/Drohung, empfindliches Übel, Verwerflichkeit, legitime Anzeigeandrohung vs. Missbrauch im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `notruf-online` | Akute Gefahr, laufende Tat, Selbst-/Fremdgefährdung: Sofort Polizei/112/110 statt Entwurf im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `online-plattform-screenshots` | Screenshots, URLs, Zeitstempel, Accountdaten, Plattformmeldungen und Löschrisiko beweissicher sichern im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisi... |
| `onlinewache-opferschutz` | Adressat und Form: Onlinewache, Polizeidienststelle, Staatsanwaltschaft, Spezialdienststelle Cybercrime, Zoll oder Finanzbehörde im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Recht... |
| `opferschutz-nebenklage` | Rechte Verletzter: Nebenklage, psychosoziale Prozessbegleitung, Adhäsion, Schutzanordnung, Akteneinsicht im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prior... |
| `rechtsfolgen-ruecknahme` | Strafanzeige mit Zivilrecht koordinieren: Schadensersatz, Unterlassung, einstweilige Verfügung, Kündigung, Versicherung, Adhäsion im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rech... |
| `ruecknahme-einstellung-170-153` | Was nach Anzeige passiert: Einstellung, Rücknahme Strafantrag, Opportunität, Beschwerde, Kommunikation mit StA im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `sachbeschaedigung-sachverhalt` | Sachbeschädigung: Beschädigung/Zerstörung/Veränderung, Fotos, Kostenvoranschlag, Strafantrag, Zivilforderung im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert p... |
| `sachverhalt-ohne-adjektive` | Entfernt Polemik und Rechtswertungen aus Anzeigen; schreibt nüchtern, präzise und beweisnah im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Outp... |
| `stalking-vs` | Nachstellung anzeigen: wiederholtes Verhalten, Eignung zur Beeinträchtigung, Dokumentation, Kontaktverbote und Plattformbeweise im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechts... |
| `steuerhinterziehung-akteneinsicht` | Steuerstraftaten anzeigen oder Selbstbelastung vermeiden: Drittanzeige, Selbstanzeige-Abgrenzung, Belege, Finanzamt/Steufa im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprech... |
| `strafantrag-form-frist` | Strafantrag richtig stellen, beweisen und Rücknahmefolgen prüfen im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risi... |
| `strafanzeige-vs-strafantrag-158` | Unterscheidet Strafanzeige, Strafantrag, Dienstaufsichtsbeschwerde, Privatklage und zivilrechtliche Abmahnung im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `tierschutz-ueblerede` | Tierschutzanzeige: erhebliche Schmerzen/Leiden, Rohheit, länger anhaltende Wiederholung, Veterinäramt und Beweise im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lief... |
| `ueblerede-verleumdung-186-187` | Strafanzeige und Kommunikation so formulieren, dass keine unnötige ehrverletzende Drittverbreitung entsteht im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert pr... |
| `umweltstraftaten-unternehmen` | Umweltstraftaten anzeigen: Gewässer, Boden, Luft, Abfall, Genehmigungen, Beweise und Umweltbehörde im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisiert... |
| `unternehmen-internal-investigation` | Unternehmensanzeige nach interner Untersuchung: Legal Hold, Mitarbeiterinterviews, Datenschutz, Arbeitsrecht, Beschlagnahmerisiko und Bericht im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Bel... |
| `untreue-urheberrecht` | Untreue anzeigen: Vermögensbetreuungspflicht, Pflichtverletzung, Vermögensnachteil, Organ-/Mitarbeiterfälle im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert pr... |
| `urheberrecht-markenrecht` | IP-Strafanzeigen bei Urheber-, Marken-, Design- und Patentrechtsverletzungen: Strafantrag, Testkauf, Originalitätsnachweis, Zoll im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Recht... |
| `verkehrsunfall-video` | Unerlaubtes Entfernen vom Unfallort: Schaden, Wartepflicht, Feststellungen, Dashcam/Zeugen, Selbstmeldung im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prio... |
| `video-audio-kug-201` | Video-/Audioaufnahmen als Beweis: Recht am Bild, Vertraulichkeit des Wortes, öffentliche Situation, Polizei/Versammlung und Veröffentlichungsverbot im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Friste... |
| `wer-zeugenliste` | Sachverhaltskern einer Anzeige: chronologisch, nüchtern, belegbar, ohne Polemik im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-... |
| `whistleblower-computerbetrug` | Hinweisgebermeldung, interne Stelle, externe Meldung, Strafanzeige und Schutz vor Repressalien koordinieren im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert pr... |
| `zeugenliste-kontakt` | Zeugen benennen, aber nicht beeinflussen: Kontaktdaten, Wahrnehmung, Reihenfolge und Dokumentation im Strafanzeige-Vorbereitung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisiert... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
