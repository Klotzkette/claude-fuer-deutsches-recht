---
name: dokumente-rendern-urteil-docx
description: "Für Urteil rendern - DOCX und PDF im Gerichtslayout: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Urteil rendern - DOCX und PDF im Gerichtslayout

Erzeugt aus strukturierten Markdown-Bausteinen ein lieferfertiges Urteil im Layout deutscher Amts- und Landgerichte.

## Triage zu Beginn

1. Welcher Dokumenttyp soll gerendert werden — Urteil, Versäumnisurteil oder Beschluss?
2. Welches Ausgabeformat — nur DOCX oder DOCX und PDF (LibreOffice soffice nötig)?
3. Sind alle Eingabedateien vorhanden (rubrum.yaml, tenor.md, tatbestand.md, entscheidungsgruende.md)?
4. Welche Tenor-Variante soll übernommen werden, wenn mehrere vorliegen?

## Zentrale Normen

- § 313 ZPO — Form und Inhalt des Urteils
- § 315 ZPO — Unterschrift der Richter
- § 317, 318 ZPO — Urteilszustellung und Bindungswirkung
- § 319 ZPO — Berichtigung offenbarer Unrichtigkeiten
- § 130b ZPO — elektronisches Dokument (beA-Signaturen)

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

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

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
