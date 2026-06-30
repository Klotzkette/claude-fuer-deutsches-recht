# Memorandums-Ersteller

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral. Alias Memorandumsmacher.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`memorandums-ersteller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/memorandums-ersteller.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/memorandums-ersteller/memorandums-ersteller-werkstatt.md" download><code>memorandums-ersteller-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/memorandums-ersteller/memorandums-ersteller-schnellstart.md" download><code>memorandums-ersteller-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Grenzüberschreitender Asset-Deal Volkenrath Energie SE / Pipeline Northsea Ltd.: [Gesamt-PDF](../testakten/memorandum-grenzueberschreitender-asset-deal-volkenrath-energie/gesamt-pdf/memorandum-grenzueberschreitender-asset-deal-volkenrath-energie_gesamt.pdf), [`testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie.zip), [`testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `memorandums-ersteller` | Erzeugt aus heterogenen Mandantenunterlagen ein professionelles juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit lückenloser Quellenreferenzierung; Fragestellung als Ein-Satz-Fragen; Antworten als … |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 58 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anschluss-routing` | Anschluss-Routing für Memorandum-Ersteller: wählt den nächsten Spezial-Skill nach Engpass (Mandantenbericht-Fristen, Sachverhalt, Quellen, Vorergebnisse), dokumentiert Router-Entscheidung mit Begründung. |
| `antworten-interessen-ausfuehrungen-fragen` | Antworten: Mehrparteienkonflikt und Interessenmatrix. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `ausfuehrungen-formular-portal-und-einreichung` | Ausfuehrungen: Formular, Portal und Einreichungslogik. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `dokumente-intake` | Dokumentenintake für Memorandum-Ersteller: sortiert Sachverhalt, Quellen, Vorergebnisse, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `due-diligence-ergebnis-handlungsempfehlung` | Memo Rechtsteil einer Due Diligence: Material Findings, Issues List, Red Flags, Empfehlungen für SPA-Klauseln (Garantien, Freistellungen). Format DD-Memo mit Executive Summary, Detailfindings, Änderungsempfehlungen Kaufvertrag. Output: p... |
| `einstieg-routing` | Einstieg, Triage und Routing für Memorandum-Ersteller: ordnet Rolle (Mandant, Geschäftsleitung, Aufsichtsorgan), markiert Frist (Mandantenbericht-Fristen), wählt Norm (Anwendungsbereich nach Mandat) und Zuständigkeit (zuständige Stelle),... |
| `fragen-compliance-dokumentation-und-akte` | Fragen: Compliance-Dokumentation und Aktenvermerk. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `gliederung-mandantenunterlagen-memorandum` | Gliederung: Schriftsatz-, Brief- und Memo-Bausteine. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `haftungsrisiko-rechtsanwalt-board-pack` | Internes Memo zur Haftungspruefung: Mandantenbeziehung, vereinbarte Leistung, denkbare Pflichtverletzung, Schaden, Kausalitaet, Verjährung. Output: Haftungs-Memo für Kanzleileitung und Berufshaftpflichtversicherer. Pflicht-Hinweise an Ve... |
| `juristisches-questions-fristennotiz` | Juristisches: Fristen, Form, Zuständigkeit und Rechtsweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `laenge-formate-mandantenfreundliche-fassung` | Memo-Laenge an Komplexitaet anpassen: 1-Seiten-Antwort (schneller Mandant-Check), 3-5-Seiten-Memo (Standardfall), 10+-Seiten-Memo (komplexe Restrukturierung, M&A). Pro Format vorgegebene Inhalts-Skelette. Output: Wahl des passenden Forma... |
| `mandantenanfrage-schnell` | Schnell-Memo zu eingehender Mandantenanfrage: in 30 Minuten, einseitig, mit 3-Punkte-Plan. Anlass: Erstgespraech, Eilanruf, Hilfeanfrage Kanzleikollege. Format: Frage, Kurzantwort, Risiken, naechster Schritt, offene Punkte. Output: Memo-... |
| `mandantenkommunikation-redteam` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Memorandums Ersteller. |
| `mandantenunterlagen-tatbestand-beweis-und-belege` | Mandantenunterlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `memo-board-pack-besondere-anlaesse-spezial` | Spezialfall Memo als Bestandteil eines Board-Packs: Aufsichtsrat / Beirat, Eilfristen, vertrauliche Anlagen, Aktenzeichen. Prüfraster für Vorstand und Generalsekretariat im Memorandums Ersteller. |
| `memo-compliance-vorfall-intern` | Internes Compliance-Vorfall-Memo: Schwere des Vorfalls, betroffene Personen, betroffene Normen (KWG, MaRisk, GwG, DSGVO, KartellG), Meldepflichten, Sicherungsmassnahmen, Handlungsempfehlung. Speziell zu beachten: Self-Reporting-Linien (K... |
| `memo-ergebnis-handlungsempfehlung` | Ergebnis und Handlungsempfehlung trennen: Ergebnis ist die rechtliche Antwort, Handlungsempfehlung ist die operative Konsequenz. Empfehlung mit Optionen, Risikoabschaetzung, Kostenrahmen, naechster Schritt mit verantwortlicher Person und... |
| `memo-fristen-sofortmassnahmen` | Fristen und Sofortmassnahmen vor dem juristischen Inhalt: ein Memo beginnt mit 'Frist zuerst', wenn sich aus dem Sachverhalt erkennbare Termine ergeben (z. B. Klagefrist Kuendigungsschutzgesetz, Einspruch Strafbefehl). Output: Frist-Box... |
| `memo-fuer-mandant-vs-intern` | Memo für Mandanten unterscheidet sich vom internen Memo: weniger Streitstaende, mehr Empfehlungs-Klartext, Glossar für Fachbegriffe, klare Antwort 'ja/nein/teils' am Anfang. Internes Memo: vollstaendige Streitstaende, Risikobewertung, al... |
| `memo-mandantenfreundliche-fassung-spezial` | Spezialfall mandantenfreundliche Fassung eines juristischen Memos: Klartext, Handlungsoptionen, Risikoampel, Anhang für Tiefe. Prüfraster für Geschäftsleitung als Adressat im Memorandums Ersteller. |
| `memo-memo-typenuebersicht-bauleiter` | Bauleiter Memo-Typen: Kurz-Memo, Standard-Memo, Long-Form-Memo, Risk-Memo. Prüfraster für Zielgruppe, Tiefe und Format. Mustertext Inhaltsverzeichnis pro Typ im Memorandums Ersteller. |
| `memo-pruefung-im-gutachtenstil` | Prüfungsabschnitt im Gutachtenstil: Obersatz, Definition, Subsumtion, Zwischenergebnis. Streitiges nur dann oeffnen, wenn für das Ergebnis relevant. BGH-Linien werden zitiert, nicht referiert. Output mit klaren Ueberschriften und kurzer... |
| `memo-quellen-zitierregel` | Quellenzitate im Memo nach deutscher Hauszitierweise v4: Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link; Literatur, Kommentare und Datenbankfundstellen nur bei Nutzerquelle oder dokumentiertem Live-Zugriff im Mem... |
| `memo-rechtsfragen-formulieren` | Rechtsfragen praezise formulieren: jede Frage in einer Frage, mit normativem Bezug. Schlechte Formulierung 'Was sind die rechtlichen Folgen' wird ersetzt durch 'Hat der Mandant einen Anspruch gegen X auf Y aus Norm Z'. Liste der haeufigs... |
| `memo-research-tracking-leitfaden` | Leitfaden Research- und Quellen-Tracking für Memos: Quellenarten, Zitierregeln dejure.org / openjur, BGH / BVerfG / EuGH, Versionierung. Prüfraster für Erstautor und Review im Memorandums Ersteller. |
| `memo-vier-teile-aufbau` | Vier-Teile-Memo aufbauen: 1 Sachverhalt, 2 Rechtsfragen, 3 Prüfung mit Subsumtion, 4 Ergebnis und Handlungsempfehlung. Jede Sektion mit Mindestumfang und Pflicht-Inhalten. Beispiel-Geruest für Mandanten-Memo und für kanzleiinternes Junio... |
| `memo-zu-grenzueberschreitenden-faellen` | Memo zu grenzueberschreitenden Faellen: anwendbares Recht (Rom I / Rom II), zuständiges Gericht (Brueessel Ia, EuGVVO), Anerkennung und Vollstreckung im Ausland. Output: kurzes IPR/IZPR-Memo mit Empfehlung zum Gerichtsstand und Vollstrec... |
| `memo-zur-rechtsmittelentscheidung` | Rechtsmittel-Memo: Berufung/Revision/Beschwerde nach erstinstanzlicher Niederlage. Erfolgsaussichten, Kosten, Zeitfaktor, Mandantenpraeferenz. Prüfraster: Welche Beanstandungen tragen wirklich? Mandantenrisiko bei Verschlechterung. Outpu... |
| `memo-zur-vertragsentscheidung` | Vertragsentscheidungs-Memo: Soll der Mandant Vertrag X mit Bedingungen Y abschliessen? Prüfung wirtschaftliche und rechtliche Risiken, Verhandlungsspielraum, BATNA, Empfehlung. Output: Memo mit klarer Empfehlung 'abschliessen/nachverhand... |
| `memorandum-dokumentenmatrix-und-lueckenliste` | Memorandum: Dokumentenmatrix, Lückenliste und Nachforderung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `memorandums-ersteller` | Erstellt ein professionelles juristisches Memorandum aus heterogenen Mandantenunterlagen. Anwendungsfall Mandant hat Unterlagen eingereicht und Kanzlei soll Rechtslage in Memorandumsform aufbereiten. Normen rechtsgebietsneutral einsetzba... |
| `optional-beweislast-piercing-sonderfall` | Optional: Beweislast, Darlegungslast und Substantiierung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `output-waehlen` | Output-Wahl für Memorandum-Ersteller: stimmt Adressat (Mandant, Geschäftsleitung, Aufsichtsorgan), Frist (Mandantenbericht-Fristen) und Form auf den Zweck ab — typische Outputs: Memo im Gutachtenstil, Executive Summary, Risikomatrix. |
| `piercing-sonderfall-und-edge-case` | Piercing: Sonderfall und Edge-Case-Prüfung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `pinpoint-fehlerkatalog` | Pinpoint Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `prozessstrategie-klageerhebung-gutachtenstil` | Memo zur Prozessstrategie vor Klageerhebung: Erfolgsaussichten, Streitwert, Kosten, Beweislage, Vergleichsbereitschaft Gegner, Vollstreckungsaussichten. Output: Memo mit Empfehlung 'Klage erheben/aussergerichtlich verhandeln/abwarten' un... |
| `quellen-livecheck` | Quellen-Live-Check für Memorandum-Ersteller: prüft Normen (Anwendungsbereich nach Mandat) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt zuständige Stelle und Quellenhygiene nach references/quellenhygiene.md. |
| `quellenreferenz-quellenkarte` | Quellenreferenz Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `questions-fristennotiz-und-naechster-schritt` | Questions: Fristennotiz und nächster Schritt. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `rechtliche-internationaler-bezug-und-schnittstellen` | Rechtliche: Internationaler Bezug und Schnittstellen. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `rechtsfortbildung-bgh-rechtsfragen` | Memo zu aktueller BGH-Entscheidung: Sachverhalt der Entscheidung, Leitsatz, Rechtsfrage, Begruendung BGH, praktische Auswirkungen für die Kanzlei. Format Update-Memo für Mandanten und Anwaltskollegen. Pflicht: Originalfundstelle, dejure.... |
| `rechtsgebietsneutral-sachverhalt-satz` | Rechtsgebietsneutral: Abschlussprodukt und Übergabe. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `sachverhalt-fixieren-vier-teile` | Sachverhalt sauber fixieren: zeitliche, raeumliche, personelle Ordnung, Unterscheidung 'unstreitig' / 'streitig' / 'unklar' / 'Annahme'. Vermeidet juristisches Wertvokabular im Sachverhalt. Markiert Tatsachen, für die Belege im Mandanten... |
| `sachverhalt-verhandlung-vergleich-und-eskalation` | Sachverhalt: Verhandlung, Vergleich und Eskalation. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `satz-zahlen-schwellen-und-berechnung` | Satz: Zahlen, Schwellenwerte und Berechnung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `spezial-pinpoint-red-team-und-qualitaetskontrolle` | Pinpoint: Red-Team und Qualitätskontrolle. |
| `spezial-quellenreferenz-livequellen-und-rechtsprechungscheck` | Quellenreferenz: Livequellen- und Rechtsprechungscheck. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Memorandums Ersteller-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei D... |
| `teile-vier-wandelt` | Teile: Behörden-, Gerichts- oder Registerweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Memorandum-Ersteller: trennt fehlende Tatsachen von fehlenden Belegen (Sachverhalt, Quellen, Vorergebnisse), nennt pro Lücke Beweisthema, Beschaffungsweg (zuständige Stelle), Frist und Ersatznachweis. |
| `vier-risikoampel-und-gegenargumente` | Vier: Risikoampel, Gegenargumente und Verteidigungslinien. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `wandelt-erstpruefung-und-mandatsziel` | Wandelt: Erstprüfung, Rollenklärung und Mandatsziel. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Memorandums Ersteller. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Memorandums Ersteller. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Memorandums Ersteller. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zitierung-mandantenkommunikation-entscheidungsvorlage` | Zitierung: Mandantenkommunikation und Entscheidungsvorlage: Zitierung: Mandantenkommunikation und Entscheidungsvorlage. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
