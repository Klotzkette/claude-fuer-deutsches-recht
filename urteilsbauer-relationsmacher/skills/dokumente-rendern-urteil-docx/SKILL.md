---
name: dokumente-rendern-urteil-docx
description: "Zivilurteil als DOCX im offiziellen Gerichtslayout rendern: Richter oder Referendar will fertiges Urteil als Dokument ausgeben. Normen: § 313 ZPO (Urteilsinhalt und -form). Pruefraster: Gerichtslayout (Aktenzeichen, Gerichtsbezeichnung, IM NAMEN DES VOLKES), Parteien, Anwaelte, Spruchkoerper, Tenor, Tatbestand, Entscheidungsgruende, Rechtsmittelbelehrung, Unterschriftenzeile. Output DOCX-Datei (und optional PDF) nach deutschem Gerichtsstandard. Abgrenzung: Inhalt des Urteils schreiben siehe entscheidungsgruende-zivil-schreiben, tatbestand-zivil-schreiben; Tenor siehe tenor-bauen-zivil."
---

# Urteil rendern - DOCX und PDF im Gerichtslayout

Erzeugt aus strukturierten Markdown-Bausteinen ein lieferfertiges Urteil im Layout deutscher Amts- und Landgerichte.


## Triage zu Beginn

1. Welcher Dokumenttyp soll gerendert werden — Urteil, Versäumnisurteil oder Beschluss?
2. Welches Ausgabeformat — nur DOCX oder DOCX und PDF (LibreOffice soffice nötig)?
3. Sind alle Eingabedateien vorhanden (rubrum.yaml, tenor.md, tatbestand.md, entscheidungsgruende.md)?
4. Welche Tenor-Variante soll übernommen werden, wenn mehrere vorliegen?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 12.06.2018 - VI ZR 559/16, NJW 2018, 2868 — Urteil muss von allen Richtern des Spruchkörpers unterschrieben sein, die an der Entscheidung mitgewirkt haben (§ 315 Abs. 1 ZPO); elektronische Signatur nach § 130b ZPO gleichwertig.
- BGH, Beschl. v. 10.07.2020 - V ZB 68/19, NJW 2020, 3661 — Fehlende Unterschrift eines Richters führt zu Nichtigkeit des Urteils; Heilung nur in engen Grenzen möglich.
- BGH, Urt. v. 27.03.2019 - IV ZR 76/18, NJW 2019, 1742 — Urteil muss Rubrum mit vollständigen Parteibezeichnungen enthalten; Fehler im Rubrum können per Berichtigungsbeschluss korrigiert werden (§ 319 ZPO).
- BVerfG, Beschl. v. 30.06.2014 - 1 BvR 2340/13, NJW 2014, 3219 — Formvorschriften für gerichtliche Entscheidungen sind aus Rechtssicherheitsgründen strikt einzuhalten.

## Zentrale Normen

- § 313 ZPO — Form und Inhalt des Urteils
- § 315 ZPO — Unterschrift der Richter
- § 317, 318 ZPO — Urteilszustellung und Bindungswirkung
- § 319 ZPO — Berichtigung offenbarer Unrichtigkeiten
- § 130b ZPO — elektronisches Dokument (beA-Signaturen)

## Kommentarliteratur

- Zöller/Heßler, ZPO, 35. Aufl. 2024, § 313 Rn. 1-30 (Urteilsinhalt)
- Thomas/Putzo, ZPO, 45. Aufl. 2024, § 315 Rn. 1-15 (Unterschrift)

## Schritt-für-Schritt-Workflow

1. **Wahlfragen stellen** (s. oben: Dokumenttyp, Format, Tenor-Variante).
2. **Eingabeordner prüfen:** Alle 5 Dateien vorhanden? rubrum.yaml valide?
3. **Render aufrufen:**
   ```bash
   python3 .../render_urteil.py eingabe/ ausgabe.docx --typ urteil --pdf
   ```
4. **Output prüfen:** Rubrum vollständig? Tenor nummeriert? Unterschriftenzeile vorhanden?
5. **PDF-Export:** Falls `soffice` verfügbar, PDF als zweite Datei.

## Output-Template

**Adressat:** Gericht / Gerichtsakte — Tonfall: formal-amtlich

Das gerenderte Urteil folgt dem Layout:
- DIN A4, Arial 11pt
- Gerichtsbezeichnung zentriert, Aktenzeichen oben rechts kursiv
- "Im Namen des Volkes" — "Urteil" zentriert fett
- Tenor nummeriert, eingerückt
- Tatbestand, Entscheidungsgründe, Rechtsmittelbelehrung, Unterschrift

## Wahlfrage vor dem Render - IMMER stellen

Vor dem Rendern muss der Workflow den Nutzer fragen:

1. **Dokumenttyp** Urteil oder Versäumnisurteil oder Beschluss (oder Relations-Dokument im Schul-Layout)?
2. **Ausgabeformat** DOCX oder DOCX und PDF?
3. **Tenor-Variante** wenn aus der Relation drei Varianten vorliegen welche soll übernommen werden?

## Eingabeschema

Der Eingabeordner enthält:

```
projekt/
  rubrum.yaml         # Aktenzeichen, Gericht, Verkuendungsdatum, letzte muendliche Verhandlung, Spruchkoerper, Parteien, Anwaelte
  tenor.md            # nummerierte Liste 1) 2) 3) ...
  tatbestand.md
  entscheidungsgruende.md
  rechtsmittelbelehrung.md   # optional, wenn fehlt nimmt das Skript die Standardberufungsformel
```

## Aufrufbeispiel

```bash
# Vollurteil
python3 urteilsbauer-relationsmacher/skills/dokumente-rendern-urteil-docx/assets/render_urteil.py \
  testakten/solis-vision-x-smartglasses/output \
  testakten/solis-vision-x-smartglasses/output/urteil.docx \
  --typ urteil --pdf

# Versaeumnisurteil (ohne Tatbestand und Gruende)
python3 .../render_urteil.py eingabe ausgabe.docx --typ versaeumnis

# Beschluss
python3 .../render_urteil.py eingabe ausgabe.docx --typ beschluss
```

Ausgabe: `Urteil-{Aktenzeichen}.docx` (und `.pdf` wenn `soffice` verfügbar).

## Layout

- Arial 11pt (gerichtsüblich)
- DIN A4, Rand: links 2.5 cm, rechts 2 cm, oben/unten 2 cm
- Aktenzeichen oben rechts kursiv klein
- Gerichtsbezeichnung zentriert fett
- "Im Namen des Volkes" zentriert
- "Urteil" zentriert fett
- Rubrum mit Parteien linksbuendig, Anträge eingerueckt
- "hat das Amtsgericht ... für Recht erkannt:" am Ende des Rubrums
- Tenor nummeriert 1) 2) 3) eingerueckt
- "Tatbestand" fett, dann Fliesstext
- "Entscheidungsgründe" fett, dann Fliesstext
- Rechtsmittelbelehrung mit Trennung
- Unterschriftenzeile (Richtername + Funktion)

## Voraussetzungen

`pip install python-docx pyyaml`. Für PDF: LibreOffice (`soffice`).
