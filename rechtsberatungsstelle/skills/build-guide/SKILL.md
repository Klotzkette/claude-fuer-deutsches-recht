---
name: build-guide
description: >
  Hilft einem anleitenden Volljuristen, einen praxisbereichsspezifischen
  Leitfaden zu erstellen, der das Verhalten der studierendengerichteten Skills
  konfiguriert – Intake-Fragen, Pädagogikhaltung (ausführen / anleiten / lehren),
  Prüfungsgates, RDG-Grenzen und örtliche Besonderheiten. Aufrufen, wenn ein
  Anleiter einen neuen Leitfaden aufbauen oder einen bestehenden überarbeiten will.
argument-hint: "[optional: Fachbereich – z. B. 'asyl', 'sgbii', 'mietrecht']"
language: de
triggers:
  - "leitfaden erstellen"
  - "beratungsstelle aufbauen"
  - "guide konfigurieren"
  - "build-guide"
---

# /build-guide

1. Lade `CLAUDE.md` → Rolle (muss Anleitender Volljurist sein), Fachbereiche, Rechtsgrundlage.
2. Nutze den untenstehenden Workflow.
3. Wenn der Nutzer kein Anleitender Volljurist ist: Stopp und weiterleiten (Studierende → `/rechtsberatungsstelle:ramp`).
4. Durchlaufe: Fachbereich → Intake-Fragen → Pädagogikhaltung → Prüfungsgates → Querprüfungen → örtliche Besonderheiten.
5. Schreibe `guides/<fachbereich>.md`. Erstelle das Verzeichnis `guides/` bei Bedarf.
6. Biete einen Testlauf an: `/rechtsberatungsstelle:draft` unter der konfigurierten Haltung ausführen, damit der Anleiter sieht, was Studierende sehen.

---

# Build Guide: Anleitungsgeführter Fachbereichsleitfaden

## Zweck

Der Anleiter-Leitfaden ist der Regler, der studierendengerichtete Skills von „Arbeit erledigen" auf „Studierenden die Arbeit lehren" umstellt. Jeder studierendengerichtete Skill liest den Leitfaden, bevor er eine Ausgabe produziert: Intake stellt die Fragen, die der Anleiter gewünscht hat; Entwurfs-Skills wählen eine Pädagogikhaltung (ausführen / anleiten / lehren); Prüfungsgates leiten zu den Punkten weiter, die dem Anleiter wichtig sind.

**Zielgruppe: der anleitende Volljurist.** Nicht Studierende. Studierende starten mit `/rechtsberatungsstelle:ramp`.

## Berufsrechtlicher Rahmen

Dieser Leitfaden ist ein internes Konfigurationsdokument. Er legt fest, wie die Beratungsstelle nach § 6 Abs. 2 Nr. 2 RDG betrieben wird:

- **§ 6 Abs. 2 Nr. 2 RDG:** Unentgeltlichkeit und Anleiterpflicht sind in jedem Leitfaden zu verankern.
- **§ 43a Abs. 2 BRAO:** Verschwiegenheit des Anleiters erstreckt sich auf alle im Rahmen der Beratungsstelle erlangten Informationen.
- **§ 43a Abs. 4 BRAO / BORA § 3:** Der Leitfaden muss Konfliktprüfungsregeln für den Fachbereich enthalten.
- **Krenzler, in: Krenzler (Hrsg.), RDG, 2. Aufl. 2021, § 6 Rn. 44–52:** Anforderungen an die Anleitungsorganisation.

## Schlüsselinhalte des Leitfadens

Biete dies als Checkliste an, die der Anleiter durcharbeiten oder als Inhaltsverzeichnis nutzen kann:

- Was müssen Studierende wissen, bevor sie einen Fall berühren? (Verschwiegenheit nach § 43a BRAO analog / § 203 StGB; RDG-Grenzen; Umfang ihrer Befugnisse)
- Was sind die 3–5 häufigsten Fehler von Studierenden in diesem Fachbereich, und wie soll der Skill sie erkennen?
- Wann muss der Studierende pausieren und Rücksprache halten? (Einreichung, Versand, Strategieentscheidung, Vergleich)
- Welches Sprachniveau ist für Mandantenmitteilungen anzustreben? (Leichte Sprache Niveau B1/B2 als Ziel bei Mandanten ohne juristische Vorbildung; ggf. mehrsprachig bei Geflüchteten)
- Welche örtlichen Sonderregeln, Formulare oder Fristen muss jede Studierende kennen?
- Wann soll der Skill lehren statt tun? (Je Dokumenttyp – Default und Ausnahmen festlegen)

