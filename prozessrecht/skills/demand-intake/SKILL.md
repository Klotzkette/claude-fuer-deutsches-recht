---
name: mahnschreiben-intake
description: Vorbereitende Informationserhebung für ein Mahnschreiben oder eine vorgerichtliche Aufforderung – Parteien, Sachverhalt, Anspruchsgrundlage, Forderungsbetrag, BATNA und Vertraulichkeitsfilter – wird als strukturierte intake.md gespeichert, auf die der mahnschreiben-Skill zugreift. Verwenden, wenn der Nutzer ein Mahnschreiben vorbereiten, einen Intake vor dem Entwurf durchführen oder Kontext für eine Zahlungsaufforderung, Mängelrüge oder Abmahnung erfassen möchte.
language: de
triggers:
  - "mahnschreiben-intake"
  - "intake mahnschreiben"
  - "vorbereitung mahnung"
  - "mahnung vorbereiten"
  - "forderung erfassen"
---

# Mahnschreiben-Intake

## Zweck

Strukturierte Erfassung aller für ein Mahnschreiben oder eine vorgerichtliche Aufforderung notwendigen Informationen, bevor der Entwurf erstellt wird. Der Skill führt ein geordnetes Interview und schreibt die Antworten in `demand-letters/[slug]/intake.md`.

## Eingaben

- Neuer Slug oder vorhandenes Mandat (Slug)
- Optional: `--full` für vollständigen erweiterten Intake (inkl. BATNA, Prozesskostenrisiko, Streitwertschätzung)

## Ablauf

1. **Mandantenidentifikation:**
   - Vollständiger Name / Firma, Anschrift, Kontaktperson
   - Mandantentyp: Verbraucher (§ 13 BGB) oder Unternehmer (§ 14 BGB) – für Verzugszinsberechnung relevant (§ 288 Abs. 1 vs. 2 BGB)

2. **Schuldneridentifikation:**
   - Vollständiger Name / Firma, Anschrift, HRB-Nummer (bei Gesellschaften)
   - Zustellungsfähige Anschrift vorhanden? (für spätere Klagezustellung, § 253 Abs. 2 Nr. 1 ZPO)
   - Ist die Passivlegitimation des Schuldners geklärt? (z. B. bei Gesamtschuld § 421 BGB, Rechtsnachfolge, Konzernmutter)

3. **Sachverhaltserfassung:**
   - Wie kam das Schuldverhältnis zustande? (Vertragsurkunde vorhanden?)
   - Was wurde nicht geleistet oder schlecht geleistet?
   - Wann war Leistung fällig?
   - Hat der Mandant bereits gemahnt? (schriftlich / mündlich / konkludent – relevant für § 286 Abs. 1 BGB)
   - Gab es Reaktionen des Schuldners (Einwände, Aufrechnungen, Minderung)?

4. **Forderungserfassung:**
   - Hauptforderung (Betrag, Art, Rechtsgrundlage)
   - Nebenforderungen: Verzugszinsen (§ 288 BGB), vorgerichtliche Anwaltskosten (§ 13 RVG i. V. m. VV 2300), Schadensersatz (§§ 280, 281 BGB)
   - Fälligkeitsdatum und bisherige Mahnungen (mit Datum)
   - Offene Restforderung (nach Teilzahlungen)

5. **Hebel und Risiko (BATNA):**
   - Was ist die beste Alternative des Mandanten ohne Mahnschreiben?
   - Welche Risiken bestehen (Aufrechnung, Gegenansprüche, Insolvenzrisiko)?
   - Ist ein Güteantrag (§ 15a EGZPO) im zuständigen Bundesland Pflicht?
   - Empfiehlt sich ein Mahnbescheid (§§ 688 ff. ZPO) statt Mahnschreiben?

6. **Vertraulichkeitsfilter:**
   - Enthält der Sachverhalt vertrauliche Informationen Dritter, die nicht in das Schreiben dürfen?
   - Besteht Zeugnisverweigerungsrecht des Mandanten für bestimmte Tatsachen?

7. **Intake-Datei schreiben:** `demand-letters/[slug]/intake.md` mit allen Feldern befüllen. Fehlende Pflichtfelder markieren.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 286 Rn. 14 ff. (Mahnung: Bestimmtheit, Form, Empfangsbedürftigkeit).
- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 288 Rn. 1 ff. (Verzugszinsen: Höhe, Fälligkeit, Verbraucher vs. Unternehmer).
- BGH, Urt. v. 25.10.2007 – III ZR 91/07, NJW 2008, 435 Rn. 14 (Mahnungserfordernisse: Bestimmtheit und Ernsthaftigkeit).
- RVG § 13 i. V. m. VV 2300 (Geschäftsgebühr für vorgerichtliche Tätigkeit; Faktor 1,3 als Schwellenwert – BGH, Urt. v. 13.01.2011 – IX ZR 110/10, NJW 2011, 1603 Rn. 9).

## Ausgabeformat

```yaml
# demand-letters/[slug]/intake.md
mandant:
  name: ""
  typ: "Unternehmer / Verbraucher"
  anschrift: ""
schuldner:
  name: ""
  anschrift: ""
  hrb: ""
  passivlegitimation_geklaert: true/false
schuldverhaeltnis:
  entstehungsgrund: ""
  vertrag_vorhanden: true/false
  anlage: ""
forderung:
  art: ""
  hauptbetrag: 0.00
  faelligkeit: ""
  bisherige_mahnungen: []
  verzugszinsen_p_a: "5% / 9% über Basiszinssatz"
  anwaltskosten: 0.00
anspruchsgrundlage: ""
fristen_geplant:
  fristsetzung_bis: ""
batna: ""
risiken: []
gueteantrag_erforderlich: false
vertraulichkeit_geprüft: true
```

## Risiken / typische Fehler

- **Fehlende Passivlegitimation:** Bei GmbH-Schuldner Handelsregisterauszug abrufen; Insolvenzantrag prüfen (InsO § 17 ff.) – Mahnung an insolventen Schuldner ist sinnlos.
- **Gesamtschuldner übersehen:** Bei mehreren Schuldnern (§ 421 BGB) alle mahnen, um Verjährungshemmung (§ 213 BGB) zu bewirken.
- **Verjährung prüfen:** Intake prüft automatisch die Regelverjährung (§§ 195, 199 BGB: 3 Jahre zum 31.12.); kürzere Sonderfristen (§ 438 BGB: 2 Jahre für Mängelansprüche; § 548 BGB: 6 Monate für Vermieter; § 195 ff. BGB) gesondert markieren.
- **Unterlassungsaufforderung ohne Vertragsstrafe:** Abmahnungen nach UWG, UrhG, MarkenG müssen eine Unterlassungs- und Verpflichtungserklärung mit Vertragsstrafeversprechen enthalten; fehlt dies, kann der Abgemahnte eine nicht der Kostenfolge des § 97a UrhG entsprechende Erklärung abgeben.
