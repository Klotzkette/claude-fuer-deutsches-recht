# Codex-Instruktion: Skill-Veredelung auf Anthropic-Niveau
## Konkreter Implementierungsauftrag für ~1000+ verbesserbare Skills

Verfasser: Claude (Opus 4.7)
Stand: 2026-06-05
Branch: `claude/skill-improvements-codex-instructions`
Adressat: Codex
Aufgabe: Implementiere die unten gelisteten sechs Operationen. Reihenfolge ist vorgegeben (A → F), weil spätere Operationen auf früheren aufbauen.

**Grundprinzipien für Codex bei jeder Änderung:**

1. **Kein Substanzverlust.** Fachinhalt (BGB-§§, BVerfGE-Anker, Subsumtionsbeispiele, Mandantenwissen, Schriftsatzmuster) bleibt erhalten oder zieht in einen anderen Skill um. Nichts wird gelöscht.
2. **Nicht roboterhaft.** Keine neuen Templates. Wenn du eine alte Floskel ersetzt, ersetzt du sie durch **fallbezogene, lebenslagen-spezifische Sprache** — nicht durch eine andere Floskel.
3. **Individualisierung statt Generizität.** Jeder Skill bekommt sein **eigenes** Norm-Profil, seine **eigenen** Anker-Az, seine **eigenen** Ausgaben. Beispiel: ein Skill zu § 86b SGG zitiert § 86b-Rechtsprechung — nicht den BAG-Entgeltgleichheits-Anker, der heute überall steht.
4. **Anthropic-Niveau heißt:** Ein Skill = eine Frage = ein klarer Trigger im `description`-Feld. Description sagt **wann**, nicht **wie**.
5. **Sprache:** Sie-Form (außer Plugin spielt explizit Du-Mandat). Behördensprache nüchtern. Lebenslagen statt Lehrbuch-Intros.

---

## Datenlage (Stand 2026-06-05)

| Kennzahl | Wert |
|---|---|
| SKILL.md gesamt | 5951 |
| Plugins | 209 |
| Kompendien mit "kompendium-NN-X-bis-Y"-Slugs | 4369 |
| Skills mit V90-Fachkern-Block (Boilerplate) außerhalb `allgemein` | 841 |
| Skills mit exakt 35 Zeilen (byte-identische `workflow-*`-Klone, nur Plugin-Name getauscht) | 242 |
| Skills mit `workflow-kaltstart-und-routing`-Slug (verteilt auf Plugins) | 101 |
| Skills mit `workflow-dokumentenintake`-Slug | 97 |
| Skills mit `workflow-output-waehlen`-Slug | 88 |
| Skills mit `workflow-rechtsquellen-livecheck`-Slug | 87 |
| Skills mit `workflow-unterlagen-lueckenliste`-Slug | 95 |
| Skills mit `workflow-anschluss-skills-router`-Slug | 66 |
| Skills mit `spezial-*-livequellen-und-rechtsprechungscheck` | 188 |
| Skills mit `spezial-*-red-team-und-qualitaetskontrolle` | 88 |
| Kompendien mit Boilerplate-Description `"…: eigenständiger Arbeits-Skill für verwandte Arbeitsmodule…"` | 4691 |
| Skills mit Description-Marker `im Plugin X` | 652 |

**Erkennbares Veredelungs-Volumen:** Mindestens **1850 Skills** lassen sich substanziell verbessern, davon ~880 (workflow-* + spezial-* Wrapper) durch Verschmelzung oder Individualisierung und ~970 durch De-Boilerplate-Operationen auf Kompendien. Das überschreitet das von Tom genannte Ziel "1000 Skills" deutlich.

---

## Operation A — Plugin-spezifische Veredelung der sechs Workflow-Wrapper-Skills

### Befund
Sechs `workflow-*`-Skills sind aktuell **byte-identische Klone**, in 60-101 Plugins parallel vorhanden, nur mit Plugin-Name getauscht:

| Skill-Slug | Vorkommen | Zustand |
|---|---|---|
| `workflow-kaltstart-und-routing` | 101 Plugins | Großteils 35-Zeilen-Klon mit Plugin-Name in der `description` |
| `workflow-dokumentenintake` | 97 Plugins | Klon mit kleinen plugin-spezifischen Anhängen (Bsp. `fachanwalt-verkehrsrecht`: Verkehrsrechts-Intake nach Säule) |
| `workflow-unterlagen-lueckenliste` | 95 Plugins | Klon |
| `workflow-output-waehlen` | 88 Plugins | Klon |
| `workflow-rechtsquellen-livecheck` | 87 Plugins | Klon |
| `workflow-anschluss-skills-router` | 66 Plugins | Klon |

**Belegt:** `diff` zwischen `ki-richtlinie-kanzleien/skills/workflow-anschluss-skills-router/SKILL.md` und `common-law-kompass/skills/workflow-anschluss-skills-router/SKILL.md` nach Plugin-Name-Substitution = **0 Bytes Unterschied**. Reine Wrapper.

**Gegenbeispiel:** `patentrecherche/skills/workflow-dokumentenintake/SKILL.md` ist tatsächlich plugin-spezifisch (Espacenet, DEPATISnet, IPC/CPC-Klassen, FTO, Validity). Das ist der Zielzustand.

