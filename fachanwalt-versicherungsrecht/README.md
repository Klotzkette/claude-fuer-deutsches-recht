# Fachanwalt Versicherungsrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Plugin Fachanwalt für Versicherungsrecht. VVG VAG Berufsunfähigkeit private Krankenversicherung Lebens- und Rentenversicherung Sachversicherung Haftpflicht D-und-O. Schnittstelle Plugin kanzlei-allgemein.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`fachanwalt-versicherungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-versicherungsrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-versicherungsrecht-werkstatt.md" download><code>fachanwalt-versicherungsrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-versicherungsrecht-schnellstart.md" download><code>fachanwalt-versicherungsrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-bu-deckungsklage-pflegekraft-vogelweide-aachen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bu-deckungsklage-pflegekraft-vogelweide-aachen.zip) (BU-Deckungsklage Pflegekraft Vogelweide Aachen); [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) (Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Deckungsanspruch prüfen und gegen die Ablehnung des Versicherers durchsetzen.
## Anwalts-Dashboard für den Schnelleinstieg

Der Skill `einstieg-routing` ist das Anwalts-Dashboard zu diesem Plugin:
Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch,
Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs,
Norm-Radar, Leitentscheidungs-Anker und genau eine Rueckfrage - bei
klarer Faktenlage sofort zum Spezial-Skill. Der Anwalt bleibt im Driver Seat.

Konvention: [`Install from .zip`](../references/anwalts-dashboard-konvention.md)
| Quellen-Anker: [`references/leitentscheidungen-anker.md`](../references/leitentscheidungen-anker.md)
| Quellenhygiene: [`references/quellenhygiene.md`](../references/quellenhygiene.md).