## Workflow

### Schritt 1: Rollenprüfung

Dies ist ein Anleiter-Skill. Lies `CLAUDE.md` → `Rolle`. Wenn die Rolle nicht „Anleitender Volljurist" ist:

> Dieser Skill ist für Anleiter – er konfiguriert das Verhalten der studierendengerichteten Skills. Wenn Sie der Anleiter sind, stellen Sie sicher, dass Ihre Rolle in `/rechtsberatungsstelle:cold-start-interview` auf „Anleitender Volljurist" gesetzt ist. Wenn Sie Studierende/r sind, ist dies nicht der richtige Skill für Sie – starten Sie mit `/rechtsberatungsstelle:ramp`.

Stopp, wenn Rolle nicht Anleiter.

### Schritt 2: Fachbereich?

> Für welchen Fachbereich soll dieser Leitfaden gelten? (Asyl/Aufenthaltsrecht | SGB II/Bürgergeld | Mietrecht | Verbraucherrecht | Familienrecht | SGB IX/Eingliederungshilfe | Sonstiges)

Falls „Sonstiges": Kurzname erfragen → wird zum Dateinamen (Kleinbuchstaben, Bindestriche: `asyl.md`, `sgbii.md`, `mietrecht.md`).

Prüfe die in `CLAUDE.md` → `Fachbereiche` eingetragenen Bereiche. Wenn der gewählte Bereich dort nicht aufgeführt ist, hinweisen.

Falls ein Leitfaden für diesen Bereich bereits existiert: „Möchten Sie (a) abschnittsweise überarbeiten, (b) neu aufbauen und überschreiben, oder (c) zunächst den bestehenden Leitfaden sehen?"

### Schritt 3: Intake-Fragen

> Was sollten Studierende eine neue Mandantin/einen neuen Mandanten für diesen Fachbereich fragen? Ich starte mit einem generischen Intake für [Fachbereich] – sagen Sie mir, was hinzugefügt, entfernt oder geändert werden soll. Welche Warnsignale sollten Studierende erkennen? Welche Fälle passen gut zur Beratungsstelle, welche sollten weitervermittelt werden?

Fachbereichs-Defaults (wenn keine Angaben vorhanden):

**Asyl/Aufenthaltsrecht:**
- Aktueller Status und Einreisezeitpunkt (Datum für Jahresfrist § 74 AsylG wichtig!)
- Laufende Verfahren: BAMF-Bescheid erhalten? Klage eingereicht?
- Besondere Vulnerabilität: Minderjährigkeit, Traumatisierung, Behinderung (§ 76b SGB IX)
- Familienangehörige und deren Status
- Vorstrafen (mit Sensibilität erfragen – § 3 AsylG, § 60 AufenthG prüfen)
- Sprachkenntnisse / Dolmetscherbedarf
- Dringlichkeit: Zustellungsdatum des Bescheids? Klagefrist (§ 74 AsylG: 2 Wochen bei § 36-Bescheid!)?

**SGB II / Bürgergeld:**
- Aktueller Leistungsbezug / zuletzt erhaltener Bescheid
- Anlass: Bewilligungs-, Änderungs- oder Ablehnungsbescheid? Sanktionsbescheid?
- Einkommensverhältnisse, Vermögen (§§ 11–12 SGB II)
- Unterkunftskosten (§ 22 SGB II – Angemessenheit prüfen)
- Widerspruchsfrist: 1 Monat ab Bekanntgabe (§ 84 SGG)
- Vorherige Kontakte mit dem Jobcenter (Widersprüche, Klagen)

**Mietrecht:**
- Art des Mietverhältnisses (privat, sozial, öffentlich-gefördert)
- Anlassfall: Kündigung, Mieterhöhung, Mängel, Kaution, Modernisierung?
- Mietvertrag und Mietdauer
- Dokumentation vorhandener Mängel (Fotos, Schriftverkehr)
- Mietspiegel des Ortes verfügbar? (z. B. Berliner Mietspiegel 2023/2024)
- Dringlichkeit: Räumungsklage? Gerichtstermin?

### Schritt 4: Pädagogikhaltung

