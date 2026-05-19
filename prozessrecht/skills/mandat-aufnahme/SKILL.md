---
name: mandat-aufnahme
description: Aufnahme eines neuen Mandats – strukturierte Fragen zu Identifizierung, Interessenkonflikten, Sachverhalt, Risikotriage, Materialität, Verfahrensart, Außenanwalt, Verantwortlichen, Beweissicherung und Schlüsselfristen; schreibt mandat.md und verlauf.md und fügt eine strukturierte Zeile in _log.yaml ein. Verwenden, wenn der Nutzer sagt „neues Mandat", „Mandat aufnehmen" oder ein neues Mandat ins Portfolio aufnehmen möchte.
language: de
triggers:
  - "mandat-aufnahme"
  - "neues mandat"
  - "mandat aufnehmen"
  - "neue sache"
  - "neue akte"
---

# Mandat-Intake

## Zweck

Vollständige und strukturierte Aufnahme eines neuen Mandats in das Portfolio. Der Skill führt ein interaktives Interview und schreibt die Ergebnisse in `mandate/[slug]/mandat.md` (Stammdaten), `mandate/[slug]/verlauf.md` (Erstem Eintrag) und hängt eine Zeile an `mandate/_log.yaml` an.

## Eingaben

- Optional: Name oder Kurzbezeichnung des Mandats
- Hochgeladene Dokumente (z. B. Klageschrift, Abmahnung, Bescheid, Vertrag)

## Ablauf

### 1. Identifikation und Aktenzeichen

- Kanzlei-Aktenzeichen und interner Slug (URL-freundlich, z. B. `mueller-gmbh-werkvertrag-2024`)
- Mandantenname (juristische oder natürliche Person), Kontaktperson
- Mandantentyp: Unternehmer (§ 14 BGB) / Verbraucher (§ 13 BGB)
- Gegenseite: Vollständiger Name, Anschrift, Verfahrensbevollmächtigter (wenn bekannt)
- Mandats-Art: Klage / Verteidigung / Beratung / Rechtsmittel / Vollstreckung

### 2. Interessenkonflikt-Check (§ 43a Abs. 4 BRAO, § 3 BORA)

- Vertritt die Kanzlei bereits die Gegenseite in irgendeinem Mandat?
- Ist ein Anwalt der Kanzlei früher für die Gegenseite tätig gewesen?
- Bestehen sonstige Interessenkonflikte (persönliche Beziehungen, Eigeninteresse)?
- **Bei positivem Befund:** Mandat ablehnen oder um Einverständnis einholen; Plugin erstellt Interessenkonflikt-Vermerk.

### 3. Sachverhaltserfassung

- Kurzbeschreibung des Sachverhalts (wer, was, wann, wie viel?)
- Anspruchsgrundlage (vorläufig, z. B. § 280 BGB, § 823 BGB, § 1 UWG)
- Rechtliches Kernproblem (streitige Tat- oder Rechtsfrage)
- Vorhandene Dokumente: Liste und Anlage-Nummern

### 4. Verfahrensart und Zuständigkeit

- Verfahrensordnung: ZPO / ArbGG / VwGO / FGO / SGG / FamFG / StPO
- Sachlich zuständiges Gericht: AG (§§ 23 ff. GVG), LG (§§ 71 ff. GVG), Spezialgerichte (ArbG, VG, FG, SG)
- Örtliche Zuständigkeit: allgemeiner Gerichtsstand (§§ 12, 13 ZPO), besonderer Gerichtsstand (§ 29 ZPO: Erfüllungsort), ausschließlicher Gerichtsstand (§ 29a ZPO: Miete)
- Streitwert (vorläufig, nach GKG/RVG)

### 5. Risikotriage

- Erfolgsaussichten: stark / mittel / schwach (mit Kurzbereg)
- Worst-Case-Szenario (maximale Exposition inkl. Kosten § 91 ZPO)
- Wichtig: Prozesskostenrisiko nach § 91 ZPO; ggf. Rechtsschutzversicherung vorhanden?
- Verjährungsrisiko prüfen: Restlaufzeit (§§ 195, 199 BGB)

### 6. Außenanwalt / Korrespondenzanwalt

- Wird die Sache vollständig intern geführt oder von externer Kanzlei?
- Externer Anwalt: Name, Kanzlei, Kontakt
- Reporting-Intervall an Mandanten

### 7. Beweissicherung

- Ist sofortige Beweissicherung erforderlich? (z. B. Baumangel, drohende Sachzustandsveränderung)
- Aufbewahrungsanordnung erstellen? → Weiterleitung an Skill `beweissicherung`

### 8. Schlüsselfristen

- Klagefrist / Antwortfrist
- Verjährungsablauf
- Nächste Prozesshandlung

### 9. mandat.md und verlauf.md schreiben

```yaml
# mandat.md
slug: ""
kanzlei_az: ""
mandant:
  name: ""
  typ: "Unternehmer / Verbraucher"
gegenseite:
  name: ""
  anwalt: ""
verfahren:
  art: ""
  gericht: ""
  az_gericht: ""
  verfahrensordnung: ""
streitwert: 0
anspruchsgrundlage: ""
risiko: "hoch / mittel / gering"
exposition_max: 0
verjährung: ""
außenanwalt: ""
status: "aktiv"
beweissicherung: false
angelegt: "TT.MM.JJJJ"
nächste_frist: "TT.MM.JJJJ"
```

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- BRAO § 43a Abs. 4 (Interessenkonflikt: Verbot der Vertretung widerstreitender Interessen).
- BGH, Urt. v. 26.09.2019 – IX ZR 315/18, NJW 2020, 224 Rn. 25 (Interessenkonflikt: Verletzung des Vertretungsverbots; Schadensersatzpflicht des Anwalts).
- Greger, in: Zöller, ZPO, 35. Aufl. 2024, §§ 12–37 Rn. 1 ff. (Gerichtszuständigkeit: sachlich, örtlich, funktionell).
- BGH, Urt. v. 22.11.2023 – VIII ZR 141/22, NJW 2024, 301 Rn. 14 (Streitwert bei mehreren Klageanträgen: Zusammenrechnung § 5 ZPO).

## Ausgabeformat

Interaktiver Dialog, dann automatisches Schreiben von `mandat.md`, `verlauf.md` (erster Eintrag: „Mandat aufgenommen, TT.MM.JJJJ") und Append in `_log.yaml`.

## Risiken / typische Fehler

- **Interessenkonflikt nicht erkannt:** § 43a Abs. 4 BRAO – bei Verstoß droht Schadensersatzpflicht des Anwalts (BGH – IX ZR 315/18) und berufsrechtliche Sanktionen (§§ 113 ff. BRAO).
- **Verjährung nicht geprüft:** Vor Intake stets Verjährungsablauf ermitteln; läuft die Verjährung in < 3 Monaten, sofort Hemmungsmaßnahmen (§ 204 BGB: Klageerhebung, Mahnbescheid) einleiten.
- **Zuständigkeit falsch:** Fehlerhafte sachliche Zuständigkeit führt zur Verweisung (§ 281 ZPO) und Zeitverlust; Streitwertgrenzen (AG: bis EUR 5.000; LG: ab EUR 5.001, § 23 Nr. 1 GVG) prüfen.
- **Mandant ist Verbraucher – besondere Pflichten:** Informationspflichten nach § 43d BRAO (Kostenmitteilung), § 13 RVG (Vergütungsvereinbarung).
