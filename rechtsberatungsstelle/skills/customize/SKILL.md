---
name: customize
description: >
  Passt das Beratungsstellenprofil (CLAUDE.md) oder einen Fachbereichsleitfaden
  (guides/<fachbereich>.md) gezielt an – ohne den vollen Cold-Start-Workflow zu
  durchlaufen. Für kleinere Aktualisierungen: neuer Fachbereich, geänderte
  Prüfungsgates, aktualisierte Kontakte, Semesterwechsel. Nur für den
  anleitenden Volljurist.
argument-hint: "[Abschnitt der CLAUDE.md oder Name des Leitfadens – z. B. 'fachbereiche', 'gates', 'asyl']"
language: de
triggers:
  - "profil anpassen"
  - "konfiguration ändern"
  - "customize"
  - "einstellungen"
  - "leitfaden aktualisieren"
---

# /customize

1. Lade `CLAUDE.md` → aktuelles Profil anzeigen.
2. Frage: Welcher Abschnitt soll geändert werden?
3. Führe die gezielte Änderung durch – kein Full-Redo.
4. Aktualisierte Datei ausgeben.

---

# Beratungsstellenprofil anpassen

## Zweck

Nach der Ersteinrichtung (`/cold-start-interview`) müssen Beratungsstellenprofile regelmäßig aktualisiert werden:
- Semesterwechsel: Neue Studierende, neuer Anleiter.
- Neuer Fachbereich hinzugefügt.
- Gesetzesänderung (z. B. neue Regelbedarfsstufen SGB II, neues BAMF-Merkblatt).
- Neue örtliche Kooperationspartner.
- Prüfungsgates angepasst (erfahrene Studierende brauchen weniger Gateways).

Dieser Skill macht gezielte Änderungen, ohne das gesamte Profil neu aufzurollen.

**Nur für den anleitenden Volljuristen.**

## Häufige Anpassungsszenarien

### 1. Semesterwechsel

> Welche Studierenden sind neu? Welche gehen? Wer übernimmt laufende Mandate?

Änderungen in `CLAUDE.md`:
- `Semester: [WS 2024/25]` → `[SS 2025]`
- Liste der aktiven Studierenden aktualisieren.
- Mandate-Übergabe: Verweis auf `/rechtsberatungsstelle:semester-handoff`.

### 2. Neuen Fachbereich hinzufügen

Fachbereich in `CLAUDE.md` unter `Fachbereiche` ergänzen. Dann sofort:
> „Soll für den neuen Bereich auch ein Leitfaden erstellt werden? → `/rechtsberatungsstelle:build-guide [fachbereich]`"

### 3. Prüfungsgates ändern

> Welche Gates sollen geändert werden? Verschärfen oder lockern?

Tabelle in `CLAUDE.md` → `Aufsichtsmodell` anpassen. Hinweis: Lockerung nur bei nachgewiesener Erfahrung der Studierenden. § 6 Abs. 2 Nr. 2 RDG verlangt tatsächliche Anleitung.

### 4. Gesetzesänderungen einpflegen

Häufige Anlässe:
- Neue Regelbedarfsstufen SGB II ab 1. Januar (jährliche Anpassung per Regelbedarfsermittlungsgesetz).
- Neues BAMF-Merkblatt oder Entscheidungspraxis zu einem Herkunftsland.
- BGH-Urteil zur Schönheitsreparatur / Mieterhöhung.
- Änderungen im AsylG / AufenthG.

Pflegen Sie in `CLAUDE.md` → `Wichtige Normen` die relevante Änderung ein. Datum der Änderung festhalten.

### 5. Örtliche Kontakte aktualisieren

Jobcenter, Ausländerbehörde, BAMF-Außenstelle, Gericht, Dolmetscherdienste – Telefon, Zuständigkeit, Sprechzeiten.

### 6. Pädagogikhaltung ändern

Für ein bestimmtes Semester oder einen bestimmten Studierenden die Default-Haltung anpassen. Z. B.: „Für dieses Semester soll der Skill primär im Modus ‚Anleiten' arbeiten, da alle Studierenden im ersten Klinik-Semester sind."

## Workflow

### Schritt 1: Aktuelles Profil anzeigen

Gesamte `CLAUDE.md` ausgeben als Referenz.

### Schritt 2: Gezielter Abschnitt

Welcher Abschnitt? Optionen:
- `[A]` Beratungsstellentyp und Rechtsgrundlage
- `[B]` Fachbereiche
- `[C]` Aufsichtsmodell / Prüfungsgates
- `[D]` Pädagogikhaltung
- `[E]` Verschwiegenheitsorganisation
- `[F]` Örtliche Besonderheiten / Kontakte
- `[G]` Wichtige Normen (Gesetzesänderung)
- `[H]` Semester / Studierende
- `[L]` Fachbereichsleitfaden `guides/<name>.md`

### Schritt 3: Änderung durchführen

Nur den angegebenen Abschnitt bearbeiten. Alle übrigen Abschnitte unverändert lassen.

### Schritt 4: Änderungshistorie

Am Ende der `CLAUDE.md` einen Änderungseintrag hinzufügen:
```
## Änderungshistorie
- [Datum] Abschnitt [B] geändert: SGB IX / § 76b hinzugefügt. [Kürzel Anleiter]
- [Datum] Abschnitt [H] geändert: Semesterwechsel SS 2025. [Kürzel Anleiter]
```

## Ausgabeformat

Vollständige, aktualisierte `CLAUDE.md` (oder `guides/<name>.md`). Kein `[KI-GESTÜTZTER ENTWURF]`-Vermerk.

## Risiken / typische Fehler

- **Versehentliches Löschen:** Beim Anpassen einzelner Abschnitte nie den Rest des Profils löschen. Immer vollständige Datei ausgeben, nicht nur den geänderten Abschnitt.
- **Gesetzesänderungen nicht eingepflegt:** Veraltertes Profil führt dazu, dass der Skill mit überholten Normen arbeitet (z. B. falsche Regelbedarfsstufen, falsche Fristen).
- **Mandate ohne Übergabe:** Beim Semesterwechsel sicherstellen, dass alle laufenden Mandate über `/rechtsberatungsstelle:semester-handoff` übergeben werden, bevor das Profil auf das neue Semester umgestellt wird.
