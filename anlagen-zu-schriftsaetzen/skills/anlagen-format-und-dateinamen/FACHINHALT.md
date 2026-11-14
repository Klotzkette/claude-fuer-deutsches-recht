---
name: anlagen-format-und-dateinamen
description: "Erzeugt gerichtstaugliche PDF- und Dateinamensprofile für Schriftsatz und Anlagen: trennt Bundesvorgaben von Berliner und nordrhein-westfälischen Empfehlungen, verwendet auf Wunsch einen strengen ASCII-Unterstrich-Standard, wahrt Längen- und Reihenfolgegrenzen und liefert eine vollständige Altname-Neuname-Liste ohne Nummernverlust."
---

# Anlagenformat und Dateinamen

## 1. Erst lesen, dann benennen

Lies Gerichtshinweis, bisherigen Nummernkreis, Schriftsatz und Dateibestand. Wenn das Gericht kein eigenes Profil vorgibt, verwende den strengen Standard mit ASCII, Unterstrichen, maximal 60 Zeichen und führender Dateifolge. Weise aus, dass dies Kanzleistandard und nicht die Grenze des Bundesrechts ist.

## 2. Verifizierte Profile

| Profil | Kernaussage | Muster |
| --- | --- | --- |
| Bund nach ERVB 2025 | maximal 90 Zeichen einschließlich Endung; Umlaute und Eszett sind zulässig | `01_Anlage_K1_Kaufvertrag.pdf` |
| Berlin | jede Komponente eigene Datei; Hauptdokument `00`, Anlagen ab `01`; Datum und Kurzinhalt; maximal 60 Zeichen; keine Umlaute oder Sonderzeichen | `01_20260710_AnlageK1_Kaufvertrag.pdf` |
| NRW | Rolle nur beim Hauptdokument; sprechende gerichtliche Dokumenttypen; Anlagen neutral fortlaufend | `K_Schriftsatz_mit_Antraegen.pdf`, `Anlage_01.pdf` |
| Gerichtssicher | strengster gemeinsamer Arbeitsstandard: ASCII, Unterstrich, maximal 60 Zeichen, führende Reihenfolge | `02_20260710_AnlageK2_Mahnung.pdf` |

Quellen und Links stehen in `references/BEA-ENDPRODUKTION-RECHT-TECHNIK.md` und maschinenlesbar in `assets/dateinamensprofile.json`.

## 3. Umbenennungsmatrix

| Anlage | bisheriger Name | neuer Name | Zeichen | Beweisthema | Freigabe |
| --- | --- | --- | --- | --- | --- |
| K 1 | Originaldatei | `01_20260710_AnlageK1_Kaufvertrag.pdf` | Zahl | Vertragsschluss | offen oder frei |

Der Dateiname bleibt sprechend, aber knapp. Keine Mandantennamen, Gesundheitsdaten oder unnötigen Geschäftsgeheimnisse in Dateinamen aufnehmen.

## 4. Formatcheck

1. Jede einzureichende Anlage als eigene PDF.
2. Keine Verschlüsselung, eingebetteten Dateien oder aktiven Skripte.
3. Scan lesbar und sinnvoll durchsuchbar; OCR verändert das sichtbare Originalbild nicht.
4. Tabellen und Präsentationen nach Konvertierung auf abgeschnittene Inhalte prüfen.
5. PDF/A nur nach technischer Validierung bestätigen.
6. Dateiname, Stempel, Schriftsatzbezug und Anlagenverzeichnis stimmen überein.

## 5. Rechtsprechungsanker

BVerfG, Beschluss vom 16. Februar 2023, 1 BvR 1881/21, betrifft eine ältere Rechtslage ohne ausdrückliche Dateinamensgrenze. Die Entscheidung schützt eine damals technisch ordnungsgemäße Einreichung vor einer nicht normierten Zusatzanforderung, hebt aber die spätere 90-Zeichen-Regel der ERVB nicht auf.

## 6. Output

Liefere Profilentscheidung mit Quelle, vollständige Umbenennungsmatrix, Konvertierungsliste und Stop-Fehler. Bei bevorstehendem Versand direkt in `bea-versandmappe-endfertigung` weiterarbeiten.
