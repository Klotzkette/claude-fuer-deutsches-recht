# Intensiver Audit-Report: Repo `claude-fuer-deutsches-recht`

Stand: 2026-06-08
Verfasser: Claude
Branch: keine — Findings nur dokumentiert, nicht implementiert.
Zweck: Auf Toms Aufforderung "such intensiv nach Fehlern, mach Aufstellung mit Lösungsvorschlägen, noch nicht hochladen".

Repo-Größe gerade: **212 Plugins**, **18 549 SKILL.md**, **203 Testakten**.

---

## Befunde nach Schwere

### 🔴 Schwer — beeinträchtigt Skill-Funktion

#### S1. 479 Skills mit identischer Description in 14 Gruppen (Skelett-Klone)

Die sechs Skelett-Skills (`einstieg-routing`, `dokumente-intake`, `unterlagen-luecken`, `output-waehlen`, `quellen-livecheck`, `anschluss-routing`) haben über alle ~100 Plugins hinweg **dieselbe `description`-Zeile**. Das ist genau die Anti-Pattern, die Tom mehrfach kritisiert hatte:

| Vorkommen | Description-Anfang |
|---|---|
| 100× | "Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel…" |
| 96× | "Dokumentenintake: sortiert Dokumente, erkennt Lücken…" |
| 94× | "Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken…" |
| 86× | "Rechtsquellen-Livecheck: Quellenprüfung; Normenstand…" |
| 68× | "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel…" |
| 35× | weitere generische |

**Konsequenz für Claude-Code:** Mehrere Skills mit identischer Description konkurrieren beim Trigger-Matching. Claude lädt den falschen oder zufälligen — der Plugin-Kontext (z. B. Mietrecht vs. Patentrecht) wird ignoriert.

**Ursache:** Mein PR #227 hatte den Body individualisiert, aber das `description`-Feld nicht angefasst.

