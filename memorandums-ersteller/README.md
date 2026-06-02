# Memorandums-Ersteller

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`memorandums-ersteller`) | [`memorandums-ersteller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/memorandums-ersteller.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Grenzüberschreitender Asset-Deal Volkenrath Energie SE / Pipeline Northsea Ltd.** (`memorandum-grenzueberschreitender-asset-deal-volkenrath-energie`) | [Gesamt-PDF lesen](../testakten/memorandum-grenzueberschreitender-asset-deal-volkenrath-energie/gesamt-pdf/memorandum-grenzueberschreitender-asset-deal-volkenrath-energie_gesamt.pdf) | [`testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-memorandum-grenzueberschreitender-asset-deal-volkenrath-energie.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Memorandums-Ersteller (`memorandums-ersteller`, dieses Plugin) | [memorandums-ersteller.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/memorandums-ersteller.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
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

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Memorandums Ersteller-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `memo-board-pack-besondere-anlaesse-spezial` | Spezialfall Memo als Bestandteil eines Board-Packs: Aufsichtsrat / Beirat, Eilfristen, vertrauliche Anlagen, Aktenzeichen. Pruefraster fuer Vorstand und Generalsekretariat. |
| `memo-compliance-vorfall-intern` | Internes Compliance-Vorfall-Memo: Schwere des Vorfalls, betroffene Personen, betroffene Normen (KWG, MaRisk, GwG, DSGVO, KartellG), Meldepflichten, Sicherungsmassnahmen, Handlungsempfehlung. Speziell zu beachten: Self-Reporting-Linien (K... |
| `memo-due-diligence-rechtsteil` | Memo Rechtsteil einer Due Diligence: Material Findings, Issues List, Red Flags, Empfehlungen fuer SPA-Klauseln (Garantien, Freistellungen). Format DD-Memo mit Executive Summary, Detailfindings, Aenderungsempfehlungen Kaufvertrag. Output:... |
| `memo-ergebnis-handlungsempfehlung` | Ergebnis und Handlungsempfehlung trennen: Ergebnis ist die rechtliche Antwort, Handlungsempfehlung ist die operative Konsequenz. Empfehlung mit Optionen, Risikoabschaetzung, Kostenrahmen, naechster Schritt mit verantwortlicher Person und... |
| `memo-fristen-sofortmassnahmen` | Fristen und Sofortmassnahmen vor dem juristischen Inhalt: ein Memo beginnt mit 'Frist zuerst', wenn sich aus dem Sachverhalt erkennbare Termine ergeben (z. B. Klagefrist Kuendigungsschutzgesetz, Einspruch Strafbefehl). Output: Frist-Box... |
| `memo-fuer-mandant-vs-intern` | Memo fuer Mandanten unterscheidet sich vom internen Memo: weniger Streitstaende, mehr Empfehlungs-Klartext, Glossar fuer Fachbegriffe, klare Antwort 'ja/nein/teils' am Anfang. Internes Memo: vollstaendige Streitstaende, Risikobewertung,... |
| `memo-haftungsrisiko-rechtsanwalt` | Internes Memo zur Haftungspruefung: Mandantenbeziehung, vereinbarte Leistung, denkbare Pflichtverletzung, Schaden, Kausalitaet, Verjaehrung. Output: Haftungs-Memo fuer Kanzleileitung und Berufshaftpflichtversicherer. Pflicht-Hinweise an... |
| `memo-laenge-und-formate` | Memo-Laenge an Komplexitaet anpassen: 1-Seiten-Antwort (schneller Mandant-Check), 3-5-Seiten-Memo (Standardfall), 10+-Seiten-Memo (komplexe Restrukturierung, M&A). Pro Format vorgegebene Inhalts-Skelette. Output: Wahl des passenden Formats. |
| `memo-mandantenfreundliche-fassung-spezial` | Spezialfall mandantenfreundliche Fassung eines juristischen Memos: Klartext, Handlungsoptionen, Risikoampel, Anhang fuer Tiefe. Pruefraster fuer Geschaeftsleitung als Adressat. |
| `memo-memo-typenuebersicht-bauleiter` | Bauleiter Memo-Typen: Kurz-Memo, Standard-Memo, Long-Form-Memo, Risk-Memo. Pruefraster fuer Zielgruppe, Tiefe und Format. Mustertext Inhaltsverzeichnis pro Typ. |
| `memo-prozessstrategie-vor-klageerhebung` | Memo zur Prozessstrategie vor Klageerhebung: Erfolgsaussichten, Streitwert, Kosten, Beweislage, Vergleichsbereitschaft Gegner, Vollstreckungsaussichten. Output: Memo mit Empfehlung 'Klage erheben/aussergerichtlich verhandeln/abwarten' un... |
| `memo-pruefung-im-gutachtenstil` | Pruefungsabschnitt im Gutachtenstil: Obersatz, Definition, Subsumtion, Zwischenergebnis. Streitiges nur dann oeffnen, wenn fuer das Ergebnis relevant. BGH-Linien werden zitiert, nicht referiert. Output mit klaren Ueberschriften und kurze... |
| `memo-quellen-zitierregel` | Quellenzitate im Memo nach deutscher Hauszitierweise v4: Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link; Literatur, Kommentare und Datenbankfundstellen nur bei Nutzerquelle oder dokumentiertem Live-Zugriff. |
| `memo-rechtsfortbildung-bgh-aktuell` | Memo zu aktueller BGH-Entscheidung: Sachverhalt der Entscheidung, Leitsatz, Rechtsfrage, Begruendung BGH, praktische Auswirkungen fuer die Kanzlei. Format Update-Memo fuer Mandanten und Anwaltskollegen. Pflicht: Originalfundstelle, dejur... |
| `memo-rechtsfragen-formulieren` | Rechtsfragen praezise formulieren: jede Frage in einer Frage, mit normativem Bezug. Schlechte Formulierung 'Was sind die rechtlichen Folgen' wird ersetzt durch 'Hat der Mandant einen Anspruch gegen X auf Y aus Norm Z'. Liste der haeufigs... |
| `memo-research-tracking-leitfaden` | Leitfaden Research- und Quellen-Tracking fuer Memos: Quellenarten, Zitierregeln dejure.org / openjur, BGH / BVerfG / EuGH, Versionierung. Pruefraster fuer Erstautor und Review. |
| `memo-sachverhalt-fixieren` | Sachverhalt sauber fixieren: zeitliche, raeumliche, personelle Ordnung, Unterscheidung 'unstreitig' / 'streitig' / 'unklar' / 'Annahme'. Vermeidet juristisches Wertvokabular im Sachverhalt. Markiert Tatsachen, fuer die Belege im Mandante... |
| `memo-vier-teile-aufbau` | Vier-Teile-Memo aufbauen: 1) Sachverhalt, 2) Rechtsfrage(n), 3) Pruefung mit Subsumtion, 4) Ergebnis und Handlungsempfehlung. Jede Sektion mit Mindestumfang und Pflicht-Inhalten. Beispiel-Geruest fuer Mandanten-Memo und fuer kanzleiinter... |
| `memo-zu-grenzueberschreitenden-faellen` | Memo zu grenzueberschreitenden Faellen: anwendbares Recht (Rom I / Rom II), zustaendiges Gericht (Brueessel Ia, EuGVVO), Anerkennung und Vollstreckung im Ausland. Output: kurzes IPR/IZPR-Memo mit Empfehlung zum Gerichtsstand und Vollstre... |
| `memo-zu-mandantenanfrage-schnell` | Schnell-Memo zu eingehender Mandantenanfrage: in 30 Minuten, einseitig, mit 3-Punkte-Plan. Anlass: Erstgespraech, Eilanruf, Hilfeanfrage Kanzleikollege. Format: Frage, Kurzantwort, Risiken, naechster Schritt, offene Punkte. Output: Memo-... |
| `memo-zur-rechtsmittelentscheidung` | Rechtsmittel-Memo: Berufung/Revision/Beschwerde nach erstinstanzlicher Niederlage. Erfolgsaussichten, Kosten, Zeitfaktor, Mandantenpraeferenz. Pruefraster: Welche Beanstandungen tragen wirklich? Mandantenrisiko bei Verschlechterung. Outp... |
| `memo-zur-vertragsentscheidung` | Vertragsentscheidungs-Memo: Soll der Mandant Vertrag X mit Bedingungen Y abschliessen? Pruefung wirtschaftliche und rechtliche Risiken, Verhandlungsspielraum, BATNA, Empfehlung. Output: Memo mit klarer Empfehlung 'abschliessen/nachverhan... |
| `memorandums-ersteller` | Erstellt ein professionelles juristisches Memorandum aus heterogenen Mandantenunterlagen. Anwendungsfall Mandant hat Unterlagen eingereicht und Kanzlei soll Rechtslage in Memorandumsform aufbereiten. Normen rechtsgebietsneutral einsetzba... |
| `spezial-antworten-mehrparteien-konflikt-und-interessen` | Antworten: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ausfuehrungen-formular-portal-und-einreichung` | Ausfuehrungen: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fragen-compliance-dokumentation-und-akte` | Fragen: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gliederung-schriftsatz-brief-und-memo-bausteine` | Gliederung: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-juristisches-fristen-form-und-zustaendigkeit` | Juristisches: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mandantenunterlagen-tatbestand-beweis-und-belege` | Mandantenunterlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-memorandum-dokumentenmatrix-und-lueckenliste` | Memorandum: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-optional-beweislast-und-darlegungslast` | Optional: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-piercing-sonderfall-und-edge-case` | Piercing: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pinpoint-red-team-und-qualitaetskontrolle` | Pinpoint: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-quellenreferenz-livequellen-und-rechtsprechungscheck` | Quellenreferenz: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-questions-fristennotiz-und-naechster-schritt` | Questions: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtliche-internationaler-bezug-und-schnittstellen` | Rechtliche: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsgebietsneutral-abschlussprodukt-und-uebergabe` | Rechtsgebietsneutral: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-sachverhalt-verhandlung-vergleich-und-eskalation` | Sachverhalt: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-satz-zahlen-schwellen-und-berechnung` | Satz: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-teile-behoerden-gericht-und-registerweg` | Teile: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vier-risikoampel-und-gegenargumente` | Vier: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-wandelt-erstpruefung-und-mandatsziel` | Wandelt: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zitierung-mandantenkommunikation-entscheidungsvorlage` | Zitierung: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin memorandums-ersteller: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin memorandums-ersteller: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin memorandums-ersteller: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin memorandums-ersteller: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin memorandums-ersteller: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin memorandums-ersteller: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin memorandums-ersteller: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin memorandums-ersteller: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin memorandums-ersteller: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin memorandums-ersteller: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
