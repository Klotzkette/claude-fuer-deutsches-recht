---
name: fehlzeit-erfassen
description: Neue Abwesenheit oder neuen Urlaubseintrag im Register anlegen – mit allen für die Fristenberechnung nach BUrlG, EFZG, MuSchG und BEEG notwendigen Informationen. Startet die Überwachung von Fristen ab dem ersten Tag.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - fehlzeit eintragen
  - urlaub eintragen
  - log fehlzeit
  - fehlzeit-erfassen
  - abwesenheit melden
argument-hint: "[Abwesenheitstyp, Mitarbeiter-ID, Bundesland, Startdatum]"
---

# /arbeitsrecht:fehlzeit-erfassen

## Zweck

Neue Abwesenheit in `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/urlaubsregister.yaml` eintragen, sodass der Urlaub-/Fehlzeiten-Tracker alle Fristen ab Tag 1 überwacht.

## Eingaben

- Mitarbeiter-Angaben (Name/ID – anonymisiert genügt)
- Abwesenheitstyp und Startdatum
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Standort, Tarifvertrag

## Ablauf

### 1. Konfiguration lesen

Standort-Fußabdruck, HRIS-Status, Tarifvertrag prüfen. Falls HRIS verbunden: Hinweis, dass Eintrag besser dort erfolgt; trotzdem im Register dokumentieren, wenn Nutzer dies wünscht.

### 2. Alle nötigen Informationen in einem einzigen Prompt abfragen

> Kurze Angaben für den Fehlzeiteintrag:
>
> - **Mitarbeiter-ID oder Rolle** (anonymisiert ist in Ordnung)
> - **Bundesland** (bestimmt anwendbare Regeln)
> - **Abwesenheitstyp:**
>   - Krankheit / Arbeitsunfähigkeit (EFZG)
>   - Urlaub (BUrlG)
>   - Mutterschutz / Beschäftigungsverbot (MuSchG)
>   - Elternzeit (BEEG)
>   - Pflegezeit (PflegeZG)
>   - Sonstiges
> - **Startdatum** der Abwesenheit
> - **Voraussichtliches Rückkehrdatum** (falls bekannt – leer lassen wenn unbekannt)
> - **Bei Elternzeit:** Hat die Mitarbeiterin/der Mitarbeiter die Elternzeit schriftlich angemeldet? Anmeldedatum?
> - **Bei Krankheit:** Gleiche Erkrankung wie in zurückliegenden 12 Monaten? (für EFZG-Neuanspruchs-Berechnung)
> - **Schwangerschaft/Entbindung:** Errechneter Entbindungstermin (für MuSchG-Fristen)

### 3. Fristen automatisch berechnen

Je nach Abwesenheitstyp:

**Krankheit (EFZG):**
- EFZG-Erschöpfungsdatum: Startdatum + 42 Tage (6 Wochen) [Achtung: Werktage vs. Kalendertage; § 3 EFZG zählt Kalendertage, nicht Arbeitstage; BAG, Urt. v. 13.07.2005 – 5 AZR 578/04, NZA 2006, 98 `[Modellwissen – prüfen]`]
- BEM-Prüfdatum: ab 6-wöchiger AU innerhalb von 12 Monaten (§ 167 Abs. 2 SGB IX)
- Wenn gleiche Erkrankung: Neuer EFZG-Anspruch? Letzter AU-Zeitraum prüfen.

**Urlaub (BUrlG):**
- Verfallsdatum: 31.12. des laufenden Jahres (§ 7 Abs. 3 S. 1 BUrlG) bzw. 31.03. des Folgejahres bei Übertragung
- Hinweispflichts-Erinnerung: 3 Monate vor Verfall (EuGH C-684/16)
- Resturlaub berechnen: Gesamtanspruch − genommene Tage

**Mutterschutz (MuSchG):**
- Schutzfrist-Beginn: 6 Wochen vor errechnetem Entbindungstermin (§ 3 MuSchG)
- Schutzfrist-Ende: 8 Wochen nach Entbindung (§ 3 Abs. 2 MuSchG; 12 Wochen bei Frühgeburt)
- Kündigungsschutz-Ende: 4 Monate nach Entbindung (§ 17 Abs. 1 S. 1 Nr. 1 MuSchG)

