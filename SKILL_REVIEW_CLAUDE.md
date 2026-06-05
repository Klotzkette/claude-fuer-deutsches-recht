# Skill-Review claude-fuer-deutsches-recht
## Begutachtung der konsolidierten Skills nach Kompendien-Sortierung

Verfasser: Claude (Opus 4.7 / 1M context)
Stand: 2026-06-05
Repository: `Klotzkette/claude-fuer-deutsches-recht`
Branch: `claude/review-german-law-skills-9LH3E`
Aufgabe: Einer von drei parallelen Reviews (Claude / Codex / Perplexity), die du danach gegeneinander vergleichst und Codex zur Implementierung gibst.

Diese Datei ist bewusst lang. Sie ist als Lesedokument für dich gedacht, nicht als Output an einen Mandanten.

---

## 0. Worauf ich geschaut habe (Methode)

Ich konnte nicht alle 5629 SKILL.md einzeln lesen. Was ich gemacht habe:

- Repo-weite Strukturzählungen (`Bash`, `Grep`).
- Stichproben aus elf repräsentativen Plugins quer durch die Cluster (Verbraucher-Recht, Beamtenrecht, Selbstvertreter, Steuerrecht, Römisches Recht, ALR, Arbeitszeugnis, DBA, Insolvenzrecht, Kartellrecht, Migrationsrecht).
- Volltextlesung von vier Kompendien (selbstvertreter-sozialgericht/k08, beamtenrecht/k06, selbstvertreter-amtsgericht/k01, roemisches-recht/k11).
- Vergleich zweier identisch wirkender Mini-Skills (`red-team-beamtenrecht` ↔ `output-waehlen-memo-widerspruch-eilantrag`) zur Quantifizierung der Restduplikate.
- Quervergleich mit Anthropic-Skill-Niveau (pdf, docx, xlsx, skill-creator).

Ich nenne unten an mehreren Stellen `Plugin/SKILL-Pfad` als konkretes Beleg-Sample, damit du oder Codex direkt nachgucken können.

---

## 1. Gesamtbild auf einen Blick

| Kennzahl | Wert |
|---|---|
| SKILL.md gesamt (in Repo) | 5951 |
| Davon `kompendium-*` / `komp-*` (gebündelte Arbeitsbereiche) | 4369 |
| Nicht-Kompendien (Einzelskills, allgemein, red-team etc.) | 1582 |
| Plugins mit `skills/`-Verzeichnis | ~209 |
| Plugins mit `skills/allgemein/` | 93 |
| Skills mit gleicher 6-zeiliger "V90 Fachkern"-Box | 855 |
| Skills mit identischem BAG-Anker-Triplet (`23.10.2025 8 AZR 300/24` + 2 weitere) | 102 |
| Skills mit identischem BSG-Anker-Triplet (`05.11.2024 B 12 BA 3/23 R` + 2 weitere) | 82 |
| Skills mit identischer "Status und Rechtsquelle"-Prüfprogramm-Liste | 37 |
| Skills mit identischer 4-Punkt-`Arbeitsregel` der Kompendien-Schablone | 4369 |
| Slugs mit ≥ 60 Zeichen | 58 |

**Kernbefund:** Die Codex-Konsolidierung hat das schlimmste Problem (19 162 generische Wrapper) erfolgreich gelöst. Die Kompendien-Schablone als solche ist tragfähig. **Aber:** in der Schablone steckt jetzt selbst Boilerplate-Duplikat (V90-Block, BAG/BSG-Triplet, 4-Punkt-Arbeitsregel), und der Bündelungsalgorithmus ist alphabetisch, nicht semantisch — das produziert disparate Mischungen.

Das Repo ist heute **besser, aber noch nicht auf Anthropic-Niveau**. Anthropic-Skills haben drei Eigenschaften, die wir noch nicht durchgängig erreichen:

1. **Eine klare, einzelne Funktion** (`pdf` kann genau PDFs lesen/schreiben — nichts anderes).
2. **Eindeutiger Trigger im `description`-Feld** (das Modell weiß sofort: wann lade ich das, wann nicht).
3. **Kein internes Boilerplate.** Anthropic-Skills haben keinen "Fachkern-Block", keine "Quellenhygiene-Box", keine "Red-Team-Sieben-Fallen-Liste" — sondern den eigentlichen Inhalt und Beispiele.

Wir machen das umgekehrt: viele Skills haben eine fast leere `## Aufgabe`, dann einen großen V90-Block, dann eine generische Prüfschablone. Das ist die historische Erblast aus den 19 162 Wrappern, sie steckt jetzt nur an anderer Stelle.

