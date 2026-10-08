# Smoke Tests — vergaberecht-werkstatt

Prüfkette nach jedem Release. Alle automatisierbaren Abschnitte laufen mit
einem Befehl. Für den schnellen Entwicklungscheck werden nur die
releasebezogenen ZIP- und Git-Prüfungen ausgelassen:

```bash
python3 scripts/run-smoke-tests.py
python3 scripts/run-smoke-tests.py --quick
```

Der Runner validiert Nummerierung und Code-Fences, extrahiert die Bash-Blöcke
und führt sie mit Exit-Code-Prüfung aus. Ungeschlossene Blöcke, doppelte
Abschnitte und leere Prüfskripte brechen ab. Abschnitte ohne Bash-Block werden
als manuell gelistet; `<!-- smoke: release -->` kennzeichnet teure
Releaseprüfungen.

## 1. Validatoren

```bash
node scripts/validate-plugin-structure.mjs
python3 scripts/validate-yaml-frontmatter.py
python3 scripts/validate-skill-discovery.py
python3 scripts/validate-workflow-usability.py
python3 scripts/sync-references.py --check
python3 scripts/validate-rechtsstand-2026.py
python3 scripts/validate-legal-regressions.py
python3 scripts/run-eval.py
python3 scripts/sync-public-entrypoints.py --check
python3 scripts/validate-public-integration.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

Alle Validatoren, der Synchronitätscheck und die fallbezogenen Rubrics müssen mit Exit 0 enden. Der Discovery-Validator verhindert generische Import-Boilerplate, pluginübergreifend identische Skill-Texte, identische oder nahezu ununterscheidbare Beschreibungen und fehlende Einträge in Plugin-README oder Skill-Index. Die Rechtsstandsvalidatoren sperren überholte Rechtsschutzmuster, falsche Fristanknüpfungen, veraltetes BSIG, falsche Zuständigkeiten, erfundene Kostenformeln und nachweislich fehlzugeordnete Entscheidungen.

## 2. Marketplace-Manifest

```bash
python3 -c "import re, json; d=json.load(open('.claude-plugin/marketplace.json')); assert re.fullmatch(r'\d+\.\d+\.\d+', d['version']); print('marketplace ok')"
```

## 3. Skill-Anzahl pro Plugin

```bash
test "$(find vergabestelle-behoerden/skills -maxdepth 2 -name SKILL.md | wc -l | tr -d ' ')" = "122"
test "$(find bieter-unternehmen/skills -maxdepth 2 -name SKILL.md | wc -l | tr -d ' ')" = "113"
test "$(find konkurrenten-rechtsschutz/skills -maxdepth 2 -name SKILL.md | wc -l | tr -d ' ')" = "20"
```

## 4. Megaprompt und Miniprompt Groessen

```bash
python3 - <<'PY'
from pathlib import Path

work = sorted(Path('.').glob('vergaberecht-arbeitsprompt-*.md'))
quick = sorted(Path('.').glob('vergaberecht-kurzprompt-*.md'))
mini = [
    Path('unified-mini-prompts/vergabestelle-behoerden.md'),
    Path('unified-mini-prompts/bieter-unternehmen.md'),
    Path('unified-mini-prompts/konkurrenten-rechtsschutz.md'),
]
assert len(work) == len(quick) == len(mini) == 3
for path in work + quick:
    size = len(path.read_text(encoding='utf-8'))
    assert 5_000 <= size <= 100_000, (path, size)
for path in mini:
    size = len(path.read_bytes())
    assert 1_000 <= size <= 7_500, (path, size)
print('Promptgrößen plausibel; Unified-Mini-Prompts höchstens 7.500 UTF-8-Bytes')
PY
```

Dieser Block ist ein Sichtcheck für Root-Arbeits- und Root-Kurzprompts. Die harten 7.500 Zeichen gelten für die Unified-Mini-Prompts und werden in Abschnitt 14 mit `validate-mini-prompt-entrypoints.py` erzwungen. Root-Kurzprompts dürfen als Schnellstart-Arbeitsblätter länger sein, wenn sie Fallkarte, Skill-Routing, Fristen, Quellenstatus und Output-Weiche tragen.

## 5. Plugin-Description Marketplace-Limit

```bash
python3 -c "
import json
d=json.load(open('.claude-plugin/marketplace.json'))
for p in d['plugins']:
  assert len(p['description']) <= 300, p['name']