### Auftrag an Codex

Für **jeden** der sechs Wrapper-Slugs in **jedem** der 60-101 Plugins:

#### Schritt A1 — Inhaltliche Individualisierung (Pflicht)

Pro Plugin und Wrapper-Skill:

- **Identifiziere das Plugin-spezifische Substrat:** Was wird in diesem Rechtsgebiet hochgeladen / dokumentiert / abgefragt / routet sich wohin?
  - Bei `patentrecherche/workflow-dokumentenintake`: Erfindungsmeldung, Anspruchssatz, DEPATISnet-Treffer — schon gut.
  - Bei `selbstvertreter-amtsgericht/workflow-dokumentenintake`: Klageschrift, Klageerwiderung, Ladung, Urteil, Vollstreckungstitel.
  - Bei `mietrecht/workflow-dokumentenintake`: Mietvertrag, Nebenkostenabrechnung, Mängelanzeige, Mahnung, Kündigungsschreiben, Räumungsklage.
  - Bei `kartellrecht-marktabgrenzung-pruefung/workflow-dokumentenintake`: Anmeldungsunterlagen, Umsatzdaten, Marktbefragungen, BKartA-Schreiben, Phase-I-Mitteilung.
- **Ersetze die 35 Klon-Zeilen** durch 100-200 Zeilen plugin-spezifischen Inhalt.
- **Behalte die Slug-Namen** für Operation A. Erst in Operation D werden sie umbenannt.

#### Schritt A2 — Description präzisieren

Aktuell: `"Kaltstart und Routing im Plugin <X>: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills."`

Ersetze durch eine Lebenslagen-Beschreibung, z. B.:

- `workflow-kaltstart-und-routing` in `mietrecht`: `"Erstanalyse mietrechtlicher Sachverhalte: ordnet Wohnraummiete / Gewerbemiete / WEG, sortiert nach Mängel / Kündigung / Betriebskosten / Mieterhöhung, identifiziert Notfristen § 174 BGB Schriftform und § 573c BGB Ordentliche Kündigung, leitet zum passenden Spezial-Skill."`
- `workflow-kaltstart-und-routing` in `kartellrecht-marktabgrenzung-pruefung`: `"Erstanalyse kartellrechtlicher Vorgänge: trennt Fusionskontrolle / Kartellverbot / Marktmissbrauch, identifiziert BKartA / EU-KOM / nationale Behörde, ordnet relevante Marktdefinition (sachlich, räumlich, zeitlich), leitet zur passenden Methodik."`

#### Schritt A3 — Bei echter Redundanz: Löschen statt Veredeln

In einigen Plugins ist der Workflow-Wrapper schlicht überflüssig, weil das `allgemein`-Skill dieselbe Funktion bereits übernimmt. Prüfe bei jedem Plugin: Wenn `allgemein` bereits Triage + Routing macht, **lösche** `workflow-kaltstart-und-routing` und `workflow-anschluss-skills-router`. Behalte nur, wenn substantiell andere Funktion.

**Geschätzte Reduktion:** ~250 Skills (aus den 534 wrapper-Vorkommen) bleiben nach Individualisierung und Löschung. Ergebnis: 280-330 echte, plugin-spezifische Workflow-Skills.

---

## Operation B — Spezial-Wrapper auflösen (276 Skills)

### Befund
Zwei systematische Wrapper-Klassen:

- `spezial-*-livequellen-und-rechtsprechungscheck` (188 Skills) — generischer "frische Rechtsprechung holen"-Stub.
- `spezial-*-red-team-und-qualitaetskontrolle` (88 Skills) — generischer "Fehler-Check"-Stub.

Diese sind weder fachlich individualisiert noch unterscheiden sich die Bodies wesentlich.

### Auftrag an Codex

#### Schritt B1 — Livequellen-Skills

Ersetze die 188 `spezial-*-livequellen-*`-Skills durch **plugin-spezifische Live-Quellen-Karten**. Pro Plugin entsteht eine Datei `skills/<plugin-slug>-quellenkarte/SKILL.md` mit:

- Konkrete Behörden-URLs (DPMA, BMF, BKartA, BfArM etc.)
- Konkrete Rechtsprechungsdatenbanken mit den **plugin-relevanten Senaten/Spruchkörpern** (Bsp. `kartellrecht`: BGH Kartellsenat KZR, OLG Düsseldorf VI-Kart)
- Konkrete Aktenzeichen-Muster (Bsp. `patentrecht`: X ZR / 4 Ni / BPatG)
- Konkrete Fachjournale, die der Nutzer kennen muss (Bsp. `arbeitsrecht`: NZA, NJW-RR, AuR)
- Quellenhygiene-Regel: "Kein BeckRS/juris-Blindzitat aus Modellwissen" (1-Zeiler, nicht der bisherige 5-Block).

#### Schritt B2 — Red-Team-Skills

Ersetze die 88 `spezial-*-red-team-*`-Skills durch **plugin-spezifische Fehlerlisten**. Pro Plugin entsteht `skills/<plugin-slug>-redteam-fehlerkatalog/SKILL.md` mit:

- 8-15 **konkrete typische Fehler** in diesem Rechtsgebiet (nicht: "falsche Frist" — sondern: "Übersehene 4-Tage-Bekanntgabe-Fiktion nach § 37 Abs. 2 SGB X seit 01.01.2025").
- Pro Fehler: Symptom + Diagnose + Heilung.
- Bsp. für `sozialrecht-redteam-fehlerkatalog`:
  - **Fehler:** Klagefrist § 87 SGG verpasst, weil Bekanntgabe-Fiktion ab 01.01.2025 auf 4 Tage verkürzt (vorher 3 Tage). **Diagnose:** Tagebuchberechnung mit altem 3-Tage-Anker. **Heilung:** Wiedereinsetzung § 67 SGG mit Substantiierung der Fristberechnung.

#### Schritt B3 — Verschmelzung wo angebracht

Wenn ein Plugin sowohl `*-livequellen-*` als auch `*-red-team-*` enthält und beide unter 50 Zeilen sind, **verschmelze** zu einem Skill `<plugin>-qualitaetssicherung/SKILL.md`.

**Geschätzte Reduktion:** 276 → ~140 plugin-spezifische Qualitäts-Skills.

---

## Operation C — Boilerplate-Diet im V90-Fachkern (841 Skills)

### Befund
841 Skills tragen einen identischen 6-Zeilen-V90-Fachkern-Block (Problemfokus / Normenradar / Verifizierte Anker / Arbeitsmodus / Outputpflicht / Fehlerbremse). 

**Konkret:** 102 Skills verschiedener Plugins enthalten denselben BAG-Anker `BAG, Urteil vom 23.10.2025 - 8 AZR 300/24` — auch Skills, die mit Arbeitsrecht nichts zu tun haben (z. B. Bürgergeld-Module in `selbstvertreter-sozialgericht`). 82 Skills enthalten denselben BSG-Anker.

### Auftrag an Codex

#### Schritt C1 — V90-Block nur im `allgemein`-Skill belassen

Für jedes Plugin:
1. Behalte den V90-Block in `skills/allgemein/SKILL.md`.
2. **Entferne** ihn aus allen anderen Skills.

#### Schritt C2 — Modulspezifische Drei-Zeilen-Anker einsetzen

Wo der V90-Block entfernt wird, **füge einen 3-zeiligen modulspezifischen Anker** ein:

- **Zeile 1:** Tragende Norm (1-2 Paragraphen, das wirklich Relevante).
- **Zeile 2:** Eine zentrale Entscheidung mit Gericht/Datum/Az + Kernaussage in einem Satz — passend zum **konkreten Modul**.
- **Zeile 3:** Quellenhygiene-Hinweis (kurz: "Az live verifizieren").

Beispiele:

- In `selbstvertreter-sozialgericht/skills/.../eilantrag-86b-sgg-grundlagen`:
  - **Norm:** § 86b SGG iVm § 920 ZPO analog.
  - **Anker:** BVerfG, Beschluss vom 12.05.2005 - 1 BvR 569/05 (effektiver Eilrechtsschutz Art. 19 IV GG); bei Bürgergeld-eA zusätzlich BSG, Beschluss vom 13.10.2011 - B 14 AS 33/11 B (Existenzminimum-Sicherung).
  - **Quellenhygiene:** Az live über bsg.bund.de / bverfg.de prüfen.
- In `beamtenrecht/skills/.../alimentation-fuenf-parameter`:
  - **Norm:** Art. 33 V GG.
  - **Anker:** BVerfGE 139, 64 (R-Besoldung 5.5.2015 - 2 BvL 17/09); BVerfGE 155, 1 (Berliner Richterbesoldung 4.5.2020 - 2 BvL 4/18).
  - **Quellenhygiene:** Bandzahl und Rn live in bverfg.de prüfen.

**Vorteil:** Anker ist **modulrelevant**, nicht generisch. Modell bekommt im Kontext genau das, was zur konkreten Frage passt.

**Schätzung:** Entfernt ~5050 Boilerplate-Zeilen aus dem Repo, fügt ~2520 modulspezifische Zeilen ein. Netto: -2530 Zeilen, +2520 Substanz.

---

## Operation D — Kompendien re-clustern und umbenennen (4369 Skills)

### Befund
4369 Skills heißen `kompendium-NN-<erstesmodul>-bis-<letztesmodul>`. Drei Probleme:

1. **Slug-Trümmer:** "kompendium-08-buergergeld-ueberbru-bis-eilantrag-86b-sgg-gr" (60 Zeichen am Limit). Nicht durchsuchbar.
2. **Alphabetische statt semantische Bündelung:** Module B-D-D-D-E in einem File, obwohl thematisch nicht verwandt.
3. **Identische `Arbeitsregel`-Boilerplate** ("1. Zuerst das passende Arbeitsmodul…") in allen 4369 Files.

### Auftrag an Codex

#### Schritt D1 — Re-Clustering nach Sachzusammenhang

Pro Plugin:

1. Liste alle Module aller Kompendien auf (es gibt z. B. in `selbstvertreter-sozialgericht` heute 26 Kompendien × ~5 Module = ~130 Module).
2. Cluster die Module **nach Rechtsgebiet/Lebenslage**, nicht nach Alphabet.
3. Bilde 6-12 neue Kompendien pro Plugin mit je 4-7 thematisch verwandten Modulen.
4. Neue Slugs: `<plugin-prefix>-<cluster-thema>` ohne `NN-X-bis-Y`-Brücke.

