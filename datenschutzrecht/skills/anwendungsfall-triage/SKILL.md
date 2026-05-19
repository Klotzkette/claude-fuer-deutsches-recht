---
name: anwendungsfall-triage
description: >
  Prüft einen neuen Verarbeitungsvorgang datenschutzrechtlich und klassifiziert ihn als
  FREIGABE, DSA ERFORDERLICH, DSFA PFLICHT oder STOPP — mit Rechtsgrundlagenprüfung,
  Datenschutzrichtlinien-Abgleich und Weiterleitung an den nächsten Schritt.
  Lädt, wenn der Nutzer eine neue Verarbeitung, ein Produktfeature oder eine
  Auftragsverarbeitung beschreibt und fragt, ob eine Datenschutz-Folgenabschätzung nötig ist.
language: de
triggers:
  - "Datenschutz-Triage"
  - "brauchen wir eine DSFA"
  - "neues Feature datenschutzrechtlich prüfen"
  - "Verarbeitungstätigkeit einordnen"
  - "Rechtsgrundlage DSGVO"
  - "Privacy by Design"
  - "Auftragsverarbeitung prüfen"
  - "Verzeichnis Verarbeitungstätigkeiten"
  - "DSGVO Use-Case prüfen"
  - "datenschutzrechtliche Vorabprüfung"
---

# Datenschutz-Triage neuer Verarbeitungsvorgänge

## Zweck

Diese Skill beantwortet die Frage vor jeder Datenschutz-Folgenabschätzung (DSFA):
Ist eine Prüfung erforderlich — und wenn ja, welche Art?

Die Triage ist schneller als die DSFA-Generierung, aber ihr vorgelagert. Sie erstellt
die Folgenabschätzung nicht, sondern bestimmt, ob sie geboten ist.

**Vier Klassifikationen:**
- **FREIGABE** — Keine gesonderte Prüfung. Standardschutzmaßnahmen gelten.
- **DSA ERFORDERLICH** — Datenschutzprüfung vor oder begleitend zum Einsatz.
- **DSFA PFLICHT** — Art. 35 DSGVO zwingend; DSB-Einbindung erforderlich.
- **STOPP** — Verarbeitung widerspricht Datenschutzrichtlinie oder entbehrt jeder
  Rechtsgrundlage; Neugestaltung vor Fortführung zwingend.

## Eingaben

- Beschreibung des Verarbeitungsvorgangs (Datenarten, Zweck, Betroffenenkreis)
- Datenkategorien (Art. 4 Nr. 1, Art. 9 DSGVO); Beschäftigtendaten (§ 26 BDSG)?
- Neu erhoben oder Zweckänderung bei vorhandenen Daten (Art. 5 Abs. 1 lit. b DSGVO)?
- Auftragsverarbeiter / Drittland-Übermittlung?
- Automatisierte Entscheidungsfindung (Art. 22 DSGVO)?
- Cookies / Endgerätezugriff (§§ 24 ff. TDDDG)?

## Rechtlicher Rahmen

### Kernvorschriften

- **DSGVO:** Art. 5 (Grundsätze), Art. 6 (Rechtsgrundlagen), Art. 9 (besondere
  Kategorien), Art. 13/14 (Informationspflichten), Art. 17 (Löschrecht), Art. 22
  (automatisierte Entscheidungen), Art. 25 (Privacy by Design/Default), Art. 28 (AVV),
  Art. 30 (Verarbeitungsverzeichnis), Art. 32 (TOM), Art. 35 (DSFA), Art. 44 ff.
  (Drittlandtransfer).
- **BDSG:** § 22 (Gesundheits-/Sozialdaten), § 26 (Beschäftigtendatenschutz), § 38
  (betrieblicher DSB).
- **TDDDG (ehem. TTDSG):** §§ 24 ff. — Einwilligung für Cookies/Endgerätezugriffe.
- **Art. 35 Abs. 4 DSGVO** i. V. m. DSK-Positivliste — nationale Pflichttatbestände.

### Leitentscheidungen

- `EuGH, Urt. v. 16.07.2020 – C-311/18, NJW 2020, 2613 Rn. 91 ff. (Schrems II)`
  — Ungültigkeit EU-US-Privacy-Shield; Standardvertragsklauseln erfordern Transfer
  Impact Assessment; maßgeblich für Art. 44 ff. DSGVO.
- `EuGH, Urt. v. 07.12.2023 – C-634/21, NJW 2024, 203 Rn. 45 ff. (Schufa-Scoring)`
  — Automatisiertes Scoring als Entscheidung i. S. d. Art. 22 DSGVO, wenn Dritte
  maßgeblich darauf abstellen; zentral für Triage von KI-/Scoring-Vorhaben.