**Elternzeit (BEEG):**
- Anmeldefrist geprüft? (7 Wochen vor Beginn; § 16 Abs. 1 BEEG)
- Elternzeit-Ende: 3. Geburtstag des Kindes als maximale Frist
- Kündigungsschutz-Ende: Ende der Elternzeit (§ 18 Abs. 1 BEEG)
- Teilzeit-Anspruch: Ab Beginn der Elternzeit (§ 15 Abs. 6 BEEG)

**Pflegezeit (PflegeZG):**
- Max. 6 Monate (§ 3 Abs. 1 PflegeZG)
- Kündigungsschutz: ab Ankündigung bis 4 Wochen nach Ende (§ 5 PflegeZG)
- Ankündigungsfrist: 10 Arbeitstage vor Beginn (§ 3 Abs. 3 PflegeZG)

### 4. Eintrag schreiben

Register-Eintrag anlegen in `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/urlaubsregister.yaml`:

```yaml
- id: [generierte ID]
  mitarbeiter: [anonymisierte Bezeichnung]
  bundesland: [BL]
  typ: [krankheit|urlaub|mutterschutz|elternzeit|pflegezeit|sonstiges]
  startdatum: [JJJJ-MM-TT]
  rueckkehr_geplant: [JJJJ-MM-TT | unbekannt]
  fristen:
    efzg_erschoepfung: [JJJJ-MM-TT]      # nur bei Krankheit
    bem_pruefung: [JJJJ-MM-TT]            # nur bei Krankheit ≥ 6 Wochen
    urlaubsverfall_warnung: [JJJJ-MM-TT]  # nur bei Urlaub
    schutzfrist_ende: [JJJJ-MM-TT]        # MuSchG/BEEG
    ks_schutz_ende: [JJJJ-MM-TT]          # Kündigungsschutz-Ende
  notizen: [ggf.]
  status: offen
```

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-deutsches-recht.md`.

- § 3 EFZG (6-Wochen-Fortzahlung), § 5 EFZG (Nachweispflicht)
- § 3, 7 BUrlG (Mindesturlaub, Übertragung, Verfall)
- § 3 MuSchG (Schutzfristen), § 17 MuSchG (Kündigungsschutz)
- §§ 15–18 BEEG (Elternzeit, Anmeldung, Kündigungsschutz)
- § 167 Abs. 2 SGB IX (BEM-Pflicht)
- EuGH, Urt. v. 06.11.2018 – C-684/16 (Max-Planck), NZA 2018, 1474

## Ausgabeformat

```
FEHLZEITEINTRAG ANGELEGT – [ID] – [Datum]

Mitarbeiter:   [ID/Rolle]
Typ:           [Abwesenheitstyp]
Bundesland:    [BL]
Start:         [Datum]
Rückkehr:      [Datum / unbekannt]

Berechnete Fristen:
  [Fristname]:  [Datum]  [Norm]

Gespeichert: ~/.../urlaubsregister.yaml
Nächste Prüfung: /arbeitsrecht:urlaub-fehlzeiten
```

## Beispiele

```
/arbeitsrecht:fehlzeit-erfassen
Mitarbeiterin HR-022, Bayern, Elternzeit ab 01.02.2025.
Anmeldung liegt schriftlich vor (10.12.2024). Rückkehr geplant 01.02.2026.
```

## Risiken / typische Fehler

- **BEEG-Anmeldung nachträglich** – Elternzeit kann nicht rückwirkend beantragt werden; Anmeldedatum prüfen.
- **Mehrere Abwesenheitsperioden bei gleicher Erkrankung** – EFZG-Neuanspruch-Prüfung nicht vergessen.
- **Urlaubsverfall ohne Hinweis-Dokumentation** – Arbeitgeber muss nachweisen, dass er auf drohenden Urlaubsverfall hingewiesen hat (EuGH C-684/16); im Register dokumentieren.
- **Anonymisierung** – auch im internen Register: Mitarbeiter-IDs statt Namen verwenden; § 26 BDSG.
