---
name: mahnschreiben-erhalten
description: "Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: §§ 286 287 BGB, §§ 203 204 BGB. Pruefraster: Forderungspruefung, Verjaebrungsrisiko, Verteidigungsoptionen. Output: Antwortschreiben auf Mahnschreiben. Abgrenzung: nicht Klageverteidigung."
---

# Eingehendes Mahnschreiben / Abmahnung – Triage

## Triage — kläre vor der Auswertung

1. **Schreibentyp:** Einfache Mahnung, Abmahnung (Wettbewerb/Urheberrecht), Forderungsschreiben eines Inkassos oder Klageankündigung?
2. **Frist:** Enthalt das Schreiben eine Zahlungsfrist oder Reaktionsfrist — wann läuft sie ab?
3. **Berechtigung:** Ist die behauptete Forderung dem Grunde und der Höhe nach berechtigt?
4. **Portfolio-Abgleich:** Liegt bereits ein Mandat oder ein Konflikt zu diesem Sachverhalt vor?
5. **Handlungspriorität:** Sofortige Reaktion (Unterlassung, Zahlung, Ablehnung) oder abwarten?

## Zentrale Normen
- § 286 BGB (Verzug durch Mahnung)
- § 203 BGB (Verjährungshemmung durch Verhandlungen)
- § 8 Abs. 1 UWG (Abmahnung im Wettbewerbsrecht)
- § 97a UrhG (Abmahnung im Urheberrecht)
- § 43a Abs. 1 BRAO (Interessenkonflikt bei eingehenden Forderungen)

## Rechtsprechung (ergänzt)
1. BGH, Urt. v. 17.07.2008 – I ZR 75/06, NJW 2008, 3711 Rn. 16 — Eine wirksame Mahnung setzt die Bestimmtheit der Forderung und den ernsthaften Erfüllungswillen des Gläubigers voraus; fehlt es daran, tritt kein Verzug ein.
2. BGH, Urt. v. 01.06.2006 – I ZR 167/03, GRUR 2007, 164 Rn. 12 — Eine Abmahnung im Wettbewerbsrecht muss die beanstandete Verletzungshandlung konkret bezeichnen; Pauschalabmahnungen sind unzulässig.
3. BGH, Urt. v. 25.10.2012 – I ZR 112/11, NJW 2013, 775 Rn. 19 — Verhandlungen hemmen die Verjährung nach § 203 BGB bereits bei bloßem Beantworten einer Forderung; ein ausdrückliches Verhandlungsangebot ist nicht erforderlich.
4. BGH, Urt. v. 14.01.2016 – I ZR 65/14, NJW 2016, 2269 — Die Reaktionsprüfung bei eingehenden Abmahnungen umfasst auch eine Interessenabwägung; eine sofortige Unterlassungserklärung kann Rechtsnachteile begründen.

## Kommentarliteratur
- Köhler/Bornkamm/Feddersen, UWG, 42. Aufl. 2024, § 8 Rn. 1 ff. (Abmahnung Wettbewerbsrecht).
- Grüneberg, BGB, 83. Aufl. 2024, § 286 Rn. 1 ff. (Verzug durch Mahnung).
- Wandtke/Bullinger, UrhG, 6. Aufl. 2022, § 97a Rn. 1 ff. (Abmahnung Urheberrecht).

## Zweck

Strukturierte Auswertung und Triage eingehender Mahnschreiben, Abmahnungen, Forderungsschreiben oder Klagedrohungen. Das Plugin extrahiert relevante Felder, prüft die Berechtigung der Forderung, gleicht mit dem Portfolio offener Mandate ab und erstellt eine priorisierte Handlungsübersicht mit Fristen.

## Eingaben

- Hochgeladenes oder einzufügendes Schreiben (Text, Scan, PDF)
- Optional: `--slug=custom-slug` für eigenes Aktenzeichen

## Ablauf

