---
name: mahnschreiben-entwurf
description: Entwurf eines anwaltlichen Mahnschreibens / einer vorgerichtlichen Aufforderung auf Basis eines abgeschlossenen Intakes – mit Fristsetzung nach § 286 BGB, Hinweis auf Klageandrohung und Checkliste für Mandatsgeheimnisschutz. Verwenden, wenn der Nutzer sagt „Entwurf Mahnschreiben", „schreib das Aufforderungsschreiben" oder das Mahnschreiben-Intake abgeschlossen ist.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - mahnschreiben
  - aufforderungsschreiben
  - mahnung entwerfen
  - verzugsschreiben
  - fristsetzung schreiben
---

# Mahnschreiben / Vorgerichtliche Aufforderung

## Zweck

Entwurf eines anwaltlichen Mahnschreibens (§ 286 Abs. 1 BGB) oder einer qualifizierten vorgerichtlichen Aufforderung mit Fristsetzung. Einsetzbar für Zahlungsverzug, Pflichtverletzungen, Mängelrügen (§ 281 Abs. 1 BGB) und Unterlassungsaufforderungen (§ 8 Abs. 1 UWG, § 97 Abs. 1 UrhG, § 14 Abs. 5 MarkenG). Das Schreiben ist anwaltlich unterzeichnet und nach § 13 RVG abrechenbar.

## Eingaben

- Abgeschlossenes `mahnschreiben-aufnahme.md` im Mandatsordner (Slug)
- Gewünschter Schriftsatztyp: `--zahlungsverzug`, `--mängelrüge`, `--unterlassung`, `--schadensersatz`
- Optional: `--version=N` für Versionierung bei Überarbeitungen
- Optional: `--skip-gate` – Pflicht-Checkliste überspringen (nur mit expliziter Bestätigung)

## Ablauf

1. **Intake laden:** `demand-letters/[slug]/intake.md` einlesen. Fehlende Pflichtfelder als Fehler ausgeben; kein Entwurf ohne vollständigen Intake.

2. **Pflicht-Checkliste (Gate) – vor dem Entwurf:**
   - [ ] Ist die Forderung dem Grunde nach schlüssig dargetan (§ 286 Abs. 1 BGB)?
   - [ ] Ist der Schuldner eindeutig identifiziert (Name, Anschrift, ggf. Handelsregisternummer)?
   - [ ] Ist der Betrag oder die geschuldete Handlung konkret bezeichnet?
   - [ ] Ist die Frist angemessen (i. d. R. 2 Wochen; bei Baurecht oder komplexen Leistungen ggf. länger)?
   - [ ] Sind Verzugsschäden (§ 288 BGB: 5 % über Basiszinssatz bei Verbrauchern; 9 % bei Unternehmen) korrekt beziffert?
   - [ ] Droht ein Güteantrag (§ 15a EGZPO) in bestimmten Bundesländern vor Klageerhebung?
   - [ ] Mandatsgeheimnis: Enthält das Schreiben keine vertraulichen Informationen Dritter?
   - [ ] FRE-408-Äquivalent (DE): § 278 Abs. 6 ZPO; Vergleichsangebote im Schreiben als solche kennzeichnen.

3. **Schreiben entwerfen:**
   - Briefkopf: Kanzlei, Datum, Aktenzeichen
   - Betreff: Mandant ./. Schuldner – [Kurzbezeichnung des Anspruchs]
   - Einleitung: Mandat und Vertretung
   - Sachverhalt: Knapp, tatsächlich, ohne rechtliche Wertungen
   - Forderung: Betrag / Handlung / Unterlassung, Rechtsgrundlage
   - Fristsetzung: Konkretes Datum (nicht „binnen 14 Tagen", sondern „bis zum [TT.MM.JJJJ]")
   - Konsequenzen: Klageandrohung, Kostenfolge (§§ 91 ZPO, 93 ZPO bei Anerkenntnisklage beachten)
   - Grußformel, Unterschrift

4. **Post-Send-Checkliste:**
   - Zugangsdokumentation (Einschreiben / Fax / gerichtliche Zustellung) planen
   - Frist in Kanzleifristbuch eintragen
   - Mandats-History-Update (`/mandat-update [slug] Mahnschreiben versandt`)

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- BGH, Urt. v. 17.07.2008 – I ZR 75/06, NJW 2008, 3711 Rn. 16 (Anforderungen an die Mahnung: Bestimmtheit der Forderung).
- BGH, Urt. v. 25.10.2007 – III ZR 91/07, NJW 2008, 435 Rn. 14 (Verzug ohne Mahnung bei kalendermäßig bestimmter Leistungszeit, § 286 Abs. 2 Nr. 1 BGB).
- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 286 Rn. 14 ff. (Form und Inhalt der Mahnung).
- Looschelders, in: Staudinger, BGB, Neubearb. 2022, § 286 Rn. 45 (Mahnung als einseitige empfangsbedürftige Willenserklärung).
- BGH, Urt. v. 14.07.2010 – VIII ZR 45/09, NJW 2010, 2944 Rn. 11 (Abmahnerfordernis im Kaufrecht vor Rücktritt).
- Zum Verzugszins: § 247 BGB (Basiszinssatz); § 288 Abs. 1, 2 BGB.

## Ausgabeformat

```
[KANZLEI-BRIEFKOPF]

An: [Name und Anschrift Schuldner]
Datum: TT.MM.JJJJ
Aktenzeichen: [Kanzleiaktenzeichen]
Mandatsgeheimnis – § 43a Abs. 2 BRAO / § 203 StGB

Betreff: [Mandant] ./. [Schuldner] – Zahlungsaufforderung / Aufforderung zur Mängelbeseitigung

Sehr geehrte Damen und Herren,

wir vertreten [Mandant] und nehmen wie folgt Stellung:

I. Sachverhalt
...

II. Forderung
Wir fordern Sie auf, den Betrag von EUR [X.XXX,XX] bis spätestens zum [TT.MM.JJJJ] auf unser Anderkonto zu überweisen.

III. Hinweis auf Klage
Sollte die Zahlung nicht fristgerecht eingehen, sind wir angewiesen, unverzüglich Klage zu erheben und die uns entstehenden Kosten nach §§ 91, 788 ZPO gegen Sie geltend zu machen.

Mit freundlichen Grüßen
[Anwalt, Kanzlei]
```

Ausgabe als Markdown-Datei `demand-letters/[slug]/v[N].md`.

## Risiken / typische Fehler

- **Unkonkrete Fristsetzung:** „Unverzüglich" oder „sofort" löst keinen Verzug aus; es ist ein konkretes Datum zu nennen (BGH, Urt. v. 17.07.2008 – I ZR 75/06, NJW 2008, 3711 Rn. 16).
- **§ 93 ZPO (sofortiges Anerkenntnis):** Wird der Schuldner sofort klaglos, trägt der Kläger die Kosten; Mahnschreiben vorher immer prüfen, ob es bereits eine wirksame Mahnung gab.
- **Unterlassung ohne Abmahnung:** Im UWG/UrhG/MarkenG ist die Abmahnung (mit Unterlassungsaufforderung und Vertragsstrafe) zwingende Voraussetzung; ohne Abmahnung keine Kostenerstattung (§ 97a Abs. 1 UrhG).
- **Güteantrag-Pflicht (§ 15a EGZPO):** In Bayern, Brandenburg, NRW und weiteren Ländern ist bei bestimmten Streitwerten ein Güteantrag vor Klageerhebung vorgeschrieben.
- **Fristberechnung:** Fristende nicht auf Sonn- oder Feiertag setzen (§ 193 BGB).