- `BGH, Urt. v. 12.10.2021 – VI ZR 488/19, NJW 2022, 1314 Rn. 20 ff.`
  — Datenschutzrechtliche Haftung Art. 82 DSGVO; Beweislastverteilung.
- `BVerfG, Beschl. v. 06.11.2019 – 1 BvR 16/13, NJW 2020, 300 Rn. 95 ff.`
  *(Recht auf Vergessen I)* — Datenschutz als Teil des allgemeinen Persönlichkeitsrechts
  (Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG); Abwägung mit Kommunikationsfreiheiten.

### Kommentare

- `Kühling/Buchner (Hrsg.), DSGVO/BDSG, 4. Aufl. 2024, Art. 35 DSGVO Rn. 10 ff.`
  — DSFA-Pflicht, Schwellenwerte, Verhältnis zu nationalen Listen.
- `Simitis/Hornung/Spiecker (Hrsg.), DSGVO, 2. Aufl. 2022, Art. 6 Rn. 30 ff.`
  — Rechtsgrundlagen; berechtigtes Interesse als Auffangtatbestand.
- `Gola (Hrsg.), DSGVO, 3. Aufl. 2022, Art. 22 Rn. 5 ff.`
  — Automatisierte Entscheidungsfindung; Abgrenzung zu Profiling.
- `Paal/Pauly (Hrsg.), DS-GVO BDSG, 3. Aufl. 2021, Art. 25 DSGVO Rn. 7 ff.`
  — Privacy by Design und Privacy by Default als Entwurfspflicht.
- `Ehmann/Selmayr (Hrsg.), DS-GVO, 2. Aufl. 2018, Art. 35 Rn. 25 ff.`
  — Anwendungsbereich der DSFA; Verhältnis zu Art. 5, 25 DSGVO.

## Ablauf

### Schritt 1: Verarbeitungsvorgang klären

Bei vager Beschreibung zuerst nachfragen: Datenkategorien (Art. 9?), Betroffenenkreis
(Beschäftigte → § 26 BDSG!), Zweck, Neu oder Zweckänderung, Auftragsverarbeiter,
automatisierte Entscheidung (Art. 22), Endgerätezugriff (§ 24 TDDDG).

### Schritt 2: Hausinternes DSA-Raster

Konfiguriertes Prüfraster aus CLAUDE.md lesen. Trigger erfüllt → mindestens
**DSA ERFORDERLICH**. Nicht erfüllt → weiter mit Schritt 3.

### Schritt 3: DSFA-Pflichtprüfung (Art. 35 DSGVO)

**Pflichttatbestände (Art. 35 Abs. 3, DSK-Positivliste):**
- Systematische automatisierte Bewertung persönlicher Aspekte inkl. Profiling mit
  erheblichen Auswirkungen (Art. 22 DSGVO; vgl. EuGH C-634/21).
- Umfangreiche Verarbeitung besonderer Datenkategorien (Art. 9 DSGVO).
- Systematische umfangreiche Überwachung öffentlich zugänglicher Bereiche.

**Starke Indikatoren (kein Pflichttatbestand, aber DSFA dringend empfohlen):**
neue Technologie, Kinderdaten, Zusammenführung getrennter Datensätze,
Diskriminierungspotenzial, Cross-Context-Tracking, verhaltensbasierte Werbung.

Pflichttatbestand erfüllt → **DSFA PFLICHT**. Nur Indikatoren → **DSA ERFORDERLICH**.

### Schritt 4: Datenschutzrichtlinien-Abgleich

Vorhaben gegen konfigurierte Richtlinien prüfen. Typische Konflikte:
Datenkategorie nicht in Richtlinie erfasst; Drittlandweitergabe ohne Grundlage
(Art. 44 ff. DSGVO); Löschfristen (Art. 17) überschritten; Zweckbindung (Art. 5
Abs. 1 lit. b) verletzt; Betroffenenrechte unvollständig.

Direkter Konflikt → **STOPP**. Konflikt muss aufgelöst sein vor Fortführung.

### Schritt 5: Klassifikation und Ausgabe

```
Kurzergebnis: [DSFA PFLICHT / DSA ERFORDERLICH / FREIGABE / STOPP — ein Satz]

VORGANG: [wie verstanden]
KLASSIFIKATION: [...]
Hausinternes DSA-Raster ausgelöst? [Ja / Nein]
DSFA-Pflicht (Art. 35 DSGVO)? [Ja — Tatbestand / Nein / N/A]
Richtlinienkonflikt? [Keiner / Ja — konkreter Konflikt]
Begründung: [1–3 Sätze]
```