1. **Feldextraktion:**
   - Absender (Name, Kanzlei, Anschrift)
   - Empfänger (Mandant / Gesellschaft)
   - Datum des Schreibens
   - Aktenzeichen / Referenz des Absenders
   - Art des Schreibens (Mahnung, Abmahnung, Klagedrohung, Aufforderung zur Unterlassung, C&D-Äquivalent)
   - Geldforderung (Betrag, Währung, Fälligkeitsdatum)
   - Anspruchsgrundlage (soweit angegeben)
   - Gesetzte Frist (Datum extrahieren; wenn „2 Wochen ab Zugang" oder ähnlich: Frist anhand des Schreibdatums + Postlaufzeit schätzen)

2. **Portfolio-Abgleich:** Prüfen, ob zu Absender / Sachverhalt bereits ein Mandat in `mandate/_log.yaml` existiert. Wenn ja: Verknüpfung herstellen und History-Update vorschlagen.

3. **Berechtigungsprüfung (Kurzanalyse):**
   - Besteht das behauptete Schuldverhältnis dem Grunde nach?
   - Ist die Forderung bezifferbar und plausibel?
   - Sind Verjährungseinwände (§§ 195, 199 BGB) offensichtlich möglich?
   - Stehen Gegenansprüche (Aufrechnung § 387 BGB, Zurückbehaltungsrecht § 273 BGB) im Raum?
   - Besteht Verdacht auf unberechtigte Abmahnung (§ 8c UWG, § 97a Abs. 4 UrhG)?
   - Ist die Abmahnung formell vollständig (Unterlassungserklärung, Vertragsstrafe, Vollmacht)?

4. **Risikoeinschätzung:** Ampelschema:
   - 🔴 Hohe Berechtigung / akute Frist – sofortiger Handlungsbedarf
   - 🟡 Mittlere Berechtigung / prüfungsbedürftig
   - 🟢 Geringe Berechtigung / defensiv haltbar

5. **Handlungsoptionen mit Empfehlung:**
   - (a) Zahlung / Erfüllung (mit Vorbehalten)
   - (b) Modifizierte Unterlassungserklärung (bei Abmahnung)
   - (c) Abwehr / Zurückweisung mit Begründung
   - (d) Verhandlung / Vergleichsgespräch
   - (e) Schutzschrift hinterlegen (§ 945a ZPO) bei Gefahr einstweiliger Verfügung
   - (f) Mandat-Intake → neues Mandat anlegen

6. **Fristen-Alarm:**
   - Antwortfrist aus Schreiben extrahieren und als absolute Frist eintragen
   - Verjährungshemmung durch Verhandlung (§ 203 BGB) oder Mahnbescheid (§ 204 Abs. 1 Nr. 3 BGB) als Optionen nennen

7. **Datei speichern:** `inbound/[JJJJ-MM-TT]-[slug].md`

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- BGH, Urt. v. 17.07.2008 – I ZR 75/06, NJW 2008, 3711 Rn. 16 (Formvoraussetzungen der Mahnung).
- BGH, Urt. v. 01.06.2006 – I ZR 167/03, GRUR 2007, 164 Rn. 12 – „Telefax-Flatrate" (Anforderungen an Abmahnung im Wettbewerbsrecht).
- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, § 8c Rn. 5 ff. (missbräuchliche Abmahnung).
- BGH, Urt. v. 25.10.2012 – I ZR 112/11, NJW 2013, 775 Rn. 19 (Verjährungshemmung durch Verhandlungen, § 203 BGB).
- Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 945a Rn. 1 ff. (Schutzschrift, Hinterlegung im ZSSR).

## Ausgabeformat

```
EINGEHENDES SCHREIBEN – TRIAGE-BERICHT
Slug: [automatisch generiert]
Datum Eingang: TT.MM.JJJJ
Absender: [Kanzlei / Gläubiger]
Art: [Mahnung | Abmahnung | Klagedrohung]

──────────────────────────────────────
KERNFELDER
──────────────────────────────────────
Forderungsbetrag:   EUR X.XXX,XX
Anspruchsgrundlage: § 280 Abs. 1, 3, § 281 BGB
Frist gesetzt bis:  TT.MM.JJJJ
Konsequenz:         Klageandrohung

──────────────────────────────────────
RISIKOEINSCHÄTZUNG: 🟡 MITTEL
──────────────────────────────────────
Begründung: Forderung dem Grunde nach plausibel;
Zugang der Fristsetzung unklar; Verjährung prüfen.

──────────────────────────────────────
HANDLUNGSOPTIONEN
──────────────────────────────────────
Empfehlung: (c) Abwehr – fehlender Verjährungsverzicht
Alternativen: (d) Verhandlung, (e) Schutzschrift

──────────────────────────────────────
FRISTEN
──────────────────────────────────────
⚠️ Antwortfrist:       TT.MM.JJJJ
📅 Verjährungsende:    31.12.JJJJ (§§ 195, 199 BGB)
```

## Risiken / typische Fehler

- **Fristüberschreitung:** Bei Abmahnungen im UWG/UrhG ist die Frist oft sehr kurz (3–10 Tage); plug-in markiert Schreiben mit kurzem Frist-Alert.
- **Schutzschrift vergessen:** Bei drohender einstweiliger Verfügung (z. B. Wettbewerbsrecht, Markenrecht) sofortige Schutzschrift-Hinterlegung im Zentralen Schutzschriftenregister (ZSSR, § 945a ZPO) erwägen.
- **Kostenfalle § 93 ZPO:** Wenn Berechtigung klar, Zahlung / Unterlassungserklärung vor Klagezustellung prüfen; sonst trägt Beklagter Kosten trotz sofortigem Anerkenntnis.
- **Unvollständige Vollmacht:** Abmahnung ohne beigefügte Vollmacht ist zurückweisbar (§ 174 BGB); Zurückweisung unverzüglich erklären.
