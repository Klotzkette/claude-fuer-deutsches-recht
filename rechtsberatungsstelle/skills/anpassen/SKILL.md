---
name: anpassen
description: "Für /anpassen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Plugin für die studentische Rechtsberatungsstelle."
---

# /anpassen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

1. Lade `CLAUDE.md` → aktuelles Profil anzeigen.
2. Frage: Welcher Abschnitt soll geändert werden?
3. Führe die gezielte Änderung durch – kein Full-Redo.
4. Aktualisierte Datei ausgeben.

---

### Beratungsstellenprofil anpassen

## Triage zu Beginn
1. Welcher Abschnitt des Profils soll angepasst werden: Semesterwechsel, Fachbereich, Prüfungsgates, Anleiter-Kontakt oder Gesetzesaenderung?
2. Hat sich die Rechtsgrundlage der Beratungsstelle geaendert (z.B. neues RDG, neue Kooperationsvereinbarung)?
3. Sind neue Studenten aufgenommen worden, die in die CLAUDE.md eingetragen werden müssen?
4. Soll gleichzeitig ein Fachbereichsleitfaden angepasst werden oder nur das Hauptprofil?

## Zentrale Normen
- § 6 Abs. 2 Nr. 2 RDG — Anleitungsstruktur muss aktuell und wirksam sein; Semesterwechsel erfordert Profil-Update
- Art. 30 DSGVO — Verarbeitungsverzeichnis: bei Änderung des Verarbeitungsumfangs zu aktualisieren
- §§ 43, 43a BRAO — Berufspflichten des Anleiters: kontinuierliche Aktualitaet der Organisationsunterlagen
- § 203 Abs. 4 StGB — Einbeziehung Dritter: bei Wechsel von Studentenn neue Verschwiegenheitsvereinbarungen prüfen

## Häufige Anpassungsszenarien

### 1. Semesterwechsel

> Welche Studentenn sind neu? Welche gehen? Wer übernimmt laufende Mandate?

Änderungen in `CLAUDE.md`:
- `Semester: [WS 2024/25]` → `[SS 2025]`
- Liste der aktiven Studentenn aktualisieren.
- Mandate-Übergabe: Verweis auf `/rechtsberatungsstelle:semester-übergabe`.

### 2. Neuen Fachbereich hinzufügen

Fachbereich in `CLAUDE.md` unter `Fachbereiche` ergänzen. Dann sofort:
> "Soll für den neuen Bereich auch ein Leitfaden erstellt werden? → `/rechtsberatungsstelle:leitfaden-erstellen [fachbereich]`"

### 3. Prüfungsgates ändern

> Welche Gates sollen geändert werden? Verschärfen oder lockern?

Tabelle in `CLAUDE.md` → `Aufsichtsmodell` anpassen. Hinweis: Lockerung nur bei nachgewiesener Erfahrung der Studentenn. § 6 Abs. 2 Nr. 2 RDG verlangt tatsächliche Anleitung.

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

Für ein bestimmtes Semester oder einen bestimmten Studentenn die Default-Haltung anpassen. Z. B.: "Für dieses Semester soll der Skill primär im Modus 'Anleiten' arbeiten, da alle Studentenn im ersten Klinik-Semester sind."

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
- `[H]` Semester / Studenten
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

## Risiken / typische Fehler

- **Versehentliches Löschen:** Beim Anpassen einzelner Abschnitte nie den Rest des Profils löschen. Immer vollständige Datei ausgeben, nicht nur den geänderten Abschnitt.
- **Gesetzesänderungen nicht eingepflegt:** Veraltertes Profil führt dazu, dass der Skill mit überholten Normen arbeitet (z. B. falsche Regelbedarfsstufen, falsche Fristen).
- **Mandate ohne Übergabe:** Beim Semesterwechsel sicherstellen, dass alle laufenden Mandate über `/rechtsberatungsstelle:semester-übergabe` übergeben werden, bevor das Profil auf das neue Semester umgestellt wird.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