**Konkrete Cluster-Vorschläge für die wichtigsten Plugins:**

##### `selbstvertreter-sozialgericht` (26 → ~10 Kompendien)
- `selbstvertreter-sozialgericht-eilrechtsschutz` (Eilantrag § 86b SGG + Bürgergeld-eA + Krankenkasse-eA + Pflegekasse-eA + Aufschiebende Wirkung)
- `selbstvertreter-sozialgericht-pflege` (Pflegegrade + Pflegegeld + Pflegekassenleistungen + Verhinderungspflege + Pflegekurse)
- `selbstvertreter-sozialgericht-buergergeld` (Antrag + Bedarfsgemeinschaft + Sanktionen + Mehrbedarf + Aufrechnung + Überbrückungsgeld nach Haft)
- `selbstvertreter-sozialgericht-rente` (EM-Rente + Mutterrente + Kontenklärung + Versorgungsausgleich)
- `selbstvertreter-sozialgericht-gdb-und-schwerbehinderung` (GdB-Verfahren + Schwerbehindertenausweis + Nachteilsausgleiche + Persönliches Budget + Eingliederungshilfe)
- `selbstvertreter-sozialgericht-krankenkasse` (Hilfsmittel + Häusliche Krankenpflege + Wahltarife + Zahnersatz + Mutterschutz)
- `selbstvertreter-sozialgericht-verfahrensformalitaeten` (Akteneinsicht § 25 SGB X + DSGVO Art. 15 + Anwaltskosten § 183 SGG + Klage zur Niederschrift + Mitwirkungspflichten § 60 SGB I)
- `selbstvertreter-sozialgericht-fristen-und-rechtsmittel` (Widerspruchsfrist § 84 SGG + Wiedereinsetzung § 67 SGG + Berufung + Revision + Zulassungsgrenzen)
- `selbstvertreter-sozialgericht-zugaenglichkeit-und-it` (Dolmetscher § 185 GVG + Einfache Sprache + PDF-Erstellung + Mein Justizpostfach + Schriftform)
- `selbstvertreter-sozialgericht-wohnen-und-existenzsicherung` (Wohngeld + KdU + Sozialhilfe + BAföG + Elterngeld + Kindergeld)

##### `beamtenrecht` (22 → ~8 Kompendien)
- `beamtenrecht-status-und-eingriff` (Status + Statusamt/Funktionsamt + Ernennung + Entlassung + Versetzung)
- `beamtenrecht-besoldung-grundsystem` (Besoldungsgruppen + Eingruppierung + Stufenfestsetzung + Familienzuschlag + Aufstieg)
- `beamtenrecht-besoldung-zulagen` (Auslandszuschlag + Erschwerniszulagen + Mehrarbeit + Schichtdienst + Gefährdung)
- `beamtenrecht-alimentation-verfassung` ⭐ (Fünf-Parameter-BVerfG + Mindestabstandsgebot + Zeitnahe Geltendmachung)
- `beamtenrecht-konkurrenten-und-beurteilung` (Konkurrentenklage + Beurteilung + Bestenauslese Art. 33 II GG + Eilrechtsschutz § 123 VwGO)
- `beamtenrecht-disziplinar-und-dienstvergehen` (BDG + Disziplinarmaßnahmen + Beamtstg § 47 + Außerdienstliches)
- `beamtenrecht-dienstunfaehigkeit-und-versorgung` (BeamtVG + Ruhegehalt + Hinterbliebenenversorgung + Unfallruhegehalt + Dienstunfähigkeit)
- `beamtenrecht-spezialberufe` (Polizei/Feuerwehr + Soldaten + Hochschullehrer + PTBS + Schwerbehinderte-Bewerber)

##### `roemisches-recht` (22 → ~8 Kompendien)
- `roemisches-recht-personenrecht-status-und-familie`
- `roemisches-recht-sachenrecht` (Eigentum + Besitz + Servituten + Hypotheca + Vindikation)
- `roemisches-recht-schuldrecht-vertraege` (Kauf + Leihe + Darlehen + Miete + Auftrag + Gesellschaft + Innominatkontrakte)
- `roemisches-recht-schuldrecht-haftung` (Delikte + Bereicherung + GoA + Aquilia)
- `roemisches-recht-erbrecht` (Testament + Kodizill + Fideikommiss + Pflichtteil)
- `roemisches-recht-prozessrecht` (Legisaktionen + Formularprozess + Kognitionsverfahren + Konkurs)
- `roemisches-recht-quellen-und-rezeption` (XII Tafeln + Digesten + Justinian + Glossatoren + Rezeption ius commune)
- `roemisches-recht-vergleich-mit-bgb` ⭐ (rom-074 bis rom-081 — die didaktisch besten Module zu Bereicherung/GoA/Delikt/Servituten-Vergleich)

#### Schritt D2 — Slug-Konvention durchsetzen

