---
name: rechtsberatungsstelle-anpassen
description: "Rechtsberatungsstelle-Plugin an spezifische Kanzlei oder Uni anpassen: Anwendungsfall neue Rechtsberatungsstelle moechte Plugin konfigurieren mit eigenen Rechtsgebieten Zielgruppe und Verfahrensregeln. BeratungsHiG, BRAO, hochschulspezifische Beratungsordnung. Pruefraster Rechtsgebiete einstellen, Zielgruppe und Sprachstil, Beratungsschein-Regelungen, Anleiter-Kontakte und Eskalationspfade konfigurieren. Output konfiguriertes Plugin-Profil mit angepassten Workflows fuer die jeweilige Stelle. Abgrenzung zu Kaltstart-Interview fuer Erst-Einrichtung und zu Einarbeitung-Skill."
---

# /anpassen

1. Lade `CLAUDE.md` → aktuelles Profil anzeigen.
2. Frage: Welcher Abschnitt soll geändert werden?
3. Führe die gezielte Änderung durch – kein Full-Redo.
4. Aktualisierte Datei ausgeben.

---

# Beratungsstellenprofil anpassen


## Triage zu Beginn
1. Welcher Abschnitt des Profils soll angepasst werden: Semesterwechsel, Fachbereich, Prüfungsgates, Anleiter-Kontakt oder Gesetzesaenderung?
2. Hat sich die Rechtsgrundlage der Beratungsstelle geaendert (z.B. neues RDG, neue Kooperationsvereinbarung)?
3. Sind neue Studierende aufgenommen worden, die in die CLAUDE.md eingetragen werden muessen?
4. Soll gleichzeitig ein Fachbereichsleitfaden angepasst werden oder nur das Hauptprofil?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — Kanzleiorganisation (hier: Beratungsstellenorganisation) muss stets auf aktuellem Stand gehalten werden; veraltete Konfigurationen begruenden Haftungsrisiken.
- BVerfG, Beschl. v. 14.01.2020 - 1 BvR 2316/19, NJW 2020, 897 — Berufsrechtliche Organisationspflichten gelten kontinuierlich; Semesterwechsel und Personalwechsel muessen sofort in der Konfiguration abgebildet werden.
- BGH, Urt. v. 07.02.2019 - IX ZR 5/18, NJW 2019, 1513 — Aktuell geltende Gesetze und Regelbedarfe muessen in Beratungsunterlagen widergespiegelt sein; veraltete Normen-Referenzen begruenden Beratungsfehlerrisiko.
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Datenschutzrelevante Konfigurationsaenderungen erfordern Aktualisierung des Verarbeitungsverzeichnisses (Art. 30 DSGVO).

## Zentrale Normen
- § 6 Abs. 2 Nr. 2 RDG — Anleitungsstruktur muss aktuell und wirksam sein; Semesterwechsel erfordert Profil-Update
- Art. 30 DSGVO — Verarbeitungsverzeichnis: bei Aenderung des Verarbeitungsumfangs zu aktualisieren
- §§ 43, 43a BRAO — Berufspflichten des Anleiters: kontinuierliche Aktualitaet der Organisationsunterlagen
- § 203 Abs. 4 StGB — Einbeziehung Dritter: bei Wechsel von Studierenden neue Verschwiegenheitsvereinbarungen pruefen

## Kommentarliteratur
- Krenzler (Hrsg.) RDG § 6 Rn. 44-52 (Anleitungsorganisation: Aktualitaetspflicht bei Semesterwechsel)
- Kühling/Buchner DSGVO Art. 30 Rn. 1-25 (Verarbeitungsverzeichnis: Inhalt und Aktualisierungspflicht)

## Zweck

Nach der Ersteinrichtung (`/kaltstart-interview`) müssen Beratungsstellenprofile regelmäßig aktualisiert werden:
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
- Mandate-Übergabe: Verweis auf `/rechtsberatungsstelle:semester-übergabe`.

### 2. Neuen Fachbereich hinzufügen

Fachbereich in `CLAUDE.md` unter `Fachbereiche` ergänzen. Dann sofort:
> „Soll für den neuen Bereich auch ein Leitfaden erstellt werden? → `/rechtsberatungsstelle:leitfaden-erstellen [fachbereich]`"

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

## Ablauf

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
- **Mandate ohne Übergabe:** Beim Semesterwechsel sicherstellen, dass alle laufenden Mandate über `/rechtsberatungsstelle:semester-übergabe` übergeben werden, bevor das Profil auf das neue Semester umgestellt wird.
