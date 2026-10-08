---
name: 06-dateinamen-manifest-erzeugen
description: "Nach PDF-Prüfung oder bei langen, kryptischen oder ungeeigneten Dateinamen: benennt Schriftsatz und Anlagen kurz und sprechend. Verwendet den internen 80-Zeichen-Standard einschließlich Endung mit ASCII und genau einem Punkt vor pdf. Liefert geordnete Dateinamen und das interne Versandmanifest."
---

# Dateinamen und Versandmanifest erzeugen

## Zweck und Anwendungsfall

Dieser Skill erstellt aus den geprüften Arbeitskopien einen verständlichen Upload-Satz. Er benennt ausschließlich Ausgabekopien und ändert niemals die Quelldateien.

## Eingaben

- geprüfte PDFs aus Skill 05.
- Anlagenplan und Parteirolle.
- Hauptdokumenttyp, Kurzgegenstand, relevante Dokumentdaten.
- Quellenpfade und aktuelle Hashwerte.

## Ablauf / Checkliste

1. Reihenfolge festlegen: genau ein Hauptschriftsatz zuerst, Anlagen danach in Zitier-/Anlagenfolge. Präfixbreite für alle Dateien einheitlich nach Gesamtzahl wählen.
2. Hauptname bilden: `01_K_Replik_Mietrueckstand.pdf` oder entsprechende B-/Dokumenttyp-Fassung.
3. Anlagenname bilden: `02_Anlage_K07_Mietkonto_2026-07-10.pdf`.
4. Alle Wörter mit Unterstrich trennen. Leerzeichen und Satzzeichen entfernen beziehungsweise durch einen Unterstrich ersetzen.
5. Umlaute transliterieren: `ae`, `oe`, `ue`; `ß` wird `ss`.
6. Nur ASCII-Buchstaben, Ziffern, Unterstrich und Minus verwenden; genau ein Punkt trennt `.pdf`.
7. Gesamtlänge einschließlich `.pdf` auf höchstens 80 Zeichen begrenzen. Zuerst Füllwörter und interne IDs kürzen, niemals Anlagenrolle/-nummer oder wesentlichen Dokumenttyp verlieren.
8. Doppelte oder nur in Groß-/Kleinschreibung abweichende Zielnamen, widersprüchliche K-/B-Nummern und fehlende logische Reihenfolge rot markieren.
9. Dateien als neue Kopien nach `_bea_ausgabe/upload` schreiben.
10. Internes `versandmanifest.csv` nach der [Vorlage](../../templates/versandmanifest.csv) mit exakt derselben Spaltenreihenfolge erzeugen: Quelle, Ziel, Seiten, Bytes, SHA256, OCR, Kennzeichnung, Datenschutz und Status. Die Quellen-/Render-Zuordnung aus Skill 05 bleibt separat erhalten und verbindet jeden Ausgabehash mit genau einem geprüften Quellenstand.
11. Quellen nur als relative Pfade ohne `..`, Laufwerksbuchstaben, Rückwärtsschrägstrich oder tabellenaktive Präfixe eintragen. `bereit` ist nur bei grünem OCR-, Kennzeichnungs- und Datenschutzstatus zulässig.
12. Dateisystem und Manifest zeilenweise gegeneinander prüfen. Jede PDF muss genau einmal und in Präfixreihenfolge vorkommen; kein Eintrag darf ins Leere zeigen.

## Quellenpflicht

Der [Dateinamen- und Manifeststandard](../../references/dateinamen-und-manifest.md) ist vollständig anzuwenden. Die durchgängige Quellen-/Render-Kette folgt [Inhaltstreue und Renderabgleich](../../references/inhaltstreue-und-renderabgleich.md). Die amtliche 90-Zeichen-Grenze steht im [ERV-Versandstandard](../../references/erv-versandstandard.md); intern bleiben 80 Zeichen verbindlich. Die automatisierbaren Namens- und Manifeststopps stehen im [100-Punkte-Fehlerkatalog](../../references/100-punkte-fehlerkatalog.md). Keine Rechtsprechungsanker.

## Ausgabeformat

1. finaler Upload-Ordner mit logisch nummerierten Einzel-PDFs.
2. Umbenennungstabelle Quelle zu Ziel.
3. vollständiges `versandmanifest.csv`.
4. Längen-, Zeichen-, Reihenfolge- und Hashprüfung.
5. Übergabe an Skill 07.

Dateibezeichnungen und Abkürzungen werden verständlich erläutert. Ein Manifest mit fehlenden Hashes oder Platzhaltern ist nicht fertig.

## Beispiele

- `Mietvertrag Müller endgültig (unterschrieben).pdf` wird als Arbeitskopie `02_Anlage_K01_Mietvertrag_Unterschrieben.pdf` geführt.
- `Kontoauszug_01.07.2026.pdf` erhält nur einen Punkt vor `pdf`: `03_Anlage_K02_Kontoauszug_2026-07-01.pdf`.
- Zielname hat 86 Zeichen: Kurzgegenstand kürzen, nicht einfach die Dateiendung oder Anlagenummer abschneiden.