*Voraussetzungen bei DSA / DSFA:*

| Anforderung | Verantwortlich | Erledigt? |
|---|---|---|
| Datenschutzprüfung / DSFA (Art. 35 DSGVO) | DSB | ☐ |
| Berechtigtes-Interesse-Abwägung (Art. 6 Abs. 1 lit. f) | DSB / Legal | ☐ |
| DSB-Konsultation (DSFA-Pflichtverfahren) | DSB | ☐ |
| AVV (Art. 28 DSGVO) | Legal | ☐ |
| Richtlinienaktualisierung vor Launch | DSB | ☐ |
| Eintrag Verarbeitungsverzeichnis (Art. 30) | DSB | ☐ |

**Rechtsgrundlage (Art. 6 DSGVO):** [lit. a Einwilligung / lit. b Vertrag /
lit. c rechtliche Verpflichtung / lit. f berechtigte Interessen — oder „unklar"]

Nach Klassifikation immer anbieten: „Soll ich jetzt direkt mit der DSFA beginnen?"

*Bei STOPP:*  
Konflikt benennen. Optionen: (A) Vorhaben umgestalten, (B) Richtlinie aktualisieren
(Vereinbarkeit mit Rechtsgrundlage prüfen). Keinen Weg vorschlagen, wenn keiner besteht.

### Schritt 6: Weiterleitung

- **KI-Governance:** Automatisierte Entscheidungen (Art. 22; EuGH C-634/21) → parallel
  KI-Folgenabschätzung erwägen.
- **Beschäftigtendatenschutz:** § 26 BDSG und Mitbestimmung (§§ 87 Abs. 1 Nr. 6,
  94 BetrVG) prüfen.

## Ausgabeformat

Ausgabe im Chat. Bei DSA, DSFA oder STOPP optional Protokolldatei:
`~/datenschutz-triagen/triage-YYYY-MM-DD-[vorgang].md`.

**Sammel-Triage** (Feature-Liste):

| # | Vorgang | Klassifikation | Blocker |
|---|---|---|---|
| 1 | [Vorgang] | FREIGABE | — |
| 2 | [Vorgang] | DSA ERFORDERLICH | Rechtsgrundlage offen; AVV fehlt |
| 3 | [Vorgang] | DSFA PFLICHT | Art.-9-Daten, großer Umfang |
| 4 | [Vorgang] | STOPP | Zweckbindungsverstoß |

## Beispiel

**Vorgang:** ML-basiertes Kreditscoring für Bestandskunden; Ergebnis fließt in
automatisierte Kreditentscheidung.

**Klassifikation:** DSFA PFLICHT — Art. 35 Abs. 3 lit. a DSGVO: systematische
automatisierte Bewertung persönlicher Aspekte mit erheblichen Auswirkungen
(Kreditablehnung). Zugleich Tatbestand Art. 22 Abs. 1 DSGVO. Nach EuGH C-634/21
(Schufa-Scoring) reicht es, dass Dritte maßgeblich auf das Scoring abstellen.
DSB-Konsultation und Verarbeitungsverzeichnis-Eintrag (Art. 30) zwingend.

## Risiken und typische Fehler

- **„Anonymisiert" = FREIGABE:** Pseudonymisierte Daten bleiben personenbezogen
  (Art. 4 Nr. 1 DSGVO). Re-Identifikationsrisiko konkret prüfen.
- **„Wir machen das ähnlich":** Bestehende, nie geprüfte Verarbeitungen legitimieren
  keine neue. Bei anderem Umfang/Zweck/Kategorie: neu triagen.
- **„Nur ein Pilot":** Pilot mit echten Personendaten unterliegt denselben Anforderungen.
- **„Der Anbieter regelt Datenschutz":** AVV nach Art. 28 zwingend; Triage bleibt beim
  Verantwortlichen (Art. 4 Nr. 7 DSGVO).
- **Inferred Data übersehen:** Score, Risikoklasse, Präferenz = personenbezogenes Datum.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Quellenpflicht

Jede Klassifikation muss nennen: einschlägige DSGVO-/BDSG-Normen mit Artikel/Absatz,
DSK-Listenfundstelle bei DSFA-Pflicht, einschlägige Rechtsprechung in korrekter
Zitierweise, Kommentare in Bearbeiterstil.

Beispiel Rechtsprechung:
`EuGH, Urt. v. 16.07.2020 – C-311/18, NJW 2020, 2613 Rn. 91 ff. (Schrems II)`

Beispiel Kommentar:
`Kühling/Buchner/Bäcker, DSGVO/BDSG, 4. Aufl. 2024, Art. 35 DSGVO Rn. 10`