print('plugin descriptions ok')
"
```

## 6. Testakten

```bash
test -f testakten/README.md
test "$(find testakten -mindepth 1 -maxdepth 1 -type d ! -name megaprompts | wc -l | tr -d ' ')" -ge 7
for d in testakten/*/; do
  test "$(basename "$d")" = "megaprompts" && continue
  test -f "$d/README.md"
done
for role in vergabestelle-behoerden bieter-unternehmen konkurrenten-rechtsschutz; do
  rg -q "$role" testakten/README.md
done
python3 scripts/validate-testakten-falllogik.py
```

Mindestens eine zugeordnete Testakte pro Marktrolle und ein README. Der
Falllogik-Validator sichert lückenlose Aktenstücknummern, README-Verlinkung,
lebensnahe Dokumenttitel, vollständige §-134-Schreiben, rechtzeitige
Nachprüfungsanträge, die Reihenfolge von VK-Beschluss und sofortiger Beschwerde
sowie konsistente GAEB-Positionsbezüge.

## 7. Anker-Rechtsprechung verifizieren

```bash
for az in "C-81/98" "C-19/00" "X ZB 10/16" "XIII ZR 19/19" "1 BvR 1160/03" "C-124/17" "C-590/24" "C-810/24" "C-186/25"; do rg -q "$az" references/leitentscheidungen-anker.md; done
test -f references/bundeswehrbeschaffung-bwbbg-2026.md
test -f references/praxisrechtsprechung-vk-2016-2026.md
for az in "VK 2-34/22" "VK 2-35/24" "VK 2-39/25" "VK 3-42/23" "VK 2-5/21" "VK 1-31/22" "VK 2-24/22" "VK 2-82/23" "VK 2-93/24" "VK 2-57/21" "VK 1-65/22"; do rg -q "$az" references/praxisrechtsprechung-vk-2016-2026.md; done
for plugin in vergabestelle-behoerden bieter-unternehmen konkurrenten-rechtsschutz; do
  for ref in OUTPUT-FORMAT.md leitentscheidungen-anker.md methodik-vergaberecht.md praxisrechtsprechung-vk-2016-2026.md quellenhygiene.md veroeffentlichungswege.md zitierweise.md zuschlag-nicht-nur-preis.md; do test -f "$plugin/references/$ref"; done
  for az in "VK 2-34/22" "VK 2-35/24" "VK 2-39/25" "VK 2-93/24" "VK 1-65/22"; do rg -q "$az" "$plugin/references/praxisrechtsprechung-vk-2016-2026.md"; done
done
! rg -n "\.\./\.\./\.\./references/" vergabestelle-behoerden/skills bieter-unternehmen/skills konkurrenten-rechtsschutz/skills
rg -q "praxisrechtsprechung-vk-2016-2026" references/leitentscheidungen-anker.md README.md vergabestelle-behoerden/skills/23-stellungnahme-vergabekammer/SKILL.md bieter-unternehmen/skills/nachpruefungsantrag-powerdraft/SKILL.md konkurrenten-rechtsschutz/skills/nachpruefungsantrag-konkurrent-vk/SKILL.md
! rg -n "C-[0-9]+/[0-9]{3,}|Z[BR] [0-9]+/[0-9]{3,}|BvR [0-9]+/[0-9]{3,}|Verg [0-9]+/[0-9]{3,}" references/leitentscheidungen-anker.md
```

Der Block prüft mechanisch: keine fehlgeformten Jahresteile in Aktenzeichen (Jahr immer zweistellig), die Kernanker aus CLAUDE.md (Alcatel C-81/98, SIAC C-19/00, BGH X ZB 10/16, BGH XIII ZR 19/19, BVerfG 1 BvR 1160/03, Vossloh C-124/17) sind vorhanden, und alle drei Plugin-ZIPs bleiben mit ihren zentralen Arbeitsreferenzen autark. Formatreferenz:

- EuGH: C-NN/JJ oder T-NN/JJ (Beispiel: C-19/00, T-345/12)
- BGH: X ZB NN/JJ oder X ZR NN/JJ (Beispiel: X ZB 10/16)
- BVerfG: 1 BvR NNNN/JJ (Beispiel: 1 BvR 1160/03)
- VK Bund / Land: VK [Bund|Land] NNN/JJ (Beispiel: VK Bund 1-83/19)
- OLG-Vergabesenat: Verg NN/JJ (Beispiel: OLG Düsseldorf Verg 47/18)

Manuell bleibt die inhaltliche Live-Verifikation nach Quellenhygiene: Vor tragender Verwendung Gericht, Datum, Aktenzeichen und tragende Aussage gegen amtliche oder frei prüfbare Quellen abgleichen.

## 8. Schwellenwert-Aktualität

```bash
for f in CLAUDE.md vergaberecht-arbeitsprompt-*.md vergaberecht-kurzprompt-*.md testakten/megaprompts/*.md unified-mini-prompts/{vergabestelle-behoerden,bieter-unternehmen,konkurrenten-rechtsschutz}.md; do
  for vo in 2025/2150 2025/2151 2025/2152 2025/2487; do
    rg -q "$vo" "$f"
  done
done
```

CLAUDE.md, Arbeitsprompts, Kurzprompts, Unified Mini Prompts und generierte Megaprompts müssen alle vier Schwellenwertquellen nennen und zuordnen: 2025/2152 klassisch, 2025/2150 Sektoren, 2025/2151 Konzessionen und 2025/2487 Verteidigung/Sicherheit. Bei neuer VO Folge-Release und diesen Block auf die neuen VO-Nummern umstellen.

## 9. Bund-Länder-Reform und Wertgrenzen

```bash
test -f bieter-unternehmen/references/BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md
test -f vergabestelle-behoerden/references/BUND-LAENDER-VERGABEREFORM-WERTGRENZEN-2026.md
test -f bieter-unternehmen/assets/templates/bund-länder-wertgrenzen-livecheck.md
test -f vergabestelle-behoerden/assets/templates/bund-länder-wertgrenzen-livecheck.md
rg -n "Vergabebeschleunigungsgesetz|BGBl\\. 2026 I Nr\\. 137|Nordrhein-Westfalen|Hessen|Mecklenburg-Vorpommern|Brandenburg|Direktauftrag|Bund-Länder-Wertgrenzen" bieter-unternehmen/references vergabestelle-behoerden/references bieter-unternehmen/skills/schwellenwerte-2026-2027-livecheck vergabestelle-behoerden/skills/schwellenwerte-2026-2027-livecheck unified-mini-prompts testakten/megaprompts
```

Bundesreform und Landeswertgrenzen müssen in beiden Pluginrollen sichtbar sein. Bei jedem Unterschwellenfall: Bundesland, Auftraggebertyp, Leistungsart, Auftragswert, Stichtag, Verkündung, Fördermittel, Binnenmarktrelevanz und amtliche Quelle prüfen.

## 10. Datenformate und Uploadrouting

```bash
test -f bieter-unternehmen/skills/unterlagen-und-lv-datenformate-auslesen/SKILL.md
test -f bieter-unternehmen/skills/angebot-in-vorgegebenem-format-erstellen/SKILL.md
test -f vergabestelle-behoerden/skills/vergabeunterlagen-lv-datenformate-bereitstellen/SKILL.md
test -f vergabestelle-behoerden/skills/bekanntmachung-berichtigung-und-upload-routing/SKILL.md
test -f konkurrenten-rechtsschutz/skills/unterlagen-lv-formatangriff/SKILL.md
test -f vergabestelle-behoerden/assets/templates/systemuebergabe-entscheidungsdaten.md
test -f bieter-unternehmen/assets/templates/angebotsfreeze-systemuebergabe.md
test -f konkurrenten-rechtsschutz/assets/templates/beweiskette-systemexport.md
python3 scripts/validate-system-integration.py
rg -n "GAEB|XML|Excel|PDF|Upload-Routing|eForms|TED|DVAL|Legacy|SAP|ERP|MCP|Hash|Mapping" unified-mini-prompts testakten/megaprompts SKILLS.md skills-index konkurrenten-rechtsschutz
```

Neue Format-Workflows müssen in allen betroffenen Plugins, Unified Mini Prompts, Megaprompts und Skill-Index auftauchen.

## 11. Insolvenz und § 132 GWB

```bash
test -f bieter-unternehmen/skills/insolvenz-und-132-gwb-auftragnehmerwechsel/SKILL.md
test -f vergabestelle-behoerden/skills/insolvenz-und-132-gwb-auftragnehmerwechsel/SKILL.md
test -f bieter-unternehmen/references/INSOLVENZ-132-GWB.md
test -f vergabestelle-behoerden/references/INSOLVENZ-132-GWB.md
test -d testakten/05-insolvenz-auftragnehmerwechsel-132-gwb
test -f testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/05_nachpruefungsantrag_vk_dataportus.md
test -f testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/06_beiladungsantrag_erwerber_vk.md
test -f testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/07_stellungnahme_vergabestelle_vk.md
test -f testakten/05-insolvenz-auftragnehmerwechsel-132-gwb/08_fallvarianten_insolvenzplan_assetdeal.md
rg -n "Insolvenz|Auftragnehmerwechsel|§ 132|Advania|Asset Deal|Vergabekammer" bieter-unternehmen vergabestelle-behoerden unified-mini-prompts testakten/megaprompts SKILLS.md skills-index
```

Auftragnehmerinsolvenz muss in beiden Pluginrollen sichtbar sein: Vergabestelle steuert Fortführung, Interimsvergabe und Neuausschreibung; Bieter prüft Angriff, Erwerber-/Fortführungspaket und Fristen.

## 12. Konkurrentenrechtsschutz

```bash
test -f konkurrenten-rechtsschutz/skills/ruege-konkurrent-160-gwb/SKILL.md
test -f konkurrenten-rechtsschutz/skills/nachpruefungsantrag-konkurrent-vk/SKILL.md
test -f konkurrenten-rechtsschutz/skills/sofortige-beschwerde-olg-vergabesenat/SKILL.md
test -d testakten/06-konkurrentenrechtsschutz-rechenzentrum-musterkreis
test -f testakten/06-konkurrentenrechtsschutz-rechenzentrum-musterkreis/04_ruegeschreiben_konkurrent.md
test -f testakten/06-konkurrentenrechtsschutz-rechenzentrum-musterkreis/06_nachpruefungsantrag_vk.md
rg -n "Konkurrent|unterlegene Bieter|Zuschlagssperre|Akteneinsicht|De-facto|OLG|Kostenrisiko" konkurrenten-rechtsschutz unified-mini-prompts testakten/megaprompts SKILLS.md skills-index
```

Der Rechtsschutz aus Konkurrentensicht muss als eigene Marktrolle sichtbar sein: Rüge, Nichtabhilfe, Nachprüfungsantrag, Zuschlagssperre, Akteneinsicht, Wertungs-/Eignungsangriff, OLG-Beschwerde und Kostenrisiko.

## 13. Lokale Suffixartefakte

```bash
test -z "$(find . \( -path './.git' -o -path './dist' \) -prune -o -type f -name '* [2-9]*' -print)"
```

Keine Finder-/Sync-Duplikate wie `SKILL 2.md`, `README 2.md`, Schutzplatzhalter-Dateien oder `*_gesamt 2.pdf` im Release-Baum lassen; sie würden sonst in Plugin-, Referenz- oder Testakten-ZIPs landen.

## 14. Prompt-Routing und autarker Fallback

```bash
python3 scripts/generate-megaprompt.py --check
python3 scripts/generate-unified-mini-prompts.py --check
python3 scripts/validate-prompt-routing-autarky.py
python3 scripts/validate-mini-prompt-entrypoints.py
```

Mega-, Mini-, Kurz- und Arbeitsprompts müssen im Dual-Mode funktionieren: Wenn Claude-Skills verfügbar sind, routen sie über exakte Skill-Slugs; ohne installierte Skills bleiben sie autark verwendbar. Verboten sind notwendige Repo-Referenzpfade, SKILL.md-Abhängigkeiten und unbekannte Skill-Slugs.
Zusätzlich prüft der Validator die zentralen Router-Tabellen: Jeder dort genannte Ziel-Skill muss im Plugin existieren, in der Prioritätsliste stehen und in jedem Rollenprompt sichtbar sein. Damit fallen verkümmernde Spezialskills wie Dashboard-, Legacy-, Bietergemeinschafts-, VK- oder Kostenmodule schon vor dem Release auf.
Der Mini-Prompt-Validator sichert die rechtsprechungsfesten Einstiegskerne je Marktrolle: unter 7.500 Zeichen, mit Sofortworkflow, Output-Weiche, Norm-/Rechtsprechungskern, ECLI-Ankern und Pflichtarbeitsbegriffen statt generischer Schnellstartsprache.

## 15. C-268/25 Bietergemeinschaft

```bash
rg -n "C-268/25|Schlussanträge GA Kokott|ECLI:EU:C:2026:382" vergaberecht-arbeitsprompt-*.md vergaberecht-kurzprompt-*.md unified-mini-prompts/*.md testakten/megaprompts/*.md references/leitentscheidungen-anker.md README.md CODEX.md
! rg -n "EuGH, Urteil.*C-268/25|C-268/25.*EuGH, Urteil|EuGH Urteil.*C-268/25|C-268/25.*EuGH Urteil" vergaberecht-arbeitsprompt-*.md vergaberecht-kurzprompt-*.md unified-mini-prompts/*.md testakten/megaprompts/*.md references/leitentscheidungen-anker.md README.md CODEX.md
```

C-268/25 darf nur als Schlussanträge der Generalanwältin behandelt werden, nicht als EuGH-Urteil. Sichtbar sein müssen Einzelfallprüfung, Zurechnung, Sorgfalt/Kenntnis/Einfluss, Austauschbarkeit und nicht wesentliche Angebotsänderung.

## 16. Git-Status

<!-- smoke: release -->

```bash
test -z "$(git status --porcelain)"
test -n "$(git tag --points-at HEAD)"
```

Working tree sauber. Letzter Commit identisch mit Tag.

## 17. Testakten-Datenwusel ohne Markdown

<!-- smoke: release -->

```bash
python3 scripts/validate-testakten-echtformate.py >/dev/null
python3 scripts/build-testakten-release-zips.py dist >/dev/null
python3 scripts/validate-testakten-release-zips.py dist >/dev/null
python3 -c "
import zipfile, glob, sys
erlaubt = {'.docx', '.xlsx', '.pdf'}
for z in glob.glob('dist/testakte-*.zip'):
    ns = zipfile.ZipFile(z).namelist()
    assert ns and all('/' not in n and '\\\\' not in n for n in ns), (z, 'Unterordner gefunden')
    assert ns[0] == 'README.txt', (z, 'Pflichtwarnhinweis fehlt am Anfang')
    assert '00_Gesamtakte.pdf' not in ns, (z, 'Gesamt-PDF nur separat ausliefern')
    dateitypen = {__import__('pathlib').Path(n).suffix.lower() for n in ns if n != 'README.txt'}
    assert dateitypen <= erlaubt, (z, 'Formatfehler')
    if z.endswith('-einzelpdfs.zip'):
        assert dateitypen == {'.pdf'} and '00_Gesamtakte.pdf' not in ns, (z, 'Einzel-PDF-Auswahl fehlerhaft')
    else:
        assert erlaubt <= dateitypen, (z, 'DOCX/XLSX/PDF nicht vollständig')
    assert len({n.casefold() for n in ns}) == len(ns), (z, 'Namenskollision')
print('testakten-zips flach, kollisionsfrei und ausschliesslich aus DOCX/XLSX/PDF')
"
```

Release-Grundregel: Jedes Testakten-ZIP liegt ohne Unterordner vor und enthält Arbeitsdateien als DOCX, XLSX oder PDF sowie README.txt mit Warnhinweis. Einzel-PDF-ZIPs enthalten nur die einzelnen PDFs und README.txt. Technische Rohformate und interne Bewertungsraster verbleiben im Quellenbestand. Details in CLAUDE.md und `testakten/README.md`.

## 18. Übersichtslinks und Schnellzugriff

```bash
python3 scripts/validate-doc-links.py
python3 scripts/validate-navigation.py
test -f vergabestelle-behoerden/assets/templates/fallkarte-output-weiche.md
test -f bieter-unternehmen/assets/templates/fallkarte-output-weiche.md
test -f konkurrenten-rechtsschutz/assets/templates/fallkarte-output-weiche.md
test -f vergabestelle-behoerden/assets/templates/ordnerfall-startprotokoll.md
test -f bieter-unternehmen/assets/templates/ordnerfall-startprotokoll.md
test -f konkurrenten-rechtsschutz/assets/templates/ordnerfall-startprotokoll.md
rg -q "fallkarte-output-weiche" vergabestelle-behoerden/assets/templates/startbildschirm-applet-dashboard.md bieter-unternehmen/assets/templates/startbildschirm-applet-dashboard.md konkurrenten-rechtsschutz/assets/templates/startbildschirm-konkurrenten-dashboard.md vergabestelle-behoerden/skills/vergabe-os-master-orchestrator/SKILL.md bieter-unternehmen/skills/vergabe-os-master-orchestrator/SKILL.md konkurrenten-rechtsschutz/skills/konkurrenzrechtsschutz-orchestrator/SKILL.md
rg -q "ordnerfall-startprotokoll" vergabestelle-behoerden/README.md bieter-unternehmen/README.md konkurrenten-rechtsschutz/README.md vergabestelle-behoerden/skills/vergabe-os-master-orchestrator/SKILL.md bieter-unternehmen/skills/vergabe-os-master-orchestrator/SKILL.md konkurrenten-rechtsschutz/skills/konkurrenzrechtsschutz-orchestrator/SKILL.md vergabestelle-behoerden/skills/workflow-kaltstart-und-routing/SKILL.md bieter-unternehmen/skills/workflow-kaltstart-und-routing/SKILL.md konkurrenten-rechtsschutz/skills/startbildschirm-konkurrentenangriff/SKILL.md
rg -q "Ohne Skillauswahl starten|Arbeitsname" SKILLS.md skills-index/vergabestelle-behoerden.md skills-index/bieter-unternehmen.md skills-index/konkurrenten-rechtsschutz.md
for f in vergabestelle-behoerden/assets/templates/fallkarte-output-weiche.md bieter-unternehmen/assets/templates/fallkarte-output-weiche.md konkurrenten-rechtsschutz/assets/templates/fallkarte-output-weiche.md; do
  rg -q "Falltyp" "$f"
  rg -q "Normenanker" "$f"
  rg -q "Quellenstatus" "$f"
  rg -q "Outputwunsch" "$f"
done
for f in vergabestelle-behoerden/assets/templates/ordnerfall-startprotokoll.md bieter-unternehmen/assets/templates/ordnerfall-startprotokoll.md konkurrenten-rechtsschutz/assets/templates/ordnerfall-startprotokoll.md; do
  rg -q "Fallkarte" "$f"
  rg -q "Fristenampel" "$f"
  rg -q "Quelleninventar" "$f"
  rg -q "Output-Weiche" "$f"
done
```

Root-README, SKILLS.md, Skill-Index, Plugin-READMEs, Testakten-README und Unified-Mini-Prompt-README müssen lokal konsistente Links haben. Externe Release-URLs werden bewusst nicht aufgerufen, damit der Smoke-Test schnell bleibt und nicht durch Netzwerklatenz einfriert.
Die Fallkarten-Outputweiche und das Ordnerfall-Startprotokoll müssen in allen drei Pluginrollen vorhanden und aus den Start-/Orchestratorvorlagen erreichbar sein. Skill-Detailseiten müssen neben dem technischen Slug auch einen sprechenden Arbeitsnamen aus der H1 zeigen, damit Zuordnung und Routing ohne Umbenennung stabil bleiben.

## 19. GitHub Release

<!-- smoke: manual -->

Im GitHub-Repo unter Releases muss aktueller Tag vorhanden sein, mit angehängten Plugin-ZIPs und marketplace.json.
Der Release-Workflow muss vor dem Upload `scripts/validate-release-zips.py` ausführen. Dieser Validator prüft neben Manifest, Größe und ZIP-Hygiene auch die plugininterne Referenz-Autarkie: gemeinsame Kernreferenzen müssen im ZIP liegen, alte Repo-Root-Referenzpfade sind verboten und jeder Skill-Verweis auf `references/*.md` muss im ZIP auflösbar sein.
Der Release-Workflow muss nach dem Upload `scripts/validate-release-assets.py` ausführen. Erwartet werden alle Plugin-, Skill-, Prompt- und Testakten-Assets plus `marketplace.json` und `checksums-sha256.txt`; Name, Upload-Status, Dateigröße und SHA-256-Digest müssen zur lokal gebauten `dist/`-Fassung passen. Das Prüfsummenmanifest selbst muss jedes andere Release-Asset genau einmal mit korrektem SHA-256 aufführen.