| Alte Konvention | Neue Konvention |
|---|---|
| `kompendium-08-buergergeld-ueberbru-bis-eilantrag-86b-sgg-gr` | `selbstvertreter-sozialgericht-eilrechtsschutz` |
| `komp-15-teil-02-laufbahnrecht-laender-matrix` | `beamtenrecht-laufbahnrecht-laendermatrix` |
| `kompendium-11-pralr-043-band-teil-bis-pralr-049-abschlussm` | `pralr-quellen-und-methodik` |

Regel: Max 45 Zeichen, semantischer Cluster-Name, kein `NN`, kein `bis`.

#### Schritt D3 — `Arbeitsregel`-Boilerplate ersetzen

Die identische 4-Punkt-Liste in 4369 Files raus. Stattdessen ein **plugin-spezifischer Arbeitsweg-Satz** pro Kompendium, z. B.:

- In `selbstvertreter-sozialgericht-eilrechtsschutz`: *"Eilrechtsschutz beim SG braucht Anordnungsanspruch und Anordnungsgrund. Glaubhaftmachung durch eidesstattliche Versicherung. Stets parallel Widerspruch oder Klage in der Hauptsache führen. Wenn Existenzminimum betroffen: BVerfG verlangt zügige Entscheidung."*
- In `beamtenrecht-alimentation-verfassung`: *"Verfassungsmäßigkeit der Alimentation ist zweistufig: erste Stufe Fünf-Parameter, zweite Stufe Gesamtabwägung. Zeitnahe Geltendmachung im Haushaltsjahr ist Anspruchsvoraussetzung. BVerfG-Urteile zitierst Du nach Band/Rn, nicht nach Az allein."*

---

## Operation E — Description-Triggert auf Anthropic-Niveau (4691 Skills)

### Befund
4691 Skills haben eine `description` der Form:

```
"<plugin-name>: eigenständiger Arbeits-Skill für verwandte Arbeitsmodule zu X, Y, Z und N weitere Arbeitsmodule; mit Intake, Prüfroutine, Normen-/Quellenradar, Beweislogik, Outputmuster und Qualitätscheck."
```

Anthropic-Vergleich:

- Anthropic `pdf`: `"Use this when the user wants to read, edit, or create a PDF document."` — sagt **wann** das Skill geladen werden soll.
- Anthropic `xlsx`: `"Use this skill when working with Excel spreadsheets (.xlsx, .xls files)."` — Trigger.
- Unsere Kompendien-Description sagt **was im Skill drin ist** (Intake / Prüfroutine / etc.) — kein Trigger.

### Auftrag an Codex

Ersetze die 4691 Boilerplate-Descriptions durch **Lebenslagen-Trigger**:

#### Muster für Spezialskills

```
"Nutze dies, wenn <konkrete Lebenslage / konkreter Auftrag>.
Beispiele: <2-3 prototypische Sätze, mit denen Nutzer:innen das Skill auslösen>."
```

Beispiel `selbstvertreter-sozialgericht-eilrechtsschutz/SKILL.md`:

```
description: "Nutze dies, wenn jemand selbstvertretend einen Eilantrag § 86b SGG beim Sozialgericht braucht — typischerweise weil Bürgergeld eingestellt wurde, eine Krankenkassen-Leistung dringend verweigert wird oder ein Pflegehilfsmittel zurückgehalten wird. Auslöser: 'Mein Geld wurde gestrichen', 'Die Kasse zahlt nicht', 'Ich brauche einen Eilantrag'."
```

Beispiel `beamtenrecht-alimentation-verfassung/SKILL.md`:

```
description: "Nutze dies, wenn ein Beamter oder Richter Verfassungsmäßigkeit der eigenen Besoldung prüft — Fünf-Parameter-Test erster Stufe (BVerfGE 139, 64), Mindestabstand zur Grundsicherung (BVerfG 4.5.2020 - 2 BvL 4/18), zeitnahe Geltendmachung im Haushaltsjahr. Auslöser: 'Ist meine Besoldung amtsangemessen?', 'Widerspruch gegen R-Besoldung', 'Verfassungsbeschwerde Alimentation'."
```

#### Anti-Patterns die zu vermeiden sind

- ❌ `"<plugin>: X mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis."` (27 Skills haben das aktuell — alle ersetzen)
- ❌ `"<plugin>: eigenständiger Arbeits-Skill für …"` (4691 Skills — alle ersetzen)
- ❌ Kommas in Zahlen: `1,5` → `1.5` oder `eineinhalb`. (CLAUDE.md schon vorgegeben.)
- ❌ HTML-Tags `<>` in Description (Validator beschwert sich).
- ❌ Description > 1024 Zeichen (Validator-Bruch).

---

## Operation F — Mini-Wrapper-Klone konsolidieren (~250 Skills)

### Befund
In `beamtenrecht` (Beispiel) gibt es vier Mini-Skills (38-42 Zeilen), die strukturell **denselben Inhalt** mit unterschiedlichen Titeln haben:

- `red-team-beamtenrecht/SKILL.md`
- `output-waehlen-memo-widerspruch-eilantrag/SKILL.md`
- `quellenhygiene-beamtenrecht-fundstellen-red-team/SKILL.md`
- `versorgungsakte-dokumentenintake-und-berechnung/SKILL.md`
- `aktenstruktur-und-dokumentenintake/SKILL.md`

