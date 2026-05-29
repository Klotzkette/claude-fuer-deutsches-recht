# Audit-Verzeichnis

Dieses Verzeichnis dokumentiert Halluzinations-Audits ueber alle Aktenzeichen
in den SKILL.md-Dateien des Repos.

## Wellen

| Welle | Datum | Umfang | Status |
|---|---|---|---|
| 1 — Stichprobe v14.2.4 | 27.05.2026 | 25 Skills aus User-Report | abgeschlossen, in v14.2.4 gefixt |
| 2 — Vollaudit | 27.05.2026 | 3228 unique AZ, 22 parallele Subagenten | abgeschlossen, Befunde in `audit_problems_2026-05-27.json` |
| 3 — Reparatur (AZ-Strip) | 29.05.2026 | 969 problematische AZ aus 88 Skills entfernt | abgeschlossen, in v24.1.0 |
| 4 — References-Konsistenz | 29.05.2026 | 17 tote Verweise, 83 verwaiste Files | abgeschlossen, Befunde in `references_audit_2026-05-29.json` |
| 5 — References-Einzelfix | 29.05.2026 | 16 verbleibende tote Verweise einzeln geprüft | abgeschlossen, 14 als falsch-positiv (ASCII-Trees, andere Auflösungspfade), 1 echter Bug gefixt, 2 als Laufzeit-Caches dokumentiert |
| 6 — UNVERIFIABLE-Online-Check | 29.05.2026 | 893 UNVERIFIABLE-AZ gegen dejure, BGH, BAG, BFH, EuGH etc. geprüft (20 parallele Batches) | abgeschlossen, Konsolidierung in `welle2_unverifiable_audit_2026-05-29.json` |

## Welle 2 — Methodik

22 parallele Subagenten haben je ~147 unique Aktenzeichen geprueft. Pro AZ:

1. `pplx search web "<court> <az>"` gegen dejure.org / openJur / bundesgerichtshof.de / curia.europa.eu
2. Vergleich des im Skill behaupteten Themas mit der echten Entscheidung
3. Klassifikation:
   - **OK**: AZ existiert und Kontext passt
   - **WRONG_TOPIC**: AZ existiert, aber Kontext beschreibt anderen Sachverhalt
   - **NOT_FOUND**: AZ findet sich nicht
   - **UNVERIFIABLE**: Quellenlage zu duenn

## Ergebnis Welle 2

- **3228** unique Aktenzeichen geprueft
- **1062** OK (32,9 %)
- **893** UNVERIFIABLE (27,7 %) — meist OLG/LG/FG ohne oeffentlichen Volltext
- **621** WRONG_TOPIC (19,2 %)
- **355** NOT_FOUND (11,0 %)
- **976 Problemfaelle** (30,2 %) sind in `audit_problems_2026-05-27.json`
  detailliert aufgelistet

## Hinweis zur Datenqualitaet

Der hohe WRONG_TOPIC-Anteil zeigt: das Aktenzeichen existiert, aber
die im Skill behauptete Aussage trifft nicht auf das tatsaechliche Urteil zu.
Typische Muster sind falsche Senate (z.B. IX ZR statt VIII ZR), falsche
Jahrgaenge oder voellig andere Themen unter identischem AZ.

Diese Faelle muessen in einer Folge-Welle (Welle 3 — Reparatur) systematisch
bereinigt werden: betroffene Skill-Stellen entweder ersatzlos streichen
oder durch verifizierte AZ ersetzen.

Die UNVERIFIABLE-Faelle sind nicht zwangslaeufig fehlerhaft; sie konnten
nur ohne juris-/Beck-Zugang nicht abschliessend gegengeprueft werden.

## Folgeschritte

1. Welle 3 — Reparatur: 976 Problemfaelle systematisch fixen – erledigt in v24.1.0 (Strip ueber `strip_az.py`)
2. Optional: 893 UNVERIFIABLE mit juris/Beck-Zugang nachpruefen
3. CI-Hook etablieren, der neue AZ-Aufnahmen gegen dejure-API gegenprueft

## Welle 3 — AZ-Strip (29.05.2026)