**Lösungsvorschlag:**
- Für jeden der 479 betroffenen Skills die `description` aus dem Plugin-Fachprofile generieren (analog meinem Fachprofile-Dictionary in PR #227). Beispiel:
  - `mietrecht/einstieg-routing` → `description: "Mietrechtlicher Sachverhalt-Einstieg: ordnet Wohnraum / Gewerbe / WEG, sortiert nach Mängel / Kündigung / Nebenkosten, identifiziert Frist § 573c BGB Ordentliche Kündigung."`
  - `patentrecherche/einstieg-routing` → `description: "Patentrechtlicher Einstieg: ordnet FTO / Validity / Family-Watch, sortiert nach DPMA / EPA / USPTO, identifiziert Prioritätstag § 3 PatG."`
- Geschätzter Aufwand: 30 min (Skript mit gleicher Fachprofile-DB).

---

#### S2. Broken Cross-References in Fachlandkarte-Sektionen

Die Skelett-Skills enthalten "Fachlandkarte"-Tabellen, die andere Skills im Plugin auflisten. Stichprobe `kanzlei-builder-hub/dokumente-intake`:

```
- `allgemein-anschluss-router-workflow-chronologie` — Allgemein Chronologie Fristen ← EXISTIERT NICHT
- `community-leistungsmatrix-fristennotiz-automatischer` — … ← EXISTIERT NICHT
- `kanzlei-builder-hub-kaltstart-interview` — … ← EXISTIERT NICHT
- `kanzleiumgebung-khub-sonderfall-livecheck-interessen` — … ← EXISTIERT NICHT
- `khub-mandantenkonferenz-paralegal-rollen-rentier-rechtsanwalt` — … ← EXISTIERT NICHT
- `qualitaetspruefung-builder-daten-red` — … ← EXISTIERT NICHT
```

**Ursache:** Slugs wurden in PR #229 (Word-Salat) und durch nachfolgende Codex-Polish-Commits umbenannt; die statischen Fachlandkarte-Tabellen in den ~530 Skelett-Skills wurden nicht mitgezogen.

**Geschätzte Reichweite:** mindestens 530 Skills × je 10-15 Cross-Refs = ~6 000 broken refs.

**Lösungsvorschlag:**
- Skript schreibt die Fachlandkarte-Tabelle pro Skelett-Skill **dynamisch** aus dem aktuellen Plugin-Verzeichnis neu (max. 15 Geschwister-Skills pro Tabelle, sortiert nach Slug).
- Geschätzter Aufwand: 1 h (Skript + Verifikation).

---

#### S3. 27 Skills mit `p<Nummer>` statt `§<Nummer>` im Slug (InsO-Plugin)

In `fachanwalt-insolvenz-sanierungsrecht/skills/` finden sich 27 Slugs der Form `p001-ziele-p003c-zustandigkeit-p004a`. Das `p` steht für `§` — Codex hat die Sonderzeichen-Substitution unsauber gemacht. Beispiele:

- `p003d` (kompletter Slug — keinerlei semantischer Inhalt; nur "§ 3 d InsO" verschleiert)
- `p126`
- `p139-eroffnungsantrag-p147`
- `p270f-anordnung-p270g-eigenverwaltung`
- `p020-auskunfts-p021-anordnung-p022` (drei §§ zusammengeworfen)
- `p092-gesamtschaden-p093-personliche-p227` (Word-Salat)

**Konsequenz:** Slug ist nicht auffindbar (wer sucht nach "p020"?), Tool-Description ist auch noch generisch ("p020-auskunfts-p021-anordnung-p022" — als sollte ein Mandant das eingeben).

**Lösungsvorschlag:**
- Pro Slug: `p` zu `paragraph-` ersetzen oder semantisches Thema aus dem Body extrahieren und als Slug verwenden:
  - `p003d` → `inso-3d-gruppen-gerichtsstand`
  - `p020-auskunfts-p021-anordnung-p022` → `inso-20-21-auskunftspflicht-sicherungsanordnung` oder einzelne Skills.
- Geschätzter Aufwand: 1 h (per-Skill manuelle Inspektion + Rename).

---

### 🟡 Mittel — beeinträchtigt Lesbarkeit / Konsistenz

#### M1. Asset-Marker-Inkonsistenz zwischen README, SKILLS.md, CHANGELOG, ASSET_INDEX

| Datei | Behauptete Skill-Zahl |
|---|---|
| Tatsächlich vorhanden | **18 549** |
| `README.md` Zeile 36 | 18 536 |
| `CHANGELOG.md` Zeile 50 | 18 549 (korrekt) |
| `CHANGELOG.md` Zeile 89 | 18 536 |
| `SKILLS.md` Zeile 3 | 18 549 (korrekt) |
| `ASSET_INDEX.md` | "211 Plugins" (tatsächlich 212) |

**Lösungsvorschlag:**
- README und CHANGELOG (Zeile 89) auf 18 549 / 212 / 203 angleichen.
- Asset-Index-Marker-Skript (`scripts/refresh-asset-index.*`) prüfen und einmal laufen lassen; ggf. in CI integrieren.
- Geschätzter Aufwand: 5 min.

---

#### M2. 20 Skills mit unbalanced Klammern in Description

Aus dem Scan:

```
fachanwalt-verwaltungsrecht/skills/fa-verwaltungsrecht-mandant-redteam-gate
fachanwalt-verkehrsrecht/skills/verkehrsstrafrecht-interessen-verkehrsunfall
fachanwalt-insolvenz-sanierungsrecht/skills/p270f-anordnung-p270g-eigenverwaltung
fachanwalt-insolvenz-sanierungsrecht/skills/livecheck-fristennotiz-sanierungsrecht
fachanwalt-insolvenz-sanierungsrecht/skills/p139-eroffnungsantrag-p147
fachanwalt-insolvenz-sanierungsrecht/skills/p020-auskunfts-p021-anordnung-p022
fachanwalt-insolvenz-sanierungsrecht/skills/p092-gesamtschaden-p093-personliche-p227
fachanwalt-insolvenz-sanierungsrecht/skills/p083-erbschaft-p084-auseinandersetzung
fachanwalt-insolvenz-sanierungsrecht/skills/p260-uberwachung-p261-aufgaben-p262
fachanwalt-insolvenz-sanierungsrecht/skills/p003e-unternehmensgruppe-p004b
fachanwalt-agrarrecht/skills/eu-agrarfoerderung-gap-direktzahlungen-hoefe
fachanwalt-miet-wohnungseigentumsrecht/skills/miet-modernisierungsmieterhoehung-wem
fachanwalt-vergaberecht/skills/facto
selbstvertreter-sozialgericht/skills/pflegegeld-pflegegrad-mds-gutachten-streit
fachanwalt-sozialrecht/skills/sgb-sg
```

`description` öffnet z. B. `(`, schließt nicht oder umgekehrt. JSON/Markdown sind tolerant — Validator schlägt nicht an —, aber Modellverarbeitung kann durcheinandergeraten.

**Lösungsvorschlag:**
- Pro Skill einzelner Edit, fehlenden Klammer-Partner ergänzen oder entfernen.
- Geschätzter Aufwand: 20 min.

---

#### M3. 7 H1-Headings mit echter "X / Y / Z"-Aufzählung (legitim, aber stilistisch)

```
wandeldarlehen-lebenszyklus/kyc-aml-geldwaesche: "KYC / AML / Geldwäscheprävention"
gesellschaftsgruender/share-classes-a-b-c: "Anteilsklassen A / B / C / Common"
steuerrecht-anwalt-und-berater/tatsaechliche-verstaendigung-schlussbesprechung: "Tatsächliche Verständigung / Schlussbesprechung / Steuer-Ver"
insolvenzrecht/sanierungsgewinn-mandantenwarnung-iv-und-cro: "Sanierungsgewinn — Mandantenwarnung an Insolvenzverwalter / "
insiderrecht-compliance/employee-schulung: "Mitarbeiteraktienprogramme (ESOP / LTIP / RSU) – Insiderrech"
gesellschaftsrecht/handelsregisteranmeldung-integrations: "Handelsregisteranmeldung – HRB / HRA / GnR / PartGR"
verlagsredaktion/abstimmung-mit-produktion-satz-druck: "Abstimmung Produktion / Satz / Druck"
```

Diese sind **legitim** (Aufzählung verwandter Konzepte), aber das `…` am Ende von einigen Titeln zeigt, dass mein Mischmasch-Skript hier abgeschnitten hat. Beispiel "Tatsächliche Verständigung / Schlussbesprechung / Steuer-Ver" ist offensichtlich abgehackt.

**Lösungsvorschlag:**
- 3 Titel ergänzen / umformulieren (steuer-, sanierungs-, insider-Titel sind abgehackt).
- 4 weitere stehen sauber und können bleiben (KYC/AML, Anteilsklassen, Handelsregister, Produktion/Satz/Druck).
- Geschätzter Aufwand: 5 min.

---

#### M4. 4 Skills mit problematischen 2-Zeichen-Slugs

```
grosskanzlei-corporate-ma/skills/02/  — name: "02"
grosskanzlei-corporate-ma/skills/03/  — name: "03"
grosskanzlei-corporate-ma/skills/04/  — name: "04"
```

Plus weitere 2-3-Zeichen-Slugs (`bag`, `bgb`, `kg`, `ma`, `vvg`) — diese sind teils legitim (Abkürzungen). Aber rein numerische Slugs `02`/`03`/`04` sind unbrauchbar.

**Inspektion:** `02` heißt "Corporate und M&A Rechtsprechungsrecherche", `03` heißt "Transaktionsstruktur", `04` heißt "Umwandlungssteuerrecht Buchwertantrag". Bedeutung steckt nur in der Description; Slug ist sinnfrei.

**Lösungsvorschlag:**
- Renamen zu sprechenden Slugs:
  - `02` → `corporate-rechtsprechungsrecherche`
  - `03` → `transaktionsstruktur-share-asset-deal`
  - `04` → `umwandlungssteuerrecht-buchwertantrag`
- Geschätzter Aufwand: 5 min.

---

#### M5. 1 Plugin ohne Einstiegs-Skill: `normenkontrollrat-nkr`

Hat weder `allgemein/` noch `einstieg-routing/` noch `kaltstart-*/`. Nutzer:innen finden keinen Triage-Einstieg.

**Lösungsvorschlag:**
- `normenkontrollrat-nkr/skills/allgemein/SKILL.md` anlegen mit Plugin-Überblick und Routing zu den vorhandenen Spezial-Skills.
- Geschätzter Aufwand: 10 min.

---

### 🟢 Klein — Komfort / Pflege

#### K1. Stand-Marker in ASSET_INDEX.md veraltet

Zeile 211 nennt "211 Plugins" (jetzt 212), Zeile 229 nennt "203 Testakten" — Letzteres stimmt zwar, aber die Auto-Update-Logik scheint nicht synchron zu laufen.

**Lösungsvorschlag:** Trigger des Refresh-Skripts in einen Git-Hook oder eine GitHub Action setzen.

---

#### K2. Multiple Stand-Daten in einer Datei

In `CHANGELOG.md` stehen Stände aus v237, v238 und v239 nebeneinander mit teils widersprüchlichen Skill-Zahlen. Das ist normales Changelog-Verhalten, aber bei Validierung Augenmerk.

---

## Was sauber ist ✅

| Check | Ergebnis |
|---|---|
| Validator (`scripts/validate-plugin-structure.mjs`) | **grün** |
| Plugin-Verzeichnis ↔ Marketplace.json | 212 ↔ 212, **synchron** |
| Plugin-Versionen einheitlich | alle 212 auf `239.0.0` |
| V90-Fachkern-Boilerplate | 0 |
| "ergänzende Prüffelder"-Mischmasch | 0 |
| "Dieser Workflow-Skill für"-Klon | 0 |
| Multiple H1 in Skills | 0 |
| Word-Salat-Slugs (Doppel-Token) | 0 |
| Slugs > 64 Zeichen (Anthropic-Limit) | 0 |
| Frontmatter ungültig (kein Name/Description) | 0 |
| Description > 1024 Zeichen | 0 |
| Description mit HTML `<>` | 0 |
| Skills mit identischem Body | 0 echte Duplikate (nur 1 cross-Plugin, ist OK) |
| Frontmatter-Name ≠ Verzeichnisname | 0 (außer YAML-Quote-Cosmetik bei `02`/`03`/`04`) |

---

## Priorisierter Implementierungsplan

Falls Tom alle Findings adressieren will:

1. **S1** Descriptions individualisieren (479 Skills, 30 min, Skript). **Höchster Hebel** für Skill-Funktion.
2. **S2** Fachlandkarte-Cross-Refs reparieren (~530 Skills, ~6 000 broken refs, 1 h, Skript).
3. **M2** 20 Klammer-Defekte (20 min, manuell).
4. **S3** 27 `p<Nr>` Slugs renamen (1 h, manuell mit Body-Inspektion).
5. **M4** 3 numerische Slugs (`02`/`03`/`04`) renamen (5 min).
6. **M3** 3 abgehackte H1-Titel ergänzen (5 min).
7. **M5** `normenkontrollrat-nkr/allgemein` anlegen (10 min).
8. **M1 + K1** Asset-Marker auf 18 549 / 212 angleichen + Refresh-Skript triggern (5 min).

**Gesamtaufwand:** ca. 3 Stunden bis komplett sauber.

---

## Kein-Mist-Aussage

Im Vergleich zu den Vor-PR-Zuständen ist das Repo **deutlich sauberer**. Die verbliebenen Findings sind:

- **2 verkettete Folgewirkungen meiner eigenen PRs**: S1 (Description nicht individualisiert) und S2 (Cross-Refs nicht nachgezogen) — beide aus PR #227.
- **3 Codex-Erblasten**: S3 (`p<Nr>`-Slugs), M2 (Klammer-Defekte), M3 (abgehackte H1).
- **3 Pflege-Themen**: Asset-Marker, fehlender Einstiegs-Skill, numerische Slugs.

Keine fundamentalen Bugs, keine Skill-Beschädigungen, keine verlorene Substanz.
