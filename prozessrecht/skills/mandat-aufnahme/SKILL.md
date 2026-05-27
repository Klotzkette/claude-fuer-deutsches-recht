---
name: mandat-aufnahme
description: "Prozessmandat aufnehmen: Sachverhalt erfassen, Zustaendigkeit pruefen, Klagekonzept skizzieren. Normen: §§ 253 261 ZPO, BRAO. Pruefraster: Sachverhaltserfassung, Anspruchsgrundlage, Zustaendigkeit, Kosten-Risiko-Analyse. Output: Mandatsaufnahme-Protokoll. Abgrenzung: nicht inhaltliche Klageschrift."
---

# Mandat-Intake

## Triage — kläre vor der Aufnahme

1. **Mandatstyp:** Klägerseite, Beklagtenseite, Beratungsmandat oder gemischtes Mandat?
2. **Interessenkonflikt:** Besteht ein Interessenkonflikt mit laufenden oder abgeschlossenen Mandaten (§ 43a Abs. 4 BRAO, § 3 BORA)?
3. **Verfahrensart:** Zivilverfahren, arbeitsgerichtliches Verfahren, Verwaltungsverfahren, Strafverfahren?
4. **Schlüsselfristen:** Gibt es laufende Fristen (Verjährung, Rechtsmittelfrist, Klagefrist) die sofort gesichert werden müssen?
5. **Außenmandat:** Wird ein Korrespondenzanwalt oder Fachanwalt benötigt?

## Zentrale Normen
- § 43a Abs. 4 BRAO (Interessenkonflikt — Vertretungsverbot)
- § 3 BORA (Interessenkonflikt — weitere Fallgruppen)
- § 49b BRAO (Vergütungsvereinbarung)
- § 204 BGB (Verjährungshemmung durch Klage)
- § 232 ff. ZPO (Fristen und Fristenberechnung)

## Rechtsprechung (ergänzt)
1. BGH, Urt. v. 26.09.2019 – IX ZR 315/18, NJW 2020, 224 Rn. 25 — Ein Interessenkonflikt nach § 43a Abs. 4 BRAO führt zur Schadensersatzpflicht des Anwalts gegenüber dem beschädigten Mandanten; der Anwalt muss das Mandat unverzüglich niederlegen.
2. BGH, Urt. v. 22.11.2023 – VIII ZR 141/22, NJW 2024, 301 Rn. 14 — Der Streitwert ist bei mehreren Klageanträgen nach § 5 ZPO zusammenzurechnen, soweit sie nicht denselben Gegenstand betreffen; bei Aufnahme muss der Streitwert vorsorglich bestimmt werden.
3. BGH, Urt. v. 22.04.2010 – IX ZR 160/09, NJW 2010, 2655 Rn. 12 — Anwaltliche Haftung bei versaeumter Frist setzt voraus, dass der Anwalt alle ihm zumutbaren Maßnahmen zur Fristensicherung unterlassen hat; eine Mandatsaufnahme ohne sofortigen Fristencheck ist sorgfaltswidrig.
4. BGH, Urt. v. 19.03.2020 – IX ZR 239/18, NJW 2020, 2034 — Die anwaltliche Beratungspflicht bei Mandatsaufnahme umfasst die Abschätzung des Prozessrisikos und die transparente Darlegung gegenüber dem Mandanten; fehlt die Risikoaufklärung, haftet der Anwalt.

## Kommentarliteratur
- Deckenbrock/Henssler, BRAO, 5. Aufl. 2021, § 43a Rn. 1 ff. (Interessenkonflikt).
- Mayer/Kroiber, RVG, 8. Aufl. 2022, § 49b Rn. 1 ff. (Vergütungsvereinbarung).
- Zöller/Feskorn, ZPO, 35. Aufl. 2024, § 232 Rn. 1 ff. (Fristen).

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
verjaehrung: ""
aussenanwalt: ""
status: "aktiv"
beweissicherung: false
angelegt: "TT.MM.JJJJ"
naechste_frist: "TT.MM.JJJJ"
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
- **Zuständigkeit falsch:** Fehlerhafte sachliche Zuständigkeit führt zur Verweisung (§ 281 ZPO) und Zeitverlust; Streitwertgrenzen (AG: bis EUR 10.000; LG: über EUR 10.000, § 23 Nr. 1 GVG i. d. F. seit 1.1.2026) prüfen.
- **Mandant ist Verbraucher – besondere Pflichten:** Informationspflichten nach § 43d BRAO (Kostenmitteilung), § 13 RVG (Vergütungsvereinbarung).
