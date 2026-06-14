# Testbericht — Klotzkette German Legal Skills

**Erstellt:** 2026-06-14
**Arbeitsstand:** v328.0.0 / Fix nach v327: Top-Level `version` in `.claude-plugin/marketplace.json` jetzt synchron mit Plugin-Versionen. SKILLS.md und skills-index neu generiert, zeigen jetzt korrekt v328. 213 Plugins, 25639 Skills, 206 Testakten.
**Plugins gesamt:** 213
**Skills gesamt:** 25639
**Testakten gesamt:** 206 (inkl. Hilfsmaterial-Verzeichnisse `formatvorlagen-paradebeispiele` und `megaprompts`)

## Kurzbefund

Dritte Salvage-Schleife: Die Inventare des alten Haupt-Worktrees wurden gegen den frischen main abgeglichen. 4.946 Skill-Salvage-Aktionen sind nachvollzogen; 203 zusätzlich gerettete Non-Skill-Dateien sind vorhanden. Nicht erneut eingeführt wurden nur geschützte Arbeitszeugnis-Zusätze und alte generische `allgemein`-Kollisionen. Vier fachliche Konfliktkandidaten wurden geprüft; der Mittelstands-Beirat und die Behördenmail für Deutsch als Zweitsprache wurden gezielt nachgeschärft.

Das Repository ist nach dem v311-Pflege-Release stabil und uploadfähig. Der seit v306 schwelende Workflow-Failure (Hilfsmaterial-Ordner in `testakten/` ohne `gesamt-pdf`) ist behoben. Der `verhaeltnismaessigkeitspruefer` ist auf 85 Skills gewachsen; in zwei thematischen Wellen kamen je 5 Skills hinzu (Art. 3 GG / AGG und Drittwirkung der Grundrechte). Welle 2 und Welle 3 haben gemeinsam die Umlaut- und Komposita-Stamm-Hygiene über das gesamte Repo gezogen.

Alle Übersichten, Sofort-Download-Sektionen und Release-Assets sind synchron: Plugin-Manifests, Marketplace, Top-Level-README, Asset-Index, SKILLS.md und der pro-Plugin-Detailindex stehen auf demselben Stand.

## Kennzahlen

| Kennzahl | Wert |
|---|---:|
| Plugin-Manifests | 213 |
| Skill-Dateien `SKILL.md` | 25639 |
| Testakten-Verzeichnisse | 204 |
| Testakten mit Gesamt-PDF nach Validator | 204 |
| Skills im `verhaeltnismaessigkeitspruefer` | 85 |
| seit v305 enthaltene Pull Requests | 8 |

## Validatoren

| Check | Ergebnis |
|---|---|
| `python3 scripts/validate-yaml-frontmatter.py` | OK — 0 Fehler, 0 Warnungen |
| `node scripts/validate-plugin-structure.mjs` | OK |
| `python3 scripts/validate-testakten-gesamt-pdf.py` | OK |
| Eval-Harness Welle 2 und Welle 3 | 204/204 All-Pass |
| Repo-weiter Grep nach Anbieternamen im EU-Gateway-Plugin | 0 Treffer |
| JSON-Validität der EU-Gateway-Config | OK |

## Veränderungen v305 → v310

### Inhaltliche Erweiterungen im `verhaeltnismaessigkeitspruefer`

**Wellenkomplex Art. 3 GG und AGG (5 neue Skills):**
- `art-3-gg-allgemeiner-gleichheitssatz` — Willkuerformel, Neue Formel, gleitender Massstab
- `art-3-abs-2-3-besondere-gleichheitssaetze` — Geschlecht, Behinderung, Diskriminierungsverbote
- `agg-systematik-und-verhaeltnismaessigkeit` — AGG-Aufbau, Paragraph 8/10/20 AGG
- `verhaeltnismaessigkeit-mittelbare-diskriminierung` — Paragraph 3 II AGG, EuGH-Linie Bilka
- `gleichbehandlung-arbeitsrecht-praxischeck` — Paragraph 7/15/22 AGG, BAG-Linien