Plugin Fachanwalt für Versicherungsrecht. Orientierung VVG VAG Berufsunfähigkeit private Krankenversicherung Lebens- und Rentenversicherung Sachversicherung Haftpflicht D-und-O. Schnittstellen kanzlei-allgemein und fachanwalt-verkehrsrecht.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-versicherungsrecht-orientierung` | Orientierung im Versicherungsrecht — FAO Voraussetzungen Normen typische Mandate Fristen Quellenprüfung. VVG (Versicherungsvertragsgesetz) VAG (Versicherungsaufsichtsgesetz) Berufsunfähigkeit Krankenversicherung L… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 91 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Versicherungsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 12 VVG Klagefrist, Versicherungsschein, AVB, Schadensanzeige), dokumentiert Router-Entscheidung mit Begründung. |
| `berufsunfaehigkeit-fristen-form-und-zustaendigkeit` | Berufsunfaehigkeit: Fristen, Form, Zuständigkeit und Rechtsweg: Berufsunfaehigkeit: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `berufsunfaehigkeit-klage` | Klage bei abgelehnter Berufsunfähigkeitsversicherungs-Leistung: Anwendungsfall BU-Versicherung hat Leistungsantrag abgelehnt oder Verweisung auf andere Tätigkeit ausgesprochen. Normen §§ 172 ff... |
| `berufsunfaehigkeit-paragraf-172-vvg` | Berufsunfaehigkeit § 172 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `cyber-loesegeld-sanktionsrecht` | Cyber-Versicherung bei Ransomware mit Sanktionsrisiko und Geldwäscherecht: Anwendungsfall Unternehmen erhaelt Erpressung durch Ransomware und prüft Lösegeldzahlung auf Versicherungsd... |
| `deckungsanfrage-pruefen` | Prüfung von Versicherungsschadenfaellen und Deckungsablehnungen nach VVG: Anwendungsfall Versicherung hat Leistung abgelehnt oder eingeschraenkt und Mandant will wissen ob Klage Aussi... |
| `deckungsklage` | Deckungsklage gegen Versicherer auf Versicherungsleistung nach erfolgloser außergerichtlicher Phase: Anwendungsfall Versicherer verweigert Leistung endguelt... |
| `deckungsklage-mehrparteien-konflikt-und-interessen` | Deckungsklage: Mehrparteienkonflikt und Interessenmatrix: Deckungsklage: Mehrparteienkonflikt und Interessenmatrix. |
| `deckungspruefung-obliegenheiten-regress` | Deckungsprüfung, Obliegenheiten und Regressrisiko: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output: Deckungsprüfung, Obliegenheiten und Regressrisiko: führt schnell durch... |
| `do-deckungsabwehr` | D-und-O-Versicherung Directors-and-Officers Deckungsabwehr durch Versicherer bei Pflichtverletzungsansprüchen: Anwendungsfall Versicherung hat Dec... |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Versicherungsrecht: sortiert Versicherungsschein, AVB, Schadensanzeige, prüft Datum, Absender, Frist und Beweiswert (Schadensbilder, SV-Gutachten Schaden); markiert Lücken; berücksichtigt Mandatsgeheimnis... |
| `einfuehrung-sonderfall-edge-case` | Einfuehrung: Sonderfall und Edge-Case-Prüfung: Einfuehrung: Sonderfall und Edge-Case-Prüfung. |
| `einstieg-routing` | Anwalts-Dashboard Fachanwalt Versicherungsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der A... |
| `einstieg-schnelltriage-fallrouting` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Versicherungsrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodu... |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsw... |
| `erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel. |
| `fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage` | Klage bei abgelehnter Berufsunfähigkeitsversicherungs-Leistung. Anwendungsfall BU-Versicherung hat Leistungsantrag abgelehnt oder Verweisung auf andere Tätigkeit ausgesprochen. Normen §§ 172 ff. VVG BU-Versicherung § 15 VVG Anzeigepflich... |
| `fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht` | Cyber-Versicherung bei Ransomware mit Sanktionsrisiko und Geldwäscherecht. Anwendungsfall Unternehmen erhaelt Erpressung durch Ransomware und prüft Lösegeldzahlung auf Versicherungsdeckung und Sanktionsrechtsverstoesse. Normen VVG Cyber-... |
| `fachanwalt-versicherungsrecht-deckungsklage` | Deckungsklage gegen Versicherer auf Versicherungsleistung nach erfolgloser außergerichtlicher Phase. Anwendungsfall Versicherer verweigert Leistung endgueltig und Klage soll erhoben werden. Normen § 1 VVG Versicherungsanspruch § 215 VVG... |
| `fachanwalt-versicherungsrecht-do-deckungsabwehr` | D-und-O-Versicherung Directors-and-Officers Deckungsabwehr durch Versicherer bei Pflichtverletzungsansprüchen. Anwendungsfall Versicherung hat Deckung für Geschäftsführerhaftungsanspruch nach § 43 GmbHG abgelehnt. Normen § 43 GmbHG Haftu... |
| `fachanwalt-versicherungsrecht-lebensversicherung-rueckkauf` | Workflow-Skill zu fachanwalt versicherungsrecht lebensversicherung rueckkauf. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-versicherungsrecht-leistungsablehnung-pruefen` | Ablehnung des Versicherers prüfen nach §§ 1 28 VVG Obliegenheitsverletzung und Risikoausschluss. Anwendungsfall Versicherung hat Schadensantrag abgelehnt und Mandant fragt nach Erfolgsaussichten. Normen § 28 VVG Obliegenheitsverletzung §... |
| `fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung` | Außergerichtliche Schlichtung über Versicherungs-Ombudsmann oder PKV-Ombudsmann als Alternative zur Klage. Anwendungsfall Streitwert bis 10000 EUR oder Mandant will Klage vermeiden und Schlichtung versuchen. Normen §§ 214 ff. VVG Schlich... |
| `fachanwalt-versicherungsrecht-orientierung` | Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO. Anwendungsfall Kanzlei will Versicherungsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung Versicherungsrecht vor. Normen VVG VAG GDV-... |
| `fachanwalt-versicherungsrecht-regress-abwehr` | Regressabwehr gegen Sozialversicherungstraeger und Versicherungstraeger nach Schadensersatzleistung. Anwendungsfall Sozialversicherungstraeger oder Versicherung macht Regress auf Haftenden geltend. Normen § 116 SGB X Forderungsuebergang... |
| `fehlerkatalog` | Versr Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `gebaeudeversicherung-paragraf-86-vvg` | Gebaeudeversicherung § 86 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `haftpflicht-paragraf-100-vvg` | Haftpflicht § 100 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `haftpflicht-quellenkarte` | Haftpflicht Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `hausratversicherung-paragraf-19-vvg` | Hausratversicherung § 19 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `kanzlei-compliance-dokumentation-und-akte` | Kanzlei: Compliance-Dokumentation und Aktenvermerk: Kanzlei: Compliance-Dokumentation und Aktenvermerk. |
| `kfz-haftpflicht-paragraf-115-vvg` | kfz Haftpflicht § 115 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `klage-versicherer-strategie` | Klagestrategie gegen Versicherer nach erfolgloser außergerichtlicher Korrespondenz: Anwendungsfall alle außergerichtlichen Einigungsversuche sind gescheitert und Klage muss... |
| `krankenversicherung-risikoampel-und-gegenargumente` | Krankenversicherung: Risikoampel, Gegenargumente und Verteidigungslinien: Krankenversicherung: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `lebens-behoerden-gericht-und-registerweg` | Lebens: Behörden-, Gerichts- oder Registerweg: Lebens: Behörden-, Gerichts- oder Registerweg. |
| `lebensversicherung-rueckkauf` | Fachanwalt Versicherungsrecht Lebensversicherung Rueckkauf: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Versicherungsrecht Lebensversicherung Rueckkauf: ordnet No... |
| `lebensversicherung-widerruf-paragraf-152-vvg` | Lebensversicherung Widerruf § 152 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `leistungsablehnung-international-schnittstellen` | Leistungsablehnung: Internationaler Bezug und Schnittstellen: Leistungsablehnung: Internationaler Bezug und Schnittstellen. |
| `leistungsablehnung-pruefen` | Ablehnung des Versicherers prüfen nach §§ 1 28 VVG Obliegenheitsverletzung und Risikoausschluss: Anwendungsfall Versicherung hat Schadensantrag abgelehnt und Ma... |
| `mandat-triage-versicherungsrecht` | Strukturierte Eingangs-Abfrage für versicherungsrechtliche Mandate mit Fristen-Sofort-Check: Anwendungsfall neues Versicherungsmandat geht ein und muss schnell tria... |
| `obliegenheitsverletzung-mandantenentscheidung` | Obliegenheitsverletzung: Mandantenkommunikation und Entscheidungsvorlage: Obliegenheitsverletzung: Mandantenkommunikation und Entscheidungsvorlage. |
| `ombudsmann-gdv-schlichtung` | Außergerichtliche Schlichtung über Versicherungs-Ombudsmann oder PKV-Ombudsmann als Alternative zur Klage: Anwendungsfall Streitwert bis 10000 EUR ode... |
| `orientierung-mandat-fachanwaltschaft` | Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO: Anwendungsfall Kanzlei will Versicherungsmandat beurteilen oder Anwalt bereitet sich... |
| `output-waehlen` | Output-Wahl für Fachanwalt Versicherungsrecht: stimmt Adressat (Versicherungsnehmer, Versicherer, Geschädigter), Frist (§ 12 VVG Klagefrist) und Form auf den Zweck ab — typische Outputs: Deckungsklage, Schadensersatzklage, Ombudsmann-Ein... |
| `private-dokumentenmatrix-und-lueckenliste` | Private: Dokumentenmatrix, Lückenliste und Nachforderung: Private: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `private-krankenversicherung-paragraf-203-vvg` | Private Krankenversicherung § 203 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `pruefen-formular-portal-und-einreichung` | Prüfen: Formular, Portal und Einreichungslogik: Prüfen: Formular, Portal und Einreichungslogik. |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Versicherungsrecht: prüft Normen (VVG, PflVG, ZPO/Versicherungs-Streit) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Zivilgerichte und Quellenhygiene nach references/quellenhyg... |
| `rechtsschutz-beweislast-und-darlegungslast` | Rechtsschutz: Beweislast, Darlegungslast und Substantiierung: Rechtsschutz: Beweislast, Darlegungslast und Substantiierung. |
| `rechtsschutz-paragraf-3-arb` | Rechtsschutz § 3 arb: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `regress-abwehr` | Regressabwehr gegen Sozialversicherungstraeger und Versicherungstraeger nach Schadensersatzleistung: Anwendungsfall Sozialversicherungstraeger oder Versiche... |
| `rente-versicherung-paragraf-149-vvg` | Rente Versicherung § 149 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `rentenversicherung-schriftsatz-brief-und-memo-bausteine` | Rentenversicherung: Schriftsatz-, Brief- und Memo-Bausteine: Rentenversicherung: Schriftsatz-, Brief- und Memo-Bausteine. |
| `sachversicherung-verhandlung-vergleich-und-eskalation` | Sachversicherung: Verhandlung, Vergleich und Eskalation: Sachversicherung: Verhandlung, Vergleich und Eskalation. |
| `schnittstelle-zahlen-schwellen-und-berechnung` | Schnittstelle: Zahlen, Schwellenwerte und Berechnung: Schnittstelle: Zahlen, Schwellenwerte und Berechnung. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Deckungsklage, Klage BU/UB, Klage Sachversicherung, RSV-Deckungsklage: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau: Substantiierter Sch... |
| `spezial-deckungspruefung-obliegenheiten-regress` | Deckungsprüfung, Obliegenheiten und Regressrisiko: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-haftpflicht-livequellen-und-rechtsprechungscheck` | Haftpflicht: Livequellen- und Rechtsprechungscheck. |
| `spezial-pruefen-formular-portal-und-einreichung` | Pruefen: Formular, Portal und Einreichungslogik. |
| `spezial-versr-red-team-und-qualitaetskontrolle` | Versr: Red-Team und Qualitätskontrolle. |
| `themen-fristennotiz-und-naechster-schritt` | Themen: Fristennotiz und nächster Schritt: Themen: Fristennotiz und nächster Schritt. |
| `unfallversicherung-paragrafe-178-vvg` | Unfallversicherung §§ 178 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Versicherungsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Versicherungsschein, AVB, Schadensanzeige), nennt pro Lücke Beweisthema, Beschaffungsweg (Zivilgerichte), Frist und Ersatzn... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Versicherungsvertragsrecht (Personen- und Sachversicherung): ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleic... |
| `versicherungsrecht-tatbestand-beweis-und-belege` | Versicherungsrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage: Versicherungsrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `versr-bafin-ombudsmann-aufsichtsbeschwerde` | BaFin-Beschwerde, Versicherungsombudsmann, PKV-Ombudsmann und Klage taktisch wählen: BaFin-Beschwerde, Versicherungsombudsmann, PKV-Ombudsmann und Klage taktisch wählen. |
| `versr-bu-anerkennt-was-spezial` | Spezialfall Berufsunfaehigkeitsversicherung: Anerkennungsfaktum aktive Versicherung gegen Nachpruefung, konkrete und abstrakte Verweisung, 50-Prozent-BU: Spezialfall Berufsunfaehigkeitsversicherung: Anerkennungsfaktum aktive Versicherung... |
| `versr-bu-leistungspruefung-spezial` | Spezialfall BU-Leistungspruefung: Berufsbeschreibung, 50-Prozent-Grenze, Mitwirkungspflichten, Nachpruefungsverfahren: Prüfraster für Ver... |
| `versr-bu-nachpruefung-anerkenntnis` | BU-Anerkenntnis, Nachprüfung und Leistungseinstellung: Vergleichszustand, Gesundheitsverbesserung, Berufswechsel, Mitwirkung und Prozessstrategie: BU-Anerkenntnis, Nachprüfung und Leistungseinstellung: Vergleichszustand, Gesundheitsverbe... |
| `versr-cyber-ransomware-dora-sanktionen` | Cyberversicherung bei Ransomware: Deckung, Lösegeld, Forensik, DSGVO-Meldung, DORA/NIS2 und Sanktionsrecht: Cyberversicherung bei Ransomware: Deckung, Lösegeld, Forensik, DSGVO-Meldung, DORA/NIS2 und Sanktionsrecht. |
| `versr-d-o-claims-made-ausschluesse` | D&O-Deckung bei Organhaftung: Claims-made, Notice, Wissentlichkeit, Innenhaftung, Insolvenz, Abwehrkosten und Vergleichskontrolle: D&O-Deckung bei Organhaftung: Claims-made, Notice, Wissentlichkeit, Innenhaftung, Insolvenz, Abwehrkosten... |
| `versr-d-und-o-spezialfall` | Spezialfall D-and-O-Versicherung: Versicherte Person Vorstand und Aufsichtsrat, Innenhaftung, Versicherungsfall claims-made, Deckungsausschluesse: Spezialfall D-and-O-Versicherung: Versicherte Person Vorstand und Aufsichtsrat, Innenhaftu... |
| `versr-deckungsklage-leitfaden` | Leitfaden Deckungsklage in Haftpflicht und Rechtsschutz: Deckungszusage, Abwehrdeckung, Stichentscheid bei Erfolgsaussicht: Prüfrast... |
| `versr-deckungsprozess-215-vvg-beweislast` | Deckungsklage: Gerichtsstand § 215 VVG, Klageart, Beweislast, Sachverständige, Streitwert und Vergleichsfenster: Deckungsklage: Gerichtsstand § 215 VVG, Klageart, Beweislast, Sachverständige, Streitwert und Vergleichsfenster. |
| `versr-einfuehrung-themen` | Versicherungsrecht einfuehrend: Lebens-, Berufsunfaehigkeits-, Unfall-, Krankenversicherung, KFZ-Haftpflicht, Wohngebaeude, Hausrat, Rechtsschutz, gewerbliche Sparten: Versicherungsrecht einfuehrend: Lebens-, Berufsunfaehigkeits-, Unfall... |
| `versr-kreditausfall-restschuldversicherung` | Kreditausfall-, Warenkredit- und Restschuldversicherung: Limit, Ausfall, Obliegenheiten, Verbraucherdarlehen, Kopplung und Widerruf: Kreditausfall-, Warenkredit- und Restschuldversicherung: Limit, Ausfall, Obliegenheiten, Verbraucherdarl... |
| `versr-lebensversicherung-bezugsrecht-bewertungsreserven` | Lebensversicherung: Bezugsrecht, Erbfall, Scheidung, Sicherungsabtretung, Rückkaufswert, Überschüsse und Bewertungsreserven: Lebensversicherung: Bezugsrecht, Erbfall, Scheidung, Sicherungsabtretung, Rückkaufswert, Überschüsse und Bewertu... |
| `versr-obliegenheit-28-quotelung-kausalitaet` | Obliegenheitsverletzung nach § 28 VVG mit Vorsatz/grober Fahrlässigkeit, Rechtsfolgenbelehrung, Kausalitätsgegenbeweis und Quote: Obliegenheitsverletzung nach § 28 VVG mit Vorsatz/grober Fahrlässigkeit, Rechtsfolgenbelehrung, Kausalitäts... |
| `versr-obliegenheitsverletzung-praxis` | Obliegenheitsverletzung in der Praxis: § 28 VVG, Aufklaerungspflicht, Anzeigepflicht: Folgen Leistungsfreiheit bei Vorsatz, Quotelung bei grober Fahrlaessigkeit, Kausalita... |
| `versr-pkv-beitragsanpassung-medizinische-notwendigkeit` | PKV-Mandate zu Beitragsanpassung § 203 VVG, medizinischer Notwendigkeit, GOÄ/GOZ-Kürzung, Tarifwechsel und Rückforderung: PKV-Mandate zu Beitragsanpassung § 203 VVG, medizinischer Notwendigkeit, GOÄ/GOZ-Kürzung, Tarifwechsel und Rückford... |
| `versr-rechtsschutz-deckungsklage-spezial` | Spezialfall Rechtsschutzversicherungs-Deckungsklage: Wartezeit, Vorvertraglichkeit (BGH IV ZR), Stichentscheid, Streitwert in Deckungsklage: Spezialfall Rechtsschutzversicherungs-Deckungsklage: Wartezeit, Vorvertraglichkeit (BGH IV ZR),... |
| `versr-rechtsschutz-stichentscheid-vorvertraglichkeit` | Rechtsschutzversicherung: Deckungszusage, Stichentscheid, Vorvertraglichkeit, Mutwilligkeit, Kostenpositionen und RSV-Prozess: Rechtsschutzversicherung: Deckungszusage, Stichentscheid, Vorvertraglichkeit, Mutwilligkeit, Kostenpositionen... |
| `versr-regress-subrogation-86-vvg` | Regress, Legalzession, Quotenvorrecht, Sozialversicherungsträgerregress und Regressabwehr nach Regulierung: Regress, Legalzession, Quotenvorrecht, Sozialversicherungsträgerregress und Regressabwehr nach Regulierung. |
| `versr-versicherungsvertragspruefung-bauleiter` | Bauleiter Versicherungsvertragspruefung: vorvertragliche Anzeigepflicht § 19 VVG, Obliegenheiten § 28 VVG, Beweislast, Rechtsfolgen Verletzung: Bauleiter Versicherungsvertragspruefung: vorvertragliche Anzeigepflicht § 19 VVG, Obliegenhei... |
| `versr-vvg-anzeigepflicht-19-arglist` | Vorvertragliche Anzeigepflicht im Fachanwaltsmandat: Gesundheitsfragen, Belehrung, Rücktritt, Kündigung, Anpassung und Arglistanfechtung in BU/PKV/Leben/Unfall: Vorvertragliche Anzeigepflicht im Fachanwaltsmandat: Gesundheitsfragen, Bele... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