---

## 2. Was die Kompendien-Konsolidierung sehr gut gemacht hat

Damit das hier nicht nur Kritik ist — die echten Stärken:

### 2.1 Massive Reduktion ohne Substanzverlust
Aus ~19 162 SKILL.md sind 5951 geworden. Der wirklich wertvolle Inhalt (z. B. die BVerfG-Fünf-Parameter-Alimentation in `beamtenrecht/kompendium-06`, die `condictio`-Pendants in `roemisches-recht/kompendium-11`, die § 86b-SGG-Schriftsatzvorlage in `selbstvertreter-sozialgericht/kompendium-08`) ist erhalten geblieben. Das war die Hauptsorge, und sie ist nicht eingetreten.

### 2.2 Tatsächlich starke Inhalte
Einzelne Kompendien-Module sind genuin gut:

- `beamtenrecht/skills/kompendium-06-besold-neu-003-besol-bis-besold-neu-009-minde` → Modul 6 (Amtsangemessene Alimentation): Klare Fünf-Parameter-Pruefung erster Stufe, Trennung erste/zweite Stufe, BVerfGE-Anker mit Band+Randnummer. Das ist **Fachanwalts-Niveau**, nicht Lehrbuch.
- `selbstvertreter-sozialgericht/skills/kompendium-08-.../eilantrag-86b-sgg-grundlagen` → Vollständiger SG-Eilantrag mit eidesstattlicher Versicherung, Antragsmuster, Anlagenliste. Das spart einer/m Bürger:in zwei Stunden Recherche.
- `roemisches-recht/skills/kompendium-11-.../rom-074-bereicherungsrecht-vergleich` → Saubere Zuordnung Digestenstellen → BGB §§ 812-822, einschließlich Einheits- vs. Trennungslehre. Universitätsniveau.
- `selbstvertreter-amtsgericht/skills/kompendium-01-anfaenger-workflow-a-bis-fristbeginn-zustellu` → Sehr starkes Triage-Schema in Sie-Form mit drei Führungsstufen (sehr geführt / normal / Kurzmodus). Das ist genau die richtige Idee für einen Allgemein-Skill.

### 2.3 Einheitliche Quellenhygiene
Der überall verbaute Block ("Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen") setzt eine sehr saubere Regel um. Das ist nicht Anthropic-Stil, aber für deutsche Kanzleien richtig. Sollte bleiben — nur nicht 855-mal im selben Wortlaut.

### 2.4 Frontmatter-Disziplin
Nur `name` + `description`. Keine wilden `triggers`, `language`, `rechtsgebiet`. Das ist sauber, validatorfest, und macht jedes Skill für Claude ladbar.

---

## 3. Was noch nicht stimmt — die fünf Hauptprobleme

### Problem 1: Alphabetische Bündelung produziert disparate Kompendien

**Beleg:** `selbstvertreter-sozialgericht/skills/kompendium-08-buergergeld-ueberbru-bis-eilantrag-86b-sgg-gr/` bündelt fünf Module:

| Modul | Thema |
|---|---|
| `buergergeld-ueberbrueckungsgeld` | SGB II Sondervorschrift Haftentlassene |
| `dokumenten-erzeugung-pdf-laien-sozialgericht` | IT-Anleitung: Word → PDF, Smartphone-Scan |
| `dolmetscher-beim-sozialgericht-laien` | § 185 GVG Sprachmittlung |
| `dsgvo-art-15-auskunft-sozialakte` | Datenschutzrechtlicher Auskunftsanspruch |
| `eilantrag-86b-sgg-grundlagen` | SGG-Eilrechtsschutz |

Diese fünf haben gemeinsam: **nichts.** Außer dass sie alphabetisch in `B-D-D-D-E` fallen. Ein:e Bürger:in mit Eilantrag-Anliegen bekommt 600 Zeilen geladen, davon 400 zu PDF-Anleitung und DSGVO. Das ist genau das Disparat-Problem, das du befürchtet hast.

**Weiter:** `kompendium-04-akteneinsicht-25-sgb-bis-anwaltskosten-bei-er` mischt Akteneinsicht + Amtsermittlung + Anfechtungsklage + Anlagen-Bezeichnen + Anwaltskosten — wieder fünf "A"s, keine Sachlogik.