Alle 969 als WRONG_TOPIC oder NOT_FOUND klassifizierten Aktenzeichen wurden
aus den betroffenen SKILL.md entfernt. Strategie:

- Pro Audit-Eintrag wurde die AZ-Zeichenkette in der jeweils betroffenen
  SKILL.md gesucht und die enthaltende Markdown-Zeile/Bulletpoint geloescht.
- YAML-Frontmatter wurde nicht angetastet (Schutz gegen Header-Beschaedigung).
- Konsekutive Leerzeilen wurden kollabiert.
- Ergebnis: 175 Dateien geaendert, 392 Zeilen entfernt.
- Validatoren (`validate-plugin-structure`, `validate-yaml-frontmatter`,
  `welle5_komma_check`) anschliessend gruen.

## Welle 4 — References-Audit (29.05.2026)

Pruefung der Markdown-Verweise auf `references/`-Dateien:

- 115 References-Dateien gesamt
- 29 davon werden mindestens einmal verlinkt
- 83 sind nicht verlinkt (werden aber durch Skill-Engine via Glob geladen,
  also nicht zwingend tot)
- 17 tote Verweise: SKILL.md/README.md referenzieren Dateien, die nicht
  existieren. Beispiel: `rechtsberatungsstelle/.../SKILL.md` verwies auf
  `references/pruef-warteschlange.yaml`, faktisch heisst die Datei aber
  `review-queue.yaml` (in dieser Welle gefixt).

Vollstaendige Liste in `references_audit_2026-05-29.json`.

## Welle 5 — References-Einzelfix (29.05.2026)

Die 16 verbleibenden toten Verweise einzeln durchgegangen:

- **14 falsch-positiv:** Aufloesungspfad war anders (z. B. `mietspiegel-quellen.md`
  liegt unter `mietrecht/references/`, mein Audit-Script konnte ihn von
  `TESTBERICHT.md` aus nicht aufloesen), ASCII-Tree-Beispiele in README-Dateien,
  Pfade in generierten Skills (klagewerkstatt-<kanzlei>), `../../`-Pfade.
- **1 echter Bug gefixt:** `produktrecht/skills/produktrecht-kaltstart-interview`
  verwies auf `references/launch-pruefung-framework-de.md`; korrigiert auf
  `produktrecht/skills/launch-pruefung/references/seven-category-framework.md`.
- **2 Laufzeit-Caches dokumentiert:** `kanzlei-builder-hub` legt zur Laufzeit
  `registry-cache.json` und `surfaced.json` an; entsprechende `references/`-
  Verzeichnisse mit `README.md`-Hinweis angelegt.

## Welle 6 — UNVERIFIABLE-Online-Check (29.05.2026)

Die 893 in Welle 2 als UNVERIFIABLE klassifizierten Aktenzeichen wurden
online gegen dejure.org, BGH-Datenbank, BAG-Datenbank, BFH-Datenbank,
Curia, openJur, NRWE und Landesjustizportale geprueft. Methodik:
20 parallele Subagenten haben je ~45 AZ in einer Schnellrunde gesichtet.

Konsolidiertes Ergebnis (in `welle2_unverifiable_audit_2026-05-29.json`):

- 148 AZ klar verifiziert (vorher UNVERIFIABLE, jetzt rehabilitiert)
- 621 AZ in Schnellrunde nicht auffindbar
- 30 AZ widerspruechlich klassifiziert (in-batch)
- 94 AZ von Subagenten uebersprungen

**Strip-Strategie konservativ:** Nur AZ entfernen, die
(a) in der Schnellrunde nicht auffindbar waren und
(b) im Original-Audit klare Negativ-Marker (`nicht in dejure verifizierbar`,
`nicht in Datenbanken auffindbar`) tragen und
(c) keine positiven Marker (`AZ existiert`, `Datum plausibel`) zeigen.

Dieses Filter ergab 7 sichere Loeschkandidaten. Alle 7 waren jedoch
bereits durch Welle 3 (v24.1.0) aus den Skills verschwunden –
Welle 6 hat netto null weitere Zeilen entfernt, liefert aber eine
konsolidierte Klassifikation aller 893 ursprueglichen UNVERIFIABLE-AZ
fuer kuenftige Reparaturwellen.
