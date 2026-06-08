# Fachanwalt Verkehrsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-verkehrsrecht`) | [`fachanwalt-verkehrsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-verkehrsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **StVO-Akte Schulstraße/Lieferzone** (`strassenverkehrsrecht-stvo-schulstrasse-lieferzone`) | [Gesamt-PDF lesen](../testakten/strassenverkehrsrecht-stvo-schulstrasse-lieferzone/gesamt-pdf/strassenverkehrsrecht-stvo-schulstrasse-lieferzone_gesamt.pdf) | [`testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strassenverkehrsrecht-stvo-schulstrasse-lieferzone.zip) |
| **Verkehrsunfall Tannenbruck — A45 Quotenstreit, OWi, Fahrerlaubnis-Entzug, MPU** (`verkehrsunfall-quotenstreit-tannenbruck-a45`) | [Gesamt-PDF lesen](../testakten/verkehrsunfall-quotenstreit-tannenbruck-a45/gesamt-pdf/verkehrsunfall-quotenstreit-tannenbruck-a45_gesamt.pdf) | [`testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin Fachanwalt für Verkehrsrecht. Orientierung StVG StVO PflVG VVG-Bezüge. Verkehrsunfall Personenschaden Sachschaden Bußgeld Fahrerlaubnis OWi-Verfahren Verkehrsstrafrecht (§§ 315c 316 StGB). Schnittstellen zu Versicherungs- und Strafrecht.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-verkehrsrecht-orientierung` | Orientierung im Verkehrsrecht — FAO Voraussetzungen Normen typische Mandate Fristen Quellenprüfung. Verkehrsunfall mit Personen- und Sachschaden Schadensregulierung Versicherung Haftpflicht Kasko Bußgeld Fahrerlau… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 34 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Verkehrsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 67 OWiG Einspruch 2 Wochen, Bußgeldbescheid, Polizeiprotokoll, Anhörungsbogen), dokumentiert Router-Entscheidung mit Begründung. |
| `autonom-bezuege-fachanwalt` | Autonom Bezuege Fachanwalt im Plugin Fachanwalt Verkehrsrecht: prüft konkret Autonom, Bezuege, Fachanwalt. |
| `blitzer-messung-paragraf-3-stvo` | Blitzer Messung § 3 StVO: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `bussgeld-unfall-haftungsquote-vkr` | Bussgeld Unfall Haftungsquote VKR im Plugin Fachanwalt Verkehrsrecht: prüft konkret Bussgeld, Mandant hatte Verkehrsunfall und fragt, Spezialfall fiktive Abrechnung beim Totalschaden. |
| `dieselskandal-paragraf-826-bgb` | Dieselskandal § 826 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Verkehrsrecht: sortiert Bußgeldbescheid, Polizeiprotokoll, Anhörungsbogen, prüft Datum, Absender, Frist und Beweiswert (Messprotokoll, Eichschein); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `einstieg-routing` | Einstieg, Triage und Routing für Fachanwalt Verkehrsrecht: ordnet Rolle (Betroffener/Geschädigter, Behörde, Versicherer), markiert Frist (§ 67 OWiG Einspruch 2 Wochen), wählt Norm (StGB §§ 142/315c, 316, StVG, StVO) und Zuständigkeit (AG... |
| `erstgespraech-mandatsannahme-verkehr-autonom` | Erstgespraech Mandatsannahme Verkehr Autonom im Plugin Fachanwalt Verkehrsrecht: prüft konkret Strukturierter Erstgespraechsleitfaden für Verkehrsrecht, OWi- und Verk, Unfall mit autonomem Fahrzeug oder Frage zur Haftung bei, Mandant hat... |
| `fa-verkehrsrecht-fristen-risiko-mandant` | FA Verkehrsrecht Fristen Risiko Mandant im Plugin Fachanwalt Verkehrsrecht: prüft konkret Fristen- und Risikoampel im Plugin fachanwalt-verkehrsrecht, Mandantenkommunikation im Plugin fachanwalt-verkehrsrecht, Red-Team Qualitygate im Plu... |
| `fahrerlaubnis-entzug-paragraf-3-stvg` | Fahrerlaubnis Entzug § 3 StVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `fahrerlaubnis-kanzlei-personen` | Fahrerlaubnis Kanzlei Personen im Plugin Fachanwalt Verkehrsrecht: prüft konkret Fahrerlaubnis, Kanzlei, Personen. |
| `haftpflicht-paragraf-115-vvg` | Haftpflicht § 115 VVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `kaskoversicherung-paragraf-81-vvg-bgh-iv-zr-25-21` | Kaskoversicherung Paragraf 81 Vvg BGH Iv Zr 25 21: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `kfz-handel-paragraf-434-bgb` | kfz Handel § 434 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `mandat-triage-schriftsatzkern-substantiierung` | Mandat Triage Schriftsatzkern Substantiierung im Plugin Fachanwalt Verkehrsrecht: prüft konkret Neues Verkehrsrechtsmandat kommt rein und Anwalt muss, Substantiierter Schriftsatzkern für Klage Verkehrsunfall, Einspruch OWi-Bußgeldb, 315C. |
| `mpu-vorbereitung-orientierung` | MPU Vorbereitung Orientierung im Plugin Fachanwalt Verkehrsrecht: prüft konkret Mandant muss MPU ablegen und fragt wie er sich vorbereiten, Einstieg in den Skill-Verbund Verkehrsrecht, Mandant hat Verkehrsunfall und fordert Schadensersat... |
| `output-waehlen` | Output-Wahl für Fachanwalt Verkehrsrecht: stimmt Adressat (Betroffener/Geschädigter, Behörde, Versicherer), Frist (§ 67 OWiG Einspruch 2 Wochen) und Form auf den Zweck ab — typische Outputs: Einspruch OWi, Strafbefehlseinspruch, MPU-Bera... |
| `personenschaden-paragraf-249-bgb` | Personenschaden § 249 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `pflvg-quoten-sonderfall-stgb` | Pflvg Quoten Sonderfall Stgb im Plugin Fachanwalt Verkehrsrecht: prüft konkret Pflvg, Quoten, Stgb. |
| `punkte-fahrerlaubnis-paragraf-4-stvg-bverwg-3-c-25-19` | Punkte Fahrerlaubnis Paragraf 4 Stvg BVerwG 3 C 25 19: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Verkehrsrecht: prüft Normen (StGB §§ 142/315c, 316, StVG, StVO) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt AG (Bußgeld + Straf) und Quellenhygiene nach references/quellenhygi... |
| `sachschaden-quellenkarte` | Sachschaden Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `schmerzensgeld-paragraf-253-bgb` | Schmerzensgeld § 253 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `schnittstelle-fehlerkatalog` | Schnittstelle Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `stvg-verkehr-fristennotiz-vkr-blitzer` | Stvg Verkehr Fristennotiz VKR Blitzer im Plugin Fachanwalt Verkehrsrecht: prüft konkret Stvg, Verkehr, Spezialfall Blitzer- und Messverfahren. |
| `stvo-unfallregulierung-beweislast` | Stvo Unfallregulierung Beweislast im Plugin Fachanwalt Verkehrsrecht: prüft konkret Stvo, Unfallregulierung, Verkehrsrecht. |
| `tempo-messung-unfallregulierung-quoten` | Tempo Messung Unfallregulierung Quoten im Plugin Fachanwalt Verkehrsrecht: prüft konkret Mandant bestreitet korrekte Geschwindigkeitsmessung in, Mandant hat Unfall mit Mitverschulden und fragt welche, Versicherer hat Regulierung angebote... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Verkehrsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Bußgeldbescheid, Polizeiprotokoll, Anhörungsbogen), nennt pro Lücke Beweisthema, Beschaffungsweg (AG (Bußgeld + Straf)), Frist u... |
| `verk-fahrerlaubnisrecht-leitfaden-fahrtenbuch` | Verk Fahrerlaubnisrecht Leitfaden Fahrtenbuch im Plugin Fachanwalt Verkehrsrecht: prüft konkret Leitfaden Fahrerlaubnisrecht, Spezialfall Fahrtenbuchanordnung § 31a StVZO, Spezialfall Trunkenheits- und Drogenfahrt. |
| `verk-unfallregulierung` | Verk Unfallregulierung im Plugin Fachanwalt Verkehrsrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Unfallregulierung, Chronologie und Belegmatrix im Plugin. |
| `verkehrsstrafrecht-interessen-verkehrsunfall` | Verkehrsstrafrecht Interessen Verkehrsunfall im Plugin Fachanwalt Verkehrsrecht: prüft konkret Verkehrsstrafrecht, Verkehrsunfall, Vergleichsverhandlungs-Strategie für Verkehrsrecht Unfall-, OWi- und Verkehrsst. |
| `verkehrsunfall-paragraf-7-stvg` | Verkehrsunfall § 7 StVG: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `vkr-bussgeldverfahren-bussgeld-einspruch` | VKR Bussgeldverfahren Bussgeld Einspruch im Plugin Fachanwalt Verkehrsrecht: prüft konkret Bussgeldverfahren Grundzuege, Prüfungslinie für bussgeld einspruch pruefen, Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft. |
| `vkr-einfuehrung` | VKR Einfuehrung im Plugin Fachanwalt Verkehrsrecht im Fachanwalt Verkehrsrecht. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