**Beleg #3:** `beamtenrecht/skills/kompendium-06-besold-neu-003-besol-bis-besold-neu-009-minde` bündelt Eingruppierung + Stufenfestsetzung + Auslandszuschlag + Erschwerniszulagen + Mehrarbeit + Amtsangemessene Alimentation + Mindestabstandsgebot. Hier ist die Kohärenz besser (alles Besoldungsrecht), aber die juristische Tiefe schwankt extrem: Module 1-7 sind 20-30 Zeilen Stichworte, Modul 8 (Alimentation) ist 50 Zeilen ausgearbeitetes Fachwissen. Das ist visuell, was man "Klumpenbildung" nennt.

**Empfehlung für Codex:**
- Re-Bündelung **nach Sachzusammenhang, nicht nach Alphabet**.
- In selbstvertreter-sozialgericht z. B.: ein Kompendium "Eilrechtsschutz" (§ 86b SGG + Bürgergeld-eA + Krankenkasse-eA + Pflegekasse-eA), ein eigenes "IT-Hilfsmittel" (PDF + Smartphone + ELSTER + MJP), ein eigenes "Sprache und Zugänglichkeit" (Dolmetscher + einfache Sprache + Schriftgrößen-Tipps), ein eigenes "Daten-Auskunft" (DSGVO + SGB X § 25 + Beschwerde Datenschutzaufsicht).
- Naming-Konvention vorgeben: `kompendium-<plugin-kurz>-<thema-kurz>` statt `kompendium-NN-<erstesmodul>-bis-<letztesmodul>`. Die heutige Naming-Konvention macht es buchstäblich unmöglich, das richtige Kompendium zu finden.

### Problem 2: Der "V90 Fachkern"-Block ist 855-mal dasselbe

855 Skills enthalten denselben sechszeiligen Block mit `Problemfokus`/`Normenradar`/`Verifizierte Anker`/`Arbeitsmodus`/`Outputpflicht`/`Fehlerbremse`. Beispielsweise:

- 102 Skills nennen identisch `BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit)` + zwei weitere BAG-Az.
- 82 Skills nennen identisch `BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten)` + zwei weitere BSG-Az.
- In `selbstvertreter-sozialgericht/kompendium-08` taucht derselbe Block fünfmal hintereinander auf (einmal pro Modul) — das sind allein in einem File 30 redundante Zeilen.

**Was dabei wirklich passiert:** Ein:e Nutzer:in lädt das Skill, Claude bekommt seitenweise identischen Boilerplate-Text in den Kontext, der **für die konkrete Fachfrage nichts beiträgt**. Bei `buergergeld-ueberbrueckungsgeld` ist die "BAG-Entgeltgleichheit"-Verweis schlicht falsch verortet — das ist Arbeitsrecht, nicht SGB II.

**Empfehlung für Codex:**
- V90-Block pro Plugin **einmal** in `skills/allgemein/SKILL.md` schreiben.
- Aus jedem Modul rausnehmen.
- Wenn ein Modul einen eigenen Norm-/Anker-Block braucht (z. B. Eilantrag § 86b SGG hat andere Anker als Pflegegrad MDK), dann **modulspezifisch und kurz** — drei Zeilen, nicht sechs Blockzitate aus Tarifgleichheits-Rechtsprechung.
- Konsequenz: ~5000 Skill-Zeilen weniger Boilerplate, schärferer Fokus.

### Problem 3: 27 Skills enden mit demselben generischen Tagline

```
"mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis"
```

Das ist nicht-aussagekräftiges Marketing-Geräusch. In `beamtenrecht/kompendium-06/Modul 1` z. B.: *"Besoldungsgruppe Eingruppierung Amt und Funktion mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis."* — Das sagt einem Modell nichts darüber, **wann** dieses Modul vor einem anderen gewählt werden soll.

**Anthropic-Pattern:** `description` ist der wichtigste Trigger. Es muss eine **konkrete Lebenslage** nennen, nicht den Methodenstil.

**Empfehlung:**
- Alle 27 betroffenen Skills: Tagline streichen, ersetzen durch konkrete Tatbestandsbeschreibung im Stil "Wenn der Bescheid X enthält und der Mandant Y will, …".

### Problem 4: Restwrapper-Skills mit fast identischem Body