**Wellenkomplex Drittwirkung der Grundrechte (5 neue Skills):**
- `drittwirkung-grundrechte-mittelbar` — Lueth-Linie, Generalklauseln als Einbruchstellen
- `schutzpflichtdimension-grundrechte` — Triage-Beschluss BVerfG 16.12.2021, Art. 3 III 2 GG
- `drittwirkung-stadionverbot-bundesverfassungsgericht` — BVerfGE 148, 267, eingriffsaehnliche Drittwirkung
- `drittwirkung-unionsgrundrechte-charta` — EuGH Mangold/Egenberger/Bauer, Art. 52 I GRCh
- `drittwirkung-praxischeck-zivilrecht` — Paragraph 138, 242, 826, 307, 315 BGB als Einbruchstellen

### Welle 2 und Welle 3 — Hygiene-Sweeps

- **Welle 2:** Umlaut-Hygiene-Sweep über 6498 Dateien mit 204/204 All-Pass im Eval-Harness. Quellenhygiene-Anschluss in den vom Sweep berührten Skills.
- **Welle 3:** Komposita-Stamm-Sweep mit `scripts/sweep-umlaut-welle-3.py`. Erfasst ASCII-Schreibungen am Wortanfang (Pattern `\bStamm`, ohne `\b` am Ende) und damit zusammengesetzte Wörter, die Welle 2 nicht treffen konnte. Zusätzlich Behandlung des `description:`-Feldes in YAML-Frontmatter; das `name:`-Feld bleibt geschützt. 5253 Dateien angefasst, rund 31,7 Millionen Zeichen geändert.

### `arbeitszeugnispruefer-skill` — Eval-Harness-Drop-In

Bundle mit eigenem Eval-Harness-Drop-In nach Harvey-LAB-Vorbild.

### `0_setup-cowork3p-eu-gateway` — vollständige Neutralisierung

Anbieterneutrale Setup-Anleitung für Cowork-3P über einen EU-Gateway-Anbieter. Ordner-, Datei- und Inhaltsbenennung ohne konkreten Anbieternamen. Anbieterneutrale Voraussetzungen (AVV nach Art. 28 DSGVO, Zusatzvereinbarung nach § 43e Abs. 3 BRAO i. V. m. § 203 Abs. 4 StGB, EU-Hosting) und Hinweisblock zur Anbieterauswahl.

## Konsolidierungslogik

Die Pflege folgt konservativen Regeln:

- Einstieg, Kaltstart, Routing, Dokumentenintake, Rechtsquellencheck, Outputwahl und Quality-Gates bleiben sichtbare Einstiegspunkte.
- Skills mit Zusatzdateien, Assets, References oder Toolmaterial bleiben eigenständig.
- Steuerrechtliche DBA-Skills bleiben als Einzelskills erhalten, weil die Einzelabkommen selbst Arbeitsgegenstand sind.
- Sprechende Skillnamen haben Vorrang vor technischen oder generischen Kürzeln.
- Zusammengeführte Skills müssen freistehend bleiben und dürfen keine Artefakte wie „frühere Beschreibung", „Dieser Skill bündelt" oder unspezifische Sammelüberschriften behalten.

## Offene bewusste Ausnahme

Einige große Fach- und Werkstattplugins bleiben oberhalb einer niedrigen Zielmarke, wenn die sichtbare Auswahl einzelner Fallgruppen praktisch wichtiger ist als weitere Verdichtung. Das gilt insbesondere für stark differenzierte Steuer-, Arbeitszeugnis-, Liquiditäts-, Selbstvertreter- und Fachanwaltsworkflows.

## Offen für Welle 4

- 83 false-positive Sanity-Check-Abbrüche aus Welle 3 manuell adressieren
- Restliche Stamm-Familien ergänzen (`Bruecke*`, `Tatbestaenden`, `Erklaert`, `Rechtfertigungs*` etc.)
- 213 Skills mit verbleibendem „Az verifizieren"-Marker (unverändert seit Welle 2)

## Residualrisiko

Die Validierung prüft Struktur, Frontmatter, Gesamt-PDF-Verfügbarkeit und grundlegende Markdown-/Git-Sauberkeit. Sie ersetzt keine vollständige fachliche Rechtsprüfung jedes einzelnen Skill-Abschnitts. Für Rechtsprechung, Normstand und Literaturhinweise bleibt die Regel des Repos maßgeblich: nur mit überprüfbarer Quelle, Datum, Aktenzeichen und frei zugänglicher Fundstelle ausgeben, soweit keine Nutzerquelle ausdrücklich bereitgestellt wird.

Die Rechtsvergleichs-Skills enthalten in jedem Land einen Live-Recherche-Disclaimer mit Original-Datenbanken.
