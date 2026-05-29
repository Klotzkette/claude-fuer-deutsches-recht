---
name: mahnschreiben-entwurf
description: "Vorgerichtliches Mahnschreiben entwerfen: Zahlungsaufforderung mit Frist und Klageankündigung. Normen: §§ 286 288 BGB, §§ 204 ff. BGB. Prüfraster: Verjaebrungshemmung, Verzugsbeginn, Schadensersatz, Klageandrohung. Output: Mahnschreiben-Entwurf mit Fristsetzung. Abgrenzung: nicht Mahnbescheid (gerichtliches Verfahren)."
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
   - Fristsetzung: Konkretes Datum (nicht "binnen 14 Tagen", sondern "bis zum [TT.MM.JJJJ]")
   - Konsequenzen: Klageandrohung, Kostenfolge (§§ 91 ZPO, 93 ZPO bei Anerkenntnisklage beachten)
   - Grußformel, Unterschrift

4. **Post-Send-Checkliste:**
   - Zugangsdokumentation (Einschreiben / Fax / gerichtliche Zustellung) planen
   - Frist in Kanzleifristbuch eintragen
   - Mandats-History-Update (`/mandat-update [slug] Mahnschreiben versandt`)

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 93 ZPO (sofortiges Anerkenntnis):** Wird der Schuldner sofort klaglos, trägt der Kläger die Kosten; Mahnschreiben vorher immer prüfen, ob es bereits eine wirksame Mahnung gab.
- **Unterlassung ohne Abmahnung:** Im UWG/UrhG/MarkenG ist die Abmahnung (mit Unterlassungsaufforderung und Vertragsstrafe) zwingende Voraussetzung; ohne Abmahnung keine Kostenerstattung (§ 97a Abs. 1 UrhG).
- **Güteantrag-Pflicht (§ 15a EGZPO):** In Bayern, Brandenburg, NRW und weiteren Ländern ist bei bestimmten Streitwerten ein Güteantrag vor Klageerhebung vorgeschrieben.
- **Fristberechnung:** Fristende nicht auf Sonn- oder Feiertag setzen (§ 193 BGB).