**Beleg:** `beamtenrecht/skills/red-team-beamtenrecht/SKILL.md` (38 Zeilen) und `beamtenrecht/skills/output-waehlen-memo-widerspruch-eilantrag/SKILL.md` (38 Zeilen) haben **denselben Prüfprogramm-Block** ("Status und Rechtsquelle / Eingriff und Ziel / Materielle Prüfung / Verfahren / Output"), **dieselben Pflichtfragen** ("Welcher Status liegt vor: Beamter, Richter, Bewerber, …"), **dieselbe Ausgabeformatliste** ("Kurzantwort in drei Sätzen / Checkliste …"). Nur `## Aufgabe` und Frontmatter unterscheiden sich.

In `beamtenrecht` allein finden sich **37 Skills**, die diese identische "Status und Rechtsquelle"-Liste enthalten.

**Empfehlung:**
- Diese Mini-Skills (`red-team-*`, `output-waehlen-*`, `quellenhygiene-*`, `versorgungsakte-dokumentenintake-*`, `aktenstruktur-und-dokumentenintake`) sind funktional **derselbe Skill**: "Beamtenrecht-Vorbereitungs-Checkliste". Auf einen reduzieren, mit klarer Spezialisierung pro `description` (z. B. "Red-Team" = nachträgliche Kritik vs. "Aktenintake" = Vorbereitung).
- Oder: alle vier ins `skills/allgemein/SKILL.md` verschmelzen und einzeln löschen.

### Problem 5: 58 Slugs an der 60-Zeichen-Grenze, einige zwingen zu Abkürzungen

Beispiele:
- `kompendium-08-buergergeld-ueberbru-bis-eilantrag-86b-sgg-gr` → "ueberbru" und "sgg-gr" sind ASCII-Trümmer, weil die 64-Zeichen-Grenze zwingt.
- `wirtschaftspruefer-bestaetigungsvermerk-risikofall-kaltstart-u` → letzter Buchstabe weg.
- `kv-001-kaltstart-krankenversicherung-bescheid-rechnung-und-frist` (64 Zeichen, am Limit).

**Empfehlung:**
- Naming-Konvention wechseln auf `<plugin-prefix>-<thema-präzise>` mit präzisem statt verkettetem Namen.
- Z. B. `selbstvertreter-sozialgericht/skills/eilantrag-86b-sgg` statt `kompendium-08-buergergeld-ueberbru-bis-eilantrag-86b-sgg-gr`.
- Maximallänge selbst auferlegt: 45 Zeichen. Lässt Luft für Suffixe.

---

## 4. Plugin-für-Plugin: konkrete Befunde aus den Stichproben

### 4.1 `selbstvertreter-sozialgericht` (27 Skills, davon 26 Kompendien)
**Plus:** Allgemein-Skill ist hervorragend (V90-Stummer-Upload-Logik, einfache Sprache, drei Führungsstufen). Eilantrag-Modul professionell. Bürgergeld-Überbrückungsgeld nach Haftentlassung — fachlich solide.

**Minus:**
- Alphabetische Kompendienbildung verbindet IT-Anleitung (PDF) mit Sozialrechtsgrundlagen (§ 86b SGG).
- Jedes Modul wiederholt den BSG-Anker (Lehrende/Pilot/GmbH-GF), obwohl die Module Pflegegrad oder Bürgergeld betreffen.
- "Dolmetscher beim SG" und "Einfache Sprache Tipps" wären besser zusammengebündelt als jedes für sich.

**Was Codex tun sollte:**
1. Themen-Cluster bauen: Eilrechtsschutz / Bescheidlogik / Pflegegrad / Bürgergeld / Rente / Krankenkasse / Verfahrensformalitäten / IT-Hilfsmittel / Zugänglichkeit.
2. Pro Cluster ein Kompendium, ~5-7 Module.
3. V90-Block aus den Modulen rausstreichen, nur im Allgemein-Skill belassen.
4. Bei jedem Bürgergeld-Modul stattdessen einen Bürgergeld-spezifischen Norm-Anker (§§ 7, 19, 22 SGB II, § 41 SGB II) statt der falsch verorteten BAG-Lehrender-Az.

### 4.2 `beamtenrecht` (45 Skills, davon 22 Kompendien)
**Plus:** Modul "Amtsangemessene Alimentation Fünf Parameter" ist **das beste Modul im gesamten Repo, das ich gesehen habe**. BVerfGE-Band+Randnummer-Zitate, saubere erste/zweite Stufe-Trennung, ausdrückliche Klarstellung "Privatwirtschaftsvergleich ist NICHT Parameter erster Stufe". Das ist Pflichtlektüre.

