---
name: dokumente-rendern-urteil-docx
description: "Rendert ein vollstaendiges Zivilurteil als DOCX (und optional PDF via soffice) im offiziellen Gerichtslayout: Aktenzeichen oben rechts Gerichtsbezeichnung zentriert IM NAMEN DES VOLKES Urteil-Bezeichnung Parteien Anwaelte Spruchkoerper Verhandlungstermin Tenor mit Einrueckung Tatbestand Entscheidungsgruende Rechtsmittelbelehrung Unterschriftenzeile. Verwendet python-docx und die Vorlage assets render_urteil.py."
---

# Urteil rendern - DOCX und PDF im Gerichtslayout

Erzeugt aus strukturierten Markdown-Bausteinen ein lieferfertiges Urteil im Layout deutscher Amts- und Landgerichte.

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
