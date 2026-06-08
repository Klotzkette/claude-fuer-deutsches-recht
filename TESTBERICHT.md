# Testbericht — Klotzkette German Legal Skills

**Erstellt:** 2026-06-05
**Arbeitsstand:** v239.0.0 / LausitzStorage-Testakte um zehn Finanzierungs- und Gesellschafterstreit-Originale erweitert (Sicherheitenpoolvertrag, Kontoverpfändung Commerzbank, Globalzession LEAG-Pacht, Anteilsverpfändung UR 388⁄2025, Antrag Abberufung Bauernfeind, Lindenthal-Notarprotest, Einberufung 24.06.2026, EPC-Anzahlung Sungrow, Anlage 4 Stadtwerke, Forensik Cap-Table V2). 33 → 43 Aktenstücke; Gesamt-PDF 188 KB. 212 Plugins, 18.536 Skills, 203 Testakten.
**Plugins gesamt:** 212
**Skills gesamt:** 18536
**Testakten gesamt:** 203

## Kurzbefund

Das Repository ist nach der formalen Glattziehung release- und uploadfähig. Der neue Stand korrigiert insbesondere die manuell gepflegte alphabetische Root-README-Liste und den Asset-Index: `status-navigator-step-plan` und `verhaeltnismaessigkeitspruefer` sind dort wieder sichtbar; der Asset-Index zählt 212 Plugin-ZIPs und 203 Testakten-ZIPs mit den tatsächlich vom Release-Workflow erzeugten `testakte-<slug>.zip`-Links.

Die parallel eingegangenen Verbesserungen aus dem vorherigen Release bleiben erhalten. Der neue Schwerpunkt liegt darauf, dass alle sichtbaren Übersichten, Sofort-Download-Sektionen und Release-Assets denselben Stand abbilden.

## Kennzahlen

| Kennzahl | Wert |
|---|---:|
| Plugin-Manifests | 212 |
| Skill-Dateien `SKILL.md` | 18536 |
| Testakten-Verzeichnisse | 203 |
| Testakten mit Gesamt-PDF nach Validator | 203 |
| Skillnamen-/Artefakt-Scan | 0 alte Autogen-Muster, 0 `Nutze dies`, 0 Einwort-/Zahlenslugs, 0 `Kompendium`-/`Sammelskill`-Namen, 0 `bündelt`-/`Arbeitsmodul`-Artefakte, 0 `Nutze diesen Skill`-/`Dieses Fachmodul greift ...`-Starter in Skillanfängen |
| Bewusste Ausnahmen | Einige große Fach- und Werkstattplugins bleiben umfangreicher, wo Einzelzugriff praktisch wichtiger ist als weitere Verdichtung. |

## Validatoren

| Check | Ergebnis |
|---|---|
| `python3 scripts/validate-yaml-frontmatter.py` | OK — 0 Fehler, 0 Warnungen |
| `node scripts/validate-plugin-structure.mjs` | OK |
| `python3 scripts/validate-testakten-gesamt-pdf.py` | OK — 203 Testakten |
| `python3 scripts/validate-release-zips.py dist .claude-plugin/marketplace.json` | OK — lokale ZIP-Simulation für alle 212 Marketplace-Plugins |
| `git diff --check` | OK |

## Konsolidierungslogik

Die Pflege folgt konservativen Regeln:

- Einstieg, Kaltstart, Routing, Dokumentenintake, Rechtsquellencheck, Outputwahl und Quality-Gates bleiben soweit möglich als sichtbare Einstiegspunkte erhalten.
- Skills mit Zusatzdateien, Assets, References oder Toolmaterial bleiben eigenständig.
- Steuerrechtliche DBA-Skills bleiben als Einzelskills erhalten, weil hier die Einzelabkommen selbst der Arbeitsgegenstand sind.
- Sprechende Skillnamen haben Vorrang vor technischen oder generischen Kürzeln.
- Zusammengeführte Skills müssen freistehend bleiben und dürfen keine Artefakte wie "frühere Beschreibung", "Dieser Skill bündelt" oder unspezifische Sammelüberschriften behalten.

Damit sinkt die Bedienlast für Nutzerinnen und Nutzer, ohne dass fachliches Material aus den alten Skills aus dem Repository verschwindet.

## Nachgezogene Meta-Pflege

- Root-README auf den aktuellen Stand gebracht: 212 Plugins, 18536 Skills, 203 Testakten. Fehlendes Plugin `fahrgastrechte` bleibt in der alphabetischen Plugin-Tabelle geführt.
- Testakten-README auf den aktuellen Stand und 203 Testakten geprüft.
- In 52 Plugins wurden generische Kurz-Präfixe aus Skill-Slugs entfernt (z. B. `dsv-`, `kom-`, `btm-`, `ifg-`, `owi-`, `hoai-`, `bho-`, `stb-`, `legw-`, `solo-`, `pe-`, `vc-`, `tk-`, `vbr-`, `vdg-`, `db-`, `kv-`, `lease-`, `ins-`, `verl-`, `inv-`, `iv-`, `nkr-`, `inso-`, `ips-`, `vaf-`, `spez-`, `elsj-`, `ifap-`, `jveg-`, `liqui-`, `zvg-`, `zv-` und je nach Plugin weitere). Semantische Präfixe (`lph-` HOAI-Leistungsphasen, `bess-` Battery Storage, `plan-` Insolvenzplan) bleiben erhalten.
- `SKILLS.md` und `skills-index/` wurden mit den Generatoren neu aufgebaut.
- Veraltete Angaben aus der alten 52-Plugin-/361-Skill-Phase wurden aus diesem Testbericht entfernt.
- Nach v211 wurden 2906 `SKILL.md`-Dateien zusätzlich sprachlich nachpoliert, damit verdichtete Skills nicht mehr wie Generator- oder Konsolidierungsartefakte starten.

## Offene bewusste Ausnahme

Einzelne große Fach- und Werkstattplugins bleiben oberhalb einer niedrigen Zielmarke, wenn die sichtbare Auswahl einzelner Fallgruppen praktisch wichtiger ist als weitere Verdichtung. Das gilt insbesondere für stark differenzierte Steuer-, Arbeitszeugnis-, Liquiditäts-, Selbstvertreter- und Fachanwaltsworkflows.

## Residualrisiko

Die Validierung prüft Struktur, Frontmatter, Gesamt-PDF-Verfügbarkeit und grundlegende Markdown-/Git-Sauberkeit. Sie ersetzt keine vollständige fachliche Rechtsprüfung jedes einzelnen Skill-Abschnitts. Für Rechtsprechung, Normstand und Literaturhinweise bleibt die Regel des Repos maßgeblich: nur mit überprüfbarer Quelle, Datum, Aktenzeichen und frei zugänglicher Fundstelle ausgeben, soweit nicht eine Nutzerquelle ausdrücklich bereitgestellt wird.