**Minus:**
- 37 von 45 Skills haben identische "Status und Rechtsquelle"-Prüfprogramm-Boilerplate.
- Vier Mini-Skills (`red-team-beamtenrecht`, `output-waehlen-memo-widerspruch-eilantrag`, `quellenhygiene-beamtenrecht-fundstellen-red-team`, `versorgungsakte-dokumentenintake-und-berechnung`) wiederholen sich semantisch.
- Module "Besold-Neu-003 Eingruppierung" usw. sind teils sehr knapp, manche unter 30 Zeilen.

**Was Codex tun sollte:**
1. Die vier Mini-Skills auf zwei oder einen einzigen reduzieren.
2. Das Alimentations-Modul aus dem Kompendium-06-Cluster rausziehen, **eigener Skill** `beamtenrecht/skills/alimentation-fuenf-parameter`. Das verdient als Solo-Skill aufzutauchen, nicht als Modul Nr. 6 von 7.
3. Restliche Besoldungs-Module dünner schreiben (Stichworte) und in zwei thematische Cluster verteilen (Grundbesoldung / Zulagen+Auslandsdienst).

### 4.3 `roemisches-recht` (27 Skills, davon 22 Kompendien)
**Plus:** Die Vergleichs-Module (röm. Institut ↔ BGB) sind didaktisch sauber. Digesten-Zitate korrekt formatiert (D. 12.6.1 etc.).

**Minus:**
- Kompendienbildung wieder alphabetisch nach `rom-NNN`-Nummer, was die historische Reihenfolge unterbricht (Kompendium 1 hat `rom-047`, `rom-133`, `rom-153` — bunt durcheinander).
- "rom-neu"-Module sind redundant zu den älteren "rom"-Modulen (z. B. `rom-neu-005-zwoelftafelg` neben `rom-102-zwoelftafelg`).
- Allgemein-Skill habe ich nicht detailliert gelesen, aber bei 27 Skills + Kompendien-Pattern droht dasselbe V90-Doppelproblem.

**Was Codex tun sollte:**
1. `rom`- und `rom-neu`-Module zusammenführen, Duplikate (Zwölftafelgesetz, Bereicherungsrecht) auf je ein Modul reduzieren.
2. Re-Bündelung **chronologisch oder systematisch** (Personenrecht / Sachenrecht / Schuldrecht / Erbrecht / Prozessrecht / Rezeption), nicht alphabetisch nach rom-NNN.
3. Die "Vergleich"-Module (rom-074 bis rom-080) sind didaktisch das Wertvollste — bündeln und prominenter machen.

### 4.4 `preussisches-allgemeines-landrecht-pralr` (28 Skills, davon 19 Kompendien)
**Plus:** Sehr spezifisches Thema, klar abgegrenzt, gute Stoffsammlung.

**Minus:**
- `pralr-spez-*`- vs. `pralr-NNN-*` vs. `pralr-neu-NNN-*` — drei parallele Naming-Schemata in einem Plugin. Das deutet auf historisch gewachsene, nicht final aufgeräumte Inkonsistenz.
- Beispiel: `kompendium-12-pralr-050-pralr-in-a-bis-pralr-neu-004-erster` mischt alte und neue Nummerierung.

**Was Codex tun sollte:**
1. Eine einzige Nummerierung erzwingen (pralr-NNN), neu durchnummerieren, Duplikate löschen.
2. `pralr-spez-*` (Spezialthemen wie Gesinderecht, Sklaverei) als eigene Sammlung im Kompendium "Spezialinstitute".

### 4.5 `steuerrecht-anwalt-und-berater` (91 Skills, davon nur 25 Kompendien — 63 spezifische)
**Plus:** Hier ist der Anteil **substantieller Einzelskills hoch**. Insbesondere die DBA-Skills (`stb-dba-frankreich-1959`, `stb-dba-grenzgaenger-schweiz-60-tage-rueckkehr` etc.) sind echte Fachanwalt-Tools — pro Land ein Skill ist genau richtig.

**Minus:**
- 25 Kompendien stehen neben 63 Spezialskills — die Kompendien wirken hier wie ein Fremdkörper. Wenn `stb-dba-belgien` ein Einzelskill bleibt, warum dann `kompendium-15` mit "stb-lohn-abfindungen bis stb-lohn-jobticket"?
- Ungleichgewicht zwischen Bündelungsgrad in DBA (sehr granular, ein Land = ein Skill) und Lohnsteuer (gepoolt in Kompendien).