Sie wiederholen die identische "Status und Rechtsquelle / Eingriff und Ziel / Materielle Prüfung / Verfahren / Output"-Prüfschema-Boilerplate. 37 Skills im `beamtenrecht` allein nutzen diese Liste; über alle Plugins hinweg 100+.

### Auftrag an Codex

#### Schritt F1 — Pro Plugin: Mini-Wrapper verschmelzen oder löschen

Pro Plugin alle Skills < 60 Zeilen sammeln. Wenn ihre Bodies > 70 % Überlappung haben:

- **Variante A (bevorzugt):** Verschmelze zu einem einzigen `<plugin>-qualitaetssicherung/SKILL.md` mit klaren Subsections (Red Team / Output-Wahl / Quellenhygiene / Aktenstruktur). Sub-Sections sind durch Headings strukturiert, nicht durch separate SKILL.md-Files.
- **Variante B:** Wenn das `allgemein`-Skill schon diese Funktionen abdeckt: **lösche** die Mini-Wrapper komplett.

#### Schritt F2 — Inhaltlich aufwerten

Die verschmolzenen Skills sollen **plugin-spezifisch** werden:

- Bsp. `beamtenrecht-qualitaetssicherung`: Statt generischer "Status / Eingriff / Materielles / Verfahren / Output"-Liste — konkrete Red-Team-Fragen zu Beamtenrecht: *"Habe ich Bundes- vs. Landesbesoldung sauber getrennt? § 19 BBG vs. § 18 LBG NW? Ist Konkurrentensituation berücksichtigt? Bestenauslese Art. 33 II GG geprüft? Bei Eilantrag § 123 VwGO: Anordnungsanspruch vs. Anordnungsgrund? Akteneinsicht § 88 ff. BBG vor Schriftsatz?"*

**Geschätzte Reduktion:** ~250 Mini-Wrapper → ~100 echte plugin-spezifische Qualitäts-Skills.

---

## Operation G — Wissens-Injektions-Punkte (wo Tom-Wissen rein muss)

Das ist der wichtigste Punkt für Codex, weil Tom explizit sagt: *"mit dem von mir addierten / generierten Wissen, das ist wichtig"*.

### Auftrag an Codex

Bei jeder veredelten Skill-Datei prüfen, ob Tom-Wissen (in `references/`, in `CLAUDE.md`, in vorherigen Sessions) injiziert werden sollte. Die folgenden Wissensbestände sind in diesem Repo dokumentiert und sollen aktiv in die richtigen Skills eingearbeitet werden:

#### G1 — Methodik (in `references/methodik-buergerliches-recht.md`)
Soll referenziert werden in **allen** Skills, die Subsumtion machen. Konkret in Gutachtenstil-Skills (Hausarbeiten, Memos, Schriftsätze). Mehrere Plugins betroffen:
- `jurastudium`, `subsumtions-pruefer`, `bgb-at-pruefer`, `hausarbeitenmacher`
- alle `fachanwalt-*` Plugins (Mandantenmemos)

#### G2 — Zitierweise (in `references/zitierweise.md`)
Soll referenziert werden in **allen** Skills, die Quellen ausgeben. Das ist praktisch jedes Skill. Codex soll einen 1-Zeiler einbauen: *"Quellenangaben nach `references/zitierweise.md`."*

#### G3 — Quellenhygiene-Regeln aus CLAUDE.md
CLAUDE.md verbietet:
- Halluzinierte Aktenzeichen
- BeckRS/juris-Blindzitate aus Modellwissen
- Mandantengeheimnis-Verletzungen

Diese drei Verbote sind heute in 855 V90-Blocks redundant kopiert. Soll **einmal** in `references/quellenhygiene.md` ausgelagert und in jedem Skill referenziert werden, nicht ausgeschrieben.

#### G4 — Plugin-spezifische Sammlungen
Pro Plugin gibt es einen Wissensschatz, den Tom über mehrere Sessions kuratiert hat:

| Plugin | Tom-Wissen, das injiziert werden soll |
|---|---|
| `beamtenrecht` | BVerfGE 139, 64 + BVerfGE 155, 1; Fünf-Parameter-Trennung erste/zweite Stufe; Mindestabstandsgebot 15 %; Zeitnahe Geltendmachung |
| `selbstvertreter-sozialgericht` | § 86b SGG-Eilantragsmuster mit eidesstattlicher Versicherung; 4-Tage-Bekanntgabe-Fiktion § 37 II SGG seit 01.01.2025; § 183 SGG-Kostenfreiheit |
| `selbstvertreter-amtsgericht` | Drei-Führungsstufen-Modell (sehr geführt / normal / Kurzmodus); Stummer-Upload-Logik |
| `roemisches-recht` | Digestenstellen D. 4.9 (receptum nautarum), D. 12.6 (condictio indebiti), D. 13.6 (commodatum), D. 14.2 (lex Rhodia), D. 18.6 (Kauf-Gefahrtragung), D. 41.2 (Besitz); 11 Vergleichs-Module rom-074 bis rom-080 |
| `pralr` | Einl. §§ 74-75 Aufopferung, ALR II 5 §§ 196-197 Sklaverei, PrALR 38 Spezialinstitute |
| `arbeitszeugnis-analyse` | Geheimcode-Katalog rot/orange/grün, Zufriedenheitsformel-Decodierung, § 109 GewO |
| `kartellrecht-marktabgrenzung-pruefung` | SSNIP-Test, Marktabgrenzung sachlich/räumlich/zeitlich, BKartA-Phase-I/Phase-II |
| `bauträgervertrag` (40 Skills, von Tom kuratiert) | MaBV § 3, MaBV § 7, BGB §§ 650u ff., § 650v BGB Sicherheitsleistung |
| `gebrauchsmusterrecht` | GebrMG § 1 (Erfindungsbegriff), § 5 (Neuheit), § 13 (Eintragung), § 15 (Löschung) |
| `steuerrecht-anwalt-und-berater` | Alle DBA-Skills sind bereits Tom-individualisiert (60-Tage-Rückkehr, Grenzgänger-Frankreich/Schweiz/Österreich, Tie-Breaker-Rules) — **nicht anfassen**, das ist Gold |
| `roemisches-recht/rom-074 bis rom-081` | Vergleichs-Module BGB ↔ röm. Recht (Bereicherung, GoA, Delikt, Servituten, Hypothek, Gesellschaft, Kauf, lateinische Maximen) — sind bereits Tom-individualisiert |

