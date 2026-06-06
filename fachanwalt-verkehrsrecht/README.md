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

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `autonom-bezuege-fachanwalt` | Autonom Bezuege Fachanwalt im Plugin Fachanwalt Verkehrsrecht: prüft konkret Autonom, Bezuege, Fachanwalt. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `bussgeld-unfall-haftungsquote-vkr` | Bussgeld Unfall Haftungsquote VKR im Plugin Fachanwalt Verkehrsrecht: prüft konkret Bussgeld, Mandant hatte Verkehrsunfall und fragt, Spezialfall fiktive Abrechnung beim Totalschaden. Liefert priorisierten Output mit Norm-Pinpoints, Risi... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `erstgespraech-mandatsannahme-verkehr-autonom` | Erstgespraech Mandatsannahme Verkehr Autonom im Plugin Fachanwalt Verkehrsrecht: prüft konkret Strukturierter Erstgespraechsleitfaden für Verkehrsrecht, OWi- und Verk, Unfall mit autonomem Fahrzeug oder Frage zur Haftung bei, Mandant hat... |
| `fa-verkehrsrecht-fristen-risiko-mandant` | FA Verkehrsrecht Fristen Risiko Mandant im Plugin Fachanwalt Verkehrsrecht: prüft konkret Fristen- und Risikoampel im Plugin fachanwalt-verkehrsrecht, Mandantenkommunikation im Plugin fachanwalt-verkehrsrecht, Red-Team Qualitygate im Plu... |
| `fahrerlaubnis-kanzlei-personen` | Fahrerlaubnis Kanzlei Personen im Plugin Fachanwalt Verkehrsrecht: prüft konkret Fahrerlaubnis, Kanzlei, Personen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `mandat-triage-schriftsatzkern-substantiierung` | Mandat Triage Schriftsatzkern Substantiierung im Plugin Fachanwalt Verkehrsrecht: prüft konkret Neues Verkehrsrechtsmandat kommt rein und Anwalt muss, Substantiierter Schriftsatzkern für Klage Verkehrsunfall, Einspruch OWi-Bußgeldb, 315C... |
| `mpu-vorbereitung-orientierung` | MPU Vorbereitung Orientierung im Plugin Fachanwalt Verkehrsrecht: prüft konkret Mandant muss MPU ablegen und fragt wie er sich vorbereiten, Einstieg in den Skill-Verbund Verkehrsrecht, Mandant hat Verkehrsunfall und fordert Schadensersat... |
| `output-waehlen` | Output wählen im Plugin Fachanwalt Verkehrsrecht: Diese Output-Weiche für Fachanwalt Verkehrsrecht entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `pflvg-quoten-sonderfall-stgb` | Pflvg Quoten Sonderfall Stgb im Plugin Fachanwalt Verkehrsrecht: prüft konkret Pflvg, Quoten, Stgb. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `sachschaden-quellenkarte` | Sachschaden Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `schnittstelle-fehlerkatalog` | Schnittstelle Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `stvg-verkehr-fristennotiz-vkr-blitzer` | Stvg Verkehr Fristennotiz VKR Blitzer im Plugin Fachanwalt Verkehrsrecht: prüft konkret Stvg, Verkehr, Spezialfall Blitzer- und Messverfahren. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `stvo-unfallregulierung-beweislast` | Stvo Unfallregulierung Beweislast im Plugin Fachanwalt Verkehrsrecht: prüft konkret Stvo, Unfallregulierung, Verkehrsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `tempo-messung-unfallregulierung-quoten` | Tempo Messung Unfallregulierung Quoten im Plugin Fachanwalt Verkehrsrecht: prüft konkret Mandant bestreitet korrekte Geschwindigkeitsmessung in, Mandant hat Unfall mit Mitverschulden und fragt welche, Versicherer hat Regulierung angebote... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verk-fahrerlaubnisrecht-leitfaden-fahrtenbuch` | Verk Fahrerlaubnisrecht Leitfaden Fahrtenbuch im Plugin Fachanwalt Verkehrsrecht: prüft konkret Leitfaden Fahrerlaubnisrecht, Spezialfall Fahrtenbuchanordnung § 31a StVZO, Spezialfall Trunkenheits- und Drogenfahrt. Liefert priorisierten... |
| `verk-unfallregulierung` | Verk Unfallregulierung im Plugin Fachanwalt Verkehrsrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Unfallregulierung, Chronologie und Belegmatrix im Plugin. Liefert priorisierten Output mit Norm-Pinpoints, Ri... |
| `verkehrsstrafrecht-interessen-verkehrsunfall` | Verkehrsstrafrecht Interessen Verkehrsunfall im Plugin Fachanwalt Verkehrsrecht: prüft konkret Verkehrsstrafrecht, Verkehrsunfall, Vergleichsverhandlungs-Strategie für Verkehrsrecht (Unfall-, OWi- und Verkehrsst. Liefert priorisierten Ou... |
| `vkr-bussgeldverfahren-bussgeld-einspruch` | VKR Bussgeldverfahren Bussgeld Einspruch im Plugin Fachanwalt Verkehrsrecht: prüft konkret Bussgeldverfahren Grundzuege, Prüfungslinie für bussgeld einspruch pruefen, Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft. Liefert pri... |
| `vkr-einfuehrung` | VKR Einfuehrung im Plugin Fachanwalt Verkehrsrecht im Fachanwalt Verkehrsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und näc... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