**Was Codex tun sollte:**
1. Lohnsteuer-Kompendien aufbrechen — Abfindung, Jobticket, Kurzarbeit, Krankheit verdienen je einen eigenen Skill, weil sie distinkte Tatbestände sind.
2. DBA-Skills so lassen wie sie sind, das ist Best Practice.
3. Allgemein-Skill `anw-kaltstart-interview` ist solide; die anderen drei kaltstart-Skills (anw-grest-kaltstart-asset-share-deal, anw-grundsteuer-kaltstart-bescheidkette) sind richtig granular.

### 4.6 `arbeitszeugnis-analyse` (50 Skills, **0 Kompendien**)
**Plus:** Hier ist das einzige Plugin im Repo, in dem Codex die Kompendien-Welle nicht angewendet hat. Ergebnis: 50 saubere, fokussierte Einzelskills. `rote-flaggen-katalog`, `orange-flaggen-katalog`, `gruen-flaggen-katalog`, `negative-codeworte-katalog` — jedes ist ein eigener Mini-Katalog mit klarer Funktion.

**Minus:**
- Trotzdem zu viele Skills, weil das Plugin **um vier Achsen oversliced**: Farbampel (rot/orange/grün) × Form (Katalog/Workflow/Spezial) × Phase (Kaltstart/Mandatsannahme/Berichtigung) × Spezial-Topik (Schlussformel/Steigerungsadverbien/Zufriedenheitsformel).
- Beispiel: `spezial-codeworte-compliance-dokumentation-und-akte` vs. `geheimcode-katalog` vs. `negative-codeworte-katalog` — drei Skills für eine Sache (Codes erkennen).
- Trotz fehlender Kompendien: identischer V90-Fachkern-Block taucht hier auch in jedem Skill auf.

**Was Codex tun sollte:**
1. Konsolidieren auf ~25 Skills max: 4 Flag-Kataloge (rot/orange/grün + Sonderzeichen) + 1 Negationskatalog + 6 Workflow-Skills (Kaltstart, Mandatsannahme, Berichtigung, Klage, Vergleich, Verhandlung) + 5 Spezialanalyse-Skills (Schlussformel, Notenformel, Strukturanalyse, Branche, Führungsposition) + 5 Output-Skills (Mandantenbericht, Tabellenausgabe, Drohbrief, Klageschrift, Vergleichsentwurf) + 3 Beweis-/Recht-Skills.
2. Diese **bewusst keine Kompendien-Pattern** verwenden, sondern Anthropic-Style: ein Skill, eine Funktion, einen Trigger.
3. Das Plugin als Referenz nutzen, wie das Repo aussehen sollte.

### 4.7 `selbstvertreter-amtsgericht` (30 Skills, davon 29 Kompendien — 96 %)
**Plus:** Allgemein-Skill `kompendium-01-anfaenger-workflow-a-bis-fristbeginn-zustellu` enthält das ausgezeichnete Drei-Führungsstufen-Modell. Triage-Tabelle (Rolle/Verfahrensstand/Frist/Streitwert/Gericht/Unterlagen/Ziel) ist sehr brauchbar.

**Minus:**
- 96 % Kompendien-Quote ist extrem. Quasi keine Einzelskills mehr.
- Innerhalb der Kompendien dieselben Boilerplate-Probleme wie in `selbstvertreter-sozialgericht`.

**Was Codex tun sollte:**
1. Aus dem Allgemein-Skill ggf. drei eigenständige Triage-Skills extrahieren (Klage-Triage, Beklagten-Triage, Vollstreckungs-Triage), falls die Drei-Führungsstufen-Logik in einer einzigen Datei zu viel wird.

### 4.8 Plugins, in die ich nicht im Detail geschaut habe, aber aus Strukturzahlen ableite

Bei den folgenden Plugins liegt die Kompendien-Quote **über 85 %**:
- `verbraucherschutzrecht-pruefer` (93 %)
- `haushaltsrecht-bho` (93 %)
- `telekommunikationsrecht` (90 %)
- `private-equity-praxis` (90 %)
- `insiderrecht-compliance` (90 %)
- `commercial-courts-deutschland` (90 %)
- `bundesnetzagentur-verfahren` (28/32 = 88 %)

Hier ist die Vermutung: **gleiche Probleme wie bei `selbstvertreter-*`** — alphabetische Bündelung, V90-Wiederholung, generische Taglines. Codex sollte diese Plugins als nächste Welle anpacken.