#### G5 — V90 Fachkern: wo der eigentlich hingehört
Der V90-Block ist **gut gemeint, aber falsch platziert**. Er gehört NICHT in jedes Modul. Er gehört in `skills/allgemein/SKILL.md` pro Plugin **einmal**, als sektion "Qualitäts- und Quellenstandards für dieses Plugin". Dort darf er ausführlich sein — der Allgemein-Skill ist genau dafür da.

---

## Operation H — Naming-Konvention pro Plugin (alle 5951 Skills)

### Regeln (verbindlich für Codex)

1. **Max 45 Zeichen** im Slug (Anthropic-Limit ist 64, wir nehmen Puffer).
2. **ASCII only**, `[a-z0-9-]+`, keine `_`, keine Großbuchstaben.
3. **Kein `kompendium-NN-X-bis-Y`-Pattern**. Stattdessen semantischer Cluster-Name.
4. **Prefix nur, wenn nötig**. Wenn das Plugin `selbstvertreter-sozialgericht` heißt, muss nicht jeder Skill `selbstvertreter-sozialgericht-`-Prefix tragen — der Plugin-Pfad sagt das schon. Aber bei Cluster-Slugs ist Prefix lesbarkeits-helfend.
5. **Keine Stop-Wörter** wie `spezial-`, `workflow-`, `kompendium-`, `komp-`. Das ist Metadaten, kein Thema.
6. **Mit dem Cluster-Thema beginnen, nicht enden.** `eilrechtsschutz-86b-sgg` (gut) statt `sgg-86b-eilrechtsschutz` (umständlich).

### Slugnamen-Refactoring: Beispielliste

| Alter Slug | Neuer Slug |
|---|---|
| `kompendium-08-buergergeld-ueberbru-bis-eilantrag-86b-sgg-gr` | `eilrechtsschutz-86b-sgg` |
| `komp-15-teil-02-laufbahnrecht-laender-matrix` | `laufbahnrecht-laendermatrix` |
| `kompendium-11-pralr-043-band-teil-bis-pralr-049-abschlussm` | `pralr-quellen-und-methodik` |
| `spezial-pflichtverteidigung-livequellen-und-rechtsprechungscheck` | `pflichtverteidigung-quellenkarte` |
| `wirtschaftspruefer-bestaetigungsvermerk-risikofall-kaltstart-u` | `wp-bestaetigungsvermerk-risikofall` |
| `space-001-kaltstart-weltraummandat-quellenkarte-und-risikocockpi` | `weltraummandat-kaltstart` |
| `output-waehlen-memo-widerspruch-eilantrag` | (LÖSCHEN, weil in `allgemein` integriert) |

---

## Operation I — Validation und Qualitätskriterien (am Ende jeder Operation)

Nach jeder Operation Codex laufen lassen:

```bash
node scripts/validate-plugin-structure.mjs
```

Pflicht-Kriterien:

- ✅ Alle SKILL.md haben Frontmatter mit genau `name` + `description`.
- ✅ Alle `description` ≤ 1024 Zeichen.
- ✅ Alle Slugs ≤ 64 Zeichen (Soll: ≤ 45).
- ✅ Keine Zahl-Komma-Zahl-Muster.
- ✅ Kein HTML-`<>` in Description.
- ✅ Skill-`name` im Frontmatter = Verzeichnisname.
- ✅ Plugin-`description` in `plugin.json` ≤ 300 Zeichen.

Manuelle Stichproben durch Tom:

- 5 zufällige veredelte Skills durchlesen — keine generische Sprache, keine Boilerplate?
- 3 Plugins komplett durchgehen — sinnvolle Cluster, keine Redundanz?
- 1 Vergleich Anthropic-Skill (z. B. `pdf`) ↔ unser veredeltes Skill — vergleichbarer Stil?

---

## Operation J — Reihenfolge der Implementierung

Codex soll in dieser Reihenfolge arbeiten, weil Operationen aufeinander aufbauen:

1. **Operation C** (V90-Diet) zuerst — entfernt Boilerplate, macht den Rest lesbar.
2. **Operation E** (Description-Trigger) parallel — viele Descriptions berühren keine V90-Blocks.
3. **Operation B** (Spezial-Wrapper) — kleines, abgegrenztes Volumen, gut zum Üben.
4. **Operation A** (Workflow-Wrapper) — größtes Volumen, braucht plugin-spezifische Inhalte.
5. **Operation F** (Mini-Wrapper) — räumt nach den anderen auf.
6. **Operation D** (Re-Clustering + Rename) zuletzt — strukturelle Großoperation, sollte auf bereits bereinigtem Boden stattfinden.
7. **Operation G** (Wissens-Injektion) wirkt **parallel** in allen Operationen — pro Skill, das angefasst wird, prüfen.
8. **Operation H** (Naming) wird mit Operation D zusammengeführt.
9. **Operation I** (Validation) nach jeder Operation.

---

## Anhang 1 — Konkrete Liste der ~1000 worst skills (Beispiele)

Codex bekommt die vollständige Liste durch die folgenden Suchen (alle laufen direkt im Repo):

```bash
# 1. Workflow-Wrapper (~534 Skills, jeder ein Kandidat)
find . -name SKILL.md -path "*/skills/workflow-kaltstart-und-routing/*"
find . -name SKILL.md -path "*/skills/workflow-dokumentenintake/*"
find . -name SKILL.md -path "*/skills/workflow-output-waehlen/*"
find . -name SKILL.md -path "*/skills/workflow-rechtsquellen-livecheck/*"
find . -name SKILL.md -path "*/skills/workflow-unterlagen-lueckenliste/*"
find . -name SKILL.md -path "*/skills/workflow-anschluss-skills-router/*"

# 2. Spezial-Wrapper (~276 Skills)
find . -name SKILL.md -path "*/skills/spezial-*livequellen*"
find . -name SKILL.md -path "*/skills/spezial-*red-team*"

# 3. V90-Block in Modulen (841 Skills) — bekommen Operation C
grep -l "V90 Fachkern" -r --include=SKILL.md . | grep -v "/allgemein/"

# 4. Generische "mit geführtem Workflow"-Tagline (27 Skills)
grep -l "mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik" -r --include=SKILL.md .

# 5. Kompendien mit "X-bis-Y"-Slug (4369 Skills) — bekommen Operation D + H
find . -name SKILL.md -path "*/kompendium-*-bis-*"

# 6. Mini-Wrapper-Skills (~250 Skills) — bekommen Operation F
find . -name SKILL.md | while read f; do
  lines=$(wc -l < "$f")
  [ "$lines" -lt 45 ] && echo "$f"
done
```

**Geschätzte Größenordnung:** Summe der distinkten Skills aus den obigen Listen (mit Overlap-Bereinigung): ~1850 unique Skills, davon mindestens 1000 echte Veredelungs-Kandidaten.

---

## Anhang 2 — Was NICHT verändert werden soll

Diese Skills sind bereits auf gutem Niveau und sollen **nicht** angefasst werden:

- **`steuerrecht-anwalt-und-berater/skills/stb-dba-*` (alle Länder-DBA)** — Goldstandard, perfekt individualisiert.
- **`beamtenrecht/skills/komp-08-teil-02-amtsangemessene-alimentation` Modul-6** (Fünf-Parameter) — soll bleiben, ggf. als eigener Skill ausgelagert.
- **`selbstvertreter-amtsgericht/skills/kompendium-01-anfaenger-workflow-a-bis-fristbeginn-zustellu` Drei-Führungsstufen-Modell** — Gold, bleibt.
- **`arbeitszeugnis-analyse/skills/rote-flaggen-katalog`, `orange-flaggen-katalog`, `gruen-flaggen-katalog`** — sind echte Kataloge, bleiben (aber Description-Trigger nach Operation E aufwerten).
- **`roemisches-recht/skills/.../rom-074 bis rom-081`** (Vergleichsmodule) — didaktisches Gold, bleibt.

---

## Anhang 3 — Erwartetes Endergebnis nach allen Operationen

| Kennzahl | Heute | Ziel nach allen Operationen |
|---|---|---|
| SKILL.md gesamt | 5951 | ~3500-4000 |
| Kompendien | 4369 | ~1600-1800 (semantisch geclustert) |
| Spezialskills | 1260 | ~1700-2200 (durch Workflow-Wrapper-Individualisierung) |
| Plugins | 209 | 209 (unverändert) |
| V90-Blocks in Modulen | 841 | 0 (alle in `allgemein` zentralisiert) |
| Wrapper-Klone | ~810 | 0 |
| Slug-Länge max | 64 | ≤ 45 |
| Description-Trigger-Qualität | 4691 Boilerplate | 0 Boilerplate, alle Lebenslagen-Trigger |

Das Repo ist danach kompakter, individueller, näher an Anthropic-Niveau — aber mit der gesamten von Tom kuratierten juristischen Substanz erhalten.

---

## Schluss

Tom erwartet vergleichbare Reviews von Claude (dieses Dokument), Codex und Perplexity. Codex implementiert die Synthese.

Wenn Codex zu einer Operation Rückfragen hat: bitte vor Implementierung Pull Request mit `Draft` öffnen und einzelne Plugin-Veredelung als Beispiel pushen. Tom validiert.