Drei Stufen – Anleiter wählt Default und kann je Dokumenttyp übersteuern:

| Haltung | Was der Skill tut | Geeignet für |
|---|---|---|
| **Ausführen** | Entwurf vollständig ausarbeiten; Studierende analysieren und übergeben | Routineschriftsätze im 3. Semester+ |
| **Anleiten** | Gliederung und Schlüsselpunkte ausgeben; Studierende füllen aus | Memos, neue Fachbereiche |
| **Lehren** | Nur Fragen stellen; Studierenden zur Lösung führen | 1. Semester, neue Fachbereiche, komplexe Rechtsfragen |

### Schritt 5: Prüfungsgates

> Welche Arten von Dokumenten oder Entscheidungen müssen zwingend zu Ihnen? Ich schlage vor: Klageerhebung, Widerspruch (bei kurzfristigen Rechtsbehelfsfristen sofort), alle Schriftsätze an Gericht, alle Mitteilungen an Mandanten mit konkretem Rechtsrat.

Anleiter kann die Gate-Liste erweitern, einschränken oder beibehalten.

### Schritt 6: Querprüfungen

Welche anderen Fachbereiche überschneiden sich regelmäßig?

- Asylmandate → fast immer SGB II/XII-Fragen (§ 7 Abs. 1 Satz 2 Nr. 1 SGB II: Leistungsausschluss für bestimmte Ausländer beachten!)
- Mietmandate → ggf. Sozialhilfe (§ 22 SGB II Unterkunftskosten), ggf. Familienrecht
- SGB II → Arbeitsrecht (Eingliederungsvereinbarung, Sanktionen bei Ablehnung von Arbeit)

### Schritt 7: Örtliche Besonderheiten

> Gibt es örtliche Regeln, Sonderformulare oder Fristen, die jede Studierende kennen muss? Welche lokalen Anlaufstellen (Gerichte, Behörden, Dolmetscherdienste, Kooperationspartner) sind wichtig?

**Berlin-Beispiele:**
- Berliner Mietspiegel 2023/2024 (qualifiziert nach § 558d BGB)
- Jobcenter-Bezirke Berlin (11 Bezirke) – Formulare und Zuständigkeiten
- BAMF-Außenstellen Berlin, Eisenhüttenstadt
- Pro Bono Berlin e. V. als Weitervermittlungspartner
- Berliner Beratungszentrum für Migration und Qualifizierung (BBZ)

**Bremen-Beispiele:**
- Jobcenter Bremen (zentral)
- BAMF Bremen
- Refugee Law Clinic Bremen (Uni Bremen) – Kooperationen möglich
- Caritasverband Bremen – Migrationsberatung
- Verbraucherzentrale Bremen

### Schritt 8: Leitfaden schreiben

Ausgabe: `guides/<fachbereich>.md` mit den Sektionen:
1. Fachbereichsüberblick und RDG-Grenzen
2. Intake-Fragen (Standard und Warnsignale)
3. Pädagogikhaltung (Default + Ausnahmen)
4. Prüfungsgates
5. Querprüfungen
6. Örtliche Besonderheiten und Weitervermittlung
7. Wichtige Fristen auf einen Blick
8. Empfohlene Quellen und Datenbanken

## Ausgabeformat

Supervisor-gerichtetes Konfigurationsdokument in Markdown. Kein `[KI-GESTÜTZTER ENTWURF]`-Vermerk – dies ist kein Studierenden-Output, sondern Anleiter-Konfiguration. Länge: 80–150 Zeilen pro Leitfaden.

## Risiken / typische Fehler

- **Fristenversäumnis:** Der Leitfaden muss für jeden Fachbereich die kritischsten Fristen explizit benennen. Besonders gefährlich: § 36 AsylG (1 Woche), § 74 AsylG (2 Wochen bei beschleunigtem Verfahren), § 4 KSchG (3 Wochen).
- **RDG-Grenzen nicht klar kommuniziert:** Studierende ohne klare Anleitungsstruktur überschreiten versehentlich § 3 RDG.
- **Fehlende Konfliktprüfung:** Ohne explizite Gate-Regel übersehen Studierende, wann sie den Anleiter einschalten müssen.
- **Sprachbarrieren bei Geflüchteten:** Leitfaden sollte Dolmetscherressourcen und Sprach-Level-Anforderungen an Mandantenbriefe festlegen.