Bei den großen Fachanwalts-Plugins (jeweils 45-58 Skills, davon ~22 Kompendien, also ~50 % Kompendien-Quote) ist die Mischung ähnlich wie bei `beamtenrecht`/`steuerrecht`: gute Spezialskills nebenher, aber Kompendien-Boilerplate raubt Kontext.

---

## 5. Anthropic-Niveau: was die uns als Maßstab vorgeben

Du hattest dich erinnert, dass wir uns Anthropic-Skills angeschaut hatten. Wesentliche Eigenschaften:

| Anthropic-Skill | Wir |
|---|---|
| **Eine Funktion pro Skill.** `pdf` macht PDF, sonst nichts. | Manche Kompendien decken 5+ disparate Themen ab. |
| **Description ist Trigger.** "Use when the user wants to read or write a PDF." | Description sagt oft methodisches Geräusch ("mit geführtem Workflow, Normencheck…"). |
| **Kein Boilerplate im Body.** Direkt Schritt 1, 2, 3. | Jeder Skill hat V90-Block, Quellenhygiene-Box, "Arbeitsregel"-Liste. |
| **Beispiele zuerst.** Was schreibt der User, was tut der Skill, was kommt zurück. | Beispiele oft am Ende oder fehlen. |
| **Klare Voraussetzungen.** "Requires X tool / Y permission." | Wir haben keine Tool-Voraussetzungen, weil die Skills tool-agnostisch sind, aber sagen das nicht offen. |
| **Kompakt.** Meist 80-200 Zeilen. | Unsere Kompendien sind 400-800 Zeilen. |

**Daraus folgt — drei Schraubregeln, die ich Codex an die Hand geben würde:**

1. **Skill = ein Tatbestand + ein Output.** Wenn ein Skill mehrere Tatbestände abdeckt, prüfen, ob Aufspaltung möglich ist.
2. **V90-Block kommt ins Allgemein-Skill, sonst nirgends.** Spezialskills haben einen **eigenen, kurzen, modulspezifischen** Normradar (3-5 Zeilen, nicht 6 generische).
3. **Description = Wann lade ich das? Nicht: Was kann das?** Anthropic-Modell entscheidet anhand der `description`, ob ein Skill geladen wird. Generische Description = Skill wird unter-/übertrieben oft geladen.

---

## 6. Konkrete Streich- und Verschmelz-Liste für Codex

Wenn ich Codex am Schluss zwei Stunden geben würde, würde ich ihn folgende fünf Operationen tun lassen:

### Operation A: Boilerplate-Diet (geschätzte 5000 Zeilen weniger)
```
Für jedes SKILL.md in skills/kompendium-*/ und skills/komp-*/:
  - Wenn V90-Block vorhanden UND identisch mit dem in skills/allgemein/SKILL.md:
    → Block entfernen, ggf. durch 3-zeiligen modulspezifischen Normradar ersetzen.
  - Wenn "Qualitäts-Hardening"-Block am Ende vorhanden UND identisch mit anderen Skills:
    → Block entfernen, einmalig in skills/allgemein/SKILL.md belassen.
```

### Operation B: Kompendien-Resort nach Sachzusammenhang
```
Pro Plugin:
  - Aktuelle Kompendien-Module extrahieren.
  - In thematische Cluster zu je 4-6 Modulen einsortieren (statt alphabetisch).
  - Neue Kompendien-Slugs nach Pattern <plugin>-<cluster-name> (z. B. selbstvertreter-sozialgericht-eilrechtsschutz).
```

### Operation C: Mini-Wrapper-Verschmelzung
```
Finde alle SKILL.md kleiner als 50 Zeilen ohne substantiellen Inhalt:
  - red-team-* / output-waehlen-* / quellenhygiene-* / aktenstruktur-* / *-dokumentenintake
  - Verschmelze zu einem Skill pro Plugin: skills/red-team-und-quality/SKILL.md
  - Oder: in skills/allgemein/SKILL.md aufnehmen und Einzeldateien löschen.
```

### Operation D: Slugnamen kürzen
```
Für alle Skill-Slugs > 50 Zeichen:
  - Neuer Slug nach Pattern <thema-konkret> ohne "kompendium-NN-X-bis-Y"-Brücke.
  - Lange Beschreibung statt verstümmelter Slug.
```

### Operation E: Description-Trigger einschärfen
```
Für jedes SKILL.md:
  - Description liest sich wie "Wenn der User X braucht, dann …", nicht wie "[Plugin]: X mit geführtem Workflow, Normencheck, …".
  - Tagline "mit geführtem Workflow, …" streichen.
  - Kommata in Zahlen nicht erlaubt (CLAUDE.md sagt das schon).
```

