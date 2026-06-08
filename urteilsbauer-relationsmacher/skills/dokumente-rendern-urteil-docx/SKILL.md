---
name: dokumente-rendern-urteil-docx
description: "Zivilurteil als DOCX im offiziellen Gerichtslayout rendern: Richter oder Referendar will fertiges Urteil als Dokument ausgeben. Normen: § 313 ZPO (Urteilsinhalt und -form). Prüfraster: Gerichtslayout (Aktenzeichen, Gerichtsbezeichnung, IM NAMEN DES VOLKES), Parteien, Anwaelte, Spruchkoerper, Tenor, Tatbestand, Entscheidungsgründe, Rechtsmittelbelehrung, Unterschriftenzeile. Output DOCX-Datei (und optional PDF) nach deutschem Gerichtsstandard. Abgrenzung: Inhalt des Urteils schreiben siehe entscheidungsgründe-zivil-schreiben, tatbestand-zivil-schreiben; Tenor siehe tenor-bauen-zivil."
---

# Urteil rendern - DOCX und PDF im Gerichtslayout

Erzeugt aus strukturierten Markdown-Bausteinen ein lieferfertiges Urteil im Layout deutscher Amts- und Landgerichte.

## Triage zu Beginn

1. Welcher Dokumenttyp soll gerendert werden — Urteil, Versäumnisurteil oder Beschluss?
2. Welches Ausgabeformat — nur DOCX oder DOCX und PDF (LibreOffice soffice nötig)?
3. Sind alle Eingabedateien vorhanden (rubrum.yaml, tenor.md, tatbestand.md, entscheidungsgruende.md)?
4. Welche Tenor-Variante soll übernommen werden, wenn mehrere vorliegen?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 313 ZPO — Form und Inhalt des Urteils
- § 315 ZPO — Unterschrift der Richter
- § 317, 318 ZPO — Urteilszustellung und Bindungswirkung
- § 319 ZPO — Berichtigung offenbarer Unrichtigkeiten
- § 130b ZPO — elektronisches Dokument (beA-Signaturen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

Vor dem Rendern muss der den Nutzer fragen:

1. **Dokumenttyp** Urteil oder Versäumnisurteil oder Beschluss (oder Relations-Dokument im Schul-Layout)?
2. **Ausgabeformat** DOCX oder DOCX und PDF?
3. **Tenor-Variante** wenn aus der Relation drei Varianten vorliegen welche soll übernommen werden?

## Eingabeschema

Der Eingabeordner enthält:

```
projekt/
 rubrum.yaml # Aktenzeichen, Gericht, Verkuendungsdatum, letzte muendliche Verhandlung, Spruchkoerper, Parteien, Anwaelte
 tenor.md # nummerierte Liste 1) 2) 3) ...
 tatbestand.md
 entscheidungsgruende.md
 rechtsmittelbelehrung.md # optional, wenn fehlt nimmt das Skript die Standardberufungsformel
```

## Aufrufbeispiel

```bash
### Vollurteil
python3 urteilsbauer-relationsmacher/skills/dokumente-rendern-urteil-docx/assets/render_urteil.py \
 testakten/solis-vision-x-smartglasses/output \
 testakten/solis-vision-x-smartglasses/output/urteil.docx \
 --typ urteil --pdf

### Versaeumnisurteil (ohne Tatbestand und Gruende)
python3 .../render_urteil.py eingabe ausgabe.docx --typ versaeumnis

### Beschluss
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

<!-- AUDIT 27.05.2026 | bundle_053
Geprüft: BGH VI ZR 559/16 (NOT_FOUND auf dejure.org)
Ersatz: BGH I ZR 90/14, GRUR 2016, 860 (verifiziert auf dejure.org)
Thema: § 315 ZPO Verhinderungsgrund Richterunterschrift — thematisch passend
Hinweis: BGH V ZB 68/19 (NJW 2020, 3661) in derselben Sektion ebenfalls NOT_FOUND; nicht im Bundle-Scope, zur Nachprüfung vorgemerkt.
-->