---

## 7. Wo ich unsicher bin (offene Fragen für deinen Vergleich mit Codex / Perplexity)

1. **Ist die Kompendien-Schablone überhaupt das richtige Pattern, oder sollten wir komplett zurück zu Einzelskills?**
   - Pro Schablone: Reduziert Frontmatter-Overhead, gruppiert verwandte Themen, ein File pro Cluster.
   - Contra Schablone: Lädt für eine konkrete Frage 500 Zeilen, davon 400 irrelevant. Anthropic macht das nicht.
   - Mein Vorschlag: **Beibehalten, aber chirurgischer einsetzen** — nicht 96 % Kompendien-Quote wie bei `selbstvertreter-amtsgericht`, sondern ~40 %. Restliche 60 % sollten Einzelskills sein.

2. **Sollen wir den V90-Block überhaupt behalten?** Er steht nirgends in der CLAUDE.md, wirkt aber wie Codex-erfundene Konvention.
   - Pro: Einheitliche Quellenhygiene-Checkliste pro Plugin.
   - Contra: 855-fach redundant.
   - Mein Vorschlag: V90 als **eigener kleiner Skill** `skills/quellenhygiene-und-anker/SKILL.md` pro Plugin, einmal. Verweis in `skills/allgemein/SKILL.md`, nicht in jedes Modul.

3. **Wie aggressiv reduzieren?** Wenn Codex/Perplexity sagen "auf 3000 Skills runter", würde ich zustimmen. Wenn sie "auf 2000" sagen, wird's eng.

4. **Was tun mit den 58 zu langen Slugs?** Brechen wir die naming-Konvention auf oder zwingen Code zur Verkürzung?

---

## 8. Mein Ein-Satz-Urteil

Das Repo ist nach der Codex-Konsolidierung **fachlich brauchbar, aber technisch noch zu generisch** — die Kompendien-Schablone selbst ist Boilerplate geworden, die Bündelung ist alphabetisch statt semantisch, und Anthropic-Niveau (eine Funktion = ein Skill mit klarem Trigger) erreichen wir noch nicht. Mit den fünf Operationen oben kommen wir auf ~3000-3500 wirklich gut sortierte Skills, von denen jeder einzeln ladbar ist und genau eine Frage beantwortet.

---

## Anhang: Daten zu den Stichproben

### Gelesene Files
- `selbstvertreter-sozialgericht/skills/kompendium-08-buergergeld-ueberbru-bis-eilantrag-86b-sgg-gr/SKILL.md` (589 Zeilen)
- `beamtenrecht/skills/kompendium-06-besold-neu-003-besol-bis-besold-neu-009-minde/SKILL.md` (384 Zeilen)
- `selbstvertreter-amtsgericht/skills/kompendium-01-anfaenger-workflow-a-bis-fristbeginn-zustellu/SKILL.md` (gelesen Anfang)
- `roemisches-recht/skills/kompendium-11-rom-074-bereicherung-bis-rom-081-lateinische/SKILL.md` (Anfang)
- `arbeitszeugnis-analyse/skills/rote-flaggen-katalog/SKILL.md` (65 Zeilen)
- `steuerrecht-anwalt-und-berater/skills/anw-kaltstart-interview/SKILL.md` (Anfang)
- `selbstvertreter-sozialgericht/skills/allgemein/SKILL.md` (Anfang)
- `beamtenrecht/skills/red-team-beamtenrecht/SKILL.md` (38 Zeilen)
- `beamtenrecht/skills/output-waehlen-memo-widerspruch-eilantrag/SKILL.md` (38 Zeilen)

### Plugins mit hoher Kompendien-Quote (>85 %)
- `selbstvertreter-amtsgericht` 96 %
- `verbraucherschutzrecht-pruefer` 93 %
- `haushaltsrecht-bho` 93 %
- `telekommunikationsrecht` 90 %
- `private-equity-praxis` 90 %
- `insiderrecht-compliance` 90 %
- `commercial-courts-deutschland` 90 %
- `bundesnetzagentur-verfahren` 88 %

### Plugins mit niedriger Kompendien-Quote (Vergleichsfälle)
- `arbeitszeugnis-analyse` 0 % (50 Skills, alle Einzelskills)
- `steuerrecht-anwalt-und-berater` 27 % (91 Skills, davon 25 Kompendien)
- `ki-richtlinie-kanzleien` 33 % (48 Skills, davon 16 Kompendien)
